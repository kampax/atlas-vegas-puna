"""Controla que los datos del atlas estén completos y coherentes antes de publicar.

Uso, desde la raíz del repositorio:
    python herramientas/validar_datos.py

Termina con código 0 si no hay errores. Los avisos no bloquean, pero conviene leerlos.
Ver PROCESO.md para saber qué hacer con cada error.
"""
import json
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from actualizar_readme import readme_actualizado  # noqa: E402
from etiquetar_fotos_decisions import PREGUNTAS_NOUL, TIPOS_TOMA  # noqa: E402

try:
    from PIL import Image
except ImportError:  # Pillow es opcional: sin él no se controlan los tamaños
    Image = None

RAIZ = Path(__file__).resolve().parent.parent
CAMPOS = ["id", "fecha", "lat", "lon", "precision", "vega", "ancho", "alto", "altitud",
          "provincia", "departamento", "etiquetas", "tipo_toma", "verdor"]
LADO_FOTO, LADO_MINIATURA = 1600, 480
# Recuadro amplio de la Puna argentina, para detectar coordenadas cambiadas de signo o de lugar
LAT_MIN, LAT_MAX, LON_MIN, LON_MAX = -32.0, -21.5, -70.5, -64.5

errores, avisos = [], []


def clave_nombre(nombre):
    """Forma normalizada de un nombre de vega para detectar variantes del mismo lugar."""
    t = unicodedata.normalize("NFD", nombre).encode("ascii", "ignore").decode().casefold()
    t = re.sub(r"^vega\s+", "", t.strip())
    return re.sub(r"[\s.]+", " ", t).strip()


def tiene_exif(ruta):
    with open(ruta, "rb") as f:
        cabecera = f.read(65536)
    return b"Exif\x00\x00" in cabecera


def main():
    datos = json.loads((RAIZ / "data" / "fotos.json").read_text(encoding="utf-8"))
    fotos, resumen = datos["fotos"], datos["resumen"]
    puntos = {f["properties"]["nombre"] for f in json.loads(
        (RAIZ / "data" / "vegas_muestreadas.geojson").read_text(encoding="utf-8"))["features"]}
    deptos = {(f["properties"]["provincia"], f["properties"]["nombre"]) for f in json.loads(
        (RAIZ / "data" / "departamentos.geojson").read_text(encoding="utf-8"))["features"]}

    # Campos y valores de cada foto
    ids = set()
    for f in fotos:
        fid = f.get("id", "?")
        faltan = [c for c in CAMPOS if c not in f]
        if faltan:
            errores.append(f"{fid}: faltan campos {', '.join(faltan)}")
            continue
        if fid in ids:
            errores.append(f"{fid}: id repetido")
        ids.add(fid)
        # Sin hora se acepta (fotos reenviadas por WhatsApp, que pierden la hora de la toma)
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}( \d{2}:\d{2})?", f["fecha"]):
            errores.append(f"{fid}: fecha con formato inválido ({f['fecha']!r})")
        if f["precision"] not in ("exacta", "aproximada"):
            errores.append(f"{fid}: precision debe ser 'exacta' o 'aproximada'")
        if not (LAT_MIN <= f["lat"] <= LAT_MAX and LON_MIN <= f["lon"] <= LON_MAX):
            errores.append(f"{fid}: coordenadas fuera de la Puna ({f['lat']}, {f['lon']})")
        if (f["provincia"], f["departamento"]) not in deptos:
            errores.append(f"{fid}: departamento desconocido ({f['provincia']} / {f['departamento']})")
        if not isinstance(f["altitud"], int) or not 2000 <= f["altitud"] <= 6500:
            errores.append(f"{fid}: altitud inválida ({f['altitud']!r})")
        if f["vega"] is not None and (not isinstance(f["vega"], str) or not f["vega"].strip()):
            errores.append(f"{fid}: vega debe ser un nombre o null")
        if not set(f["etiquetas"]) <= set(PREGUNTAS_NOUL):
            errores.append(f"{fid}: etiquetas fuera del vocabulario {sorted(set(f['etiquetas']) - set(PREGUNTAS_NOUL))}")
        if f["tipo_toma"] not in TIPOS_TOMA:
            errores.append(f"{fid}: tipo_toma desconocido ({f['tipo_toma']!r})")
        if f["verdor"] not in (1, 2, 3, 4, 5):
            errores.append(f"{fid}: verdor debe ser un entero de 1 a 5")

    # Archivos de imagen
    for carpeta, lado in (("fotos", LADO_FOTO), ("miniaturas", LADO_MINIATURA)):
        en_disco = {p.stem for p in (RAIZ / carpeta).glob("*.jpg")}
        for fid in sorted(ids - en_disco):
            errores.append(f"{fid}: falta {carpeta}/{fid}.jpg")
        for fid in sorted(en_disco - ids):
            avisos.append(f"{carpeta}/{fid}.jpg no figura en data/fotos.json")
        for f in fotos:
            ruta = RAIZ / carpeta / f"{f.get('id')}.jpg"
            if not ruta.exists():
                continue
            if tiene_exif(ruta):
                errores.append(f"{carpeta}/{ruta.name}: conserva metadatos EXIF")
            if Image:
                with Image.open(ruta) as im:
                    w, h = im.size
                if max(w, h) > lado:
                    errores.append(f"{carpeta}/{ruta.name}: mide {w}x{h}, el máximo es {lado} px")
                if carpeta == "fotos" and (w, h) != (f.get("ancho"), f.get("alto")):
                    errores.append(f"{ruta.name}: mide {w}x{h} pero fotos.json dice {f.get('ancho')}x{f.get('alto')}")
    if not Image:
        avisos.append("Pillow no está instalado: no se controlaron los tamaños de las imágenes")

    # Nombres de vegas: variantes del mismo lugar y nombres de punto escritos distinto
    variantes = defaultdict(set)
    for f in fotos:
        if f.get("vega"):
            variantes[clave_nombre(f["vega"])].add(f["vega"])
    for p in puntos:
        variantes[clave_nombre(p)].add(p)
    for grupo in variantes.values():
        if len(grupo) > 1:
            correcto = next((n for n in grupo if n in puntos), None)
            detalle = f" (usar el del punto de muestreo: {correcto!r})" if correcto else ""
            errores.append(f"Nombres de vega que parecen el mismo lugar: {sorted(grupo)}{detalle}")

    # Resumen de cabecera de fotos.json, que el sitio muestra en la portada
    if fotos and all(c in f for f in fotos for c in CAMPOS):
        alts = [f["altitud"] for f in fotos]
        esperado = {
            "total": len(fotos),
            "anio_inicio": min(f["fecha"] for f in fotos)[:4],
            "anio_fin": max(f["fecha"] for f in fotos)[:4],
            "con_gps": sum(f["precision"] == "exacta" for f in fotos),
            "aproximadas": sum(f["precision"] == "aproximada" for f in fotos),
            "altitud_min": min(alts),
            "altitud_max": max(alts),
        }
        for k, v in esperado.items():
            if resumen.get(k) != v:
                errores.append(f"resumen.{k} de fotos.json vale {resumen.get(k)!r} y debería ser {v!r}")

    # README
    actual, nuevo = readme_actualizado()
    if actual != nuevo:
        errores.append("El README está desactualizado: correr python herramientas/actualizar_readme.py")

    for a in avisos:
        print(f"AVISO  {a}")
    for e in errores:
        print(f"ERROR  {e}")
    print(f"\n{len(fotos)} fotos revisadas: {len(errores)} errores, {len(avisos)} avisos.")
    sys.exit(1 if errores else 0)


if __name__ == "__main__":
    main()
