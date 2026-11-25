// Comprobación de webs (lote 48), en una pestaña de r.jina.ai. W.run([['cuenta','dominio'], …]); una petición cada ~3,4 s.
window.W = window.W || { out: {}, st: { n: 0, err: 0 } };
W.s = (ms) => new Promise((r) => setTimeout(r, ms));
W.get = async (url) => { const r = await fetch('/' + url, { headers: { 'x-return-format': 'text' } }); const t = await r.text(); await W.s(3400); return { c: r.status, t }; };
W.one = async (d) => {
  const o = { d };
  try {
    const a = await W.get('https://' + d + '/products.json?limit=250');
    const m = a.t.match(/"products"\s*:\s*\[/); if (m) { o.shopify = (a.t.match(/"handle"\s*:/g) || []).length; return o; }
    const b = await W.get('https://' + d + '/wp-json/wc/store/v1/products?per_page=100');
    if (/"prices"\s*:/.test(b.t)) { o.woo = (b.t.match(/"permalink"\s*:/g) || []).length; return o; }
    const h = await W.get('https://' + d + '/');
    o.code = h.c; const t = h.t.toLowerCase(); o.len = t.length;
    o.cart = /añadir al carrito|add to cart|anadir al carrito|añadir a la cesta|comprar ahora|carrito|checkout|tienda online|shop now|cesta/.test(t);
    o.prices = (t.match(/\d+[.,]\d{2}\s?€|€\s?\d+[.,]\d{2}/g) || []).length;
    o.err = /error|not found|404|suspend|parking|domain|dominio|en construcci|próximamente|proximamente|mantenimiento|coming soon|password|contraseña/.test(t.slice(0, 1500)) ? t.slice(0, 160).replace(/\s+/g, ' ') : '';
    o.title = (h.t.match(/Title:\s*(.*)/) || [])[1] || '';
  } catch (e) { o.x = String(e).slice(0, 80); W.st.err++; }
  return o;
};
W.run = async (list) => { for (const [u, d] of list) { if (W.out[u]) continue; W.out[u] = await W.one(d); W.st.n++; } W.done = true; };
'webchk ok';
