// 26/11: SEED10 (seed_20261126), las 70 tiendas del scrapeo nocturno del 25-26/11 (lote 48).
// uso: node t_s48.mjs (desde una carpeta con d1shim.mjs y w48mod.mjs = copia del worker con export {…})
import { makeD1 } from './d1shim.mjs';
import { seedOnce, DDL, SEED_KEY, SEED2_KEY, SEED3_KEY, SEED4_KEY, SEED5_KEY, SEED6_KEY, SEED7_KEY, SEED8_KEY, SEED9_KEY,
  SEED, SEED2, SEED3, SEED4, SEED5, SEED6, SEED7, SEED8, SEED9, SEED10, SEED10_KEY, LEAD_DEL } from './w48mod.mjs';
let ok = 0, ko = 0; const t = (c, m) => { if (c) ok++; else { ko++; console.log('FALLO:', m); } };
const rows = (db) => Object.fromEntries(db.prepare("SELECT id, data FROM docs WHERE coll='leads'").all().map((r) => [r.id, JSON.parse(r.data)]));
const norm = (u) => (u || '').toLowerCase().replace(/\/+$/, '');
const old = [...SEED, ...SEED2, ...SEED3, ...SEED4, ...SEED5, ...SEED6, ...SEED7, ...SEED8, ...SEED9];

t(SEED10_KEY === 'seed_20261126', 'clave');
t(SEED10.length === 70 && new Set(SEED10.map((x) => x[0])).size === 70, '70 sin repetir');
const ids = new Set(old.map((x) => x[0])); t(SEED10.every((x) => !ids.has(x[0]) && !LEAD_DEL.includes(x[0])), 'ningún id de los SEED anteriores ni de LEAD_DEL');
const igs = new Set(old.map((x) => norm(x[1].instagram)));
const dupIg = SEED10.filter((x) => igs.has(norm(x[1].instagram))).map((x) => x[0]); t(!dupIg.length, 'ningún Instagram repetido: ' + dupIg);
const phs = new Set(old.map((x) => x[1].phone).filter(Boolean));
const dupPh = SEED10.filter((x) => x[1].phone && phs.has(x[1].phone)).map((x) => x[0]); t(!dupPh.length, 'ningún teléfono repetido: ' + dupPh);
t(SEED10.every((x) => x[1].stage === 'new' && x[1].lotDay === '2026-11-26'), 'nuevas, en el lote del 26/11');
t(SEED10.every((x) => !x[1].pageUrl || x[1].pageUrl === `https://404growth.com/p/${x[1].slug}/`), 'pageUrl coherente con slug');
t(SEED10.every((x) => ['moda', 'joya', 'sneakers'].includes(x[1].niche)), 'nichos de siempre');
t(SEED10.filter((x) => x[1].priority === 50).every((x) => x[1].phoneType === 'fijo' && /AVISO: solo publican fijo/.test(x[1].notes)), 'solo fijo: prioridad 50 y aviso');
t(SEED10.every((x) => !/árabe|arabe|caft|abaya/i.test(x[1].notes + x[1].name)), 'nada árabe');

const env = { DB: makeD1(), SEED_LOCAL: 1 }; for (const s of DDL) env.DB._db.exec(s); const db = env.DB._db;
for (const k of [SEED_KEY, SEED2_KEY, SEED3_KEY, SEED4_KEY, SEED5_KEY, SEED6_KEY, SEED7_KEY, SEED8_KEY, SEED9_KEY]) db.prepare("INSERT INTO meta (k, v) VALUES (?, '1')").run(k);
db.prepare("INSERT INTO meta (k, v) VALUES ('crm_rev', '9')").run();
db.prepare("INSERT INTO docs (coll, id, data, updated) VALUES ('leads', 'mod-vieja', ?, 1)").run(JSON.stringify({ name: 'vieja', order: 2035, stage: 'new' }));
await seedOnce(env); let L = rows(db);
t(Object.keys(L).length === 71, 'entran las 70 (y la vieja sigue): ' + Object.keys(L).length);
t(db.prepare("SELECT v FROM meta WHERE k='crm_rev'").get().v === '10', 'sube crm_rev');
t(db.prepare("SELECT v FROM meta WHERE k=?").get(SEED10_KEY), 'apunta la clave');
await seedOnce(env); t(Object.keys(rows(db)).length === 71, 'no duplica');
console.log(`${ok} bien, ${ko} mal`); process.exit(ko ? 1 : 0);
