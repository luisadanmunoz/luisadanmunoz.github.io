---
title: "VM Scale Sets"
indice: compute
resumen: "Grupos de máquinas idénticas que escalan solas."
estado: documentado   # proximamente | en-curso | documentado
orden: 2
last_review: 2026-10-20
fuentes:
  - titulo: "What are Virtual Machine Scale Sets?"
    url: https://learn.microsoft.com/azure/virtual-machine-scale-sets/overview
  - titulo: "Orchestration modes for Virtual Machine Scale Sets in Azure"
    url: https://learn.microsoft.com/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-orchestration-modes
  - titulo: "Orchestration modes API comparison"
    url: https://learn.microsoft.com/azure/virtual-machine-scale-sets/orchestration-modes-api-comparison
  - titulo: "FAQ for Azure Virtual Machine Scale Sets"
    url: https://learn.microsoft.com/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-faq
  - titulo: "Compare virtual machine-based compute products"
    url: https://learn.microsoft.com/azure/virtual-machines/compare-compute-products
  - titulo: "Availability options for Azure Virtual Machines"
    url: https://learn.microsoft.com/azure/virtual-machines/availability
  - titulo: "Attach or detach a Virtual Machine to or from a Virtual Machine Scale Set"
    url: https://learn.microsoft.com/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-attach-detach-vm
  - titulo: "Upgrade policy modes for Virtual Machine Scale Sets"
    url: https://learn.microsoft.com/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-upgrade-policy
  - titulo: "Configure rolling upgrades on Virtual Machine Scale Sets"
    url: https://learn.microsoft.com/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-configure-rolling-upgrades
  - titulo: "Rolling upgrades with MaxSurge on Virtual Machine Scale Sets"
    url: https://learn.microsoft.com/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-maxsurge
  - titulo: "Azure Virtual Machine Scale Set automatic OS image upgrades"
    url: https://learn.microsoft.com/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-automatic-upgrade
  - titulo: "Automatic Guest Patching for Azure Virtual Machines and Scale Sets"
    url: https://learn.microsoft.com/azure/virtual-machines/automatic-vm-guest-patching
  - titulo: "Unsupported workloads for Azure Update Manager"
    url: https://learn.microsoft.com/azure/update-manager/unsupported-workloads
  - titulo: "Using Application Health extension with Virtual Machine Scale Sets"
    url: https://learn.microsoft.com/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-health-extension
  - titulo: "Automatic instance repairs for Azure Virtual Machine Scale Sets"
    url: https://learn.microsoft.com/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-automatic-instance-repairs
  - titulo: "Use scale-in policies with Azure Virtual Machine Scale Sets"
    url: https://learn.microsoft.com/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-scale-in-policy
  - titulo: "Instance Protection for Azure Virtual Machine Scale Set instances"
    url: https://learn.microsoft.com/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-instance-protection
  - titulo: "Terminate notification for Azure Virtual Machine Scale Set instances"
    url: https://learn.microsoft.com/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-terminate-notification
  - titulo: "Standby pools for Virtual Machine Scale Sets"
    url: https://learn.microsoft.com/azure/virtual-machine-scale-sets/standby-pools-overview
  - titulo: "Azure Spot Virtual Machines for Virtual Machine Scale Sets"
    url: https://learn.microsoft.com/azure/virtual-machine-scale-sets/use-spot
  - titulo: "Spot Priority Mix for high availability and cost savings"
    url: https://learn.microsoft.com/azure/virtual-machine-scale-sets/spot-priority-mix
  - titulo: "Best practices for autoscale"
    url: https://learn.microsoft.com/azure/azure-monitor/autoscale/autoscale-best-practices
  - titulo: "Understand autoscale settings"
    url: https://learn.microsoft.com/azure/azure-monitor/autoscale/autoscale-understanding-settings
  - titulo: "Flapping in Autoscale"
    url: https://learn.microsoft.com/azure/azure-monitor/autoscale/autoscale-flapping
  - titulo: "Use predictive autoscale to scale out before load demands in virtual machine scale sets"
    url: https://learn.microsoft.com/azure/azure-monitor/autoscale/autoscale-predictive
  - titulo: "Diagnostic settings in autoscale"
    url: https://learn.microsoft.com/azure/azure-monitor/autoscale/autoscale-diagnostics
  - titulo: "Troubleshoot Azure Monitor autoscale"
    url: https://learn.microsoft.com/azure/azure-monitor/autoscale/autoscale-troubleshoot
  - titulo: "Autoscaling (Azure Architecture Center)"
    url: https://learn.microsoft.com/azure/architecture/best-practices/auto-scaling
  - titulo: "Trusted Launch for Azure virtual machines"
    url: https://learn.microsoft.com/azure/virtual-machines/trusted-launch
  - titulo: "Trusted launch FAQs"
    url: https://learn.microsoft.com/azure/virtual-machines/trusted-launch-faq
  - titulo: "Default outbound access in Azure"
    url: https://learn.microsoft.com/azure/virtual-network/ip-services/default-outbound-access
  - titulo: "Install and manage the Azure Monitor Agent"
    url: https://learn.microsoft.com/azure/azure-monitor/agents/azure-monitor-agent-manage
  - titulo: "Manage data collection rule associations in Azure Monitor"
    url: https://learn.microsoft.com/azure/azure-monitor/data-collection/data-collection-rule-associations
  - titulo: "Azure Policy built-in definitions for Azure Virtual Machines"
    url: https://learn.microsoft.com/azure/virtual-machines/policy-reference
  - titulo: "Associate a virtual machine scale set with Flexible Orchestration to a capacity reservation group"
    url: https://learn.microsoft.com/azure/virtual-machines/capacity-reservation-associate-virtual-machine-scale-set-flex
  - titulo: "Architecture best practices for Azure Virtual Machines and scale sets (WAF)"
    url: https://learn.microsoft.com/azure/well-architected/service-guides/virtual-machines
  - titulo: "azurerm_orchestrated_virtual_machine_scale_set"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/orchestrated_virtual_machine_scale_set
  - titulo: "azurerm_monitor_autoscale_setting"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/monitor_autoscale_setting
  - titulo: "Microsoft.Compute virtualMachineScaleSets (plantillas ARM/Bicep)"
    url: https://learn.microsoft.com/azure/templates/microsoft.compute/virtualmachinescalesets
  - titulo: "Módulo Terraform Compute/VirtualMachineScaleSet"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Compute/VirtualMachineScaleSet
  - titulo: "Módulo Terraform PRO/common/assigned_identity"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/PRO/common/assigned_identity
  - titulo: "Módulo Terraform Security/Seguridad/modules/monitor_diagnostic_setting"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Security/Seguridad/modules/monitor_diagnostic_setting
---

Un **Virtual Machine Scale Set** agrupa VMs que se crean a partir de un mismo modelo y que Azure reparte entre zonas o dominios de error, escala con reglas, actualiza por lotes y repara cuando la aplicación deja de responder. El scale set no cuesta nada: se pagan las VMs, los discos y la red que usa.

Es el paso natural cuando una carga en [Virtual Machines](/recursos/compute/virtual-machines/) necesita varias instancias iguales detrás de un balanceador. Todo lo que la ficha de VMs dice sobre tamaños, discos, cifrado y salida a Internet sigue valiendo aquí; esta ficha cubre lo que añade el scale set.

## Qué es y cuándo usarlo

### Flexible o Uniform

El modo de orquestación se elige al crear el scale set y **no se puede cambiar después**. Microsoft recomienda Flexible para cargas nuevas.

| | **Flexible** (recomendado) | Uniform |
|---|---|---|
| Tipo de VM | VM estándar (`Microsoft.Compute/virtualMachines`) | VM propia del scale set |
| Gestión de cada instancia | APIs, RBAC y etiquetas de VM normales | APIs de VM del scale set |
| Instancias con garantía de dominio de error | Hasta 1000 | 100 en la tabla comparativa (3000 en las FAQ de la misma página) |
| Mezclar tamaños, SO, Spot y normales | Sí | No |
| Añadir VMs existentes | Sí (mismo grupo de recursos) | No |
| Azure Backup / Site Recovery | Sí / Sí (por PowerShell) | No / No |
| Identidad gestionada | **Solo de usuario** | Sistema o usuario |
| Salud de la aplicación | Solo extensión de salud | Extensión o sonda del balanceador |
| Salida a Internet por defecto | **No**: las instancias que crea el scale set necesitan salida explícita | Sí |
| Parcheo automático de invitado | Sí | No |
| Actualización automática de la imagen del SO | En preview | Sí |
| Service Fabric y AKS | No | Sí |

### Scale set o VMs sueltas

| Situación | Elección |
|---|---|
| Varias instancias iguales detrás de un balanceador que suben y bajan con la carga | **Scale set Flexible con autoescalado** |
| Unas pocas VMs distintas que deben repartirse entre zonas o dominios de error | Scale set Flexible sin autoescalado (sustituye a los conjuntos de disponibilidad) |
| Un servidor único o un *pet* con estado | [VM](/recursos/compute/virtual-machines/) |
| Escritorios virtuales | [AVD](/recursos/avd/session-hosts/), que tiene su propio escalado |
| Contenedores | AKS o Container Apps |

### Disponibilidad

| Despliegue | SLA | Notas |
|---|---|---|
| **Instancias en varias zonas** | **99,99 %** | `platformFaultDomainCount = 1` obligatorio con zonas |
| Instancias en varios dominios de error de una región | 99,95 % | De 1 a 3 dominios según la región |
| Spot | Sin SLA | Expulsión con 30 segundos de aviso |

- Con `platformFaultDomainCount = 1` Azure reparte al máximo y se admiten hasta 1000 instancias. Con más de un dominio de error y tamaños sin actualizaciones que conserven la memoria (series G, H, L, M y N), el límite baja a 200.
- **El reparto entre zonas no mueve VMs**: cuando hay desequilibrio, se corrige al reducir, borrando primero en la zona sobrante.
- `zone_balance = true` obliga a un reparto estricto, que puede impedir crecer si una zona no tiene capacidad.

### Cómo se mantiene sano y al día

| Pieza | Qué hace | Requisito en Flexible |
|---|---|---|
| **Extensión de salud** (Rich Health States) | Sondea un endpoint local (http, https o tcp) y marca la instancia como *Healthy*, *Unhealthy* o *Unknown* | Es la única fuente de salud admitida |
| **Reparación automática** | Reemplaza (por defecto), reimagina o reinicia instancias no sanas, como mucho el 5 % a la vez, tras un periodo de gracia de 10 a 90 minutos | Extensión de salud |
| **Actualización Rolling** | Aplica el modelo por lotes y para si demasiadas instancias quedan no sanas | Extensión de salud |
| **MaxSurge** | Crea VMs nuevas con el modelo nuevo en vez de actualizar en el sitio | Cuota de vCPU e IPs libres en la subred; no se combina con la actualización automática de imagen |
| **Parcheo automático de invitado** (`AutomaticByPlatform`) | Instala parches críticos y de seguridad por fases, con prácticas de despliegue seguro | Extensión de salud; solo imágenes de plataforma, no personalizadas |
| Actualización automática de imagen del SO | Sustituye el disco del SO cuando se publica una imagen nueva | En preview en Flexible |
| **Notificación de terminación** | Avisa por Scheduled Events antes de borrar una instancia (5-15 minutos) | No disponible en Spot |
| **Política de reducción** | *Default*, *NewestVM* u *OldestVM*: qué instancias se borran primero | — |
| **Protección de instancias** | Excluye instancias concretas de la reducción o de las acciones del scale set | — |

- **Azure Update Manager no gestiona scale sets**: el parcheo va por el parcheo automático de invitado o publicando imágenes nuevas.
- Si la aplicación no responde en el endpoint de salud, **todas las instancias quedan no sanas**, la reparación las reemplaza en bucle y las actualizaciones Rolling se detienen.

### Autoescalado

Azure Monitor autoescala con perfiles (mínimo, máximo y por defecto) y reglas por métrica o por horario.

| Práctica | Por qué |
|---|---|
| **Siempre una regla de subida y otra de bajada, con la misma métrica** | Con una sola dirección el set se queda en el máximo o en el mínimo; con métricas distintas aparece el *flapping* |
| **Margen amplio entre umbrales** (p. ej. 70 % y 30 %) | El motor descarta reducciones que provocarían subir de nuevo (*flapping*) |
| Mínimo y máximo distintos | Con mínimo = máximo nunca escala |
| Enfriamiento por regla | Cada regla tiene su propio *cooldown*; cambiar el autoescalado lo reinicia |
| **No cambiar a mano el número de instancias** | El motor lo devuelve al rango mínimo-máximo; la sincronización puede tardar hasta una hora |
| **Autoescalado predictivo** | Solo para scale sets y solo *Percentage CPU*. Necesita 7 días de historia, solo sube, y puede adelantarse hasta 1 hora. Empezar en *ForecastOnly* |
| Diagnóstico | Las categorías `AutoscaleEvaluations` y `AutoscaleScaleActions` explican por qué escaló o no |
| **Standby pools** | VMs preaprovisionadas para escalar más rápido; solo en Flexible y con un dominio de error. Con autoescalado, mejor desasignadas o hibernadas: las que están en marcha cuentan en los cálculos |

### Seguridad

Igual que en una VM, pero con dos diferencias:

| Control | En un scale set Flexible |
|---|---|
| Trusted Launch | Admitido. **El recurso de azurerm no expone `securityProfile`**: con Terraform hace falta registrar *Trusted Launch as default* en la suscripción, o desplegar con Bicep |
| Cifrado en el host | Igual que en VMs; requiere registrar `EncryptionAtHost` |
| Identidad | **Solo de usuario**. AMA debe autenticarse con ella (`mi_res_id`) |
| Login con Entra ID | Al adjuntar una VM Windows con login de Entra ID, el rol de inicio de sesión debe asignarse en el ámbito del scale set |
| Red | Sin IP pública; NSG en la subred; salida explícita por NAT Gateway o firewall |

### Monitorización

- **Azure Monitor Agent** va en el modelo del scale set, autenticado con la identidad de usuario.
- **La DCR no se puede asociar al scale set Flexible**: se asocia a cada VM. Azure Monitor recomienda hacerlo con Azure Policy para que las VMs que crea el autoescalado queden cubiertas.
- Políticas integradas: *Configure Windows Machines to be associated with a DCR or a DCE* (`eab1f514-…`) y su equivalente para Linux (`2ea82cdd-…`).

### Cómo se factura

| Concepto | Detalle |
|---|---|
| Scale set | **Sin coste propio** |
| VMs, discos y red | Como en [Virtual Machines](/recursos/compute/virtual-machines/), por cada instancia |
| Spot | Precio variable, hasta un 90 % menos; con `max_bid_price = -1` no se expulsa por precio |
| Standby pool | VMs en marcha: cómputo y almacenamiento; desasignadas: solo discos y red |
| Autoescalado | Sin coste; los logs de diagnóstico se pagan en Log Analytics |

Formas de ahorrar:

| Mecanismo | Cuándo |
|---|---|
| **Autoescalado** con mínimo ajustado | Cargas con picos y valles |
| **Spot Priority Mix** (solo Flexible) | Una base de VMs normales garantizada y el resto en Spot |
| Reservas o savings plan | Sobre el mínimo que siempre está encendido |
| Azure Hybrid Benefit | Windows Server con Software Assurance |
| Política de expulsión *Delete* en Spot | Con autoescalado, evita pagar discos de VMs expulsadas y agotar la cuota |

### Qué escenario recomiendo

| Escenario del cliente | Diseño | Por qué |
|---|---|---|
| Web o API en VMs con tráfico variable | Flexible en 3 zonas + balanceador estándar + autoescalado por CPU + Rolling + reparación | 99,99 % y coste ajustado a la carga |
| Cargas por lotes o renderizado | Flexible con Spot Priority Mix (base normal + Spot) y expulsión *Delete* | Hasta un 90 % menos sin perder toda la capacidad |
| Picos diarios predecibles | Autoescalado predictivo en *ForecastOnly* una semana; después *Enabled* | Sube antes de que llegue la carga |
| Arranques lentos (aplicaciones pesadas) | Standby pool desasignado | Escala en menos tiempo |
| Varias VMs distintas que necesitan reparto entre zonas | Flexible sin autoescalado | Sustituye a los conjuntos de disponibilidad |
| Scale sets Uniform existentes | Mantener mientras funcionen; nuevos en Flexible | El modo no se puede cambiar |
| Imágenes propias (golden image) | Azure Compute Gallery + Rolling | El parcheo automático no admite imágenes personalizadas |

### Datos que conviene llevar a la reunión

- **Flexible es el modo recomendado** y no se puede cambiar después de crear el scale set.
- **El scale set no cuesta**: se pagan las VMs.
- **Sin endpoint de salud no hay Rolling, ni reparación, ni parcheo automático**: la aplicación tiene que exponerlo.
- **Las instancias que crea un scale set Flexible no tienen salida a Internet** si no se configura NAT Gateway o firewall.
- **Update Manager no parchea scale sets.**
- **Spot Priority Mix** combina ahorro y una capacidad mínima garantizada.
- **El autoescalado necesita reglas en ambos sentidos y margen entre umbrales.**
- **Con Terraform, Trusted Launch depende de registrar *Trusted Launch as default*.**

## Decisiones de diseño

| Decisión | Lo que aplico | Por qué |
|---|---|---|
| Orquestación | **Flexible** con `azurerm_orchestrated_virtual_machine_scale_set` (nativo) | Recomendado por Microsoft; el módulo del repositorio solo hace Uniform |
| Zonas | 1, 2 y 3 por defecto, con `platform_fault_domain_count = 1` | 99,99 % y máximo reparto |
| Instancias | `instances = null` cuando hay autoescalado | El atributo es *Computed* en Flexible: Terraform no revierte lo que decide el autoescalado |
| Salud | Extensión de salud siempre (`ApplicationHealthWindows/Linux` 2.0) | Base de Rolling, reparación y parcheo |
| Actualización | Rolling al 20 % por lote, con prioridad a instancias no sanas | Lo más seguro para producción |
| Reparación | *Replace* con 30 minutos de gracia | Tiempo de arranque de la aplicación antes de actuar |
| Parches | `AutomaticByPlatform`; hotpatch con imágenes Azure Edition | Parcheo por fases con salud |
| Identidad | Identidad de usuario por scale set (módulo `PRO/common/assigned_identity`) | Flexible no admite identidad del sistema |
| Monitorización | AMA con la identidad de usuario + asociación a DCR por Azure Policy | Las VMs del autoescalado quedan cubiertas |
| Autoescalado | CPU 70/30, ventanas de 10 minutos, enfriamiento 5/10 minutos, diagnóstico a Log Analytics | Margen anti-*flapping* y trazabilidad |
| Terminación | Aviso de 5 minutos (desactivado en Spot) | La aplicación puede vaciar conexiones |
| Spot | Priority Mix con expulsión *Delete* | Ahorro sin perder la base |
| Credenciales | Windows: contraseña aleatoria en Key Vault; Linux: solo SSH | Sin secretos en el código |

Alineación con el Well-Architected Framework:

- **Fiabilidad**: zonas, salud, reparación, Rolling y notificación de terminación.
- **Seguridad**: cifrado en el host, sin IP pública, identidad de usuario, secretos en Key Vault y Trusted Launch (Bicep o TLaD).
- **Coste**: autoescalado, Spot Priority Mix, Hybrid Benefit y política de expulsión *Delete*.
- **Excelencia operativa**: todo en IaC, parcheo por plataforma, diagnóstico del autoescalado y DCR por política.
- **Rendimiento**: red acelerada y escalado predictivo.

## Módulo de Terraform

### El módulo del repositorio

[`Compute/VirtualMachineScaleSet`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Compute/VirtualMachineScaleSet) **no sirve para producción**:

| Problema | Detalle |
|---|---|
| **Solo Uniform** | Usa `azurerm_linux_virtual_machine_scale_set` y `azurerm_windows_virtual_machine_scale_set`. No hay módulo Flexible en el repositorio |
| **Autoescalado roto en Linux** | Con autoescalado pasa `instances = null`. En Uniform el atributo tiene valor por defecto `0` y no es *Computed*: cada `apply` intentaría dejar el scale set **a cero instancias** |
| **Autoescalado roto en Windows** | En `azurerm_windows_virtual_machine_scale_set`, `instances` es obligatorio: con `null` el plan falla |
| Sin `ignore_changes` en `instances` | El provider lo recomienda cuando hay autoescalado |
| Valores inseguros por defecto | `secure_boot_enabled`, `vtpm_enabled` y `encryption_at_host_enabled` a `false`; `disable_password_authentication = false` en Linux |
| Nombre por defecto | Si no se pasa `name`, se genera con `environment = "dev"` |
| Salud y mantenimiento | `upgrade_mode = "Manual"` por defecto; sin extensión de salud, reparación automática ni política Rolling |
| Autoescalado | Solo CPU, sin notificaciones ni diagnóstico |
| Contraseña | Se genera con `random_password` y solo queda en el estado y en un output; no va a Key Vault |
| Versiones | `azurerm >= 3.70.0`: no fija el mínimo que necesitan los atributos que usa |

Lo que sí reutilizo:

- [`PRO/common/assigned_identity`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/PRO/common/assigned_identity): identidad de usuario, sin bloque `provider`, compatible con `for_each`.
- [`Security/Seguridad/modules/monitor_diagnostic_setting`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Security/Seguridad/modules/monitor_diagnostic_setting): diagnóstico del autoescalado. Usa `enabled_log` y `enabled_metric`, válidos en azurerm 4.x.

Limitaciones del propio provider (azurerm 4.81) con Flexible:

- No expone `securityProfile` (Trusted Launch), `scale_in_policy` ni la actualización automática de extensiones (`enableAutomaticUpgrade`).
- `upgrade_mode` y `rolling_upgrade_policy` fuerzan la **recreación** del scale set si cambian.
- Con imágenes Windows Server Azure Edition compatibles, exige `hotpatching_enabled = true`.

### Estructura en el proyecto

```txt
/
├── providers.tf                 # azurerm >= 4.81.0, random
├── vm_scale_sets.tf             # contraseña en Key Vault, identidad, scale set, autoescalado, diagnóstico
├── dcr_association_policy.tf    # asociación a DCR por Azure Policy
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
      # Validado con 4.81.0 (rolling_upgrade_policy, priority_mix y validaciones de Flexible).
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

variable "tags" {
  description = "Tags corporativos comunes a todos los recursos."
  type        = map(string)
}
```

### `vm_scale_sets.tf`

```hcl
# =============================================================================
# VM Scale Sets en orquestación Flexible, seguros por defecto:
# zonas, cifrado en el host, sin IP pública, identidad de usuario, extensión de salud,
# reparación automática, actualización por lotes (Rolling), parcheo AutomaticByPlatform,
# Azure Monitor Agent con identidad de usuario y autoescalado con diagnóstico
#
# DEPENDENCY: grupos de recursos y subredes creados; NSG en la subred (o network_security_group_id)
# DEPENDENCY: salida explícita a Internet en la subred (NAT Gateway, firewall con UDR o reglas de
#             salida del balanceador): la orquestación Flexible no tiene salida por defecto
# DEPENDENCY: característica Microsoft.Compute/EncryptionAtHost registrada en la suscripción
# DEPENDENCY: Trusted Launch: azurerm_orchestrated_virtual_machine_scale_set no expone securityProfile;
#             registrar Microsoft.Compute/TrustedLaunchByDefaultPreview en la suscripción para que
#             los scale sets nuevos se creen con Secure Boot + vTPM (o desplegar con Bicep)
# DEPENDENCY: Key Vault con RBAC para la contraseña de Windows; la identidad de Terraform
#             necesita "Key Vault Secrets Officer" y alcance de red al vault
# DEPENDENCY: balanceador estándar (pool + regla + sonda) o Application Gateway creados antes;
#             con balanceador, el scale set debe depender de la regla
# DEPENDENCY: la aplicación responde en el endpoint de salud configurado (si no, todas las
#             instancias quedan Unhealthy/Unknown y la reparación automática las reemplaza)
# =============================================================================

variable "vm_scale_sets" {
  description = "Scale sets en orquestación Flexible (clave = nombre del recurso)."
  type = map(object({
    resource_group_name = string
    location            = string
    os_type             = string # Windows | Linux
    sku_name            = string # p. ej. Standard_D4as_v6

    # Alta disponibilidad: zonas (99,99 %) o dominios de error (99,95 %)
    zones                       = optional(list(string), ["1", "2", "3"]) # [] = regional
    zone_balance                = optional(bool, false)                   # true = reparto estricto (puede fallar si una zona no tiene capacidad)
    platform_fault_domain_count = optional(number, 1)                     # 1 = máximo reparto; obligatorio 1 con zonas

    instances = optional(number, 2) # solo sin autoescalado

    # Imagen: Marketplace o Azure Compute Gallery (exactamente una)
    source_image_reference = optional(object({
      publisher = string
      offer     = string
      sku       = string
      version   = optional(string, "latest")
    }))
    source_image_id = optional(string)
    license_type    = optional(string) # Windows_Server (Azure Hybrid Benefit), RHEL_BYOS, SLES_BYOS

    computer_name_prefix = optional(string) # Windows: 9 caracteres como máximo
    admin_username       = string
    ssh_public_key       = optional(string) # Linux (obligatoria)
    key_vault_id         = optional(string) # Windows: dónde se guarda la contraseña generada
    timezone             = optional(string) # Windows, p. ej. "Romance Standard Time"

    # Parches: AutomaticByPlatform exige extensión de salud y no admite imágenes personalizadas
    patch_mode          = optional(string, "AutomaticByPlatform") # Windows: AutomaticByPlatform | AutomaticByOS | Manual; Linux: AutomaticByPlatform | ImageDefault
    hotpatching_enabled = optional(bool, false)                   # obligatorio true con imágenes Azure Edition compatibles

    # Red: una NIC privada por instancia; sin IP pública ni reenvío
    subnet_id                                    = string
    network_security_group_id                    = optional(string)
    accelerated_networking_enabled               = optional(bool, true)
    load_balancer_backend_address_pool_ids       = optional(list(string), [])
    application_gateway_backend_address_pool_ids = optional(list(string), [])

    os_disk = optional(object({
      storage_account_type = optional(string, "Premium_LRS")
      disk_size_gb         = optional(number)
      caching              = optional(string, "ReadWrite")
    }), {})

    data_disks = optional(map(object({
      lun                  = number
      disk_size_gb         = number
      storage_account_type = optional(string, "Premium_LRS")
      caching              = optional(string, "ReadOnly")
    })), {})

    disk_encryption_set_id        = optional(string) # CMK (SSE) para SO y datos
    encryption_at_host_enabled    = optional(bool, true)
    user_assigned_identity_ids    = optional(list(string), []) # además de la identidad que crea esta ficha
    capacity_reservation_group_id = optional(string)

    # Salud de la aplicación (Rich Health States, ApplicationHealthWindows/Linux 2.0)
    health_probe = object({
      protocol            = string           # http | https | tcp
      port                = optional(number) # obligatorio con tcp
      request_path        = optional(string) # obligatorio con http/https
      interval_in_seconds = optional(number, 5)
      number_of_probes    = optional(number, 3)
      grace_period        = optional(number) # segundos; por defecto interval * probes
    })

    # Actualización del modelo: Rolling exige la extensión de salud. ForceNew en azurerm
    upgrade_mode = optional(string, "Rolling")
    rolling_upgrade_policy = optional(object({
      max_batch_instance_percent              = optional(number, 20)
      max_unhealthy_instance_percent          = optional(number, 20)
      max_unhealthy_upgraded_instance_percent = optional(number, 20)
      pause_time_between_batches              = optional(string, "PT0S")
      prioritize_unhealthy_instances_enabled  = optional(bool, true)
      maximum_surge_instances_enabled         = optional(bool, false) # crea VMs nuevas: requiere cuota e IPs libres
    }), {})

    automatic_instance_repair = optional(object({
      enabled      = optional(bool, true)
      action       = optional(string, "Replace") # Replace | Reimage | Restart
      grace_period = optional(string, "PT30M")   # PT10M - PT90M
    }), {})

    termination_notification = optional(object({
      enabled = optional(bool, true)     # no se aplica a Spot (no admite notificación de terminación)
      timeout = optional(string, "PT5M") # PT5M - PT15M
    }), {})

    # Spot Priority Mix (solo Flexible): base de VMs normales + porcentaje por encima
    spot = optional(object({
      base_regular_count            = optional(number, 0)
      regular_percentage_above_base = optional(number, 0)
      eviction_policy               = optional(string, "Delete")
      max_bid_price                 = optional(number, -1) # -1 = sin expulsión por precio
    }))

    # Autoescalado por CPU (Azure Monitor). null = número fijo de instancias
    autoscale = optional(object({
      minimum               = number
      maximum               = number
      default               = number
      scale_out_cpu_percent = optional(number, 70)
      scale_in_cpu_percent  = optional(number, 30)
      time_window           = optional(string, "PT10M")
      scale_out_cooldown    = optional(string, "PT5M")
      scale_in_cooldown     = optional(string, "PT10M")
      predictive_mode       = optional(string) # ForecastOnly | Enabled (empezar en ForecastOnly)
      predictive_look_ahead = optional(string, "PT15M")
      notification_emails   = optional(list(string), [])
    }))

    azure_monitor_agent_enabled = optional(bool, true)
    log_analytics_workspace_id  = optional(string) # diagnóstico del autoescalado

    tags = optional(map(string), {})
  }))
  default = {}

  validation {
    condition     = alltrue([for k, v in var.vm_scale_sets : contains(["Windows", "Linux"], v.os_type)])
    error_message = "os_type debe ser Windows o Linux."
  }

  validation {
    condition     = alltrue([for k, v in var.vm_scale_sets : (v.source_image_reference == null) != (v.source_image_id == null)])
    error_message = "Indica exactamente uno: source_image_reference o source_image_id."
  }

  validation {
    condition = alltrue([
      for k, v in var.vm_scale_sets :
      v.os_type == "Linux" ? v.ssh_public_key != null : v.key_vault_id != null
    ])
    error_message = "Linux necesita ssh_public_key; Windows necesita key_vault_id para guardar la contraseña."
  }

  validation {
    condition = alltrue([
      for k, v in var.vm_scale_sets :
      v.os_type == "Linux" || length(coalesce(v.computer_name_prefix, k)) <= 9
    ])
    error_message = "En Windows el prefijo del nombre de equipo tiene 9 caracteres como máximo: usa computer_name_prefix."
  }

  validation {
    condition = alltrue([
      for k, v in var.vm_scale_sets :
      alltrue([for z in v.zones : contains(["1", "2", "3"], z)]) &&
      (length(v.zones) == 0 ? v.platform_fault_domain_count >= 1 && v.platform_fault_domain_count <= 3 : v.platform_fault_domain_count == 1) &&
      (length(v.zones) > 0 || !v.zone_balance)
    ])
    error_message = "zones admite 1, 2 y 3; con zonas, platform_fault_domain_count = 1 (sin zonas, de 1 a 3); zone_balance requiere zonas."
  }

  validation {
    condition = alltrue([
      for k, v in var.vm_scale_sets :
      contains(["Premium_LRS", "Premium_ZRS", "StandardSSD_LRS", "StandardSSD_ZRS"], v.os_disk.storage_account_type) &&
      contains(["None", "ReadOnly", "ReadWrite"], v.os_disk.caching)
    ])
    error_message = "Disco del SO: Premium o Standard SSD (Standard HDD como SO se retira en 2028)."
  }

  validation {
    condition = alltrue(flatten([
      for k, v in var.vm_scale_sets : [
        for dk, d in v.data_disks :
        contains(["Premium_LRS", "Premium_ZRS", "PremiumV2_LRS", "UltraSSD_LRS", "StandardSSD_LRS", "StandardSSD_ZRS", "Standard_LRS"], d.storage_account_type) &&
        contains(["None", "ReadOnly", "ReadWrite"], d.caching)
      ]
    ])) && alltrue([for k, v in var.vm_scale_sets : length(distinct([for d in values(v.data_disks) : d.lun])) == length(v.data_disks)])
    error_message = "Tipo de disco de datos o caching no válido, o LUN repetido."
  }

  validation {
    condition = alltrue([
      for k, v in var.vm_scale_sets :
      v.os_type == "Windows" ? contains(["AutomaticByPlatform", "AutomaticByOS", "Manual"], v.patch_mode) : contains(["AutomaticByPlatform", "ImageDefault"], v.patch_mode)
    ])
    error_message = "patch_mode: Windows admite AutomaticByPlatform, AutomaticByOS o Manual; Linux, AutomaticByPlatform o ImageDefault."
  }

  validation {
    condition     = alltrue([for k, v in var.vm_scale_sets : v.source_image_id == null || v.patch_mode != "AutomaticByPlatform"])
    error_message = "El parcheo automático de invitado no admite imágenes personalizadas: con source_image_id usa otro patch_mode y publica versiones nuevas de la imagen."
  }

  validation {
    # Imágenes de Windows Server compatibles con hotpatch: el provider exige hotpatching_enabled = true
    condition = alltrue([
      for k, v in var.vm_scale_sets :
      (
        v.os_type == "Windows" && v.source_image_reference != null &&
        try(v.source_image_reference.publisher == "MicrosoftWindowsServer" && v.source_image_reference.offer == "WindowsServer" &&
          contains([
            "2022-datacenter-azure-edition-core", "2022-datacenter-azure-edition-core-smalldisk",
            "2022-datacenter-azure-edition-hotpatch", "2022-datacenter-azure-edition-hotpatch-smalldisk",
            "2025-datacenter-azure-edition", "2025-datacenter-azure-edition-smalldisk",
            "2025-datacenter-azure-edition-core", "2025-datacenter-azure-edition-core-smalldisk"
        ], v.source_image_reference.sku), false)
      ) == (v.hotpatching_enabled && v.patch_mode == "AutomaticByPlatform")
    ])
    error_message = "Con imágenes Windows Server Azure Edition compatibles, hotpatching_enabled = true y patch_mode = AutomaticByPlatform; con el resto, hotpatching_enabled = false."
  }

  validation {
    condition = alltrue([
      for k, v in var.vm_scale_sets :
      contains(["http", "https", "tcp"], v.health_probe.protocol) &&
      (v.health_probe.protocol == "tcp" ? v.health_probe.port != null && v.health_probe.request_path == null : v.health_probe.request_path != null) &&
      v.health_probe.interval_in_seconds >= 5 && v.health_probe.interval_in_seconds <= 60 &&
      v.health_probe.number_of_probes >= 1 && v.health_probe.number_of_probes <= 24 &&
      (v.health_probe.grace_period == null || coalesce(v.health_probe.grace_period, 0) <= 14400)
    ])
    error_message = "health_probe: protocol http/https/tcp; tcp exige port y no admite request_path; http/https exigen request_path; intervalo 5-60 s; sondas 1-24; gracia <= 14400 s."
  }

  validation {
    condition = alltrue([
      for k, v in var.vm_scale_sets :
      contains(["Automatic", "Manual", "Rolling"], v.upgrade_mode) &&
      contains(["Replace", "Reimage", "Restart"], v.automatic_instance_repair.action) &&
      can(regex("^PT(1[0-9]|[2-8][0-9]|90)M$", v.automatic_instance_repair.grace_period))
    ])
    error_message = "upgrade_mode: Automatic, Manual o Rolling; reparación: Replace, Reimage o Restart con gracia entre PT10M y PT90M."
  }

  validation {
    condition = alltrue([
      for k, v in var.vm_scale_sets :
      can(regex("^PT([5-9]|1[0-5])M$", v.termination_notification.timeout))
    ])
    error_message = "termination_notification.timeout entre PT5M y PT15M."
  }

  validation {
    condition = alltrue([
      for k, v in var.vm_scale_sets :
      v.spot == null || (
        try(contains(["Delete", "Deallocate"], v.spot.eviction_policy), false) &&
        try(v.spot.base_regular_count >= 0 && v.spot.base_regular_count <= 1000, false) &&
        try(v.spot.regular_percentage_above_base >= 0 && v.spot.regular_percentage_above_base <= 100, false) &&
        (v.autoscale == null || try(v.spot.eviction_policy == "Delete", false))
      )
    ])
    error_message = "Spot: eviction_policy Delete o Deallocate (Delete si hay autoescalado), base 0-1000 y porcentaje 0-100."
  }

  validation {
    condition = alltrue([
      for k, v in var.vm_scale_sets :
      v.autoscale == null || try(
        v.autoscale.minimum < v.autoscale.maximum &&
        v.autoscale.default >= v.autoscale.minimum && v.autoscale.default <= v.autoscale.maximum &&
        v.autoscale.maximum <= 1000 &&
        v.autoscale.scale_out_cpu_percent > v.autoscale.scale_in_cpu_percent &&
        (v.autoscale.predictive_mode == null || contains(["ForecastOnly", "Enabled"], coalesce(v.autoscale.predictive_mode, "x"))),
      false)
    ])
    error_message = "autoscale: minimum < maximum <= 1000, default entre ambos, umbral de salida mayor que el de entrada y predictive_mode ForecastOnly o Enabled."
  }

  validation {
    condition = alltrue([
      for k, v in var.vm_scale_sets :
      v.license_type == null || contains(["Windows_Server", "Windows_Client", "RHEL_BYOS", "SLES_BYOS", "None"], coalesce(v.license_type, "None"))
    ])
    error_message = "license_type no válido."
  }
}

# -----------------------------------------------------------------------------
# Contraseña de Windows: generada y guardada en Key Vault (nunca en tfvars)
# -----------------------------------------------------------------------------
resource "random_password" "vmss_windows_admin" {
  for_each = { for k, v in var.vm_scale_sets : k => v if v.os_type == "Windows" }

  length           = 24
  special          = true
  override_special = "!@#$%*()-_=+[]{}:?"
  min_lower        = 2
  min_upper        = 2
  min_numeric      = 2
  min_special      = 2
}

resource "azurerm_key_vault_secret" "vmss_windows_admin" {
  for_each = random_password.vmss_windows_admin

  name         = "vmss-${each.key}-admin"
  value        = each.value.result
  key_vault_id = var.vm_scale_sets[each.key].key_vault_id
  content_type = "VMSS local administrator (${var.vm_scale_sets[each.key].admin_username})"
}

# -----------------------------------------------------------------------------
# Identidad de usuario por scale set (Flexible no admite identidad del sistema)
# Módulo PRO/common/assigned_identity del repositorio
# -----------------------------------------------------------------------------
module "vmss_identity" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//PRO/common/assigned_identity?ref=main"
  for_each = var.vm_scale_sets

  name                = "id-${each.key}"
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  tags                = merge(var.tags, each.value.tags)
}

# -----------------------------------------------------------------------------
# Scale set (orquestación Flexible). Recurso nativo: el repositorio solo tiene Uniform
# -----------------------------------------------------------------------------
resource "azurerm_orchestrated_virtual_machine_scale_set" "this" {
  for_each = var.vm_scale_sets

  name                = each.key
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  sku_name            = each.value.sku_name

  # Con autoescalado, null: el número de instancias lo gobierna Azure Monitor y Terraform no lo revierte
  instances = each.value.autoscale == null ? each.value.instances : null

  zones                       = length(each.value.zones) > 0 ? each.value.zones : null
  zone_balance                = length(each.value.zones) > 0 ? each.value.zone_balance : null
  platform_fault_domain_count = each.value.platform_fault_domain_count

  source_image_id = each.value.source_image_id
  dynamic "source_image_reference" {
    for_each = each.value.source_image_reference == null ? [] : [each.value.source_image_reference]
    content {
      publisher = source_image_reference.value.publisher
      offer     = source_image_reference.value.offer
      sku       = source_image_reference.value.sku
      version   = source_image_reference.value.version
    }
  }
  license_type = each.value.license_type

  encryption_at_host_enabled    = each.value.encryption_at_host_enabled
  capacity_reservation_group_id = each.value.capacity_reservation_group_id

  identity {
    type         = "UserAssigned"
    identity_ids = concat([module.vmss_identity[each.key].id], each.value.user_assigned_identity_ids)
  }

  os_profile {
    dynamic "windows_configuration" {
      for_each = each.value.os_type == "Windows" ? [1] : []
      content {
        admin_username           = each.value.admin_username
        admin_password           = random_password.vmss_windows_admin[each.key].result
        computer_name_prefix     = coalesce(each.value.computer_name_prefix, each.key)
        timezone                 = each.value.timezone
        provision_vm_agent       = true
        enable_automatic_updates = each.value.patch_mode != "Manual"
        patch_mode               = each.value.patch_mode
        patch_assessment_mode    = each.value.patch_mode == "AutomaticByPlatform" ? "AutomaticByPlatform" : "ImageDefault"
        hotpatching_enabled      = each.value.hotpatching_enabled
      }
    }

    dynamic "linux_configuration" {
      for_each = each.value.os_type == "Linux" ? [1] : []
      content {
        admin_username                  = each.value.admin_username
        disable_password_authentication = true
        computer_name_prefix            = coalesce(each.value.computer_name_prefix, each.key)
        provision_vm_agent              = true
        patch_mode                      = each.value.patch_mode
        patch_assessment_mode           = each.value.patch_mode == "AutomaticByPlatform" ? "AutomaticByPlatform" : "ImageDefault"

        admin_ssh_key {
          username   = each.value.admin_username
          public_key = each.value.ssh_public_key
        }
      }
    }
  }

  os_disk {
    storage_account_type   = each.value.os_disk.storage_account_type
    caching                = each.value.os_disk.caching
    disk_size_gb           = each.value.os_disk.disk_size_gb
    disk_encryption_set_id = each.value.disk_encryption_set_id
  }

  dynamic "data_disk" {
    for_each = each.value.data_disks
    content {
      lun                    = data_disk.value.lun
      disk_size_gb           = data_disk.value.disk_size_gb
      storage_account_type   = data_disk.value.storage_account_type
      caching                = data_disk.value.caching
      create_option          = "Empty"
      disk_encryption_set_id = each.value.disk_encryption_set_id
    }
  }

  network_interface {
    name                          = "nic-${each.key}"
    primary                       = true
    enable_accelerated_networking = each.value.accelerated_networking_enabled
    enable_ip_forwarding          = false
    network_security_group_id     = each.value.network_security_group_id

    ip_configuration {
      name                                         = "ipconfig1"
      primary                                      = true
      subnet_id                                    = each.value.subnet_id
      load_balancer_backend_address_pool_ids       = each.value.load_balancer_backend_address_pool_ids
      application_gateway_backend_address_pool_ids = each.value.application_gateway_backend_address_pool_ids
    }
  }

  boot_diagnostics {} # almacenamiento gestionado por Azure

  # Salud de la aplicación: base de Rolling, reparación automática y parcheo AutomaticByPlatform
  extension {
    name                               = "HealthExtension"
    publisher                          = "Microsoft.ManagedServices"
    type                               = each.value.os_type == "Windows" ? "ApplicationHealthWindows" : "ApplicationHealthLinux"
    type_handler_version               = "2.0"
    auto_upgrade_minor_version_enabled = true
    settings = jsonencode(merge(
      {
        protocol          = each.value.health_probe.protocol
        intervalInSeconds = each.value.health_probe.interval_in_seconds
        numberOfProbes    = each.value.health_probe.number_of_probes
      },
      each.value.health_probe.port == null ? {} : { port = each.value.health_probe.port },
      each.value.health_probe.request_path == null ? {} : { requestPath = each.value.health_probe.request_path },
      each.value.health_probe.grace_period == null ? {} : { gracePeriod = each.value.health_probe.grace_period }
    ))
  }

  # Azure Monitor Agent autenticado con la identidad de usuario (la DCR se asocia por política)
  dynamic "extension" {
    for_each = each.value.azure_monitor_agent_enabled ? [1] : []
    content {
      name                               = each.value.os_type == "Windows" ? "AzureMonitorWindowsAgent" : "AzureMonitorLinuxAgent"
      publisher                          = "Microsoft.Azure.Monitor"
      type                               = each.value.os_type == "Windows" ? "AzureMonitorWindowsAgent" : "AzureMonitorLinuxAgent"
      type_handler_version               = "1.0"
      auto_upgrade_minor_version_enabled = true
      settings = jsonencode({
        authentication = {
          managedIdentity = {
            identifier-name  = "mi_res_id"
            identifier-value = module.vmss_identity[each.key].id
          }
        }
      })
    }
  }

  upgrade_mode = each.value.upgrade_mode

  dynamic "rolling_upgrade_policy" {
    for_each = each.value.upgrade_mode == "Rolling" ? [each.value.rolling_upgrade_policy] : []
    content {
      max_batch_instance_percent              = rolling_upgrade_policy.value.max_batch_instance_percent
      max_unhealthy_instance_percent          = rolling_upgrade_policy.value.max_unhealthy_instance_percent
      max_unhealthy_upgraded_instance_percent = rolling_upgrade_policy.value.max_unhealthy_upgraded_instance_percent
      pause_time_between_batches              = rolling_upgrade_policy.value.pause_time_between_batches
      prioritize_unhealthy_instances_enabled  = rolling_upgrade_policy.value.prioritize_unhealthy_instances_enabled
      maximum_surge_instances_enabled         = rolling_upgrade_policy.value.maximum_surge_instances_enabled
    }
  }

  automatic_instance_repair {
    enabled      = each.value.automatic_instance_repair.enabled
    action       = each.value.automatic_instance_repair.action
    grace_period = each.value.automatic_instance_repair.grace_period
  }

  dynamic "termination_notification" {
    # Spot no admite notificación de terminación
    for_each = each.value.spot == null && each.value.termination_notification.enabled ? [each.value.termination_notification.timeout] : []
    content {
      enabled = true
      timeout = termination_notification.value
    }
  }

  # Spot Priority Mix
  priority        = each.value.spot == null ? "Regular" : "Spot"
  eviction_policy = try(each.value.spot.eviction_policy, null)
  max_bid_price   = try(each.value.spot.max_bid_price, null)
  dynamic "priority_mix" {
    for_each = each.value.spot == null ? [] : [each.value.spot]
    content {
      base_regular_count            = priority_mix.value.base_regular_count
      regular_percentage_above_base = priority_mix.value.regular_percentage_above_base
    }
  }

  tags = merge(var.tags, each.value.tags)
}

# -----------------------------------------------------------------------------
# Autoescalado por CPU con margen entre umbrales (evita el flapping)
# -----------------------------------------------------------------------------
resource "azurerm_monitor_autoscale_setting" "this" {
  for_each = { for k, v in var.vm_scale_sets : k => v if v.autoscale != null }

  name                = "autoscale-${each.key}"
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  target_resource_id  = azurerm_orchestrated_virtual_machine_scale_set.this[each.key].id
  enabled             = true

  profile {
    name = "default"

    capacity {
      default = each.value.autoscale.default
      minimum = each.value.autoscale.minimum
      maximum = each.value.autoscale.maximum
    }

    rule {
      metric_trigger {
        metric_name        = "Percentage CPU"
        metric_namespace   = "microsoft.compute/virtualmachinescalesets"
        metric_resource_id = azurerm_orchestrated_virtual_machine_scale_set.this[each.key].id
        time_grain         = "PT1M"
        statistic          = "Average"
        time_window        = each.value.autoscale.time_window
        time_aggregation   = "Average"
        operator           = "GreaterThan"
        threshold          = each.value.autoscale.scale_out_cpu_percent
      }
      scale_action {
        direction = "Increase"
        type      = "ChangeCount"
        value     = 1
        cooldown  = each.value.autoscale.scale_out_cooldown
      }
    }

    rule {
      metric_trigger {
        metric_name        = "Percentage CPU"
        metric_namespace   = "microsoft.compute/virtualmachinescalesets"
        metric_resource_id = azurerm_orchestrated_virtual_machine_scale_set.this[each.key].id
        time_grain         = "PT1M"
        statistic          = "Average"
        time_window        = each.value.autoscale.time_window
        time_aggregation   = "Average"
        operator           = "LessThan"
        threshold          = each.value.autoscale.scale_in_cpu_percent
      }
      scale_action {
        direction = "Decrease"
        type      = "ChangeCount"
        value     = 1
        cooldown  = each.value.autoscale.scale_in_cooldown
      }
    }
  }

  dynamic "predictive" {
    for_each = each.value.autoscale.predictive_mode == null ? [] : [each.value.autoscale.predictive_mode]
    content {
      scale_mode      = predictive.value
      look_ahead_time = each.value.autoscale.predictive_look_ahead
    }
  }

  dynamic "notification" {
    for_each = length(each.value.autoscale.notification_emails) > 0 ? [1] : []
    content {
      email {
        custom_emails = each.value.autoscale.notification_emails
      }
    }
  }

  tags = merge(var.tags, each.value.tags)
}

# Diagnóstico del autoescalado (evaluaciones y acciones) a Log Analytics
# Módulo Security/Seguridad/modules/monitor_diagnostic_setting del repositorio
module "autoscale_diagnostics" {
  source = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Security/Seguridad/modules/monitor_diagnostic_setting?ref=main"
  for_each = {
    for k, v in var.vm_scale_sets : k => v
    if v.autoscale != null && v.log_analytics_workspace_id != null
  }

  monitor_diagnostic_setting_name = "diag-autoscale-${each.key}"
  target_resource_id              = azurerm_monitor_autoscale_setting.this[each.key].id
  log_analytics_workspace_id      = each.value.log_analytics_workspace_id
  log_analytics_destination_type  = "Dedicated"
  enabled_logs = [
    { category = "AutoscaleEvaluations" },
    { category = "AutoscaleScaleActions" }
  ]
}

# -----------------------------------------------------------------------------
# Salidas
# -----------------------------------------------------------------------------
output "vm_scale_set_ids" {
  description = "ID de cada scale set."
  value       = { for k, v in azurerm_orchestrated_virtual_machine_scale_set.this : k => v.id }
}

output "vm_scale_set_unique_ids" {
  description = "unique_id de cada scale set (para consultas de Resource Graph)."
  value       = { for k, v in azurerm_orchestrated_virtual_machine_scale_set.this : k => v.unique_id }
}

output "vm_scale_set_identities" {
  description = "Identidad de usuario de cada scale set (id, principal_id) para RBAC y AMA."
  value       = { for k, v in module.vmss_identity : k => { id = v.id, principal_id = v.principal_id } }
}

output "windows_admin_secret_ids" {
  description = "Secreto de Key Vault con la contraseña de administrador de cada scale set Windows."
  value       = { for k, v in azurerm_key_vault_secret.vmss_windows_admin : k => v.versionless_id }
}
```

### `dcr_association_policy.tf`

```hcl
# =============================================================================
# Asociación de las instancias a la DCR mediante Azure Policy (DeployIfNotExists)
# En orquestación Flexible la DCR no se asocia al scale set: se asocia a cada VM,
# también a las que crea el autoescalado. Azure Monitor recomienda hacerlo por política.
#
# Definiciones integradas:
#   eab1f514-22e3-42e3-9a1f-e1dc9199355c  Configure Windows Machines to be associated with a DCR or a DCE
#   2ea82cdd-f2e8-4500-af75-67a2e084ca74  Configure Linux Machines to be associated with a DCR or a DCE
# Roles que declara la definición: Monitoring Contributor y Log Analytics Contributor
#
# DEPENDENCY: Data Collection Rule creada (Windows o Linux)
# DEPENDENCY: si la landing zone ya asigna estas políticas en el grupo de administración, no dupliques
# =============================================================================

variable "dcr_policy_assignments" {
  description = "Asignaciones de la política de asociación a DCR por grupo de recursos (clave = sufijo del nombre)."
  type = map(object({
    resource_group_id       = string
    location                = string # región de la identidad de la asignación
    os_type                 = string # Windows | Linux
    data_collection_rule_id = string
    enforce                 = optional(bool, true)
  }))
  default = {}

  validation {
    condition     = alltrue([for k, v in var.dcr_policy_assignments : contains(["Windows", "Linux"], v.os_type)])
    error_message = "os_type debe ser Windows o Linux."
  }

  validation {
    condition     = alltrue([for k, v in var.dcr_policy_assignments : can(regex("^[a-z0-9-]{1,40}$", k))])
    error_message = "La clave forma parte del nombre de la asignación: minúsculas, números y guiones (40 como máximo)."
  }
}

resource "azurerm_resource_group_policy_assignment" "dcr_association" {
  for_each = var.dcr_policy_assignments

  name                 = "dcra-${each.key}"
  display_name         = "Asociar ${each.value.os_type} a la DCR (${each.key})"
  resource_group_id    = each.value.resource_group_id
  policy_definition_id = each.value.os_type == "Windows" ? "/providers/Microsoft.Authorization/policyDefinitions/eab1f514-22e3-42e3-9a1f-e1dc9199355c" : "/providers/Microsoft.Authorization/policyDefinitions/2ea82cdd-f2e8-4500-af75-67a2e084ca74"
  location             = each.value.location
  enforce              = each.value.enforce

  identity {
    type = "SystemAssigned"
  }

  parameters = jsonencode({
    dcrResourceId = { value = each.value.data_collection_rule_id }
    resourceType  = { value = "Microsoft.Insights/dataCollectionRules" }
  })
}

resource "azurerm_role_assignment" "dcr_policy_monitoring_contributor" {
  for_each = var.dcr_policy_assignments

  scope                            = each.value.resource_group_id
  role_definition_name             = "Monitoring Contributor"
  principal_id                     = azurerm_resource_group_policy_assignment.dcr_association[each.key].identity[0].principal_id
  principal_type                   = "ServicePrincipal"
  skip_service_principal_aad_check = true
}

resource "azurerm_role_assignment" "dcr_policy_log_analytics_contributor" {
  for_each = var.dcr_policy_assignments

  scope                            = each.value.resource_group_id
  role_definition_name             = "Log Analytics Contributor"
  principal_id                     = azurerm_resource_group_policy_assignment.dcr_association[each.key].identity[0].principal_id
  principal_type                   = "ServicePrincipal"
  skip_service_principal_aad_check = true
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

vm_scale_sets = {
  # Front web Windows en tres zonas, detrás de un balanceador estándar, con hotpatch y Hybrid Benefit
  "vmss-web-pro" = {
    resource_group_name = "<rg-app-pro>"
    location            = "<region>"
    os_type             = "Windows"
    sku_name            = "Standard_D4as_v6"
    zones               = ["1", "2", "3"]

    source_image_reference = {
      publisher = "MicrosoftWindowsServer"
      offer     = "WindowsServer"
      sku       = "2025-datacenter-azure-edition"
    }
    license_type        = "Windows_Server"
    hotpatching_enabled = true
    timezone            = "Romance Standard Time"

    computer_name_prefix = "webpro"
    admin_username       = "<admin-local>"
    key_vault_id         = "<resourceId kv-<workload>-pro>"

    subnet_id                              = "<resourceId snet-web-pro>"
    load_balancer_backend_address_pool_ids = ["<resourceId lbe-web-pro/backendAddressPools/bep-web>"]

    health_probe = {
      protocol     = "http"
      port         = 80
      request_path = "/health"
    }

    autoscale = {
      minimum             = 3
      maximum             = 12
      default             = 3
      predictive_mode     = "ForecastOnly"
      notification_emails = ["<equipo-plataforma@dominio>"]
    }
    log_analytics_workspace_id = "<resourceId log-<workload>-pro>"

    tags = {
      tier = "web"
    }
  }

  # Workers Linux por lotes: 2 VMs normales garantizadas y el 75 % del resto en Spot
  "vmss-batch-pro" = {
    resource_group_name = "<rg-app-pro>"
    location            = "<region>"
    os_type             = "Linux"
    sku_name            = "Standard_D4as_v6"
    zones               = ["1", "2", "3"]

    source_image_reference = {
      publisher = "Canonical"
      offer     = "ubuntu-24_04-lts"
      sku       = "server"
    }

    computer_name_prefix = "batchpro"
    admin_username       = "azureadmin"
    ssh_public_key       = "<clave pública SSH (ssh-rsa/ssh-ed25519 ...)>"

    subnet_id = "<resourceId snet-batch-pro>"

    health_probe = {
      protocol     = "http"
      port         = 8080
      request_path = "/healthz"
    }

    spot = {
      base_regular_count            = 2
      regular_percentage_above_base = 25
      eviction_policy               = "Delete"
    }

    autoscale = {
      minimum = 2
      maximum = 20
      default = 2
    }
    log_analytics_workspace_id = "<resourceId log-<workload>-pro>"

    tags = {
      tier = "batch"
    }
  }
}

dcr_policy_assignments = {
  "app-pro-windows" = {
    resource_group_id       = "<resourceId rg-app-pro>"
    location                = "<region>"
    os_type                 = "Windows"
    data_collection_rule_id = "<resourceId dcr-vm-windows-pro>"
  }
  "app-pro-linux" = {
    resource_group_id       = "<resourceId rg-app-pro>"
    location                = "<region>"
    os_type                 = "Linux"
    data_collection_rule_id = "<resourceId dcr-vm-linux-pro>"
  }
}
```

### Despliegue y comprobación

```powershell
# Requisitos (una vez por suscripción)
Register-AzProviderFeature -FeatureName "EncryptionAtHost" -ProviderNamespace "Microsoft.Compute"
# Trusted Launch por defecto para lo que se cree con Terraform
Register-AzProviderFeature -FeatureName "TrustedLaunchByDefaultPreview" -ProviderNamespace "Microsoft.Compute"
Get-AzProviderFeature -ProviderNamespace "Microsoft.Compute" |
    Where-Object { $_.FeatureName -in "EncryptionAtHost", "TrustedLaunchByDefaultPreview" }

terraform init
terraform plan -var-file="env/pro.tfvars" -out="pro.tfplan"
terraform apply "pro.tfplan"

# Modelo del scale set: orquestación, Trusted Launch, actualización y reparación
Get-AzVmss -ResourceGroupName "<rg-app-pro>" -VMScaleSetName "vmss-web-pro" | ForEach-Object {
    [PSCustomObject]@{
        Orchestration    = $_.OrchestrationMode
        SecurityType     = $_.VirtualMachineProfile.SecurityProfile.SecurityType
        EncryptionAtHost = $_.VirtualMachineProfile.SecurityProfile.EncryptionAtHost
        UpgradeMode      = $_.UpgradePolicy.Mode
        AutoRepair       = $_.AutomaticRepairsPolicy.Enabled
        Capacity         = $_.Sku.Capacity
    }
}

# Instancias del scale set y estado (Resource Graph: en Flexible son VMs normales)
Search-AzGraph -Query @"
resources
| where type =~ 'microsoft.compute/virtualmachines'
| where tostring(properties.virtualMachineScaleSet.id) endswith '/vmss-web-pro'
| project name, zone = tostring(zones[0]), powerState = tostring(properties.extended.instanceView.powerState.code), priority = tostring(properties.priority)
"@

# Corrección de la política de DCR para las VMs que ya existían al asignarla
Start-AzPolicyRemediation -Name "dcra-app-pro-windows-$(Get-Date -Format yyyyMMddHHmm)" `
    -PolicyAssignmentId "<resourceId rg-app-pro>/providers/Microsoft.Authorization/policyAssignments/dcra-app-pro-windows" `
    -ResourceGroupName "<rg-app-pro>"
```

Por qué no escaló (con el diagnóstico en Log Analytics):

```kusto
AutoscaleEvaluationsLog
| where TimeGenerated > ago(2h)
| where OperationName == "MetricEvaluation" or OperationName == "ScaleRuleEvaluation"
| project TimeGenerated, OperationName, MetricData, ObservedValue, Threshold, EstimateScaleResult
```

### Equivalente en Bicep

Un scale set por despliegue. Bicep sí declara Trusted Launch (`securityProfile`), la política de reducción y la actualización automática de AMA. La contraseña se lee de Key Vault con `getSecret` en el `.bicepparam`.

`sku.capacity` se aplica en cada despliegue. Con autoescalado, el motor vuelve a llevar el número de instancias a su rango mínimo-máximo.

`vmss.bicep`:

```bicep
// =============================================================================
// Un scale set en orquestación Flexible, seguro por defecto: zonas, Trusted Launch, cifrado en el
// host, identidad de usuario, extensión de salud, reparación automática, Rolling, parcheo
// AutomaticByPlatform, AMA con identidad de usuario, autoescalado con diagnóstico y asociación
// a la DCR por Azure Policy
// DEPENDENCY: subred con NSG y salida explícita; EncryptionAtHost registrada en la suscripción
// DEPENDENCY: contraseña de Windows en Key Vault (se lee con getSecret en el .bicepparam)
// DEPENDENCY: balanceador estándar o Application Gateway creados antes si se usan
// =============================================================================
param name string
param location string = resourceGroup().location

@allowed(['Windows', 'Linux'])
param osType string

param skuName string

@description('[] = regional; con zonas, platformFaultDomainCount = 1.')
param zones array = ['1', '2', '3']

@minValue(1)
@maxValue(3)
param platformFaultDomainCount int = 1

@description('Solo sin autoescalado.')
@minValue(0)
@maxValue(1000)
param instances int = 2

param imageReference object
param licenseType string?

@maxLength(9)
@description('Windows: 9 caracteres como máximo.')
param computerNamePrefix string

param adminUsername string

@secure()
param adminPassword string = ''

param sshPublicKey string = ''

@description('Obligatorio true con imágenes Windows Server Azure Edition compatibles con hotpatch.')
param hotpatchingEnabled bool = false

param timeZone string?

param subnetId string
param networkSecurityGroupId string?
param loadBalancerBackendPoolIds array = []
param applicationGatewayBackendPoolIds array = []

@allowed(['Premium_LRS', 'Premium_ZRS', 'StandardSSD_LRS', 'StandardSSD_ZRS'])
param osDiskType string = 'Premium_LRS'

param diskEncryptionSetId string?
param encryptionAtHost bool = true

@description('{ protocol, port?, requestPath?, intervalInSeconds?, numberOfProbes?, gracePeriod? }')
param healthProbe object

@allowed(['Automatic', 'Manual', 'Rolling'])
param upgradeMode string = 'Rolling'

@allowed(['Replace', 'Reimage', 'Restart'])
param repairAction string = 'Replace'
param repairGracePeriod string = 'PT30M'

@description('PT5M - PT15M; no se aplica con Spot.')
param terminationNotBeforeTimeout string = 'PT5M'

@allowed(['Default', 'NewestVM', 'OldestVM'])
param scaleInPolicy string = 'Default'

@description('null = sin Spot. { baseRegularPriorityCount, regularPriorityPercentageAboveBase, evictionPolicy }')
param spot object?

@description('null = número fijo. { minimum, maximum, default, scaleOutCpu?, scaleInCpu?, predictiveMode?, emails? }')
param autoscale object?

param logAnalyticsWorkspaceId string?
param dataCollectionRuleId string?
param tags object = {}

var isWindows = osType == 'Windows'
var isSpot = spot != null
var hasAutoscale = autoscale != null
var desRef = empty(diskEncryptionSetId ?? '') ? null : { id: diskEncryptionSetId }
var patchSettings = {
  patchMode: 'AutomaticByPlatform'
  assessmentMode: 'AutomaticByPlatform'
}

resource uami 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = {
  name: 'id-${name}'
  location: location
  tags: tags
}

resource vmss 'Microsoft.Compute/virtualMachineScaleSets@2024-11-01' = {
  name: name
  location: location
  tags: tags
  zones: empty(zones) ? null : zones
  sku: {
    name: skuName
    capacity: hasAutoscale ? autoscale!.default : instances
  }
  identity: {
    type: 'UserAssigned'
    userAssignedIdentities: {
      '${uami.id}': {}
    }
  }
  properties: {
    orchestrationMode: 'Flexible'
    platformFaultDomainCount: platformFaultDomainCount
    upgradePolicy: {
      mode: upgradeMode
      rollingUpgradePolicy: upgradeMode == 'Rolling'
        ? {
            maxBatchInstancePercent: 20
            maxUnhealthyInstancePercent: 20
            maxUnhealthyUpgradedInstancePercent: 20
            pauseTimeBetweenBatches: 'PT0S'
            prioritizeUnhealthyInstances: true
          }
        : null
    }
    automaticRepairsPolicy: {
      enabled: true
      gracePeriod: repairGracePeriod
      repairAction: repairAction
    }
    scaleInPolicy: {
      rules: [
        scaleInPolicy
      ]
    }
    priorityMixPolicy: isSpot
      ? {
          baseRegularPriorityCount: spot!.baseRegularPriorityCount
          regularPriorityPercentageAboveBase: spot!.regularPriorityPercentageAboveBase
        }
      : null
    virtualMachineProfile: {
      licenseType: licenseType
      priority: isSpot ? 'Spot' : 'Regular'
      evictionPolicy: isSpot ? spot!.evictionPolicy : null
      billingProfile: isSpot ? { maxPrice: -1 } : null
      securityProfile: {
        securityType: 'TrustedLaunch'
        uefiSettings: {
          secureBootEnabled: true
          vTpmEnabled: true
        }
        encryptionAtHost: encryptionAtHost
      }
      osProfile: {
        computerNamePrefix: computerNamePrefix
        adminUsername: adminUsername
        adminPassword: isWindows ? adminPassword : null
        allowExtensionOperations: true
        windowsConfiguration: isWindows
          ? {
              provisionVMAgent: true
              enableAutomaticUpdates: true
              timeZone: timeZone
              patchSettings: union(patchSettings, { enableHotpatching: hotpatchingEnabled })
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
              patchSettings: patchSettings
            }
      }
      storageProfile: {
        imageReference: imageReference
        osDisk: {
          createOption: 'FromImage'
          caching: 'ReadWrite'
          managedDisk: {
            storageAccountType: osDiskType
            diskEncryptionSet: desRef
          }
        }
      }
      networkProfile: {
        networkApiVersion: '2020-11-01'
        networkInterfaceConfigurations: [
          {
            name: 'nic-${name}'
            properties: {
              primary: true
              enableAcceleratedNetworking: true
              enableIPForwarding: false
              networkSecurityGroup: empty(networkSecurityGroupId ?? '') ? null : { id: networkSecurityGroupId }
              ipConfigurations: [
                {
                  name: 'ipconfig1'
                  properties: {
                    primary: true
                    subnet: {
                      id: subnetId
                    }
                    loadBalancerBackendAddressPools: [for id in loadBalancerBackendPoolIds: { id: id }]
                    applicationGatewayBackendAddressPools: [for id in applicationGatewayBackendPoolIds: { id: id }]
                  }
                }
              ]
            }
          }
        ]
      }
      diagnosticsProfile: {
        bootDiagnostics: {
          enabled: true // almacenamiento gestionado
        }
      }
      scheduledEventsProfile: isSpot
        ? null
        : {
            terminateNotificationProfile: {
              enable: true
              notBeforeTimeout: terminationNotBeforeTimeout
            }
          }
      extensionProfile: {
        extensions: [
          {
            name: 'HealthExtension'
            properties: {
              publisher: 'Microsoft.ManagedServices'
              type: isWindows ? 'ApplicationHealthWindows' : 'ApplicationHealthLinux'
              typeHandlerVersion: '2.0'
              autoUpgradeMinorVersion: true
              settings: healthProbe
            }
          }
          {
            name: isWindows ? 'AzureMonitorWindowsAgent' : 'AzureMonitorLinuxAgent'
            properties: {
              publisher: 'Microsoft.Azure.Monitor'
              type: isWindows ? 'AzureMonitorWindowsAgent' : 'AzureMonitorLinuxAgent'
              typeHandlerVersion: '1.0'
              autoUpgradeMinorVersion: true
              enableAutomaticUpgrade: true
              settings: {
                authentication: {
                  managedIdentity: {
                    'identifier-name': 'mi_res_id'
                    'identifier-value': uami.id
                  }
                }
              }
            }
          }
        ]
      }
    }
  }
}

resource autoscaleSetting 'Microsoft.Insights/autoscalesettings@2022-10-01' = if (hasAutoscale) {
  name: 'autoscale-${name}'
  location: location
  tags: tags
  properties: {
    enabled: true
    targetResourceUri: vmss.id
    profiles: [
      {
        name: 'default'
        capacity: {
          minimum: string(autoscale!.minimum)
          maximum: string(autoscale!.maximum)
          default: string(autoscale!.default)
        }
        rules: [
          {
            metricTrigger: {
              metricName: 'Percentage CPU'
              metricNamespace: 'microsoft.compute/virtualmachinescalesets'
              metricResourceUri: vmss.id
              timeGrain: 'PT1M'
              statistic: 'Average'
              timeWindow: 'PT10M'
              timeAggregation: 'Average'
              operator: 'GreaterThan'
              threshold: autoscale.?scaleOutCpu ?? 70
            }
            scaleAction: {
              direction: 'Increase'
              type: 'ChangeCount'
              value: '1'
              cooldown: 'PT5M'
            }
          }
          {
            metricTrigger: {
              metricName: 'Percentage CPU'
              metricNamespace: 'microsoft.compute/virtualmachinescalesets'
              metricResourceUri: vmss.id
              timeGrain: 'PT1M'
              statistic: 'Average'
              timeWindow: 'PT10M'
              timeAggregation: 'Average'
              operator: 'LessThan'
              threshold: autoscale.?scaleInCpu ?? 30
            }
            scaleAction: {
              direction: 'Decrease'
              type: 'ChangeCount'
              value: '1'
              cooldown: 'PT10M'
            }
          }
        ]
      }
    ]
    predictiveAutoscalePolicy: {
      scaleMode: autoscale.?predictiveMode ?? 'Disabled'
      scaleLookAheadTime: (autoscale.?predictiveMode ?? 'Disabled') == 'Disabled' ? null : 'PT15M'
    }
    notifications: empty(autoscale.?emails ?? [])
      ? []
      : [
          {
            operation: 'Scale'
            email: {
              customEmails: autoscale!.emails
            }
          }
        ]
  }
}

resource autoscaleDiagnostics 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = if (hasAutoscale && !empty(logAnalyticsWorkspaceId ?? '')) {
  name: 'diag-autoscale-${name}'
  scope: autoscaleSetting
  properties: {
    workspaceId: logAnalyticsWorkspaceId
    logAnalyticsDestinationType: 'Dedicated'
    logs: [
      {
        category: 'AutoscaleEvaluations'
        enabled: true
      }
      {
        category: 'AutoscaleScaleActions'
        enabled: true
      }
    ]
  }
}

// Asociación de cada VM (también las del autoescalado) a la DCR mediante Azure Policy
var dcrPolicyDefinitionId = isWindows
  ? '/providers/Microsoft.Authorization/policyDefinitions/eab1f514-22e3-42e3-9a1f-e1dc9199355c'
  : '/providers/Microsoft.Authorization/policyDefinitions/2ea82cdd-f2e8-4500-af75-67a2e084ca74'

resource dcrPolicy 'Microsoft.Authorization/policyAssignments@2024-04-01' = if (!empty(dataCollectionRuleId ?? '')) {
  name: 'dcra-${name}'
  location: location
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    displayName: 'Asociar ${osType} a la DCR (${name})'
    policyDefinitionId: dcrPolicyDefinitionId
    parameters: {
      dcrResourceId: {
        value: dataCollectionRuleId
      }
      resourceType: {
        value: 'Microsoft.Insights/dataCollectionRules'
      }
    }
  }
}

// Monitoring Contributor y Log Analytics Contributor (roles que declara la definición)
var dcrPolicyRoles = [
  '749f88d5-cbae-40b8-bcfc-e573ddc772fa'
  '92aaf0da-9dab-42b6-94a3-d43ce8d16293'
]

resource dcrPolicyRoleAssignments 'Microsoft.Authorization/roleAssignments@2022-04-01' = [
  for roleId in dcrPolicyRoles: if (!empty(dataCollectionRuleId ?? '')) {
    name: guid(resourceGroup().id, 'dcra-${name}', roleId)
    properties: {
      roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', roleId)
      principalId: dcrPolicy!.identity.principalId
      principalType: 'ServicePrincipal'
    }
  }
]

output id string = vmss.id
output identityId string = uami.id
output identityPrincipalId string = uami.properties.principalId
```

`vmss-web-pro.bicepparam` (Windows):

```bicep
using 'vmss.bicep'

param name = 'vmss-web-pro'
param osType = 'Windows'
param skuName = 'Standard_D4as_v6'
param zones = ['1', '2', '3']

param imageReference = {
  publisher: 'MicrosoftWindowsServer'
  offer: 'WindowsServer'
  sku: '2025-datacenter-azure-edition'
  version: 'latest'
}
param licenseType = 'Windows_Server'
param hotpatchingEnabled = true
param timeZone = 'Romance Standard Time'

param computerNamePrefix = 'webpro'
param adminUsername = '<admin-local>'
// Contraseña en Key Vault: el despliegue necesita permiso de lectura de secretos
// y el vault con enabledForTemplateDeployment = true
param adminPassword = az.getSecret('<subscriptionId>', '<rg-security-pro>', '<kv-<workload>-pro>', 'vmss-vmss-web-pro-admin')

param subnetId = '<resourceId snet-web-pro>'
param loadBalancerBackendPoolIds = [
  '<resourceId lbe-web-pro/backendAddressPools/bep-web>'
]

param healthProbe = {
  protocol: 'http'
  port: 80
  requestPath: '/health'
  intervalInSeconds: 5
  numberOfProbes: 3
}

param autoscale = {
  minimum: 3
  maximum: 12
  default: 3
  predictiveMode: 'ForecastOnly'
  emails: [
    '<equipo-plataforma@dominio>'
  ]
}
param logAnalyticsWorkspaceId = '<resourceId log-<workload>-pro>'
param dataCollectionRuleId = '<resourceId dcr-vm-windows-pro>'

param tags = {
  environment: 'pro'
  workload: '<workload>'
  owner: '<owner>'
  costcenter: '<costcenter>'
  tier: 'web'
}
```

`vmss-batch-pro.bicepparam` (Linux con Spot):

```bicep
using 'vmss.bicep'

param name = 'vmss-batch-pro'
param osType = 'Linux'
param skuName = 'Standard_D4as_v6'
param zones = ['1', '2', '3']

param imageReference = {
  publisher: 'Canonical'
  offer: 'ubuntu-24_04-lts'
  sku: 'server'
  version: 'latest'
}

param computerNamePrefix = 'batchpro'
param adminUsername = 'azureadmin'
param sshPublicKey = '<clave pública SSH (ssh-rsa/ssh-ed25519 ...)>'

param subnetId = '<resourceId snet-batch-pro>'

param healthProbe = {
  protocol: 'http'
  port: 8080
  requestPath: '/healthz'
}

// 2 VMs normales garantizadas y el 75 % del resto en Spot
param spot = {
  baseRegularPriorityCount: 2
  regularPriorityPercentageAboveBase: 25
  evictionPolicy: 'Delete'
}

param autoscale = {
  minimum: 2
  maximum: 20
  default: 2
}
param logAnalyticsWorkspaceId = '<resourceId log-<workload>-pro>'
param dataCollectionRuleId = '<resourceId dcr-vm-linux-pro>'

param tags = {
  environment: 'pro'
  workload: '<workload>'
  owner: '<owner>'
  costcenter: '<costcenter>'
  tier: 'batch'
}
```

Despliegue:

```powershell
Get-ChildItem -Filter "vmss-*.bicepparam" | ForEach-Object {
    New-AzResourceGroupDeployment -ResourceGroupName "<rg-app-pro>" -TemplateParameterFile $_.FullName -Name ("vmss-" + $_.BaseName)
}
```

## Errores típicos

| Síntoma | Causa | Solución |
|---|---|---|
| El scale set baja a cero instancias en cada `apply` | Módulo Uniform del repositorio con autoescalado (`instances = null` → `0`) | Flexible con `instances = null`, o `ignore_changes = [instances]` en Uniform |
| `The argument "instances" is required` en Windows | Módulo Uniform del repositorio con autoescalado | Igual que el anterior |
| `health extension is required when upgrade_mode is set to Rolling` | Rolling sin extensión de salud | Mantener `HealthExtension` en el modelo |
| `when patch_mode is set to AutomaticByPlatform, an application health extension must be configured` | Parcheo por plataforma sin extensión de salud | Igual que el anterior |
| `when using a hotpatching enabled image, hotpatching_enabled must be set to true` | Imagen Windows Server Azure Edition compatible con hotpatch | `hotpatching_enabled = true` (la validación del root lo exige) |
| El plan quiere **recrear** el scale set | Cambio de `upgrade_mode`, `rolling_upgrade_policy`, `zone_balance` o eliminación de una zona | Decidirlo antes de producción; si no, desplegar un scale set nuevo y migrar el tráfico |
| Todas las instancias *Unhealthy* o *Unknown* y la reparación las reemplaza en bucle | La aplicación no responde en el endpoint de salud o tarda más que el periodo de gracia | Revisar puerto y ruta; subir `grace_period` de la extensión y de la reparación |
| El despliegue Rolling se detiene | Más instancias no sanas que `max_unhealthy_*` | Corregir la salud de la aplicación y volver a aplicar el modelo |
| Las instancias no salen a Internet (Windows Update, paquetes) | Las VMs que crea un scale set Flexible no tienen salida por defecto | NAT Gateway o firewall con UDR en la subred |
| AMA instalado pero sin datos | Falta la asociación a la DCR en cada VM | Asignación de la política y corrección para las VMs existentes |
| AMA no se autentica | Sin `authentication.managedIdentity` (Flexible no tiene identidad del sistema) | `mi_res_id` con la identidad de usuario |
| Scale set creado sin Trusted Launch desde Terraform | El provider no expone `securityProfile`; o la imagen o el tamaño no admiten Trusted Launch | Registrar `TrustedLaunchByDefaultPreview` antes de crear (o usar Bicep) y elegir imagen y tamaño compatibles |
| El autoescalado no reduce nunca | *Flapping*: umbrales demasiado cerca | Más margen (p. ej. 70/30) |
| El autoescalado no actúa | Mínimo igual a máximo, enfriamiento activo o regla en un solo sentido | Revisar `AutoscaleEvaluationsLog` |
| El número de instancias vuelve solo a otro valor | Cambio manual fuera del rango del autoescalado | Cambiar mínimo y máximo, no las instancias |
| El predictivo no muestra datos | Menos de 7 días de historia | Esperar en *ForecastOnly* |
| `OperationNotAllowed` por cuota al escalar o con MaxSurge | Cuota de vCPU de la familia o de Spot agotada | Pedir cuota antes; MaxSurge necesita margen extra |
| Spot sin capacidad o expulsadas a la vez | Capacidad Spot de la región o el tamaño | `base_regular_count` > 0 y Spot Placement Score para elegir región y tamaño |
| No se puede activar la notificación de terminación | Instancias Spot | No se admite en Spot: Scheduled Events con 30 segundos |
| Rolling falla en Flexible con un error de política de actualización | La página de modos de orquestación aún lista la política de actualización como no admitida, mientras la de Rolling la documenta para Flexible | Validar en `dev` antes de `pro`; si la región lo rechaza, `upgrade_mode = "Manual"` (también recrea el scale set) |
| Windows: el prefijo de nombre se rechaza | Más de 9 caracteres | `computer_name_prefix` corto |
