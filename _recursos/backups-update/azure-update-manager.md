---
title: "Azure Update Manager"
indice: backups-update
resumen: "Parches y actualizaciones desde un único sitio."
estado: documentado   # proximamente | en-curso | documentado
orden: 5
last_review: 2026-10-20
fuentes:
  - titulo: "What is Azure Update Manager?"
    url: https://learn.microsoft.com/azure/update-manager/overview
  - titulo: "Prerequisites for Azure Update Manager"
    url: https://learn.microsoft.com/azure/update-manager/prerequisites
  - titulo: "Update options and orchestration in Azure Update Manager"
    url: https://learn.microsoft.com/azure/update-manager/updates-maintenance-schedules
  - titulo: "Manage multiple machines with Azure Update Manager (orquestación del parcheo)"
    url: https://learn.microsoft.com/azure/update-manager/manage-multiple-machines
  - titulo: "Schedule recurring updates for machines by using the Azure portal and Azure Policy"
    url: https://learn.microsoft.com/azure/update-manager/scheduled-patching
  - titulo: "Managing VM updates with Maintenance Configurations"
    url: https://learn.microsoft.com/azure/virtual-machines/maintenance-configurations
  - titulo: "How to programmatically manage updates for Azure VMs"
    url: https://learn.microsoft.com/azure/update-manager/manage-vms-programmatically
  - titulo: "MaintenanceWindow.recurEvery (formato de recurrencia)"
    url: https://learn.microsoft.com/javascript/api/@azure/arm-maintenance/maintenancewindow
  - titulo: "About dynamic scoping"
    url: https://learn.microsoft.com/azure/update-manager/dynamic-scope-overview
  - titulo: "Manage a dynamic scope"
    url: https://learn.microsoft.com/azure/update-manager/manage-dynamic-scoping
  - titulo: "About pre and post events"
    url: https://learn.microsoft.com/azure/update-manager/pre-post-scripts-overview
  - titulo: "Create pre and post events"
    url: https://learn.microsoft.com/azure/update-manager/pre-post-events-schedule-maintenance-configuration
  - titulo: "Manage pre and post events"
    url: https://learn.microsoft.com/azure/update-manager/manage-pre-post-events
  - titulo: "Azure Maintenance Configuration as an Event Grid source"
    url: https://learn.microsoft.com/azure/event-grid/event-schema-maintenance-configuration
  - titulo: "Automate assessment at scale by using Azure Policy"
    url: https://learn.microsoft.com/azure/update-manager/periodic-assessment-at-scale
  - titulo: "Azure Policy built-in definitions (Azure Update Manager)"
    url: https://learn.microsoft.com/azure/governance/policy/samples/built-in-policies#azure-update-manager
  - titulo: "Definiciones integradas de Azure Update Manager (azure-policy)"
    url: https://github.com/Azure/azure-policy/tree/master/built-in-policies/policyDefinitions/Azure%20Update%20Manager
  - titulo: "Access Azure Update Manager operations data using Azure Resource Graph"
    url: https://learn.microsoft.com/azure/update-manager/query-logs
  - titulo: "Create alerts (preview)"
    url: https://learn.microsoft.com/azure/update-manager/manage-alerts
  - titulo: "Unsupported workloads for Azure Update Manager"
    url: https://learn.microsoft.com/azure/update-manager/unsupported-workloads
  - titulo: "Support matrix for Azure Update Manager"
    url: https://learn.microsoft.com/azure/update-manager/support-matrix-updates
  - titulo: "Troubleshoot known issues with Azure Update Manager"
    url: https://learn.microsoft.com/azure/update-manager/troubleshoot
  - titulo: "Troubleshoot problems with Maintenance Configurations"
    url: https://learn.microsoft.com/azure/virtual-machines/troubleshoot-maintenance-configurations
  - titulo: "Azure Update Manager frequently asked questions (precios)"
    url: https://learn.microsoft.com/azure/update-manager/update-manager-faq
  - titulo: "Azure Update Manager pricing"
    url: https://azure.microsoft.com/pricing/details/azure-update-management-center/
  - titulo: "Extended Security Updates (ESU) for Windows Server"
    url: https://learn.microsoft.com/azure/update-manager/extended-security-updates
  - titulo: "Manage hotpatches on Arc-enabled machines"
    url: https://learn.microsoft.com/azure/update-manager/manage-hot-patching-arc-machines
  - titulo: "Hotpatch for Windows Server"
    url: https://learn.microsoft.com/windows-server/get-started/hotpatch
  - titulo: "Scalable Windows virtual machine patch management (Azure Architecture Center)"
    url: https://learn.microsoft.com/azure/architecture/virtual-machines/patch-management
  - titulo: "Migrate from Log Analytics agent to Azure Monitor Agent (retirada de Automation Update Management)"
    url: https://learn.microsoft.com/azure/azure-monitor/agents/azure-monitor-agent-migration
  - titulo: "azurerm_maintenance_configuration"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/maintenance_configuration
  - titulo: "azurerm_maintenance_assignment_dynamic_scope"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/maintenance_assignment_dynamic_scope
  - titulo: "Microsoft.Maintenance maintenanceConfigurations (plantillas ARM/Bicep)"
    url: https://learn.microsoft.com/azure/templates/microsoft.maintenance/maintenanceconfigurations
  - titulo: "Módulo Terraform BackupAndUpdate/MaintenanceConfiguration"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/BackupAndUpdate/MaintenanceConfiguration
  - titulo: "Módulo Terraform BackupAndUpdate/MaintenanceAssignment"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/BackupAndUpdate/MaintenanceAssignment
---

**Azure Update Manager** gestiona los parches del sistema operativo de VMs de Azure y de servidores conectados con Azure Arc (on-premises, VMware, SCVMM, otras nubes) desde un único sitio. Sustituye a Automation Update Management, retirado el 31 de agosto de 2024 junto con el agente de Log Analytics:

- **No depende** de Log Analytics, Azure Automation ni Azure Monitor Agent: es una capacidad nativa de la VM, con una extensión que se instala sola la primera vez.
- **Los datos viven en Azure Resource Graph**: 7 días de evaluaciones y 30 días de instalaciones.
- **Permisos por recurso** con RBAC, en lugar de por cuenta de Automation y workspace.

Junto a [Azure Backup](/recursos/backups-update/azure-backup/) y [Azure Site Recovery](/recursos/backups-update/azure-site-recovery/), cierra la parte de operación de las VMs: copias, réplica y parches.

## Qué es y cuándo usarlo

### Qué ofrece

| Capacidad | Qué hace |
|---|---|
| **Evaluación periódica** | Revisa las actualizaciones pendientes cada 24 horas |
| Evaluación e instalación bajo demanda | Una vez, sobre una o varias máquinas |
| **Calendarios** (*maintenance configurations*, ámbito `InGuestPatch`) | Instalación recurrente en una ventana, con clasificaciones, KB o paquetes y reinicio |
| **Ámbitos dinámicos** | Las máquinas entran por suscripción, grupo de recursos, región, SO o tags en cada ejecución |
| **Eventos previos y posteriores** | Event Grid antes y después de la ventana: encender VMs, snapshots, parar servicios, informes |
| Hotpatch | Parches de seguridad sin reinicio en Windows Server compatibles |
| Informes y alertas | Workbooks y consultas de Resource Graph; alertas sobre esas consultas (preview) |
| Origen de las actualizaciones | Windows Update/Microsoft Update, **WSUS** si la máquina lo tiene configurado, y los repositorios de cada distribución Linux |

No instala drivers ni actualizaciones que requieran aceptar un EULA.

### Orquestación del parcheo en VMs de Azure

| Opción del portal | Propiedades de la VM | Qué pasa |
|---|---|---|
| **Customer Managed Schedules** | `patchMode = AutomaticByPlatform` + `bypassPlatformSafetyChecksOnUserSchedule = true` | **Requisito para los calendarios**: solo se parchea cuando lo dice el calendario |
| Azure Managed - Safe Deployment | `patchMode = AutomaticByPlatform` | Parcheo automático de Azure (*automatic VM guest patching*) |
| Automatic by OS | `AutomaticByOS` (Windows) | Windows Update decide por su cuenta |
| Image Default | `ImageDefault` (Linux) | La configuración de la imagen |
| Manual | `Manual` (Windows) | Actualizaciones automáticas desactivadas |

- **Sin Customer Managed Schedules, el calendario no parchea la VM.** Los servidores Arc no tienen este requisito.
- Para que **nada** parchee una VM: Customer Managed Schedules sin calendario asociado.

### El calendario

| Regla | Valor |
|---|---|
| Ventana | **Entre 1 h 30 min y 3 h 55 min** |
| Recurrencia | 6 horas como mínimo; diaria, semanal o mensual (hora solo por API) |
| Formato mensual | `Month Second Tuesday Offset4`: segundo martes + 4 días (desplazamiento de -6 a +6) |
| Inicio | 15 minutos o más después de crearlo; evitar crearlo entre las 23:45 y las 00:00 |
| Cambios de máquinas o ámbitos | Hasta 15 minutos antes del inicio (40 si hay evento previo) |
| Reinicio | `IfRequired`, `Always` o `Never` (algunas claves de registro de Windows pueden reiniciar igualmente) |
| Clasificaciones Windows | Critical, Security, UpdateRollup, FeaturePack, ServicePack, Definition, Tools, Updates |
| Clasificaciones Linux | Critical, Security, Other |
| Modo | `InGuestPatchMode = User` |

Cómo se consume la ventana:

| | Windows | Linux |
|---|---|---|
| Para empezar a instalar | 20 min restantes (service pack) o 15 (resto) | Lotes: 5 min por paquete hasta 3; después 15 + 2 por paquete |
| Para reiniciar | 10 min restantes | 15 min restantes (solo VMs de Azure) |
| Espera al reinicio | 15 min en VMs de Azure, 25 en Arc | — |

Con menos de 25 minutos no se evalúa ni se instala nada. Una instalación en curso no se corta al terminar la ventana, pero lo pendiente se salta y la ejecución queda como *Failed* con `maintenanceWindowExceeded`.

### Cómo se asignan las máquinas

| Método | Para qué | Detalle |
|---|---|---|
| **Ámbito dinámico** | La norma | Filtros por suscripción, grupo de recursos, región, SO y tags; evaluado en cada ejecución; VMs y Arc |
| Asignación estática | Excepciones | Una VM concreta; mover la VM de grupo de recursos o suscripción rompe la asignación |
| Azure Policy *Schedule recurring updates* | Alternativa al ámbito dinámico | Crea asignaciones estáticas y también ajusta el modo de parcheo |

Límites:

| Elemento | Límite |
|---|---|
| Calendarios por suscripción y región | 250 |
| Máquinas asociadas a un calendario | 3000 |
| Máquinas por ámbito dinámico | 1000 |
| Ámbitos dinámicos por calendario | 200 |
| Suscripciones en los ámbitos de un calendario | 200 |
| Filtros de tag o de grupo de recursos por ámbito | 50 |

### Eventos previos y posteriores

| Momento | Qué pasa |
|---|---|
| ~30 min antes | Se lanza el evento previo (Event Grid → función, webhook, cola, Event Hub) |
| 20 min | Tiempo que tienen los eventos previos para terminar |
| Hasta 10 min antes | El evento previo puede **cancelar** esa ejecución; si no la cancela, el parcheo sigue aunque haya fallado |
| Tras la instalación | Evento posterior, dentro o fuera de la ventana |

- El estado de la ejecución **no incluye** el de los eventos: se revisa en el destino.
- Event Grid entrega *al menos una vez*: las acciones deben ser idempotentes.
- Los runbooks heredados de Automation Update Management funcionan como webhooks, filtrando por `Microsoft.Maintenance.PreMaintenanceEvent` y `PostMaintenanceEvent`.

### Disponibilidad durante el parcheo

Un calendario actualiza **a la vez** todas sus máquinas. Solo dentro de un conjunto de disponibilidad respeta los dominios de actualización. Microsoft recomienda:

- Oleadas por zona, dominio o grupo de instancias, con un tag y un calendario por oleada.
- Un escalonado tras el Patch Tuesday: desarrollo, pruebas y producción en días distintos.

### Qué no cubre

| Carga | Alternativa |
|---|---|
| Windows 10/11 | Microsoft Intune |
| Virtual Machine Scale Sets | Actualizaciones automáticas de la imagen del SO |
| Nodos de AKS | Mecanismo de actualización de nodos de AKS |
| SO x86 | No soportado |

### Arc, hotpatch y ESU

- **Arc**: basta con el agente conectado; sin requisito de modo de parcheo.
- **Hotpatch**: las imágenes *Azure Edition* de Windows Server 2022 y 2025 reciben parches de seguridad sin reinicio. Cada trimestre llega una actualización base que sí reinicia. En Arc, Windows Server 2025 Standard y Datacenter tienen hotpatch **sin coste** desde el 19 de mayo de 2026.
- **ESU**: Windows Server 2012/2012 R2 en Azure los recibe gratis. Fuera de Azure, se contratan con Arc y se instalan con Update Manager. **El periodo de ESU de 2012/2012 R2 terminó el 13 de octubre de 2026**; los de Windows Server 2016 se facturan desde el 13 de enero de 2027.

### Gobierno con Azure Policy

| Definición integrada | Efecto | Uso |
|---|---|---|
| *Configure periodic checking for missing system updates on azure virtual machines* | Modify | Evaluación cada 24 h en VMs; una asignación por SO |
| *… on azure Arc-enabled servers* | Modify | Lo mismo en Arc |
| *Set prerequisite for Scheduling recurring updates on Azure virtual machines* | DeployIfNotExists | Pone las VMs en Customer Managed Schedules |
| *Schedule recurring updates using Azure Update Manager* | DeployIfNotExists | Asigna máquinas a un calendario |
| *Machines should be configured to periodically check for missing system updates* | Audit/Deny | Medir quién no tiene evaluación periódica |

### Cómo se factura

| Recurso | Coste de Update Manager |
|---|---|
| **VMs de Azure** | **Sin coste** |
| VMs de Azure Local creadas con el resource bridge de Arc | Sin coste |
| Servidores Arc | Por servidor y mes, prorrateado por día conectado y gestionado |
| Servidores Arc con ESU por Arc, Defender for Servers Plan 2 en la suscripción, o Software Assurance/suscripción de Windows Server declarada | Sin coste |

No hay coste por transferencia de datos. Los eventos previos y posteriores sí consumen Event Grid y el destino (Functions, Automation).

### Qué escenario recomiendo

| Escenario del cliente | Diseño | Por qué |
|---|---|---|
| VMs de Azure en producción | Calendarios mensuales tras el Patch Tuesday, ámbitos dinámicos por tag y oleadas | Control del momento y sin reiniciar una capa entera |
| Desarrollo y pruebas | Calendario semanal o *Azure Managed - Safe Deployment* | Siempre al día, poco esfuerzo |
| Servidores on-premises o en otras nubes | Arc + mismos calendarios y ámbitos | Un único modelo; revisar si les aplica la gratuidad (SA, ESU, Defender P2) |
| VMs que se apagan fuera de horario | Evento previo que las enciende y posterior que las apaga | Si está apagada no se parchea |
| SQL Server o aplicaciones con servicios que parar | Eventos previos y posteriores que paran y arrancan servicios | Parcheo sin corrupción ni bloqueos |
| Windows Server 2025 | Hotpatch (Azure Edition o Arc) | Menos reinicios |
| Organización con muchas suscripciones | Azure Policy en cada suscripción: evaluación, requisito y auditoría | Visibilidad y prerrequisitos sin intervención manual |
| Cliente que viene de Automation Update Management o WSUS/SCCM | Migración a calendarios; WSUS puede seguir como origen | Retirado el producto anterior; WSUS sigue soportado |

### Datos que conviene llevar a la reunión

- **Sin coste en VMs de Azure**; en Arc, por servidor salvo SA, ESU o Defender for Servers Plan 2.
- **Automation Update Management está retirado** desde agosto de 2024: si el cliente aún lo tiene, migrar es obligatorio.
- **Sin Customer Managed Schedules, los calendarios no parchean** las VMs de Azure.
- **Ventana máxima de 3 h 55 min**: más máquinas no alargan la ventana; se reparten en oleadas.
- **Un calendario reinicia todo lo que toca a la vez**: las oleadas son parte del diseño de alta disponibilidad.
- **No parchea Windows 10/11, scale sets ni AKS.**
- **Los datos de cumplimiento están en Resource Graph** (7 días de evaluaciones y 30 de instalaciones): para histórico largo hay que exportarlos.
- **Hotpatch** reduce los reinicios a uno por trimestre en Windows Server compatible.
- **Windows Server 2012/2012 R2 ya no recibe ESU** (terminaron el 13 de octubre de 2026): migrar o actualizar.

## Decisiones de diseño

| Decisión | Lo que aplico | Por qué |
|---|---|---|
| Calendarios | Módulo del repositorio, `InGuestPatch`, modo `User` | El ámbito de Update Manager |
| Ventana | 3 h 55 min por defecto, validada entre 1 h 30 y 3 h 55 | El máximo permitido; menos reduce lo que cabe |
| Recurrencia | Mensual relativa al Patch Tuesday con desplazamiento | Patrón recomendado por Microsoft |
| Clasificaciones | Critical + Security por defecto; producción añade UpdateRollup y Definition | Mínimo seguro, ampliable por calendario |
| Reinicio | `IfRequired` | Ni reinicios innecesarios ni parches a medias |
| Asignación | Ámbitos dinámicos por tag; estáticas solo para excepciones | Las máquinas nuevas entran solas |
| Oleadas | Un calendario y un valor de tag por oleada | Disponibilidad durante el parcheo |
| Requisito de las VMs | Azure Policy DeployIfNotExists + atributos en el módulo de VM | Nadie se queda fuera por el modo de parcheo |
| Evaluación periódica | Azure Policy Modify en VMs (y Arc) con remediación | Cumplimiento visible a diario |
| Eventos | Event Grid hacia Azure Functions; webhooks solo como variable sensible | Sin secretos en el código |
| Ubicación | Root propio (gestión), una ejecución por suscripción para los ámbitos dinámicos | Los ámbitos son recursos de suscripción |

Alineación con el Well-Architected Framework:

- **Seguridad**: parches críticos y de seguridad siempre, evaluación diaria, auditoría con Azure Policy.
- **Fiabilidad**: oleadas, conjuntos de disponibilidad, eventos para parar servicios y snapshots.
- **Excelencia operativa**: calendarios, ámbitos y gobierno en IaC; informes en Resource Graph.
- **Coste**: sin coste en Azure; en Arc, revisar los beneficios de SA, ESU y Defender.
- **Rendimiento**: ventanas fuera del horario de uso.

## Módulo de Terraform

### Los módulos del repositorio

| Pieza | Módulo | Estado |
|---|---|---|
| Calendario | [`BackupAndUpdate/MaintenanceConfiguration`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/BackupAndUpdate/MaintenanceConfiguration) | **Utilizable** con valores explícitos |
| Asignación (VM, VMSS, host dedicado, ámbito dinámico) | [`BackupAndUpdate/MaintenanceAssignment`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/BackupAndUpdate/MaintenanceAssignment) | **Utilizable** |
| Eventos previos y posteriores, Azure Policy | — | No hay módulo |

**`MaintenanceConfiguration`**:

- Su validación de `visibility` admite `Public`, pero el provider solo acepta `Custom`.
- No obliga a `install_patches` ni a `in_guest_user_patch_mode` con `scope = "InGuestPatch"`, aunque el provider los exige: el error llega en el `apply`.
- Ventana por defecto de 2 horas en `UTC`, sin validar el rango de 1 h 30 a 3 h 55 ni las clasificaciones permitidas.
- Si no se pasa `name`, genera `maint-config-dev-001` (entorno `dev` por defecto): en la ficha el nombre va siempre explícito.

**`MaintenanceAssignment`**:

- Un único módulo con cuatro tipos y `count`; admite azurerm desde 3.70.
- La variable `tags` no la usa ningún recurso, y `location` es obligatoria aunque el ámbito dinámico no la usa.
- La asignación de **scale sets** es para el ámbito *OS image* (actualizaciones automáticas de imagen), **no para Update Manager**.
- El ámbito dinámico se crea en la suscripción del provider: para otras suscripciones, una llamada con `providers = { azurerm = azurerm.<alias> }`.

Sobre el provider: azurerm no tiene recurso para asignar estáticamente un **servidor Arc**. En Arc se usan ámbitos dinámicos (`Microsoft.HybridCompute/machines`) o la política de programación.

### Estructura en el proyecto

Root propio de gestión:

```txt
/
├── providers.tf          # azurerm >= 4.64.0
├── update_manager.tf     # calendarios (módulo), ámbitos y asignaciones (módulo), eventos
├── update_governance.tf  # Azure Policy: evaluación, requisito y auditoría
└── env/
    └── pro.tfvars
```

### `providers.tf`

```hcl
terraform {
  required_version = ">= 1.6.0"
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      # Misma versión mínima que el resto de fichas de Backup & Update.
      # < 5.0.0: restricción de los módulos de AzureTerraformModules.
      version = ">= 4.64.0, < 5.0.0"
    }
  }
}

# Los ámbitos dinámicos se crean en la suscripción de este provider
provider "azurerm" {
  features {}
}

variable "tags" {
  description = "Tags corporativos comunes a todos los recursos."
  type        = map(string)
}
```

### `update_manager.tf`

```hcl
# =============================================================================
# Azure Update Manager: calendarios de mantenimiento (maintenance configurations InGuestPatch),
# ámbitos dinámicos, asignaciones estáticas y eventos previos y posteriores
#
# DEPENDENCY: grupos de recursos de las configuraciones creados
# DEPENDENCY: VMs de Azure con orquestación "Customer Managed Schedules"
#             (patch_mode = AutomaticByPlatform + bypass_platform_safety_checks_on_user_schedule_enabled = true);
#             la aplica update_governance.tf o el propio módulo de VM. Arc no lo necesita.
# DEPENDENCY: los ámbitos dinámicos se crean en la suscripción del provider
# DEPENDENCY: eventos previos/posteriores: Function App o webhook ya desplegados
# =============================================================================

variable "maintenance_configurations" {
  description = "Calendarios de parcheo (clave = nombre de la maintenance configuration)."
  type = map(object({
    resource_group_name = string
    location            = string

    window = object({
      start_date_time      = string                 # "YYYY-MM-DD hh:mm", 15 minutos o más después de crearla
      duration             = optional(string, "03:55") # entre 01:30 y 03:55
      time_zone            = string                 # p. ej. "Romance Standard Time"
      recur_every          = string                 # p. ej. "Month Second Tuesday Offset4", "Week Saturday"
      expiration_date_time = optional(string)
    })

    reboot = optional(string, "IfRequired") # IfRequired | Always | Never

    windows = optional(object({
      classifications_to_include = optional(list(string), ["Critical", "Security"])
      kb_numbers_to_include      = optional(list(string), [])
      kb_numbers_to_exclude      = optional(list(string), [])
    }), {})

    linux = optional(object({
      classifications_to_include    = optional(list(string), ["Critical", "Security"])
      package_names_mask_to_include = optional(list(string), [])
      package_names_mask_to_exclude = optional(list(string), [])
    }), {})

    # Ámbitos dinámicos: las máquinas se evalúan en cada ejecución (máx. 1000 por ámbito)
    dynamic_scopes = optional(map(object({
      locations       = optional(list(string), [])
      os_types        = optional(list(string), ["Windows", "Linux"])
      resource_groups = optional(list(string), [])
      resource_types  = optional(list(string), ["Microsoft.Compute/virtualMachines", "Microsoft.HybridCompute/machines"])
      tag_filter      = optional(string, "Any") # Any | All
      tags            = optional(map(list(string)), {})
    })), {})

    # Asignaciones estáticas de VMs de Azure (clave = nombre lógico)
    virtual_machines = optional(map(object({
      id       = string
      location = string
    })), {})

    # Eventos previos y posteriores (Event Grid). Sin webhooks con secreto en el código:
    # el endpoint preferido es una función; el webhook se lee de var.maintenance_event_webhook_urls.
    events = optional(map(object({
      event_type  = string           # PreMaintenanceEvent | PostMaintenanceEvent
      function_id = optional(string) # {function_app_id}/functions/{nombre}
    })), {})

    tags = optional(map(string), {})
  }))
  default = {}

  validation {
    condition = alltrue([
      for k, v in var.maintenance_configurations :
      can(regex("^(01:(3[0-9]|[45][0-9])|02:[0-5][0-9]|03:([0-4][0-9]|5[0-5]))$", v.window.duration))
    ])
    error_message = "La ventana de parcheo (InGuestPatch) dura entre 01:30 y 03:55."
  }

  validation {
    condition = alltrue([
      for k, v in var.maintenance_configurations :
      can(regex("^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}$", v.window.start_date_time))
    ])
    error_message = "start_date_time con formato YYYY-MM-DD hh:mm."
  }

  validation {
    condition     = alltrue([for k, v in var.maintenance_configurations : contains(["IfRequired", "Always", "Never"], v.reboot)])
    error_message = "reboot debe ser IfRequired, Always o Never."
  }

  validation {
    condition = alltrue([
      for k, v in var.maintenance_configurations :
      alltrue([for c in v.windows.classifications_to_include : contains(["Critical", "Security", "UpdateRollup", "FeaturePack", "ServicePack", "Definition", "Tools", "Updates"], c)]) &&
      alltrue([for c in v.linux.classifications_to_include : contains(["Critical", "Security", "Other"], c)])
    ])
    error_message = "Clasificaciones no válidas: Windows (Critical, Security, UpdateRollup, FeaturePack, ServicePack, Definition, Tools, Updates); Linux (Critical, Security, Other)."
  }

  validation {
    condition = alltrue(flatten([
      for k, v in var.maintenance_configurations : [
        for sk, s in v.dynamic_scopes :
        contains(["Any", "All"], s.tag_filter) &&
        alltrue([for o in s.os_types : contains(["Windows", "Linux"], o)]) &&
        alltrue([for t in s.resource_types : contains(["Microsoft.Compute/virtualMachines", "Microsoft.HybridCompute/machines"], t)]) &&
        length(s.tags) <= 50 && length(s.resource_groups) <= 50
      ]
    ]))
    error_message = "Ámbito dinámico: tag_filter Any/All, os_types Windows/Linux, tipos VM o Arc y 50 filtros de tag o grupo de recursos como máximo."
  }

  validation {
    condition = alltrue(flatten([
      for k, v in var.maintenance_configurations : [
        for ek, e in v.events : contains(["PreMaintenanceEvent", "PostMaintenanceEvent"], e.event_type)
      ]
    ]))
    error_message = "event_type debe ser PreMaintenanceEvent o PostMaintenanceEvent."
  }

  validation {
    condition = alltrue([
      for k, v in var.maintenance_configurations : length(k) + length(v.resource_group_name) < 128
    ])
    error_message = "Nombre de la configuración y del grupo de recursos: menos de 128 caracteres."
  }
}

variable "maintenance_event_webhook_urls" {
  description = "URLs de webhook (Automation) por evento, con clave <configuración>/<evento>. Contienen un token: inyectar desde un secreto del pipeline."
  type        = map(string)
  default     = {}
  sensitive   = true
}

# -----------------------------------------------------------------------------
# Calendarios (scope InGuestPatch, modo de parcheo "User")
# -----------------------------------------------------------------------------
module "maintenance_configuration" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//BackupAndUpdate/MaintenanceConfiguration?ref=main"
  for_each = var.maintenance_configurations

  name                     = each.key
  resource_group_name      = each.value.resource_group_name
  location                 = each.value.location
  scope                    = "InGuestPatch"
  visibility               = "Custom"
  in_guest_user_patch_mode = "User"

  window = {
    start_date_time      = each.value.window.start_date_time
    expiration_date_time = each.value.window.expiration_date_time
    duration             = each.value.window.duration
    time_zone            = each.value.window.time_zone
    recur_every          = each.value.window.recur_every
  }

  install_patches = {
    reboot  = each.value.reboot
    windows = each.value.windows
    linux   = each.value.linux
  }

  tags = merge(var.tags, each.value.tags)
}

# -----------------------------------------------------------------------------
# Ámbitos dinámicos (suscripción del provider)
# -----------------------------------------------------------------------------
module "maintenance_dynamic_scope" {
  source = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//BackupAndUpdate/MaintenanceAssignment?ref=main"
  for_each = {
    for s in flatten([
      for k, v in var.maintenance_configurations : [
        for sk, scope in v.dynamic_scopes : {
          key      = "${k}/${sk}"
          config   = k
          name     = "${k}-${sk}" # único por suscripción
          location = v.location
          scope    = scope
        }
      ]
    ]) : s.key => s
  }

  location                     = each.value.location
  maintenance_configuration_id = module.maintenance_configuration[each.value.config].id
  assignment_type              = "DynamicScope"

  dynamic_scope = {
    name = each.value.name
    filter = {
      locations       = each.value.scope.locations
      os_types        = each.value.scope.os_types
      resource_groups = each.value.scope.resource_groups
      resource_types  = each.value.scope.resource_types
      tag_filter      = each.value.scope.tag_filter
      tags            = [for tag, values in each.value.scope.tags : { tag = tag, values = values }]
    }
  }
}

# -----------------------------------------------------------------------------
# Asignaciones estáticas de VMs concretas
# -----------------------------------------------------------------------------
module "maintenance_vm_assignment" {
  source = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//BackupAndUpdate/MaintenanceAssignment?ref=main"
  for_each = {
    for a in flatten([
      for k, v in var.maintenance_configurations : [
        for vk, vm in v.virtual_machines : {
          key    = "${k}/${vk}"
          config = k
          vm     = vm
        }
      ]
    ]) : a.key => a
  }

  location                     = each.value.vm.location
  maintenance_configuration_id = module.maintenance_configuration[each.value.config].id
  assignment_type              = "VirtualMachine"
  virtual_machine_id           = each.value.vm.id
}

# -----------------------------------------------------------------------------
# Eventos previos y posteriores: system topic por configuración + suscripción por evento
# -----------------------------------------------------------------------------
resource "azurerm_eventgrid_system_topic" "maintenance" {
  for_each = { for k, v in var.maintenance_configurations : k => v if length(v.events) > 0 }

  name                = "evgt-${each.key}"
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  source_resource_id  = module.maintenance_configuration[each.key].id
  topic_type          = "Microsoft.Maintenance.MaintenanceConfigurations"

  tags = merge(var.tags, each.value.tags)
}

resource "azurerm_eventgrid_system_topic_event_subscription" "maintenance" {
  for_each = {
    for e in flatten([
      for k, v in var.maintenance_configurations : [
        for ek, ev in v.events : {
          key    = "${k}/${ek}"
          config = k
          name   = ek
          event  = ev
          rg     = v.resource_group_name
        }
      ]
    ]) : e.key => e
  }

  name                  = each.value.name
  system_topic          = azurerm_eventgrid_system_topic.maintenance[each.value.config].name
  resource_group_name   = each.value.rg
  event_delivery_schema = "EventGridSchema"
  included_event_types  = ["Microsoft.Maintenance.${each.value.event.event_type}"]

  dynamic "azure_function_endpoint" {
    for_each = each.value.event.function_id == null ? [] : [each.value.event.function_id]
    content {
      function_id = azure_function_endpoint.value
    }
  }

  dynamic "webhook_endpoint" {
    for_each = each.value.event.function_id == null ? [each.key] : []
    content {
      url = var.maintenance_event_webhook_urls[webhook_endpoint.value]
    }
  }

  lifecycle {
    precondition {
      condition     = each.value.event.function_id != null || contains(keys(var.maintenance_event_webhook_urls), each.key)
      error_message = "Cada evento necesita function_id o una URL en maintenance_event_webhook_urls con la misma clave."
    }
  }
}

# -----------------------------------------------------------------------------
# Salidas
# -----------------------------------------------------------------------------
output "maintenance_configuration_ids" {
  description = "Calendarios de parcheo (para la política de programación o asignaciones externas)."
  value       = { for k, m in module.maintenance_configuration : k => m.id }
}

output "maintenance_dynamic_scope_ids" {
  description = "Ámbitos dinámicos (configuración/ámbito)."
  value       = { for k, m in module.maintenance_dynamic_scope : k => m.id }
}
```

### `update_governance.tf`

```hcl
# =============================================================================
# Gobierno de Azure Update Manager con Azure Policy (definiciones integradas):
# - Evaluación periódica cada 24 horas en VMs (59efceea) y en servidores Arc (bfea026e) — Modify
# - Requisito "Customer Managed Schedules" en VMs (9905ca54) — DeployIfNotExists
# - Auditoría de evaluación periódica (bd876905) — Audit
# DEPENDENCY: la identidad de Terraform necesita asignar roles en cada suscripción
# DEPENDENCY: una política de evaluación por sistema operativo (la definición recibe un único osType)
# =============================================================================

variable "update_governance" {
  description = "Gobierno por suscripción (clave = nombre corto sin guiones, máx. 20 caracteres)."
  type = map(object({
    subscription_id = string # /subscriptions/<id>
    location        = string # región de la identidad gestionada de las asignaciones

    os_types          = optional(list(string), ["Windows", "Linux"])
    machine_locations = optional(list(string), []) # vacío = todas
    tag_values        = optional(map(string), {})  # vacío = todas las máquinas
    tag_operator      = optional(string, "Any")    # Any | All

    periodic_assessment_vms = optional(bool, true)
    periodic_assessment_arc = optional(bool, false)
    prerequisite_vms        = optional(bool, true) # Customer Managed Schedules
    audit                   = optional(bool, true)
    remediate_existing      = optional(bool, true)
  }))
  default = {}

  validation {
    condition     = alltrue([for k, v in var.update_governance : can(regex("^[a-z0-9]{1,20}$", k))])
    error_message = "Clave de gobierno: 1-20 minúsculas o números, sin guiones (los nombres de asignación tienen 64 caracteres como máximo)."
  }

  validation {
    condition = alltrue([
      for k, v in var.update_governance :
      contains(["Any", "All"], v.tag_operator) && alltrue([for o in v.os_types : contains(["Windows", "Linux"], o)])
    ])
    error_message = "tag_operator Any o All; os_types Windows o Linux."
  }
}

# -----------------------------------------------------------------------------
# Evaluación periódica (Modify): una asignación por suscripción, tipo de máquina y SO
# -----------------------------------------------------------------------------
resource "azurerm_subscription_policy_assignment" "aum_assessment" {
  for_each = {
    for a in flatten([
      for k, v in var.update_governance : [
        for item in concat(
          v.periodic_assessment_vms ? [for os in v.os_types : { kind = "vm", os = os, definition = "59efceea-0c96-497e-a4a1-4eb2290dac15", role = "Contributor" }] : [],
          v.periodic_assessment_arc ? [for os in v.os_types : { kind = "arc", os = os, definition = "bfea026e-043f-4ff4-9d1b-bf301ca7ff46", role = "Azure Connected Machine Resource Administrator" }] : []
          ) : {
          key  = "${k}-${item.kind}-${lower(item.os)}"
          gov  = v
          item = item
        }
      ]
    ]) : a.key => a
  }

  name                 = "aum-assess-${each.key}"
  display_name         = "Update Manager: evaluación periódica (${each.value.item.kind}, ${each.value.item.os})"
  subscription_id      = each.value.gov.subscription_id
  location             = each.value.gov.location
  policy_definition_id = "/providers/Microsoft.Authorization/policyDefinitions/${each.value.item.definition}"

  identity {
    type = "SystemAssigned"
  }

  parameters = jsonencode({
    assessmentMode = { value = "AutomaticByPlatform" }
    osType         = { value = each.value.item.os }
    locations      = { value = each.value.gov.machine_locations }
    tagValues      = { value = each.value.gov.tag_values }
    tagOperator    = { value = each.value.gov.tag_operator }
  })

  non_compliance_message {
    content = "La máquina no tiene activada la evaluación periódica de actualizaciones."
  }
}

# Rol que declara cada definición: Contributor (VMs) o Azure Connected Machine Resource Administrator (Arc)
resource "azurerm_role_assignment" "aum_assessment" {
  for_each = azurerm_subscription_policy_assignment.aum_assessment

  scope                = each.value.subscription_id
  role_definition_name = strcontains(each.key, "-arc-") ? "Azure Connected Machine Resource Administrator" : "Contributor"
  principal_id         = each.value.identity[0].principal_id
  principal_type       = "ServicePrincipal"
}

resource "azurerm_subscription_policy_remediation" "aum_assessment" {
  for_each = {
    for k, a in azurerm_subscription_policy_assignment.aum_assessment : k => a
    if var.update_governance[split("-", k)[0]].remediate_existing
  }

  name                 = "remediate-${each.value.name}"
  subscription_id      = each.value.subscription_id
  policy_assignment_id = each.value.id

  depends_on = [azurerm_role_assignment.aum_assessment]
}

# -----------------------------------------------------------------------------
# Requisito de programación: patch mode AutomaticByPlatform + BypassPlatformSafetyChecksOnUserSchedule
# -----------------------------------------------------------------------------
resource "azurerm_subscription_policy_assignment" "aum_prerequisite" {
  for_each = { for k, v in var.update_governance : k => v if v.prerequisite_vms }

  name                 = "aum-prereq-${each.key}"
  display_name         = "Update Manager: Customer Managed Schedules en VMs"
  subscription_id      = each.value.subscription_id
  location             = each.value.location
  policy_definition_id = "/providers/Microsoft.Authorization/policyDefinitions/9905ca54-1471-49c6-8291-7582c04cd4d4"

  identity {
    type = "SystemAssigned"
  }

  parameters = jsonencode({
    operatingSystemTypes = { value = each.value.os_types }
    locations            = { value = each.value.machine_locations }
    tagValues            = { value = [for key, value in each.value.tag_values : { key = key, value = value }] }
    tagOperator          = { value = each.value.tag_operator }
    effect               = { value = "DeployIfNotExists" }
  })

  non_compliance_message {
    content = "La VM no tiene la orquestación Customer Managed Schedules necesaria para los calendarios de Update Manager."
  }
}

resource "azurerm_role_assignment" "aum_prerequisite" {
  for_each = azurerm_subscription_policy_assignment.aum_prerequisite

  scope                = each.value.subscription_id
  role_definition_name = "Contributor"
  principal_id         = each.value.identity[0].principal_id
  principal_type       = "ServicePrincipal"
}

resource "azurerm_subscription_policy_remediation" "aum_prerequisite" {
  for_each = {
    for k, a in azurerm_subscription_policy_assignment.aum_prerequisite : k => a
    if var.update_governance[k].remediate_existing
  }

  name                 = "remediate-${each.value.name}"
  subscription_id      = each.value.subscription_id
  policy_assignment_id = each.value.id

  depends_on = [azurerm_role_assignment.aum_prerequisite]
}

# -----------------------------------------------------------------------------
# Auditoría (VMs y Arc)
# -----------------------------------------------------------------------------
resource "azurerm_subscription_policy_assignment" "aum_audit" {
  for_each = { for k, v in var.update_governance : k => v if v.audit }

  name                 = "aum-audit-${each.key}"
  display_name         = "Machines should be configured to periodically check for missing system updates"
  subscription_id      = each.value.subscription_id
  policy_definition_id = "/providers/Microsoft.Authorization/policyDefinitions/bd876905-5b84-4f73-ab2d-2e7a7c4568d9"

  parameters = jsonencode({
    effect = { value = "Audit" }
  })
}
```

### `env/pro.tfvars`

```hcl
tags = {
  environment = "pro"
  workload    = "<workload>"
  owner       = "<owner>"
  costcenter  = "<costcenter>"
}

# Calendarios por oleada, alineados con el segundo martes (Patch Tuesday).
# Producción en dos oleadas para no reiniciar a la vez todas las instancias de una capa.
maintenance_configurations = {
  "mc-patch-pro-wave1" = {
    resource_group_name = "<rg-management-pro>"
    location            = "<region>"

    window = {
      start_date_time = "2026-11-14 22:00"
      duration        = "03:55"
      time_zone       = "Romance Standard Time"
      recur_every     = "Month Second Tuesday Offset4" # sábado siguiente al Patch Tuesday
    }

    reboot = "IfRequired"

    windows = {
      classifications_to_include = ["Critical", "Security", "UpdateRollup", "Definition"]
    }
    linux = {
      classifications_to_include = ["Critical", "Security"]
    }

    dynamic_scopes = {
      wave1 = {
        locations = ["<region>"]
        tags = {
          PatchGroup = ["pro-wave1"]
        }
      }
    }

    events = {
      pre-start-vms = {
        event_type  = "PreMaintenanceEvent"
        function_id = "<resourceId func-patching-pro>/functions/PreMaintenance"
      }
      post-report = {
        event_type  = "PostMaintenanceEvent"
        function_id = "<resourceId func-patching-pro>/functions/PostMaintenance"
      }
    }
  }

  "mc-patch-pro-wave2" = {
    resource_group_name = "<rg-management-pro>"
    location            = "<region>"

    window = {
      start_date_time = "2026-11-15 22:00"
      duration        = "03:55"
      time_zone       = "Romance Standard Time"
      recur_every     = "Month Second Tuesday Offset5" # domingo siguiente
    }

    windows = {
      classifications_to_include = ["Critical", "Security", "UpdateRollup", "Definition"]
    }
    linux = {
      classifications_to_include = ["Critical", "Security"]
    }

    dynamic_scopes = {
      wave2 = {
        locations = ["<region>"]
        tags = {
          PatchGroup = ["pro-wave2"]
        }
      }
    }

    # VM excepcional fuera de los tags
    virtual_machines = {
      vm-legacy-01 = {
        id       = "<resourceId vm-legacy-01>"
        location = "<region>"
      }
    }
  }
}

update_governance = {
  pro = {
    subscription_id         = "/subscriptions/<subscription-id-pro>"
    location                = "<region>"
    periodic_assessment_arc = true
  }
}
```

### Atributos de las VMs nuevas

En el módulo `Compute/Compute` del repositorio, cada VM puede nacer ya con Customer Managed Schedules y evaluación periódica:

```hcl
patch_mode                                             = "AutomaticByPlatform"
bypass_platform_safety_checks_on_user_schedule_enabled = true
patch_assessment_mode                                  = "AutomaticByPlatform"
provision_vm_agent                                     = true
```

### Despliegue y comprobación

```powershell
terraform init
terraform plan -var-file="env/pro.tfvars" -out="pro.tfplan"
terraform apply "pro.tfplan"

# Evaluación bajo demanda de una VM
Invoke-AzVMPatchAssessment -ResourceGroupName "<rg-app-pro>" -VMName "<vm-app-01>"

# VMs que aún no tienen Customer Managed Schedules
$query = @"
resources
| where type =~ 'microsoft.compute/virtualmachines'
| extend os = tostring(properties.storageProfile.osDisk.osType)
| extend settings = iff(os =~ 'Windows', properties.osProfile.windowsConfiguration.patchSettings, properties.osProfile.linuxConfiguration.patchSettings)
| extend patchMode = tostring(settings.patchMode), bypass = tobool(settings.automaticByPlatformSettings.bypassPlatformSafetyChecksOnUserSchedule)
| where patchMode != 'AutomaticByPlatform' or bypass != true
| project name, resourceGroup, os, patchMode, bypass
"@
Search-AzGraph -Query $query

# Máquinas asociadas a un calendario
$mcId = "<resourceId mc-patch-pro-wave1>"
Search-AzGraph -Query @"
maintenanceresources
| where type =~ 'microsoft.maintenance/configurationassignments'
| where properties.maintenanceConfigurationId =~ '$mcId'
| project machine = tostring(properties.resourceId), assignment = name
"@

# Ejecuciones fallidas o que agotaron la ventana (30 días)
Search-AzGraph -Query @"
patchinstallationresources
| where type endswith 'patchinstallationresults'
| where properties.status =~ 'Failed' or tobool(properties.maintenanceWindowExceeded)
| project id, status = tostring(properties.status), windowExceeded = properties.maintenanceWindowExceeded,
          failed = toint(properties.failedPatchCount), pending = toint(properties.pendingPatchCount),
          start = todatetime(properties.startDateTime)
| order by start desc
"@
```

### Equivalente en Bicep

`main.bicep` (grupo de recursos de gestión: calendarios, asignaciones estáticas y eventos):

```bicep
// =============================================================================
// Azure Update Manager: calendarios (InGuestPatch), asignaciones estáticas y eventos previos/posteriores
// Se despliega en el grupo de recursos de gestión
// DEPENDENCY: VMs con orquestación Customer Managed Schedules (governance.bicep)
// DEPENDENCY: Function App con las funciones de los eventos ya desplegada
// =============================================================================
targetScope = 'resourceGroup'

type patchWindow = {
  @description('YYYY-MM-DD hh:mm; 15 minutos o más después de crear el calendario.')
  startDateTime: string
  @description('Entre 01:30 y 03:55.')
  duration: string
  timeZone: string
  @description('Por ejemplo: Month Second Tuesday Offset4, Week Saturday.')
  recurEvery: string
  expirationDateTime: string?
}

type staticVm = {
  name: string
  resourceGroupName: string
}

type maintenanceEvent = {
  name: string
  eventType: ('PreMaintenanceEvent' | 'PostMaintenanceEvent')
  @description('{functionAppId}/functions/{nombre}')
  functionId: string
}

type maintenanceConfiguration = {
  name: string
  window: patchWindow
  rebootSetting: ('IfRequired' | 'Always' | 'Never')
  windowsClassifications: ('Critical' | 'Security' | 'UpdateRollup' | 'FeaturePack' | 'ServicePack' | 'Definition' | 'Tools' | 'Updates')[]
  windowsKbNumbersToExclude: string[]?
  linuxClassifications: ('Critical' | 'Security' | 'Other')[]
  linuxPackageNameMasksToExclude: string[]?
  staticVms: staticVm[]?
  events: maintenanceEvent[]?
}

param location string = resourceGroup().location
param maintenanceConfigurations maintenanceConfiguration[]
param tags object = {}

resource configs 'Microsoft.Maintenance/maintenanceConfigurations@2023-04-01' = [
  for mc in maintenanceConfigurations: {
    name: mc.name
    location: location
    tags: tags
    properties: {
      maintenanceScope: 'InGuestPatch'
      visibility: 'Custom'
      extensionProperties: {
        InGuestPatchMode: 'User'
      }
      maintenanceWindow: {
        startDateTime: mc.window.startDateTime
        duration: mc.window.duration
        timeZone: mc.window.timeZone
        recurEvery: mc.window.recurEvery
        expirationDateTime: mc.window.?expirationDateTime
      }
      installPatches: {
        rebootSetting: mc.rebootSetting
        windowsParameters: {
          classificationsToInclude: mc.windowsClassifications
          kbNumbersToExclude: mc.?windowsKbNumbersToExclude ?? []
        }
        linuxParameters: {
          classificationsToInclude: mc.linuxClassifications
          packageNameMasksToExclude: mc.?linuxPackageNameMasksToExclude ?? []
        }
      }
    }
  }
]

// Asignaciones estáticas: recurso de extensión sobre cada VM (módulo en el grupo de recursos de la VM)
module staticAssignments 'vm-assignment.bicep' = [
  for item in flatten(map(range(0, length(maintenanceConfigurations)), i => map(maintenanceConfigurations[i].?staticVms ?? [], vm => {
    configIndex: i
    vm: vm
  }))): {
    name: 'aum-${maintenanceConfigurations[item.configIndex].name}-${item.vm.name}'
    scope: resourceGroup(item.vm.resourceGroupName)
    params: {
      vmName: item.vm.name
      location: location
      maintenanceConfigurationId: configs[item.configIndex].id
    }
  }
]

// Eventos: un system topic por calendario con eventos
resource topics 'Microsoft.EventGrid/systemTopics@2025-02-15' = [
  for (mc, i) in maintenanceConfigurations: if (!empty(mc.?events ?? [])) {
    name: 'evgt-${mc.name}'
    location: location
    tags: tags
    properties: {
      source: configs[i].id
      topicType: 'Microsoft.Maintenance.MaintenanceConfigurations'
    }
  }
]

module eventSubscriptions 'event-subscription.bicep' = [
  for item in flatten(map(range(0, length(maintenanceConfigurations)), i => map(maintenanceConfigurations[i].?events ?? [], ev => {
    configIndex: i
    event: ev
  }))): {
    name: 'aum-evt-${maintenanceConfigurations[item.configIndex].name}-${item.event.name}'
    params: {
      systemTopicName: 'evgt-${maintenanceConfigurations[item.configIndex].name}'
      name: item.event.name
      eventType: item.event.eventType
      functionId: item.event.functionId
    }
    dependsOn: [
      topics
    ]
  }
]

output maintenanceConfigurationIds array = [for (mc, i) in maintenanceConfigurations: configs[i].id]
```

`vm-assignment.bicep`:

```bicep
// Asignación estática de una VM a un calendario de Update Manager
// DEPENDENCY: VM existente en este grupo de recursos y en la misma suscripción que el calendario
param vmName string
param location string
param maintenanceConfigurationId string

resource vm 'Microsoft.Compute/virtualMachines@2024-11-01' existing = {
  name: vmName
}

resource assignment 'Microsoft.Maintenance/configurationAssignments@2023-04-01' = {
  name: last(split(maintenanceConfigurationId, '/'))
  scope: vm
  location: location
  properties: {
    maintenanceConfigurationId: maintenanceConfigurationId
  }
}
```

`event-subscription.bicep`:

```bicep
// Evento previo o posterior de un calendario hacia una función (sin secretos en la plantilla)
// DEPENDENCY: system topic del calendario creado en este grupo de recursos
param systemTopicName string
param name string

@allowed(['PreMaintenanceEvent', 'PostMaintenanceEvent'])
param eventType string

@description('{functionAppId}/functions/{nombre}')
param functionId string

resource topic 'Microsoft.EventGrid/systemTopics@2025-02-15' existing = {
  name: systemTopicName
}

resource subscription 'Microsoft.EventGrid/systemTopics/eventSubscriptions@2025-02-15' = {
  parent: topic
  name: name
  properties: {
    eventDeliverySchema: 'EventGridSchema'
    destination: {
      endpointType: 'AzureFunction'
      properties: {
        resourceId: functionId
      }
    }
    filter: {
      includedEventTypes: [
        'Microsoft.Maintenance.${eventType}'
      ]
    }
  }
}
```

`subscription.bicep` (ámbitos dinámicos y Azure Policy en la suscripción):

```bicep
// =============================================================================
// Ámbito de suscripción: ámbitos dinámicos de Update Manager y gobierno con Azure Policy
// DEPENDENCY: calendarios creados (salida maintenanceConfigurationIds de main.bicep)
// DEPENDENCY: identidad del despliegue con permiso para asignar roles en la suscripción
// =============================================================================
targetScope = 'subscription'

type dynamicScope = {
  @description('Único en la suscripción.')
  name: string
  maintenanceConfigurationId: string
  locations: string[]?
  osTypes: ('Windows' | 'Linux')[]?
  resourceGroups: string[]?
  @description('Etiqueta -> valores admitidos.')
  tags: object?
  tagOperator: ('Any' | 'All')?
}

param location string
param dynamicScopes dynamicScope[] = []

@description('Sistemas operativos para la evaluación periódica (una asignación por SO).')
param osTypes array = [
  'Windows'
  'Linux'
]

param periodicAssessmentArc bool = false
param remediateExisting bool = true

var contributorRoleId = 'b24988ac-6180-42a0-ab88-20f7382dd24c'
var arcAdminRoleId = 'cd570a14-e51a-42ad-bac8-bafd67325302'

// -----------------------------------------------------------------------------
// Ámbitos dinámicos (sin región: la asignación es de suscripción)
// -----------------------------------------------------------------------------
resource scopes 'Microsoft.Maintenance/configurationAssignments@2023-04-01' = [
  for s in dynamicScopes: {
    name: s.name
    properties: {
      maintenanceConfigurationId: s.maintenanceConfigurationId
      filter: {
        resourceTypes: [
          'Microsoft.Compute/virtualMachines'
          'Microsoft.HybridCompute/machines'
        ]
        locations: s.?locations ?? []
        osTypes: s.?osTypes ?? ['Windows', 'Linux']
        resourceGroups: s.?resourceGroups ?? []
        tagSettings: {
          tags: s.?tags ?? {}
          filterOperator: s.?tagOperator ?? 'Any'
        }
      }
    }
  }
]

// -----------------------------------------------------------------------------
// Evaluación periódica (Modify) en VMs y, opcionalmente, en Arc
// -----------------------------------------------------------------------------
var assessments = concat(
  map(osTypes, os => {
    name: 'aum-assess-vm-${toLower(os)}'
    os: os
    definition: '59efceea-0c96-497e-a4a1-4eb2290dac15'
    roleId: contributorRoleId
  }),
  periodicAssessmentArc
    ? map(osTypes, os => {
        name: 'aum-assess-arc-${toLower(os)}'
        os: os
        definition: 'bfea026e-043f-4ff4-9d1b-bf301ca7ff46'
        roleId: arcAdminRoleId
      })
    : []
)

resource assessmentAssignments 'Microsoft.Authorization/policyAssignments@2024-04-01' = [
  for a in assessments: {
    name: a.name
    location: location
    identity: {
      type: 'SystemAssigned'
    }
    properties: {
      displayName: 'Update Manager: evaluación periódica (${a.name})'
      policyDefinitionId: '/providers/Microsoft.Authorization/policyDefinitions/${a.definition}'
      parameters: {
        assessmentMode: {
          value: 'AutomaticByPlatform'
        }
        osType: {
          value: a.os
        }
      }
      nonComplianceMessages: [
        {
          message: 'La máquina no tiene activada la evaluación periódica de actualizaciones.'
        }
      ]
    }
  }
]

resource assessmentRoles 'Microsoft.Authorization/roleAssignments@2022-04-01' = [
  for (a, i) in assessments: {
    name: guid(subscription().id, a.name, a.roleId)
    properties: {
      principalId: assessmentAssignments[i].identity.principalId
      principalType: 'ServicePrincipal'
      roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', a.roleId)
    }
  }
]

resource assessmentRemediations 'Microsoft.PolicyInsights/remediations@2021-10-01' = [
  for (a, i) in assessments: if (remediateExisting) {
    name: 'remediate-${a.name}'
    properties: {
      policyAssignmentId: assessmentAssignments[i].id
      resourceDiscoveryMode: 'ExistingNonCompliant'
    }
    dependsOn: [
      assessmentRoles
    ]
  }
]

// -----------------------------------------------------------------------------
// Requisito "Customer Managed Schedules" en VMs (DeployIfNotExists)
// -----------------------------------------------------------------------------
resource prerequisite 'Microsoft.Authorization/policyAssignments@2024-04-01' = {
  name: 'aum-prereq'
  location: location
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    displayName: 'Update Manager: Customer Managed Schedules en VMs'
    policyDefinitionId: '/providers/Microsoft.Authorization/policyDefinitions/9905ca54-1471-49c6-8291-7582c04cd4d4'
    parameters: {
      operatingSystemTypes: {
        value: osTypes
      }
      effect: {
        value: 'DeployIfNotExists'
      }
    }
  }
}

resource prerequisiteRole 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(subscription().id, 'aum-prereq', contributorRoleId)
  properties: {
    principalId: prerequisite.identity.principalId
    principalType: 'ServicePrincipal'
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', contributorRoleId)
  }
}

resource prerequisiteRemediation 'Microsoft.PolicyInsights/remediations@2021-10-01' = if (remediateExisting) {
  name: 'remediate-aum-prereq'
  properties: {
    policyAssignmentId: prerequisite.id
    resourceDiscoveryMode: 'ExistingNonCompliant'
  }
  dependsOn: [
    prerequisiteRole
  ]
}

// -----------------------------------------------------------------------------
// Auditoría
// -----------------------------------------------------------------------------
resource audit 'Microsoft.Authorization/policyAssignments@2024-04-01' = {
  name: 'aum-audit'
  properties: {
    displayName: 'Machines should be configured to periodically check for missing system updates'
    policyDefinitionId: '/providers/Microsoft.Authorization/policyDefinitions/bd876905-5b84-4f73-ab2d-2e7a7c4568d9'
    parameters: {
      effect: {
        value: 'Audit'
      }
    }
  }
}
```

`main.pro.bicepparam`:

```bicep
using 'main.bicep'

param maintenanceConfigurations = [
  {
    name: 'mc-patch-pro-wave1'
    window: {
      startDateTime: '2026-11-14 22:00'
      duration: '03:55'
      timeZone: 'Romance Standard Time'
      recurEvery: 'Month Second Tuesday Offset4'
    }
    rebootSetting: 'IfRequired'
    windowsClassifications: [
      'Critical'
      'Security'
      'UpdateRollup'
      'Definition'
    ]
    linuxClassifications: [
      'Critical'
      'Security'
    ]
    events: [
      {
        name: 'pre-start-vms'
        eventType: 'PreMaintenanceEvent'
        functionId: '<resourceId func-patching-pro>/functions/PreMaintenance'
      }
    ]
  }
  {
    name: 'mc-patch-pro-wave2'
    window: {
      startDateTime: '2026-11-15 22:00'
      duration: '03:55'
      timeZone: 'Romance Standard Time'
      recurEvery: 'Month Second Tuesday Offset5'
    }
    rebootSetting: 'IfRequired'
    windowsClassifications: [
      'Critical'
      'Security'
      'UpdateRollup'
      'Definition'
    ]
    linuxClassifications: [
      'Critical'
      'Security'
    ]
    staticVms: [
      {
        name: 'vm-legacy-01'
        resourceGroupName: '<rg-app-pro>'
      }
    ]
  }
]

param tags = {
  environment: 'pro'
  workload: '<workload>'
}
```

`subscription.pro.bicepparam`:

```bicep
using 'subscription.bicep'

param location = '<region>'

param dynamicScopes = [
  {
    name: 'mc-patch-pro-wave1-wave1'
    maintenanceConfigurationId: '<resourceId mc-patch-pro-wave1>'
    locations: [
      '<region>'
    ]
    tags: {
      PatchGroup: [
        'pro-wave1'
      ]
    }
  }
  {
    name: 'mc-patch-pro-wave2-wave2'
    maintenanceConfigurationId: '<resourceId mc-patch-pro-wave2>'
    locations: [
      '<region>'
    ]
    tags: {
      PatchGroup: [
        'pro-wave2'
      ]
    }
  }
]

param periodicAssessmentArc = true
```

Despliegue:

```powershell
$main = New-AzResourceGroupDeployment -ResourceGroupName "<rg-management-pro>" -TemplateParameterFile "main.pro.bicepparam"
$main.Outputs.maintenanceConfigurationIds.Value

New-AzSubscriptionDeployment -Location "<region>" -TemplateParameterFile "subscription.pro.bicepparam"
```

## Errores típicos

| Síntoma | Causa | Solución |
|---|---|---|
| El calendario se ejecuta pero no parchea una VM de Azure | La VM no está en Customer Managed Schedules | Política de requisito o atributos `patch_mode` + `bypass_platform_safety_checks_on_user_schedule_enabled` |
| La VM se parchea fuera del calendario | Modo `AutomaticByOS` o *Azure Managed - Safe Deployment* | Customer Managed Schedules |
| Reinicio con `reboot = "Never"` | Claves de registro de Windows Update que fuerzan el reinicio | Revisar la configuración del agente de Windows Update |
| *Failed* con `maintenanceWindowExceeded = true` | Ventana corta (un service pack necesita 20 minutos libres) | Ventana más larga o menos máquinas por oleada |
| No se instala nada y no hay errores de parche | Quedaban menos de 25 minutos al empezar | Revisar solapes de ventanas o ampliarlas |
| La creación de la ventana falla | Duración fuera de 1 h 30 – 3 h 55, recurrencia menor de 6 horas o inicio a menos de 15 minutos | Ajustar la ventana |
| El calendario se salta una ejecución | Creado o modificado cerca de las 00:00 o menos de 15 minutos antes del inicio | Cambios con margen; 40 minutos si hay evento previo |
| Una VM movida de grupo de recursos o suscripción deja de parchearse | Las asignaciones no siguen al recurso | Quitar la asignación, mover y volver a asignar |
| Ámbito dinámico que no parchea nada | Más de 200 suscripciones en el ámbito (el cálculo de máquinas falla por limitación de peticiones) o filtros que no coinciden con ninguna máquina | Revisar límites y filtros; indicar las regiones en los ámbitos por grupo de recursos |
| Varias VMs del mismo conjunto de disponibilidad fallan | Calendarios simultáneos sobre el mismo conjunto | Ampliar ventana o separar por horario |
| VMs apagadas sin parches | El calendario no las enciende | Evento previo que las arranque y posterior que las apague |
| El evento previo falla y se parchea igualmente | La cancelación no es automática | Llamar a la API de cancelación desde el evento previo |
| El evento se ejecuta dos veces | Event Grid entrega al menos una vez | Acciones idempotentes |
| `visibility = "Public"` rechazado | El provider solo admite `Custom` | `Custom` |
| Error de `install_patches` o `in_guest_user_patch_mode` en el `apply` | El módulo no los exige con `InGuestPatch` | Pasarlos siempre (la ficha lo hace) |
| Remediación de la evaluación periódica fallida en imágenes de galería o especializadas | Limitación conocida de la política | Lanzar de nuevo la remediación tras crear la VM |
| La extensión de Update Manager no queda *Succeeded* | Error de instalación del agente | Quitar la extensión y lanzar una evaluación bajo demanda |
| Windows 10/11, scale sets o AKS sin parches | No soportados | Intune, actualización de imagen de VMSS o actualización de nodos de AKS |
