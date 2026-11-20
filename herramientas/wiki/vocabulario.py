"""Vocabularios cerrados de las fichas y sus nombres para mostrar (ver wiki/_esquema.md)."""

PAISES = {
    "argentina": "Argentina",
    "bolivia": "Bolivia",
    "chile": "Chile",
    "peru": "Perú",
    "ecuador": "Ecuador",
    "colombia": "Colombia",
    "venezuela": "Venezuela",
    "andes-general": "Andes en general",
    "fuera-de-andes": "Fuera de los Andes",
}

ECOSISTEMAS = {
    "vega": "Vegas",
    "bofedal": "Bofedales",
    "turbera": "Turberas",
    "paramo": "Páramos",
    "humedal-altoandino": "Humedales altoandinos",
    "laguna-salar": "Lagunas y salares",
    "pastizal-puna": "Pastizales de la Puna",
    "bosque-inundable": "Bosques inundables",
    "otro": "Otros ambientes",
}

TEMAS = {
    "definicion-y-clasificacion": "Definición y clasificación",
    "hidrologia": "Hidrología",
    "vegetacion": "Vegetación",
    "fauna": "Fauna",
    "microbiologia": "Microbiología",
    "suelos-y-turba": "Suelos y turba",
    "carbono-y-gases": "Carbono y gases de efecto invernadero",
    "paleoambiente": "Paleoambiente",
    "arqueologia-y-ocupacion-humana": "Arqueología y ocupación humana",
    "pastoreo": "Pastoreo",
    "comunidades-y-gobernanza": "Comunidades y gobernanza",
    "mineria-y-extraccion-de-agua": "Minería y extracción de agua",
    "cambio-climatico": "Cambio climático",
    "teledeteccion-y-mapeo": "Teledetección y mapeo",
    "conservacion-y-restauracion": "Conservación y restauración",
}

METODOS = {
    "teledeteccion-optica": "Teledetección óptica",
    "radar": "Radar",
    "lidar-y-fotogrametria": "LiDAR y fotogrametría",
    "inventario-de-vegetacion": "Inventario de vegetación",
    "muestreo-de-suelos-y-turba": "Muestreo de suelos y turba",
    "testigos-sedimentarios": "Testigos sedimentarios",
    "datacion-radiocarbono": "Datación por radiocarbono",
    "medicion-de-gases": "Medición de gases",
    "hidrologia-de-campo": "Hidrología de campo",
    "isotopos-y-geoquimica": "Isótopos y geoquímica",
    "analisis-estadistico": "Análisis estadístico",
    "modelado": "Modelado",
    "encuestas-y-etnografia": "Encuestas y etnografía",
    "excavacion-arqueologica": "Excavación arqueológica",
    "experimento-de-campo": "Experimento de campo",
    "analisis-de-laboratorio": "Análisis de laboratorio",
    "revision-bibliografica": "Revisión bibliográfica",
}

# campo de la ficha -> (carpeta de la wiki, vocabulario)
FACETAS = {
    "temas": ("temas", TEMAS),
    "paises": ("paises", PAISES),
    "ecosistemas": ("ecosistemas", ECOSISTEMAS),
    "metodos": ("metodos", METODOS),
}

TIPOS_DOCUMENTO = {"articulo", "tesis", "informe", "libro", "capitulo", "resumen-congreso", "otro"}
IDIOMAS = {"es", "en", "pt", "otro"}
