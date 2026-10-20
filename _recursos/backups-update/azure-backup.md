---
title: "Azure Backup"
indice: backups-update
resumen: "Políticas de copia y retención para tus cargas."
estado: documentado   # proximamente | en-curso | documentado
orden: 3
last_review: 2026-10-20
fuentes:
  - titulo: "What is the Azure Backup service?"
    url: https://learn.microsoft.com/azure/backup/backup-overview
  - titulo: "Backup cloud and on-premises workloads to cloud (guía y buenas prácticas)"
    url: https://learn.microsoft.com/azure/backup/guidance-best-practices
  - titulo: "Support matrix for Azure VM backups"
    url: https://learn.microsoft.com/azure/backup/backup-support-matrix-iaas
  - titulo: "An overview of Azure VM backup (consistencia y costes)"
    url: https://learn.microsoft.com/azure/backup/backup-azure-vms-introduction
  - titulo: "Back up an Azure VM by using the Enhanced policy"
    url: https://learn.microsoft.com/azure/backup/backup-azure-vms-enhanced-policy
  - titulo: "Migrate Azure VM backups from standard to enhanced policy"
    url: https://learn.microsoft.com/azure/backup/backup-azure-vm-migrate-enhanced-policy
  - titulo: "Instant Restore capability (coste de snapshots)"
    url: https://learn.microsoft.com/azure/backup/backup-instant-restore-capability
  - titulo: "Agentless multidisk crash-consistent backup for Azure VMs"
    url: https://learn.microsoft.com/azure/backup/backup-azure-vms-agentless-multi-disk-crash-consistent-overview
  - titulo: "Configure application-consistent backup for Azure Linux VMs"
    url: https://learn.microsoft.com/azure/backup/backup-azure-linux-app-consistent
  - titulo: "How to restore Azure VM data in Azure portal"
    url: https://learn.microsoft.com/azure/backup/backup-azure-arm-restore-vms
  - titulo: "About SQL Server Backup in Azure VMs"
    url: https://learn.microsoft.com/azure/backup/backup-azure-sql-database
  - titulo: "Support matrix for SQL Server backups in Azure VMs"
    url: https://learn.microsoft.com/azure/backup/sql-support-matrix
  - titulo: "Back up and restore SQL databases in Azure VMs with PowerShell"
    url: https://learn.microsoft.com/azure/backup/backup-azure-sql-automation
  - titulo: "About Azure Files backup"
    url: https://learn.microsoft.com/azure/backup/azure-file-share-backup-overview
  - titulo: "Support matrix for Azure Files backup"
    url: https://learn.microsoft.com/azure/backup/azure-file-share-support-matrix
  - titulo: "Overview of Archive tier in Azure Backup"
    url: https://learn.microsoft.com/azure/backup/archive-tier-support
  - titulo: "Use Archive tier support"
    url: https://learn.microsoft.com/azure/backup/use-archive-tier-support
  - titulo: "Audit and enforce backup during VM creation using Azure Policy"
    url: https://learn.microsoft.com/azure/backup/backup-azure-auto-enable-backup
  - titulo: "Supported VM SKUs for Azure Policy"
    url: https://learn.microsoft.com/azure/backup/backup-azure-policy-supported-skus
  - titulo: "Azure Policy built-in definitions for Azure Backup"
    url: https://learn.microsoft.com/azure/backup/policy-reference
  - titulo: "Definición VirtualMachineWithTag_DINE.json (azure-policy)"
    url: https://github.com/Azure/azure-policy/blob/master/built-in-policies/policyDefinitions/Backup/VirtualMachineWithTag_DINE.json
  - titulo: "Query your backups using Azure Resource Graph"
    url: https://learn.microsoft.com/azure/backup/query-backups-using-azure-resource-graph
  - titulo: "Estimate Azure Backup costs and understand pricing"
    url: https://learn.microsoft.com/azure/backup/azure-backup-pricing
  - titulo: "Enable-AzRecoveryServicesBackupProtection (acceso IdentityBased para Azure Files)"
    url: https://learn.microsoft.com/powershell/module/az.recoveryservices/enable-azrecoveryservicesbackupprotection
  - titulo: "azurerm_backup_policy_vm"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/backup_policy_vm
  - titulo: "azurerm_backup_policy_file_share"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/backup_policy_file_share
  - titulo: "azurerm_backup_policy_vm_workload"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/backup_policy_vm_workload
  - titulo: "azurerm_backup_protected_vm"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/backup_protected_vm
  - titulo: "Microsoft.RecoveryServices vaults/backupPolicies (plantillas ARM/Bicep)"
    url: https://learn.microsoft.com/azure/templates/microsoft.recoveryservices/vaults/backuppolicies
  - titulo: "Módulo Terraform BackupAndUpdate/BackupPolicyVM"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/BackupAndUpdate/BackupPolicyVM
  - titulo: "Módulo Terraform BackupAndUpdate/BackupPolicyFileShare"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/BackupAndUpdate/BackupPolicyFileShare
  - titulo: "Módulo Terraform BackupAndUpdate/BackupProtectedVM"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/BackupAndUpdate/BackupProtectedVM
  - titulo: "Módulo Terraform BackupAndUpdate/BackupProtectedFileShare"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/BackupAndUpdate/BackupProtectedFileShare
---

**Azure Backup** es el servicio. Los almacenes son donde vive: el [Recovery Services vault](/recursos/backups-update/recovery-services-vault/) para VMs, SQL Server en VMs y Azure Files, y el [Backup vault](/recursos/backups-update/backup-vault/) para discos, blobs y PostgreSQL. Esta ficha trata lo que hay encima del almacén:

- **Las políticas**: cuándo se copia, cuánto se guarda y en qué nivel.
- **La protección** de cada carga.
- **El gobierno**: que ninguna VM se quede sin copia.

Aquí se decide el RPO, el RTO y buena parte del coste.

## Qué es y cuándo usarlo

### Qué protege cada política

| Carga | Almacén | Política | RPO mínimo |
|---|---|---|---|
| VM (Standard) | Recovery Services | Una copia diaria o semanal | 24 horas |
| **VM (Enhanced)** | Recovery Services | Cada 4, 6, 8, 12 o 24 horas | **4 horas** |
| **SQL Server en VM** | Recovery Services | Completa, diferencial y **log cada 15 minutos** | 15 minutos, restauración a un punto en el tiempo |
| Azure Files (snapshot) | Recovery Services | Snapshots en la propia cuenta | Varias al día |
| **Azure Files (vaulted)** | Recovery Services | Snapshot + copia diaria al almacén | 24 horas (copia fuera de la cuenta) |
| Discos, blobs, PostgreSQL, AKS | Backup vault | Ver la [ficha del Backup vault](/recursos/backups-update/backup-vault/) | Según carga |

### VM: Standard o Enhanced

| | Standard | **Enhanced** (recomendada) |
|---|---|---|
| Frecuencia | 1 al día | Cada 4 horas |
| Instant Restore (snapshots) | 1-5 días (5 con frecuencia semanal) | 1-30 días |
| Snapshots | Snapshot de blob en la cuenta de la VM | Snapshot de disco administrado, **resistente a zona** |
| Trusted Launch, Premium SSD v2, Ultra | Trusted Launch solo por CLI, PowerShell o REST recientes; el resto no | **Sí** |
| Copias sin agente (crash-consistent multidisco) | No | Sí |
| Volver atrás | — | **No** se puede pasar de Enhanced a Standard |

Coste de los snapshots, con el ejemplo de Microsoft (VM de 100 GB, 2 % de cambio diario y 5 días de Instant Restore): **10 GB facturables con Standard y 108 GB con Enhanced**, porque el primer snapshot de disco administrado es completo.

### Niveles de almacenamiento

| Nivel | Qué es | Para qué |
|---|---|---|
| **Snapshot** (Instant Restore) | Snapshots en tu suscripción | Restauraciones rápidas de días recientes |
| **Vault-Standard** | Copia en el almacén, aislada de tu suscripción | Retención normal |
| **Vault-Archive** | Archivo de bajo coste | Retención larga por cumplimiento |

Reglas del archivo:

- **VMs**: solo puntos **mensuales y anuales**, con 3 meses o más en Vault-Standard y 6 meses o más de retención pendiente.
- **SQL/SAP HANA**: solo copias completas, con 45 días o más en el almacén.
- **Borrado anticipado**: borrar un punto con menos de 180 días en archivo cobra el resto.
- **No funciona en almacenes ZRS.**
- **En VMs, archivar puede encarecer**: los puntos incrementales pasan a completos. Por eso existe el modo `TierRecommended`, que solo mueve los conjuntos que ahorran.

### Consistencia de las copias de VM

| Tipo | Cómo | Al restaurar |
|---|---|---|
| **Coherente con la aplicación** (por defecto) | VSS en Windows; pre/post scripts en Linux | Arranca sin pérdida y las aplicaciones en estado coherente |
| Coherente con el sistema de archivos | Si fallan writers VSS o no hay scripts en Linux | Arranca; la aplicación hace su propia recuperación |
| Crash-consistent | VM apagada, fallo de las anteriores u opción sin agente | Comprobación de disco; se pierde lo que estaba en memoria |

La copia de una VM con SQL Server hace un VSS *copy-only*: no trunca logs ni da restauración a un punto en el tiempo. **Para bases de datos, la copia de SQL Server en VM** (por base de datos, con logs).

### Formas de restaurar una VM

| Opción | Detalle |
|---|---|
| Crear VM | Rápido, configuración básica, misma región |
| Restaurar discos | Discos + plantilla para personalizar la VM |
| Reemplazar discos | Sobre la VM existente; guarda antes un snapshot de lo actual |
| Ficheros sueltos | Monta el punto de recuperación y copias lo necesario |
| Otra región / suscripción / zona | Cross Region Restore (GRS), Cross Subscription Restore y Cross Zonal Restore |

### Azure Files: snapshot o vaulted

| | Snapshot | **Vaulted** (`vault-standard`) |
|---|---|---|
| Dónde queda la copia | En la propia cuenta | Fuera de la cuenta, en el almacén |
| Retención | Hasta 200 snapshots por share | Hasta 99 años; snapshots hasta 30 días |
| Restauración | Share completo o ficheros sueltos | Share completo (sin ficheros sueltos) |
| Ransomware o borrado de la cuenta | Expuesto | **Protegido** |

Microsoft recomienda pasar a vaulted.

### Gobierno con Azure Policy

| Definición integrada | Efecto | Uso |
|---|---|---|
| *Azure Backup should be enabled for Virtual Machines* | Audit | Medir cuántas VMs no tienen copia |
| *Configure backup on VMs **with** a given tag to an existing vault in the same location* | DeployIfNotExists | Equipo central de backup; las VMs entran por tag |
| *… **without** a given tag to an existing vault* | DeployIfNotExists | Todo entra salvo lo marcado |
| *… to a **new** vault with a default policy* | DeployIfNotExists | Cada equipo con su almacén por grupo de recursos |

Limitaciones que hay que contar:

- **Una asignación por suscripción y región**, y no se pueden asignar a nivel de grupo de administración.
- **Solo cubre imágenes de Marketplace concretas.** La regla filtra por editor, oferta y SKU, y Microsoft advierte que las imágenes personalizadas pueden no estar soportadas. Las VMs de imágenes de galería o personalizadas pueden quedar fuera.
- Microsoft aconseja no lanzarla sobre más de 200 VMs de golpe.
- Las VMs existentes necesitan una **remediación**.

### Cómo se factura

| Concepto | Cálculo |
|---|---|
| **Instancia protegida** | Por elemento, según los datos reales (en VMs, sin el disco temporal) |
| **Almacenamiento** | GB de los puntos de recuperación, al precio de la redundancia del almacén |
| Snapshots | Aparte; más caros con Enhanced |
| Archivo | Más barato por GB, con 180 días de permanencia mínima |
| Duración | Desde la primera copia correcta y mientras queden datos, aunque se pare la protección |

### Qué escenario recomiendo

| Escenario del cliente | Diseño | Por qué |
|---|---|---|
| Servidores generales | VM Enhanced diaria, 30 días + mensuales | Trusted Launch y snapshots resistentes a zona |
| Servidores críticos con RPO de horas | VM Enhanced cada 4 horas, 7 días de Instant Restore | RPO bajo y restauración rápida |
| SQL Server en VM | Política de SQL: completa diaria + log cada 15 min; la VM con política normal | Restauración a un punto en el tiempo por base de datos |
| Cumplimiento con retención de años | Mensuales/anuales en archivo con `TierRecommended` | Coste por GB mínimo |
| Shares (FSLogix, ficheros departamentales) | Azure Files vaulted | Copia fuera de la cuenta |
| Muchas suscripciones y equipos | Azure Policy por tag hacia el almacén central + auditoría | Nadie se queda sin copia |

### Datos que conviene llevar a la reunión

- **El RPO lo decide la política.** VM Standard: 24 horas. Enhanced: hasta 4 horas. SQL con logs: 15 minutos.
- **Enhanced es obligatoria para VMs nuevas modernas** (Trusted Launch, Premium SSD v2, Ultra) y no tiene vuelta atrás. Cuesta más en snapshots.
- **Hacer copia de la VM no es hacer copia de la base de datos.** SQL Server necesita su propia política para tener restauración a un punto en el tiempo.
- **El archivo no siempre ahorra en VMs**: usar el modo recomendado y contar los 180 días mínimos.
- **Azure Files con snapshot no protege frente al borrado de la cuenta.** Vaulted sí.
- **Azure Policy automatiza la protección, pero solo para imágenes soportadas** y una suscripción y región por asignación.
- **Se factura mientras queden datos**, aunque la VM ya no exista.
- **Probar restauraciones**: es la única forma de saber que el RTO es real.

## Decisiones de diseño

| Decisión | Lo que aplico | Por qué |
|---|---|---|
| Políticas de VM | Enhanced (`V2`) por defecto | Cubre todas las VMs nuevas |
| Instant Restore | 7 días y RG de snapshots con prefijo propio | Restauración rápida en un RG gobernado |
| Retención | Diaria 30 días + semanal/mensual según la carga | Esquema abuelo-padre-hijo, ajustable por política |
| Archivo | `TierRecommended` en la política de retención larga | Solo mueve lo que ahorra |
| Azure Files | `vault-standard` con 7 días de snapshot | Copia fuera de la cuenta y restauración rápida desde snapshot |
| SQL Server en VM | Completa diaria + log cada 15 minutos, compresión | Restauración a un punto en el tiempo |
| Protección de VMs | Por mapa en IaC o por Azure Policy con tag | Explícito para lo crítico y automático para el resto |
| Protección de shares | Una registración por cuenta y una protección por share | Evita el conflicto del módulo |
| Gobierno | Auditoría en cada suscripción + DeployIfNotExists por tag | Visibilidad y corrección |
| Ubicación | Mismo root que la ficha del Recovery Services vault | Políticas y almacén en el mismo ciclo de vida |

Alineación con el Well-Architected Framework:

- **Fiabilidad**: RPO por política, Instant Restore, Cross Region/Zone Restore y pruebas de restauración.
- **Seguridad**: copias fuera de la suscripción (vaulted) y protección del almacén (inmutabilidad, MUA, soft delete).
- **Coste**: niveles, archivo recomendado y retenciones justificadas.
- **Excelencia operativa**: políticas, protección y Azure Policy en IaC; auditoría continua.
- **Rendimiento**: horarios repartidos y 100 VMs como máximo por política.

## Módulo de Terraform

### Los módulos del repositorio

| Pieza | Módulo | Estado |
|---|---|---|
| Política de VMs | [`BackupAndUpdate/BackupPolicyVM`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/BackupAndUpdate/BackupPolicyVM) | **Utilizable** |
| Política de Azure Files | [`BackupAndUpdate/BackupPolicyFileShare`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/BackupAndUpdate/BackupPolicyFileShare) | Solo snapshot |
| Protección de VMs | [`BackupAndUpdate/BackupProtectedVM`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/BackupAndUpdate/BackupProtectedVM) | **Utilizable** |
| Protección de shares | [`BackupAndUpdate/BackupProtectedFileShare`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/BackupAndUpdate/BackupProtectedFileShare) | **Falla con varios shares de una misma cuenta** |
| Política de SQL Server en VM | — | No hay módulo |

**`BackupPolicyVM`**:

- Expone el archivo (`tiering_policy`).
- `instant_restore_retention_days = 2` por defecto falla con frecuencia `Weekly`, porque el provider exige 5.
- `instant_restore_resource_group.prefix` es opcional en el módulo, pero obligatorio en el provider.
- No expone `consistency_type`.

**`BackupPolicyFileShare`** no expone `backup_tier` ni `snapshot_retention_in_days` (azurerm 4.58.0 o posterior), así que solo crea políticas de snapshot. En la ficha va nativo.

**`BackupProtectedVM`**:

- Usa `count` y admite azurerm desde 3.70.
- Con `protection_state = "BackupsSuspended"` o `"ProtectionStopped"`, la API puede no devolver `backup_policy_id`. El provider recomienda `ignore_changes`, que no se puede añadir desde fuera del módulo: diff perpetuo.

**`BackupProtectedFileShare`**:

- Registra la cuenta (`azurerm_backup_container_storage_account`) en cada llamada. El contenedor es uno por cuenta y almacén, así que **el segundo share de la misma cuenta intenta crear un recurso que ya existe**.
- Declara una variable `tags` que no usa ningún recurso.
- En la ficha, la registración va una vez por cuenta y la protección, por share.

**SQL Server en VM**: azurerm tiene la política (`azurerm_backup_policy_vm_workload`), pero **no tiene recurso para registrar la VM ni proteger bases de datos**. Eso se hace con PowerShell, CLI o REST, preferiblemente con autoprotección por instancia.

### Estructura en el proyecto

Mismo root que la [ficha del Recovery Services vault](/recursos/backups-update/recovery-services-vault/). Este `backup_policies.tf` **sustituye** al de esa ficha:

```txt
/
├── providers.tf                 # el de la ficha Recovery Services Vault (azurerm >= 4.64.0)
├── recovery_services_vaults.tf  # el de la ficha Recovery Services Vault
├── backup_policies.tf           # VMs (módulo), Azure Files y SQL Server
├── backup_protection.tf         # VMs (módulo) y shares
├── backup_governance.tf         # Azure Policy: auditoría y protección por tag
└── env/
    └── pro.tfvars
```

### Políticas · `backup_policies.tf`

```hcl
# =============================================================================
# Políticas de Azure Backup en el Recovery Services vault: VMs (Enhanced, con
# archivo opcional), Azure Files (snapshot o vaulted) y SQL Server en VMs
# Sustituye al backup_policies.tf de la ficha Recovery Services Vault (lo amplía)
# DEPENDENCY: azurerm_recovery_services_vault.this (recovery_services_vaults.tf)
# =============================================================================

variable "backup_policies_vm" {
  description = "Políticas de VMs (clave = nombre de la política)."
  type = map(object({
    vault       = string                # clave de var.recovery_services_vaults
    policy_type = optional(string, "V2") # V2 = Enhanced
    timezone    = string

    backup = object({
      frequency     = string # Hourly (solo V2) | Daily | Weekly
      time          = optional(string, "23:00")
      hour_interval = optional(number)
      hour_duration = optional(number)
      weekdays      = optional(list(string))
    })

    instant_restore_retention_days = optional(number, 7)
    instant_restore_rg_prefix      = string

    retention_daily = optional(number, 30)
    retention_weekly = optional(object({
      count    = number
      weekdays = list(string)
    }))
    retention_monthly = optional(object({
      count    = number
      weekdays = optional(list(string))
      weeks    = optional(list(string))
    }))
    retention_yearly = optional(object({
      count    = number
      months   = list(string)
      weekdays = optional(list(string))
      weeks    = optional(list(string))
    }))

    # Archivo: solo puntos mensuales y anuales; no en almacenes ZRS
    archive = optional(object({
      mode          = string # TierRecommended | TierAfter
      duration      = optional(number)
      duration_type = optional(string) # Months con TierAfter (mínimo 3)
    }))
  }))
  default = {}

  validation {
    condition     = alltrue([for k, v in var.backup_policies_vm : v.backup.frequency != "Hourly" || v.policy_type == "V2"])
    error_message = "La frecuencia Hourly solo existe en la política Enhanced (V2)."
  }

  validation {
    condition     = alltrue([for k, v in var.backup_policies_vm : v.backup.frequency != "Weekly" || v.instant_restore_retention_days == 5])
    error_message = "Con frecuencia Weekly, instant_restore_retention_days debe ser 5."
  }

  validation {
    condition = alltrue([
      for k, v in var.backup_policies_vm :
      v.archive == null || v.retention_monthly != null || v.retention_yearly != null
    ])
    error_message = "El archivo solo mueve puntos mensuales o anuales: define retention_monthly o retention_yearly."
  }

  validation {
    condition = alltrue([
      for k, v in var.backup_policies_vm :
      v.archive == null || contains(["TierRecommended", "TierAfter"], try(v.archive.mode, ""))
    ])
    error_message = "archive.mode debe ser TierRecommended o TierAfter."
  }
}

variable "backup_policies_file_share" {
  description = "Políticas de Azure Files (clave = nombre de la política)."
  type = map(object({
    vault       = string
    timezone    = string
    backup_tier = optional(string, "vault-standard") # vault-standard (copia fuera de la cuenta) | snapshot

    backup = object({
      frequency = string # Daily | Hourly
      time      = optional(string, "23:00")
      hourly = optional(object({
        interval        = number
        start_time      = string
        window_duration = number
      }))
    })

    snapshot_retention_in_days = optional(number, 7) # vault-standard: menor que retention_daily (máx. 30)
    retention_daily            = number
    retention_weekly = optional(object({
      count    = number
      weekdays = list(string)
    }))
    retention_monthly = optional(object({
      count    = number
      weekdays = optional(list(string))
      weeks    = optional(list(string))
    }))
  }))
  default = {}

  validation {
    condition     = alltrue([for k, v in var.backup_policies_file_share : contains(["vault-standard", "snapshot"], v.backup_tier)])
    error_message = "backup_tier debe ser vault-standard o snapshot."
  }

  validation {
    condition = alltrue([
      for k, v in var.backup_policies_file_share :
      v.backup_tier != "vault-standard" || v.snapshot_retention_in_days < v.retention_daily
    ])
    error_message = "En vault-standard, snapshot_retention_in_days debe ser menor que retention_daily."
  }

  validation {
    condition     = alltrue([for k, v in var.backup_policies_file_share : v.backup_tier != "snapshot" || v.retention_daily <= 200])
    error_message = "En el nivel snapshot, la retención diaria máxima es de 200 días (200 snapshots por share)."
  }
}

variable "backup_policies_sql" {
  description = "Políticas de SQL Server en VMs de Azure (clave = nombre de la política)."
  type = map(object({
    vault               = string
    timezone            = string
    compression_enabled = optional(bool, true)

    full = object({
      frequency       = string # Daily | Weekly
      time            = string
      weekdays        = optional(list(string)) # con Weekly
      retention_daily = optional(number)       # con Daily (7-9999)
      retention_weekly = optional(object({     # obligatoria con Weekly
        count    = number
        weekdays = list(string)
      }))
    })

    log = optional(object({
      frequency_in_minutes = number           # 15, 30, 60, 120, 240, 480, 720 o 1440
      retention_days       = optional(number, 15) # 7-35
    }))
  }))
  default = {}

  validation {
    condition = alltrue([
      for k, v in var.backup_policies_sql :
      v.log == null || (try(v.log.retention_days, 0) >= 7 && try(v.log.retention_days, 0) <= 35)
    ])
    error_message = "La retención de logs debe estar entre 7 y 35 días."
  }

  validation {
    condition = alltrue([
      for k, v in var.backup_policies_sql :
      (v.full.frequency == "Daily" && v.full.retention_daily != null) || (v.full.frequency == "Weekly" && v.full.retention_weekly != null)
    ])
    error_message = "Full diario necesita retention_daily; full semanal necesita retention_weekly."
  }
}

module "backup_policy_vm" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//BackupAndUpdate/BackupPolicyVM?ref=main"
  for_each = var.backup_policies_vm

  name                = each.key
  resource_group_name = azurerm_recovery_services_vault.this[each.value.vault].resource_group_name
  recovery_vault_name = azurerm_recovery_services_vault.this[each.value.vault].name

  policy_type                    = each.value.policy_type
  timezone                       = each.value.timezone
  instant_restore_retention_days = each.value.instant_restore_retention_days
  instant_restore_resource_group = {
    prefix = each.value.instant_restore_rg_prefix
  }

  backup            = each.value.backup
  retention_daily   = each.value.retention_daily
  retention_weekly  = each.value.retention_weekly
  retention_monthly = each.value.retention_monthly
  retention_yearly  = each.value.retention_yearly

  tiering_policy = each.value.archive == null ? null : {
    archive_tier = each.value.archive
  }
}

# Nativo: el módulo BackupPolicyFileShare no expone backup_tier ni snapshot_retention_in_days
resource "azurerm_backup_policy_file_share" "this" {
  for_each            = var.backup_policies_file_share
  name                = each.key
  resource_group_name = azurerm_recovery_services_vault.this[each.value.vault].resource_group_name
  recovery_vault_name = azurerm_recovery_services_vault.this[each.value.vault].name
  timezone            = each.value.timezone

  backup_tier                = each.value.backup_tier
  snapshot_retention_in_days = each.value.backup_tier == "vault-standard" ? each.value.snapshot_retention_in_days : null

  backup {
    frequency = each.value.backup.frequency
    time      = each.value.backup.frequency == "Daily" ? each.value.backup.time : null

    dynamic "hourly" {
      for_each = each.value.backup.hourly != null ? [each.value.backup.hourly] : []
      content {
        interval        = hourly.value.interval
        start_time      = hourly.value.start_time
        window_duration = hourly.value.window_duration
      }
    }
  }

  retention_daily {
    count = each.value.retention_daily
  }

  dynamic "retention_weekly" {
    for_each = each.value.retention_weekly != null ? [each.value.retention_weekly] : []
    content {
      count    = retention_weekly.value.count
      weekdays = retention_weekly.value.weekdays
    }
  }

  dynamic "retention_monthly" {
    for_each = each.value.retention_monthly != null ? [each.value.retention_monthly] : []
    content {
      count    = retention_monthly.value.count
      weekdays = retention_monthly.value.weekdays
      weeks    = retention_monthly.value.weeks
    }
  }
}

resource "azurerm_backup_policy_vm_workload" "sql" {
  for_each            = var.backup_policies_sql
  name                = each.key
  resource_group_name = azurerm_recovery_services_vault.this[each.value.vault].resource_group_name
  recovery_vault_name = azurerm_recovery_services_vault.this[each.value.vault].name
  workload_type       = "SQLDataBase"

  settings {
    time_zone           = each.value.timezone
    compression_enabled = each.value.compression_enabled
  }

  protection_policy {
    policy_type = "Full"

    backup {
      frequency = each.value.full.frequency
      time      = each.value.full.time
      weekdays  = each.value.full.frequency == "Weekly" ? each.value.full.weekdays : null
    }

    dynamic "retention_daily" {
      for_each = each.value.full.frequency == "Daily" ? [each.value.full.retention_daily] : []
      content {
        count = retention_daily.value
      }
    }

    dynamic "retention_weekly" {
      for_each = each.value.full.retention_weekly != null ? [each.value.full.retention_weekly] : []
      content {
        count    = retention_weekly.value.count
        weekdays = retention_weekly.value.weekdays
      }
    }
  }

  dynamic "protection_policy" {
    for_each = each.value.log != null ? [each.value.log] : []
    content {
      policy_type = "Log"

      backup {
        frequency_in_minutes = protection_policy.value.frequency_in_minutes
      }

      simple_retention {
        count = protection_policy.value.retention_days
      }
    }
  }
}

output "backup_policy_ids" {
  description = "IDs de las políticas, para la protección en esta ficha o en los proyectos de carga."
  value = merge(
    { for k, m in module.backup_policy_vm : k => m.id },
    { for k, p in azurerm_backup_policy_file_share.this : k => p.id },
    { for k, p in azurerm_backup_policy_vm_workload.sql : k => p.id },
  )
}
```

### Protección · `backup_protection.tf`

```hcl
# =============================================================================
# Protección de VMs y shares de Azure Files
# DEPENDENCY: backup_policies.tf (políticas) y recovery_services_vaults.tf (almacén)
# DEPENDENCY: VMs y almacén en la misma región; el almacén puede estar en otra
#             suscripción del mismo tenant
# DEPENDENCY: Shares de Azure Files: la cuenta se registra una sola vez por almacén
# =============================================================================

variable "protected_vms" {
  description = "VMs a proteger (clave = nombre lógico)."
  type = map(object({
    vault             = string
    policy            = string # clave de var.backup_policies_vm
    vm_id             = string
    exclude_disk_luns = optional(list(number))
    include_disk_luns = optional(list(number))
  }))
  default = {}

  validation {
    condition     = alltrue([for k, v in var.protected_vms : v.exclude_disk_luns == null || v.include_disk_luns == null])
    error_message = "Usa include_disk_luns o exclude_disk_luns, no ambos."
  }
}

variable "protected_file_shares" {
  description = "Shares a proteger (clave = nombre lógico)."
  type = map(object({
    vault              = string
    policy             = string # clave de var.backup_policies_file_share
    storage_account_id = string
    share_name         = string
  }))
  default = {}
}

module "backup_protected_vm" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//BackupAndUpdate/BackupProtectedVM?ref=main"
  for_each = var.protected_vms

  resource_group_name = azurerm_recovery_services_vault.this[each.value.vault].resource_group_name
  recovery_vault_name = azurerm_recovery_services_vault.this[each.value.vault].name
  backup_policy_id    = module.backup_policy_vm[each.value.policy].id
  source_vm_id        = each.value.vm_id
  exclude_disk_luns   = each.value.exclude_disk_luns
  include_disk_luns   = each.value.include_disk_luns
}

# Una sola registración por cuenta y almacén (el módulo BackupProtectedFileShare la repite por share)
resource "azurerm_backup_container_storage_account" "this" {
  for_each = {
    for item in distinct([
      for k, v in var.protected_file_shares : { vault = v.vault, storage_account_id = v.storage_account_id }
    ]) : "${item.vault}|${item.storage_account_id}" => item
  }

  resource_group_name = azurerm_recovery_services_vault.this[each.value.vault].resource_group_name
  recovery_vault_name = azurerm_recovery_services_vault.this[each.value.vault].name
  storage_account_id  = each.value.storage_account_id
}

resource "azurerm_backup_protected_file_share" "this" {
  for_each                  = var.protected_file_shares
  resource_group_name       = azurerm_recovery_services_vault.this[each.value.vault].resource_group_name
  recovery_vault_name       = azurerm_recovery_services_vault.this[each.value.vault].name
  source_storage_account_id = azurerm_backup_container_storage_account.this["${each.value.vault}|${each.value.storage_account_id}"].storage_account_id
  source_file_share_name    = each.value.share_name
  backup_policy_id          = azurerm_backup_policy_file_share.this[each.value.policy].id
}
```

### Gobierno · `backup_governance.tf`

```hcl
# =============================================================================
# Gobierno de Azure Backup con Azure Policy:
# - Auditoría: "Azure Backup should be enabled for Virtual Machines"
# - Protección automática de VMs con un tag hacia un almacén existente
# DEPENDENCY: El almacén y las VMs, en la misma suscripción y región que la asignación
# DEPENDENCY: La identidad de Terraform necesita permiso para asignar roles en la suscripción
# =============================================================================

variable "backup_policy_audit_subscription_ids" {
  description = "Suscripciones donde auditar VMs sin backup (clave = nombre lógico, valor = /subscriptions/<id>)."
  type        = map(string)
  default     = {}
}

variable "backup_policy_auto_enable" {
  description = "Asignaciones de protección automática por suscripción y región (clave = nombre de la asignación, máx. 64)."
  type = map(object({
    subscription_id   = string # /subscriptions/<id> (la del almacén)
    location          = string # región de las VMs y del almacén
    vm_policy         = string # clave de var.backup_policies_vm
    inclusion_tag     = string # p. ej. "backup"
    inclusion_values  = list(string)
    effect            = optional(string, "DeployIfNotExists") # AuditIfNotExists para empezar solo midiendo
    remediate_existing = optional(bool, false)
  }))
  default = {}

  validation {
    condition     = alltrue([for k, v in var.backup_policy_auto_enable : length(k) <= 64 && length(v.inclusion_tag) > 0])
    error_message = "Nombre de la asignación de 64 caracteres como máximo y tag de inclusión obligatorio."
  }

  validation {
    condition     = alltrue([for k, v in var.backup_policy_auto_enable : contains(["DeployIfNotExists", "AuditIfNotExists", "Disabled"], v.effect)])
    error_message = "effect debe ser DeployIfNotExists, AuditIfNotExists o Disabled."
  }
}

resource "azurerm_subscription_policy_assignment" "backup_audit" {
  for_each             = var.backup_policy_audit_subscription_ids
  name                 = "audit-vm-backup-${each.key}"
  display_name         = "Azure Backup should be enabled for Virtual Machines"
  subscription_id      = each.value
  policy_definition_id = "/providers/Microsoft.Authorization/policyDefinitions/013e242c-8828-4970-87b3-ab247555486d"

  non_compliance_message {
    content = "La VM no tiene Azure Backup configurado."
  }
}

resource "azurerm_subscription_policy_assignment" "backup_auto_enable" {
  for_each             = var.backup_policy_auto_enable
  name                 = each.key
  display_name         = "Backup de VMs con ${each.value.inclusion_tag} en ${each.value.location}"
  subscription_id      = each.value.subscription_id
  location             = each.value.location
  policy_definition_id = "/providers/Microsoft.Authorization/policyDefinitions/345fa903-145c-4fe1-8bcd-93ec2adccde8"

  identity {
    type = "SystemAssigned"
  }

  parameters = jsonencode({
    vaultLocation     = { value = each.value.location }
    inclusionTagName  = { value = each.value.inclusion_tag }
    inclusionTagValue = { value = each.value.inclusion_values }
    backupPolicyId    = { value = module.backup_policy_vm[each.value.vm_policy].id }
    effect            = { value = each.value.effect }
  })
}

# Roles que declara la definición (roleDefinitionIds): Virtual Machine Contributor y Backup Contributor
resource "azurerm_role_assignment" "backup_auto_enable" {
  for_each = {
    for item in flatten([
      for k, v in var.backup_policy_auto_enable : [
        for role in ["Virtual Machine Contributor", "Backup Contributor"] : { key = "${k}|${role}", assignment = k, role = role, scope = v.subscription_id }
      ]
    ]) : item.key => item
  }

  scope                = each.value.scope
  role_definition_name = each.value.role
  principal_id         = azurerm_subscription_policy_assignment.backup_auto_enable[each.value.assignment].identity[0].principal_id
  principal_type       = "ServicePrincipal"
}

# Remediación de las VMs que ya existían (la asignación solo actúa sola sobre VMs nuevas o modificadas)
resource "azurerm_subscription_policy_remediation" "backup_auto_enable" {
  for_each             = { for k, v in var.backup_policy_auto_enable : k => v if v.remediate_existing && v.effect == "DeployIfNotExists" }
  name                 = "remediate-${each.key}"
  subscription_id      = each.value.subscription_id
  policy_assignment_id = azurerm_subscription_policy_assignment.backup_auto_enable[each.key].id
  location_filters     = [each.value.location]

  depends_on = [azurerm_role_assignment.backup_auto_enable]
}
```

### `env/pro.tfvars`

```hcl
# Se añade al pro.tfvars de la ficha Recovery Services Vault (mismo root)

backup_policies_vm = {
  "bkpol-vm-enhanced-4h" = {
    vault       = "rsv-<workload>-pro-<region>-01"
    policy_type = "V2"
    timezone    = "<zona horaria Windows, p. ej. Romance Standard Time>"

    backup = {
      frequency     = "Hourly"
      time          = "08:00"
      hour_interval = 4
      hour_duration = 24
    }

    instant_restore_retention_days = 7
    instant_restore_rg_prefix      = "rg-<workload>-pro-bkp-snapshots-"

    retention_daily = 30
    retention_weekly = {
      count    = 12
      weekdays = ["Sunday"]
    }
    retention_monthly = {
      count    = 12
      weekdays = ["Sunday"]
      weeks    = ["First"]
    }
  }

  "bkpol-vm-daily-ltr" = {
    vault       = "rsv-<workload>-pro-<region>-01"
    policy_type = "V2"
    timezone    = "<zona horaria Windows>"

    backup = {
      frequency = "Daily"
      time      = "23:00"
    }

    instant_restore_retention_days = 7
    instant_restore_rg_prefix      = "rg-<workload>-pro-bkp-snapshots-"

    retention_daily = 30
    retention_monthly = {
      count    = 60
      weekdays = ["Sunday"]
      weeks    = ["First"]
    }
    retention_yearly = {
      count    = 10
      months   = ["January"]
      weekdays = ["Sunday"]
      weeks    = ["First"]
    }

    archive = {
      mode = "TierRecommended" # solo VMs; el almacén no puede ser ZRS
    }
  }
}

backup_policies_file_share = {
  "bkpol-files-vault-daily" = {
    vault       = "rsv-<workload>-pro-<region>-01"
    timezone    = "<zona horaria Windows>"
    backup_tier = "vault-standard"
    backup = {
      frequency = "Daily"
      time      = "22:00"
    }
    snapshot_retention_in_days = 7
    retention_daily            = 30
    retention_weekly = {
      count    = 12
      weekdays = ["Sunday"]
    }
  }
}

backup_policies_sql = {
  "bkpol-sql-daily-log15" = {
    vault    = "rsv-<workload>-pro-<region>-01"
    timezone = "<zona horaria Windows>"
    full = {
      frequency       = "Daily"
      time            = "01:00"
      retention_daily = 30
    }
    log = {
      frequency_in_minutes = 15
      retention_days       = 15
    }
  }
}

protected_vms = {
  app-01 = {
    vault  = "rsv-<workload>-pro-<region>-01"
    policy = "bkpol-vm-enhanced-4h"
    vm_id  = "<resourceId vm-app-01>"
  }
}

protected_file_shares = {
  fslogix-profiles = {
    vault              = "rsv-<workload>-pro-<region>-01"
    policy             = "bkpol-files-vault-daily"
    storage_account_id = "<resourceId cuenta FSLogix>"
    share_name         = "profiles"
  }
}

backup_policy_audit_subscription_ids = {
  workload-pro = "/subscriptions/<subscriptionId>"
}

backup_policy_auto_enable = {
  "bkp-auto-vm-pro-<region>" = {
    subscription_id    = "/subscriptions/<subscriptionId>"
    location           = "<region>"
    vm_policy          = "bkpol-vm-daily-ltr"
    inclusion_tag      = "backup"
    inclusion_values   = ["daily-ltr"]
    effect             = "DeployIfNotExists"
    remediate_existing = true
  }
}
```

### SQL Server en VM (fuera de Terraform)

Con la política creada, se registra la VM y se activa la autoprotección de la instancia. Las bases de datos nuevas entran solas:

```powershell
$vault  = Get-AzRecoveryServicesVault -ResourceGroupName "<rg-backup-pro>" -Name "rsv-<workload>-pro-<region>-01"
$vm     = Get-AzVM -ResourceGroupName "<rg-sql-pro>" -Name "<vm-sql-01>"
$policy = Get-AzRecoveryServicesBackupProtectionPolicy -Name "bkpol-sql-daily-log15" -VaultId $vault.ID

Register-AzRecoveryServicesBackupContainer -ResourceId $vm.ID -BackupManagementType AzureWorkload -WorkloadType MSSQL -VaultId $vault.ID -Force

$instance = Get-AzRecoveryServicesBackupProtectableItem -WorkloadType MSSQL -ItemType SQLInstance -VaultId $vault.ID -Name "MSSQLSERVER" -ServerName "<vm-sql-01>"
Enable-AzRecoveryServicesBackupAutoProtection -InputItem $instance -BackupManagementType AzureWorkload -WorkloadType MSSQL -Policy $policy -VaultId $vault.ID
```

### Despliegue y comprobación

```powershell
terraform init
terraform plan -var-file="env/pro.tfvars" -out="pro.tfplan"
terraform apply "pro.tfplan"

# Elementos protegidos y último backup
$vault = Get-AzRecoveryServicesVault -ResourceGroupName "<rg-backup-pro>" -Name "rsv-<workload>-pro-<region>-01"
Get-AzRecoveryServicesBackupItem -BackupManagementType AzureVM -WorkloadType AzureVM -VaultId $vault.ID |
    Select-Object Name, ProtectionStatus, LastBackupStatus, LastBackupTime

# VMs sin backup en las suscripciones visibles (Azure Resource Graph)
$query = @"
Resources
| where type in~ ('microsoft.compute/virtualmachines')
| extend resourceId = tolower(id)
| join kind = leftouter (RecoveryServicesResources
    | where type == 'microsoft.recoveryservices/vaults/backupfabrics/protectioncontainers/protecteditems'
    | where properties.backupManagementType == 'AzureIaasVM'
    | project resourceId = tolower(tostring(properties.sourceResourceId)), backupItemId = id) on resourceId
| where isempty(backupItemId)
| project name, resourceGroup, location, tags
"@
Search-AzGraph -Query $query
```

### Equivalente en Bicep

`main.bicep` (políticas y protección sobre el almacén existente):

```bicep
// =============================================================================
// Azure Backup en un Recovery Services vault existente: políticas (VM Enhanced con
// archivo, Azure Files vaulted, SQL Server en VM) y protección de VMs y shares
// DEPENDENCY: Recovery Services vault existente en este RG (ficha Recovery Services Vault)
// DEPENDENCY: VMs y cuentas de almacenamiento en la misma región que el almacén
// =============================================================================
targetScope = 'resourceGroup'

param vaultName string

@description('Zona horaria Windows, p. ej. Romance Standard Time.')
param timeZone string

param snapshotResourceGroupPrefix string

@description('VMs a proteger: [{ name, resourceGroup }].')
param protectedVms array = []

@description('Shares a proteger (una sola cuenta): nombre de la cuenta, su RG y los shares.')
param fileShareStorageAccountName string = ''
param fileShareStorageAccountResourceGroup string = ''
param fileShareNames array = []

// Las horas de las políticas se expresan como fecha y hora; solo cuenta la hora
var vmBackupTime = '2026-01-01T23:00:00Z'
var filesBackupTime = '2026-01-01T22:00:00Z'
var sqlFullTime = '2026-01-01T01:00:00Z'

resource vault 'Microsoft.RecoveryServices/vaults@2025-02-01' existing = {
  name: vaultName
}

// VMs: Enhanced diaria, LTR mensual 5 años y anual 10 años, archivo de los puntos recomendados
resource policyVm 'Microsoft.RecoveryServices/vaults/backupPolicies@2025-02-01' = {
  parent: vault
  name: 'bkpol-vm-daily-ltr'
  properties: {
    backupManagementType: 'AzureIaasVM'
    policyType: 'V2'
    timeZone: timeZone
    instantRpRetentionRangeInDays: 7
    instantRPDetails: {
      azureBackupRGNamePrefix: snapshotResourceGroupPrefix
    }
    schedulePolicy: {
      schedulePolicyType: 'SimpleSchedulePolicyV2'
      scheduleRunFrequency: 'Daily'
      dailySchedule: {
        scheduleRunTimes: [
          vmBackupTime
        ]
      }
    }
    retentionPolicy: {
      retentionPolicyType: 'LongTermRetentionPolicy'
      dailySchedule: {
        retentionTimes: [
          vmBackupTime
        ]
        retentionDuration: {
          count: 30
          durationType: 'Days'
        }
      }
      monthlySchedule: {
        retentionScheduleFormatType: 'Weekly'
        retentionScheduleWeekly: {
          daysOfTheWeek: [
            'Sunday'
          ]
          weeksOfTheMonth: [
            'First'
          ]
        }
        retentionTimes: [
          vmBackupTime
        ]
        retentionDuration: {
          count: 60
          durationType: 'Months'
        }
      }
      yearlySchedule: {
        retentionScheduleFormatType: 'Weekly'
        monthsOfYear: [
          'January'
        ]
        retentionScheduleWeekly: {
          daysOfTheWeek: [
            'Sunday'
          ]
          weeksOfTheMonth: [
            'First'
          ]
        }
        retentionTimes: [
          vmBackupTime
        ]
        retentionDuration: {
          count: 10
          durationType: 'Years'
        }
      }
    }
    tieringPolicy: {
      ArchivedRP: {
        tieringMode: 'TierRecommended'
      }
    }
  }
}

// Azure Files: vaulted (copia fuera de la cuenta), snapshots 7 días y almacén 30 días + 12 semanas
resource policyFiles 'Microsoft.RecoveryServices/vaults/backupPolicies@2025-02-01' = {
  parent: vault
  name: 'bkpol-files-vault-daily'
  properties: {
    backupManagementType: 'AzureStorage'
    workLoadType: 'AzureFileShare'
    timeZone: timeZone
    schedulePolicy: {
      schedulePolicyType: 'SimpleSchedulePolicy'
      scheduleRunFrequency: 'Daily'
      scheduleRunTimes: [
        filesBackupTime
      ]
    }
    vaultRetentionPolicy: {
      snapshotRetentionInDays: 7
      vaultRetention: {
        retentionPolicyType: 'LongTermRetentionPolicy'
        dailySchedule: {
          retentionTimes: [
            filesBackupTime
          ]
          retentionDuration: {
            count: 30
            durationType: 'Days'
          }
        }
        weeklySchedule: {
          daysOfTheWeek: [
            'Sunday'
          ]
          retentionTimes: [
            filesBackupTime
          ]
          retentionDuration: {
            count: 12
            durationType: 'Weeks'
          }
        }
      }
    }
  }
}

// SQL Server en VM: completo diario 30 días + log cada 15 minutos 15 días
resource policySql 'Microsoft.RecoveryServices/vaults/backupPolicies@2025-02-01' = {
  parent: vault
  name: 'bkpol-sql-daily-log15'
  properties: {
    backupManagementType: 'AzureWorkload'
    workLoadType: 'SQLDataBase'
    settings: {
      timeZone: timeZone
      issqlcompression: true
    }
    subProtectionPolicy: [
      {
        policyType: 'Full'
        schedulePolicy: {
          schedulePolicyType: 'SimpleSchedulePolicy'
          scheduleRunFrequency: 'Daily'
          scheduleRunTimes: [
            sqlFullTime
          ]
        }
        retentionPolicy: {
          retentionPolicyType: 'LongTermRetentionPolicy'
          dailySchedule: {
            retentionTimes: [
              sqlFullTime
            ]
            retentionDuration: {
              count: 30
              durationType: 'Days'
            }
          }
        }
      }
      {
        policyType: 'Log'
        schedulePolicy: {
          schedulePolicyType: 'LogSchedulePolicy'
          scheduleFrequencyInMins: 15
        }
        retentionPolicy: {
          retentionPolicyType: 'SimpleRetentionPolicy'
          retentionDuration: {
            count: 15
            durationType: 'Days'
          }
        }
      }
    ]
  }
}

// Protección de VMs: contenedor iaasvmcontainer;iaasvmcontainerv2;<rg>;<vm>
resource vmProtection 'Microsoft.RecoveryServices/vaults/backupFabrics/protectionContainers/protectedItems@2025-02-01' = [
  for vm in protectedVms: {
    name: '${vaultName}/Azure/iaasvmcontainer;iaasvmcontainerv2;${vm.resourceGroup};${vm.name}/vm;iaasvmcontainerv2;${vm.resourceGroup};${vm.name}'
    properties: {
      protectedItemType: 'Microsoft.Compute/virtualMachines'
      policyId: policyVm.id
      sourceResourceId: resourceId(vm.resourceGroup, 'Microsoft.Compute/virtualMachines', vm.name)
    }
  }
]

// Azure Files: la cuenta se registra una vez y después se protege cada share
var storageContainerName = 'storagecontainer;Storage;${fileShareStorageAccountResourceGroup};${fileShareStorageAccountName}'

resource storageContainer 'Microsoft.RecoveryServices/vaults/backupFabrics/protectionContainers@2025-02-01' = if (!empty(fileShareNames)) {
  name: '${vaultName}/Azure/${storageContainerName}'
  properties: {
    backupManagementType: 'AzureStorage'
    containerType: 'StorageContainer'
    sourceResourceId: resourceId(fileShareStorageAccountResourceGroup, 'Microsoft.Storage/storageAccounts', fileShareStorageAccountName)
  }
}

resource shareProtection 'Microsoft.RecoveryServices/vaults/backupFabrics/protectionContainers/protectedItems@2025-02-01' = [
  for share in fileShareNames: {
    parent: storageContainer
    name: 'AzureFileShare;${share}'
    properties: {
      protectedItemType: 'AzureFileShareProtectedItem'
      sourceResourceId: resourceId(fileShareStorageAccountResourceGroup, 'Microsoft.Storage/storageAccounts', fileShareStorageAccountName)
      policyId: policyFiles.id
    }
  }
]

output vmPolicyId string = policyVm.id
output filesPolicyId string = policyFiles.id
output sqlPolicyId string = policySql.id
```

`main.pro.bicepparam`:

```bicep
using 'main.bicep'

param vaultName = 'rsv-<workload>-pro-<region>-01'
param timeZone = '<zona horaria Windows, p. ej. Romance Standard Time>'
param snapshotResourceGroupPrefix = 'rg-<workload>-pro-bkp-snapshots-'

param protectedVms = [
  {
    name: 'vm-app-01'
    resourceGroup: '<rg-app-pro>'
  }
]

param fileShareStorageAccountName = '<cuenta FSLogix>'
param fileShareStorageAccountResourceGroup = '<rg-avd-pro>'
param fileShareNames = [
  'profiles'
]
```

`governance.bicep` (ámbito de suscripción):

```bicep
// =============================================================================
// Gobierno de Azure Backup con Azure Policy (ámbito de suscripción)
// DEPENDENCY: almacén y VMs en esta suscripción y en la región indicada
// DEPENDENCY: política de VM existente (salida vmPolicyId de main.bicep)
// =============================================================================
targetScope = 'subscription'

param location string
param vmBackupPolicyId string
param inclusionTagName string = 'backup'
param inclusionTagValues array

@allowed(['DeployIfNotExists', 'AuditIfNotExists', 'Disabled'])
param effect string = 'DeployIfNotExists'

param remediateExisting bool = false

var auditDefinitionId = '/providers/Microsoft.Authorization/policyDefinitions/013e242c-8828-4970-87b3-ab247555486d'
var autoEnableDefinitionId = '/providers/Microsoft.Authorization/policyDefinitions/345fa903-145c-4fe1-8bcd-93ec2adccde8'

// Roles declarados por la definición: Virtual Machine Contributor y Backup Contributor
var roleIds = [
  '9980e02c-c2be-4d73-94e8-173b1dc7cf3c'
  '5e467623-bb1f-42f4-a55d-6e525e11384b'
]

resource auditAssignment 'Microsoft.Authorization/policyAssignments@2024-04-01' = {
  name: 'audit-vm-backup'
  properties: {
    displayName: 'Azure Backup should be enabled for Virtual Machines'
    policyDefinitionId: auditDefinitionId
    nonComplianceMessages: [
      {
        message: 'La VM no tiene Azure Backup configurado.'
      }
    ]
  }
}

resource autoEnableAssignment 'Microsoft.Authorization/policyAssignments@2024-04-01' = {
  name: 'bkp-auto-vm-${location}'
  location: location
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    displayName: 'Backup de VMs con ${inclusionTagName} en ${location}'
    policyDefinitionId: autoEnableDefinitionId
    parameters: {
      vaultLocation: {
        value: location
      }
      inclusionTagName: {
        value: inclusionTagName
      }
      inclusionTagValue: {
        value: inclusionTagValues
      }
      backupPolicyId: {
        value: vmBackupPolicyId
      }
      effect: {
        value: effect
      }
    }
  }
}

resource assignmentRoles 'Microsoft.Authorization/roleAssignments@2022-04-01' = [
  for roleId in roleIds: {
    name: guid(subscription().id, autoEnableAssignment.id, roleId)
    properties: {
      principalId: autoEnableAssignment.identity.principalId
      principalType: 'ServicePrincipal'
      roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', roleId)
    }
  }
]

resource remediation 'Microsoft.PolicyInsights/remediations@2021-10-01' = if (remediateExisting && effect == 'DeployIfNotExists') {
  name: 'remediate-bkp-auto-vm-${location}'
  properties: {
    policyAssignmentId: autoEnableAssignment.id
    filters: {
      locations: [
        location
      ]
    }
    resourceDiscoveryMode: 'ExistingNonCompliant'
  }
  dependsOn: [
    assignmentRoles
  ]
}
```

`governance.pro.bicepparam`:

```bicep
using 'governance.bicep'

param location = '<region>'
param vmBackupPolicyId = '<vmPolicyId de main.bicep>'
param inclusionTagName = 'backup'
param inclusionTagValues = [
  'daily-ltr'
]
param effect = 'DeployIfNotExists'
param remediateExisting = true
```

Despliegue:

```powershell
az deployment group create --resource-group <rg-backup-pro> --parameters main.pro.bicepparam
az deployment sub create   --location <region> --parameters governance.pro.bicepparam
```

## Errores típicos

| Síntoma | Causa | Solución |
|---|---|---|
| El segundo share de una cuenta falla con *already exists* | Se registra la cuenta una vez por share (módulo `BackupProtectedFileShare`) | Una registración por cuenta y almacén |
| `instant_restore_retention_days` rechazado | Con frecuencia `Weekly` el provider exige 5 | Ajustar a 5 o usar frecuencia diaria |
| La política de archivo no se puede guardar | Retención mensual/anual insuficiente (VM: TierAfter + 6 meses; SQL: TierAfter + 180 días) o almacén ZRS | Alargar la retención o usar un almacén GRS/LRS |
| La factura de almacenamiento sube al archivar VMs | Los puntos incrementales pasan a completos | `TierRecommended` en lugar de mover todo |
| Cobros tras borrar puntos archivados | Borrado anticipado (menos de 180 días en archivo) | Archivar solo retenciones largas |
| No se puede proteger una VM Trusted Launch desde el portal con política Standard | Standard solo la admite por CLI, PowerShell o REST recientes | Política Enhanced |
| Se quiere volver de Enhanced a Standard | No está soportado | Decidir antes; nuevas VMs en Enhanced |
| La copia de la VM no permite restaurar SQL a un minuto concreto | La copia de VM es *copy-only* sin logs | Política de SQL Server en VM con logs |
| Las copias de log de una base de datos no se ejecutan | La base está en modelo de recuperación *Simple* | Modelo *Full* o asumir solo completas |
| Linux con copias solo coherentes con el sistema de archivos | Sin pre/post scripts o fallan | Configurar `VMSnapshotScriptPluginConfig.json` (permisos 600/700) |
| La asignación de Azure Policy no protege ninguna VM | Tag de inclusión vacío o valores sin formato de array | `inclusionTagName` informado y valores como `["valor"]` |
| VMs de imagen personalizada sin protección automática | La definición solo cubre editores, ofertas y SKUs concretos de Marketplace | Protegerlas por IaC (`protected_vms`) |
| Las VMs existentes no se protegen tras asignar la política | DeployIfNotExists solo actúa sola en VMs nuevas o modificadas | Tarea de remediación |
| Retrasos de horas en las primeras copias tras asignar la política | Demasiadas VMs a la vez | Menos de 200 VMs por oleada |
| `diff` perpetuo en `backup_policy_id` de una VM con protección parada | La API no devuelve la política | `ignore_changes` (no posible desde el módulo) |
| La plantilla "vault tier" de Microsoft crea copias solo con snapshot | El quickstart de Bicep/ARM no define `vaultRetentionPolicy` | Definir `vaultRetentionPolicy` (Bicep) o `backup_tier = "vault-standard"` (Terraform) |
| La copia de Azure Files falla con el acceso por clave desactivado | Por defecto se usa la clave de la cuenta; el acceso *IdentityBased* existe en la API y en Az PowerShell, no en azurerm | Activar la clave o proteger con `-AccessType IdentityBased` fuera de Terraform |
