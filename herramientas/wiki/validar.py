"""Valida las fichas de wiki/_fichas contra el esquema y los textos de wiki/_texto.

Uso: python herramientas/wiki/validar.py
Sale con código 1 si hay errores; los avisos no bloquean.
"""
import json, os, re, sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vocabulario import FACETAS, TIPOS_DOCUMENTO, IDIOMAS

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WIKI = os.path.join(RAIZ, "wiki")

OBLIGATORIOS = ["id", "archivo", "tipo_documento", "titulo", "titulo_es", "autores", "anio",
                "idioma", "cita", "paises", "ecosistemas", "temas", "metodos", "resumen",
                "hallazgos", "relevancia_puna_argentina"]


def paginas_de(i):
    with open(os.path.join(WIKI, "_texto", i + ".txt"), encoding="utf-8") as f:
        m = re.search(r"PAGINAS: (\d+)", f.read(500))
    return int(m.group(1)) if m else 10**6


def validar():
    errores, avisos = defaultdict(list), defaultdict(list)
    textos = {f[:-4] for f in os.listdir(os.path.join(WIKI, "_texto"))}
    fichas = {}
    for f in sorted(os.listdir(os.path.join(WIKI, "_fichas"))):
        if not f.endswith(".json"):
            continue
        i = f[:-5]
        try:
            with open(os.path.join(WIKI, "_fichas", f), encoding="utf-8") as fh:
                d = json.load(fh)
        except Exception as e:
            errores[i].append(f"JSON inválido: {e}")
            continue
        fichas[i] = d
        if d.get("id") != i:
            errores[i].append(f"id '{d.get('id')}' no coincide con el archivo")
        if i not in textos:
            errores[i].append("no hay texto en _texto con ese id")
        if d.get("excluir"):
            avisos[i].append("excluida de la wiki: " + str(d.get("notas_calidad")))
            continue
        for c in OBLIGATORIOS:
            if d.get(c) in (None, "", []) and c not in ("metodos",):
                errores[i].append(f"falta '{c}'")
        for campo, (_, vocab) in FACETAS.items():
            for v in d.get(campo) or []:
                if v not in vocab:
                    errores[i].append(f"{campo}: valor fuera de vocabulario '{v}'")
        if d.get("tipo_documento") not in TIPOS_DOCUMENTO:
            errores[i].append(f"tipo_documento inválido '{d.get('tipo_documento')}'")
        if d.get("idioma") not in IDIOMAS:
            errores[i].append(f"idioma inválido '{d.get('idioma')}'")
        if not 1 <= len(d.get("temas") or []) <= 4:
            avisos[i].append(f"{len(d.get('temas') or [])} temas (se esperan 1 a 4)")
        n = len(d.get("hallazgos") or [])
        if not 4 <= n <= 8:
            avisos[i].append(f"{n} hallazgos (se esperan 4 a 8)")
        maxp = paginas_de(i) if i in textos else 10**6
        for h in (d.get("hallazgos") or []) + (d.get("datos_clave") or []) + (d.get("terminos") or []):
            p = h.get("pagina")
            if p is not None and (not isinstance(p, int) or not 1 <= p <= maxp):
                errores[i].append(f"página fuera de rango: {p} (el texto tiene {maxp})")
        palabras = len((d.get("resumen") or "").split())
        if not 100 <= palabras <= 320:
            avisos[i].append(f"resumen de {palabras} palabras")
        a = d.get("anio")
        if a is not None and not (isinstance(a, int) and 1900 <= a <= 2026):
            errores[i].append(f"año inválido: {a}")
        dup = d.get("duplicado_de")
        if dup and dup not in textos:
            errores[i].append(f"duplicado_de apunta a un id inexistente: {dup}")

    # duplicados por DOI o título
    por_clave = defaultdict(list)
    for i, d in fichas.items():
        for clave in (d.get("doi") or "", re.sub(r"\W+", "", (d.get("titulo") or "").lower())[:60]):
            if clave:
                por_clave[clave.lower()].append(i)
    for clave, ids in por_clave.items():
        if len(ids) > 1:
            for i in ids:
                avisos[i].append(f"posible duplicado de {', '.join(x for x in ids if x != i)}")

    faltan = sorted(textos - set(fichas))
    return fichas, errores, avisos, faltan


if __name__ == "__main__":
    fichas, errores, avisos, faltan = validar()
    for nombre, grupo in (("ERROR", errores), ("aviso", avisos)):
        for i in sorted(grupo):
            for m in dict.fromkeys(grupo[i]):
                print(f"{nombre:5} {i}: {m}")
    print(f"\n{len(fichas)} fichas, {sum(map(len, errores.values()))} errores, "
          f"{sum(map(len, avisos.values()))} avisos, {len(faltan)} textos sin ficha")
    if faltan:
        print("Sin ficha:", ", ".join(faltan))

    # citas de las síntesis: cada [[id]] debe ser una ficha válida (no excluida)
    validas = {i for i, d in fichas.items() if not d.get("excluir")}
    malas, n_citas = 0, 0
    base = os.path.join(WIKI, "_sintesis")
    for faceta in ("temas", "paises", "ecosistemas"):
        carpeta = os.path.join(base, faceta)
        for f in sorted(os.listdir(carpeta)) if os.path.isdir(carpeta) else []:
            with open(os.path.join(carpeta, f), encoding="utf-8") as fh:
                ids = re.findall(r"\[\[([^\]|]+)\]\]", fh.read())
            n_citas += len(ids)
            for i in sorted(set(ids) - validas):
                print(f"ERROR síntesis {faceta}/{f}: cita inexistente o excluida [[{i}]]")
                malas += 1
    if n_citas:
        print(f"Síntesis: {n_citas} citas, {malas} inválidas")
    sys.exit(1 if errores or malas else 0)
