---
title: "Auditar Entra ID de verdad: licencias, políticas y riesgo que nadie estaba mirando"
description: "Una auditoría de solo lectura de Entra ID que empezó con «tiene P2» y acabó con una brecha de licencias, administradores sin MFA y un ataque de password spray activo."
date: 2026-10-16
area: azure
owner: Luis Adán Muñoz
categories: [Identidad]
tags: [entra-id, conditional-access, id-protection, pim, mfa, microsoft-graph, powershell, licencias, auditoria]
repo:
last_review: 2026-10-16
---

La petición parecía sencilla: *"El cliente tiene Entra ID P2, revisa qué tiene activado y qué no, y qué le podemos proponer"*. Un tenant de Educación con decenas de miles de cuentas entre alumnos, profesorado y personal, varias marcas académicas conviviendo en el mismo directorio y años de historia administrativa encima.

Lo que salió de ahí no fue una lista de funcionalidades sin activar. Fue una brecha de licencias que hacía que las políticas de acceso condicional se aplicasen a usuarios que no tenían derecho a ellas, administradores globales de más, una cuenta break-glass protegida solo con un código por correo y, sobre todo, un ataque de *password spray* en curso con cientos de cuentas marcadas en riesgo que nadie estaba resolviendo.

En este post cuento cómo lo monté: los scripts, las fases, los errores que cometí por el camino y lo que aprendí de cada uno.

> Todos los nombres de cliente, dominios, cuentas e identificadores de tenant se han omitido. Las cifras se dan redondeadas o como orden de magnitud.

---

## La regla: solo lectura y cada afirmación con su fuente

Antes de escribir una sola línea me puse dos reglas:

1. **Solo lectura.** Ningún script cambia nada. Todo sale a CSV (delimitado por `;` para que Excel en español lo abra sin pelearse) y las conclusiones se sacan de ahí.
2. **Nada se afirma sin documentación oficial.** Cada hallazgo que iba al informe tenía que estar respaldado por Microsoft Learn. Y esto, como verás, me obligó a rectificar varias afirmaciones que "todo el mundo sabe" y que no eran exactamente así.

El trabajo se dividió en fases, una por script:

| Fase | Script | Qué responde |
|---|---|---|
| 1 | `Get-TenantLicenseInventory.ps1` | ¿Qué licencias hay y quién tiene **de verdad** P1/P2? |
| 2 | `Get-TenantIdentityProtection.ps1` | Acceso condicional, registro de MFA, roles privilegiados, exclusiones |
| 2b | `Get-TenantPerUserMfaState.ps1` | ¿Queda MFA heredado "por usuario"? |
| — | Consultas puntuales | ¿Se aplican las políticas sin licencia? ¿Qué pasa con el riesgo? |

Todo con **Microsoft Graph PowerShell SDK v2**, y en algún caso puntual llamando a `beta` cuando la propiedad que necesitaba solo existía allí.

---

## Fase 1: licencias, o por qué "tiene P2" no significa nada

### Licencia asignada no es licencia efectiva

El primer error habitual es contar SKUs. Un usuario puede tener asignado un SKU que incluye `AAD_PREMIUM` y tener ese plan de servicio **deshabilitado**. O tenerlo por grupo y además directo. O tenerlo en estado de error.

Por eso el script no mira solo `assignedLicenses`, sino también `licenseAssignmentStates` (origen directo o por grupo, estado, `disabledPlans`) y `assignedPlans`, y calcula para cada usuario si **efectivamente** tiene `AAD_PREMIUM` (P1) y `AAD_PREMIUM_P2` (P2):

```powershell
$hasPlan = {
    param($user, $servicePlanId)
    foreach ($state in @($user.LicenseAssignmentStates)) {
        if ($state.State -ne 'Active') { continue }
        $sku = $skuMap[$state.SkuId]
        if (-not $sku) { continue }
        $plan = $sku.ServicePlans | Where-Object ServicePlanId -eq $servicePlanId
        if ($plan -and ($state.DisabledPlans -notcontains $servicePlanId)) { return $true }
    }
    return $false
}
```

### El mundo EDU tiene sus propias trampas

En un tenant educativo la mayoría de alumnos y buena parte del personal están en los SKUs gratuitos **A1** (`STANDARDWOFFPACK_STUDENT` / `STANDARDWOFFPACK_FACULTY`), que **no incluyen Entra ID P1**. Y ojo con un clásico: **Office 365 A3** (`ENTERPRISEPACKPLUS_FACULTY`) tampoco trae P1; es **Microsoft 365 A3** el que lo trae.

Además, hay que vigilar el **Student Use Benefit** (`M365EDU_A3_STUUSEBNFT`), que sí incluye P1 y suele estar infrautilizado.

El resultado en este tenant: la inmensa mayoría de cuentas sin P1, y **solo dos licencias P2**. El "tiene P2" de la petición inicial era técnicamente cierto, pero para dos personas.

### Errores de licencia por grupo

El inventario también destapó asignaciones fallidas por `MutuallyExclusiveViolation`: usuarios que reciben por grupo dos SKUs incompatibles. Para encontrar los grupos con miembros en error, mi primera versión pedía la propiedad directamente:

```powershell
# MAL: devuelve 400 "can only be used as a filter argument"
Get-MgGroup -GroupId $gid -Property 'id','displayName','hasMembersWithLicenseErrors'
```

`hasMembersWithLicenseErrors` **solo se puede usar como filtro**:

```powershell
$groupsWithErrors = Get-MgGroup -All -Filter 'hasMembersWithLicenseErrors eq true' -Property 'id','displayName'
```

### El primer fallo serio: un script que no sabía pararse

La primera ejecución canceló sin querer la autenticación interactiva justo en `Get-MgSubscribedSku`. El script mostró una advertencia… **y siguió**. Leyó decenas de miles de usuarios y exportó un inventario con **cero SKUs**. Un CSV perfectamente formado y completamente inútil.

Desde entonces, todos los scripts tienen precondiciones explícitas:

```powershell
$ctx = Get-MgContext
if (-not $ctx) { throw 'No hay sesión de Microsoft Graph. Ejecuta Connect-MgGraph primero.' }

$missing = $RequiredScopes | Where-Object { $ctx.Scopes -notcontains $_ }
if ($missing) { throw "Faltan scopes: $($missing -join ', ')" }

$skus = @(Get-MgSubscribedSku -All -ErrorAction Stop)
if ($skus.Count -eq 0) { throw 'No se han devuelto SKUs. Revisa tenant y permisos.' }
```

Si algo va mal, mejor que el script explote al principio a que produzca un informe falso al final.

---

## Fase 2: protección de identidad

El segundo script cruza acceso condicional, registro de métodos, roles y exclusiones. Exporta una docena de CSV, pero los hallazgos que importaban fueron estos.

### Alcance real del acceso condicional

Para cada política se resuelve a quién afecta realmente: usuarios y grupos incluidos, menos exclusiones, expandiendo membresías transitivas. Eso permite responder preguntas como "¿cuántas personas tienen MFA exigido en todas las aplicaciones?". La respuesta aquí fue incómoda: había políticas de MFA que cubrían a unas **doscientas** personas, pero solo **una treintena** lo tenían exigido para **todas** las aplicaciones. El resto, para un subconjunto.

### Brecha de licencias

Las políticas incluían a muchos usuarios **sin P1**. Microsoft lo deja claro: cada usuario que se beneficia de acceso condicional necesita P1, y las políticas basadas en riesgo necesitan P2. Volveré sobre esto en la fase 4, porque la pregunta "¿pero se aplican o no?" merece su propia sección.

### Administración privilegiada

- **13 Global Administrators** cuando Microsoft recomienda menos de cinco. Matiz importante que tuve que corregir en mi propio borrador: no eran 13 "activos", sino **4 permanentes y 9 elegibles en PIM**. Sigue siendo demasiado, pero la conversación con el cliente es distinta.
- Cuentas **deshabilitadas que seguían teniendo roles** asignados.
- Una cuenta **break-glass** cuyo único método era **código por correo electrónico**. La recomendación es al menos dos cuentas de emergencia, con métodos resistentes al phishing (FIDO2 o certificado) y excluidas de forma controlada y monitorizada.

Para clasificar los roles usé `isPrivileged`, que hoy solo está en `beta`:

```powershell
$roleDefs = Invoke-MgGraphRequest -Method GET `
  -Uri 'https://graph.microsoft.com/beta/roleManagement/directory/roleDefinitions?$select=id,displayName,isPrivileged' `
  -OutputType PSObject
```

Con un fallback a una lista de nombres por parámetro, porque `beta` puede cambiar y no quiero que el informe dependa de ello.

### Autenticación heredada y registro de MFA

El tenant tenía habilitados protocolos heredados y SMTP AUTH básico, que Microsoft está retirando. Y el porcentaje de usuarios **sin MFA registrado** era muy alto. Otra corrección de redacción: escribí "no tiene ningún método" y no era cierto; muchos tienen email o teléfono para SSPR, pero **no tienen MFA registrado**, que es lo que importa.

### El bug más tonto de PowerShell (otra vez)

Contando miembros de grupos me salía un usuario en grupos vacíos. El culpable:

```powershell
@($null).Count   # 1
```

Si una llamada devuelve `$null` y lo envuelves en `@()`, tienes un array con un elemento. Solución: una función que normaliza.

```powershell
function ConvertTo-Array {
    param($InputObject)
    if ($null -eq $InputObject) { return ,@() }
    return ,@($InputObject)
}
```

---

## Fase 2b: MFA por usuario, y el 403 que no era un 403

El MFA "por usuario" (el antiguo, el de la consola legacy) es un riesgo silencioso: convive mal con acceso condicional y Microsoft recomienda migrarlo. Se lee con:

```
GET https://graph.microsoft.com/beta/users/{id}/authentication/requirements
```

que devuelve `perUserMfaState` (`disabled`, `enabled`, `enforced`).

Con decenas de miles de usuarios no se puede llamar uno a uno. El script usa **JSON `$batch`** (20 peticiones por lote), gestiona **429 con `Retry-After`**, guarda un **checkpoint** cada N lotes y permite **reanudar** desde una carpeta anterior:

```powershell
$body = @{ requests = @(
    $chunk | ForEach-Object -Begin { $i = 0 } -Process {
        @{ id = "$i"; method = 'GET'; url = "/users/$($_.Id)/authentication/requirements" }
        $i++
    })
} | ConvertTo-Json -Depth 5

$resp = Invoke-MgGraphRequest -Method POST -Uri 'https://graph.microsoft.com/beta/$batch' -Body $body
foreach ($r in $resp.responses) {
    if ($r.status -eq 429) { $retry += $r; $wait = [int]$r.headers.'Retry-After' }
}
```

La primera pasada completa devolvió **403 en todos los lotes**. Horas de ejecución para nada. El motivo: el rol que necesitaba (Global Reader o Authentication Policy Administrator) estaba asignado **como elegible en PIM y no lo había activado** antes de conectar. El token solo lleva los roles **activos** en el momento de autenticarse.

Dos cambios:

- Activar el rol en PIM **antes** de `Connect-MgGraph` (y reconectar si ya había sesión).
- Un parámetro `-Max403Batches` (por defecto 3): si los primeros lotes devuelven 403, el script se para. *Fail fast*.

Resultado: MFA por usuario residual, pero presente, incluido en alguna cuenta administrativa.

---

## Fase 4: ¿se aplican las políticas a usuarios sin licencia?

Esta fue la pregunta que más discusión generó. La documentación dice que necesitas la licencia; no dice que la política *deje de aplicarse* si no la tienes. Y en este caso eso era justo lo relevante: si las políticas se aplicaban, el cliente estaba protegido *de facto* pero incumpliendo licenciamiento; si no, estaba desprotegido.

Mi primer intento de comprobarlo fue mirar `result` (`success` / `failure`) de las políticas en los inicios de sesión. Error: las políticas que no exigen nada en ese contexto aparecen como `notApplied`, y eso no distingue "no aplica por condiciones" de "no aplica por licencia".

Lo correcto es mirar en `beta` los campos `conditionsSatisfied` y `conditionsNotSatisfied` de `appliedConditionalAccessPolicies`:

```powershell
$si = Invoke-MgGraphRequest -Method GET `
  -Uri "https://graph.microsoft.com/beta/auditLogs/signIns/$signInId" -OutputType PSObject

$si.appliedConditionalAccessPolicies |
  Select-Object displayName, result, conditionsSatisfied, conditionsNotSatisfied
```

Sobre una muestra de algo menos de doscientos usuarios **solo con A1** (sin P1), las políticas se **evaluaban** y, cuando se cumplían las condiciones, se **aplicaban**. El motor no comprueba la licencia del usuario en tiempo de evaluación.

El contraste lo puso la política **gestionada por Microsoft** de inicio de sesión de riesgo: estaba limitada a un grupo creado automáticamente con exactamente **dos miembros**, el mismo número que licencias P2. Ahí Microsoft sí recorta el alcance a lo licenciado.

Conclusión para el informe: **protección real, pero en incumplimiento de licencias**, y con la política de riesgo cubriendo a dos personas en un tenant de decenas de miles.

---

## Fase 5: el riesgo que nadie miraba

Aquí la auditoría dejó de ser un ejercicio de cumplimiento.

### Detecciones premium en usuarios sin P2

Sin P2, la documentación indica que ves información de riesgo limitada. Pero al revisar las detecciones por usuario, cuentas con **solo A1** mostraban el **tipo real** de detección: `passwordSpray`, `maliciousIPAddress`, `anonymizedIPAddress`, `unfamiliarFeatures`, `unlikelyTravel`, `anomalousToken`. Algunas con decenas de detecciones; una con más de noventa.

La señal existe. Lo que no existe sin P2 es la **remediación automática** basada en políticas de riesgo.

### Un password spray en curso

El recuento de `riskyUsers` por estado y nivel dibujó el panorama:

| Estado | Orden de magnitud |
|---|---|
| `remediated` | Cientos |
| `dismissed` | Cientos |
| `atRisk` (bajo) | Cientos |
| `atRisk` (medio) | Cientos |
| `atRisk` (alto) | Decenas |

Ordenando por fecha de la última actualización de riesgo, había detecciones nuevas **cada pocas horas** el día de la consulta, con cuentas que habían tenido actividad de inicio de sesión minutos antes. Un ataque de *password spray* activo.

Y lo peor estaba en la cola de la lista: cuentas en riesgo **desde 2021** sin resolver, buzones funcionales (pagos, canal ético, marketing, calendario) en riesgo, una cuenta con rol de **User Administrator** en riesgo alto y **sin MFA registrado**, y tres cuentas en riesgo que además estaban **en el grupo de exclusión** de acceso condicional.

Un detalle que hay que entender bien: un usuario en riesgo que **no tiene MFA registrado** no puede autorremediar; si una política le exige MFA para resolver el riesgo, se queda bloqueado. Por eso la remediación tiene que ir de la mano de una campaña de registro.

### Propiedades que engañan

Para priorizar necesitaba saber si había habido acceso **real** después de la detección. Y aquí hay tres propiedades que es fácil leer mal:

| Propiedad | Lo que parece | Lo que es |
|---|---|---|
| `signInActivity.lastSignInDateTime` | Último acceso | Último **intento**, con éxito o fallido |
| `signInActivity.lastSuccessfulSignInDateTime` | — | Último acceso **con éxito** (sin datos anteriores a diciembre de 2023) |
| `riskyUser.riskLastUpdatedDateTime` | Desde cuándo está en riesgo | **Última actualización** del riesgo, no el inicio |

Y sobre `dismissed`: el `riskDetail` dice quién lo descartó (`adminDismissedAllRiskForUser` desde Entra, `m365DAdminDismissedDetection` desde Defender). No todo `dismissed` es "alguien de identidad lo revisó".

Consultar `signInActivity` usuario a usuario sobre cientos de cuentas acabó en **TooManyRequests** con reintentos agotados. La versión buena va en `$batch`, respeta `Retry-After`, convierte todo a UTC antes de comparar y marca como `SIN DATOS` lo que no se pudo leer en lugar de inventarlo.

---

## Un aviso que conviene meter en cualquier auditoría ahora

Microsoft ha anunciado la retirada de **SMS y voz** como métodos de autenticación, con **passkeys** como opción por defecto desde septiembre de 2026 y una retirada escalonada durante 2027. En un tenant donde buena parte del MFA registrado depende del teléfono, esto no es un detalle: es un proyecto. Conviene medir ya la dependencia de SMS por segmento y planificar la migración junto con la campaña de registro.

---

## Lo que aprendí por el camino

1. **Un script de auditoría que no falla al principio miente al final.** Precondiciones de sesión, scopes y datos mínimos, siempre. Y `-ErrorAction Stop` en las llamadas que no pueden fallar en silencio.
2. **PIM afecta a tu propio trabajo.** Si el rol es elegible y no lo activas antes de conectar, el token no lo lleva. Verifícalo antes de lanzar horas de ejecución, y para pronto si aparecen 403.
3. **Nunca dejes marcadores en los comandos.** Pasé comandos con `<fecha>` o `<UPN-de-prueba>` que se ejecutaron literalmente. Los comandos que entregues tienen que funcionar con copiar y pegar: autodetección de carpetas, búsqueda automática del usuario de prueba.
4. **"Necesita licencia" no es lo mismo que "no se aplica".** Compruébalo con `conditionsSatisfied` en los inicios de sesión, no con `result`.
5. **Lee la definición de cada propiedad.** `lastSignInDateTime` incluye fallos. `riskLastUpdatedDateTime` no es la fecha de inicio. Un informe que confunde esto saca conclusiones falsas.
6. **Matiza las cifras.** "13 Global Admins" y "4 permanentes y 9 elegibles" son el mismo dato, pero no la misma recomendación. "Sin método" y "sin MFA registrado" tampoco.
7. **El throttling es parte del diseño.** En tenants grandes, `$batch`, `Retry-After`, checkpoints y reanudación no son optimizaciones: son la única forma de terminar.

---

## Entregables

De todo esto salió:

- Tres scripts de solo lectura reutilizables, parametrizados y sin nada específico del cliente.
- Un informe técnico y ejecutivo con propuesta priorizada (P0 a P3), cada hallazgo respaldado por documentación de Microsoft Learn.
- Una presentación para dirección.
- Un anexo de evidencias con las cuentas concretas, que **no** se incluye aquí por razones obvias.

La propuesta, resumida: contener primero (cuentas en riesgo alto, exclusiones, administradores sin MFA), regularizar licencias después (P1 para quien está en el alcance de acceso condicional, P2 donde aporte), y luego reducir privilegios, migrar el MFA por usuario, retirar autenticación heredada y preparar la salida del SMS.

---

## Reflexión final

La mayoría de auditorías de identidad que veo se quedan en "estas funcionalidades no las tienes activadas". Es útil, pero se queda corto. Lo interesante aparece cuando cruzas datos: licencias con alcance de políticas, roles con métodos registrados, riesgo con exclusiones. Ahí es donde salen las cuentas que nadie estaba mirando.

Y para hacerlo bien hacen falta dos cosas que no tienen nada de sofisticado: scripts que fallen cuando deben y la disciplina de no afirmar nada que no puedas respaldar con la documentación oficial. En esta auditoría corregí varias frases mías por eso, y el informe salió mejor.

---

*Si tienes preguntas o quieres comentar algo de este post, escríbeme a luisadanmunoz@outlook.com.*

Revisado el 16 de octubre de 2026.
