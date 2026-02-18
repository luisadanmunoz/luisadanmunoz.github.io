# Azure Speech Service

## 📋 Características

**Speech Service** combina speech-to-text, text-to-speech, speech translation y speaker recognition. Neural voices, custom models, real-time y batch.

### Pricing

**Speech-to-Text:**
- Standard: $1/hora audio
- Custom: $1.40/hora audio

**Text-to-Speech:**
- Neural voices: $16 per millón de caracteres
- Custom Neural Voice: $24 per millón + hosting $2,900/mes

**Speech Translation:**
- $2.50/hora audio

**Speaker Recognition:**
- Verification: $1 per 1000 transacciones
- Identification: $1 per 1000 transacciones

**Ejemplo:**
```
Call center: 1000 horas audio/mes
Speech-to-Text: 1000 × $1 = $1,000/mes
Text-to-Speech (responses): 10M chars × $16/million = $160/mes
Total: ~$1,160/mes

vs Human transcription: $1-2/minuto
1000 hours = 60,000 min × $1.50 = $90,000
Speech Service: 98.7% más económico
```

---

## 🏆 Best Practices

### Speech-to-Text
- ✅ **Real-time**: Streaming transcription
- ✅ **Batch**: Archivos de audio
- ✅ **Custom models**: Domain-specific vocabulary
- ✅ **Diarization**: Identificar speakers
- ✅ **110+ idiomas**: Cobertura global

### Text-to-Speech
- ✅ **Neural voices**: Natural sounding
- ✅ **400+ voices**: Múltiples idiomas
- ✅ **SSML**: Speech Synthesis Markup
- ✅ **Custom Neural Voice**: Voz personalizada
- ✅ **Voice styles**: Emotions, tones

### Speech Translation
- ✅ **Real-time**: Simultaneous translation
- ✅ **90+ idiomas**: Speech-to-text translation
- ✅ **Speech-to-speech**: Voice output
- ✅ **Multi-language**: Detectar y traducir

### Speaker Recognition
- ✅ **Verification**: 1:1 matching (authentication)
- ✅ **Identification**: 1:N matching (who is speaking)
- ✅ **Text-independent**: Sin frase específica
- ✅ **Enrollment**: 20 segundos audio

### Custom Models
- ✅ **Acoustic model**: Para entornos ruidosos
- ✅ **Language model**: Vocabulario técnico
- ✅ **Pronunciation**: Nombres propios, marcas
- ✅ **Training data**: Transcripciones + audio

### Integration
- ✅ **Speech SDK**: C#, C++, Java, Python, JavaScript
- ✅ **REST API**: HTTP endpoints
- ✅ **Speech CLI**: Command line
- ✅ **Speech Studio**: Web UI para testing
- ✅ **Bot Framework**: Voice bots

### Optimización
- ✅ **Audio format**: WAV, MP3, Opus
- ✅ **Sample rate**: 16 kHz recommended
- ✅ **Channels**: Mono preferred
- ✅ **Noise reduction**: Pre-processing
- ✅ **Compression**: Balance calidad/costo

---

## ⚠️ Limitaciones

- Audio duration: Max 10 minutos (real-time)
- Batch: Max 1000 files simultáneos
- Custom voice: Requiere 2000+ utterances
- Languages: No todos features en todos idiomas
- Latency: Real-time ~100-300ms

---

## ✅ Checklist

- [ ] Speech resource creado
- [ ] Region seleccionada (latency)
- [ ] Speech-to-Text configurado
- [ ] Custom model training (si aplica)
- [ ] Vocabulary list creada
- [ ] Text-to-Speech voice seleccionada
- [ ] SSML templates creadas
- [ ] Custom Neural Voice (si necesario)
- [ ] Speaker Recognition enrollments
- [ ] SDK integrado en aplicación
- [ ] Audio format optimizado
- [ ] Error handling implementado
- [ ] Monitoring configurado
- [ ] Cost tracking habilitado
