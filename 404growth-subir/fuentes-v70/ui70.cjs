const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const errs = [];
  const pg = await b.newPage({ viewport: { width: 1280, height: 900 } });
  pg.on('pageerror', (e) => errs.push('pageerror ' + e.message)); pg.on('console', (m) => { if (m.type() === 'error') errs.push('console ' + m.text()); });
  await pg.goto('http://localhost:8770/admin#archivos'); await pg.waitForSelector('#ar-drop', { timeout: 10000 });
  const r = {}; r.tabs = await pg.$$eval('[data-cbtab]', (x) => x.map((e) => e.textContent + ':' + e.getAttribute('aria-pressed')));
  r.empty = await pg.textContent('.ar-t td.empty');
  await pg.setInputFiles('#ar-in', ['Modelo 303 3T.pdf', 'Seguro coche.jpg', 'Contrato alquiler local.docx']);
  await pg.waitForFunction(() => document.querySelectorAll('.ar-t tr[data-arq]').length === 3, null, { timeout: 20000 });
  r.rows = await pg.$$eval('.ar-t tr[data-arq] b', (x) => x.map((e) => e.textContent));
  r.views = await pg.$$eval('.ar-t tr[data-arq]', (x) => x.map((e) => e.querySelector('a[href*="ver=1"]') ? 'ver' : 'no'));
  await pg.screenshot({ path: 'ui-desk.png', fullPage: true });
  // search
  await pg.fill('#ar-q', 'seguro'); r.search = await pg.$$eval('.ar-t tr[data-arq]', (x) => x.filter((e) => !e.hidden).length);
  await pg.fill('#ar-q', 'zzz'); r.none = await pg.$eval('#ar-none', (e) => !e.hidden); await pg.fill('#ar-q', '');
  // new folder + upload into it
  await pg.click('[data-arnew]'); await pg.fill('#ar-nfn', 'Hacienda'); await pg.click('#f-arnf button[type=submit]');
  await pg.waitForSelector('[data-arf="Hacienda"][aria-pressed=true]'); r.dropText = await pg.textContent('#ar-drop span');
  await pg.setInputFiles('#ar-in', ['Modelo 303 3T.pdf']);
  await pg.waitForFunction(() => document.querySelectorAll('.ar-t tr[data-arq]').length === 1 && /Hacienda/.test(document.querySelector('[data-arf="Hacienda"]').textContent), null, { timeout: 20000 });
  r.folderCount = await pg.textContent('[data-arf="Hacienda"]');
  // rename folder
  await pg.click('[data-arren]'); await pg.fill('#ar-nfn', 'Hacienda 2026'); await pg.click('#f-arnf button[type=submit]');
  await pg.waitForSelector('[data-arf="Hacienda 2026"][aria-pressed=true]');
  // all, edit one, delete one
  await pg.click('[data-arf=""]'); await pg.waitForFunction(() => document.querySelectorAll('.ar-t tr[data-arq]').length === 4);
  const first = await pg.getAttribute('[data-ared]', 'data-ared'); await pg.click('[data-ared="' + first + '"]');
  await pg.fill('#ae-name', 'Contrato del local.docx'); await pg.fill('#ae-folder', 'Contratos'); await pg.fill('#ae-note', 'Vence en 2028'); await pg.click('#f-ared button[type=submit]');
  await pg.waitForSelector('[data-arf="Contratos"]'); r.edited = await pg.$$eval('.ar-t tr[data-arq]', (x) => x.map((e) => e.querySelector('b').textContent + ' | ' + (e.querySelector('.chip') || {}).textContent));
  const del = await pg.getAttribute('[data-ardel]', 'data-ardel'); await pg.click('[data-ardel="' + del + '"]'); await pg.click('[data-ardel="' + del + '"]');
  await pg.waitForFunction(() => document.querySelectorAll('.ar-t tr[data-arq]').length === 3); r.afterDel = 3;
  // view and download
  const pdfRow = await pg.$('.ar-t tr[data-arq*="303"] a[href*="ver=1"]'); const href = await pdfRow.getAttribute('href');
  const resp = await pg.request.get('http://localhost:8770' + href); r.viewType = resp.headers()['content-type'] + ' ' + (await resp.body()).length;
  const [dl] = await Promise.all([pg.waitForEvent('download'), pg.click('.ar-t tr[data-arq*="seguro"] a[download]')]); r.dlName = dl.suggestedFilename();
  // too big: a 51 MB file is refused without uploading
  require('fs').writeFileSync('grande.zip', Buffer.alloc(51 * 1048576));
  await pg.setInputFiles('#ar-in', ['grande.zip']); await pg.waitForSelector('.ar-ui.err'); r.big = await pg.textContent('.ar-ui.err .hint');
  await pg.click('[data-arx]'); r.bigGone = (await pg.$$('.ar-ui.err')).length === 0;
  r.space = await pg.textContent('.ar-sp');
  await pg.screenshot({ path: 'ui-desk2.png', fullPage: true });
  // other tabs still work
  await pg.click('[data-cbtab="res"]'); await pg.waitForSelector('[data-cbtab="res"][aria-pressed=true]'); r.resOk = !!(await pg.$('#cb .cb-per'));
  await pg.click('[data-cbtab="arch"]'); await pg.waitForSelector('#ar-drop');
  // phone
  const m = await b.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 }); m.on('pageerror', (e) => errs.push('m ' + e.message));
  await m.goto('http://localhost:8770/admin#archivos'); await m.waitForSelector('.ar-t tr[data-arq]');
  r.mScroll = await m.evaluate(() => document.documentElement.scrollWidth - innerWidth);
  await m.screenshot({ path: 'ui-mob.png', fullPage: true });
  r.errs = errs; console.log(JSON.stringify(r, null, 1)); await b.close();
})();
