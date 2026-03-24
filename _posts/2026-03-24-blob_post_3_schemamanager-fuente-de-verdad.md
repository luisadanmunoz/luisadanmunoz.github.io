---
title: terraform-agent-paso-2-schemamanager-fuente-de-verdad
area: azure/iac
owner: LuisAdan
categories: [IaC, IA]
tags:
  - terraform
  - azure
  - python
  - multiagent
  - llm
  - iac
  - platform-engineering
  - software-architecture
repo: https://github.com/org/terraform-agent
last_review: 2026-03-24
---

# Paso 2: El módulo que impide que un LLM invente atributos de Terraform

*~15 MB de JSON. Un índice en memoria. Cero alucinaciones de atributos. Así funciona el SchemaManager.*

---

Si llegaste desde el post anterior, ya sabes que el Paso 1 definió los contratos de datos entre agentes. Este post cubre el Paso 2: el componente que convierte el schema real del provider azurerm en la única fuente de verdad que el Builder puede consultar.

El Paso 2 tampoco llama a ningún LLM. Tampoco toca Azure. Pero sin él, todo lo que venga después es frágil.

---

## El problema concreto

Los LLMs cometen un tipo de error muy específico cuando generan Terraform: inventan atributos que no existen o usan nombres de versiones anteriores del provider.

Algunos ejemplos reales con azurerm 4.x:

```hcl
# ❌ enable_https_traffic_only fue renombrado en azurerm 3.x
resource "azurerm_storage_account" "main" {
  enable_https_traffic_only = true  # no existe en 4.x
}

# ❌ address_prefix no existe en azurerm_virtual_network
resource "azurerm_virtual_network" "main" {
  address_prefix = "10.0.0.0/16"  # el atributo es address_space (lista)
}

# ❌ subnet inline está deprecated
resource "azurerm_virtual_network" "main" {
  subnet {
    name           = "snet-app"
    address_prefix = "10.0.1.0/24"
  }
}
```

Ninguno de estos errores se detecta en el prompt. Se detectan en `terraform validate`, que es la cuarta etapa del pipeline de revisión. Si el Builder llega hasta ahí antes de enterarse, ha desperdiciado tres etapas y una iteración completa del bucle de reintentos.

El SchemaManager mueve esa detección al origen: antes de generar una sola línea de HCL.

---

## Qué se construyó

Un módulo Python con tres modelos internos y una interfaz pública de ocho métodos:

```
schema/
├── schema_manager.py        # módulo principal
└── azurerm_4_0.json         # generado con terraform providers schema -json (~15 MB)

tests/
└── schema/
    ├── test_schema_manager.py
    └── fixtures/
        └── azurerm_minimal.json  # 3 recursos para CI, sin depender del JSON real
```

---

## Cómo funciona por dentro

El JSON que produce `terraform providers schema -json` tiene esta estructura para cada recurso:

```json
{
  "provider_schemas": {
    "registry.terraform.io/hashicorp/azurerm": {
      "resource_schemas": {
        "azurerm_virtual_network": {
          "version": 0,
          "block": {
            "attributes": {
              "address_space": { "type": ["list","string"], "required": true },
              "location":      { "type": "string", "required": true },
              "id":            { "type": "string", "computed": true }
            },
            "block_types": {
              "ddos_protection_plan": { "nesting_mode": "list", "block": {...} }
            }
          }
        }
      }
    }
  }
}
```

El SchemaManager carga este JSON una sola vez en `__init__`, navega hasta `resource_schemas` y construye un índice en memoria. Cada recurso se convierte en un objeto `ResourceSchema` con cuatro colecciones ya clasificadas:

```python
@dataclass
class ResourceSchema:
    resource_type: str
    required_attributes:      dict[str, AttributeSchema]
    optional_attributes:      dict[str, AttributeSchema]
    computed_only_attributes: dict[str, AttributeSchema]
    blocks:                   dict[str, BlockSchema]

    def summary(self) -> dict:
        """Versión compacta para prompts del Builder."""
        return {
            "required_attributes":      list(self.required_attributes.keys()),
            "optional_attributes":      list(self.optional_attributes.keys()),
            "computed_only_attributes": list(self.computed_only_attributes.keys()),
            "required_blocks":          [k for k,v in self.blocks.items() if v.required],
            "optional_blocks":          [k for k,v in self.blocks.items() if not v.required],
        }
```

El Builder no recibe el JSON crudo. Recibe `summary()`: una lista de nombres. Con eso tiene suficiente para saber qué puede usar, qué es obligatorio y qué no debe tocar porque es `computed_only`.

---

## Las decisiones no obvias

### 1. `SchemaError` en lugar de `None` para recursos inexistentes

La primera versión devolvía `None` si un recurso no existía en el schema. El problema: cada caller tenía que manejar el caso nulo.

```python
# ❌ con None — el error puede propagarse silenciosamente
schema = sm.get_resource_schema("azurerm_nonexistent")
if schema:
    attrs = schema.required_attributes  # nunca llega aquí
# pero nadie se entera del fallo hasta más tarde
```

```python
# ✅ con SchemaError — el fallo es inmediato y trazable
try:
    schema = sm.get_resource_schema("azurerm_nonexistent")
except SchemaError as e:
    # e.resource_type = "azurerm_nonexistent"
    # el contexto está en la excepción
```

`SchemaError` hereda de la jerarquía de excepciones del sistema y lleva `resource_type` como atributo. El Orquestador puede capturarla, loguearla con `pipeline_id` y escalar al usuario sin perder contexto.

### 2. Carga única con índice en memoria

El JSON se parsea una sola vez en `__init__`. Las consultas posteriores son búsquedas en un `dict` Python: O(1).

La alternativa —leer el JSON en cada consulta— parece más "pura" pero introduce latencia variable en el hot path del Builder. Con ~847 recursos y un JSON de 15 MB, la primera carga tarda ~2-3 segundos. Cada consulta posterior tarda microsegundos.

### 3. Normalización de tipos

El schema de Terraform representa los tipos como listas anidadas:

```json
"type": ["list", "string"]
"type": ["map", "number"]
"type": ["object", {"ip_configuration": [...]}]
```

El SchemaManager normaliza esto a strings legibles antes de exponerlo:

```python
["list", "string"]          → "list(string)"
["map", "number"]           → "map(number)"
["object", {"a": ..., "b": ...}] → "object(a, b)"
```

El Builder trabaja con `"list(string)"`, no con `["list", "string"]`. Es un detalle pequeño con impacto grande en la legibilidad de los prompts y en los tests.

### 4. Fixture minimal para CI

Los tests no dependen del JSON real de 15 MB. Un fixture de 3 recursos cubre toda la interfaz pública:

- `azurerm_resource_group` — recurso simple, solo atributos
- `azurerm_virtual_network` — recurso con bloques anidados
- `azurerm_storage_account` — recurso con atributos sensitive y computed

Esto permite ejecutar la suite completa en CI en menos de un segundo, sin Terraform instalado, sin descargar el provider, sin conexión a internet.

---

## La interfaz completa

```python
from schema import SchemaManager

sm = SchemaManager("schema/azurerm_4_0.json")

# Cuántos recursos hay
print(sm.resource_count)  # 847

# Existe un recurso?
sm.resource_exists("azurerm_virtual_network")  # True
sm.resource_exists("azurerm_nonexistent")       # False

# Schema completo
schema = sm.get_resource_schema("azurerm_virtual_network")
schema.required_attributes   # {"address_space": AttributeSchema(...), ...}
schema.optional_attributes   # {"bgp_community": ..., "dns_servers": ..., ...}
schema.computed_only_attributes  # {"id": ..., "guid": ...}
schema.blocks                # {"ddos_protection_plan": BlockSchema(...), ...}

# Resumen para prompts
sm.get_summary("azurerm_virtual_network")
# {
#   "required_attributes": ["address_space", "location", "name", "resource_group_name"],
#   "optional_attributes": ["bgp_community", "dns_servers", "tags", ...],
#   "computed_only_attributes": ["guid", "id"],
#   "required_blocks": [],
#   "optional_blocks": ["ddos_protection_plan", "encryption", "timeouts"]
# }
```

Con `summary()`, el Builder puede construir un prompt del tipo:

> *"Genera HCL para azurerm_virtual_network. Atributos requeridos: address_space, location, name, resource_group_name. No incluyas atributos computed_only: guid, id."*

El LLM no adivina. Trabaja con una lista exacta extraída del schema real del provider.

---

## Cómo replicarlo

```bash
# 1. Generar el JSON del provider (solo la primera vez)
mkdir -p schema
cd /tmp && cat > provider.tf << 'EOF'
terraform {
  required_providers {
    azurerm = { source = "hashicorp/azurerm", version = "~> 4.0" }
  }
}
provider "azurerm" { features {} }
EOF
terraform init
terraform providers schema -json > /ruta/proyecto/schema/azurerm_4_0.json

# 2. Añadir a .gitignore (no commitear los 15 MB)
echo "schema/azurerm_4_0.json" >> .gitignore

# 3. Ejecutar los tests (con fixture minimal, sin el JSON real)
pytest tests/schema/ -v --cov=schema --cov-report=term-missing

# 4. Verificación manual con el JSON real
python -c "
from schema import SchemaManager
sm = SchemaManager('schema/azurerm_4_0.json')
print(f'Recursos indexados: {sm.resource_count}')
print(sm.get_summary('azurerm_virtual_network'))
"
```

Resultado esperado:

```
Recursos indexados: 847
{
  'required_attributes': ['address_space', 'location', 'name', 'resource_group_name'],
  'optional_attributes': ['bgp_community', 'dns_servers', 'edge_zone', 'tags', ...],
  'optional_blocks': ['ddos_protection_plan', 'encryption', 'timeouts']
}
```

---

## Lo que este paso no hace

No valida que los *valores* de los atributos sean correctos. Sabe que `address_space` existe y es de tipo `list(string)`, pero no sabe si `["10.0.0.0/8", "192.168.0.0/16"]` es una combinación válida para ese entorno.

Esa validación semántica ocurre en el Revisor, en la etapa `checkov` y `terraform plan`. El SchemaManager resuelve un problema más acotado: que el Builder no use atributos que no existen. Lo demás tiene su sitio más adelante en el pipeline.

---

## Siguiente paso

El Paso 3 configura el backend remoto de tfstate en Azure Blob Storage y la autenticación OIDC desde GitHub Actions.

Con los contratos y el SchemaManager en su sitio, el siguiente bloque es la infraestructura de soporte que hace posible ejecutar `terraform plan` desde el pipeline sin secretos de larga duración. Sin esto, el Revisor no puede ejecutar el plan porque no tiene acceso al state ni credenciales seguras para Azure.

Es el primer paso que requiere recursos reales en Azure.

---

*El código de este paso, la documentación técnica completa y los tests están disponibles en el repositorio del proyecto.*

---

**Tags:** `terraform` `azure` `python` `multiagent` `llm` `iac` `platform-engineering` `software-architecture`