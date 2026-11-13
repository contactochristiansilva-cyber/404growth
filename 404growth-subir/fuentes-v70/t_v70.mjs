import { makeD1 } from './d1shim.mjs';
import { archApi } from './w70mod.mjs';
const env = { DB: makeD1() };
let ok = 0, ko = 0; const t = (c, m) => { if (c) ok++; else { ko++; console.log('FALLO:', m); } };
const R = (m, p, b, raw) => archApi(new Request('https://404growth.com/admin/api/' + p, { method: m, headers: raw ? { 'content-type': 'application/octet-stream' } : { 'content-type': 'application/json' }, body: raw || (b ? JSON.stringify(b) : undefined) }), env, p);
const J = async (r) => ({ s: r.status, j: await r.json() });
// 1. empty list
let r = await J(await R('GET', 'arch')); t(r.s === 200 && r.j.files.length === 0 && r.j.part === 1500000 && typeof r.j.db === 'number', 'lista vacía');
// 2. a 3.7 MB PDF in 3 parts
const N = 3700000, pdf = new Uint8Array(N); for (let i = 0; i < N; i++) pdf[i] = (i * 31 + 7) & 255; pdf.set([0x25, 0x50, 0x44, 0x46, 0x2d, 0x31], 0);
r = await J(await R('POST', 'arch', { name: 'Escritura notaría.pdf', size: N, folder: '  Hacienda ' })); t(r.s === 200 && r.j.parts === 3, 'crear');
const id = r.j.id;
t((await R('POST', 'arch/' + id + '/done')).status === 409, 'done sin trozos = incompleto');
t((await R('PUT', 'arch/' + id + '/p/0', null, pdf.slice(0, 1000))).status === 400, 'trozo de tamaño malo');
t((await R('PUT', 'arch/' + id + '/p/5', null, pdf.slice(0, 10))).status === 400, 'trozo fuera de rango');
for (let k = 0; k < 3; k++) { const x = await R('PUT', 'arch/' + id + '/p/' + k, null, pdf.slice(k * 1500000, Math.min(N, (k + 1) * 1500000))); t(x.status === 200, 'trozo ' + k); }
// a part sent twice (a retry) does not break it
t((await R('PUT', 'arch/' + id + '/p/1', null, pdf.slice(1500000, 3000000))).status === 200, 'reintento de un trozo');
r = await J(await R('GET', 'arch')); t(r.j.files.length === 0, 'no sale en la lista hasta acabar');
r = await J(await R('POST', 'arch/' + id + '/done')); t(r.s === 200 && r.j.type === 'application/pdf', 'acabar: es PDF');
r = await J(await R('GET', 'arch')); t(r.j.files.length === 1 && r.j.files[0].folder === 'Hacienda' && r.j.files[0].size === N && r.j.used === N, 'lista con el PDF en Hacienda');
// 3. download is the same bytes, inline only with ver=1
let d = await archApi(new Request('https://404growth.com/admin/api/arch/' + id + '?ver=1'), env, 'arch/' + id);
let got = new Uint8Array(await d.arrayBuffer()); t(d.headers.get('content-type') === 'application/pdf' && /^inline/.test(d.headers.get('content-disposition')), 'ver PDF en línea');
t(got.length === N && got.every((v, i) => v === pdf[i]), 'mismos bytes');
d = await archApi(new Request('https://404growth.com/admin/api/arch/' + id), env, 'arch/' + id);
t(/^attachment/.test(d.headers.get('content-disposition')) && /filename\*=UTF-8''Escritura%20notar%C3%ADa\.pdf/.test(d.headers.get('content-disposition')), 'descargar con su nombre');
await d.arrayBuffer();
// 4. an HTML file is never opened inline (it would run inside the admin)
const html = new TextEncoder().encode('<script>alert(1)</script>');
r = await J(await R('POST', 'arch', { name: 'x.html', size: html.length }));
const hid = r.j.id; t(r.j.parts === 1, 'html 1 trozo'); await R('PUT', 'arch/' + hid + '/p/0', null, html);
r = await J(await R('POST', 'arch/' + hid + '/done')); t(r.j.type === '', 'html sin tipo visible');
d = await archApi(new Request('https://404growth.com/admin/api/arch/' + hid + '?ver=1'), env, 'arch/' + hid);
t(d.headers.get('content-type') === 'application/octet-stream' && /^attachment/.test(d.headers.get('content-disposition')) && d.headers.get('x-content-type-options') === 'nosniff', 'html solo se descarga'); await d.arrayBuffer();
// 5. limits and names
t((await R('POST', 'arch', { name: 'grande.zip', size: 60 * 1048576 })).status === 413, 'más de 50 MB');
t((await R('POST', 'arch', { name: 'vacío.txt', size: 0 })).status === 400, 'vacío');
t((await R('POST', 'arch', { name: '   ', size: 10 })).status === 400, 'sin nombre');
r = await J(await R('POST', 'arch', { name: '../../etc/pass:wd', size: 3 })); const nid = r.j.id;
await R('PUT', 'arch/' + nid + '/p/0', null, new Uint8Array([1, 2, 3])); await R('POST', 'arch/' + nid + '/done');
r = await J(await R('GET', 'arch')); const nf = r.j.files.find((f) => f.id === nid); t(nf && !/[\/:]/.test(nf.name) && nf.folder === 'General', 'nombre limpio y carpeta General: ' + (nf && nf.name));
// 6. edit: rename, move, note; rename a folder
t((await R('POST', 'arch/' + id, { name: 'Escritura.pdf', folder: 'Notaría', note: 'Original en el cajón' })).status === 200, 'editar');
r = await J(await R('GET', 'arch')); let f1 = r.j.files.find((f) => f.id === id); t(f1.name === 'Escritura.pdf' && f1.folder === 'Notaría' && f1.note === 'Original en el cajón', 'editado');
t((await R('POST', 'arch/' + id, { name: '' })).status === 400, 'no deja nombre vacío');
r = await J(await R('POST', 'archf', { from: 'Notaría', to: 'Escrituras' })); t(r.j.folder === 'Escrituras', 'carpeta renombrada');
r = await J(await R('GET', 'arch')); f1 = r.j.files.find((f) => f.id === id); t(f1.folder === 'Escrituras', 'archivo movido con la carpeta');
// 7. a cut-off upload disappears after 6 hours; delete removes the parts
r = await J(await R('POST', 'arch', { name: 'a medias.pdf', size: 2000000 })); const cut = r.j.id; await R('PUT', 'arch/' + cut + '/p/0', null, pdf.slice(0, 1500000));
env.DB._db.prepare('UPDATE arch SET created = created - 7*3600000 WHERE id = ?').run(cut);
await R('GET', 'arch'); t(!env.DB._db.prepare('SELECT 1 FROM arch WHERE id = ?').get(cut) && !env.DB._db.prepare('SELECT 1 FROM archp WHERE id = ?').get(cut), 'subida cortada se borra');
t((await R('DELETE', 'arch/' + id)).status === 200 && !env.DB._db.prepare('SELECT 1 FROM archp WHERE id = ?').get(id), 'borrar quita los trozos');
t((await archApi(new Request('https://404growth.com/admin/api/arch/' + id), env, 'arch/' + id)).status === 404, 'borrado ya no se descarga');
// 8. the database limit
env.DB._db.exec("CREATE TABLE IF NOT EXISTS big (b BLOB)"); const blk = new Uint8Array(4 * 1048576);
for (let i = 0; i < 112; i++) env.DB._db.prepare('INSERT INTO big VALUES (?)').run(blk);   // ~448 MB
r = await J(await R('POST', 'arch', { name: 'otro.pdf', size: 5 * 1048576 })); t(r.s === 507 && r.j.error === 'full', 'admin lleno: ' + r.s);
console.log(ok + ' bien, ' + ko + ' mal'); process.exit(ko ? 1 : 0);
