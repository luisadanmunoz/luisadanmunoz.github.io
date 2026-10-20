---
title: "Workspaces"
indice: avd
resumen: "La agrupación que el usuario ve al conectarse."
estado: documentado   # proximamente | en-curso | documentado
orden: 4
last_review: 2026-10-20
fuentes:
  - titulo: "Azure Virtual Desktop terminology (workspaces)"
    url: https://learn.microsoft.com/azure/virtual-desktop/terminology#workspaces
  - titulo: "Create an application group, a workspace, and assign users"
    url: https://learn.microsoft.com/azure/virtual-desktop/create-application-group-workspace
  - titulo: "Deploy Azure Virtual Desktop (add an application group to a workspace)"
    url: https://learn.microsoft.com/azure/virtual-desktop/deploy-azure-virtual-desktop#add-an-application-group-to-a-workspace
  - titulo: "Azure Virtual Desktop service architecture and resilience (feed discovery)"
    url: https://learn.microsoft.com/azure/virtual-desktop/service-architecture-resilience
  - titulo: "Azure Private Link with Azure Virtual Desktop"
    url: https://learn.microsoft.com/azure/virtual-desktop/private-link-overview
  - titulo: "Set up Private Link with Azure Virtual Desktop"
    url: https://learn.microsoft.com/azure/virtual-desktop/private-link-setup
  - titulo: "Set up email discovery to subscribe to your feed"
    url: https://learn.microsoft.com/windows-server/remote/remote-desktop-services/rds-email-discovery
  - titulo: "Azure Virtual Desktop FAQ (ubicación)"
    url: https://learn.microsoft.com/azure/virtual-desktop/faq
  - titulo: "Azure Virtual Desktop service limits"
    url: https://learn.microsoft.com/azure/azure-resource-manager/management/azure-subscription-service-limits#azure-virtual-desktop-service-limits
  - titulo: "Supported logs for Microsoft.DesktopVirtualization/workspaces"
    url: https://learn.microsoft.com/azure/azure-monitor/reference/supported-logs/microsoft-desktopvirtualization-workspaces-logs
  - titulo: "Microsoft.DesktopVirtualization workspaces (plantillas ARM/Bicep)"
    url: https://learn.microsoft.com/azure/templates/microsoft.desktopvirtualization/workspaces
  - titulo: "azurerm_virtual_desktop_workspace"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/virtual_desktop_workspace
  - titulo: "azurerm_virtual_desktop_workspace_application_group_association"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/virtual_desktop_workspace_application_group_association
  - titulo: "Submódulo Terraform VDI/modules/virtual_desktop_workspace"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/AzureVirtualDesktop/VDI/modules/virtual_desktop_workspace
  - titulo: "Submódulo Terraform VDI/modules/virtual_desktop_workspace_application_group_association"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/AzureVirtualDesktop/VDI/modules/virtual_desktop_workspace_application_group_association
  - titulo: "Módulo Terraform AzureVirtualDesktop/Workspace"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/AzureVirtualDesktop/Workspace
---

Un **workspace** es lo que el usuario ve en Windows App: un bloque con nombre (por ejemplo *"Contoso - Escritorios"*) que agrupa los escritorios y aplicaciones de los [application groups](/recursos/avd/application-groups/) registrados en él. No tiene capacidad ni coste propio. Aun así, **un application group que no está en un workspace no aparece en el cliente**, y es el recurso donde se decide si **la descarga del feed va por red privada**.

## Qué es y cuándo usarlo

### Cómo encaja

| Pieza | Relación con el workspace |
|---|---|
| Application group | Se registra en **un único** workspace; sin registro, el usuario no lo ve aunque tenga el rol |
| Host pool | No se registra directamente: llega a través de sus application groups |
| Usuario | Ve en Windows App un bloque por workspace, solo con los recursos a los que tiene acceso |
| Ubicación | El workspace tiene que estar en la misma región que sus application groups |

### Qué pasa cuando el usuario se conecta

1. **Descubrimiento del feed**: el cliente pregunta a `rdweb.wvd.microsoft.com` qué workspaces tiene el usuario. Traffic Manager lo dirige a la instancia del servicio más cercana.
2. **Descarga del feed**: por cada workspace, el cliente descarga los archivos RDP e iconos de lo que tiene asignado.
3. **Conexión**: al abrir un escritorio o una aplicación, la sesión va al host pool (eso se controla en el host pool).

La URL para suscribirse manualmente es `https://rdweb.wvd.microsoft.com/api/arm/feeddiscovery`. Para que el usuario solo tenga que escribir su correo, se publica un registro TXT `_msradc.<dominio>` con esa URL (*email discovery*).

### Private Link en el workspace

| Subrecurso | Para qué | Cuántos | Zona DNS privada |
|---|---|---|---|
| `feed` | Descarga del feed de ese workspace | Uno por workspace | `privatelink.wvd.microsoft.com` |
| `global` | Descubrimiento inicial de todos los workspaces | **Uno para toda la organización**, en un workspace vacío y dedicado | `privatelink-global.wvd.microsoft.com` |

- El acceso público del workspace solo tiene dos valores: habilitado o deshabilitado (en el host pool hay cuatro).
- **El workspace del endpoint `global` siempre es accesible por la red pública**, aunque se configure como privado: el servicio ignora ese ajuste.
- **Si se borra el workspace del `global`, deja de funcionar el descubrimiento de feeds de todos los usuarios.** Por eso lleva un bloqueo contra borrado.
- Desde septiembre de 2023, el `global` usa su propia zona (`privatelink-global.wvd.microsoft.com`). Compartir `privatelink.wvd.microsoft.com` dejó de estar soportado.

Combinaciones de Private Link que admite el servicio:

| Escenario | PE `global` | PE `feed` | PE `connection` (host pool) |
|---|---|---|---|
| Todo privado | ✅ | ✅ | ✅ |
| Descubrimiento público, resto privado | ❌ | ✅ | ✅ |
| Solo las sesiones privadas | ❌ | ❌ | ✅ |
| Todo público | ❌ | ❌ | ❌ |

### Límites que conviene tener a mano

| Límite | Valor |
|---|---|
| Workspaces por tenant de Entra ID | 1.300 |
| Host pools por workspace | 400 |
| Workspaces por application group | 1 |
| PE `global` por organización | 1 |
| Nombre del workspace | 3 a 64 caracteres |

### Qué escenario recomiendo

| Escenario del cliente | Diseño | Por qué |
|---|---|---|
| Despliegue en una región | Un workspace por entorno (`pro`, `pre`) con nombre de negocio | Lo que ve el usuario queda limpio y ordenado |
| Varias regiones | Un workspace por región (los application groups tienen que estar en su misma región) | Requisito de ubicación del servicio |
| Varias unidades de negocio que no deben ver lo de las demás | Workspaces separados solo si cambia el nombre visible; el acceso lo siguen dando los application groups | El workspace agrupa, no da permisos |
| Requisito de no exponer nada a Internet | `public_network_access_enabled = false`, PE `feed` en cada workspace y PE `global` en un workspace dedicado en el hub | Todo el flujo del cliente por la red privada |
| Usuarios en Internet, sesiones privadas | Workspace público y host pool con PE `connection` | Sin depender de VPN para descargar el feed |

### Datos que conviene llevar a la reunión

- **El workspace no da permisos**: solo agrupa. El acceso lo da el rol sobre el application group.
- **El nombre del workspace es lo primero que ve el usuario** en Windows App; conviene un nombre de negocio, no el técnico.
- **Con email discovery** el usuario se suscribe escribiendo su correo, sin copiar URLs.
- **Todo privado exige una pieza compartida en toda la organización** (el PE `global`): se decide quién la aloja, normalmente el hub.
- **Hay un caso de cliente Windows que falla con Private Link**: el Remote Desktop client para Windows, en una red privada sin Internet, si el usuario está suscrito a la vez a feeds públicos y privados.

## Decisiones de diseño

| Decisión | Lo que aplico | Por qué |
|---|---|---|
| Número de workspaces | Uno por entorno y región | Simplicidad y requisito de región |
| Nombre visible | `friendly_name` con el nombre de la empresa y el propósito | Es lo que ve el usuario |
| Registro de application groups | Desde el workspace, en IaC, con validación de grupo único y misma región | Un grupo solo puede estar en un workspace |
| Red | `public_network_access_enabled = false` + PE `feed` cuando el cliente pide todo privado | Feed por la red privada |
| Descubrimiento | Un único workspace vacío con PE `global` en el hub y bloqueo `CanNotDelete` | Pieza compartida de la que dependen todos los usuarios |
| DNS | Zonas `privatelink.wvd.microsoft.com` y `privatelink-global.wvd.microsoft.com` enlazadas a las VNets de los clientes (o reenvío desde el DNS corporativo) | El cliente tiene que resolver las IPs privadas |
| Observabilidad | *Diagnostic settings* Checkpoint, Error, Management y Feed a Log Analytics | Las categorías que pide AVD Insights para el workspace |
| Suscripción de usuarios | Registro TXT `_msradc` en el dominio de correo | Alta de usuarios sin URLs |

Alineación con el Well-Architected Framework:

- **Seguridad**: feed privado y descubrimiento privado cuando el cliente lo exige.
- **Fiabilidad**: bloqueo del workspace `global`; un workspace por región.
- **Coste**: sin coste propio; solo los Private Endpoints.
- **Excelencia operativa**: registro de grupos y endpoints en IaC; diagnósticos del feed.
- **Rendimiento**: el servicio enruta al usuario a la instancia más cercana; no requiere ajuste.

## Módulo de Terraform

### Los módulos del repositorio

| Pieza | Módulo | Estado |
|---|---|---|
| Workspace | [`AzureVirtualDesktop/VDI/modules/virtual_desktop_workspace`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/AzureVirtualDesktop/VDI/modules/virtual_desktop_workspace) | Utilizable (recomendado) |
| Registro de application groups | [`AzureVirtualDesktop/VDI/modules/virtual_desktop_workspace_application_group_association`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/AzureVirtualDesktop/VDI/modules/virtual_desktop_workspace_application_group_association) | Utilizable |
| Workspace (independiente) | [`AzureVirtualDesktop/Workspace`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/AzureVirtualDesktop/Workspace) | Utilizable con condiciones |

Los dos submódulos de `VDI` son finos y no usan `locals`. No crean Private Endpoints ni *diagnostic settings*, que van como recursos nativos.

`AzureVirtualDesktop/Workspace`:

- Deja `public_network_access_enabled = true` por defecto.
- Recorre `application_group_ids` con `for_each = toset(...)`. Si los application groups se crean en el mismo `apply`, sus IDs no se conocen en el `plan` y Terraform no puede calcular las claves del `for_each`.
- Usa `locals` y `count`.

En la ficha el registro va por **claves** de `var.application_groups`, que sí se conocen en el `plan`.

**Cambio en la ficha de Application Groups**: el registro en el workspace pasa a `workspaces.tf`. El `workspace_id` de `var.application_groups` queda solo para workspaces de otro proyecto, y una `precondition` impide registrar un grupo por los dos lados.

### Estructura en el proyecto

```txt
/
├── providers.tf
├── host_pools.tf           # ficha Host Pools
├── session_hosts.tf        # ficha Session Hosts
├── application_groups.tf   # ficha Application Groups
├── workspaces.tf           # workspaces, registro de grupos, Private Link y diagnósticos
└── env/
    ├── dev.tfvars
    ├── pre.tfvars
    └── pro.tfvars
```

### `providers.tf`

```hcl
# Mismo providers.tf del proyecto de AVD (host pools, session hosts, application groups)
terraform {
  required_version = ">= 1.6.0"
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      # < 5.0.0: restricción de los módulos de AzureTerraformModules.
      version = ">= 4.0.0, < 5.0.0"
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

variable "tags" {
  description = "Tags corporativos comunes a todos los recursos."
  type        = map(string)
}
```

### Workspaces · `workspaces.tf`

```hcl
# =============================================================================
# Workspaces: feed de usuario, registro de application groups, Private Link y diagnósticos
# Submódulos de AzureVirtualDesktop/VDI/modules
# DEPENDENCY: application_groups.tf de la ficha Application Groups en el mismo root (module.application_group)
# DEPENDENCY: Subnet de Private Endpoints y zonas privatelink.wvd.microsoft.com (feed)
#             y privatelink-global.wvd.microsoft.com (global) enlazadas a las VNets de los clientes
# DEPENDENCY: Resource provider Microsoft.DesktopVirtualization re-registrado en la suscripción (Private Link)
# DEPENDENCY: Log Analytics workspace existente
# =============================================================================

variable "workspaces" {
  description = "Workspaces (clave = nombre del workspace)."
  type = map(object({
    resource_group_name = string
    location            = string # la misma región que sus application groups
    friendly_name       = string # nombre que ve el usuario en Windows App
    description         = optional(string)

    # Claves de var.application_groups que se publican en este workspace
    application_groups = list(string)

    public_network_access_enabled = optional(bool, false)
    private_endpoint = optional(object({
      subnet_id           = string
      private_dns_zone_id = string # privatelink.wvd.microsoft.com
    }))

    log_analytics_workspace_id = string
    tags                       = optional(map(string), {})
  }))

  validation {
    condition     = alltrue([for k, v in var.workspaces : v.public_network_access_enabled || v.private_endpoint != null])
    error_message = "Un workspace sin acceso público necesita private_endpoint (subrecurso feed)."
  }

  validation {
    # Un application group solo puede estar en un workspace
    condition = length(flatten([for k, v in var.workspaces : v.application_groups])) == length(distinct(flatten([for k, v in var.workspaces : v.application_groups])))
    error_message = "Un application group solo puede registrarse en un workspace."
  }
}

variable "feed_discovery" {
  description = <<-EOT
    Workspace vacío y dedicado para el Private Endpoint 'global' (descubrimiento inicial del feed).
    Solo UNO en todo el despliegue de AVD de la organización: dejar null si ya existe en otro proyecto.
  EOT
  type = object({
    name                = string
    resource_group_name = string
    location            = string
    subnet_id           = string
    private_dns_zone_id = string # privatelink-global.wvd.microsoft.com
    tags                = optional(map(string), {})
  })
  default = null
}

module "workspace" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//AzureVirtualDesktop/VDI/modules/virtual_desktop_workspace?ref=main"
  for_each = var.workspaces

  virtual_desktop_workspace_name = each.key
  resource_group_name            = each.value.resource_group_name
  location                       = each.value.location
  friendly_name                  = each.value.friendly_name
  description                    = each.value.description
  public_network_access_enabled  = each.value.public_network_access_enabled

  tags = merge(var.tags, each.value.tags)
}

module "workspace_application_group" {
  source = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//AzureVirtualDesktop/VDI/modules/virtual_desktop_workspace_application_group_association?ref=main"
  for_each = {
    for item in flatten([
      for wk, w in var.workspaces : [
        for ag in w.application_groups : {
          key       = "${wk}/${ag}"
          workspace = wk
          app_group = ag
        }
      ]
    ]) : item.key => item
  }

  workspace_id         = module.workspace[each.value.workspace].id
  application_group_id = module.application_group[each.value.app_group].id
}

# Private Endpoint 'feed' (uno por workspace)
resource "azurerm_private_endpoint" "workspace_feed" {
  for_each            = { for k, v in var.workspaces : k => v if v.private_endpoint != null }
  name                = "pe-${each.key}-feed"
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  subnet_id           = each.value.private_endpoint.subnet_id

  private_service_connection {
    name                           = "psc-${each.key}-feed"
    private_connection_resource_id = module.workspace[each.key].id
    subresource_names              = ["feed"]
    is_manual_connection           = false
  }

  private_dns_zone_group {
    name                 = "default"
    private_dns_zone_ids = [each.value.private_endpoint.private_dns_zone_id]
  }

  tags = merge(var.tags, each.value.tags)
}

# Workspace dedicado al descubrimiento inicial del feed (sin application groups)
module "workspace_feed_discovery" {
  source = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//AzureVirtualDesktop/VDI/modules/virtual_desktop_workspace?ref=main"
  count  = var.feed_discovery != null ? 1 : 0

  virtual_desktop_workspace_name = var.feed_discovery.name
  resource_group_name            = var.feed_discovery.resource_group_name
  location                       = var.feed_discovery.location
  friendly_name                  = "Descubrimiento de feed (no borrar)"
  description                    = "Termina el Private Endpoint global de AVD. Sin application groups."
  public_network_access_enabled  = true # el servicio ignora el acceso privado en este workspace

  tags = merge(var.tags, var.feed_discovery.tags)
}

resource "azurerm_private_endpoint" "feed_discovery_global" {
  count               = var.feed_discovery != null ? 1 : 0
  name                = "pe-${var.feed_discovery.name}-global"
  resource_group_name = var.feed_discovery.resource_group_name
  location            = var.feed_discovery.location
  subnet_id           = var.feed_discovery.subnet_id

  private_service_connection {
    name                           = "psc-${var.feed_discovery.name}-global"
    private_connection_resource_id = module.workspace_feed_discovery[0].id
    subresource_names              = ["global"]
    is_manual_connection           = false
  }

  private_dns_zone_group {
    name                 = "default"
    private_dns_zone_ids = [var.feed_discovery.private_dns_zone_id]
  }

  tags = merge(var.tags, var.feed_discovery.tags)
}

resource "azurerm_management_lock" "feed_discovery" {
  count      = var.feed_discovery != null ? 1 : 0
  name       = "no-borrar-feed-discovery"
  scope      = module.workspace_feed_discovery[0].id
  lock_level = "CanNotDelete"
  notes      = "Si se borra este workspace deja de funcionar el descubrimiento de feeds de todos los usuarios."
}

resource "azurerm_monitor_diagnostic_setting" "workspace" {
  for_each                   = var.workspaces
  name                       = "diag-${each.key}"
  target_resource_id         = module.workspace[each.key].id
  log_analytics_workspace_id = each.value.log_analytics_workspace_id

  enabled_log {
    category = "Checkpoint"
  }
  enabled_log {
    category = "Error"
  }
  enabled_log {
    category = "Management"
  }
  enabled_log {
    category = "Feed"
  }

  lifecycle {
    precondition {
      condition = alltrue([
        for ag in each.value.application_groups :
        contains(keys(var.application_groups), ag) && var.application_groups[ag].location == each.value.location
      ])
      error_message = "Los application groups del workspace deben existir en var.application_groups y estar en su misma región."
    }
    precondition {
      # Evita registrar el mismo grupo dos veces (aquí y con workspace_id en application_groups.tf)
      condition     = alltrue([for ag in each.value.application_groups : try(var.application_groups[ag].workspace_id, null) == null])
      error_message = "Un application group registrado aquí no puede tener también workspace_id en var.application_groups."
    }
  }
}

output "workspace_ids" {
  description = "IDs de los workspaces."
  value       = { for k, m in module.workspace : k => m.id }
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

workspaces = {
  "vdws-<workload>-pro" = {
    resource_group_name = "<rg-avd-pro>"
    location            = "<region>"
    friendly_name       = "<Empresa> - Escritorios"

    application_groups = [
      "vdag-<workload>-pro-desktop",
      "vdag-<workload>-pro-finanzas",
      "vdag-<workload>-pro-dev-desktop",
    ]

    public_network_access_enabled = false
    private_endpoint = {
      subnet_id           = "<resourceId snet-privateendpoints>"
      private_dns_zone_id = "<resourceId privatelink.wvd.microsoft.com>"
    }

    log_analytics_workspace_id = "<resourceId log-analytics-workspace>"
  }
}

# Solo en el proyecto que aloja el endpoint global de la organización (uno en total)
feed_discovery = {
  name                = "vdws-feeddiscovery-global"
  resource_group_name = "<rg-avd-shared>"
  location            = "<region>"
  subnet_id           = "<resourceId snet-privateendpoints-hub>"
  private_dns_zone_id = "<resourceId privatelink-global.wvd.microsoft.com>"
}
```

`feed_discovery` solo se informa en **un** proyecto de toda la organización; en el resto, `null`. En `dev.tfvars` y `pre.tfvars`, un workspace por entorno con sus application groups.

Despliegue y comprobación:

```powershell
terraform init
terraform plan -var-file="env/pro.tfvars" -out="pro.tfplan"
terraform apply "pro.tfplan"

# Application groups registrados en el workspace
(Get-AzWvdWorkspace -Name "vdws-<workload>-pro" -ResourceGroupName "<rg-avd-pro>").ApplicationGroupReference

# Resolución privada desde un equipo cliente en la red corporativa
Resolve-DnsName "rdweb.wvd.microsoft.com"
```

Registro TXT para *email discovery*, en el DNS público del dominio de correo:

```txt
_msradc.<dominio>   TXT   "https://rdweb.wvd.microsoft.com/api/arm/feeddiscovery"
```

### Equivalente en Bicep

`main.bicep`. En ARM, la lista `applicationGroupReferences` es la lista completa: lo que no esté en ella se desregistra al desplegar.

```bicep
// =============================================================================
// Workspace de AVD privado con sus application groups, Private Endpoint 'feed',
// diagnósticos y, opcionalmente, el workspace dedicado al descubrimiento global
// DEPENDENCY: Resource Group existente (targetScope = resourceGroup)
// DEPENDENCY: Application groups existentes en la misma región
// DEPENDENCY: Zonas privatelink.wvd.microsoft.com y privatelink-global.wvd.microsoft.com
// DEPENDENCY: Resource provider Microsoft.DesktopVirtualization re-registrado en la suscripción
// DEPENDENCY: Log Analytics workspace existente
// =============================================================================
targetScope = 'resourceGroup'

param location string = resourceGroup().location

@minLength(3)
@maxLength(64)
param workspaceName string

@description('Nombre que ve el usuario en Windows App.')
param friendlyName string

@description('IDs de los application groups que se publican en este workspace (misma región).')
param applicationGroupIds array

@allowed(['Enabled', 'Disabled'])
param publicNetworkAccess string = 'Disabled'

param privateEndpointSubnetId string
param privateDnsZoneId string
param logAnalyticsWorkspaceId string

@description('true solo en el despliegue que aloja el único endpoint global de la organización.')
param deployFeedDiscovery bool = false

param feedDiscoveryWorkspaceName string = 'vdws-feeddiscovery-global'
param globalPrivateDnsZoneId string = ''

param tags object = {}

resource workspace 'Microsoft.DesktopVirtualization/workspaces@2025-10-10' = {
  name: workspaceName
  location: location
  tags: tags
  properties: {
    friendlyName: friendlyName
    applicationGroupReferences: applicationGroupIds
    publicNetworkAccess: publicNetworkAccess
  }
}

resource feedEndpoint 'Microsoft.Network/privateEndpoints@2024-05-01' = {
  name: 'pe-${workspaceName}-feed'
  location: location
  tags: tags
  properties: {
    subnet: {
      id: privateEndpointSubnetId
    }
    privateLinkServiceConnections: [
      {
        name: 'psc-${workspaceName}-feed'
        properties: {
          privateLinkServiceId: workspace.id
          groupIds: [
            'feed'
          ]
        }
      }
    ]
  }
}

resource feedDnsZoneGroup 'Microsoft.Network/privateEndpoints/privateDnsZoneGroups@2024-05-01' = {
  parent: feedEndpoint
  name: 'default'
  properties: {
    privateDnsZoneConfigs: [
      {
        name: 'privatelink-wvd-microsoft-com'
        properties: {
          privateDnsZoneId: privateDnsZoneId
        }
      }
    ]
  }
}

resource diagnostics 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = {
  name: 'diag-${workspaceName}'
  scope: workspace
  properties: {
    workspaceId: logAnalyticsWorkspaceId
    logs: [
      { category: 'Checkpoint', enabled: true }
      { category: 'Error', enabled: true }
      { category: 'Management', enabled: true }
      { category: 'Feed', enabled: true }
    ]
  }
}

// Workspace vacío para el endpoint 'global' (uno en toda la organización)
resource feedDiscoveryWorkspace 'Microsoft.DesktopVirtualization/workspaces@2025-10-10' = if (deployFeedDiscovery) {
  name: feedDiscoveryWorkspaceName
  location: location
  tags: tags
  properties: {
    friendlyName: 'Descubrimiento de feed (no borrar)'
    description: 'Termina el Private Endpoint global de AVD. Sin application groups.'
    publicNetworkAccess: 'Enabled' // el servicio ignora el acceso privado en este workspace
  }
}

resource feedDiscoveryLock 'Microsoft.Authorization/locks@2020-05-01' = if (deployFeedDiscovery) {
  name: 'no-borrar-feed-discovery'
  scope: feedDiscoveryWorkspace
  properties: {
    level: 'CanNotDelete'
    notes: 'Si se borra este workspace deja de funcionar el descubrimiento de feeds de todos los usuarios.'
  }
}

resource globalEndpoint 'Microsoft.Network/privateEndpoints@2024-05-01' = if (deployFeedDiscovery) {
  name: 'pe-${feedDiscoveryWorkspaceName}-global'
  location: location
  tags: tags
  properties: {
    subnet: {
      id: privateEndpointSubnetId
    }
    privateLinkServiceConnections: [
      {
        name: 'psc-${feedDiscoveryWorkspaceName}-global'
        properties: {
          privateLinkServiceId: feedDiscoveryWorkspace.id
          groupIds: [
            'global'
          ]
        }
      }
    ]
  }
}

resource globalDnsZoneGroup 'Microsoft.Network/privateEndpoints/privateDnsZoneGroups@2024-05-01' = if (deployFeedDiscovery) {
  parent: globalEndpoint
  name: 'default'
  properties: {
    privateDnsZoneConfigs: [
      {
        name: 'privatelink-global-wvd-microsoft-com'
        properties: {
          privateDnsZoneId: globalPrivateDnsZoneId
        }
      }
    ]
  }
}

output workspaceId string = workspace.id
```

`main.pro.bicepparam`:

```bicep
using 'main.bicep'

param workspaceName = 'vdws-<workload>-pro'
param friendlyName = '<Empresa> - Escritorios'

param applicationGroupIds = [
  '<resourceId vdag-<workload>-pro-desktop>'
  '<resourceId vdag-<workload>-pro-finanzas>'
  '<resourceId vdag-<workload>-pro-dev-desktop>'
]

param publicNetworkAccess = 'Disabled'
param privateEndpointSubnetId = '<resourceId snet-privateendpoints>'
param privateDnsZoneId = '<resourceId privatelink.wvd.microsoft.com>'
param logAnalyticsWorkspaceId = '<resourceId log-analytics-workspace>'

// Solo en el despliegue que aloja el endpoint global de la organización
param deployFeedDiscovery = false
param globalPrivateDnsZoneId = '<resourceId privatelink-global.wvd.microsoft.com>'

param tags = {
  environment: 'pro'
  workload: '<workload>'
  owner: '<owner>'
  costcenter: '<costcenter>'
}
```

Despliegue:

```powershell
az deployment group what-if --resource-group <rg-avd-pro> --parameters main.pro.bicepparam
az deployment group create  --resource-group <rg-avd-pro> --parameters main.pro.bicepparam
```

## Errores típicos

| Síntoma | Causa | Solución |
|---|---|---|
| El usuario se suscribe pero no ve ningún recurso | Los application groups no están registrados en el workspace o no tiene el rol en ellos | Registrar el grupo y revisar *Desktop Virtualization User* |
| Error al registrar un application group | Ya está registrado en otro workspace | Quitarlo del workspace anterior |
| Error de ubicación al registrar el grupo | Workspace y application group en regiones distintas | Workspace en la región de sus grupos |
| `Invalid for_each argument` en el módulo `Workspace` | `toset()` sobre IDs que no se conocen hasta el `apply` | Registrar los grupos por clave, como en esta ficha |
| Tras desplegar con Bicep desaparecen grupos del workspace | `applicationGroupReferences` sustituye la lista entera | Gestionar la lista solo desde un sitio |
| Con el workspace en privado, el cliente no descarga el feed | Falta el PE `feed` o el cliente no resuelve `privatelink.wvd.microsoft.com` | Crear el PE y enlazar la zona o reenviar el DNS |
| El descubrimiento sigue saliendo por Internet | No hay PE `global` o la zona `privatelink-global.wvd.microsoft.com` no se resuelve | Crear el único PE `global` y su zona |
| Se configuró el workspace del `global` como privado y sigue accesible | El servicio ignora ese ajuste en ese workspace | Comportamiento esperado |
| Todos los usuarios dejan de descubrir sus feeds | Se borró el workspace del PE `global` | Recrearlo con su PE; protegerlo con `CanNotDelete` |
| El cliente de Windows no muestra el feed en una red sin Internet | Suscrito a la vez a feeds públicos y privados | Limitación documentada: usar solo el feed privado en esa red |
| Email discovery no encuentra la suscripción | Registro `_msradc` mal escrito o en el dominio equivocado | TXT en el dominio del correo del usuario con la URL de AVD |
