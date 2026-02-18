# Azure Form Recognizer (Document Intelligence)

## 📋 Características

**Form Recognizer** (ahora Document Intelligence) es OCR + AI para extraer datos de documentos. Pre-built models (facturas, recibos, IDs) y custom models. Part of Azure Cognitive Services.

### Pricing

**Pre-built models:**
- Read: $0.001/página (OCR básico)
- Layout: $0.01/página (estructura + tablas)
- Invoice: $0.01/página
- Receipt: $0.01/página
- ID: $0.01/página
- Business card: $0.01/página

**Custom models:**
- Training: FREE
- Extraction: $0.01/página

**Ejemplo:**
```
1,000 facturas/mes:
Pre-built invoice: 1,000 × $0.01 = $10/mes

Manual processing: 5 min × $20/hora = ~$1.67/factura
1,000 × $1.67 = $1,670/mes

Form Recognizer: 99.4% más económico
```

---

## 🏆 Best Practices

### Pre-built Models
- ✅ **Read**: OCR texto simple
- ✅ **Layout**: Estructura, tablas, selección marks
- ✅ **Invoice**: Facturas (vendor, total, items)
- ✅ **Receipt**: Recibos (merchant, total, items)
- ✅ **ID**: Identificaciones, pasaportes
- ✅ **Business Card**: Tarjetas de presentación
- ✅ **W-2**: Formularios fiscales US

### Custom Models
- ✅ **Formularios específicos**: Plantillas propias
- ✅ **Training**: Mínimo 5 documentos ejemplo
- ✅ **Labeling**: Studio UI para etiquetar
- ✅ **Tables**: Extraer datos tabulares
- ✅ **Signatures**: Detectar firmas

### Document Types
- ✅ **PDF**: Nativos y escaneados
- ✅ **Images**: JPG, PNG, BMP, TIFF
- ✅ **Office**: DOCX, XLSX, PPTX
- ✅ **Multi-page**: PDFs de múltiples páginas
- ✅ **Handwriting**: Manuscrito (inglés)

### Processing
- ✅ **Synchronous**: <4 segundos respuesta
- ✅ **Asynchronous**: Documentos grandes
- ✅ **Batch**: Múltiples documentos
- ✅ **Confidence scores**: Por campo
- ✅ **Bounding boxes**: Ubicación en documento

### Integration
- ✅ **REST API**: Direct integration
- ✅ **SDK**: .NET, Python, Java, JavaScript
- ✅ **Logic Apps**: Workflow automation
- ✅ **Power Automate**: Low-code automation
- ✅ **Form Recognizer Studio**: UI training

### Validation
- ✅ **Confidence threshold**: Filtrar resultados
- ✅ **Human review**: Low confidence items
- ✅ **Feedback loop**: Mejorar modelo custom
- ✅ **A/B testing**: Comparar modelos

---

## ⚠️ Limitaciones

- File size: Max 500 MB
- Pages: Max 2,000 por documento
- Training: Min 5 documentos para custom
- Languages: Mejor inglés, limitado otros
- Handwriting: Solo inglés actualmente

---

## ✅ Checklist

- [ ] Form Recognizer resource creado
- [ ] Modelo seleccionado (pre-built/custom)
- [ ] Documentos de prueba preparados
- [ ] Custom model training (si aplica)
- [ ] Labeling completado (custom)
- [ ] Modelo entrenado y publicado
- [ ] API integration implementada
- [ ] Confidence threshold configurado
- [ ] Human review workflow (si aplica)
- [ ] Batch processing configurado
- [ ] Monitoring habilitado
- [ ] Error handling implementado
