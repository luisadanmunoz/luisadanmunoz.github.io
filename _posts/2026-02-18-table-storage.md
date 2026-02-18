---
title: Azure Table Storage
area: azure/storage
owner: LuisAdan
categories: [Resources, Almacenamiento]
tags:
  - azure
  - table-storage
  - nosql
  - key-value
  - structured-data
  - scalable-storage
  - storage
  - schemaless
cost: https://azure.microsoft.com/pricing/details/storage/tables/
repo: https://github.com/org/azure-table-storage-iac
last_review: 2026-02-18
---

## 📋 Características

**Table Storage** es NoSQL key-value store. Schema-less, rápido, económico. Para datos semi-estructurados, telemetría, logs.

### Pricing

**Operaciones:**
- $0.05 per millón de transacciones

**Almacenamiento:**
- LRS: $0.045/GB/mes
- GRS: $0.056/GB/mes

**Ejemplo:**
```
100 GB datos, 50M operaciones/mes:
Storage: 100 × $0.045 = $4.50
Transacciones: 50 × $0.05 = $2.50
Total: ~$7/mes

vs Cosmos DB Table API (100 RU/s):
~$24/mes
Table Storage: 70% más económico
```

---

## 🏆 Best Practices

### Casos de uso
- ✅ **Logs/telemetría**: Almacenar millones de eventos
- ✅ **Datos semi-estructurados**: Flexible schema
- ✅ **User data**: Perfiles, configuraciones
- ✅ **Metadata**: Índices, catálogos
- ✅ **IoT device data**: Estado de dispositivos

### Modelado de datos
- ✅ **Partition Key**: Distribución y consultas
- ✅ **Row Key**: Identificador único dentro de partición
- ✅ **Timestamp**: Automático, versionado
- ✅ **Propiedades**: Máximo 255 por entidad
- ✅ **Tamaño entidad**: Máximo 1 MB

### Particionamiento
- ✅ **Estrategia**: Balance entre queries y distribución
- ✅ **Hot partitions**: Evitar concentración
- ✅ **Compound keys**: PartitionKey + RowKey
- ✅ **Time-based**: Año-mes-día para series temporales
- ✅ **Hash distribution**: Para distribución uniforme

### Consultas
- ✅ **Point query**: PartitionKey + RowKey (más rápido)
- ✅ **Range query**: PartitionKey + rango RowKey
- ✅ **Table scan**: Evitar (muy lento)
- ✅ **Filters**: $filter OData
- ✅ **Projection**: $select para campos específicos

### Performance
- ✅ **Batch operations**: Hasta 100 ops (mismo PartitionKey)
- ✅ **Parallel queries**: Múltiples particiones
- ✅ **Paging**: Continuation tokens
- ✅ **Caching**: Client-side cache
- ✅ **Throughput**: ~20,000 entidades/seg por partición

### Seguridad
- ✅ **SAS tokens**: Acceso delegado
- ✅ **Shared Key**: Account key
- ✅ **HTTPS**: Siempre usar TLS
- ✅ **Private Endpoint**: Acceso privado
- ✅ **RBAC**: Control de acceso

---

## ⚠️ Limitaciones

- Tamaño entidad: Max 1 MB
- Propiedades: Max 255 por entidad
- Transacciones: Max 100 ops en batch (mismo PartitionKey)
- Consultas complejas: Sin JOINs, GROUP BY
- Índices: Solo PartitionKey + RowKey

---

## ✅ Checklist

- [ ] Storage Account creado
- [ ] Tabla creada
- [ ] Estrategia de particionamiento definida
- [ ] PartitionKey + RowKey diseñados
- [ ] Datos cargados
- [ ] Consultas optimizadas (point/range)
- [ ] Batch operations implementadas
- [ ] SAS tokens configurados
- [ ] Monitoring habilitado
- [ ] Backup strategy definida
- [ ] Escalado planificado
