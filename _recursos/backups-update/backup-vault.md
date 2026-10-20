---
title: "Backup Vault"
indice: backups-update
resumen: "Almacén para copias de discos, blobs y bases de datos PaaS."
estado: documentado   # proximamente | en-curso | documentado
orden: 2
last_review: 2026-10-20
fuentes:
  - titulo: "Backup vaults overview"
    url: https://learn.microsoft.com/azure/backup/backup-vault-overview
  - titulo: "Create and delete Backup vaults"
    url: https://learn.microsoft.com/azure/backup/create-manage-backup-vault
  - titulo: "Azure Backup - Frequently asked questions (tipos de almacén)"
    url: https://learn.microsoft.com/azure/backup/backup-azure-backup-faq
  - titulo: "Support matrix for Azure Backup"
    url: https://learn.microsoft.com/azure/backup/backup-support-matrix
  - titulo: "Secure by default with soft delete for Azure Backup"
    url: https://learn.microsoft.com/azure/backup/secure-by-default
  - titulo: "Immutable vault for Azure Backup"
    url: https://learn.microsoft.com/azure/backup/backup-azure-immutable-vault-concept
  - titulo: "Multiuser authorization using Resource Guard"
    url: https://learn.microsoft.com/azure/backup/multi-user-authorization-concept
  - titulo: "Configure Multi-user authorization using Resource Guard (Backup vault)"
    url: https://learn.microsoft.com/azure/backup/multi-user-authorization?pivots=vaults-backup-vault
  - titulo: "Set-AzDataProtectionResourceGuardMapping"
    url: https://learn.microsoft.com/powershell/module/az.dataprotection/set-azdataprotectionresourceguardmapping
  - titulo: "Encrypt backup data in a Backup vault by using customer-managed keys"
    url: https://learn.microsoft.com/azure/backup/encryption-at-rest-with-cmk-for-backup-vault
  - titulo: "Overview of Azure Disk Backup"
    url: https://learn.microsoft.com/azure/backup/disk-backup-overview
  - titulo: "Azure Disk Backup support matrix"
    url: https://learn.microsoft.com/azure/backup/disk-backup-support-matrix
  - titulo: "Back up Azure Disks using Azure portal (permisos)"
    url: https://learn.microsoft.com/azure/backup/backup-managed-disks
  - titulo: "Troubleshooting backup failures in Azure Disk Backup"
    url: https://learn.microsoft.com/azure/backup/disk-backup-troubleshoot
  - titulo: "Overview of Azure Blob backup"
    url: https://learn.microsoft.com/azure/backup/blob-backup-overview
  - titulo: "Configure vaulted backup for Azure Blobs"
    url: https://learn.microsoft.com/azure/backup/blob-backup-configure-tutorial
  - titulo: "About Azure Data Lake Storage vaulted backup"
    url: https://learn.microsoft.com/azure/backup/azure-data-lake-storage-backup-overview
  - titulo: "About Azure Database for PostgreSQL - Flexible Server backup"
    url: https://learn.microsoft.com/azure/backup/backup-azure-database-postgresql-flex-overview
  - titulo: "Support matrix for Azure Database for PostgreSQL - Flexible Server vaulted backup"
    url: https://learn.microsoft.com/azure/backup/backup-azure-database-postgresql-flex-support-matrix
  - titulo: "About Azure PostgreSQL flexible server and elastic cluster vaulted backup (v2) (preview)"
    url: https://learn.microsoft.com/azure/backup/backup-azure-postgresql-flex-server-elastic-cluster-v2-overview
  - titulo: "What is Azure Kubernetes Service backup?"
    url: https://learn.microsoft.com/azure/backup/azure-kubernetes-service-backup-overview
  - titulo: "Prerequisites for Azure Kubernetes Service backup"
    url: https://learn.microsoft.com/azure/backup/azure-kubernetes-service-cluster-backup-concept
  - titulo: "Manage Azure Monitor based alerts for Azure Backup"
    url: https://learn.microsoft.com/azure/backup/backup-azure-monitoring-alerts
  - titulo: "Diagnostic Events for Azure Backup users"
    url: https://learn.microsoft.com/azure/backup/backup-azure-diagnostic-events
  - titulo: "Supported logs for Microsoft.DataProtection/BackupVaults"
    url: https://learn.microsoft.com/azure/azure-monitor/reference/supported-logs/microsoft-dataprotection-backupvaults-logs
  - titulo: "Create a disk backup policy with the REST API"
    url: https://learn.microsoft.com/azure/backup/backup-azure-dataprotection-use-rest-api-create-update-disk-policy
  - titulo: "Microsoft.DataProtection backupVaults (plantillas ARM/Bicep)"
    url: https://learn.microsoft.com/azure/templates/microsoft.dataprotection/backupvaults
  - titulo: "Azure built-in roles for Compute (Disk Snapshot Contributor)"
    url: https://learn.microsoft.com/azure/role-based-access-control/built-in-roles/compute
  - titulo: "azurerm_data_protection_backup_vault"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/data_protection_backup_vault
  - titulo: "azurerm_data_protection_backup_policy_disk"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/data_protection_backup_policy_disk
  - titulo: "Azure Verified Module: Data Protection Backup Vault (Terraform)"
    url: https://github.com/Azure/terraform-azurerm-avm-res-dataprotection-backupvault
---

El **Backup vault** es el almacén de Azure Backup para las cargas "nuevas": discos administrados, blobs, Data Lake Storage, Azure Database for PostgreSQL flexible server y AKS. No sustituye al [Recovery Services vault](/recursos/backups-update/recovery-services-vault/): cada carga tiene su almacén y no se elige. Lo que cambia frente al Recovery Services vault es el modelo. **El almacén accede a los orígenes con su identidad gestionada**, así que cada copia necesita roles concretos sobre el disco, la cuenta o el servidor. Además, varias cargas guardan las copias **en tu propia suscripción** (nivel operacional) y no en el almacén.

## Qué es y cuándo usarlo

### Qué va a cada almacén

| Carga | Almacén |
|---|---|
| VMs de Azure, SQL Server y SAP HANA en VMs, Azure Files, MARS, MABS, DPM | [Recovery Services vault](/recursos/backups-update/recovery-services-vault/) |
| **Discos administrados** | **Backup vault** |
| **Blobs** y **Azure Data Lake Storage** | **Backup vault** |
| **Azure Database for PostgreSQL flexible server** | **Backup vault** |
| **AKS** | **Backup vault** |

### Niveles de copia por carga

| Carga | Dónde queda la copia | Lo que conviene saber |
|---|---|---|
| Discos | **Operacional**: snapshots incrementales en un RG de tu suscripción | Sin copia al almacén. Máximo 1 año o 450 snapshots por disco |
| Blobs | Operacional (restauración a un punto en el tiempo, hasta 360 días) **y** copia al almacén (hasta 10 años) | Las políticas nuevas incluyen siempre la copia al almacén |
| Data Lake Storage | Copia al almacén, hasta 10 años | Hasta 1.000 contenedores por cuenta |
| PostgreSQL flexible (v1, GA) | Almacén, copia lógica (`pg_dump`) | **Semanal**, servidores de hasta 1 TB, se restaura como ficheros |
| PostgreSQL flexible y elastic cluster (v2, preview) | Almacén, snapshots de disco incrementales | Diaria, hasta 32/64 TB, se restaura como servidor; PostgreSQL 15+ |
| AKS | Operacional (snapshots) y, opcionalmente, almacén | Requiere extensión de backup y *Trusted Access* |

**El nivel operacional no lo protegen ni la inmutabilidad ni el soft delete del almacén**: aplican solo a lo que está en el almacén. CMK tampoco cifra el nivel operacional.

### Permisos que necesita el almacén

| Carga | Rol para la identidad del almacén | Ámbito |
|---|---|---|
| Discos | *Disk Backup Reader* | Disco (o su RG o suscripción) |
| Discos | *Disk Snapshot Contributor* | RG de snapshots |
| Discos con DES | *Reader* | Disk Encryption Set |
| Discos, restauración | *Disk Restore Operator* | RG de destino |
| Blobs y Data Lake | *Storage Account Backup Contributor* | Cuenta (o RG) |
| PostgreSQL flexible (v1) | *PostgreSQL Flexible Server Long Term Retention Backup Role* + *Reader* | Servidor + su RG |
| AKS | *Reader* en el clúster y en el RG de snapshots, entre otros | Ver los prerrequisitos de AKS |

Los roles pueden tardar hasta 30 minutos en aplicarse.

### Seguridad del almacén

| Capacidad | Qué hace | Reversible |
|---|---|---|
| **Soft delete** | Conserva 14-180 días lo borrado (14 sin coste) | `On` sí; **`AlwaysOn` no** |
| **Inmutabilidad** `Unlocked` | Bloquea operaciones que pierden puntos de recuperación | Sí |
| **Inmutabilidad** `Locked` | Lo mismo con almacenamiento WORM | **No** |
| **MUA** | Operaciones críticas con permiso sobre un Resource Guard ajeno | Sí, con aprobación |
| **CMK** | Cifra los niveles de almacén y archivo con tu clave | **No** se vuelve a claves de plataforma |

- **Soft delete obligatorio (secure by default)**: en Backup vaults solo es GA en Australia East, West Central US y East Asia. En el resto está en preview y el portal todavía permite desactivarlo.
- **CMK** se puede activar antes o después de proteger elementos (en el Recovery Services vault, solo antes). Infraestructura con doble cifrado solo al crear el almacén.
- **No hay Private Endpoints para Backup vaults.**

### Redundancia y Cross Region Restore

| Opción | Cuándo |
|---|---|
| **GRS** | Producción: copia en la región emparejada |
| GRS + Cross Region Restore | Restaurar PostgreSQL o AKS en la región secundaria sin esperar a un desastre declarado; se cobra a precio RA-GRS |
| ZRS | Residencia del dato en la región |
| LRS | Dev/test |

**La redundancia no se puede cambiar después de proteger elementos**, y Cross Region Restore no se puede desactivar. La redundancia del almacén no afecta a los snapshots operacionales de discos.

### Cómo se factura

| Carga | Conceptos |
|---|---|
| Discos | Solo los snapshots incrementales (almacenamiento estándar) en tu suscripción. **Sin tarifa de instancia protegida** |
| Blobs operacional | Sin tarifa de instancia; pagas la retención de versiones, soft delete y change feed, y las restauraciones |
| Blobs y Data Lake con copia al almacén | Instancia protegida (según tamaño) + transacciones + almacenamiento del almacén |
| PostgreSQL flexible | Instancia protegida por bloques de 250 GB + almacenamiento del almacén |
| Soft delete | Gratis hasta 14 días de retención |

### Límites que conviene conocer

| Límite | Valor |
|---|---|
| Almacenes por suscripción | 500 (Recovery Services y Backup vaults) |
| Disco ↔ almacén | Misma región; pueden estar en suscripciones distintas |
| RG de snapshots | Misma suscripción que el disco; **no se puede cambiar** después de configurar |
| Retención de discos | 1 año o 450 snapshots, lo que llegue antes |
| Discos con ADE | No soportados |
| PostgreSQL v1 | 1 TB por servidor, una copia por semana |

### Qué escenario recomiendo

| Escenario del cliente | Diseño | Por qué |
|---|---|---|
| Discos de datos fuera de VMs protegidas, o con RPO de horas | Política de discos cada 4 horas y RG de snapshots dedicado | Snapshots rápidos sin agente |
| VMs completas | [Recovery Services vault](/recursos/backups-update/recovery-services-vault/), no el Backup vault | Consistencia de aplicación y restauración de ficheros |
| Cuentas de datos críticas o requisitos anti-ransomware | Blobs con copia al almacén, inmutabilidad y MUA | El operacional vive en la propia cuenta |
| PostgreSQL con retención larga | Política semanal en almacén; v2 si se necesita diario o más de 1 TB (preview) | Retención de hasta 10 años |
| Producción estándar | GRS, soft delete `AlwaysOn`, inmutabilidad `Unlocked` → `Locked`, MUA | Nivel *Excellent* |

### Datos que conviene llevar a la reunión

- **El Backup vault no se elige: lo marca la carga.** VMs y Azure Files van al Recovery Services vault.
- **Los discos se copian como snapshots en la suscripción del cliente.** Ni la inmutabilidad ni el soft delete del almacén los protegen: hay que gobernar el RG de snapshots con RBAC y locks propios.
- **Cada origen necesita roles para la identidad del almacén.** Es trabajo de IaC por carga y hay que coordinarlo con quien administra cada recurso.
- **No hay Private Endpoint**, a diferencia del Recovery Services vault.
- **PostgreSQL v1 es semanal y hasta 1 TB.** El v2, diario y hasta 64 TB, sigue en preview.
- **Soft delete `AlwaysOn` e inmutabilidad `Locked` son irreversibles.** Se activan en producción con las retenciones ya validadas.
- **Las alertas de fallo de trabajos están activas por defecto.** Lo que hay que diseñar es a quién se notifican.

## Decisiones de diseño

| Decisión | Lo que aplico | Por qué |
|---|---|---|
| Redundancia | `GeoRedundant` en producción; LRS en dev/test | Copia fuera de la región |
| Cross Region Restore | Desactivado por defecto | Irreversible y con recargo |
| Soft delete | `On` por defecto, `AlwaysOn` en producción; `Off` bloqueado por validación | En la mayoría de regiones aún se puede desactivar |
| Inmutabilidad | `Unlocked` por defecto; `Locked` como decisión explícita | Primero lo reversible |
| MUA | `backupResourceGuardProxies` con **azapi** | azurerm no tiene recurso para Backup vaults |
| Identidad | Identidad del sistema; CMK opcional con ella y rol *Key Vault Crypto Service Encryption User* | El recurso CMK de azurerm no permite elegir identidad |
| Snapshots de discos | RG dedicado con *Disk Snapshot Contributor* para el almacén, desde esta ficha | Es infraestructura de la plataforma de backup |
| Permisos sobre orígenes | En el proyecto de cada carga | El dueño del recurso decide |
| Alertas | Las integradas (activas por defecto) y regla de procesamiento hacia un action group | Destinatarios explícitos |
| Diagnósticos | `CoreAzureBackup`, `AddonAzureBackupJobs`, `AddonAzureBackupPolicy`, `AddonAzureBackupProtectedInstance` | Backup vault envía siempre a tablas dedicadas |
| Políticas | Discos cada 4 h con 7 días (+30 días del primero del día), blobs 30+30 días, PostgreSQL semanal 3 meses | Puntos de partida para ajustar por carga |

Alineación con el Well-Architected Framework:

- **Seguridad**: identidad gestionada con roles mínimos por origen, soft delete, inmutabilidad, MUA y CMK opcional.
- **Fiabilidad**: GRS, Cross Region Restore cuando se pida y copia al almacén para blobs y bases de datos.
- **Coste**: discos y blobs operacionales sin tarifa de instancia; retenciones ajustadas al límite de snapshots.
- **Excelencia operativa**: almacén, permisos de plataforma, políticas, alertas y diagnósticos en IaC.
- **Rendimiento**: snapshots incrementales y restauración desde el nivel operacional.

## Módulo de Terraform

### Los módulos del repositorio

**[`AzureTerraformModules`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/BackupAndUpdate) no tiene módulo de Backup vault**: `BackupAndUpdate` solo cubre el Recovery Services vault, sus políticas, la protección de VMs y shares, y Update Manager. En la ficha va con recursos nativos.

Si se quiere un módulo ya hecho, Microsoft publica el Azure Verified Module [`avm-res-dataprotection-backupvault`](https://github.com/Azure/terraform-azurerm-avm-res-dataprotection-backupvault). Cubre también las instancias de backup (discos, blobs, Data Lake, AKS y PostgreSQL).

Lo que azurerm no cubre del Backup vault:

- No hay recurso para la asociación con el Resource Guard (MUA): se usa `azapi`.
- No expone `monitoringSettings` ni *Cross Subscription Restore*.
- `azurerm_data_protection_backup_vault_customer_managed_key` solo recibe la clave: usa la identidad del sistema.
- **Todos los argumentos de las políticas fuerzan recrearlas.**
- `redundancy` también fuerza recrear el almacén.

### Estructura en el proyecto

```txt
/
├── providers.tf
├── backup_vaults.tf     # almacén, CMK, MUA, RG de snapshots, alertas y diagnósticos
├── backup_policies.tf   # discos, blobs y PostgreSQL flexible
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
      # 4.49.0: identidades de usuario en azurerm_data_protection_backup_vault.
      # < 5.0.0: misma restricción que los módulos de AzureTerraformModules.
      version = ">= 4.49.0, < 5.0.0"
    }
    azapi = {
      source  = "Azure/azapi"
      version = ">= 2.0.0, < 3.0.0" # MUA: azurerm no tiene asociación con Resource Guard para Backup vaults
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

### Almacén · `backup_vaults.tf`

```hcl
# =============================================================================
# Backup vault: redundancia, soft delete, inmutabilidad, identidad, CMK opcional,
# MUA con Resource Guard, diagnósticos, enrutado de alertas y permisos sobre el
# grupo de recursos de snapshots
# DEPENDENCY: Resource Group existente
# DEPENDENCY: Proveedor Microsoft.DataProtection registrado en la suscripción
# DEPENDENCY: Resource Guard del equipo de seguridad (misma región, otra suscripción
#             o tenant) y rol Reader sobre él para la identidad de Terraform
# DEPENDENCY: CMK opcional: Key Vault con soft delete y purge protection (RBAC)
# DEPENDENCY: Grupos de recursos de snapshots de discos, en la suscripción de los discos
# DEPENDENCY: Los permisos sobre cada origen (disco, cuenta, servidor) van con la carga
# =============================================================================

variable "backup_vaults" {
  description = "Backup vaults (clave = nombre del almacén)."
  type = map(object({
    resource_group_name = string
    location            = string # la misma región que los orígenes que protege

    datastore_type               = optional(string, "VaultStore")
    redundancy                   = optional(string, "GeoRedundant") # GeoRedundant | ZoneRedundant | LocallyRedundant
    cross_region_restore_enabled = optional(bool, false)            # solo GRS; irreversible

    # Soft delete: AlwaysOn es irreversible; Off no se admite aquí
    soft_delete                = optional(string, "On") # On | AlwaysOn
    retention_duration_in_days = optional(number, 14)   # 14-180; más de 14 se factura

    # Inmutabilidad: Unlocked es reversible; Locked es irreversible (decisión explícita)
    immutability = optional(string, "Unlocked") # Disabled | Unlocked | Locked

    identity = optional(object({
      type         = optional(string, "SystemAssigned")
      identity_ids = optional(list(string), [])
    }), {})

    # CMK con la identidad del sistema; no se puede volver a claves de plataforma
    cmk = optional(object({
      key_vault_id     = string # para el rol Key Vault Crypto Service Encryption User
      key_vault_key_id = string # sin versión para rotación automática
    }))

    resource_guard_id = optional(string)
    action_group_ids  = optional(list(string), [])

    # Grupos de recursos donde Azure Backup guarda los snapshots de discos
    snapshot_resource_group_ids = optional(map(string), {})

    log_analytics_workspace_id = string
    tags                       = optional(map(string), {})
  }))
  default = {}

  validation {
    condition = alltrue([
      for k, v in var.backup_vaults :
      contains(["GeoRedundant", "ZoneRedundant", "LocallyRedundant"], v.redundancy)
    ])
    error_message = "redundancy debe ser GeoRedundant, ZoneRedundant o LocallyRedundant."
  }

  validation {
    condition     = alltrue([for k, v in var.backup_vaults : !v.cross_region_restore_enabled || v.redundancy == "GeoRedundant"])
    error_message = "Cross Region Restore solo está disponible con redundancy = GeoRedundant."
  }

  validation {
    condition     = alltrue([for k, v in var.backup_vaults : contains(["On", "AlwaysOn"], v.soft_delete)])
    error_message = "soft_delete debe ser On o AlwaysOn: no se despliegan almacenes sin soft delete."
  }

  validation {
    condition     = alltrue([for k, v in var.backup_vaults : v.retention_duration_in_days >= 14 && v.retention_duration_in_days <= 180])
    error_message = "retention_duration_in_days debe estar entre 14 y 180."
  }

  validation {
    condition     = alltrue([for k, v in var.backup_vaults : contains(["Disabled", "Unlocked", "Locked"], v.immutability)])
    error_message = "immutability debe ser Disabled, Unlocked o Locked."
  }

  validation {
    condition     = alltrue([for k, v in var.backup_vaults : v.cmk == null || strcontains(v.identity.type, "SystemAssigned")])
    error_message = "CMK en esta ficha usa la identidad del sistema: identity.type debe incluir SystemAssigned."
  }
}

resource "azurerm_data_protection_backup_vault" "this" {
  for_each            = var.backup_vaults
  name                = each.key
  resource_group_name = each.value.resource_group_name
  location            = each.value.location

  datastore_type               = each.value.datastore_type
  redundancy                   = each.value.redundancy
  cross_region_restore_enabled = each.value.cross_region_restore_enabled

  soft_delete                = each.value.soft_delete
  retention_duration_in_days = each.value.retention_duration_in_days
  immutability               = each.value.immutability

  identity {
    type         = each.value.identity.type
    identity_ids = each.value.identity.type == "SystemAssigned" ? null : each.value.identity.identity_ids
  }

  tags = merge(var.tags, each.value.tags)
}

# CMK: permiso de la identidad sobre el Key Vault y después la clave
resource "azurerm_role_assignment" "bv_cmk" {
  for_each             = { for k, v in var.backup_vaults : k => v if v.cmk != null }
  scope                = each.value.cmk.key_vault_id
  role_definition_name = "Key Vault Crypto Service Encryption User"
  principal_id         = azurerm_data_protection_backup_vault.this[each.key].identity[0].principal_id
  principal_type       = "ServicePrincipal"
}

resource "azurerm_data_protection_backup_vault_customer_managed_key" "this" {
  for_each                        = { for k, v in var.backup_vaults : k => v if v.cmk != null }
  data_protection_backup_vault_id = azurerm_data_protection_backup_vault.this[each.key].id
  key_vault_key_id                = each.value.cmk.key_vault_key_id

  depends_on = [azurerm_role_assignment.bv_cmk]
}

# Snapshots de discos: Disk Snapshot Contributor en el RG dedicado
resource "azurerm_role_assignment" "bv_snapshot_rg" {
  for_each = {
    for item in flatten([
      for vk, v in var.backup_vaults : [
        for rk, rg_id in v.snapshot_resource_group_ids : { key = "${vk}/${rk}", vault = vk, scope = rg_id }
      ]
    ]) : item.key => item
  }

  scope                = each.value.scope
  role_definition_name = "Disk Snapshot Contributor"
  principal_id         = azurerm_data_protection_backup_vault.this[each.value.vault].identity[0].principal_id
  principal_type       = "ServicePrincipal"
}

# Multi-user authorization (azurerm no tiene recurso para Backup vaults)
resource "azapi_resource" "bv_resource_guard_proxy" {
  for_each  = { for k, v in var.backup_vaults : k => v if v.resource_guard_id != null }
  type      = "Microsoft.DataProtection/backupVaults/backupResourceGuardProxies@2025-07-01"
  name      = "DppResourceGuardProxy"
  parent_id = azurerm_data_protection_backup_vault.this[each.key].id

  body = {
    properties = {
      resourceGuardResourceId = each.value.resource_guard_id
    }
  }
}

# Backup vault envía siempre a tablas dedicadas (resource-specific)
resource "azurerm_monitor_diagnostic_setting" "bv" {
  for_each                   = var.backup_vaults
  name                       = "diag-${each.key}"
  target_resource_id         = azurerm_data_protection_backup_vault.this[each.key].id
  log_analytics_workspace_id = each.value.log_analytics_workspace_id

  dynamic "enabled_log" {
    for_each = toset([
      "CoreAzureBackup",
      "AddonAzureBackupJobs",
      "AddonAzureBackupPolicy",
      "AddonAzureBackupProtectedInstance",
    ])
    content {
      category = enabled_log.value
    }
  }
}

# Notificaciones de las alertas integradas (se generan por defecto)
resource "azurerm_monitor_alert_processing_rule_action_group" "bv" {
  for_each             = { for k, v in var.backup_vaults : k => v if length(v.action_group_ids) > 0 }
  name                 = "apr-${each.key}"
  resource_group_name  = each.value.resource_group_name
  scopes               = [azurerm_data_protection_backup_vault.this[each.key].id]
  add_action_group_ids = each.value.action_group_ids
  description          = "Envía las alertas integradas de Azure Backup del almacén ${each.key}."
  tags                 = merge(var.tags, each.value.tags)
}

output "backup_vault_ids" {
  description = "IDs de los Backup vaults."
  value       = { for k, v in azurerm_data_protection_backup_vault.this : k => v.id }
}

output "backup_vault_principal_ids" {
  description = "Object ID de la identidad del sistema: permisos sobre cada origen."
  value       = { for k, v in azurerm_data_protection_backup_vault.this : k => try(v.identity[0].principal_id, null) }
}
```

### Políticas · `backup_policies.tf`

```hcl
# =============================================================================
# Políticas de partida: discos (operacional), blobs (operacional + vault) y
# PostgreSQL flexible server (vault)
# DEPENDENCY: azurerm_data_protection_backup_vault.this (backup_vaults.tf)
# Todas las políticas de Backup vault se recrean al cambiar cualquier argumento
# =============================================================================

variable "backup_policies_disk" {
  description = "Políticas de discos administrados (clave = nombre de la política)."
  type = map(object({
    vault                      = string       # clave de var.backup_vaults
    repeating_time_intervals   = list(string) # ISO 8601, p. ej. R/2026-01-01T02:00:00+00:00/PT4H
    default_retention_duration = string       # ISO 8601, p. ej. P7D (máximo 1 año o 450 snapshots)
    time_zone                  = optional(string, "UTC")
    retention_rules = optional(map(object({
      duration          = string
      priority          = number
      absolute_criteria = string # FirstOfDay | FirstOfWeek | ...
    })), {})
  }))
  default = {}
}

variable "backup_policies_blob" {
  description = "Políticas de blobs (clave = nombre de la política)."
  type = map(object({
    vault                                  = string
    operational_default_retention_duration = optional(string)       # p. ej. P30D
    vault_default_retention_duration       = optional(string)       # p. ej. P30D
    repeating_time_intervals               = optional(list(string)) # obligatorio con vault_default_retention_duration
    time_zone                              = optional(string, "UTC")
  }))
  default = {}

  validation {
    condition = alltrue([
      for k, v in var.backup_policies_blob :
      v.operational_default_retention_duration != null || v.vault_default_retention_duration != null
    ])
    error_message = "Hace falta retención operacional, de almacén o ambas."
  }

  validation {
    condition = alltrue([
      for k, v in var.backup_policies_blob :
      v.vault_default_retention_duration == null || v.repeating_time_intervals != null
    ])
    error_message = "La copia al almacén (vault_default_retention_duration) necesita repeating_time_intervals."
  }
}

variable "backup_policies_postgresql_flexible" {
  description = "Políticas de Azure Database for PostgreSQL flexible server (clave = nombre)."
  type = map(object({
    vault                      = string
    repeating_time_intervals   = list(string) # semanal, p. ej. R/2026-01-04T02:00:00+00:00/P1W
    default_retention_duration = string       # p. ej. P3M (hasta 10 años)
    time_zone                  = optional(string, "UTC")
  }))
  default = {}
}

resource "azurerm_data_protection_backup_policy_disk" "this" {
  for_each = var.backup_policies_disk
  name     = each.key
  vault_id = azurerm_data_protection_backup_vault.this[each.value.vault].id

  backup_repeating_time_intervals = each.value.repeating_time_intervals
  default_retention_duration      = each.value.default_retention_duration
  time_zone                       = each.value.time_zone

  dynamic "retention_rule" {
    for_each = each.value.retention_rules
    content {
      name     = retention_rule.key
      duration = retention_rule.value.duration
      priority = retention_rule.value.priority
      criteria {
        absolute_criteria = retention_rule.value.absolute_criteria
      }
    }
  }
}

resource "azurerm_data_protection_backup_policy_blob_storage" "this" {
  for_each = var.backup_policies_blob
  name     = each.key
  vault_id = azurerm_data_protection_backup_vault.this[each.value.vault].id

  operational_default_retention_duration = each.value.operational_default_retention_duration
  vault_default_retention_duration       = each.value.vault_default_retention_duration
  backup_repeating_time_intervals        = each.value.repeating_time_intervals
  time_zone                              = each.value.time_zone
}

resource "azurerm_data_protection_backup_policy_postgresql_flexible_server" "this" {
  for_each = var.backup_policies_postgresql_flexible
  name     = each.key
  vault_id = azurerm_data_protection_backup_vault.this[each.value.vault].id

  backup_repeating_time_intervals = each.value.repeating_time_intervals
  time_zone                       = each.value.time_zone

  default_retention_rule {
    life_cycle {
      data_store_type = "VaultStore"
      duration        = each.value.default_retention_duration
    }
  }
}

output "backup_vault_policy_ids" {
  description = "IDs de las políticas (para los azurerm_data_protection_backup_instance_* de cada carga)."
  value = merge(
    { for k, p in azurerm_data_protection_backup_policy_disk.this : k => p.id },
    { for k, p in azurerm_data_protection_backup_policy_blob_storage.this : k => p.id },
    { for k, p in azurerm_data_protection_backup_policy_postgresql_flexible_server.this : k => p.id },
  )
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

backup_vaults = {
  "bvault-<workload>-pro-<region>-01" = {
    resource_group_name = "<rg-backup-pro>"
    location            = "<region>"

    redundancy                   = "GeoRedundant"
    cross_region_restore_enabled = false

    soft_delete                = "AlwaysOn" # irreversible
    retention_duration_in_days = 14
    immutability               = "Unlocked" # pasar a "Locked" tras validar retenciones

    resource_guard_id = "<resourceId Resource Guard en la suscripción de seguridad>"
    action_group_ids  = ["<resourceId action group de operaciones>"]

    snapshot_resource_group_ids = {
      discos-pro = "<resourceId rg-<workload>-pro-bkp-disk-snapshots>"
    }

    log_analytics_workspace_id = "<resourceId log-analytics-workspace>"
  }
}

backup_policies_disk = {
  "bkpol-disk-4h-7d" = {
    vault                      = "bvault-<workload>-pro-<region>-01"
    repeating_time_intervals   = ["R/2026-01-01T02:00:00+00:00/PT4H"]
    default_retention_duration = "P7D"
    retention_rules = {
      Daily = {
        duration          = "P30D"
        priority          = 25
        absolute_criteria = "FirstOfDay"
      }
    }
  }
}

backup_policies_blob = {
  "bkpol-blob-op30d-vault30d" = {
    vault                                  = "bvault-<workload>-pro-<region>-01"
    operational_default_retention_duration = "P30D"
    vault_default_retention_duration       = "P30D"
    repeating_time_intervals               = ["R/2026-01-01T03:00:00+00:00/P1D"]
  }
}

backup_policies_postgresql_flexible = {
  "bkpol-pgflex-weekly-3m" = {
    vault                      = "bvault-<workload>-pro-<region>-01"
    repeating_time_intervals   = ["R/2026-01-04T02:00:00+00:00/P1W"]
    default_retention_duration = "P3M"
  }
}
```

En `dev.tfvars`: `redundancy = "LocallyRedundant"`, `soft_delete = "On"`, `immutability = "Unlocked"` y sin `resource_guard_id`.

### Proteger un disco desde el proyecto de la carga

Las instancias de backup van con cada carga. Para un disco, el patrón es este:

```hcl
# DEPENDENCY: backup_vault_principal_ids y backup_vault_policy_ids de la plataforma de backup
resource "azurerm_role_assignment" "disk_backup_reader" {
  scope                = azurerm_managed_disk.data.id
  role_definition_name = "Disk Backup Reader"
  principal_id         = var.backup_vault_principal_id
  principal_type       = "ServicePrincipal"
}

resource "azurerm_data_protection_backup_instance_disk" "data" {
  name                         = "bi-${azurerm_managed_disk.data.name}"
  location                     = azurerm_managed_disk.data.location # misma región que el almacén
  vault_id                     = var.backup_vault_id
  disk_id                      = azurerm_managed_disk.data.id
  snapshot_resource_group_name = var.snapshot_resource_group_name
  backup_policy_id             = var.backup_policy_disk_id

  depends_on = [azurerm_role_assignment.disk_backup_reader]
}
```

Despliegue y comprobación:

```powershell
terraform init
terraform plan -var-file="env/pro.tfvars" -out="pro.tfplan"
terraform apply "pro.tfplan"

# Comprobaciones
Get-AzDataProtectionBackupVault -ResourceGroupName "<rg-backup-pro>" -VaultName "bvault-<workload>-pro-<region>-01" | Format-List
Get-AzDataProtectionResourceGuardMapping -ResourceGroupName "<rg-backup-pro>" -VaultName "bvault-<workload>-pro-<region>-01"
Get-AzDataProtectionBackupPolicy -ResourceGroupName "<rg-backup-pro>" -VaultName "bvault-<workload>-pro-<region>-01" | Select-Object Name
```

### Equivalente en Bicep

`main.bicep`:

```bicep
// =============================================================================
// Backup vault: redundancia, soft delete, inmutabilidad, alertas, MUA con Resource Guard,
// diagnósticos, permisos sobre el RG de snapshots y políticas de partida
// DEPENDENCY: Resource Group existente (targetScope = resourceGroup)
// DEPENDENCY: Resource Guard del equipo de seguridad (misma región) y Reader sobre él
// DEPENDENCY: RG de snapshots de discos existente
// =============================================================================
targetScope = 'resourceGroup'

param location string = resourceGroup().location

param vaultName string

@allowed(['GeoRedundant', 'ZoneRedundant', 'LocallyRedundant'])
param redundancy string = 'GeoRedundant'

@description('Solo con GeoRedundant. Irreversible.')
param crossRegionRestore bool = false

@description('AlwaysOn es irreversible.')
@allowed(['On', 'AlwaysOn'])
param softDeleteState string = 'On'

@minValue(14)
@maxValue(180)
param softDeleteRetentionDays int = 14

@allowed(['Disabled', 'Unlocked', 'Locked'])
param immutabilityState string = 'Unlocked'

param resourceGuardId string = ''
param actionGroupIds array = []
param logAnalyticsWorkspaceId string

@description('Nombre del RG de snapshots de discos (misma suscripción).')
param snapshotResourceGroupName string

param tags object = {}

var backupLogCategories = [
  'CoreAzureBackup'
  'AddonAzureBackupJobs'
  'AddonAzureBackupPolicy'
  'AddonAzureBackupProtectedInstance'
]

resource vault 'Microsoft.DataProtection/backupVaults@2025-07-01' = {
  name: vaultName
  location: location
  tags: tags
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    storageSettings: [
      {
        datastoreType: 'VaultStore'
        type: redundancy
      }
    ]
    featureSettings: {
      crossRegionRestoreSettings: {
        state: crossRegionRestore ? 'Enabled' : 'Disabled'
      }
    }
    securitySettings: {
      softDeleteSettings: {
        state: softDeleteState
        retentionDurationInDays: softDeleteRetentionDays
      }
      immutabilitySettings: {
        state: immutabilityState
      }
    }
    monitoringSettings: {
      azureMonitorAlertSettings: {
        alertsForAllJobFailures: 'Enabled'
      }
    }
  }
}

resource resourceGuardProxy 'Microsoft.DataProtection/backupVaults/backupResourceGuardProxies@2025-07-01' = if (!empty(resourceGuardId)) {
  parent: vault
  name: 'DppResourceGuardProxy'
  properties: {
    resourceGuardResourceId: resourceGuardId
  }
}

resource diagnostics 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = {
  name: 'diag-${vaultName}'
  scope: vault
  properties: {
    workspaceId: logAnalyticsWorkspaceId
    logs: [
      for category in backupLogCategories: {
        category: category
        enabled: true
      }
    ]
  }
}

resource alertRouting 'Microsoft.AlertsManagement/actionRules@2021-08-08' = if (!empty(actionGroupIds)) {
  name: 'apr-${vaultName}'
  location: 'global'
  tags: tags
  properties: {
    scopes: [
      vault.id
    ]
    actions: [
      {
        actionType: 'AddActionGroups'
        actionGroupIds: actionGroupIds
      }
    ]
    description: 'Envía las alertas integradas de Azure Backup del almacén.'
    enabled: true
  }
}

module snapshotRole 'snapshot-rg-role.bicep' = {
  name: 'snapshot-role-${vaultName}'
  scope: resourceGroup(snapshotResourceGroupName)
  params: {
    vaultPrincipalId: vault.identity.principalId
    vaultId: vault.id
  }
}

// Discos: snapshot cada 4 horas en el almacén operacional, 7 días
resource policyDisk 'Microsoft.DataProtection/backupVaults/backupPolicies@2025-07-01' = {
  parent: vault
  name: 'bkpol-disk-4h-7d'
  properties: {
    objectType: 'BackupPolicy'
    datasourceTypes: [
      'Microsoft.Compute/disks'
    ]
    policyRules: [
      {
        name: 'BackupHourly'
        objectType: 'AzureBackupRule'
        backupParameters: {
          objectType: 'AzureBackupParams'
          backupType: 'Incremental'
        }
        dataStore: {
          objectType: 'DataStoreInfoBase'
          dataStoreType: 'OperationalStore'
        }
        trigger: {
          objectType: 'ScheduleBasedTriggerContext'
          schedule: {
            repeatingTimeIntervals: [
              'R/2026-01-01T02:00:00+00:00/PT4H'
            ]
          }
          taggingCriteria: [
            {
              isDefault: true
              taggingPriority: 99
              tagInfo: {
                tagName: 'Default'
              }
            }
          ]
        }
      }
      {
        name: 'Default'
        objectType: 'AzureRetentionRule'
        isDefault: true
        lifecycles: [
          {
            deleteAfter: {
              objectType: 'AbsoluteDeleteOption'
              duration: 'P7D'
            }
            sourceDataStore: {
              objectType: 'DataStoreInfoBase'
              dataStoreType: 'OperationalStore'
            }
          }
        ]
      }
    ]
  }
}

// Blobs: operacional 30 días + copia diaria al almacén con 30 días
resource policyBlob 'Microsoft.DataProtection/backupVaults/backupPolicies@2025-07-01' = {
  parent: vault
  name: 'bkpol-blob-op30d-vault30d'
  properties: {
    objectType: 'BackupPolicy'
    datasourceTypes: [
      'Microsoft.Storage/storageAccounts/blobServices'
    ]
    policyRules: [
      {
        name: 'Default'
        objectType: 'AzureRetentionRule'
        isDefault: true
        lifecycles: [
          {
            deleteAfter: {
              objectType: 'AbsoluteDeleteOption'
              duration: 'P30D'
            }
            sourceDataStore: {
              objectType: 'DataStoreInfoBase'
              dataStoreType: 'OperationalStore'
            }
          }
        ]
      }
      {
        name: 'Default'
        objectType: 'AzureRetentionRule'
        isDefault: true
        lifecycles: [
          {
            deleteAfter: {
              objectType: 'AbsoluteDeleteOption'
              duration: 'P30D'
            }
            sourceDataStore: {
              objectType: 'DataStoreInfoBase'
              dataStoreType: 'VaultStore'
            }
          }
        ]
      }
      {
        name: 'BackupDaily'
        objectType: 'AzureBackupRule'
        backupParameters: {
          objectType: 'AzureBackupParams'
          backupType: 'Discrete'
        }
        dataStore: {
          objectType: 'DataStoreInfoBase'
          dataStoreType: 'VaultStore'
        }
        trigger: {
          objectType: 'ScheduleBasedTriggerContext'
          schedule: {
            repeatingTimeIntervals: [
              'R/2026-01-01T03:00:00+00:00/P1D'
            ]
            timeZone: 'UTC'
          }
          taggingCriteria: [
            {
              isDefault: true
              taggingPriority: 99
              tagInfo: {
                tagName: 'Default'
              }
            }
          ]
        }
      }
    ]
  }
}

// PostgreSQL flexible server: completo semanal en el almacén, 3 meses
resource policyPgFlex 'Microsoft.DataProtection/backupVaults/backupPolicies@2025-07-01' = {
  parent: vault
  name: 'bkpol-pgflex-weekly-3m'
  properties: {
    objectType: 'BackupPolicy'
    datasourceTypes: [
      'Microsoft.DBforPostgreSQL/flexibleServers'
    ]
    policyRules: [
      {
        name: 'BackupWeekly'
        objectType: 'AzureBackupRule'
        backupParameters: {
          objectType: 'AzureBackupParams'
          backupType: 'Full'
        }
        dataStore: {
          objectType: 'DataStoreInfoBase'
          dataStoreType: 'VaultStore'
        }
        trigger: {
          objectType: 'ScheduleBasedTriggerContext'
          schedule: {
            repeatingTimeIntervals: [
              'R/2026-01-04T02:00:00+00:00/P1W'
            ]
            timeZone: 'UTC'
          }
          taggingCriteria: [
            {
              isDefault: true
              taggingPriority: 99
              tagInfo: {
                tagName: 'Default'
              }
            }
          ]
        }
      }
      {
        name: 'Default'
        objectType: 'AzureRetentionRule'
        isDefault: true
        lifecycles: [
          {
            deleteAfter: {
              objectType: 'AbsoluteDeleteOption'
              duration: 'P3M'
            }
            sourceDataStore: {
              objectType: 'DataStoreInfoBase'
              dataStoreType: 'VaultStore'
            }
          }
        ]
      }
    ]
  }
}

output vaultId string = vault.id
output vaultPrincipalId string = vault.identity.principalId
output diskPolicyId string = policyDisk.id
output blobPolicyId string = policyBlob.id
output pgFlexPolicyId string = policyPgFlex.id
```

`snapshot-rg-role.bicep` (el rol se asigna en otro grupo de recursos, por eso va como módulo):

```bicep
// Disk Snapshot Contributor del Backup vault en el grupo de recursos de snapshots
// DEPENDENCY: el grupo de recursos existe en la misma suscripción que los discos
targetScope = 'resourceGroup'

param vaultPrincipalId string
param vaultId string

// Disk Snapshot Contributor (rol integrado)
var diskSnapshotContributorRoleId = '7efff54f-a5b4-42b5-a1c5-5411624893ce'

resource snapshotRole 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(resourceGroup().id, vaultId, diskSnapshotContributorRoleId)
  properties: {
    principalId: vaultPrincipalId
    principalType: 'ServicePrincipal'
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', diskSnapshotContributorRoleId)
  }
}
```

`main.pro.bicepparam`:

```bicep
using 'main.bicep'

param vaultName = 'bvault-<workload>-pro-<region>-01'
param redundancy = 'GeoRedundant'
param crossRegionRestore = false
param softDeleteState = 'AlwaysOn' // irreversible
param softDeleteRetentionDays = 14
param immutabilityState = 'Unlocked'

param resourceGuardId = '<resourceId Resource Guard en la suscripción de seguridad>'
param actionGroupIds = [
  '<resourceId action group de operaciones>'
]
param logAnalyticsWorkspaceId = '<resourceId log-analytics-workspace>'
param snapshotResourceGroupName = 'rg-<workload>-pro-bkp-disk-snapshots'

param tags = {
  environment: 'pro'
  workload: '<workload>'
  owner: '<owner>'
  costcenter: '<costcenter>'
}
```

Despliegue:

```powershell
az deployment group what-if --resource-group <rg-backup-pro> --parameters main.pro.bicepparam
az deployment group create  --resource-group <rg-backup-pro> --parameters main.pro.bicepparam
```

## Errores típicos

| Síntoma | Causa | Solución |
|---|---|---|
| *Role assignment not done* o validación fallida justo después de asignar roles | Los roles tardan hasta 30 minutos en aplicarse | Esperar y revalidar |
| `UserErrorSnapshotRGOrMSIPermissionsNotPresent` | El RG de snapshots no existe o falta *Disk Snapshot Contributor* | Crear el RG y asignar el rol |
| `UserErrorMSIPermissionsNotPresentOnDES` | El disco usa un Disk Encryption Set | *Reader* sobre el DES para el almacén |
| `UserErrorDiskBackupRestoreRGOrMSIPermissionsNotPresent` | Falta el RG de destino o permisos sobre él | Crear el RG y dar *Disk Restore Operator* |
| `LinkedAuthorizationFailed` al restaurar | El usuario no tiene lectura sobre el disco de origen | *Reader* sobre el disco |
| *"Cannot delete the Backup vault as there are existing backup instances or backup policies"* | Quedan instancias o políticas | Borrarlas antes (revisar todos los tipos de origen) |
| `UserErrorCMKMissingMangedIdentityPermissionOnKeyVault` o `UserErrorCMKKeyVaultAuthFailure` | La identidad no tiene permisos sobre la clave, o la clave no es RSA | *Key Vault Crypto Service Encryption User* y clave RSA |
| Errores de purge protection o soft delete al activar CMK | El Key Vault no tiene ambos activados | Activarlos en el Key Vault |
| El `plan` propone recrear la política al cambiar la retención | Los argumentos de las políticas fuerzan recrearlas | Política nueva y reasignar las instancias |
| El `plan` propone recrear el almacén | Cambio de `redundancy` | Decidirla al crear; con elementos protegidos, almacén nuevo |
| Copias de PostgreSQL que fallan entre semana | La v1 solo admite una copia semanal | Frecuencia semanal o v2 (preview) |
| La copia de PostgreSQL falla en servidores grandes | La v1 admite hasta 1 TB | v2 (preview) |
| Error al configurar la copia de blobs al almacén | Cuenta sin contenedores o con más de 1.000 | Crear o excluir contenedores |
| Quitar `resource_guard_id` o hacer `destroy` falla con MUA activo | Desactivar MUA es una operación crítica | Desbloquearla antes con `Unlock-AzDataProtectionResourceGuardOperation -ResourceGuardOperationRequest DisableMUA` (permiso sobre el Resource Guard) |
| Backup de AKS que falla con Azure Policy en el clúster | Las directivas afectan al namespace de la extensión | Excluir `dataprotection-microsoft` |
| El ejemplo oficial de Terraform para PostgreSQL no hace `plan` | Usa `azurerm_data_protection_backup_policy` y `storage_settings`, que no existen en azurerm | Usar `azurerm_data_protection_backup_policy_postgresql_flexible_server`, `datastore_type` y `redundancy` |
