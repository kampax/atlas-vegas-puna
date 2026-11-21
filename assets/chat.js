// Chat del personaje del atlas. Habla con el intermediario (bot/worker.js), nunca con DeepSeek directo.
// Configuración en index.html: window.CHAT = { url, nombre, saludo }.
// En localhost usa /chat (servidor de bot/servidor-local.mjs); si no hay url, el chat no se muestra.
(function () {
  const cfg = window.CHAT || {};
  const local = /^(localhost|127\.0\.0\.1)$/.test(location.hostname);
  const modoLocal = local ? new URLSearchParams(location.search).get("modo") : null;
  const URL_CHAT = local ? ("/chat" + (modoLocal ? `?modo=${encodeURIComponent(modoLocal)}` : "")) : cfg.url;
  if (!URL_CHAT) return;

  const NOMBRE = cfg.nombre || "Doña Vicuña";
  const SALUDO = cfg.saludo || `¡Hola! Soy ${NOMBRE}. Preguntame sobre vegas y bofedales.`;
  const SUGERENCIAS = cfg.sugerencias || [
    "¿Qué es una vega y en qué se diferencia de un bofedal?",
    "¿Cómo se monitorean las vegas desde el espacio con imágenes satelitales?",
    "¿Cómo afecta el pastoreo a las vegas?",
    "¿De dónde sale el agua de las vegas?",
  ];
  const AVATAR = `<img src="assets/vicuna.jpg" alt="" aria-hidden="true">`;

  const esc = s => s.replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const inline = s => esc(s)
    .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
    .replace(/(^|[^\w*])\*([^*\n]+?)\*(?=[^\w*]|$)/g, "$1<em>$2</em>");

  // Formato mínimo: párrafos, listas con "-", **negrita**, *cursiva* y bloque final de "Fuentes:".
  function formatear(texto) {
    const mFuentes = texto.match(/\n\s*(?:#{1,6}\s*)?\*{0,2}Fuentes:?\*{0,2}:?\s*(?:\n|$)/i);
    const cuerpo = mFuentes ? texto.slice(0, mFuentes.index) : texto;
    const fuentes = mFuentes ? texto.slice(mFuentes.index + mFuentes[0].length) : "";
    // Agrupa líneas consecutivas de lista en <ul>; el resto, en párrafos.
    const bloque = t => {
      let html = "", parrafo = [], items = [];
      const cerrar = () => {
        if (parrafo.length) html += `<p>${parrafo.join("<br>")}</p>`;
        if (items.length) html += `<ul>${items.map(i => `<li>${i}</li>`).join("")}</ul>`;
        parrafo = []; items = [];
      };
      t.trim().split("\n").forEach(l => {
        const item = l.match(/^\s*(?:[-•*]|\d+[.)])\s+(.*)/);
        if (!l.trim()) cerrar();
        else if (item) { if (parrafo.length) cerrar(); items.push(inline(item[1])); }
        else { if (items.length) cerrar(); parrafo.push(inline(l)); }
      });
      cerrar();
      return html;
    };
    let html = bloque(cuerpo || "");
    if (fuentes && fuentes.trim()) {
      html += `<div class="chat-fuentes"><strong>Fuentes</strong>` +
        fuentes.split("\n").map(l => l.replace(/^\s*[-•*]\s*/, "").trim()).filter(Boolean)
          .map(l => `<p>${inline(l).replace(/(https?:\/\/[^\s<]+)/g, '<a href="$1" target="_blank" rel="noopener">$1</a>')}</p>`).join("") + "</div>";
    }
    return html;
  }

  const boton = document.createElement("button");
  boton.className = "chat-boton";
  boton.innerHTML = `<span class="chat-avatar">${AVATAR}</span><span class="chat-etiqueta">Preguntale a ${esc(NOMBRE)}</span>`;
  boton.setAttribute("aria-label", `Abrir el chat con ${NOMBRE}`);

  const panel = document.createElement("section");
  panel.className = "chat-panel";
  panel.hidden = true;
  panel.setAttribute("role", "dialog");
  panel.setAttribute("aria-label", `Chat con ${NOMBRE}`);
  panel.innerHTML = `
    <header class="chat-cabecera">
      <span class="chat-avatar">${AVATAR}</span>
      <div><strong>${esc(NOMBRE)}</strong><span>Responde con la bibliografía sobre vegas y bofedales</span></div>
      <button type="button" data-accion="nueva" title="Empezar de nuevo">Nueva</button>
      <button type="button" data-accion="cerrar" aria-label="Cerrar el chat">✕</button>
    </header>
    <div class="chat-mensajes" aria-live="polite"></div>
    <div class="chat-sugerencias"></div>
    <form class="chat-form">
      <textarea rows="1" maxlength="1500" placeholder="Escribí tu pregunta…" aria-label="Tu pregunta"></textarea>
      <button type="submit">Enviar</button>
    </form>
    <p class="chat-nota">Respuestas generadas por IA a partir de una selección de artículos científicos. Pueden tener errores: verificá en las fuentes citadas. <a href="https://github.com/kampax/atlas-vegas-puna#chatbot-bibliogr%C3%A1fico-do%C3%B1a-vicu%C3%B1a" target="_blank" rel="noopener">Cómo está armado (GitHub)</a>.</p>`;
  document.body.append(boton, panel);

  const lista = panel.querySelector(".chat-mensajes");
  const sug = panel.querySelector(".chat-sugerencias");
  const form = panel.querySelector(".chat-form");
  const campo = form.querySelector("textarea");
  const enviar = form.querySelector("button");
  let historial = [];
  let ocupado = false;
  let controlador = null;

  // Ánimo de Doña Vicuña en la cabecera: pensando (esperando), hablando (llega texto), contenta (terminó).
  let tAnimo = null;
  function animo(estado) {
    clearTimeout(tAnimo);
    panel.classList.remove("pensando", "hablando", "contenta");
    if (!estado) return;
    void panel.offsetWidth;   // reinicia la animación aunque se repita el mismo estado
    panel.classList.add(estado);
    if (estado === "contenta") tAnimo = setTimeout(() => panel.classList.remove("contenta"), 800);
  }

  function burbuja(clase, html) {
    const d = document.createElement("div");
    d.className = "chat-msj " + clase;
    d.innerHTML = html;
    lista.append(d);
    lista.scrollTop = lista.scrollHeight;
    return d;
  }
  function reiniciar() {
    historial = [];
    lista.innerHTML = "";
    burbuja("bot", formatear(SALUDO));
    sug.innerHTML = SUGERENCIAS.map(s => `<button type="button">${esc(s)}</button>`).join("");
    sug.hidden = false;
  }

  async function preguntar(texto) {
    texto = texto.trim();
    if (!texto || ocupado) return;
    ocupado = true;
    controlador = new AbortController();
    enviar.type = "button";
    enviar.textContent = "Detener";
    enviar.classList.add("chat-detener");
    lista.setAttribute("aria-busy", "true");
    sug.hidden = true;
    burbuja("usuario", `<p>${esc(texto)}</p>`);
    historial.push({ role: "user", content: texto });
    const b = burbuja("bot chat-escribiendo", "");
    b.setAttribute("aria-label", "Escribiendo respuesta");
    let respuesta = "";
    let termino = false;
    animo("pensando");
    try {
      const r = await fetch(URL_CHAT, {
        method: "POST", headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ mensajes: historial }),
        signal: controlador.signal,
      });
      if (!r.ok) {
        const e = await r.json().catch(() => ({}));
        throw new Error(e.error || `Error ${r.status}`);
      }
      const prov = r.headers.get("X-Proveedor");
      const modo = r.headers.get("X-Modo");
      const metaHtml = prov
        ? `<div class="chat-meta">${esc(
            (prov === "sin-contexto" ? "Sin consulta al modelo" : `Respondido por ${prov}`) +
            (modo ? ` · modo ${modo}` : "")
          )}</div>`
        : "";
      const lector = r.body.getReader(), dec = new TextDecoder();
      for (;;) {
        const { value, done } = await lector.read();
        if (done) break;
        respuesta += dec.decode(value, { stream: true });
        if (respuesta && !panel.classList.contains("hablando")) animo("hablando");
        b.removeAttribute("aria-label");
        b.innerHTML = formatear(respuesta) + metaHtml;
        lista.scrollTop = lista.scrollHeight;
      }
      if (!respuesta.trim()) throw new Error("No llegó respuesta");
      b.innerHTML = formatear(respuesta) + metaHtml;
      historial.push({ role: "assistant", content: respuesta });
      termino = true;
    } catch (e) {
      if (e.name === "AbortError") {
        if (respuesta.trim()) historial.push({ role: "assistant", content: respuesta });
        else { historial.pop(); b.remove(); }
      } else {
        historial.pop();
        b.remove();
        burbuja("error", `<p>No pude responder: ${esc(e.message)}. Probá de nuevo en un momento.</p>`);
      }
    } finally {
      animo(termino ? "contenta" : null);
      b.classList.remove("chat-escribiendo");
      b.removeAttribute("aria-label");
      lista.setAttribute("aria-busy", "false");
      controlador = null;
      ocupado = false;
      enviar.type = "submit";
      enviar.textContent = "Enviar";
      enviar.classList.remove("chat-detener");
      campo.focus();
    }
  }

  boton.addEventListener("click", () => {
    panel.hidden = false; boton.hidden = true;
    if (window.metrica) window.metrica("abrir-chat", "Abrir el chat");
    if (!lista.childElementCount) reiniciar();
    campo.focus();
  });
  panel.addEventListener("click", e => {
    const a = e.target.closest("[data-accion]")?.dataset.accion;
    if (a === "cerrar") { panel.hidden = true; boton.hidden = false; boton.focus(); }
    if (a === "nueva" && !ocupado) reiniciar();
    const s = e.target.closest(".chat-sugerencias button");
    if (s) preguntar(s.textContent);
  });
  panel.addEventListener("keydown", e => {
    if (e.key === "Escape") { panel.hidden = true; boton.hidden = false; boton.focus(); }
  });
  enviar.addEventListener("click", () => { if (ocupado && controlador) controlador.abort(); });
  form.addEventListener("submit", e => {
    e.preventDefault();
    if (ocupado) return;
    const t = campo.value;
    campo.value = "";
    campo.style.height = "auto";
    preguntar(t);
  });
  campo.addEventListener("keydown", e => {
    if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); form.requestSubmit(); }
  });
  campo.addEventListener("input", () => { campo.style.height = "auto"; campo.style.height = campo.scrollHeight + "px"; });
})();
