---
title: "FSLogix"
indice: avd
resumen: "Perfiles de usuario en contenedores para sesiones rápidas."
estado: documentado   # proximamente | en-curso | documentado
orden: 6
last_review: 2026-10-20
fuentes:
  - titulo: "User profile management with FSLogix profile containers"
    url: https://learn.microsoft.com/azure/virtual-desktop/fslogix-profile-containers
  - titulo: "FSLogix prerequisites (licencias y exclusiones de antivirus)"
    url: https://learn.microsoft.com/fslogix/overview-prerequisites
  - titulo: "FSLogix configuration examples"
    url: https://learn.microsoft.com/fslogix/concepts-configuration-examples
  - titulo: "Configure SMB storage permissions for FSLogix"
    url: https://learn.microsoft.com/fslogix/how-to-configure-storage-permissions
  - titulo: "Store FSLogix profile containers on Azure Files using Microsoft Entra ID"
    url: https://learn.microsoft.com/azure/virtual-desktop/create-profile-container-azure-ad
  - titulo: "Store FSLogix profile containers on Azure Files and AD DS"
    url: https://learn.microsoft.com/fslogix/how-to-configure-profile-container-azure-files-active-directory
  - titulo: "Storage options for FSLogix profile containers"
    url: https://learn.microsoft.com/azure/virtual-desktop/store-fslogix-profile
  - titulo: "Azure Files guidance for virtual desktop workloads"
    url: https://learn.microsoft.com/azure/storage/files/virtual-desktop-workloads
  - titulo: "Enable Microsoft Entra Kerberos authentication on Azure Files"
    url: https://learn.microsoft.com/azure/storage/files/storage-files-identity-auth-hybrid-identities-enable
  - titulo: "Assign share-level permissions for Azure file shares"
    url: https://learn.microsoft.com/azure/storage/files/storage-files-identity-assign-share-level-permissions
  - titulo: "Configure directory and file-level permissions for Azure file shares"
    url: https://learn.microsoft.com/azure/storage/files/storage-files-identity-configure-file-level-permissions
  - titulo: "Troubleshoot Azure Files identity-based authentication (SMB)"
    url: https://learn.microsoft.com/troubleshoot/azure/azure-storage/files/security/files-troubleshoot-smb-authentication
  - titulo: "Azure Files AD DS authentication and AES-256 Kerberos encryption"
    url: https://learn.microsoft.com/troubleshoot/azure/azure-storage/files/security/files-troubleshoot-encryption
  - titulo: "Support matrix for Azure Files backup"
    url: https://learn.microsoft.com/azure/backup/azure-file-share-support-matrix
  - titulo: "Store FSLogix profile containers on Azure NetApp Files"
    url: https://learn.microsoft.com/fslogix/how-to-configure-profile-container-netapp
  - titulo: "Microsoft.Storage storageAccounts/fileServices (plantillas ARM/Bicep)"
    url: https://learn.microsoft.com/azure/templates/microsoft.storage/storageaccounts/fileservices
  - titulo: "azurerm_storage_account"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/storage_account
  - titulo: "azurerm_storage_share"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/storage_share
  - titulo: "Módulo Terraform Storage/StorageAccount"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Storage/StorageAccount
  - titulo: "Módulo Terraform Storage/storage-account"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Storage/storage-account
  - titulo: "Módulo Terraform Storage/FileShare"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Storage/FileShare
---

**FSLogix** guarda el perfil completo de cada usuario en un disco virtual (VHDX) en un recurso compartido SMB y lo monta al iniciar sesión. Para Windows y las aplicaciones, el perfil está en el disco local. Es la pieza que permite que, en un [host pool](/recursos/avd/host-pools/) pooled, el usuario conserve escritorio, Outlook, Teams y configuración aunque cada día caiga en una VM distinta. **Viene instalado en las imágenes multisesión de AVD y su licencia va incluida** en las mismas licencias que dan derecho a AVD.

## Qué es y cuándo usarlo

### Cuándo sí y cuándo no

| Escenario | ¿FSLogix? | Motivo |
|---|---|---|
| Host pool pooled | **Sí, imprescindible** | El usuario cambia de host en cada conexión |
| Host pool personal | Normalmente no | El perfil vive en el disco de su VM |
| Host pool personal con hibernación | **No** | La hibernación no es compatible con FSLogix |
| Varias sesiones simultáneas del mismo usuario en un host pool | No soportado en AVD | AVD no admite conexiones múltiples dentro del mismo host pool |
| Ya hay otra solución de perfiles y solo falla Office | Contenedor ODFC | Solo redirige los datos de Microsoft 365 |

### Tipos de contenedor

| Contenedor | Qué guarda | Recomendación |
|---|---|---|
| **Profile container** | El perfil completo, incluidos los datos de Microsoft 365 | **El recomendado** (un único contenedor) |
| ODFC | Solo datos de Office (Outlook, Teams, OneDrive…) | Solo junto a otra solución de perfiles |

Licencias que dan derecho a FSLogix: Microsoft 365 E3/E5, A3/A5, F1/F3 y Business; Windows Enterprise E3/E5 y Education A3/A5; RDS CAL o SAL; y el acceso por usuario de Azure Virtual Desktop.

### Dónde guardar los perfiles

| | **Azure Files Premium** (recomendado) | Azure Files Standard | Azure NetApp Files |
|---|---|---|---|
| Disco | SSD, capacidad provisionada | HDD, pago por uso | Volúmenes en capacity pools (Standard, Premium, Ultra) |
| Cuándo | Medium, Heavy y Power; Light con más de 200 usuarios | Light con menos de 200 usuarios, dev/test | Escala muy grande o latencia ~1 ms |
| Identidad | AD DS, Entra Domain Services o **Microsoft Entra Kerberos** (híbridas, solo cloud y externas) | Igual | Solo AD DS o Entra Domain Services; **no admite identidades solo cloud** |
| Límites | 100 TiB por share; 10.000 handles en la raíz (soft en SSD) | 100 TiB por share | 3.000 perfiles concurrentes por volumen recomendados |
| Mínimo | 1 GiB por share | 1 GiB | Capacity pool de 1 TiB |

En todos los casos, **el almacenamiento tiene que estar en la misma región que los session hosts**.

### Cómo se autentican los hosts contra Azure Files

| Unión de los session hosts | Fuente de identidad de la cuenta | Línea de visión con los DC |
|---|---|---|
| **Microsoft Entra ID** (recomendado) | **Microsoft Entra Kerberos** (`AADKERB`) | No (solo para fijar ACLs con identidades híbridas) |
| Entra hybrid join | Microsoft Entra Kerberos o AD DS | No con Entra Kerberos |
| AD DS | AD DS (`AD`) | Sí |

Una cuenta de almacenamiento solo admite **una** fuente de identidad.

### Permisos: dos niveles

| Nivel | Qué se configura | Recomendación |
|---|---|---|
| Share (RBAC) | Rol por defecto para todas las identidades autenticadas | *Storage File Data SMB Share Contributor* |
| Share (RBAC) | Administradores que gestionan ACLs | *Storage File Data SMB Share Elevated Contributor* |
| NTFS en la raíz | `CREATOR OWNER`: Modificar (subcarpetas y archivos) | Cada usuario solo ve su carpeta |
| NTFS en la raíz | Grupo de administradores: Control total | Soporte y operación |
| NTFS en la raíz | Grupo de usuarios: Modificar (solo esta carpeta) | Pueden crear su carpeta de perfil |

### Configuración de FSLogix (ejemplo "Standard")

| Valor | Dato | Para qué |
|---|---|---|
| `Enabled` | 1 | Obligatorio |
| `VHDLocations` | `\\<cuenta>.file.core.windows.net\<share>` | Dónde se crean los contenedores |
| `VolumeType` | VHDX | Más tamaño y menos corrupción que VHD |
| `SizeInMBs` | 30000 | Tamaño máximo del disco dinámico |
| `DeleteLocalProfileWhenVHDShouldApply` | 1 | Evita perfiles locales con pérdida de datos |
| `FlipFlopProfileDirectoryName` | 1 | Carpetas `usuario_SID`, más fáciles de recorrer (**solo en despliegues nuevos**) |
| `ProfileType` | 0 | Una sola conexión por perfil |
| `LockedRetryCount` / `LockedRetryInterval` | 3 / 15 | Fallo más rápido si el VHDX está bloqueado |
| `ReAttachRetryCount` / `ReAttachIntervalSeconds` | 3 / 15 | Igual al reconectar |

Con Entra Kerberos, además en el host: `CloudKerberosTicketRetrievalEnabled = 1` y `LoadCredKeyFromProfile = 1`.

### Alta disponibilidad y continuidad

| Opción | Cómo | Cuándo |
|---|---|---|
| **ZRS** en la cuenta (recomendado) | Réplica síncrona en 3 zonas | Por defecto en producción |
| Cloud Cache | `CCDLocations` con 2+ proveedores; escribe en todos de forma asíncrona | Alta disponibilidad entre proveedores o DR entre regiones |
| DR sin recuperación de perfiles | Infraestructura duplicada en otra región; los usuarios estrenan perfil | Lo más simple; exige preparar a los usuarios |
| Azure Backup de Azure Files | Instantáneas y copia a almacén | Recuperar perfiles corruptos o borrados |

### Qué escenario recomiendo

| Escenario del cliente | Diseño | Por qué |
|---|---|---|
| Despliegue nuevo, hosts unidos a Entra ID | Azure Files Premium ZRS + Microsoft Entra Kerberos + Private Endpoint | Sin dependencia de los DC y todo en PaaS |
| Hosts unidos a AD DS | Azure Files Premium con la cuenta unida a AD DS y **AES-256** | Kerberos del dominio |
| Miles de usuarios concurrentes | Varios shares (o cuentas) repartidos por grupo con configuración por objeto, o Azure NetApp Files | Límites de handles y de IOPS |
| Requisito de continuidad regional | Cloud Cache con dos proveedores en regiones distintas | Perfil disponible en la región de respaldo |
| Usuarios solo cloud o externos | Microsoft Entra Kerberos con soporte de grupos solo cloud | Azure NetApp Files no los admite |

### Datos que conviene llevar a la reunión

- **FSLogix no se paga aparte**: va con Microsoft 365 E3/E5 y el resto de licencias de AVD; el coste es el almacenamiento.
- **Premium se factura por lo provisionado**, no por lo usado: el tamaño del share es una decisión de coste.
- **Con hosts unidos a Entra ID no hace falta AD** para los perfiles: Microsoft Entra Kerberos los sirve, también para identidades solo cloud.
- **Hay pasos en Entra ID fuera de la IaC**: consentimiento de administrador, exclusión de MFA y, con Private Endpoint, el FQDN de privatelink en la aplicación de la cuenta.
- **Cuentas unidas a AD DS: hay que pasar a AES-256.** Las actualizaciones de Windows Server de 2026 cambian el cifrado Kerberos por defecto y dejan atrás RC4; una cuenta sin actualizar puede dejar de montar los perfiles. Las cuentas con Microsoft Entra Kerberos no se ven afectadas.
- **Azure Backup de Azure Files necesita el acceso por clave de la cuenta activado.**
- **Sin exclusiones de antivirus**, los contenedores se corrompen: es la causa más común de incidencias.

## Decisiones de diseño

| Decisión | Lo que aplico | Por qué |
|---|---|---|
| Almacenamiento | Azure Files Premium (FileStorage) ZRS en la región de los hosts | Recomendación de Microsoft para la mayoría de clientes y resiliencia de zona |
| Identidad | Microsoft Entra Kerberos (`AADKERB`) | Hosts unidos a Entra ID sin línea de visión con los DC |
| SMB | Solo SMB 3.1.1, autenticación solo Kerberos, ticket AES-256 y cifrado de canal AES-GCM | Sin NTLM ni RC4 |
| Red | `public_network_access = false`, firewall en Deny, Private Endpoint `file` en `privatelink.file.core.windows.net` | Perfiles solo por red privada |
| Permisos | Share por defecto *SMB Share Contributor*; administradores *Elevated Contributor*; ACLs NTFS con `CREATOR OWNER` | Cada usuario solo accede a su perfil |
| Claves de la cuenta | Activadas solo porque Azure Backup las necesita; nadie monta con clave | Requisito de Azure Backup |
| Protección | Soft delete de shares (14 días) y Azure Backup diario | Recuperación ante borrado o corrupción |
| Configuración del host | Ejemplo "Standard" de FSLogix, VHDX, un único contenedor | La configuración más simple que recomienda Microsoft |
| Despliegue de la configuración | Run Command desde IaC, o imagen dorada o Intune | Igual en todos los hosts |
| Antivirus | Exclusiones de FSLogix en Defender (procesos, rutas, VHD/VHDX locales y del share) | Evita corrupción y perfiles temporales |
| Observabilidad | `StorageRead`, `StorageWrite`, `StorageDelete` y métrica `Transaction` del servicio de archivos | Diagnóstico de bloqueos y latencia |

Alineación con el Well-Architected Framework:

- **Seguridad**: red privada, Kerberos con AES-256 y sin NTLM, mínimo privilegio en share y NTFS.
- **Fiabilidad**: ZRS, soft delete, backup y, si hace falta, Cloud Cache.
- **Coste**: cuota provisionada ajustada al uso real; Standard solo para cargas Light pequeñas.
- **Excelencia operativa**: cuenta, share, permisos y configuración del host en IaC.
- **Rendimiento**: SSD en la misma región que los hosts y reparto entre shares si se acercan los límites de handles.

## Módulo de Terraform

### Los módulos del repositorio

| Pieza | Módulo | Estado |
|---|---|---|
| Cuenta de almacenamiento | [`Storage/StorageAccount`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Storage/StorageAccount) | **No utilizable con azurerm 4.x sin cambios** |
| Cuenta de almacenamiento (alternativa) | [`Storage/storage-account`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Storage/storage-account) | No sirve para FSLogix |
| File share | [`Storage/FileShare`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Storage/FileShare) | Utilizable con condiciones |

- **`Storage/StorageAccount`** usa `enable_https_traffic_only`, eliminado en azurerm 4.0 en favor de `https_traffic_only_enabled`. Su `versions.tf` admite `< 5.0.0`, así que falla en el `plan`. Además no expone `azure_files_authentication` ni `share_properties` (SMB y soft delete), imprescindibles para FSLogix.
- **`Storage/storage-account`** ya está en sintaxis 4.x, pero tampoco expone `azure_files_authentication` ni `share_properties`. No crea Private Endpoint y solo configura diagnósticos del servicio de blobs, con el bloque `metric`, que se elimina en azurerm 5.0.
- **`Storage/FileShare`** funciona (`storage_account_id`), pero usa `locals` y `count`, y su `versions.tf` admite azurerm 3.70, donde `storage_account_id` aún no existía en `azurerm_storage_share`.

En la ficha la cuenta y el share van con recursos nativos.

### Estructura en el proyecto

```txt
/
├── providers.tf
├── host_pools.tf / session_hosts.tf / application_groups.tf / workspaces.tf / scaling_plans.tf
├── fslogix.tf               # Azure Files, permisos, backup y configuración de los hosts
├── scripts/
│   ├── Register-AvdAgent.ps1
│   └── Set-FslogixProfile.ps1
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
      version = ">= 4.31.0, < 5.0.0" # 4.31.0: enabled_metric en diagnostic settings (fslogix.tf)
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

### Almacenamiento y configuración · `fslogix.tf`

```hcl
# =============================================================================
# FSLogix: Azure Files Premium con Microsoft Entra Kerberos, Private Endpoint,
# permisos de share, diagnósticos, backup y configuración de los session hosts
# DEPENDENCY: session_hosts.tf de la ficha Session Hosts en el mismo root (VMs con tag avd-group)
# DEPENDENCY: Subnet de Private Endpoints y zona privatelink.file.core.windows.net
# DEPENDENCY: Grupos de Entra ID de usuarios y administradores de perfiles
# DEPENDENCY: Tras el primer apply (pasos en Entra ID, fuera de Terraform):
#   - consentimiento de administrador a la app "[Storage Account] <cuenta>.file.core.windows.net"
#   - exclusión de esa app en las directivas de Conditional Access con MFA
#   - <cuenta>.privatelink.file.core.windows.net en identifierUris de la app (acceso por Private Endpoint)
#   - tag kdc_enable_cloud_group_sids en el manifiesto si hay identidades solo cloud
#   - ACLs NTFS de la raíz del share
# =============================================================================

variable "fslogix_storage" {
  description = "Cuentas de Azure Files para perfiles FSLogix (clave = nombre de la cuenta)."
  type = map(object({
    resource_group_name = string
    location            = string # la misma región que los session hosts
    replication_type    = optional(string, "ZRS") # Premium FileStorage: LRS o ZRS

    share_name     = optional(string, "profiles")
    share_quota_gb = number # cuota provisionada (Premium factura lo provisionado)

    identity_source = optional(string, "AADKERB") # AADKERB | AD
    # AADKERB con identidades híbridas (opcional, para gestionar ACLs desde el Explorador)
    # o AD (obligatorio con todos sus campos)
    active_directory = optional(object({
      domain_name         = string
      domain_guid         = string
      domain_sid          = optional(string)
      storage_sid         = optional(string)
      forest_name         = optional(string)
      netbios_domain_name = optional(string)
    }))

    default_share_level_permission = optional(string, "StorageFileDataSmbShareContributor")
    admin_group_object_ids         = optional(map(string), {}) # Elevated Contributor (ACLs y soporte)

    share_soft_delete_days    = optional(number, 14)
    shared_access_key_enabled = optional(bool, true) # Azure Backup de Azure Files necesita las claves

    private_endpoint = object({
      subnet_id           = string
      private_dns_zone_id = string # privatelink.file.core.windows.net
    })

    backup = optional(object({
      recovery_vault_name           = string
      recovery_vault_resource_group = string
      backup_policy_id              = string # política de tipo Azure File Share
    }))

    log_analytics_workspace_id = string
    tags                       = optional(map(string), {})
  }))
  default = {}

  validation {
    condition     = alltrue([for k, v in var.fslogix_storage : can(regex("^[a-z0-9]{3,24}$", k))])
    error_message = "El nombre de la cuenta: 3-24 caracteres, minúsculas y números."
  }

  validation {
    condition     = alltrue([for k, v in var.fslogix_storage : contains(["LRS", "ZRS"], v.replication_type)])
    error_message = "Azure Files Premium (FileStorage) solo admite LRS o ZRS."
  }

  validation {
    condition = alltrue([
      for k, v in var.fslogix_storage :
      contains(["AADKERB", "AD"], v.identity_source) && (v.identity_source != "AD" || v.active_directory != null)
    ])
    error_message = "identity_source debe ser AADKERB o AD; con AD, active_directory es obligatorio."
  }

  validation {
    condition     = alltrue([for k, v in var.fslogix_storage : v.backup == null || v.shared_access_key_enabled])
    error_message = "Azure Backup de Azure Files necesita shared_access_key_enabled = true."
  }
}

variable "fslogix_session_hosts" {
  description = "Configuración de FSLogix por grupo de session hosts (clave = grupo de var.session_hosts)."
  type = map(object({
    storage        = string # clave de var.fslogix_storage
    size_in_mbs    = optional(number, 30000)
    entra_kerberos = optional(bool, true) # false con session hosts unidos a AD DS
  }))
  default = {}
}

resource "azurerm_storage_account" "fslogix" {
  for_each                 = var.fslogix_storage
  name                     = each.key
  resource_group_name      = each.value.resource_group_name
  location                 = each.value.location
  account_kind             = "FileStorage"
  account_tier             = "Premium"
  account_replication_type = each.value.replication_type

  min_tls_version                 = "TLS1_2"
  https_traffic_only_enabled      = true
  public_network_access_enabled   = false
  shared_access_key_enabled       = each.value.shared_access_key_enabled
  allow_nested_items_to_be_public = false
  cross_tenant_replication_enabled = false

  network_rules {
    default_action = "Deny"
    bypass         = ["AzureServices"] # Azure Backup es un servicio de confianza
  }

  azure_files_authentication {
    directory_type                 = each.value.identity_source
    default_share_level_permission = each.value.default_share_level_permission

    dynamic "active_directory" {
      for_each = each.value.active_directory != null ? [each.value.active_directory] : []
      content {
        domain_name         = active_directory.value.domain_name
        domain_guid         = active_directory.value.domain_guid
        domain_sid          = active_directory.value.domain_sid
        storage_sid         = active_directory.value.storage_sid
        forest_name         = active_directory.value.forest_name
        netbios_domain_name = active_directory.value.netbios_domain_name
      }
    }
  }

  share_properties {
    retention_policy {
      days = each.value.share_soft_delete_days
    }

    smb {
      versions                        = ["SMB3.1.1"]
      authentication_types            = ["Kerberos"]
      kerberos_ticket_encryption_type = ["AES-256"] # sin RC4
      channel_encryption_type         = ["AES-128-GCM", "AES-256-GCM"]
    }
  }

  tags = merge(var.tags, each.value.tags)
}

resource "azurerm_storage_share" "fslogix" {
  for_each           = var.fslogix_storage
  name               = each.value.share_name
  storage_account_id = azurerm_storage_account.fslogix[each.key].id
  quota              = each.value.share_quota_gb
  enabled_protocol   = "SMB"
}

resource "azurerm_private_endpoint" "fslogix" {
  for_each            = var.fslogix_storage
  name                = "pe-${each.key}-file"
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  subnet_id           = each.value.private_endpoint.subnet_id

  private_service_connection {
    name                           = "psc-${each.key}-file"
    private_connection_resource_id = azurerm_storage_account.fslogix[each.key].id
    subresource_names              = ["file"]
    is_manual_connection           = false
  }

  private_dns_zone_group {
    name                 = "default"
    private_dns_zone_ids = [each.value.private_endpoint.private_dns_zone_id]
  }

  tags = merge(var.tags, each.value.tags)
}

# Administradores de perfiles: pueden fijar ACLs NTFS sin usar la clave de la cuenta
resource "azurerm_role_assignment" "fslogix_admin" {
  for_each = {
    for item in flatten([
      for sk, s in var.fslogix_storage : [
        for gk, oid in s.admin_group_object_ids : { key = "${sk}/${gk}", storage = sk, principal_id = oid }
      ]
    ]) : item.key => item
  }

  scope                = azurerm_storage_share.fslogix[each.value.storage].id
  role_definition_name = "Storage File Data SMB Share Elevated Contributor"
  principal_id         = each.value.principal_id
  principal_type       = "Group"
}

resource "azurerm_monitor_diagnostic_setting" "fslogix_files" {
  for_each                   = var.fslogix_storage
  name                       = "diag-${each.key}-file"
  target_resource_id         = "${azurerm_storage_account.fslogix[each.key].id}/fileServices/default"
  log_analytics_workspace_id = each.value.log_analytics_workspace_id

  enabled_log {
    category = "StorageRead"
  }
  enabled_log {
    category = "StorageWrite"
  }
  enabled_log {
    category = "StorageDelete"
  }
  enabled_metric {
    category = "Transaction"
  }
}

resource "azurerm_backup_container_storage_account" "fslogix" {
  for_each            = { for k, v in var.fslogix_storage : k => v if v.backup != null }
  resource_group_name = each.value.backup.recovery_vault_resource_group
  recovery_vault_name = each.value.backup.recovery_vault_name
  storage_account_id  = azurerm_storage_account.fslogix[each.key].id
}

resource "azurerm_backup_protected_file_share" "fslogix" {
  for_each                  = { for k, v in var.fslogix_storage : k => v if v.backup != null }
  resource_group_name       = each.value.backup.recovery_vault_resource_group
  recovery_vault_name       = each.value.backup.recovery_vault_name
  source_storage_account_id = azurerm_backup_container_storage_account.fslogix[each.key].storage_account_id
  source_file_share_name    = azurerm_storage_share.fslogix[each.key].name
  backup_policy_id          = each.value.backup.backup_policy_id
}

# Configuración de FSLogix, Entra Kerberos y exclusiones de antivirus en cada session host
resource "azurerm_virtual_machine_run_command" "fslogix" {
  for_each = {
    for k, vm in azurerm_windows_virtual_machine.session_host : k => vm
    if contains(keys(var.fslogix_session_hosts), vm.tags["avd-group"])
  }

  name               = "Set-FslogixProfile"
  location           = each.value.location
  virtual_machine_id = each.value.id

  source {
    script = file("${path.root}/scripts/Set-FslogixProfile.ps1")
  }

  parameter {
    name  = "VhdLocation"
    value = "\\\\${azurerm_storage_account.fslogix[var.fslogix_session_hosts[each.value.tags["avd-group"]].storage].name}.file.core.windows.net\\${azurerm_storage_share.fslogix[var.fslogix_session_hosts[each.value.tags["avd-group"]].storage].name}"
  }

  parameter {
    name  = "SizeInMBs"
    value = tostring(var.fslogix_session_hosts[each.value.tags["avd-group"]].size_in_mbs)
  }

  parameter {
    name  = "EntraKerberos"
    value = tostring(var.fslogix_session_hosts[each.value.tags["avd-group"]].entra_kerberos)
  }

  tags = each.value.tags
}

output "fslogix_vhd_locations" {
  description = "Rutas UNC para VHDLocations."
  value = {
    for k, s in azurerm_storage_share.fslogix :
    k => "\\\\${azurerm_storage_account.fslogix[k].name}.file.core.windows.net\\${s.name}"
  }
}
```

### Configuración del host · `scripts/Set-FslogixProfile.ps1`

```powershell
# Configura FSLogix Profile Container (ejemplo "Standard" de la documentación de FSLogix),
# Microsoft Entra Kerberos para Azure Files y las exclusiones de antivirus de Defender.
# En producción, el mismo contenido puede ir en la imagen dorada o en una directiva de Intune.
param(
    [Parameter(Mandatory = $true)]
    [string] $VhdLocation,            # \\<cuenta>.file.core.windows.net\<share>

    [int]    $SizeInMBs = 30000,

    [string] $EntraKerberos = 'true'  # 'true' en session hosts unidos a Microsoft Entra ID
)

$ErrorActionPreference = 'Stop'

# --- FSLogix Profile Container ------------------------------------------------
$fslogix = 'HKLM:\SOFTWARE\FSLogix\Profiles'
New-Item -Path $fslogix -Force | Out-Null

$dword = @{
    Enabled                              = 1
    DeleteLocalProfileWhenVHDShouldApply = 1
    FlipFlopProfileDirectoryName         = 1   # solo en despliegues nuevos
    LockedRetryCount                     = 3
    LockedRetryInterval                  = 15
    ProfileType                          = 0
    ReAttachIntervalSeconds              = 15
    ReAttachRetryCount                   = 3
    SizeInMBs                            = $SizeInMBs
}
foreach ($name in $dword.Keys) {
    New-ItemProperty -Path $fslogix -Name $name -PropertyType DWord -Value $dword[$name] -Force | Out-Null
}
New-ItemProperty -Path $fslogix -Name 'VolumeType'   -PropertyType String      -Value 'VHDX'          -Force | Out-Null
New-ItemProperty -Path $fslogix -Name 'VHDLocations' -PropertyType MultiString -Value @($VhdLocation) -Force | Out-Null

# --- Microsoft Entra Kerberos (session hosts unidos a Entra ID) ----------------
if ($EntraKerberos -eq 'true') {
    $kerberos = 'HKLM:\SYSTEM\CurrentControlSet\Control\Lsa\Kerberos\Parameters'
    New-Item -Path $kerberos -Force | Out-Null
    New-ItemProperty -Path $kerberos -Name 'CloudKerberosTicketRetrievalEnabled' -PropertyType DWord -Value 1 -Force | Out-Null

    $aadAccount = 'HKLM:\SOFTWARE\Policies\Microsoft\AzureADAccount'
    New-Item -Path $aadAccount -Force | Out-Null
    New-ItemProperty -Path $aadAccount -Name 'LoadCredKeyFromProfile' -PropertyType DWord -Value 1 -Force | Out-Null
}

# --- Exclusiones de antivirus (Microsoft Defender) -----------------------------
if (Get-Command -Name Add-MpPreference -ErrorAction SilentlyContinue) {
    $share = $VhdLocation.TrimEnd('\')
    Add-MpPreference -ExclusionProcess @('frxsvc.exe', 'frxccds.exe')
    Add-MpPreference -ExclusionPath @(
        "$env:ProgramFiles\FSLogix\Apps"
        "$env:ProgramData\FSLogix"
        '%TEMP%\*\*.VHD', '%TEMP%\*\*.VHDX'
        "$env:windir\TEMP\*\*.VHD", "$env:windir\TEMP\*\*.VHDX"
        "$share\*\*.VHD", "$share\*\*.VHD.lock", "$share\*\*.VHD.meta", "$share\*\*.VHD.metadata"
        "$share\*\*.VHDX", "$share\*\*.VHDX.lock", "$share\*\*.VHDX.meta", "$share\*\*.VHDX.metadata"
    )
}

Write-Output "FSLogix configurado con VHDLocations = $VhdLocation. Reiniciar el host para aplicar la configuración de Kerberos."
```

### `env/pro.tfvars`

```hcl
tags = {
  environment = "pro"
  workload    = "<workload>"
  owner       = "<owner>"
  costcenter  = "<costcenter>"
}

fslogix_storage = {
  "stfslogix<workload>pro01" = {
    resource_group_name = "<rg-avd-pro>"
    location            = "<region>"
    replication_type    = "ZRS"

    share_name     = "profiles"
    share_quota_gb = 2048 # p. ej. 100 usuarios x ~20 GB de perfil medio; revisar con el uso real

    identity_source = "AADKERB"

    admin_group_object_ids = {
      admins-avd = "<objectId grupo administradores AVD>"
    }

    private_endpoint = {
      subnet_id           = "<resourceId snet-privateendpoints>"
      private_dns_zone_id = "<resourceId privatelink.file.core.windows.net>"
    }

    backup = {
      recovery_vault_name           = "<rsv-avd-pro>"
      recovery_vault_resource_group = "<rg-backup-pro>"
      backup_policy_id              = "<resourceId política Azure File Share diaria>"
    }

    log_analytics_workspace_id = "<resourceId log-analytics-workspace>"
  }
}

# Solo los host pools pooled; los personales guardan el perfil en el disco de la VM
fslogix_session_hosts = {
  pooled-01 = {
    storage = "stfslogix<workload>pro01"
  }
}
```

En `dev.tfvars` y `pre.tfvars`: `replication_type = "LRS"`, cuota pequeña y sin `backup`.

### Pasos después del primer `apply`

1. **Consentimiento de administrador**: Entra ID → App registrations → *All applications* → `[Storage Account] <cuenta>.file.core.windows.net` → API permissions → *Grant admin consent*.
2. **Excluir esa aplicación** de las directivas de Conditional Access que exigen MFA.
3. **Private Endpoint**: en el manifiesto de la aplicación, añadir `<cuenta>.privatelink.file.core.windows.net` junto a cada `<cuenta>.file.core.windows.net` de `identifierUris`.
4. **Identidades solo cloud**: añadir el tag `kdc_enable_cloud_group_sids` en el manifiesto.
5. **ACLs NTFS de la raíz**, con un usuario del grupo administrador:
   - Con identidades híbridas, desde un equipo con línea de visión a los DC y con `icacls`.
   - Con identidades solo cloud, desde *Manage access* del share en el portal.

```powershell
$share = "\\<cuenta>.file.core.windows.net\profiles"
icacls $share /inheritance:r
icacls $share /grant:r "CREATOR OWNER:(OI)(CI)(IO)(M)"
icacls $share /grant:r "<DOMINIO>\<grupo-admins-avd>:(OI)(CI)(F)"
icacls $share /grant:r "<DOMINIO>\<grupo-usuarios-avd>:(M)"
```

Despliegue y comprobación:

```powershell
terraform init
terraform plan -var-file="env/pro.tfvars" -out="pro.tfplan"
terraform apply "pro.tfplan"

# En un session host, con un usuario de AVD: ticket Kerberos de la cuenta y perfil montado
klist get cifs/<cuenta>.file.core.windows.net
Get-ItemProperty -Path "HKLM:\SOFTWARE\FSLogix\Profiles" | Select-Object Enabled, VHDLocations, VolumeType
```

### Equivalente en Bicep

`main.bicep` (la configuración del host es la misma que en Terraform: imagen, Intune o el script con Run Command):

```bicep
// =============================================================================
// Azure Files Premium para perfiles FSLogix: Microsoft Entra Kerberos, SMB endurecido,
// Private Endpoint, permisos de share y diagnósticos
// DEPENDENCY: Resource Group existente (targetScope = resourceGroup)
// DEPENDENCY: Subnet de Private Endpoints y zona privatelink.file.core.windows.net
// DEPENDENCY: Grupo de Entra ID de administradores de perfiles
// DEPENDENCY: Pasos posteriores en Entra ID (consentimiento, exclusión de MFA, identifierUris de private link)
// =============================================================================
targetScope = 'resourceGroup'

param location string = resourceGroup().location

@minLength(3)
@maxLength(24)
param storageAccountName string

@allowed(['Premium_ZRS', 'Premium_LRS'])
param skuName string = 'Premium_ZRS'

param shareName string = 'profiles'

@description('Cuota provisionada en GiB (Premium factura lo provisionado).')
@minValue(1)
param shareQuotaGiB int

@allowed(['StorageFileDataSmbShareContributor', 'StorageFileDataSmbShareReader', 'StorageFileDataSmbShareElevatedContributor', 'None'])
param defaultSharePermission string = 'StorageFileDataSmbShareContributor'

@description('true si se usa Azure Backup para el share (lo exige).')
param allowSharedKeyAccess bool = true

param shareSoftDeleteDays int = 14

param adminGroupObjectIds array = []

param privateEndpointSubnetId string
param privateDnsZoneId string
param logAnalyticsWorkspaceId string

param tags object = {}

// Storage File Data SMB Share Elevated Contributor (rol integrado)
var elevatedContributorRoleId = 'a7264617-510b-434b-a828-9731dc254ea7'

resource storage 'Microsoft.Storage/storageAccounts@2024-01-01' = {
  name: storageAccountName
  location: location
  tags: tags
  kind: 'FileStorage'
  sku: {
    name: skuName
  }
  properties: {
    minimumTlsVersion: 'TLS1_2'
    supportsHttpsTrafficOnly: true
    publicNetworkAccess: 'Disabled'
    allowSharedKeyAccess: allowSharedKeyAccess
    allowBlobPublicAccess: false
    allowCrossTenantReplication: false
    networkAcls: {
      defaultAction: 'Deny'
      bypass: 'AzureServices'
    }
    azureFilesIdentityBasedAuthentication: {
      directoryServiceOptions: 'AADKERB'
      defaultSharePermission: defaultSharePermission
    }
  }
}

resource fileServices 'Microsoft.Storage/storageAccounts/fileServices@2024-01-01' = {
  parent: storage
  name: 'default'
  properties: {
    shareDeleteRetentionPolicy: {
      enabled: true
      days: shareSoftDeleteDays
    }
    protocolSettings: {
      smb: {
        versions: 'SMB3.1.1;'
        authenticationMethods: 'Kerberos;'
        kerberosTicketEncryption: 'AES-256;'
        channelEncryption: 'AES-128-GCM;AES-256-GCM;'
      }
    }
  }
}

resource share 'Microsoft.Storage/storageAccounts/fileServices/shares@2024-01-01' = {
  parent: fileServices
  name: shareName
  properties: {
    shareQuota: shareQuotaGiB
    enabledProtocols: 'SMB'
  }
}

resource privateEndpoint 'Microsoft.Network/privateEndpoints@2024-05-01' = {
  name: 'pe-${storageAccountName}-file'
  location: location
  tags: tags
  properties: {
    subnet: {
      id: privateEndpointSubnetId
    }
    privateLinkServiceConnections: [
      {
        name: 'psc-${storageAccountName}-file'
        properties: {
          privateLinkServiceId: storage.id
          groupIds: [
            'file'
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
        name: 'privatelink-file-core-windows-net'
        properties: {
          privateDnsZoneId: privateDnsZoneId
        }
      }
    ]
  }
}

resource adminAccess 'Microsoft.Authorization/roleAssignments@2022-04-01' = [
  for oid in adminGroupObjectIds: {
    name: guid(share.id, oid, elevatedContributorRoleId)
    scope: share
    properties: {
      principalId: oid
      principalType: 'Group'
      roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', elevatedContributorRoleId)
    }
  }
]

resource diagnostics 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = {
  name: 'diag-${storageAccountName}-file'
  scope: fileServices
  properties: {
    workspaceId: logAnalyticsWorkspaceId
    logs: [
      { category: 'StorageRead', enabled: true }
      { category: 'StorageWrite', enabled: true }
      { category: 'StorageDelete', enabled: true }
    ]
    metrics: [
      { category: 'Transaction', enabled: true }
    ]
  }
}

output storageAccountId string = storage.id
output vhdLocation string = '\\\\${storage.name}.file.${environment().suffixes.storage}\\${share.name}'
```

`main.pro.bicepparam`:

```bicep
using 'main.bicep'

param storageAccountName = 'stfslogixwkldpro01'
param skuName = 'Premium_ZRS'
param shareName = 'profiles'
param shareQuotaGiB = 2048

param adminGroupObjectIds = [
  '<objectId grupo administradores AVD>'
]

param privateEndpointSubnetId = '<resourceId snet-privateendpoints>'
param privateDnsZoneId = '<resourceId privatelink.file.core.windows.net>'
param logAnalyticsWorkspaceId = '<resourceId log-analytics-workspace>'

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
| `Unsupported argument "enable_https_traffic_only"` en el `plan` | Módulo escrito para azurerm 3.x | Usar `https_traffic_only_enabled` |
| El usuario entra con perfil temporal o local | Sin acceso al share, falta un permiso o había un perfil local previo | Revisar RBAC y NTFS, `DeleteLocalProfileWhenVHDShouldApply = 1` y borrar perfiles locales antiguos |
| Error 1326 *"The username or password is incorrect"* al montar por Private Endpoint | El FQDN de privatelink no está en la aplicación de la cuenta | Añadirlo a `identifierUris` |
| Error 1327 *"Account restrictions are preventing this user from signing in"* | Conditional Access exige MFA a la aplicación de la cuenta | Excluir la aplicación de la directiva |
| No se obtiene ticket Kerberos para la cuenta | Falta el consentimiento de administrador o `CloudKerberosTicketRetrievalEnabled` | Conceder consentimiento y aplicar la clave en el host (reiniciar) |
| Usuarios solo cloud sin acceso | Falta `kdc_enable_cloud_group_sids` en el manifiesto | Añadir el tag |
| Error de Graph al activar Entra Kerberos | Una directiva de aplicaciones bloquea credenciales del *Storage Resource Provider* | Excepción para la app `a6aa9161-5291-40bb-8c5c-923b567bee3b` |
| Fallos de montaje tras actualizar Windows Server en cuentas unidas a AD DS | El cifrado Kerberos por defecto deja de ser RC4 | Pasar la cuenta a AES-256 (`Update-AzStorageAccountAuthForAES256`) |
| Montaje con Entra Kerberos falla por tipo de cifrado | Directiva del cliente que no permite AES-256 (`SupportedEncryptionTypes`) | Permitir AES-256 en la directiva de Kerberos |
| Accesos intermitentes tras cambios de red | El cliente pierde la configuración de KDC proxy | GPO *Specify KDC proxy servers for Kerberos clients* |
| El backup del share falla con `UserErrorStorageKeyBasedAuthenticationNotPermitted` | Acceso por clave desactivado | `shared_access_key_enabled = true` |
| Inicios de sesión lentos o *ERROR_SHARING_VIOLATION* | El antivirus escanea los VHDX o los procesos de FSLogix | Aplicar todas las exclusiones de FSLogix |
| Usuarios con perfil nuevo vacío tras un cambio de configuración | Se activó `FlipFlopProfileDirectoryName` (o patrones de nombre) en un entorno existente | No cambiarlo en despliegues con perfiles; revertir y recuperar |
| Varios usuarios no pueden iniciar sesión a la vez en un share grande | Límite de handles en la raíz del share | Repartir usuarios entre shares o activar los límites ampliados en SSD |
| La hibernación de un host personal falla | FSLogix no es compatible con la hibernación | No usar FSLogix en ese host pool o no hibernar |
