// Recorrido de la v77 con Playwright: las páginas de /equipo, la candidatura completa (con CV), la prueba, la entrevista y la vista Talento del admin.
const { chromium, devices } = require('playwright');
const fs = require('fs');
const B = 'http://localhost:8777';
let ok = 0, ko = 0; const t = (c, m) => { if (c) ok++; else { ko++; console.log('FALLO:', m); } };
(async () => {
  const br = await chromium.launch();
  const shots = 'shots'; fs.mkdirSync(shots, { recursive: true });
  // 1. las páginas, sin scroll lateral ni errores, a 360, 390 y 1440
  for (const [w, h] of [[360, 780], [390, 844], [1440, 900]]) {
    const ctx = await br.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: 1 }); const p = await ctx.newPage(); const errs = [];
    p.on('pageerror', (e) => errs.push(e.message)); p.on('console', (m) => { if (m.type() === 'error') errs.push(m.text()); });
    for (const pg of ['/equipo/', '/equipo/tiendas/', '/equipo/setter/', '/equipo/growth/', '/equipo/abierta/']) {
      await p.goto(B + pg, { waitUntil: 'networkidle' });
      const sw = await p.evaluate(() => document.documentElement.scrollWidth); t(sw <= w, pg + ' a ' + w + ': scroll lateral ' + sw);
      if (pg !== '/equipo/') { const n = await p.$$eval('section.sec[id] .sn', (x) => x.map((y) => y.textContent)); t(['01', '02', '03', '04', '05'].every((k) => n.includes(k)), pg + ': los 5 puntos ' + n.join(',')); }
    }
    t(!errs.filter((x) => !/favicon|apple-touch|og-|404/.test(x)).length, 'errores a ' + w + ': ' + errs.join(' | '));
    await p.goto(B + '/equipo/tiendas/', { waitUntil: 'networkidle' });
    await p.screenshot({ path: shots + '/tiendas-' + w + '.png', fullPage: true });
    await p.goto(B + '/equipo/', { waitUntil: 'networkidle' }); await p.screenshot({ path: shots + '/index-' + w + '.png', fullPage: true });
    await ctx.close();
  }
  // 2. la candidatura en el móvil, paso a paso, con borrador y CV
  const ctx = await br.newContext({ ...devices['iPhone 13'], viewport: { width: 390, height: 844 } }); const p = await ctx.newPage();
  await p.goto(B + '/equipo/tiendas/?utm_source=linkedin&utm_medium=post&utm_campaign=tiendas', { waitUntil: 'networkidle' });
  await p.click('#fm [data-next]'); t(await p.$eval('[data-f=name]', (x) => x.classList.contains('err')), 'paso 1 vacío: marca el nombre');
  await p.fill('#f-name', 'Marta Prueba Ruiz'); await p.fill('#f-email', 'marta@example.com'); await p.fill('#f-phone', '611 222 333'); await p.fill('#f-city', 'Sevilla, España');
  await p.reload({ waitUntil: 'networkidle' }); t(await p.inputValue('#f-name') === 'Marta Prueba Ruiz', 'el borrador se guarda al recargar');
  await p.click('#fm [data-next]'); t(await p.$eval('.fm-top span', (x) => x.textContent) === 'Paso 2 de 4', 'paso 2');
  await p.click('#fm [data-next]'); t(await p.$eval('[data-f=portfolio]', (x) => x.classList.contains('err')), 'en tiendas el portfolio es obligatorio');
  await p.fill('#f-portfolio', 'martaprueba.example.com');
  fs.writeFileSync('cv.pdf', '%PDF-1.4\n% CV de prueba\n');
  await p.setInputFiles('#f-cv', 'cv.pdf'); t((await p.textContent('[data-f=cv] .fn')).includes('cv.pdf'), 'CV elegido');
  await p.click('#fm [data-next]');
  await p.click('[data-f=ko1] label:first-child'); await p.fill('#f-q1', 'Monté tres tiendas Shopify de moda: Lumen, Brisa y Odette. Hice tema, fichas y fotos con IA.');
  await p.fill('#f-q2', 'Ordeno el catálogo, rehago fotos con IA, portada fuerte y fichas completas; reviso en el móvil cada día.');
  await p.fill('#f-q3', 'Nano Banana para fotos de producto, GPT Image para portadas y Claude para fichas y textos.');
  await p.screenshot({ path: shots + '/form-paso3-390.png' });
  await p.click('#fm [data-next]');
  for (const [f, k] of [['hours', 2], ['start', 1], ['tz', 1], ['lang', 1]]) await p.click('[data-f=' + f + '] label:nth-child(' + k + ')');
  await p.fill('#f-rate', '550 € por tienda');
  await p.click('[data-send]'); t((await p.textContent('.fmsg')).includes('privacidad'), 'sin la casilla no se envía');
  await p.check('[name=consent]'); await p.check('[name=keep]');
  await p.screenshot({ path: shots + '/form-paso4-390.png' });
  await p.click('[data-send]'); await p.waitForSelector('.done', { timeout: 8000 });
  t((await p.textContent('.done h3')).includes('Recibida, Marta'), 'candidatura enviada');
  await p.screenshot({ path: shots + '/form-hecho-390.png' });
  // 3. el admin la ve con su nota y su CV
  const A = await br.newPage({ viewport: { width: 1366, height: 900 } });
  await A.goto(B + '/admin/', { waitUntil: 'networkidle' }); await A.waitForSelector('.tl-c');
  const card = await A.textContent('.tl-c'); t(card.includes('Marta Prueba Ruiz') && card.includes('CV') && /IA: (avanzar|dudoso)/.test(card), 'tarjeta en el admin: ' + card);
  await A.screenshot({ path: shots + '/admin-tablero-1366.png' });
  await A.click('.tl-c'); await A.waitForSelector('.tl-h h2');
  const det = await A.textContent('#tl'); t(det.includes('Portfolio y calidad visual') && det.includes('Llegó desde: linkedin · post') && det.includes('Abrir el PDF'), 'ficha con rúbrica, origen y CV');
  await A.screenshot({ path: shots + '/admin-ficha-1366.png', fullPage: true });
  await A.click('[data-tl=stage][data-tlv=test]'); await A.waitForSelector('.tl-msg textarea');
  const msg = await A.inputValue('.tl-msg textarea'); t(msg.includes('Hola Marta') && msg.includes('/equipo/prueba/?t='), 'mensaje de la prueba listo para WhatsApp');
  const wa = await A.getAttribute('.tl-msg a[data-tl=wa]', 'href'); t(wa.startsWith('https://wa.me/34611222333?text='), 'botón de WhatsApp con su número');
  await A.screenshot({ path: shots + '/admin-mensaje-1366.png' });
  const link = msg.match(/https:\/\/404growth\.com(\/equipo\/prueba\/\?t=[^\s]+)/)[1];
  // 4. la prueba, en su página
  await p.goto(B + link, { waitUntil: 'networkidle' }); await p.waitForSelector('#pzf');
  t((await p.textContent('#pz-h')).includes('Marta'), 'página de la prueba con su nombre');
  await p.fill('#pzf [name=l] >> nth=0', 'olvido-marta.myshopify.com'); await p.fill('#pzf [name=text]', 'Contraseña: prueba. Portada con novedades y categorías; ficha del vestido Lino.');
  await p.screenshot({ path: shots + '/prueba-390.png', fullPage: true });
  await p.click('#pzf button[type=submit]'); await p.waitForSelector('#pz .done'); t(true, 'prueba entregada');
  // 5. de vuelta en el admin: prueba entregada y puntuada; a entrevista
  await A.click('[data-tl=back]'); await A.waitForSelector('.tl-c');
  t((await A.textContent('.tl-col:nth-child(4)')).includes('Marta'), 'en la columna «Prueba entregada»');
  await A.click('.tl-c'); await A.waitForSelector('.tl-h h2');
  t((await A.textContent('#tl')).includes('La IA sobre su prueba'), 'la prueba tiene nota');
  await A.click('[data-tl=stage][data-tlv=meet]'); await A.waitForSelector('.tl-msg textarea');
  const m2 = await A.inputValue('.tl-msg textarea'); const link2 = m2.match(/https:\/\/404growth\.com(\/equipo\/entrevista\/\?t=[^\s]+)/)[1];
  await p.goto(B + link2, { waitUntil: 'networkidle' }); await p.waitForFunction(() => !document.querySelector('#iv .load'));
  const ivtxt = await p.textContent('#iv'); t(/Elige el día|cerramos a mano|no quedan horas/.test(ivtxt), 'página de la entrevista: ' + ivtxt.slice(0, 80));
  if (await p.$('#iv .days button')) { await p.click('#iv .hours button'); await p.screenshot({ path: shots + '/entrevista-390.png', fullPage: true }); }
  // 6. el tablero en el móvil
  const M = await br.newPage({ viewport: { width: 390, height: 844 } }); await M.goto(B + '/admin/', { waitUntil: 'networkidle' }); await M.waitForSelector('.tl-c');
  t(await M.evaluate(() => document.documentElement.scrollWidth) <= 390, 'admin en el móvil sin scroll lateral');
  await M.screenshot({ path: shots + '/admin-tablero-390.png', fullPage: true });
  await M.click('.tl-c'); await M.waitForSelector('.tl-h h2'); t(await M.evaluate(() => document.documentElement.scrollWidth) <= 390, 'ficha en el móvil sin scroll lateral');
  await M.screenshot({ path: shots + '/admin-ficha-390.png', fullPage: true });
  console.log(ok + ' bien, ' + ko + ' mal');
  await br.close(); process.exit(ko ? 1 : 0);
})();
