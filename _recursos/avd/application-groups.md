---
title: "Application Groups"
indice: avd
resumen: "Qué escritorios y aplicaciones ve cada usuario."
estado: documentado   # proximamente | en-curso | documentado
orden: 3
last_review: 2026-10-20
fuentes:
  - titulo: "Azure Virtual Desktop terminology (application groups)"
    url: https://learn.microsoft.com/azure/virtual-desktop/terminology#application-groups
  - titulo: "Preferred application group type behavior for pooled host pools"
    url: https://learn.microsoft.com/azure/virtual-desktop/preferred-application-group-type
  - titulo: "Create an application group, a workspace, and assign users"
    url: https://learn.microsoft.com/azure/virtual-desktop/create-application-group-workspace
  - titulo: "Publish applications with RemoteApp"
    url: https://learn.microsoft.com/azure/virtual-desktop/publish-applications-stream-remoteapp
  - titulo: "Add and manage App Attach applications"
    url: https://learn.microsoft.com/azure/virtual-desktop/app-attach-setup
  - titulo: "Built-in Azure RBAC roles for Azure Virtual Desktop"
    url: https://learn.microsoft.com/azure/virtual-desktop/rbac
  - titulo: "Azure Virtual Desktop FAQ (permisos y ubicación)"
    url: https://learn.microsoft.com/azure/virtual-desktop/faq
  - titulo: "Licensing Azure Virtual Desktop (per-user access pricing)"
    url: https://learn.microsoft.com/azure/virtual-desktop/licensing
  - titulo: "Azure Virtual Desktop service limits"
    url: https://learn.microsoft.com/azure/azure-resource-manager/management/azure-subscription-service-limits#azure-virtual-desktop-service-limits
  - titulo: "Supported logs for Microsoft.DesktopVirtualization/applicationgroups"
    url: https://learn.microsoft.com/azure/azure-monitor/reference/supported-logs/microsoft-desktopvirtualization-applicationgroups-logs
  - titulo: "Microsoft.DesktopVirtualization applicationGroups (plantillas ARM/Bicep)"
    url: https://learn.microsoft.com/azure/templates/microsoft.desktopvirtualization/applicationgroups
  - titulo: "Microsoft.DesktopVirtualization applicationGroups/applications (plantillas ARM/Bicep)"
    url: https://learn.microsoft.com/azure/templates/microsoft.desktopvirtualization/applicationgroups/applications
  - titulo: "azurerm_virtual_desktop_application_group"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/virtual_desktop_application_group
  - titulo: "azurerm_virtual_desktop_application"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/virtual_desktop_application
  - titulo: "azurerm_virtual_desktop_workspace_application_group_association"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/virtual_desktop_workspace_application_group_association
  - titulo: "Submódulo Terraform VDI/modules/virtual_desktop_application_group"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/AzureVirtualDesktop/VDI/modules/virtual_desktop_application_group
  - titulo: "Submódulo Terraform VDI/modules/virtual_desktop_application"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/AzureVirtualDesktop/VDI/modules/virtual_desktop_application
  - titulo: "Submódulo Terraform VDI/modules/virtual_desktop_workspace_application_group_association"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/AzureVirtualDesktop/VDI/modules/virtual_desktop_workspace_application_group_association
  - titulo: "Módulo Terraform AzureVirtualDesktop/ApplicationGroup"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/AzureVirtualDesktop/ApplicationGroup
---

Un **application group** decide **qué ve cada usuario** de un [host pool](/recursos/avd/host-pools/): el escritorio completo o solo unas aplicaciones concretas. Es también **el punto donde se da el acceso**: a los usuarios no se les asignan VMs ni host pools, sino application groups, con el rol *Desktop Virtualization User*. Para que aparezca en Windows App, el application group se registra en un workspace.

## Qué es y cuándo usarlo

### Los dos tipos

| | **Desktop** | **RemoteApp** |
|---|---|---|
| Qué ve el usuario | El escritorio completo de Windows | Solo las aplicaciones publicadas, en ventanas integradas en su equipo |
| Host pools | Pooled y Personal | **Solo Pooled** |
| Cuántos por host pool | **Uno** | Varios |
| Si el usuario está en varios | — | Ve la suma de las aplicaciones de todos los grupos del mismo host pool |
| *Per-user access pricing* (usuarios externos) | Tramo *Desktops + apps* | Tramo *Apps* (más barato) |
| Cuándo | Puesto de trabajo completo | Una aplicación de negocio, acceso de terceros, convivencia con el PC local |

### Desktop y RemoteApp en el mismo host pool

Un host pool pooled puede tener a la vez su grupo Desktop y varios RemoteApp. Si un usuario está asignado a los dos tipos **en el mismo host pool**, solo ve lo que marca el *preferred application group type* del host pool. Así se evita que abra dos sesiones en el mismo pool, lo que provoca sesiones en negro, bloqueos al iniciar sesión y hosts sobrecargados.

| Grupos del host pool | El usuario está en | Tipo preferido | Ve |
|---|---|---|---|
| Desktop y RemoteApp | Solo Desktop | Cualquiera | Escritorio |
| Desktop y RemoteApp | Solo RemoteApp | Cualquiera | Aplicaciones |
| Desktop y RemoteApp | Ambos | Desktop | Escritorio |
| Desktop y RemoteApp | Ambos | RemoteApp | Aplicaciones |
| Desktop y RemoteApp | Ambos | Sin definir | Escritorio |

Para dar a la misma persona escritorio **y** aplicaciones a la vez, tienen que venir de **host pools distintos**.

### Cómo se publican aplicaciones RemoteApp

| Origen | Cómo | Observaciones |
|---|---|---|
| Menú Inicio de los session hosts | Se elige del menú Inicio (portal o `Get-AzWvdStartMenuItem`) | Necesita al menos un session host encendido |
| **Ruta de archivo** (la que uso en IaC) | Ruta local del `.exe` en los session hosts | La aplicación tiene que estar en la imagen, en la misma ruta en todos los hosts |
| Aplicaciones de Microsoft Store | Ruta `shell:AppsFolder\<PackageFamilyName>!<AppId>` | La ruta del `.exe` cambia con cada versión; el icono hay que dejarlo en una ruta fija |
| **App Attach** (MSIX/Appx) | Paquete asignado al host pool y aplicación de tipo `MsixApplication` | La aplicación no va en la imagen; en Terraform no lo soporta azurerm |

La política de argumentos de línea de comandos (`DoNotAllow`, `Allow`, `Require`) controla si el cliente puede pasar parámetros. Por defecto, `DoNotAllow`.

### Límites que conviene tener a mano

| Límite | Valor |
|---|---|
| Application groups por tenant de Entra ID | 1.000 (ampliable por soporte) |
| Aplicaciones RemoteApp por application group | 500 |
| Asignaciones de rol por objeto de AVD | 200 (por eso, grupos y no usuarios) |
| Application group Desktop por host pool | 1 |
| Nombre del application group | 3 a 64 caracteres |
| Nombre de una aplicación | 3 a 24 caracteres |
| Ubicación | La misma que el host pool y el workspace |

### Qué escenario recomiendo

| Escenario del cliente | Diseño | Por qué |
|---|---|---|
| Puesto completo para la plantilla | Un grupo Desktop por host pool, asignado a un grupo de Entra ID | Lo más simple de operar |
| Una aplicación de negocio para todos y escritorio solo para algunos | Host pool pooled con Desktop + RemoteApp y grupos de usuarios **distintos** | Cada colectivo ve lo suyo sin solaparse |
| Acceso de proveedores o terceros | RemoteApp con las aplicaciones mínimas y redirecciones restringidas | Menos superficie expuesta |
| Aplicación SaaS para clientes externos | RemoteApp con *per-user access pricing* | Tramo *Apps*, más barato que *Desktops + apps* |
| Muchas aplicaciones con ciclos de vida distintos | RemoteApp con App Attach | Las aplicaciones se actualizan sin rehacer la imagen |

### Datos que conviene llevar a la reunión

- **El acceso se da al application group, no a la VM**: con el rol *Desktop Virtualization User* y siempre a grupos de Entra ID. Con session hosts unidos a Entra ID hace falta además *Virtual Machine User Login*.
- **RemoteApp solo funciona con host pools pooled.**
- **Un usuario con escritorio y aplicaciones del mismo host pool solo ve uno de los dos**: si necesita ambos, van en host pools distintos.
- **Un application group que no está registrado en un workspace no aparece** en Windows App, aunque el usuario tenga el rol.
- **Con usuarios externos, el tipo de grupo cambia el precio**: solo RemoteApp entra en el tramo *Apps*.
- **Los usuarios tienen que estar en el mismo tenant de Entra ID** que el host pool, el workspace y el application group.

## Decisiones de diseño

| Decisión | Lo que aplico | Por qué |
|---|---|---|
| Acceso | *Desktop Virtualization User* sobre el application group, solo a grupos de Entra ID | Límite de 200 asignaciones por objeto y alta/baja desde Entra ID |
| Separación | Grupos de usuarios distintos para Desktop y RemoteApp del mismo host pool | Evita el conflicto del tipo preferido |
| Tipo preferido | Fijado siempre en el host pool | Comportamiento predecible del feed |
| Publicación | Aplicaciones por ruta de archivo desde IaC, instaladas en la imagen; App Attach para las que cambian a menudo | Configuración reproducible |
| Argumentos | `DoNotAllow` salvo necesidad concreta | El cliente no puede alterar cómo arranca la aplicación |
| Nombre visible | `default_desktop_display_name` y `friendly_name` con nombres de negocio | El usuario no ve "SessionDesktop" ni el nombre técnico |
| Workspace | Registro del grupo en el workspace desde IaC | Sin registro no hay feed |
| Ubicación | Misma región que host pool y workspace | Requisito del servicio |
| Observabilidad | *Diagnostic settings* Checkpoint, Error y Management a Log Analytics | Auditoría de cambios y errores |
| Permisos de administración | *User Access Administrator* (o rol personalizado) acotado a los application groups para quien gestiona accesos | Asignar usuarios exige escribir asignaciones de rol |

Alineación con el Well-Architected Framework:

- **Seguridad**: mínimo privilegio por grupo y RemoteApp para exponer solo lo necesario.
- **Fiabilidad**: aplicaciones en la imagen o con App Attach, sin depender de instalaciones manuales en cada host.
- **Coste**: RemoteApp donde baste con aplicaciones; con usuarios externos reduce el tramo de precio.
- **Excelencia operativa**: grupos, aplicaciones y asignaciones en IaC.
- **Rendimiento**: sin sesiones duplicadas en el mismo pool gracias al tipo preferido.

## Módulo de Terraform

### Los módulos del repositorio

| Pieza | Módulo | Estado |
|---|---|---|
| Application group | [`AzureVirtualDesktop/VDI/modules/virtual_desktop_application_group`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/AzureVirtualDesktop/VDI/modules/virtual_desktop_application_group) | Utilizable (recomendado) |
| Aplicación RemoteApp | [`AzureVirtualDesktop/VDI/modules/virtual_desktop_application`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/AzureVirtualDesktop/VDI/modules/virtual_desktop_application) | Utilizable |
| Registro en el workspace | [`AzureVirtualDesktop/VDI/modules/virtual_desktop_workspace_application_group_association`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/AzureVirtualDesktop/VDI/modules/virtual_desktop_workspace_application_group_association) | Utilizable |
| Application group (independiente) | [`AzureVirtualDesktop/ApplicationGroup`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/AzureVirtualDesktop/ApplicationGroup) | Utilizable con condiciones |

Los tres submódulos de `VDI` son finos, sin `locals`, y validan los tipos. Ninguno cubre la asignación de usuarios ni los *diagnostic settings*, así que van como recursos nativos.

`AzureVirtualDesktop/ApplicationGroup` usa `locals` y `count`. Solo crea el grupo: no publica aplicaciones, no lo registra en el workspace y no asigna usuarios.

`azurerm_virtual_desktop_application` no tiene argumento para el tipo de aplicación, así que no publica aplicaciones de App Attach (`MsixApplication`). Para eso hay que usar Bicep o azapi.

### Estructura en el proyecto

```txt
/
├── providers.tf
├── host_pools.tf           # ficha Host Pools (module.host_pool)
├── session_hosts.tf        # ficha Session Hosts
├── application_groups.tf   # application groups, aplicaciones, accesos y registro en el workspace
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

### Application groups · `application_groups.tf`

```hcl
# =============================================================================
# Application groups, aplicaciones RemoteApp, asignación de usuarios y registro en el workspace
# Submódulos de AzureVirtualDesktop/VDI/modules
# DEPENDENCY: host_pools.tf de la ficha Host Pools en el mismo root (module.host_pool)
# DEPENDENCY: Workspace existente (ficha Workspaces) en la misma región que el host pool
# DEPENDENCY: Grupos de seguridad de Entra ID para los usuarios (mismo tenant que los recursos de AVD)
# DEPENDENCY: Para RemoteApp, las aplicaciones instaladas en la imagen de los session hosts
# =============================================================================

variable "application_groups" {
  description = "Application groups (clave = nombre del application group)."
  type = map(object({
    host_pool           = string # clave de var.host_pools
    resource_group_name = string
    location            = string # la misma región que el host pool y el workspace
    type                = string # Desktop | RemoteApp
    friendly_name       = optional(string)
    description         = optional(string)

    # Solo Desktop: nombre del escritorio en el cliente (obligatorio para conectar desde el portal de Windows 365)
    default_desktop_display_name = optional(string)

    workspace_id = optional(string) # registro en el workspace; sin él, el grupo no aparece en el feed

    # Grupos de Entra ID con el rol Desktop Virtualization User sobre el application group
    user_group_object_ids = optional(map(string), {})

    # Solo RemoteApp (clave = nombre de la aplicación, máximo 24 caracteres)
    applications = optional(map(object({
      friendly_name                = string
      path                         = string # ruta local del .exe o shell:AppsFolder\<PackageFamilyName>!<AppId>
      description                  = optional(string)
      command_line_argument_policy = optional(string, "DoNotAllow") # DoNotAllow | Allow | Require
      command_line_arguments       = optional(string)
      icon_path                    = optional(string) # ruta local en los session hosts
      icon_index                   = optional(number, 0)
      show_in_portal               = optional(bool)
    })), {})

    log_analytics_workspace_id = string
    tags                       = optional(map(string), {})
  }))

  validation {
    condition     = alltrue([for k, v in var.application_groups : contains(["Desktop", "RemoteApp"], v.type)])
    error_message = "type debe ser Desktop o RemoteApp."
  }

  validation {
    condition     = alltrue([for k, v in var.application_groups : v.type == "RemoteApp" || length(v.applications) == 0])
    error_message = "Solo los application groups RemoteApp publican aplicaciones."
  }

  validation {
    condition     = alltrue(flatten([for k, v in var.application_groups : [for ak, a in v.applications : length(ak) <= 24]]))
    error_message = "El nombre de una aplicación admite como máximo 24 caracteres."
  }

  validation {
    condition = alltrue(flatten([
      for k, v in var.application_groups : [
        for ak, a in v.applications : contains(["DoNotAllow", "Allow", "Require"], a.command_line_argument_policy)
      ]
    ]))
    error_message = "command_line_argument_policy debe ser DoNotAllow, Allow o Require."
  }

  validation {
    # Un único application group Desktop por host pool
    condition = alltrue([
      for hp in distinct([for k, v in var.application_groups : v.host_pool]) :
      length([for k, v in var.application_groups : k if v.host_pool == hp && v.type == "Desktop"]) <= 1
    ])
    error_message = "Un host pool solo admite un application group de tipo Desktop."
  }
}

module "application_group" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//AzureVirtualDesktop/VDI/modules/virtual_desktop_application_group?ref=main"
  for_each = var.application_groups

  virtual_desktop_application_group_name = each.key
  resource_group_name                    = each.value.resource_group_name
  location                               = each.value.location
  type                                   = each.value.type
  host_pool_id                           = module.host_pool[each.value.host_pool].id
  friendly_name                          = each.value.friendly_name
  description                            = each.value.description
  default_desktop_display_name           = each.value.type == "Desktop" ? each.value.default_desktop_display_name : null

  tags = merge(var.tags, each.value.tags)
}

module "application" {
  source = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//AzureVirtualDesktop/VDI/modules/virtual_desktop_application?ref=main"
  for_each = {
    for item in flatten([
      for gk, g in var.application_groups : [
        for ak, a in g.applications : {
          key   = "${gk}/${ak}"
          group = gk
          name  = ak
          app   = a
        }
      ]
    ]) : item.key => item
  }

  virtual_desktop_application_name = each.value.name
  application_group_id             = module.application_group[each.value.group].id
  friendly_name                    = each.value.app.friendly_name
  description                      = each.value.app.description
  path                             = each.value.app.path
  command_line_argument_policy     = each.value.app.command_line_argument_policy
  command_line_arguments           = each.value.app.command_line_arguments
  icon_path                        = each.value.app.icon_path
  icon_index                       = each.value.app.icon_index
  show_in_portal                   = each.value.app.show_in_portal
}

module "workspace_association" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//AzureVirtualDesktop/VDI/modules/virtual_desktop_workspace_application_group_association?ref=main"
  for_each = { for k, v in var.application_groups : k => v if v.workspace_id != null }

  workspace_id         = each.value.workspace_id
  application_group_id = module.application_group[each.key].id
}

# Acceso de los usuarios: rol Desktop Virtualization User sobre el application group
resource "azurerm_role_assignment" "avd_user" {
  for_each = {
    for item in flatten([
      for gk, g in var.application_groups : [
        for uk, oid in g.user_group_object_ids : {
          key          = "${gk}/${uk}"
          group        = gk
          principal_id = oid
        }
      ]
    ]) : item.key => item
  }

  scope                = module.application_group[each.value.group].id
  role_definition_name = "Desktop Virtualization User"
  principal_id         = each.value.principal_id
  principal_type       = "Group"
}

resource "azurerm_monitor_diagnostic_setting" "application_group" {
  for_each                   = var.application_groups
  name                       = "diag-${each.key}"
  target_resource_id         = module.application_group[each.key].id
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

  lifecycle {
    # RemoteApp solo existe en host pools Pooled (la validación cruza dos variables)
    precondition {
      condition     = each.value.type == "Desktop" || var.host_pools[each.value.host_pool].type == "Pooled"
      error_message = "Los application groups RemoteApp solo se pueden asignar a host pools Pooled."
    }
  }
}

output "application_group_ids" {
  description = "IDs de los application groups (los usa la ficha Workspaces)."
  value       = { for k, m in module.application_group : k => m.id }
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

application_groups = {
  # Escritorio completo del host pool pooled
  "vdag-<workload>-pro-desktop" = {
    host_pool                    = "vdpool-<workload>-pro-01"
    resource_group_name          = "<rg-avd-pro>"
    location                     = "<region>"
    type                         = "Desktop"
    friendly_name                = "Escritorio corporativo"
    default_desktop_display_name = "Escritorio corporativo"
    workspace_id                 = "<resourceId vdws-<workload>-pro>"
    user_group_object_ids = {
      oficina = "<objectId grupo AVD-Escritorio>"
    }
    log_analytics_workspace_id = "<resourceId log-analytics-workspace>"
  }

  # Aplicaciones publicadas del mismo host pool para otro colectivo
  "vdag-<workload>-pro-finanzas" = {
    host_pool           = "vdpool-<workload>-pro-01"
    resource_group_name = "<rg-avd-pro>"
    location            = "<region>"
    type                = "RemoteApp"
    friendly_name       = "Aplicaciones de Finanzas"
    workspace_id        = "<resourceId vdws-<workload>-pro>"
    user_group_object_ids = {
      finanzas = "<objectId grupo AVD-Finanzas>"
    }
    applications = {
      excel = {
        friendly_name = "Excel"
        path          = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
        icon_path     = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
      }
      erp-cliente = {
        friendly_name = "ERP"
        path          = "C:\\Program Files\\<ERP>\\<erp>.exe"
        icon_path     = "C:\\Program Files\\<ERP>\\<erp>.exe"
      }
    }
    log_analytics_workspace_id = "<resourceId log-analytics-workspace>"
  }

  # Escritorio del host pool personal
  "vdag-<workload>-pro-dev-desktop" = {
    host_pool                    = "vdpool-<workload>-pro-dev01"
    resource_group_name          = "<rg-avd-pro>"
    location                     = "<region>"
    type                         = "Desktop"
    friendly_name                = "Puesto de desarrollo"
    default_desktop_display_name = "Puesto de desarrollo"
    workspace_id                 = "<resourceId vdws-<workload>-pro>"
    user_group_object_ids = {
      desarrollo = "<objectId grupo AVD-Desarrollo>"
    }
    log_analytics_workspace_id = "<resourceId log-analytics-workspace>"
  }
}
```

En `dev.tfvars` y `pre.tfvars`, mismo esquema con los grupos de usuarios de pruebas de cada entorno.

Despliegue y comprobación:

```powershell
terraform init
terraform plan -var-file="env/pro.tfvars" -out="pro.tfplan"
terraform apply "pro.tfplan"

# Aplicaciones publicadas y asignaciones del grupo
Get-AzWvdApplication -GroupName "vdag-<workload>-pro-finanzas" -ResourceGroupName "<rg-avd-pro>" |
    Select-Object Name, FriendlyName, FilePath
Get-AzRoleAssignment -Scope (Get-AzWvdApplicationGroup -Name "vdag-<workload>-pro-finanzas" -ResourceGroupName "<rg-avd-pro>").Id |
    Select-Object DisplayName, RoleDefinitionName
```

### Equivalente en Bicep

`main.bicep` (el registro en el workspace se hace desde el propio workspace, en su ficha):

```bicep
// =============================================================================
// Application groups de un host pool: Desktop y/o RemoteApp, aplicaciones,
// asignación de grupos de usuarios y diagnósticos
// DEPENDENCY: Resource Group existente (targetScope = resourceGroup)
// DEPENDENCY: Host pool existente en la misma región (RemoteApp solo con Pooled)
// DEPENDENCY: Log Analytics workspace existente
// DEPENDENCY: El registro en el workspace (applicationGroupReferences) se hace en la ficha Workspaces
// =============================================================================
targetScope = 'resourceGroup'

param location string = resourceGroup().location

param hostPoolName string
param hostPoolResourceGroupName string = resourceGroup().name

param logAnalyticsWorkspaceId string

@description('Application groups del host pool. applications solo en RemoteApp (nombre de 24 caracteres como máximo).')
param applicationGroups array = [
  {
    name: 'vdag-workload-pro-desktop'
    type: 'Desktop'
    friendlyName: 'Escritorio corporativo'
    description: ''
    userGroupObjectIds: []
    applications: []
  }
]

param tags object = {}

// Desktop Virtualization User (rol integrado)
var desktopVirtualizationUserRoleId = '1d18fff3-a72a-46b5-b4a9-0b38a3cd7e63'

var userAssignments = flatten(map(applicationGroups, (g, i) => map(g.userGroupObjectIds, oid => {
  groupIndex: i
  principalId: oid
})))

var applications = flatten(map(applicationGroups, (g, i) => map(g.applications, app => union(app, {
  groupIndex: i
}))))

resource hostPool 'Microsoft.DesktopVirtualization/hostPools@2025-10-10' existing = {
  name: hostPoolName
  scope: resourceGroup(hostPoolResourceGroupName)
}

resource appGroups 'Microsoft.DesktopVirtualization/applicationGroups@2025-10-10' = [
  for g in applicationGroups: {
    name: g.name
    location: location
    tags: tags
    properties: {
      applicationGroupType: g.type
      hostPoolArmPath: hostPool.id
      friendlyName: g.friendlyName
      description: empty(g.description) ? null : g.description
    }
  }
]

resource apps 'Microsoft.DesktopVirtualization/applicationGroups/applications@2025-10-10' = [
  for app in applications: {
    parent: appGroups[app.groupIndex]
    name: app.name
    properties: {
      applicationType: 'InBuilt'
      friendlyName: app.friendlyName
      filePath: app.filePath
      iconPath: app.?iconPath ?? app.filePath
      iconIndex: app.?iconIndex ?? 0
      commandLineSetting: app.?commandLineSetting ?? 'DoNotAllow'
      commandLineArguments: app.?commandLineArguments
      showInPortal: true
    }
  }
]

resource userAccess 'Microsoft.Authorization/roleAssignments@2022-04-01' = [
  for a in userAssignments: {
    name: guid(appGroups[a.groupIndex].id, a.principalId, desktopVirtualizationUserRoleId)
    scope: appGroups[a.groupIndex]
    properties: {
      principalId: a.principalId
      principalType: 'Group'
      roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', desktopVirtualizationUserRoleId)
    }
  }
]

resource diagnostics 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = [
  for (g, i) in applicationGroups: {
    name: 'diag-${g.name}'
    scope: appGroups[i]
    properties: {
      workspaceId: logAnalyticsWorkspaceId
      logs: [
        { category: 'Checkpoint', enabled: true }
        { category: 'Error', enabled: true }
        { category: 'Management', enabled: true }
      ]
    }
  }
]

output applicationGroupIds array = [for (g, i) in applicationGroups: appGroups[i].id]
```

`main.pro.bicepparam`:

```bicep
using 'main.bicep'

param hostPoolName = 'vdpool-<workload>-pro-01'
param hostPoolResourceGroupName = '<rg-avd-pro>'
param logAnalyticsWorkspaceId = '<resourceId log-analytics-workspace>'

param applicationGroups = [
  {
    name: 'vdag-<workload>-pro-desktop'
    type: 'Desktop'
    friendlyName: 'Escritorio corporativo'
    description: ''
    userGroupObjectIds: [
      '<objectId grupo AVD-Escritorio>'
    ]
    applications: []
  }
  {
    name: 'vdag-<workload>-pro-finanzas'
    type: 'RemoteApp'
    friendlyName: 'Aplicaciones de Finanzas'
    description: ''
    userGroupObjectIds: [
      '<objectId grupo AVD-Finanzas>'
    ]
    applications: [
      {
        name: 'excel'
        friendlyName: 'Excel'
        filePath: 'C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE'
      }
      {
        name: 'erp-cliente'
        friendlyName: 'ERP'
        filePath: 'C:\\Program Files\\<ERP>\\<erp>.exe'
      }
    ]
  }
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
az deployment group what-if --resource-group <rg-avd-pro> --parameters main.pro.bicepparam
az deployment group create  --resource-group <rg-avd-pro> --parameters main.pro.bicepparam
```

## Errores típicos

| Síntoma | Causa | Solución |
|---|---|---|
| El usuario no ve nada en Windows App | El application group no está registrado en ningún workspace | Asociarlo al workspace |
| El usuario no ve nada aunque el grupo esté en el workspace | No tiene *Desktop Virtualization User* sobre el application group | Asignar el rol a su grupo de Entra ID |
| El usuario ve el escritorio pero no las aplicaciones (o al revés) | Está en Desktop y RemoteApp del mismo host pool y manda el tipo preferido | Separar colectivos o mover uno de los grupos a otro host pool |
| Error al crear un segundo application group Desktop | Solo se admite uno por host pool | Usar el existente o crear otro host pool |
| Error al crear un RemoteApp sobre un host pool personal | RemoteApp solo existe en pooled | Usar Desktop o un host pool pooled |
| Error de ubicación al crear el grupo o asociarlo al workspace | Grupo, host pool y workspace en regiones distintas | Misma región para los tres |
| En el portal no aparece la lista del menú Inicio | No hay ningún session host encendido | Encender al menos uno o publicar por ruta de archivo |
| La aplicación de Microsoft Store deja de abrir tras actualizarse | Se publicó con la ruta del `.exe`, que incluye la versión | Publicar con `shell:AppsFolder\<PackageFamilyName>!<AppId>` |
| La aplicación abre con el icono genérico | `icon_path` apunta a una ruta que no existe en los hosts | Ruta local fija en la imagen |
| La aplicación no arranca en algunos hosts | No está instalada en todos o no en la misma ruta | Incluirla en la imagen dorada y redesplegar |
| Error de validación al crear la aplicación | Nombre de más de 24 caracteres | Nombre corto; el visible va en `friendly_name` |
| Error al asignar usuarios desde IaC | La identidad del pipeline no puede escribir asignaciones de rol | *User Access Administrator* (o rol con `roleAssignments/write`) acotado al RG |
| La conexión desde el portal de Windows 365 se queda en "Loading Client" | Falta `default_desktop_display_name` en el grupo Desktop | Informarlo |
| No hay forma de publicar una aplicación App Attach con Terraform | `azurerm_virtual_desktop_application` no admite `MsixApplication` | Publicarla con Bicep o azapi |
