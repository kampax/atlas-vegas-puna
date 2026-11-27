# Vegas de la Puna Argentina

Proyecto personal de atlas fotográfico de **vegas de la Puna argentina**: una representación visual de estos humedales altoandinos a partir de las fotografías tomadas en campañas de campo.

Las vegas (o bofedales) son humedales de altura alimentados principalmente por agua subterránea. En la Puna sostienen la ganadería local y gran parte de la biodiversidad regional. Este sitio muestra cómo se ven en el terreno, ordenadas por lugar y por fecha.

## En cifras

<!-- auto:cifras -->
- **465 fotografías** de 19 campañas de campo, entre 2016 y 2026.
- 244 con la ubicación GPS de la cámara y 221 con ubicación aproximada.
- Altitudes de 3.012 a 4.778 m s. n. m.
- 47 vegas identificadas en las fotos (26 de ellas son puntos de muestreo); 15 fotografiadas en más de una campaña.
<!-- /auto:cifras -->

## Qué muestra

- Las **fotografías** agrupadas por campaña de campo.
- Un **mapa** con el lugar de cada foto. Al tocar una foto, el mapa se acerca a la vega correspondiente sobre imagen satelital.
- El **borde de la Puna argentina** y los **límites de sus departamentos**, que se pueden ocultar.
- Los **58 puntos de muestreo de vegas** y, si se activan, los **polígonos de vegas** de la región.
- Filtros por **año**, **provincia**, **departamento** y **vega**, combinables. Al elegir un departamento, el mapa lo encuadra y resalta su límite. Los nombres de vegas de cada campaña también filtran al tocarlos.
- **Comparación en el tiempo:** las vegas fotografiadas en más de una campaña se pueden ver lado a lado, una columna por campaña, con la estación del año (por ejemplo, Botijuela en invierno de 2017, primavera de 2017, verano de 2018 y otoño de 2019). Se abre desde el visor o desde el filtro de vega.
- Un visor de fotos que se maneja con flechas o deslizando el dedo en el teléfono.
- **Enlaces para compartir:** la dirección guarda lo que se está viendo (año, lugar, vega, foto o comparación), así se puede mandar un enlace exacto. Por ejemplo, `#vega=botijuela&comparar=botijuela` abre la comparación de Botijuela y `#anio=2021&departamento=los-andes` muestra las fotos de 2021 en Los Andes. El visor tiene un botón para copiar el enlace a la foto abierta.

### Vegas para comparar en el tiempo

<!-- auto:comparables -->
| Vega | Campañas |
|---|---:|
| Antofalla | 5 |
| Antofagasta, Botijuela, Las Quinoas, Olacapato chico, Quebrada del diablo, Real Grande | 4 |
| Las pitas, Trapiche | 3 |
| Aguas Calientes abajo, Laguna antofagasta, Loro Huasi, Matadero, Tocomar, Vega Sinuosa | 2 |
<!-- /auto:comparables -->

En el mapa, un punto **lleno** indica que la foto tiene la ubicación GPS de la cámara. Un punto **hueco** indica una ubicación **aproximada**, estimada a partir de la hora de la toma, del nombre de la vega o del paisaje.

Cada foto muestra además su **altitud**. Es un dato fijo, obtenido del modelo digital de elevación [Copernicus DEM GLO-30](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_DEM_GLO30) (versión 2024_1, 30 m de resolución) en el punto de la foto, extraído con Google Earth Engine. En las fotos con ubicación aproximada, la altitud también es aproximada.

## Campañas

<!-- auto:campanias -->
| Campaña | Fotos | Vegas identificadas |
|---|---:|---|
| Abril de 2016 | 29 | Abra Aparejo, Cortaderas, Incahuasi, La 40, Las Peladas |
| Febrero de 2017 | 3 | Matadero |
| Agosto de 2017 | 7 | Antofalla, Botijuela, Las Quinoas, Quebrada del diablo |
| Noviembre de 2017 | 10 | Antofalla, Botijuela, Loro Huasi, Pozo bravo, Quebrada del diablo |
| Febrero de 2018 | 20 | Antofalla, Botijuela, Las Quinoas, Loro Huasi, Quebrada del diablo |
| Marzo de 2018 | 13 | Matadero, Vega Laguna Huaca Huasi, Vega Sinuosa |
| Mayo de 2018 | 11 | Las pitas, Real Grande |
| Septiembre de 2018 | 10 | Antofagasta, Laguna antofagasta |
| Enero de 2019 | 6 |  |
| Febrero de 2019 | 2 | Tocomar |
| Marzo de 2019 | 20 | Antofagasta, Antofalla, Botijuela, Las Quinoas, Quebrada del diablo |
| Febrero de 2021 | 87 | Acay norte, Acay sur, Antofagasta, Cementerio, Las Cuevas, Mirihuaca, Real Grande, San Antonio de los Cobres |
| Mayo de 2021 | 20 | Las pitas, Olacapato chico, Real Grande |
| Octubre de 2021 | 66 | Alazán, Antofalla, Laguna blanca pueblo, Las pitas, Las Quinoas, Olacapato chico, Punta de la Peña, Real Grande, Vega Sinuosa |
| Diciembre de 2021 | 68 | Aguas Calientes abajo, Maktud, Nac. Aguas Calientes, Parinayu, Río Los Patos abajo, Río Los Patos arriba, Trapiche |
| Febrero de 2026 | 32 | Aguas Calientes abajo, Antofagasta, Cacao, Laguna antofagasta, Olacapato chico, Paicuqui arriba, Rincón, Trapiche, Vega Laguna |
| Marzo de 2026 | 5 | Huancar, Tocomar |
| Junio de 2026 | 52 | Carachi Pampa, Los Nacimientos, Olacapato chico, Paicuqui abajo, Quebrada de Curuto, Quebrada Seca |
| Septiembre de 2026 | 4 | Peñas Blancas, Trapiche |
<!-- /auto:campanias -->

Cada foto lleva el nombre de la vega donde se tomó. Si está a menos de 3 km de uno de los puntos de muestreo, se usa el nombre de ese punto; si no, el nombre con que se identificó la vega en el campo.

## Provincias y departamentos

Se consideran **departamentos de la Puna** los que tienen al menos el 5 % de su superficie dentro del área de estudio: 24 departamentos de Jujuy, Salta, Catamarca, La Rioja, San Juan y Tucumán. En el mapa se dibujan recortados al borde de la Puna.

Cada foto se asigna al departamento que la contiene. Unas pocas caen justo fuera del límite de catastro, en las Cumbres Calchaquíes; se asignan al departamento más cercano (a menos de 5 km), que es Tafí del Valle, como confirma la cartografía FAO GAUL.

<!-- auto:departamentos -->
| Provincia | Departamento | Fotos |
|---|---|---:|
| Catamarca | Antofagasta de la Sierra | 319 |
| Catamarca | Tinogasta | 29 |
| Catamarca | Belén | 26 |
| Jujuy | Cochinoca | 4 |
| Salta | Los Andes | 28 |
| Salta | Molinos | 16 |
| Salta | La Poma | 14 |
| Salta | Rosario de Lerma | 2 |
| Tucumán | Tafí del Valle | 27 |
<!-- /auto:departamentos -->

## Chatbot bibliográfico (Doña Vicuña)

El sitio incluye un asistente de consultas (**Doña Vicuña**) pensado como **un pequeño experimento** para responder preguntas sobre vegas, bofedales, turberas y humedales altoandinos usando **exclusivamente una selección de artículos científicos** sobre estos ecosistemas (citando las fuentes en cada respuesta). No pretende abarcar ni representar toda la bibliografía existente sobre el tema.

- **Artículos incluidos:** el listado completo y actualizable con autores, año, título, DOI y temática general está en [BIBLIOGRAFIA.md](BIBLIOGRAFIA.md).
- **Sugerir artículos nuevos:** si conocés trabajos científicos sobre vegas o bofedales que deberían sumarse, podés proponerlos abriendo un **Issue** en el repositorio (indicando título, año y DOI o enlace).

## Estructura

```
index.html                       Página del sitio
assets/comun.js                  Carga de datos, mapas base y visor de fotos
assets/chat.js, chat.css         Interfaz del chatbot bibliográfico
assets/vicuna.jpg                Avatar del chatbot
bot/                             Worker de Cloudflare y servidor local del chat
data/fotos.json                  Fecha, ubicación y vega de cada foto
data/vegas_muestreadas.geojson   58 puntos de muestreo de vegas
data/vegas.geojson               Polígonos de vegas (simplificados)
data/puna.geojson                Borde del área de la Puna argentina
data/departamentos.geojson       Departamentos de la Puna, recortados al borde, con su provincia
fotos/                           Fotos para el visor (máx. 1600 px)
miniaturas/                      Miniaturas (máx. 480 px)
herramientas/                    Scripts para regenerar el README, validar los datos y etiquetar fotos
BIBLIOGRAFIA.md                  Listado de artículos científicos usados por el chatbot
PROCESO.md                       Cómo agregar fotos, corregir datos o sumar bibliografía
```

Para incorporar información nueva (fotos de una campaña, correcciones, puntos de muestreo o artículos para el chat), seguir [PROCESO.md](PROCESO.md).

Cada foto de `data/fotos.json` tiene estos campos:

| Campo | Contenido |
|---|---|
| `id` | Nombre del archivo en `fotos/` y `miniaturas/` (sin `.jpg`) |
| `fecha` | Fecha y hora de la toma (`AAAA-MM-DD HH:MM`) |
| `lat`, `lon` | Coordenadas en WGS84 |
| `precision` | `exacta` (GPS de la cámara) o `aproximada` |
| `vega` | Nombre de la vega: el punto de muestreo más cercano si está a menos de 3 km, o la vega identificada en el campo |
| `ancho`, `alto` | Tamaño en píxeles de la foto publicada |
| `altitud` | Altitud en metros sobre el nivel del mar (Copernicus DEM GLO-30) |
| `provincia`, `departamento` | Provincia y departamento de la Puna donde se tomó la foto |

Las fotos se publican **sin metadatos EXIF**: no incluyen el modelo del teléfono ni las coordenadas originales.

## Verlo en local

El sitio es estático. Desde la carpeta del proyecto:

```bash
python -m http.server 8000
```

Después abre <http://localhost:8000>. Abrir `index.html` con doble clic no alcanza, porque el navegador bloquea la carga de los datos.

## Publicarlo en GitHub Pages

1. Crea en GitHub un repositorio llamado `atlas-vegas-puna` y sube el contenido de esta carpeta.
2. En el repositorio, ve a **Settings → Pages**.
3. En **Build and deployment**, elige **Deploy from a branch**, la rama `main` y la carpeta `/ (root)`.
4. En uno o dos minutos el sitio queda en `https://<usuario>.github.io/atlas-vegas-puna/`.

## Créditos

- **Fotografías:** [Carlos Javier Navarro](https://www.researchgate.net/profile/Carlos-Javier-Navarro).
- **Instituciones:** CONICET; Instituto de Ecología Regional (IER, CONICET y UNT); Instituto de Datación y Arqueometría (InDyA). Sus logos están en `assets/logos/`.
- **Financiamiento:** Agencia Nacional de Promoción de la Investigación, el Desarrollo Tecnológico y la Innovación (Agencia I+D+i, ex ANPCyT), a través del Fondo para la Investigación Científica y Tecnológica (FONCyT), y Universidad Nacional de Tucumán (UNT). Los proyectos se ejecutaron en el IER (CONICET-UNT):

| Proyecto | Período | Título (abreviado) | Responsable | Financiamiento |
|---|---|---|---|---|
| PICT-2018-03881 | 2018-2023 | Transición de la megaherbivoría en el gradiente altitudinal del noroeste argentino | H. R. Grau | FONCyT, Agencia I+D+i |
| PICT-2018-04228 | 2018-2023 | Clasificación socio-ecológica de humedales de la Puna | A. E. Izquierdo | FONCyT, Agencia I+D+i |
| PIUNT G506 | 2017-2019 | Optimización territorial participativa del patrimonio socio-ambiental de la Puna argentina | H. R. Grau | SCAIT, UNT |
| PICT-2016-2173 | 2017-2022 | Sistemas socio-ecológicos altoandinos, conflictos y toma de decisiones | H. R. Grau | FONCyT, Agencia I+D+i |
| PICT-2012-1565 | 2014-2016 | Distribución, variabilidad ecológica y biodiversidad de los humedales de la Puna argentina | H. R. Grau | FONCyT, Agencia I+D+i |

- **Mapas base:** © OpenTopoMap (CC-BY-SA) y © colaboradores de OpenStreetMap; imágenes satelitales y etiquetas © Esri, Maxar, Earthstar Geographics.
- **Límites:** borde de la Puna según el área de estudio del proyecto; límites departamentales de los catastros provinciales y del IGM. Verificación de departamentos con FAO GAUL (vía Google Earth Engine).
- **Altitud:** Copernicus DEM GLO-30 © DLR e.V. 2010-2014 y © Airbus Defence and Space GmbH 2014-2018, provisto bajo el programa COPERNICUS por la Unión Europea y la ESA; procesado con [Google Earth Engine](https://earthengine.google.com) (Gorelick et al., 2017, *Remote Sensing of Environment* 202: 18-27).
- **Mapa interactivo:** [Leaflet](https://leafletjs.com).
- **Tipografías:** Newsreader e Instrument Sans (Google Fonts, SIL Open Font License).

Las fotografías pertenecen a su autor. Para reutilizarlas, consulta antes con él.

**Contacto:** [cjnavarro@indya.unju.edu.ar](mailto:cjnavarro@indya.unju.edu.ar)
