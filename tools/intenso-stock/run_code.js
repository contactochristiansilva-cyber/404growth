const LINES = { Esenciales: 1, Nicho: 1, Extractos: 1 };
const TOTAL = 500;
const AVISO = 150; // 30 % de 500 ml

function ml(s) {
  const m = String(s || '').match(/(\d+)\s*ml/i);
  return m ? parseInt(m[1], 10) : 0;
}
function norm(s) {
  return String(s || '').replace(/\s+/g, ' ').trim().toLowerCase();
}

export default function main(input) {
  const need = {};
  const add = (line, title, m) => {
    if (!LINES[line] || !title || !m) return;
    const k = line + '|' + norm(title);
    need[k] = (need[k] || 0) + m;
  };

  for (const li of input.order.lineItems || []) {
    const p = li.product || {};
    const q = li.quantity || 0;
    const t = p.productType;
    const at = {};
    for (const a of li.customAttributes || []) at[a.key] = a.value;

    if (LINES[t]) {
      add(t, p.title, ml(li.variantTitle) * q);
    } else if (t === 'Decant') {
      if (at['Perfume']) add(String(li.variantTitle || '').trim(), at['Perfume'], 5 * q);
    } else if (t === 'Pack') {
      const line = String(p.title || '').trim().split(/\s+/).pop();
      const s = ml(li.variantTitle);
      for (const k in at) {
        if (/^Perfume \d+$/.test(k) && at[k]) add(line, at[k], s * q);
      }
    }
  }

  const updates = [];
  for (const pr of input.getProductData || []) {
    const k = pr.productType + '|' + norm(pr.title);
    if (!need[k]) continue;
    const vendido = need[k];
    delete need[k];
    const raw = pr.mlEnStock && pr.mlEnStock.value;
    const antes = raw !== null && raw !== undefined && raw !== '' && !isNaN(parseInt(raw, 10)) ? parseInt(raw, 10) : TOTAL;
    const queda = Math.max(0, antes - vendido);
    const items = (pr.variants || []).map((v) => {
      const s = ml(v.title);
      return { id: v.inventoryItem.id, qty: s > 0 ? Math.floor(queda / s) : 0 };
    });
    updates.push({
      productId: pr.id,
      titulo: pr.title,
      linea: pr.productType,
      ml: queda,
      antes,
      vendido,
      aviso: antes >= AVISO && queda < AVISO,
      pct: Math.round((queda * 100) / TOTAL),
      items,
    });
  }
  return { updates };
}
