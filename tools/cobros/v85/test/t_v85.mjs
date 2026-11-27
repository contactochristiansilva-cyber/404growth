// v85: avisos de las mensualidades. node t_v85.mjs (necesita w85mod.mjs = worker v85 + «export { billRemind, brParts, DDL, getMeta, setMeta };»)
import { makeD1 } from './d1shim.mjs';
import { billRemind, brParts, DDL, getMeta } from './w85mod.mjs';
const env = { DB: makeD1() }; for (const s of DDL) env.DB._db.exec(s); const db = env.DB._db;
let ok = 0, bad = 0; const eq = (a, b, m) => { if (JSON.stringify(a) === JSON.stringify(b)) ok++; else { bad++; console.log('FALLA', m, a, b); } };
const RN = Date.now; const T = (s) => { const t = RN.call(Date) && Date.parse(s); Date.now = () => t; return t; };   // instante UTC (y el reloj del worker, para plansRun)
const ins = (id, grp, n, due, paid, kind = 'rec', client = 'Kiss of Life') => db.prepare("INSERT INTO pay (id, client_id, client, concept, amount, cur, kind, grp, n, due, paid, note, created) VALUES (?, 'c_k', ?, 'Cuota', 49000, 'EUR', ?, ?, ?, ?, ?, '', 1)").run(id, client, kind, grp, n, due, paid);
const plan = (id, client, start, upto, active = 1) => db.prepare("INSERT INTO plans (id, client_id, client, concept, amount, cur, start, upto, active, created) VALUES (?, 'c_k', ?, 'Cuota', 49000, 'EUR', ?, ?, ?, 1)").run(id, client, start, upto, active);
// estado real del 27/11: el cobro de hoy quedó en la cuota de diciembre
plan('pl_fjP5H1zNFLdt', 'Kiss of Life', '2026-11-27', 1);
ins('p_fjP5H1zNFLdt_1', 'pl_fjP5H1zNFLdt', 2, '2026-12-27', '2026-11-27');
// otro plan sin ninguna cuota cobrada: no avisa
plan('pl_otro', 'La Casa de Inés', '2026-11-27', 1);
ins('p_otro_0', 'pl_otro', 1, '2026-11-27', ''); ins('p_otro_1', 'pl_otro', 2, '2026-12-27', '');
const pay = (id) => db.prepare('SELECT due, paid FROM pay WHERE id = ?').get(id);
const meta = async (k) => !!(await getMeta(env, k));
eq(brParts(T('2026-12-26T07:30:00Z')), { day: '2026-12-26', h: 8 }, 'hora de Madrid en invierno');
// 27/11 a las 10:20 de Turquía (8:20 en Madrid): arregla Kiss of Life y manda la prueba, pero todavía no hay avisos
let r = await billRemind(env, T('2026-11-27T07:20:00Z'));
eq(r, { skip: 'hour' }, 'antes de las 9 no avisa');
eq(pay('p_fjP5H1zNFLdt_0'), { due: '2026-11-27', paid: '2026-11-27' }, 'noviembre cobrado');
eq(pay('p_fjP5H1zNFLdt_1'), { due: '2026-12-27', paid: '' }, 'diciembre pendiente');
eq(await meta('brtest_20261127'), true, 'prueba enviada una vez');
r = await billRemind(env, T('2026-11-27T10:00:00Z'));
eq(r.sent, 0, 'el 27/11 no hay nada que avisar (noviembre ya cobrado; La Casa de Inés sin primera cuota)');
eq(db.prepare("SELECT count(*) c FROM pay WHERE id LIKE 'p_fjP5H1zNFLdt_%'").get().c, 2, 'el arreglo no duplica');
// 25/12: nada
r = await billRemind(env, T('2026-12-25T10:00:00Z')); eq(r.sent, 0, '25/12 sin aviso');
// 26/12 a las 9:30 de Madrid: el del día antes
r = await billRemind(env, T('2026-12-26T08:30:00Z')); eq(r.sent, 1, '26/12 aviso del día antes');
eq(await meta('brem:p_fjP5H1zNFLdt_1:p'), true, 'marca del día antes');
r = await billRemind(env, T('2026-12-26T15:00:00Z')); eq(r.sent, 0, 'no repite el del día antes');
// 27/12: el del mismo día
r = await billRemind(env, T('2026-12-27T08:01:00Z')); eq(r.sent, 1, '27/12 aviso del día');
r = await billRemind(env, T('2026-12-27T20:00:00Z')); eq(r.sent, 0, 'no repite el del día');
// ya cobrado el 27/12: el 26/1 avisa de enero (plansRun ha creado la cuota)
db.prepare("UPDATE pay SET paid = '2026-12-27' WHERE id = 'p_fjP5H1zNFLdt_1'").run();
r = await billRemind(env, T('2027-01-26T09:00:00Z')); eq(r.sent, 1, '26/1 aviso de enero');
eq(pay('p_fjP5H1zNFLdt_2'), { due: '2027-01-27', paid: '' }, 'cuota de enero creada');
// cliente nuevo: cobra la primera y se activa sola
db.prepare("UPDATE pay SET paid = '2026-11-27' WHERE id = 'p_otro_0'").run();
r = await billRemind(env, T('2027-01-27T09:00:00Z')); eq(r.sent >= 2, true, '27/1 avisos del día de los dos clientes');
// plan parado: no avisa
db.prepare("UPDATE plans SET active = 0 WHERE id = 'pl_otro'").run(); ins('p_otro_9', 'pl_otro', 9, '2027-02-27', '');
r = await billRemind(env, T('2027-02-26T09:00:00Z')); eq(await meta('brem:p_otro_9:p'), false, 'plan parado sin aviso');
console.log(ok, 'bien', bad, 'mal'); process.exit(bad ? 1 : 0);
