// Prueba de la v78 (briefs): enlace con clave, guardar campo a campo sin pisar a otros, archivos, enviar, avisos y el admin.
// Antes: cp <worker v78> w78mod.mjs && echo "export { briefPublic, briefApi, BRIEF_Q };" >> w78mod.mjs
import { makeD1 } from './d1shim.mjs';
import { makeR2 } from './r2.mjs';
const PUSH = [];
globalThis.__push = PUSH;
const mod = await import('./w78mod.mjs');
const { briefPublic, briefApi, BRIEF_Q } = mod;
const env = { DB: makeD1(), DEV: 'http://localhost:8778', TV: makeR2() };
env.DB._db.exec("CREATE TABLE IF NOT EXISTS meta (k TEXT PRIMARY KEY, v TEXT)");
let ok = 0, ko = 0; const t = (c, m) => { if (c) ok++; else { ko++; console.log('FALLO:', m); } };
const O = { origin: 'http://localhost:8778', 'content-type': 'application/json' };
const P = async (method, path, b, h) => { const r = await briefPublic(new Request('http://localhost:8778/l/' + path, { method, headers: Object.assign({}, O, h || {}), body: b === undefined ? undefined : (b instanceof Uint8Array || typeof b === 'string' ? b : JSON.stringify(b)) }), env, {}, path.split('?')[0]); return { s: r.status, j: await r.json().catch(() => null) }; };
const A = async (method, path, b) => { const r = await briefApi(new Request('http://localhost:8778/admin/api/' + path, { method, headers: { 'content-type': 'application/json' }, body: b ? JSON.stringify(b) : undefined }), env, path.split('?')[0]); return r; };
const AJ = async (m, p, b) => (await A(m, p, b)).json();

// 1. el brief existe solo, con su clave (no está en el código)
let L = await AJ('GET', 'brief'); const br = L.briefs.find((x) => x.id === 'efap-miami');
t(br && /\/brief\/efap-miami\/\?k=[A-Za-z0-9_-]{24}$/.test(br.link), 'el brief de EFAP con su enlace: ' + (br && br.link));
t(br.tot === 91 && br.n === 0 && !br.started && !br.sent, 'sin empezar, 91 preguntas: ' + br.tot);
const K = br.link.split('k=')[1];
// 2. sin clave o con otra clave, nada
t((await P('GET', 'brief?b=efap-miami&k=xxxxxxxxxxxxxxxxxxxxxxxx')).s === 403, 'clave mala: 403');
t((await P('GET', 'brief?b=efap-miami')).s === 403, 'sin clave: 403');
t((await P('POST', 'brief', { b: 'efap-miami', k: K, set: { quien: 'x' } }, { origin: 'https://otro.com' })).s === 403, 'otro origen: 403');
// 3. guardar campo a campo; dos personas a la vez no se pisan
let r = await P('POST', 'brief', { b: 'efap-miami', k: K, set: { quien: 'Ana · coordinadora', fecha: '2027-01-16', edades: ['8 a 12 (Academy)', '13 a 15 (Performance)'], precio: 'Otro', precio_o: '10 $ que se devuelven', c_jug: 'cambiar', c_jug_o: 'Más de 500', agenda__p: true, inventado: 'no' } });
t(r.s === 200 && r.j.n === 8, 'guarda 8 campos (el inventado no): ' + JSON.stringify(r.j));
await P('POST', 'brief', { b: 'efap-miami', k: K, set: { lugar: 'Campo X, Hollywood' } });   // otra persona, otro campo
r = await P('GET', 'brief?b=efap-miami&k=' + K);
const d = r.j.data;
t(d.quien === 'Ana · coordinadora' && d.lugar === 'Campo X, Hollywood' && d.edades.length === 2 && d.agenda__p === 1 && !('inventado' in d), 'los dos cambios están y nada inventado');
await P('POST', 'brief', { b: 'efap-miami', k: K, set: { agenda__p: false, lugar: '' } });
r = await P('GET', 'brief?b=efap-miami&k=' + K);
t(!('agenda__p' in r.j.data) && !('lugar' in r.j.data) && r.j.data.quien, 'vaciar un campo lo quita y no toca el resto');
t(PUSH.filter((x) => /Brief empezado/.test(x.title)).length === 1, 'un solo aviso de «empezado»: ' + PUSH.map((x) => x.title).join(' | '));
// 4. textos muy largos se recortan; tipos raros fuera
await P('POST', 'brief', { b: 'efap-miami', k: K, set: { agenda: 'a'.repeat(9000), edades: 'no es lista', aforo: 150 } });
r = await P('GET', 'brief?b=efap-miami&k=' + K);
t(r.j.data.agenda.length === 8000 && Array.isArray(r.j.data.edades) && r.j.data.aforo === '150', 'largo recortado, lista intacta, número como texto');
// 5. archivos
const png = new Uint8Array([137, 80, 78, 71, 13, 10, 26, 10, 1, 2, 3]);
r = await P('PUT', 'briefup?b=efap-miami&k=' + K + '&n=' + encodeURIComponent('Logo EFAP (vector).png'), png, { 'content-type': 'image/png', 'content-length': String(png.length) });
t(r.s === 200 && r.j.files.length === 1 && r.j.files[0].name === 'Logo EFAP (vector).png' && /^brief\/efap-miami\/.+Logo_EFAP_vector_\.png$/.test(r.j.files[0].k), 'sube el archivo a brief/efap-miami/: ' + JSON.stringify(r.j && r.j.files));
const fk = r.j.files[0].k;
t(env.TV.objs.has(fk), 'está en R2');
r = await P('PUT', 'briefup?b=efap-miami&k=' + K + '&n=big.mov', new Uint8Array(4), { 'content-type': 'video/quicktime', 'content-length': String(96 * 1048576) });
t(r.s === 413, 'más de 95 MB: 413');
r = await P('PUT', 'briefup?b=efap-miami&k=mal' + K.slice(3) + '&n=x.png', png, { 'content-type': 'image/png', 'content-length': String(png.length) });
t(r.s === 403, 'subir con otra clave: 403');
// 6. el admin lo ve todo y descarga el archivo
let D = await AJ('GET', 'brief/efap-miami');
t(D.q && D.q.sections.length === 10 && D.brief.files.length === 1 && D.brief.n >= 7, 'el admin tiene preguntas, respuestas y archivo: ' + D.brief.n);
let fr = await A('GET', 'brief/efap-miami/f?k=' + encodeURIComponent(fk));
t(fr.status === 200 && fr.headers.get('content-type') === 'image/png' && /inline/.test(fr.headers.get('content-disposition')), 'la foto se abre en el navegador');
r = await P('PUT', 'briefup?b=efap-miami&k=' + K + '&n=pagina.html', new TextEncoder().encode('<script>alert(1)</script>'), { 'content-type': 'text/html', 'content-length': '25' });
const hk = r.j.files[1].k;
fr = await A('GET', 'brief/efap-miami/f?k=' + encodeURIComponent(hk));
t(fr.headers.get('content-type') === 'application/octet-stream' && /attachment/.test(fr.headers.get('content-disposition')), 'un HTML subido solo se descarga');
t((await A('GET', 'brief/efap-miami/f?k=brief/efap-miami/otro')).status === 404, 'un archivo que no es suyo: 404');
// 7. quitar un archivo
r = await P('POST', 'brief', { b: 'efap-miami', k: K, a: 'rmfile', f: hk });
t(r.j.files.length === 1 && !env.TV.objs.has(hk), 'quitado de la lista y de R2');
// 8. enviar
r = await P('POST', 'brief', { b: 'efap-miami', k: K, a: 'send' });
t(r.s === 200 && r.j.sent, 'enviado');
t(PUSH.some((x) => /Brief enviado · EFAP Miami/.test(x.title) && /de 91 preguntas respondidas y 1 archivo\./.test(x.body)), 'aviso de enviado con el recuento: ' + PUSH.map((x) => x.body).join(' | '));
L = await AJ('GET', 'brief'); t(L.briefs[0].sent && L.briefs[0].who === 'Ana · coordinadora', 'en la lista: enviado y quién lo rellena');
// 9. vaciar (después de probarlo uno mismo): misma clave, sin datos ni archivos
t((await AJ('POST', 'brief/efap-miami/reset', {})).ok, 'vaciado');
r = await P('GET', 'brief?b=efap-miami&k=' + K);
t(r.s === 200 && !Object.keys(r.j.data).length && !r.j.files.length && !r.j.sent && !env.TV.objs.has(fk), 'vacío, sin archivos, la clave sigue valiendo');
L = await AJ('GET', 'brief'); t(!L.briefs[0].started, 'vuelve a «Sin empezar»');
console.log(ok + ' bien, ' + ko + ' mal'); process.exit(ko ? 1 : 0);
