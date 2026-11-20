// Intermediario del chat del atlas: recibe la conversación desde la página, agrega el personaje
// y la base de conocimiento (la wiki) y consulta la API de GLM (Z.AI), DeepSeek o Gemini (Google).
// La clave nunca llega al navegador.
//
// Variables (wrangler.toml / .dev.vars):
//   MODO              "rag" (por defecto, recuperación BM25 de fragmentos) o "completo" (wiki entera)
//   RAG_K             opcional (modo rag): máximo de fragmentos a enviar (por defecto 8)
//   RAG_MAX_TOKENS    opcional (modo rag): tope aproximado de tokens de contexto (por defecto 6000)
//   PROVEEDOR         "glm", "deepseek" o "gemini". Si falta, se usa el que tenga clave
//                     (en ese orden: GLM, DeepSeek, Gemini).
//   RESPALDO          proveedores a probar, en orden, si el principal falla o está saturado
//                     (separados por coma, p. ej. "deepseek"). Vacío = sin respaldo.
//   GLM_API_KEY       secreta: `npx wrangler secret put GLM_API_KEY` (z.ai, sección API Keys)
//   DEEPSEEK_API_KEY  secreta: `npx wrangler secret put DEEPSEEK_API_KEY`
//   GEMINI_API_KEY    secreta: `npx wrangler secret put GEMINI_API_KEY` (aistudio.google.com/apikey)
//   ORIGENES          orígenes permitidos separados por coma (p. ej. https://kampax.github.io)
//   MODELO            modelo de DeepSeek: deepseek-flash (por defecto) o deepseek-v4-pro
//   MODELO_GEMINI     modelo de Gemini: gemini-2.5-flash (por defecto)
//   MODELO_GLM        modelo de Z.AI: glm-4.7-flash (por defecto, gratuito)
//   GLM_API_URL       opcional: otra dirección de Z.AI (p. ej. la del GLM Coding Plan)
//   API_URL           opcional, solo para pruebas con un servicio simulado

import CONOCIMIENTO from "./conocimiento.js";
import { PERSONAJE, REGLA_RAG, RESPUESTA_SIN_DATOS, BLOQUE_ATLAS, PREGUNTA_SOBRE_ATLAS } from "./personaje.js";
import { buscarFragmentos, armarContextoRag, canonicalizarFuentes, RAG_K_DEFECTO, RAG_MAX_TOKENS_DEFECTO } from "./rag.js";

// Los tres servicios hablan el formato de chat de OpenAI (Gemini mediante su capa de compatibilidad),
// así que solo cambian la dirección, la clave, el modelo y cómo se apaga el razonamiento.
const PROVEEDORES = {
  glm: {
    nombre: "GLM (Z.AI)",
    api: env => env.GLM_API_URL || "https://api.z.ai/api/paas/v4/chat/completions",
    clave: env => env.GLM_API_KEY,
    variableClave: "GLM_API_KEY",
    modelo: env => env.MODELO_GLM || "glm-4.7-flash",
    // GLM-4.x permite apagar el razonamiento; los GLM-5.3 solo regulan cuánto piensan.
    extra: env => /^glm-5\.3/.test(env.MODELO_GLM || "glm-4.7-flash")
      ? { reasoning_effort: "low" } : { thinking: { type: "disabled" } },
  },
  deepseek: {
    nombre: "DeepSeek",
    api: () => "https://api.deepseek.com/chat/completions",
    clave: env => env.DEEPSEEK_API_KEY,
    variableClave: "DEEPSEEK_API_KEY",
    modelo: env => env.MODELO || "deepseek-flash",
    extra: () => ({ thinking: { type: "disabled" } }),   // respuestas rápidas de chat
  },
  gemini: {
    nombre: "Gemini",
    api: () => "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions",
    clave: env => env.GEMINI_API_KEY,
    variableClave: "GEMINI_API_KEY",
    modelo: env => env.MODELO_GEMINI || "gemini-2.5-flash",
    // 2.5 Flash y Flash-Lite permiten apagar el razonamiento; 2.5 Pro y los Gemini 3, no del todo.
    extra: env => /^gemini-2\.5-flash/.test(env.MODELO_GEMINI || "gemini-2.5-flash")
      ? { reasoning_effort: "none" } : { reasoning_effort: "low" },
  },
};

function elegirProveedor(env) {
  const pedido = (env.PROVEEDOR || "").trim().toLowerCase();
  if (pedido) return PROVEEDORES[pedido] || null;
  if (env.GLM_API_KEY) return PROVEEDORES.glm;
  if (env.DEEPSEEK_API_KEY) return PROVEEDORES.deepseek;
  if (env.GEMINI_API_KEY) return PROVEEDORES.gemini;
  return PROVEEDORES.glm;   // sin ninguna clave: el error lo explica abajo
}

// Si un proveedor falla, se lo saltea un rato para no hacer esperar cada pregunta.
const ENFRIAMIENTO_MS = 2 * 60_000;
const fallidoHasta = new Map();

// Principal + respaldos (de RESPALDO) que tengan clave, sin repetir.
function cadenaProveedores(env) {
  const principal = elegirProveedor(env);
  if (!principal) return { error: `PROVEEDOR desconocido: ${env.PROVEEDOR} (usar glm, deepseek o gemini)` };
  const lista = [principal];
  for (const n of (env.RESPALDO || "").split(",").map(s => s.trim().toLowerCase()).filter(Boolean)) {
    const p = PROVEEDORES[n];
    if (p && !lista.includes(p)) lista.push(p);
  }
  const conClave = lista.filter(p => p.clave(env));
  if (!conClave.length) return { error: `Falta configurar ${principal.variableClave}` };
  // Los que están "enfriándose" van al final (se usan solo si no queda otro).
  const ahora = Date.now();
  const listos = conClave.filter(p => !(fallidoHasta.get(p.nombre) > ahora));
  const enfriando = conClave.filter(p => fallidoHasta.get(p.nombre) > ahora);
  return { lista: [...listos, ...enfriando] };
}

function mensajeError(prov, estado) {
  return estado === 401 || estado === 403 ? `Clave de ${prov.nombre} inválida` :
         estado === 402 ? `La cuenta de ${prov.nombre} no tiene saldo` :
         estado === 429 ? "Demasiadas consultas, probá en un momento" :
         estado === 0 ? "No se pudo conectar con el servicio de respuestas" : "El servicio no respondió";
}
const MAX_MENSAJES = 12;        // historial que se reenvía
const MAX_CARACTERES = 1500;    // por mensaje del usuario
const MAX_RESPUESTA = 1500;     // tokens de salida
const LIMITE_HORA_DEFECTO = 20; // preguntas por hora y por IP
const VENTANA_MS = 3600_000;

// Registro en memoria por instancia del Worker (aproximado en Cloudflare, exacto en local).
const usosPorIp = new Map();

function limitarIp(req, env) {
  const limite = env.LIMITE_HORA !== undefined ? Number(env.LIMITE_HORA) : LIMITE_HORA_DEFECTO;
  if (!(limite > 0)) return null;
  const ip = req.headers.get("CF-Connecting-IP")
    || req.headers.get("X-Forwarded-For")?.split(",")[0].trim()
    || "desconocida";
  const ahora = Date.now();
  const desde = ahora - VENTANA_MS;
  if (usosPorIp.size > 1000) {
    for (const [k, lista] of usosPorIp) {
      if (!lista.length || lista[lista.length - 1] <= desde) usosPorIp.delete(k);
    }
  }
  const lista = (usosPorIp.get(ip) || []).filter(t => t > desde);
  if (lista.length >= limite) {
    const esperaSeg = Math.max(1, Math.ceil((lista[0] + VENTANA_MS - ahora) / 1000));
    return { limite, esperaSeg };
  }
  lista.push(ahora);
  usosPorIp.set(ip, lista);
  return null;
}

// Fijo y siempre igual: los tres servicios cachean este prefijo entre preguntas (mucho más barato y rápido).
const SISTEMA = `${PERSONAJE}${BLOQUE_ATLAS}\n\n=== BASE DE CONOCIMIENTO ===\n\n${CONOCIMIENTO}`;
// Prefijo fijo para modo RAG (mantiene el caché del personaje y agrega la regla de fragmentos).
const PERSONAJE_RAG = `${PERSONAJE}${REGLA_RAG}${BLOQUE_ATLAS}`;

const MODOS_VALIDOS = new Set(["completo", "rag"]);

function esLocalhost(req, url) {
  return (url.hostname === "localhost" || url.hostname === "127.0.0.1") && !req.headers.get("CF-Ray");
}

function elegirModo(req, url, env) {
  let pedido = (env.MODO || "rag").trim().toLowerCase();
  // Solo en localhost se permite forzar el modo por pregunta (?modo=rag o cabecera X-Modo-Prueba).
  if (esLocalhost(req, url)) {
    const override = (url.searchParams.get("modo") || req.headers.get("X-Modo-Prueba") || "").trim().toLowerCase();
    if (override) pedido = override;
  }
  if (!MODOS_VALIDOS.has(pedido)) {
    return { error: `MODO desconocido: ${pedido} (usar completo o rag)` };
  }
  return { modo: pedido };
}

function estimarTokensEntrada(sistema, mensajes) {
  let chars = sistema.length;
  for (const m of mensajes) chars += m.content.length + 12;
  return Math.ceil(chars / 4);
}

function cabecerasCors(req, env) {
  const origen = req.headers.get("Origin") || "";
  const permitidos = (env.ORIGENES || "").split(",").map(s => s.trim()).filter(Boolean);
  const ok = permitidos.includes(origen) || /^http:\/\/(localhost|127\.0\.0\.1)(:\d+)?$/.test(origen);
  return ok ? { "Access-Control-Allow-Origin": origen, "Vary": "Origin", "Access-Control-Expose-Headers": "X-Modo, X-Proveedor" } : null;
}

function error(estado, mensaje, cors) {
  return new Response(JSON.stringify({ error: mensaje }), {
    status: estado, headers: { "Content-Type": "application/json; charset=utf-8", ...(cors || {}) },
  });
}

// Valida y limpia el historial que manda la página.
function limpiar(mensajes) {
  if (!Array.isArray(mensajes) || !mensajes.length) return null;
  const ult = mensajes.slice(-MAX_MENSAJES).filter(m =>
    m && (m.role === "user" || m.role === "assistant") && typeof m.content === "string" && m.content.trim());
  while (ult.length && ult[0].role !== "user") ult.shift();   // que empiece con el usuario
  if (!ult.length || ult[ult.length - 1].role !== "user") return null;
  return ult.map(m => ({ role: m.role, content: m.content.slice(0, m.role === "user" ? MAX_CARACTERES : 6000) }));
}

const RE_FUENTES_HEADER = /\n\s*(?:#{1,6}\s*)?\*{0,2}Fuentes:?\*{0,2}:?\s*(?:\n|$)/i;

function extraerDelta(l, estadoUso) {
  if (!l.startsWith("data:")) return "";
  const dato = l.slice(5).trim();
  if (!dato || dato === "[DONE]") return "";
  try {
    const obj = JSON.parse(dato);
    if (obj?.usage?.prompt_tokens && estadoUso) estadoUso.promptTokens = obj.usage.prompt_tokens;
    return obj?.choices?.[0]?.delta?.content || "";
  } catch { /* línea incompleta o de control: se ignora */ }
  return "";
}

// Convierte el stream SSE (formato OpenAI) en texto plano (solo la respuesta, sin razonamiento)
// y reemplaza las citas del bloque final "Fuentes:" por sus citas canónicas de la wiki.
function soloTexto(cuerpo, alTerminar) {
  const dec = new TextDecoder(), enc = new TextEncoder();
  const estadoUso = { promptTokens: null };
  let resto = "";
  let cola = "";
  let enFuentes = false;
  let cabeceraFuentes = "";
  let textoFuentes = "";

  function empujarTexto(t, ctrl) {
    if (!t) return;
    if (enFuentes) {
      textoFuentes += t;
      return;
    }
    cola += t;
    const m = cola.match(RE_FUENTES_HEADER);
    if (m) {
      const antes = cola.slice(0, m.index);
      if (antes) ctrl.enqueue(enc.encode(antes));
      cabeceraFuentes = m[0];
      textoFuentes = cola.slice(m.index + m[0].length);
      cola = "";
      enFuentes = true;
      return;
    }
    // Mantiene una cola corta para no partir "\nFuentes:\n" entre dos trozos del stream.
    const MARGEN = 32;
    if (cola.length > MARGEN) {
      ctrl.enqueue(enc.encode(cola.slice(0, -MARGEN)));
      cola = cola.slice(-MARGEN);
    }
  }

  return cuerpo.pipeThrough(new TransformStream({
    transform(trozo, ctrl) {
      resto += dec.decode(trozo, { stream: true });
      const lineas = resto.split("\n");
      resto = lineas.pop();
      for (const l of lineas) empujarTexto(extraerDelta(l, estadoUso), ctrl);
    },
    flush(ctrl) {
      resto += dec.decode();
      if (resto.trim()) empujarTexto(extraerDelta(resto, estadoUso), ctrl);
      if (enFuentes) {
        const canon = canonicalizarFuentes(textoFuentes);
        ctrl.enqueue(enc.encode(cabeceraFuentes + (canon || textoFuentes)));
      } else if (cola) {
        ctrl.enqueue(enc.encode(cola));
      }
      if (alTerminar) alTerminar(estadoUso.promptTokens);
    },
  }));
}

export default {
  async fetch(req, env) {
    const cors = cabecerasCors(req, env);
    const url = new URL(req.url);
    const local = esLocalhost(req, url);

    if (req.method === "OPTIONS") {
      if (!cors) return new Response(null, { status: 403 });
      const allowHeaders = local ? "Content-Type, X-Modo-Prueba" : "Content-Type";
      return new Response(null, { headers: { ...cors, "Access-Control-Allow-Methods": "POST", "Access-Control-Allow-Headers": allowHeaders, "Access-Control-Max-Age": "86400" } });
    }
    if (url.pathname !== "/chat" || req.method !== "POST") return error(404, "No encontrado", cors);
    if (!cors) return error(403, "Origen no permitido", null);
    const modoRes = elegirModo(req, url, env);
    if (modoRes.error) return error(500, modoRes.error, cors);
    const modo = modoRes.modo;

    const cadena = cadenaProveedores(env);
    if (cadena.error) return error(500, cadena.error, cors);

    let cuerpo;
    try { cuerpo = await req.json(); } catch { return error(400, "JSON inválido", cors); }
    const mensajes = limpiar(cuerpo?.mensajes);
    if (!mensajes) return error(400, "La conversación debe terminar con un mensaje del usuario", cors);

    const bloqueado = limitarIp(req, env);
    if (bloqueado) {
      return new Response(JSON.stringify({ error: `Llegaste al límite de ${bloqueado.limite} preguntas por hora` }), {
        status: 429,
        headers: {
          "Content-Type": "application/json; charset=utf-8",
          "Retry-After": String(bloqueado.esperaSeg),
          ...(cors || {}),
        },
      });
    }

    let sistema = SISTEMA;
    let refs = ["wiki-completa"];
    if (modo === "rag") {
      const k = env.RAG_K ? Number(env.RAG_K) : RAG_K_DEFECTO;
      const maxTokens = env.RAG_MAX_TOKENS ? Number(env.RAG_MAX_TOKENS) : RAG_MAX_TOKENS_DEFECTO;
      const { fragmentos } = buscarFragmentos(mensajes, { k, maxTokens });
      // Sin fragmentos: respuesta fija, salvo que pregunten por el atlas (autoría, contacto, financiamiento...).
      const ultima = mensajes[mensajes.length - 1]?.content || "";
      if (!fragmentos.length && !PREGUNTA_SOBRE_ATLAS.test(ultima)) {
        console.log(`[chat] modo=rag proveedor=sin-contexto tokens_in=0 refs=[]`);
        const cab = {
          "Content-Type": "text/plain; charset=utf-8",
          "Cache-Control": "no-store",
          "X-Modo": "rag",
          "X-Proveedor": "sin-contexto",
          ...(local ? { "X-Tokens-Entrada": "0" } : {}),
          ...cors,
        };
        return new Response(RESPUESTA_SIN_DATOS, { headers: cab });
      }
      refs = [...new Set(fragmentos.map(f => f.ref))];
      sistema = fragmentos.length
        ? `${PERSONAJE_RAG}\n\n=== FRAGMENTOS RELEVANTES ===\n\n${armarContextoRag(fragmentos)}`
        : PERSONAJE_RAG;
    }

    const tokensEst = estimarTokensEntrada(sistema, mensajes);

    // Prueba el principal y, si falla antes de empezar a responder, el siguiente respaldo.
    let ultimo = null;
    for (const prov of cadena.lista) {
      let r;
      try {
        r = await fetch(env.API_URL || prov.api(env), {
          method: "POST",
          headers: { "Content-Type": "application/json", "Authorization": `Bearer ${prov.clave(env)}` },
          body: JSON.stringify({
            model: prov.modelo(env),
            messages: [{ role: "system", content: sistema }, ...mensajes],
            ...prov.extra(env),
            temperature: 0.4,
            max_tokens: MAX_RESPUESTA,
            stream: true,
          }),
        });
      } catch (e) {
        console.log(prov.nombre, "red", e?.message || e);
        r = null;
      }
      if (r && r.ok && r.body) {
        fallidoHasta.delete(prov.nombre);
        console.log(`[chat] modo=${modo} proveedor=${prov.nombre} tokens_in=${tokensEst} (est) refs=${JSON.stringify(refs)}`);
        const cab = {
          "Content-Type": "text/plain; charset=utf-8",
          "Cache-Control": "no-store",
          "X-Modo": modo,
          "X-Proveedor": prov.nombre,
          ...(local ? { "X-Tokens-Entrada": String(tokensEst) } : {}),
          ...cors,
        };
        const stream = soloTexto(r.body, tokensReales => {
          if (tokensReales) {
            console.log(`[chat] modo=${modo} proveedor=${prov.nombre} tokens_in=${tokensReales} (real)`);
          }
        });
        return new Response(stream, { headers: cab });
      }
      if (r) console.log(prov.nombre, r.status, (await r.text().catch(() => "")).slice(0, 500));
      fallidoHasta.set(prov.nombre, Date.now() + ENFRIAMIENTO_MS);
      ultimo = { prov, estado: r ? r.status : 0 };
    }
    return error(502, mensajeError(ultimo.prov, ultimo.estado), cors);
  },
};
