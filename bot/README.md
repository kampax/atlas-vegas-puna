# Bot del atlas (Doña Vicuña)

Chat que responde preguntas sobre vegas y bofedales usando **solo la wiki bibliográfica**
(`wiki/`, local y fuera de git). Las respuestas las genera **GLM** de Z.AI (`glm-4.7-flash`,
gratuito, por defecto), **DeepSeek** (`deepseek-flash`) o **Gemini** de Google (`gemini-2.5-flash`),
según se elija.

```
index.html + assets/chat.js  →  bot/worker.js (Cloudflare Worker)  →  API de GLM, DeepSeek o Gemini
     el navegador               guarda la clave, agrega el personaje
                                y la wiki completa como contexto
```

- `personaje.js`: nombre, voz y reglas del personaje (editable). También tiene `SOBRE_EL_ATLAS`, los datos fijos del atlas (autor de las fotos, contacto, instituciones, financiamiento y créditos), que van al modelo en los dos modos. Si cambian los créditos del `README.md` o de `index.html`, actualizalos ahí también.
- `worker.js`: el intermediario. Valida la conversación, limita orígenes (CORS) y largo, elige
  el modo (`completo` o `rag`) y devuelve la respuesta en streaming.
- `conocimiento.js`: la wiki empaquetada (~410 mil tokens, para `MODO = "completo"`). **Se genera**
  con `python herramientas/wiki/construir.py` y no se sube a git.
- `indice_rag.js`: índice BM25, fragmentos con citas completas y el vector (embedding bge-m3) de cada
  fragmento, en int8 + escala y base64 (para `MODO = "rag"`). También **se genera** con
  `python herramientas/wiki/construir.py` y no se sube a git.
- `rag.js`: buscador en JavaScript puro, sin dependencias externas: BM25 (normalización en español,
  sinónimos del dominio y soporte para repreguntas) y, si el Worker pudo convertir la pregunta en
  vector, búsqueda híbrida con los embeddings precalculados.
- `servidor-local.mjs`: sirve el atlas con el chat en `http://localhost:8787` para probar.

## Probar en tu computadora

1. Crear `bot/.dev.vars` (no se sube a git) con la clave del servicio que quieras usar:
   ```
   GLM_API_KEY="..."
   DEEPSEEK_API_KEY="sk-..."
   GEMINI_API_KEY="AIza..."
   PROVEEDOR="glm"
   ```
   `PROVEEDOR` es opcional: si falta, se usa el primero que tenga clave (GLM, DeepSeek, Gemini).
2. Desde la raíz del repo: `node bot/servidor-local.mjs` y abrir http://localhost:8787.

## Publicar (Cloudflare Workers, plan gratuito)

Hace falta una cuenta de Cloudflare y Node.js. Desde la carpeta `bot/`:

```
npx wrangler login
npx wrangler secret put GLM_API_KEY     # o DEEPSEEK_API_KEY / GEMINI_API_KEY, según el proveedor
npx wrangler deploy
```

El deploy imprime la dirección del Worker (p. ej. `https://atlas-vegas-bot.<tu-cuenta>.workers.dev`).
Ponerla en `index.html`, en `window.CHAT.url`, agregando `/chat` al final, y publicar el sitio.
Mientras `url` esté vacía, el chat no aparece en el sitio publicado (sí en `localhost`).

`ORIGENES` en `wrangler.toml` lista los dominios que pueden usar el bot
(hoy `https://kampax.github.io`). Si el sitio cambia de dominio, actualizarlo y volver a desplegar.

## Elegir el proveedor (GLM, DeepSeek o Gemini)

En `wrangler.toml`, `PROVEEDOR = "glm"`, `"deepseek"` o `"gemini"`, y volver a desplegar.
Solo hace falta cargar el secreto del proveedor elegido. Los modelos se cambian con `MODELO_GLM`,
`MODELO` (DeepSeek) y `MODELO_GEMINI`.

**Respaldo:** `RESPALDO = "deepseek"` hace que, si el proveedor principal falla o está saturado
(algo frecuente en el plan gratuito de GLM), la pregunta se responda con DeepSeek sin que quien
consulta lo note. Se pueden poner varios en orden (`"deepseek,gemini"`); solo se usan los que
tienen su clave cargada. Tras una falla, el principal se saltea durante 2 minutos para no demorar
cada pregunta. Hoy está configurado así: **GLM por defecto y DeepSeek de respaldo**.

**GLM (Z.AI):** la clave se crea en <https://z.ai> (API Keys). El modelo por defecto,
`glm-4.7-flash`, es gratuito. `glm-4.5-flash`, también gratuito, tiene menos contexto y no alcanza
para la wiki completa. El plan gratuito limita cuántas consultas se atienden a la vez; si se
satura, el chat responde "Demasiadas consultas". Si la clave es del GLM Coding Plan, ese plan usa
otra dirección (`GLM_API_URL`) y está pensado para herramientas de programación, no para un chat público.

La clave de Gemini se crea gratis en <https://aistudio.google.com/apikey>. Tener en cuenta:

- **Plan gratuito de Gemini:** sirve para probar, pero cada pregunta manda la wiki completa
  (~410 mil tokens) y el plan gratuito limita los tokens por minuto, así que admite muy pocas
  preguntas por minuto y por día. Además, en el plan gratuito Google puede usar las consultas
  para mejorar sus productos. Para uso público conviene activar la facturación en Google AI Studio.
- Google retira modelos con el tiempo: si el chat deja de responder, revisar el nombre vigente en <https://ai.google.dev/gemini-api/docs/models> y actualizar `MODELO_GEMINI`.

## Elegir el modo (`completo` o `rag`)

El bot soporta dos modos, configurables con la variable `MODO` en `bot/wrangler.toml` (producción)
o `bot/.dev.vars` / variables de entorno (local). Ambos modos funcionan con GLM, DeepSeek y Gemini
y respetan `RESPALDO`. Cambiar de modo es cambiar `MODO` y reiniciar (`servidor-local.mjs`) o
desplegar (`npx wrangler deploy`). La respuesta incluye siempre la cabecera `X-Modo`.

- **`MODO = "rag"` (por defecto):** busca en el propio Worker los fragmentos más relevantes de la wiki
  (~300–600 palabras cada uno, con su `REF` y `Cita:` completa con DOI) y envía solo el personaje +
  esos fragmentos (por defecto `RAG_K = 8` y tope `RAG_MAX_TOKENS = 6000`). Toma la última pregunta y
  hasta 2 anteriores para entender repreguntas (p. ej. *"¿y en Chile?"*). Si no encuentra fragmentos
  relevantes, responde directo sin llamar al modelo.
  - *Búsqueda híbrida:* el Worker convierte la pregunta en vector con Workers AI (`@cf/baai/bge-m3`,
    binding `[ai]` en `wrangler.toml`; si es una repregunta corta, junto con la anterior) y lo compara
    con los vectores precalculados de cada fragmento. Puntaje = 0,3 × BM25 normalizado al máximo +
    0,7 × similitud normalizada respecto de la mediana (`(sim − mediana)/(máx − mediana)`, mínimo 0). Un
    fragmento sin palabras en común con la pregunta entra si su similitud normalizada es ≥ 0,6. Los
    sinónimos del dominio siguen sumando en la parte BM25. El peso se cambia con `RAG_PESO_BM25`.
  - *Fuera de tema:* con vector, si la similitud máxima (sin normalizar) queda bajo 0,43, se da la
    respuesta fija sin llamar al modelo (las preguntas de prueba fuera de tema dan ≤ 0,42 y las del
    tema ≥ 0,47). Sin vector se usa el umbral BM25 de siempre, que no filtra bien esas preguntas.
  - *Respaldo:* si no hay binding `AI`, se agota el cupo diario gratuito de Workers AI, falla o tarda
    más de 5 s, la búsqueda sigue solo con BM25, sin error para quien pregunta (y no se reintenta por
    30 min si fue el cupo, 1 min si fue otra falla). La cabecera `X-Busqueda` dice `hibrida` o `bm25`.
  - *Ventajas:* reduce la entrada ~50 veces (~7 mil tokens frente a ~410 mil), baja costos y
    latencia, permite usar modelos con menos contexto (como `glm-4.7-flash` gratuito) y ahorra cuota en planes gratuitos.
  - *Riesgos / límites:* con el tope de 6000 tokens entran ~3–6 fragmentos (las síntesis rondan
    2200 tokens), así que en preguntas muy comparativas cita menos estudios que `completo`.
- **`MODO = "completo"`:** envía el personaje + la wiki entera (~410 mil tokens)
  en cada pregunta.
  - *Ventajas:* el modelo ve los 241 documentos y todas las síntesis a la vez (máxima cobertura para
    preguntas amplias o comparativas) y los proveedores cachean ese prefijo fijo.
  - *Riesgos / límites:* sin caché es más caro y lento; excede el límite de prompt de `glm-4.7-flash`
    y satura rápido planes gratuitos con tope de tokens por minuto (como Gemini gratis).

**Pruebas en `localhost`:** solo en `localhost`/`127.0.0.1` se puede forzar el modo por pregunta sin
reiniciar usando `?modo=rag` o `?modo=completo` en `/chat` (o la cabecera `X-Modo-Prueba`), y en modo
rag `?busqueda=bm25` (sin embeddings) o `?peso=0.5` (peso de BM25). En producción esas opciones están
deshabilitadas. `servidor-local.mjs` imita el binding `AI` llamando a la API REST de Workers AI con
las credenciales de `npx wrangler login` (sin credenciales, o con `SIN_AI=1`, usa solo BM25).

Para comparar modos sobre un banco de 15 preguntas (`rag` = solo BM25, `hibrido-X` = híbrida con peso X):

```
node herramientas/wiki/comparar_modos.mjs --modos completo,rag,hibrido-0.3,hibrido-0.5,hibrido-0.7
```

Para medir solo la búsqueda, sin llamar a ningún modelo de lenguaje (estudio esperado recuperado en
preguntas parafraseadas, citas enviadas al modelo y similitud de preguntas fuera de tema):

```
node herramientas/wiki/probar_busqueda.mjs
```

Los vectores de las preguntas de ambos scripts se guardan en `wiki/_bot/vectores_preguntas.json`
para no gastar cupo de Workers AI al repetirlos.

Resultados del 20/11/2026 (peso 0,3 elegido; detalle en `herramientas/wiki/comparacion_modos.md`):

| | `completo` | `rag` (BM25) | híbrida 0,3 | híbrida 0,5 | híbrida 0,7 |
|---|---:|---:|---:|---:|---:|
| Fuentes citadas (15 preguntas, una corrida) | 73 | 51 | **62** | 49 | 36 |
| Estudio correcto recuperado (12 preguntas parafraseadas) | — | 8 | **10** | 10 | 9 |
| Preguntas fuera de tema con respuesta fija (6) | — | 0 | **6** | 6 | 6 |

Prueba del tope de tokens (21/11/2026, una corrida con GLM; detalle en `wiki/_bot/informe_rag_max_tokens.md`):
con `RAG_MAX_TOKENS = 10000` no hubo mejora (fuentes citadas: rag 41 → 35, híbrida 70 → 54) y cada
consulta usa ~45 % más tokens de entrada, así que **el tope queda en 6000**. La variación entre corridas
del mismo modo (±10–20 fuentes en el total) es del mismo tamaño que esas diferencias: para afinar el
tope conviene repetir cada configuración 2–3 veces.

## Estado del modo híbrido

*Actualizado el 21/11/2026.*

- **Publicado:** el Worker con la búsqueda híbrida y el binding `AI` está desplegado desde el 20/11/2026
  (versión `614e0d9c`), y su código es el de `main` (merge del PR #1, commit `a635ee6`).
- **Hoy responde solo con BM25:** el cupo gratuito diario de Workers AI se agotó el 20/11 por un error
  al calcular los vectores (un lote se repitió durante ~10 minutos; ya está corregido). A las 00:39 UTC
  del 21/11 la API todavía devolvía el error 4006 (*daily free allocation of 10,000 neurons*), aunque
  Cloudflare indica que el cupo se renueva a las 00:00 UTC. Mientras tanto el bot funciona con
  normalidad, sin la parte semántica, y pasa solo a la búsqueda híbrida cuando el cupo se libera, sin
  volver a desplegar.
- **Cómo verificarlo:** la cabecera `X-Busqueda` de cada respuesta dice `hibrida` o `bm25`:

  ```
  curl -s -D - -o /dev/null -X POST https://atlas-vegas-bot.kampax.workers.dev/chat -H "Content-Type: application/json" -H "Origin: https://kampax.github.io" --data '{"mensajes":[{"role":"user","content":"¿Qué es un bofedal?"}]}'
  ```

  Si dice `bm25`, `npx wrangler tail` (desde `bot/`) muestra el motivo en la línea
  `[chat] embeddings no disponibles, sigo con BM25: ...`. Después de un error de cupo, cada instancia
  del Worker espera 30 min antes de volver a probar Workers AI.
- **Si el error 4006 sigue más de un día:** revisar el consumo de Workers AI en el panel de Cloudflare.
  En el plan Workers Paid el uso del bot (una llamada corta por pregunta) costaría muy poco y no
  dependería del cupo gratuito.

## Actualizar el conocimiento

Cada vez que cambie la wiki: `python herramientas/wiki/construir.py` (regenera tanto
`bot/conocimiento.js` como `bot/indice_rag.js`) y luego `npx wrangler deploy`.

Al final, `construir.py` llama a `node herramientas/wiki/embeddings.mjs`, que agrega a `indice_rag.js`
el vector de cada fragmento (Workers AI `@cf/baai/bge-m3`, multilingüe):

- Los vectores se guardan en `wiki/_bot/vectores.json` (fuera de git, como la wiki) con la huella del
  texto (sha1 de modelo + texto) como clave: **solo los fragmentos nuevos o modificados van a la API**,
  en lotes de hasta 50 (y de hasta ~120 mil caracteres, porque la API acepta ~60 mil tokens por llamada).
  Recalcular los ~620 fragmentos desde cero tarda ~35 s.
- Credenciales: `CLOUDFLARE_API_TOKEN`, o la sesión de `npx wrangler login`. La cuenta sale de
  `CLOUDFLARE_ACCOUNT_ID`, de `account_id` en `wrangler.toml` o de la primera cuenta del token.
- Sin Node, sin red o sin credenciales el índice se arma igual: esos fragmentos quedan sin vector y se
  buscan solo por BM25. Para reusar solo el caché: `node herramientas/wiki/embeddings.mjs --sin-red`.
- Cuidado con el cupo gratuito de Workers AI (10 000 neuronas por día; según Cloudflare se renueva a
  las 00:00 UTC, pero el 21/11/2026 seguía agotado después de esa hora): recalcular todo el índice
  gasta una parte apreciable y una pregunta del chat, casi nada. El cupo es el mismo para el Worker y
  para estos scripts, así que agotarlo en una prueba deja al chat publicado solo con BM25.

## Costos y cuidados

- Cada pregunta manda la wiki completa. DeepSeek la cachea automáticamente: con caché, unos
  0,0006 USD por pregunta; sin caché (primera pregunta o tras un rato sin uso), unos 0,03 USD.
  Precios de `deepseek-flash` en noviembre de 2026; los de horario pico son el doble.
- Conviene cargar un saldo acotado en DeepSeek y, si el tráfico crece, agregar una regla de
  límite de velocidad en Cloudflare (Security → WAF → Rate limiting) para la ruta `/chat`.
- Para respuestas más elaboradas: `MODELO = "deepseek-v4-pro"` en `wrangler.toml` (unas 4 a 7 veces más caro).
