---
title: "Host Pools"
indice: avd
resumen: "El conjunto de máquinas que sirven los escritorios."
estado: documentado   # proximamente | en-curso | documentado
orden: 1
last_review: 2026-10-20
fuentes:
  - titulo: "Azure Virtual Desktop terminology"
    url: https://learn.microsoft.com/azure/virtual-desktop/terminology
  - titulo: "Host pool management approaches"
    url: https://learn.microsoft.com/azure/virtual-desktop/host-pool-management-approaches
  - titulo: "Host pool load balancing algorithms"
    url: https://learn.microsoft.com/azure/virtual-desktop/host-pool-load-balancing
  - titulo: "Preferred application group type behavior"
    url: https://learn.microsoft.com/azure/virtual-desktop/preferred-application-group-type
  - titulo: "Configure a validation environment"
    url: https://learn.microsoft.com/azure/virtual-desktop/configure-validation-environment
  - titulo: "Deploy Azure Virtual Desktop"
    url: https://learn.microsoft.com/azure/virtual-desktop/deploy-azure-virtual-desktop
  - titulo: "Add session hosts to a host pool"
    url: https://learn.microsoft.com/azure/virtual-desktop/add-session-hosts-host-pool
  - titulo: "Azure Private Link with Azure Virtual Desktop"
    url: https://learn.microsoft.com/azure/virtual-desktop/private-link-overview
  - titulo: "Set up Private Link with Azure Virtual Desktop"
    url: https://learn.microsoft.com/azure/virtual-desktop/private-link-setup
  - titulo: "Configure Start VM on Connect"
    url: https://learn.microsoft.com/azure/virtual-desktop/start-virtual-machine-connect
  - titulo: "Assign Azure RBAC roles to the Azure Virtual Desktop service principals"
    url: https://learn.microsoft.com/azure/virtual-desktop/service-principal-assign-roles
  - titulo: "Built-in Azure RBAC roles for Azure Virtual Desktop"
    url: https://learn.microsoft.com/azure/virtual-desktop/rbac
  - titulo: "Configure single sign-on using Microsoft Entra ID"
    url: https://learn.microsoft.com/azure/virtual-desktop/configure-single-sign-on
  - titulo: "Supported RDP properties"
    url: https://learn.microsoft.com/azure/virtual-desktop/rdp-properties
  - titulo: "Send diagnostic data to Log Analytics"
    url: https://learn.microsoft.com/azure/virtual-desktop/diagnostics-log-analytics
  - titulo: "Supported logs for Microsoft.DesktopVirtualization/hostpools"
    url: https://learn.microsoft.com/azure/azure-monitor/reference/supported-logs/microsoft-desktopvirtualization-hostpools-logs
  - titulo: "Licensing Azure Virtual Desktop"
    url: https://learn.microsoft.com/azure/virtual-desktop/licensing
  - titulo: "Azure Virtual Desktop service limits"
    url: https://learn.microsoft.com/azure/azure-resource-manager/management/azure-subscription-service-limits#azure-virtual-desktop-service-limits
  - titulo: "Troubleshoot common Azure Virtual Desktop Agent issues"
    url: https://learn.microsoft.com/troubleshoot/azure/virtual-desktop/troubleshoot-agent
  - titulo: "Microsoft.DesktopVirtualization hostPools (plantillas ARM/Bicep)"
    url: https://learn.microsoft.com/azure/templates/microsoft.desktopvirtualization/hostpools
  - titulo: "azurerm_virtual_desktop_host_pool"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/virtual_desktop_host_pool
  - titulo: "azurerm_virtual_desktop_host_pool_registration_info"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/virtual_desktop_host_pool_registration_info
  - titulo: "Azure Virtual Desktop pricing"
    url: https://azure.microsoft.com/pricing/details/virtual-desktop/
  - titulo: "Submódulo Terraform VDI/modules/virtual_desktop_host_pool"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/AzureVirtualDesktop/VDI/modules/virtual_desktop_host_pool
  - titulo: "Submódulo Terraform VDI/modules/virtual_desktop_host_pool_registration_info"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/AzureVirtualDesktop/VDI/modules/virtual_desktop_host_pool_registration_info
  - titulo: "Módulo Terraform AzureVirtualDesktop/HostPool"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/AzureVirtualDesktop/HostPool
---

Un **host pool** es la agrupación lógica de máquinas virtuales registradas en Azure Virtual Desktop como *session hosts*. Todas deberían salir de la misma imagen y tener la misma configuración, porque el servicio reparte a los usuarios entre ellas sin distinguirlas. El host pool decide **cómo se reparten las sesiones** (pooled o personal, y con qué algoritmo), **por qué red llegan** (pública o Private Link) y **qué experiencia RDP tienen los usuarios**. No cuesta nada por sí mismo: se paga por las VMs, los discos, la red y las licencias.

## Qué es y cuándo usarlo

### Cuándo sí

- Escritorios o aplicaciones Windows publicados para empleados que trabajan en remoto o desde dispositivos no gestionados.
- Sustituir una granja RDS on-premises o un VDI de terceros.
- Aplicaciones heredadas que necesitan estar cerca de sus datos en Azure.
- Puestos de desarrollo o de alto rendimiento (GPU) con acceso controlado.
- Proveedores y contratistas que no deben tener los datos en su equipo.

### Cuándo no

| Si el caso es… | Mejor opción | Motivo |
|---|---|---|
| Un PC en la nube por usuario, con precio fijo y gestión desde Intune sin infraestructura | Windows 365 | No hay host pools, red ni imágenes que mantener |
| Administración puntual de servidores por RDP | Azure Bastion | AVD está pensado para usuarios finales, no para administradores |
| Aplicaciones web o SaaS | Acceso directo con Entra ID y Conditional Access | Un escritorio intermedio solo añade coste y latencia |
| Ofrecer una aplicación a clientes externos (SaaS) | AVD con *per-user access pricing* | Las licencias de Microsoft 365 o Windows no cubren usos comerciales externos |

### Tipos de host pool

| | **Pooled** (recomendado por defecto) | **Personal** |
|---|---|---|
| Usuarios por VM | Varios a la vez (Windows 11 Enterprise multi-session o Windows Server) | Uno; la VM queda asignada al usuario |
| Reparto | BreadthFirst o DepthFirst según sesiones | Siempre a su VM asignada (Persistent) |
| Perfil de usuario | FSLogix obligatorio (el usuario cambia de VM) | En el disco de la VM |
| Actualización | Redesplegando desde una imagen nueva | Windows Update, Intune o Configuration Manager |
| Escalado | Autoscale enciende y apaga por umbral de capacidad y horario | Autoscale arranca con Start VM on Connect y apaga o hiberna al desconectar |
| Coste por usuario | Bajo: se comparten CPU y memoria | Alto: una VM por usuario |
| Cuándo | Trabajadores de oficina, call centers, aplicaciones publicadas | Desarrolladores, administradores con software propio, aplicaciones que no soportan multisesión |

En Personal la asignación puede ser **Automatic** (el servicio da una VM libre al primer acceso) o **Direct** (el administrador elige la VM). Con Direct se pueden asignar varios escritorios a un mismo usuario.

### Algoritmo de reparto (solo Pooled)

| Algoritmo | Cómo funciona | Cuándo |
|---|---|---|
| **BreadthFirst** (recomendado) | Elige al azar entre la mitad de los hosts con menos sesiones | Mejor experiencia de usuario; reparte la carga desde el principio |
| **DepthFirst** | Llena un host hasta el límite de sesiones antes de pasar al siguiente | Ahorro con Autoscale o Start VM on Connect; requiere fijar el límite |

El **límite de sesiones** (`maximum_sessions_allowed`) va de 0 a 999999. Con DepthFirst hay que fijarlo con datos de las pruebas de carga, porque el valor por defecto (999999) llenaría un único host. Con muchas conexiones simultáneas el servicio puede superarlo puntualmente.

### Modelos de gestión

| Modelo | Qué hace Azure | Limitaciones |
|---|---|---|
| **Standard** (el habitual con IaC) | Nada: tú creas, registras, actualizas y escalas los session hosts con tus pipelines | Tú garantizas que todos los hosts sean iguales |
| **Session host configuration** | Crea los hosts desde una configuración (imagen, tamaño, red, dominio), los actualiza por lotes con *session host update* y Autoscale puede crearlos y borrarlos | Solo Pooled; no admite herramientas externas de alta de hosts ni tokens de registro; no soportado en Azure Local |

**El modelo se elige al crear el host pool y no se puede cambiar.** En azurerm 4.x no encontré recurso para la *session host configuration*; si el cliente la quiere con Terraform hay que usar azapi.

### Acceso de red (`public_network_access`)

Cada conexión tiene dos lados (cliente → gateway y session host → gateway) y el host pool controla los dos:

| Valor | Resultado |
|---|---|
| `Enabled` | Clientes y session hosts por ruta pública o privada |
| `Disabled` (recomendado con Private Link) | Solo se permite la sesión si cliente y session host usan rutas privadas |
| `EnabledForClientsOnly` / `EnabledForSessionHostsOnly` | Un lado público y el otro privado (ver aviso) |

> Aviso: Learn se contradice en los valores intermedios. La guía de Private Link asocia "público para usuarios, privado para session hosts" a `EnabledForSessionHostsOnly`, mientras que la referencia del SDK describe ese valor como "permite acceso público a los session hosts". Si se usa uno de estos dos valores, hay que comprobar en el portal (Host pool → Networking → Public access) qué opción ha quedado marcada.

Private Link en AVD tiene tres subrecursos: `connection` en el host pool (uno por host pool), `feed` en el workspace y `global` (uno solo para todo el despliegue, en un workspace vacío dedicado). Los dos primeros usan la zona `privatelink.wvd.microsoft.com`; `global`, `privatelink-global.wvd.microsoft.com`. Esta ficha cubre `connection`; `feed` y `global` van en la ficha de Workspaces.

### Licencias

| Sistema operativo del host | Uso interno (empleados y contratistas) | Uso comercial externo |
|---|---|---|
| Windows 11/10 Enterprise y multi-session | Microsoft 365 E3, E5, A3, A5, F3, Business Premium; Windows Enterprise E3/E5; Windows VDA por usuario | *Per-user access pricing* en la suscripción |
| Windows Server 2016–2025 | RDS CAL con Software Assurance o RDS User Subscription | No soportado |

Con licencia válida no se paga la licencia de Windows de la VM: el servicio la aplica al crear los hosts. Si los hosts se crean por fuera (Terraform), hay que indicar `license_type = "Windows_Client"` en la VM. Las suscripciones Dev/Test permiten que los usuarios de pruebas se conecten sin licencia propia.

### Límites que conviene tener a mano

| Límite | Valor |
|---|---|
| Session hosts por host pool | 10.000 |
| Host pools por workspace | 400 |
| Application groups por tenant | 1.000 (ampliable por soporte) |
| Asignaciones de rol por objeto de AVD | 200 |
| Validez del token de registro | De 1 hora a 27 días |
| Ventanas de actualización programada del agente | Máximo 2, de 2 horas cada una |
| Nombre del host pool | 3 a 64 caracteres |
| Prefijo de nombre de VM | Prefijo + sufijo ≤ 15 caracteres (nombre NetBIOS) |

### Qué escenario recomiendo

| Escenario del cliente | Diseño | Por qué |
|---|---|---|
| Oficina estándar, Microsoft 365 | Pooled, Windows 11 multi-session, BreadthFirst, FSLogix, Autoscale | El menor coste por usuario con buena experiencia |
| Coste por encima de todo, horario fijo | Pooled, DepthFirst + Autoscale + Start VM on Connect | Concentra sesiones y apaga lo que sobra |
| Desarrolladores o software que no soporta multisesión | Personal, asignación Automatic, Start VM on Connect | VM dedicada, encendida solo cuando se usa |
| Requisito de no exponer nada a Internet | `public_network_access = "Disabled"` + PE `connection`, `feed` y `global` | Todo el tráfico de AVD por la red privada |
| Despliegue mediano o grande | Un host pool de validación además del productivo | Recibe antes las actualizaciones del servicio |
| Equipo sin IaC que quiere menos operación | Session host configuration (Pooled) | Azure crea y actualiza los hosts por lotes |

### Datos que conviene llevar a la reunión

- **El host pool es gratis**: el coste es VM + disco + red + licencias. El ahorro real está en el algoritmo, el límite de sesiones y el escalado.
- **No hay que abrir puertos de entrada**: los session hosts y los clientes salen hacia el servicio (*reverse connect*). Ni IP públicas ni 3389 abierto.
- **El tipo (Pooled/Personal) y el modelo de gestión no se cambian después**: un cambio implica host pool nuevo y migración de usuarios.
- **Las licencias de Microsoft 365 no sirven para clientes externos**: para un SaaS hace falta *per-user access pricing*.
- **Entra ID join + SSO** es hoy la opción más simple. Si siguen dependiendo de AD DS (recursos SMB, GPO), Entra hybrid join con objeto Kerberos en Entra ID.
- **Private Link en AVD exige re-registrar el resource provider** `Microsoft.DesktopVirtualization` en cada suscripción antes de crear los endpoints.

## Decisiones de diseño

| Decisión | Lo que aplico | Por qué |
|---|---|---|
| Tipo | Pooled salvo requisito claro de VM dedicada | Coste por usuario y operación por imágenes |
| Algoritmo | BreadthFirst; DepthFirst solo junto con Autoscale | Experiencia de usuario primero |
| Límite de sesiones | Fijado por pruebas de carga con el SKU real, nunca el valor por defecto | Con DepthFirst el valor por defecto concentra a todos en un host |
| Modelo de gestión | Standard con IaC; session host configuration si no hay pipelines | Decisión irreversible, se valida con el cliente |
| Identidad de los hosts | Entra ID join con SSO (`enablerdsaadauth:i:1`) y Conditional Access sobre *Windows Cloud Login* | Sin contraseña en la conexión y MFA centralizado |
| Red | `public_network_access = "Disabled"` + PE `connection` en `privatelink.wvd.microsoft.com` | Sesiones solo por ruta privada |
| Filtrado | NSG o Azure Firewall con la service tag `WindowsVirtualDesktop`; todo el rango TCP 1–65535 abierto hacia el PE `connection` | El servicio mapea puertos dinámicos sobre la IP del PE |
| Start VM on Connect | Activado, con *Desktop Virtualization Power On Contributor* en el alcance que contiene las VMs | Ahorro sin que el usuario dependa de un horario |
| Token de registro | Corto (días), rotado por IaC y nunca en el repositorio | Un token vigente permite registrar cualquier VM en el pool |
| Actualizaciones del agente | Programadas en una ventana fuera de horario | Evita reinicios del stack en horario laboral |
| Validación | Un host pool con `validate_environment = true` por cada imagen productiva | Detecta cambios del servicio antes de que lleguen a producción |
| Observabilidad | *Diagnostic settings* Checkpoint, Error, Management, Connection, HostRegistration y AgentHealthStatus a Log Analytics + AVD Insights | Son las categorías que pide Insights y no tienen coste de exportación |
| Ubicación | Host pool, application groups y workspace en la misma región; los metadatos se guardan en la geografía del host pool | Requisito del servicio y de residencia de datos |

Alineación con el Well-Architected Framework:

- **Seguridad**: sin puertos de entrada, Private Link, SSO con Conditional Access y tokens de registro de vida corta.
- **Fiabilidad**: host pool de validación, hosts en zonas de disponibilidad y perfiles FSLogix fuera de la VM.
- **Coste**: Pooled, Start VM on Connect, Autoscale y límite de sesiones medido.
- **Excelencia operativa**: imágenes versionadas, IaC y diagnósticos en Log Analytics.
- **Rendimiento**: SKU y límite de sesiones según pruebas de carga y RDP Shortpath (con Private Link requiere el *opt-in* de UDP).

## Módulo de Terraform

### Los módulos del repositorio

| Pieza | Módulo | Estado |
|---|---|---|
| Host pool | [`AzureVirtualDesktop/VDI/modules/virtual_desktop_host_pool`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/AzureVirtualDesktop/VDI/modules/virtual_desktop_host_pool) | Utilizable (recomendado) |
| Token de registro | [`AzureVirtualDesktop/VDI/modules/virtual_desktop_host_pool_registration_info`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/AzureVirtualDesktop/VDI/modules/virtual_desktop_host_pool_registration_info) | Utilizable |
| Host pool (independiente) | [`AzureVirtualDesktop/HostPool`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/AzureVirtualDesktop/HostPool) | Utilizable con condiciones |
| Pila completa | [`AzureVirtualDesktop/VDI`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/AzureVirtualDesktop/VDI) | Utilizable con condiciones |

El submódulo `virtual_desktop_host_pool` es el que uso en la ficha. Expone `public_network_access`, `vm_template`, las actualizaciones programadas del agente y los *timeouts*. Además valida con `precondition` las combinaciones imposibles:

- Personal exige `personal_desktop_assignment_type` y el algoritmo Persistent.
- Pooled no admite Persistent.
- Personal no admite límite de sesiones.
- Las ventanas del agente deben ser una o dos.

No crea Private Endpoint ni *diagnostic settings*, que van como recursos nativos.

`AzureVirtualDesktop/HostPool` usa `locals` y no expone `public_network_access`, `vm_template`, Private Endpoint ni *diagnostic settings*. Con él, el host pool queda siempre con acceso público.

La pila `AzureVirtualDesktop/VDI` declara un bloque `provider` en su `versions.tf`. Un módulo con su propio bloque `provider` no admite `for_each`, `count` ni `depends_on` desde el root. Por eso llamo directamente a los submódulos.

El provider azurerm no expone la identidad gestionada del host pool. Por eso Start VM on Connect se configura en Terraform con el service principal de Azure Virtual Desktop. En Bicep uso la identidad *system-assigned* del host pool.

### Estructura en el proyecto

```txt
/
├── providers.tf
├── host_pools.tf   # host pools, token, Private Endpoint, diagnósticos y rol de Start VM on Connect
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
      # public_network_access y vm_template existen en toda la rama 4.x.
      # < 5.0.0: restricción de los módulos de AzureTerraformModules.
      version = ">= 4.0.0, < 5.0.0"
    }
    time = {
      source  = "hashicorp/time"
      version = ">= 0.11.0"
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

### Host pools · `host_pools.tf`

```hcl
# =============================================================================
# Host pools con el submódulo AzureVirtualDesktop/VDI/modules/virtual_desktop_host_pool
# DEPENDENCY: Resource Group y Log Analytics workspace existentes
# DEPENDENCY: Subnet de Private Endpoints y zona privatelink.wvd.microsoft.com enlazada a las VNets
#             de los session hosts y de los clientes (si public_network_access no es Enabled)
# DEPENDENCY: Resource provider Microsoft.DesktopVirtualization re-registrado en la suscripción
#             (requisito para usar Private Link con AVD)
# DEPENDENCY: Application groups, workspace y session hosts van en sus propias fichas
# =============================================================================

variable "host_pools" {
  description = "Host pools del entorno (clave = nombre del host pool)."
  type = map(object({
    resource_group_name = string
    location            = string
    friendly_name       = optional(string)
    description         = optional(string)

    type                             = string                     # Pooled | Personal
    load_balancer_type               = string                     # BreadthFirst | DepthFirst (Pooled) · Persistent (Personal)
    maximum_sessions_allowed         = optional(number)           # solo Pooled
    personal_desktop_assignment_type = optional(string)           # Automatic | Direct (solo Personal)
    preferred_app_group_type         = optional(string, "Desktop") # Desktop | RailApplications | None
    validate_environment             = optional(bool, false)
    start_vm_on_connect              = optional(bool, false)
    custom_rdp_properties            = optional(string)

    public_network_access = optional(string, "Disabled") # Enabled | Disabled | EnabledForClientsOnly | EnabledForSessionHostsOnly
    private_endpoint = optional(object({
      subnet_id           = string
      private_dns_zone_id = string # privatelink.wvd.microsoft.com
    }))

    scheduled_agent_updates = optional(object({
      enabled                   = optional(bool, true)
      timezone                  = optional(string, "Romance Standard Time")
      use_session_host_timezone = optional(bool, false)
      schedule = list(object({
        day_of_week = string
        hour_of_day = number
      }))
    }))

    registration_token = optional(object({
      enabled       = optional(bool, true)
      rotation_days = optional(number, 7) # máximo 27 días de validez del token
    }), {})

    log_analytics_workspace_id = string
    diagnostic_log_categories = optional(list(string), [
      "Checkpoint", "Error", "Management", "Connection", "HostRegistration", "AgentHealthStatus"
    ])

    tags = optional(map(string), {})
  }))

  validation {
    condition     = alltrue([for k, v in var.host_pools : contains(["Pooled", "Personal"], v.type)])
    error_message = "type debe ser Pooled o Personal."
  }

  validation {
    condition = alltrue([
      for k, v in var.host_pools : v.type != "Pooled" || (v.maximum_sessions_allowed != null && contains(["BreadthFirst", "DepthFirst"], v.load_balancer_type))
    ])
    error_message = "Un host pool Pooled necesita maximum_sessions_allowed y load_balancer_type BreadthFirst o DepthFirst."
  }

  validation {
    condition = alltrue([
      for k, v in var.host_pools : contains(["Enabled", "Disabled", "EnabledForClientsOnly", "EnabledForSessionHostsOnly"], v.public_network_access)
    ])
    error_message = "public_network_access debe ser Enabled, Disabled, EnabledForClientsOnly o EnabledForSessionHostsOnly."
  }

  validation {
    condition     = alltrue([for k, v in var.host_pools : v.public_network_access == "Enabled" || v.private_endpoint != null])
    error_message = "Si public_network_access no es Enabled, el host pool necesita private_endpoint (subrecurso connection)."
  }

  validation {
    condition     = alltrue([for k, v in var.host_pools : v.registration_token.rotation_days >= 1 && v.registration_token.rotation_days <= 27])
    error_message = "registration_token.rotation_days debe estar entre 1 y 27 (validez máxima del token)."
  }
}

variable "avd_power_on_assignments" {
  description = <<-EOT
    Rol 'Desktop Virtualization Power On Contributor' para Start VM on Connect.
    principal_id = object ID del service principal de Azure Virtual Desktop en el tenant
    (aplicación 9cdead84-a844-4324-93f2-b2e6bb768d07). scope = suscripción o RG que contenga las VMs.
  EOT
  type = map(object({
    principal_id = string
    scope        = string
  }))
  default = {}
}

module "host_pool" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//AzureVirtualDesktop/VDI/modules/virtual_desktop_host_pool?ref=main"
  for_each = var.host_pools

  virtual_desktop_host_pool_name   = each.key
  resource_group_name              = each.value.resource_group_name
  location                         = each.value.location
  friendly_name                    = each.value.friendly_name
  description                      = each.value.description
  type                             = each.value.type
  load_balancer_type               = each.value.load_balancer_type
  maximum_sessions_allowed         = each.value.type == "Pooled" ? each.value.maximum_sessions_allowed : null
  personal_desktop_assignment_type = each.value.type == "Personal" ? each.value.personal_desktop_assignment_type : null
  preferred_app_group_type         = each.value.preferred_app_group_type
  validate_environment             = each.value.validate_environment
  start_vm_on_connect              = each.value.start_vm_on_connect
  custom_rdp_properties            = each.value.custom_rdp_properties
  public_network_access            = each.value.public_network_access
  scheduled_agent_updates          = each.value.scheduled_agent_updates

  tags = merge(var.tags, each.value.tags)
}

# Token de registro con rotación: se regenera al pasar rotation_days (máximo 27 días)
resource "time_rotating" "registration" {
  for_each      = { for k, v in var.host_pools : k => v if v.registration_token.enabled }
  rotation_days = each.value.registration_token.rotation_days
}

module "host_pool_registration" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//AzureVirtualDesktop/VDI/modules/virtual_desktop_host_pool_registration_info?ref=main"
  for_each = time_rotating.registration

  hostpool_id     = module.host_pool[each.key].id
  expiration_date = each.value.rotation_rfc3339
}

# Private Endpoint del subrecurso connection (uno por host pool)
resource "azurerm_private_endpoint" "host_pool" {
  for_each            = { for k, v in var.host_pools : k => v if v.private_endpoint != null }
  name                = "pe-${each.key}-connection"
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  subnet_id           = each.value.private_endpoint.subnet_id

  private_service_connection {
    name                           = "psc-${each.key}-connection"
    private_connection_resource_id = module.host_pool[each.key].id
    subresource_names              = ["connection"]
    is_manual_connection           = false
  }

  private_dns_zone_group {
    name                 = "default"
    private_dns_zone_ids = [each.value.private_endpoint.private_dns_zone_id]
  }

  tags = merge(var.tags, each.value.tags)
}

resource "azurerm_monitor_diagnostic_setting" "host_pool" {
  for_each                   = var.host_pools
  name                       = "diag-${each.key}"
  target_resource_id         = module.host_pool[each.key].id
  log_analytics_workspace_id = each.value.log_analytics_workspace_id

  dynamic "enabled_log" {
    for_each = toset(each.value.diagnostic_log_categories)
    content {
      category = enabled_log.value
    }
  }
}

# Start VM on Connect: el servicio de AVD necesita poder encender las VMs
resource "azurerm_role_assignment" "avd_power_on" {
  for_each             = var.avd_power_on_assignments
  scope                = each.value.scope
  role_definition_name = "Desktop Virtualization Power On Contributor"
  principal_id         = each.value.principal_id
}

output "host_pool_ids" {
  description = "IDs de los host pools."
  value       = { for k, m in module.host_pool : k => m.id }
}

output "registration_tokens" {
  description = "Tokens de registro vigentes (para el agente de los session hosts)."
  value       = { for k, m in module.host_pool_registration : k => m.token }
  sensitive   = true
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

host_pools = {
  "vdpool-<workload>-pro-01" = {
    resource_group_name = "<rg-avd-pro>"
    location            = "<region>"
    friendly_name       = "Escritorio corporativo"

    type                     = "Pooled"
    load_balancer_type       = "BreadthFirst"
    maximum_sessions_allowed = 12 # sale de las pruebas de carga con el SKU elegido
    preferred_app_group_type = "Desktop"
    start_vm_on_connect      = true

    # Session hosts unidos a Entra ID con SSO; añadir aquí redirecciones (portapapeles, unidades…)
    custom_rdp_properties = "enablerdsaadauth:i:1;"

    public_network_access = "Disabled"
    private_endpoint = {
      subnet_id           = "<resourceId snet-privateendpoints>"
      private_dns_zone_id = "<resourceId privatelink.wvd.microsoft.com>"
    }

    scheduled_agent_updates = {
      timezone = "Romance Standard Time"
      schedule = [
        { day_of_week = "Saturday", hour_of_day = 2 }
      ]
    }

    registration_token = {
      rotation_days = 7
    }

    log_analytics_workspace_id = "<resourceId log-analytics-workspace>"
  }

  "vdpool-<workload>-val-01" = {
    resource_group_name = "<rg-avd-pro>"
    location            = "<region>"
    friendly_name       = "Validación"
    description         = "Recibe las actualizaciones del servicio antes que producción"

    type                     = "Pooled"
    load_balancer_type       = "BreadthFirst"
    maximum_sessions_allowed = 12
    validate_environment     = true
    start_vm_on_connect      = true
    custom_rdp_properties    = "enablerdsaadauth:i:1;"

    public_network_access = "Disabled"
    private_endpoint = {
      subnet_id           = "<resourceId snet-privateendpoints>"
      private_dns_zone_id = "<resourceId privatelink.wvd.microsoft.com>"
    }

    log_analytics_workspace_id = "<resourceId log-analytics-workspace>"
  }

  "vdpool-<workload>-pro-dev01" = {
    resource_group_name = "<rg-avd-pro>"
    location            = "<region>"
    friendly_name       = "Puestos de desarrollo"

    type                             = "Personal"
    load_balancer_type               = "Persistent"
    personal_desktop_assignment_type = "Automatic"
    start_vm_on_connect              = true
    custom_rdp_properties            = "enablerdsaadauth:i:1;"

    public_network_access = "Disabled"
    private_endpoint = {
      subnet_id           = "<resourceId snet-privateendpoints>"
      private_dns_zone_id = "<resourceId privatelink.wvd.microsoft.com>"
    }

    log_analytics_workspace_id = "<resourceId log-analytics-workspace>"
  }
}

avd_power_on_assignments = {
  suscripcion-avd = {
    principal_id = "<objectId del service principal Azure Virtual Desktop>"
    scope        = "/subscriptions/<subscriptionId-avd-pro>"
  }
}
```

En `dev.tfvars` y `pre.tfvars`, mismo esquema con un único host pool, menos sesiones y `start_vm_on_connect = true` para no pagar VMs encendidas sin uso.

Para obtener el `principal_id` del service principal de Azure Virtual Desktop en el tenant del cliente:

```powershell
(Get-AzADServicePrincipal -ApplicationId "9cdead84-a844-4324-93f2-b2e6bb768d07").Id
```

Despliegue:

```powershell
terraform init
terraform plan -var-file="env/pro.tfvars" -out="pro.tfplan"
terraform apply "pro.tfplan"
```

Leer el token para el agente de los session hosts (sin dejarlo en disco):

```powershell
(terraform output -json registration_tokens | ConvertFrom-Json)."vdpool-<workload>-pro-01"
```

### Equivalente en Bicep

`main.bicep`:

```bicep
// =============================================================================
// Host pool de AVD privado: Private Endpoint (connection), diagnósticos,
// token de registro e identidad gestionada para Start VM on Connect
// DEPENDENCY: Resource Group existente (targetScope = resourceGroup)
// DEPENDENCY: Subnet de Private Endpoints y zona privatelink.wvd.microsoft.com enlazada a las VNets
// DEPENDENCY: Resource provider Microsoft.DesktopVirtualization re-registrado en la suscripción (Private Link)
// DEPENDENCY: Log Analytics workspace existente
// DEPENDENCY: Session hosts en este mismo Resource Group (alcance del rol de Start VM on Connect)
// =============================================================================
targetScope = 'resourceGroup'

param location string = resourceGroup().location

@minLength(3)
@maxLength(64)
param hostPoolName string

param friendlyName string = ''

@allowed(['Pooled', 'Personal'])
param hostPoolType string = 'Pooled'

@description('Pooled: BreadthFirst o DepthFirst. Personal: Persistent.')
@allowed(['BreadthFirst', 'DepthFirst', 'Persistent'])
param loadBalancerType string = 'BreadthFirst'

@description('Solo Pooled: sesiones máximas por session host (sale de las pruebas de carga).')
@minValue(1)
@maxValue(999999)
param maxSessionLimit int = 12

@allowed(['Automatic', 'Direct'])
param personalDesktopAssignmentType string = 'Automatic'

@allowed(['Desktop', 'RailApplications', 'None'])
param preferredAppGroupType string = 'Desktop'

param validationEnvironment bool = false

param startVMOnConnect bool = true

@description('Propiedades RDP personalizadas. enablerdsaadauth:i:1 activa el SSO con Entra ID.')
param customRdpProperty string = 'enablerdsaadauth:i:1;'

@allowed(['Enabled', 'Disabled', 'EnabledForClientsOnly', 'EnabledForSessionHostsOnly'])
param publicNetworkAccess string = 'Disabled'

param privateEndpointSubnetId string
param privateDnsZoneId string
param logAnalyticsWorkspaceId string

param diagnosticLogCategories array = [
  'Checkpoint'
  'Error'
  'Management'
  'Connection'
  'HostRegistration'
  'AgentHealthStatus'
]

@description('Validez del token de registro (máximo 27 días).')
param registrationTokenExpiration string = dateTimeAdd(utcNow(), 'P7D')

@description('Ventanas de actualización del agente (máximo 2). Vacío = actualización por defecto del servicio.')
param agentUpdateWindows array = [
  {
    dayOfWeek: 'Saturday'
    hour: 2
  }
]

param agentUpdateTimeZone string = 'Romance Standard Time'

param tags object = {}

// Desktop Virtualization Power On Contributor (rol integrado)
var powerOnContributorRoleId = '489581de-a3bd-480d-9518-53dea7416b33'

var logs = [for c in diagnosticLogCategories: { category: c, enabled: true }]

resource hostPool 'Microsoft.DesktopVirtualization/hostPools@2025-10-10' = {
  name: hostPoolName
  location: location
  tags: tags
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    friendlyName: empty(friendlyName) ? null : friendlyName
    hostPoolType: hostPoolType
    loadBalancerType: hostPoolType == 'Personal' ? 'Persistent' : loadBalancerType
    maxSessionLimit: hostPoolType == 'Pooled' ? maxSessionLimit : null
    personalDesktopAssignmentType: hostPoolType == 'Personal' ? personalDesktopAssignmentType : null
    preferredAppGroupType: preferredAppGroupType
    validationEnvironment: validationEnvironment
    startVMOnConnect: startVMOnConnect
    customRdpProperty: customRdpProperty
    publicNetworkAccess: publicNetworkAccess
    registrationInfo: {
      expirationTime: registrationTokenExpiration
      registrationTokenOperation: 'Update'
    }
    agentUpdate: empty(agentUpdateWindows)
      ? {
          type: 'Default'
        }
      : {
          type: 'Scheduled'
          maintenanceWindowTimeZone: agentUpdateTimeZone
          useSessionHostLocalTime: false
          maintenanceWindows: agentUpdateWindows
        }
  }
}

resource privateEndpoint 'Microsoft.Network/privateEndpoints@2024-05-01' = {
  name: 'pe-${hostPoolName}-connection'
  location: location
  tags: tags
  properties: {
    subnet: {
      id: privateEndpointSubnetId
    }
    privateLinkServiceConnections: [
      {
        name: 'psc-${hostPoolName}-connection'
        properties: {
          privateLinkServiceId: hostPool.id
          groupIds: [
            'connection'
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
        name: 'privatelink-wvd-microsoft-com'
        properties: {
          privateDnsZoneId: privateDnsZoneId
        }
      }
    ]
  }
}

resource diagnostics 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = {
  name: 'diag-${hostPoolName}'
  scope: hostPool
  properties: {
    workspaceId: logAnalyticsWorkspaceId
    logs: logs
  }
}

// Start VM on Connect con la identidad del host pool, acotado al RG de los session hosts
resource powerOnAssignment 'Microsoft.Authorization/roleAssignments@2022-04-01' = if (startVMOnConnect) {
  name: guid(resourceGroup().id, hostPool.id, powerOnContributorRoleId)
  properties: {
    principalId: hostPool.identity.principalId
    principalType: 'ServicePrincipal'
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', powerOnContributorRoleId)
  }
}

output hostPoolId string = hostPool.id
output hostPoolPrincipalId string = hostPool.identity.principalId

@secure()
output registrationToken string = first(hostPool.listRegistrationTokens().value)!.token
```

`main.pro.bicepparam`:

```bicep
using 'main.bicep'

param hostPoolName = 'vdpool-<workload>-pro-01'
param friendlyName = 'Escritorio corporativo'
param hostPoolType = 'Pooled'
param loadBalancerType = 'BreadthFirst'
param maxSessionLimit = 12
param preferredAppGroupType = 'Desktop'
param startVMOnConnect = true
param customRdpProperty = 'enablerdsaadauth:i:1;'
param publicNetworkAccess = 'Disabled'

param privateEndpointSubnetId = '<resourceId snet-privateendpoints>'
param privateDnsZoneId = '<resourceId privatelink.wvd.microsoft.com>'
param logAnalyticsWorkspaceId = '<resourceId log-analytics-workspace>'

param agentUpdateWindows = [
  {
    dayOfWeek: 'Saturday'
    hour: 2
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
az provider register --namespace Microsoft.DesktopVirtualization
az deployment group what-if --resource-group <rg-avd-pro> --parameters main.pro.bicepparam
az deployment group create  --resource-group <rg-avd-pro> --parameters main.pro.bicepparam
```

## Errores típicos

| Síntoma | Causa | Solución |
|---|---|---|
| El session host no aparece en el pool; evento 3277 `INVALID_REGISTRATION_TOKEN` o `EXPIRED_MACHINE_TOKEN` | Token caducado o de otro host pool | Generar un token nuevo, escribirlo en `HKLM:\SOFTWARE\Microsoft\RDInfraAgent` y reiniciar `RDAgentBootLoader` |
| Hosts preaprovisionados que no se registran tras meses apagados | El token de máquina caduca a los 90 días sin encender la VM | Encenderlas al menos 20 minutos cada 90 días |
| Tras cambiar `public_network_access` o crear el PE, los hosts no aceptan sesiones | El agente no recarga la configuración de red | Reiniciar `RDAgentBootLoader` en cada host (o reiniciar los hosts) |
| Los usuarios no conectan con el host pool en `Disabled` | El cliente no resuelve por `privatelink.wvd.microsoft.com` o falta el PE `feed` del workspace | Revisar DNS privado y los PE `connection` y `feed` |
| Conexión intermitente con Private Link | NSG o firewall limitando puertos hacia el PE `connection` | Abrir el rango TCP 1–65535 hacia la IP del PE |
| RDP Shortpath deja de funcionar al pasar a Private Link | UDP sobre Private Link requiere *opt-in* | Activar "Allow Direct UDP network path over Private Link" y desactivar Shortpath público (STUN/TURN) |
| Start VM on Connect no enciende la VM | Falta el rol *Desktop Virtualization Power On Contributor* en un alcance que contenga las VMs | Asignarlo al service principal de AVD o a la identidad del host pool |
| Start VM on Connect falla con nombres con tildes o eñes | Solo admite caracteres ANSI en host pool, hosts y RG | Renombrar siguiendo la convención sin caracteres especiales |
| Todos los usuarios caen en el mismo host | DepthFirst con el límite por defecto (999999) | Fijar `maximum_sessions_allowed` con datos reales |
| Se supera el límite de sesiones de un host | Muchas conexiones simultáneas: el servicio puede rebasarlo puntualmente | Dimensionar con margen; no es un error de configuración |
| El usuario solo ve las RemoteApps y no el escritorio | `preferred_app_group_type` y asignación a ambos tipos de application group | Ajustar el tipo preferido o separar las asignaciones |
| Entra ID join: los clientes web, macOS o iOS no conectan | Falta SSO o la propiedad RDP para Entra ID | `enablerdsaadauth:i:1` con SSO configurado (o `targetisaadjoined:i:1` como alternativa heredada) |
| Doble petición de credenciales con SSO en hosts con Entra hybrid join | Falta el objeto Kerberos en Entra ID | Crear el *Kerberos Server object* |
| `terraform plan` quiere recrear el host pool | Cambio de `type`, `personal_desktop_assignment_type`, `name` o `location` (fuerzan recreación) | Decidirlo antes; un cambio de tipo es una migración |
| No se puede añadir una session host configuration a un pool existente | El modelo de gestión se fija al crear | Crear un host pool nuevo con ese modelo |
| Error al guardar el *diagnostic setting* | La categoría ya está activa en otro *diagnostic setting* del mismo host pool | Unificar las categorías en un único *diagnostic setting* |
