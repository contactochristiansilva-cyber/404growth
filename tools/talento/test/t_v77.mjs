// Prueba de la v77 (Talento). Antes: cp <worker v77> w77mod.mjs && echo "export { talPublic, talApi, talReady, DDL, TAL };" >> w77mod.mjs
import { makeD1 } from './d1shim.mjs';
const AI = { calls: [], mode: 'ok' }, MAIL = [];
globalThis.fetch = async (url, o) => {
  const u = String(url);
  if (u.startsWith('https://api.anthropic.com/')) {
    const b = JSON.parse(o.body); AI.calls.push(b);
    if (AI.mode === 'fail') return new Response(JSON.stringify({ error: { message: 'boom' } }), { status: 500 });
    const ids = b.tools[0].input_schema.properties.scores.items.properties.id.enum;
    return new Response(JSON.stringify({ content: [{ type: 'tool_use', name: 'puntuar', input: { scores: ids.map((id, k) => ({ id, score: k === 0 ? 5 : 3, why: 'porque ' + id })), summary: 'Buen perfil.', strengths: ['a', 'b'], risks: ['c'], rec: 'avanzar', questions: ['¿Qué tal?'] } }] }), { status: 200 });
  }
  if (u.includes('/emails')) { MAIL.push(JSON.parse(o.body)); return new Response('{}', { status: 200 }); }
  throw new Error('fetch inesperado: ' + u);
};
const { talPublic, talApi, DDL, TAL } = await import('./w77mod.mjs');
const env = { DB: makeD1() }; for (const s of DDL) env.DB._db.exec(s);
const db = env.DB._db;
let ok = 0, ko = 0; const t = (c, m) => { if (c) ok++; else { ko++; console.log('FALLO:', m); } };
const meta = (k, v) => db.prepare("INSERT INTO meta (k, v) VALUES (?, ?) ON CONFLICT(k) DO UPDATE SET v = excluded.v").run(k, v);
let ip = '1.1.1.1';
const P = async (p, b, o) => { o = o || {}; const h = { 'content-type': 'application/json', 'cf-connecting-ip': ip }; if (!o.noorigin) h.origin = 'https://404growth.com';
  const r = await talPublic(new Request('https://404growth.com/l/' + p + (o.qs || ''), { method: o.m || 'POST', headers: o.raw ? Object.assign(h, { 'content-type': 'application/pdf' }) : h, body: o.raw ? o.raw : (o.m === 'GET' ? undefined : JSON.stringify(b)) }), env, {}, p);
  return { s: r.status, j: await r.json() }; };
const A = async (m, p, b) => { const r = await talApi(new Request('https://404growth.com/admin/api/' + p, { method: m, headers: { 'content-type': 'application/json' }, body: b ? JSON.stringify(b) : undefined }), env, p, {}); const ct = r.headers.get('content-type') || ''; return { s: r.status, j: ct.includes('json') ? await r.json() : null, r }; };
const ans = (x) => Object.assign({ name: 'Lucía Prueba Gómez', email: 'lucia@example.com', phone: '612 345 678', city: 'Málaga, España', linkedin: 'linkedin.com/in/lucia-prueba-gomez', portfolio: 'https://lucia.example.com', video: 'https://youtu.be/lucia60s', hours: 'De 20 a 30 h', start: 'Ya', rate: '600 € por tienda', tz: 'si', lang: 'si', src: 'LinkedIn', ko1: 'si', q1: 'Monté tres tiendas Shopify de moda y joyería, con el tema Dawn personalizado.', q2: 'Primero ordeno el catálogo y rehago las fotos con IA, luego portada y fichas.', q3: 'Nano Banana y GPT Image para fotos; Claude para textos y fichas.' }, x || {});
meta('soc_cfg', JSON.stringify({ aiKey: 'k' }));

// 1. puestos abiertos
let r = await P('jobs', null, { m: 'GET' }); t(r.s === 200 && r.j.open.tiendas === true && r.j.open.setter === true && Object.keys(r.j.open).length === 4, 'jobs: los 4 abiertos');
// 2. origen
r = await P('job', { job: 'tiendas', consent: true, a: ans() }, { noorigin: true }); t(r.s === 403, 'sin origen no entra');
// 3. campos
r = await P('job', { job: 'tiendas', consent: true, a: ans({ email: 'mal', q2: 'corta', portfolio: '', video: '' }) }); t(r.s === 400 && r.j.fields.includes('email') && r.j.fields.includes('q2') && r.j.fields.includes('portfolio') && r.j.fields.includes('video'), 'campos mal (también sin vídeo): ' + JSON.stringify(r.j));
r = await P('job', { job: 'tiendas', consent: false, a: ans() }); t(r.s === 400 && r.j.error === 'consent', 'sin consentimiento no entra');
r = await P('job', { job: 'nada', consent: true, a: ans() }); t(r.s === 404, 'puesto que no existe');
// 4. robots
r = await P('job', { job: 'tiendas', consent: true, web: 'x', a: ans() }); t(r.s === 200 && db.prepare('SELECT COUNT(*) n FROM tcand').get().n === 0, 'el campo oculto no guarda nada');
// 5. una buena
r = await P('job', { job: 'tiendas', consent: true, keep: true, a: ans(), utm: { utm_source: 'linkedin', utm_medium: 'post' } });
t(r.s === 200 && /^T[A-Za-z0-9_-]{12}$/.test(r.j.id) && /^T[A-Za-z0-9_-]{12}\.[A-Za-z0-9_-]{16}$/.test(r.j.cvt), 'candidatura guardada: ' + JSON.stringify(r.j));
const id1 = r.j.id, cvt1 = r.j.cvt;
let row = db.prepare('SELECT * FROM tcand WHERE id = ?').get(id1);
t(row.stage === 'new' && row.phone === '+34612345678' && row.keep === 1 && row.score != null, 'fila: etapa, teléfono con prefijo, permiso y nota');
const ai1 = JSON.parse(row.ai); const W = TAL.jobs[0].rubric; const exp = Math.round(W.reduce((s, x, k) => s + x.w * (k === 0 ? 5 : 3) / 5, 0) * 100 / W.reduce((s, x) => s + x.w, 0));
t(ai1.total === exp && row.score === exp && ai1.rec === 'avanzar' && ai1.scores.length === W.length, 'la nota sale de los pesos de la rúbrica: ' + ai1.total + ' / ' + exp);
const sent = JSON.stringify(AI.calls[0]);
t(!sent.includes('Lucía') && !sent.includes('lucia@') && !sent.includes('612') && !sent.includes('Málaga') && !sent.includes('lucia-prueba'), 'la IA no ve nombre, email, teléfono, ciudad ni LinkedIn');
t(sent.includes('Dawn') && sent.includes('Portfolio y calidad visual') && AI.calls[0].tool_choice.name === 'puntuar', 'la IA ve las respuestas y la rúbrica');
// 6. eliminatorias
r = await P('job', { job: 'setter', consent: true, a: ans({ email: 'b@example.com', tz: 'no', ko1: 'no' }) }); const id2 = r.j.id;
t(JSON.parse(db.prepare('SELECT ko FROM tcand WHERE id = ?').get(id2).ko).join() === 'tz,ko1', 'no cumple: horario y experiencia');
t(JSON.stringify(AI.calls[1]).includes('condiciones eliminatorias'), 'la IA sabe que no cumple');
// 7. repetida
r = await P('job', { job: 'tiendas', consent: true, a: ans() }); t(r.s === 409 && r.j.error === 'dup', 'la misma persona al mismo puesto: repetida');
// 8. límite por IP
for (let k = 0; k < 3; k++) await P('job', { job: 'abierta', consent: true, a: ans({ email: 'x' + k + '@example.com', area: 'Diseño', q1: 'Diseño de tiendas y marcas desde hace años.', q2: 'Ordenar las plantillas y el método de fotos.' }) });
r = await P('job', { job: 'abierta', consent: true, a: ans({ email: 'x9@example.com', area: 'Diseño', q1: 'Diseño de tiendas y marcas desde hace años.', q2: 'Ordenar las plantillas.' }) }); t(r.s === 429, 'más de 5 al día desde la misma conexión: espera');
ip = '2.2.2.2';
// 9. CV
r = await P('jobcv', null, { qs: '?c=' + cvt1, raw: new TextEncoder().encode('hola, no soy un pdf') }); t(r.s === 415, 'el CV tiene que ser PDF');
const pdf = new TextEncoder().encode('%PDF-1.4\n% prueba\n'); r = await P('jobcv', null, { qs: '?c=' + id1 + '.xxxxxxxxxxxxxxxx', raw: pdf }); t(r.s === 404, 'CV con código malo');
r = await P('jobcv', null, { qs: '?c=' + cvt1, raw: pdf }); t(r.s === 200 && db.prepare('SELECT cv FROM tcand WHERE id = ?').get(id1).cv === 1, 'CV guardado');
r = await P('jobcv', null, { qs: '?c=' + cvt1, raw: pdf }); t(r.s === 409, 'el CV solo una vez');
let a = await A('GET', 'tal/' + id1 + '/cv'); const bytes = new Uint8Array(await a.r.arrayBuffer()); t(a.s === 200 && a.r.headers.get('content-type') === 'application/pdf' && bytes[0] === 0x25 && bytes.length === pdf.length, 'el admin abre el CV');
// 10. admin: lista y ficha
a = await A('GET', 'tal'); t(a.s === 200 && a.j.cands.length === 5 && a.j.ai === true && a.j.mail === false && a.j.jobs.length === 4 && a.j.stages.length === 9, 'lista del admin');
const c1 = a.j.cands.find((x) => x.id === id1); t(c1 && c1.score === exp && c1.rec === 'avanzar' && !c1.seen && c1.cv && !('email' in c1), 'tarjeta: nota, sin ver, sin email');
a = await A('GET', 'tal/' + id1); t(a.j.cand.email === 'lucia@example.com' && a.j.cand.ai.total === exp && a.j.cand.links.test.includes('/equipo/prueba/?t=' + id1 + '.') && a.j.qs.length > 10 && a.j.job.rubric.length === 6, 'ficha completa');
t(db.prepare('SELECT seen FROM tcand WHERE id = ?').get(id1).seen === 1, 'abrirla la marca como vista');
// 11. etapas y mensajes (sin clave de email: para WhatsApp)
a = await A('POST', 'tal/' + id1, { stage: 'test' }); row = db.prepare('SELECT * FROM tcand WHERE id = ?').get(id1); const tt = JSON.parse(row.test);
t(a.s === 200 && row.stage === 'test' && tt.sent && tt.due - tt.sent === 2 * 864e5, 'prueba técnica con 48 h de plazo');
t(a.j.msg && a.j.msg.sent === '' && a.j.msg.wa.startsWith('https://wa.me/34612345678?text=') && a.j.msg.text.includes('/equipo/prueba/?t=' + id1 + '.') && a.j.msg.text.startsWith('Hola Lucía,'), 'sin clave de email: el mensaje queda listo para WhatsApp');
a = await A('POST', 'tal/' + id1 + '/msg', { kind: 'test', via: 'wa' }); t(JSON.parse(db.prepare('SELECT msgs FROM tcand WHERE id = ?').get(id1).msgs).some((m) => m.k === 'test' && m.via === 'wa'), 'apuntado como enviado por WhatsApp');
a = await A('POST', 'tal/' + id2, { stage: 'test' }); t(a.s === 200, 'setter a prueba');
let ab = db.prepare("SELECT id FROM tcand WHERE job = 'abierta'").get().id; a = await A('POST', 'tal/' + ab, { stage: 'test' }); t(a.s === 400 && a.j.error === 'notest', 'la candidatura abierta no tiene prueba');
a = await A('POST', 'tal/' + id1, { stage: 'bogus' }); t(a.s === 400, 'etapa que no existe');
// 12. la prueba, en su página
r = await P('jobt', { t: id1 + '.' + 'y'.repeat(16) }); t(r.s === 404, 'prueba con código malo');
const tok1 = cvt1.split('.')[1];
r = await P('jobt', { t: id1 + '.' + tok1 }); t(r.s === 200 && r.j.name === 'Lucía' && r.j.test.title.includes('Olvido') && !r.j.done, 'página de la prueba');
r = await P('jobts', { t: id1 + '.' + tok1, links: ['olvido-prueba.myshopify.com', 'javascript:alert(1)'], text: 'corto' }); t(r.s === 200, 'entrega con un enlace');
row = db.prepare('SELECT * FROM tcand WHERE id = ?').get(id1); const t2 = JSON.parse(row.test);
t(row.stage === 'testd' && t2.sub.links.length === 1 && t2.sub.links[0] === 'https://olvido-prueba.myshopify.com/' && t2.ai && t2.ai.total > 0, 'entregada: etapa, enlaces limpios y nota de la IA');
r = await P('jobts', { t: id1 + '.' + tok1, links: [], text: 'x' }); t(r.s === 400, 'una entrega vacía no vale');
// 13. con clave de email
meta('nl_key', 're_x');
a = await A('POST', 'tal/' + id1, { stage: 'meet' }); t(a.j.msg.sent === 'email' && MAIL.length === 1 && MAIL[0].to[0] === 'lucia@example.com' && MAIL[0].html.includes('/equipo/entrevista/?t=' + id1 + '.'), 'con clave: el email de la entrevista sale solo');
a = await A('POST', 'tal/' + id2, { stage: 'no', send: false }); t(!a.j.msg && MAIL.length === 1, 'sin mandar mensaje si se pide así');
a = await A('POST', 'tal/' + id2 + '/msg', { kind: 'no' }); t(a.j.msg.text.includes('no vamos a seguir adelante') && a.j.msg.sent === '', 'preparar el mensaje de descarte sin enviarlo');
// 14. entrevista
r = await P('jobm', { t: id1 + '.' + tok1 }); t(r.s === 200 ? Array.isArray(r.j.slots) && r.j.dur === 30 : r.s === 503, 'huecos de la entrevista (' + r.s + ')');
r = await P('jobmb', { t: id1 + '.' + tok1, start: '2020-01-01T10:00:00.000Z' }); t(r.s === 409 || r.s === 503, 'una hora que no está libre no se reserva (' + r.s + ')');
r = await P('jobm', { t: ab + '.' + 'z'.repeat(16) }); t(r.s === 404, 'entrevista con código malo');
// 15. abrir y cerrar puestos
a = await A('POST', 'taljob/setter', { open: false }); r = await P('jobs', null, { m: 'GET' }); t(r.j.open.setter === false && r.j.open.tiendas === true, 'cerrar un puesto');
r = await P('job', { job: 'setter', consent: true, a: ans({ email: 'z@example.com' }) }); t(r.s === 409 && r.j.error === 'closed', 'un puesto cerrado no recibe');
// 16. notas, permiso y borrar
a = await A('POST', 'tal/' + id1, { notes: 'Muy buena', keep: false }); row = db.prepare('SELECT * FROM tcand WHERE id = ?').get(id1); t(row.notes === 'Muy buena' && row.keep === 0, 'notas y permiso');
// 17. sin clave de IA
meta('soc_cfg', JSON.stringify({})); ip = '3.3.3.3';
r = await P('job', { job: 'growth', consent: true, a: ans({ email: 'g@example.com' }) }); row = db.prepare('SELECT * FROM tcand WHERE id = ?').get(r.j.id); t(row.score === null && JSON.parse(row.ai).err === 'noai', 'sin clave de IA: llega sin nota');
meta('soc_cfg', JSON.stringify({ aiKey: 'k' })); a = await A('POST', 'tal/' + r.j.id + '/ai', {}); t(a.j.ai.total > 0 && db.prepare('SELECT score FROM tcand WHERE id = ?').get(r.j.id).score > 0, 'volver a puntuar');
// 18. RGPD: se borran solas
const old = Date.now() - 200 * 864e5, older = Date.now() - 400 * 864e5;
db.prepare("UPDATE tcand SET upd = ? WHERE id = ?").run(old, id2);                     // 6 meses y sin permiso: fuera
db.prepare("UPDATE tcand SET upd = ?, keep = 1 WHERE id = ?").run(old, ab);            // con permiso: se queda
db.prepare("UPDATE tcand SET upd = ?, stage = 'hired' WHERE id = ?").run(older, r.j.id);   // del equipo: se queda
db.prepare("UPDATE tcand SET upd = ? WHERE id = ?").run(old, id1);                     // sin permiso, con CV: fuera, y su CV también
a = await A('GET', 'tal'); const left = a.j.cands.map((x) => x.id);
t(!left.includes(id2) && !left.includes(id1) && left.includes(ab) && left.includes(r.j.id), 'limpieza a los 6 meses (12 con permiso; nunca el equipo)');
t(db.prepare('SELECT COUNT(*) n FROM tcvf').get().n === 0, 'el CV se borra con su candidatura');
a = await A('DELETE', 'tal/' + ab); t(a.s === 200 && !db.prepare('SELECT id FROM tcand WHERE id = ?').get(ab), 'borrar a mano');
a = await A('GET', 'tal/' + ab); t(a.s === 404, 'ya no está');
// 19. prueba interna (?interno=1): se puede repetir, sale marcada, no cuenta y la entrevista no crea evento
ip = '4.4.4.4';
let d1 = await P('job', { job: 'tiendas', consent: true, dev: 1, a: ans({ email: 'chris@example.com' }) });
let d2 = await P('job', { job: 'tiendas', consent: true, dev: 1, a: ans({ email: 'chris@example.com' }) });
t(d1.s === 200 && d2.s === 200 && d1.j.dev === true, 'prueba interna: se puede repetir');
a = await A('GET', 'tal'); t(a.j.cands.filter((x) => x.dev).length === 2 && a.j.cands.filter((x) => !x.dev).length >= 1, 'salen marcadas como prueba');
await A('POST', 'tal/' + d1.j.id, { stage: 'meet', send: false });
const dtok = d1.j.cvt.split('.')[1];
r = await P('jobm', { t: d1.j.id + '.' + dtok });
if (r.s === 200 && r.j.slots.length) {
  t(r.j.dev === true, 'la página de la entrevista sabe que es prueba');
  r = await P('jobmb', { t: d1.j.id + '.' + dtok, start: r.j.slots[0] });
  const mt = JSON.parse(db.prepare('SELECT meet FROM tcand WHERE id = ?').get(d1.j.id).meet);
  t(r.s === 200 && r.j.dev === true && mt.dry === 1 && mt.start > 0, 'entrevista de prueba sin evento en Google');
} else t(r.s === 503, 'sin calendario: ' + r.s);
a = await A('DELETE', 'taldev'); a = await A('GET', 'tal'); t(!a.j.cands.some((x) => x.dev) && a.j.cands.length >= 1, 'borrar las pruebas internas deja las de verdad');
console.log(ok + ' bien, ' + ko + ' mal');
process.exit(ko ? 1 : 0);
