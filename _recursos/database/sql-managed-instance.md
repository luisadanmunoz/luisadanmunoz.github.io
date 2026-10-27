---
title: "SQL Managed Instance"
indice: database
resumen: "Compatibilidad casi total con SQL Server, gestionada."
estado: documentado   # proximamente | en-curso | documentado
orden: 2
last_review: 2026-10-27
fuentes:
  - titulo: "What is Azure SQL Managed Instance?"
    url: https://learn.microsoft.com/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview
  - titulo: "Features comparison: Azure SQL Database and Azure SQL Managed Instance"
    url: https://learn.microsoft.com/azure/azure-sql/database/features-comparison
  - titulo: "vCore purchasing model - Azure SQL Managed Instance"
    url: https://learn.microsoft.com/azure/azure-sql/managed-instance/service-tiers-managed-instance-vcore
  - titulo: "Use Next-gen General Purpose service tier"
    url: https://learn.microsoft.com/azure/azure-sql/managed-instance/service-tiers-next-gen-general-purpose-use
  - titulo: "Try Azure SQL Managed Instance for free"
    url: https://learn.microsoft.com/azure/azure-sql/managed-instance/free-offer
  - titulo: "Stop and start an instance - Azure SQL Managed Instance"
    url: https://learn.microsoft.com/azure/azure-sql/managed-instance/instance-stop-start-how-to
  - titulo: "Azure Hybrid Benefit - Azure SQL Database & SQL Managed Instance"
    url: https://learn.microsoft.com/azure/azure-sql/azure-hybrid-benefit
  - titulo: "Overview of business continuity with Azure SQL Managed Instance"
    url: https://learn.microsoft.com/azure/azure-sql/managed-instance/business-continuity-high-availability-disaster-recover-hadr-overview
  - titulo: "Configure a license-free standby replica for Azure SQL Managed Instance"
    url: https://learn.microsoft.com/azure/azure-sql/managed-instance/failover-group-standby-replica-how-to-configure
  - titulo: "Connectivity architecture for Azure SQL Managed Instance"
    url: https://learn.microsoft.com/azure/azure-sql/managed-instance/connectivity-architecture-overview
  - titulo: "Determine required subnet size and range for Azure SQL Managed Instance"
    url: https://learn.microsoft.com/azure/azure-sql/managed-instance/vnet-subnet-determine-size
  - titulo: "Enable service-aided subnet configuration for Azure SQL Managed Instance"
    url: https://learn.microsoft.com/azure/azure-sql/managed-instance/subnet-service-aided-configuration-enable
  - titulo: "Azure SQL Managed Instance connection types"
    url: https://learn.microsoft.com/azure/azure-sql/managed-instance/connection-types-overview
  - titulo: "Azure Private Link for Azure SQL Managed Instance"
    url: https://learn.microsoft.com/azure/azure-sql/managed-instance/private-endpoint-overview
  - titulo: "Availability through local and zone redundancy - Azure SQL Managed Instance"
    url: https://learn.microsoft.com/azure/azure-sql/managed-instance/high-availability-sla-local-zone-redundancy
  - titulo: "Configure zone redundancy - Azure SQL Managed Instance"
    url: https://learn.microsoft.com/azure/azure-sql/managed-instance/instance-zone-redundancy-configure
  - titulo: "Feature availability by region - Azure SQL Managed Instance"
    url: https://learn.microsoft.com/azure/azure-sql/managed-instance/region-availability
  - titulo: "Reliability in Azure SQL Managed Instance"
    url: https://learn.microsoft.com/azure/reliability/reliability-sql-managed-instance
  - titulo: "Automated backups in Azure SQL Managed Instance"
    url: https://learn.microsoft.com/azure/azure-sql/managed-instance/automated-backups-overview
  - titulo: "Manage Azure SQL Managed Instance long-term backup retention"
    url: https://learn.microsoft.com/azure/azure-sql/managed-instance/long-term-backup-retention-configure
  - titulo: "Failover groups overview & best practices - Azure SQL Managed Instance"
    url: https://learn.microsoft.com/azure/azure-sql/managed-instance/failover-group-sql-mi
  - titulo: "Configure a failover group for Azure SQL Managed Instance"
    url: https://learn.microsoft.com/azure/azure-sql/managed-instance/failover-group-configure-sql-mi
  - titulo: "Update policy in Azure SQL Managed Instance"
    url: https://learn.microsoft.com/azure/azure-sql/managed-instance/update-policy
  - titulo: "Maintenance window in Azure SQL Managed Instance"
    url: https://learn.microsoft.com/azure/azure-sql/managed-instance/maintenance-window
  - titulo: "Configure maintenance window in Azure SQL Managed Instance"
    url: https://learn.microsoft.com/azure/azure-sql/managed-instance/maintenance-window-configure
  - titulo: "Duration of management operations in Azure SQL Managed Instance"
    url: https://learn.microsoft.com/azure/azure-sql/managed-instance/management-operations-duration
  - titulo: "Overview of management operations in Azure SQL Managed Instance"
    url: https://learn.microsoft.com/azure/azure-sql/managed-instance/management-operations-overview
  - titulo: "Secure your Azure SQL Managed Instance"
    url: https://learn.microsoft.com/azure/azure-sql/managed-instance/secure-managed-instance
  - titulo: "Configure and manage Microsoft Entra authentication with Azure SQL"
    url: https://learn.microsoft.com/azure/azure-sql/database/authentication-aad-configure
  - titulo: "Directory Readers role in Microsoft Entra ID for Azure SQL"
    url: https://learn.microsoft.com/azure/azure-sql/database/authentication-aad-directory-readers-role
  - titulo: "Microsoft Entra-only authentication with Azure SQL"
    url: https://learn.microsoft.com/azure/azure-sql/database/authentication-azure-ad-only-authentication
  - titulo: "Azure SQL Transparent Data Encryption with customer-managed key"
    url: https://learn.microsoft.com/azure/azure-sql/database/transparent-data-encryption-byok-overview
  - titulo: "Scan your Azure SQL databases for vulnerabilities"
    url: https://learn.microsoft.com/azure/defender-for-cloud/sql-azure-vulnerability-assessment-overview
  - titulo: "Troubleshoot express and classic configuration"
    url: https://learn.microsoft.com/azure/defender-for-cloud/troubleshoot-vulnerability-findings
  - titulo: "SQL Server Audit in Azure SQL Managed Instance"
    url: https://learn.microsoft.com/azure/azure-sql/managed-instance/auditing
  - titulo: "Get started with Azure SQL Managed Instance auditing"
    url: https://learn.microsoft.com/azure/azure-sql/managed-instance/auditing-configure
  - titulo: "Monitor Azure SQL Managed Instance"
    url: https://learn.microsoft.com/azure/azure-sql/managed-instance/monitoring-sql-managed-instance-azure-monitor
  - titulo: "Supported logs for Microsoft.Sql/managedInstances"
    url: https://learn.microsoft.com/azure/azure-monitor/reference/supported-logs/microsoft-sql-managedinstances-logs
  - titulo: "Configure streaming export of diagnostic telemetry"
    url: https://learn.microsoft.com/azure/azure-sql/database/metrics-diagnostic-telemetry-logging-streaming-export-configure
  - titulo: "Azure built-in roles for Security"
    url: https://learn.microsoft.com/azure/role-based-access-control/built-in-roles/security
  - titulo: "azurerm_mssql_managed_instance"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/mssql_managed_instance
  - titulo: "azurerm_mssql_managed_instance_failover_group"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/mssql_managed_instance_failover_group
  - titulo: "azurerm_mssql_managed_database"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/mssql_managed_database
  - titulo: "Microsoft.Sql managedInstances (plantillas ARM/Bicep)"
    url: https://learn.microsoft.com/azure/templates/microsoft.sql/managedinstances
  - titulo: "Módulo Terraform Security/Seguridad/modules/monitor_diagnostic_setting"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Security/Seguridad/modules/monitor_diagnostic_setting
---

**Azure SQL Managed Instance** es el motor de SQL Server Enterprise como servicio, con compatibilidad casi total: SQL Server Agent, consultas y transacciones entre bases de datos, linked servers, CLR, Service Broker, Database Mail, replicación transaccional y CDC. Se despliega **dentro de una subred de tu VNet** y es de un solo inquilino, con cómputo y almacenamiento dedicados. Es el destino natural para llevar instancias de SQL Server a PaaS con pocos cambios. Si la aplicación no necesita funcionalidades de instancia, [Azure SQL Database](/recursos/database/azure-sql-database/) es más simple; si necesita el sistema operativo, [SQL Server en VM](/recursos/database/sql-server-en-vm/).

## Qué es y cuándo usarlo

### Niveles de servicio

| | **General Purpose** | **Next-gen General Purpose** | **Business Critical** |
|---|---|---|---|
| Para qué | La mayoría de cargas; nivel por defecto | Igual coste base, más rendimiento y capacidad | Latencia de IO baja (1-2 ms) y recuperación rápida |
| vCores máx. | 80 | 128 | 128 |
| Almacenamiento máx. | 16 TB | 32 TB | 16 TB |
| Bases de datos máx. | 100 | 500 | 100 |
| Réplicas | Nodos en espera | Nodos en espera | Tres réplicas, una de lectura incluida |
| Latencia de almacenamiento | 5-10 ms | Mejor que General Purpose (Elastic SAN) | 1-2 ms |
| Facturación | vCores, almacenamiento reservado y copias | Igual, más IOPS por encima de 3 por GB | vCores, almacenamiento reservado y copias; unas **2,7 veces** el cómputo de General Purpose |

Hardware: standard-series (Gen5, 5,1 GB por vCore), premium-series (7 GB por vCore, hasta 128 vCores) y premium-series memory optimized (13,6 GB por vCore, hasta 64). Next-gen General Purpose permite además **memoria flexible**.

El almacenamiento se reserva en **múltiplos de 32 GB** y se factura el máximo configurado. Las copias tienen gratis tanto espacio como el tamaño máximo de datos.

### Política de actualización

| Política | Qué implica |
|---|---|
| **SQL Server 2022** | Formato de bases alineado con SQL Server 2022: se puede restaurar una copia en SQL Server 2022 y hacer failover bidireccional con el link |
| **SQL Server 2025** (preview) | Lo mismo con SQL Server 2025 |
| **Always-up-to-date** | Todas las novedades en cuanto salen; se pierde la vuelta a SQL Server |

El cambio es **solo hacia arriba y sin vuelta atrás**. En un failover group, las dos instancias deben tener la misma política.

### Red

La instancia vive en una **subred exclusiva** delegada a `Microsoft.Sql/managedInstances`, con un **NSG y una tabla de rutas propios**. El servicio añade y mantiene sus reglas y rutas obligatorias (prefijo `Microsoft.Sql-managedInstances_UseOnly_mi-`) mediante una *network intent policy*, que impide cambios que las rompan.

| Decisión | Detalle |
|---|---|
| Tamaño de la subred | /27 como mínimo. Fórmula de Microsoft: `5 + (GP × 4) + (BC × 10) + (BC con zonas × 2) + (grupos de VM × 8)`. **El rango no se puede cambiar** con recursos dentro: mejor grande |
| Varias instancias | En la misma subred cuando la seguridad lo permita: la primera instancia de una subred es la que más tarda |
| NSG y tablas de rutas | Uno por subred delegada; reutilizarlos entre subredes de instancias con peering rompe la conectividad |
| Endpoint local de la VNet | Por defecto: `<instancia>.<zona-dns>.database.windows.net`, puerto 1433, resuelve a una IP de la subred |
| Tipo de conexión | **Redirect** por defecto desde octubre de 2025 (más rendimiento); exige permitir el 1433 hacia **todo el rango** de la subred. Proxy es el modo heredado |
| Endpoint público | `<instancia>.public.<zona-dns>...`, puerto 3342, siempre Proxy. Deshabilitado por defecto: mantenerlo así |
| Private endpoint | Subrecurso `managedInstance`, solo puerto 1433 y siempre Proxy. **El DNS no se registra solo**: zona `privatelink.<zona-dns>.database.windows.net` con un registro A si el private endpoint está en otra VNet (otro nombre de zona si está en la misma) |
| DNS | No sobrescribir `database.windows.net`, `core.windows.net`, `vault.azure.net`, `login.microsoftonline.com` y otros dominios de la plataforma |
| Azure Policy | No denegar `Microsoft.Network/networkIntentPolicies` ni las `serviceEndpointPolicies` que empiezan por `_e41f87a2_` |
| No soportado | NAT Gateway, cifrado de VNet, IPv6 y Microsoft peering de ExpressRoute en la VNet |

### Seguridad

| Control | Recomendación |
|---|---|
| Autenticación | **Solo Microsoft Entra**: deshabilita la autenticación SQL. Los logins de Entra son de instancia (`CREATE LOGIN ... FROM EXTERNAL PROVIDER`) |
| Identidad | La instancia **necesita el rol Directory Readers** (o los permisos de Graph equivalentes) para que funcione Entra. Con una identidad de usuario creada antes, un Privileged Role Administrator la autoriza una sola vez |
| Cifrado | TDE con clave del cliente: Key Vault con soft-delete y purge protection, y el rol Key Vault Crypto Service Encryption User para la identidad |
| Vulnerabilidades | Defender for SQL en la suscripción. La evaluación **express** en instancias exige la **identidad de sistema** activa |
| Auditoría | SQL Server Audit con `TO EXTERNAL_MONITOR` y diagnostic setting `SQLSecurityAuditEvents`. `DevOpsOperationsAudit` registra las operaciones del soporte de Microsoft |
| Conectividad interna | Cada 10 segundos el servicio prueba un login que falla (`AzureSQLConnectivityChecker`): esas entradas en la auditoría son normales |

### Disponibilidad y recuperación

| Capacidad | Detalle |
|---|---|
| Redundancia de zona | General Purpose y Business Critical, en regiones concretas (Spain Central, West Europe y North Europe, entre otras). Exige copias **ZRS o GZRS**, **tiene coste adicional** y se activa o desactiva en línea. En Next-gen General Purpose está en preview y depende de que Elastic SAN tenga ZRS en la región |
| Sin zonas | Una caída del centro de datos deja la instancia sin servicio hasta que se resuelva; solo queda el failover group o el geo-restore |
| Copias | PITR de 1 a 35 días, **GRS por defecto** (geo-restore activado). LTR hasta 10 años, **sin inmutabilidad** en Managed Instance. Las copias solo se restauran en instancias con la misma política de actualización o superior |
| Instancia borrada | Para recuperar bases, abrir un caso con soporte **en 5 días** |
| Failover groups | Exactamente **dos instancias** en regiones distintas, la secundaria vacía y en la **misma zona DNS** (se fija al crearla). VNets sin solapes y conectadas, puertos **5022 y 11000-11999** abiertos entre ambas. Mejor en regiones emparejadas (replicación más rápida). Política gestionada por el cliente recomendada |
| Lo que no replica | Las bases de sistema: logins, jobs del Agent y otros objetos de `master` y `msdb` se recrean y sincronizan a mano en la secundaria |
| Réplica standby | Secundaria solo para recuperación ante desastres: **sin coste de licencia** de sus vCores |
| Managed Instance link | Grupos de disponibilidad distribuidos con SQL Server: migración casi sin parada, recuperación ante desastres o lectura en Azure. Réplica pasiva sin licencia con *hybrid failover rights* |

### Mantenimiento y operaciones

- Por defecto, la mayoría de las actualizaciones se bloquean de 8:00 a 17:00 hora local. Las ventanas **Weekday** (22:00-6:00, lunes a jueves) y **Weekend** (22:00-6:00, viernes a domingo) son gratuitas, están disponibles en todas las regiones y se nombran `SQL_<Región>_MI_1` y `SQL_<Región>_MI_2`. En failover groups entre regiones no emparejadas, una ventana distinta en cada instancia.
- Crear una instancia: el 95 % termina en 30 minutos; **con zonas, hasta 4 horas**. Escalar vCores: hasta 60 minutos más la siembra de bases. Durante el cambio final la instancia no responde hasta 20 segundos en Business Critical y hasta 2 minutos en General Purpose.
- Borrar la última instancia de una subred elimina el clúster virtual (hasta 90 minutos); hasta entonces la subred no se puede borrar.

### Cómo se factura

| Concepto | Detalle |
|---|---|
| Cómputo y licencia | Por hora iniciada. **Parada y arranque** (solo General Purpose): parada no se paga ni cómputo ni licencia, solo almacenamiento. No se puede parar con zonas, en un failover group, con el link ni en un pool |
| Almacenamiento | Tamaño máximo configurado |
| Azure Hybrid Benefit | Licencias de SQL Server con Software Assurance |
| Reservas | Hasta un 80 % de ahorro |
| Instance pools | Ahorro cuando hay varias instancias (también con reservas) |
| Réplica standby | Sin licencia en la secundaria |
| Gratis | Una instancia General Purpose por suscripción durante 12 meses: 720 horas de vCore al mes, 4 u 8 vCores, 64 GB, sin SLA |

### Qué escenario recomiendo

| Escenario del cliente | Diseño | Por qué |
|---|---|---|
| Migrar instancias de SQL Server con Agent, cross-database o CLR | Managed Instance General Purpose; Managed Instance link o [Database Migration Service](/recursos/migrate-assessments/database-migration-service/) | Compatibilidad casi total con pocos cambios |
| OLTP crítico con IO de baja latencia | Business Critical redundante en zonas | SSD local, réplica de lectura y conmutación rápida |
| Muchas bases o más de 16 TB con presupuesto | Next-gen General Purpose | Hasta 500 bases y 32 TB al coste base de General Purpose |
| Desarrollo y pruebas | General Purpose con horario de parada | Sin cómputo ni licencia fuera de horario |
| Recuperación ante desastres regional | Failover group gestionado por el cliente con secundaria standby | Listener estable y sin licencia en la secundaria |
| Seguir con SQL Server en local y usar Azure | Managed Instance link | Réplica casi en tiempo real y conmutación en ambos sentidos con SQL Server 2022 o 2025 |
| La aplicación no usa funcionalidades de instancia | Azure SQL Database | Más sencillo y con Hyperscale y serverless |

### Datos que conviene llevar a la reunión

- **La subred se dimensiona al principio**: no se puede ampliar con instancias dentro.
- **Crear una instancia con zonas puede tardar hasta 4 horas.**
- **Sin el rol Directory Readers no funciona la autenticación de Entra**: hace falta un Privileged Role Administrator.
- **El cambio de política de actualización no tiene vuelta atrás** y condiciona las restauraciones en SQL Server.
- **Los logins y jobs del Agent no viajan con el failover group.**
- **Parar la instancia ahorra cómputo y licencia**, pero solo en General Purpose sin zonas ni failover group.
- **La secundaria standby no paga licencia.**
- **NAT Gateway no está soportado** en la subred de la instancia.

## Decisiones de diseño

| Decisión | Lo que aplico | Por qué |
|---|---|---|
| Recurso | `azurerm_mssql_managed_instance` nativo | El repositorio no tiene módulo de Managed Instance |
| Red | Subred, NSG y tabla de rutas como dependencia; sin endpoint público; Redirect | La red es de la landing zone; superficie mínima y mejor rendimiento |
| Autenticación | Solo Entra con un grupo como administrador; sin login ni contraseña SQL | Sin secretos en el código |
| Identidad | De usuario **creada antes** (con Directory Readers) más la de sistema | Entra funciona desde el primer momento; la de sistema la exige la evaluación express |
| Cifrado | Clave del cliente opcional, con el rol asignado antes y rotación automática | Control de la clave sin intervención manual |
| Zonas | Activadas por defecto; exigen copias ZRS o GZRS (validado) | Resiliencia ante la caída de una zona |
| Next-gen General Purpose | Validado que no se combine con zonas | El provider lo rechaza (en Azure está en preview) |
| Política de actualización | SQL Server 2022 por defecto | Mantiene la vuelta a SQL Server; el cambio es irreversible |
| Failover groups | Secundarias en un recurso aparte con la zona DNS de la primaria; gestionado por el cliente; standby opcional | La zona DNS solo se fija al crear |
| Bases de datos | Solo en primarias, con PITR y LTR | El failover group las replica |
| Parada y arranque | Solo General Purpose sin zonas ni failover group (validado) | Restricciones de la plataforma |
| Diagnóstico | `SQLSecurityAuditEvents`, `DevOpsOperationsAudit` y `ResourceUsageStats` en la instancia; rendimiento en cada base | Auditoría y telemetría en Log Analytics |

Alineación con el Well-Architected Framework:

- **Fiabilidad**: zonas, copias geo-zonales, failover group y ventana de mantenimiento.
- **Seguridad**: red privada, solo Entra, clave del cliente, auditoría y Defender.
- **Coste**: nivel según carga, Hybrid Benefit, reservas, parada fuera de horario y standby.
- **Excelencia operativa**: IaC con validaciones y diagnóstico centralizado.
- **Rendimiento**: Business Critical, Next-gen General Purpose y Redirect.

## Módulo de Terraform

### Los módulos del repositorio

El repositorio [AzureTerraformModules](https://github.com/luisadanmunoz/AzureTerraformModules) **no tiene módulo de SQL Managed Instance** (ninguno usa `azurerm_mssql_managed_instance`). Uso los recursos nativos y reutilizo [`Security/Seguridad/modules/monitor_diagnostic_setting`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Security/Seguridad/modules/monitor_diagnostic_setting).

Notas del provider (azurerm 4.81):

- `database_format` solo admite `SQLServer2022` y `AlwaysUpToDate`: **no tiene la política SQL Server 2025** (Bicep sí, con la API 2025-01-01).
- No hay recurso para la evaluación de vulnerabilidades **express** en instancias; `azurerm_mssql_managed_instance_vulnerability_assessment` usa la configuración clásica con cuenta de almacenamiento.
- `long_term_retention_policy.immutable_backups_enabled` de `azurerm_mssql_managed_database` está obsoleto: el propio provider lo describe como **no funcional**, coherente con que Managed Instance no admite copias inmutables.
- Rechaza la redundancia de zona en Next-gen General Purpose (`general_purpose_v2_enabled`).
- Los nombres de SKU del provider son `GP_Gen8IM` y `GP_Gen8IH`; la tabla de Learn usa `GP_G8IM` y `GP_G8IH`.
- `proxy_override = "Default"` ya equivale a Redirect en Azure; el root lo fija explícito.
- La primera identidad de usuario pasa a ser la identidad principal; `dns_zone_partner_id` y `timezone_id` solo se fijan al crear.

### Estructura en el proyecto

```txt
/
├── providers.tf             # azurerm >= 4.81.0
├── sql_managed_instance.tf  # instancias, TDE, diagnóstico, horario, bases de datos y failover groups
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
      # Validado con 4.81.0 (azurerm_mssql_managed_instance con database_format, hybrid_secondary_usage
      # y general_purpose_v2_enabled; azurerm_mssql_managed_instance_failover_group con secondary_type).
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

### `sql_managed_instance.tf`

```hcl
# =============================================================================
# Azure SQL Managed Instance segura por defecto:
# instancia en una subred delegada, solo autenticación Microsoft Entra, sin endpoint público,
# conexión Redirect, redundancia de zona con copias ZRS, TDE con clave del cliente opcional,
# ventana de mantenimiento, diagnóstico y auditoría a Log Analytics; bases de datos con retención
# corta y larga, horario de parada y arranque opcional y failover groups gestionados por el cliente
#
# DEPENDENCY: grupos de recursos creados
# DEPENDENCY: subred exclusiva (/27 como mínimo; dimensionarla con la fórmula de Microsoft) delegada a
#             Microsoft.Sql/managedInstances, con NSG y tabla de rutas propios asociados
# DEPENDENCY: Azure Policy no debe denegar Microsoft.Network/networkIntentPolicies ni las
#             serviceEndpointPolicies que gestiona el servicio
# DEPENDENCY: identidad de usuario creada ANTES, con el rol Directory Readers (o los permisos de
#             Microsoft Graph equivalentes) concedido por un Privileged Role Administrator: sin él,
#             la autenticación de Entra no funciona
# DEPENDENCY: grupo de Microsoft Entra para el administrador de la instancia
# DEPENDENCY: TDE con clave del cliente: Key Vault con soft-delete y purge protection
# DEPENDENCY: failover group: VNets sin solapes y conectadas (peering global), puertos 5022 y
#             11000-11999 abiertos entre ambas subredes, instancia secundaria vacía
# DEPENDENCY: Microsoft Defender for SQL en la suscripción (amenazas y evaluación de vulnerabilidades)
# DEPENDENCY: Log Analytics para diagnóstico y auditoría
# =============================================================================

variable "sql_managed_instances" {
  description = "Instancias administradas (clave = nombre de la instancia)."
  type = map(object({
    resource_group_name = string
    location            = string
    subnet_id           = string # delegada a Microsoft.Sql/managedInstances, con NSG y tabla de rutas

    sku_name                 = optional(string, "GP_Gen5") # GP_Gen5 | GP_Gen8IM | GP_Gen8IH | BC_Gen5 | BC_Gen8IM | BC_Gen8IH
    vcores                   = number
    storage_size_in_gb       = number                # múltiplo de 32
    next_gen_general_purpose = optional(bool, false) # Next-gen General Purpose (Elastic SAN)
    storage_iops             = optional(number)      # solo Next-gen General Purpose

    license_type              = optional(string, "LicenseIncluded") # BasePrice = Azure Hybrid Benefit
    hybrid_secondary_usage    = optional(string, "Active")          # Passive = réplica DR sin licencia (link con SQL Server)
    zone_redundant            = optional(bool, true)
    backup_storage_redundancy = optional(string, "ZRS")           # GRS | GZRS | ZRS | LRS
    update_policy             = optional(string, "SQLServer2022") # SQLServer2022 | AlwaysUpToDate (sin vuelta atrás)
    connection_type           = optional(string, "Redirect")
    maintenance_window        = optional(string, "SQL_Default") # SQL_Default | SQL_<Región>_MI_1 | SQL_<Región>_MI_2
    timezone_id               = optional(string, "UTC")         # solo al crear
    collation                 = optional(string, "SQL_Latin1_General_CP1_CI_AS")

    # Solo Microsoft Entra: sin login ni contraseña SQL
    entra_admin = object({
      login_username = string
      object_id      = string
      principal_type = optional(string, "Group")
    })

    # Identidad de usuario creada antes y con Directory Readers
    identity = object({
      id           = string
      principal_id = string
    })

    tde_customer_managed_key = optional(object({
      key_vault_id          = string
      key_vault_key_id      = string # con o sin versión
      auto_rotation_enabled = optional(bool, true)
    }))

    # Secundaria de un failover group: clave de la instancia primaria (comparte su zona DNS)
    dns_zone_partner = optional(string)

    # Solo General Purpose sin redundancia de zona ni failover group
    start_stop_schedule = optional(object({
      timezone_id = optional(string, "UTC")
      schedules = list(object({
        start_day  = string
        start_time = string # HH:mm
        stop_day   = string
        stop_time  = string
      }))
    }))

    log_analytics_workspace_id = string
    tags                       = optional(map(string), {})
  }))
  default = {}

  validation {
    condition     = alltrue([for k, v in var.sql_managed_instances : can(regex("^[0-9a-z]([-0-9a-z]{0,61}[0-9a-z])?$", k))])
    error_message = "Nombre: minúsculas, números y guiones; sin guion al principio ni al final; 63 caracteres como máximo."
  }
  validation {
    condition     = alltrue([for v in values(var.sql_managed_instances) : contains(["GP_Gen5", "GP_Gen8IM", "GP_Gen8IH", "BC_Gen5", "BC_Gen8IM", "BC_Gen8IH"], v.sku_name)])
    error_message = "sku_name: GP_Gen5, GP_Gen8IM, GP_Gen8IH, BC_Gen5, BC_Gen8IM o BC_Gen8IH."
  }
  validation {
    condition = alltrue([for v in values(var.sql_managed_instances) : (
      v.storage_size_in_gb >= 32 && v.storage_size_in_gb % 32 == 0 &&
      v.storage_size_in_gb <= (v.next_gen_general_purpose ? 32768 : 16384)
    )])
    error_message = "storage_size_in_gb: múltiplo de 32; hasta 16 TB (32 TB en Next-gen General Purpose)."
  }
  validation {
    condition = alltrue([for v in values(var.sql_managed_instances) : (
      startswith(v.sku_name, "BC_") ? !v.next_gen_general_purpose : true
      ) && (
      v.storage_iops == null ? true : v.next_gen_general_purpose
      ) && (
      startswith(v.sku_name, "GP_") && !v.next_gen_general_purpose ? v.vcores <= 80 : true
    )])
    error_message = "Next-gen e IOPS solo en General Purpose; General Purpose clásico hasta 80 vCores."
  }
  validation {
    condition     = alltrue([for v in values(var.sql_managed_instances) : !(v.zone_redundant && v.next_gen_general_purpose)])
    error_message = "La redundancia de zona de Next-gen General Purpose está en preview y el provider la rechaza."
  }
  validation {
    condition     = alltrue([for v in values(var.sql_managed_instances) : v.zone_redundant ? contains(["ZRS", "GZRS"], v.backup_storage_redundancy) : contains(["GRS", "GZRS", "ZRS", "LRS"], v.backup_storage_redundancy)])
    error_message = "Con redundancia de zona las copias deben ser ZRS o GZRS."
  }
  validation {
    condition = alltrue([for v in values(var.sql_managed_instances) : (
      contains(["SQLServer2022", "AlwaysUpToDate"], v.update_policy) &&
      contains(["Redirect", "Proxy"], v.connection_type) &&
      contains(["LicenseIncluded", "BasePrice"], v.license_type) &&
      contains(["Active", "Passive"], v.hybrid_secondary_usage) &&
      contains(["Group", "User", "Application"], v.entra_admin.principal_type) &&
      can(regex("^(SQL_Default|SQL_[A-Za-z0-9]+_MI_[0-9]+)$", v.maintenance_window))
    )])
    error_message = "Revisa update_policy, connection_type, license_type, hybrid_secondary_usage, entra_admin.principal_type o maintenance_window."
  }
  validation {
    condition = alltrue([for v in values(var.sql_managed_instances) : v.start_stop_schedule == null ? true : (
      startswith(v.sku_name, "GP_") && !v.zone_redundant
    )])
    error_message = "El horario de parada y arranque solo existe en General Purpose sin redundancia de zona."
  }
  validation {
    condition = alltrue([for v in values(var.sql_managed_instances) : v.tde_customer_managed_key == null ? true : can(
      regex("^https://[a-z0-9-]+\\.vault\\.azure\\.net/keys/[A-Za-z0-9-]+(/[a-f0-9]{32})?$", v.tde_customer_managed_key.key_vault_key_id)
    )])
    error_message = "tde_customer_managed_key.key_vault_key_id debe ser el identificador de una clave de Key Vault."
  }
}

variable "sql_managed_databases" {
  description = "Bases de datos de las instancias (clave = <instancia>/<base de datos>)."
  type = map(object({
    short_term_retention_days = optional(number, 7) # 1-35
    long_term_retention = optional(object({
      weekly_retention  = optional(string, "PT0S") # ISO 8601: P4W, P12M, P10Y...
      monthly_retention = optional(string, "PT0S")
      yearly_retention  = optional(string, "PT0S")
      week_of_year      = optional(number, 1)
    }))
    diagnostic_log_categories = optional(list(string), ["SQLInsights", "QueryStoreRuntimeStatistics", "QueryStoreWaitStatistics", "Errors"])
    tags                      = optional(map(string), {})
  }))
  default = {}

  validation {
    condition     = alltrue([for k, v in var.sql_managed_databases : length(split("/", k)) == 2 && v.short_term_retention_days >= 1 && v.short_term_retention_days <= 35])
    error_message = "Clave <instancia>/<base de datos>; short_term_retention_days de 1 a 35."
  }
}

variable "sql_managed_instance_failover_groups" {
  description = "Failover groups entre instancias (clave = nombre del grupo)."
  type = map(object({
    instance                  = string                     # clave de la instancia primaria
    partner_instance          = string                     # clave de la secundaria (con dns_zone_partner = instance)
    failover_mode             = optional(string, "Manual") # recomendado: gestionado por el cliente
    grace_minutes             = optional(number)           # solo Automatic, 60 o más
    secondary_type            = optional(string, "Geo")    # Standby = sin licencia si solo es DR
    readonly_failover_enabled = optional(bool, false)
  }))
  default = {}

  validation {
    condition = alltrue([for v in values(var.sql_managed_instance_failover_groups) : (
      contains(["Geo", "Standby"], v.secondary_type) &&
      (v.failover_mode == "Manual" ? v.grace_minutes == null : v.failover_mode == "Automatic" && coalesce(v.grace_minutes, 0) >= 60)
    )])
    error_message = "secondary_type Geo o Standby; failover_mode Manual (sin grace_minutes) o Automatic con grace_minutes >= 60."
  }
}

# -----------------------------------------------------------------------------
# Clave del cliente: rol para envolver y desenvolver la DEK antes de crear la instancia
# -----------------------------------------------------------------------------
resource "azurerm_role_assignment" "sqlmi_tde" {
  for_each = { for k, v in var.sql_managed_instances : k => v if v.tde_customer_managed_key != null }

  scope                            = each.value.tde_customer_managed_key.key_vault_id
  role_definition_name             = "Key Vault Crypto Service Encryption User"
  principal_id                     = each.value.identity.principal_id
  principal_type                   = "ServicePrincipal"
  skip_service_principal_aad_check = true
  description                      = "TDE con clave del cliente de ${each.key}"
}

# -----------------------------------------------------------------------------
# Instancias (recurso nativo: el repositorio no tiene módulo de SQL Managed Instance).
# Las secundarias de un failover group se crean aparte para heredar la zona DNS de la primaria.
# -----------------------------------------------------------------------------
resource "azurerm_mssql_managed_instance" "primary" {
  for_each = { for k, v in var.sql_managed_instances : k => v if v.dns_zone_partner == null }

  name                = each.key
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  subnet_id           = each.value.subnet_id

  sku_name                       = each.value.sku_name
  vcores                         = each.value.vcores
  storage_size_in_gb             = each.value.storage_size_in_gb
  general_purpose_v2_enabled     = each.value.next_gen_general_purpose
  storage_iops                   = each.value.storage_iops
  license_type                   = each.value.license_type
  hybrid_secondary_usage         = each.value.hybrid_secondary_usage
  zone_redundant_enabled         = each.value.zone_redundant
  storage_account_type           = each.value.backup_storage_redundancy
  database_format                = each.value.update_policy
  proxy_override                 = each.value.connection_type
  public_data_endpoint_enabled   = false
  minimum_tls_version            = "1.2"
  maintenance_configuration_name = each.value.maintenance_window
  timezone_id                    = each.value.timezone_id
  collation                      = each.value.collation

  azure_active_directory_administrator {
    login_username                      = each.value.entra_admin.login_username
    object_id                           = each.value.entra_admin.object_id
    principal_type                      = each.value.entra_admin.principal_type
    azuread_authentication_only_enabled = true
  }

  # Identidad de sistema: la exige la evaluación de vulnerabilidades express en instancias
  identity {
    type         = "SystemAssigned, UserAssigned"
    identity_ids = [each.value.identity.id]
  }

  tags = merge(var.tags, each.value.tags)

  depends_on = [azurerm_role_assignment.sqlmi_tde]
}

resource "azurerm_mssql_managed_instance" "secondary" {
  for_each = { for k, v in var.sql_managed_instances : k => v if v.dns_zone_partner != null }

  name                = each.key
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  subnet_id           = each.value.subnet_id

  sku_name                       = each.value.sku_name
  vcores                         = each.value.vcores
  storage_size_in_gb             = each.value.storage_size_in_gb
  general_purpose_v2_enabled     = each.value.next_gen_general_purpose
  storage_iops                   = each.value.storage_iops
  license_type                   = each.value.license_type
  hybrid_secondary_usage         = each.value.hybrid_secondary_usage
  zone_redundant_enabled         = each.value.zone_redundant
  storage_account_type           = each.value.backup_storage_redundancy
  database_format                = each.value.update_policy
  proxy_override                 = each.value.connection_type
  public_data_endpoint_enabled   = false
  minimum_tls_version            = "1.2"
  maintenance_configuration_name = each.value.maintenance_window
  timezone_id                    = each.value.timezone_id
  collation                      = each.value.collation
  dns_zone_partner_id            = azurerm_mssql_managed_instance.primary[each.value.dns_zone_partner].id

  azure_active_directory_administrator {
    login_username                      = each.value.entra_admin.login_username
    object_id                           = each.value.entra_admin.object_id
    principal_type                      = each.value.entra_admin.principal_type
    azuread_authentication_only_enabled = true
  }

  # Identidad de sistema: la exige la evaluación de vulnerabilidades express en instancias
  identity {
    type         = "SystemAssigned, UserAssigned"
    identity_ids = [each.value.identity.id]
  }

  tags = merge(var.tags, each.value.tags)

  depends_on = [azurerm_role_assignment.sqlmi_tde]

  lifecycle {
    precondition {
      condition     = contains(keys(var.sql_managed_instances), each.value.dns_zone_partner) && try(var.sql_managed_instances[each.value.dns_zone_partner].dns_zone_partner, null) == null
      error_message = "dns_zone_partner debe ser la clave de una instancia primaria."
    }
    precondition {
      condition     = var.sql_managed_instances[each.value.dns_zone_partner].update_policy == each.value.update_policy
      error_message = "Las instancias de un failover group deben tener la misma update policy."
    }
  }
}

# Clave del cliente como protector TDE de la instancia (rotación automática por defecto)
resource "azurerm_mssql_managed_instance_transparent_data_encryption" "this" {
  for_each = { for k, v in var.sql_managed_instances : k => v if v.tde_customer_managed_key != null }

  managed_instance_id   = merge(azurerm_mssql_managed_instance.primary, azurerm_mssql_managed_instance.secondary)[each.key].id
  key_vault_key_id      = each.value.tde_customer_managed_key.key_vault_key_id
  auto_rotation_enabled = each.value.tde_customer_managed_key.auto_rotation_enabled
}

# Diagnóstico y auditoría (SQLSecurityAuditEvents recibe la auditoría creada con TO EXTERNAL_MONITOR)
module "sqlmi_diagnostics" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Security/Seguridad/modules/monitor_diagnostic_setting?ref=main"
  for_each = var.sql_managed_instances

  monitor_diagnostic_setting_name = "diag-${each.key}"
  target_resource_id              = merge(azurerm_mssql_managed_instance.primary, azurerm_mssql_managed_instance.secondary)[each.key].id
  log_analytics_workspace_id      = each.value.log_analytics_workspace_id
  enabled_logs = [
    { category = "SQLSecurityAuditEvents" },
    { category = "DevOpsOperationsAudit" },
    { category = "ResourceUsageStats" }
  ]
  enabled_metrics = [{ category = "AllMetrics" }]
}

resource "azurerm_mssql_managed_instance_start_stop_schedule" "this" {
  for_each = { for k, v in var.sql_managed_instances : k => v if v.start_stop_schedule != null }

  managed_instance_id = merge(azurerm_mssql_managed_instance.primary, azurerm_mssql_managed_instance.secondary)[each.key].id
  timezone_id         = each.value.start_stop_schedule.timezone_id
  description         = "Parada fuera de horario de ${each.key}"

  dynamic "schedule" {
    for_each = each.value.start_stop_schedule.schedules
    content {
      start_day  = schedule.value.start_day
      start_time = schedule.value.start_time
      stop_day   = schedule.value.stop_day
      stop_time  = schedule.value.stop_time
    }
  }
}

# -----------------------------------------------------------------------------
# Bases de datos (solo en primarias: el failover group las replica en la secundaria)
# -----------------------------------------------------------------------------
resource "azurerm_mssql_managed_database" "this" {
  for_each = var.sql_managed_databases

  name                      = split("/", each.key)[1]
  managed_instance_id       = try(azurerm_mssql_managed_instance.primary[split("/", each.key)[0]].id, null)
  short_term_retention_days = each.value.short_term_retention_days

  dynamic "long_term_retention_policy" {
    for_each = each.value.long_term_retention == null ? [] : [each.value.long_term_retention]
    content {
      weekly_retention  = long_term_retention_policy.value.weekly_retention
      monthly_retention = long_term_retention_policy.value.monthly_retention
      yearly_retention  = long_term_retention_policy.value.yearly_retention
      week_of_year      = long_term_retention_policy.value.week_of_year
    }
  }

  tags = merge(var.tags, each.value.tags)

  lifecycle {
    precondition {
      condition     = try(var.sql_managed_instances[split("/", each.key)[0]].dns_zone_partner, "x") == null
      error_message = "Las bases de datos se declaran en una instancia primaria (no secundaria de un failover group)."
    }
  }
}

module "sqlmi_database_diagnostics" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Security/Seguridad/modules/monitor_diagnostic_setting?ref=main"
  for_each = var.sql_managed_databases

  monitor_diagnostic_setting_name = "diag-${replace(each.key, "/", "-")}"
  target_resource_id              = azurerm_mssql_managed_database.this[each.key].id
  log_analytics_workspace_id      = var.sql_managed_instances[split("/", each.key)[0]].log_analytics_workspace_id
  enabled_logs                    = [for c in each.value.diagnostic_log_categories : { category = c }]
}

# -----------------------------------------------------------------------------
# Failover groups
# -----------------------------------------------------------------------------
resource "azurerm_mssql_managed_instance_failover_group" "this" {
  for_each = var.sql_managed_instance_failover_groups

  name                        = each.key
  location                    = var.sql_managed_instances[each.value.instance].location
  managed_instance_id         = azurerm_mssql_managed_instance.primary[each.value.instance].id
  partner_managed_instance_id = azurerm_mssql_managed_instance.secondary[each.value.partner_instance].id
  secondary_type              = each.value.secondary_type

  read_write_endpoint_failover_policy {
    mode          = each.value.failover_mode
    grace_minutes = each.value.grace_minutes
  }
  readonly_endpoint_failover_policy_enabled = each.value.readonly_failover_enabled

  depends_on = [azurerm_mssql_managed_database.this]

  lifecycle {
    precondition {
      condition     = var.sql_managed_instances[each.value.partner_instance].dns_zone_partner == each.value.instance
      error_message = "La secundaria debe declarar dns_zone_partner = la instancia primaria."
    }
    precondition {
      condition     = var.sql_managed_instances[each.value.instance].location != var.sql_managed_instances[each.value.partner_instance].location
      error_message = "Las instancias de un failover group deben estar en regiones distintas."
    }
    precondition {
      condition     = alltrue([for i in [each.value.instance, each.value.partner_instance] : var.sql_managed_instances[i].start_stop_schedule == null])
      error_message = "Una instancia en un failover group no se puede parar: quita start_stop_schedule."
    }
  }
}

# Avisos (no bloquean)
check "failover_group_same_size" {
  assert {
    condition = alltrue([for v in values(var.sql_managed_instance_failover_groups) : (
      var.sql_managed_instances[v.instance].sku_name == var.sql_managed_instances[v.partner_instance].sku_name &&
      var.sql_managed_instances[v.instance].vcores == var.sql_managed_instances[v.partner_instance].vcores &&
      var.sql_managed_instances[v.instance].storage_size_in_gb == var.sql_managed_instances[v.partner_instance].storage_size_in_gb
    )])
    error_message = "Microsoft recomienda el mismo nivel, vCores y almacenamiento en primaria y secundaria."
  }
}

output "sql_managed_instance_ids" {
  value = { for k, v in merge(azurerm_mssql_managed_instance.primary, azurerm_mssql_managed_instance.secondary) : k => v.id }
}

output "sql_managed_instance_fqdns" {
  description = "Endpoint local de la VNet: <instancia>.<zona DNS>.database.windows.net"
  value       = { for k, v in merge(azurerm_mssql_managed_instance.primary, azurerm_mssql_managed_instance.secondary) : k => v.fqdn }
}

output "sql_managed_instance_dns_zones" {
  value = { for k, v in merge(azurerm_mssql_managed_instance.primary, azurerm_mssql_managed_instance.secondary) : k => v.dns_zone }
}

output "sql_managed_instance_system_identities" {
  description = "Identidad de sistema (la usa la evaluación de vulnerabilidades express)."
  value       = { for k, v in merge(azurerm_mssql_managed_instance.primary, azurerm_mssql_managed_instance.secondary) : k => try(v.identity[0].principal_id, null) }
}

output "sql_managed_instance_failover_group_listeners" {
  value = {
    for k, v in azurerm_mssql_managed_instance_failover_group.this : k => {
      read_write = "${k}.${azurerm_mssql_managed_instance.primary[var.sql_managed_instance_failover_groups[k].instance].dns_zone}.database.windows.net"
      read_only  = "${k}.secondary.${azurerm_mssql_managed_instance.primary[var.sql_managed_instance_failover_groups[k].instance].dns_zone}.database.windows.net"
    }
  }
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

sql_managed_instances = {
  "sqlmi-workload-pro-01" = {
    resource_group_name = "<rg-workload-pro>"
    location            = "<región-primaria>"
    subnet_id           = "<resourceId snet-sqlmi-pro (delegada, con NSG y tabla de rutas)>"

    sku_name           = "BC_Gen5"
    vcores             = 8
    storage_size_in_gb = 512

    zone_redundant            = true
    backup_storage_redundancy = "GZRS"              # zonas en la región y geo-restore
    maintenance_window        = "<SQL_Región_MI_2>" # Weekend

    entra_admin = {
      login_username = "<grupo sqlmi-admins-pro>"
      object_id      = "<objectId del grupo>"
    }

    identity = {
      id           = "<resourceId id-sqlmi-workload-pro (con Directory Readers)>"
      principal_id = "<principalId de la identidad>"
    }

    tde_customer_managed_key = {
      key_vault_id     = "<resourceId kv-workload-pro>"
      key_vault_key_id = "<https://kv-workload-pro.vault.azure.net/keys/tde-sqlmi>"
    }

    log_analytics_workspace_id = "<resourceId log-platform-pro>"
  }

  # Secundaria del failover group: misma configuración, otra región, vacía y en la zona DNS de la primaria
  "sqlmi-workload-pro-dr-01" = {
    resource_group_name = "<rg-workload-pro-dr>"
    location            = "<región-secundaria>"
    subnet_id           = "<resourceId snet-sqlmi-pro-dr (delegada, con NSG y tabla de rutas)>"
    dns_zone_partner    = "sqlmi-workload-pro-01"

    sku_name                  = "BC_Gen5"
    vcores                    = 8
    storage_size_in_gb        = 512
    zone_redundant            = true
    backup_storage_redundancy = "GZRS"
    maintenance_window        = "<SQL_RegiónDR_MI_1>" # Weekday: distinta de la primaria

    entra_admin = {
      login_username = "<grupo sqlmi-admins-pro>"
      object_id      = "<objectId del grupo>"
    }

    identity = {
      id           = "<resourceId id-sqlmi-workload-pro-dr (con Directory Readers)>"
      principal_id = "<principalId de la identidad>"
    }

    # Ambas instancias deben poder abrir la clave
    tde_customer_managed_key = {
      key_vault_id     = "<resourceId kv-workload-pro>"
      key_vault_key_id = "<https://kv-workload-pro.vault.azure.net/keys/tde-sqlmi>"
    }

    log_analytics_workspace_id = "<resourceId log-platform-pro>"
  }
}

sql_managed_databases = {
  "sqlmi-workload-pro-01/erp" = {
    short_term_retention_days = 35
    long_term_retention = {
      weekly_retention  = "P5W"
      monthly_retention = "P12M"
      yearly_retention  = "P10Y"
      week_of_year      = 1
    }
  }
  "sqlmi-workload-pro-01/staging" = {}
}

sql_managed_instance_failover_groups = {
  "fog-sqlmi-workload-pro" = {
    instance         = "sqlmi-workload-pro-01"
    partner_instance = "sqlmi-workload-pro-dr-01"
    secondary_type   = "Standby" # solo recuperación ante desastres: sin coste de licencia
  }
}
```

### Despliegue y comprobación

Antes del despliegue, la identidad de usuario necesita el rol Directory Readers. Lo concede un Privileged Role Administrator; en producción, mejor a través de un grupo con asignación de roles:

```powershell
Connect-MgGraph -Scopes "RoleManagement.ReadWrite.Directory"
$role = Get-MgDirectoryRole -Filter "DisplayName eq 'Directory Readers'"
$msi  = Get-MgServicePrincipal -Filter "DisplayName eq 'id-sqlmi-workload-pro'"
New-MgDirectoryRoleMemberByRef -DirectoryRoleId $role.Id `
    -BodyParameter @{ "@odata.id" = "https://graph.microsoft.com/v1.0/directoryObjects/$($msi.Id)" }
```

```powershell
terraform init
terraform plan -var-file="env/pro.tfvars" -out="pro.tfplan"
terraform apply "pro.tfplan"   # la primera instancia de una subred puede tardar horas

# Ventanas de mantenimiento disponibles en la región
Get-AzMaintenancePublicConfiguration |
    Where-Object { $_.Location -eq "<región>" -and $_.MaintenanceScope -eq "SQLManagedInstance" } |
    Select-Object Name, Location

# Configuración de la instancia
Get-AzSqlInstance -ResourceGroupName "<rg-workload-pro>" -Name "sqlmi-workload-pro-01" |
    Select-Object ManagedInstanceName, FullyQualifiedDomainName, Sku, VCores, ZoneRedundant,
        ProxyOverride, PublicDataEndpointEnabled, DatabaseFormat, BackupStorageRedundancy

# Failover group
Get-AzSqlDatabaseInstanceFailoverGroup -ResourceGroupName "<rg-workload-pro>" -Location "<región>"
```

Después del despliegue, la auditoría a Log Analytics se activa con T-SQL desde una sesión de Entra:

```sql
CREATE SERVER AUDIT [audit-azure-monitor] TO EXTERNAL_MONITOR;
GO
CREATE SERVER AUDIT SPECIFICATION [audit-spec-logins]
FOR SERVER AUDIT [audit-azure-monitor]
    ADD (SUCCESSFUL_LOGIN_GROUP),
    ADD (FAILED_LOGIN_GROUP)
WITH (STATE = ON);
GO
ALTER SERVER AUDIT [audit-azure-monitor] WITH (STATE = ON);
GO

-- Logins de Entra a nivel de instancia
CREATE LOGIN [grp-erp-app] FROM EXTERNAL PROVIDER;
SELECT SERVERPROPERTY('ProductUpdateType'); -- CU = política SQL Server 2022/2025; Continuous = Always-up-to-date
```

Consultas en Log Analytics (todas las categorías van a `AzureDiagnostics`):

```kusto
// Eventos de auditoría por hora
AzureDiagnostics
| where Category == "SQLSecurityAuditEvents"
| summarize count() by bin(TimeGenerated, 1h), Resource

// Instancias con CPU por encima del 95 % en la última hora
AzureDiagnostics
| where Category == "ResourceUsageStats" and TimeGenerated > ago(1h)
| summarize avg_cpu = max(todouble(avg_cpu_percent_s)) by _ResourceId
| where avg_cpu > 95

// Ocupación del almacenamiento reservado
AzureDiagnostics
| where Category == "ResourceUsageStats"
| summarize arg_max(TimeGenerated, todouble(storage_space_used_mb_s) * 100 / todouble(reserved_storage_mb_s)) by _ResourceId
```

### Equivalente en Bicep

Una plantilla por instancia. La secundaria se despliega después de la primaria con `dnsZonePartnerId`. El rol sobre el Key Vault usa `role-on-resource.bicep`, el mismo de las fichas anteriores. La API `2025-01-01` admite la política SQL Server 2025.

`sqlmi.bicep`:

```bicep
// =============================================================================
// Azure SQL Managed Instance segura por defecto: subred delegada, solo Microsoft Entra, sin endpoint
// público, Redirect, redundancia de zona con copias ZRS/GZRS, TDE con clave del cliente opcional,
// ventana de mantenimiento, diagnóstico y auditoría a Log Analytics, bases de datos con retención,
// horario de parada opcional (General Purpose) y failover group gestionado por el cliente
// DEPENDENCY: subred delegada a Microsoft.Sql/managedInstances con NSG y tabla de rutas propios
// DEPENDENCY: identidad de usuario creada antes y con Directory Readers
// DEPENDENCY: secundaria de un failover group: se despliega después de la primaria (dnsZonePartnerId)
// DEPENDENCY: role-on-resource.bicep en la misma carpeta
// =============================================================================
@minLength(1)
@maxLength(63)
param name string
param location string = resourceGroup().location
param subnetId string

@allowed(['GP_Gen5', 'GP_G8IM', 'GP_G8IH', 'BC_Gen5', 'BC_G8IM', 'BC_G8IH'])
param skuName string = 'GP_Gen5'
param vCores int
@description('Múltiplo de 32')
param storageSizeInGB int
param nextGenGeneralPurpose bool = false

@allowed(['LicenseIncluded', 'BasePrice'])
param licenseType string = 'LicenseIncluded'
@allowed(['Active', 'Passive'])
param hybridSecondaryUsage string = 'Active'
param zoneRedundant bool = true
@allowed(['GRS', 'GZRS', 'ZRS', 'LRS'])
param backupStorageRedundancy string = 'ZRS'
@allowed(['SQLServer2022', 'SQLServer2025', 'AlwaysUpToDate'])
param updatePolicy string = 'SQLServer2022'
@allowed(['Redirect', 'Proxy'])
param connectionType string = 'Redirect'
@description('SQL_Default | SQL_<Región>_MI_1 | SQL_<Región>_MI_2')
param maintenanceWindow string = 'SQL_Default'
param timezoneId string = 'UTC'

@description('{ loginName, objectId, principalType: Group|User|Application }')
param entraAdmin object

@description('Identidad de usuario creada antes y con Directory Readers')
param userAssignedIdentityId string
param userAssignedIdentityPrincipalId string

@description('{ keyVaultId, keyVaultKeyId (con versión) }; vacío = clave del servicio')
param tdeCustomerManagedKey object = {}

@description('ID de la instancia primaria si esta es la secundaria de un failover group')
param dnsZonePartnerId string = ''

@description('{ timezoneId, schedules: [{ startDay, startTime, stopDay, stopTime }] }; solo General Purpose sin zonas')
param startStopSchedule object = {}

param logAnalyticsWorkspaceId string

@description('[{ name, retentionDays?, ltr?: { weekly?, monthly?, yearly?, weekOfYear? } }]')
param databases array = []

@description('[{ name, partnerManagedInstanceId, partnerRegion, failoverMode? (Manual), graceMinutes?, secondaryType? (Geo|Standby), readOnlyFailover? }]')
param failoverGroups array = []

param tags object = {}

var useCmk = !empty(tdeCustomerManagedKey)

module tdeRole 'role-on-resource.bicep' = if (useCmk) {
  name: '${take(name, 45)}-tde-role'
  scope: resourceGroup(
    split(tdeCustomerManagedKey.?keyVaultId ?? '/s/x/r/x', '/')[2],
    split(tdeCustomerManagedKey.?keyVaultId ?? '/s/x/r/x', '/')[4]
  )
  params: {
    resourceId: tdeCustomerManagedKey.keyVaultId
    roleDefinitionId: 'e147488a-f6f5-4113-8e2d-b22465e65bf6' // Key Vault Crypto Service Encryption User
    principalId: userAssignedIdentityPrincipalId
    description: 'TDE con clave del cliente de ${name}'
  }
}

resource instance 'Microsoft.Sql/managedInstances@2025-01-01' = {
  name: name
  location: location
  tags: tags
  sku: {
    name: skuName
  }
  identity: {
    type: 'SystemAssigned,UserAssigned'
    userAssignedIdentities: {
      '${userAssignedIdentityId}': {}
    }
  }
  properties: {
    subnetId: subnetId
    vCores: vCores
    storageSizeInGB: storageSizeInGB
    isGeneralPurposeV2: nextGenGeneralPurpose
    licenseType: licenseType
    hybridSecondaryUsage: hybridSecondaryUsage
    zoneRedundant: zoneRedundant
    requestedBackupStorageRedundancy: backupStorageRedundancy == 'GRS'
      ? 'Geo'
      : (backupStorageRedundancy == 'GZRS' ? 'GeoZone' : (backupStorageRedundancy == 'ZRS' ? 'Zone' : 'Local'))
    databaseFormat: updatePolicy
    proxyOverride: connectionType
    publicDataEndpointEnabled: false
    minimalTlsVersion: '1.2'
    maintenanceConfigurationId: subscriptionResourceId(
      'Microsoft.Maintenance/publicMaintenanceConfigurations',
      maintenanceWindow
    )
    timezoneId: timezoneId
    dnsZonePartner: empty(dnsZonePartnerId) ? null : dnsZonePartnerId
    primaryUserAssignedIdentityId: userAssignedIdentityId
    keyId: useCmk ? tdeCustomerManagedKey.keyVaultKeyId : null
    administrators: {
      administratorType: 'ActiveDirectory'
      principalType: entraAdmin.?principalType ?? 'Group'
      login: entraAdmin.loginName
      sid: entraAdmin.objectId
      tenantId: tenant().tenantId
      azureADOnlyAuthentication: true
    }
  }
  dependsOn: [
    tdeRole
  ]
}

// Diagnóstico y auditoría (la auditoría se crea con CREATE SERVER AUDIT ... TO EXTERNAL_MONITOR)
resource diagnostics 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = {
  name: 'diag-${name}'
  scope: instance
  properties: {
    workspaceId: logAnalyticsWorkspaceId
    logs: [
      {
        category: 'SQLSecurityAuditEvents'
        enabled: true
      }
      {
        category: 'DevOpsOperationsAudit'
        enabled: true
      }
      {
        category: 'ResourceUsageStats'
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

resource schedule 'Microsoft.Sql/managedInstances/startStopSchedules@2025-01-01' = if (!empty(startStopSchedule)) {
  parent: instance
  name: 'default'
  properties: {
    timeZoneId: startStopSchedule.?timezoneId ?? 'UTC'
    description: 'Parada fuera de horario de ${name}'
    scheduleList: startStopSchedule.?schedules ?? []
  }
}

resource dbs 'Microsoft.Sql/managedInstances/databases@2025-01-01' = [
  for d in databases: {
    parent: instance
    name: d.name
    location: location
    tags: tags
    properties: {}
  }
]

resource shortTermRetention 'Microsoft.Sql/managedInstances/databases/backupShortTermRetentionPolicies@2025-01-01' = [
  for (d, i) in databases: {
    parent: dbs[i]
    name: 'default'
    properties: {
      retentionDays: d.?retentionDays ?? 7
    }
  }
]

resource longTermRetention 'Microsoft.Sql/managedInstances/databases/backupLongTermRetentionPolicies@2025-01-01' = [
  for (d, i) in databases: if (contains(d, 'ltr')) {
    parent: dbs[i]
    name: 'default'
    properties: {
      weeklyRetention: d.?ltr.?weekly ?? 'PT0S'
      monthlyRetention: d.?ltr.?monthly ?? 'PT0S'
      yearlyRetention: d.?ltr.?yearly ?? 'PT0S'
      weekOfYear: d.?ltr.?weekOfYear ?? 1
    }
  }
]

resource dbDiagnostics 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = [
  for (d, i) in databases: {
    name: 'diag-${d.name}'
    scope: dbs[i]
    properties: {
      workspaceId: logAnalyticsWorkspaceId
      logs: map(['SQLInsights', 'QueryStoreRuntimeStatistics', 'QueryStoreWaitStatistics', 'Errors'], c => {
        category: c
        enabled: true
      })
    }
  }
]

// Failover group: se crea desde la región de la primaria
resource fogs 'Microsoft.Sql/locations/instanceFailoverGroups@2025-01-01' = [
  for f in failoverGroups: {
    name: '${location}/${f.name}'
    properties: {
      managedInstancePairs: [
        {
          primaryManagedInstanceId: instance.id
          partnerManagedInstanceId: f.partnerManagedInstanceId
        }
      ]
      partnerRegions: [
        {
          location: f.partnerRegion
        }
      ]
      readWriteEndpoint: {
        failoverPolicy: f.?failoverMode ?? 'Manual'
        failoverWithDataLossGracePeriodMinutes: (f.?failoverMode ?? 'Manual') == 'Automatic' ? f.graceMinutes : null
      }
      readOnlyEndpoint: {
        failoverPolicy: (f.?readOnlyFailover ?? false) ? 'Enabled' : 'Disabled'
      }
      secondaryType: f.?secondaryType ?? 'Geo'
    }
    dependsOn: [
      dbs
    ]
  }
]

output managedInstanceId string = instance.id
output fullyQualifiedDomainName string = instance.properties.fullyQualifiedDomainName
output dnsZone string = instance.properties.dnsZone
output systemAssignedPrincipalId string = instance.identity.principalId
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

`sqlmi-workload-pro-01.bicepparam`:

```bicep
using 'sqlmi.bicep'

// La secundaria (sqlmi-workload-pro-dr-01) se despliega después con la misma plantilla,
// dnsZonePartnerId = ID de esta instancia y sin databases ni failoverGroups
param name = 'sqlmi-workload-pro-01'
param subnetId = '<resourceId snet-sqlmi-pro (delegada, con NSG y tabla de rutas)>'

param skuName = 'BC_Gen5'
param vCores = 8
param storageSizeInGB = 512

param zoneRedundant = true
param backupStorageRedundancy = 'GZRS'
param maintenanceWindow = '<SQL_Región_MI_2>' // Weekend

param entraAdmin = {
  loginName: '<grupo sqlmi-admins-pro>'
  objectId: '<objectId del grupo>'
  principalType: 'Group'
}

param userAssignedIdentityId = '<resourceId id-sqlmi-workload-pro (con Directory Readers)>'
param userAssignedIdentityPrincipalId = '<principalId de la identidad>'

param tdeCustomerManagedKey = {
  keyVaultId: '<resourceId kv-workload-pro>'
  keyVaultKeyId: '<https://kv-workload-pro.vault.azure.net/keys/tde-sqlmi/versión>'
}

param logAnalyticsWorkspaceId = '<resourceId log-platform-pro>'

param databases = [
  {
    name: 'erp'
    retentionDays: 35
    ltr: {
      weekly: 'P5W'
      monthly: 'P12M'
      yearly: 'P10Y'
      weekOfYear: 1
    }
  }
  {
    name: 'staging'
  }
]

param failoverGroups = [
  {
    name: 'fog-sqlmi-workload-pro'
    partnerManagedInstanceId: '<resourceId sqlmi-workload-pro-dr-01>'
    partnerRegion: '<región-secundaria>'
    secondaryType: 'Standby' // solo recuperación ante desastres: sin coste de licencia
  }
]
```

Despliegue:

```powershell
New-AzResourceGroupDeployment -ResourceGroupName "<rg-workload-pro>" `
    -TemplateParameterFile "sqlmi-workload-pro-01.bicepparam" -Name "sqlmi-workload-pro-01"
```

## Errores típicos

| Síntoma | Causa | Solución |
|---|---|---|
| La creación falla al validar la subred | Subred no delegada, sin NSG o tabla de rutas, compartida o pequeña | Requisitos de red y fórmula de tamaño |
| La creación tarda horas | Primera instancia de la subred, zonas o falta de capacidad en la región | Esperado; agrupar instancias en la misma subred |
| No se puede ampliar la subred | Hay instancias dentro | Subred nueva y mover la instancia |
| Un cambio en el NSG o la ruta se rechaza | La network intent policy protege las reglas obligatorias | Crear reglas propias; no tocar las `Microsoft.Sql-managedInstances_UseOnly_mi-` |
| Los despliegues fallan por Azure Policy | Deny sobre `networkIntentPolicies` o `serviceEndpointPolicies` del servicio | Excluirlos de la política |
| Fallo de conectividad tras añadir NAT Gateway | No soportado | Salida por firewall con UDR |
| Login de Entra rechazado | La identidad de la instancia no tiene Directory Readers | Concederlo (Privileged Role Administrator) |
| Las conexiones Redirect fallan desde on-premises | Solo se abrió el 1433 a la IP de la instancia | Abrir el 1433 a **todo** el rango de la subred |
| El private endpoint no resuelve | El DNS no se registra automáticamente | Zona `privatelink.<zona-dns>.database.windows.net` y registro A |
| Error de certificado por el private endpoint en la misma VNet | El nombre no coincide con el certificado | `HostNameInCertificate` con el nombre del endpoint local |
| No se crea el failover group | Secundaria con bases, otra zona DNS, VNets solapadas o puertos 5022 y 11000-11999 cerrados | Secundaria vacía con `dns_zone_partner` y red preparada |
| Los usuarios no entran tras conmutar | Los logins y jobs viven en `master` y `msdb` y no se replican | Recrearlos y sincronizarlos en la secundaria |
| No se puede activar la redundancia de zona | Copias GRS o LRS, región sin soporte o Next-gen General Purpose | Copias ZRS o GZRS y región soportada |
| No se puede parar la instancia | Business Critical, zonas, failover group, link o pool | Solo General Purpose sin esas opciones |
| No se puede restaurar en SQL Server | Política Always-up-to-date (o 2025 para SQL Server 2022) | Elegir la política antes de cambiarla; es irreversible |
| La política SQL Server 2025 no existe en Terraform | El provider 4.81 solo admite 2022 y Always-up-to-date | Bicep con la API 2025-01-01 |
| La evaluación express no se activa | La instancia no tiene identidad de sistema | Identidad `SystemAssigned, UserAssigned` (lo que aplica el root) |
| Logins fallidos de `AzureSQLConnectivityChecker` en la auditoría | Pruebas internas de conectividad del servicio | Normal; no son un incidente de seguridad |
