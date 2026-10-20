---
title: "Scaling Plans"
indice: avd
resumen: "Encendido y apagado automático según la demanda."
estado: documentado   # proximamente | en-curso | documentado
orden: 5
last_review: 2026-10-20
fuentes:
  - titulo: "Autoscale scaling plans and example scenarios"
    url: https://learn.microsoft.com/azure/virtual-desktop/autoscale-scenarios
  - titulo: "Create and assign an autoscale scaling plan"
    url: https://learn.microsoft.com/azure/virtual-desktop/autoscale-create-assign-scaling-plan
  - titulo: "Autoscale glossary"
    url: https://learn.microsoft.com/azure/virtual-desktop/autoscale-glossary
  - titulo: "Azure Virtual Desktop autoscale FAQ"
    url: https://learn.microsoft.com/azure/virtual-desktop/autoscale-faq
  - titulo: "Troubleshoot autoscale issues"
    url: https://learn.microsoft.com/troubleshoot/azure/virtual-desktop/troubleshoot-autoscale
  - titulo: "Monitor autoscale operations with Insights"
    url: https://learn.microsoft.com/azure/virtual-desktop/autoscale-monitor-operations-insights
  - titulo: "Built-in Azure RBAC roles for Azure Virtual Desktop"
    url: https://learn.microsoft.com/azure/virtual-desktop/rbac
  - titulo: "Assign RBAC roles to the Azure Virtual Desktop service principals"
    url: https://learn.microsoft.com/azure/virtual-desktop/service-principal-assign-roles
  - titulo: "Configure Start VM on Connect"
    url: https://learn.microsoft.com/azure/virtual-desktop/start-virtual-machine-connect
  - titulo: "Hibernation for Azure virtual machines"
    url: https://learn.microsoft.com/azure/virtual-machines/hibernate-resume
  - titulo: "Supported logs for Microsoft.DesktopVirtualization/scalingplans"
    url: https://learn.microsoft.com/azure/azure-monitor/reference/supported-logs/microsoft-desktopvirtualization-scalingplans-logs
  - titulo: "Microsoft.DesktopVirtualization scalingPlans (plantillas ARM/Bicep)"
    url: https://learn.microsoft.com/azure/templates/microsoft.desktopvirtualization/scalingplans
  - titulo: "azurerm_virtual_desktop_scaling_plan"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/virtual_desktop_scaling_plan
  - titulo: "azurerm_virtual_desktop_scaling_plan_host_pool_association"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/virtual_desktop_scaling_plan_host_pool_association
  - titulo: "azapi_resource"
    url: https://registry.terraform.io/providers/Azure/azapi/latest/docs/resources/resource
  - titulo: "Submódulo Terraform VDI/modules/virtual_desktop_scaling_plan"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/AzureVirtualDesktop/VDI/modules/virtual_desktop_scaling_plan
  - titulo: "Submódulo Terraform VDI/modules/virtual_desktop_scaling_plan_host_pool_association"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/AzureVirtualDesktop/VDI/modules/virtual_desktop_scaling_plan_host_pool_association
  - titulo: "Módulo Terraform AzureVirtualDesktop/ScalingPlan"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/AzureVirtualDesktop/ScalingPlan
---

Un **scaling plan** es el autoscale nativo de Azure Virtual Desktop. Enciende y apaga (desasigna) los session hosts de uno o varios [host pools](/recursos/avd/host-pools/) según un horario y la ocupación real. No tiene coste propio y es **la palanca de ahorro más grande de AVD**: una VM desasignada no paga cómputo. Sustituye a la antigua herramienta de escalado con Azure Automation y Logic Apps, y no se pueden usar las dos a la vez en el mismo host pool.

## Qué es y cuándo usarlo

### Métodos de escalado

| Método | Qué hace | Host pools | Estado |
|---|---|---|---|
| **Gestión de energía** (recomendado) | Enciende y desasigna session hosts existentes | Pooled y Personal con gestión *standard* | Disponible de forma general |
| Dinámico | Además crea y elimina session hosts entre un mínimo y un máximo | Solo pooled con *session host configuration* | Preview; no disponible en Azure Government |

### Las cuatro fases de cada programación

| Fase | Momento | Qué suele configurarse |
|---|---|---|
| **Ramp-up** | Inicio de la jornada | % mínimo de hosts encendidos y umbral de capacidad; BreadthFirst |
| **Peak** | Horas de más uso | Algoritmo; hereda el umbral del ramp-up |
| **Ramp-down** | Cuando baja el uso | % mínimo, umbral, cierre forzoso o no; DepthFirst para concentrar sesiones |
| **Off-peak** | Noches y fines de semana | Algoritmo; hereda el umbral del ramp-down |

Los días sin programación heredan la configuración *off-peak* del último día programado hasta el siguiente ramp-up. Por ejemplo, con un solo horario de lunes a viernes, el fin de semana se queda en el off-peak del viernes.

### Pooled: cómo decide encender o apagar

- **Capacidad disponible** = hosts encendidos × límite de sesiones del host pool. **Capacidad usada** = sesiones / capacidad disponible.
- Si la capacidad usada **supera** el umbral, enciende otro host, en cualquier fase.
- En ramp-down y off-peak solo apaga un host si todas las sesiones caben en menos hosts sin pasar el umbral. **Las sesiones desconectadas cuentan como activas.**
- Hosts necesarios = sesiones (activas + desconectadas) / (límite de sesiones × umbral), redondeado hacia arriba.
- Al apagar un host, lo pone en drain mode, avisa a los usuarios y lo desasigna. Con *force logoff*, cierra las sesiones pasado el tiempo de espera.

### Personal: qué controla

| Ajuste | Opciones |
|---|---|
| Encendido al inicio del ramp-up | Ninguna VM, solo las asignadas a un usuario, o todas |
| Start VM on Connect por fase | Activado o desactivado |
| Al desconectarse el usuario (tras 0–360 min) | Desasignar, hibernar o nada |
| Al cerrar sesión (tras 0–360 min) | Desasignar, hibernar o nada |

La **hibernación** solo existe en host pools personales y **no es compatible con FSLogix ni App Attach**.

### Reglas que conviene tener a mano

| Regla | Detalle |
|---|---|
| Asignación | Un scaling plan puede ir a varios host pools del **mismo tipo**; cada host pool admite **un** scaling plan |
| Tipo | Pooled o Personal; **no se cambia después** de crearlo |
| Región | La misma que la de los host pools |
| Zona horaria | El plan solo opera en la suya |
| Límite de sesiones | Obligatorio un `maximum_sessions_allowed` propio en pooled (el valor por defecto no sirve) |
| Algoritmo de reparto | En pooled, el del plan sustituye al del host pool |
| Drain mode | En pooled, autoscale lo sobrescribe: para mantenimiento se usa la **etiqueta de exclusión** |
| Permisos | *Desktop Virtualization Power On Off Contributor* **en la suscripción**; por debajo autoscale no funciona bien |
| Otras herramientas | Ni la herramienta de escalado con Automation ni herramientas de terceros sobre el mismo host pool |

### Qué escenario recomiendo

| Escenario del cliente | Diseño | Por qué |
|---|---|---|
| Oficina con horario estable | Pooled: ramp-up 25 %/60 %, ramp-down 0 %/90 % sin cierre forzoso, off-peak 0 % | Apaga todo de noche sin echar a nadie |
| Coste por encima de todo | Lo anterior + cierre forzoso en ramp-down + política de cierre de sesiones desconectadas | Llega a cero hosts fuera de horario |
| Turnos o 24×7 | Varias programaciones por días y % mínimo > 0 en off-peak | Siempre hay capacidad para el turno |
| Puestos personales | Plan personal con Start VM on Connect y desasignar tras desconexión o cierre de sesión | Cada VM solo consume cuando su usuario trabaja |
| Personales sin FSLogix que deben reanudar rápido | Hibernar en lugar de desasignar | El usuario vuelve a su sesión tal como la dejó |

### Datos que conviene llevar a la reunión

- **Autoscale no cuesta nada**: el ahorro sale de las horas de VM desasignadas.
- **Para llegar a cero hosts por la noche** no basta con el plan: las sesiones desconectadas mantienen hosts encendidos. Hace falta además la política *Set time limit for disconnected sessions* (Intune o GPO), por ejemplo de 15–30 minutos.
- **El cierre forzoso cierra también sesiones activas** cuando vence el tiempo de espera: se pacta con negocio.
- **Para mantenimiento se usa la etiqueta de exclusión**, no el drain mode, porque autoscale lo deshace en pooled.
- **El autoscale dinámico** (crear y borrar hosts) **sigue en preview** y solo vale con *session host configuration*.

## Decisiones de diseño

| Decisión | Lo que aplico | Por qué |
|---|---|---|
| Método | Gestión de energía | Disponible de forma general y compatible con hosts desplegados por IaC |
| Programaciones | Laborables y fin de semana por separado, en la zona horaria del negocio (`Romance Standard Time`) | Los días sin programación arrastran el off-peak |
| Algoritmos | BreadthFirst en ramp-up y peak; DepthFirst en ramp-down y off-peak | Experiencia por el día y consolidación por la noche |
| Umbrales | Ramp-up 60 %, ramp-down 90 %; % mínimo según el primer pico de inicios de sesión | Margen al empezar el día y consolidación agresiva al final |
| Cierre de sesiones | Sin cierre forzoso por defecto + política de cierre de desconectadas (15–30 min) | Ahorro sin cortar a usuarios conectados |
| Mantenimiento | Etiqueta de exclusión `excludeFromScaling` en las VMs | Autoscale no las enciende, apaga ni cambia su drain mode |
| Permisos | *Power On Off Contributor* en la suscripción al service principal de AVD | Requisito del servicio; incluye el encendido de Start VM on Connect |
| Personales | Start VM on Connect en todas las fases y desasignar tras desconexión o cierre | Las VMs solo encendidas con su usuario |
| Observabilidad | Categoría `Autoscale` del scaling plan y `AutoscaleEvaluationPooled` del host pool en Log Analytics; AVD Insights | Ver por qué encendió o apagó cada host |

Alineación con el Well-Architected Framework:

- **Coste**: el pilar principal; horas de cómputo solo cuando hay usuarios.
- **Fiabilidad**: % mínimo y umbrales que dejan margen al primer pico.
- **Rendimiento**: BreadthFirst en horas punta y umbral de ramp-up conservador.
- **Excelencia operativa**: programaciones en IaC, etiqueta de exclusión para mantenimiento y diagnósticos.
- **Seguridad**: permisos acotados a los roles de AVD (no *Contributor*).

## Módulo de Terraform

### Los módulos del repositorio

| Pieza | Módulo | Estado |
|---|---|---|
| Scaling plan pooled | [`AzureVirtualDesktop/VDI/modules/virtual_desktop_scaling_plan`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/AzureVirtualDesktop/VDI/modules/virtual_desktop_scaling_plan) | Utilizable (recomendado) |
| Asignación a host pools | [`AzureVirtualDesktop/VDI/modules/virtual_desktop_scaling_plan_host_pool_association`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/AzureVirtualDesktop/VDI/modules/virtual_desktop_scaling_plan_host_pool_association) | Utilizable |
| Scaling plan (independiente) | [`AzureVirtualDesktop/ScalingPlan`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/AzureVirtualDesktop/ScalingPlan) | Utilizable con condiciones |

Los submódulos de `VDI` no usan `locals`. El del scaling plan admite asignaciones en línea (bloques `host_pool`); la ficha las deja a `null` y usa el recurso de asociación para no mezclar los dos mecanismos.

`AzureVirtualDesktop/ScalingPlan` usa `locals` y `count`, y pone `time_zone = "UTC"` por defecto: con ese valor la programación se desplaza una hora respecto a la hora local con cada cambio de horario.

**`azurerm` solo soporta scaling plans de host pools pooled**: `azurerm_virtual_desktop_scaling_plan` no tiene tipo de host pool ni programaciones personales. Los planes personales van con **azapi**. Ningún módulo cubre el rol *Power On Off Contributor* ni los *diagnostic settings*.

**Ajuste en la ficha de Host Pools**: si se usan scaling plans, el rol *Desktop Virtualization Power On Contributor* de `avd_power_on_assignments` sobra. *Power On Off Contributor*, asignado aquí en la suscripción, ya incluye el encendido.

### Estructura en el proyecto

```txt
/
├── providers.tf            # añade azapi
├── host_pools.tf           # ficha Host Pools
├── session_hosts.tf        # ficha Session Hosts
├── application_groups.tf   # ficha Application Groups
├── workspaces.tf           # ficha Workspaces
├── scaling_plans.tf        # scaling plans pooled (azurerm) y personales (azapi), permisos y diagnósticos
└── env/
    ├── dev.tfvars
    ├── pre.tfvars
    └── pro.tfvars
```

### `providers.tf`

```hcl
# Mismo providers.tf del proyecto de AVD, con azapi para los scaling plans de host pools personales
terraform {
  required_version = ">= 1.6.0"
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      # < 5.0.0: restricción de los módulos de AzureTerraformModules.
      version = ">= 4.0.0, < 5.0.0"
    }
    azapi = {
      source  = "Azure/azapi"
      version = ">= 2.0.0, < 3.0.0" # azurerm solo soporta scaling plans de host pools pooled
    }
    time = {
      source  = "hashicorp/time"
      version = ">= 0.11.0" # rotación del token de registro (host_pools.tf)
    }
  }
}

provider "azurerm" {
  features {}
}

provider "azapi" {}

variable "tags" {
  description = "Tags corporativos comunes a todos los recursos."
  type        = map(string)
}
```

### Scaling plans · `scaling_plans.tf`

```hcl
# =============================================================================
# Scaling plans (autoscale de gestión de energía)
# Pooled: submódulos AzureVirtualDesktop/VDI/modules (azurerm)
# Personal: azapi (azurerm no soporta scaling plans de host pools personales)
# DEPENDENCY: host_pools.tf de la ficha Host Pools en el mismo root (module.host_pool)
# DEPENDENCY: Host pools pooled con maximum_sessions_allowed definido (no el valor por defecto)
# DEPENDENCY: Rol Desktop Virtualization Power On Off Contributor a nivel de SUSCRIPCIÓN
#             para el service principal de AVD (o la identidad del host pool)
# DEPENDENCY: Política de cierre de sesiones desconectadas en los session hosts (Intune o GPO)
# =============================================================================

variable "pooled_scaling_plans" {
  description = "Scaling plans para host pools pooled (clave = nombre del scaling plan)."
  type = map(object({
    resource_group_name = string
    location            = string # la misma región que los host pools
    time_zone           = string # p. ej. "Romance Standard Time"
    friendly_name       = optional(string)
    description         = optional(string)
    exclusion_tag       = optional(string, "excludeFromScaling")
    host_pools          = list(string) # claves de var.host_pools (todos Pooled)

    schedules = map(object({
      days_of_week = list(string)

      ramp_up_start_time                 = string # "HH:MM"
      ramp_up_load_balancing_algorithm   = optional(string, "BreadthFirst")
      ramp_up_minimum_hosts_percent      = number
      ramp_up_capacity_threshold_percent = number

      peak_start_time               = string
      peak_load_balancing_algorithm = optional(string, "BreadthFirst")

      ramp_down_start_time                 = string
      ramp_down_load_balancing_algorithm   = optional(string, "DepthFirst")
      ramp_down_minimum_hosts_percent      = number
      ramp_down_capacity_threshold_percent = number
      ramp_down_force_logoff_users         = optional(bool, false)
      ramp_down_wait_time_minutes          = optional(number, 30)
      ramp_down_notification_message       = optional(string, "El escritorio se va a apagar. Guarda tu trabajo y cierra la sesión.")
      ramp_down_stop_hosts_when            = optional(string, "ZeroActiveSessions") # ZeroSessions | ZeroActiveSessions

      off_peak_start_time               = string
      off_peak_load_balancing_algorithm = optional(string, "DepthFirst")
    }))

    log_analytics_workspace_id = string
    tags                       = optional(map(string), {})
  }))
  default = {}

  validation {
    condition = alltrue(flatten([
      for k, v in var.pooled_scaling_plans : [
        for sk, s in v.schedules : [
          s.ramp_up_capacity_threshold_percent >= 1, s.ramp_up_capacity_threshold_percent <= 100,
          s.ramp_down_capacity_threshold_percent >= 1, s.ramp_down_capacity_threshold_percent <= 100,
          s.ramp_up_minimum_hosts_percent >= 0, s.ramp_up_minimum_hosts_percent <= 100,
          s.ramp_down_minimum_hosts_percent >= 0, s.ramp_down_minimum_hosts_percent <= 100,
        ]
      ]
    ]))
    error_message = "Umbral de capacidad entre 1 y 100 y porcentaje mínimo de hosts entre 0 y 100."
  }

  validation {
    condition = alltrue(flatten([
      for k, v in var.pooled_scaling_plans : [
        for sk, s in v.schedules : contains(["ZeroSessions", "ZeroActiveSessions"], s.ramp_down_stop_hosts_when)
      ]
    ]))
    error_message = "ramp_down_stop_hosts_when debe ser ZeroSessions o ZeroActiveSessions."
  }

  validation {
    # Un host pool solo puede tener un scaling plan
    condition     = length(flatten([for k, v in var.pooled_scaling_plans : v.host_pools])) == length(distinct(flatten([for k, v in var.pooled_scaling_plans : v.host_pools])))
    error_message = "Un host pool solo puede asignarse a un scaling plan."
  }
}

variable "personal_scaling_plans" {
  description = "Scaling plans para host pools personales (clave = nombre del scaling plan)."
  type = map(object({
    resource_group_name = string
    location            = string
    time_zone           = string
    friendly_name       = optional(string)
    description         = optional(string)
    exclusion_tag       = optional(string, "excludeFromScaling")
    host_pools          = list(string) # claves de var.host_pools (todos Personal)

    schedules = map(object({
      days_of_week = list(string)

      ramp_up_start_time          = string                   # "HH:MM"
      ramp_up_auto_start_hosts    = optional(string, "None")   # None | WithAssignedUser | All
      ramp_up_start_vm_on_connect = optional(string, "Enable") # Enable | Disable
      peak_start_time             = string
      ramp_down_start_time        = string
      off_peak_start_time         = string

      # Para todas las fases: acción y espera (0-360 min) tras desconexión y tras cierre de sesión
      action_on_disconnect          = optional(string, "Deallocate") # None | Deallocate | Hibernate
      minutes_to_wait_on_disconnect = optional(number, 60)
      action_on_logoff              = optional(string, "Deallocate")
      minutes_to_wait_on_logoff     = optional(number, 15)
    }))

    log_analytics_workspace_id = string
    tags                       = optional(map(string), {})
  }))
  default = {}

  validation {
    condition = alltrue(flatten([
      for k, v in var.personal_scaling_plans : [
        for sk, s in v.schedules : [
          s.minutes_to_wait_on_disconnect >= 0, s.minutes_to_wait_on_disconnect <= 360,
          s.minutes_to_wait_on_logoff >= 0, s.minutes_to_wait_on_logoff <= 360,
          contains(["None", "Deallocate", "Hibernate"], s.action_on_disconnect),
          contains(["None", "Deallocate", "Hibernate"], s.action_on_logoff),
          contains(["None", "WithAssignedUser", "All"], s.ramp_up_auto_start_hosts),
        ]
      ]
    ]))
    error_message = "Esperas entre 0 y 360 minutos; acciones None, Deallocate o Hibernate; ramp_up_auto_start_hosts None, WithAssignedUser o All."
  }
}

variable "avd_power_on_off_assignments" {
  description = <<-EOT
    Rol 'Desktop Virtualization Power On Off Contributor' a nivel de suscripción (por debajo autoscale no funciona).
    principal_id = object ID del service principal de Azure Virtual Desktop (aplicación 9cdead84-a844-4324-93f2-b2e6bb768d07).
    Incluye el permiso de encendido: sustituye a 'Power On Contributor' de Start VM on Connect.
  EOT
  type = map(object({
    principal_id    = string
    subscription_id = string
  }))
  default = {}
}

# --- Pooled (azurerm) --------------------------------------------------------

module "scaling_plan_pooled" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//AzureVirtualDesktop/VDI/modules/virtual_desktop_scaling_plan?ref=main"
  for_each = var.pooled_scaling_plans

  virtual_desktop_scaling_plan_name = each.key
  resource_group_name               = each.value.resource_group_name
  location                          = each.value.location
  time_zone                         = each.value.time_zone
  friendly_name                     = each.value.friendly_name
  description                       = each.value.description
  exclusion_tag                     = each.value.exclusion_tag

  # Las asignaciones van en el recurso de asociación (no mezclar con bloques host_pool en línea)
  host_pool = null

  schedule = [
    for sk, s in each.value.schedules : merge(s, { name = sk })
  ]

  tags = merge(var.tags, each.value.tags)
}

module "scaling_plan_pooled_association" {
  source = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//AzureVirtualDesktop/VDI/modules/virtual_desktop_scaling_plan_host_pool_association?ref=main"
  for_each = {
    for item in flatten([
      for pk, p in var.pooled_scaling_plans : [
        for hp in p.host_pools : { key = "${pk}/${hp}", plan = pk, host_pool = hp }
      ]
    ]) : item.key => item
  }

  scaling_plan_id = module.scaling_plan_pooled[each.value.plan].id
  host_pool_id    = module.host_pool[each.value.host_pool].id
  enabled         = true

  depends_on = [azurerm_role_assignment.avd_power_on_off]
}

# --- Personal (azapi) --------------------------------------------------------

resource "azapi_resource" "scaling_plan_personal" {
  for_each  = var.personal_scaling_plans
  type      = "Microsoft.DesktopVirtualization/scalingPlans@2025-10-10"
  name      = each.key
  location  = each.value.location
  parent_id = "/subscriptions/${data.azurerm_client_config.current.subscription_id}/resourceGroups/${each.value.resource_group_name}"
  tags      = merge(var.tags, each.value.tags)

  body = {
    properties = {
      hostPoolType = "Personal"
      timeZone     = each.value.time_zone
      friendlyName = coalesce(each.value.friendly_name, each.key)
      description  = coalesce(each.value.description, "")
      exclusionTag = each.value.exclusion_tag
      hostPoolReferences = [
        for hp in each.value.host_pools : {
          hostPoolArmPath    = module.host_pool[hp].id
          scalingPlanEnabled = true
        }
      ]
    }
  }

  depends_on = [azurerm_role_assignment.avd_power_on_off]
}

resource "azapi_resource" "scaling_plan_personal_schedule" {
  for_each = {
    for item in flatten([
      for pk, p in var.personal_scaling_plans : [
        for sk, s in p.schedules : { key = "${pk}/${sk}", plan = pk, name = sk, s = s }
      ]
    ]) : item.key => item
  }

  type      = "Microsoft.DesktopVirtualization/scalingPlans/personalSchedules@2025-10-10"
  name      = each.value.name
  parent_id = azapi_resource.scaling_plan_personal[each.value.plan].id

  body = {
    properties = {
      daysOfWeek = each.value.s.days_of_week

      rampUpStartTime                 = { hour = tonumber(split(":", each.value.s.ramp_up_start_time)[0]), minute = tonumber(split(":", each.value.s.ramp_up_start_time)[1]) }
      rampUpAutoStartHosts            = each.value.s.ramp_up_auto_start_hosts
      rampUpStartVMOnConnect          = each.value.s.ramp_up_start_vm_on_connect
      rampUpActionOnDisconnect        = each.value.s.action_on_disconnect
      rampUpMinutesToWaitOnDisconnect = each.value.s.minutes_to_wait_on_disconnect
      rampUpActionOnLogoff            = each.value.s.action_on_logoff
      rampUpMinutesToWaitOnLogoff     = each.value.s.minutes_to_wait_on_logoff

      peakStartTime                 = { hour = tonumber(split(":", each.value.s.peak_start_time)[0]), minute = tonumber(split(":", each.value.s.peak_start_time)[1]) }
      peakStartVMOnConnect          = "Enable"
      peakActionOnDisconnect        = each.value.s.action_on_disconnect
      peakMinutesToWaitOnDisconnect = each.value.s.minutes_to_wait_on_disconnect
      peakActionOnLogoff            = each.value.s.action_on_logoff
      peakMinutesToWaitOnLogoff     = each.value.s.minutes_to_wait_on_logoff

      rampDownStartTime                 = { hour = tonumber(split(":", each.value.s.ramp_down_start_time)[0]), minute = tonumber(split(":", each.value.s.ramp_down_start_time)[1]) }
      rampDownStartVMOnConnect          = "Enable"
      rampDownActionOnDisconnect        = each.value.s.action_on_disconnect
      rampDownMinutesToWaitOnDisconnect = each.value.s.minutes_to_wait_on_disconnect
      rampDownActionOnLogoff            = each.value.s.action_on_logoff
      rampDownMinutesToWaitOnLogoff     = each.value.s.minutes_to_wait_on_logoff

      offPeakStartTime                 = { hour = tonumber(split(":", each.value.s.off_peak_start_time)[0]), minute = tonumber(split(":", each.value.s.off_peak_start_time)[1]) }
      offPeakStartVMOnConnect          = "Enable"
      offPeakActionOnDisconnect        = each.value.s.action_on_disconnect
      offPeakMinutesToWaitOnDisconnect = each.value.s.minutes_to_wait_on_disconnect
      offPeakActionOnLogoff            = each.value.s.action_on_logoff
      offPeakMinutesToWaitOnLogoff     = each.value.s.minutes_to_wait_on_logoff
    }
  }
}

data "azurerm_client_config" "current" {}

# --- Comprobaciones cruzadas con var.host_pools -------------------------------

resource "terraform_data" "scaling_plan_host_pool_check" {
  for_each = merge(
    { for k, v in var.pooled_scaling_plans : k => { type = "Pooled", location = v.location, host_pools = v.host_pools } },
    { for k, v in var.personal_scaling_plans : k => { type = "Personal", location = v.location, host_pools = v.host_pools } },
  )

  input = each.value.host_pools

  lifecycle {
    precondition {
      condition     = alltrue([for hp in each.value.host_pools : var.host_pools[hp].type == each.value.type])
      error_message = "El scaling plan solo admite host pools de su mismo tipo (Pooled o Personal)."
    }
    precondition {
      condition     = alltrue([for hp in each.value.host_pools : var.host_pools[hp].location == each.value.location])
      error_message = "El scaling plan tiene que estar en la misma región que sus host pools."
    }
    precondition {
      condition     = each.value.type == "Personal" || alltrue([for hp in each.value.host_pools : var.host_pools[hp].maximum_sessions_allowed != null])
      error_message = "Autoscale en pooled exige un maximum_sessions_allowed definido en el host pool."
    }
    precondition {
      # Un host pool solo puede tener un scaling plan, también entre pooled y personal
      condition = length(concat(flatten([for k, v in var.pooled_scaling_plans : v.host_pools]), flatten([for k, v in var.personal_scaling_plans : v.host_pools]))) == length(distinct(concat(flatten([for k, v in var.pooled_scaling_plans : v.host_pools]), flatten([for k, v in var.personal_scaling_plans : v.host_pools]))))
      error_message = "Un host pool solo puede asignarse a un scaling plan."
    }
  }
}

# --- Permisos y diagnósticos -------------------------------------------------

resource "azurerm_role_assignment" "avd_power_on_off" {
  for_each             = var.avd_power_on_off_assignments
  scope                = "/subscriptions/${each.value.subscription_id}"
  role_definition_name = "Desktop Virtualization Power On Off Contributor"
  principal_id         = each.value.principal_id
}

resource "azurerm_monitor_diagnostic_setting" "scaling_plan" {
  for_each = merge(
    { for k, v in var.pooled_scaling_plans : k => { id = module.scaling_plan_pooled[k].id, law = v.log_analytics_workspace_id } },
    { for k, v in var.personal_scaling_plans : k => { id = azapi_resource.scaling_plan_personal[k].id, law = v.log_analytics_workspace_id } },
  )

  name                       = "diag-${each.key}"
  target_resource_id         = each.value.id
  log_analytics_workspace_id = each.value.law

  enabled_log {
    category = "Autoscale"
  }
}

output "scaling_plan_ids" {
  description = "IDs de los scaling plans."
  value = merge(
    { for k, m in module.scaling_plan_pooled : k => m.id },
    { for k, r in azapi_resource.scaling_plan_personal : k => r.id },
  )
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

pooled_scaling_plans = {
  "vdscaling-<workload>-pro-pooled" = {
    resource_group_name = "<rg-avd-pro>"
    location            = "<region>"
    time_zone           = "Romance Standard Time"
    friendly_name       = "Autoscale escritorios pooled"
    host_pools          = ["vdpool-<workload>-pro-01"]

    schedules = {
      laborables = {
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

        ramp_up_start_time                 = "07:00"
        ramp_up_minimum_hosts_percent      = 25
        ramp_up_capacity_threshold_percent = 60

        peak_start_time = "09:00"

        ramp_down_start_time                 = "18:00"
        ramp_down_minimum_hosts_percent      = 0
        ramp_down_capacity_threshold_percent = 90
        ramp_down_force_logoff_users         = false
        ramp_down_stop_hosts_when            = "ZeroActiveSessions"

        off_peak_start_time = "21:00"
      }
      fin-de-semana = {
        days_of_week = ["Saturday", "Sunday"]

        ramp_up_start_time                 = "09:00"
        ramp_up_minimum_hosts_percent      = 0
        ramp_up_capacity_threshold_percent = 90

        peak_start_time = "10:00"

        ramp_down_start_time                 = "14:00"
        ramp_down_minimum_hosts_percent      = 0
        ramp_down_capacity_threshold_percent = 90

        off_peak_start_time = "16:00"
      }
    }

    log_analytics_workspace_id = "<resourceId log-analytics-workspace>"
  }
}

personal_scaling_plans = {
  "vdscaling-<workload>-pro-personal" = {
    resource_group_name = "<rg-avd-pro>"
    location            = "<region>"
    time_zone           = "Romance Standard Time"
    friendly_name       = "Autoscale puestos personales"
    host_pools          = ["vdpool-<workload>-pro-dev01"]

    schedules = {
      laborables = {
        days_of_week             = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        ramp_up_start_time       = "07:30"
        ramp_up_auto_start_hosts = "None" # los enciende Start VM on Connect
        peak_start_time          = "09:00"
        ramp_down_start_time     = "18:00"
        off_peak_start_time      = "20:00"

        action_on_disconnect          = "Deallocate"
        minutes_to_wait_on_disconnect = 60
        action_on_logoff              = "Deallocate"
        minutes_to_wait_on_logoff     = 15
      }
    }

    log_analytics_workspace_id = "<resourceId log-analytics-workspace>"
  }
}

avd_power_on_off_assignments = {
  suscripcion-avd-pro = {
    principal_id    = "<objectId del service principal Azure Virtual Desktop>"
    subscription_id = "<subscriptionId-avd-pro>"
  }
}
```

En `dev.tfvars` y `pre.tfvars`: ramp-up más tarde, % mínimo a 0 y cierre forzoso en ramp-down, porque son entornos sin usuarios fuera de horario.

Despliegue y comprobación:

```powershell
terraform init
terraform plan -var-file="env/pro.tfvars" -out="pro.tfplan"
terraform apply "pro.tfplan"

# Plan asignado y programaciones
Get-AzWvdScalingPlan -ResourceGroupName "<rg-avd-pro>" -Name "vdscaling-<workload>-pro-pooled" |
    Select-Object Name, HostPoolType, TimeZone, ExclusionTag
Get-AzWvdScalingPlanPooledSchedule -ResourceGroupName "<rg-avd-pro>" -ScalingPlanName "vdscaling-<workload>-pro-pooled"

# Excluir una VM de autoscale durante un mantenimiento
Update-AzTag -ResourceId "<resourceId vm>" -Tag @{ excludeFromScaling = "true" } -Operation Merge
```

### Equivalente en Bicep

`main.bicep` (pooled y personal con sus programaciones):

```bicep
// =============================================================================
// Scaling plans de AVD (gestión de energía): uno pooled y, opcionalmente,
// uno personal, con sus programaciones y diagnósticos
// DEPENDENCY: Resource Group existente (targetScope = resourceGroup)
// DEPENDENCY: Host pools existentes en la misma región (pooled con límite de sesiones definido)
// DEPENDENCY: Rol Power On Off Contributor en la suscripción (power-on-off-role.bicep)
// DEPENDENCY: Log Analytics workspace existente
// =============================================================================
targetScope = 'resourceGroup'

param location string = resourceGroup().location
param timeZone string = 'Romance Standard Time'
param exclusionTag string = 'excludeFromScaling'
param logAnalyticsWorkspaceId string

param pooledPlanName string
@description('IDs de host pools pooled (cada host pool solo admite un scaling plan).')
param pooledHostPoolIds array

param personalPlanName string = ''
@description('IDs de host pools personales. Vacío = no se crea el plan personal.')
param personalHostPoolIds array = []

param tags object = {}

var weekdays = [
  'Monday'
  'Tuesday'
  'Wednesday'
  'Thursday'
  'Friday'
]

resource pooledPlan 'Microsoft.DesktopVirtualization/scalingPlans@2025-10-10' = {
  name: pooledPlanName
  location: location
  tags: tags
  properties: {
    hostPoolType: 'Pooled'
    timeZone: timeZone
    exclusionTag: exclusionTag
    hostPoolReferences: [
      for id in pooledHostPoolIds: {
        hostPoolArmPath: id
        scalingPlanEnabled: true
      }
    ]
  }
}

resource pooledWeekdays 'Microsoft.DesktopVirtualization/scalingPlans/pooledSchedules@2025-10-10' = {
  parent: pooledPlan
  name: 'laborables'
  properties: {
    daysOfWeek: weekdays
    rampUpStartTime: { hour: 7, minute: 0 }
    rampUpLoadBalancingAlgorithm: 'BreadthFirst'
    rampUpMinimumHostsPct: 25
    rampUpCapacityThresholdPct: 60
    peakStartTime: { hour: 9, minute: 0 }
    peakLoadBalancingAlgorithm: 'BreadthFirst'
    rampDownStartTime: { hour: 18, minute: 0 }
    rampDownLoadBalancingAlgorithm: 'DepthFirst'
    rampDownMinimumHostsPct: 0
    rampDownCapacityThresholdPct: 90
    rampDownForceLogoffUsers: false
    rampDownStopHostsWhen: 'ZeroActiveSessions'
    rampDownWaitTimeMinutes: 30
    rampDownNotificationMessage: 'El escritorio se va a apagar. Guarda tu trabajo y cierra la sesión.'
    offPeakStartTime: { hour: 21, minute: 0 }
    offPeakLoadBalancingAlgorithm: 'DepthFirst'
  }
}

resource personalPlan 'Microsoft.DesktopVirtualization/scalingPlans@2025-10-10' = if (!empty(personalHostPoolIds)) {
  name: empty(personalPlanName) ? 'unused' : personalPlanName
  location: location
  tags: tags
  properties: {
    hostPoolType: 'Personal'
    timeZone: timeZone
    exclusionTag: exclusionTag
    hostPoolReferences: [
      for id in personalHostPoolIds: {
        hostPoolArmPath: id
        scalingPlanEnabled: true
      }
    ]
  }
}

resource personalWeekdays 'Microsoft.DesktopVirtualization/scalingPlans/personalSchedules@2025-10-10' = if (!empty(personalHostPoolIds)) {
  parent: personalPlan
  name: 'laborables'
  properties: {
    daysOfWeek: weekdays
    rampUpStartTime: { hour: 7, minute: 30 }
    rampUpAutoStartHosts: 'None' // los enciende Start VM on Connect
    rampUpStartVMOnConnect: 'Enable'
    rampUpActionOnDisconnect: 'Deallocate'
    rampUpMinutesToWaitOnDisconnect: 60
    rampUpActionOnLogoff: 'Deallocate'
    rampUpMinutesToWaitOnLogoff: 15
    peakStartTime: { hour: 9, minute: 0 }
    peakStartVMOnConnect: 'Enable'
    peakActionOnDisconnect: 'Deallocate'
    peakMinutesToWaitOnDisconnect: 60
    peakActionOnLogoff: 'Deallocate'
    peakMinutesToWaitOnLogoff: 15
    rampDownStartTime: { hour: 18, minute: 0 }
    rampDownStartVMOnConnect: 'Enable'
    rampDownActionOnDisconnect: 'Deallocate'
    rampDownMinutesToWaitOnDisconnect: 30
    rampDownActionOnLogoff: 'Deallocate'
    rampDownMinutesToWaitOnLogoff: 5
    offPeakStartTime: { hour: 20, minute: 0 }
    offPeakStartVMOnConnect: 'Enable'
    offPeakActionOnDisconnect: 'Deallocate'
    offPeakMinutesToWaitOnDisconnect: 15
    offPeakActionOnLogoff: 'Deallocate'
    offPeakMinutesToWaitOnLogoff: 5
  }
}

resource pooledDiagnostics 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = {
  name: 'diag-${pooledPlanName}'
  scope: pooledPlan
  properties: {
    workspaceId: logAnalyticsWorkspaceId
    logs: [
      { category: 'Autoscale', enabled: true }
    ]
  }
}

resource personalDiagnostics 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = if (!empty(personalHostPoolIds)) {
  name: 'diag-${personalPlanName}'
  scope: personalPlan
  properties: {
    workspaceId: logAnalyticsWorkspaceId
    logs: [
      { category: 'Autoscale', enabled: true }
    ]
  }
}

output pooledScalingPlanId string = pooledPlan.id
```

`power-on-off-role.bicep` (despliegue a nivel de suscripción):

```bicep
// =============================================================================
// Rol Desktop Virtualization Power On Off Contributor en la suscripción
// (por debajo de la suscripción autoscale no funciona correctamente)
// DEPENDENCY: Permiso Microsoft.Authorization/roleAssignments/write en la suscripción
// =============================================================================
targetScope = 'subscription'

@description('Object ID del service principal de Azure Virtual Desktop (aplicación 9cdead84-a844-4324-93f2-b2e6bb768d07) o de la identidad del host pool.')
param principalId string

// Desktop Virtualization Power On Off Contributor (rol integrado)
var powerOnOffContributorRoleId = '40c5ff49-9181-41f8-ae61-143b0e78555e'

resource powerOnOff 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(subscription().id, principalId, powerOnOffContributorRoleId)
  properties: {
    principalId: principalId
    principalType: 'ServicePrincipal'
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', powerOnOffContributorRoleId)
  }
}
```

`main.pro.bicepparam`:

```bicep
using 'main.bicep'

param timeZone = 'Romance Standard Time'
param logAnalyticsWorkspaceId = '<resourceId log-analytics-workspace>'

param pooledPlanName = 'vdscaling-<workload>-pro-pooled'
param pooledHostPoolIds = [
  '<resourceId vdpool-<workload>-pro-01>'
]

param personalPlanName = 'vdscaling-<workload>-pro-personal'
param personalHostPoolIds = [
  '<resourceId vdpool-<workload>-pro-dev01>'
]

param tags = {
  environment: 'pro'
  workload: '<workload>'
  owner: '<owner>'
  costcenter: '<costcenter>'
}
```

Despliegue:

```powershell
$avdSpId = (Get-AzADServicePrincipal -ApplicationId "9cdead84-a844-4324-93f2-b2e6bb768d07").Id
az deployment sub create --location <region> --template-file power-on-off-role.bicep --parameters principalId=$avdSpId

az deployment group what-if --resource-group <rg-avd-pro> --parameters main.pro.bicepparam
az deployment group create  --resource-group <rg-avd-pro> --parameters main.pro.bicepparam
```

## Errores típicos

| Síntoma | Causa | Solución |
|---|---|---|
| Autoscale no enciende ni apaga nada | Falta *Power On Off Contributor* o está asignado por debajo de la suscripción | Asignarlo en cada suscripción con host pools y session hosts |
| Fuera de horario siguen hosts encendidos sin usuarios conectados | Las sesiones desconectadas cuentan como activas | Política *Set time limit for disconnected sessions* y % mínimo 0 en off-peak |
| El ramp-down apaga más despacio de lo esperado | El cierre forzoso espera el tiempo configurado antes de cerrar sesiones | Reducir la espera si negocio lo acepta y combinar con la política de desconectadas |
| Un host en mantenimiento vuelve a aceptar sesiones | Autoscale sobrescribe el drain mode en pooled | Usar la etiqueta de exclusión antes de poner drain mode |
| Hay hosts excluidos y aun así no se cumple el % mínimo | Los hosts con etiqueta de exclusión cuentan en el cálculo del mínimo | Quitar la etiqueta a hosts suficientes |
| Los usuarios ven "No resources available" | Todos los hosts encendibles están excluidos o apagados y el umbral no se ha superado | Revisar etiquetas y % mínimo de la fase |
| No deja asignar el plan a un host pool | Otro tipo de host pool, otra región o el host pool ya tiene otro plan | Mismo tipo y región, un plan por host pool |
| La programación se dispara una hora antes o después | Zona horaria UTC o equivocada | Zona horaria del negocio (`Romance Standard Time`) |
| El fin de semana se comporta como el off-peak del viernes | No hay programación para esos días | Añadir una programación de fin de semana |
| El host pool ignora su algoritmo de reparto | En pooled manda el algoritmo de cada fase del plan | Configurarlo en el plan |
| Conflictos o arranques inesperados | Convive con la herramienta de escalado de Automation o con un script de terceros | Desactivar el otro mecanismo |
| La hibernación no funciona en el plan personal | Hibernación no habilitada en las VMs, o el host pool usa FSLogix o App Attach | Habilitarla en las VMs o usar desasignar |
| Autoscale dinámico falla con `CustomerVmNoAccessToDeploymentPackageException` | Sin acceso a `wvdhpustgr0prod.blob.core.windows.net` | Permitir ese endpoint |
| `terraform plan` no admite un plan personal con azurerm | El recurso de azurerm solo soporta pooled | Usar azapi (como en la ficha) o Bicep |
