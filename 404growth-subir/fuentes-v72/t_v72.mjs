// Prueba de la v72. Antes: cp ../admin/worker.js w72mod.mjs && echo "export { delivApi, DDL };" >> w72mod.mjs ; después: node t_v72.mjs
import { makeD1 } from './d1shim.mjs';
import { delivApi, DDL } from './w72mod.mjs';
const env = { DB: makeD1() }; for (const s of DDL) env.DB._db.exec(s);
let ok = 0, ko = 0; const t = (c, m) => { if (c) ok++; else { ko++; console.log('FALLO:', m); } };
const R = async (m, p, b) => { const r = await delivApi(new Request('https://404growth.com/admin/api/' + p, { method: m, headers: { 'content-type': 'application/json' }, body: b ? JSON.stringify(b) : undefined }), env, p); return { s: r.status, j: await r.json() }; };
const db = env.DB._db;
db.prepare("INSERT INTO clients (id, name, created, start_date, archived) VALUES ('c_AAA111', 'Cliente Uno', 1, '2026-11-13', 0), ('c_BBB222', 'Cliente Dos', 2, '2026-11-09', 0), ('c_CCC333', 'Cliente Archivado', 3, '', 1)").run();
let r = await R('GET', 'deliv'); t(r.s === 200 && r.j.clients.length === 3 && Object.keys(r.j.items).length === 0, 'lista vacía');
t(r.j.clients.find((c) => c.id === 'c_AAA111').start === '2026-11-13' && r.j.clients.find((c) => c.id === 'c_CCC333').archived === true, 'arranque y archivado');
r = await R('POST', 'deliv/c_AAA111', { at: '2026-11-28T20:00', note: 'Web' }); t(r.s === 200 && r.j.item.at === '2026-11-28T20:00' && r.j.item.note === 'Web' && !r.j.item.done, 'poner fecha');
r = await R('POST', 'deliv/c_AAA111', { at: '2026-13-01T20:00' }); t(r.s === 400 && r.j.error === 'date', 'fecha mala');
r = await R('POST', 'deliv/c_AAA111', { at: '2026-11-28T24:00' }); t(r.s === 400, 'hora mala');
r = await R('POST', 'deliv/c_ZZZ999', { at: '2026-11-28T20:00' }); t(r.s === 404, 'cliente que no existe');
r = await R('POST', 'deliv/../x', { at: '2026-11-28T20:00' }); t(r.s === 404, 'ruta rara');
r = await R('POST', 'deliv/c_AAA111', { done: true }); t(r.j.item.done > 0, 'entregada');
r = await R('POST', 'deliv/c_AAA111', { at: '2026-11-29T23:59' }); t(!r.j.item.done && r.j.item.note === 'Web', 'cambiar la fecha la vuelve a poner en cuenta atrás y mantiene la nota');
r = await R('POST', 'deliv/c_BBB222', { done: true }); t(r.s === 400, 'no se puede entregar sin fecha');
r = await R('POST', 'deliv/c_AAA111', { done: true }); r = await R('POST', 'deliv/c_AAA111', { done: false }); t(r.j.item.done === null, 'volver a la cuenta atrás');
r = await R('GET', 'deliv'); t(r.j.items.c_AAA111.at === '2026-11-29T23:59' && r.j.items.c_AAA111.upd > 0, 'se lee');
r = await R('POST', 'deliv/c_AAA111', { at: '', note: '' }); t(r.j.item === null, 'quitar todo borra');
r = await R('GET', 'deliv'); t(!r.j.items.c_AAA111, 'ya no está');
r = await R('POST', 'deliv/c_BBB222', { at: '2026-11-24T23:59', note: 'x'.repeat(500) }); t(r.j.item.note.length === 200, 'nota recortada');
// nada del portal lo lee: la colección solo aparece en delivApi
const src = (await import('node:fs')).readFileSync('w72mod.mjs', 'utf8');
const a0 = src.indexOf('async function delivApi'), a1 = src.indexOf('async function quotesApi');
const pos = [...src.matchAll(/coll = 'deliv'|VALUES \('deliv'/g)].map((m) => m.index);
t(pos.length === 4 && pos.every((i) => i > a0 && i < a1), 'la colección deliv solo se usa dentro de delivApi');
console.log(ok + ' bien, ' + ko + ' mal'); process.exit(ko ? 1 : 0);
