---
title: Azure SQL Managed Instance
area: azure/databases
owner: LuisAdan
categories: [Resources, Bases de Datos]
tags:
  - azure
  - sql-managed-instance
  - paas
  - relational-database
  - sql-server
  - migration
  - hybrid-cloud
  - enterprise-database
cost: https://azure.microsoft.com/pricing/details/azure-sql-managed-instance/
repo: https://github.com/org/azure-sql-managed-instance-iac
last_review: 2026-02-18
---

## 📋 Características

**SQL Managed Instance** es SQL Server totalmente gestionado en Azure. 100% compatibilidad con SQL Server, VNet isolation, fácil migración. PaaS con funcionalidades IaaS.

### Pricing

**General Purpose:**
| vCores | Storage | Precio/hora | Precio/mes (730h) |
|--------|---------|-------------|-------------------|
| 4 vCore | 32 GB-16 TB | ~$0.70 | ~$511 |
| 8 vCore | 32 GB-16 TB | ~$1.40 | ~$1,022 |
| 16 vCore | 32 GB-16 TB | ~$2.80 | ~$2,044 |

**Business Critical:**
| vCores | Storage | Precio/hora | Precio/mes |
|--------|---------|-------------|------------|
| 4 vCore | 32 GB-4 TB | ~$1.82 | ~$1,329 |
| 8 vCore | 32 GB-4 TB | ~$3.64 | ~$2,657 |
| 16 vCore | 32 GB-4 TB | ~$7.28 | ~$5,314 |

**Storage:** $0.115/GB/mes adicional

**Ejemplo:**
```
Producción: Business Critical 8 vCore, 500 GB
Compute: $2,657/mes
Storage: 500 × $0.115 = $57.50
Total: ~$2,715/mes

vs SQL Server on VM (D8s_v3):
VM: $280/mes
SQL License: $1,500/mes
Management: $500/mes
Total: ~$2,280/mes
Managed Instance: 19% más caro pero totalmente gestionado
```

**Reserved Instance (3 años): ~65% descuento**

---

## 🏆 Best Practices

### Casos de uso
- ✅ **Lift and shift**: Migración SQL Server
- ✅ **Modernización**: De on-prem a cloud
- ✅ **Multi-database apps**: Consolidación
- ✅ **ISV applications**: Software vendors
- ✅ **High compatibility**: Near-100% T-SQL

### Service Tiers
- ✅ **General Purpose**: Workloads normales, SSD remoto
- ✅ **Business Critical**: Baja latencia, SSD local, AlwaysOn
- ✅ **Hyperscale**: Preview, hasta 100 TB

### Características SQL Server
- ✅ **SQL Agent**: Jobs programados
- ✅ **CLR**: .NET assemblies
- ✅ **Linked servers**: Conexiones externas
- ✅ **Service Broker**: Mensajería
- ✅ **Database Mail**: Email notifications
- ✅ **Cross-database queries**: Entre bases

### High Availability
- ✅ **Built-in**: 99.99% SLA
- ✅ **AlwaysOn**: Business Critical (3 réplicas)
- ✅ **Auto-failover**: Transparente
- ✅ **Zone redundant**: Multi-AZ
- ✅ **Read replicas**: Business Critical incluidas

### Networking
- ✅ **VNet integration**: Mandatory
- ✅ **Dedicated subnet**: /24 mínimo (recomendado /25)
- ✅ **Private endpoint**: Acceso privado
- ✅ **Public endpoint**: Opcional (disabled default)
- ✅ **DNS**: Private DNS zone

### Migration
- ✅ **Database Migration Service**: Online migration
- ✅ **Backup/restore**: Desde URL
- ✅ **Transactional replication**: Continuous sync
- ✅ **Log replay**: Punto en tiempo
- ✅ **Data Migration Assistant**: Evaluación

### Backup & Recovery
- ✅ **Automated backups**: 7-35 días retention
- ✅ **Long-term retention**: Hasta 10 años
- ✅ **Point-in-time restore**: Cualquier momento
- ✅ **Geo-restore**: Cross-region
- ✅ **Copy-only backups**: Manual backups

---

## ⚠️ Limitaciones

- VNet: Requiere subnet dedicado (/24 mínimo)
- Provisioning: 4-6 horas iniciales
- Scale: Operación puede tardar horas
- Storage: Max 16 TB (GP), 4 TB (BC)
- Databases: Max 100 por instancia

---

## ✅ Checklist

- [ ] VNet y subnet creados (/24 o mayor)
- [ ] NSG configurado
- [ ] Route table configurada
- [ ] SQL Managed Instance creada
- [ ] Service tier seleccionado (GP/BC)
- [ ] vCores dimensionados
- [ ] Public endpoint configurado (si necesario)
- [ ] Databases migradas
- [ ] SQL Agent jobs configurados
- [ ] Backup retention configurado
- [ ] Monitoring habilitado
- [ ] Alerts configuradas
- [ ] Reserved Instance comprada (savings)
