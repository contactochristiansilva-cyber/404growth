/* ---------- v72 · Entregables (14/11/2026): la fecha de entrega de la tienda de cada cliente, con su cuenta atrás ----------
   Chris: «en entregables solamente fechas de entrega de tienda, por cliente, donde yo defino la fecha manualmente y se activa una
   cuenta atrás; esto será solo para mí, no para el cliente». Va en docs (coll 'deliv', id = el del cliente): nada del portal lo lee.
   at = «AAAA-MM-DDTHH:MM» en hora de España; done = cuándo se marcó como entregada; note = una nota corta. */
async function delivApi(req, env, p) {
  const m = req.method, DBq = env.DB, now = Date.now();
  if (p === "deliv" && m === "GET") {
    const cl = (await DBq.prepare("SELECT id, name, start_date, archived FROM clients ORDER BY name COLLATE NOCASE").all()).results || [];
    const items = {};
    for (const x of (await DBq.prepare("SELECT id, data, updated FROM docs WHERE coll = 'deliv'").all()).results || []) items[x.id] = Object.assign(parse(x.data, {}), { upd: x.updated });
    return json({ clients: cl.map((c) => ({ id: c.id, name: c.name, start: c.start_date || "", archived: !!c.archived })), items: items });
  }
  const q = /^deliv\/(c_[A-Za-z0-9_-]{3,40})$/.exec(p);
  if (q && m === "POST") {
    if (!(await DBq.prepare("SELECT id FROM clients WHERE id = ?1").bind(q[1]).first())) return bad("missing", 404);
    const b = await body(req); if (!b) return bad("body");
    const row = await DBq.prepare("SELECT data FROM docs WHERE coll = 'deliv' AND id = ?1").bind(q[1]).first();
    const d = row ? parse(row.data, {}) : {};
    if (b.at !== undefined) {
      const at = typeof b.at === "string" ? b.at.trim() : "";
      if (at && !/^20\d\d-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])T([01]\d|2[0-3]):[0-5]\d$/.test(at)) return bad("date");
      if (at !== d.at) d.done = null;
      d.at = at;
    }
    if (b.note !== undefined) d.note = str(b.note, 200);
    if (b.done !== undefined) { if (b.done && !d.at) return bad("date"); d.done = b.done ? now : null; }
    if (!d.at && !d.note) { await DBq.prepare("DELETE FROM docs WHERE coll = 'deliv' AND id = ?1").bind(q[1]).run(); return json({ ok: true, item: null }); }
    await DBq.prepare("INSERT INTO docs (coll, id, data, updated) VALUES ('deliv', ?1, ?2, ?3) ON CONFLICT(coll, id) DO UPDATE SET data = excluded.data, updated = excluded.updated").bind(q[1], JSON.stringify(d), now).run();
    return json({ ok: true, item: d });
  }
  return bad("missing", 404);
}
