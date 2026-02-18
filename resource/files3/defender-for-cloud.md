# Microsoft Defender for Cloud

## 📋 Características

**Defender for Cloud** es cloud security posture management (CSPM) + workload protection. Formerly Azure Security Center + Azure Defender. Multi-cloud support (Azure, AWS, GCP).

### Pricing

**Foundational CSPM:** FREE
- Secure score
- Security recommendations
- Azure Policy integration

**Defender CSPM:** $5/resource/mes
- Attack path analysis
- Cloud security graph
- Agentless scanning

**Workload Protection Plans:**
| Plan | Coverage | Precio/recurso/mes |
|------|----------|-------------------|
| **Servers** | VMs, Arc servers | $15/server |
| **App Service** | Web apps | $15/instance |
| **SQL** | Databases | $15/server |
| **Storage** | Storage accounts | $10/account |
| **Containers** | AKS, ACR | $7/vCore |
| **Key Vault** | Key vaults | $0.20/vault |
| **Resource Manager** | Subscription | $5/subscription |
| **DNS** | DNS zones | $0.40/million queries |

**Example:**
```
50 VMs + 10 App Service + 5 SQL:
Servers: 50 × $15 = $750
App Service: 10 × $15 = $150
SQL: 5 × $15 = $75
CSPM: FREE
Total: ~$975/mes
```

---

## 🏆 Best Practices

### CSPM (Free)
- ✅ **Secure Score**: Track security posture (0-100%)
- ✅ **Recommendations**: Prioritized fixes
- ✅ **Compliance**: PCI-DSS, ISO 27001, NIST
- ✅ **Azure Policy**: Automatic enforcement

### Defender CSPM
- ✅ **Attack paths**: Multi-step attack scenarios
- ✅ **Cloud security graph**: Asset relationships
- ✅ **Agentless scanning**: VM vulnerability assessment
- ✅ **Code scanning**: DevOps integration

### Workload Protection
- ✅ **Just-in-Time VM access**: Reduce attack surface
- ✅ **Adaptive application controls**: Whitelist apps
- ✅ **File integrity monitoring**: Detect changes
- ✅ **Network map**: Visualize topology
- ✅ **Threat protection**: Real-time alerts

### Multi-cloud
- ✅ **AWS connector**: Protect EC2, RDS
- ✅ **GCP connector**: Protect Compute, SQL
- ✅ **Hybrid**: Arc-enabled servers
- ✅ **Unified view**: Single dashboard

### DevSecOps
- ✅ **Defender for DevOps**: GitHub, Azure DevOps
- ✅ **IaC scanning**: Terraform, ARM, Bicep
- ✅ **Container scanning**: Image vulnerabilities
- ✅ **Secrets detection**: Exposed credentials

### Integration
- ✅ **Sentinel**: SIEM integration
- ✅ **Logic Apps**: Automated response
- ✅ **Email/SMS**: Alert notifications
- ✅ **Webhooks**: Custom integrations

---

## ⚠️ Limitaciones

- Free tier: Basic recommendations only
- Defender plans: Per-resource pricing
- Multi-cloud: Requires connectors
- Alert volume: Can be high initially

---

## ✅ Checklist

- [ ] Defender for Cloud enabled
- [ ] Secure Score reviewed
- [ ] Recommendations prioritized
- [ ] Defender plans enabled (Servers, SQL, etc.)
- [ ] JIT VM access configured
- [ ] Adaptive application controls enabled
- [ ] File integrity monitoring enabled
- [ ] Workflow automation configured
- [ ] Multi-cloud connectors (if needed)
- [ ] DevOps integration (if needed)
- [ ] Alerts configured
- [ ] Compliance dashboards reviewed
