---
title: "PostgreSQL Flexible Server"
indice: database
resumen: "PostgreSQL gestionado con control de red."
estado: documentado   # proximamente | en-curso | documentado
orden: 4
last_review: 2026-11-12
fuentes:
  - titulo: "What is Azure Database for PostgreSQL flexible server?"
    url: https://learn.microsoft.com/azure/postgresql/overview
  - titulo: "Supported versions of PostgreSQL in Azure Database for PostgreSQL flexible server"
    url: https://learn.microsoft.com/azure/postgresql/configure-maintain/concepts-supported-versions
  - titulo: "Azure Database for PostgreSQL flexible server extended support"
    url: https://learn.microsoft.com/azure/postgresql/configure-maintain/extended-support
  - titulo: "Compute options in Azure Database for PostgreSQL flexible server"
    url: https://learn.microsoft.com/azure/postgresql/compute-storage/concepts-compute
  - titulo: "Storage in Azure Database for PostgreSQL flexible server"
    url: https://learn.microsoft.com/azure/postgresql/compute-storage/concepts-storage
  - titulo: "Premium SSD storage option in Azure Database for PostgreSQL flexible server"
    url: https://learn.microsoft.com/azure/postgresql/compute-storage/concepts-storage-premium-ssd
  - titulo: "Premium SSD v2 storage option in Azure Database for PostgreSQL flexible server"
    url: https://learn.microsoft.com/azure/postgresql/compute-storage/concepts-storage-premium-ssd-v2
  - titulo: "Limits in Azure Database for PostgreSQL flexible server"
    url: https://learn.microsoft.com/azure/postgresql/configure-maintain/concepts-limits
  - titulo: "Networking with public access (allowed IP addresses)"
    url: https://learn.microsoft.com/azure/postgresql/network/concepts-networking-public
  - titulo: "Network with private access (virtual network integration)"
    url: https://learn.microsoft.com/azure/postgresql/network/concepts-networking-private
  - titulo: "Networking with Private Link in Azure Database for PostgreSQL flexible server"
    url: https://learn.microsoft.com/azure/postgresql/network/concepts-networking-private-link
  - titulo: "Change from virtual network integration to a private endpoint-capable network configuration"
    url: https://learn.microsoft.com/azure/postgresql/network/how-to-migrate-vnet-private-endpoint-capable-server
  - titulo: "Azure Private Endpoint private DNS zone values"
    url: https://learn.microsoft.com/azure/private-link/private-endpoint-dns
  - titulo: "Microsoft Entra authentication in Azure Database for PostgreSQL flexible server"
    url: https://learn.microsoft.com/azure/postgresql/security/security-entra-concepts
  - titulo: "Use Microsoft Entra ID authentication in Azure Database for PostgreSQL flexible server"
    url: https://learn.microsoft.com/azure/postgresql/security/security-entra-configure
  - titulo: "Transport Layer Security (TLS) in Azure Database for PostgreSQL flexible server"
    url: https://learn.microsoft.com/azure/postgresql/security/security-tls
  - titulo: "Data encryption at rest in Azure Database for PostgreSQL flexible server"
    url: https://learn.microsoft.com/azure/postgresql/security/security-data-encryption
  - titulo: "Configure data encryption in Azure Database for PostgreSQL flexible server"
    url: https://learn.microsoft.com/azure/postgresql/security/security-configure-data-encryption
  - titulo: "Secure your Azure Database for PostgreSQL flexible server"
    url: https://learn.microsoft.com/azure/postgresql/security/security-overview
  - titulo: "Audit logging in Azure Database for PostgreSQL flexible server"
    url: https://learn.microsoft.com/azure/postgresql/security/security-audit
  - titulo: "Microsoft Defender for Cloud in Azure Database for PostgreSQL flexible server"
    url: https://learn.microsoft.com/azure/postgresql/security/security-defender-for-cloud
  - titulo: "Reliability in Azure Database for PostgreSQL"
    url: https://learn.microsoft.com/azure/reliability/reliability-postgresql-flexible-server
  - titulo: "Configure high availability for Azure Database for PostgreSQL flexible server"
    url: https://learn.microsoft.com/azure/postgresql/high-availability/how-to-configure-high-availability
  - titulo: "Backup and restore in Azure Database for PostgreSQL flexible server"
    url: https://learn.microsoft.com/azure/postgresql/backup-restore/concepts-backup-restore
  - titulo: "Overview of business continuity in Azure Database for PostgreSQL flexible server"
    url: https://learn.microsoft.com/azure/postgresql/backup-restore/concepts-business-continuity
  - titulo: "Read replicas in Azure Database for PostgreSQL flexible server"
    url: https://learn.microsoft.com/azure/postgresql/read-replica/concepts-read-replicas
  - titulo: "PgBouncer in Azure Database for PostgreSQL flexible server"
    url: https://learn.microsoft.com/azure/postgresql/connectivity/concepts-pgbouncer
  - titulo: "Monitor using metrics and logs in Azure Database for PostgreSQL flexible server"
    url: https://learn.microsoft.com/azure/postgresql/monitor/concepts-monitoring
  - titulo: "Configure and access logs in Azure Database for PostgreSQL flexible server"
    url: https://learn.microsoft.com/azure/postgresql/monitor/how-to-configure-and-access-logs
  - titulo: "Prepay for compute resources with reserved capacity in Azure Database for PostgreSQL flexible server"
    url: https://learn.microsoft.com/azure/postgresql/configure-maintain/concepts-reserved-pricing
  - titulo: "Microsoft.DBforPostgreSQL flexibleServers (plantillas ARM/Bicep)"
    url: https://learn.microsoft.com/azure/templates/microsoft.dbforpostgresql/flexibleservers
  - titulo: "azurerm_postgresql_flexible_server"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/postgresql_flexible_server
  - titulo: "Módulo Terraform Database/PostgreSQLFlexible"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Database/PostgreSQLFlexible
  - titulo: "Módulo Terraform Networking/Networking/modules/private_endpoint"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Networking/Networking/modules/private_endpoint
  - titulo: "Módulo Terraform Security/Seguridad/modules/monitor_diagnostic_setting"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Security/Seguridad/modules/monitor_diagnostic_setting
---

**Azure Database for PostgreSQL flexible server** es PostgreSQL comunitario gestionado: Azure se encarga del SO, de los parches menores, de las copias y de la alta disponibilidad, y tú decides la red, la ventana de mantenimiento, los parámetros del motor y el tamaño. Corre en una VM Linux con el almacenamiento separado (tres copias síncronas locales), así que el cómputo se escala en segundos y se puede **parar** para no pagarlo. Para SQL Server está [Azure SQL Database](/recursos/database/azure-sql-database/); para MySQL, [MySQL Flexible Server](/recursos/database/mysql-flexible-server/).

## Qué es y cuándo usarlo

### Niveles de cómputo

| Nivel | Series | Para qué | Límites |
|---|---|---|---|
| **Burstable** | B (1 a 20 vCores) | Desarrollo, pruebas, PoC, bases pequeñas | **No es para producción**: sin créditos de CPU cae a la línea base y puede dejar de responder. Sin alta disponibilidad, réplicas, PgBouncer ni copias bajo demanda. Sin soporte 24x7 ni RCA |
| **General Purpose** | Ddsv5, Dadsv5, Ddsv6, Dadsv6... (4 GiB por vCore) | La mayoría de cargas de producción | — |
| **Memory Optimized** | Edsv5, Eadsv5, Edsv6... (6,75 a 9,5 GiB por vCore) | Alta concurrencia, procesamiento en memoria | — |

- vCores hacia arriba o abajo y almacenamiento hacia arriba en segundos; **el almacenamiento nunca baja**.
- El máximo de conexiones depende del tamaño (B1ms: 50; D4ds_v5: 1.718) y se reservan 15 para replicación y monitorización.
- La serie **v6 está en preview** y no admite integración en VNet.

### Versiones

| Versión | Estado |
|---|---|
| 14, 15, 16, 17, 18 | Soportadas |
| 11, 12, 13 | **Soporte extendido de pago** desde el 1 de septiembre de 2026 (cobro automático) |

La 14 sale del soporte estándar el 31 de enero de 2027. Los parches menores los aplica Azure en la ventana de mantenimiento. La **actualización de versión mayor es en el sitio**, pero desactiva la alta disponibilidad, obliga a borrar las réplicas antes, no actualiza extensiones como pgvector y no conserva la configuración de pgaudit.

### Almacenamiento

| | Premium SSD | Premium SSD v2 |
|---|---|---|
| Tamaño | Saltos fijos (32 GiB a 32 TiB) | De GiB en GiB hasta 64 TiB |
| IOPS | Según el tamaño, hasta 20.000 | 3.000 gratis (12.000 desde 512 GiB), hasta 80.000, **independientes del tamaño** |
| Throughput | Hasta 900 MB/s | 125 MB/s gratis (500 MB/s desde 400 GiB), hasta 1.200 MB/s |
| Crecimiento automático | GA; **duplica tamaño y coste** | Preview |
| Limitaciones | Cruzar 4.096 GiB es offline | Sin Burstable, sin copias a largo plazo, sin copia bajo demanda, sin PostgreSQL 13; no se migra en línea desde Premium SSD |

Con el 95 % de uso o menos de 5 GiB libres, **el servidor pasa a solo lectura**: alerta sobre `storage_percentage` o crecimiento automático. El tamaño de VM también limita las IOPS.

### Red

El modo se elige al crear:

| Modo | Cómo | Cuándo |
|---|---|---|
| **Acceso público + private endpoint** | Acceso público deshabilitado y uno o varios private endpoints (`postgresqlServer`, zona `privatelink.postgres.database.azure.com`) | **Opción por defecto**: varias VNets, hub and spoke, serie v6 |
| Integración en VNet | El servidor vive en una subred delegada; zona privada que termine en `postgres.database.azure.com` | Diseños existentes; no admite private endpoints ni la serie v6 |

- Pasar de integración en VNet a private endpoint **es irreversible**, deja el servidor sin servicio hasta 10 minutos y, después, inaccesible hasta crear el endpoint.
- **No se restaura entre modos**: una copia de un servidor público vuelve a público y una de VNet a VNet.
- Las reglas de firewall, endpoints y parámetros **no se copian** al restaurar.

### Seguridad

| Control | Recomendación |
|---|---|
| Autenticación | **Solo Microsoft Entra** (sin contraseña), con un grupo como administrador. Activarla reinicia el servidor. Los tokens duran hasta 1 hora (24 h los de identidades del sistema) |
| TLS | `require_secure_transport` siempre `on` (es el valor por defecto); TLS 1.2 y 1.3; mejor `ssl_min_protocol_version = TLSv1.3` si todos los clientes lo soportan. No hay mTLS |
| Clientes | `sslmode=verify-full` (o `verify-ca` si el DNS privado no lo permite) con las raíces DigiCert Global Root G2 y Microsoft RSA Root CA 2017. **Nada de pinning** ni intermedias: rotan sin aviso |
| Contraseñas | Desde PostgreSQL 14 solo SCRAM-SHA-256 |
| Cifrado | Siempre con AES-256; clave del cliente opcional (ver abajo) |
| Auditoría | Extensión `pgaudit` (permitirla, cargarla en `shared_preload_libraries` y `CREATE EXTENSION`); `pgaudit.log = ROLE` redacta las contraseñas |
| Defender | **Defender for open-source relational databases** (todos los niveles): alertas de fuerza bruta y accesos anómalos, y recomendaciones de CSPM |

**Clave del cliente**: se elige **solo al crear** y no se puede volver a la clave del servicio. El Key Vault va en la misma región, con purge protection, 90 días de retención y el rol *Key Vault Crypto Service Encryption User* para la identidad de usuario. Si el servidor pierde acceso a la clave, pasa a **Inaccessible** en unos 60 minutos. Con el firewall del Key Vault, hay que permitir los servicios de confianza.

### Alta disponibilidad

| Configuración | SLA | Comportamiento |
|---|---|---|
| **Zone-redundant** | 99,99 % | Standby en otra zona, réplica síncrona: **RPO 0**, failover en 60-120 segundos |
| Same-zone | 99,95 % | Standby en la misma zona; no protege de la caída de la zona |
| Sin alta disponibilidad | 99,9 % | Un solo servidor; ante fallo se reprovisiona |

- El standby **cuesta lo mismo que el primario**; la replicación entre zonas no se cobra.
- No hay alta disponibilidad en Burstable. **Las zonas no se cambian después**: hay que recrear el servidor.
- El mantenimiento se aplica primero al standby, así que con alta disponibilidad el impacto es mínimo.
- Tras un failover, el antiguo standby es el primario y **las zonas quedan intercambiadas**.
- El standby replica también los errores: un `DROP TABLE` se arregla con una restauración.

### Copias y recuperación

| Opción | Detalle |
|---|---|
| **Copias automáticas** | Snapshot diario más WAL; **RPO de hasta 5 minutos**; retención de 7 a 35 días; ZRS en regiones con zonas. Gratis hasta el 100 % del almacenamiento aprovisionado |
| Copia geo-redundante | **Solo al crear** y en regiones emparejadas; RPO de hasta 1 hora y sin PITR en la región remota. **Spain Central no la ofrece** |
| Réplicas de lectura | Hasta 5, asíncronas, en cualquier región; con **virtual endpoints** la cadena de conexión no cambia al promocionar. Azure **no promociona solo** |
| [Retención a largo plazo](/recursos/backups-update/backup-vault/) | Azure Backup (Backup vault) hasta 10 años: copias lógicas semanales, servidores de hasta 1 TiB, se restauran como ficheros |
| Copias bajo demanda | Hasta 7, ni en Burstable ni en Premium SSD v2 |

- Restaurar siempre **crea un servidor nuevo**, sin alta disponibilidad, réplicas, reglas ni parámetros del original.
- Borrar el servidor borra sus copias: **bloqueo de recurso** en producción.
- Las réplicas no tienen alta disponibilidad ni copias, y una réplica promocionada tampoco: hay que activarla después.
- Para PgBouncer: puerto 6432, mismo host, sin reinicio al activarlo; tras un failover se reinicia en el nuevo primario.

### Cómo se factura

| Concepto | Detalle |
|---|---|
| Cómputo | Por vCore y hora según nivel y serie. **Parado no se cobra**; arranca solo a los 7 días |
| Alta disponibilidad | El standby al mismo precio que el primario |
| Almacenamiento | Por GiB aprovisionado; en Premium SSD v2, además las IOPS y el throughput por encima de lo gratuito |
| Copias | Gratis hasta el tamaño aprovisionado; el exceso por GiB y mes. La geo-redundante cuenta doble |
| Réplicas | Cómputo y almacenamiento propios más tráfico entre regiones |
| Reservas | 1 o 3 años, **hasta un 65 %** de ahorro en cómputo |
| Soporte extendido | Versiones 11 a 13, desde el 1 de septiembre de 2026 |

### Qué escenario recomiendo

| Escenario del cliente | Diseño | Por qué |
|---|---|---|
| Producción crítica | General Purpose o Memory Optimized, zone-redundant, private endpoint, solo Entra | RPO 0 en zona, sin contraseñas ni exposición |
| Recuperación ante desastre en Spain Central | Réplica en otra región con virtual endpoint | La región no tiene copia geo-redundante |
| IO intensivo | Premium SSD v2 con IOPS ajustadas | Rendimiento sin pagar capacidad de más |
| Muchas conexiones cortas (contenedores, funciones) | PgBouncer integrado en el 6432 | Menos procesos en el servidor |
| Desarrollo y pruebas | Burstable parado fuera de horario | Sin coste de cómputo parado |
| Cumplimiento con retención larga | Backup vault con política semanal | Hasta 10 años, fuera de la suscripción del servidor |
| Aplicaciones en [Container Apps](/recursos/compute/container-apps/) | Identidad gestionada como rol de Entra | Sin secretos en la aplicación |

### Datos que conviene llevar a la reunión

- **Red, clave del cliente y copia geo-redundante se deciden al crear.**
- **Spain Central no tiene copia geo-redundante**: la recuperación regional va con réplicas.
- **Burstable no es para producción.**
- **Con el disco al 95 % el servidor pasa a solo lectura.**
- **La actualización de versión mayor desactiva la alta disponibilidad** y obliga a quitar réplicas.
- **Las versiones 11 a 13 ya pagan soporte extendido.**
- **Parado no paga cómputo, pero arranca solo a los 7 días.**

## Decisiones de diseño

| Decisión | Lo que aplico | Por qué |
|---|---|---|
| Servidor | Recurso nativo `azurerm_postgresql_flexible_server` | El módulo del repositorio no inicializa |
| Red | Private endpoint por defecto; integración en VNet como alternativa (uno u otro, validado) | Es el modo con más opciones y el que Microsoft permite migrar |
| Acceso público | `public_network_access_enabled = false` explícito | El provider lo pone a `true` si se omite |
| Autenticación | Entra siempre; contraseña solo si se pide, generada y guardada en Key Vault | Sin secretos en el código |
| Administradores | Grupos de Entra, creados antes que las bases | Recomendación de Microsoft para que puedan ser propietarios |
| TLS | `require_secure_transport = on` forzado (validado) | No se puede desactivar por error |
| Query Store | `pg_qs.query_capture_mode = top` y muestreo de esperas | Sin ellos, varias categorías de diagnóstico van vacías |
| Diagnóstico | `allLogs` + `AllMetrics` en tablas dedicadas | Microsoft desaconseja AzureDiagnostics para estas categorías |
| Alta disponibilidad | Zone-redundant con zonas distintas (validado); `ignore_changes` en las zonas | Tras un failover las zonas se intercambian |
| Clave del cliente | Identidad de usuario y rol antes del servidor | Solo se puede activar al crear |
| Réplicas | Simétricas con el origen y con private endpoint propio; virtual endpoint ReadWrite | Recuperación regional sin cambiar la cadena de conexión |
| Versiones | 14 a 18 (validado) | 11 a 13 están en soporte extendido de pago |

Alineación con el Well-Architected Framework:

- **Fiabilidad**: zone-redundant, réplicas entre regiones, virtual endpoints y retención de copias.
- **Seguridad**: red privada, Entra sin contraseñas, TLS, clave del cliente y Defender.
- **Coste**: niveles por entorno, parada, reservas y Premium SSD v2.
- **Excelencia operativa**: IaC con validaciones y diagnóstico completo.
- **Rendimiento**: Query Store, PgBouncer y almacenamiento ajustable.

## Módulo de Terraform

### Los módulos del repositorio

[Database/PostgreSQLFlexible](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Database/PostgreSQLFlexible) **no inicializa**: declara `variable "version"`, un nombre reservado en Terraform (`The variable name "version" is reserved`). Es el mismo fallo que el módulo de SQL Server. Además:

- Admite PostgreSQL 11 a 16: ni 17 ni 18, y deja crear versiones en soporte extendido.
- No tiene administradores de Entra, diagnóstico, private endpoints, réplicas ni virtual endpoints.
- `authentication` deja la contraseña activa por defecto y el ejemplo saca la contraseña en un output (sensible).
- Usa `locals` para el nombre y las tags.

Por eso el servidor va con el recurso nativo. Se reutilizan `private_endpoint`, `monitor_diagnostic_setting` (con `category_group`) y `PRO/common/assigned_identity` para la clave del cliente.

Notas del provider (azurerm 4.81, API 2025-08-01):

- `public_network_access_enabled` vale **`true` por defecto**. Microsoft lo advierte también al migrar de VNet a private endpoint: si se omite, Terraform intenta abrir el acceso público.
- **No soporta Premium SSD v2**: no hay tipo de almacenamiento, IOPS ni throughput. Bicep sí.
- La validación de `sku_name` no acepta las series **Dadsv6 y Eadsv6** ni los tamaños v6 de 128 y 192 vCores que publica Learn.
- `customer_managed_key`, `geo_redundant_backup_enabled` y `delegated_subnet_id` son ForceNew, coherente con el servicio.
- `administrator_password_wo` (write-only) evita la contraseña en el estado, pero exige Terraform 1.11 o posterior.

### Estructura en el proyecto

```txt
/
├── providers.tf               # azurerm >= 4.81.0, random
├── postgresql_flexible.tf     # identidad, servidor, Entra, parámetros, bases, endpoints, diagnóstico y réplicas
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
      # Validado con 4.81.0 (API 2025-08-01: PostgreSQL 18, virtual endpoints y administradores de Entra).
      # < 5.0.0: restricción de los módulos de AzureTerraformModules.
      version = ">= 4.81.0, < 5.0.0"
    }
    random = {
      source  = "hashicorp/random"
      version = ">= 3.6.0, < 4.0.0"
    }
  }
}

provider "azurerm" {
  features {}
}

# Tenant de la sesión de Terraform (sin IDs en el código)
data "azurerm_client_config" "current" {}

variable "tags" {
  description = "Tags corporativos comunes a todos los recursos."
  type        = map(string)
}
```

### `postgresql_flexible.tf`

```hcl
# =============================================================================
# Azure Database for PostgreSQL flexible server seguro por defecto: sin acceso público
# (private endpoint o integración en VNet), solo Microsoft Entra salvo que se pida contraseña,
# TLS obligatorio, alta disponibilidad entre zonas, clave del cliente opcional, diagnóstico en
# tablas dedicadas, réplicas de lectura en otra región y virtual endpoints
#
# DEPENDENCY: grupos de recursos creados
# DEPENDENCY: grupos de Microsoft Entra para los administradores (se recomienda grupo)
# DEPENDENCY: con private endpoint: subred de endpoints y zona privatelink.postgres.database.azure.com
#             enlazada a las VNets que resuelven
# DEPENDENCY: con integración en VNet: subred delegada a Microsoft.DBforPostgreSQL/flexibleServers y
#             zona privada que termine en postgres.database.azure.com
# DEPENDENCY: con clave del cliente: Key Vault en la misma región, con purge protection y RBAC
# DEPENDENCY: con contraseña: Key Vault con RBAC para el secreto ("Key Vault Secrets Officer")
# DEPENDENCY: espacio de trabajo de Log Analytics
# =============================================================================

variable "postgresql_servers" {
  description = "Servidores flexibles de PostgreSQL (clave = nombre, único en Azure)."
  type = map(object({
    resource_group_name = string
    location            = string
    version             = string # 14 a 18 (11 a 13 están en soporte extendido de pago)
    sku_name            = string # B_Standard_B2s | GP_Standard_D4ds_v5 | MO_Standard_E4ds_v5 ...

    storage_mb        = number
    storage_tier      = optional(string) # P4..P80; por defecto el del tamaño
    auto_grow_enabled = optional(bool, true)

    zone = optional(string)
    high_availability = optional(object({
      mode                      = optional(string, "ZoneRedundant") # ZoneRedundant | SameZone
      standby_availability_zone = optional(string)
    }))

    backup_retention_days        = optional(number, 7)
    geo_redundant_backup_enabled = optional(bool, false) # solo al crear y en regiones emparejadas

    maintenance_window = optional(object({
      day_of_week  = number # 0 = domingo
      start_hour   = number
      start_minute = optional(number, 0)
    }))

    # Autenticación: Entra siempre; contraseña solo si hace falta (se guarda en Key Vault)
    entra_admins = map(object({ # clave = nombre visible del grupo o identidad
      object_id      = string
      principal_type = optional(string, "Group") # Group | User | ServicePrincipal
    }))
    password_auth_enabled = optional(bool, false)
    administrator_login   = optional(string)
    key_vault_id          = optional(string) # para el secreto de la contraseña

    # Red: private endpoints (acceso público deshabilitado) o integración en VNet, nunca ambos
    private_endpoints = optional(map(object({
      subnet_id           = string
      private_dns_zone_id = string
    })), {})
    delegated_subnet_id = optional(string)
    private_dns_zone_id = optional(string) # solo con delegated_subnet_id

    # Clave del cliente: solo al crear; no se puede volver a la clave del servicio
    customer_managed_key = optional(object({
      key_vault_id     = string
      key_vault_key_id = string # sin versión = rotación automática
    }))

    databases = optional(map(object({
      charset   = optional(string, "UTF8")
      collation = optional(string, "en_US.utf8")
    })), {})

    server_parameters = optional(map(string), {})

    log_analytics_workspace_id = string
    tags                       = optional(map(string), {})
  }))
  default = {}

  validation {
    condition     = alltrue([for k, v in var.postgresql_servers : contains(["14", "15", "16", "17", "18"], v.version)])
    error_message = "version debe ser 14, 15, 16, 17 o 18: 11, 12 y 13 están en soporte extendido de pago."
  }

  validation {
    condition     = alltrue([for k, v in var.postgresql_servers : can(regex("^(B|GP|MO)_Standard_", v.sku_name))])
    error_message = "sku_name debe empezar por B_Standard_, GP_Standard_ o MO_Standard_."
  }

  validation {
    condition = alltrue([
      for k, v in var.postgresql_servers :
      v.high_availability == null || !startswith(v.sku_name, "B_")
    ])
    error_message = "La alta disponibilidad no existe en Burstable: usa General Purpose o Memory Optimized."
  }

  validation {
    condition = alltrue([
      for k, v in var.postgresql_servers :
      v.high_availability == null || contains(["ZoneRedundant", "SameZone"], try(v.high_availability.mode, ""))
    ])
    error_message = "high_availability.mode debe ser ZoneRedundant o SameZone."
  }

  validation {
    condition = alltrue([
      for k, v in var.postgresql_servers :
      try(v.high_availability.mode, "") != "ZoneRedundant" || try(v.high_availability.standby_availability_zone, null) == null ||
      v.zone == null || try(v.high_availability.standby_availability_zone, "") != v.zone
    ])
    error_message = "Con ZoneRedundant, la zona del standby debe ser distinta de la del primario."
  }

  validation {
    condition     = alltrue([for k, v in var.postgresql_servers : v.backup_retention_days >= 7 && v.backup_retention_days <= 35])
    error_message = "backup_retention_days debe estar entre 7 y 35."
  }

  validation {
    condition     = alltrue([for k, v in var.postgresql_servers : length(v.entra_admins) > 0])
    error_message = "Hace falta al menos un administrador de Microsoft Entra."
  }

  validation {
    condition = alltrue(flatten([
      for k, v in var.postgresql_servers : [
        for ak, a in v.entra_admins : contains(["Group", "User", "ServicePrincipal"], a.principal_type)
      ]
    ]))
    error_message = "principal_type debe ser Group, User o ServicePrincipal."
  }

  validation {
    condition = alltrue([
      for k, v in var.postgresql_servers :
      !v.password_auth_enabled || (v.administrator_login != null && v.key_vault_id != null)
    ])
    error_message = "Con password_auth_enabled hacen falta administrator_login y key_vault_id (la contraseña va a Key Vault)."
  }

  validation {
    condition = alltrue([
      for k, v in var.postgresql_servers :
      (v.delegated_subnet_id == null) != (length(v.private_endpoints) == 0)
    ])
    error_message = "Elige un modo de red: private_endpoints o delegated_subnet_id (no ambos, no ninguno)."
  }

  validation {
    condition = alltrue([
      for k, v in var.postgresql_servers :
      v.delegated_subnet_id == null ? v.private_dns_zone_id == null : v.private_dns_zone_id != null
    ])
    error_message = "private_dns_zone_id va solo con delegated_subnet_id (y es obligatorio con él)."
  }

  validation {
    condition = alltrue([
      for k, v in var.postgresql_servers :
      lower(lookup(v.server_parameters, "require_secure_transport", "on")) == "on"
    ])
    error_message = "require_secure_transport no puede desactivarse."
  }
}

variable "postgresql_replicas" {
  description = "Réplicas de lectura (clave = nombre). Heredan versión, SKU y almacenamiento del origen."
  type = map(object({
    source_server       = string # clave en postgresql_servers
    resource_group_name = string
    location            = string
    zone                = optional(string)
    private_endpoints = map(object({
      subnet_id           = string
      private_dns_zone_id = string
    }))
    virtual_endpoint_name = optional(string) # ReadWrite: sigue al primario tras promocionar
    tags                  = optional(map(string), {})
  }))
  default = {}
}

# -----------------------------------------------------------------------------
# Identidad y rol para la clave del cliente (antes de crear el servidor)
# -----------------------------------------------------------------------------
module "postgresql_identity" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//PRO/common/assigned_identity?ref=main"
  for_each = { for k, v in var.postgresql_servers : k => v if v.customer_managed_key != null }

  name                = "id-${each.key}"
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  tags                = merge(var.tags, each.value.tags)
}

resource "azurerm_role_assignment" "postgresql_cmk" {
  for_each = { for k, v in var.postgresql_servers : k => v if v.customer_managed_key != null }

  scope                            = each.value.customer_managed_key.key_vault_id
  role_definition_name             = "Key Vault Crypto Service Encryption User"
  principal_id                     = module.postgresql_identity[each.key].principal_id
  principal_type                   = "ServicePrincipal"
  skip_service_principal_aad_check = true
  description                      = "Cifrado con clave del cliente de ${each.key}"
}

# -----------------------------------------------------------------------------
# Contraseña del administrador (solo si se habilita la autenticación por contraseña)
# -----------------------------------------------------------------------------
resource "random_password" "postgresql_admin" {
  for_each = { for k, v in var.postgresql_servers : k => v if v.password_auth_enabled }

  length           = 32
  special          = true
  override_special = "!#$%*()-_=+[]{}:?"
  min_lower        = 2
  min_upper        = 2
  min_numeric      = 2
  min_special      = 2
}

resource "azurerm_key_vault_secret" "postgresql_admin" {
  for_each = random_password.postgresql_admin

  name         = "psql-${each.key}-admin"
  value        = each.value.result
  key_vault_id = var.postgresql_servers[each.key].key_vault_id
  content_type = "PostgreSQL administrator (${var.postgresql_servers[each.key].administrator_login})"
}

# -----------------------------------------------------------------------------
# Servidor (recurso nativo: Database/PostgreSQLFlexible no inicializa)
# -----------------------------------------------------------------------------
resource "azurerm_postgresql_flexible_server" "this" {
  for_each = var.postgresql_servers

  name                = each.key
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  version             = each.value.version
  sku_name            = each.value.sku_name

  storage_mb        = each.value.storage_mb
  storage_tier      = each.value.storage_tier
  auto_grow_enabled = each.value.auto_grow_enabled

  zone = each.value.zone
  dynamic "high_availability" {
    for_each = each.value.high_availability != null ? [each.value.high_availability] : []
    content {
      mode                      = high_availability.value.mode
      standby_availability_zone = high_availability.value.standby_availability_zone
    }
  }

  backup_retention_days        = each.value.backup_retention_days
  geo_redundant_backup_enabled = each.value.geo_redundant_backup_enabled

  dynamic "maintenance_window" {
    for_each = each.value.maintenance_window != null ? [each.value.maintenance_window] : []
    content {
      day_of_week  = maintenance_window.value.day_of_week
      start_hour   = maintenance_window.value.start_hour
      start_minute = maintenance_window.value.start_minute
    }
  }

  authentication {
    active_directory_auth_enabled = true
    password_auth_enabled         = each.value.password_auth_enabled
    tenant_id                     = data.azurerm_client_config.current.tenant_id
  }
  administrator_login    = each.value.password_auth_enabled ? each.value.administrator_login : null
  administrator_password = each.value.password_auth_enabled ? random_password.postgresql_admin[each.key].result : null

  # El provider pone true por defecto: siempre explícito
  public_network_access_enabled = false
  delegated_subnet_id           = each.value.delegated_subnet_id
  private_dns_zone_id           = each.value.private_dns_zone_id

  dynamic "identity" {
    for_each = each.value.customer_managed_key != null ? [1] : []
    content {
      type         = "UserAssigned"
      identity_ids = [module.postgresql_identity[each.key].id]
    }
  }

  dynamic "customer_managed_key" {
    for_each = each.value.customer_managed_key != null ? [each.value.customer_managed_key] : []
    content {
      key_vault_key_id                  = customer_managed_key.value.key_vault_key_id
      primary_user_assigned_identity_id = module.postgresql_identity[each.key].id
    }
  }

  tags = merge(var.tags, each.value.tags)

  lifecycle {
    # Tras un failover el standby pasa a primario y las zonas se intercambian
    ignore_changes = [zone, high_availability[0].standby_availability_zone]

    precondition {
      condition     = !(each.value.geo_redundant_backup_enabled && each.value.customer_managed_key != null)
      error_message = "Copia geo-redundante con clave del cliente necesita clave e identidad en la región emparejada: fuera de este root."
    }
  }

  depends_on = [azurerm_role_assignment.postgresql_cmk]
}

# Administradores de Microsoft Entra (antes que las bases, para que puedan ser propietarios)
resource "azurerm_postgresql_flexible_server_active_directory_administrator" "this" {
  for_each = merge([
    for k, v in var.postgresql_servers : {
      for ak, a in v.entra_admins : "${k}/${ak}" => merge(a, { server = k, name = ak, rg = v.resource_group_name })
    }
  ]...)

  server_name         = azurerm_postgresql_flexible_server.this[each.value.server].name
  resource_group_name = each.value.rg
  tenant_id           = data.azurerm_client_config.current.tenant_id
  object_id           = each.value.object_id
  principal_name      = each.value.name
  principal_type      = each.value.principal_type
}

# Parámetros: TLS obligatorio y Query Store (lo necesitan las categorías de diagnóstico)
resource "azurerm_postgresql_flexible_server_configuration" "this" {
  for_each = merge([
    for k, v in var.postgresql_servers : {
      for pk, pv in merge({
        "require_secure_transport"              = "on"
        "pg_qs.query_capture_mode"              = "top"
        "pgms_wait_sampling.query_capture_mode" = "all"
      }, v.server_parameters) : "${k}/${pk}" => { server = k, name = pk, value = pv }
    }
  ]...)

  server_id = azurerm_postgresql_flexible_server.this[each.value.server].id
  name      = each.value.name
  value     = each.value.value
}

resource "azurerm_postgresql_flexible_server_database" "this" {
  for_each = merge([
    for k, v in var.postgresql_servers : {
      for dk, d in v.databases : "${k}/${dk}" => merge(d, { server = k, name = dk })
    }
  ]...)

  server_id = azurerm_postgresql_flexible_server.this[each.value.server].id
  name      = each.value.name
  charset   = each.value.charset
  collation = each.value.collation

  depends_on = [azurerm_postgresql_flexible_server_active_directory_administrator.this]
}

module "postgresql_private_endpoint" {
  source = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Networking/Networking/modules/private_endpoint?ref=main"
  for_each = merge([
    for k, v in var.postgresql_servers : {
      for pk, p in v.private_endpoints : "${k}-${pk}" => merge(p, { server = k, rg = v.resource_group_name, location = v.location })
    }
  ]...)

  private_endpoint_name          = "pe-${each.key}"
  custom_network_interface_name  = "nic-pe-${each.key}"
  resource_group_name            = each.value.rg
  location                       = each.value.location
  subnet_id                      = each.value.subnet_id
  private_connection_resource_id = azurerm_postgresql_flexible_server.this[each.value.server].id
  subresource_names              = ["postgresqlServer"]
  private_dns_zone_ids           = [each.value.private_dns_zone_id]
  tags                           = merge(var.tags, var.postgresql_servers[each.value.server].tags)
}

# Todas las categorías (allLogs) en tablas dedicadas + métricas
module "postgresql_diagnostics" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Security/Seguridad/modules/monitor_diagnostic_setting?ref=main"
  for_each = var.postgresql_servers

  monitor_diagnostic_setting_name = "diag-${each.key}"
  target_resource_id              = azurerm_postgresql_flexible_server.this[each.key].id
  log_analytics_workspace_id      = each.value.log_analytics_workspace_id
  log_analytics_destination_type  = "Dedicated"
  enabled_logs                    = [{ category_group = "allLogs" }]
  enabled_metrics                 = [{ category = "AllMetrics" }]
}

# -----------------------------------------------------------------------------
# Réplicas de lectura (otra región = recuperación ante desastre) y virtual endpoints
# -----------------------------------------------------------------------------
resource "azurerm_postgresql_flexible_server" "replica" {
  for_each = var.postgresql_replicas

  name                = each.key
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  zone                = each.value.zone

  create_mode      = "Replica"
  source_server_id = azurerm_postgresql_flexible_server.this[each.value.source_server].id

  # Simétrica con el origen
  version           = var.postgresql_servers[each.value.source_server].version
  sku_name          = var.postgresql_servers[each.value.source_server].sku_name
  storage_mb        = var.postgresql_servers[each.value.source_server].storage_mb
  auto_grow_enabled = var.postgresql_servers[each.value.source_server].auto_grow_enabled

  authentication {
    active_directory_auth_enabled = true
    password_auth_enabled         = var.postgresql_servers[each.value.source_server].password_auth_enabled
    tenant_id                     = data.azurerm_client_config.current.tenant_id
  }

  public_network_access_enabled = false

  tags = merge(var.tags, each.value.tags)

  lifecycle {
    precondition {
      condition     = !startswith(var.postgresql_servers[each.value.source_server].sku_name, "B_")
      error_message = "Burstable no admite réplicas de lectura."
    }
    precondition {
      condition = (
        var.postgresql_servers[each.value.source_server].customer_managed_key == null &&
        var.postgresql_servers[each.value.source_server].delegated_subnet_id == null
      )
      error_message = "Este root crea réplicas solo de servidores con private endpoint y clave del servicio."
    }
  }
}

module "postgresql_replica_private_endpoint" {
  source = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Networking/Networking/modules/private_endpoint?ref=main"
  for_each = merge([
    for k, v in var.postgresql_replicas : {
      for pk, p in v.private_endpoints : "${k}-${pk}" => merge(p, { replica = k, rg = v.resource_group_name, location = v.location })
    }
  ]...)

  private_endpoint_name          = "pe-${each.key}"
  custom_network_interface_name  = "nic-pe-${each.key}"
  resource_group_name            = each.value.rg
  location                       = each.value.location
  subnet_id                      = each.value.subnet_id
  private_connection_resource_id = azurerm_postgresql_flexible_server.replica[each.value.replica].id
  subresource_names              = ["postgresqlServer"]
  private_dns_zone_ids           = [each.value.private_dns_zone_id]
  tags                           = merge(var.tags, var.postgresql_replicas[each.value.replica].tags)
}

module "postgresql_replica_diagnostics" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Security/Seguridad/modules/monitor_diagnostic_setting?ref=main"
  for_each = var.postgresql_replicas

  monitor_diagnostic_setting_name = "diag-${each.key}"
  target_resource_id              = azurerm_postgresql_flexible_server.replica[each.key].id
  log_analytics_workspace_id      = var.postgresql_servers[each.value.source_server].log_analytics_workspace_id
  log_analytics_destination_type  = "Dedicated"
  enabled_logs                    = [{ category_group = "allLogs" }]
  enabled_metrics                 = [{ category = "AllMetrics" }]
}

resource "azurerm_postgresql_flexible_server_virtual_endpoint" "this" {
  for_each = { for k, v in var.postgresql_replicas : k => v if v.virtual_endpoint_name != null }

  name              = each.value.virtual_endpoint_name
  source_server_id  = azurerm_postgresql_flexible_server.this[each.value.source_server].id
  replica_server_id = azurerm_postgresql_flexible_server.replica[each.key].id
  type              = "ReadWrite"
}

# -----------------------------------------------------------------------------
# Salidas
# -----------------------------------------------------------------------------
output "postgresql_server_ids" {
  description = "IDs de los servidores."
  value       = { for k, s in azurerm_postgresql_flexible_server.this : k => s.id }
}

output "postgresql_fqdns" {
  description = "FQDN de cada servidor (5432 directo, 6432 con PgBouncer)."
  value       = { for k, s in azurerm_postgresql_flexible_server.this : k => s.fqdn }
}

output "postgresql_replica_ids" {
  description = "IDs de las réplicas de lectura."
  value       = { for k, s in azurerm_postgresql_flexible_server.replica : k => s.id }
}

output "postgresql_virtual_endpoint_ids" {
  description = "IDs de los virtual endpoints."
  value       = { for k, e in azurerm_postgresql_flexible_server_virtual_endpoint.this : k => e.id }
}

output "postgresql_admin_secret_ids" {
  description = "Secretos de Key Vault con la contraseña del administrador (si la hay)."
  value       = { for k, s in azurerm_key_vault_secret.postgresql_admin : k => s.versionless_id }
}
```

### `env/pro.tfvars`

Servidor zone-redundant con private endpoint y una réplica en otra región con virtual endpoint.

```hcl
tags = {
  environment = "pro"
  workload    = "<workload>"
  owner       = "<owner>"
  costcenter  = "<costcenter>"
}

postgresql_servers = {
  "psql-<workload>-pro-01" = {
    resource_group_name = "<rg-data-pro>"
    location            = "<region>"
    version             = "17"
    sku_name            = "GP_Standard_D4ds_v5"
    storage_mb          = 131072

    zone = "1"
    high_availability = {
      mode                      = "ZoneRedundant"
      standby_availability_zone = "2"
    }

    backup_retention_days = 35
    maintenance_window = {
      day_of_week = 0 # domingo
      start_hour  = 2
    }

    entra_admins = {
      "<grupo-dba-pro>" = { object_id = "<objectId grupo-dba-pro>" }
    }

    private_endpoints = {
      app = {
        subnet_id           = "<resourceId snet-pe-pro>"
        private_dns_zone_id = "<resourceId privatelink.postgres.database.azure.com>"
      }
    }

    databases = {
      appdb = {}
    }

    server_parameters = {
      "ssl_min_protocol_version" = "TLSv1.3" # solo si todos los clientes soportan TLS 1.3
      "logfiles.retention_days"  = "7"
      "pgbouncer.enabled"        = "true"
    }

    log_analytics_workspace_id = "<resourceId log-<workload>-pro>"
  }
}

# Réplica en otra región: la recuperación ante desastre cuando la región no tiene copia geo-redundante
postgresql_replicas = {
  "psql-<workload>-pro-dr-01" = {
    source_server       = "psql-<workload>-pro-01"
    resource_group_name = "<rg-data-pro-dr>"
    location            = "<region-dr>"
    zone                = "1"
    private_endpoints = {
      app = {
        subnet_id           = "<resourceId snet-pe-pro-dr>"
        private_dns_zone_id = "<resourceId privatelink.postgres.database.azure.com>"
      }
    }
    virtual_endpoint_name = "psql-<workload>-pro-ve"
  }
}
```

### Despliegue y comprobación

```powershell
terraform init
terraform plan -var-file="env/pro.tfvars" -out="pro.tfplan"
terraform apply "pro.tfplan"

Get-AzPostgreSqlFlexibleServer -ResourceGroupName "<rg-data-pro>" -Name "psql-<workload>-pro-01" | Format-List
Get-AzPostgreSqlFlexibleServerConfiguration -ResourceGroupName "<rg-data-pro>" -ServerName "psql-<workload>-pro-01" |
    Where-Object { $_.Name -in "require_secure_transport", "ssl_min_protocol_version", "pgbouncer.enabled" } |
    Select-Object Name, Value
```

Conexión con Entra (miembro del grupo administrador) y alta de la identidad de una aplicación:

```powershell
$env:PGPASSWORD = az account get-access-token --resource-type oss-rdbms --query accessToken -o tsv
psql "host=psql-<workload>-pro-01.postgres.database.azure.com port=5432 dbname=postgres user=<grupo-dba-pro> sslmode=verify-full"
```

```sql
-- En la base postgres
SELECT * FROM pgaadauth_create_principal('<identidad-de-la-app>', false, false);
```

Prueba de failover (fuera de horas, con al menos 15-20 minutos entre failovers):

```powershell
Restart-AzPostgreSqlFlexibleServer -ResourceGroupName "<rg-data-pro>" -Name "psql-<workload>-pro-01" `
    -RestartWithFailover -FailoverMode ForcedFailover
```

### Equivalente en Bicep

Una plantilla por servidor, con las réplicas en el mismo grupo de recursos. A diferencia de Terraform, admite **Premium SSD v2** con IOPS y throughput. Para el rol sobre el Key Vault de otro grupo de recursos usa `role-on-resource.bicep`, el mismo de las fichas de SQL.

`postgresql.bicep`:

```bicep
// =============================================================================
// Azure Database for PostgreSQL flexible server seguro por defecto: sin acceso público
// (private endpoint o integración en VNet), solo Microsoft Entra salvo que se pida contraseña,
// TLS obligatorio, alta disponibilidad entre zonas, Premium SSD o Premium SSD v2, clave del
// cliente opcional, diagnóstico en tablas dedicadas y réplicas de lectura con virtual endpoint
// DEPENDENCY: grupo de Entra administrador; zona privatelink.postgres.database.azure.com
// DEPENDENCY: Key Vault con purge protection en la misma región (si hay clave del cliente)
// DEPENDENCY: role-on-resource.bicep en la misma carpeta
// =============================================================================
@minLength(3)
@maxLength(63)
param name string
param location string = resourceGroup().location

@allowed(['14', '15', '16', '17', '18'])
param version string

@description('{ name (Standard_D4ds_v5), tier (Burstable | GeneralPurpose | MemoryOptimized) }')
param sku object

@description('{ sizeGb, type (Premium_LRS | PremiumV2_LRS), autoGrow? (por defecto solo en Premium_LRS), tier?, iops?, throughput? }')
param storage object

param zone string
@description('{ mode (ZoneRedundant | SameZone), standbyZone? }; vacío = sin alta disponibilidad')
param highAvailability object = {}

@minValue(7)
@maxValue(35)
param backupRetentionDays int = 7
param geoRedundantBackup bool = false

@description('{ dayOfWeek, startHour, startMinute? }; vacío = ventana del sistema')
param maintenanceWindow object = {}

@description('[{ objectId, principalName, principalType (Group | User | ServicePrincipal) }]')
@minLength(1)
param entraAdmins array

param passwordAuth bool = false
param administratorLogin string = ''
@secure()
param administratorPassword string = ''

@description('[{ name, subnetId, privateDnsZoneId }] (acceso público deshabilitado)')
param privateEndpoints array = []
@description('Integración en VNet: { subnetId, privateDnsZoneId }; vacío = private endpoints')
param vnetIntegration object = {}

@description('Clave del cliente: { keyVaultId, keyUri (sin versión = rotación automática) }')
param customerManagedKey object = {}

@description('{ nombre: { charset?, collation? } }')
param databases object = {}

@description('Parámetros del servidor { nombre: valor }; require_secure_transport siempre on')
param serverParameters object = {}

param logAnalyticsWorkspaceId string

@description('[{ name, location, zone?, privateEndpoints: [{ name, subnetId, privateDnsZoneId }] }] en este grupo de recursos')
param replicas array = []
@description('Nombre del virtual endpoint ReadWrite (requiere al menos una réplica)')
param virtualEndpointName string = ''

param tags object = {}

var useCmk = !empty(customerManagedKey)
var useVnet = !empty(vnetIntegration)
var parameters = union(
  {
    'pg_qs.query_capture_mode': 'top'
    'pgms_wait_sampling.query_capture_mode': 'all'
  },
  serverParameters,
  {
    require_secure_transport: 'on'
  }
)

resource identity 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = if (useCmk) {
  name: 'id-${name}'
  location: location
  tags: tags
}

module cmkRole 'role-on-resource.bicep' = if (useCmk) {
  name: '${take(name, 45)}-cmk-role'
  scope: resourceGroup(
    split(customerManagedKey.?keyVaultId ?? '/s/x/r/x', '/')[2],
    split(customerManagedKey.?keyVaultId ?? '/s/x/r/x', '/')[4]
  )
  params: {
    resourceId: customerManagedKey.keyVaultId
    roleDefinitionId: 'e147488a-f6f5-4113-8e2d-b22465e65bf6' // Key Vault Crypto Service Encryption User
    principalId: identity!.properties.principalId
    description: 'Cifrado con clave del cliente de ${name}'
  }
}

resource server 'Microsoft.DBforPostgreSQL/flexibleServers@2025-08-01' = {
  name: name
  location: location
  tags: tags
  sku: {
    name: sku.name
    tier: sku.tier
  }
  identity: useCmk
    ? {
        type: 'UserAssigned'
        userAssignedIdentities: {
          '${identity.id}': {}
        }
      }
    : null
  properties: {
    createMode: 'Create'
    version: version
    storage: {
      storageSizeGB: storage.sizeGb
      type: storage.type
      autoGrow: (storage.?autoGrow ?? storage.type == 'Premium_LRS') ? 'Enabled' : 'Disabled'
      tier: storage.?tier
      iops: storage.type == 'PremiumV2_LRS' ? storage.?iops : null
      throughput: storage.type == 'PremiumV2_LRS' ? storage.?throughput : null
    }
    availabilityZone: zone
    highAvailability: empty(highAvailability)
      ? {
          mode: 'Disabled'
        }
      : {
          mode: highAvailability.mode
          standbyAvailabilityZone: highAvailability.?standbyZone
        }
    backup: {
      backupRetentionDays: backupRetentionDays
      geoRedundantBackup: geoRedundantBackup ? 'Enabled' : 'Disabled'
    }
    maintenanceWindow: empty(maintenanceWindow)
      ? {
          customWindow: 'Disabled'
        }
      : {
          customWindow: 'Enabled'
          dayOfWeek: maintenanceWindow.dayOfWeek
          startHour: maintenanceWindow.startHour
          startMinute: maintenanceWindow.?startMinute ?? 0
        }
    authConfig: {
      activeDirectoryAuth: 'Enabled'
      passwordAuth: passwordAuth ? 'Enabled' : 'Disabled'
      tenantId: tenant().tenantId
    }
    administratorLogin: passwordAuth ? administratorLogin : null
    administratorLoginPassword: passwordAuth ? administratorPassword : null
    network: {
      publicNetworkAccess: 'Disabled'
      delegatedSubnetResourceId: useVnet ? vnetIntegration.subnetId : null
      privateDnsZoneArmResourceId: useVnet ? vnetIntegration.privateDnsZoneId : null
    }
    dataEncryption: useCmk
      ? {
          type: 'AzureKeyVault'
          primaryKeyURI: customerManagedKey.keyUri
          primaryUserAssignedIdentityId: identity.id
        }
      : {
          type: 'SystemManaged'
        }
  }
  dependsOn: [
    cmkRole
  ]
}

// Administradores de Entra antes que las bases, para que puedan ser propietarios
@batchSize(1)
resource admins 'Microsoft.DBforPostgreSQL/flexibleServers/administrators@2025-08-01' = [
  for a in entraAdmins: {
    parent: server
    name: a.objectId
    properties: {
      principalType: a.principalType
      principalName: a.principalName
      tenantId: tenant().tenantId
    }
  }
]

// Parámetros de uno en uno, sin actualizaciones simultáneas sobre el servidor
@batchSize(1)
resource configurations 'Microsoft.DBforPostgreSQL/flexibleServers/configurations@2025-08-01' = [
  for p in items(parameters): {
    parent: server
    name: p.key
    properties: {
      value: p.value
      source: 'user-override'
    }
    dependsOn: [
      admins
    ]
  }
]

resource dbs 'Microsoft.DBforPostgreSQL/flexibleServers/databases@2025-08-01' = [
  for d in items(databases): {
    parent: server
    name: d.key
    properties: {
      charset: d.value.?charset ?? 'UTF8'
      collation: d.value.?collation ?? 'en_US.utf8'
    }
    dependsOn: [
      admins
      configurations
    ]
  }
]

resource pes 'Microsoft.Network/privateEndpoints@2024-05-01' = [
  for pe in privateEndpoints: if (!useVnet) {
    name: 'pe-${name}-${pe.name}'
    location: location
    tags: tags
    properties: {
      subnet: {
        id: pe.subnetId
      }
      customNetworkInterfaceName: 'nic-pe-${name}-${pe.name}'
      privateLinkServiceConnections: [
        {
          name: 'postgresqlServer'
          properties: {
            privateLinkServiceId: server.id
            groupIds: [
              'postgresqlServer'
            ]
          }
        }
      ]
    }
  }
]

resource peDns 'Microsoft.Network/privateEndpoints/privateDnsZoneGroups@2024-05-01' = [
  for (pe, i) in privateEndpoints: if (!useVnet) {
    parent: pes[i]
    name: 'default'
    properties: {
      privateDnsZoneConfigs: [
        {
          name: 'postgres'
          properties: {
            privateDnsZoneId: pe.privateDnsZoneId
          }
        }
      ]
    }
  }
]

resource diagnostics 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = {
  name: 'diag-${name}'
  scope: server
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

// Réplicas de lectura simétricas con el origen (sin alta disponibilidad ni copias propias)
resource replicaServers 'Microsoft.DBforPostgreSQL/flexibleServers@2025-08-01' = [
  for r in replicas: if (!useCmk && !useVnet && sku.tier != 'Burstable') {
    name: r.name
    location: r.location
    tags: tags
    sku: {
      name: sku.name
      tier: sku.tier
    }
    properties: {
      createMode: 'Replica'
      sourceServerResourceId: server.id
      availabilityZone: r.?zone
      storage: {
        storageSizeGB: storage.sizeGb
        type: storage.type
        autoGrow: (storage.?autoGrow ?? storage.type == 'Premium_LRS') ? 'Enabled' : 'Disabled'
      }
      network: {
        publicNetworkAccess: 'Disabled'
      }
    }
    dependsOn: [
      dbs
    ]
  }
]

resource replicaPes 'Microsoft.Network/privateEndpoints@2024-05-01' = [
  for (r, i) in replicas: if (!useCmk && !useVnet && sku.tier != 'Burstable') {
    name: 'pe-${r.name}-${r.privateEndpoints[0].name}'
    location: r.location
    tags: tags
    properties: {
      subnet: {
        id: r.privateEndpoints[0].subnetId
      }
      customNetworkInterfaceName: 'nic-pe-${r.name}-${r.privateEndpoints[0].name}'
      privateLinkServiceConnections: [
        {
          name: 'postgresqlServer'
          properties: {
            privateLinkServiceId: replicaServers[i].id
            groupIds: [
              'postgresqlServer'
            ]
          }
        }
      ]
    }
  }
]

resource replicaPeDns 'Microsoft.Network/privateEndpoints/privateDnsZoneGroups@2024-05-01' = [
  for (r, i) in replicas: if (!useCmk && !useVnet && sku.tier != 'Burstable') {
    parent: replicaPes[i]
    name: 'default'
    properties: {
      privateDnsZoneConfigs: [
        {
          name: 'postgres'
          properties: {
            privateDnsZoneId: r.privateEndpoints[0].privateDnsZoneId
          }
        }
      ]
    }
  }
]

resource replicaDiagnostics 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = [
  for (r, i) in replicas: if (!useCmk && !useVnet && sku.tier != 'Burstable') {
    name: 'diag-${r.name}'
    scope: replicaServers[i]
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
]

resource virtualEndpoint 'Microsoft.DBforPostgreSQL/flexibleServers/virtualEndpoints@2025-08-01' = if (!empty(virtualEndpointName) && !empty(replicas)) {
  parent: server
  name: virtualEndpointName
  properties: {
    endpointType: 'ReadWrite'
    members: [
      replicas[0].name
    ]
  }
  dependsOn: [
    replicaServers
  ]
}

output serverId string = server.id
output fqdn string = server.properties.fullyQualifiedDomainName
output replicaIds array = [for (r, i) in replicas: replicaServers[i].id]
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

`psql-workload-pro-01.bicepparam`:

```bicep
using 'postgresql.bicep'

param name = 'psql-<workload>-pro-01'
param version = '17'
param sku = {
  name: 'Standard_D4ds_v5'
  tier: 'GeneralPurpose'
}

// Premium SSD v2: IOPS y throughput independientes del tamaño (Terraform no lo soporta)
param storage = {
  sizeGb: 128
  type: 'PremiumV2_LRS'
  iops: 3000
  throughput: 125
}

param zone = '1'
param highAvailability = {
  mode: 'ZoneRedundant'
  standbyZone: '2'
}

param backupRetentionDays = 35
param maintenanceWindow = {
  dayOfWeek: 0
  startHour: 2
}

param entraAdmins = [
  {
    objectId: '<objectId grupo-dba-pro>'
    principalName: '<grupo-dba-pro>'
    principalType: 'Group'
  }
]

param privateEndpoints = [
  {
    name: 'app'
    subnetId: '<resourceId snet-pe-pro>'
    privateDnsZoneId: '<resourceId privatelink.postgres.database.azure.com>'
  }
]

param databases = {
  appdb: {}
}

param serverParameters = {
  ssl_min_protocol_version: 'TLSv1.3' // solo si todos los clientes soportan TLS 1.3
  'logfiles.retention_days': '7'
  'pgbouncer.enabled': 'true'
}

param logAnalyticsWorkspaceId = '<resourceId log-<workload>-pro>'

param replicas = [
  {
    name: 'psql-<workload>-pro-dr-01'
    location: '<region-dr>'
    zone: '1'
    privateEndpoints: [
      {
        name: 'app'
        subnetId: '<resourceId snet-pe-pro-dr>'
        privateDnsZoneId: '<resourceId privatelink.postgres.database.azure.com>'
      }
    ]
  }
]
param virtualEndpointName = 'psql-<workload>-pro-ve'

param tags = {
  environment: 'pro'
  workload: '<workload>'
}
```

Despliegue:

```powershell
New-AzResourceGroupDeployment -ResourceGroupName "<rg-data-pro>" `
    -TemplateParameterFile "psql-workload-pro-01.bicepparam" -Name "psql-<workload>-pro-01"
```

## Errores típicos

| Síntoma | Causa | Solución |
|---|---|---|
| `The variable name "version" is reserved` en `terraform init` | Módulo `Database/PostgreSQLFlexible` del repositorio | Recurso nativo (o renombrar la variable en el módulo) |
| `terraform plan` quiere abrir el acceso público | `public_network_access_enabled` omitido (por defecto `true`) | Declararlo `false` |
| `terraform plan` quiere recrear el servidor | Cambio de `delegated_subnet_id`, clave del cliente o copia geo-redundante (ForceNew), o se migró de VNet a private endpoint y el código no | Alinear el código; esas decisiones son de creación |
| Drift en la zona tras un failover | El standby pasó a primario y las zonas se invirtieron | `ignore_changes` en las zonas (ya incluido) |
| El servidor pasa a solo lectura | 95 % del disco o menos de 5 GiB libres | Crecimiento automático o ampliar; `SET SESSION CHARACTERISTICS AS TRANSACTION READ WRITE` para borrar datos |
| El crecimiento automático no salta | Cruza 4.096 GiB o hay mucho WAL | Ampliación manual (offline al cruzar ese límite) |
| El servidor deja de responder en Burstable | Créditos de CPU agotados | Alerta sobre *CPU Credits Remaining*; subir de tamaño o de nivel |
| Server **Inaccessible** | Clave del cliente deshabilitada, caducada, borrada o bloqueada por el firewall del Key Vault | Restaurar el acceso y esperar a la revalidación (hasta 60 minutos) |
| Un usuario de Entra no conecta | Nombre distinto (sensible a mayúsculas), token caducado o rol no creado | Nombre exacto del grupo o UPN; token justo antes de conectar; `pgaadauth_create_principal` |
| Se recrea un usuario de Entra con el mismo nombre y no entra | El rol se asocia al ID del objeto, no al nombre | Transferir propiedad y volver a crear el rol |
| Fallo de TLS en clientes tras una rotación | Pinning o certificados intermedios en el almacén | Solo las raíces DigiCert Global Root G2 y Microsoft RSA Root CA 2017 |
| Query Performance Insight vacío | Query Store desactivado o diagnóstico sin las categorías | `pg_qs.query_capture_mode` y `pgms_wait_sampling.query_capture_mode`; categorías en Log Analytics |
| No se puede activar la alta disponibilidad | Nivel Burstable | General Purpose o Memory Optimized |
| La actualización de versión mayor se bloquea | El servidor tiene réplicas | Borrarlas, actualizar y volver a crearlas |
| `Unable to complete the operation because the disk is still being hydrated` | Operaciones seguidas sobre Premium SSD v2 | Espaciar escalados, alta disponibilidad y réplicas |
| La restauración no conecta | Las reglas, endpoints y parámetros no se copian | Recrearlos en el servidor nuevo |
