---
title: Azure Private Link
area: azure/networking
owner: LuisAdan
categories: [Resources, Redes]
tags:
  - azure
  - private-link
  - private-endpoint
  - network-security
  - zero-trust
  - service-connectivity
  - data-exfiltration-prevention
  - hybrid-networking
cost: https://azure.microsoft.com/pricing/details/private-link/
repo: https://github.com/org/azure-private-link-iac
last_review: 2026-02-18
---

## 📋 Características

**Private Link** permite acceso privado a servicios Azure PaaS sobre red privada. Private endpoints en VNet, sin exposición pública, tráfico permanece en backbone Microsoft.

### Pricing

**Private Endpoint:**
- $0.01/hora (~$7.30/mes) por endpoint
- Data processing: $0.01/GB

**Private Link Service:**
- $0.03/hora (~$22/mes) por servicio
- Data processing: $0.01/GB

**Ejemplo:**
```
5 servicios con Private Endpoints:
Endpoints: 5 × $7.30 = $36.50/mes
Data transfer (100 GB): 100 × $0.01 = $1
Total: ~$37.50/mes

vs Public endpoints + ExpressRoute:
ExpressRoute: $1,800/mes
Private Link: 98% más económico
Plus: Mejor security posture
```

---

## 🏆 Best Practices

### Casos de uso
- ✅ **Security**: Eliminar exposición pública
- ✅ **Compliance**: Datos no salen de red privada
- ✅ **Hybrid**: Conectar on-prem a PaaS
- ✅ **Cross-tenant**: Servicios entre tenants
- ✅ **SaaS providers**: Ofrecer acceso privado

### Servicios soportados
- ✅ **Storage**: Blob, File, Queue, Table
- ✅ **SQL**: SQL Database, Managed Instance
- ✅ **Cosmos DB**: NoSQL database
- ✅ **Key Vault**: Secrets management
- ✅ **App Service**: Web apps
- ✅ **100+ servicios**: Cognitive, Synapse, etc.

### Private Endpoint
- ✅ **VNet integration**: NIC en subnet
- ✅ **Private IP**: Dirección IP privada
- ✅ **DNS integration**: Private DNS zone
- ✅ **NSG**: Network security groups
- ✅ **Multiple endpoints**: Diferentes subnets

### Private Link Service
- ✅ **Custom services**: Exponer tus servicios
- ✅ **Standard Load Balancer**: Required
- ✅ **Auto-approval**: Confianza automática
- ✅ **Manual approval**: Control acceso
- ✅ **Visibility**: Quien puede ver servicio

### DNS Configuration
- ✅ **Private DNS Zone**: Azure DNS automático
- ✅ **DNS forwarding**: On-prem integration
- ✅ **Conditional forwarding**: Hybrid scenarios
- ✅ **privatelink.* zones**: Por servicio

### Security
- ✅ **No public IP**: Tráfico totalmente privado
- ✅ **NSG support**: Network filtering
- ✅ **UDR support**: Custom routing
- ✅ **Azure Firewall**: Inspect traffic
- ✅ **Audit logs**: Connection tracking

### Networking
- ✅ **Hub-spoke**: Central private endpoints
- ✅ **Multi-region**: Endpoints por región
- ✅ **Cross-VNet**: Peering connections
- ✅ **ExpressRoute**: On-prem connectivity
- ✅ **VPN**: Site-to-site access

---

## ⚠️ Limitaciones

- Por VNet: Max 1000 private endpoints
- DNS: Requiere Private DNS zones
- Some services: No todos soportan Private Link
- Cross-region: Separate endpoint needed
- IP address: Consume una IP del subnet

---

## ✅ Checklist

- [ ] Servicio PaaS identificado
- [ ] Subnet para private endpoints creado
- [ ] Private endpoint creado
- [ ] Private DNS zone creada
- [ ] DNS zone linked to VNet
- [ ] A record verificado
- [ ] Connectivity probada (private IP)
- [ ] Public access deshabilitado (servicio)
- [ ] NSG rules ajustadas
- [ ] On-prem DNS forwarding (si hybrid)
- [ ] Monitoring configurado
- [ ] Documentation actualizada
