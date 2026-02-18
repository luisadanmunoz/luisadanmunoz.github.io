# Azure Queue Storage

## 📋 Características

**Queue Storage** es servicio de mensajería simple para comunicación asíncrona. Colas FIFO, millones de mensajes, integración HTTP/HTTPS. Más simple que Service Bus.

### Pricing

**Operaciones:**
- $0.05 per millón de operaciones (Class 1: write)
- $0.004 per millón de operaciones (Class 2: read/delete)

**Almacenamiento:**
- LRS: $0.045/GB/mes
- GRS: $0.056/GB/mes

**Ejemplo:**
```
10M mensajes/mes (20M operaciones total):
Write: 10M × $0.05/million = $0.50
Read/Delete: 10M × $0.004/million = $0.04
Storage (1 GB promedio): $0.045
Total: ~$0.59/mes

vs Service Bus Basic: $0.05/million = $0.50
Queue Storage: Más económico para casos simples
```

---

## 🏆 Best Practices

### Casos de uso
- ✅ **Desacoplamiento**: Separar componentes
- ✅ **Load leveling**: Suavizar picos de carga
- ✅ **Procesamiento asíncrono**: Tareas en background
- ✅ **Buffering**: Cola de trabajo
- ✅ **Message passing**: Comunicación simple

### Operaciones
- ✅ **Put message**: Añadir a cola (64 KB max)
- ✅ **Get messages**: Leer sin eliminar (invisible 30 sec)
- ✅ **Peek messages**: Ver sin marcar
- ✅ **Delete message**: Eliminar después de procesar
- ✅ **Update message**: Modificar contenido/visibility

### Configuración
- ✅ **Visibility timeout**: 30 segundos default (configurable)
- ✅ **Time-to-live**: 7 días default (máx infinito)
- ✅ **Message size**: Máximo 64 KB
- ✅ **Queue metadata**: Custom properties
- ✅ **CORS**: Cross-origin access

### Escalabilidad
- ✅ **Throughput**: ~2,000 msg/sec por cola
- ✅ **Tamaño**: Hasta 500 TB (límite Storage Account)
- ✅ **Número mensajes**: Ilimitado (dentro de 500 TB)
- ✅ **Múltiples consumidores**: Competencia por mensajes

### Confiabilidad
- ✅ **At-least-once delivery**: Puede haber duplicados
- ✅ **Poison message**: Mover a cola de errores
- ✅ **Dequeue count**: Rastrear intentos
- ✅ **Dead letter**: Implementación manual

### Monitoreo
- ✅ **Queue length**: Número de mensajes
- ✅ **Approximate message count**: Métricas
- ✅ **Diagnostic logs**: Storage Analytics
- ✅ **Alerts**: Cola creciendo mucho

---

## ⚠️ Limitaciones

- Tamaño mensaje: Max 64 KB
- Ordenamiento: FIFO aproximado (no garantizado estricto)
- Transacciones: No soporta transacciones
- TTL: Máximo infinito (pero recomendado 7 días)
- Throughput: ~2k msg/sec por cola

---

## ✅ Checklist

- [ ] Storage Account creado
- [ ] Cola creada
- [ ] Visibility timeout configurado
- [ ] Time-to-live definido
- [ ] SAS token o connection string configurado
- [ ] Cliente implementado (SDK)
- [ ] Manejo de poison messages
- [ ] Retry policy configurado
- [ ] Monitoring habilitado
- [ ] Alertas configuradas (queue length)
- [ ] Escalado planificado
