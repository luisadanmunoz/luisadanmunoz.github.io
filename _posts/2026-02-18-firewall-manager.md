---
title: Azure Firewall Manager
area: azure/networking
owner: LuisAdan
categories: [Resources, Redes]
tags:
  - azure
  - firewall-manager
  - network-security
  - centralized-security
  - virtual-wan
  - hub-spoke
  - policy-management
  - zero-trust
cost: https://azure.microsoft.com/pricing/details/firewall-manager/
repo: https://github.com/org/azure-firewall-manager-iac
last_review: 2026-02-18
---

## 📋 Características

**Firewall Manager** es servicio de gestión centralizada para Azure Firewall y políticas de seguridad. Administración multi-firewall, políticas heredadas, integración con Virtual WAN.

### Pricing

✅ **FREE** - No charge por Firewall Manager

**Costos asociados:**
- Azure Firewall: $913-1,314/mes por instancia
- Firewall Policy: $100/mes por política base + $20/mes por 1000 reglas

**Ejemplo:**
```
Hub-and-spoke: 3 Azure Firewalls, 1 política compartida
Firewalls: 3 × $913 = $2,739/mes
Policy (base): $100/mes
Policy (5000 reglas): 5 × $20 = $100/mes
Total: ~$2,939/mes

vs Gestión manual: Mismo costo pero centralizado
Firewall Manager: FREE, facilita gestión
```

---

## 🏆 Best Practices

### Topologías
- ✅ **Secured virtual hub**: Virtual WAN + Firewall
- ✅ **Hub VNet**: Traditional hub-and-spoke
- ✅ **Multiple hubs**: Multi-region deployments
- ✅ **Hybrid**: On-prem + cloud

### Firewall Policies
- ✅ **Base policy**: Políticas corporativas
- ✅ **Child policies**: Herencia para equipos
- ✅ **Rule collections**: Organizar reglas
- ✅ **Priority**: Orden de evaluación (100-65000)
- ✅ **DNAT, Network, Application**: Tipos de reglas

### Gestión centralizada
- ✅ **Multi-firewall**: Un lugar para todos
- ✅ **Policy hierarchy**: Base + derivadas
- ✅ **Threat Intelligence**: Compartido
- ✅ **DNS settings**: Configuración centralizada
- ✅ **TLS inspection**: Certificados compartidos

### Security Partners
- ✅ **Check Point**: CloudGuard
- ✅ **iboss**: Cloud Security
- ✅ **Zscaler**: Internet Access
- ✅ **Integration**: Routing automático

### Deployment
- ✅ **Azure Portal**: UI deployment
- ✅ **ARM templates**: Infrastructure as Code
- ✅ **Terraform**: Multi-cloud IaC
- ✅ **Azure CLI/PowerShell**: Automation

### Monitoring
- ✅ **Workbooks**: Dashboards integrados
- ✅ **Diagnostic logs**: Azure Monitor
- ✅ **Metrics**: Performance tracking
- ✅ **Alerts**: Anomalías y eventos

---

## ⚠️ Limitaciones

- Requires: Azure Firewall SKU Standard o Premium
- Policy limit: 100 policies per subscription
- Regional: Policies region-specific
- Virtual WAN: Requiere Secured Hub creation

---

## ✅ Checklist

- [ ] Firewall Manager enabled
- [ ] Firewall Policy creada (base)
- [ ] Rule collections configuradas
- [ ] Child policies creadas (por equipo)
- [ ] Azure Firewalls asociadas a policies
- [ ] Threat Intelligence habilitado
- [ ] DNS settings configurados
- [ ] Security partners integrados (si aplica)
- [ ] Monitoring dashboard configurado
- [ ] Alerts establecidas
- [ ] Backup de policies documentado
- [ ] Change management process
