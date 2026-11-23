// Playwright: tu-tienda at 360, 390 and 1440; validation, submit, success, lead created, /book link with UTM.
const { chromium } = require('playwright');
const BASE = process.argv[2] || 'http://localhost:8787', OUT = process.argv[3] || '/tmp';
(async () => {
  const b = await chromium.launch(); let n = 0, bad = 0;
  const ok = (c, m) => { n++; if (!c) { bad++; console.log('FALLA:', m); } else console.log('ok', m); };
  for (const [w, h] of [[360, 740], [390, 844], [1440, 900]]) {
    const p = await b.newPage({ viewport: { width: w, height: h } });
    const errs = []; p.on('pageerror', (e) => errs.push(String(e)));
    await p.goto(BASE + '/tu-tienda?utm_source=youtube&utm_medium=video&utm_campaign=tienes-web');
    const sw = await p.evaluate(() => document.documentElement.scrollWidth);
    ok(sw <= w, w + ': sin scroll lateral (' + sw + ')');
    await p.screenshot({ path: `${OUT}/tt-${w}.png`, fullPage: true });
    await p.click('#go');
    ok((await p.textContent('#err')).includes('nombre'), w + ': pide el nombre');
    await p.fill('input[name=name]', 'Lucía Pérez'); await p.fill('input[name=biz]', 'Boutique Prueba ' + w);
    await p.fill('input[name=ig]', '@prueba ' + w); await p.fill('input[name=phone]', '612 345 6' + String(w).slice(0, 2));
    await p.click('#go');
    ok((await p.textContent('#err')).includes('Instagram'), w + ': Instagram con espacio no vale');
    await p.fill('input[name=ig]', '@prueba_' + w);
    await p.click('#go');
    ok((await p.textContent('#err')).includes('privacidad'), w + ': pide aceptar la privacidad');
    await p.click('text=Joyería'); await p.click('text=Tenemos web, pero no vende');
    await p.check('input[name=ok]'); await p.click('#go');
    await p.waitForSelector('.box.sent', { timeout: 5000 }).catch(() => {});
    ok(await p.isVisible('.done'), w + ': sale el «Hecho»');
    ok((await p.textContent('#dt')) === 'Hecho, Lucía.', w + ': saluda por el nombre');
    const href = await p.getAttribute('#bk', 'href');
    ok(href.startsWith('/book?') && href.includes('utm_source=youtube') && href.includes('utm_campaign=tienes-web') && href.includes('utm_content=tu-tienda'), w + ': botón a /book con la UTM: ' + href);
    await p.screenshot({ path: `${OUT}/tt-${w}-ok.png`, fullPage: false });
    ok(!errs.length, w + ': sin errores de JS ' + errs.join(' '));
    await p.close();
  }
  const leads = await (await fetch(BASE + '/__leads')).json();
  ok(leads.length === 3, 'tres leads creados');
  const d = JSON.parse(leads[0].data);
  ok(d.niche === 'joya' && d.ttWeb === 'web' && d.ttUtm.utm_campaign === 'tienes-web', 'lead con nicho, web y UTM');
  // internal test: nothing is sent
  const p = await b.newPage({ viewport: { width: 390, height: 844 } });
  await p.goto(BASE + '/tu-tienda?interno=1');
  ok(await p.isVisible('#int'), 'prueba interna: se ve el aviso');
  await p.fill('input[name=name]', 'Chris'); await p.fill('input[name=biz]', 'Interna'); await p.fill('input[name=ig]', 'interna'); await p.fill('input[name=phone]', '600000000');
  await p.check('input[name=ok]'); await p.click('#go'); await p.waitForSelector('.box.sent');
  const after = await (await fetch(BASE + '/__leads')).json();
  ok(after.length === 3, 'prueba interna: no crea lead');
  await b.close();
  console.log(`\n${n - bad}/${n} comprobaciones`); process.exit(bad ? 1 : 0);
})();
