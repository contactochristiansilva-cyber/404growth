// 17/11 (lote 38): SEED2 = 30 sin muebles, LEAD_PATCH al lote del 17/11 y las del 16/11 sin enviar salen del CRM (a leads_out).
import { makeD1 } from './d1shim.mjs';
import { seedOnce, patchOnce, delOnce, outOnce, DDL, SEED, SEED_KEY, SEED2, SEED2_KEY, LEAD_PATCH, LEAD_PATCH_KEY, LEAD_PATCH_16NOV, LEAD_DEL, LEAD_OUT_KEY } from './w79mod.mjs';
let ok = 0, ko = 0; const t = (c, m) => { if (c) ok++; else { ko++; console.log('FALLO:', m); } };
const rows = (db, coll) => db.prepare("SELECT id, data FROM docs WHERE coll=?").all(coll).map((r) => [r.id, JSON.parse(r.data)]);

// Production case: SEED and lpatch_20261116c already ran; the 16/11 batch (LEAD_PATCH_16NOV) is in the CRM, some sent.
const env = { DB: makeD1(), SEED_LOCAL: 1 }; for (const s of DDL) env.DB._db.exec(s); const db = env.DB._db;
for (const k of [SEED_KEY, 'ldel_20261115b', 'lpatch_20261116c']) db.prepare("INSERT INTO meta (k, v) VALUES (?, '1')").run(k);
const byId = Object.fromEntries(SEED.map((x) => [x[0], x[1]]));
const lot16 = LEAD_PATCH_16NOV.map((x) => x[0]).filter((id) => byId[id]);
let o = 0;
for (const id of lot16) db.prepare("INSERT INTO docs (coll, id, data, updated) VALUES ('leads', ?, ?, 1)").run(id, JSON.stringify(Object.assign({}, byId[id], LEAD_PATCH_16NOV.find((x) => x[0] === id)[1], { order: ++o })));
const sent = lot16.slice(0, 5), hasNote = lot16[6];
for (const id of sent) db.prepare("UPDATE docs SET data = json_set(data, '$.stage', 'contacted', '$.contactedAt', 1789000000000) WHERE coll='leads' AND id=?").run(id);
db.prepare("UPDATE docs SET data = json_set(data, '$.notes', json_extract(data, '$.notes') || ' nota de Chris') WHERE coll='leads' AND id=?").run(hasNote);
const other = ['mod-otro-dia-sevilla', { niche: 'moda', name: 'Otro día', stage: 'new', pageUrl: 'https://404growth.com/p/otro/' }];   // a lead from another day stays
db.prepare("INSERT INTO docs (coll, id, data, updated) VALUES ('leads', ?, ?, 1)").run(other[0], JSON.stringify(Object.assign({}, other[1], { order: ++o, lotDay: '2026-11-13' })));
db.prepare("INSERT INTO meta (k, v) VALUES ('crm_rev', '5')").run();

await seedOnce(env); await patchOnce(env); await delOnce(env); await outOnce(env);
const L = rows(db, 'leads'), ids = new Set(L.map((x) => x[0])), out = rows(db, 'leads_out');
t(SEED2_KEY === 'seed_20261116w' && SEED2.length === 30 && new Set(SEED2.map((x) => x[0])).size === 30, 'SEED2: 30 ids distintos');
t(SEED2.every((x) => ['moda', 'joya', 'sneakers'].includes(x[1].niche)), 'sin muebles');
t(!SEED2.some((x) => /matia/i.test(x[0])), 'sin Matia');
t(SEED2.every((x) => ids.has(x[0])), 'entran las 30');
t(LEAD_PATCH_KEY === 'lpatch_20261117' && LEAD_PATCH.length === 30 && LEAD_PATCH.every((x) => SEED2.some((y) => y[0] === x[0])), 'el parche nuevo es de las 30');
const S2 = L.filter((x) => SEED2.some((y) => y[0] === x[0])).map((x) => x[1]);
t(S2.every((d) => d.lotDay === '2026-11-17' && /^https:\/\/404growth\.com\/p\/[a-z0-9-]+\/$/.test(d.pageUrl) && d.pageUrl.endsWith('/' + d.slug + '/')), 'las 30 con lotDay 17/11, slug y pageUrl');
t(S2.every((d) => d.stage === 'new' && /^\+34[67]\d{8}$/.test(d.whatsapp)), 'por contactar y con WhatsApp móvil');
t(S2.every((d) => !/arab|árab|hiyab|hijab|mueble|sof[aá]|colch/i.test(d.name + ' ' + d.notes)), 'nada árabe ni de muebles');
t(new Set(S2.map((d) => d.slug)).size === 30, 'slugs distintos');
t(sent.every((id) => ids.has(id)), 'las enviadas del 16/11 se quedan');
const unsent = lot16.filter((id) => !sent.includes(id));
t(unsent.every((id) => !ids.has(id)), 'las del 16/11 sin enviar salen del CRM');
t(out.length === unsent.length && unsent.every((id) => out.some((x) => x[0] === id)), 'y quedan en leads_out');
t(out.find((x) => x[0] === hasNote)[1].notes.endsWith('nota de Chris'), 'leads_out guarda sus datos tal cual');
t(ids.has(other[0]), 'un lead de otro día no se toca');
t(JSON.parse(db.prepare("SELECT v FROM meta WHERE k=?").get(LEAD_OUT_KEY).v).length === unsent.length, 'los ids quedan en meta');
t(Number(db.prepare("SELECT v FROM meta WHERE k='crm_rev'").get().v) > 5, 'crm_rev sube (los navegadores recargan)');
// once: a second run with a fresh module does not move anything else (key in meta)
const M = await import('./w79mod.mjs?again');
db.prepare("UPDATE docs SET data = json_set(data, '$.lotDay', '2026-11-16') WHERE coll='leads' AND id=?").run(SEED2[0][0]);
await M.seedOnce(env); await M.patchOnce(env); await M.delOnce(env); await M.outOnce(env);
t(rows(db, 'leads').some((x) => x[0] === SEED2[0][0]), 'una sola vez: con la clave guardada no saca nada más');
t(rows(db, 'leads').length === L.length, 'nada entra dos veces');
console.log(ok + ' bien, ' + ko + ' mal'); process.exit(ko ? 1 : 0);
