"""Ingesta automática de nuevos PDFs a la wiki bibliográfica y al conocimiento del bot.

Flujo por cada PDF en la carpeta de entrada (por defecto `wiki/_entrantes/`):
  1. Extrae el texto por páginas (PyMuPDF).
  2. Verifica si está duplicado contra las fichas existentes (DOI, título, id).
  3. Evalúa con DeepSeek si trata sobre vegas, bofedales o humedales altoandinos;
     si no es pertinente, lo mueve a `_descartados/`.
  4. Genera la ficha JSON siguiendo `wiki/_esquema.md` y `vocabulario.py`, y la valida.
  5. Actualiza los insumos y las síntesis afectadas en `wiki/_sintesis/`.
  6. Ejecuta `validar.py` y `construir.py` para actualizar la wiki y `bot/conocimiento.js`.
  7. Mueve los PDFs incorporados a `_procesados/`.

Uso:
  python herramientas/wiki/ingestar_nuevos.py
  python herramientas/wiki/ingestar_nuevos.py "otra/carpeta" --sin-sintesis
  python herramientas/wiki/ingestar_nuevos.py --dry-run
"""
import argparse
import difflib
import json
import os
import re
import shutil
import sys
import urllib.error
import urllib.request

try:
    import pymupdf
except ImportError:  # pragma: no cover
    import fitz as pymupdf

DIR_WIKI_TOOLS = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, DIR_WIKI_TOOLS)

from construir import WIKI, RAIZ, construir, leer_fichas  # noqa: E402
from extraer_texto import SALIDA as DIR_TEXTO, id_de  # noqa: E402
from insumos_sintesis import PAGINAS, compacta  # noqa: E402
from validar import validar  # noqa: E402
from vocabulario import ECOSISTEMAS, FACETAS, IDIOMAS, METODOS, PAISES, TEMAS, TIPOS_DOCUMENTO  # noqa: E402

DIR_FICHAS = os.path.join(WIKI, "_fichas")
DIR_ENTRADA_DEFECTO = os.path.join(WIKI, "_entrantes")
API_DEEPSEEK = "https://api.deepseek.com/chat/completions"
MAX_CHARS_TEXTO = 360_000


def cargar_api_key():
    key = os.environ.get("DEEPSEEK_API_KEY", "").strip()
    if key:
        return key
    dev_vars = os.path.join(RAIZ, "bot", ".dev.vars")
    if os.path.exists(dev_vars):
        with open(dev_vars, encoding="utf-8") as f:
            for linea in f:
                m = re.match(r'^\s*DEEPSEEK_API_KEY\s*=\s*"?([^"\r\n]+)"?\s*$', linea)
                if m:
                    return m.group(1).strip()
    raise RuntimeError(
        "Falta DEEPSEEK_API_KEY (definila como variable de entorno o en bot/.dev.vars)."
    )


def llamar_deepseek(api_key, modelo, mensajes, json_mode=False, max_tokens=4000):
    cuerpo = {
        "model": modelo,
        "messages": mensajes,
        "thinking": {"type": "disabled"},
        "temperature": 0.2,
        "max_tokens": max_tokens,
    }
    if json_mode:
        cuerpo["response_format"] = {"type": "json_object"}
    req = urllib.request.Request(
        API_DEEPSEEK,
        data=json.dumps(cuerpo).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            datos = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detalle = e.read().decode("utf-8", errors="replace")[:400]
        raise RuntimeError(f"Error HTTP {e.code} de DeepSeek: {detalle}") from e
    except urllib.error.URLError as e:
        raise RuntimeError(f"Error de red al consultar DeepSeek: {e.reason}") from e
    return datos["choices"][0]["message"]["content"]


def normalizar_texto(s):
    return re.sub(r"\W+", " ", (s or "").lower()).strip()


def extraer_pdf(ruta_pdf):
    doc = pymupdf.open(ruta_pdf)
    paginas = []
    for n, p in enumerate(doc, 1):
        paginas.append(f"\n=== Página {n} ===\n{p.get_text()}")
    return len(doc), "".join(paginas)


def extraer_dois(texto):
    crudos = re.findall(r"10\.\d{4,9}/[^\s\"'<>\]\)]+", texto[:20_000])
    return {c.rstrip(".,;:)") .lower() for c in crudos}


def buscar_duplicado(fichas, doi_candidatos=None, titulo=None, texto_inicio=None):
    doi_candidatos = {d.lower() for d in (doi_candidatos or []) if d}
    tit_norm = normalizar_texto(titulo)
    inicio_norm = normalizar_texto(texto_inicio)[:1500] if texto_inicio else ""

    for fid, f in fichas.items():
        f_doi = (f.get("doi") or "").strip().lower()
        if f_doi and f_doi in doi_candidatos:
            return fid, f"mismo DOI ({f_doi})"
        for campo in ("titulo", "titulo_es"):
            ft = normalizar_texto(f.get(campo))
            if not ft or len(ft) < 15:
                continue
            if tit_norm and difflib.SequenceMatcher(None, tit_norm, ft).ratio() >= 0.88:
                return fid, f"título coincidente ({f.get('titulo')})"
            if inicio_norm and ft in inicio_norm:
                return fid, f"título presente en la primera página ({f.get('titulo')})"
    return None, None


def id_unico(base, existentes):
    if base not in existentes:
        return base
    n = 2
    while f"{base}-{n}" in existentes:
        n += 1
    return f"{base}-{n}"


def preparar_texto_llm(texto):
    if len(texto) <= MAX_CHARS_TEXTO:
        return texto
    mitad_ini = 220_000
    mitad_fin = 140_000
    return (
        texto[:mitad_ini]
        + "\n\n[... SECCIÓN INTERMEDIA OMITIDA POR LONGITUD ...]\n\n"
        + texto[-mitad_fin:]
    )


def prompt_ficha(fid, archivo, n_paginas, texto_con_paginas):
    vocab = {
        "tipo_documento": sorted(TIPOS_DOCUMENTO),
        "idioma": sorted(IDIOMAS),
        "paises": list(PAISES.keys()),
        "ecosistemas": list(ECOSISTEMAS.keys()),
        "temas": list(TEMAS.keys()),
        "metodos": list(METODOS.keys()),
    }
    return f"""Analizá el siguiente documento académico (ID: {fid}, archivo: {archivo}, {n_paginas} páginas).

Primero determiná si es un trabajo pertinente para una wiki sobre vegas, bofedales, turberas y humedales altoandinos/andinos (incluye ecología, hidrología, vegetación, fauna, microbiología, suelos/turba, carbono, paleoambiente, arqueología pastoral, pastoreo, comunidades/gobernanza, minería/agua, cambio climático, teledetección o conservación en estos ecosistemas).
Si NO trata sobre humedales ni ambientes andinos (por ejemplo, se coló por la palabra "Vega", trata de otra región del mundo sin aporte comparativo directo, o es otro tema ajeno), marcá "es_pertinente": false y explicá brevemente en "motivo_descarte".

Si "es_pertinente" es true, generá el objeto "ficha" en JSON válido siguiendo ESTRICTAMENTE estas reglas:
1. No inventes datos, cifras, autores ni páginas. Si un dato no consta, usá null o [].
2. Escribí todo en español claro con palabras propias (no traduzcas literal ni copies oraciones).
3. Cada hallazgo, dato_clave y termino debe indicar "pagina" como entero entre 1 y {n_paginas} según las marcas "=== Página N ===".
4. Vocabularios cerrados (usá SOLO estos valores exactos):
{json.dumps(vocab, ensure_ascii=False, indent=2)}
5. "temas": entre 1 y 4 valores. "hallazgos": entre 4 y 8 ítems autocontenidos. "resumen": 150 a 250 palabras.
6. "autores": lista como ["Apellido, Iniciales.", ...] (si hay más de 20, los 19 primeros y el último). "anio": entero entre 1900 y 2026 (o null si no consta).
7. "doi": sin prefijo https://doi.org/ (o null). "cita": cita completa en formato APA 7.

Respondé ÚNICAMENTE con un JSON con esta estructura:
{{
  "es_pertinente": true,
  "motivo_descarte": null,
  "ficha": {{
    "id": "{fid}",
    "archivo": "{archivo}",
    "tipo_documento": "articulo",
    "titulo": "...",
    "titulo_es": "...",
    "autores": ["..."],
    "anio": 2024,
    "revista": null,
    "volumen_paginas": null,
    "doi": null,
    "idioma": "es",
    "cita": "...",
    "paises": ["argentina"],
    "region": "...",
    "sitios": ["..."],
    "altitud_m": {{"min": null, "max": null}},
    "ecosistemas": ["vega"],
    "temas": ["hidrologia"],
    "metodos": ["hidrologia-de-campo"],
    "resumen": "...",
    "hallazgos": [{{"texto": "...", "pagina": 1}}],
    "datos_clave": [{{"variable": "...", "valor": "...", "unidad": "...", "contexto": "...", "pagina": 1}}],
    "especies": ["..."],
    "terminos": [{{"termino": "...", "definicion": "...", "pagina": 1}}],
    "relevancia_puna_argentina": "...",
    "limitaciones": null,
    "duplicado_de": null,
    "notas_calidad": null
  }}
}}

DOCUMENTO:
{preparar_texto_llm(texto_con_paginas)}"""


def validar_ficha_local(d, n_paginas):
    errs = []
    oblig = ["id", "archivo", "tipo_documento", "titulo", "titulo_es", "autores", "anio",
             "idioma", "cita", "paises", "ecosistemas", "temas", "resumen",
             "hallazgos", "relevancia_puna_argentina"]
    for c in oblig:
        if d.get(c) in (None, "", []):
            errs.append(f"falta '{c}'")
    for campo, (_, vocab) in FACETAS.items():
        for v in d.get(campo) or []:
            if v not in vocab:
                errs.append(f"{campo}: valor inválido '{v}'")
    if d.get("tipo_documento") not in TIPOS_DOCUMENTO:
        errs.append(f"tipo_documento inválido '{d.get('tipo_documento')}'")
    if d.get("idioma") not in IDIOMAS:
        errs.append(f"idioma inválido '{d.get('idioma')}'")
    for h in (d.get("hallazgos") or []) + (d.get("datos_clave") or []) + (d.get("terminos") or []):
        p = h.get("pagina")
        if p is not None and (not isinstance(p, int) or not 1 <= p <= n_paginas):
            errs.append(f"página fuera de rango: {p} (1..{n_paginas})")
    a = d.get("anio")
    if a is not None and not (isinstance(a, int) and 1900 <= a <= 2026):
        errs.append(f"año inválido: {a}")
    return errs


def mover_a(ruta_pdf, subcarpeta):
    os.makedirs(subcarpeta, exist_ok=True)
    destino = os.path.join(subcarpeta, os.path.basename(ruta_pdf))
    if os.path.exists(destino):
        base, ext = os.path.splitext(os.path.basename(ruta_pdf))
        n = 2
        while os.path.exists(os.path.join(subcarpeta, f"{base}-{n}{ext}")):
            n += 1
        destino = os.path.join(subcarpeta, f"{base}-{n}{ext}")
    shutil.move(ruta_pdf, destino)
    return destino


def actualizar_insumos(fichas_validas, afectados):
    out = os.path.join(WIKI, "_sintesis", "_insumos")
    os.makedirs(out, exist_ok=True)
    for faceta, slug in sorted(afectados):
        if slug not in PAGINAS.get(faceta, []):
            continue
        sel = sorted((d for d in fichas_validas.values() if slug in (d.get(faceta) or [])),
                     key=lambda d: d.get("anio") or 0)
        ruta = os.path.join(out, f"{faceta}__{slug}.md")
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(f"# Insumos: {faceta} / {slug} ({len(sel)} documentos)\n\n" + "\n\n".join(map(compacta, sel)) + "\n")


def actualizar_sintesis(api_key, modelo, faceta, slug, nuevas_fichas, fichas_validas):
    ruta = os.path.join(WIKI, "_sintesis", faceta, f"{slug}.md")
    if not os.path.exists(ruta):
        return False
    with open(ruta, encoding="utf-8") as f:
        actual = f.read().strip()
    aportes = "\n\n".join(compacta(d) for d in nuevas_fichas)
    prompt = f"""Actualizá la siguiente página de síntesis de la wiki (`{faceta}/{slug}`) incorporando los aportes de las fichas nuevas.

REGLAS OBLIGATORIAS:
- Mantené el contenido y las citas `[[<id>]]` existentes salvo que debas integrar nueva evidencia o contrastar resultados.
- Toda afirmación nueva debe citar su ficha exacta como `[[<id>]]` (ej. `[[{nuevas_fichas[0]['id']}]]`). Nunca escribas "Autor et al." a mano.
- Solo usá información presente en la síntesis actual y en las fichas nuevas.
- Mantené la estructura con encabezados `##` (sin título `#` de primer nivel), el tono claro en español y la sección final `## Qué significa para las vegas de la Puna argentina`.
- Devolvé únicamente el Markdown actualizado, sin bloques de código ni comentarios extra.

=== SÍNTESIS ACTUAL ===
{actual}

=== FICHAS NUEVAS A INCORPORAR ===
{aportes}"""
    nuevo_md = llamar_deepseek(api_key, modelo, [{"role": "user", "content": prompt}], max_tokens=4500).strip()
    citas = set(re.findall(r"\[\[([^\]|/]+)\]\]", nuevo_md))
    invalidas = citas - set(fichas_validas)
    if invalidas or not nuevo_md:
        raise RuntimeError(f"Síntesis {faceta}/{slug} generó citas inválidas: {sorted(invalidas)}")
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(nuevo_md + "\n")
    return True


def asegurar_carpeta_entrada(carpeta):
    os.makedirs(carpeta, exist_ok=True)
    leeme = os.path.join(carpeta, "README.txt")
    if not os.path.exists(leeme):
        with open(leeme, "w", encoding="utf-8") as f:
            f.write(
                "Colocá acá los archivos .pdf nuevos que quieras sumar a la wiki.\n"
                "Luego ejecutá desde la raíz del repo:\n"
                "  python herramientas/wiki/ingestar_nuevos.py\n\n"
                "Subcarpetas automáticas:\n"
                "  _procesados/  PDFs incorporados a la wiki\n"
                "  _duplicados/  PDFs repetidos respecto a fichas ya existentes\n"
                "  _descartados/ PDFs que no tratan sobre vegas/bofedales o sin texto legible\n"
            )


def main():
    parser = argparse.ArgumentParser(description="Ingesta automática de PDFs nuevos a la wiki.")
    parser.add_argument("carpeta", nargs="?", default=DIR_ENTRADA_DEFECTO,
                        help="Carpeta con los PDFs nuevos (por defecto wiki/_entrantes)")
    parser.add_argument("--modelo", default=os.environ.get("DEEPSEEK_MODELO", "deepseek-flash"),
                        help="Modelo de DeepSeek (por defecto deepseek-flash)")
    parser.add_argument("--sin-sintesis", action="store_true",
                        help="No actualizar las páginas de síntesis (solo fichas, validación y build)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Evalúa duplicados y pertinencia sin escribir archivos ni mover PDFs")
    args = parser.parse_args()

    carpeta = os.path.abspath(args.carpeta)
    asegurar_carpeta_entrada(carpeta)
    pdfs = sorted(f for f in os.listdir(carpeta)
                  if f.lower().endswith(".pdf") and os.path.isfile(os.path.join(carpeta, f)))
    if not pdfs:
        print(f"No hay PDFs nuevos en {carpeta}")
        return 0

    api_key = cargar_api_key()
    fichas = leer_fichas()
    ids_existentes = set(fichas) | {f[:-4] for f in os.listdir(DIR_TEXTO) if f.endswith(".txt")}

    incorporadas = []
    duplicados = []
    descartados = []

    for nombre in pdfs:
        ruta_pdf = os.path.join(carpeta, nombre)
        print(f"\n==> Procesando {nombre}...")
        try:
            n_pag, texto_paginas = extraer_pdf(ruta_pdf)
        except Exception as e:
            print(f"  ERROR leyendo PDF: {e}")
            continue

        if len(re.findall(r"[A-Za-zÁÉÍÓÚáéíóúÑñ]", texto_paginas)) < 200:
            print("  DESCARTADO: el PDF no tiene texto extraíble (posible escaneo sin OCR).")
            descartados.append((nombre, "sin texto extraíble"))
            if not args.dry_run:
                mover_a(ruta_pdf, os.path.join(carpeta, "_descartados"))
            continue

        dois = extraer_dois(texto_paginas)
        dup_id, dup_motivo = buscar_duplicado(fichas, doi_candidatos=dois, texto_inicio=texto_paginas)
        if dup_id:
            print(f"  DUPLICADO de '{dup_id}' ({dup_motivo}).")
            duplicados.append((nombre, dup_id))
            if not args.dry_run:
                mover_a(ruta_pdf, os.path.join(carpeta, "_duplicados"))
            continue

        fid = id_unico(id_de(nombre), ids_existentes)
        ids_existentes.add(fid)

        try:
            resp_raw = llamar_deepseek(
                api_key, args.modelo,
                [{"role": "user", "content": prompt_ficha(fid, nombre, n_pag, texto_paginas)}],
                json_mode=True, max_tokens=4500,
            )
            res = json.loads(resp_raw)
        except Exception as e:
            print(f"  ERROR generando ficha ({e}); reintentando una vez...")
            try:
                resp_raw = llamar_deepseek(
                    api_key, args.modelo,
                    [{"role": "user", "content": prompt_ficha(fid, nombre, n_pag, texto_paginas)}],
                    json_mode=True, max_tokens=6000,
                )
                res = json.loads(resp_raw)
            except Exception as e2:
                print(f"  ERROR definitivo en '{nombre}': {e2}; se omite y sigue.")
                continue

        if not res.get("es_pertinente"):
            motivo = res.get("motivo_descarte") or "fuera de tema (no trata humedales altoandinos)"
            print(f"  DESCARTADO: {motivo}")
            descartados.append((nombre, motivo))
            if not args.dry_run:
                mover_a(ruta_pdf, os.path.join(carpeta, "_descartados"))
            continue

        ficha = res.get("ficha") or {}
        ficha["id"] = fid
        ficha["archivo"] = nombre

        dup_id2, dup_motivo2 = buscar_duplicado(
            fichas, doi_candidatos=[ficha.get("doi")], titulo=ficha.get("titulo")
        )
        if dup_id2:
            print(f"  DUPLICADO de '{dup_id2}' ({dup_motivo2}).")
            duplicados.append((nombre, dup_id2))
            if not args.dry_run:
                mover_a(ruta_pdf, os.path.join(carpeta, "_duplicados"))
            continue

        errs = validar_ficha_local(ficha, n_pag)
        if errs:
            print(f"  Corrigiendo errores de esquema: {errs}")
            fix_raw = llamar_deepseek(
                api_key, args.modelo,
                [{"role": "user", "content": (
                    f"Corregí únicamente los errores listados en este JSON de ficha (máx página {n_pag}):\n"
                    f"Errores: {errs}\n\nJSON actual:\n{json.dumps(ficha, ensure_ascii=False)}"
                )}],
                json_mode=True, max_tokens=4500,
            )
            ficha = json.loads(fix_raw)
            ficha["id"] = fid
            ficha["archivo"] = nombre
            errs = validar_ficha_local(ficha, n_pag)
            if errs:
                print(f"  ERROR: la ficha siguió con errores ({errs}); se deja el PDF sin mover.")
                continue

        print(f"  ACEPTADO como '{fid}': {ficha.get('titulo_es')}")
        if not args.dry_run:
            os.makedirs(DIR_TEXTO, exist_ok=True)
            with open(os.path.join(DIR_TEXTO, f"{fid}.txt"), "w", encoding="utf-8") as f:
                f.write(f"ARCHIVO: {nombre}\nID: {fid}\nPAGINAS: {n_pag}\n{texto_paginas}")
            os.makedirs(DIR_FICHAS, exist_ok=True)
            with open(os.path.join(DIR_FICHAS, f"{fid}.json"), "w", encoding="utf-8") as f:
                json.dump(ficha, f, ensure_ascii=False, indent=2)
                f.write("\n")
            mover_a(ruta_pdf, os.path.join(carpeta, "_procesados"))
        fichas[fid] = ficha
        incorporadas.append(ficha)

    if incorporadas and not args.dry_run:
        fichas_validas = {i: d for i, d in fichas.items() if not d.get("excluir") and not d.get("duplicado_de")}
        afectados = set()
        por_pagina = {}
        for d in incorporadas:
            for faceta in ("temas", "paises", "ecosistemas"):
                for slug in d.get(faceta) or []:
                    afectados.add((faceta, slug))
                    por_pagina.setdefault((faceta, slug), []).append(d)

        print("\n==> Actualizando insumos de síntesis...")
        actualizar_insumos(fichas_validas, afectados)

        if not args.sin_sintesis:
            print("==> Actualizando síntesis afectadas...")
            for faceta, slug in sorted(afectados):
                if slug not in PAGINAS.get(faceta, []):
                    continue
                try:
                    if actualizar_sintesis(api_key, args.modelo, faceta, slug, por_pagina[(faceta, slug)], fichas_validas):
                        print(f"  Síntesis actualizada: {faceta}/{slug}")
                except Exception as e:
                    print(f"  Aviso: no se actualizó {faceta}/{slug} ({e})")

        print("\n==> Validando y reconstruyendo wiki + bot/conocimiento.js...")
        _, errores, _, _ = validar()
        if errores:
            print(f"ERRORES de validación: {dict(errores)}")
            return 1
        construir()

    print("\n=== Resumen ===")
    print(f"Incorporados: {len(incorporadas)} | Duplicados: {len(duplicados)} | Descartados: {len(descartados)}")
    if incorporadas and not args.dry_run:
        print("Para actualizar el bot publicado en Cloudflare: cd bot && npx wrangler deploy")
    return 0


if __name__ == "__main__":
    sys.exit(main())
