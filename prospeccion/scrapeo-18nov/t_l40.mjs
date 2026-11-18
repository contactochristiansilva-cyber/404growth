// 18–19/11/2026, lote 40: el SEED4 y el LEAD_PATCH nuevo llevan la propuesta de 29 tiendas; 5 pasan al 20/11 sin propuesta
// (fotos pendientes por el cupo de Flow) y Vichy Motril sale del lote.
// Se ejecuta junto a d1shim.mjs y w40mod.mjs (copia del worker con «export {…}» al final).
import { makeD1 } from './d1shim.mjs';
import { seedOnce, patchOnce, DDL, SEED_KEY, SEED2_KEY, SEED3_KEY, SEED4, SEED4_KEY, LEAD_PATCH, LEAD_PATCH_KEY } from './w40mod.mjs';
let ok = 0, ko = 0; const t = (c, m) => { if (c) ok++; else { ko++; console.log('FALLO:', m); } };
const rows = (db) => Object.fromEntries(db.prepare("SELECT id, data FROM docs WHERE coll='leads'").all().map((r) => [r.id, JSON.parse(r.data)]));
const V = 'mod-vichy-motril-motril';
const DAY = { 'casual-coria': '2026-11-20', 'mercedes-beltran': '2026-11-20', 'modas-rocio': '2026-11-21' };
const PEND = ['mod-cent-vuit-barcelona', 'mod-casual-coria-coria-del-rio', 'mod-doble-ele-sevilla', 'mod-marga-pineiro-massanassa', 'joy-novojoya-chiclana-de-la-frontera'];

t(LEAD_PATCH_KEY === 'lpatch_20261119' && LEAD_PATCH.length === 35, 'LEAD_PATCH nuevo con 35 entradas');
t(SEED4_KEY === 'seed_20261119' && SEED4.length === 35, 'SEED4 sigue con 35');
const S4 = Object.fromEntries(SEED4);
const withP = SEED4.filter(([id]) => id !== V && !PEND.includes(id));
const pend = SEED4.filter(([id]) => PEND.includes(id));
t(withP.every(([, d]) => d.slug && d.pageUrl === `https://404growth.com/p/${d.slug}/` && d.lotDay === (DAY[d.slug] || '2026-11-19')), 'las 34 con slug, pageUrl y su día');
t(withP.length === 29 && new Set(withP.map(([, d]) => d.slug)).size === 29, '29 slugs distintos');
t(pend.length === 5 && pend.every(([, d]) => !d.slug && !d.pageUrl && d.lotDay === '2026-11-20' && /a medias/.test(d.notes)), 'las 5 pendientes: al 20/11 sin propuesta');
t(!S4[V].lotDay && !S4[V].slug && S4[V].priority === 30 && /ya vende online en vichymotril\.com/.test(S4[V].notes), 'Vichy: fuera del lote, con AVISO');
t(withP.every(([, d]) => d.notes.includes('Propuesta (lote 40): ' + d.pageUrl) && !d.notes.includes('Falta su propuesta')), 'notas con el enlace de su propuesta');
const coriaAll = SEED4.filter(([, d]) => d.zone === 'Coria del Río').map(([, d]) => d.lotDay);
t(coriaAll.length === 3 && new Set(coriaAll).size === 3, 'Coria del Río: tres días distintos');
const ant = withP.filter(([, d]) => d.zone === 'Antequera').map(([, d]) => d.lotDay);
t(ant.length === 2 && new Set(ant).size === 2, 'Antequera: dos días distintos');

// Caso 1: el SEED4 todavía no ha entrado (lo normal): entra ya con todo y el parche no cambia nada malo.
{
  const env = { DB: makeD1(), SEED_LOCAL: 1 }; for (const s of DDL) env.DB._db.exec(s); const db = env.DB._db;
  for (const k of [SEED_KEY, SEED2_KEY, SEED3_KEY]) db.prepare("INSERT INTO meta (k, v) VALUES (?, '1')").run(k);
  await seedOnce(env); await patchOnce(env);
  const L = rows(db);
  t(Object.keys(L).length === 35, 'caso 1: entran las 35');
  t(withP.every(([id, d]) => L[id].pageUrl === d.pageUrl && L[id].lotDay === d.lotDay), 'caso 1: cada una con su propuesta y su día');
  t(!L[V].lotDay && L[V].priority === 30, 'caso 1: Vichy sin lote');
  t(pend.every(([id]) => !L[id].pageUrl && L[id].lotDay === '2026-11-20'), 'caso 1: las 5 pendientes sin propuesta, el 20/11');
  t(db.prepare("SELECT v FROM meta WHERE k=?").get(LEAD_PATCH_KEY)?.v === '35', 'caso 1: el parche queda apuntado');
}
// Caso 2: el SEED4 ya entró sin propuesta (versión anterior): el parche las pone.
{
  const env = { DB: makeD1(), SEED_LOCAL: 1 }; for (const s of DDL) env.DB._db.exec(s); const db = env.DB._db;
  for (const k of [SEED_KEY, SEED2_KEY, SEED3_KEY, SEED4_KEY]) db.prepare("INSERT INTO meta (k, v) VALUES (?, '1')").run(k);
  for (const [id, d] of SEED4) { const o = Object.assign({}, d, { lotDay: '2026-11-19', priority: 85 }); delete o.slug; delete o.pageUrl; db.prepare("INSERT INTO docs (coll, id, data, updated) VALUES ('leads', ?, ?, 1)").run(id, JSON.stringify(o)); }
  db.prepare("INSERT INTO meta (k, v) VALUES ('crm_rev', '3')").run();
  const M = await import('./w40mod.mjs?c2');
  await M.seedOnce(env); await M.patchOnce(env);
  const L = rows(db);
  t(withP.every(([id, d]) => L[id].slug === d.slug && L[id].pageUrl === d.pageUrl && L[id].lotDay === d.lotDay), 'caso 2: el parche pone slug, pageUrl y día');
  t(!('lotDay' in L[V]) && L[V].priority === 30, 'caso 2: a Vichy se le quita el lote');
  t(pend.every(([id]) => !L[id].pageUrl && L[id].lotDay === '2026-11-20'), 'caso 2: las 5 pendientes pasan al 20/11');
  t(Number(db.prepare("SELECT v FROM meta WHERE k='crm_rev'").get().v) > 3, 'caso 2: crm_rev sube');
  // una sola vez: si Chris cambia algo a mano, no se pisa
  db.prepare("UPDATE docs SET data = json_set(data, '$.lotDay', '2026-11-25') WHERE id = ?").run(withP[0][0]);
  const M2 = await import('./w40mod.mjs?c3');
  await M2.patchOnce(env);
  t(rows(db)[withP[0][0]].lotDay === '2026-11-25', 'el parche corre una sola vez');
}
console.log(ok + ' bien, ' + ko + ' mal'); process.exit(ko ? 1 : 0);
