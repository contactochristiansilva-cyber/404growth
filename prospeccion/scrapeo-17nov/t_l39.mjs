// 17/11 (for 18/11): SEED3 = 30 new shops (no moda, no food), LEAD_PATCH = the 5 unsent of the lote 38 to the batch of 18/11, 4 new niches.
import { makeD1 } from './d1shim.mjs';
import { writeFileSync, readFileSync, existsSync } from 'node:fs';
const OUT = '/home/claude/404growth/prospeccion/l33/out';
import { execFileSync } from 'node:child_process';
import { seedOnce, patchOnce, delOnce, outOnce, DDL, PAGES, SEED, SEED_KEY, SEED2, SEED2_KEY, SEED3, SEED3_KEY, LEAD_PATCH, LEAD_PATCH_KEY, LEAD_PATCH_17NOV, LEAD_OUT_KEY } from './w80mod.mjs';
let ok = 0, ko = 0; const t = (c, m) => { if (c) ok++; else { ko++; console.log('FALLO:', m); } };
const rows = (db, coll) => db.prepare("SELECT id, data FROM docs WHERE coll=?").all(coll).map((r) => [r.id, JSON.parse(r.data)]);

// Production: SEED, SEED2, the 17/11 patch, ldel and lout already ran; the lote 38 is in the CRM with 25 sent and 5 unsent.
const env = { DB: makeD1(), SEED_LOCAL: 1 }; for (const s of DDL) env.DB._db.exec(s); const db = env.DB._db;
for (const k of [SEED_KEY, SEED2_KEY, 'lpatch_20261117', 'ldel_20261115b', LEAD_OUT_KEY]) db.prepare("INSERT INTO meta (k, v) VALUES (?, '1')").run(k);
let o = 0;
const p17 = Object.fromEntries(LEAD_PATCH_17NOV);
for (const [id, d] of SEED2) db.prepare("INSERT INTO docs (coll, id, data, updated) VALUES ('leads', ?, ?, 1)").run(id, JSON.stringify(Object.assign({}, d, p17[id], { order: ++o })));
const unsent = LEAD_PATCH.map((x) => x[0]);
for (const [id] of SEED2) if (!unsent.includes(id)) db.prepare("UPDATE docs SET data = json_set(data, '$.stage', 'contacted', '$.contactedAt', 1789000000000) WHERE coll='leads' AND id=?").run(id);
const gone = SEED[3][0];   // a lead of the old SEED that Chris deleted by hand must not come back
db.prepare("INSERT INTO meta (k, v) VALUES ('crm_rev', '7')").run();

await seedOnce(env); await patchOnce(env); await delOnce(env); await outOnce(env);
const L = rows(db, 'leads'), ids = new Set(L.map((x) => x[0])), byId = Object.fromEntries(L);
t(SEED3_KEY === 'seed_20261118' && SEED3.length === 30 && new Set(SEED3.map((x) => x[0])).size === 30, 'SEED3: 30 ids distintos');
t(SEED3.every((x) => ids.has(x[0])), 'entran las 30');
t(!ids.has(gone), 'el SEED viejo no se vuelve a ejecutar');
t(L.length === 60, 'solo entran las 30 nuevas (30 del lote 38 + 30)');
const N = ['merceria', 'arte', 'artesania', 'electro', 'joya', 'cosmetica', 'suplementos', 'toys', 'deporte'];
t(SEED3.every((x) => N.includes(x[1].niche)), 'ningún nicho de moda ni de comida');
t(SEED3.every((x) => !/arab|árab|hiyab|hijab|moda|boutique|carnic|jam[oó]n|charcut|gourmet|vino/i.test(x[1].name + ' ' + x[1].notes)), 'nada árabe, de moda ni de comida en nombres y notas');
t(SEED3.every((x) => x[1].stage === 'new' && x[1].igFollowers >= 10000 && /^https:\/\/www\.instagram\.com\/[a-z0-9_.]+\/$/.test(x[1].instagram)), 'por contactar, +10k y con su Instagram');
t(SEED3.every((x) => /^\+34[6789]\d{8}$/.test(x[1].phone)), 'todas con teléfono');
t(SEED3.every((x) => x[1].whatsapp === '' ? x[1].phoneType === 'fijo' && /AVISO: Solo publican fijo/.test(x[1].notes) : /^\+34\d{9}$/.test(x[1].whatsapp)), 'sin WhatsApp solo las de fijo, con su aviso');
t(SEED3.filter((x) => x[1].waOk === false).every((x) => /WhatsApp sin comprobar/.test(x[1].notes)), 'waOk false = WhatsApp sin comprobar en las notas');
t(SEED3.filter((x) => x[1].waOk !== false && x[1].whatsapp).every((x) => /lo publican como WhatsApp/.test(x[1].notes)), 'las demás lo publican como WhatsApp');
// 17/11 por la noche: las 30 ya tienen propuesta (lote 39) y van al lote del 18/11
const SEL = JSON.parse(readFileSync('/home/claude/404growth/prospeccion/l33/sel39.json', 'utf8'));
const SL = new Set(SEL.map((x) => x.slug));
t(SEED3.every((x) => SL.has(x[1].slug) && x[1].pageUrl === `https://404growth.com/p/${x[1].slug}/` && x[1].lotDay === '2026-11-18' && x[1].notes.includes(x[1].pageUrl)), 'las 30 con su propuesta y en el lote del 18/11');
t(new Set(SEED3.map((x) => x[1].slug)).size === 30 && SEL.length === 30, 'una propuesta distinta para cada una');
t(SEED3.every((x) => existsSync(`${OUT}/p-${x[1].slug}.html`) && existsSync(`${OUT}/p-${x[1].slug}--tienda.html`)), 'las 30 páginas están hechas (out/)');
t(SEED3.every((x) => byId[x[0]] && byId[x[0]].pageUrl === x[1].pageUrl && byId[x[0]].lotDay === '2026-11-18' && byId[x[0]].stage === 'new'), 'en el CRM salen en el lote del 18/11 con su enlace');
t(SEED3.every((x) => !SEED2.some((y) => y[0] === x[0]) && !SEED.some((y) => y[0] === x[0])), 'ningún id repetido con lotes anteriores');
t(LEAD_PATCH_KEY === 'lpatch_20261118' && LEAD_PATCH.length === 35 && LEAD_PATCH.slice(0, 5).every((x) => x[1].lotDay === '2026-11-18' && Object.keys(x[1]).length === 1)
  && LEAD_PATCH.slice(5).every((x, i) => x[0] === SEED3[i][0] && x[1].lotDay === '2026-11-18' && x[1].pageUrl === SEED3[i][1].pageUrl && x[1].slug === SEED3[i][1].slug), 'el parche nuevo: las 5 del lote 38 y las 30 con su propuesta al 18/11');
t(unsent.every((id) => byId[id] && byId[id].lotDay === '2026-11-18' && byId[id].stage === 'new' && byId[id].pageUrl), 'las 5 sin enviar del lote 38 pasan al 18/11 con su propuesta');
t(SEED2.filter((x) => !unsent.includes(x[0])).every((x) => byId[x[0]].lotDay === '2026-11-17' && byId[x[0]].stage === 'contacted'), 'las enviadas del lote 38 no cambian');
t(rows(db, 'leads_out').length === 0, 'outOnce no vuelve a sacar nada');
t(Number(db.prepare("SELECT v FROM meta WHERE k='crm_rev'").get().v) > 7, 'crm_rev sube');
// once: a second run with a fresh module changes nothing
const M = await import('./w80mod.mjs?again');
await M.seedOnce(env); await M.patchOnce(env); await M.delOnce(env); await M.outOnce(env);
t(rows(db, 'leads').length === 60, 'una sola vez: nada entra dos veces');

// if the SEED3 had already gone in without proposal, the patch adds it
{
  const e2 = { DB: makeD1(), SEED_LOCAL: 1 }; for (const s of DDL) e2.DB._db.exec(s); const d2 = e2.DB._db;
  for (const k of [SEED_KEY, SEED2_KEY, SEED3_KEY, 'lpatch_20261117', 'ldel_20261115b', LEAD_OUT_KEY]) d2.prepare("INSERT INTO meta (k, v) VALUES (?, '1')").run(k);
  let n = 0;
  for (const [id, d] of SEED3) { const c = Object.assign({}, d, { order: ++n }); delete c.pageUrl; delete c.slug; delete c.lotDay; d2.prepare("INSERT INTO docs (coll, id, data, updated) VALUES ('leads', ?, ?, 1)").run(id, JSON.stringify(c)); }
  const M3 = await import('./w80mod.mjs?third');   // fresh module: lpatched is per module
  await M3.patchOnce(e2);
  const B = Object.fromEntries(rows(d2, 'leads'));
  t(SEED3.every((x) => B[x[0]].pageUrl === x[1].pageUrl && B[x[0]].lotDay === '2026-11-18'), 'con el SEED3 ya subido sin propuesta, el parche le pone la propuesta y el lote');
}

// the 4 new niches in the CRM page
const crm = PAGES.crm, adm = PAGES.admin;
for (const k of ['merceria', 'arte', 'artesania', 'electro']) {
  t(new RegExp('var SHOPN=\\{[^}]*,' + k + ':1').test(crm) && new RegExp('NOPAGE=\\{[^}]*,' + k + ':1').test(crm) && new RegExp('var IGN=\\{[^}]*,' + k + ':1').test(crm) && new RegExp('var ESN=\\{[^}]*,' + k + ':1').test(crm), k + ': tienda con propuesta (SHOPN, NOPAGE, IGN, ESN)');
  t(crm.includes("['" + k + "','") && crm.includes(k + ":'_" + k + "'") && crm.includes('deal_' + k + ':2500') && crm.includes('em1s_' + k + ':'), k + ': pestaña y textos');
  t(adm.includes(k + ": '") && adm.includes(k + ":'"), k + ': nombre en el admin');
}
// every inline script of the two pages still parses
let bad = 0;
for (const [name, html] of [['crm', crm], ['admin', adm]]) {
  const sc = [...html.matchAll(/<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)<\/script>/g)].map((m) => m[1]).filter((s) => s.trim());
  sc.forEach((s, i) => { const f = `/tmp/claude-0/-home-claude/86561a8c-5895-52c1-874b-e63866019285/scratchpad/t39/s_${name}_${i}.js`; writeFileSync(f, s); try { execFileSync('node', ['--check', f], { stdio: 'pipe' }); } catch (e) { bad++; console.log('script roto', name, i, String(e.stderr).slice(0, 300)); } });
}
t(bad === 0, 'los scripts de las páginas CRM y admin compilan');
console.log(ok + ' bien, ' + ko + ' mal'); process.exit(ko ? 1 : 0);
