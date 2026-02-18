---
title: Arquitectura Multi-Región en Azure: Traffic Manager, Front Door y Application Gateway
area: azure/networking
categories: [Resources, Networking]
owner: LuisAdan
tags:
  - azure
  - Traffic Manager
  - Front Door
  - Application Gateway
cost: URL
repo: URL
last_review: 2025-11-05
---
## Introducción

En arquitecturas empresariales modernas, la alta disponibilidad global es un requisito crítico. Azure ofrece múltiples servicios de balanceo de carga, pero ¿cuándo usar cada uno? En este artículo explico cómo diseñar una arquitectura multi-región robusta combinando Traffic Manager, Azure Front Door y Application Gateway.

## El Problema

Imagina que necesitas:
- **Alta disponibilidad global**: aplicación disponible 24/7 incluso si una región falla
- **Optimización de latencia**: usuarios en Europa y América con experiencia óptima
- **Seguridad en capas**: WAF, DDoS protection, y control de tráfico
- **Escalabilidad regional**: capacidad de escalar independientemente por región

La pregunta es: ¿un solo servicio de Azure puede cubrir todo esto?

**Respuesta corta**: No. Necesitas una arquitectura en capas.

## Los Tres Servicios Clave

### Traffic Manager - Routing DNS Global

**Qué es**: Load balancer basado en DNS que opera en la capa de red.

**Cuándo usarlo**:
- Necesitas routing global entre regiones
- Failover automático entre regiones
- Soportas tráfico no-HTTP (TCP, UDP)

**Ventajas**:
- Routing methods: Performance, Priority, Geographic, Weighted
- Health monitoring de endpoints
- Bajo costo (~$0.54/millón de queries)
- Agnóstico al protocolo

**Limitaciones**:
- Solo DNS routing (no procesa tráfico HTTP directamente)
- Latencia de DNS TTL en failover (30-90 segundos)
- No tiene WAF integrado
- No hace SSL termination

### Azure Front Door - Global Application Delivery

**Qué es**: Global Layer 7 load balancer con CDN, WAF y aceleración de tráfico.

**Cuándo usarlo**:
- Aplicaciones web HTTP/HTTPS exclusivamente
- Necesitas CDN + WAF en el edge
- Quieres SSL offloading global
- Aceleración de contenido dinámico

**Ventajas**:
- Anycast network (Microsoft global edge)
- WAF integrado con managed rules
- Caching inteligente
- SSL/TLS termination
- Failover instantáneo (sin DNS TTL)
- URL-based routing, rewrites, redirects

**Limitaciones**:
- Solo HTTP/HTTPS
- Costo más alto (~$22/mes + $0.20/GB)
- No soporta tráfico L4 genérico

### Application Gateway - Regional Load Balancer

**Qué es**: Load balancer regional Layer 7 con WAF y routing avanzado.

**Cuándo usarlo**:
- Load balancing dentro de una región
- Necesitas WAF a nivel regional
- Routing complejo basado en paths/headers
- Integración con VNet y Private Link

**Ventajas**:
- Autoscaling y zone redundancy
- WAF con OWASP rules
- SSL offloading
- URL-based routing
- Cookie-based session affinity
- Private connectivity

**Limitaciones**:
- Servicio regional (no global)
- No tiene capacidades CDN
- Costo por instancia (~$150-250/mes)

## Arquitectura Multi-Región Recomendada

### Opción 1: Traffic Manager → Front Door → Application Gateway

```
                    Traffic Manager
                    (DNS Global Routing)
                           |
        +------------------+------------------+
        |                                     |
   Front Door                            Front Door
   (Primary - West Europe)            (Secondary - East US)
        |                                     |
   App Gateway                           App Gateway
   (Regional LB + WAF)                  (Regional LB + WAF)
        |                                     |
   Backend Pool                          Backend Pool
   (VMs/VMSS/AKS)                       (VMs/VMSS/AKS)
```

**Flujo de tráfico**:
1. Usuario hace DNS query → Traffic Manager
2. Traffic Manager devuelve Front Door endpoint más cercano
3. Front Door enruta a región óptima (con CDN + WAF edge)
4. Application Gateway distribuye tráfico regional (WAF regional + routing)
5. Backend pool procesa request

**Cuándo usar esta arquitectura**:
- Máxima redundancia y seguridad
- Necesitas inspección multi-capa (WAF en edge + regional)
- Aplicación requiere routing complejo regional
- Budget permite triple stack

### Opción 2: Traffic Manager → Application Gateway (Más Común)

```
                    Traffic Manager
                    (DNS Global Routing)
                           |
        +------------------+------------------+
        |                                     |
   App Gateway                           App Gateway
   (West Europe)                         (East US)
        |                                     |
   Backend Pool                          Backend Pool
```

**Cuándo usar**:
- No necesitas CDN
- WAF regional es suficiente
- Costos optimizados
- Tráfico no requiere aceleración global

### Opción 3: Front Door → Application Gateway (Recomendada para Web)

```
                    Front Door
                    (Global Entry Point)
                           |
        +------------------+------------------+
        |                                     |
   App Gateway                           App Gateway
   (West Europe)                         (East US)
        |                                     |
   Backend Pool                          Backend Pool
```

**Cuándo usar**:
- Solo tráfico HTTP/HTTPS
- Necesitas CDN + aceleración
- Quieres failover instantáneo (sin DNS TTL)
- Preferencia por gestión simplificada

**Ventaja clave**: Front Door maneja failover sin depender de DNS TTL, resultando en tiempos de failover más rápidos (segundos vs minutos).

## Implementación Terraform

### Estructura de Proyecto

```
terraform/
├── modules/
│   ├── traffic-manager/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   ├── front-door/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   └── application-gateway/
│       ├── main.tf
│       ├── variables.tf
│       └── outputs.tf
└── environments/
    └── production/
        ├── main.tf
        ├── region-primary.tf
        └── region-secondary.tf
```

### Traffic Manager Module

```hcl
# modules/traffic-manager/main.tf
resource "azurerm_traffic_manager_profile" "main" {
  name                   = "tm-${var.project}-${var.environment}"
  resource_group_name    = var.resource_group_name
  traffic_routing_method = var.routing_method

  dns_config {
    relative_name = "tm-${var.project}"
    ttl           = 30
  }

  monitor_config {
    protocol                     = "HTTPS"
    port                         = 443
    path                         = "/health"
    interval_in_seconds          = 30
    timeout_in_seconds           = 10
    tolerated_number_of_failures = 3
  }

  tags = var.tags
}

# Endpoint Primary Region
resource "azurerm_traffic_manager_azure_endpoint" "primary" {
  name               = "endpoint-primary-${var.primary_region}"
  profile_id         = azurerm_traffic_manager_profile.main.id
  target_resource_id = var.primary_endpoint_id
  weight             = var.primary_weight
  priority           = var.primary_priority
  
  # Opcional: Geographic mappings
  dynamic "geo_mappings" {
    for_each = var.routing_method == "Geographic" ? [1] : []
    content {
      location = var.primary_geo_mapping
    }
  }
}

# Endpoint Secondary Region
resource "azurerm_traffic_manager_azure_endpoint" "secondary" {
  name               = "endpoint-secondary-${var.secondary_region}"
  profile_id         = azurerm_traffic_manager_profile.main.id
  target_resource_id = var.secondary_endpoint_id
  weight             = var.secondary_weight
  priority           = var.secondary_priority

  dynamic "geo_mappings" {
    for_each = var.routing_method == "Geographic" ? [1] : []
    content {
      location = var.secondary_geo_mapping
    }
  }
}
```

```hcl
# modules/traffic-manager/variables.tf
variable "project" {
  type        = string
  description = "Nombre del proyecto"
}

variable "environment" {
  type        = string
  description = "Ambiente"
  validation {
    condition     = contains(["prod", "staging", "dev"], var.environment)
    error_message = "Valores permitidos: prod, staging, dev"
  }
}

variable "resource_group_name" {
  type        = string
  description = "Nombre del resource group"
}

variable "routing_method" {
  type        = string
  description = "Método de routing"
  default     = "Performance"
  validation {
    condition     = contains(["Performance", "Geographic", "Priority", "Weighted"], var.routing_method)
    error_message = "Método inválido"
  }
}

variable "primary_endpoint_id" {
  type        = string
  description = "Resource ID del endpoint primary"
}

variable "secondary_endpoint_id" {
  type        = string
  description = "Resource ID del endpoint secondary"
}

variable "primary_weight" {
  type        = number
  description = "Weight para primary endpoint"
  default     = 100
}

variable "secondary_weight" {
  type        = number
  description = "Weight para secondary endpoint"
  default     = 100
}

variable "primary_priority" {
  type        = number
  description = "Priority para primary endpoint (1 = highest)"
  default     = 1
}

variable "secondary_priority" {
  type        = number
  description = "Priority para secondary endpoint"
  default     = 2
}

variable "primary_region" {
  type        = string
  description = "Primary region name"
}

variable "secondary_region" {
  type        = string
  description = "Secondary region name"
}

variable "primary_geo_mapping" {
  type        = list(string)
  description = "Geographic mappings para primary"
  default     = []
}

variable "secondary_geo_mapping" {
  type        = list(string)
  description = "Geographic mappings para secondary"
  default     = []
}

variable "tags" {
  type        = map(string)
  description = "Tags"
  default     = {}
}
```

```hcl
# modules/traffic-manager/outputs.tf
output "id" {
  value       = azurerm_traffic_manager_profile.main.id
  description = "Resource ID del Traffic Manager Profile"
}

output "fqdn" {
  value       = azurerm_traffic_manager_profile.main.fqdn
  description = "FQDN del Traffic Manager"
}

output "primary_endpoint_id" {
  value       = azurerm_traffic_manager_azure_endpoint.primary.id
  description = "ID del endpoint primary"
}

output "secondary_endpoint_id" {
  value       = azurerm_traffic_manager_azure_endpoint.secondary.id
  description = "ID del endpoint secondary"
}
```

### Application Gateway Module (Simplificado)

```hcl
# modules/application-gateway/main.tf
resource "azurerm_public_ip" "main" {
  name                = "pip-appgw-${var.region_suffix}"
  location            = var.location
  resource_group_name = var.resource_group_name
  allocation_method   = "Static"
  sku                 = "Standard"
  zones               = ["1", "2", "3"]

  tags = var.tags
}

resource "azurerm_application_gateway" "main" {
  name                = "appgw-${var.project}-${var.region_suffix}"
  location            = var.location
  resource_group_name = var.resource_group_name
  zones               = ["1", "2", "3"]

  sku {
    name     = var.sku_name
    tier     = var.sku_tier
    capacity = var.capacity
  }

  gateway_ip_configuration {
    name      = "gateway-ip-config"
    subnet_id = var.subnet_id
  }

  frontend_port {
    name = "frontend-port-https"
    port = 443
  }

  frontend_port {
    name = "frontend-port-http"
    port = 80
  }

  frontend_ip_configuration {
    name                 = "frontend-ip-config"
    public_ip_address_id = azurerm_public_ip.main.id
  }

  backend_address_pool {
    name = "backend-pool"
  }

  backend_http_settings {
    name                  = "backend-http-settings"
    cookie_based_affinity = "Disabled"
    port                  = 80
    protocol              = "Http"
    request_timeout       = 60

    probe_name = "health-probe"
  }

  http_listener {
    name                           = "http-listener"
    frontend_ip_configuration_name = "frontend-ip-config"
    frontend_port_name             = "frontend-port-http"
    protocol                       = "Http"
  }

  request_routing_rule {
    name                       = "routing-rule"
    rule_type                  = "Basic"
    http_listener_name         = "http-listener"
    backend_address_pool_name  = "backend-pool"
    backend_http_settings_name = "backend-http-settings"
    priority                   = 100
  }

  probe {
    name                = "health-probe"
    protocol            = "Http"
    path                = "/health"
    interval            = 30
    timeout             = 30
    unhealthy_threshold = 3
    host                = "127.0.0.1"
  }

  # WAF Configuration
  dynamic "waf_configuration" {
    for_each = var.sku_tier == "WAF_v2" ? [1] : []
    content {
      enabled          = true
      firewall_mode    = var.waf_mode
      rule_set_type    = "OWASP"
      rule_set_version = "3.2"
    }
  }

  tags = var.tags
}
```

### Deployment Multi-Región

```hcl
# environments/production/main.tf
terraform {
  required_version = ">= 1.5.0"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }

  backend "azurerm" {
    resource_group_name  = "rg-terraform-state"
    storage_account_name = "stterraformstate"
    container_name       = "tfstate"
    key                  = "multi-region-prod.tfstate"
  }
}

provider "azurerm" {
  features {}
}

# Resource Groups
resource "azurerm_resource_group" "global" {
  name     = "rg-global-prod"
  location = "westeurope"

  tags = local.common_tags
}

resource "azurerm_resource_group" "primary" {
  name     = "rg-primary-westeurope-prod"
  location = "westeurope"

  tags = local.common_tags
}

resource "azurerm_resource_group" "secondary" {
  name     = "rg-secondary-eastus-prod"
  location = "eastus"

  tags = local.common_tags
}

# Virtual Networks
module "vnet_primary" {
  source = "../../modules/virtual-network"

  name                = "vnet-primary-weu"
  location            = azurerm_resource_group.primary.location
  resource_group_name = azurerm_resource_group.primary.name
  address_space       = ["10.0.0.0/16"]

  subnets = {
    appgw = {
      address_prefixes = ["10.0.1.0/24"]
    }
    backend = {
      address_prefixes = ["10.0.2.0/24"]
    }
  }

  tags = local.common_tags
}

module "vnet_secondary" {
  source = "../../modules/virtual-network"

  name                = "vnet-secondary-eus"
  location            = azurerm_resource_group.secondary.location
  resource_group_name = azurerm_resource_group.secondary.name
  address_space       = ["10.1.0.0/16"]

  subnets = {
    appgw = {
      address_prefixes = ["10.1.1.0/24"]
    }
    backend = {
      address_prefixes = ["10.1.2.0/24"]
    }
  }

  tags = local.common_tags
}

# Application Gateways
module "appgw_primary" {
  source = "../../modules/application-gateway"

  project             = var.project
  location            = azurerm_resource_group.primary.location
  resource_group_name = azurerm_resource_group.primary.name
  region_suffix       = "weu"
  subnet_id           = module.vnet_primary.subnet_ids["appgw"]
  
  sku_name  = "WAF_v2"
  sku_tier  = "WAF_v2"
  capacity  = 2
  waf_mode  = "Prevention"

  tags = local.common_tags
}

module "appgw_secondary" {
  source = "../../modules/application-gateway"

  project             = var.project
  location            = azurerm_resource_group.secondary.location
  resource_group_name = azurerm_resource_group.secondary.name
  region_suffix       = "eus"
  subnet_id           = module.vnet_secondary.subnet_ids["appgw"]
  
  sku_name  = "WAF_v2"
  sku_tier  = "WAF_v2"
  capacity  = 2
  waf_mode  = "Prevention"

  tags = local.common_tags
}

# Traffic Manager
module "traffic_manager" {
  source = "../../modules/traffic-manager"

  project             = var.project
  environment         = var.environment
  resource_group_name = azurerm_resource_group.global.name
  
  routing_method = "Performance"
  
  primary_endpoint_id   = module.appgw_primary.public_ip_id
  secondary_endpoint_id = module.appgw_secondary.public_ip_id
  
  primary_region   = "westeurope"
  secondary_region = "eastus"
  
  primary_priority   = 1
  secondary_priority = 2

  tags = local.common_tags
}

# Locals
locals {
  common_tags = {
    Project     = var.project
    Environment = var.environment
    ManagedBy   = "Terraform"
    CostCenter  = "Engineering"
  }
}

# Variables
variable "project" {
  type        = string
  description = "Nombre del proyecto"
  default     = "webapp"
}

variable "environment" {
  type        = string
  description = "Ambiente"
  default     = "prod"
}

# Outputs
output "traffic_manager_fqdn" {
  value       = module.traffic_manager.fqdn
  description = "FQDN del Traffic Manager para acceso público"
}

output "primary_appgw_public_ip" {
  value       = module.appgw_primary.public_ip_address
  description = "IP pública del Application Gateway primary"
}

output "secondary_appgw_public_ip" {
  value       = module.appgw_secondary.public_ip_address
  description = "IP pública del Application Gateway secondary"
}
```

## Consideraciones de Diseño

### Métodos de Routing en Traffic Manager

**Performance** (Recomendado para multi-región):
- Enruta al endpoint con menor latencia
- Ideal para optimizar experiencia de usuario
- Azure mide latencia real desde diferentes ubicaciones

**Priority** (Disaster Recovery):
- Active-Passive failover
- Primary recibe 100% del tráfico
- Secondary solo se activa si primary falla

**Geographic**:
- Routing basado en ubicación geográfica
- Útil para compliance (GDPR, data residency)
- Ejemplo: Europa → West Europe, América → East US

**Weighted**:
- Distribución porcentual del tráfico
- Útil para:
  - Blue-Green deployments
  - Canary releases
  - Testing en producción

### Health Monitoring

**Traffic Manager**:
```hcl
monitor_config {
  protocol                     = "HTTPS"
  port                         = 443
  path                         = "/health"
  interval_in_seconds          = 30
  timeout_in_seconds           = 10
  tolerated_number_of_failures = 3
}
```

**Implicaciones**:
- Failover time ≈ 60-90 segundos
- 3 fallos consecutivos = endpoint degraded
- DNS TTL adicional = 30 segundos mínimo

**Application Gateway**:
```hcl
probe {
  name                = "health-probe"
  protocol            = "Http"
  path                = "/health"
  interval            = 30
  timeout             = 30
  unhealthy_threshold = 3
}
```

**Best Practice**: Implementa endpoints `/health` que verifiquen:
- Conectividad a base de datos
- Disponibilidad de servicios dependientes
- Capacidad de procesamiento
- No solo un "200 OK" estático

### WAF en Múltiples Capas

**Front Door WAF** (Si se usa):
- Protección en el edge global
- Bloquea ataques antes de llegar a Azure
- Managed rules de Microsoft
- Custom rules para lógica específica

**Application Gateway WAF**:
- Protección regional
- Segunda capa de defensa
- OWASP Top 10 protection
- Puede tener reglas específicas por región

**Estrategia recomendada**:
- Front Door: Reglas generales + rate limiting
- App Gateway: Reglas específicas de aplicación

### Costos Estimados

**Escenario 1: Traffic Manager + App Gateway (2 regiones)**
```
Traffic Manager:
├── Profile: $0.54/million queries
└── Health checks: incluidos

Application Gateway (x2):
├── Gateway Hours: $0.36/hour × 720h = $259/mes/region
├── Data Processing: $0.008/GB
└── Total 2 regiones: ~$518/mes + data

TOTAL ESTIMADO: ~$550-700/mes
```

**Escenario 2: Front Door + App Gateway (2 regiones)**
```
Front Door Premium:
├── Base: $22/mes
├── Routing Rules: $2.40/mes
├── Data Transfer: $0.20/GB
└── WAF: $31.76/mes

Application Gateway (x2): ~$518/mes

TOTAL ESTIMADO: ~$600-900/mes + data
```

**Escenario 3: Traffic Manager + Front Door + App Gateway**
```
Traffic Manager: ~$15/mes
Front Door: ~$56/mes
Application Gateway (x2): ~$518/mes

TOTAL ESTIMADO: ~$600-1000/mes + data
```

### Optimización de Costos

1. **DR con secondary reducido**:
   - Primary: 3 instancias (full capacity)
   - Secondary: 1 instancia (warm standby)
   - Ahorro: ~30-40%

2. **Autoscaling inteligente**:
   ```hcl
   autoscale_configuration {
     min_capacity = 2
     max_capacity = 10
   }
   ```

3. **Reserved Capacity**:
   - Commitments de 1-3 años
   - Descuento hasta 30%

## Testing y Validación

### 1. Validar Health Probes

```bash
# Test Traffic Manager health
az network traffic-manager endpoint show \
  --name endpoint-primary-westeurope \
  --profile-name tm-webapp-prod \
  --resource-group rg-global-prod \
  --type azureEndpoints

# Test App Gateway health
az network application-gateway show-backend-health \
  --name appgw-webapp-weu \
  --resource-group rg-primary-westeurope-prod
```

### 2. Simular Failover

```bash
# Deshabilitar endpoint primary
az network traffic-manager endpoint update \
  --name endpoint-primary-westeurope \
  --profile-name tm-webapp-prod \
  --resource-group rg-global-prod \
  --type azureEndpoints \
  --endpoint-status Disabled

# Monitorear DNS resolution
watch -n 5 "nslookup tm-webapp.trafficmanager.net"

# Validar que apunta a secondary
curl -I https://tm-webapp.trafficmanager.net
```

### 3. Load Testing

```bash
# Usando Azure Load Testing
az load test create \
  --name "multi-region-test" \
  --test-plan-id "/subscriptions/.../test-plan" \
  --engine-instances 10 \
  --target-url "https://tm-webapp.trafficmanager.net"
```

## Monitoreo y Observabilidad

### Métricas Clave

**Traffic Manager**:
- Query volume by endpoint
- Endpoint health status
- Routing distribution

**Application Gateway**:
- Total requests
- Failed requests
- Backend response time
- Throughput
- Unhealthy host count

**Queries útiles - Log Analytics**:

```kusto
// Traffic Manager - Endpoint health changes
AzureDiagnostics
| where ResourceType == "TRAFFICMANAGERPROFILES"
| where Category == "ProbeHealthStatusEvents"
| project TimeGenerated, Resource, OperationName, ResultDescription
| order by TimeGenerated desc

// Application Gateway - Failed requests
AzureDiagnostics
| where ResourceType == "APPLICATIONGATEWAYS"
| where httpStatus_d >= 400
| summarize count() by bin(TimeGenerated, 5m), httpStatus_d, requestUri_s
| render timechart

// Application Gateway - Backend health
AzureDiagnostics
| where ResourceType == "APPLICATIONGATEWAYS"
| where Category == "ApplicationGatewayAccessLog"
| extend BackendServer = columnifexists("backendHostname_s", "")
| summarize 
    TotalRequests = count(),
    FailedRequests = countif(httpStatus_d >= 500)
    by BackendServer
| extend HealthPercentage = (TotalRequests - FailedRequests) * 100.0 / TotalRequests
```

### Alertas Recomendadas

```hcl
# Alert: Application Gateway unhealthy backends
resource "azurerm_monitor_metric_alert" "unhealthy_backends" {
  name                = "alert-unhealthy-backends"
  resource_group_name = azurerm_resource_group.primary.name
  scopes              = [module.appgw_primary.id]
  description         = "Alert when backends become unhealthy"
  severity            = 1

  criteria {
    metric_namespace = "Microsoft.Network/applicationGateways"
    metric_name      = "UnhealthyHostCount"
    aggregation      = "Average"
    operator         = "GreaterThan"
    threshold        = 0
  }

  action {
    action_group_id = azurerm_monitor_action_group.ops_team.id
  }
}

# Alert: Traffic Manager endpoint down
resource "azurerm_monitor_metric_alert" "endpoint_down" {
  name                = "alert-tm-endpoint-down"
  resource_group_name = azurerm_resource_group.global.name
  scopes              = [module.traffic_manager.id]
  description         = "Alert when Traffic Manager endpoint goes down"
  severity            = 0

  criteria {
    metric_namespace = "Microsoft.Network/trafficManagerProfiles"
    metric_name      = "ProbeAgentCurrentEndpointStateByProfileResourceId"
    aggregation      = "Maximum"
    operator         = "LessThan"
    threshold        = 1
  }

  action {
    action_group_id = azurerm_monitor_action_group.ops_team.id
  }
}
```

## Decisión: ¿Cuál Arquitectura Elegir?

### Usa Traffic Manager + Application Gateway si:
- ✅ No necesitas CDN
- ✅ WAF regional es suficiente
- ✅ Budget es limitado
- ✅ Tienes tráfico no-HTTP además de web
- ✅ Necesitas máximo control sobre routing regional

### Usa Front Door + Application Gateway si:
- ✅ Solo tráfico HTTP/HTTPS
- ✅ Necesitas CDN y aceleración global
- ✅ Quieres failover instantáneo (sin DNS delay)
- ✅ Requieres WAF en el edge
- ✅ Usuarios globales con requisitos de baja latencia

### Usa Traffic Manager + Front Door + Application Gateway si:
- ✅ Máxima redundancia es crítica
- ✅ Necesitas routing híbrido (HTTP + no-HTTP)
- ✅ Compliance requiere múltiples capas de seguridad
- ✅ Budget no es restricción principal
- ✅ Arquitectura enterprise con SLA 99.99%+

## Conclusión

La arquitectura multi-región en Azure no es one-size-fits-all. La combinación correcta de Traffic Manager, Front Door y Application Gateway depende de:

1. **Tipo de tráfico**: HTTP-only vs multi-protocolo
2. **Requisitos de latencia**: Cuán crítica es la experiencia global
3. **Presupuesto**: Costos operacionales vs disponibilidad
4. **Complejidad**: Capacidad de gestión del equipo

**Mi recomendación general**: 
- **Startups/SMB**: Front Door + App Gateway
- **Enterprise**: Traffic Manager + App Gateway (con opción de agregar Front Door después)
- **Global Scale**: Front Door + App Gateway (sin Traffic Manager)

La clave está en **empezar simple** y escalar la arquitectura según crecen los requisitos. Azure permite agregar capas incrementalmente sin rediseño completo.

## Referencias

- [Multi-region load balancing - Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/high-availability/reference-architecture-traffic-manager-application-gateway)
- [Use Azure Traffic Manager with Application Gateway](https://learn.microsoft.com/en-us/azure/traffic-manager/traffic-manager-use-with-application-gateway)
- [Azure Front Door Best Practices](https://learn.microsoft.com/en-us/azure/frontdoor/best-practices)
- [Well-Architected Framework - Traffic Manager](https://learn.microsoft.com/en-us/azure/well-architected/service-guides/azure-traffic-manager)

---

*Luis Muñoz - Cloud Infrastructure & Azure Automation Specialist*  
*Blog: [luisadanmunoz.github.io/posts](https://luisadanmunoz.github.io/posts)*
