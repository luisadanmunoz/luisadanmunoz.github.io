# Azure Translator

## 📋 Características

**Azure Translator** es servicio de traducción automática con AI. Neural Machine Translation (NMT), 100+ idiomas, personalización con Custom Translator.

### Pricing

**Text Translation:**
- S1: $10 per millón de caracteres
- FREE tier: 2M caracteres/mes

**Document Translation:**
- S1: $15 per millón de caracteres

**Custom Translator:**
- Training: $10/modelo/mes (hosting)
- Translation: +$10 adicional per millón caracteres

**Ejemplo:**
```
Traducir 10M caracteres/mes (text):
10 × $10 = $100/mes

Con custom model:
Translation: $100
Model hosting: $10/mes
Custom translation: 10 × $10 = $100
Total: ~$210/mes

vs Human translation: $0.10-0.20/palabra
10M chars = ~2M palabras = $200k-400k
Translator: 99.9% más económico
```

---

## 🏆 Best Practices

### Casos de uso
- ✅ **Websites**: Localización multi-idioma
- ✅ **Apps**: Traducción in-app
- ✅ **Documents**: PDFs, Office, HTML
- ✅ **Chat/Support**: Atención multi-idioma
- ✅ **Content**: Blogs, artículos, productos

### Idiomas soportados
- ✅ **100+ idiomas**: Cobertura global
- ✅ **Neural translation**: Alta calidad
- ✅ **Transliteration**: Conversión scripts
- ✅ **Language detection**: Automático
- ✅ **Bilingual dictionary**: Traducciones alternativas

### Features
- ✅ **Text translation**: Texto simple
- ✅ **Document translation**: Preservar formato
- ✅ **Batch translation**: Múltiples documentos
- ✅ **Custom Translator**: Modelos específicos
- ✅ **Dictionary lookup**: Contexto adicional

### Document Translation
- ✅ **Formatos**: PDF, DOCX, XLSX, PPTX, HTML
- ✅ **Layout preservation**: Mantiene formato
- ✅ **Batch**: Hasta 1000 documentos
- ✅ **Async**: Procesos largos
- ✅ **Glossary**: Términos personalizados

### Custom Translator
- ✅ **Domain-specific**: Jerga técnica
- ✅ **Training**: Mínimo 10k sentence pairs
- ✅ **Tuning**: Mejorar calidad
- ✅ **Testing**: Validación BLEU score
- ✅ **Deployment**: Endpoint dedicado

### Integration
- ✅ **REST API**: HTTP calls
- ✅ **SDK**: .NET, Python, Java, Node.js
- ✅ **Functions**: Serverless translation
- ✅ **Logic Apps**: Workflow automation
- ✅ **Power Automate**: Low-code

---

## ⚠️ Limitaciones

- Request size: Max 50,000 caracteres por request
- Document size: Max 40 MB
- Languages: No todos pares soportados igual
- Custom Translator: Requiere training data
- Real-time: Latency ~100-500ms

---

## ✅ Checklist

- [ ] Translator resource creado
- [ ] API key obtenido
- [ ] Idiomas objetivo identificados
- [ ] Text translation implementado
- [ ] Document translation configurado (si aplica)
- [ ] Glossary creado (términos específicos)
- [ ] Custom model training (si necesario)
- [ ] Training data preparado (10k+ pairs)
- [ ] Modelo entrenado y deployado
- [ ] Integration testing completado
- [ ] Error handling implementado
- [ ] Monitoring configurado
- [ ] Cost tracking habilitado
