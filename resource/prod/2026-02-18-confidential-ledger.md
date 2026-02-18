---
title: Azure Confidential Ledger
area: azure/security
owner: LuisAdan
categories: [Resources, Seguridad]
tags:
  - azure
  - confidential-ledger
  - blockchain
  - tamper-proof
  - immutable-records
  - data-integrity
  - confidential-computing
  - audit-trail
cost: https://azure.microsoft.com/pricing/details/azure-confidential-ledger/
repo: https://github.com/org/azure-confidential-ledger-iac
last_review: 2026-02-18
---

## 📋 Características

**Confidential Ledger** es blockchain-inspired tamper-proof ledger. Basado en Confidential Consortium Framework (CCF). Append-only, cryptographic proof, TEE-protected.

### Pricing

**Operaciones:**
- Write: $0.30 per 10,000 transacciones
- Read: $0.02 per 10,000 transacciones

**Storage:** Incluido en operaciones de escritura

**Ejemplo:**
```
100k transacciones/mes (write), 500k lecturas:
Write: 10 × $0.30 = $3.00
Read: 50 × $0.02 = $1.00
Total: ~$4/mes

Blockchain tradicional: $500-5,000/mes
Confidential Ledger: 99% más económico
```

---

## 🏆 Best Practices

### Casos de uso
- ✅ **Audit trails**: Registros inmutables
- ✅ **Supply chain**: Trazabilidad productos
- ✅ **Healthcare**: Registros médicos
- ✅ **Financial**: Transacciones financieras
- ✅ **Legal**: Contratos, evidencia digital
- ✅ **IoT**: Histórico de sensores

### Propiedades
- ✅ **Append-only**: No se puede modificar/borrar
- ✅ **Tamper-proof**: Cryptographic evidence
- ✅ **Confidential**: TEE-protected (SGX)
- ✅ **Consensus**: Byzantine fault-tolerant
- ✅ **Cryptographic proof**: Merkle trees

### Operaciones
- ✅ **Append**: Añadir entrada
- ✅ **Read**: Leer entrada específica
- ✅ **Range query**: Leer rango
- ✅ **Receipt**: Prueba criptográfica
- ✅ **Verify**: Validar integridad

### Usuarios y roles
- ✅ **Administrator**: Gestión ledger
- ✅ **Contributor**: Escribir entradas
- ✅ **Reader**: Solo lectura
- ✅ **Certificate-based**: PKI authentication
- ✅ **Azure AD**: Integración identidad

### Receipts y verificación
- ✅ **Transaction receipt**: Por cada write
- ✅ **Merkle proof**: Cryptographic evidence
- ✅ **External verification**: Sin depender de Azure
- ✅ **Attestation**: TEE verification

### Integration
- ✅ **REST API**: HTTP endpoints
- ✅ **SDK**: Python, JavaScript, .NET
- ✅ **Event Grid**: Notificaciones
- ✅ **Logic Apps**: Workflow automation

---

## ⚠️ Limitaciones

- Throughput: ~1,000 TPS típico
- Eliminación: No se puede borrar datos
- Modificación: Append-only (no updates)
- Consultas: Limitadas a range queries
- Regional: Disponibilidad limitada

---

## ✅ Checklist

- [ ] Caso de uso validado (inmutabilidad requerida)
- [ ] Confidential Ledger creado
- [ ] Usuarios/roles configurados
- [ ] Certificados emitidos (PKI)
- [ ] Azure AD integration (opcional)
- [ ] Aplicación integrada (SDK)
- [ ] Primera transacción escrita
- [ ] Receipt obtenido y verificado
- [ ] Verificación externa probada
- [ ] Monitoring configurado
- [ ] Backup strategy (receipts)
- [ ] Compliance requirements validados
