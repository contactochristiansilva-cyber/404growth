// v71 · presupuesto aceptado → cobro pendiente en Facturación (13/11/2026). Chris: «cuando le doy a presupuesto aceptado se pase a facturación
// pendiente de darle a cobrado hoy, siempre». Al aceptar: el pago único entra como cobro sin cobrar (vence el día que se acepta) y la cuota al mes
// como cobro mensual que empieza ese día. Si ya había un cobro igual de ese cliente (mismo importe), se une a ese y no se duplica.
// Volver a pendiente o a no aceptado quita lo que se creó y no se había cobrado. Lo cobrado no se toca nunca.
// d.bill = { cid, client, day, pay, payMade, plan, planMade, legacy }. Los presupuestos que ya estaban aceptados antes de la v71 solo reciben
// el pago único (legacy: no se sabe desde qué mes va la cuota).
const QB_KEY = "quotes_bill_v71";
const madridDay = () => new Intl.DateTimeFormat("en-CA", { timeZone: "Europe/Madrid" }).format(new Date());
const qbPayId = (qid) => ("p_q_" + qid.slice(2)).slice(0, 32);
const qbPlanId = (qid) => ("pl_" + qid.slice(2)).slice(0, 23);
async function qBillSync(env, qid, d, legacy) {
  const DBq = env.DB, now = Date.now(), q = [], b = Object.assign({}, d.bill || {});
  if (!b.day) b.day = madridDay();
  if (legacy) b.legacy = 1;
  if (b.client === undefined) {
    const name = String(d.name || "").trim();
    const c = name ? await DBq.prepare("SELECT id, name FROM clients WHERE lower(name) = lower(?1) ORDER BY archived, created LIMIT 1").bind(name).first() : null;
    b.cid = c ? c.id : ""; b.client = c ? c.name : str(name, 80) || "Presupuesto";
  }
  const once = Math.round((Number(d.once) || 0) * 100), mon = Math.round((Number(d.monthly) || 0) * 100);
  const what = str(d.what || "", 120) || "Presupuesto aceptado";
  const unpaid = "(paid IS NULL OR paid = '')";
  // pago único
  if (b.pay && b.payMade) {
    if (once > 0) q.push(DBq.prepare("UPDATE pay SET amount = ?2, concept = ?3 WHERE id = ?1 AND " + unpaid).bind(b.pay, once, what));
    else { q.push(DBq.prepare("DELETE FROM pay WHERE id = ?1 AND " + unpaid).bind(b.pay)); delete b.pay; delete b.payMade; }
  } else if (!b.pay && once > 0) {
    const rows = (await DBq.prepare("SELECT id, kind, grp, amount FROM pay WHERE kind IN ('one', 'split') AND ((?1 <> '' AND client_id = ?1) OR lower(client) = lower(?2))").bind(b.cid, b.client).all()).results || [];
    let hit = rows.find((r) => r.kind === "one" && Number(r.amount) === once);
    if (!hit) { const g = {}; for (const r of rows) if (r.kind === "split" && r.grp) g[r.grp] = (g[r.grp] || 0) + Number(r.amount); const k = Object.keys(g).find((x) => g[x] === once); if (k) hit = rows.find((r) => r.grp === k); }
    if (hit) b.pay = hit.id;
    else {
      b.pay = qbPayId(qid); b.payMade = 1;
      q.push(DBq.prepare("INSERT OR IGNORE INTO pay (id, client_id, client, concept, amount, cur, kind, grp, n, due, paid, note, created) VALUES (?1, ?2, ?3, ?4, ?5, 'EUR', 'one', '', 1, ?6, '', 'Presupuesto aceptado', ?7)").bind(b.pay, b.cid, b.client, what, once, b.day, now));
    }
  }
  // cuota al mes
  if (b.plan && b.planMade) {
    if (mon > 0) q.push(DBq.prepare("UPDATE plans SET amount = ?2 WHERE id = ?1").bind(b.plan, mon));
    else { q.push(...qbPlanUndo(env, b.plan)); delete b.plan; delete b.planMade; }
  } else if (!b.plan && mon > 0 && !b.legacy) {
    const pl = await DBq.prepare("SELECT id FROM plans WHERE active = 1 AND amount = ?3 AND ((?1 <> '' AND client_id = ?1) OR lower(client) = lower(?2)) LIMIT 1").bind(b.cid, b.client, mon).first();
    if (pl) b.plan = pl.id;
    else {
      b.plan = qbPlanId(qid); b.planMade = 1;
      q.push(DBq.prepare("INSERT OR IGNORE INTO plans (id, client_id, client, concept, amount, cur, start, active, created) VALUES (?1, ?2, ?3, ?4, ?5, 'EUR', ?6, 1, ?7)").bind(b.plan, b.cid, b.client, str("Cuota mensual · " + what, 120), mon, b.day, now));
    }
  }
  return { bill: b, q: q };
}
function qbPlanUndo(env, id) {
  const DBq = env.DB;
  return [DBq.prepare("DELETE FROM pay WHERE grp = ?1 AND (paid IS NULL OR paid = '')").bind(id),
    DBq.prepare("DELETE FROM plans WHERE id = ?1 AND NOT EXISTS (SELECT 1 FROM pay WHERE grp = ?1)").bind(id),
    DBq.prepare("UPDATE plans SET active = 0, ended = ?2 WHERE id = ?1").bind(id, madridDay())];
}
function qBillUndo(env, b) {
  const q = []; if (!b) return q;
  if (b.pay && b.payMade) q.push(env.DB.prepare("DELETE FROM pay WHERE id = ?1 AND (paid IS NULL OR paid = '')").bind(b.pay));
  if (b.plan && b.planMade) q.push(...qbPlanUndo(env, b.plan));
  return q;
}
// los aceptados que aún no están en Facturación (los de antes de la v71, o los que se aceptan desde el código con Q_SET)
async function quotesBillSweep(env) {
  const DBq = env.DB, legacy = !(await DBq.prepare("SELECT v FROM meta WHERE k = ?1").bind(QB_KEY).first());
  const all = ((await DBq.prepare("SELECT id, data FROM docs WHERE coll = 'quotes'").all()).results || []).map((x) => ({ id: x.id, d: parse(x.data, {}) }));
  for (const x of all) {
    if (x.d.status !== "accepted" || x.d.bill) continue;
    const r = await qBillSync(env, x.id, x.d, legacy); x.d.bill = r.bill;
    await DBq.batch(r.q.concat([DBq.prepare("UPDATE docs SET data = ?1, updated = ?2 WHERE coll = 'quotes' AND id = ?3").bind(JSON.stringify(x.d), Date.now(), x.id)]));
  }
  if (legacy) await DBq.prepare("INSERT INTO meta (k, v) VALUES (?1, '1') ON CONFLICT(k) DO NOTHING").bind(QB_KEY).run();
}
