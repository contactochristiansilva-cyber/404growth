/* Buscador por nombre de perfume o marca: sugerencias mientras se escribe (aunque haya faltas)
   y, al buscar el nombre exacto, directo a su perfume de Intenso. */
(() => {
  const SRC = window.INTENSO_EQ_URL;
  if (!SRC) return;
  const norm = (s) => s.normalize('NFD').replace(/\p{M}/gu, '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
  const NUM = { 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 7: 'seven', 9: 'nine' };
  let D = null;
  const load = () => D || (D = fetch(SRC).then((r) => r.json()).then((j) => {
    const B = j.b.map(([n, al]) => ({ n, keys: [norm(n), ...al.map(norm)], ps: [] }));
    const P = j.p.map(([n, bi, hs, auto]) => { const p = { n, b: B[bi], hs: hs.split('|'), k: norm(n), auto }; B[bi].ps.push(p); return p; });
    const X = new Map();
    const add = (k, p) => { if (!k) return; const a = X.get(k) || []; if (!a.includes(p)) a.push(p); X.set(k, a); };
    for (const p of P) {
      const ks = [p.k];
      if (p.k.split(' ').some((w) => NUM[w])) ks.push(p.k.split(' ').map((w) => NUM[w] || w).join(' '));
      if ((' ' + p.k + ' ').includes(' n 5 ')) ks.push(p.k.replace('n 5', 'n5'), p.k.replace('n 5', 'no 5'), 'n 5', 'n5');
      p.alts = ks;
      for (const k of ks) {
        if (p.auto) add(k, p);
        for (const bk of p.b.keys) { add(`${k} ${bk}`, p); add(`${bk} ${k}`, p); }
      }
    }
    return { B, P, X };
  }).catch(() => null));

  // distancia de edición (con cambio de dos letras seguidas)
  function dist(a, b, max) {
    if (Math.abs(a.length - b.length) > max) return max + 1;
    let p2 = null, p1 = Array.from({ length: b.length + 1 }, (_, i) => i);
    for (let i = 1; i <= a.length; i++) {
      const c = [i]; let low = i;
      for (let j = 1; j <= b.length; j++) {
        let v = Math.min(p1[j] + 1, c[j - 1] + 1, p1[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
        if (p2 && i > 1 && j > 1 && a[i - 1] === b[j - 2] && a[i - 2] === b[j - 1]) v = Math.min(v, p2[j - 2] + 1);
        c.push(v); if (v < low) low = v;
      }
      if (low > max) return max + 1;
      p2 = p1; p1 = c;
    }
    return p1[b.length];
  }
  // cuánto se parece lo escrito (q) a un nombre (s): 0 = nada
  function score(q, s) {
    if (!s) return 0;
    if (s === q) return 120;
    if (s.startsWith(q)) return 100 - Math.min(30, s.length - q.length) / 3;
    const qs = q.replace(/ /g, ''), ss = s.replace(/ /g, '');
    if (qs.length > 2 && ss.startsWith(qs)) return 95;
    const starts = [0]; for (let i = 0; i < s.length; i++) if (s[i] === ' ') starts.push(i + 1);
    for (let n = 1; n < starts.length; n++) if (s.slice(starts[n]).startsWith(q)) return 85 - n;
    if (q.length > 3 && s.includes(q)) return 70;
    const max = q.length < 4 ? 0 : q.length < 7 ? 1 : 2;
    if (!max) return 0;
    let best = max + 1;
    for (const st of starts) {
      const seg = s.slice(st);
      for (const L of [q.length - 1, q.length, q.length + 1]) if (L > 0 && L <= seg.length) best = Math.min(best, dist(q, seg.slice(0, L), max));
      if (!best) break;
    }
    if (best <= max) return 62 - best * 12;
    if (qs.length >= 5) { const d = dist(qs, ss.slice(0, qs.length), max); if (d <= max) return 58 - d * 12; }
    return 0;
  }
  async function suggest(q, lim = 8) {
    const d = await load(); q = norm(q);
    if (!d || q.length < 2 || /^[0-9 ]+$/.test(q) || /^n [0-9]+$/.test(q)) return [];
    const bs = d.B.map((b) => ({ t: 'b', b, s: Math.max(...b.keys.map((k) => score(q, k))) })).filter((x) => x.s > 0);
    const ps = d.P.map((p) => ({ t: 'p', p, s: Math.max(...p.alts.map((a) => score(q, a)), ...p.b.keys.map((k) => Math.max(score(q, `${k} ${p.k}`), score(q, `${p.k} ${k}`) - 2))) })).filter((x) => x.s > 0);
    bs.sort((a, b) => b.s - a.s || b.b.ps.length - a.b.ps.length);
    // marca escrita entera: la marca y todos sus perfumes
    if (bs[0] && bs[0].s >= 120) return [bs[0], ...bs[0].b.ps.slice().sort((a, b) => a.n.localeCompare(b.n, 'es')).map((p) => ({ t: 'p', p, s: 100 }))];
    ps.sort((a, b) => b.s - a.s || a.p.n.length - b.p.n.length);
    const top = Math.max(bs[0] ? bs[0].s : 0, ps[0] ? ps[0].s : 0);
    const out = bs.filter((x) => x.s >= top - 25).slice(0, 2);
    for (const x of ps) { if (out.length >= lim) break; if (x.s >= top - 40) out.push(x); }
    return out;
  }
  async function find(q) {
    const d = await load(); if (!d) return null;
    const t = norm(q).split(' ').filter(Boolean);
    if (!t.length || t.every((w) => /^[0-9]+$/.test(w) || w === 'n')) return null;
    for (let n = t.length; n > 0; n--) for (let i = 0; i + n <= t.length; i++) {
      if (n === 1 && t.length > 1 && t[i].length < 5) continue;
      const a = d.X.get(t.slice(i, i + n).join(' '));
      if (a) return a.flatMap((p) => p.hs);
    }
    return null;
  }
  window.intensoEq = find; window.intensoSug = suggest;

  const P = {};
  const prod = (h) => P[h] || (P[h] = fetch(`/products/${h}.js`).then((r) => (r.ok ? r.json() : null)).catch(() => null));
  const money = (c) => (c / 100).toLocaleString('es-ES', { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + ' €';
  const esc = (s) => s.replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  async function box(el, hs, title) {
    const ps = (await Promise.all(hs.map(prod))).filter(Boolean);
    if (!ps.length) { el.hidden = true; return; }
    el.innerHTML = `<b class="eqh">${title}</b>` + ps.map((p) => `<a class="eqc" href="${p.url}">${p.featured_image ? `<img src="${p.featured_image}&width=160" alt="" width="52" height="70">` : ''}<span><b>${esc(p.title)}</b><small>${esc(p.type)} · desde ${money(p.price_min)}</small></span><i aria-hidden="true">→</i></a>`).join('');
    el.hidden = false;
  }

  // lista de sugerencias pegada a un buscador
  function attach(input, opts = {}) {
    const form = input.form;
    const wrap = document.createElement('div'); wrap.className = 'eqs-w' + (opts.inline ? ' eqs-in' : '');
    const list = document.createElement('div'); list.className = 'eqs'; list.hidden = true; list.setAttribute('role', 'listbox');
    const multi = document.createElement('div'); multi.className = 'eqbox'; multi.hidden = true;
    wrap.append(list, multi);
    const pos = () => { const r = (form || input).getBoundingClientRect(); wrap.style.left = (r.left + window.scrollX) + 'px'; wrap.style.top = (r.bottom + window.scrollY) + 'px'; wrap.style.width = r.width + 'px'; };
    if (opts.inline) opts.place(wrap); else { wrap.classList.add('eqs-abs'); document.body.append(wrap); window.addEventListener('resize', () => { if (!list.hidden || !multi.hidden) pos(); }); }
    let items = [], sel = -1, tm, seq = 0;
    const close = () => { list.hidden = true; sel = -1; input.setAttribute('aria-expanded', 'false'); };
    const pick = async (it) => {
      if (it.t === 'b') { input.value = it.b.n + ' '; input.focus(); run(); return; }
      close();
      if (it.p.hs.length === 1) { location.href = `/products/${it.p.hs[0]}`; return; }
      box(multi, it.p.hs, 'Te recomendamos');
    };
    const paint = () => {
      list.innerHTML = items.map((it, i) => it.t === 'b'
        ? `<button type="button" role="option" class="eqs-i${i === sel ? ' is-on' : ''}" data-i="${i}"><b>${esc(it.b.n)}</b><small>Marca · ${it.b.ps.length} ${it.b.ps.length === 1 ? 'perfume' : 'perfumes'}</small></button>`
        : `<button type="button" role="option" class="eqs-i${i === sel ? ' is-on' : ''}" data-i="${i}"><b>${esc(it.p.n)}</b><small>${esc(it.p.b.n)}</small></button>`).join('');
      list.hidden = !items.length; input.setAttribute('aria-expanded', items.length ? 'true' : 'false');
    };
    const run = async () => {
      const q = input.value, my = ++seq; multi.hidden = true;
      if (!opts.inline) pos();
      const r = q.trim().length >= 2 ? await suggest(q) : [];
      if (my !== seq) return;
      items = r; sel = -1; paint();
    };
    input.setAttribute('aria-autocomplete', 'list');
    input.addEventListener('focus', () => { load(); if (input.value.trim().length >= 2) run(); });
    input.addEventListener('input', () => { clearTimeout(tm); tm = setTimeout(run, 90); });
    input.addEventListener('keydown', (e) => {
      if (list.hidden || !items.length) return;
      if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
        e.preventDefault();
        if (e.key === 'ArrowDown') sel = sel >= items.length - 1 ? -1 : sel + 1; else sel = sel <= -1 ? items.length - 1 : sel - 1;
        paint();
      } else if (e.key === 'Enter' && sel >= 0) { e.preventDefault(); e.stopPropagation(); pick(items[sel]); }
      else if (e.key === 'Escape') close();
    });
    list.addEventListener('mousedown', (e) => e.preventDefault());
    list.addEventListener('click', (e) => { const b = e.target.closest('[data-i]'); if (b) pick(items[+b.dataset.i]); });
    document.addEventListener('click', (e) => { if (!wrap.contains(e.target) && e.target !== input) close(); });
    return { multi, close, pos };
  }

  const boxes = new WeakMap();
  const hero = document.getElementById('q-hero');
  if (hero) boxes.set(hero.form, attach(hero));
  const top = document.querySelector('[data-psearch]');
  if (top) {
    const res = document.querySelector('[data-psearch-res]');
    boxes.set(top.form || top, attach(top, { inline: true, place: (w) => (res ? res.insertAdjacentElement('beforebegin', w) : top.insertAdjacentElement('afterend', w)) }));
  }
  document.querySelectorAll('main form[action$="/search"] input[name="q"]').forEach((i) => { if (i !== hero && i !== top) boxes.set(i.form, attach(i)); });

  // al buscar: nombre exacto -> su perfume; si hay dos, se enseñan; si no, búsqueda normal
  document.addEventListener('submit', async (e) => {
    const f = e.target; if (!(f instanceof HTMLFormElement)) return;
    const a = (f.getAttribute('action') || '').split('?')[0];
    if (!a.endsWith('/search') || f.dataset.eqDone) return;
    const q = (f.querySelector('input[name="q"]') || {}).value || '';
    if (!q.trim()) return;
    e.preventDefault();
    const r = await find(q);
    if (r && r.length === 1) { location.href = `/products/${r[0]}`; return; }
    const bx = boxes.get(f);
    if (r && r.length > 1 && bx) { bx.close(); bx.pos(); box(bx.multi, r, 'Te recomendamos'); return; }
    f.dataset.eqDone = '1'; HTMLFormElement.prototype.submit.call(f);
  }, true);

  if (location.pathname.endsWith('/search')) {
    const q = new URLSearchParams(location.search).get('q');
    if (q) find(q).then((r) => {
      if (r && r.length === 1) location.replace(`/products/${r[0]}`);
      else if (r) { const m = document.querySelector('main') || document.body; const el = document.createElement('div'); el.className = 'eqbox eqpage'; m.prepend(el); box(el, r, 'Te recomendamos'); }
    });
  }
})();
