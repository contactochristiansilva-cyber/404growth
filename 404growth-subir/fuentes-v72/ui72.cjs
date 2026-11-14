// Prueba de la vista Entregables (v72) con Playwright, contra srv72.mjs (node srv72.mjs &) en el puerto 8772.
const { chromium } = require('playwright');
const OUT = process.argv[2] || '.';
(async () => {
  const b = await chromium.launch(); const errs = []; let ok = 0, ko = 0; const t = (c, m) => { if (c) ok++; else { ko++; console.log('FALLO:', m); } };
  for (const [name, vp] of [['d', { width: 1366, height: 900 }], ['m', { width: 390, height: 844 }]]) {
    const p = await b.newPage({ viewport: vp, timezoneId: 'Europe/Istanbul', locale: 'es-ES' });
    p.on('pageerror', (e) => errs.push(name + ': ' + e.message));
    await p.goto('http://localhost:8772/'); await p.waitForSelector('#dv', { timeout: 8000 });
    if (name === 'd') {
      const txt = await p.textContent('#dv');
      t(/Cuenta atrás/.test(txt) && /Sin fecha todavía/.test(txt), 'grupos');
      t(!/Cliente Archivado/.test(txt), 'el archivado sin fecha no sale');
      const order = await p.$$eval('#dv .dv-r h3', (h) => h.map((x) => x.textContent));
      t(order[0] === 'Cliente Dos' && order[1] === 'Cliente Tres', 'orden: la vencida y luego la más cercana: ' + order.join(','));
      t(await p.$eval('#dv-c_BBB222 .dv-c', (e) => e.classList.contains('late')), 'vencida en rojo');
      t(await p.$eval('#dv-c_CCC333 .dv-c', (e) => e.classList.contains('soon')), 'menos de 2 días en ámbar');
      const a1 = await p.textContent('#dv-c_CCC333 .dv-n'); await p.waitForTimeout(2100); const a2 = await p.textContent('#dv-c_CCC333 .dv-n');
      t(a1 !== a2, 'la cuenta atrás corre: ' + a1 + ' → ' + a2);
      t(/23:59/.test(await p.textContent('#dv-c_CCC333 .dv-w')), 'muestra la hora de España');
      await p.click('#dv-c_AAA111 [data-dv="d15"]'); await p.click('#dv-c_AAA111 button[type=submit]');
      await p.waitForSelector('#dv-c_AAA111 .dv-c[data-dvt]');
      const w = await p.textContent('#dv-c_AAA111 .dv-w'); t(/23:59/.test(w), 'día 15 hasta el final del día: ' + w);
      await p.click('#dv-c_AAA111 [data-dv="edit"]'); await p.fill('#dv-c_AAA111 input[name=d]', '2026-12-04'); await p.fill('#dv-c_AAA111 input[name=t]', '18:30'); await p.click('#dv-c_AAA111 button[type=submit]');
      await p.waitForFunction(() => /18:30/.test((document.querySelector('#dv-c_AAA111 .dv-w') || {}).textContent || ''), null, { timeout: 5000 }).then(() => t(true, ''), () => t(false, 'cambiar fecha con hora'));
      await p.click('#dv-c_CCC333 [data-dv="done"]'); await p.waitForSelector('details.dv-dn');
      t(/Entregadas · 1/.test(await p.textContent('details.dv-dn summary')), 'pasa a entregadas');
      await p.click('#dv-c_BBB222 [data-dv="clear"]'); t(/Seguro/.test(await p.textContent('#dv-c_BBB222 [data-dv="clear"]')), 'pide confirmación');
      await p.click('#dv-c_BBB222 [data-dv="clear"]'); await p.waitForFunction(() => !document.querySelector('#dv-c_BBB222 .dv-c'), null, { timeout: 5000 }).then(() => t(true, ''), () => t(false, 'quitar fecha'));
      await p.screenshot({ path: OUT + '/ui-d.png', fullPage: true });
    } else {
      t(!(await p.evaluate(() => document.documentElement.scrollWidth > innerWidth)), 'móvil sin scroll lateral');
      await p.screenshot({ path: OUT + '/ui-m.png', fullPage: true });
    }
  }
  console.log(errs.length ? errs.join('\n') : 'sin errores de JS');
  console.log(ok + ' bien, ' + ko + ' mal'); await b.close(); process.exit(ko ? 1 : 0);
})();
