---
title: Azure Chaos Studio
area: azure/reliability
owner: LuisAdan
categories: [Resources, Confiabilidad]
tags:
  - azure
  - chaos-studio
  - chaos-engineering
  - resilience
  - fault-injection
  - site-reliability
  - testing
cost: https://azure.microsoft.com/pricing/details/chaos-studio/
repo: https://github.com/org/azure-chaos-studio-iac
last_review: 2026-02-18
---

## 📋 Características

**Chaos Studio** es managed chaos engineering service. Inject faults, test resilience, validate disaster recovery. Controlled experiments.

### Pricing

**Experiment runs:** FREE
**Agent-based faults:** $0.001/agent-minute

**Example:**
```
Agent-based fault on 5 VMs, 30 minutes:
5 × 30 × $0.001 = $0.15 per experiment

Monthly resilience testing (4 experiments):
4 × $0.15 = $0.60/mes
```

**Service-direct faults:** FREE (no agents)

---

## 🏆 Best Practices

### Fault Types

**Service-direct (agentless):**
- ✅ Stop VM
- ✅ Restart VM
- ✅ Kill AKS pods
- ✅ Add network latency
- ✅ Throttle disk I/O

**Agent-based:**
- ✅ CPU pressure
- ✅ Memory pressure
- ✅ Kill process
- ✅ Network disconnect
- ✅ DNS failure

### Experiment Design
- ✅ **Hypothesis**: Define expected behavior
- ✅ **Steady state**: Baseline metrics
- ✅ **Blast radius**: Limit scope
- ✅ **Observability**: Monitor impact

### Safety
- ✅ **Production readiness**: Test in non-prod first
- ✅ **Change management**: Communicate tests
- ✅ **Rollback plan**: Stop experiments quickly
- ✅ **Business hours**: Avoid peak times initially

### Integration
- ✅ **Azure Monitor**: Track metrics during tests
- ✅ **Application Insights**: Application impact
- ✅ **Alerts**: Notify on unexpected behavior
- ✅ **CI/CD**: Automate resilience testing

### Common Scenarios
- ✅ **VM failure**: Stop VMs, validate failover
- ✅ **Network issues**: Latency, packet loss
- ✅ **Resource exhaustion**: CPU/memory pressure
- ✅ **Zone failure**: Multi-zone resilience
- ✅ **Dependency failure**: External service outage

---

## ⚠️ Limitaciones

- Agent installation: Required for agent-based faults
- Target resources: Must be enabled for Chaos
- Concurrent experiments: Limited per subscription
- Fault duration: Max 12 hours

---

## ✅ Checklist

- [ ] Chaos Studio enabled
- [ ] Targets onboarded
- [ ] Agent installed (if needed)
- [ ] Experiment designed
- [ ] Hypothesis documented
- [ ] Monitoring configured
- [ ] Safety measures in place
- [ ] Experiment executed
- [ ] Results analyzed
- [ ] Improvements identified
