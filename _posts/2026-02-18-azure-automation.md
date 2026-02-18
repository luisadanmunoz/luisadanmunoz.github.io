---
title: Azure Automation
area: azure/management
owner: LuisAdan
categories: [Resources, Gestión]
tags:
  - azure
  - automation
  - runbooks
  - powershell
  - python
  - update-management
  - desired-state-configuration
  - dsc
cost: https://azure.microsoft.com/pricing/details/automation/
repo: https://github.com/org/azure-automation-iac
last_review: 2026-02-18
---

## 📋 Características

**Azure Automation** es automation service para runbooks, configuration management, update management. PowerShell, Python, graphical runbooks.

### Pricing

**Process Automation:**
- FREE: 500 minutes/mes
- Paid: $0.002/minute (~$1.44 per 12 hours)

**Configuration Management:**
- Nodes: $6/node/mes (first 5 FREE)
- State Configuration pulls: FREE

**Update Management:**
- Azure VMs: FREE
- Non-Azure VMs: $6/node/mes (first 5 FREE)

**Watcher Tasks:**
- $0.002/minute

**Example:**
```
50 runbooks running 10 min/día each:
50 × 10 × 30 = 15,000 minutes/mes
First 500: FREE
Next 14,500: 14,500 × $0.002 = $29/mes

Update Management (20 on-prem servers):
First 5: FREE
Next 15: 15 × $6 = $90/mes

Total: ~$119/mes
```

---

## 🏆 Best Practices

### Runbook Development
- ✅ **PowerShell 7**: Modern syntax
- ✅ **Python 3**: Cross-platform
- ✅ **Modules**: Import Az modules
- ✅ **Source control**: GitHub/Azure Repos integration
- ✅ **Webhooks**: Trigger from external systems

### Scheduling
- ✅ **One-time**: Future execution
- ✅ **Recurring**: Cron-like schedules
- ✅ **Link to runbook**: Multiple schedules
- ✅ **Time zones**: Respect local time

### State Configuration (DSC)
- ✅ **Desired state**: Configuration as code
- ✅ **Node compliance**: Track drift
- ✅ **Pull mode**: Nodes pull config
- ✅ **Reporting**: Compliance dashboard

### Update Management
- ✅ **Patch compliance**: View update status
- ✅ **Deployment schedules**: Maintenance windows
- ✅ **Pre/post scripts**: Custom actions
- ✅ **Reboot control**: Automatic/manual

### Security
- ✅ **Managed Identity**: No credentials in code
- ✅ **Run As accounts**: Service principal auth
- ✅ **Variables**: Encrypted storage
- ✅ **Credentials**: Secure assets
- ✅ **Certificates**: PKI integration

### Monitoring
- ✅ **Job status**: Success/failed/suspended
- ✅ **Logs**: Output/error streams
- ✅ **Metrics**: Job duration, failures
- ✅ **Alerts**: Failed jobs notification

---

## ⚠️ Limitaciones

- Runbook execution: Max 3 hours (fair share)
- Concurrent jobs: 20-100 (tier dependent)
- Job logs retention: 30 days
- Module size: 100 MB max

---

## ✅ Checklist

- [ ] Automation account created
- [ ] Managed Identity enabled
- [ ] Modules imported (Az, custom)
- [ ] Runbooks created/imported
- [ ] Variables/credentials configured
- [ ] Schedules created
- [ ] Webhooks configured (if needed)
- [ ] State Configuration setup (if needed)
- [ ] Update Management enabled (if needed)
- [ ] Monitoring configured
- [ ] Alerts set (failed jobs)
