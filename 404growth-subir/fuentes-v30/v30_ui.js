  /* ---------- v30: proposal intelligence on the visit page and in the «Visitas» tab ---------- */
  var TCN = { human_likely: 'Persona (probable)', automation_likely: 'Automático (probable)', security_scanner: 'Escáner de seguridad del correo', link_preview: 'Vista previa de enlace', search_crawler: 'Buscador', unknown: 'Sin clasificar' };
  var DEVN = { m: 'Móvil', t: 'Tablet', d: 'Ordenador' };
  function evText(e) {
    var m = e.m || {}, l = e.l ? '«' + e.l + '»' : '';
    switch (e.y) {
      case 'open': return 'Abre la propuesta';
      case 'res': return 'Vuelve a la misma visita';
      case 'rel': return 'Recarga la página';
      case 'hid': return 'Sale de la pestaña o bloquea el móvil';
      case 'vis': return 'Vuelve a la pestaña';
      case 'idle': return 'Deja de interactuar (30 s quieto)';
      case 'wake': return 'Vuelve a moverse por la página';
      case 'end': return 'Cierra o deja la página';
      case 'sin': return 'Llega a ' + (l || secName({ s: e.s }, 'prop'));
      case 'scr': return 'Ha bajado hasta el ' + e.n + ' %';
      case 'exp': return 'Despliega ' + l;
      case 'col': return 'Pliega ' + l;
      case 'tab': return 'Abre la pestaña ' + l;
      case 'vplay': return 'Reproduce el vídeo ' + l;
      case 'vprog': return 'Vídeo ' + l + ' al ' + e.n + ' %';
      case 'vpause': return 'Pausa el vídeo ' + l + (e.n != null ? ' (al ' + e.n + ' %)' : '');
      case 'vend': return 'Ve entero el vídeo ' + l;
      case 'copy': return 'Copia texto' + (m.len ? ' (' + m.len + ' caracteres; el texto no se guarda)' : '');
      case 'print': return 'Pide imprimir la página';
      case 'share': return 'Pulsa compartir' + (m.ch ? ' (' + m.ch + ')' : '');
      case 'dl': return 'Pide descargar ' + (m.file ? '«' + m.file + '»' : 'un documento') + ' (se pidió; no sabemos si se guardó)';
      case 'form0': return 'Empieza a rellenar un formulario';
      case 'form1': return 'Envía un formulario';
      case 'err': return 'Error en la página: ' + (m.msg || '');
      case 'rerr': return 'No carga ' + (m.res || m.tag || 'un recurso');
      case 'nav': return 'Carga: ' + [m.ttfb != null ? 'respuesta ' + m.ttfb + ' ms' : '', m.lcp ? 'contenido principal ' + (m.lcp / 1000).toFixed(1) + ' s' : '', m.load ? 'completa ' + (m.load / 1000).toFixed(1) + ' s' : '', m.net ? 'red ' + m.net : ''].filter(Boolean).join(' · ');
      case 'resize': return 'Gira la pantalla (' + (m.or || '') + ')';
      case 'fs': return 'Pone pantalla completa';
      default: return e.y;
    }
  }
  var QUIET = { tick: 1, idle: 1, wake: 1, resize: 1 };
  function timeline(v) {
    var L = (v.events || []).filter(function (e) { return !QUIET[e.y] }).map(function (e) { return { t: e.t || 0, o: e.id || 0, html: '<b>' + esc(evText(e)) + '</b>' + (e.s && e.y !== 'sin' ? '<span>' + esc(secName({ s: e.s, sh: '' }, v.kind)) + '</span>' : '') } });
    (v.clicks || []).forEach(function (c, i) { var tg = target(c.h); L.push({ t: c.t || 0, o: 1e9 + i, html: '<b>Pulsa ' + (c.w ? '«' + esc(c.w) + '»' : 'algo') + '</b><span>' + esc(secName(c, v.kind)) + (tg ? ' · ' + esc(tg) : '') + '</span>' }) });
    L.sort(function (a, b) { return a.t - b.t || a.o - b.o });
    if (!L.length) return '<div class="empty">Sin acciones registradas en esta visita. El detalle de acciones se registra desde el contador v3 (27 oct 2026); los clics, desde el 22 oct.</div>';
    return '<ol class="cl">' + L.map(function (x) { return '<li><time>' + clock(x.t) + '</time>' + x.html + '</li>' }).join('') + '</ol>';
  }
  function bars(rows, max) {
    max = Math.max(1, max || Math.max.apply(null, rows.map(function (r) { return r[1] })));
    return '<div class="bars">' + rows.map(function (r) { return '<div class="br"><span>' + esc(r[0]) + '</span><i><b style="width:' + Math.max(2, Math.round(r[1] / max * 100)) + '%"></b></i><em>' + esc(dur(r[1])) + '</em></div>' }).join('') + '</div>';
  }
  function reading(v, labels) {
    if (v.act == null && !v.sd) return '';
    var h = '<h3>Lectura</h3><div class="kv">';
    h += '<div><b>' + esc(dur(v.act || 0)) + '</b><span>activo (pestaña a la vista y moviéndose, o con un vídeo)</span></div>';
    h += '<div><b>' + esc(dur(v.secs)) + '</b><span>con la página a la vista</span></div>';
    h += '<div><b>' + (v.sd || 0) + ' %</b><span>hasta dónde bajó</span></div></div>';
    h += '<div class="scrollbar"><i style="width:' + (v.sd || 0) + '%"></i></div>';
    var ss = v.ss || {}, rows = Object.keys(ss).map(function (k) { return [labels[k] || secName({ s: k }, v.kind), ss[k]] }).sort(function (a, b) { return b[1] - a[1] });
    if (rows.length) h += '<h3>Tiempo activo en cada parte</h3>' + bars(rows.slice(0, 14));
    return h;
  }
  function device(v) {
    if (!v.br && !v.scr && !v.ci) return '<h3>Dispositivo y red</h3><div class="empty">' + esc(place(v)) + '. El detalle del dispositivo y de la red se guarda desde el contador v3 (27 oct 2026).</div>';
    var R = [['Dispositivo', [DEVN[v.dv] || '', v.os, v.br].filter(function (x) { return x && x !== 'Desconocido' }).join(' · ') || 'Desconocido'],
      ['Pantalla', v.scr], ['Idioma', v.lang], ['Zona horaria', v.tz], ['Modo oscuro', v.dk ? 'sí' : (v.br ? 'no' : '')], ['Táctil', v.tch == null ? '' : v.tch ? 'sí (' + v.tch + ' puntos)' : 'no'],
      ['Ubicación aproximada', [v.ci, v.rg, cname(v.cc)].filter(Boolean).join(', ')], ['Red', [v.aso, v.asn ? 'AS' + v.asn : '', v.ipv ? 'IPv' + v.ipv : ''].filter(Boolean).join(' · ')],
      ['Llegó desde', v.ref ? v.ref : ''], ['Cómo la abrió', { navigate: 'con un enlace o escribiendo la dirección', reload: 'recargando', back_forward: 'con atrás/adelante', prerender: 'precargada' }[v.nav] || '']];
    return '<h3>Dispositivo y red</h3><dl class="dv">' + R.filter(function (r) { return r[1] }).map(function (r) { return '<dt>' + esc(r[0]) + '</dt><dd>' + esc(r[1]) + '</dd>' }).join('') + '</dl>' +
      '<p class="fine">La ubicación y la red salen de la conexión (Cloudflare): son aproximadas, no una dirección física, y una IP no identifica a una persona. La IP no se guarda.</p>';
  }
  function traffic(v) {
    var tc = v.tcm || v.tc; if (!tc) return '';
    var cls = tc === 'human_likely' ? 'ok' : tc === 'unknown' ? 'mid' : 'bad';
    return '<h3>Tipo de tráfico</h3><div class="tcard"><span class="tchip ' + cls + '">' + esc(TCN[tc] || tc) + (v.tcm ? ' · corregido a mano' : ' · ' + (v.tcc || 0) + ' % seguro') + '</span>' +
      (v.tcw && !v.tcm ? '<p>' + esc(v.tcw) + '</p>' : '') + '<p class="fine">Es una estimación por señales (navegador, red, interacción), no una prueba.</p>' +
      '<div class="row"><button type="button" class="btn sm" data-vp-tc="human_likely">Es una persona</button><button type="button" class="btn sm" data-vp-tc="automation_likely">Es un robot</button></div></div>';
  }
  function cname(c) { var n = c || ''; try { if (c && window.Intl && Intl.DisplayNames) n = new Intl.DisplayNames(['es'], { type: 'region' }).of(c) || c } catch (e) {} return n }
  function scoreCard(it, slug) {
    if (!it) return '';
    var oc = it.outcome || {}, st = { won: 'Cerrado', meet: 'Reunión pendiente', lost: 'No cerrado' }[oc.stage];
    var lv = it.score >= 70 ? 'hot' : it.score >= 40 ? 'warm' : 'cold';
    var h = '<div class="ic ' + lv + '"><div class="sc"><b>' + it.score + '</b><small>/100</small></div><div><p class="t">Interés en la propuesta' + (st ? ' · <em>' + esc(st) + '</em>' : '') + '</p>' +
      '<p class="c">Fiabilidad ' + esc(it.conf) + '. ' + esc(it.why || '') + '</p>' + (st === 'Cerrado' ? '<p class="c"><b>La venta cerrada manda sobre la puntuación.</b></p>' : '') + '</div></div>';
    if (it.factors && it.factors.length) h += '<ul class="fx">' + it.factors.slice().sort(function (a, b) { return b.pts - a.pts }).map(function (f) { return '<li><em>+' + f.pts + '</em>' + esc(f.txt) + '</li>' }).join('') + '</ul>';
    h += '<p class="fine">Actividad no es intención de compra: puede leerla alguien sin capacidad de decisión. ' + it.visits + (it.visits === 1 ? ' visita' : ' visitas') + ' de personas' + (it.bounces ? ', ' + it.bounces + ' de menos de 5 s sin tocar nada' : '') + (it.robots ? ', ' + it.robots + ' automáticas (no cuentan)' : '') + '.</p>';
    if (it.readers && it.readers.length) h += '<h3>Quién la abre<em>' + it.readers.length + (it.readers.length === 1 ? ' dispositivo' : ' dispositivos') + '</em></h3><ul class="rd">' + it.readers.map(function (r) {
      return '<li><b>' + esc(r.label) + '</b><span class="lvl ' + r.level + '">' + esc({ principal: 'Principal', posible: 'Posible lector adicional', ambiguo: 'Ambiguo' }[r.level]) + '</span><span>' + r.visits + (r.visits === 1 ? ' visita' : ' visitas') + (r.place ? ' · ' + esc(r.place) : '') + ' · ' + esc(r.note) + '</span></li>' }).join('') + '</ul>' +
      (it.simultaneous ? '<p class="fine"><b>Acceso simultáneo:</b> dos dispositivos distintos la tenían abierta a la vez.</p>' : '') + (it.shares ? '<p class="fine"><b>Compartida a propósito:</b> ha pulsado compartir ' + it.shares + (it.shares === 1 ? ' vez' : ' veces') + '.</p>' : '');
    return h;
  }
  function paintV30(d) {
    var v = d.visit, labels = {}; (d.intel && d.intel.sections || []).forEach(function (s) { labels[s.id] = s.label });
    return reading(v, labels) + '<h3>Lo que ha hecho<em>' + ((v.events || []).filter(function (e) { return !QUIET[e.y] }).length + (v.clicks || []).length || '') + '</em></h3>' + timeline(v) + device(v) + traffic(v);
  }

  /* the «Visitas» tab: Visitas · Propuestas · Movimientos · Avisos */
  var M = { mode: 'list', tr: 'h', dev: '', props: null, feed: null, alerts: null, cfg: null, robots: null, at: {} };
  function segHtml() {
    var un = M.alerts ? M.alerts.unseen : 0;
    return '<div class="vseg" role="tablist">' + [['list', 'Visitas'], ['props', 'Propuestas'], ['feed', 'Movimientos'], ['alerts', 'Avisos' + (un ? ' · ' + un : '')]].map(function (x) {
      return '<button type="button" role="tab" data-vm="' + x[0] + '" aria-selected="' + (M.mode === x[0]) + '">' + x[1] + '</button>' }).join('') + '</div>';
  }
  function filt(L) { return L.filter(function (v) { var tc = v.tcm || v.tc; if (M.tr === 'h' && tc && tc !== 'human_likely' && tc !== 'unknown') return false; if (M.dev && (v.dv || v.dev) !== M.dev) return false; return true }) }
  function filtersHtml() {
    return '<div class="vfil"><select data-vf="tr" aria-label="Tipo de tráfico"><option value="h"' + (M.tr === 'h' ? ' selected' : '') + '>Solo personas</option><option value="a"' + (M.tr === 'a' ? ' selected' : '') + '>Todo el tráfico</option></select>' +
      '<select data-vf="dev" aria-label="Dispositivo"><option value="">Todos los dispositivos</option><option value="m"' + (M.dev === 'm' ? ' selected' : '') + '>Móvil</option><option value="t"' + (M.dev === 't' ? ' selected' : '') + '>Tablet</option><option value="d"' + (M.dev === 'd' ? ' selected' : '') + '>Ordenador</option></select></div>';
  }
  function propsHtml() {
    if (!M.props) return '<div class="note">Calculando el interés de cada propuesta…</div>';
    var L = M.props.list || []; if (!L.length) return '<div class="note">Ninguna propuesta abierta en los últimos 60 días.</div>';
    return '<p class="vsec">Ordenadas por interés (0-100). Toca una para ver por qué.</p><div class="vlist">' + L.slice().sort(function (a, b) { return b.score - a.score || b.last - a.last }).map(function (p) {
      var st = { won: 'Cerrado', meet: 'Reunión pendiente', lost: 'No cerrado' }[p.stage];
      return '<button type="button" class="vrow prow" data-vp-slug="' + esc(p.slug) + '"><span class="pscore ' + (p.score >= 70 ? 'hot' : p.score >= 40 ? 'warm' : 'cold') + '">' + p.score + '</span><b>' + esc(p.name) + '</b><span class="w">' + esc(ago(p.last)) + '</span>' +
        '<span>' + esc([st, p.visits + (p.visits === 1 ? ' visita' : ' visitas'), p.returns ? p.returns + (p.returns === 1 ? ' vuelta' : ' vueltas') : '', dur(p.act) + ' activo', p.contacts ? 'ha pulsado contactar' : '', p.possible ? 'posible lector adicional' : '', 'fiabilidad ' + p.conf].filter(Boolean).join(' · ')) + '</span>' +
        (p.top && p.top.length ? '<span class="top">' + esc(p.top.join(' · ')) + '</span>' : '') + '</button>' }).join('') + '</div>';
  }
  function feedHtml() {
    if (!M.feed) return '<div class="note">Cargando los movimientos…</div>';
    var L = (M.feed.items || []).filter(function (x) { return M.tr !== 'h' || x.human }); if (!L.length) return '<div class="note">Sin movimientos en los últimos 3 días.</div>';
    return '<p class="vsec">Últimos 3 días · se actualiza cada 10 s</p><ol class="cl feed">' + L.map(function (x) {
      var txt = x.t === 'c' ? 'Pulsa ' + (x.w ? '«' + x.w + '»' : 'algo') + (target(x.h) ? ' · ' + target(x.h) : '') : evText(x);
      return '<li><time>' + esc(new Date(x.ts).toLocaleTimeString('es-ES', { hour: '2-digit', minute: '2-digit' })) + '</time><b><button type="button" class="lk" data-vp="' + x.vid + '">' + esc(x.name) + '</button>' + (x.web ? ' · su web' : '') + (x.human ? '' : ' · automático') + '</b><span>' + esc(txt) + '</span></li>' }).join('') + '</ol>';
  }
  var AK = { entry: 'Entrada', contact: 'Contacto', meeting: 'Reunión', docs: 'Documento', high: 'Interés alto', reader: 'Otro lector', idle: 'Sin actividad', robot: 'Automático' };
  function alertsHtml() {
    var h = '';
    if (!M.alerts) h += '<div class="note">Cargando los avisos…</div>';
    else if (!(M.alerts.alerts || []).length) h += '<div class="note">Todavía no hay avisos.</div>';
    else h += '<div class="vrowh"><p class="vsec">Últimos avisos</p>' + (M.alerts.unseen ? '<button type="button" class="btn sm" data-va="seen">Marcar como vistos</button>' : '') + '</div><ol class="cl feed">' + M.alerts.alerts.map(function (a) {
      return '<li class="' + (a.seen ? '' : 'new') + '"><time>' + esc(new Date(a.ts).toLocaleDateString('es-ES', { day: 'numeric', month: 'short' })) + '</time><b><a class="lk" href="' + esc(a.url || '#') + '">' + esc(a.title || a.name) + '</a> <span class="ak ' + esc(a.kind) + '">' + esc(AK[a.kind] || a.kind) + '</span>' + (a.pushed ? ' <small>· al móvil</small>' : '') + '</b><span>' + esc(a.body || '') + '</span></li>' }).join('') + '</ol>';
    var c = M.cfg && M.cfg.alerts;
    if (c) {
      var sw = function (k, t, x) { return '<label class="sw2"><input type="checkbox" data-ac="' + k + '"' + (c[k] ? ' checked' : '') + '><span>' + t + (x || '') + '</span></label>' };
      h += '<p class="vsec">Qué te llega al móvil</p><div class="cfgbox">' + sw('entry', 'Cada vez que alguien abre su propuesta (con «es la 2.ª vez»…)') + sw('contact', 'Si pulsa WhatsApp, llamar, email o Instagram') + sw('meeting', 'Si pulsa reservar una reunión') + sw('docs', 'Si descarga, imprime, comparte o envía un formulario') +
        sw('high', 'Si el interés pasa de ', '<input type="number" min="10" max="100" data-ac="highAt" value="' + c.highAt + '" aria-label="Puntuación mínima" class="num"> / 100') + sw('reader', 'Si la abre otro dispositivo desde otra red (posible lector adicional)') +
        sw('idle', 'Si una propuesta abierta lleva sin actividad ', '<input type="number" min="1" max="60" data-ac="idleDays" value="' + c.idleDays + '" aria-label="Días" class="num"> días') +
        '<label class="sw2">Guardar las acciones durante <input type="number" min="30" max="730" data-ac="retDays" value="' + c.retDays + '" class="num" aria-label="Días que se guardan"> días</label>' +
        '<div class="row"><button type="button" class="btn sm" data-va="save">Guardar</button><span class="fine" id="va-msg"></span></div>' +
        '<details><summary>Pesos de la puntuación</summary><div class="wgrid">' + Object.keys(M.cfg.weights).map(function (k) { return '<label>' + esc(WN[k] || k) + '<input type="number" min="0" max="100" step="0.5" data-aw="' + k + '" value="' + M.cfg.weights[k] + '" class="num"></label>' }).join('') + '</div></details></div>';
    }
    var R = M.robots;
    if (R) {
      var raw = R.raw || [], tot = raw.reduce(function (a, r) { return a + r.n }, 0), vv = R.visits || [];
      h += '<p class="vsec">Tráfico automático (30 días)</p><div class="cfgbox"><p class="fine">' + (tot ? tot + ' aperturas de robots por su nombre (vistas previas de WhatsApp, escáneres del correo, buscadores…): ' + raw.slice(0, 8).map(function (r) { return (TCN[r.tc] || r.tc) + ' en ' + r.slug + ' (' + r.n + ')' }).join(', ') + '.' : 'Ningún robot por su nombre.') +
        ' Visitas por tipo: ' + (vv.map(function (x) { return (TCN[x.tc] || 'antes de v3') + ' ' + x.n }).join(' · ') || 'ninguna') + '. Los robots se guardan aparte y nunca cuentan ni avisan.</p></div>';
    }
    return h;
  }
  var WN = { ret: 'Por cada vuelta', retMax: 'Máximo por vueltas', minPts: 'Por minuto activo', minMax: 'Máximo por tiempo', scroll: 'Leerla entera', price: 'Leer lo económico', priceAgain: 'Volver a lo económico', parts: 'Mirar 3+ partes', web: 'Abrir su web nueva', contact: 'Pulsar contactar', meeting: 'Pulsar reunión', docs: 'Por descarga/impresión', docsMax: 'Máximo por documentos', video: 'Ver un vídeo', reader: 'Posible otro lector' };
  function tabHtml() {
    var body = M.mode === 'props' ? propsHtml() : M.mode === 'feed' ? filtersHtml() + feedHtml() : M.mode === 'alerts' ? alertsHtml() : filtersHtml() + listHtml();
    return segHtml() + '<div id="vis-body">' + body + '</div>';
  }
  function loadMode(force) {
    var k = M.mode, t = Date.now(); if (!force && t - (M.at[k] || 0) < 8000) return; M.at[k] = t;
    if (k === 'props') api('visits/intel').then(function (j) { M.props = j; paintList() }, function () {});
    if (k === 'feed') api('visits/feed').then(function (j) { M.feed = j; paintList() }, function () {});
    if (k === 'alerts') { api('visits/alerts').then(function (j) { M.alerts = j; paintList() }, function () {}); api('visits/cfg').then(function (j) { M.cfg = j; paintList() }, function () {}); api('visits/robots').then(function (j) { M.robots = j; paintList() }, function () {}) }
  }
  function post(p, b) { return fetch('/admin/api/' + p, { method: 'POST', headers: { 'x-404': '1', 'content-type': 'application/json' }, body: JSON.stringify(b || {}) }).then(function (r) { return r.json() }) }
  document.addEventListener('click', function (e) {
    var t = e.target.closest('[data-vm],[data-va],[data-vp-tc],[data-vp-del]'); if (!t) return;
    if (t.hasAttribute('data-vm')) { M.mode = t.getAttribute('data-vm'); paintList(); loadMode(true); return }
    if (t.getAttribute('data-va') === 'seen') { post('visits/alerts/seen').then(function () { loadMode(true) }); return }
    if (t.getAttribute('data-va') === 'save') {
      var a = {}, w = {}; document.querySelectorAll('[data-ac]').forEach(function (i) { a[i.getAttribute('data-ac')] = i.type === 'checkbox' ? (i.checked ? 1 : 0) : Number(i.value) });
      document.querySelectorAll('[data-aw]').forEach(function (i) { w[i.getAttribute('data-aw')] = Number(i.value) });
      post('visits/cfg', { alerts: a, weights: w }).then(function (j) { if (j.alerts) { M.cfg.alerts = j.alerts; M.cfg.weights = j.weights; var m = document.getElementById('va-msg'); if (m) m.textContent = 'Guardado.' } else { var m2 = document.getElementById('va-msg'); if (m2) m2.textContent = 'Revisa los números.' } }); return }
    if (t.hasAttribute('data-vp-tc')) { var d = S.data; if (!d || !d.visit) return; post('visit/' + d.visit.id + '/class', { tc: t.getAttribute('data-vp-tc') }).then(function () { load() }); return }
    if (t.hasAttribute('data-vp-del')) { var s = t.getAttribute('data-vp-del'), x = prompt('Esto borra todas las visitas, clics y acciones guardadas de «' + s + '». No se puede deshacer. Escribe ' + s + ' para confirmarlo.');
      if (x === s) post('visits/delete/' + s, { confirm: s }).then(function (j) { alert(j.ok ? 'Borrado: ' + j.visits + ' visitas.' : 'No se ha podido borrar.'); hide(); loadList() }); return }
  });
  document.addEventListener('change', function (e) { var t = e.target; if (t.hasAttribute && t.hasAttribute('data-vf')) { M[t.getAttribute('data-vf')] = t.value; paintList() } });
  setInterval(function () { if (document.visibilityState === 'visible' && document.getElementById('vis-body') && M.mode !== 'list' && M.mode !== 'alerts') loadMode() }, 10000);
