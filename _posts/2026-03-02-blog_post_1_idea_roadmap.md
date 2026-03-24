---
title: terraform-agent-idea-y-roadmap
area: azure/iac
owner: LuisAdan
categories: [IA, IaC]
tags:
  - terraform
  - azure
  - llm
  - multiagent
  - iac
  - python
  - platform-engineering
repo: https://github.com/org/terraform-agent
last_review: 2026-03-02
---

# Estoy construyendo un sistema que convierte lenguaje natural en infraestructura Azure desplegada. Esto es lo que he aprendido hasta ahora.

*Infraestructura como código generada, validada y desplegada por agentes de IA. Sin templates. Sin alucinaciones. Con Terraform real.*

---

Llevo un tiempo pensando en el mismo problema que muchos equipos de plataforma tienen pero pocos verbalizan bien: **Terraform es potente, pero la barrera de entrada sigue siendo alta**. Un desarrollador que necesita un entorno en Azure no debería tener que aprender HCL, entender el modelo de recursos de azurerm o saber qué atributos son opcionales en la versión 4.x del provider.

Pero la solución obvia —generar el Terraform con un LLM— tiene un problema estructural que no se resuelve simplemente con un buen prompt: **los modelos de lenguaje alucinen atributos que no existen, usan versiones deprecadas del provider y producen HCL que no pasa ni el `terraform validate`**.

Así que decidí construir algo distinto. Y en esta serie de posts voy a documentar cómo.

---

## La idea en una frase

Un pipeline multiagente que toma requisitos en lenguaje natural, los convierte en HCL válido para Azure, lo valida con herramientas reales y lo despliega con aprobación humana en el bucle.

No es un chatbot que genera código. Es un sistema de producción con contratos, reintentos, estado persistente y seguridad desde el principio.

---

## Por qué los enfoques existentes no me convencían

He evaluado varias aproximaciones antes de construir esto:

**Módulos Terraform con variables**: siguen requiriendo que alguien sepa Terraform. La barrera no desaparece, solo baja un escalón.

**Terraform CDK**: añade una capa de abstracción útil, pero sigue siendo código. El desarrollador de aplicaciones que necesita un entorno a las 3pm no quiere aprender TypeScript para eso.

**LLM + prompt directo**: el problema ya mencionado. Sin una fuente de verdad del schema del provider, el modelo inventa. Y cuando el HCL llega a `terraform plan`, explota.

**Herramientas comerciales de IaC con AI**: existen, pero son cajas negras, costosas y no se adaptan a las restricciones de seguridad de muchas organizaciones (OIDC, tenants propios, políticas de red).

Lo que faltaba era un sistema que use el schema real del provider como fuente de verdad, valide el HCL generado con las mismas herramientas que usaría un ingeniero senior, y mantenga un humano en el bucle antes de aplicar cualquier cambio.

---

## La arquitectura a alto nivel

Sin entrar en detalles de implementación todavía, el sistema tiene estas piezas:

**Agentes especializados**, cada uno con una responsabilidad única:
- Uno que recoge requisitos en lenguaje natural y los estructura
- Uno que consulta documentación oficial de Azure para extraer best practices
- Uno que genera el HCL usando el schema exacto del provider como única referencia
- Uno que ejecuta un pipeline de validación con herramientas reales
- Uno que orquesta el estado, los reintentos y las métricas

**Infraestructura de soporte** diseñada para producción desde el día uno:
- Estado remoto en Azure Blob Storage con locking nativo
- Autenticación sin secretos de larga duración (OIDC)
- Flujo de aprobación humana antes de cualquier `terraform apply`

**Un bucle de corrección automática** entre el generador y el validador, con límite de reintentos y escalado explícito cuando se agota.

---

## El roadmap que estoy siguiendo

Estoy construyendo esto en fases pequeñas, donde cada paso produce algo funcional antes de avanzar al siguiente. El orden no es arbitrario: cada componente desbloquea el siguiente.

```
Fase 1 — Fundamentos
  ├── Paso 1: Capa de contratos (interfaces entre agentes)
  ├── Paso 2: Fuente de verdad del provider
  └── Paso 3: Backend remoto de estado + autenticación OIDC

Fase 2 — Agentes Core
  ├── Paso 4: Agente Conversacional
  ├── Paso 5: Agente Arquitecto (integración con docs oficiales)
  └── Paso 6: Agente Builder (generación de HCL)

Fase 3 — Pipeline de Revisión
  ├── Paso 7: Pipeline fmt → tflint → checkov → validate → plan
  └── Paso 8: Bucle Builder ↔ Revisor con reintentos

Fase 4 — Despliegue y Aprobación
  ├── Paso 9: Flujo de aprobación humana
  ├── Paso 10: Agente Deployer
  └── Paso 11: Orquestador con estado persistente y métricas

Fase 5 — Post-MVP
  ├── Validación de políticas con OPA
  ├── Outputs sensibles a Key Vault
  ├── Observabilidad completa
  ├── Operaciones Day 2 (modificar, destruir, importar)
  └── Detección de drift
```

Cada post de esta serie cubre un paso. Cuando termine, el repositorio completo estará disponible.

---

## Lo que he aprendido en el Paso 1

El primer paso no genera infraestructura. No llama a ningún LLM. No toca Azure.

Define los contratos de datos entre agentes: qué información existe, qué forma tiene, y qué invariantes debe cumplir. Es la decisión de diseño más importante del sistema, y la que más se subestima.

Algunas decisiones no obvias que tomé aquí y que evitaron problemas más adelante:

- Por qué un UUID de correlación generado una sola vez cambia completamente la depurabilidad del sistema
- Por qué `passed` no puede ser un campo editable si quieres que el sistema sea coherente
- Por qué un diccionario genérico y un modelo Pydantic no son intercambiables, aunque en Python parezca que sí

El siguiente post entra en esos detalles.

---

## Por qué lo estoy documentando públicamente

Dos razones.

La primera es práctica: documentar mientras construyes obliga a entender lo que estás haciendo. Si no puedes explicar una decisión de diseño, probablemente no la has tomado bien.

La segunda es que este tipo de sistema —multiagente, con herramientas reales, con seguridad desde el principio— no tiene muchos referentes documentados desde cero. La mayoría de los tutoriales de "AI + Terraform" son demos de 5 minutos que no sobrevivirían un entorno real.

Esto pretende ser diferente.

---

*Siguiente post: Paso 1 en detalle — cómo definir contratos Pydantic v2 que hacen que un sistema multiagente sea depurable, testeable y mantenible.*

---

**Tags:** `terraform` `azure` `llm` `multiagent` `iac` `python` `pydantic` `devops` `platform-engineering`
