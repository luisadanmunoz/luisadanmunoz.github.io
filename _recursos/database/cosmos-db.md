---
title: "Cosmos DB"
indice: database
resumen: "Base de datos distribuida para varios modelos."
estado: documentado   # proximamente | en-curso | documentado
orden: 6
last_review: 2026-11-12
fuentes:
  - titulo: "Azure Cosmos DB - Database for the AI Era"
    url: https://learn.microsoft.com/azure/cosmos-db/overview
  - titulo: "How to choose between provisioned throughput and serverless"
    url: https://learn.microsoft.com/azure/cosmos-db/throughput-serverless
  - titulo: "Azure Cosmos DB serverless account performance"
    url: https://learn.microsoft.com/azure/cosmos-db/serverless-performance
  - titulo: "Create Azure Cosmos DB containers and databases with autoscale"
    url: https://learn.microsoft.com/azure/cosmos-db/provision-throughput-autoscale
  - titulo: "Frequently asked questions about autoscale throughput in Azure Cosmos DB"
    url: https://learn.microsoft.com/azure/cosmos-db/autoscale-faq
  - titulo: "Azure Cosmos DB lifetime free tier"
    url: https://learn.microsoft.com/azure/cosmos-db/free-tier
  - titulo: "Azure Cosmos DB service quotas and default limits"
    url: https://learn.microsoft.com/azure/cosmos-db/concepts-limits
  - titulo: "Limit the total throughput provisioned on your Azure Cosmos DB account"
    url: https://learn.microsoft.com/azure/cosmos-db/limit-total-account-throughput
  - titulo: "Partitioning and horizontal scaling in Azure Cosmos DB"
    url: https://learn.microsoft.com/azure/cosmos-db/partitioning
  - titulo: "Hierarchical partition keys in Azure Cosmos DB"
    url: https://learn.microsoft.com/azure/cosmos-db/hierarchical-partition-keys
  - titulo: "Unlimited logical partition storage with hierarchical partition keys in Azure Cosmos DB"
    url: https://learn.microsoft.com/azure/cosmos-db/hierarchical-partition-keys-unlimited-scale
  - titulo: "Reliability in Azure Cosmos DB"
    url: https://learn.microsoft.com/azure/reliability/reliability-cosmos-db
  - titulo: "Distribute your data globally with Azure Cosmos DB"
    url: https://learn.microsoft.com/azure/cosmos-db/distribute-data-globally
  - titulo: "Per-partition automatic failover in Azure Cosmos DB"
    url: https://learn.microsoft.com/azure/cosmos-db/per-partition-automatic-failover
  - titulo: "Configure per-partition automatic failover for Azure Cosmos DB"
    url: https://learn.microsoft.com/azure/cosmos-db/how-to-configure-per-partition-automatic-failover
  - titulo: "Disaster recovery guidance for Azure Cosmos DB"
    url: https://learn.microsoft.com/azure/cosmos-db/disaster-recovery-guidance
  - titulo: "Online backup and on-demand data restore in Azure Cosmos DB"
    url: https://learn.microsoft.com/azure/cosmos-db/online-backup-and-restore
  - titulo: "Continuous backup with point-in-time restore in Azure Cosmos DB"
    url: https://learn.microsoft.com/azure/cosmos-db/continuous-backup-restore-introduction
  - titulo: "Migrate an Azure Cosmos DB account from periodic to continuous backup mode"
    url: https://learn.microsoft.com/azure/cosmos-db/migrate-continuous-backup
  - titulo: "Configure Azure Private Link for an Azure Cosmos DB account"
    url: https://learn.microsoft.com/azure/cosmos-db/how-to-configure-private-endpoints
  - titulo: "Azure Private Endpoint private DNS zone values"
    url: https://learn.microsoft.com/azure/private-link/private-endpoint-dns
  - titulo: "Connect to Azure Cosmos DB for NoSQL using role-based access control and Microsoft Entra ID"
    url: https://learn.microsoft.com/azure/cosmos-db/how-to-connect-role-based-access-control
  - titulo: "Azure Cosmos DB for NoSQL data plane security reference"
    url: https://learn.microsoft.com/azure/cosmos-db/reference-data-plane-security
  - titulo: "How to audit Azure Cosmos DB control plane operations"
    url: https://learn.microsoft.com/azure/cosmos-db/audit-control-plane-logs
  - titulo: "Self-serve minimum TLS version enforcement in Azure Cosmos DB"
    url: https://learn.microsoft.com/azure/cosmos-db/self-serve-minimum-tls-enforcement
  - titulo: "Configure customer-managed keys for your Azure Cosmos DB account with Azure Key Vault"
    url: https://learn.microsoft.com/azure/cosmos-db/how-to-setup-customer-managed-keys
  - titulo: "Configure customer-managed keys for your existing Azure Cosmos DB account with Azure Key Vault"
    url: https://learn.microsoft.com/azure/cosmos-db/how-to-setup-customer-managed-keys-existing-accounts
  - titulo: "Secure your Azure Cosmos DB for NoSQL account"
    url: https://learn.microsoft.com/azure/cosmos-db/security
  - titulo: "Overview of Microsoft Defender for Azure Cosmos DB"
    url: https://learn.microsoft.com/azure/defender-for-cloud/concept-defender-for-cosmos
  - titulo: "Monitor Azure Cosmos DB"
    url: https://learn.microsoft.com/azure/cosmos-db/monitor
  - titulo: "Monitor Azure Cosmos DB data using Azure Monitor aggregated diagnostics logs (preview)"
    url: https://learn.microsoft.com/azure/cosmos-db/monitor-aggregated-logs
  - titulo: "Supported logs for Microsoft.DocumentDB/DatabaseAccounts"
    url: https://learn.microsoft.com/azure/azure-monitor/reference/supported-logs/microsoft-documentdb-databaseaccounts-logs
  - titulo: "Understand your Azure Cosmos DB bill"
    url: https://learn.microsoft.com/azure/cosmos-db/understand-your-bill
  - titulo: "Azure Cosmos DB pricing & discounts with Reserved Capacity"
    url: https://learn.microsoft.com/azure/cosmos-db/reserved-capacity
  - titulo: "Architecture best practices for Azure Cosmos DB for NoSQL"
    url: https://learn.microsoft.com/azure/well-architected/service-guides/cosmos-db
  - titulo: "Microsoft.DocumentDB databaseAccounts 2025-10-15 (plantillas ARM/Bicep)"
    url: https://learn.microsoft.com/azure/templates/microsoft.documentdb/2025-10-15/databaseaccounts
  - titulo: "New-AzCosmosDBSqlRoleAssignment"
    url: https://learn.microsoft.com/powershell/module/az.cosmosdb/new-azcosmosdbsqlroleassignment
  - titulo: "azurerm_cosmosdb_account"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/cosmosdb_account
  - titulo: "azurerm_cosmosdb_sql_role_assignment"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/cosmosdb_sql_role_assignment
  - titulo: "Módulo Terraform Database/CosmosDB"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Database/CosmosDB
  - titulo: "Módulo Terraform Networking/Networking/modules/private_endpoint"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Networking/Networking/modules/private_endpoint
  - titulo: "Módulo Terraform Security/Seguridad/modules/monitor_diagnostic_setting"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Security/Seguridad/modules/monitor_diagnostic_setting
---

**Azure Cosmos DB** es la base de datos NoSQL distribuida de Azure: documentos JSON con esquema flexible, latencia de un dígito en milisegundos, distribución global con un clic y escritura en varias regiones. Se paga por **unidades de petición (RU)**: leer un documento de 1 KB cuesta 1 RU y escribirlo, 5 RU (sin indexación; con índices, más). Esta ficha cubre la **API for NoSQL**, la que tiene más funciones (RBAC de datos, Defender, PPAF). Para aplicaciones MongoDB, Microsoft sugiere Azure DocumentDB, y Cosmos DB for PostgreSQL está en retirada: para eso, [PostgreSQL Flexible Server](/recursos/database/postgresql-flexible-server/).

## Qué es y cuándo usarlo

### Modelo de capacidad

| Modo | Cómo se cobra | Para qué | Límites |
|---|---|---|---|
| **Provisionado manual** | RU/s reservadas por hora, se usen o no | Carga estable y predecible | Mínimo 400 RU/s por contenedor |
| **Provisionado autoscale** | La RU/s más alta alcanzada en cada hora (mínimo el 10 % del máximo), a 1,5 veces la tarifa manual | Picos y carga variable; **la opción por defecto** | Máximo mínimo 1.000 RU/s; escala entre el 10 % y el 100 % |
| **Serverless** | RU consumidas | Tráfico intermitente, desarrollo | **Una sola región**, sin SLA de latencia en escritura, 5.000 RU/s por partición física; zonas solo al crear |

- El modo serverless o provisionado se elige al crear la cuenta.
- **Nivel gratuito**: 1.000 RU/s y 25 GB para toda la vida de la cuenta, una cuenta por suscripción, no en serverless.
- **Tope de la cuenta** (`total_throughput_limit`): impide aprovisionar más RU/s de las previstas; buen control de coste.
- Throughput compartido en la base **no es recomendable**: un contenedor puede dejar sin RU/s a los demás (429).

### Particionado

La clave de partición es **la decisión de diseño más importante** y no se cambia sin copiar el contenedor:

- Una partición lógica admite **20 GB**; una física, 50 GB y **10.000 RU/s**.
- Clave con muchos valores y reparto uniforme de lecturas y escrituras; si no, partición caliente y 429 con RU/s libres.
- **Claves jerárquicas** (hasta 3 niveles, `MultiHash`, versión 2): superan los 20 GB por prefijo. Terminar en `/id` elimina el límite. No se añaden a contenedores existentes.

### Distribución y alta disponibilidad

| Configuración | Comportamiento |
|---|---|
| **Una región con zonas** | Réplicas síncronas en varias zonas, sin impacto en latencia; resiste la caída de una zona |
| Una región sin zonas | La caída de la zona o de la región deja la cuenta sin servicio |
| **Varias regiones, escritura en una** | Lecturas locales; failover **gestionado por el servicio** (puede tardar una hora o más) o forzado por ti |
| **PPAF** (*Per-partition automatic failover*) | Failover por partición: **RTO < 3 min (P99)**, RPO 0 con Strong. Requiere SDK reciente, modo directo y provisionado |
| **Escritura multirregión** | Activo-activo con 99,999 % de disponibilidad; **sin Strong**, con conflictos que resolver |

- **Zonas**: se activan por región. En una cuenta existente, solo al **añadir una región**. El recargo de zonas no se aplica con escritura multirregión ni con autoscale.
- Escritura multirregión y PPAF forman el nivel **Business Critical**.
- RPO ante caída regional: **0 con Strong**, menos de 15 minutos con Session, Consistent Prefix o Eventual.
- Una región caída la devuelve Microsoft al servicio; puede tardar varios días.
- Simulacros: failover forzado (región offline) o la simulación de PPAF.

### Consistencia

Cinco niveles: Strong, Bounded Staleness, **Session** (el habitual), Consistent Prefix y Eventual. Strong exige al menos dos regiones disponibles para mantener el quórum y no existe con escritura multirregión. Bounded Staleness en multirregión: mínimo 300 segundos y 100.000 operaciones.

### Seguridad

| Control | Recomendación |
|---|---|
| Red | **Acceso público deshabilitado desde la creación** y private endpoints (`Sql`, zona `privatelink.documents.azure.com`). Añadir un endpoint a una cuenta existente corta unos 5 minutos |
| Autenticación | **Sin claves** (`disableLocalAuth`) y RBAC de datos con Entra: *Cosmos DB Built-in Data Reader* (`00000000-0000-0000-0000-000000000001`) y *Data Contributor* (`...0002`), por cuenta, base o contenedor. No se gestiona desde el portal |
| Metadatos | `disableKeyBasedMetadataWriteAccess`: bases, contenedores y RU/s solo por ARM, CLI o PowerShell |
| TLS | Mínimo TLS 1.2 (el único valor de `minimalTlsVersion`); TLS 1.3 admitido desde marzo de 2025; 1.0 y 1.1 retirados en agosto de 2025 |
| Cifrado | Siempre cifrado; clave del cliente opcional, **también en cuentas existentes** (no en Cassandra ni con búsqueda vectorial; IDs de documento de hasta 990 bytes) |
| Defender | **Defender for Azure Cosmos DB** (solo NoSQL): inyección SQL, accesos anómalos, extracción de claves |
| Auditoría | Categoría `ControlPlaneRequests` para cambios de cuenta, red, RBAC y copias |

**Clave del cliente**: identidad de usuario como identidad por defecto (`UserAssignedIdentity=...`), Key Vault con soft delete y purge protection y rol *Key Vault Crypto Service Encryption User*. Con la clave revocada, **solo se puede borrar la cuenta**. Con copia continua, la identidad propia es obligatoria (la *first-party* no vale).

### Copias y recuperación

| Modo | Detalle |
|---|---|
| **Continua 7 días** | Restauración a cualquier segundo, en una cuenta nueva o en la misma. **Sin coste de almacenamiento**; se paga cada restauración |
| Continua 30 o 35 días | Igual, con coste de almacenamiento por GB y región |
| Periódica | Por defecto en cuentas antiguas: intervalo mínimo 1 hora, retención hasta un mes; **la restauración la hace soporte** |

- Pasar de periódica a continua es **irreversible**.
- Las copias **no son geo-resistentes por sí solas**: hace falta una segunda región.
- Se restaura en una región donde existía la cuenta de origen. El throughput restaurado puede no coincidir con el del punto de restauración.

### Monitorización

- Diagnóstico en **tablas dedicadas** (`CDB*`), que Microsoft recomienda frente a AzureDiagnostics.
- `DataPlaneRequests` registra cada petición y encarece Log Analytics. Las versiones agregadas (`DataPlaneRequests5M`/`15M`, preview) reducen el coste hasta un 95 %.
- `PartitionKeyRUConsumption` y `PartitionKeyStatistics` localizan particiones calientes o cerca de 20 GB.
- Las métricas de plataforma se recogen solas; Cosmos DB no admite exportarlas como categoría de diagnóstico.

### Cómo se factura

| Concepto | Detalle |
|---|---|
| Throughput | RU/s por hora y por región; autoscale a 1,5 veces la tarifa manual; serverless por RU consumida |
| Escritura multirregión | Tarifa por RU/s más alta que con una región de escritura |
| Almacenamiento | Por GB y región |
| Zonas | Recargo en la región, salvo con escritura multirregión o autoscale |
| Copias | Continua 7 días sin coste de almacenamiento; 30/35 días por GB y región; cada restauración por GB |
| Reservas | 1 o 3 años de RU/s, **hasta un 63 %**; no cubren almacenamiento |
| Nivel gratuito | 1.000 RU/s y 25 GB por cuenta, una por suscripción |

### Qué escenario recomiendo

| Escenario del cliente | Diseño | Por qué |
|---|---|---|
| Producción crítica en una región | Zonas, autoscale, private endpoint, sin claves | Resiste la caída de una zona; recargo de zonas exento con autoscale |
| Recuperación ante desastre | Segunda región de lectura con PPAF | RTO de minutos sin conflictos de escritura |
| Usuarios en varios continentes | Escritura multirregión con Session | Latencia local de escritura y 99,999 % |
| SaaS multiinquilino | Clave jerárquica `/tenantId` → `/userId` → `/id` | Inquilinos grandes sin límite de 20 GB |
| Desarrollo, PoC o tráfico esporádico | Serverless o nivel gratuito | Pagar por uso |
| Cumplimiento | Clave del cliente, `ControlPlaneRequests`, Defender | Separación de funciones y trazabilidad |
| Aplicaciones en [Container Apps](/recursos/compute/container-apps/) | Identidad gestionada con *Data Contributor* en su base | Sin secretos en la aplicación |

### Datos que conviene llevar a la reunión

- **La clave de partición no se cambia**: copiar el contenedor es la única vía.
- **Serverless o provisionado se decide al crear**; serverless es de una sola región.
- **Las zonas en una cuenta existente solo llegan añadiendo una región.**
- **El failover gestionado puede tardar una hora o más**; PPAF lo baja a minutos.
- **Strong no existe con escritura multirregión.**
- **La copia continua de 7 días no paga almacenamiento**, pero las copias no salen de las regiones de la cuenta.
- **Sin claves, las aplicaciones necesitan RBAC de datos**, que no se gestiona desde el portal.

## Decisiones de diseño

| Decisión | Lo que aplico | Por qué |
|---|---|---|
| Cuenta | Recurso nativo `azurerm_cosmosdb_account` | El módulo del repositorio no valida con azurerm 4.x |
| API | NoSQL (`GlobalDocumentDB`) | Es la que admite RBAC de datos, Defender y PPAF |
| Red | Acceso público deshabilitado y private endpoint obligatorio (validado) | Ni un minuto expuesta tras crearla |
| Autenticación | `local_authentication_enabled = false` y RBAC de datos con roles integrados | Sin claves ni cadenas de conexión |
| Metadatos | `access_key_metadata_writes_enabled = false` | Bases y contenedores solo por IaC |
| Regiones | Mapa con una prioridad 0 y prioridades únicas (validado); zonas activadas por defecto | Las zonas no se añaden después |
| Consistencia | Session; Strong incompatible con escritura multirregión (validado) | Equilibrio habitual entre coherencia y latencia |
| Copias | Continua 7 días por defecto; 35 días rechazado (validado) | Restauración propia sin coste de almacenamiento; el provider no admite 35 |
| Throughput | Manual o autoscale, nunca ambos (validado); nada en serverless | Errores de plan antes que de API |
| Particionado | Rutas múltiples = `MultiHash` versión 2 | Claves jerárquicas como en Learn |
| Clave del cliente | Identidad de usuario como identidad por defecto y rol antes de la cuenta | Compatible con copia continua |
| Diagnóstico | Plano de control, consultas y particiones en tablas dedicadas; sin `DataPlaneRequests` | Coste contenido en Log Analytics |

Alineación con el Well-Architected Framework:

- **Fiabilidad**: zonas, varias regiones, PPAF y copia continua.
- **Seguridad**: red privada, Entra sin claves, metadatos bloqueados, Defender y clave del cliente.
- **Coste**: autoscale, tope de la cuenta, nivel gratuito, serverless y reservas.
- **Excelencia operativa**: IaC con validaciones y pruebas; auditoría del plano de control.
- **Rendimiento**: claves jerárquicas y diagnóstico de particiones calientes.

## Módulo de Terraform

### El módulo del repositorio

[Database/CosmosDB](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Database/CosmosDB) **no valida con azurerm 4.x**:

- Usa `enable_automatic_failover`, `enable_free_tier` y `enable_multiple_write_locations`, renombrados en 4.x (`Unsupported argument`).
- Pasa `ip_range_filter` como texto; en 4.x es un conjunto (`Incorrect attribute value type`).
- Con OpenTofu 1.8.8, las validaciones de `mongo_server_version` y `backup` fallan con valores nulos porque `||` no cortocircuita.
- Deja **acceso público y claves activados por defecto**, saca claves y cadenas de conexión en outputs (sensibles) y fija una lista de capacidades que incluye `MongoDBv3.4`.
- No tiene private endpoints, diagnóstico, RBAC de datos, bases ni contenedores. Usa `locals`.

Por eso la cuenta va con el recurso nativo. Se reutilizan `private_endpoint`, `monitor_diagnostic_setting` y `PRO/common/assigned_identity`.

Notas del provider (azurerm 4.81, API 2024-08-15):

- `public_network_access_enabled` y `local_authentication_enabled` permiten el acceso por defecto: siempre explícitos.
- El tier de copia continua solo admite **7 y 30 días**; 35 días no.
- **`key_vault_key_id` es ForceNew**: añadir la clave del cliente recrea la cuenta, aunque el servicio permite activarla en una existente. Decídelo al crear o hazlo fuera de Terraform.
- `minimal_tls_version` solo acepta `Tls12`, igual que el servicio.
- `default_identity_type` vale `FirstPartyIdentity` por defecto; con clave del cliente y copia continua hay que poner la identidad de usuario.

### Estructura en el proyecto

```txt
/
├── providers.tf    # azurerm >= 4.81.0
├── cosmosdb.tf     # identidad, cuenta, bases, contenedores, RBAC de datos, endpoints y diagnóstico
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
      # Validado con 4.81.0 (API 2024-08-15: local_authentication_enabled, capacity y RBAC de datos).
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

### `cosmosdb.tf`

```hcl
# =============================================================================
# Azure Cosmos DB for NoSQL seguro por defecto: sin acceso público (solo private endpoints),
# sin claves (solo Microsoft Entra con RBAC de datos), sin escrituras de metadatos con claves,
# zonas en cada región, copia continua, clave del cliente opcional y diagnóstico en tablas
# dedicadas
#
# DEPENDENCY: grupos de recursos creados
# DEPENDENCY: subred de endpoints y zona privatelink.documents.azure.com enlazada a las VNets
#             que resuelven
# DEPENDENCY: identidades de Entra (aplicaciones o identidades gestionadas) para el RBAC de datos
# DEPENDENCY: con clave del cliente: Key Vault con soft delete y purge protection, clave RSA
# DEPENDENCY: espacio de trabajo de Log Analytics
# =============================================================================

variable "cosmosdb_accounts" {
  description = "Cuentas de Azure Cosmos DB for NoSQL (clave = nombre, único en Azure)."
  type = map(object({
    resource_group_name = string
    location            = string                          # región del recurso (la de prioridad 0)
    capacity_mode       = optional(string, "Provisioned") # Provisioned | Serverless (solo al crear)

    # Regiones: clave = región; prioridad 0 = región de escritura
    geo_locations = map(object({
      failover_priority = number
      zone_redundant    = optional(bool, true) # en regiones con zonas; en cuentas existentes solo al añadir región
    }))
    automatic_failover_enabled       = optional(bool, true)
    multiple_write_locations_enabled = optional(bool, false) # escritura multirregión (Business Critical)

    consistency = optional(object({
      level                   = optional(string, "Session")
      max_interval_in_seconds = optional(number) # solo BoundedStaleness
      max_staleness_prefix    = optional(number) # solo BoundedStaleness
    }), {})

    backup = optional(object({
      type                = optional(string, "Continuous")      # Continuous | Periodic
      tier                = optional(string, "Continuous7Days") # Continuous7Days | Continuous30Days
      interval_in_minutes = optional(number, 240)               # solo Periodic
      retention_in_hours  = optional(number, 8)                 # solo Periodic
      storage_redundancy  = optional(string, "Geo")             # solo Periodic: Geo | Zone | Local
    }), {})

    free_tier_enabled      = optional(bool, false) # una cuenta por suscripción; no en serverless
    total_throughput_limit = optional(number)      # tope de RU/s de la cuenta (-1 = sin límite)

    private_endpoints = map(object({
      subnet_id           = string
      private_dns_zone_id = string
    }))

    customer_managed_key = optional(object({
      key_vault_id     = string
      key_vault_key_id = string # sin versión
    }))

    # RBAC de datos con los roles integrados (Reader | Contributor); scope vacío = toda la cuenta
    data_role_assignments = optional(map(object({
      principal_id = string
      role         = string
      database     = optional(string)
    })), {})

    sql_databases = optional(map(object({
      throughput               = optional(number) # compartido; mejor en el contenedor
      autoscale_max_throughput = optional(number)
      containers = optional(map(object({
        partition_key_paths      = list(string) # 2 o 3 niveles = clave jerárquica (MultiHash, versión 2)
        partition_key_version    = optional(number)
        throughput               = optional(number)
        autoscale_max_throughput = optional(number)
        default_ttl              = optional(number) # -1 = TTL por elemento
      })), {})
    })), {})

    log_analytics_workspace_id = string
    diagnostic_log_categories = optional(list(string), [
      "ControlPlaneRequests",
      "QueryRuntimeStatistics",
      "PartitionKeyRUConsumption",
      "PartitionKeyStatistics",
    ])
    tags = optional(map(string), {})
  }))
  default = {}

  validation {
    condition     = alltrue([for k, v in var.cosmosdb_accounts : contains(["Provisioned", "Serverless"], v.capacity_mode)])
    error_message = "capacity_mode debe ser Provisioned o Serverless."
  }

  validation {
    condition = alltrue([
      for k, v in var.cosmosdb_accounts :
      length([for l, g in v.geo_locations : l if g.failover_priority == 0]) == 1 &&
      length(distinct([for l, g in v.geo_locations : g.failover_priority])) == length(v.geo_locations)
    ])
    error_message = "geo_locations necesita exactamente una región con prioridad 0 y prioridades únicas."
  }

  validation {
    condition = alltrue([
      for k, v in var.cosmosdb_accounts :
      contains([for l, g in v.geo_locations : l if g.failover_priority == 0], v.location)
    ])
    error_message = "location debe ser la región con failover_priority 0."
  }

  validation {
    condition = alltrue([
      for k, v in var.cosmosdb_accounts :
      v.capacity_mode != "Serverless" || (length(v.geo_locations) == 1 && !v.multiple_write_locations_enabled && !v.free_tier_enabled)
    ])
    error_message = "Serverless: una sola región, sin escritura multirregión y sin nivel gratuito."
  }

  validation {
    condition = alltrue(flatten([
      for k, v in var.cosmosdb_accounts : [
        for dk, d in v.sql_databases : concat(
          [v.capacity_mode != "Serverless" || (d.throughput == null && d.autoscale_max_throughput == null)],
          [for ck, c in d.containers : v.capacity_mode != "Serverless" || (c.throughput == null && c.autoscale_max_throughput == null)]
        )
      ]
    ]))
    error_message = "En serverless no se configura throughput en bases ni contenedores."
  }

  validation {
    condition = alltrue(flatten([
      for k, v in var.cosmosdb_accounts : [
        for dk, d in v.sql_databases : concat(
          [d.throughput == null || d.autoscale_max_throughput == null],
          [for ck, c in d.containers : c.throughput == null || c.autoscale_max_throughput == null]
        )
      ]
    ]))
    error_message = "throughput (manual) y autoscale_max_throughput son excluyentes."
  }

  validation {
    condition = alltrue(flatten([
      for k, v in var.cosmosdb_accounts : [
        for dk, d in v.sql_databases : [
          for ck, c in d.containers : length(c.partition_key_paths) >= 1 && length(c.partition_key_paths) <= 3
        ]
      ]
    ]))
    error_message = "partition_key_paths admite de 1 a 3 niveles."
  }

  validation {
    condition = alltrue([
      for k, v in var.cosmosdb_accounts :
      contains(["Strong", "BoundedStaleness", "Session", "ConsistentPrefix", "Eventual"], v.consistency.level)
    ])
    error_message = "consistency.level debe ser Strong, BoundedStaleness, Session, ConsistentPrefix o Eventual."
  }

  validation {
    condition = alltrue([
      for k, v in var.cosmosdb_accounts :
      !(v.multiple_write_locations_enabled && v.consistency.level == "Strong")
    ])
    error_message = "Strong no es compatible con escritura multirregión."
  }

  validation {
    condition = alltrue([
      for k, v in var.cosmosdb_accounts :
      !v.multiple_write_locations_enabled || length(v.geo_locations) >= 2
    ])
    error_message = "La escritura multirregión necesita al menos dos regiones."
  }

  validation {
    condition = alltrue([
      for k, v in var.cosmosdb_accounts :
      v.consistency.level != "BoundedStaleness" || (
        coalesce(v.consistency.max_interval_in_seconds, 0) >= (length(v.geo_locations) == 1 ? 5 : 300) &&
        coalesce(v.consistency.max_staleness_prefix, 0) >= (length(v.geo_locations) == 1 ? 1 : 100000)
      )
    ])
    error_message = "BoundedStaleness exige max_interval_in_seconds y max_staleness_prefix (mínimo 300 s y 100.000 en multirregión)."
  }

  validation {
    condition = alltrue([
      for k, v in var.cosmosdb_accounts :
      contains(["Continuous", "Periodic"], v.backup.type) &&
      (v.backup.type != "Continuous" || contains(["Continuous7Days", "Continuous30Days"], v.backup.tier))
    ])
    error_message = "backup.type debe ser Continuous (Continuous7Days | Continuous30Days) o Periodic."
  }

  validation {
    condition     = alltrue([for k, v in var.cosmosdb_accounts : length(v.private_endpoints) > 0])
    error_message = "El acceso público está deshabilitado: hace falta al menos un private endpoint."
  }

  validation {
    condition = alltrue(flatten([
      for k, v in var.cosmosdb_accounts : [
        for ak, a in v.data_role_assignments : contains(["Reader", "Contributor"], a.role) &&
        (a.database == null || contains(keys(v.sql_databases), coalesce(a.database, "-")))
      ]
    ]))
    error_message = "data_role_assignments: role Reader o Contributor y database, si se indica, declarada en sql_databases."
  }
}

# -----------------------------------------------------------------------------
# Identidad y rol para la clave del cliente (antes de crear la cuenta)
# -----------------------------------------------------------------------------
module "cosmosdb_identity" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//PRO/common/assigned_identity?ref=main"
  for_each = { for k, v in var.cosmosdb_accounts : k => v if v.customer_managed_key != null }

  name                = "id-${each.key}"
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  tags                = merge(var.tags, each.value.tags)
}

resource "azurerm_role_assignment" "cosmosdb_cmk" {
  for_each = { for k, v in var.cosmosdb_accounts : k => v if v.customer_managed_key != null }

  scope                            = each.value.customer_managed_key.key_vault_id
  role_definition_name             = "Key Vault Crypto Service Encryption User"
  principal_id                     = module.cosmosdb_identity[each.key].principal_id
  principal_type                   = "ServicePrincipal"
  skip_service_principal_aad_check = true
  description                      = "Cifrado con clave del cliente de ${each.key}"
}

# -----------------------------------------------------------------------------
# Cuenta (recurso nativo: Database/CosmosDB no valida con azurerm 4.x)
# -----------------------------------------------------------------------------
resource "azurerm_cosmosdb_account" "this" {
  for_each = var.cosmosdb_accounts

  name                = each.key
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  offer_type          = "Standard"
  kind                = "GlobalDocumentDB"

  dynamic "capabilities" {
    for_each = each.value.capacity_mode == "Serverless" ? ["EnableServerless"] : []
    content {
      name = capabilities.value
    }
  }

  consistency_policy {
    consistency_level       = each.value.consistency.level
    max_interval_in_seconds = each.value.consistency.level == "BoundedStaleness" ? each.value.consistency.max_interval_in_seconds : null
    max_staleness_prefix    = each.value.consistency.level == "BoundedStaleness" ? each.value.consistency.max_staleness_prefix : null
  }

  dynamic "geo_location" {
    for_each = each.value.geo_locations
    content {
      location          = geo_location.key
      failover_priority = geo_location.value.failover_priority
      zone_redundant    = geo_location.value.zone_redundant
    }
  }

  automatic_failover_enabled       = each.value.automatic_failover_enabled
  multiple_write_locations_enabled = each.value.multiple_write_locations_enabled
  free_tier_enabled                = each.value.free_tier_enabled

  # Seguridad: sin red pública, sin claves y sin cambios de metadatos con claves
  public_network_access_enabled         = false
  is_virtual_network_filter_enabled     = false
  network_acl_bypass_for_azure_services = false
  local_authentication_enabled          = false
  access_key_metadata_writes_enabled    = false
  minimal_tls_version                   = "Tls12"

  backup {
    type                = each.value.backup.type
    tier                = each.value.backup.type == "Continuous" ? each.value.backup.tier : null
    interval_in_minutes = each.value.backup.type == "Periodic" ? each.value.backup.interval_in_minutes : null
    retention_in_hours  = each.value.backup.type == "Periodic" ? each.value.backup.retention_in_hours : null
    storage_redundancy  = each.value.backup.type == "Periodic" ? each.value.backup.storage_redundancy : null
  }

  dynamic "capacity" {
    for_each = each.value.total_throughput_limit != null ? [each.value.total_throughput_limit] : []
    content {
      total_throughput_limit = capacity.value
    }
  }

  dynamic "identity" {
    for_each = each.value.customer_managed_key != null ? [1] : []
    content {
      type         = "UserAssigned"
      identity_ids = [module.cosmosdb_identity[each.key].id]
    }
  }
  key_vault_key_id      = try(each.value.customer_managed_key.key_vault_key_id, null)
  default_identity_type = each.value.customer_managed_key != null ? "UserAssignedIdentity=${module.cosmosdb_identity[each.key].id}" : "FirstPartyIdentity"

  tags = merge(var.tags, each.value.tags)

  depends_on = [azurerm_role_assignment.cosmosdb_cmk]
}

resource "azurerm_cosmosdb_sql_database" "this" {
  for_each = merge([
    for k, v in var.cosmosdb_accounts : {
      for dk, d in v.sql_databases : "${k}/${dk}" => merge(d, { account = k, name = dk, rg = v.resource_group_name })
    }
  ]...)

  name                = each.value.name
  resource_group_name = each.value.rg
  account_name        = azurerm_cosmosdb_account.this[each.value.account].name
  throughput          = each.value.throughput

  dynamic "autoscale_settings" {
    for_each = each.value.autoscale_max_throughput != null ? [each.value.autoscale_max_throughput] : []
    content {
      max_throughput = autoscale_settings.value
    }
  }
}

resource "azurerm_cosmosdb_sql_container" "this" {
  for_each = merge(flatten([
    for k, v in var.cosmosdb_accounts : [
      for dk, d in v.sql_databases : {
        for ck, c in d.containers : "${k}/${dk}/${ck}" => merge(c, { account = k, database = dk, name = ck, rg = v.resource_group_name })
      }
    ]
  ])...)

  name                  = each.value.name
  resource_group_name   = each.value.rg
  account_name          = azurerm_cosmosdb_account.this[each.value.account].name
  database_name         = azurerm_cosmosdb_sql_database.this["${each.value.account}/${each.value.database}"].name
  partition_key_paths   = each.value.partition_key_paths
  partition_key_kind    = length(each.value.partition_key_paths) > 1 ? "MultiHash" : "Hash"
  partition_key_version = each.value.partition_key_version != null ? each.value.partition_key_version : (length(each.value.partition_key_paths) > 1 ? 2 : null)
  throughput            = each.value.throughput
  default_ttl           = each.value.default_ttl

  dynamic "autoscale_settings" {
    for_each = each.value.autoscale_max_throughput != null ? [each.value.autoscale_max_throughput] : []
    content {
      max_throughput = autoscale_settings.value
    }
  }
}

# RBAC del plano de datos con los roles integrados (00...01 lector, 00...02 colaborador)
resource "azurerm_cosmosdb_sql_role_assignment" "this" {
  for_each = merge([
    for k, v in var.cosmosdb_accounts : {
      for ak, a in v.data_role_assignments : "${k}/${ak}" => merge(a, { account = k, rg = v.resource_group_name })
    }
  ]...)

  resource_group_name = each.value.rg
  account_name        = azurerm_cosmosdb_account.this[each.value.account].name
  role_definition_id  = "${azurerm_cosmosdb_account.this[each.value.account].id}/sqlRoleDefinitions/${each.value.role == "Reader" ? "00000000-0000-0000-0000-000000000001" : "00000000-0000-0000-0000-000000000002"}"
  principal_id        = each.value.principal_id
  scope               = each.value.database == null ? azurerm_cosmosdb_account.this[each.value.account].id : "${azurerm_cosmosdb_account.this[each.value.account].id}/dbs/${each.value.database}"

  depends_on = [azurerm_cosmosdb_sql_database.this]
}

module "cosmosdb_private_endpoint" {
  source = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Networking/Networking/modules/private_endpoint?ref=main"
  for_each = merge([
    for k, v in var.cosmosdb_accounts : {
      for pk, p in v.private_endpoints : "${k}-${pk}" => merge(p, { account = k, rg = v.resource_group_name, location = v.location })
    }
  ]...)

  private_endpoint_name          = "pe-${each.key}"
  custom_network_interface_name  = "nic-pe-${each.key}"
  resource_group_name            = each.value.rg
  location                       = each.value.location
  subnet_id                      = each.value.subnet_id
  private_connection_resource_id = azurerm_cosmosdb_account.this[each.value.account].id
  subresource_names              = ["Sql"]
  private_dns_zone_ids           = [each.value.private_dns_zone_id]
  tags                           = merge(var.tags, var.cosmosdb_accounts[each.value.account].tags)
}

# Tablas dedicadas (CDB*). DataPlaneRequests registra cada petición y sale caro: añadirlo
# (o DataPlaneRequests5M, agregado, en preview) solo si hace falta
module "cosmosdb_diagnostics" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Security/Seguridad/modules/monitor_diagnostic_setting?ref=main"
  for_each = var.cosmosdb_accounts

  monitor_diagnostic_setting_name = "diag-${each.key}"
  target_resource_id              = azurerm_cosmosdb_account.this[each.key].id
  log_analytics_workspace_id      = each.value.log_analytics_workspace_id
  log_analytics_destination_type  = "Dedicated"
  enabled_logs                    = [for c in each.value.diagnostic_log_categories : { category = c }]
  # Las métricas de plataforma ya se recogen solas; Cosmos DB no admite exportarlas como categoría
}

# -----------------------------------------------------------------------------
# Salidas
# -----------------------------------------------------------------------------
output "cosmosdb_account_ids" {
  description = "IDs de las cuentas."
  value       = { for k, a in azurerm_cosmosdb_account.this : k => a.id }
}

output "cosmosdb_endpoints" {
  description = "Endpoint de cada cuenta (las aplicaciones entran con Entra, sin claves)."
  value       = { for k, a in azurerm_cosmosdb_account.this : k => a.endpoint }
}

output "cosmosdb_sql_container_ids" {
  description = "IDs de los contenedores."
  value       = { for k, c in azurerm_cosmosdb_sql_container.this : k => c.id }
}
```

### `env/pro.tfvars`

Cuenta con dos regiones y zonas, copia continua de 30 días, tope de RU/s, clave jerárquica y RBAC de datos por base.

```hcl
tags = {
  environment = "pro"
  workload    = "<workload>"
  owner       = "<owner>"
  costcenter  = "<costcenter>"
}

cosmosdb_accounts = {
  "cosmos-<workload>-pro-01" = {
    resource_group_name = "<rg-data-pro>"
    location            = "<region>"

    # Escritura en <region> con zonas y lectura en <region-dr>: failover gestionado por el servicio
    geo_locations = {
      "<region>"    = { failover_priority = 0 }
      "<region-dr>" = { failover_priority = 1 }
    }

    backup = {
      type = "Continuous"
      tier = "Continuous30Days"
    }

    total_throughput_limit = 20000 # tope de coste de la cuenta

    private_endpoints = {
      app = {
        subnet_id           = "<resourceId snet-pe-pro>"
        private_dns_zone_id = "<resourceId privatelink.documents.azure.com>"
      }
    }

    data_role_assignments = {
      app = {
        principal_id = "<principalId identidad-app>"
        role         = "Contributor"
        database     = "appdb"
      }
      lectura = {
        principal_id = "<principalId grupo-lectura-pro>"
        role         = "Reader"
      }
    }

    sql_databases = {
      appdb = {
        containers = {
          orders = {
            partition_key_paths      = ["/tenantId", "/customerId", "/id"] # jerárquica
            autoscale_max_throughput = 4000
          }
          sessions = {
            partition_key_paths      = ["/id"]
            autoscale_max_throughput = 1000
            default_ttl              = 86400
          }
        }
      }
    }

    log_analytics_workspace_id = "<resourceId log-<workload>-pro>"
  }
}
```

### Despliegue y comprobación

```powershell
terraform init
terraform plan -var-file="env/pro.tfvars" -out="pro.tfplan"
terraform apply "pro.tfplan"

Get-AzCosmosDBAccount -ResourceGroupName "<rg-data-pro>" -Name "cosmos-<workload>-pro-01" | Format-List
Get-AzCosmosDBSqlRoleDefinition -ResourceGroupName "<rg-data-pro>" -AccountName "cosmos-<workload>-pro-01"
```

Asignar el rol de datos a otra identidad sin pasar por Terraform:

```powershell
$account = Get-AzCosmosDBAccount -ResourceGroupName "<rg-data-pro>" -Name "cosmos-<workload>-pro-01"
New-AzCosmosDBSqlRoleAssignment -ResourceGroupName "<rg-data-pro>" -AccountName $account.Name `
    -RoleDefinitionId "$($account.Id)/sqlRoleDefinitions/00000000-0000-0000-0000-000000000001" `
    -Scope $account.Id -PrincipalId "<principalId>"
```

### Equivalente en Bicep

Una plantilla por cuenta con la API GA 2025-10-15. Los contenedores con varias rutas usan `MultiHash` versión 2, como en el ejemplo de Learn. Para el rol sobre el Key Vault de otro grupo de recursos usa `role-on-resource.bicep`, el mismo de las fichas de SQL y PostgreSQL.

`cosmosdb.bicep`:

```bicep
// =============================================================================
// Azure Cosmos DB for NoSQL seguro por defecto: sin acceso público (solo private endpoints),
// sin claves (solo Microsoft Entra con RBAC de datos), sin escrituras de metadatos con claves,
// zonas en cada región, copia continua, clave del cliente opcional y diagnóstico en tablas
// dedicadas
// DEPENDENCY: zona privatelink.documents.azure.com; identidades de Entra para el RBAC de datos
// DEPENDENCY: Key Vault con soft delete y purge protection (si hay clave del cliente)
// DEPENDENCY: role-on-resource.bicep en la misma carpeta
// =============================================================================
@minLength(3)
@maxLength(44)
param name string

@description('[{ locationName, failoverPriority, isZoneRedundant? (true) }]; prioridad 0 = escritura')
@minLength(1)
param locations array

@allowed(['Provisioned', 'Serverless'])
param capacityMode string = 'Provisioned'
param automaticFailover bool = true
param multipleWriteLocations bool = false

@description('{ level (Session), maxIntervalInSeconds?, maxStalenessPrefix? }')
param consistency object = {
  level: 'Session'
}

@description('{ type (Continuous | Periodic), tier? (Continuous7Days | Continuous30Days), intervalInMinutes?, retentionInHours?, storageRedundancy? }')
param backup object = {
  type: 'Continuous'
  tier: 'Continuous7Days'
}

param freeTier bool = false
@description('Tope de RU/s de la cuenta; -1 o 0 = sin tope')
param totalThroughputLimit int = -1

@description('[{ name, subnetId, privateDnsZoneId }]')
@minLength(1)
param privateEndpoints array

@description('Clave del cliente: { keyVaultId, keyUri (sin versión) }')
param customerManagedKey object = {}

@description('[{ name, principalId, role (Reader | Contributor), database? }]')
param dataRoleAssignments array = []

@description('{ base: { throughput?, autoscaleMaxThroughput?, containers: { nombre: { partitionKeyPaths, throughput?, autoscaleMaxThroughput?, defaultTtl? } } } }')
param sqlDatabases object = {}

param logAnalyticsWorkspaceId string
param diagnosticLogCategories array = [
  'ControlPlaneRequests'
  'QueryRuntimeStatistics'
  'PartitionKeyRUConsumption'
  'PartitionKeyStatistics'
]

param tags object = {}

var useCmk = !empty(customerManagedKey)
var writeLocation = filter(locations, l => l.failoverPriority == 0)[0].locationName
var containers = flatten(map(
  items(sqlDatabases),
  d =>
    map(items(d.value.?containers ?? {}), c => {
      database: d.key
      name: c.key
      value: c.value
    })
))

resource identity 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = if (useCmk) {
  name: 'id-${name}'
  location: writeLocation
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

resource account 'Microsoft.DocumentDB/databaseAccounts@2025-10-15' = {
  name: name
  location: writeLocation
  tags: tags
  kind: 'GlobalDocumentDB'
  identity: useCmk
    ? {
        type: 'UserAssigned'
        userAssignedIdentities: {
          '${identity.id}': {}
        }
      }
    : null
  properties: {
    databaseAccountOfferType: 'Standard'
    locations: [
      for l in locations: {
        locationName: l.locationName
        failoverPriority: l.failoverPriority
        isZoneRedundant: l.?isZoneRedundant ?? true
      }
    ]
    capabilities: capacityMode == 'Serverless'
      ? [
          {
            name: 'EnableServerless'
          }
        ]
      : []
    consistencyPolicy: {
      defaultConsistencyLevel: consistency.level
      maxIntervalInSeconds: consistency.level == 'BoundedStaleness' ? consistency.maxIntervalInSeconds : null
      maxStalenessPrefix: consistency.level == 'BoundedStaleness' ? consistency.maxStalenessPrefix : null
    }
    enableAutomaticFailover: automaticFailover
    enableMultipleWriteLocations: multipleWriteLocations
    enableFreeTier: freeTier
    // Seguridad: sin red pública, sin claves y sin cambios de metadatos con claves
    publicNetworkAccess: 'Disabled'
    isVirtualNetworkFilterEnabled: false
    networkAclBypass: 'None'
    disableLocalAuth: true
    disableKeyBasedMetadataWriteAccess: true
    minimalTlsVersion: 'Tls12'
    backupPolicy: backup.type == 'Continuous'
      ? {
          type: 'Continuous'
          continuousModeProperties: {
            tier: backup.?tier ?? 'Continuous7Days'
          }
        }
      : {
          type: 'Periodic'
          periodicModeProperties: {
            backupIntervalInMinutes: backup.?intervalInMinutes ?? 240
            backupRetentionIntervalInHours: backup.?retentionInHours ?? 8
            backupStorageRedundancy: backup.?storageRedundancy ?? 'Geo'
          }
        }
    capacity: totalThroughputLimit > 0
      ? {
          totalThroughputLimit: totalThroughputLimit
        }
      : null
    keyVaultKeyUri: useCmk ? customerManagedKey.keyUri : null
    defaultIdentity: useCmk ? 'UserAssignedIdentity=${identity.id}' : 'FirstPartyIdentity'
  }
  dependsOn: [
    cmkRole
  ]
}

resource dbs 'Microsoft.DocumentDB/databaseAccounts/sqlDatabases@2025-10-15' = [
  for d in items(sqlDatabases): {
    parent: account
    name: d.key
    properties: {
      resource: {
        id: d.key
      }
      options: capacityMode == 'Serverless'
        ? {}
        : union(
            contains(d.value, 'throughput') ? { throughput: d.value.throughput } : {},
            contains(d.value, 'autoscaleMaxThroughput')
              ? { autoscaleSettings: { maxThroughput: d.value.autoscaleMaxThroughput } }
              : {}
          )
    }
  }
]

resource sqlContainers 'Microsoft.DocumentDB/databaseAccounts/sqlDatabases/containers@2025-10-15' = [
  for c in containers: {
    name: '${name}/${c.database}/${c.name}'
    properties: {
      resource: {
        id: c.name
        partitionKey: {
          paths: c.value.partitionKeyPaths
          kind: length(c.value.partitionKeyPaths) > 1 ? 'MultiHash' : 'Hash'
          version: length(c.value.partitionKeyPaths) > 1 ? 2 : null
        }
        defaultTtl: c.value.?defaultTtl
      }
      options: capacityMode == 'Serverless'
        ? {}
        : union(
            contains(c.value, 'throughput') ? { throughput: c.value.throughput } : {},
            contains(c.value, 'autoscaleMaxThroughput')
              ? { autoscaleSettings: { maxThroughput: c.value.autoscaleMaxThroughput } }
              : {}
          )
    }
    dependsOn: [
      dbs
    ]
  }
]

// RBAC del plano de datos con los roles integrados (00...01 lector, 00...02 colaborador)
resource dataRoles 'Microsoft.DocumentDB/databaseAccounts/sqlRoleAssignments@2025-10-15' = [
  for a in dataRoleAssignments: {
    parent: account
    name: guid(account.id, a.name, a.principalId)
    properties: {
      roleDefinitionId: '${account.id}/sqlRoleDefinitions/${a.role == 'Reader' ? '00000000-0000-0000-0000-000000000001' : '00000000-0000-0000-0000-000000000002'}'
      principalId: a.principalId
      scope: empty(a.?database ?? '') ? account.id : '${account.id}/dbs/${a.database}'
    }
    dependsOn: [
      dbs
    ]
  }
]

resource pes 'Microsoft.Network/privateEndpoints@2024-05-01' = [
  for pe in privateEndpoints: {
    name: 'pe-${name}-${pe.name}'
    location: writeLocation
    tags: tags
    properties: {
      subnet: {
        id: pe.subnetId
      }
      customNetworkInterfaceName: 'nic-pe-${name}-${pe.name}'
      privateLinkServiceConnections: [
        {
          name: 'Sql'
          properties: {
            privateLinkServiceId: account.id
            groupIds: [
              'Sql'
            ]
          }
        }
      ]
    }
  }
]

resource peDns 'Microsoft.Network/privateEndpoints/privateDnsZoneGroups@2024-05-01' = [
  for (pe, i) in privateEndpoints: {
    parent: pes[i]
    name: 'default'
    properties: {
      privateDnsZoneConfigs: [
        {
          name: 'documents'
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
  scope: account
  properties: {
    workspaceId: logAnalyticsWorkspaceId
    logAnalyticsDestinationType: 'Dedicated'
    logs: [
      for c in diagnosticLogCategories: {
        category: c
        enabled: true
      }
    ]
  }
}

output accountId string = account.id
output endpoint string = account.properties.documentEndpoint
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

`cosmos-workload-pro-01.bicepparam`:

```bicep
using 'cosmosdb.bicep'

param name = 'cosmos-<workload>-pro-01'

// Escritura en <region> con zonas y lectura en <region-dr>
param locations = [
  {
    locationName: '<region>'
    failoverPriority: 0
  }
  {
    locationName: '<region-dr>'
    failoverPriority: 1
  }
]

param backup = {
  type: 'Continuous'
  tier: 'Continuous30Days'
}

param totalThroughputLimit = 20000

param privateEndpoints = [
  {
    name: 'app'
    subnetId: '<resourceId snet-pe-pro>'
    privateDnsZoneId: '<resourceId privatelink.documents.azure.com>'
  }
]

param dataRoleAssignments = [
  {
    name: 'app'
    principalId: '<principalId identidad-app>'
    role: 'Contributor'
    database: 'appdb'
  }
  {
    name: 'lectura'
    principalId: '<principalId grupo-lectura-pro>'
    role: 'Reader'
  }
]

param sqlDatabases = {
  appdb: {
    containers: {
      orders: {
        partitionKeyPaths: [
          '/tenantId'
          '/customerId'
          '/id'
        ]
        autoscaleMaxThroughput: 4000
      }
      sessions: {
        partitionKeyPaths: [
          '/id'
        ]
        autoscaleMaxThroughput: 1000
        defaultTtl: 86400
      }
    }
  }
}

param logAnalyticsWorkspaceId = '<resourceId log-<workload>-pro>'

param tags = {
  environment: 'pro'
  workload: '<workload>'
}
```

Despliegue:

```powershell
New-AzResourceGroupDeployment -ResourceGroupName "<rg-data-pro>" `
    -TemplateParameterFile "cosmos-workload-pro-01.bicepparam" -Name "cosmos-<workload>-pro-01"
```

## Errores típicos

| Síntoma | Causa | Solución |
|---|---|---|
| `Unsupported argument` sobre `enable_automatic_failover` en `terraform validate` | Módulo `Database/CosmosDB` con nombres de azurerm 3.x | Recurso nativo con `automatic_failover_enabled` y equivalentes |
| `terraform plan` quiere recrear la cuenta | Cambio de `key_vault_key_id`, `kind` o `free_tier_enabled` (ForceNew) | Decisiones de creación; la clave del cliente en una cuenta existente, fuera de Terraform |
| Las aplicaciones fallan tras desactivar las claves | Siguen usando cadena de conexión o clave | `DefaultAzureCredential` y rol de datos asignado a su identidad |
| `Operation 'POST' on resource ... is not allowed through Azure Cosmos DB endpoint` | Metadatos bloqueados y el SDK intenta crear bases o contenedores | Crearlos por IaC, CLI o PowerShell |
| 429 con RU/s libres en la cuenta | Partición caliente o throughput compartido en la base | Revisar `CDBPartitionKeyRUConsumption`; clave con más valores o jerárquica; throughput por contenedor |
| Escrituras rechazadas en una partición | La partición lógica llegó a 20 GB | Clave jerárquica terminada en `/id` (contenedor nuevo y copia) |
| Nadie conecta tras crear el private endpoint | DNS sin la zona `privatelink.documents.azure.com` o firewall con modo directo | Zona enlazada a la VNet; puertos TCP 0-65535 abiertos hacia el endpoint |
| Corte de unos 5 minutos al añadir un private endpoint | Comportamiento por defecto en cuentas existentes | Permitir antes IP o VNet, esperar 10 minutos, crear el endpoint y quitar la regla |
| No se pueden activar zonas en la región actual | En cuentas existentes solo al añadir una región | Añadir una región temporal y seguir el procedimiento de Learn |
| Failover regional que no llega | El failover gestionado puede tardar una hora o más | Failover forzado (región offline) o PPAF |
| No se puede volver a copia periódica | La migración a continua es irreversible | Asumirlo antes de migrar |
| La cuenta solo permite borrarse | Clave del cliente revocada | Restaurar el acceso a la clave antes de cualquier otra operación |
| Coste alto de Log Analytics | `DataPlaneRequests` por petición | Categorías agregadas (`DataPlaneRequests5M`) o solo las de particiones y consultas |
