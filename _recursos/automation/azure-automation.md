---
title: "Azure Automation"
indice: automation
resumen: "Runbooks en PowerShell y Python para tareas programadas."
estado: documentado   # proximamente | en-curso | documentado
orden: 1
last_review: 2026-10-20
fuentes:
  - titulo: "Azure Automation runbook types"
    url: https://learn.microsoft.com/azure/automation/automation-runbook-types
  - titulo: "Runbook execution in Azure Automation"
    url: https://learn.microsoft.com/azure/automation/automation-runbook-execution
  - titulo: "Runtime environment in Azure Automation"
    url: https://learn.microsoft.com/azure/automation/runtime-environment-overview
  - titulo: "Manage Runtime environment and associated runbooks"
    url: https://learn.microsoft.com/azure/automation/manage-runtime-environment
  - titulo: "Azure Automation limits and quotas"
    url: https://learn.microsoft.com/azure/automation/automation-subscription-limits-faq
  - titulo: "Hybrid Runbook Worker overview"
    url: https://learn.microsoft.com/azure/automation/automation-hybrid-runbook-worker
  - titulo: "Deploy an extension-based Hybrid Runbook Worker"
    url: https://learn.microsoft.com/azure/automation/extension-based-hybrid-runbook-worker-install
  - titulo: "Use Azure Private Link with Azure Automation"
    url: https://learn.microsoft.com/azure/automation/how-to/private-link-security
  - titulo: "Disable local authentication in Automation"
    url: https://learn.microsoft.com/azure/automation/disable-local-authentication
  - titulo: "Migrate from Run As accounts to managed identities"
    url: https://learn.microsoft.com/azure/automation/migrate-run-as-accounts-managed-identity
  - titulo: "Azure Automation State Configuration overview (retirement)"
    url: https://learn.microsoft.com/azure/automation/automation-dsc-overview
  - titulo: "What's new in Azure Automation (retirements)"
    url: https://learn.microsoft.com/azure/automation/whats-new
  - titulo: "Troubleshoot runbook issues"
    url: https://learn.microsoft.com/azure/automation/troubleshoot/runbooks
  - titulo: "Private DNS zone values"
    url: https://learn.microsoft.com/azure/private-link/private-endpoint-dns
  - titulo: "azurerm_automation_runbook"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/automation_runbook
  - titulo: "azurerm_automation_runtime_environment"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/automation_runtime_environment
  - titulo: "azurerm_automation_job_schedule"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/automation_job_schedule
  - titulo: "Azure Automation pricing"
    url: https://azure.microsoft.com/pricing/details/automation/
  - titulo: "Módulo Terraform Automation/AutomationAccount"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Automation/AutomationAccount
  - titulo: "Módulo Terraform Automation/Runbook"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Automation/Runbook
  - titulo: "Módulo Terraform Automation/HybridWorkerGroup"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Automation/HybridWorkerGroup
---

Azure Automation ejecuta **runbooks** (scripts de PowerShell o Python) bajo demanda, por programación o desde una alerta, contra recursos de Azure o de tu centro de datos. Es la herramienta de operación clásica: apagar y encender VMs, rotar secretos, limpiar recursos huérfanos, generar informes o lanzar remediaciones. Las dos decisiones que más pesan son **dónde se ejecuta el runbook** (sandbox de Azure o Hybrid Runbook Worker) y **en qué runtime** (PowerShell 7.4 o Python 3.10 mediante *runtime environments*).

## Qué es y cuándo usarlo

### Cuándo sí

- Tareas de operación recurrentes sobre recursos de Azure con PowerShell o Python.
- Scripts que deben ejecutarse dentro de tu red o en servidores on-premises (con Hybrid Runbook Worker).
- Remediaciones lanzadas desde alertas de Azure Monitor.
- Equipos de sistemas que ya trabajan en PowerShell y no quieren mantener una aplicación.

### Cuándo no

| Si el caso es… | Mejor opción | Motivo |
|---|---|---|
| Integración entre aplicaciones con conectores y aprobaciones | Logic Apps | Diseñador visual y más de 1.400 conectores |
| Código de aplicación por eventos o una API | Azure Functions | Modelo de eventos, escalado y despliegue de aplicación |
| Parcheo de servidores | Azure Update Manager | Update Management de Automation se retiró en agosto de 2024 |
| Configuración deseada de servidores (DSC) | Azure Machine Configuration | State Configuration se retira el 30 de septiembre de 2027 |
| Apagado y encendido de VMs fuera de horario | Start/Stop VMs v2 | La v1 sobre Automation está deprecada; la v2 corre en Functions |
| Un proceso de más de 3 horas en la nube | Hybrid Runbook Worker | El sandbox detiene los jobs a las 3 horas (*fair share*) |

### SKU y entornos de ejecución

El Automation Account tiene dos SKU: **Free** y **Basic**. Free se queda en 500 minutos de ejecución al mes por suscripción; Basic factura los minutos de *job* y las horas de *watchers* que superen las unidades gratuitas (500 minutos de jobs y 744 horas de watchers al mes).

| Entorno | Dónde corre | Límites | Red privada | Cuándo |
|---|---|---|---|---|
| **Sandbox de Azure** (cloud job) | Infraestructura compartida de Azure | 3 h por job, 400 MB de memoria, 1 GB de disco, 1.000 sockets | ❌ No llega a recursos protegidos por Private Endpoint ni por firewall (Automation no es *trusted service*) | Gestión del plano de control de Azure (ARM) |
| **Hybrid Runbook Worker** (extensión V2) | Tu VM de Azure o servidor con Azure Arc | Sin límite de duración; 50 jobs concurrentes por worker | ✅ Corre en tu red | Recursos privados, on-premises, procesos largos o con mucha memoria |

Runtimes soportados:

| Tipo | Versiones soportadas | Observaciones |
|---|---|---|
| **PowerShell** (recomendado) | 7.6, 7.4 y 5.1 | 7.4 y 7.6 solo a través de *runtime environments*; 7.1 y 7.2 ya no tienen soporte del producto |
| **Python** (recomendado) | 3.10 | Python 2.7 y 3.8 sin soporte; los webhooks no pueden arrancar runbooks de Python |
| PowerShell Workflow | 5.1 | No existe en PowerShell 7; no corre en Hybrid Workers Linux |
| Gráficos | 5.1 | Solo editables en el portal; no se pueden firmar ni convertir a texto |

Límites que conviene tener a mano:

| Límite | Valor |
|---|---|
| Duración de un job en sandbox | 3 horas (se detiene y no se reinicia) |
| Memoria de un sandbox | 400 MB |
| Runbooks por Automation Account | 800 |
| Jobs nuevos cada 30 s por cuenta | 100 |
| Tamaño de un stream de salida | 1 MiB |
| Parámetros por runbook | 50 (512 KB en total) |
| Retención de los datos de jobs | 30 días |
| Tags por Automation Account | 15 |

### Qué escenario recomiendo

| Escenario del cliente | Diseño | Por qué |
|---|---|---|
| Runbooks que solo tocan recursos de Azure por ARM | Sandbox + identidad gestionada, cuenta Basic | Sin infraestructura que mantener |
| Runbooks que acceden a Key Vault, SQL o Storage privados | Hybrid Worker en la VNet + Private Endpoint `DSCAndHybridWorker` | El sandbox no llega a Private Endpoints |
| Automatización de servidores on-premises | Hybrid Worker sobre servidores con Azure Arc | Mismo modelo de gestión que en Azure |
| Procesos largos o con mucha memoria | Hybrid Worker | Sin el corte de 3 horas ni el límite de 400 MB |
| Disparo desde sistemas externos | Webhook con Private Endpoint `Webhook` (requiere autenticación local) o, mejor, inicio del job por ARM con Entra ID | Los webhooks dependen de un token en la URL |

### Datos que conviene llevar a la reunión

- **Las cuentas Run As se retiraron el 30 de septiembre de 2023**: todo se autentica con identidad gestionada. Si el cliente aún tiene runbooks con `Get-AutomationConnection`, hay que migrarlos.
- **El Hybrid Worker basado en agente (MMA) se retiró el 31 de agosto de 2024** y desde el 1 de abril de 2025 sus jobs se detienen. Solo vale el basado en extensión.
- **Update Management y Change Tracking con Log Analytics se retiraron el 31 de agosto de 2024** (sustitutos: Azure Update Manager y Change Tracking con AMA).
- **State Configuration (DSC) se retira el 30 de septiembre de 2027** (sustituto: Azure Machine Configuration).
- **Los runbooks con módulos AzureRM dejaron de ejecutarse desde el 1 de febrero de 2025**: solo módulos Az.
- **Desactivar la autenticación local rompe los webhooks**: se decide antes de diseñar cómo se disparan los runbooks.

## Decisiones de diseño

| Decisión | Lo que aplico | Por qué |
|---|---|---|
| Identidad | Identidad gestionada *system-assigned* en la cuenta; *user-assigned* si varias cuentas comparten permisos | Sustituye a Run As; sin certificados que renovar |
| Permisos | Roles mínimos por *scope* concreto (p. ej. *Virtual Machine Contributor* en un RG), nunca *Contributor* de suscripción | Mínimo privilegio; los runbooks suelen tener mucho alcance |
| Runtime | PowerShell 7.4 (o Python 3.10) con *runtime environment* | Versiones con soporte y paquetes fijados por entorno |
| Paquetes | Módulos fijados en el runtime environment (Az, Azure CLI y los propios) | Evita conflictos de versiones entre runbooks |
| Dónde se ejecuta | Sandbox para gestión ARM; Hybrid Worker para todo lo que toque redes privadas | El sandbox no ve Private Endpoints |
| Hybrid Worker | Extensión V2 con identidad *system-assigned* en la VM, mínimo 2 workers por grupo | Alta disponibilidad del grupo y sin agente MMA |
| Red | `public_network_access = false` + Private Endpoints `DSCAndHybridWorker` (y `Webhook` si aplica) en `privatelink.azure-automation.net` | Tráfico de workers y webhooks por la red privada |
| Autenticación local | Desactivada salvo que haya webhooks | Solo Entra ID |
| Secretos | Key Vault desde el runbook con la identidad gestionada; variables cifradas solo para valores que no son secretos | Rotación centralizada y auditoría |
| Código | Scripts en Git, desplegados por IaC o pipeline; nada editado en el portal | Trazabilidad y revisión de cambios |
| Programaciones | Zona horaria explícita (`Europe/Madrid`) y parámetros en minúsculas | Evita sorpresas con el horario de verano y un fallo conocido de Automation |
| Observabilidad | *Diagnostic settings* `JobLogs`, `JobStreams` y `AuditEvent` a Log Analytics y alertas sobre jobs fallidos | La retención de jobs en la cuenta es de solo 30 días |
| Resiliencia | Runbooks idempotentes, con reintentos y estado fuera del job (Blob, tabla o base de datos) | Los jobs pueden interrumpirse y no guardan estado entre ejecuciones |

Alineación con el Well-Architected Framework:

- **Seguridad**: identidad gestionada con mínimo privilegio, red privada, sin autenticación local y secretos en Key Vault.
- **Fiabilidad**: runbooks idempotentes, Hybrid Workers redundantes y alertas sobre jobs fallidos.
- **Coste**: sandbox mientras se pueda; vigilar los minutos de job, que se facturan a partir de los 500 gratuitos.
- **Excelencia operativa**: código en Git, runtime environments versionados y logs en Log Analytics.
- **Rendimiento**: dividir trabajos grandes en runbooks hijo y llevar a Hybrid Worker lo que supere los límites del sandbox.

## Módulo de Terraform

### Los módulos del repositorio

| Pieza | Módulo | Estado |
|---|---|---|
| Automation Account | [`Automation/AutomationAccount`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Automation/AutomationAccount) | Utilizable |
| Runbook | [`Automation/Runbook`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Automation/Runbook) | Utilizable solo para runtimes antiguos |
| Programación | [`Automation/AutomationSchedule`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Automation/AutomationSchedule) | Utilizable |
| Hybrid Worker | [`Automation/HybridWorkerGroup`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Automation/HybridWorkerGroup) | Utilizable con condiciones |

`AutomationAccount` cubre identidad, CMK, Private Endpoints y *diagnostic settings*. A tener en cuenta:

- Por defecto deja `local_authentication_enabled` y `public_network_access_enabled` en `true`: hay que pasarlos explícitamente.
- Usa el bloque `metric` en los *diagnostic settings*, eliminado en azurerm 5.0 en favor de `enabled_metric`.
- Entre las categorías por defecto incluye `DscNodeStatus`, que pierde sentido con State Configuration en retirada.

`Runbook` no expone `runtime_environment_name` y su validación no admite el tipo `Python`, así que no permite PowerShell 7.4 ni Python 3.10. Además, `log_activity_trace_level` valida de 0 a 99, cuando el provider solo acepta 0, 9 o 15 (y solo en runbooks gráficos). En la ficha despliego los runbooks con recursos nativos.

`HybridWorkerGroup` usa la clave del mapa como `worker_id`, que tiene que ser un UUID, y no instala la extensión del Hybrid Worker en la VM. Sin la extensión, el worker queda registrado pero no ejecuta nada.

### Estructura en el proyecto

```txt
/
├── providers.tf
├── automation.tf   # cuenta con el módulo
├── runbooks.tf     # runtime environments, runbooks y programaciones
├── hybrid.tf       # Hybrid Workers basados en extensión
├── runbooks/
│   └── Stop-VmsFueraDeHorario.ps1
└── env/
    ├── dev.tfvars
    ├── pre.tfvars
    └── pro.tfvars
```

### `providers.tf`

```hcl
terraform {
  required_version = ">= 1.6.0"
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      # 4.59.0: runtime_environment_name en azurerm_automation_runbook (PowerShell 7.4 / Python 3.10).
      # < 5.0.0: restricción de los módulos de AzureTerraformModules.
      version = ">= 4.59.0, < 5.0.0"
    }
    random = {
      source  = "hashicorp/random"
      version = ">= 3.6.0"
    }
  }
}

provider "azurerm" {
  features {}
}

variable "tags" {
  description = "Tags corporativos comunes a todos los recursos."
  type        = map(string)
}
```

### Cuenta con el módulo · `automation.tf`

```hcl
# =============================================================================
# Automation Account con el módulo Automation/AutomationAccount
# DEPENDENCY: Resource Group y Log Analytics workspace existentes
# DEPENDENCY: Subnet de Private Endpoints y zona privatelink.azure-automation.net
# =============================================================================

variable "automation_account" {
  description = "Automation Account del entorno."
  type = object({
    name                          = string
    resource_group_name           = string
    location                      = string
    public_network_access_enabled = optional(bool, false)
    local_authentication_enabled  = optional(bool, false) # true solo si se usan webhooks
    private_endpoint_subnet_id    = string
    private_dns_zone_id           = string
    log_analytics_workspace_id    = string
    tags                          = optional(map(string), {})
  })
}

variable "automation_role_assignments" {
  description = "Permisos de la identidad del Automation Account: una entrada por asignación."
  type = map(object({
    scope                = string
    role_definition_name = string
  }))
  default = {}
}

module "automation_account" {
  source = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Automation/AutomationAccount?ref=main"

  name                = var.automation_account.name
  resource_group_name = var.automation_account.resource_group_name
  location            = var.automation_account.location
  sku_name            = "Basic"

  public_network_access_enabled = var.automation_account.public_network_access_enabled
  local_authentication_enabled  = var.automation_account.local_authentication_enabled

  identity = {
    type = "SystemAssigned"
  }

  # Un Private Endpoint por subrecurso
  private_endpoints = [
    {
      name                 = "pe-${var.automation_account.name}-hrw"
      subnet_id            = var.automation_account.private_endpoint_subnet_id
      subresource_names    = ["DSCAndHybridWorker"]
      private_dns_zone_ids = [var.automation_account.private_dns_zone_id]
    },
    {
      name                 = "pe-${var.automation_account.name}-webhook"
      subnet_id            = var.automation_account.private_endpoint_subnet_id
      subresource_names    = ["Webhook"]
      private_dns_zone_ids = [var.automation_account.private_dns_zone_id]
    }
  ]

  diagnostic_settings = {
    name                       = "diag-${var.automation_account.name}"
    log_analytics_workspace_id = var.automation_account.log_analytics_workspace_id
    enabled_log_categories     = ["JobLogs", "JobStreams", "AuditEvent"]
  }

  tags = merge(var.tags, var.automation_account.tags)
}

resource "azurerm_role_assignment" "automation" {
  for_each             = var.automation_role_assignments
  scope                = each.value.scope
  role_definition_name = each.value.role_definition_name
  principal_id         = module.automation_account.principal_id
}
```

### Runbooks y programaciones · `runbooks.tf`

```hcl
# =============================================================================
# Runtime environments, runbooks y programaciones (recursos nativos)
# El módulo Automation/Runbook no admite runtime environments (PowerShell 7.4 / Python 3.10).
# DEPENDENCY: Automation Account (automation.tf)
# DEPENDENCY: Ficheros de script en ./runbooks del repositorio
# =============================================================================

variable "runtime_environments" {
  description = "Runtime environments: lenguaje, versión y paquetes por defecto (solo PowerShell)."
  type = map(object({
    language         = string # PowerShell | Python
    version          = string # 7.4 | 5.1 | 3.10
    default_packages = optional(map(string), {})
    description      = optional(string)
  }))
  default = {}

  validation {
    condition     = alltrue([for k, v in var.runtime_environments : contains(["PowerShell", "Python"], v.language)])
    error_message = "language debe ser PowerShell o Python."
  }
}

variable "runbooks" {
  description = "Runbooks: script del repositorio, runtime environment y programaciones."
  type = map(object({
    runbook_type        = string # PowerShell | Python
    runtime_environment = string # clave de var.runtime_environments
    script_path         = string # relativo a ./runbooks
    description         = optional(string)
    log_verbose         = optional(bool, false)
    log_progress        = optional(bool, false)
    schedules = optional(map(object({
      frequency   = string # OneTime | Hour | Day | Week | Month
      interval    = optional(number, 1)
      start_time  = string # RFC3339, en el futuro
      timezone    = optional(string, "Etc/UTC")
      week_days   = optional(list(string))
      run_on      = optional(string)          # nombre del Hybrid Worker Group; vacío = sandbox de Azure
      parameters  = optional(map(string), {}) # claves en minúsculas
    })), {})
  }))
  default = {}

  validation {
    condition     = alltrue([for k, v in var.runbooks : contains(["PowerShell", "Python"], v.runbook_type)])
    error_message = "runbook_type debe ser PowerShell o Python (tipos que admiten runtime environment)."
  }

  validation {
    condition = alltrue(flatten([
      for k, v in var.runbooks : [for sk, s in v.schedules : [for pk in keys(s.parameters) : pk == lower(pk)]]
    ]))
    error_message = "Las claves de parameters de una programación deben ir en minúsculas (limitación de Azure Automation)."
  }
}

resource "azurerm_automation_runtime_environment" "this" {
  for_each                 = var.runtime_environments
  name                     = each.key
  location                 = var.automation_account.location
  automation_account_id    = module.automation_account.id
  runtime_language         = each.value.language
  runtime_version          = each.value.version
  runtime_default_packages = each.value.language == "PowerShell" ? each.value.default_packages : null
  description              = each.value.description
  tags                     = merge(var.tags, var.automation_account.tags)
}

resource "azurerm_automation_runbook" "this" {
  for_each                 = var.runbooks
  name                     = each.key
  location                 = var.automation_account.location
  resource_group_name      = var.automation_account.resource_group_name
  automation_account_name  = module.automation_account.name
  runbook_type             = each.value.runbook_type
  runtime_environment_name = azurerm_automation_runtime_environment.this[each.value.runtime_environment].name
  description              = each.value.description
  log_verbose              = each.value.log_verbose
  log_progress             = each.value.log_progress
  content                  = file("${path.root}/runbooks/${each.value.script_path}")
  tags                     = merge(var.tags, var.automation_account.tags)
}

resource "azurerm_automation_schedule" "this" {
  for_each = merge([
    for rk, rv in var.runbooks : { for sk, sv in rv.schedules : "${rk}-${sk}" => sv }
  ]...)

  name                    = each.key
  resource_group_name     = var.automation_account.resource_group_name
  automation_account_name = module.automation_account.name
  frequency               = each.value.frequency
  interval                = each.value.frequency == "OneTime" ? null : each.value.interval
  start_time              = each.value.start_time
  timezone                = each.value.timezone
  week_days               = each.value.frequency == "Week" ? each.value.week_days : null

  lifecycle {
    ignore_changes = [start_time] # evita drift cuando la fecha de inicio ya ha pasado
  }
}

resource "azurerm_automation_job_schedule" "this" {
  for_each = merge([
    for rk, rv in var.runbooks : { for sk, sv in rv.schedules : "${rk}-${sk}" => merge(sv, { runbook = rk }) }
  ]...)

  resource_group_name     = var.automation_account.resource_group_name
  automation_account_name = module.automation_account.name
  runbook_name            = azurerm_automation_runbook.this[each.value.runbook].name
  schedule_name           = azurerm_automation_schedule.this[each.key].name
  parameters              = each.value.parameters
  run_on                  = each.value.run_on
}
```

### Hybrid Runbook Workers · `hybrid.tf`

```hcl
# =============================================================================
# Hybrid Runbook Workers basados en extensión (V2)
# DEPENDENCY: VMs Azure existentes con identidad system-assigned habilitada
# DEPENDENCY: Conectividad de las VMs con el Private Endpoint DSCAndHybridWorker (misma VNet o enlazada) y su DNS
# Para servidores Arc se usa azurerm_arc_machine_extension con el mismo publisher y settings.
# =============================================================================

variable "hybrid_worker_groups" {
  description = "Grupos de Hybrid Workers con sus VMs (clave = nombre del grupo)."
  type = map(object({
    os_type = string # Windows | Linux
    vm_ids  = map(string) # clave lógica => resource ID de la VM
  }))
  default = {}

  validation {
    condition     = alltrue([for k, v in var.hybrid_worker_groups : contains(["Windows", "Linux"], v.os_type)])
    error_message = "os_type debe ser Windows o Linux."
  }
}

resource "azurerm_automation_hybrid_runbook_worker_group" "this" {
  for_each                = var.hybrid_worker_groups
  name                    = each.key
  resource_group_name     = var.automation_account.resource_group_name
  automation_account_name = module.automation_account.name
}

# El worker_id tiene que ser un UUID; se genera una vez por VM y se mantiene estable
resource "random_uuid" "hybrid_worker" {
  for_each = merge([
    for gk, gv in var.hybrid_worker_groups : { for vk, vid in gv.vm_ids : "${gk}-${vk}" => vid }
  ]...)

  keepers = {
    vm_id = each.value
  }
}

resource "azurerm_automation_hybrid_runbook_worker" "this" {
  for_each = merge([
    for gk, gv in var.hybrid_worker_groups : { for vk, vid in gv.vm_ids : "${gk}-${vk}" => { group = gk, vm_id = vid } }
  ]...)

  resource_group_name     = var.automation_account.resource_group_name
  automation_account_name = module.automation_account.name
  worker_group_name       = azurerm_automation_hybrid_runbook_worker_group.this[each.value.group].name
  worker_id               = random_uuid.hybrid_worker[each.key].result
  vm_resource_id          = each.value.vm_id
}

resource "azurerm_virtual_machine_extension" "hybrid_worker" {
  for_each = merge([
    for gk, gv in var.hybrid_worker_groups : { for vk, vid in gv.vm_ids : "${gk}-${vk}" => { os = gv.os_type, vm_id = vid } }
  ]...)

  name                       = "HybridWorkerExtension"
  virtual_machine_id         = each.value.vm_id
  publisher                  = "Microsoft.Azure.Automation.HybridWorker"
  type                       = each.value.os == "Windows" ? "HybridWorkerForWindows" : "HybridWorkerForLinux"
  type_handler_version       = "1.1"
  auto_upgrade_minor_version = true
  automatic_upgrade_enabled  = true

  settings = jsonencode({
    AutomationAccountURL = module.automation_account.hybrid_service_url
  })

  depends_on = [azurerm_automation_hybrid_runbook_worker.this]
}
```

### Variables por entorno · `env/pro.tfvars`

```hcl
tags = {
  environment = "pro"
  workload    = "<workload>"
  owner       = "<owner>"
  costCenter  = "<cost-center>"
}

automation_account = {
  name                       = "aa-<workload>-pro-<region>-001"
  resource_group_name        = "<rg-workload-pro>"
  location                   = "<region>"
  private_endpoint_subnet_id = "<resourceId snet-private-endpoints>"
  private_dns_zone_id        = "<resourceId privatelink.azure-automation.net>"
  log_analytics_workspace_id = "<resourceId log-analytics-workspace>"
}

automation_role_assignments = {
  vms-operacion = {
    scope                = "<resourceId rg-vms-pro>"
    role_definition_name = "Virtual Machine Contributor"
  }
}

runtime_environments = {
  "powershell-7-4" = {
    language = "PowerShell"
    version  = "7.4"
    default_packages = {
      "az"        = "12.3.0"
      "azure cli" = "2.64.0"
    }
  }
}

runbooks = {
  "Stop-VmsFueraDeHorario" = {
    runbook_type        = "PowerShell"
    runtime_environment = "powershell-7-4"
    script_path         = "Stop-VmsFueraDeHorario.ps1"
    schedules = {
      laborables-21h = {
        frequency  = "Week"
        start_time = "<yyyy-MM-ddT21:00:00+02:00>"
        timezone   = "Europe/Madrid"
        week_days  = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        parameters = { resourcegroupname = "<rg-vms-pro>" }
      }
    }
  }
}

hybrid_worker_groups = {
  "hwg-<workload>-pro" = {
    os_type = "Windows"
    vm_ids = {
      vm01 = "<resourceId vm-hrw-01>"
      vm02 = "<resourceId vm-hrw-02>"
    }
  }
}
```

En `dev.tfvars` y `pre.tfvars`, mismo esquema con un único worker y los permisos acotados a los RG de cada entorno.

Despliegue:

```powershell
terraform init
terraform plan -var-file="env/pro.tfvars" -out="pro.tfplan"
terraform apply "pro.tfplan"
```

### Equivalente en Bicep

`main.bicep` (en ARM el contenido del runbook se publica desde una URL, no en línea):

```bicep
// =============================================================================
// Azure Automation: cuenta privada, runtime environment, runbook programado
// y Hybrid Runbook Workers basados en extensión
// DEPENDENCY: Resource Group existente (targetScope = resourceGroup)
// DEPENDENCY: Subnet de Private Endpoints y zona privatelink.azure-automation.net
// DEPENDENCY: Log Analytics workspace existente
// DEPENDENCY: Script del runbook publicado en una URL accesible para Azure (p. ej. blob con SAS o commit fijado)
// DEPENDENCY: VMs Windows del Hybrid Worker en este mismo Resource Group, con identidad system-assigned habilitada
// =============================================================================
targetScope = 'resourceGroup'

param location string = resourceGroup().location

param automationAccountName string

@description('false salvo que haga falta acceso público (p. ej. cloud jobs disparados por alertas de Azure Monitor).')
param publicNetworkAccess bool = false

@description('true solo si se usan webhooks (requieren autenticación local).')
param localAuthEnabled bool = false

param privateEndpointSubnetId string
param privateDnsZoneId string
param logAnalyticsWorkspaceId string

@allowed(['PowerShell', 'Python'])
param runtimeLanguage string = 'PowerShell'

@description('7.4 o 5.1 para PowerShell; 3.10 para Python.')
param runtimeVersion string = '7.4'

@description('Paquetes por defecto del runtime (solo PowerShell).')
param defaultPackages object = {
  az: '12.3.0'
  'azure cli': '2.64.0'
}

param runbookName string

@description('URL del script del runbook (versión fijada).')
param runbookContentUri string

@description('Inicio de la programación diaria, RFC3339 y al menos 5 minutos en el futuro.')
param scheduleStartTime string

param scheduleTimeZone string = 'Europe/Madrid'

@description('Nombre del Hybrid Worker Group donde ejecutar el runbook. Vacío = sandbox de Azure.')
param hybridWorkerGroupName string = ''

@description('VMs Windows que forman el Hybrid Worker Group.')
param hybridWorkerVmIds array = []

param tags object = {}

resource automationAccount 'Microsoft.Automation/automationAccounts@2024-10-23' = {
  name: automationAccountName
  location: location
  tags: tags
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    sku: {
      name: 'Basic'
    }
    publicNetworkAccess: publicNetworkAccess
    disableLocalAuth: !localAuthEnabled
  }
}

resource privateEndpoint 'Microsoft.Network/privateEndpoints@2024-05-01' = {
  name: 'pe-${automationAccountName}-hrw'
  location: location
  tags: tags
  properties: {
    subnet: {
      id: privateEndpointSubnetId
    }
    privateLinkServiceConnections: [
      {
        name: 'psc-${automationAccountName}-hrw'
        properties: {
          privateLinkServiceId: automationAccount.id
          groupIds: [
            'DSCAndHybridWorker'
          ]
        }
      }
    ]
  }
}

resource privateDnsZoneGroup 'Microsoft.Network/privateEndpoints/privateDnsZoneGroups@2024-05-01' = {
  parent: privateEndpoint
  name: 'default'
  properties: {
    privateDnsZoneConfigs: [
      {
        name: 'privatelink-azure-automation-net'
        properties: {
          privateDnsZoneId: privateDnsZoneId
        }
      }
    ]
  }
}

resource diagnostics 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = {
  name: 'diag-${automationAccountName}'
  scope: automationAccount
  properties: {
    workspaceId: logAnalyticsWorkspaceId
    logs: [
      { category: 'JobLogs', enabled: true }
      { category: 'JobStreams', enabled: true }
      { category: 'AuditEvent', enabled: true }
    ]
    metrics: [
      { category: 'AllMetrics', enabled: true }
    ]
  }
}

resource runtimeEnvironment 'Microsoft.Automation/automationAccounts/runtimeEnvironments@2024-10-23' = {
  parent: automationAccount
  name: '${toLower(runtimeLanguage)}-${replace(runtimeVersion, '.', '-')}'
  location: location
  tags: tags
  properties: {
    runtime: {
      language: runtimeLanguage
      version: runtimeVersion
    }
    defaultPackages: runtimeLanguage == 'PowerShell' ? defaultPackages : {}
  }
}

resource runbook 'Microsoft.Automation/automationAccounts/runbooks@2024-10-23' = {
  parent: automationAccount
  name: runbookName
  location: location
  tags: tags
  properties: {
    runbookType: runtimeLanguage
    runtimeEnvironment: runtimeEnvironment.name
    logVerbose: false
    logProgress: false
    publishContentLink: {
      uri: runbookContentUri
    }
  }
}

resource schedule 'Microsoft.Automation/automationAccounts/schedules@2024-10-23' = {
  parent: automationAccount
  name: '${runbookName}-diario'
  properties: {
    frequency: 'Day'
    interval: 1
    startTime: scheduleStartTime
    timeZone: scheduleTimeZone
  }
}

resource hybridWorkerGroup 'Microsoft.Automation/automationAccounts/hybridRunbookWorkerGroups@2024-10-23' = if (!empty(hybridWorkerGroupName)) {
  parent: automationAccount
  name: empty(hybridWorkerGroupName) ? 'unused' : hybridWorkerGroupName
}

// El nombre del worker tiene que ser un GUID: se deriva de forma estable de la VM
resource hybridWorkers 'Microsoft.Automation/automationAccounts/hybridRunbookWorkerGroups/hybridRunbookWorkers@2024-10-23' = [
  for vmId in hybridWorkerVmIds: if (!empty(hybridWorkerGroupName)) {
    parent: hybridWorkerGroup
    name: guid(automationAccount.id, vmId)
    properties: {
      vmResourceId: vmId
    }
  }
]

resource hybridWorkerVms 'Microsoft.Compute/virtualMachines@2024-07-01' existing = [
  for vmId in hybridWorkerVmIds: {
    name: last(split(vmId, '/'))
  }
]

resource hybridWorkerExtensions 'Microsoft.Compute/virtualMachines/extensions@2024-07-01' = [
  for (vmId, i) in hybridWorkerVmIds: if (!empty(hybridWorkerGroupName)) {
    parent: hybridWorkerVms[i]
    name: 'HybridWorkerExtension'
    location: location
    properties: {
      publisher: 'Microsoft.Azure.Automation.HybridWorker'
      type: 'HybridWorkerForWindows'
      typeHandlerVersion: '1.1'
      autoUpgradeMinorVersion: true
      enableAutomaticUpgrade: true
      settings: {
        AutomationAccountURL: automationAccount.properties.automationHybridServiceUrl
      }
    }
    dependsOn: [
      hybridWorkers
    ]
  }
]

resource jobSchedule 'Microsoft.Automation/automationAccounts/jobSchedules@2024-10-23' = {
  parent: automationAccount
  name: guid(automationAccount.id, runbook.name, schedule.name)
  properties: {
    runbook: {
      name: runbook.name
    }
    schedule: {
      name: schedule.name
    }
    runOn: empty(hybridWorkerGroupName) ? null : hybridWorkerGroupName
  }
  dependsOn: [
    hybridWorkerGroup
  ]
}

output automationAccountId string = automationAccount.id
output principalId string = automationAccount.identity.principalId
output hybridServiceUrl string = automationAccount.properties.automationHybridServiceUrl
```

`main.pro.bicepparam`:

```bicep
using './main.bicep'

param automationAccountName = 'aa-<workload>-pro-<region>-001'
param publicNetworkAccess = false
param localAuthEnabled = false
param privateEndpointSubnetId = '<resourceId snet-private-endpoints>'
param privateDnsZoneId = '<resourceId privatelink.azure-automation.net>'
param logAnalyticsWorkspaceId = '<resourceId log-analytics-workspace>'
param runtimeLanguage = 'PowerShell'
param runtimeVersion = '7.4'
param runbookName = 'Stop-VmsFueraDeHorario'
param runbookContentUri = '<URL fijada del script .ps1>'
param scheduleStartTime = '<yyyy-MM-ddT21:00:00+02:00>'
param scheduleTimeZone = 'Europe/Madrid'
param hybridWorkerGroupName = 'hwg-<workload>-pro'
param hybridWorkerVmIds = [
  '<resourceId vm-hrw-01>'
  '<resourceId vm-hrw-02>'
]
param tags = {
  environment: 'pro'
  workload: '<workload>'
  owner: '<owner>'
  costCenter: '<cost-center>'
}
```

Despliegue:

```powershell
az deployment group what-if --resource-group <rg-workload-pro> --parameters main.pro.bicepparam
az deployment group create  --resource-group <rg-workload-pro> --parameters main.pro.bicepparam
```

## Errores típicos

| Síntoma | Causa | Solución |
|---|---|---|
| El job pasa a *Stopped* a las 3 horas (*"The job was evicted…"*) | *Fair share* del sandbox | Hybrid Worker o dividir en runbooks hijo |
| *"The job was tried three times but it failed"* | Más de 400 MB de memoria, más de 1.000 sockets o módulos incompatibles | Reducir datos en memoria, partir el trabajo o usar Hybrid Worker |
| El runbook no llega a Key Vault, SQL o Storage con firewall o Private Endpoint | El sandbox no está en la red y Automation no es *trusted service* | Ejecutarlo en un Hybrid Worker dentro de la VNet |
| *"The quota for the monthly total job run time has been reached"* | Cuenta en SKU Free (500 minutos) | Pasar la cuenta a Basic |
| Un webhook deja de funcionar | Autenticación local desactivada | Iniciar el job por ARM con Entra ID o reactivar la autenticación local |
| Las alertas de Azure Monitor no disparan el webhook | Con el acceso público desactivado, las alertas no pueden usar el webhook | Mantener el acceso público para ese caso o iniciar el job por ARM desde otro servicio |
| La programación no pasa bien un parámetro al runbook | Automation normaliza los nombres de parámetro a minúsculas | Usar siempre claves en minúsculas en `parameters` |
| La extensión del Hybrid Worker falla con *"Authentication failed for private links"* | La VM no tiene conectividad con el Private Endpoint de la cuenta | Misma VNet o enlazada y resolución por `privatelink.azure-automation.net` |
| La extensión falla porque no encuentra la identidad | La VM no tiene identidad *system-assigned* | Activarla antes de instalar la extensión |
| `worker_id` inválido al registrar el worker | El ID tiene que ser un UUID | Generarlo con `random_uuid` o `guid()` |
| El runbook en 7.4 no encuentra un módulo | El módulo está importado en otro runtime | Añadir el paquete al runtime environment del runbook |
| Un runbook en 7.x falla con `.\hijo.ps1` | La ejecución de scripts hijo por ruta no está soportada | `Start-AutomationRunbook` o `Start-AzAutomationRunbook` |
| Fallan runbooks que usan rutas como `C:\modules` | Dependencia de rutas internas del servicio | Localizar módulos con `Get-ChildItem` |
| `terraform plan` muestra cambios continuos en `start_time` | La fecha de inicio ya ha pasado | `ignore_changes = [start_time]` |
| Fallan runbooks heredados con `Get-AutomationConnection` | Dependen de Run As, retirado | Migrar a identidad gestionada (`Connect-AzAccount -Identity`) |
