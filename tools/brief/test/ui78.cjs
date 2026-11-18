// Prueba en el navegador del brief (v78): enlace privado, guardar solo, dos personas, archivos, enviar, móvil y el admin.
// Uso: node srv78.mjs & y luego node ui78.cjs (capturas en shots/)
const { chromium, devices } = require('playwright');
const fs = require('fs');
const B = 'http://localhost:8778';
let ok = 0, ko = 0; const t = (c, m) => { if (c) ok++; else { ko++; console.log('FALLO:', m); } };
fs.mkdirSync('shots', { recursive: true });
(async () => {
  const br = await chromium.launch();
  const A = await br.newPage({ viewport: { width: 1366, height: 900 } });
  const L = await (await A.request.get(B + '/admin/api/brief')).json(); const link = L.briefs[0].link.replace('https://404growth.com', B);
  // 1. sin la clave: aviso
  let ctx = await br.newContext({ viewport: { width: 390, height: 844 } }); let p = await ctx.newPage();
  await p.goto(B + '/brief/efap-miami/', { waitUntil: 'networkidle' });
  t(await p.isVisible('#gate'), 'sin clave sale «Enlace no válido»');
  await ctx.close();
  // 2. móvil: rellenar
  ctx = await br.newContext({ ...devices['iPhone 13'], viewport: { width: 390, height: 844 } }); p = await ctx.newPage(); const errs = []; p.on('pageerror', (e) => errs.push(String(e)));
  await p.goto(link, { waitUntil: 'networkidle' });
  t(!(await p.isVisible('#gate')), 'con la clave se abre');
  await p.waitForFunction(() => /Guardado/.test(document.querySelector('#st').textContent));
  t(await p.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth), 'sin scroll lateral a 390');
  await p.screenshot({ path: 'shots/b-hero-390.png' });
  await p.fill('#f-quien', 'Ana · coordinadora');
  await p.fill('#f-fecha', '2027-01-16');
  await p.click('[data-q="edades"] .chip:has-text("8 a 12")');
  await p.click('[data-q="edades"] .chip:has-text("13 a 15")');
  await p.click('[data-q="precio"] .chip:has-text("Otro")');
  t(await p.isVisible('#f-precio_o'), '«Otro» abre su campo');
  await p.fill('#f-precio_o', '10 $ que se devuelven al venir');
  await p.click('[data-q="c_jug"] .chip:has-text("Hay que cambiarlo")');
  t(await p.isVisible('#f-c_jug_o'), '«Hay que cambiarlo» abre «¿Qué ponemos?»');
  await p.fill('#f-c_jug_o', 'Más de 500 jugadores');
  await p.check('[name="agenda__p"]');
  t(await p.$eval('[data-q="agenda"]', (x) => x.classList.contains('is-pend')), '«Aún no lo sabemos» marca la pregunta');
  await p.waitForTimeout(1200);
  await p.waitForFunction(() => /Guardado/.test(document.querySelector('#st').textContent));
  t(/^6 de 91$/.test(await p.textContent('.cnt')), 'el contador: ' + await p.textContent('.cnt'));
  await p.locator('#s2').scrollIntoViewIfNeeded(); await p.screenshot({ path: 'shots/b-s2-390.png' });
  await p.setViewportSize({ width: 360, height: 780 }); t(await p.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth), 'sin scroll lateral a 360'); await p.setViewportSize({ width: 390, height: 844 });
  // archivo
  fs.writeFileSync('logo.png', Buffer.from([137, 80, 78, 71, 13, 10, 26, 10, 0, 0, 0, 13]));
  await p.setInputFiles('#fin', 'logo.png');
  await p.waitForFunction(() => document.querySelectorAll('#fl [data-rm]').length === 1, null, { timeout: 8000 });
  t(true, 'el archivo se sube y sale en la lista');
  // 3. otra persona, a la vez, en el ordenador
  const ctx2 = await br.newContext({ viewport: { width: 1440, height: 900 } }); const p2 = await ctx2.newPage();
  await p2.goto(link, { waitUntil: 'networkidle' }); await p2.waitForFunction(() => /Guardado/.test(document.querySelector('#st').textContent));
  t(await p2.inputValue('#f-quien') === 'Ana · coordinadora' && await p2.isChecked('[data-q="edades"] input[value="13 a 15 (Performance)"]') && await p2.inputValue('#f-c_jug_o') === 'Más de 500 jugadores', 'la otra persona ve lo escrito');
  t(await p2.$$eval('#fl [data-rm]', (x) => x.length) === 1, 'y el archivo');
  await p2.fill('#f-lugar', 'Campo municipal, Hollywood (Florida)'); await p2.waitForTimeout(1300);
  await p2.screenshot({ path: 'shots/b-1440.png' });
  await p2.locator('#s6').scrollIntoViewIfNeeded(); await p2.screenshot({ path: 'shots/b-s6-1440.png' });
  // la primera persona vuelve a la pestaña: ve lo de la otra y no pierde lo suyo
  await p.fill('#f-horario', 'Llegada 8:30 · 9:00 a 13:00'); await p.waitForTimeout(1200);
  await p.evaluate(() => document.dispatchEvent(new Event('visibilitychange')));
  await p.waitForFunction(() => document.querySelector('#f-lugar').value.length > 0, null, { timeout: 5000 });
  t(await p.inputValue('#f-horario') === 'Llegada 8:30 · 9:00 a 13:00', 'nadie pisa a nadie');
  // 4. recargar: todo sigue
  await p.reload({ waitUntil: 'networkidle' }); await p.waitForFunction(() => /Guardado/.test(document.querySelector('#st').textContent));
  t(await p.inputValue('#f-precio_o') === '10 $ que se devuelven al venir' && await p.isChecked('[name="agenda__p"]') && await p.inputValue('#f-fecha') === '2027-01-16', 'al recargar sigue todo');
  // 5. enviar
  await p.click('#sendb'); await p.waitForFunction(() => /Recibido/.test(document.querySelector('#sendm').textContent));
  t(true, 'enviado');
  await p.locator('#enviar').scrollIntoViewIfNeeded(); await p.screenshot({ path: 'shots/b-enviar-390.png' });
  const push = await (await p.request.get(B + '/__push')).json();
  t(push.some((x) => /empezado/.test(x.title)) && push.some((x) => /enviado/.test(x.title)), 'avisos: ' + push.map((x) => x.title).join(' | '));
  t(!errs.length, 'sin errores: ' + errs.join(' | '));
  // 6. el admin
  await A.goto(B + '/admin/', { waitUntil: 'networkidle' }); await A.waitForSelector('.br-c');
  t(/Enviado el/.test(await A.textContent('.br-c')) && /Ana · coordinadora/.test(await A.textContent('.br-c')), 'la tarjeta: enviado y quién');
  await A.screenshot({ path: 'shots/b-admin-lista.png' });
  await A.click('[data-br="open"]'); await A.waitForSelector('.br-sec');
  const txt = await A.textContent('#br');
  t(/Otro: 10 \$ que se devuelven/.test(txt) && /Hay que cambiarlo: Más de 500/.test(txt) && /Aún no lo saben/.test(txt) && /logo\.png/.test(txt), 'el detalle enseña «otro», «cambiar», pendientes y archivos');
  await A.screenshot({ path: 'shots/b-admin-detalle.png', fullPage: true });
  await A.check('[data-br="hide"]'); await A.waitForTimeout(300);
  t((await A.$$('.br-q')).length < 30, 'ocultar lo que falta: ' + (await A.$$('.br-q')).length);
  await A.setViewportSize({ width: 390, height: 844 }); t(await A.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth), 'admin sin scroll lateral a 390');
  await br.close();
  console.log(ok + ' bien, ' + ko + ' mal'); process.exit(ko ? 1 : 0);
})();
