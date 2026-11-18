// Prueba del vídeo selfie (v77f): subida por partes a R2, la candidatura con su vídeo, reproducir con rangos y borrar.
// Antes, como t_v77.mjs: cp <worker> w77mod.mjs && echo "export { talPublic, talApi, talReady, DDL, TAL };" >> w77mod.mjs
import { makeD1 } from './d1shim.mjs';
import { makeR2 } from './r2mock.mjs';
globalThis.fetch = async (url, o) => {
  const u = String(url);
  if (u.startsWith('https://api.anthropic.com/')) {
    const b = JSON.parse(o.body); fetch.last = b;
    const ids = b.tools[0].input_schema.properties.scores.items.properties.id.enum;
    return new Response(JSON.stringify({ content: [{ type: 'tool_use', name: 'puntuar', input: { scores: ids.map((id) => ({ id, score: 3, why: 'x' })), summary: 's', strengths: [], risks: [], rec: 'dudoso', questions: [] } }] }), { status: 200 });
  }
  if (u.includes('/emails')) return new Response('{}', { status: 200 });
  throw new Error('fetch inesperado: ' + u);
};
const { talPublic, talApi, DDL } = await import('./w77mod.mjs');
const env = { DB: makeD1(), TV: makeR2() }; for (const s of DDL) env.DB._db.exec(s);
const db = env.DB._db;
db.prepare("INSERT INTO meta (k, v) VALUES ('soc_cfg', ?)").run(JSON.stringify({ aiKey: 'k' }));
let ok = 0, ko = 0; const t = (c, m) => { if (c) ok++; else { ko++; console.log('FALLO:', m); } };
let ip = '2.2.2.2';
const H = () => ({ 'content-type': 'application/json', 'cf-connecting-ip': ip, origin: 'https://404growth.com' });
const P = async (p, b, e) => { const r = await talPublic(new Request('https://404growth.com/l/' + p, { method: 'POST', headers: H(), body: JSON.stringify(b) }), e || env, {}, p); return { s: r.status, j: await r.json() }; };
const PUT = async (q, buf, e) => { const r = await talPublic(new Request('https://404growth.com/l/jobvp' + q, { method: 'PUT', headers: Object.assign(H(), { 'content-length': String(buf.length) }), body: buf }), e || env, {}, 'jobvp'); return { s: r.status, j: await r.json() }; };
const A = async (m, p, hd, qs) => talApi(new Request('https://404growth.com/admin/api/' + p + (qs || ''), { method: m, headers: hd || {} }), env, p, {});
const ans = (x) => Object.assign({ name: 'Ana Vídeo Pérez', email: 'ana@example.com', phone: '+54 9 11 2345 6789', city: 'Buenos Aires, Argentina', portfolio: 'https://ana.example.com', hours: 'De 20 a 30 h', start: 'Ya', rate: '500 € por tienda', tz: 'si', lang: 'si', ko1: 'si', q1: 'Monté tres tiendas Shopify de moda y joyería, con el tema Dawn personalizado.', q2: 'Primero ordeno el catálogo y rehago las fotos con IA, luego portada y fichas.', q3: 'Nano Banana y GPT Image para fotos; Claude para textos y fichas.' }, x || {});
const MiB = 1048576, body = (n, fill) => { const b = new Uint8Array(n); b.fill(fill || 7); return b; };
const upload = async (size, job, type) => {
  let r = await P('jobv', { a: 'start', job: job || 'tiendas', size, type: type || 'video/mp4', dur: 42, src: 'rec' }); if (r.s !== 200) return r;
  const { k, t: tok, ps } = r.j, parts = [];
  for (let i = 0, n = 1; i < size; i += ps, n++) { const pr = await PUT('?k=' + encodeURIComponent(k) + '&t=' + tok + '&n=' + n, body(Math.min(ps, size - i), n)); if (pr.s !== 200) return pr; parts.push({ n, etag: pr.j.etag }); }
  r = await P('jobv', { a: 'done', k, t: tok, parts }); r.k = k; r.tok = tok; return r;
};

// 1. /l/jobs dice si hay vídeos
let r = await talPublic(new Request('https://404growth.com/l/jobs'), env, {}, 'jobs'); let j = await r.json(); t(j.vid === true && j.vmax === 150 * MiB, '/l/jobs: vid y vmax');
r = await talPublic(new Request('https://404growth.com/l/jobs'), { DB: env.DB }, {}, 'jobs'); j = await r.json(); t(j.vid === false, 'sin R2: vid false');
// 2. empezar: límites
r = await P('jobv', { a: 'start', job: 'tiendas', size: 151 * MiB, type: 'video/mp4' }); t(r.s === 413, 'más de 150 MB no');
r = await P('jobv', { a: 'start', job: 'tiendas', size: 3 * MiB, type: 'application/pdf' }); t(r.s === 415, 'solo vídeo');
r = await P('jobv', { a: 'start', job: 'tiendas', size: 100, type: 'video/mp4' }); t(r.s === 400, 'demasiado pequeño');
r = await P('jobv', { a: 'start', job: 'nada', size: 3 * MiB, type: 'video/mp4' }); t(r.s === 404, 'puesto que no existe');
r = await P('jobv', { a: 'start', job: 'tiendas', size: 3 * MiB, type: 'video/mp4' }, { DB: env.DB }); t(r.s === 503 && r.j.error === 'novid', 'sin R2: novid');
// 3. subida en 3 partes (8 + 8 + 4 MiB) y una de una sola parte
const up1 = await upload(20 * MiB); t(up1.s === 200 && up1.j.vk === up1.k + '|' + up1.tok && up1.j.size === 20 * MiB, 'subida por partes: ' + JSON.stringify(up1.j));
t(env.TV.objs.get(up1.k) && env.TV.objs.get(up1.k).data.length === 20 * MiB && env.TV.objs.get(up1.k).type === 'video/mp4', 'el vídeo está en R2');
const row1 = db.prepare('SELECT * FROM tvid WHERE k = ?').get(up1.k); t(row1.done === 1 && row1.cid === null && row1.src === 'rec' && row1.dur === 42, 'tvid: hecho, sin candidatura');
r = await PUT('?k=' + encodeURIComponent(up1.k) + '&t=' + up1.tok + '&n=1', body(10)); t(r.s === 404, 'no se añaden partes a un vídeo terminado');
// partes: código malo, parte de más, parte demasiado grande
r = await P('jobv', { a: 'start', job: 'tiendas', size: 6 * MiB, type: 'video/quicktime' }); const k2 = r.j.k, t2 = r.j.t;
r = await PUT('?k=' + encodeURIComponent(k2) + '&t=AAAAAAAAAAAAAAAA&n=1', body(10)); t(r.s === 404, 'parte con código malo');
r = await PUT('?k=' + encodeURIComponent(k2) + '&t=' + t2 + '&n=2', body(10)); t(r.s === 400, 'parte de más');
r = await PUT('?k=' + encodeURIComponent(k2) + '&t=' + t2 + '&n=1', body(8 * MiB + 1)); t(r.s === 413, 'parte demasiado grande');
r = await P('jobv', { a: 'done', k: k2, t: t2, parts: [] }); t(r.s === 400, 'terminar sin partes no');
r = await P('jobv', { a: 'abort', k: k2, t: t2 }); t(r.s === 200 && !db.prepare('SELECT k FROM tvid WHERE k = ?').get(k2), 'tirar una subida a medias');
// 4. la candidatura con su vídeo
r = await P('job', { job: 'tiendas', consent: true, a: ans() }); t(r.s === 400 && r.j.fields.includes('video'), 'sin vídeo ni enlace: falta el vídeo');
r = await P('job', { job: 'tiendas', consent: true, a: ans(), vk: up1.k + '|BBBBBBBBBBBBBBBB' }); t(r.s === 400 && r.j.fields.includes('video'), 'con un código de vídeo falso: falta el vídeo');
r = await P('job', { job: 'setter', consent: true, a: ans({ ko1: 'si', q1: 'Vendí por WhatsApp a tiendas de moda durante dos años, con seguimiento diario.', q2: 'Primero escucho y luego ofrezco ver su tienda.', q3: 'Constancia y buen tono.' }), vk: up1.j.vk }); t(r.s === 400 && r.j.fields.includes('video'), 'el vídeo de un puesto no vale para otro');
r = await P('job', { job: 'tiendas', consent: true, a: ans(), vk: up1.j.vk }); t(r.s === 200, 'candidatura con su vídeo: ' + JSON.stringify(r.j));
const id = r.j.id, c = db.prepare('SELECT * FROM tcand WHERE id = ?').get(id), d = JSON.parse(c.data);
t(d.vid && d.vid.k === up1.k && d.vid.size === 20 * MiB && d.vid.src === 'rec', 'la candidatura guarda su vídeo');
t(db.prepare('SELECT cid FROM tvid WHERE k = ?').get(up1.k).cid === id, 'tvid apunta a la candidatura');
await new Promise((s) => setTimeout(s, 30));
t(fetch.last && /ha grabado o subido su vídeo de presentación, que no ves/.test(fetch.last.messages[0].content), 'la IA sabe que hay vídeo (no lo ve)');
ip = '2.2.2.3'; r = await P('job', { job: 'tiendas', consent: true, a: ans({ email: 'otra@example.com' }), vk: up1.j.vk }); t(r.s === 400 && r.j.fields.includes('video'), 'el mismo vídeo no vale dos veces');
r = await P('jobv', { a: 'abort', k: up1.k, t: up1.tok }); t(r.s === 404 && env.TV.objs.has(up1.k), 'un vídeo ya enviado no se puede tirar desde fuera');
// 5. en el admin: la lista dice que hay vídeo; se ve con rangos y se descarga
let ar = await A('GET', 'tal'); let aj = await ar.json(); t(aj.cands.find((x) => x.id === id).vid === 1, 'lista: vid = 1');
ar = await A('GET', 'tal/' + id + '/video'); t(ar.status === 200 && ar.headers.get('accept-ranges') === 'bytes' && ar.headers.get('content-type') === 'video/mp4' && (await ar.arrayBuffer()).byteLength === 20 * MiB, 'vídeo entero');
ar = await A('GET', 'tal/' + id + '/video', { range: 'bytes=0-1' }); t(ar.status === 206 && ar.headers.get('content-range') === 'bytes 0-1/' + 20 * MiB && (await ar.arrayBuffer()).byteLength === 2, 'rango 0-1 (Safari)');
ar = await A('GET', 'tal/' + id + '/video', { range: 'bytes=' + (8 * MiB - 1) + '-' + (8 * MiB) }); const two = new Uint8Array(await ar.arrayBuffer()); t(ar.status === 206 && two[0] === 1 && two[1] === 2, 'rango entre dos partes');
ar = await A('GET', 'tal/' + id + '/video', { range: 'bytes=-10' }); t(ar.status === 206 && (await ar.arrayBuffer()).byteLength === 10, 'los últimos 10 bytes');
ar = await A('GET', 'tal/' + id + '/video', { range: 'bytes=' + 30 * MiB + '-' }); t(ar.status === 416, 'rango fuera: 416');
ar = await A('GET', 'tal/' + id + '/video', {}, '?dl=1'); t(/attachment/.test(ar.headers.get('content-disposition') || '') && /\.mp4/.test(decodeURIComponent(ar.headers.get('content-disposition'))), 'descargar');
// 6. una subida a la galería (quicktime) que nunca se envía se borra al día siguiente; borrar la candidatura borra su vídeo
ip = '2.2.2.4'; const up3 = await upload(3 * MiB, 'tiendas', 'video/quicktime'); t(up3.s === 200 && env.TV.objs.get(up3.k).type === 'video/quicktime', 'vídeo .mov de una sola parte');
db.prepare('UPDATE tvid SET ts = ? WHERE k = ?').run(Date.now() - 2 * 86400000, up3.k);
await A('GET', 'tal'); t(!env.TV.objs.has(up3.k) && !db.prepare('SELECT k FROM tvid WHERE k = ?').get(up3.k), 'la subida que nadie envió se borra');
ar = await A('DELETE', 'tal/' + id); t(ar.status === 200 && !env.TV.objs.has(up1.k) && !db.prepare('SELECT k FROM tvid WHERE k = ?').get(up1.k), 'borrar la candidatura borra su vídeo');
// 7. límite de subidas por conexión
ip = '9.9.9.9'; let last; for (let i = 0; i < 13; i++) last = await P('jobv', { a: 'start', job: 'tiendas', size: 3 * MiB, type: 'video/mp4' }); t(last.s === 429, '13 subidas en un día desde la misma conexión: 429');
// 8. la candidatura abierta no lo exige
ip = '3.3.3.3'; r = await P('job', { job: 'abierta', consent: true, a: ans({ email: 'abierta@example.com', area: 'Diseño', q1: 'Diseño de tiendas y marcas desde hace años.', q2: 'Ordenar las plantillas y el método.' }) }); t(r.s === 200, 'abierta sin vídeo: ' + JSON.stringify(r.j));
console.log(ok + ' bien, ' + ko + ' mal'); process.exit(ko ? 1 : 0);
