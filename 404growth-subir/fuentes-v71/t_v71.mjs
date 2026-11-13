// Prueba de la v71. Antes: cp ../admin/worker.js w71mod.mjs && echo "export { quotesApi, billing, plansRun, payEdit, planEdit, DDL, qbPayId };" >> w71mod.mjs ; después: node t_v71.mjs
import { makeD1 } from './d1shim.mjs';
import { quotesApi, billing, payEdit, DDL } from './w71mod.mjs';
const env = { DB: makeD1() };
for (const s of DDL) env.DB._db.exec(s);
let ok = 0, ko = 0; const t = (c, m) => { if (c) ok++; else { ko++; console.log('FALLO:', m); } };
const R = async (m, p, b) => { const r = await quotesApi(new Request('https://404growth.com/admin/api/' + p, { method: m, headers: { 'content-type': 'application/json', 'x-404': '1' }, body: b ? JSON.stringify(b) : undefined }), env, p); return { s: r.status, j: await r.json() }; };
const B = async () => (await billing(env)).json();
const db = env.DB._db, now = Date.now();
const today = new Intl.DateTimeFormat('en-CA', { timeZone: 'Europe/Madrid' }).format(new Date());
// estado real del 13/11: clientes, cobros y los cuatro presupuestos, con Intenso, Kiss of Life y Open Fit ya aceptados
db.prepare("INSERT INTO clients (id, name, created) VALUES ('c_ZM1IhO3i0RDR', 'Kiss of Life', 1), ('c_laX5PV3mqsmk', 'Open Fit', 2)").run();
db.prepare("INSERT INTO pay (id, client_id, client, concept, amount, cur, kind, grp, n, due, paid, note, created) VALUES ('p_intenso_tienda', '', 'Intenso Fragancias', 'Tienda', 144000, 'EUR', 'one', '', 1, '2026-11-11', '2026-11-13', '', 1), ('p_2qu78iIY3MVo', 'c_ZM1IhO3i0RDR', 'Kiss of Life', 'Tienda Online KOL', 114000, 'EUR', 'one', '', 1, '2026-11-09', '2026-11-10', '', 2)").run();
for (const k of ['quotes_seed', 'quotes_add_20261111', 'quotes_set_20261113']) db.prepare("INSERT INTO meta (k, v) VALUES (?, '1')").run(k);
const Q = (id, d) => db.prepare("INSERT INTO docs (coll, id, data, updated) VALUES ('quotes', ?, ?, 1)").run(id, JSON.stringify(d));
Q('q_intensofragancias', { name: 'Intenso Fragancias', what: 'Tienda online', once: 1440, monthly: 490, status: 'accepted', created: 5 });
Q('q_carmenvalencia', { name: 'Carmen Valencia', what: 'Tienda online', once: 1380, monthly: 0, status: 'pending', created: 4 });
Q('q_kissoflife', { name: 'Kiss of Life', what: 'Tienda online + plan socio', once: 1140, monthly: 490, status: 'accepted', created: 3 });
Q('q_openfit', { name: 'Open Fit', what: 'Web (pago único, IVA incluido)', once: 2050, monthly: 0, status: 'accepted', created: 2 });
Q('q_antequeracf', { name: 'Antequera CF', what: 'Tienda online completa', once: 2800, monthly: 0, status: 'pending', created: 1 });
// 1. al abrir Facturación (sin pasar por Presupuestos): Open Fit sale pendiente; Intenso y Kiss of Life no se duplican; ninguna cuota se inventa
let b = await B();
const of = b.pays.filter((p) => p.client === 'Open Fit');
t(of.length === 1 && of[0].amount === 205000 && of[0].paid === '' && of[0].due === today && of[0].client_id === 'c_laX5PV3mqsmk' && of[0].kind === 'one', 'Open Fit pendiente en Facturación: ' + JSON.stringify(of));
t(b.pays.filter((p) => p.client === 'Intenso Fragancias').length === 1 && b.pays.filter((p) => p.client === 'Kiss of Life').length === 1, 'Intenso y KoL sin duplicar');
t(b.plans.length === 0, 'sin cuotas inventadas para los aceptados de antes');
b = await B(); t(b.pays.length === 3, 'abrir otra vez no duplica');
// 2. Presupuestos enseña el estado del cobro
let r = await R('GET', 'quotes'); const g = (id) => r.j.quotes.find((q) => q.id === id);
t(g('q_openfit').billPaid === '' && g('q_openfit').bill.payMade === 1, 'Open Fit: pendiente de cobrar');
t(g('q_intensofragancias').billPaid === '2026-11-13' && !g('q_intensofragancias').bill.payMade, 'Intenso: cobrado (unido al cobro que había)');
t(g('q_kissoflife').bill.pay === 'p_2qu78iIY3MVo' && g('q_kissoflife').bill.legacy === 1, 'KoL: unido por cliente e importe');
// 3. Cobrado hoy en Facturación → en Presupuestos sale cobrado
await payEdit(new Request('https://x/', { method: 'POST', body: JSON.stringify({ paid: today }) }), env, of[0].id);
r = await R('GET', 'quotes'); t(g('q_openfit').billPaid === today, 'Open Fit cobrado');
// 4. aceptar uno nuevo con pago único y cuota: entra el cobro pendiente y la cuota mensual (con su primer mes)
r = await R('POST', 'quotes/q_carmenvalencia', { monthly: 300 }); t(r.s === 200 && !r.j.pay, 'editar pendiente no crea nada');
r = await R('POST', 'quotes/q_carmenvalencia', { status: 'accepted' }); t(r.j.pay && r.j.plan, 'aceptar → cobro y cuota');
b = await B(); let cv = b.pays.filter((p) => p.client === 'Carmen Valencia');
t(cv.some((p) => p.kind === 'one' && p.amount === 138000 && p.paid === '' && p.due === today) && cv.some((p) => p.kind === 'rec' && p.amount === 30000 && p.due === today), 'Carmen: pago único y primer mes pendientes: ' + JSON.stringify(cv.map((p) => [p.kind, p.amount, p.due])));
t(b.plans.length === 1 && b.plans[0].start === today && b.plans[0].client === 'Carmen Valencia', 'cuota mensual creada');
// 5. aceptar dos veces seguidas o recargar no duplica
await R('POST', 'quotes/q_carmenvalencia', { status: 'accepted' }); await R('GET', 'quotes'); b = await B();
const cvp = b.pays.filter((p) => p.client === 'Carmen Valencia'); t(cvp.filter((p) => p.kind === 'one').length === 1 && new Set(cvp.map((p) => p.n + p.kind)).size === cvp.length && b.plans.length === 1, 'sin duplicados: ' + JSON.stringify(cvp.map((p) => [p.kind, p.n, p.due])));
// 6. cambiar el importe mientras está aceptado y sin cobrar
await R('POST', 'quotes/q_carmenvalencia', { once: 1500 }); b = await B();
t(b.pays.find((p) => p.client === 'Carmen Valencia' && p.kind === 'one').amount === 150000, 'importe actualizado');
// 7. volver a pendiente quita lo que no estaba cobrado
r = await R('POST', 'quotes/q_carmenvalencia', { status: 'pending' }); t(r.j.undone === true, 'deshacer avisa');
b = await B(); t(b.pays.filter((p) => p.client === 'Carmen Valencia').length === 0 && b.plans.length === 0, 'Carmen fuera de Facturación');
r = await R('GET', 'quotes'); t(!g('q_carmenvalencia').bill, 'sin bill');
// 8. no aceptado con algo ya cobrado: lo cobrado se queda
r = await R('POST', 'quotes/q_antequeracf', { status: 'accepted' }); b = await B(); const ac = b.pays.find((p) => p.client === 'Antequera CF');
t(ac && ac.amount === 280000, 'Antequera entra');
await payEdit(new Request('https://x/', { method: 'POST', body: JSON.stringify({ paid: today }) }), env, ac.id);
await R('POST', 'quotes/q_antequeracf', { status: 'rejected' }); b = await B();
t(b.pays.filter((p) => p.client === 'Antequera CF').length === 1, 'lo cobrado no se borra');
// 9. si ya habían metido el cobro a mano antes de aceptar, se une a ese
db.prepare("INSERT INTO pay (id, client_id, client, concept, amount, cur, kind, grp, n, due, paid, note, created) VALUES ('p_manual0001', '', 'nuevo cliente', 'a mano', 99900, 'EUR', 'one', '', 1, '2026-11-12', '', '', 9)").run();
r = await R('POST', 'quotes', { name: 'Nuevo Cliente', what: 'Web', once: 999 }); const nid = r.j.id;
await R('POST', 'quotes/' + nid, { status: 'accepted' }); b = await B();
t(b.pays.filter((p) => p.client.toLowerCase() === 'nuevo cliente').length === 1, 'unido al cobro hecho a mano');
// 10. un cobro creado y borrado a mano en Facturación no vuelve
r = await R('POST', 'quotes', { name: 'Borra Yo', what: 'Web', once: 100 }); const bid = r.j.id; await R('POST', 'quotes/' + bid, { status: 'accepted' });
db.prepare("DELETE FROM pay WHERE client = 'Borra Yo'").run(); await B(); r = await R('GET', 'quotes');
t((await B()).pays.filter((p) => p.client === 'Borra Yo').length === 0 && g(bid).billPaid === null, 'borrado a mano no vuelve');
// 11. un presupuesto aceptado desde el código (Q_SET) entra completo en la siguiente carga
db.prepare("UPDATE docs SET data = json_set(data, '$.status', 'accepted') WHERE id = 'q_carmenvalencia'").run(); b = await B();
t(b.pays.some((p) => p.client === 'Carmen Valencia' && p.kind === 'one') && b.plans.some((p) => p.client === 'Carmen Valencia'), 'aceptado por código: cobro y cuota');
console.log(ok + ' bien, ' + ko + ' mal'); process.exit(ko ? 1 : 0);
