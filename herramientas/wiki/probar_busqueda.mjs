// Mide la recuperación del modo RAG sin llamar a ningún modelo de lenguaje: BM25 solo contra búsqueda
// híbrida (BM25 + embeddings) con distintos pesos.
//
// - Preguntas dirigidas: preguntas en español, con otras palabras, sobre un estudio puntual (casi todos
//   publicados en inglés). Acierto = el estudio esperado está entre los fragmentos enviados al modelo.
// - Banco de comparar_modos.mjs: cuántos estudios distintos (citas) recibe el modelo por pregunta.
// - Fuera de tema: similitud máxima, para calibrar UMBRAL_SIMILITUD_MINIMA.
//
// Uso (desde la raíz del repo; necesita `npx wrangler login` o CLOUDFLARE_API_TOKEN para los vectores
// de las preguntas nuevas; las ya calculadas se guardan en wiki/_bot/vectores_preguntas.json):
//   node herramientas/wiki/probar_busqueda.mjs
import { pathToFileURL } from "node:url";
import { buscarFragmentos, textoConsultaVector, UMBRAL_SIMILITUD_MINIMA } from "../../bot/rag.js";
import INDICE from "../../bot/indice_rag.js";
import { vectoresPreguntas } from "./embeddings.mjs";
import { PREGUNTAS } from "./comparar_modos.mjs";

const PESOS = [0.3, 0.5, 0.7];

const u = content => [{ role: "user", content }];
export const DIRIGIDAS = [
  [["otto2017"], "¿Qué pasaría con los humedales del sur del Perú si en el futuro llueve menos?"],
  [["seasonal-water-storage-bofedal-2023"], "¿Los bofedales funcionan como esponjas que guardan agua y la sueltan a los ríos en la época seca?"],
  [["planas-clarke2020"], "¿Qué pasa con los gases que larga una turbera cuando se tapan las zanjas que la secaban?"],
  [["dangles2017"], "¿Pueden los humedales de montaña servir de alarma temprana del calentamiento en Bolivia?"],
  [["caziani2001"], "¿Qué aves acuáticas viven en las lagunas y vegas de Jujuy, Salta y Catamarca?"],
  [["jhydrol-2022-127687"], "¿Cambia la capacidad del suelo de un bofedal para dejar pasar el agua cuando se lo drena y se lo pastorea mucho?"],
  [["villa2019"], "¿Las partes más altas y secas de una turbera largan menos metano que los pozos más húmedos?"],
  [["benavides2014"], "¿Qué plantas que forman turba en Colombia corren más riesgo si sube la temperatura?"],
  [["preston2003"], "¿Es cierto que los animales de los pastores están arruinando el altiplano de Tarija?"],
  [["de-la-fuente-et-al-2021-long-term-spatiotemporal-variability-in-high-andean-wetl"], "¿Cómo fueron cambiando durante décadas los oasis de las cuencas cerradas del altiplano chileno vistos desde el espacio?"],
  [["earle2003"], "¿Puede formarse turba muy rápido en un lugar tan seco como el borde sur del altiplano?"],
  [["navarro2020", "1-s2-0-s2213305423000152-main-3"], "¿Volver a tener grandes herbívoros silvestres en la Puna mejora la biodiversidad?"],
].map(([ids, q]) => ({ ids, mensajes: u(q) }));

// Preguntas cortas del tema: no deben caer bajo el umbral de "fuera de tema".
export const CORTAS = ["¿Qué es un bofedal?", "vicuñas", "¿Hay flamencos en las vegas?", "turba", "litio",
  "¿Qué es una vega?", "¿Dónde hay bofedales?"].map(u);

export const FUERA_DE_TEMA = [
  "¿Cuál es la receta tradicional de pizza napolitana?",
  "¿Quién ganó el mundial de fútbol de 1986?",
  "¿Cómo se hace un pan de masa madre?",
  "¿Cuál es la cotización del dólar hoy?",
  "¿Cómo instalo Python en Windows?",
  "Recomendame una serie para ver el fin de semana",
].map(u);

export const vectoresDe = listaMensajes => vectoresPreguntas(listaMensajes.map(textoConsultaVector));

const nCitas = frs => new Set(frs.flatMap(f => String(f.cita).split("\n").map(s => s.trim()).filter(Boolean))).size;
const INDICE_FRAG = INDICE.fragmentos;

async function main() {
  const todos = [...DIRIGIDAS.map(d => d.mensajes), ...PREGUNTAS.map(p => p.mensajes), ...CORTAS, ...FUERA_DE_TEMA];
  const vecs = await vectoresDe(todos);
  let iv = 0;
  const conf = [{ nombre: "bm25", vector: false }, ...PESOS.map(p => ({ nombre: `híbrida ${p}`, vector: true, peso: p }))];
  const correr = (mensajes, vector, c) => buscarFragmentos(mensajes, c.vector ? { vector, pesoBm25: c.peso } : {});

  console.log("\n## Preguntas dirigidas (estudio esperado entre los enviados; posición)\n");
  console.log(`| Estudio esperado (ficha) | ${conf.map(c => c.nombre).join(" | ")} |`);
  console.log(`|---|${conf.map(() => "---:").join("|")}|`);
  const aciertos = conf.map(() => 0);
  for (const d of DIRIGIDAS) {
    const v = vecs[iv++];
    const celdas = conf.map((c, j) => {
      const frs = correr(d.mensajes, v, c).fragmentos;
      const pos = frs.findIndex(f => d.ids.some(id => f.id.startsWith(`doc:${id}:`)));
      if (pos >= 0) aciertos[j]++;
      return pos >= 0 ? `${pos + 1}` : "—";
    });
    const ref = (INDICE_FRAG.find(f => f.id.startsWith(`doc:${d.ids[0]}:`)) || {}).ref || d.ids[0];
    console.log(`| ${ref} | ${celdas.join(" | ")} |`);
  }
  console.log(`| **Aciertos** | ${aciertos.map(a => `**${a}/${DIRIGIDAS.length}**`).join(" | ")} |`);

  console.log("\n## Banco de comparar_modos: fragmentos / citas distintas enviadas al modelo\n");
  console.log(`| # | Categoría | ${conf.map(c => c.nombre).join(" | ")} | sim. máx |`);
  console.log(`|---:|---|${conf.map(() => "---:").join("|")}|---:|`);
  for (const p of PREGUNTAS) {
    const v = vecs[iv++];
    let simMax = 0;
    const celdas = conf.map(c => {
      const r = correr(p.mensajes, v, c);
      if (c.vector) simMax = r.mejorScore;
      return r.fragmentos.length ? `${r.fragmentos.length} / ${nCitas(r.fragmentos)}` : "sin datos";
    });
    console.log(`| ${p.id} | ${p.categoria} | ${celdas.join(" | ")} | ${simMax.toFixed(3)} |`);
  }

  console.log(`\n## Cortas del tema (umbral de similitud: ${UMBRAL_SIMILITUD_MINIMA})\n`);
  for (const m of CORTAS) {
    const v = vecs[iv++];
    const h = buscarFragmentos(m, { vector: v }), b = buscarFragmentos(m);
    console.log(`- ${m[0].content}  sim. máx = ${h.mejorScore.toFixed(3)} → híbrida: ${h.fragmentos.length} frag.; bm25: ${b.fragmentos.length} frag.`);
  }

  console.log(`\n## Fuera de tema\n`);
  for (const m of FUERA_DE_TEMA) {
    const v = vecs[iv++];
    const h = buscarFragmentos(m, { vector: v }), b = buscarFragmentos(m);
    console.log(`- ${m[0].content}  sim. máx = ${h.mejorScore.toFixed(3)} → híbrida: ${h.fragmentos.length} frag.; bm25: ${b.fragmentos.length} frag. (mejor ${b.mejorScore})`);
  }
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  main().catch(e => { console.error(e); process.exit(1); });
}
