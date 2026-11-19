// 19/11 (para el 20 y el 21/11): SEED5 = 29 tiendas que ya venden a distancia, con interacción real y sin tienda online de verdad.
// uso: node t_s20.mjs (desde la carpeta que tiene d1shim.mjs y w20mod.mjs = copia del worker + export {…})
import { makeD1 } from './d1shim.mjs';
import { readFileSync } from 'node:fs';
import { seedOnce, patchOnce, delOnce, outOnce, DDL, SEED, SEED_KEY, SEED2, SEED2_KEY, SEED3, SEED3_KEY, SEED4, SEED4_KEY, SEED5, SEED5_KEY, LEAD_PATCH_KEY, LEAD_OUT_KEY } from './w20mod.mjs';
let ok = 0, ko = 0; const t = (c, m) => { if (c) ok++; else { ko++; console.log('FALLO:', m); } };
const rows = (db, coll) => db.prepare("SELECT id, data FROM docs WHERE coll=?").all(coll).map((r) => [r.id, JSON.parse(r.data)]);
const N = 29;

// Producción: SEED…SEED4, el parche del 19/11, ldel y lout ya corrieron; el lote del 19/11 está en el CRM y enviado.
const env = { DB: makeD1(), SEED_LOCAL: 1 }; for (const s of DDL) env.DB._db.exec(s); const db = env.DB._db;
for (const k of [SEED_KEY, SEED2_KEY, SEED3_KEY, SEED4_KEY, LEAD_PATCH_KEY, 'ldel_20261115b', LEAD_OUT_KEY]) db.prepare("INSERT INTO meta (k, v) VALUES (?, '1')").run(k);
let o = 0;
for (const [id, d] of SEED4) db.prepare("INSERT INTO docs (coll, id, data, updated) VALUES ('leads', ?, ?, 1)").run(id, JSON.stringify(Object.assign({}, d, { order: ++o, stage: 'contacted', contactedAt: 1795000000000 })));
const gone = SEED3[2][0];   // uno del SEED3 que no está (borrado o enviado y sacado) no puede volver
db.prepare("INSERT INTO meta (k, v) VALUES ('crm_rev', '9')").run();

await seedOnce(env); await patchOnce(env); await delOnce(env); await outOnce(env);
const L = rows(db, 'leads'), ids = new Set(L.map((x) => x[0])), byId = Object.fromEntries(L);
t(SEED5_KEY === 'seed_20261120' && SEED5.length === N && new Set(SEED5.map((x) => x[0])).size === N, 'SEED5: 29 ids distintos');
t(SEED5.every((x) => ids.has(x[0])), 'entran las 29');
t(!ids.has(gone), 'el SEED3 no se vuelve a ejecutar');
t(L.length === SEED4.length + N, 'solo entran las 29 nuevas');
t(SEED5.every((x) => ['moda', 'sneakers'].includes(x[1].niche)), 'nichos: moda y zapatería');
t(SEED5.every((x) => !/arab|árab|hiyab|hijab|abaya|caft|halal/i.test(x[1].name + ' ' + x[1].notes)), 'nada árabe');
t(SEED5.every((x) => !/canarias|tenerife|las palmas|lanzarote|fuerteventura/i.test(x[1].region + ' ' + x[1].zone)), 'nada de Canarias');
t(SEED5.every((x) => x[1].stage === 'new' && x[1].igFollowers >= 3500 && /^https:\/\/www\.instagram\.com\/[a-z0-9_.]+\/$/.test(x[1].instagram)), 'por contactar, con su Instagram');
t(SEED5.every((x) => /^\+34[67]\d{8}$/.test(x[1].phone) && /^\+34[67]\d{8}$/.test(x[1].whatsapp)), 'todas con un móvil para WhatsApp');
t(SEED5.filter((x) => x[1].waOk === false).every((x) => /WhatsApp sin comprobar/.test(x[1].notes)), 'waOk false = WhatsApp sin comprobar en las notas');
t(SEED5.filter((x) => x[1].waOk !== false).every((x) => /lo publican como WhatsApp/.test(x[1].notes)), 'las demás lo publican como WhatsApp');
t(SEED5.every((x) => /^Ya vende a distancia: .{15,}/m.test(x[1].notes)), 'todas con su señal de venta a distancia');
t(SEED5.every((x) => /^Tienda online: /m.test(x[1].notes) && /mediana de/.test(x[1].notes)), 'todas con su web y su interacción');
t(SEED5.every((x) => ['2026-11-20', '2026-11-21'].includes(x[1].lotDay) && !x[1].pageUrl && !x[1].slug), 'en el lote del 20 o del 21/11, todavía sin propuesta');
t(SEED5.filter((x) => x[1].lotDay === '2026-11-20').length === 15 && SEED5.filter((x) => x[1].lotDay === '2026-11-21').length === 14, '15 el 20/11 y 14 el 21/11');
const same = {}; for (const [, d] of SEED5) { const k = d.zone + '|' + d.lotDay; same[k] = (same[k] || 0) + 1; }
t(Object.values(same).every((n) => n === 1), 'nunca dos del mismo pueblo el mismo día');
t(SEED5.every((x) => ![SEED, SEED2, SEED3, SEED4].some((S) => S.some((y) => y[0] === x[0]))), 'ningún id repetido con lotes anteriores');
const ph = SEED5.map((x) => x[1].whatsapp);
t(new Set(ph).size === N, 'ningún número repetido entre las 29');
const prevPh = new Set([...SEED, ...SEED2, ...SEED3, ...SEED4].flatMap((x) => [x[1].phone, x[1].whatsapp]).filter(Boolean));
t(ph.every((p) => !prevPh.has(p)), 'ningún número que ya estuviera en lotes anteriores');
const prevIg = new Set([...SEED, ...SEED2, ...SEED3, ...SEED4].map((x) => x[1].instagram));
t(SEED5.every((x) => !prevIg.has(x[1].instagram)), 'ningún Instagram que ya estuviera en lotes anteriores');
t(SEED4.every((x) => byId[x[0]].stage === 'contacted'), 'el lote del 19/11 no cambia');
t(Number(db.prepare("SELECT v FROM meta WHERE k='crm_rev'").get().v) > 9, 'crm_rev sube');
const M = await import('./w20mod.mjs?again');
await M.seedOnce(env); await M.patchOnce(env); await M.delOnce(env); await M.outOnce(env);
t(rows(db, 'leads').length === SEED4.length + N, 'una sola vez: nada entra dos veces');
{
  const e2 = { DB: makeD1(), SEED_LOCAL: 1 }; for (const s of DDL) e2.DB._db.exec(s);
  const M2 = await import('./w20mod.mjs?empty');
  await M2.seedOnce(e2);
  const n = rows(e2.DB._db, 'leads').length;
  t(n >= SEED5.length + SEED4.length, 'CRM vacío: entran todas las listas (' + n + ')');
}
const J = JSON.parse(readFileSync(process.env.LEADS || '/home/claude/404growth/prospeccion/scrapeo-19nov/leads.json', 'utf8'));
t(J.length === N && J.every((x, i) => SEED5[i][1].instagram === `https://www.instagram.com/${x.ig}/`), 'leads.json y SEED5 en el mismo orden');
console.log(ok + ' bien, ' + ko + ' mal'); process.exit(ko ? 1 : 0);
