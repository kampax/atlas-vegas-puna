# Comparación de modos: `completo` vs `rag`

- Fecha: 2026-11-20 15:59 UTC
- Preguntas evaluadas: 15
- Proveedor configurado: `glm` (respaldo: `deepseek`)

## Tabla resumen

| # | Categoría | Prov. (comp / rag) | Tokens in (comp / rag) | Tiempo s (comp / rag) | Fuentes (comp / rag) | DOI en Fuentes (comp / rag) |
|---:|---|---|---:|---:|---|---|
| 1 | Definición | DeepSeek / DeepSeek | 194.987 / 6.702 | 10.4 / 3.9 | 2 / 3 | 2/2 / 3/3 |
| 2 | Puna argentina vs. otros países | DeepSeek / DeepSeek | 194.999 / 6.527 | 4.9 / 3.1 | 5 / 2 | 5/5 / 2/2 |
| 3 | Cifras concretas | DeepSeek / DeepSeek | 194.997 / 6.560 | 3.1 / 2.0 | 3 / 2 | 3/3 / 2/2 |
| 4 | Pastoreo | DeepSeek / DeepSeek | 194.991 / 6.718 | 4.5 / 5.4 | 4 / 6 | 4/4 / 6/6 |
| 5 | Agua / Hidrología | DeepSeek / DeepSeek | 194.989 / 6.737 | 4.9 / 3.9 | 3 / 5 | 3/3 / 5/5 |
| 6 | Carbono | DeepSeek / DeepSeek | 194.993 / 6.278 | 5.4 / 3.6 | 5 / 3 | 5/5 / 3/3 |
| 7 | Minería / Litio | DeepSeek / DeepSeek | 194.996 / 6.710 | 7.0 / 4.7 | 6 / 4 | 6/6 / 4/4 |
| 8 | Teledetección / Mapeo | DeepSeek / DeepSeek | 194.995 / 6.303 | 6.6 / 6.2 | 8 / 10 | 8/8 / 9/10 |
| 9 | Vegetación / Cojines | DeepSeek / DeepSeek | 194.997 / 6.720 | 4.7 / 3.0 | 2 / 2 | 2/2 / 2/2 |
| 10 | Atlas fotográfico | DeepSeek / DeepSeek | 194.993 / 6.403 | 3.0 / 1.7 | 1 / 1 | 0/1 / 0/1 |
| 11 | Cambio climático | DeepSeek / DeepSeek | 194.993 / 6.427 | 5.7 / 3.4 | 6 / 2 | 6/6 / 2/2 |
| 12 | Repregunta (pastoreo en Chile) | DeepSeek / DeepSeek | 195.031 / 6.655 | 4.1 / 3.5 | 4 / 3 | 4/4 / 3/3 |
| 13 | Repregunta (carbono en Puna arg.) | DeepSeek / DeepSeek | 195.031 / 6.793 | 4.2 / 2.6 | 2 / 3 | 2/2 / 3/3 |
| 14 | Fuera de tema | DeepSeek / DeepSeek | 194.986 / 6.650 | 7.7 / 2.1 | 0 / 2 | N/A / 1/2 |
| 15 | Sin datos en la wiki | DeepSeek / DeepSeek | 194.996 / 6.309 | 3.1 / 1.9 | 1 / 1 | 1/1 / 1/1 |

## Promedios y totales

- **Tokens de entrada promedio:** completo = 194.998 | rag = 6.566 (**96.6 % menos** en RAG)
- **Tiempo promedio:** completo = 5.28 s | rag = 3.41 s
- **DOIs en bloque Fuentes:** completo = 51/52 | rag = 46/49

## Detalle por pregunta

### 1. Definición
**Pregunta:** ¿Qué es una vega y en qué se diferencia de un bofedal?

#### Modo `completo` (DeepSeek, ~194987 tok, 10.4 s, DOI: 2/2)

¡Buena pregunta! Y ojo que la palabra "vega" tiene sus bemoles.

En los Andes Centrales hay una propuesta que reserva "vega" (o "ciénaga") para las praderas húmedas sin turba de altitudes medias, entre 3000 y 4000 m, de menor valor forrajero y a menudo sin manejo, y deja "bofedal" para los humedales de juncáceas en cojín entre 3500 y 5000 m (Yager et al., 2021). Pero en la Puna argentina "vega" se usa también para turberas de cojín, como la de Cerro Tuzgle, a 4350 m y formada sobre todo por *Oxychloe andina* (Schittek et al., 2016). Los propios autores de esa distinción advierten que en Argentina "vega" nombra humedales con turba (Yager et al., 2021).

Así que, si sos de acá, lo más práctico es decir "vega" y después aclarar si tiene turba o no. ¿Querés que te cuente cómo se clasifican según la planta en cojín que las forma?

Fuentes:
Yager, K., Prieto, M., & Meneses, R. I. (2021). Reframing pastoral practices of bofedal management to increase the resilience of Andean water towers. Mountain Research and Development, 41(4), A1-A9. https://doi.org/10.1659/MRD-JOURNAL-D-21-00011.1
Schittek, K., Kock, S. T., Lücke, A., Hense, J., Ohlendorf, C., Kulemeyer, J. J., Lupo, L. C., & Schäbitz, F. (2016). A high-altitude peatland record of environmental changes in the NW Argentine Andes (24°S) over the last 2100 years. Climate of the Past, 12, 1165-1180. https://doi.org/10.5194/cp-12-1165-2016

#### Modo `rag` (DeepSeek, ~6702 tok, 3.9 s, DOI: 3/3)

¡Buena pregunta, che! Es una de esas palabras que todos usamos y que, según quién la escriba, cambia de significado. Te cuento cómo aparece en los estudios.

En la Puna argentina, "vega" es el término de campo para los humedales altoandinos, y muchas veces incluye vegas con turba, no solo praderas húmedas sin turba (Yager et al., 2021). En cambio, en los Andes Centrales hay una propuesta de distinguir "vega" o "ciénaga" (praderas húmedas sin turba, de 3000-4000 m, menor valor forrajero y a menudo sin manejo) del bofedal (3500-5000 m, manejado y con turba) (Yager et al., 2021). Otra línea, en Perú, propone usar "bofedal" como término amplio para cualquier humedal de alta montaña de la puna, sin importar la vegetación ni el suelo, y después precisar si es turbera o pradera húmeda (Chimner et al., 2019). Ojo: esa distinción vega/bofedal viene de Bolivia y Perú, y choca con el uso argentino (Yager et al., 2021).

Para nuestra Puna, la única clasificación propia del conjunto es la de 47 vegas ordenadas por altitud, clima, tamaño y productividad, con vegas altas de *Oxychloe andina* y vegas bajas salinas (Izquierdo et al., 2020).

Fuentes:
Yager, K., Prieto, M., & Meneses, R. I. (2021). Reframing pastoral practices of bofedal management to increase the resilience of Andean water towers. Mountain Research and Development, 41(4), A1-A9. https://doi.org/10.1659/MRD-JOURNAL-D-21-00011.1
Chimner, R. A., Bourgeau-Chavez, L., Grelik, S., Hribljan, J. A., Planas Clarke, A. M., Polk, M. H., Lilleskov, E. A., & Fuentealba, B. (2019). Mapping mountain peatlands and wet meadows using multi-date, multi-sensor remote sensing in the Cordillera Blanca, Peru. Wetlands. https://doi.org/10.1007/s13157-019-01134-1
Izquierdo, A. E., Carilla, J., Nieto, C., Osinaga Acosta, O., Martin, E., Grau, H. R., & Reynaga, M. C. (2020). Multi-taxon patterns from high Andean peatlands: Assessing climatic and landscape variables. Community Ecology. https://doi.org/10.1007/s42974-020-00029-0

---

### 2. Puna argentina vs. otros países
**Pregunta:** ¿Qué diferencias hay entre los estudios sobre vegas en la Puna argentina y los de Bolivia, Perú o Chile?

#### Modo `completo` (DeepSeek, ~194999 tok, 4.9 s, DOI: 5/5)

¡Buena pregunta! La diferencia más grande es de cantidad y de enfoque. Argentina es el país menos estudiado: de 119 publicaciones sobre bofedales, solo 9 incluyen sitios argentinos, frente a 49 de Bolivia, 41 de Perú y 31 de Chile (White-Nockleby et al., 2021). Además, los estudios argentinos son mayormente regionales y satelitales —inventarios de vegas, NDVI, paleoclima de un solo sitio—, mientras que en Bolivia, Perú y Chile abundan los estudios de sitio con mediciones de suelo, napa, carbono y gases (Izquierdo et al., 2020) (Navarro et al., 2020) (Cooper et al., 2019).

Otra diferencia es la terminología: en la Puna argentina "vega" designa también humedales con turba, mientras que una propuesta para los Andes Centrales reserva "vega" para praderas húmedas sin turba y "bofedal" para las turberas de cojín (Yager et al., 2021). Y hay un vacío propio: no hay en la bibliografía estudios argentinos de exclusión del ganado, capacidad de carga, riego pastoril ni mediciones de flujo de agua subterránea o de gases en campo (White-Nockleby et al., 2021) (Navarro et al., 2020).

Fuentes:
White-Nockleby, C., Prieto, M., Yager, K., & Meneses, R. I. (2021). Understanding bofedales as cultural landscapes in the Central Andes. Wetlands, 41, 102. https://doi.org/10.1007/s13157-021-01500-y
Izquierdo, A. E., Carilla, J., Nieto, C., Osinaga Acosta, O., Martin, E., Grau, H. R., & Reynaga, M. C. (2020). Multi-taxon patterns from high Andean peatlands: Assessing climatic and landscape variables. Community Ecology. https://doi.org/10.1007/s42974-020-00029-0
Navarro, C. J., Izquierdo, A. E., Aráoz, E., Foguet, J., & Grau, H. R. (2020). Rewilding of large herbivore communities in high elevation Puna: Geographic segregation and no evidence of positive effects on peatland productivity. Regional Environmental Change, 20, 112. https://doi.org/10.1007/s10113-020-01704-8
Cooper, D. J., Sueltenfuss, J., Oyague, E., Yager, K., Slayback, D., Cabero Caballero, E. M., Argollo, J., & Mark, B. G. (2019). Drivers of peatland water table dynamics in the central Andes, Bolivia and Peru. Hydrological Processes, 33, 1913-1925. https://doi.org/10.1002/hyp.13446
Yager, K., Prieto, M., & Meneses, R. I. (2021). Reframing pastoral practices of bofedal management to increase the resilience of Andean water towers. Mountain Research and Development, 41(4), A1-A9. https://doi.org/10.1659/MRD-JOURNAL-D-21-00011.1

#### Modo `rag` (DeepSeek, ~6527 tok, 3.1 s, DOI: 2/2)

¡Qué buena pregunta! Y te cuento que hay una diferencia bien marcada en cuánto se estudia cada lugar. De las 119 publicaciones revisadas entre 1977 y 2018, 49 incluyen sitios en Bolivia, 41 en Perú y 31 en Chile, pero solo 9 en Argentina (White-Nockleby et al., 2021). Además, los términos quechuas y aimaras para nombrar estos humedales (oqho, waylla, juqhu y otros) aparecen solo en estudios de Bolivia y Perú, ninguno de Argentina ni de Chile (White-Nockleby et al., 2021).

También hay una diferencia de enfoque: la mitad de los trabajos de ciencias sociales y multidisciplinarios menciona prácticas de manejo comunitario, frente a solo un cuarto de los de ciencias naturales, donde muchas veces la relación se ve como unidireccional (las comunidades se benefician pero no modifican el humedal) (White-Nockleby et al., 2021). Y en cuanto a la terminología, en Argentina las turberas de juncáceas se llaman "vegas altoandinas", mientras que en Bolivia se habla de "bofedal" (White-Nockleby et al., 2021; Ruthsatz, 2012).

Ojo con un dato que viene de Bolivia: la riqueza de especies de los bofedales disminuye desde Bolivia hacia el noroeste argentino y el norte de Chile por el aumento de la aridez y el enriquecimiento salino de origen volcánico (Ruthsatz, 2012). Es evidencia boliviana comparada con relevamientos del NOA, así que tomala como tendencia regional.

Fuentes:
White-Nockleby, C., Prieto, M., Yager, K., & Meneses, R. I. (2021). Understanding bofedales as cultural landscapes in the Central Andes. Wetlands, 41, 102. https://doi.org/10.1007/s13157-021-01500-y
Ruthsatz, B. (2012). Vegetación y ecología de los bofedales altoandinos de Bolivia (C. Pérez, Trad.). Phytocoenologia, 42(3-4), 133-179. https://doi.org/10.1127/0340-269X/2012/0042-0535

---

### 3. Cifras concretas
**Pregunta:** ¿Cuántas vegas y qué superficie total se registraron en la Puna argentina según la bibliografía?

#### Modo `completo` (DeepSeek, ~194997 tok, 3.1 s, DOI: 3/3)

¡Hola! Según los estudios que conozco, en la Puna argentina se registraron **8134 vegas** que suman unas **110.900 ha**, apenas el 0,78 % de la superficie de la Puna (Navarro et al., 2020) (Izquierdo et al., 2020). La mayoría son chicas: el 58 % mide menos de 5 ha, y todas esas juntas ocupan solo el 12 % de la superficie total de vegas (Navarro et al., 2020).

Un detalle: hay un trabajo que cita 895 ha, pero muy probablemente es una errata por 110.895 ha; la referencia que se usa es ~110.900 ha (Casagranda et al., 2019).

Fuentes:
Navarro, C. J., Izquierdo, A. E., Aráoz, E., Foguet, J., & Grau, H. R. (2020). Rewilding of large herbivore communities in high elevation Puna: Geographic segregation and no evidence of positive effects on peatland productivity. Regional Environmental Change, 20, 112. https://doi.org/10.1007/s10113-020-01704-8
Izquierdo, A. E., Carilla, J., Nieto, C., Osinaga Acosta, O., Martin, E., Grau, H. R., & Reynaga, M. C. (2020). Multi-taxon patterns from high Andean peatlands: Assessing climatic and landscape variables. Community Ecology. https://doi.org/10.1007/s42974-020-00029-0
Casagranda, E., Navarro, C., Grau, H. R., & Izquierdo, A. E. (2019). Interannual lake fluctuations in the Argentine Puna: Relationships with its associated peatlands and climate change. Regional Environmental Change, 19, 1737-1750. https://doi.org/10.1007/s10113-019-01514-7

#### Modo `rag` (DeepSeek, ~6560 tok, 2.0 s, DOI: 2/2)

¡Hola! Según el mapa regional, la Puna argentina tiene 8134 vegas que suman unas 110.900 ha, lo que representa apenas el 0,78 % de su superficie (Navarro et al., 2020) (Izquierdo et al., 2020). Predominan las pequeñas: el 58 % mide menos de 5 ha, aunque en conjunto solo aporta el 12 % del área total (Navarro et al., 2020).

Fuentes:
Navarro, C. J., Izquierdo, A. E., Aráoz, E., Foguet, J., & Grau, H. R. (2020). Rewilding of large herbivore communities in high elevation Puna: Geographic segregation and no evidence of positive effects on peatland productivity. Regional Environmental Change, 20, 112. https://doi.org/10.1007/s10113-020-01704-8
Izquierdo, A. E., Carilla, J., Nieto, C., Osinaga Acosta, O., Martin, E., Grau, H. R., & Reynaga, M. C. (2020). Multi-taxon patterns from high Andean peatlands: Assessing climatic and landscape variables. Community Ecology. https://doi.org/10.1007/s42974-020-00029-0

---

### 4. Pastoreo
**Pregunta:** ¿Cómo afecta el pastoreo de camélidos y ganado a las vegas y bofedales?

#### Modo `completo` (DeepSeek, ~194991 tok, 4.5 s, DOI: 4/4)

¡Qué buena pregunta! Es de las más discutidas en los estudios, y no hay una sola respuesta.

En la Cordillera Real de Bolivia, todos los bofedales con datos de carga estaban sobrepastoreados (cocientes entre capacidad de carga y carga animal de 0,02 a 0,94), y con más presión los cojines de *Oxychloe* y *Distichia* eran reemplazados por *Festuca dolichophylla* y *Plantago tubulosa*, con menos agua superficial (Cochi Machaca et al., 2018). En cambio, en Tarija se considera engañoso el término "sobrepastoreo", porque la biomasa depende más de la lluvia y la salinidad, y el número de animales cambió poco en 50 años (Preston et al., 2003). Y en la Puna argentina, a escala regional, la cercanía al ganado explicó menos del 1 % de la variación del verdor de 8134 vegas, sin señales de degradación (Navarro et al., 2020).

Ojo: los umbrales de cojín y de turba expuesta que indican pérdida de carbono vienen de Colombia, un páramo mucho más húmedo que la Puna (Martínez-Amigo y Benavides, 2023). En Argentina no hay estudios de exclusión del ganado ni de capacidad de carga en vegas.

Fuentes:
Cochi Machaca, N., Condori, B., Rojas Pardo, A., Anthelme, F., Meneses, R. I., Weeda, C. E., & Perotto-Baldivieso, H. L. (2018). Effects of grazing pressure on plant species composition and water presence on bofedales in the Andes mountain range of Bolivia. Mires and Peat, 21, Article 15, 1-15. https://doi.org/10.19189/MaP.2017.OMB.303
Preston, D., Fairbairn, J., Paniagua, N., Maas, G., Yevara, M., & Beck, S. (2003). Grazing and environmental change on the Tarija altiplano, Bolivia. Mountain Research and Development, 23(2), 141-148. https://doi.org/10.1659/0276-4741(2003)023[0141:GAECOT]2.0.CO;2
Navarro, C. J., Izquierdo, A. E., Aráoz, E., Foguet, J., & Grau, H. R. (2020). Rewilding of large herbivore communities in high elevation Puna: Geographic segregation and no evidence of positive effects on peatland productivity. Regional Environmental Change, 20, 112. https://doi.org/10.1007/s10113-020-01704-8
Martínez-Amigo, V., & Benavides, J. C. (2023). Carbon balance shift in mountain peatlands along a gradient of grazing disturbance in the tropical Andes (Colombia). Plant Ecology, 224, 1049-1058. https://doi.org/10.1007/s11258-023-01356-8

#### Modo `rag` (DeepSeek, ~6718 tok, 5.4 s, DOI: 6/6)

¡Hola! Es una de las preguntas más discutidas en la bibliografía, y la respuesta corta es: depende de dónde mires y con qué vara midas. Te cuento lo que muestran los estudios.

- **No hay acuerdo sobre el "sobrepastoreo".** Algunos trabajos lo diagnostican con cálculos de capacidad de carga (Cochi Machaca et al., 2018; Carevic et al., 2019), mientras que otros consideran el término engañoso: en Tarija (Bolivia) el clima y la salinidad explican más las diferencias de biomasa que el ganado (Preston et al., 2003), y en 8134 vegas de la Puna argentina no se detectó efecto del ganado sobre el NDVI (Navarro et al., 2020). Ojo: casi toda la evidencia sobre carga animal, riego y degradación viene de Bolivia, Chile y Perú; aplicarla a la Puna argentina es una inferencia (Síntesis — Pastoreo).
- **Efectos locales cerca de los asentamientos.** El pisoteo y el pastoreo selectivo reemplazan gramíneas palatables (Poa, Agrostis, Deyeuxia, Festuca) por especies menos palatables como Stipa leptostachya o Festuca orthophylla (Preston et al., 2003). En Lauca (Chile), el pastoreo doméstico reduce gramíneas y juncos palatables, mientras que las vicuñas consumen cojines y mantienen la riqueza (Rundel y Palma, 2000).
- **El manejo hace la diferencia.** La trashumancia, el pastoreo al partir y las rotaciones reparten la carga y favorecen la recuperación de las pasturas (Preston et al., 2003). En Sajama los pastores llevan los animales al pajonal de mañana y al bofedal de tarde para evitar el sobrepastoreo del bofedal (Perreault, 2025), aunque los cercos generalizados pueden concentrar animales y el parque les atribuye la caída de vicuñas de ~5000 a ~1525 entre 2010 y 2023 (Perreault, 2025).
- **Segregación espacial.** En la Puna argentina el ganado se concentra en vegas cercanas a los asentamientos y las vicuñas en las remotas (Navarro et al., 2020).

Fuentes:
Cochi Machaca, N., Condori, B., Rojas Pardo, A., Anthelme, F., Meneses, R. I., Weeda, C. E., & Perotto-Baldivieso, H. L. (2018). Effects of grazing pressure on plant species composition and water presence on bofedales in the Andes mountain range of Bolivia. Mires and Peat, 21, Article 15, 1-15. https://doi.org/10.19189/MaP.2017.OMB.303
Carevic, F. S., Anderson, M., & Muñoz, A. (2019). Is the temporary grazing exclusion a good management alternative for arid peatlands? Arid Land Research and Management. https://doi.org/10.1080/15324982.2018.1563242
Preston, D., Fairbairn, J., Paniagua, N., Maas, G., Yevara, M., & Beck, S. (2003). Grazing and environmental change on the Tarija altiplano, Bolivia. Mountain Research and Development, 23(2), 141-148. https://doi.org/10.1659/0276-4741(2003)023[0141:GAECOT]2.0.CO;2
Navarro, C. J., Izquierdo, A. E., Aráoz, E., Foguet, J., & Grau, H. R. (2020). Rewilding of large herbivore communities in high elevation Puna: Geographic segregation and no evidence of positive effects on peatland productivity. Regional Environmental Change, 20, 112. https://doi.org/10.1007/s10113-020-01704-8
Rundel, P. W., & Palma, B. (2000). Preserving the unique puna ecosystems of the Andean Altiplano: A descriptive account of Lauca National Park, Chile. Mountain Research and Development, 20(3), 262-271. https://doi.org/10.1659/0276-4741(2000)020[0262:PTUPEO]2.0.CO;2
Perreault, T. (2025). Adaptive livelihoods in Andean pastoralism: Community-based institutions, peatland management, and migration in Sajama National Park, Bolivia. Mountain Research and Development, 45(2), R1-R8. https://doi.org/10.1659/mrd.2024.00030

---

### 5. Agua / Hidrología
**Pregunta:** ¿De dónde proviene el agua que mantiene a las vegas y bofedales?

#### Modo `completo` (DeepSeek, ~194989 tok, 4.9 s, DOI: 3/3)

¡Qué buena pregunta! Es de las más importantes, porque de eso depende todo lo demás. En diez turberas de Bolivia y Perú el agua que mantiene la napa llega desde acuíferos de ladera —morenas, taludes, coluvio o roca— recargados por lluvia y nieve, y no de arroyos ni del deshielo glaciar, algo que confirman los isótopos (Cooper et al., 2019). En temporada de lluvias la napa se mantiene a menos de 20 cm de la superficie y en la seca baja a 40-90 cm en muchos sitios (Cooper et al., 2019).

En la Puna argentina, la turbera de Cerro Tuzgle se recarga con lluvia reciente y agua subterránea somera, sin aporte geotermal (Kock et al., 2019). Y ojo, que hay un debate: otros trabajos vinculan la expansión de humedales al deshielo glaciar (Polk et al., 2017), mientras que Cooper et al. (2019) no encontraron aporte glaciar en sus turberas.

Fuentes:
Cooper, D. J., Sueltenfuss, J., Oyague, E., Yager, K., Slayback, D., Cabero Caballero, E. M., Argollo, J., & Mark, B. G. (2019). Drivers of peatland water table dynamics in the central Andes, Bolivia and Peru. Hydrological Processes, 33, 1913-1925. https://doi.org/10.1002/hyp.13446
Kock, S. T., Schittek, K., Wissel, H., Vos, H., Ohlendorf, C., Schäbitz, F., Lupo, L. C., Kulemeyer, J. J., & Lücke, A. (2019). Stable oxygen isotope records (δ18O) of a high-Andean cushion peatland in NW Argentina (24°S) imply South American Summer Monsoon related moisture changes during the Late Holocene. Frontiers in Earth Science, 7, 45. https://doi.org/10.3389/feart.2019.00045
Polk, M. H., Young, K. R., Baraer, M., Mark, B. G., McKenzie, J. M., Bury, J., & Carey, M. (2017). Exploring hydrologic connections between tropical mountain wetlands and glacier recession in Peru's Cordillera Blanca. Applied Geography, 78, 94-103. https://doi.org/10.1016/j.apgeog.2016.11.004

#### Modo `rag` (DeepSeek, ~6737 tok, 3.9 s, DOI: 5/5)

¡Qué linda pregunta, che! Es de las más importantes para entender estos humedales.

En diez turberas de Bolivia y Perú, el agua que mantiene la napa llega desde acuíferos de ladera (morenas, talud, coluvio o roca) recargados por lluvia y nieve, sin aporte de arroyos ni de deshielo glaciar, algo que confirman los isótopos (Cooper et al., 2019). Los bofedales de Bolivia y el sur de Perú son turberas minerotróficas alimentadas por vertientes y arroyos (Ruthsatz, 2012), y en Cajamarca (Perú) ninguna turbera muestreada era ombrotrófica (Cooper et al., 2010).

En ambientes más secos la recarga parece ser reciente: en Cerro Tuzgle (Jujuy, 4350 m) y en Lagunillas (Atacama, Chile), las aguas de pozas y manantiales siguen una línea de evaporación local que apunta a lluvia reciente y agua subterránea somera, sin aguas antiguas ni geotermales (Kock et al., 2019). Ojo que casi toda esta evidencia viene de Bolivia, Perú y Chile; para las vegas de la Puna argentina todavía faltan balances hídricos y pozos freáticos propios (Valois et al., 2020).

Fuentes:
Cooper, D. J., Sueltenfuss, J., Oyague, E., Yager, K., Slayback, D., Cabero Caballero, E. M., Argollo, J., & Mark, B. G. (2019). Drivers of peatland water table dynamics in the central Andes, Bolivia and Peru. Hydrological Processes, 33, 1913-1925. https://doi.org/10.1002/hyp.13446
Ruthsatz, B. (2012). Vegetación y ecología de los bofedales altoandinos de Bolivia (C. Pérez, Trad.). Phytocoenologia, 42(3-4), 133-179. https://doi.org/10.1127/0340-269X/2012/0042-0535
Cooper, D. J., Wolf, E. C., Colson, C., Vering, W., Granda, A., & Meyer, M. (2010). Alpine peatlands of the Andes, Cajamarca, Peru. Arctic, Antarctic, and Alpine Research, 42(1), 19-33. https://doi.org/10.1657/1938-4246-42.1.19
Kock, S. T., Schittek, K., Wissel, H., Vos, H., Ohlendorf, C., Schäbitz, F., Lupo, L. C., Kulemeyer, J. J., & Lücke, A. (2019). Stable oxygen isotope records (δ18O) of a high-Andean cushion peatland in NW Argentina (24°S) imply South American Summer Monsoon related moisture changes during the Late Holocene. Frontiers in Earth Science, 7, 45. https://doi.org/10.3389/feart.2019.00045
Valois, R., Schaffer, N., Figueroa, R., Maldonado, A., Yáñez, E., Hevia, A., Yánez Carrizo, G., & MacDonell, S. (2020). Characterizing the water storage capacity and hydrological role of mountain peatlands in the arid Andes of North-Central Chile. Water, 12(4), 1071. https://doi.org/10.3390/w12041071

---

### 6. Carbono
**Pregunta:** ¿Cuánto carbono orgánico acumulan los suelos de turberas y bofedales andinos?

#### Modo `completo` (DeepSeek, ~194993 tok, 5.4 s, DOI: 5/5)

¡Qué buena pregunta! Te cuento lo que muestran los estudios, con la aclaración de que casi todos los datos vienen de Perú, Bolivia, Ecuador y Colombia, y muy poco de la Puna argentina.

- En bofedales de Puno (Perú), los primeros 30 cm guardaron entre 23 y 30,6 kg C/m² según el régimen de inundación (Segnini et al., 2010), y en Junín (Perú) unos 210,9 t C/ha, casi el doble que los pastizales y cultivos vecinos (Carbajal et al., 2024).
- Midiendo toda la columna de turba, nueve turberas del páramo ecuatoriano promediaron 1282 Mg C/ha, con casi la mitad del carbono en capas minerales intercaladas (Hribljan et al., 2016).
- En la Puna argentina, diez vegas (3323–4748 m) almacenaron en promedio 66,11 Mg C/ha en los primeros 30 cm, más del 70 % del carbono del sistema planta-suelo (Chiappero et al., 2026). Y en dos turberas de Catamarca junto a un salar, una guardó cuatro veces más que la otra: 281,8 frente a 71,5 Mg C/ha (Chiappero et al., 2021).

Ojo con las cifras: dependen de cuánta profundidad se mida y de si se cuentan las capas minerales, así que no son directamente comparables entre estudios.

Fuentes:
Segnini, A., Posadas, A., Quiroz, R., Milori, D. M. B. P., Saab, S. C., Martin Neto, L., & Vaz, C. M. P. (2010). Spectroscopic assessment of soil organic matter in wetlands from the High Andes. Soil Science Society of America Journal, 74(6), 2246-2253. https://doi.org/10.2136/sssaj2009.0445
Carbajal, M., Ramírez, D. A., Turin, C., Schaeffer, S. M., Konkel, J., Ninanya, J., Rinza, J., De Mendiburu, F., Zorogastua, P., Villaorduña, L., & Quiroz, R. (2024). From rangelands to cropland, land-use change and its impact on soil organic carbon variables in a Peruvian Andean highlands: A machine learning modeling approach. Ecosystems, 27, 899-917. https://doi.org/10.1007/s10021-024-00928-7
Hribljan, J. A., Suárez, E., Heckman, K. A., Lilleskov, E. A., & Chimner, R. A. (2016). Peatland carbon stocks and accumulation rates in the Ecuadorian páramo. Wetlands Ecology and Management. https://doi.org/10.1007/s11273-016-9482-2
Chiappero, M. F., Vaieretti, M. V., Gallardo, N., & Izquierdo, A. E. (2026). Carbon storage patterns in high Andean wetlands: local factors explain the variability of soil carbon stocks in the Argentine Puna. Plant and Soil, 525, 1393–1408. https://doi.org/10.1007/s11104-026-08829-5
Chiappero, M. F., Vaieretti, M. V., & Izquierdo, A. E. (2021). A baseline soil survey of two peatlands associated with a lithium-rich salt flat in the Argentine Puna: physico-chemical characteristics, carbon storage and biota. Mires and Peat, 27, Article 16, 1–13. https://doi.org/10.19189/MaP.2020.OMB.StA.2126

#### Modo `rag` (DeepSeek, ~6278 tok, 3.6 s, DOI: 3/3)

¡Qué lindo tema para arrancar! Te cuento lo que dicen los estudios que tengo a mano.

Los bofedales y turberas altoandinas son los suelos con más carbono orgánico de los Andes. En bofedales de Bolivia se registraron las concentraciones más altas, cerca de 500 g/kg en superficie, mientras que las turberas de Ecuador mostraron las más bajas, alrededor de 132 g/kg (Alavi-Murillo et al., 2022). En bofedales de Puno (Perú, 3881 m) la concentración en los primeros 30 cm varió entre 121,7 y 215,6 g C kg-1, con stocks de 30,62 kg C m-2 en un bofedal estacional y 23,03 kg C m-2 en uno anegado todo el año (Segnini et al., 2010). Midiendo toda la columna de turba, nueve turberas del páramo ecuatoriano promediaron 3,8 m de espesor y 1282 Mg C ha-1, con un rango de 245 a 2025 Mg C ha-1 (Hribljan et al., 2016).

Ojo con un detalle: hay un trabajo que encontró más carbono por área en el bofedal estacional que en el permanente (Segnini et al., 2010), mientras que una revisión regional indica lo contrario, que los permanentes acumulan más (Alavi-Murillo et al., 2022). Y para la Puna argentina casi no hay datos: solo 14 de 334 muestras de esa revisión andina correspondían a turberas, y el sur de los Andes está subrepresentado (Alavi-Murillo et al., 2022).

Fuentes:
Alavi-Murillo, G., Diels, J., Gilles, J., & Willems, P. (2022). Soil organic carbon in Andean high-mountain ecosystems: Importance, challenges, and opportunities for carbon sequestration. Regional Environmental Change, 22, 128. https://doi.org/10.1007/s10113-022-01980-6
Segnini, A., Posadas, A., Quiroz, R., Milori, D. M. B. P., Saab, S. C., Martin Neto, L., & Vaz, C. M. P. (2010). Spectroscopic assessment of soil organic matter in wetlands from the High Andes. Soil Science Society of America Journal, 74(6), 2246-2253. https://doi.org/10.2136/sssaj2009.0445
Hribljan, J. A., Suárez, E., Heckman, K. A., Lilleskov, E. A., & Chimner, R. A. (2016). Peatland carbon stocks and accumulation rates in the Ecuadorian páramo. Wetlands Ecology and Management. https://doi.org/10.1007/s11273-016-9482-2

---

### 7. Minería / Litio
**Pregunta:** ¿Qué impactos tiene la minería de litio y la extracción de agua sobre las vegas y bofedales?

#### Modo `completo` (DeepSeek, ~194996 tok, 7.0 s, DOI: 6/6)

¡Buena pregunta, che! Te cuento lo que dicen los estudios, pero ojo: casi todo lo que sabemos de impactos medidos viene de otros países, y en la Puna argentina lo que hay es una línea de base, no impactos documentados.

- **La amenaza está señalada, pero poco medida.** La minería de salmueras (litio, potasio, bórax) aparece como amenaza para los humedales cercanos a salares, junto con el bombeo de acuíferos, el entubado de cauces y los caminos que cortan el flujo de agua (Yager et al., 2021). Pero no hay estudios de campo sobre el impacto hidrológico de la minería de litio en vegas: la amenaza solo se menciona en ese ensayo regional (Yager et al., 2021).
- **El agua subterránea puede ser un recurso fósil.** En la cuenca del Lauca (Chile), gran parte del agua almacenada data de hace unos 13.000-12.000 años y la recarga actual es limitada, así que bombearla sería explotar un recurso no renovable (Rundel y Palma, 2000). Y en turberas de Bolivia y Perú, cuando la napa bajó más de 1 m durante meses, los cojines de *Distichia* y *Oxychloe* murieron (Cooper et al., 2015; Cooper et al., 2019).
- **El caso más drástico es cualitativo.** En Las Vegas de Chiu-Chiu (Chile), tras asignar 850 l/s del río Loa a la empresa sanitaria para el crecimiento urbano ligado al cobre, la vega se secó y el ganado pasó de unas 3000 a 50-100 cabezas, según los comuneros (Prieto, 2015).
- **En Argentina hay línea de base, no impactos.** En dos turberas de Catamarca asociadas a un salar con litio, Laguna Negra almacenó cuatro veces más carbono que Laguna Tres Quebradas (281,8 frente a 71,5 Mg ha⁻¹ en 0-30 cm) y esta última triplicó la abundancia y diversidad de mesofauna: cada humedal puede responder distinto ante el bombeo de salmueras (Chiappero et al., 2021).

Fuentes:
Yager, K., Prieto, M., & Meneses, R. I. (2021). Reframing pastoral practices of bofedal management to increase the resilience of Andean water towers. Mountain Research and Development, 41(4), A1-A9. https://doi.org/10.1659/MRD-JOURNAL-D-21-00011.1
Rundel, P. W., & Palma, B. (2000). Preserving the unique puna ecosystems of the Andean Altiplano: A descriptive account of Lauca National Park, Chile. Mountain Research and Development, 20(3), 262-271. https://doi.org/10.1659/0276-4741(2000)020[0262:PTUPEO]2.0.CO;2
Cooper, D. J., Kaczynski, K., Slayback, D., & Yager, K. (2015). Growth and organic carbon production in peatlands dominated by Distichia muscoides, Bolivia, South America. Arctic, Antarctic, and Alpine Research, 47(3), 505-510. https://doi.org/10.1657/AAAR0014-060
Cooper, D. J., Sueltenfuss, J., Oyague, E., Yager, K., Slayback, D., Cabero Caballero, E. M., Argollo, J., & Mark, B. G. (2019). Drivers of peatland water table dynamics in the central Andes, Bolivia and Peru. Hydrological Processes, 33, 1913-1925. https://doi.org/10.1002/hyp.13446
Prieto, M. (2015). Privatizing water in the Chilean Andes: The case of Las Vegas de Chiu-Chiu. Mountain Research and Development, 35(3), 220-229. https://doi.org/10.1659/MRD-JOURNAL-D-14-00033.1
Chiappero, M. F., Vaieretti, M. V., & Izquierdo, A. E. (2021). A baseline soil survey of two peatlands associated with a lithium-rich salt flat in the Argentine Puna: physico-chemical characteristics, carbon storage and biota. Mires and Peat, 27, Article 16, 1–13. https://doi.org/10.19189/MaP.2020.OMB.StA.2126

#### Modo `rag` (DeepSeek, ~6710 tok, 4.7 s, DOI: 4/4)

¡Buena pregunta, che! Te cuento lo que dicen los estudios que tengo a mano.

La minería afecta a los bofedales por bombeo de agua subterránea, entubado de cauces y caminos que cortan el flujo; la mina Chuquicamata destruyó varios bofedales de la cuenca del San Pedro de Inacaliri, y la minería de salmueras (litio, potasio, bórax) amenaza a los humedales cercanos a salares (Yager et al., 2021). Ojo que esa amenaza de salmueras aparece señalada en un ensayo regional, no en estudios de campo: no hay en los insumos estudios que midan el impacto hidrológico de la minería de litio sobre vegas (Yager et al., 2021).

Para la Puna argentina sí existe una línea de base previa a la explotación de litio en dos turberas de Catamarca (4100 m) asociadas al mismo salar: Laguna Negra almacenó cuatro veces más carbono orgánico que Laguna Tres Quebradas (281,8 frente a 71,5 Mg ha-1 en 0–30 cm) y fue más salina, mientras esta última triplicó la abundancia y diversidad de mesofauna, lo que muestra que cada humedal puede responder distinto ante el bombeo de salmueras (Chiappero et al., 2021).

Sobre la extracción de agua en general, la evidencia cuantitativa es escasa y a veces contraintuitiva. En el bofedal de Chucuyo (Chile), el caudal extraído por el canal Lauca no se correlacionó con el NDVI ni con la superficie, mientras que la precipitación sí lo hizo; los autores concluyen que el canal probablemente redujo el agua del sector, pero que el daño no puede cuantificarse sin imágenes anteriores a su construcción (Uribe-Álvarez et al., 2022). Y en Las Vegas de Chiu-Chiu, tras asignarse 850 l/s del río Loa a la empresa sanitaria, la vega se secó y el ganado pasó de unas 3000 a 50-100 cabezas, según los comuneros (Prieto, 2015).

Fuentes:
Yager, K., Prieto, M., & Meneses, R. I. (2021). Reframing pastoral practices of bofedal management to increase the resilience of Andean water towers. Mountain Research and Development, 41(4), A1-A9. https://doi.org/10.1659/MRD-JOURNAL-D-21-00011.1
Chiappero, M. F., Vaieretti, M. V., & Izquierdo, A. E. (2021). A baseline soil survey of two peatlands associated with a lithium-rich salt flat in the Argentine Puna: physico-chemical characteristics, carbon storage and biota. Mires and Peat, 27, Article 16, 1–13. https://doi.org/10.19189/MaP.2020.OMB.StA.2126
Uribe-Álvarez, M. C., Prieto, M., & Meseguer-Ruiz, O. (2022). Bofedal response to climate variability, local management, and water extraction: A case study of Chucuyo, Northern Chile. Journal of Mountain Science, 19(1), 241-252. https://doi.org/10.1007/s11629-021-6974-1
Prieto, M. (2015). Privatizing water in the Chilean Andes: The case of Las Vegas de Chiu-Chiu. Mountain Research and Development, 35(3), 220-229. https://doi.org/10.1659/MRD-JOURNAL-D-14-00033.1

---

### 8. Teledetección / Mapeo
**Pregunta:** ¿Qué sensores satelitales e índices se usan para mapear y monitorear vegas altoandinas?

#### Modo `completo` (DeepSeek, ~194995 tok, 6.6 s, DOI: 8/8)

¡Buena pregunta! Te cuento lo que muestran los estudios que conozco.

Los sensores más usados son **Landsat** (con índices de vegetación como el NDVI) y, para separar tipos de humedal, se suma **radar** y topografía. En el Altiplano chileno un umbral de NDVI de 0,23 bastó para delimitar 5665 bofedales que suman 510,27 km² (Chávez et al., 2019), y en el sur de Perú se usaron umbrales de NDVI de estación seca con exactitudes del 90 al 94 % (Otto et al., 2011) (Otto y Gibbons, 2017). Combinar óptico, radar en bandas L y C e índices topográficos con Random Forests separó turberas de praderas húmedas con 92 % de exactitud en Huascarán (Chimner et al., 2019) y 97,1 % en la jalca de Amazonas (Curatola Fernández et al., 2023).

Para humedad del suelo, **Sentinel-2** delimitó vegas con 94 % de exactitud en marzo y estimó la humedad mejor que WorldView-2 (r² 0,58 frente a 0,34), gracias a sus bandas de infrarrojo de onda corta (Araya-López et al., 2018). Para series largas, **MODIS** sirve para monitorear productividad, aunque subestima los humedales perennes y sobrestima los temporales (Otto et al., 2011). Ojo: un mayor verdor no siempre equivale a más vega de turba, porque el aumento puede ser de pastizal húmedo temporal (Dangles et al., 2017).

En la Puna argentina ya hay un mapa de 8134 vegas hecho con NDVI de MODIS (Navarro et al., 2020), pero no hay estudios de radar ni Sentinel-2 en la región dentro de esta bibliografía.

Fuentes:
Chávez, R. O., Christie, D. A., Olea, M., & Anderson, T. G. (2019). A multiscale productivity assessment of high Andean peatlands across the Chilean Altiplano using 31 years of Landsat imagery. Remote Sensing, 11(24), 2955. https://doi.org/10.3390/rs11242955
Otto, M., Scherer, D., & Richters, J. (2011). Hydrological differentiation and spatial distribution of high altitude wetlands in a semi-arid Andean region derived from satellite data. Hydrology and Earth System Sciences, 15, 1713-1727. https://doi.org/10.5194/hess-15-1713-2011
Otto, M., & Gibbons, R. E. (2017). Potential effects of projected decrease in annual rainfall on spatial distribution of high Andean wetlands in southern Peru. Wetlands. https://doi.org/10.1007/s13157-017-0896-2
Chimner, R. A., Bourgeau-Chavez, L., Grelik, S., Hribljan, J. A., Planas Clarke, A. M., Polk, M. H., Lilleskov, E. A., & Fuentealba, B. (2019). Mapping mountain peatlands and wet meadows using multi-date, multi-sensor remote sensing in the Cordillera Blanca, Peru. Wetlands. https://doi.org/10.1007/s13157-019-01134-1
Curatola Fernández, G. F., Makowski Giannoni, S., Delgado Florián, E., Rengifo, P., Rascón, J., Chichipe Vela, E., Butrich, C., Salas López, R., Oliva-Cruz, M., & Scheske, C. (2023). Mapping high-altitude peatlands to inform a landscape conservation strategy in the Andes of northern Peru. Environmental Conservation, 50, 212-219. https://doi.org/10.1017/S0376892923000267
Araya-López, R. A., Lopatin, J., Fassnacht, F. E., & Hernández, H. J. (2018). Monitoring Andean high altitude wetlands in central Chile with seasonal optical data: A comparison between Worldview-2 and Sentinel-2 imagery. ISPRS Journal of Photogrammetry and Remote Sensing. https://doi.org/10.1016/j.isprsjprs.2018.04.001
Dangles, O., Rabatel, A., Kraemer, M., Zeballos, G., Soruco, A., Jacobsen, D., & Anthelme, F. (2017). Ecosystem sentinels for climate change? Evidence of wetland cover changes over the last 30 years in the tropical Andes. PLoS ONE, 12(5), e0175814. https://doi.org/10.1371/journal.pone.0175814
Navarro, C. J., Izquierdo, A. E., Aráoz, E., Foguet, J., & Grau, H. R. (2020). Rewilding of large herbivore communities in high elevation Puna: Geographic segregation and no evidence of positive effects on peatland productivity. Regional Environmental Change, 20, 112. https://doi.org/10.1007/s10113-020-01704-8

#### Modo `rag` (DeepSeek, ~6303 tok, 6.2 s, DOI: 9/10)

¡Hola! Qué lindo poder contarte esto, porque hay bastante trabajo sobre el tema. Te resumo lo que muestran los estudios que conozco.

- **Landsat con índices de vegetación** es lo más usado para delimitar y seguir vegas y bofedales en el tiempo (Síntesis — Teledetección y mapeo). El **NDVI** es el índice estrella: en la estación seca casi solo la vegetación con agua permanente sigue verde, y eso permite separar los humedales. Los umbrales varían según el sitio: 0,23 en el Altiplano chileno (Chávez et al., 2019), 0,3 en Nuñoa, Perú (Mazzarino y Finn, 2016) y 0,468 en la Cordillera Real de Bolivia (Dangles et al., 2017).
- Sumar un **índice de agua (NDII, umbral 0,45)** al NDVI ayuda a distinguir sectores inundados y humedales perennes de los temporales (Otto et al., 2011).
- Para separar tipos de humedal (turberas de praderas húmedas) resultó útil combinar **radar en bandas L y C** e índices topográficos con Landsat y Random Forests: 92 % de exactitud en Huascarán (Chimner et al., 2019) y 97,1 % en la jalca de Amazonas (Curatola Fernández et al., 2023).
- **Sentinel-2** delimitó vegas en Chile central con 94 % de exactitud en marzo y estimó la humedad del suelo mejor que WorldView-2 (r² 0,58 frente a 0,34), gracias a sus bandas de infrarrojo de onda corta (Araya-López et al., 2018).
- El **radar en banda C del ERS** atraviesa la nubosidad y estimó biomasa seca de bofedales bolivianos con error de 0,3 kg/m², aunque se satura sobre 2,0 kg/m² (Moreau y Le Toan, 2003).

Un detalle importante: **MODIS (250 m)** solo recoge unos dos tercios de lo detectado con Landsat y sobrestima los humedales temporales (Otto et al., 2011). Y ojo, que el verdor no siempre alcanza: cerca de un cuarto de los humedales con plantas en cojín de Huascarán no eran turberas, así que el NDVI no basta para detectar turba (Chimner et al., 2019). En la Puna argentina, el mapa de 8134 vegas se hizo con NDVI de MODIS (Navarro et al., 2020), y en Pozuelos, Jujuy, NDVI, SAVI y MSAVI2 se ajustaron a la cobertura pero no a la biomasa (Rojo et al., 2019).

Fuentes:
Araya-López, R. A., Lopatin, J., Fassnacht, F. E., & Hernández, H. J. (2018). Monitoring Andean high altitude wetlands in central Chile with seasonal optical data: A comparison between Worldview-2 and Sentinel-2 imagery. ISPRS Journal of Photogrammetry and Remote Sensing. https://doi.org/10.1016/j.isprsjprs.2018.04.001
Chávez, R. O., Christie, D. A., Olea, M., & Anderson, T. G. (2019). A multiscale productivity assessment of high Andean peatlands across the Chilean Altiplano using 31 years of Landsat imagery. Remote Sensing, 11(24), 2955. https://doi.org/10.3390/rs11242955
Chimner, R. A., Bourgeau-Chavez, L., Grelik, S., Hribljan, J. A., Planas Clarke, A. M., Polk, M. H., Lilleskov, E. A., & Fuentealba, B. (2019). Mapping mountain peatlands and wet meadows using multi-date, multi-sensor remote sensing in the Cordillera Blanca, Peru. Wetlands. https://doi.org/10.1007/s13157-019-01134-1
Curatola Fernández, G. F., Makowski Giannoni, S., Delgado Florián, E., Rengifo, P., Rascón, J., Chichipe Vela, E., Butrich, C., Salas López, R., Oliva-Cruz, M., & Scheske, C. (2023). Mapping high-altitude peatlands to inform a landscape conservation strategy in the Andes of northern Peru. Environmental Conservation, 50, 212-219. https://doi.org/10.1017/S0376892923000267
Dangles, O., Rabatel, A., Kraemer, M., Zeballos, G., Soruco, A., Jacobsen, D., & Anthelme, F. (2017). Ecosystem sentinels for climate change? Evidence of wetland cover changes over the last 30 years in the tropical Andes. PLoS ONE, 12(5), e0175814. https://doi.org/10.1371/journal.pone.0175814
Mazzarino, M., & Finn, J. T. (2016). An NDVI analysis of vegetation trends in an Andean watershed. Wetlands Ecology and Management. https://doi.org/10.1007/s11273-016-9492-0
Moreau, S., & Le Toan, T. (2003). Biomass quantification of Andean wetland forages using ERS satellite SAR data for optimizing livestock management. Remote Sensing of Environment, 84, 477-492. https://doi.org/10.1016/S0034-4257(02)00111-6
Navarro, C. J., Izquierdo, A. E., Aráoz, E., Foguet, J., & Grau, H. R. (2020). Rewilding of large herbivore communities in high elevation Puna: Geographic segregation and no evidence of positive effects on peatland productivity. Regional Environmental Change, 20, 112. https://doi.org/10.1007/s10113-020-01704-8
Otto, M., Scherer, D., & Richters, J. (2011). Hydrological differentiation and spatial distribution of high altitude wetlands in a semi-arid Andean region derived from satellite data. Hydrology and Earth System Sciences, 15, 1713-1727. https://doi.org/10.5194/hess-15-1713-2011
Rojo,

---

### 9. Vegetación / Cojines
**Pregunta:** ¿Qué especies de plantas en cojín dominan los bofedales y cómo se distribuyen según el ambiente?

#### Modo `completo` (DeepSeek, ~194997 tok, 4.7 s, DOI: 2/2)

En los bofedales de los Andes centrales, la turba la forman sobre todo juncáceas en cojín, y cuál domina depende del agua y las sales. *Distichia muscoides* predomina donde el agua de vertiente es abundante y muy pobre en sodio y cloruro; *Oxychloe andina* tolera mejor la sequía, la salinidad y el aporte de sedimentos, y se impone hacia el sur y el oeste; junto a lagunas saladas aparece la ciperácea *Zameioscirpus atacamensis*, que rara vez supera los 4300 m (Ruthsatz, 2012). La altitud y el contenido de sodio y cloruro del agua son los factores que más ordenan estos tipos: los bofedales de *Patosia* sola están 200 a 250 m más bajos que los de *Distichia* (Ruthsatz, 2012). En la Puna argentina, las vegas altas y frías están dominadas por *Oxychloe andina* y son menos diversas, mientras las bajas y cálidas son más ricas y a menudo salinas (Izquierdo et al., 2020). Ojo: esta clasificación viene de Bolivia y se extiende a Jujuy y Salta, con el límite sur de los bofedales de *Distichia* cerca del Paso de Acay (Ruthsatz, 2012).

Fuentes:
Ruthsatz, B. (2012). Vegetación y ecología de los bofedales altoandinos de Bolivia (C. Pérez, Trad.). Phytocoenologia, 42(3-4), 133-179. https://doi.org/10.1127/0340-269X/2012/0042-0535
Izquierdo, A. E., Carilla, J., Nieto, C., Osinaga Acosta, O., Martin, E., Grau, H. R., & Reynaga, M. C. (2020). Multi-taxon patterns from high Andean peatlands: Assessing climatic and landscape variables. Community Ecology. https://doi.org/10.1007/s42974-020-00029-0

#### Modo `rag` (DeepSeek, ~6720 tok, 3.0 s, DOI: 2/2)

¡Buena pregunta! En los bofedales andinos las plantas en cojín que forman la turba son sobre todo juncáceas: *Distichia muscoides*, *Oxychloe andina* y *Patosia clandestina*, y en ambientes salinos aparece la ciperácea *Zameioscirpus atacamensis* (Ruthsatz, 2012). La distribución la ordenan principalmente la altitud y el contenido de sodio y cloruro del agua de vertiente: *Distichia* domina donde el agua es muy pobre en esas sales y hay poca sequía, mientras que *Oxychloe* tolera más sequía, sal y sedimentos y predomina hacia el sur y el oeste (Ruthsatz, 2012). Los bofedales de *Patosia* sola están unos 200 a 250 m más bajos que los de *Distichia*, y los salinos de *Zameioscirpus* rara vez superan los 4300 m (Ruthsatz, 2012). En la Puna argentina, las vegas altas, frías y húmedas están dominadas por *Oxychloe andina* y son más pobres en plantas, mientras que las bajas y cálidas son más ricas y a menudo salinas (Izquierdo et al., 2020). Ojo: el trabajo de Ruthsatz es una síntesis de bofedales de Bolivia y el sur de Perú, así que conviene tomarlo como referencia regional antes de aplicarlo a la Puna argentina.

Fuentes:
Ruthsatz, B. (2012). Vegetación y ecología de los bofedales altoandinos de Bolivia (C. Pérez, Trad.). Phytocoenologia, 42(3-4), 133-179. https://doi.org/10.1127/0340-269X/2012/0042-0535
Izquierdo, A. E., Carilla, J., Nieto, C., Osinaga Acosta, O., Martin, E., Grau, H. R., & Reynaga, M. C. (2020). Multi-taxon patterns from high Andean peatlands: Assessing climatic and landscape variables. Community Ecology. https://doi.org/10.1007/s42974-020-00029-0

---

### 10. Atlas fotográfico
**Pregunta:** ¿Qué vega tiene más fotografías en el atlas fotográfico y en qué provincia está?

#### Modo `completo` (DeepSeek, ~194993 tok, 3.0 s, DOI: 0/1)

La vega con más fotografías es **Real Grande**, con 64 fotos (16 con GPS exacto y 48 aproximadas), y está en la provincia de **Catamarca**, departamento de Antofagasta de la Sierra, entre 4158 y 4222 m s. n. m. (Atlas de vegas de la Puna argentina, data/fotos.json).

Fuentes:
Atlas de vegas de la Puna argentina (data/fotos.json).

#### Modo `rag` (DeepSeek, ~6403 tok, 1.7 s, DOI: 0/1)

¡Hola! La vega con más fotos en el atlas es **Real Grande**, con 64 fotografías (16 con GPS exacto y 48 aproximadas), y está en **Antofagasta de la Sierra, Catamarca**, entre 4158 y 4222 m s. n. m. (Atlas de vegas de la Puna argentina, data/fotos.json). Sus campañas fueron en mayo 2018 (otoño, 10 fotos), febrero 2021 (verano, 41) y octubre 2021 (primavera, 13) (Atlas de vegas de la Puna argentina, data/fotos.json). De paso, Catamarca — Antofagasta de la Sierra es también el departamento con más fotos del atlas: 319 (Atlas de vegas de la Puna argentina, data/fotos.json).

Fuentes:
Atlas de vegas de la Puna argentina (data/fotos.json).

---

### 11. Cambio climático
**Pregunta:** ¿Cómo afecta el retroceso de glaciares y el cambio climático a estos humedales?

#### Modo `completo` (DeepSeek, ~194993 tok, 5.7 s, DOI: 6/6)

¡Buena pregunta! Te cuento lo que dicen los estudios, con una aclaración importante: casi toda la evidencia viene de Perú, Bolivia y Chile, y en la Puna argentina las vegas casi no tienen glaciares, así que hay que tomarla con cautela.

- **A corto plazo, el deshielo puede hacer crecer los humedales.** En la Cordillera Blanca (Perú) los humedales aumentaron de 12.402 a 13.858 ha entre 1987 y 1995, siguiendo el "pico de agua" glaciar, y se espera que después declinen (Polk et al., 2017). En la Cordillera Real (Bolivia) crecieron 1,15 km² por año entre 1984 y 2011, pero sobre todo por pastizales húmedos temporales y no por bofedales de cojín (Dangles et al., 2017).
- **No todos los bofedales dependen del glaciar.** En diez turberas de Bolivia y Perú el agua viene de acuíferos de ladera recargados por lluvia y nieve, no del deshielo (Cooper et al., 2019). Por eso, para vegas sin glaciares como las puneñas, pesan más la lluvia y el agua subterránea.
- **El riesgo mayor es la caída de la napa.** Los cojines de *Distichia* mueren si la napa baja más de 1 m durante meses (Cooper et al., 2015), y en la Puna argentina la productividad de las vegas siguió al área de las lagunas cercanas y no a la lluvia satelital (Casagranda et al., 2019).
- **El calentamiento también afecta el suelo.** En vegas de Catamarca, incubar suelos a 25 °C triplicó la respiración de CO₂ respecto de 10 °C (Chiappero et al., 2024).

Fuentes:
Polk, M. H., Young, K. R., Baraer, M., Mark, B. G., McKenzie, J. M., Bury, J., & Carey, M. (2017). Exploring hydrologic connections between tropical mountain wetlands and glacier recession in Peru's Cordillera Blanca. Applied Geography, 78, 94-103. https://doi.org/10.1016/j.apgeog.2016.11.004
Dangles, O., Rabatel, A., Kraemer, M., Zeballos, G., Soruco, A., Jacobsen, D., & Anthelme, F. (2017). Ecosystem sentinels for climate change? Evidence of wetland cover changes over the last 30 years in the tropical Andes. PLoS ONE, 12(5), e0175814. https://doi.org/10.1371/journal.pone.0175814
Cooper, D. J., Sueltenfuss, J., Oyague, E., Yager, K., Slayback, D., Cabero Caballero, E. M., Argollo, J., & Mark, B. G. (2019). Drivers of peatland water table dynamics in the central Andes, Bolivia and Peru. Hydrological Processes, 33, 1913-1925. https://doi.org/10.1002/hyp.13446
Cooper, D. J., Kaczynski, K., Slayback, D., & Yager, K. (2015). Growth and organic carbon production in peatlands dominated by Distichia muscoides, Bolivia, South America. Arctic, Antarctic, and Alpine Research, 47(3), 505-510. https://doi.org/10.1657/AAAR0014-060
Casagranda, E., Navarro, C., Grau, H. R., & Izquierdo, A. E. (2019). Interannual lake fluctuations in the Argentine Puna: Relationships with its associated peatlands and climate change. Regional Environmental Change, 19, 1737-1750. https://doi.org/10.1007/s10113-019-01514-7
Chiappero, M. F., Vaieretti, M. V., Gallardo, N., & Izquierdo, A. E. (2024). Experimental warming increases respiration and affects microbial communities of soil wetlands at different elevations of the Argentinean Puna. Soil Ecology Letters, 6(4), 240242. https://doi.org/10.1007/s42832-024-0242-6

#### Modo `rag` (DeepSeek, ~6427 tok, 3.4 s, DOI: 2/2)

¡Qué lindo preguntar eso, che! Es una de las cosas que más se estudia en los Andes, aunque ojo: casi toda la evidencia viene de Bolivia y Perú, no de la Puna argentina.

Lo que muestran los estudios es que, a corto plazo, el deshielo **amplía** los humedales. En la Cordillera Real de Bolivia crecieron 1,15 km² por año entre 1984 y 2011, pero sobre todo por parches temporales de pastizal húmedo, no por bofedales de cojín perennes (Dangles et al., 2017). En el Parque Nacional Huascarán (Perú) los humedales pasaron de 12.402 a 13.858 ha entre 1987 y 1995, siguiendo un "pico de agua" glaciar con retraso (Polk et al., 2017).

El problema es que ese aumento se prevé **transitorio**: cuando el aporte glaciar disminuya, los humedales se degradarían, se fragmentarían y perderían servicios como almacenar carbono y agua (Dangles et al., 2017; Polk et al., 2017). Además, los humedales pequeños y de contorno irregular son los más propensos a secarse (Dangles et al., 2017).

Fuentes:
Dangles, O., Rabatel, A., Kraemer, M., Zeballos, G., Soruco, A., Jacobsen, D., & Anthelme, F. (2017). Ecosystem sentinels for climate change? Evidence of wetland cover changes over the last 30 years in the tropical Andes. PLoS ONE, 12(5), e0175814. https://doi.org/10.1371/journal.pone.0175814
Polk, M. H., Young, K. R., Baraer, M., Mark, B. G., McKenzie, J. M., Bury, J., & Carey, M. (2017). Exploring hydrologic connections between tropical mountain wetlands and glacier recession in Peru's Cordillera Blanca. Applied Geography, 78, 94-103. https://doi.org/10.1016/j.apgeog.2016.11.004

---

### 12. Repregunta (pastoreo en Chile)
**Pregunta:** ¿Y en Chile qué muestran los estudios?
*(Con historial previo: "¿Cómo afecta el pastoreo de camélidos y ganado a las vegas y bofedales?")*

#### Modo `completo` (DeepSeek, ~195031 tok, 4.1 s, DOI: 4/4)

En el altiplano chileno, el bofedal de Arabilla (Tarapacá) está sobrecargado: la oferta de *Oxychloe andina* alcanza para unas 60 de las 394 unidades animales presentes, y cinco meses de exclusión mejoraron rasgos foliares sin cambiar la cobertura (Carevic et al., 2019). En el Parque Nacional Lauca, el ganado doméstico favorece los cojines poco palatables de *Oxychloe* y reduce la diversidad, mientras que las vicuñas, que comen cojines, mantienen la riqueza de especies (Rundel y Palma, 2000). Además, la cantidad de llamas y alpacas por sector se correlacionó con la superficie de bofedal (r² = 0,67), pero la de vicuñas no, lo que sugiere que la competencia con el ganado podría limitar su acceso a los bofedales (Shaw et al., 2012). Un caso distinto es Chiu-Chiu, donde la vega se secó cuando el Estado no le asignó derechos de riego y el ganado pasó de unas 3000 cabezas a 50-100, según los comuneros (Prieto, 2015).

Fuentes:
Carevic, F. S., Anderson, M., & Muñoz, A. (2019). Is the temporary grazing exclusion a good management alternative for arid peatlands? Arid Land Research and Management. https://doi.org/10.1080/15324982.2018.1563242
Rundel, P. W., & Palma, B. (2000). Preserving the unique puna ecosystems of the Andean Altiplano: A descriptive account of Lauca National Park, Chile. Mountain Research and Development, 20(3), 262-271. https://doi.org/10.1659/0276-4741(2000)020[0262:PTUPEO]2.0.CO;2
Shaw, A. K., Galaz, J. L., & Marquet, P. A. (2012). Population dynamics of the vicuña (Vicugna vicugna): density-dependence, rainfall, and spatial distribution. Journal of Mammalogy, 93(3), 658-666. https://doi.org/10.1644/11-MAMM-A-257.1
Prieto, M. (2015). Privatizing water in the Chilean Andes: The case of Las Vegas de Chiu-Chiu. Mountain Research and Development, 35(3), 220-229. https://doi.org/10.1659/MRD-JOURNAL-D-14-00033.1

#### Modo `rag` (DeepSeek, ~6655 tok, 3.5 s, DOI: 3/3)

En el norte de Chile, los pastores aymaras mantienen los bofedales con limpieza, riego, abonado con estiércol, períodos de descanso y quemas controladas, y los autores sostienen que bofedales y pastizales son ecosistemas socio-naturales producidos por el pastoreo, no pastos naturales (García et al., 2021). Los planes de manejo de CONAF, en cambio, los tratan como pastizales naturales, restringen el fuego y los usos tradicionales, y no les dan a los pastores un rol activo (García et al., 2021). Además, la cantidad de llamas y alpacas por sector se correlacionó con la superficie de bofedal (r² = 0,67), pero la de vicuñas no (Shaw et al., 2012). En Lauca, el pastoreo doméstico reduce gramíneas y juncos palatables, mientras que las vicuñas consumen cojines y mantienen la riqueza (Rundel y Palma, 2000). Ojo: son estudios de Chile, no de la Puna argentina.

Fuentes:
García, M., Prieto, M., & Kalazich, F. (2021). The protection of the mountain ecosystems of the Southern Central Andes: Tensions between Aymara herding practices and conservation policies. eco.mont, 13(1), 22-30. https://doi.org/10.1553/eco.mont-13-1s22
Shaw, A. K., Galaz, J. L., & Marquet, P. A. (2012). Population dynamics of the vicuña (Vicugna vicugna): density-dependence, rainfall, and spatial distribution. Journal of Mammalogy, 93(3), 658-666. https://doi.org/10.1644/11-MAMM-A-257.1
Rundel, P. W., & Palma, B. (2000). Preserving the unique puna ecosystems of the Andean Altiplano: A descriptive account of Lauca National Park, Chile. Mountain Research and Development, 20(3), 262-271. https://doi.org/10.1659/0276-4741(2000)020[0262:PTUPEO]2.0.CO;2

---

### 13. Repregunta (carbono en Puna arg.)
**Pregunta:** ¿Y en la Puna argentina hay datos de eso?
*(Con historial previo: "¿Cuánto carbono orgánico acumulan los suelos de turberas y bofedales andinos?")*

#### Modo `completo` (DeepSeek, ~195031 tok, 4.2 s, DOI: 2/2)

Sí, hay mediciones propias. En diez vegas de la Puna argentina (3323–4748 m), el suelo hasta 30 cm almacenó en promedio 66,11 Mg C ha-1 (rango 21,79–139,67), más del 70 % del carbono total del sistema, y su variación respondió a factores locales (capacidad de intercambio catiónico, potasio, relación C:N y profundidad del nivel freático) y no a la altitud (Chiappero et al., 2026). En dos turberas de Catamarca asociadas a un salar con litio, Laguna Negra guardó 281,8 Mg ha-1 en 0–30 cm frente a 71,5 en Laguna Tres Quebradas, lo que muestra que humedales vecinos pueden responder muy distinto (Chiappero et al., 2021). Para comparar, la síntesis ecorregional de 12 estudios de la Puna da una media de 173,94 Mg C ha-1 (Chiappero et al., 2026).

Fuentes:
Chiappero, M. F., Vaieretti, M. V., Gallardo, N., & Izquierdo, A. E. (2026). Carbon storage patterns in high Andean wetlands: local factors explain the variability of soil carbon stocks in the Argentine Puna. Plant and Soil, 525, 1393–1408. https://doi.org/10.1007/s11104-026-08829-5
Chiappero, M. F., Vaieretti, M. V., & Izquierdo, A. E. (2021). A baseline soil survey of two peatlands associated with a lithium-rich salt flat in the Argentine Puna: physico-chemical characteristics, carbon storage and biota. Mires and Peat, 27, Article 16, 1–13. https://doi.org/10.19189/MaP.2020.OMB.StA.2126

#### Modo `rag` (DeepSeek, ~6793 tok, 2.6 s, DOI: 3/3)

En los estudios disponibles no aparece información sobre carbono orgánico en suelos de vegas de la Puna argentina. La revisión regional encontró solo 14 muestras de turberas entre 334 muestras de suelo superficial, y casi ningún dato del sur andino (Alavi-Murillo et al., 2022). De la Puna argentina la bibliografía sobre suelos y turba reúne solo dos trabajos, ambos sobre la turbera de Cerro Tuzgle (Jujuy), que miden espesor y edad de la turba, carbono, química de la materia orgánica, agua retenida, pastoreo y gases (Schittek et al., 2016) (Kock et al., 2019). Así que hay un vacío grande justo en nuestra zona.

Fuentes:
Alavi-Murillo, G., Diels, J., Gilles, J., & Willems, P. (2022). Soil organic carbon in Andean high-mountain ecosystems: Importance, challenges, and opportunities for carbon sequestration. Regional Environmental Change, 22, 128. https://doi.org/10.1007/s10113-022-01980-6
Schittek, K., Kock, S. T., Lücke, A., Hense, J., Ohlendorf, C., Kulemeyer, J. J., Lupo, L. C., & Schäbitz, F. (2016). A high-altitude peatland record of environmental changes in the NW Argentine Andes (24°S) over the last 2100 years. Climate of the Past, 12, 1165-1180. https://doi.org/10.5194/cp-12-1165-2016
Kock, S. T., Schittek, K., Wissel, H., Vos, H., Ohlendorf, C., Schäbitz, F., Lupo, L. C., Kulemeyer, J. J., & Lücke, A. (2019). Stable oxygen isotope records (δ18O) of a high-Andean cushion peatland in NW Argentina (24°S) imply South American Summer Monsoon related moisture changes during the Late Holocene. Frontiers in Earth Science, 7, 45. https://doi.org/10.3389/feart.2019.00045

---

### 14. Fuera de tema
**Pregunta:** ¿Cuál es la receta tradicional de pizza napolitana?

#### Modo `completo` (DeepSeek, ~194986 tok, 7.7 s, DOI: N/A)

Uy, ahí me agarraste fuera de tema: yo soy Doña Vicuña y solo sé de vegas, bofedales y turberas de los Andes. De pizza napolitana no tengo nada en mis estudios, así que mejor no te invento nada.

Si querés, te cuento sobre la flora de las vegas, cómo se mide el carbono de sus suelos o qué se sabe del pastoreo en estos humedales. ¿Te interesa alguno de esos temas?

#### Modo `rag` (DeepSeek, ~6650 tok, 2.1 s, DOI: 1/2)

Uy, esa me la sé de memoria… pero no por los estudios, ja. Me limito a lo que sé de vegas, bofedales y turberas de los Andes, así que de pizza napolitana no tengo nada para contarte.

Si querés, te cuento sobre el riego tradicional que amplía bofedales (Buttolph y Coppock, 2004) o sobre cómo los pastores usaron el fuego y el agua para mantener estos humedales (Domic et al., 2018). ¿Te interesa alguno de esos temas?

Fuentes:
Buttolph, L. P., & Coppock, D. L. (2004). Influence of deferred grazing on vegetation dynamics and livestock productivity in an Andean pastoral system. Journal of Applied Ecology, 41, 664-674.
Domic, A. I., Capriles, J. M., Escobar-Torrez, K., Santoro, C. M., & Maldonado, A. (2018). Two thousand years of land-use and vegetation evolution in the Andean highlands of northern Chile inferred from pollen and charcoal analyses. Quaternary, 1(3), 32. https://doi.org/10.3390/quat1030032

---

### 15. Sin datos en la wiki
**Pregunta:** ¿Cuál fue el caudal exacto del río Loa en enero de 2025 medido por la estación de Calama?

#### Modo `completo` (DeepSeek, ~194996 tok, 3.1 s, DOI: 1/1)

En los estudios que conozco no hay datos sobre el caudal del río Loa en enero de 2025 medido en Calama. Lo que sí hay es el caso de Las Vegas de Chiu-Chiu, sobre el mismo río Loa, donde se documenta que tras la constitución de derechos de agua iniciada en 1983 se asignaron 850 l/s del Loa a la empresa sanitaria para el crecimiento urbano ligado al cobre, la vega se secó y, según los comuneros, el ganado pasó de unas 3000 a 50-100 cabezas (Prieto, 2015). Esa evidencia es cualitativa y basada en testimonios e imágenes Landsat, no en mediciones hidrológicas de una fecha puntual (Prieto, 2015).

Fuentes:
Prieto, M. (2015). Privatizing water in the Chilean Andes: The case of Las Vegas de Chiu-Chiu. Mountain Research and Development, 35(3), 220-229. https://doi.org/10.1659/MRD-JOURNAL-D-14-00033.1

#### Modo `rag` (DeepSeek, ~6309 tok, 1.9 s, DOI: 1/1)

En los estudios que tengo a mano no hay ningún dato sobre el caudal del río Loa medido en Calama en enero de 2025. Lo que sí aparece es que, tras la privatización del agua en Chiu-Chiu, se asignaron 850 l/s del Loa aguas arriba de esa localidad a la empresa sanitaria estatal (Prieto, 2015), pero no hay registros de caudales por fecha como el que buscás.

Fuentes:
Prieto, M. (2015). Privatizing water in the Chilean Andes: The case of Las Vegas de Chiu-Chiu. Mountain Research and Development, 35(3), 220-229. https://doi.org/10.1659/MRD-JOURNAL-D-14-00033.1

---
