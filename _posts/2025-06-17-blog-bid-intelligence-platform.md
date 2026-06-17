---
title: bid-intelligence-platform
area: azure/iac
owner: LuisAdan
categories: [IA, IaC]
tags:
  - azure
  - management-groups
  - governance
  - rbac
  - policy
last_review: 2026-06-17
---

Responder a un pliego de licitación de 500 páginas es un trabajo que consume semanas. Hay que leer, extraer requisitos, buscar evidencias en documentación propia, redactar, revisar y asegurarse de no dejar nada sin cubrir. El error humano es caro: un requisito ignorado puede descalificar una oferta.

Llevo semanas construyendo una **Bid Intelligence Platform**: un sistema que orquesta diez agentes de IA especializados para automatizar ese proceso de principio a fin, manteniendo trazabilidad total entre cada requisito del pliego y la evidencia que lo respalda.

Este post explica las decisiones de diseño que tomé y cómo está construido.

---

## El problema real

Un equipo de preventa típico tiene que:

1. Leer el pliego (PDF, DOCX, XLSX, anexos)
2. Extraer todos los requisitos —técnicos, administrativos, legales, económicos—
3. Buscar en su base documental (ofertas ganadas, fichas técnicas) qué evidencias tienen
4. Redactar una respuesta coherente con citas trazables
5. Detectar gaps y riesgos antes de presentar
6. Revisar, iterar, exportar

Nada de esto es trivial de automatizar. Un chatbot con documentos no sirve: no hay trazabilidad, no hay estructura, no hay garantía de que la respuesta esté fundamentada en evidencia real. Necesitaba algo más parecido a un equipo de trabajo que a un asistente de chat.

---

## Arquitectura: diez agentes, un pipeline

El núcleo de la plataforma es un pipeline agentico con seis fases:

```
Documento PDF/DOCX/XLSX
        ↓
[Agente 1 — Ingesta]       → Extrae texto, tablas y estructura → Vector store
        ↓
[Agente 2 — Extractor]     → Identifica todos los requisitos del pliego
        ↓
[Agente 3 — Clasificador]  → Categoriza (técnico/admin/legal/económico) + routing
        ↓
        ├── [Agente 4 — Técnico]  → Respuesta técnica con evidencia del corpus
        └── [Agente 6 — Legal]    → Análisis de riesgos legales
              ↓ (paralelo)
[Agente 8 — Redactor]      → Síntesis en prosa profesional con citas numeradas
        ↓
[Agente 10 — Cumplimiento] → Matriz de cumplimiento + score global
        ↓
     Revisión humana (UI / API)
        ↓
     Exportación Word / Excel / PDF
```

Cada agente tiene responsabilidad única, prompt de sistema propio y acceso controlado al RAG corporativo. Ninguno inventa: si no hay evidencia en el corpus, declara el gap explícitamente.

---

## Decisión de diseño #1: Arquitectura hexagonal

Lo primero que hice fue separar el dominio del negocio de la infraestructura. La estructura del proyecto refleja eso:

```
bid-intelligence-platform/
├── core/
│   ├── models/      # Dominio puro: Bid, Requirement, Document
│   └── ports/       # Interfaces abstractas: LLMPort, VectorStorePort, DocumentProcessorPort
├── adapters/
│   ├── local/       # Implementaciones locales: OpenAI, ChromaDB, pymupdf
│   └── azure/       # Implementaciones Azure: Azure OpenAI, AI Search, Document Intelligence
├── agents/          # Los agentes especializados
├── orchestrator/    # Pipeline de coordinación
├── rag/             # Chunker + Retriever híbrido
├── api/             # FastAPI
└── ui/              # Streamlit (prototipo)
```

La clave está en que `core/ports/` define las interfaces. Los agentes dependen de abstracciones, no de implementaciones. El resultado es que puedo correr todo localmente con ChromaDB y OpenAI SDK, y después reemplazar esos adaptadores por Azure AI Search y Azure OpenAI **sin tocar una sola línea de lógica de negocio**.

La tabla de migración es directa:

| Local | Azure (producción) |
|---|---|
| ChromaDB | Azure AI Search |
| pymupdf | Azure AI Document Intelligence |
| SQLite | Azure SQL Database |
| OpenAI SDK | Azure OpenAI |
| Filesystem | Azure Blob Storage / ADLS Gen2 |
| In-memory state | Azure Service Bus + Redis |

Esto me permitió validar el pipeline completo en mi máquina antes de comprometer ni un euro en Azure.

---

## Decisión de diseño #2: RAG híbrido con RRF

El retrieval es el componente más crítico para la calidad de las respuestas. Usé **Reciprocal Rank Fusion (RRF)** para combinar búsqueda vectorial y keyword (BM25):

```python
def _reciprocal_rank_fusion(
    self,
    vector_results: list[SearchResult],
    keyword_results: list[SearchResult],
    k: int = 60,
) -> list[RetrievedChunk]:
    scores: dict[str, float] = {}

    for rank, result in enumerate(vector_results):
        scores[result.id] = scores.get(result.id, 0.0) + 1.0 / (k + rank + 1)

    for rank, result in enumerate(keyword_results):
        scores[result.id] = scores.get(result.id, 0.0) + 1.0 / (k + rank + 1)

    return sorted(scores.items(), key=lambda x: x[1], reverse=True)
```

RRF es robusto porque no necesita normalizar scores de distinto origen: combina los rankings, no las puntuaciones. Un chunk que aparece en los primeros puestos de ambas búsquedas sube al tope; uno que solo aparece en una se queda más abajo.

El chunking es semántico por sección → párrafo → tokens como fallback. Ventana de 512 tokens con overlap de 64 para no romper el contexto entre chunks.

---

## Decisión de diseño #3: Trazabilidad como requisito de primer nivel

El mayor riesgo de estos sistemas es la alucinación: generar respuestas convincentes sin evidencia real. Mi solución es estructural, no post-hoc.

Cada respuesta generada incluye citas numeradas `[1]`, `[2]`... trazables a documentos concretos del corpus. El `ContextBuilder` construye el contexto con cabeceras explícitas:

```
[1] Oferta_Cliente_X_2024.pdf — Sección 3.2 Arquitectura (pág. 47)
Implementamos una solución de alta disponibilidad basada en Azure...

[2] Ficha_Tecnica_Producto_A.pdf — Capacidades de integración (pág. 12)
...
```

Si el agente no encuentra evidencia suficiente, **no redacta**: devuelve un gap con `has_gaps: true` y `gap_summary` explicando qué falta. Eso es más valioso que una respuesta inventada.

El `AgentTrace` captura para cada ejecución: qué chunks usó, qué documentos citó, cuántos tokens consumió y cuánto tardó. Trazabilidad completa de extremo a extremo.

---

## Decisión de diseño #4: Concurrencia controlada

Un pliego típico tiene entre 30 y 150 requisitos. Procesarlos secuencialmente sería demasiado lento. Los proceso en paralelo con un semáforo que limita a tres requisitos simultáneos para respetar los rate limits de la API:

```python
semaphore = asyncio.Semaphore(3)

async def process_one(req: dict) -> dict:
    async with semaphore:
        return await self._process_single_requirement(req, bid_id, language)

tasks = [process_one(req) for req in requirements]
await asyncio.gather(*tasks)
```

Dentro de cada requisito, el análisis técnico y el análisis legal corren en paralelo también. El redactor espera a ambos antes de sintetizar.

---

## Stack técnico

**Entorno local (desarrollo/validación):**
- Python 3.12, FastAPI, Streamlit
- OpenAI SDK (`gpt-4o` + `text-embedding-3-small`)
- ChromaDB (vector store persistido en disco)
- SQLite + Alembic (modelo de datos y migraciones)
- pymupdf + python-docx + openpyxl (extracción documental)
- loguru (logging estructurado)

**Producción (Azure):**
- Azure OpenAI (`gpt-4o`, `text-embedding-3-large`)
- Azure AI Foundry (orquestación agentica)
- Azure AI Search (RAG híbrido con semantic ranker)
- Azure AI Document Intelligence (OCR y extracción estructurada)
- Azure Container Apps (backend + agentes)
- Azure Key Vault + Managed Identity
- Application Insights

---

## La base documental corporativa

El corpus corporativo es el corazón del sistema. Contiene ofertas ganadas, ofertas perdidas y fichas técnicas de productos. Los agentes consultan este corpus para respaldar cada respuesta.

El flujo de incorporación de nuevos documentos tiene una etapa de aprobación: no cualquier documento entra al corpus directamente. Hay un proceso de revisión antes de que un documento pase a producción y sea consultable por los agentes.

La integración con SharePoint (para entornos enterprise) sincroniza el corpus automáticamente cuando se publican nuevos documentos en las bibliotecas designadas.

---

## Estado actual y próximos pasos

El pipeline local está operativo: ingesta, extracción, clasificación, análisis técnico+legal, redacción y matriz de cumplimiento funcionan end-to-end. He procesado pliegos reales de entre 50 y 200 páginas con resultados que ya son útiles como primer borrador.

Lo que viene:

- **Agentes administrativo y económico** (actualmente el clasificador los enruta pero no tienen agente específico)
- **Exportación** a Word con track-changes y a Excel con la matriz de cumplimiento completa
- **Revisión humana multi-nivel** en la UI: cada requisito con su evidencia y la posibilidad de editar y aprobar
- **Migración a Azure**: reemplazar los adaptadores locales por los servicios de Azure sin tocar la lógica de negocio

La arquitectura hexagonal hace que esa migración sea, en teoría, un cambio de configuración. En teoría.

---

## Reflexión final

Lo que más me ha costado no es el código: es definir qué significa "una buena respuesta" en este dominio. Una respuesta a una licitación no es solo texto correcto: tiene que ser trazable, conservadora cuando hay incertidumbre, estructurada según los criterios del pliego y revisable por un humano antes de salir.

Esos requisitos informan cada decisión de diseño: por qué los agentes citan sus fuentes, por qué hay una fase de revisión humana antes de exportar, por qué los gaps se declaran explícitamente en lugar de rellenarse con texto plausible.

La IA puede acelerar enormemente este proceso. Pero la firma al pie de la oferta sigue siendo humana.

---

*El código está en desarrollo activo. Si tienes preguntas sobre la arquitectura o el stack, puedes contactarme en [luisadanmunoz@outlook.com](mailto:luisadanmunoz@outlook.com).*
