---
title: "SQL Server en VM"
indice: database
resumen: "Control total del motor cuando el PaaS no encaja."
estado: documentado   # proximamente | en-curso | documentado
orden: 3
last_review: 2026-10-27
fuentes:
  - titulo: "What is SQL Server on Azure Windows Virtual Machines?"
    url: https://learn.microsoft.com/azure/azure-sql/virtual-machines/windows/sql-server-on-azure-vm-iaas-what-is-overview
  - titulo: "What is Azure SQL?"
    url: https://learn.microsoft.com/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview
  - titulo: "Azure SQL decision tree"
    url: https://learn.microsoft.com/azure/azure-sql/azure-sql-decision-tree
  - titulo: "Migration overview: SQL Server to Azure SQL Managed Instance"
    url: https://learn.microsoft.com/data-migration/sql-server/managed-instance/overview
  - titulo: "Checklist: Best practices for SQL Server on Azure VMs"
    url: https://learn.microsoft.com/azure/azure-sql/virtual-machines/windows/performance-guidelines-best-practices-checklist
  - titulo: "VM size: Performance best practices for SQL Server on Azure VMs"
    url: https://learn.microsoft.com/azure/azure-sql/virtual-machines/windows/performance-guidelines-best-practices-vm-size
  - titulo: "Storage: Performance best practices for SQL Server on Azure VMs"
    url: https://learn.microsoft.com/azure/azure-sql/virtual-machines/windows/performance-guidelines-best-practices-storage
  - titulo: "Configure storage for SQL Server on Azure VMs"
    url: https://learn.microsoft.com/azure/azure-sql/virtual-machines/windows/storage-configuration
  - titulo: "Deploy SQL Server on Azure VMs with Premium SSD v2 storage (preview)"
    url: https://learn.microsoft.com/azure/azure-sql/virtual-machines/windows/storage-configuration-premium-ssd-v2
  - titulo: "Azure managed disk types"
    url: https://learn.microsoft.com/azure/virtual-machines/disks-types
  - titulo: "Automate management with the Windows SQL Server IaaS Agent extension"
    url: https://learn.microsoft.com/azure/azure-sql/virtual-machines/windows/sql-server-iaas-agent-extension-automate-management
  - titulo: "Register a SQL Server VM with the SQL IaaS Agent extension"
    url: https://learn.microsoft.com/azure/azure-sql/virtual-machines/windows/sql-agent-extension-manually-register-single-vm
  - titulo: "Change the license model for a SQL virtual machine in Azure"
    url: https://learn.microsoft.com/azure/azure-sql/virtual-machines/windows/licensing-model-azure-hybrid-benefit-ahb-change
  - titulo: "Pricing guidance for SQL Server on Azure VMs"
    url: https://learn.microsoft.com/azure/azure-sql/virtual-machines/windows/pricing-guidance
  - titulo: "Security considerations for SQL Server on Azure Virtual Machines"
    url: https://learn.microsoft.com/azure/azure-sql/virtual-machines/windows/security-considerations-best-practices
  - titulo: "Provision SQL Server on Azure VM (Azure portal)"
    url: https://learn.microsoft.com/azure/azure-sql/virtual-machines/windows/create-sql-vm-portal
  - titulo: "Connect to a SQL Server virtual machine on Azure"
    url: https://learn.microsoft.com/azure/azure-sql/virtual-machines/windows/ways-to-connect-to-sql
  - titulo: "Enable Microsoft Entra authentication for SQL Server on Azure VMs"
    url: https://learn.microsoft.com/azure/azure-sql/virtual-machines/windows/configure-azure-ad-authentication-for-sql-vm
  - titulo: "Enable Defender for SQL Servers on Machines"
    url: https://learn.microsoft.com/azure/defender-for-cloud/defender-for-sql-usage
  - titulo: "Backup and restore for SQL Server on Azure VMs"
    url: https://learn.microsoft.com/azure/azure-sql/virtual-machines/windows/backup-restore
  - titulo: "Azure Update Manager for SQL Server on Azure VMs"
    url: https://learn.microsoft.com/azure/azure-sql/virtual-machines/azure-update-manager-sql-vm
  - titulo: "SQL best practices assessment for SQL Server on Azure VMs"
    url: https://learn.microsoft.com/azure/azure-sql/virtual-machines/windows/sql-assessment-for-sql-vm
  - titulo: "Business continuity and HADR for SQL Server on Azure VMs"
    url: https://learn.microsoft.com/azure/azure-sql/virtual-machines/windows/business-continuity-high-availability-disaster-recovery-hadr-overview
  - titulo: "Always On availability group on SQL Server on Azure VMs"
    url: https://learn.microsoft.com/azure/azure-sql/virtual-machines/windows/availability-group-overview
  - titulo: "Quickstart: Create SQL Server VM using Bicep"
    url: https://learn.microsoft.com/azure/azure-sql/virtual-machines/windows/create-sql-vm-bicep
  - titulo: "Microsoft.SqlVirtualMachine sqlVirtualMachines (plantillas ARM/Bicep)"
    url: https://learn.microsoft.com/azure/templates/microsoft.sqlvirtualmachine/sqlvirtualmachines
  - titulo: "azurerm_mssql_virtual_machine"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/mssql_virtual_machine
  - titulo: "Módulo Terraform Compute/Compute/modules/windows_virtual_machine"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Compute/Compute/modules/windows_virtual_machine
  - titulo: "Módulo Terraform Compute/Compute/modules/managed_disk"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Compute/Compute/modules/managed_disk
---

**SQL Server en Azure Virtual Machines** es SQL Server completo sobre una VM de Azure: tú eliges la versión, la edición y el sistema operativo, y tienes acceso al servidor y a su sistema de archivos. Es IaaS: el parcheo, las copias y la alta disponibilidad son responsabilidad tuya, con ayuda de la **extensión SQL IaaS Agent**. Es la opción cuando [SQL Managed Instance](/recursos/database/sql-managed-instance/) o [Azure SQL Database](/recursos/database/azure-sql-database/) no encajan. La VM en sí sigue el patrón de la [ficha de Virtual Machines](/recursos/compute/virtual-machines/).

## Qué es y cuándo usarlo

### Cuándo elegir una VM y no PaaS

| Necesidad | Destino |
|---|---|
| Acceso al sistema operativo o a los archivos (agentes de terceros instalados junto a SQL Server) | **SQL Server en VM** |
| Una versión concreta de SQL Server que no se actualice sola | **SQL Server en VM** |
| FileStream o FileTable, PolyBase o transacciones entre instancias | **SQL Server en VM** |
| Instancias con muchas bases y hasta 256 TB de almacenamiento | **SQL Server en VM** |
| SQL Agent, CLR, replicación transaccional, consultas entre bases o linked servers sin gestionar el SO | SQL Managed Instance |
| Aplicación nueva o sin dependencias de instancia | Azure SQL Database |

El precio de la libertad: **la alta disponibilidad la montas tú** y cambiar CPU o almacenamiento implica parada.

### Imágenes y ediciones

Las imágenes de Marketplace las publica `MicrosoftSQLServer`. Las ofertas tienen la forma `sql2022-ws2022` y los SKU, `enterprise-gen2`, `standard-gen2`, `web-gen2` o `SQLDEV-gen2`. SQL Server 2025 añade las ediciones `entdev-gen2` y `stddev-gen2`.

| Edición | Uso | Licencia de SQL Server |
|---|---|---|
| Developer (Enterprise o Standard en 2025) | Desarrollo y pruebas; **nunca producción** | Gratis |
| Express | Producción ligera: hasta 4 núcleos, menos de 1 GB de memoria y 50 GB por base | Gratis |
| Web | Sitios web pequeños | De pago |
| Standard | Cargas pequeñas y medianas | De pago o Hybrid Benefit |
| Enterprise | Cargas grandes o críticas | De pago o Hybrid Benefit |

- Microsoft mantiene **una sola imagen** por combinación de SO, versión y edición, y la renueva con el tiempo.
- Las imágenes se publican en **RTM y no se actualizan**: hay que aplicar los cumulative updates tras desplegar.
- Las imágenes BYOL ya no existen. Se despliega Standard o Enterprise y se activa Azure Hybrid Benefit.
- SQL Server 2012 y 2014 ya no están en Marketplace.

### La extensión SQL IaaS Agent

Registrar la VM en la extensión crea el recurso **SQL virtual machine** (`Microsoft.SqlVirtualMachine`), separado de la VM. Es gratis. Las imágenes de Marketplace desplegadas desde el portal se registran solas; las instalaciones propias de SQL Server 2016 o posterior se registran automáticamente cuando las detecta el CEIP.

| Sin agente (registro básico) | Con agente (se instala al activar la función) |
|---|---|
| Gestión en el portal | Configuración de almacenamiento y de tempdb |
| Cambio de licencia (PAYG, AHUB, DR) sin parada | Microsoft Entra ID |
| Cambio de versión o edición en los metadatos | SQL best practices assessment |
| Extended Security Updates | Automated Backup y Automated Patching |
| | Recomendaciones de Defender for Cloud e I/O Analysis |

- Desde marzo de 2023 no hay modos de gestión: el agente tiene **mínimo privilegio**, con un rol de SQL Server por función activada.
- Soporta una instancia por defecto o una única instancia con nombre. **En una FCI** el registro es limitado: sin backup, patching ni Entra.
- Necesita **TCP/IP habilitado** y solo existe en algunas regiones (consulta abajo).
- Quitar el recurso SQL virtual machine devuelve la licencia a la de la imagen.

### Tamaño de VM

| Recomendación | Detalle |
|---|---|
| Mínimo | 4 vCores. Desarrollo con serie D o B y crecer después |
| Relación memoria/vCore | 8:1 en producción; 4:1 solo para entornos pequeños; 16:1 o más en data warehouse |
| Punto de partida | **Ebdsv5**: mejor precio/rendimiento, con disco temporal para tempdb y soporte de Premium SSD v2 |
| Críticos y data warehouse | Mbdsv3, Msv3/Mdsv3 y el resto de la serie M |
| Ahorro en licencias | vCPUs restringidas (p. ej. M64-32ms licencia 32 vCores) y personalización de vCores |
| No soportado | Virtual Machine Scale Sets, más de 64 vCores por nodo NUMA sin desactivar SMT y discos con sector de 8 KB |

Atención con los tamaños con disco efímero sin inicializar, como **FXmdsv2**: SQL Server instalado a mano no arranca si tempdb está en el disco temporal.

### Almacenamiento

Datos, log y tempdb van en **unidades separadas**. Nada de SQL en `C:`.

| Disco | Tipo | Caching |
|---|---|---|
| Datos | Premium SSD P30/P40 o Premium SSD v2 | **ReadOnly** con Premium SSD |
| Log | Premium SSD P30 o superior, Premium SSD v2 o Ultra Disk (submilisegundo) | **None** |
| tempdb | Disco temporal `D:` | — |
| SO | Premium SSD | ReadWrite (el valor por defecto, no tocarlo) |

- **Nunca ReadWrite** en discos con datos o log: rompe la durabilidad de las transacciones.
- Cambiar el caching **desconecta y reconecta el disco**: para el servicio de SQL Server antes.
- Los discos de 4 TiB o más (P50+) no admiten caching.
- **Premium SSD v2** no admite caching, ajusta IOPS y throughput sin cambiar el tamaño y, en la mayoría de regiones con zonas, solo se conecta a VMs zonales.
- Con Premium SSD, la extensión crea pools de Storage Spaces con **stripe de 64 KB** y unidad de asignación de 64 KB. El número de columnas se fija al crear el pool: añadir discos después da capacidad, no rendimiento.
- La configuración automática de almacenamiento solo funciona con **imagen de Marketplace y Premium SSD**. Con Premium SSD v2 desde el portal (preview) solo vale Ebdsv5 o Ebsv5.
- Standard HDD o SSD solo en desarrollo y pruebas. Write Accelerator (serie M) para el log, nunca para datos.
- Si el disco temporal no da para tempdb: VM más grande o tempdb en un disco de datos con ReadOnly.

### Seguridad

| Control | Recomendación |
|---|---|
| Conectividad | **Private** (solo la VNet) o Local; nunca Public. NSG con el puerto de SQL abierto solo desde las subredes de aplicación |
| Acceso a la VM | Sin puertos de administración abiertos: Bastion o JIT |
| Autenticación | Windows por defecto: `sa` queda deshabilitado. Con SQL Server 2022 o posterior, **Microsoft Entra ID** |
| Entra | Identidad gestionada con **Directory Readers** o los permisos de Graph `User.Read.All`, `GroupMember.Read.All` y `Application.Read.All`. Salida 80 y 443 hacia `AzureActiveDirectory`. **No se puede desactivar** una vez activado ni se usa con FCI |
| Cifrado | Cifrado en el host; Azure Disk Encryption si hay que cifrar también el disco temporal; VMs confidenciales para datos en uso |
| Defender | **Defender for SQL Servers on Machines** (plan Defender for Databases): instala AMA, la extensión SQL IaaS y la de Defender, y añade la evaluación de vulnerabilidades |
| Restauraciones | Nunca restaurar un `.bak` de origen no fiable: puede tomar la instancia y el host |

### Copias de seguridad

| Opción | Lo que aporta | Límites |
|---|---|---|
| **[Azure Backup](/recursos/backups-update/azure-backup/)** | Recovery Services vault, log cada 15 minutos, restauración a un punto en el tiempo desde el portal, retención de años, soporte de grupos de disponibilidad, alertas e informes | Servicio aparte, de pago por uso |
| Automated Backup | Copias de todas las bases a una cuenta de almacenamiento, hasta 90 días | Standard y Enterprise. Necesita la clave de la cuenta, no borra copias caducadas y se restaura a mano |
| Manual (backup to URL, discos) | Control total | Todo lo gestionas tú |

Para usar Azure Backup, Automated Backup tiene que estar desactivado.

### Parcheo

**[Azure Update Manager](/recursos/backups-update/azure-update-manager/)** sustituye al Automated Patching de la extensión. Instala los **cumulative updates de SQL Server**, que Automated Patching no instala, además de las actualizaciones críticas e importantes del SO y de SQL Server.

- **Nunca los dos a la vez**: provoca parches fuera de ventana.
- Hay que activar *Microsoft updates* en la VM e incluir la clasificación *Updates* en la configuración de mantenimiento para que entren los CU.
- Update Manager **no sabe que hay un grupo de disponibilidad**: escalona las réplicas en ventanas distintas.

### Alta disponibilidad y recuperación

La alta disponibilidad de la VM **no protege la instancia de SQL Server**: el servicio puede caerse con la VM sana.

| Opción | Tipo | Detalle |
|---|---|---|
| **Grupo de disponibilidad Always On** | HA y DR | Réplicas en **zonas distintas** (99,99 %) o en un conjunto de disponibilidad (99,95 %). Las zonas añaden latencia y coste de tráfico entre zonas: probar con carga |
| Subredes múltiples | Conectividad | Una subred por réplica: **sin Azure Load Balancer ni DNN** para el listener |
| Una sola subred | Conectividad | Listener con DNN o con VNN y Load Balancer interno (con Floating IP); `MultiSubnetFailover=True` en la cadena de conexión |
| FCI | HA | Instancia completa con almacenamiento compartido (discos compartidos, S2D o Premium file share) |
| Log shipping | DR | Copias de log a un Azure file share |
| Azure Site Recovery | DR | Replica la VM completa a otra región |

- El clúster de Windows (WSFC) necesita un **dominio de Active Directory**; solo los grupos distribuidos configurados a mano prescinden de él.
- Umbrales de clúster menos agresivos: `SameSubnetDelay` y `CrossSubnetDelay` 1 segundo, `SameSubnetThreshold` y `CrossSubnetThreshold` 40 latidos. Una NIC por nodo. Quórum con votos impares y sin votos en la región de DR.
- **La geo-replicación de discos rompe SQL Server** si datos y log están en discos distintos: no garantiza el orden de escritura entre discos.
- **Réplicas pasivas gratis**: una para HA y otra para DR por instancia, con Software Assurance o con pago por uso si todas las réplicas están en Azure. Se marca con la licencia **DR**.

### Cómo se factura

| Concepto | Detalle |
|---|---|
| Cómputo | La VM, por segundo, con la licencia de Windows salvo Hybrid Benefit |
| Licencia de SQL Server (PAYG) | Por segundo y por vCPU; mismo coste en todas las versiones. **La estimación del portal no la incluye** |
| Azure Hybrid Benefit (AHUB) | Licencias por núcleos con Software Assurance o suscripción: solo se paga el cómputo base. Para cargas 24x7 y de vida conocida |
| PAYG | Cargas temporales, periódicas o de vida incierta |
| Réplicas pasivas | Licencia DR, sin coste de SQL Server |
| Developer y Express | Solo la VM |
| Discos y copias | Almacenamiento de cada disco y servicio de copias aparte |
| VM parada | **Solo desasignada** deja de cobrar cómputo y licencia |

El cambio de licencia **no tiene parada, no reinicia nada y es inmediato**. Solo para Standard y Enterprise. Con Hybrid Benefit gestionado de forma centralizada, la licencia ya no se cambia VM a VM.

### Qué escenario recomiendo

| Escenario del cliente | Diseño | Por qué |
|---|---|---|
| Migración tal cual con agentes en el servidor o versión fija | VM Ebdsv5 con imagen de Marketplace y AHUB | Sin rediseño y con licencias existentes |
| Producción crítica con RPO cercano a cero | Grupo de disponibilidad en dos zonas y dos subredes, secundaria con licencia DR | Sin balanceador, conmutación rápida y secundaria sin licencia |
| IO intensivo | Ebdsv5 con Premium SSD v2 o serie M con Write Accelerator para el log | Latencia submilisegundo sin pagar capacidad de más |
| Desarrollo y pruebas | Developer en serie D o B con apagado y desasignación | Sin licencia de SQL Server y sin cómputo fuera de horario |
| Recuperación ante desastres regional | Réplica asíncrona en otra región o Azure Site Recovery | La réplica pasiva no paga licencia |
| La aplicación no necesita el SO | [SQL Managed Instance](/recursos/database/sql-managed-instance/) | Parcheo, copias y alta disponibilidad incluidos |
| Inventario y licencias de SQL Server fuera de Azure | [Azure Arc para SQL Server](/recursos/hybrid/azure-arc-para-sql-server/) | Gestión y licencias desde Azure |

### Datos que conviene llevar a la reunión

- **Las imágenes llegan en RTM**: el primer CU se aplica tras desplegar.
- **Datos ReadOnly, log None, nunca ReadWrite.**
- **El número de columnas del pool no cambia**: dimensionar los discos al principio.
- **Automated Patching y Update Manager nunca juntos**; Update Manager no conoce el grupo de disponibilidad.
- **Entra exige SQL Server 2022 o posterior** y permisos de Graph, y no se puede desactivar.
- **La secundaria pasiva no paga licencia** con la licencia DR.
- **Solo desasignada** la VM deja de cobrar.
- **Cambiar CPU o almacenamiento** supone parada; en PaaS no.

## Decisiones de diseño

| Decisión | Lo que aplico | Por qué |
|---|---|---|
| Imagen | Marketplace `MicrosoftSQLServer`, ofertas y SKU validados | Almacenamiento y SQL Server configurados por la plataforma |
| VM | Módulo `windows_virtual_machine` del repositorio con zona, Trusted Launch y cifrado en el host | Mismo patrón que la ficha de VMs |
| Red | NIC privada sin IP pública; conectividad de SQL **PRIVATE** | Superficie mínima |
| Administrador local | Contraseña aleatoria guardada en Key Vault | Sin secretos en el código |
| Discos | Al menos uno de datos y uno de log (validado); datos y log fuera de `C:` y `D:` | Buenas prácticas de almacenamiento |
| Caching | Derivado del rol: ReadOnly en datos con Premium SSD < 4 TiB; None en el resto | Nadie puede poner ReadWrite por error |
| Configuración de almacenamiento | La de la extensión (pools de 64 KB, bases de sistema en datos, tempdb en `D:`) solo con Premium SSD | Es lo que soporta la extensión |
| Premium SSD v2 | Permitido con zona obligatoria (validado); volúmenes preparados dentro de la VM | Mejor precio/rendimiento en Ebdsv5 |
| Instancia | Memoria máxima obligatoria, IFI y Lock Pages in Memory activados | Lista de buenas prácticas |
| Parcheo | Update Manager (`AutomaticByPlatform`); sin Automated Patching | Instala los CU y evita conflictos |
| Copias | Azure Backup fuera de Terraform; sin Automated Backup | Automated Backup exige la clave de la cuenta en el código |
| Entra | Identidad de usuario creada antes; activación con PowerShell (Terraform) o en la plantilla (Bicep) | El provider no lo soporta |
| Licencias | PAYG por defecto; AHUB y DR solo en Standard y Enterprise (validado) | Developer, Express y Web no cambian de licencia |
| Monitorización | AMA con la DCR; assessment con su propio espacio de trabajo | Telemetría y buenas prácticas en Log Analytics |

Alineación con el Well-Architected Framework:

- **Fiabilidad**: zonas, grupos de disponibilidad en varias subredes, Azure Backup y discos separados.
- **Seguridad**: red privada, Trusted Launch, cifrado en el host, Entra, Key Vault y Defender.
- **Coste**: Hybrid Benefit, licencia DR en réplicas pasivas, vCPUs restringidas y Developer fuera de producción.
- **Excelencia operativa**: IaC con validaciones, Update Manager y assessment.
- **Rendimiento**: Ebdsv5, caching por rol, tempdb local y Premium SSD v2.

## Módulo de Terraform

### Los módulos del repositorio

El repositorio [AzureTerraformModules](https://github.com/luisadanmunoz/AzureTerraformModules) **no tiene módulo de SQL Server en VM**: ningún módulo usa `azurerm_mssql_virtual_machine`, ni los grupos de VMs de SQL ni los listeners. La VM, los discos, las conexiones y la extensión de AMA usan los módulos de `Compute/Compute/modules`, los mismos que la [ficha de Virtual Machines](/recursos/compute/virtual-machines/), que funcionan con azurerm 4.x. Lo propio de SQL Server va en el recurso nativo.

- `windows_virtual_machine` sigue sin publicar la identidad: el root la lee con `data "azurerm_virtual_machine"`.
- `managed_disk` acepta `disk_iops_read_write` y `disk_mbps_read_write`, así que sirve para Premium SSD v2.
- `Compute/VirtualMachine` sigue sin servir con azurerm 4.x (ver la ficha de VMs).

Notas del provider (azurerm 4.81):

- **No tiene autenticación de Entra**: ni `azureAdAuthenticationSettings`, ni `leastPrivilegeMode`, ni `enableAutomaticUpgrade` de la API. Se activa después con PowerShell; Bicep sí lo admite.
- `sql_license_type` es **ForceNew**: cambiar la licencia destruye y recrea el recurso SQL virtual machine, aunque en Azure el cambio es en caliente. Lo mismo con `collation`, `instant_file_initialization_enabled` y `lock_pages_in_memory_enabled`.
- `auto_backup` exige `storage_account_access_key` y la contraseña de cifrado; `key_vault_credential`, el secreto de un service principal; `wsfc_domain_credential`, contraseñas de dominio. El root no los usa.
- Quitar el bloque `auto_backup` también fuerza la recreación.
- `assessment` solo activa la función: ni el provider ni la API tienen dónde indicar el espacio de trabajo de Log Analytics, así que se activa con la CLI.
- `auto_patching` existe, pero es el Automated Patching que no debe convivir con Update Manager.
- `temp_db_settings.luns` es obligatorio: con tempdb en `D:` va vacío.

### Estructura en el proyecto

```txt
/
├── providers.tf               # azurerm >= 4.64.0, random
├── sql_virtual_machines.tf    # NIC, contraseña, VM, discos, registro en la extensión y AMA
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
      # Validado con 4.81.0. >= 4.0: nombres de argumentos de la NIC (accelerated_networking_enabled).
      # < 5.0.0: restricción de los módulos de AzureTerraformModules.
      version = ">= 4.64.0, < 5.0.0"
    }
    random = {
      source  = "hashicorp/random"
      version = ">= 3.6.0, < 4.0.0"
    }
  }
}

provider "azurerm" {
  features {
    virtual_machine {
      # No borrar el disco del SO al destruir la VM: decisión explícita, no por defecto
      delete_os_disk_on_deletion = false
    }
  }
}

variable "tags" {
  description = "Tags corporativos comunes a todos los recursos."
  type        = map(string)
}
```

### `sql_virtual_machines.tf`

```hcl
# =============================================================================
# SQL Server en VMs Windows seguras por defecto: imagen de Marketplace, zona, Trusted Launch,
# cifrado en el host, sin IP pública, discos separados para datos y log con el caching de
# las buenas prácticas, tempdb en el disco temporal y registro en la extensión SQL IaaS Agent
# (conectividad privada, configuración de instancia y de almacenamiento)
#
# DEPENDENCY: proveedor Microsoft.SqlVirtualMachine registrado en la suscripción
# DEPENDENCY: característica Microsoft.Compute/EncryptionAtHost registrada en la suscripción
# DEPENDENCY: grupos de recursos y subredes creados; NSG en la subred con el puerto de SQL
#             abierto solo desde las subredes de aplicación (y salida 80 y 443 a la etiqueta
#             AzureActiveDirectory si se usa autenticación de Entra)
# DEPENDENCY: tamaño de VM con disco temporal local (p. ej. Ebdsv5) para tempdb en D:
# DEPENDENCY: salida explícita a Internet en la subred (NAT Gateway o firewall con UDR) para
#             Windows Update, las extensiones y Microsoft Entra ID
# DEPENDENCY: Key Vault con RBAC para la contraseña de Windows; la identidad de Terraform
#             necesita "Key Vault Secrets Officer" y alcance de red al vault
# DEPENDENCY: identidad de usuario creada antes, con Directory Readers o los permisos de
#             Microsoft Graph, si se va a activar la autenticación de Entra
# DEPENDENCY: Data Collection Rule y Disk Encryption Set (CMK) creados si se usan
# =============================================================================

variable "sql_virtual_machines" {
  description = "SQL Server en VMs (clave = nombre del recurso)."
  type = map(object({
    resource_group_name = string
    location            = string
    size                = string           # memoria 8:1 por vCore en producción, p. ej. Standard_E8bds_v5
    zone                = optional(string) # 1 | 2 | 3; null solo en conjuntos de disponibilidad
    computer_name       = optional(string) # 15 caracteres como máximo

    # Imagen de Marketplace (publisher MicrosoftSQLServer)
    image_offer   = string                     # p. ej. sql2022-ws2022
    image_sku     = string                     # p. ej. enterprise-gen2
    image_version = optional(string, "latest") # las imágenes llegan en RTM: parchear después

    # Licencias: PAYG, AHUB (Software Assurance) o DR (réplica pasiva gratuita)
    sql_license_type = optional(string, "PAYG")
    os_license_type  = optional(string) # Windows_Server (Azure Hybrid Benefit de Windows)

    # Red: una NIC privada; sin IP pública ni reenvío de IP
    subnet_id                      = string
    private_ip_address             = optional(string)
    accelerated_networking_enabled = optional(bool, true)
    sql_connectivity_port          = optional(number, 1433)

    # Administrador local de Windows: la contraseña se genera y se guarda en Key Vault
    admin_username = string
    key_vault_id   = string

    os_disk = optional(object({
      storage_account_type = optional(string, "Premium_LRS")
      disk_size_gb         = optional(number)
    }), {})

    # Discos de SQL Server: al menos uno de datos y uno de log; el caching se deriva del rol
    data_disks = map(object({
      role                 = string # data | log
      lun                  = number
      disk_size_gb         = number
      storage_account_type = optional(string, "Premium_LRS") # Premium_LRS | PremiumV2_LRS | StandardSSD_LRS
      disk_iops_read_write = optional(number)                # solo PremiumV2_LRS
      disk_mbps_read_write = optional(number)                # solo PremiumV2_LRS
    }))

    # Configuración de almacenamiento de la extensión (solo con Premium_LRS)
    storage_workload_type          = optional(string, "GENERAL") # GENERAL | OLTP | DW
    data_path                      = optional(string, "F:\\SQLData")
    log_path                       = optional(string, "G:\\SQLLog")
    system_db_on_data_disk_enabled = optional(bool, true)
    tempdb = optional(object({
      path                = optional(string, "D:\\SQLTemp") # disco temporal local
      data_file_count     = optional(number, 8)             # uno por núcleo, hasta 8
      data_file_size_mb   = optional(number, 256)
      data_file_growth_mb = optional(number, 512)
      log_file_size_mb    = optional(number, 256)
      log_file_growth_mb  = optional(number, 512)
    }), {})

    # Configuración de la instancia (lpim e ifi solo se fijan al crear)
    sql_instance = object({
      max_server_memory_mb                 = number # deja memoria al sistema operativo
      min_server_memory_mb                 = optional(number, 0)
      max_dop                              = optional(number, 0)
      adhoc_workloads_optimization_enabled = optional(bool, false) # true en OLTP con mucho SQL ad hoc
      instant_file_initialization_enabled  = optional(bool, true)
      lock_pages_in_memory_enabled         = optional(bool, true)
      collation                            = optional(string, "SQL_Latin1_General_CP1_CI_AS")
    })

    disk_encryption_set_id     = optional(string)
    encryption_at_host_enabled = optional(bool, true)

    user_assigned_identity_ids    = optional(list(string), []) # la primera, para Entra
    capacity_reservation_group_id = optional(string)
    timezone                      = optional(string)

    data_collection_rule_id = optional(string)

    tags = optional(map(string), {})
  }))
  default = {}

  validation {
    condition = alltrue([
      for k, v in var.sql_virtual_machines :
      contains(["sql2025-ws2025", "sql2022-ws2022", "sql2019-ws2022", "sql2019-ws2019", "sql2017-ws2019"], lower(v.image_offer))
    ])
    error_message = "image_offer debe ser una oferta de SQL Server con soporte: sql2025-ws2025, sql2022-ws2022, sql2019-ws2022, sql2019-ws2019 o sql2017-ws2019."
  }

  validation {
    condition = alltrue([
      for k, v in var.sql_virtual_machines :
      contains(["enterprise-gen2", "standard-gen2", "web-gen2", "enterprisedbengineonly-gen2", "sqldev-gen2", "entdev-gen2", "stddev-gen2"], lower(v.image_sku))
    ])
    error_message = "image_sku no válido (enterprise-gen2, standard-gen2, web-gen2, enterprisedbengineonly-gen2, SQLDEV-gen2, entdev-gen2 o stddev-gen2)."
  }

  validation {
    condition     = alltrue([for k, v in var.sql_virtual_machines : contains(["PAYG", "AHUB", "DR"], v.sql_license_type)])
    error_message = "sql_license_type debe ser PAYG, AHUB o DR."
  }

  validation {
    condition = alltrue([
      for k, v in var.sql_virtual_machines :
      v.sql_license_type == "PAYG" || can(regex("^(standard|enterprise)", lower(v.image_sku)))
    ])
    error_message = "AHUB y DR solo existen para Standard y Enterprise (Developer, Express y Web no cambian de licencia)."
  }

  validation {
    condition     = alltrue([for k, v in var.sql_virtual_machines : length(coalesce(v.computer_name, k)) <= 15])
    error_message = "El nombre de equipo de Windows tiene 15 caracteres como máximo: usa computer_name."
  }

  validation {
    condition     = alltrue([for k, v in var.sql_virtual_machines : v.zone == null || contains(["1", "2", "3"], coalesce(v.zone, "x"))])
    error_message = "zone debe ser 1, 2 o 3."
  }

  validation {
    condition = alltrue([
      for k, v in var.sql_virtual_machines :
      contains(["Premium_LRS", "Premium_ZRS", "StandardSSD_LRS", "StandardSSD_ZRS"], v.os_disk.storage_account_type)
    ])
    error_message = "Disco del SO: Premium o Standard SSD (Premium SSD v2 no sirve como disco del SO)."
  }

  validation {
    condition = alltrue(flatten([
      for k, v in var.sql_virtual_machines : [
        for dk, d in v.data_disks :
        contains(["data", "log"], d.role) && contains(["Premium_LRS", "PremiumV2_LRS", "StandardSSD_LRS"], d.storage_account_type)
      ]
    ]))
    error_message = "Cada disco necesita role data o log y tipo Premium_LRS, PremiumV2_LRS o StandardSSD_LRS."
  }

  validation {
    condition = alltrue([
      for k, v in var.sql_virtual_machines :
      contains([for d in values(v.data_disks) : d.role], "data") && contains([for d in values(v.data_disks) : d.role], "log")
    ])
    error_message = "Datos y log van en discos separados: hace falta al menos un disco data y uno log."
  }

  validation {
    condition = alltrue([
      for k, v in var.sql_virtual_machines :
      length(distinct([for d in values(v.data_disks) : d.lun])) == length(v.data_disks)
    ])
    error_message = "Los LUN de los discos no pueden repetirse."
  }

  validation {
    condition = alltrue(flatten([
      for k, v in var.sql_virtual_machines : [
        for dk, d in v.data_disks :
        d.storage_account_type != "PremiumV2_LRS" || v.zone != null
      ]
    ]))
    error_message = "Premium SSD v2 solo se conecta a VMs zonales en la mayoría de regiones con zonas: indica zone."
  }

  validation {
    condition = alltrue(flatten([
      for k, v in var.sql_virtual_machines : [
        for dk, d in v.data_disks :
        d.storage_account_type == "PremiumV2_LRS" || (d.disk_iops_read_write == null && d.disk_mbps_read_write == null)
      ]
    ]))
    error_message = "disk_iops_read_write y disk_mbps_read_write solo se ajustan en Premium SSD v2."
  }

  validation {
    condition     = alltrue([for k, v in var.sql_virtual_machines : contains(["GENERAL", "OLTP", "DW"], v.storage_workload_type)])
    error_message = "storage_workload_type debe ser GENERAL, OLTP o DW."
  }

  validation {
    condition = alltrue([
      for k, v in var.sql_virtual_machines :
      !startswith(upper(v.data_path), "C:") && !startswith(upper(v.data_path), "D:") &&
      !startswith(upper(v.log_path), "C:") && !startswith(upper(v.log_path), "D:") &&
      substr(upper(v.data_path), 0, 2) != substr(upper(v.log_path), 0, 2)
    ])
    error_message = "Datos y log van en unidades distintas y nunca en C: (SO) ni en D: (disco temporal)."
  }

  validation {
    condition     = alltrue([for k, v in var.sql_virtual_machines : v.tempdb.data_file_count >= 1 && v.tempdb.data_file_count <= 8])
    error_message = "Durante el despliegue tempdb admite de 1 a 8 ficheros de datos."
  }

  validation {
    condition = alltrue([
      for k, v in var.sql_virtual_machines :
      v.sql_instance.max_server_memory_mb >= 128 && v.sql_instance.min_server_memory_mb <= v.sql_instance.max_server_memory_mb
    ])
    error_message = "max_server_memory_mb debe ser >= 128 y mayor o igual que min_server_memory_mb."
  }

  validation {
    condition     = alltrue([for k, v in var.sql_virtual_machines : v.sql_connectivity_port >= 1 && v.sql_connectivity_port <= 65535])
    error_message = "sql_connectivity_port debe estar entre 1 y 65535."
  }
}

# -----------------------------------------------------------------------------
# NIC privada (sin IP pública, sin reenvío; el NSG va en la subred)
# -----------------------------------------------------------------------------
resource "azurerm_network_interface" "sql" {
  for_each = var.sql_virtual_machines

  name                           = "nic-${each.key}"
  resource_group_name            = each.value.resource_group_name
  location                       = each.value.location
  accelerated_networking_enabled = each.value.accelerated_networking_enabled
  ip_forwarding_enabled          = false

  ip_configuration {
    name                          = "ipconfig1"
    subnet_id                     = each.value.subnet_id
    private_ip_address_allocation = each.value.private_ip_address == null ? "Dynamic" : "Static"
    private_ip_address            = each.value.private_ip_address
  }

  tags = merge(var.tags, each.value.tags)
}

# -----------------------------------------------------------------------------
# Contraseña del administrador local: generada y guardada en Key Vault (nunca en tfvars)
# -----------------------------------------------------------------------------
resource "random_password" "sql_vm_admin" {
  for_each = var.sql_virtual_machines

  length           = 24
  special          = true
  override_special = "!@#$%*()-_=+[]{}:?"
  min_lower        = 2
  min_upper        = 2
  min_numeric      = 2
  min_special      = 2
}

resource "azurerm_key_vault_secret" "sql_vm_admin" {
  for_each = random_password.sql_vm_admin

  name         = "vm-${each.key}-admin"
  value        = each.value.result
  key_vault_id = var.sql_virtual_machines[each.key].key_vault_id
  content_type = "VM local administrator (${var.sql_virtual_machines[each.key].admin_username})"
}

# -----------------------------------------------------------------------------
# VM Windows con la imagen de SQL Server (módulo Compute/Compute/modules del repositorio)
# -----------------------------------------------------------------------------
module "sql_windows_virtual_machine" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Compute/Compute/modules/windows_virtual_machine?ref=main"
  for_each = var.sql_virtual_machines

  windows_virtual_machine_name = each.key
  computer_name                = coalesce(each.value.computer_name, each.key)
  resource_group_name          = each.value.resource_group_name
  location                     = each.value.location
  size                         = each.value.size
  zone                         = each.value.zone
  network_interface_ids        = [azurerm_network_interface.sql[each.key].id]

  admin_username = each.value.admin_username
  admin_password = random_password.sql_vm_admin[each.key].result

  source_image_reference = {
    publisher = "MicrosoftSQLServer"
    offer     = each.value.image_offer
    sku       = each.value.image_sku
    version   = each.value.image_version
  }
  license_type = each.value.os_license_type
  timezone     = each.value.timezone

  # Trusted Launch + cifrado de extremo a extremo
  secure_boot_enabled        = true
  vtpm_enabled               = true
  encryption_at_host_enabled = each.value.encryption_at_host_enabled

  # Azure Update Manager (Customer Managed Schedules); nunca junto al Automated Patching de SQL
  provision_vm_agent                                     = true
  allow_extension_operations                             = true
  patch_mode                                             = "AutomaticByPlatform"
  bypass_platform_safety_checks_on_user_schedule_enabled = true
  patch_assessment_mode                                  = "AutomaticByPlatform"

  capacity_reservation_group_id = each.value.capacity_reservation_group_id

  identity = {
    type         = length(each.value.user_assigned_identity_ids) > 0 ? "SystemAssigned, UserAssigned" : "SystemAssigned"
    identity_ids = length(each.value.user_assigned_identity_ids) > 0 ? each.value.user_assigned_identity_ids : null
  }

  os_disk = {
    name                   = "osdisk-${each.key}"
    caching                = "ReadWrite" # valor por defecto del disco del SO: no cambiarlo
    storage_account_type   = each.value.os_disk.storage_account_type
    disk_size_gb           = each.value.os_disk.disk_size_gb
    disk_encryption_set_id = each.value.disk_encryption_set_id
  }

  boot_diagnostics = {} # almacenamiento gestionado por Azure

  tags = merge(var.tags, each.value.tags)
}

# -----------------------------------------------------------------------------
# Discos de datos y log (misma zona que la VM)
# -----------------------------------------------------------------------------
module "sql_data_disk" {
  source = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Compute/Compute/modules/managed_disk?ref=main"
  for_each = {
    for d in flatten([
      for k, v in var.sql_virtual_machines : [
        for dk, disk in v.data_disks : {
          key  = "${k}/${dk}"
          name = "disk-${k}-${dk}"
          vm   = v
          disk = disk
        }
      ]
    ]) : d.key => d
  }

  managed_disk_name             = each.value.name
  resource_group_name           = each.value.vm.resource_group_name
  location                      = each.value.vm.location
  zone                          = each.value.vm.zone
  create_option                 = "Empty"
  storage_account_type          = each.value.disk.storage_account_type
  disk_size_gb                  = each.value.disk.disk_size_gb
  disk_iops_read_write          = each.value.disk.disk_iops_read_write
  disk_mbps_read_write          = each.value.disk.disk_mbps_read_write
  disk_encryption_set_id        = each.value.vm.disk_encryption_set_id
  public_network_access_enabled = false
  network_access_policy         = "DenyAll" # sin exportación ni importación por SAS

  tags = merge(var.tags, each.value.vm.tags)
}

# Caching: ReadOnly en datos con Premium SSD (< 4 TiB); None en log y en Premium SSD v2
module "sql_data_disk_attachment" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Compute/Compute/modules/virtual_machine_data_disk_attachment?ref=main"
  for_each = module.sql_data_disk

  managed_disk_id    = each.value.id
  virtual_machine_id = module.sql_windows_virtual_machine[split("/", each.key)[0]].id
  lun                = var.sql_virtual_machines[split("/", each.key)[0]].data_disks[split("/", each.key)[1]].lun
  caching = (
    var.sql_virtual_machines[split("/", each.key)[0]].data_disks[split("/", each.key)[1]].role == "data" &&
    var.sql_virtual_machines[split("/", each.key)[0]].data_disks[split("/", each.key)[1]].storage_account_type == "Premium_LRS" &&
    var.sql_virtual_machines[split("/", each.key)[0]].data_disks[split("/", each.key)[1]].disk_size_gb < 4096
  ) ? "ReadOnly" : "None"
}

# -----------------------------------------------------------------------------
# Registro en la extensión SQL IaaS Agent (crea el recurso SQL virtual machine)
# Sin auto_patching (Update Manager), sin auto_backup (Azure Backup) y sin key_vault_credential:
# los dos últimos exigen claves o secretos en el código
# -----------------------------------------------------------------------------
resource "azurerm_mssql_virtual_machine" "this" {
  for_each = var.sql_virtual_machines

  virtual_machine_id = module.sql_windows_virtual_machine[each.key].id
  sql_license_type   = each.value.sql_license_type

  sql_connectivity_type = "PRIVATE"
  sql_connectivity_port = each.value.sql_connectivity_port

  sql_instance {
    max_server_memory_mb                 = each.value.sql_instance.max_server_memory_mb
    min_server_memory_mb                 = each.value.sql_instance.min_server_memory_mb
    max_dop                              = each.value.sql_instance.max_dop
    adhoc_workloads_optimization_enabled = each.value.sql_instance.adhoc_workloads_optimization_enabled
    instant_file_initialization_enabled  = each.value.sql_instance.instant_file_initialization_enabled
    lock_pages_in_memory_enabled         = each.value.sql_instance.lock_pages_in_memory_enabled
    collation                            = each.value.sql_instance.collation
  }

  # La extensión crea los pools de Storage Spaces (64 KB) solo con Premium SSD;
  # con Premium SSD v2 o Standard SSD los volúmenes se preparan dentro de la VM
  dynamic "storage_configuration" {
    for_each = alltrue([for d in values(each.value.data_disks) : d.storage_account_type == "Premium_LRS"]) ? [each.value] : []
    content {
      disk_type                      = "NEW"
      storage_workload_type          = storage_configuration.value.storage_workload_type
      system_db_on_data_disk_enabled = storage_configuration.value.system_db_on_data_disk_enabled

      data_settings {
        default_file_path = storage_configuration.value.data_path
        luns              = sort([for d in values(storage_configuration.value.data_disks) : d.lun if d.role == "data"])
      }

      log_settings {
        default_file_path = storage_configuration.value.log_path
        luns              = sort([for d in values(storage_configuration.value.data_disks) : d.lun if d.role == "log"])
      }

      temp_db_settings {
        default_file_path      = storage_configuration.value.tempdb.path
        luns                   = [] # disco temporal local: sin discos de datos
        data_file_count        = storage_configuration.value.tempdb.data_file_count
        data_file_size_mb      = storage_configuration.value.tempdb.data_file_size_mb
        data_file_growth_in_mb = storage_configuration.value.tempdb.data_file_growth_mb
        log_file_size_mb       = storage_configuration.value.tempdb.log_file_size_mb
        log_file_growth_mb     = storage_configuration.value.tempdb.log_file_growth_mb
      }
    }
  }

  tags = merge(var.tags, each.value.tags)

  # La configuración de almacenamiento necesita los discos ya conectados
  depends_on = [module.sql_data_disk_attachment]
}

# -----------------------------------------------------------------------------
# Azure Monitor Agent + asociación a la DCR
# -----------------------------------------------------------------------------
module "sql_vm_ama" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Compute/Compute/modules/virtual_machine_extension?ref=main"
  for_each = { for k, v in var.sql_virtual_machines : k => v if v.data_collection_rule_id != null }

  virtual_machine_extension_name = "AzureMonitorWindowsAgent"
  virtual_machine_id             = module.sql_windows_virtual_machine[each.key].id
  publisher                      = "Microsoft.Azure.Monitor"
  type                           = "AzureMonitorWindowsAgent"
  type_handler_version           = "1.0"
  auto_upgrade_minor_version     = true
  automatic_upgrade_enabled      = true

  tags = merge(var.tags, each.value.tags)

  depends_on = [azurerm_mssql_virtual_machine.this]
}

resource "azurerm_monitor_data_collection_rule_association" "sql" {
  for_each = { for k, v in var.sql_virtual_machines : k => v if v.data_collection_rule_id != null }

  name                    = "dcra-${each.key}"
  target_resource_id      = module.sql_windows_virtual_machine[each.key].id
  data_collection_rule_id = each.value.data_collection_rule_id

  depends_on = [module.sql_vm_ama]
}

# El módulo no publica la identidad: se lee después de crear la VM
data "azurerm_virtual_machine" "sql" {
  for_each = var.sql_virtual_machines

  name                = each.key
  resource_group_name = each.value.resource_group_name

  depends_on = [module.sql_windows_virtual_machine]
}

# -----------------------------------------------------------------------------
# Salidas
# -----------------------------------------------------------------------------
output "sql_virtual_machine_ids" {
  description = "IDs de los recursos SQL virtual machine (Microsoft.SqlVirtualMachine)."
  value       = { for k, s in azurerm_mssql_virtual_machine.this : k => s.id }
}

output "virtual_machine_ids" {
  description = "IDs de las VMs."
  value       = { for k, m in module.sql_windows_virtual_machine : k => m.id }
}

output "private_ips" {
  description = "IP privada de cada VM (el listener de un grupo de disponibilidad tiene otras)."
  value       = { for k, n in azurerm_network_interface.sql : k => n.private_ip_address }
}

output "principal_ids" {
  description = "principalId de la identidad del sistema (RBAC y permisos de Graph)."
  value       = { for k, d in data.azurerm_virtual_machine.sql : k => try(d.identity[0].principal_id, null) }
}

output "admin_secret_ids" {
  description = "Secretos de Key Vault con la contraseña local de cada VM."
  value       = { for k, s in azurerm_key_vault_secret.sql_vm_admin : k => s.versionless_id }
}
```

### `env/pro.tfvars`

Dos réplicas para un grupo de disponibilidad en dos zonas y dos subredes. La secundaria es pasiva y usa la licencia DR.

```hcl
tags = {
  environment = "pro"
  workload    = "<workload>"
  owner       = "<owner>"
  costcenter  = "<costcenter>"
}

sql_virtual_machines = {
  # Réplica principal del grupo de disponibilidad: zona 1, subred propia, Azure Hybrid Benefit
  "vm-sql-pro-01" = {
    resource_group_name = "<rg-sql-pro>"
    location            = "<region>"
    size                = "Standard_E8bds_v5"
    zone                = "1"
    computer_name       = "vmsqlpro01"

    image_offer      = "sql2022-ws2022"
    image_sku        = "enterprise-gen2"
    sql_license_type = "AHUB"
    os_license_type  = "Windows_Server"
    timezone         = "Romance Standard Time"

    subnet_id      = "<resourceId snet-sql-pro-z1>"
    admin_username = "<admin-local>"
    key_vault_id   = "<resourceId kv-<workload>-pro>"

    data_disks = {
      data01 = { role = "data", lun = 0, disk_size_gb = 1024 }
      data02 = { role = "data", lun = 1, disk_size_gb = 1024 }
      log01  = { role = "log", lun = 2, disk_size_gb = 1024 }
    }
    storage_workload_type = "OLTP"

    sql_instance = {
      max_server_memory_mb                 = 57344 # ajustar con Memory\Available Bytes
      adhoc_workloads_optimization_enabled = true
    }

    user_assigned_identity_ids = ["<resourceId id-sql-pro>"]
    data_collection_rule_id    = "<resourceId dcr-sql-windows-pro>"

    tags = {
      PatchGroup = "sql-pro-wave2"
    }
  }

  # Réplica secundaria pasiva: zona 2, otra subred (sin balanceador ni DNN), licencia DR gratuita
  "vm-sql-pro-02" = {
    resource_group_name = "<rg-sql-pro>"
    location            = "<region>"
    size                = "Standard_E8bds_v5"
    zone                = "2"
    computer_name       = "vmsqlpro02"

    image_offer      = "sql2022-ws2022"
    image_sku        = "enterprise-gen2"
    sql_license_type = "DR"
    os_license_type  = "Windows_Server"
    timezone         = "Romance Standard Time"

    subnet_id      = "<resourceId snet-sql-pro-z2>"
    admin_username = "<admin-local>"
    key_vault_id   = "<resourceId kv-<workload>-pro>"

    data_disks = {
      data01 = { role = "data", lun = 0, disk_size_gb = 1024 }
      data02 = { role = "data", lun = 1, disk_size_gb = 1024 }
      log01  = { role = "log", lun = 2, disk_size_gb = 1024 }
    }
    storage_workload_type = "OLTP"

    sql_instance = {
      max_server_memory_mb                 = 57344
      adhoc_workloads_optimization_enabled = true
    }

    user_assigned_identity_ids = ["<resourceId id-sql-pro>"]
    data_collection_rule_id    = "<resourceId dcr-sql-windows-pro>"

    tags = {
      PatchGroup = "sql-pro-wave1"
    }
  }
}
```

### Despliegue y comprobación

Antes del primer despliegue:

```powershell
Register-AzResourceProvider -ProviderNamespace Microsoft.SqlVirtualMachine

# Regiones donde existe la extensión SQL IaaS Agent
(Get-AzResourceProvider -ProviderNamespace Microsoft.SqlVirtualMachine).ResourceTypes |
    Where-Object { $_.ResourceTypeName -eq "SqlVirtualMachines" } |
    Select-Object -ExpandProperty Locations
```

```powershell
terraform init
terraform plan -var-file="env/pro.tfvars" -out="pro.tfplan"
terraform apply "pro.tfplan"

Get-AzSqlVM -ResourceGroupName "<rg-sql-pro>" -Name "vm-sql-pro-01" | Format-List
Get-AzVMSqlServerExtension -VMName "vm-sql-pro-01" -ResourceGroupName "<rg-sql-pro>"
```

**Microsoft Entra ID**. La identidad necesita los permisos de Graph, que concede un administrador con `AppRoleAssignment.ReadWrite.All`. Después se activa en cada VM:

```powershell
Connect-MgGraph -Scopes "AppRoleAssignment.ReadWrite.All" -TenantId "<tenant-id>"
$graph = Get-MgServicePrincipal -Filter "DisplayName eq 'Microsoft Graph'"
$msi   = Get-MgServicePrincipal -Filter "displayName eq 'id-sql-pro'"
foreach ($perm in "User.Read.All", "GroupMember.Read.All", "Application.Read.All") {
    $role = $graph.AppRoles | Where-Object { $_.Value -eq $perm }
    New-MgServicePrincipalAppRoleAssignment -ServicePrincipalId $msi.Id `
        -BodyParameter @{ principalId = $msi.Id; resourceId = $graph.Id; appRoleId = $role.Id }
}

# Irreversible: una vez activado no se puede desactivar
Update-AzSqlVM -ResourceGroupName "<rg-sql-pro>" -Name "vm-sql-pro-01" `
    -IdentityType "UserAssigned" -ManagedIdentityClientId "<clientId id-sql-pro>"
```

**SQL best practices assessment**. El espacio de trabajo debe estar en la misma suscripción y su ubicación no puede tener espacios. Una ejecución consume entre un 5 y un 10 % de CPU:

```powershell
az sql vm update -g "<rg-sql-pro>" -n "vm-sql-pro-01" `
    --assessment-weekly-interval 1 --assessment-day-of-week Sunday --assessment-start-time-local "23:00" `
    --workspace-name "<log-workload-pro>" --workspace-rg "<rg-monitor-pro>" --agent-rg "<rg-monitor-pro>"
```

**Azure Backup**. Con la política de SQL de la [ficha de Azure Backup](/recursos/backups-update/azure-backup/), registro de la VM y autoprotección de la instancia:

```powershell
$vault  = Get-AzRecoveryServicesVault -ResourceGroupName "<rg-backup-pro>" -Name "rsv-<workload>-pro-<region>-01"
$vm     = Get-AzVM -ResourceGroupName "<rg-sql-pro>" -Name "vm-sql-pro-01"
$policy = Get-AzRecoveryServicesBackupProtectionPolicy -Name "bkpol-sql-daily-log15" -VaultId $vault.ID

Register-AzRecoveryServicesBackupContainer -ResourceId $vm.ID -BackupManagementType AzureWorkload -WorkloadType MSSQL -VaultId $vault.ID -Force

$instance = Get-AzRecoveryServicesBackupProtectableItem -WorkloadType MSSQL -ItemType SQLInstance -VaultId $vault.ID -Name "MSSQLSERVER" -ServerName "vm-sql-pro-01"
Enable-AzRecoveryServicesBackupAutoProtection -InputItem $instance -BackupManagementType AzureWorkload -WorkloadType MSSQL -Policy $policy -VaultId $vault.ID
```

Con Premium SSD v2 o Standard SSD, la extensión no prepara los volúmenes: se crea un pool por rol dentro de la VM con stripe y unidad de asignación de 64 KB y una columna por disco:

```powershell
# Filtra solo los discos de datos de SQL (repite con los de log, letra G:)
$disks = Get-PhysicalDisk | Where-Object { $_.FriendlyName -like "<discos de datos>" }

New-StoragePool -FriendlyName "SQLData" -StorageSubsystemFriendlyName "Windows Storage on vmsqlpro01" `
    -PhysicalDisks $disks | New-VirtualDisk -FriendlyName "SQLData" -Interleave 65536 `
    -NumberOfColumns $disks.Count -ResiliencySettingName simple -UseMaximumSize |
    Initialize-Disk -PartitionStyle GPT -PassThru | New-Partition -DriveLetter F -UseMaximumSize |
    Format-Volume -FileSystem NTFS -NewFileSystemLabel "SQLData" -AllocationUnitSize 65536 -Confirm:$false
```

### Equivalente en Bicep

Una plantilla por VM. A diferencia de Terraform, la API admite **Entra, mínimo privilegio y la actualización automática de la extensión** en el propio recurso. La contraseña se lee de Key Vault en el `.bicepparam`.

`sqlvm.bicep`:

```bicep
// =============================================================================
// SQL Server en una VM Windows segura por defecto: imagen de Marketplace, zona, Trusted Launch,
// cifrado en el host, sin IP pública, discos de datos y log con el caching de las buenas
// prácticas, tempdb en el disco temporal y registro en la extensión SQL IaaS Agent
// (conectividad privada, mínimo privilegio, instancia, almacenamiento y Entra opcional)
// DEPENDENCY: proveedor Microsoft.SqlVirtualMachine y EncryptionAtHost registrados
// DEPENDENCY: subred con NSG y salida explícita; contraseña en Key Vault (getSecret en el .bicepparam)
// DEPENDENCY: con Entra, identidad con Directory Readers o permisos de Graph ANTES del despliegue
// =============================================================================
param name string
param location string = resourceGroup().location
param size string

@allowed(['1', '2', '3'])
param zone string

@maxLength(15)
param computerName string

@allowed(['sql2025-ws2025', 'sql2022-ws2022', 'sql2019-ws2022', 'sql2019-ws2019', 'sql2017-ws2019'])
param imageOffer string

@allowed([
  'enterprise-gen2'
  'standard-gen2'
  'web-gen2'
  'enterprisedbengineonly-gen2'
  'SQLDEV-gen2'
  'entdev-gen2'
  'stddev-gen2'
])
param imageSku string

@allowed(['PAYG', 'AHUB', 'DR'])
param sqlLicenseType string = 'PAYG'

@description('Windows_Server = Azure Hybrid Benefit de Windows')
param osLicenseType string?
param timeZone string?

param subnetId string
param privateIpAddress string?
param sqlPort int = 1433

param adminUsername string

@secure()
param adminPassword string

@allowed(['Premium_LRS', 'Premium_ZRS', 'StandardSSD_LRS', 'StandardSSD_ZRS'])
param osDiskType string = 'Premium_LRS'

@description('[{ name, role (data|log), lun, sizeGb, sku (Premium_LRS|PremiumV2_LRS|StandardSSD_LRS), iops?, mbps? }]')
@minLength(2)
param dataDisks array

@allowed(['GENERAL', 'OLTP', 'DW'])
param storageWorkloadType string = 'GENERAL'
param dataPath string = 'F:\\SQLData'
param logPath string = 'G:\\SQLLog'

@description('{ path, dataFileCount, dataFileSizeMb, dataGrowthMb, logFileSizeMb, logGrowthMb }')
param tempDb object = {
  path: 'D:\\SQLTemp'
  dataFileCount: 8
  dataFileSizeMb: 256
  dataGrowthMb: 512
  logFileSizeMb: 256
  logGrowthMb: 512
}

@description('{ maxServerMemoryMb, minServerMemoryMb?, maxDop?, adHoc?, ifi?, lpim?, collation? }')
param sqlInstance object

@description('Identidades de usuario adicionales (resourceId)')
param userAssignedIdentityIds array = []

param enableEntraAuthentication bool = false

@description('clientId de la identidad de usuario para Entra; vacío = identidad del sistema')
param entraIdentityClientId string = ''

param diskEncryptionSetId string?
param encryptionAtHost bool = true
param dataCollectionRuleId string?
param tags object = {}

var desRef = empty(diskEncryptionSetId ?? '') ? null : { id: diskEncryptionSetId }
var onlyPremiumSsd = length(filter(dataDisks, d => d.sku != 'Premium_LRS')) == 0
var hasDataAndLog = length(filter(dataDisks, d => d.role == 'data')) > 0 && length(filter(
  dataDisks,
  d => d.role == 'log'
)) > 0

resource nic 'Microsoft.Network/networkInterfaces@2024-05-01' = {
  name: 'nic-${name}'
  location: location
  tags: tags
  properties: {
    enableAcceleratedNetworking: true
    enableIPForwarding: false
    ipConfigurations: [
      {
        name: 'ipconfig1'
        properties: {
          subnet: {
            id: subnetId
          }
          privateIPAllocationMethod: empty(privateIpAddress ?? '') ? 'Dynamic' : 'Static'
          privateIPAddress: privateIpAddress
        }
      }
    ]
  }
}

resource disks 'Microsoft.Compute/disks@2024-03-02' = [
  for d in dataDisks: {
    name: 'disk-${name}-${d.name}'
    location: location
    tags: tags
    sku: {
      name: d.sku
    }
    zones: [
      zone
    ]
    properties: {
      creationData: {
        createOption: 'Empty'
      }
      diskSizeGB: d.sizeGb
      diskIOPSReadWrite: d.sku == 'PremiumV2_LRS' ? d.?iops : null
      diskMBpsReadWrite: d.sku == 'PremiumV2_LRS' ? d.?mbps : null
      encryption: empty(diskEncryptionSetId ?? '')
        ? null
        : {
            type: 'EncryptionAtRestWithCustomerKey'
            diskEncryptionSetId: diskEncryptionSetId
          }
      publicNetworkAccess: 'Disabled'
      networkAccessPolicy: 'DenyAll'
    }
  }
]

resource vm 'Microsoft.Compute/virtualMachines@2024-11-01' = {
  name: name
  location: location
  zones: [
    zone
  ]
  tags: tags
  identity: empty(userAssignedIdentityIds)
    ? {
        type: 'SystemAssigned'
      }
    : {
        type: 'SystemAssigned, UserAssigned'
        userAssignedIdentities: toObject(userAssignedIdentityIds, id => id, id => {})
      }
  properties: {
    hardwareProfile: {
      vmSize: size
    }
    licenseType: osLicenseType
    securityProfile: {
      securityType: 'TrustedLaunch'
      uefiSettings: {
        secureBootEnabled: true
        vTpmEnabled: true
      }
      encryptionAtHost: encryptionAtHost
    }
    storageProfile: {
      imageReference: {
        publisher: 'MicrosoftSQLServer'
        offer: imageOffer
        sku: imageSku
        version: 'latest'
      }
      osDisk: {
        name: 'osdisk-${name}'
        createOption: 'FromImage'
        caching: 'ReadWrite'
        deleteOption: 'Detach'
        managedDisk: {
          storageAccountType: osDiskType
          diskEncryptionSet: desRef
        }
      }
      // ReadOnly en datos con Premium SSD (< 4 TiB); None en log y en Premium SSD v2
      dataDisks: [
        for (d, i) in dataDisks: {
          lun: d.lun
          createOption: 'Attach'
          caching: d.role == 'data' && d.sku == 'Premium_LRS' && d.sizeGb < 4096 ? 'ReadOnly' : 'None'
          managedDisk: {
            id: disks[i].id
          }
        }
      ]
    }
    osProfile: {
      computerName: computerName
      adminUsername: adminUsername
      adminPassword: adminPassword
      allowExtensionOperations: true
      windowsConfiguration: {
        provisionVMAgent: true
        timeZone: timeZone
        patchSettings: {
          patchMode: 'AutomaticByPlatform'
          assessmentMode: 'AutomaticByPlatform'
          automaticByPlatformSettings: {
            bypassPlatformSafetyChecksOnUserSchedule: true
            rebootSetting: 'IfRequired'
          }
        }
      }
    }
    networkProfile: {
      networkInterfaces: [
        {
          id: nic.id
          properties: {
            deleteOption: 'Detach'
          }
        }
      ]
    }
    diagnosticsProfile: {
      bootDiagnostics: {
        enabled: true
      }
    }
  }
}

// Registro en la extensión SQL IaaS Agent; sin Automated Patching ni Automated Backup
resource sqlVm 'Microsoft.SqlVirtualMachine/sqlVirtualMachines@2023-10-01' = {
  name: name
  location: location
  tags: tags
  properties: {
    virtualMachineResourceId: vm.id
    sqlServerLicenseType: sqlLicenseType
    leastPrivilegeMode: 'Enabled'
    enableAutomaticUpgrade: true
    serverConfigurationsManagementSettings: {
      sqlConnectivityUpdateSettings: {
        connectivityType: 'PRIVATE'
        port: sqlPort
      }
      sqlInstanceSettings: {
        maxServerMemoryMB: sqlInstance.maxServerMemoryMb
        minServerMemoryMB: sqlInstance.?minServerMemoryMb ?? 0
        maxDop: sqlInstance.?maxDop ?? 0
        isOptimizeForAdHocWorkloadsEnabled: sqlInstance.?adHoc ?? false
        isIfiEnabled: sqlInstance.?ifi ?? true
        isLpimEnabled: sqlInstance.?lpim ?? true
        collation: sqlInstance.?collation ?? 'SQL_Latin1_General_CP1_CI_AS'
      }
      azureAdAuthenticationSettings: enableEntraAuthentication
        ? {
            clientId: entraIdentityClientId
          }
        : null
    }
    // La extensión crea los pools de Storage Spaces solo con Premium SSD
    storageConfigurationSettings: onlyPremiumSsd && hasDataAndLog
      ? {
          diskConfigurationType: 'NEW'
          storageWorkloadType: storageWorkloadType
          sqlSystemDbOnDataDisk: true
          sqlDataSettings: {
            defaultFilePath: dataPath
            luns: map(filter(dataDisks, d => d.role == 'data'), d => d.lun)
          }
          sqlLogSettings: {
            defaultFilePath: logPath
            luns: map(filter(dataDisks, d => d.role == 'log'), d => d.lun)
          }
          sqlTempDbSettings: {
            defaultFilePath: tempDb.path
            dataFileCount: tempDb.dataFileCount
            dataFileSize: tempDb.dataFileSizeMb
            dataGrowth: tempDb.dataGrowthMb
            logFileSize: tempDb.logFileSizeMb
            logGrowth: tempDb.logGrowthMb
          }
        }
      : null
  }
}

resource ama 'Microsoft.Compute/virtualMachines/extensions@2024-11-01' = if (!empty(dataCollectionRuleId ?? '')) {
  parent: vm
  name: 'AzureMonitorWindowsAgent'
  location: location
  properties: {
    publisher: 'Microsoft.Azure.Monitor'
    type: 'AzureMonitorWindowsAgent'
    typeHandlerVersion: '1.0'
    autoUpgradeMinorVersion: true
    enableAutomaticUpgrade: true
  }
  dependsOn: [
    sqlVm
  ]
}

resource dcra 'Microsoft.Insights/dataCollectionRuleAssociations@2023-03-11' = if (!empty(dataCollectionRuleId ?? '')) {
  name: 'dcra-${name}'
  scope: vm
  properties: {
    dataCollectionRuleId: dataCollectionRuleId
  }
  dependsOn: [
    ama
  ]
}

output vmId string = vm.id
output sqlVirtualMachineId string = sqlVm.id
output principalId string = vm.identity.principalId
output privateIp string = nic.properties.ipConfigurations[0].properties.privateIPAddress
```

`vm-sql-pro-01.bicepparam`:

```bicep
using 'sqlvm.bicep'

param name = 'vm-sql-pro-01'
param size = 'Standard_E8bds_v5'
param zone = '1'
param computerName = 'vmsqlpro01'

param imageOffer = 'sql2022-ws2022'
param imageSku = 'enterprise-gen2'
param sqlLicenseType = 'AHUB'
param osLicenseType = 'Windows_Server'
param timeZone = 'Romance Standard Time'

param subnetId = '<resourceId snet-sql-pro-z1>'
param adminUsername = '<admin-local>'

// La contraseña vive en Key Vault; el vault necesita enabledForTemplateDeployment = true
param adminPassword = az.getSecret(
  '<subscription-id>',
  '<rg-security-pro>',
  '<kv-workload-pro>',
  'vm-vm-sql-pro-01-admin'
)

param dataDisks = [
  {
    name: 'data01'
    role: 'data'
    lun: 0
    sizeGb: 1024
    sku: 'Premium_LRS'
  }
  {
    name: 'data02'
    role: 'data'
    lun: 1
    sizeGb: 1024
    sku: 'Premium_LRS'
  }
  {
    name: 'log01'
    role: 'log'
    lun: 2
    sizeGb: 1024
    sku: 'Premium_LRS'
  }
]
param storageWorkloadType = 'OLTP'

param sqlInstance = {
  maxServerMemoryMb: 57344 // ajustar con Memory\Available Bytes
  adHoc: true
}

// Entra: la identidad ya tiene Directory Readers (o los permisos de Graph)
param userAssignedIdentityIds = [
  '<resourceId id-sql-pro>'
]
param enableEntraAuthentication = true
param entraIdentityClientId = '<clientId id-sql-pro>'

param dataCollectionRuleId = '<resourceId dcr-sql-windows-pro>'

param tags = {
  environment: 'pro'
  workload: '<workload>'
  PatchGroup: 'sql-pro-wave2'
}
```

Despliegue:

```powershell
New-AzResourceGroupDeployment -ResourceGroupName "<rg-sql-pro>" `
    -TemplateParameterFile "vm-sql-pro-01.bicepparam" -Name "vm-sql-pro-01"
```

## Errores típicos

| Síntoma | Causa | Solución |
|---|---|---|
| `Microsoft.SqlVirtualMachine/SqlVirtualMachines ... was not found` al cambiar la licencia | La VM no está registrada en la extensión | Registrar la VM (o desplegar el recurso SQL virtual machine) |
| El registro falla en la región | La extensión no existe en esa región | Consultar las regiones con `Get-AzResourceProvider` |
| La configuración de almacenamiento no aparece o está en gris | Imagen que no es de Marketplace, Premium SSD v2, pool personalizado o TCP/IP deshabilitado | Preparar los volúmenes a mano; habilitar TCP/IP |
| Ampliar el pool no mejora el rendimiento | Las columnas se fijan al crear el pool | Recrear el pool con más discos o subir el nivel de rendimiento del disco |
| SQL Server no arranca tras reiniciar | tempdb en un disco efímero sin inicializar (p. ej. FXmdsv2) con SQL instalado a mano | Imagen de Marketplace, otra serie o script de inicialización |
| Latencia de escritura alta en el log | Caching ReadOnly o ReadWrite en el disco de log | Caching None (con el servicio de SQL parado) |
| Throttling de IOPS con discos de sobra | Límite sin caché de la VM | VM con más throughput, caching ReadOnly en datos o Premium SSD v2 |
| Parches fuera de la ventana | Automated Patching y Update Manager a la vez | Desactivar Automated Patching |
| No llegan los cumulative updates | Automated Patching no los instala o falta *Microsoft updates* | Update Manager con la clasificación *Updates* |
| Failover inesperado al parchear | Update Manager no conoce el grupo de disponibilidad | Ventanas distintas por réplica |
| `The selected managed identity does not have enough permissions for Microsoft Entra authentication` | Faltan permisos de Graph o Directory Readers | Conceder los permisos antes de activar |
| Los logins de Entra no conectan | Salida a `AzureActiveDirectory` bloqueada o SQL Server anterior a 2022 | NSG con salida 80 y 443; SQL Server 2022 o posterior |
| No se puede activar Azure Backup | Automated Backup activado | Desactivarlo antes |
| El assessment no aparece activado tras automatizarlo | La DCR y su asociación no siguen el nombre `<guid>_<región>_DCR_<n>` | Activarlo con la CLI o el portal |
| `Preflight validation failed` al activar el assessment | La ubicación del espacio de trabajo tiene espacios | Otro espacio de trabajo |
| `terraform plan` quiere recrear el recurso SQL virtual machine | Cambio de `sql_license_type`, collation, IFI o LPIM (ForceNew en el provider) | Cambiar la licencia con `Update-AzSqlVM` y alinear el código, o asumir la recreación |
| Datos corruptos tras recuperar discos geo-replicados | Datos y log en discos distintos con GRS | Solución de DR de SQL Server (grupo de disponibilidad, log shipping o copias) |
| La licencia vuelve a PAYG | La VM se recreó para meterla en un conjunto de disponibilidad o se borró el recurso SQL virtual machine | Volver a aplicar AHUB o DR |
