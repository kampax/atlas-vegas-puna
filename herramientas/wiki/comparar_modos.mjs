// Compara MODO="completo" vs MODO="rag" sobre un banco de 15 preguntas de prueba.
// Guarda respuestas, citas, verificación de DOI, tokens aproximados y tiempos en un .md.
//
// Uso (desde la raíz del repo):
//   node herramientas/wiki/comparar_modos.mjs
//   node herramientas/wiki/comparar_modos.mjs --url http://localhost:8787/chat
//   node herramientas/wiki/comparar_modos.mjs --salida herramientas/wiki/comparacion_modos.md

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import worker from "../../bot/worker.js";

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

const env = {
  MODO: "completo",
  MODELO: "deepseek-flash",
  ORIGENES: "",
  ...leerDevVars(),
  LIMITE_HORA: "0", // sin límite por IP para correr las 30 consultas del benchmark
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

async function consultar(mensajes, modo) {
  const t0 = performance.now();
  let r;
  if (URL_EXTERNA) {
    const u = new URL(URL_EXTERNA);
    u.searchParams.set("modo", modo);
    r = await fetch(u, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ mensajes }),
    });
  } else {
    const req = new Request(`http://localhost:8787/chat?modo=${modo}`, {
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
  const modoReal = r.headers.get("X-Modo") || modo;
  const tokensIn = Number(r.headers.get("X-Tokens-Entrada") || 0);
  return {
    ok: r.ok,
    status: r.status,
    modo: modoReal,
    proveedor: prov,
    tokensIn,
    ms,
    texto: texto.trim(),
    citas: analizarCitas(texto),
  };
}

const dormir = ms => new Promise(res => setTimeout(res, ms));

async function main() {
  const lista = SOLO ? PREGUNTAS.slice(0, SOLO) : PREGUNTAS;
  const resultados = [];

  for (const p of lista) {
    const ultima = p.mensajes[p.mensajes.length - 1].content;
    console.log(`\n=== [${p.id}/${lista.length}] ${p.categoria}: ${ultima} ===`);
    const comp = await consultar(p.mensajes, "completo");
    await dormir(400);
    const rag = await consultar(p.mensajes, "rag");
    await dormir(400);
    resultados.push({ pregunta: p, completo: comp, rag });
  }

  // Construir reporte Markdown
  const ahora = new Date().toISOString().slice(0, 16).replace("T", " ");
  const md = [
    `# Comparación de modos: \`completo\` vs \`rag\``,
    "",
    `- Fecha: ${ahora} UTC`,
    `- Preguntas evaluadas: ${resultados.length}`,
    `- Proveedor configurado: \`${env.PROVEEDOR || "auto"}\` (respaldo: \`${env.RESPALDO || "ninguno"}\`)`,
    "",
    "## Tabla resumen",
    "",
    "| # | Categoría | Prov. (comp / rag) | Tokens in (comp / rag) | Tiempo s (comp / rag) | Fuentes (comp / rag) | DOI en Fuentes (comp / rag) |",
    "|---:|---|---|---:|---:|---|---|",
  ];

  let sumTokComp = 0, sumTokRag = 0, sumMsComp = 0, sumMsRag = 0;
  let sumFuentesComp = 0, sumDoiComp = 0, sumFuentesRag = 0, sumDoiRag = 0;

  for (const { pregunta: p, completo: c, rag: r } of resultados) {
    sumTokComp += c.tokensIn; sumTokRag += r.tokensIn;
    sumMsComp += c.ms; sumMsRag += r.ms;
    sumFuentesComp += c.citas.nFuentes; sumDoiComp += c.citas.conDoi;
    sumFuentesRag += r.citas.nFuentes; sumDoiRag += r.citas.conDoi;

    md.push(
      `| ${p.id} | ${p.categoria} | ${c.proveedor} / ${r.proveedor} | ` +
      `${c.tokensIn.toLocaleString("es-AR")} / ${r.tokensIn.toLocaleString("es-AR")} | ` +
      `${(c.ms / 1000).toFixed(1)} / ${(r.ms / 1000).toFixed(1)} | ` +
      `${c.citas.nFuentes} / ${r.citas.nFuentes} | ` +
      `${c.citas.doiOk} / ${r.citas.doiOk} |`
    );
  }

  const n = resultados.length || 1;
  const ahorroTok = sumTokComp ? ((1 - sumTokRag / sumTokComp) * 100).toFixed(1) : "0";
  md.push(
    "",
    "## Promedios y totales",
    "",
    `- **Tokens de entrada promedio:** completo = ${Math.round(sumTokComp / n).toLocaleString("es-AR")} | rag = ${Math.round(sumTokRag / n).toLocaleString("es-AR")} (**${ahorroTok} % menos** en RAG)`,
    `- **Tiempo promedio:** completo = ${(sumMsComp / n / 1000).toFixed(2)} s | rag = ${(sumMsRag / n / 1000).toFixed(2)} s`,
    `- **DOIs en bloque Fuentes:** completo = ${sumDoiComp}/${sumFuentesComp} | rag = ${sumDoiRag}/${sumFuentesRag}`,
    "",
    "## Detalle por pregunta",
    ""
  );

  for (const { pregunta: p, completo: c, rag: r } of resultados) {
    const ultima = p.mensajes[p.mensajes.length - 1].content;
    md.push(`### ${p.id}. ${p.categoria}`);
    md.push(`**Pregunta:** ${ultima}`);
    if (p.mensajes.length > 1) {
      md.push(`*(Con historial previo: "${p.mensajes[0].content}")*`);
    }
    md.push("");
    md.push(`#### Modo \`completo\` (${c.proveedor}, ~${c.tokensIn} tok, ${(c.ms / 1000).toFixed(1)} s, DOI: ${c.citas.doiOk})`);
    md.push("");
    md.push(c.texto);
    md.push("");
    md.push(`#### Modo \`rag\` (${r.proveedor}, ~${r.tokensIn} tok, ${(r.ms / 1000).toFixed(1)} s, DOI: ${r.citas.doiOk})`);
    md.push("");
    md.push(r.texto);
    md.push("");
    md.push("---");
    md.push("");
  }

  fs.writeFileSync(SALIDA, md.join("\n"), "utf8");
  console.log("\n" + md.slice(6, 6 + resultados.length + 10).join("\n"));
  console.log(`\nReporte guardado en: ${SALIDA}`);
}

main().catch(e => {
  console.error(e);
  process.exit(1);
});
