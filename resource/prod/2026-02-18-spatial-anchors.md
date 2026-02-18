---
title: Azure Spatial Anchors
area: azure/mixed-reality
owner: LuisAdan
categories: [Resources, Realidad Mixta]
tags:
  - azure
  - spatial-anchors
  - mixed-reality
  - augmented-reality
  - hololens
  - ar-vr
  - spatial-computing
  - cross-platform
cost: https://azure.microsoft.com/pricing/details/spatial-anchors/
repo: https://github.com/org/azure-spatial-anchors-iac
last_review: 2026-02-18
---

## 📋 Características

**Spatial Anchors** es servicio para mixed reality experiences. Anclar contenido virtual a ubicaciones físicas, multi-dispositivo, multi-usuario, persistencia en cloud.

### Pricing

**Anchor operations:**
- FREE: 10,000 anchors stored
- Paid: $0.0005 per anchor stored/mes + $0.003 per query

**Ejemplo:**
```
AR retail app: 1000 anchors, 100k queries/mes
Storage: 1000 × $0.0005 = $0.50
Queries: 100,000 × $0.003 = $300
Total: ~$300.50/mes

vs Build from scratch:
Desarrollo: $50k+
Infraestructura: $1k/mes
Spatial Anchors: 99% más económico
```

---

## 🏆 Best Practices

### Casos de uso
- ✅ **Retail**: Virtual product placement
- ✅ **Manufacturing**: Assembly instructions AR
- ✅ **Education**: Interactive learning
- ✅ **Navigation**: Indoor wayfinding
- ✅ **Gaming**: Location-based AR games
- ✅ **Collaboration**: Shared AR experiences

### Plataformas soportadas
- ✅ **HoloLens**: Microsoft mixed reality
- ✅ **iOS**: ARKit devices
- ✅ **Android**: ARCore devices
- ✅ **Unity**: Game engine
- ✅ **Unreal**: Game engine

### Anchor Creation
- ✅ **Device tracking**: 6DOF positioning
- ✅ **Visual features**: Surface detection
- ✅ **Cloud upload**: Persist in Azure
- ✅ **Expiration**: Set lifetime
- ✅ **Metadata**: Custom properties

### Anchor Discovery
- ✅ **Nearby anchors**: Spatial queries
- ✅ **Anchor identifiers**: Direct lookup
- ✅ **Coarse relocalization**: WiFi/GPS/BLE
- ✅ **Visual scan**: Camera-based

### Multi-user scenarios
- ✅ **Shared experiences**: Ver mismo contenido
- ✅ **Collaboration**: Trabajo conjunto
- ✅ **Real-time sync**: Azure SignalR
- ✅ **Anchor sharing**: ID distribution

### Performance
- ✅ **Local caching**: Reduce queries
- ✅ **Batch operations**: Multiple anchors
- ✅ **Coarse reloc**: Faster discovery
- ✅ **Anchor lifetime**: Delete unused

### Development
- ✅ **SDK**: C#, C++, Java, Objective-C
- ✅ **Unity plugin**: Easy integration
- ✅ **Samples**: GitHub examples
- ✅ **Emulator**: Test without device

---

## ⚠️ Limitaciones

- Device support: ARKit/ARCore/HoloLens only
- Indoor accuracy: ~1-3 metros típico
- Outdoor: GPS coarse relocalization
- Network: Requiere conectividad para cloud
- Tracking: Depende de features visuales

---

## ✅ Checklist

- [ ] Spatial Anchors account creado
- [ ] SDK instalado (Unity/Native)
- [ ] Device capabilities verificadas
- [ ] Anchor creation implementado
- [ ] Cloud upload configurado
- [ ] Anchor discovery implementado
- [ ] Coarse relocalization configurada
- [ ] Multi-user sharing (si aplica)
- [ ] Anchor expiration strategy
- [ ] Testing en dispositivos reales
- [ ] Performance optimizada
- [ ] Monitoring configurado
