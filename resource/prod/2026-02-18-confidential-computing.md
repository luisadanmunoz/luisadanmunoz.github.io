---
title: Azure Confidential Computing
area: azure/security
owner: LuisAdan
categories: [Resources, Seguridad]
tags:
  - azure
  - confidential-computing
  - tee
  - secure-enclaves
  - data-protection
  - intel-sgx
  - amd-sev
  - zero-trust
cost: https://azure.microsoft.com/pricing/details/virtual-machines/
repo: https://github.com/org/azure-confidential-computing-iac
last_review: 2026-02-18
---

## 📋 Características

**Confidential Computing** protects data in use with hardware-based Trusted Execution Environments (TEEs). Intel SGX, AMD SEV-SNP. Encrypted memory, verifiable execution.

### Pricing

**Confidential VMs (DCsv3/DCdsv3):**
| Size | vCPU | RAM | Precio/hora | Precio/mes |
|------|------|-----|-------------|------------|
| **DC2s_v3** | 2 | 16 GB | ~$0.192 | ~$140 |
| **DC4s_v3** | 4 | 32 GB | ~$0.384 | ~$280 |
| **DC8s_v3** | 8 | 64 GB | ~$0.768 | ~$561 |
| **DC48s_v3** | 48 | 384 GB | ~$4.61 | ~$3,365 |

**Premium ~40% more** than standard VMs (confidentiality protection)

**Confidential Containers (AKS):**
- Standard AKS pricing + confidential node pool

**Example:**
```
Confidential workload: 5 × DC4s_v3 VMs
5 × $280 = $1,400/mes

vs Standard D4s_v3: 5 × $140 = $700/mes
Premium: $700/mes for data-in-use encryption
```

---

## 🏆 Best Practices

### Use Cases
- ✅ **Healthcare**: PHI data processing
- ✅ **Financial**: Fraud detection, trading
- ✅ **Government**: Classified data
- ✅ **Multi-party**: Confidential consortiums
- ✅ **AI/ML**: Protected model training

### VM Types
- ✅ **DCsv3-series**: AMD SEV-SNP (recommended)
- ✅ **DCdsv3-series**: AMD SEV-SNP + local disk
- ✅ **DCsv2-series**: Intel SGX (legacy, limited memory)

### Confidential Containers
- ✅ **AKS**: Confidential node pools
- ✅ **Container Instances**: SGX-enabled
- ✅ **Enclaves**: Intel SGX enclaves
- ✅ **Attestation**: Verify TEE integrity

### Application Development
- ✅ **Lift-and-shift**: No code changes (SEV-SNP)
- ✅ **Enclave-aware**: Intel SGX apps
- ✅ **Open Enclave SDK**: Cross-platform
- ✅ **Confidential Consortium Framework**: Multi-party apps

### Attestation
- ✅ **Azure Attestation**: Verify TEE
- ✅ **Remote attestation**: Prove security
- ✅ **Policies**: Define trust boundaries
- ✅ **Certificates**: Attestation tokens

### Encryption
- ✅ **Memory encryption**: Hardware-based
- ✅ **Disk encryption**: OS and data disks
- ✅ **Network encryption**: TLS/IPSec
- ✅ **Key management**: Key Vault integration

---

## ⚠️ Limitaciones

- Cost premium: ~40% more than standard VMs
- DCsv2: Limited enclave memory (Intel SGX)
- Performance: Slight overhead for encryption
- Regional availability: Limited regions
- OS support: Ubuntu, Windows Server

---

## ✅ Checklist

- [ ] Use case validated (data-in-use protection)
- [ ] VM size selected (DCsv3 recommended)
- [ ] OS image selected (Ubuntu/Windows)
- [ ] VM deployed
- [ ] Attestation configured
- [ ] Application deployed
- [ ] Key Vault integration
- [ ] Disk encryption enabled
- [ ] Network security configured
- [ ] Monitoring enabled
- [ ] Compliance requirements validated
- [ ] Performance tested
