// Prueba de la vista Entregables (v73) con Playwright, contra srv73.mjs (node srv73.mjs &) en el puerto 8773.
const { chromium } = require('playwright');
const OUT = process.argv[2] || '.';
(async () => {
  const b = await chromium.launch(); const errs = []; let ok = 0, ko = 0; const t = (c, m) => { if (c) ok++; else { ko++; console.log('FALLO:', m); } };
  const wait = (p, fn, arg, m) => p.waitForFunction(fn, arg, { timeout: 5000 }).then(() => t(true, ''), () => t(false, m));
  for (const [name, vp] of [['d', { width: 1366, height: 900 }], ['m', { width: 390, height: 844 }]]) {
    const p = await b.newPage({ viewport: vp, timezoneId: 'Europe/Istanbul', locale: 'es-ES' });
    p.on('pageerror', (e) => errs.push(name + ': ' + e.message));
    await p.goto('http://localhost:8773/'); await p.waitForSelector('#dv', { timeout: 8000 });
    if (name === 'd') {
      const txt = await p.textContent('#dv');
      t(/Cuenta atrás/.test(txt) && /Sin fecha todavía/.test(txt), 'grupos');
      t(!/Cliente Cuatro/.test(txt), 'el que no ha pagado no sale aunque tenga fecha');
      t(!/Cliente Archivado/.test(txt), 'una cuota mensual no lo mete');
      t(/Facturación/.test(await p.textContent('#dv .head')), 'explica que entran al cobrar');
      const order = await p.$$eval('#dv .dv-r h3', (h) => h.map((x) => x.textContent));
      t(order[0] === 'Cliente Dos' && order[1] === 'Cliente Tres' && order.length === 4, 'orden: la vencida, la más cercana y luego sin fecha: ' + order.join(','));
      t(/Pagado el 10 nov/.test(await p.textContent('#dv-c_BBB222 .dv-meta')), 'día del pago');
      t(await p.$eval('#dv-c_BBB222 .dv-c', (e) => e.classList.contains('late')), 'vencida en rojo');
      t(await p.$eval('#dv-c_CCC333 .dv-c', (e) => e.classList.contains('soon')), 'menos de 2 días en ámbar');
      const a1 = await p.textContent('#dv-c_CCC333 .dv-n'); await p.waitForTimeout(2100); const a2 = await p.textContent('#dv-c_CCC333 .dv-n');
      t(a1 !== a2, 'la cuenta atrás corre: ' + a1 + ' → ' + a2);
      t(/Día 15 del arranque/.test(await p.textContent('#dv-c_AAA111 [data-dv="d15"]')), 'con arranque: día 15 del arranque');
      const b15 = await p.textContent('#dv-n_tienda-sin-ficha [data-dv="d15"]');
      t(/15 días desde el pago \(28 nov\)/.test(b15), 'sin arranque: 15 días desde el pago: ' + b15);
      await p.click('#dv-n_tienda-sin-ficha [data-dv="d15"]'); await p.click('#dv-n_tienda-sin-ficha button[type=submit]');
      await p.waitForSelector('#dv-n_tienda-sin-ficha .dv-c[data-dvt]');
      const w = await p.textContent('#dv-n_tienda-sin-ficha .dv-w'); t(/28 de noviembre, 23:59/.test(w), 'fecha desde el pago hasta el final del día: ' + w);
      await p.click('#dv-n_tienda-sin-ficha [data-dv="edit"]'); await p.fill('#dv-n_tienda-sin-ficha input[name=d]', '2026-12-04'); await p.fill('#dv-n_tienda-sin-ficha input[name=t]', '18:30'); await p.click('#dv-n_tienda-sin-ficha button[type=submit]');
      await wait(p, () => /18:30/.test((document.querySelector('#dv-n_tienda-sin-ficha .dv-w') || {}).textContent || ''), null, 'cambiar fecha con hora');
      await p.click('#dv-c_CCC333 [data-dv="done"]'); await p.waitForSelector('details.dv-dn');
      t(/Entregadas · 1/.test(await p.textContent('details.dv-dn summary')), 'pasa a entregadas');
      await p.click('#dv-c_BBB222 [data-dv="clear"]'); t(/Seguro/.test(await p.textContent('#dv-c_BBB222 [data-dv="clear"]')), 'quitar fecha pide confirmación');
      await p.click('#dv-c_BBB222 [data-dv="clear"]'); await wait(p, () => !!document.querySelector('#dv-c_BBB222') && !document.querySelector('#dv-c_BBB222 .dv-c'), null, 'quitar fecha lo deja en la lista sin fecha');
      await p.click('#dv-c_AAA111 [data-dv="hide"]'); t(/Seguro/.test(await p.textContent('#dv-c_AAA111 [data-dv="hide"]')), 'quitar de la lista pide confirmación');
      await p.click('#dv-c_AAA111 [data-dv="hide"]'); await p.waitForSelector('details.dv-hd');
      t(/Quitados de la lista · 1/.test(await p.textContent('details.dv-hd summary')), 'pasa a quitados');
      await p.click('details.dv-hd summary'); await p.click('#dv-c_AAA111 [data-dv="unhide"]');
      await wait(p, () => !document.querySelector('details.dv-hd') && !!document.querySelector('#dv-c_AAA111 .dv-ed'), null, 'volver a la lista');
      await p.screenshot({ path: OUT + '/ui-d.png', fullPage: true });
    } else {
      t(!(await p.evaluate(() => document.documentElement.scrollWidth > innerWidth)), 'móvil sin scroll lateral');
      await p.screenshot({ path: OUT + '/ui-m.png', fullPage: true });
    }
  }
  console.log(errs.length ? errs.join('\n') : 'sin errores de JS');
  console.log(ok + ' bien, ' + ko + ' mal'); await b.close(); process.exit(ko ? 1 : 0);
})();
