// Captura del móvil del inicio (su tienda en el teléfono) para adjuntar en WhatsApp / Instagram.
const { chromium, devices } = require('playwright');
(async () => {
  const slugs = process.argv.slice(2); const b = await chromium.launch();
  const ctx = await b.newContext({ ...devices['iPhone 13'], deviceScaleFactor: 3, reducedMotion: 'reduce' });
  for (const s of slugs) {
    const p = await ctx.newPage();
    await p.goto(`http://localhost:8733/p-${s}.html`, { waitUntil: 'load' });
    await p.addStyleTag({ content: '.hero .stage .ph{width:330px!important;box-shadow:0 30px 60px -20px rgba(0,0,0,.35),0 0 0 1px rgba(0,0,0,.08)!important}.stage .glow{display:none!important}.nav,.wa-fab{display:none!important}' });
    await p.evaluate(() => { dispatchEvent(new Event('resize')); });
    await p.waitForTimeout(900);
    const r = await p.$eval('.hero .ph', e => { const b = e.getBoundingClientRect(); return {x:b.x + scrollX, y:b.y + scrollY, w:b.width, h:b.height}; });
    const pad = 22; await p.screenshot({ path: `l33/wa/${s}.png`, fullPage: true, clip: { x: Math.max(0, r.x - pad), y: Math.max(0, r.y - pad), width: r.w + 2 * pad, height: r.h + 2 * pad } });
    console.log('ok', s); await p.close();
  }
  await b.close();
})();
