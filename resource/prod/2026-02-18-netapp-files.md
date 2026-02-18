---
title: Azure NetApp Files
area: azure/storage
owner: LuisAdan
categories: [Resources, Almacenamiento]
tags:
  - azure
  - netapp-files
  - storage
  - nfs
  - smb
  - high-performance
  - enterprise-storage
  - file-shares
cost: https://azure.microsoft.com/pricing/details/netapp/
repo: https://github.com/org/azure-netapp-files-iac
last_review: 2026-02-18
---

## 📋 Características

**NetApp Files** es enterprise-grade NFS/SMB file storage. High-performance, sub-ms latency, snapshots, replication. For SAP, databases, HPC.

### Pricing Tiers

| Service Level | Performance | Precio/GB/mes |
|---------------|-------------|---------------|
| **Standard** | 16 MiB/s per TB | ~$0.000403/GB/hour (~$0.29/GB/mes) |
| **Premium** | 64 MiB/s per TB | ~$0.000807/GB/hour (~$0.59/GB/mes) |
| **Ultra** | 128 MiB/s per TB | ~$0.001210/GB/hour (~$0.88/GB/mes) |

**Minimum:** 4 TiB capacity pool

**Example:**
```
Premium tier, 10 TiB:
10 × 1024 × $0.59 = $6,042/mes

Performance: 10 TB × 64 MiB/s = 640 MiB/s
```

**Snapshots:** FREE (consume capacity)
**Cross-region replication:** Data transfer costs

---

## 🏆 Best Practices

### Use Cases
- ✅ **SAP HANA**: Certified for production
- ✅ **Oracle**: Database workloads
- ✅ **SQL Server**: High IOPS needs
- ✅ **HPC**: Parallel file systems
- ✅ **VDI**: FSLogix profiles (AVD)

### Performance
- ✅ **Service level**: Match workload requirements
- ✅ **Volume quota**: Determines throughput
- ✅ **Standard network features**: Default
- ✅ **Large volumes**: Better performance

### Data Protection
- ✅ **Snapshots**: Up to 255 per volume
- ✅ **Snapshot policy**: Automated schedules
- ✅ **Cross-region replication**: DR
- ✅ **Backup**: Azure NetApp Files backup

### Networking
- ✅ **Delegated subnet**: Dedicated /26+
- ✅ **VNet integration**: Private connectivity
- ✅ **NFSv3/NFSv4.1**: Protocol support
- ✅ **SMB**: Windows workloads

### Cost Optimization
- ✅ **Cool access**: Inactive data to blob storage
- ✅ **Right-size volumes**: Match actual usage
- ✅ **Standard tier**: Non-critical workloads
- ✅ **Capacity pool**: Shared across volumes

---

## ⚠️ Limitaciones

- Minimum capacity pool: 4 TiB
- Minimum volume: 100 GiB
- Regional service: Not all regions
- Capacity pool max: 500 TiB
- Snapshots: Max 255 per volume

---

## ✅ Checklist

- [ ] NetApp account created
- [ ] Capacity pool created (4 TiB minimum)
- [ ] Service level selected
- [ ] Delegated subnet configured
- [ ] Volume created
- [ ] Protocol configured (NFS/SMB)
- [ ] Mounted to workload
- [ ] Snapshot policy configured
- [ ] Backup enabled
- [ ] Monitoring configured
