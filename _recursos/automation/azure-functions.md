---
title: "Azure Functions"
indice: automation
resumen: "Código por eventos que se paga por uso."
estado: documentado   # proximamente | en-curso | documentado
orden: 3
last_review: 2026-10-20
fuentes:
  - titulo: "Azure Functions hosting options"
    url: https://learn.microsoft.com/azure/azure-functions/functions-scale
  - titulo: "Flex Consumption plan"
    url: https://learn.microsoft.com/azure/azure-functions/flex-consumption-plan
  - titulo: "Create and manage apps in Flex Consumption"
    url: https://learn.microsoft.com/azure/azure-functions/flex-consumption-how-to
  - titulo: "Premium plan"
    url: https://learn.microsoft.com/azure/azure-functions/functions-premium-plan
  - titulo: "Consumption plan (legacy) y retirada de Linux"
    url: https://learn.microsoft.com/azure/azure-functions/consumption-plan
  - titulo: "Migrate Consumption to Flex Consumption"
    url: https://learn.microsoft.com/azure/azure-functions/migration/migrate-plan-consumption-to-flex
  - titulo: "Networking options"
    url: https://learn.microsoft.com/azure/azure-functions/functions-networking-options
  - titulo: "Storage considerations"
    url: https://learn.microsoft.com/azure/azure-functions/storage-considerations
  - titulo: "Identity-based connections and required roles"
    url: https://learn.microsoft.com/azure/azure-functions/manage-connections
  - titulo: "Automate resource deployment (Bicep/ARM)"
    url: https://learn.microsoft.com/azure/azure-functions/functions-infrastructure-as-code
  - titulo: "Zone redundancy"
    url: https://learn.microsoft.com/azure/azure-functions/functions-zone-redundancy
  - titulo: "Flex Consumption IaC samples"
    url: https://github.com/Azure-Samples/azure-functions-flex-consumption-samples
  - titulo: "azurerm_function_app_flex_consumption"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/function_app_flex_consumption
  - titulo: "azurerm 5.0 upgrade guide"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/5.0-upgrade-guide
  - titulo: "Azure Functions pricing"
    url: https://azure.microsoft.com/pricing/details/functions/
  - titulo: "Módulo Terraform Automation/FunctionApp"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Automation/FunctionApp
---

Azure Functions ejecuta código como respuesta a un evento: una petición HTTP, un mensaje en una cola, un fichero que llega a un blob o un temporizador. No gestionas servidores y, según el plan, pagas solo por las ejecuciones. La decisión que más pesa en un proyecto no es el código, sino **el plan de hosting**: condiciona el coste, la red privada, el arranque en frío y lo que podrás hacer con la identidad gestionada.

## Qué es y cuándo usarlo

### Cuándo sí

- Procesos cortos disparados por eventos: colas de Service Bus, Event Hubs, Event Grid, blobs o timers.
- APIs ligeras o *backends* de integración que no justifican un App Service encendido todo el día.
- Automatizaciones de plataforma escritas en código (Python, PowerShell, .NET…) que necesitan escalar solas.
- Orquestaciones con estado mediante Durable Functions.

### Cuándo no

| Si el caso es… | Mejor opción | Motivo |
|---|---|---|
| Integración con conectores y poco código | Logic Apps | El flujo se mantiene sin desarrolladores |
| Runbooks de operación sobre recursos Azure o híbridos | Azure Automation | Hybrid Worker, módulos de PowerShell gestionados |
| Microservicios con contenedores propios y varios lenguajes | Container Apps | Control de la imagen y de las revisiones |
| Peticiones HTTP que tardan más de 230 segundos | Durable Functions (patrón asíncrono) o App Service | Cualquier trigger HTTP se corta a los 230 s por el *idle timeout* del balanceador, sea cual sea el plan |

### Planes de hosting

| Plan | SKU (ARM) | SO | Escala máxima | Arranque en frío | Red privada (salida / entrada) | Timeout máx. | Facturación | Estado |
|---|---|---|---|---|---|---|---|---|
| **Flex Consumption** | `FC1` / `FlexConsumption` | Solo Linux | 1.000 instancias por grupo de funciones | Mejorado; se elimina con *always ready* | ✅ VNet / ✅ Private Endpoint | Sin límite (gracia de 60 min al reducir escala) | Ejecuciones + GB·s activos + baseline de *always ready* | **Recomendado** para serverless |
| **Premium (Elastic)** | `EP1`, `EP2`, `EP3` / `ElasticPremium` | Linux y Windows | Windows 100, Linux 20–100 según región | Sin arranque en frío (*always ready* + *prewarmed*) | ✅ VNet / ✅ Private Endpoint | Sin límite (gracia de 60 min) | Núcleo·s y memoria de las instancias asignadas; **mínimo 1 instancia siempre facturada** | GA |
| **Dedicated (App Service)** | `B1`, `S1`, `P1v3`… | Linux y Windows | 10–30 (100 en ASE) | No aplica con *Always On* | ✅ VNet / ✅ Private Endpoint | Sin límite (requiere *Always On*) | Precio del App Service Plan | GA |
| **Container Apps** | Entorno de Container Apps | Linux (contenedor) | 300–1.000 réplicas | Depende de réplicas mínimas | VNet del entorno / ❌ Private Endpoint de la app | Sin límite con réplicas ≥ 1 | Modelo de Container Apps | GA |
| **Consumption** (legacy) | `Y1` / `Dynamic` | Windows (Linux en retirada) | Windows 200, Linux 100 | Sí, escala a cero | ❌ / ❌ | 10 min (5 por defecto) | Ejecuciones + GB·s | **Legacy** |

Tamaños disponibles:

| Plan | Opción | vCPU | Memoria |
|---|---|---|---|
| Flex Consumption | 512 MB | 0,25 | 512 MB |
| Flex Consumption | 2.048 MB (por defecto) | 1 | 2 GB |
| Flex Consumption | 4.096 MB | 2 | 4 GB |
| Premium | EP1 | 1 | 3,5 GB |
| Premium | EP2 | 2 | 7 GB |
| Premium | EP3 | 4 | 14 GB |

### Qué plan recomiendo según el escenario

| Escenario del cliente | Plan | Por qué |
|---|---|---|
| Carga variable o esporádica, con acceso a recursos privados | **Flex Consumption** | Serverless con VNet, Private Endpoint e identidad gestionada sin claves |
| API con latencia exigente y tráfico constante | **Premium EP1+** o Flex con *always ready* | Sin arranque en frío; comparar coste de ambos con la calculadora |
| Dependencia de Windows (módulos de PowerShell 5.1, .NET Framework) | **Premium** o **Dedicated** en Windows | Flex solo existe en Linux |
| El cliente ya tiene un App Service Plan infrautilizado o necesita coste fijo | **Dedicated** | Reutiliza capacidad pagada; facturación predecible |
| Contenedor propio, GPU o convivir con microservicios | **Container Apps** | Control de la imagen y del entorno |
| Aislamiento total de red y compute | **Dedicated en App Service Environment v3** | Tenant único, todo dentro de la VNet |
| Nuevo proyecto en Consumption | **No** | Plan legacy; ir directamente a Flex |

### Datos que conviene llevar a la reunión

- **Consumption en Linux se retira el 30 de septiembre de 2028** y ya no recibe nuevas versiones de lenguaje. Las apps que seguían con runtime v3 en Linux Consumption dejaron de ejecutarse tras el 30 de septiembre de 2026. Windows Consumption no está afectado por ahora, pero la recomendación oficial es migrar a Flex.
- **No hay migración en caliente a Flex**: hay que crear una app nueva y volver a desplegar el código. Tampoco se puede salir de Flex a otro plan.
- **Premium nunca baja de una instancia facturada**, aunque no haya ejecuciones. Es el plan con el coste más predecible, pero no escala a cero.
- **Premium en Spain Central escala como máximo a 20 instancias**, tanto en Windows como en Linux. En North Europe y West Europe el máximo es 100.
- **Flex comparte una cuota regional de 250 núcleos por suscripción** entre todas sus apps. Las instancias *always ready* cuentan; las que están a cero, no. Se puede ampliar por soporte.
- **Flex no está en todas las regiones**. Compruébalo antes de comprometer la región del cliente (ver el comando en el módulo).

## Decisiones de diseño

| Decisión | Lo que aplico | Por qué |
|---|---|---|
| Plan | Flex Consumption por defecto; Premium solo con dependencia de Windows, apps compartiendo plan o latencia sin arranque en frío | Es el plan recomendado por Microsoft y el único serverless con red privada |
| Sistema operativo | Linux | Flex es solo Linux, Python solo existe en Linux y Windows Consumption es legacy |
| Runtime | Functions v4 y modelo *isolated worker* en .NET | Flex no soporta .NET *in-process* |
| Una app por plan | Sí en Flex (es obligatorio). En Premium agrupo apps del mismo dominio y SO | El plan Flex solo admite una app |
| Storage del host | Cuenta dedicada por app, `allowBlobPublicAccess = false`, en la misma región | La cuenta guarda claves de función, estado de triggers y, en Flex, el paquete de código |
| Autenticación al storage | Identidad gestionada (`AzureWebJobsStorage__accountName`) y `allowSharedKeyAccess = false` en Flex y Dedicated | Elimina secretos. En Premium no es posible: ver la fila siguiente |
| Premium y Azure Files | Premium y Consumption usan Azure Files para el contenido y **Azure Files no admite identidad gestionada** | Hay que dejar la clave compartida activa, guardar la cadena en Key Vault o crear la app sin Azure Files (con escala limitada) |
| Roles del host | `Storage Blob Data Owner` + `Storage Table Data Contributor` (eventos de diagnóstico). Añadir `Storage Queue Data Contributor` si hay triggers de blob | Mínimo privilegio según Microsoft Learn |
| Telemetría | Application Insights *workspace-based* con autenticación Entra (`APPLICATIONINSIGHTS_AUTHENTICATION_STRING = Authorization=AAD`) y rol `Monitoring Metrics Publisher` | Permite desactivar la autenticación local de App Insights |
| Entrada | `public_network_access = Disabled` + Private Endpoint (`sites`) con zona `privatelink.azurewebsites.net` | Zero Trust; la app solo se expone dentro de la red o detrás de APIM/App Gateway |
| Salida | Integración con VNet. En Premium y Dedicated, además, *Route All* activado; en Flex no hace falta porque todo el tráfico ya sale por la VNet | Permite controlar la salida con NSG, UDR y Azure Firewall |
| Subnet de integración | Flex: `/27` para una app, `/26` para varias, delegada a `Microsoft.App/environments`. Premium/Dedicated: `/26` Linux, `/24` Windows, delegada a `Microsoft.Web/serverFarms` | El tamaño no se puede cambiar después de asignarla |
| Storage privado | Private Endpoints de blob, queue y table (y file en Premium) con sus zonas DNS | El host necesita los tres servicios; sin ellos la app no arranca |
| Resiliencia | Flex con zona redundante: storage ZRS y al menos 2 instancias *always ready* por grupo | Es requisito de Microsoft para la redundancia de zona en Flex |
| Escalado | Fijar `maximum_instance_count` según los límites del destino (SQL, APIs de terceros) | Evita que el escalado tumbe dependencias |
| Costes (FinOps) | Flex sin *always ready* en dev/pre; *always ready* solo en el grupo HTTP de pro | El *baseline* de *always ready* se factura siempre y no tiene concesión gratuita |
| Despliegues sin corte | Flex: estrategia de *rolling update* (en preview). Premium/Dedicated: *deployment slots* | Flex no soporta slots |

Alineación con el Well-Architected Framework:

- **Seguridad**: identidad gestionada, sin claves en app settings, entrada privada y salida controlada.
- **Fiabilidad**: zona redundante, storage ZRS y límites de escalado alineados con las dependencias.
- **Coste**: plan serverless por defecto y *always ready* solo donde el negocio lo pida.
- **Excelencia operativa**: todo en IaC, App Insights con Entra ID y diagnósticos de la plataforma.
- **Rendimiento**: memoria de instancia y concurrencia por función ajustadas a la carga.

## Módulo de Terraform

### El módulo del repositorio

Módulo: [`Automation/FunctionApp`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Automation/FunctionApp) en [AzureTerraformModules](https://github.com/luisadanmunoz/AzureTerraformModules).

Qué cubre:

- `azurerm_linux_function_app` y `azurerm_windows_function_app` sobre un plan existente (Premium o Dedicated).
- Storage con clave o con identidad gestionada, integración con VNet, *route all*, restricciones de IP, CORS, identidad *SystemAssigned*/*UserAssigned* y `create = true/false`.

Qué no cubre todavía (se resuelve en el root, como en los ejemplos de abajo):

- **Flex Consumption** (`azurerm_function_app_flex_consumption`).
- El plan, la storage, el Private Endpoint, los roles RBAC y los *diagnostic settings*.

> No uses `PRO/services/function_app` del mismo repositorio: se basa en `azurerm_function_app` y `azurerm_app_service_plan`, que **se eliminaron en azurerm 5.0**.

Versiones: el módulo admite `azurerm >= 3.70.0, < 5.0.0`. Para Flex hace falta `>= 4.58.0` (rango 1–1.000 de `maximum_instance_count`). La rama 5.x del provider ya está publicada, así que el módulo tendrá que revisarse antes de subir de mayor.

Antes de elegir región para Flex (PowerShell con Azure CLI):

```powershell
az functionapp list-flexconsumption-locations --query "sort_by(@, &name)[].{Region:name}" -o table
# Solo regiones con redundancia de zona
az functionapp list-flexconsumption-locations --zone-redundant=true --query "sort_by(@, &name)[].{Region:name}" -o table
# Registrar el proveedor que necesita la integración con VNet de Flex
az provider register --namespace Microsoft.App
```

### Estructura en el proyecto

```txt
/
├── providers.tf
├── premium.tf        # Premium / Dedicated con el módulo
├── flex.tf           # Flex Consumption con recursos nativos
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
      # 4.58.0: maximum_instance_count 1-1000 en Flex. < 5.0.0: restricción del módulo Automation/FunctionApp.
      version = ">= 4.58.0, < 5.0.0"
    }
  }
}

provider "azurerm" {
  features {}
  storage_use_azuread = true
}
```

### Premium o Dedicated con el módulo · `premium.tf`

```hcl
# =============================================================================
# Premium (EP1-EP3) o Dedicated con el módulo Automation/FunctionApp
# DEPENDENCY: Resource Group, plan (EPx o Pxv3), storage account y Application Insights existentes
# DEPENDENCY: Subnet de integración delegada a Microsoft.Web/serverFarms (/26 Linux, /24 Windows)
# DEPENDENCY: Subnet de Private Endpoints y zona privatelink.azurewebsites.net
# =============================================================================

variable "function_apps" {
  description = "Function Apps en plan Premium (EP) o Dedicated, una entrada por app."
  type = map(object({
    name                          = string
    resource_group_name           = string
    location                      = string
    os_type                       = string
    service_plan_name             = string
    service_plan_rg               = string
    storage_account_name          = string
    storage_account_rg            = string
    storage_uses_managed_identity = bool # false en EP (Azure Files exige clave), true en Dedicated
    always_on                     = bool # true en Dedicated, false en EP
    app_insights_name             = string
    app_insights_rg               = string
    integration_subnet_id         = string
    private_endpoint_subnet_id    = string
    private_dns_zone_id           = string
    application_stack = object({
      dotnet_version              = optional(string)
      java_version                = optional(string)
      node_version                = optional(string)
      python_version              = optional(string)
      powershell_core_version     = optional(string)
      use_dotnet_isolated_runtime = optional(bool, false)
    })
    app_settings = optional(map(string), {})
    tags         = optional(map(string), {})
  }))
  default = {}

  validation {
    condition     = alltrue([for k, v in var.function_apps : contains(["Linux", "Windows"], v.os_type)])
    error_message = "os_type debe ser Linux o Windows."
  }
}

variable "tags" {
  description = "Tags corporativos comunes a todos los recursos."
  type        = map(string)
}

data "azurerm_service_plan" "this" {
  for_each            = var.function_apps
  name                = each.value.service_plan_name
  resource_group_name = each.value.service_plan_rg
}

data "azurerm_storage_account" "this" {
  for_each            = var.function_apps
  name                = each.value.storage_account_name
  resource_group_name = each.value.storage_account_rg
}

data "azurerm_application_insights" "this" {
  for_each            = var.function_apps
  name                = each.value.app_insights_name
  resource_group_name = each.value.app_insights_rg
}

module "function_app" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Automation/FunctionApp?ref=main"
  for_each = var.function_apps

  name                = each.value.name
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  os_type             = each.value.os_type
  service_plan_id     = data.azurerm_service_plan.this[each.key].id

  storage_account_name          = each.value.storage_account_name
  storage_uses_managed_identity = each.value.storage_uses_managed_identity
  storage_account_access_key    = each.value.storage_uses_managed_identity ? null : data.azurerm_storage_account.this[each.key].primary_access_key

  https_only                    = true
  public_network_access_enabled = false
  virtual_network_subnet_id     = each.value.integration_subnet_id

  identity = {
    type = "SystemAssigned"
  }

  site_config = {
    always_on                              = each.value.always_on
    vnet_route_all_enabled                 = true
    minimum_tls_version                    = "1.2"
    ftps_state                             = "Disabled"
    application_insights_connection_string = data.azurerm_application_insights.this[each.key].connection_string
    application_stack                      = each.value.application_stack
  }

  app_settings = each.value.app_settings
  tags         = merge(var.tags, each.value.tags)
}

# RBAC del host sobre la storage, solo cuando no se usa clave
resource "azurerm_role_assignment" "blob_owner" {
  for_each             = { for k, v in var.function_apps : k => v if v.storage_uses_managed_identity }
  scope                = data.azurerm_storage_account.this[each.key].id
  role_definition_name = "Storage Blob Data Owner"
  principal_id         = module.function_app[each.key].principal_id
}

resource "azurerm_role_assignment" "table_contributor" {
  for_each             = { for k, v in var.function_apps : k => v if v.storage_uses_managed_identity }
  scope                = data.azurerm_storage_account.this[each.key].id
  role_definition_name = "Storage Table Data Contributor"
  principal_id         = module.function_app[each.key].principal_id
}

# Entrada privada
resource "azurerm_private_endpoint" "function_app" {
  for_each            = var.function_apps
  name                = "pe-${each.value.name}"
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  subnet_id           = each.value.private_endpoint_subnet_id

  private_service_connection {
    name                           = "psc-${each.value.name}"
    private_connection_resource_id = module.function_app[each.key].id
    subresource_names              = ["sites"]
    is_manual_connection           = false
  }

  private_dns_zone_group {
    name                 = "default"
    private_dns_zone_ids = [each.value.private_dns_zone_id]
  }

  tags = merge(var.tags, each.value.tags)
}
```

### Flex Consumption · `flex.tf`

Mientras el módulo no soporte Flex, lo despliego con el recurso nativo:

```hcl
# =============================================================================
# Flex Consumption (FC1): recursos nativos, el módulo aún no lo soporta
# DEPENDENCY: Resource Group, storage account con el contenedor de despliegue y Application Insights existentes
# DEPENDENCY: Subnet de integración delegada a Microsoft.App/environments (/27 una app, /26 varias)
# DEPENDENCY: Proveedor Microsoft.App registrado en la suscripción
# DEPENDENCY: Subnet de Private Endpoints y zona privatelink.azurewebsites.net
# =============================================================================

variable "flex_function_apps" {
  description = "Function Apps en Flex Consumption, una entrada por app (un plan FC1 por app)."
  type = map(object({
    name                       = string
    plan_name                  = string
    resource_group_name        = string
    location                   = string
    runtime_name               = string
    runtime_version            = string
    instance_memory_in_mb      = optional(number, 2048)
    maximum_instance_count     = optional(number, 100)
    always_ready               = optional(map(number), {}) # { http = 1 }
    storage_account_name       = string
    storage_account_rg         = string
    deployment_container_name  = string
    app_insights_name          = string
    app_insights_rg            = string
    integration_subnet_id      = string
    private_endpoint_subnet_id = string
    private_dns_zone_id        = string
    app_settings               = optional(map(string), {})
    tags                       = optional(map(string), {})
  }))
  default = {}

  validation {
    condition     = alltrue([for k, v in var.flex_function_apps : contains([512, 2048, 4096], v.instance_memory_in_mb)])
    error_message = "instance_memory_in_mb debe ser 512, 2048 o 4096."
  }

  validation {
    condition     = alltrue([for k, v in var.flex_function_apps : contains(["dotnet-isolated", "node", "java", "powershell", "python", "custom"], v.runtime_name)])
    error_message = "runtime_name no soportado en Flex Consumption (el modelo .NET in-process no existe en Flex)."
  }

  validation {
    condition     = alltrue([for k, v in var.flex_function_apps : v.maximum_instance_count >= 1 && v.maximum_instance_count <= 1000])
    error_message = "maximum_instance_count debe estar entre 1 y 1000."
  }
}

data "azurerm_storage_account" "flex" {
  for_each            = var.flex_function_apps
  name                = each.value.storage_account_name
  resource_group_name = each.value.storage_account_rg
}

data "azurerm_application_insights" "flex" {
  for_each            = var.flex_function_apps
  name                = each.value.app_insights_name
  resource_group_name = each.value.app_insights_rg
}

resource "azurerm_service_plan" "flex" {
  for_each            = var.flex_function_apps
  name                = each.value.plan_name
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  os_type             = "Linux"
  sku_name            = "FC1"
  tags                = merge(var.tags, each.value.tags)
}

resource "azurerm_function_app_flex_consumption" "this" {
  for_each            = var.flex_function_apps
  name                = each.value.name
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  service_plan_id     = azurerm_service_plan.flex[each.key].id

  storage_container_type      = "blobContainer"
  storage_container_endpoint  = "${data.azurerm_storage_account.flex[each.key].primary_blob_endpoint}${each.value.deployment_container_name}"
  storage_authentication_type = "SystemAssignedIdentity"

  runtime_name           = each.value.runtime_name
  runtime_version        = each.value.runtime_version
  instance_memory_in_mb  = each.value.instance_memory_in_mb
  maximum_instance_count = each.value.maximum_instance_count

  dynamic "always_ready" {
    for_each = each.value.always_ready
    content {
      name           = always_ready.key
      instance_count = always_ready.value
    }
  }

  https_only                    = true
  public_network_access_enabled = false
  virtual_network_subnet_id     = each.value.integration_subnet_id

  identity {
    type = "SystemAssigned"
  }

  app_settings = merge(
    {
      "AzureWebJobsStorage__accountName"         = each.value.storage_account_name
      "APPLICATIONINSIGHTS_AUTHENTICATION_STRING" = "Authorization=AAD"
    },
    each.value.app_settings
  )

  site_config {
    minimum_tls_version                    = "1.2"
    application_insights_connection_string = data.azurerm_application_insights.flex[each.key].connection_string
  }

  tags = merge(var.tags, each.value.tags)
}

resource "azurerm_role_assignment" "flex_blob_owner" {
  for_each             = var.flex_function_apps
  scope                = data.azurerm_storage_account.flex[each.key].id
  role_definition_name = "Storage Blob Data Owner"
  principal_id         = azurerm_function_app_flex_consumption.this[each.key].identity[0].principal_id
}

resource "azurerm_role_assignment" "flex_table_contributor" {
  for_each             = var.flex_function_apps
  scope                = data.azurerm_storage_account.flex[each.key].id
  role_definition_name = "Storage Table Data Contributor"
  principal_id         = azurerm_function_app_flex_consumption.this[each.key].identity[0].principal_id
}

resource "azurerm_role_assignment" "flex_metrics_publisher" {
  for_each             = var.flex_function_apps
  scope                = data.azurerm_application_insights.flex[each.key].id
  role_definition_name = "Monitoring Metrics Publisher"
  principal_id         = azurerm_function_app_flex_consumption.this[each.key].identity[0].principal_id
}

resource "azurerm_private_endpoint" "flex" {
  for_each            = var.flex_function_apps
  name                = "pe-${each.value.name}"
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  subnet_id           = each.value.private_endpoint_subnet_id

  private_service_connection {
    name                           = "psc-${each.value.name}"
    private_connection_resource_id = azurerm_function_app_flex_consumption.this[each.key].id
    subresource_names              = ["sites"]
    is_manual_connection           = false
  }

  private_dns_zone_group {
    name                 = "default"
    private_dns_zone_ids = [each.value.private_dns_zone_id]
  }

  tags = merge(var.tags, each.value.tags)
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

function_apps = {}

flex_function_apps = {
  orders = {
    name                       = "func-<workload>-pro-<region>-001"
    plan_name                  = "asp-<workload>-pro-<region>-001"
    resource_group_name        = "<rg-workload-pro>"
    location                   = "<region>"
    runtime_name               = "python"
    runtime_version            = "3.12"
    instance_memory_in_mb      = 2048
    maximum_instance_count     = 100
    always_ready               = { http = 2 }
    storage_account_name       = "<st-host-pro>"
    storage_account_rg         = "<rg-workload-pro>"
    deployment_container_name  = "app-package"
    app_insights_name          = "<appi-workload-pro>"
    app_insights_rg            = "<rg-monitoring-pro>"
    integration_subnet_id      = "<resourceId snet-func-integration>"
    private_endpoint_subnet_id = "<resourceId snet-private-endpoints>"
    private_dns_zone_id        = "<resourceId privatelink.azurewebsites.net>"
  }
}
```

En `dev.tfvars` y `pre.tfvars`, mismo esquema con `always_ready = {}` y un `maximum_instance_count` bajo.

Despliegue:

```powershell
terraform init
terraform plan -var-file="env/pro.tfvars" -out="pro.tfplan"
terraform apply "pro.tfplan"
```

### Equivalente en Bicep (Flex Consumption)

`main.bicep`:

```bicep
// =============================================================================
// Azure Functions · Flex Consumption (FC1) privado, identidad gestionada sin claves
// DEPENDENCY: Resource Group existente (targetScope = resourceGroup)
// DEPENDENCY: Storage account existente con el contenedor de despliegue ya creado
// DEPENDENCY: Subnet de integración delegada a Microsoft.App/environments (/27 mínimo)
// DEPENDENCY: Subnet para Private Endpoints y zona privatelink.azurewebsites.net
// DEPENDENCY: Application Insights (workspace-based) existente
// DEPENDENCY: Proveedor Microsoft.App registrado en la suscripción
// =============================================================================
targetScope = 'resourceGroup'

@description('Región. Comprueba antes que soporta Flex Consumption.')
param location string = resourceGroup().location

@description('Nombre de la Function App (único global, forma parte del FQDN).')
@maxLength(32)
param functionAppName string

@description('Nombre del plan FC1.')
param planName string

@allowed(['dotnet-isolated', 'node', 'java', 'powershell', 'python', 'custom'])
param runtimeName string

@description('Versión del runtime, por ejemplo 8 para dotnet-isolated o 3.12 para python.')
param runtimeVersion string

@allowed([512, 2048, 4096])
param instanceMemoryMB int = 2048

@minValue(1)
@maxValue(1000)
param maximumInstanceCount int = 100

@description('Instancias always ready por grupo de escalado, p. ej. [{ name: \'http\', instanceCount: 1 }]. Vacío = escala a cero.')
param alwaysReady array = []

param zoneRedundant bool = false

@description('Storage account host (AzureWebJobsStorage) y de despliegue.')
param storageAccountName string

@description('Contenedor blob para el paquete de despliegue. Debe existir antes de crear la app.')
param deploymentContainerName string

param appInsightsName string

@description('Resource ID de la subnet de integración (salida) delegada a Microsoft.App/environments.')
param integrationSubnetId string

@description('Resource ID de la subnet donde vive el Private Endpoint (entrada).')
param privateEndpointSubnetId string

@description('Resource ID de la zona privatelink.azurewebsites.net.')
param privateDnsZoneId string

param tags object = {}

// Roles built-in (IDs fijos de Azure)
var roleStorageBlobDataOwner = 'b7e6dc6d-f1e8-4753-8033-0f276bb0955b'
var roleStorageTableDataContributor = '0a9a7e1f-b9d0-4cc4-a60d-0319b160aaa3'
var roleMonitoringMetricsPublisher = '3913510d-42f4-4e42-8a64-420c390055eb'

resource storage 'Microsoft.Storage/storageAccounts@2023-05-01' existing = {
  name: storageAccountName
}

resource appInsights 'Microsoft.Insights/components@2020-02-02' existing = {
  name: appInsightsName
}

resource plan 'Microsoft.Web/serverfarms@2024-04-01' = {
  name: planName
  location: location
  tags: tags
  kind: 'functionapp'
  sku: {
    tier: 'FlexConsumption'
    name: 'FC1'
  }
  properties: {
    reserved: true
    zoneRedundant: zoneRedundant
  }
}

resource functionApp 'Microsoft.Web/sites@2024-11-01' = {
  name: functionAppName
  location: location
  tags: tags
  kind: 'functionapp,linux'
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    serverFarmId: plan.id
    httpsOnly: true
    publicNetworkAccess: 'Disabled'
    // En Flex todo el tráfico de salida ya pasa por la VNet; Route All no es necesario
    virtualNetworkSubnetId: integrationSubnetId
    siteConfig: {
      minTlsVersion: '1.2'
      ftpsState: 'Disabled'
      appSettings: [
        {
          name: 'AzureWebJobsStorage__accountName'
          value: storage.name
        }
        {
          name: 'APPLICATIONINSIGHTS_CONNECTION_STRING'
          value: appInsights.properties.ConnectionString
        }
        {
          name: 'APPLICATIONINSIGHTS_AUTHENTICATION_STRING'
          value: 'Authorization=AAD'
        }
      ]
    }
    functionAppConfig: {
      deployment: {
        storage: {
          type: 'blobContainer'
          value: '${storage.properties.primaryEndpoints.blob}${deploymentContainerName}'
          authentication: {
            type: 'SystemAssignedIdentity'
          }
        }
      }
      runtime: {
        name: runtimeName
        version: runtimeVersion
      }
      scaleAndConcurrency: {
        instanceMemoryMB: instanceMemoryMB
        maximumInstanceCount: maximumInstanceCount
        alwaysReady: alwaysReady
      }
    }
  }
}

// RBAC mínimo del host sobre la storage y App Insights (Entra ID, sin claves)
resource raBlobOwner 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(storage.id, functionApp.id, roleStorageBlobDataOwner)
  scope: storage
  properties: {
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', roleStorageBlobDataOwner)
    principalId: functionApp.identity.principalId
    principalType: 'ServicePrincipal'
  }
}

resource raTableContributor 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(storage.id, functionApp.id, roleStorageTableDataContributor)
  scope: storage
  properties: {
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', roleStorageTableDataContributor)
    principalId: functionApp.identity.principalId
    principalType: 'ServicePrincipal'
  }
}

resource raMetricsPublisher 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(appInsights.id, functionApp.id, roleMonitoringMetricsPublisher)
  scope: appInsights
  properties: {
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', roleMonitoringMetricsPublisher)
    principalId: functionApp.identity.principalId
    principalType: 'ServicePrincipal'
  }
}

// Entrada privada: Private Endpoint sobre el subrecurso 'sites'
resource privateEndpoint 'Microsoft.Network/privateEndpoints@2024-05-01' = {
  name: 'pe-${functionAppName}'
  location: location
  tags: tags
  properties: {
    subnet: {
      id: privateEndpointSubnetId
    }
    privateLinkServiceConnections: [
      {
        name: 'psc-${functionAppName}'
        properties: {
          privateLinkServiceId: functionApp.id
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

output functionAppId string = functionApp.id
output functionAppName string = functionApp.name
output defaultHostName string = functionApp.properties.defaultHostName
output principalId string = functionApp.identity.principalId
```

`main.pro.bicepparam`:

```bicep
using './main.bicep'

param functionAppName = 'func-<workload>-pro-<region>-001'
param planName = 'asp-<workload>-pro-<region>-001'
param runtimeName = 'python'
param runtimeVersion = '3.12'
param instanceMemoryMB = 2048
param maximumInstanceCount = 100
param alwaysReady = [
  {
    name: 'http'
    instanceCount: 2
  }
]
param zoneRedundant = true
param storageAccountName = '<st-host-pro>'
param deploymentContainerName = 'app-package'
param appInsightsName = '<appi-workload-pro>'
param integrationSubnetId = '<resourceId subnet snet-func-integration (delegada a Microsoft.App/environments)>'
param privateEndpointSubnetId = '<resourceId subnet snet-private-endpoints>'
param privateDnsZoneId = '<resourceId privatelink.azurewebsites.net>'
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
| La app "Premium" no escala sola y cuesta más de lo previsto | Se creó un plan `P1v2`/`P1v3` (Dedicated) en lugar de `EP1` | Los planes Premium de Functions empiezan por **E** (`EP1`–`EP3`) |
| La app Premium no arranca tras deshabilitar las claves de la storage | Premium y Consumption montan el contenido en Azure Files, que no admite identidad gestionada | Mantener `allowSharedKeyAccess = true` con la cadena en Key Vault, o crear la app sin Azure Files, o pasar a Flex |
| Error al integrar Flex con la VNet | Subnet delegada a `Microsoft.Web/serverFarms` o proveedor `Microsoft.App` sin registrar | Delegar a `Microsoft.App/environments` y registrar `Microsoft.App` |
| La subnet no se puede usar para Flex | Ya tiene Private Endpoints, Service Endpoints o se comparte con un entorno de Container Apps | Subnet dedicada solo para la integración |
| La subnet de Premium se queda sin IPs al escalar | Cada instancia consume una IP y en un cambio de SKU el consumo se duplica | `/26` en Linux y `/24` en Windows desde el principio |
| El host falla al arrancar con identidad gestionada | Falta `Storage Blob Data Owner` (o la asignación aún no ha propagado) | Asignar el rol sobre la storage y reiniciar; añadir `Storage Table Data Contributor` para los eventos de diagnóstico |
| La app no arranca después de cerrar el firewall de la storage | Faltan Private Endpoints de blob, queue o table (o file en Premium) o sus zonas DNS | Crear los cuatro (tres en Flex) y comprobar la resolución desde la subnet de integración |
| Un trigger HTTP devuelve timeout a los 230 s | Límite del balanceador de entrada, no del plan | Patrón asíncrono con Durable Functions o encolar el trabajo y responder enseguida |
| Las funciones cortan a los 10 minutos | Consumption tiene un máximo de 10 minutos | Flex o Premium |
| Al crear el plan: "The pricing tier isn't allowed in this resource group" | El resource group ya está ligado a un pool de infraestructura incompatible (p. ej. Linux Consumption junto a Linux Premium) | Crear el plan en un resource group nuevo |
| Premium con Private Endpoint no pasa de 20 instancias | Límite de escalado para triggers HTTP restringidos por Private Endpoint | Dimensionarlo así o repartir la carga |
| Triggers no HTTP en Premium detrás de VNet no escalan | Por defecto no escalan más allá de las instancias *prewarmed* | Activar *runtime scale monitoring* (Flex lo soporta de forma nativa) |
| `WEBSITE_TIME_ZONE` no tiene efecto | No está soportado en Flex | Trabajar en UTC en el código y en las expresiones CRON |
| `terraform plan` falla con `azurerm_function_app` | Recurso eliminado en azurerm 5.0 | Migrar a `azurerm_linux_function_app` / `azurerm_windows_function_app` o a `azurerm_function_app_flex_consumption` |
| Se intenta cambiar una app existente a Flex | No hay migración en caliente entre planes | App nueva en Flex y nuevo despliegue del código |
