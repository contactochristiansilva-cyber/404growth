// 21/11 (para el 23/11): SEED6 = 40 tiendas con nivel de conciencia alto (anuncios en Meta o web rota o sin tienda).
// uso: node t_s23.mjs (desde la carpeta que tiene d1shim.mjs y w23mod.mjs = copia del worker + export {…})
import { makeD1 } from './d1shim.mjs';
import { readFileSync } from 'node:fs';
import { seedOnce, patchOnce, delOnce, outOnce, DDL, SEED, SEED_KEY, SEED2, SEED2_KEY, SEED3, SEED3_KEY, SEED4, SEED4_KEY, SEED5, SEED5_KEY, SEED6, SEED6_KEY, LEAD_PATCH_KEY, LEAD_OUT_KEY } from './w23mod.mjs';
let ok = 0, ko = 0; const t = (c, m) => { if (c) ok++; else { ko++; console.log('FALLO:', m); } };
const rows = (db, coll) => db.prepare("SELECT id, data FROM docs WHERE coll=?").all(coll).map((r) => [r.id, JSON.parse(r.data)]);
const N = 40, PREV = [SEED, SEED2, SEED3, SEED4, SEED5];

// Producción: todas las listas anteriores ya corrieron y el lote del 20/11 está en el CRM y enviado.
const env = { DB: makeD1(), SEED_LOCAL: 1 }; for (const s of DDL) env.DB._db.exec(s); const db = env.DB._db;
for (const k of [SEED_KEY, SEED2_KEY, SEED3_KEY, SEED4_KEY, SEED5_KEY, LEAD_PATCH_KEY, 'ldel_20261115b', LEAD_OUT_KEY]) db.prepare("INSERT INTO meta (k, v) VALUES (?, '1')").run(k);
let o = 0;
for (const [id, d] of SEED5) db.prepare("INSERT INTO docs (coll, id, data, updated) VALUES ('leads', ?, ?, 1)").run(id, JSON.stringify(Object.assign({}, d, { order: ++o, stage: 'contacted', contactedAt: 1795000000000 })));
const gone = SEED4[1][0];   // uno del SEED4 que ya no está no puede volver
db.prepare("INSERT INTO meta (k, v) VALUES ('crm_rev', '9')").run();

await seedOnce(env); await patchOnce(env); await delOnce(env); await outOnce(env);
const L = rows(db, 'leads'), ids = new Set(L.map((x) => x[0])), byId = Object.fromEntries(L);
t(SEED6_KEY === 'seed_20261123' && SEED6.length === N && new Set(SEED6.map((x) => x[0])).size === N, 'SEED6: 40 ids distintos');
t(SEED6.every((x) => ids.has(x[0])), 'entran las 40');
t(!ids.has(gone), 'el SEED4 no se vuelve a ejecutar');
t(L.length === SEED5.length + N, 'solo entran las 40 nuevas');
t(SEED6.every((x) => ['merceria', 'moda', 'sneakers', 'joya', 'suplementos'].includes(x[1].niche)), 'nichos esperados');
t(SEED6.every((x) => !/arab|árab|hiyab|hijab|abaya|caft|halal/i.test(x[1].name + ' ' + x[1].notes)), 'nada árabe');
t(SEED6.every((x) => !/canarias|tenerife|las palmas|lanzarote|fuerteventura/i.test(x[1].region + ' ' + x[1].zone)), 'nada de Canarias');
t(SEED6.every((x) => x[1].stage === 'new' && /^https:\/\/www\.instagram\.com\/[a-z0-9_.]+\/$/.test(x[1].instagram)), 'por contactar, con su Instagram');
t(SEED6.every((x) => /^\+34[6789]\d{8}$/.test(x[1].phone)), 'todas con teléfono');
t(SEED6.filter((x) => !/^\+34[67]/.test(x[1].phone)).length === 1, 'solo una con fijo (Calzados Isacio)');
t(SEED6.every((x) => /^Anuncios en Meta: /m.test(x[1].notes) && /^Nivel [ABC] /m.test(x[1].notes)), 'todas con anuncios y nivel en las notas');
t(SEED6.filter((x) => /^Nivel A/m.test(x[1].notes)).length === 16, '16 de nivel A (anuncian en Meta)');
t(SEED6.every((x) => /^Ya vende a distancia: .{10,}/m.test(x[1].notes) && /^Tienda online: /m.test(x[1].notes)), 'todas con su señal y su web');
t(SEED6.every((x) => x[1].lotDay === '2026-11-23' && !x[1].pageUrl && !x[1].slug), 'en el lote del 23/11, todavía sin propuesta');
t(SEED6.every((x) => !PREV.some((S) => S.some((y) => y[0] === x[0]))), 'ningún id repetido con lotes anteriores');
const ph = SEED6.map((x) => x[1].phone);
t(new Set(ph).size === N, 'ningún número repetido entre las 40');
const prevPh = new Set(PREV.flat().flatMap((x) => [x[1].phone, x[1].whatsapp]).filter(Boolean));
t(ph.every((p) => !prevPh.has(p)), 'ningún número de lotes anteriores');
const prevIg = new Set(PREV.flat().map((x) => x[1].instagram));
t(SEED6.every((x) => !prevIg.has(x[1].instagram)), 'ningún Instagram de lotes anteriores');
t(SEED5.every((x) => byId[x[0]].stage === 'contacted'), 'el lote anterior no cambia');
t(Number(db.prepare("SELECT v FROM meta WHERE k='crm_rev'").get().v) > 9, 'crm_rev sube');
const M = await import('./w23mod.mjs?again');
await M.seedOnce(env); await M.patchOnce(env); await M.delOnce(env); await M.outOnce(env);
t(rows(db, 'leads').length === SEED5.length + N, 'una sola vez: nada entra dos veces');
{
  const e2 = { DB: makeD1(), SEED_LOCAL: 1 }; for (const s of DDL) e2.DB._db.exec(s);
  const M2 = await import('./w23mod.mjs?empty');
  await M2.seedOnce(e2);
  const n = rows(e2.DB._db, 'leads').length;
  t(n >= SEED6.length + SEED5.length, 'CRM vacío: entran todas las listas (' + n + ')');
}
const J = JSON.parse(readFileSync(process.env.LEADS || '/home/claude/404growth/prospeccion/scrapeo-21nov/leads.json', 'utf8'));
t(J.length === N && J.every((x, i) => SEED6[i][1].instagram === `https://www.instagram.com/${x.ig}/`), 'leads.json y SEED6 en el mismo orden');
console.log(ok + ' bien, ' + ko + ' mal'); process.exit(ko ? 1 : 0);
