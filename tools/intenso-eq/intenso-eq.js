/* Buscador: si escriben el nombre de un perfume de marca, lleva a su perfume de Intenso.
   El índice (intenso-eq.json) solo guarda huellas, sin nombres en claro. */
(() => {
  const SRC = window.INTENSO_EQ_URL;
  if (!SRC || !window.crypto || !crypto.subtle) return;
  let D = null;
  const load = () => D || (D = fetch(SRC).then((r) => r.json()).then((j) => {
    const m = new Map();
    for (let i = 0; i < j.k.length; i += 8) m.set(j.k.slice(i, i + 6), j.h[parseInt(j.k.slice(i + 6, i + 8), 36)]);
    return { s: j.s, m };
  }).catch(() => null));
  const norm = (s) => s.normalize('NFD').replace(/\p{M}/gu, '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
  const hex = async (s) => {
    const b = new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s))).slice(0, 6);
    return btoa(String.fromCharCode(...b)).replace(/\+/g, '-').replace(/\//g, '_').slice(0, 6);
  };
  async function find(q) {
    const d = await load(); if (!d) return null;
    const t = norm(q).split(' ').filter(Boolean);
    if (!t.length || t.every((w) => /^\d+$/.test(w) || w === 'n')) return null;   // sus números van al buscador normal
    const spans = [];
    for (let i = 0; i < t.length; i++) for (let j = t.length; j > i; j--) spans.push([i, j]);
    spans.sort((a, b) => (b[1] - b[0]) - (a[1] - a[0]) || a[0] - b[0]);
    for (const [i, j] of spans) {
      const w = t.slice(i, j);
      if (w.length === 1 && t.length > 1 && w[0].length < 5) continue;
      const v = d.m.get(await hex(d.s + w.join(' '))); if (v) return v.split('|');
    }
    return null;
  }
  window.intensoEq = find;
  const P = {};
  const prod = (h) => P[h] || (P[h] = fetch(`/products/${h}.js`).then((r) => (r.ok ? r.json() : null)).catch(() => null));
  const money = (c) => (c / 100).toLocaleString('es-ES', { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + ' €';
  async function cards(hs) {
    const ps = (await Promise.all(hs.map(prod))).filter(Boolean);
    return ps.map((p) => `<a class="eqc" href="${p.url}">${p.featured_image ? `<img src="${p.featured_image}&width=160" alt="" width="64" height="85">` : ''}<span><b>${p.title}</b><small>${p.type} · desde ${money(p.price_min)}</small></span><i aria-hidden="true">→</i></a>`).join('');
  }
  async function box(el, hs, title) {
    const html = await cards(hs);
    if (!html) { el.hidden = true; return; }
    el.innerHTML = `<b class="eqh">${title}</b>${html}`; el.hidden = false;
  }
  const go = (hs) => { location.href = `/products/${hs[0]}`; };
  // formularios de búsqueda (portada, cabecera y página de búsqueda)
  document.addEventListener('submit', async (e) => {
    const f = e.target; if (!(f instanceof HTMLFormElement)) return;
    const a = (f.getAttribute('action') || '').split('?')[0];
    if (!/\/search$/.test(a) || f.dataset.eqDone) return;
    const q = (f.querySelector('input[name="q"]') || {}).value || '';
    if (!q.trim()) return;
    e.preventDefault();
    const r = await find(q);
    if (r && r.length === 1) return go(r);
    if (r && r.length > 1) {
      let el = f.parentNode.querySelector('.eqbox');
      if (!el) { el = document.createElement('div'); el.className = 'eqbox'; f.insertAdjacentElement('afterend', el); }
      return box(el, r, 'Te recomendamos');
    }
    f.dataset.eqDone = '1'; HTMLFormElement.prototype.submit.call(f);
  }, true);
  // búsqueda predictiva de la cabecera
  const ps = document.querySelector('[data-psearch]');
  if (ps) {
    let tm; const res = document.querySelector('[data-psearch-res]');
    const el = document.createElement('div'); el.className = 'eqbox'; el.hidden = true;
    if (res) res.insertAdjacentElement('beforebegin', el);
    ps.addEventListener('focus', load, { once: true });
    ps.addEventListener('input', () => {
      clearTimeout(tm); const q = ps.value;
      tm = setTimeout(async () => { const r = q.trim().length > 2 ? await find(q) : null; if (ps.value !== q) return; if (r) box(el, r, 'Para ti'); else el.hidden = true; }, 260);
    });
  }
  const hq = document.getElementById('q-hero'); if (hq) hq.addEventListener('focus', load, { once: true });
  // si llegan a /search con el nombre, directos a su perfume
  if (/\/search$/.test(location.pathname)) {
    const q = new URLSearchParams(location.search).get('q');
    if (q) find(q).then((r) => {
      if (r && r.length === 1) location.replace(`/products/${r[0]}`);
      else if (r) { const m = document.querySelector('main') || document.body; const el = document.createElement('div'); el.className = 'eqbox eqpage'; m.prepend(el); box(el, r, 'Te recomendamos'); }
    });
  }
})();
