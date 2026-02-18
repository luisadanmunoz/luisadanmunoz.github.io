---
title: Azure VMware Solution (AVS)
area: azure/compute
owner: LuisAdan
categories: [Resources, Cómputo]
tags:
  - azure
  - vmware
  - avs
  - private-cloud
  - migration
  - hybrid-cloud
  - vsphere
  - nsx
  - vsan
cost: https://azure.microsoft.com/pricing/details/azure-vmware/
repo: https://github.com/org/azure-vmware-solution-iac
last_review: 2026-02-18
---

## 📋 Características

**Azure VMware Solution** es VMware vSphere running natively on Azure. VMware Cloud Foundation (vSphere, vSAN, NSX-T). Migrate or extend VMware workloads.

### Pricing

**Nodes (AV36/AV36P):**
- AV36: 36 cores, 576 GB RAM, 15.36 TB raw storage
- Standard: ~$8.50/hour (~$6,205/node/mes)
- Reserved 1-year: ~$5.50/hour (~$4,015/node/mes) - 35% discount
- Reserved 3-year: ~$4.10/hour (~$2,993/node/mes) - 52% discount

**Minimum:** 3 nodes per cluster

**Example:**
```
Small private cloud (3 nodes, AV36):
Pay-as-you-go: 3 × $6,205 = $18,615/mes
1-year reserved: 3 × $4,015 = $12,045/mes
3-year reserved: 3 × $2,993 = $8,979/mes

Savings: $9,636/mes (52% with 3-year RI)
```

**Additional costs:**
- Outbound data transfer: Standard Azure rates
- Azure services integration: Standard pricing
- HCX migration: Included FREE

---

## 🏆 Best Practices

### Sizing
- ✅ **Minimum 3 nodes**: HA requirement
- ✅ **Scale up to 16**: Per cluster
- ✅ **Multiple clusters**: Workload isolation
- ✅ **Right-size**: Match on-prem capacity

### Networking
- ✅ **ExpressRoute**: Dedicated connection (required)
- ✅ **/22 CIDR**: Management network minimum
- ✅ **NSX-T**: Software-defined networking
- ✅ **Azure VNet**: Hybrid connectivity
- ✅ **Global Reach**: Site-to-site connectivity

### Migration
- ✅ **HCX**: VMware HCX included
- ✅ **vMotion**: Live migration, zero downtime
- ✅ **Bulk migration**: Large-scale moves
- ✅ **Network extension**: L2 stretch
- ✅ **Disaster recovery**: SRM integration

### Integration
- ✅ **Azure services**: Native integration
- ✅ **Backup**: Azure Backup Server, third-party
- ✅ **Monitoring**: Azure Monitor, vROps
- ✅ **NetApp Files**: NFS datastores
- ✅ **Elastic SAN**: iSCSI datastores

### Management
- ✅ **vCenter**: Full administrative access
- ✅ **NSX-T Manager**: Network management
- ✅ **vSAN**: Storage policies
- ✅ **CloudAdmin role**: Azure-managed
- ✅ **Automation**: PowerCLI, Terraform

### DR & Backup
- ✅ **Site Recovery Manager**: VMware SRM
- ✅ **vSphere Replication**: Built-in replication
- ✅ **Azure Site Recovery**: Hybrid DR
- ✅ **Third-party**: Veeam, Commvault
- ✅ **Snapshots**: vSAN snapshots

---

## ⚠️ Limitaciones

- Minimum: 3 nodes required
- Maximum: 16 nodes per cluster
- ExpressRoute: Required for connectivity
- Region availability: Limited regions
- Host access: No ESXi shell access

---

## ✅ Checklist

- [ ] AVS private cloud requested
- [ ] ExpressRoute circuit provisioned
- [ ] Network segments planned (/22 minimum)
- [ ] Nodes sized (3-16)
- [ ] vCenter credentials received
- [ ] NSX-T configured
- [ ] HCX deployed (for migration)
- [ ] Azure VNet peering configured
- [ ] Monitoring enabled
- [ ] Backup solution configured
- [ ] DR plan defined
- [ ] Reserved Instances purchased (cost savings)
