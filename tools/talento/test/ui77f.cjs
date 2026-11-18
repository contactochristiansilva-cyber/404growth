// Prueba en el navegador del vídeo selfie (v77f): grabar con la cámara (falsa) de Chromium, subir de la galería, límites y sin R2.
// Uso: node srv77.mjs & (con el R2 de mentira) y luego node ui77f.cjs. Necesita ffmpeg para los vídeos de prueba.
const { chromium, devices } = require('playwright');
const fs = require('fs'); const { execSync } = require('child_process');
const B = 'http://localhost:8777';
let ok = 0, ko = 0; const t = (c, m) => { if (c) ok++; else { ko++; console.log('FALLO:', m); } };
const shots = 'shots'; fs.mkdirSync(shots, { recursive: true });
const mkvid = (f, secs) => { if (!fs.existsSync(f)) execSync('ffmpeg -v error -y -f lavfi -i testsrc2=size=360x640:rate=25 -f lavfi -i sine=frequency=440 -t ' + secs + ' -c:v libx264 -preset ultrafast -pix_fmt yuv420p -c:a aac -shortest ' + f); };
mkvid('v12.mp4', 12); mkvid('v80.mp4', 80);
// rellena lo que haya en el paso que se ve (lo justo para pasar)
const fill = async (p) => {
  for (const fd of await p.$$('.fs.on .fd')) {
    const id = await fd.getAttribute('data-f'); if (!id || id === 'video' || id === 'cv') continue;
    if (await fd.$('.pills')) { await (await fd.$('label')).click(); continue; }
    const ta = await fd.$('textarea'); if (ta) { await ta.fill('Vendí por WhatsApp a tiendas de moda durante dos años, con seguimiento diario y buenos resultados.'); continue; }
    const inp = await fd.$('input'); if (!inp || await inp.inputValue()) continue;
    const ty = await inp.getAttribute('type');
    await inp.fill(ty === 'email' ? 'ana' + Date.now() + '@example.com' : ty === 'tel' ? '+54 9 11 2345 6789' : ty === 'url' ? 'https://ana.example.com' : id === 'city' ? 'Buenos Aires, Argentina' : id === 'name' ? 'Ana Prueba' : 'Texto de prueba');
  }
};
const next = (p) => p.click('#fm [data-next]');
(async () => {
  const br = await chromium.launch({ args: ['--use-fake-ui-for-media-stream', '--use-fake-device-for-media-stream'] });
  // 1. móvil: grabar en la página
  let ctx = await br.newContext({ ...devices['iPhone 13'], viewport: { width: 390, height: 844 }, permissions: ['camera', 'microphone'] });
  let p = await ctx.newPage(); const errs = []; p.on('pageerror', (e) => errs.push(String(e)));
  await p.goto(B + '/equipo/setter/', { waitUntil: 'networkidle' });
  await fill(p); await next(p); await fill(p); await next(p);
  t(await p.$eval('.fm-top b', (x) => x.textContent) === 'Tu vídeo', 'paso 3: el vídeo');
  t(await p.isVisible('[data-vrec]') && await p.isVisible('label[for=f-vfile]'), 'botones «Grabar ahora» y «Subir de la galería»');
  await p.screenshot({ path: shots + '/vf-paso-390.png' });
  t(await p.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth), 'paso del vídeo sin scroll lateral a 390');
  t(await p.evaluate(() => document.querySelector('#fm').getBoundingClientRect().left >= 0), 'el formulario no se corre hacia un lado');
  await p.setViewportSize({ width: 360, height: 780 }); t(await p.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth), 'ni a 360'); await p.setViewportSize({ width: 390, height: 844 });
  await next(p); t(await p.$eval('.vbox', (x) => x.classList.contains('bad')) && (await p.textContent('.verr')).includes('Graba tu vídeo'), 'sin vídeo no se sigue');
  await p.click('[data-vrec]'); await p.waitForSelector('[data-vcam]:not([hidden])'); await p.waitForFunction(() => document.querySelector('.vlive').videoWidth > 0);
  await p.click('[data-vgo]'); await p.waitForTimeout(3000);
  t((await p.textContent('.vtime')).startsWith('0:0'), 'el contador corre: ' + await p.textContent('.vtime'));
  await p.screenshot({ path: shots + '/vf-grabando-390.png' });
  await p.click('[data-vgo]');   // a los 3 s: demasiado corto
  await p.waitForFunction(() => /un poco más/.test(document.querySelector('.verr').textContent)); t(await p.isVisible('[data-vpick]'), 'menos de 10 s: vuelve a pedirlo');
  await p.click('[data-vrec]'); await p.waitForSelector('[data-vcam]:not([hidden])'); await p.waitForFunction(() => document.querySelector('.vlive').videoWidth > 0);
  await p.click('[data-vgo]'); await p.waitForTimeout(11500); await p.click('[data-vgo]');
  await p.waitForSelector('[data-vdone]:not([hidden])'); t(await p.isVisible('.vprev'), 'se ve el vídeo grabado');
  await p.waitForFunction(() => document.querySelector('[data-vdone]').classList.contains('ok'), null, { timeout: 15000 });
  t(/Vídeo listo/.test(await p.textContent('.vst')), 'subido: ' + await p.textContent('.vst'));
  await p.screenshot({ path: shots + '/vf-listo-390.png' });
  t(await p.evaluate(() => !document.querySelector('.vlive').srcObject), 'la cámara se apaga al terminar');
  await next(p); await fill(p); await next(p); await fill(p);
  await p.check('[name=consent]'); await p.click('[data-send]'); await p.waitForSelector('.done', { timeout: 10000 });
  t((await p.textContent('.done h3')).includes('Recibida'), 'candidatura enviada con el vídeo grabado');
  t(!errs.length, 'sin errores en la página: ' + errs.join(' | '));
  await ctx.close();
  // 2. el admin la ve con su vídeo
  const A = await br.newPage({ viewport: { width: 1366, height: 900 } });
  const L = await (await A.request.get(B + '/admin/api/tal')).json(); const c = L.cands.find((x) => x.job === 'setter');
  t(c && c.vid === 1, 'en la lista: con vídeo');
  const vr = await A.request.get(B + '/admin/api/tal/' + c.id + '/video', { headers: { range: 'bytes=0-1' } }); t(vr.status() === 206, 'el vídeo se sirve por rangos');
  await A.goto(B + '/admin/', { waitUntil: 'networkidle' }); await A.waitForSelector('.tl-c');
  t((await A.textContent('.tl-c')).includes('Vídeo'), 'la tarjeta dice «Vídeo»');
  await A.click('.tl-c'); await A.waitForSelector('.tl-h h2');
  const hasV = await A.$('video[src*="/video"]'); t(!!hasV, 'el admin enseña el reproductor');
  if (hasV) { await A.waitForFunction(() => { const v = document.querySelector('video[src*="/video"]'); return v && v.readyState >= 1; }, null, { timeout: 8000 }).catch(() => {}); t(await A.evaluate(() => document.querySelector('video[src*="/video"]').readyState >= 1), 'el reproductor carga el vídeo'); }
  await A.screenshot({ path: shots + '/vf-admin-1366.png' });
  // 3. ordenador: subir de la galería (uno de 80 s no, uno de 12 s sí)
  ctx = await br.newContext({ viewport: { width: 1366, height: 900 } }); p = await ctx.newPage();
  await p.goto(B + '/equipo/growth/', { waitUntil: 'networkidle' });
  await fill(p); await next(p); await fill(p); await next(p);
  await p.screenshot({ path: shots + '/vf-paso-1366.png' });
  await p.setInputFiles('#f-vfile', 'v80.mp4'); await p.waitForFunction(() => /máximo es 1 minuto/.test(document.querySelector('.verr').textContent));
  t(true, 'un vídeo de 80 s no se acepta');
  await p.setInputFiles('#f-vfile', 'v12.mp4'); await p.waitForSelector('[data-vdone]:not([hidden])');
  await p.waitForFunction(() => document.querySelector('[data-vdone]').classList.contains('ok'), null, { timeout: 15000 }); t(true, 'el de 12 s se sube');
  await p.screenshot({ path: shots + '/vf-galeria-1366.png' });
  await p.reload({ waitUntil: 'networkidle' });
  t(await p.isVisible('[data-vdone]') && /Vídeo listo/.test(await p.textContent('.vst')), 'al recargar, el vídeo sigue subido (borrador)');
  await p.click('[data-vredo]'); t(await p.isVisible('[data-vpick]'), '«Grabar o elegir otro» vuelve a los botones');
  await ctx.close();
  // 4. sin R2: queda el enlace, como antes
  ctx = await br.newContext({ viewport: { width: 390, height: 844 } }); p = await ctx.newPage();
  await p.route('**/l/jobs', (r) => r.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify({ open: { tiendas: true, setter: true, growth: true, abierta: true }, vid: false }) }));
  await p.goto(B + '/equipo/tiendas/', { waitUntil: 'networkidle' });
  await fill(p); await next(p); await p.fill('#f-portfolio', 'https://ana.example.com'); await fill(p); await next(p);
  t(!(await p.isVisible('[data-vbox]')) && await p.isVisible('#f-video'), 'sin R2: se pide el enlace');
  await next(p); t(await p.$eval('[data-f=video]', (x) => x.classList.contains('err')), 'sin R2: el enlace es obligatorio');
  await p.fill('#f-video', 'https://youtu.be/abc123'); await next(p); t(await p.$eval('.fm-top b', (x) => x.textContent) === 'El puesto', 'con el enlace se sigue');
  await ctx.close();
  await br.close();
  console.log(ok + ' bien, ' + ko + ' mal'); process.exit(ko ? 1 : 0);
})();
