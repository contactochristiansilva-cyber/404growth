const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const R = []; const ok = (n, c, x) => R.push((c ? 'OK   ' : 'FALLA ') + n + (x !== undefined ? ' → ' + JSON.stringify(x) : ''));
  const st = p => p.evaluate(() => { const v = document.querySelector('#vv'), s = document.querySelector('#screen'), g = document.querySelector('#vgo'), l = document.querySelector('#vlq');
    return { cls: s.className, t: +v.currentTime.toFixed(2), muted: v.muted, paused: v.paused, loop: v.loop, controls: v.controls, btn: getComputedStyle(g).display !== 'none', vop: getComputedStyle(v).opacity, lq: l.src.slice(0, 22), lqok: l.classList.contains('ok') }; });
  // 1) móvil, red lenta: primero el fotograma borroso
  let c = await b.newContext({ viewport: { width: 390, height: 664 }, isMobile: true, hasTouch: true }); let p = await c.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message));
  const reqs = []; p.on('request', r => { if (/\/l\//.test(r.url())) reqs.push(r.url()) });
  await p.route('**/v/book/**', async r => { await new Promise(z => setTimeout(z, 1200)); r.continue(); });
  await p.goto('http://127.0.0.1:8765/book.html', { waitUntil: 'domcontentloaded' }); await p.waitForTimeout(500);
  let s = await st(p); ok('mientras carga: fotograma borroso a la vista y vídeo transparente', !/vp/.test(s.cls) && s.vop === '0' && s.lq.startsWith('data:image/jpeg') && s.btn, s);
  await p.waitForTimeout(5500); s = await st(p); ok('arranca solo, sin sonido y en bucle', /vp/.test(s.cls) && s.t > 0.3 && s.muted && s.loop && !s.paused && !s.controls && s.btn, s);
  const t1 = s.t;
  // 2) botón: desde 0 y con audio
  await p.tap('#vgo'); await p.waitForTimeout(250); s = await st(p); ok('al pulsar: vuelve a 0, con sonido, con controles y sin botón', s.t < 0.6 && s.t < t1 && !s.muted && !s.loop && s.controls && !s.btn && /aud/.test(s.cls), s);
  await p.waitForTimeout(1500); s = await st(p); ok('sigue reproduciendo con sonido', !s.paused && s.t > 0.8 && !s.muted, s);
  // 3) con audio, al bajar a reservar no se para
  await p.evaluate(() => document.querySelector('#reservar').scrollIntoView()); await p.waitForTimeout(700); s = await st(p); ok('con audio sigue sonando al bajar al calendario', !s.paused, s.paused);
  // 4) al acabar vuelve el botón
  await p.evaluate(() => document.querySelector('#vv').dispatchEvent(new Event('ended'))); s = await st(p); ok('al terminar vuelve el botón', s.btn && !s.controls && !/aud/.test(s.cls), s);
  ok('sin errores de script', errs.length === 0, errs);
  await c.close();
  // 5) de fondo: se para fuera de pantalla y sigue al volver
  c = await b.newContext({ viewport: { width: 1366, height: 768 } }); p = await c.newPage();
  await p.goto('http://127.0.0.1:8765/book.html'); await p.waitForTimeout(2500);
  await p.evaluate(() => document.querySelector('#reservar').scrollIntoView()); await p.waitForTimeout(800); s = await st(p); ok('de fondo: se para al salir de pantalla', s.paused, s);
  await p.evaluate(() => scrollTo(0, 0)); await p.waitForTimeout(900); s = await st(p); ok('de fondo: sigue al volver', !s.paused && s.muted, s);
  await c.close();
  // 6) reducir movimiento: sin arranque, póster nítido, el botón funciona
  c = await b.newContext({ viewport: { width: 390, height: 664 }, reducedMotion: 'reduce' }); p = await c.newPage();
  await p.goto('http://127.0.0.1:8765/book.html'); await p.waitForTimeout(1500); s = await st(p); ok('reducir movimiento: no arranca y se ve el fotograma nítido', s.paused && s.t === 0 && s.lqok && s.btn, s);
  await p.click('#vgo'); await p.waitForTimeout(2500); s = await st(p); ok('reducir movimiento: el botón lo reproduce con sonido', !s.paused && !s.muted && s.t > 0.3, s);
  await c.close();
  // 7) sin el archivo de hls: se queda el fotograma nítido
  c = await b.newContext({ viewport: { width: 390, height: 664 } }); p = await c.newPage(); await p.route('**/hls.light.min.js', r => r.abort());
  await p.goto('http://127.0.0.1:8765/book.html'); await p.waitForTimeout(1500); s = await st(p); ok('si falla la carga: fotograma nítido', s.lqok, s);
  await c.close(); await b.close(); console.log(R.join('\n'));
})();
