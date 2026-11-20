// Servidor de prueba: sirve el atlas en http://localhost:8787 y atiende /chat con el mismo
// código del Worker. Las claves (GLM_API_KEY, DEEPSEEK_API_KEY o GEMINI_API_KEY) y PROVEEDOR se leen de
// variables de entorno o de bot/.dev.vars.
//
// Uso (desde la raíz del repo):  node bot/servidor-local.mjs
import http from "node:http";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import worker from "./worker.js";

const aqui = path.dirname(fileURLToPath(import.meta.url));
const raiz = path.resolve(aqui, "..");
const PUERTO = Number(process.env.PUERTO || 8787);

function leerDevVars() {
  try {
    return Object.fromEntries(fs.readFileSync(path.join(aqui, ".dev.vars"), "utf8")
      .split(/\r?\n/).map(l => l.match(/^\s*([A-Z_]+)\s*=\s*"?([^"]*)"?\s*$/)).filter(Boolean).map(m => [m[1], m[2]]));
  } catch { return {}; }
}
const env = { MODO: "rag", MODELO: "deepseek-flash", ORIGENES: "", ...leerDevVars() };
for (const k of ["MODO", "RAG_K", "RAG_MAX_TOKENS", "PROVEEDOR", "GLM_API_KEY", "DEEPSEEK_API_KEY",
  "GEMINI_API_KEY", "MODELO", "MODELO_GEMINI", "MODELO_GLM", "GLM_API_URL", "RESPALDO", "API_URL",
  "LIMITE_HORA"]) {
  if (process.env[k]) env[k] = process.env[k];
}
const modoActivo = (env.MODO || "rag").trim().toLowerCase();
const ACTIVOS = {
  glm: ["GLM (Z.AI)", env.MODELO_GLM || "glm-4.7-flash", "GLM_API_KEY"],
  deepseek: ["DeepSeek", env.MODELO, "DEEPSEEK_API_KEY"],
  gemini: ["Gemini", env.MODELO_GEMINI || "gemini-2.5-flash", "GEMINI_API_KEY"],
};
const elegido = (env.PROVEEDOR || "").toLowerCase()
  || (env.GLM_API_KEY ? "glm" : env.DEEPSEEK_API_KEY ? "deepseek" : env.GEMINI_API_KEY ? "gemini" : "glm");
const [nombreProv, modeloProv, claveProv] = ACTIVOS[elegido] || ["?", "?", "?"];

const TIPOS = { ".html": "text/html; charset=utf-8", ".js": "text/javascript; charset=utf-8", ".css": "text/css",
  ".json": "application/json", ".geojson": "application/json", ".svg": "image/svg+xml", ".png": "image/png",
  ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp", ".ico": "image/x-icon" };

http.createServer(async (req, res) => {
  const url = new URL(req.url, `http://localhost:${PUERTO}`);
  if (url.pathname === "/chat") {
    const trozos = [];
    for await (const t of req) trozos.push(t);
    const headers = new Headers({
      "Content-Type": "application/json",
      "Origin": `http://localhost:${PUERTO}`,
      "X-Forwarded-For": req.socket.remoteAddress || "127.0.0.1",
    });
    if (req.headers["x-modo-prueba"]) headers.set("X-Modo-Prueba", String(req.headers["x-modo-prueba"]));
    const r = await worker.fetch(new Request(url, {
      method: req.method, headers, body: req.method === "POST" ? Buffer.concat(trozos) : undefined }), env);
    res.writeHead(r.status, Object.fromEntries(r.headers));
    if (r.body) for await (const t of r.body) res.write(t);
    return res.end();
  }
  // archivos estáticos del atlas (nunca fuera del repo, nunca la wiki ni el bot)
  const rel = decodeURIComponent(url.pathname === "/" ? "/index.html" : url.pathname);
  const ruta = path.resolve(raiz, "." + rel);
  if (!ruta.startsWith(raiz + path.sep) || /[\\/](wiki|bot|\.git)[\\/]/.test(ruta.slice(raiz.length))) {
    res.writeHead(403); return res.end();
  }
  fs.readFile(ruta, (e, datos) => {
    if (e) { res.writeHead(404); return res.end("No encontrado"); }
    res.writeHead(200, { "Content-Type": TIPOS[path.extname(ruta).toLowerCase()] || "application/octet-stream" });
    res.end(datos);
  });
}).listen(PUERTO, () => {
  console.log(`Atlas con chat en http://localhost:${PUERTO}  (modo: ${modoActivo}; ${nombreProv}, ${modeloProv}` +
    (env.RESPALDO ? `; respaldo: ${env.RESPALDO})` : ")"));
  if (!env[claveProv]) console.log(`Aviso: falta ${claveProv} (variable de entorno o bot/.dev.vars)`);
});
