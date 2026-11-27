"""Regenera los bloques <!-- auto:... --> del README a partir de data/fotos.json.

Uso, desde la raíz del repositorio:
    python herramientas/actualizar_readme.py              # reescribe el README
    python herramientas/actualizar_readme.py --verificar  # solo avisa si está desactualizado
"""
import sys
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
README = RAIZ / "README.md"
MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
         "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]


def orden(texto):
    """Orden alfabético sin distinguir mayúsculas ni tildes."""
    sin_tildes = unicodedata.normalize("NFD", texto).encode("ascii", "ignore").decode()
    return sin_tildes.casefold()


def miles(n):
    return f"{n:,}".replace(",", ".")


def campania(mes):
    anio, m = mes.split("-")
    return f"{MESES[int(m) - 1]} de {anio}"


def readme_actualizado():
    """Devuelve (texto actual, texto con los bloques auto regenerados)."""
    fotos = json.loads((RAIZ / "data" / "fotos.json").read_text(encoding="utf-8"))["fotos"]
    geo = json.loads((RAIZ / "data" / "vegas_muestreadas.geojson").read_text(encoding="utf-8"))
    puntos = {f["properties"]["nombre"] for f in geo["features"]}

    fotos_por_mes = Counter(f["fecha"][:7] for f in fotos)
    vegas_por_mes = defaultdict(set)
    meses_por_vega = defaultdict(set)
    for f in fotos:
        if f.get("vega"):
            vegas_por_mes[f["fecha"][:7]].add(f["vega"])
            meses_por_vega[f["vega"]].add(f["fecha"][:7])

    meses = sorted(fotos_por_mes)
    gps = sum(f["precision"] == "exacta" for f in fotos)
    alts = [f["altitud"] for f in fotos if f.get("altitud") is not None]
    comparables = {v: len(m) for v, m in meses_por_vega.items() if len(m) > 1}
    de_muestreo = sum(v in puntos for v in meses_por_vega)

    cifras = "\n".join([
        f"- **{len(fotos)} fotografías** de {len(meses)} campañas de campo, "
        f"entre {meses[0][:4]} y {meses[-1][:4]}.",
        f"- {gps} con la ubicación GPS de la cámara y {len(fotos) - gps} con ubicación aproximada.",
        f"- Altitudes de {miles(min(alts))} a {miles(max(alts))} m s. n. m.",
        f"- {len(meses_por_vega)} vegas identificadas en las fotos ({de_muestreo} de ellas son "
        f"puntos de muestreo); {len(comparables)} fotografiadas en más de una campaña.",
    ])

    filas = ["| Vega | Campañas |", "|---|---:|"]
    for n in sorted(set(comparables.values()), reverse=True):
        nombres = sorted((v for v, c in comparables.items() if c == n), key=orden)
        filas.append(f"| {', '.join(nombres)} | {n} |")
    tabla_comparables = "\n".join(filas)

    filas = ["| Campaña | Fotos | Vegas identificadas |", "|---|---:|---|"]
    for mes in meses:
        vegas = ", ".join(sorted(vegas_por_mes[mes], key=orden))
        filas.append(f"| {campania(mes)} | {fotos_por_mes[mes]} | {vegas} |")
    tabla_campanias = "\n".join(filas)

    deptos = Counter((f["provincia"], f["departamento"]) for f in fotos)
    filas = ["| Provincia | Departamento | Fotos |", "|---|---|---:|"]
    for (prov, depto), n in sorted(deptos.items(), key=lambda x: (orden(x[0][0]), -x[1])):
        filas.append(f"| {prov} | {depto} | {n} |")
    tabla_deptos = "\n".join(filas)

    crudo = README.read_bytes().decode("utf-8")
    fin_linea = "\r\n" if "\r\n" in crudo else "\n"
    texto = crudo.replace("\r\n", "\n")
    for nombre, contenido in [("cifras", cifras), ("comparables", tabla_comparables),
                              ("campanias", tabla_campanias), ("departamentos", tabla_deptos)]:
        patron = re.compile(rf"(<!-- auto:{nombre} -->\n).*?(\n<!-- /auto:{nombre} -->)", re.S)
        texto, n = patron.subn(lambda m: m.group(1) + contenido + m.group(2), texto)
        if n != 1:
            raise SystemExit(f"No se encontró el bloque auto:{nombre} en el README")
    return crudo, texto.replace("\n", fin_linea)


def main():
    actual, nuevo = readme_actualizado()
    if "--verificar" in sys.argv[1:]:
        if actual != nuevo:
            print("El README está desactualizado: correr python herramientas/actualizar_readme.py")
            sys.exit(1)
        print("README al día.")
        return
    if actual == nuevo:
        print("README al día, sin cambios.")
        return
    README.write_bytes(nuevo.encode("utf-8"))
    print("README actualizado.")


if __name__ == "__main__":
    main()
