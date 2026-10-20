---
title: "Container Registry"
indice: compute
resumen: "Registro privado para tus imágenes."
estado: documentado   # proximamente | en-curso | documentado
orden: 6
last_review: 2026-10-20
fuentes:
  - titulo: "Introduction to Azure Container Registry"
    url: https://learn.microsoft.com/azure/container-registry/container-registry-intro
  - titulo: "Azure Container Registry SKU features and limits"
    url: https://learn.microsoft.com/azure/container-registry/container-registry-skus
  - titulo: "Best practices for Azure Container Registry"
    url: https://learn.microsoft.com/azure/container-registry/container-registry-best-practices
  - titulo: "Recommendations for tagging and versioning container images"
    url: https://learn.microsoft.com/azure/container-registry/container-registry-image-tag-version
  - titulo: "Secure your Azure Container Registry deployment"
    url: https://learn.microsoft.com/azure/container-registry/secure-container-registry
  - titulo: "Zone redundancy in Azure Container Registry"
    url: https://learn.microsoft.com/azure/container-registry/zone-redundancy
  - titulo: "Reliability in Azure Container Registry"
    url: https://learn.microsoft.com/azure/reliability/reliability-container-registry
  - titulo: "Geo-replication in Azure Container Registry"
    url: https://learn.microsoft.com/azure/container-registry/container-registry-geo-replication
  - titulo: "Container image storage in Azure Container Registry"
    url: https://learn.microsoft.com/azure/container-registry/container-registry-storage
  - titulo: "Connect privately to an Azure container registry by using Azure Private Link"
    url: https://learn.microsoft.com/azure/container-registry/container-registry-private-endpoints
  - titulo: "Dedicated data endpoints in Azure Container Registry"
    url: https://learn.microsoft.com/azure/container-registry/container-registry-dedicated-data-endpoints
  - titulo: "Azure Private Endpoint private DNS zone values"
    url: https://learn.microsoft.com/azure/private-link/private-endpoint-dns
  - titulo: "Configure public IP network rules"
    url: https://learn.microsoft.com/azure/container-registry/container-registry-access-selected-networks
  - titulo: "Allow trusted services to securely access a network-restricted container registry"
    url: https://learn.microsoft.com/azure/container-registry/allow-access-trusted-services
  - titulo: "Manage network bypass policy for tasks"
    url: https://learn.microsoft.com/azure/container-registry/manage-network-bypass-policy-for-tasks
  - titulo: "Azure Container Registry Microsoft Entra permissions and role assignments overview"
    url: https://learn.microsoft.com/azure/container-registry/container-registry-rbac-built-in-roles-overview
  - titulo: "Azure ABAC repository permissions in Azure Container Registry"
    url: https://learn.microsoft.com/azure/container-registry/container-registry-rbac-abac-repository-permissions
  - titulo: "Azure built-in roles for Containers"
    url: https://learn.microsoft.com/azure/role-based-access-control/built-in-roles/containers
  - titulo: "Configure registry acceptance of Microsoft Entra authentication scopes"
    url: https://learn.microsoft.com/azure/container-registry/container-registry-disable-authentication-as-arm
  - titulo: "Overview of customer-managed keys"
    url: https://learn.microsoft.com/azure/container-registry/tutorial-customer-managed-keys
  - titulo: "Rotate and revoke a customer-managed key"
    url: https://learn.microsoft.com/azure/container-registry/tutorial-rotate-revoke-customer-managed-keys
  - titulo: "Transition from Docker Content Trust to Notary Project"
    url: https://learn.microsoft.com/azure/container-registry/container-registry-content-trust-deprecation
  - titulo: "Set a retention policy to retain untagged manifests"
    url: https://learn.microsoft.com/azure/container-registry/container-registry-retention-policy
  - titulo: "Optimize image pulls with artifact cache in Azure Container Registry"
    url: https://learn.microsoft.com/azure/container-registry/artifact-cache-overview
  - titulo: "Scan registry images with Microsoft Defender for Cloud"
    url: https://learn.microsoft.com/azure/container-registry/scan-images-defender
  - titulo: "Monitor Azure Container Registry"
    url: https://learn.microsoft.com/azure/container-registry/monitor-container-registry
  - titulo: "Azure Policy built-in definitions for Azure Container Registry"
    url: https://learn.microsoft.com/azure/container-registry/policy-reference
  - titulo: "Troubleshoot network issues with registry"
    url: https://learn.microsoft.com/azure/container-registry/container-registry-troubleshoot-access
  - titulo: "azurerm_container_registry"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/container_registry
  - titulo: "Microsoft.ContainerRegistry registries (plantillas ARM/Bicep)"
    url: https://learn.microsoft.com/azure/templates/microsoft.containerregistry/registries
  - titulo: "Módulo Terraform Containers/ACR"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Containers/ACR
  - titulo: "Módulo Terraform PRO/services/container_registry"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/PRO/services/container_registry
  - titulo: "Módulo Terraform Networking/Networking/modules/private_endpoint"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Networking/Networking/modules/private_endpoint
  - titulo: "Módulo Terraform Security/Seguridad/modules/monitor_diagnostic_setting"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Security/Seguridad/modules/monitor_diagnostic_setting
---

**Azure Container Registry (ACR)** es el registro privado gestionado de Azure para imágenes de contenedores, charts de Helm y otros artefactos OCI. Es la pieza que alimenta a [AKS](/recursos/compute/aks/), [Container Apps](/recursos/compute/container-apps/), [Container Instances](/recursos/compute/container-instances/) y App Service. Como todo lo que se ejecuta sale de aquí, un registro mal configurado reparte imágenes vulnerables o manipuladas por todo el entorno.

## Qué es y cuándo usarlo

### Para qué sirve

| Necesidad | Cómo la cubre ACR |
|---|---|
| Guardar las imágenes propias cerca de donde se ejecutan | Registro en la misma región que AKS o Container Apps: menos latencia y sin coste de salida entre regiones |
| Desplegar en varias regiones con un único nombre | Georreplicación (Premium): un endpoint global, réplicas activas-activas |
| No depender de Docker Hub ni de sus límites | Caché de artefactos: se trae la imagen del origen la primera vez y luego se sirve desde ACR |
| Construir imágenes sin agentes propios | ACR Tasks |
| Controlar quién publica y quién descarga cada repositorio | Roles de Entra ID con condiciones ABAC por repositorio |
| Analizar vulnerabilidades | Defender for Containers analiza las imágenes que se suben, importan o se han descargado en los últimos 30 días |

### Planes

| | Basic | Standard | **Premium** |
|---|---|---|---|
| Almacenamiento incluido | 10 GiB | 100 GiB | 500 GiB |
| Límite de almacenamiento | 40 TiB | 40 TiB | 100 TiB |
| Webhooks | 2 | 10 | 500 |
| Redundancia de zona | Sí (por defecto) | Sí (por defecto) | Sí (por defecto) |
| ABAC por repositorio | Sí | Sí | Sí |
| Pull anónimo | No | Sí | Sí |
| **Private endpoints** (hasta 200) | No | No | **Sí** |
| **Reglas de IP públicas** | No | No | **Sí** |
| **Georreplicación** | No | No | **Sí** |
| Clave gestionada por el cliente (CMK) | No | No | Sí |
| Retención de manifiestos sin etiqueta | No | No | Sí (preview) |
| Bloqueo de exportación | No | No | Sí |
| Lecturas por minuto (por registro) | 10 000 | 10 000 | 20 000 |

- **La redundancia de zona es gratuita y está activa por defecto en todos los planes** en las regiones con zonas, también en registros antiguos. La propiedad `zoneRedundancy` es un resto: aunque marque `Disabled`, el registro es redundante.
- El cambio de plan no tiene caída, pero para bajar de Premium hay que eliminar antes las réplicas y los registros conectados.
- **Sin georreplicación, una caída regional deja el registro inaccesible** y los datos no se recuperan automáticamente.

### Seguridad

| Control | Recomendación de Microsoft | Por defecto en Azure |
|---|---|---|
| Usuario admin | Desactivado: credenciales compartidas con permisos totales | Desactivado |
| Pull anónimo | Solo para registros deliberadamente públicos | Desactivado |
| Tokens de Entra con audiencia ARM | **Desactivarlos**: el registro solo acepta tokens con audiencia ACR | Aceptados |
| Modo de permisos | **ABAC** (`AbacRepositoryPermissions`): será el modo por defecto | Legacy |
| Red | Private endpoint y acceso público desactivado (Premium) | Público |
| Excepción de servicios de confianza | Solo si se usan (Defender, ACI, Machine Learning, importación, caché) | Activada |
| Tareas que saltan la red | Desactivado salvo que una tarea lo necesite | Desactivado |
| Exportación | Bloqueada en registros privados | Permitida |
| Firma de imágenes | **Notary Project (Notation)**; Docker Content Trust se retira el 31 de marzo de 2028 y desde el 31 de mayo de 2026 no se puede activar en registros nuevos | — |
| Imágenes de producción | Bloquear etiquetas (`write-enabled`/`delete-enabled` a `false`) | — |
| Registro | Bloqueo `CanNotDelete` | — |

**ABAC cambia los roles.** En modo ABAC no se respetan `AcrPull`, `AcrPush` ni `AcrDelete`, y Owner, Contributor y Reader solo dan plano de control. Los roles de datos son:

| Rol | Permite | Condición por repositorio |
|---|---|---|
| Container Registry Repository Reader | Pull | Sí |
| Container Registry Repository Writer | Pull y push | Sí |
| Container Registry Repository Contributor | Pull, push y borrado | Sí |
| Container Registry Repository Catalog Lister | Listar repositorios | No |

- Un rol ABAC **sin condición** da acceso a todo el registro.
- Los prefijos de las condiciones **deben acabar en `/`**: sin la barra, `backend` también da acceso a `backend-infra/...`.
- Pasar un registro existente a ABAC **invalida las credenciales en caché** de los clientes (401) hasta que se renuevan. En AKS hay que reiniciar kubelet o reemplazar los nodos; reiniciar pods no basta.

### Red

| Opción | Cuándo |
|---|---|
| **Private endpoint + acceso público desactivado** | Producción. Requiere la zona `privatelink.azurecr.io` (los data endpoints `<registro>.<región>.data.azurecr.io` van en la misma zona) |
| Reglas de IP públicas | Cuando no hay red privada; máximo 200 reglas |
| Service endpoints | En preview y solo para AKS o VMs; Microsoft recomienda private endpoints |

Al cerrar el acceso público:

- `az acr build` deja de funcionar sin un agent pool dedicado.
- Los agentes hospedados de Azure DevOps no llegan: hacen falta agentes propios con visibilidad del private endpoint.
- El portal y la CLI no listan repositorios desde fuera de la red.
- **App Service** no usa la excepción de servicios de confianza.
- Cada private endpoint consume **1 IP global + 1 por réplica** (más 1 por réplica si hay endpoints regionales).

### Cómo se factura

| Concepto | Detalle |
|---|---|
| Plan | Tarifa diaria por registro que incluye el almacenamiento de la tabla |
| Almacenamiento extra | Por GiB y día sobre lo incluido |
| **Réplicas** | **Cada réplica se factura como un registro Premium de su región**; el almacenamiento se cobra por réplica |
| Transferencia | Tráfico entre regiones al replicar; los pulls en la misma región evitan la salida de datos |
| Private endpoints, Defender, Log Analytics | Cada servicio factura aparte |

Formas de ahorrar: registro en la misma región que el cómputo, retención o purga de manifiestos sin etiqueta, un registro compartido por plataforma (con ABAC por repositorio) en lugar de uno por aplicación y réplicas solo donde haya cómputo.

### Qué escenario recomiendo

| Escenario del cliente | Diseño | Por qué |
|---|---|---|
| AKS o Container Apps en producción en una región | Premium + private endpoint + ABAC + diagnóstico | Red privada y permisos por repositorio |
| Cargas en varias regiones o requisito de DR | Premium con réplica en la región secundaria | Continuidad ante caída regional y pulls cercanos |
| Desarrollo y pruebas | Standard sin red privada, con Entra ID | Coste bajo; privado no es posible por debajo de Premium |
| Dependencia de imágenes públicas (Docker Hub, MCR, GHCR) | Caché de artefactos en el registro privado | Sin límites de Docker Hub y todo pasa por la red privada |
| Sector regulado | Premium + CMK + exportación bloqueada + Notation | Control de la clave, sin exfiltración e integridad de la cadena de suministro |
| Muchos equipos | Un registro por plataforma y entorno, repositorios por equipo con ABAC | Menos coste y gobierno centralizado |
| Registros heredados con `AcrPull`/`AcrPush` | Plan de migración a ABAC (roles nuevos antes del cambio) | Evita cortes de acceso |

### Datos que conviene llevar a la reunión

- **Private endpoints, reglas de IP y georreplicación son solo de Premium.**
- **La redundancia de zona ya está incluida** en todos los planes y regiones con zonas.
- **Sin réplica, una caída regional deja el registro sin servicio.**
- **ABAC es el futuro modo por defecto** y desactiva `AcrPull`/`AcrPush`.
- **Docker Content Trust se retira en marzo de 2028**: firmar con Notation.
- **App Service necesita tokens con audiencia ARM** y no usa la excepción de servicios de confianza: hay que validarlo antes de cerrar el registro.
- **Defender for Containers y la caché de artefactos necesitan la excepción de servicios de confianza** en un registro privado.
- **Cada réplica cuesta como otro registro Premium.**

## Decisiones de diseño

| Decisión | Lo que aplico | Por qué |
|---|---|---|
| Recurso | `azurerm_container_registry` nativo | Los dos módulos del repositorio fallan o son inseguros con azurerm 4.x |
| Plan | Premium por defecto | Private endpoint y reglas de red |
| Red | Acceso público desactivado, `network_rule_set` en `Deny`, private endpoint (módulo `Networking/Networking/modules/private_endpoint`) | Superficie mínima |
| Data endpoints | Activados automáticamente si hay private endpoints | Microsoft los activa al crear el private endpoint; declararlo evita diferencias |
| Servicios de confianza | `AzureServices` por defecto | Defender y la caché de artefactos lo necesitan; `None` si no se usan |
| Tareas | Sin salto de red | Recomendación de Microsoft |
| Autenticación | Sin admin, sin pull anónimo, solo tokens con audiencia ACR | Credenciales atribuibles y mínimas |
| Autorización | Modo ABAC; condiciones por repositorio o prefijo validadas | Mínimo privilegio por equipo |
| Exportación | Bloqueada si el registro es privado | Evita exfiltración |
| Retención | Opcional (preview) | Borra datos de forma irrecuperable y rompe pulls por digest |
| Firma | `trust_policy_enabled = false` | DCT retirado; Notation fuera del registro |
| Zonas | No se declara `zone_redundancy_enabled` | Propiedad heredada, sin efecto, y en azurerm fuerza la recreación |
| Réplicas | Mapa por región, ordenado alfabéticamente | El provider lo exige |
| CMK | Opcional, con identidad de usuario | Solo al crear y sin vuelta atrás |
| Diagnóstico | `allLogs` + `AllMetrics` a Log Analytics (tablas dedicadas) | Auditoría de inicios de sesión y operaciones |
| Bloqueo | `CanNotDelete` | Evita perder el registro y sus imágenes |

Alineación con el Well-Architected Framework:

- **Fiabilidad**: zonas incluidas, réplica opcional y bloqueo contra borrado.
- **Seguridad**: red privada, Entra ID con ABAC, tokens ACR, exportación bloqueada, Defender y Notation.
- **Coste**: registro compartido, retención, réplicas solo donde hay cómputo.
- **Excelencia operativa**: IaC, diagnóstico y políticas.
- **Rendimiento**: registro en la región del cómputo, caché de artefactos y réplicas cercanas.

## Módulo de Terraform

### Los módulos del repositorio

Ninguno de los dos módulos de ACR sirve con azurerm 4.x:

| Módulo | Problema |
|---|---|
| [`Containers/ACR`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Containers/ACR) | **No pasa `validate` con azurerm 4.x** (comprobado con 4.81): usa los bloques `retention_policy` y `trust_policy`, el bloque `virtual_network` dentro de `network_rule_set` y el argumento `enabled` en `encryption`, que azurerm 4.0 eliminó o sustituyó por `retention_policy_in_days` y `trust_policy_enabled`. Su `versions.tf` admite `< 5.0.0`. Con OpenTofu 1.8, además, la validación de `identity` falla si no se pasa identidad (`||` no cortocircuita). Valores por defecto: `public_network_access_enabled = true`, plan Standard y nombre construido con `environment` |
| [`PRO/services/container_registry`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/PRO/services/container_registry) | **Inseguro**: `admin_enabled = true` y `public_network_access_enabled = true` fijos, sin variables. Siempre crea un private endpoint, `private_dns_zone_ids` es un `string` que se envuelve en lista, y no tiene diagnóstico ni roles |

Lo que sí reutilizo:

- [`Networking/Networking/modules/private_endpoint`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Networking/Networking/modules/private_endpoint): envoltorio fino, sin bloque `provider`, compatible con `for_each`.
- [`Security/Seguridad/modules/monitor_diagnostic_setting`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Security/Seguridad/modules/monitor_diagnostic_setting): diagnóstico.

Notas del provider (azurerm 4.81):

- `role_assignment_mode`, `azuread_authentication_as_arm_policy_enabled` y `network_rule_bypass_for_tasks_enabled` existen en el recurso. Sus valores por defecto son `LegacyRegistryPermissions`, `true` y `false`.
- `zone_redundancy_enabled` fuerza la recreación.
- El provider no gestiona la eliminación temporal (*soft delete*, en preview).

### Estructura en el proyecto

```txt
/
├── providers.tf               # azurerm >= 4.81.0
├── container_registries.tf    # registro, private endpoints, roles ABAC, caché, diagnóstico, bloqueo
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
      # Validado con 4.81.0 (role_assignment_mode, network_rule_bypass_for_tasks_enabled,
      # azuread_authentication_as_arm_policy_enabled y retention_policy_in_days).
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

### `container_registries.tf`

```hcl
# =============================================================================
# Azure Container Registry seguro por defecto:
# Premium, sin acceso público, private endpoint, sin usuario admin ni pull anónimo,
# solo tokens de Entra con audiencia ACR, permisos por repositorio (ABAC),
# exportación bloqueada, diagnóstico, bloqueo contra borrado y caché de artefactos opcional
#
# DEPENDENCY: grupos de recursos creados
# DEPENDENCY: subred para private endpoints y zona privada privatelink.azurecr.io enlazada a las
#             VNets que resuelven (los registros de los data endpoints se crean en la misma zona)
# DEPENDENCY: CMK: Key Vault con purge protection, clave RSA/RSA-HSM y una identidad de usuario
#             con permisos sobre la clave ANTES de crear el registro (solo se puede activar al crearlo)
# DEPENDENCY: Log Analytics para el diagnóstico
# DEPENDENCY: la identidad de Terraform necesita permisos para asignar roles (RBAC Administrator)
#             y para crear bloqueos (Owner o User Access Administrator) si lock_enabled = true
# =============================================================================

variable "container_registries" {
  description = "Registros de contenedores (clave = nombre del registro, único global, 5-50 alfanuméricos)."
  type = map(object({
    resource_group_name = string
    location            = string
    sku                 = optional(string, "Premium") # Basic | Standard | Premium

    # Red (las restricciones de red y los private endpoints exigen Premium)
    public_network_access_enabled         = optional(bool, false)
    allowed_ip_ranges                     = optional(list(string), [])        # solo con acceso público; Premium
    network_rule_bypass_option            = optional(string, "AzureServices") # AzureServices | None
    network_rule_bypass_for_tasks_enabled = optional(bool, false)
    data_endpoint_enabled                 = optional(bool) # null = automático con private endpoints (Premium)

    private_endpoints = optional(map(object({
      subnet_id           = string
      private_dns_zone_id = string           # privatelink.azurecr.io
      resource_group_name = optional(string) # por defecto, el del registro
      location            = optional(string) # por defecto, el del registro
    })), {})

    # Identidad y autorización
    role_assignment_mode                         = optional(string, "AbacRepositoryPermissions") # AbacRepositoryPermissions | LegacyRegistryPermissions
    azuread_authentication_as_arm_policy_enabled = optional(bool, false)                         # false = solo tokens con audiencia ACR (App Service necesita true)

    role_assignments = optional(map(object({
      principal_id        = string
      role                = string
      principal_type      = optional(string, "ServicePrincipal") # User | Group | ServicePrincipal
      repositories        = optional(list(string), [])           # ABAC: nombres exactos
      repository_prefixes = optional(list(string), [])           # ABAC: prefijos acabados en "/"
    })), {})

    # Datos
    export_policy_enabled    = optional(bool)   # null = solo si hay acceso público (Premium)
    retention_policy_in_days = optional(number) # manifiestos sin etiqueta (Premium, preview); null = sin retención
    georeplications = optional(map(object({     # clave = región (Premium)
      regional_endpoint_enabled = optional(bool, false)
      tags                      = optional(map(string), {})
    })), {})

    customer_managed_key = optional(object({ # Premium; solo al crear
      key_vault_key_id          = string     # sin versión = rotación automática
      user_assigned_identity_id = string
      identity_client_id        = string
    }))
    user_assigned_identity_ids = optional(list(string), [])

    # Caché de artefactos para orígenes públicos sin credenciales (p. ej. mcr.microsoft.com)
    cache_rules = optional(map(object({
      source_repo = string
      target_repo = string
    })), {})

    log_analytics_workspace_id = optional(string)
    lock_enabled               = optional(bool, true)

    tags = optional(map(string), {})
  }))
  default = {}

  validation {
    condition     = alltrue([for k, v in var.container_registries : can(regex("^[a-zA-Z0-9]{5,50}$", k))])
    error_message = "El nombre del registro (clave) admite de 5 a 50 caracteres alfanuméricos."
  }

  validation {
    condition = alltrue([
      for k, v in var.container_registries :
      contains(["Basic", "Standard", "Premium"], v.sku) &&
      contains(["AzureServices", "None"], v.network_rule_bypass_option) &&
      contains(["AbacRepositoryPermissions", "LegacyRegistryPermissions"], v.role_assignment_mode)
    ])
    error_message = "sku: Basic, Standard o Premium; network_rule_bypass_option: AzureServices o None; role_assignment_mode: AbacRepositoryPermissions o LegacyRegistryPermissions."
  }

  validation {
    condition = alltrue([
      for k, v in var.container_registries :
      v.sku == "Premium" || (
        v.public_network_access_enabled && length(v.allowed_ip_ranges) == 0 && length(v.private_endpoints) == 0 &&
        length(v.georeplications) == 0 && v.customer_managed_key == null && v.retention_policy_in_days == null
      )
    ])
    error_message = "Private endpoints, desactivar el acceso público, reglas de IP, georreplicación, CMK y retención exigen Premium."
  }

  validation {
    condition     = alltrue([for k, v in var.container_registries : v.public_network_access_enabled || length(v.allowed_ip_ranges) == 0])
    error_message = "allowed_ip_ranges solo tiene efecto con acceso público: desactivarlo anula las reglas de firewall."
  }

  validation {
    condition     = alltrue([for k, v in var.container_registries : !(coalesce(v.export_policy_enabled, true) == false && v.public_network_access_enabled)])
    error_message = "Para desactivar la exportación, el acceso público debe estar desactivado."
  }

  validation {
    condition     = alltrue([for k, v in var.container_registries : length(v.cache_rules) == 0 || v.network_rule_bypass_option == "AzureServices" || v.public_network_access_enabled])
    error_message = "La caché de artefactos no puede rellenar un registro restringido sin network_rule_bypass_option = AzureServices."
  }

  validation {
    condition = alltrue([
      for k, v in var.container_registries :
      v.retention_policy_in_days == null || (coalesce(v.retention_policy_in_days, -1) >= 0 && coalesce(v.retention_policy_in_days, -1) <= 365)
    ])
    error_message = "retention_policy_in_days entre 0 y 365."
  }

  validation {
    condition = alltrue(flatten([
      for k, v in var.container_registries : [
        for rk, r in v.role_assignments :
        v.role_assignment_mode == "AbacRepositoryPermissions"
        ? contains(["Container Registry Repository Reader", "Container Registry Repository Writer", "Container Registry Repository Contributor", "Container Registry Repository Catalog Lister"], r.role)
        : contains(["AcrPull", "AcrPush", "AcrDelete"], r.role)
      ]
    ]))
    error_message = "Con ABAC solo se respetan los roles Container Registry Repository Reader/Writer/Contributor/Catalog Lister; con LegacyRegistryPermissions, AcrPull/AcrPush/AcrDelete."
  }

  validation {
    condition = alltrue(flatten([
      for k, v in var.container_registries : [
        for rk, r in v.role_assignments :
        (length(r.repositories) + length(r.repository_prefixes) == 0) || (
          v.role_assignment_mode == "AbacRepositoryPermissions" &&
          contains(["Container Registry Repository Reader", "Container Registry Repository Writer"], r.role) &&
          alltrue([for p in r.repository_prefixes : endswith(p, "/")]) &&
          alltrue([for n in concat(r.repositories, r.repository_prefixes) : can(regex("^[a-z0-9._/-]+$", n)) && !strcontains(n, "'")])
        )
      ]
    ]))
    error_message = "Condiciones ABAC: solo con Reader o Writer en modo ABAC; nombres en minúsculas; los prefijos acaban en '/' (sin la barra se concede acceso a repositorios que no comparten el prefijo)."
  }

  validation {
    condition = alltrue(flatten([
      for k, v in var.container_registries : [
        for rk, r in v.role_assignments : contains(["User", "Group", "ServicePrincipal"], r.principal_type)
      ]
    ]))
    error_message = "principal_type: User, Group o ServicePrincipal."
  }
}

# -----------------------------------------------------------------------------
# Registro (recurso nativo: los módulos del repositorio no funcionan con azurerm 4.x)
# -----------------------------------------------------------------------------
resource "azurerm_container_registry" "this" {
  for_each = var.container_registries

  name                = each.key
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  sku                 = each.value.sku

  # Autenticación: solo Entra ID
  admin_enabled                                = false
  anonymous_pull_enabled                       = false
  azuread_authentication_as_arm_policy_enabled = each.value.azuread_authentication_as_arm_policy_enabled
  role_assignment_mode                         = each.value.role_assignment_mode

  # Red
  public_network_access_enabled         = each.value.public_network_access_enabled
  network_rule_bypass_option            = each.value.network_rule_bypass_option
  network_rule_bypass_for_tasks_enabled = each.value.network_rule_bypass_for_tasks_enabled
  data_endpoint_enabled                 = each.value.sku == "Premium" ? coalesce(each.value.data_endpoint_enabled, length(each.value.private_endpoints) > 0) : null

  dynamic "network_rule_set" {
    for_each = each.value.sku == "Premium" ? [1] : []
    content {
      default_action = "Deny"
      ip_rule = [
        for r in each.value.allowed_ip_ranges : { action = "Allow", ip_range = r }
      ]
    }
  }

  # Datos: exportación bloqueada en registros privados; Docker Content Trust no (retirado)
  export_policy_enabled    = each.value.sku == "Premium" ? coalesce(each.value.export_policy_enabled, each.value.public_network_access_enabled) : true
  retention_policy_in_days = each.value.retention_policy_in_days
  trust_policy_enabled     = false

  # Georreplicación: el provider espera las regiones en orden alfabético
  # La redundancia de zona ya está activa por defecto en todas las regiones con zonas
  dynamic "georeplications" {
    for_each = sort(keys(each.value.georeplications))
    content {
      location                  = georeplications.value
      regional_endpoint_enabled = each.value.georeplications[georeplications.value].regional_endpoint_enabled
      tags                      = merge(var.tags, each.value.tags, each.value.georeplications[georeplications.value].tags)
    }
  }

  dynamic "identity" {
    for_each = each.value.customer_managed_key != null || length(each.value.user_assigned_identity_ids) > 0 ? [1] : []
    content {
      type = "UserAssigned"
      identity_ids = distinct(concat(
        each.value.customer_managed_key == null ? [] : [each.value.customer_managed_key.user_assigned_identity_id],
        each.value.user_assigned_identity_ids
      ))
    }
  }

  dynamic "encryption" {
    for_each = each.value.customer_managed_key == null ? [] : [each.value.customer_managed_key]
    content {
      key_vault_key_id   = encryption.value.key_vault_key_id
      identity_client_id = encryption.value.identity_client_id
    }
  }

  tags = merge(var.tags, each.value.tags)
}

# -----------------------------------------------------------------------------
# Private endpoints (módulo Networking/Networking/modules/private_endpoint del repositorio)
# -----------------------------------------------------------------------------
module "acr_private_endpoint" {
  source = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Networking/Networking/modules/private_endpoint?ref=main"
  for_each = merge([
    for k, v in var.container_registries : {
      for pk, p in v.private_endpoints : "${k}-${pk}" => merge(p, { registry = k })
    }
  ]...)

  private_endpoint_name          = "pe-${each.key}"
  custom_network_interface_name  = "nic-pe-${each.key}"
  resource_group_name            = coalesce(each.value.resource_group_name, var.container_registries[each.value.registry].resource_group_name)
  location                       = coalesce(each.value.location, var.container_registries[each.value.registry].location)
  subnet_id                      = each.value.subnet_id
  private_connection_resource_id = azurerm_container_registry.this[each.value.registry].id
  subresource_names              = ["registry"]
  private_dns_zone_ids           = [each.value.private_dns_zone_id]
  tags                           = merge(var.tags, var.container_registries[each.value.registry].tags)
}

# -----------------------------------------------------------------------------
# Roles de plano de datos; con ABAC, condición opcional por repositorio o prefijo
# -----------------------------------------------------------------------------
resource "azurerm_role_assignment" "acr" {
  for_each = merge([
    for k, v in var.container_registries : {
      for rk, r in v.role_assignments : "${k}-${rk}" => merge(r, { registry = k })
    }
  ]...)

  scope                = azurerm_container_registry.this[each.value.registry].id
  role_definition_name = each.value.role
  principal_id         = each.value.principal_id
  principal_type       = each.value.principal_type

  condition_version = length(each.value.repositories) + length(each.value.repository_prefixes) > 0 ? "2.0" : null
  condition = length(each.value.repositories) + length(each.value.repository_prefixes) > 0 ? format(
    "((%s) OR (%s))",
    join(" AND ", [
      for a in(each.value.role == "Container Registry Repository Writer"
        ? ["content/read", "metadata/read", "content/write", "metadata/write"]
      : ["content/read", "metadata/read"]) :
      "!(ActionMatches{'Microsoft.ContainerRegistry/registries/repositories/${a}'})"
    ]),
    join(" OR ", concat(
      [for n in each.value.repositories : "@Request[Microsoft.ContainerRegistry/registries/repositories:name] StringEqualsIgnoreCase '${n}'"],
      [for p in each.value.repository_prefixes : "@Request[Microsoft.ContainerRegistry/registries/repositories:name] StringStartsWithIgnoreCase '${p}'"]
    ))
  ) : null
}

# -----------------------------------------------------------------------------
# Caché de artefactos (orígenes sin autenticación; Docker Hub necesita credential set)
# -----------------------------------------------------------------------------
resource "azurerm_container_registry_cache_rule" "this" {
  for_each = merge([
    for k, v in var.container_registries : {
      for ck, c in v.cache_rules : "${k}-${ck}" => merge(c, { registry = k, rule = ck })
    }
  ]...)

  name                  = each.value.rule
  container_registry_id = azurerm_container_registry.this[each.value.registry].id
  source_repo           = each.value.source_repo
  target_repo           = each.value.target_repo
}

# -----------------------------------------------------------------------------
# Diagnóstico (módulo Security/Seguridad/modules/monitor_diagnostic_setting del repositorio)
# -----------------------------------------------------------------------------
module "acr_diagnostics" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Security/Seguridad/modules/monitor_diagnostic_setting?ref=main"
  for_each = { for k, v in var.container_registries : k => v if v.log_analytics_workspace_id != null }

  monitor_diagnostic_setting_name = "diag-${each.key}"
  target_resource_id              = azurerm_container_registry.this[each.key].id
  log_analytics_workspace_id      = each.value.log_analytics_workspace_id
  log_analytics_destination_type  = "Dedicated"
  enabled_logs = [
    { category_group = "allLogs" } # ContainerRegistryLoginEvents y ContainerRegistryRepositoryEvents
  ]
  enabled_metrics = [
    { category = "AllMetrics" }
  ]
}

# -----------------------------------------------------------------------------
# Bloqueo contra borrado del registro (y de sus imágenes)
# -----------------------------------------------------------------------------
resource "azurerm_management_lock" "acr" {
  for_each = { for k, v in var.container_registries : k => v if v.lock_enabled }

  name       = "lock-${each.key}"
  scope      = azurerm_container_registry.this[each.key].id
  lock_level = "CanNotDelete"
  notes      = "Protege el registro y sus imágenes contra el borrado accidental."
}

# -----------------------------------------------------------------------------
# Salidas
# -----------------------------------------------------------------------------
output "container_registry_ids" {
  description = "ID de cada registro."
  value       = { for k, v in azurerm_container_registry.this : k => v.id }
}

output "container_registry_login_servers" {
  description = "Servidor de inicio de sesión de cada registro (<nombre>.azurecr.io)."
  value       = { for k, v in azurerm_container_registry.this : k => v.login_server }
}

output "container_registry_data_endpoints" {
  description = "Data endpoints de cada registro (reglas de firewall y DNS)."
  value       = { for k, v in azurerm_container_registry.this : k => v.data_endpoint_host_names }
}

output "container_registry_private_endpoint_ids" {
  description = "ID de cada private endpoint."
  value       = { for k, v in module.acr_private_endpoint : k => v.id }
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

container_registries = {
  # Clave = nombre global del registro (5-50 alfanuméricos): sustituir "workload"
  "crworkloadpro01" = {
    resource_group_name = "<rg-shared-pro>"
    location            = "<region>"
    sku                 = "Premium"

    # Solo privado: private endpoint en la VNet hub o de servicios compartidos
    public_network_access_enabled = false
    private_endpoints = {
      hub = {
        subnet_id           = "<resourceId snet-privateendpoints-pro>"
        private_dns_zone_id = "<resourceId privatelink.azurecr.io>"
      }
    }
    # AzureServices: Defender for Containers y la caché de artefactos necesitan esta excepción
    network_rule_bypass_option = "AzureServices"

    # Réplica en la región secundaria para continuidad y pulls cercanos
    georeplications = {
      "<region-secundaria>" = {}
    }

    retention_policy_in_days = 30

    role_assignments = {
      # Nodos de AKS (identidad kubelet): solo pull de las imágenes de la aplicación
      aks-kubelet = {
        principal_id        = "<objectId identidad kubelet aks-workload-pro>"
        role                = "Container Registry Repository Reader"
        repository_prefixes = ["workload/", "mirror/"]
      }
      # Pipeline de CI/CD: push solo a sus repositorios
      cicd-push = {
        principal_id        = "<objectId identidad federada del pipeline>"
        role                = "Container Registry Repository Writer"
        repository_prefixes = ["workload/"]
      }
      # Equipo de plataforma: listar repositorios
      platform-catalog = {
        principal_id   = "<objectId grupo de plataforma>"
        role           = "Container Registry Repository Catalog Lister"
        principal_type = "Group"
      }
    }

    cache_rules = {
      dotnetaspnet = {
        source_repo = "mcr.microsoft.com/dotnet/aspnet"
        target_repo = "mirror/dotnet/aspnet"
      }
    }

    log_analytics_workspace_id = "<resourceId log-platform-pro>"

    tags = {
      dataclassification = "internal"
    }
  }
}
```

### Despliegue y comprobación

```powershell
terraform init
terraform plan -var-file="env/pro.tfvars" -out="pro.tfplan"
terraform apply "pro.tfplan"

# Configuración de seguridad del registro (propiedades de la API)
$acr = Get-AzResource -ResourceGroupName "<rg-shared-pro>" -ResourceType "Microsoft.ContainerRegistry/registries" -Name "crworkloadpro01" -ExpandProperties
[PSCustomObject]@{
    Sku                 = $acr.Sku.Name
    AdminUser           = $acr.Properties.adminUserEnabled
    PublicNetworkAccess = $acr.Properties.publicNetworkAccess
    Bypass              = $acr.Properties.networkRuleBypassOptions
    DataEndpoints       = $acr.Properties.dataEndpointEnabled
    RoleAssignmentMode  = $acr.Properties.roleAssignmentMode
    ArmAudienceTokens   = $acr.Properties.policies.azureADAuthenticationAsArmPolicy.status
    Export              = $acr.Properties.policies.exportPolicy.status
}

# Resolución privada desde una VM o un agente dentro de la red
Resolve-DnsName "crworkloadpro01.azurecr.io"
Resolve-DnsName "crworkloadpro01.<region>.data.azurecr.io"

# Uso frente a los límites del plan
Get-AzContainerRegistryUsage -ResourceGroupName "<rg-shared-pro>" -RegistryName "crworkloadpro01"

# Inicio de sesión con token de audiencia ACR (necesario con azuread_authentication_as_arm_policy_enabled = false)
az login --scope https://containerregistry.azure.net/.default
az acr login --name crworkloadpro01
```

Auditoría en Log Analytics:

```kusto
// Inicios de sesión fallidos
ContainerRegistryLoginEvents
| where ResultDescription != "200"
| project TimeGenerated, Identity, CallerIpAddress, ResultDescription

// Quién borró o desetiquetó imágenes
ContainerRegistryRepositoryEvents
| where OperationName contains "Delete" or OperationName contains "Untag"
| project TimeGenerated, LoginServer, OperationName, Repository, Tag, Identity, CallerIpAddress
```

### Equivalente en Bicep

Un registro por despliegue. Bicep admite los mismos ajustes, incluida la condición ABAC por prefijo. Los ID de los roles de repositorio son los de la documentación de roles integrados de Azure.

`acr.bicep`:

```bicep
// =============================================================================
// Un Azure Container Registry seguro por defecto: Premium, sin acceso público, private endpoint,
// sin admin ni pull anónimo, solo tokens con audiencia ACR, ABAC por repositorio,
// exportación bloqueada, réplicas, diagnóstico, bloqueo y caché de artefactos
// DEPENDENCY: subred para private endpoints y zona privada privatelink.azurecr.io
// DEPENDENCY: CMK: clave e identidad de usuario con permisos sobre ella antes de crear el registro
// =============================================================================
@minLength(5)
@maxLength(50)
param name string
param location string = resourceGroup().location

@allowed(['Basic', 'Standard', 'Premium'])
param sku string = 'Premium'

param publicNetworkAccess bool = false

@description('Solo con acceso público (Premium).')
param allowedIpRanges array = []

@allowed(['AzureServices', 'None'])
param networkRuleBypassOptions string = 'AzureServices'

param networkRuleBypassAllowedForTasks bool = false

@description('false = solo tokens de Entra con audiencia ACR (App Service necesita true).')
param authenticationAsArmPolicy bool = false

@allowed(['AbacRepositoryPermissions', 'LegacyRegistryPermissions'])
param roleAssignmentMode string = 'AbacRepositoryPermissions'

@description('0-365; -1 = sin retención de manifiestos sin etiqueta (Premium).')
@minValue(-1)
@maxValue(365)
param retentionDays int = -1

@description('Regiones de réplica (Premium).')
param replicaLocations array = []

@description('[{ name, subnetId, privateDnsZoneId }]')
param privateEndpoints array = []

@description('null = sin CMK. { keyId (sin versión), userAssignedIdentityId, identityClientId }')
param customerManagedKey object?

@description('[{ name, principalId, role, principalType?, repositoryPrefixes? }] (roles ABAC)')
param roleAssignments array = []

@description('[{ name, sourceRepository, targetRepository }]')
param cacheRules array = []

param logAnalyticsWorkspaceId string?
param lockEnabled bool = true
param tags object = {}

var isPremium = sku == 'Premium'
var hasCmk = customerManagedKey != null
var ipRules = [for r in allowedIpRanges: { action: 'Allow', value: r }]

// Condición ABAC por prefijos (acabados en "/"): acciones de datos del rol OR repositorio permitido
var readActions = ['content/read', 'metadata/read']
var writeActions = ['content/read', 'metadata/read', 'content/write', 'metadata/write']
var roleConditions = [
  for ra in roleAssignments: empty(ra.?repositoryPrefixes ?? [])
    ? ''
    : format(
        '(({0}) OR ({1}))',
        join(
          map(
            ra.role == 'Container Registry Repository Writer' ? writeActions : readActions,
            a => '!(ActionMatches{\'Microsoft.ContainerRegistry/registries/repositories/${a}\'})'
          ),
          ' AND '
        ),
        join(
          map(
            ra.repositoryPrefixes,
            px => '@Request[Microsoft.ContainerRegistry/registries/repositories:name] StringStartsWithIgnoreCase \'${px}\''
          ),
          ' OR '
        )
      )
]

// IDs de los roles integrados de ACR
var roleIds = {
  'Container Registry Repository Reader': 'b93aa761-3e63-49ed-ac28-beffa264f7ac'
  'Container Registry Repository Writer': '2a1e307c-b015-4ebd-883e-5b7698a07328'
  'Container Registry Repository Contributor': '2efddaa5-3f1f-4df3-97df-af3f13818f4c'
  'Container Registry Repository Catalog Lister': 'bfdb9389-c9a5-478a-bb2f-ba9ca092c3c7'
}

resource registry 'Microsoft.ContainerRegistry/registries@2025-11-01' = {
  name: name
  location: location
  tags: tags
  sku: {
    name: sku
  }
  identity: hasCmk
    ? {
        type: 'UserAssigned'
        userAssignedIdentities: {
          '${customerManagedKey!.userAssignedIdentityId}': {}
        }
      }
    : null
  properties: {
    adminUserEnabled: false
    anonymousPullEnabled: false
    roleAssignmentMode: roleAssignmentMode
    publicNetworkAccess: publicNetworkAccess ? 'Enabled' : 'Disabled'
    networkRuleBypassOptions: networkRuleBypassOptions
    networkRuleBypassAllowedForTasks: networkRuleBypassAllowedForTasks
    dataEndpointEnabled: isPremium && !empty(privateEndpoints)
    networkRuleSet: isPremium
      ? {
          defaultAction: 'Deny'
          ipRules: ipRules
        }
      : null
    policies: {
      azureADAuthenticationAsArmPolicy: {
        status: authenticationAsArmPolicy ? 'enabled' : 'disabled'
      }
      exportPolicy: isPremium
        ? {
            status: publicNetworkAccess ? 'enabled' : 'disabled'
          }
        : null
      retentionPolicy: isPremium && retentionDays >= 0
        ? {
            days: retentionDays
            status: 'enabled'
          }
        : null
    }
    encryption: hasCmk
      ? {
          status: 'enabled'
          keyVaultProperties: {
            keyIdentifier: customerManagedKey!.keyId
            identity: customerManagedKey!.identityClientId
          }
        }
      : null
  }
}

resource replicas 'Microsoft.ContainerRegistry/registries/replications@2025-11-01' = [
  for r in (isPremium ? replicaLocations : []): {
    parent: registry
    name: r
    location: r
    tags: tags
    properties: {
      regionEndpointEnabled: false
    }
  }
]

resource pe 'Microsoft.Network/privateEndpoints@2024-05-01' = [
  for p in (isPremium ? privateEndpoints : []): {
    name: 'pe-${name}-${p.name}'
    location: location
    tags: tags
    properties: {
      subnet: {
        id: p.subnetId
      }
      customNetworkInterfaceName: 'nic-pe-${name}-${p.name}'
      privateLinkServiceConnections: [
        {
          name: 'pe-${name}-${p.name}-psc'
          properties: {
            privateLinkServiceId: registry.id
            groupIds: [
              'registry'
            ]
          }
        }
      ]
    }
  }
]

resource peDns 'Microsoft.Network/privateEndpoints/privateDnsZoneGroups@2024-05-01' = [
  for (p, i) in (isPremium ? privateEndpoints : []): {
    parent: pe[i]
    name: 'default'
    properties: {
      privateDnsZoneConfigs: [
        {
          name: 'privatelink-azurecr-io'
          properties: {
            privateDnsZoneId: p.privateDnsZoneId
          }
        }
      ]
    }
  }
]

resource acrRoles 'Microsoft.Authorization/roleAssignments@2022-04-01' = [
  for (ra, i) in roleAssignments: {
    name: guid(registry.id, ra.principalId, ra.role)
    scope: registry
    properties: {
      roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', roleIds[ra.role])
      principalId: ra.principalId
      principalType: ra.?principalType ?? 'ServicePrincipal'
      conditionVersion: empty(roleConditions[i]) ? null : '2.0'
      condition: empty(roleConditions[i]) ? null : roleConditions[i]
    }
  }
]

resource cache 'Microsoft.ContainerRegistry/registries/cacheRules@2025-11-01' = [
  for c in cacheRules: {
    parent: registry
    name: c.name
    properties: {
      sourceRepository: c.sourceRepository
      targetRepository: c.targetRepository
    }
  }
]

resource diagnostics 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = if (!empty(logAnalyticsWorkspaceId ?? '')) {
  name: 'diag-${name}'
  scope: registry
  properties: {
    workspaceId: logAnalyticsWorkspaceId
    logAnalyticsDestinationType: 'Dedicated'
    logs: [
      {
        categoryGroup: 'allLogs'
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

resource lock 'Microsoft.Authorization/locks@2020-05-01' = if (lockEnabled) {
  name: 'lock-${name}'
  scope: registry
  properties: {
    level: 'CanNotDelete'
    notes: 'Protege el registro y sus imágenes contra el borrado accidental.'
  }
}

output id string = registry.id
output loginServer string = registry.properties.loginServer
```

`crworkloadpro01.bicepparam`:

```bicep
using 'acr.bicep'

param name = 'crworkloadpro01'
param sku = 'Premium'
param publicNetworkAccess = false

// AzureServices: Defender for Containers y la caché de artefactos necesitan esta excepción
param networkRuleBypassOptions = 'AzureServices'

param privateEndpoints = [
  {
    name: 'hub'
    subnetId: '<resourceId snet-privateendpoints-pro>'
    privateDnsZoneId: '<resourceId privatelink.azurecr.io>'
  }
]

param replicaLocations = [
  '<region-secundaria>'
]

param retentionDays = 30

param roleAssignments = [
  {
    name: 'aks-kubelet'
    principalId: '<objectId identidad kubelet aks-workload-pro>'
    role: 'Container Registry Repository Reader'
    repositoryPrefixes: ['workload/', 'mirror/']
  }
  {
    name: 'cicd-push'
    principalId: '<objectId identidad federada del pipeline>'
    role: 'Container Registry Repository Writer'
    repositoryPrefixes: ['workload/']
  }
  {
    name: 'platform-catalog'
    principalId: '<objectId grupo de plataforma>'
    role: 'Container Registry Repository Catalog Lister'
    principalType: 'Group'
  }
]

param cacheRules = [
  {
    name: 'dotnetaspnet'
    sourceRepository: 'mcr.microsoft.com/dotnet/aspnet'
    targetRepository: 'mirror/dotnet/aspnet'
  }
]

param logAnalyticsWorkspaceId = '<resourceId log-platform-pro>'

param tags = {
  environment: 'pro'
  workload: '<workload>'
  owner: '<owner>'
  costcenter: '<costcenter>'
  dataclassification: 'internal'
}
```

Despliegue:

```powershell
New-AzResourceGroupDeployment -ResourceGroupName "<rg-shared-pro>" `
    -TemplateParameterFile "crworkloadpro01.bicepparam" -Name "acr-crworkloadpro01"
```

## Errores típicos

| Síntoma | Causa | Solución |
|---|---|---|
| `Blocks of type "retention_policy" are not expected here` (o `trust_policy`, `virtual_network`) | Módulo `Containers/ACR` con azurerm 4.x | Recurso nativo con `retention_policy_in_days` y `trust_policy_enabled` |
| `401 Unauthorized` tras pasar a ABAC | Las credenciales en caché se emitieron en el modo anterior | Renovarlas: reiniciar kubelet o reemplazar los nodos de AKS |
| `insufficient_scope` o `403` al hacer pull o push | En ABAC, `AcrPull`/`AcrPush` no cuentan, o la condición no incluye el repositorio | Rol `Container Registry Repository Reader/Writer`; revisar prefijo con `/` |
| Un pipeline puede escribir en repositorios que no debería | Prefijo de la condición sin `/` final | Corregir el prefijo (la validación del root lo exige) |
| `az acr login` rechazado | Registro configurado solo para tokens con audiencia ACR | `az login --scope https://containerregistry.azure.net/.default` |
| App Service no descarga la imagen | Tokens con audiencia ARM desactivados, o registro privado (App Service no es servicio de confianza) | `azuread_authentication_as_arm_policy_enabled = true` para ese registro y acceso por red privada |
| `az acr build` falla | Acceso público desactivado | Agent pool dedicado o etiqueta de servicio `AzureContainerRegistry` |
| Agentes hospedados de Azure DevOps no llegan | No admiten private endpoints | Agentes propios en la red |
| Pull lento o fallido desde la red privada; resuelve IP pública | Falta el registro DNS del data endpoint o la zona no está enlazada | Zona `privatelink.azurecr.io` enlazada; registros del global y de cada data endpoint |
| Defender no analiza las imágenes | Registro privado con `network_rule_bypass_option = None` | `AzureServices` |
| La caché devuelve imágenes pero no guarda nada | Excepción de servicios de confianza desactivada | `AzureServices` (la validación del root lo exige) |
| Docker Hub no se puede cachear sin credenciales | Docker Hub solo admite pulls autenticados en la caché | Credential set con secretos en Key Vault |
| `429 Too Many Requests` | Límite de peticiones del plan o por identidad | Reintentos con backoff; Premium o réplicas |
| Imágenes desaparecidas | Retención de manifiestos sin etiqueta con despliegues por digest | Etiquetas únicas o desactivar la retención |
| No se puede activar DCT | Desde el 31 de mayo de 2026 no se activa en registros nuevos | Notation y Key Vault |
| No se puede activar CMK | Solo se puede activar al crear el registro | Crear un registro nuevo e importar las imágenes |
| El plan quiere recrear el registro | Cambio de `zone_redundancy_enabled` | No declararlo: la redundancia de zona ya está activa |
| No se puede pasar de Premium a Standard | Hay réplicas o registros conectados | Eliminarlos antes |
| `terraform destroy` falla | Bloqueo `CanNotDelete` | Quitar `lock_enabled` de forma explícita |
