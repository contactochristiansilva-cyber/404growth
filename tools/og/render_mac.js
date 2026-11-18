// Paso 2 de wa_og.py: con el Playwright del Mac (para que salga la SF Pro), cada <src>/<slug>.html -> <web>/p-<slug>--wa.jpg.
// Se pega en browser_run_code_unsafe cambiando SRC, WEB y el tramo (FROM, TO): unas 100 por llamada.
async (page) => {
  const SRC = '/Users/antoniosilvacamacho/Downloads/404growth-subir/og-wa';
  const WEB = '/Users/antoniosilvacamacho/Downloads/web117-404growth';
  const FROM = 0, TO = 100;
  await page.setViewportSize({width: 1200, height: 630});
  await page.goto('file://' + SRC + '/lista.json');
  const all = JSON.parse(await page.evaluate(() => document.body.innerText));
  const done = [];
  for (const s of all.slice(FROM, TO)) {
    await page.goto('file://' + SRC + '/' + s + '.html');
    await page.evaluate(async () => {
      const u = getComputedStyle(document.querySelector('.bg')).backgroundImage.slice(5, -2);
      await new Promise(r => { const i = new Image(); i.onload = i.onerror = r; i.src = u; });
      await document.fonts.ready;
    });
    await page.waitForTimeout(60);
    await page.screenshot({path: WEB + '/p-' + s + '--wa.jpg', type: 'jpeg', quality: 86});
    done.push(s);
  }
  return {total: all.length, hechas: done.length, ultima: done[done.length - 1]};
}
