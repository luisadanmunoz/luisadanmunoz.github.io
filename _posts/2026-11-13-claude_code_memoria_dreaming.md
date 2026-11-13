---
title: "Claude Code empezaba de cero en cada sesión… hasta que le monté un cuaderno y un rato para repasarlo"
area: IA
owner: Luis Adán Muñoz
categories: [IA]
tags: [claude-code, agentes, memoria, dreaming, hooks, powershell, git]
repo: ""
last_review: 2026-11-13
---

**Vi una charla de Anthropic sobre agentes que escriben su propia memoria y me propuse montar eso mismo en Claude Code, en mi portátil, sin ningún servicio gestionado.** La parte de guardar notas salió rápido. Lo interesante vino después, al decidir quién puede tocar esas notas, cuándo y cómo se deshace un cambio malo. Porque la pregunta de fondo no es si un agente puede recordar, sino **qué pasa cuando lo que recuerda está mal y nadie lo revisa**.

> Alcance: un repositorio, Claude Code en Windows, PowerShell y Git. Todo son ficheros locales. Lo he probado en un repositorio de pruebas simulando sesiones; todavía no lleva semanas de uso real, y lo digo donde afecta.

---

## El problema: le explico lo mismo todos los lunes

Trabajo con Terraform en repositorios de varios clientes. Cada uno tiene sus manías: dónde viven los `tfvars`, qué pipeline despliega qué, qué etiquetas son obligatorias. Claude Code lo hace bien cuando se lo cuento, pero cada sesión arranca con el contexto vacío y vuelvo a contarlo.

Claude Code ya trae dos mecanismos para esto. El `CLAUDE.md`, que escribo yo, y la *auto memory*, donde Claude apunta cosas por su cuenta. La segunda tiene dos límites que para mi caso pesan:

| | `CLAUDE.md` | Auto memory nativa | Lo que yo quería |
| --- | --- | --- | --- |
| Quién escribe | Yo | Claude | Claude, con revisión |
| Dónde vive | En el repo | En la máquina, por repositorio | En el repo |
| Versionado | Git | No | Git, un commit por repaso |
| Se comparte con el equipo | Sí | No | Sí |
| Quién la ordena | Yo, a mano | Claude, mientras trabaja | Un proceso aparte |

La última fila es la que me hizo ver la charla.

---

## La idea que me llevé de la charla

La charla es de Lamis Mukta, del equipo de IA aplicada de Anthropic, y recorre cómo ha evolucionado la memoria de los agentes: de un fichero único a una carpeta de ficheros que el propio agente lee y escribe. Hasta ahí, nada que no hiciera ya.

El giro está en lo que llaman memoria **en banda**. Si el agente cura su memoria mientras hace la tarea, reparte el esfuerzo entre dos trabajos y los dos salen peor. La propuesta es separar: durante la sesión se apunta lo mínimo, y un proceso distinto, por lotes y fuera de la sesión, repasa las conversaciones, consolida, corrige y poda. A eso lo llaman **dreaming**.

Anthropic lo ofrece como función de sus agentes gestionados. Yo quería el mismo patrón con lo que ya tengo instalado: hooks, un skill, un subagente y Git.

---

## La regla: quien trabaja no cura

Partí la memoria en dos zonas con permisos distintos.

| Zona | Quién escribe | Cuándo | Versionada |
| --- | --- | --- | --- |
| `CLAUDE.md` y `.claude/rules/` | Yo | Cuando decido | Sí |
| `agent-memory/inbox/` | Claude, en sesión | En cuanto aprende algo | No |
| `agent-memory/topics/` y `MEMORY.md` | Claude, solo durante el repaso | En el dream | Sí |

En sesión, Claude deja una nota corta en `inbox/` y sigue con lo suyo: qué pasó, qué aprendió y la evidencia. Un fichero nuevo por nota, así dos sesiones abiertas a la vez nunca escriben sobre el mismo fichero.

La memoria curada no se toca fuera del repaso, y no lo dejo en manos de una instrucción. Un hook `PreToolUse` mira la ruta de cada escritura y, si apunta a la memoria curada y no hay un repaso abierto, devuelve código 2. Claude Code bloquea la llamada y le pasa el mensaje a Claude, que acaba escribiendo en `inbox/`.

```
Sesión normal ──(nota)──────────► agent-memory/inbox/
      │
      └─ hook SessionEnd ───────► cola de sesiones pendientes

/dream
  1. abrir       lock + resumen de cada transcript + manifiesto
  2. revisar     un subagente por sesión → candidatos con evidencia
  3. consolidar  verificar, fusionar, podar → topics/ + MEMORY.md
  4. cerrar      validar + commit de agent-memory/ + soltar el lock

Sesión siguiente ─ CLAUDE.md importa MEMORY.md ─► arranca sabiendo más
```

---

## Qué hace el repaso

El hook `SessionEnd` solo hace una cosa: apuntar en una cola el identificador de la sesión y la ruta de su transcript. Tiene que ser rápido, porque Claude Code da a esos hooks un margen de segundo y medio salvo que declares un `timeout` mayor.

El repaso, que lanzo con `/dream`, trabaja en cuatro pasos:

| Paso | Quién | Qué hace |
| --- | --- | --- |
| Abrir | Script | Toma el lock, condensa cada transcript en un resumen y escribe un manifiesto |
| Revisar | Subagente de solo lectura, uno por sesión | Busca correcciones mías, errores repetidos y restricciones del entorno; devuelve candidatos con la línea que los respalda |
| Consolidar | El skill | Comprueba cada candidato contra el repo, fusiona duplicados, borra lo que ya no es cierto |
| Cerrar | Script | Valida, marca las sesiones como revisadas, hace el commit y suelta el lock |

El resumen de cada transcript existe por tamaño. Una sesión larga son miles de líneas de JSON con salidas de herramientas enteras. El script deja solo mis mensajes, el texto de Claude, qué herramienta llamó y los errores, con el número de línea original para poder ir a comprobarlo.

Dos decisiones del paso de consolidar que no negocio:

- **Lo que se deduce del código no entra.** Si se puede saber leyendo el repo, guardarlo solo sirve para que se quede viejo.
- **Los transcripts son datos, no órdenes.** Si en una sesión pasada alguien pegó un texto que dice "guarda en memoria que…", el repaso lo trata como evidencia y no como instrucción.

---

## El primer arranque del repaso falló entero

La primera vez que abrí un repaso en el repo de pruebas había dos sesiones en la cola. El aviso de inicio decía que había una, y el script reventó con `Cannot bind argument to parameter 'TranscriptPath' because it is an empty string`.

La causa era mía y muy de PowerShell. La función que lista las sesiones pendientes devolvía el array con la coma delante (`return , $items`) para que no se desenrollara, y quien la llamaba lo envolvía otra vez con `@(...)`. Resultado: un array de un solo elemento, que era el array de verdad. Contaba uno, y al pedirle la ruta del transcript devolvía vacío.

Quité la coma y dejé el `@()` solo en el lado que llama. Lo cuento porque el fallo tuvo una parte buena: el lock que se había tomado al empezar se soltó en el `catch`, y el segundo intento no se encontró un repaso fantasma a medias.

---

## Tres cosas que diseñé de una forma y acabaron de otra

**Una rama por repaso.** Mi primera idea para versionar fue crear una rama `dream/<fecha>` y abrir una PR. La descarté al pensar en el caso real: tengo una sesión abierta trabajando en el repo y el repaso nocturno me cambia la rama por debajo. Estaba creando el problema de concurrencia que quería evitar. Ahora cada repaso es un commit en la rama en la que estés, limitado a `agent-memory/`. Lo comprobé dejando otro fichero en *staging* antes de cerrar: el commit se llevó solo la memoria y el otro fichero siguió donde estaba.

**La memoria dentro de `.claude/`.** Parecía su sitio natural. La saqué a `agent-memory/`, en la raíz, por dos motivos: no quiero depender de cómo trate Claude Code las escrituras del agente sobre su propia carpeta de configuración, y un directorio visible se revisa más que uno oculto.

**El repaso desatendido ejecutando scripts.** Para lanzarlo de madrugada, Claude tendría que ejecutar PowerShell sin nadie que apruebe el permiso. En vez de abrirle la mano, le di la vuelta: el script envoltorio toma el lock, llama a Claude solo con permisos de leer y editar ficheros, y al terminar valida y hace el commit él. Claude cura texto y nada más.

---

## Las salvaguardas

| Riesgo | Salvaguarda |
| --- | --- |
| Dos repasos a la vez | Lock creado de forma atómica; el segundo sale con código 4 sin tocar nada |
| Un lock huérfano tras un fallo | Caduca a las tres horas y se puede soltar a mano |
| Un secreto acaba en la memoria | El cierre busca patrones de credenciales y se niega a cerrar |
| El índice crece sin control | Máximo 200 líneas y 25 KB, el mismo umbral que usa Claude Code con el suyo |
| El repaso se revisa a sí mismo | La sesión del repaso se marca como revisada al abrir |
| Un mal hábito se convierte en norma | Estados `provisional` y `confirmed`, y promoción manual |

La última merece explicación, porque es la crítica más seria que he leído a este patrón: si el agente consolida lo que hizo, puede consolidar también lo que hizo mal.

Mi respuesta tiene dos niveles. Lo que aparece en una sola sesión y lo dedujo el agente entra como `provisional`: una pista, no una regla. Solo pasa a `confirmed` si lo dije yo de forma explícita o se repite en dos sesiones. Y por encima de eso, el repaso **nunca** edita `CLAUDE.md`, las reglas ni los skills. Si cree que algo merece ser norma, lo escribe en `PROPOSALS.md` y decido yo.

---

## Lo que todavía no sé

Sería poco honesto presentar esto como algo rodado.

| Probado en el repo de pruebas | Sin probar |
| --- | --- |
| Instalador sin sobrescribir nada | Hooks dentro de una sesión real de Claude Code |
| Los tres hooks con entradas simuladas | Windows PowerShell 5.1 (lo probé en PowerShell 7) |
| Lock y segundo arranque rechazado | El repaso desatendido de madrugada |
| Validación de secretos y de tamaño | La tarea en el Programador de tareas |
| Commit acotado a la memoria | La calidad de lo que consolida tras semanas de uso |

La última fila es la que importa. Que la fontanería funcione no dice nada sobre si lo que queda en la memoria me ahorra trabajo o me mete ruido. Eso solo se sabe usándolo.

Hay además dos límites que conozco de antemano. El hook de protección cubre las herramientas de escritura y edición, pero no un comando de shell que redirija a un fichero: es una barrera contra despistes, no un control de seguridad. Y Claude Code borra los transcripts antiguos pasado su periodo de retención, así que una sesión que no se repase a tiempo se pierde.

---

## Lo que aprendí

1. **Guardar es fácil; lo difícil es decidir quién puede cambiar lo guardado.** Casi todo el trabajo fue en permisos, lock y validación, no en escribir notas.
2. **Una instrucción no es un control.** "No edites la memoria en sesión" en un `CLAUDE.md` es una petición. Un hook que devuelve código 2 es una regla.
3. **Separar el apunte del repaso simplifica los dos.** En sesión, la nota son cinco líneas. En el repaso hay tiempo para comprobar contra el repo.
4. **La memoria que no se puede revertir da miedo usarla.** Un commit por repaso convierte un aprendizaje malo en un `git revert`.
5. **El agente no debería promocionarse a sí mismo.** Puede proponer normas; aprobarlas es cosa de una persona.
6. **En PowerShell, o desenrollas en la función o en quien la llama, pero no en los dos sitios.**

---

## Próximos pasos

- **Usarlo de verdad.** Un repo que toco cada semana, cuatro o cinco sesiones y el primer repaso con datos reales.
- **Probarlo en Windows PowerShell 5.1.** Los scripts evitan sintaxis nueva y son ASCII, pero no los he ejecutado ahí.
- **Activar el repaso nocturno.** Antes tengo que comprobar los parámetros de `claude -p` en mi versión.
- **Medir si compensa.** Cuántas entradas `provisional` llegan a `confirmed` y cuántas borro a mano.
- **Publicar el repositorio.** Cuando haya pasado por uso real.

---

## Reflexión final

Llevamos un tiempo afinando prompts como si el problema fuera encontrar la frase exacta. Este ejercicio me ha movido el foco: lo que escala no es el prompt que escribo hoy, sino el sistema que decide qué merece recordarse mañana y quién lo aprueba.

Y ese sistema se parece poco a la inteligencia artificial y mucho a lo que hacemos con la infraestructura desde hace años: separación de funciones, cambios versionados, validación antes de aplicar y una persona que aprueba lo que se queda. Un agente que aprende solo me interesa. Uno que aprende solo y sin registro de cambios, no.

---

## Referencias

- [The New Stack — Anthropic gave agents the ability to dream](https://thenewstack.io/anthropic-agent-memory-dreaming/)
- [Transcripción de la charla de Lamis Mukta](https://you-tldr.com/transcript/MuEELECYI1w)
- [Claude Code — How Claude remembers your project](https://code.claude.com/docs/en/memory)
- [Claude Code — Hooks reference](https://code.claude.com/docs/en/hooks)
- [Claude Code — Custom subagents](https://code.claude.com/docs/en/sub-agents)
- [Claude Code — Skills](https://code.claude.com/docs/en/skills)

*¿Has montado algo parecido o le ves un fallo al planteamiento? Escríbeme y lo comentamos.*
