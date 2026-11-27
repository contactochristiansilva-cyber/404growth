
/* ---------- v85 (27/11/2026): avisos de las mensualidades ----------
   Chris: «con cada cliente el cual cobre la primera mensualidad se tiene que activar de manera automática el que todos los meses
   me llegue una notificación el día de antes y el día exacto en el que hay que cobrarle». Cuenta cada cobro mensual (pay.kind 'rec')
   sin cobrar de un plan activo que ya tiene alguna cuota cobrada: el día antes («manda la factura») y el mismo día, desde las 9:00
   de Madrid. Cada aviso sale una sola vez (meta brem:<cobro>:p|d). */
const BR_HOUR = 9;
const BR_FIX_KEY = "brfix_20261127";    // Kiss of Life: el cobro del 27/11 quedó apuntado en la cuota de diciembre
const BR_TEST_KEY = "brtest_20261127";  // Chris pidió una prueba de los dos avisos: sale una vez, al subir el admin
function brParts(ms) { const o = {}; new Intl.DateTimeFormat("en-US", { timeZone: CAL_TZ, hourCycle: "h23", year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit" }).formatToParts(new Date(ms)).forEach((x) => { o[x.type] = x.value; }); return { day: o.year + "-" + o.month + "-" + o.day, h: Number(o.hour) }; }
function brAdd(d, n) { const t = new Date(d + "T12:00:00Z"); t.setUTCDate(t.getUTCDate() + n); return t.toISOString().slice(0, 10); }
function brLong(d) { return new Date(d + "T12:00:00Z").toLocaleDateString("es-ES", { timeZone: "UTC", day: "numeric", month: "long" }); }
function brMoney(c, cur) { try { return (c / 100).toLocaleString("es-ES", { style: "currency", currency: cur || "EUR", maximumFractionDigits: c % 100 ? 2 : 0 }); } catch (e) { return (c / 100) + " " + (cur || "EUR"); } }
function brMsg(r, today, pre) {
  const amt = brMoney(r.amount, r.cur), tag = "brem:" + r.id + ":" + (today ? "d" : "p");
  return today
    ? { title: (pre || "") + "Hoy toca cobrar · " + r.client, body: "Hoy hay que cobrarle la mensualidad a " + r.client + " (" + amt + "). Cuando la cobres, pulsa «Cobrado hoy» en Facturación.", tag: tag, url: "/admin#facturacion" }
    : { title: (pre || "") + "Mañana toca cobrar · " + r.client, body: "Mañana, " + brLong(r.due) + ", hay que cobrarle la mensualidad a " + r.client + " (" + amt + "). Manda hoy la factura para poder cobrarla.", tag: tag, url: "/admin#facturacion" };
}
async function brFix(env) {
  const DBq = env.DB; if (await getMeta(env, BR_FIX_KEY)) return;
  const a = await DBq.prepare("SELECT * FROM pay WHERE id = 'p_fjP5H1zNFLdt_1'").first(), z = await DBq.prepare("SELECT id FROM pay WHERE id = 'p_fjP5H1zNFLdt_0'").first();
  if (a && !z && a.paid === "2026-11-27" && a.due === "2026-12-27") await DBq.batch([
    DBq.prepare("INSERT INTO pay (id, client_id, client, concept, amount, cur, kind, grp, n, due, paid, note, created) VALUES ('p_fjP5H1zNFLdt_0', ?1, ?2, ?3, ?4, ?5, 'rec', ?6, 1, '2026-11-27', '2026-11-27', '', ?7)").bind(a.client_id || "", a.client, a.concept || "", a.amount, a.cur, a.grp, (a.created || Date.now()) - 1),
    DBq.prepare("UPDATE pay SET paid = '' WHERE id = 'p_fjP5H1zNFLdt_1'"),
  ]);
  await setMeta(env, BR_FIX_KEY, "1");
}
async function billRemind(env, nowMs) {
  const DBq = env.DB, t = brParts(nowMs || Date.now());
  await brFix(env);
  if (!(await getMeta(env, BR_TEST_KEY))) {
    await setMeta(env, BR_TEST_KEY, "1");
    const ex = { id: "prueba", client: "Kiss of Life", amount: 49000, cur: "EUR", due: "2026-12-27" };
    try { await pushAll(env, brMsg(ex, false, "Prueba · ")); await pushAll(env, brMsg(ex, true, "Prueba · ")); } catch (e) {}
  }
  if (t.h < BR_HOUR) return { skip: "hour" };
  await plansRun(env);
  const rows = (await DBq.prepare("SELECT p.id, p.client, p.amount, p.cur, p.due FROM pay p JOIN plans pl ON pl.id = p.grp WHERE p.kind = 'rec' AND pl.active = 1 AND (p.paid IS NULL OR p.paid = '') AND p.due IN (?1, ?2) AND EXISTS (SELECT 1 FROM pay q WHERE q.grp = p.grp AND q.kind = 'rec' AND q.paid IS NOT NULL AND q.paid <> '')").bind(t.day, brAdd(t.day, 1)).all()).results || [];
  let sent = 0;
  for (const r of rows) {
    const today = r.due === t.day, k = "brem:" + r.id + ":" + (today ? "d" : "p");
    if (await getMeta(env, k)) continue;
    await setMeta(env, k, String(Date.now()));
    try { await pushAll(env, brMsg(r, today)); sent++; } catch (e) {}
  }
  return { sent: sent };
}
