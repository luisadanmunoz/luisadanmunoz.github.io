---
title: "Session Hosts"
indice: avd
resumen: "Las máquinas virtuales donde se conectan los usuarios."
estado: documentado   # proximamente | en-curso | documentado
orden: 2
last_review: 2026-10-20
fuentes:
  - titulo: "Add session hosts to a host pool"
    url: https://learn.microsoft.com/azure/virtual-desktop/add-session-hosts-host-pool
  - titulo: "Prerequisites for Azure Virtual Desktop"
    url: https://learn.microsoft.com/azure/virtual-desktop/prerequisites
  - titulo: "Session host virtual machine sizing guidelines"
    url: https://learn.microsoft.com/windows-server/remote/remote-desktop-services/session-host-virtual-machine-sizing-guidelines
  - titulo: "Microsoft Entra joined session hosts"
    url: https://learn.microsoft.com/azure/virtual-desktop/azure-ad-joined-session-hosts
  - titulo: "Sign in to a Windows VM using Microsoft Entra ID"
    url: https://learn.microsoft.com/entra/identity/devices/howto-vm-sign-in-azure-ad-windows
  - titulo: "Windows update management methodologies for session hosts"
    url: https://learn.microsoft.com/azure/virtual-desktop/windows-update-management-methodologies-session-hosts
  - titulo: "Session host statuses and health checks"
    url: https://learn.microsoft.com/azure/virtual-desktop/session-host-status-health-checks
  - titulo: "Drain session hosts for maintenance"
    url: https://learn.microsoft.com/azure/virtual-desktop/drain-mode
  - titulo: "Security recommendations for Azure Virtual Desktop"
    url: https://learn.microsoft.com/azure/virtual-desktop/security-recommendations
  - titulo: "Enable screen capture protection"
    url: https://learn.microsoft.com/azure/virtual-desktop/screen-capture-protection
  - titulo: "Watermarking in Azure Virtual Desktop"
    url: https://learn.microsoft.com/azure/virtual-desktop/watermarking
  - titulo: "Apply a Windows license to session host virtual machines"
    url: https://learn.microsoft.com/azure/virtual-desktop/apply-windows-license
  - titulo: "Required FQDNs and endpoints for Azure Virtual Desktop"
    url: https://learn.microsoft.com/azure/virtual-desktop/required-fqdn-endpoint
  - titulo: "Troubleshoot common Azure Virtual Desktop Agent issues"
    url: https://learn.microsoft.com/troubleshoot/azure/virtual-desktop/troubleshoot-agent
  - titulo: "Windows 11 release information"
    url: https://learn.microsoft.com/windows/release-health/windows11-release-information
  - titulo: "PowerShell DSC Extension (retirement)"
    url: https://learn.microsoft.com/azure/virtual-machines/extensions/dsc-windows
  - titulo: "Run scripts in a Windows VM with managed Run Commands"
    url: https://learn.microsoft.com/azure/virtual-machines/windows/run-command-managed
  - titulo: "Trusted launch for Azure virtual machines"
    url: https://learn.microsoft.com/azure/virtual-machines/trusted-launch
  - titulo: "Hibernation for Azure virtual machines"
    url: https://learn.microsoft.com/azure/virtual-machines/hibernate-resume
  - titulo: "Plantillas ARM oficiales de AVD (Azure/RDS-Templates)"
    url: https://github.com/Azure/RDS-Templates/tree/master/ARM-wvd-templates
  - titulo: "azurerm_windows_virtual_machine"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/windows_virtual_machine
  - titulo: "azurerm_virtual_machine_run_command"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/virtual_machine_run_command
  - titulo: "Guía de actualización a azurerm 4.0"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide
  - titulo: "Módulo Terraform AzureVirtualDesktop/SessionHost"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/AzureVirtualDesktop/SessionHost
---

Los **session hosts** son las máquinas virtuales Windows donde se ejecutan los escritorios y las aplicaciones. Se registran en un [host pool](/recursos/avd/host-pools/) con el agente de Azure Virtual Desktop y, a partir de ahí, el servicio les envía usuarios. Son la parte que más pesa en la factura y en la experiencia: **el tamaño de la VM, el sistema operativo, la imagen y cómo se actualizan** deciden cuántos usuarios caben, cuánto cuesta cada uno y cuánto trabajo da mantenerlos.

## Qué es y cuándo usarlo

Un session host es una VM normal con tres piezas añadidas: el **AVD Agent**, el **Boot Loader** y la pila *side-by-side* que recibe las conexiones. No necesita IP pública ni puertos de entrada: la VM sale hacia el servicio y el servicio le entrega las sesiones.

### Sistema operativo

| Sistema operativo | Tipo de host pool | Licencia (uso interno) | Cuándo |
|---|---|---|---|
| **Windows 11 Enterprise multi-session** (recomendado) | Pooled | Microsoft 365 E3/E5/A3/A5/F3/Business Premium, Windows Enterprise E3/E5, Windows VDA | Escritorio compartido; solo existe en AVD |
| **Windows 11 Enterprise** | Personal | Las mismas | Un usuario por VM |
| **Windows Server 2022 / 2025** | Pooled | RDS CAL con Software Assurance o RDS User Subscription | Aplicaciones que solo soportan servidor o migraciones de granjas RDS |

Windows Server necesita además el rol *Remote Desktop Session Host* y un servidor de licencias RDS. Para uso comercial externo solo vale Windows cliente con *per-user access pricing*.

### Versión de Windows 11

| Versión | Fin de actualizaciones (Enterprise y multi-session) | Recomendación |
|---|---|---|
| 23H2 | **10 de noviembre de 2026** | Migrar ya |
| 24H2 | 12 de octubre de 2027 | Aceptable en despliegues existentes |
| **25H2** | 10 de octubre de 2028 | Recomendada para despliegues nuevos |
| 26H2 | 9 de octubre de 2029 | Disponible desde el 29 de septiembre de 2026; comprobar la imagen de AVD en Marketplace antes de usarla |

Imágenes de Marketplace (publisher `MicrosoftWindowsDesktop`):

| Imagen | Offer | SKU |
|---|---|---|
| Windows 11 Enterprise multi-session + Microsoft 365 Apps | `office-365` | `win11-25h2-avd-m365` |
| Windows 11 Enterprise multi-session | `windows-11` | `win11-25h2-avd` |
| Windows 11 Enterprise | `windows-11` | `win11-25h2-ent` |

En producción recomiendo una **imagen dorada en Azure Compute Gallery** construida desde una de estas, con versión fijada.

### Tamaño de las VMs

La guía de Microsoft para multisesión (punto de partida, siempre a validar con pruebas de carga):

| Perfil | Usuarios por vCPU | Mínimo por VM | Ejemplos |
|---|---|---|---|
| Light (entrada de datos) | 6 | 8 vCPU, 16 GB RAM | D8s_v5, D8as_v4 |
| Medium (Office, web estática) | 4 | 8 vCPU, 16 GB RAM | D8s_v5, D16s_v5 |
| Heavy (Outlook, PowerPoint, desarrollo) | 2 | 8 vCPU, 16 GB RAM | D8s_v5, D16s_v5 |
| Power (CAD, edición de vídeo, ML) | 1 | 6 vCPU, 56 GB RAM | D16ds_v5, NV-series (GPU) |

- En multisesión, VMs de **entre 6 y 24 vCPU**. Microsoft no recomienda bajar de 4 núcleos, porque la interfaz de Windows se vuelve inestable con varios usuarios.
- Para hosts personales, mínimo 2 núcleos físicos (normalmente 4 vCPU).
- **Disco de SO Premium SSD** en producción.

### Unión a directorio

| Opción | Requisitos | Cuándo |
|---|---|---|
| **Microsoft Entra ID** (recomendado) | Extensión `AADLoginForWindows`, identidad *system-assigned* en la VM, rol *Virtual Machine User Login* a los usuarios y SSO en el host pool | Despliegues nuevos; perfiles FSLogix en Azure Files con Entra Kerberos |
| **AD DS** | Línea de visión con los DC, cuenta de unión, OU dedicada | Dependencia fuerte de GPO, recursos SMB con Kerberos o aplicaciones que la exigen |
| Microsoft Entra hybrid join | Unión a AD DS + sincronización con Entra ID; objeto Kerberos en Entra ID para SSO | Transición: GPO de AD y acceso con identidad de Entra |

**Todos los hosts de un host pool deben usar el mismo tipo de unión.**

### Cómo se registran en el host pool

| Método | Cómo funciona | Observaciones |
|---|---|---|
| Portal o plantilla ARM del servicio | Extensión DSC que instala el agente con el token | La **extensión DSC se retira el 31 de marzo de 2028** |
| **Agente con `msiexec`** (el que uso) | Se descargan el agente y el Boot Loader y se instalan con `REGISTRATIONTOKEN=` | Procedimiento de Learn para VMs creadas fuera de AVD. Aquí lo lanzo con un Run Command gestionado y el token como parámetro protegido |
| Session host configuration | El servicio crea las VMs y el agente hace la unión | Solo con ese modelo de gestión del host pool |

### Actualizaciones

| Método | Windows multi-session | Windows Enterprise (personal) | Windows Server |
|---|---|---|---|
| Imagen nueva en Azure Compute Gallery y redespliegue | **Recomendado** | No recomendado | No recomendado |
| Session host update (session host configuration) | **Recomendado** | No soportado | No recomendado |
| Windows Update / Windows Autopatch | No recomendado | **Recomendado** | Soportado / no soportado |
| Azure Update Manager / parcheo automático de invitado | No soportado | No soportado | **Recomendado** |
| Configuration Manager | Soportado | Soportado | Soportado |

El *hotpatch* (parches sin reinicio) está soportado en multisesión, en Windows 11 Enterprise 24H2 o superior con VBS y en Windows Server Azure Edition.

### Estados de un session host

| Estado | Recibe sesiones nuevas | Qué significa |
|---|---|---|
| Available | ✅ | Ha pasado todas las comprobaciones (también si ha llegado al límite de sesiones) |
| Needs Assistance | ✅ | Falla una comprobación no crítica: URLs requeridas, IMDS (169.254.169.254) o agente de monitorización |
| Upgrading / Upgrade Failed | ✅ | El agente se está actualizando o no ha podido; las sesiones siguen funcionando |
| Unavailable | ❌ | Apagado o falla una comprobación crítica (unión a dominio, confianza de dominio, pila SxS) |
| Shutdown | ❌ | VM apagada |

El **drain mode** impide sesiones nuevas en un host sin echar a los usuarios conectados. Es el paso previo a cualquier mantenimiento o retirada.

### Límites que conviene tener a mano

| Límite | Valor |
|---|---|
| Session hosts por host pool | 10.000 |
| VMs por despliegue desde el portal | 400 |
| Nombre del equipo | 15 caracteres (NetBIOS) |
| Validez del token de registro | 1 hora a 27 días |
| Host apagado sin renovar su token de máquina | 90 días (encenderlo 20 minutos para renovarlo) |
| Hibernación | Solo host pools personales; no compatible con FSLogix ni App Attach |

### Qué escenario recomiendo

| Escenario del cliente | Diseño | Por qué |
|---|---|---|
| Oficina estándar | Windows 11 25H2 multi-session + M365 Apps, D8s_v5–D16s_v5, Entra ID join, imagen dorada en Compute Gallery | Mejor relación coste-usuario y operación por imágenes |
| Aplicación de servidor o granja RDS migrada | Windows Server 2022/2025 con RDS CAL | Compatibilidad con la aplicación |
| Desarrolladores o usuarios avanzados | Windows 11 Enterprise en host pool personal, Windows Update/Autopatch | VM dedicada gestionada como un PC |
| Diseño, CAD o vídeo | NV-series con GPU en host pool personal o pooled de baja densidad | La CPU sola no da la experiencia gráfica |
| Datos sensibles | Trusted launch, *screen capture protection*, marca de agua y redirecciones desactivadas | Evita la fuga de información desde el cliente |

### Datos que conviene llevar a la reunión

- **Windows 11 23H2 deja de recibir actualizaciones el 10 de noviembre de 2026**: cualquier imagen basada en 23H2 hay que rehacerla ya.
- **Windows 11 multi-session solo existe en Azure Virtual Desktop** y el derecho de uso va incluido en Microsoft 365 E3/E5: no se paga licencia de Windows en la VM (`license_type = Windows_Client`).
- **En multisesión no se parchea con Windows Update**: se publica una imagen nueva y se reemplazan los hosts. Hay que montar la cadena de imágenes desde el principio.
- **No hay que abrir puertos de entrada** ni poner IP públicas: los hosts solo necesitan salida a las URLs de AVD.
- **El tamaño se decide con pruebas de carga**, no con la tabla: la guía de usuarios por vCPU es un punto de partida.
- **La extensión DSC se retira en marzo de 2028**: una automatización nueva no debería depender de ella.

## Decisiones de diseño

| Decisión | Lo que aplico | Por qué |
|---|---|---|
| Sistema operativo | Windows 11 25H2 Enterprise multi-session (con M365 Apps si aplica) | Versión con soporte hasta octubre de 2028 |
| Imagen | Imagen dorada versionada en Azure Compute Gallery; Marketplace solo para pruebas | Todos los hosts iguales y cambios trazables |
| Tamaño | Familia Dsv5/Dasv5 de 8 a 16 vCPU, validada con pruebas de carga | Rango recomendado para multisesión |
| Disponibilidad | Hosts repartidos en las 3 zonas de la región | Una zona caída no deja sin escritorio a todos |
| Seguridad de la VM | Trusted launch (Secure Boot + vTPM) y *encryption at host* | Requisito de Windows 11 y protección del arranque |
| Red | Sin IP pública ni NSG por NIC; NSG en la subnet y salida controlada a las URLs requeridas | AVD no necesita puertos de entrada |
| Identidad | Entra ID join con identidad *system-assigned*, Intune y *Virtual Machine User Login* en el RG para el grupo de usuarios | Sin dependencia de los DC y gestión moderna |
| Credenciales | Administrador local y cuenta de unión en Key Vault | Nada sensible en el repositorio ni en tfvars |
| Registro | Run Command gestionado con el instalador oficial y el token como parámetro protegido | No depende de la extensión DSC |
| Licencia | `license_type = "Windows_Client"` | Aplica el derecho de uso de Microsoft 365 / Windows Enterprise |
| Actualización | Imagen nueva y reemplazo progresivo (drain mode → baja → alta con la nueva imagen) | Método recomendado para multisesión |
| Nombres | Prefijo de 12 caracteres como máximo + `-NN`, con `start_index` para ampliar | Nombre NetBIOS de 15 caracteres y altas sin renombrar |
| Protección de datos | Defender for Endpoint, exclusiones de FSLogix, *screen capture protection* y marca de agua según la sensibilidad | Recomendaciones de seguridad de AVD |

Alineación con el Well-Architected Framework:

- **Seguridad**: Trusted launch, sin puertos de entrada, Entra ID con Conditional Access, secretos en Key Vault y EDR.
- **Fiabilidad**: hosts en zonas, imagen versionada y reemplazo progresivo con drain mode.
- **Coste**: multisesión, derecho de uso de Windows incluido, tamaño medido y escalado con Autoscale.
- **Excelencia operativa**: imágenes y hosts por IaC; los hosts no se modifican a mano.
- **Rendimiento**: SKU con redes aceleradas, Premium SSD y límite de sesiones acorde al tamaño.

## Módulo de Terraform

### El módulo del repositorio

| Pieza | Módulo | Estado |
|---|---|---|
| Session hosts | [`AzureVirtualDesktop/SessionHost`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/AzureVirtualDesktop/SessionHost) | **No utilizable con azurerm 4.x sin cambios** |

Lo bueno: cubre Trusted launch, zonas, imagen de Compute Gallery o de Marketplace, unión a Entra ID (con Intune) o AD DS, y el registro con el token en `protected_settings`. Lo que hay que corregir antes de usarlo:

- **Falla con azurerm 4.x**: usa `enable_accelerated_networking` en `azurerm_network_interface`, que se eliminó en 4.0 en favor de `accelerated_networking_enabled`. Su `versions.tf` admite `>= 3.70.0, < 5.0.0`, así que el error aparece en el `plan`.
- **Imagen por defecto `win11-23h2-avd`**: 23H2 deja de recibir actualizaciones el 10 de noviembre de 2026.
- **Registro con la extensión DSC**, que se retira el 31 de marzo de 2028, y con un paquete `Configuration_*.zip` de versión fija.
- **Contraseñas**: genera la del administrador con `random_password` y la expone en un `output`. La de unión a dominio llega por variable. Las dos acaban en el *state*, y ninguna se lee de Key Vault.
- **`count` + `locals`**: quitar un host de en medio desplaza los índices y recrea los posteriores. Además limita a 100 instancias por llamada.
- `computer_name` se compone de prefijo + entorno + 3 dígitos sin validar los 15 caracteres; zona horaria UTC y sin *boot diagnostics* por defecto.

Hasta corregirlo, la ficha despliega los hosts con recursos nativos: `for_each` sobre un mapa, contraseñas de Key Vault y registro con Run Command.

### Estructura en el proyecto

```txt
/
├── providers.tf
├── host_pools.tf      # ficha Host Pools (module.host_pool_registration da el token)
├── session_hosts.tf   # VMs, unión a directorio y registro
├── scripts/
│   └── Register-AvdAgent.ps1
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
      # 4.0.0: accelerated_networking_enabled en azurerm_network_interface.
      # < 5.0.0: restricción de los módulos de AzureTerraformModules.
      version = ">= 4.0.0, < 5.0.0"
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

### Session hosts · `session_hosts.tf`

```hcl
# =============================================================================
# Session hosts de AVD (recursos nativos)
# DEPENDENCY: host_pools.tf de la ficha Host Pools en el mismo root
#             (module.host_pool y module.host_pool_registration)
# DEPENDENCY: Subnet de session hosts con salida a las URLs requeridas de AVD (sin IP pública ni puertos de entrada)
# DEPENDENCY: Key Vault con la contraseña del administrador local (y la de la cuenta de unión a AD DS si aplica)
# DEPENDENCY: Imagen de Marketplace o de Azure Compute Gallery
# DEPENDENCY: scripts/Register-AvdAgent.ps1 en el repositorio
# =============================================================================

variable "session_hosts" {
  description = "Grupos de session hosts (clave = nombre lógico del grupo)."
  type = map(object({
    host_pool           = string # clave de var.host_pools
    resource_group_name = string
    location            = string
    subnet_id           = string

    name_prefix    = string # máximo 12 caracteres: prefijo + "-NN" ≤ 15 (nombre NetBIOS)
    instance_count = number
    start_index    = optional(number, 1) # para añadir hosts sin renombrar los existentes
    zones          = optional(list(string), ["1", "2", "3"])

    vm_size              = string
    os_disk_type         = optional(string, "Premium_LRS")
    os_disk_size_gb      = optional(number, 128)
    encryption_at_host   = optional(bool, true) # requiere la feature EncryptionAtHost registrada
    timezone             = optional(string, "Romance Standard Time")
    boot_diagnostics     = optional(bool, true)

    # Imagen: Azure Compute Gallery (recomendado) o Marketplace
    source_image_id = optional(string)
    marketplace_image = optional(object({
      publisher = string
      offer     = string
      sku       = string
      version   = optional(string, "latest")
      }), {
      publisher = "MicrosoftWindowsDesktop"
      offer     = "office-365"
      sku       = "win11-25h2-avd-m365"
      version   = "latest"
    })

    join_type         = optional(string, "EntraID") # EntraID | ADDS
    intune_enrollment = optional(bool, true)        # solo EntraID
    ad_domain = optional(object({
      domain_name          = string
      ou_path              = optional(string)
      join_username        = string # usuario con permiso de unión, sin dominio
      password_secret_name = string # secreto en var.key_vault_id
    }))

    tags = optional(map(string), {})
  }))

  validation {
    condition     = alltrue([for k, v in var.session_hosts : length(v.name_prefix) <= 12])
    error_message = "name_prefix admite como máximo 12 caracteres (prefijo + '-NN' ≤ 15)."
  }

  validation {
    condition     = alltrue([for k, v in var.session_hosts : contains(["EntraID", "ADDS"], v.join_type)])
    error_message = "join_type debe ser EntraID o ADDS."
  }

  validation {
    condition     = alltrue([for k, v in var.session_hosts : v.join_type != "ADDS" || v.ad_domain != null])
    error_message = "Con join_type ADDS hay que informar ad_domain."
  }

  validation {
    condition     = alltrue([for k, v in var.session_hosts : v.start_index + v.instance_count - 1 <= 99])
    error_message = "El sufijo numérico es de dos dígitos: start_index + instance_count - 1 no puede superar 99."
  }
}

variable "local_admin" {
  description = "Administrador local de los session hosts; la contraseña se lee de Key Vault."
  type = object({
    username             = string
    password_secret_name = string
  })
}

variable "key_vault_id" {
  description = "Key Vault con los secretos de administrador local y de unión a dominio."
  type        = string
}

variable "vm_login_assignments" {
  description = "Solo Entra ID: rol Virtual Machine User Login (o Administrator Login) para los grupos de usuarios."
  type = map(object({
    scope                = string # RG de los session hosts
    role_definition_name = optional(string, "Virtual Machine User Login")
    principal_id         = string # object ID del grupo de Entra ID
  }))
  default = {}
}

data "azurerm_key_vault_secret" "local_admin" {
  name         = var.local_admin.password_secret_name
  key_vault_id = var.key_vault_id
}

data "azurerm_key_vault_secret" "domain_join" {
  for_each     = { for k, v in var.session_hosts : k => v if v.join_type == "ADDS" }
  name         = each.value.ad_domain.password_secret_name
  key_vault_id = var.key_vault_id
}

resource "azurerm_network_interface" "session_host" {
  for_each = {
    for item in flatten([
      for gk, g in var.session_hosts : [
        for i in range(g.instance_count) : {
          key   = format("%s-%02d", g.name_prefix, g.start_index + i)
          group = gk
        }
      ]
    ]) : item.key => item
  }

  name                           = "nic-${each.key}"
  resource_group_name            = var.session_hosts[each.value.group].resource_group_name
  location                       = var.session_hosts[each.value.group].location
  accelerated_networking_enabled = true

  ip_configuration {
    name                          = "ipconfig1"
    subnet_id                     = var.session_hosts[each.value.group].subnet_id
    private_ip_address_allocation = "Dynamic"
  }

  tags = merge(var.tags, var.session_hosts[each.value.group].tags)
}

resource "azurerm_windows_virtual_machine" "session_host" {
  for_each = {
    for item in flatten([
      for gk, g in var.session_hosts : [
        for i in range(g.instance_count) : {
          key   = format("%s-%02d", g.name_prefix, g.start_index + i)
          group = gk
          zone  = length(g.zones) > 0 ? g.zones[(g.start_index + i - 1) % length(g.zones)] : null
        }
      ]
    ]) : item.key => item
  }

  name                  = each.key
  computer_name         = each.key
  resource_group_name   = var.session_hosts[each.value.group].resource_group_name
  location              = var.session_hosts[each.value.group].location
  size                  = var.session_hosts[each.value.group].vm_size
  zone                  = each.value.zone
  network_interface_ids = [azurerm_network_interface.session_host[each.key].id]

  admin_username = var.local_admin.username
  admin_password = data.azurerm_key_vault_secret.local_admin.value

  # Derecho de uso de Windows incluido en Microsoft 365 / Windows Enterprise (no se paga la licencia en la VM)
  license_type = "Windows_Client"
  timezone     = var.session_hosts[each.value.group].timezone

  # Trusted launch
  secure_boot_enabled        = true
  vtpm_enabled               = true
  encryption_at_host_enabled = var.session_hosts[each.value.group].encryption_at_host

  # AADLoginForWindows exige identidad system-assigned
  identity {
    type = "SystemAssigned"
  }

  os_disk {
    name                 = "osdisk-${each.key}"
    caching              = "ReadWrite"
    storage_account_type = var.session_hosts[each.value.group].os_disk_type
    disk_size_gb         = var.session_hosts[each.value.group].os_disk_size_gb
  }

  source_image_id = var.session_hosts[each.value.group].source_image_id

  dynamic "source_image_reference" {
    for_each = var.session_hosts[each.value.group].source_image_id == null ? [var.session_hosts[each.value.group].marketplace_image] : []
    content {
      publisher = source_image_reference.value.publisher
      offer     = source_image_reference.value.offer
      sku       = source_image_reference.value.sku
      version   = source_image_reference.value.version
    }
  }

  dynamic "boot_diagnostics" {
    for_each = var.session_hosts[each.value.group].boot_diagnostics ? [1] : []
    content {} # cuenta de almacenamiento gestionada
  }

  # avd-group enlaza cada VM con su grupo de var.session_hosts (lo usan extensiones y Run Command)
  tags = merge(var.tags, var.session_hosts[each.value.group].tags, {
    "avd-group"     = each.value.group
    "avd-host-pool" = var.session_hosts[each.value.group].host_pool
  })

  lifecycle {
    # La contraseña rota en Key Vault; la imagen nueva se aplica redesplegando hosts, no in-place
    ignore_changes = [admin_password, source_image_id, source_image_reference]
  }
}

# Unión a Microsoft Entra ID (con inscripción opcional en Intune)
resource "azurerm_virtual_machine_extension" "entra_join" {
  for_each = {
    for k, vm in azurerm_windows_virtual_machine.session_host : k => vm
    if var.session_hosts[vm.tags["avd-group"]].join_type == "EntraID"
  }

  name                       = "AADLoginForWindows"
  virtual_machine_id         = each.value.id
  publisher                  = "Microsoft.Azure.ActiveDirectory"
  type                       = "AADLoginForWindows"
  type_handler_version       = "2.0"
  auto_upgrade_minor_version = true

  # mdmId de Intune: mismo valor que las plantillas ARM oficiales de AVD
  settings = var.session_hosts[each.value.tags["avd-group"]].intune_enrollment ? jsonencode({
    mdmId = "0000000a-0000-0000-c000-000000000000"
  }) : null
}

# Unión a AD DS
resource "azurerm_virtual_machine_extension" "adds_join" {
  for_each = {
    for k, vm in azurerm_windows_virtual_machine.session_host : k => vm
    if var.session_hosts[vm.tags["avd-group"]].join_type == "ADDS"
  }

  name                       = "JsonADDomainExtension"
  virtual_machine_id         = each.value.id
  publisher                  = "Microsoft.Compute"
  type                       = "JsonADDomainExtension"
  type_handler_version       = "1.3"
  auto_upgrade_minor_version = true

  settings = jsonencode({
    Name    = var.session_hosts[each.value.tags["avd-group"]].ad_domain.domain_name
    OUPath  = var.session_hosts[each.value.tags["avd-group"]].ad_domain.ou_path
    User    = "${var.session_hosts[each.value.tags["avd-group"]].ad_domain.domain_name}\\${var.session_hosts[each.value.tags["avd-group"]].ad_domain.join_username}"
    Restart = "true"
    Options = "3"
  })

  protected_settings = jsonencode({
    Password = data.azurerm_key_vault_secret.domain_join[each.value.tags["avd-group"]].value
  })
}

# Registro en el host pool: agente + Boot Loader con el token (Run Command gestionado)
resource "azurerm_virtual_machine_run_command" "avd_agent" {
  for_each = azurerm_windows_virtual_machine.session_host

  name               = "Register-AvdAgent"
  location           = each.value.location
  virtual_machine_id = each.value.id

  source {
    script = file("${path.root}/scripts/Register-AvdAgent.ps1")
  }

  protected_parameter {
    name  = "RegistrationToken"
    value = module.host_pool_registration[var.session_hosts[each.value.tags["avd-group"]].host_pool].token
  }

  tags = each.value.tags

  lifecycle {
    # El token rota; un host ya registrado no necesita volver a ejecutar el script
    ignore_changes = [protected_parameter]
  }

  depends_on = [
    azurerm_virtual_machine_extension.entra_join,
    azurerm_virtual_machine_extension.adds_join,
  ]
}

resource "azurerm_role_assignment" "vm_login" {
  for_each             = var.vm_login_assignments
  scope                = each.value.scope
  role_definition_name = each.value.role_definition_name
  principal_id         = each.value.principal_id
}

output "session_host_ids" {
  description = "IDs de las VMs de session host."
  value       = { for k, vm in azurerm_windows_virtual_machine.session_host : k => vm.id }
}
```

### Script de registro · `scripts/Register-AvdAgent.ps1`

```powershell
# Registra la VM como session host: instala el Azure Virtual Desktop Agent y el Boot Loader
# con el token de registro del host pool (procedimiento de Learn para VMs creadas fuera de AVD).
# Idempotente: si la VM ya está registrada no hace nada.
param(
    [Parameter(Mandatory = $true)]
    [string] $RegistrationToken
)

$ErrorActionPreference = 'Stop'

$agentKey = 'HKLM:\SOFTWARE\Microsoft\RDInfraAgent'
if ((Test-Path $agentKey) -and ((Get-ItemProperty -Path $agentKey -ErrorAction SilentlyContinue).IsRegistered -eq 1)) {
    Write-Output 'La VM ya está registrada en un host pool. Sin cambios.'
    return
}

$workDir = Join-Path $env:TEMP 'avd-agent'
New-Item -Path $workDir -ItemType Directory -Force | Out-Null

# Enlaces oficiales: Azure Virtual Desktop Agent y Agent Boot Loader
$uris = @(
    'https://go.microsoft.com/fwlink/?linkid=2310011'
    'https://go.microsoft.com/fwlink/?linkid=2311028'
)

$installers = @()
foreach ($uri in $uris) {
    $expandedUri = (Invoke-WebRequest -MaximumRedirection 0 -Uri $uri -UseBasicParsing -ErrorAction SilentlyContinue).Headers.Location
    $fileName = ($expandedUri).Split('/')[-1]
    $filePath = Join-Path $workDir $fileName
    Invoke-WebRequest -Uri $expandedUri -UseBasicParsing -OutFile $filePath
    Unblock-File -Path $filePath
    $installers += $filePath
}

$agent      = $installers | Where-Object { $_ -match 'RDAgent\.Installer' } | Select-Object -First 1
$bootLoader = $installers | Where-Object { $_ -match 'RDAgentBootLoader' } | Select-Object -First 1

$agentArgs = @('/i', "`"$agent`"", '/quiet', '/norestart', "REGISTRATIONTOKEN=$RegistrationToken", '/l*v', "`"$workDir\agent.log`"")
$result = Start-Process -FilePath 'msiexec.exe' -ArgumentList $agentArgs -Wait -PassThru
if ($result.ExitCode -ne 0) { throw "La instalación del agente terminó con código $($result.ExitCode). Revisar $workDir\agent.log" }

$bootArgs = @('/i', "`"$bootLoader`"", '/quiet', '/norestart', '/l*v', "`"$workDir\bootloader.log`"")
$result = Start-Process -FilePath 'msiexec.exe' -ArgumentList $bootArgs -Wait -PassThru
if ($result.ExitCode -ne 0) { throw "La instalación del Boot Loader terminó con código $($result.ExitCode). Revisar $workDir\bootloader.log" }

Write-Output 'Agente y Boot Loader instalados. La VM aparecerá en el host pool en unos minutos.'
```

### `env/pro.tfvars`

```hcl
tags = {
  environment = "pro"
  workload    = "<workload>"
  owner       = "<owner>"
  costcenter  = "<costcenter>"
}

key_vault_id = "<resourceId kv-avd-pro>"

local_admin = {
  username             = "<admin-local>"
  password_secret_name = "avd-local-admin-password"
}

session_hosts = {
  pooled-01 = {
    host_pool           = "vdpool-<workload>-pro-01"
    resource_group_name = "<rg-avd-hosts-pro>"
    location            = "<region>"
    subnet_id           = "<resourceId snet-avd-hosts>"

    name_prefix    = "avdpro01"
    instance_count = 4
    zones          = ["1", "2", "3"]

    vm_size = "Standard_D8s_v5" # 8 vCPU: ~32 usuarios medium según la guía (4 por vCPU), validar con pruebas de carga

    # Imagen dorada en Azure Compute Gallery (versión fijada)
    source_image_id = "<resourceId gal-avd/images/win11-25h2-avd-m365/versions/1.0.0>"

    join_type         = "EntraID"
    intune_enrollment = true
  }

  personal-dev = {
    host_pool           = "vdpool-<workload>-pro-dev01"
    resource_group_name = "<rg-avd-hosts-pro>"
    location            = "<region>"
    subnet_id           = "<resourceId snet-avd-hosts>"

    name_prefix    = "avdprodev"
    instance_count = 3
    vm_size        = "Standard_D4s_v5"

    marketplace_image = {
      publisher = "MicrosoftWindowsDesktop"
      offer     = "windows-11"
      sku       = "win11-25h2-ent"
    }

    join_type = "EntraID"

    # Alternativa con AD DS (todo el host pool con el mismo tipo de unión):
    # join_type = "ADDS"
    # ad_domain = {
    #   domain_name          = "<dominio.local>"
    #   ou_path              = "OU=AVD,OU=Equipos,DC=<dominio>,DC=local"
    #   join_username        = "<svc-domainjoin>"
    #   password_secret_name = "avd-domain-join-password"
    # }
  }
}

vm_login_assignments = {
  usuarios-avd = {
    scope        = "<resourceId rg-avd-hosts-pro>"
    principal_id = "<objectId grupo usuarios AVD>"
  }
  admins-avd = {
    scope                = "<resourceId rg-avd-hosts-pro>"
    role_definition_name = "Virtual Machine Administrator Login"
    principal_id         = "<objectId grupo administradores AVD>"
  }
}
```

En `dev.tfvars` y `pre.tfvars`, mismo esquema con un host por grupo y la imagen de Marketplace para pruebas.

Despliegue y comprobación:

```powershell
terraform init
terraform plan -var-file="env/pro.tfvars" -out="pro.tfplan"
terraform apply "pro.tfplan"

# Resultado del registro en cada VM
Get-AzVMRunCommand -ResourceGroupName "<rg-avd-hosts-pro>" -VMName "avdpro01-01" -RunCommandName "Register-AvdAgent" -Expand InstanceView |
    Select-Object -ExpandProperty InstanceView

# Estado de los hosts en el pool
Get-AzWvdSessionHost -ResourceGroupName "<rg-avd-pro>" -HostPoolName "vdpool-<workload>-pro-01" |
    Select-Object Name, Status, UpdateState, AllowNewSession
```

Learn indica reiniciar los hosts cuando aparezcan como *Available* tras el primer registro.

Para cambiar de imagen, la ficha ignora los cambios de imagen en las VMs existentes. Se sube `start_index` (o se añade un grupo nuevo) con la imagen nueva, se ponen en drain mode los hosts antiguos y se retiran.

### Equivalente en Bicep

`main.bicep` (lee el token del host pool existente con `listRegistrationTokens()`; `Register-AvdAgent.ps1` va en la misma carpeta):

```bicep
// =============================================================================
// Session hosts de AVD: VMs Trusted launch repartidas en zonas, unión a Entra ID
// o AD DS y registro en el host pool con Run Command (agente + Boot Loader)
// DEPENDENCY: Resource Group de los session hosts (targetScope = resourceGroup)
// DEPENDENCY: Host pool existente con un token de registro vigente
// DEPENDENCY: Subnet con salida a las URLs requeridas de AVD
// DEPENDENCY: Key Vault con las contraseñas (se pasan con getSecret() en el .bicepparam)
// DEPENDENCY: Register-AvdAgent.ps1 junto a este fichero
// =============================================================================
targetScope = 'resourceGroup'

param location string = resourceGroup().location

param hostPoolName string
param hostPoolResourceGroupName string = resourceGroup().name

@maxLength(12)
@description('Prefijo de las VMs: prefijo + "-NN" ≤ 15 caracteres (nombre NetBIOS).')
param namePrefix string

@minValue(1)
param instanceCount int

@minValue(1)
@description('Primer número de la serie, para añadir hosts sin renombrar los existentes.')
param startIndex int = 1

param zones array = [
  '1'
  '2'
  '3'
]

param vmSize string

@allowed(['Premium_LRS', 'Premium_ZRS', 'StandardSSD_LRS'])
param osDiskType string = 'Premium_LRS'

param osDiskSizeGB int = 128

@description('Requiere la feature EncryptionAtHost registrada en la suscripción.')
param encryptionAtHost bool = true

param timeZone string = 'Romance Standard Time'

@description('Imagen de Azure Compute Gallery. Vacío = imagen de Marketplace.')
param galleryImageId string = ''

param marketplaceImage object = {
  publisher: 'MicrosoftWindowsDesktop'
  offer: 'office-365'
  sku: 'win11-25h2-avd-m365'
  version: 'latest'
}

param subnetId string

param adminUsername string

@secure()
param adminPassword string

@allowed(['EntraID', 'ADDS'])
param joinType string = 'EntraID'

param intuneEnrollment bool = true

param domainName string = ''
param domainOuPath string = ''
param domainJoinUsername string = ''

@secure()
param domainJoinPassword string = ''

param tags object = {}

resource hostPool 'Microsoft.DesktopVirtualization/hostPools@2025-10-10' existing = {
  name: hostPoolName
  scope: resourceGroup(hostPoolResourceGroupName)
}

var registrationToken = first(hostPool.listRegistrationTokens().value)!.token

var imageReference = empty(galleryImageId) ? marketplaceImage : { id: galleryImageId }

resource nics 'Microsoft.Network/networkInterfaces@2024-05-01' = [
  for i in range(startIndex, instanceCount): {
    name: 'nic-${namePrefix}-${padLeft(i, 2, '0')}'
    location: location
    tags: tags
    properties: {
      enableAcceleratedNetworking: true
      ipConfigurations: [
        {
          name: 'ipconfig1'
          properties: {
            privateIPAllocationMethod: 'Dynamic'
            subnet: {
              id: subnetId
            }
          }
        }
      ]
    }
  }
]

resource vms 'Microsoft.Compute/virtualMachines@2024-07-01' = [
  for (i, idx) in range(startIndex, instanceCount): {
    name: '${namePrefix}-${padLeft(i, 2, '0')}'
    location: location
    tags: union(tags, { 'avd-host-pool': hostPoolName })
    zones: empty(zones) ? null : [zones[(i - 1) % length(zones)]]
    identity: {
      type: 'SystemAssigned' // necesaria para AADLoginForWindows
    }
    properties: {
      hardwareProfile: {
        vmSize: vmSize
      }
      licenseType: 'Windows_Client'
      securityProfile: {
        securityType: 'TrustedLaunch'
        uefiSettings: {
          secureBootEnabled: true
          vTpmEnabled: true
        }
        encryptionAtHost: encryptionAtHost
      }
      osProfile: {
        computerName: '${namePrefix}-${padLeft(i, 2, '0')}'
        adminUsername: adminUsername
        adminPassword: adminPassword
        windowsConfiguration: {
          timeZone: timeZone
          provisionVMAgent: true
        }
      }
      storageProfile: {
        imageReference: imageReference
        osDisk: {
          name: 'osdisk-${namePrefix}-${padLeft(i, 2, '0')}'
          createOption: 'FromImage'
          caching: 'ReadWrite'
          diskSizeGB: osDiskSizeGB
          managedDisk: {
            storageAccountType: osDiskType
          }
        }
      }
      networkProfile: {
        networkInterfaces: [
          {
            id: nics[idx].id
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
]

resource entraJoin 'Microsoft.Compute/virtualMachines/extensions@2024-07-01' = [
  for (i, idx) in range(startIndex, instanceCount): if (joinType == 'EntraID') {
    parent: vms[idx]
    name: 'AADLoginForWindows'
    location: location
    properties: {
      publisher: 'Microsoft.Azure.ActiveDirectory'
      type: 'AADLoginForWindows'
      typeHandlerVersion: '2.0'
      autoUpgradeMinorVersion: true
      // mdmId de Intune: mismo valor que las plantillas ARM oficiales de AVD
      settings: intuneEnrollment ? { mdmId: '0000000a-0000-0000-c000-000000000000' } : null
    }
  }
]

resource addsJoin 'Microsoft.Compute/virtualMachines/extensions@2024-07-01' = [
  for (i, idx) in range(startIndex, instanceCount): if (joinType == 'ADDS') {
    parent: vms[idx]
    name: 'JsonADDomainExtension'
    location: location
    properties: {
      publisher: 'Microsoft.Compute'
      type: 'JsonADDomainExtension'
      typeHandlerVersion: '1.3'
      autoUpgradeMinorVersion: true
      settings: {
        Name: domainName
        OUPath: empty(domainOuPath) ? null : domainOuPath
        User: '${domainName}\\${domainJoinUsername}'
        Restart: 'true'
        Options: '3'
      }
      protectedSettings: {
        Password: domainJoinPassword
      }
    }
  }
]

resource registerAgent 'Microsoft.Compute/virtualMachines/runCommands@2024-07-01' = [
  for (i, idx) in range(startIndex, instanceCount): {
    parent: vms[idx]
    name: 'Register-AvdAgent'
    location: location
    properties: {
      source: {
        script: loadTextContent('Register-AvdAgent.ps1')
      }
      protectedParameters: [
        {
          name: 'RegistrationToken'
          value: registrationToken
        }
      ]
      timeoutInSeconds: 1800
      treatFailureAsDeploymentFailure: true
    }
    dependsOn: [
      entraJoin[idx]
      addsJoin[idx]
    ]
  }
]

output sessionHostIds array = [for (i, idx) in range(startIndex, instanceCount): vms[idx].id]
```

`main.pro.bicepparam` (contraseña desde Key Vault con `getSecret()`):

```bicep
using 'main.bicep'

param hostPoolName = 'vdpool-<workload>-pro-01'
param hostPoolResourceGroupName = '<rg-avd-pro>'

param namePrefix = 'avdpro01'
param instanceCount = 4
param startIndex = 1

param vmSize = 'Standard_D8s_v5'
param galleryImageId = '<resourceId gal-avd/images/win11-25h2-avd-m365/versions/1.0.0>'

param subnetId = '<resourceId snet-avd-hosts>'

param adminUsername = '<admin-local>'
param adminPassword = az.getSecret('<subscriptionId>', '<rg-kv>', '<kv-avd-pro>', 'avd-local-admin-password')

param joinType = 'EntraID'
param intuneEnrollment = true

param tags = {
  environment: 'pro'
  workload: '<workload>'
  owner: '<owner>'
  costcenter: '<costcenter>'
}
```

Despliegue:

```powershell
az deployment group what-if --resource-group <rg-avd-hosts-pro> --parameters main.pro.bicepparam
az deployment group create  --resource-group <rg-avd-hosts-pro> --parameters main.pro.bicepparam
```

## Errores típicos

| Síntoma | Causa | Solución |
|---|---|---|
| `Unsupported argument "enable_accelerated_networking"` en el `plan` | Módulo escrito para azurerm 3.x | Usar `accelerated_networking_enabled` |
| El host no aparece en el pool; evento 3277 `INVALID_REGISTRATION_TOKEN` | Token caducado o de otro host pool | Token nuevo en `HKLM:\SOFTWARE\Microsoft\RDInfraAgent` y reiniciar `RDAgentBootLoader` |
| `NAME_ALREADY_REGISTERED` al recrear un host | Queda el objeto del host anterior en el pool | Quitar el session host del pool antes de recrear la VM |
| Host en *Needs Assistance* (UrlsAccessibleCheck) | Firewall o proxy bloqueando URLs requeridas | Abrir las URLs de AVD (comprobar con `WVDAgentUrlTool.exe`) |
| Host en *Needs Assistance* (MetaDataServiceCheck) | Proxy interceptando 169.254.169.254 | Excluir IMDS del proxy (`netsh winhttp set proxy … bypass-list="169.254.169.254"`) |
| Host *Unavailable* tras el arranque o con Start VM on Connect | `RDAgentBootLoader` tarda en arrancar | Inicio *Automatic (Delayed Start)* o subir `ServicesPipeTimeout` |
| `AADLoginForWindows` falla con `DSREG_E_MSI_TENANTID_UNAVAILABLE` | La VM no tiene identidad *system-assigned* | Activarla antes de instalar la extensión |
| La unión a Entra ID falla por nombre duplicado | Ya existe un dispositivo con ese nombre en Entra ID | Borrar el objeto antiguo o cambiar el nombre |
| "Your account is configured to prevent you from using this device" | Falta *Virtual Machine User Login* | Asignar el rol al grupo de usuarios en el RG de los hosts |
| "The sign-in method you're trying to use isn't allowed" | Conditional Access exige MFA sin método fuerte | Usar SSO o excluir la app de inicio de sesión de VM según la guía |
| La unión a AD DS falla | Sin DNS hacia los DC o OU mal escrita | DNS de la VNet apuntando a los DC y `ou_path` completo |
| Hosts preaprovisionados que no se registran tras meses apagados | El token de máquina caduca a los 90 días | Encenderlos 20 minutos cada 90 días |
| El Run Command de Terraform aparece correcto pero el host no se registra | El estado del script no se refleja en el recurso | Revisar `InstanceView` del Run Command y `%TEMP%\avd-agent\agent.log` |
| La hibernación no funciona con FSLogix | No es compatible con FSLogix ni App Attach | No activarla en esos host pools |
| Fallos en session host update con `AgentRegistrationFailureGeneric` | La imagen lleva restos de la extensión DSC | Borrar `C:\packages\plugin` de la imagen y reintentar |
