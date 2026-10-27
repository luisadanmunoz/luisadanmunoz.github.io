---
title: "Azure SQL Database"
indice: database
resumen: "SQL Server como servicio."
estado: documentado   # proximamente | en-curso | documentado
orden: 1
last_review: 2026-10-27
fuentes:
  - titulo: "What is Azure SQL Database?"
    url: https://learn.microsoft.com/azure/azure-sql/database/sql-database-paas-overview
  - titulo: "Features comparison: Azure SQL Database and Azure SQL Managed Instance"
    url: https://learn.microsoft.com/azure/azure-sql/database/features-comparison
  - titulo: "Compare vCore and DTU-based purchasing models of Azure SQL Database"
    url: https://learn.microsoft.com/azure/azure-sql/database/purchasing-models
  - titulo: "vCore purchasing model - Azure SQL Database"
    url: https://learn.microsoft.com/azure/azure-sql/database/service-tiers-sql-database-vcore
  - titulo: "Hyperscale service tier"
    url: https://learn.microsoft.com/azure/azure-sql/database/service-tier-hyperscale
  - titulo: "Hyperscale secondary replicas"
    url: https://learn.microsoft.com/azure/azure-sql/database/service-tier-hyperscale-replicas
  - titulo: "Serverless compute tier for Azure SQL Database"
    url: https://learn.microsoft.com/azure/azure-sql/database/serverless-tier-overview
  - titulo: "Serverless compute tier billing for Azure SQL Database"
    url: https://learn.microsoft.com/azure/azure-sql/database/serverless-tier-billing
  - titulo: "Auto-pause and auto-resume in the serverless compute tier"
    url: https://learn.microsoft.com/azure/azure-sql/database/serverless-tier-auto-pause-resume
  - titulo: "Deploy Azure SQL Database for free"
    url: https://learn.microsoft.com/azure/azure-sql/database/free-tier
  - titulo: "Elastic pools help you manage and scale multiple databases in Azure SQL Database"
    url: https://learn.microsoft.com/azure/azure-sql/database/elastic-pool-overview
  - titulo: "Plan and manage costs for Azure SQL Database"
    url: https://learn.microsoft.com/azure/azure-sql/database/cost-management
  - titulo: "Azure Hybrid Benefit - Azure SQL Database & SQL Managed Instance"
    url: https://learn.microsoft.com/azure/azure-sql/azure-hybrid-benefit
  - titulo: "How a reservation discount is applied to Azure SQL Database"
    url: https://learn.microsoft.com/azure/cost-management-billing/reservations/understand-reservation-charges
  - titulo: "Configure a license-free standby replica for Azure SQL Database"
    url: https://learn.microsoft.com/azure/azure-sql/database/standby-replica-how-to-configure
  - titulo: "Availability through redundancy - Azure SQL Database"
    url: https://learn.microsoft.com/azure/azure-sql/database/high-availability-sla-local-zone-redundancy
  - titulo: "Enable zone redundancy for Azure SQL Database"
    url: https://learn.microsoft.com/azure/azure-sql/database/enable-zone-redundancy
  - titulo: "Create a zone-redundant Hyperscale database"
    url: https://learn.microsoft.com/azure/azure-sql/database/hyperscale-create-zone-redundant-database
  - titulo: "Reliability in Azure SQL Database"
    url: https://learn.microsoft.com/azure/reliability/reliability-sql-database
  - titulo: "Automated backups in Azure SQL Database"
    url: https://learn.microsoft.com/azure/azure-sql/database/automated-backups-overview
  - titulo: "Long-term retention backups"
    url: https://learn.microsoft.com/azure/azure-sql/database/long-term-retention-overview
  - titulo: "Failover groups overview & best practices (Azure SQL Database)"
    url: https://learn.microsoft.com/azure/azure-sql/database/failover-group-sql-db
  - titulo: "Configure a failover group for Azure SQL Database"
    url: https://learn.microsoft.com/azure/azure-sql/database/failover-group-configure-sql-db
  - titulo: "Maintenance window in Azure SQL Database"
    url: https://learn.microsoft.com/azure/azure-sql/database/maintenance-window
  - titulo: "Maintenance window FAQ in Azure SQL Database"
    url: https://learn.microsoft.com/azure/azure-sql/database/maintenance-window-faq
  - titulo: "Secure your Azure SQL Database"
    url: https://learn.microsoft.com/azure/azure-sql/database/secure-database
  - titulo: "Connectivity settings"
    url: https://learn.microsoft.com/azure/azure-sql/database/connectivity-settings
  - titulo: "Azure SQL Database network access controls"
    url: https://learn.microsoft.com/azure/azure-sql/database/network-access-controls-overview
  - titulo: "Azure Private Link for Azure SQL Database"
    url: https://learn.microsoft.com/azure/azure-sql/database/private-endpoint-overview
  - titulo: "Azure Private Endpoint private DNS zone values"
    url: https://learn.microsoft.com/azure/private-link/private-endpoint-dns
  - titulo: "Outbound firewall rules for Azure SQL Database"
    url: https://learn.microsoft.com/azure/azure-sql/database/outbound-firewall-rule-overview
  - titulo: "Use virtual network service endpoints and rules for servers in Azure SQL Database"
    url: https://learn.microsoft.com/azure/azure-sql/database/vnet-service-endpoint-rule-overview
  - titulo: "Troubleshoot connectivity issues and other errors"
    url: https://learn.microsoft.com/azure/azure-sql/database/troubleshoot-common-errors-issues
  - titulo: "Microsoft Entra-only authentication with Azure SQL"
    url: https://learn.microsoft.com/azure/azure-sql/database/authentication-azure-ad-only-authentication
  - titulo: "Managed identities in Microsoft Entra for Azure SQL"
    url: https://learn.microsoft.com/azure/azure-sql/database/authentication-azure-ad-user-assigned-managed-identity
  - titulo: "Configure and manage Microsoft Entra authentication with Azure SQL"
    url: https://learn.microsoft.com/azure/azure-sql/database/authentication-aad-configure
  - titulo: "Azure SQL Transparent Data Encryption with customer-managed key"
    url: https://learn.microsoft.com/azure/azure-sql/database/transparent-data-encryption-byok-overview
  - titulo: "Managed identities for transparent data encryption with customer-managed key"
    url: https://learn.microsoft.com/azure/azure-sql/database/transparent-data-encryption-byok-identity
  - titulo: "Scan your Azure SQL databases for vulnerabilities"
    url: https://learn.microsoft.com/azure/defender-for-cloud/sql-azure-vulnerability-assessment-overview
  - titulo: "Enable vulnerability assessment (Express)"
    url: https://learn.microsoft.com/azure/defender-for-cloud/sql-azure-vulnerability-assessment-enable
  - titulo: "Migrate from classic Defender for SQL APIs"
    url: https://learn.microsoft.com/azure/defender-for-cloud/migrate-classic-defender-for-sql-apis
  - titulo: "Auditing for Azure SQL Database"
    url: https://learn.microsoft.com/azure/azure-sql/database/auditing-overview
  - titulo: "Set up Auditing for Azure SQL Database"
    url: https://learn.microsoft.com/azure/azure-sql/database/auditing-setup
  - titulo: "Configure streaming export of diagnostic telemetry"
    url: https://learn.microsoft.com/azure/azure-sql/database/metrics-diagnostic-telemetry-logging-streaming-export-configure
  - titulo: "Supported logs for Microsoft.Sql/servers/databases"
    url: https://learn.microsoft.com/azure/azure-monitor/reference/supported-logs/microsoft-sql-servers-databases-logs
  - titulo: "Monitor Azure SQL Database with metrics and alerts"
    url: https://learn.microsoft.com/azure/azure-sql/database/monitoring-metrics-alerts
  - titulo: "Monitor Azure SQL workloads with database watcher (preview)"
    url: https://learn.microsoft.com/azure/azure-sql/database-watcher-overview
  - titulo: "Ledger overview"
    url: https://learn.microsoft.com/sql/relational-databases/security/ledger/ledger-overview
  - titulo: "Azure built-in roles for Security"
    url: https://learn.microsoft.com/azure/role-based-access-control/built-in-roles/security
  - titulo: "azurerm_mssql_server"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/mssql_server
  - titulo: "azurerm_mssql_database"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/mssql_database
  - titulo: "azurerm_mssql_failover_group"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/mssql_failover_group
  - titulo: "Microsoft.Sql servers (plantillas ARM/Bicep)"
    url: https://learn.microsoft.com/azure/templates/microsoft.sql/servers
  - titulo: "Microsoft.Sql servers/databases (plantillas ARM/Bicep)"
    url: https://learn.microsoft.com/azure/templates/microsoft.sql/servers/databases
  - titulo: "Módulo Terraform Database/SQLServer"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Database/SQLServer
  - titulo: "Módulo Terraform Database/SQLDatabase"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Database/SQLDatabase
  - titulo: "Módulo Terraform Database/SQLElasticPool"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Database/SQLElasticPool
  - titulo: "Módulo Terraform PRO/common/assigned_identity"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/PRO/common/assigned_identity
  - titulo: "Módulo Terraform Networking/Networking/modules/private_endpoint"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Networking/Networking/modules/private_endpoint
  - titulo: "Módulo Terraform Security/Seguridad/modules/monitor_diagnostic_setting"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Security/Seguridad/modules/monitor_diagnostic_setting
---

**Azure SQL Database** es el motor de SQL Server como servicio: Microsoft aplica parches y actualizaciones, hace las copias de seguridad y gestiona la alta disponibilidad. Cada base de datos vive en un **servidor lógico**, que es el punto de conexión, el límite de red y el lugar donde se configuran autenticación, auditoría y cifrado. Si la aplicación necesita funcionalidades de instancia (Agent, cross-database, CLR...), la alternativa es [SQL Managed Instance](/recursos/database/sql-managed-instance/); si necesita control del sistema operativo, [SQL Server en VM](/recursos/database/sql-server-en-vm/).

## Qué es y cuándo usarlo

### Modelos de compra y niveles

Hay dos modelos: **DTU** (Basic, Standard y Premium, paquetes cerrados de CPU, memoria e IO) y **vCore**. vCore permite elegir hardware, vCores y almacenamiento, y es el único con Azure Hybrid Benefit y reservas. Esta ficha trabaja solo con vCore.

| | **General Purpose** | **Business Critical** | **Hyperscale** |
|---|---|---|---|
| Para qué | Equilibrado y orientado a presupuesto | OLTP con muchas transacciones y baja latencia de IO | **Nivel recomendado y por defecto para OLTP y HTAP nuevos o en modernización** |
| vCores | 2-128 | 2-128 | 2-192 |
| Almacenamiento | 1 GB-4 TB, remoto premium | 1 GB-4 TB, SSD local | Hasta 128 TB, crece según uso |
| Réplicas | Una, sin lectura | Tres réplicas y una de lectura incluida | 0-4 de alta disponibilidad y hasta 30 réplicas con nombre |
| Facturación | vCores, almacenamiento reservado y copias | vCores, almacenamiento reservado y copias | vCores **por réplica**, almacenamiento asignado (mínimo 10 GB) y copias; el log no se factura |
| Serverless | Sí | No | Sí (pausa automática en preview) |

### Cómputo provisionado o serverless

| | Provisioned | Serverless |
|---|---|---|
| Uso | Regular y con utilización media alta, o varias bases en un pool | Intermitente e impredecible, con utilización media baja |
| Facturación | Por hora | Por segundo: el mayor entre CPU y memoria usadas y el mínimo configurado |
| En pausa | — | Solo se paga el almacenamiento |
| Primera respuesta | Inmediata | Más lenta tras la pausa |
| Descuentos | Reservas y Azure Hybrid Benefit | **Ninguno de los dos** |

La pausa automática (mínimo 15 minutos en General Purpose y 60 en Hyperscale) **no ocurre** si hay geo-replicación o failover group, retención a largo plazo o un alias DNS en el servidor. Basta con una conexión abierta (un pool de conexiones, una sonda de salud) para que no se pause.

### Elastic pools

Un elastic pool comparte vCores entre muchas bases de datos del mismo servidor. Encaja con **muchas bases de utilización media baja y picos en momentos distintos** (SaaS con una base por cliente), no con varias bases de carga media-alta constante. El pool se factura por hora al máximo de vCores, sin cargo por base de datos, y el precio del vCore es el mismo que en una base única. El diagnóstico se configura en el pool y en cada base de datos.

### Red

| Decisión | Recomendación |
|---|---|
| Acceso | **Private endpoint** (subrecurso `sqlServer`, zona `privatelink.database.windows.net`) y **acceso público deshabilitado**: crear el private endpoint no bloquea el acceso público por sí solo |
| Reglas de firewall | Con el acceso público deshabilitado no se pueden crear ni modificar (error 42101) |
| "Allow Azure services" | Crea la regla `0.0.0.0` y abre el servidor a **cualquier recurso de Azure, de cualquier cliente**. Evitarla |
| Política de conexión | `Redirect` da menor latencia y más rendimiento, pero exige abrir **1433-65535** entre cliente y private endpoint. `Proxy` solo usa 1433. `Default` es Redirect dentro de Azure y Proxy fuera; los private endpoints existentes con Default usan Proxy |
| Salida | Reglas de salida: limitan auditoría, evaluación de vulnerabilidades, import/export, `OPENROWSET`, `BULK INSERT` y `sp_invoke_external_rest_endpoint` a una lista de FQDN. En geo-replicación, las mismas reglas en todos los servidores |
| TLS | 1.2 por defecto; 1.0 y 1.1 están retirados |
| Rutas por NVA o firewall | Enrutamiento simétrico: el NVA debe aplicar SNAT o la respuesta no vuelve por el mismo camino |

### Seguridad

| Control | Recomendación |
|---|---|
| Autenticación | **Solo Microsoft Entra**: deshabilita la autenticación SQL para todos, incluido el administrador del servidor. El administrador de Entra se define antes. Azure Policy puede exigirlo |
| Separación de funciones | Activar o desactivar "solo Entra" lo pueden hacer Owner, Contributor y SQL Security Manager, **no** SQL Server Contributor |
| Identidad del servidor | Identidad de usuario como identidad principal. Para crear usuarios de Entra (`CREATE USER ... FROM EXTERNAL PROVIDER`) necesita `User.Read.All`, `GroupMember.Read.All` y `Application.Read.All` en Microsoft Graph, que concede un Privileged Role Administrator (o el rol Directory Readers, más amplio) |
| Cifrado en reposo | TDE activo por defecto. Con **clave del cliente**: Key Vault con soft-delete y purge protection, clave RSA 2048 o 3072, y la identidad con *get*, *wrapKey* y *unwrapKey* (rol Key Vault Crypto Service Encryption User). Borrar esa identidad deja las bases **inaccesibles** |
| Amenazas y vulnerabilidades | Microsoft Defender for SQL en la suscripción: activa la protección frente a amenazas y la evaluación de vulnerabilidades **express** (sin cuenta de almacenamiento y con escaneos periódicos automáticos). Ver [Defender for Cloud](/recursos/security/microsoft-defender-for-cloud/) |
| APIs clásicas | Las APIs clásicas de evaluación de vulnerabilidades y protección frente a amenazas (por ejemplo, *Server Security Alert Policy*) se retiran el **16 de agosto de 2027** |
| Auditoría | A Log Analytics: se crea un diagnostic setting `SQLSecurityAuditEvents`; si alguien lo borra, la auditoría **falla en silencio**, así que conviene una alerta. Con mucha carga, la auditoría puede no registrar todos los eventos |
| Datos | Always Encrypted, ledger (a prueba de manipulaciones; una base ledger se define al crearla y no se puede revertir), enmascaramiento dinámico, clasificación y Row-Level Security |

### Disponibilidad y recuperación

| Capacidad | Detalle |
|---|---|
| Redundancia de zona | General Purpose (**con coste adicional**, solo hardware standard-series Gen5), Business Critical y Premium (**sin coste adicional**) y Hyperscale (sin coste adicional si hay varias réplicas). Basic y Standard no la admiten |
| Hyperscale en zonas | **Solo al crear**, con al menos 1 réplica de alta disponibilidad y copias ZRS o GZRS. Para cambiarlo: copia, restauración o geo-réplica |
| General Purpose y Business Critical | Se activa o desactiva en línea, con una breve desconexión |
| Caída de zona | Normalmente menos de 30 segundos y sin pérdida de datos |
| PITR | Retención de 1 a 35 días (7 por defecto); diferenciales cada 12 o 24 horas |
| Copias | LRS, ZRS o GRS. El geo-restore solo funciona con copias geo-redundantes, que se replican a la región emparejada |
| Retención larga (LTR) | Hasta 10 años, con opción de copias **inmutables** (WORM) |
| Failover groups | Política **gestionada por el cliente** (recomendada). La gestionada por Microsoft exige 1 hora de gracia como mínimo, falla todos los grupos de la región a la vez y puede tardar varias horas. Listeners `<grupo>.database.windows.net` y `<grupo>.secondary.database.windows.net` |
| Conmutación del cliente | Normalmente hasta 60 segundos; la conmutación forzada puede perder datos (replicación asíncrona) |
| Réplica standby | Secundario solo para recuperación ante desastres: **sin coste de licencia** (ahorro estimado del 35-40 %) |
| Borrado de servidor | Retención de servidores eliminados (soft delete) en preview |

### Mantenimiento

Por defecto, Azure bloquea la mayoría de las actualizaciones de 8:00 a 17:00 hora local de la región, pero las urgentes pueden llegar fuera de esa franja. Las ventanas **Weekday** (22:00-6:00, lunes a jueves) y **Weekend** (22:00-6:00, viernes a domingo) son gratuitas, limitan el mantenimiento planificado a esa franja (salvo casos excepcionales, como un parche de seguridad crítico) y permiten **avisos con 24 horas de antelación**. Con bases redundantes en zonas, las ventanas personalizadas solo están disponibles en algunas regiones. En un pool manda la ventana del pool. Con geo-réplica en regiones no emparejadas, conviene una ventana distinta en cada región.

### Cómo se factura

| Concepto | Detalle |
|---|---|
| Cómputo | vCores por hora (provisioned) o por segundo (serverless). En Hyperscale, cada réplica de alta disponibilidad se factura al mismo precio que la primaria |
| Almacenamiento | GP y BC: el tamaño máximo configurado, con un 30 % adicional para el log. Hyperscale: lo asignado |
| Copias | Almacenamiento de copias según redundancia y retención |
| Azure Hybrid Benefit | Licencias de SQL Server con Software Assurance; ahorro de hasta un 30 % o más. Solo vCore provisioned; **no** serverless ni Hyperscale nuevo |
| Reservas | Solo vCore provisioned; no serverless |
| Gratis | Hasta 10 bases General Purpose serverless por suscripción, cada una con **100.000 vCore-segundos, 32 GB de datos y 32 GB de copias al mes** |
| IOPS | No se facturan |

### Qué escenario recomiendo

| Escenario del cliente | Diseño | Por qué |
|---|---|---|
| Aplicación nueva o modernizada | Hyperscale provisioned, 1 réplica de alta disponibilidad, redundancia de zona | Nivel recomendado; escala de almacenamiento y lectura |
| OLTP crítico con IO de muy baja latencia | Business Critical redundante en zonas | SSD local y réplica de lectura incluida |
| Carga moderada con presupuesto ajustado | General Purpose provisioned | Coste predecible |
| Desarrollo, pruebas o carga intermitente | General Purpose serverless con pausa | Paga por segundo y en pausa solo almacenamiento |
| SaaS con una base por cliente | Elastic pool | Comparte vCores entre picos que no coinciden |
| Recuperación ante desastres regional | Failover group gestionado por el cliente; secundario standby si no se lee | Listeners estables y sin coste de licencia en el secundario |
| Licencias de SQL Server con SA | Azure Hybrid Benefit en vCore provisioned (no Hyperscale nuevo) | Descuento sobre la licencia |
| Necesita Agent, cross-database o compatibilidad de instancia | SQL Managed Instance | Funcionalidades de instancia |

### Datos que conviene llevar a la reunión

- **Hyperscale es el nivel recomendado por defecto** para cargas nuevas.
- **La redundancia de zona de Hyperscale se decide al crear** la base de datos.
- **Serverless no tiene reservas ni Azure Hybrid Benefit**, y la geo-replicación o la retención larga impiden la pausa.
- **Azure Hybrid Benefit no aplica a Hyperscale nuevo.**
- **El private endpoint no cierra el acceso público** por sí solo.
- **"Allow Azure services" abre el servidor a todo Azure**, no solo a la suscripción del cliente.
- **Las APIs clásicas de Defender for SQL se retiran en agosto de 2027.**
- **Microsoft recomienda failover groups gestionados por el cliente**: la conmutación gestionada por Microsoft puede tardar horas.
- **Existe una capa gratuita** de 10 bases serverless por suscripción.

## Decisiones de diseño

| Decisión | Lo que aplico | Por qué |
|---|---|---|
| Servidor | Recurso nativo `azurerm_mssql_server` | El módulo `Database/SQLServer` no inicializa |
| Autenticación | Solo Entra con un grupo como administrador; sin login ni contraseña SQL en el código | Sin secretos y con revocación centralizada |
| Identidad | Identidad de usuario por servidor (módulo del repositorio) como identidad principal | Se puede preautorizar en Graph y en Key Vault antes de crear el servidor |
| Red | Acceso público deshabilitado, private endpoints y prohibición de la regla `0.0.0.0` | Superficie mínima |
| Salida | Restringida por defecto, con FQDN permitidos explícitos | Evita exfiltración por auditoría, import/export o REST |
| Cifrado | TDE siempre; clave del cliente opcional con el rol asignado **antes** de crear el servidor | El servidor valida el acceso a la clave al crearse |
| Vulnerabilidades | Evaluación express en el servidor; protección frente a amenazas desde el plan de Defender | Sin las APIs clásicas que se retiran |
| Auditoría | Diagnostic setting `SQLSecurityAuditEvents` en master y política de auditoría con Azure Monitor | Auditoría central en Log Analytics |
| Bases de datos | Recurso nativo `azurerm_mssql_database` con validación de SKU vCore | El módulo `Database/SQLDatabase` falla sin clave del cliente y no expone lo necesario |
| Zonas | Activadas por defecto; aviso si una base única no las tiene; Hyperscale exige réplica y copias Zone o GeoZone | Reglas de la plataforma validadas en el plan |
| Copias | Redundancia `Zone` por defecto, PITR configurable, LTR con inmutabilidad opcional | Resiliencia en la región; geo-restore solo si se elige Geo o GeoZone |
| Serverless | Valida que LTR y failover groups no convivan con pausa automática | La plataforma no pausaría y se pagaría cómputo continuo |
| Licencias | `license_type` solo en provisioned GP o BC | Azure Hybrid Benefit no aplica al resto |
| Elastic pools | Módulo `Database/SQLElasticPool` del repositorio con zonas activadas | Funciona con `for_each` |
| Failover groups | Gestionado por el cliente (Manual) por defecto; misma clave TDE en ambos servidores | Recomendación de Microsoft y validación de claves al crear el grupo |
| Diagnóstico | Categorías de rendimiento en cada base y métricas Basic e InstanceAndAppAdvanced en bases y pools, a la tabla `AzureDiagnostics` | Azure SQL Database no tiene tablas específicas por recurso |

Alineación con el Well-Architected Framework:

- **Fiabilidad**: zonas, réplicas de Hyperscale, PITR y LTR, failover groups y ventana de mantenimiento.
- **Seguridad**: solo Entra, red privada, salida restringida, TDE con clave del cliente, auditoría y evaluación de vulnerabilidades.
- **Coste**: nivel y cómputo según carga, pools, serverless, Hybrid Benefit, reservas y standby.
- **Excelencia operativa**: IaC con validaciones y diagnóstico centralizado.
- **Rendimiento**: Hyperscale, réplicas de lectura y política Redirect.

## Módulo de Terraform

### Los módulos del repositorio

| Módulo | Estado |
|---|---|
| [`Database/SQLServer`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Database/SQLServer) | **No inicializa** (comprobado): declara una variable llamada `version`, nombre reservado en los bloques `module` (*The variable name "version" is reserved*). Además, las claves de almacenamiento de auditoría no son `sensitive`, `allow_azure_services` crea la regla `0.0.0.0`, usa la API clásica *Server Security Alert Policy* y no tiene private endpoints, reglas de salida ni evaluación express. Uso el recurso nativo |
| [`Database/SQLDatabase`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Database/SQLDatabase) | **Falla en cualquier `plan` sin clave del cliente** (comprobado): `transparent_data_encryption_key_automatic_rotation_enabled = false` por defecto activa el `RequiredWith` del provider sobre la clave. Solo funciona pasando `null` explícitamente. Tampoco expone réplicas de Hyperscale, ventana de mantenimiento ni `secondary_type`; `zone_redundant` es `false` por defecto; la validación de retención (7-35) impide 1-6 días; usa la política de amenazas clásica y su clave de almacenamiento no es `sensitive`. Uso el recurso nativo |
| [`Database/SQLElasticPool`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Database/SQLElasticPool) | **Lo reutilizo** (comprobado con `for_each`). Su `zone_redundant` es `false` por defecto: el root lo pasa a `true` |

También reutilizo [`PRO/common/assigned_identity`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/PRO/common/assigned_identity), [`Networking/Networking/modules/private_endpoint`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Networking/Networking/modules/private_endpoint) (subrecurso `sqlServer`) y [`Security/Seguridad/modules/monitor_diagnostic_setting`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Security/Seguridad/modules/monitor_diagnostic_setting).

Notas del provider (azurerm 4.81):

- `azuread_administrator` no tiene tipo de principal y toma el tenant del contexto: no hay que escribir el tenant.
- `minimum_tls_version` todavía acepta 1.0, 1.1 y `Disabled` en 4.x; en 5.0 solo 1.2.
- `maintenance_configuration_name` valida contra una lista fija que **no incluye todas las regiones** (por ejemplo, no tiene Spain Central). `SQL_Default` siempre es válido.
- `ledger_enabled`, `collation` y `secondary_type` fuerzan la recreación de la base de datos.
- Los secundarios que crea un failover group no quedan en el estado de Terraform.

### Estructura en el proyecto

```txt
/
├── providers.tf      # azurerm >= 4.81.0
├── sql_database.tf   # identidad, servidor, red, auditoría, pools, bases de datos y failover groups
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
      # Validado con 4.81.0 (azurerm_mssql_server con express_vulnerability_assessment_enabled,
      # azurerm_mssql_database con secondary_type y long_term_retention_policy.immutable_backups_enabled).
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

### `sql_database.tf`

```hcl
# =============================================================================
# Azure SQL Database seguro por defecto:
# servidor lógico solo con autenticación Microsoft Entra, sin acceso público (private endpoints),
# TLS 1.2, identidad de usuario como identidad principal, TDE con clave del cliente opcional,
# salida restringida, evaluación de vulnerabilidades (express) y auditoría a Log Analytics;
# bases de datos vCore redundantes en zonas, con retención corta y larga, ventana de
# mantenimiento y diagnóstico; elastic pools opcionales y failover groups gestionados por el cliente
#
# DEPENDENCY: grupos de recursos creados
# DEPENDENCY: grupo de Microsoft Entra para el administrador del servidor (no un usuario)
# DEPENDENCY: permisos de Microsoft Graph (User.Read.All, GroupMember.Read.All, Application.Read.All)
#             concedidos a la identidad del servidor por un Privileged Role Administrator, para crear
#             usuarios de Entra con CREATE USER ... FROM EXTERNAL PROVIDER
# DEPENDENCY: private endpoints: subred y zona privatelink.database.windows.net (en el hub)
# DEPENDENCY: TDE con clave del cliente: Key Vault con soft-delete y purge protection, clave RSA
#             2048/3072 versionada; acceso desde Azure SQL (servicios de confianza o private endpoint)
# DEPENDENCY: Microsoft Defender for SQL habilitado en la suscripción (protección frente a amenazas)
# DEPENDENCY: Log Analytics para auditoría y diagnóstico
# DEPENDENCY: la identidad de Terraform necesita permisos para asignar roles en el Key Vault
# =============================================================================

variable "sql_servers" {
  description = "Servidores lógicos de Azure SQL (clave = nombre del servidor, único en Azure)."
  type = map(object({
    resource_group_name = string
    location            = string

    # Administrador de Entra: un grupo; la autenticación SQL queda deshabilitada
    entra_admin = object({
      login_username = string # nombre del grupo
      object_id      = string
    })

    connection_policy                    = optional(string, "Default") # Default | Proxy | Redirect
    public_network_access_enabled        = optional(bool, false)
    firewall_rules                       = optional(map(object({ start_ip_address = string, end_ip_address = string })), {})
    outbound_network_restriction_enabled = optional(bool, true)
    outbound_firewall_fqdns              = optional(list(string), []) # cuentas de almacenamiento o servidores SQL permitidos

    private_endpoints = optional(map(object({
      subnet_id           = string
      private_dns_zone_id = string # privatelink.database.windows.net
    })), {})

    # TDE con clave del cliente (vacío = clave gestionada por el servicio)
    tde_customer_managed_key = optional(object({
      key_vault_id     = string
      key_vault_key_id = string # https://<vault>.vault.azure.net/keys/<clave>/<versión>
    }))

    express_vulnerability_assessment_enabled = optional(bool, true)
    log_analytics_workspace_id               = string # auditoría (SQLSecurityAuditEvents) y diagnóstico
    tags                                     = optional(map(string), {})
  }))
  default = {}

  validation {
    condition     = alltrue([for k, v in var.sql_servers : can(regex("^[a-z0-9][a-z0-9-]{0,61}[a-z0-9]$", k))])
    error_message = "Nombre de servidor: 2-63 caracteres, minúsculas, números y guiones, sin guion al principio ni al final."
  }
  validation {
    condition     = alltrue([for v in values(var.sql_servers) : contains(["Default", "Proxy", "Redirect"], v.connection_policy)])
    error_message = "connection_policy: Default, Proxy o Redirect."
  }
  validation {
    condition     = alltrue([for v in values(var.sql_servers) : v.public_network_access_enabled || length(v.firewall_rules) == 0])
    error_message = "Con el acceso público deshabilitado no se admiten reglas de firewall IP."
  }
  validation {
    condition = alltrue(flatten([for v in values(var.sql_servers) : [
      for r in values(v.firewall_rules) : r.start_ip_address != "0.0.0.0"
    ]]))
    error_message = "No se admite la regla 0.0.0.0 (Allow Azure services): abre el servidor a cualquier recurso de Azure, de cualquier cliente."
  }
  validation {
    condition = alltrue([for v in values(var.sql_servers) : v.tde_customer_managed_key == null ? true : can(
      regex("^https://[a-z0-9-]+\\.vault\\.azure\\.net/keys/[A-Za-z0-9-]+/[a-f0-9]{32}$", v.tde_customer_managed_key.key_vault_key_id)
    )])
    error_message = "tde_customer_managed_key.key_vault_key_id debe ser el identificador versionado de una clave de Key Vault."
  }
}

variable "sql_elastic_pools" {
  description = "Elastic pools (clave = nombre del pool)."
  type = map(object({
    server = string # clave de sql_servers
    sku = object({
      name     = string # GP_Gen5 | BC_Gen5 | HS_Gen5 | ...
      tier     = string # GeneralPurpose | BusinessCritical | Hyperscale
      family   = optional(string, "Gen5")
      capacity = number # vCores
    })
    per_database_settings = object({ min_capacity = number, max_capacity = number })
    max_size_gb           = optional(number)
    zone_redundant        = optional(bool, true)
    license_type          = optional(string, "LicenseIncluded") # BasePrice = Azure Hybrid Benefit
    maintenance_window    = optional(string, "SQL_Default")
    tags                  = optional(map(string), {})
  }))
  default = {}

  validation {
    condition     = alltrue([for v in values(var.sql_elastic_pools) : contains(["GeneralPurpose", "BusinessCritical", "Hyperscale"], v.sku.tier)])
    error_message = "Solo pools vCore: GeneralPurpose, BusinessCritical o Hyperscale."
  }
  validation {
    condition     = alltrue([for v in values(var.sql_elastic_pools) : v.per_database_settings.max_capacity <= v.sku.capacity && v.per_database_settings.min_capacity <= v.per_database_settings.max_capacity])
    error_message = "per_database_settings: min <= max <= capacidad del pool."
  }
}

variable "sql_databases" {
  description = "Bases de datos (clave = nombre de la base de datos)."
  type = map(object({
    server       = string           # clave de sql_servers
    elastic_pool = optional(string) # clave de sql_elastic_pools (null = base de datos única)

    sku_name                    = optional(string)         # GP_Gen5_2 | GP_S_Gen5_2 | BC_Gen5_4 | HS_Gen5_2 | HS_S_Gen5_2 ...
    max_size_gb                 = optional(number)         # GP/BC: tamaño facturado; Hyperscale: no aplica
    min_capacity                = optional(number)         # solo serverless
    auto_pause_delay_in_minutes = optional(number)         # solo serverless; -1 = sin pausa
    read_replica_count          = optional(number)         # Hyperscale: réplicas de alta disponibilidad (0-4)
    read_scale                  = optional(bool)           # Business Critical: réplica de lectura incluida
    license_type                = optional(string)         # BasePrice = Azure Hybrid Benefit (solo provisioned no Hyperscale)
    zone_redundant              = optional(bool, true)     # Hyperscale: solo al crear
    backup_storage_redundancy   = optional(string, "Zone") # Geo | GeoZone | Zone | Local
    collation                   = optional(string, "SQL_Latin1_General_CP1_CI_AS")
    ledger_enabled              = optional(bool, false) # solo al crear; no se puede desactivar
    maintenance_window          = optional(string, "SQL_Default")

    short_term_retention_days = optional(number, 7) # 1-35
    backup_interval_in_hours  = optional(number, 12)
    long_term_retention = optional(object({
      weekly_retention          = optional(string, "PT0S") # ISO 8601: P4W, P12M, P10Y...
      monthly_retention         = optional(string, "PT0S")
      yearly_retention          = optional(string, "PT0S")
      week_of_year              = optional(number, 1)
      immutable_backups_enabled = optional(bool, false)
    }))

    diagnostic_log_categories = optional(list(string), [
      "SQLInsights", "AutomaticTuning", "QueryStoreRuntimeStatistics", "QueryStoreWaitStatistics",
      "Errors", "DatabaseWaitStatistics", "Timeouts", "Blocks", "Deadlocks"
    ])
    tags = optional(map(string), {})
  }))
  default = {}

  validation {
    condition = alltrue([for v in values(var.sql_databases) : v.elastic_pool != null ? v.sku_name == null : can(
      regex("^(GP|BC|HS)(_S)?_(Gen5|8IM|8IH|PRMS|MOPRMS|DC|FSv2)_[0-9]+$", v.sku_name)
    )])
    error_message = "Base de datos única: sku_name vCore (GP_Gen5_2, GP_S_Gen5_2, BC_Gen5_4, HS_Gen5_2...). En un pool, sin sku_name."
  }
  validation {
    condition = alltrue([for v in values(var.sql_databases) : can(regex("_S_", v.sku_name)) ? true : (
      v.min_capacity == null && v.auto_pause_delay_in_minutes == null
    )])
    error_message = "min_capacity y auto_pause_delay_in_minutes solo aplican a SKUs serverless (GP_S_ / HS_S_)."
  }
  validation {
    condition = alltrue([for v in values(var.sql_databases) : v.license_type == null ? true : (
      v.elastic_pool == null && !can(regex("_S_", v.sku_name)) && !can(regex("^HS_", v.sku_name)) && contains(["LicenseIncluded", "BasePrice"], v.license_type)
    )])
    error_message = "license_type solo en bases provisioned GP/BC (Azure Hybrid Benefit no aplica a serverless ni a Hyperscale nuevo); en un pool se define en el pool."
  }
  validation {
    condition     = alltrue([for v in values(var.sql_databases) : contains(["Geo", "GeoZone", "Zone", "Local"], v.backup_storage_redundancy)])
    error_message = "backup_storage_redundancy: Geo, GeoZone, Zone o Local."
  }
  validation {
    condition = alltrue([for v in values(var.sql_databases) : v.elastic_pool != null ? true : (
      can(regex("^HS_", v.sku_name)) && v.zone_redundant ? (
        coalesce(v.read_replica_count, 0) >= 1 && contains(["Zone", "GeoZone"], v.backup_storage_redundancy)
      ) : true
    )])
    error_message = "Hyperscale redundante en zonas: al menos 1 réplica de alta disponibilidad y copias Zone o GeoZone."
  }
  validation {
    condition     = alltrue([for v in values(var.sql_databases) : v.short_term_retention_days >= 1 && v.short_term_retention_days <= 35 && contains([12, 24], v.backup_interval_in_hours)])
    error_message = "short_term_retention_days de 1 a 35; backup_interval_in_hours 12 o 24."
  }
  validation {
    condition     = alltrue([for v in values(var.sql_databases) : (v.auto_pause_delay_in_minutes == null ? true : v.auto_pause_delay_in_minutes == -1) || v.long_term_retention == null])
    error_message = "La retención a largo plazo impide la pausa automática: usa auto_pause_delay_in_minutes = -1."
  }
  validation {
    condition     = alltrue([for v in values(var.sql_databases) : v.elastic_pool == null || v.maintenance_window == "SQL_Default"])
    error_message = "En un elastic pool la ventana de mantenimiento es la del pool."
  }
}

variable "sql_failover_groups" {
  description = "Failover groups (clave = nombre del grupo; da nombre a los listeners <nombre>.database.windows.net)."
  type = map(object({
    server         = string       # clave de sql_servers (primario)
    partner_server = string       # clave de sql_servers en otra región
    databases      = list(string) # claves de sql_databases del servidor primario
    # Recomendado: gestionado por el cliente (Manual). Automatic solo si se tolera 1 h o más de caída
    failover_mode                      = optional(string, "Manual")
    grace_minutes                      = optional(number) # solo Automatic, 60 o más
    readonly_endpoint_failover_enabled = optional(bool, false)
    tags                               = optional(map(string), {})
  }))
  default = {}

  validation {
    condition = alltrue([for v in values(var.sql_failover_groups) : v.failover_mode == "Manual" ? v.grace_minutes == null : (
      v.failover_mode == "Automatic" && coalesce(v.grace_minutes, 0) >= 60
    )])
    error_message = "failover_mode Manual (sin grace_minutes) o Automatic con grace_minutes >= 60."
  }
}

# -----------------------------------------------------------------------------
# Identidad de usuario del servidor (Graph y TDE con clave del cliente)
# -----------------------------------------------------------------------------
module "sql_identity" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//PRO/common/assigned_identity?ref=main"
  for_each = var.sql_servers

  name                = "id-${each.key}"
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  tags                = merge(var.tags, each.value.tags)
}

# Envolver y desenvolver la DEK con la clave (antes de crear el servidor)
resource "azurerm_role_assignment" "sql_tde" {
  for_each = { for k, v in var.sql_servers : k => v if v.tde_customer_managed_key != null }

  scope                            = each.value.tde_customer_managed_key.key_vault_id
  role_definition_name             = "Key Vault Crypto Service Encryption User"
  principal_id                     = module.sql_identity[each.key].principal_id
  principal_type                   = "ServicePrincipal"
  skip_service_principal_aad_check = true
  description                      = "TDE con clave del cliente de ${each.key}"
}

# -----------------------------------------------------------------------------
# Servidor lógico (recurso nativo: el módulo Database/SQLServer no inicializa)
# -----------------------------------------------------------------------------
resource "azurerm_mssql_server" "this" {
  for_each = var.sql_servers

  name                = each.key
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  version             = "12.0"

  # Sin administrador SQL ni contraseña: solo Microsoft Entra
  azuread_administrator {
    login_username              = each.value.entra_admin.login_username
    object_id                   = each.value.entra_admin.object_id
    azuread_authentication_only = true
  }

  identity {
    type         = "UserAssigned"
    identity_ids = [module.sql_identity[each.key].id]
  }
  primary_user_assigned_identity_id            = module.sql_identity[each.key].id
  transparent_data_encryption_key_vault_key_id = try(each.value.tde_customer_managed_key.key_vault_key_id, null)

  minimum_tls_version                      = "1.2"
  connection_policy                        = each.value.connection_policy
  public_network_access_enabled            = each.value.public_network_access_enabled
  outbound_network_restriction_enabled     = each.value.outbound_network_restriction_enabled
  express_vulnerability_assessment_enabled = each.value.express_vulnerability_assessment_enabled

  tags = merge(var.tags, each.value.tags)

  depends_on = [azurerm_role_assignment.sql_tde]
}

resource "azurerm_mssql_firewall_rule" "this" {
  for_each = merge([
    for k, v in var.sql_servers : { for rk, r in v.firewall_rules : "${k}-${rk}" => merge(r, { server = k, name = rk }) }
  ]...)

  name             = each.value.name
  server_id        = azurerm_mssql_server.this[each.value.server].id
  start_ip_address = each.value.start_ip_address
  end_ip_address   = each.value.end_ip_address
}

resource "azurerm_mssql_outbound_firewall_rule" "this" {
  for_each = merge([
    for k, v in var.sql_servers : { for f in v.outbound_firewall_fqdns : "${k}-${f}" => { server = k, fqdn = f } }
  ]...)

  name      = each.value.fqdn
  server_id = azurerm_mssql_server.this[each.value.server].id
}

module "sql_private_endpoint" {
  source = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Networking/Networking/modules/private_endpoint?ref=main"
  for_each = merge([
    for k, v in var.sql_servers : {
      for pk, p in v.private_endpoints : "${k}-${pk}" => merge(p, { server = k, rg = v.resource_group_name, location = v.location })
    }
  ]...)

  private_endpoint_name          = "pe-${each.key}"
  custom_network_interface_name  = "nic-pe-${each.key}"
  resource_group_name            = each.value.rg
  location                       = each.value.location
  subnet_id                      = each.value.subnet_id
  private_connection_resource_id = azurerm_mssql_server.this[each.value.server].id
  subresource_names              = ["sqlServer"]
  private_dns_zone_ids           = [each.value.private_dns_zone_id]
  tags                           = merge(var.tags, var.sql_servers[each.value.server].tags)
}

# -----------------------------------------------------------------------------
# Auditoría del servidor a Log Analytics: diagnostic setting en master + política de auditoría
# -----------------------------------------------------------------------------
module "sql_audit_diagnostics" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Security/Seguridad/modules/monitor_diagnostic_setting?ref=main"
  for_each = var.sql_servers

  monitor_diagnostic_setting_name = "diag-audit-${each.key}"
  target_resource_id              = "${azurerm_mssql_server.this[each.key].id}/databases/master"
  log_analytics_workspace_id      = each.value.log_analytics_workspace_id
  enabled_logs                    = [{ category = "SQLSecurityAuditEvents" }]
}

resource "azurerm_mssql_server_extended_auditing_policy" "this" {
  for_each = var.sql_servers

  server_id              = azurerm_mssql_server.this[each.key].id
  enabled                = true
  log_monitoring_enabled = true

  depends_on = [module.sql_audit_diagnostics]
}

# -----------------------------------------------------------------------------
# Elastic pools (módulo Database/SQLElasticPool)
# -----------------------------------------------------------------------------
module "sql_elastic_pool" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Database/SQLElasticPool?ref=main"
  for_each = var.sql_elastic_pools

  name                           = each.key
  server_id                      = azurerm_mssql_server.this[each.value.server].id
  resource_group_name            = var.sql_servers[each.value.server].resource_group_name
  location                       = var.sql_servers[each.value.server].location
  sku                            = each.value.sku
  per_database_settings          = each.value.per_database_settings
  max_size_gb                    = each.value.max_size_gb
  zone_redundant                 = each.value.zone_redundant
  license_type                   = each.value.license_type
  maintenance_configuration_name = each.value.maintenance_window
  tags                           = merge(var.tags, each.value.tags)
}

module "sql_elastic_pool_diagnostics" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Security/Seguridad/modules/monitor_diagnostic_setting?ref=main"
  for_each = var.sql_elastic_pools

  monitor_diagnostic_setting_name = "diag-${each.key}"
  target_resource_id              = module.sql_elastic_pool[each.key].id
  log_analytics_workspace_id      = var.sql_servers[each.value.server].log_analytics_workspace_id
  enabled_metrics                 = [{ category = "Basic" }, { category = "InstanceAndAppAdvanced" }]
}

# -----------------------------------------------------------------------------
# Bases de datos (recurso nativo: el módulo Database/SQLDatabase falla sin clave del cliente
# y no expone réplicas de Hyperscale ni ventana de mantenimiento)
# -----------------------------------------------------------------------------
resource "azurerm_mssql_database" "this" {
  for_each = var.sql_databases

  name            = each.key
  server_id       = azurerm_mssql_server.this[each.value.server].id
  elastic_pool_id = each.value.elastic_pool == null ? null : module.sql_elastic_pool[each.value.elastic_pool].id
  sku_name        = each.value.elastic_pool == null ? each.value.sku_name : "ElasticPool"

  max_size_gb                    = each.value.max_size_gb
  min_capacity                   = each.value.min_capacity
  auto_pause_delay_in_minutes    = each.value.auto_pause_delay_in_minutes
  read_replica_count             = each.value.read_replica_count
  read_scale                     = each.value.read_scale
  license_type                   = each.value.license_type
  zone_redundant                 = each.value.elastic_pool == null ? each.value.zone_redundant : null
  storage_account_type           = each.value.backup_storage_redundancy
  collation                      = each.value.collation
  ledger_enabled                 = each.value.ledger_enabled
  maintenance_configuration_name = each.value.elastic_pool == null ? each.value.maintenance_window : null

  # TDE siempre activo; la clave es la del servidor (servicio o cliente)
  transparent_data_encryption_enabled = true

  short_term_retention_policy {
    retention_days           = each.value.short_term_retention_days
    backup_interval_in_hours = each.value.backup_interval_in_hours
  }

  dynamic "long_term_retention_policy" {
    for_each = each.value.long_term_retention == null ? [] : [each.value.long_term_retention]
    content {
      weekly_retention          = long_term_retention_policy.value.weekly_retention
      monthly_retention         = long_term_retention_policy.value.monthly_retention
      yearly_retention          = long_term_retention_policy.value.yearly_retention
      week_of_year              = long_term_retention_policy.value.week_of_year
      immutable_backups_enabled = long_term_retention_policy.value.immutable_backups_enabled
    }
  }

  tags = merge(var.tags, each.value.tags)
}

module "sql_database_diagnostics" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Security/Seguridad/modules/monitor_diagnostic_setting?ref=main"
  for_each = var.sql_databases

  monitor_diagnostic_setting_name = "diag-${each.key}"
  target_resource_id              = azurerm_mssql_database.this[each.key].id
  log_analytics_workspace_id      = var.sql_servers[each.value.server].log_analytics_workspace_id
  enabled_logs                    = [for c in each.value.diagnostic_log_categories : { category = c }]
  enabled_metrics                 = [{ category = "Basic" }, { category = "InstanceAndAppAdvanced" }]
}

# -----------------------------------------------------------------------------
# Failover groups: el servicio crea y siembra los secundarios en el servidor asociado
# -----------------------------------------------------------------------------
resource "azurerm_mssql_failover_group" "this" {
  for_each = var.sql_failover_groups

  name      = each.key
  server_id = azurerm_mssql_server.this[each.value.server].id
  databases = [for d in each.value.databases : azurerm_mssql_database.this[d].id]

  partner_server {
    id = azurerm_mssql_server.this[each.value.partner_server].id
  }

  read_write_endpoint_failover_policy {
    mode          = each.value.failover_mode
    grace_minutes = each.value.grace_minutes
  }
  readonly_endpoint_failover_policy_enabled = each.value.readonly_endpoint_failover_enabled

  tags = merge(var.tags, each.value.tags)

  lifecycle {
    precondition {
      condition     = var.sql_servers[each.value.server].location != var.sql_servers[each.value.partner_server].location
      error_message = "El servidor asociado debe estar en otra región."
    }
    precondition {
      condition     = alltrue([for d in each.value.databases : var.sql_databases[d].server == each.value.server])
      error_message = "Las bases de datos del grupo deben pertenecer al servidor primario."
    }
    precondition {
      condition = (
        try(var.sql_servers[each.value.server].tde_customer_managed_key.key_vault_key_id, "") ==
        try(var.sql_servers[each.value.partner_server].tde_customer_managed_key.key_vault_key_id, "")
      )
      error_message = "Con TDE de clave del cliente, primario y secundario deben usar la misma clave (Azure SQL valida el acceso a todas las claves al crear el grupo)."
    }
    precondition {
      condition     = alltrue([for d in each.value.databases : coalesce(var.sql_databases[d].auto_pause_delay_in_minutes, -1) == -1])
      error_message = "La geo-replicación impide la pausa automática: usa auto_pause_delay_in_minutes = -1."
    }
  }
}

# Avisos (no bloquean)
check "zone_redundant_databases" {
  assert {
    condition     = alltrue([for v in values(var.sql_databases) : v.elastic_pool != null || v.zone_redundant])
    error_message = "Hay bases de datos únicas sin redundancia de zona."
  }
}

output "sql_server_ids" {
  value = { for k, v in azurerm_mssql_server.this : k => v.id }
}

output "sql_server_fqdns" {
  description = "FQDN público; con private endpoint se resuelve a la IP privada desde la red."
  value       = { for k, v in azurerm_mssql_server.this : k => v.fully_qualified_domain_name }
}

output "sql_server_identities" {
  description = "Identidad principal de cada servidor (para los permisos de Microsoft Graph)."
  value       = { for k, v in module.sql_identity : k => { id = v.id, principal_id = v.principal_id } }
}

output "sql_database_ids" {
  value = { for k, v in azurerm_mssql_database.this : k => v.id }
}

output "sql_failover_group_listeners" {
  value = {
    for k, v in azurerm_mssql_failover_group.this : k => {
      read_write = "${k}.database.windows.net"
      read_only  = "${k}.secondary.database.windows.net"
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

sql_servers = {
  "sql-workload-pro-01" = {
    resource_group_name = "<rg-workload-pro>"
    location            = "<región-primaria>"

    entra_admin = {
      login_username = "<grupo sql-admins-pro>"
      object_id      = "<objectId del grupo>"
    }

    # Redirect: menor latencia; exige abrir 1433-65535 hacia la subred del private endpoint
    connection_policy = "Redirect"

    private_endpoints = {
      app = {
        subnet_id           = "<resourceId snet-pe-workload-pro>"
        private_dns_zone_id = "<resourceId privatelink.database.windows.net (hub)>"
      }
    }

    tde_customer_managed_key = {
      key_vault_id     = "<resourceId kv-workload-pro>"
      key_vault_key_id = "<https://kv-workload-pro.vault.azure.net/keys/tde-sql/versión>"
    }

    log_analytics_workspace_id = "<resourceId log-platform-pro>"
  }

  # Servidor secundario del failover group, en otra región
  "sql-workload-pro-dr-01" = {
    resource_group_name = "<rg-workload-pro-dr>"
    location            = "<región-secundaria>"

    entra_admin = {
      login_username = "<grupo sql-admins-pro>"
      object_id      = "<objectId del grupo>"
    }
    connection_policy = "Redirect"

    private_endpoints = {
      app = {
        subnet_id           = "<resourceId snet-pe-workload-pro-dr>"
        private_dns_zone_id = "<resourceId privatelink.database.windows.net (hub)>"
      }
    }

    # La misma clave del mismo Key Vault que el primario: ambos servidores deben poder abrirla
    tde_customer_managed_key = {
      key_vault_id     = "<resourceId kv-workload-pro>"
      key_vault_key_id = "<https://kv-workload-pro.vault.azure.net/keys/tde-sql/versión>"
    }

    log_analytics_workspace_id = "<resourceId log-platform-pro>"
  }
}

sql_elastic_pools = {
  "sqlep-workload-tenants-pro" = {
    server = "sql-workload-pro-01"
    sku = {
      name     = "GP_Gen5"
      tier     = "GeneralPurpose"
      capacity = 4
    }
    per_database_settings = {
      min_capacity = 0
      max_capacity = 2
    }
    max_size_gb = 256
  }
}

sql_databases = {
  # Base de datos principal: Hyperscale, 1 réplica de alta disponibilidad para la redundancia de zona
  "sqldb-workload-app" = {
    server                    = "sql-workload-pro-01"
    sku_name                  = "HS_Gen5_4"
    read_replica_count        = 1
    backup_storage_redundancy = "Zone" # GeoZone si se quiere geo-restore a la región emparejada
    short_term_retention_days = 35
    long_term_retention = {
      weekly_retention  = "P5W"
      monthly_retention = "P12M"
      yearly_retention  = "P10Y"
      week_of_year      = 1
    }
  }

  # Bases de datos de clientes en el elastic pool
  "sqldb-workload-tenant-a" = {
    server       = "sql-workload-pro-01"
    elastic_pool = "sqlep-workload-tenants-pro"
  }
  "sqldb-workload-tenant-b" = {
    server       = "sql-workload-pro-01"
    elastic_pool = "sqlep-workload-tenants-pro"
  }
}

sql_failover_groups = {
  "fog-workload-pro" = {
    server         = "sql-workload-pro-01"
    partner_server = "sql-workload-pro-dr-01"
    databases      = ["sqldb-workload-app"]
  }
}
```

### Despliegue y comprobación

Antes del primer despliegue, un Privileged Role Administrator concede a la identidad del servidor los permisos de Microsoft Graph (la identidad sale en el output `sql_server_identities`).

```powershell
terraform init
terraform plan -var-file="env/pro.tfvars" -out="pro.tfplan"
terraform apply "pro.tfplan"

# Permisos de Microsoft Graph para la identidad del servidor (Privileged Role Administrator)
Connect-MgGraph -Scopes "AppRoleAssignment.ReadWrite.All", "Application.Read.All"
$graph = Get-MgServicePrincipal -Filter "DisplayName eq 'Microsoft Graph'"
$msi   = Get-MgServicePrincipal -Filter "DisplayName eq 'id-sql-workload-pro-01'"
foreach ($role in "User.Read.All", "GroupMember.Read.All", "Application.Read.All") {
    $appRole = $graph.AppRoles | Where-Object { $_.Value -eq $role }
    New-MgServicePrincipalAppRoleAssignment -ServicePrincipalId $msi.Id -PrincipalId $msi.Id `
        -ResourceId $graph.Id -AppRoleId $appRole.Id
}

# Configuración del servidor
$server = Get-AzSqlServer -ResourceGroupName "<rg-workload-pro>" -ServerName "sql-workload-pro-01"
$server | Select-Object ServerName, PublicNetworkAccess, MinimalTlsVersion, RestrictOutboundNetworkAccess
Get-AzSqlServerActiveDirectoryOnlyAuthentication -ServerName "sql-workload-pro-01" -ResourceGroupName "<rg-workload-pro>"
Get-AzSqlServerTransparentDataEncryptionProtector -ServerName "sql-workload-pro-01" -ResourceGroupName "<rg-workload-pro>"

# Bases de datos: nivel, zonas y redundancia de copias
Get-AzSqlDatabase -ResourceGroupName "<rg-workload-pro>" -ServerName "sql-workload-pro-01" |
    Select-Object DatabaseName, SkuName, ZoneRedundant, HighAvailabilityReplicaCount, CurrentBackupStorageRedundancy

# Resolución privada desde una VM de la red (debe devolver una IP privada)
Resolve-DnsName "sql-workload-pro-01.database.windows.net"

# Failover group
Get-AzSqlDatabaseFailoverGroup -ResourceGroupName "<rg-workload-pro>" -ServerName "sql-workload-pro-01"
```

Desde una sesión con Entra, la creación de usuarios contenidos:

```sql
CREATE USER [id-app-workload-pro] FROM EXTERNAL PROVIDER;
ALTER ROLE db_datareader ADD MEMBER [id-app-workload-pro];
ALTER ROLE db_datawriter ADD MEMBER [id-app-workload-pro];

SELECT SERVERPROPERTY('IsExternalAuthenticationOnly'); -- 1 = solo Entra
```

Consultas en Log Analytics (Azure SQL Database solo envía sus categorías a la tabla `AzureDiagnostics`):

```kusto
AzureDiagnostics
| where Category == "SQLSecurityAuditEvents"
| where TimeGenerated > ago(1d)
| summarize count() by action_name_s, succeeded_s

AzureDiagnostics
| where Category == "Deadlocks"
| where TimeGenerated > ago(7d)
```

### Equivalente en Bicep

Una plantilla por servidor. El servidor secundario del failover group se despliega primero (sin `failoverGroups`) y su ID se pasa al primario. Para asignar el rol sobre el Key Vault de otro grupo de recursos, `sql.bicep` usa `role-on-resource.bicep`, el mismo de las fichas de AKS, Container Instances y Container Apps.

`sql.bicep`:

```bicep
// =============================================================================
// Servidor lógico de Azure SQL seguro por defecto: solo Microsoft Entra, sin acceso público
// (private endpoints), TLS 1.2, identidad de usuario, TDE con clave del cliente opcional, salida
// restringida, evaluación de vulnerabilidades express y auditoría a Log Analytics; elastic pools,
// bases de datos vCore con retención y diagnóstico, y failover groups gestionados por el cliente
// DEPENDENCY: grupo de Entra para el administrador; permisos de Microsoft Graph para la identidad
// DEPENDENCY: subred de private endpoints y zona privatelink.database.windows.net
// DEPENDENCY: Key Vault con soft-delete y purge protection (si se usa clave del cliente)
// DEPENDENCY: el servidor asociado de un failover group se despliega antes (con esta misma plantilla)
// DEPENDENCY: role-on-resource.bicep en la misma carpeta
// =============================================================================
@minLength(2)
@maxLength(63)
param name string
param location string = resourceGroup().location

@description('Grupo de Microsoft Entra administrador del servidor')
param entraAdmin object // { loginName, objectId }

@allowed(['Default', 'Proxy', 'Redirect'])
param connectionPolicy string = 'Default'
param outboundNetworkRestriction bool = true
param outboundFirewallFqdns array = []

@description('[{ name, subnetId, privateDnsZoneId }]')
param privateEndpoints array = []

@description('TDE con clave del cliente: { keyVaultId, keyVaultKeyId (versionado) }; vacío = clave del servicio')
param tdeCustomerManagedKey object = {}

param expressVulnerabilityAssessment bool = true
param logAnalyticsWorkspaceId string

@description('[{ name, skuName, tier, capacity, minPerDb, maxPerDb, maxSizeGb?, zoneRedundant?, licenseType?, maintenanceWindow? }]')
param elasticPools array = []

@description('[{ name, skuName? | elasticPool?, maxSizeGb?, minCapacity?, autoPauseDelay?, haReplicas?, readScale?, licenseType?, zoneRedundant?, backupStorageRedundancy?, ledger?, maintenanceWindow?, retentionDays?, ltr? }]')
param databases array = []

@description('[{ name, partnerServerId, databases: [nombres], failoverMode? (Manual), graceMinutes?, readOnlyFailover? }]')
param failoverGroups array = []

param tags object = {}

var useCmk = !empty(tdeCustomerManagedKey)
var diagnosticLogCategories = [
  'SQLInsights'
  'AutomaticTuning'
  'QueryStoreRuntimeStatistics'
  'QueryStoreWaitStatistics'
  'Errors'
  'DatabaseWaitStatistics'
  'Timeouts'
  'Blocks'
  'Deadlocks'
]

resource identity 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = {
  name: 'id-${name}'
  location: location
  tags: tags
}

// Key Vault Crypto Service Encryption User antes de crear el servidor
module tdeRole 'role-on-resource.bicep' = if (useCmk) {
  name: '${take(name, 45)}-tde-role'
  scope: resourceGroup(
    split(tdeCustomerManagedKey.?keyVaultId ?? '/s/x/r/x', '/')[2],
    split(tdeCustomerManagedKey.?keyVaultId ?? '/s/x/r/x', '/')[4]
  )
  params: {
    resourceId: tdeCustomerManagedKey.keyVaultId
    roleDefinitionId: 'e147488a-f6f5-4113-8e2d-b22465e65bf6'
    principalId: identity.properties.principalId
    description: 'TDE con clave del cliente de ${name}'
  }
}

resource server 'Microsoft.Sql/servers@2023-08-01' = {
  name: name
  location: location
  tags: tags
  identity: {
    type: 'UserAssigned'
    userAssignedIdentities: {
      '${identity.id}': {}
    }
  }
  properties: {
    version: '12.0'
    minimalTlsVersion: '1.2'
    publicNetworkAccess: 'Disabled'
    restrictOutboundNetworkAccess: outboundNetworkRestriction ? 'Enabled' : 'Disabled'
    primaryUserAssignedIdentityId: identity.id
    keyId: useCmk ? tdeCustomerManagedKey.keyVaultKeyId : null
    administrators: {
      administratorType: 'ActiveDirectory'
      principalType: 'Group'
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

resource connection 'Microsoft.Sql/servers/connectionPolicies@2023-08-01' = {
  parent: server
  name: 'default'
  properties: {
    connectionType: connectionPolicy
  }
}

resource outboundRules 'Microsoft.Sql/servers/outboundFirewallRules@2023-08-01' = [
  for fqdn in outboundFirewallFqdns: {
    parent: server
    name: fqdn
  }
]

resource vulnerabilityAssessment 'Microsoft.Sql/servers/sqlVulnerabilityAssessments@2023-08-01' = if (expressVulnerabilityAssessment) {
  parent: server
  name: 'default'
  properties: {
    state: 'Enabled'
  }
}

resource privateEndpointsRes 'Microsoft.Network/privateEndpoints@2024-05-01' = [
  for pe in privateEndpoints: {
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
          name: 'sqlServer'
          properties: {
            privateLinkServiceId: server.id
            groupIds: [
              'sqlServer'
            ]
          }
        }
      ]
    }
  }
]

resource privateDnsGroups 'Microsoft.Network/privateEndpoints/privateDnsZoneGroups@2024-05-01' = [
  for (pe, i) in privateEndpoints: {
    parent: privateEndpointsRes[i]
    name: 'default'
    properties: {
      privateDnsZoneConfigs: [
        {
          name: 'sql'
          properties: {
            privateDnsZoneId: pe.privateDnsZoneId
          }
        }
      ]
    }
  }
]

// Auditoría del servidor a Log Analytics: diagnostic setting en master + política de auditoría
resource master 'Microsoft.Sql/servers/databases@2023-08-01' existing = {
  parent: server
  name: 'master'
}

resource auditDiagnostics 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = {
  name: 'diag-audit-${name}'
  scope: master
  properties: {
    workspaceId: logAnalyticsWorkspaceId
    logs: [
      {
        category: 'SQLSecurityAuditEvents'
        enabled: true
      }
    ]
  }
}

resource auditing 'Microsoft.Sql/servers/auditingSettings@2023-08-01' = {
  parent: server
  name: 'default'
  properties: {
    state: 'Enabled'
    isAzureMonitorTargetEnabled: true
  }
  dependsOn: [
    auditDiagnostics
  ]
}

resource pools 'Microsoft.Sql/servers/elasticPools@2023-08-01' = [
  for p in elasticPools: {
    parent: server
    name: p.name
    location: location
    tags: tags
    sku: {
      name: p.skuName
      tier: p.tier
      capacity: p.capacity
    }
    properties: {
      perDatabaseSettings: {
        minCapacity: p.minPerDb
        maxCapacity: p.maxPerDb
      }
      maxSizeBytes: contains(p, 'maxSizeGb') ? p.maxSizeGb * 1073741824 : null
      zoneRedundant: p.?zoneRedundant ?? true
      licenseType: p.?licenseType ?? 'LicenseIncluded'
      maintenanceConfigurationId: subscriptionResourceId(
        'Microsoft.Maintenance/publicMaintenanceConfigurations',
        p.?maintenanceWindow ?? 'SQL_Default'
      )
    }
  }
]

resource poolDiagnostics 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = [
  for (p, i) in elasticPools: {
    name: 'diag-${p.name}'
    scope: pools[i]
    properties: {
      workspaceId: logAnalyticsWorkspaceId
      metrics: [
        {
          category: 'Basic'
          enabled: true
        }
        {
          category: 'InstanceAndAppAdvanced'
          enabled: true
        }
      ]
    }
  }
]

resource dbs 'Microsoft.Sql/servers/databases@2023-08-01' = [
  for d in databases: {
    parent: server
    name: d.name
    location: location
    tags: tags
    sku: contains(d, 'elasticPool')
      ? {
          name: 'ElasticPool'
        }
      : {
          name: d.skuName
        }
    properties: {
      elasticPoolId: contains(d, 'elasticPool')
        ? resourceId('Microsoft.Sql/servers/elasticPools', name, d.elasticPool)
        : null
      maxSizeBytes: contains(d, 'maxSizeGb') ? d.maxSizeGb * 1073741824 : null
      minCapacity: d.?minCapacity
      autoPauseDelay: d.?autoPauseDelay
      highAvailabilityReplicaCount: d.?haReplicas
      readScale: (d.?readScale ?? false) ? 'Enabled' : null
      licenseType: d.?licenseType
      zoneRedundant: contains(d, 'elasticPool') ? null : (d.?zoneRedundant ?? true)
      requestedBackupStorageRedundancy: d.?backupStorageRedundancy ?? 'Zone'
      collation: d.?collation ?? 'SQL_Latin1_General_CP1_CI_AS'
      isLedgerOn: d.?ledger ?? false
      maintenanceConfigurationId: contains(d, 'elasticPool')
        ? null
        : subscriptionResourceId(
            'Microsoft.Maintenance/publicMaintenanceConfigurations',
            d.?maintenanceWindow ?? 'SQL_Default'
          )
    }
    dependsOn: [
      pools
    ]
  }
]

resource shortTermRetention 'Microsoft.Sql/servers/databases/backupShortTermRetentionPolicies@2023-08-01' = [
  for (d, i) in databases: {
    parent: dbs[i]
    name: 'default'
    properties: {
      retentionDays: d.?retentionDays ?? 7
      diffBackupIntervalInHours: 12
    }
  }
]

resource longTermRetention 'Microsoft.Sql/servers/databases/backupLongTermRetentionPolicies@2023-08-01' = [
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
      logs: map(diagnosticLogCategories, c => { category: c, enabled: true })
      metrics: [
        {
          category: 'Basic'
          enabled: true
        }
        {
          category: 'InstanceAndAppAdvanced'
          enabled: true
        }
      ]
    }
  }
]

resource fogs 'Microsoft.Sql/servers/failoverGroups@2023-08-01' = [
  for f in failoverGroups: {
    parent: server
    name: f.name
    tags: tags
    properties: {
      partnerServers: [
        {
          id: f.partnerServerId
        }
      ]
      databases: map(f.databases, db => resourceId('Microsoft.Sql/servers/databases', name, db))
      readWriteEndpoint: {
        failoverPolicy: f.?failoverMode ?? 'Manual'
        failoverWithDataLossGracePeriodMinutes: (f.?failoverMode ?? 'Manual') == 'Automatic' ? f.graceMinutes : null
      }
      readOnlyEndpoint: {
        failoverPolicy: (f.?readOnlyFailover ?? false) ? 'Enabled' : 'Disabled'
      }
    }
    dependsOn: [
      dbs
    ]
  }
]

output serverId string = server.id
output fullyQualifiedDomainName string = server.properties.fullyQualifiedDomainName
output identityPrincipalId string = identity.properties.principalId
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

`sql-workload-pro-01.bicepparam`:

```bicep
using 'sql.bicep'

// Desplegar antes sql-workload-pro-dr-01 (misma plantilla, sin failoverGroups) en la región secundaria
param name = 'sql-workload-pro-01'

param entraAdmin = {
  loginName: '<grupo sql-admins-pro>'
  objectId: '<objectId del grupo>'
}

// Redirect: menor latencia; exige abrir 1433-65535 hacia la subred del private endpoint
param connectionPolicy = 'Redirect'

param privateEndpoints = [
  {
    name: 'app'
    subnetId: '<resourceId snet-pe-workload-pro>'
    privateDnsZoneId: '<resourceId privatelink.database.windows.net (hub)>'
  }
]

// La misma clave en el servidor secundario
param tdeCustomerManagedKey = {
  keyVaultId: '<resourceId kv-workload-pro>'
  keyVaultKeyId: '<https://kv-workload-pro.vault.azure.net/keys/tde-sql/versión>'
}

param logAnalyticsWorkspaceId = '<resourceId log-platform-pro>'

param elasticPools = [
  {
    name: 'sqlep-workload-tenants-pro'
    skuName: 'GP_Gen5'
    tier: 'GeneralPurpose'
    capacity: 4
    minPerDb: 0
    maxPerDb: 2
    maxSizeGb: 256
  }
]

param databases = [
  {
    name: 'sqldb-workload-app'
    skuName: 'HS_Gen5_4'
    haReplicas: 1
    backupStorageRedundancy: 'Zone'
    retentionDays: 35
    ltr: {
      weekly: 'P5W'
      monthly: 'P12M'
      yearly: 'P10Y'
      weekOfYear: 1
    }
  }
  {
    name: 'sqldb-workload-tenant-a'
    elasticPool: 'sqlep-workload-tenants-pro'
  }
  {
    name: 'sqldb-workload-tenant-b'
    elasticPool: 'sqlep-workload-tenants-pro'
  }
]

param failoverGroups = [
  {
    name: 'fog-workload-pro'
    partnerServerId: '<resourceId sql-workload-pro-dr-01>'
    databases: [
      'sqldb-workload-app'
    ]
  }
]
```

Despliegue:

```powershell
New-AzResourceGroupDeployment -ResourceGroupName "<rg-workload-pro>" `
    -TemplateParameterFile "sql-workload-pro-01.bicepparam" -Name "sql-workload-pro-01"
```

## Errores típicos

| Síntoma | Causa | Solución |
|---|---|---|
| *The variable name "version" is reserved* al usar `Database/SQLServer` | Variable con nombre reservado | Recurso nativo |
| *all of `transparent_data_encryption_key_automatic_rotation_enabled,transparent_data_encryption_key_vault_key_id` must be specified* con `Database/SQLDatabase` | Valor por defecto `false` sin clave | Recurso nativo (o pasar `null`) |
| Error 47073 al conectar | Acceso público deshabilitado y el cliente sale por el endpoint público | Conectar por el private endpoint y revisar el DNS |
| Error 42101 al crear reglas de firewall | Acceso público deshabilitado | No usar reglas IP; el root lo valida |
| Conecta desde la VNet pero no desde on-premises | Política Redirect y puertos 1433-65535 cerrados en el firewall local | Abrir el rango o usar `Proxy` |
| Después de crear el private endpoint siguen entrando conexiones públicas | El private endpoint no deshabilita el acceso público | `public_network_access_enabled = false` |
| `CREATE USER ... FROM EXTERNAL PROVIDER` falla | La identidad del servidor no tiene permisos de Graph | Conceder `User.Read.All`, `GroupMember.Read.All` y `Application.Read.All` |
| No se puede crear el servidor con clave del cliente | Key Vault sin soft-delete o purge protection, sin acceso para la identidad, o el firewall del vault no deja pasar a Azure SQL | Requisitos del Key Vault y rol asignado antes |
| Bases de datos inaccesibles | Se ha borrado la identidad o revocado su acceso a la clave | Restaurar acceso; no borrar la identidad principal |
| El failover group no se crea con clave del cliente | Algún servidor no accede a todas las claves | Misma clave en ambos servidores (validado) |
| No se puede activar la redundancia de zona en Hyperscale | Solo al crear, con 1 réplica de alta disponibilidad y copias Zone o GeoZone | Copia, restauración o geo-réplica |
| Serverless no se pausa y la factura es alta | Conexiones abiertas, LTR, geo-replicación o alias DNS | Cerrar conexiones o pasar a provisioned |
| No hay opción de Azure Hybrid Benefit | Serverless, DTU o Hyperscale nuevo | Solo vCore provisioned GP o BC |
| La auditoría dejó de llegar a Log Analytics | Alguien borró el diagnostic setting `SQLSecurityAuditEvents` | Alerta sobre su borrado y redeploy |
| La ventana de mantenimiento se rechaza en el plan | La lista del provider no incluye la región | `SQL_Default` o desplegarla con Bicep |
| Alta latencia de geo-replicación en pools | Pools de 8 vCores o menos con más de 250 bases geo-replicadas | Escalar el pool o reducir bases replicadas |
| La regla `0.0.0.0` aparece en el servidor | Se activó "Allow Azure services" | Eliminarla; el root la rechaza |
