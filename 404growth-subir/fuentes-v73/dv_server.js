/* ---------- v72 · v73 · Entregables (14/11/2026): la fecha de entrega de la tienda de cada cliente que ya ha pagado, con su cuenta atrás ----------
   v72: Chris: «en entregables solamente fechas de entrega de tienda, por cliente, donde yo defino la fecha manualmente y se activa una
   cuenta atrás; esto será solo para mí, no para el cliente». Nada del portal lee esta colección.
   v73: Chris: «ahí debe entrar cada cliente que yo notifique en admin que ha pagado». Un cliente entra cuando en Facturación se marca
   como cobrado un pago único o la primera mitad (kind 'one' o 'split') con cobro desde DELIV_FROM. Las cuotas mensuales no cuentan.
   docs (coll 'deliv'): id = el del cliente (c_…) o, si el cobro no tiene ficha en Clientes, n_<nombre>. Campos: name, cid, pay (el cobro),
   paidOn, at «AAAA-MM-DDTHH:MM» en hora de España, note, done (cuándo se entregó) y hidden (quitado de la lista a mano: no vuelve solo).
   Si se deshace el cobro, deja de salir y, si no tenía fecha ni nota, se borra. Una fecha puesta antes de cobrar espera sin verse. */
const DELIV_FROM = "2026-11-01";
function dvKey(s) { return String(s || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "").slice(0, 40); }
async function delivSweep(env) {
  const DBq = env.DB, now = Date.now();
  const cl = (await DBq.prepare("SELECT id, name, start_date, archived FROM clients").all()).results || [];
  const byId = {}, byName = {};
  for (const c of cl) { byId[c.id] = c; const k = dvKey(c.name); if (k && !byName[k]) byName[k] = c; }
  const docs = {}, orig = {}, gone = [];
  for (const x of (await DBq.prepare("SELECT id, data FROM docs WHERE coll = 'deliv'").all()).results || []) { docs[x.id] = parse(x.data, {}); orig[x.id] = JSON.stringify(docs[x.id]); }
  const pays = (await DBq.prepare("SELECT id, client_id, client, paid FROM pay WHERE kind IN ('one', 'split') AND paid >= ?1 ORDER BY paid, id").bind(DELIV_FROM).all()).results || [];
  const want = {}, payKey = {};
  for (const p of pays) {
    const n = dvKey(p.client), c = (p.client_id && byId[p.client_id]) || (n && byName[n]);
    const k = c ? c.id : n ? "n_" + n : ""; if (!k) continue;
    payKey[p.id] = k;
    if (!want[k]) want[k] = { name: c ? c.name : str(p.client, 80), cid: c ? c.id : "", pay: p.id, paidOn: p.paid };
  }
  for (const id of Object.keys(docs)) {                       // a charge with no client file that now has one: its date, note… go with it
    const o = docs[id], k2 = o.pay && payKey[o.pay];
    if (!id.startsWith("n_") || want[id] || !k2 || k2 === id) continue;
    const t = docs[k2] || {}; for (const f of ["at", "note", "done", "hidden"]) if (o[f] && !t[f]) t[f] = o[f];
    docs[k2] = t; delete docs[id]; gone.push(id);
  }
  for (const k in want) docs[k] = Object.assign(docs[k] || {}, want[k]);
  for (const k of Object.keys(docs)) {
    const d = docs[k]; if (want[k] || !d.paidOn) continue;   // no longer paid (the charge was undone or deleted): it stops showing
    delete d.paidOn; delete d.pay;
    if (!d.at && !d.note && !d.done) { delete docs[k]; gone.push(k); }
  }
  const q = gone.filter((k) => orig[k] !== undefined).map((k) => DBq.prepare("DELETE FROM docs WHERE coll = 'deliv' AND id = ?1").bind(k));
  for (const k in docs) if (JSON.stringify(docs[k]) !== orig[k]) q.push(DBq.prepare("INSERT INTO docs (coll, id, data, updated) VALUES ('deliv', ?1, ?2, ?3) ON CONFLICT(coll, id) DO UPDATE SET data = excluded.data, updated = excluded.updated").bind(k, JSON.stringify(docs[k]), now));
  for (let i = 0; i < q.length; i += 80) await DBq.batch(q.slice(i, i + 80));
  return { docs: docs, byId: byId };
}
async function delivApi(req, env, p) {
  const m = req.method, DBq = env.DB, now = Date.now();
  if (p === "deliv" && m === "GET") {
    const r = await delivSweep(env), items = [];
    for (const k in r.docs) {
      const d = r.docs[k]; if (!d.paidOn) continue;
      const c = d.cid && r.byId[d.cid];
      items.push({ id: k, name: c ? c.name : d.name || "", cid: d.cid || "", start: c ? c.start_date || "" : "", archived: c ? !!c.archived : false, paidOn: d.paidOn, at: d.at || "", note: d.note || "", done: d.done || null, hidden: d.hidden || null });
    }
    items.sort((a, b) => a.name.localeCompare(b.name, "es"));
    return json({ items: items, from: DELIV_FROM });
  }
  const q = /^deliv\/((?:c|n)_[A-Za-z0-9_-]{2,44})$/.exec(p);
  if (q && m === "POST") {
    const b = await body(req); if (!b) return bad("body");
    const row = await DBq.prepare("SELECT data FROM docs WHERE coll = 'deliv' AND id = ?1").bind(q[1]).first();
    const d = row ? parse(row.data, {}) : null;
    if (!d || !d.paidOn) return bad("missing", 404);          // only clients whose payment is marked as cobrado are here
    if (b.at !== undefined) {
      const at = typeof b.at === "string" ? b.at.trim() : "";
      if (at && !/^20\d\d-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])T([01]\d|2[0-3]):[0-5]\d$/.test(at)) return bad("date");
      if (at !== (d.at || "")) d.done = null;
      d.at = at;
    }
    if (b.note !== undefined) d.note = str(b.note, 200);
    if (b.done !== undefined) { if (b.done && !d.at) return bad("date"); d.done = b.done ? now : null; }
    if (b.hide !== undefined) d.hidden = b.hide ? now : null;
    await DBq.prepare("INSERT INTO docs (coll, id, data, updated) VALUES ('deliv', ?1, ?2, ?3) ON CONFLICT(coll, id) DO UPDATE SET data = excluded.data, updated = excluded.updated").bind(q[1], JSON.stringify(d), now).run();
    return json({ ok: true, item: d });
  }
  return bad("missing", 404);
}
