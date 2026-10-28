---
title: "Azure DevOps ya tiene pipelines. ¿Y si ahora le añadimos agentes de IA con ado-aw?"
description: "De una pregunta sobre ado-aw a diseñar una plataforma de agentes de IA para una organización de Azure DevOps: arquitectura multiproyecto, MCP, permisos, un primer agente y 28 casos de uso."
date: 2026-10-27
area: azure
owner: Luis Adán Muñoz
categories: [DevOps, Inteligencia Artificial]
tags: [azure-devops, ado-aw, agentes-ia, mcp, github-copilot, azure-pipelines, entra-id, seguridad, automatizacion]
repo:
last_review: 2026-10-27
---

Todo empezó con un enlace: [Azure DevOps Agentic Workflows (`ado-aw`)](https://githubnext.github.io/ado-aw/setup/quick-start/). La documentación prometía algo que me llamó la atención: describir un agente de IA en Markdown y compilarlo a un pipeline de Azure DevOps.

Mi primera pregunta fue si era *open source*. Sí: el repositorio de GitHub Next es público y utiliza licencia MIT. Pero la pregunta interesante vino después: **¿qué utilidad tendría en una organización de Azure DevOps Services que ya funciona, con muchos proyectos, repositorios, pipelines, Boards y equipos trabajando sobre la misma plataforma?**

No quería crear otro pipeline de ejemplo para decir que había metido IA en DevOps. Quería saber si podía añadir una capa de análisis que aprovechase lo que el cliente ya tiene, sin cambiar sus procesos de despliegue ni empezar repartiendo permisos de escritura.

De esa conversación salieron una arquitectura de referencia, el diseño de un primer agente para analizar fallos de pipelines, una preparación de entorno, un plan de validación y un catálogo de **28 casos de uso**. En este post cuento las decisiones que tomé, dónde vi los riesgos y qué queda por demostrar.

> El escenario es Azure DevOps **Services (cloud)**, con múltiples proyectos dentro de **una sola organización**. No incluyo nombres, URLs ni identificadores reales. Los ejemplos de ejecución son ilustrativos: **todavía no he ejecutado el agente contra un entorno real del cliente**.

---

## La regla: aprovechar Azure DevOps, no sustituirlo

La situación de partida es bastante habitual. Una organización crece, se crean proyectos por aplicación o equipo y cada uno acaba teniendo sus propios repositorios, pipelines y formas de trabajar. Azure DevOps guarda los datos, pero extraer una conclusión transversal sigue siendo un trabajo muy manual.

Un equipo investiga un fallo de autenticación en un pipeline. Otro lleva días viendo errores intermitentes en una tarea de NuGet. Un tercero tiene work items bloqueados desde hace semanas. Y cuando alguien pregunta qué problemas se repiten en toda la organización, toca entrar en varios proyectos, abrir ejecuciones, revisar logs y construir un informe.

Me puse dos restricciones desde el principio:

1. **No tocar los pipelines productivos.** El primer agente debe funcionar como una ejecución independiente en un proyecto central.
2. **Solo lectura y conclusiones con evidencias.** Si el agente afirma que una service connection está fallando, quiero ver qué ejecución, qué tarea y qué línea del log respaldan esa hipótesis.

El objetivo inicial no es que la IA arregle nada. Es comprobar si **ayuda a diagnosticar mejor** y si lo hace con un modelo de seguridad aceptable para una organización real.

---

## Qué hace realmente ado-aw

`ado-aw` es un compilador y un framework de ejecución para *agentic workflows* en Azure DevOps. La idea es escribir la configuración y las instrucciones en un archivo Markdown y generar a partir de él un YAML de Azure Pipelines.

```text
Definición del agente (Markdown + YAML front matter)
                       |
                       v
                 ado-aw compile
                       |
                       v
              Pipeline .lock.yml
                       |
                       v
                 Azure Pipelines
                       |
              Agent -> Detection
                       |
                       v
                SafeOutputs
```

La separación entre etapas es importante:

| Etapa | Responsabilidad |
|---|---|
| `Agent` | Ejecutar el modelo y consultar las herramientas disponibles. |
| `Detection` | Analizar las acciones propuestas y aplicar controles antes de ejecutarlas. |
| `SafeOutputs` | Materializar determinadas acciones autorizadas mediante una identidad separada. |

Esto no convierte automáticamente en seguro cualquier workflow. Sigue habiendo que revisar qué herramientas puede llamar el agente, qué token tiene cada etapa y qué acciones de salida están configuradas. Pero ofrece una estructura bastante más interesante que un script que llama directamente a un modelo con un token de administrador.

El motor documentado es **GitHub Copilot CLI**. Aunque `ado-aw` sea MIT, eso no significa que la ejecución sea gratuita ni que el modelo sea open source: hay que considerar acceso a Copilot, capacidad de Azure Pipelines y, si corresponde, consumo de otro proveedor de IA.

Referencias: [Quick Start](https://githubnext.github.io/ado-aw/setup/quick-start/) y [configuración del motor](https://githubnext.github.io/ado-aw/reference/engine/).

---

## Primera decisión: un proyecto central, no un agente por proyecto

Con todos los proyectos dentro de la misma organización, podría instalar un workflow en cada repositorio. Es posible, pero no lo elegiría para empezar: dispersaría los permisos, las actualizaciones y la observabilidad.

Prefiero crear un proyecto específico —por ejemplo, `AI-DevOps-Platform`— desde el que ejecutar los agentes que consulten los demás proyectos autorizados.

```text
Azure DevOps Services - una organización
|
+-- Proyecto A
|   +-- Boards / Repos / Pipelines
|
+-- Proyecto B
|   +-- Boards / Repos / Pipelines
|
+-- Proyecto C
|   +-- Test Plans / Artifacts / Wiki
|
+-- AI-DevOps-Platform
    +-- Repositorio de workflows
    +-- ado-aw
    +-- Pipeline Intelligence
    +-- Boards Intelligence (futuro)
    +-- Repository Intelligence (futuro)
    +-- Governance Intelligence (futuro)
              |
              v
      Azure DevOps MCP / REST API
              |
              v
    Proyectos con acceso autorizado
```

La centralización es una **decisión de arquitectura**, no algo que `ado-aw` cree automáticamente. Habría que mantener un inventario de proyectos permitidos, controlar versiones de agentes, definir identidades y decidir qué información puede aparecer en los informes.

Tiene una ventaja clara: el piloto puede limitarse a dos proyectos y no necesita alterar sus definiciones YAML. Si el resultado no merece la pena, retiramos el pipeline central y revocamos los accesos concedidos.

---

## La pieza de integración: Azure DevOps MCP

Para diagnosticar un pipeline, el agente necesita consultar las ejecuciones y leer logs. El prompt, por sí solo, no le da ese contexto.

Aquí encaja el servidor [Azure DevOps MCP de Microsoft](https://github.com/microsoft/azure-devops-mcp). MCP permite exponer herramientas para que un agente consulte servicios como Boards, Repos, Pipelines o Wiki. Según el servicio y la operación, también existen herramientas de escritura, que no quiero habilitar en el primer piloto.

En `ado-aw` hay integración específica con Azure DevOps MCP. Se puede delimitar el conjunto de herramientas (*toolsets*) y crear una lista explícita de herramientas permitidas.

La documentación muestra una configuración con esta forma:

```yaml
tools:
  bash: []
  edit: false
  azure-devops:
    toolsets: [core, pipelines]
    allowed:
      - core_list_projects
      - pipelines_definition
      - pipelines_build
      - pipelines_build_log
```

**Esto es un fragmento de diseño, no un agente listo para ejecutar.** El nombre de cada herramienta y su pertenencia a un *toolset* deben comprobarse contra la versión concreta de `@azure-devops/mcp` que se vaya a fijar. `ado-aw` transmite esos nombres al servidor MCP; no verifica que sigan existiendo en versiones posteriores.

Hay un detalle de seguridad que conviene no pasar por alto: según la documentación de `ado-aw`, **si se omite `tools.bash`, el acceso a Bash es amplio por defecto**, y `edit` también está habilitado de forma predeterminada. Si queremos que el agente no tenga esas capacidades, hay que desactivarlas explícitamente.

Para el piloto prefiero que el agente únicamente pueda consultar información de Azure DevOps, sin ejecutar comandos arbitrarios ni editar archivos.

Referencias: [Tools configuration](https://githubnext.github.io/ado-aw/reference/tools/) y [Using MCP](https://githubnext.github.io/ado-aw/guides/using-mcp/).

---

## El primer agente: Pipeline Intelligence

De los servicios de Azure DevOps, elegí empezar por **Pipelines**. Los fallos dejan evidencias relativamente claras: ejecución, fase, tarea, código de error, log y duración. Eso nos permite comprobar si el diagnóstico del modelo tiene sentido o si está inventando una explicación plausible.

El agente tendría seis tareas:

1. Consultar las ejecuciones de dos o tres proyectos previamente autorizados.
2. Localizar las ejecuciones fallidas en una ventana temporal acotada.
3. Recuperar los logs relevantes, sin enviar al modelo información que no haga falta.
4. Agrupar errores repetidos y proponer una clasificación.
5. Separar evidencia observada, hipótesis de causa y recomendación.
6. Publicar un informe para que lo revise un ingeniero.

La distinción entre evidencia e hipótesis me parece especialmente importante. Un `403` puede apuntar a un problema de permisos, pero no demuestra por sí solo que haya que cambiar una service connection. Un `timeout` tampoco demuestra necesariamente que exista un fallo de red.

### Cómo debería ser un diagnóstico

Un ejemplo del formato esperado —**no es una salida real del agente**— sería:

```text
Proyecto: Aplicaciones
Pipeline: Build-Backend
Ejecución: 1842
Resultado: Failed

Tarea afectada: Restore NuGet packages

EVIDENCIA
- NU1301: Unable to load the service index for source...
- Error registrado durante la restauración de paquetes.

HIPÓTESIS
- Problema de conectividad o autenticación contra el feed.
- Confianza: media.

COMPROBACIONES PROPUESTAS
1. Revisar la conectividad y la URL del feed.
2. Verificar la autenticación de la tarea NuGet.
3. Comparar con la última ejecución correcta.

ACCIÓN EJECUTADA
- Ninguna.
```

El informe tendría que enlazar con la ejecución original. Si no puede consultar el log, debe indicarlo: **no quiero un diagnóstico convincente construido sobre datos incompletos**.

---

## Definir el agente en Markdown y compilarlo

Una de las ventajas del proyecto es mantener la intención del agente en un archivo legible. La definición combina *front matter* YAML con instrucciones en Markdown.

Un esqueleto para ilustrar el diseño sería:

````markdown
---
name: "Pipeline Intelligence"
description: "Analiza fallos de Azure Pipelines"
engine:
  id: copilot
  timeout-minutes: 20
tools:
  bash: []
  edit: false
  azure-devops:
    toolsets: [core, pipelines]
    allowed:
      - core_list_projects
      - pipelines_definition
      - pipelines_build
      - pipelines_build_log
permissions:
  read: ado-aw-read
---

# Instrucciones

Analiza exclusivamente las ejecuciones de los proyectos
que figuren en la configuración del piloto.

Para cada fallo:
1. Identifica la ejecución y la tarea afectada.
2. Cita el error relevante del log.
3. Separa hechos, hipótesis y recomendaciones.
4. No propongas cambios sin una evidencia concreta.
5. Si falta información, indícalo.

No modifiques repositorios, pipelines ni work items.
````

El ejemplo resume las decisiones principales; para ejecutarlo hay que configurar el proyecto, la identidad, la conexión de lectura y validar la sintaxis con una versión concreta del compilador.

En un repositorio inicializado con `ado-aw`, el flujo básico documentado es:

```bash
ado-aw init
ado-aw compile agents/pipeline-intelligence.md
ado-aw enable
ado-aw run
```

`compile` genera el YAML del workflow. Después hay que versionarlo y registrar la definición del pipeline en Azure DevOps. `enable` y `run` necesitan una sesión y permisos adecuados para interactuar con la organización.

No he añadido un `.lock.yml` escrito a mano como supuesto resultado de compilación: **ese archivo debe salir del compilador real**, con la versión del framework que utilicemos en el piloto.

Referencia: [Quick Start de ado-aw](https://githubnext.github.io/ado-aw/setup/quick-start/).

---

## El riesgo que apareció al revisar permisos: `read` no garantiza solo lectura

Esta fue la parte más delicada del diseño.

La primera idea era crear un service principal en Entra ID, darle acceso de lectura a dos proyectos y referenciarlo desde `permissions.read`. Hasta ahí, bien.

Pero la documentación de `ado-aw` deja claro que, **aunque solo se configure `permissions.read`, SafeOutputs puede seguir utilizando `$(System.AccessToken)`**, el token integrado del pipeline, para operaciones de escritura.

Es decir: **un agente con conexión de lectura no es lo mismo que un workflow entero sin capacidad de escritura**.

Las identidades y las capacidades deben revisarse por separado:

| Componente | Identidad / credencial | Diseño para el piloto |
|---|---|---|
| Agent | Service principal de lectura | Solo los proyectos autorizados. |
| Azure DevOps MCP | Token protegido por la integración | Herramientas de consulta explícitamente permitidas. |
| Pipeline central | Build Service Identity | Permisos mínimos en su proyecto. |
| SafeOutputs | `System.AccessToken` o conexión específica | Sin acciones de modificación habilitadas. |

Además, quiero mantener activa la opción de Azure DevOps **`Limit job authorization scope to current project`**. Para consultar varios proyectos no es necesario abrir el token de build a toda la organización: podemos utilizar una identidad separada con acceso explícito a cada proyecto.

En la práctica, antes de llamar a un modelo haría dos pruebas: comprobar que la identidad puede leer las ejecuciones de los proyectos seleccionados y revisar sus permisos efectivos de escritura. Un `HTTP 200` de lectura demuestra acceso, **no demuestra ausencia de permisos de modificación**.

Otra precaución: los logs pueden incluir secretos accidentalmente expuestos, rutas internas, identificadores o datos de negocio. Hay que limitar el contexto enviado al modelo, respetar las políticas del cliente y establecer retención y acceso a los informes.

Referencias: [Service Connections de ado-aw](https://githubnext.github.io/ado-aw/setup/service-connections/) y [Access tokens en Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/access-tokens?view=azure-devops).

---

## Entra ID y Workload Identity Federation

Para el acceso a Azure DevOps prefiero una identidad de aplicación, no un PAT personal compartido entre scripts y pipelines. La propuesta utiliza un **service principal** con una **service connection** y, cuando la configuración lo permita, **Workload Identity Federation (WIF)**.

El esquema es:

```text
Pipeline central
     |
     v
Service Connection (WIF)
     |
     v
Microsoft Entra ID
     |
     v
Token para Azure DevOps
     |
     v
Azure DevOps API / MCP
     |
     v
Proyectos permitidos
```

Que Entra ID emita un token no significa que ese principal ya pueda consultar cualquier proyecto. Hay que incorporarlo a la organización de Azure DevOps y asignar los permisos necesarios sobre los recursos de destino.

Por eso la primera prueba técnica **no debe incluir IA**. Prepararía un pipeline sencillo que obtenga el token y consulte las ejecuciones de dos proyectos. Si esa prueba falla, no tiene sentido depurar Copilot o MCP todavía.

También comprobaría el alcance de las service connections. No autorizaría la conexión para todos los pipelines del proyecto central por comodidad: la limitaría a los que realmente la necesiten.

---

## ¿Y si el modelo está en Microsoft Foundry?

Otra pregunta que surgió fue si `ado-aw` obliga a utilizar el servicio de inferencia de GitHub Copilot.

La documentación indica que el motor soportado es **Copilot CLI**, pero también describe una configuración **BYOK** (*Bring Your Own Key*) para conectar con otros proveedores de modelos, incluido un ejemplo basado en Foundry.

```text
Azure Pipelines
     |
     v
ado-aw / Copilot CLI
     |
     v
Proveedor configurado mediante BYOK
     |
     v
Modelo desplegado en Foundry
```

Eso abre una alternativa de gobierno y facturación, pero no equivale a reemplazar completamente el runtime de Copilot CLI. Hay que validar autenticación, conectividad, políticas de red, cuotas y costes.

Para el MVP no mezclaría demasiadas variables. Primero confirmaría que el workflow compila y que la autenticación hacia Azure DevOps funciona. Después compararía las opciones de inferencia.

Referencia: [Engine configuration de ado-aw](https://githubnext.github.io/ado-aw/reference/engine/).

---

## El catálogo que salió del diseño: 28 casos de uso

Cuando dejé de pensar en un único agente y miré todos los servicios de Azure DevOps, apareció un catálogo bastante amplio.

No son 28 capacidades listas para activar. Son **28 hipótesis de automatización**, algunas apoyadas en herramientas MCP existentes y otras pendientes de APIs REST o integraciones específicas. Las agrupé así:

| Servicio / área | Casos | Ideas principales |
|---|---:|---|
| **Pipelines** | 6 | Diagnóstico de fallos, recurrencia, tiempos anómalos, análisis de flakiness, dependencias y resúmenes operativos. |
| **Boards** | 5 | Elementos bloqueados, backlog envejecido, clasificación, duplicados y seguimiento de incidencias. |
| **Repos y PR** | 4 | Revisión de cambios, estándares, dependencias y Terraform/Bicep. |
| **Test Plans** | 3 | Tendencias de fallos, cobertura y relación entre pruebas e incidencias. |
| **Wiki** | 2 | Documentación desactualizada e inconsistencias con repositorios. |
| **Seguridad** | 2 | Revisión de configuraciones sensibles y patrones de riesgo en código. |
| **Artifacts** | 2 | Versiones obsoletas y dependencias de paquetes. |
| **Gobierno multiproyecto** | 4 | Estándares, permisos, inventario y reporting consolidado. |
| **Total** | **28** | |

Tres me parecen especialmente interesantes para una evolución posterior.

### Boards Intelligence

Consultar work items abiertos, identificar los que no tienen responsable o llevan semanas sin actividad y generar un resumen para sus equipos. La IA podría sugerir una clasificación, **no cambiar las prioridades automáticamente**.

### Repository Intelligence

Revisar PR y detectar configuraciones que merecen atención: una versión antigua de Terraform, un módulo sin restricciones, una variable sensible o una desviación respecto a una convención de repositorios. No sustituye a linters, análisis estático ni políticas de rama; añade contexto a sus resultados.

### DevOps Governance

Comparar configuraciones entre proyectos para localizar diferencias en políticas de rama, pipelines, aprobaciones o nomenclaturas. Parece sencillo, pero tiene una dependencia esencial: **si no existe un estándar acordado, el agente no sabe distinguir una desviación de una excepción aceptada**.

Por eso el catálogo se organiza por fases. No pondría todos esos agentes a ejecutarse cada noche: primero hay que demostrar que producen información útil y que podemos controlar su impacto.

---

## Tres niveles de automatización, y ninguno empieza desplegando en producción

La tentación es clara: si el agente detecta un problema, ¿por qué no dejar que lo solucione?

Porque detectar un patrón no equivale a entender las consecuencias de modificar un pipeline o un repositorio. Una política de ramas aparentemente débil puede tener una excepción aprobada. Un fallo intermitente puede estar causado por una dependencia externa. Una corrección automática puede romper algo que estaba funcionando.

Dividí la evolución en tres niveles:

| Nivel | Comportamiento | Cuándo lo utilizaría |
|---|---|---|
| **1. Observar** | Leer, analizar y publicar informes. | Primer piloto. |
| **2. Recomendar** | Proponer work items, cambios o PR sujetos a aprobación. | Cuando la precisión esté medida. |
| **3. Actuar** | Ejecutar operaciones limitadas y auditables. | Solo para acciones concretas, revisadas y con controles. |

Lo interesante de `ado-aw` es que su arquitectura permite evolucionar hacia acciones supervisadas. Lo peligroso sería utilizar esa capacidad sin diseñar primero la autorización y la trazabilidad.

---

## Cómo estoy organizando el piloto

Antes de tocar el Azure DevOps del cliente, preparé la documentación y los componentes de trabajo:

| Entregable | Para qué sirve | Estado |
|---|---|---|
| 01. Arquitectura de referencia | Componentes, flujos, identidades y límites de seguridad. | Diseñado. |
| 02. Pipeline Intelligence | Definición del agente y utilidades de preparación. | Preparado localmente. |
| 03. Preparación de Azure DevOps | Proyecto central, service connection, WIF y pruebas de acceso. | Procedimiento preparado. |
| 04. Ejecución y validación | Casos de prueba, evidencias y decisión GO/NO-GO. | Documentado. |
| 05. Catálogo de casos de uso | Evolución posible sobre los servicios de Azure DevOps. | Documentado. |

Los artefactos locales no sustituyen una prueba real. **No hay todavía un YAML compilado y ejecutado contra la organización del cliente ni un informe generado por el agente con logs reales**.

La secuencia que seguiría es esta:

1. Crear el proyecto central privado y seleccionar dos proyectos piloto.
2. Configurar la identidad de Entra ID y la conexión de lectura.
3. Comprobar el acceso REST sin IA y revisar los permisos efectivos.
4. Fijar versiones de `ado-aw`, Copilot CLI y el servidor MCP.
5. Compilar el agente y registrar el pipeline generado.
6. Ejecutarlo manualmente sobre una muestra limitada de fallos.
7. Revisar cada diagnóstico con un ingeniero y decidir si tiene utilidad.

Los indicadores también tienen que ser concretos. Mediría **precisión del diagnóstico**, porcentaje de informes con evidencia verificable, tiempo ahorrado, coste por ejecución y cumplimiento de los límites de seguridad.

No consideraría éxito que el modelo redacte un informe bonito. El éxito es que alguien pueda utilizarlo para investigar un fallo más rápido **sin perder trazabilidad ni ampliar privilegios**.

---

## Lo que aprendí al revisar la herramienta

1. **Open source no es igual a coste cero.** El compilador tiene licencia MIT, pero el motor, la ejecución y la operación de la solución tienen costes y dependencias.
2. **Un prompt no es un control de seguridad.** Las prohibiciones tienen que existir en herramientas, identidades y permisos efectivos.
3. **`permissions.read` no resuelve por sí solo el problema.** SafeOutputs puede disponer de `System.AccessToken`. Hay que revisar el pipeline completo.
4. **Los defaults importan.** En la documentación actual, Bash y edición tienen valores predeterminados permisivos. Para solo lectura, se deshabilitan explícitamente.
5. **MCP no elimina el mantenimiento.** Hay que fijar versiones y validar los nombres de las herramientas. Una actualización puede cambiar el contrato que utiliza el agente.
6. **No mezclar fallos de autenticación con fallos de IA.** Primero una prueba REST con la identidad federada; después el agente.
7. **Cada diagnóstico necesita un enlace a la evidencia.** Un modelo puede explicar con mucha seguridad un error cuya causa real desconoce.
8. **El escalado debe venir después del MVP.** Una única organización facilita el gobierno, pero eso no justifica abrir todos los proyectos al primer agente.

---

## Entregables y próximos pasos

El resultado de este trabajo no es una plataforma desplegada, sino una base para decidir si merece la pena construirla: arquitectura multiproyecto, configuración inicial de Pipeline Intelligence, procedimiento de acceso, plan de pruebas y catálogo de 28 casos de uso.

La siguiente prueba importante será bastante menos espectacular que pedirle a un agente que corrija un pipeline: **obtener un token de Entra ID mediante la service connection, consultar ejecuciones de dos proyectos y demostrar que la identidad tiene exactamente el acceso que necesita**.

Si eso funciona, tocará compilar el workflow real y contrastar diagnósticos con logs conocidos. Y si el resultado no es suficientemente preciso o el coste no compensa, tendremos datos para parar antes de extenderlo a toda la organización.

---

## Reflexión final

Lo que me interesa de `ado-aw` no es escribir un Markdown que luego se convierte en YAML. Eso, por sí solo, es una comodidad.

Lo interesante es la posibilidad de usar agentes dentro de una plataforma que ya genera muchísima información: ejecuciones, código, pruebas, incidencias y documentación. **La oportunidad está en convertir esa información en diagnósticos y decisiones verificables**, sin obligar a cada equipo a construir su propia automatización.

Pero hay un orden que no quiero invertir: primero arquitectura y permisos; después conectividad y evidencias; luego IA; y solo al final, si tiene sentido, acciones automatizadas.

Un agente que identifica problemas y se equivoca de vez en cuando puede ser útil si permite revisar sus fuentes. Un agente con permisos amplios que se equivoca ejecutando cambios es otra historia.

---

## Referencias

- [GitHub Next - Azure DevOps Agentic Workflows](https://github.com/githubnext/ado-aw)
- [ado-aw - Quick Start](https://githubnext.github.io/ado-aw/setup/quick-start/)
- [ado-aw - Service Connections](https://githubnext.github.io/ado-aw/setup/service-connections/)
- [ado-aw - Tools configuration](https://githubnext.github.io/ado-aw/reference/tools/)
- [ado-aw - Engine / BYOK](https://githubnext.github.io/ado-aw/reference/engine/)
- [ado-aw - Integración con MCP](https://githubnext.github.io/ado-aw/guides/using-mcp/)
- [Microsoft - Azure DevOps MCP Server](https://github.com/microsoft/azure-devops-mcp)
- [Microsoft Learn - Job authorization scope](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/access-tokens?view=azure-devops)

---

*Si tienes preguntas o quieres comentar algo de este post, escríbeme a luisadanmunoz@outlook.com.*

Revisado el 27 de octubre de 2026.
