// Lote 39 (17/11/2026): Google Flow en modo manual, sin agente, todo desde la consola de la pestaña del proyecto.
// 1) Pestaña del proyecto: pegar PROJECT y luego mandar los trabajos con mkbat39.py (lotes de browser_batch:
//    JS para elegir la referencia y escribir el texto + teclas REALES Down/Return para añadirla y Return para enviar).
//    El formato (3:4, 16:9, 9:16) se cambia a mano en el chip del modelo; por eso q39s.json va ordenado por formato.
// 2) Otra pestaña del mismo proyecto, en /edit/<id de la foto más nueva>: pegar VIEWER y __run(700) sin esperar;
//    recorre de la más nueva a la más vieja con un ArrowRight sintético y guarda cada foto por su texto exacto.
// 3) Pestañas flow.google.com/robots.txt con RECEIVER (una descarga por pestaña) y SEND desde el visor.

// ---------- PROJECT ----------
window.__Q = JSON.parse(localStorage.__q39);            // q39s.json, cargado antes en localStorage
window.__s = (ms) => new Promise((r) => setTimeout(r, ms));
window.__ed = () => [...document.querySelectorAll('div[contenteditable=true]')].find((e) => (e.getAttribute('aria-label') || '').includes('crear')) || document.querySelector('div[contenteditable=true]');
window.__pt = (i) => { const e = __ed(); e.focus(); document.execCommand('selectAll', false); document.execCommand('insertText', false, __Q[i].t); return e.textContent.length; };
// devuelve «largo del texto / referencias en la petición / referencias que debía llevar»
window.__pt2 = (i) => { const L = __pt(i); const n = __ed().parentElement.parentElement.parentElement.querySelectorAll('img').length; return L + '/' + n + '/' + __Q[i].r.length; };
window.__plus = () => [...document.querySelectorAll('button')].find((b) => (b.getAttribute('aria-label') || '').startsWith('Añadir ingredientes'));
window.__srch = async (txt) => {   // el buscador del selector de recursos solo acepta el valor con el setter nativo + evento input
  let inp = null;
  for (let k = 0; k < 30 && !inp; k++) { inp = document.querySelector('.cdk-overlay-container input[placeholder="Buscar recursos"]'); if (!inp) await __s(100); }
  Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set.call(inp, txt);
  inp.dispatchEvent(new Event('input', { bubbles: true }));
  await __s(1300); return txt;
};
window.__pr = async (i, k) => { if (!document.querySelector('.cdk-overlay-container input[placeholder="Buscar recursos"]')) __plus().click(); return await __srch(__Q[i].r[k]); };
// después de __pr: tecla real Down + Return añade la primera coincidencia; después __pt2(i) y Return real envía.

// ---------- VIEWER (pestaña /edit/<id>) ----------
window.__Q = JSON.parse(localStorage.__q39).concat(JSON.parse(localStorage.__q39r || '[]'));
window.__s = (ms) => new Promise((r) => setTimeout(r, ms));
window.__nz = (s) => s.replace(/\s+/g, ' ').trim();
window.__TM = {}; __Q.forEach((q) => { __TM[__nz(q.t)] = q; });
window.__big = () => { let b = null, ba = 0; for (const i of document.querySelectorAll('img')) { const r = i.getBoundingClientRect(); const a = r.width * r.height; if (a > ba && i.complete && i.naturalWidth > 200) { ba = a; b = i; } } return b; };
window.__jpg = async (img) => { const r = await fetch(img.src); const bm = await createImageBitmap(await r.blob()); const c = document.createElement('canvas'); c.width = bm.width; c.height = bm.height; c.getContext('2d').drawImage(bm, 0, 0); return { d: c.toDataURL('image/jpeg', 0.92), w: bm.width, h: bm.height }; };
window.__R = {}; window.__st = { n: 0, seen: 0, miss: [], done: false };
window.__run = async (max) => {   // la primera vez que sale una clave se queda (la más nueva gana: así entran las rehechas)
  for (let k = 0; k < max; k++) {
    const tp = document.querySelector('.text-part'); const t = tp ? __nz(tp.textContent) : '';
    if (t) { const q = __TM[t]; if (q) { const kk = q.s + '__' + q.id; if (!__R[kk]) { __R[kk] = await __jpg(__big()); __R[kk].i = q.i; __st.n++; } } else __st.miss.push(t.slice(0, 50)); }
    __st.seen++; const before = location.pathname; const prev = (__big() || {}).src || '';
    document.body.dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowRight', code: 'ArrowRight', keyCode: 39, which: 39, bubbles: true }));
    let w = 0; while (location.pathname === before && w < 60) { await __s(100); w++; }
    if (location.pathname === before) { __st.done = 'stuck'; return; }   // si se queda en la primera: document.activeElement.blur() y otra vez
    let w2 = 0; while (w2 < 60) { const im = __big(); if (im && im.complete && im.src !== prev) break; await __s(100); w2++; }
    await __s(150);
  }
  __st.done = true;
};

// ---------- RECEIVER (cada pestaña flow.google.com/robots.txt, con su nombre r1, r2…) ----------
window.__me = 'r1'; { const bc = new BroadcastChannel('l39'); bc.onmessage = (e) => { if (e.data.to !== __me) return; const a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([e.data.json], { type: 'application/json' })); a.download = e.data.name; document.body.appendChild(a); a.click(); bc.postMessage({ ack: __me, len: e.data.json.length }); }; }

// ---------- SEND (en el visor): 4 trozos de ~27 MB → ~/Downloads/l39-ai-N.json → device_stage_files → l38/unflow.py ----------
// const bc = new BroadcastChannel('l39'); const ks = Object.keys(__R).sort(); const per = Math.ceil(ks.length / 4);
// for (let c = 0; c < 4; c++) { const sub = {}; ks.slice(c * per, (c + 1) * per).forEach((k) => sub[k] = __R[k]); bc.postMessage({ to: 'r' + (c + 1), name: 'l39-ai-' + (c + 1) + '.json', json: JSON.stringify(sub) }); await __s(1500); }
