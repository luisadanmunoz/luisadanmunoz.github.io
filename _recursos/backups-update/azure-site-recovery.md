---
title: "Azure Site Recovery"
indice: backups-update
resumen: "Réplica de cargas a otra región ante desastres."
estado: documentado   # proximamente | en-curso | documentado
orden: 4
last_review: 2026-10-20
fuentes:
  - titulo: "About Site Recovery"
    url: https://learn.microsoft.com/azure/site-recovery/site-recovery-overview
  - titulo: "Azure to Azure disaster recovery architecture"
    url: https://learn.microsoft.com/azure/site-recovery/azure-to-azure-architecture
  - titulo: "Support matrix for Azure VM disaster recovery between Azure regions"
    url: https://learn.microsoft.com/azure/site-recovery/azure-to-azure-support-matrix
  - titulo: "Tutorial: Set up disaster recovery for Azure VMs"
    url: https://learn.microsoft.com/azure/site-recovery/azure-to-azure-tutorial-enable-replication
  - titulo: "Common questions about Azure-to-Azure disaster recovery"
    url: https://learn.microsoft.com/azure/site-recovery/azure-to-azure-common-questions
  - titulo: "About networking in Azure virtual machine disaster recovery"
    url: https://learn.microsoft.com/azure/site-recovery/azure-to-azure-about-networking
  - titulo: "Replicate machines with private endpoints in Azure Site Recovery"
    url: https://learn.microsoft.com/azure/site-recovery/azure-to-azure-how-to-enable-replication-private-endpoints
  - titulo: "Azure Private Endpoint private DNS zone values"
    url: https://learn.microsoft.com/azure/private-link/private-endpoint-dns
  - titulo: "Turn off key based access on cache account"
    url: https://learn.microsoft.com/azure/site-recovery/asr-turn-off-key-authentication-cache
  - titulo: "Azure Virtual Machines disaster recovery - High Churn support"
    url: https://learn.microsoft.com/azure/site-recovery/concepts-azure-to-azure-high-churn-support
  - titulo: "Enable Azure VM disaster recovery between availability zones"
    url: https://learn.microsoft.com/azure/site-recovery/azure-to-azure-how-to-enable-zone-to-zone-disaster-recovery
  - titulo: "Azure Site Recovery support for Azure trusted launch virtual machines"
    url: https://learn.microsoft.com/azure/site-recovery/concepts-trusted-vm
  - titulo: "Support for using Site Recovery with Azure Backup"
    url: https://learn.microsoft.com/azure/site-recovery/site-recovery-backup-interoperability
  - titulo: "About recovery plans"
    url: https://learn.microsoft.com/azure/site-recovery/recovery-plan-overview
  - titulo: "Create and customize recovery plans"
    url: https://learn.microsoft.com/azure/site-recovery/site-recovery-create-recovery-plans
  - titulo: "Tutorial: Run a disaster recovery drill for Azure VMs"
    url: https://learn.microsoft.com/azure/site-recovery/azure-to-azure-tutorial-dr-drill
  - titulo: "Run a test failover (disaster recovery drill) to Azure"
    url: https://learn.microsoft.com/azure/site-recovery/site-recovery-test-failover-to-azure
  - titulo: "Tutorial: Fail over Azure VMs to a secondary region"
    url: https://learn.microsoft.com/azure/site-recovery/azure-to-azure-tutorial-failover-failback
  - titulo: "Automatic update of the Mobility service in Azure-to-Azure replication"
    url: https://learn.microsoft.com/azure/site-recovery/azure-to-azure-autoupdate
  - titulo: "Migrate from a Run As account to Managed Identities"
    url: https://learn.microsoft.com/azure/site-recovery/how-to-migrate-run-as-accounts-managed-identity
  - titulo: "Use Azure Policy to set up Azure Site Recovery"
    url: https://learn.microsoft.com/azure/site-recovery/azure-to-azure-how-to-enable-policy
  - titulo: "Set up disaster recovery for Azure virtual machines using Azure PowerShell"
    url: https://learn.microsoft.com/azure/site-recovery/azure-to-azure-powershell
  - titulo: "Troubleshoot Azure-to-Azure VM network connectivity issues"
    url: https://learn.microsoft.com/azure/site-recovery/azure-to-azure-troubleshoot-network-connectivity
  - titulo: "Troubleshoot replication in Azure VM disaster recovery"
    url: https://learn.microsoft.com/azure/site-recovery/azure-to-azure-troubleshoot-replication
  - titulo: "Troubleshoot Azure-to-Azure VM replication errors"
    url: https://learn.microsoft.com/azure/site-recovery/azure-to-azure-troubleshoot-errors
  - titulo: "Use the Recovery Services dashboard (alertas integradas de ASR)"
    url: https://learn.microsoft.com/azure/site-recovery/site-recovery-monitor-and-troubleshoot
  - titulo: "Azure security baseline for Site Recovery"
    url: https://learn.microsoft.com/security/benchmark/azure/baselines/site-recovery-security-baseline
  - titulo: "On-demand Capacity Reservation"
    url: https://learn.microsoft.com/azure/virtual-machines/capacity-reservation-overview
  - titulo: "Azure Site Recovery pricing"
    url: https://azure.microsoft.com/pricing/details/site-recovery/
  - titulo: "Microsoft.RecoveryServices vaults/replicationFabrics/replicationProtectionContainers/replicationProtectedItems (plantillas ARM/Bicep)"
    url: https://learn.microsoft.com/azure/templates/microsoft.recoveryservices/vaults/replicationfabrics/replicationprotectioncontainers/replicationprotecteditems
  - titulo: "azurerm_site_recovery_replicated_vm"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/site_recovery_replicated_vm
  - titulo: "azurerm_site_recovery_protection_container_mapping"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/site_recovery_protection_container_mapping
  - titulo: "azurerm_site_recovery_replication_recovery_plan"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/site_recovery_replication_recovery_plan
  - titulo: "Módulo Terraform Migrate/SiteRecoveryFabric"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Migrate/SiteRecoveryFabric
  - titulo: "Módulo Terraform Migrate/SiteRecoveryProtectionContainer"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Migrate/SiteRecoveryProtectionContainer
  - titulo: "Módulo Terraform Migrate/SiteRecoveryReplicationPolicy"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Migrate/SiteRecoveryReplicationPolicy
  - titulo: "Módulo Terraform Migrate/SiteRecoveryNetworkMapping"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Migrate/SiteRecoveryNetworkMapping
---

**Azure Site Recovery** (ASR) mantiene una copia viva de tus VMs en otra región (o en otra zona de la misma región) y orquesta el arranque allí cuando la principal cae. No sustituye a las copias de seguridad:

- [Azure Backup](/recursos/backups-update/azure-backup/) responde a "necesito los datos de hace tres semanas".
- ASR responde a "la región no está disponible y necesito la aplicación funcionando en minutos u horas".

Usa un [Recovery Services vault](/recursos/backups-update/recovery-services-vault/), pero **no el mismo que el de backup**: el de backup va en la región de las VMs y el de ASR, fuera de ella.

## Qué es y cuándo usarlo

### Cómo funciona entre regiones

| Pieza | Dónde | Qué hace |
|---|---|---|
| **Extensión de movilidad** | En cada VM | Captura las escrituras de los discos y las envía a la caché |
| **Cuenta de caché** | Región de origen, misma suscripción que las VMs | Almacena los cambios antes de enviarlos a destino |
| **Discos de réplica** | Región de destino | Reciben los datos y los puntos de recuperación |
| **Recovery Services vault** | Cualquier región salvo la de origen (su grupo de recursos tampoco) | Orquestación y metadatos; no guarda datos de cliente |
| **Fabric / contenedor / mapeo** | Dentro del almacén | Representan cada región y qué política se usa entre ellas |
| **Plan de recuperación** | Dentro del almacén | Orden de arranque, scripts y acciones manuales |

La VM solo necesita **salida** hacia ASR; no hace falta ninguna conexión entrante.

### Entre regiones o entre zonas

| | Entre regiones | **Zone-to-zone** |
|---|---|---|
| Protege frente a | Caída de una región completa | Caída de una zona de disponibilidad |
| Almacén | Fuera de la región de origen | Puede estar en la misma región |
| Red | VNet propia en destino y mapeo de redes | Red de la misma región; el simulacro exige otra VNet |
| Grupo de recursos de destino | Distinto del de origen | **Obligatoriamente distinto** |
| No soportado | — | Discos ZRS y Ultra |
| Regiones | Cualquier par soportado | Solo regiones con zonas listadas por Microsoft (entre ellas Spain Central, West Europe, North Europe y Sweden Central) |

### Puntos de recuperación

| Tipo | Frecuencia | Detalle |
|---|---|---|
| **Crash-consistent** | Cada 5 minutos | No se puede cambiar; lo que estaba en memoria se pierde |
| **Coherente con la aplicación** | Desactivado por defecto; cada 1 hora como mínimo | VSS *copy-only* en Windows (no rompe la cadena de logs de SQL); afecta al rendimiento |
| Retención | Hasta 15 días con discos administrados | Más allá de las 2 últimas horas, ASR poda los puntos (1 cada 1-4 horas según la antigüedad) |

Al conmutar se elige el punto:

| Opción | RTO | RPO |
|---|---|---|
| *Latest processed* | Bajo: no procesa nada pendiente | El último punto ya procesado |
| *Latest* | Mayor: procesa todo lo recibido | **El más bajo** |
| *Latest app-consistent* | Bajo | El del último punto coherente con la aplicación |
| *Latest multi-VM* | — | Punto común a todas las VMs del grupo de replicación |

Los **grupos de replicación** (`multi_vm_group_name`) dan puntos comunes a varias VMs, pero penalizan el rendimiento: solo para aplicaciones que lo necesiten.

### Tasa de cambio (churn)

| Opción | Caché | Máximo por VM | Máximo por disco |
|---|---|---|---|
| Normal | Standard GPv2 | 54 MB/s | 20 MB/s |
| **High Churn** (VM con 32 GB de RAM o más) | Premium block blob | 100 MB/s | 50 MB/s |
| High Churn ampliado (256 GB de RAM o más, discos Premium SSD, Premium SSD v2 o Ultra) | Premium block blob | 500 MB/s | 250 MB/s según tamaño |

- **Premium SSD v2 y Ultra solo se replican con High Churn.**
- Los 500 MB/s solo existen entre regiones de una lista concreta: **Spain Central y Sweden Central no están**; West Europe y North Europe sí.
- Una cuenta de caché V2 admite unos 750 discos a 4 MB/s (375 a 8 MB/s).

### Red

Salida necesaria desde las VMs (HTTPS 443):

| Destino | URL | Service tag |
|---|---|---|
| Caché | `*.blob.core.windows.net` (o la cuenta concreta) | `Storage.<región de origen>` |
| Autenticación | `login.microsoftonline.com` | `AzureActiveDirectory` |
| Servicio ASR | `*.hypervrecoverymanager.windowsazure.com` | `AzureSiteRecovery` |
| Monitorización | `*.servicebus.windows.net` | `EventHub.<región de destino>` |
| VMs con ADE | `*.vault.azure.net` | `AzureKeyVault` |
| Actualización automática del agente | `*.automation.ext.azure.com` | `GuestAndHybridManagement` |

- **Las mismas reglas, invertidas, en la región de destino**: sin ellas no hay reprotección.
- Solo **proxys sin autenticación** (`ProxyInfo.conf`).
- Si la salida pasa por un NVA o un Azure Firewall, Microsoft recomienda un **endpoint de servicio de Storage** en las subredes para que la replicación no sature el appliance.

### Private Endpoints

- Solo en **almacenes nuevos sin nada registrado**: se crean **antes** de replicar.
- Subrecurso `AzureSiteRecovery` y zona `privatelink.siterecovery.windowsazure.com`. Los de Azure Backup no sirven para ASR.
- Uno en la red de origen y otro en la de recuperación. **Con hub & spoke y peering, uno solo** y una sola zona. Con dos, cada uno en su zona: reutilizar la zona sobrescribe los registros.
- **9 IPs** como mínimo en las subredes de origen y de recuperación, más 1 si la caché también usa Private Endpoint.
- El almacén necesita **identidad gestionada** con roles en la caché: *Contributor* + *Storage Blob Data Contributor* (Standard) o *Storage Blob Data Owner* (Premium), y la excepción de servicios de confianza.
- Entra ID no tiene Private Endpoint: la salida a `AzureActiveDirectory` sigue siendo obligatoria.
- **La actualización automática del agente con cuenta de Automation no funciona** con Private Endpoints.
- Con ExpressRoute, la replicación por *private peering* solo funciona con Private Endpoints.

### Compatibilidad que hay que revisar

| Elemento | Estado |
|---|---|
| Trusted Launch | Soportado con restricciones (en Linux, solo VMs creadas desde el 1 de abril de 2024) |
| Confidential VMs | No soportado |
| Extensiones de la VM | **No se replican**: hay que instalarlas tras el failover |
| RBAC de la VM | No se replica |
| Tags de la VM | Se replican |
| Azure Backup en la misma VM | Compatible; restaurar un disco o la VM obliga a desactivar y reactivar la réplica |
| Discos de réplica y de failover | Se crean **con acceso público** salvo que se configure lo contrario |
| Herramientas | Portal, PowerShell y REST. **Azure CLI no está soportada** |
| Mover almacén o recursos replicados de grupo de recursos | No soportado |

### Capacidad en destino

ASR crea las VMs en el momento del failover. Sin reserva, **la capacidad en la región de destino no está garantizada**. Para cargas críticas, **Capacity Reservation** (se paga aparte). No cubre todos los tamaños ni es compatible con conjuntos de disponibilidad, PPG, hosts dedicados, Spot ni discos Ultra.

### Azure Policy

La definición integrada *Configure disaster recovery on virtual machines by enabling replication via Azure Site Recovery* activa la réplica en las VMs nuevas de una suscripción o grupo de recursos, y en las existentes con remediación. **No sirve** con Private Endpoints, Azure Disk Encryption, discos con CMK, Premium SSD v2, Ultra, entre suscripciones ni con VMs apagadas. En un entorno con Private Endpoints, la protección va por IaC.

### Cómo se factura

| Concepto | Detalle |
|---|---|
| **Licencia por instancia protegida** | Los primeros 31 días de cada instancia son gratis |
| Discos de réplica | En la región de destino |
| Cuenta de caché | Almacenamiento y transacciones en origen |
| Tráfico entre regiones | Salida de datos (ASR comprime hasta un 50 %) |
| Snapshots | De los puntos de recuperación |
| Simulacros | Sin cuota de ASR, pero sí cómputo y almacenamiento mientras duran |
| Capacity Reservation | Opcional y aparte |

### Qué escenario recomiendo

| Escenario del cliente | Diseño | Por qué |
|---|---|---|
| Aplicación crítica que debe sobrevivir a la pérdida de la región | ASR entre regiones + plan de recuperación + Capacity Reservation | RTO y capacidad predecibles |
| Aplicación crítica solo frente a fallo de zona | Zone-to-zone | Sin latencia ni salida entre regiones |
| Servidores generales | ASR entre regiones sin reserva y con simulacros semestrales | Coste contenido |
| Bases de datos en VM con mucha escritura | High Churn + puntos coherentes con la aplicación cada 4 horas | Más ancho de banda de réplica |
| SQL Server con Always On | La réplica nativa de SQL en lugar de ASR para la base de datos | ASR se integra con Always On, pero no lo sustituye |
| Entorno con Private Endpoints e hub & spoke | Un PE de ASR en el hub, caché con firewall y sin clave | Todo el tráfico de control por red privada |
| PaaS (App Service, SQL Database, Storage) | Su redundancia geográfica propia | ASR es para VMs |

### Datos que conviene llevar a la reunión

- **ASR no es backup.** Replica también los errores y el ransomware; se necesitan los dos.
- **RPO de minutos** (crash-consistent cada 5 minutos) y **RTO que depende del plan de recuperación**: solo un simulacro lo mide.
- **Dos almacenes**: el de backup en la región de las VMs y el de ASR fuera de ella.
- **La capacidad en destino no está garantizada** sin Capacity Reservation.
- **Extensiones, RBAC y configuración de red no se replican**: el plan de recuperación debe recrearlas.
- **Los simulacros no afectan a producción** y solo cuestan el tiempo que están encendidos. Deben hacerse en una red aislada.
- **Licencia por VM protegida**, más discos en destino, caché y tráfico entre regiones.
- **Private Endpoints antes de replicar la primera VM**, o hay que empezar con un almacén nuevo.

## Decisiones de diseño

| Decisión | Lo que aplico | Por qué |
|---|---|---|
| Almacén | Uno dedicado a ASR, en la región de destino, con identidad SystemAssigned | Exigencia de región y acceso a la caché sin clave |
| Infraestructura | Fabrics, contenedores y política con los módulos del repositorio | Reutilizar lo que hay |
| Failback | Mapeo de contenedores y de redes de ida **y de vuelta** desde el principio | La reprotección no depende de nadie |
| Política | En `pro`, 24 horas de retención y puntos coherentes cada 4 horas | Equilibrio entre RPO, coste y rendimiento |
| Caché | Sin soft delete, sin clave de acceso, firewall con servicios de confianza y subredes de origen | Soportado por ASR y seguro por defecto |
| Private Endpoints | Antes que cualquier VM (`depends_on`) | Requisito del servicio |
| VMs | Mapa por VM con discos y NICs explícitos; red de simulacro separada | Nada implícito en el failover |
| Planes de recuperación | Grupos por capa (datos, aplicación, web) con acciones manuales o runbooks | Orden de arranque y RTO repetibles |
| Discos de réplica | Público abierto con Terraform (limitación del provider); `DenyAll` con Bicep | Ver el hallazgo del provider |
| Diagnóstico | Tablas `AzureSiteRecoveryJobs` y `ASRReplicatedItems` del almacén | Ya en la ficha del Recovery Services vault |

Alineación con el Well-Architected Framework:

- **Fiabilidad**: réplica continua, puntos cada 5 minutos, failback preparado y simulacros.
- **Seguridad**: Private Endpoints, identidad gestionada, caché sin clave y discos de réplica sin acceso público (Bicep).
- **Coste**: licencia por VM, réplica en Standard donde baste, simulacros cortos y reserva de capacidad solo para lo crítico.
- **Excelencia operativa**: infraestructura, protección y planes de recuperación en IaC; alertas integradas.
- **Rendimiento**: High Churn donde la tasa de cambio lo exige y endpoint de servicio de Storage frente al NVA.

## Módulo de Terraform

### Los módulos del repositorio

Están en `Migrate/`, no en `BackupAndUpdate/`:

| Pieza | Módulo | Estado |
|---|---|---|
| Fabric | [`Migrate/SiteRecoveryFabric`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Migrate/SiteRecoveryFabric) | **Utilizable** |
| Contenedor de protección | [`Migrate/SiteRecoveryProtectionContainer`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Migrate/SiteRecoveryProtectionContainer) | **Utilizable** |
| Política de replicación | [`Migrate/SiteRecoveryReplicationPolicy`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Migrate/SiteRecoveryReplicationPolicy) | Utilizable con valores explícitos |
| Mapeo de redes | [`Migrate/SiteRecoveryNetworkMapping`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Migrate/SiteRecoveryNetworkMapping) | Utilizable; una dirección por llamada |
| Mapeo de contenedores, VM replicada, plan de recuperación, caché, PE de ASR | — | No hay módulo |

Lo que hay que saber de los cuatro:

- Usan `count` con `create` y admiten azurerm desde 3.70.
- Declaran `locals.tf` con tags y una variable `tags`, pero **ningún recurso de ASR admite tags**: no hacen nada.
- **`SiteRecoveryReplicationPolicy`** trae por defecto 1440 minutos de retención y puntos coherentes cada 240, cuando el valor por defecto de Microsoft es tenerlos desactivados. Tampoco valida que la frecuencia no supere la retención; el provider lo detecta en el `apply`, no en el `plan`. En la ficha los valores van siempre explícitos y validados en el root.
- **`SiteRecoveryNetworkMapping`** crea un solo sentido. El failback necesita el inverso; en la ficha se llama al módulo dos veces por red.

Sobre el provider (azurerm 4.81, API `2024-04-01`):

- `azurerm_site_recovery_replicated_vm` **no expone el acceso de red de los discos de réplica y de failover**, así que se crean con acceso público. La API lo admite desde la versión `2026-02-01` (`recoveryNetworkAccessPolicy`, `recoveryPublicNetworkAccess`). Con Terraform hay que cerrarlo después en cada disco o desplegar con Bicep.
- La configuración de las NICs se aplica en una actualización posterior a la protección; casi todo lo demás **fuerza recreación**: cambiar un disco o el grupo de recursos de destino desactiva la réplica y vuelve a hacer la réplica inicial.
- La política se crea siempre con la sincronización multi-VM activada.

### Estructura en el proyecto

Mismo root que la [ficha del Recovery Services vault](/recursos/backups-update/recovery-services-vault/), que aporta el almacén y el diagnóstico de ASR. Este `providers.tf` **sustituye** al de esa ficha (añade `storage_use_azuread`):

```txt
/
├── providers.tf                 # azurerm >= 4.64.0 y storage_use_azuread
├── recovery_services_vaults.tf  # el de la ficha Recovery Services Vault
├── site_recovery.tf             # ASR: módulos de Migrate/ + recursos nativos
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
      # 4.64.0: deja de intentar cambiar el soft delete de almacenes en AlwaysON (secure by default).
      # < 5.0.0: restricción de los módulos de AzureTerraformModules.
      version = ">= 4.64.0, < 5.0.0"
    }
  }
}

provider "azurerm" {
  features {}

  # La cuenta de caché de ASR se crea con la clave de acceso desactivada:
  # el provider debe usar Entra ID para el plano de datos de Storage.
  storage_use_azuread = true
}

variable "tags" {
  description = "Tags corporativos comunes a todos los recursos."
  type        = map(string)
}
```

### `site_recovery.tf`

```hcl
# =============================================================================
# Azure Site Recovery (Azure a Azure): infraestructura de réplica, cuenta de caché,
# Private Endpoints, VMs replicadas y planes de recuperación
#
# DEPENDENCY: azurerm_recovery_services_vault.this (recovery_services_vaults.tf) con identidad
#             SystemAssigned, en una región distinta de la de origen (o la misma en zone-to-zone)
# DEPENDENCY: redes virtuales de origen y destino creadas; en destino, subredes con el nombre
#             que se indica en cada NIC
# DEPENDENCY: grupos de recursos de destino creados y distintos de los de origen
# DEPENDENCY: salida a Internet o a las service tags de ASR desde las subredes de las VMs
# DEPENDENCY: endpoint de servicio Microsoft.Storage (o Private Endpoint) en las subredes de origen
#             para llegar a la cuenta de caché con firewall
# =============================================================================

variable "site_recovery" {
  description = "Escenarios de DR (clave = nombre del par, p. ej. sdc-weu). Una entrada por almacén y región de origen."
  type = map(object({
    vault           = string # clave en var.recovery_services_vaults
    source_location = string
    target_location = string
    zone_to_zone    = optional(bool, false) # true: misma región, otra zona

    # Retención de puntos (máx. 15 días) y puntos coherentes con la aplicación (0 = desactivado)
    replication_policy = optional(object({
      recovery_point_retention_in_minutes                  = optional(number, 1440)
      application_consistent_snapshot_frequency_in_minutes = optional(number, 0)
    }), {})

    # Actualización automática del agente de movilidad. No compatible con Private Endpoints.
    # La cuenta de Automation debe estar en la misma región que el almacén.
    automatic_update = optional(object({
      automation_account_id           = string
      automation_account_principal_id = string # identidad asignada por el sistema
    }))

    # Mapeo de redes origen -> destino; el inverso (failback) se crea solo
    network_mappings = optional(map(object({
      source_network_id = string
      target_network_id = string
    })), {})

    # Cuenta de caché: misma región y suscripción que las VMs de origen
    cache_storage_account = object({
      name                     = string
      resource_group_name      = string
      high_churn               = optional(bool, false)  # Premium block blob; obligatorio con Premium SSD v2 y Ultra
      account_replication_type = optional(string, "LRS") # LRS | ZRS
      allowed_subnet_ids       = optional(list(string), [])
      private_endpoint = optional(object({
        subnet_id           = string
        private_dns_zone_id = string # privatelink.blob.core.windows.net
      }))
    })

    # Private Endpoints del almacén para ASR (subrecurso AzureSiteRecovery). Crear ANTES de replicar.
    # Hub & spoke con peering: uno solo. Redes aisladas: uno en origen y otro en recuperación,
    # cada uno con su propia zona privatelink.siterecovery.windowsazure.com.
    private_endpoints = optional(map(object({
      subnet_id           = string
      location            = string
      resource_group_name = string
      private_dns_zone_id = string
    })), {})

    replicated_vms = optional(map(object({
      source_vm_id                              = string
      target_resource_group_id                  = string
      target_network_id                         = optional(string) # vacío solo en zone-to-zone
      test_network_id                           = optional(string) # red aislada para simulacros
      target_zone                               = optional(string)
      target_availability_set_id                = optional(string)
      target_proximity_placement_group_id       = optional(string)
      target_capacity_reservation_group_id      = optional(string)
      target_virtual_machine_size               = optional(string)
      target_boot_diagnostic_storage_account_id = optional(string)
      target_disk_encryption_set_id             = optional(string) # para todos los discos
      multi_vm_group_name                       = optional(string)

      managed_disks = map(object({
        disk_id                  = string
        target_disk_type         = string
        target_replica_disk_type = string
      }))

      network_interfaces = optional(map(object({
        source_network_interface_id = string
        target_subnet_name          = string
        target_static_ip            = optional(string)
        failover_test_subnet_name   = optional(string)
        failover_test_static_ip     = optional(string)
      })), {})
    })), {})

    # Planes de recuperación: hasta 7 grupos de arranque y 100 VMs
    recovery_plans = optional(map(object({
      primary_zone  = optional(string) # solo zone-to-zone
      recovery_zone = optional(string)
      boot_groups = list(object({
        vms = list(string) # claves de replicated_vms
        pre_actions = optional(list(object({
          name                      = string
          type                      = string # AutomationRunbookActionDetails | ManualActionDetails
          fail_over_directions      = optional(list(string), ["PrimaryToRecovery", "RecoveryToPrimary"])
          fail_over_types           = optional(list(string), ["TestFailover", "PlannedFailover", "UnplannedFailover"])
          fabric_location           = optional(string) # Primary | Recovery (runbooks)
          runbook_id                = optional(string)
          manual_action_instruction = optional(string)
        })), [])
        post_actions = optional(list(object({
          name                      = string
          type                      = string
          fail_over_directions      = optional(list(string), ["PrimaryToRecovery", "RecoveryToPrimary"])
          fail_over_types           = optional(list(string), ["TestFailover", "PlannedFailover", "UnplannedFailover"])
          fabric_location           = optional(string)
          runbook_id                = optional(string)
          manual_action_instruction = optional(string)
        })), [])
      }))
    })), {})

    tags = optional(map(string), {})
  }))
  default = {}

  validation {
    condition = alltrue([
      for k, v in var.site_recovery :
      v.zone_to_zone == (lower(v.source_location) == lower(v.target_location))
    ])
    error_message = "Región de origen y destino iguales solo en zone-to-zone (zone_to_zone = true)."
  }

  validation {
    condition = alltrue([
      for k, v in var.site_recovery :
      v.replication_policy.recovery_point_retention_in_minutes >= 0 &&
      v.replication_policy.recovery_point_retention_in_minutes <= 21600
    ])
    error_message = "La retención de puntos de recuperación va de 0 a 21600 minutos (15 días)."
  }

  validation {
    condition = alltrue([
      for k, v in var.site_recovery :
      v.replication_policy.application_consistent_snapshot_frequency_in_minutes == 0 || (
        v.replication_policy.application_consistent_snapshot_frequency_in_minutes >= 60 &&
        v.replication_policy.application_consistent_snapshot_frequency_in_minutes <= v.replication_policy.recovery_point_retention_in_minutes
      )
    ])
    error_message = "Puntos coherentes con la aplicación: 0 (desactivado) o cada 60 minutos o más, sin superar la retención."
  }

  validation {
    condition = alltrue([
      for k, v in var.site_recovery :
      v.automatic_update == null || length(v.private_endpoints) == 0
    ])
    error_message = "La actualización automática del agente con cuenta de Automation no funciona con Private Endpoints."
  }

  validation {
    condition = alltrue([
      for k, v in var.site_recovery :
      can(regex("^[a-z0-9]{3,24}$", v.cache_storage_account.name)) &&
      contains(["LRS", "ZRS"], v.cache_storage_account.account_replication_type)
    ])
    error_message = "Cuenta de caché: 3-24 minúsculas y números; redundancia LRS o ZRS."
  }

  validation {
    condition = alltrue(flatten([
      for k, v in var.site_recovery : [
        for vk, vm in v.replicated_vms :
        lower(vm.target_resource_group_id) != lower(join("/", slice(split("/", vm.source_vm_id), 0, 5)))
      ]
    ]))
    error_message = "El grupo de recursos de destino debe ser distinto del de la VM de origen."
  }

  validation {
    condition = alltrue(flatten([
      for k, v in var.site_recovery : [
        for vk, vm in v.replicated_vms : v.zone_to_zone ? vm.target_zone != null : vm.target_network_id != null
      ]
    ]))
    error_message = "Zone-to-zone exige target_zone; entre regiones, target_network_id."
  }

  validation {
    condition = alltrue(flatten([
      for k, v in var.site_recovery : [
        for vk, vm in v.replicated_vms :
        vm.test_network_id == null || vm.test_network_id != vm.target_network_id
      ]
    ]))
    error_message = "La red de simulacro (test_network_id) debe ser distinta de la red de recuperación."
  }

  validation {
    condition = alltrue(flatten([
      for k, v in var.site_recovery : [
        for pk, p in v.recovery_plans :
        length(p.boot_groups) >= 1 && length(p.boot_groups) <= 7 &&
        length(flatten([for g in p.boot_groups : g.vms])) <= 100 &&
        alltrue([for vm in flatten([for g in p.boot_groups : g.vms]) : contains(keys(v.replicated_vms), vm)])
      ]
    ]))
    error_message = "Plan de recuperación: 1-7 grupos, 100 VMs como máximo y solo claves de replicated_vms."
  }
}

# -----------------------------------------------------------------------------
# Fabrics: uno por región (en zone-to-zone, uno solo)
# -----------------------------------------------------------------------------
module "asr_fabric" {
  source = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Migrate/SiteRecoveryFabric?ref=main"
  for_each = {
    for f in distinct(flatten([
      for k, v in var.site_recovery : [
        { key = "${k}/${v.source_location}", vault = v.vault, location = v.source_location },
        { key = "${k}/${v.target_location}", vault = v.vault, location = v.target_location },
      ]
    ])) : f.key => f
  }

  name                = "fabric-${each.value.location}"
  resource_group_name = azurerm_recovery_services_vault.this[each.value.vault].resource_group_name
  recovery_vault_name = azurerm_recovery_services_vault.this[each.value.vault].name
  location            = each.value.location
}

# -----------------------------------------------------------------------------
# Contenedores de protección: origen y destino (en zone-to-zone, ambos en el mismo fabric)
# -----------------------------------------------------------------------------
module "asr_container" {
  source = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Migrate/SiteRecoveryProtectionContainer?ref=main"
  for_each = {
    for c in flatten([
      for k, v in var.site_recovery : [
        { key = "${k}/source", pair = k, vault = v.vault, location = v.source_location, role = "source" },
        { key = "${k}/target", pair = k, vault = v.vault, location = v.target_location, role = "target" },
      ]
    ]) : c.key => c
  }

  name                 = "pc-${each.value.pair}-${each.value.role}"
  resource_group_name  = azurerm_recovery_services_vault.this[each.value.vault].resource_group_name
  recovery_vault_name  = azurerm_recovery_services_vault.this[each.value.vault].name
  recovery_fabric_name = module.asr_fabric["${each.value.pair}/${each.value.location}"].name
}

# -----------------------------------------------------------------------------
# Política de replicación
# -----------------------------------------------------------------------------
module "asr_policy" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Migrate/SiteRecoveryReplicationPolicy?ref=main"
  for_each = var.site_recovery

  name                                                 = "pol-${each.key}"
  resource_group_name                                  = azurerm_recovery_services_vault.this[each.value.vault].resource_group_name
  recovery_vault_name                                  = azurerm_recovery_services_vault.this[each.value.vault].name
  recovery_point_retention_in_minutes                  = each.value.replication_policy.recovery_point_retention_in_minutes
  application_consistent_snapshot_frequency_in_minutes = each.value.replication_policy.application_consistent_snapshot_frequency_in_minutes
}

# -----------------------------------------------------------------------------
# Mapeo de contenedores: ida (protección) y vuelta (reprotección y failback)
# -----------------------------------------------------------------------------
resource "azurerm_site_recovery_protection_container_mapping" "this" {
  for_each = {
    for m in flatten([
      for k, v in var.site_recovery : [
        { key = "${k}/forward", pair = k, vault = v.vault, from = "source", to = "target", from_location = v.source_location, auto = v.automatic_update },
        { key = "${k}/reverse", pair = k, vault = v.vault, from = "target", to = "source", from_location = v.target_location, auto = v.automatic_update },
      ]
    ]) : m.key => m
  }

  name                                      = "map-${replace(each.key, "/", "-")}"
  resource_group_name                       = azurerm_recovery_services_vault.this[each.value.vault].resource_group_name
  recovery_vault_name                       = azurerm_recovery_services_vault.this[each.value.vault].name
  recovery_fabric_name                      = module.asr_fabric["${each.value.pair}/${each.value.from_location}"].name
  recovery_source_protection_container_name = module.asr_container["${each.value.pair}/${each.value.from}"].name
  recovery_target_protection_container_id   = module.asr_container["${each.value.pair}/${each.value.to}"].id
  recovery_replication_policy_id            = module.asr_policy[each.value.pair].id

  # El ajuste se aplica a todas las VMs del contenedor
  dynamic "automatic_update" {
    for_each = each.value.auto == null ? [] : [each.value.auto]
    content {
      enabled               = true
      automation_account_id = automatic_update.value.automation_account_id
      authentication_type   = "SystemAssignedIdentity"
    }
  }

  depends_on = [azurerm_role_assignment.asr_automation]
}

# La identidad de la cuenta de Automation necesita permisos sobre el almacén
resource "azurerm_role_assignment" "asr_automation" {
  for_each = { for k, v in var.site_recovery : k => v if v.automatic_update != null }

  scope                = azurerm_recovery_services_vault.this[each.value.vault].id
  role_definition_name = "Contributor"
  principal_id         = each.value.automatic_update.automation_account_principal_id
  principal_type       = "ServicePrincipal"
}

# -----------------------------------------------------------------------------
# Mapeo de redes: ida y vuelta (no aplica a zone-to-zone)
# -----------------------------------------------------------------------------
module "asr_network_mapping" {
  source = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Migrate/SiteRecoveryNetworkMapping?ref=main"
  for_each = {
    for n in flatten([
      for k, v in var.site_recovery : [
        for nk, net in v.network_mappings : [
          {
            key = "${k}/${nk}/forward", pair = k, vault = v.vault
            from_location = v.source_location, to_location = v.target_location
            from_network = net.source_network_id, to_network = net.target_network_id
          },
          {
            key = "${k}/${nk}/reverse", pair = k, vault = v.vault
            from_location = v.target_location, to_location = v.source_location
            from_network = net.target_network_id, to_network = net.source_network_id
          },
        ]
      ] if !v.zone_to_zone
    ]) : n.key => n
  }

  name                        = "netmap-${replace(each.key, "/", "-")}"
  resource_group_name         = azurerm_recovery_services_vault.this[each.value.vault].resource_group_name
  recovery_vault_name         = azurerm_recovery_services_vault.this[each.value.vault].name
  source_recovery_fabric_name = module.asr_fabric["${each.value.pair}/${each.value.from_location}"].name
  target_recovery_fabric_name = module.asr_fabric["${each.value.pair}/${each.value.to_location}"].name
  source_network_id           = each.value.from_network
  target_network_id           = each.value.to_network
}

# -----------------------------------------------------------------------------
# Cuenta de caché en la región de origen
# Sin soft delete (no soportado), sin clave de acceso y con firewall + servicios de confianza
# -----------------------------------------------------------------------------
resource "azurerm_storage_account" "asr_cache" {
  for_each = var.site_recovery

  name                     = each.value.cache_storage_account.name
  resource_group_name      = each.value.cache_storage_account.resource_group_name
  location                 = each.value.source_location
  account_kind             = each.value.cache_storage_account.high_churn ? "BlockBlobStorage" : "StorageV2"
  account_tier             = each.value.cache_storage_account.high_churn ? "Premium" : "Standard"
  account_replication_type = each.value.cache_storage_account.account_replication_type
  access_tier              = each.value.cache_storage_account.high_churn ? null : "Hot"

  https_traffic_only_enabled      = true
  min_tls_version                 = "TLS1_2"
  shared_access_key_enabled       = false # el almacén accede con su identidad gestionada
  allow_nested_items_to_be_public = false
  # ASR necesita el endpoint público con firewall; desactivarlo rompe la replicación
  public_network_access_enabled = true

  network_rules {
    default_action             = "Deny"
    bypass                     = ["AzureServices"]
    virtual_network_subnet_ids = each.value.cache_storage_account.allowed_subnet_ids
  }

  tags = merge(var.tags, each.value.tags)
}

# Permisos de la identidad del almacén sobre la caché (obligatorios con PE o sin clave de acceso)
resource "azurerm_role_assignment" "asr_cache" {
  for_each = {
    for r in flatten([
      for k, v in var.site_recovery : [
        for role in ["Contributor", v.cache_storage_account.high_churn ? "Storage Blob Data Owner" : "Storage Blob Data Contributor"] : {
          key   = "${k}/${role}"
          pair  = k
          vault = v.vault
          role  = role
        }
      ]
    ]) : r.key => r
  }

  scope                = azurerm_storage_account.asr_cache[each.value.pair].id
  role_definition_name = each.value.role
  principal_id         = azurerm_recovery_services_vault.this[each.value.vault].identity[0].principal_id
  principal_type       = "ServicePrincipal"
}

resource "azurerm_private_endpoint" "asr_cache" {
  for_each = { for k, v in var.site_recovery : k => v if v.cache_storage_account.private_endpoint != null }

  name                = "pe-${each.value.cache_storage_account.name}-blob"
  resource_group_name = each.value.cache_storage_account.resource_group_name
  location            = each.value.source_location
  subnet_id           = each.value.cache_storage_account.private_endpoint.subnet_id

  private_service_connection {
    name                           = "psc-${each.value.cache_storage_account.name}-blob"
    private_connection_resource_id = azurerm_storage_account.asr_cache[each.key].id
    subresource_names              = ["blob"]
    is_manual_connection           = false
  }

  private_dns_zone_group {
    name                 = "default"
    private_dns_zone_ids = [each.value.cache_storage_account.private_endpoint.private_dns_zone_id]
  }

  tags = merge(var.tags, each.value.tags)
}

# -----------------------------------------------------------------------------
# Private Endpoints del almacén para ASR
# -----------------------------------------------------------------------------
resource "azurerm_private_endpoint" "asr" {
  for_each = {
    for p in flatten([
      for k, v in var.site_recovery : [
        for pk, pe in v.private_endpoints : {
          key   = "${k}/${pk}"
          pair  = k
          vault = v.vault
          name  = "pe-${v.vault}-asr-${pk}"
          pe    = pe
          tags  = v.tags
        }
      ]
    ]) : p.key => p
  }

  name                = each.value.name
  resource_group_name = each.value.pe.resource_group_name
  location            = each.value.pe.location
  subnet_id           = each.value.pe.subnet_id

  private_service_connection {
    name                           = "psc-${each.value.name}"
    private_connection_resource_id = azurerm_recovery_services_vault.this[each.value.vault].id
    subresource_names              = ["AzureSiteRecovery"]
    is_manual_connection           = false
  }

  private_dns_zone_group {
    name                 = "default"
    private_dns_zone_ids = [each.value.pe.private_dns_zone_id]
  }

  tags = merge(var.tags, each.value.tags)
}

# -----------------------------------------------------------------------------
# VMs replicadas
# Casi todos los argumentos fuerzan recreación: cambiar uno desactiva y reactiva la réplica
# (réplica inicial completa de nuevo).
# -----------------------------------------------------------------------------
resource "azurerm_site_recovery_replicated_vm" "this" {
  for_each = {
    for r in flatten([
      for k, v in var.site_recovery : [
        for vk, vm in v.replicated_vms : {
          key             = "${k}/${vk}"
          name            = vk
          pair            = k
          vault           = v.vault
          source_location = v.source_location
          target_location = v.target_location
          vm              = vm
        }
      ]
    ]) : r.key => r
  }

  name                                      = each.value.name
  resource_group_name                       = azurerm_recovery_services_vault.this[each.value.vault].resource_group_name
  recovery_vault_name                       = azurerm_recovery_services_vault.this[each.value.vault].name
  recovery_replication_policy_id            = module.asr_policy[each.value.pair].id
  source_recovery_fabric_name               = module.asr_fabric["${each.value.pair}/${each.value.source_location}"].name
  source_vm_id                              = each.value.vm.source_vm_id
  source_recovery_protection_container_name = module.asr_container["${each.value.pair}/source"].name
  target_resource_group_id                  = each.value.vm.target_resource_group_id
  target_recovery_fabric_id                 = module.asr_fabric["${each.value.pair}/${each.value.target_location}"].id
  target_recovery_protection_container_id   = module.asr_container["${each.value.pair}/target"].id

  target_network_id                         = each.value.vm.target_network_id
  test_network_id                           = each.value.vm.test_network_id
  target_zone                               = each.value.vm.target_zone
  target_availability_set_id                = each.value.vm.target_availability_set_id
  target_proximity_placement_group_id       = each.value.vm.target_proximity_placement_group_id
  target_capacity_reservation_group_id      = each.value.vm.target_capacity_reservation_group_id
  target_virtual_machine_size               = each.value.vm.target_virtual_machine_size
  target_boot_diagnostic_storage_account_id = each.value.vm.target_boot_diagnostic_storage_account_id
  multi_vm_group_name                       = each.value.vm.multi_vm_group_name

  dynamic "managed_disk" {
    for_each = each.value.vm.managed_disks
    content {
      disk_id                       = managed_disk.value.disk_id
      staging_storage_account_id    = azurerm_storage_account.asr_cache[each.value.pair].id
      target_resource_group_id      = each.value.vm.target_resource_group_id
      target_disk_type              = managed_disk.value.target_disk_type
      target_replica_disk_type      = managed_disk.value.target_replica_disk_type
      target_disk_encryption_set_id = each.value.vm.target_disk_encryption_set_id
    }
  }

  dynamic "network_interface" {
    for_each = each.value.vm.network_interfaces
    content {
      source_network_interface_id = network_interface.value.source_network_interface_id
      target_subnet_name          = network_interface.value.target_subnet_name
      target_static_ip            = network_interface.value.target_static_ip
      failover_test_subnet_name   = network_interface.value.failover_test_subnet_name
      failover_test_static_ip     = network_interface.value.failover_test_static_ip
    }
  }

  # Con Disk Encryption Set la creación puede durar hasta 5 horas
  timeouts {
    create = "5h"
  }

  # DEPENDENCY: mapeos, permisos sobre la caché y Private Endpoints listos antes de replicar
  depends_on = [
    azurerm_site_recovery_protection_container_mapping.this,
    module.asr_network_mapping,
    azurerm_role_assignment.asr_cache,
    azurerm_private_endpoint.asr,
    azurerm_private_endpoint.asr_cache,
  ]
}

# -----------------------------------------------------------------------------
# Planes de recuperación: orden de arranque y acciones
# -----------------------------------------------------------------------------
resource "azurerm_site_recovery_replication_recovery_plan" "this" {
  for_each = {
    for p in flatten([
      for k, v in var.site_recovery : [
        for pk, plan in v.recovery_plans : {
          key             = "${k}/${pk}"
          name            = pk
          pair            = k
          vault           = v.vault
          source_location = v.source_location
          target_location = v.target_location
          zone_to_zone    = v.zone_to_zone
          plan            = plan
        }
      ]
    ]) : p.key => p
  }

  name                      = each.value.name
  recovery_vault_id         = azurerm_recovery_services_vault.this[each.value.vault].id
  source_recovery_fabric_id = module.asr_fabric["${each.value.pair}/${each.value.source_location}"].id
  target_recovery_fabric_id = module.asr_fabric["${each.value.pair}/${each.value.target_location}"].id

  shutdown_recovery_group {}
  failover_recovery_group {}

  dynamic "boot_recovery_group" {
    for_each = each.value.plan.boot_groups
    content {
      replicated_protected_items = [
        for vm in boot_recovery_group.value.vms : azurerm_site_recovery_replicated_vm.this["${each.value.pair}/${vm}"].id
      ]

      dynamic "pre_action" {
        for_each = boot_recovery_group.value.pre_actions
        content {
          name                      = pre_action.value.name
          type                      = pre_action.value.type
          fail_over_directions      = pre_action.value.fail_over_directions
          fail_over_types           = pre_action.value.fail_over_types
          fabric_location           = pre_action.value.fabric_location
          runbook_id                = pre_action.value.runbook_id
          manual_action_instruction = pre_action.value.manual_action_instruction
        }
      }

      dynamic "post_action" {
        for_each = boot_recovery_group.value.post_actions
        content {
          name                      = post_action.value.name
          type                      = post_action.value.type
          fail_over_directions      = post_action.value.fail_over_directions
          fail_over_types           = post_action.value.fail_over_types
          fabric_location           = post_action.value.fabric_location
          runbook_id                = post_action.value.runbook_id
          manual_action_instruction = post_action.value.manual_action_instruction
        }
      }
    }
  }

  dynamic "azure_to_azure_settings" {
    for_each = each.value.zone_to_zone ? [each.value.plan] : []
    content {
      primary_zone  = azure_to_azure_settings.value.primary_zone
      recovery_zone = azure_to_azure_settings.value.recovery_zone
    }
  }
}

# -----------------------------------------------------------------------------
# Salidas
# -----------------------------------------------------------------------------
output "site_recovery_replication_policy_ids" {
  description = "Políticas de replicación por par."
  value       = { for k, m in module.asr_policy : k => m.id }
}

output "site_recovery_replicated_vm_ids" {
  description = "Elementos replicados (par/VM)."
  value       = { for k, r in azurerm_site_recovery_replicated_vm.this : k => r.id }
}

output "site_recovery_recovery_plan_ids" {
  description = "Planes de recuperación (par/plan)."
  value       = { for k, p in azurerm_site_recovery_replication_recovery_plan.this : k => p.id }
}

output "site_recovery_cache_storage_account_ids" {
  description = "Cuentas de caché por par."
  value       = { for k, s in azurerm_storage_account.asr_cache : k => s.id }
}
```

### `env/pro.tfvars`

```hcl
# Se añade al env/pro.tfvars de la ficha Recovery Services Vault.
# Almacén de ASR en la región de DESTINO: el de backup vive en la de origen, así que son dos almacenes.
recovery_services_vaults = {
  # ... almacén de backup de la región de origen (ficha Recovery Services Vault) ...

  "rsv-<workload>-pro-<region-destino>-asr-01" = {
    resource_group_name = "<rg-asr-pro-destino>" # el grupo de recursos tampoco puede estar en la región de origen
    location            = "<region-destino>"

    storage_mode_type             = "GeoRedundant" # ASR no guarda datos en el almacén; solo metadatos
    immutability                  = "Disabled"     # no aplica a ASR
    public_network_access_enabled = false

    identity = {
      type = "SystemAssigned" # acceso a la caché sin clave y con Private Endpoints
    }

    private_endpoints = {} # los de Azure Backup no sirven para ASR; van en site_recovery

    action_group_ids           = ["<resourceId action group de operaciones>"]
    log_analytics_workspace_id = "<resourceId log-analytics-workspace>"
    site_recovery_diagnostics  = true
  }
}

site_recovery = {
  "<origen>-<destino>" = {
    vault           = "rsv-<workload>-pro-<region-destino>-asr-01"
    source_location = "<region-origen>"
    target_location = "<region-destino>"

    replication_policy = {
      recovery_point_retention_in_minutes                  = 1440 # 24 horas
      application_consistent_snapshot_frequency_in_minutes = 240  # cada 4 horas (VSS copy-only)
    }

    network_mappings = {
      spoke-app = {
        source_network_id = "<resourceId vnet-app-pro-origen>"
        target_network_id = "<resourceId vnet-app-pro-destino>"
      }
    }

    cache_storage_account = {
      name                = "<stasrcachepro01>"
      resource_group_name = "<rg-asr-pro-origen>" # región y suscripción de las VMs
      high_churn          = false
      allowed_subnet_ids  = ["<resourceId snet-app-origen (con service endpoint Microsoft.Storage)>"]
    }

    # Hub & spoke con peering entre regiones: un único Private Endpoint en el hub
    private_endpoints = {
      hub = {
        subnet_id           = "<resourceId snet-privateendpoints-hub>"
        location            = "<region-origen>"
        resource_group_name = "<rg-connectivity-pro>"
        private_dns_zone_id = "<resourceId privatelink.siterecovery.windowsazure.com>"
      }
    }

    replicated_vms = {
      "vm-app-01" = {
        source_vm_id             = "<resourceId vm-app-01>"
        target_resource_group_id = "<resourceId rg-app-pro-destino>"
        target_network_id        = "<resourceId vnet-app-pro-destino>"
        test_network_id          = "<resourceId vnet-app-pro-destino-test>" # aislada, mismo direccionamiento
        target_zone              = "1"

        managed_disks = {
          os = {
            disk_id                  = "<resourceId osdisk vm-app-01>"
            target_disk_type         = "Premium_LRS"
            target_replica_disk_type = "Standard_LRS"
          }
          data01 = {
            disk_id                  = "<resourceId datadisk01 vm-app-01>"
            target_disk_type         = "Premium_LRS"
            target_replica_disk_type = "Standard_LRS"
          }
        }

        network_interfaces = {
          nic01 = {
            source_network_interface_id = "<resourceId nic vm-app-01>"
            target_subnet_name          = "snet-app"
            failover_test_subnet_name   = "snet-app"
          }
        }
      }

      "vm-sql-01" = {
        source_vm_id             = "<resourceId vm-sql-01>"
        target_resource_group_id = "<resourceId rg-app-pro-destino>"
        target_network_id        = "<resourceId vnet-app-pro-destino>"
        test_network_id          = "<resourceId vnet-app-pro-destino-test>"
        target_zone              = "1"

        managed_disks = {
          os = {
            disk_id                  = "<resourceId osdisk vm-sql-01>"
            target_disk_type         = "Premium_LRS"
            target_replica_disk_type = "Premium_LRS" # réplica premium por la tasa de cambio
          }
        }

        network_interfaces = {
          nic01 = {
            source_network_interface_id = "<resourceId nic vm-sql-01>"
            target_subnet_name          = "snet-data"
            failover_test_subnet_name   = "snet-data"
          }
        }
      }
    }

    recovery_plans = {
      "rp-app-pro" = {
        boot_groups = [
          {
            vms = ["vm-sql-01"] # primero la base de datos
          },
          {
            vms = ["vm-app-01"]
            post_actions = [
              {
                name                      = "validar-aplicacion"
                type                      = "ManualActionDetails"
                manual_action_instruction = "Comprobar el acceso a la aplicación y actualizar DNS si procede."
              }
            ]
          },
        ]
      }
    }
  }
}
```

### Despliegue, comprobación y simulacro

```powershell
terraform init
terraform plan -var-file="env/pro.tfvars" -out="pro.tfplan"
terraform apply "pro.tfplan"

# Contexto del almacén de ASR
$vault = Get-AzRecoveryServicesVault -ResourceGroupName "<rg-asr-pro-destino>" -Name "rsv-<workload>-pro-<region-destino>-asr-01"
Set-AzRecoveryServicesAsrVaultContext -Vault $vault | Out-Null

# Estado de la réplica
$fabric    = Get-AzRecoveryServicesAsrFabric -Name "fabric-<region-origen>"
$container = Get-AzRecoveryServicesAsrProtectionContainer -Fabric $fabric -Name "pc-<origen>-<destino>-source"
Get-AzRecoveryServicesAsrReplicationProtectedItem -ProtectionContainer $container |
    Select-Object FriendlyName, ProtectionState, ReplicationHealth, TestFailoverState

# Simulacro del plan en la red aislada
$plan    = Get-AzRecoveryServicesAsrRecoveryPlan -Name "rp-app-pro"
$testNet = Get-AzVirtualNetwork -ResourceGroupName "<rg-network-destino>" -Name "<vnet-app-pro-destino-test>"
$job = Start-AzRecoveryServicesAsrTestFailoverJob -RecoveryPlan $plan -Direction PrimaryToRecovery -AzureVMNetworkId $testNet.Id
while ($job.State -in @("NotStarted", "InProgress")) {
    Start-Sleep -Seconds 30
    $job = Get-AzRecoveryServicesAsrJob -Job $job
}
$job.State

# Validar la aplicación y limpiar (borra las VMs de prueba)
Start-AzRecoveryServicesAsrTestFailoverCleanupJob -RecoveryPlan $plan -Comment "Simulacro <fecha>: <resultado>"
```

### Equivalente en Bicep

Cubre el escenario entre regiones con la API `2026-07-01`, que sí permite cerrar el acceso de red de los discos de réplica. La red y la subred de destino se fijan al habilitar la protección; el tamaño de destino y las IPs se ajustan después en el portal o con `Set-AzRecoveryServicesAsrReplicationProtectedItem`.

`main.bicep` (grupo de recursos del almacén de ASR):

```bicep
// =============================================================================
// Azure Site Recovery (Azure a Azure, entre regiones) sobre un Recovery Services vault existente
// Se despliega en el grupo de recursos del almacén (región de destino)
// DEPENDENCY: almacén con identidad SystemAssigned, fuera de la región de origen
// DEPENDENCY: redes de origen, destino y simulacro creadas; grupos de recursos de destino creados
// DEPENDENCY: zone-to-zone no está cubierto aquí (un solo fabric); usar la variante de Terraform
// =============================================================================
targetScope = 'resourceGroup'

type networkMapping = {
  name: string
  sourceNetworkId: string
  targetNetworkId: string
}

type replicatedDisk = {
  diskId: string
  targetDiskType: ('Standard_LRS' | 'StandardSSD_LRS' | 'Premium_LRS' | 'PremiumV2_LRS' | 'UltraSSD_LRS' | 'StandardSSD_ZRS' | 'Premium_ZRS')
  replicaDiskType: ('Standard_LRS' | 'StandardSSD_LRS' | 'Premium_LRS' | 'PremiumV2_LRS' | 'UltraSSD_LRS' | 'StandardSSD_ZRS' | 'Premium_ZRS')
}

type replicatedVm = {
  name: string
  sourceVmId: string
  targetResourceGroupId: string
  targetNetworkId: string
  targetSubnetName: string
  targetZone: string?
  multiVmGroupName: string?
  disks: replicatedDisk[]
}

type privateEndpoint = {
  name: string
  location: string
  resourceGroupName: string
  subnetId: string
  privateDnsZoneId: string
}

type recoveryPlan = {
  name: string
  @description('Grupos de arranque en orden (máx. 7); cada uno, nombres de VMs replicadas.')
  @maxLength(7)
  bootGroups: string[][]
}

param vaultName string
param pairName string
param sourceLocation string
param targetLocation string

@description('Retención de puntos de recuperación en minutos (máx. 15 días).')
@minValue(0)
@maxValue(21600)
param recoveryPointRetentionInMinutes int = 1440

@description('Frecuencia de puntos coherentes con la aplicación: 0 (desactivado) o 60 minutos o más.')
param appConsistentFrequencyInMinutes int = 0

param networkMappings networkMapping[] = []

param cacheStorageAccountName string
param cacheResourceGroupName string
param cacheHighChurn bool = false
param cacheAllowedSubnetIds array = []

param asrPrivateEndpoints privateEndpoint[] = []

@description('Acceso de red de los discos de réplica y de failover. Por defecto, sin acceso público ni exportación.')
@allowed(['AllowAll', 'DenyAll'])
param recoveryDiskNetworkAccessPolicy string = 'DenyAll'

param replicatedVms replicatedVm[] = []
param recoveryPlans recoveryPlan[] = []
param tags object = {}

resource vault 'Microsoft.RecoveryServices/vaults@2025-02-01' existing = {
  name: vaultName
}

// Private Endpoints de ASR: antes de registrar nada en el almacén
module asrPe 'asr-pe.bicep' = [
  for pe in asrPrivateEndpoints: {
    name: 'asr-pe-${pe.name}'
    scope: resourceGroup(pe.resourceGroupName)
    params: {
      name: pe.name
      location: pe.location
      subnetId: pe.subnetId
      vaultId: vault.id
      privateDnsZoneId: pe.privateDnsZoneId
      tags: tags
    }
  }
]

// Caché en la región de origen, con permisos para la identidad del almacén
module cache 'asr-cache.bicep' = {
  name: 'asr-cache-${pairName}'
  scope: resourceGroup(cacheResourceGroupName)
  params: {
    name: cacheStorageAccountName
    location: sourceLocation
    vaultPrincipalId: vault.identity.principalId
    highChurn: cacheHighChurn
    allowedSubnetIds: cacheAllowedSubnetIds
    tags: tags
  }
}

resource sourceFabric 'Microsoft.RecoveryServices/vaults/replicationFabrics@2026-07-01' = {
  parent: vault
  name: 'fabric-${sourceLocation}'
  properties: {
    customDetails: {
      instanceType: 'Azure'
      location: sourceLocation
    }
  }
}

resource targetFabric 'Microsoft.RecoveryServices/vaults/replicationFabrics@2026-07-01' = {
  parent: vault
  name: 'fabric-${targetLocation}'
  properties: {
    customDetails: {
      instanceType: 'Azure'
      location: targetLocation
    }
  }
}

resource sourceContainer 'Microsoft.RecoveryServices/vaults/replicationFabrics/replicationProtectionContainers@2026-07-01' = {
  parent: sourceFabric
  name: 'pc-${pairName}-source'
  properties: {
    providerSpecificInput: [
      {
        instanceType: 'A2A'
      }
    ]
  }
}

resource targetContainer 'Microsoft.RecoveryServices/vaults/replicationFabrics/replicationProtectionContainers@2026-07-01' = {
  parent: targetFabric
  name: 'pc-${pairName}-target'
  properties: {
    providerSpecificInput: [
      {
        instanceType: 'A2A'
      }
    ]
  }
}

resource policy 'Microsoft.RecoveryServices/vaults/replicationPolicies@2026-07-01' = {
  parent: vault
  name: 'pol-${pairName}'
  properties: {
    providerSpecificInput: {
      instanceType: 'A2A'
      recoveryPointHistory: recoveryPointRetentionInMinutes
      appConsistentFrequencyInMinutes: appConsistentFrequencyInMinutes
      multiVmSyncStatus: 'Enable'
    }
  }
}

// Ida (protección) y vuelta (reprotección y failback)
resource forwardMapping 'Microsoft.RecoveryServices/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectionContainerMappings@2026-07-01' = {
  parent: sourceContainer
  name: 'map-${pairName}-forward'
  properties: {
    targetProtectionContainerId: targetContainer.id
    policyId: policy.id
    providerSpecificInput: {
      instanceType: 'A2A'
      agentAutoUpdateStatus: 'Disabled'
    }
  }
}

resource reverseMapping 'Microsoft.RecoveryServices/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectionContainerMappings@2026-07-01' = {
  parent: targetContainer
  name: 'map-${pairName}-reverse'
  properties: {
    targetProtectionContainerId: sourceContainer.id
    policyId: policy.id
    providerSpecificInput: {
      instanceType: 'A2A'
      agentAutoUpdateStatus: 'Disabled'
    }
  }
}

// La "red" de ASR dentro de un fabric se llama como la VNet
resource forwardNetworkMappings 'Microsoft.RecoveryServices/vaults/replicationFabrics/replicationNetworks/replicationNetworkMappings@2026-07-01' = [
  for m in networkMappings: {
    name: '${vaultName}/${sourceFabric.name}/${last(split(m.sourceNetworkId, '/'))}/netmap-${m.name}-forward'
    properties: {
      recoveryFabricName: targetFabric.name
      recoveryNetworkId: m.targetNetworkId
      fabricSpecificDetails: {
        instanceType: 'AzureToAzure'
        primaryNetworkId: m.sourceNetworkId
      }
    }
  }
]

resource reverseNetworkMappings 'Microsoft.RecoveryServices/vaults/replicationFabrics/replicationNetworks/replicationNetworkMappings@2026-07-01' = [
  for m in networkMappings: {
    name: '${vaultName}/${targetFabric.name}/${last(split(m.targetNetworkId, '/'))}/netmap-${m.name}-reverse'
    properties: {
      recoveryFabricName: sourceFabric.name
      recoveryNetworkId: m.sourceNetworkId
      fabricSpecificDetails: {
        instanceType: 'AzureToAzure'
        primaryNetworkId: m.targetNetworkId
      }
    }
  }
]

// VMs replicadas: red y subred de destino en la habilitación; tamaño, IPs y red de simulacro, después
resource protectedItems 'Microsoft.RecoveryServices/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectedItems@2026-07-01' = [
  for vm in replicatedVms: {
    parent: sourceContainer
    name: vm.name
    properties: {
      policyId: policy.id
      providerSpecificDetails: {
        instanceType: 'A2A'
        fabricObjectId: vm.sourceVmId
        recoveryContainerId: targetContainer.id
        recoveryResourceGroupId: vm.targetResourceGroupId
        recoveryAzureNetworkId: vm.targetNetworkId
        recoverySubnetName: vm.targetSubnetName
        recoveryAvailabilityZone: vm.?targetZone
        multiVmGroupName: vm.?multiVmGroupName
        vmManagedDisks: [
          for d in vm.disks: {
            diskId: d.diskId
            primaryStagingAzureStorageAccountId: cache.outputs.id
            recoveryResourceGroupId: vm.targetResourceGroupId
            recoveryTargetDiskAccountType: d.targetDiskType
            recoveryReplicaDiskAccountType: d.replicaDiskType
            recoveryNetworkAccessPolicy: recoveryDiskNetworkAccessPolicy
            recoveryPublicNetworkAccess: recoveryDiskNetworkAccessPolicy == 'AllowAll' ? 'Enabled' : 'Disabled'
          }
        ]
      }
    }
    dependsOn: [
      forwardMapping
      reverseMapping
      forwardNetworkMappings
      reverseNetworkMappings
      asrPe
    ]
  }
]

resource plans 'Microsoft.RecoveryServices/vaults/replicationRecoveryPlans@2026-07-01' = [
  for p in recoveryPlans: {
    parent: vault
    name: p.name
    properties: {
      primaryFabricId: sourceFabric.id
      recoveryFabricId: targetFabric.id
      failoverDeploymentModel: 'ResourceManager'
      groups: concat(
        [
          {
            groupType: 'Shutdown'
            replicationProtectedItems: []
          }
          {
            groupType: 'Failover'
            replicationProtectedItems: []
          }
        ],
        map(p.bootGroups, group => {
          groupType: 'Boot'
          replicationProtectedItems: map(group, vmName => {
            id: resourceId(
              'Microsoft.RecoveryServices/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectedItems',
              vaultName,
              sourceFabric.name,
              sourceContainer.name,
              vmName
            )
            virtualMachineId: filter(replicatedVms, v => v.name == vmName)[0].sourceVmId
          })
        })
      )
    }
    dependsOn: [
      protectedItems
    ]
  }
]

output policyId string = policy.id
output cacheStorageAccountId string = cache.outputs.id
output protectedItemIds array = [for (vm, i) in replicatedVms: protectedItems[i].id]
```

`asr-cache.bicep`:

```bicep
// =============================================================================
// Cuenta de caché de Azure Site Recovery (región y suscripción de las VMs de origen)
// Sin soft delete (no soportado), sin clave de acceso y con firewall + servicios de confianza
// DEPENDENCY: identidad gestionada del almacén (principalId)
// DEPENDENCY: endpoint de servicio Microsoft.Storage en las subredes permitidas
// =============================================================================
param name string
param location string
param vaultPrincipalId string

@description('Premium block blob para alta tasa de cambio (obligatorio con Premium SSD v2 y Ultra).')
param highChurn bool = false

@allowed(['LRS', 'ZRS'])
param redundancy string = 'LRS'

param allowedSubnetIds array = []
param tags object = {}

var contributorRoleId = 'b24988ac-6180-42a0-ab88-20f7382dd24c'
var blobDataContributorRoleId = 'ba92f5b4-2d11-453d-a403-e96b0029c9fe'
var blobDataOwnerRoleId = 'b7e6dc6d-f1e8-4753-8033-0f276bb0955b'

resource cache 'Microsoft.Storage/storageAccounts@2025-01-01' = {
  name: name
  location: location
  kind: highChurn ? 'BlockBlobStorage' : 'StorageV2'
  sku: {
    name: highChurn ? 'Premium_${redundancy}' : 'Standard_${redundancy}'
  }
  properties: {
    accessTier: highChurn ? null : 'Hot'
    supportsHttpsTrafficOnly: true
    minimumTlsVersion: 'TLS1_2'
    allowSharedKeyAccess: false
    allowBlobPublicAccess: false
    // ASR necesita el endpoint público con firewall; desactivarlo rompe la replicación
    publicNetworkAccess: 'Enabled'
    networkAcls: {
      defaultAction: 'Deny'
      bypass: 'AzureServices'
      virtualNetworkRules: [
        for subnetId in allowedSubnetIds: {
          id: subnetId
          action: 'Allow'
        }
      ]
    }
  }
  tags: tags
}

resource roles 'Microsoft.Authorization/roleAssignments@2022-04-01' = [
  for roleId in [contributorRoleId, highChurn ? blobDataOwnerRoleId : blobDataContributorRoleId]: {
    name: guid(cache.id, vaultPrincipalId, roleId)
    scope: cache
    properties: {
      principalId: vaultPrincipalId
      principalType: 'ServicePrincipal'
      roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', roleId)
    }
  }
]

output id string = cache.id
```

`asr-pe.bicep`:

```bicep
// =============================================================================
// Private Endpoint del almacén para Azure Site Recovery (subrecurso AzureSiteRecovery)
// DEPENDENCY: almacén sin elementos registrados (crear ANTES de replicar)
// DEPENDENCY: zona privatelink.siterecovery.windowsazure.com enlazada a las redes de origen y destino
// =============================================================================
param name string
param location string
param subnetId string
param vaultId string
param privateDnsZoneId string
param tags object = {}

resource pe 'Microsoft.Network/privateEndpoints@2024-05-01' = {
  name: name
  location: location
  properties: {
    subnet: {
      id: subnetId
    }
    privateLinkServiceConnections: [
      {
        name: 'psc-${name}'
        properties: {
          privateLinkServiceId: vaultId
          groupIds: [
            'AzureSiteRecovery'
          ]
        }
      }
    ]
  }
  tags: tags
}

resource dnsGroup 'Microsoft.Network/privateEndpoints/privateDnsZoneGroups@2024-05-01' = {
  parent: pe
  name: 'default'
  properties: {
    privateDnsZoneConfigs: [
      {
        name: 'siterecovery'
        properties: {
          privateDnsZoneId: privateDnsZoneId
        }
      }
    ]
  }
}
```

`main.pro.bicepparam`:

```bicep
using 'main.bicep'

param vaultName = 'rsv-<workload>-pro-<region-destino>-asr-01'
param pairName = '<origen>-<destino>'
param sourceLocation = '<region-origen>'
param targetLocation = '<region-destino>'

param recoveryPointRetentionInMinutes = 1440
param appConsistentFrequencyInMinutes = 240

param networkMappings = [
  {
    name: 'spoke-app'
    sourceNetworkId: '<resourceId vnet-app-pro-origen>'
    targetNetworkId: '<resourceId vnet-app-pro-destino>'
  }
]

param cacheStorageAccountName = '<stasrcachepro01>'
param cacheResourceGroupName = '<rg-asr-pro-origen>'
param cacheAllowedSubnetIds = [
  '<resourceId snet-app-origen>'
]

param asrPrivateEndpoints = [
  {
    name: 'pe-rsv-asr-hub'
    location: '<region-origen>'
    resourceGroupName: '<rg-connectivity-pro>'
    subnetId: '<resourceId snet-privateendpoints-hub>'
    privateDnsZoneId: '<resourceId privatelink.siterecovery.windowsazure.com>'
  }
]

param replicatedVms = [
  {
    name: 'vm-sql-01'
    sourceVmId: '<resourceId vm-sql-01>'
    targetResourceGroupId: '<resourceId rg-app-pro-destino>'
    targetNetworkId: '<resourceId vnet-app-pro-destino>'
    targetSubnetName: 'snet-data'
    targetZone: '1'
    disks: [
      {
        diskId: '<resourceId osdisk vm-sql-01>'
        targetDiskType: 'Premium_LRS'
        replicaDiskType: 'Premium_LRS'
      }
    ]
  }
  {
    name: 'vm-app-01'
    sourceVmId: '<resourceId vm-app-01>'
    targetResourceGroupId: '<resourceId rg-app-pro-destino>'
    targetNetworkId: '<resourceId vnet-app-pro-destino>'
    targetSubnetName: 'snet-app'
    targetZone: '1'
    disks: [
      {
        diskId: '<resourceId osdisk vm-app-01>'
        targetDiskType: 'Premium_LRS'
        replicaDiskType: 'Standard_LRS'
      }
    ]
  }
]

param recoveryPlans = [
  {
    name: 'rp-app-pro'
    bootGroups: [
      [
        'vm-sql-01'
      ]
      [
        'vm-app-01'
      ]
    ]
  }
]
```

Despliegue:

```powershell
New-AzResourceGroupDeployment -ResourceGroupName "<rg-asr-pro-destino>" -TemplateParameterFile "main.pro.bicepparam"
```

## Errores típicos

| Síntoma | Causa | Solución |
|---|---|---|
| El almacén no se puede usar para replicar VMs de su misma región | Entre regiones, el almacén y su grupo de recursos deben estar fuera de la región de origen | Almacén de ASR en destino (o zone-to-zone si eso es lo que se quiere) |
| Los Private Endpoints no funcionan en un almacén ya usado | Solo se pueden crear antes de registrar elementos | Almacén nuevo y PEs antes de la primera VM |
| Errores **151037** o **151072** | Sin salida a las URLs de ASR o DNS personalizado inaccesible (típico al reproteger) | Service tags en NSG/firewall y DNS alcanzable desde ambas regiones |
| Error **151196** | Sin salida a Entra ID (frecuente detrás de un balanceador interno Standard) | Regla `AzureActiveDirectory` o NAT Gateway |
| Error **151197** | Sin salida a los endpoints de ASR | Service tag `AzureSiteRecovery` |
| 151072 con proxy corporativo | Proxy con autenticación o mal detectado | Proxy sin autenticación en `ProxyInfo.conf` |
| Réplica en estado crítico tras endurecer la caché | Acceso público desactivado, soft delete activo o subredes de origen sin permiso | Firewall con servicios de confianza y subredes; sin soft delete |
| La caché falla tras desactivar la clave | La identidad del almacén no tiene los roles | *Contributor* + *Storage Blob Data Contributor/Owner* antes de desactivarla |
| RPO que crece y avisos de *Data change rate beyond supported limits* | Tasa de cambio por encima del límite o NVA saturado | High Churn, discos Premium o endpoint de servicio de Storage |
| No se puede proteger una VM con Premium SSD v2 o Ultra | Solo se replican con High Churn | Caché Premium block blob |
| Zone-to-zone rechazado | Discos ZRS o Ultra, o mismo grupo de recursos de destino | Discos LRS y otro grupo de recursos |
| El failover falla por capacidad | Sin reserva no hay capacidad garantizada en destino | Capacity Reservation u otro tamaño de destino |
| La VM conmutada arranca sin agentes ni permisos | Extensiones y RBAC no se replican | Recrearlos en el plan de recuperación (runbook) |
| El simulacro choca con producción | Se usó la red de recuperación | Red de simulacro aislada con el mismo direccionamiento |
| La reprotección falla | Faltan el mapeo inverso o las reglas de red en destino | Mapeos de ida y vuelta y reglas en ambas regiones |
| Un `apply` reinicia la réplica inicial de una VM | Cambio en un argumento que fuerza recreación | Revisar el `plan`; los cambios de destino, en el portal o PowerShell |
| `apply` agota el tiempo con Disk Encryption Set | La protección con DES puede durar hasta 5 horas | `timeouts { create = "5h" }` |
| Discos de réplica con acceso público | azurerm no expone el acceso de red de los discos | Cerrarlo por disco tras cancelar la exportación, o Bicep con `DenyAll` |
| La actualización automática del agente falla | Cuenta de Automation con Run As (retirada), en otra región o con Private Endpoints | Identidad gestionada, misma región que el almacén y sin PE |
| Restaurar la VM desde Azure Backup rompe la réplica | ASR no soporta restauraciones de disco o VM sobre un elemento replicado | Desactivar y reactivar la réplica tras restaurar |
| Comandos de ASR con Azure CLI | No está soportado | PowerShell, REST o portal |
