(function () {
  'use strict';
  var C = window.BRIEF, API = '/l/brief', UP = '/l/briefup', MAX = 95 * 1048576;
  var form = document.getElementById('bf'), st = document.getElementById('st'), stT = st.querySelector('span');
  var qs = new URLSearchParams(location.search), K = qs.get('k') || '';
  var LS = 'brief:' + C.id + ':';
  function ls(k, v) { try { if (v === undefined) return localStorage.getItem(LS + k); if (v === null) localStorage.removeItem(LS + k); else localStorage.setItem(LS + k, v); } catch (e) { return null; } }
  if (K) ls('k', K); else { K = ls('k') || ''; if (K) history.replaceState(null, '', location.pathname + '?k=' + encodeURIComponent(K) + location.hash); }
  var Q = {}, ORDER = [];
  C.sections.forEach(function (s) { s.q.forEach(function (q) { q.sec = s.id; Q[q.id] = q; ORDER.push(q.id); }); });
  var dirty = {}, busy = false, timer = null, files = [], sent = null, upd = null;

  /* ---------- leer y escribir los campos ---------- */
  function group(n) { return form.querySelectorAll('input[name="' + n + '"]'); }
  function valOf(key) {
    if (/__p$/.test(key)) { var p = form.elements[key]; return p && p.checked ? 1 : ''; }
    var q = Q[key];
    if (q && (q.type === 'one' || q.type === 'confirm')) { var r = form.querySelector('input[name="' + key + '"]:checked'); return r ? r.value : ''; }
    if (q && q.type === 'many') return [].map.call(form.querySelectorAll('input[name="' + key + '"]:checked'), function (x) { return x.value; });
    var e = form.elements[key]; return e ? e.value : '';
  }
  function setVal(key, v) {
    if (/__p$/.test(key)) { var p = form.elements[key]; if (p) p.checked = !!v; return; }
    var q = Q[key];
    if (q && (q.type === 'one' || q.type === 'confirm' || q.type === 'many')) { var L = [].concat(v || []); [].forEach.call(group(key), function (x) { x.checked = L.indexOf(x.value) >= 0; }); return; }
    var e = form.elements[key]; if (e && document.activeElement !== e) e.value = v == null ? '' : String(v);
  }
  function filled(id) {
    var q = Q[id]; if (q.type === 'files') return files.length > 0;
    if (valOf(id + '__p')) return true;
    var v = valOf(id); return Array.isArray(v) ? v.length > 0 : String(v).trim() !== '';
  }
  function refresh(id) {
    var q = Q[id]; if (!q) return; var box = form.querySelector('[data-q="' + id + '"]'); if (!box) return;
    var v = valOf(id), o = box.querySelector('.oth');
    if (o) { var show = q.type === 'confirm' ? v === 'cambiar' : (Array.isArray(v) ? v.indexOf('Otro') >= 0 : v === 'Otro'); o.hidden = !show; }
    box.classList.toggle('is-pend', !!valOf(id + '__p'));
  }
  function progress() {
    var tot = 0, n = 0;
    C.sections.forEach(function (s) {
      var a = 0; s.q.forEach(function (q) { if (filled(q.id)) a++; });
      tot += s.q.length; n += a;
      var l = document.querySelector('.nav a[href="#' + s.id + '"]'); if (l) { l.querySelector('i').textContent = a + '/' + s.q.length; l.classList.toggle('full', a === s.q.length); }
    });
    document.querySelector('.bar i').style.width = Math.round(n * 100 / tot) + '%';
    document.querySelector('.cnt').textContent = n + ' de ' + tot;
    var sc = document.getElementById('sendc'); if (sc) sc.textContent = n + ' de ' + tot;
  }

  /* ---------- guardar ---------- */
  function status(kind, t) {
    st.className = 'st ' + kind;
    stT.textContent = kind === 'ok' ? 'Guardado' + (t ? ' · ' + new Date(t).toLocaleTimeString('es-ES', { hour: '2-digit', minute: '2-digit' }) : '') :
      kind === 'saving' ? 'Guardando…' : kind === 'off' ? 'Sin conexión: se guardará al volver' : 'Enlace no válido';
  }
  function keep() { ls('q', Object.keys(dirty).length ? JSON.stringify(dirty) : null); }
  function sched(ms) { clearTimeout(timer); timer = setTimeout(save, ms == null ? 700 : ms); }
  function save() {
    if (!K || busy) return;
    var keys = Object.keys(dirty); if (!keys.length) return;
    var set = {}; keys.forEach(function (k) { set[k] = dirty[k]; });
    busy = true; status('saving');
    fetch(API, { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify({ b: C.id, k: K, set: set }) })
      .then(function (r) { if (r.status === 403) throw { key: 1 }; if (!r.ok) throw {}; return r.json(); })
      .then(function (j) { keys.forEach(function (k) { if (dirty[k] === set[k]) delete dirty[k]; }); keep(); busy = false; upd = j.upd; status('ok', j.upd); if (Object.keys(dirty).length) sched(200); })
      .catch(function (e) { busy = false; keep(); if (e && e.key) { gate(); return; } status('off'); sched(5000); });
  }
  function changed(key) {
    var base = key.replace(/(__p|_o)$/, '');
    dirty[key] = valOf(key); keep(); refresh(base); progress(); sched();
  }
  form.addEventListener('input', function (e) { var n = e.target.name; if (!n || e.target.type === 'file') return; if (e.target.type === 'radio' || e.target.type === 'checkbox') return; changed(n); });
  form.addEventListener('change', function (e) { var n = e.target.name; if (!n || e.target.type === 'file') return; changed(n); });
  form.addEventListener('submit', function (e) { e.preventDefault(); });
  window.addEventListener('pagehide', function () { if (Object.keys(dirty).length && K && navigator.sendBeacon) { try { navigator.sendBeacon(API, new Blob([JSON.stringify({ b: C.id, k: K, set: dirty })], { type: 'application/json' })); } catch (e) {} } });

  /* ---------- cargar (y traer lo que hayan escrito otros) ---------- */
  function apply(data) {
    Object.keys(data).forEach(function (k) { if (!(k in dirty)) setVal(k, data[k]); });
    ORDER.forEach(function (id) {
      var q = Q[id];
      ['', '_o', '__p'].forEach(function (s) { var k = id + s; if (!(k in data) && !(k in dirty) && (s !== '_o' || q.other || q.type === 'confirm') && (s !== '__p' || form.elements[k])) setVal(k, s === '' && q.type === 'many' ? [] : ''); });
      refresh(id);
    });
    progress();
  }
  function load(first) {
    if (!K) { gate(); return; }
    fetch(API + '?b=' + encodeURIComponent(C.id) + '&k=' + encodeURIComponent(K), { cache: 'no-store' })
      .then(function (r) { if (r.status === 403 || r.status === 404) throw { key: 1 }; if (!r.ok) throw {}; return r.json(); })
      .then(function (j) {
        if (first) { try { var q = JSON.parse(ls('q') || 'null'); if (q && typeof q === 'object') Object.keys(q).forEach(function (k) { dirty[k] = q[k]; }); } catch (e) {} }
        files = j.files || []; sent = j.sent; upd = j.upd;
        apply(j.data || {});
        Object.keys(dirty).forEach(function (k) { setVal(k, dirty[k]); refresh(k.replace(/(__p|_o)$/, '')); });
        renderFiles(); progress(); sentUi();
        if (Object.keys(dirty).length) sched(300); else status('ok', upd);
      })
      .catch(function (e) { if (e && e.key) { gate(); return; } status('off'); if (first) setTimeout(function () { load(true); }, 6000); });
  }
  document.addEventListener('visibilitychange', function () { if (document.visibilityState === 'visible' && K && !busy) load(false); });
  function gate() { document.getElementById('gate').hidden = false; status('key'); }

  /* ---------- archivos ---------- */
  var fl = document.getElementById('fl'), fin = document.getElementById('fin'), drop = document.getElementById('drop'), queue = [], upping = false;
  function size(n) { return n >= 1048576 ? (n / 1048576).toFixed(n >= 10485760 ? 0 : 1).replace('.', ',') + ' MB' : Math.max(1, Math.round(n / 1024)) + ' KB'; }
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function renderFiles() {
    if (!fl) return;
    fl.innerHTML = files.map(function (f) { return '<li><span class="fn">' + esc(f.name) + '</span><span class="fs">' + size(f.size) + '</span><button type="button" data-rm="' + esc(f.k) + '" aria-label="Quitar ' + esc(f.name) + '">Quitar</button></li>'; }).join('') +
      queue.map(function (u) { return '<li data-up="' + u.id + '"><span class="fn">' + esc(u.f.name) + '</span>' + (u.err ? '<span class="fs err">' + esc(u.err) + '</span>' : '<span class="fp"><i style="width:' + u.p + '%"></i></span><span class="fs">' + size(u.f.size) + '</span>') + '</li>'; }).join('');
    progress();
  }
  function add(list) {
    [].forEach.call(list, function (f) { var u = { id: Math.random().toString(36).slice(2), f: f, p: 0 }; if (f.size > MAX) u.err = 'Pesa más de 95 MB: compártelo por enlace'; else if (!f.size) u.err = 'Archivo vacío'; queue.push(u); });
    renderFiles(); next();
  }
  function next() {
    if (upping) return; var u = queue.filter(function (x) { return !x.err && !x.done; })[0]; if (!u) return;
    if (!K) { gate(); return; }
    upping = true;
    var x = new XMLHttpRequest();
    x.open('PUT', UP + '?b=' + encodeURIComponent(C.id) + '&k=' + encodeURIComponent(K) + '&n=' + encodeURIComponent(u.f.name));
    x.setRequestHeader('content-type', u.f.type || 'application/octet-stream');
    x.upload.onprogress = function (e) { if (e.lengthComputable) { u.p = Math.round(e.loaded * 100 / e.total); var b = fl.querySelector('[data-up="' + u.id + '"] .fp i'); if (b) b.style.width = u.p + '%'; } };
    x.onload = function () {
      upping = false;
      if (x.status === 200) { try { files = JSON.parse(x.responseText).files || files; } catch (e) {} u.done = 1; queue = queue.filter(function (y) { return y !== u; }); status('ok', Date.now()); }
      else u.err = x.status === 413 ? 'Pesa demasiado' : x.status === 409 ? 'No caben más archivos' : x.status === 403 ? 'Enlace no válido' : 'No se pudo subir';
      renderFiles(); next();
    };
    x.onerror = function () { upping = false; u.err = 'Sin conexión'; renderFiles(); next(); };
    x.send(u.f);
  }
  if (fin) {
    fin.addEventListener('change', function () { add(fin.files); fin.value = ''; });
    ['dragenter', 'dragover'].forEach(function (t) { drop.addEventListener(t, function (e) { e.preventDefault(); drop.classList.add('over'); }); });
    ['dragleave', 'drop'].forEach(function (t) { drop.addEventListener(t, function (e) { e.preventDefault(); drop.classList.remove('over'); }); });
    drop.addEventListener('drop', function (e) { if (e.dataTransfer && e.dataTransfer.files) add(e.dataTransfer.files); });
    fl.addEventListener('click', function (e) {
      var b = e.target.closest('[data-rm]'); if (!b) return;
      if (b.getAttribute('data-sure') !== '1') { b.setAttribute('data-sure', '1'); b.textContent = '¿Seguro?'; setTimeout(function () { b.removeAttribute('data-sure'); b.textContent = 'Quitar'; }, 3000); return; }
      fetch(API, { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify({ b: C.id, k: K, a: 'rmfile', f: b.getAttribute('data-rm') }) })
        .then(function (r) { return r.json(); }).then(function (j) { if (j.files) { files = j.files; renderFiles(); } });
    });
  }

  /* ---------- enviar ---------- */
  var sb = document.getElementById('sendb'), sm = document.getElementById('sendm');
  function when(t) { return new Date(t).toLocaleString('es-ES', { day: 'numeric', month: 'long', hour: '2-digit', minute: '2-digit' }); }
  function sentUi() { if (sent) { sm.className = 'done'; sm.textContent = 'Enviado el ' + when(sent) + '. Podéis seguir cambiando cosas: se guardan solas.'; sb.textContent = 'Avisar de nuevo'; } }
  sb.addEventListener('click', function () {
    if (!K) { gate(); return; }
    sb.disabled = true; save();
    fetch(API, { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify({ b: C.id, k: K, a: 'send' }) })
      .then(function (r) { if (!r.ok) throw {}; return r.json(); })
      .then(function (j) { sent = j.sent; sb.disabled = false; sm.className = 'done'; sm.textContent = '¡Recibido! Lo revisamos y os escribimos para cerrar lo que falte.'; sb.textContent = 'Avisar de nuevo'; })
      .catch(function () { sb.disabled = false; sm.className = ''; sm.textContent = 'No se pudo enviar. Revisad la conexión y probad otra vez: lo escrito ya está guardado.'; });
  });
  var cp = document.getElementById('copyl');
  cp.addEventListener('click', function () {
    var t = location.origin + location.pathname + '?k=' + encodeURIComponent(K), ok = function () { cp.textContent = 'Enlace copiado'; setTimeout(function () { cp.textContent = 'Copiar el enlace'; }, 2500); };
    try { navigator.clipboard.writeText(t).then(ok, function () { prompt('Copia el enlace:', t); }); } catch (e) { prompt('Copia el enlace:', t); }
  });

  /* ---------- índice: la sección que se está viendo ---------- */
  var SECS = [].slice.call(document.querySelectorAll('.sec')), NAV = [].slice.call(document.querySelectorAll('.nav a')), cur = '', raf = 0;
  function spy() {
    raf = 0; var y = window.innerHeight * 0.35, id = '';
    SECS.forEach(function (s) { if (s.getBoundingClientRect().top <= y) id = s.id; });
    if (id === cur) return; cur = id;
    NAV.forEach(function (a) { var on = a.getAttribute('href') === '#' + id; a.classList.toggle('on', on); if (on && a.scrollIntoView && window.innerWidth < 1040) { var n = a.parentNode; n.scrollTo({ left: a.offsetLeft - 16, behavior: 'smooth' }); } });
  }
  window.addEventListener('scroll', function () { if (!raf) raf = requestAnimationFrame(spy); }, { passive: true });
  spy();

  ORDER.forEach(refresh); progress(); load(true);
})();
