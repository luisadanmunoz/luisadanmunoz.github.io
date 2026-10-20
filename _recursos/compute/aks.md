---
title: "AKS"
indice: compute
resumen: "Kubernetes gestionado por Azure."
estado: documentado   # proximamente | en-curso | documentado
orden: 3
last_review: 2026-10-20
fuentes:
  - titulo: "What is Azure Kubernetes Service (AKS) Automatic?"
    url: https://learn.microsoft.com/azure/aks/intro-aks-automatic
  - titulo: "Free, Standard, and Premium pricing tiers for AKS cluster management"
    url: https://learn.microsoft.com/azure/aks/free-standard-pricing-tiers
  - titulo: "AKS long-term support for Kubernetes versions"
    url: https://learn.microsoft.com/azure/aks/long-term-support
  - titulo: "Supported Kubernetes versions in AKS"
    url: https://learn.microsoft.com/azure/aks/supported-kubernetes-versions
  - titulo: "Platform-initiated upgrades in AKS"
    url: https://learn.microsoft.com/azure/aks/platform-initiated-upgrades
  - titulo: "Automatically upgrade an AKS cluster"
    url: https://learn.microsoft.com/azure/aks/auto-upgrade-cluster
  - titulo: "Autoupgrade node OS images"
    url: https://learn.microsoft.com/azure/aks/auto-upgrade-node-os-image
  - titulo: "Use planned maintenance to schedule and control upgrades for your AKS cluster"
    url: https://learn.microsoft.com/azure/aks/planned-maintenance
  - titulo: "AKS cluster upgrade practices"
    url: https://learn.microsoft.com/azure/architecture/operator-guides/aks/aks-upgrade-practices
  - titulo: "Baseline architecture for an AKS cluster"
    url: https://learn.microsoft.com/azure/architecture/reference-architectures/containers/aks/baseline-aks
  - titulo: "Architecture best practices for Azure Kubernetes Service (AKS)"
    url: https://learn.microsoft.com/azure/well-architected/service-guides/azure-kubernetes-service
  - titulo: "Secure your AKS cluster"
    url: https://learn.microsoft.com/azure/aks/secure-aks
  - titulo: "Plan control plane networking for AKS"
    url: https://learn.microsoft.com/azure/aks/plan-control-plane-networking
  - titulo: "Use API Server VNet Integration in AKS"
    url: https://learn.microsoft.com/azure/aks/api-server-vnet-integration
  - titulo: "Create a private AKS cluster"
    url: https://learn.microsoft.com/azure/aks/private-clusters
  - titulo: "Azure CNI Overlay networking in AKS"
    url: https://learn.microsoft.com/azure/aks/concepts-network-azure-cni-overlay
  - titulo: "AKS CNI networking overview"
    url: https://learn.microsoft.com/azure/aks/concepts-network-cni-overview
  - titulo: "Best practices for network connectivity and security in AKS"
    url: https://learn.microsoft.com/azure/aks/operator-best-practices-network
  - titulo: "Secure traffic between pods using network policies in AKS"
    url: https://learn.microsoft.com/azure/aks/use-network-policies
  - titulo: "Customize cluster egress with outbound types in AKS"
    url: https://learn.microsoft.com/azure/aks/egress-outboundtype
  - titulo: "Limit network traffic with Azure Firewall in AKS"
    url: https://learn.microsoft.com/azure/aks/limit-egress-traffic
  - titulo: "Outbound network and FQDN rules for AKS clusters"
    url: https://learn.microsoft.com/azure/aks/outbound-rules-control-egress
  - titulo: "Managed identities in AKS overview"
    url: https://learn.microsoft.com/azure/aks/managed-identity-overview
  - titulo: "Use a pre-created kubelet managed identity in AKS"
    url: https://learn.microsoft.com/azure/aks/pre-created-kubelet-managed-identity
  - titulo: "Access and identity options for AKS"
    url: https://learn.microsoft.com/azure/aks/concepts-identity
  - titulo: "Manage local accounts with AKS-managed Microsoft Entra integration"
    url: https://learn.microsoft.com/azure/aks/local-accounts
  - titulo: "Use kubelogin to authenticate users in AKS"
    url: https://learn.microsoft.com/azure/aks/kubelogin-authentication
  - titulo: "Microsoft Entra Workload ID with AKS"
    url: https://learn.microsoft.com/azure/aks/workload-identity-overview
  - titulo: "Use deployment safeguards to enforce best practices in AKS"
    url: https://learn.microsoft.com/azure/aks/deployment-safeguards
  - titulo: "Manage system node pools in AKS"
    url: https://learn.microsoft.com/azure/aks/use-system-pools
  - titulo: "Add an Azure Spot node pool to an AKS cluster"
    url: https://learn.microsoft.com/azure/aks/spot-node-pool
  - titulo: "Storage options for applications in AKS (ephemeral OS disks)"
    url: https://learn.microsoft.com/azure/aks/concepts-storage
  - titulo: "Best practices for cost optimization in AKS"
    url: https://learn.microsoft.com/azure/aks/best-practices-cost
  - titulo: "Enable monitoring for AKS clusters"
    url: https://learn.microsoft.com/azure/azure-monitor/containers/kubernetes-monitoring-enable
  - titulo: "Monitor AKS"
    url: https://learn.microsoft.com/azure/aks/monitor-aks
  - titulo: "Monitor Kubernetes clusters using Azure Monitor and cloud native tools"
    url: https://learn.microsoft.com/azure/azure-monitor/containers/monitor-kubernetes
  - titulo: "AKS monitoring data reference"
    url: https://learn.microsoft.com/azure/aks/monitor-aks-reference
  - titulo: "Azure built-in roles"
    url: https://learn.microsoft.com/azure/role-based-access-control/built-in-roles
  - titulo: "azurerm_kubernetes_cluster"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/kubernetes_cluster
  - titulo: "azurerm_kubernetes_cluster_node_pool"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/kubernetes_cluster_node_pool
  - titulo: "azurerm_kubernetes_cluster_deployment_safeguard"
    url: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/kubernetes_cluster_deployment_safeguard
  - titulo: "Microsoft.ContainerService managedClusters (plantillas ARM/Bicep)"
    url: https://learn.microsoft.com/azure/templates/microsoft.containerservice/managedclusters
  - titulo: "Módulo Terraform Containers/AKS"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Containers/AKS
  - titulo: "Módulo Terraform Containers/Kubernetes"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Containers/Kubernetes
  - titulo: "Módulo Terraform PRO/services/aks"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/PRO/services/aks
  - titulo: "Módulo Terraform PRO/common/assigned_identity"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/PRO/common/assigned_identity
  - titulo: "Módulo Terraform Gobernanza/Gobernanza/modules/role_assignment"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Gobernanza/Gobernanza/modules/role_assignment
  - titulo: "Módulo Terraform Security/Seguridad/modules/monitor_diagnostic_setting"
    url: https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Security/Seguridad/modules/monitor_diagnostic_setting
---

**Azure Kubernetes Service (AKS)** es Kubernetes gestionado: Azure opera el plano de control (API server, etcd, scheduler) y el cliente gestiona los nodos, que son conjuntos de escalado de VMs en su suscripción. Tiene dos modos: **AKS Automatic**, con la configuración de producción ya aplicada y los nodos gestionados por Azure, y **AKS Standard**, donde cada decisión de red, identidad, nodos y actualizaciones la toma el equipo. Esta ficha despliega AKS Standard con la línea base de seguridad de Microsoft y explica cuándo conviene Automatic. Las imágenes salen de [Container Registry](/recursos/compute/container-registry/).

## Qué es y cuándo usarlo

### AKS frente a las alternativas de contenedores

| Necesidad | Servicio |
|---|---|
| Plataforma de contenedores para muchos equipos, con control total de Kubernetes (operadores, CRD, Helm, GitOps, service mesh) | **AKS** |
| Microservicios o APIs sin gestionar Kubernetes, con escalado a cero | [Container Apps](/recursos/compute/container-apps/) |
| Un contenedor o un trabajo puntual, sin orquestación | [Container Instances](/recursos/compute/container-instances/) |
| Kubernetes fuera de Azure gestionado desde Azure | [Azure Arc para Kubernetes](/recursos/hybrid/azure-arc-para-kubernetes/) |

### AKS Automatic o AKS Standard

| | **AKS Automatic** | **AKS Standard** |
|---|---|---|
| Recomendación de Microsoft | **Opción por defecto para la mayoría de cargas de producción** | Cuando hace falta control manual de red, nodos o actualizaciones |
| Plan | Standard incluido (SLA, hasta 5000 nodos y SLA de pod readiness) | Free, Standard o Premium |
| Nodos | Node autoprovisioning (elige el SKU por los requests de los pods) | Pools que define el equipo |
| Seguridad por defecto | Entra ID + Azure RBAC, workload identity, deployment safeguards en modo Enforce, API Server VNet Integration | Todo opcional |
| Actualizaciones | Canal `stable` y SO de nodos gestionados | Las configura el equipo |
| Monitorización | Managed Prometheus y Container insights activados | Se configura aparte |
| Limitaciones | Sin nodos Windows; un clúster Standard no se puede convertir en Automatic | — |
| Terraform | `azurerm_kubernetes_automatic_cluster` (azurerm 4.81 o posterior) | `azurerm_kubernetes_cluster` |

### Planes del plano de control

| | Free | **Standard** | Premium |
|---|---|---|---|
| SLA del API server | No | **99,95 % con zonas; 99,9 % sin ellas** | Igual que Standard |
| Nodos por clúster | Hasta 1000 (recomendado para menos de 10) | Hasta 5000 | Hasta 5000 |
| Soporte de versiones | Comunidad (unos 12 meses por versión menor) | Comunidad | **LTS: 24 meses** (plan de soporte `AKSLongTermSupport`) |
| Uso | Desarrollo y pruebas | Producción | Producción que no puede seguir el ritmo de versiones |

En regiones con zonas, el plano de control se reparte entre zonas automáticamente. Los nodos se pagan siempre como VMs, discos y red, en cualquier plan.

### Fechas que afectan a clústeres existentes

| Fecha | Qué ocurre | Acción |
|---|---|---|
| **31 de octubre de 2026** | Se retiran las imágenes de **Azure Linux 2.0** (sin parches desde el 30 de noviembre de 2025): los pools no podrán escalar | Migrar a `AzureLinux3` |
| 30 de septiembre de 2026 | Azure NPM deja de estar soportado en nodos Windows | Otra política de red |
| Noviembre de 2026 | Fin de parches críticos para el NGINX del complemento de application routing | Migrar a Application Routing con Gateway API |
| **1 de junio de 2027** | AKS actualiza solo los clústeres que sigan en versiones sin soporte tras 60 días de gracia, **sin respetar ventanas de mantenimiento, sin parar por APIs obsoletas y saltándose los PodDisruptionBudget** | Mantener versiones soportadas |
| 30 de septiembre de 2028 | Fin de Azure NPM en Linux | **Azure CNI con Cilium** |
| 31 de marzo de 2028 | Retirada de **kubenet** | **Azure CNI Overlay** |

### Seguridad: línea base de Microsoft

| Área | Control | Por defecto en AKS Standard |
|---|---|---|
| API server | Clúster privado o rangos de IP autorizados; **API Server VNet Integration** | Público |
| Autenticación | Entra ID + **Azure RBAC**; **cuentas locales desactivadas** (son una puerta trasera sin auditoría) | Cuentas locales activas |
| Identidades | Identidades administradas; workload identity para los pods (pod-managed identity está obsoleto) | Identidad de sistema |
| Red interna | Políticas de red (Cilium) | Sin políticas |
| Salida | UDR hacia Azure Firewall con el FQDN tag `AzureKubernetesService` (los NSG no sirven: las dependencias son FQDN) | Salida a Internet sin restricción |
| Admisión | Azure Policy, **deployment safeguards** y Pod Security Standards | Desactivado |
| Secretos | CSI de Key Vault con rotación; cifrado de etcd con KMS | — |
| Nodos | Cifrado en host, canal de SO de nodos, Image Cleaner | Sin cifrado en host |
| Amenazas | Defender for Containers | Desactivado |
| Auditoría | Diagnóstico `kube-audit-admin` y `guard` | Sin registros |

### Red

| Decisión | Recomendación |
|---|---|
| Modelo de IPs | **Azure CNI Overlay**: pods en un rango privado que no consume IPs de la VNet, hasta 5000 nodos y 250 pods por nodo (kubenet: 400 nodos). El paso de kubenet a Overlay es de un solo sentido |
| Plano de datos y políticas | **Azure CNI con Cilium** (`network_data_plane` y `network_policy` en `cilium`). kubenet no puede pasar directamente a Cilium |
| API server | Microsoft recomienda en general un clúster **público** con VNet Integration y rangos autorizados; **privado** cuando hay requisitos de seguridad o cumplimiento |
| API Server VNet Integration | Subred delegada a `Microsoft.ContainerService/managedClusters`, mínimo **/28**, reutilizable por varios clústeres de la VNet. AKS reserva al menos 9 IPs. No disponible en qatarcentral ni con VNet encryption en SKUs v4 o posteriores |
| DNS privado | `System` (zona en el grupo de nodos) o zona propia en el hub: `private.<región>.azmk8s.io` con VNet Integration y `privatelink.<región>.azmk8s.io` sin ella. La zona propia no se puede cambiar después |
| Salida | `userDefinedRouting` hacia el firewall; al menos 20 IPs públicas en el firewall para no agotar SNAT |
| Rangos reservados | `169.254.0.0/16`, `172.30.0.0/16`, `172.31.0.0/16` y `192.0.2.0/24` no se pueden usar para pods, servicios ni la VNet |

### Cómo se factura

| Concepto | Detalle |
|---|---|
| Plano de control | Gratis en Free; tarifa por hora y clúster en Standard y Premium |
| Nodos | VMs, discos de SO (el disco efímero va incluido en el precio de la VM) y discos de datos |
| Red | Load balancer, IPs públicas, NAT o firewall y tráfico de salida |
| Observabilidad | Ingesta en Log Analytics (`kube-audit` completo es la categoría más cara) |
| Opcionales | Defender for Containers, Advanced Container Networking Services, Azure Monitor workspace |

Formas de ahorrar: escalador automático y pools de usuario que bajan a cero, **pools Spot** para cargas interrumpibles, VMs Arm64, reservas o savings plans para la base estable, node autoprovisioning, VPA para ajustar requests, `start/stop` de clústeres de desarrollo, el complemento de análisis de costes (Standard o Premium) y `kube-audit-admin` en lugar de `kube-audit`.

### Qué escenario recomiendo

| Escenario del cliente | Diseño | Por qué |
|---|---|---|
| Nueva plataforma de contenedores Linux sin requisitos especiales | **AKS Automatic** | Microsoft lo recomienda por defecto; menos decisiones y menos operación |
| Producción con hub-spoke, firewall central y requisitos de red propios | **AKS Standard** con la línea base de esta ficha | Control de IPs, salida, DNS y pools |
| Nodos Windows | AKS Standard | Automatic no admite Windows |
| Entorno regulado o sin tiempo para actualizar cada año | Standard + Premium con LTS | 24 meses por versión |
| Desarrollo y pruebas | Free, un pool de sistema pequeño y `start/stop` | Coste mínimo |
| Clústeres con kubenet o Azure NPM | Plan de migración a CNI Overlay y Cilium | Retiradas en 2028 |
| Clústeres con Azure Linux 2.0 | Migración inmediata a `AzureLinux3` | Imágenes retiradas el 31 de octubre de 2026 |
| Cargas batch o de CI | Pool Spot con escalado desde cero | Mucho más barato y tolerante a desalojos |

### Datos que conviene llevar a la reunión

- **AKS Automatic es la recomendación por defecto de Microsoft** para producción; Standard, cuando hace falta control.
- **Free no tiene SLA**: producción siempre en Standard o Premium.
- **LTS solo existe en Premium.**
- **Desde el 1 de junio de 2027, un clúster sin soporte se actualiza solo**, sin ventanas ni PDB.
- **Azure Linux 2.0 deja de escalar el 31 de octubre de 2026.**
- **kubenet se retira el 31 de marzo de 2028** y Azure NPM en 2028: Overlay con Cilium.
- **Las cuentas locales están activas por defecto** y no dejan rastro de auditoría.
- **Los NSG no bastan para controlar la salida**: hace falta un firewall con FQDN.
- **`kube-audit` completo dispara el coste** de Log Analytics: `kube-audit-admin`.

## Decisiones de diseño

| Decisión | Lo que aplico | Por qué |
|---|---|---|
| Modo | AKS Standard con `azurerm_kubernetes_cluster` nativo | Control de red e integración con hub-spoke; los módulos del repositorio fallan o se quedan cortos |
| Plan | Standard; Premium solo con LTS (validado) | SLA |
| API server | Privado + **API Server VNet Integration**, sin FQDN público | Tráfico nodo-API server siempre privado y sin túnel |
| DNS | `System` o zona propia con formato validado; zona propia exige `vnet_id` | AKS enlaza la zona a la VNet del clúster |
| Red | Azure CNI Overlay + Cilium; rangos sin valores por defecto | Escala, políticas de red y sin kubenet ni NPM |
| Salida | `userDefinedRouting`; exige `route_table_id` | Todo sale por el firewall |
| Identidades | De usuario para plano de control y kubelet, con permisos creados **antes** que el clúster | Sin errores de aprovisionamiento ni esperas de replicación |
| Permisos del plano de control | Network Contributor en subredes, VNet y tabla de rutas; Private DNS Zone Contributor en la zona; Managed Identity Operator sobre kubelet | Los que pide la documentación |
| Acceso | Entra ID + Azure RBAC, cuentas locales desactivadas, grupo de administradores obligatorio | Todo acceso auditado |
| Pods | OIDC + workload identity; CSI de Key Vault con rotación | Sin secretos en el clúster |
| Admisión | Azure Policy + deployment safeguards (`Warn`, `Baseline`) | Pasar a `Enforce` cuando los manifiestos cumplan |
| Pool de sistema | 3 nodos zonales, `CriticalAddonsOnly`, AzureLinux3, disco efímero, cifrado en host, sin serie B | Recomendaciones de pools de sistema |
| Pools de usuario | Escalado automático; Spot con etiqueta y taint declarados y sin surge | Coste y sin diferencias en el plan |
| Actualizaciones | Canal `stable` + `NodeImage`, dos ventanas de mantenimiento obligatorias; `kubernetes_version` nula con canal | Parches sin intervención en horario controlado |
| Seguridad adicional | Defender, Image Cleaner (7 días) | Línea base |
| Monitorización | Container insights con identidad (DCR con ContainerLogV2) y diagnóstico `kube-apiserver`, `kube-audit-admin`, `kube-controller-manager`, `cluster-autoscaler` y `guard` en tablas dedicadas | Lo que recomienda Microsoft como punto de partida |
| ACR | Identidad kubelet con `Container Registry Repository Reader` (o `AcrPull` en modo legacy) | Coherente con el registro en modo ABAC |
| Bloqueo | `CanNotDelete` | Evita borrar el clúster |

Alineación con el Well-Architected Framework:

- **Fiabilidad**: plan Standard con SLA, pool de sistema zonal de 3 nodos, surge en actualizaciones y ventanas de mantenimiento.
- **Seguridad**: API privado, Entra ID sin cuentas locales, workload identity, políticas de red, salida filtrada, safeguards, Defender y cifrado en host.
- **Coste**: escalado automático, Spot, disco efímero, análisis de costes y registros mínimos.
- **Excelencia operativa**: IaC, canales automáticos y auditoría.
- **Rendimiento**: Overlay con Cilium y discos efímeros.

## Módulo de Terraform

### Los módulos del repositorio

Ninguno sirve para un clúster de producción con azurerm 4.x:

| Módulo | Problema |
|---|---|
| [`Containers/AKS`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Containers/AKS) | Su `versions.tf` admite azurerm `>= 3.70.0`, pero usa nombres de 4.x (`auto_scaling_enabled`), así que falla con 3.x. Valores por defecto inseguros: `sku_tier = "Free"`, `private_cluster_enabled = false`, `azure_policy_enabled = false`, `local_account_disabled = false`. Usa el bloque `maintenance_window` heredado, `node_taints` está comentado en todos los pools y `environment` vale `dev` por defecto |
| [`Containers/Kubernetes/modules/kubernetes_cluster`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Containers/Kubernetes/modules/kubernetes_cluster) | **No pasa `validate`** (comprobado con azurerm 4.81): `service_principal` es una variable `sensitive` y se usa en un `for_each` dinámico. No expone `host_encryption_enabled`, `kubelet_identity`, `key_vault_secrets_provider`, `maintenance_window_auto_upgrade`, `maintenance_window_node_os`, `auto_scaler_profile`, `monitor_metrics` ni `node_resource_group`, y no devuelve la identidad kubelet. Además, el `versions.tf` de `Containers/Kubernetes` declara un bloque `provider`, por lo que solo los submódulos admiten `for_each` |
| [`Containers/Kubernetes/modules/kubernetes_cluster_node_pool`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Containers/Kubernetes/modules/kubernetes_cluster_node_pool) | Valida, pero no expone `host_encryption_enabled` ni `eviction_policy`, que el provider exige para Spot. Usa `container_log_max_line`, obsoleto y eliminado en azurerm 5.0 (`container_log_max_files`) |
| [`PRO/services/aks`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/PRO/services/aks) | **No reutilizable**: kubenet + Calico (kubenet se retira en 2028), CIDR fijos en el código, 2 nodos `Standard_D2_v2` fijos, AGIC obligatorio y rol **DNS Zone Contributor** (zonas públicas) en lugar de **Private DNS Zone Contributor** |
| [`Gobernanza/Gobernanza/modules/role_assignment`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Gobernanza/Gobernanza/modules/role_assignment) | La precondición que comprueba `condition_version` llama a `contains()` aunque el valor sea null y **falla con OpenTofu** (comprobado con 1.8, donde el OR lógico no cortocircuita): es decir, en cualquier asignación sin condición ABAC |

Lo que sí reutilizo:

- [`PRO/common/assigned_identity`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/PRO/common/assigned_identity) para la identidad del plano de control. Para la identidad kubelet uso el recurso nativo porque el módulo no devuelve `client_id`, que AKS exige.
- [`Security/Seguridad/modules/monitor_diagnostic_setting`](https://github.com/luisadanmunoz/AzureTerraformModules/tree/main/Security/Seguridad/modules/monitor_diagnostic_setting) para los registros del plano de control.

Notas del provider (azurerm 4.81):

- `os_disk_type` vale `Managed` por defecto en Terraform, aunque AKS elige disco efímero cuando cabe: hay que declararlo.
- `network_profile` y `private_dns_zone_id` fuerzan la recreación del clúster.
- `oidc_issuer_enabled` no se puede desactivar una vez activado.
- Cambiar `host_encryption_enabled`, `os_sku` u otros ajustes del pool de sistema exige `temporary_name_for_rotation`.
- Con escalado automático, el provider recomienda ignorar `node_count`.

### Estructura en el proyecto

```txt
/
├── providers.tf       # azurerm >= 4.81.0
├── aks_clusters.tf    # identidades, permisos, clúster, pools, safeguards, ACR, Container insights, diagnóstico, bloqueo
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
      # Validado con 4.81.0 (azurerm_kubernetes_cluster_deployment_safeguard, maintenance_window_auto_upgrade,
      # maintenance_window_node_os, advanced_networking y os_sku AzureLinux3).
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

### `aks_clusters.tf`

```hcl
# =============================================================================
# AKS Standard con la línea base de seguridad de Microsoft:
# clúster privado con API Server VNet Integration, Azure CNI Overlay con Cilium,
# salida por el firewall (UDR), Entra ID + Azure RBAC sin cuentas locales,
# identidades de usuario (plano de control y kubelet), workload identity, CSI de Key Vault,
# Azure Policy + deployment safeguards, Defender, Image Cleaner, actualizaciones automáticas
# con ventanas de mantenimiento, pool de sistema dedicado y zonal con cifrado en host,
# Container insights (ContainerLogV2), registros del plano de control y bloqueo contra borrado
#
# DEPENDENCY: grupos de recursos creados
# DEPENDENCY: VNet con subred de nodos (no delegada) y, para VNet Integration, subred del API server
#             delegada a Microsoft.ContainerService/managedClusters (mínimo /28, solo para AKS)
# DEPENDENCY: outbound_type = userDefinedRouting: tabla de rutas con 0.0.0.0/0 hacia el firewall
#             ASOCIADA a la subred de nodos antes de crear el clúster, y reglas de salida de AKS en el
#             firewall (FQDN tag AzureKubernetesService)
# DEPENDENCY: zona privada propia (opcional): private.<región>.azmk8s.io con VNet Integration o
#             privatelink.<región>.azmk8s.io sin ella, enlazada a la VNet del hub o al resolver
# DEPENDENCY: grupo de Entra ID para administradores del clúster
# DEPENDENCY: Log Analytics (Container insights, Defender y registros del plano de control)
# DEPENDENCY: host_encryption_enabled exige la característica EncryptionAtHost registrada en la suscripción
# DEPENDENCY: la identidad de Terraform necesita permisos para asignar roles (RBAC Administrator o
#             User Access Administrator) en subredes, VNet, tabla de rutas, zona DNS y ACR,
#             y para crear bloqueos si lock_enabled = true
# =============================================================================

variable "aks_clusters" {
  description = "Clústeres AKS Standard (clave = nombre del clúster)."
  type = map(object({
    resource_group_name = string
    location            = string
    dns_prefix          = optional(string) # por defecto, la clave
    node_resource_group = optional(string) # por defecto, MC_<rg>_<clúster>_<región>

    # Plan y versiones
    sku_tier                  = optional(string, "Standard")           # Free | Standard | Premium
    support_plan              = optional(string, "KubernetesOfficial") # KubernetesOfficial | AKSLongTermSupport (exige Premium)
    kubernetes_version        = optional(string)                       # null con canal automático
    automatic_upgrade_channel = optional(string, "stable")             # patch | rapid | node-image | stable | none
    node_os_upgrade_channel   = optional(string, "NodeImage")          # NodeImage | SecurityPatch | Unmanaged | None

    # Ventanas de mantenimiento: escalonarlas entre clústeres (sin valores por defecto a propósito)
    maintenance_window_auto_upgrade = object({
      frequency    = string           # Weekly | AbsoluteMonthly | RelativeMonthly
      interval     = number           # cada N semanas o meses
      duration     = number           # horas, 4-24
      day_of_week  = optional(string) # Weekly y RelativeMonthly
      week_index   = optional(string) # RelativeMonthly: First | Second | Third | Fourth | Last
      day_of_month = optional(number) # AbsoluteMonthly
      start_time   = string           # "HH:mm"
      utc_offset   = optional(string, "+00:00")
    })
    maintenance_window_node_os = object({
      frequency    = string # Daily | Weekly | AbsoluteMonthly | RelativeMonthly
      interval     = number
      duration     = number
      day_of_week  = optional(string)
      week_index   = optional(string)
      day_of_month = optional(number)
      start_time   = string
      utc_offset   = optional(string, "+00:00")
    })

    # Red
    network = object({
      node_subnet_id          = string
      api_server_subnet_id    = optional(string) # null = sin API Server VNet Integration
      vnet_id                 = optional(string) # obligatorio con zona DNS privada propia (AKS crea el enlace)
      route_table_id          = optional(string) # obligatorio con userDefinedRouting (permiso de la identidad)
      private_cluster_enabled = optional(bool, true)
      private_dns_zone_id     = optional(string, "System") # System | None | ID de zona propia
      authorized_ip_ranges    = optional(list(string), []) # solo en clústeres públicos
      outbound_type           = optional(string, "userDefinedRouting")
      pod_cidr                = string # rango de Overlay: no puede solaparse con la VNet ni con redes conectadas
      service_cidr            = string
      dns_service_ip          = string                # dentro de service_cidr
      acns_observability      = optional(bool, false) # Advanced Container Networking Services (de pago)
      acns_security           = optional(bool, false) # filtrado por FQDN y L7 con Cilium (de pago)
    })

    # Identidad y acceso
    admin_group_object_ids = list(string) # grupos de Entra con Azure Kubernetes Service RBAC Cluster Admin
    local_account_disabled = optional(bool, true)
    run_command_enabled    = optional(bool, true) # comandos sin acceso de red al API server privado (gobernado por RBAC)

    # Pool de sistema (solo complementos críticos)
    system_node_pool = object({
      name                          = optional(string, "system")
      vm_size                       = string # mínimo 4 vCPU y 4 GiB; sin serie B
      zones                         = optional(list(string), ["1", "2", "3"])
      min_count                     = optional(number, 3)
      max_count                     = optional(number, 5)
      max_pods                      = optional(number) # con Overlay, hasta 250
      os_sku                        = optional(string, "AzureLinux3")
      os_disk_type                  = optional(string, "Ephemeral")
      os_disk_size_gb               = optional(number) # con Ephemeral, debe caber en la caché o el temporal de la VM
      host_encryption_enabled       = optional(bool, true)
      temporary_name_for_rotation   = optional(string, "systemtmp")
      max_surge                     = optional(string, "33%")
      drain_timeout_in_minutes      = optional(number, 30)
      node_soak_duration_in_minutes = optional(number, 0)
      node_labels                   = optional(map(string), {})
    })

    # Pools de usuario
    node_pools = optional(map(object({
      vm_size                       = string
      mode                          = optional(string, "User")
      os_type                       = optional(string, "Linux")
      os_sku                        = optional(string) # null = AzureLinux3 en Linux; Windows2022 en Windows
      subnet_id                     = optional(string) # por defecto, la de nodos
      zones                         = optional(list(string), ["1", "2", "3"])
      min_count                     = optional(number, 0)
      max_count                     = number
      max_pods                      = optional(number)
      priority                      = optional(string, "Regular") # Regular | Spot
      os_disk_type                  = optional(string, "Ephemeral")
      os_disk_size_gb               = optional(number)
      host_encryption_enabled       = optional(bool, true)
      temporary_name_for_rotation   = optional(string)
      max_surge                     = optional(string, "33%") # Spot no admite surge
      drain_timeout_in_minutes      = optional(number, 30)
      node_soak_duration_in_minutes = optional(number, 0)
      node_labels                   = optional(map(string), {})
      node_taints                   = optional(list(string), [])
    })), {})

    auto_scaler_profile = optional(object({
      expander                         = optional(string) # least-waste | most-pods | priority | random
      balance_similar_node_groups      = optional(bool)
      scale_down_unneeded              = optional(string)
      scale_down_utilization_threshold = optional(string)
    }))

    # Complementos
    key_vault_secrets_provider_rotation_interval = optional(string, "2m")
    image_cleaner_interval_hours                 = optional(number, 168)
    cost_analysis_enabled                        = optional(bool, true) # Standard o Premium
    keda_enabled                                 = optional(bool, false)
    vertical_pod_autoscaler_enabled              = optional(bool, false)
    defender_enabled                             = optional(bool, true) # Defender for Containers (plan de suscripción aparte)

    deployment_safeguards = optional(object({
      enabled                      = optional(bool, true)
      level                        = optional(string, "Warn")     # Warn | Enforce
      pod_security_standards_level = optional(string, "Baseline") # Privileged | Baseline | Restricted
      excluded_namespaces          = optional(list(string), [])
    }), {})

    # Pull desde ACR con la identidad kubelet
    acr_pull = optional(map(object({
      registry_id = string
      role        = optional(string, "Container Registry Repository Reader") # ABAC; AcrPull en modo legacy
    })), {})

    # Observabilidad
    log_analytics_workspace_id       = string
    log_analytics_workspace_location = string # la DCR de Container insights va en la región del workspace
    container_insights = optional(object({
      streams             = optional(list(string), ["Microsoft-ContainerLogV2", "Microsoft-KubeEvents", "Microsoft-KubePodInventory"])
      interval            = optional(string, "1m")
      namespace_filtering = optional(string, "Off") # Off | Include | Exclude
      namespaces          = optional(list(string), [])
    }), {})
    diagnostic_log_categories = optional(list(string), ["kube-apiserver", "kube-audit-admin", "kube-controller-manager", "cluster-autoscaler", "guard"])

    lock_enabled = optional(bool, true)
    tags         = optional(map(string), {})
  }))
  default = {}

  validation {
    condition     = alltrue([for k, v in var.aks_clusters : can(regex("^[a-zA-Z0-9][a-zA-Z0-9_-]{0,61}[a-zA-Z0-9]$", k))])
    error_message = "Nombre del clúster: 2-63 caracteres, letras, números, guiones y guiones bajos; empieza y acaba en letra o número."
  }

  validation {
    condition = alltrue([
      for k, v in var.aks_clusters :
      contains(["Free", "Standard", "Premium"], v.sku_tier) &&
      contains(["KubernetesOfficial", "AKSLongTermSupport"], v.support_plan) &&
      ((v.sku_tier == "Premium") == (v.support_plan == "AKSLongTermSupport"))
    ])
    error_message = "sku_tier: Free, Standard o Premium; el soporte LTS (AKSLongTermSupport) va siempre con Premium y viceversa."
  }

  validation {
    condition     = alltrue([for k, v in var.aks_clusters : !v.cost_analysis_enabled || v.sku_tier != "Free"])
    error_message = "El complemento de análisis de costes exige Standard o Premium."
  }

  validation {
    condition = alltrue([
      for k, v in var.aks_clusters :
      contains(["patch", "rapid", "node-image", "stable", "none"], v.automatic_upgrade_channel) &&
      contains(["NodeImage", "SecurityPatch", "Unmanaged", "None"], v.node_os_upgrade_channel) &&
      (v.automatic_upgrade_channel != "node-image" || v.node_os_upgrade_channel == "NodeImage")
    ])
    error_message = "automatic_upgrade_channel: patch, rapid, node-image, stable o none; node_os_upgrade_channel: NodeImage, SecurityPatch, Unmanaged o None; el canal node-image obliga a NodeImage."
  }

  validation {
    condition     = alltrue([for k, v in var.aks_clusters : v.automatic_upgrade_channel == "none" || v.kubernetes_version == null])
    error_message = "Con canal de actualización automática, kubernetes_version debe ser null: fijarla hace que Terraform intente devolver el clúster a la versión anterior."
  }

  validation {
    condition = alltrue(flatten([
      for k, v in var.aks_clusters : [
        for w in [v.maintenance_window_auto_upgrade, v.maintenance_window_node_os] :
        w.duration >= 4 && w.duration <= 24 && w.interval >= 1 && can(regex("^([01][0-9]|2[0-3]):[0-5][0-9]$", w.start_time))
      ]
    ]))
    error_message = "Ventanas de mantenimiento: duración de 4 a 24 horas, intervalo >= 1 y start_time en formato HH:mm."
  }

  validation {
    condition = alltrue([
      for k, v in var.aks_clusters :
      contains(["Weekly", "AbsoluteMonthly", "RelativeMonthly"], v.maintenance_window_auto_upgrade.frequency) &&
      contains(["Daily", "Weekly", "AbsoluteMonthly", "RelativeMonthly"], v.maintenance_window_node_os.frequency)
    ])
    error_message = "Frecuencia: Weekly, AbsoluteMonthly o RelativeMonthly para la actualización automática; también Daily para el SO de los nodos."
  }

  validation {
    condition = alltrue([
      for k, v in var.aks_clusters :
      contains(["loadBalancer", "userDefinedRouting", "managedNATGateway", "userAssignedNATGateway"], v.network.outbound_type) &&
      (v.network.outbound_type != "userDefinedRouting" || v.network.route_table_id != null)
    ])
    error_message = "outbound_type: loadBalancer, userDefinedRouting, managedNATGateway o userAssignedNATGateway; userDefinedRouting exige route_table_id (la identidad del clúster necesita permiso sobre la tabla)."
  }

  validation {
    condition = alltrue([
      for k, v in var.aks_clusters :
      contains(["System", "None"], v.network.private_dns_zone_id) || (
        v.network.vnet_id != null &&
        can(regex(v.network.api_server_subnet_id != null
          ? "/privatednszones/([a-z0-9-]+\\.)?private\\.[a-z0-9]+\\.azmk8s\\.io$"
          : "/privatednszones/([a-z0-9-]+\\.)?privatelink\\.[a-z0-9]+\\.azmk8s\\.io$",
        lower(v.network.private_dns_zone_id)))
      )
    ])
    error_message = "private_dns_zone_id: System, None o el ID de una zona private.<región>.azmk8s.io (con VNet Integration) o privatelink.<región>.azmk8s.io (sin ella); una zona propia exige vnet_id."
  }

  validation {
    condition     = alltrue([for k, v in var.aks_clusters : !v.network.private_cluster_enabled || length(v.network.authorized_ip_ranges) == 0])
    error_message = "authorized_ip_ranges solo aplica a clústeres públicos."
  }

  validation {
    condition     = alltrue([for k, v in var.aks_clusters : length(v.admin_group_object_ids) > 0 || !v.local_account_disabled])
    error_message = "Sin cuentas locales hace falta al menos un grupo de administradores de Entra ID; si no, nadie puede entrar al clúster."
  }

  validation {
    condition = alltrue([
      for k, v in var.aks_clusters :
      can(regex("^[a-z][a-z0-9]{0,11}$", v.system_node_pool.name)) &&
      v.system_node_pool.min_count >= 2 && v.system_node_pool.max_count >= v.system_node_pool.min_count &&
      !can(regex("(?i)^standard_b", v.system_node_pool.vm_size)) &&
      contains(["AzureLinux3", "AzureLinux", "Ubuntu", "Ubuntu2204", "Ubuntu2404"], v.system_node_pool.os_sku) &&
      contains(["Ephemeral", "Managed"], v.system_node_pool.os_disk_type)
    ])
    error_message = "Pool de sistema: nombre de 1-12 minúsculas y números empezando por letra, Linux, al menos 2 nodos (3 recomendados), sin serie B y os_disk_type Ephemeral o Managed."
  }

  validation {
    condition = alltrue(flatten([
      for k, v in var.aks_clusters : [
        for pk, p in v.node_pools :
        contains(["User", "System"], p.mode) && contains(["Linux", "Windows"], p.os_type) &&
        contains(["Regular", "Spot"], p.priority) && contains(["Ephemeral", "Managed"], p.os_disk_type) &&
        (p.priority == "Regular" || p.mode == "User") &&
        (p.os_type == "Linux" || p.mode == "User") &&
        can(regex(p.os_type == "Windows" ? "^[a-z][a-z0-9]{0,5}$" : "^[a-z][a-z0-9]{0,11}$", pk)) &&
        p.max_count >= p.min_count && (p.mode == "User" || p.min_count >= 1)
      ]
    ]))
    error_message = "Pools: mode User o System, os_type Linux o Windows, priority Regular o Spot; Spot y Windows solo en modo User; nombre en minúsculas de hasta 12 caracteres (6 en Windows); max_count >= min_count."
  }

  validation {
    condition = alltrue(flatten([
      for k, v in var.aks_clusters : [
        for ak, a in v.acr_pull : contains(["Container Registry Repository Reader", "AcrPull"], a.role)
      ]
    ]))
    error_message = "acr_pull.role: Container Registry Repository Reader (registro en modo ABAC) o AcrPull (modo legacy)."
  }

  validation {
    condition = alltrue([
      for k, v in var.aks_clusters :
      contains(["Warn", "Enforce"], v.deployment_safeguards.level) &&
      contains(["Privileged", "Baseline", "Restricted"], v.deployment_safeguards.pod_security_standards_level) &&
      contains(["Off", "Include", "Exclude"], v.container_insights.namespace_filtering) &&
      !(contains(v.container_insights.streams, "Microsoft-ContainerLogV2") && contains(v.container_insights.streams, "Microsoft-ContainerLogV2-HighScale"))
    ])
    error_message = "deployment_safeguards: Warn o Enforce y Privileged, Baseline o Restricted; namespace_filtering: Off, Include o Exclude; no combinar Microsoft-ContainerLogV2 y Microsoft-ContainerLogV2-HighScale (duplica datos)."
  }
}

# -----------------------------------------------------------------------------
# Identidad del plano de control (módulo PRO/common/assigned_identity del repositorio)
# -----------------------------------------------------------------------------
module "aks_identity" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//PRO/common/assigned_identity?ref=main"
  for_each = var.aks_clusters

  name                = "id-${each.key}"
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  tags                = merge(var.tags, each.value.tags)
}

# Identidad kubelet: recurso nativo porque el módulo no devuelve client_id, que AKS necesita
resource "azurerm_user_assigned_identity" "kubelet" {
  for_each = var.aks_clusters

  name                = "id-${each.key}-kubelet"
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  tags                = merge(var.tags, each.value.tags)
}

# -----------------------------------------------------------------------------
# Permisos de la identidad del plano de control ANTES de crear el clúster
# (recurso nativo: el módulo role_assignment del repositorio falla con condition_version = null)
# -----------------------------------------------------------------------------
resource "azurerm_role_assignment" "aks_control_plane" {
  for_each = merge([
    for k, v in var.aks_clusters : merge(
      { "${k}-node-subnet" = { cluster = k, scope = v.network.node_subnet_id, role = "Network Contributor" } },
      v.network.api_server_subnet_id == null ? {} : { "${k}-apiserver-subnet" = { cluster = k, scope = v.network.api_server_subnet_id, role = "Network Contributor" } },
      v.network.vnet_id == null ? {} : { "${k}-vnet" = { cluster = k, scope = v.network.vnet_id, role = "Network Contributor" } },
      v.network.route_table_id == null ? {} : { "${k}-route-table" = { cluster = k, scope = v.network.route_table_id, role = "Network Contributor" } },
      contains(["System", "None"], v.network.private_dns_zone_id) ? {} : { "${k}-private-dns" = { cluster = k, scope = v.network.private_dns_zone_id, role = "Private DNS Zone Contributor" } },
      { for pk, p in v.node_pools : "${k}-pool-${pk}-subnet" => { cluster = k, scope = p.subnet_id, role = "Network Contributor" } if p.subnet_id != null && p.subnet_id != v.network.node_subnet_id },
      { "${k}-kubelet-identity" = { cluster = k, scope = null, role = "Managed Identity Operator" } }
    )
  ]...)

  # La asignación sobre la identidad kubelet se resuelve aquí porque su ID no se conoce hasta crearla
  scope                            = each.value.scope != null ? each.value.scope : azurerm_user_assigned_identity.kubelet[each.value.cluster].id
  role_definition_name             = each.value.role
  principal_id                     = module.aks_identity[each.value.cluster].principal_id
  principal_type                   = "ServicePrincipal"
  skip_service_principal_aad_check = true # identidad recién creada: evita errores de replicación de Entra ID
  description                      = "AKS ${each.value.cluster}: identidad del plano de control"
}

# -----------------------------------------------------------------------------
# Clúster (recurso nativo: los módulos del repositorio fallan o no exponen la línea base)
# -----------------------------------------------------------------------------
resource "azurerm_kubernetes_cluster" "this" {
  for_each = var.aks_clusters

  name                = each.key
  resource_group_name = each.value.resource_group_name
  location            = each.value.location
  dns_prefix          = coalesce(each.value.dns_prefix, each.key)
  node_resource_group = each.value.node_resource_group

  sku_tier                  = each.value.sku_tier
  support_plan              = each.value.support_plan
  kubernetes_version        = each.value.kubernetes_version
  automatic_upgrade_channel = each.value.automatic_upgrade_channel == "none" ? null : each.value.automatic_upgrade_channel
  node_os_upgrade_channel   = each.value.node_os_upgrade_channel

  # Acceso al API server
  private_cluster_enabled             = each.value.network.private_cluster_enabled
  private_dns_zone_id                 = each.value.network.private_cluster_enabled ? each.value.network.private_dns_zone_id : null
  private_cluster_public_fqdn_enabled = false

  dynamic "api_server_access_profile" {
    for_each = each.value.network.api_server_subnet_id != null || length(each.value.network.authorized_ip_ranges) > 0 ? [1] : []
    content {
      virtual_network_integration_enabled = each.value.network.api_server_subnet_id != null
      subnet_id                           = each.value.network.api_server_subnet_id
      authorized_ip_ranges                = length(each.value.network.authorized_ip_ranges) > 0 ? each.value.network.authorized_ip_ranges : null
    }
  }

  # Identidad: Entra ID + Azure RBAC, sin cuentas locales
  local_account_disabled            = each.value.local_account_disabled
  role_based_access_control_enabled = true
  azure_active_directory_role_based_access_control {
    azure_rbac_enabled     = true
    admin_group_object_ids = each.value.admin_group_object_ids
  }
  run_command_enabled = each.value.run_command_enabled

  identity {
    type         = "UserAssigned"
    identity_ids = [module.aks_identity[each.key].id]
  }

  kubelet_identity {
    client_id                 = azurerm_user_assigned_identity.kubelet[each.key].client_id
    object_id                 = azurerm_user_assigned_identity.kubelet[each.key].principal_id
    user_assigned_identity_id = azurerm_user_assigned_identity.kubelet[each.key].id
  }

  oidc_issuer_enabled       = true # no se puede desactivar una vez activado
  workload_identity_enabled = true

  # Red: Azure CNI Overlay con Cilium (kubenet se retira en 2028 y Azure NPM en 2026-2028)
  network_profile {
    network_plugin      = "azure"
    network_plugin_mode = "overlay"
    network_data_plane  = "cilium"
    network_policy      = "cilium"
    pod_cidr            = each.value.network.pod_cidr
    service_cidr        = each.value.network.service_cidr
    dns_service_ip      = each.value.network.dns_service_ip
    outbound_type       = each.value.network.outbound_type
    load_balancer_sku   = "standard"

    dynamic "advanced_networking" {
      for_each = each.value.network.acns_observability || each.value.network.acns_security ? [1] : []
      content {
        observability_enabled = each.value.network.acns_observability
        security_enabled      = each.value.network.acns_security
      }
    }
  }

  # Pool de sistema: zonal, solo complementos críticos, cifrado en host
  default_node_pool {
    name                         = each.value.system_node_pool.name
    vm_size                      = each.value.system_node_pool.vm_size
    vnet_subnet_id               = each.value.network.node_subnet_id
    zones                        = each.value.system_node_pool.zones
    auto_scaling_enabled         = true
    min_count                    = each.value.system_node_pool.min_count
    max_count                    = each.value.system_node_pool.max_count
    node_count                   = each.value.system_node_pool.min_count
    max_pods                     = each.value.system_node_pool.max_pods
    only_critical_addons_enabled = true
    os_sku                       = each.value.system_node_pool.os_sku
    os_disk_type                 = each.value.system_node_pool.os_disk_type
    os_disk_size_gb              = each.value.system_node_pool.os_disk_size_gb
    host_encryption_enabled      = each.value.system_node_pool.host_encryption_enabled
    node_public_ip_enabled       = false
    temporary_name_for_rotation  = each.value.system_node_pool.temporary_name_for_rotation
    node_labels                  = each.value.system_node_pool.node_labels
    tags                         = merge(var.tags, each.value.tags)

    upgrade_settings {
      max_surge                     = each.value.system_node_pool.max_surge
      drain_timeout_in_minutes      = each.value.system_node_pool.drain_timeout_in_minutes
      node_soak_duration_in_minutes = each.value.system_node_pool.node_soak_duration_in_minutes
    }
  }

  dynamic "auto_scaler_profile" {
    for_each = each.value.auto_scaler_profile == null ? [] : [each.value.auto_scaler_profile]
    content {
      expander                         = auto_scaler_profile.value.expander
      balance_similar_node_groups      = auto_scaler_profile.value.balance_similar_node_groups
      scale_down_unneeded              = auto_scaler_profile.value.scale_down_unneeded
      scale_down_utilization_threshold = auto_scaler_profile.value.scale_down_utilization_threshold
    }
  }

  # Ventanas de mantenimiento (aksManagedAutoUpgradeSchedule y aksManagedNodeOSUpgradeSchedule)
  dynamic "maintenance_window_auto_upgrade" {
    for_each = each.value.automatic_upgrade_channel == "none" ? [] : [each.value.maintenance_window_auto_upgrade]
    content {
      frequency    = maintenance_window_auto_upgrade.value.frequency
      interval     = maintenance_window_auto_upgrade.value.interval
      duration     = maintenance_window_auto_upgrade.value.duration
      day_of_week  = maintenance_window_auto_upgrade.value.day_of_week
      week_index   = maintenance_window_auto_upgrade.value.week_index
      day_of_month = maintenance_window_auto_upgrade.value.day_of_month
      start_time   = maintenance_window_auto_upgrade.value.start_time
      utc_offset   = maintenance_window_auto_upgrade.value.utc_offset
    }
  }

  dynamic "maintenance_window_node_os" {
    for_each = contains(["NodeImage", "SecurityPatch"], each.value.node_os_upgrade_channel) ? [each.value.maintenance_window_node_os] : []
    content {
      frequency    = maintenance_window_node_os.value.frequency
      interval     = maintenance_window_node_os.value.interval
      duration     = maintenance_window_node_os.value.duration
      day_of_week  = maintenance_window_node_os.value.day_of_week
      week_index   = maintenance_window_node_os.value.week_index
      day_of_month = maintenance_window_node_os.value.day_of_month
      start_time   = maintenance_window_node_os.value.start_time
      utc_offset   = maintenance_window_node_os.value.utc_offset
    }
  }

  # Complementos de seguridad y operación
  azure_policy_enabled         = true # requisito de deployment safeguards
  image_cleaner_enabled        = true
  image_cleaner_interval_hours = each.value.image_cleaner_interval_hours
  cost_analysis_enabled        = each.value.cost_analysis_enabled

  key_vault_secrets_provider {
    secret_rotation_enabled  = true
    secret_rotation_interval = each.value.key_vault_secrets_provider_rotation_interval
  }

  dynamic "microsoft_defender" {
    for_each = each.value.defender_enabled ? [1] : []
    content {
      log_analytics_workspace_id = each.value.log_analytics_workspace_id
    }
  }

  dynamic "workload_autoscaler_profile" {
    for_each = each.value.keda_enabled || each.value.vertical_pod_autoscaler_enabled ? [1] : []
    content {
      keda_enabled                    = each.value.keda_enabled
      vertical_pod_autoscaler_enabled = each.value.vertical_pod_autoscaler_enabled
    }
  }

  # Container insights con identidad administrada (la DCR se crea abajo)
  oms_agent {
    log_analytics_workspace_id      = each.value.log_analytics_workspace_id
    msi_auth_for_monitoring_enabled = true
  }

  tags = merge(var.tags, each.value.tags)

  lifecycle {
    # El escalador automático cambia el número de nodos
    ignore_changes = [default_node_pool[0].node_count]
  }

  depends_on = [azurerm_role_assignment.aks_control_plane]
}

# -----------------------------------------------------------------------------
# Pools de usuario (recurso nativo: el submódulo no expone host_encryption_enabled ni eviction_policy)
# -----------------------------------------------------------------------------
resource "azurerm_kubernetes_cluster_node_pool" "this" {
  for_each = merge([
    for k, v in var.aks_clusters : {
      for pk, p in v.node_pools : "${k}-${pk}" => merge(p, { cluster = k, pool = pk })
    }
  ]...)

  name                  = each.value.pool
  kubernetes_cluster_id = azurerm_kubernetes_cluster.this[each.value.cluster].id
  vm_size               = each.value.vm_size
  mode                  = each.value.mode
  os_type               = each.value.os_type
  os_sku                = coalesce(each.value.os_sku, each.value.os_type == "Windows" ? "Windows2022" : "AzureLinux3")
  vnet_subnet_id        = coalesce(each.value.subnet_id, var.aks_clusters[each.value.cluster].network.node_subnet_id)
  zones                 = each.value.zones

  auto_scaling_enabled = true
  min_count            = each.value.min_count
  max_count            = each.value.max_count
  node_count           = each.value.min_count
  max_pods             = each.value.max_pods

  os_disk_type                = each.value.os_disk_type
  os_disk_size_gb             = each.value.os_disk_size_gb
  host_encryption_enabled     = each.value.host_encryption_enabled
  node_public_ip_enabled      = false
  temporary_name_for_rotation = each.value.temporary_name_for_rotation

  # Spot: AKS añade la etiqueta y el taint; se declaran para que el plan no muestre diferencias
  priority        = each.value.priority
  eviction_policy = each.value.priority == "Spot" ? "Delete" : null
  spot_max_price  = each.value.priority == "Spot" ? -1 : null
  node_labels     = merge(each.value.node_labels, each.value.priority == "Spot" ? { "kubernetes.azure.com/scalesetpriority" = "spot" } : {})
  node_taints     = distinct(concat(each.value.node_taints, each.value.priority == "Spot" ? ["kubernetes.azure.com/scalesetpriority=spot:NoSchedule"] : []))

  # Los pools Spot no tienen nodos de surge
  dynamic "upgrade_settings" {
    for_each = each.value.priority == "Regular" ? [1] : []
    content {
      max_surge                     = each.value.max_surge
      drain_timeout_in_minutes      = each.value.drain_timeout_in_minutes
      node_soak_duration_in_minutes = each.value.node_soak_duration_in_minutes
    }
  }

  tags = merge(var.tags, var.aks_clusters[each.value.cluster].tags)

  lifecycle {
    ignore_changes = [node_count]
  }
}

# -----------------------------------------------------------------------------
# Deployment safeguards (Azure Policy) y Pod Security Standards
# -----------------------------------------------------------------------------
resource "azurerm_kubernetes_cluster_deployment_safeguard" "this" {
  for_each = { for k, v in var.aks_clusters : k => v.deployment_safeguards if v.deployment_safeguards.enabled }

  kubernetes_cluster_id        = azurerm_kubernetes_cluster.this[each.key].id
  level                        = each.value.level
  pod_security_standards_level = each.value.pod_security_standards_level
  excluded_namespaces          = each.value.excluded_namespaces
}

# -----------------------------------------------------------------------------
# Pull de imágenes desde ACR con la identidad kubelet
# -----------------------------------------------------------------------------
resource "azurerm_role_assignment" "aks_acr_pull" {
  for_each = merge([
    for k, v in var.aks_clusters : {
      for ak, a in v.acr_pull : "${k}-${ak}" => merge(a, { cluster = k })
    }
  ]...)

  scope                            = each.value.registry_id
  role_definition_name             = each.value.role
  principal_id                     = azurerm_user_assigned_identity.kubelet[each.value.cluster].principal_id
  principal_type                   = "ServicePrincipal"
  skip_service_principal_aad_check = true
  description                      = "AKS ${each.value.cluster}: pull con la identidad kubelet"
}

# -----------------------------------------------------------------------------
# Container insights: DCR y asociación (necesarias con autenticación por identidad administrada)
# -----------------------------------------------------------------------------
resource "azurerm_monitor_data_collection_rule" "container_insights" {
  for_each = var.aks_clusters

  name                = "MSCI-${each.key}-${each.value.location}"
  resource_group_name = each.value.resource_group_name
  location            = each.value.log_analytics_workspace_location
  kind                = "Linux"

  destinations {
    log_analytics {
      workspace_resource_id = each.value.log_analytics_workspace_id
      name                  = "ciworkspace"
    }
  }

  data_flow {
    streams      = each.value.container_insights.streams
    destinations = ["ciworkspace"]
  }

  data_sources {
    extension {
      name           = "ContainerInsightsExtension"
      extension_name = "ContainerInsights"
      streams        = each.value.container_insights.streams
      extension_json = jsonencode({
        dataCollectionSettings = {
          interval               = each.value.container_insights.interval
          namespaceFilteringMode = each.value.container_insights.namespace_filtering
          namespaces             = each.value.container_insights.namespaces
          enableContainerLogV2   = true
        }
      })
    }
  }

  tags = merge(var.tags, each.value.tags)
}

resource "azurerm_monitor_data_collection_rule_association" "container_insights" {
  for_each = var.aks_clusters

  name                    = "ContainerInsightsExtension"
  target_resource_id      = azurerm_kubernetes_cluster.this[each.key].id
  data_collection_rule_id = azurerm_monitor_data_collection_rule.container_insights[each.key].id
  description             = "Container insights del clúster ${each.key}"
}

# -----------------------------------------------------------------------------
# Registros del plano de control (módulo Security/Seguridad/modules/monitor_diagnostic_setting)
# kube-audit completo es muy caro: kube-audit-admin excluye get y list
# -----------------------------------------------------------------------------
module "aks_diagnostics" {
  source   = "git::https://github.com/luisadanmunoz/AzureTerraformModules.git//Security/Seguridad/modules/monitor_diagnostic_setting?ref=main"
  for_each = { for k, v in var.aks_clusters : k => v if length(v.diagnostic_log_categories) > 0 }

  monitor_diagnostic_setting_name = "diag-${each.key}"
  target_resource_id              = azurerm_kubernetes_cluster.this[each.key].id
  log_analytics_workspace_id      = each.value.log_analytics_workspace_id
  log_analytics_destination_type  = "Dedicated" # tablas AKSAudit, AKSAuditAdmin y AKSControlPlane
  enabled_logs                    = [for c in each.value.diagnostic_log_categories : { category = c }]
}

# -----------------------------------------------------------------------------
# Bloqueo contra borrado del clúster
# -----------------------------------------------------------------------------
resource "azurerm_management_lock" "aks" {
  for_each = { for k, v in var.aks_clusters : k => v if v.lock_enabled }

  name       = "lock-${each.key}"
  scope      = azurerm_kubernetes_cluster.this[each.key].id
  lock_level = "CanNotDelete"
  notes      = "Protege el clúster contra el borrado accidental."
}

# -----------------------------------------------------------------------------
# Salidas
# -----------------------------------------------------------------------------
output "aks_cluster_ids" {
  description = "ID de cada clúster."
  value       = { for k, v in azurerm_kubernetes_cluster.this : k => v.id }
}

output "aks_private_fqdns" {
  description = "FQDN privado del API server de cada clúster."
  value       = { for k, v in azurerm_kubernetes_cluster.this : k => v.private_fqdn }
}

output "aks_oidc_issuer_urls" {
  description = "Emisor OIDC de cada clúster (credenciales federadas de workload identity)."
  value       = { for k, v in azurerm_kubernetes_cluster.this : k => v.oidc_issuer_url }
}

output "aks_node_resource_groups" {
  description = "Grupo de recursos de nodos de cada clúster."
  value       = { for k, v in azurerm_kubernetes_cluster.this : k => v.node_resource_group }
}

output "aks_control_plane_identities" {
  description = "Identidad del plano de control de cada clúster."
  value       = { for k, v in module.aks_identity : k => { id = v.id, principal_id = v.principal_id } }
}

output "aks_kubelet_identities" {
  description = "Identidad kubelet de cada clúster (permisos sobre ACR)."
  value       = { for k, v in azurerm_user_assigned_identity.kubelet : k => { id = v.id, client_id = v.client_id, principal_id = v.principal_id } }
}

output "aks_key_vault_secrets_provider_identities" {
  description = "Identidad del complemento de CSI de Key Vault (permisos de lectura de secretos)."
  value       = { for k, v in azurerm_kubernetes_cluster.this : k => try(v.key_vault_secrets_provider[0].secret_identity[0].object_id, null) }
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

aks_clusters = {
  "aks-workload-pro-01" = {
    resource_group_name = "<rg-aks-workload-pro>"
    location            = "<region>"
    node_resource_group = "<rg-aks-workload-pro-nodes>"

    # Standard: SLA del API server y hasta 5000 nodos
    sku_tier                  = "Standard"
    automatic_upgrade_channel = "stable"    # versión N-1 más reciente
    node_os_upgrade_channel   = "NodeImage" # imagen semanal con parches y correcciones

    # Escalonar las ventanas entre clústeres y entornos (pro después de pre)
    maintenance_window_auto_upgrade = {
      frequency   = "RelativeMonthly"
      interval    = 1
      week_index  = "Second"
      day_of_week = "Tuesday"
      start_time  = "<HH:mm>"
      utc_offset  = "<+01:00>"
      duration    = 6
    }
    maintenance_window_node_os = {
      frequency   = "Weekly"
      interval    = 1
      day_of_week = "Sunday"
      start_time  = "<HH:mm>"
      utc_offset  = "<+01:00>"
      duration    = 4
    }

    network = {
      node_subnet_id       = "<resourceId snet-aks-nodes-pro>"
      api_server_subnet_id = "<resourceId snet-aks-apiserver-pro (/28, delegada)>"
      vnet_id              = "<resourceId vnet-spoke-aks-pro>"
      route_table_id       = "<resourceId rt-aks-pro (0.0.0.0/0 -> firewall)>"

      # Zona propia en el hub para resolver desde redes conectadas (formato de VNet Integration)
      private_cluster_enabled = true
      private_dns_zone_id     = "<resourceId private.<region>.azmk8s.io>"
      outbound_type           = "userDefinedRouting"

      # Rangos sin solape con la VNet, el hub, on-premises ni los rangos reservados de AKS
      pod_cidr       = "<cidr-pods>"
      service_cidr   = "<cidr-servicios>"
      dns_service_ip = "<ip-dentro-de-service_cidr>"
    }

    admin_group_object_ids = ["<objectId grupo aks-admins-pro>"]

    system_node_pool = {
      vm_size         = "<Standard_D4ds_v5>" # 4 vCPU; temporal suficiente para disco efímero de 128 GiB
      os_disk_size_gb = 128
      min_count       = 3
      max_count       = 5
    }

    node_pools = {
      apps = {
        vm_size         = "<Standard_D8ds_v5>"
        os_disk_size_gb = 128
        min_count       = 3
        max_count       = 12
        node_labels     = { "workload" = "apps" }
      }
      batch = {
        vm_size     = "<Standard_D8ds_v5>"
        priority    = "Spot" # trabajos interrumpibles
        min_count   = 0
        max_count   = 10
        node_labels = { "workload" = "batch" }
      }
    }

    deployment_safeguards = {
      level                        = "Warn" # pasar a Enforce cuando los manifiestos cumplan
      pod_security_standards_level = "Baseline"
    }

    acr_pull = {
      platform = {
        registry_id = "<resourceId crworkloadpro01>"
        role        = "Container Registry Repository Reader" # registro en modo ABAC
      }
    }

    log_analytics_workspace_id       = "<resourceId log-platform-pro>"
    log_analytics_workspace_location = "<region>"

    tags = {
      dataclassification = "internal"
    }
  }
}
```

### Despliegue y comprobación

```powershell
terraform init
terraform plan -var-file="env/pro.tfvars" -out="pro.tfplan"
terraform apply "pro.tfplan"

# Configuración del clúster (propiedades de la API)
$aks = Get-AzResource -ResourceGroupName "<rg-aks-workload-pro>" -ResourceType "Microsoft.ContainerService/managedClusters" -Name "aks-workload-pro-01" -ExpandProperties
[PSCustomObject]@{
    Tier                = $aks.Sku.tier
    LocalAccounts       = -not $aks.Properties.disableLocalAccounts
    AzureRbac           = $aks.Properties.aadProfile.enableAzureRBAC
    PrivateCluster      = $aks.Properties.apiServerAccessProfile.enablePrivateCluster
    VnetIntegration     = $aks.Properties.apiServerAccessProfile.enableVnetIntegration
    NetworkDataplane    = $aks.Properties.networkProfile.networkDataplane
    OutboundType        = $aks.Properties.networkProfile.outboundType
    UpgradeChannel      = $aks.Properties.autoUpgradeProfile.upgradeChannel
    NodeOsChannel       = $aks.Properties.autoUpgradeProfile.nodeOSUpgradeChannel
}

# Acceso con Entra ID desde una máquina con visibilidad del API server privado
az aks get-credentials --resource-group "<rg-aks-workload-pro>" --name "aks-workload-pro-01"
kubelogin convert-kubeconfig -l azurecli
kubectl get nodes -o wide

# Sin visibilidad de red: comando a través de ARM (run_command_enabled = true)
az aks command invoke --resource-group "<rg-aks-workload-pro>" --name "aks-workload-pro-01" --command "kubectl get pods -n kube-system"

# Ventanas de mantenimiento y versiones de imagen de nodo
az aks maintenanceconfiguration list --resource-group "<rg-aks-workload-pro>" --cluster-name "aks-workload-pro-01" -o table
az aks nodepool get-upgrades --resource-group "<rg-aks-workload-pro>" --cluster-name "aks-workload-pro-01" --nodepool-name "apps"
```

Auditoría en Log Analytics (tablas dedicadas):

```kusto
// Cambios en el clúster por usuario (sin get ni list)
AKSAuditAdmin
| where ResponseStatus.code != 401
| summarize Count = count() by Username = tostring(User.username), ResourceId = _ResourceId
| sort by Count desc

// Cambios en deployments de un namespace
AKSAuditAdmin
| where ObjectRef.resource == "deployments" and ObjectRef.namespace == "<namespace>"
| project TimeGenerated, Verb, RequestUri, User, ObjectRef
```

### Equivalente en Bicep

Un clúster por despliegue. `aks.bicep` usa un módulo auxiliar, `role-on-resource.bicep`, para asignar roles sobre recursos de otros grupos de recursos (subredes, VNet, tabla de rutas, zona DNS y registro), porque una asignación de rol solo puede apuntar a recursos del grupo que se despliega. Todos los pools van en `agentPoolProfiles`; el pool de sistema lleva el taint `CriticalAddonsOnly=true:NoSchedule`, que es lo que hace `only_critical_addons_enabled` en Terraform.

`aks.bicep`:

```bicep
// =============================================================================
// AKS Standard con la línea base de seguridad: privado con API Server VNet Integration,
// CNI Overlay + Cilium, salida por UDR, Entra ID + Azure RBAC sin cuentas locales,
// identidades de usuario, workload identity, CSI de Key Vault, Azure Policy + safeguards,
// Defender, Image Cleaner, actualizaciones automáticas con ventanas, Container insights,
// registros del plano de control y bloqueo
// DEPENDENCY: subred de nodos, subred del API server delegada (/28) y tabla de rutas asociada
// DEPENDENCY: zona private.<región>.azmk8s.io (si es propia), grupo de administradores de Entra ID
// DEPENDENCY: Log Analytics; característica EncryptionAtHost registrada
// DEPENDENCY: role-on-resource.bicep en la misma carpeta
// =============================================================================
@minLength(2)
@maxLength(63)
param name string
param location string = resourceGroup().location
param dnsPrefix string = name
param nodeResourceGroup string = ''

@allowed(['Free', 'Standard', 'Premium'])
param skuTier string = 'Standard'

@description('Premium exige AKSLongTermSupport y viceversa.')
@allowed(['KubernetesOfficial', 'AKSLongTermSupport'])
param supportPlan string = 'KubernetesOfficial'

@description('Vacío con canal automático.')
param kubernetesVersion string = ''

@allowed(['patch', 'rapid', 'node-image', 'stable', 'none'])
param upgradeChannel string = 'stable'

@allowed(['NodeImage', 'SecurityPatch', 'Unmanaged', 'None'])
param nodeOsUpgradeChannel string = 'NodeImage'

@description('Ventana de aksManagedAutoUpgradeSchedule: { schedule, durationHours, startTime, utcOffset }')
param autoUpgradeWindow object

@description('Ventana de aksManagedNodeOSUpgradeSchedule: { schedule, durationHours, startTime, utcOffset }')
param nodeOsUpgradeWindow object

// Red
param nodeSubnetId string

@description('Subred delegada a Microsoft.ContainerService/managedClusters (/28). Vacío = sin VNet Integration.')
param apiServerSubnetId string = ''

@description('Con zona DNS propia: la identidad necesita Network Contributor en la VNet.')
param vnetId string = ''

param routeTableId string = ''
param privateClusterEnabled bool = true

@description('System, None o el ID de una zona private.<región>.azmk8s.io (con VNet Integration).')
param privateDnsZoneId string = 'System'

param authorizedIpRanges array = []

@allowed(['loadBalancer', 'userDefinedRouting', 'managedNATGateway', 'userAssignedNATGateway'])
param outboundType string = 'userDefinedRouting'

param podCidr string
param serviceCidr string
param dnsServiceIp string
param acnsObservability bool = false
param acnsSecurity bool = false

// Identidad y acceso
@minLength(1)
param adminGroupObjectIds array
param runCommandEnabled bool = true

@description('{ name?, vmSize, zones?, minCount?, maxCount?, osDiskSizeGB?, maxPods?, maxSurge? }')
param systemPool object

@description('[{ name, vmSize, minCount?, maxCount, priority?, mode?, osType?, osSku?, subnetId?, zones?, osDiskSizeGB?, maxPods?, nodeLabels?, nodeTaints?, maxSurge? }]')
param nodePools array = []

// Complementos
param imageCleanerIntervalHours int = 168
param costAnalysisEnabled bool = true
param kedaEnabled bool = false
param vpaEnabled bool = false
param defenderEnabled bool = true

@allowed(['Warn', 'Enforce'])
param safeguardsLevel string = 'Warn'

@allowed(['Privileged', 'Baseline', 'Restricted'])
param podSecurityStandardsLevel string = 'Baseline'

param safeguardsExcludedNamespaces array = []

@description('[{ registryId, role? }]; role = Container Registry Repository Reader (ABAC) o AcrPull')
param acrPull array = []

// Observabilidad
param logAnalyticsWorkspaceId string
param logAnalyticsWorkspaceLocation string = location
param containerInsightsStreams array = ['Microsoft-ContainerLogV2', 'Microsoft-KubeEvents', 'Microsoft-KubePodInventory']
param diagnosticLogCategories array = ['kube-apiserver', 'kube-audit-admin', 'kube-controller-manager', 'cluster-autoscaler', 'guard']

param lockEnabled bool = true
param tags object = {}

var roleIds = {
  'Network Contributor': '4d97b98b-1d4f-4787-a291-c67834d212e7'
  'Private DNS Zone Contributor': 'b12aa53e-6015-4669-85d0-8515ebb3ae7f'
  'Managed Identity Operator': 'f1a07417-d97a-45cb-824c-7a7467783830'
  AcrPull: '7f951dda-4ed3-4680-a7ca-43fe172d538d'
  'Container Registry Repository Reader': 'b93aa761-3e63-49ed-ac28-beffa264f7ac'
}

var customDnsZone = !contains(['System', 'None'], privateDnsZoneId)
var poolSubnets = filter(map(nodePools, p => p.?subnetId ?? ''), s => !empty(s) && s != nodeSubnetId)

// Destinos de Network Contributor y Private DNS Zone Contributor para la identidad del plano de control
var networkScopes = union(
  [nodeSubnetId],
  empty(apiServerSubnetId) ? [] : [apiServerSubnetId],
  empty(vnetId) ? [] : [vnetId],
  empty(routeTableId) ? [] : [routeTableId],
  poolSubnets
)

var spotLabel = { 'kubernetes.azure.com/scalesetpriority': 'spot' }
var spotTaint = 'kubernetes.azure.com/scalesetpriority=spot:NoSchedule'

var systemProfile = {
  name: systemPool.?name ?? 'system'
  mode: 'System'
  osType: 'Linux'
  osSKU: 'AzureLinux3'
  vmSize: systemPool.vmSize
  vnetSubnetID: nodeSubnetId
  availabilityZones: systemPool.?zones ?? ['1', '2', '3']
  enableAutoScaling: true
  count: systemPool.?minCount ?? 3
  minCount: systemPool.?minCount ?? 3
  maxCount: systemPool.?maxCount ?? 5
  maxPods: systemPool.?maxPods
  osDiskType: 'Ephemeral'
  osDiskSizeGB: systemPool.?osDiskSizeGB
  enableEncryptionAtHost: true
  enableNodePublicIP: false
  nodeTaints: ['CriticalAddonsOnly=true:NoSchedule']
  upgradeSettings: {
    maxSurge: systemPool.?maxSurge ?? '33%'
    drainTimeoutInMinutes: 30
  }
  tags: tags
}

var userProfiles = [
  for p in nodePools: {
    name: p.name
    mode: p.?mode ?? 'User'
    osType: p.?osType ?? 'Linux'
    osSKU: p.?osSku ?? ((p.?osType ?? 'Linux') == 'Windows' ? 'Windows2022' : 'AzureLinux3')
    vmSize: p.vmSize
    vnetSubnetID: p.?subnetId ?? nodeSubnetId
    availabilityZones: p.?zones ?? ['1', '2', '3']
    enableAutoScaling: true
    count: p.?minCount ?? 0
    minCount: p.?minCount ?? 0
    maxCount: p.maxCount
    maxPods: p.?maxPods
    osDiskType: p.?osDiskType ?? 'Ephemeral'
    osDiskSizeGB: p.?osDiskSizeGB
    enableEncryptionAtHost: true
    enableNodePublicIP: false
    scaleSetPriority: p.?priority ?? 'Regular'
    scaleSetEvictionPolicy: (p.?priority ?? 'Regular') == 'Spot' ? 'Delete' : null
    spotMaxPrice: (p.?priority ?? 'Regular') == 'Spot' ? json('-1') : null
    nodeLabels: union(p.?nodeLabels ?? {}, (p.?priority ?? 'Regular') == 'Spot' ? spotLabel : {})
    nodeTaints: union(p.?nodeTaints ?? [], (p.?priority ?? 'Regular') == 'Spot' ? [spotTaint] : [])
    upgradeSettings: (p.?priority ?? 'Regular') == 'Spot'
      ? null
      : {
          maxSurge: p.?maxSurge ?? '33%'
          drainTimeoutInMinutes: 30
        }
    tags: tags
  }
]

resource controlPlaneIdentity 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = {
  name: 'id-${name}'
  location: location
  tags: tags
}

resource kubeletIdentity 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = {
  name: 'id-${name}-kubelet'
  location: location
  tags: tags
}

// Permisos previos a la creación del clúster
module networkRoles 'role-on-resource.bicep' = [
  for (scopeId, i) in networkScopes: {
    name: '${take(name, 50)}-net-${i}'
    scope: resourceGroup(split(scopeId, '/')[2], split(scopeId, '/')[4])
    params: {
      resourceId: scopeId
      roleDefinitionId: roleIds['Network Contributor']
      principalId: controlPlaneIdentity.properties.principalId
      description: 'AKS ${name}: identidad del plano de control'
    }
  }
]

module dnsRole 'role-on-resource.bicep' = if (privateClusterEnabled && customDnsZone) {
  name: '${take(name, 50)}-dns'
  scope: resourceGroup(split(privateDnsZoneId, '/')[2], split(privateDnsZoneId, '/')[4])
  params: {
    resourceId: privateDnsZoneId
    roleDefinitionId: roleIds['Private DNS Zone Contributor']
    principalId: controlPlaneIdentity.properties.principalId
    description: 'AKS ${name}: registros del API server'
  }
}

resource kubeletOperator 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(kubeletIdentity.id, controlPlaneIdentity.id, 'Managed Identity Operator')
  scope: kubeletIdentity
  properties: {
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', roleIds['Managed Identity Operator'])
    principalId: controlPlaneIdentity.properties.principalId
    principalType: 'ServicePrincipal'
  }
}

resource aks 'Microsoft.ContainerService/managedClusters@2025-10-01' = {
  name: name
  location: location
  tags: tags
  sku: {
    name: 'Base'
    tier: skuTier
  }
  identity: {
    type: 'UserAssigned'
    userAssignedIdentities: {
      '${controlPlaneIdentity.id}': {}
    }
  }
  properties: {
    dnsPrefix: dnsPrefix
    kubernetesVersion: empty(kubernetesVersion) ? null : kubernetesVersion
    nodeResourceGroup: empty(nodeResourceGroup) ? null : nodeResourceGroup
    supportPlan: supportPlan
    enableRBAC: true
    disableLocalAccounts: true
    aadProfile: {
      managed: true
      enableAzureRBAC: true
      adminGroupObjectIDs: adminGroupObjectIds
      tenantID: tenant().tenantId
    }
    apiServerAccessProfile: {
      enablePrivateCluster: privateClusterEnabled
      privateDNSZone: privateClusterEnabled ? privateDnsZoneId : null
      enablePrivateClusterPublicFQDN: false
      enableVnetIntegration: !empty(apiServerSubnetId)
      subnetId: empty(apiServerSubnetId) ? null : apiServerSubnetId
      authorizedIPRanges: privateClusterEnabled ? null : authorizedIpRanges
      disableRunCommand: !runCommandEnabled
    }
    networkProfile: {
      networkPlugin: 'azure'
      networkPluginMode: 'overlay'
      networkDataplane: 'cilium'
      networkPolicy: 'cilium'
      podCidr: podCidr
      serviceCidr: serviceCidr
      dnsServiceIP: dnsServiceIp
      outboundType: outboundType
      loadBalancerSku: 'standard'
      advancedNetworking: acnsObservability || acnsSecurity
        ? {
            enabled: true
            observability: {
              enabled: acnsObservability
            }
            security: {
              enabled: acnsSecurity
            }
          }
        : null
    }
    agentPoolProfiles: concat([systemProfile], userProfiles)
    identityProfile: {
      kubeletidentity: {
        resourceId: kubeletIdentity.id
        clientId: kubeletIdentity.properties.clientId
        objectId: kubeletIdentity.properties.principalId
      }
    }
    oidcIssuerProfile: {
      enabled: true
    }
    securityProfile: {
      workloadIdentity: {
        enabled: true
      }
      imageCleaner: {
        enabled: true
        intervalHours: imageCleanerIntervalHours
      }
      defender: defenderEnabled
        ? {
            logAnalyticsWorkspaceResourceId: logAnalyticsWorkspaceId
            securityMonitoring: {
              enabled: true
            }
          }
        : null
    }
    addonProfiles: {
      azurepolicy: {
        enabled: true
      }
      azureKeyvaultSecretsProvider: {
        enabled: true
        config: {
          enableSecretRotation: 'true'
          rotationPollInterval: '2m'
        }
      }
      omsagent: {
        enabled: true
        config: {
          logAnalyticsWorkspaceResourceID: logAnalyticsWorkspaceId
          useAADAuth: 'true'
        }
      }
    }
    autoUpgradeProfile: {
      upgradeChannel: upgradeChannel
      nodeOSUpgradeChannel: nodeOsUpgradeChannel
    }
    metricsProfile: {
      costAnalysis: {
        enabled: costAnalysisEnabled && skuTier != 'Free'
      }
    }
    workloadAutoScalerProfile: {
      keda: {
        enabled: kedaEnabled
      }
      verticalPodAutoscaler: {
        enabled: vpaEnabled
      }
    }
  }
  dependsOn: [
    networkRoles
    dnsRole
    kubeletOperator
  ]
}

resource autoUpgradeSchedule 'Microsoft.ContainerService/managedClusters/maintenanceConfigurations@2025-10-01' = if (upgradeChannel != 'none') {
  parent: aks
  name: 'aksManagedAutoUpgradeSchedule'
  properties: {
    maintenanceWindow: autoUpgradeWindow
  }
}

resource nodeOsSchedule 'Microsoft.ContainerService/managedClusters/maintenanceConfigurations@2025-10-01' = if (contains(['NodeImage', 'SecurityPatch'], nodeOsUpgradeChannel)) {
  parent: aks
  name: 'aksManagedNodeOSUpgradeSchedule'
  properties: {
    maintenanceWindow: nodeOsUpgradeWindow
  }
}

resource safeguards 'Microsoft.ContainerService/deploymentSafeguards@2025-07-01' = {
  name: 'default'
  scope: aks
  properties: {
    level: safeguardsLevel
    podSecurityStandardsLevel: podSecurityStandardsLevel
    excludedNamespaces: safeguardsExcludedNamespaces
  }
}

module acrRoles 'role-on-resource.bicep' = [
  for (a, i) in acrPull: {
    name: '${take(name, 50)}-acr-${i}'
    scope: resourceGroup(split(a.registryId, '/')[2], split(a.registryId, '/')[4])
    params: {
      resourceId: a.registryId
      roleDefinitionId: roleIds[a.?role ?? 'Container Registry Repository Reader']
      principalId: kubeletIdentity.properties.principalId
      description: 'AKS ${name}: pull con la identidad kubelet'
    }
  }
]

resource containerInsightsDcr 'Microsoft.Insights/dataCollectionRules@2023-03-11' = {
  name: 'MSCI-${name}-${location}'
  location: logAnalyticsWorkspaceLocation
  kind: 'Linux'
  tags: tags
  properties: {
    dataSources: {
      extensions: [
        {
          name: 'ContainerInsightsExtension'
          extensionName: 'ContainerInsights'
          streams: containerInsightsStreams
          extensionSettings: {
            dataCollectionSettings: {
              interval: '1m'
              namespaceFilteringMode: 'Off'
              enableContainerLogV2: true
            }
          }
        }
      ]
    }
    destinations: {
      logAnalytics: [
        {
          name: 'ciworkspace'
          workspaceResourceId: logAnalyticsWorkspaceId
        }
      ]
    }
    dataFlows: [
      {
        streams: containerInsightsStreams
        destinations: [
          'ciworkspace'
        ]
      }
    ]
  }
}

resource containerInsightsDcra 'Microsoft.Insights/dataCollectionRuleAssociations@2023-03-11' = {
  name: 'ContainerInsightsExtension'
  scope: aks
  properties: {
    dataCollectionRuleId: containerInsightsDcr.id
    description: 'Container insights del clúster ${name}'
  }
}

resource diagnostics 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = if (!empty(diagnosticLogCategories)) {
  name: 'diag-${name}'
  scope: aks
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

resource lock 'Microsoft.Authorization/locks@2020-05-01' = if (lockEnabled) {
  name: 'lock-${name}'
  scope: aks
  properties: {
    level: 'CanNotDelete'
    notes: 'Protege el clúster contra el borrado accidental.'
  }
}

output id string = aks.id
output privateFqdn string = aks.properties.?privateFQDN ?? ''
output oidcIssuerUrl string = aks.properties.oidcIssuerProfile.issuerURL
output kubeletIdentityClientId string = kubeletIdentity.properties.clientId
output keyVaultSecretsProviderObjectId string = aks.properties.addonProfiles.azureKeyvaultSecretsProvider.identity.objectId
```

`role-on-resource.bicep`:

```bicep
// =============================================================================
// Asigna un rol sobre un recurso de otro grupo de recursos (subred, VNet, tabla de rutas,
// zona DNS privada o registro). Se despliega con scope en el grupo de recursos del destino.
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
```

`aks-workload-pro-01.bicepparam`:

```bicep
using 'aks.bicep'

param name = 'aks-workload-pro-01'
param nodeResourceGroup = '<rg-aks-workload-pro-nodes>'
param skuTier = 'Standard'
param upgradeChannel = 'stable'
param nodeOsUpgradeChannel = 'NodeImage'

// Escalonar entre clústeres y entornos
param autoUpgradeWindow = {
  schedule: {
    relativeMonthly: {
      intervalMonths: 1
      weekIndex: 'Second'
      dayOfWeek: 'Tuesday'
    }
  }
  durationHours: 6
  startTime: '<HH:mm>'
  utcOffset: '<+01:00>'
}
param nodeOsUpgradeWindow = {
  schedule: {
    weekly: {
      intervalWeeks: 1
      dayOfWeek: 'Sunday'
    }
  }
  durationHours: 4
  startTime: '<HH:mm>'
  utcOffset: '<+01:00>'
}

param nodeSubnetId = '<resourceId snet-aks-nodes-pro>'
param apiServerSubnetId = '<resourceId snet-aks-apiserver-pro>'
param vnetId = '<resourceId vnet-spoke-aks-pro>'
param routeTableId = '<resourceId rt-aks-pro>'
param privateDnsZoneId = '<resourceId private.<region>.azmk8s.io>'
param outboundType = 'userDefinedRouting'
param podCidr = '<cidr-pods>'
param serviceCidr = '<cidr-servicios>'
param dnsServiceIp = '<ip-dentro-de-service_cidr>'

param adminGroupObjectIds = ['<objectId grupo aks-admins-pro>']

param systemPool = {
  vmSize: '<Standard_D4ds_v5>'
  osDiskSizeGB: 128
  minCount: 3
  maxCount: 5
}

param nodePools = [
  {
    name: 'apps'
    vmSize: '<Standard_D8ds_v5>'
    osDiskSizeGB: 128
    minCount: 3
    maxCount: 12
    nodeLabels: { workload: 'apps' }
  }
  {
    name: 'batch'
    vmSize: '<Standard_D8ds_v5>'
    priority: 'Spot'
    minCount: 0
    maxCount: 10
    nodeLabels: { workload: 'batch' }
  }
]

param safeguardsLevel = 'Warn'
param podSecurityStandardsLevel = 'Baseline'

param acrPull = [
  {
    registryId: '<resourceId crworkloadpro01>'
    role: 'Container Registry Repository Reader'
  }
]

param logAnalyticsWorkspaceId = '<resourceId log-platform-pro>'

param tags = {
  environment: 'pro'
  workload: '<workload>'
  owner: '<owner>'
  costcenter: '<costcenter>'
  dataclassification: 'internal'
}
```

Despliegue:

```powershell
New-AzResourceGroupDeployment -ResourceGroupName "<rg-aks-workload-pro>" `
    -TemplateParameterFile "aks-workload-pro-01.bicepparam" -Name "aks-workload-pro-01"
```

## Errores típicos

| Síntoma | Causa | Solución |
|---|---|---|
| El clúster falla al aprovisionarse con VNet Integration | La identidad del plano de control no tiene permisos en la subred del API server | Network Contributor en las subredes del API server y de nodos **antes** de crear el clúster (la plantilla lo hace con `depends_on`) |
| `Invalid dynamic for_each value` en el módulo `kubernetes_cluster` | `service_principal` sensible usado en `for_each` | Recurso nativo |
| `Invalid function argument` en el módulo `role_assignment` | `contains()` con `condition_version` nulo | Recurso `azurerm_role_assignment` nativo |
| Falla la creación con una zona DNS propia en hub-spoke | La identidad no puede enlazar la zona a la VNet del clúster | Network Contributor en la VNet (`vnet_id`) y Private DNS Zone Contributor en la zona |
| La zona privada propia se rechaza | Formato equivocado: con VNet Integration es `private.<región>.azmk8s.io` | Validación del root |
| `kubectl` no conecta desde fuera de la VNet | Clúster privado | VPN, ExpressRoute, Bastion o jump box en una red conectada; o `az aks command invoke` |
| `kubectl` pide credenciales y las rechaza | Cuentas locales desactivadas: solo Entra ID | `kubelogin convert-kubeconfig -l azurecli`; en pipelines, `-l azurepipelines` o workload identity |
| Error de ruta al crear con `userDefinedRouting` | La subred no tiene tabla de rutas con `0.0.0.0/0` hacia un NVA | Asociar la tabla antes de crear el clúster |
| Nodos `NotReady` o imágenes que no descargan tras el firewall | Faltan reglas de salida de AKS | Regla de aplicación con el FQDN tag `AzureKubernetesService` y las reglas de red de la documentación |
| Pods de aplicación en `Pending` | El pool de sistema tiene el taint `CriticalAddonsOnly` | Pool de usuario |
| Error de validación con disco efímero | El disco no cabe en la caché o el temporal de la VM | Reducir `os_disk_size_gb` o elegir otro tamaño |
| `EncryptionAtHost` no está habilitado | Característica no registrada en la suscripción | Registrarla antes del despliegue |
| No se puede crear un pool Spot como pool de sistema | Spot solo en pools de usuario | Validación del root |
| Pool Azure Linux 2.0 que no escala | Imágenes retiradas el 31 de octubre de 2026 | `os_sku = "AzureLinux3"` |
| La actualización de versión se bloquea | AKS detecta uso de APIs eliminadas en la versión destino | Actualizar manifiestos; el bloqueo no aplica a las actualizaciones de plataforma |
| El plan quiere bajar la versión de Kubernetes | `kubernetes_version` fija con canal automático | Dejarla en null (la validación lo exige) |
| El plan cambia `node_count` en cada ejecución | Escalador automático | `ignore_changes` (incluido) |
| Ventana de mantenimiento rechazada | Duración inferior a 4 horas | De 4 a 24 horas |
| `401` al descargar de ACR | La identidad kubelet tiene `AcrPull` en un registro ABAC, o el registro pasó a ABAC con credenciales en caché | `Container Registry Repository Reader`; ver [Container Registry](/recursos/compute/container-registry/) |
| Safeguards no se aplican | Falta el complemento de Azure Policy o `Microsoft.PolicyInsights` sin registrar | `azure_policy_enabled = true` (fijo) y registrar el proveedor |
| Coste alto de Log Analytics | `kube-audit` completo | `kube-audit-admin` y plan Basic en la tabla `AKSAudit` si hace falta |
| Agotamiento de SNAT en el firewall | Pocas IPs públicas | Al menos 20 IPs o NAT Gateway en el firewall |
| `terraform destroy` falla | Bloqueo `CanNotDelete` | Quitar `lock_enabled` de forma explícita |
