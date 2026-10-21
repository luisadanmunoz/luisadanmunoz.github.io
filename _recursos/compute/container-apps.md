---
title: "Container Apps"
indice: compute
resumen: "Contenedores sin gestionar Kubernetes."
estado: documentado   # proximamente | en-curso | documentado
orden: 4
last_review: 2026-10-21
fuentes:
  - titulo: "Azure Container Apps environments"
    url: https://learn.microsoft.com/azure/container-apps/environment
  - titulo: "Compute and billing structures in Azure Container Apps"
    url: https://learn.microsoft.com/azure/container-apps/structure
  - titulo: "Azure Container Apps plan types"
    url: https://learn.microsoft.com/azure/container-apps/plans
  - titulo: "Workload profiles in Azure Container Apps"
    url: https://learn.microsoft.com/azure/container-apps/workload-profiles-overview
  - titulo: "Consumption-only environment type in Azure Container Apps (legacy)"
    url: https://learn.microsoft.com/azure/container-apps/environment-type-consumption-only
  - titulo: "Azure Container Apps express overview"
    url: https://learn.microsoft.com/azure/container-apps/express-overview
  - titulo: "Azure Container Apps express FAQ"
    url: https://learn.microsoft.com/azure/container-apps/express-faq
  - titulo: "Containers in Azure Container Apps"
    url: https://learn.microsoft.com/azure/container-apps/containers
  - titulo: "Billing in Azure Container Apps"
    url: https://learn.microsoft.com/azure/container-apps/billing
  - titulo: "Networking in an Azure Container Apps environment"
    url: https://learn.microsoft.com/azure/container-apps/networking
  - titulo: "Virtual network configuration"
    url: https://learn.microsoft.com/azure/container-apps/custom-virtual-networks
  - titulo: "Provide a virtual network to an Azure Container Apps environment"
    url: https://learn.microsoft.com/azure/container-apps/vnet-custom
  - titulo: "Private endpoints and DNS for virtual networks in Azure Container Apps environments"
    url: https://learn.microsoft.com/azure/container-apps/private-endpoints-with-dns
  - titulo: "Use a private endpoint with an Azure Container Apps environment"
    url: https://learn.microsoft.com/azure/container-apps/how-to-use-private-endpoint
  - titulo: "Azure Private Endpoint private DNS zone values"
    url: https://learn.microsoft.com/azure/private-link/private-endpoint-dns
  - titulo: "Control outbound traffic in Azure Container Apps with user defined routes"
    url: https://learn.microsoft.com/azure/container-apps/user-defined-routes
  - titulo: "Azure Container Apps environment integration with Azure Firewall"
    url: https://learn.microsoft.com/azure/container-apps/use-azure-firewall
  - titulo: "Network security groups for configuring a virtual network in Azure Container Apps"
    url: https://learn.microsoft.com/azure/container-apps/firewall-integration
  - titulo: "Protect Azure Container Apps with Web Application Firewall on Application Gateway"
    url: https://learn.microsoft.com/azure/container-apps/waf-app-gateway
  - titulo: "Configure ingress for an Azure Container Apps environment"
    url: https://learn.microsoft.com/azure/container-apps/ingress-environment-configuration
  - titulo: "Reliability in Azure Container Apps"
    url: https://learn.microsoft.com/azure/reliability/reliability-container-apps
  - titulo: "Security overview for Azure Container Apps"
    url: https://learn.microsoft.com/azure/container-apps/security
  - titulo: "Secure your Azure Container Apps deployment"
    url: https://learn.microsoft.com/azure/container-apps/secure-deployment
  - titulo: "Manage secrets in Azure Container Apps"
    url: https://learn.microsoft.com/azure/container-apps/manage-secrets
  - titulo: "Managed identities in Azure Container Apps"
    url: https://learn.microsoft.com/azure/container-apps/managed-identity
  - titulo: "Azure Container Apps image pull with managed identity"
    url: https://learn.microsoft.com/azure/container-apps/managed-identity-image-pull
  - titulo: "Log storage and monitoring options in Azure Container Apps"
    url: https://learn.microsoft.com/azure/container-apps/log-options
  - titulo: "Monitor logs in Azure Container Apps with Log Analytics"
    url: https://learn.microsoft.com/azure/container-apps/log-monitoring
  - titulo: "Supported logs for Microsoft.App/managedEnvironments"
    url: https://learn.microsoft.com/azure/azure-monitor/reference/supported-logs/microsoft-app-managedenvironments-logs
  - titulo: "Troubleshoot common deployment failures in Azure Container Apps"
    url: https://learn.microsoft.com/azure/container-apps/troubleshoot-deployment-errors
  - titulo: "Azure built-in roles"
    url: https://learn.microsoft.com/azure/role-based-access-control/built-in-roles
  - titulo: "azurerm_container_app_environment"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/container_app_environment
  - titulo: "azurerm_container_app"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/container_app
  - titulo: "azurerm_container_app_job"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/container_app_job
  - titulo: "Microsoft.App managedEnvironments (plantillas ARM/Bicep)"
    url: https://learn.microsoft.com/azure/templates/microsoft.app/managedenvironments
  - titulo: "Microsoft.App containerApps (plantillas ARM/Bicep)"
    url: https://learn.microsoft.com/azure/templates/microsoft.app/containerapps
  - titulo: "Módulo Terraform Containers/Containers"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Containers/Containers
  - titulo: "Módulo Terraform Containers/ContainerApp"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Containers/ContainerApp
  - titulo: "Módulo Terraform Containers/ContainerAppEnvironment"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Containers/ContainerAppEnvironment
  - titulo: "Módulo Terraform PRO/common/assigned_identity"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/PRO/common/assigned_identity
  - titulo: "Módulo Terraform Networking/Networking/modules/private_endpoint"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Networking/Networking/modules/private_endpoint
  - titulo: "Módulo Terraform Security/Seguridad/modules/monitor_diagnostic_setting"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Security/Seguridad/modules/monitor_diagnostic_setting
---

**Azure Container Apps** ejecuta APIs, microservicios, workers y tareas en contenedores sin exponer ni operar Kubernetes: escala con reglas HTTP o KEDA (también a cero), publica con un ingress gestionado, versiona con revisiones e integra Dapr. Todo vive dentro de un **entorno**, que es el límite de red, registros y cómputo que comparten sus apps y jobs. Las imágenes salen de [Container Registry](/recursos/compute/container-registry/).

## Qué es y cuándo usarlo

### Container Apps frente a las alternativas

| Necesidad | Servicio |
|---|---|
| APIs y microservicios con escalado automático, revisiones e ingress gestionado | **Container Apps** |
| Workers que escalan con colas o eventos y tareas programadas o bajo demanda | **Container Apps** (apps sin ingress y jobs) |
| API de Kubernetes completa, operadores, CRD o nodos Windows | [AKS](/recursos/compute/aks/) |
| Un contenedor puntual sin orquestación | [Container Instances](/recursos/compute/container-instances/) |

### Tipos de entorno

| | **Workload profiles (v2)** | Solo Consumption (v1, heredado) | Express |
|---|---|---|---|
| Situación | **Tipo por defecto y recomendado** | Heredado | Entorno compartido y gestionado para apps web y APIs sencillas |
| Planes | Consumption y Dedicated | Consumption | Consumption |
| UDR, NAT Gateway y private endpoints | **Sí** | No | Sin perfiles de carga, Dapr, jobs, identidad de sistema, referencias a Key Vault, dominios propios ni sidecars; hasta 30 réplicas por app |
| Subred | **/27** como mínimo, delegada a `Microsoft.App/environments` | /23 | — |

Para pagar por uso, Microsoft recomienda **un entorno v2 con el perfil Consumption**, no un entorno v1. Microsoft puede **migrar automáticamente** algunos entornos existentes a Express, avisando entre 25 y 30 días antes y con opción de excluirse.

### Perfiles de carga

| Perfil | Plan | Características |
|---|---|---|
| **Consumption** | Consumption | Serverless, escala a cero, hasta **4 vCPU y 8 GiB** por réplica en pasos de 0,25 vCPU con el doble de memoria. Incluido siempre y solo uno por entorno |
| **Dedicated** D4-D32 (uso general) y E4-E32 (memoria) | Dedicated | Un solo inquilino; se paga por instancia del perfil y varias apps comparten instancias |
| GPU (Consumption o Dedicated) | Según el perfil | Regiones concretas; los dedicados con GPU exigen ticket de capacidad |
| Flexible (preview) | — | Subred /25 como mínimo; no escala a cero |

### Red

| Decisión | Recomendación |
|---|---|
| VNet | Propia desde el principio: **el tipo de red y el tamaño de la subred no se pueden cambiar** tras crear el entorno |
| Subred | Exclusiva del entorno. Container Apps reserva 14 IPs; con Consumption, una IP por cada 10 réplicas; con Dedicated, una por nodo; en modo Single las necesidades se duplican durante cada despliegue. Una /27 da 90 réplicas Consumption o 9 nodos |
| Entrada | **Entorno interno** (IP privada); publicar a Internet con Application Gateway con WAF o Front Door Premium con Private Link. En un entorno externo, la entrada no pasa por la subred y **no se puede filtrar con NSG** |
| DNS con entorno interno | Zona privada con el dominio por defecto del entorno y registros `*` y `@` hacia su IP estática |
| Private endpoint | Acceso público desactivado, subred **no delegada** y zona `privatelink.<región>.azurecontainerapps.io` |
| Salida | UDR hacia Azure Firewall o NAT Gateway (solo v2). El firewall debe permitir `mcr.microsoft.com`, `*.data.mcr.microsoft.com`, `packages.aks.azure.com`, `acs-mirror.azureedge.net`, el ACR y `*.blob.core.windows.net`, Key Vault y los endpoints de identidad |

### Seguridad

| Control | Recomendación |
|---|---|
| Identidad | Identidad de usuario para el pull de ACR (Microsoft la prefiere a la de sistema) y para acceder a Key Vault, Storage, Service Bus o SQL |
| Secretos | **Referencias a Key Vault** con el rol Key Vault Secrets User; con URI sin versión, Container Apps recoge la nueva versión en 30 minutos como máximo |
| Transporte | Sin HTTP inseguro; **cifrado entre apps** del entorno (peer-to-peer, puede añadir latencia); mTLS con clientes externos mediante certificado de cliente |
| Entrada | Ingress limitado al entorno o a la VNet, restricciones de IP y WAF delante |
| Imágenes | ACR privado y escaneo con Defender |
| Registros | `azure-monitor` + diagnostic settings: el envío directo a Log Analytics **no admite Private Link** |

**Rutas HTTP del entorno** (`httpRouteConfigs`): una regla de enrutado del entorno puede exponer apps que tienen ingress interno, así que conviene limitar quién puede crearlas en el entorno.

### Disponibilidad y ciclo de vida

- **Redundancia de zona**: solo al crear el entorno, con VNet propia y **al menos 2 réplicas mínimas** por app. No se puede activar ni desactivar después. Sin coste extra.
- Las cargas son sin estado: el almacenamiento efímero se pierde con la réplica.
- **Un entorno inactivo (sin apps ni jobs activos) o en estado fallido por la red o Azure Policy durante más de 90 días se elimina automáticamente.**

### Cómo se factura

| Concepto | Detalle |
|---|---|
| Consumption | vCPU-segundos, GiB-segundos y peticiones HTTP. **Gratis cada mes por suscripción: 180 000 vCPU-s, 360 000 GiB-s y 2 millones de peticiones** |
| Réplicas a cero | Sin coste de cómputo |
| Dedicated | Cuota fija de **Dedicated Plan Management** por entorno más cada instancia de perfil |
| **Private endpoints y mantenimiento planificado** | **Generan la cuota de Dedicated Plan Management también en Consumption** |
| Ingress | Las réplicas del proxy de entrada no se facturan en el modo por defecto |
| Red y registros | NAT Gateway, firewall, Private Link y Log Analytics, aparte |

### Qué escenario recomiendo

| Escenario del cliente | Diseño | Por qué |
|---|---|---|
| APIs internas y microservicios en producción | Entorno v2 interno, zonas, Consumption, App Gateway con WAF o APIM delante | Red privada y pago por uso |
| Cargas estables o que necesitan más de 4 vCPU por réplica | Perfil Dedicated D o E | Coste predecible y aislamiento |
| Workers de colas | App sin ingress con regla KEDA, mínimo 0 si tolera arranques en frío | Solo paga cuando hay trabajo |
| Procesos programados o bajo demanda | Container Apps jobs | Sin réplicas permanentes |
| Acceso privado desde otras redes o Front Door | Private endpoint con acceso público desactivado | Tráfico privado (con cuota de gestión dedicada) |
| Entornos v1 existentes | Migrar a v2 | UDR, NAT, private endpoints y mejor uso de IPs |
| Webs y APIs simples sin requisitos de red | Express | Sin infraestructura que gestionar |
| Requisitos de Kubernetes completos | AKS | Container Apps no expone la API de Kubernetes |

### Datos que conviene llevar a la reunión

- **Entorno v2 siempre**: v1 no admite UDR, NAT Gateway ni private endpoints.
- **La red, la subred y la redundancia de zona se eligen al crear el entorno** y no se cambian.
- **Hay capa gratuita mensual** por suscripción en Consumption.
- **El private endpoint añade la cuota de Dedicated Plan Management**, también en Consumption.
- **Un entorno inactivo 90 días se elimina.**
- **Un entorno externo no se puede filtrar con NSG**: entorno interno y WAF delante.
- **Microsoft puede migrar entornos existentes a Express** salvo que el cliente se excluya.

## Decisiones de diseño

| Decisión | Lo que aplico | Por qué |
|---|---|---|
| Entorno | Submódulo `container_app_environment` del repositorio | Expone lo necesario y admite `for_each` |
| Tipo | v2 con el perfil Consumption declarado siempre y perfiles dedicados opcionales | Añadir perfiles a un entorno creado sin ellos lo recrea |
| Red | Subred obligatoria, entorno interno, acceso público desactivado | Sin exposición a Internet |
| DNS | Zona privada del dominio por defecto (`*` y `@`) enlazada a las VNets indicadas; private endpoints opcionales | Resolución desde el hub y el spoke |
| Zonas | Activadas por defecto; aviso (`check`) si una app tiene menos de 2 réplicas mínimas | Solo se eligen al crear |
| Cifrado | Peer-to-peer activado por defecto | Tráfico cifrado dentro del entorno |
| Registros | `azure-monitor` + diagnostic settings (consola, sistema, HTTP opcional, métricas) en tablas dedicadas | Compatible con Private Link y sin la clave del workspace |
| Identidad | Una identidad de usuario por app y por job con sus roles creados **antes** | El pull y la lectura de secretos ocurren al crear la revisión |
| Secretos | Solo referencias a Key Vault; las variables apuntan a secretos declarados (validado) | Nada sensible en el código ni en los `tfvars` |
| Ingress | Sin HTTP inseguro, 100 % a la última revisión, restricciones de IP opcionales | Superficie mínima |
| Recursos | Validación de CPU y memoria del perfil Consumption | Evita errores de despliegue |
| Sondas | Startup, liveness y readiness HTTP en la misma ruta | Tráfico solo a réplicas sanas |
| Jobs | Programados (cron UTC) o manuales | Tareas sin réplicas permanentes |

Alineación con el Well-Architected Framework:

- **Fiabilidad**: zonas, 2 réplicas mínimas, sondas y revisiones.
- **Seguridad**: red privada, identidad sin credenciales, Key Vault, HTTPS y cifrado entre apps.
- **Coste**: escala a cero, capa gratuita, perfiles según carga y jobs.
- **Excelencia operativa**: IaC con validaciones y registros centralizados.
- **Rendimiento**: escalado HTTP y KEDA, y perfiles dedicados para cargas pesadas.

## Módulo de Terraform

### Los módulos del repositorio

| Módulo | Estado |
|---|---|
| [`Containers/Containers`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Containers/Containers) (raíz) | Declara un bloque `provider` en `versions.tf`: solo sus submódulos admiten `for_each` |
| `Containers/Containers/modules/container_app_environment` | **Lo reutilizo**: expone `public_network_access`, `logs_destination`, `mutual_tls_enabled`, zonas y perfiles. Su variable `dapr_application_insights_connection_string` no es `sensitive` |
| `Containers/Containers/modules/container_app_job` | **Lo reutilizo** para los jobs |
| `Containers/Containers/modules/container_app` | **Falla con OpenTofu en apps sin ingress** (comprobado con 1.8): la precondición de `traffic_weight` indexa `var.ingress` aunque sea null. Tampoco devuelve la identidad. Uso el recurso nativo |
| [`Containers/ContainerApp`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Containers/ContainerApp) | **No pasa `validate`** con azurerm 4.81: la variable `secrets` es `sensitive` y se usa en un `for_each` dinámico. Usa `count` y `locals` |
| [`Containers/ContainerAppEnvironment`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Containers/ContainerAppEnvironment) | **Falla en cualquier `plan`** (comprobado): `dapr_components`, `storages` y `certificates` son `sensitive` y se recorren con `for_each`, aunque estén vacías. Sin subred tampoco funciona: envía `internal_load_balancer_enabled` y `zone_redundancy_enabled` como `false` y el provider exige la subred en cuanto se declaran. No expone `public_network_access` ni `logs_destination` |

También reutilizo [`PRO/common/assigned_identity`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/PRO/common/assigned_identity), [`Networking/Networking/modules/private_endpoint`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Networking/Networking/modules/private_endpoint) (subrecurso `managedEnvironments`) y [`Security/Seguridad/modules/monitor_diagnostic_setting`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Security/Seguridad/modules/monitor_diagnostic_setting).

Notas del provider (azurerm 4.81):

- La subred, el entorno interno, la redundancia de zona y el grupo de infraestructura **fuerzan la recreación** del entorno.
- Pasar de no tener `workload_profile` a tenerlos (o al revés) **fuerza la recreación** del entorno.
- `mutual_tls_enabled` figura como preview en el provider.

### Estructura en el proyecto

```txt
/
├── providers.tf        # azurerm >= 4.81.0
├── container_apps.tf   # entorno, DNS, private endpoints, diagnóstico, identidades, roles, apps y jobs
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
      # Validado con 4.81.0 (azurerm_container_app_environment con logs_destination, public_network_access
      # y mutual_tls_enabled).
      # < 5.0.0: restricción de los módulos de AzureTerraformModules.
      version = ">= 4.81.0, < 5.0.0"
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

### `container_apps.tf`

```hcl
# =============================================================================
# Azure Container Apps seguro por defecto:
# entorno de workload profiles (v2) interno en una subred propia, sin acceso público,
# redundante en zonas, con cifrado entre aplicaciones, logs por Azure Monitor (diagnostic
# settings) y DNS privado; apps y jobs con identidad de usuario para el pull de ACR y los
# secretos como referencias a Key Vault (nunca valores en el código)
#
# DEPENDENCY: grupos de recursos creados
# DEPENDENCY: subred exclusiva delegada a Microsoft.App/environments, /27 como mínimo
#             (dimensionarla al crear: no se puede cambiar); /25 si se usará el perfil Flexible
# DEPENDENCY: salida controlada: tabla de rutas 0.0.0.0/0 al firewall (o NAT Gateway) asociada a la
#             subred, con las reglas de salida de Container Apps (MCR, AKS, ACR, Key Vault, identidad)
# DEPENDENCY: private endpoints: subred NO delegada y zona privatelink.<región>.azurecontainerapps.io
# DEPENDENCY: ACR con acceso desde la red del entorno; Key Vault con los secretos
# DEPENDENCY: Log Analytics para el diagnóstico (el envío directo no admite Private Link)
# DEPENDENCY: la identidad de Terraform necesita permisos para asignar roles en ACR, Key Vault y
#             los ámbitos de role_assignments
# =============================================================================

variable "container_app_environments" {
  description = "Entornos de Container Apps (clave = nombre del entorno)."
  type = map(object({
    resource_group_name                = string
    location                           = string
    infrastructure_subnet_id           = string           # delegada a Microsoft.App/environments, /27 o mayor
    infrastructure_resource_group_name = optional(string) # grupo gestionado por la plataforma

    internal_load_balancer_enabled = optional(bool, true) # entorno interno: solo accesible desde la red
    public_network_access          = optional(string, "Disabled")
    zone_redundancy_enabled        = optional(bool, true) # solo al crear
    mutual_tls_enabled             = optional(bool, true) # cifrado entre apps del entorno (algo de latencia)

    # El perfil Consumption se añade siempre; aquí solo los dedicados
    dedicated_workload_profiles = optional(map(object({
      workload_profile_type = string # D4 | D8 | D16 | D32 | E4 | E8 | E16 | E32 | NC24-A100 | NC48-A100 | NC96-A100
      minimum_count         = optional(number, 0)
      maximum_count         = number
    })), {})

    # Zona privada <dominio por defecto> con registros * y @ hacia la IP estática del entorno interno
    private_dns = optional(object({
      resource_group_name = string
      virtual_network_ids = map(string) # VNets que resuelven las apps
    }))

    private_endpoints = optional(map(object({
      subnet_id           = string # no delegada
      private_dns_zone_id = string # privatelink.<región>.azurecontainerapps.io
    })), {})

    log_analytics_workspace_id = string
    http_logs_enabled          = optional(bool, false) # ContainerAppHTTPLogs (coste)
    tags                       = optional(map(string), {})
  }))
  default = {}

  validation {
    condition     = alltrue([for k, v in var.container_app_environments : can(regex("^[a-z][a-z0-9-]{0,58}[a-z0-9]$", k))])
    error_message = "Nombre del entorno: 2-60 minúsculas, números y guiones, empezando por letra."
  }

  validation {
    condition = alltrue([
      for k, v in var.container_app_environments :
      contains(["Enabled", "Disabled"], v.public_network_access) &&
      (length(v.private_endpoints) == 0 || v.public_network_access == "Disabled")
    ])
    error_message = "public_network_access: Enabled o Disabled; los private endpoints exigen Disabled."
  }

  validation {
    condition = alltrue(flatten([
      for k, v in var.container_app_environments : [
        for pk, p in v.dedicated_workload_profiles :
        pk != "Consumption" &&
        contains(["D4", "D8", "D16", "D32", "E4", "E8", "E16", "E32", "NC24-A100", "NC48-A100", "NC96-A100"], p.workload_profile_type) &&
        p.maximum_count >= p.minimum_count
      ]
    ]))
    error_message = "Perfiles dedicados: tipos D4-D32, E4-E32 o NC*-A100, nombre distinto de Consumption y maximum_count >= minimum_count."
  }

  validation {
    condition     = alltrue([for k, v in var.container_app_environments : v.private_dns == null || v.internal_load_balancer_enabled])
    error_message = "La zona privada del dominio por defecto solo tiene sentido en un entorno interno."
  }
}

variable "container_apps" {
  description = "Container apps (clave = nombre de la app)."
  type = map(object({
    environment              = string # clave de container_app_environments
    resource_group_name      = string
    workload_profile_name    = optional(string, "Consumption")
    revision_mode            = optional(string, "Single")
    min_replicas             = optional(number, 2) # con zonas, 2 o más para repartir réplicas
    max_replicas             = optional(number, 10)
    http_concurrent_requests = optional(number) # regla de escalado HTTP

    ingress = optional(object({
      target_port             = number
      external_enabled        = optional(bool, false) # false = solo dentro del entorno
      transport               = optional(string, "auto")
      client_certificate_mode = optional(string, "ignore") # ignore | accept | require (mTLS con clientes)
      allowed_ip_ranges       = optional(list(string), [])
    }))

    acr = optional(object({
      server      = string
      registry_id = string
      role        = optional(string, "Container Registry Repository Reader")
    }))

    key_vault_id = optional(string)          # Key Vault Secrets User para la identidad de la app
    secrets      = optional(map(string), {}) # nombre (minúsculas) -> ID del secreto en Key Vault (sin versión = rotación)

    role_assignments = optional(map(object({
      scope = string
      role  = string
    })), {})

    containers = map(object({
      image      = string
      cpu        = number
      memory     = string # "2Gi"; en Consumption, el doble de la CPU
      args       = optional(list(string))
      command    = optional(list(string))
      env        = optional(map(string), {})
      secret_env = optional(map(string), {}) # VARIABLE -> nombre del secreto
      probe = optional(object({
        path      = string
        port      = number
        transport = optional(string, "HTTP")
      }))
    }))

    tags = optional(map(string), {})
  }))
  default = {}

  validation {
    condition     = alltrue([for k, v in var.container_apps : can(regex("^[a-z][a-z0-9-]{0,30}[a-z0-9]$", k)) && !strcontains(k, "--")])
    error_message = "Nombre de la app: 2-32 minúsculas, números y guiones, empezando por letra y sin guiones dobles."
  }

  validation {
    condition = alltrue([
      for k, v in var.container_apps :
      contains(["Single", "Multiple"], v.revision_mode) &&
      v.max_replicas >= v.min_replicas && v.min_replicas >= 0
    ])
    error_message = "revision_mode: Single o Multiple; max_replicas >= min_replicas >= 0."
  }

  validation {
    condition = alltrue([
      for k, v in var.container_apps :
      v.ingress == null || (
        contains(["auto", "http", "http2", "tcp"], try(v.ingress.transport, "auto")) &&
        contains(["ignore", "accept", "require"], try(v.ingress.client_certificate_mode, "ignore"))
      )
    ])
    error_message = "ingress.transport: auto, http, http2 o tcp; client_certificate_mode: ignore, accept o require."
  }

  validation {
    condition = alltrue([
      for k, v in var.container_apps :
      v.workload_profile_name != "Consumption" || (
        sum([for c in values(v.containers) : c.cpu]) >= 0.25 &&
        sum([for c in values(v.containers) : c.cpu]) <= 4 &&
        sum([for c in values(v.containers) : c.cpu]) * 4 == floor(sum([for c in values(v.containers) : c.cpu]) * 4) &&
        sum([for c in values(v.containers) : tonumber(trimsuffix(c.memory, "Gi"))]) == 2 * sum([for c in values(v.containers) : c.cpu])
      )
    ])
    error_message = "En Consumption, la CPU total va de 0,25 a 4 en pasos de 0,25 y la memoria total es el doble (por ejemplo 0.5 y 1Gi)."
  }

  validation {
    condition = alltrue(flatten([
      for k, v in var.container_apps : concat(
        [for s in keys(v.secrets) : can(regex("^[a-z0-9][a-z0-9-]*[a-z0-9]$", s))],
        [for c in values(v.containers) : [for sn in values(c.secret_env) : contains(keys(v.secrets), sn)]]
      )
    ]))
    error_message = "Los secretos van en minúsculas, números y guiones, y cada secret_env debe apuntar a un secreto declarado."
  }

  validation {
    condition = alltrue([
      for k, v in var.container_apps :
      (length(v.secrets) == 0 || v.key_vault_id != null) &&
      (v.acr == null || contains(["Container Registry Repository Reader", "AcrPull"], try(v.acr.role, "")))
    ])
    error_message = "Los secretos de Key Vault necesitan key_vault_id; acr.role: Container Registry Repository Reader (ABAC) o AcrPull (legacy)."
  }
}

variable "container_app_jobs" {
  description = "Jobs de Container Apps (clave = nombre del job). Programados o manuales."
  type = map(object({
    environment                = string
    resource_group_name        = string
    location                   = string
    workload_profile_name      = optional(string, "Consumption")
    cron_expression            = optional(string) # null = disparo manual
    replica_timeout_in_seconds = optional(number, 1800)
    replica_retry_limit        = optional(number, 1)
    parallelism                = optional(number, 1)

    acr = optional(object({
      server      = string
      registry_id = string
      role        = optional(string, "Container Registry Repository Reader")
    }))
    key_vault_id = optional(string)
    secrets      = optional(map(string), {})
    role_assignments = optional(map(object({
      scope = string
      role  = string
    })), {})

    containers = map(object({
      image      = string
      cpu        = number
      memory     = string
      args       = optional(list(string))
      command    = optional(list(string))
      env        = optional(map(string), {})
      secret_env = optional(map(string), {})
    }))

    tags = optional(map(string), {})
  }))
  default = {}

  validation {
    condition = alltrue(flatten([
      for k, v in var.container_app_jobs : concat(
        [can(regex("^[a-z][a-z0-9-]{0,30}[a-z0-9]$", k))],
        [length(v.secrets) == 0 || v.key_vault_id != null],
        [for c in values(v.containers) : [for sn in values(c.secret_env) : contains(keys(v.secrets), sn)]]
      )
    ]))
    error_message = "Jobs: nombre de 2-32 minúsculas, números y guiones; los secretos necesitan key_vault_id y cada secret_env debe apuntar a un secreto declarado."
  }
}

# -----------------------------------------------------------------------------
# Entorno (submódulo Containers/Containers/modules/container_app_environment)
# El perfil Consumption se declara siempre: un entorno creado sin perfiles no admite añadirlos
# -----------------------------------------------------------------------------
module "cae" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Containers/Containers/modules/container_app_environment?ref=main"
  for_each = var.container_app_environments

  container_app_environment_name     = each.key
  resource_group_name                = each.value.resource_group_name
  location                           = each.value.location
  infrastructure_subnet_id           = each.value.infrastructure_subnet_id
  infrastructure_resource_group_name = each.value.infrastructure_resource_group_name
  internal_load_balancer_enabled     = each.value.internal_load_balancer_enabled
  public_network_access              = each.value.public_network_access
  zone_redundancy_enabled            = each.value.zone_redundancy_enabled
  mutual_tls_enabled                 = each.value.mutual_tls_enabled
  logs_destination                   = "azure-monitor" # diagnostic settings: compatible con Private Link
  workload_profile = concat(
    [{ name = "Consumption", workload_profile_type = "Consumption" }],
    [for pk, p in each.value.dedicated_workload_profiles : merge(p, { name = pk })]
  )
  tags = merge(var.tags, each.value.tags)
}

module "cae_diagnostics" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Security/Seguridad/modules/monitor_diagnostic_setting?ref=main"
  for_each = var.container_app_environments

  monitor_diagnostic_setting_name = "diag-${each.key}"
  target_resource_id              = module.cae[each.key].id
  log_analytics_workspace_id      = each.value.log_analytics_workspace_id
  log_analytics_destination_type  = "Dedicated"
  enabled_logs = concat(
    [{ category = "ContainerAppConsoleLogs" }, { category = "ContainerAppSystemLogs" }],
    each.value.http_logs_enabled ? [{ category = "ContainerAppHTTPLogs" }] : []
  )
  enabled_metrics = [{ category = "AllMetrics" }]
}

# DNS privado del entorno interno: * y @ hacia la IP estática del balanceador interno
resource "azurerm_private_dns_zone" "cae" {
  for_each = { for k, v in var.container_app_environments : k => v if v.private_dns != null }

  name                = module.cae[each.key].default_domain
  resource_group_name = each.value.private_dns.resource_group_name
  tags                = merge(var.tags, each.value.tags)
}

resource "azurerm_private_dns_a_record" "cae" {
  for_each = merge([
    for k, v in var.container_app_environments : {
      for r in ["*", "@"] : "${k}-${r == "*" ? "wildcard" : "apex"}" => { env = k, record = r, rg = v.private_dns.resource_group_name }
    } if v.private_dns != null
  ]...)

  name                = each.value.record
  zone_name           = azurerm_private_dns_zone.cae[each.value.env].name
  resource_group_name = each.value.rg
  ttl                 = 300
  records             = [module.cae[each.value.env].static_ip_address]
}

resource "azurerm_private_dns_zone_virtual_network_link" "cae" {
  for_each = merge([
    for k, v in var.container_app_environments : {
      for lk, vnet in v.private_dns.virtual_network_ids : "${k}-${lk}" => { env = k, vnet = vnet, rg = v.private_dns.resource_group_name }
    } if v.private_dns != null
  ]...)

  name                  = "link-${each.key}"
  resource_group_name   = each.value.rg
  private_dns_zone_name = azurerm_private_dns_zone.cae[each.value.env].name
  virtual_network_id    = each.value.vnet
  registration_enabled  = false
}

module "cae_private_endpoint" {
  source = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Networking/Networking/modules/private_endpoint?ref=main"
  for_each = merge([
    for k, v in var.container_app_environments : {
      for pk, p in v.private_endpoints : "${k}-${pk}" => merge(p, { env = k, rg = v.resource_group_name, location = v.location })
    }
  ]...)

  private_endpoint_name          = "pe-${each.key}"
  custom_network_interface_name  = "nic-pe-${each.key}"
  resource_group_name            = each.value.rg
  location                       = each.value.location
  subnet_id                      = each.value.subnet_id
  private_connection_resource_id = module.cae[each.value.env].id
  subresource_names              = ["managedEnvironments"]
  private_dns_zone_ids           = [each.value.private_dns_zone_id]
  tags                           = merge(var.tags, var.container_app_environments[each.value.env].tags)
}

# -----------------------------------------------------------------------------
# Identidad de usuario por app y por job (módulo PRO/common/assigned_identity)
# -----------------------------------------------------------------------------
module "aca_identity" {
  source = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//PRO/common/assigned_identity?ref=main"
  for_each = merge(
    { for k, v in var.container_apps : "app-${k}" => { name = k, rg = v.resource_group_name, location = var.container_app_environments[v.environment].location, tags = v.tags } },
    { for k, v in var.container_app_jobs : "job-${k}" => { name = k, rg = v.resource_group_name, location = v.location, tags = v.tags } }
  )

  name                = "id-${each.value.name}"
  resource_group_name = each.value.rg
  location            = each.value.location
  tags                = merge(var.tags, each.value.tags)
}

# Permisos ANTES de crear apps y jobs: el pull y la lectura de secretos ocurren al crear la revisión
resource "azurerm_role_assignment" "aca" {
  for_each = merge(concat(
    [
      for k, v in var.container_apps : merge(
        v.acr == null ? {} : { "app-${k}-acr" = { identity = "app-${k}", scope = v.acr.registry_id, role = v.acr.role } },
        v.key_vault_id == null ? {} : { "app-${k}-kv" = { identity = "app-${k}", scope = v.key_vault_id, role = "Key Vault Secrets User" } },
        { for rk, r in v.role_assignments : "app-${k}-${rk}" => { identity = "app-${k}", scope = r.scope, role = r.role } }
      )
    ],
    [
      for k, v in var.container_app_jobs : merge(
        v.acr == null ? {} : { "job-${k}-acr" = { identity = "job-${k}", scope = v.acr.registry_id, role = v.acr.role } },
        v.key_vault_id == null ? {} : { "job-${k}-kv" = { identity = "job-${k}", scope = v.key_vault_id, role = "Key Vault Secrets User" } },
        { for rk, r in v.role_assignments : "job-${k}-${rk}" => { identity = "job-${k}", scope = r.scope, role = r.role } }
      )
    ]
  )...)

  scope                            = each.value.scope
  role_definition_name             = each.value.role
  principal_id                     = module.aca_identity[each.value.identity].principal_id
  principal_type                   = "ServicePrincipal"
  skip_service_principal_aad_check = true
  description                      = "Container Apps ${each.value.identity}"
}

# -----------------------------------------------------------------------------
# Apps (recurso nativo: el submódulo container_app falla con OpenTofu en apps sin ingress)
# -----------------------------------------------------------------------------
resource "azurerm_container_app" "this" {
  for_each = var.container_apps

  name                         = each.key
  resource_group_name          = each.value.resource_group_name
  container_app_environment_id = module.cae[each.value.environment].id
  workload_profile_name        = each.value.workload_profile_name
  revision_mode                = each.value.revision_mode
  max_inactive_revisions       = 10

  identity {
    type         = "UserAssigned"
    identity_ids = [module.aca_identity["app-${each.key}"].id]
  }

  dynamic "registry" {
    for_each = each.value.acr == null ? [] : [each.value.acr]
    content {
      server   = registry.value.server
      identity = module.aca_identity["app-${each.key}"].id
    }
  }

  # Solo referencias a Key Vault: ningún valor secreto en Terraform
  dynamic "secret" {
    for_each = each.value.secrets
    content {
      name                = secret.key
      identity            = module.aca_identity["app-${each.key}"].id
      key_vault_secret_id = secret.value
    }
  }

  dynamic "ingress" {
    for_each = each.value.ingress == null ? [] : [each.value.ingress]
    content {
      target_port                = ingress.value.target_port
      external_enabled           = ingress.value.external_enabled
      transport                  = ingress.value.transport
      client_certificate_mode    = ingress.value.client_certificate_mode
      allow_insecure_connections = false

      dynamic "ip_security_restriction" {
        for_each = ingress.value.allowed_ip_ranges
        content {
          name             = "allow-${ip_security_restriction.key}"
          action           = "Allow"
          ip_address_range = ip_security_restriction.value
        }
      }

      traffic_weight {
        latest_revision = true
        percentage      = 100
      }
    }
  }

  template {
    min_replicas = each.value.min_replicas
    max_replicas = each.value.max_replicas

    dynamic "http_scale_rule" {
      for_each = each.value.http_concurrent_requests == null ? [] : [each.value.http_concurrent_requests]
      content {
        name                = "http"
        concurrent_requests = tostring(http_scale_rule.value)
      }
    }

    dynamic "container" {
      for_each = each.value.containers
      content {
        name    = container.key
        image   = container.value.image
        cpu     = container.value.cpu
        memory  = container.value.memory
        args    = container.value.args
        command = container.value.command

        dynamic "env" {
          for_each = container.value.env
          content {
            name  = env.key
            value = env.value
          }
        }

        dynamic "env" {
          for_each = container.value.secret_env
          content {
            name        = env.key
            secret_name = env.value
          }
        }

        dynamic "liveness_probe" {
          for_each = container.value.probe == null ? [] : [container.value.probe]
          content {
            transport = liveness_probe.value.transport
            port      = liveness_probe.value.port
            path      = liveness_probe.value.path
          }
        }

        dynamic "readiness_probe" {
          for_each = container.value.probe == null ? [] : [container.value.probe]
          content {
            transport = readiness_probe.value.transport
            port      = readiness_probe.value.port
            path      = readiness_probe.value.path
          }
        }

        dynamic "startup_probe" {
          for_each = container.value.probe == null ? [] : [container.value.probe]
          content {
            transport = startup_probe.value.transport
            port      = startup_probe.value.port
            path      = startup_probe.value.path
          }
        }
      }
    }
  }

  tags = merge(var.tags, var.container_app_environments[each.value.environment].tags, each.value.tags)

  depends_on = [azurerm_role_assignment.aca]
}

# -----------------------------------------------------------------------------
# Jobs (submódulo Containers/Containers/modules/container_app_job)
# -----------------------------------------------------------------------------
module "acj" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Containers/Containers/modules/container_app_job?ref=main"
  for_each = var.container_app_jobs

  container_app_job_name       = each.key
  resource_group_name          = each.value.resource_group_name
  location                     = each.value.location
  container_app_environment_id = module.cae[each.value.environment].id
  workload_profile_name        = each.value.workload_profile_name
  replica_timeout_in_seconds   = each.value.replica_timeout_in_seconds
  replica_retry_limit          = each.value.replica_retry_limit

  identity = {
    type         = "UserAssigned"
    identity_ids = [module.aca_identity["job-${each.key}"].id]
  }

  registry = each.value.acr == null ? null : [{
    server   = each.value.acr.server
    identity = module.aca_identity["job-${each.key}"].id
  }]

  secret = length(each.value.secrets) == 0 ? null : [
    for name, id in each.value.secrets : {
      name                = name
      identity            = module.aca_identity["job-${each.key}"].id
      key_vault_secret_id = id
    }
  ]

  schedule_trigger_config = each.value.cron_expression == null ? null : {
    cron_expression          = each.value.cron_expression
    parallelism              = each.value.parallelism
    replica_completion_count = each.value.parallelism
  }
  manual_trigger_config = each.value.cron_expression != null ? null : {
    parallelism              = each.value.parallelism
    replica_completion_count = each.value.parallelism
  }

  template = {
    container = [
      for cn, c in each.value.containers : {
        name    = cn
        image   = c.image
        cpu     = c.cpu
        memory  = c.memory
        args    = c.args
        command = c.command
        env = concat(
          [for n, val in c.env : { name = n, value = val }],
          [for n, s in c.secret_env : { name = n, secret_name = s }]
        )
      }
    ]
  }

  tags = merge(var.tags, var.container_app_environments[each.value.environment].tags, each.value.tags)

  depends_on = [azurerm_role_assignment.aca]
}

# -----------------------------------------------------------------------------
# Comprobaciones (avisos, no bloquean)
# -----------------------------------------------------------------------------
check "zone_redundant_replicas" {
  assert {
    condition = alltrue([
      for k, v in var.container_apps :
      !var.container_app_environments[v.environment].zone_redundancy_enabled || v.min_replicas >= 2
    ])
    error_message = "Hay apps con menos de 2 réplicas mínimas en un entorno con zonas: no se reparten entre zonas."
  }
}

# -----------------------------------------------------------------------------
# Salidas
# -----------------------------------------------------------------------------
output "container_app_environment_ids" {
  description = "ID de cada entorno."
  value       = { for k, v in module.cae : k => v.id }
}

output "container_app_environment_static_ips" {
  description = "IP estática de cada entorno (privada si es interno)."
  value       = { for k, v in module.cae : k => v.static_ip_address }
}

output "container_app_environment_default_domains" {
  description = "Dominio por defecto de cada entorno (nombre de la zona privada en entornos internos)."
  value       = { for k, v in module.cae : k => v.default_domain }
}

output "container_app_fqdns" {
  description = "FQDN de la última revisión de cada app."
  value       = { for k, v in azurerm_container_app.this : k => v.latest_revision_fqdn }
}

output "container_app_identities" {
  description = "Identidad de usuario de cada app y job."
  value       = { for k, v in module.aca_identity : k => { id = v.id, principal_id = v.principal_id } }
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

container_app_environments = {
  "cae-workload-pro-01" = {
    resource_group_name                = "<rg-workload-pro>"
    location                           = "<region>"
    infrastructure_subnet_id           = "<resourceId snet-cae-pro (/24, delegada, con UDR al firewall)>"
    infrastructure_resource_group_name = "<rg-workload-pro-cae-infra>"

    # Entorno interno, sin acceso público, con zonas y cifrado entre apps (valores por defecto)

    dedicated_workload_profiles = {
      d4 = { workload_profile_type = "D4", minimum_count = 0, maximum_count = 3 }
    }

    private_dns = {
      resource_group_name = "<rg-dns-hub>"
      virtual_network_ids = {
        hub   = "<resourceId vnet-hub>"
        spoke = "<resourceId vnet-spoke-workload-pro>"
      }
    }

    log_analytics_workspace_id = "<resourceId log-platform-pro>"
  }
}

container_apps = {
  # API interna detrás de Application Gateway o Front Door
  "ca-workload-api" = {
    environment         = "cae-workload-pro-01"
    resource_group_name = "<rg-workload-pro>"
    min_replicas        = 2
    max_replicas        = 10

    http_concurrent_requests = 50

    ingress = {
      target_port      = 8080
      external_enabled = true # visible en la VNet (el entorno es interno), no en Internet
    }

    acr = {
      server      = "<registro>.azurecr.io"
      registry_id = "<resourceId crworkloadpro01>"
    }

    key_vault_id = "<resourceId kv-workload-pro>"
    secrets = {
      "db-connection" = "https://<kv-workload-pro>.vault.azure.net/secrets/db-connection"
    }

    containers = {
      api = {
        image  = "<registro>.azurecr.io/workload/api:<version>"
        cpu    = 0.5
        memory = "1Gi"
        env = {
          ASPNETCORE_URLS = "http://+:8080"
        }
        secret_env = {
          ConnectionStrings__Default = "db-connection"
        }
        probe = { path = "/healthz", port = 8080 }
      }
    }
  }

  # Worker sin ingress en el perfil dedicado
  "ca-workload-worker" = {
    environment           = "cae-workload-pro-01"
    resource_group_name   = "<rg-workload-pro>"
    workload_profile_name = "d4"
    min_replicas          = 2
    max_replicas          = 4

    acr = {
      server      = "<registro>.azurecr.io"
      registry_id = "<resourceId crworkloadpro01>"
    }

    containers = {
      worker = {
        image  = "<registro>.azurecr.io/workload/worker:<version>"
        cpu    = 2
        memory = "8Gi"
      }
    }
  }
}

container_app_jobs = {
  "caj-workload-nightly" = {
    environment         = "cae-workload-pro-01"
    resource_group_name = "<rg-workload-pro>"
    location            = "<region>"
    cron_expression     = "0 2 * * *" # UTC

    acr = {
      server      = "<registro>.azurecr.io"
      registry_id = "<resourceId crworkloadpro01>"
    }

    containers = {
      job = {
        image  = "<registro>.azurecr.io/workload/job:<version>"
        cpu    = 1
        memory = "2Gi"
      }
    }
  }
}
```

### Despliegue y comprobación

```powershell
terraform init
terraform plan -var-file="env/pro.tfvars" -out="pro.tfplan"
terraform apply "pro.tfplan"

# Configuración del entorno (propiedades de la API)
$cae = Get-AzResource -ResourceGroupName "<rg-workload-pro>" -ResourceType "Microsoft.App/managedEnvironments" -Name "cae-workload-pro-01" -ExpandProperties
[PSCustomObject]@{
    Internal            = $cae.Properties.vnetConfiguration.internal
    ZoneRedundant       = $cae.Properties.zoneRedundant
    PublicNetworkAccess = $cae.Properties.publicNetworkAccess
    PeerEncryption      = $cae.Properties.peerTrafficConfiguration.encryption.enabled
    LogsDestination     = $cae.Properties.appLogsConfiguration.destination
    DefaultDomain       = $cae.Properties.defaultDomain
    StaticIp            = $cae.Properties.staticIp
}

# Resolución privada desde una VM de la red
Resolve-DnsName "ca-workload-api.$($cae.Properties.defaultDomain)"

# Revisiones, registros del sistema y ejecución manual del job
az containerapp revision list --name "ca-workload-api" --resource-group "<rg-workload-pro>" -o table
az containerapp logs show --name "ca-workload-api" --resource-group "<rg-workload-pro>" --type system --tail 50
az containerapp job start --name "caj-workload-nightly" --resource-group "<rg-workload-pro>"
```

Consultas en Log Analytics (tablas de diagnostic settings, sin sufijo `_CL`):

```kusto
ContainerAppConsoleLogs
| where TimeGenerated > ago(1h)
| order by TimeGenerated desc

ContainerAppSystemLogs
| where TimeGenerated > ago(1d)
| order by TimeGenerated desc
```

### Equivalente en Bicep

Un entorno con sus apps y jobs por despliegue. `aca.bicep` usa dos módulos auxiliares: `cae-dns.bicep` para la zona privada (su nombre es el dominio que Azure genera al crear el entorno, así que no puede calcularse al inicio del despliegue) y `role-on-resource.bicep` para asignar roles sobre ACR y Key Vault en otros grupos de recursos.

**`role-on-resource.bicep` actualizado**: además de redes, zonas DNS y ACR, cubre Key Vault, Service Bus, Event Hubs y Storage. Sustituye a la versión de las fichas de AKS y Container Instances.

`aca.bicep`:

```bicep
// =============================================================================
// Entorno de Container Apps interno (workload profiles v2) con zonas, cifrado entre apps,
// sin acceso público, logs por diagnostic settings y DNS privado; apps y jobs con identidad
// de usuario para ACR y secretos como referencias a Key Vault
// DEPENDENCY: subred delegada a Microsoft.App/environments (/27 o mayor) con la salida controlada
// DEPENDENCY: role-on-resource.bicep y cae-dns.bicep en la misma carpeta
// =============================================================================
@minLength(2)
@maxLength(60)
param name string
param location string = resourceGroup().location
param infrastructureSubnetId string
param infrastructureResourceGroup string = ''
param internal bool = true
param zoneRedundant bool = true
param peerEncryption bool = true

@description('[{ name, type: D4|D8|...|E32, minimumCount, maximumCount }]')
param dedicatedWorkloadProfiles array = []

@description('VNets que resuelven el dominio del entorno interno; vacío = sin zona privada')
param privateDnsVirtualNetworkIds array = []

@description('Grupo de recursos de la zona privada (misma suscripción); vacío = el del despliegue')
param privateDnsResourceGroup string = ''

param logAnalyticsWorkspaceId string
param httpLogsEnabled bool = false

@description('[{ name, workloadProfileName?, minReplicas?, maxReplicas?, httpConcurrentRequests?, ingress?: { targetPort, external?, transport?, allowedIpRanges? }, acr?: { server, registryId, role? }, keyVaultId?, secrets?: { nombre: idSecreto }, containers: [{ name, image, cpu, memory, env?: {}, secretEnv?: {}, probe?: { path, port } }] }]')
param apps array = []

@description('[{ name, cronExpression?, replicaTimeout?, replicaRetryLimit?, acr?, keyVaultId?, secrets?, containers }]')
param jobs array = []

param tags object = {}

var roleIds = {
  'Container Registry Repository Reader': 'b93aa761-3e63-49ed-ac28-beffa264f7ac'
  AcrPull: '7f951dda-4ed3-4680-a7ca-43fe172d538d'
  'Key Vault Secrets User': '4633458b-17de-408a-b874-0445c86b69e6'
}

var workloads = concat(
  map(apps, a => union(a, { kind: 'app' })),
  map(jobs, j => union(j, { kind: 'job' }))
)

// Asignaciones previas: ACR y Key Vault por cada app o job
var roleAssignments = flatten(map(
  range(0, length(workloads)),
  i => concat(
    contains(workloads[i], 'acr')
      ? [{ index: i, scope: workloads[i].acr.registryId, role: workloads[i].acr.?role ?? 'Container Registry Repository Reader' }]
      : [],
    contains(workloads[i], 'keyVaultId') ? [{ index: i, scope: workloads[i].keyVaultId, role: 'Key Vault Secrets User' }] : []
  )
))

resource environment 'Microsoft.App/managedEnvironments@2025-07-01' = {
  name: name
  location: location
  tags: tags
  properties: {
    vnetConfiguration: {
      infrastructureSubnetId: infrastructureSubnetId
      internal: internal
    }
    infrastructureResourceGroup: empty(infrastructureResourceGroup) ? null : infrastructureResourceGroup
    zoneRedundant: zoneRedundant
    publicNetworkAccess: 'Disabled'
    peerTrafficConfiguration: {
      encryption: {
        enabled: peerEncryption
      }
    }
    appLogsConfiguration: {
      destination: 'azure-monitor'
    }
    workloadProfiles: concat(
      [
        {
          name: 'Consumption'
          workloadProfileType: 'Consumption'
        }
      ],
      map(dedicatedWorkloadProfiles, p => {
        name: p.name
        workloadProfileType: p.type
        minimumCount: p.minimumCount
        maximumCount: p.maximumCount
      })
    )
  }
}

resource diagnostics 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = {
  name: 'diag-${name}'
  scope: environment
  properties: {
    workspaceId: logAnalyticsWorkspaceId
    logAnalyticsDestinationType: 'Dedicated'
    logs: concat(
      [
        {
          category: 'ContainerAppConsoleLogs'
          enabled: true
        }
        {
          category: 'ContainerAppSystemLogs'
          enabled: true
        }
      ],
      httpLogsEnabled
        ? [
            {
              category: 'ContainerAppHTTPLogs'
              enabled: true
            }
          ]
        : []
    )
    metrics: [
      {
        category: 'AllMetrics'
        enabled: true
      }
    ]
  }
}

// DNS privado del entorno interno (módulo: el nombre de la zona solo se conoce tras crear el entorno)
module dns 'cae-dns.bicep' = if (internal && !empty(privateDnsVirtualNetworkIds)) {
  name: '${take(name, 50)}-dns'
  scope: resourceGroup(empty(privateDnsResourceGroup) ? resourceGroup().name : privateDnsResourceGroup)
  params: {
    defaultDomain: environment.properties.defaultDomain
    staticIp: environment.properties.staticIp
    virtualNetworkIds: privateDnsVirtualNetworkIds
    tags: tags
  }
}

resource identities 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = [
  for w in workloads: {
    name: 'id-${w.name}'
    location: location
    tags: tags
  }
]

module roles 'role-on-resource.bicep' = [
  for (ra, i) in roleAssignments: {
    name: '${take(name, 40)}-role-${i}'
    scope: resourceGroup(split(ra.scope, '/')[2], split(ra.scope, '/')[4])
    params: {
      resourceId: ra.scope
      roleDefinitionId: roleIds[ra.role]
      principalId: identities[ra.index].properties.principalId
      description: 'Container Apps ${workloads[ra.index].name}'
    }
  }
]

resource containerApps 'Microsoft.App/containerApps@2025-07-01' = [
  for (a, i) in apps: {
    name: a.name
    location: location
    tags: tags
    identity: {
      type: 'UserAssigned'
      userAssignedIdentities: {
        '${identities[i].id}': {}
      }
    }
    properties: {
      environmentId: environment.id
      workloadProfileName: a.?workloadProfileName ?? 'Consumption'
      configuration: {
        activeRevisionsMode: 'Single'
        maxInactiveRevisions: 10
        ingress: contains(a, 'ingress')
          ? {
              targetPort: a.ingress.targetPort
              external: a.ingress.?external ?? false
              transport: a.ingress.?transport ?? 'auto'
              allowInsecure: false
              ipSecurityRestrictions: map(
                range(0, length(a.ingress.?allowedIpRanges ?? [])),
                n => { name: 'allow-${n}', action: 'Allow', ipAddressRange: a.ingress.allowedIpRanges[n] }
              )
              traffic: [
                {
                  latestRevision: true
                  weight: 100
                }
              ]
            }
          : null
        registries: contains(a, 'acr') ? [{ server: a.acr.server, identity: identities[i].id }] : []
        secrets: map(items(a.?secrets ?? {}), s => { name: s.key, keyVaultUrl: s.value, identity: identities[i].id })
      }
      template: {
        scale: {
          minReplicas: a.?minReplicas ?? 2
          maxReplicas: a.?maxReplicas ?? 10
          rules: contains(a, 'httpConcurrentRequests')
            ? [{ name: 'http', http: { metadata: { concurrentRequests: string(a.httpConcurrentRequests) } } }]
            : []
        }
        containers: map(a.containers, c => {
          name: c.name
          image: c.image
          resources: {
            cpu: json(string(c.cpu))
            memory: c.memory
          }
          env: concat(
            map(items(c.?env ?? {}), e => { name: e.key, value: e.value }),
            map(items(c.?secretEnv ?? {}), e => { name: e.key, secretRef: e.value })
          )
          probes: contains(c, 'probe')
            ? map(['Liveness', 'Readiness', 'Startup'], t => { type: t, httpGet: { path: c.probe.path, port: c.probe.port } })
            : []
        })
      }
    }
    dependsOn: [
      roles
    ]
  }
]

resource containerJobs 'Microsoft.App/jobs@2025-07-01' = [
  for (j, i) in jobs: {
    name: j.name
    location: location
    tags: tags
    identity: {
      type: 'UserAssigned'
      userAssignedIdentities: {
        '${identities[length(apps) + i].id}': {}
      }
    }
    properties: {
      environmentId: environment.id
      workloadProfileName: j.?workloadProfileName ?? 'Consumption'
      configuration: {
        triggerType: contains(j, 'cronExpression') ? 'Schedule' : 'Manual'
        replicaTimeout: j.?replicaTimeout ?? 1800
        replicaRetryLimit: j.?replicaRetryLimit ?? 1
        scheduleTriggerConfig: contains(j, 'cronExpression')
          ? {
              cronExpression: j.cronExpression
              parallelism: 1
              replicaCompletionCount: 1
            }
          : null
        manualTriggerConfig: contains(j, 'cronExpression')
          ? null
          : {
              parallelism: 1
              replicaCompletionCount: 1
            }
        registries: contains(j, 'acr') ? [{ server: j.acr.server, identity: identities[length(apps) + i].id }] : []
        secrets: map(items(j.?secrets ?? {}), s => { name: s.key, keyVaultUrl: s.value, identity: identities[length(apps) + i].id })
      }
      template: {
        containers: map(j.containers, c => {
          name: c.name
          image: c.image
          resources: {
            cpu: json(string(c.cpu))
            memory: c.memory
          }
          env: concat(
            map(items(c.?env ?? {}), e => { name: e.key, value: e.value }),
            map(items(c.?secretEnv ?? {}), e => { name: e.key, secretRef: e.value })
          )
        })
      }
    }
    dependsOn: [
      roles
    ]
  }
]

output environmentId string = environment.id
output staticIp string = environment.properties.staticIp
output defaultDomain string = environment.properties.defaultDomain
```

`cae-dns.bicep`:

```bicep
// =============================================================================
// Zona privada del dominio por defecto de un entorno interno de Container Apps:
// registros * y @ hacia la IP estática y enlaces a las VNets que resuelven
// =============================================================================
param defaultDomain string
param staticIp string
param virtualNetworkIds array
param tags object = {}

resource zone 'Microsoft.Network/privateDnsZones@2024-06-01' = {
  name: defaultDomain
  location: 'global'
  tags: tags
}

resource records 'Microsoft.Network/privateDnsZones/A@2024-06-01' = [
  for r in ['*', '@']: {
    parent: zone
    name: r
    properties: {
      ttl: 300
      aRecords: [
        {
          ipv4Address: staticIp
        }
      ]
    }
  }
]

resource links 'Microsoft.Network/privateDnsZones/virtualNetworkLinks@2024-06-01' = [
  for (vnetId, i) in virtualNetworkIds: {
    parent: zone
    name: 'link-${i}-${last(split(vnetId, '/'))}'
    location: 'global'
    tags: tags
    properties: {
      registrationEnabled: false
      virtualNetwork: {
        id: vnetId
      }
    }
  }
]
```

`role-on-resource.bicep`:

```bicep
// =============================================================================
// Asigna un rol sobre un recurso de otro grupo de recursos. Se despliega con scope en el grupo
// de recursos del destino. Tipos soportados: subred, VNet, tabla de rutas, zona DNS privada,
// Container Registry, Key Vault, Service Bus, Event Hubs y Storage account.
// Cualquier otro tipo NO asigna nada: añadirlo aquí antes de usarlo.
// =============================================================================
param resourceId string
param roleDefinitionId string
param principalId string
param description string = ''

var segments = split(resourceId, '/')
var type = toLower('${segments[6]}/${segments[7]}')
var isSubnet = type == 'microsoft.network/virtualnetworks' && length(segments) > 10
var isVnet = type == 'microsoft.network/virtualnetworks' && length(segments) <= 10
var isRouteTable = type == 'microsoft.network/routetables'
var isDnsZone = type == 'microsoft.network/privatednszones'
var isRegistry = type == 'microsoft.containerregistry/registries'
var isKeyVault = type == 'microsoft.keyvault/vaults'
var isServiceBus = type == 'microsoft.servicebus/namespaces'
var isEventHub = type == 'microsoft.eventhub/namespaces'
var isStorage = type == 'microsoft.storage/storageaccounts'
var roleId = subscriptionResourceId('Microsoft.Authorization/roleDefinitions', roleDefinitionId)

resource subnet 'Microsoft.Network/virtualNetworks/subnets@2024-05-01' existing = if (isSubnet) {
  name: isSubnet ? '${segments[8]}/${segments[10]}' : 'none/none'
}

resource vnet 'Microsoft.Network/virtualNetworks@2024-05-01' existing = if (isVnet) {
  name: segments[8]
}

resource routeTable 'Microsoft.Network/routeTables@2024-05-01' existing = if (isRouteTable) {
  name: segments[8]
}

resource dnsZone 'Microsoft.Network/privateDnsZones@2024-06-01' existing = if (isDnsZone) {
  name: segments[8]
}

resource registry 'Microsoft.ContainerRegistry/registries@2025-11-01' existing = if (isRegistry) {
  name: segments[8]
}

resource keyVault 'Microsoft.KeyVault/vaults@2023-07-01' existing = if (isKeyVault) {
  name: segments[8]
}

resource serviceBus 'Microsoft.ServiceBus/namespaces@2024-01-01' existing = if (isServiceBus) {
  name: segments[8]
}

resource eventHub 'Microsoft.EventHub/namespaces@2024-01-01' existing = if (isEventHub) {
  name: segments[8]
}

resource storage 'Microsoft.Storage/storageAccounts@2023-05-01' existing = if (isStorage) {
  name: segments[8]
}

resource onSubnet 'Microsoft.Authorization/roleAssignments@2022-04-01' = if (isSubnet) {
  name: guid(resourceId, principalId, roleDefinitionId)
  scope: subnet
  properties: {
    roleDefinitionId: roleId
    principalId: principalId
    principalType: 'ServicePrincipal'
    description: description
  }
}

resource onVnet 'Microsoft.Authorization/roleAssignments@2022-04-01' = if (isVnet) {
  name: guid(resourceId, principalId, roleDefinitionId)
  scope: vnet
  properties: {
    roleDefinitionId: roleId
    principalId: principalId
    principalType: 'ServicePrincipal'
    description: description
  }
}

resource onRouteTable 'Microsoft.Authorization/roleAssignments@2022-04-01' = if (isRouteTable) {
  name: guid(resourceId, principalId, roleDefinitionId)
  scope: routeTable
  properties: {
    roleDefinitionId: roleId
    principalId: principalId
    principalType: 'ServicePrincipal'
    description: description
  }
}

resource onDnsZone 'Microsoft.Authorization/roleAssignments@2022-04-01' = if (isDnsZone) {
  name: guid(resourceId, principalId, roleDefinitionId)
  scope: dnsZone
  properties: {
    roleDefinitionId: roleId
    principalId: principalId
    principalType: 'ServicePrincipal'
    description: description
  }
}

resource onRegistry 'Microsoft.Authorization/roleAssignments@2022-04-01' = if (isRegistry) {
  name: guid(resourceId, principalId, roleDefinitionId)
  scope: registry
  properties: {
    roleDefinitionId: roleId
    principalId: principalId
    principalType: 'ServicePrincipal'
    description: description
  }
}

resource onKeyVault 'Microsoft.Authorization/roleAssignments@2022-04-01' = if (isKeyVault) {
  name: guid(resourceId, principalId, roleDefinitionId)
  scope: keyVault
  properties: {
    roleDefinitionId: roleId
    principalId: principalId
    principalType: 'ServicePrincipal'
    description: description
  }
}

resource onServiceBus 'Microsoft.Authorization/roleAssignments@2022-04-01' = if (isServiceBus) {
  name: guid(resourceId, principalId, roleDefinitionId)
  scope: serviceBus
  properties: {
    roleDefinitionId: roleId
    principalId: principalId
    principalType: 'ServicePrincipal'
    description: description
  }
}

resource onEventHub 'Microsoft.Authorization/roleAssignments@2022-04-01' = if (isEventHub) {
  name: guid(resourceId, principalId, roleDefinitionId)
  scope: eventHub
  properties: {
    roleDefinitionId: roleId
    principalId: principalId
    principalType: 'ServicePrincipal'
    description: description
  }
}

resource onStorage 'Microsoft.Authorization/roleAssignments@2022-04-01' = if (isStorage) {
  name: guid(resourceId, principalId, roleDefinitionId)
  scope: storage
  properties: {
    roleDefinitionId: roleId
    principalId: principalId
    principalType: 'ServicePrincipal'
    description: description
  }
}
```

`cae-workload-pro-01.bicepparam`:

```bicep
using 'aca.bicep'

param name = 'cae-workload-pro-01'
param infrastructureSubnetId = '<resourceId snet-cae-pro (/24, delegada, con UDR al firewall)>'
param infrastructureResourceGroup = '<rg-workload-pro-cae-infra>'

param dedicatedWorkloadProfiles = [
  { name: 'd4', type: 'D4', minimumCount: 0, maximumCount: 3 }
]

param privateDnsResourceGroup = '<rg-dns-hub>'
param privateDnsVirtualNetworkIds = [
  '<resourceId vnet-hub>'
  '<resourceId vnet-spoke-workload-pro>'
]

param logAnalyticsWorkspaceId = '<resourceId log-platform-pro>'

param apps = [
  {
    name: 'ca-workload-api'
    minReplicas: 2
    maxReplicas: 10
    httpConcurrentRequests: 50
    ingress: { targetPort: 8080, external: true }
    acr: { server: '<registro>.azurecr.io', registryId: '<resourceId crworkloadpro01>' }
    keyVaultId: '<resourceId kv-workload-pro>'
    secrets: {
      'db-connection': 'https://<kv-workload-pro>.vault.azure.net/secrets/db-connection'
    }
    containers: [
      {
        name: 'api'
        image: '<registro>.azurecr.io/workload/api:<version>'
        cpu: '0.5'
        memory: '1Gi'
        env: { ASPNETCORE_URLS: 'http://+:8080' }
        secretEnv: { ConnectionStrings__Default: 'db-connection' }
        probe: { path: '/healthz', port: 8080 }
      }
    ]
  }
  {
    name: 'ca-workload-worker'
    workloadProfileName: 'd4'
    minReplicas: 2
    maxReplicas: 4
    acr: { server: '<registro>.azurecr.io', registryId: '<resourceId crworkloadpro01>' }
    containers: [
      { name: 'worker', image: '<registro>.azurecr.io/workload/worker:<version>', cpu: '2', memory: '8Gi' }
    ]
  }
]

param jobs = [
  {
    name: 'caj-workload-nightly'
    cronExpression: '0 2 * * *'
    acr: { server: '<registro>.azurecr.io', registryId: '<resourceId crworkloadpro01>' }
    containers: [
      { name: 'job', image: '<registro>.azurecr.io/workload/job:<version>', cpu: '1', memory: '2Gi' }
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
New-AzResourceGroupDeployment -ResourceGroupName "<rg-workload-pro>" `
    -TemplateParameterFile "cae-workload-pro-01.bicepparam" -Name "cae-workload-pro-01"
```

## Errores típicos

| Síntoma | Causa | Solución |
|---|---|---|
| `Invalid for_each argument` (valor sensible) en `Containers/ContainerAppEnvironment` | Variables `sensitive` recorridas con `for_each` | Submódulo `container_app_environment` |
| `Invalid dynamic for_each value` en `Containers/ContainerApp` | Variable `secrets` sensible en `for_each` | Recurso nativo |
| `Attempt to index null value` en el submódulo `container_app` | App sin ingress | Recurso nativo |
| La subred se rechaza | Menor de /27, sin delegar a `Microsoft.App/environments` o compartida | Subred exclusiva, /27 o mayor y delegada |
| Despliegues que fallan por falta de IPs | En modo Single las IPs se duplican durante el cambio de revisión | Subred mayor (no se amplía: nuevo entorno) |
| No se puede crear el private endpoint | Subred delegada o acceso público activado | Subred no delegada y `public_network_access = Disabled` (validado) |
| Las apps no resuelven con entorno interno | Falta la zona del dominio por defecto o el enlace a la VNet | Bloque `private_dns` |
| El entorno o las revisiones fallan tras activar el UDR | El firewall bloquea MCR, AKS, ACR, Key Vault o identidad | Reglas de aplicación de la documentación |
| `Authorization failed` con Key Vault | Falta Key Vault Secrets User o la asignación aún se propaga (hasta 10 minutos) | Rol en el vault y reintentar |
| Key Vault deniega por firewall | El vault no es accesible desde el entorno | Private endpoint del vault en la VNet |
| Variable de entorno vacía | La referencia no coincide con el nombre del secreto (distingue mayúsculas) | Validación del root |
| El valor antiguo del secreto persiste | Cambiar un secreto no crea revisión | Reiniciar la revisión; con URI sin versión, hasta 30 minutos |
| La imagen no se descarga | Rol que no aplica al modo del registro o ACR inaccesible | `Container Registry Repository Reader` en ABAC y red hacia el ACR |
| Error de CPU y memoria | Combinación no válida en Consumption | CPU de 0,25 a 4 y memoria al doble (validado) |
| No se puede activar la redundancia de zona | Solo al crear el entorno | Nuevo entorno y volver a desplegar |
| Una app cae con una zona | Una sola réplica mínima | `min_replicas` de 2 o más (aviso del `check`) |
| El plan quiere recrear el entorno al añadir perfiles | Se creó sin `workload_profile` | El root declara siempre `Consumption` desde el principio |
| El entorno ha desaparecido | Inactivo o fallido durante más de 90 días | Mantener una app o job activo y vigilar el estado |
| No hay registros en Log Analytics con Private Link | El destino `log-analytics` no admite Private Link | `azure-monitor` + diagnostic settings (lo que aplica el root) |
