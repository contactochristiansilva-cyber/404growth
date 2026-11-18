// Prueba de la v76: reservar desde la agenda de una propuesta pasa su contacto del CRM a «Pendiente de reunión».
// uso: en una carpeta con w76.mjs (copia del worker del admin + "export { crmFromProposal, DDL };") y d1shim.mjs → node t_v76.mjs
import { makeD1 } from './d1shim.mjs';
const M = await import('./w76.mjs');
let ok = 0, bad = 0; const t = (c, m) => { if (c) ok++; else { bad++; console.log('FALLO: ' + m); } };
const env = { DB: makeD1() }; for (const s of M.DDL) env.DB._db.exec(s); const db = env.DB._db;
const put = (id, d) => db.prepare("INSERT INTO docs (coll, id, data, updated) VALUES ('leads', ?, ?, 1)").run(id, JSON.stringify(d));
const get = (id) => JSON.parse(db.prepare("SELECT data FROM docs WHERE coll = 'leads' AND id = ?").get(id).data);
const rev = () => +((db.prepare("SELECT v FROM meta WHERE k = 'crm_rev'").get() || {}).v || 0);
put('mer-lanas-paloma', { name: 'Lanas Paloma', slug: 'lanas-paloma', stage: 'new', notes: 'Contacto: bio de Instagram' });
put('mod-ganado', { name: 'Ganado', slug: 'ganado', stage: 'won', contactedAt: 5, closedAt: 9 });
put('mod-tocada', { name: 'Tocada', slug: 'tocada', stage: 'contacted', contactedAt: 7 });
const start = Date.parse('2026-11-20T15:00:00Z'), now = Date.parse('2026-11-18T09:00:00Z'), r0 = rev();

t(await M.crmFromProposal(env, 'lanas-paloma', 'Labc123', start, now) === 'Lanas Paloma', 'devuelve el nombre del contacto');
let l = get('mer-lanas-paloma');
t(l.stage === 'meet', 'pasa a «Pendiente de reunión»');
t(l.contactedAt === now && l.repliedAt === now && l.hotAt === now && l.meetAt === now, 'con las fechas de las etapas anteriores, como al moverlo a mano');
t(l.notes.startsWith('Contacto: bio de Instagram\n') && /Reservó la llamada desde su propuesta para el .*20.*noviembre.*16:00.*Labc123/.test(l.notes), 'nota con el día y la hora de España: ' + l.notes);
t(rev() === r0 + 1, 'sube crm_rev para que el CRM abierto se actualice');

t(await M.crmFromProposal(env, 'tocada', 'Lx', start, now) === 'Tocada', 'otro contacto');
l = get('mod-tocada');
t(l.stage === 'meet' && l.contactedAt === 7 && l.meetAt === now, 'no cambia la fecha del primer mensaje que ya tenía');

await M.crmFromProposal(env, 'ganado', 'Ly', start, now); l = get('mod-ganado');
t(l.stage === 'won' && l.closedAt === 9 && !l.meetAt && /Reservó la llamada/.test(l.notes), 'un cliente cerrado sigue cerrado, solo con la nota');

t(await M.crmFromProposal(env, 'no-existe', 'Lz', start, now) === null, 'sin contacto con ese slug no hace nada');
console.log(ok + ' bien, ' + bad + ' mal'); process.exit(bad ? 1 : 0);
