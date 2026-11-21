# Comparación de modos: `completo`, `rag`, `hibrido-0.3`, `hibrido-0.5`, `hibrido-0.7`

- Fecha: 2026-11-20 23:04 UTC
- Preguntas evaluadas: 15
- Proveedor configurado: `glm` (respaldo: `deepseek`)
- `rag` = modo rag solo con BM25; `hibrido-X` = modo rag con búsqueda híbrida (X = peso de BM25, el resto embeddings bge-m3).
- Proveedor «fija»: el bot no encontró fragmentos relevantes y dio la respuesta fija sin llamar al modelo.

## Fuentes citadas por pregunta

| # | Categoría | `completo` | `rag` | `hibrido-0.3` | `hibrido-0.5` | `hibrido-0.7` |
|---:|---|---:|---:|---:|---:|---:|
| 1 | Definición | 3 | 2 | 6 | 4 | 1 |
| 2 | Puna argentina vs. otros países | 11 | 2 | 3 | 4 | 3 |
| 3 | Cifras concretas | 4 | 2 | 5 | 4 | 2 |
| 4 | Pastoreo | 6 | 5 | 5 | 5 | 2 |
| 5 | Agua / Hidrología | 9 | 8 | 4 | 2 | 2 |
| 6 | Carbono | 7 | 2 | 9 | 9 | 4 |
| 7 | Minería / Litio | 7 | 4 | 5 | 4 | 5 |
| 8 | Teledetección / Mapeo | 11 | 10 | 9 | 1 | 2 |
| 9 | Vegetación / Cojines | 1 | 2 | 2 | 4 | 2 |
| 10 | Atlas fotográfico | 0 | 1 | 1 | 1 | 1 |
| 11 | Cambio climático | 7 | 6 | 7 | 5 | 4 |
| 12 | Repregunta (pastoreo en Chile) | 4 | 3 | 3 | 3 | 5 |
| 13 | Repregunta (carbono en Puna arg.) | 2 | 3 | 2 | 2 | 2 |
| 14 | Fuera de tema | 0 | 0 | 0 | 0 | 0 |
| 15 | Sin datos en la wiki | 1 | 1 | 1 | 1 | 1 |
| | **Total** | **73** | **51** | **62** | **49** | **36** |

## Detalle técnico

| # | Categoría | Proveedor (`completo` / `rag` / `hibrido-0.3` / `hibrido-0.5` / `hibrido-0.7`) | Tokens in (`completo` / `rag` / `hibrido-0.3` / `hibrido-0.5` / `hibrido-0.7`) | Tiempo s (`completo` / `rag` / `hibrido-0.3` / `hibrido-0.5` / `hibrido-0.7`) | DOI en Fuentes (`completo` / `rag` / `hibrido-0.3` / `hibrido-0.5` / `hibrido-0.7`) |
|---:|---|---|---|---|---|
| 1 | Definición | DS / DS / DS / DS / DS | 412.044 / 7.397 / 6.976 / 7.384 / 7.164 | 15.9 / 3.1 / 3.8 / 4.3 / 2.6 | 2/3 / 1/2 / 4/6 / 3/4 / 1/1 |
| 2 | Puna argentina vs. otros países | DS / DS / DS / DS / DS | 412.056 / 7.477 / 7.446 / 7.062 / 7.062 | 8.4 / 3.0 / 4.0 / 3.2 / 3.3 | 6/11 / 2/2 / 3/3 / 3/4 / 3/3 |
| 3 | Cifras concretas | DS / DS / DS / DS / DS | 412.054 / 7.390 / 7.060 / 7.169 / 7.118 | 5.2 / 2.0 / 2.7 / 2.8 / 2.5 | 4/4 / 1/2 / 3/5 / 3/4 / 1/2 |
| 4 | Pastoreo | DS / DS / DS / DS / DS | 412.048 / 7.418 / 7.380 / 7.309 / 7.356 | 6.3 / 4.3 / 4.3 / 4.0 / 3.6 | 5/6 / 5/5 / 3/5 / 4/5 / 2/2 |
| 5 | Agua / Hidrología | DS / DS / DS / DS / DS | 412.046 / 7.387 / 7.209 / 7.372 / 7.323 | 8.2 / 4.7 / 3.9 / 3.2 / 3.3 | 8/9 / 7/8 / 3/4 / 2/2 / 2/2 |
| 6 | Carbono | DS / GLM / GLM / GLM / GLM | 412.049 / 7.348 / 7.382 / 7.308 / 7.363 | 8.2 / 20.3 / 21.6 / 22.1 / 14.3 | 5/7 / 2/2 / 4/9 / 6/9 / 3/4 |
| 7 | Minería / Litio | DS / DS / DS / DS / DS | 412.053 / 7.226 / 7.328 / 7.328 / 7.399 | 19.3 / 5.5 / 5.1 / 3.9 / 4.0 | 5/7 / 4/4 / 3/5 / 2/4 / 4/5 |
| 8 | Teledetección / Mapeo | DS / DS / DS / DS / DS | 412.052 / 6.940 / 7.002 / 7.140 / 7.140 | 8.8 / 6.5 / 5.6 / 3.7 / 4.8 | 10/11 / 8/10 / 8/9 / 1/1 / 2/2 |
| 9 | Vegetación / Cojines | DS / DS / DS / DS / DS | 412.054 / 6.876 / 7.178 / 7.178 / 7.437 | 5.3 / 2.5 / 3.3 / 3.7 / 2.9 | 1/1 / 2/2 / 2/2 / 3/4 / 2/2 |
| 10 | Atlas fotográfico | DS / DS / DS / DS / DS | 412.050 / 7.318 / 7.296 / 6.937 / 7.026 | 3.5 / 1.8 / 1.7 / 1.5 / 1.3 | N/A / 0/1 / 0/1 / 0/1 / 0/1 |
| 11 | Cambio climático | DS / DS / DS / DS / DS | 412.050 / 7.422 / 7.359 / 7.297 / 7.042 | 8.1 / 4.6 / 5.6 / 4.9 / 3.9 | 7/7 / 4/6 / 7/7 / 5/5 / 4/4 |
| 12 | Repregunta (pastoreo en Chile) | DS / DS / DS / DS / DS | 412.088 / 7.431 / 7.420 / 7.070 / 7.431 | 16.5 / 3.1 / 3.5 / 2.9 / 3.7 | 3/4 / 2/3 / 2/3 / 2/3 / 2/5 |
| 13 | Repregunta (carbono en Puna arg.) | DS / DS / DS / DS / DS | 412.088 / 7.435 / 7.477 / 6.949 / 7.217 | 4.4 / 3.8 / 2.2 / 2.7 / 2.3 | 2/2 / 3/3 / 2/2 / 2/2 / 2/2 |
| 14 | Fuera de tema | DS / DS / fija / fija / fija | 412.043 / 7.386 / 0 / 0 / 0 | 4.4 / 1.6 / 0.0 / 0.0 / 0.0 | N/A / N/A / N/A / N/A / N/A |
| 15 | Sin datos en la wiki | DS / DS / DS / DS / DS | 412.052 / 7.395 / 6.991 / 6.991 / 7.029 | 8.9 / 2.0 / 1.8 / 2.5 / 2.4 | 1/1 / 1/1 / 1/1 / 1/1 / 1/1 |

## Promedios y totales

- **`completo`:** 73 fuentes citadas (4.9 por pregunta), DOI 59/73, ~412.055 tokens de entrada, 8.76 s promedio
- **`rag`:** 51 fuentes citadas (3.4 por pregunta), DOI 42/51, ~7.323 tokens de entrada, 4.60 s promedio
- **`hibrido-0.3`:** 62 fuentes citadas (4.1 por pregunta), DOI 45/62, ~6.767 tokens de entrada, 4.60 s promedio
- **`hibrido-0.5`:** 49 fuentes citadas (3.3 por pregunta), DOI 37/49, ~6.700 tokens de entrada, 4.36 s promedio
- **`hibrido-0.7`:** 36 fuentes citadas (2.4 por pregunta), DOI 29/36, ~6.740 tokens de entrada, 3.66 s promedio

## Detalle por pregunta

### 1. Definición
**Pregunta:** ¿Qué es una vega y en qué se diferencia de un bofedal?

#### Modo `completo` (DeepSeek, ~412044 tok, 15.9 s, DOI: 2/3)

¡Buena pregunta, che! Es un lío de nombres que viene de lejos. En la Puna argentina usamos "vega" para casi todo, pero en la literatura hay una distinción que conviene conocer.

Por un lado, hay una propuesta que reserva "vega" o "ciénaga" para praderas húmedas sin turba, de 3.000 a 4.000 m, a menudo sin manejo, y "bofedal" para humedales de 3.500 a 5.000 m, con turba y manejados por los pastores (Yager et al., 2021). Pero ojo: en la Puna argentina el término "vega" también designa humedales con capas de turba de varios metros, como la de Cerro Tuzgle (Carilla et al., 2018). De hecho, una revisión de 119 trabajos encontró 128 sinónimos y definiciones contradictorias, y en Argentina ni siquiera se usan los términos indígenas (White-Nockleby et al., 2021).

Así que, en criollo: la distinción vega/bofedal es útil para entenderse con colegas de Perú o Bolivia, pero en casa "vega" abarca todo el combo.

Fuentes:
Yager, K., Prieto, M., & Meneses, R. I. (2021). Reframing pastoral practices of bofedal management to increase the resilience of Andean water towers. Mountain Research and Development, 41(4), A1-A9. https://doi.org/10.1659/MRD-JOURNAL-D-21-00011.1
Carilla, J., Grau, A., & Cuello, S. (2018). Vegetación de la Puna argentina. En H. R. Grau, M. J. Babot, A. E. Izquierdo y A. Grau (Eds.), Puna argentina: naturaleza y cultura (Serie Conservación de la Naturaleza, 24, pp. 143-156). Fundación Miguel Lillo.
White-Nockleby, C., Prieto, M., Yager, K., & Meneses, R. I. (2021). Understanding bofedales as cultural landscapes in the Central Andes. Wetlands, 41, 102. https://doi.org/10.1007/s13157-021-01500-y

#### Modo `rag` (DeepSeek, búsqueda bm25, ~7397 tok, 3.1 s, DOI: 1/2)

¡Buena pregunta, che! Mirá, en los estudios que conozco el término "vega andina" se usa para humedales azonales de la zona andina, alimentados por aguas minerales que vienen de laderas o cuencas; en el norte de Chile también se los llama bofedal (Squeo et al., 2006). Y "bofedal" es el término andino para los humedales de alta montaña: hay autores que proponen usarlo para cualquier humedal de alta montaña de la puna, sin importar la vegetación dominante ni el tipo de suelo, y después precisar si es turbera, pradera húmeda u otro (Chimner et al., 2019).

Ojo que la distinción no siempre es tan nítida: en la práctica los dos términos se solapan bastante según la región y el autor. Lo que sí conviene separar es el tipo de suelo: una vega o turbera tiene suelo orgánico de 40 cm o más, mientras que una pradera húmeda se satura solo estacionalmente y tiene menos de 40 cm de materia orgánica (Chimner et al., 2019; Squeo et al., 2006).

Fuentes:
Squeo, F. A., Ibacache, E., Warner, B., Espinoza, D., Aravena, R., & Gutiérrez, J. R. (2006). Productividad y diversidad florística de la Vega Tambo, Cordillera de Doña Ana. En Geoecología de los Andes desérticos. La Alta Montaña del Valle del Elqui (pp. 1-27).
Chimner, R. A., Bourgeau-Chavez, L., Grelik, S., Hribljan, J. A., Planas Clarke, A. M., Polk, M. H., Lilleskov, E. A., & Fuentealba, B. (2019). Mapping mountain peatlands and wet meadows using multi-date, multi-sensor remote sensing in the Cordillera Blanca, Peru. Wetlands. https://doi.org/10.1007/s13157-019-01134-1

#### Modo `hibrido-0.3` (DeepSeek, búsqueda hibrida, ~6976 tok, 3.8 s, DOI: 4/6)

¡Buena pregunta! En el norte de Chile y el noroeste argentino conviven los términos "vega", "bofedal" y "ciénago" para nombrar estos humedales (Gonnet et al., 2016). Los estudios de campo coinciden en que las turberas puneñas son *fens* minerotróficos alimentados por agua subterránea, vertientes y arroyos, y no turberas ombrotróficas (Cooper et al., 2010; Ruthsatz, 2012; Salvador et al., 2014; Chimner et al., 2019).

Ahora, ojo: no todos usan las palabras igual. Una corriente propone distinguir "vega" o "ciénaga" (praderas húmedas sin turba, de 3.000–4.000 m, a menudo sin manejo) frente a "bofedal" (3.500–5.000 m, con turba y manejo pastoril) (Yager et al., 2021). Pero otros autores recomiendan usar "bofedal" como paraguas para cualquier humedal altoandino de puna (Chimner et al., 2019). Así que la diferencia depende de qué definición sigas.

Fuentes:
Gonnet, J. M., Lopez, C., Aranibar, D. E., & Lictevout, E. (2016). Manual introductorio al manejo de vegas y bofedales mediante prácticas tradicionales de culturas andinas en el norte de Chile. Corporación Norte Grande.
Cooper, D. J., Wolf, E. C., Colson, C., Vering, W., Granda, A., & Meyer, M. (2010). Alpine peatlands of the Andes, Cajamarca, Peru. Arctic, Antarctic, and Alpine Research, 42(1), 19-33. https://doi.org/10.1657/1938-4246-42.1.19
Ruthsatz, B. (2012). Vegetación y ecología de los bofedales altoandinos de Bolivia (C. Pérez, Trad.). Phytocoenologia, 42(3-4), 133-179. https://doi.org/10.1127/0340-269X/2012/0042-0535
Salvador, F., Monerris, J., & Rochefort, L. (2014). Peatlands of the Peruvian Puna ecoregion: types, characteristics and disturbance. Mires and Peat, 15(03), 1–17.
Chimner, R. A., Bourgeau-Chavez, L., Grelik, S., Hribljan, J. A., Planas Clarke, A. M., Polk, M. H., Lilleskov, E. A., & Fuentealba, B. (2019). Mapping mountain peatlands and wet meadows using multi-date, multi-sensor remote sensing in the Cordillera Blanca, Peru. Wetlands. https://doi.org/10.1007/s13157-019-01134-1
Yager, K., Prieto, M., & Meneses, R. I. (2021). Reframing pastoral practices of bofedal management to increase the resilience of Andean water towers. Mountain Research and Development, 41(4), A1-A9. https://doi.org/10.1659/MRD-JOURNAL-D-21-00011.1

#### Modo `hibrido-0.5` (DeepSeek, búsqueda hibrida, ~7384 tok, 4.3 s, DOI: 3/4)

¡Hola! Buena pregunta, y bien de entrada te digo que la respuesta depende de dónde estés parado, porque los nombres cambian según el país.

En los Andes Centrales, "bofedal" es el término más usado (aparece en 92 de 119 trabajos de una revisión) y suele reservarse para formaciones de cojines duros de juncáceas como *Distichia*, *Oxychloe* y *Patosia*, o de la ciperácea *Zameioscirpus atacamensis* en sitios muy salinos, que forman turberas minerotróficas alimentadas por vertientes (Ruthsatz, 2012). En cambio, "vega", "ciénaga" o "humedal" se usan más en altitudes medias (unos 3000-4000 m) para praderas húmedas sin turba, de menor valor forrajero y a menudo sin manejo pastoril (Yager et al., 2021). En el norte de Chile y el noroeste argentino, "vega" se usa justamente para lo que en Bolivia se llama bofedal y otros humedales (Ruthsatz, 2012).

Ojo con un detalle importante: la vegetación sola no alcanza para diagnosticar turba. En Huascarán, cerca de un cuarto de los humedales de cojines no eran turberas, así que hay que mirar el suelo (Chimner et al., 2019). Y en la Puna argentina se propuso el concepto de "hidroecosistema" para agrupar humedales colindantes e interdependientes, como salares, lagunas, vegas salitrosas y vegas (Izquierdo et al., 2016).

Fuentes:
Ruthsatz, B. (2012). Vegetación y ecología de los bofedales altoandinos de Bolivia (C. Pérez, Trad.). Phytocoenologia, 42(3-4), 133-179. https://doi.org/10.1127/0340-269X/2012/0042-0535
Yager, K., Prieto, M., & Meneses, R. I. (2021). Reframing pastoral practices of bofedal management to increase the resilience of Andean water towers. Mountain Research and Development, 41(4), A1-A9. https://doi.org/10.1659/MRD-JOURNAL-D-21-00011.1
Chimner, R. A., Bourgeau-Chavez, L., Grelik, S., Hribljan, J. A., Planas Clarke, A. M., Polk, M. H., Lilleskov, E. A., & Fuentealba, B. (2019). Mapping mountain peatlands and wet meadows using multi-date, multi-sensor remote sensing in the Cordillera Blanca, Peru. Wetlands. https://doi.org/10.1007/s13157-019-01134-1
Izquierdo, A. E., Foguet, J., & Grau, H. R. (2016). “Hidroecosistemas” de la Puna y Altos Andes de Argentina. Acta Geológica Lilloana, 28(2), 390–402.

#### Modo `hibrido-0.7` (DeepSeek, búsqueda hibrida, ~7164 tok, 2.6 s, DOI: 1/1)

¡Hola! Buena pregunta, y ojo que la respuesta depende de dónde estés parado. En el norte de Argentina y Chile se usa "vega" para lo que en Bolivia se llama "bofedal" y otros humedales en general: son términos más amplios que abarcan todos los ambientes húmedos (Ruthsatz, 2012). En cambio, en sentido estricto, el bofedal son las formaciones de cojines duros de juncáceas (Distichia, Oxychloe, Patosia) o, en sitios muy salinos, de la ciperácea Zameioscirpus atacamensis, que forman turberas alimentadas por agua de vertientes (Ruthsatz, 2012). Y más que una cubierta pura de cojines, conviene pensarlo como un "complejo de bofedal": un mosaico de cojines formadores de turba, céspedes de ciperáceas, pozas, cauces, vertientes, ecotonos y sectores halófilos (Ruthsatz, 2012).

Fuentes:
Ruthsatz, B. (2012). Vegetación y ecología de los bofedales altoandinos de Bolivia (C. Pérez, Trad.). Phytocoenologia, 42(3-4), 133-179. https://doi.org/10.1127/0340-269X/2012/0042-0535

---

### 2. Puna argentina vs. otros países
**Pregunta:** ¿Qué diferencias hay entre los estudios sobre vegas en la Puna argentina y los de Bolivia, Perú o Chile?

#### Modo `completo` (DeepSeek, ~412056 tok, 8.4 s, DOI: 6/11)

¡Qué linda pregunta! Y bien de fondo, porque no es lo mismo estudiar una vega jujeña que un bofedal boliviano. Te resumo lo que dicen los trabajos que conozco:

- **Cantidad y tradición de estudio:** Argentina fue históricamente el país menos representado en la literatura andina sobre bofedales: solo 9 de 119 trabajos entre 1977 y 2018, frente a 49 de Bolivia, 41 de Perú y 31 de Chile, y sin términos indígenas en los estudios argentinos (White-Nockleby et al., 2021). En cambio, en los últimos años se consolidó una base propia de la Puna argentina: inventarios regionales, ordenación multitaxón de 47 vegas y modelado espacial de ensambles (Izquierdo et al., 2018; Izquierdo et al., 2020; Casagranda y Izquierdo, 2023).

- **Terminología:** en Bolivia, Perú y el norte de Chile se habla de "bofedal" (y de *oqho*, *hoq'o*, *waylla*), mientras en el noroeste argentino se usa "vega" o "ciénego" (Gonnet et al., 2016; White-Nockleby et al., 2021). Y hay un choque: algunos proponen reservar "bofedal" para turberas manejadas con turba y "vega" para praderas sin turba (Yager et al., 2021), pero en la Puna argentina "vega" designa también humedales con capas de turba de varios metros (Carilla et al., 2018).

- **Enfoque de los estudios:** en los países vecinos abundan los estudios de campo sobre turba, hidrología, carbono y manejo tradicional del riego (Cooper et al., 2010; Hribljan et al., 2015; Verzijl y Guerrero Quispe, 2013; García Barriga et al., 2026). En Argentina predominan los inventarios satelitales, el modelado de nicho, la biodiversidad multitaxonómica y el análisis del pastoreo y el reasilvestramiento (Izquierdo et al., 2016; Navarro et al., 2023).

- **Un vacío compartido y otro propio:** en toda la región falta cuantificar qué superficie de bofedal depende del riego humano (White-Nockleby et al., 2021), y en Argentina además faltan mediciones de campo de napa, flujos de gases y balances hídricos instrumentados, que sí existen en Perú, Bolivia y Chile (Cooper et al., 2019; Valois et al., 2020; Chiappero et al., 2024).

Fuentes:
White-Nockleby, C., Prieto, M., Yager, K., & Meneses, R. I. (2021). Understanding bofedales as cultural landscapes in the Central Andes. Wetlands, 41, 102. https://doi.org/10.1007/s13157-021-01500-y
Izquierdo, A. E., Aragón, R., Navarro, C. J., & Casagranda, E. (2018). Humedales de la Puna: principales proveedores de servicios ecosistémicos de la región. En H. R. Grau, M. J. Babot, A. Izquierdo y A. Grau (Eds.), La Puna argentina: naturaleza y cultura (Serie Conservación de la Naturaleza, 24, pp. 96-111). Fundación Miguel Lillo.
Izquierdo, A. E., Carilla, J., Nieto, C., Osinaga Acosta, O., Martin, E., Grau, H. R., & Reynaga, M. C. (2020). Multi-taxon patterns from high Andean peatlands: Assessing climatic and landscape variables. Community Ecology. https://doi.org/10.1007/s42974-020-00029-0
Casagranda, E., & Izquierdo, A. E. (2023). Modeling the potential distribution of floristic assemblages of high Andean wetlands dominated by Juncaceae and Cyperaceae in the Argentine Puna. Vegetation Classification and Survey, 4, 47-58. https://doi.org/10.3897/VCS.95779
Gonnet, J. M., Lopez, C., Aranibar, D. E., & Lictevout, E. (2016). Manual introductorio al manejo de vegas y bofedales mediante prácticas tradicionales de culturas andinas en el norte de Chile. Corporación Norte Grande.
Yager, K., Prieto, M., & Meneses, R. I. (2021). Reframing pastoral practices of bofedal management to increase the resilience of Andean water towers. Mountain Research and Development, 41(4), A1-A9. https://doi.org/10.1659/MRD-JOURNAL-D-21-00011.1
Carilla, J., Grau, A., & Cuello, S. (2018). Vegetación de la Puna argentina. En H. R. Grau, M. J. Babot, A. E. Izquierdo y A. Grau (Eds.), Puna argentina: naturaleza y cultura (Serie Conservación de la Naturaleza, 24, pp. 143-156). Fundación Miguel Lillo.
Cooper, D. J., Wolf, E. C., Colson, C., Vering, W., Granda, A., & Meyer, M. (2010). Alpine peatlands of the Andes, Cajamarca, Peru. Arctic, Antarctic, and Alpine Research, 42(1), 19-33. https://doi.org/10.1657/1938-4246-42.1.19
Hribljan, J. A., Cooper, D. J., Sueltenfuss, J., Wolf, E. C., Heckman, K. A., Lilleskov, E. A., & Chimner, R. A. (2015). Carbon storage and long-term rate of accumulation in high-altitude Andean peatlands of Bolivia. Mires and Peat, 15(12), 1–14.
Verzijl, A., & Guerrero Quispe, S. (2013). The system nobody sees: Irrigated wetland management and alpaca herding in the Peruvian Andes. Mountain Research and Development, 33(3), 280-293. https://doi.org/10.1659/MRD-JOURNAL-D-12-00123.1
García Barriga, M., Oyaneder, A., Sitz

#### Modo `rag` (DeepSeek, búsqueda bm25, ~7477 tok, 3.0 s, DOI: 2/2)

¡Buena pregunta! La diferencia más marcada es de cantidad: en la revisión de 119 publicaciones sobre bofedales (1977-2018), solo 9 estudios incluyen sitios de Argentina, frente a 49 de Bolivia, 41 de Perú y 31 de Chile (White-Nockleby et al., 2021). Además, ningún estudio de Argentina o Chile usa términos indígenas como oqho o waylla, que sí aparecen en trabajos de Bolivia y Perú (White-Nockleby et al., 2021).

También hay una diferencia de enfoque: la mitad de los trabajos de ciencias sociales y multidisciplinarios menciona prácticas de manejo comunitario, mientras que en los de ciencias naturales esa proporción baja a un cuarto (White-Nockleby et al., 2021). Y ojo con la terminología: en la Puna argentina "vega" suele designar también humedales con turba, mientras que en buena parte de la literatura de Bolivia y Chile "vega" se reserva para praderas húmedas sin turba de menor altitud (Yager et al., 2021).

Fuentes:
Yager, K., Prieto, M., & Meneses, R. I. (2021). Reframing pastoral practices of bofedal management to increase the resilience of Andean water towers. Mountain Research and Development, 41(4), A1-A9. https://doi.org/10.1659/MRD-JOURNAL-D-21-00011.1
White-Nockleby, C., Prieto, M., Yager, K., & Meneses, R. I. (2021). Understanding bofedales as cultural landscapes in the Central Andes. Wetlands, 41, 102. https://doi.org/10.1007/s13157-021-01500-y

#### Modo `hibrido-0.3` (DeepSeek, búsqueda hibrida, ~7446 tok, 4.0 s, DOI: 3/3)

¡Buena pregunta! La diferencia más marcada es de cantidad y de enfoque. En la revisión de 119 publicaciones sobre bofedales de los Andes Centrales (1977-2018), solo 9 estudios tenían sitios en Argentina, frente a 49 en Bolivia, 41 en Perú y 31 en Chile; además, los trabajos argentinos no usaban términos indígenas ni había estudios multidisciplinarios recientes (White-Nockleby et al., 2021).

En cuanto al enfoque, la revisión muestra que en ciencias naturales las amenazas más citadas son el sobrepastoreo y el cambio climático (38 menciones cada una), seguidas por minería (26) y uso de agua (18), mientras que en ciencias sociales encabezan las políticas estatales (14) y el mercado (9) (White-Nockleby et al., 2021). Ojo: esos conteos son de toda la región, no desagregados por país.

Un contraste interesante es que en la Puna argentina ya hay estudios regionales propios, como el relevamiento de 8.134 vegas (110.895 ha, 0,78 % del territorio) y el análisis de cómo el ganado actual explica menos del 0,1 % de la variación del NDVI (Navarro et al., 2020). En cambio, en Perú el pastoreo ovino a escala local se vinculó con bajo oxígeno disuelto y deterioro de índices bióticos acuáticos (Quispe Mamani et al., 2021): son escalas distintas, así que conviene no trasladar conclusiones de un país a otro sin cuidado.

Fuentes:
White-Nockleby, C., Prieto, M., Yager, K., & Meneses, R. I. (2021). Understanding bofedales as cultural landscapes in the Central Andes. Wetlands, 41, 102. https://doi.org/10.1007/s13157-021-01500-y
Navarro, C. J., Izquierdo, A. E., Aráoz, E., Foguet, J., & Grau, H. R. (2020). Rewilding of large herbivore communities in high elevation Puna: Geographic segregation and no evidence of positive effects on peatland productivity. Regional Environmental Change, 20, 112. https://doi.org/10.1007/s10113-020-01704-8
Quispe Mamani, M. C., Villasante Benavides, J. F., Feriz García, D., Luque-Fernández, C. R., Pauca Tanco, A., & Villegas Paredes, L. N. (2021). Diversity of aquatic macroinvertebrates and water quality of the High Andean wetlands of Chalhuanca, Arequipa-Peru. Biodiversity Journal, 12(2), 517-528. https://doi.org/10.31396/Biodiv.Jour.2021.12.2.517.528

#### Modo `hibrido-0.5` (DeepSeek, búsqueda hibrida, ~7062 tok, 3.2 s, DOI: 3/4)

¡Buena pregunta! La diferencia más fuerte es de cantidad: en la revisión de 119 publicaciones sobre bofedales de los Andes Centrales (1977-2018), solo 9 estudios tenían sitios en Argentina, frente a 49 en Bolivia, 41 en Perú y 31 en Chile (White-Nockleby et al., 2021). Además, esos trabajos argentinos casi no usan términos indígenas ni hay estudios multidisciplinarios recientes sobre el tema (White-Nockleby et al., 2021).

Ojo con la terminología: en la Puna argentina "vega" suele designar también humedales con turba, mientras que en Bolivia y Chile "bofedal" refiere más estrictamente a los parches de plantas en cojín con humedad constante (Yager et al., 2021; Gonnet et al., 2016). Y hay un dato ecológico propio de Argentina: las 8.134 vegas puneñas ocupan 110.895 ha (0,78–0,8 % del territorio), y el 58 % mide menos de 5 ha, lo que las hace más vulnerables al cambio climático (Navarro et al., 2020).

Fuentes:
Yager, K., Prieto, M., & Meneses, R. I. (2021). Reframing pastoral practices of bofedal management to increase the resilience of Andean water towers. Mountain Research and Development, 41(4), A1-A9. https://doi.org/10.1659/MRD-JOURNAL-D-21-00011.1
Gonnet, J. M., Lopez, C., Aranibar, D. E., & Lictevout, E. (2016). Manual introductorio al manejo de vegas y bofedales mediante prácticas tradicionales de culturas andinas en el norte de Chile. Corporación Norte Grande.
White-Nockleby, C., Prieto, M., Yager, K., & Meneses, R. I. (2021). Understanding bofedales as cultural landscapes in the Central Andes. Wetlands, 41, 102. https://doi.org/10.1007/s13157-021-01500-y
Navarro, C. J., Izquierdo, A. E., Aráoz, E., Foguet, J., & Grau, H. R. (2020). Rewilding of large herbivore communities in high elevation Puna: Geographic segregation and no evidence of positive effects on peatland productivity. Regional Environmental Change, 20, 112. https://doi.org/10.1007/s10113-020-01704-8

#### Modo `hibrido-0.7` (DeepSeek, búsqueda hibrida, ~7062 tok, 3.3 s, DOI: 3/3)

¡Hola! Muy buena pregunta, y tiene que ver con lo que más me gusta rumiar mientras pasto: cuánta investigación se hace en cada rincón de los Andes. La revisión de White-Nockleby y colegas encontró que Argentina es el país con menos estudios de bofedales: solo 9 de 119 publicaciones, frente a 49 de Bolivia, 41 de Perú y 31 de Chile, y sin términos indígenas ni trabajos multidisciplinarios recientes (White-Nockleby et al., 2021). Además, la mayoría de la literatura (68 %) viene de las ciencias naturales, con menos peso de las sociales (18,5 %) y las multidisciplinarias (13,4 %) (White-Nockleby et al., 2021).

Ojo con un matiz: esos 119 trabajos son la base de una revisión sobre bofedales en los Andes Centrales, y en la Puna argentina "vega" suele designar también humedales con turba, así que la comparación terminológica no es directa (Yager et al., 2021). Igual, la base faunística argentina existe y es propia: 8.134 vegas que ocupan 110.895 ha, un 0,78–0,8 % del territorio (Navarro et al., 2020).

Fuentes:
White-Nockleby, C., Prieto, M., Yager, K., & Meneses, R. I. (2021). Understanding bofedales as cultural landscapes in the Central Andes. Wetlands, 41, 102. https://doi.org/10.1007/s13157-021-01500-y
Yager, K., Prieto, M., & Meneses, R. I. (2021). Reframing pastoral practices of bofedal management to increase the resilience of Andean water towers. Mountain Research and Development, 41(4), A1-A9. https://doi.org/10.1659/MRD-JOURNAL-D-21-00011.1
Navarro, C. J., Izquierdo, A. E., Aráoz, E., Foguet, J., & Grau, H. R. (2020). Rewilding of large herbivore communities in high elevation Puna: Geographic segregation and no evidence of positive effects on peatland productivity. Regional Environmental Change, 20, 112. https://doi.org/10.1007/s10113-020-01704-8

---

### 3. Cifras concretas
**Pregunta:** ¿Cuántas vegas y qué superficie total se registraron en la Puna argentina según la bibliografía?

#### Modo `completo` (DeepSeek, ~412054 tok, 5.2 s, DOI: 4/4)

¡Hola! Qué lindo poder contarte esto, porque es una de las preguntas más frecuentes y la respuesta tiene su matiz. Según los inventarios satelitales, en la Puna argentina se mapearon **8134 vegas que suman unas 110.895 ha** (0,78 % del territorio), con el 58 % de las unidades menores a 5 ha (Navarro et al., 2020) (Izquierdo et al., 2018). Pero ojo: las cifras cambian según el recorte y el método, porque otro trabajo sobre ~12 millones de ha contabilizó **8593 vegas que cubren 54.880 ha** (Casagranda y Izquierdo, 2023), y un mapeo previo había estimado 94.427,55 ha (161.402 ha corregidas) (Izquierdo et al., 2015).

Fuentes:
Navarro, C. J., Izquierdo, A. E., Aráoz, E., Foguet, J., & Grau, H. R. (2020). Rewilding of large herbivore communities in high elevation Puna: Geographic segregation and no evidence of positive effects on peatland productivity. Regional Environmental Change, 20, 112. https://doi.org/10.1007/s10113-020-01704-8
Izquierdo, A. E., Grau, H. R., Navarro, C. J., Casagranda, E., Castilla, M. C., & Grau, A. (2018). Highlands in transition: Urbanization, pastoralism, mining, tourism, and wildlife in the Argentinian Puna. Mountain Research and Development, 38(4), 390-400. https://doi.org/10.1659/MRD-JOURNAL-D-17-00075.1
Casagranda, E., & Izquierdo, A. E. (2023). Modeling the potential distribution of floristic assemblages of high Andean wetlands dominated by Juncaceae and Cyperaceae in the Argentine Puna. Vegetation Classification and Survey, 4, 47-58. https://doi.org/10.3897/VCS.95779
Izquierdo, A. E., Foguet, J., & Grau, H. R. (2015). Mapping and spatial characterization of Argentine High Andean peatbogs. Wetlands Ecology and Management. https://doi.org/10.1007/s11273-015-9433-3

#### Modo `rag` (DeepSeek, búsqueda bm25, ~7390 tok, 2.0 s, DOI: 1/2)

Según el inventario regional de humedales de la Puna argentina, las vegas cubren unas 110.895 ha (Izquierdo et al., 2016). En cuanto al número de unidades, en los fragmentos que tengo a mano no aparece un conteo de vegas: lo que sí figura es que se mapearon 33 salares y 113 lagos y lagunas (Izquierdo et al., 2016). Como referencia de magnitud, las vegas ocupan solo el 0,78 % de la Puna argentina (Navarro et al., 2020).

Fuentes:
Izquierdo, A. E., Foguet, J., & Grau, H. R. (2016). “Hidroecosistemas” de la Puna y Altos Andes de Argentina. Acta Geológica Lilloana, 28(2), 390–402.
Navarro, C. J., Izquierdo, A. E., Aráoz, E., Foguet, J., & Grau, H. R. (2020). Rewilding of large herbivore communities in high elevation Puna: Geographic segregation and no evidence of positive effects on peatland productivity. Regional Environmental Change, 20, 112. https://doi.org/10.1007/s10113-020-01704-8

#### Modo `hibrido-0.3` (DeepSeek, búsqueda hibrida, ~7060 tok, 2.7 s, DOI: 3/5)

En la Puna argentina se mapearon primero 94.427,55 ha de vegas (0,66 % del área, 10.428 polígonos) (Izquierdo et al., 2015), y el inventario actualizado distinguió 110.895 ha de vegas (0,78 %; 8134 unidades) dentro de 866.580 ha de humedales (Izquierdo et al., 2016) (Izquierdo et al., 2018) (Navarro et al., 2020) (Izquierdo et al., 2020). Ojo: son dos momentos distintos del mapeo, no cifras contradictorias.

Fuentes:
Izquierdo, A. E., Foguet, J., & Grau, H. R. (2015). Mapping and spatial characterization of Argentine High Andean peatbogs. Wetlands Ecology and Management. https://doi.org/10.1007/s11273-015-9433-3
Izquierdo, A. E., Foguet, J., & Grau, H. R. (2016). “Hidroecosistemas” de la Puna y Altos Andes de Argentina. Acta Geológica Lilloana, 28(2), 390–402.
Izquierdo, A. E., Aragón, R., Navarro, C. J., & Casagranda, E. (2018). Humedales de la Puna: principales proveedores de servicios ecosistémicos de la región. En H. R. Grau, M. J. Babot, A. Izquierdo y A. Grau (Eds.), La Puna argentina: naturaleza y cultura (Serie Conservación de la Naturaleza, 24, pp. 96-111). Fundación Miguel Lillo.
Navarro, C. J., Izquierdo, A. E., Aráoz, E., Foguet, J., & Grau, H. R. (2020). Rewilding of large herbivore communities in high elevation Puna: Geographic segregation and no evidence of positive effects on peatland productivity. Regional Environmental Change, 20, 112. https://doi.org/10.1007/s10113-020-01704-8
Izquierdo, A. E., Carilla, J., Nieto, C., Osinaga Acosta, O., Martin, E., Grau, H. R., & Reynaga, M. C. (2020). Multi-taxon patterns from high Andean peatlands: Assessing climatic and landscape variables. Community Ecology. https://doi.org/10.1007/s42974-020-00029-0

#### Modo `hibrido-0.5` (DeepSeek, búsqueda hibrida, ~7169 tok, 2.8 s, DOI: 3/4)

¡Hola! Según los inventarios que conozco, hay dos cifras que conviene no mezclar. El primer mapeo regional registró 94.427,55 ha de vegas (0,66 % del área, en 10.428 polígonos), con una estimación corregida de 161.402 ha (Izquierdo et al., 2015). El inventario actualizado distinguió 110.895 ha de vegas (0,78 %, en 8134 unidades) dentro de un total de 866.580 ha de humedales (Izquierdo et al., 2016; Navarro et al., 2020). Y en el área de estudio del modelado florístico se contaron 8.593 vegas que suman 54.880 ha (Casagranda y Izquierdo, 2023).

Fuentes:
Izquierdo, A. E., Foguet, J., & Grau, H. R. (2015). Mapping and spatial characterization of Argentine High Andean peatbogs. Wetlands Ecology and Management. https://doi.org/10.1007/s11273-015-9433-3
Izquierdo, A. E., Foguet, J., & Grau, H. R. (2016). “Hidroecosistemas” de la Puna y Altos Andes de Argentina. Acta Geológica Lilloana, 28(2), 390–402.
Navarro, C. J., Izquierdo, A. E., Aráoz, E., Foguet, J., & Grau, H. R. (2020). Rewilding of large herbivore communities in high elevation Puna: Geographic segregation and no evidence of positive effects on peatland productivity. Regional Environmental Change, 20, 112. https://doi.org/10.1007/s10113-020-01704-8
Casagranda, E., & Izquierdo, A. E. (2023). Modeling the potential distribution of floristic assemblages of high Andean wetlands dominated by Juncaceae and Cyperaceae in the Argentine Puna. Vegetation Classification and Survey, 4, 47-58. https://doi.org/10.3897/VCS.95779

#### Modo `hibrido-0.7` (DeepSeek, búsqueda hibrida, ~7118 tok, 2.5 s, DOI: 1/2)

Según el inventario regional actualizado, en la Puna argentina se mapearon **110.895 ha de vegas** (0,78 % del área), distribuidas en **8134 unidades**, con una precisión del mapa de 87,15 % (Izquierdo et al., 2016). Ese inventario forma parte de un total de 866.580 ha de humedales, que además incluye 61.123 ha de vegas salitrosas de transición, 654.076 ha de salares y 40.486 ha de cuerpos de agua (Izquierdo et al., 2016).

Un mapeo anterior, sobre 14,3 millones de ha, había registrado 94.427,55 ha (0,66 %; 10.428 polígonos; 85,5 % de exactitud), con una estimación corregida de 161.402 ha (Izquierdo et al., 2015). Ojo que las cifras no son del todo comparables: el inventario más reciente actualizó el mapa de vegas y mejoró la precisión, por eso el número de hectáreas y de unidades cambia entre ambos trabajos.

Fuentes:
Izquierdo, A. E., Foguet, J., & Grau, H. R. (2016). “Hidroecosistemas” de la Puna y Altos Andes de Argentina. Acta Geológica Lilloana, 28(2), 390–402.
Izquierdo, A. E., Foguet, J., & Grau, H. R. (2015). Mapping and spatial characterization of Argentine High Andean peatbogs. Wetlands Ecology and Management. https://doi.org/10.1007/s11273-015-9433-3

---

### 4. Pastoreo
**Pregunta:** ¿Cómo afecta el pastoreo de camélidos y ganado a las vegas y bofedales?

#### Modo `completo` (DeepSeek, ~412048 tok, 6.3 s, DOI: 5/6)

¡Buena pregunta! Te cuento lo que muestran los estudios, que no siempre coinciden entre sí.

En varios trabajos se documenta que el pastoreo continuo e intenso degrada los bofedales: rompe los cojines que funcionan como diques, reduce el agua superficial y favorece gramíneas menos palatables (Cochi Machaca et al., 2018). En Nor Yauyos-Cochas (Perú), cargas altas con vacunos y zanjas redujeron la cobertura de *Distichia muscoides* y bajaron la conductividad hidráulica superficial de la turba (Oyague et al., 2022). Además, el ganado con pezuña compacta más que los camélidos (Cochi Machaca et al., 2018).

Pero en la Puna argentina la evidencia es más matizada: en los ciénegos de Suripujio (Jujuy) bajo pastoreo móvil tradicional no se detectó degradación lineal (Quiroga Mendiola, 2012), y en 50 vegas relevadas solo el 6 % superó las cargas recomendadas, con mayor diversidad de plantas y macroinvertebrados en vegas pastoreadas que en las reasilvestradas (Navarro et al., 2023). A escala regional, la accesibilidad ganadera explicó menos del 1 % de la variación del NDVI de 8134 vegas (Navarro et al., 2020).

Un dato clave: el ganado doméstico se concentra en las vegas cercanas a los poblados y desplaza espacialmente a las vicuñas, que quedan en hábitats subóptimos pese a un solapamiento dietario mayor al 70 % (Borgnia et al., 2008).

Fuentes:
Cochi Machaca, N., Condori, B., Rojas Pardo, A., Anthelme, F., Meneses, R. I., Weeda, C. E., & Perotto-Baldivieso, H. L. (2018). Effects of grazing pressure on plant species composition and water presence on bofedales in the Andes mountain range of Bolivia. Mires and Peat, 21, Article 15, 1-15. https://doi.org/10.19189/MaP.2017.OMB.303
Oyague, E., Cooper, D. J., & Ingol, E. (2022). Effects of land use on the hydrologic regime, vegetation, and hydraulic conductivity of peatlands in the central Peruvian Andes. Journal of Hydrology, 609, 127687. https://doi.org/10.1016/j.jhydrol.2022.127687
Quiroga Mendiola, M. (2012). Sociedades y agroecosistemas pastoriles de alta montaña en la Puna. Departamento Yavi, Provincia de Jujuy, República Argentina [Tesis doctoral en Ciencias Agropecuarias]. Universidad Nacional de Córdoba, Facultad de Ciencias Agropecuarias.
Navarro, C. J., Carilla, J., Osinaga Acosta, O., Nieto, C., Ovejero, R., & Grau, H. R. (2023). Herbivore rewilding does not promote biodiversity in Argentine Andean peatlands. Anthropocene, 42, 100382. https://doi.org/10.1016/j.ancene.2023.100382
Navarro, C. J., Izquierdo, A. E., Aráoz, E., Foguet, J., & Grau, H. R. (2020). Rewilding of large herbivore communities in high elevation Puna: Geographic segregation and no evidence of positive effects on peatland productivity. Regional Environmental Change, 20, 112. https://doi.org/10.1007/s10113-020-01704-8
Borgnia, M., Vilá, B. L., & Cassini, M. H. (2008). Interaction between wild camelids and livestock in an Andean semi-desert. Journal of Arid Environments, 72, 2150-2158. https://doi.org/10.1016/j.jaridenv.2008.07.012

#### Modo `rag` (DeepSeek, búsqueda bm25, ~7418 tok, 4.3 s, DOI: 5/5)

¡Hola! Qué linda pregunta, y bien de campo. Te cuento lo que muestran los estudios, con un detalle importante: hay evidencia de Bolivia y Chile además de la Argentina, así que lo aclaro cuando corresponde.

- **El ganado doméstico se queda con las mejores vegas.** En 50 vegas de la Puna argentina (3.200–4.700 m), 28 fueron usadas solo por ganado doméstico, 13 solo por herbívoros silvestres y apenas 9 (18 %) por ambos; la densidad de vicuñas subía con la distancia a los poblados (r = 0,38) (Navarro et al., 2020). En Laguna Blanca (Catamarca) los pastores concentran el ganado en las vegas (81,4 % a menos de 1 km de los asentamientos, frente a 11,7 % de las vicuñas), pese a un solapamiento dietario mayor al 70 % (Borgnia et al., 2008).
- **En Bolivia, el "sobrepastoreo" no explica todo.** En el altiplano de Tarija los bofedales son recurso clave de invierno y soportan cargas altas, pero la biomasa depende más de la lluvia y la salinidad que del número de animales; los autores consideran engañoso el término sobrepastoreo (Preston et al., 2003).
- **En Chile, el ganado se asocia a los bofedales.** La superficie de bofedal se correlacionó con el ganado doméstico (r² = 0,67) pero no con la vicuña (Shaw et al., 2012).
- **El reemplazo por camélidos silvestres no aumentó la productividad ni la biodiversidad de las turberas** en la Puna argentina (Navarro et al., 2020; Navarro et al., 2023).

Fuentes:
Preston, D., Fairbairn, J., Paniagua, N., Maas, G., Yevara, M., & Beck, S. (2003). Grazing and environmental change on the Tarija altiplano, Bolivia. Mountain Research and Development, 23(2), 141-148. https://doi.org/10.1659/0276-4741(2003)023[0141:GAECOT]2.0.CO;2
Shaw, A. K., Galaz, J. L., & Marquet, P. A. (2012). Population dynamics of the vicuña (Vicugna vicugna): density-dependence, rainfall, and spatial distribution. Journal of Mammalogy, 93(3), 658-666. https://doi.org/10.1644/11-MAMM-A-257.1
Navarro, C. J., Izquierdo, A. E., Aráoz, E., Foguet, J., & Grau, H. R. (2020). Rewilding of large herbivore communities in high elevation Puna: Geographic segregation and no evidence of positive effects on peatland productivity. Regional Environmental Change, 20, 112. https://doi.org/10.1007/s10113-020-01704-8
Borgnia, M., Vilá, B. L., & Cassini, M. H. (2008). Interaction between wild camelids and livestock in an Andean semi-desert. Journal of Arid Environments, 72, 2150-2158. https://doi.org/10.1016/j.jaridenv.2008.07.012
Navarro, C. J., Carilla, J., Osinaga Acosta, O., Nieto, C., Ovejero, R., & Grau, H. R. (2023). Herbivore rewilding does not promote biodiversity in Argentine Andean peatlands. Anthropocene, 42, 100382. https://doi.org/10.1016/j.ancene.2023.100382

#### Modo `hibrido-0.3` (DeepSeek, búsqueda hibrida, ~7380 tok, 4.3 s, DOI: 3/5)

¡Hola! Te cuento lo que dicen los estudios que tengo a mano. El pastoreo es clave para las vegas y bofedales, pero el tipo de ganado y la carga hacen gran diferencia: vacas, ovejas y cabras causan mayores impactos que los camélidos (Cochi Machaca et al., 2018). El pisoteo excesivo rompe los bordes de los cojines de *Distichia muscoides* y *Oxychloe andina*, que funcionan como diques que retienen pozas; eso conecta las pozas, reduce el agua superficial y desplaza a los cojines por otras especies, incluso invasoras indicadoras de sobrepastoreo (Cochi Machaca et al., 2018) (Oyague y Cooper, 2020).

En Nor Yauyos-Cochas (Perú), cargas crecientes redujeron *D. muscoides* (de 68 % a 41–47 %) y bajaron la conductividad hidráulica superficial de la turba (Oyague et al., 2022). Ojo: casi toda esta evidencia viene de Bolivia y Perú, así que aplicarla a la Puna argentina requiere cautela. En la Puna argentina lo que sí está documentado es que la emigración, la urbanización y el empleo en minería desestructuran la trashumancia y concentran el ganado cerca de los asentamientos (Izquierdo et al., 2018) (Casagranda et al., 2026).

Fuentes:
Cochi Machaca, N., Condori, B., Rojas Pardo, A., Anthelme, F., Meneses, R. I., Weeda, C. E., & Perotto-Baldivieso, H. L. (2018). Effects of grazing pressure on plant species composition and water presence on bofedales in the Andes mountain range of Bolivia. Mires and Peat, 21, Article 15, 1-15. https://doi.org/10.19189/MaP.2017.OMB.303
Oyague, E., & Cooper, D. J. (2020). Peatlands of the Central Andes Puna, South America. Wetland Science & Practice, 255-260.
Oyague, E., Cooper, D. J., & Ingol, E. (2022). Effects of land use on the hydrologic regime, vegetation, and hydraulic conductivity of peatlands in the central Peruvian Andes. Journal of Hydrology, 609, 127687. https://doi.org/10.1016/j.jhydrol.2022.127687
Izquierdo, A. E., Grau, H. R., Navarro, C. J., Casagranda, E., Castilla, M. C., & Grau, A. (2018). Highlands in transition: Urbanization, pastoralism, mining, tourism, and wildlife in the Argentinian Puna. Mountain Research and Development, 38(4), 390-400. https://doi.org/10.1659/MRD-JOURNAL-D-17-00075.1
Casagranda, E., Navarro, C. J., & Grau, H. R. (2026). High-altitude pastoralism in the Argentine Puna: mapping livestock settlements as spatial proxies for extensive livestock use [Preprint]. SSRN. https://ssrn.com/abstract=6149297

#### Modo `hibrido-0.5` (DeepSeek, búsqueda hibrida, ~7309 tok, 4.0 s, DOI: 4/5)

El pastoreo afecta de varias maneras, y no todas son negativas. Por un lado, el pisoteo excesivo rompe los bordes de los cojines de *Distichia muscoides* y *Oxychloe andina* que retienen las pozas, reduce el agua superficial y desplaza esos cojines por otras especies, incluso invasoras indicadoras de sobrepastoreo (Cochi Machaca et al., 2018) (Domic et al., 2021) (Oyague y Cooper, 2020). En Nor Yauyos-Cochas (Perú) las cargas altas redujeron *D. muscoides* del 68 % al 41–47 % y bajaron la conductividad hidráulica superficial de la turba (Oyague et al., 2022). El tipo de ganado importa: vacas, ovejas y cabras causan mayores impactos que los camélidos (Cochi Machaca et al., 2018) (Oyague et al., 2022).

Ahora, ojo con los diagnósticos simples: en el altiplano de Tarija (Bolivia, cerca de la Puna jujeña) los autores consideran engañoso el término sobrepastoreo y concluyen que, en la mayor parte del área, el pastoreo actual no afecta la vegetación más que en los últimos 500 a 1000 años, gracias a los movimientos estacionales que reparten la carga (Preston et al., 2003). Es decir, hay estudios que muestran degradación por carga excesiva y otros que relativizan el impacto cuando hay manejo estacional.

Fuentes:
Cochi Machaca, N., Condori, B., Rojas Pardo, A., Anthelme, F., Meneses, R. I., Weeda, C. E., & Perotto-Baldivieso, H. L. (2018). Effects of grazing pressure on plant species composition and water presence on bofedales in the Andes mountain range of Bolivia. Mires and Peat, 21, Article 15, 1-15. https://doi.org/10.19189/MaP.2017.OMB.303
Domic, A. I., Capriles, J. M., Meneses, R. I., & Pacheco, P. (2021). Plant community assembly is predicted by an environmental gradient in high-altitude wetlands in the semiarid western Bolivian Andes. Mires and Peat, 27, Article 01. https://doi.org/10.19189/MaP.2019.JSP.StA.1916
Oyague, E., & Cooper, D. J. (2020). Peatlands of the Central Andes Puna, South America. Wetland Science & Practice, 255-260.
Oyague, E., Cooper, D. J., & Ingol, E. (2022). Effects of land use on the hydrologic regime, vegetation, and hydraulic conductivity of peatlands in the central Peruvian Andes. Journal of Hydrology, 609, 127687. https://doi.org/10.1016/j.jhydrol.2022.127687
Preston, D., Fairbairn, J., Paniagua, N., Maas, G., Yevara, M., & Beck, S. (2003). Grazing and environmental change on the Tarija altiplano, Bolivia. Mountain Research and Development, 23(2), 141-148. https://doi.org/10.1659/0276-4741(2003)023[0141:GAECOT]2.0.CO;2

#### Modo `hibrido-0.7` (DeepSeek, búsqueda hibrida, ~7356 tok, 3.6 s, DOI: 2/2)

¡Buena pregunta, che! El pastoreo afecta de varias maneras y no todo es blanco o negro.

Por un lado, las vegas y bofedales son forraje clave, sobre todo en la estación seca y en sequías, cuando el ganado depende casi exclusivamente de ellos (Preston et al., 2003). Pero la carga suele exceder la oferta: en la Cordillera Real (Bolivia) los 21 bofedales evaluados estaban sobrepastoreados, con cocientes capacidad/carga de 0,02 a 0,94 (Cochi Machaca et al., 2018).

El impacto físico es concreto: los cojines de *Distichia muscoides* y *Oxychloe andina* funcionan como diques que retienen pozas, y el pisoteo excesivo rompe sus bordes, conecta las pozas y reduce el agua superficial, desplazando a los cojines por otras especies (Cochi Machaca et al., 2018). Además, el tipo de ganado importa: vacas, ovejas y cabras causan mayores impactos que los camélidos (Cochi Machaca et al., 2018).

Ojo, que hay matices: en el altiplano de Tarija (Bolivia) los autores consideran engañoso el término "sobrepastoreo" y sostienen que el pastoreo actual no afecta la vegetación más que en los últimos 500 a 1000 años, gracias a los movimientos estacionales que reparten la carga (Preston et al., 2003). Es decir, los estudios no siempre coinciden.

Fuentes:
Preston, D., Fairbairn, J., Paniagua, N., Maas, G., Yevara, M., & Beck, S. (2003). Grazing and environmental change on the Tarija altiplano, Bolivia. Mountain Research and Development, 23(2), 141-148. https://doi.org/10.1659/0276-4741(2003)023[0141:GAECOT]2.0.CO;2
Cochi Machaca, N., Condori, B., Rojas Pardo, A., Anthelme, F., Meneses, R. I., Weeda, C. E., & Perotto-Baldivieso, H. L. (2018). Effects of grazing pressure on plant species composition and water presence on bofedales in the Andes mountain range of Bolivia. Mires and Peat, 21, Article 15, 1-15. https://doi.org/10.19189/MaP.2017.OMB.303

---

### 5. Agua / Hidrología
**Pregunta:** ¿De dónde proviene el agua que mantiene a las vegas y bofedales?

#### Modo `completo` (DeepSeek, ~412046 tok, 8.2 s, DOI: 8/9)

¡Qué buena pregunta, che! Es clave para entender por qué estas vegas existen donde existen. Te cuento lo que muestran los estudios: en gran parte de la Puna, las vegas y bofedales se sostienen sobre todo por **descargas perennes de agua subterránea** que vienen de laderas, morrenas antiguas, depósitos coluviales y fallas tectónicas, más que por el deshielo glaciar directo (Cooper et al., 2010) (Ruthsatz, 2012) (Cooper et al., 2019) (Oyague y Cooper, 2020). Un caso bien documentado en Catamarca: el río Mojones pasa de efímero a permanente a los 4300 m gracias a cinco vertientes asociadas a fallas inversas cuaternarias que alimentan una vega orgánica de 15 km (Tchilinguirian et al., 2018).

En 10 turberas de Bolivia y Perú se confirmó que el agua llega desde acuíferos de ladera (morenas laterales, talud, coluvio o roca) y fluye hacia el arroyo, sin aporte del cauce ni del glaciar; los isótopos lo respaldan (Cooper et al., 2019). Eso no quita que la lluvia y la nieve recarguen esos acuíferos: en el Altiplano chileno la recarga efectiva es infrecuente, de 10–35 % de la lluvia y solo en años húmedos cada 20–30 años (de la Fuente et al., 2021).

Ojo, que hay matices según la escala: en cabeceras muy glaciarizadas el deshielo puede dominar el caudal seco (80–91 % frente a 9–20 % de los bofedales en una cuenca de Vilcanota) (Gribbin et al., 2024), mientras que a escala de cuenca el flujo subsuperficial no glaciar de bofedales y laderas aportó el 74 % del estiaje (Ross et al., 2023). Y en la Puna argentina, en Cerro Tuzgle los isótopos indican recarga por lluvia reciente y agua subterránea somera (Kock et al., 2019).

Fuentes:
Cooper, D. J., Wolf, E. C., Colson, C., Vering, W., Granda, A., & Meyer, M. (2010). Alpine peatlands of the Andes, Cajamarca, Peru. Arctic, Antarctic, and Alpine Research, 42(1), 19-33. https://doi.org/10.1657/1938-4246-42.1.19
Ruthsatz, B. (2012). Vegetación y ecología de los bofedales altoandinos de Bolivia (C. Pérez, Trad.). Phytocoenologia, 42(3-4), 133-179. https://doi.org/10.1127/0340-269X/2012/0042-0535
Cooper, D. J., Sueltenfuss, J., Oyague, E., Yager, K., Slayback, D., Cabero Caballero, E. M., Argollo, J., & Mark, B. G. (2019). Drivers of peatland water table dynamics in the central Andes, Bolivia and Peru. Hydrological Processes, 33, 1913-1925. https://doi.org/10.1002/hyp.13446
Oyague, E., & Cooper, D. J. (2020). Peatlands of the Central Andes Puna, South America. Wetland Science & Practice, 255-260.
Tchilinguirian, P., Grana, L., & Olivera, D. (2018). Contexto paleoambiental para la ocupación arqueológica en Corral Grande (Antofagasta de la Sierra, Catamarca, Argentina). Chungara Revista de Antropología Chilena, 50(4), 605-621. https://doi.org/10.4067/S0717-73562018005001502
de la Fuente, A., Meruane, C., & Suárez, F. (2021). Long-term spatiotemporal variability in high Andean wetlands in northern Chile. Science of the Total Environment, 756, 143830. https://doi.org/10.1016/j.scitotenv.2020.143830
Gribbin, T., Mackay, J. D., MacDonald, A., Hannah, D. M., Buytaert, W., Baiker, J. R., Montoya, N., Perry, L. B., Seimon, A., Rado, M., Arias, S., & Vargas, M. (2024). Bofedal wetland and glacial melt contributions to dry season streamflow in a high-Andean headwater watershed. Hydrological Processes, 38(8), e15237. https://doi.org/10.1002/hyp.15237
Ross, A. C., Mendoza, M. M., Drenkhan, F., Montoya, N., Baiker, J. R., Mackay, J. D., Hannah, D. M., & Buytaert, W. (2023). Seasonal water storage and release dynamics of bofedal wetlands in the Central Andes. Hydrological Processes, 37(8), e14940. https://doi.org/10.1002/hyp.14940
Kock, S. T., Schittek, K., Wissel, H., Vos, H., Ohlendorf, C., Schäbitz, F., Lupo, L. C., Kulemeyer, J. J., & Lücke, A. (2019). Stable oxygen isotope records (δ18O) of a high-Andean cushion peatland in NW Argentina (24°S) imply South American Summer Monsoon related moisture changes during the Late Holocene. Frontiers in Earth Science, 7, 45. https://doi.org/10.3389/feart.2019.00045

#### Modo `rag` (DeepSeek, búsqueda bm25, ~7387 tok, 4.7 s, DOI: 7/8)

¡Buena pregunta, che! La respuesta corta es: sobre todo de agua subterránea, aunque hay matices y algún debate.

En los Andes centrales, varios estudios muestran que el agua subterránea no glaciar domina el sostenimiento de los bofedales (Cooper et al., 2019) (Oyague y Cooper, 2020) (Ross et al., 2023). Pero no todos coinciden: algunos trabajos vinculan la expansión de humedales al retroceso glaciar (Polk et al., 2017), y en cabeceras muy glaciarizadas el caudal seco sigue dominado en 80–91 % por hielo glaciar frente a 9–20 % de bofedales (Gribbin et al., 2024). Ojo: esa evidencia viene de Perú y Bolivia, no de la Puna argentina.

Para nuestras vegas, lo que sí está documentado es que son más estables que las lagunas por su sostén subterráneo, incluidas vertientes controladas por fallas inversas y cuencas altas confinadas (Tchilinguirian et al., 2018) (Grana et al., 2016). Y hay un vacío importante: faltan balances hídricos instrumentados, redes de piezómetros y estimaciones de edad del agua en vegas de la Puna argentina (Souza et al., 2025).

Fuentes:
Cooper, D. J., Sueltenfuss, J., Oyague, E., Yager, K., Slayback, D., Cabero Caballero, E. M., Argollo, J., & Mark, B. G. (2019). Drivers of peatland water table dynamics in the central Andes, Bolivia and Peru. Hydrological Processes, 33, 1913-1925. https://doi.org/10.1002/hyp.13446
Oyague, E., & Cooper, D. J. (2020). Peatlands of the Central Andes Puna, South America. Wetland Science & Practice, 255-260.
Ross, A. C., Mendoza, M. M., Drenkhan, F., Montoya, N., Baiker, J. R., Mackay, J. D., Hannah, D. M., & Buytaert, W. (2023). Seasonal water storage and release dynamics of bofedal wetlands in the Central Andes. Hydrological Processes, 37(8), e14940. https://doi.org/10.1002/hyp.14940
Polk, M. H., Young, K. R., Baraer, M., Mark, B. G., McKenzie, J. M., Bury, J., & Carey, M. (2017). Exploring hydrologic connections between tropical mountain wetlands and glacier recession in Peru's Cordillera Blanca. Applied Geography, 78, 94-103. https://doi.org/10.1016/j.apgeog.2016.11.004
Gribbin, T., Mackay, J. D., MacDonald, A., Hannah, D. M., Buytaert, W., Baiker, J. R., Montoya, N., Perry, L. B., Seimon, A., Rado, M., Arias, S., & Vargas, M. (2024). Bofedal wetland and glacial melt contributions to dry season streamflow in a high-Andean headwater watershed. Hydrological Processes, 38(8), e15237. https://doi.org/10.1002/hyp.15237
Tchilinguirian, P., Grana, L., & Olivera, D. (2018). Contexto paleoambiental para la ocupación arqueológica en Corral Grande (Antofagasta de la Sierra, Catamarca, Argentina). Chungara Revista de Antropología Chilena, 50(4), 605-621. https://doi.org/10.4067/S0717-73562018005001502
Grana, L., Tchilinguirian, P., Hocsman, S., Escola, P., & Maidana, N. I. (2016). Paleohydrological changes in highland desert rivers and human occupation, 7000-3000 cal. yr B.P., south-central Andes, Argentina. Geoarchaeology: An International Journal, 31(5), 412-433. https://doi.org/10.1002/gea.21559
Souza, R. G., Domingues, A. M., Spindlegger, A., Mair-Bauernfeind, C., & Part, F. (2025). Review of the current knowledge and identified gaps in assessing the social and environmental impacts of mining processes in the Lithium Triangle. Sustainable Production and Consumption, 53, 40-63. https://doi.org/10.1016/j.spc.2024.11.031

#### Modo `hibrido-0.3` (DeepSeek, búsqueda hibrida, ~7209 tok, 3.9 s, DOI: 3/4)

¡Qué buena pregunta! Y te cuento que hay bastante consenso en los estudios: el agua que sostiene estos humedales viene sobre todo de **flujo subterráneo lateral desde las laderas**, recargado por lluvia y nieve, y no del arroyo ni del deshielo glaciar. En 10 turberas de Bolivia y Perú monitoreadas con pozos, isótopos y sensores, el agua llegaba siempre desde acuíferos de ladera (morenas, taludes, coluvio o roca) y fluía hacia el arroyo, nunca al revés (Cooper et al., 2019). En la puna húmeda de Cusco, los bofedales se saturan con apenas ~197 mm de lluvia acumulada, mucho menos de lo que haría falta para recargar directamente un metro de turba, lo que confirma ese aporte lateral subterráneo (Wunderlich et al., 2023).

Ojo que estos datos son de Perú y Bolivia; para la Puna argentina conviene tomarlos como referencia hasta tener mediciones locales. Y hay otra mirada complementaria: desde la ecología del manejo se plantea que muchos bofedales además se forman y se mantienen con el riego pastoril (canales, champas, diques), así que el agua también llega por obra humana (Yager et al., 2021; Gonnet et al., 2016).

Fuentes:
Cooper, D. J., Sueltenfuss, J., Oyague, E., Yager, K., Slayback, D., Cabero Caballero, E. M., Argollo, J., & Mark, B. G. (2019). Drivers of peatland water table dynamics in the central Andes, Bolivia and Peru. Hydrological Processes, 33, 1913-1925. https://doi.org/10.1002/hyp.13446
Wunderlich, W., Lang, M., Keating, K., Bandera Perez, W., & Oshun, J. (2023). The role of peat-forming bofedales in sustaining baseflow in the humid puna. Journal of Hydrology: Regional Studies, 47, 101394. https://doi.org/10.1016/j.ejrh.2023.101394
Yager, K., Prieto, M., & Meneses, R. I. (2021). Reframing pastoral practices of bofedal management to increase the resilience of Andean water towers. Mountain Research and Development, 41(4), A1-A9. https://doi.org/10.1659/MRD-JOURNAL-D-21-00011.1
Gonnet, J. M., Lopez, C., Aranibar, D. E., & Lictevout, E. (2016). Manual introductorio al manejo de vegas y bofedales mediante prácticas tradicionales de culturas andinas en el norte de Chile. Corporación Norte Grande.

#### Modo `hibrido-0.5` (DeepSeek, búsqueda hibrida, ~7372 tok, 3.2 s, DOI: 2/2)

¡Qué linda pregunta, che! Lo primero para tener claro es que el agua que sostiene estos humedales viene sobre todo de **flujo subterráneo lateral desde las laderas**, recargado por lluvia y nieve, y no del arroyo ni del deshielo glaciar. En 10 turberas de Bolivia y Perú se vio que la napa se alimenta de acuíferos de ladera (morenas laterales, talud, coluvio o roca) y fluye siempre hacia el arroyo, nunca al revés (Cooper et al., 2019). Por eso en temporada de lluvias la napa queda a menos de 20 cm de la superficie y en la seca baja a 40-90 cm (Cooper et al., 2019).

En la puna húmeda del Cusco (Perú) también confirmaron que el agua llega principalmente por flujo subterráneo lateral desde las laderas: los bofedales se saturan con apenas ~197 mm de lluvia acumulada, mucho menos de lo que haría falta para recargar directamente un metro de turba (Wunderlich et al., 2023). Ojo que estos datos son de Bolivia y Perú; para la Puna argentina no tengo estudios de este tipo en los fragmentos que manejo.

Fuentes:
Cooper, D. J., Sueltenfuss, J., Oyague, E., Yager, K., Slayback, D., Cabero Caballero, E. M., Argollo, J., & Mark, B. G. (2019). Drivers of peatland water table dynamics in the central Andes, Bolivia and Peru. Hydrological Processes, 33, 1913-1925. https://doi.org/10.1002/hyp.13446
Wunderlich, W., Lang, M., Keating, K., Bandera Perez, W., & Oshun, J. (2023). The role of peat-forming bofedales in sustaining baseflow in the humid puna. Journal of Hydrology: Regional Studies, 47, 101394. https://doi.org/10.1016/j.ejrh.2023.101394

#### Modo `hibrido-0.7` (DeepSeek, búsqueda hibrida, ~7323 tok, 3.3 s, DOI: 2/2)

¡Buena pregunta! Es una de las más importantes para entender estos humedales.

En los estudios que conozco, el agua que sostiene a los bofedales viene principalmente de **agua subterránea de ladera**: se recarga con lluvia y nieve en las laderas (morenas, taludes, coluvio, roca) y fluye hacia el arroyo, no desde el cauce ni del deshielo glaciar. En las 10 turberas monitoreadas en Bolivia y Perú, la napa se mantuvo a menos de 20 cm de la superficie en época de lluvias y bajó a 40–90 cm en la seca, y los isótopos confirmaron ese origen subterráneo (Cooper et al., 2019). En la puna húmeda de Cusco (Perú) también se vio que los bofedales se saturan con lluvias acumuladas relativamente modestas, lo que confirma el aporte lateral subterráneo desde las laderas (Wunderlich et al., 2023).

Ojo: hay un debate abierto sobre el rol del deshielo glaciar, y varios de esos trabajos son de Perú y Bolivia, no de la Puna argentina.

Fuentes:
Cooper, D. J., Sueltenfuss, J., Oyague, E., Yager, K., Slayback, D., Cabero Caballero, E. M., Argollo, J., & Mark, B. G. (2019). Drivers of peatland water table dynamics in the central Andes, Bolivia and Peru. Hydrological Processes, 33, 1913-1925. https://doi.org/10.1002/hyp.13446
Wunderlich, W., Lang, M., Keating, K., Bandera Perez, W., & Oshun, J. (2023). The role of peat-forming bofedales in sustaining baseflow in the humid puna. Journal of Hydrology: Regional Studies, 47, 101394. https://doi.org/10.1016/j.ejrh.2023.101394

---

### 6. Carbono
**Pregunta:** ¿Cuánto carbono orgánico acumulan los suelos de turberas y bofedales andinos?

#### Modo `completo` (DeepSeek, ~412049 tok, 8.2 s, DOI: 5/7)

¡Qué linda pregunta! Te cuento lo que dicen los estudios que conozco, y vas a ver que las cifras cambian bastante según cuánta profundidad se mida y en qué lugar.

En los primeros 30 cm, los bofedales de Puno (Perú) guardaron entre 23 y 30 kg C/m² según el régimen de inundación (Segnini et al., 2010), y en Junín promediaron 210,9 t C/ha, casi el doble que los pastizales vecinos (Carbajal et al., 2024). En la Puna argentina, diez vegas promediaron 66,11 Mg C/ha en 0–30 cm, con un rango de 21,79 a 139,67 (Chiappero et al., 2026).

Cuando se mide toda la columna de turba, los números se disparan: 1040 y 572 Mg C/ha en dos bofedales bolivianos (Hribljan et al., 2015), y en Huascarán las turberas llegan a 1092–2101 Mg C/ha frente a unos 30 Mg C/ha en vegas de suelo mineral (Chimner et al., 2020; Young et al., 2023). Ojo que una revisión andina encontró que solo 14 de 334 muestras de suelo provenían de turberas, así que el sur andino sigue subrepresentado (Alavi-Murillo et al., 2022).

Fuentes:
Segnini, A., Posadas, A., Quiroz, R., Milori, D. M. B. P., Saab, S. C., Martin Neto, L., & Vaz, C. M. P. (2010). Spectroscopic assessment of soil organic matter in wetlands from the High Andes. Soil Science Society of America Journal, 74(6), 2246-2253. https://doi.org/10.2136/sssaj2009.0445
Carbajal, M., Ramírez, D. A., Turin, C., Schaeffer, S. M., Konkel, J., Ninanya, J., Rinza, J., De Mendiburu, F., Zorogastua, P., Villaorduña, L., & Quiroz, R. (2024). From rangelands to cropland, land-use change and its impact on soil organic carbon variables in a Peruvian Andean highlands: A machine learning modeling approach. Ecosystems, 27, 899-917. https://doi.org/10.1007/s10021-024-00928-7
Chiappero, M. F., Vaieretti, M. V., Gallardo, N., & Izquierdo, A. E. (2026). Carbon storage patterns in high Andean wetlands: local factors explain the variability of soil carbon stocks in the Argentine Puna. Plant and Soil, 525, 1393–1408. https://doi.org/10.1007/s11104-026-08829-5
Hribljan, J. A., Cooper, D. J., Sueltenfuss, J., Wolf, E. C., Heckman, K. A., Lilleskov, E. A., & Chimner, R. A. (2015). Carbon storage and long-term rate of accumulation in high-altitude Andean peatlands of Bolivia. Mires and Peat, 15(12), 1–14.
Chimner, R. A., Boone, R., Bowser, G., Bourgeau-Chavez, L., Fuentealba, B., Gilbert, J., Ñaupari, J. A., Polk, M. H., Resh, S., Turin, C., Young, K. R., & Zarria-Samanamud, M. (2020). Andes, Bofedales, and the Communities of Huascarán National Park, Peru. Wetland Science & Practice, October 2020, 246-254.
Young, K. R., Alata, E., Chimner, R. A., Boone, R. B., Bowser, G., Bourgeau-Chavez, L., Fuentealba, B., Gilbert, J., Ñaupari, J. A., Polk, M. H., Resh, S. C., Turin, C., & Zarria-Samanamud, M. (2023). Ecological change and livestock governance in a Peruvian national park. Land, 12(11), 2051. https://doi.org/10.3390/land12112051
Alavi-Murillo, G., Diels, J., Gilles, J., & Willems, P. (2022). Soil organic carbon in Andean high-mountain ecosystems: Importance, challenges, and opportunities for carbon sequestration. Regional Environmental Change, 22, 128. https://doi.org/10.1007/s10113-022-01980-6

#### Modo `rag` (GLM (Z.AI), búsqueda bm25, ~7348 tok, 20.3 s, DOI: 2/2)

¡Qué buena pregunta, compañero! Como bien sabés, en la Puna el suelo es casi como una mochila gigante que guarda el carbono. Los estudios que conozco muestran que estos ecosistemas son los que más carbono guardan en los Andes, aunque los datos del sur andino (incluida la Argentina) son escasos.

Las turberas y bofedales de Bolivia alcanzan las concentraciones más altas, con valores cercanos a los 500 g/kg en la superficie (Alavi-Murillo et al., 2022). En promedio, los bofedales tienen un stock de carbono orgánico de 12,3 a 13,6 kg/m² en los primeros 30 cm de profundidad (Alavi-Murillo et al., 2022). Por otro lado, en Perú se registraron valores de carbono orgánico del suelo de 11,2% en bofedales y un stock de 210,9 t/ha en 0-30 cm (Carbajal et al., 2024).

Fuentes:
Alavi-Murillo, G., Diels, J., Gilles, J., & Willems, P. (2022). Soil organic carbon in Andean high-mountain ecosystems: Importance, challenges, and opportunities for carbon sequestration. Regional Environmental Change, 22, 128. https://doi.org/10.1007/s10113-022-01980-6
Carbajal, M., Ramírez, D. A., Turin, C., Schaeffer, S. M., Konkel, J., Ninanya, J., Rinza, J., De Mendiburu, F., Zorogastua, P., Villaorduña, L., & Quiroz, R. (2024). From rangelands to cropland, land-use change and its impact on soil organic carbon variables in a Peruvian Andean highlands: A machine learning modeling approach. Ecosystems, 27, 899-917. https://doi.org/10.1007/s10021-024-00928-7

#### Modo `hibrido-0.3` (GLM (Z.AI), búsqueda hibrida, ~7382 tok, 21.6 s, DOI: 4/9)

¡Hola! Qué buena pregunta, porque acá en la Puna, donde el aire es fino y el sol pega fuerte, esos suelos son como esponjas gigantes que guardan el carbono. En los bofedales y turberas andinos, el carbono orgánico del suelo (COS) es el que más acumula de toda la región, superando a los pastizales de puna o a los bosques de Polylepis.

Según los datos que tenemos, las turberas y bofedales andinos acumulan carbono a tasas muy altas. Por ejemplo, en el Altiplano chileno, las turberas acumulan entre 70 y 292 gramos de carbono por metro cuadrado por año (Earle et al., 2003). En Bolivia, los cojines de *Distichia muscoides* pueden producir hasta más de 4 kilogramos de carbono por metro cuadrado por año (Cooper et al., 2015). Y en Ecuador, las turberas de páramo acumulan entre 26 y 46 gramos de carbono por metro cuadrado por año (Hribljan et al., 2016).

En cuanto a las reservas totales que guardan en el suelo, varían mucho según dónde estés y cómo sea el sitio. En el Parque Nacional Huascarán (Perú), las turberas pueden almacenar entre 1092 y 2101 megagramos de carbono por hectárea (Chimner et al., 2020). En Bolivia, dos bofedales (Tuni y Manasaya) guardan alrededor de 572 y 1040 Mg C ha-1, respectivamente (Hribljan et al., 2015). En Ecuador, las turberas de páramo promedian 1282 Mg C ha-1 (Hribljan et2016). Incluso en los primeros 30 cm, diez vegas de la Puna argentina controladas por variables locales promediaron 66,11 Mg C/ha (Chiappero et al., 2026).

Fuentes:
Earle, L. R., Warner, B. G., & Aravena, R. (2003). Rapid development of an unusual peat-accumulating ecosystem in the Chilean Altiplano. Quaternary Research, 59, 2-11.
Cooper, D. J., Kaczynski, K., Slayback, D., & Yager, "K. (2015). Growth and organic carbon production in peatlands dominated by Do
Chimner, R. A., Boone, R., Bowser, G., Bourgeau-Chavez, L., Fuentealba, B., Gilbert, J., Ñaupari, J. A., Polk, M. H., Resh, S., Turin, C., Young, K. R., & Zarria-Samanamud, M. (2020). Andes, Bofedales, and the Communities of Huascarán National Park, Peru. Wetland Science & Practice, October 2020, 246-254.
Hribljan, J. A., Suárez, E., Heckman, K. A., Lilleskov, E. A., & Chimner, R. A. (2016). Peatland carbon stocks and accumulation rates in the Ecuadorian páramo. Wetlands Ecology and Management. https://doi.org/10.1007/s11273-016-9482-2
Hribljan, [REDACTED] et al., 2015. Carbon storage and long-term accumulation rates in high-altitude Andean peatlands of Bolivia. Mires and Peat, 15(12), 1–14. https://doi.org/10.19189/MaP.2015.OMB.016
Chiappero, M. F., Vaieretti, M. V., Gallardo, N., & Izquierdo, A. E. (2026). Carbon storage patterns in high Andean wetlands: local factors explain the variability of soil carbon stocks in the Argentine Puna. Plant and Soil, 525, 1393–1408. https://doi.org/10.1007/s11104-026-08829-5
(Nota: La cita de Cooper et al. 2015 en el texto final se cortó en el prompt anterior, aquí está completa).*
Cooper, D. J., Kaczynski, K., Slayback, D., & Yager, K. (2015). Growth and organic carbon production in peatlands dominated by Distichia muscoides, Bolivia, South America. Arctic, Antarctic, and Alpine Research, 47(3), 505-510. https://doi.org/10.1657/AAAR0014-060
Hribljan, J. A., Cooper, D. J., Sueltenfuss, J., Wolf, E. C., Heckman, K. A., Lilleskov, E. A., & Chimner, R. A. (2015). Carbon storage and long-term rate of accumulation in high-altitude Andean peatlands of Bolivia. Mires and Peat, 15(12), 1–14.

#### Modo `hibrido-0.5` (GLM (Z.AI), búsqueda hibrida, ~7308 tok, 22.1 s, DOI: 6/9)

¡Hola! Qué buena pregunta, porque acá en la Puna los bofedales son como nuestros "jardines de invierno", llenos de vida y humedad. La verdad es que esos suelos son como esponjas gigantes que guardan mucho carbono, mucho más de lo que imaginás.

Según los estudios que conozco, los bofedales y turberas son los ecosistemas con más carbono orgánico en los Andes. En Bolivia, por ejemplo, algunos bofedales acumulan hasta **1040 Mg C ha⁻¹** (toneladas métricas de carbono por hectárea) en toda la columna de turba (Hribljan et al., 2015). En el Parque Nacional Huascarán (Perú), donde casi todo son turberas, el carbono acumulado llega a **1092 a 2101 Mg C ha⁻¹**, concentrando el 97% del carbono de todos los humedales de ese parque (Chimner et al., 2020; Young et al., 2023).

Si miramos solo la primera capa de suelo (los primeros 30 cm), los valores son más bajos pero igual impresionantes. En Puno (Perú), los bofedales estacionales tienen un stock de **30,62 kg C m⁻²**, mientras que los anegados todo el año guardan **23,03 kg C m⁻²** (Segnini et al., 2010). En Junín (Perú), los bofedales promediaron **210,9 t ha⁻¹** en 0–30 cm, casi el doble que los pastizales vecinos (Carbajal et al., 2024).

Las concentraciones de carbono orgánico en el suelo también varían mucho según el país. Las turberas de Bolivia alcanzan las máximas concentraciones, cercanas a **500 g/kg** (Alavi-Murillo et al., 2022), mientras que las de Ecuador muestran las más bajas, alrededor de **132 g/kg** (Alavi-Murillo et al., 2022). En la Puna argentina, los estudios recientes muestran que estos suelos son sumideros importantes de carbono, aunque faltan más datos para tener una imagen completa (Chiappero et al., 2026; Chiappero et al., 2021).

Fuentes:
Alavi-Murillo, G., Diels, J., Gilles, J., & Willems, P. (2022). Soil organic carbon in Andean high-mountain ecosystems: Importance, challenges, and opportunities for carbon sequestration. Regional Environmental Change, 22, 128. https://doi.org/10.1007/s10113-022-01980-6
Carbajal, M., Ramírez, D. A., Turin, C., Schaeffer, S. M., Konkel, J., Ninanya, J., Rinza, J., De Mendiburu, F., Zorogastua, P., Villaorduña, L., & Quiroz, R. (2024). From rangelands to cropland, land-use change and its impact on soil organic carbon variables in a Peruvian Andean highlands: A machine learning modeling approach. Ecosystems, 27, 899-917. https://doi.org/10.1007/s10021-024-00928-7
Chiappero, M. F., Vaieretti, M. V., Gallardo, N., & Izquierdo, A. E. (2026). Carbon storage patterns in high Andean wetlands: local factors explain the variability of soil carbon stocks in the Argentine Puna. Plant and Soil, 525, 1393–1408. https://doi.org/10.1007/s11104-026-08829-5
Chiappero, M. F., Vaieretti, M. V., & Izquierdo, A. E. (2021). A baseline soil survey of two peatlands associated with a lithium-rich salt flat in the Argentine Puna: physico-chemical characteristics, carbon storage and biota. Mires and Peat, 27, Article 16, 1–13. https://doi.org/10.19189/MaP.2020.OMB.StA.2126
Chimner, R. A., Boone, R., Bowser, G., Bourgeau-Chavez, L., Fuentealba, B., Gilbert, J., Ñaupari, J. A., Polk, M. H., Resh, S., Turin, C., Young, K. R., & Zarria-Samanamud, M. (2020). Andes, Bofedales, and the Communities of Huascarán National Park, Peru. Wetland Science & Practice, October 2020, 246-254.
Hribljan, J. A., Cooper, D. J., Sueltenfuss, J., Wolf, E. C., Heckman, K. A., Lilleskov, E. A., & Chimner, R. A. (2015). Carbon storage and long-term rate of accumulation in high-altitude Andean peatlands of Bolivia. Mires and Peat, 15(12), 1–14.
Segnini, A., Souza, A. A., Novotny, E. H., Milori, D. M. B. P., da Silva, W. T. L., Bonagamba, T. J., Posadas, A., & Quiroz, R. (2013). Characterization of peatland soils from the High Andes through 13C nuclear magnetic resonance spectroscopy. Soil Science Society of America Journal, 77, 673-679. https://doi.org/10.2136/sssaj2012.0291
Segnini, A., Posadas, A., Quiroz, R., Milori, D. M. B. P., Saab, S. C., Martin Neto, L., & Vaz, C. M. P. (2010). Spectroscopic assessment of soil organic matter in wetlands from the High Andes. Soil Science Society of America Journal, 74(6), 2246-2253. https://doi.org/10.2136/sssaj2009.0445
Young, K. R., Alata, E., Chimner, R. A., Boone, R. B., Bowser, G., Bourgeau-Chavez, L., Fuentealba, B., Gilbert, J., Ñaupari, J. A., Polk, M. H., Resh, S. C., Turin, C., & Zarria-Samanamud, M. (2023). Ecological change and livestock governance in a Peruvian national park. Land

#### Modo `hibrido-0.7` (GLM (Z.AI), búsqueda hibrida, ~7363 tok, 14.3 s, DOI: 3/4)

¡Hola! Qué buena pregunta, porque acá en la Puna, donde el aire es fino y el viento pita, los bofedales son como nuestros "bares" de agua y comida. Lo que guarda el suelo bajo esos cojines de pasto es increíble, pero también muy variable según dónde estés.

Según los estudios que conozco, los bofedales y turberas son los lugares con más carbono orgánico de los Andes, pero los datos de la Puna argentina son escasos. En general, las turberas de Bolivia acumulan mucho más que las de Ecuador, y los bofedales de Puno (Perú) tienen valores intermedios.

Aquí te cuento los números clave:

*   **En Bolivia (los campeones):** Las turberas de *Distichia muscoides* pueden guardar hasta **500 g de carbono por kilo de suelo** en la superficie, lo que es mucho. Si miramos toda la columna de turba, un bofedal de la puna seca (Manasaya) acumuló **1040 Mg C por hectárea**, y uno húmedo (Tuni) acumuló **572 Mg C por hectárea** (Hribljan et al., 2015).
*   **En Ecuador (los más bajos):** Las turberas de ahí tienen concentraciones más bajas, alrededor de **132 g de carbono por kilo de suelo** (Alavi-Murillo et al., 2022).
*   **En Perú (bofedales):** En Puno, los bofedales estacionales tienen entre **121,7 y 215,6 g de carbono por kilo de suelo**, y en Junín, los bofedales acumularon casi el doble de carbono que los pastizales vecinos (Chiappero et al., 2026; Carbajal et al., 2024).

En resumen, esos cojones verdes que ves en el mapa son verdaderos tanques de carbono, mucho más que los pastizales de altura.

Fuentes:
Hribljan, J. A., Cooper, D. J., Sueltenfuss, J., Wolf, E. C., Heckman, K. A., Lilleskov, E. A., & Chimner, R. A. (2015). Carbon storage and long-term rate of accumulation in high-altitude Andean peatlands of Bolivia. Mires and Peat, 15(12), 1–14.
Alavi-Murillo, G., Diels, J., Gilles, J., & Willems, P. (2022). Soil organic carbon in Andean high-mountain ecosystems: Importance, challenges, and opportunities for carbon sequestration. Regional Environmental Change, 22, 128. https://doi.org/10.1007/s10113-022-01980-6
Chiappero, M. F., Vaieretti, M. V., Gallardo, N., & Izquierdo, A. E. (2026). Carbon storage patterns in high Andean wetlands: local factors explain the variability of soil carbon stocks in the Argentine Puna. Plant and Soil, 525, 1393–1408. https://doi.org/10.1007/s11104-026-08829-5
Carbajal, M., Ramírez, D. A., Turin, C., Schaeffer, S. M., Konkel, J., Ninanya, J., Rinza, J., De Mendiburu, F., Zorogastua, P., Villaorduña, L., & Quiroz, R. (2024). From rangelands to cropland, land-use change and its impact on soil organic carbon variables in a Peruvian Andean highlands: A machine learning modeling approach. Ecosystems, 27, 899-917. https://doi.org/10.1007/s10021-024-00928-7

---

### 7. Minería / Litio
**Pregunta:** ¿Qué impactos tiene la minería de litio y la extracción de agua sobre las vegas y bofedales?

#### Modo `completo` (DeepSeek, ~412053 tok, 19.3 s, DOI: 5/7)

¡Buena pregunta, che! Es un tema central para las vegas de la Puna. Te resumo lo que dicen los estudios, con la aclaración de que mucha evidencia viene de Chile y Perú, aunque ya hay casos documentados en Argentina.

- **Consumo de agua y desecación directa:** la extracción evaporítica de litio consume entre 500.000 y 1.000.000 L de salmuera más 80.000–140.000 L de agua dulce por tonelada de carbonato de litio (Marconi et al., 2022), y otras estimaciones hablan de ~2 millones de litros por tonelada (Izquierdo et al., 2015). En Catamarca, el desvío del río Trapiche para el proyecto Fénix secó permanentemente 32 ha de la Vega Trapiche, con pérdida total de vegetación (Marconi et al., 2022).

- **Descenso de la napa y pérdida de cojines:** en la Vega Tocorpuri (Chile, 5200 m), la desecación minera redujo la humedad del suelo de 92 % a 47 %, el carbono de 14,59 % a 1,89 % y las bacterias cultivables en dos órdenes de magnitud, eliminando cianobacterias y diatomeas (Belfiore et al., 2018). En Tambo-Puquíos (Chile) se registraron cotas piezométricas abatidas de −2,5 a −3,8 m atribuidas al bombeo minero (Cepeda-Pizarro, 2013).

- **Agua relíctica y recarga lenta:** en el Salar de Atacama, más del 93 % del flujo entrante es agua subterránea relíctica (>65 años), y la autoridad hídrica sobrestimó el rendimiento neto de la cuenca (18 % frente a 9 % real), sobreasignando derechos (Moran et al., 2022). En cuencas endorreicas del Altiplano chileno, la recarga efectiva ocurre solo cada 20–30 años (de la Fuente et al., 2021).

- **Vacíos en la evaluación ambiental:** en Catamarca, el 100 % de los 11 Informes de Impacto Ambiental de exploración revisados carecía de balance hídrico, y ninguno de 18 proyectos realizó consultas públicas conformes a ley (Marconi et al., 2022).

Ojo: hay un debate abierto. Moran et al. (2022) sostienen que los acuíferos de salmuera están desconectados de los humedales superficiales a escala humana y que el riesgo principal viene del agua dulce, mientras otros trabajos advierten que el bombeo de salmueras abate el nivel de base y afecta vegas y lagunas periféricas (Izquierdo et al., 2015; Souza et al., 2025).

Fuentes:
Belfiore, C., Fernandez, A., Santos, A. P., Contreras, M., & Farías, M. E. (2018). Characterization and comparison of microbial soil diversity in two Andean peatlands in different states of conservation-Vega Tocorpuri. Journal of Geoscience and Environment Protection, 6, 194-210. https://doi.org/10.4236/gep.2018.64012
Cepeda-Pizarro, J. (2013). Variabilidad temporal de algunos parámetros físicos e hidroquímicos de un prado húmedo alto-andino del norte-centro de Chile. IDESIA (Chile), 31(2), 89-97.
de la Fuente, A., Meruane, C., & Suárez, F. (2021). Long-term spatiotemporal variability in high Andean wetlands in northern Chile. Science of the Total Environment, 756, 143830. https://doi.org/10.1016/j.scitotenv.2020.143830
Izquierdo, A., Grau, H. R., Carilla, J., & Casagranda, E. (2015). Side effects of green technologies: the potential environmental costs of Lithium mining on high elevation Andean wetlands in the context of climate change. GLP News, 12, 53-56.
Marconi, P., Arengo, F., & Clark, A. (2022). The arid Andean plateau waterscapes and the lithium triangle: Flamingos as flagships for conservation of high-altitude wetlands under pressure from mining development. Wetlands Ecology and Management, 30, 827-852. https://doi.org/10.1007/s11273-022-09872-6
Moran, B. J., Boutt, D. F., McKnight, S. V., Jenckes, J., Munk, L. A., Corkran, D., & Kirshen, A. (2022). Relic groundwater and prolonged drought confound interpretations of water sustainability and lithium extraction in arid lands. Earth's Future, 10, e2021EF002555. https://doi.org/10.1029/2021EF002555
Souza, R. G., Domingues, A. M., Spindlegger, A., Mair-Bauernfeind, C., & Part, F. (2025). Review of the current knowledge and identified gaps in assessing the social and environmental impacts of mining processes in the Lithium Triangle. Sustainable Production and Consumption, 53, 40-63. https://doi.org/10.1016/j.spc.2024.11.031

#### Modo `rag` (DeepSeek, búsqueda bm25, ~7226 tok, 5.5 s, DOI: 4/4)

¡Hola! Buena pregunta, y bien de actualidad. Te cuento lo que dicen los estudios que tengo a mano.

En la Puna de Catamarca, el desvío y embalsado del río Trapiche para el proyecto Fénix (Salar del Hombre Muerto) provocó la desecación permanente de 32 ha de la Vega Trapiche, con pérdida total de su vegetación (Marconi et al., 2022). Además, en la subcuenca protegida del río Los Patos se aprobó a dos proyectos una extracción conjunta de 3.416.000 m³/año sin estudios detallados de balance hídrico ni evaluación de impactos acumulativos (Marconi et al., 2022). Los mismos autores señalan que el 100% de los 11 informes de impacto ambiental de exploración revisados en Catamarca carece de caracterización hidrogeológica y modelos de balance hídrico (Marconi et al., 2022).

Del otro lado de la cordillera, en Chile, el caso de la Laguna Santa Rosa (cuenca del Salar de Maricunga, contigua a la Puna catamarqueña por el Paso San Francisco) muestra cómo el bombeo minero desecó al menos 70 ha de humedales, con otras 73 ha en riesgo (Alam y Sepúlveda, 2022). Ojo con un detalle importante: ese trabajo advierte que los eventos extremos de precipitación pueden enmascarar temporalmente la retracción de humedales inducida por el bombeo, así que un año "bueno" no prueba que todo esté bien (Alam y Sepúlveda, 2022).

Sobre el marco general, la revisión de Souza et al. (2025) identifica la extracción de salmuera y agua dulce, la evaporación en piscinas y la reinyección como los flujos que más afectan la disponibilidad y calidad del agua, con efectos sobre la biodiversidad y las comunidades locales. Y hay una discusión interesante entre autores: mientras unos remarcan esos impactos sobre los humedales, Moran et al. (2022) sostienen —para el Salar de Atacama— que los acuíferos de salmuera están desconectados de los sistemas de agua superficial y humedales en escalas de tiempo humanas, y que por eso no pueden equipararse los impactos de la extracción de salmuera con los del agua dulce. Es un debate abierto, y conviene leerlo con las dos posturas en mente.

Fuentes:
Alam, M. A., & Sepúlveda, R. (2022). Environmental degradation through mining for energy resources: The case of the shrinking Laguna Santa Rosa wetland in the Atacama Region of Chile. Energy Geoscience, 3, 182-190. https://doi.org/10.1016/j.engeos.2021.11.006
Marconi, P., Arengo, F., & Clark, A. (2022). The arid Andean plateau waterscapes and the lithium triangle: Flamingos as flagships for conservation of high-altitude wetlands under pressure from mining development. Wetlands Ecology and Management, 30, 827-852. https://doi.org/10.1007/s11273-022-09872-6
Moran, B. J., Boutt, D. F., McKnight, S. V., Jenckes, J., Munk, L. A., Corkran, D., & Kirshen, A. (2022). Relic groundwater and prolonged drought confound interpretations of water sustainability and lithium extraction in arid lands. Earth's Future, 10, e2021EF002555. https://doi.org/10.1029/2021EF002555
Souza, R. G., Domingues, A. M., Spindlegger, A., Mair-Bauernfeind, C., & Part, F. (2025). Review of the current knowledge and identified gaps in assessing the social and environmental impacts of mining processes in the Lithium Triangle. Sustainable Production and Consumption, 53, 40-63. https://doi.org/10.1016/j.spc.2024.11.031

#### Modo `hibrido-0.3` (DeepSeek, búsqueda hibrida, ~7328 tok, 5.1 s, DOI: 3/5)

¡Buena pregunta, che! Es uno de los temas que más se estudia en la Puna. Te resumo lo que dicen los trabajos:

- La evaporación de salmueras consume muchísima agua: se estiman unos 2.000.000 L por tonelada de litio (Izquierdo et al., 2015), o entre 500.000 y 1.000.000 L de salmuera más 80.000–140.000 L de agua dulce por tonelada de carbonato de litio (Marconi et al., 2022). Eso abate el nivel freático y reduce el agua dulce disponible para lagunas y turberas periféricas (Izquierdo et al., 2015).
- Hay casos documentados en Argentina: en Catamarca, el desvío del río Trapiche secó permanentemente 32 ha de la Vega Trapiche, y los informes de impacto revisados carecían de balance hídrico (Marconi et al., 2022).
- A escala regional, unas 35.562 ha de humedales puneños argentinos (4,10 %) se asocian a presiones antrópicas, sobre todo minería (Izquierdo et al., 2018).
- Ojo que no todos coinciden: un trabajo en Atacama sostiene que los acuíferos de salmuera estarían desconectados de los humedales superficiales a escala humana (Moran et al., 2022), mientras que otros advierten que el bombeo sí afecta vegas y lagunas (Izquierdo et al., 2015; Souza et al., 2025). Y esto se da en un contexto de desecación de los últimos 30 años y proyecciones de +2 a 4 °C (Izquierdo et al., 2015).

Fuentes:
Izquierdo, A., Grau, H. R., Carilla, J., & Casagranda, E. (2015). Side effects of green technologies: the potential environmental costs of Lithium mining on high elevation Andean wetlands in the context of climate change. GLP News, 12, 53-56.
Marconi, P., Arengo, F., & Clark, A. (2022). The arid Andean plateau waterscapes and the lithium triangle: Flamingos as flagships for conservation of high-altitude wetlands under pressure from mining development. Wetlands Ecology and Management, 30, 827-852. https://doi.org/10.1007/s11273-022-09872-6
Izquierdo, A. E., Aragón, R., Navarro, C. J., & Casagranda, E. (2018). Humedales de la Puna: principales proveedores de servicios ecosistémicos de la región. En H. R. Grau, M. J. Babot, A. Izquierdo y A. Grau (Eds.), La Puna argentina: naturaleza y cultura (Serie Conservación de la Naturaleza, 24, pp. 96-111). Fundación Miguel Lillo.
Moran, B. J., Boutt, D. F., McKnight, S. V., Jenckes, J., Munk, L. A., Corkran, D., & Kirshen, A. (2022). Relic groundwater and prolonged drought confound interpretations of water sustainability and lithium extraction in arid lands. Earth's Future, 10, e2021EF002555. https://doi.org/10.1029/2021EF002555
Souza, R. G., Domingues, A. M., Spindlegger, A., Mair-Bauernfeind, C., & Part, F. (2025). Review of the current knowledge and identified gaps in assessing the social and environmental impacts of mining processes in the Lithium Triangle. Sustainable Production and Consumption, 53, 40-63. https://doi.org/10.1016/j.spc.2024.11.031

#### Modo `hibrido-0.5` (DeepSeek, búsqueda hibrida, ~7328 tok, 3.9 s, DOI: 2/4)

¡Buena pregunta! Te cuento lo que dicen los estudios de la Puna.

La minería de litio y la extracción de agua son de las amenazas más serias para las vegas. La evaporación de salmueras consume cerca de dos millones de litros de agua por cada tonelada de litio obtenida, lo que abate el nivel freático de la cuenca y reduce el agua dulce disponible para lagunas y turberas periféricas (Izquierdo et al., 2015). Ese proceso coincide con una tendencia de desecación registrada en los últimos 30 años y con escenarios futuros más cálidos y secos (Izquierdo et al., 2015).

En Catamarca, el desvío del río Trapiche (proyecto Fénix, Salar del Hombre Muerto) secó permanentemente 32 ha de la Vega Trapiche, y el 100 % de los 11 Informes de Impacto Ambiental de exploración revisados carece de balance hídrico (Marconi et al., 2022). A escala regional, unas 35.562 ha de humedales puneños argentinos (4,10 %) se asocian a presiones antrópicas, principalmente minería (20.785 ha) y turismo (10.639 ha) (Izquierdo et al., 2018).

Un dato importante: no todos coinciden. Un trabajo en Atacama sostiene que los acuíferos de salmuera estarían desconectados de los humedales superficiales a escala humana (Moran et al., 2022), mientras otros advierten que el bombeo abate el nivel de base y afecta vegas y lagunas periféricas (Izquierdo et al., 2015). Ojo que varios de estos casos son de Chile y Bolivia; aplicarlos a la Puna argentina requiere cuidado.

Fuentes:
Izquierdo, A., Grau, H. R., Carilla, J., & Casagranda, E. (2015). Side effects of green technologies: the potential environmental costs of Lithium mining on high elevation Andean wetlands in the context of climate change. GLP News, 12, 53-56.
Marconi, P., Arengo, F., & Clark, A. (2022). The arid Andean plateau waterscapes and the lithium triangle: Flamingos as flagships for conservation of high-altitude wetlands under pressure from mining development. Wetlands Ecology and Management, 30, 827-852. https://doi.org/10.1007/s11273-022-09872-6
Izquierdo, A. E., Aragón, R., Navarro, C. J., & Casagranda, E. (2018). Humedales de la Puna: principales proveedores de servicios ecosistémicos de la región. En H. R. Grau, M. J. Babot, A. Izquierdo y A. Grau (Eds.), La Puna argentina: naturaleza y cultura (Serie Conservación de la Naturaleza, 24, pp. 96-111). Fundación Miguel Lillo.
Moran, B. J., Boutt, D. F., McKnight, S. V., Jenckes, J., Munk, L. A., Corkran, D., & Kirshen, A. (2022). Relic groundwater and prolonged drought confound interpretations of water sustainability and lithium extraction in arid lands. Earth's Future, 10, e2021EF002555. https://doi.org/10.1029/2021EF002555

#### Modo `hibrido-0.7` (DeepSeek, búsqueda hibrida, ~7399 tok, 4.0 s, DOI: 4/5)

¡Hola! Buena pregunta, y delicada. Te cuento lo que dicen los estudios que conozco.

La minería de litio y el bombeo de agua pueden abatir las napas que sostienen vegas y bofedales: se estima que evaporar salmueras consume entre 500.000 y 1.000.000 L de salmuera más 80.000–140.000 L de agua dulce por tonelada de litio (Marconi et al., 2022), y otras estimaciones hablan de ~2.000.000 L por tonelada (Izquierdo et al., 2015). En Catamarca, el desvío del río Trapiche (proyecto Fénix, Salar del Hombre Muerto) secó permanentemente 32 ha de la Vega Trapiche, y los 11 Informes de Impacto Ambiental de exploración revisados carecían de balance hídrico (Marconi et al., 2022). También el entubado de cauces y los caminos que cortan el flujo afectan a los bofedales, como en la cuenca del San Pedro de Inacaliri en Chile (Yager et al., 2021).

Ojo, que no todos coinciden: un trabajo en Atacama sostiene que los acuíferos de salmuera están desconectados de los humedales superficiales a escala humana (Moran et al., 2022), mientras otros advierten que el bombeo abate el nivel de base y afecta vegas y lagunas periféricas (Izquierdo et al., 2015; Souza et al., 2025). Y hay un vacío importante: faltan balances hídricos de cuenca y estudios de ciclo de vida social específicos de sitio para el litio (Souza et al., 2025).

Fuentes:
Marconi, P., Arengo, F., & Clark, A. (2022). The arid Andean plateau waterscapes and the lithium triangle: Flamingos as flagships for conservation of high-altitude wetlands under pressure from mining development. Wetlands Ecology and Management, 30, 827-852. https://doi.org/10.1007/s11273-022-09872-6
Izquierdo, A., Grau, H. R., Carilla, J., & Casagranda, E. (2015). Side effects of green technologies: the potential environmental costs of Lithium mining on high elevation Andean wetlands in the context of climate change. GLP News, 12, 53-56.
Yager, K., Prieto, M., & Meneses, R. I. (2021). Reframing pastoral practices of bofedal management to increase the resilience of Andean water towers. Mountain Research and Development, 41(4), A1-A9. https://doi.org/10.1659/MRD-JOURNAL-D-21-00011.1
Moran, B. J., Boutt, D. F., McKnight, S. V., Jenckes, J., Munk, L. A., Corkran, D., & Kirshen, A. (2022). Relic groundwater and prolonged drought confound interpretations of water sustainability and lithium extraction in arid lands. Earth's Future, 10, e2021EF002555. https://doi.org/10.1029/2021EF002555
Souza, R. G., Domingues, A. M., Spindlegger, A., Mair-Bauernfeind, C., & Part, F. (2025). Review of the current knowledge and identified gaps in assessing the social and environmental impacts of mining processes in the Lithium Triangle. Sustainable Production and Consumption, 53, 40-63. https://doi.org/10.1016/j.spc.2024.11.031

---

### 8. Teledetección / Mapeo
**Pregunta:** ¿Qué sensores satelitales e índices se usan para mapear y monitorear vegas altoandinas?

#### Modo `completo` (DeepSeek, ~412052 tok, 8.8 s, DOI: 10/11)

¡Buena pregunta! Para mapear y monitorear vegas se usan sobre todo sensores ópticos y de radar, combinados con índices de vegetación y agua. Te resumo lo que muestran los estudios:

- **Landsat** es la base: con umbrales de NDVI de estación seca se delimitan los humedales, porque por encima de ~4200 m solo las vegas mantienen vegetación verde (Otto y Gibbons, 2017). En el Altiplano chileno, un NDVI de 0,23 con persistencia del 75 % delimitó 5665 bofedales (Chávez et al., 2019).
- **Sentinel-2** supera a Landsat-8 para discriminar grados de conservación (86,59 % frente a 77,90 % de exactitud), gracias a sus bandas Red Edge (Jara et al., 2019), y también sirve para estimar humedad del suelo usando el infrarrojo de onda corta (Araya-López et al., 2018).
- **Combinar óptico + radar + topografía** con Random Forests es lo más preciso para separar turberas de praderas húmedas: 90 % en Ecuador (Hribljan et al., 2017), 92 % en Huascarán (Chimner et al., 2019) y 97,1 % en la jalca peruana (Curatola Fernández et al., 2023).
- Índices de agua como el **NDII** ayudan a separar sectores inundados de temporales (Otto et al., 2011), y el NDWI y el GVMI captan los gradientes de humedad y salinidad entre tipos de vegas (Izquierdo et al., 2022).

Ojo con una advertencia: un mayor verdor satelital no siempre equivale a una vega más sana, porque puede reflejar gramíneas estacionales en lugar de cojines (Dangles et al., 2017). Y en la Puna argentina, los índices espectrales actuales no predicen el carbono del suelo de las vegas (Chiappero et al., 2026).

Fuentes:
Otto, M., & Gibbons, R. E. (2017). Potential effects of projected decrease in annual rainfall on spatial distribution of high Andean wetlands in southern Peru. Wetlands. https://doi.org/10.1007/s13157-017-0896-2
Chávez, R. O., Christie, D. A., Olea, M., & Anderson, T. G. (2019). A multiscale productivity assessment of high Andean peatlands across the Chilean Altiplano using 31 years of Landsat imagery. Remote Sensing, 11(24), 2955. https://doi.org/10.3390/rs11242955
Jara, C., Delegido, J., Ayala, J., Lozano, P., Armas, A., & Flores, V. (2019). Estudio de bofedales en los Andes ecuatorianos a través de la comparación de imágenes Landsat-8 y Sentinel-2. Revista de Teledetección, 53, 45-57. https://doi.org/10.4995/raet.2019.11715
Araya-López, R. A., Lopatin, J., Fassnacht, F. E., & Hernández, H. J. (2018). Monitoring Andean high altitude wetlands in central Chile with seasonal optical data: A comparison between Worldview-2 and Sentinel-2 imagery. ISPRS Journal of Photogrammetry and Remote Sensing. https://doi.org/10.1016/j.isprsjprs.2018.04.001
Hribljan, J. A., Suarez, E., Bourgeau-Chavez, L., Endres, S., Lilleskov, E. A., Chimbolema, S., Wayson, C., Serocki, E., & Chimner, R. A. (2017). Multidate, multisensor remote sensing reveals high density of carbon-rich mountain peatlands in the páramo of Ecuador. Global Change Biology, 23, 5412-5425. https://doi.org/10.1111/gcb.13807
Chimner, R. A., Bourgeau-Chavez, L., Grelik, S., Hribljan, J. A., Planas Clarke, A. M., Polk, M. H., Lilleskov, E. A., & Fuentealba, B. (2019). Mapping mountain peatlands and wet meadows using multi-date, multi-sensor remote sensing in the Cordillera Blanca, Peru. Wetlands. https://doi.org/10.1007/s13157-019-01134-1
Curatola Fernández, G. F., Makowski Giannoni, S., Delgado Florián, E., Rengifo, P., Rascón, J., Chichipe Vela, E., Butrich, C., Salas López, R., Oliva-Cruz, M., & Scheske, C. (2023). Mapping high-altitude peatlands to inform a landscape conservation strategy in the Andes of northern Peru. Environmental Conservation, 50, 212-219. https://doi.org/10.1017/S0376892923000267
Otto, M., Scherer, D., & Richters, J. (2011). Hydrological differentiation and spatial distribution of high altitude wetlands in a semi-arid Andean region derived from satellite data. Hydrology and Earth System Sciences, 15, 1713-1727. https://doi.org/10.5194/hess-15-1713-2011
Izquierdo, A. E., Blundo, C., Carilla, J., Foguet, J., Navarro, C. J., Casagranda, E., Chiappero, M. F., & Vaieretti, M. V. (2022). Floristic types of high-Andean wetlands from northwest Argentina and their remote-sensed characterization at a regional scale. Applied Vegetation Science, 25, e12658. https://doi.org/10.1111/avsc.12658
Dangles, O., Rabatel, A., Kraemer, M., Zeballos, G., Soruco, A., Jacobsen, D., & Anthelme, F. (2017). Ecosystem sentinels for climate change? Evidence of wetland cover changes over the last 30 years in the tropical Andes. PLoS ONE, 12(5), e0175814. https://doi.org/10.1371/journal.pone.0175814
Chiappero, M. F., Vaieretti, M. V., Gallardo

#### Modo `rag` (DeepSeek, búsqueda bm25, ~6940 tok, 6.5 s, DOI: 8/10)

¡Buena pregunta! Te resumo lo que muestran los estudios que tengo a mano.

Las series **Landsat** con índices de vegetación siguen siendo la base principal, cada vez más complementadas con **Sentinel-2, MODIS, radar, drones y aprendizaje automático** (Síntesis — Teledetección y mapeo). El **NDVI** es el índice estrella para delimitar vegas, aunque el umbral varía según el sitio: 0,23 en el Altiplano chileno (Chávez et al., 2019), 0,3 en Nuñoa, Perú (Mazzarino y Finn, 2016) y 0,468 en la Cordillera Real de Bolivia (Dangles et al., 2017). Combinar NDVI con el índice de agua **NDII** (umbral 0,45) permite separar sectores inundados y humedales perennes de los temporales, con hasta 99 % de fiabilidad en Perú (Otto et al., 2011; Garcia y Otto, 2015).

Para distinguir turberas de praderas húmedas, la clave fue combinar **óptico (Landsat) con radar en bandas L y C** e índices topográficos mediante **Random Forests**: 90 % en el páramo ecuatoriano (Hribljan et al., 2017), 92 % en Huascarán (Chimner et al., 2019) y 97,1 % en la jalca de Amazonas (Curatola Fernández et al., 2023). Ojo: el verdor no basta para detectar turba, porque cerca de un cuarto de los humedales con cojín en Huascarán no eran turberas (Chimner et al., 2019).

En cuanto a sensores, **Sentinel-2** viene mostrando ventajas: en la Reserva Chimborazo (Ecuador) alcanzó 86,59 % de exactitud frente a 77,90 % de Landsat-8 (Jara et al., 2019), y en Chile central delimitó vegas con 94 % de exactitud y estimó mejor la humedad del suelo que WorldView-2 (r² 0,58 frente a 0,34) gracias al infrarrojo de onda corta (Araya-López et al., 2018). **MODIS** (250 m), en cambio, capta solo unos dos tercios de los humedales detectados con Landsat y sobrestima los temporales (Otto et al., 2011), aunque sirvió para clasificar fisonomías regionales en Salta y Jujuy con 85 % de fiabilidad (Baldassini et al., 2012).

Fuentes:
Chávez, R. O., Christie, D. A., Olea, M., & Anderson, T. G. (2019). A multiscale productivity assessment of high Andean peatlands across the Chilean Altiplano using 31 years of Landsat imagery. Remote Sensing, 11(24), 2955. https://doi.org/10.3390/rs11242955
Mazzarino, M., & Finn, J. T. (2016). An NDVI analysis of vegetation trends in an Andean watershed. Wetlands Ecology and Management. https://doi.org/10.1007/s11273-016-9492-0
Dangles, O., Rabatel, A., Kraemer, M., Zeballos, G., Soruco, A., Jacobsen, D., & Anthelme, F. (2017). Ecosystem sentinels for climate change? Evidence of wetland cover changes over the last 30 years in the tropical Andes. PLoS ONE, 12(5), e0175814. https://doi.org/10.1371/journal.pone.0175814
Otto, M., Scherer, D., & Richters, J. (2011). Hydrological differentiation and spatial distribution of high altitude wetlands in a semi-arid Andean region derived from satellite data. Hydrology and Earth System Sciences, 15, 1713-1727. https://doi.org/10.5194/hess-15-1713-2011
Garcia, E., & Otto, M. (2015). Caracterización ecohidrológica de humedales alto andinos usando imágenes de satélite multitemporales en la cabecera de cuenca del río Santa, Ancash, Perú. Ecología Aplicada, 14(2), 115-125.
Hribljan, J. A., Suarez, E., Bourgeau-Chavez, L., Endres, S., Lilleskov, E. A., Chimbolema, S., Wayson, C., Serocki, E., & Chimner, R. A. (2017). Multidate, multisensor remote sensing reveals high density of carbon-rich mountain peatlands in the páramo of Ecuador. Global Change Biology, 23, 5412-5425. https://doi.org/10.1111/gcb.13807
Chimner, R. A., Bourgeau-Chavez, L., Grelik, S., Hribljan, J. A., Planas Clarke, A. M., Polk, M. H., Lilleskov, E. A., & Fuentealba, B. (2019). Mapping mountain peatlands and wet meadows using multi-date, multi-sensor remote sensing in the Cordillera Blanca, Peru. Wetlands. https://doi.org/10.1007/s13157-019-01134-1
Curatola Fernández, G. F., Makowski Giannoni, S., Delgado Florián, E., Rengifo, P., Rascón, J., Chichipe Vela, E., Butrich, C., Salas López, R., Oliva-Cruz, M., & Scheske, C. (2023). Mapping high-altitude peatlands to inform a landscape conservation strategy in the Andes of northern Peru. Environmental Conservation, 50, 212-219. https://doi.org/10.1017/S0376892923000267
Jara, C., Delegido, J., Ayala, J., Lozano, P., Armas, A., & Flores, V. (2019). Estudio de bofedales en los Andes ecuatorianos a través de la comparación de imágenes Landsat-8 y Sentinel-2. Revista de Teledetección, 53, 45-57. https://doi.org/10.4995/raet.2019.11715
Araya-López, R. A., Lopatin, J., Fassnacht, F. E., & Hernández, H. J. (2018). Monitoring Andean high

#### Modo `hibrido-0.3` (DeepSeek, búsqueda hibrida, ~7002 tok, 5.6 s, DOI: 8/9)

¡Buena pregunta! En los estudios que conozco, la base sigue siendo Landsat con índices de vegetación, cada vez más complementada con Sentinel-2, MODIS, imágenes de muy alta resolución, radar y drones (Síntesis — Teledetección y mapeo).

- **NDVI**: sirve para separar las vegas del entorno árido, sobre todo en la estación seca. Los umbrales varían según el sitio: 0,23 en el Altiplano chileno (Chávez et al., 2019), 0,3 en la cuenca de Nuñoa, Perú (Mazzarino y Finn, 2016), y 0,468 en la Cordillera Real de Bolivia (Dangles et al., 2017).
- **NDVI + NDII** (índice de agua, umbral 0,45): separa sectores inundados y humedales perennes de los temporales, con hasta 99 % de fiabilidad en la cabecera del río Santa, Perú (Otto et al., 2011; Garcia y Otto, 2015).
- **Óptico + radar (bandas L y C) + índices topográficos** con Random Forests: distingue turberas de praderas húmedas, con exactitudes de 90 % en el páramo ecuatoriano (Hribljan et al., 2017), 92 % en Huascarán (Chimner et al., 2019) y 97,1 % en la jalca de Amazonas (Curatola Fernández et al., 2023).

Un dato de cautela: el verdor no basta para detectar turba, porque cerca de un cuarto de los humedales con plantas en cojín de Huascarán no eran turberas (Chimner et al., 2019). Y ojo que todos estos ejemplos vienen de Perú, Bolivia, Ecuador y Chile; para la Puna argentina hay trabajos propios con Landsat y Sentinel-2 (Izquierdo et al., 2022).

Fuentes:
Chávez, R. O., Christie, D. A., Olea, M., & Anderson, T. G. (2019). A multiscale productivity assessment of high Andean peatlands across the Chilean Altiplano using 31 years of Landsat imagery. Remote Sensing, 11(24), 2955. https://doi.org/10.3390/rs11242955
Mazzarino, M., & Finn, J. T. (2016). An NDVI analysis of vegetation trends in an Andean watershed. Wetlands Ecology and Management. https://doi.org/10.1007/s11273-016-9492-0
Dangles, O., Rabatel, A., Kraemer, M., Zeballos, G., Soruco, A., Jacobsen, D., & Anthelme, F. (2017). Ecosystem sentinels for climate change? Evidence of wetland cover changes over the last 30 years in the tropical Andes. PLoS ONE, 12(5), e0175814. https://doi.org/10.1371/journal.pone.0175814
Otto, M., Scherer, D., & Richters, J. (2011). Hydrological differentiation and spatial distribution of high altitude wetlands in a semi-arid Andean region derived from satellite data. Hydrology and Earth System Sciences, 15, 1713-1727. https://doi.org/10.5194/hess-15-1713-2011
Garcia, E., & Otto, M. (2015). Caracterización ecohidrológica de humedales alto andinos usando imágenes de satélite multitemporales en la cabecera de cuenca del río Santa, Ancash, Perú. Ecología Aplicada, 14(2), 115-125.
Hribljan, J. A., Suarez, E., Bourgeau-Chavez, L., Endres, S., Lilleskov, E. A., Chimbolema, S., Wayson, C., Serocki, E., & Chimner, R. A. (2017). Multidate, multisensor remote sensing reveals high density of carbon-rich mountain peatlands in the páramo of Ecuador. Global Change Biology, 23, 5412-5425. https://doi.org/10.1111/gcb.13807
Chimner, R. A., Bourgeau-Chavez, L., Grelik, S., Hribljan, J. A., Planas Clarke, A. M., Polk, M. H., Lilleskov, E. A., & Fuentealba, B. (2019). Mapping mountain peatlands and wet meadows using multi-date, multi-sensor remote sensing in the Cordillera Blanca, Peru. Wetlands. https://doi.org/10.1007/s13157-019-01134-1
Curatola Fernández, G. F., Makowski Giannoni, S., Delgado Florián, E., Rengifo, P., Rascón, J., Chichipe Vela, E., Butrich, C., Salas López, R., Oliva-Cruz, M., & Scheske, C. (2023). Mapping high-altitude peatlands to inform a landscape conservation strategy in the Andes of northern Peru. Environmental Conservation, 50, 212-219. https://doi.org/10.1017/S0376892923000267
Izquierdo, A. E., Blundo, C., Carilla, J., Foguet, J., Navarro, C. J., Casagranda, E., Chiappero, M. F., & Vaieretti, M. V. (2022). Floristic types of high-Andean wetlands from northwest Argentina and their remote-sensed characterization at a regional scale. Applied Vegetation Science, 25, e12658. https://doi.org/10.1111/avsc.12658

#### Modo `hibrido-0.5` (DeepSeek, búsqueda hibrida, ~7140 tok, 3.7 s, DOI: 1/1)

¡Buena pregunta! Te cuento lo que muestran los estudios que conozco.

La base sigue siendo Landsat con índices de vegetación, cada vez más complementada con Sentinel-2, MODIS, radar, drones y aprendizaje automático (Síntesis — Teledetección y mapeo). Para delimitar vegas se usan índices como el NDVI —con umbrales que varían según el sitio: 0,23 en el Altiplano chileno, 0,3 en Nuñoa (Perú) y 0,468 en la Cordillera Real de Bolivia— y combinaciones de NDVI con el índice de agua NDII (umbral 0,45), que llegan a 99 % de fiabilidad en la cabecera del río Santa, Perú (Síntesis — Teledetección y mapeo). Para distinguir turberas de praderas húmedas, combinar imágenes ópticas Landsat con radar en bandas L y C e índices topográficos mediante Random Forests alcanzó 90 % en el páramo ecuatoriano, 92 % en Huascarán y 97,1 % en la jalca de Amazonas (Síntesis — Teledetección y mapeo).

En cuanto a sensores, Sentinel-2 suele superar a Landsat-8 y WorldView-2: en la Reserva Chimborazo (Ecuador) logró 86,59 % de exactitud frente a 77,90 % de Landsat-8, y en Chile central delimitó vegas con 94 % de exactitud y estimó mejor la humedad del suelo (r² 0,58 frente a 0,34) gracias al infrarrojo de onda corta (Síntesis — Teledetección y mapeo). Ojo: MODIS (250 m) capta solo unos dos tercios de los humedales detectados con Landsat y sobrestima los temporales (Síntesis — Teledetección y mapeo). Y en la Puna argentina, un estudio regional usó 4039 escenas Sentinel-2 y 1418 escenas Landsat 8 con índices de salinidad (SI/SI2) y humedad (NDWI/GVMI) para caracterizar cinco tipos florísticos de vegas (Izquierdo et al., 2022).

Fuentes:
Izquierdo, A. E., Blundo, C., Carilla, J., Foguet, J., Navarro, C. J., Casagranda, E., Chiappero, M. F., & Vaieretti, M. V. (2022). Floristic types of high-Andean wetlands from northwest Argentina and their remote-sensed characterization at a regional scale. Applied Vegetation Science, 25, e12658. https://doi.org/10.1111/avsc.12658

#### Modo `hibrido-0.7` (DeepSeek, búsqueda hibrida, ~7140 tok, 4.8 s, DOI: 2/2)

¡Buena pregunta! En los estudios que conozco, la base sigue siendo las series Landsat con índices de vegetación, cada vez más complementadas con Sentinel-2, MODIS, imágenes de muy alta resolución, radar, drones y aprendizaje automático (Izquierdo et al., 2022).

- **Índices de verdor y agua:** el NDVI es el más usado para separar vegas del resto del paisaje, con umbrales que varían según el sitio (0,23 en el Altiplano chileno, 0,3 en Nuñoa, Perú, y 0,468 en la Cordillera Real de Bolivia) (Araya-López et al., 2018). Combinar NDVI con el índice de agua NDII (umbral 0,45) permite distinguir sectores inundados y humedales perennes de los temporales, con hasta 99 % de fiabilidad en la cabecera del río Santa, Perú (Araya-López et al., 2018).
- **Sentinel-2 vs. Landsat-8 y WorldView-2:** Sentinel-2 rinde mejor por su resolución y sus bandas Red Edge y SWIR; en Ecuador alcanzó 86,59 % de exactitud frente a 77,90 % de Landsat-8, y en Chile central delimitó vegas con 94 % de exactitud y estimó mejor la humedad del suelo (r² 0,58 frente a 0,34 de WorldView-2) (Araya-López et al., 2018).
- **Radar + óptico con Random Forests:** combinar Landsat con radar en bandas L y C e índices topográficos permitió separar turberas de praderas húmedas con exactitudes de 90 % en el páramo ecuatoriano, 92 % en Huascarán y 97,1 % en la jalca de Amazonas (Araya-López et al., 2018). Ojo: el verdor no basta para detectar turba, porque cerca de un cuarto de los humedales con cojines de Huascarán no eran turberas (Araya-López et al., 2018).
- **MODIS (250 m):** capta solo unos dos tercios de los humedales que detecta Landsat y sobrestima los temporales, aunque sirvió para clasificar fisonomías regionales en Salta y Jujuy con 85 % de fiabilidad (Araya-López et al., 2018).

Casi todos estos ejemplos vienen de Perú, Bolivia, Chile y Ecuador; para la Puna argentina, el trabajo de referencia es la clasificación florística de 50 vegas con variables espaciales (SRTM) y espectrales de Sentinel-2 y Landsat 8 (Izquierdo et al., 2022).

Fuentes:
Araya-López, R. A., Lopatin, J., Fassnacht, F. E., & Hernández, H. J. (2018). Monitoring Andean high altitude wetlands in central Chile with seasonal optical data: A comparison between Worldview-2 and Sentinel-2 imagery. ISPRS Journal of Photogrammetry and Remote Sensing. https://doi.org/10.1016/j.isprsjprs.2018.04.001
Izquierdo, A. E., Blundo, C., Carilla, J., Foguet, J., Navarro, C. J., Casagranda, E., Chiappero, M. F., & Vaieretti, M. V. (2022). Floristic types of high-Andean wetlands from northwest Argentina and their remote-sensed characterization at a regional scale. Applied Vegetation Science, 25, e12658. https://doi.org/10.1111/avsc.12658

---

### 9. Vegetación / Cojines
**Pregunta:** ¿Qué especies de plantas en cojín dominan los bofedales y cómo se distribuyen según el ambiente?

#### Modo `completo` (DeepSeek, ~412054 tok, 5.3 s, DOI: 1/1)

En los bofedales de los Andes centrales las plantas en cojín que forman la turba son sobre todo juncáceas, y su dominio cambia con la humedad y la salinidad del agua. *Distichia muscoides* predomina en sitios húmedos, con poca sequía y aguas de vertiente pobres en sodio y cloruro; *Oxychloe andina* tolera mejor la aridez, la salinidad y el aporte de sedimentos, y domina hacia el sur y el oeste; *Patosia clandestina* aparece unos 200–250 m más abajo que las turberas de *Distichia*; y la ciperácea *Zameioscirpus atacamensis* domina en ambientes salinos, rara vez por encima de 4300 m (Ruthsatz, 2012). En la Puna argentina, el límite sur conocido de *Distichia* está cerca del Paso de Acay (Salta), y la riqueza de los bofedales disminuye desde Bolivia hacia el noroeste argentino y el norte de Chile por el aumento de la aridez y la salinidad de origen volcánico (Ruthsatz, 2012).

Fuentes:
Ruthsatz, B. (2012). Vegetación y ecología de los bofedales altoandinos de Bolivia (C. Pérez, Trad.). Phytocoenologia, 42(3-4), 133-179. https://doi.org/10.1127/0340-269X/2012/0042-0535

#### Modo `rag` (DeepSeek, búsqueda bm25, ~6876 tok, 2.5 s, DOI: 2/2)

¡Hola! En los bofedales, las plantas en cojín que suelen dominar son las juncáceas **Distichia muscoides**, **Oxychloe andina** y **Patosia clandestina**, y en sitios muy salinos la ciperácea **Zameioscirpus atacamensis** (Ruthsatz, 2012). Según el ambiente, los cojines de *Distichia* y *Oxychloe* aparecen solo en los sectores anegados, mientras que en los sectores desecados dominan gramíneas de ladera y halófitas (Domic et al., 2021). Además, los bofedales con solo *Patosia* suelen estar 200–250 m más bajos que los de *Distichia*, y los de *Distichia* con *Oxychloe* pueden superar los 5000 m (Ruthsatz, 2012).

Fuentes:
Ruthsatz, B. (2012). Vegetación y ecología de los bofedales altoandinos de Bolivia (C. Pérez, Trad.). Phytocoenologia, 42(3-4), 133-179. https://doi.org/10.1127/0340-269X/2012/0042-0535
Domic, A. I., Capriles, J. M., Meneses, R. I., & Pacheco, P. (2021). Plant community assembly is predicted by an environmental gradient in high-altitude wetlands in the semiarid western Bolivian Andes. Mires and Peat, 27, Article 01. https://doi.org/10.19189/MaP.2019.JSP.StA.1916

#### Modo `hibrido-0.3` (DeepSeek, búsqueda hibrida, ~7178 tok, 3.3 s, DOI: 2/2)

¡Hola! En los bofedales las plantas en cojín que forman turba y estructuran el humedal son sobre todo juncáceas: *Distichia muscoides*, *Oxychloe andina* y *Patosia clandestina* (Ruthsatz, 2012). La distribución depende del ambiente: *D. muscoides* domina en sitios húmedos y pobres en sales, *O. andina* tolera más aridez, salinidad y sedimentos, y *Patosia clandestina* aparece unos 200–250 m más abajo (Ruthsatz, 2012). En un gradiente de humedad dentro de bofedales del altiplano boliviano, *D. muscoides* y *O. andina* se hallaron solo en los sectores anegados, mientras que en los desecados dominaron gramíneas de ladera y halófitas (Domic et al., 2021). Ojo: estos estudios son de Bolivia, así que conviene tomarlos como referencia al pensar la Puna argentina.

Fuentes:
Ruthsatz, B. (2012). Vegetación y ecología de los bofedales altoandinos de Bolivia (C. Pérez, Trad.). Phytocoenologia, 42(3-4), 133-179. https://doi.org/10.1127/0340-269X/2012/0042-0535
Domic, A. I., Capriles, J. M., Meneses, R. I., & Pacheco, P. (2021). Plant community assembly is predicted by an environmental gradient in high-altitude wetlands in the semiarid western Bolivian Andes. Mires and Peat, 27, Article 01. https://doi.org/10.19189/MaP.2019.JSP.StA.1916

#### Modo `hibrido-0.5` (DeepSeek, búsqueda hibrida, ~7178 tok, 3.7 s, DOI: 3/4)

En los bofedales, las plantas en cojín que forman turba y estructuran el humedal son sobre todo las juncáceas *Distichia muscoides*, *Oxychloe andina* y *Patosia clandestina* (Ruthsatz, 2012; Squeo et al., 2006). Se reparten según el ambiente: *D. muscoides* domina en sitios húmedos y pobres en sales, mientras que *O. andina* tolera mayor aridez, salinidad y sedimentos, y *P. clandestina* aparece unos 200–250 m más abajo (Ruthsatz, 2012). En un bofedal boliviano, ambas especies en cojín se hallaron solo en los sectores anegados, no en los desecados (Domic et al., 2021). Además, *O. andina* es más alto (3,8 cm frente a 1,5 cm de *D. muscoides*) y, con sus hojas punzantes, ofrecería más refugio a otras plantas frente al pastoreo y el frío (Raevel et al., 2017).

Fuentes:
Ruthsatz, B. (2012). Vegetación y ecología de los bofedales altoandinos de Bolivia (C. Pérez, Trad.). Phytocoenologia, 42(3-4), 133-179. https://doi.org/10.1127/0340-269X/2012/0042-0535
Squeo, F. A., Warner, B. G., Aravena, R., & Espinoza, D. (2006). Bofedales: high altitude peatlands of the central Andes. [Revista no identificada], 245-255.
Domic, A. I., Capriles, J. M., Meneses, R. I., & Pacheco, P. (2021). Plant community assembly is predicted by an environmental gradient in high-altitude wetlands in the semiarid western Bolivian Andes. Mires and Peat, 27, Article 01. https://doi.org/10.19189/MaP.2019.JSP.StA.1916
Raevel, V., Anthelme, F., Meneses, R. I., & Munoz, F. (2017). Cushion-plant protection determines guild-dependent plant strategies in high-elevation peatlands of the Cordillera Real, Bolivian Andes. Perspectives in Plant Ecology, Evolution and Systematics. https://doi.org/10.1016/j.ppees.2017.09.006

#### Modo `hibrido-0.7` (DeepSeek, búsqueda hibrida, ~7437 tok, 2.9 s, DOI: 2/2)

¡Hola! En los bofedales, las plantas en cojín que forman turba son sobre todo juncáceas, y su dominancia cambia según el agua y la salinidad. *Distichia muscoides* aparece en aguas pobres en sodio y cloruro, con menor sequía; *Patosia clandestina* suele estar unos 200–250 m más abajo; *Oxychloe andina* domina sitios más secos, salinos o con sedimentos hacia el sur y el oeste; y la ciperácea *Zameioscirpus atacamensis* ocupa ambientes salinos, rara vez por encima de los 4.300 m (Ruthsatz, 2012). En un bofedal del altiplano boliviano, *D. muscoides* y *O. andina* aparecieron solo en los sectores anegados, mientras que en los desecados dominaron gramíneas de ladera y halófitas (Domic et al., 2021). Ojo: estos estudios son de Bolivia, aunque las mismas juncáceas dominan vegas de la Puna argentina (Ruthsatz, 2012).

Fuentes:
Ruthsatz, B. (2012). Vegetación y ecología de los bofedales altoandinos de Bolivia (C. Pérez, Trad.). Phytocoenologia, 42(3-4), 133-179. https://doi.org/10.1127/0340-269X/2012/0042-0535
Domic, A. I., Capriles, J. M., Meneses, R. I., & Pacheco, P. (2021). Plant community assembly is predicted by an environmental gradient in high-altitude wetlands in the semiarid western Bolivian Andes. Mires and Peat, 27, Article 01. https://doi.org/10.19189/MaP.2019.JSP.StA.1916

---

### 10. Atlas fotográfico
**Pregunta:** ¿Qué vega tiene más fotografías en el atlas fotográfico y en qué provincia está?

#### Modo `completo` (DeepSeek, ~412050 tok, 3.5 s, DOI: N/A)

La vega con más fotografías es **Real Grande**, con 64 fotos, y está en la provincia de **Catamarca**, en el departamento de Antofagasta de la Sierra (Atlas de vegas de la Puna argentina, data/fotos.json).

#### Modo `rag` (DeepSeek, búsqueda bm25, ~7318 tok, 1.8 s, DOI: 0/1)

¡Hola! La vega con más fotos es **Real Grande**, con 64 fotografías (16 con GPS exacto y 48 aproximadas), y está en el departamento de Antofagasta de la Sierra, en **Catamarca** (Atlas de vegas de la Puna argentina, data/fotos.json). Sus fotos van de 4158 a 4222 m s. n. m. y se tomaron en tres campañas: mayo 2018, febrero 2021 y octubre 2021 (Atlas de vegas de la Puna argentina, data/fotos.json).

Fuentes:
Atlas de vegas de la Puna argentina (data/fotos.json).

#### Modo `hibrido-0.3` (DeepSeek, búsqueda hibrida, ~7296 tok, 1.7 s, DOI: 0/1)

¡Hola! La vega con más fotografías es **Real Grande**, con 64 fotos (16 con GPS exacto y 48 aproximadas), y está en el departamento de Antofagasta de la Sierra, en **Catamarca** (Atlas de vegas de la Puna argentina, data/fotos.json). Sus fotos van de 4158 a 4222 m s. n. m. y se tomaron en tres campañas: mayo 2018, febrero 2021 y octubre 2021 (Atlas de vegas de la Puna argentina, data/fotos.json).

Fuentes:
Atlas de vegas de la Puna argentina (data/fotos.json).

#### Modo `hibrido-0.5` (DeepSeek, búsqueda hibrida, ~6937 tok, 1.5 s, DOI: 0/1)

La vega con más fotos es **Real Grande**, con 64 fotografías (16 con GPS exacto y 48 aproximadas), y está en **Antofagasta de la Sierra, Catamarca** (Atlas de vegas de la Puna argentina, data/fotos.json). Le siguen Antofalla (28) y Antofagasta (24), también en Catamarca.

Fuentes:
Atlas de vegas de la Puna argentina (data/fotos.json).

#### Modo `hibrido-0.7` (DeepSeek, búsqueda hibrida, ~7026 tok, 1.3 s, DOI: 0/1)

La vega con más fotografías es **Real Grande**, con 64 fotos (16 con GPS exacto y 48 aproximadas), y está en el departamento Antofagasta de la Sierra, provincia de Catamarca (Atlas de vegas de la Puna argentina, data/fotos.json).

Fuentes:
Atlas de vegas de la Puna argentina (data/fotos.json).

---

### 11. Cambio climático
**Pregunta:** ¿Cómo afecta el retroceso de glaciares y el cambio climático a estos humedales?

#### Modo `completo` (DeepSeek, ~412050 tok, 8.1 s, DOI: 7/7)

¡Buena pregunta! Es un tema central para nuestras vegas. Te cuento lo que muestran los estudios:

El retroceso glaciar puede expandir los humedales de forma transitoria, pero no los salva a largo plazo. En la Cordillera Real de Bolivia, la superficie de humedales creció 1,15 km²/año entre 1984 y 2011 mientras los glaciares perdían ~35%, aunque ese aumento se debió sobre todo a pastizales húmedos temporales y se espera que se revierta cuando disminuya el aporte de deshielo (Dangles et al., 2017). En Huascarán (Perú) los humedales pasaron de 12.402 a 13.858 ha entre 1987 y 1995, antes de empezar a retroceder tras el "pico de agua" (Polk et al., 2017).

Ojo: muchos bofedales dependen más del agua subterránea de laderas que del hielo directo. Diez turberas de Bolivia y Perú se alimentan de acuíferos de ladera recargados por lluvia y nieve, no de glaciares (Cooper et al., 2019). Pero en cabeceras muy glaciarizadas la cosa cambia: en Vilcanota, los bofedales aportan un caudal estable de ~0,09 m³/s (9–20% del estiaje) frente a 80–91% de origen glaciar, que se reduce a la mitad en la estación seca (Gribbin et al., 2024).

En la Puna argentina ya hay señales propias: una fase seca iniciada hace ~130 años en Cerro Tuzgle (Kock et al., 2019) y una retracción sostenida de lagunas desde 1930, acelerada desde 1976 (Morales et al., 2015). Además, el calentamiento experimental en suelos de vegas de Catamarca triplicó la respiración de CO₂, sobre todo en las vegas más altas y orgánicas (Chiappero et al., 2024).

Fuentes:
Dangles, O., Rabatel, A., Kraemer, M., Zeballos, G., Soruco, A., Jacobsen, D., & Anthelme, F. (2017). Ecosystem sentinels for climate change? Evidence of wetland cover changes over the last 30 years in the tropical Andes. PLoS ONE, 12(5), e0175814. https://doi.org/10.1371/journal.pone.0175814
Polk, M. H., Young, K. R., Baraer, M., Mark, B. G., McKenzie, J. M., Bury, J., & Carey, M. (2017). Exploring hydrologic connections between tropical mountain wetlands and glacier recession in Peru's Cordillera Blanca. Applied Geography, 78, 94-103. https://doi.org/10.1016/j.apgeog.2016.11.004
Cooper, D. J., Sueltenfuss, J., Oyague, E., Yager, K., Slayback, D., Cabero Caballero, E. M., Argollo, J., & Mark, B. G. (2019). Drivers of peatland water table dynamics in the central Andes, Bolivia and Peru. Hydrological Processes, 33, 1913-1925. https://doi.org/10.1002/hyp.13446
Gribbin, T., Mackay, J. D., MacDonald, A., Hannah, D. M., Buytaert, W., Baiker, J. R., Montoya, N., Perry, L. B., Seimon, A., Rado, M., Arias, S., & Vargas, M. (2024). Bofedal wetland and glacial melt contributions to dry season streamflow in a high-Andean headwater watershed. Hydrological Processes, 38(8), e15237. https://doi.org/10.1002/hyp.15237
Kock, S. T., Schittek, K., Wissel, H., Vos, H., Ohlendorf, C., Schäbitz, F., Lupo, L. C., Kulemeyer, J. J., & Lücke, A. (2019). Stable oxygen isotope records (δ18O) of a high-Andean cushion peatland in NW Argentina (24°S) imply South American Summer Monsoon related moisture changes during the Late Holocene. Frontiers in Earth Science, 7, 45. https://doi.org/10.3389/feart.2019.00045
Morales, M. S., Carilla, J., Grau, H. R., & Villalba, R. (2015). Multi-century lake area changes in the Andean high-elevation ecosystems of the Southern Altiplano. Climate of the Past Discussions, 11, 1821–1855. https://doi.org/10.5194/cpd-11-1821-2015
Chiappero, M. F., Vaieretti, M. V., Gallardo, N., & Izquierdo, A. E. (2024). Experimental warming increases respiration and affects microbial communities of soil wetlands at different elevations of the Argentinean Puna. Soil Ecology Letters, 6(4), 240242. https://doi.org/10.1007/s42832-024-0242-6

#### Modo `rag` (DeepSeek, búsqueda bm25, ~7422 tok, 4.6 s, DOI: 4/6)

¡Hola! Buena pregunta, y bien de actualidad. Te cuento lo que dicen los estudios, con una aclaración importante: buena parte de la evidencia viene de Bolivia, Perú y Chile, así que la aplicamos a la Puna argentina con cuidado.

- **El agua de deshielo primero sube y después baja.** Con el retroceso glaciar, el caudal aumenta al principio del derretimiento y disminuye a medida que el glaciar se achica, lo que puede afectar el área y el agua superficial de los bofedales (Dangles et al., 2014). En la Cordillera Blanca del Perú se propone que los humedales siguen esa curva de "pico de agua" con un desfase, y se prevé su degradación y fragmentación cuando caiga el aporte de deshielo (Polk et al., 2017).
- **En Bolivia, la cobertura de humedales creció entre 1984 y 2011**, sobre todo por parches temporales de pastizal húmedo en años lluviosos, mientras glaciares y nieve se redujeron cerca de 35 %; los autores prevén que ese aumento sea transitorio cuando disminuya el aporte glaciar (Dangles et al., 2017).
- **En la Puna argentina**, 15 lagunas puneñas se achicaron entre 1986 y 2017 y el verdor de las vegas siguió el área lacustre más que la lluvia satelital (Casagranda et al., 2019). A esto se suma el cambio climático superpuesto a una transición socioecológica: urbanización, caída de ovinos, expansión del litio y turismo (Izquierdo et al., 2018).
- **Como respuesta**, se promueven estrategias de adaptación basadas en ecosistemas y comunidades, con enfoque de cuenca (Lorini, 2014).

Fuentes:
Dangles, O., Meneses, R. I., & Anthelme, F. (2014). BIOTHAW: Un proyecto multidisciplinario que propone un marco metodológico para el estudio de los bofedales altoandinos en un contexto de cambio climático. Ecología en Bolivia, 49(3), 6-13.
Polk, M. H., Young, K. R., Baraer, M., Mark, B. G., McKenzie, J. M., Bury, J., & Carey, M. (2017). Exploring hydrologic connections between tropical mountain wetlands and glacier recession in Peru's Cordillera Blanca. Applied Geography, 78, 94-103. https://doi.org/10.1016/j.apgeog.2016.11.004
Dangles, O., Rabatel, A., Kraemer, M., Zeballos, G., Soruco, A., Jacobsen, D., & Anthelme, F. (2017). Ecosystem sentinels for climate change? Evidence of wetland cover changes over the last 30 years in the tropical Andes. PLoS ONE, 12(5), e0175814. https://doi.org/10.1371/journal.pone.0175814
Casagranda, E., Navarro, C., Grau, H. R., & Izquierdo, A. E. (2019). Interannual lake fluctuations in the Argentine Puna: Relationships with its associated peatlands and climate change. Regional Environmental Change, 19, 1737-1750. https://doi.org/10.1007/s10113-019-01514-7
Izquierdo, A. E., Grau, H. R., Navarro, C. J., Casagranda, E., Castilla, M. C., & Grau, A. (2018). Highlands in transition: Urbanization, pastoralism, mining, tourism, and wildlife in the Argentinian Puna. Mountain Research and Development, 38(4), 390-400. https://doi.org/10.1659/MRD-JOURNAL-D-17-00075.1
Lorini, H. (2014). Estrategia de adaptación al cambio climático para humedales altoandinos. Fundación Humedales / Wetlands International.

#### Modo `hibrido-0.3` (DeepSeek, búsqueda hibrida, ~7359 tok, 5.6 s, DOI: 7/7)

¡Buena pregunta! Te cuento lo que muestran los estudios, casi todos de Perú y Bolivia, así que ojo al aplicarlo a la Puna argentina.

El retroceso glaciar es generalizado: la Cordillera Blanca pasó de 723 km² en 1970 a 482 km² en 2010 (Polk et al., 2017), y la Cordillera Real perdió cerca del 48 % entre 1975 y 2006 (Cardenas et al., 2022). A corto plazo ese deshielo amplió los humedales —1,15 km² por año en la Cordillera Real entre 1984 y 2011 (Dangles et al., 2017), y de 12.402 a 13.858 ha en Huascarán entre 1987 y 1995 (Polk et al., 2017)—, pero se prevé que esa expansión sea transitoria y que los humedales se retraigan cuando baje el aporte de hielo (Dangles et al., 2017).

Hay un matiz importante: el agua subterránea y la nieve suelen pesar más que el deshielo directo. Diez turberas de Bolivia y Perú dependen de acuíferos de ladera recargados por lluvia y nieve (Cooper et al., 2019), y en la cuenca peruana Vilcanota-Urubamba el flujo subsuperficial no glaciar aportó el 74 % del caudal en estación seca frente a solo 12 % del deshielo (Ross et al., 2023). En cambio, en una cabecera muy glaciada de esa misma cordillera los bofedales aportaron apenas 9-20 % del caudal seco frente a 80-91 % de origen glaciar (Gribbin et al., 2024). O sea: los estudios no siempre coinciden en cuánto pesa el hielo, y depende mucho de la escala de cuenca.

Para la Puna argentina, donde casi no hay glaciares, la lluvia y el agua subterránea mandan más que el hielo (Navarro et al., 2020). ¿Querés que profundice en algún caso en particular?

Fuentes:
Polk, M. H., Young, K. R., Baraer, M., Mark, B. G., McKenzie, J. M., Bury, J., & Carey, M. (2017). Exploring hydrologic connections between tropical mountain wetlands and glacier recession in Peru's Cordillera Blanca. Applied Geography, 78, 94-103. https://doi.org/10.1016/j.apgeog.2016.11.004
Cardenas, T., Naoki, K., Landivar, C. M., Struelens, Q., Gómez, M. I., Meneses, R. I., Cauvy-Fraunié, S., Anthelme, F., & Dangles, O. (2022). Glacier influence on bird assemblages in habitat islands of the high Bolivian Andes. Diversity and Distributions, 28(2), 242-256. https://doi.org/10.1111/ddi.13458
Dangles, O., Rabatel, A., Kraemer, M., Zeballos, G., Soruco, A., Jacobsen, D., & Anthelme, F. (2017). Ecosystem sentinels for climate change? Evidence of wetland cover changes over the last 30 years in the tropical Andes. PLoS ONE, 12(5), e0175814. https://doi.org/10.1371/journal.pone.0175814
Cooper, D. J., Sueltenfuss, J., Oyague, E., Yager, K., Slayback, D., Cabero Caballero, E. M., Argollo, J., & Mark, B. G. (2019). Drivers of peatland water table dynamics in the central Andes, Bolivia and Peru. Hydrological Processes, 33, 1913-1925. https://doi.org/10.1002/hyp.13446
Ross, A. C., Mendoza, M. M., Drenkhan, F., Montoya, N., Baiker, J. R., Mackay, J. D., Hannah, D. M., & Buytaert, W. (2023). Seasonal water storage and release dynamics of bofedal wetlands in the Central Andes. Hydrological Processes, 37(8), e14940. https://doi.org/10.1002/hyp.14940
Gribbin, T., Mackay, J. D., MacDonald, A., Hannah, D. M., Buytaert, W., Baiker, J. R., Montoya, N., Perry, L. B., Seimon, A., Rado, M., Arias, S., & Vargas, M. (2024). Bofedal wetland and glacial melt contributions to dry season streamflow in a high-Andean headwater watershed. Hydrological Processes, 38(8), e15237. https://doi.org/10.1002/hyp.15237
Navarro, C. J., Izquierdo, A. E., Aráoz, E., Foguet, J., & Grau, H. R. (2020). Rewilding of large herbivore communities in high elevation Puna: Geographic segregation and no evidence of positive effects on peatland productivity. Regional Environmental Change, 20, 112. https://doi.org/10.1007/s10113-020-01704-8

#### Modo `hibrido-0.5` (DeepSeek, búsqueda hibrida, ~7297 tok, 4.9 s, DOI: 5/5)

¡Buena pregunta! Lo que muestran los estudios es que la respuesta no es una sola: depende del sitio y del plazo.

- **A corto plazo, el deshielo puede ampliar los humedales.** En la Cordillera Real de Bolivia la superficie de humedales sobre 4500 m creció 1,15 km² por año entre 1984 y 2011, sobre todo por parches temporales de pastizal húmedo y no por bofedales de cojín (Dangles et al., 2017). En Huascarán (Perú) pasaron de 12.402 a 13.858 ha entre 1987 y 1995, antes de bajar después del "pico de agua" (Polk et al., 2017).
- **Pero se prevé que esa expansión sea transitoria.** Con la retracción glaciar se anticipa degradación, fragmentación y pérdida de servicios como almacenamiento de carbono y agua (Polk et al., 2017; Dangles et al., 2017).
- **El agua subterránea y la lluvia pesan mucho.** Diez turberas de Bolivia y Perú dependen de acuíferos de ladera recargados por lluvia y nieve (Cooper et al., 2019), y en la cuenca Vilcanota-Urubamba el flujo subsuperficial no glaciar aportó el 74 % del caudal en estación seca frente a solo 12 % del deshielo (Ross et al., 2023).
- **Ojo con la escala:** en una cabecera muy glaciarizada de esa misma cordillera, en cambio, los bofedales aportaron solo 9-20 % del caudal seco frente a 80-91 % de origen glaciar (Gribbin et al., 2024). Es decir, los estudios no coinciden del todo y la importancia relativa varía con la escala de cuenca.

Todo esto viene de Bolivia y Perú; para la Puna argentina hay menos datos específicos sobre glaciares.

Fuentes:
Dangles, O., Rabatel, A., Kraemer, M., Zeballos, G., Soruco, A., Jacobsen, D., & Anthelme, F. (2017). Ecosystem sentinels for climate change? Evidence of wetland cover changes over the last 30 years in the tropical Andes. PLoS ONE, 12(5), e0175814. https://doi.org/10.1371/journal.pone.0175814
Polk, M. H., Young, K. R., Baraer, M., Mark, B. G., McKenzie, J. M., Bury, J., & Carey, M. (2017). Exploring hydrologic connections between tropical mountain wetlands and glacier recession in Peru's Cordillera Blanca. Applied Geography, 78, 94-103. https://doi.org/10.1016/j.apgeog.2016.11.004
Cooper, D. J., Sueltenfuss, J., Oyague, E., Yager, K., Slayback, D., Cabero Caballero, E. M., Argollo, J., & Mark, B. G. (2019). Drivers of peatland water table dynamics in the central Andes, Bolivia and Peru. Hydrological Processes, 33, 1913-1925. https://doi.org/10.1002/hyp.13446
Ross, A. C., Mendoza, M. M., Drenkhan, F., Montoya, N., Baiker, J. R., Mackay, J. D., Hannah, D. M., & Buytaert, W. (2023). Seasonal water storage and release dynamics of bofedal wetlands in the Central Andes. Hydrological Processes, 37(8), e14940. https://doi.org/10.1002/hyp.14940
Gribbin, T., Mackay, J. D., MacDonald, A., Hannah, D. M., Buytaert, W., Baiker, J. R., Montoya, N., Perry, L. B., Seimon, A., Rado, M., Arias, S., & Vargas, M. (2024). Bofedal wetland and glacial melt contributions to dry season streamflow in a high-Andean headwater watershed. Hydrological Processes, 38(8), e15237. https://doi.org/10.1002/hyp.15237

#### Modo `hibrido-0.7` (DeepSeek, búsqueda hibrida, ~7042 tok, 3.9 s, DOI: 4/4)

¡Buena pregunta! Te cuento lo que muestran los estudios, casi todos de los Andes tropicales (Bolivia y Perú), así que ojo al aplicarlo a la Puna argentina.

A corto plazo el deshielo puede **ampliar** los humedales: en la Cordillera Real de Bolivia la superficie de humedales sobre 4500 m creció 1,15 km² por año entre 1984 y 2011, sobre todo por pastizales húmedos temporales y no por bofedales de cojín (Dangles et al., 2017). En Huascarán (Perú) los humedales pasaron de 12.402 a 13.858 ha entre 1987 y 1995, y por cada hectárea de glaciar perdida el humedal aumentó 0,07 ha (Polk et al., 2017).

Pero ese aumento se prevé **transitorio**: cuando disminuya el aporte glaciar se espera retracción, fragmentación y pérdida de servicios como almacenamiento de carbono y agua (Dangles et al., 2017; Polk et al., 2017). Además, los acuíferos y la nieve suelen pesar más que el hielo directo: diez turberas de Bolivia y Perú dependen de acuíferos de ladera recargados por lluvia y nieve (Cooper et al., 2019), y en la cuenca peruana Vilcanota-Urubamba el flujo subsuperficial no glaciar aportó el 74 % del caudal en estación seca frente a solo 12 % del deshielo (Ross et al., 2023). ¿Querés que profundice en algún caso?

Fuentes:
Dangles, O., Rabatel, A., Kraemer, M., Zeballos, G., Soruco, A., Jacobsen, D., & Anthelme, F. (2017). Ecosystem sentinels for climate change? Evidence of wetland cover changes over the last 30 years in the tropical Andes. PLoS ONE, 12(5), e0175814. https://doi.org/10.1371/journal.pone.0175814
Polk, M. H., Young, K. R., Baraer, M., Mark, B. G., McKenzie, J. M., Bury, J., & Carey, M. (2017). Exploring hydrologic connections between tropical mountain wetlands and glacier recession in Peru's Cordillera Blanca. Applied Geography, 78, 94-103. https://doi.org/10.1016/j.apgeog.2016.11.004
Cooper, D. J., Sueltenfuss, J., Oyague, E., Yager, K., Slayback, D., Cabero Caballero, E. M., Argollo, J., & Mark, B. G. (2019). Drivers of peatland water table dynamics in the central Andes, Bolivia and Peru. Hydrological Processes, 33, 1913-1925. https://doi.org/10.1002/hyp.13446
Ross, A. C., Mendoza, M. M., Drenkhan, F., Montoya, N., Baiker, J. R., Mackay, J. D., Hannah, D. M., & Buytaert, W. (2023). Seasonal water storage and release dynamics of bofedal wetlands in the Central Andes. Hydrological Processes, 37(8), e14940. https://doi.org/10.1002/hyp.14940

---

### 12. Repregunta (pastoreo en Chile)
**Pregunta:** ¿Y en Chile qué muestran los estudios?
*(Con historial previo: "¿Cómo afecta el pastoreo de camélidos y ganado a las vegas y bofedales?")*

#### Modo `completo` (DeepSeek, ~412088 tok, 16.5 s, DOI: 3/4)

En Chile los estudios muestran las dos caras. En Arabilla (Tarapacá), *Oxychloe andina* solo alcanza para unas 60 de las 394 unidades animales que pastorean, así que el bofedal está sobrecargado (Carevic et al., 2019). En Atacama, el 100 % de 13 vegas precordilleranas presenta cárcavas y avance de *Tessaria absinthioides* por pastoreo caprino-ovino intensivo, mientras los bofedales altos casi no se degradan por su inaccesibilidad (Contreras Poblete, 2007). En Lauca, el ganado doméstico reduce las gramíneas palatables y favorece los cojines, mientras las vicuñas mantienen la riqueza vegetal (Rundel y Palma, 2000). Y en el altiplano de Tarapacá, burros asilvestrados y vicuñas coinciden en vegas sobre 3700 m (~15 % de avistamientos), aunque sin desplazamiento a escala de paisaje (Malo et al., 2016).

Fuentes:
Carevic, F. S., Anderson, M., & Muñoz, A. (2019). Is the temporary grazing exclusion a good management alternative for arid peatlands? Arid Land Research and Management. https://doi.org/10.1080/15324982.2018.1563242
Contreras Poblete, R. F. (2007). Uso de vegas y bofedales de la zona cordillerana y precordillerana de la Región de Atacama [Memoria de título de Ingeniero Forestal]. Universidad de Chile, Facultad de Ciencias Forestales.
Rundel, P. W., & Palma, B. (2000). Preserving the unique puna ecosystems of the Andean Altiplano: A descriptive account of Lauca National Park, Chile. Mountain Research and Development, 20(3), 262-271. https://doi.org/10.1659/0276-4741(2000)020[0262:PTUPEO]2.0.CO;2
Malo, J. E., González, B. A., Mata, C., Vielma, A., Donoso, D. S., Fuentes, N., & Estades, C. F. (2016). Low habitat overlap at landscape scale between wild camelids and feral donkeys in the Chilean desert. Acta Oecologica, 70, 1-9. https://doi.org/10.1016/j.actao.2015.11.002

#### Modo `rag` (DeepSeek, búsqueda bm25, ~7431 tok, 3.1 s, DOI: 2/3)

En Chile hay estudios sobre pastoreo en vegas y bofedales, pero con matices. En la Región de Atacama, Contreras Poblete (2007) documenta el uso de vegas y bofedales cordilleranos y precordilleranos, y el pastoreo intenso se asocia con el desplazamiento de los cojines por especies indicadoras de sobrepastoreo (Contreras Poblete, 2007). En el norte de Chile, el ganado doméstico se correlaciona fuertemente con la superficie de bofedal (r² = 0,67), mientras las vicuñas muestran menor acceso (Shaw et al., 2012). En Tarapacá, los burros asilvestrados no desplazaron a las vicuñas a escala de paisaje, aunque coinciden localmente en vegas sobre 3700 m (15,7 % y 15,4 % de avistamientos) (Malo et al., 2016). Ojo: son estudios de Chile, así que conviene tomarlos como referencia y no trasladarlos sin más a la Puna argentina.

Fuentes:
Contreras Poblete, R. F. (2007). Uso de vegas y bofedales de la zona cordillerana y precordillerana de la Región de Atacama [Memoria de título de Ingeniero Forestal]. Universidad de Chile, Facultad de Ciencias Forestales.
Shaw, A. K., Galaz, J. L., & Marquet, P. A. (2012). Population dynamics of the vicuña (Vicugna vicugna): density-dependence, rainfall, and spatial distribution. Journal of Mammalogy, 93(3), 658-666. https://doi.org/10.1644/11-MAMM-A-257.1
Malo, J. E., González, B. A., Mata, C., Vielma, A., Donoso, D. S., Fuentes, N., & Estades, C. F. (2016). Low habitat overlap at landscape scale between wild camelids and feral donkeys in the Chilean desert. Acta Oecologica, 70, 1-9. https://doi.org/10.1016/j.actao.2015.11.002

#### Modo `hibrido-0.3` (DeepSeek, búsqueda hibrida, ~7420 tok, 3.5 s, DOI: 2/3)

En Chile, el estudio de Carevic et al. (2019) en Arabilla mostró que los cojines de *Oxychloe andina* solo sostienen 60 de 394 unidades animales, es decir, la carga supera la capacidad del bofedal (Carevic et al., 2019). También se documentó que vacas, ovejas y cabras causan mayores impactos que los camélidos (Contreras Poblete, 2007). Y en Chiu-Chiu, la denegación estatal de derechos de riego secó la vega y redujo el ganado de ~3000 a 50-100 cabezas (Prieto, 2015). Ojo: son casos de Chile, no de la Puna argentina.

Fuentes:
Carevic, F. S., Anderson, M., & Muñoz, A. (2019). Is the temporary grazing exclusion a good management alternative for arid peatlands? Arid Land Research and Management. https://doi.org/10.1080/15324982.2018.1563242
Contreras Poblete, R. F. (2007). Uso de vegas y bofedales de la zona cordillerana y precordillerana de la Región de Atacama [Memoria de título de Ingeniero Forestal]. Universidad de Chile, Facultad de Ciencias Forestales.
Prieto, M. (2015). Privatizing water in the Chilean Andes: The case of Las Vegas de Chiu-Chiu. Mountain Research and Development, 35(3), 220-229. https://doi.org/10.1659/MRD-JOURNAL-D-14-00033.1

#### Modo `hibrido-0.5` (DeepSeek, búsqueda hibrida, ~7070 tok, 2.9 s, DOI: 2/3)

En Chile hay varios trabajos que muestran efectos del pastoreo sobre vegas y bofedales. En Arabilla, *Oxychloe andina* sostiene solo 60 de 394 unidades animales, o sea que la carga excede la oferta forrajera (Carevic et al., 2019). En la Región de Atacama se documentó que vacas, ovejas y cabras causan mayores impactos que los camélidos (Contreras Poblete, 2007). Y en Tarapacá, los burros asilvestrados coincidieron con camélidos en vegas sobre 3.700 m (~15 % de avistamientos), con riesgo de introgresión genética por híbridos guanaco × llama (Malo et al., 2016). Ojo: son estudios chilenos, así que conviene tomarlos como referencia y no trasladarlos sin más a la Puna argentina.

Fuentes:
Carevic, F. S., Anderson, M., & Muñoz, A. (2019). Is the temporary grazing exclusion a good management alternative for arid peatlands? Arid Land Research and Management. https://doi.org/10.1080/15324982.2018.1563242
Contreras Poblete, R. F. (2007). Uso de vegas y bofedales de la zona cordillerana y precordillerana de la Región de Atacama [Memoria de título de Ingeniero Forestal]. Universidad de Chile, Facultad de Ciencias Forestales.
Malo, J. E., González, B. A., Mata, C., Vielma, A., Donoso, D. S., Fuentes, N., & Estades, C. F. (2016). Low habitat overlap at landscape scale between wild camelids and feral donkeys in the Chilean desert. Acta Oecologica, 70, 1-9. https://doi.org/10.1016/j.actao.2015.11.002

#### Modo `hibrido-0.7` (DeepSeek, búsqueda hibrida, ~7431 tok, 3.7 s, DOI: 2/5)

En Chile, los estudios que conozco sobre pastoreo en vegas y bofedales son más bien pocos y no todos coinciden. En la Región de Atacama se documentó que vacas, ovejas y cabras causan mayores impactos que los camélidos (Contreras Poblete, 2007), y en Caquena las correlaciones entre ganado y NDVI fueron bajas (Meza Aliaga y Díaz Villalobos, 2014). También en Chile, una exclusión temporaria de pastoreo en turberas áridas no cambió la biomasa ni la cobertura total (Carevic et al., 2019), y en la Vega Tambo excluir guanacos no alteró biomasa ni diversidad (Squeo et al., 2006). Además, en Tarapacá los burros asilvestrados no desplazaron a las vicuñas a escala de paisaje, aunque coinciden localmente en vegas sobre 3700 m (Malo et al., 2016).

Fuentes:
Contreras Poblete, R. F. (2007). Uso de vegas y bofedales de la zona cordillerana y precordillerana de la Región de Atacama [Memoria de título de Ingeniero Forestal]. Universidad de Chile, Facultad de Ciencias Forestales.
Meza Aliaga, M., & Díaz Villalobos, Y. (2014). Efectos de la variabilidad climática sobre las fluctuaciones del nivel de las aguas y actividad ganadera en humedales altoandinos. Interciencia, 39(9), 651-658.
Carevic, F. S., Anderson, M., & Muñoz, A. (2019). Is the temporary grazing exclusion a good management alternative for arid peatlands? Arid Land Research and Management. https://doi.org/10.1080/15324982.2018.1563242
Squeo, F. A., Ibacache, E., Warner, B., Espinoza, D., Aravena, R., & Gutiérrez, J. R. (2006). Productividad y diversidad florística de la Vega Tambo, Cordillera de Doña Ana. En Geoecología de los Andes desérticos. La Alta Montaña del Valle del Elqui (pp. 1-27).
Malo, J. E., González, B. A., Mata, C., Vielma, A., Donoso, D. S., Fuentes, N., & Estades, C. F. (2016). Low habitat overlap at landscape scale between wild camelids and feral donkeys in the Chilean desert. Acta Oecologica, 70, 1-9. https://doi.org/10.1016/j.actao.2015.11.002

---

### 13. Repregunta (carbono en Puna arg.)
**Pregunta:** ¿Y en la Puna argentina hay datos de eso?
*(Con historial previo: "¿Cuánto carbono orgánico acumulan los suelos de turberas y bofedales andinos?")*

#### Modo `completo` (DeepSeek, ~412088 tok, 4.4 s, DOI: 2/2)

Sí, hay datos propios de la Puna argentina. En diez vegas puneñas (3323–4748 m), los primeros 30 cm de suelo promediaron 66,11 Mg C ha⁻¹ (rango 21,79–139,67), y ese carbono representó más del 70 % del total del sistema, sin caer con la profundidad por la intercalación de capas minerales y orgánicas (Chiappero et al., 2026). Además, dos turberas vecinas junto a un mismo salar en Catamarca difirieron cuatro veces entre sí: 281,8 Mg C ha⁻¹ en Laguna Negra frente a 71,5 Mg C ha⁻¹ en Laguna Tres Quebradas (Chiappero et al., 2021). Eso muestra que cada vega puede comportarse distinto y conviene monitorearlas por separado, sobre todo frente a la minería de litio.

Fuentes:
Chiappero, M. F., Vaieretti, M. V., & Izquierdo, A. E. (2021). A baseline soil survey of two peatlands associated with a lithium-rich salt flat in the Argentine Puna: physico-chemical characteristics, carbon storage and biota. Mires and Peat, 27, Article 16, 1–13. https://doi.org/10.19189/MaP.2020.OMB.StA.2126
Chiappero, M. F., Vaieretti, M. V., Gallardo, N., & Izquierdo, A. E. (2026). Carbon storage patterns in high Andean wetlands: local factors explain the variability of soil carbon stocks in the Argentine Puna. Plant and Soil, 525, 1393–1408. https://doi.org/10.1007/s11104-026-08829-5

#### Modo `rag` (DeepSeek, búsqueda bm25, ~7435 tok, 3.8 s, DOI: 3/3)

En los estudios que conozco no hay datos de carbono orgánico en suelos de vegas de la Puna argentina. La revisión de Alavi-Murillo et al. (2022) muestra que el sur andino, incluida la Puna argentina, casi no tiene datos de carbono en suelos, y que las turberas están subrepresentadas en la compilación (solo 14 muestras, de Bolivia, Perú y Ecuador) (Alavi-Murillo et al., 2022). Lo que sí hay son antecedentes de otros países que sirven de marco: en bofedales de Junín (Perú) se midió 11,2 ± 1,60 % de carbono orgánico en los primeros 30 cm y un stock de 210,9 t ha-1 (Carbajal et al., 2024), y en turberas de la Cordillera Blanca (Perú) un 15,7 % de carbono a 35-40 cm frente a 2,9 % en praderas húmedas (Chimner et al., 2019). Ojo, son ambientes más húmedos que la Puna argentina, así que conviene tomarlos como referencia y no como valores esperables para tus vegas.

Fuentes:
Alavi-Murillo, G., Diels, J., Gilles, J., & Willems, P. (2022). Soil organic carbon in Andean high-mountain ecosystems: Importance, challenges, and opportunities for carbon sequestration. Regional Environmental Change, 22, 128. https://doi.org/10.1007/s10113-022-01980-6
Carbajal, M., Ramírez, D. A., Turin, C., Schaeffer, S. M., Konkel, J., Ninanya, J., Rinza, J., De Mendiburu, F., Zorogastua, P., Villaorduña, L., & Quiroz, R. (2024). From rangelands to cropland, land-use change and its impact on soil organic carbon variables in a Peruvian Andean highlands: A machine learning modeling approach. Ecosystems, 27, 899-917. https://doi.org/10.1007/s10021-024-00928-7
Chimner, R. A., Bourgeau-Chavez, L., Grelik, S., Hribljan, J. A., Planas Clarke, A. M., Polk, M. H., Lilleskov, E. A., & Fuentealba, B. (2019). Mapping mountain peatlands and wet meadows using multi-date, multi-sensor remote sensing in the Cordillera Blanca, Peru. Wetlands. https://doi.org/10.1007/s13157-019-01134-1

#### Modo `hibrido-0.3` (DeepSeek, búsqueda hibrida, ~7477 tok, 2.2 s, DOI: 2/2)

Sí, hay datos, aunque todavía pocos. En diez vegas de la Puna argentina el reservorio medio de carbono en el suelo (0–30 cm) fue de 66,11 Mg C ha-1, con un rango de 21,79 a 139,67 (Chiappero et al., 2026). En la síntesis ecorregional de 12 estudios de la Puna (Argentina, Perú y Bolivia) los reservorios variaron entre 23 y 688 Mg C ha-1, con una media de 173,94 (Chiappero et al., 2026). Una revisión regional señala justamente que el sur andino, incluida la Puna argentina, casi no tiene datos de carbono en suelos (Alavi-Murillo et al., 2022).

Fuentes:
Chiappero, M. F., Vaieretti, M. V., Gallardo, N., & Izquierdo, A. E. (2026). Carbon storage patterns in high Andean wetlands: local factors explain the variability of soil carbon stocks in the Argentine Puna. Plant and Soil, 525, 1393–1408. https://doi.org/10.1007/s11104-026-08829-5
Alavi-Murillo, G., Diels, J., Gilles, J., & Willems, P. (2022). Soil organic carbon in Andean high-mountain ecosystems: Importance, challenges, and opportunities for carbon sequestration. Regional Environmental Change, 22, 128. https://doi.org/10.1007/s10113-022-01980-6

#### Modo `hibrido-0.5` (DeepSeek, búsqueda hibrida, ~6949 tok, 2.7 s, DOI: 2/2)

En los estudios que conozco, la Puna argentina casi no tiene datos propios de carbono en suelos de vegas: la revisión de Alavi-Murillo et al. (2022) señala que el sur andino y las turberas están subrepresentados (solo 14 muestras de turberas, de Bolivia, Perú y Ecuador), así que lo que hay son valores de referencia de otros países. Por ejemplo, en bofedales de Bolivia los suelos superficiales llegan a cerca de 500 g/kg de carbono orgánico (Alavi-Murillo et al., 2022), y en bofedales de Puno, Perú, se reportan stocks de 23 a 30 kg C/m² en los primeros 30 cm según el régimen de inundación (Segnini et al., 2010). Esos datos sirven para dimensionar el vacío y como marco comparativo, pero no reemplazan mediciones en vegas puneñas argentinas.

Fuentes:
Alavi-Murillo, G., Diels, J., Gilles, J., & Willems, P. (2022). Soil organic carbon in Andean high-mountain ecosystems: Importance, challenges, and opportunities for carbon sequestration. Regional Environmental Change, 22, 128. https://doi.org/10.1007/s10113-022-01980-6
Segnini, A., Posadas, A., Quiroz, R., Milori, D. M. B. P., Saab, S. C., Martin Neto, L., & Vaz, C. M. P. (2010). Spectroscopic assessment of soil organic matter in wetlands from the High Andes. Soil Science Society of America Journal, 74(6), 2246-2253. https://doi.org/10.2136/sssaj2009.0445

#### Modo `hibrido-0.7` (DeepSeek, búsqueda hibrida, ~7217 tok, 2.3 s, DOI: 2/2)

En los estudios disponibles no aparece información sobre carbono orgánico en suelos de vegas de la Puna argentina. La compilación de Alavi-Murillo et al. (2022) señala justamente que el sur andino, incluida la Puna argentina, casi no tiene datos de carbono en suelos, y que las turberas están subrepresentadas en la evidencia (solo 14 muestras, de Bolivia, Perú y Ecuador). Lo más cercano son los datos de puna de Perú y Bolivia (Hribljan et al., 2024), que no incluyen muestras argentinas.

Fuentes:
Alavi-Murillo, G., Diels, J., Gilles, J., & Willems, P. (2022). Soil organic carbon in Andean high-mountain ecosystems: Importance, challenges, and opportunities for carbon sequestration. Regional Environmental Change, 22, 128. https://doi.org/10.1007/s10113-022-01980-6
Hribljan, J. A., Hough, M., Lilleskov, E. A., Suarez, E., Heckman, K., Planas-Clarke, A. M., & Chimner, R. A. (2024). Elevation and temperature are strong predictors of long-term carbon accumulation across tropical Andean mountain peatlands. Mitigation and Adaptation Strategies for Global Change, 29, 1. https://doi.org/10.1007/s11027-023-10089-y

---

### 14. Fuera de tema
**Pregunta:** ¿Cuál es la receta tradicional de pizza napolitana?

#### Modo `completo` (DeepSeek, ~412043 tok, 4.4 s, DOI: N/A)

Uy, esa me la sé de memoria… pero no la puedo contar. Mi mundo son las vegas, los bofedales y las turberas de la Puna: sobre pizza napolitana no tengo nada en mi base de conocimiento, así que no te voy a inventar ingredientes ni tiempos de horno.

Si querés, te cuento cómo se cocina "a fuego lento" la turba en una vega, o qué plantas forman los cojines de Oxychloe y Distichia. ¿Te interesa alguno de esos temas?

#### Modo `rag` (DeepSeek, búsqueda bm25, ~7386 tok, 1.6 s, DOI: N/A)

Uy, esa me la sé de memoria… pero no, che: de cocina no hablo. Soy Doña Vicuña y solo sé de vegas, bofedales, turberas y humedales altoandinos. Si querés, preguntame por el agua, el pastoreo o las plantas de estos humedales de la Puna.

#### Modo `hibrido-0.3` (sin-contexto, búsqueda hibrida, ~0 tok, 0.0 s, DOI: N/A)

En los estudios disponibles no aparece información sobre eso. Si querés, preguntame sobre vegas, bofedales, turberas o humedales altoandinos (definiciones, agua, vegetación, pastoreo, carbono, minería, monitoreo satelital o el atlas fotográfico de la Puna argentina) y te cuento lo que dice la bibliografía.

#### Modo `hibrido-0.5` (sin-contexto, búsqueda hibrida, ~0 tok, 0.0 s, DOI: N/A)

En los estudios disponibles no aparece información sobre eso. Si querés, preguntame sobre vegas, bofedales, turberas o humedales altoandinos (definiciones, agua, vegetación, pastoreo, carbono, minería, monitoreo satelital o el atlas fotográfico de la Puna argentina) y te cuento lo que dice la bibliografía.

#### Modo `hibrido-0.7` (sin-contexto, búsqueda hibrida, ~0 tok, 0.0 s, DOI: N/A)

En los estudios disponibles no aparece información sobre eso. Si querés, preguntame sobre vegas, bofedales, turberas o humedales altoandinos (definiciones, agua, vegetación, pastoreo, carbono, minería, monitoreo satelital o el atlas fotográfico de la Puna argentina) y te cuento lo que dice la bibliografía.

---

### 15. Sin datos en la wiki
**Pregunta:** ¿Cuál fue el caudal exacto del río Loa en enero de 2025 medido por la estación de Calama?

#### Modo `completo` (DeepSeek, ~412052 tok, 8.9 s, DOI: 1/1)

En los estudios que conozco no hay datos sobre el caudal del río Loa en enero de 2025 medido en la estación de Calama. Lo que sí hay de esa cuenca es otra cosa: en Chiu-Chiu, sobre el Loa, se documentó cómo la privatización del agua secó las vegas del pueblo y redujo el ganado de unas 3000 cabezas a 50–100 (Prieto, 2015). Si te interesa el tema del agua en esa zona, puedo contarte más sobre eso.

Fuentes:
Prieto, M. (2015). Privatizing water in the Chilean Andes: The case of Las Vegas de Chiu-Chiu. Mountain Research and Development, 35(3), 220-229. https://doi.org/10.1659/MRD-JOURNAL-D-14-00033.1

#### Modo `rag` (DeepSeek, búsqueda bm25, ~7395 tok, 2.0 s, DOI: 1/1)

En los estudios disponibles no aparece información sobre eso: no hay datos de caudal del río Loa medidos en Calama en enero de 2025. Lo que sí hay sobre el Loa es de otro contexto y otra fuente: el trabajo de Prieto (2015) en Chiu-Chiu, a 2535 m s. n. m., donde tras la privatización se asignaron 850 l/s del río Loa, aguas arriba de Chiu-Chiu, a la empresa sanitaria estatal (Prieto, 2015). Ese dato es de Chile, no de la Puna argentina, y no corresponde a una medición de estación en 2025.

Fuentes:
Prieto, M. (2015). Privatizing water in the Chilean Andes: The case of Las Vegas de Chiu-Chiu. Mountain Research and Development, 35(3), 220-229. https://doi.org/10.1659/MRD-JOURNAL-D-14-00033.1

#### Modo `hibrido-0.3` (DeepSeek, búsqueda hibrida, ~6991 tok, 1.8 s, DOI: 1/1)

En los estudios disponibles no aparece información sobre eso: no hay datos de caudal del río Loa medidos en Calama en enero de 2025. Lo que sí documenta Prieto (2015) para esa zona es otro dato hídrico: tras la privatización se asignaron 850 l/s del Loa, aguas arriba de Chiu-Chiu, a la empresa sanitaria estatal para sostener el crecimiento urbano ligado al auge minero (Prieto, 2015).

Fuentes:
Prieto, M. (2015). Privatizing water in the Chilean Andes: The case of Las Vegas de Chiu-Chiu. Mountain Research and Development, 35(3), 220-229. https://doi.org/10.1659/MRD-JOURNAL-D-14-00033.1

#### Modo `hibrido-0.5` (DeepSeek, búsqueda hibrida, ~6991 tok, 2.5 s, DOI: 1/1)

En los estudios disponibles no aparece información sobre eso: no hay datos de caudal del río Loa medidos en Calama en enero de 2025. Lo que sí documenta el trabajo de Prieto (2015) para esa cuenca es otra cosa: que tras la privatización se asignaron 850 l/s del Loa, aguas arriba de Chiu-Chiu, a la empresa sanitaria estatal para sostener el crecimiento urbano ligado al auge minero (Prieto, 2015). Ese dato es de Chile, no de la Puna argentina.

Fuentes:
Prieto, M. (2015). Privatizing water in the Chilean Andes: The case of Las Vegas de Chiu-Chiu. Mountain Research and Development, 35(3), 220-229. https://doi.org/10.1659/MRD-JOURNAL-D-14-00033.1

#### Modo `hibrido-0.7` (DeepSeek, búsqueda hibrida, ~7029 tok, 2.4 s, DOI: 1/1)

En los estudios disponibles no aparece información sobre eso: no hay datos de caudal del río Loa medidos en enero de 2025 en la estación de Calama. Lo que sí hay, para el caso de Chiu-Chiu (Chile, a 2535 m sobre el río Loa), es el registro de que tras la privatización se asignaron 850 l/s del Loa, aguas arriba de Chiu-Chiu, a la empresa sanitaria estatal para sostener el crecimiento urbano ligado al auge minero (Prieto, 2015). Si te interesa el tema del agua en vegas andinas, puedo contarte más sobre ese caso.

Fuentes:
Prieto, M. (2015). Privatizing water in the Chilean Andes: The case of Las Vegas de Chiu-Chiu. Mountain Research and Development, 35(3), 220-229. https://doi.org/10.1659/MRD-JOURNAL-D-14-00033.1

---
