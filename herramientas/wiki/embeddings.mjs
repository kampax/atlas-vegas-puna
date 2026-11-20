// Embeddings de los fragmentos del modo RAG con Workers AI (bge-m3, multilingüe: el mismo modelo que usa
// el Worker para convertir la pregunta en vector).
//
// Se calculan una sola vez por fragmento y se guardan en wiki/_bot/vectores.json (fuera de git, como la
// wiki), con la huella del texto (sha1 de modelo + texto) como clave: si un fragmento no cambia, su vector
// no se vuelve a pedir. Solo los fragmentos nuevos o modificados van a la API, en lotes de 50.
//
// Uso (lo llama construir.py después de escribir bot/indice_rag.js; también se puede correr solo):
//   node herramientas/wiki/embeddings.mjs            agrega los vectores a bot/indice_rag.js
//   node herramientas/wiki/embeddings.mjs --sin-red  usa solo el caché (los que falten quedan sin vector)
//
// Credenciales (en este orden): CLOUDFLARE_API_TOKEN, o la sesión de `npx wrangler login`.
// Cuenta: CLOUDFLARE_ACCOUNT_ID, account_id de bot/wrangler.toml, o la primera cuenta del token.
// Sin red o sin credenciales el índice queda igual de usable: esos fragmentos se buscan solo por BM25.
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath, pathToFileURL } from "node:url";

export const MODELO = "@cf/baai/bge-m3";
export const DIMS = 1024;
const RAIZ = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const CACHE = path.join(RAIZ, "wiki", "_bot", "vectores.json");
const INDICE = path.join(RAIZ, "bot", "indice_rag.js");
const LOTE = 50;                 // textos por llamada
const LOTE_CARACTERES = 120_000; // la API admite ~60 mil tokens por llamada en total

export const huella = texto => crypto.createHash("sha1").update(MODELO + "\n" + texto).digest("hex").slice(0, 20);

// Texto que se convierte en vector: el título y la sección dan contexto al fragmento.
export const textoParaVector = f => `${f.titulo}\n${f.seccion || ""}\n${f.texto}`.slice(0, 6000);

// int8 + escala: 1 KB por fragmento en vez de 4 KB, con pérdida despreciable para similitud coseno.
export function cuantizar(v) {
  const max = Math.max(...v.map(Math.abs)) || 1;
  const q = Int8Array.from(v, x => Math.round(x / max * 127));
  return { b: Buffer.from(q.buffer).toString("base64"), e: +(max / 127).toPrecision(6) };
}

export function token() {
  if (process.env.CLOUDFLARE_API_TOKEN) return process.env.CLOUDFLARE_API_TOKEN;
  const base = process.env.XDG_CONFIG_HOME || (process.platform === "win32"
    ? path.join(process.env.APPDATA || "", "xdg.config") : path.join(os.homedir(), ".config"));
  for (const dir of [path.join(base, ".wrangler"), path.join(os.homedir(), ".wrangler")]) {
    try {
      const t = /oauth_token\s*=\s*"([^"]+)"/.exec(fs.readFileSync(path.join(dir, "config", "default.toml"), "utf8"));
      if (t) return t[1];
    } catch { /* probar la siguiente ubicación */ }
  }
  return null;
}

let cuentaCache = null;
export async function cuenta(clave) {
  if (cuentaCache) return cuentaCache;
  if (process.env.CLOUDFLARE_ACCOUNT_ID) return (cuentaCache = process.env.CLOUDFLARE_ACCOUNT_ID);
  try {
    const m = /^\s*account_id\s*=\s*"([^"]+)"/m.exec(fs.readFileSync(path.join(RAIZ, "bot", "wrangler.toml"), "utf8"));
    if (m) return (cuentaCache = m[1]);
  } catch { /* sin wrangler.toml */ }
  const r = await fetch("https://api.cloudflare.com/client/v4/accounts", { headers: { Authorization: `Bearer ${clave}` } });
  const j = await r.json().catch(() => ({}));
  if (!r.ok || !j.result?.length) throw new Error(`no se pudo averiguar la cuenta de Cloudflare (${r.status}); definir CLOUDFLARE_ACCOUNT_ID`);
  return (cuentaCache = j.result[0].id);
}

/** Pide a Workers AI (API REST) los vectores de una lista de textos. */
export async function calcular(textos, { progreso = true } = {}) {
  const clave = token();
  if (!clave) throw new Error("faltan credenciales de Cloudflare (npx wrangler login, o CLOUDFLARE_API_TOKEN)");
  const id = await cuenta(clave);
  const salida = [];
  for (let i = 0; i < textos.length;) {
    let fin = i + 1, chars = textos[i].length;
    while (fin < textos.length && fin - i < LOTE && chars + textos[fin].length <= LOTE_CARACTERES) chars += textos[fin++].length;
    const r = await fetch(`https://api.cloudflare.com/client/v4/accounts/${id}/ai/run/${MODELO}`, {
      method: "POST", headers: { Authorization: `Bearer ${clave}`, "Content-Type": "application/json" },
      body: JSON.stringify({ text: textos.slice(i, fin) }),
    });
    const j = await r.json().catch(() => ({}));
    if (!r.ok || !j.success) {
      const motivo = r.status === 401 || r.status === 403
        ? "sesión vencida: ejecutá `npx wrangler login`" : JSON.stringify(j.errors || r.status);
      throw new Error(`Workers AI: ${motivo}`);
    }
    if (j.result?.data?.length !== fin - i) throw new Error("Workers AI devolvió una cantidad de vectores inesperada");
    salida.push(...j.result.data);
    i = fin;
    if (progreso) process.stdout.write(`  embeddings: ${i}/${textos.length}\r`);
  }
  if (progreso && textos.length) process.stdout.write("\n");
  return salida;
}

// Vectores de preguntas ya calculadas (pruebas y comparaciones): evita gastar cupo repitiendo el banco.
const CACHE_PREGUNTAS = path.join(RAIZ, "wiki", "_bot", "vectores_preguntas.json");

/** Vectores de una lista de textos de pregunta, con caché en wiki/_bot/vectores_preguntas.json. */
export async function vectoresPreguntas(textos) {
  let cache = {};
  try { cache = JSON.parse(fs.readFileSync(CACHE_PREGUNTAS, "utf8")); } catch { /* sin caché todavía */ }
  const faltan = [...new Set(textos.filter(t => !cache[huella(t)]))];
  if (faltan.length) {
    const datos = await calcular(faltan, { progreso: false });
    faltan.forEach((t, i) => { cache[huella(t)] = datos[i]; });
    fs.mkdirSync(path.dirname(CACHE_PREGUNTAS), { recursive: true });
    fs.writeFileSync(CACHE_PREGUNTAS, JSON.stringify(cache));
  }
  return textos.map(t => cache[huella(t)]);
}

/**
 * Imitación del binding `AI` del Worker para Node (servidor-local.mjs, comparar_modos.mjs): llama a la
 * API REST con las mismas credenciales. Si no hay credenciales devuelve null y el bot sigue con BM25.
 * Con { cache: true } reutiliza los vectores de preguntas ya calculadas (solo para pruebas).
 */
export function aiPorRest({ cache = false } = {}) {
  if (!token() && !cache) return null;
  return {
    async run(modelo, { text }) {
      if (modelo !== MODELO) throw new Error(`modelo no soportado: ${modelo}`);
      return { data: cache ? await vectoresPreguntas(text) : await calcular(text, { progreso: false }) };
    },
  };
}

function leerCache() {
  try {
    const c = JSON.parse(fs.readFileSync(CACHE, "utf8"));
    if (c.modelo === MODELO) return c;
  } catch { /* sin caché todavía */ }
  return { modelo: MODELO, dims: DIMS, vectores: {} };
}

/**
 * Devuelve { vectores: [{b, e} | null por texto], faltantes, nuevos, error } usando y actualizando el caché.
 * Si no hay red o credenciales, los que falten quedan en null (esos fragmentos solo se buscan por BM25).
 */
export async function vectoresPara(textos, { conRed = true } = {}) {
  const cache = leerCache();
  const claves = textos.map(huella);
  const pedir = [...new Set(claves.filter(c => !cache.vectores[c]))];
  let error = null, nuevos = 0;
  if (pedir.length && conRed) {
    const textoDe = new Map(claves.map((c, i) => [c, textos[i]]));
    try {
      const datos = await calcular(pedir.map(c => textoDe.get(c)));
      pedir.forEach((c, i) => { cache.vectores[c] = cuantizar(datos[i]); });
      nuevos = pedir.length;
    } catch (e) { error = e.message; }
  }
  // Solo se guardan los vectores en uso: el caché no crece con versiones viejas de los textos.
  const usados = Object.fromEntries(claves.filter(c => cache.vectores[c]).map(c => [c, cache.vectores[c]]));
  fs.mkdirSync(path.dirname(CACHE), { recursive: true });
  fs.writeFileSync(CACHE, JSON.stringify({ modelo: MODELO, dims: DIMS, vectores: usados }));
  const vectores = claves.map(c => usados[c] || null);
  return { vectores, faltantes: vectores.filter(v => !v).length, nuevos, error };
}

/** Agrega a bot/indice_rag.js un bloque `vec`: n × DIMS bytes int8 en base64 y una escala por fragmento. */
export async function agregarVectores({ red = true } = {}) {
  const fuente = fs.readFileSync(INDICE, "utf8");
  const m = /^(\/\/[^\n]*\n)?export default (.*);\s*$/s.exec(fuente);
  if (!m) throw new Error("bot/indice_rag.js no tiene el formato esperado");
  const indice = JSON.parse(m[2]);
  const N = indice.fragmentos.length;
  const r = await vectoresPara(indice.fragmentos.map(textoParaVector), { conRed: red });
  const bytes = new Int8Array(N * DIMS), escalas = [];
  r.vectores.forEach((v, i) => {
    if (v) {
      // Ojo: Buffer.from(...).buffer puede ser un bloque compartido; hay que respetar byteOffset.
      const buf = Buffer.from(v.b, "base64");
      bytes.set(new Int8Array(buf.buffer, buf.byteOffset, buf.length), i * DIMS);
    }
    escalas.push(v ? v.e : 0);
  });
  indice.vec = { modelo: MODELO, dims: DIMS, escalas, b64: Buffer.from(bytes.buffer).toString("base64") };
  fs.writeFileSync(INDICE, (m[1] || "") + "export default " + JSON.stringify(indice) + ";\n");
  const aviso = `embeddings ${N - r.faltantes}/${N}` + (r.nuevos ? ` (${r.nuevos} nuevos)` : "")
    + (r.error ? ` — sin calcular los nuevos: ${r.error}` : r.faltantes && !red ? " — sin red: faltan algunos" : "");
  console.log(`indice_rag.js: ${aviso}`);
  return r;
}

if (import.meta.url === pathToFileURL(process.argv[1] || "").href) {
  agregarVectores({ red: !process.argv.includes("--sin-red") }).catch(e => {
    // Nunca rompe el build: el índice ya está escrito y funciona solo con BM25.
    console.warn(`Aviso: no se agregaron vectores (${e.message}); el modo rag usará solo BM25.`);
  });
}
