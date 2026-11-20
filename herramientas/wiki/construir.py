"""Construye la wiki de Obsidian y el archivo de conocimiento del bot a partir de las fichas.

Entradas:  wiki/_fichas/*.json            (una ficha por documento)
           wiki/_sintesis/<faceta>/*.md   (síntesis por tema/país/ecosistema; opcional)
Salidas:   wiki/fuentes, wiki/temas, wiki/paises, wiki/ecosistemas, wiki/metodos,
           wiki/glosario.md, wiki/index.md       -> para leer en Obsidian
           wiki/_bot/conocimiento.md             -> lo único que lee el bot

En las síntesis, las citas se escriben como [[<id de ficha>]] y aquí se convierten
en enlaces con autor y año. Uso: python herramientas/wiki/construir.py
"""
import json, math, os, re, shutil, sys, unicodedata
from collections import Counter, defaultdict
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vocabulario import FACETAS

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WIKI = os.path.join(RAIZ, "wiki")
ROTULOS = {"temas": "Temas", "paises": "Países", "ecosistemas": "Ecosistemas", "metodos": "Métodos"}
CARPETAS = ["fuentes"] + [c for c, _ in FACETAS.values()]


def leer_fichas():
    fichas = {}
    for f in sorted(os.listdir(os.path.join(WIKI, "_fichas"))):
        if f.endswith(".json"):
            with open(os.path.join(WIKI, "_fichas", f), encoding="utf-8") as fh:
                d = json.load(fh)
            fichas[d["id"]] = d
    return fichas


def apellido(autor):
    return autor.split(",")[0].strip()


def autores_corto(d):
    a = d.get("autores") or ["Anónimo"]
    if len(a) == 1:
        return apellido(a[0])
    if len(a) == 2:
        return f"{apellido(a[0])} y {apellido(a[1])}"
    return f"{apellido(a[0])} et al."


def cita_corta(d):
    return f"{autores_corto(d)}, {d.get('anio') or 's. f.'}"


def enlace(d):
    return f"[[fuentes/{d['id']}|{cita_corta(d)}]]"


def yaml_lista(v):
    return "[" + ", ".join(json.dumps(x, ensure_ascii=False) for x in v) + "]"


def leer_sintesis(carpeta, slug, fichas):
    ruta = os.path.join(WIKI, "_sintesis", carpeta, slug + ".md")
    if not os.path.exists(ruta):
        return None
    with open(ruta, encoding="utf-8") as f:
        texto = f.read().strip()

    def reemplazo(m):
        i = m.group(1)
        return enlace(fichas[i]) if i in fichas else m.group(0)

    return re.sub(r"\[\[([^\]|/]+)\]\]", reemplazo, texto)


def pagina_fuente(d, fichas):
    fm = ["---", "tipo: fuente", f"aliases: [{json.dumps(cita_corta(d), ensure_ascii=False)}]",
          f"titulo: {json.dumps(d['titulo'], ensure_ascii=False)}",
          f"autores: {yaml_lista(d.get('autores') or [])}", f"anio: {d.get('anio')}",
          f"revista: {json.dumps(d.get('revista'), ensure_ascii=False)}",
          f"doi: {json.dumps(d.get('doi'))}", f"tipo_documento: {d.get('tipo_documento')}",
          f"idioma: {d.get('idioma')}", f"archivo: {json.dumps(d.get('archivo'), ensure_ascii=False)}"]
    for campo in FACETAS:
        fm.append(f"{campo}: {yaml_lista(d.get(campo) or [])}")
    fm.append("---")

    l = fm + ["", f"# {d['titulo_es']}", ""]
    if d.get("titulo_es") != d.get("titulo"):
        l += [f"*{d['titulo']}*", ""]
    l += [f"> {d['cita']}", ""]
    if d.get("doi"):
        l += [f"DOI: [{d['doi']}](https://doi.org/{d['doi']})", ""]
    if d.get("duplicado_de") and d["duplicado_de"] in fichas:
        l += [f"> [!warning] Duplicado de {enlace(fichas[d['duplicado_de']])}", ""]

    lugar = []
    for campo, (carpeta, vocab) in FACETAS.items():
        vals = [f"[[{carpeta}/{v}|{vocab[v]}]]" for v in d.get(campo) or [] if v in vocab]
        if vals:
            lugar.append(f"- **{ROTULOS[carpeta]}:** " + ", ".join(vals))
    if d.get("region"):
        lugar.append(f"- **Región:** {d['region']}")
    if d.get("sitios"):
        lugar.append(f"- **Sitios:** {', '.join(d['sitios'])}")
    alt = d.get("altitud_m") or {}
    if alt.get("min") or alt.get("max"):
        rango = alt.get("min") if alt.get("min") == alt.get("max") else f"{alt.get('min') or '?'}–{alt.get('max') or '?'}"
        lugar.append(f"- **Altitud:** {rango} m s. n. m.")
    l += lugar + ["", "## Resumen", "", d["resumen"], "", "## Hallazgos principales", ""]
    for h in d.get("hallazgos") or []:
        l.append(f"- {h['texto']} (p. {h.get('pagina', '?')})")
    if d.get("datos_clave"):
        l += ["", "## Datos clave", "", "| Variable | Valor | Unidad | Contexto | Pág. |", "|---|---|---|---|---|"]
        for x in d["datos_clave"]:
            fila = [str(x.get(k) or "").replace("|", "/") for k in ("variable", "valor", "unidad", "contexto", "pagina")]
            l.append("| " + " | ".join(fila) + " |")
    if d.get("especies"):
        l += ["", "## Especies", "", ", ".join(f"*{e}*" for e in d["especies"])]
    if d.get("terminos"):
        l += ["", "## Términos definidos", ""]
        for t in d["terminos"]:
            l.append(f"- **{t['termino']}:** {t['definicion']} (p. {t.get('pagina', '?')})")
    l += ["", "## Relevancia para las vegas de la Puna argentina", "", d["relevancia_puna_argentina"]]
    if d.get("limitaciones"):
        l += ["", "## Limitaciones", "", d["limitaciones"]]
    if d.get("notas_calidad"):
        l += ["", f"> [!note] Nota de calidad: {d['notas_calidad']}"]
    return "\n".join(l) + "\n"


def pagina_faceta(carpeta, slug, nombre, ids, fichas):
    l = ["---", f"tipo: {carpeta}", "---", "", f"# {nombre}", ""]
    s = leer_sintesis(carpeta, slug, fichas)
    if s:
        l += [s, ""]
    l += [f"## Fuentes ({len(ids)})", ""]
    for i in sorted(ids, key=lambda x: (-(fichas[x].get("anio") or 0), cita_corta(fichas[x]))):
        d = fichas[i]
        l.append(f"- {enlace(d)} — {d['titulo_es']}")
    return "\n".join(l) + "\n"


def escribir(ruta, texto):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(texto)


def construir():
    fichas = leer_fichas()
    fichas = {i: d for i, d in fichas.items() if not d.get("excluir")}
    validas = {i: d for i, d in fichas.items() if not d.get("duplicado_de")}
    for c in CARPETAS:
        shutil.rmtree(os.path.join(WIKI, c), ignore_errors=True)

    for d in fichas.values():
        escribir(os.path.join(WIKI, "fuentes", d["id"] + ".md"), pagina_fuente(d, fichas))

    indice = defaultdict(lambda: defaultdict(list))
    for i, d in validas.items():
        for campo in FACETAS:
            for v in d.get(campo) or []:
                indice[campo][v].append(i)
    for campo, (carpeta, vocab) in FACETAS.items():
        for slug, nombre in vocab.items():
            if indice[campo][slug]:
                escribir(os.path.join(WIKI, carpeta, slug + ".md"),
                         pagina_faceta(carpeta, slug, nombre, indice[campo][slug], validas))

    # glosario: definiciones que dan los propios documentos
    glos = defaultdict(list)
    for d in validas.values():
        for t in d.get("terminos") or []:
            glos[t["termino"].strip().lower()].append((t["definicion"], d, t.get("pagina")))
    g = ["---", "tipo: glosario", "---", "", "# Glosario", "",
         "Definiciones tal como las dan los documentos de la bibliografía.", ""]
    for termino in sorted(glos):
        g += [f"## {termino.capitalize()}", ""]
        for defi, d, p in glos[termino]:
            g.append(f"- {defi} — {enlace(d)}, p. {p or '?'}")
        g.append("")
    escribir(os.path.join(WIKI, "glosario.md"), "\n".join(g))

    # índice
    anios = [d["anio"] for d in validas.values() if d.get("anio")]
    ix = ["# Wiki de vegas y bofedales andinos", "",
          f"{len(validas)} documentos ({min(anios)}–{max(anios)}). Construida el {date.today():%d/%m/%Y} "
          "a partir de `_fichas/`; no editar a mano las páginas generadas (ver `CLAUDE.md`).", ""]
    for campo, (carpeta, vocab) in FACETAS.items():
        ix += [f"## {ROTULOS[carpeta]}", ""]
        for slug, nombre in vocab.items():
            if indice[campo][slug]:
                ix.append(f"- [[{carpeta}/{slug}|{nombre}]] ({len(indice[campo][slug])})")
        ix.append("")
    ix += ["## Otros", "", "- [[glosario|Glosario]]", "", "## Todas las fuentes", ""]
    for d in sorted(validas.values(), key=lambda d: cita_corta(d)):
        ix.append(f"- {enlace(d)} — {d['titulo_es']}")
    escribir(os.path.join(WIKI, "index.md"), "\n".join(ix) + "\n")

    exportar_bibliografia(validas)
    exportar_bot(validas)
    n_frag = exportar_indice_rag(validas)
    print(f"Wiki: {len(fichas)} fuentes ({len(fichas) - len(validas)} duplicadas), "
          f"{sum(1 for c in indice.values() for ids in c.values() if ids)} páginas de facetas, "
          f"{n_frag} fragmentos RAG")


def exportar_bibliografia(fichas):
    """Genera BIBLIOGRAFIA.md en la raíz del repo con título, año, DOI y temática."""
    temas_rotulo = FACETAS["temas"][1]
    docs = sorted(fichas.values(), key=lambda d: (-(d.get("anio") or 0), d.get("titulo") or ""))
    anios = [d["anio"] for d in docs if d.get("anio")]
    lineas = [
        "# Bibliografía del chatbot (Doña Vicuña)",
        "",
        f"Listado de los **{len(docs)} documentos científicos** ({min(anios)}–{max(anios)}) "
        "sobre vegas, bofedales, turberas y humedales altoandinos utilizados como base de conocimiento del chat.",
        "",
        "¿Conocés algún trabajo que falte? Podés sugerirlo abriendo un **Issue** en este repositorio "
        "con el título, año y DOI (o enlace) del artículo.",
        "",
        "| Autores | Año | Título | DOI | Temática general |",
        "|---|---:|---|---|---|",
    ]
    for d in docs:
        autores = autores_corto(d).replace("|", "/")
        anio = d.get("anio") or "s. f."
        titulo = (d.get("titulo") or d.get("titulo_es") or "").replace("|", "/").replace("\n", " ").strip()
        doi = d.get("doi")
        doi_celda = f"[{doi}](https://doi.org/{doi})" if doi else "—"
        temas = ", ".join(temas_rotulo.get(t, t) for t in (d.get("temas") or [])) or "—"
        lineas.append(f"| {autores} | {anio} | {titulo} | {doi_celda} | {temas} |")
    lineas += ["", "*Archivo generado automáticamente a partir de la base bibliográfica local.*", ""]
    escribir(os.path.join(RAIZ, "BIBLIOGRAFIA.md"), "\n".join(lineas))


MESES_ES = ("", "enero", "febrero", "marzo", "abril", "mayo", "junio",
            "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")


def estacion_de(mes):
    if mes == 12 or mes <= 2:
        return "verano"
    if mes <= 5:
        return "otoño"
    if mes <= 8:
        return "invierno"
    return "primavera"


def resumen_atlas_fotos():
    """Genera un resumen compacto de data/fotos.json para el conocimiento del bot."""
    ruta = os.path.join(RAIZ, "data", "fotos.json")
    if not os.path.exists(ruta):
        return []
    with open(ruta, encoding="utf-8") as f:
        datos = json.load(f)
    res = datos.get("resumen") or {}
    fotos = datos.get("fotos") or []

    por_vega = defaultdict(list)
    por_depto = defaultdict(int)
    sin_vega = 0
    for ft in fotos:
        por_depto[(ft.get("provincia") or "?", ft.get("departamento") or "?")] += 1
        v = ft.get("vega")
        if v:
            por_vega[v].append(ft)
        else:
            sin_vega += 1

    l = [
        "# DATOS DEL ATLAS FOTOGRÁFICO (data/fotos.json)",
        "",
        "Fuente: Atlas de vegas de la Puna argentina (data/fotos.json).",
        f"Total: {res.get('total', len(fotos))} fotografías ({res.get('anio_inicio')}–{res.get('anio_fin')}), "
        f"{res.get('con_gps')} con GPS exacto y {res.get('aproximadas')} con ubicación aproximada; "
        f"altitud de {res.get('altitud_min')} a {res.get('altitud_max')} m s. n. m. "
        f"Hay {len(por_vega)} vegas reconocidas ({len(fotos) - sin_vega} fotos asociadas a una vega a menos de 3 km; "
        f"{sin_vega} fotos sin vega asignada).",
        "",
        "Fotos por provincia y departamento: " + "; ".join(
            f"{prov} — {dep}: {n}" for (prov, dep), n in sorted(por_depto.items(), key=lambda x: (-x[1], x[0]))
        ) + ".",
        "",
        "## Vegas con fotografías en el atlas",
        "",
    ]
    for vega in sorted(por_vega, key=lambda v: (-len(por_vega[v]), v)):
        grupo = por_vega[vega]
        alts = [ft["altitud"] for ft in grupo if ft.get("altitud") is not None]
        alt_txt = (f"{min(alts)} m" if min(alts) == max(alts) else f"{min(alts)}–{max(alts)} m") if alts else "s/d"
        exactas = sum(1 for ft in grupo if ft.get("precision") == "exacta")
        lugares = sorted({f"{ft.get('departamento')}, {ft.get('provincia')}" for ft in grupo if ft.get("provincia")})
        camps = defaultdict(int)
        estaciones = set()
        for ft in grupo:
            fecha = ft.get("fecha") or ""
            m = re.match(r"^(\d{4})-(\d{2})", fecha)
            if m:
                anio, mes = int(m.group(1)), int(m.group(2))
                est = estacion_de(mes)
                estaciones.add(est)
                camps[(anio, mes, est)] += 1
        camps_txt = "; ".join(
            f"{MESES_ES[mes]} {anio} ({est}): {n}"
            for (anio, mes, est), n in sorted(camps.items())
        )
        est_txt = ", ".join(sorted(estaciones))
        l.append(
            f"- **{vega}**: {len(grupo)} fotos ({exactas} con GPS exacto, {len(grupo) - exactas} aproximadas) | "
            f"Ubicación: {'; '.join(lugares)} | Altitud: {alt_txt} s. n. m. | "
            f"Estaciones: {est_txt} | Campañas ({len(camps)}): {camps_txt}."
        )
    l.append("")
    return l


def exportar_bot(fichas):
    """Texto compacto que el bot recibe como contexto. Es lo único que el bot conoce."""
    l = ["# BASE DE CONOCIMIENTO: vegas, bofedales y humedales altoandinos", "",
         "Cada documento empieza con [REF: Autor, año]. Citar siempre con esa referencia.", ""]
    l += resumen_atlas_fotos()
    for campo, (carpeta, vocab) in FACETAS.items():
        for slug, nombre in vocab.items():
            s = leer_sintesis(carpeta, slug, fichas)
            if s:
                s = re.sub(r"\[\[fuentes/[^|\]]+\|([^\]]+)\]\]", r"(\1)", s)
                l += [f"## Síntesis — {nombre}", "", s, ""]
    l += ["# DOCUMENTOS", ""]
    for d in sorted(fichas.values(), key=cita_corta):
        l.append(f"## [REF: {cita_corta(d)}] {d['titulo_es']}")
        l.append(f"Cita: {d['cita']}")
        meta = []
        if d.get("paises"):
            meta.append("Países: " + ", ".join(d["paises"]))
        if d.get("region"):
            meta.append("Región: " + d["region"])
        if d.get("sitios"):
            meta.append("Sitios: " + ", ".join(d["sitios"]))
        if d.get("ecosistemas"):
            meta.append("Ecosistemas: " + ", ".join(d["ecosistemas"]))
        alt = d.get("altitud_m") or {}
        if alt.get("min") or alt.get("max"):
            meta.append(f"Altitud: {alt.get('min') or '?'}-{alt.get('max') or '?'} m")
        l.append(" | ".join(meta))
        l.append(f"Resumen: {d['resumen']}")
        l.append("Hallazgos:")
        l += [f"- {h['texto']}" for h in d.get("hallazgos") or []]
        if d.get("datos_clave"):
            l.append("Datos: " + "; ".join(
                f"{x.get('variable')}: {x.get('valor')} {x.get('unidad') or ''} ({x.get('contexto') or ''})".strip()
                for x in d["datos_clave"]))
        if d.get("especies"):
            l.append("Especies: " + ", ".join(d["especies"]))
        if d.get("terminos"):
            l.append("Definiciones: " + " ".join(f"{t['termino']}: {t['definicion']}" for t in d["terminos"]))
        l.append(f"Relevancia para la Puna argentina: {d['relevancia_puna_argentina']}")
        l.append("")
    texto = "\n".join(l)
    escribir(os.path.join(WIKI, "_bot", "conocimiento.md"), texto)
    # módulo que importa el Worker del bot (bot/conocimiento.js, excluido de git)
    escribir(os.path.join(RAIZ, "bot", "conocimiento.js"),
             "// Generado por herramientas/wiki/construir.py a partir de la wiki. No editar.\n"
             f"export default {json.dumps(texto, ensure_ascii=False)};\n")


# --- Índice RAG (BM25) ---
# La normalización y raíz simple de abajo debe mantenerse idéntica a la de bot/rag.js.
STOPWORDS_ES = {
    "el", "la", "los", "las", "un", "una", "unos", "unas", "de", "del", "al",
    "en", "con", "por", "para", "sin", "sobre", "entre", "hacia", "desde",
    "hasta", "segun", "como", "que", "cual", "cuales", "quien", "quienes",
    "donde", "cuando", "cuanto", "cuanta", "cuantos", "cuantas", "porque",
    "pero", "sino", "aunque", "mientras", "si", "no", "ni", "mas", "muy",
    "tan", "tanto", "todo", "toda", "todos", "todas", "otro", "otra", "otros",
    "otras", "este", "esta", "estos", "estas", "ese", "esa", "esos", "esas",
    "aquel", "aquella", "aquellos", "aquellas", "su", "sus", "mi", "mis",
    "tu", "tus", "nuestro", "nuestra", "nuestros", "nuestras", "nos", "me",
    "te", "se", "le", "les", "lo", "ser", "es", "son", "era", "eran", "fue",
    "fueron", "sido", "estar", "estan", "estaba", "hay", "haber", "ha", "han",
    "habia", "tener", "tiene", "tienen", "hacer", "hace", "hacen", "puede",
    "pueden", "poder", "asi", "tambien", "solo", "ya", "aun", "aqui", "alli",
    "ahi", "bien", "mal", "cada", "uno", "dos", "tres", "vez", "veces", "esto",
    "eso", "aquello", "algo", "nada", "alguien", "nadie", "mucho", "mucha",
    "muchos", "muchas", "poco", "poca", "pocos", "pocas", "mismo", "misma",
    "mismos", "mismas", "bajo", "ante", "tras", "contra", "durante", "mediante",
    "respecto", "acerca", "traves", "mas", "menos", "donde", "cuyo", "cuya",
    "alguno", "alguna", "algunos", "algunas", "ninguno", "ninguna", "embargo",
    "ademas", "incluso", "luego", "entonces", "pues", "sea", "sean", "sus",
}

SUFIJOS_ES = (
    "aciones", "iciones", "amiento", "imiento", "idades", "adores", "adoras",
    "ancias", "encias", "acion", "icion", "mente", "ibles", "ables", "ismos",
    "istas", "anzas", "antes", "entes", "ando", "iendo", "ados", "adas",
    "idos", "idas", "ivos", "ivas", "icos", "icas", "osos", "osas", "ales",
    "ares", "eros", "eras", "idad", "able", "ible", "ismo", "ista", "anza",
    "ante", "ente",
)


def quitar_tildes(texto):
    norm = unicodedata.normalize("NFD", texto.lower())
    return "".join(c for c in norm if unicodedata.category(c) != "Mn")


def raiz_es(w):
    if len(w) < 5 or w.isdigit():
        return w
    for suf in SUFIJOS_ES:
        if w.endswith(suf) and len(w) - len(suf) >= 3:
            return w[:-len(suf)]
    if w.endswith("ces") and len(w) >= 5:
        return w[:-3] + "z"
    if w.endswith("es") and len(w) >= 5 and w[-3] in "lrndjz":
        return w[:-2]
    if w.endswith("s") and len(w) >= 4 and w[-2] in "aeiou":
        return w[:-1]
    return w


def tokenizar_es(texto):
    limpio = quitar_tildes(texto)
    out = []
    for w in re.findall(r"[a-z0-9]{2,}", limpio):
        if w in STOPWORDS_ES:
            continue
        r = raiz_es(w)
        if len(r) >= 2 and r not in STOPWORDS_ES:
            out.append(r)
    return out


def _palabras(s):
    return len(s.split())


def _estimar_tokens(texto, cita, titulo):
    return math.ceil((len(texto) + len(cita) + len(titulo) + 90) / 4)


def _agrupar_bloques(bloques, min_pal=300, max_pal=550, solap_bloques=1):
    """Agrupa pares (etiqueta_seccion, texto_bloque) en fragmentos de ~300-550 palabras
    con solapamiento de bloques completos, respetando párrafos/ítems."""
    if not bloques:
        return []
    total_pal = sum(_palabras(t) for _, t in bloques)
    if total_pal <= max_pal:
        seccs = list(dict.fromkeys(s for s, _ in bloques if s))
        return [(", ".join(seccs), "\n".join(t for _, t in bloques))]

    frags = []
    i = 0
    n = len(bloques)
    while i < n:
        actual = []
        pal = 0
        j = i
        while j < n:
            w = _palabras(bloques[j][1])
            if actual and pal + w > max_pal and pal >= min_pal:
                break
            actual.append(bloques[j])
            pal += w
            j += 1
            if pal >= max_pal:
                break
        seccs = list(dict.fromkeys(s for s, _ in actual if s))
        frags.append((", ".join(seccs), "\n".join(t for _, t in actual)))
        if j >= n:
            break
        # Retroceder solap_bloques para solapamiento, garantizando avance
        siguiente = max(i + 1, j - solap_bloques)
        # Si lo que queda es muy corto (<160 palabras), sumarlo al último si no se pasa mucho
        restante = sum(_palabras(t) for _, t in bloques[j:])
        if restante < 160 and pal + restante <= max_pal + 140:
            actual.extend(bloques[j:])
            seccs = list(dict.fromkeys(s for s, _ in actual if s))
            frags[-1] = (", ".join(seccs), "\n".join(t for _, t in actual))
            break
        i = siguiente
    return frags


def _fragmentos_atlas():
    lineas = resumen_atlas_fotos()
    if not lineas:
        return []
    encabezado = []
    vegas = []
    en_vegas = False
    for l in lineas:
        if l.startswith("## Vegas con fotografías"):
            en_vegas = True
            continue
        if not en_vegas:
            if l.strip() and not l.startswith("# DATOS DEL ATLAS"):
                encabezado.append(l)
        elif l.strip():
            vegas.append(l)

    resumen_corto = "\n".join(encabezado)
    bloques = [("Resumen del atlas", resumen_corto)] + [("Vegas con fotografías", v) for v in vegas]
    grupos = _agrupar_bloques(bloques, min_pal=300, max_pal=480, solap_bloques=2)
    out = []
    for idx, (secc, txt) in enumerate(grupos):
        if idx > 0:
            txt = "Atlas fotográfico de vegas de la Puna argentina (data/fotos.json) — continuación:\n" + txt
        cita = "Atlas de vegas de la Puna argentina (data/fotos.json)."
        titulo = "Datos del Atlas fotográfico de vegas de la Puna argentina"
        out.append({
            "id": f"atlas:{idx}",
            "ref": "Atlas fotográfico (data/fotos.json)",
            "titulo": titulo,
            "cita": cita,
            "paises": ["argentina"],
            "seccion": f"Datos del Atlas fotográfico (parte {idx + 1})" if len(grupos) > 1 else "Datos del Atlas fotográfico",
            "texto": txt,
            "tok": _estimar_tokens(txt, cita, titulo),
        })
    return out


def _fragmentos_documento(d):
    ref = cita_corta(d)
    meta = []
    if d.get("paises"):
        meta.append("Países: " + ", ".join(d["paises"]))
    if d.get("region"):
        meta.append("Región: " + d["region"])
    if d.get("sitios"):
        meta.append("Sitios: " + ", ".join(d["sitios"]))
    if d.get("ecosistemas"):
        meta.append("Ecosistemas: " + ", ".join(d["ecosistemas"]))
    alt = d.get("altitud_m") or {}
    if alt.get("min") or alt.get("max"):
        meta.append(f"Altitud: {alt.get('min') or '?'}-{alt.get('max') or '?'} m")
    meta_txt = " | ".join(meta)

    bloques = []
    if meta_txt:
        bloques.append(("Metadatos", meta_txt))
    if d.get("resumen"):
        bloques.append(("Resumen", f"Resumen: {d['resumen']}"))
    hallazgos = d.get("hallazgos") or []
    if hallazgos:
        bloques.append(("Hallazgos", "Hallazgos:\n- " + hallazgos[0]["texto"]))
        for h in hallazgos[1:]:
            bloques.append(("Hallazgos", f"- {h['texto']}"))
    if d.get("datos_clave"):
        datos_txt = "Datos: " + "; ".join(
            f"{x.get('variable')}: {x.get('valor')} {x.get('unidad') or ''} ({x.get('contexto') or ''})".strip()
            for x in d["datos_clave"])
        bloques.append(("Datos clave", datos_txt))
    if d.get("especies"):
        bloques.append(("Especies", "Especies: " + ", ".join(d["especies"])))
    if d.get("terminos"):
        bloques.append(("Definiciones", "Definiciones: " + " ".join(
            f"{t['termino']}: {t['definicion']}" for t in d["terminos"])))
    if d.get("relevancia_puna_argentina"):
        bloques.append(("Relevancia Puna argentina", f"Relevancia para la Puna argentina: {d['relevancia_puna_argentina']}"))

    grupos = _agrupar_bloques(bloques, min_pal=300, max_pal=520, solap_bloques=2)
    out = []
    for idx, (secc, txt) in enumerate(grupos):
        if idx > 0 and meta_txt and not txt.startswith("Países:"):
            txt = f"{meta_txt}\n{txt}"
        out.append({
            "id": f"doc:{d['id']}:{idx}",
            "ref": ref,
            "titulo": d["titulo_es"],
            "cita": d["cita"],
            "paises": d.get("paises") or [],
            "seccion": secc or "Documento",
            "texto": txt,
            "tok": _estimar_tokens(txt, d["cita"], d["titulo_es"]),
        })
    return out


def _fragmentos_sintesis(carpeta, slug, nombre, fichas):
    ruta = os.path.join(WIKI, "_sintesis", carpeta, slug + ".md")
    if not os.path.exists(ruta):
        return []
    with open(ruta, encoding="utf-8") as f:
        crudo = f.read().strip()
    if not crudo:
        return []

    # Dividir respetando encabezados ## y párrafos
    bloques = []
    secc_actual = "Panorama"
    for par in re.split(r"\n\s*\n", crudo):
        par = par.strip()
        if not par:
            continue
        m = re.match(r"^##+\s+(.+)$", par)
        if m:
            secc_actual = m.group(1).strip()
            continue
        # Si un párrafo arranca con encabezado pegado sin línea en blanco
        lineas = par.split("\n")
        m0 = re.match(r"^##+\s+(.+)$", lineas[0].strip())
        if m0:
            secc_actual = m0.group(1).strip()
            resto = "\n".join(lineas[1:]).strip()
            if resto:
                bloques.append((secc_actual, f"### {secc_actual}\n{resto}"))
        else:
            bloques.append((secc_actual, par))

    grupos = _agrupar_bloques(bloques, min_pal=300, max_pal=520, solap_bloques=1)
    out = []
    paises = [slug] if carpeta == "paises" else []
    for idx, (secc, txt_crudo) in enumerate(grupos):
        ids_citados = list(dict.fromkeys(re.findall(r"\[\[([^\]|/]+)\]\]", txt_crudo)))
        citas_ref = [fichas[i]["cita"] for i in ids_citados if i in fichas and fichas[i].get("cita")]

        def reemplazo(m):
            i = m.group(1)
            return f"({cita_corta(fichas[i])})" if i in fichas else m.group(0)

        txt = re.sub(r"\[\[([^\]|/]+)\]\]", reemplazo, txt_crudo)
        cita = "\n".join(citas_ref) if citas_ref else f"Síntesis temática de la wiki ({nombre})."
        titulo = f"Síntesis — {nombre}"
        out.append({
            "id": f"sin:{carpeta}:{slug}:{idx}",
            "ref": titulo,
            "titulo": titulo,
            "cita": cita,
            "paises": paises,
            "seccion": secc or nombre,
            "texto": txt,
            "tok": _estimar_tokens(txt, cita, titulo),
        })
    return out


def exportar_indice_rag(fichas):
    """Genera bot/indice_rag.js con fragmentos y estructuras precalculadas para BM25."""
    fragmentos = []
    fragmentos.extend(_fragmentos_atlas())
    for campo, (carpeta, vocab) in FACETAS.items():
        for slug, nombre in vocab.items():
            fragmentos.extend(_fragmentos_sintesis(carpeta, slug, nombre, fichas))
    for d in sorted(fichas.values(), key=cita_corta):
        fragmentos.extend(_fragmentos_documento(d))

    n = len(fragmentos)
    dl = []
    df = Counter()
    postings = defaultdict(list)

    for idx, f in enumerate(fragmentos):
        # Repetir título y metadatos una vez para dar leve prioridad a coincidencias en título/país/ref
        base_busq = " ".join([
            f["titulo"], f["titulo"], f["ref"], " ".join(f["paises"]), f["seccion"], f["texto"]
        ])
        toks = tokenizar_es(base_busq)
        dl.append(len(toks))
        tf = Counter(toks)
        for term, cnt in tf.items():
            df[term] += 1
            postings[term].extend((idx, cnt))

    avgdl = round(sum(dl) / n, 2) if n else 0.0
    idf = {
        term: round(math.log(1.0 + (n - freq + 0.5) / (freq + 0.5)), 4)
        for term, freq in sorted(df.items())
    }
    postings_ord = {term: postings[term] for term in sorted(postings)}

    indice = {
        "version": 1,
        "k1": 1.5,
        "b": 0.75,
        "avgdl": avgdl,
        "n": n,
        "idf": idf,
        "postings": postings_ord,
        "dl": dl,
        "fragmentos": fragmentos,
    }
    escribir(os.path.join(RAIZ, "bot", "indice_rag.js"),
             "// Generado por herramientas/wiki/construir.py para búsqueda BM25 (modo RAG). No editar.\n"
             f"export default {json.dumps(indice, ensure_ascii=False, separators=(',', ':'))};\n")
    agregar_vectores()
    return n


def agregar_vectores():
    """Agrega los embeddings (bge-m3, con caché en wiki/_bot/vectores.json) a bot/indice_rag.js.

    Sin Node, sin red o sin credenciales de Cloudflare el índice queda como está y el bot usa solo BM25.
    """
    import shutil as _sh, subprocess
    node = _sh.which("node")
    if not node:
        print("Aviso: no se encontró Node.js; indice_rag.js queda sin vectores (solo BM25).")
        return
    script = os.path.join(RAIZ, "herramientas", "wiki", "embeddings.mjs")
    try:
        subprocess.run([node, script], cwd=RAIZ, check=False, timeout=900)
    except Exception as e:  # nunca rompe el build
        print(f"Aviso: no se agregaron vectores ({e}); el modo rag usará solo BM25.")


if __name__ == "__main__":
    construir()
