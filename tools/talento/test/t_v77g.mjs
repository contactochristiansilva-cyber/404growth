// Prueba de la v77g: posts «solo LinkedIn» (las 3 ofertas de empleo) en LinkedIn y blog del admin.
// Antes: cp <worker v77g> w77gmod.mjs && echo "export { socialApi, DDL, LIJOB };" >> w77gmod.mjs
import { makeD1 } from './d1shim.mjs';
const LI = [];
globalThis.fetch = async (url, o) => {
  const u = String(url);
  if (u === 'https://api.linkedin.com/rest/posts') { LI.push(JSON.parse(o.body)); return new Response('', { status: 201, headers: { 'x-restli-id': 'urn:li:share:' + (7000 + LI.length) } }); }
  throw new Error('fetch inesperado: ' + u);
};
const { socialApi, DDL, LIJOB } = await import('./w77gmod.mjs');
const env = { DB: makeD1() }; for (const s of DDL) env.DB._db.exec(s);
const db = env.DB._db;
const meta = (k, v) => db.prepare("INSERT INTO meta (k, v) VALUES (?, ?) ON CONFLICT(k) DO UPDATE SET v = excluded.v").run(k, v);
meta('li_tok', JSON.stringify({ t: 'tok', sub: 'abc', name: 'Christian', exp: Date.now() + 30 * 864e5 }));
let ok = 0, ko = 0; const t = (c, m) => { if (c) ok++; else { ko++; console.log('FALLO:', m); } };
const S = async (m, p, b) => { const r = await socialApi(new Request('https://404growth.com/admin/api/social/' + p, { method: m, headers: { 'content-type': 'application/json' }, body: b ? JSON.stringify(b) : undefined }), env, p); return { s: r.status, j: await r.json() }; };

// 1. al abrir LinkedIn y blog entran las 3 ofertas como borradores «solo LinkedIn», una sola vez
let r = await S('GET', 'li'); let dr = r.j.posts.filter((p) => p.status === 'draft' && p.auto === 2);
t(r.s === 200 && dr.length === 3, 'entran 3 borradores solo LinkedIn: ' + dr.length);
t(dr.every((p) => /^Oferta de empleo:/.test(p.li) && !p.body && p.li.includes('utm_medium=post')), 'empiezan por «Oferta de empleo:» y llevan su enlace');
t(dr.map((p) => p.slug).join() === 'empleo-tiendas-shopify,empleo-setter,empleo-growth', 'en orden: tiendas, setter, growth');
db.prepare("DELETE FROM lpost WHERE slug = 'empleo-growth'").run();
r = await S('GET', 'li'); t(r.j.posts.filter((p) => p.auto === 2).length === 2, 'no vuelven a entrar (ni el que se borra a mano)');
// 2. guardar los cambios de Chris
r = await S('POST', 'li/save', { slug: 'empleo-setter', title: 'Oferta de empleo · Setter', li: 'Oferta de empleo: busco setter. Texto cambiado por Chris.\n\n#empleo', kw: '', descr: '', body: '' });
t(r.s === 200 && r.j.slug, 'se guarda: ' + JSON.stringify(r.j)); const setSlug = r.j.slug;
// 3. el borrador diario con IA (auto = 1) de hoy no se borra al publicar una oferta
db.prepare("INSERT INTO lpost (slug, title, descr, kw, li, body, status, created, updated, auto) VALUES ('hoy-ia', 'Artículo de hoy', 'd', 'k', 'Post de hoy', 'Cuerpo', 'draft', ?, ?, 1)").run(Date.now(), Date.now());
r = await S('POST', 'li/publish', { slug: setSlug, li: true });
t(r.s === 200 && r.j.lionly && r.j.li === 'https://www.linkedin.com/feed/update/urn:li:share:7001/', 'publicado en LinkedIn: ' + JSON.stringify(r.j));
t(LI.length === 1 && LI[0].commentary.startsWith('Oferta de empleo: busco setter') && !/Visita mi web/.test(LI[0].commentary), 'va tal cual, sin «Visita mi web» delante');
t(/\{hashtag\|\\#\|empleo\}/.test(LI[0].commentary), 'los hashtags salen como hashtags');
const row = db.prepare('SELECT * FROM lpost WHERE slug = ?').get(setSlug); t(row.status === 'published' && row.li_url && row.auto === 2 && !row.body, 'queda publicado, sin artículo');
t(!!db.prepare("SELECT slug FROM lpost WHERE slug = 'hoy-ia'").get(), 'el borrador de hoy de la IA sigue ahí');
r = await S('POST', 'li/publish', { slug: setSlug, li: true }); t(r.s === 200 && LI.length === 1, 'pulsar otra vez no lo publica dos veces');
r = await S('POST', 'li/publish', { slug: 'empleo-tiendas-shopify', li: false }); t(r.s === 400 && r.j.error === 'nopost', 'sin LinkedIn no se publica (no hay blog)');
// 4. el blog y sus métricas no lo ven
t(db.prepare("SELECT COUNT(*) AS n FROM lpost WHERE status = 'published' AND auto != 2").get().n === 0, 'el blog no tiene la oferta');
// 5. un post normal sigue igual: con «Visita mi web» y su artículo
r = await S('POST', 'li/publish', { slug: 'hoy-ia', li: true });
t(r.s === 200 && !r.j.lionly && LI[1].commentary.startsWith('Visita mi web'), 'el post normal lleva «Visita mi web» y va al blog');
console.log(ok + ' bien, ' + ko + ' mal'); process.exit(ko ? 1 : 0);
