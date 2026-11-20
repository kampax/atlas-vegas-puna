// Búsqueda BM25 en JavaScript puro para el modo RAG del bot "Doña Vicuña".
// Sin dependencias externas: funciona igual en Cloudflare Workers y en servidor-local.mjs.
//
// La normalización y raíz simple deben coincidir con herramientas/wiki/construir.py.

import INDICE from "./indice_rag.js";

const STOPWORDS_ES = new Set([
  "el", "la", "los", "las", "un", "una", "unos", "unas", "de", "del", "al",
  "en", "con", "por", "para", "sin", "sobre", "entre", "hacia", "desde",
  "hasta", "segun", "como", "que", "cual", "cuales", "quien", "quienes",
  "donde", "cuando", "cuanto", "cuanta", "cuantos", "cuantas", "porque",
  "pero", "sino", "aunque", "mientras", "si", "no", "ni", "mas", "muy",
  "tan", "tanto", "todo", "toda", "todos", "todas", "otro", "otra", "otros",
  "otras", "este", "esta", "estos", "estas", "ese", "esa", "esos", "esas",
  "aquel", "aquella", "aquellos", "aquellas", "su", "sus", "mi", "mis",
  "tu", "tus", "nuestro", "nuestra", "nuestros", "nuestras", "nos", "me",
  "te", "se", "le", "les", "lo", "ser", "es", "son", "era", "eran", "fue",
  "fueron", "sido", "estar", "estan", "estaba", "hay", "haber", "ha", "han",
  "habia", "tener", "tiene", "tienen", "hacer", "hace", "hacen", "puede",
  "pueden", "poder", "asi", "tambien", "solo", "ya", "aun", "aqui", "alli",
  "ahi", "bien", "mal", "cada", "uno", "dos", "tres", "vez", "veces", "esto",
  "eso", "aquello", "algo", "nada", "alguien", "nadie", "mucho", "mucha",
  "muchos", "muchas", "poco", "poca", "pocos", "pocas", "mismo", "misma",
  "mismos", "mismas", "bajo", "ante", "tras", "contra", "durante", "mediante",
  "respecto", "acerca", "traves", "menos", "cuyo", "cuya",
  "alguno", "alguna", "algunos", "algunas", "ninguno", "ninguna", "embargo",
  "ademas", "incluso", "luego", "entonces", "pues", "sea", "sean",
]);

const SUFIJOS_ES = [
  "aciones", "iciones", "amiento", "imiento", "idades", "adores", "adoras",
  "ancias", "encias", "acion", "icion", "mente", "ibles", "ables", "ismos",
  "istas", "anzas", "antes", "entes", "ando", "iendo", "ados", "adas",
  "idos", "idas", "ivos", "ivas", "icos", "icas", "osos", "osas", "ales",
  "ares", "eros", "eras", "idad", "able", "ible", "ismo", "ista", "anza",
  "ante", "ente",
];

export function quitarTildes(texto) {
  return String(texto || "")
    .toLowerCase()
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "");
}

export function raizEs(w) {
  if (w.length < 5 || /^\d+$/.test(w)) return w;
  for (const suf of SUFIJOS_ES) {
    if (w.endsWith(suf) && w.length - suf.length >= 3) {
      return w.slice(0, -suf.length);
    }
  }
  if (w.endsWith("ces") && w.length >= 5) return w.slice(0, -3) + "z";
  if (w.endsWith("es") && w.length >= 5 && "lrndjz".includes(w[w.length - 3])) {
    return w.slice(0, -2);
  }
  if (w.endsWith("s") && w.length >= 4 && "aeiou".includes(w[w.length - 2])) {
    return w.slice(0, -1);
  }
  return w;
}

export function tokenizarEs(texto) {
  const limpio = quitarTildes(texto);
  const palabras = limpio.match(/[a-z0-9]{2,}/g) || [];
  const out = [];
  for (const w of palabras) {
    if (STOPWORDS_ES.has(w)) continue;
    const r = raizEs(w);
    if (r.length >= 2 && !STOPWORDS_ES.has(r)) out.push(r);
  }
  return out;
}

// Grupos de sinónimos del dominio (basados en herramientas/wiki/vocabulario.py).
// Evitamos palabras genéricas ("tradicional", "local", "tema") para no disparar falsos positivos.
const GRUPOS_SINONIMOS_CRUDOS = [
  ["vega", "bofedal", "turbera", "humedal", "altoandino", "mallin", "cienaga", "fen", "oqho"],
  ["pastoreo", "ganado", "ganaderia", "camelido", "llama", "alpaca", "vicuna", "oveja", "ovino", "sobrepastoreo", "forraje", "pastura"],
  ["agua", "hidrologia", "hidrologico", "caudal", "vertiente", "manantial", "subterraneo", "acuifero", "freatico", "escorrentia", "glaciar", "deshielo", "nieve", "riego"],
  ["carbono", "cos", "soc", "turba", "organico", "metano", "ch4", "co2", "invernadero", "secuestro"],
  ["mineria", "minero", "litio", "salmuera", "salar", "extraccion", "bombeo"],
  ["teledeteccion", "satelite", "satelital", "ndvi", "sentinel", "landsat", "mapeo", "inventario", "sensor", "radar", "monitoreo"],
  ["climatico", "sequia", "calentamiento", "precipitacion", "aridez"],
  ["vegetacion", "flora", "cojin", "oxychloe", "distichia", "patosia", "juncacea", "ciperacea", "graminea"],
  ["fauna", "flamenco", "vicuna", "guanaco", "anfibio", "macroinvertebrado", "biodiversidad"],
  ["gobernanza", "indigena", "campesino", "acequia", "conservacion", "restauracion"],
  ["fotografia", "fotografico", "atlas", "campana", "gps"],
  ["superficie", "hectarea", "extension", "cobertura"],
];

// Mapa término normalizado -> Set de sinónimos normalizados
const MAPA_SINONIMOS = new Map();
for (const grupo of GRUPOS_SINONIMOS_CRUDOS) {
  const norm = [...new Set(grupo.flatMap(tokenizarEs))];
  for (const t of norm) {
    let s = MAPA_SINONIMOS.get(t);
    if (!s) { s = new Set(); MAPA_SINONIMOS.set(t, s); }
    for (const o of norm) if (o !== t) s.add(o);
  }
}

export const RAG_K_DEFECTO = 8;
export const RAG_MAX_TOKENS_DEFECTO = 6000;
export const UMBRAL_SCORE_MINIMO = 1.5;

/**
 * Construye el vector de pesos de términos de consulta a partir de la última
 * pregunta del usuario y hasta 2 preguntas anteriores (para repreguntas),
 * aplicando expansión de sinónimos solo sobre la pregunta actual con peso menor.
 */
export function construirPesosConsulta(mensajes) {
  const usuarios = (mensajes || [])
    .filter(m => m && m.role === "user" && typeof m.content === "string" && m.content.trim())
    .slice(-3);
  if (!usuarios.length) return { pesos: new Map(), directos: new Set() };

  const ultimaToks = tokenizarEs(usuarios[usuarios.length - 1].content);
  const esRepreguntaCorta = ultimaToks.length < 5;
  const pesosTurno = usuarios.length === 1
    ? [1.0]
    : usuarios.length === 2
      ? [esRepreguntaCorta ? 0.5 : 0.2, 1.0]
      : [esRepreguntaCorta ? 0.25 : 0.1, esRepreguntaCorta ? 0.5 : 0.2, 1.0];

  const pesos = new Map();
  const directos = new Set();

  usuarios.forEach((m, idx) => {
    const wTurno = pesosTurno[idx];
    const toks = idx === usuarios.length - 1 ? ultimaToks : tokenizarEs(m.content);
    for (const t of toks) {
      directos.add(t);
      pesos.set(t, Math.max(pesos.get(t) || 0, wTurno));
    }
  });

  // Expansión de sinónimos sobre los términos de la pregunta actual (peso reducido).
  for (const t of new Set(ultimaToks)) {
    const syns = MAPA_SINONIMOS.get(t);
    if (!syns) continue;
    const wSyn = 0.28;
    for (const s of syns) {
      if ((pesos.get(s) || 0) < wSyn) pesos.set(s, wSyn);
    }
  }

  return { pesos, directos };
}

/**
 * Busca los fragmentos más relevantes con BM25 y respeta k y el tope de tokens.
 */
export function buscarFragmentos(mensajes, opts = {}) {
  const k = Number(opts.k) > 0 ? Number(opts.k) : RAG_K_DEFECTO;
  const maxTokens = Number(opts.maxTokens) > 0 ? Number(opts.maxTokens) : RAG_MAX_TOKENS_DEFECTO;
  const umbral = opts.umbral !== undefined ? Number(opts.umbral) : UMBRAL_SCORE_MINIMO;

  const { pesos, directos } = construirPesosConsulta(mensajes);
  if (!pesos.size || !INDICE.n) return { fragmentos: [], mejorScore: 0 };

  const { k1, b, avgdl, idf, postings, dl, fragmentos } = INDICE;
  const scores = new Float64Array(INDICE.n);
  const directScores = new Float64Array(INDICE.n);

  for (const [term, w] of pesos) {
    const termIdf = idf[term];
    const post = postings[term];
    if (!termIdf || !post) continue;
    const esDirecto = directos.has(term);
    for (let i = 0; i < post.length; i += 2) {
      const docIdx = post[i];
      const tf = post[i + 1];
      const num = tf * (k1 + 1);
      const den = tf + k1 * (1 - b + b * (dl[docIdx] / avgdl));
      const aporte = w * termIdf * (num / den);
      scores[docIdx] += aporte;
      if (esDirecto) directScores[docIdx] += aporte;
    }
  }

  const candidatos = [];
  for (let i = 0; i < INDICE.n; i++) {
    if (scores[i] > 0 && directScores[i] > 0) {
      candidatos.push({ idx: i, score: scores[i], direct: directScores[i] });
    }
  }
  candidatos.sort((a, c) => c.score - a.score);

  const mejorScore = candidatos.length ? candidatos[0].score : 0;
  if (!candidatos.length || mejorScore < umbral) {
    return { fragmentos: [], mejorScore: Math.round(mejorScore * 100) / 100 };
  }

  const elegidos = [];
  const vistos = new Set();
  let tokensAcum = 0;
  for (const c of candidatos) {
    if (elegidos.length >= k) break;
    const f = fragmentos[c.idx];
    if (vistos.has(f.id)) continue;
    const tok = f.tok || Math.ceil((f.texto.length + f.cita.length + 100) / 4);
    if (elegidos.length > 0 && tokensAcum + tok > maxTokens) continue;
    vistos.add(f.id);
    elegidos.push({ ...f, score: Math.round(c.score * 100) / 100 });
    tokensAcum += tok;
  }

  return { fragmentos: elegidos, mejorScore: Math.round(mejorScore * 100) / 100 };
}

/**
 * Formatea los fragmentos recuperados para el mensaje de sistema en modo RAG.
 */
export function armarContextoRag(fragmentos) {
  return fragmentos.map((f, i) => {
    const meta = [];
    if (f.paises?.length) meta.push(`Países: ${f.paises.join(", ")}`);
    if (f.seccion) meta.push(`Sección: ${f.seccion}`);
    const etiquetaCita = f.cita.includes("\n")
      ? `Citas referenciadas:\n${f.cita}`
      : `Cita: ${f.cita}`;
    return [
      `## [${i + 1}] [REF: ${f.ref}] ${f.titulo}`,
      etiquetaCita,
      meta.length ? meta.join(" | ") : null,
      f.texto,
    ].filter(Boolean).join("\n");
  }).join("\n\n---\n\n");
}
