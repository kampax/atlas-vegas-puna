"""Extrae el texto de cada PDF de la bibliografía a wiki/_texto/<id>.txt con marcas de página.

Uso: python herramientas/wiki/extraer_texto.py "<carpeta con PDFs>"
"""
import os, re, sys, unicodedata
import fitz  # PyMuPDF

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SALIDA = os.path.join(RAIZ, "wiki", "_texto")


def id_de(nombre):
    s = os.path.splitext(nombre)[0]
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s[:80].rstrip("-")


def main(carpeta):
    os.makedirs(SALIDA, exist_ok=True)
    vistos = {}
    for f in sorted(os.listdir(carpeta)):
        if not f.lower().endswith(".pdf"):
            continue
        i = id_de(f)
        if i in vistos:
            i = f"{i}-{len(vistos)}"
        vistos[i] = f
        doc = fitz.open(os.path.join(carpeta, f))
        partes = [f"ARCHIVO: {f}\nID: {i}\nPAGINAS: {len(doc)}\n"]
        for n, p in enumerate(doc, 1):
            partes.append(f"\n=== Página {n} ===\n{p.get_text()}")
        with open(os.path.join(SALIDA, i + ".txt"), "w", encoding="utf-8") as o:
            o.write("".join(partes))
    print(f"{len(vistos)} textos en {SALIDA}")


if __name__ == "__main__":
    main(sys.argv[1])
