---
title: "MySQL Flexible Server"
indice: database
resumen: "MySQL gestionado con alta disponibilidad."
estado: documentado   # proximamente | en-curso | documentado
orden: 5
last_review: 2026-11-12
fuentes:
  - titulo: "What is Azure Database for MySQL flexible server?"
    url: https://learn.microsoft.com/azure/mysql/flexible-server/overview
  - titulo: "Azure Database for MySQL version support policy"
    url: https://learn.microsoft.com/azure/mysql/concepts-version-policy
  - titulo: "What's new in Azure Database for MySQL flexible server in 2026?"
    url: https://learn.microsoft.com/azure/mysql/whats-new/whats-new-2026
  - titulo: "Major version upgrade in Azure Database for MySQL"
    url: https://learn.microsoft.com/azure/mysql/flexible-server/how-to-upgrade
  - titulo: "Azure Database for MySQL - Flexible Server service tiers"
    url: https://learn.microsoft.com/azure/mysql/flexible-server/concepts-service-tiers-storage
  - titulo: "Storage IOPS in Azure Database for MySQL - Flexible Server"
    url: https://learn.microsoft.com/azure/mysql/flexible-server/concepts-storage-iops
  - titulo: "Server concepts in Azure Database for MySQL - Flexible Server"
    url: https://learn.microsoft.com/azure/mysql/flexible-server/concept-servers
  - titulo: "Connectivity and networking concepts for Azure Database for MySQL - Flexible Server"
    url: https://learn.microsoft.com/azure/mysql/flexible-server/concepts-networking
  - titulo: "Private Network Access using virtual network integration for Azure Database for MySQL - Flexible Server"
    url: https://learn.microsoft.com/azure/mysql/flexible-server/concepts-networking-vnet
  - titulo: "Private Link for Azure Database for MySQL - Flexible Server"
    url: https://learn.microsoft.com/azure/mysql/flexible-server/concepts-networking-private-link
  - titulo: "Azure Private Endpoint private DNS zone values"
    url: https://learn.microsoft.com/azure/private-link/private-endpoint-dns
  - titulo: "Microsoft Entra authentication for Azure Database for MySQL - Flexible Server"
    url: https://learn.microsoft.com/azure/mysql/security/security-entra-authentication
  - titulo: "Set up Microsoft Entra authentication for Azure Database for MySQL - Flexible Server"
    url: https://learn.microsoft.com/azure/mysql/security/security-how-to-entra
  - titulo: "Transport Layer Security (TLS) in Azure Database for MySQL"
    url: https://learn.microsoft.com/azure/mysql/security/security-tls
  - titulo: "Connect to Azure Database for MySQL - Flexible Server with encrypted connections"
    url: https://learn.microsoft.com/azure/mysql/security/security-tls-how-to-connect
  - titulo: "Data encryption with customer managed keys for Azure Database for MySQL"
    url: https://learn.microsoft.com/azure/mysql/security/security-customer-managed-key
  - titulo: "Secure your Azure Database for MySQL"
    url: https://learn.microsoft.com/azure/mysql/security/security-overview
  - titulo: "Enable Defender for open-source relational databases on Azure"
    url: https://learn.microsoft.com/azure/defender-for-cloud/enable-defender-for-databases-azure
  - titulo: "High availability in Azure Database for MySQL"
    url: https://learn.microsoft.com/azure/mysql/flexible-server/concepts-high-availability
  - titulo: "High-availability (HA) frequently asked questions (FAQ) in Azure Database for MySQL"
    url: https://learn.microsoft.com/azure/mysql/flexible-server/concepts-high-availability-faq
  - titulo: "Reliability in Azure Database for MySQL"
    url: https://learn.microsoft.com/azure/reliability/reliability-database-mysql
  - titulo: "Backup and restore in Azure Database for MySQL"
    url: https://learn.microsoft.com/azure/mysql/flexible-server/concepts-backup-restore
  - titulo: "Overview of business continuity with Azure Database for MySQL - Flexible Server"
    url: https://learn.microsoft.com/azure/mysql/flexible-server/concepts-business-continuity
  - titulo: "Read replicas in Azure Database for MySQL"
    url: https://learn.microsoft.com/azure/mysql/flexible-server/concepts-read-replicas
  - titulo: "Monitor Azure Database for MySQL - Flexible Server"
    url: https://learn.microsoft.com/azure/mysql/flexible-server/concepts-monitor-mysql
  - titulo: "Tutorial: Configure audit logs by using Azure Database for MySQL - Flexible Server"
    url: https://learn.microsoft.com/azure/mysql/flexible-server/tutorial-configure-audit
  - titulo: "Supported logs for Microsoft.DBforMySQL/flexibleServers"
    url: https://learn.microsoft.com/azure/azure-monitor/reference/supported-logs/microsoft-dbformysql-flexibleservers-logs
  - titulo: "Architecture best practices for Azure Database for MySQL"
    url: https://learn.microsoft.com/azure/well-architected/service-guides/azure-database-for-mysql
  - titulo: "Microsoft.DBforMySQL flexibleServers 2024-12-30 (plantillas ARM/Bicep)"
    url: https://learn.microsoft.com/azure/templates/microsoft.dbformysql/2024-12-30/flexibleservers
  - titulo: "Microsoft.DBforMySQL flexibleServers/administrators 2024-12-30"
    url: https://learn.microsoft.com/azure/templates/microsoft.dbformysql/2024-12-30/flexibleservers/administrators
  - titulo: "Microsoft.DBforMySQL flexibleServers 2025-06-01-preview"
    url: https://learn.microsoft.com/azure/templates/microsoft.dbformysql/2025-06-01-preview/flexibleservers
  - titulo: "Az.MySql (PowerShell)"
    url: https://learn.microsoft.com/powershell/module/az.mysql/
  - titulo: "azurerm_mysql_flexible_server"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/mysql_flexible_server
  - titulo: "azurerm_mysql_flexible_server_active_directory_administrator"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/mysql_flexible_server_active_directory_administrator
  - titulo: "Módulo Terraform Database/MySQLFlexible"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Database/MySQLFlexible
  - titulo: "Módulo Terraform PRO/services/mysql_flexible_server"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/PRO/services/mysql_flexible_server
  - titulo: "Módulo Terraform Networking/Networking/modules/private_endpoint"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Networking/Networking/modules/private_endpoint
  - titulo: "Módulo Terraform Security/Seguridad/modules/monitor_diagnostic_setting"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Security/Seguridad/modules/monitor_diagnostic_setting
---

**Azure Database for MySQL flexible server** es MySQL Community Edition (InnoDB) gestionado. Azure se encarga del SO, de los parches menores, de las copias y de la alta disponibilidad. Tú decides la red, la ventana de mantenimiento, los parámetros del motor y el tamaño. El cómputo escala en segundos y el servidor se puede **parar** hasta 30 días sin pagar cómputo. Para PostgreSQL está [PostgreSQL Flexible Server](/recursos/database/postgresql-flexible-server/); para SQL Server, [Azure SQL Database](/recursos/database/azure-sql-database/).

## Qué es y cuándo usarlo

### Versiones

| Versión | Estado |
|---|---|
| **8.4** | Soportada; la opción para servidores nuevos |
| 8.0 | Soportada hasta el **31 de enero de 2027**; desde el 1 de febrero, soporte extendido de pago hasta el 31 de mayo de 2029 |
| 5.7 | **Soporte extendido de pago desde el 1 de octubre de 2026** (alta y cobro automáticos) |
| 9.5 | Preview (*innovation release*): sin alta disponibilidad, réplicas ni copias; el servidor se borra a los 30 días |

- El soporte extendido se cobra por vCore y hora, también en réplicas y standby. **Parado no se cobra**.
- La actualización de versión mayor es en el sitio y **no tiene vuelta atrás**: copia bajo demanda antes. Hay validación previa de 8.0 a 8.4 en preview (noviembre de 2026).
- En 8.4 el plugin de autenticación por defecto es `caching_sha2_password`: revisa los conectores de las aplicaciones.

### Niveles de cómputo

| Nivel | Series | Para qué | Límites |
|---|---|---|---|
| **Burstable** | B1ms a B20ms | Desarrollo, pruebas, bases pequeñas | **No es para producción**. Sin alta disponibilidad ni réplicas, ni intervalo de copia ajustable |
| **General Purpose** | Ddsv4, Dadsv5 (2 a 96 vCores) | La mayoría de cargas | — |
| **Memory Optimized** | Edsv4, Edsv5, Eadsv5 (2 a 96 vCores) | Alta concurrencia, caché grande | — |

- Cambiar el tamaño de cómputo **reinicia el servidor** (60-120 segundos); ampliar almacenamiento es en línea.
- El máximo de conexiones depende del tamaño (B1ms: 341; D4ads_v5: 2.731).
- Hay oferta gratuita de 12 meses con la cuenta gratuita de Azure: B1ms 750 horas y 32 GB.

### Almacenamiento e IOPS

| Aspecto | Detalle |
|---|---|
| Tamaño | 20 GiB a 16 TiB (Memory Optimized hasta 32 TiB), de GiB en GiB. **Solo crece** |
| Crecimiento automático | Activo por defecto: +5 GB por debajo de 100 GB, +5 % por encima. **Obligatorio con alta disponibilidad** |
| IOPS | Mínimo 360; máximo según el tamaño de cómputo (hasta 80.000 en Memory Optimized) |
| Modos | **Preaprovisionadas** (fijas, pagas las asignadas) o **autoescalado** (pagas las que usas) |

**Solo lectura**: con 100 GiB o menos, cuando queda menos del 5 % libre; por encima, cuando quedan menos de 5 GiB. Crecimiento automático o alerta sobre `storage_percent`.

### Red

El método de conectividad **se elige al crear y no se cambia** después:

| Modo | Cómo | Cuándo |
|---|---|---|
| **Acceso público + private endpoint** | Acceso público deshabilitado y private endpoints (`mysqlServer`, zona `privatelink.mysql.database.azure.com`) | **Opción por defecto**: hub and spoke, varias VNets |
| Integración en VNet | Subred delegada a `Microsoft.DBforMySQL/flexibleServers` (mínimo /29; 2 IPs por servidor con alta disponibilidad); zona privada que termine en `mysql.database.azure.com` | Diseños existentes; sin endpoint público |

- Private Link solo existe en servidores creados con **acceso público**; con el acceso deshabilitado solo entran los endpoints.
- Se puede pasar de VNet a acceso público o Private Link **sin vuelta atrás**, con 5-10 minutos de corte (unos 20 con alta disponibilidad).
- En VNet no se mueve de subred ni se cambia la zona DNS privada después.
- Borra los private endpoints antes que el servidor. Conecta **siempre por FQDN**: la IP puede cambiar.

### Seguridad

| Control | Recomendación |
|---|---|
| Autenticación | Microsoft Entra con un **grupo** como administrador (MySQL admite **uno solo**). `aad_auth_only = ON` deja fuera las contraseñas. La contraseña del administrador inicial es obligatoria al crear: a Key Vault como cuenta de emergencia |
| Identidad | Entra exige una **identidad asignada por el usuario** con `User.Read.All`, `GroupMember.Read.All` y `Application.Read.All` en Graph (o *Directory Readers*), concedidos por un *Privileged Role Administrator* |
| Tokens | Audiencia `ossrdbms`: desde enero de 2027 se rechazan otras audiencias. Los tokens duran de 5 a 60 minutos |
| TLS | `require_secure_transport = ON` (por defecto); TLS 1.2 por defecto y **TLS 1.3 recomendado** en 8.0 y posteriores. `tls_version` es estático (reinicia). Sin mTLS ni certificados propios |
| Clientes | Validación completa con las raíces DigiCert Global Root G2 y Microsoft RSA Root CA 2017. **Nada de pinning** ni intermedias |
| Cifrado | AES-256 siempre; clave del cliente opcional (ver abajo) |
| Auditoría | `audit_log_enabled = ON`, eventos según cumplimiento y categoría `MySqlAuditLogs` a Log Analytics. Hay un libro de auditoría integrado |
| Defender | **Defender for open-source relational databases** (todos los niveles) |

**Clave del cliente**: a diferencia de PostgreSQL, se puede activar o cambiar en un servidor existente. Requisitos:

- Key Vault en la misma región y tenant, con soft delete y purge protection.
- Rol *Key Vault Crypto Service Encryption User* para la identidad.
- Si se pierde el acceso a la clave, el servidor rechaza conexiones en **10 minutos** y pasa a **Inaccessible**. Una clave **caducada** no lo bloquea.
- La copia geo-redundante necesita otra clave e identidad en la región emparejada.

### Alta disponibilidad

| Configuración | Comportamiento |
|---|---|
| **Zone-redundant** | Standby en otra zona, replicación síncrona: **RPO 0**, failover en 60-120 segundos. **Solo al crear** |
| Same-zone (local) | Standby en la misma zona, menos latencia; se activa también después. No protege de la caída de la zona |
| Sin alta disponibilidad | Un servidor; ante fallo de zona, restauración geo o réplica |

- El standby es pasivo (no lee ni escribe) y **se paga igual que el primario**.
- Zone-redundant añade entre un 5 y un 10 % de latencia de escritura.
- Sin alta disponibilidad en Burstable. Con ella, GTID activo y crecimiento automático obligatorio. Reiniciar por un parámetro estático reinicia también el standby.
- **Claves primarias en todas las tablas** y nada de borrados en cascada multitabla (bug 102586 de MySQL): pueden romper la replicación.
- El SLA de cada configuración está en la página de SLA de MySQL, enlazada desde las preguntas frecuentes de alta disponibilidad.

### Copias y recuperación

| Opción | Detalle |
|---|---|
| **Copias automáticas** | Snapshot diario más log cada 5 minutos; retención de 1 a 35 días (7 por defecto). LRS por defecto, **ZRS con zone-redundant** |
| Copia geo-redundante | Restauración en otra región con RPO de hasta 1 hora. **Spain Central no la ofrece**. Desde ZRS solo se activa al crear |
| Réplicas de lectura | Hasta **10**, asíncronas, en cualquier región. La recuperación ante desastre es **manual**: se detiene la replicación y se cambia la cadena de conexión |
| *Reader endpoint* | Preview: un DNS para repartir lecturas entre réplicas; aún sin réplicas geográficas |
| Copias bajo demanda | Hasta 50 |
| Retención a largo plazo | Con Azure Backup, en preview y **pausada** a fecha de revisión |

- Restaurar **crea un servidor nuevo**, sin alta disponibilidad; `time_zone` y `event_scheduler` vuelven al valor por defecto.
- Un servidor borrado se recupera durante **5 días**. Aun así, **bloqueo de recurso** en producción.
- Las réplicas heredan el método de red y las cuentas del origen. No tienen alta disponibilidad, tampoco al promocionarse. No se puede parar un servidor con réplicas.
- No cambies variables como `foreign_key_checks` en sesión: rompen la restauración a un punto en el tiempo y la replicación.

### Cómo se factura

| Concepto | Detalle |
|---|---|
| Cómputo | Por vCore y hora según nivel y serie. **Parado no se cobra**; arranca solo a los 30 días |
| Alta disponibilidad | El standby al mismo precio que el primario |
| Almacenamiento | Por GiB aprovisionado, también parado |
| IOPS | Preaprovisionadas por encima de las incluidas, o por uso con autoescalado |
| Copias | Gratis hasta el 100 % del almacenamiento aprovisionado; la geo-redundante cuenta doble |
| Réplicas | Cómputo y almacenamiento propios más tráfico entre regiones |
| Reservas | 1 o 3 años de cómputo con descuento |
| Soporte extendido | 5.7 desde octubre de 2026; 8.0 desde febrero de 2027 |

### Qué escenario recomiendo

| Escenario del cliente | Diseño | Por qué |
|---|---|---|
| Producción crítica | General Purpose o Memory Optimized 8.4, zone-redundant, private endpoint, solo Entra | RPO 0 en zona, sin contraseñas ni exposición |
| Recuperación ante desastre en Spain Central | Réplica en otra región con private endpoint propio | La región no tiene copia geo-redundante |
| Carga con picos | Autoescalado de IOPS | Pagas lo que usas sin throttling |
| Carga estable e intensiva | IOPS preaprovisionadas | Rendimiento predecible |
| Lecturas que no caben en un servidor | Réplicas (*reader endpoint* cuando salga de preview) | Escalado horizontal de lecturas |
| Desarrollo y pruebas | Burstable parado fuera de horario | Sin coste de cómputo parado |
| Servidores en 5.7 u 8.0 | Actualización a 8.4 con validación previa | Fuera del soporte extendido de pago |
| Aplicaciones en [Container Apps](/recursos/compute/container-apps/) | Identidad gestionada como usuario de Entra (`CREATE AADUSER`) | Sin secretos en la aplicación |

### Datos que conviene llevar a la reunión

- **Red y alta disponibilidad zone-redundant se deciden al crear.**
- **Spain Central no tiene copia geo-redundante**: la recuperación regional va con réplicas.
- **5.7 ya paga soporte extendido y 8.0 lo pagará desde febrero de 2027.**
- **Entra necesita permisos de Graph** que concede un administrador de roles privilegiados.
- **Burstable no es para producción** ni tiene alta disponibilidad.
- **Disco casi lleno = solo lectura.**
- **Parado no paga cómputo, pero arranca solo a los 30 días.**

## Decisiones de diseño

| Decisión | Lo que aplico | Por qué |
|---|---|---|
| Servidor | Recurso nativo `azurerm_mysql_flexible_server` | Los dos módulos del repositorio no sirven (ver abajo) |
| Red | Private endpoint por defecto; integración en VNet como alternativa (uno u otro, validado) | El método no se cambia después |
| Acceso público | `public_network_access = "Disabled"` explícito | `public_network_access_enabled` es solo lectura en azurerm 4.x |
| Identidad | Una identidad de usuario por servidor, siempre | La necesitan Entra y la clave del cliente |
| Autenticación | Contraseña generada a Key Vault; `aad_auth_only = ON` tras crear el administrador de Entra | Sin secretos en el código y sin bloquearse fuera |
| TLS | `require_secure_transport = ON` forzado (validado) | No se puede desactivar por error |
| Auditoría | `audit_log_enabled` y `slow_query_log` en `ON` | Sin ellos, `MySqlAuditLogs` y `MySqlSlowLogs` van vacías |
| Diagnóstico | Las dos categorías + `AllMetrics` | Son todas las que publica el servicio |
| Alta disponibilidad | Zonas distintas y crecimiento automático (validado); `ignore_changes` en zonas | Tras un failover las zonas se intercambian |
| IOPS | Fijas o autoescalado, nunca ambas (validado) | El provider lo rechaza en el apply |
| Réplicas | Simétricas con el origen y con private endpoint propio | Recuperación regional |
| Versiones | 8.0.21 y 8.4 (validado) | 5.7 está en soporte extendido de pago |

Alineación con el Well-Architected Framework:

- **Fiabilidad**: zone-redundant, réplicas entre regiones y retención de copias.
- **Seguridad**: red privada, Entra, TLS, auditoría, clave del cliente y Defender.
- **Coste**: niveles por entorno, parada, autoescalado de IOPS y reservas.
- **Excelencia operativa**: IaC con validaciones, pruebas y diagnóstico.
- **Rendimiento**: consultas lentas, IOPS ajustables y réplicas de lectura.

## Módulo de Terraform

### Los módulos del repositorio

[Database/MySQLFlexible](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Database/MySQLFlexible) **no inicializa**: declara `variable "version"`, un nombre reservado (`Invalid variable name`). Es el mismo fallo que los módulos de SQL Server y PostgreSQL. Además:

- Declara `public_network_access_enabled` pero **no la usa**: el servidor queda con el valor por defecto de Azure.
- Solo admite 5.7 y 8.0.21 (no 8.4). La contraseña entra como variable.
- No tiene administrador de Entra, diagnóstico ni private endpoints. Usa `locals`.

[PRO/services/mysql_flexible_server](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/PRO/services/mysql_flexible_server) guarda la contraseña en Key Vault, pero:

- Tiene el acceso público comentado y la versión 8.0.21 fija.
- Su private endpoint (`mysqlServer`) no tiene grupo de zona DNS.
- No tiene Entra. Fija `random` en 3.1.3 y la variable se llama `commom_tags`.

Por eso el servidor va con el recurso nativo. Se reutilizan `private_endpoint`, `monitor_diagnostic_setting` y `PRO/common/assigned_identity`.

Notas del provider (azurerm 4.81, API 2023-12-30):

- **`public_network_access_enabled` es solo lectura**; el argumento es `public_network_access` (`Enabled`/`Disabled`). Si se omite, Azure lo deja `Enabled` salvo en VNet.
- `size_gb` llega a 16.384: **no admite los 32 TiB** de Memory Optimized.
- `iops` llega a 48.000: no admite los máximos de los tamaños grandes de Memory Optimized.
- La expresión de `sku_name` **no está anclada** en todas sus alternativas y le falta **D96ads_v5**.
- `administrator_login`, `delegated_subnet_id`, `private_dns_zone_id` y `geo_redundant_backup_enabled` son ForceNew.
- `iops` con `io_scaling_enabled` falla en el apply.
- `administrator_password_wo` evita la contraseña en el estado, pero exige Terraform 1.11 o posterior.

### Estructura en el proyecto

```txt
/
├── providers.tf          # azurerm >= 4.81.0, random
├── mysql_flexible.tf     # identidad, contraseña, servidor, Entra, parámetros, bases, endpoints, diagnóstico y réplicas
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
      # Validado con 4.81.0 (MySQL 8.4, public_network_access y administrador de Entra con identidad).
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

### `mysql_flexible.tf`

```hcl
# =============================================================================
# Azure Database for MySQL flexible server seguro por defecto: sin acceso público
# (private endpoint o integración en VNet), administrador de Microsoft Entra con identidad
# asignada por el usuario, solo Entra salvo que se pida contraseña (aad_auth_only), TLS
# obligatorio, auditoría y consultas lentas, alta disponibilidad entre zonas, clave del cliente
# opcional y réplicas de lectura en otra región
#
# DEPENDENCY: grupos de recursos creados
# DEPENDENCY: grupo de Microsoft Entra para el administrador (MySQL admite uno solo)
# DEPENDENCY: la identidad id-<servidor> necesita User.Read.All, GroupMember.Read.All y
#             Application.Read.All en Microsoft Graph (o el rol Directory Readers), concedidos por
#             un Privileged Role Administrator: sin ellos el administrador de Entra no funciona
# DEPENDENCY: Key Vault con RBAC para el secreto del administrador ("Key Vault Secrets Officer")
# DEPENDENCY: con private endpoint: subred de endpoints y zona privatelink.mysql.database.azure.com
#             enlazada a las VNets que resuelven
# DEPENDENCY: con integración en VNet: subred delegada a Microsoft.DBforMySQL/flexibleServers y
#             zona privada que termine en mysql.database.azure.com
# DEPENDENCY: con clave del cliente: Key Vault en la misma región y tenant, con soft delete y
#             purge protection
# DEPENDENCY: espacio de trabajo de Log Analytics
# =============================================================================

variable "mysql_servers" {
  description = "Servidores flexibles de MySQL (clave = nombre, único en Azure)."
  type = map(object({
    resource_group_name = string
    location            = string
    version             = string # 8.0.21 (MySQL 8.0) | 8.4
    sku_name            = string # B_Standard_B2ms | GP_Standard_D4ads_v5 | MO_Standard_E4ads_v5 ...

    storage = object({
      size_gb            = number # solo crece; bajar fuerza la recreación
      auto_grow_enabled  = optional(bool, true)
      iops               = optional(number) # IOPS preaprovisionadas (incompatible con io_scaling_enabled)
      io_scaling_enabled = optional(bool, false)
    })

    zone = optional(string)
    high_availability = optional(object({
      mode                      = optional(string, "ZoneRedundant") # ZoneRedundant (solo al crear) | SameZone
      standby_availability_zone = optional(string)
    }))

    backup_retention_days        = optional(number, 7)
    geo_redundant_backup_enabled = optional(bool, false) # no disponible en todas las regiones

    maintenance_window = optional(object({
      day_of_week  = number # 0 = domingo
      start_hour   = number
      start_minute = optional(number, 0)
    }))

    # Autenticación: la contraseña del administrador es obligatoria al crear (va a Key Vault);
    # con password_auth_enabled = false se fuerza aad_auth_only = ON y solo entra Entra
    entra_admin = object({
      login     = string # nombre visible del grupo
      object_id = string
    })
    password_auth_enabled = optional(bool, false)
    administrator_login   = string
    key_vault_id          = string

    # Red: private endpoints (acceso público deshabilitado) o integración en VNet, nunca ambos
    private_endpoints = optional(map(object({
      subnet_id           = string
      private_dns_zone_id = string
    })), {})
    delegated_subnet_id = optional(string)
    private_dns_zone_id = optional(string) # solo con delegated_subnet_id

    customer_managed_key = optional(object({
      key_vault_id     = string
      key_vault_key_id = string
    }))

    databases = optional(map(object({
      charset   = optional(string, "utf8mb4")
      collation = optional(string, "utf8mb4_0900_ai_ci")
    })), {})

    server_parameters = optional(map(string), {})

    log_analytics_workspace_id = string
    tags                       = optional(map(string), {})
  }))
  default = {}

  validation {
    condition     = alltrue([for k, v in var.mysql_servers : contains(["8.0.21", "8.4"], v.version)])
    error_message = "version debe ser 8.0.21 (MySQL 8.0) o 8.4: 5.7 está en soporte extendido de pago."
  }

  validation {
    condition     = alltrue([for k, v in var.mysql_servers : can(regex("^(B|GP|MO)_Standard_", v.sku_name))])
    error_message = "sku_name debe empezar por B_Standard_, GP_Standard_ o MO_Standard_."
  }

  validation {
    condition     = alltrue([for k, v in var.mysql_servers : v.high_availability == null || !startswith(v.sku_name, "B_")])
    error_message = "La alta disponibilidad no existe en Burstable: usa General Purpose o Memory Optimized."
  }

  validation {
    condition = alltrue([
      for k, v in var.mysql_servers :
      v.high_availability == null || contains(["ZoneRedundant", "SameZone"], try(v.high_availability.mode, ""))
    ])
    error_message = "high_availability.mode debe ser ZoneRedundant o SameZone."
  }

  validation {
    condition = alltrue([
      for k, v in var.mysql_servers :
      try(v.high_availability.mode, "") != "ZoneRedundant" || try(v.high_availability.standby_availability_zone, null) == null ||
      v.zone == null || try(v.high_availability.standby_availability_zone, "") != v.zone
    ])
    error_message = "Con ZoneRedundant, la zona del standby debe ser distinta de la del primario."
  }

  validation {
    condition     = alltrue([for k, v in var.mysql_servers : v.high_availability == null || v.storage.auto_grow_enabled])
    error_message = "Con alta disponibilidad el crecimiento automático del almacenamiento está siempre activo: no lo desactives."
  }

  validation {
    condition     = alltrue([for k, v in var.mysql_servers : v.storage.size_gb >= 20 && v.storage.size_gb <= 16384])
    error_message = "storage.size_gb debe estar entre 20 y 16384 (límite del provider)."
  }

  validation {
    condition     = alltrue([for k, v in var.mysql_servers : !(v.storage.io_scaling_enabled && v.storage.iops != null)])
    error_message = "storage.iops no se puede fijar con io_scaling_enabled: elige IOPS preaprovisionadas o autoescalado."
  }

  validation {
    condition     = alltrue([for k, v in var.mysql_servers : v.backup_retention_days >= 1 && v.backup_retention_days <= 35])
    error_message = "backup_retention_days debe estar entre 1 y 35."
  }

  validation {
    condition = alltrue([
      for k, v in var.mysql_servers :
      (v.delegated_subnet_id == null) != (length(v.private_endpoints) == 0)
    ])
    error_message = "Elige un modo de red: private_endpoints o delegated_subnet_id (no ambos, no ninguno)."
  }

  validation {
    condition = alltrue([
      for k, v in var.mysql_servers :
      v.delegated_subnet_id == null ? v.private_dns_zone_id == null : v.private_dns_zone_id != null
    ])
    error_message = "private_dns_zone_id va solo con delegated_subnet_id (y es obligatorio con él)."
  }

  validation {
    condition = alltrue([
      for k, v in var.mysql_servers :
      upper(lookup(v.server_parameters, "require_secure_transport", "ON")) == "ON"
    ])
    error_message = "require_secure_transport no puede desactivarse."
  }

  validation {
    condition     = alltrue([for k, v in var.mysql_servers : !contains(keys(v.server_parameters), "aad_auth_only")])
    error_message = "aad_auth_only se controla con password_auth_enabled, no con server_parameters."
  }
}

variable "mysql_replicas" {
  description = "Réplicas de lectura (clave = nombre). Heredan versión, SKU, almacenamiento y cuentas del origen."
  type = map(object({
    source_server       = string # clave en mysql_servers
    resource_group_name = string
    location            = string
    zone                = optional(string)
    private_endpoints = map(object({
      subnet_id           = string
      private_dns_zone_id = string
    }))
    tags = optional(map(string), {})
  }))
  default = {}
}

# -----------------------------------------------------------------------------
# Identidad del servidor: la usa el administrador de Entra (Graph) y la clave del cliente
# -----------------------------------------------------------------------------
module "mysql_identity" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//PRO/common/assigned_identity?ref=main"
  for_each = var.mysql_servers

  name                = "id-${each.key}"
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  tags                = merge(var.tags, each.value.tags)
}

resource "azurerm_role_assignment" "mysql_cmk" {
  for_each = { for k, v in var.mysql_servers : k => v if v.customer_managed_key != null }

  scope                            = each.value.customer_managed_key.key_vault_id
  role_definition_name             = "Key Vault Crypto Service Encryption User"
  principal_id                     = module.mysql_identity[each.key].principal_id
  principal_type                   = "ServicePrincipal"
  skip_service_principal_aad_check = true
  description                      = "Cifrado con clave del cliente de ${each.key}"
}

# -----------------------------------------------------------------------------
# Contraseña del administrador: obligatoria al crear, nunca en el código ni en tfvars
# -----------------------------------------------------------------------------
resource "random_password" "mysql_admin" {
  for_each = var.mysql_servers

  length           = 32
  special          = true
  override_special = "!#$%*()-_=+[]{}:?"
  min_lower        = 2
  min_upper        = 2
  min_numeric      = 2
  min_special      = 2
}

resource "azurerm_key_vault_secret" "mysql_admin" {
  for_each = var.mysql_servers

  name         = "mysql-${each.key}-admin"
  value        = random_password.mysql_admin[each.key].result
  key_vault_id = each.value.key_vault_id
  content_type = "MySQL administrator (${each.value.administrator_login})"
}

# -----------------------------------------------------------------------------
# Servidor (recurso nativo: Database/MySQLFlexible no inicializa)
# -----------------------------------------------------------------------------
resource "azurerm_mysql_flexible_server" "this" {
  for_each = var.mysql_servers

  name                = each.key
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  version             = each.value.version
  sku_name            = each.value.sku_name

  administrator_login    = each.value.administrator_login
  administrator_password = random_password.mysql_admin[each.key].result

  storage {
    size_gb            = each.value.storage.size_gb
    auto_grow_enabled  = each.value.storage.auto_grow_enabled
    iops               = each.value.storage.iops
    io_scaling_enabled = each.value.storage.io_scaling_enabled
  }

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

  # public_network_access_enabled es solo lectura en 4.x: el control es public_network_access
  public_network_access = "Disabled"
  delegated_subnet_id   = each.value.delegated_subnet_id
  private_dns_zone_id   = each.value.private_dns_zone_id

  identity {
    type         = "UserAssigned"
    identity_ids = [module.mysql_identity[each.key].id]
  }

  dynamic "customer_managed_key" {
    for_each = each.value.customer_managed_key != null ? [each.value.customer_managed_key] : []
    content {
      key_vault_key_id                  = customer_managed_key.value.key_vault_key_id
      primary_user_assigned_identity_id = module.mysql_identity[each.key].id
    }
  }

  tags = merge(var.tags, each.value.tags)

  lifecycle {
    # Tras un failover las zonas se intercambian; intercambiarlas aquí forzaría otro failover
    ignore_changes = [zone, high_availability[0].standby_availability_zone]

    precondition {
      condition     = !(each.value.geo_redundant_backup_enabled && each.value.customer_managed_key != null)
      error_message = "Copia geo-redundante con clave del cliente necesita clave e identidad en la región emparejada: fuera de este root."
    }
  }

  depends_on = [azurerm_role_assignment.mysql_cmk]
}

# Un único administrador de Entra por servidor (se recomienda un grupo)
resource "azurerm_mysql_flexible_server_active_directory_administrator" "this" {
  for_each = var.mysql_servers

  server_id   = azurerm_mysql_flexible_server.this[each.key].id
  identity_id = module.mysql_identity[each.key].id
  login       = each.value.entra_admin.login
  object_id   = each.value.entra_admin.object_id
  tenant_id   = data.azurerm_client_config.current.tenant_id
}

# Parámetros: TLS obligatorio, auditoría y consultas lentas (alimentan el diagnóstico)
resource "azurerm_mysql_flexible_server_configuration" "this" {
  for_each = merge([
    for k, v in var.mysql_servers : {
      for pk, pv in merge({
        "require_secure_transport" = "ON"
        "audit_log_enabled"        = "ON"
        "slow_query_log"           = "ON"
      }, v.server_parameters) : "${k}/${pk}" => { server = k, name = pk, value = pv, rg = v.resource_group_name }
    }
  ]...)

  name                = each.value.name
  resource_group_name = each.value.rg
  server_name         = azurerm_mysql_flexible_server.this[each.value.server].name
  value               = each.value.value
}

# Solo Entra: después de que exista el administrador de Entra, o nadie podría entrar
resource "azurerm_mysql_flexible_server_configuration" "aad_auth_only" {
  for_each = { for k, v in var.mysql_servers : k => v if !v.password_auth_enabled }

  name                = "aad_auth_only"
  resource_group_name = each.value.resource_group_name
  server_name         = azurerm_mysql_flexible_server.this[each.key].name
  value               = "ON"

  depends_on = [azurerm_mysql_flexible_server_active_directory_administrator.this]
}

resource "azurerm_mysql_flexible_database" "this" {
  for_each = merge([
    for k, v in var.mysql_servers : {
      for dk, d in v.databases : "${k}/${dk}" => merge(d, { server = k, name = dk, rg = v.resource_group_name })
    }
  ]...)

  name                = each.value.name
  resource_group_name = each.value.rg
  server_name         = azurerm_mysql_flexible_server.this[each.value.server].name
  charset             = each.value.charset
  collation           = each.value.collation
}

module "mysql_private_endpoint" {
  source = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Networking/Networking/modules/private_endpoint?ref=main"
  for_each = merge([
    for k, v in var.mysql_servers : {
      for pk, p in v.private_endpoints : "${k}-${pk}" => merge(p, { server = k, rg = v.resource_group_name, location = v.location })
    }
  ]...)

  private_endpoint_name          = "pe-${each.key}"
  custom_network_interface_name  = "nic-pe-${each.key}"
  resource_group_name            = each.value.rg
  location                       = each.value.location
  subnet_id                      = each.value.subnet_id
  private_connection_resource_id = azurerm_mysql_flexible_server.this[each.value.server].id
  subresource_names              = ["mysqlServer"]
  private_dns_zone_ids           = [each.value.private_dns_zone_id]
  tags                           = merge(var.tags, var.mysql_servers[each.value.server].tags)
}

# Auditoría y consultas lentas (tabla AzureDiagnostics) + métricas
module "mysql_diagnostics" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Security/Seguridad/modules/monitor_diagnostic_setting?ref=main"
  for_each = var.mysql_servers

  monitor_diagnostic_setting_name = "diag-${each.key}"
  target_resource_id              = azurerm_mysql_flexible_server.this[each.key].id
  log_analytics_workspace_id      = each.value.log_analytics_workspace_id
  enabled_logs                    = [{ category = "MySqlAuditLogs" }, { category = "MySqlSlowLogs" }]
  enabled_metrics                 = [{ category = "AllMetrics" }]
}

# -----------------------------------------------------------------------------
# Réplicas de lectura en otra región (recuperación ante desastre manual: detener la replicación)
# -----------------------------------------------------------------------------
resource "azurerm_mysql_flexible_server" "replica" {
  for_each = var.mysql_replicas

  name                = each.key
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  zone                = each.value.zone

  create_mode      = "Replica"
  source_server_id = azurerm_mysql_flexible_server.this[each.value.source_server].id

  # Simétrica con el origen para que no se quede atrás
  version  = var.mysql_servers[each.value.source_server].version
  sku_name = var.mysql_servers[each.value.source_server].sku_name
  storage {
    size_gb           = var.mysql_servers[each.value.source_server].storage.size_gb
    auto_grow_enabled = var.mysql_servers[each.value.source_server].storage.auto_grow_enabled
  }

  public_network_access = "Disabled"

  tags = merge(var.tags, each.value.tags)

  lifecycle {
    # replication_role = "None" lo cambia quien promociona (fuera de Terraform o con un cambio explícito)
    ignore_changes = [replication_role]

    precondition {
      condition     = !startswith(var.mysql_servers[each.value.source_server].sku_name, "B_")
      error_message = "Burstable no admite réplicas de lectura."
    }
    precondition {
      condition = (
        var.mysql_servers[each.value.source_server].customer_managed_key == null &&
        var.mysql_servers[each.value.source_server].delegated_subnet_id == null
      )
      error_message = "Este root crea réplicas solo de servidores con private endpoint y clave del servicio."
    }
  }

  depends_on = [azurerm_mysql_flexible_database.this]
}

module "mysql_replica_private_endpoint" {
  source = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Networking/Networking/modules/private_endpoint?ref=main"
  for_each = merge([
    for k, v in var.mysql_replicas : {
      for pk, p in v.private_endpoints : "${k}-${pk}" => merge(p, { replica = k, rg = v.resource_group_name, location = v.location })
    }
  ]...)

  private_endpoint_name          = "pe-${each.key}"
  custom_network_interface_name  = "nic-pe-${each.key}"
  resource_group_name            = each.value.rg
  location                       = each.value.location
  subnet_id                      = each.value.subnet_id
  private_connection_resource_id = azurerm_mysql_flexible_server.replica[each.value.replica].id
  subresource_names              = ["mysqlServer"]
  private_dns_zone_ids           = [each.value.private_dns_zone_id]
  tags                           = merge(var.tags, var.mysql_replicas[each.value.replica].tags)
}

module "mysql_replica_diagnostics" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Security/Seguridad/modules/monitor_diagnostic_setting?ref=main"
  for_each = var.mysql_replicas

  monitor_diagnostic_setting_name = "diag-${each.key}"
  target_resource_id              = azurerm_mysql_flexible_server.replica[each.key].id
  log_analytics_workspace_id      = var.mysql_servers[each.value.source_server].log_analytics_workspace_id
  enabled_logs                    = [{ category = "MySqlAuditLogs" }, { category = "MySqlSlowLogs" }]
  enabled_metrics                 = [{ category = "AllMetrics" }]
}

# -----------------------------------------------------------------------------
# Salidas
# -----------------------------------------------------------------------------
output "mysql_server_ids" {
  description = "IDs de los servidores."
  value       = { for k, s in azurerm_mysql_flexible_server.this : k => s.id }
}

output "mysql_fqdns" {
  description = "FQDN de cada servidor (puerto 3306); conecta siempre por FQDN, nunca por IP."
  value       = { for k, s in azurerm_mysql_flexible_server.this : k => s.fqdn }
}

output "mysql_identity_principal_ids" {
  description = "Principal ID de cada identidad: a estos hay que concederles los permisos de Microsoft Graph."
  value       = { for k, m in module.mysql_identity : k => m.principal_id }
}

output "mysql_replica_ids" {
  description = "IDs de las réplicas de lectura."
  value       = { for k, s in azurerm_mysql_flexible_server.replica : k => s.id }
}

output "mysql_admin_secret_ids" {
  description = "Secretos de Key Vault con la contraseña del administrador."
  value       = { for k, s in azurerm_key_vault_secret.mysql_admin : k => s.versionless_id }
}
```

### `env/pro.tfvars`

Servidor 8.4 zone-redundant con private endpoint y una réplica en otra región.

```hcl
tags = {
  environment = "pro"
  workload    = "<workload>"
  owner       = "<owner>"
  costcenter  = "<costcenter>"
}

mysql_servers = {
  "mysql-<workload>-pro-01" = {
    resource_group_name = "<rg-data-pro>"
    location            = "<region>"
    version             = "8.4"
    sku_name            = "GP_Standard_D4ads_v5"

    storage = {
      size_gb            = 128
      io_scaling_enabled = true # paga por IOPS usadas; para carga estable, fija iops
    }

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

    entra_admin = {
      login     = "<grupo-dba-pro>"
      object_id = "<objectId grupo-dba-pro>"
    }
    administrator_login = "<admin-break-glass>"
    key_vault_id        = "<resourceId kv-<workload>-pro>"

    private_endpoints = {
      app = {
        subnet_id           = "<resourceId snet-pe-pro>"
        private_dns_zone_id = "<resourceId privatelink.mysql.database.azure.com>"
      }
    }

    databases = {
      appdb = {}
    }

    # tls_version (TLS 1.3) y audit_log_events se añaden aquí con el valor exacto que admite el
    # servidor (Get-AzMySqlFlexibleServerConfiguration -Name <parámetro>); tls_version es estático (reinicia)
    server_parameters = {
      "long_query_time" = "10"
    }

    log_analytics_workspace_id = "<resourceId log-<workload>-pro>"
  }
}

# Réplica en otra región: la recuperación ante desastre cuando la región no tiene copia geo-redundante
mysql_replicas = {
  "mysql-<workload>-pro-dr-01" = {
    source_server       = "mysql-<workload>-pro-01"
    resource_group_name = "<rg-data-pro-dr>"
    location            = "<region-dr>"
    zone                = "1"
    private_endpoints = {
      app = {
        subnet_id           = "<resourceId snet-pe-pro-dr>"
        private_dns_zone_id = "<resourceId privatelink.mysql.database.azure.com>"
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

Get-AzMySqlFlexibleServer -ResourceGroupName "<rg-data-pro>" -Name "mysql-<workload>-pro-01" | Format-List
Get-AzMySqlFlexibleServerConfiguration -ResourceGroupName "<rg-data-pro>" -ServerName "mysql-<workload>-pro-01" |
    Where-Object { $_.Name -in "require_secure_transport", "tls_version", "aad_auth_only", "audit_log_enabled" } |
    Select-Object Name, Value
```

Antes del `apply`, un administrador de roles privilegiados concede los permisos de Graph a la identidad (`mysql_identity_principal_ids`). Después, conexión con Entra (miembro del grupo administrador) y alta de la identidad de una aplicación:

```powershell
$token = az account get-access-token --resource-type oss-rdbms --query accessToken -o tsv
mysql -h "mysql-<workload>-pro-01.mysql.database.azure.com" --user "<grupo-dba-pro>" `
    --enable-cleartext-plugin --ssl-mode=VERIFY_IDENTITY --ssl-ca="DigiCertGlobalRootG2.crt.pem" --password="$token"
```

```sql
CREATE AADUSER '<identidad-de-la-app>';
GRANT SELECT, INSERT, UPDATE, DELETE ON appdb.* TO '<identidad-de-la-app>';
```

Prueba de failover (fuera de horas):

```powershell
Restart-AzMySqlFlexibleServer -ResourceGroupName "<rg-data-pro>" -Name "mysql-<workload>-pro-01" `
    -RestartWithFailover Enabled
```

### Equivalente en Bicep

Una plantilla por servidor, con las réplicas en el mismo grupo de recursos. La contraseña del administrador sale de Key Vault con `az.getSecret` en el `.bicepparam`. La ventana de mantenimiento **no se puede fijar al crear** (limitación documentada de la API): va en una actualización posterior. Para el rol sobre el Key Vault de otro grupo de recursos usa `role-on-resource.bicep`, el mismo de las fichas de SQL y PostgreSQL.

`mysql.bicep`:

```bicep
// =============================================================================
// Azure Database for MySQL flexible server seguro por defecto: sin acceso público (private
// endpoint o integración en VNet), administrador de Entra con identidad asignada, solo Entra
// salvo que se pida contraseña (aad_auth_only), TLS obligatorio, auditoría y consultas lentas,
// alta disponibilidad entre zonas, clave del cliente opcional y réplicas de lectura
// DEPENDENCY: grupo de Entra administrador; zona privatelink.mysql.database.azure.com
// DEPENDENCY: permisos de Microsoft Graph para la identidad id-<servidor> (se conceden fuera)
// DEPENDENCY: secreto con la contraseña del administrador en Key Vault (getSecret en .bicepparam)
// DEPENDENCY: Key Vault con purge protection en la misma región (si hay clave del cliente)
// DEPENDENCY: role-on-resource.bicep en la misma carpeta
// La ventana de mantenimiento no se puede fijar al crear el servidor: va en una actualización aparte
// =============================================================================
@minLength(1)
@maxLength(63)
param name string
param location string = resourceGroup().location

// La referencia de 2024-12-30 enumera 5.7 y 8.0.21; 8.4 aparece en 2025-06-01-preview
@allowed(['8.0.21', '8.4'])
param version string

@description('{ name (Standard_D4ads_v5), tier (Burstable | GeneralPurpose | MemoryOptimized) }')
param sku object

@description('{ sizeGb, autoGrow? (true), iops?, autoIoScaling? (false) }')
param storage object

param zone string
@description('{ mode (ZoneRedundant | SameZone), standbyZone? }; vacío = sin alta disponibilidad')
param highAvailability object = {}

@minValue(1)
@maxValue(35)
param backupRetentionDays int = 7
param geoRedundantBackup bool = false

@description('{ login, objectId } del grupo administrador (MySQL admite uno)')
param entraAdmin object

param passwordAuth bool = false
param administratorLogin string
@secure()
param administratorPassword string

@description('[{ name, subnetId, privateDnsZoneId }] (acceso público deshabilitado)')
param privateEndpoints array = []
@description('Integración en VNet: { subnetId, privateDnsZoneId }; vacío = private endpoints')
param vnetIntegration object = {}

@description('Clave del cliente: { keyVaultId, keyUri }')
param customerManagedKey object = {}

@description('{ nombre: { charset?, collation? } }')
param databases object = {}

@description('Parámetros del servidor { nombre: valor }; require_secure_transport siempre ON')
param serverParameters object = {}

param logAnalyticsWorkspaceId string

@description('[{ name, location, zone?, privateEndpoints: [{ name, subnetId, privateDnsZoneId }] }] en este grupo de recursos')
param replicas array = []

param tags object = {}

var useCmk = !empty(customerManagedKey)
var useVnet = !empty(vnetIntegration)
var autoGrow = storage.?autoGrow ?? true
var parameters = union(
  {
    audit_log_enabled: 'ON'
    slow_query_log: 'ON'
  },
  serverParameters,
  {
    require_secure_transport: 'ON'
  }
)

resource identity 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = {
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
    principalId: identity.properties.principalId
    description: 'Cifrado con clave del cliente de ${name}'
  }
}

resource server 'Microsoft.DBforMySQL/flexibleServers@2024-12-30' = {
  name: name
  location: location
  tags: tags
  sku: {
    name: sku.name
    tier: sku.tier
  }
  identity: {
    type: 'UserAssigned'
    userAssignedIdentities: {
      '${identity.id}': {}
    }
  }
  properties: {
    createMode: 'Default'
    version: version
    administratorLogin: administratorLogin
    administratorLoginPassword: administratorPassword
    availabilityZone: zone
    storage: {
      storageSizeGB: storage.sizeGb
      // Con alta disponibilidad el crecimiento automático es obligatorio
      autoGrow: (autoGrow || !empty(highAvailability)) ? 'Enabled' : 'Disabled'
      autoIoScaling: (storage.?autoIoScaling ?? false) ? 'Enabled' : 'Disabled'
      iops: (storage.?autoIoScaling ?? false) ? null : storage.?iops
    }
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
    network: {
      publicNetworkAccess: 'Disabled'
      delegatedSubnetResourceId: useVnet ? vnetIntegration.subnetId : null
      privateDnsZoneResourceId: useVnet ? vnetIntegration.privateDnsZoneId : null
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

resource admin 'Microsoft.DBforMySQL/flexibleServers/administrators@2024-12-30' = {
  parent: server
  name: 'ActiveDirectory'
  properties: {
    administratorType: 'ActiveDirectory'
    identityResourceId: identity.id
    login: entraAdmin.login
    sid: entraAdmin.objectId
    tenantId: tenant().tenantId
  }
}

// Parámetros de uno en uno, sin actualizaciones simultáneas sobre el servidor
@batchSize(1)
resource configurations 'Microsoft.DBforMySQL/flexibleServers/configurations@2024-12-30' = [
  for p in items(parameters): {
    parent: server
    name: p.key
    properties: {
      value: p.value
      source: 'user-override'
    }
    dependsOn: [
      admin
    ]
  }
]

// Solo Entra: después de que exista el administrador de Entra
resource aadAuthOnly 'Microsoft.DBforMySQL/flexibleServers/configurations@2024-12-30' = if (!passwordAuth) {
  parent: server
  name: 'aad_auth_only'
  properties: {
    value: 'ON'
    source: 'user-override'
  }
  dependsOn: [
    configurations
  ]
}

resource dbs 'Microsoft.DBforMySQL/flexibleServers/databases@2024-12-30' = [
  for d in items(databases): {
    parent: server
    name: d.key
    properties: {
      charset: d.value.?charset ?? 'utf8mb4'
      collation: d.value.?collation ?? 'utf8mb4_0900_ai_ci'
    }
    dependsOn: [
      aadAuthOnly
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
          name: 'mysqlServer'
          properties: {
            privateLinkServiceId: server.id
            groupIds: [
              'mysqlServer'
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
          name: 'mysql'
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
    logs: [
      {
        category: 'MySqlAuditLogs'
        enabled: true
      }
      {
        category: 'MySqlSlowLogs'
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

// Réplicas de lectura simétricas con el origen (sin alta disponibilidad)
resource replicaServers 'Microsoft.DBforMySQL/flexibleServers@2024-12-30' = [
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
        autoGrow: (autoGrow || !empty(highAvailability)) ? 'Enabled' : 'Disabled'
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
          name: 'mysqlServer'
          properties: {
            privateLinkServiceId: replicaServers[i].id
            groupIds: [
              'mysqlServer'
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
          name: 'mysql'
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
      logs: [
        {
          category: 'MySqlAuditLogs'
          enabled: true
        }
        {
          category: 'MySqlSlowLogs'
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

output serverId string = server.id
output fqdn string = server.properties.fullyQualifiedDomainName
output identityPrincipalId string = identity.properties.principalId
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

`mysql-workload-pro-01.bicepparam`:

```bicep
using 'mysql.bicep'

param name = 'mysql-<workload>-pro-01'
param version = '8.4'
param sku = {
  name: 'Standard_D4ads_v5'
  tier: 'GeneralPurpose'
}

// Autoescalado de IOPS: paga por las usadas; para carga estable, fija iops
param storage = {
  sizeGb: 128
  autoIoScaling: true
}

param zone = '1'
param highAvailability = {
  mode: 'ZoneRedundant'
  standbyZone: '2'
}

param backupRetentionDays = 35

param entraAdmin = {
  login: '<grupo-dba-pro>'
  objectId: '<objectId grupo-dba-pro>'
}

// Cuenta de emergencia: la contraseña sale de Key Vault, nunca del fichero
param administratorLogin = '<admin-break-glass>'
param administratorPassword = az.getSecret(
  '<subscriptionId>',
  '<rg-kv-pro>',
  '<kv-<workload>-pro>',
  'mysql-<workload>-pro-01-admin'
)

param privateEndpoints = [
  {
    name: 'app'
    subnetId: '<resourceId snet-pe-pro>'
    privateDnsZoneId: '<resourceId privatelink.mysql.database.azure.com>'
  }
]

param databases = {
  appdb: {}
}

param serverParameters = {
  long_query_time: '10'
}

param logAnalyticsWorkspaceId = '<resourceId log-<workload>-pro>'

param replicas = [
  {
    name: 'mysql-<workload>-pro-dr-01'
    location: '<region-dr>'
    zone: '1'
    privateEndpoints: [
      {
        name: 'app'
        subnetId: '<resourceId snet-pe-pro-dr>'
        privateDnsZoneId: '<resourceId privatelink.mysql.database.azure.com>'
      }
    ]
  }
]

param tags = {
  environment: 'pro'
  workload: '<workload>'
}
```

Despliegue:

```powershell
New-AzResourceGroupDeployment -ResourceGroupName "<rg-data-pro>" `
    -TemplateParameterFile "mysql-workload-pro-01.bicepparam" -Name "mysql-<workload>-pro-01"
```

## Errores típicos

| Síntoma | Causa | Solución |
|---|---|---|
| `Invalid variable name` sobre `variable "version"` en `terraform init` | Módulo `Database/MySQLFlexible` del repositorio | Recurso nativo (o renombrar la variable en el módulo) |
| `Can't configure a value for "public_network_access_enabled"` | En azurerm 4.x es solo lectura | `public_network_access = "Disabled"` |
| El servidor queda con acceso público | `public_network_access` omitido | Declararlo `Disabled` |
| `terraform plan` quiere recrear el servidor | Cambio de subred, zona DNS, login del administrador, copia geo-redundante o bajada de `size_gb` (ForceNew) | Alinear el código; son decisiones de creación |
| ``iops` can not be set if `io_scaling_enabled` is set to true`` | IOPS fijas y autoescalado a la vez | Elegir uno (validado en el root) |
| El administrador de Entra no puede entrar | La identidad no tiene los permisos de Graph o el nombre no coincide (sensible a mayúsculas) | Conceder `User.Read.All`, `GroupMember.Read.All` y `Application.Read.All`; usar el nombre exacto del grupo |
| Nadie entra tras activar `aad_auth_only` | Se activó antes de que existiera el administrador de Entra | Crear el administrador primero (el root ya lo ordena) |
| `Access denied` con token de Entra | Token caducado, audiencia distinta de `ossrdbms` o cliente sin `--enable-cleartext-plugin` | Token justo antes de conectar, con `--resource-type oss-rdbms` |
| `ERROR 3159 ... insecure transport` | Cliente sin TLS con `require_secure_transport = ON` | `--ssl-mode=REQUIRED` o superior en el cliente |
| Fallo de TLS en clientes tras una rotación | Pinning o intermedias en el almacén | Solo las raíces DigiCert Global Root G2 y Microsoft RSA Root CA 2017 |
| El servidor pasa a solo lectura | Poco espacio libre (5 % o 5 GiB) | Ampliar almacenamiento o crecimiento automático |
| Server **Inaccessible** | Clave del cliente borrada, sin permisos o identidad eliminada | Recuperar clave o Key Vault y revalidar el cifrado |
| `MySqlAuditLogs` vacía | `audit_log_enabled` desactivado o sin diagnóstico | Parámetro en `ON` y categoría en la configuración de diagnóstico |
| La replicación se rompe | Tablas sin clave primaria, `AUTO_INCREMENT` añadido después o borrados en cascada | Claves primarias; recrear la réplica tras cambios de esquema |
| No se puede parar el servidor | Tiene réplicas | Promocionarlas o borrarlas antes |
| Zone-redundant no aparece al editar | Solo se configura al crear | Restaurar o recrear con zone-redundant |
