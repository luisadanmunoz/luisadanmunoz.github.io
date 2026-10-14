#!/usr/bin/env python3
"""Publicación de artículos del blog en LinkedIn (perfil personal).

Subcomandos:
  preparar  Detecta los artículos nuevos del último merge en main, espera a que estén
            publicados en la web y genera los borradores (texto + enlace + imagen).
  publicar  Publica los borradores en LinkedIn (Posts API + Images API).
  token     Comprueba cuántos días le quedan al token de acceso (introspección).

Solo usa la biblioteca estándar de Python.

Documentación oficial:
  Posts API:   https://learn.microsoft.com/linkedin/marketing/community-management/shares/posts-api
  Images API:  https://learn.microsoft.com/linkedin/marketing/community-management/shares/images-api
  little text: https://learn.microsoft.com/linkedin/marketing/community-management/shares/little-text-format
  userinfo:    https://learn.microsoft.com/linkedin/consumer/integrations/self-serve/sign-in-with-linkedin-v2
  Introspect:  https://learn.microsoft.com/linkedin/shared/authentication/token-introspection
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.linkedin.com"
UA = "luisadanmunoz.es-linkedin/1.0"


# ---------------------------------------------------------------- utilidades
def log(msg):
    print(msg, flush=True)


def resumen(md):
    """Añade texto al resumen del job de GitHub Actions."""
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    if path:
        with open(path, "a", encoding="utf-8") as f:
            f.write(md + "\n")


def salida(nombre, valor):
    path = os.environ.get("GITHUB_OUTPUT")
    if path:
        with open(path, "a", encoding="utf-8") as f:
            f.write(f"{nombre}={valor}\n")


def http(method, url, headers=None, data=None, timeout=60):
    req = urllib.request.Request(url, method=method, data=data, headers={"User-Agent": UA, **(headers or {})})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, dict(r.headers), r.read()
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers), e.read()


def li_headers(token, extra=None):
    return {
        "Authorization": f"Bearer {token}",
        "Linkedin-Version": os.environ.get("LINKEDIN_VERSION") or "202609",
        "X-Restli-Protocol-Version": "2.0.0",
        **(extra or {}),
    }


# little text format: los caracteres reservados se escapan con barra invertida
RESERVADOS = re.compile(r"([\\|{}@\[\]()<>#*_~])")


def escapar(texto):
    return RESERVADOS.sub(r"\\\1", texto)


SIGLAS = {"ai", "ia", "id", "iac", "rbac", "gdap", "csp", "llm", "sql", "aks", "avd", "mfa", "api", "vm", "waf", "caf", "mcp", "rag", "sre", "ci", "cd"}


def hashtag(tag):
    partes = re.split(r"[^0-9A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+", str(tag))
    valor = "".join(p.upper() if p.lower() in SIGLAS else p[:1].upper() + p[1:] for p in partes if p)
    return f"#{valor}" if valor else ""


CATEGORIA_TAG = {"azure": "Azure", "ia": "IA", "noticias": "Azure"}


def componer_texto(art):
    """Texto del post. El artículo puede traer su propio texto en `linkedin:`."""
    propio = art.get("linkedin")
    if isinstance(propio, str) and propio.strip():
        cuerpo = escapar(propio.strip())
    else:
        cuerpo = escapar(art["title"])
        if art.get("description"):
            cuerpo += "\n\n" + escapar(art["description"])
    tags = []
    for t in [CATEGORIA_TAG.get(art.get("categoria", ""), "")] + list(art.get("tags") or []):
        h = hashtag(t)
        if h and h.lower() not in [x.lower() for x in tags]:
            tags.append(h)
    texto = f"{cuerpo}\n\nLo cuento en el blog 👉 {escapar(art['url'])}"
    if tags:
        texto += "\n\n" + " ".join(tags[:5])
    return texto


# ---------------------------------------------------------------- preparar
def articulos_nuevos():
    """Ficheros de _posts añadidos en el último commit de main (merge de PR incluido)."""
    try:
        out = subprocess.check_output(
            ["git", "diff", "--diff-filter=A", "--name-only", "HEAD^1", "HEAD", "--", "_posts/"], text=True
        )
    except subprocess.CalledProcessError:
        return []
    return [l.strip() for l in out.splitlines() if l.strip().endswith((".md", ".markdown", ".html"))]


def leer_manifiesto(site):
    status, _, body = http("GET", f"{site.rstrip('/')}/api/posts.json?t={int(time.time())}")
    if status != 200:
        return None
    return json.loads(body.decode("utf-8"))


def cmd_preparar(a):
    if a.articulo:
        objetivos = [a.articulo.strip()]
    else:
        objetivos = articulos_nuevos()
    if not objetivos:
        log("No hay artículos nuevos en este cambio.")
        resumen("### LinkedIn\nNo hay artículos nuevos en este cambio. No se publica nada.")
        salida("total", "0")
        json.dump([], open(a.salida, "w"))
        return

    log(f"Artículos a preparar: {objetivos}")
    borradores, pendientes = [], list(objetivos)
    limite = time.time() + a.espera * 60
    while pendientes and time.time() < limite:
        man = leer_manifiesto(a.site) or []
        por_path = {m["path"]: m for m in man}
        por_url = {m["url"].rstrip("/"): m for m in man}
        for obj in list(pendientes):
            m = por_path.get(obj) or por_url.get(obj.rstrip("/"))
            if m:
                pendientes.remove(obj)
                if m.get("linkedin") is False:
                    log(f"{obj}: tiene `linkedin: false`, se omite.")
                    continue
                borradores.append({**m, "texto": componer_texto(m)})
        if pendientes:
            log(f"Esperando a que la web publique: {pendientes}")
            time.sleep(30)

    for obj in pendientes:
        log(f"::warning::{obj} no aparece en la web publicada (¿fecha futura o borrador?). Se omite.")

    json.dump(borradores, open(a.salida, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    salida("total", str(len(borradores)))

    md = ["### Borradores para LinkedIn", ""]
    if not borradores:
        md.append("No hay nada que publicar.")
    for b in borradores:
        md += [f"**{b['title']}**  ", f"{b['url']}", "", "```text", b["texto"].replace("\\", ""), "```", ""]
    md.append("Revisa el texto. Si está bien, aprueba el job **publicar** (entorno `linkedin`).")
    resumen("\n".join(md))
    log("\n".join(md))


# ---------------------------------------------------------------- publicar
def persona(token):
    urn = os.environ.get("LINKEDIN_PERSON_URN", "").strip()
    if urn:
        return urn
    status, _, body = http("GET", f"{API}/v2/userinfo", {"Authorization": f"Bearer {token}"})
    if status != 200:
        sys.exit(f"No se pudo obtener el usuario (userinfo {status}): {body[:300]!r}. "
                 "Define el secreto LINKEDIN_PERSON_URN o autoriza el scope openid/profile.")
    return f"urn:li:person:{json.loads(body)['sub']}"


def subir_imagen(token, owner, url_imagen):
    status, _, img = http("GET", url_imagen)
    if status != 200:
        log(f"::warning::No se pudo descargar la imagen {url_imagen} ({status}); se publica sin miniatura.")
        return None
    status, _, body = http(
        "POST", f"{API}/rest/images?action=initializeUpload",
        li_headers(token, {"Content-Type": "application/json"}),
        json.dumps({"initializeUploadRequest": {"owner": owner}}).encode(),
    )
    if status != 200:
        log(f"::warning::initializeUpload {status}: {body[:300]!r}; se publica sin miniatura.")
        return None
    valor = json.loads(body)["value"]
    status, _, body = http("PUT", valor["uploadUrl"], {"Authorization": f"Bearer {token}"}, img, timeout=120)
    if status not in (200, 201):
        log(f"::warning::Subida de imagen {status}: {body[:300]!r}; se publica sin miniatura.")
        return None
    return valor["image"]


def cmd_publicar(a):
    token = os.environ.get("LINKEDIN_ACCESS_TOKEN", "").strip()
    if not token:
        sys.exit("Falta el secreto LINKEDIN_ACCESS_TOKEN.")
    borradores = json.load(open(a.borradores, encoding="utf-8"))
    if not borradores:
        log("Nada que publicar.")
        return
    autor = persona(token)
    md = ["### Publicado en LinkedIn", ""]
    fallos = 0
    for b in borradores:
        articulo = {"source": b["url"], "title": b["title"][:400]}
        if b.get("description"):
            articulo["description"] = b["description"][:4000]
        miniatura = subir_imagen(token, autor, b["image"]) if b.get("image") else None
        if miniatura:
            articulo["thumbnail"] = miniatura
        post = {
            "author": autor,
            "commentary": b["texto"],
            "visibility": "PUBLIC",
            "distribution": {"feedDistribution": "MAIN_FEED", "targetEntities": [], "thirdPartyDistributionChannels": []},
            "content": {"article": articulo},
            "lifecycleState": "PUBLISHED",
            "isReshareDisabledByAuthor": False,
        }
        status, headers, body = http(
            "POST", f"{API}/rest/posts", li_headers(token, {"Content-Type": "application/json"}),
            json.dumps(post, ensure_ascii=False).encode("utf-8"),
        )
        if status == 201:
            urn = headers.get("x-restli-id") or headers.get("X-RestLi-Id") or ""
            enlace = f"https://www.linkedin.com/feed/update/{urn}/" if urn else "(sin URN en la respuesta)"
            log(f"OK {b['title']} -> {enlace}")
            md.append(f"- [{b['title']}]({enlace})")
        else:
            fallos += 1
            log(f"::error::{b['title']}: LinkedIn respondió {status}: {body[:500]!r}")
            md.append(f"- ❌ {b['title']}: error {status}")
            if status == 401:
                md.append("  - El token ha caducado o se ha revocado: ejecuta `Obtener-TokenLinkedIn.ps1` y actualiza el secreto.")
    resumen("\n".join(md))
    if fallos:
        sys.exit(1)


# ---------------------------------------------------------------- token
def cmd_token(a):
    token = os.environ.get("LINKEDIN_ACCESS_TOKEN", "").strip()
    cid = os.environ.get("LINKEDIN_CLIENT_ID", "").strip()
    secreto = os.environ.get("LINKEDIN_CLIENT_SECRET", "").strip()
    if not (token and cid and secreto):
        log("Faltan secretos (LINKEDIN_ACCESS_TOKEN, LINKEDIN_CLIENT_ID, LINKEDIN_CLIENT_SECRET). No se comprueba.")
        salida("dias", "-1")
        return
    datos = urllib.parse.urlencode({"client_id": cid, "client_secret": secreto, "token": token}).encode()
    status, _, body = http("POST", "https://www.linkedin.com/oauth/v2/introspectToken",
                           {"Content-Type": "application/x-www-form-urlencoded"}, datos)
    if status != 200:
        log(f"Introspección {status}: {body[:300]!r}")
        salida("dias", "0")
        return
    info = json.loads(body)
    if not info.get("active"):
        dias = 0
    else:
        dias = int((int(info.get("expires_at", 0)) - time.time()) // 86400)
    log(f"Token activo: {info.get('active')} · caduca en {dias} días · scopes: {info.get('scope')}")
    resumen(f"### Token de LinkedIn\nActivo: **{info.get('active')}** · caduca en **{dias} días**")
    salida("dias", str(dias))


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("preparar")
    s.add_argument("--site", required=True)
    s.add_argument("--salida", default="borradores.json")
    s.add_argument("--articulo", default="")
    s.add_argument("--espera", type=int, default=10, help="minutos máximos esperando a que la web publique")
    s = sub.add_parser("publicar")
    s.add_argument("--borradores", default="borradores.json")
    sub.add_parser("token")
    a = p.parse_args()
    {"preparar": cmd_preparar, "publicar": cmd_publicar, "token": cmd_token}[a.cmd](a)


if __name__ == "__main__":
    main()
