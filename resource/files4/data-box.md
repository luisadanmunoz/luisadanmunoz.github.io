# Azure Data Box

## 📋 Características

**Data Box** es servicio de transferencia física de datos a gran escala. Dispositivos físicos para migración offline. Para TB/PB de datos cuando transferencia de red no es práctica.

### Pricing

**Data Box (100 TB utilizable):**
- $300 por transferencia completa (ida + vuelta)
- Incluye: Envío, dispositivo, procesamiento

**Data Box Disk (35 TB total, 5 discos):**
- $200 por orden
- SSD encriptados

**Data Box Heavy (800 TB utilizable):**
- $3,000 por transferencia

**Ejemplo:**
```
Migración 80 TB a Azure:

Opción 1 - Data Box:
Costo: $300 one-time
Tiempo: ~2 semanas (envío + procesamiento)

Opción 2 - Transferencia de red (1 Gbps):
80 TB × 8 bits = 640 Tb
640 Tb ÷ 1 Gbps = 640,000 segundos = ~7.4 días
Costo transferencia: FREE (ingress)
Costo tiempo: Delay en migración

Data Box: Mejor para >10 TB o red limitada
```

---

## 🏆 Best Practices

### Casos de uso
- ✅ **Migración cloud**: On-prem a Azure (one-time)
- ✅ **Backup inicial**: Seed initial backup
- ✅ **Disaster recovery**: Recuperación masiva
- ✅ **Media workflows**: Archivos grandes (video)
- ✅ **Edge collection**: Datos remotos sin conectividad

### Proceso
1. **Pedir**: Azure Portal, orden Data Box
2. **Recibir**: ~5-7 días envío
3. **Copiar**: Conectar, copiar datos (USB 3.1, 1 GbE, 10 GbE)
4. **Devolver**: Enviar de vuelta
5. **Procesamiento**: Azure copia a Storage Account (~1-2 días)
6. **Verificación**: Datos disponibles
7. **Borrado seguro**: Dispositivo limpiado (NIST 800-88)

### Data Box vs Disk vs Heavy
- ✅ **Disk (35 TB)**: <40 TB, $200
- ✅ **Data Box (100 TB)**: 40-500 TB, $300
- ✅ **Heavy (800 TB)**: 500+ TB, $3,000

### Preparación
- ✅ **Inventario**: Listar datos a migrar
- ✅ **Storage Account**: Crear destino
- ✅ **Networking**: Conectividad dispositivo
- ✅ **Shares**: Configurar SMB/NFS shares
- ✅ **Copy tool**: Robocopy, rsync

### Seguridad
- ✅ **Encriptación**: AES 256-bit automático
- ✅ **Unlock key**: Azure Portal
- ✅ **Borrado**: NIST 800-88 compliant
- ✅ **Chain of custody**: Rastreo completo
- ✅ **BitLocker**: Windows encryption

### Optimización
- ✅ **Múltiples hilos**: Copias paralelas
- ✅ **Archivos grandes**: Mejor rendimiento
- ✅ **Organizar**: Por Storage Account/Container
- ✅ **Validación**: Checksums automáticos

---

## ⚠️ Limitaciones

- Tiempo envío: 5-7 días cada dirección
- Disponibilidad: Regiones limitadas
- Tamaño archivo: Max 4.75 TB por archivo
- Procesamiento: 1-2 días en Azure
- No tiempo real: Migración offline

---

## ✅ Checklist

- [ ] Cantidad datos calculada (TB)
- [ ] Dispositivo seleccionado (Disk/Box/Heavy)
- [ ] Orden creada en Azure Portal
- [ ] Storage Account destino creado
- [ ] Dispositivo recibido
- [ ] Red configurada (conectar dispositivo)
- [ ] Unlock key obtenido
- [ ] Datos copiados
- [ ] Validación local completada
- [ ] Dispositivo devuelto
- [ ] Procesamiento Azure completado
- [ ] Datos verificados en Storage
- [ ] Confirmación borrado seguro
