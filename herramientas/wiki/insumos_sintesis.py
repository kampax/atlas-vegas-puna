"""Prepara, para cada página de síntesis, un archivo con las fichas que le corresponden.

Salida: wiki/_sintesis/_insumos/<faceta>__<slug>.md (versión compacta de las fichas).
Uso: python herramientas/wiki/insumos_sintesis.py
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vocabulario import FACETAS
from construir import leer_fichas, cita_corta, WIKI

# páginas de síntesis que se escriben (las facetas muy genéricas o con 1 documento quedan solo como listado)
PAGINAS = {
    "temas": list(FACETAS["temas"][1]),
    "paises": ["argentina", "bolivia", "chile", "peru", "ecuador", "colombia"],
    "ecosistemas": ["vega", "bofedal", "turbera", "paramo"],
}


def compacta(d):
    l = [f"### [[{d['id']}]] — {cita_corta(d)} — {d['titulo_es']}",
         f"Países: {', '.join(d.get('paises') or [])} | Región: {d.get('region') or '-'} | "
         f"Ecosistemas: {', '.join(d.get('ecosistemas') or [])} | Temas: {', '.join(d.get('temas') or [])}",
         f"Resumen: {d['resumen']}", "Hallazgos:"]
    l += [f"- {h['texto']}" for h in d.get("hallazgos") or []]
    if d.get("datos_clave"):
        l.append("Datos: " + "; ".join(f"{x.get('variable')}: {x.get('valor')} {x.get('unidad') or ''} ({x.get('contexto') or ''})" for x in d["datos_clave"]))
    l.append(f"Relevancia para la Puna argentina: {d['relevancia_puna_argentina']}")
    return "\n".join(l)


if __name__ == "__main__":
    fichas = {i: d for i, d in leer_fichas().items() if not d.get("excluir") and not d.get("duplicado_de")}
    out = os.path.join(WIKI, "_sintesis", "_insumos")
    os.makedirs(out, exist_ok=True)
    for faceta, slugs in PAGINAS.items():
        for s in slugs:
            sel = sorted((d for d in fichas.values() if s in (d.get(faceta) or [])), key=lambda d: d.get("anio") or 0)
            with open(os.path.join(out, f"{faceta}__{s}.md"), "w", encoding="utf-8") as f:
                f.write(f"# Insumos: {faceta} / {s} ({len(sel)} documentos)\n\n" + "\n\n".join(map(compacta, sel)) + "\n")
            print(f"{faceta}__{s}: {len(sel)} docs, ~{os.path.getsize(os.path.join(out, f'{faceta}__{s}.md'))//4000}k tokens")
