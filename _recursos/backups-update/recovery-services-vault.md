---
title: "Recovery Services Vault"
indice: backups-update
resumen: "Almacén de copias de máquinas, SQL y ficheros."
estado: documentado   # proximamente | en-curso | documentado
orden: 1
last_review: 2026-10-20
fuentes:
  - titulo: "Recovery Services vaults overview"
    url: https://learn.microsoft.com/azure/backup/backup-azure-recovery-services-vault-overview
  - titulo: "Create and configure a Recovery Services vault"
    url: https://learn.microsoft.com/azure/backup/backup-create-recovery-services-vault
  - titulo: "Support matrix for Azure Backup"
    url: https://learn.microsoft.com/azure/backup/backup-support-matrix
  - titulo: "Azure Backup - Frequently asked questions"
    url: https://learn.microsoft.com/azure/backup/backup-azure-backup-faq
  - titulo: "Secure by default with soft delete for Azure Backup"
    url: https://learn.microsoft.com/azure/backup/secure-by-default
  - titulo: "Immutable vault for Azure Backup"
    url: https://learn.microsoft.com/azure/backup/backup-azure-immutable-vault-concept
  - titulo: "Multiuser authorization using Resource Guard"
    url: https://learn.microsoft.com/azure/backup/multi-user-authorization-concept
  - titulo: "Configure Multi-user authorization using Resource Guard"
    url: https://learn.microsoft.com/azure/backup/multi-user-authorization
  - titulo: "Overview of security features in Azure Backup"
    url: https://learn.microsoft.com/azure/backup/security-overview
  - titulo: "Azure Backup security best practices to safeguard backup data"
    url: https://learn.microsoft.com/azure/backup/azure-backup-data-protection-best-practices
  - titulo: "Private endpoints for Azure Backup: Version 2 experience"
    url: https://learn.microsoft.com/azure/backup/backup-azure-private-endpoints-concept
  - titulo: "Create and use private endpoints (v2 experience) for Azure Backup"
    url: https://learn.microsoft.com/azure/backup/backup-azure-private-endpoints-configure-manage
  - titulo: "Encrypt backup data by using customer-managed keys"
    url: https://learn.microsoft.com/azure/backup/encryption-at-rest-with-cmk
  - titulo: "Monitoring and Reporting solutions for Azure Backup"
    url: https://learn.microsoft.com/azure/backup/monitoring-and-alerts-overview
  - titulo: "Manage Azure Monitor based alerts for Azure Backup"
    url: https://learn.microsoft.com/azure/backup/backup-azure-monitoring-alerts
  - titulo: "Diagnostic Events for Azure Backup users"
    url: https://learn.microsoft.com/azure/backup/backup-azure-diagnostic-events
  - titulo: "Supported logs for Microsoft.RecoveryServices/Vaults"
    url: https://learn.microsoft.com/azure/azure-monitor/reference/supported-logs/microsoft-recoveryservices-vaults-logs
  - titulo: "Back up an Azure VM by using the Enhanced policy"
    url: https://learn.microsoft.com/azure/backup/backup-azure-vms-enhanced-policy
  - titulo: "Instant Restore capability (coste de snapshots)"
    url: https://learn.microsoft.com/azure/backup/backup-instant-restore-capability
  - titulo: "An overview of Azure VM backup (costes)"
    url: https://learn.microsoft.com/azure/backup/backup-azure-vms-introduction
  - titulo: "Estimate Azure Backup costs and understand pricing"
    url: https://learn.microsoft.com/azure/backup/azure-backup-pricing
  - titulo: "Reliability in Azure Backup"
    url: https://learn.microsoft.com/azure/reliability/reliability-backup
  - titulo: "Microsoft.RecoveryServices vaults (plantillas ARM/Bicep)"
    url: https://learn.microsoft.com/azure/templates/microsoft.recoveryservices/vaults
  - titulo: "azurerm_recovery_services_vault"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/recovery_services_vault
  - titulo: "azurerm_recovery_services_vault_resource_guard_association"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/recovery_services_vault_resource_guard_association
  - titulo: "azurerm_backup_policy_vm"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/backup_policy_vm
  - titulo: "Módulo Terraform BackupAndUpdate/RecoveryServicesVault"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/BackupAndUpdate/RecoveryServicesVault
  - titulo: "Módulo Terraform BackupAndUpdate/BackupPolicyVM"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/BackupAndUpdate/BackupPolicyVM
  - titulo: "Módulo Terraform BackupAndUpdate/BackupPolicyFileShare"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/BackupAndUpdate/BackupPolicyFileShare
---

El **Recovery Services vault** es el almacén de Azure Backup (y de Azure Site Recovery) para máquinas virtuales, SQL Server y SAP HANA en VMs de Azure, Azure Files y servidores on-premises con el agente MARS, MABS o DPM. Guarda los puntos de recuperación y las políticas que los crean. El almacenamiento lo gestiona Azure: no hay cuentas de almacenamiento que crear ni que dimensionar. Las decisiones importantes son la **redundancia**, la **seguridad del propio almacén** (soft delete, inmutabilidad, MUA) y la **red**. Varias de ellas son irreversibles o solo se pueden tomar antes de proteger el primer elemento.

## Qué es y cuándo usarlo

### Recovery Services vault o Backup vault

| Carga | Almacén |
|---|---|
| VMs de Azure, SQL Server y SAP HANA en VMs, Azure Files | **Recovery Services vault** |
| Servidores on-premises (agente MARS, MABS, DPM) | **Recovery Services vault** |
| Replicación y DR con Azure Site Recovery | **Recovery Services vault** ([ficha](/recursos/backups-update/azure-site-recovery/)) |
| Discos administrados, blobs, Azure Database for PostgreSQL, AKS | [Backup vault](/recursos/backups-update/backup-vault/) |

Un almacén protege solo cargas **de su misma región**: hace falta un almacén por región con cargas. La VM y el almacén sí pueden estar en suscripciones distintas.

### Redundancia del almacenamiento de backup

| Opción | Qué protege | Cuándo |
|---|---|---|
| **GRS** (valor por defecto) | Copia en la región emparejada | Producción con Azure como destino principal de backup |
| GRS + **Cross Region Restore** | Además, restaurar en la región secundaria sin esperar a que Microsoft declare desastre | Simulacros de DR y cumplimiento |
| ZRS | Tres zonas de la región, residencia del dato | Requisito de no salir de la región |
| LRS | Tres copias en un datacenter | Dev/test o cuando Azure no es la copia principal |

**La redundancia solo se puede cambiar antes de configurar el primer backup.** Cross Region Restore no se puede desactivar una vez activado, cuesta más y los elementos tardan hasta 48 horas en estar disponibles en la región secundaria. El RPO en la secundaria puede llegar a 36 horas.

### Seguridad del almacén

| Capacidad | Qué hace | Reversible |
|---|---|---|
| **Soft delete** | Conserva 14-180 días los datos borrados (los 14 primeros sin coste) | **Obligatorio**: no se puede desactivar con ningún cliente ni versión de API |
| **Inmutabilidad** *Enabled* (`Unlocked`) | Bloquea operaciones que pierden puntos de recuperación: reducir retención, parar con borrado… | Sí |
| **Inmutabilidad** *Enabled and locked* (`Locked`) | Lo mismo, de forma irreversible y con almacenamiento WORM | **No** |
| **Multi-user authorization (MUA)** | Las operaciones críticas exigen permiso sobre un *Resource Guard* de otro equipo | Sí, con aprobación |
| **CMK** | Cifra con tu clave de Key Vault en lugar de la de plataforma | **No** se puede desactivar |

Niveles de seguridad que muestra Azure: **Excellent** = inmutabilidad bloqueada o soft delete *AlwaysON* + MUA; **Good** = inmutabilidad bloqueada o soft delete; **Fair** = solo MUA; **Poor** = nada de lo anterior. Con el soft delete forzado, **todo almacén nuevo parte de Good**; MUA lo sube a Excellent.

### Red: cuándo hace falta Private Endpoint

| Carga | ¿Private Endpoint? |
|---|---|
| Backup de VMs de Azure | No lo necesita (sí para **restaurar ficheros sueltos** desde un almacén con PE) |
| Azure Files | No (los snapshots están en la propia cuenta) |
| SQL Server / SAP HANA en VMs, agente MARS, DPM 2022+ y MABS v4+ | **Sí**, recomendado |

- **El Private Endpoint solo se puede crear en almacenes que nunca han registrado ni intentado proteger nada.**
- Cada Private Endpoint consume unas 10 IPs que pueden crecer: Microsoft recomienda una /25 libre. Máximo 12 por almacén.
- Hacen falta tres zonas privadas: `privatelink.<geo>.backup.windowsazure.com`, `privatelink.blob.core.windows.net` y `privatelink.queue.core.windows.net`.

### Límites que conviene conocer

| Límite | Valor |
|---|---|
| Almacenes por suscripción | 500 |
| Elementos protegidos por almacén (recomendado) | 2.000 de todas las cargas |
| VMs por almacén | 1.000 (250 registros al día) |
| VMs por política | 100 |
| Políticas por almacén | 200; con ARM, PowerShell o CLI, 50 altas o cambios cada 24 horas |
| Mover almacenes | Entre suscripciones o grupos de recursos, nunca entre regiones |
| Mover datos entre almacenes | No soportado |

### Cómo se factura

| Concepto | Cálculo |
|---|---|
| **Instancia protegida** | Por elemento, según el tamaño usado (en VMs, datos reales de los discos, sin el disco temporal) |
| **Almacenamiento de backup** | GB consumidos por los puntos de recuperación, al precio de la redundancia elegida |
| Snapshots de Instant Restore | Aparte, como almacenamiento de snapshots. Con la política Enhanced el primero es una copia completa |
| Cross Region Restore | Recargo sobre GRS |
| Alertas integradas | Gratis; los avisos por email, gratis hasta 1.000 al mes |

La facturación empieza con el primer backup correcto y **continúa mientras quede algún dato en el almacén**, aunque se haya parado la protección.

### Qué escenario recomiendo

| Escenario del cliente | Diseño | Por qué |
|---|---|---|
| Producción estándar | GRS, inmutabilidad `Unlocked` → `Locked` tras validar, MUA, alertas de Azure Monitor | Nivel *Excellent* y protección frente a ransomware |
| DR con simulacros obligatorios | GRS + Cross Region Restore (acceso público habilitado) | Restaurar en la secundaria en cualquier momento |
| Residencia del dato en la región | ZRS | Sin copia en otra región |
| SQL/HANA en VMs o servidores on-premises | Almacén **nuevo** con Private Endpoint y acceso público denegado | El PE no se añade después |
| VMs con Trusted Launch, Premium SSD v2 o Ultra | Política **Enhanced** (V2) | La Standard no las soporta o tiene limitaciones |
| Dev/test | LRS, sin Cross Region Restore | Coste |

### Datos que conviene llevar a la reunión

- **Hay decisiones de día cero**: redundancia, CMK y Private Endpoint solo se pueden fijar **antes de proteger el primer elemento**. Si se cambian después, hay que crear otro almacén.
- **El soft delete ya no es opcional**: Azure lo fuerza en todos los almacenes, incluido el propio almacén cuando se borra. Lo que se decide es la retención (14-180 días) y si se bloquea la inmutabilidad.
- **Inmutabilidad bloqueada es para siempre**: no se pueden reducir retenciones y el almacén solo se puede borrar a través de soporte.
- **MUA** necesita un segundo equipo (seguridad) dueño del Resource Guard, idealmente en otra suscripción o tenant.
- **Las alertas clásicas están retiradas** (fecha anunciada: 31 de marzo de 2026). Las alertas de Azure Monitor se generan solas; lo que hay que diseñar es a quién se notifican.
- **El backup de VMs no necesita Private Endpoint.** El de SQL/HANA en VMs y el agente MARS, sí. Si el cliente los usa, el almacén debe nacer con PE.
- **Cross Region Restore y acceso público denegado no son compatibles** hoy: hay que elegir.
- **Coste = instancias protegidas + almacenamiento + snapshots.** La política Enhanced añade coste de snapshots, pero es la única opción para Trusted Launch con todas las funciones.

## Decisiones de diseño

| Decisión | Lo que aplico | Por qué |
|---|---|---|
| Redundancia | `GeoRedundant` en producción; LRS en dev/test | Copia fuera de la región principal |
| Cross Region Restore | Desactivado por defecto | Irreversible, con recargo e incompatible con acceso público denegado |
| Soft delete | No se declara en Terraform (lo fuerza Azure); 14 días en Bicep, configurable | `soft_delete_enabled` está obsoleto en azurerm 4.x |
| Inmutabilidad | `Unlocked` por defecto; `Locked` como decisión explícita por entorno | Lo reversible primero, lo irreversible cuando la retención está validada |
| MUA | Asociación con un Resource Guard que gestiona seguridad | Las operaciones críticas no dependen de un solo administrador |
| Red | `public_network_access_enabled = false` y Private Endpoint `AzureBackup` (experiencia v2) con las tres zonas | Sin tráfico público; v2 no necesita identidad gestionada |
| Identidad | Identidad del sistema siempre; CMK con identidad de usuario | El permiso sobre la clave tiene que existir antes de asociarla |
| Alertas | Alertas de Azure Monitor activadas, clásicas desactivadas; regla de procesamiento hacia un action group | Sin duplicados y con destinatarios explícitos |
| Diagnósticos | Seis categorías de Azure Backup en tablas dedicadas; ASR en otro diagnostic setting opcional | Los informes de Backup solo leen las tablas dedicadas |
| Políticas | VM **Enhanced** cada 4 horas y diaria, Azure Files diaria; RG de snapshots con nombre propio | Trusted Launch y RPO bajo; snapshots en un RG gobernado |
| Protección de elementos | Fuera de esta ficha: va con cada carga (`azurerm_backup_protected_vm`, `_file_share`) | El ciclo de vida de la VM manda |

Alineación con el Well-Architected Framework:

- **Seguridad**: soft delete, inmutabilidad, MUA, red privada y CMK opcional.
- **Fiabilidad**: GRS y, si se pide, Cross Region Restore; políticas Enhanced con snapshots resistentes a zona.
- **Coste**: redundancia por entorno, retenciones justificadas y archivo para puntos mensuales y anuales.
- **Excelencia operativa**: almacén, políticas, alertas y diagnósticos en IaC; informes de Backup sobre tablas dedicadas.
- **Rendimiento**: Instant Restore para restauraciones rápidas desde snapshot.

## Módulo de Terraform

### Los módulos del repositorio

| Pieza | Módulo | Estado |
|---|---|---|
| Almacén | [`BackupAndUpdate/RecoveryServicesVault`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/BackupAndUpdate/RecoveryServicesVault) | Utilizable con condiciones; **le faltan piezas de seguridad** |
| Política de VMs | [`BackupAndUpdate/BackupPolicyVM`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/BackupAndUpdate/BackupPolicyVM) | Utilizable |
| Política de Azure Files | [`BackupAndUpdate/BackupPolicyFileShare`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/BackupAndUpdate/BackupPolicyFileShare) | Utilizable con condiciones |
| Protección de VMs y shares | [`BackupProtectedVM`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/BackupAndUpdate/BackupProtectedVM), [`BackupProtectedFileShare`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/BackupAndUpdate/BackupProtectedFileShare) | Se usan desde el proyecto de cada carga |

**`RecoveryServicesVault`**:

- Usa `locals` y `count`.
- Valores por defecto inseguros: `public_network_access_enabled = true` e `immutability = "Disabled"`.
- Declara `soft_delete_enabled`, obsoleto en azurerm 4.x y que desaparece en 5.0. Con `false` el `plan` falla con *"Soft Delete is a required security feature and cannot be disabled"*.
- Su `versions.tf` admite azurerm desde 3.70.0. Con versiones anteriores a 4.64.0, el provider intenta modificar el soft delete de almacenes en *AlwaysON*.
- El bloque `monitoring` solo expone dos opciones, y `alerts_for_critical_operation_failures_enabled` (alertas **clásicas**, retiradas) vale `true` por defecto. No expone las alertas de failover ni de replicación de ASR.
- Diagnósticos: un único diagnostic setting sin `log_analytics_destination_type`. Mezcla categorías de tablas dedicadas con `AzureBackupReport` y `AzureSiteRecoveryEvents`, que solo funcionan en modo *AzureDiagnostics*, e incluye `AddonAzureBackupAlerts` (alertas clásicas, no recomendada). Con un solo modo, unas u otras categorías no llegan a los informes de Backup. Además usa el bloque `metric`, que se elimina en azurerm 5.0.
- No crea Private Endpoint, ni asociación con Resource Guard (MUA), ni enrutado de alertas.

**`BackupPolicyVM`**:

- `instant_restore_retention_days = 2` por defecto: con frecuencia `Weekly` el provider exige 5.
- `instant_restore_resource_group.prefix` es opcional en el módulo, pero obligatorio en el provider.
- No expone `consistency_type`.

**`BackupPolicyFileShare`** no expone `backup_tier` ni `snapshot_retention_in_days`, así que solo crea políticas de *snapshot* (sin copia al almacén).

En la ficha, el almacén va con recursos nativos y las políticas se llaman a los módulos del repositorio.

### Estructura en el proyecto

```txt
/
├── providers.tf
├── recovery_services_vaults.tf  # almacén, PE, MUA, alertas y diagnósticos
├── backup_policies.tf           # políticas con los módulos del repositorio
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
      # 4.64.0: deja de intentar cambiar el soft delete de almacenes en AlwaysON (secure by default).
      # < 5.0.0: restricción de los módulos de AzureTerraformModules.
      version = ">= 4.64.0, < 5.0.0"
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

### Almacén · `recovery_services_vaults.tf`

```hcl
# =============================================================================
# Recovery Services vault: redundancia, inmutabilidad, alertas de Azure Monitor,
# Private Endpoint, MUA con Resource Guard y diagnósticos en tablas dedicadas
# DEPENDENCY: Resource Group existente
# DEPENDENCY: Proveedor Microsoft.RecoveryServices registrado en la suscripción
# DEPENDENCY: Subnet de Private Endpoints con al menos una /25 libre
# DEPENDENCY: Zonas privadas privatelink.<geo>.backup.windowsazure.com,
#             privatelink.blob.core.windows.net y privatelink.queue.core.windows.net,
#             enlazadas a la VNet de las cargas protegidas
# DEPENDENCY: Resource Guard creado por el equipo de seguridad (misma región, otra
#             suscripción o tenant) y rol Reader sobre él para la identidad de Terraform
# DEPENDENCY: CMK opcional: Key Vault con soft delete y purge protection, identidad
#             de usuario con Key Vault Crypto Service Encryption User sobre la clave
# =============================================================================

variable "recovery_services_vaults" {
  description = "Recovery Services vaults (clave = nombre del almacén)."
  type = map(object({
    resource_group_name = string
    location            = string # la misma región que las cargas que protege

    sku = optional(string, "Standard") # Standard | RS0 (no afecta a la redundancia)

    # Redundancia del almacenamiento de backup: solo se puede cambiar antes de proteger elementos
    storage_mode_type            = optional(string, "GeoRedundant") # GeoRedundant | ZoneRedundant | LocallyRedundant
    cross_region_restore_enabled = optional(bool, false)            # solo GRS; no se puede desactivar sin recrear

    # Inmutabilidad: Unlocked es reversible; Locked es irreversible (decisión explícita)
    immutability = optional(string, "Unlocked") # Disabled | Unlocked | Locked

    public_network_access_enabled      = optional(bool, false)
    classic_vmware_replication_enabled = optional(bool, false)

    # Identidad gestionada: necesaria para CMK; una vez activada no se debe desactivar
    identity = optional(object({
      type         = optional(string, "SystemAssigned") # SystemAssigned | UserAssigned | "SystemAssigned, UserAssigned"
      identity_ids = optional(list(string), [])
    }), {})

    # CMK: solo en almacenes sin elementos protegidos; no se puede desactivar después.
    # Con identidad de usuario, porque el permiso sobre la clave debe existir antes de asociarla.
    encryption = optional(object({
      key_id                            = string
      infrastructure_encryption_enabled = bool   # inmutable: decisión explícita
      user_assigned_identity_id         = string # también en identity.identity_ids
    }))

    # Alertas integradas de Azure Monitor sí; alertas clásicas (retiradas) no
    monitoring = optional(object({
      alerts_for_all_job_failures_enabled            = optional(bool, true)
      alerts_for_all_failover_issues_enabled         = optional(bool, true)
      alerts_for_all_replication_issues_enabled      = optional(bool, true)
      alerts_for_critical_operation_failures_enabled = optional(bool, false) # clásicas
      email_notifications_for_site_recovery_enabled  = optional(bool, false) # clásicas
    }), {})

    # Private Endpoints de Azure Backup (subrecurso AzureBackup); crearlos ANTES de proteger nada
    private_endpoints = optional(map(object({
      subnet_id            = string
      private_dns_zone_ids = list(string) # backup, blob y queue
      location             = optional(string)
      resource_group_name  = optional(string)
    })), {})

    # Multi-user authorization: Resource Guard gestionado por seguridad
    resource_guard_id = optional(string)

    # Notificaciones de las alertas integradas
    action_group_ids = optional(list(string), [])

    log_analytics_workspace_id = string
    site_recovery_diagnostics  = optional(bool, false) # true si el almacén se usa también para ASR

    tags = optional(map(string), {})
  }))
  default = {}

  validation {
    condition     = alltrue([for k, v in var.recovery_services_vaults : can(regex("^[A-Za-z][A-Za-z0-9-]{1,49}$", k))])
    error_message = "Nombre del almacén: 2-50 caracteres, empieza por letra; solo letras, números y guiones."
  }

  validation {
    condition = alltrue([
      for k, v in var.recovery_services_vaults :
      contains(["GeoRedundant", "ZoneRedundant", "LocallyRedundant"], v.storage_mode_type)
    ])
    error_message = "storage_mode_type debe ser GeoRedundant, ZoneRedundant o LocallyRedundant."
  }

  validation {
    condition = alltrue([
      for k, v in var.recovery_services_vaults :
      !v.cross_region_restore_enabled || v.storage_mode_type == "GeoRedundant"
    ])
    error_message = "Cross Region Restore solo está disponible con storage_mode_type = GeoRedundant."
  }

  validation {
    condition = alltrue([
      for k, v in var.recovery_services_vaults :
      !v.cross_region_restore_enabled || v.public_network_access_enabled
    ])
    error_message = "Cross Region Restore no está soportado con el acceso público denegado."
  }

  validation {
    condition     = alltrue([for k, v in var.recovery_services_vaults : contains(["Disabled", "Unlocked", "Locked"], v.immutability)])
    error_message = "immutability debe ser Disabled, Unlocked o Locked."
  }

  validation {
    condition     = alltrue([for k, v in var.recovery_services_vaults : length(v.private_endpoints) <= 12])
    error_message = "Un almacén admite como máximo 12 Private Endpoints."
  }

  validation {
    condition = alltrue([
      for k, v in var.recovery_services_vaults :
      v.encryption == null || contains(v.identity.identity_ids, try(v.encryption.user_assigned_identity_id, ""))
    ])
    error_message = "La identidad de usuario de CMK debe estar también en identity.identity_ids."
  }
}

resource "azurerm_recovery_services_vault" "this" {
  for_each            = var.recovery_services_vaults
  name                = each.key
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  sku                 = each.value.sku

  storage_mode_type            = each.value.storage_mode_type
  cross_region_restore_enabled = each.value.cross_region_restore_enabled
  immutability                 = each.value.immutability

  public_network_access_enabled      = each.value.public_network_access_enabled
  classic_vmware_replication_enabled = each.value.classic_vmware_replication_enabled
  # soft_delete_enabled no se declara: obsoleto en azurerm 4.x y el soft delete ya es obligatorio

  identity {
    type         = each.value.identity.type
    identity_ids = each.value.identity.type == "SystemAssigned" ? null : each.value.identity.identity_ids
  }

  dynamic "encryption" {
    for_each = each.value.encryption != null ? [each.value.encryption] : []
    content {
      key_id                            = encryption.value.key_id
      infrastructure_encryption_enabled = encryption.value.infrastructure_encryption_enabled
      use_system_assigned_identity      = false
      user_assigned_identity_id         = encryption.value.user_assigned_identity_id
    }
  }

  monitoring {
    alerts_for_all_job_failures_enabled            = each.value.monitoring.alerts_for_all_job_failures_enabled
    alerts_for_all_failover_issues_enabled         = each.value.monitoring.alerts_for_all_failover_issues_enabled
    alerts_for_all_replication_issues_enabled      = each.value.monitoring.alerts_for_all_replication_issues_enabled
    alerts_for_critical_operation_failures_enabled = each.value.monitoring.alerts_for_critical_operation_failures_enabled
    email_notifications_for_site_recovery_enabled  = each.value.monitoring.email_notifications_for_site_recovery_enabled
  }

  tags = merge(var.tags, each.value.tags)
}

# Private Endpoints de Azure Backup (experiencia v2: sin identidad gestionada ni PEs de blob/queue propios)
resource "azurerm_private_endpoint" "rsv" {
  for_each = {
    for item in flatten([
      for vk, v in var.recovery_services_vaults : [
        for pk, pe in v.private_endpoints : {
          key                 = "${vk}/${pk}"
          vault               = vk
          name                = "pe-${vk}-${pk}"
          subnet_id           = pe.subnet_id
          dns_zone_ids        = pe.private_dns_zone_ids
          location            = coalesce(pe.location, v.location)
          resource_group_name = coalesce(pe.resource_group_name, v.resource_group_name)
          tags                = v.tags
        }
      ]
    ]) : item.key => item
  }

  name                = each.value.name
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  subnet_id           = each.value.subnet_id

  private_service_connection {
    name                           = "psc-${each.value.name}"
    private_connection_resource_id = azurerm_recovery_services_vault.this[each.value.vault].id
    subresource_names              = ["AzureBackup"]
    is_manual_connection           = false
  }

  private_dns_zone_group {
    name                 = "default"
    private_dns_zone_ids = each.value.dns_zone_ids
  }

  tags = merge(var.tags, each.value.tags)
}

# Multi-user authorization: las operaciones críticas exigen permiso sobre el Resource Guard
resource "azurerm_recovery_services_vault_resource_guard_association" "this" {
  for_each          = { for k, v in var.recovery_services_vaults : k => v if v.resource_guard_id != null }
  vault_id          = azurerm_recovery_services_vault.this[each.key].id
  resource_guard_id = each.value.resource_guard_id
}

# Azure Backup: las seis categorías de informes en tablas dedicadas (resource-specific)
resource "azurerm_monitor_diagnostic_setting" "rsv_backup" {
  for_each                       = var.recovery_services_vaults
  name                           = "diag-${each.key}-backup"
  target_resource_id             = azurerm_recovery_services_vault.this[each.key].id
  log_analytics_workspace_id     = each.value.log_analytics_workspace_id
  log_analytics_destination_type = "Dedicated"

  dynamic "enabled_log" {
    for_each = toset([
      "CoreAzureBackup",
      "AddonAzureBackupJobs",
      "AddonAzureBackupPolicy",
      "AddonAzureBackupStorage",
      "AddonAzureBackupProtectedInstance",
      "AzureBackupOperations",
    ])
    content {
      category = enabled_log.value
    }
  }
}

# Azure Site Recovery: tablas dedicadas de trabajos y elementos replicados
resource "azurerm_monitor_diagnostic_setting" "rsv_site_recovery" {
  for_each                       = { for k, v in var.recovery_services_vaults : k => v if v.site_recovery_diagnostics }
  name                           = "diag-${each.key}-asr"
  target_resource_id             = azurerm_recovery_services_vault.this[each.key].id
  log_analytics_workspace_id     = each.value.log_analytics_workspace_id
  log_analytics_destination_type = "Dedicated"

  enabled_log {
    category = "AzureSiteRecoveryJobs"
  }
  enabled_log {
    category = "ASRReplicatedItems"
  }
}

# Notificaciones de las alertas integradas (se generan siempre; esto decide a quién avisar)
resource "azurerm_monitor_alert_processing_rule_action_group" "rsv" {
  for_each             = { for k, v in var.recovery_services_vaults : k => v if length(v.action_group_ids) > 0 }
  name                 = "apr-${each.key}"
  resource_group_name  = each.value.resource_group_name
  scopes               = [azurerm_recovery_services_vault.this[each.key].id]
  add_action_group_ids = each.value.action_group_ids
  description          = "Envía las alertas integradas de Azure Backup del almacén ${each.key}."
  tags                 = merge(var.tags, each.value.tags)
}

output "recovery_services_vault_ids" {
  description = "IDs de los almacenes."
  value       = { for k, v in azurerm_recovery_services_vault.this : k => v.id }
}

output "recovery_services_vault_principal_ids" {
  description = "Object ID de la identidad del sistema (permisos de CMK)."
  value       = { for k, v in azurerm_recovery_services_vault.this : k => try(v.identity[0].principal_id, null) }
}
```

### Políticas · `backup_policies.tf`

```hcl
# =============================================================================
# Políticas de partida del almacén: VM (Enhanced) y Azure Files
# DEPENDENCY: azurerm_recovery_services_vault.this (recovery_services_vaults.tf)
# La protección de cada VM o share (azurerm_backup_protected_vm / _file_share) va con la carga
# =============================================================================

variable "backup_policies_vm" {
  description = "Políticas de backup de VMs (clave = nombre de la política)."
  type = map(object({
    vault       = string                # clave de var.recovery_services_vaults
    policy_type = optional(string, "V2") # V2 = Enhanced; obligatoria para Trusted Launch, Premium SSD v2 y Ultra
    timezone    = string                # p. ej. "Romance Standard Time"

    backup = object({
      frequency     = string # Hourly (solo V2) | Daily | Weekly
      time          = optional(string, "23:00")
      hour_interval = optional(number) # 4, 6, 8 o 12
      hour_duration = optional(number) # múltiplo de hour_interval, 4-24
      weekdays      = optional(list(string))
    })

    instant_restore_retention_days = optional(number, 7) # V1: 1-5 (5 con Weekly); V2: 1-30
    instant_restore_rg_prefix      = string              # RG de los snapshots: no dejar el nombre por defecto

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
  }))
  default = {}

  validation {
    condition     = alltrue([for k, v in var.backup_policies_vm : v.backup.frequency != "Hourly" || v.policy_type == "V2"])
    error_message = "La frecuencia Hourly solo existe en la política Enhanced (V2)."
  }

  validation {
    condition = alltrue([
      for k, v in var.backup_policies_vm :
      v.policy_type == "V2" ? v.instant_restore_retention_days >= 1 && v.instant_restore_retention_days <= 30 : v.instant_restore_retention_days >= 1 && v.instant_restore_retention_days <= 5
    ])
    error_message = "Instant Restore: 1-5 días en V1 y 1-30 días en V2."
  }

  validation {
    condition     = alltrue([for k, v in var.backup_policies_vm : v.backup.frequency != "Weekly" || v.instant_restore_retention_days == 5])
    error_message = "Con frecuencia Weekly, instant_restore_retention_days debe ser 5."
  }
}

variable "backup_policies_file_share" {
  description = "Políticas de backup de Azure Files (clave = nombre de la política)."
  type = map(object({
    vault    = string
    timezone = string
    backup = object({
      frequency = string # Daily | Hourly
      time      = optional(string, "23:00")
      hourly = optional(object({
        interval        = number
        start_time      = string
        window_duration = number
      }))
    })
    retention_daily = optional(number, 30) # 1-200 (límite de 200 snapshots por share)
    retention_weekly = optional(object({
      count    = number
      weekdays = list(string)
    }))
  }))
  default = {}
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
}

module "backup_policy_file_share" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//BackupAndUpdate/BackupPolicyFileShare?ref=main"
  for_each = var.backup_policies_file_share

  name                = each.key
  resource_group_name = azurerm_recovery_services_vault.this[each.value.vault].resource_group_name
  recovery_vault_name = azurerm_recovery_services_vault.this[each.value.vault].name

  timezone         = each.value.timezone
  backup           = each.value.backup
  retention_daily  = each.value.retention_daily
  retention_weekly = each.value.retention_weekly
}

output "backup_policy_ids" {
  description = "IDs de las políticas (para azurerm_backup_protected_vm / _file_share)."
  value = merge(
    { for k, m in module.backup_policy_vm : k => m.id },
    { for k, m in module.backup_policy_file_share : k => m.id },
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

recovery_services_vaults = {
  "rsv-<workload>-pro-<region>-01" = {
    resource_group_name = "<rg-backup-pro>"
    location            = "<region>"

    storage_mode_type            = "GeoRedundant"
    cross_region_restore_enabled = false # true exige acceso público; ver la ficha
    immutability                 = "Unlocked" # pasar a "Locked" tras validar retenciones

    public_network_access_enabled = false

    private_endpoints = {
      hub = {
        subnet_id = "<resourceId snet-privateendpoints>"
        private_dns_zone_ids = [
          "<resourceId privatelink.<geo>.backup.windowsazure.com>",
          "<resourceId privatelink.blob.core.windows.net>",
          "<resourceId privatelink.queue.core.windows.net>",
        ]
      }
    }

    resource_guard_id = "<resourceId Resource Guard en la suscripción de seguridad>"
    action_group_ids  = ["<resourceId action group de operaciones>"]

    log_analytics_workspace_id = "<resourceId log-analytics-workspace>"
  }
}

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

  "bkpol-vm-daily" = {
    vault       = "rsv-<workload>-pro-<region>-01"
    policy_type = "V2"
    timezone    = "<zona horaria Windows>"

    backup = {
      frequency = "Daily"
      time      = "23:00"
    }

    instant_restore_retention_days = 7
    instant_restore_rg_prefix      = "rg-<workload>-pro-bkp-snapshots-"
    retention_daily                = 30
  }
}

backup_policies_file_share = {
  "bkpol-files-daily" = {
    vault    = "rsv-<workload>-pro-<region>-01"
    timezone = "<zona horaria Windows>"
    backup = {
      frequency = "Daily"
      time      = "22:00"
    }
    retention_daily = 30
    retention_weekly = {
      count    = 12
      weekdays = ["Sunday"]
    }
  }
}
```

En `dev.tfvars`: `storage_mode_type = "LocallyRedundant"`, `immutability = "Unlocked"`, sin `resource_guard_id` y retenciones cortas.

### Orden de despliegue

1. **Almacén y Private Endpoint** en el mismo `apply`, antes de que ningún proyecto proteja nada en él.
2. **Comprobar la resolución DNS** desde la VNet de las cargas (debe devolver IPs privadas).
3. **Proteger las cargas** desde sus proyectos con `backup_policy_ids`.
4. **Bloquear la inmutabilidad** (`immutability = "Locked"`) cuando las retenciones estén validadas.

```powershell
terraform init
terraform plan -var-file="env/pro.tfvars" -out="pro.tfplan"
terraform apply "pro.tfplan"

# Comprobaciones
$vault = Get-AzRecoveryServicesVault -ResourceGroupName "<rg-backup-pro>" -Name "rsv-<workload>-pro-<region>-01"
Get-AzRecoveryServicesBackupProperty -Vault $vault
Get-AzPrivateEndpointConnection -PrivateLinkResourceId $vault.ID | Select-Object Name, PrivateLinkServiceConnectionState
Resolve-DnsName "<id-del-almacen>.<servicio>.privatelink.<geo>.backup.windowsazure.com"
```

### Equivalente en Bicep

`main.bicep` (a diferencia de azurerm, permite fijar la retención del soft delete):

```bicep
// =============================================================================
// Recovery Services vault: redundancia, soft delete, inmutabilidad, alertas de Azure Monitor,
// Private Endpoint, MUA con Resource Guard, diagnósticos y políticas de partida
// DEPENDENCY: Resource Group existente (targetScope = resourceGroup)
// DEPENDENCY: Subnet de Private Endpoints (/25 libre) y zonas privadas de backup, blob y queue
// DEPENDENCY: Resource Guard del equipo de seguridad (misma región) y Reader sobre él
// =============================================================================
targetScope = 'resourceGroup'

param location string = resourceGroup().location

@minLength(2)
@maxLength(50)
param vaultName string

@allowed(['GeoRedundant', 'ZoneRedundant', 'LocallyRedundant'])
param storageRedundancy string = 'GeoRedundant'

@description('Solo con GeoRedundant y acceso público habilitado. No se puede desactivar.')
param crossRegionRestore bool = false

@description('Unlocked es reversible; Locked es irreversible.')
@allowed(['Disabled', 'Unlocked', 'Locked'])
param immutabilityState string = 'Unlocked'

@minValue(14)
@maxValue(180)
param softDeleteRetentionDays int = 14

param publicNetworkAccess bool = false

param privateEndpointSubnetId string

@description('IDs de las zonas privadas de backup (<geo>), blob y queue.')
param privateDnsZoneIds array

param resourceGuardId string = ''
param actionGroupIds array = []
param logAnalyticsWorkspaceId string
param siteRecoveryDiagnostics bool = false

@description('Zona horaria Windows de las políticas, p. ej. Romance Standard Time.')
param policyTimeZone string

@description('Hora de inicio de las políticas, HH:mm.')
param backupTime string = '23:00'

param snapshotResourceGroupPrefix string

param tags object = {}

// Las horas de las políticas se expresan como fecha y hora; solo cuenta la hora
var scheduleTime = '2026-01-01T${backupTime}:00Z'

var backupLogCategories = [
  'CoreAzureBackup'
  'AddonAzureBackupJobs'
  'AddonAzureBackupPolicy'
  'AddonAzureBackupStorage'
  'AddonAzureBackupProtectedInstance'
  'AzureBackupOperations'
]

resource vault 'Microsoft.RecoveryServices/vaults@2025-02-01' = {
  name: vaultName
  location: location
  tags: tags
  sku: {
    name: 'RS0'
    tier: 'Standard'
  }
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    publicNetworkAccess: publicNetworkAccess ? 'Enabled' : 'Disabled'
    redundancySettings: {
      standardTierStorageRedundancy: storageRedundancy
      crossRegionRestore: crossRegionRestore ? 'Enabled' : 'Disabled'
    }
    securitySettings: {
      softDeleteSettings: {
        softDeleteState: 'AlwaysON'
        softDeleteRetentionPeriodInDays: softDeleteRetentionDays
        enhancedSecurityState: 'AlwaysON'
      }
      immutabilitySettings: {
        state: immutabilityState
      }
    }
    monitoringSettings: {
      azureMonitorAlertSettings: {
        alertsForAllJobFailures: 'Enabled'
        alertsForAllFailoverIssues: 'Enabled'
        alertsForAllReplicationIssues: 'Enabled'
      }
      classicAlertSettings: {
        alertsForCriticalOperations: 'Disabled'
        emailNotificationsForSiteRecovery: 'Disabled'
      }
    }
  }
}

resource privateEndpoint 'Microsoft.Network/privateEndpoints@2024-05-01' = {
  name: 'pe-${vaultName}-backup'
  location: location
  tags: tags
  properties: {
    subnet: {
      id: privateEndpointSubnetId
    }
    privateLinkServiceConnections: [
      {
        name: 'psc-${vaultName}-backup'
        properties: {
          privateLinkServiceId: vault.id
          groupIds: [
            'AzureBackup'
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
      for (zoneId, i) in privateDnsZoneIds: {
        name: 'zone-${i}'
        properties: {
          privateDnsZoneId: zoneId
        }
      }
    ]
  }
}

resource resourceGuardProxy 'Microsoft.RecoveryServices/vaults/backupResourceGuardProxies@2025-02-01' = if (!empty(resourceGuardId)) {
  parent: vault
  name: 'VaultProxy'
  properties: {
    resourceGuardResourceId: resourceGuardId
  }
}

resource diagnosticsBackup 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = {
  name: 'diag-${vaultName}-backup'
  scope: vault
  properties: {
    workspaceId: logAnalyticsWorkspaceId
    logAnalyticsDestinationType: 'Dedicated'
    logs: [
      for category in backupLogCategories: {
        category: category
        enabled: true
      }
    ]
  }
}

resource diagnosticsSiteRecovery 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = if (siteRecoveryDiagnostics) {
  name: 'diag-${vaultName}-asr'
  scope: vault
  properties: {
    workspaceId: logAnalyticsWorkspaceId
    logAnalyticsDestinationType: 'Dedicated'
    logs: [
      { category: 'AzureSiteRecoveryJobs', enabled: true }
      { category: 'ASRReplicatedItems', enabled: true }
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

// Política Enhanced de VMs: cada 4 horas, 7 días de snapshots
resource policyVmEnhanced 'Microsoft.RecoveryServices/vaults/backupPolicies@2025-02-01' = {
  parent: vault
  name: 'bkpol-vm-enhanced-4h'
  properties: {
    backupManagementType: 'AzureIaasVM'
    policyType: 'V2'
    timeZone: policyTimeZone
    instantRpRetentionRangeInDays: 7
    instantRPDetails: {
      azureBackupRGNamePrefix: snapshotResourceGroupPrefix
    }
    schedulePolicy: {
      schedulePolicyType: 'SimpleSchedulePolicyV2'
      scheduleRunFrequency: 'Hourly'
      hourlySchedule: {
        interval: 4
        scheduleWindowStartTime: scheduleTime
        scheduleWindowDuration: 24
      }
    }
    retentionPolicy: {
      retentionPolicyType: 'LongTermRetentionPolicy'
      dailySchedule: {
        retentionTimes: [
          scheduleTime
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
          scheduleTime
        ]
        retentionDuration: {
          count: 12
          durationType: 'Weeks'
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
          scheduleTime
        ]
        retentionDuration: {
          count: 12
          durationType: 'Months'
        }
      }
    }
  }
}

// Política de Azure Files: diaria, 30 días
resource policyFiles 'Microsoft.RecoveryServices/vaults/backupPolicies@2025-02-01' = {
  parent: vault
  name: 'bkpol-files-daily'
  properties: {
    backupManagementType: 'AzureStorage'
    workLoadType: 'AzureFileShare'
    timeZone: policyTimeZone
    schedulePolicy: {
      schedulePolicyType: 'SimpleSchedulePolicy'
      scheduleRunFrequency: 'Daily'
      scheduleRunTimes: [
        scheduleTime
      ]
    }
    retentionPolicy: {
      retentionPolicyType: 'LongTermRetentionPolicy'
      dailySchedule: {
        retentionTimes: [
          scheduleTime
        ]
        retentionDuration: {
          count: 30
          durationType: 'Days'
        }
      }
    }
  }
}

output vaultId string = vault.id
output vaultPrincipalId string = vault.identity.principalId
output vmPolicyId string = policyVmEnhanced.id
output filesPolicyId string = policyFiles.id
```

`main.pro.bicepparam`:

```bicep
using 'main.bicep'

param vaultName = 'rsv-<workload>-pro-<region>-01'
param storageRedundancy = 'GeoRedundant'
param crossRegionRestore = false
param immutabilityState = 'Unlocked'
param softDeleteRetentionDays = 14
param publicNetworkAccess = false

param privateEndpointSubnetId = '<resourceId snet-privateendpoints>'
param privateDnsZoneIds = [
  '<resourceId privatelink.<geo>.backup.windowsazure.com>'
  '<resourceId privatelink.blob.core.windows.net>'
  '<resourceId privatelink.queue.core.windows.net>'
]

param resourceGuardId = '<resourceId Resource Guard en la suscripción de seguridad>'
param actionGroupIds = [
  '<resourceId action group de operaciones>'
]
param logAnalyticsWorkspaceId = '<resourceId log-analytics-workspace>'

param policyTimeZone = '<zona horaria Windows, p. ej. Romance Standard Time>'
param backupTime = '23:00'
param snapshotResourceGroupPrefix = 'rg-<workload>-pro-bkp-snapshots-'

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
| *"Soft Delete is a required security feature and cannot be disabled"* en el `plan` | `soft_delete_enabled = false` | Quitar el argumento |
| No se puede cambiar la redundancia del almacén | Ya hay backups configurados | Decidirla antes; si no, almacén nuevo |
| No se puede crear el Private Endpoint | El almacén ya registró o intentó proteger elementos | Crear un almacén nuevo con PE desde el principio |
| Backups correctos pero las restauraciones fallan (salvo VM completa) | Acceso público denegado sin Private Endpoint | Crear el PE o permitir el acceso público |
| Backup de SQL/HANA o MARS falla tras el primer backup con DNS propio | Faltan registros de blob y queue | Zonas privadas de Azure o reenviadores condicionales a 168.63.129.16 |
| Cross Region Restore no disponible | Acceso público denegado, o almacén LRS/ZRS | Requiere GRS y acceso público |
| No se puede reducir la retención de una política | Inmutabilidad activada | Esperado; con `Unlocked`, desactivar temporalmente; con `Locked`, no es posible |
| No se puede borrar el almacén | Elementos aún protegidos, servidores o cuentas registrados, replicación de ASR o PEs | Parar la protección (los datos pasan a soft delete) y limpiar dependencias; con inmutabilidad bloqueada, solo soporte. El almacén borrado queda en soft delete |
| Operación crítica rechazada en un almacén con MUA | Falta permiso sobre el Resource Guard | Pedir *Backup MUA Operator* temporal (PIM) al equipo de seguridad |
| No se puede activar CMK | El almacén ya tiene elementos protegidos o intentados | CMK solo en almacenes nuevos |
| El backup MARS falla en un almacén con CMK | MARS no soporta almacenes cifrados con CMK | Almacén separado sin CMK para MARS |
| Alertas duplicadas | Alertas clásicas y de Azure Monitor a la vez | `alerts_for_critical_operation_failures_enabled = false` |
| Los informes de Backup salen vacíos | Categorías enviadas en modo *AzureDiagnostics* | `log_analytics_destination_type = "Dedicated"` |
| No se puede proteger una VM Trusted Launch desde el portal con política Standard | La Standard solo la admite por CLI, PowerShell o REST recientes | Política Enhanced |
| `instant_restore_retention_days` rechazado con frecuencia Weekly | El provider exige 5 días | Ajustar a 5 |
| Error al crear o editar políticas por automatización | Más de 50 cambios de políticas en 24 horas | Agrupar cambios |
| Error al actualizar un almacén existente con azurerm < 4.64.0 | El provider intenta cambiar el soft delete de un almacén *AlwaysON* | Subir a 4.64.0 o posterior |
