# Azure Site Recovery (ASR)

## 📋 Características

**Site Recovery** es disaster recovery service. VM replication, failover/failback, RPO <15 min, Azure-to-Azure, on-prem-to-Azure.

### Pricing

**Azure-to-Azure:**
- Protected instance: $25/instance/mes
- Cache storage: Standard Storage pricing

**VMware/Physical-to-Azure:**
- Protected instance: $25/instance/mes
- Process server: FREE
- Configuration server: FREE

**Hyper-V-to-Azure:**
- Protected instance: $25/instance/mes

**Replication data transfer:** FREE

**Example:**
```
DR for 20 Azure VMs:
20 × $25 = $500/mes

Cache storage (1 TB): ~$18/mes

Total: ~$518/mes

vs Azure Backup: ~$200/mes
ASR provides: Near-zero RPO, automated failover
```

---

## 🏆 Best Practices

### Azure-to-Azure
- ✅ **Region pairs**: Use paired regions
- ✅ **Availability zones**: Zone-to-zone DR
- ✅ **Recovery Services Vault**: One per target region
- ✅ **Replication policy**: RPO <15 min default

### VMware-to-Azure
- ✅ **Configuration server**: On-prem management
- ✅ **Process server**: Replication gateway
- ✅ **Mobility service**: Agent on VMs
- ✅ **Retention**: 72 hours crash-consistent

### Failover Planning
- ✅ **Recovery plans**: Automated orchestration
- ✅ **Multi-tier apps**: Group VMs
- ✅ **Scripts**: Pre/post failover actions
- ✅ **Network mapping**: VNet to VNet

### Testing
- ✅ **Test failover**: Non-disruptive DR drill
- ✅ **Isolated network**: Test VNet
- ✅ **Cleanup**: Auto or manual
- ✅ **Regular testing**: Quarterly minimum

### Networking
- ✅ **IP retention**: Keep same IPs if possible
- ✅ **Network Security Groups**: Replicate rules
- ✅ **Load balancers**: Recreate in target
- ✅ **ExpressRoute**: DR connectivity

### Monitoring
- ✅ **Replication health**: Green/yellow/red
- ✅ **RPO**: Track <15 min SLA
- ✅ **Test failover success**: Track drills
- ✅ **Failover readiness**: Dashboard

---

## ⚠️ Limitaciones

- Max VMs per vault: 500 (can increase)
- Replication lag: <15 min typical
- Supported OS: Windows, Linux (specific versions)
- Not for: Data backup (use Azure Backup)

---

## ✅ Checklist

- [ ] Recovery Services Vault created (target region)
- [ ] Replication policy configured
- [ ] VMs enabled for replication
- [ ] Replication health verified
- [ ] Network mapping configured
- [ ] Recovery plan created
- [ ] Test failover executed
- [ ] Failover runbook documented
- [ ] Monitoring configured
- [ ] Regular DR drills scheduled
