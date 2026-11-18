/* 404 Growth · la agenda dentro de cada propuesta (18/11/2026)
   El mismo calendario de /book (huecos reales de Google, las mismas 3–5 horas por día y 5 días), metido en la propia propuesta:
   el cliente elige día y hora, deja su nombre, su email y su WhatsApp, y la llamada queda reservada sin salir de la página. Al reservar va a /metodo?c=<lead>,
   que es la página de gracias (v52). La tienda y lo que vende ya se saben por la propuesta: no se preguntan.
   Se monta en <section id="agenda" data-slug data-biz data-sec> (lo pone tools/agenda/patch.py). Un solo archivo para todas:
   cambiar aquí las preguntas o los textos cambia todas las propuestas. */
(function () {
  var root = document.getElementById('agenda'); if (!root || root.__ag) return; root.__ag = 1;
  var d = document, PROD = /(^|\.)404growth\.com$/.test(location.hostname), API = '/l/', TZ = 'Europe/Madrid', WA = '34610594450';
  /* prueba interna: los navegadores marcados con ?interno=1 (el mismo aviso que /book y el contador de visitas; ?interno=0 lo quita)
     hacen todo el recorrido con los huecos reales, pero el servidor no crea nada (dry): ni evento en Google, ni lead, ni CRM, ni aviso */
  var INT = false; try { var iq = /[?&]interno=([01])/.exec(location.search); if (iq) { if (iq[1] === '1') localStorage.setItem('c404int', '1'); else localStorage.removeItem('c404int'); } INT = !!localStorage.getItem('c404int'); } catch (e) {}
  var SLUG = root.getAttribute('data-slug') || '', BIZ = root.getAttribute('data-biz') || '', SEC = root.getAttribute('data-sec') || 'otro';
  function $(id) { return d.getElementById(id); }
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

  var css = '' +
    '.ag{--a:var(--t,#2E7A64);--ad:var(--td,#235F4E);background:var(--cream,#F7F2EE);color:#141110;padding:112px 0 124px;font-family:var(--f,-apple-system,BlinkMacSystemFont,"SF Pro Display","SF Pro Text","Helvetica Neue",Inter,Arial,sans-serif);letter-spacing:-.011em;scroll-margin-top:24px}' +
    '.ag *{box-sizing:border-box}.ag-w{max-width:1080px;margin:0 auto;padding:0 40px}' +
    '.ag-eb{display:inline-flex;align-items:center;gap:8px;font-size:13px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--a)}' +
    '.ag-eb:before{content:"";width:8px;height:8px;border-radius:50%;background:var(--a);box-shadow:0 0 0 4px color-mix(in srgb,var(--a) 18%,transparent)}' +
    '.ag h2{font-size:clamp(40px,5.4vw,68px);letter-spacing:-.05em;line-height:.98;margin:16px 0 16px;font-weight:600}' +
    '.ag h2 span{color:#9C9490}' +
    '.ag-sub{font-size:19px;line-height:1.5;color:#5F5855;max-width:640px;margin:0 0 44px}' +
    '.ag-card{display:grid;grid-template-columns:290px 1fr;background:#fff;border-radius:28px;border:1px solid #ECE5DF;box-shadow:0 30px 70px -40px rgba(20,17,16,.35);overflow:hidden;transition:box-shadow .4s}' +
    '.ag-card.fl{box-shadow:0 0 0 4px color-mix(in srgb,var(--a) 30%,transparent),0 30px 70px -40px rgba(20,17,16,.35)}' +
    '.ag-me{padding:32px 28px;background:#FBF9F7;border-right:1px solid #F0EAE5;display:flex;flex-direction:column;gap:22px}' +
    '.ag-who{display:flex;gap:14px;align-items:center}.ag-who img{width:60px;height:60px;border-radius:50%;object-fit:cover;flex:none}' +
    '.ag-who small{display:block;font-size:12px;color:#9C9490}.ag-who b{display:block;font-size:17px;font-weight:600;letter-spacing:-.02em}.ag-who span{display:block;font-size:13.5px;color:#6E6764}' +
    '.ag-li{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:11px;font-size:14.5px;color:#3B3532}' +
    '.ag-li li{display:flex;gap:10px;align-items:center}.ag-li svg{width:18px;height:18px;flex:none;color:var(--a)}' +
    '.ag-sel{margin:0;padding:16px;border-radius:16px;background:#fff;border:1px solid #ECE5DF;font-size:13.5px;color:#6E6764;line-height:1.45}' +
    '.ag-sel b{display:block;font-size:15.5px;color:#141110;font-weight:600;margin-bottom:3px}' +
    '.ag-main{padding:32px 36px 36px;min-height:430px;position:relative}' +
    '.ag-h{display:flex;justify-content:space-between;align-items:baseline;gap:12px;margin:0 0 14px}.ag-h b{font-size:17px;font-weight:600}.ag-h span{font-size:13px;color:#9C9490}' +
    '.ag-days{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:10px}' +
    '.ag-day,.ag-time,.ag-ch button{appearance:none;-webkit-appearance:none;font:inherit;color:inherit;cursor:pointer;background:#fff;border:1px solid #E6DFDA;transition:border-color .18s,background .18s,color .18s,transform .18s}' +
    '.ag-day{border-radius:18px;padding:13px 4px 11px;display:flex;flex-direction:column;align-items:center;gap:1px;min-width:0}' +
    '.ag-day small{font-size:12px;color:#9C9490;text-transform:capitalize}.ag-day b{font-size:25px;font-weight:600;letter-spacing:-.03em;line-height:1.15}' +
    '.ag-day i{font-style:normal;font-size:11px;color:var(--a);margin-top:3px;white-space:nowrap}' +
    '.ag-day:hover,.ag-time:hover,.ag-ch button:hover{border-color:var(--a)}.ag-day:active,.ag-time:active{transform:scale(.97)}' +
    '.ag-day[aria-selected=true],.ag-time[aria-selected=true]{background:var(--a);border-color:var(--a);color:#fff}' +
    '.ag-day[aria-selected=true] small,.ag-day[aria-selected=true] i{color:rgba(255,255,255,.85)}' +
    '.ag-hrs{margin-top:26px}.ag-times{display:grid;grid-template-columns:repeat(auto-fill,minmax(96px,1fr));gap:10px}' +
    '.ag-time{border-radius:99px;padding:13px 8px;font-size:16px;font-weight:600;font-variant-numeric:tabular-nums}' +
    '.ag-load,.ag-none{display:block;grid-column:1/-1;color:#9C9490;font-size:15px;padding:18px 0}.ag-none a{color:var(--a)}' +
    '.ag-top{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px}' +
    '.ag-back{appearance:none;border:0;background:none;font:inherit;font-size:14px;color:#6E6764;cursor:pointer;padding:6px 0}.ag-back:hover{color:#141110}' +
    '.ag-pn{font-size:13px;color:#9C9490;font-variant-numeric:tabular-nums}' +
    '.ag-bar{height:4px;border-radius:9px;background:#F0EAE5;overflow:hidden;margin-bottom:26px}.ag-bar i{display:block;height:100%;width:33%;background:var(--a);border-radius:9px;transition:width .35s}' +
    '.ag-q{border:0;margin:0;padding:0;min-width:0}.ag-q legend{font-size:clamp(21px,2.3vw,26px);font-weight:600;letter-spacing:-.03em;line-height:1.2;margin:0 0 18px;padding:0}' +
    '.ag-ch{display:grid;grid-template-columns:1fr 1fr;gap:10px}.ag-ch button{border-radius:16px;padding:17px 18px;text-align:left;font-size:16px;font-weight:500}' +
    '.ag-ch button[aria-pressed=true]{border-color:var(--a);background:color-mix(in srgb,var(--a) 9%,#fff);box-shadow:inset 0 0 0 1px var(--a)}' +
    '.ag-f{display:flex;flex-direction:column;gap:7px;margin-bottom:16px}.ag-f label{font-size:13.5px;color:#6E6764}' +
    '.ag-f input{font:inherit;font-size:17px;color:#141110;padding:15px 16px;border-radius:14px;border:1px solid #E1D9D3;background:#fff;outline:none;width:100%;transition:border-color .18s,box-shadow .18s}' +
    '.ag-f input:focus{border-color:var(--a);box-shadow:0 0 0 4px color-mix(in srgb,var(--a) 16%,transparent)}.ag-f input.bad{border-color:#C8482F;box-shadow:0 0 0 4px rgba(200,72,47,.12)}' +
    '.ag-go{appearance:none;border:0;cursor:pointer;font:inherit;display:inline-flex;align-items:center;justify-content:center;gap:12px;width:100%;background:var(--a);color:#fff;font-weight:600;font-size:17px;padding:17px 28px;border-radius:99px;transition:background .2s;margin-top:6px}' +
    '.ag-go:hover{background:var(--ad)}.ag-go[disabled]{opacity:.7;cursor:default}' +
    '.ag-trust{list-style:none;margin:4px 0 16px;padding:0;display:flex;flex-direction:column;gap:7px;font-size:13.5px;color:#6E6764}.ag-trust li:before{content:"✓";color:var(--a);font-weight:700;margin-right:8px}' +
    '.ag-err{margin:0 0 12px;color:#B23E27;font-size:14.5px}.ag-err a{color:inherit}' +
    '.ag-legal{margin:12px 0 0;font-size:12.5px;color:#9C9490;text-align:center}.ag-legal a{color:inherit}' +
    '.ag-alt{margin:22px 0 0;font-size:15px;color:#6E6764}.ag-alt a{color:#141110;font-weight:600}' +
    '.ag-ok{text-align:center;padding:60px 10px}.ag-ok b{display:block;font-size:26px;letter-spacing:-.03em;margin-bottom:6px}.ag-ok span{color:#6E6764}' +
    '.ag-test{display:inline-flex;align-items:center;gap:8px;margin:0 0 18px;padding:7px 12px;border-radius:99px;background:#FFF4D6;color:#7A5300;font-size:13px;font-weight:600}' +
    '.ag [hidden]{display:none!important}' +
    '.wa-fab.ag-off{opacity:0!important;pointer-events:none!important;transform:translateY(16px)!important;transition:opacity .25s,transform .25s!important}' +
    '@media (max-width:860px){.ag{padding:76px 0 84px}.ag-w{padding:0 18px}.ag-sub{font-size:17px;margin-bottom:28px}' +
    '.ag-card{grid-template-columns:1fr;border-radius:24px}.ag-me{border-right:0;border-bottom:1px solid #F0EAE5;padding:20px 20px 18px;gap:14px}' +
    '.ag-who{gap:12px}.ag-who img{width:46px;height:46px}.ag-who small{display:none}.ag-who b{font-size:16px}.ag-who span{font-size:13px}' +
    '.ag-li{flex-direction:row;flex-wrap:wrap;gap:6px 14px;font-size:13px}.ag-li svg{width:16px;height:16px}.ag-card.s2 .ag-li{display:none}' +
    '.ag-sel{padding:11px 14px;border-radius:14px;font-size:12.5px}.ag-sel b{font-size:14.5px;margin-bottom:1px}' +
    '.ag-main{padding:22px 18px 24px;min-height:0}.ag-days{gap:6px}.ag-day{border-radius:14px;padding:10px 2px 9px}.ag-day b{font-size:21px}.ag-day i{font-size:10px}' +
    '.ag-times{grid-template-columns:repeat(3,1fr);gap:8px}.ag-ch{grid-template-columns:1fr}.ag-ch button{padding:15px 16px}}' +
    '@media (prefers-reduced-motion:reduce){.ag *{transition:none!important}}';
  var st = d.createElement('style'); st.textContent = css; d.head.appendChild(st);

  var I = { cal: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4.5" width="18" height="16" rx="3"/><path d="M3 9.5h18M8 3v3M16 3v3"/></svg>',
    vid: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2.5" y="6" width="13" height="12" rx="3"/><path d="M15.5 10.5 21 7.5v9l-5.5-3"/></svg>',
    tag: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12V4.5A1.5 1.5 0 0 1 4.5 3H12l9 9-9 9z"/><circle cx="8" cy="8" r="1.4"/></svg>' };
  var app = root.querySelector('.ag-app') || root;
  app.innerHTML =
    '<div class="ag-card" id="ag-card"><aside class="ag-me"><div class="ag-who"><img src="/christian-hola.jpg" alt="Christian Silva" width="60" height="60" loading="lazy"><div><small>Vas a hablar con</small><b>Christian Silva</b><span>Fundador de 404 Growth</span></div></div>' +
    '<ul class="ag-li"><li>' + I.cal + '30 minutos</li><li>' + I.vid + 'Google Meet</li><li>' + I.tag + 'Precio cerrado, sin compromiso</li></ul>' +
    '<p class="ag-sel" id="ag-sel" hidden></p></aside>' +
    '<div class="ag-main">' + (INT ? '<p class="ag-test">Prueba interna · no se reserva nada ni llega invitación</p>' : '') + '<div id="ag-1"><div class="ag-h"><b>Elige un día</b><span>Hora de España</span></div>' +
    '<div class="ag-days" id="ag-days" role="listbox" aria-label="Días disponibles"><span class="ag-load">Cargando huecos libres…</span></div>' +
    '<div class="ag-hrs" id="ag-hrs" hidden><div class="ag-h"><b id="ag-dl">Elige una hora</b></div><div class="ag-times" id="ag-times" role="listbox" aria-label="Horas disponibles"></div></div></div>' +
    '<form id="ag-2" hidden novalidate><div class="ag-top"><button type="button" class="ag-back" id="ag-back">‹ Atrás</button><span class="ag-pn" id="ag-pn">1 de 2</span></div><div class="ag-bar"><i id="ag-pb"></i></div>' +
    '<fieldset class="ag-q" data-q="1"><legend>¿Cómo te llamas?</legend><div class="ag-f"><label for="ag-name">Tu nombre</label><input id="ag-name" name="name" autocomplete="given-name" maxlength="80" placeholder="Tu nombre" enterkeyhint="next"></div>' +
    '<button class="ag-go" type="button" id="ag-nx">Continuar <span aria-hidden="true">→</span></button></fieldset>' +
    '<fieldset class="ag-q" data-q="2" hidden><legend id="ag-q2">¿Dónde te mando el enlace de la llamada?</legend>' +
    '<div class="ag-f"><label for="ag-email">Email · aquí te llega la invitación con el enlace de Meet</label><input id="ag-email" name="email" type="email" autocomplete="email" maxlength="160" placeholder="tu@email.com"></div>' +
    '<div class="ag-f"><label for="ag-phone">WhatsApp · por si te surge algo y hay que mover la hora</label><input id="ag-phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" maxlength="24" placeholder="600 000 000"></div>' +
    '<ul class="ag-trust"><li>Solo te escribo yo, Christian. Nada de llamadas comerciales.</li><li>No compartimos tus datos con nadie.</li></ul>' +
    '<p class="ag-err" id="ag-err" role="alert" hidden></p><button class="ag-go" type="submit" id="ag-go">Confirmar llamada <span aria-hidden="true">→</span></button>' +
    '<p class="ag-legal">Al confirmar aceptas la <a href="/legal" target="_blank" rel="noopener">política de privacidad</a>.</p></fieldset></form></div></div>' +
    '<p class="ag-alt">¿Prefieres escribir? <a href="https://wa.me/' + WA + '?text=' + encodeURIComponent('Hola Christian, he visto la propuesta de ' + (BIZ || 'mi tienda') + '. ') + '" target="_blank" rel="noopener">Háblame por WhatsApp</a></p>';

  /* ---------- los huecos: los mismos que /book ---------- */
  var SL = [], day = null, pick = null, loaded = false;
  var fD = new Intl.DateTimeFormat('es-ES', { timeZone: TZ, weekday: 'short', day: 'numeric', month: 'short' }), fT = new Intl.DateTimeFormat('es-ES', { timeZone: TZ, hour: '2-digit', minute: '2-digit' }),
    fK = new Intl.DateTimeFormat('en-CA', { timeZone: TZ, year: 'numeric', month: '2-digit', day: '2-digit' }), fL = new Intl.DateTimeFormat('es-ES', { timeZone: TZ, weekday: 'long', day: 'numeric', month: 'long', hour: '2-digit', minute: '2-digit' });
  function demoSlots() { var out = [], t = new Date(); t.setMinutes(0, 0, 0); for (var dd = 1; out.length < 120 && dd < 20; dd++) { var x = new Date(t.getTime() + dd * 864e5), wd = x.getDay(); if (wd === 0 || wd === 6) continue;
    for (var h = 9; h < 18; h++) for (var m = 0; m < 60; m += 30) { if ((h * 7 + m + dd) % 5 === 0) continue; out.push(new Date(Date.UTC(x.getUTCFullYear(), x.getUTCMonth(), x.getUTCDate(), h - 1, m)).toISOString()); } } return out; }
  function noCal(msg) { $('ag-days').innerHTML = '<span class="ag-none">' + msg + ' <a href="https://wa.me/' + WA + '" target="_blank" rel="noopener">Escríbeme por WhatsApp</a> y te doy hueco.</span>'; }
  function load() { if (loaded) return; loaded = true; if (!PROD) { SL = demoSlots(); drawDays(); return; }
    fetch(API + 'slots', { method: 'POST', body: '{}', headers: { 'content-type': 'application/json' } }).then(function (r) { return r.json(); })
      .then(function (j) { SL = (j && j.slots) || []; drawDays(); }).catch(function () { loaded = false; noCal('No se ha podido cargar la agenda.'); }); }
  function hsh(t) { var h = 7; for (var i = 0; i < t.length; i++) h = (h * 31 + t.charCodeAt(i)) | 0; return Math.abs(h); }
  function groups() { var all = {}, g = {}, order = []; SL.forEach(function (iso) { var k = fK.format(new Date(iso)); if (!all[k]) { all[k] = []; order.push(k); } all[k].push(iso); });
    order.forEach(function (k) { var n = 3 + hsh('d' + k) % 3; g[k] = all[k].slice().sort(function (a, b) { return hsh(a) - hsh(b); }).slice(0, n).sort(); }); return { g: g, order: order }; }
  function part(p, t) { return ((p.find(function (x) { return x.type === t; }) || {}).value || '').replace('.', ''); }
  function drawDays() { var G = groups(), box = $('ag-days'); if (!G.order.length) return noCal('Ahora mismo no hay huecos libres.');
    box.innerHTML = G.order.slice(0, 5).map(function (k) { var p = fD.formatToParts(new Date(G.g[k][0]));
      return '<button type="button" class="ag-day" role="option" aria-selected="false" data-k="' + k + '"><small>' + esc(part(p, 'weekday')) + '</small><b>' + esc(part(p, 'day')) + '</b><small>' + esc(part(p, 'month')) + '</small><i>' + G.g[k].length + ' libres</i></button>'; }).join('');
    [].forEach.call(box.children, function (b) { b.onclick = function () { choose(b.getAttribute('data-k')); }; }); $('ag-hrs').hidden = true; }
  function choose(k) { day = k; var hr = $('ag-hrs'), first = hr.hidden, G = groups(), t = G.g[k] || []; hr.hidden = false;
    [].forEach.call($('ag-days').children, function (b) { b.setAttribute('aria-selected', b.getAttribute('data-k') === k); });
    $('ag-dl').textContent = 'Horas libres · ' + fD.format(new Date(t[0] || Date.now())).replace('.', '');
    $('ag-times').innerHTML = t.map(function (iso) { return '<button type="button" class="ag-time" role="option" aria-selected="false" data-t="' + iso + '">' + fT.format(new Date(iso)) + '</button>'; }).join('');
    [].forEach.call($('ag-times').children, function (b) { b.onclick = function () { time(b.getAttribute('data-t')); }; });
    if (first) setTimeout(function () { var r = hr.getBoundingClientRect(); if (r.bottom > innerHeight) scrollBy({ top: Math.min(r.bottom - innerHeight + 24, r.top - 80), behavior: 'smooth' }); }, 60); }
  function cap(t) { return t.charAt(0).toUpperCase() + t.slice(1); }
  function time(iso) { pick = iso; $('ag-sel').innerHTML = '<b>' + esc(cap(fL.format(new Date(iso)))) + '</b>30 min · Google Meet · hora de España'; $('ag-sel').hidden = false;
    $('ag-1').hidden = true; $('ag-2').hidden = false; $('ag-card').classList.add('s2'); q(1); top(); }
  /* sube lo justo para ver la pregunta: por debajo del menú fijo de la propuesta (en el móvil, la parte de las preguntas) */
  function top() { var nav = d.querySelector('.nav'), off = (nav && getComputedStyle(nav).position === 'fixed' ? nav.getBoundingClientRect().bottom : 0) + 14,
    el = innerWidth <= 860 ? root.querySelector('.ag-main') : $('ag-card'), r = el.getBoundingClientRect(); if (r.top < off || r.top > innerHeight * .45) scrollBy({ top: r.top - off, behavior: 'smooth' }); }

  /* ---------- las preguntas: solo el nombre y el contacto. La tienda y lo que vende vienen de la propuesta, y la inversión
     no se pregunta aquí (Chris, 18/11/2026: «dos pasos, sin inversión»; en /book sí se pregunta) ---------- */
  var Q = 1;
  function q(n) { Q = n; [].forEach.call(d.querySelectorAll('.ag-q'), function (x) { x.hidden = +x.getAttribute('data-q') !== n; });
    $('ag-pn').textContent = n + ' de 2'; $('ag-pb').style.width = (n * 50) + '%';
    if (n === 2) { var nm = ($('ag-name').value.trim().split(' ')[0] || ''); $('ag-q2').textContent = (nm ? 'Perfecto, ' + nm.charAt(0).toUpperCase() + nm.slice(1) + '. ' : 'Perfecto. ') + '¿Dónde te mando el enlace de la llamada?'; }
    var f = d.querySelector('.ag-q[data-q="' + n + '"] input'); if (f && innerWidth > 860) try { f.focus({ preventScroll: true }); } catch (e) {}
    if (n > 1) top(); }
  function nx() { var n = $('ag-name'); if (n.value.trim().length < 2) { n.classList.add('bad'); return n.focus(); } q(2); }
  $('ag-nx').onclick = nx; $('ag-name').onkeydown = function (e) { if (e.key === 'Enter') { e.preventDefault(); nx(); } };
  $('ag-back').onclick = function () { if (Q > 1) q(Q - 1); else { $('ag-2').hidden = true; $('ag-1').hidden = false; $('ag-card').classList.remove('s2'); } };
  $('ag-2').addEventListener('input', function (e) { if (e.target.classList) e.target.classList.remove('bad'); if (!this.querySelector('.bad')) $('ag-err').hidden = true; });
  $('ag-2').onsubmit = function (e) { e.preventDefault(); var f = this, err = $('ag-err'); if (Q < 2) { nx(); return; }
    var v = { name: f.name.value.trim(), email: f.email.value.trim(), phone: f.phone.value.trim() }, tel = v.phone.replace(/[^\d+]/g, '');
    var ok = { name: v.name.length >= 2, email: /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v.email), phone: /^\+?\d{9,15}$/.test(tel) }, all = true;
    Object.keys(ok).forEach(function (k) { f[k].classList.toggle('bad', !ok[k]); if (!ok[k]) all = false; });
    if (!ok.name) return q(1);
    if (!all) { err.textContent = !ok.email && v.email ? 'Revisa el email.' : !ok.phone && v.phone ? 'Revisa el número de WhatsApp.' : 'Rellena el email y el WhatsApp, por favor.'; err.hidden = false; return; }
    err.hidden = true; var go = $('ag-go'); go.disabled = true; go.firstChild.textContent = 'Reservando… ';
    var body = { k: '', start: pick, name: v.name, email: v.email, phone: tel, biz: BIZ || 'Tienda de la propuesta ' + SLUG, bud: '', sec: SEC, n: SEC !== 'otro' ? SEC : 'tienda', p: SLUG,
      utm: { utm_source: 'propuesta', utm_medium: 'agenda', utm_campaign: SLUG, utm_content: 'agenda' }, tz: (Intl.DateTimeFormat().resolvedOptions().timeZone || TZ), mc: false, fbp: '', fbc: '', dry: INT ? 1 : 0 };
    var done = function (j) { go.disabled = false; go.firstChild.textContent = 'Confirmar llamada ';
      if (j && j.ok) {
        try { sessionStorage.setItem('c404bk', JSON.stringify({ c: j.id || '', name: v.name.split(' ')[0], email: v.email, start: j.start || pick, join: j.join || '', gcal: j.gcal || '', mailed: !!j.mailed, google: /meet\.google\.com/.test(j.join || ''), fresh: 1 })); } catch (x) {}
        go.disabled = true; go.firstChild.textContent = '¡Reservada! ';
        if (!PROD) { $('ag-2').innerHTML = '<div class="ag-ok"><b>¡Reservada! (prueba)</b><span>En la web real ahora pasaría a la página de gracias: /metodo?c=…</span></div>'; return; }
        setTimeout(function () { location.href = '/metodo' + (j.id ? '?c=' + encodeURIComponent(j.id) : ''); }, 350); return; }
      if (j && j.error === 'taken') { SL = j.slots || SL; err.textContent = 'Esa hora se acaba de ocupar. Elige otra, por favor.'; err.hidden = false;
        setTimeout(function () { $('ag-2').hidden = true; $('ag-1').hidden = false; $('ag-card').classList.remove('s2'); drawDays(); }, 1400); return; }
      err.innerHTML = 'No se ha podido reservar. <a href="https://wa.me/' + WA + '?text=' + encodeURIComponent('Hola Christian, he visto la propuesta de ' + (BIZ || 'mi tienda') + ' y quiero reservar la llamada para el ' + fL.format(new Date(pick))) + '" target="_blank" rel="noopener">Escríbeme por WhatsApp</a> y te la dejo hecha.'; err.hidden = false; };
    if (!PROD) { setTimeout(function () { done({ ok: true, id: 'Ldemo' }); }, 600); return; }
    fetch(API + 'book', { method: 'POST', body: JSON.stringify(body), headers: { 'content-type': 'application/json' } }).then(function (r) { return r.json(); }).then(done).catch(function () { done(null); }); };

  /* ---------- los botones de la propuesta bajan aquí; los huecos se cargan al acercarse ---------- */
  d.addEventListener('click', function (e) { var a = e.target.closest && e.target.closest('a[href="#agenda"]'); if (!a) return; e.preventDefault(); load();
    root.scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' });
    var c = $('ag-card'); setTimeout(function () { c.classList.add('fl'); setTimeout(function () { c.classList.remove('fl'); }, 1400); }, 700);
    try { history.replaceState(null, '', '#agenda'); } catch (x) {} });
  if ('IntersectionObserver' in window) { var io = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { load(); io.disconnect(); } }, { rootMargin: '900px 0px' }); io.observe(root); } else load();
  if (location.hash === '#agenda') load();
  /* el botón flotante de WhatsApp tapaba las respuestas en el móvil: se esconde mientras se ve la agenda (ella ya lleva su enlace a WhatsApp) */
  var fab = d.querySelector('.wa-fab'); if (fab && 'IntersectionObserver' in window) new IntersectionObserver(function (es) { fab.classList.toggle('ag-off', es[0].isIntersecting); }, { rootMargin: '-80px 0px -80px 0px' }).observe(root);
})();
