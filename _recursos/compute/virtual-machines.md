---
title: "Virtual Machines"
indice: compute
resumen: "Servidores Windows o Linux bajo demanda."
estado: documentado   # proximamente | en-curso | documentado
orden: 1
last_review: 2026-10-20
fuentes:
  - titulo: "Virtual machines in Azure (overview)"
    url: https://learn.microsoft.com/azure/virtual-machines/overview
  - titulo: "Sizes for virtual machines in Azure"
    url: https://learn.microsoft.com/azure/virtual-machines/sizes/overview
  - titulo: "'D' family general purpose VM size series"
    url: https://learn.microsoft.com/azure/virtual-machines/sizes/general-purpose/d-family
  - titulo: "Availability options for Azure Virtual Machines"
    url: https://learn.microsoft.com/azure/virtual-machines/availability
  - titulo: "Service Level Agreements (SLA) for Online Services"
    url: https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services
  - titulo: "Best practices for achieving high availability with Azure virtual machines and managed disks"
    url: https://learn.microsoft.com/azure/virtual-machines/disks-high-availability
  - titulo: "Azure managed disk types"
    url: https://learn.microsoft.com/azure/virtual-machines/disks-types
  - titulo: "Migrate your Standard HDD OS disks by September 08, 2028"
    url: https://learn.microsoft.com/azure/virtual-machines/disks-hdd-os-retirement
  - titulo: "Server-side encryption of Azure Disk Storage (encryption at host)"
    url: https://learn.microsoft.com/azure/virtual-machines/disk-encryption
  - titulo: "Use the Azure portal to enable end-to-end encryption using encryption at host"
    url: https://learn.microsoft.com/azure/virtual-machines/disks-enable-host-based-encryption-portal
  - titulo: "Migrate from Azure Disk Encryption to encryption at host"
    url: https://learn.microsoft.com/azure/virtual-machines/disk-encryption-migrate
  - titulo: "Trusted Launch for Azure virtual machines"
    url: https://learn.microsoft.com/azure/virtual-machines/trusted-launch
  - titulo: "Default outbound access in Azure"
    url: https://learn.microsoft.com/azure/virtual-network/ip-services/default-outbound-access
  - titulo: "Sign in to Windows virtual machine in Azure using Microsoft Entra ID"
    url: https://learn.microsoft.com/entra/identity/devices/howto-vm-sign-in-azure-ad-windows
  - titulo: "Sign in to a Linux virtual machine in Azure by using Microsoft Entra ID and OpenSSH"
    url: https://learn.microsoft.com/entra/identity/devices/howto-vm-sign-in-azure-ad-linux
  - titulo: "Azure Monitor agent: Resource Manager templates"
    url: https://learn.microsoft.com/azure/azure-monitor/agents/resource-manager-agent
  - titulo: "Architecture best practices for Azure Virtual Machines and scale sets (WAF)"
    url: https://learn.microsoft.com/azure/well-architected/service-guides/virtual-machines
  - titulo: "Azure Virtual Machines baseline architecture"
    url: https://learn.microsoft.com/azure/architecture/virtual-machines/baseline
  - titulo: "Best practices for virtual machine cost optimization"
    url: https://learn.microsoft.com/azure/virtual-machines/cost-optimization-best-practices
  - titulo: "Quick tips to optimize virtual machines on Azure (Spot)"
    url: https://learn.microsoft.com/startups/build/cost-mgmt/vm-optimization
  - titulo: "Azure Spot Virtual Machines"
    url: https://learn.microsoft.com/azure/virtual-machines/spot-vms
  - titulo: "How the Azure reservation discount is applied to virtual machines"
    url: https://learn.microsoft.com/azure/cost-management-billing/manage/understand-vm-reservation-charges
  - titulo: "What are savings plans?"
    url: https://learn.microsoft.com/azure/cost-management-billing/savings-plan/savings-plan-overview
  - titulo: "On-demand Capacity Reservation"
    url: https://learn.microsoft.com/azure/virtual-machines/capacity-reservation-overview
  - titulo: "azurerm_windows_virtual_machine"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/windows_virtual_machine
  - titulo: "azurerm_linux_virtual_machine"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/linux_virtual_machine
  - titulo: "Microsoft.Compute virtualMachines (plantillas ARM/Bicep)"
    url: https://learn.microsoft.com/azure/templates/microsoft.compute/virtualmachines
  - titulo: "Módulo Terraform Compute/Compute/modules/windows_virtual_machine"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Compute/Compute/modules/windows_virtual_machine
  - titulo: "Módulo Terraform Compute/Compute/modules/linux_virtual_machine"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Compute/Compute/modules/linux_virtual_machine
  - titulo: "Módulo Terraform Compute/Compute/modules/managed_disk"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Compute/Compute/modules/managed_disk
  - titulo: "Módulo Terraform Compute/Compute/modules/virtual_machine_data_disk_attachment"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Compute/Compute/modules/virtual_machine_data_disk_attachment
  - titulo: "Módulo Terraform Compute/Compute/modules/virtual_machine_extension"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Compute/Compute/modules/virtual_machine_extension
  - titulo: "Módulo Terraform Compute/VirtualMachine"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Compute/VirtualMachine
  - titulo: "Módulo Terraform Compute/VMExtension-AzureMonitorAgent"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Compute/VMExtension-AzureMonitorAgent
---

Las **máquinas virtuales** son el IaaS de Azure: tú gestionas el sistema operativo, los parches, el software y los datos, y Azure el hardware, la virtualización y la red física. Son la opción natural para migrar servidores tal cual (*lift & shift*), para software que no existe como PaaS o que necesita control del SO, y para cargas con licencias atadas al servidor.

Una VM nunca va sola. Esta ficha es el centro de un conjunto:

- Discos: [Managed Disks](/recursos/storage/managed-disks/).
- Escalado horizontal: [VM Scale Sets](/recursos/compute/vm-scale-sets/).
- Operación: [Azure Backup](/recursos/backups-update/azure-backup/), [Azure Site Recovery](/recursos/backups-update/azure-site-recovery/) y [Azure Update Manager](/recursos/backups-update/azure-update-manager/).

## Qué es y cuándo usarlo

### VM o PaaS

| Necesidad | Mejor opción |
|---|---|
| Migrar un servidor sin tocar la aplicación | **VM** |
| Software que exige acceso al SO, drivers o agentes propios | **VM** |
| Varias instancias idénticas que escalan solas | [VM Scale Sets](/recursos/compute/vm-scale-sets/) |
| Web o API propia | App Service, Container Apps o Functions |
| Base de datos | Azure SQL, PostgreSQL o MySQL gestionados (o SQL Server en VM si hace falta el motor completo) |
| Escritorios | Azure Virtual Desktop (también VMs, como [session hosts](/recursos/avd/session-hosts/)) |

Con una VM, **el parcheo, la copia, la monitorización y el endurecimiento del SO son tuyos**.

### Elegir el tamaño

El nombre del tamaño se lee así: `Standard_D4as_v6` = familia **D** (propósito general), **4** vCPU, **a** (AMD), **s** (admite Premium SSD), generación **v6**.

| Familia | Para qué |
|---|---|
| **B** | Cargas con picos ocasionales (desarrollo, pruebas, servidores poco usados) |
| **D** | Propósito general: la mayoría de servidores de aplicación |
| **E** | Más memoria por vCPU: bases de datos, cachés |
| **F** | Más CPU por memoria: cálculo, servidores web con mucho tráfico |
| **L** | Almacenamiento local NVMe |
| **M** | Memoria muy alta (SAP HANA) |
| **N** | GPU |

Letras habituales: **a** (AMD), **p** (Arm, Azure Cobalt), **d** (disco temporal local), **l** (menos memoria), **s** (Premium SSD).

En propósito general, las series v6 (AMD EPYC 4.ª generación o Cobalt 100) son la generación actual. Las variantes sin **d** no traen disco temporal y salen más baratas si no se necesita.

### Disponibilidad y SLA

| Despliegue | SLA de conectividad |
|---|---|
| **Dos o más VMs en zonas distintas** | **99,99 %** |
| Dos o más VMs en un conjunto de disponibilidad | 99,95 % |
| VM única con Premium SSD, Premium SSD v2 o Ultra en todos sus discos | 99,9 % |
| VM única con Standard SSD o HDD | Menor |
| Spot | Sin SLA |

- **Una sola VM no es alta disponibilidad**: para 99,99 % hacen falta al menos dos, en zonas distintas, detrás de un balanceador.
- Los conjuntos de disponibilidad no cubren la caída de una zona. Microsoft ofrece una migración (en preview) a scale sets flexibles.
- Para cargas de una sola VM, discos ZRS mantienen los datos si cae la zona.

### Discos

| Tipo | Uso | ¿Disco de SO? |
|---|---|---|
| **Premium SSD** | Producción | Sí |
| **Premium SSD v2** | Producción con IOPS y throughput ajustables | No |
| Ultra Disk | Bases de datos muy exigentes | No |
| Standard SSD | Web poco usada, desarrollo | Sí |
| Standard HDD | Copias y datos fríos | **Como SO se retira el 8 de septiembre de 2028** |

### Seguridad de la VM

| Control | Qué aporta | Estado por defecto |
|---|---|---|
| **Trusted Launch** (Secure Boot + vTPM) | Protección contra bootkits y rootkits; atestación | Por defecto en portal, PowerShell y CLI; en ARM, Bicep y Terraform hay que declararlo (o API 2025-11-01+) |
| **Cifrado en el host** | Cifra disco temporal y cachés; los datos viajan cifrados al almacenamiento | Desactivado; requiere registrar `EncryptionAtHost` en la suscripción |
| SSE con claves de plataforma | Cifrado de discos en reposo | Siempre activo |
| SSE con CMK (Disk Encryption Set) | Control de la clave | Opcional |
| **Azure Disk Encryption** | BitLocker/DM-Crypt dentro de la VM | **Se retira el 15 de septiembre de 2028**: las VMs con ADE no arrancarán sus discos cifrados tras un reinicio |
| Sin IP pública | La VM no es escaneable desde Internet | Bastion o red privada para administrar |
| Identidad gestionada | Acceso a Key Vault, Storage, etc. sin secretos | Opcional |
| Login con Entra ID | RBAC (*Virtual Machine Administrator/User Login*), MFA y acceso condicional en el inicio de sesión | Opcional; en Windows une la VM a Entra ID (incompatible con unirla a un dominio AD) |

El cifrado en el host **no puede activarse** en VMs que tengan o hayan tenido ADE. Para pasar de ADE a cifrado en el host hay que crear discos y VMs nuevos.

### Salida a Internet

- Desde el 31 de marzo de 2026, las **VNets nuevas** (API posterior) crean **subredes privadas**: sin salida por defecto.
- Las existentes no cambian, pero la IP de salida por defecto no es tuya y puede cambiar.
- **Windows Update y la activación de Windows necesitan salida explícita**: NAT Gateway, firewall con UDR o balanceador con reglas de salida.

### Operación

| Necesidad | Servicio |
|---|---|
| Copias | [Azure Backup](/recursos/backups-update/azure-backup/) (política Enhanced para Trusted Launch) |
| Réplica a otra región | [Azure Site Recovery](/recursos/backups-update/azure-site-recovery/) |
| Parches | [Azure Update Manager](/recursos/backups-update/azure-update-manager/) con Customer Managed Schedules |
| Métricas y logs | Azure Monitor Agent + Data Collection Rules (VM insights) |
| Amenazas y vulnerabilidades | Defender for Servers |
| Acceso administrativo | Bastion o JIT; login con Entra ID |
| Capacidad garantizada | Capacity Reservation (se paga aparte) |

### Cómo se factura

| Concepto | Detalle |
|---|---|
| Cómputo | Mientras la VM está asignada; **una VM detenida desde el SO sigue facturándose**, una *desasignada* no |
| Licencia | Windows, SQL Server, RHEL y SLES se suman al cómputo salvo Azure Hybrid Benefit |
| Discos | Por tamaño aprovisionado (y rendimiento en Premium SSD v2 y Ultra), aunque la VM esté parada |
| Red | IPs públicas, salida de datos, balanceadores, NAT Gateway |
| Copias, monitorización y seguridad | Cada servicio factura aparte |

Formas de ahorrar:

| Mecanismo | Ahorro | Compromiso |
|---|---|---|
| **Reservas** (1 o 3 años) | Hasta un 72 % sobre pago por uso | Tamaño y región concretos; las horas no usadas se pierden |
| **Savings plan for compute** (1 o 3 años) | Descuento sobre pago por uso, con más flexibilidad que una reserva | Gasto por hora comprometido en cómputo elegible (VMs, App Service, Functions Premium, Container Apps…) |
| **Azure Hybrid Benefit** | Licencias de Windows Server/SQL Server o suscripciones Linux propias | Software Assurance o suscripción |
| **Spot** | Hasta un 90 % | Expulsión con 30 segundos de aviso; sin SLA |
| B-series, apagado programado | Desarrollo y pruebas | Rendimiento por créditos |

### Qué escenario recomiendo

| Escenario del cliente | Diseño | Por qué |
|---|---|---|
| Aplicación crítica en VMs | Dos o más VMs en zonas distintas + balanceador + Premium SSD | 99,99 % |
| Servidor único que no se puede duplicar | Premium SSD (o ZRS) + Backup + ASR | 99,9 % y recuperación ante la caída de la zona o la región |
| Servidores Windows con licencias propias | Azure Hybrid Benefit + reservas a 3 años | Licencia y cómputo más baratos |
| Desarrollo y pruebas | B-series o D pequeñas, Standard SSD, apagado programado | Coste mínimo |
| Cargas por lotes interrumpibles | Spot con política *Delete* | Hasta un 90 % menos |
| Muchas instancias idénticas | VM Scale Sets flexibles | Escalado, zonas y reparación automáticos |
| VMs heredadas con ADE | Migrar a cifrado en el host antes de 2028 | ADE se retira |
| Requisitos de confidencialidad en uso | Confidential VMs | Memoria cifrada y atestación |

### Datos que conviene llevar a la reunión

- **Una VM no es alta disponibilidad**: 99,99 % exige dos o más en zonas distintas.
- **Trusted Launch y cifrado en el host** son la línea base; con IaC hay que declararlos.
- **ADE se retira en septiembre de 2028** y no se puede convertir en el sitio: hay que planificar la migración.
- **Standard HDD como disco de SO también se retira en 2028.**
- **Las VNets nuevas no tienen salida a Internet por defecto**: Windows Update necesita NAT Gateway o firewall.
- **Detener no es desasignar**: una VM parada desde el SO se sigue pagando.
- **Reservas + Hybrid Benefit** es el mayor ahorro para servidores 24×7.
- **El parcheo, las copias y la monitorización son responsabilidad del cliente**: Update Manager, Backup y AMA desde el primer día.

## Decisiones de diseño

| Decisión | Lo que aplico | Por qué |
|---|---|---|
| Módulos | Submódulos de `Compute/Compute/modules` llamados desde el root con `for_each` | Son los únicos compatibles con azurerm 4.x y exponen todos los atributos |
| Zona | Obligatoria salvo justificación; discos en la misma zona | SLA y aislamiento de fallos |
| Seguridad del arranque | Trusted Launch (Secure Boot + vTPM) siempre | Línea base de Microsoft |
| Cifrado | Cifrado en el host por defecto; CMK opcional con Disk Encryption Set | Cifrado de extremo a extremo sin ADE |
| Red | NIC privada, sin IP pública ni reenvío; NSG en la subred | Superficie de ataque mínima |
| Credenciales | Windows: contraseña aleatoria guardada en Key Vault; Linux: solo clave SSH | Sin secretos en el código ni contraseñas en Linux |
| Identidad | Identidad del sistema siempre; de usuario opcional | AMA, login con Entra ID y acceso a otros servicios |
| Parches | `AutomaticByPlatform` + bypass + evaluación periódica | Listas para los calendarios de Update Manager |
| Monitorización | AMA (actualización automática) + asociación a DCR | Sin agente de Log Analytics (retirado) |
| Discos de datos | Premium SSD, sin acceso público ni exportación (`DenyAll`) | Rendimiento y protección frente a exfiltración por SAS |
| Diagnóstico de arranque | Almacenamiento gestionado | Sin cuenta de almacenamiento que gobernar |
| Borrado | El provider no borra el disco del SO al destruir la VM | Evita perder datos en un `destroy` |

Alineación con el Well-Architected Framework:

- **Fiabilidad**: zonas, Premium SSD, copias y réplica en sus fichas.
- **Seguridad**: Trusted Launch, cifrado en el host, sin IP pública, Entra ID, secretos en Key Vault.
- **Coste**: tamaños v6 sin disco local cuando no hace falta, Hybrid Benefit y reservas.
- **Excelencia operativa**: todo en IaC, parcheo y monitorización desde el despliegue.
- **Rendimiento**: red acelerada y tipo de disco por carga.

## Módulo de Terraform

### Los módulos del repositorio

Hay tres caminos en `Compute/` y no todos sirven:

| Módulo | Estado |
|---|---|
| [`Compute/Compute/modules/windows_virtual_machine`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Compute/Compute/modules/windows_virtual_machine) y [`linux_virtual_machine`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Compute/Compute/modules/linux_virtual_machine) | **Utilizables**: envoltorios finos con todos los atributos de azurerm 4.x |
| [`managed_disk`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Compute/Compute/modules/managed_disk), [`virtual_machine_data_disk_attachment`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Compute/Compute/modules/virtual_machine_data_disk_attachment), [`virtual_machine_extension`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Compute/Compute/modules/virtual_machine_extension) | **Utilizables** |
| `Compute/Compute` (raíz) | Pensado como root: declara su propio bloque `provider`, así que no se puede llamar con `for_each` desde otro root |
| [`Compute/VirtualMachine`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Compute/VirtualMachine) | **No funciona con azurerm 4.x** |
| `Compute/virtual-machine-linux` | Heredado: sin `versions.tf`, NIC propia y sin Trusted Launch |
| [`Compute/VMExtension-AzureMonitorAgent`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Compute/VMExtension-AzureMonitorAgent) | **Falla si se pasa un DCE** |

Detalle de lo que no sirve:

- **`Compute/VirtualMachine`** usa `enable_accelerated_networking` y `enable_ip_forwarding` en la NIC, que azurerm 4.0 renombró a `accelerated_networking_enabled` e `ip_forwarding_enabled`. Su `versions.tf` admite `< 5.0.0`, pero falla con cualquier 4.x. Además:
  - `secure_boot_enabled`, `vtpm_enabled` y `encryption_at_host_enabled` valen `false` por defecto.
  - `disable_password_authentication = false` en Linux por defecto.
  - Si no se pasa `name`, se genera con `environment = "dev"`.
- **`VMExtension-AzureMonitorAgent`** pone `data_collection_rule_id` y `data_collection_endpoint_id` en la misma asociación. El provider exige exactamente uno de los dos.
- **Los submódulos `windows_virtual_machine`/`linux_virtual_machine`**:
  - No publican la identidad (`principal_id`): en la ficha se lee con `data "azurerm_virtual_machine"`.
  - No tienen validaciones ni valores por defecto seguros. Todo lo seguro lo pone el root.
  - `virtual-machine-linux` y `AzureVirtualDesktop/SessionHost` también usan `enable_accelerated_networking`.

### Estructura en el proyecto

```txt
/
├── providers.tf          # azurerm >= 4.64.0, random
├── virtual_machines.tf   # NIC, contraseña en Key Vault, VMs, discos, extensiones, DCR
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
      # >= 4.0: nombres de argumentos de la NIC (accelerated_networking_enabled, ip_forwarding_enabled).
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

### `virtual_machines.tf`

```hcl
# =============================================================================
# Máquinas virtuales Windows y Linux seguras por defecto:
# zona, Trusted Launch, cifrado en el host, sin IP pública, identidad gestionada,
# Customer Managed Schedules (Update Manager), Azure Monitor Agent + DCR y login con Entra ID opcional
#
# DEPENDENCY: grupos de recursos y subredes creados; NSG asociado a la subred (no a la NIC)
# DEPENDENCY: salida explícita a Internet en la subred (NAT Gateway o firewall con UDR): las VNets
#             nuevas tienen subredes privadas por defecto y Windows Update/activación la necesitan
# DEPENDENCY: característica Microsoft.Compute/EncryptionAtHost registrada en la suscripción
# DEPENDENCY: Key Vault con RBAC para la contraseña de Windows; la identidad de Terraform
#             necesita "Key Vault Secrets Officer" y alcance de red al vault
# DEPENDENCY: Disk Encryption Set (CMK) y Data Collection Rule creados si se usan
# =============================================================================

variable "virtual_machines" {
  description = "Máquinas virtuales (clave = nombre del recurso)."
  type = map(object({
    resource_group_name = string
    location            = string
    os_type             = string           # Windows | Linux
    size                = string           # p. ej. Standard_D4as_v6
    zone                = optional(string) # 1 | 2 | 3; null solo con justificación
    computer_name       = optional(string) # Windows: 15 caracteres como máximo

    # Imagen: Marketplace o Azure Compute Gallery (exactamente una)
    source_image_reference = optional(object({
      publisher = string
      offer     = string
      sku       = string
      version   = optional(string, "latest")
    }))
    source_image_id = optional(string)
    license_type    = optional(string) # Windows_Server (Azure Hybrid Benefit), RHEL_BYOS, SLES_BYOS

    # Red: una NIC privada; sin IP pública ni reenvío de IP
    subnet_id                      = string
    private_ip_address             = optional(string) # null = dinámica
    accelerated_networking_enabled = optional(bool, true)

    # Acceso administrativo
    admin_username = string
    ssh_public_key = optional(string)    # Linux (obligatoria)
    key_vault_id   = optional(string)    # Windows: dónde se guarda la contraseña generada
    entra_login    = optional(bool, false) # AADLoginForWindows / AADSSHLoginForLinux (Windows: incompatible con unión a dominio AD)

    os_disk = optional(object({
      storage_account_type = optional(string, "Premium_LRS") # Premium_LRS | Premium_ZRS | StandardSSD_LRS | StandardSSD_ZRS
      disk_size_gb         = optional(number)
      caching              = optional(string, "ReadWrite")
    }), {})

    data_disks = optional(map(object({
      lun                  = number
      disk_size_gb         = number
      storage_account_type = optional(string, "Premium_LRS")
      caching              = optional(string, "ReadOnly") # None para discos de log
    })), {})

    disk_encryption_set_id     = optional(string) # CMK (SSE) para SO y datos
    encryption_at_host_enabled = optional(bool, true)

    user_assigned_identity_ids    = optional(list(string), []) # además de la identidad del sistema
    capacity_reservation_group_id = optional(string)
    timezone                      = optional(string) # Windows, p. ej. "Romance Standard Time"

    data_collection_rule_id = optional(string) # AMA + asociación a la DCR

    tags = optional(map(string), {})
  }))
  default = {}

  validation {
    condition     = alltrue([for k, v in var.virtual_machines : contains(["Windows", "Linux"], v.os_type)])
    error_message = "os_type debe ser Windows o Linux."
  }

  validation {
    condition = alltrue([
      for k, v in var.virtual_machines : (v.source_image_reference == null) != (v.source_image_id == null)
    ])
    error_message = "Indica exactamente uno: source_image_reference o source_image_id."
  }

  validation {
    condition = alltrue([
      for k, v in var.virtual_machines :
      v.os_type == "Linux" ? v.ssh_public_key != null : v.key_vault_id != null
    ])
    error_message = "Linux necesita ssh_public_key; Windows necesita key_vault_id para guardar la contraseña."
  }

  validation {
    condition = alltrue([
      for k, v in var.virtual_machines :
      v.os_type == "Linux" || length(coalesce(v.computer_name, k)) <= 15
    ])
    error_message = "En Windows el nombre de equipo tiene 15 caracteres como máximo: usa computer_name."
  }

  validation {
    condition     = alltrue([for k, v in var.virtual_machines : v.zone == null || contains(["1", "2", "3"], coalesce(v.zone, "x"))])
    error_message = "zone debe ser 1, 2 o 3."
  }

  validation {
    condition = alltrue([
      for k, v in var.virtual_machines :
      contains(["Premium_LRS", "Premium_ZRS", "StandardSSD_LRS", "StandardSSD_ZRS"], v.os_disk.storage_account_type)
    ])
    error_message = "Disco del SO: Premium o Standard SSD (Standard HDD como SO se retira en 2028; Ultra y Premium SSD v2 no sirven de SO)."
  }

  validation {
    condition = alltrue(flatten([
      for k, v in var.virtual_machines : [
        for dk, d in v.data_disks :
        contains(["Premium_LRS", "Premium_ZRS", "PremiumV2_LRS", "UltraSSD_LRS", "StandardSSD_LRS", "StandardSSD_ZRS", "Standard_LRS"], d.storage_account_type) &&
        contains(["None", "ReadOnly", "ReadWrite"], d.caching)
      ]
    ]))
    error_message = "Tipo de disco de datos o caching no válido."
  }

  validation {
    condition = alltrue([
      for k, v in var.virtual_machines :
      length(distinct([for d in values(v.data_disks) : d.lun])) == length(v.data_disks)
    ])
    error_message = "Los LUN de los discos de datos no pueden repetirse."
  }

  validation {
    condition = alltrue([
      for k, v in var.virtual_machines :
      v.license_type == null || contains(["Windows_Server", "Windows_Client", "RHEL_BYOS", "SLES_BYOS", "None"], coalesce(v.license_type, "None"))
    ])
    error_message = "license_type no válido."
  }
}

# -----------------------------------------------------------------------------
# NIC privada (sin IP pública, sin reenvío; el NSG va en la subred)
# -----------------------------------------------------------------------------
resource "azurerm_network_interface" "this" {
  for_each = var.virtual_machines

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
# Contraseña de Windows: generada y guardada en Key Vault (nunca en tfvars)
# -----------------------------------------------------------------------------
resource "random_password" "windows_admin" {
  for_each = { for k, v in var.virtual_machines : k => v if v.os_type == "Windows" }

  length           = 24
  special          = true
  override_special = "!@#$%*()-_=+[]{}:?"
  min_lower        = 2
  min_upper        = 2
  min_numeric      = 2
  min_special      = 2
}

resource "azurerm_key_vault_secret" "windows_admin" {
  for_each = random_password.windows_admin

  name         = "vm-${each.key}-admin"
  value        = each.value.result
  key_vault_id = var.virtual_machines[each.key].key_vault_id
  content_type = "VM local administrator (${var.virtual_machines[each.key].admin_username})"
}

# -----------------------------------------------------------------------------
# VMs (módulos Compute/Compute/modules del repositorio)
# -----------------------------------------------------------------------------
module "windows_virtual_machine" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Compute/Compute/modules/windows_virtual_machine?ref=main"
  for_each = { for k, v in var.virtual_machines : k => v if v.os_type == "Windows" }

  windows_virtual_machine_name = each.key
  computer_name                = coalesce(each.value.computer_name, each.key)
  resource_group_name          = each.value.resource_group_name
  location                     = each.value.location
  size                         = each.value.size
  zone                         = each.value.zone
  network_interface_ids        = [azurerm_network_interface.this[each.key].id]

  admin_username = each.value.admin_username
  admin_password = random_password.windows_admin[each.key].result

  source_image_reference = each.value.source_image_reference
  source_image_id        = each.value.source_image_id
  license_type           = each.value.license_type
  timezone               = each.value.timezone

  # Trusted Launch + cifrado de extremo a extremo
  secure_boot_enabled        = true
  vtpm_enabled               = true
  encryption_at_host_enabled = each.value.encryption_at_host_enabled

  # Update Manager: Customer Managed Schedules + evaluación periódica
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
    caching                = each.value.os_disk.caching
    storage_account_type   = each.value.os_disk.storage_account_type
    disk_size_gb           = each.value.os_disk.disk_size_gb
    disk_encryption_set_id = each.value.disk_encryption_set_id
  }

  boot_diagnostics = {} # almacenamiento gestionado por Azure

  tags = merge(var.tags, each.value.tags)
}

module "linux_virtual_machine" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Compute/Compute/modules/linux_virtual_machine?ref=main"
  for_each = { for k, v in var.virtual_machines : k => v if v.os_type == "Linux" }

  linux_virtual_machine_name = each.key
  computer_name              = coalesce(each.value.computer_name, each.key)
  resource_group_name        = each.value.resource_group_name
  location                   = each.value.location
  size                       = each.value.size
  zone                       = each.value.zone
  network_interface_ids      = [azurerm_network_interface.this[each.key].id]

  admin_username                  = each.value.admin_username
  disable_password_authentication = true
  admin_ssh_keys = [{
    username   = each.value.admin_username
    public_key = each.value.ssh_public_key
  }]

  source_image_reference = each.value.source_image_reference
  source_image_id        = each.value.source_image_id
  license_type           = each.value.license_type

  secure_boot_enabled        = true
  vtpm_enabled               = true
  encryption_at_host_enabled = each.value.encryption_at_host_enabled

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
    caching                = each.value.os_disk.caching
    storage_account_type   = each.value.os_disk.storage_account_type
    disk_size_gb           = each.value.os_disk.disk_size_gb
    disk_encryption_set_id = each.value.disk_encryption_set_id
  }

  boot_diagnostics = {}

  tags = merge(var.tags, each.value.tags)
}

# -----------------------------------------------------------------------------
# Discos de datos: disco + conexión (misma zona que la VM)
# -----------------------------------------------------------------------------
module "data_disk" {
  source = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Compute/Compute/modules/managed_disk?ref=main"
  for_each = {
    for d in flatten([
      for k, v in var.virtual_machines : [
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
  zone                          = endswith(each.value.disk.storage_account_type, "_ZRS") ? null : each.value.vm.zone
  create_option                 = "Empty"
  storage_account_type          = each.value.disk.storage_account_type
  disk_size_gb                  = each.value.disk.disk_size_gb
  disk_encryption_set_id        = each.value.vm.disk_encryption_set_id
  public_network_access_enabled = false
  network_access_policy         = "DenyAll" # sin exportación ni importación por SAS

  tags = merge(var.tags, each.value.vm.tags)
}

module "data_disk_attachment" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Compute/Compute/modules/virtual_machine_data_disk_attachment?ref=main"
  for_each = module.data_disk

  managed_disk_id    = each.value.id
  virtual_machine_id = try(module.windows_virtual_machine[split("/", each.key)[0]].id, module.linux_virtual_machine[split("/", each.key)[0]].id)
  lun                = var.virtual_machines[split("/", each.key)[0]].data_disks[split("/", each.key)[1]].lun
  caching            = var.virtual_machines[split("/", each.key)[0]].data_disks[split("/", each.key)[1]].caching
}

# -----------------------------------------------------------------------------
# Extensiones: Azure Monitor Agent y login con Entra ID
# -----------------------------------------------------------------------------
module "vm_extension" {
  source = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Compute/Compute/modules/virtual_machine_extension?ref=main"
  for_each = {
    for e in flatten([
      for k, v in var.virtual_machines : concat(
        v.data_collection_rule_id == null ? [] : [{
          key       = "${k}/ama"
          vm        = k
          name      = v.os_type == "Windows" ? "AzureMonitorWindowsAgent" : "AzureMonitorLinuxAgent"
          publisher = "Microsoft.Azure.Monitor"
          type      = v.os_type == "Windows" ? "AzureMonitorWindowsAgent" : "AzureMonitorLinuxAgent"
          auto      = true
        }],
        v.entra_login ? [{
          key       = "${k}/entra"
          vm        = k
          name      = v.os_type == "Windows" ? "AADLoginForWindows" : "AADSSHLoginForLinux"
          publisher = "Microsoft.Azure.ActiveDirectory"
          type      = v.os_type == "Windows" ? "AADLoginForWindows" : "AADSSHLoginForLinux"
          auto      = false
        }] : []
      )
    ]) : e.key => e
  }

  virtual_machine_extension_name = each.value.name
  virtual_machine_id             = try(module.windows_virtual_machine[each.value.vm].id, module.linux_virtual_machine[each.value.vm].id)
  publisher                      = each.value.publisher
  type                           = each.value.type
  type_handler_version           = "1.0"
  auto_upgrade_minor_version     = true
  automatic_upgrade_enabled      = each.value.auto

  tags = merge(var.tags, var.virtual_machines[each.value.vm].tags)
}

# Asociación a la DCR (una por VM; el endpoint DCE, si se usa, va en otra asociación)
resource "azurerm_monitor_data_collection_rule_association" "this" {
  for_each = { for k, v in var.virtual_machines : k => v if v.data_collection_rule_id != null }

  name                    = "dcra-${each.key}"
  target_resource_id      = try(module.windows_virtual_machine[each.key].id, module.linux_virtual_machine[each.key].id)
  data_collection_rule_id = each.value.data_collection_rule_id

  depends_on = [module.vm_extension]
}

# El módulo no publica la identidad: se lee después de crear la VM
data "azurerm_virtual_machine" "this" {
  for_each = var.virtual_machines

  name                = each.key
  resource_group_name = each.value.resource_group_name

  depends_on = [module.windows_virtual_machine, module.linux_virtual_machine]
}

# -----------------------------------------------------------------------------
# Salidas
# -----------------------------------------------------------------------------
output "virtual_machine_ids" {
  description = "IDs de las VMs."
  value       = merge({ for k, m in module.windows_virtual_machine : k => m.id }, { for k, m in module.linux_virtual_machine : k => m.id })
}

output "virtual_machine_private_ips" {
  description = "IP privada principal de cada VM."
  value       = { for k, n in azurerm_network_interface.this : k => n.private_ip_address }
}

output "virtual_machine_principal_ids" {
  description = "principalId de la identidad del sistema (para RBAC sobre otros recursos)."
  value       = { for k, d in data.azurerm_virtual_machine.this : k => try(d.identity[0].principal_id, null) }
}

output "windows_admin_secret_ids" {
  description = "Secretos de Key Vault con la contraseña local de cada VM Windows."
  value       = { for k, s in azurerm_key_vault_secret.windows_admin : k => s.versionless_id }
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

virtual_machines = {
  # Servidor de aplicación Windows en la zona 1, con Azure Hybrid Benefit
  "vm-app-pro-01" = {
    resource_group_name = "<rg-app-pro>"
    location            = "<region>"
    os_type             = "Windows"
    size                = "Standard_D4as_v6"
    zone                = "1"
    computer_name       = "vmapppro01"

    source_image_reference = {
      publisher = "MicrosoftWindowsServer"
      offer     = "WindowsServer"
      sku       = "2025-datacenter-azure-edition"
    }
    license_type = "Windows_Server"
    timezone     = "Romance Standard Time"

    subnet_id      = "<resourceId snet-app-pro>"
    admin_username = "<admin-local>"
    key_vault_id   = "<resourceId kv-<workload>-pro>"

    os_disk = {
      storage_account_type = "Premium_LRS"
    }

    data_disks = {
      data01 = {
        lun          = 0
        disk_size_gb = 256
      }
    }

    data_collection_rule_id = "<resourceId dcr-vm-windows-pro>"

    tags = {
      PatchGroup = "pro-wave1"
    }
  }

  # Segundo nodo en la zona 2 (alta disponibilidad con balanceador)
  "vm-app-pro-02" = {
    resource_group_name = "<rg-app-pro>"
    location            = "<region>"
    os_type             = "Windows"
    size                = "Standard_D4as_v6"
    zone                = "2"
    computer_name       = "vmapppro02"

    source_image_reference = {
      publisher = "MicrosoftWindowsServer"
      offer     = "WindowsServer"
      sku       = "2025-datacenter-azure-edition"
    }
    license_type = "Windows_Server"
    timezone     = "Romance Standard Time"

    subnet_id      = "<resourceId snet-app-pro>"
    admin_username = "<admin-local>"
    key_vault_id   = "<resourceId kv-<workload>-pro>"

    data_disks = {
      data01 = {
        lun          = 0
        disk_size_gb = 256
      }
    }

    data_collection_rule_id = "<resourceId dcr-vm-windows-pro>"

    tags = {
      PatchGroup = "pro-wave2"
    }
  }

  # Linux con login de Entra ID y CMK
  "vm-api-pro-01" = {
    resource_group_name = "<rg-app-pro>"
    location            = "<region>"
    os_type             = "Linux"
    size                = "Standard_D2as_v6"
    zone                = "1"

    source_image_reference = {
      publisher = "Canonical"
      offer     = "ubuntu-24_04-lts"
      sku       = "server"
    }

    subnet_id      = "<resourceId snet-app-pro>"
    admin_username = "azureadmin"
    ssh_public_key = "<clave pública SSH (ssh-rsa/ssh-ed25519 ...)>"
    entra_login    = true

    disk_encryption_set_id = "<resourceId des-<workload>-pro>"

    data_collection_rule_id = "<resourceId dcr-vm-linux-pro>"

    tags = {
      PatchGroup = "pro-wave1"
    }
  }
}
```

### Despliegue y comprobación

```powershell
# Requisito del cifrado en el host (una vez por suscripción)
Register-AzProviderFeature -FeatureName "EncryptionAtHost" -ProviderNamespace "Microsoft.Compute"
Get-AzProviderFeature -FeatureName "EncryptionAtHost" -ProviderNamespace "Microsoft.Compute"

terraform init
terraform plan -var-file="env/pro.tfvars" -out="pro.tfplan"
terraform apply "pro.tfplan"

# Seguridad y parcheo de las VMs del grupo de recursos
Get-AzVM -ResourceGroupName "<rg-app-pro>" | ForEach-Object {
    [PSCustomObject]@{
        Name             = $_.Name
        Zone             = ($_.Zones -join ",")
        SecurityType     = $_.SecurityProfile.SecurityType
        EncryptionAtHost = $_.SecurityProfile.EncryptionAtHost
        PatchMode        = if ($_.OSProfile.WindowsConfiguration) { $_.OSProfile.WindowsConfiguration.PatchSettings.PatchMode } else { $_.OSProfile.LinuxConfiguration.PatchSettings.PatchMode }
    }
}

# Rol para iniciar sesión con Entra ID (no lo da Owner ni Contributor)
New-AzRoleAssignment -ObjectId "<objectId grupo de administradores>" `
    -RoleDefinitionName "Virtual Machine Administrator Login" `
    -Scope (Get-AzVM -ResourceGroupName "<rg-app-pro>" -Name "vm-api-pro-01").Id

# VMs con IP pública, sin zona o sin cifrado en el host (Resource Graph)
Search-AzGraph -Query @"
resources
| where type =~ 'microsoft.compute/virtualmachines'
| extend zone = tostring(zones[0]), eah = tobool(properties.securityProfile.encryptionAtHost), sec = tostring(properties.securityProfile.securityType)
| where isempty(zone) or eah != true or sec !~ 'TrustedLaunch'
| project name, resourceGroup, zone, encryptionAtHost = eah, securityType = sec
"@
```

### Equivalente en Bicep

Una VM por despliegue: la contraseña se lee de Key Vault con `getSecret` en el `.bicepparam`, que solo admite un secreto por parámetro.

`vm.bicep`:

```bicep
// =============================================================================
// Una VM segura por defecto: zona, Trusted Launch, cifrado en el host, sin IP pública,
// identidad gestionada, Customer Managed Schedules, AMA + DCR y login con Entra ID opcional
// DEPENDENCY: subred con NSG y salida explícita; EncryptionAtHost registrada en la suscripción
// DEPENDENCY: contraseña de Windows en Key Vault (se lee con getSecret en el .bicepparam)
// =============================================================================
param name string
param location string = resourceGroup().location

@allowed(['Windows', 'Linux'])
param osType string

param size string

@allowed(['1', '2', '3'])
param zone string

@maxLength(15)
@description('Nombre de equipo (Windows: 15 caracteres como máximo).')
param computerName string

param imageReference object
param licenseType string?
param timeZone string?

param subnetId string
param privateIpAddress string?
param acceleratedNetworking bool = true

param adminUsername string

@secure()
@description('Windows: contraseña leída de Key Vault.')
param adminPassword string = ''

@description('Linux: clave pública SSH.')
param sshPublicKey string = ''

param entraLogin bool = false

@allowed(['Premium_LRS', 'Premium_ZRS', 'StandardSSD_LRS', 'StandardSSD_ZRS'])
param osDiskType string = 'Premium_LRS'

@description('[{ name, lun, sizeGb, sku, caching }]')
param dataDisks array = []

param diskEncryptionSetId string?
param encryptionAtHost bool = true
param dataCollectionRuleId string?
param tags object = {}

var isWindows = osType == 'Windows'
var desRef = empty(diskEncryptionSetId ?? '') ? null : { id: diskEncryptionSetId }

resource nic 'Microsoft.Network/networkInterfaces@2024-05-01' = {
  name: 'nic-${name}'
  location: location
  tags: tags
  properties: {
    enableAcceleratedNetworking: acceleratedNetworking
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
    zones: endsWith(d.sku, '_ZRS') ? null : [zone]
    properties: {
      creationData: {
        createOption: 'Empty'
      }
      diskSizeGB: d.sizeGb
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
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    hardwareProfile: {
      vmSize: size
    }
    licenseType: licenseType
    securityProfile: {
      securityType: 'TrustedLaunch'
      uefiSettings: {
        secureBootEnabled: true
        vTpmEnabled: true
      }
      encryptionAtHost: encryptionAtHost
    }
    storageProfile: {
      imageReference: imageReference
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
      dataDisks: [
        for (d, i) in dataDisks: {
          lun: d.lun
          createOption: 'Attach'
          caching: d.caching
          managedDisk: {
            id: disks[i].id
          }
        }
      ]
    }
    osProfile: {
      computerName: computerName
      adminUsername: adminUsername
      adminPassword: isWindows ? adminPassword : null
      allowExtensionOperations: true
      windowsConfiguration: isWindows
        ? {
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
        : null
      linuxConfiguration: isWindows
        ? null
        : {
            disablePasswordAuthentication: true
            provisionVMAgent: true
            ssh: {
              publicKeys: [
                {
                  path: '/home/${adminUsername}/.ssh/authorized_keys'
                  keyData: sshPublicKey
                }
              ]
            }
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
        enabled: true // almacenamiento gestionado
      }
    }
  }
}

resource ama 'Microsoft.Compute/virtualMachines/extensions@2024-11-01' = if (!empty(dataCollectionRuleId ?? '')) {
  parent: vm
  name: isWindows ? 'AzureMonitorWindowsAgent' : 'AzureMonitorLinuxAgent'
  location: location
  properties: {
    publisher: 'Microsoft.Azure.Monitor'
    type: isWindows ? 'AzureMonitorWindowsAgent' : 'AzureMonitorLinuxAgent'
    typeHandlerVersion: '1.0'
    autoUpgradeMinorVersion: true
    enableAutomaticUpgrade: true
  }
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

resource entra 'Microsoft.Compute/virtualMachines/extensions@2024-11-01' = if (entraLogin) {
  parent: vm
  name: isWindows ? 'AADLoginForWindows' : 'AADSSHLoginForLinux'
  location: location
  properties: {
    publisher: 'Microsoft.Azure.ActiveDirectory'
    type: isWindows ? 'AADLoginForWindows' : 'AADSSHLoginForLinux'
    typeHandlerVersion: '1.0'
    autoUpgradeMinorVersion: true
  }
}

output id string = vm.id
output principalId string = vm.identity.principalId
output privateIp string = nic.properties.ipConfigurations[0].properties.privateIPAddress
```

`vm-app-pro-01.bicepparam` (Windows):

```bicep
using 'vm.bicep'

param name = 'vm-app-pro-01'
param osType = 'Windows'
param size = 'Standard_D4as_v6'
param zone = '1'
param computerName = 'vmapppro01'

param imageReference = {
  publisher: 'MicrosoftWindowsServer'
  offer: 'WindowsServer'
  sku: '2025-datacenter-azure-edition'
  version: 'latest'
}
param licenseType = 'Windows_Server'
param timeZone = 'Romance Standard Time'

param subnetId = '<resourceId snet-app-pro>'
param adminUsername = '<admin-local>'

// La contraseña vive en Key Vault; la identidad del despliegue necesita leer el secreto
// y el vault, enabledForTemplateDeployment = true
param adminPassword = az.getSecret('<subscription-id>', '<rg-security-pro>', '<kv-workload-pro>', 'vm-app-pro-01-admin')

param dataDisks = [
  {
    name: 'data01'
    lun: 0
    sizeGb: 256
    sku: 'Premium_LRS'
    caching: 'ReadOnly'
  }
]

param dataCollectionRuleId = '<resourceId dcr-vm-windows-pro>'

param tags = {
  environment: 'pro'
  workload: '<workload>'
  PatchGroup: 'pro-wave1'
}
```

`vm-api-pro-01.bicepparam` (Linux):

```bicep
using 'vm.bicep'

param name = 'vm-api-pro-01'
param osType = 'Linux'
param size = 'Standard_D2as_v6'
param zone = '1'
param computerName = 'vm-api-pro-01'

param imageReference = {
  publisher: 'Canonical'
  offer: 'ubuntu-24_04-lts'
  sku: 'server'
  version: 'latest'
}

param subnetId = '<resourceId snet-app-pro>'
param adminUsername = 'azureadmin'
param sshPublicKey = '<clave pública SSH>'
param entraLogin = true

param diskEncryptionSetId = '<resourceId des-workload-pro>'
param dataCollectionRuleId = '<resourceId dcr-vm-linux-pro>'

param tags = {
  environment: 'pro'
  workload: '<workload>'
  PatchGroup: 'pro-wave1'
}
```

Despliegue:

```powershell
Get-ChildItem -Filter "vm-*.bicepparam" | ForEach-Object {
    New-AzResourceGroupDeployment -ResourceGroupName "<rg-app-pro>" -TemplateParameterFile $_.FullName -Name ("vm-" + $_.BaseName)
}
```

## Errores típicos

| Síntoma | Causa | Solución |
|---|---|---|
| `Unsupported argument "enable_accelerated_networking"` | Módulo `Compute/VirtualMachine` con azurerm 4.x | Usar los submódulos de `Compute/Compute/modules` |
| Error al crear la VM indicando que EncryptionAtHost no está habilitado | Característica sin registrar en la suscripción | `Register-AzProviderFeature -FeatureName EncryptionAtHost` |
| No se puede activar el cifrado en el host | La VM tuvo Azure Disk Encryption | Migrar a discos y VM nuevos |
| VM creada sin Trusted Launch desde Terraform o Bicep | No se declaró `secure_boot_enabled`/`vtpm_enabled` (o `securityProfile`) | Declararlo siempre |
| No se puede redimensionar a una serie M | Trusted Launch no admite ese tamaño | Desasignar y cambiar `securityType` a `Standard` (API 2025-11-01+, fuera del portal) o elegir otra serie |
| `SkuNotAvailable` o `ZonalAllocationFailed` | Tamaño sin capacidad en la región o zona | Otro tamaño o zona; Capacity Reservation para lo crítico |
| `OperationNotAllowed` por cuota | Cuota de vCPU de la familia agotada | Solicitar aumento de cuota antes del despliegue |
| Windows no se actualiza ni se activa | Subred privada sin salida explícita | NAT Gateway o firewall con UDR |
| Inicio de sesión con Entra ID rechazado | Falta el rol *Virtual Machine Administrator/User Login*, MFA por usuario heredado o el cliente no está unido a Entra ID | Asignar el rol; acceso condicional en lugar de MFA por usuario |
| AADLoginForWindows falla con 1007 | La VM no tiene identidad del sistema | Activar la identidad antes de la extensión |
| VM Windows unida a dominio y a Entra ID a la vez | No soportado | Elegir uno |
| AMA instalado pero sin datos | Falta la asociación a la DCR o la DCR no apunta al workspace | Asociación por VM; revisar la DCR |
| La asociación de DCR falla | DCR y DCE en la misma asociación (módulo `VMExtension-AzureMonitorAgent`) | Una asociación para la DCR y otra para el DCE |
| Se sigue pagando una VM apagada | Se apagó desde el SO (detenida, no desasignada) | Desasignar desde Azure |
| El disco de datos no se conecta | Zona distinta de la VM o LUN repetido | Misma zona (o ZRS) y LUN único |
| `terraform destroy` deja el disco del SO | Comportamiento elegido en el provider | Borrarlo a mano tras confirmar |
| La contraseña de Windows no se guarda | Sin permiso o sin acceso de red al Key Vault desde el ejecutor | *Key Vault Secrets Officer* y acceso privado al vault |
| Spot expulsada sin aviso aparente | Expulsión con 30 segundos | Scheduled Events y cargas tolerantes a interrupciones |
