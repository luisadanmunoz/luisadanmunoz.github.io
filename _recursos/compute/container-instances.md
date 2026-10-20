---
title: "Container Instances"
indice: compute
resumen: "Un contenedor en marcha en segundos."
estado: documentado   # proximamente | en-curso | documentado
orden: 5
last_review: 2026-10-20
fuentes:
  - titulo: "What is Azure Container Instances?"
    url: https://learn.microsoft.com/azure/container-instances/container-instances-overview
  - titulo: "Container groups in Azure Container Instances"
    url: https://learn.microsoft.com/azure/container-instances/container-instances-container-groups
  - titulo: "Resource availability and quota limits for ACI"
    url: https://learn.microsoft.com/azure/container-instances/container-instances-resource-and-quota-limits
  - titulo: "Best practices and considerations for Azure Container Instances"
    url: https://learn.microsoft.com/azure/container-instances/container-instances-best-practices-and-considerations
  - titulo: "Frequently asked questions about Azure Container Instances"
    url: https://learn.microsoft.com/azure/container-instances/container-instances-faq
  - titulo: "Reliability in Azure Container Instances"
    url: https://learn.microsoft.com/azure/reliability/reliability-container-instances
  - titulo: "About NGroups (Preview)"
    url: https://learn.microsoft.com/azure/container-instances/container-instance-ngroups/container-instances-about-ngroups
  - titulo: "Standby pools for Azure Container Instances"
    url: https://learn.microsoft.com/azure/container-instances/container-instances-standby-pool-overview
  - titulo: "Spot container groups in Azure Container Instances"
    url: https://learn.microsoft.com/azure/container-instances/container-instances-spot-containers-overview
  - titulo: "Confidential containers on Azure Container Instances"
    url: https://learn.microsoft.com/azure/container-instances/container-instances-confidential-overview
  - titulo: "Virtual network scenarios and resources for Azure Container Instances"
    url: https://learn.microsoft.com/azure/container-instances/container-instances-virtual-network-concepts
  - titulo: "Deploy container instances into an Azure virtual network"
    url: https://learn.microsoft.com/azure/container-instances/container-instances-vnet
  - titulo: "Configure a NAT gateway for static IP address for outbound traffic from a container group"
    url: https://learn.microsoft.com/azure/container-instances/container-instances-nat-gateway
  - titulo: "Deploy an ACI container group with DNS name reuse policy"
    url: https://learn.microsoft.com/azure/container-instances/how-to-reuse-dns-names
  - titulo: "Use managed identities with Azure Container Instances"
    url: https://learn.microsoft.com/azure/container-instances/container-instances-managed-identity
  - titulo: "Deploy to Azure Container Instances from Azure Container Registry using a managed identity"
    url: https://learn.microsoft.com/azure/container-instances/using-azure-container-registry-mi
  - titulo: "Set environment variables in container instances"
    url: https://learn.microsoft.com/azure/container-instances/container-instances-environment-variables
  - titulo: "Mount a secret volume in Azure Container Instances"
    url: https://learn.microsoft.com/azure/container-instances/container-instances-volume-secret
  - titulo: "Mount an Azure file share in Azure Container Instances"
    url: https://learn.microsoft.com/azure/container-instances/container-instances-volume-azure-files
  - titulo: "Encrypt deployment data"
    url: https://learn.microsoft.com/azure/container-instances/container-instances-encrypt-data
  - titulo: "Security considerations for Azure Container Instances"
    url: https://learn.microsoft.com/azure/container-instances/container-instances-image-security
  - titulo: "Azure security baseline for Container Instances"
    url: https://learn.microsoft.com/security/benchmark/azure/baselines/container-instances-security-baseline
  - titulo: "Azure Policy built-in definitions for Azure Container Instances"
    url: https://learn.microsoft.com/azure/container-instances/policy-reference
  - titulo: "Run containerized tasks with restart policies"
    url: https://learn.microsoft.com/azure/container-instances/container-instances-restart-policy
  - titulo: "Manually stop or start containers in Azure Container Instances"
    url: https://learn.microsoft.com/azure/container-instances/container-instances-stop-start
  - titulo: "Azure Container Instances states"
    url: https://learn.microsoft.com/azure/container-instances/container-state
  - titulo: "Container group and instance logging with Azure Monitor logs"
    url: https://learn.microsoft.com/azure/container-instances/container-instances-log-analytics
  - titulo: "Container Instances monitoring data reference"
    url: https://learn.microsoft.com/azure/container-instances/monitor-azure-container-instances-reference
  - titulo: "Troubleshoot common issues in Azure Container Instances"
    url: https://learn.microsoft.com/azure/container-instances/container-instances-troubleshooting
  - titulo: "Deploy container instances that use GPU resources (retirado)"
    url: https://learn.microsoft.com/azure/container-instances/container-instances-gpu
  - titulo: "azurerm_container_group"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/container_group
  - titulo: "Microsoft.ContainerInstance containerGroups (plantillas ARM/Bicep)"
    url: https://learn.microsoft.com/azure/templates/microsoft.containerinstance/containergroups
  - titulo: "Módulo Terraform Containers/ContainerInstance"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Containers/ContainerInstance
  - titulo: "Módulo Terraform PRO/common/assigned_identity"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/PRO/common/assigned_identity
  - titulo: "Módulo Terraform Security/Seguridad/modules/monitor_diagnostic_setting"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Security/Seguridad/modules/monitor_diagnostic_setting
---

**Azure Container Instances (ACI)** ejecuta contenedores Linux o Windows sin gestionar máquinas virtuales ni un orquestador: se define un **grupo de contenedores** (uno o varios contenedores que comparten host, red, almacenamiento y ciclo de vida), arranca en segundos y se paga por segundo de vCPU y memoria. Es la pieza más simple de la familia de contenedores de Azure; por eso conviene saber bien dónde termina. Las imágenes salen de [Container Registry](/recursos/compute/container-registry/).

## Qué es y cuándo usarlo

### ACI frente a las alternativas

| Necesidad | Servicio |
|---|---|
| Un contenedor o una tarea puntual (build, test, migración, procesado por lotes) sin orquestación | **ACI** |
| Sidecars en el mismo host (logging, proxy) junto a la aplicación | **ACI** (grupo multicontenedor, solo Linux) |
| Microservicios, APIs con escalado automático (también a cero), revisiones, ingress gestionado y trabajos programados | [Container Apps](/recursos/compute/container-apps/) |
| Plataforma Kubernetes completa | [AKS](/recursos/compute/aks/) (puede ráfagas en ACI con virtual nodes) |

ACI **no escala solo**: para más instancias hay que crear más grupos por API, usar NGroups (preview) o pasar a Container Apps o AKS.

### Opciones del servicio

| Opción | Para qué | Limitaciones |
|---|---|---|
| **Standard** | Uso general | Hasta 31 vCPU y 240 GB por grupo (más de 4 vCPU o 16 GB depende de capacidad regional) |
| **Confidential** | Datos en uso protegidos en un entorno de ejecución de confianza (TEE) | Sin zonas de disponibilidad; hasta 31 vCPU y 180 GB |
| **Spot** (preview) | Cargas interrumpibles con hasta un **70 % de descuento** | Solo East US 2, West Europe y West US; hasta 4 vCPU y 16 GB; sin red virtual ni zonas |
| **NGroups** (preview) | Mantener N grupos, actualizaciones progresivas, varias zonas y balanceador | En preview |
| **Standby pools** | Grupos preaprovisionados para arranques casi inmediatos | No dan resiliencia de zona; sin soporte en el portal |
| GPU | — | **Retirado el 14 de julio de 2025**: usar AKS |

Requisitos comunes: imágenes **x64** (no Arm64), de **15 GB como máximo**, y un mínimo de **1 vCPU y 1 GB por grupo** (los contenedores de dentro pueden pedir menos).

### Linux y Windows

| Capacidad | Linux | Windows |
|---|---|---|
| Varios contenedores por grupo | Sí | No |
| Volúmenes (Azure Files, emptyDir, secret, gitRepo) | Sí | No |
| Métricas de uso en Azure Monitor | Sí | No |
| Identidad administrada | Sí | Sí, pero **no puede obtener tokens dentro de una red virtual** |

### Red

| Modo | Uso | Detalles |
|---|---|---|
| **Private** (subred delegada) | Producción | Subred delegada a `Microsoft.ContainerInstance/containerGroups`, recomendada **/24** o mayor y **solo para grupos de contenedores** (ni siquiera private endpoints). **La única salida soportada es un NAT Gateway**. Los contenedores **no heredan el DNS de la VNet**: hay que declararlo. Sin IPv6 ni peering global; el portal necesita el puerto 19390 abierto para conectarse |
| Public | Demostraciones o endpoints públicos detrás de otra protección | FQDN `<etiqueta>.<región>.azurecontainer.io`; con política de reutilización distinta de `Unsecure` se añade un hash que evita el secuestro del subdominio |
| None | Tareas que no reciben tráfico | Obligatorio para Spot |

La IP del grupo **puede cambiar al reiniciarse**: para una IP fija de entrada, Application Gateway; de salida, NAT Gateway. ACI reserva los puertos 22, 1025-1027, 3389-3399, 9999, 19000, 19080, 19100, 19390, 20000-30000 y 49152-65534.

### Seguridad

| Control | Recomendación |
|---|---|
| Registro | Privado (ACR) con pull por **identidad de usuario**; ACI no admite el pull de ACR con identidad de sistema |
| Secretos | `secureValue` en variables de entorno (no se muestran en las propiedades) o volúmenes `secret` (tmpfs en RAM, solo lectura, solo Linux); los valores, desde Key Vault |
| Identidad en ejecución | Identidad administrada para Key Vault, Storage y demás servicios con Entra ID |
| Red | Subred delegada; nada de IP pública en producción |
| Cifrado | AES-256 con claves de Microsoft siempre; **CMK** opcional en Key Vault con soft delete y purge protection |
| Contenedores | Sin operaciones privilegiadas; TLS 1.2 obligatorio para conexiones seguras |
| Imágenes | Escaneo con Defender en el registro |
| Gobierno | Directivas integradas: CMK, red privada y diagnóstico a Log Analytics |

**Azure Files obliga a usar la clave de la storage account**: SMB no admite montar con identidad administrada. La clave da acceso total al share, así que hay que tratarla como secreto y, si la salida está bloqueada, añadir un service endpoint de Storage en la subred.

### Monitorización

| Integración | Cómo | Valoración |
|---|---|---|
| **Diagnostic settings** | Categorías `ContainerInstanceLog` y `ContainerEvent` a tablas estándar | **Recomendada**: sin clave del workspace, compatible con private endpoints. En el portal figura como vista previa y aplicarla **reinicia el grupo** |
| Integración heredada | ID y **clave** del workspace en el propio grupo; tablas `_CL` | Exige workspace público y autenticación local activa |

### Cómo se factura

| Concepto | Detalle |
|---|---|
| Cómputo | Por segundo de vCPU y GB de memoria solicitados mientras el grupo se ejecuta |
| Parada | `Stop` libera los recursos y **detiene la facturación**; no conserva el estado |
| Tareas | Con `OnFailure` o `Never`, solo se paga mientras dura la ejecución |
| Spot | Hasta un 70 % más barato, con desalojos posibles |
| Red | NAT Gateway, IPs públicas y tráfico, aparte |
| Zonas | Sin coste extra |

### Qué escenario recomiendo

| Escenario del cliente | Diseño | Por qué |
|---|---|---|
| Tarea programada o por evento (ETL, migración, informe) | ACI privado con `OnFailure` disparado desde Logic Apps, Functions o el pipeline; o Container Apps jobs si se quiere programación integrada | Se paga solo la ejecución |
| Agentes de build o runners efímeros | ACI privado con NAT Gateway | Arranque en segundos y acceso a recursos privados |
| API o servicio permanente | **Container Apps** | ACI no escala solo, no tiene ingress gestionado y su IP cambia |
| Ráfagas desde AKS | Virtual nodes sobre ACI | Pods sin esperar a que escale el clúster |
| Procesado interrumpible en las regiones soportadas | Spot | Hasta un 70 % menos |
| Datos sensibles en memoria | SKU Confidential | Protección por hardware |
| GPU | AKS | GPU en ACI retirado |

### Datos que conviene llevar a la reunión

- **ACI no escala automáticamente**: para servicios, Container Apps.
- **En una VNet, la única salida soportada es NAT Gateway**, y no hay IP pública ni FQDN.
- **La IP cambia en cada reinicio**, también por mantenimiento de la plataforma.
- **El pull de ACR solo funciona con identidad de usuario.**
- **Windows**: un contenedor por grupo, sin volúmenes y sin tokens de identidad dentro de una VNet.
- **Azure Files exige la clave de la storage account.**
- **GPU en ACI está retirado** (julio de 2025).
- **Spot y NGroups siguen en preview.**

## Decisiones de diseño

| Decisión | Lo que aplico | Por qué |
|---|---|---|
| Recurso | `azurerm_container_group` nativo | El módulo del repositorio no monta volúmenes y su validación falla sin identidad |
| Red | `Private` por defecto con subred obligatoria; `Public` exige política de reutilización distinta de `Unsecure` | Sin exposición y sin secuestro de subdominios |
| DNS | Servidores DNS explícitos | ACI no hereda el DNS de la VNet |
| Puertos | Se exponen solo los de los contenedores; los reservados se rechazan | Superficie mínima y sin comportamientos inesperados |
| Identidad | Una identidad de usuario por grupo (módulo `PRO/common/assigned_identity`) con sus roles creados **antes** que el grupo | El pull ocurre al crear el grupo |
| ACR | `Container Registry Repository Reader` (registro ABAC) o `AcrPull` | Coherente con la ficha de ACR |
| Secretos | Variable aparte, `sensitive`, rellenada desde Key Vault por el pipeline; nunca en `tfvars` | Sin secretos en el repositorio ni en el estado visible del plan |
| Volúmenes | Cada montaje lleva su origen; `secret` siempre de solo lectura; precondición que exige el valor | El provider exige exactamente un origen por volumen |
| Sondas | Liveness y readiness HTTP o exec | Reinicio y tráfico solo con el contenedor sano |
| Zonas | Una zona opcional (Standard, no Spot) | La resiliencia de zona exige varios grupos o NGroups |
| CMK | Opcional, con la identidad del grupo | Requisito regulatorio |
| Diagnóstico | `ContainerInstanceLog` y `ContainerEvent` en tablas dedicadas y métricas | Sin clave del workspace |
| Bloqueo | Desactivado por defecto | Casi todos los cambios recrean el grupo y el bloqueo lo impediría |

Alineación con el Well-Architected Framework:

- **Fiabilidad**: sondas, zona opcional y la recomendación de varios grupos detrás de un balanceador para servicios.
- **Seguridad**: red privada, identidad sin credenciales, secretos fuera del código, CMK y diagnóstico.
- **Coste**: pago por segundo, tareas con `OnFailure` y Spot.
- **Excelencia operativa**: IaC con validaciones de las restricciones de la plataforma.
- **Rendimiento**: imágenes pequeñas en un ACR de la misma región y standby pools si el arranque es crítico.

## Módulo de Terraform

### El módulo del repositorio

[`Containers/ContainerInstance`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Containers/ContainerInstance) valida con azurerm 4.81, pero tiene fallos que impiden usarlo en producción:

| Problema | Efecto |
|---|---|
| La variable `volumes` se declara y **no se usa**; los montajes de los contenedores solo llevan nombre y ruta | El provider exige exactamente un origen por volumen (emptyDir, secret, gitRepo o Azure Files): los montajes no funcionan |
| La validación de `identity` lee `var.identity.type` aunque `identity` sea null | **Falla con OpenTofu** cuando no se pasa identidad (comprobado con 1.8) |
| `dns_name_label_reuse_policy = "Unsecure"` por defecto | Expuesto al secuestro del subdominio |
| `image_registry_credential.password` y `diagnostics.workspace_key` sin `sensitive` | Credenciales en claro en las variables; además, la integración de logs depende de la clave del workspace |
| Usa `count` y `locals`, y construye el nombre con `environment` | No encaja con el patrón de mapas |
| `versions.tf` admite azurerm `>= 3.70.0` | No probado con 3.x |

Reutilizo [`PRO/common/assigned_identity`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/PRO/common/assigned_identity) para la identidad del grupo y [`Security/Seguridad/modules/monitor_diagnostic_setting`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Security/Seguridad/modules/monitor_diagnostic_setting) para el diagnóstico.

Notas del provider (azurerm 4.81):

- **Casi todos los argumentos fuerzan la recreación** del grupo.
- `http_get.scheme` debe ir en minúsculas (`http` o `https`): la documentación dice `Http`, pero el schema lo rechaza (comprobado).
- `key_vault_key_id` exige la **versión** de la clave.
- `subnet_ids` admite una sola subred.
- Las notas del provider sobre "sin identidad administrada en VNet" y "sin Windows en VNet" no coinciden con la documentación actual de Microsoft, que documenta el pull de ACR con identidad en VNet y la VNet para Linux y Windows. Lo que sí confirma Microsoft es que Windows no obtiene tokens de identidad dentro de una VNet.

### Estructura en el proyecto

```txt
/
├── providers.tf          # azurerm >= 4.81.0
├── container_groups.tf   # identidad, roles, grupo de contenedores, diagnóstico, bloqueo
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
      # Validado con 4.81.0 (azurerm_container_group con zones, key_vault_user_assigned_identity_id
      # y dns_name_label_reuse_policy).
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

### `container_groups.tf`

```hcl
# =============================================================================
# Azure Container Instances seguro por defecto:
# grupo de contenedores privado en una subred delegada, identidad de usuario para descargar
# de ACR sin credenciales y para acceder a otros servicios, secretos fuera del código
# (variables seguras, volúmenes secretos), sondas, CMK opcional, zona opcional
# y registros por diagnostic settings (sin clave del workspace)
#
# DEPENDENCY: grupos de recursos creados
# DEPENDENCY: modo Private: subred delegada a Microsoft.ContainerInstance/containerGroups,
#             recomendada /24 o mayor y sin otros recursos (ni private endpoints)
# DEPENDENCY: modo Private: NAT Gateway asociado a la subred (única salida soportada en VNet)
#             y DNS explícito (los contenedores no heredan el DNS de la VNet)
# DEPENDENCY: ACR: registro con acceso desde la red del grupo y con la excepción de servicios
#             de confianza (AzureServices) si es privado; private endpoint en OTRA subred
# DEPENDENCY: Azure Files: storage account y share creados, service endpoint de Storage en la
#             subred si la salida está bloqueada; la clave llega por variable sensible
# DEPENDENCY: CMK: clave en Key Vault con soft delete y purge protection
# DEPENDENCY: la identidad de Terraform necesita permisos para asignar roles en ACR y en los
#             ámbitos de role_assignments (RBAC Administrator o User Access Administrator)
# =============================================================================

variable "container_groups" {
  description = "Grupos de contenedores (clave = nombre del grupo)."
  type = map(object({
    resource_group_name = string
    location            = string
    os_type             = optional(string, "Linux")    # Linux | Windows
    sku                 = optional(string, "Standard") # Standard | Confidential
    priority            = optional(string, "Regular")  # Regular | Spot (preview, sin red ni zonas)
    restart_policy      = optional(string, "Always")   # Always (servicio) | OnFailure | Never (tareas)
    zone                = optional(string)             # una zona; solo Standard y Regular

    network = optional(object({
      mode                        = optional(string, "Private") # Private | Public | None
      subnet_id                   = optional(string)
      dns_servers                 = optional(list(string), []) # obligatorio en Private si se resuelven nombres privados
      dns_search_domains          = optional(list(string), [])
      dns_name_label              = optional(string)                # solo Public
      dns_name_label_reuse_policy = optional(string, "TenantReuse") # nunca Unsecure
    }), {})

    # Identidad de usuario creada por el root (pull de ACR y acceso a servicios)
    identity_enabled           = optional(bool, true)
    user_assigned_identity_ids = optional(list(string), []) # identidades adicionales existentes

    acr = optional(object({
      server      = string # <registro>.azurecr.io
      registry_id = string
      role        = optional(string, "Container Registry Repository Reader") # ABAC; AcrPull en modo legacy
    }))

    # Roles extra para la identidad del grupo (Key Vault, Storage, Service Bus...)
    role_assignments = optional(map(object({
      scope = string
      role  = string
    })), {})

    containers = map(object({
      image        = string
      cpu          = number
      memory       = number # GB
      cpu_limit    = optional(number)
      memory_limit = optional(number)
      ports = optional(list(object({
        port     = number
        protocol = optional(string, "TCP")
      })), [])
      commands              = optional(list(string))
      environment_variables = optional(map(string), {})
      volume_mounts = optional(map(object({ # clave = nombre del volumen
        mount_path = string
        read_only  = optional(bool, false)
      })), {})
      liveness_probe = optional(object({
        exec                  = optional(list(string))
        http_path             = optional(string)
        http_port             = optional(number)
        http_scheme           = optional(string, "http") # http | https (el schema exige minúsculas)
        initial_delay_seconds = optional(number, 10)
        period_seconds        = optional(number, 10)
        failure_threshold     = optional(number, 3)
        timeout_seconds       = optional(number, 5)
      }))
      readiness_probe = optional(object({
        exec                  = optional(list(string))
        http_path             = optional(string)
        http_port             = optional(number)
        http_scheme           = optional(string, "http") # http | https (el schema exige minúsculas)
        initial_delay_seconds = optional(number, 5)
        period_seconds        = optional(number, 10)
        failure_threshold     = optional(number, 3)
        timeout_seconds       = optional(number, 5)
      }))
    }))

    init_containers = optional(map(object({
      image                 = string
      commands              = optional(list(string))
      environment_variables = optional(map(string), {})
      volume_mounts = optional(map(object({
        mount_path = string
        read_only  = optional(bool, false)
      })), {})
    })), {})

    # Volúmenes (solo Linux). Los valores sensibles van en container_group_secrets
    volumes = optional(map(object({
      type                 = string           # empty_dir | secret | azure_file
      share_name           = optional(string) # azure_file
      storage_account_name = optional(string) # azure_file
    })), {})

    customer_managed_key = optional(object({
      key_vault_key_id = string # CON versión (el provider lo exige); la identidad necesita Get, WrapKey, UnwrapKey y GetRotationPolicy
    }))

    log_analytics_workspace_id = optional(string)
    lock_enabled               = optional(bool, false) # casi todo cambio recrea el grupo: un bloqueo lo impediría
    tags                       = optional(map(string), {})
  }))
  default = {}

  validation {
    condition     = alltrue([for k, v in var.container_groups : can(regex("^[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?$", k)) && !strcontains(k, "--")])
    error_message = "Nombre del grupo: 1-63 minúsculas, números y guiones, sin guiones al principio, al final ni consecutivos."
  }

  validation {
    condition = alltrue([
      for k, v in var.container_groups :
      contains(["Linux", "Windows"], v.os_type) &&
      contains(["Standard", "Confidential"], v.sku) &&
      contains(["Regular", "Spot"], v.priority) &&
      contains(["Always", "OnFailure", "Never"], v.restart_policy) &&
      contains(["Private", "Public", "None"], v.network.mode)
    ])
    error_message = "os_type: Linux o Windows; sku: Standard o Confidential; priority: Regular o Spot; restart_policy: Always, OnFailure o Never; network.mode: Private, Public o None."
  }

  validation {
    condition = alltrue([
      for k, v in var.container_groups :
      (v.network.mode == "Private") == (v.network.subnet_id != null) &&
      (v.network.mode == "Public" || v.network.dns_name_label == null) &&
      contains(["TenantReuse", "SubscriptionReuse", "ResourceGroupReuse", "Noreuse"], v.network.dns_name_label_reuse_policy)
    ])
    error_message = "Private exige subnet_id (y solo Private lo admite); dns_name_label solo con Public; dns_name_label_reuse_policy: TenantReuse, SubscriptionReuse, ResourceGroupReuse o Noreuse (Unsecure permite el secuestro del subdominio)."
  }

  validation {
    condition = alltrue([
      for k, v in var.container_groups :
      v.priority == "Regular" || (v.network.mode == "None" && v.zone == null && v.sku == "Standard" && v.os_type == "Linux")
    ])
    error_message = "Spot (preview) solo en Linux Standard, sin IP (network.mode = None) y sin zona."
  }

  validation {
    condition     = alltrue([for k, v in var.container_groups : v.zone == null || (v.sku == "Standard" && contains(["1", "2", "3"], coalesce(v.zone, "1")))])
    error_message = "Las zonas solo admiten la SKU Standard y los valores 1, 2 o 3."
  }

  validation {
    condition = alltrue([
      for k, v in var.container_groups :
      v.os_type == "Linux" || (length(v.containers) == 1 && length(v.volumes) == 0 && length(v.init_containers) == 0)
    ])
    error_message = "Windows: un solo contenedor, sin volúmenes ni init containers."
  }

  validation {
    condition = alltrue([
      for k, v in var.container_groups :
      sum([for c in values(v.containers) : c.cpu]) >= 1 && sum([for c in values(v.containers) : c.memory]) >= 1
    ])
    error_message = "Un grupo necesita al menos 1 vCPU y 1 GB en total."
  }

  validation {
    condition = alltrue(flatten([
      for k, v in var.container_groups : [
        for c in values(v.containers) : [
          for p in c.ports :
          contains(["TCP", "UDP"], p.protocol) &&
          !(contains([22, 9999, 19000, 19080, 19100, 19390], p.port) ||
            (p.port >= 1025 && p.port <= 1027) || (p.port >= 3389 && p.port <= 3399) ||
          (p.port >= 20000 && p.port <= 30000) || (p.port >= 49152 && p.port <= 65534))
        ]
      ]
    ]))
    error_message = "Puertos reservados por ACI: 22, 1025-1027, 3389-3399, 9999, 19000, 19080, 19100, 19390, 20000-30000 y 49152-65534. Protocolo TCP o UDP."
  }

  validation {
    condition = alltrue(flatten([
      for k, v in var.container_groups : [
        for vk, vol in v.volumes :
        contains(["empty_dir", "secret", "azure_file"], vol.type) &&
        (vol.type != "azure_file" || (vol.share_name != null && vol.storage_account_name != null))
      ]
    ]))
    error_message = "Volúmenes: empty_dir, secret o azure_file; azure_file exige share_name y storage_account_name."
  }

  validation {
    condition = alltrue(flatten([
      for k, v in var.container_groups : [
        for c in concat(values(v.containers), values(v.init_containers)) : [
          for vm in keys(c.volume_mounts) : contains(keys(v.volumes), vm)
        ]
      ]
    ]))
    error_message = "Cada volume_mounts debe referirse a un volumen declarado en volumes."
  }

  validation {
    condition = alltrue([
      for k, v in var.container_groups :
      (v.acr == null && v.customer_managed_key == null && length(v.role_assignments) == 0) || v.identity_enabled
    ])
    error_message = "acr, customer_managed_key y role_assignments necesitan identity_enabled = true (ACI solo descarga de ACR con identidad de usuario)."
  }

  validation {
    condition = alltrue([
      for k, v in var.container_groups :
      v.acr == null || contains(["Container Registry Repository Reader", "AcrPull"], try(v.acr.role, ""))
    ])
    error_message = "acr.role: Container Registry Repository Reader (registro en modo ABAC) o AcrPull (modo legacy)."
  }
}

variable "container_group_secrets" {
  description = "Valores sensibles por grupo: variables seguras (contenedor -> nombre -> valor), ficheros de volúmenes secretos (volumen -> fichero -> valor en claro) y claves de storage (volumen -> clave). Se inyectan desde Key Vault en el pipeline."
  type = map(object({
    secure_environment_variables = optional(map(map(string)), {})
    secret_volumes               = optional(map(map(string)), {})
    storage_account_keys         = optional(map(string), {})
  }))
  default   = {}
  sensitive = true
}

# -----------------------------------------------------------------------------
# Identidad de usuario del grupo (módulo PRO/common/assigned_identity del repositorio)
# -----------------------------------------------------------------------------
module "aci_identity" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//PRO/common/assigned_identity?ref=main"
  for_each = { for k, v in var.container_groups : k => v if v.identity_enabled }

  name                = "id-${each.key}"
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  tags                = merge(var.tags, each.value.tags)
}

# Permisos ANTES de crear el grupo: la imagen se descarga al crearlo
resource "azurerm_role_assignment" "aci_acr" {
  for_each = { for k, v in var.container_groups : k => v.acr if v.acr != null }

  scope                            = each.value.registry_id
  role_definition_name             = each.value.role
  principal_id                     = module.aci_identity[each.key].principal_id
  principal_type                   = "ServicePrincipal"
  skip_service_principal_aad_check = true
  description                      = "ACI ${each.key}: pull de imágenes"
}

resource "azurerm_role_assignment" "aci_extra" {
  for_each = merge([
    for k, v in var.container_groups : {
      for rk, r in v.role_assignments : "${k}-${rk}" => merge(r, { group = k })
    }
  ]...)

  scope                            = each.value.scope
  role_definition_name             = each.value.role
  principal_id                     = module.aci_identity[each.value.group].principal_id
  principal_type                   = "ServicePrincipal"
  skip_service_principal_aad_check = true
  description                      = "ACI ${each.value.group}"
}

# -----------------------------------------------------------------------------
# Grupo de contenedores (recurso nativo: el módulo del repositorio no monta volúmenes
# y su validación de identity falla cuando no se pasa identidad)
# -----------------------------------------------------------------------------
resource "azurerm_container_group" "this" {
  for_each = var.container_groups

  name                = each.key
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  os_type             = each.value.os_type
  sku                 = each.value.sku
  priority            = each.value.priority == "Spot" ? "Spot" : null
  restart_policy      = each.value.restart_policy
  zones               = each.value.zone == null ? null : [each.value.zone]

  # Red
  ip_address_type             = each.value.network.mode
  subnet_ids                  = each.value.network.mode == "Private" ? [each.value.network.subnet_id] : null
  dns_name_label              = each.value.network.dns_name_label
  dns_name_label_reuse_policy = each.value.network.mode == "Public" ? each.value.network.dns_name_label_reuse_policy : null

  dynamic "dns_config" {
    for_each = length(each.value.network.dns_servers) > 0 ? [1] : []
    content {
      nameservers    = each.value.network.dns_servers
      search_domains = each.value.network.dns_search_domains
    }
  }

  # Solo los puertos declarados en los contenedores; sin IP no se expone nada
  dynamic "exposed_port" {
    for_each = each.value.network.mode == "None" ? [] : distinct(flatten([for c in values(each.value.containers) : c.ports]))
    content {
      port     = exposed_port.value.port
      protocol = exposed_port.value.protocol
    }
  }

  # Identidad: la del grupo más las adicionales
  dynamic "identity" {
    for_each = each.value.identity_enabled || length(each.value.user_assigned_identity_ids) > 0 ? [1] : []
    content {
      type = "UserAssigned"
      identity_ids = distinct(concat(
        each.value.identity_enabled ? [module.aci_identity[each.key].id] : [],
        each.value.user_assigned_identity_ids
      ))
    }
  }

  # Pull de ACR con identidad de usuario (sin usuario ni contraseña)
  dynamic "image_registry_credential" {
    for_each = each.value.acr == null ? [] : [each.value.acr]
    content {
      server                    = image_registry_credential.value.server
      user_assigned_identity_id = module.aci_identity[each.key].id
    }
  }

  dynamic "init_container" {
    for_each = each.value.init_containers
    content {
      name                         = init_container.key
      image                        = init_container.value.image
      commands                     = init_container.value.commands
      environment_variables        = init_container.value.environment_variables
      secure_environment_variables = try(var.container_group_secrets[each.key].secure_environment_variables[init_container.key], null)

      dynamic "volume" {
        for_each = init_container.value.volume_mounts
        content {
          name                 = volume.key
          mount_path           = volume.value.mount_path
          read_only            = volume.value.read_only
          empty_dir            = each.value.volumes[volume.key].type == "empty_dir" ? true : null
          share_name           = each.value.volumes[volume.key].share_name
          storage_account_name = each.value.volumes[volume.key].storage_account_name
          storage_account_key  = each.value.volumes[volume.key].type == "azure_file" ? var.container_group_secrets[each.key].storage_account_keys[volume.key] : null
          secret               = each.value.volumes[volume.key].type == "secret" ? { for f, val in var.container_group_secrets[each.key].secret_volumes[volume.key] : f => base64encode(val) } : null
        }
      }
    }
  }

  dynamic "container" {
    for_each = each.value.containers
    content {
      name                         = container.key
      image                        = container.value.image
      cpu                          = container.value.cpu
      memory                       = container.value.memory
      cpu_limit                    = container.value.cpu_limit
      memory_limit                 = container.value.memory_limit
      commands                     = container.value.commands
      environment_variables        = container.value.environment_variables
      secure_environment_variables = try(var.container_group_secrets[each.key].secure_environment_variables[container.key], null)

      dynamic "ports" {
        for_each = container.value.ports
        content {
          port     = ports.value.port
          protocol = ports.value.protocol
        }
      }

      # Cada montaje lleva su origen: el provider exige exactamente uno por volumen
      dynamic "volume" {
        for_each = container.value.volume_mounts
        content {
          name                 = volume.key
          mount_path           = volume.value.mount_path
          read_only            = each.value.volumes[volume.key].type == "secret" ? true : volume.value.read_only
          empty_dir            = each.value.volumes[volume.key].type == "empty_dir" ? true : null
          share_name           = each.value.volumes[volume.key].share_name
          storage_account_name = each.value.volumes[volume.key].storage_account_name
          storage_account_key  = each.value.volumes[volume.key].type == "azure_file" ? var.container_group_secrets[each.key].storage_account_keys[volume.key] : null
          secret               = each.value.volumes[volume.key].type == "secret" ? { for f, val in var.container_group_secrets[each.key].secret_volumes[volume.key] : f => base64encode(val) } : null
        }
      }

      dynamic "liveness_probe" {
        for_each = container.value.liveness_probe == null ? [] : [container.value.liveness_probe]
        content {
          exec                  = liveness_probe.value.exec
          initial_delay_seconds = liveness_probe.value.initial_delay_seconds
          period_seconds        = liveness_probe.value.period_seconds
          failure_threshold     = liveness_probe.value.failure_threshold
          timeout_seconds       = liveness_probe.value.timeout_seconds

          dynamic "http_get" {
            for_each = liveness_probe.value.http_path == null ? [] : [1]
            content {
              path   = liveness_probe.value.http_path
              port   = liveness_probe.value.http_port
              scheme = liveness_probe.value.http_scheme
            }
          }
        }
      }

      dynamic "readiness_probe" {
        for_each = container.value.readiness_probe == null ? [] : [container.value.readiness_probe]
        content {
          exec                  = readiness_probe.value.exec
          initial_delay_seconds = readiness_probe.value.initial_delay_seconds
          period_seconds        = readiness_probe.value.period_seconds
          failure_threshold     = readiness_probe.value.failure_threshold
          timeout_seconds       = readiness_probe.value.timeout_seconds

          dynamic "http_get" {
            for_each = readiness_probe.value.http_path == null ? [] : [1]
            content {
              path   = readiness_probe.value.http_path
              port   = readiness_probe.value.http_port
              scheme = readiness_probe.value.http_scheme
            }
          }
        }
      }
    }
  }

  # Cifrado de los datos del despliegue con clave propia
  key_vault_key_id                    = try(each.value.customer_managed_key.key_vault_key_id, null)
  key_vault_user_assigned_identity_id = each.value.customer_managed_key == null ? null : module.aci_identity[each.key].id

  tags = merge(var.tags, each.value.tags)

  lifecycle {
    precondition {
      condition = alltrue([
        for vk, vol in each.value.volumes :
        vol.type == "empty_dir" ||
        (vol.type == "secret" && length(try(var.container_group_secrets[each.key].secret_volumes[vk], {})) > 0) ||
        (vol.type == "azure_file" && try(var.container_group_secrets[each.key].storage_account_keys[vk], "") != "")
      ])
      error_message = "Cada volumen secret o azure_file necesita su valor en container_group_secrets (secret_volumes o storage_account_keys)."
    }
  }

  depends_on = [azurerm_role_assignment.aci_acr, azurerm_role_assignment.aci_extra]
}

# -----------------------------------------------------------------------------
# Registros por diagnostic settings: tablas ContainerInstanceLog y ContainerEvent,
# sin clave del workspace (módulo Security/Seguridad/modules/monitor_diagnostic_setting)
# -----------------------------------------------------------------------------
module "aci_diagnostics" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Security/Seguridad/modules/monitor_diagnostic_setting?ref=main"
  for_each = { for k, v in var.container_groups : k => v if v.log_analytics_workspace_id != null }

  monitor_diagnostic_setting_name = "diag-${each.key}"
  target_resource_id              = azurerm_container_group.this[each.key].id
  log_analytics_workspace_id      = each.value.log_analytics_workspace_id
  log_analytics_destination_type  = "Dedicated"
  enabled_logs = [
    { category = "ContainerInstanceLog" },
    { category = "ContainerEvent" }
  ]
  enabled_metrics = [
    { category = "AllMetrics" }
  ]
}

# -----------------------------------------------------------------------------
# Bloqueo opcional
# -----------------------------------------------------------------------------
resource "azurerm_management_lock" "aci" {
  for_each = { for k, v in var.container_groups : k => v if v.lock_enabled }

  name       = "lock-${each.key}"
  scope      = azurerm_container_group.this[each.key].id
  lock_level = "CanNotDelete"
  notes      = "Protege el grupo de contenedores contra el borrado accidental."
}

# -----------------------------------------------------------------------------
# Salidas
# -----------------------------------------------------------------------------
output "container_group_ids" {
  description = "ID de cada grupo de contenedores."
  value       = { for k, v in azurerm_container_group.this : k => v.id }
}

output "container_group_ip_addresses" {
  description = "IP de cada grupo (puede cambiar al reiniciarse: no fijarla en configuraciones)."
  value       = { for k, v in azurerm_container_group.this : k => v.ip_address }
}

output "container_group_fqdns" {
  description = "FQDN de los grupos públicos."
  value       = { for k, v in azurerm_container_group.this : k => v.fqdn if try(length(v.fqdn), 0) > 0 }
}

output "container_group_identities" {
  description = "Identidad de usuario de cada grupo (para asignar roles fuera de este root)."
  value       = { for k, v in module.aci_identity : k => { id = v.id, principal_id = v.principal_id } }
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

container_groups = {
  # Servicio interno: privado, zonal, imagen de ACR con identidad, secretos desde Key Vault
  "ci-workload-api-pro-01" = {
    resource_group_name = "<rg-workload-pro>"
    location            = "<region>"
    restart_policy      = "Always"
    zone                = "1"

    network = {
      mode        = "Private"
      subnet_id   = "<resourceId snet-aci-pro (/24, delegada, con NAT Gateway)>"
      dns_servers = ["<ip-dns-privado-1>", "<ip-dns-privado-2>"]
    }

    acr = {
      server      = "<registro>.azurecr.io"
      registry_id = "<resourceId crworkloadpro01>"
    }

    role_assignments = {
      keyvault = {
        scope = "<resourceId kv-workload-pro>"
        role  = "Key Vault Secrets User"
      }
    }

    containers = {
      api = {
        image  = "<registro>.azurecr.io/workload/api:<version>"
        cpu    = 1
        memory = 2
        ports  = [{ port = 8080 }]
        environment_variables = {
          ASPNETCORE_URLS = "http://+:8080"
          KEYVAULT_URI    = "https://<kv-workload-pro>.vault.azure.net/"
        }
        liveness_probe  = { http_path = "/healthz", http_port = 8080 }
        readiness_probe = { http_path = "/ready", http_port = 8080 }
      }
    }

    log_analytics_workspace_id = "<resourceId log-platform-pro>"
    tags                       = { dataclassification = "internal" }
  }

  # Tarea nocturna: se ejecuta y termina; sin IP de entrada
  "ci-workload-job-pro-01" = {
    resource_group_name = "<rg-workload-pro>"
    location            = "<region>"
    restart_policy      = "OnFailure"

    network = {
      mode        = "Private"
      subnet_id   = "<resourceId snet-aci-pro (/24, delegada, con NAT Gateway)>"
      dns_servers = ["<ip-dns-privado-1>", "<ip-dns-privado-2>"]
    }

    acr = {
      server      = "<registro>.azurecr.io"
      registry_id = "<resourceId crworkloadpro01>"
    }

    containers = {
      job = {
        image  = "<registro>.azurecr.io/workload/job:<version>"
        cpu    = 1
        memory = 1.5
        volume_mounts = {
          config = { mount_path = "/mnt/secrets" }
          work   = { mount_path = "/mnt/work" }
        }
      }
    }

    volumes = {
      config = { type = "secret" }
      work   = { type = "empty_dir" }
    }

    log_analytics_workspace_id = "<resourceId log-platform-pro>"
  }
}

# container_group_secrets NO va aquí: el pipeline lo construye desde Key Vault (TF_VAR_container_group_secrets)
```

### Despliegue y comprobación

Los secretos se leen de Key Vault en el momento del despliegue y llegan a Terraform como variable de entorno:

```powershell
$settings = Get-AzKeyVaultSecret -VaultName "<kv-workload-pro>" -Name "job-settings" -AsPlainText
$apiKey   = Get-AzKeyVaultSecret -VaultName "<kv-workload-pro>" -Name "api-key" -AsPlainText

$env:TF_VAR_container_group_secrets = @{
    "ci-workload-job-pro-01" = @{ secret_volumes = @{ config = @{ "settings.json" = $settings } } }
    "ci-workload-api-pro-01" = @{ secure_environment_variables = @{ api = @{ API_KEY = $apiKey } } }
} | ConvertTo-Json -Depth 6 -Compress

terraform init
terraform plan -var-file="env/pro.tfvars" -out="pro.tfplan"
terraform apply "pro.tfplan"
Remove-Item Env:\TF_VAR_container_group_secrets

# Estado, red y zona (propiedades de la API)
$cg = Get-AzResource -ResourceGroupName "<rg-workload-pro>" -ResourceType "Microsoft.ContainerInstance/containerGroups" -Name "ci-workload-api-pro-01" -ExpandProperties
[PSCustomObject]@{
    State       = $cg.Properties.instanceView.state
    IpType      = $cg.Properties.ipAddress.type
    Ip          = $cg.Properties.ipAddress.ip
    Zones       = $cg.Zones -join ","
    RegistryMI  = $cg.Properties.imageRegistryCredentials.identity
}

# Logs del contenedor
Get-AzContainerInstanceLog -ResourceGroupName "<rg-workload-pro>" -ContainerGroupName "ci-workload-api-pro-01" -ContainerName "api"

# Tareas: relanzar una ejecución
Start-AzContainerGroup -ResourceGroupName "<rg-workload-pro>" -Name "ci-workload-job-pro-01"
```

Consultas en Log Analytics (tablas de diagnostic settings):

```kusto
ContainerInstanceLog
| where TimeGenerated > ago(1h)
| order by TimeGenerated desc

ContainerEvent
| where TimeGenerated > ago(1d)
| order by TimeGenerated desc
```

### Equivalente en Bicep

Un grupo por despliegue. Reutiliza `role-on-resource.bicep` de la [ficha de AKS](/recursos/compute/aks/) para asignar roles sobre ACR y otros recursos de otros grupos de recursos. Los secretos son parámetros `@secure()` que el `.bicepparam` lee de variables de entorno, rellenadas desde Key Vault.

`aci.bicep`:

```bicep
// =============================================================================
// Un grupo de contenedores seguro por defecto: privado en subred delegada, identidad de usuario
// para el pull de ACR y el acceso a servicios, secretos como parámetros @secure(), sondas,
// zona y CMK opcionales y registros por diagnostic settings
// DEPENDENCY: subred delegada a Microsoft.ContainerInstance/containerGroups (/24) con NAT Gateway
// DEPENDENCY: ACR con la excepción de servicios de confianza; private endpoint en otra subred
// DEPENDENCY: role-on-resource.bicep (ficha de AKS) en la misma carpeta para los roles en otros grupos
// =============================================================================
@minLength(1)
@maxLength(63)
param name string
param location string = resourceGroup().location

@allowed(['Linux', 'Windows'])
param osType string = 'Linux'

@allowed(['Standard', 'Confidential'])
param sku string = 'Standard'

@description('Spot (preview): sin red, sin zona, solo Linux Standard.')
@allowed(['Regular', 'Spot'])
param priority string = 'Regular'

@allowed(['Always', 'OnFailure', 'Never'])
param restartPolicy string = 'Always'

@description('Vacío = sin zona. Solo Standard y Regular.')
@allowed(['', '1', '2', '3'])
param zone string = ''

@allowed(['Private', 'Public', 'None'])
param networkMode string = 'Private'

param subnetId string = ''
param dnsServers array = []

@description('Solo Public.')
param dnsNameLabel string = ''

@allowed(['TenantReuse', 'SubscriptionReuse', 'ResourceGroupReuse', 'Noreuse'])
param dnsNameLabelReusePolicy string = 'TenantReuse'

@description('{ server, registryId, role? }; vacío = sin ACR')
param acr object = {}

@description('[{ scope, roleDefinitionId }] para la identidad del grupo')
param roleAssignments array = []

@description('[{ name, image, cpu, memoryInGB, ports?: [int], environmentVariables?: object, command?: [], volumeMounts?: [{ name, mountPath, readOnly? }], livenessPath?, readinessPath?, probePort? }]')
param containers array

@description('[{ name, type: emptyDir | secret | azureFile, shareName?, storageAccountName? }]')
param volumes array = []

@description('contenedor -> { NOMBRE: valor }')
@secure()
param secureEnvironmentVariables object = {}

@description('volumen -> { fichero: valor en claro }')
@secure()
param secretVolumes object = {}

@description('volumen -> clave de la storage account')
@secure()
param storageAccountKeys object = {}

@description('URI de la clave CON versión (https://<kv>.vault.azure.net/keys/<clave>/<versión>); vacío = claves de Microsoft')
param customerManagedKeyId string = ''

param logAnalyticsWorkspaceId string = ''
param tags object = {}

var hasAcr = !empty(acr)
var acrRoleIds = {
  'Container Registry Repository Reader': 'b93aa761-3e63-49ed-ac28-beffa264f7ac'
  AcrPull: '7f951dda-4ed3-4680-a7ca-43fe172d538d'
}
var exposedPorts = [
  for p in union(flatten(map(containers, c => c.?ports ?? [])), []): {
    port: p
    protocol: 'TCP'
  }
]
var volumeDefinitions = [
  for v in volumes: union(
    { name: v.name },
    v.type == 'emptyDir' ? { emptyDir: {} } : {},
    v.type == 'secret' ? { secret: toObject(items(secretVolumes[v.name]), i => i.key, i => base64(i.value)) } : {},
    v.type == 'azureFile'
      ? {
          azureFile: {
            shareName: v.shareName
            storageAccountName: v.storageAccountName
            storageAccountKey: storageAccountKeys[v.name]
          }
        }
      : {}
  )
]

resource identity 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = {
  name: 'id-${name}'
  location: location
  tags: tags
}

// Permisos antes de crear el grupo: la imagen se descarga al crearlo
module acrRole 'role-on-resource.bicep' = if (hasAcr) {
  name: '${take(name, 50)}-acr'
  scope: resourceGroup(split(acr.registryId, '/')[2], split(acr.registryId, '/')[4])
  params: {
    resourceId: acr.registryId
    roleDefinitionId: acrRoleIds[acr.?role ?? 'Container Registry Repository Reader']
    principalId: identity.properties.principalId
    description: 'ACI ${name}: pull de imágenes'
  }
}

module extraRoles 'role-on-resource.bicep' = [
  for (r, i) in roleAssignments: {
    name: '${take(name, 50)}-role-${i}'
    scope: resourceGroup(split(r.scope, '/')[2], split(r.scope, '/')[4])
    params: {
      resourceId: r.scope
      roleDefinitionId: r.roleDefinitionId
      principalId: identity.properties.principalId
      description: 'ACI ${name}'
    }
  }
]

resource group 'Microsoft.ContainerInstance/containerGroups@2025-09-01' = {
  name: name
  location: location
  tags: tags
  zones: empty(zone) ? null : [zone]
  identity: {
    type: 'UserAssigned'
    userAssignedIdentities: {
      '${identity.id}': {}
    }
  }
  properties: {
    osType: osType
    sku: sku
    priority: priority
    restartPolicy: restartPolicy
    subnetIds: networkMode == 'Private'
      ? [
          {
            id: subnetId
          }
        ]
      : null
    ipAddress: networkMode == 'None'
      ? null
      : {
          type: networkMode
          ports: exposedPorts
          dnsNameLabel: networkMode == 'Public' && !empty(dnsNameLabel) ? dnsNameLabel : null
          autoGeneratedDomainNameLabelScope: networkMode == 'Public' ? dnsNameLabelReusePolicy : null
        }
    dnsConfig: empty(dnsServers)
      ? null
      : {
          nameServers: dnsServers
        }
    imageRegistryCredentials: hasAcr
      ? [
          {
            server: acr.server
            identity: identity.id
          }
        ]
      : null
    encryptionProperties: empty(customerManagedKeyId)
      ? null
      : {
          vaultBaseUrl: 'https://${split(customerManagedKeyId, '/')[2]}'
          keyName: split(customerManagedKeyId, '/')[4]
          keyVersion: split(customerManagedKeyId, '/')[5]
          identity: identity.id
        }
    volumes: empty(volumes) ? null : volumeDefinitions
    containers: [
      for c in containers: {
        name: c.name
        properties: {
          image: c.image
          command: c.?command
          resources: {
            requests: {
              cpu: c.cpu
              memoryInGB: c.memoryInGB
            }
          }
          ports: map(c.?ports ?? [], p => { port: p, protocol: 'TCP' })
          environmentVariables: concat(
            map(items(c.?environmentVariables ?? {}), e => { name: e.key, value: e.value }),
            map(items(secureEnvironmentVariables[?c.name] ?? {}), e => { name: e.key, secureValue: e.value })
          )
          volumeMounts: c.?volumeMounts
          livenessProbe: empty(c.?livenessPath ?? '')
            ? null
            : {
                httpGet: {
                  path: c.livenessPath
                  port: c.probePort
                  scheme: 'http'
                }
                initialDelaySeconds: 10
                periodSeconds: 10
                failureThreshold: 3
                timeoutSeconds: 5
              }
          readinessProbe: empty(c.?readinessPath ?? '')
            ? null
            : {
                httpGet: {
                  path: c.readinessPath
                  port: c.probePort
                  scheme: 'http'
                }
                initialDelaySeconds: 5
                periodSeconds: 10
                failureThreshold: 3
                timeoutSeconds: 5
              }
        }
      }
    ]
  }
  dependsOn: [
    acrRole
    extraRoles
  ]
}

resource diagnostics 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = if (!empty(logAnalyticsWorkspaceId)) {
  name: 'diag-${name}'
  scope: group
  properties: {
    workspaceId: logAnalyticsWorkspaceId
    logAnalyticsDestinationType: 'Dedicated'
    logs: [
      {
        category: 'ContainerInstanceLog'
        enabled: true
      }
      {
        category: 'ContainerEvent'
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

output id string = group.id
output ipAddress string = group.properties.?ipAddress.?ip ?? ''
output identityPrincipalId string = identity.properties.principalId
```

`ci-workload-job-pro-01.bicepparam`:

```bicep
using 'aci.bicep'

param name = 'ci-workload-job-pro-01'
param restartPolicy = 'OnFailure'
param networkMode = 'Private'
param subnetId = '<resourceId snet-aci-pro (/24, delegada, con NAT Gateway)>'
param dnsServers = ['<ip-dns-privado-1>', '<ip-dns-privado-2>']

param acr = {
  server: '<registro>.azurecr.io'
  registryId: '<resourceId crworkloadpro01>'
}

param containers = [
  {
    name: 'job'
    image: '<registro>.azurecr.io/workload/job:<version>'
    cpu: 1
    memoryInGB: json('1.5')
    volumeMounts: [
      { name: 'config', mountPath: '/mnt/secrets', readOnly: true }
      { name: 'work', mountPath: '/mnt/work' }
    ]
  }
]

param volumes = [
  { name: 'config', type: 'secret' }
  { name: 'work', type: 'emptyDir' }
]

// Secretos: el pipeline los lee de Key Vault y los deja en variables de entorno (nunca en el repositorio)
param secretVolumes = json(readEnvironmentVariable('ACI_SECRET_VOLUMES', '{}'))
param secureEnvironmentVariables = json(readEnvironmentVariable('ACI_SECURE_ENV', '{}'))

param logAnalyticsWorkspaceId = '<resourceId log-platform-pro>'

param tags = {
  environment: 'pro'
  workload: '<workload>'
  owner: '<owner>'
  costcenter: '<costcenter>'
}
```

Despliegue:

```powershell
$settings = Get-AzKeyVaultSecret -VaultName "<kv-workload-pro>" -Name "job-settings" -AsPlainText
$env:ACI_SECRET_VOLUMES = @{ config = @{ "settings.json" = $settings } } | ConvertTo-Json -Depth 4 -Compress

New-AzResourceGroupDeployment -ResourceGroupName "<rg-workload-pro>" `
    -TemplateParameterFile "ci-workload-job-pro-01.bicepparam" -Name "aci-ci-workload-job-pro-01"
Remove-Item Env:\ACI_SECRET_VOLUMES
```

## Errores típicos

| Síntoma | Causa | Solución |
|---|---|---|
| El contenedor entra en bucle de reinicios | `Always` con una imagen sin proceso de larga duración (por ejemplo, una shell) | `OnFailure` o `Never` para tareas, o un comando que mantenga el proceso |
| Una tarea con `Never` se reinicia | `Never` solo evita reiniciar con código de salida 0 | Gestionar los errores en la aplicación y salir con 0 |
| `container group is still transitioning` | `Start` justo después de parar, o tras terminar con `Never` | Esperar unos segundos; con `Never`, `Stop` antes de `Start` o `Restart` |
| "Subnet full" o grupos atascados al iniciar | Subred menor de /24 | /24 o mayor |
| El despliegue en VNet falla | Subred con otros recursos (por ejemplo, el private endpoint de ACR) o sin delegar | Subred exclusiva y delegada; private endpoint en otra subred |
| Sin salida a Internet ni a servicios desde la VNet | Falta NAT Gateway | NAT Gateway en la subred |
| No resuelve nombres privados | ACI no hereda el DNS de la VNet | `dns_servers` explícitos |
| El pull de ACR falla con identidad | Identidad de sistema, rol que no aplica al modo del registro o registro privado sin servicios de confianza | Identidad de usuario, `Container Registry Repository Reader` en ABAC y `AzureServices` en el registro |
| Error de validación del esquema de la sonda | `scheme = "Http"` | `http` o `https` en minúsculas |
| Una app Windows en VNet no obtiene tokens | Windows en VNet no llega al endpoint de identidad | Linux, o Windows fuera de VNet |
| No monta el share de Azure Files | Clave incorrecta, contenedor sin root o sin service endpoint de Storage | Clave desde Key Vault, ejecutar como root y service endpoint |
| `ServiceUnavailable (409)` | Sin capacidad en la región, sobre todo por encima de 4 vCPU o 16 GB | Reintentar, otra región o ticket para grupos grandes |
| El grupo se reinicia sin intervención | Mantenimiento de la plataforma o caída de la aplicación | Varios grupos detrás de Application Gateway o Traffic Manager |
| La aplicación deja de responder tras un reinicio | Dependía de la IP del grupo | Application Gateway (entrada) o NAT Gateway (salida) |
| Imagen Arm64 que no arranca | ACI solo admite x64 | Imagen `linux/amd64` |
| Arranque lento | Imagen grande o en otra región | Imagen mínima en ACR de la misma región; standby pools |
| Los diagnostic settings reinician el grupo | Comportamiento documentado | Aplicarlos en una ventana de cambios |
| Cualquier cambio recrea el grupo | Casi todos los argumentos fuerzan recreación | Esperado; por eso el bloqueo está desactivado por defecto |
| La precondición de volúmenes falla | Volumen `secret` o `azure_file` sin valor en `container_group_secrets` | Rellenarlo desde Key Vault antes del `plan` |
