---
title: "Auditar un tenant de Azure desde GitHub Actions… y que la remediación llegue como una PR"
description: "De una auditoría automatizada contra CIS, WAF y MCSB a un flujo de remediación como código: una PR por storage account, private endpoint propuesto por puntuación, identidades separadas y rollback."
date: 2026-10-29
area: azure
owner: Luis Adán Muñoz
categories: [Seguridad, DevOps]
tags: [azure, github-actions, oidc, prowler, psrule, maester, defender-for-cloud, azure-policy, private-endpoint, storage-account, remediacion]
repo:
last_review: 2026-10-29
---

La petición era sencilla de enunciar: **automatizar la revisión de un tenant de Azure contra las buenas prácticas del Well-Architected Framework, CIS y el resto de estándares habituales**, que detecte lo que está mal configurado o supone un riesgo, y que todo se lance desde GitHub.

Hay muchas herramientas que hacen parte de eso. Lo interesante vino después, cuando la conversación cambió de "dime qué está mal" a **"y ahora, ¿cómo lo arreglamos sin que nadie toque el portal a mano?"**. La idea era escalar hacia la autoremediación o, como mínimo, que cada problema llegase como una PR con el cambio propuesto. Empezamos por algo concreto: **hacer privados los storage accounts**.

En este post cuento cómo quedó la arquitectura, todo lo que falló en las primeras ejecuciones (que fue bastante) y por qué la parte más difícil no fue cambiar una propiedad en Azure, sino **decidir dónde crear el private endpoint**.

> El escenario es un tenant real de Azure con varias suscripciones, y un repositorio privado en una cuenta personal de GitHub (plan Free). No incluyo identificadores, nombres de recursos ni de proyectos reales. **La auditoría completa sí se ha ejecutado contra el tenant**, y también **una primera remediación de un storage account**. El resto de PRs de remediación está pendiente de revisión.

---

## La regla: quien audita no arregla

Desde el principio separé dos cosas que es tentador mezclar:

1. **La auditoría es de solo lectura.** Una identidad con `Reader` y `Security Reader` en el *Tenant Root Group* y permisos `*.Read.All` en Microsoft Graph. No puede cambiar nada aunque quisiera.
2. **La remediación es otra identidad, con otro rol y otro entorno de GitHub.** Solo puede actuar sobre storage accounts y sus private endpoints, y solo se usa después de que alguien haya aprobado el cambio.

Ninguna de las dos usa secretos: GitHub Actions se autentica en Entra ID mediante **OIDC (*workload identity federation*)**, y cada credencial federada está limitada a un entorno de GitHub concreto.

El objetivo inicial no es que el sistema corrija solo. Es que **cada cambio llegue con su justificación, su impacto y su vuelta atrás**, y que una persona lo apruebe.

---

## Qué revisa cada herramienta

No hay una herramienta que cubra todos los marcos, así que el workflow ejecuta cuatro en paralelo y un quinto job consolida los resultados:

| Motor | Qué revisa | Marco |
|---|---|---|
| **Prowler** | Suscripciones y Entra ID | CIS Azure Foundations, ISO 27001, ENS, NIST, PCI, DORA… |
| **PSRule for Azure** | Configuración real de cada recurso | Well-Architected Framework (los cinco pilares) |
| **Azure Resource Graph** | Recomendaciones de Defender for Cloud, cumplimiento normativo y estados de Azure Policy | Microsoft Cloud Security Benchmark y estándares asignados |
| **Maester** | Configuración de identidad | EIDSCA, CISA SCuBA, buenas prácticas de Entra ID |

```text
GitHub Actions (semanal o manual)
        |
        |  OIDC, sin secretos
        v
Microsoft Entra ID ── identidad de solo lectura
        |
        +── Reader + Security Reader en el Tenant Root Group
        +── Microsoft Graph *.Read.All
        |
        v
+-----------+-----------+------------------+-----------+
|  Prowler  |  PSRule   |  Resource Graph  |  Maester  |
+-----------+-----------+------------------+-----------+
                        |
                        v
            Consolidación y normalización
                        |
        +---------------+---------------+
        v               v               v
   findings.csv     Job summary    Issue con críticos/altos
```

El job de consolidación normaliza la severidad de las cuatro fuentes, elimina duplicados y mantiene **un único issue abierto** con los hallazgos críticos y altos, que se actualiza en cada ejecución y se cierra solo cuando ya no queda ninguno.

---

## La primera ejecución falló entera. La segunda, a medias

Me gusta contar esta parte porque es la que normalmente no aparece en los posts.

**Primer intento: todos los jobs fallaron al autenticarse.** El error era `AADSTS700213: No matching federated identity record found`. Había configurado la credencial federada con el *subject* clásico, `repo:<owner>/<repo>:environment:<env>`. El repositorio, recién creado, usaba el formato nuevo de GitHub con **IDs inmutables**: `repo:<owner>@<id>/<repo>@<id>:environment:<env>`. El script de inicialización ahora lee el prefijo correcto desde la API de GitHub en lugar de suponerlo.

**Segundo intento: todo en verde, pero con números que no se sostenían.**

| Fuente | Lo que vi | Lo que pasaba realmente |
|---|---|---|
| Prowler | 2.636 hallazgos | Leía también los informes por marco normativo, que repiten cada hallazgo una vez por estándar (CIS, DORA, CMMC…). Sin duplicados: **317**. |
| PSRule | 0 hallazgos | Exportaba los recursos en 45 segundos y los "evaluaba" en uno. No estaba leyendo la entrada. |
| Defender for Cloud | 0 hallazgos | Correcto: el tenant no tenía evaluaciones. Lo confirmé consultando Resource Graph directamente. |
| Maester | Job fallido | Pester devuelve error cuando hay tests que no pasan. Los 40 hallazgos sí se habían recogido. |

El caso de PSRule es el que más me preocupa en retrospectiva: **un cero es el resultado más peligroso que puede dar una auditoría**, porque se parece mucho a "todo cumple". Ahora el job falla explícitamente si PSRule no evalúa ningún objeto. Con el formato de entrada corregido, aparecieron **189 incumplimientos** del WAF.

El resultado consolidado de la tercera ejecución:

| Fuente | Crítico | Alto | Medio | Bajo | Total |
|---|---:|---:|---:|---:|---:|
| Prowler (CIS) | 1 | 153 | 150 | 13 | 317 |
| PSRule (WAF) | 15 | 136 | 38 | 0 | 189 |
| Azure Policy | 0 | 0 | 129 | 0 | 129 |
| Maester (Entra ID) | 0 | 20 | 19 | 1 | 40 |

Entre lo más relevante: usuarios con privilegios sin MFA, container registries públicos, ausencia de flow logs y de alertas sobre cambios en NSG y políticas, y **nueve storage accounts accesibles desde Internet**.

---

## Remediación como código

Para la remediación descarté desde el principio dos opciones:

- **Scripts que corrigen directamente.** Rápido, pero sin revisión ni trazabilidad.
- **Azure Policy con `Modify` desde el primer día.** Es la herramienta correcta para *prevenir*, pero aplicada sobre un inventario sin sanear cambia cosas en producción sin que nadie haya mirado el impacto.

El flujo que monté es este:

```text
plan.yml (identidad de solo lectura)
        |
        |  Resource Graph: storage accounts, subnets, zonas DNS
        v
remediations/storage/<cuenta>-<fecha>-plan.json
        |
        v
Una PR por storage account
        |
        |  revisión + merge
        v
apply.yml (environment azure-remediation)
        |
        |  identidad con rol custom limitado
        v
Private endpoint + DNS  →  PATCH de la propiedad  →  verificación
```

El plan es un JSON versionado en el repositorio. Contiene el estado actual y el deseado de cada propiedad, y es lo que hace posible el rollback. Las salvaguardas que considero imprescindibles:

| Salvaguarda | Qué evita |
|---|---|
| **Comprobación de cambios desde el plan** | Si alguien modificó la cuenta después de generar el plan, el apply no toca esa propiedad (`Drift`). |
| **PATCH mínimo y verificación** | Solo se envían las propiedades del plan y se comprueba el valor después. |
| **Orden estricto** | Primero el private endpoint y su DNS; **solo si todo sale bien**, se desactiva el acceso público. |
| **Rollback** | Reactiva el acceso público y borra únicamente los private endpoints con la etiqueta `created-by=azure-tenant-audit`. |
| **Exclusiones** | Etiqueta `audit-remediation=exclude`, grupos de recursos gestionados por servicios (`MC_*`, Databricks…) y recursos gestionados por IaC. |

Este último punto merece una línea aparte: **si un recurso lo gestiona Terraform o Bicep, corregirlo por fuera solo genera *drift***. El siguiente `apply` lo revertiría. Esos casos aparecen como acción manual para corregirlos en el código.

---

## La primera remediación no propuso nada, y estaba bien

El primer plan revisó diez storage accounts y no generó ninguna PR. Al principio pareció un fallo, pero era el comportamiento correcto:

- Todas cumplían ya los controles fáciles: sin acceso anónimo, TLS 1.2 y solo HTTPS.
- Nueve tenían acceso público de red y **ningún private endpoint**.

Desactivar el acceso público sin private endpoint deja la cuenta inaccesible. La herramienta las había dejado como "acción manual"… **pero ese inventario solo se publicaba en el texto de la PR, y como no había PR, no se veía en ningún sitio.** Fue la primera pregunta del usuario: *"¿pero dónde veo los que no cumplen?"*.

Ahora cada ejecución publica siempre el inventario completo, en el resumen del job y como CSV descargable, haya PRs o no. Parece un detalle, pero **una herramienta que solo informa cuando actúa esconde justo lo que no sabe resolver**.

---

## Una PR por cuenta, y la PR propone dónde

La siguiente petición fue doble: **una PR por cada storage account**, y que **la propia PR propusiera dónde crear el private endpoint**, en lugar de pedir que alguien configurase subnets a mano.

La primera parte es mecánica: una rama `remediation/storage/<cuenta>` y un plan por cuenta, de forma que cada una se aprueba, rechaza o revierte por separado.

La segunda es la interesante. Un private endpoint sirve de poco si queda en una red desde la que no acceden los clientes de la cuenta. El plan analiza todas las subnets del tenant (no delegadas, no reservadas y con IPs libres) y las puntúa:

| Criterio | Puntos |
|---|---:|
| La VNet es del mismo proyecto que la cuenta (coincidencia de nombres de RG y VNet) | +30 a +40 |
| La VNet ya está enlazada a la zona `privatelink.blob` / la zona existe pero sin enlace | +20 / +10 |
| Misma región / misma suscripción | +15 / +10 |
| Subnet dedicada a private endpoints (`pe`, `private`, `endpoints`…) | +10 |
| Entorno distinto (dev ↔ pro) / red de producción para una cuenta sin entorno claro | −40 / −15 |

La PR muestra la propuesta con sus motivos, hasta dos alternativas y un **nivel de confianza**: *Alta* si la red es del mismo proyecto, *Media* si coinciden región y suscripción, *Baja* en otro caso. Para elegir otra opción basta con cambiar `"selectedOption"` en el JSON del plan dentro de la PR.

### La primera versión de la puntuación se equivocaba

Al ejecutarla contra el tenant real, **las nueve cuentas acababan propuestas en la misma subnet**, incluidas las de otro proyecto, otra suscripción y otra región. Había dos errores:

1. **"dev" contaba como proyecto compartido.** Es un entorno, no un proyecto.
2. **Pesaba más que la VNet ya tuviera DNS (+40) que ser del mismo proyecto (+5).** El DNS es cómodo, pero lo que decide si la cuenta sigue funcionando es dónde están sus clientes.

Con los pesos corregidos, una cuenta de estado de Terraform del proyecto de IA pasó a proponerse en la VNet de ese proyecto. Para las cuentas de un proyecto cuya VNet solo tiene una subnet delegada, la PR ahora lo dice explícitamente: *"la VNet del proyecto no tiene ninguna subnet utilizable; lo recomendable es crear una subnet para private endpoints"*. Y el título de la PR lleva *"revisar ubicación del PE"*.

**Una heurística que propone con seguridad un sitio equivocado es peor que una que dice "no lo sé"**. El nivel de confianza existe para eso.

---

## El primer merge falló, y la salvaguarda funcionó

La primera PR se mergeó antes de ampliar los permisos de la identidad de remediación, que todavía no podía gestionar private endpoints. El apply falló con un `403 AuthorizationFailed` al intentar leer el private endpoint.

Lo importante es lo que **no** pasó: al fallar el private endpoint, el acceso público no se desactivó. La cuenta siguió funcionando exactamente igual.

Ampliar el rol también tuvo su historia: `az role definition update` no acepta el mismo JSON que `create` y, además, **falla con roles custom definidos en un management group**. Acabé actualizándolo directamente contra la API de ARM. Con el rol corregido, relancé la misma ejecución sin tocar la PR ni el plan:

| Comprobación | Resultado |
|---|---|
| Acceso público de red | Desactivado |
| Private endpoint | Creado, conexión aprobada, etiqueta `created-by` |
| Registro DNS en `privatelink.blob.core.windows.net` | Apunta a la IP privada |

El rol final tiene diecisiete acciones, todas sobre `Microsoft.Storage/storageAccounts`, private endpoints, subnets y zonas DNS privadas. Ni `listKeys` ni acceso a datos.

---

## Lo que GitHub Free no permite

El diseño original contaba con **revisores obligatorios** en el entorno `azure-remediation`, como segunda aprobación antes de tocar Azure. En un repositorio privado de GitHub Free no está disponible, y tampoco las reglas de rama (*rulesets*) para obligar a pasar por PR.

Lo que sí funciona es limitar el entorno a la rama `main`, así que solo un workflow de `main` puede usar la identidad de escritura. Mientras haya una única persona con permiso de escritura, el merge de la PR es una aprobación razonable. Con más gente, haría falta GitHub Pro para las reglas de rama, o una organización con Enterprise para los revisores obligatorios.

---

## Lo que aprendí

1. **Un cero no es cumplimiento.** Si un motor evalúa cero objetos, el job tiene que fallar, no informar de que todo está bien.
2. **Los informes por marco normativo inflan los números.** El mismo hallazgo aparece una vez por estándar. Hay que leer la salida principal y quitar duplicados.
3. **El *subject* de OIDC no es siempre el que documenta todo el mundo.** Los repositorios nuevos pueden usar IDs inmutables; mejor leerlo de la API que suponerlo.
4. **La herramienta tiene que enseñar lo que no puede arreglar.** El inventario de "acciones manuales" es tan importante como las PRs.
5. **El orden de las operaciones es una salvaguarda.** Primero lo que añade acceso (private endpoint y DNS); después lo que lo quita.
6. **Proponer dónde es más difícil que cambiar una propiedad.** Y una propuesta con confianza baja debe decirlo en el título.
7. **Los recursos gestionados por IaC no se remedian por fuera.** Se corrigen en el código o se convierten en drift.
8. **Las herramientas oficiales también tienen huecos.** `az role definition update` con roles de management group es un buen ejemplo: la API de ARM sigue siendo el plan B.

---

## Próximos pasos

- **Revisar y mergear las PRs de confianza alta** y validar con los equipos que sus clientes acceden desde la VNet propuesta. Las cuentas de estado de Terraform necesitan antes runners dentro de la red.
- **Generar también la subnet** cuando la VNet del proyecto no tiene ninguna utilizable, calculando un rango libre, en lugar de solo recomendarlo.
- **Prevenir con Azure Policy**: una vez saneado el inventario, asignar en el Tenant Root Group las políticas integradas con `Deny` o `Modify` para que lo nuevo nazca conforme y las PRs queden para las excepciones.
- **Auto-merge solo para riesgo bajo** (TLS, HTTPS, acceso anónimo sin contenedores públicos), cuando el histórico dé confianza.
- **Extender el patrón** `remediations/<control>/` a Key Vault, SQL y NSG con puertos de administración abiertos.
- **Activar Defender for Cloud (Foundational CSPM)** para que la fuente de MCSB deje de estar vacía.

---

## Reflexión final

Auditar un tenant es, a estas alturas, un problema bastante resuelto: hay herramientas buenas y gratuitas que generan cientos de hallazgos en media hora. El cuello de botella no está en encontrar problemas, sino en **convertir cada hallazgo en un cambio que alguien se atreva a aprobar**.

Para eso, la PR resulta un formato muy natural: explica qué se va a cambiar, por qué, qué se puede romper, dónde se propone hacerlo y cómo se vuelve atrás. Y deja un rastro en Git de cada decisión.

El orden que no quiero invertir es el mismo de siempre: primero ver, luego proponer y, solo cuando lo propuesto acierte de forma consistente, dejar que algo se aplique solo. Una remediación que se equivoca dentro de una PR es una conversación. Una que se equivoca aplicándose sola es una incidencia.

---

## Referencias

- [Prowler - Documentación](https://docs.prowler.com/)
- [PSRule for Azure](https://azure.github.io/PSRule.Rules.Azure/)
- [Maester](https://maester.dev/)
- [Microsoft Learn - Azure Resource Graph](https://learn.microsoft.com/en-us/azure/governance/resource-graph/overview)
- [Microsoft Learn - Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/)
- [Microsoft Learn - Workload identity federation](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation)
- [GitHub Docs - Configuring OpenID Connect in Azure](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-azure)
- [Microsoft Learn - Private endpoint DNS configuration](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns)

---

*Si tienes preguntas o quieres comentar algo de este post, escríbeme a luisadanmunoz@outlook.com.*

Revisado el 29 de octubre de 2026.
