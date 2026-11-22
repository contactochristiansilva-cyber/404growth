// 22/11 (lote 42): SEED6 con propuesta (33) y LEAD_PATCH lpatch_20261123 (33 con propuesta + 3 que salen del lote).
// uso: node t_l42.mjs A && node t_l42.mjs B (cada caso en su proceso: patchOnce y seedOnce recuerdan que ya corrieron) (desde la carpeta con d1shim.mjs y w42mod.mjs = copia del worker con export {…})
import { makeD1 } from './d1shim.mjs';
import { seedOnce, patchOnce, delOnce, outOnce, DDL, SEED, SEED_KEY, SEED2, SEED2_KEY, SEED3, SEED3_KEY, SEED4, SEED4_KEY, SEED5, SEED5_KEY, SEED6, SEED6_KEY, LEAD_PATCH, LEAD_PATCH_KEY, LEAD_OUT_KEY } from './w42mod.mjs';
let ok = 0, ko = 0; const t = (c, m) => { if (c) ok++; else { ko++; console.log('FALLO:', m); } };
const rows = (db) => Object.fromEntries(db.prepare("SELECT id, data FROM docs WHERE coll='leads'").all().map((r) => [r.id, JSON.parse(r.data)]));
const N = 33, OUT = ['mod-mas-que-divas-algeciras', 'mod-modas-carisma-por-confirmar', 'mod-tj-moda-y-calzado-solares'];
const mk = () => { const env = { DB: makeD1(), SEED_LOCAL: 1 }; for (const s of DDL) env.DB._db.exec(s); const db = env.DB._db;
  for (const k of [SEED_KEY, SEED2_KEY, SEED3_KEY, SEED4_KEY, SEED5_KEY, 'lpatch_20261119', 'ldel_20261115b', LEAD_OUT_KEY]) db.prepare("INSERT INTO meta (k, v) VALUES (?, '1')").run(k);
  db.prepare("INSERT INTO meta (k, v) VALUES ('crm_rev', '9')").run(); return env; };
const run = async (env) => { await seedOnce(env); await patchOnce(env); await delOnce(env); await outOnce(env); };

t(SEED6_KEY === 'seed_20261123b' && LEAD_PATCH_KEY === 'lpatch_20261123', 'claves');
t(SEED6.length === N && new Set(SEED6.map((x) => x[0])).size === N, '33 en el SEED6');
t(SEED6.every((x) => /^https:\/\/404growth\.com\/p\/[a-z0-9-]+\/$/.test(x[1].pageUrl) && x[1].pageUrl.includes('/p/' + x[1].slug + '/')), 'todas con slug y pageUrl');
t(SEED6.every((x) => !OUT.includes(x[0])), 'sin las 3 que salen');
t(SEED6.every((x) => !/por confirmar/.test(x[1].zone)), 'todas con ciudad');
t(SEED6.every((x) => !/Falta su propuesta|Falta la ciudad/.test(x[1].notes) && x[1].notes.includes('404growth.com/p/' + x[1].slug + '/')), 'notas con la propuesta');
{ const p = SEED6.find((x) => x[0] === 'joy-la-plateria-del-sur-por-confirmar')[1]; t(p.lotDay === '2026-11-26' && p.zone === 'Jerez de la Frontera' && p.address === 'C. Fresa, 2', 'Platería: Jerez, jueves 26'); }
{ const z = {}; for (const [, d] of SEED6) { const k = d.lotDay + '|' + d.zone.split(' ')[0]; z[k] = (z[k] || 0) + 1; } t(Object.values(z).every((v) => v === 1), 'nunca dos del mismo pueblo el mismo día: ' + JSON.stringify(Object.entries(z).filter(([, v]) => v > 1))); }
t(SEED6.filter((x) => x[1].lotDay === '2026-11-23').length === 27, '27 el lunes 23');

// A: el SEED6 aún no había entrado
if (process.argv[2] !== 'B') { const env = mk(); await run(env); const L = rows(env.DB._db);
  t(SEED6.every((x) => L[x[0]] && L[x[0]].pageUrl === x[1].pageUrl), 'A: entran las 33 con su propuesta');
  t(OUT.every((id) => !L[id]), 'A: las 3 no entran');
  t(Object.keys(L).length === N, 'A: nada más'); }

// B: el SEED6 del 22/11 (36, sin propuesta) ya había entrado
if (process.argv[2] === 'B') { const env = mk(); const db = env.DB._db; let o = 0;
  const old = SEED6.map(([id, d]) => [id, Object.assign({}, d, { slug: undefined, pageUrl: undefined, lotDay: '2026-11-23', notes: 'vieja' })]);
  for (const id of OUT) old.push([id, { niche: 'moda', name: id, lotDay: '2026-11-23', notes: 'vieja', stage: 'new', priority: 85 }]);
  for (const [id, d] of old) db.prepare("INSERT INTO docs (coll, id, data, updated) VALUES ('leads', ?, ?, 1)").run(id, JSON.stringify(Object.assign({ order: ++o }, d)));
  db.prepare("INSERT INTO meta (k, v) VALUES (?, '36')").run(SEED6_KEY);
  await run(env); const L = rows(db);
  t(Object.keys(L).length === 36, 'B: no se duplica nada');
  t(SEED6.every((x) => L[x[0]].pageUrl === x[1].pageUrl && L[x[0]].slug === x[1].slug && L[x[0]].lotDay === x[1].lotDay && L[x[0]].notes === x[1].notes), 'B: el parche pone propuesta, día y notas');
  t(L['joy-la-plateria-del-sur-por-confirmar'].zone === 'Jerez de la Frontera' && L['mod-crisly-coquette-por-confirmar'].zone === 'Motril', 'B: ciudades de Platería y Crisly');
  t(OUT.every((id) => !('lotDay' in L[id]) && L[id].priority === 20 && /AVISO \(22\/11\): fuera del lote 42/.test(L[id].notes)), 'B: las 3 salen del lote con aviso');
  t(Object.values(L).every((d) => d.order), 'B: el orden se conserva');
  const rev = db.prepare("SELECT v FROM meta WHERE k='crm_rev'").get().v; t(rev === '10', 'B: sube crm_rev');
  await run(env); t(db.prepare("SELECT v FROM meta WHERE k='crm_rev'").get().v === '10', 'B: el parche solo corre una vez'); }

t(LEAD_PATCH.length === 36, 'parche con 36 entradas');
console.log(`${ok} bien, ${ko} mal`); process.exit(ko ? 1 : 0);
