---
title: Azure Custom Vision
area: azure/ai
owner: LuisAdan
categories: [Resources, Inteligencia Artificial]
tags:
  - azure
  - custom-vision
  - cognitive-services
  - computer-vision
  - image-classification
  - object-detection
  - machine-learning
  - ai
cost: https://azure.microsoft.com/pricing/details/cognitive-services/custom-vision-service/
repo: https://github.com/org/azure-custom-vision-iac
last_review: 2026-02-18
---

## 📋 Características

**Custom Vision** permite crear modelos de visión personalizados sin expertise en ML. Image classification y object detection. Transfer learning, pocos ejemplos necesarios.

### Pricing

**Training:**
- FREE: 2 proyectos, 5000 imágenes
- Standard: $10/mes per 1000 imágenes stored

**Predictions:**
- FREE: 10,000 transacciones/mes
- Standard: $1 per 1000 transacciones

**Training time:**
- Standard: $10/hora compute

**Ejemplo:**
```
Quality inspection: 10k product images, 100k predictions/mes
Storage: 10 × $10 = $100/mes
Training (2h): 2 × $10 = $20/mes
Predictions: 100 × $1 = $100/mes
Total: ~$220/mes

vs Build ML model from scratch:
Data scientist: $10k/mes × 3 meses = $30k
Custom Vision: $660 total (3 meses)
Savings: 97.8%
```

---

## 🏆 Best Practices

### Project Types
- ✅ **Classification**: ¿Qué es esto? (perro, gato, etc.)
- ✅ **Multi-label**: Múltiples tags (perro Y collar Y outdoor)
- ✅ **Object Detection**: ¿Dónde está? (bounding boxes)

### Casos de uso
- ✅ **Quality control**: Defectos en manufactura
- ✅ **Retail**: Reconocimiento de productos
- ✅ **Agriculture**: Enfermedades de plantas
- ✅ **Healthcare**: Screening médico
- ✅ **Wildlife**: Identificación de especies

### Training Data
- ✅ **Mínimo**: 30 imágenes por tag (classification)
- ✅ **Recomendado**: 50+ imágenes por tag
- ✅ **Object detection**: 15+ objetos etiquetados
- ✅ **Variety**: Diferentes ángulos, lighting
- ✅ **Balance**: Similar cantidad por clase

### Labeling
- ✅ **Web UI**: Custom Vision portal
- ✅ **Bounding boxes**: Para object detection
- ✅ **Tags**: Para classification
- ✅ **Negative images**: Sin objetos de interés
- ✅ **Quality**: Etiquetado preciso crítico

### Training
- ✅ **Quick training**: ~1 minuto (default)
- ✅ **Advanced training**: Mejor accuracy, más tiempo
- ✅ **Iterations**: Múltiples versiones
- ✅ **Evaluation**: Precision, recall, AP
- ✅ **Probability threshold**: Ajustar confianza

### Deployment
- ✅ **Cloud API**: REST endpoint
- ✅ **Container**: Docker export
- ✅ **Edge**: IoT Edge, Vision AI Dev Kit
- ✅ **Mobile**: Core ML, TensorFlow Lite
- ✅ **Offline**: Exportar modelo

### Optimization
- ✅ **Compact domains**: Modelos pequeños
- ✅ **Export**: ONNX, CoreML, TensorFlow
- ✅ **Batch predictions**: Múltiples imágenes
- ✅ **Caching**: Resultados frecuentes
- ✅ **Image size**: Resize para performance

---

## ⚠️ Limitaciones

- Image size: Max 6 MB (prediction), 4 MB (training)
- Tags: Max 500 per project
- Images: Depends on tier (FREE: 5k, Standard: millones)
- Training time: Varies (quick: ~1 min, advanced: hours)
- Export: Solo compact domains

---

## ✅ Checklist

- [ ] Custom Vision resource creado
- [ ] Project tipo seleccionado (classification/detection)
- [ ] Domain seleccionado (general, food, retail, etc.)
- [ ] Training images recolectadas (50+ por tag)
- [ ] Images labeled (tags o bounding boxes)
- [ ] Negative images agregadas
- [ ] Modelo entrenado (quick/advanced)
- [ ] Performance evaluado (precision, recall)
- [ ] Threshold ajustado
- [ ] Modelo publicado
- [ ] Prediction endpoint configurado
- [ ] Integration implementada
- [ ] Monitoring habilitado
- [ ] Retraining schedule definido
