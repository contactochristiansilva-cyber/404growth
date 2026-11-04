// Captura de la propuesta v33 para el correo: 600 px de ancho, x2, sin animaciones; los 6 anuncios en 2 columnas.
const { chromium } = require('playwright');
(async () => {
  const slugs = process.argv.slice(2); const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 600, height: 900 }, deviceScaleFactor: 2, reducedMotion: 'reduce' });
  for (const s of slugs) {
    const p = await ctx.newPage();
    await p.goto(`http://localhost:8733/p-${s}.html`, { waitUntil: 'load' });
    await p.addStyleTag({ content: '#captacion .adsx .adg{grid-auto-flow:row!important;grid-template-columns:repeat(2,minmax(0,1fr))!important;grid-auto-columns:auto!important;overflow:visible!important;margin:0!important;padding:0!important}#captacion .adg>*{min-width:0!important;width:auto!important}.swp,.wa-fab{display:none!important}.sk .rv{opacity:1!important;transform:none!important;filter:none!important}' });
    await p.evaluate(async () => { document.querySelectorAll('.rv').forEach(e => e.classList.add('in')); await Promise.all([...document.images].map(i => i.complete ? 0 : new Promise(r => { i.onload = i.onerror = r }))); });
    await p.waitForTimeout(1200);
    await p.screenshot({ path: `l33/mail/${s}.png`, fullPage: true });
    console.log('ok', s, await p.evaluate(() => document.documentElement.scrollHeight)); await p.close();
  }
  await b.close();
})();
