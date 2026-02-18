# Azure Virtual Desktop (AVD)

## 📋 Características

**Azure Virtual Desktop** es desktop and app virtualization service. Windows 10/11 multi-session, FSLogix, no additional licensing for M365 E3+.

### Pricing

**Service:** FREE (no AVD license cost)

**Costs:**
- VMs: Standard Azure VM pricing
- Storage: Profile storage (FSLogix)
- Networking: Bandwidth

**VM Examples (per user, 8h/day):**
| Size | vCPU | RAM | Monthly Cost |
|------|------|-----|--------------|
| B2s | 2 | 4GB | ~$30 (light users) |
| D2s_v5 | 2 | 8GB | ~$56 (standard) |
| D4s_v5 | 4 | 16GB | ~$112 (power users) |

**Multi-session Windows 10/11:**
- 2-10 users per VM typical
- Cost per user: $5-15/user/mes

**Example:**
```
50 users, Windows 11 multi-session:
10 × D4s_v5 VMs (5 users each), 8h/day:
10 × $0.192/hour × 240 hours = $460.80/mes
Per user: ~$9.22/mes
```

---

## 🏆 Best Practices

### Host Pool Design
- ✅ **Pooled**: Multi-session, cost-effective
- ✅ **Personal**: Dedicated VMs, persistent
- ✅ **Depth-first**: Load balancing
- ✅ **Breadth-first**: Distribute load

### Scaling
- ✅ **Autoscale**: Start/stop VMs based on demand
- ✅ **Peak hours**: Scale up
- ✅ **Off-hours**: Scale down/deallocate
- ✅ **Start VM on Connect**: Zero VMs when idle

### Profile Management
- ✅ **FSLogix**: Profile containers
- ✅ **Azure Files**: Premium recommended
- ✅ **Cloud Cache**: Local + cloud storage
- ✅ **Profile size**: Monitor and limit

### Performance
- ✅ **Accelerated Networking**: Enable on VMs
- ✅ **Proximity Placement Groups**: Low latency
- ✅ **Premium SSD**: OS and profile disks
- ✅ **GPU**: For graphics workloads

### Security
- ✅ **MFA**: Azure AD Conditional Access
- ✅ **RDP Shortpath**: Direct UDP connection
- ✅ **Screen capture protection**: Prevent recording
- ✅ **Watermarking**: Session watermarks

### Monitoring
- ✅ **Insights**: Built-in monitoring
- ✅ **Log Analytics**: Detailed logs
- ✅ **Connection quality**: Latency, bandwidth
- ✅ **User experience**: Performance metrics

---

## ⚠️ Limitaciones

- Windows licensing: M365 E3+ or per-user license
- Multi-session: Windows 10/11 Enterprise only
- Max users per VM: Depends on workload
- GPU: Limited VM families

---

## ✅ Checklist

- [ ] Host pool created
- [ ] VMs deployed (pooled/personal)
- [ ] FSLogix configured
- [ ] Azure Files created (profiles)
- [ ] Applications published
- [ ] Users assigned
- [ ] Autoscale configured
- [ ] MFA enabled
- [ ] Monitoring configured
- [ ] Connection tested
