# Azure Kubernetes Fleet Manager

## 📋 Características

**Kubernetes Fleet Manager** es multi-cluster orchestration for AKS. Manage multiple clusters, centralized updates, application deployment at scale.

### Pricing

✅ **Fleet resource:** FREE - No charge for fleet management

**Member clusters:** Standard AKS pricing per cluster

**Example:**
```
Fleet with 10 AKS clusters:
Fleet manager: $0
10 clusters @ $210/cluster = $2,100/mes

vs Manual management: Same cost but centralized control
```

---

## 🏆 Best Practices

### Fleet Architecture
- ✅ **Hub cluster**: Central management (optional)
- ✅ **Member clusters**: AKS clusters in fleet
- ✅ **Multi-region**: Clusters across regions
- ✅ **Multi-subscription**: Cross-subscription support

### Update Management
- ✅ **Update runs**: Orchestrated upgrades
- ✅ **Update stages**: Group clusters
- ✅ **Wait times**: Soak periods between stages
- ✅ **Auto-upgrade**: Scheduled updates
- ✅ **Node image upgrades**: OS patching

### Application Deployment
- ✅ **ClusterResourcePlacement**: Deploy to multiple clusters
- ✅ **Label selectors**: Target specific clusters
- ✅ **Namespace propagation**: Consistent namespaces
- ✅ **ConfigMaps/Secrets**: Replicate configuration

### Resource Propagation
- ✅ **Namespace**: Create across fleet
- ✅ **ConfigMap**: Distribute configuration
- ✅ **Secret**: Secure credential distribution
- ✅ **Custom resources**: Fleet-wide CRDs

### Scheduling
- ✅ **Cluster selectors**: Choose target clusters
- ✅ **Affinity**: Prefer specific clusters
- ✅ **Resource availability**: Based on capacity
- ✅ **Topology spread**: Geographic distribution

### Monitoring
- ✅ **Fleet status**: Overall health
- ✅ **Update progress**: Track rollouts
- ✅ **Member cluster health**: Individual status
- ✅ **Azure Monitor**: Centralized metrics

---

## ⚠️ Limitaciones

- Preview: Feature still evolving
- Member clusters: Must be AKS
- Region: Fleet and members same region initially
- Max clusters: Soft limit (~100 clusters)

---

## ✅ Checklist

- [ ] Fleet resource created
- [ ] Member AKS clusters created
- [ ] Clusters joined to fleet
- [ ] Update stages defined
- [ ] Update run configured
- [ ] Namespace propagation configured
- [ ] ClusterResourcePlacement created
- [ ] Application deployed to fleet
- [ ] Monitoring configured
- [ ] Update schedule defined
- [ ] Disaster recovery plan
