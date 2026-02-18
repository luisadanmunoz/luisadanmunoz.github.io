# Azure DDoS Protection

## 📋 Características

**DDoS Protection** protege contra distributed denial-of-service attacks. Layer 3-4 protection, auto-mitigation, always-on monitoring.

### Pricing Tiers

| Tier | Coverage | Pricing |
|------|----------|---------|
| **Basic** | Automatic, free | $0 (included with Azure) |
| **Standard** | Enhanced, policy tuning | $2,944/mes + $0.295 per million packets |

**Standard protects:** 100 public IPs included

**Example:**
```
Standard plan: $2,944/mes
5 VNets with public IPs: Included
50 million packets/mes: 50 × $0.295 = $14.75

Total: ~$2,959/mes
```

**Cost protection:** Up to $50k credit for scaling costs during attack

---

## 🏆 Best Practices

### Basic Protection
- ✅ **Always-on**: Automatic for all Azure resources
- ✅ **Traffic monitoring**: Baseline learning
- ✅ **Auto-mitigation**: Volumetric attacks
- ✅ **No configuration**: Zero-touch

### Standard Protection
- ✅ **Policy tuning**: Custom thresholds
- ✅ **Attack analytics**: Detailed reports
- ✅ **Metrics**: Real-time telemetry
- ✅ **DDoS Rapid Response**: 24/7 support during attack

### Architecture
- ✅ **VNet-level**: Protect all resources in VNet
- ✅ **Public IPs**: Assigned resources protected
- ✅ **Azure Firewall**: Integrated protection
- ✅ **Application Gateway**: WAF + DDoS

### Monitoring
- ✅ **Metrics**: Packets dropped, forwarded
- ✅ **Alerts**: Attack detected/mitigated
- ✅ **Diagnostic logs**: Attack details
- ✅ **Attack analytics**: Post-attack report

### Response
- ✅ **Automatic**: No manual intervention
- ✅ **Traffic scrubbing**: Filter malicious
- ✅ **DDoS Rapid Response**: Engage during attack
- ✅ **Cost protection**: Scale with confidence

---

## ⚠️ Limitaciones

- Standard: Per-VNet pricing (can add up)
- Basic: Limited tuning options
- Protection scope: L3/L4 only (not L7 app attacks)
- Response time: <5 minutes typical

---

## ✅ Checklist

- [ ] Protection tier selected (Basic/Standard)
- [ ] DDoS plan created (Standard)
- [ ] VNets associated
- [ ] Alerts configured
- [ ] Diagnostic logs enabled
- [ ] Monitoring dashboard created
- [ ] Response plan documented
- [ ] DDoS Rapid Response contact saved
- [ ] Cost protection understood
- [ ] Testing plan (optional simulation)
