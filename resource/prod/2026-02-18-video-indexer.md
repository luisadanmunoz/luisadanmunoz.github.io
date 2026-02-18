---
title: Azure Video Indexer
area: azure/ai
owner: LuisAdan
categories: [Resources, Inteligencia Artificial]
tags:
  - azure
  - video-indexer
  - media-ai
  - video-analytics
  - speech-to-text
  - face-detection
  - content-moderation
  - ai
cost: https://azure.microsoft.com/pricing/details/video-indexer/
repo: https://github.com/org/azure-video-indexer-iac
last_review: 2026-02-18
---

## 📋 Características

**Video Indexer** es servicio de análisis de video con AI. Extrae insights automáticos: transcripción, faces, sentimientos, temas, marcas. Basado en Cognitive Services.

### Pricing

**Standard account:**
- Video indexing: $0.12/minuto video
- Audio indexing: $0.03/minuto audio

**Advanced features:**
- Face detection: Incluido
- Person detection: Incluido  
- Emotion detection: Incluido
- Transcription: Incluido
- Translation: $0.015/minuto adicional

**Ejemplo:**
```
100 horas video/mes:
100 × 60 = 6,000 minutos
6,000 × $0.12 = $720/mes

Con translation:
6,000 × $0.015 = $90 adicional
Total: ~$810/mes

Manual transcription: ~$1/minuto = $6,000
Video Indexer: 90% más económico + AI insights
```

---

## 🏆 Best Practices

### Casos de uso
- ✅ **Media & entertainment**: Catalogar contenido
- ✅ **E-learning**: Buscar dentro de videos
- ✅ **Corporate**: Reuniones, entrenamientos
- ✅ **Compliance**: Revisar contenido
- ✅ **Accessibility**: Subtítulos automáticos

### Insights extraídos
- ✅ **Speech**: Transcripción, idioma
- ✅ **Faces**: Detección, reconocimiento
- ✅ **Emotions**: Sentimientos detectados
- ✅ **Topics**: Temas principales
- ✅ **Brands**: Logos, productos
- ✅ **Keywords**: Palabras clave
- ✅ **Labels**: Objetos, escenas
- ✅ **Celebrities**: Personas famosas
- ✅ **OCR**: Texto en pantalla

### Video upload
- ✅ **URL**: Direct link
- ✅ **Local file**: Upload desde disco
- ✅ **Azure Storage**: Blob reference
- ✅ **Streaming URL**: Live content
- ✅ **Batch**: Múltiples videos

### Indexing options
- ✅ **Language**: 50+ idiomas
- ✅ **Multi-language**: Detección automática
- ✅ **Advanced**: Face recognition, emotions
- ✅ **Privacy mode**: Sin face recognition
- ✅ **Streaming**: Indexar mientras sube

### Search & Discovery
- ✅ **Full-text search**: En transcripción
- ✅ **Time-based**: Buscar en timeline
- ✅ **Face search**: Por persona
- ✅ **Topic search**: Por tema
- ✅ **Sentiment**: Por emoción

### Integration
- ✅ **REST API**: Automatización
- ✅ **Widgets**: Embeddable player
- ✅ **Azure Media Services**: Streaming
- ✅ **Logic Apps**: Workflows
- ✅ **Power Apps**: Custom apps

---

## ⚠️ Limitaciones

- Video size: Max 2 GB web upload
- Duration: Sin límite (pago por minuto)
- Concurrent jobs: Tier-dependent
- Languages: 50+ pero calidad varía
- Custom models: Requiere training data

---

## ✅ Checklist

- [ ] Video Indexer account creado
- [ ] Primer video subido
- [ ] Indexing language seleccionado
- [ ] Privacy mode configurado
- [ ] Insights revisados
- [ ] Search probado
- [ ] API key obtenida
- [ ] Integration implementada
- [ ] Widgets embebidos (si aplica)
- [ ] Monitoring configurado
- [ ] Cost alerts establecidas
- [ ] Workflow automation (si aplica)
