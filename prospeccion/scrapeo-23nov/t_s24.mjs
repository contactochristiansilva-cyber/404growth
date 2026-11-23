// 23/11: SEED7 (seed_20261124), 50 tiendas sin propuesta para los lotes del 24 al 30/11.
// uso: node t_s24.mjs (desde la carpeta con d1shim.mjs y w24mod.mjs = copia del worker con export {…})
import { makeD1 } from './d1shim.mjs';
import { seedOnce, DDL, SEED_KEY, SEED2_KEY, SEED3_KEY, SEED4_KEY, SEED5_KEY, SEED6, SEED6_KEY, SEED7, SEED7_KEY, LEAD_DEL } from './w24mod.mjs';
let ok = 0, ko = 0; const t = (c, m) => { if (c) ok++; else { ko++; console.log('FALLO:', m); } };
const rows = (db) => Object.fromEntries(db.prepare("SELECT id, data FROM docs WHERE coll='leads'").all().map((r) => [r.id, JSON.parse(r.data)]));

t(SEED7_KEY === 'seed_20261124', 'clave');
t(SEED7.length === 50 && new Set(SEED7.map((x) => x[0])).size === 50, '50 sin repetir');
const s6 = new Set(SEED6.map((x) => x[0])); t(SEED7.every((x) => !s6.has(x[0]) && !LEAD_DEL.includes(x[0])), 'ninguna del SEED6 ni de LEAD_DEL');
const ig6 = new Set(SEED6.map((x) => x[1].instagram)); t(SEED7.every((x) => !ig6.has(x[1].instagram)), 'ningún Instagram del SEED6');
t(SEED7.every((x) => x[1].stage === 'new' && !x[1].pageUrl && /Falta su propuesta/.test(x[1].notes)), 'sin propuesta');
t(SEED7.every((x) => ['moda', 'joya', 'sneakers', 'cosmetica'].includes(x[1].niche)), 'nichos de siempre (sin mercerías, artesanía ni muebles)');
t(SEED7.every((x) => /^2026-11-(24|25|26|27|30)$/.test(x[1].lotDay)), 'días del 24 al 30');
{ const z = {}; for (const [, d] of [...SEED6, ...SEED7]) { if (/por confirmar/.test(d.zone)) continue; const k = d.lotDay + '|' + d.zone; z[k] = (z[k] || 0) + 1; }
  t(Object.values(z).every((v) => v === 1), 'nunca dos del mismo pueblo el mismo día: ' + JSON.stringify(Object.entries(z).filter(([, v]) => v > 1))); }
t(SEED7.every((x) => x[1].phone && /^\+34[6789]\d{8}$/.test(x[1].phone)), 'todas con teléfono');
t(SEED7.filter((x) => x[1].priority === 50).every((x) => x[1].phoneType === 'fijo' && /AVISO: Solo/.test(x[1].notes)), 'las de solo fijo, prioridad 50 y aviso');
t(SEED7.every((x) => !/árabe|arabe|caft|abaya/i.test(x[1].notes + x[1].name)), 'nada árabe');

const env = { DB: makeD1(), SEED_LOCAL: 1 }; for (const s of DDL) env.DB._db.exec(s); const db = env.DB._db;
for (const k of [SEED_KEY, SEED2_KEY, SEED3_KEY, SEED4_KEY, SEED5_KEY, SEED6_KEY]) db.prepare("INSERT INTO meta (k, v) VALUES (?, '1')").run(k);
db.prepare("INSERT INTO meta (k, v) VALUES ('crm_rev', '9')").run();
db.prepare("INSERT INTO docs (coll, id, data, updated) VALUES ('leads', 'mod-vieja', ?, 1)").run(JSON.stringify({ name: 'vieja', order: 1040, stage: 'new' }));
await seedOnce(env); let L = rows(db);
t(Object.keys(L).length === 51, 'entran las 50 (y la vieja sigue)');
t(SEED7.every((x) => L[x[0]] && L[x[0]].order > 1040), 'van detrás de las que ya había');
t(db.prepare("SELECT v FROM meta WHERE k='crm_rev'").get().v === '10', 'sube crm_rev');
t(db.prepare("SELECT v FROM meta WHERE k=?").get(SEED7_KEY), 'apunta la clave');
await seedOnce(env); t(Object.keys(rows(db)).length === 51, 'no duplica');
console.log(`${ok} bien, ${ko} mal`); process.exit(ko ? 1 : 0);
