#!/usr/bin/env python3
"""Etiquetado ecológico automático del Atlas Fotográfico de Vegas de la Puna Argentina
usando la Gemini Decisions API (gemini-decision-1).

Evalúa en una sola llamada por foto:
  - 7 preguntas binarias (type="noul") de presencia/ausencia ecológica
  - 1 pregunta de clasificación (type="choice") de tipo de toma
  - 1 rúbrica ordenada (type="score") de verdor / cobertura vegetal (1 a 5)

Guarda las respuestas completas (probabilidades y confidence) en
herramientas/etiquetas_decisions_raw.json para reanudar sin reprocesar,
exporta los casos en zona gris a herramientas/revision_dudosas.csv y, con
--aplicar-json, fusiona las etiquetas limpias en data/fotos.json.

Requiere:
  - google-genai >= 3.2.0
  - Variable de entorno GEMINI_API_KEY (nunca hardcodeada ni commiteada)
"""

from __future__ import annotations

import argparse
import base64
import csv
import json
import os
import sys
import threading
import time
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

RAIZ = Path(__file__).resolve().parent.parent
RUTA_FOTOS_JSON = RAIZ / "data" / "fotos.json"
RUTA_RAW_JSON = Path(__file__).resolve().parent / "etiquetas_decisions_raw.json"
RUTA_DUDOSAS_CSV = Path(__file__).resolve().parent / "revision_dudosas.csv"

MODELO_DECISIONS = "gemini-decision-1"
ZONA_GRIS_MIN = 0.35
ZONA_GRIS_MAX = 0.65

PREGUNTAS_NOUL = [
    "agua_superficial",
    "ganado",
    "fauna_silvestre",
    "costra_salina",
    "infraestructura",
    "nieve_hielo",
    "muestreo_campo",
]

ETIQUETAS_LEGIBLES = {
    "agua_superficial": "Agua superficial",
    "ganado": "Ganado",
    "fauna_silvestre": "Fauna silvestre",
    "costra_salina": "Costra salina",
    "infraestructura": "Infraestructura",
    "nieve_hielo": "Nieve / hielo",
    "muestreo_campo": "Muestreo de campo",
}

TIPOS_TOMA = [
    "panoramica_vega",
    "detalle_vegetacion_suelo",
    "fauna_o_ganado",
    "agua_hidrologia",
    "trabajo_de_campo",
    "otro",
]

PREGUNTAS_DECISIONS: dict[str, dict[str, Any]] = {
    "agua_superficial": {
        "type": "noul",
        "instructions": (
            "¿Se ve agua superficial visible en la fotografía (arroyo, curso de agua, "
            "meandro, charco, espejo de agua, laguna o surgente)?"
        ),
        "criteria": {
            "true_description": (
                "Hay agua líquida claramente visible sobre la superficie: arroyos, "
                "canales con agua, charcos, lagunas, ojos de agua o surgentes."
            ),
            "false_description": (
                "No se distingue agua líquida superficial (solo vegetación, suelo seco, "
                "sal o nieve/hielo sin agua libre visible)."
            ),
        },
    },
    "ganado": {
        "type": "noul",
        "instructions": (
            "¿Aparece ganado doméstico en la fotografía (llamas, ovejas, vacas, "
            "caballos, burros o cabras)?"
        ),
        "criteria": {
            "true_description": (
                "Se distinguen uno o más animales domésticos (llamas, ovejas, vacas, "
                "caballos, burros o cabras), aunque estén en plano medio o lejano."
            ),
            "false_description": (
                "No se ve ganado doméstico (no confundir con rocas, matas o fauna silvestre "
                "como vicuñas)."
            ),
        },
    },
    "fauna_silvestre": {
        "type": "noul",
        "instructions": (
            "¿Aparece fauna silvestre en la fotografía (vicuñas, aves acuáticas, "
            "flamencos, patos, guayatas, suris u otros animales silvestres)?"
        ),
        "criteria": {
            "true_description": (
                "Se distinguen animales silvestres propios de la Puna (vicuñas de pelaje "
                "canela y vientre blanco, flamencos, patos, guayatas, aves en lagunas o vegas)."
            ),
            "false_description": (
                "No se observa fauna silvestre (no contar ganado doméstico como llamas, "
                "ovejas, vacas o caballos)."
            ),
        },
    },
    "costra_salina": {
        "type": "noul",
        "instructions": (
            "¿Se observan eflorescencias salinas, costras blancas de sal sobre el suelo "
            "o bordes de salar?"
        ),
        "criteria": {
            "true_description": (
                "Hay depósitos blancos o blanquecinos de sales sobre el suelo, bordes "
                "de charcos/arroyos o un salar visible en el fondo o margen de la vega."
            ),
            "false_description": (
                "No hay costras salinas ni salares visibles (no confundir con nieve en "
                "cumbres o espuma de agua)."
            ),
        },
    },
    "infraestructura": {
        "type": "noul",
        "instructions": (
            "¿Hay elementos humanos o ganaderos visibles en el paisaje (corrales, "
            "pircas de piedra, cercos/alambrados, canales artificiales, caminos, "
            "puestos, casas, puentes o vehículos)?"
        ),
        "criteria": {
            "true_description": (
                "Se ven construcciones o intervenciones humanas como pircas, corrales, "
                "alambrados, postes, caminos/huellas vehiculares marcadas, puestos, "
                "viviendas o camionetas."
            ),
            "false_description": (
                "El paisaje se ve natural sin construcciones, cercos, puestos ni vehículos "
                "visibles (ignorar pequeños instrumentos portátiles de muestreo)."
            ),
        },
    },
    "nieve_hielo": {
        "type": "noul",
        "instructions": (
            "¿Se ve nieve o hielo en la vega, en los bordes de agua congelada o en "
            "las laderas y cerros cercanos?"
        ),
        "criteria": {
            "true_description": (
                "Hay nieve acumulada en el suelo, laderas o montañas visibles, o hielo "
                "superficial en arroyos/charcos de la vega."
            ),
            "false_description": (
                "No hay nieve ni hielo visibles (no confundir con costras blancas de sal "
                "ni con nubes)."
            ),
        },
    },
    "muestreo_campo": {
        "type": "noul",
        "instructions": (
            "¿Se ven instrumentos científicos o trabajo de campo (pozos freáticos, "
            "piezómetros/tubos de PVC, sensores, estacas de medición, cuadrantes, "
            "libretas o personas midiendo/muestreando)?"
        ),
        "criteria": {
            "true_description": (
                "Aparecen equipos o señales de muestreo científico (tubos de pozo freático, "
                "sensores, cintas métricas, cuadrantes, mochilas/equipos en uso) o personas "
                "realizando tareas de campo."
            ),
            "false_description": (
                "No se ven instrumentos científicos ni personas trabajando en la toma."
            ),
        },
    },
    "tipo_toma": {
        "type": "choice",
        "instructions": (
            "Clasifica el tipo principal de encuadre o motivo de esta fotografía de campo "
            "en una vega de la Puna."
        ),
        "criteria": {
            "panoramica_vega": (
                "Vista general o panorámica del paisaje que muestra la extensión de la "
                "vega, quebrada, valle o entorno montañoso."
            ),
            "detalle_vegetacion_suelo": (
                "Plano cercano o detalle del suelo, tapiz vegetal, cojines de vega, "
                "pastos, costras salinas o microtopografía."
            ),
            "fauna_o_ganado": (
                "El sujeto principal de la foto son animales (ganado doméstico o fauna "
                "silvestre como vicuñas o aves)."
            ),
            "agua_hidrologia": (
                "El foco principal de la foto es un cuerpo o curso de agua: arroyo, "
                "surgente, laguna, meandro o espejo de agua."
            ),
            "trabajo_de_campo": (
                "El foco principal es el muestreo, instrumentos (pozos freáticos, sensores, "
                "mediciones) o investigadores trabajando."
            ),
            "otro": (
                "No encaja claramente en las categorías anteriores (por ejemplo, camino, "
                "puesto aislado, cielo, fuego o escena atípica)."
            ),
        },
    },
    "verdor_cobertura": {
        "type": "score",
        "instructions": (
            "Evalúa el nivel de verdor y cobertura vegetal visible en la vega o primer "
            "plano vegetado de la fotografía, en una escala ordenada de 5 niveles "
            "(del índice 0 = muy seco/suelo desnudo al índice 4 = cobertura vegetal "
            "densa y verde intensa)."
        ),
        "criteria": [
            "Nivel 1 (muy seco): suelo desnudo, roca, sal, agua o vegetación completamente parda/seca sin tonos verdes visibles.",
            "Nivel 2 (bajo): cobertura vegetal escasa o mayormente seca/amarillenta, con pequeños sectores verdes aislados.",
            "Nivel 3 (intermedio): cobertura vegetal moderada o mixta, combinando parches verdes con sectores secos, pardos o suelo desnudo.",
            "Nivel 4 (alto): cobertura vegetal abundante y predominantemente verde en gran parte de la vega.",
            "Nivel 5 (muy alto): cobertura vegetal muy densa, continua y de color verde intenso (césped de vega o bofedal muy vigoroso).",
        ],
    },
}


def cargar_json(ruta: Path) -> Any:
    with ruta.open("r", encoding="utf-8") as f:
        return json.load(f)


def guardar_json_atomico(ruta: Path, datos: Any, compacto: bool = False) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    tmp = ruta.with_suffix(ruta.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        if compacto:
            json.dump(datos, f, ensure_ascii=False, separators=(",", ":"))
        else:
            json.dump(datos, f, ensure_ascii=False, indent=2)
            f.write("\n")
    os.replace(tmp, ruta)


def ruta_imagen(foto_id: str, tamano: str) -> Path:
    carpeta = "fotos" if tamano == "fotos" else "miniaturas"
    return RAIZ / carpeta / f"{foto_id}.jpg"


def seleccionar_piloto(fotos: list[dict[str, Any]], n: int) -> list[dict[str, Any]]:
    """Selecciona N fotos variadas distribuidas entre campañas (año-mes) y vegas."""
    if n >= len(fotos):
        return list(fotos)

    # Agrupar por campaña (AAAA-MM) y dentro por vega
    por_campania: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for f in fotos:
        clave = (f.get("fecha") or "sin-fecha")[:7]
        por_campania[clave].append(f)

    campanias_ord = sorted(por_campania.keys())
    elegidas: list[dict[str, Any]] = []
    elegidas_ids: set[str] = set()
    vegas_usadas: set[str] = set()

    # Primera pasada: tomar una foto por campaña priorizando vegas no repetidas
    # y nombres descriptivos (cuando existan) distribuyendo uniformemente.
    paso = max(1, len(campanias_ord) / max(1, n))
    indices_camp = [int(round(i * paso)) for i in range(min(n, len(campanias_ord)))]
    indices_camp = sorted(set(min(idx, len(campanias_ord) - 1) for idx in indices_camp))

    for idx_c in indices_camp:
        if len(elegidas) >= n:
            break
        grupo = por_campania[campanias_ord[idx_c]]
        candidata = None
        for f in grupo:
            v = f.get("vega") or ""
            if f["id"] not in elegidas_ids and v and v not in vegas_usadas:
                candidata = f
                break
        if candidata is None:
            candidata = grupo[len(grupo) // 2]
        if candidata["id"] not in elegidas_ids:
            elegidas.append(candidata)
            elegidas_ids.add(candidata["id"])
            if candidata.get("vega"):
                vegas_usadas.add(candidata["vega"])

    # Segunda pasada: completar hasta N recorriendo campañas en round-robin
    punteros = {c: 0 for c in campanias_ord}
    while len(elegidas) < n:
        progreso = False
        for c in campanias_ord:
            if len(elegidas) >= n:
                break
            grupo = por_campania[c]
            while punteros[c] < len(grupo):
                cand = grupo[punteros[c]]
                punteros[c] += 1
                if cand["id"] in elegidas_ids:
                    continue
                v = cand.get("vega") or ""
                # Preferir vegas aún no cubiertas si quedan disponibles
                if v and v in vegas_usadas and len(vegas_usadas) < 40:
                    continue
                elegidas.append(cand)
                elegidas_ids.add(cand["id"])
                if v:
                    vegas_usadas.add(v)
                progreso = True
                break
        if not progreso:
            # Relajar restricción de vega única
            for f in fotos:
                if len(elegidas) >= n:
                    break
                if f["id"] not in elegidas_ids:
                    elegidas.append(f)
                    elegidas_ids.add(f["id"])
            break

    return elegidas[:n]


def crear_cliente() -> Any:
    api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError(
            "No se encontró la variable de entorno GEMINI_API_KEY.\n"
            "Configúrala antes de ejecutar el script, por ejemplo en PowerShell:\n"
            '  $env:GEMINI_API_KEY = "TU_API_KEY"\n'
            "o en bash:\n"
            '  export GEMINI_API_KEY="TU_API_KEY"'
        )

    try:
        from google import genai
    except ImportError as exc:
        raise RuntimeError(
            "No se pudo importar 'google.genai'. Instala el SDK oficial:\n"
            '  pip install -U "google-genai>=3.2.0"'
        ) from exc

    client = genai.Client(
        api_key=api_key,
        http_options={"api_version": "v1beta"},
    )
    if not hasattr(client, "decisions"):
        ver = getattr(genai, "__version__", "desconocida")
        raise RuntimeError(
            f"Tu versión instalada de google-genai ({ver}) no incluye client.decisions.\n"
            'Actualiza a >= 3.2.0: pip install -U "google-genai>=3.2.0"'
        )
    return client


def serializar_respuesta(resp: Any) -> dict[str, Any]:
    """Convierte CreateDecisionResponse a un dict JSON-serializable limpio."""
    answers_out: dict[str, Any] = {}
    answers = getattr(resp, "answers", None) or {}
    for qid, ans in answers.items():
        qtype = getattr(ans, "type", None)
        if qtype == "noul":
            answers_out[qid] = {
                "type": "noul",
                "noul": round(float(ans.noul), 4),
                "confidence": round(float(ans.confidence), 4),
            }
        elif qtype == "choice":
            probs = {
                k: round(float(v), 4)
                for k, v in (getattr(ans, "probabilities", None) or {}).items()
            }
            answers_out[qid] = {
                "type": "choice",
                "choice": str(ans.choice),
                "confidence": round(float(ans.confidence), 4),
                "probabilities": probs,
            }
        elif qtype == "score":
            raw_score = float(ans.score)
            probs = {
                str(k): round(float(v), 4)
                for k, v in (getattr(ans, "probabilities", None) or {}).items()
            }
            legend = dict(getattr(ans, "legend", None) or {})
            answers_out[qid] = {
                "type": "score",
                "score": round(raw_score, 4),
                "score_1_5": round(raw_score + 1.0, 4),
                "verdor_int": max(1, min(5, int(round(raw_score)) + 1)),
                "confidence": round(float(ans.confidence), 4),
                "probabilities": probs,
                "legend": legend,
            }
        else:
            # Fallback genérico si el SDK agrega un campo nuevo
            if hasattr(ans, "model_dump"):
                answers_out[qid] = ans.model_dump(mode="json")
            else:
                answers_out[qid] = str(ans)

    usage_out = None
    usage = getattr(resp, "usage", None)
    if usage is not None:
        if hasattr(usage, "model_dump"):
            usage_out = usage.model_dump(mode="json", exclude_none=True)
        else:
            usage_out = str(usage)

    return {
        "answers": answers_out,
        "usage": usage_out,
    }


def evaluar_foto(
    client: Any,
    foto: dict[str, Any],
    tamano: str,
    max_reintentos: int = 4,
) -> dict[str, Any]:
    img_path = ruta_imagen(foto["id"], tamano)
    if not img_path.is_file():
        raise FileNotFoundError(f"No existe la imagen: {img_path}")

    img_b64 = base64.b64encode(img_path.read_bytes()).decode("ascii")
    input_blocks = [
        {
            "type": "text",
            "text": (
                "Fotografía de campo de una vega (humedal altoandino) en la Puna argentina. "
                "Evalúa únicamente lo que es visualmente observable en la imagen."
            ),
        },
        {
            "type": "image",
            "data": img_b64,
            "mime_type": "image/jpeg",
        },
    ]

    ultimo_error: Exception | None = None
    for intento in range(1, max_reintentos + 1):
        try:
            resp = client.decisions.create(
                model=MODELO_DECISIONS,
                input=input_blocks,
                questions=PREGUNTAS_DECISIONS,
            )
            datos = serializar_respuesta(resp)
            datos.update(
                {
                    "id": foto["id"],
                    "fecha": foto.get("fecha"),
                    "vega": foto.get("vega"),
                    "provincia": foto.get("provincia"),
                    "modelo": MODELO_DECISIONS,
                    "tamano": tamano,
                    "evaluado_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                }
            )
            return datos
        except Exception as exc:
            ultimo_error = exc
            msg = str(exc)
            # Errores de autenticación o request inválido no se reintentan
            if any(code in msg for code in ("400", "401", "403", "404")):
                raise
            espera = min(30.0, 2.0**intento)
            print(
                f"  [reintento {intento}/{max_reintentos}] {foto['id']}: {exc}. "
                f"Esperando {espera:.1f}s...",
                file=sys.stderr,
            )
            time.sleep(espera)

    assert ultimo_error is not None
    raise ultimo_error


def cargar_cache() -> dict[str, Any]:
    if RUTA_RAW_JSON.is_file():
        datos = cargar_json(RUTA_RAW_JSON)
        if isinstance(datos, dict) and "resultados" in datos:
            return datos
    return {
        "modelo": MODELO_DECISIONS,
        "actualizado_utc": None,
        "resultados": {},
    }


def guardar_cache(cache: dict[str, Any]) -> None:
    cache["actualizado_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    guardar_json_atomico(RUTA_RAW_JSON, cache, compacto=False)


def extraer_resumen_foto(
    entrada: dict[str, Any],
    umbral_prob: float,
    umbral_conf: float,
) -> tuple[list[str], str | None, int | None]:
    answers = entrada.get("answers", {})
    etiquetas: list[str] = []
    for q in PREGUNTAS_NOUL:
        ans = answers.get(q)
        if not ans:
            continue
        prob = float(ans.get("noul", 0.0))
        conf = float(ans.get("confidence", 0.0))
        if prob >= umbral_prob and conf >= umbral_conf:
            etiquetas.append(q)

    tipo_ans = answers.get("tipo_toma") or {}
    tipo_toma = tipo_ans.get("choice")

    verdor_ans = answers.get("verdor_cobertura") or {}
    verdor = verdor_ans.get("verdor_int")
    if verdor is None and "score" in verdor_ans:
        verdor = max(1, min(5, int(round(float(verdor_ans["score"]))) + 1))

    return etiquetas, tipo_toma, verdor


def detectar_dudosas(
    fotos_por_id: dict[str, dict[str, Any]],
    resultados: dict[str, dict[str, Any]],
    umbral_conf: float,
    ids_objetivo: list[str] | None = None,
) -> list[dict[str, Any]]:
    filas: list[dict[str, Any]] = []
    claves = ids_objetivo if ids_objetivo is not None else list(resultados.keys())

    for fid in claves:
        entrada = resultados.get(fid)
        if not entrada:
            continue
        meta = fotos_por_id.get(fid, {})
        answers = entrada.get("answers", {})
        tamano = entrada.get("tamano", "fotos")
        archivo = f"{tamano}/{fid}.jpg"

        for q in PREGUNTAS_NOUL:
            ans = answers.get(q)
            if not ans:
                continue
            prob = float(ans.get("noul", 0.0))
            conf = float(ans.get("confidence", 0.0))
            motivos = []
            if ZONA_GRIS_MIN <= prob <= ZONA_GRIS_MAX:
                motivos.append("prob_zona_gris")
            if conf < umbral_conf:
                motivos.append("baja_confidence")
            if motivos:
                filas.append(
                    {
                        "id": fid,
                        "fecha": meta.get("fecha") or entrada.get("fecha") or "",
                        "vega": meta.get("vega") or entrada.get("vega") or "",
                        "provincia": meta.get("provincia") or entrada.get("provincia") or "",
                        "pregunta": q,
                        "tipo": "noul",
                        "valor": "si" if prob >= 0.5 else "no",
                        "probabilidad": f"{prob:.3f}",
                        "confidence": f"{conf:.3f}",
                        "motivo": ";".join(motivos),
                        "archivo": archivo,
                    }
                )

        tipo_ans = answers.get("tipo_toma")
        if tipo_ans:
            conf = float(tipo_ans.get("confidence", 0.0))
            if conf < umbral_conf:
                choice = tipo_ans.get("choice", "")
                prob = float((tipo_ans.get("probabilities") or {}).get(choice, conf))
                filas.append(
                    {
                        "id": fid,
                        "fecha": meta.get("fecha") or entrada.get("fecha") or "",
                        "vega": meta.get("vega") or entrada.get("vega") or "",
                        "provincia": meta.get("provincia") or entrada.get("provincia") or "",
                        "pregunta": "tipo_toma",
                        "tipo": "choice",
                        "valor": choice,
                        "probabilidad": f"{prob:.3f}",
                        "confidence": f"{conf:.3f}",
                        "motivo": "baja_confidence",
                        "archivo": archivo,
                    }
                )

        verdor_ans = answers.get("verdor_cobertura")
        if verdor_ans:
            conf = float(verdor_ans.get("confidence", 0.0))
            # Para una rúbrica ordinal de 5 niveles, p_max suele quedar en ~0.35-0.55
            # cuando la foto cae entre dos niveles vecinos; solo marcar si es muy difusa.
            if conf < min(umbral_conf, 0.30):
                score_1_5 = verdor_ans.get("score_1_5")
                if score_1_5 is None and "score" in verdor_ans:
                    score_1_5 = float(verdor_ans["score"]) + 1.0
                filas.append(
                    {
                        "id": fid,
                        "fecha": meta.get("fecha") or entrada.get("fecha") or "",
                        "vega": meta.get("vega") or entrada.get("vega") or "",
                        "provincia": meta.get("provincia") or entrada.get("provincia") or "",
                        "pregunta": "verdor_cobertura",
                        "tipo": "score",
                        "valor": f"{float(score_1_5):.2f}" if score_1_5 is not None else "",
                        "probabilidad": f"{conf:.3f}",
                        "confidence": f"{conf:.3f}",
                        "motivo": "baja_confidence",
                        "archivo": archivo,
                    }
                )

    return filas


def exportar_dudosas_csv(filas: list[dict[str, Any]]) -> None:
    campos = [
        "id",
        "fecha",
        "vega",
        "provincia",
        "pregunta",
        "tipo",
        "valor",
        "probabilidad",
        "confidence",
        "motivo",
        "archivo",
    ]
    with RUTA_DUDOSAS_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(filas)


def aplicar_a_fotos_json(
    datos_atlas: dict[str, Any],
    resultados: dict[str, dict[str, Any]],
    umbral_prob: float,
    umbral_conf: float,
) -> tuple[int, int]:
    actualizadas = 0
    sin_datos = 0
    for foto in datos_atlas["fotos"]:
        entrada = resultados.get(foto["id"])
        if not entrada:
            sin_datos += 1
            continue
        etiquetas, tipo_toma, verdor = extraer_resumen_foto(
            entrada, umbral_prob=umbral_prob, umbral_conf=umbral_conf
        )
        foto["etiquetas"] = etiquetas
        if tipo_toma:
            foto["tipo_toma"] = tipo_toma
        if verdor is not None:
            foto["verdor"] = verdor
        actualizadas += 1

    guardar_json_atomico(RUTA_FOTOS_JSON, datos_atlas, compacto=True)
    return actualizadas, sin_datos


def imprimir_resumen(
    fotos_objetivo: list[dict[str, Any]],
    resultados: dict[str, dict[str, Any]],
    filas_dudosas: list[dict[str, Any]],
    umbral_prob: float,
    umbral_conf: float,
) -> None:
    evaluadas = [f for f in fotos_objetivo if f["id"] in resultados]
    print(f"\n=== Resumen ({len(evaluadas)}/{len(fotos_objetivo)} fotos evaluadas) ===")
    print(f"Umbrales activos: prob >= {umbral_prob:.2f}, confidence >= {umbral_conf:.2f}\n")

    conteo_etq: Counter[str] = Counter()
    conteo_tipo: Counter[str] = Counter()
    conteo_verdor: Counter[int] = Counter()

    print(
        f"{'ID':<34} | {'Fecha':<10} | {'Vega':<22} | {'Tipo toma':<24} | {'V':>1} | Etiquetas"
    )
    print("-" * 125)
    for f in evaluadas:
        etqs, tipo, verdor = extraer_resumen_foto(
            resultados[f["id"]], umbral_prob=umbral_prob, umbral_conf=umbral_conf
        )
        for e in etqs:
            conteo_etq[e] += 1
        if tipo:
            conteo_tipo[tipo] += 1
        if verdor is not None:
            conteo_verdor[verdor] += 1
        vega = (f.get("vega") or "-")[:22]
        fecha = (f.get("fecha") or "")[:10]
        print(
            f"{f['id'][:34]:<34} | {fecha:<10} | {vega:<22} | "
            f"{(tipo or '-'):<24} | {str(verdor or '-'):>1} | {', '.join(etqs) or '-'}"
        )

    print("\n--- Frecuencia por etiqueta ---")
    for q in PREGUNTAS_NOUL:
        print(f"  {q:<20}: {conteo_etq[q]}")

    print("\n--- Distribución por tipo_toma ---")
    for t in TIPOS_TOMA:
        if conteo_tipo[t]:
            print(f"  {t:<26}: {conteo_tipo[t]}")

    print("\n--- Distribución de verdor (1-5) ---")
    for v in range(1, 6):
        print(f"  nivel {v}: {conteo_verdor[v]}")

    fotos_dudosas = len({r["id"] for r in filas_dudosas})
    print(
        f"\n--- Casos en zona gris ---\n"
        f"  {len(filas_dudosas)} alertas en {fotos_dudosas} fotos -> {RUTA_DUDOSAS_CSV}"
    )


def construir_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description=(
            "Etiqueta fotografías del Atlas de Vegas de la Puna Argentina con "
            "Gemini Decisions API (gemini-decision-1)."
        )
    )
    p.add_argument(
        "--tamano",
        choices=["fotos", "miniaturas"],
        default="fotos",
        help="Carpeta de imágenes a enviar a la API (por defecto: fotos).",
    )
    p.add_argument(
        "--piloto",
        type=int,
        default=0,
        metavar="N",
        help="Procesa solo una muestra estratificada de N fotos variadas.",
    )
    p.add_argument(
        "--forzar",
        action="store_true",
        help="Re-evalúa las fotos aunque ya existan en etiquetas_decisions_raw.json.",
    )
    p.add_argument(
        "--umbral-prob",
        type=float,
        default=0.70,
        help="Umbral mínimo de probabilidad P(true) para activar una etiqueta noul (default: 0.70).",
    )
    p.add_argument(
        "--umbral-conf",
        type=float,
        default=0.60,
        help="Umbral mínimo de confidence para aceptar una etiqueta sin marcar duda (default: 0.60).",
    )
    p.add_argument(
        "--pausa",
        type=float,
        default=0.0,
        help="Pausa en segundos entre llamadas en modo secuencial (default: 0.0).",
    )
    p.add_argument(
        "--concurrencia",
        type=int,
        default=5,
        metavar="N",
        help="Número de hilos en paralelo para llamar a la API (default: 5; usar 1 para secuencial).",
    )
    p.add_argument(
        "--aplicar-json",
        action="store_true",
        help="Fusiona las etiquetas limpias desde el caché raw hacia data/fotos.json.",
    )
    p.add_argument(
        "--solo-resumen",
        action="store_true",
        help="No llama a la API: recalcula revision_dudosas.csv e imprime el resumen del caché.",
    )
    return p


def main(argv: list[str] | None = None) -> int:
    args = construir_parser().parse_args(argv)
    datos_atlas = cargar_json(RUTA_FOTOS_JSON)
    fotos: list[dict[str, Any]] = datos_atlas["fotos"]
    fotos_por_id = {f["id"]: f for f in fotos}
    cache = cargar_cache()
    resultados: dict[str, dict[str, Any]] = cache["resultados"]

    objetivo = seleccionar_piloto(fotos, args.piloto) if args.piloto > 0 else fotos

    if not args.solo_resumen and not (args.aplicar_json and args.piloto == 0 and not args.forzar and len(resultados) >= len(objetivo)):
        pendientes = [
            f for f in objetivo if args.forzar or f["id"] not in resultados
        ]
        if pendientes:
            try:
                client = crear_cliente()
            except RuntimeError as err:
                print(f"Error: {err}", file=sys.stderr)
                return 2

            total = len(pendientes)
            workers = max(1, int(args.concurrencia))
            print(
                f"Evaluando {total} foto(s) con {MODELO_DECISIONS} "
                f"(carpeta: {args.tamano}/, hilos: {workers}, ya en caché: {len(objetivo) - total})..."
            )
            t0 = time.monotonic()
            lock = threading.Lock()
            completadas = 0
            errores: list[tuple[str, Exception]] = []

            if workers == 1:
                for idx, foto in enumerate(pendientes, start=1):
                    try:
                        res = evaluar_foto(client, foto, tamano=args.tamano)
                    except Exception as exc:
                        print(
                            f"\n[ERROR] Falló {foto['id']} ({idx}/{total}): {exc}",
                            file=sys.stderr,
                        )
                        guardar_cache(cache)
                        return 1
                    resultados[foto["id"]] = res
                    guardar_cache(cache)

                    etqs, tipo, verdor = extraer_resumen_foto(
                        res, umbral_prob=args.umbral_prob, umbral_conf=args.umbral_conf
                    )
                    trans = time.monotonic() - t0
                    restante = (trans / idx) * (total - idx)
                    print(
                        f"[{idx:>3}/{total}] {foto['id']:<32} -> tipo={tipo:<24} "
                        f"V={verdor} etq=[{', '.join(etqs)}]  (ETA {restante:.0f}s)",
                        flush=True,
                    )
                    if args.pausa > 0 and idx < total:
                        time.sleep(args.pausa)
            else:
                with ThreadPoolExecutor(max_workers=workers) as pool:
                    futuros = {
                        pool.submit(evaluar_foto, client, foto, args.tamano): foto
                        for foto in pendientes
                    }
                    for fut in as_completed(futuros):
                        foto = futuros[fut]
                        try:
                            res = fut.result()
                        except Exception as exc:
                            with lock:
                                errores.append((foto["id"], exc))
                                print(
                                    f"\n[ERROR] Falló {foto['id']}: {exc}",
                                    file=sys.stderr,
                                    flush=True,
                                )
                            continue

                        with lock:
                            resultados[foto["id"]] = res
                            completadas += 1
                            guardar_cache(cache)
                            etqs, tipo, verdor = extraer_resumen_foto(
                                res,
                                umbral_prob=args.umbral_prob,
                                umbral_conf=args.umbral_conf,
                            )
                            trans = time.monotonic() - t0
                            restante = (trans / completadas) * (total - completadas)
                            print(
                                f"[{completadas:>3}/{total}] {foto['id']:<32} -> tipo={tipo:<24} "
                                f"V={verdor} etq=[{', '.join(etqs)}]  (ETA {restante:.0f}s)",
                                flush=True,
                            )

                if errores:
                    print(
                        f"\nTerminó con {len(errores)} error(es). Vuelve a ejecutar para reintentar las faltantes.",
                        file=sys.stderr,
                    )
                    return 1
        else:
            print(
                f"Todas las {len(objetivo)} fotos objetivo ya están en caché "
                f"({RUTA_RAW_JSON.name}). Usa --forzar para re-evaluar."
            )

    ids_obj = [f["id"] for f in objetivo if f["id"] in resultados]
    filas_dudosas = detectar_dudosas(
        fotos_por_id,
        resultados,
        umbral_conf=args.umbral_conf,
        ids_objetivo=ids_obj if args.piloto > 0 else None,
    )
    exportar_dudosas_csv(filas_dudosas)

    if ids_obj:
        imprimir_resumen(
            objetivo,
            resultados,
            filas_dudosas,
            umbral_prob=args.umbral_prob,
            umbral_conf=args.umbral_conf,
        )

    if args.aplicar_json:
        act, sin_d = aplicar_a_fotos_json(
            datos_atlas,
            resultados,
            umbral_prob=args.umbral_prob,
            umbral_conf=args.umbral_conf,
        )
        print(
            f"\nActualizado {RUTA_FOTOS_JSON}: {act} fotos con etiquetas aplicadas "
            f"({sin_d} sin evaluar todavía)."
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
