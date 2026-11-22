/* Código compartido: datos, fechas, mapas base, marcadores y visor de fotos.
   Cada página define window.BASE (ruta a la raíz del sitio) antes de cargar este archivo. */
(function () {
  const BASE = (window.BASE || '.').replace(/\/$/, '');
  const AUTOR = 'Carlos Javier Navarro';
  const AUTOR_URL = 'https://www.researchgate.net/profile/Carlos-Javier-Navarro';
  const MESES = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto',
    'septiembre', 'octubre', 'noviembre', 'diciembre'];
  const MESES_CORTOS = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic'];
  const ETIQUETAS = {
    agua_superficial: 'Agua superficial',
    ganado: 'Ganado',
    fauna_silvestre: 'Fauna silvestre',
    costra_salina: 'Costra salina',
    infraestructura: 'Infraestructura',
    nieve_hielo: 'Nieve / hielo',
    muestreo_campo: 'Muestreo de campo',
  };
  const TIPOS_TOMA = {
    panoramica_vega: 'Panorámica de vega',
    detalle_vegetacion_suelo: 'Detalle vegetación / suelo',
    fauna_o_ganado: 'Fauna o ganado',
    agua_hidrologia: 'Agua / hidrología',
    trabajo_de_campo: 'Trabajo de campo',
    otro: 'Otro',
  };
  const VERDOR = {
    1: 'Muy seco',
    2: 'Verdor bajo',
    3: 'Verdor medio',
    4: 'Verdor alto',
    5: 'Muy verde',
  };

  const url = {
    foto: id => `${BASE}/fotos/${id}.jpg`,
    mini: id => `${BASE}/miniaturas/${id}.jpg`,
    data: f => `${BASE}/data/${f}`,
  };

  async function cargarDatos() {
    // 'no-cache' revalida con el servidor: tras publicar cambios nadie ve datos viejos
    const [fotos, vegas] = await Promise.all([
      fetch(url.data('fotos.json'), { cache: 'no-cache' }).then(r => r.json()),
      fetch(url.data('vegas_muestreadas.geojson'), { cache: 'no-cache' }).then(r => r.json()),
    ]);
    // El atlas muestra solo fotos ubicadas; una sin coordenadas se ignora en lugar de romper el mapa
    const lista = fotos.fotos.filter(f => f.lat != null && f.lon != null).map((f, i) => ({ ...f, i }));
    return { resumen: fotos.resumen, fotos: lista, vegas: vegas.features };
  }

  function fechaLarga(f) {
    if (!f) return 'Sin fecha';
    const [y, m, d] = f.slice(0, 10).split('-');
    return `${parseInt(d)} de ${MESES[parseInt(m) - 1]} de ${y}`;
  }
  /* 3409 -> «3.409 m s. n. m.» */
  function altitud(m) { return `${Number(m).toLocaleString('es-AR')} m s. n. m.`; }
  function hora(f) { return f && f.length > 10 ? f.slice(11, 16) : ''; }
  function mesAnio(ym) {
    const [y, m] = ym.split('-');
    return `${MESES[parseInt(m) - 1]} de ${y}`;
  }

  /* Agrupa las fotos por campaña (mes y año de la toma). */
  function campanias(fotos) {
    const map = new Map();
    fotos.forEach(f => {
      const k = f.fecha ? f.fecha.slice(0, 7) : 'sin-fecha';
      if (!map.has(k)) map.set(k, []);
      map.get(k).push(f);
    });
    return [...map.entries()].map(([clave, items]) => ({
      clave, items,
      titulo: clave === 'sin-fecha' ? 'Sin fecha' : mesAnio(clave),
      anio: clave.slice(0, 4),
      vegas: [...new Set(items.map(f => f.vega).filter(Boolean))],
    }));
  }

  const capasBase = {
    satelite: () => L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
      maxZoom: 19, attribution: 'Imágenes © Esri, Maxar, Earthstar Geographics' }),
    /* Satélite con nombres y caminos encima (equivalente libre a «Google Hybrid») */
    hibrido: () => L.layerGroup([
      L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
        maxZoom: 19, attribution: 'Imágenes © Esri, Maxar, Earthstar Geographics' }),
      L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Transportation/MapServer/tile/{z}/{y}/{x}', {
        maxZoom: 19, opacity: 0.8 }),
      L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Boundaries_and_Places/MapServer/tile/{z}/{y}/{x}', {
        maxZoom: 19, attribution: 'Etiquetas © Esri' }),
    ]),
    relieve: () => L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
      maxZoom: 17, attribution: '© OpenStreetMap, SRTM · estilo © OpenTopoMap (CC-BY-SA)' }),
    claro: () => L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}', {
      maxZoom: 16, attribution: 'Mapa base © Esri, HERE, Garmin, © OpenStreetMap' }),
  };

  async function capaPoligonos(estilo) {
    const gj = await fetch(url.data('vegas.geojson')).then(r => r.json());
    return L.geoJSON(gj, { style: estilo, interactive: false });
  }

  /* ---------- Visor de fotos (lightbox) ----------
     Marcado común; cada diseño le da estilo con las clases .visor-* */
  /* Texto a identificador de URL: «Punta de la Peña» -> «punta-de-la-pena» */
  function slug(s) {
    return String(s || '').normalize('NFD').replace(/[̀-ͯ]/g, '')
      .toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
  }

  /* Estación del año en el hemisferio sur, a partir de 'AAAA-MM' */
  function estacion(fecha) {
    const m = parseInt((fecha || '').slice(5, 7), 10);
    if (!m) return '';
    return m === 12 || m <= 2 ? 'verano' : m <= 5 ? 'otoño' : m <= 8 ? 'invierno' : 'primavera';
  }

  /* Copia un texto al portapapeles; devuelve true si pudo */
  async function copiar(texto) {
    try { await navigator.clipboard.writeText(texto); return true; } catch (e) {
      const t = document.createElement('textarea');
      t.value = texto; t.style.position = 'fixed'; t.style.opacity = '0';
      document.body.appendChild(t); t.select();
      let ok = false; try { ok = document.execCommand('copy'); } catch (e2) { ok = false; }
      t.remove(); return ok;
    }
  }

  function crearVisor({ alCambiar, alCerrar } = {}) {
    const el = document.createElement('div');
    el.className = 'visor';
    el.setAttribute('role', 'dialog');
    el.setAttribute('aria-modal', 'true');
    el.setAttribute('aria-label', 'Foto ampliada');
    el.hidden = true;
    el.innerHTML = `
      <div class="visor-escena">
        <img class="visor-img" alt="">
        <button class="visor-nav visor-ant" aria-label="Foto anterior">‹</button>
        <button class="visor-nav visor-sig" aria-label="Foto siguiente">›</button>
        <button class="visor-cerrar" aria-label="Cerrar">✕</button>
      </div>
      <div class="visor-pie">
        <div class="visor-texto">
          <p class="visor-titulo"></p>
          <p class="visor-detalle"></p>
          <div class="visor-etiquetas"></div>
          <div class="visor-acciones"></div>
        </div>
        <p class="visor-contador"></p>
      </div>`;
    document.body.appendChild(el);
    let lista = [], idx = 0, foco = null;
    const img = el.querySelector('.visor-img');

    function pintar() {
      const f = lista[idx];
      img.src = url.foto(f.id);
      img.alt = f.vega ? `Vega ${f.vega}, ${fechaLarga(f.fecha)}` : `Foto de campo, ${fechaLarga(f.fecha)}`;
      el.querySelector('.visor-titulo').textContent = f.vega ? `Vega ${f.vega}` : fechaLarga(f.fecha);
      const det = el.querySelector('.visor-detalle');
      det.textContent = `${f.vega ? fechaLarga(f.fecha) + '. ' : ''}${f.altitud ? 'Altitud: ' + altitud(f.altitud) + ' ' : ''}Foto: `;
      const autor = document.createElement('a');
      autor.href = AUTOR_URL; autor.target = '_blank'; autor.rel = 'noopener'; autor.textContent = AUTOR;
      det.append(autor, '.');
      const etqEl = el.querySelector('.visor-etiquetas');
      etqEl.innerHTML = '';
      if (f.tipo_toma && TIPOS_TOMA[f.tipo_toma]) {
        const s = document.createElement('span');
        s.className = 'visor-chip visor-chip-tipo';
        s.textContent = TIPOS_TOMA[f.tipo_toma];
        etqEl.appendChild(s);
      }
      if (f.verdor && VERDOR[f.verdor]) {
        const s = document.createElement('span');
        s.className = 'visor-chip visor-chip-verdor';
        s.textContent = `Verdor ${f.verdor}/5`;
        s.title = `${VERDOR[f.verdor]} (etiqueta asistida por IA)`;
        etqEl.appendChild(s);
      }
      (f.etiquetas || []).forEach(e => {
        if (!ETIQUETAS[e]) return;
        const s = document.createElement('span');
        s.className = 'visor-chip';
        s.textContent = ETIQUETAS[e];
        etqEl.appendChild(s);
      });
      el.querySelector('.visor-contador').textContent = `${idx + 1} de ${lista.length}`;
      const sig = lista[idx + 1];
      if (sig) new Image().src = url.foto(sig.id);
      if (alCambiar) alCambiar(f);
    }
    function abrir(l, i) {
      lista = l; idx = i; foco = document.activeElement;
      if (el.hidden && window.metrica) window.metrica('abrir-visor', 'Abrir el visor de fotos');   // solo al abrirlo, no al cambiar de foto
      el.hidden = false; document.body.classList.add('visor-abierto');
      pintar(); el.querySelector('.visor-cerrar').focus();
    }
    function cerrar() {
      if (el.hidden) return;
      el.hidden = true; document.body.classList.remove('visor-abierto');
      if (foco && document.contains(foco)) foco.focus();
      if (alCerrar) alCerrar();
    }
    function mover(d) { idx = (idx + d + lista.length) % lista.length; pintar(); }
    el.querySelector('.visor-ant').onclick = () => mover(-1);
    el.querySelector('.visor-sig').onclick = () => mover(1);
    el.querySelector('.visor-cerrar').onclick = cerrar;
    el.addEventListener('click', e => { if (e.target === el || e.target.classList.contains('visor-escena')) cerrar(); });
    document.addEventListener('keydown', e => {
      if (el.hidden) return;
      if (e.key === 'Escape') cerrar();
      else if (e.key === 'ArrowRight') mover(1);
      else if (e.key === 'ArrowLeft') mover(-1);
    });
    let x0 = null;
    el.addEventListener('touchstart', e => { x0 = e.touches[0].clientX; }, { passive: true });
    el.addEventListener('touchend', e => {
      if (x0 === null) return;
      const dx = e.changedTouches[0].clientX - x0;
      if (Math.abs(dx) > 50) mover(dx < 0 ? 1 : -1);
      x0 = null;
    });
    return {
      abrir, cerrar,
      get abierto() { return !el.hidden; },
      get actual() { return el.hidden ? null : lista[idx]; },
      acciones: el.querySelector('.visor-acciones'),
    };
  }

  window.Vegas = { BASE, AUTOR, url, cargarDatos, fechaLarga, hora, altitud, mesAnio, campanias,
    capasBase, capaPoligonos, crearVisor, slug, estacion, copiar, MESES, MESES_CORTOS,
    ETIQUETAS, TIPOS_TOMA, VERDOR };
})();
