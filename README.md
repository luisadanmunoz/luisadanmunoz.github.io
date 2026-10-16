# luisadanmunoz.es

Web y blog técnico de Luis Adán Muñoz: Azure, Terraform e IA con Microsoft Foundry.
Sitio estático con [Jekyll](https://jekyllrb.com), publicado en GitHub Pages con GitHub Actions
y servido en `https://luisadanmunoz.es` a través de Cloudflare.

## Cómo está organizado

| Ruta | Qué contiene |
|---|---|
| `_config.yml` | Datos generales: título, redes, usuario de Buttondown y colores de las categorías |
| `_posts/` | Artículos, uno por fichero Markdown |
| `_recursos/<indice>/` | Fichas de recursos de Azure, una por fichero, agrupadas en 18 índices |
| `_data/recursos.yml` | Nombre, orden y texto de cada índice de Recursos |
| `_data/perfil.yml` | Contenido de la página Sobre mí (experiencia, proyectos, CV, foto) |
| `_layouts/`, `_includes/` | Plantillas HTML |
| `assets/css/main.css` | Estilos (paleta, tipografía, componentes) |
| `assets/js/main.js` | Menús, filtros, botón Copiar e índice del artículo |
| `assets/img/` | Logo, imagen de portada e imagen para compartir |
| `resource/` | Fichas antiguas del blog anterior. No se publican; sirven de base para completar `_recursos/` |

## Publicar un artículo

Crea `_posts/AAAA-MM-DD-titulo-corto.md`:

```markdown
---
title: "Título del artículo"
description: "Una o dos frases que aparecen en los listados y al compartir."
categoria: azure          # noticias | azure | ia
tema: "Terraform"         # etiqueta que se ve en la portada y en los filtros
last_review: 2026-10-14
versiones: "azurerm 4.x y Terraform 1.9"   # opcional
fuentes:                  # opcional, se listan al final
  - titulo: "Documentación oficial"
    url: https://learn.microsoft.com/...
mermaid: false            # true si usas diagramas mermaid
linkedin: "Texto propio para LinkedIn"   # opcional; false para no publicarlo
---

Texto en Markdown.

Párrafo con una decisión importante.
{: .decision}

Párrafo con algo a vigilar.
{: .ojo}
```

Al hacer push a `main`, la web se construye y publica sola en uno o dos minutos.

## Documentar un recurso

Cada recurso ya tiene su fichero en `_recursos/<indice>/<recurso>.md`. Para documentarlo:

1. Escribe el contenido debajo de la cabecera.
2. Cambia `estado` a `en-curso` o `documentado`.
3. Rellena `last_review` y, si quieres, `fuentes`.

Para añadir un recurso nuevo, copia una ficha existente del mismo índice y cambia `title`, `resumen` y `orden`.
Para añadir un índice nuevo, añádelo a `_data/recursos.yml`, crea `recursos/<slug>/index.html`
copiando uno existente y crea la carpeta `_recursos/<slug>/`.

## Probar en local

Necesitas Ruby 3.3 y Bundler.

```powershell
bundle install
bundle exec jekyll serve --livereload
# abre http://localhost:4000
```

## SEO

- Cada artículo necesita `description` (150-160 caracteres): es el texto que sale en Google y al compartir.
- Al documentar una ficha de recurso, añade también `description` en su cabecera.
- `sitemap.xml` y `robots.txt` son propios. Las fichas de recursos en estado `proximamente` llevan `noindex` y no
  entran en el sitemap; en cuanto pasan a `en-curso` o `documentado` se indexan solas.
- Datos estructurados: artículos y páginas (jekyll-seo-tag), ruta de navegación en artículos y fichas, y persona en Sobre mí.
- Imagen al compartir por defecto: `assets/img/og-default.jpg` (1200×630). Un artículo puede usar otra con `image:`.

## Publicar en LinkedIn

Cada artículo nuevo que llega a `main` se prepara para LinkedIn y **espera tu aprobación**:

1. Al terminar de publicarse la web, el workflow **Publicar en LinkedIn** detecta los artículos añadidos,
   espera a que estén en línea y genera el borrador (título, descripción, enlace e imagen del artículo).
2. El texto aparece en el resumen del job **preparar**. El job **publicar** queda en espera.
3. Si te gusta, pulsa **Review deployments → Approve**. Si no, **Reject** y no se publica nada.

Para un artículo concreto: Actions → *Publicar en LinkedIn* → *Run workflow*, con la ruta del artículo
(deja marcado *Solo preparar el borrador* para ver el texto sin publicar).

En la cabecera del artículo: `linkedin: "texto"` usa ese texto; `linkedin: false` no lo publica.

### Configuración (una vez)

1. En https://www.linkedin.com/developers/apps crea una app y añade los productos
   **Share on LinkedIn** y **Sign In with LinkedIn using OpenID Connect**.
   En *Auth*, añade la URL de redirección `http://localhost:8765/callback`.
2. En GitHub → Settings → Environments, crea el entorno `linkedin` y añade tu usuario en
   **Required reviewers**.
3. Obtén el token y guarda los secretos (necesita GitHub CLI con `gh auth login`):

   ```powershell
   ./.github/scripts/Obtener-TokenLinkedIn.ps1 -ClientId '<client id>' -GuardarEnGitHub
   ```

El token dura 60 días. Cada lunes el workflow *LinkedIn: aviso de caducidad del token* lo comprueba y
abre una incidencia cuando quedan 14 días o menos; para renovarlo, vuelve a ejecutar el script.
Opcional: variable de repositorio `LINKEDIN_VERSION` (por defecto `202609`) para la versión de la API.

## Dominio y publicación

- Settings → Pages → Source: **GitHub Actions**.
- Settings → Pages → Custom domain: `luisadanmunoz.es`, con **Enforce HTTPS** activado.
- DNS en Cloudflare: registros A/AAAA de GitHub Pages en la raíz y CNAME `www` → `luisadanmunoz.github.io`.
- Copia del blog anterior en la rama `backup-blog-antiguo`.
