---
title: "Logic Apps"
indice: automation
resumen: "Flujos de trabajo con conectores, sin apenas código."
estado: documentado   # proximamente | en-curso | documentado
orden: 2
last_review: 2026-10-20
fuentes:
  - titulo: "What is Azure Logic Apps?"
    url: https://learn.microsoft.com/azure/logic-apps/logic-apps-overview
  - titulo: "Standard (single-tenant) vs Consumption (multitenant)"
    url: https://learn.microsoft.com/azure/logic-apps/single-tenant-overview-compare
  - titulo: "Usage metering, billing, and pricing"
    url: https://learn.microsoft.com/azure/logic-apps/logic-apps-pricing
  - titulo: "Limits and configuration reference"
    url: https://learn.microsoft.com/azure/logic-apps/logic-apps-limits-and-config
  - titulo: "Secure traffic with private endpoints and VNet integration (Standard)"
    url: https://learn.microsoft.com/azure/logic-apps/secure-single-tenant-workflow-virtual-network-private-endpoint
  - titulo: "Deploy Standard logic apps to storage with private endpoints"
    url: https://learn.microsoft.com/azure/logic-apps/deploy-single-tenant-logic-apps-private-storage-account
  - titulo: "Create Standard workflows in the portal (managed identity for storage)"
    url: https://learn.microsoft.com/azure/logic-apps/create-single-tenant-workflows-azure-portal
  - titulo: "Edit app and host settings (Standard)"
    url: https://learn.microsoft.com/azure/logic-apps/edit-app-settings-host-settings
  - titulo: "Reliability in Azure Logic Apps"
    url: https://learn.microsoft.com/azure/reliability/reliability-logic-apps
  - titulo: "Monitor and collect diagnostic data"
    url: https://learn.microsoft.com/azure/logic-apps/monitor-workflows-collect-diagnostic-data
  - titulo: "Troubleshoot private storage account errors"
    url: https://learn.microsoft.com/troubleshoot/azure/logic-apps/common-error-deploy-logic-apps-private-storage-account
  - titulo: "Azure Service Manager retirement (ISE)"
    url: https://learn.microsoft.com/azure/azure-resource-manager/management/asm-retirement
  - titulo: "Key Vault references (Azure Files considerations)"
    url: https://learn.microsoft.com/azure/app-service/app-service-key-vault-references
  - titulo: "azurerm_logic_app_standard"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/logic_app_standard
  - titulo: "azurerm_logic_app_workflow"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/logic_app_workflow
  - titulo: "Terraform: reserved input variable names"
    url: https://developer.hashicorp.com/terraform/language/block/variable
  - titulo: "Azure Logic Apps pricing"
    url: https://azure.microsoft.com/pricing/details/logic-apps/
  - titulo: "Módulo Terraform Automation/LogicApp"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Automation/LogicApp
  - titulo: "Módulo Terraform Automation/LogicAppStandard"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Automation/LogicAppStandard
---

Logic Apps orquesta procesos de negocio e integraciones con un diseñador visual y más de 1.400 conectores ya hechos: Office 365, SAP, SQL, Service Bus, SFTP, colas, APIs… Cada workflow empieza con un trigger y sigue con acciones. Lo que más condiciona un proyecto es **elegir entre Consumption y Standard**: cambia el modelo de coste, la red privada, dónde residen los datos y cómo se despliega.

## Qué es y cuándo usarlo

### Cuándo sí

- Integraciones entre sistemas con conectores existentes, sin escribir el cliente de cada API.
- Procesos de negocio con aprobaciones, reintentos, esperas largas y condiciones.
- Intercambio B2B (EDI, AS2, X12, EDIFACT) con Integration Account.
- Modernización de BizTalk: Logic Apps Standard es su sucesor según Microsoft.

### Cuándo no

| Si el caso es… | Mejor opción | Motivo |
|---|---|---|
| Lógica compleja escrita en código, con alto rendimiento | Azure Functions (Durable Functions para orquestar) | *Code-first* y más control del runtime |
| Automatización personal o de oficina para usuarios de negocio | Power Automate | Pensado para *citizen developers* y Microsoft 365 |
| Mantenimiento de infraestructura (reiniciar VMs, remediaciones) | Azure Automation Runbooks | Ejecuta PowerShell/Python con Hybrid Worker |
| Una acción que tiene que responder en más de 2 minutos | Patrón asíncrono (202 + *polling*) | El *timeout* de una petición entrante o saliente es fijo |

### Modelos de hosting

| Modelo | SKU | Dónde corre | Workflows por recurso | Red privada (entrada / salida) | Facturación | Residencia del dato |
|---|---|---|---|---|---|---|
| **Consumption** | — (`Microsoft.Logic/workflows`) | Multitenant compartido | 1 | ❌ / ❌ (datos on-prem vía *on-premises data gateway*) | Por ejecución de cada acción y conector + retención | Se replica en la región emparejada |
| **Standard · Workflow Service Plan** | `WS1`, `WS2`, `WS3` | Single-tenant | Varios (stateful y stateless) | ✅ Private Endpoint / ✅ integración con VNet | vCPU y memoria del plan + llamadas a conectores gestionados + transacciones de storage | Se queda en la región |
| **Standard · App Service Environment v3** | Isolated v2 (solo Windows) | Tu ASE, dentro de la VNet | Varios | Hereda la red del ASE | Solo el plan Isolated v2 | Se queda en la región |
| **Standard · Hybrid** | — | Tu Kubernetes con Azure Arc | Varios | Tu red | vCPU por réplica + conectores gestionados + tu infraestructura y licencia de SQL Server | En tu infraestructura |

Tamaños del Workflow Service Plan:

| SKU | vCPU | Memoria |
|---|---|---|
| WS1 | 1 | 3,5 GB |
| WS2 | 2 | 7 GB |
| WS3 | 4 | 14 GB |

Límites que suelen salir en la conversación:

| Límite | Consumption | Standard |
|---|---|---|
| Duración máxima de una ejecución | 90 días (configurable entre 7 y 365) | Stateful 90 días por defecto (configurable). Stateless 5 min por defecto |
| Retención del historial | 90 días | 90 días por defecto (`Workflows.RuntimeConfiguration.RetentionInDays`) |
| *Timeout* de petición saliente o entrante | 120 s | 225 s por defecto |
| Conectores *built-in* | Incluye un número de operaciones gratis y luego se cobra cada acción | **Ilimitados y gratis** |
| Conectores gestionados (Standard/Enterprise) | Por ejecución | Por llamada, mismo precio que en Consumption |

### Qué modelo recomiendo según el escenario

| Escenario del cliente | Modelo | Por qué |
|---|---|---|
| Pocos flujos, poco volumen, sin requisitos de red privada | **Consumption** | Se paga solo lo que se ejecuta y no hay plan que mantener |
| Entorno regulado, acceso a recursos privados o datos que no pueden salir de la región | **Standard (WS)** | Private Endpoint, integración con VNet y residencia del dato en la región |
| Mucho volumen con conectores *built-in* (Service Bus, SQL, Blob, Event Hubs…) | **Standard (WS)** | Los *built-in* no se cobran por ejecución en Standard |
| Aislamiento total de compute y red | **Standard en ASE v3** | Tenant único y red heredada del ASE |
| Procesamiento local o entornos parcialmente desconectados | **Standard Hybrid** | Runtime en tu Kubernetes con Azure Arc |
| B2B/EDI y migración desde BizTalk | **Standard** + Integration Account | Es el destino que Microsoft recomienda para BizTalk |
| Cliente con Integration Service Environment (ISE) | **Migrar a Standard** | ISE se retiró en agosto de 2024 |

### Datos que conviene llevar a la reunión

- **Standard tiene coste fijo**: el plan WS se paga esté o no ejecutándose. Learn pone como ejemplo unos 175 USD/mes para WS1 en una región de muestra; el precio real depende de la región y se calcula en la página de precios.
- **En Standard los conectores *built-in* son gratis**, pero los gestionados (Office 365, SharePoint, SAP…) se siguen cobrando por llamada como en Consumption. Y los workflows *stateful* generan transacciones de storage que se pagan aparte.
- **Para tener SLA a nivel de app en Standard**, el *Maximum Burst* del plan tiene que ser al menos 2.
- **La zona redundante en Standard se decide al crear el plan**: no se puede activar ni desactivar después, exige mínimo 2 instancias y storage ZRS. Consumption ya es zona redundante sin hacer nada.
- **El tipo stateful/stateless se decide al crear el workflow**; cambiarlo después provoca errores en tiempo de ejecución.
- **ISE está retirado** desde agosto de 2024. Hay herramienta para clonar o exportar workflows de Consumption a Standard, pero no migra: replica definiciones y conexiones.

## Decisiones de diseño

| Decisión | Lo que aplico | Por qué |
|---|---|---|
| Modelo | Standard (WS) por defecto en entornos enterprise; Consumption solo para flujos ligeros sin red privada | Red privada, residencia del dato y coste predecible |
| Agrupación | Una Logic App Standard por dominio de negocio, con varios workflows | Comparten compute, configuración y ciclo de despliegue |
| Stateful o stateless | Stateful para procesos largos o que necesitan historial; stateless para baja latencia y mensajes pequeños (< 64 KB) | Stateless no reintenta ejecuciones interrumpidas ni guarda historial |
| Conectores | *Built-in* (service provider) siempre que exista la versión | Corren en el mismo proceso: más rendimiento y sin coste por ejecución |
| Identidad | Identidad gestionada en las conexiones (la *system-assigned* está activa por defecto en Standard) | Sin secretos en las conexiones; los *built-in* admiten sobre todo la *system-assigned* |
| Storage del runtime | Cuenta dedicada por Logic App, ZRS en producción | Guarda estado, historial y la cola de trabajos |
| Autenticación al storage | En WS **no se puede desactivar la clave de la storage** (Azure Files). Uso clave guardada en Key Vault o, para `AzureWebJobsStorage`, identidad *user-assigned* | Limitación documentada del Workflow Service Plan |
| Entrada | `public_network_access = Disabled` + Private Endpoint (`sites`) en `privatelink.azurewebsites.net`, o publicación detrás de APIM/App Gateway | Zero Trust |
| Salida | Integración con VNet + *Route All* + contenido por la VNet (`WEBSITE_CONTENTOVERVNET = 1`) | El runtime necesita llegar a la storage privada |
| Subnet de integración | `/26`, delegada a `Microsoft.Web/serverFarms` | Tamaño recomendado por Microsoft; no se puede cambiar después |
| Storage privado | Private Endpoints de blob, queue, table **y file**, con sus zonas DNS; puertos 443 y 445 abiertos desde la subnet de integración hacia la storage y 20000-30000 entre los nodos del plan | Sin los cuatro el runtime no arranca |
| Conectores gestionados detrás de firewall | Permitir las IPs salientes de los conectores gestionados de la región | Los gestionados corren fuera de tu VNet |
| Escalado | `runtime_scale_monitoring_enabled = true` y *Maximum Burst* ≥ 2 en producción | Triggers detrás de VNet que escalan; SLA de la app |
| Observabilidad | Application Insights + *diagnostic setting* `WorkflowRuntime` a Log Analytics | En Standard la categoría `WorkflowRuntime` tiene coste de exportación: filtrar lo que se envía |
| Despliegue | Infraestructura con IaC; workflows (`workflow.json`, `connections.json`) desde su propio pipeline | Standard separa infraestructura y aplicación |
| Consumption: protección | Restricción por IP en triggers y contenido del historial | No hay red privada en Consumption |

Alineación con el Well-Architected Framework:

- **Seguridad**: identidad gestionada en conexiones, entrada privada, storage privado y secretos en Key Vault.
- **Fiabilidad**: zona redundante desde la creación, storage ZRS e idempotencia (Logic Apps entrega *at least once*).
- **Coste**: Consumption para lo esporádico; Standard cuando el volumen hace rentable el plan fijo.
- **Excelencia operativa**: infraestructura en IaC y workflows en Git con su propio pipeline.
- **Rendimiento**: conectores *built-in*, stateless donde se pueda y repartir carga entre workflows o apps.

## Módulo de Terraform

### Los módulos del repositorio

| Modelo | Módulo | Estado |
|---|---|---|
| Consumption | [`Automation/LogicApp`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Automation/LogicApp) | Utilizable |
| Standard | [`Automation/LogicAppStandard`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Automation/LogicAppStandard) | **No utilizable hoy** |
| B2B | [`Automation/IntegrationAccount`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Automation/IntegrationAccount) | Complementario |

`Automation/LogicApp` (Consumption) crea el recurso, la identidad, el Integration Account vinculado y las restricciones de IP. Ten en cuenta que:

- La variable `workflow_definition` está declarada pero no se usa: `azurerm_logic_app_workflow` no admite la definición. Los triggers y acciones se despliegan aparte.
- Expone `integration_service_environment_id`, que corresponde a ISE, ya retirado.

`Automation/LogicAppStandard` tiene dos errores que impiden usarlo:

- Declara una variable llamada `version`, que Terraform reserva y no permite como nombre de variable de módulo. `terraform init` falla.
- Pasa `public_network_access_enabled` como argumento de `azurerm_logic_app_standard`, que no existe en el recurso (en 4.x es `public_network_access` con `Enabled`/`Disabled`).

Además, su ejemplo usa `FUNCTIONS_WORKER_RUNTIME = node` (el valor requerido ahora es `dotnet`), solo admite clave de storage y expone `client_certificate_mode`, cuando Standard no admite certificados de cliente entrantes. Hasta corregirlo, en la ficha despliego Standard con recursos nativos.

> Microsoft indica que, para Standard, la vía recomendada en Terraform es el provider AzAPI o el módulo AVM de `web-site`. Aquí uso `azurerm` para mantener la coherencia con el resto del repositorio.

### Estructura en el proyecto

```txt
/
├── providers.tf
├── consumption.tf   # Consumption con el módulo
├── standard.tf      # Standard con recursos nativos
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
      # 4.31.0: bloque enabled_metric en diagnostic settings (incluye vnet_content_share_enabled de 4.21.0).
      # < 5.0.0: restricción de los módulos de AzureTerraformModules.
      version = ">= 4.31.0, < 5.0.0"
    }
  }
}

provider "azurerm" {
  features {}
  storage_use_azuread = true
}

variable "tags" {
  description = "Tags corporativos comunes a todos los recursos."
  type        = map(string)
}
```

### Consumption con el módulo · `consumption.tf`

```hcl
# =============================================================================
# Logic Apps Consumption con el módulo Automation/LogicApp
# DEPENDENCY: Resource Group y Log Analytics workspace existentes
# DEPENDENCY: Integration Account existente si el flujo usa artefactos B2B
# La definición del workflow (triggers y acciones) se despliega desde el pipeline
# del propio workflow (ARM/Bicep); Terraform crea el recurso, identidad y controles.
# =============================================================================

variable "logic_apps_consumption" {
  description = "Workflows Consumption, una entrada por workflow."
  type = map(object({
    name                       = string
    resource_group_name        = string
    location                   = string
    enabled                    = optional(bool, true)
    integration_account_id     = optional(string)
    allowed_trigger_ip_ranges  = optional(list(string), [])
    allowed_content_ip_ranges  = optional(list(string), [])
    log_analytics_workspace_id = string
    tags                       = optional(map(string), {})
  }))
  default = {}
}

module "logic_app_consumption" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Automation/LogicApp?ref=main"
  for_each = var.logic_apps_consumption

  name                = each.value.name
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  enabled             = each.value.enabled

  logic_app_integration_account_id = each.value.integration_account_id

  identity = {
    type = "SystemAssigned"
  }

  # Sin rangos definidos no se envía el bloque access_control
  access_control = length(concat(each.value.allowed_trigger_ip_ranges, each.value.allowed_content_ip_ranges)) == 0 ? null : {
    trigger = length(each.value.allowed_trigger_ip_ranges) > 0 ? {
      allowed_caller_ip_address_range = each.value.allowed_trigger_ip_ranges
    } : null
    content = length(each.value.allowed_content_ip_ranges) > 0 ? {
      allowed_caller_ip_address_range = each.value.allowed_content_ip_ranges
    } : null
  }

  tags = merge(var.tags, each.value.tags)
}

resource "azurerm_monitor_diagnostic_setting" "logic_app_consumption" {
  for_each                   = var.logic_apps_consumption
  name                       = "diag-${each.value.name}"
  target_resource_id         = module.logic_app_consumption[each.key].id
  log_analytics_workspace_id = each.value.log_analytics_workspace_id

  enabled_log {
    category = "WorkflowRuntime"
  }

  enabled_metric {
    category = "AllMetrics"
  }
}
```

### Standard privado · `standard.tf`

```hcl
# =============================================================================
# Logic Apps Standard (Workflow Service Plan) privado, con recursos nativos
# El módulo Automation/LogicAppStandard no es utilizable hoy (ver la ficha).
# DEPENDENCY: Resource Group, storage account y Application Insights existentes
# DEPENDENCY: Private Endpoints de la storage para blob, queue, table y file con sus zonas DNS
# DEPENDENCY: Subnet de integración delegada a Microsoft.Web/serverFarms (/26 recomendado)
# DEPENDENCY: Subnet de Private Endpoints y zona privatelink.azurewebsites.net
# DEPENDENCY: Log Analytics workspace para los diagnostic settings
# =============================================================================

variable "logic_apps_standard" {
  description = "Logic Apps Standard, una entrada por app (cada una con su plan WS)."
  type = map(object({
    name                         = string
    plan_name                    = string
    resource_group_name          = string
    location                     = string
    sku_name                     = optional(string, "WS1")
    maximum_elastic_worker_count = optional(number, 20)
    zone_balancing_enabled       = optional(bool, false)
    worker_count                 = optional(number, 1) # >= 2 con zona redundante
    elastic_instance_minimum     = optional(number, 1)
    storage_account_name         = string
    storage_account_rg           = string
    content_share_name           = string
    content_share_quota_gb       = optional(number, 50)
    app_insights_name            = string
    app_insights_rg              = string
    integration_subnet_id        = string
    private_endpoint_subnet_id   = string
    private_dns_zone_id          = string
    log_analytics_workspace_id   = string
    app_settings                 = optional(map(string), {})
    tags                         = optional(map(string), {})
  }))
  default = {}

  validation {
    condition     = alltrue([for k, v in var.logic_apps_standard : contains(["WS1", "WS2", "WS3"], v.sku_name)])
    error_message = "sku_name debe ser WS1, WS2 o WS3 (Workflow Standard)."
  }

  validation {
    condition     = alltrue([for k, v in var.logic_apps_standard : !v.zone_balancing_enabled || v.worker_count >= 2])
    error_message = "Con zona redundante el plan necesita al menos 2 instancias (worker_count >= 2)."
  }
}

data "azurerm_storage_account" "logic_std" {
  for_each            = var.logic_apps_standard
  name                = each.value.storage_account_name
  resource_group_name = each.value.storage_account_rg
}

data "azurerm_application_insights" "logic_std" {
  for_each            = var.logic_apps_standard
  name                = each.value.app_insights_name
  resource_group_name = each.value.app_insights_rg
}

resource "azurerm_service_plan" "logic_std" {
  for_each                     = var.logic_apps_standard
  name                         = each.value.plan_name
  resource_group_name          = each.value.resource_group_name
  location                     = each.value.location
  os_type                      = "Windows"
  sku_name                     = each.value.sku_name
  maximum_elastic_worker_count = each.value.maximum_elastic_worker_count
  worker_count                 = each.value.worker_count
  zone_balancing_enabled       = each.value.zone_balancing_enabled
  tags                         = merge(var.tags, each.value.tags)
}

# La storage es privada: el share de contenido se crea antes que la app (plano de control)
resource "azurerm_storage_share" "logic_std" {
  for_each           = var.logic_apps_standard
  name               = each.value.content_share_name
  storage_account_id = data.azurerm_storage_account.logic_std[each.key].id
  quota              = each.value.content_share_quota_gb
}

resource "azurerm_logic_app_standard" "this" {
  for_each            = var.logic_apps_standard
  name                = each.value.name
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  app_service_plan_id = azurerm_service_plan.logic_std[each.key].id
  version             = "~4"

  # Azure Files no admite identidad gestionada: el plan WS necesita la clave de la storage
  storage_account_name       = each.value.storage_account_name
  storage_account_access_key = data.azurerm_storage_account.logic_std[each.key].primary_access_key
  storage_account_share_name = azurerm_storage_share.logic_std[each.key].name

  https_only                 = true
  public_network_access      = "Disabled"
  virtual_network_subnet_id  = each.value.integration_subnet_id
  vnet_content_share_enabled = true

  ftp_publish_basic_authentication_enabled = false
  scm_publish_basic_authentication_enabled = false

  identity {
    type = "SystemAssigned"
  }

  app_settings = merge(
    {
      "FUNCTIONS_WORKER_RUNTIME"              = "dotnet"
      "APPLICATIONINSIGHTS_CONNECTION_STRING" = data.azurerm_application_insights.logic_std[each.key].connection_string
    },
    each.value.app_settings
  )

  site_config {
    min_tls_version                  = "1.2"
    ftps_state                       = "Disabled"
    use_32_bit_worker_process        = false
    vnet_route_all_enabled           = true
    runtime_scale_monitoring_enabled = true
    elastic_instance_minimum         = each.value.elastic_instance_minimum
  }

  tags = merge(var.tags, each.value.tags)
}

resource "azurerm_private_endpoint" "logic_std" {
  for_each            = var.logic_apps_standard
  name                = "pe-${each.value.name}"
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  subnet_id           = each.value.private_endpoint_subnet_id

  private_service_connection {
    name                           = "psc-${each.value.name}"
    private_connection_resource_id = azurerm_logic_app_standard.this[each.key].id
    subresource_names              = ["sites"]
    is_manual_connection           = false
  }

  private_dns_zone_group {
    name                 = "default"
    private_dns_zone_ids = [each.value.private_dns_zone_id]
  }

  tags = merge(var.tags, each.value.tags)
}

resource "azurerm_monitor_diagnostic_setting" "logic_std" {
  for_each                   = var.logic_apps_standard
  name                       = "diag-${each.value.name}"
  target_resource_id         = azurerm_logic_app_standard.this[each.key].id
  log_analytics_workspace_id = each.value.log_analytics_workspace_id

  enabled_log {
    category = "WorkflowRuntime"
  }

  enabled_metric {
    category = "AllMetrics"
  }
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

logic_apps_consumption = {}

logic_apps_standard = {
  integracion = {
    name                         = "logic-<workload>-pro-<region>-001"
    plan_name                    = "asp-<workload>-pro-<region>-001"
    resource_group_name          = "<rg-workload-pro>"
    location                     = "<region>"
    sku_name                     = "WS1"
    maximum_elastic_worker_count = 20
    zone_balancing_enabled       = true
    worker_count                 = 2
    elastic_instance_minimum     = 2
    storage_account_name         = "<st-logic-pro>"
    storage_account_rg           = "<rg-workload-pro>"
    content_share_name           = "logic-<workload>-pro-content"
    app_insights_name            = "<appi-workload-pro>"
    app_insights_rg              = "<rg-monitoring-pro>"
    integration_subnet_id        = "<resourceId snet-logic-integration>"
    private_endpoint_subnet_id   = "<resourceId snet-private-endpoints>"
    private_dns_zone_id          = "<resourceId privatelink.azurewebsites.net>"
    log_analytics_workspace_id   = "<resourceId log-analytics-workspace>"
  }
}
```

En `dev.tfvars` y `pre.tfvars`, mismo esquema con `zone_balancing_enabled = false`, `worker_count = 1` y `elastic_instance_minimum = 1`.

Despliegue:

```powershell
terraform init
terraform plan -var-file="env/pro.tfvars" -out="pro.tfplan"
terraform apply "pro.tfplan"
```

### Equivalente en Bicep

Standard privado · `main.bicep`:

```bicep
// =============================================================================
// Logic Apps Standard (Workflow Service Plan) privado
// DEPENDENCY: Resource Group existente (targetScope = resourceGroup)
// DEPENDENCY: Storage account existente con Private Endpoints de blob, queue, table y file y sus zonas DNS
// DEPENDENCY: Subnet de integración delegada a Microsoft.Web/serverFarms (/26 recomendado)
// DEPENDENCY: Subnet de Private Endpoints y zona privatelink.azurewebsites.net
// DEPENDENCY: Application Insights y Log Analytics workspace existentes
// =============================================================================
targetScope = 'resourceGroup'

param location string = resourceGroup().location

@description('Nombre de la Logic App Standard (único global, forma parte del FQDN).')
param logicAppName string

param planName string

@allowed(['WS1', 'WS2', 'WS3'])
param skuName string = 'WS1'

@description('Instancias del plan. Con zona redundante, mínimo 2.')
@minValue(1)
param planCapacity int = 1

@description('Máximo de instancias en ráfaga (elastic).')
@minValue(1)
param maximumElasticWorkerCount int = 20

@description('Instancias siempre listas de la app.')
@minValue(1)
param minimumElasticInstanceCount int = 1

param zoneRedundant bool = false

param storageAccountName string

@description('Nombre del file share de contenido. Se crea aquí porque la storage es privada.')
param contentShareName string

param appInsightsName string

param logAnalyticsWorkspaceId string

@description('Resource ID de la subnet de integración (salida) delegada a Microsoft.Web/serverFarms.')
param integrationSubnetId string

@description('Resource ID de la subnet donde vive el Private Endpoint (entrada).')
param privateEndpointSubnetId string

@description('Resource ID de la zona privatelink.azurewebsites.net.')
param privateDnsZoneId string

param tags object = {}

resource storage 'Microsoft.Storage/storageAccounts@2023-05-01' existing = {
  name: storageAccountName
}

resource fileService 'Microsoft.Storage/storageAccounts/fileServices@2023-05-01' existing = {
  parent: storage
  name: 'default'
}

resource contentShare 'Microsoft.Storage/storageAccounts/fileServices/shares@2023-05-01' = {
  parent: fileService
  name: contentShareName
}

resource appInsights 'Microsoft.Insights/components@2020-02-02' existing = {
  name: appInsightsName
}

resource plan 'Microsoft.Web/serverfarms@2024-04-01' = {
  name: planName
  location: location
  tags: tags
  kind: 'elastic'
  sku: {
    name: skuName
    tier: 'WorkflowStandard'
    capacity: zoneRedundant ? max(planCapacity, 2) : planCapacity
  }
  properties: {
    maximumElasticWorkerCount: maximumElasticWorkerCount
    zoneRedundant: zoneRedundant
  }
}

// Azure Files no admite identidad gestionada: el plan WS necesita la cadena con clave
var storageConnectionString = 'DefaultEndpointsProtocol=https;AccountName=${storage.name};AccountKey=${storage.listKeys().keys[0].value};EndpointSuffix=${environment().suffixes.storage}'

resource logicApp 'Microsoft.Web/sites@2024-11-01' = {
  name: logicAppName
  location: location
  tags: tags
  kind: 'functionapp,workflowapp'
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    serverFarmId: plan.id
    httpsOnly: true
    publicNetworkAccess: 'Disabled'
    virtualNetworkSubnetId: integrationSubnetId
    outboundVnetRouting: {
      applicationTraffic: true // Route All
      contentShareTraffic: true // equivale a WEBSITE_CONTENTOVERVNET = 1
    }
    siteConfig: {
      minTlsVersion: '1.2'
      ftpsState: 'Disabled'
      use32BitWorkerProcess: false
      functionsRuntimeScaleMonitoringEnabled: true
      minimumElasticInstanceCount: minimumElasticInstanceCount
      appSettings: [
        { name: 'APP_KIND', value: 'workflowApp' }
        { name: 'FUNCTIONS_EXTENSION_VERSION', value: '~4' }
        { name: 'FUNCTIONS_WORKER_RUNTIME', value: 'dotnet' }
        { name: 'AzureFunctionsJobHost__extensionBundle__id', value: 'Microsoft.Azure.Functions.ExtensionBundle.Workflows' }
        { name: 'AzureFunctionsJobHost__extensionBundle__version', value: '[1.*, 2.0.0)' }
        { name: 'AzureWebJobsStorage', value: storageConnectionString }
        { name: 'WEBSITE_CONTENTAZUREFILECONNECTIONSTRING', value: storageConnectionString }
        { name: 'WEBSITE_CONTENTSHARE', value: contentShare.name }
        { name: 'APPLICATIONINSIGHTS_CONNECTION_STRING', value: appInsights.properties.ConnectionString }
      ]
    }
  }
}

// Sin publicación con credenciales básicas (FTP / SCM)
resource ftpPolicy 'Microsoft.Web/sites/basicPublishingCredentialsPolicies@2024-11-01' = {
  parent: logicApp
  name: 'ftp'
  properties: {
    allow: false
  }
}

resource scmPolicy 'Microsoft.Web/sites/basicPublishingCredentialsPolicies@2024-11-01' = {
  parent: logicApp
  name: 'scm'
  properties: {
    allow: false
  }
}

// Entrada privada
resource privateEndpoint 'Microsoft.Network/privateEndpoints@2024-05-01' = {
  name: 'pe-${logicAppName}'
  location: location
  tags: tags
  properties: {
    subnet: {
      id: privateEndpointSubnetId
    }
    privateLinkServiceConnections: [
      {
        name: 'psc-${logicAppName}'
        properties: {
          privateLinkServiceId: logicApp.id
          groupIds: [
            'sites'
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
        name: 'privatelink-azurewebsites-net'
        properties: {
          privateDnsZoneId: privateDnsZoneId
        }
      }
    ]
  }
}

resource diagnostics 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = {
  name: 'diag-${logicAppName}'
  scope: logicApp
  properties: {
    workspaceId: logAnalyticsWorkspaceId
    logs: [
      {
        category: 'WorkflowRuntime'
        enabled: true
      }
    ]
    metrics: [
      {
        category: 'AllMetrics'
        enabled: true
      }
    ]
  }
}

output logicAppId string = logicApp.id
output logicAppName string = logicApp.name
output defaultHostName string = logicApp.properties.defaultHostName
output principalId string = logicApp.identity.principalId
```

`main.pro.bicepparam`:

```bicep
using './main.bicep'

param logicAppName = 'logic-<workload>-pro-<region>-001'
param planName = 'asp-<workload>-pro-<region>-001'
param skuName = 'WS1'
param planCapacity = 2
param maximumElasticWorkerCount = 20
param minimumElasticInstanceCount = 2
param zoneRedundant = true
param storageAccountName = '<st-logic-pro>'
param contentShareName = 'logic-<workload>-pro-content'
param appInsightsName = '<appi-workload-pro>'
param logAnalyticsWorkspaceId = '<resourceId log-analytics-workspace>'
param integrationSubnetId = '<resourceId snet-logic-integration (delegada a Microsoft.Web/serverFarms)>'
param privateEndpointSubnetId = '<resourceId snet-private-endpoints>'
param privateDnsZoneId = '<resourceId privatelink.azurewebsites.net>'
param tags = {
  environment: 'pro'
  workload: '<workload>'
  owner: '<owner>'
  costCenter: '<cost-center>'
}
```

Consumption · `consumption.bicep` (aquí la definición del workflow sí viaja con el recurso):

```bicep
// =============================================================================
// Logic App Consumption: el recurso y su definición viajan juntos
// DEPENDENCY: workflow.json exportado del diseñador (propiedad "definition")
// DEPENDENCY: Log Analytics workspace existente
// =============================================================================
targetScope = 'resourceGroup'

param location string = resourceGroup().location
param workflowName string

@description('Rangos CIDR que pueden invocar el trigger. Vacío = sin restricción.')
param allowedTriggerIpRanges array = []

@description('Rangos CIDR que pueden ver entradas y salidas del historial. Vacío = sin restricción.')
param allowedContentIpRanges array = []

param integrationAccountId string = ''
param logAnalyticsWorkspaceId string
param tags object = {}

var triggerIpRanges = [for r in allowedTriggerIpRanges: { addressRange: r }]
var contentIpRanges = [for r in allowedContentIpRanges: { addressRange: r }]

resource workflow 'Microsoft.Logic/workflows@2019-05-01' = {
  name: workflowName
  location: location
  tags: tags
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    state: 'Enabled'
    definition: loadJsonContent('workflow.json').definition
    integrationAccount: empty(integrationAccountId) ? null : {
      id: integrationAccountId
    }
    accessControl: {
      triggers: empty(allowedTriggerIpRanges) ? null : {
        allowedCallerIpAddresses: triggerIpRanges
      }
      contents: empty(allowedContentIpRanges) ? null : {
        allowedCallerIpAddresses: contentIpRanges
      }
    }
  }
}

resource diagnostics 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = {
  name: 'diag-${workflowName}'
  scope: workflow
  properties: {
    workspaceId: logAnalyticsWorkspaceId
    logs: [
      {
        category: 'WorkflowRuntime'
        enabled: true
      }
    ]
    metrics: [
      {
        category: 'AllMetrics'
        enabled: true
      }
    ]
  }
}

output workflowId string = workflow.id
output principalId string = workflow.identity.principalId
```

Despliegue:

```powershell
az deployment group what-if --resource-group <rg-workload-pro> --parameters main.pro.bicepparam
az deployment group create  --resource-group <rg-workload-pro> --parameters main.pro.bicepparam
```

## Errores típicos

| Síntoma | Causa | Solución |
|---|---|---|
| `terraform init` falla con el módulo `LogicAppStandard` | Variable `version`, nombre reservado de Terraform | Renombrarla (p. ej. `runtime_version`) |
| `Unsupported argument "public_network_access_enabled"` | En `azurerm_logic_app_standard` el argumento es `public_network_access` | Usar `public_network_access = "Disabled"` |
| *"Access to the path 'C:\home\site\wwwroot\host.json' is denied"* o *"The network path was not found"* | La app no llega a la storage: falta algún Private Endpoint (blob, queue, table, file), la resolución DNS o el puerto 445 | Crear los cuatro, comprobar `nslookup` desde la subnet de integración y abrir 443 y 445 |
| *"Cannot reach host runtime"* en el panel de workflows | Mismo origen: storage inaccesible | Ídem; usar el detector *Logic App Down or Reporting Errors* |
| La app no arranca tras desactivar la clave de la storage | En WS no se puede desactivar el acceso por clave (Azure Files) | Mantener la clave (mejor en Key Vault) |
| Falla el despliegue con la cadena de Azure Files en Key Vault | La plataforma no resuelve la referencia al validar el share | `WEBSITE_SKIP_CONTENTSHARE_VALIDATION = 1` y crear el share antes |
| El despliegue desde VS Code o CLI falla con Private Endpoint de entrada | Solo funciona desde dentro de la VNet | Agente de despliegue en la VNet o Deployment Center |
| Triggers gestionados de tipo webhook (Event Grid, Dataverse) no se disparan | Con Private Endpoint de entrada no pueden llamar a la app | Usar trigger *built-in* equivalente o exponer un endpoint público controlado |
| Los conectores gestionados fallan detrás del firewall | No están permitidas sus IPs salientes de la región | Permitirlas en NSG/UDR/firewall |
| Acciones *Execute JavaScript Code* fallan o el workflow deja de funcionar | Falta `APP_KIND = workflowApp` en los app settings (típico en despliegues ARM/Bicep) | Añadirlo |
| Acción HTTP con error de *timeout* | Límite de la petición: 120 s fijos en Consumption, 225 s por defecto en Standard | Patrón asíncrono con *polling* o bucle *Until*; en Standard se puede ajustar el *timeout* |
| Facturas altas inesperadas en Standard | Un trigger *built-in* mal configurado (sin permisos sobre la cola o el contenedor) provoca escalado innecesario | Probar y vigilar los triggers *service provider* |
| No se puede activar la zona redundante en un plan existente | Solo se decide al crear el plan | Crear un plan nuevo con zona redundante |
| Mensajes duplicados en el destino | La entrega es *at least once* | Diseñar el destino para que sea idempotente |
