# Azure Orbital

## 📋 Características

**Azure Orbital** es ground station as a service. Comunicación con satélites desde Azure. Procesar datos satelitales directamente en cloud. Para Earth observation, communications, IoT.

### Pricing

**Contact time:**
- VHF/UHF: ~$3-5/minuto
- S-band: ~$5-10/minuto  
- X-band: ~$10-15/minuto

**Data egress:** Standard Azure rates

**Ejemplo:**
```
LEO satellite: 10 min pass, X-band
Contact: 10 × $12 = $120 por pass

4 passes/día × 30 días = 120 passes/mes
120 × $120 = $14,400/mes

vs Ground station tradicional:
Construcción: $500k-2M
Operación: $50k-100k/mes
Orbital: 70-85% más económico
```

---

## 🏆 Best Practices

### Casos de uso
- ✅ **Earth observation**: Imagery satelital
- ✅ **Weather**: Datos meteorológicos
- ✅ **IoT**: Conectividad IoT global
- ✅ **Communications**: Satcom
- ✅ **Research**: Proyectos científicos

### Bandas de frecuencia
- ✅ **VHF/UHF**: Baja velocidad, larga distancia
- ✅ **S-band**: Telemetry, tracking, command
- ✅ **X-band**: Alta velocidad, downlink ciencia
- ✅ **Ka-band**: Muy alta velocidad (futuro)

### Ground Stations
- ✅ **Global network**: Múltiples ubicaciones
- ✅ **Antenna selection**: Por banda
- ✅ **Scheduling**: Reservar contact windows
- ✅ **Redundancy**: Múltiples sites

### Processing Pipeline
- ✅ **Ingest**: Datos directamente a Azure
- ✅ **Storage**: Blob Storage, Data Lake
- ✅ **Processing**: VMs, Functions, Batch
- ✅ **Analytics**: Synapse, Databricks
- ✅ **Distribution**: CDN, API Management

### Integration
- ✅ **Event Grid**: Notificaciones
- ✅ **Functions**: Procesamiento automático
- ✅ **Storage**: Direct write
- ✅ **Machine Learning**: Análisis AI
- ✅ **Power BI**: Visualización

### Scheduling
- ✅ **Contact profiles**: Configuración frecuencia
- ✅ **TLE updates**: Orbital elements
- ✅ **Automated scheduling**: Reservation automation
- ✅ **Priority contacts**: Contactos críticos

---

## ⚠️ Limitaciones

- Regional: Ground stations en ubicaciones específicas
- Frequency bands: No todas disponibles en todos sites
- Availability: Competencia por tiempo antena
- Latency: Depende de ubicación station
- Approval: Puede requerir licenses regulatorias

---

## ✅ Checklist

- [ ] Spacecraft registered
- [ ] Orbital parameters (TLE) uploaded
- [ ] Frequency authorization obtenida
- [ ] Contact profile configurado
- [ ] Ground station seleccionada
- [ ] Contact window scheduled
- [ ] Data pipeline configurado
- [ ] Storage Account preparado
- [ ] Processing workflow definido
- [ ] Primer contact ejecutado
- [ ] Data validated
- [ ] Monitoring configurado
