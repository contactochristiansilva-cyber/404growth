const { chromium, devices } = require('playwright');
(async () => {
  const b = await chromium.launch({ args: ['--autoplay-policy=no-user-gesture-required'] });
  const VP = [[1920,1080,0],[1440,900,0],[1440,760,0],[1366,768,0],[1366,650,0],[1280,720,0],[1280,600,0],[1024,768,0],[932,430,1],[844,390,1],[740,360,1],[667,375,1],[1280,500,0],[820,1180,1],[430,932,1],[430,740,1],[390,844,1],[390,664,1],[375,667,1],[375,548,1],[360,640,1],[360,560,1],[320,568,1]];
  const out = [];
  for (const [w, h, m] of VP) {
    const c = await b.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: 1, isMobile: !!m, hasTouch: !!m });
    const p = await c.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message));
    await p.goto('http://127.0.0.1:8765/book.html', { waitUntil: 'load' }); await p.waitForTimeout(1800);
    const r = await p.evaluate(() => { const q = s => document.querySelector(s).getBoundingClientRect(); const h1 = q('.hero h1'), v = q('#screen'), bt = q('.hero .cta .btn'), go = q('#vgo');
      return { h1: [Math.round(h1.top), Math.round(h1.bottom)], vid: [Math.round(v.top), Math.round(v.bottom), Math.round(v.width)], btn: [Math.round(bt.top), Math.round(bt.bottom)], go: Math.round(go.width), ih: innerHeight, sw: document.documentElement.scrollWidth, vp: document.querySelector('#screen').className, t: +document.querySelector('#vv').currentTime.toFixed(2), muted: document.querySelector('#vv').muted }; });
    out.push(`${w}x${h} h1 ${r.h1} vid ${r.vid} btn ${r.btn} | sobra ${r.ih - r.btn[1]} | scrollW ${r.sw} | ${r.vp} t=${r.t} muted=${r.muted}${errs.length ? ' ERR ' + errs[0] : ''}`);
    if (process.argv[2] && [[1440,900],[1366,650],[390,664],[360,560],[844,390]].some(a => a[0] === w && a[1] === h)) await p.screenshot({ path: `${process.argv[2]}/s_${w}x${h}.png` });
    await c.close();
  }
  console.log(out.join('\n')); await b.close();
})();
