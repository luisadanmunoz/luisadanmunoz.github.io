# Azure HPC Cache

## 📋 Características

**HPC Cache** es file caching service for high-performance computing. Accelerate file access, aggregate storage, NFS protocol. For rendering, genomics, EDA, simulations.

### Pricing

**Cache throughput tiers:**
| Throughput | Cache Size | Precio/hora | Precio/mes (730h) |
|------------|------------|-------------|-------------------|
| **3 GB/s** | 6-48 TB | ~$1.10 | ~$803 |
| **6 GB/s** | 12-96 TB | ~$2.20 | ~$1,606 |
| **12 GB/s** | 24-192 TB | ~$4.40 | ~$3,212 |

**Storage targets:** Standard Storage pricing

**Example:**
```
HPC workload: 6 GB/s, 24 TB cache
Cache: $1,606/mes
Backend storage (NetApp/Blob): $500-2,000/mes

Total: ~$2,106-3,606/mes

Performance: 6 GB/s throughput vs direct storage ~100 MB/s
Speedup: 60x faster file access
```

---

## 🏆 Best Practices

### Use Cases
- ✅ **VFX rendering**: Frame rendering farms
- ✅ **Genomics**: DNA sequencing pipelines
- ✅ **EDA**: Electronic design automation
- ✅ **Oil & gas**: Seismic processing
- ✅ **Financial**: Risk modeling

### Storage Targets
- ✅ **Azure Blob**: Object storage
- ✅ **NetApp Files**: Enterprise NFS
- ✅ **NFS servers**: On-prem or cloud
- ✅ **Multiple targets**: Aggregate namespaces

### Architecture
- ✅ **Client access**: NFS v3 mount
- ✅ **Namespace**: Virtual file system
- ✅ **Write-back cache**: Buffered writes
- ✅ **Read cache**: Hot data caching
- ✅ **Pre-warming**: Preload data

### Performance
- ✅ **Throughput**: 3-12 GB/s
- ✅ **IOPS**: Hundreds of thousands
- ✅ **Latency**: Sub-millisecond cache hits
- ✅ **Clients**: Thousands concurrent

### Deployment
- ✅ **VNet integration**: Private networking
- ✅ **Subnet**: /24 recommended
- ✅ **DNS**: Configure name resolution
- ✅ **Firewall**: Allow NFS traffic
- ✅ **Compute**: VMSS or HPC clusters

### Monitoring
- ✅ **Cache hit ratio**: Track efficiency
- ✅ **Throughput**: Monitor utilization
- ✅ **Latency**: Client response times
- ✅ **Storage targets**: Health status

---

## ⚠️ Limitaciones

- Protocol: NFS v3 only
- Region availability: Limited regions
- Cache size: Max 192 TB per cache
- Write-back: Risk of data loss (rare)

---

## ✅ Checklist

- [ ] Use case validated (HPC workload)
- [ ] Throughput tier selected (3/6/12 GB/s)
- [ ] Cache size determined
- [ ] VNet/Subnet configured
- [ ] Storage targets identified
- [ ] HPC Cache deployed
- [ ] Storage targets added
- [ ] Namespace configured
- [ ] Client VMs configured (mount)
- [ ] Pre-warming completed (if needed)
- [ ] Performance tested
- [ ] Monitoring enabled
