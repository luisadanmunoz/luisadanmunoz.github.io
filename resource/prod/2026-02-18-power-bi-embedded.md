---
title: Power BI Embedded
area: azure/analytics
owner: LuisAdan
categories: [Resources, Analítica]
tags:
  - azure
  - power-bi
  - embedded
  - analytics
  - business-intelligence
  - reporting
  - dashboards
  - visualization
cost: https://azure.microsoft.com/pricing/details/power-bi-embedded/
repo: https://github.com/org/azure-power-bi-embedded-iac
last_review: 2026-02-18
---

## 📋 Características

**Power BI Embedded** permite embed Power BI reports/dashboards en apps. White-label analytics, row-level security, API control.

### Pricing (Capacity-based)

**Azure SKUs (A-series):**
| SKU | v-Cores | RAM | Precio/hora | Precio/mes (24/7) |
|-----|---------|-----|-------------|-------------------|
| **A1** | 1 | 3GB | $1.00 | ~$730 |
| **A2** | 2 | 5GB | $2.00 | ~$1,460 |
| **A3** | 4 | 25GB | $4.00 | ~$2,920 |
| **A4** | 8 | 25GB | $8.00 | ~$5,840 |

**Auto-pause:** Save costs when not in use

**Example:**
```
A2 capacity, 8h/day business hours:
$2.00 × 240 hours = $480/mes

vs 24/7: $1,460/mes
Savings: 67%
```

**Rendering:** $0.02 per page view (optional)

---

## 🏆 Best Practices

### Capacity Planning
- ✅ **A1**: Development/testing
- ✅ **A2**: Small production (<100 users)
- ✅ **A3**: Medium production (100-500 users)
- ✅ **A4+**: Large production (500+ users)

### Performance
- ✅ **Auto-pause**: Reduce costs (5-min idle)
- ✅ **Scale up/down**: Match usage patterns
- ✅ **Query optimization**: Efficient DAX
- ✅ **Incremental refresh**: Large datasets
- ✅ **DirectQuery vs Import**: Choose wisely

### Security
- ✅ **Row-Level Security (RLS)**: Data isolation
- ✅ **App-owns-data**: Service principal auth
- ✅ **User-owns-data**: User authentication
- ✅ **Embed tokens**: Time-limited access

### Deployment
- ✅ **Workspaces**: Organize content
- ✅ **Deployment pipelines**: Dev/test/prod
- ✅ **APIs**: Automate operations
- ✅ **Multi-tenancy**: Isolated workspaces

### Monitoring
- ✅ **Capacity metrics**: CPU, memory
- ✅ **Query performance**: Slow queries
- ✅ **Usage patterns**: Peak times
- ✅ **Auto-scale**: Trigger rules

---

## ⚠️ Limitaciones

- A1-A3: Max 48 refreshes/day
- Dataset size: SKU-dependent
- Premium features: Require higher SKUs
- Concurrent queries: Limited per SKU

---

## ✅ Checklist

- [ ] Capacity created (A-series)
- [ ] Workspace created
- [ ] Reports/dashboards published
- [ ] RLS configured
- [ ] Embed tokens implemented
- [ ] App registered (Azure AD)
- [ ] Service principal assigned
- [ ] Auto-pause configured
- [ ] Monitoring enabled
- [ ] Cost alerts set
