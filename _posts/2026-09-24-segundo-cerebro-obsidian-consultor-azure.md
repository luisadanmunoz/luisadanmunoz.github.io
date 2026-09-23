---
title: segundo-cerebro-obsidian-consultor-azure
area: productividad/knowledge-management
owner: LuisAdan
categories: [Productividad, IA]
tags:
  - obsidian
  - claude-code
  - git
  - gitleaks
  - templater
  - azure
  - knowledge-management
repo: privado
last_review: 2026-09-24
mermaid: true
---

Como consultor Azure, mi conocimiento estaba repartido por todas partes: ofertas en carpetas locales, chuletas de comandos en ficheros sueltos, apuntes de certificaciones en PDFs, módulos de Terraform en repos, y decenas de "esto ya lo resolví una vez, pero ¿dónde?".

Decidí ponerle orden con **Obsidian**, pero sin quedarme en "instalo plugins y a ver qué pasa". Quería un sistema enterprise: versionado, con guardarraíles de seguridad, convenciones estrictas y conectado a **Claude Code** para que la IA pudiera consultar y escribir en él con las mismas reglas que yo.

Esta es la guía de cómo lo monté paso a paso, con las decisiones que tomé y, sobre todo, con los errores que cometí por el camino.

---

## La regla que me impuse: no pasar de paso sin validar el anterior

El plan final tuvo 35 pasos agrupados en 8 fases. La disciplina fue sencilla: cada paso terminaba con una **prueba verificable** (un comando, una nota de prueba, una captura) y no avanzaba hasta que salía bien.

Suena lento, pero me ahorró horas. Varios de los problemas que cuento al final los detecté justo porque la prueba del paso falló.

---

## Fase 0: las decisiones que condicionan todo

Antes de crear una sola carpeta tuve que decidir cuatro cosas. Y reconozco que cambié de opinión en la más importante.

**Uno o dos vaults.** Empecé diseñando dos vaults: uno "conectable" (Azure, IA, SysOps) enlazado a Claude y GitHub, y otro "cerrado", solo local, para el material de clientes. Al avanzar vi que la separación me costaba más de lo que me aportaba, y acabé en **un vault único**, versionado en un repo privado de GitHub y conectado a Claude.

Si te planteas lo mismo, mi consejo es no decidirlo a la ligera: revisa qué dicen tus contratos y la política de tu empresa sobre almacenar datos de cliente en GitHub y procesarlos con IA. Esa decisión es tuya, no de la herramienta.

**Binarios fuera de Git.** Los `pptx`, `xlsx`, `docx`, `pdf` y `zip` no se versionan. Git está pensado para texto, y los binarios hacen crecer el repo sin aportar nada útil al historial. Los protejo con una copia de seguridad aparte.

**Repos de código fuera del vault.** Probé a meter los repos dentro de las carpetas de cliente, con su propio `.git`, y acabé sacándolos: cada repo vive en su sitio y desde las notas enlazo a su URL de GitHub.

**Motor de consultas: Bases + Tasks.** Bases es un plugin core de Obsidian: no añade código de terceros y trabaja directamente sobre las propiedades del frontmatter, que es donde está toda mi información estructurada. Tasks cubre lo que Bases no hace bien, que son las tareas sueltas dentro de las notas.

---

## Fase 1: cimientos

### Estructura de carpetas

Tras varias iteraciones, la estructura quedó así:

```
Vault-Consultoria/
├── 00-SysOps/          # Chuletas: AzCli, KQL, Docker, Kubernetes, Git, Terraform, PowerShell
├── 01-Azure/
│   ├── 01-Recursos/    # Un servicio de Azure por nota, agrupados por categoría
│   └── 02-Certificaciones/   # Una carpeta por certificación con sus apuntes
├── 02-Terraform/       # Un recurso azurerm por nota, mismas categorías
├── 03-IA/              # 01-MVP · 02-Skills · 03-Casos-de-Uso
├── 04-Clientes/<Cliente>/   # 01-Ofertas · 02-Proyectos · 03-Documentacion-Cliente · 04-Reuniones
├── 98-Documentos/      # Web-Clipper, Diagramas, Iconos-Azure
└── 99-Plantillas/      # Convenciones, registro de plugins, plantillas de Templater
```

Dos lecciones de diseño:

- **Todo con guiones, sin tildes ni espacios.** Las rutas pasan por Git, PowerShell y Claude Code, y cada carácter raro es un problema potencial.
- **Numeración correlativa.** Parece una manía, pero cuando quité una subcarpeta de cliente y quedó un hueco en la numeración, preferí renumerar. Eso me obligó a actualizar el router de plantillas y las convenciones, y fue la mejor prueba de que todo estaba bien acoplado.

Toda la estructura se crea con un script de PowerShell **idempotente**: lo puedo relanzar para añadir un cliente o una certificación sin tocar lo que ya existe.

### Git + Gitleaks: la red de seguridad

Si el vault se sube a GitHub, un secreto pegado por descuido en una nota acaba en internet. Por eso el primer guardarraíl fue un **hook pre-commit con Gitleaks**, que bloquea cualquier commit que contenga algo con aspecto de credencial:

```powershell
$hook = "#!/bin/sh`ngitleaks git --pre-commit --staged --redact -v`n"
[IO.File]::WriteAllText("$PWD\.git\hooks\pre-commit", $hook)
```

Lo probé con un token falso con formato de GitHub, y Gitleaks lo detectó, lo tapó (`REDACTED`) y abortó el commit. Justo lo que quería.

Y al día siguiente me bloqueó a mí. Al subir la carpeta `.obsidian/plugins`, Gitleaks encontró "API keys" en el `main.js` minificado de un plugin: eran falsos positivos. La solución no fue silenciar a Gitleaks, sino **no versionar el código de los plugins**, que se reinstala desde la tienda, y quedarme solo con su configuración:

```gitignore
.obsidian/plugins/*/*
!.obsidian/plugins/*/manifest.json
!.obsidian/plugins/*/data.json
```

El repo pasó de 22 MB a unos pocos KB, y Gitleaks sigue vigilando los `data.json`, que es donde de verdad podría colarse un secreto.

Otras exclusiones que no deberían faltar en ningún vault con código: `*.tfstate`, `*.tfplan`, `.terraform/`, `*.env`, `*.pfx`, `*.pem` y `*.key`. El state de Terraform puede contener secretos en claro.

---

## Fase 2: convenciones antes que contenido

Este es el paso que más me costó y el que más valor aporta: **definir el esquema antes de escribir una sola nota**. Si cargas contenido primero, luego te toca rehacer el frontmatter a mano.

Definí 14 tipos de nota, cada uno con sus campos y sus estados válidos. Un extracto:

| tipo | Campos propios | Estados |
|---|---|---|
| chuleta | herramienta, verificado, fuente | borrador · revisado |
| recurso-azure | categoria, servicio, verificado, fuente | borrador · revisado |
| modulo-terraform | categoria, recurso, provider-version, repo | borrador · probado · produccion |
| oferta | cliente, fecha-envio | borrador · enviada · ganada · perdida |
| apunte | certificacion, dominio | borrador · repasado |

Los campos `verificado` y `fuente` son los que más aprecio. Azure cambia constantemente, así que cada nota técnica registra **con qué URL oficial y en qué fecha** se validó. Una vez al mes reviso las notas con más de seis meses.

Completé el esquema con dos reglas más:

- **Nombres:** `Git - Deshacer ultimo commit`, `azurerm_key_vault`, `2026-09-23 Oferta Cliente Landing Zone`. La fecha va delante en todo lo que ocurre en un momento concreto.
- **Tags en lista cerrada**, agrupados por pilares WAF, metodologías CAF, herramienta e IA. Un tag nuevo solo existe si antes lo añado a la tabla. Así evito tener `#terraform`, `#Terraform` y `#tf` conviviendo.

Todo vive en una nota, `99-Plantillas/Convenciones.md`, que es la fuente de verdad para mí y, como veremos, también para Claude.

---

## Fase 3: plugins y plantillas

### Pocos plugins y con registro

Instalé 14 plugins de la comunidad. Todos son código de terceros con acceso completo al vault, así que los gobierno como gobernaría dependencias en un proyecto:

- Un script genera `Registro-Plugins.md` leyendo el `manifest.json` de cada plugin: nombre, versión, autor y para qué lo uso.
- Nunca pulso "Actualizar todo". Actualizo de uno en uno, revisando antes el changelog.
- Antes de instalar uno, reviso sus descargas y su fecha de última actualización.

### El router de Templater: la pieza clave

Templater permite asignar una plantilla por carpeta, pero no admite comodines. Eso choca con rutas como `04-Clientes/<cualquier cliente>/01-Ofertas`.

La solución fue **una única plantilla "router" asignada a todo el vault**, que mira dónde se ha creado la nota y aplica la plantilla que le corresponde:

```javascript
<%*
const p = tp.file.folder(true);
const s = p.split("/");
let t = null;
if (s[0] === "00-SysOps" && s.length >= 2) t = "chuleta";
else if (p.startsWith("01-Azure/01-Recursos/")) t = "recurso-azure";
else if (p.startsWith("01-Azure/02-Certificaciones/")) t = "apunte";
else if (s[0] === "02-Terraform" && s.length >= 2) t = "modulo-terraform";
else if (s[0] === "04-Clientes" && s[2] === "01-Ofertas") t = "oferta";
// ...resto de tipos
if (tp.file.title.endsWith(".excalidraw")) t = null;
if (t) { tR += await tp.file.include("[[99-Plantillas/Templater/T-" + t + "]]"); }
-%>
```

Además, cada plantilla **deduce campos de la ruta**. Si creo una nota en `00-SysOps/05-Git`, aparece sola con `tipo: chuleta` y `herramienta: Git`. Si la creo en la carpeta de una certificación, sale con `tipo: apunte` y el código de la certificación ya relleno.

La línea de `.excalidraw` la añadí más tarde, al darme cuenta de que el router aplicaría la plantilla de documento dentro de los ficheros de Excalidraw y los rompería.

### Linter, Git automático y Web Clipper

- **Linter**, con solo dos reglas: mantener `actualizado` al día y normalizar los tags. Con la carpeta de plantillas excluida, porque si no "corrige" los bloques `<% %>` de Templater.
- **Plugin Git:** commit y push automáticos 15 minutos después de dejar de editar. El hook de Gitleaks también se ejecuta en esos commits.
- **Obsidian Web Clipper** en Chrome, apuntando a `98-Documentos/Web-Clipper` con propiedades alineadas con mi esquema. Capturo documentación de Microsoft Learn con un clic y luego la muevo a su sitio.

---

## Fase 5: explotación

### Dashboard con Bases

Una nota `Inicio` se abre al arrancar Obsidian con vistas de Bases incrustadas: ofertas abiertas agrupadas por cliente, proyectos en curso, MVP de IA activos, certificaciones en curso y todo lo que está en borrador pendiente de revisar.

```yaml
filters:
  and:
    - 'tipo == "oferta"'
    - or:
        - 'estado == "borrador"'
        - 'estado == "enviada"'
views:
  - type: table
    name: Ofertas abiertas
    groupBy:
      property: cliente
      direction: ASC
```

Como todo se alimenta del frontmatter, el dashboard nunca se desincroniza.

### Por qué no usé Kanban para las ofertas

Pensé en un tablero Kanban de ofertas, pero lo descarté: mover una tarjeta de "Enviada" a "Ganada" **no cambia el `estado`** de la nota de la oferta. Tendría el estado duplicado en dos sitios, y tarde o temprano el tablero y el dashboard dirían cosas distintas. Kanban quedó solo como tablero de trabajo personal, sin ligarlo a propiedades.

### Flashcards, diagramas y enlaces

- **Spaced Repetition:** cada apunte de certificación lleva una sección de flashcards, y cada certificación se convierte automáticamente en un mazo.
- **Excalidraw con los iconos oficiales de Azure**, descargados del Azure Architecture Center. Microsoft permite usarlos en diagramas de arquitectura, formación y documentación. Los excluyo de Git porque se pueden volver a descargar.
- **Sección `## Relacionado`** en las plantillas, para enlazar un recurso con su módulo Terraform, sus chuletas y los proyectos donde lo usé. El panel de enlaces entrantes hace el resto.

---

## Fase 6: Claude Code como coautor del vault

Esta era la parte que más me interesaba. Descarté la vía del plugin Local REST API con MCP: **Claude Code trabaja directamente sobre los ficheros**, así que no necesitaba ni plugin ni puerto abierto ni API key.

### `CLAUDE.md`: las reglas de la casa

En la raíz del vault hay un `CLAUDE.md` que Claude Code carga en cada sesión. Resumido:

- Leer `Convenciones.md` antes de crear o editar nada.
- Ubicar cada nota según su tipo, usar la plantilla correspondiente sustituyendo las expresiones de Templater y **escribir la nota completa de una vez**. Si creara un fichero vacío, Templater le aplicaría su plantilla encima.
- **Rigor técnico:** toda afirmación sobre Azure, respaldada por Microsoft Learn, con `fuente` y `verificado` rellenos. Si no puede verificar algo, lo dice y añade el tag `revisar`. Nada de inventar límites, SKUs ni precios.
- **Prohibido sin confirmación:** borrar o mover notas, tocar la configuración, hacer commits y mezclar información entre clientes.

### Permisos: defensa en profundidad

El `CLAUDE.md` son instrucciones. Los permisos son la segunda capa:

```json
{
  "permissions": {
    "deny": [
      "Edit(./.obsidian/**)",
      "Edit(./.git/**)",
      "Edit(./99-Plantillas/**)",
      "Bash(git commit:*)",
      "Bash(git push:*)"
    ],
    "ask": ["Bash(Remove-Item:*)", "Bash(Move-Item:*)"]
  }
}
```

Cuando probé a pedirle "haz commit y push", Claude Code lo intentó y **el permiso lo bloqueó**. Aun así, no trato estas reglas como una barrera infalible: la red de seguridad real sigue siendo Git más Gitleaks.

### MCP de Microsoft Learn

Para que la regla de "verificar contra Microsoft Learn" tenga una fuente real detrás, conecté el MCP oficial a nivel de proyecto:

```powershell
claude mcp add --transport http --scope project microsoft-learn https://learn.microsoft.com/api/mcp
```

Un detalle de seguridad: Claude Code también cargó mis conectores de claude.ai (correo, calendario, Drive). Los desactivé para este proyecto. No quiero que el contenido de mi correo acabe volcado en una nota que se sube a GitHub.

### La prueba de fuego

Le pedí: *"Crea la nota del recurso Azure Key Vault verificando los datos en Microsoft Learn"*. Buscó en la documentación oficial, creó la nota en `01-Azure/01-Recursos/Security` con el frontmatter completo, la fuente enlazada y la fecha de verificación. Días después, al preguntarle por los límites de Key Vault, **respondió desde mi propia nota**, citando la fuente, sin volver a buscar en internet.

Eso es exactamente lo que quería: un segundo cerebro que se alimenta de fuentes oficiales y al que puedo consultar en lenguaje natural.

---

## Fase 7: mantenimiento

Un sistema sin mantenimiento se degrada, así que lo automaticé con **tareas recurrentes de Tasks** que aparecen solas en el dashboard:

- **Cada viernes:** vaciar las capturas del Web Clipper, actualizar los estados de ofertas y proyectos, lanzar la copia de binarios y comprobar que Git está limpio.
- **El día 1 de cada mes:** revisar borradores, reverificar notas antiguas, revisar plugins y tags, y archivar clientes inactivos.

La copia de binarios es un script con `robocopy` que **nunca borra en destino**: si un fichero desaparece del portátil por error, la copia lo conserva. La validé como se debe validar una copia de seguridad, restaurando un fichero y comparando su hash con el original. Una copia que no se ha restaurado nunca no es una copia.

---

## Lo que aprendí por el camino

Los errores fueron lo más instructivo:

1. **Algunos ajustes de Obsidian no viven en `data.json`.** El disparador de Templater al crear notas se guarda por dispositivo, así que mi script de configuración no podía activarlo. Tuve que hacerlo a mano.
2. **Una regla de Linter configurada no sirve si su interruptor principal está apagado.** La prueba del paso lo destapó en segundos.
3. **Hacer clic en un enlace a una nota que no existe la crea en la carpeta actual**, con la plantilla equivocada. Ahora mi regla es: primero creo la nota en su sitio y después la enlazo.
4. **Pegar un bloque de prueba dentro del propio script** crea un bucle infinito: el script se llama a sí mismo. Me pasó, y me hizo pensar que la unidad de red estaba colgada.
5. **Las unidades de red mapeadas no existen en todas las sesiones.** Uso siempre la ruta UNC en los scripts.
6. **PowerShell 5.1 y la codificación UTF-8.** Las tildes rotas y la marca BOM en un JSON me recordaron que para estos scripts hay que usar PowerShell 7.

---

## Reflexión final

Lo que más valor me ha dado no ha sido ningún plugin, sino **decidir las convenciones antes del contenido** y **validar cada paso antes de avanzar**. Con un esquema claro, las plantillas, el dashboard y Claude trabajan sobre la misma estructura y no se contradicen.

La IA escribe notas, verifica contra la documentación oficial y responde a mis preguntas. Pero las reglas del vault las decidí yo, y la última revisión antes de usar cualquier dato con un cliente sigue siendo humana.

---

*Si tienes preguntas sobre la configuración o quieres los scripts, puedes contactarme en [luisadanmunoz@outlook.com](mailto:luisadanmunoz@outlook.com).*
