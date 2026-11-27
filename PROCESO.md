# Cómo actualizar el atlas

Este documento dice qué hacer cada vez que llega información nueva: fotos de una campaña, correcciones, puntos de muestreo o artículos para el chat. La idea es que cualquier persona (o un asistente de IA) pueda hacerlo siempre igual y que los controles los haga un script, no una revisión a ojo.

## Principios

1. **`data/fotos.json` es la fuente de verdad** de las fotos. El sitio, los filtros y las tablas del README salen de ahí.
2. **Lo generado no se edita a mano.** Los bloques `<!-- auto:... -->` del README, `BIBLIOGRAFIA.md` y los archivos del bot (`bot/conocimiento.js`, `bot/indice_rag.js`) se rehacen con sus scripts.
3. **Nada se sube sin pasar el validador.** `python herramientas/validar_datos.py` tiene que terminar con `0 errores`.
4. **Un nombre por vega.** Si la vega tiene punto de muestreo, se usa el nombre del punto tal cual figura en `data/vegas_muestreadas.geojson`.
5. **Privacidad y secretos.** Las fotos se publican sin EXIF. Las claves de API van en variables de entorno o en `bot/.dev.vars`, nunca en el repositorio.

Los comandos se corren desde la raíz del repositorio. Hace falta Python 3 con Pillow (para que el validador controle los tamaños de las imágenes).

## Fotos de una campaña nueva

### 1. Preparar las imágenes

Antes de achicarlas, leer de cada original la **fecha y hora** y, si tiene, la **ubicación GPS** del EXIF. Después:

- `fotos/<id>.jpg`: lado mayor de 1600 px como máximo.
- `miniaturas/<id>.jpg`: lado mayor de 480 px como máximo.
- Las dos **sin metadatos EXIF**.
- `<id>` es el nombre del archivo sin extensión, con la convención de las fotos existentes: `AAAAMMDD-HHMMSS` para las de cámara o teléfono e `img-AAAAMMDD-waNNNN` para las que llegaron por WhatsApp.

### 2. Agregar cada foto a `data/fotos.json`

Cada foto es un objeto dentro de `"fotos"` con todos estos campos:

| Campo | Cómo se obtiene |
|---|---|
| `id` | Nombre del archivo, sin `.jpg`. |
| `fecha` | Del EXIF: `AAAA-MM-DD HH:MM`. Si no hay hora (fotos de WhatsApp), solo `AAAA-MM-DD`. |
| `lat`, `lon` | Del GPS del EXIF, en WGS84, con 5 decimales. Si no hay GPS, se estiman a partir de la hora de la toma (junto a otras fotos con GPS del mismo día), del nombre de la vega o del paisaje. |
| `precision` | `exacta` si las coordenadas vienen del GPS; `aproximada` si se estimaron. |
| `vega` | Ver "Nombres de vegas", más abajo. `null` si no se sabe. |
| `ancho`, `alto` | Tamaño en píxeles de `fotos/<id>.jpg`. |
| `altitud` | Entero, en metros, del Copernicus DEM GLO-30 (versión 2024_1) en el punto de la foto, extraído con Google Earth Engine. |
| `provincia`, `departamento` | El polígono de `data/departamentos.geojson` que contiene el punto. Si cae justo afuera, el departamento más cercano a menos de 5 km. |
| `etiquetas`, `tipo_toma`, `verdor` | Los completa el etiquetado automático (paso 4). Mientras tanto: `[]`, `"otro"` y `3`. |

### 3. Nombres de vegas

- Si la foto está a **menos de 3 km de un punto de muestreo**, se usa el nombre de ese punto, **copiado exacto** (mayúsculas, tildes y abreviaturas incluidas).
- Si no hay punto cerca, se usa el nombre con que se identificó la vega en el campo. Antes de escribirlo, revisar si ya existe en `fotos.json` y usar la misma forma.
- No agregar el prefijo "Vega" a un nombre que ya existe sin él (por ejemplo, `Matadero` y no `Vega Matadero`).
- El validador marca como error dos nombres que solo difieren en mayúsculas, tildes, puntos o el prefijo "Vega".

### 4. Etiquetado ecológico

Requiere la variable de entorno `GEMINI_API_KEY`.

```bash
python herramientas/etiquetar_fotos_decisions.py              # evalúa solo las fotos nuevas
```

Revisar `herramientas/revision_dudosas.csv` (los casos en zona gris) y después fusionar las etiquetas en `fotos.json`:

```bash
python herramientas/etiquetar_fotos_decisions.py --aplicar-json
```

### 5. Actualizar el resumen y el README

- El bloque `"resumen"` al principio de `fotos.json` alimenta la portada del sitio. Si quedó desactualizado, el validador dice qué valor corresponde a cada campo. Actualizar también `generado` con la fecha del día.
- Regenerar las tablas del README:

```bash
python herramientas/actualizar_readme.py
```

### 6. Validar, probar y subir

```bash
python herramientas/validar_datos.py
python -m http.server 8000
```

Con el validador en `0 errores`, abrir <http://localhost:8000> y revisar que las fotos nuevas aparezcan en el mapa y en su campaña. Después, hacer commit y push a `main`. GitHub Pages publica el sitio en uno o dos minutos.

## Correcciones de datos existentes

Renombrar una vega, mover una ubicación o corregir una fecha:

1. Editar `data/fotos.json` (a mano o con la herramienta local de etiquetado, que no se versiona).
2. Si cambian coordenadas: recalcular `altitud`, `provincia` y `departamento`, y revisar si la foto queda a menos de 3 km de otro punto de muestreo.
3. `python herramientas/actualizar_readme.py` y `python herramientas/validar_datos.py`.
4. Commit y push.

## Puntos de muestreo nuevos

1. Agregar el punto a `data/vegas_muestreadas.geojson` con las propiedades `nombre`, `altura`, `provincia`, `departamento` y `muestreo`.
2. Buscar las fotos a menos de 3 km y pasarlas al nombre del punto.
3. Actualizar a mano la cantidad de puntos en el README: aparece en "Qué muestra" y en "Estructura".
4. Actualizar el README, validar, commit y push.

## Artículos nuevos para el chat (Doña Vicuña)

La wiki bibliográfica es local (`wiki/` no se sube) y su procedimiento completo está en `wiki/CLAUDE.md`. En resumen:

1. Copiar los PDFs a la carpeta de la bibliografía y correr `python herramientas/wiki/extraer_texto.py "<carpeta de PDFs>"`.
2. Escribir la ficha de cada documento nuevo en `wiki/_fichas/` según `wiki/_esquema.md`, leyendo el texto completo. **Las fichas y las síntesis no se generan con APIs**: la clave de `bot/.dev.vars` es solo para el bot.
3. `python herramientas/wiki/validar.py` sin errores.
4. Actualizar las síntesis afectadas (`python herramientas/wiki/insumos_sintesis.py` y `wiki/_sintesis/_instrucciones.md`).
5. `python herramientas/wiki/construir.py`: regenera la wiki, `BIBLIOGRAFIA.md`, `bot/conocimiento.js` y `bot/indice_rag.js` (con embeddings).
6. Desde `bot/`: `npx wrangler deploy` para publicar el bot con el conocimiento nuevo.
7. Commit y push de `BIBLIOGRAFIA.md`, con un mensaje del tipo `Actualiza bibliografía del chatbot a N documentos (+Autor año, ...)`.

Más detalles del bot (proveedores, modos, costos) en [bot/README.md](bot/README.md).

## Commits

- En español, con un verbo en presente que diga qué cambia: `Agrega fotos de la campaña de marzo de 2027`, `Unifica nombres de vegas duplicados`, `Corrige la ubicación de 3 fotos de Tocomar`.
- Un commit por tarea. Los datos y el README regenerado van juntos.

## Lo que nunca se sube

- Claves y credenciales: `.env`, `bot/.dev.vars`, tokens.
- La wiki (`wiki/`) y los PDFs.
- Las salidas intermedias del etiquetado (`herramientas/etiquetas_decisions_raw.json`, `herramientas/revision_dudosas.csv`).
- La herramienta local de etiquetado y las copias de respaldo de `fotos.json`.

El `.gitignore` ya excluye casi todo esto. Antes de cada commit, mirar `git status` por si aparece algo inesperado.

## Lista de control

- [ ] Fotos en `fotos/` y `miniaturas/`, sin EXIF y con el tamaño correcto.
- [ ] Una entrada completa por foto en `data/fotos.json`.
- [ ] Nombres de vega iguales a los de los puntos de muestreo cuando corresponde.
- [ ] Etiquetado ecológico aplicado.
- [ ] `python herramientas/actualizar_readme.py`.
- [ ] `python herramientas/validar_datos.py` con `0 errores`.
- [ ] Revisión rápida en <http://localhost:8000>.
- [ ] Commit en español y push.
