// 18/11 (para el 19/11): SEED4 = 35 tiendas que ya venden a distancia, con interacción real y sin tienda online de verdad.
import { makeD1 } from './d1shim.mjs';
import { readFileSync } from 'node:fs';
import { seedOnce, patchOnce, delOnce, outOnce, DDL, SEED, SEED_KEY, SEED2, SEED2_KEY, SEED3, SEED3_KEY, SEED4, SEED4_KEY, LEAD_PATCH, LEAD_PATCH_KEY, LEAD_OUT_KEY } from './w19mod.mjs';
let ok = 0, ko = 0; const t = (c, m) => { if (c) ok++; else { ko++; console.log('FALLO:', m); } };
const rows = (db, coll) => db.prepare("SELECT id, data FROM docs WHERE coll=?").all(coll).map((r) => [r.id, JSON.parse(r.data)]);

// Producción: SEED, SEED2, SEED3, el parche del 18/11, ldel y lout ya corrieron; el lote 39 está en el CRM.
const env = { DB: makeD1(), SEED_LOCAL: 1 }; for (const s of DDL) env.DB._db.exec(s); const db = env.DB._db;
for (const k of [SEED_KEY, SEED2_KEY, SEED3_KEY, LEAD_PATCH_KEY, 'ldel_20261115b', LEAD_OUT_KEY]) db.prepare("INSERT INTO meta (k, v) VALUES (?, '1')").run(k);
let o = 0;
for (const [id, d] of SEED3) db.prepare("INSERT INTO docs (coll, id, data, updated) VALUES ('leads', ?, ?, 1)").run(id, JSON.stringify(Object.assign({}, d, { order: ++o, stage: 'contacted', contactedAt: 1795000000000 })));
const gone = SEED2[2][0];   // uno del SEED2 que Chris borró a mano no puede volver
db.prepare("INSERT INTO meta (k, v) VALUES ('crm_rev', '9')").run();

await seedOnce(env); await patchOnce(env); await delOnce(env); await outOnce(env);
const L = rows(db, 'leads'), ids = new Set(L.map((x) => x[0])), byId = Object.fromEntries(L);
t(SEED4_KEY === 'seed_20261119' && SEED4.length === 35 && new Set(SEED4.map((x) => x[0])).size === 35, 'SEED4: 35 ids distintos');
t(SEED4.every((x) => ids.has(x[0])), 'entran las 35');
t(!ids.has(gone), 'el SEED2 no se vuelve a ejecutar');
t(L.length === 65, 'solo entran las 35 nuevas (30 del lote 39 + 35)');
t(SEED4.every((x) => ['moda', 'joya', 'sneakers', 'cosmetica', 'suplementos', 'deporte'].includes(x[1].niche)), 'nichos: moda, calzado, joyería…');
t(SEED4.every((x) => !/arab|árab|hiyab|hijab|abaya|caft|halal/i.test(x[1].name + ' ' + x[1].notes)), 'nada árabe');
t(SEED4.every((x) => !/canarias|tenerife|las palmas|lanzarote|fuerteventura/i.test(x[1].region + ' ' + x[1].zone)), 'nada de Canarias');
t(SEED4.every((x) => x[1].stage === 'new' && x[1].igFollowers >= 3500 && /^https:\/\/www\.instagram\.com\/[a-z0-9_.]+\/$/.test(x[1].instagram)), 'por contactar, con su Instagram');
t(SEED4.every((x) => /^\+34[6789]\d{8}$/.test(x[1].phone) && /^\+34[6789]\d{8}$/.test(x[1].whatsapp)), 'todas con un número para WhatsApp');
t(SEED4.filter((x) => x[1].waOk === false).every((x) => /WhatsApp sin comprobar/.test(x[1].notes)), 'waOk false = WhatsApp sin comprobar en las notas');
t(SEED4.filter((x) => x[1].waOk !== false).every((x) => /lo publican como WhatsApp/.test(x[1].notes)), 'las demás lo publican como WhatsApp');
t(SEED4.every((x) => /^Ya vende a distancia: .{15,}/m.test(x[1].notes)), 'todas con su señal de venta a distancia');
t(SEED4.every((x) => /^Tienda online: /m.test(x[1].notes) && /mediana de/.test(x[1].notes)), 'todas con su web y su interacción');
t(SEED4.every((x) => x[1].lotDay === '2026-11-19' && !x[1].pageUrl && !x[1].slug), 'en el lote del 19/11, todavía sin propuesta');
t(SEED4.every((x) => !SEED.some((y) => y[0] === x[0]) && !SEED2.some((y) => y[0] === x[0]) && !SEED3.some((y) => y[0] === x[0])), 'ningún id repetido con lotes anteriores');
const ph = SEED4.map((x) => x[1].whatsapp);
t(new Set(ph).size === 35, 'ningún número repetido entre las 35');
const prevPh = new Set([...SEED, ...SEED2, ...SEED3].flatMap((x) => [x[1].phone, x[1].whatsapp]).filter(Boolean));
t(ph.every((p) => !prevPh.has(p)), 'ningún número que ya estuviera en lotes anteriores');
const prevIg = new Set([...SEED, ...SEED2, ...SEED3].map((x) => x[1].instagram));
t(SEED4.every((x) => !prevIg.has(x[1].instagram)), 'ningún Instagram que ya estuviera en lotes anteriores');
t(SEED3.every((x) => byId[x[0]].stage === 'contacted'), 'el lote 39 no cambia');
t(Number(db.prepare("SELECT v FROM meta WHERE k='crm_rev'").get().v) > 9, 'crm_rev sube');
// una sola vez
const M = await import('./w19mod.mjs?again');
await M.seedOnce(env); await M.patchOnce(env); await M.delOnce(env); await M.outOnce(env);
t(rows(db, 'leads').length === 65, 'una sola vez: nada entra dos veces');
// CRM vacío (instalación nueva): entran las cuatro listas sin chocar
{
  const e2 = { DB: makeD1(), SEED_LOCAL: 1 }; for (const s of DDL) e2.DB._db.exec(s);
  const M2 = await import('./w19mod.mjs?empty');
  await M2.seedOnce(e2);
  const n = rows(e2.DB._db, 'leads').length;
  t(n >= SEED4.length + SEED3.length, 'CRM vacío: entran todas las listas (' + n + ')');
}
// el JSON del lote coincide con el SEED4
const J = JSON.parse(readFileSync('/home/claude/404growth/prospeccion/scrapeo-18nov/leads.json', 'utf8'));
t(J.length === 35 && J.every((x, i) => SEED4[i][1].instagram === `https://www.instagram.com/${x.ig}/`), 'leads.json y SEED4 en el mismo orden');
console.log(ok + ' bien, ' + ko + ' mal'); process.exit(ko ? 1 : 0);
