// Lote 42 (22/11/2026): Google Flow en modo manual, como los lotes 39-41.
// Trabajos en localStorage.__q42 (flow/q42.json: [{s, id, f, r:[refs], t, i}], ordenados por formato).
// Por trabajo (mkbat42.py): JS __go(i) (escribe el texto y busca la 1.ª referencia) + tecla REAL «Down Return»;
// __gk(i,k) para la 2.ª y la 3.ª; y clic REAL en la flecha de enviar. Sin referencias: __go0(i).

// ---------- PROJECT ----------
window.__Q = JSON.parse(localStorage.__q42);
window.__s = (ms) => new Promise((r) => setTimeout(r, ms));
window.__ed = () => [...document.querySelectorAll('div[contenteditable=true]')].find((e) => (e.getAttribute('aria-label') || '').includes('crear')) || document.querySelector('div[contenteditable=true]');
window.__pt = (i) => { const e = __ed(); e.focus(); document.execCommand('selectAll', false); document.execCommand('insertText', false, __Q[i].t); return e.textContent.length; };
window.__plus = () => [...document.querySelectorAll('button')].find((b) => (b.getAttribute('aria-label') || '').startsWith('Añadir ingredientes'));
window.__srch = async (txt) => {
  let inp = null;
  for (let k = 0; k < 30 && !inp; k++) { inp = document.querySelector('.cdk-overlay-container input[placeholder="Buscar recursos"]'); if (!inp) await __s(100); }
  if (!inp) return 'sin buscador';
  Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set.call(inp, txt);
  inp.dispatchEvent(new Event('input', { bubbles: true }));
  await __s(1300); return txt;
};
window.__pr = async (i, k) => { if (!document.querySelector('.cdk-overlay-container input[placeholder="Buscar recursos"]')) { const p = __plus(); if (p) p.click(); } return await __srch(__Q[i].r[k]); };
window.__F = JSON.parse(localStorage.__f42 || '[]');
window.__busy = () => { const e = __ed(); return e && e.textContent.trim().length > 0; };   // la petición anterior no se fue
window.__go = async (i) => {
  await __s(2200);
  if (__busy()) { __F.push(__Q[i - 1] ? i - 1 : i); localStorage.__f42 = JSON.stringify(__F); }
  __pt(i); return await __pr(i, 0);
};
window.__go0 = async (i) => { await __s(2200); if (__busy()) { __F.push(i - 1); localStorage.__f42 = JSON.stringify(__F); } return __pt(i); };
window.__gk = async (i, k) => { await __s(1100); return await __pr(i, k); };

// ---------- VIEWER (otra pestaña, en /edit/<id de la foto más nueva>) ----------
// (es el de flow39.js con __q42) — window.__Q = JSON.parse(localStorage.__q42); y el resto igual:
window.__nz = (s) => s.replace(/\s+/g, ' ').trim();
window.__TM = {}; __Q.forEach((q) => { __TM[__nz(q.t)] = q; });
window.__big = () => { let b = null, ba = 0; for (const i of document.querySelectorAll('img')) { const r = i.getBoundingClientRect(); const a = r.width * r.height; if (a > ba && i.complete && i.naturalWidth > 200) { ba = a; b = i; } } return b; };
window.__jpg = async (img) => { const src = img.src.replace(/=[a-z0-9-]+$/i, '=s0'); const r = await fetch(src); const bm = await createImageBitmap(await r.blob()); const c = document.createElement('canvas'); c.width = bm.width; c.height = bm.height; c.getContext('2d').drawImage(bm, 0, 0); return { d: c.toDataURL('image/jpeg', 0.92), w: bm.width, h: bm.height }; };
window.__R = window.__R || {}; window.__st = { n: 0, seen: 0, miss: [], nomatch: 0, done: false };
window.__run = async (max, stopAfter = 40) => {
  let run = 0;
  for (let k = 0; k < max; k++) {
    const tp = document.querySelector('.text-part'); const t = tp ? __nz(tp.textContent) : '';
    if (t) { run = 0; const q = __TM[t]; if (q) { const kk = q.s + '__' + q.id; if (!__R[kk]) { try { __R[kk] = await __jpg(__big()); __R[kk].i = q.i; __st.n++; } catch (e) { __st.miss.push('ERR ' + kk); } } } else { __st.miss.push(t.slice(0, 50)); __st.nomatch++; } }
    else { run++; if (run >= stopAfter) { __st.done = 'fin (subidas)'; return; } }
    __st.seen++; const before = location.pathname; const prev = (__big() || {}).src || '';
    document.body.dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowRight', code: 'ArrowRight', keyCode: 39, which: 39, bubbles: true }));
    let w = 0; while (location.pathname === before && w < 60) { await __s(100); w++; }
    if (location.pathname === before) { __st.done = 'stuck'; return; }
    let w2 = 0; while (w2 < 60) { const im = __big(); if (im && im.complete && im.src !== prev) break; await __s(100); w2++; }
    await __s(150);
  }
  __st.done = true;
};

// ---------- RECEIVER (cada pestaña flow.google.com/robots.txt, con su nombre r1, r2…) ----------
// window.__me = 'r1'; { const bc = new BroadcastChannel('l42'); bc.onmessage = (e) => { if (e.data.to !== __me) return; const a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([e.data.json], { type: 'application/json' })); a.download = e.data.name; document.body.appendChild(a); a.click(); bc.postMessage({ ack: __me, len: e.data.json.length }); }; }
