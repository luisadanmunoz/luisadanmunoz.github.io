---
title: Azure Managed Grafana
area: azure/monitoring
owner: LuisAdan
categories: [Resources, Monitoreo]
tags:
  - azure
  - managed-grafana
  - monitoring
  - observability
  - dashboards
  - visualization
  - prometheus
  - azure-monitor
cost: https://azure.microsoft.com/pricing/details/managed-grafana/
repo: https://github.com/org/azure-managed-grafana-iac
last_review: 2026-02-18
---

## 📋 Características

**Managed Grafana** es fully managed Grafana service. Built-in Azure Monitor integration, alerting, dashboards, plugins. Grafana 9+.

### Pricing

**Standard tier:**
- Active users: $8.30/user/mes
- Viewers: FREE (unlimited)

**Example:**
```
Team: 10 editors + 50 viewers
Editors: 10 × $8.30 = $83/mes
Viewers: 50 × $0 = $0
Total: ~$83/mes
```

**Data sources:** Standard pricing (Log Analytics, etc.)

---

## 🏆 Best Practices

### Data Sources
- ✅ **Azure Monitor**: Native integration
- ✅ **Log Analytics**: KQL queries
- ✅ **Application Insights**: APM data
- ✅ **Prometheus**: Metrics
- ✅ **Managed Prometheus**: Azure native
- ✅ **Third-party**: MySQL, PostgreSQL, InfluxDB

### Dashboards
- ✅ **Pre-built**: Azure Monitor dashboards
- ✅ **Custom**: Build from scratch
- ✅ **Variables**: Dynamic dashboards
- ✅ **Annotations**: Mark events
- ✅ **Folders**: Organize dashboards

### Alerting
- ✅ **Alert rules**: Grafana-managed alerts
- ✅ **Contact points**: Email, Slack, Teams, webhook
- ✅ **Notification policies**: Routing rules
- ✅ **Silences**: Mute alerts temporarily
- ✅ **Azure Monitor alerts**: Integration

### Authentication
- ✅ **Azure AD**: SSO integration
- ✅ **RBAC**: Grafana roles (Admin, Editor, Viewer)
- ✅ **Service principal**: API access
- ✅ **Anonymous**: Public dashboards (optional)

### Plugins
- ✅ **Pre-installed**: Azure plugins
- ✅ **Visualization**: Charts, graphs, tables
- ✅ **Data sources**: Extend connectivity
- ✅ **App plugins**: Custom apps

### High Availability
- ✅ **Zone redundancy**: Built-in
- ✅ **SLA**: 99.9% uptime
- ✅ **Backup**: Automatic dashboard backup
- ✅ **Scaling**: Auto-managed

---

## ⚠️ Limitaciones

- Grafana version: Managed version (Grafana 9+)
- Plugin installation: Limited to approved plugins
- Custom code: No backend plugins
- Max dashboards: Soft limits (thousands supported)

---

## ✅ Checklist

- [ ] Managed Grafana created
- [ ] Azure AD integration configured
- [ ] Data sources added (Azure Monitor, LA)
- [ ] RBAC roles assigned
- [ ] Dashboards imported/created
- [ ] Alerts configured
- [ ] Contact points set up
- [ ] Notification policies defined
- [ ] Folders organized
- [ ] Team members invited
- [ ] Public dashboards (if needed)
