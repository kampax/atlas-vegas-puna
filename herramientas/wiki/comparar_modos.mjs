// Compara modos del bot sobre un banco de 15 preguntas de prueba: "completo" (wiki entera), "rag"
// (solo BM25) e "hibrido-<peso>" (modo rag con búsqueda híbrida BM25 + embeddings y ese peso de BM25).
// Guarda respuestas, citas, verificación de DOI, tokens aproximados y tiempos en un .md.
// Los vectores de las preguntas se piden a Workers AI una sola vez (wiki/_bot/vectores_preguntas.json).
//
// Uso (desde la raíz del repo):
//   node herramientas/wiki/comparar_modos.mjs
//   node herramientas/wiki/comparar_modos.mjs --modos completo,rag,hibrido-0.3,hibrido-0.5,hibrido-0.7
//   node herramientas/wiki/comparar_modos.mjs --url http://localhost:8787/chat
//   node herramientas/wiki/comparar_modos.mjs --salida herramientas/wiki/comparacion_modos.md

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import worker from "../../bot/worker.js";
import { aiPorRest } from "./embeddings.mjs";

const aqui = path.dirname(fileURLToPath(import.meta.url));
const raiz = path.resolve(aqui, "../..");
const dirBot = path.join(raiz, "bot");

function leerDevVars() {
  try {
    return Object.fromEntries(
      fs.readFileSync(path.join(dirBot, ".dev.vars"), "utf8")
        .split(/\r?\n/)
        .map(l => l.match(/^\s*([A-Z_]+)\s*=\s*"?([^"]*)"?\s*$/))
        .filter(Boolean)
        .map(m => [m[1], m[2]])
    );
  } catch { return {}; }
}

const args = process.argv.slice(2);
const argVal = flag => {
  const i = args.indexOf(flag);
  return i >= 0 ? args[i + 1] : null;
};
const URL_EXTERNA = argVal("--url");
const SALIDA = argVal("--salida") || path.join(aqui, "comparacion_modos.md");
const SOLO = argVal("--solo") ? Number(argVal("--solo")) : null;
const MODOS = (argVal("--modos") || "completo,rag,hibrido-0.3").split(",").map(s => s.trim()).filter(Boolean);

const env = {
  MODO: "completo",
  MODELO: "deepseek-flash",
  ORIGENES: "",
  ...leerDevVars(),
  LIMITE_HORA: "0", // sin límite por IP para correr todas las consultas del benchmark
  AI: aiPorRest({ cache: true }),
};
for (const k of ["PROVEEDOR", "GLM_API_KEY", "DEEPSEEK_API_KEY", "GEMINI_API_KEY",
  "MODELO", "MODELO_GEMINI", "MODELO_GLM", "GLM_API_URL", "RESPALDO", "API_URL",
  "RAG_K", "RAG_MAX_TOKENS"]) {
  if (process.env[k]) env[k] = process.env[k];
}

export const PREGUNTAS = [
  {
    id: 1,
    categoria: "Definición",
    mensajes: [{ role: "user", content: "¿Qué es una vega y en qué se diferencia de un bofedal?" }],
  },
  {
    id: 2,
    categoria: "Puna argentina vs. otros países",
    mensajes: [{ role: "user", content: "¿Qué diferencias hay entre los estudios sobre vegas en la Puna argentina y los de Bolivia, Perú o Chile?" }],
  },
  {
    id: 3,
    categoria: "Cifras concretas",
    mensajes: [{ role: "user", content: "¿Cuántas vegas y qué superficie total se registraron en la Puna argentina según la bibliografía?" }],
  },
  {
    id: 4,
    categoria: "Pastoreo",
    mensajes: [{ role: "user", content: "¿Cómo afecta el pastoreo de camélidos y ganado a las vegas y bofedales?" }],
  },
  {
    id: 5,
    categoria: "Agua / Hidrología",
    mensajes: [{ role: "user", content: "¿De dónde proviene el agua que mantiene a las vegas y bofedales?" }],
  },
  {
    id: 6,
    categoria: "Carbono",
    mensajes: [{ role: "user", content: "¿Cuánto carbono orgánico acumulan los suelos de turberas y bofedales andinos?" }],
  },
  {
    id: 7,
    categoria: "Minería / Litio",
    mensajes: [{ role: "user", content: "¿Qué impactos tiene la minería de litio y la extracción de agua sobre las vegas y bofedales?" }],
  },
  {
    id: 8,
    categoria: "Teledetección / Mapeo",
    mensajes: [{ role: "user", content: "¿Qué sensores satelitales e índices se usan para mapear y monitorear vegas altoandinas?" }],
  },
  {
    id: 9,
    categoria: "Vegetación / Cojines",
    mensajes: [{ role: "user", content: "¿Qué especies de plantas en cojín dominan los bofedales y cómo se distribuyen según el ambiente?" }],
  },
  {
    id: 10,
    categoria: "Atlas fotográfico",
    mensajes: [{ role: "user", content: "¿Qué vega tiene más fotografías en el atlas fotográfico y en qué provincia está?" }],
  },
  {
    id: 11,
    categoria: "Cambio climático",
    mensajes: [{ role: "user", content: "¿Cómo afecta el retroceso de glaciares y el cambio climático a estos humedales?" }],
  },
  {
    id: 12,
    categoria: "Repregunta (pastoreo en Chile)",
    mensajes: [
      { role: "user", content: "¿Cómo afecta el pastoreo de camélidos y ganado a las vegas y bofedales?" },
      { role: "assistant", content: "El pastoreo puede mantener la diversidad cuando es moderado o degradar los cojines si es excesivo." },
      { role: "user", content: "¿Y en Chile qué muestran los estudios?" },
    ],
  },
  {
    id: 13,
    categoria: "Repregunta (carbono en Puna arg.)",
    mensajes: [
      { role: "user", content: "¿Cuánto carbono orgánico acumulan los suelos de turberas y bofedales andinos?" },
      { role: "assistant", content: "Las turberas y bofedales andinos concentran altos valores de carbono orgánico en el suelo." },
      { role: "user", content: "¿Y en la Puna argentina hay datos de eso?" },
    ],
  },
  {
    id: 14,
    categoria: "Fuera de tema",
    mensajes: [{ role: "user", content: "¿Cuál es la receta tradicional de pizza napolitana?" }],
  },
  {
    id: 15,
    categoria: "Sin datos en la wiki",
    mensajes: [{ role: "user", content: "¿Cuál fue el caudal exacto del río Loa en enero de 2025 medido por la estación de Calama?" }],
  },
];

function analizarCitas(texto) {
  const citasTexto = [...new Set((texto.match(/\([A-ZÁÉÍÓÚÑ][^()\n]{1,60},\s*\d{4}[a-z]?\)/g) || []))];
  const mFuentes = texto.match(/\n\s*(?:#{1,6}\s*)?\*{0,2}Fuentes:?\*{0,2}:?\s*(?:\n|$)/i);
  const bloqueFuentes = mFuentes ? texto.slice(mFuentes.index + mFuentes[0].length).trim() : "";
  const lineasFuentes = bloqueFuentes
    ? bloqueFuentes.split("\n").map(l => l.replace(/^\s*[-•*]\s*/, "").trim()).filter(Boolean)
    : [];
  const conDoi = lineasFuentes.filter(l => /https?:\/\/doi\.org\/\S+/i.test(l)).length;
  return {
    citasTexto,
    nCitasTexto: citasTexto.length,
    lineasFuentes,
    nFuentes: lineasFuentes.length,
    conDoi,
    doiOk: lineasFuentes.length === 0 ? "N/A" : `${conDoi}/${lineasFuentes.length}`,
  };
}

// "rag" = solo BM25; "hibrido-0.3" = búsqueda híbrida con peso 0,3 para BM25; "completo" = wiki entera.
function parametrosModo(modo) {
  const p = new URLSearchParams();
  const m = /^hibrido(?:-([\d.]+))?$/.exec(modo);
  if (m) {
    p.set("modo", "rag");
    if (m[1]) p.set("peso", m[1]);
  } else {
    p.set("modo", modo);
    if (modo === "rag") p.set("busqueda", "bm25");
  }
  return p;
}

async function consultar(mensajes, modo) {
  const t0 = performance.now();
  let r;
  const params = parametrosModo(modo);
  if (URL_EXTERNA) {
    const u = new URL(URL_EXTERNA);
    for (const [k, v] of params) u.searchParams.set(k, v);
    r = await fetch(u, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ mensajes }),
    });
  } else {
    const req = new Request(`http://localhost:8787/chat?${params}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Origin": "http://localhost:8787",
        "X-Forwarded-For": "127.0.0.1",
      },
      body: JSON.stringify({ mensajes }),
    });
    r = await worker.fetch(req, env);
  }
  const texto = await r.text();
  const ms = Math.round(performance.now() - t0);
  const prov = r.headers.get("X-Proveedor") || (r.ok ? "?" : `HTTP ${r.status}`);
  const tokensIn = Number(r.headers.get("X-Tokens-Entrada") || 0);
  return {
    ok: r.ok,
    status: r.status,
    modo,
    busqueda: r.headers.get("X-Busqueda") || "",
    proveedor: prov,
    tokensIn,
    ms,
    texto: texto.trim(),
    citas: analizarCitas(texto),
  };
}

const dormir = ms => new Promise(res => setTimeout(res, ms));
const PROV_CORTO = { "GLM (Z.AI)": "GLM", "DeepSeek": "DS", "Gemini": "Gem", "sin-contexto": "fija" };

async function main() {
  const lista = SOLO ? PREGUNTAS.slice(0, SOLO) : PREGUNTAS;
  const resultados = [];

  for (const p of lista) {
    const ultima = p.mensajes[p.mensajes.length - 1].content;
    console.log(`\n=== [${p.id}/${lista.length}] ${p.categoria}: ${ultima} ===`);
    const porModo = {};
    for (const modo of MODOS) {
      porModo[modo] = await consultar(p.mensajes, modo);
      const c = porModo[modo];
      console.log(`  ${modo.padEnd(12)} ${c.proveedor}${c.busqueda ? ` (${c.busqueda})` : ""}: ${c.citas.nFuentes} fuentes, ${(c.ms / 1000).toFixed(1)} s`);
      await dormir(400);
    }
    resultados.push({ pregunta: p, porModo });
  }

  // Reporte Markdown
  const ahora = new Date().toISOString().slice(0, 16).replace("T", " ");
  const n = resultados.length || 1;
  const cab = MODOS.map(m => `\`${m}\``).join(" / ");
  const md = [
    `# Comparación de modos: ${MODOS.map(m => `\`${m}\``).join(", ")}`,
    "",
    `- Fecha: ${ahora} UTC`,
    `- Preguntas evaluadas: ${resultados.length}`,
    `- Proveedor configurado: \`${env.PROVEEDOR || "auto"}\` (respaldo: \`${env.RESPALDO || "ninguno"}\`)`,
    "- `rag` = modo rag solo con BM25; `hibrido-X` = modo rag con búsqueda híbrida (X = peso de BM25, el resto embeddings bge-m3).",
    "- Proveedor «fija»: el bot no encontró fragmentos relevantes y dio la respuesta fija sin llamar al modelo.",
    "",
    "## Fuentes citadas por pregunta",
    "",
    `| # | Categoría | ${MODOS.map(m => `\`${m}\``).join(" | ")} |`,
    `|---:|---|${MODOS.map(() => "---:").join("|")}|`,
  ];
  const tot = Object.fromEntries(MODOS.map(m => [m, { fuentes: 0, doi: 0, tok: 0, ms: 0 }]));
  for (const { pregunta: p, porModo } of resultados) {
    md.push(`| ${p.id} | ${p.categoria} | ${MODOS.map(m => porModo[m].citas.nFuentes).join(" | ")} |`);
    for (const m of MODOS) {
      const c = porModo[m];
      tot[m].fuentes += c.citas.nFuentes; tot[m].doi += c.citas.conDoi; tot[m].tok += c.tokensIn; tot[m].ms += c.ms;
    }
  }
  md.push(`| | **Total** | ${MODOS.map(m => `**${tot[m].fuentes}**`).join(" | ")} |`);

  md.push(
    "",
    "## Detalle técnico",
    "",
    `| # | Categoría | Proveedor (${cab}) | Tokens in (${cab}) | Tiempo s (${cab}) | DOI en Fuentes (${cab}) |`,
    "|---:|---|---|---|---|---|",
  );
  for (const { pregunta: p, porModo } of resultados) {
    const col = f => MODOS.map(m => f(porModo[m])).join(" / ");
    md.push(`| ${p.id} | ${p.categoria} | ${col(c => PROV_CORTO[c.proveedor] || c.proveedor)} | ` +
      `${col(c => c.tokensIn.toLocaleString("es-AR"))} | ${col(c => (c.ms / 1000).toFixed(1))} | ${col(c => c.citas.doiOk)} |`);
  }

  md.push("", "## Promedios y totales", "");
  for (const m of MODOS) {
    md.push(`- **\`${m}\`:** ${tot[m].fuentes} fuentes citadas (${(tot[m].fuentes / n).toFixed(1)} por pregunta), ` +
      `DOI ${tot[m].doi}/${tot[m].fuentes}, ~${Math.round(tot[m].tok / n).toLocaleString("es-AR")} tokens de entrada, ` +
      `${(tot[m].ms / n / 1000).toFixed(2)} s promedio`);
  }
  md.push("", "## Detalle por pregunta", "");

  for (const { pregunta: p, porModo } of resultados) {
    const ultima = p.mensajes[p.mensajes.length - 1].content;
    md.push(`### ${p.id}. ${p.categoria}`);
    md.push(`**Pregunta:** ${ultima}`);
    if (p.mensajes.length > 1) md.push(`*(Con historial previo: "${p.mensajes[0].content}")*`);
    md.push("");
    for (const m of MODOS) {
      const c = porModo[m];
      md.push(`#### Modo \`${m}\` (${c.proveedor}${c.busqueda ? `, búsqueda ${c.busqueda}` : ""}, ~${c.tokensIn} tok, ${(c.ms / 1000).toFixed(1)} s, DOI: ${c.citas.doiOk})`);
      md.push("", c.texto, "");
    }
    md.push("---", "");
  }

  fs.writeFileSync(SALIDA, md.join("\n"), "utf8");
  console.log("\n" + md.slice(md.indexOf("## Fuentes citadas por pregunta"), md.indexOf("## Detalle técnico")).join("\n"));
  console.log(`Reporte guardado en: ${SALIDA}`);
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  main().catch(e => {
    console.error(e);
    process.exit(1);
  });
}
