// End to end (27 oct 2026): a real proposal from the live site (Brisa, with the counter v3 added by counter3.py) in Chromium as an iPhone
// on 404growth.com → the visits Worker v3 (Node, D1 = SQLite, starting from the live v2 table) → the admin v30 (Node, same database):
// context, active time, sections, events, the entry notice, contact and download alerts, the score, a second device from another network
// (possible extra reader), robots apart, the API (ranking, feed, alerts, settings, correction, export, deletion) and the admin pages.
import { chromium } from '/home/claude/.npm-global/lib/node_modules/playwright/index.mjs';
import { DatabaseSync } from 'node:sqlite';
import fs from 'fs';
import path from 'path';
import nc from 'crypto';
let ok = 0, bad = 0; const t = (c, m) => { if (c) ok++; else { bad++; console.log('FAIL', m) } };
function d1(db) {
  const stmt = (sql, args = []) => ({ bind: (...a) => stmt(sql, a),
    first: async (col) => { const r = db.prepare(sql).get(...args); return r === undefined ? null : col ? r[col] : { ...r } },
    all: async () => ({ results: db.prepare(sql).all(...args).map((r) => ({ ...r })) }),
    run: async () => { const r = db.prepare(sql).run(...args); return { meta: { changes: Number(r.changes) } } } });
  return { prepare: (sql) => stmt(sql), batch: async (l) => { for (const s of l) await s.run() } };
}
const A = new DatabaseSync(':memory:'), V = new DatabaseSync(':memory:');
// the visits tables exactly as they are live today (v2), with an old visit of another proposal
V.exec("CREATE TABLE v (id INTEGER PRIMARY KEY AUTOINCREMENT, k TEXT NOT NULL, slug TEXT NOT NULL, ts INTEGER NOT NULL, vid TEXT NOT NULL, cc TEXT, dev TEXT, secs INTEGER NOT NULL DEFAULT 0, depth INTEGER NOT NULL DEFAULT 0, seen INTEGER, ex INTEGER)");
V.exec("CREATE TABLE c (id INTEGER PRIMARY KEY AUTOINCREMENT, k TEXT NOT NULL, ts INTEGER NOT NULL, t INTEGER NOT NULL DEFAULT 0, s TEXT, sh TEXT, w TEXT, h TEXT, x INTEGER, y INTEGER)");
V.prepare("INSERT INTO v (k, slug, ts, vid, cc, dev, secs, depth, seen, ex) VALUES ('aaaaaaaaaaaaaaaaaaaa', 'circe', ?, 'old', 'ES', 'm', 40, 3, ?, 1)").run(Date.now() - 2 * 864e5, Date.now() - 2 * 864e5 + 40e3);
const VW = (await import('/home/claude/vis/worker.v3.js')).default, AW = (await import('./worker.v30.js')).default;
const venv = { DB: d1(V) }, aenv = { DB: d1(A), VIS: d1(V), KIT_KEY: 'k-test' };
const SITE = '/tmp/claude-0/site3';
const R = {}; for (const l of fs.readFileSync(SITE + '/_redirects', 'utf8').split('\n')) { const p = l.trim().split(/\s+/); if (p.length === 3 && !p[0].includes('*')) R[p[0]] = p[1] }
const file = (pn) => { let q = R[pn] || pn; let f = path.join(SITE, q.replace(/^\//, '')); if (!fs.existsSync(f) && fs.existsSync(f + '.html')) f += '.html'; return fs.existsSync(f) && fs.statSync(f).isFile() ? f : null };
const MIME = { '.html': 'text/html', '.webp': 'image/webp', '.jpg': 'image/jpeg', '.png': 'image/png', '.woff2': 'font/woff2', '.svg': 'image/svg+xml', '.mp4': 'video/mp4' };
const realFetch = globalThis.fetch; const pushed = [];
globalThis.fetch = async (u, init) => { if (String(u).startsWith('https://web.push.apple.com')) { pushed.push(init); return new Response('', { status: 201 }) } return realFetch(u, init) };
const ago = (p, o = {}) => AW.fetch(new Request('https://404growth.com' + p, o), aenv, { waitUntil() {} });
await ago('/admin/api/push/key', { headers: { cookie: '__Host-s404=' + 'y'.repeat(30) } });
const tok = 'tok_' + 'x'.repeat(40), sha = (s) => nc.createHash('sha256').update(s).digest('base64url');
A.prepare("INSERT INTO users (id, email, role, salt, hash, iter, created) VALUES ('u1', 'c@x', 'admin', 's', 'h', 1, 1)").run();
A.prepare("INSERT INTO sessions (h, uid, created, expires) VALUES (?, 'u1', 1, ?)").run(sha(tok), Date.now() + 864e5);
const ck = { cookie: '__Host-s404=' + tok };
const dev = nc.createECDH('prime256v1'); dev.generateKeys(); const auth = nc.randomBytes(16);
await ago('/admin/api/push/sub', { method: 'POST', headers: { ...ck, origin: 'https://404growth.com', 'x-404': '1', 'content-type': 'application/json' }, body: JSON.stringify({ endpoint: 'https://web.push.apple.com/QX1', keys: { p256dh: dev.getPublicKey('base64url'), auth: auth.toString('base64url') } }) });
A.prepare("INSERT OR REPLACE INTO docs (coll, id, data, updated) VALUES ('leads', 'tat-brisa', ?, 1)").run(JSON.stringify({ niche: 'tattoo', name: 'Brisa Tattoo', slug: 'brisa-tattoo', pageUrl: 'https://404growth.com/p/brisa/', stage: 'contacted' }));
const tick = async () => { const ps = []; await AW.scheduled({}, aenv, { waitUntil: (p) => ps.push(p) }); await Promise.all(ps) };
const ece = (await import('http_ece')).default;
const note = (m) => JSON.parse(ece.decrypt(Buffer.from(new Uint8Array(m.body)), { version: 'aes128gcm', privateKey: dev, authSecret: auth }).toString());
await tick();   // the watchers' first run: they note where the counter is
const api = async (p) => (await ago('/admin/api/' + p, { headers: ck })).json();
const post = async (p, b) => ago('/admin/api/' + p, { method: 'POST', headers: { ...ck, origin: 'https://404growth.com', 'x-404': '1', 'content-type': 'application/json' }, body: JSON.stringify(b) });

const b = await chromium.launch();
const IPHONE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.6 Mobile/15E148 Safari/604.1';
const MAC = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36';
const hits = [];
async function visit(o) {
  const ctx = await b.newContext(Object.assign({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true, userAgent: IPHONE, locale: 'es-ES', timezoneId: 'Europe/Madrid', colorScheme: 'dark' }, o.ctx || {}));
  await ctx.addInitScript(() => Object.defineProperty(Navigator.prototype, 'webdriver', { get: () => false }));
  if (o.cookie) await ctx.addCookies([{ name: '__Host-s404', value: tok, domain: '404growth.com', path: '/', secure: true, httpOnly: true }]);
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', (e) => errs.push(e.message)); p.on('console', (m) => { if (m.type() === 'error' && !/Failed to load resource|error occurred when fetching the script/.test(m.text())) errs.push('console ' + m.text()) });
  await p.route('**/*', async (r) => {
    const u = new URL(r.request().url()), req = r.request(), meth = req.method();
    if (u.host === '404growth-visits.contactochristiansilva.workers.dev') {
      hits.push(u.pathname + ' ' + (req.postData() || ''));
      const rq = new Request(u.href, { method: meth, body: meth === 'POST' ? req.postData() : undefined, headers: { origin: 'https://404growth.com', 'user-agent': req.headers()['user-agent'], 'cf-connecting-ip': o.ip } });
      Object.defineProperty(rq, 'cf', { value: o.cf });
      const res = await VW.fetch(rq, venv);
      return r.fulfill({ status: res.status, headers: { 'access-control-allow-origin': 'https://404growth.com', 'content-type': 'application/json' }, body: await res.text() });
    }
    if (u.host === '404growth.com' && u.pathname.startsWith('/admin')) {
      const res = await AW.fetch(new Request(u.href, { method: meth, body: meth === 'POST' ? req.postData() : undefined, headers: req.headers() }), aenv, { waitUntil() {} });
      return r.fulfill({ status: res.status, headers: Object.fromEntries(res.headers), body: Buffer.from(await res.arrayBuffer()) });
    }
    if (u.host === '404growth.com') { const f = file(decodeURIComponent(u.pathname)); return f ? r.fulfill({ status: 200, contentType: MIME[path.extname(f)] || 'application/octet-stream', body: fs.readFileSync(f) }) : r.fulfill({ status: 404, body: '' }) }
    if (/fonts\.(googleapis|gstatic)\.com/.test(u.host)) return r.fulfill({ status: 200, body: '' });
    return r.abort();
  });
  return { ctx, p, errs };
}
const MADRID = { country: 'ES', region: 'Madrid', city: 'Madrid', asn: 3352, asOrganization: 'Telefonica de Espana' };
const BCN = { country: 'ES', region: 'Catalonia', city: 'Barcelona', asn: 12430, asOrganization: 'Vodafone Spain' };
const slow = async (p, n) => { for (let i = 0; i < n; i++) { await p.mouse.wheel(0, 380); await p.waitForTimeout(230) } };

// 1 · she opens her proposal on the iPhone and reads it
let { ctx, p, errs } = await visit({ ip: '81.0.0.1', cf: MADRID });
await p.goto('https://404growth.com/p/brisa/'); await p.waitForTimeout(3500);
let row = V.prepare("SELECT * FROM v WHERE slug = 'brisa'").get();
t(row && row.cv === 3 && row.br === 'Safari 18' && row.os === 'iOS 18.6' && row.dv === 'm', 'entry with the device ' + JSON.stringify(row && [row.br, row.os, row.dv]));
t(row.scr.startsWith('390×844') && row.lang === 'es-ES' && row.tz === 'Europe/Madrid' && row.dk === 1 && row.ci === 'Madrid' && row.aso === 'Telefonica de Espana' && row.ipv === 4, 'context: screen, language, zone, dark, city, network ' + row.scr);
t(!JSON.stringify(row).includes('81.0.0.1'), 'the IP is not kept');
await tick(); let n = pushed.map(note);
t(n.length === 1 && n[0].title === 'Brisa Tattoo' && n[0].body.includes('primera vez') && n[0].url === '/admin/crm#visita=' + row.id, 'notice of the entry ' + JSON.stringify(n[0]));
pushed.length = 0;
await slow(p, 14);   // she scrolls down through the parts
await p.evaluate(() => document.getElementById('incluye').scrollIntoView()); for (let i = 0; i < 18; i++) { await p.mouse.move(100 + i, 300); await p.waitForTimeout(1000) }   // she stays on «lo que incluye»
const sum = await p.$('details summary'); if (sum) { await sum.scrollIntoViewIfNeeded(); await sum.click(); await p.waitForTimeout(300) }
await p.evaluate(() => { const r = document.createRange(); r.selectNodeContents(document.querySelector('h1,h2')); getSelection().removeAllRanges(); getSelection().addRange(r); document.execCommand('copy') });
// a document link and a video (the live proposal has neither: added here only to test the counter)
await p.evaluate(() => { const s = document.getElementById('incluye'); const a = document.createElement('a'); a.href = '/docs/Propuesta%20Brisa.pdf'; a.textContent = 'Descargar PDF'; a.id = 'tpdf'; a.addEventListener('click', (e) => e.preventDefault()); s.appendChild(a);
  const v = document.createElement('video'); v.title = 'Reel de ejemplo'; s.appendChild(v); v.dispatchEvent(new Event('play')); setTimeout(() => v.dispatchEvent(new Event('pause')), 1500) });
await p.click('#tpdf'); await p.waitForTimeout(1600);
await p.evaluate(() => { document.querySelectorAll('a[href*="wa.me"]').forEach((a) => a.addEventListener('click', (e) => e.preventDefault())) });
const wa = p.locator('a[href*="wa.me"]:visible').last(); await wa.scrollIntoViewIfNeeded(); await wa.click(); await p.waitForTimeout(6000);
// she leaves
await p.goto('https://404growth.com/zzz-otra'); await new Promise((r) => setTimeout(r, 2500));
t(!errs.length, 'page errors ' + errs);
await ctx.close();
row = V.prepare("SELECT * FROM v WHERE id = ?").get(row.id);
const E = V.prepare("SELECT y, s, l, n, m FROM e WHERE k = ? ORDER BY id").all(row.k), ys = new Set(E.map((e) => e.y));
t(row.act >= 8 && row.act <= row.secs + 2 && row.sd >= 90 && row.ex === 1, 'active time, scroll, left ' + JSON.stringify({ act: row.act, secs: row.secs, sd: row.sd }));
const ss = JSON.parse(row.ss || '{}'); t(ss.incluye >= 4 && Object.keys(ss).length >= 4, 'seconds per part ' + row.ss);
for (const y of ['open', 'sin', 'scr', 'exp', 'copy', 'dl', 'vplay', 'vpause', 'end', 'nav']) t(ys.has(y), 'event ' + y);
t(E.filter((e) => e.y === 'scr').map((e) => e.n).join() === '25,50,75,90,100', 'scroll milestones once each');
t(JSON.parse(E.find((e) => e.y === 'dl').m).file === 'Propuesta Brisa.pdf', 'the document asked for');
t(!E.some((e) => /Tattoo M|Hola Christian/.test(e.m || '')) && JSON.parse(E.find((e) => e.y === 'copy').m).len > 0, 'copy keeps only the length');
t(E.filter((e) => e.y === 'sin').length >= 4 && E.find((e) => e.y === 'sin' && e.s === 'incluye'), 'sections seen in order');
const ids = V.prepare("SELECT COUNT(*) n, COUNT(DISTINCT i) d FROM e WHERE k = ?").get(row.k); t(ids.n === ids.d, 'no duplicated events');
// 2 · the admin: contact and download alerts, the score, the visit page data
await tick(); n = pushed.map(note);
t(n.some((x) => /WhatsApp/.test(x.body) && x.url === '/admin/crm#visita=' + row.id), 'notice: she tapped WhatsApp ' + JSON.stringify(n.map((x) => x.body)));
t(n.some((x) => /descargado «Propuesta Brisa\.pdf»/.test(x.body)), 'notice: the download');
const before = pushed.length; await tick(); t(pushed.length === before, 'no repeated notices');
let j = await api('visit/' + row.id);
t(j.visit.events.length >= 10 && j.visit.br === 'Safari 18' && j.visit.ss.incluye >= 4 && j.visit.tc === 'human_likely', 'the visit page gets everything');
t(j.intel && j.intel.score >= 20 && j.intel.factors.some((f) => f.k === 'contact') && j.intel.factors.some((f) => f.k === 'price') && j.intel.conf !== 'sin datos', 'score with its factors ' + JSON.stringify(j.intel && [j.intel.score, j.intel.conf, j.intel.factors.map((f) => f.k + f.pts)]));
t(j.intel.readers.length === 1 && j.intel.readers[0].level === 'principal', 'one device');
// 3 · later, a computer from another network opens it: possible extra reader, said with care
V.prepare('UPDATE v SET seen = seen - 7200000, ts = ts - 7200000 WHERE id = ?').run(row.id);
pushed.length = 0;
({ ctx, p, errs } = await visit({ ip: '90.0.0.9', cf: BCN, ctx: { viewport: { width: 1440, height: 900 }, isMobile: false, hasTouch: false, userAgent: MAC, colorScheme: 'light' } }));
await p.goto('https://404growth.com/p/brisa/'); await p.waitForTimeout(3500); await slow(p, 12); await p.waitForTimeout(4000); await p.goto('https://404growth.com/zzz-otra'); await p.waitForTimeout(800);
const row2 = V.prepare("SELECT * FROM v WHERE slug = 'brisa' ORDER BY id DESC").get();
t(row2.id !== row.id && row2.br === 'Chrome 141' && row2.os === 'macOS 10.15' && row2.dv === 'd' && row2.ci === 'Barcelona', 'second device ' + JSON.stringify([row2.br, row2.os, row2.dv]));
await tick(); n = pushed.map(note);
t(n.some((x) => x.body.includes('2.ª vez')) && n.some((x) => /Posible lector adicional/.test(x.body) && /No es prueba/.test(x.body)), 'notices: second entry and possible extra reader ' + JSON.stringify(n.map((x) => x.body)));
await ctx.close();
j = await api('visits/intel/brisa');
t(j.readers.length === 2 && j.readers[1].level === 'posible' && j.returns === 1 && j.factors.some((f) => f.k === 'ret') && j.factors.some((f) => f.k === 'reader') && j.outcome.name === 'Brisa Tattoo', 'two devices, a return ' + JSON.stringify(j.readers.map((r) => r.level)));
// 4 · robots: a WhatsApp preview and a mail scanner never become visits
for (const ua of ['WhatsApp/2.24.1 A', 'Mozilla/5.0 (compatible; Barracuda Sentinel)']) { const rq = new Request('https://x/h', { method: 'POST', body: JSON.stringify({ s: 'brisa' }), headers: { origin: 'https://404growth.com', 'user-agent': ua, 'cf-connecting-ip': '3.3.3.3' } }); Object.defineProperty(rq, 'cf', { value: { country: 'US' } }); await VW.fetch(rq, venv) }
t(V.prepare("SELECT COUNT(*) n FROM v WHERE slug = 'brisa'").get().n === 2 && V.prepare("SELECT COUNT(*) n FROM b").get().n === 2, 'robots apart');
let rb = await api('visits/robots'); t(rb.raw.length === 2, 'robots listed apart');
// 5 · the rest of the API
const rk = await api('visits/intel'); t(rk.list.length >= 2 && rk.list[0].slug === 'brisa' && rk.list[0].score > rk.list.find((x) => x.slug === 'circe').score, 'ranking by interest');
const fd = await api('visits/feed'); t(fd.items.length >= 10 && fd.items.some((x) => x.y === 'dl') && fd.items.some((x) => x.t === 'c' && x.kind === 'contact') && fd.items[0].name === 'Brisa Tattoo', 'feed of actions');
const al = await api('visits/alerts'); t(al.alerts.some((a) => a.kind === 'contact') && al.alerts.some((a) => a.kind === 'reader') && al.alerts.some((a) => a.kind === 'entry') && al.unseen > 0, 'alerts list ' + al.alerts.map((a) => a.kind));
let r = await post('visits/alerts/seen', {}); t((await api('visits/alerts')).unseen === 0, 'alerts seen');
let cf = await api('visits/cfg'); t(cf.alerts.entry === 1 && cf.weights.contact === 15, 'settings');
r = await post('visits/cfg', { alerts: { entry: 0, highAt: 999 }, weights: { contact: 30 } }); cf = await r.json(); t(cf.alerts.entry === 0 && cf.alerts.highAt === 100 && cf.weights.contact === 30, 'settings saved and clamped ' + JSON.stringify(cf.alerts));
r = await post('visits/cfg', { weights: { contact: 'x' } }); t(r.status === 400, 'bad weights refused');
r = await ago('/admin/api/visits/cfg', { method: 'POST', headers: { ...ck, origin: 'https://evil.com', 'x-404': '1', 'content-type': 'application/json' }, body: '{"alerts":{"entry":1}}' }); t(r.status === 403, 'settings only from the admin');
r = await ago('/admin/api/visits/intel', {}); t(r.status === 401 || r.status === 302, 'no session, no data ' + r.status);
r = await post('visit/' + row2.id + '/class', { tc: 'automation_likely' }); t(r.status === 200 && V.prepare("SELECT tcm FROM v WHERE id = ?").get(row2.id).tcm === 'automation_likely', 'classification corrected by hand');
j = await api('visits/intel/brisa'); t(j.readers.length === 1 && j.robots === 1, 'the corrected one leaves the score');
r = await post('visit/' + row2.id + '/class', { tc: 'hacker' }); t(r.status === 400, 'only known classes');
r = await ago('/admin/api/visits/export/brisa', { headers: ck }); const ex = await r.json();
t(r.headers.get('content-disposition').includes('visitas-brisa.json') && ex.visits.length === 2 && ex.events.length >= 10 && !JSON.stringify(ex).includes('"vid"'), 'export');
// with entry notices off, a new entry is listed but not pushed
pushed.length = 0;
// 6 · the admin pages: the visit, the tab with its four views, on an iPhone and a computer
for (const [W, H, mob] of [[390, 844, true], [1280, 900, false]]) {
  ({ ctx, p, errs } = await visit({ ip: '1.1.1.1', cf: MADRID, cookie: true, ctx: { viewport: { width: W, height: H }, isMobile: mob, hasTouch: mob, userAgent: mob ? IPHONE : MAC, colorScheme: 'light' } }));
  await p.addInitScript(() => { try { localStorage.setItem('crm404-niche', 'tattoo') } catch (e) {} });
  await p.goto('https://404growth.com/admin/crm#visita=' + row.id); await p.waitForTimeout(2500);
  const txt = await p.$eval('#vp-b', (e) => e.innerText);
  t(/Interés en la propuesta/.test(txt) && /Lectura/.test(txt) && /Lo que ha hecho/.test(txt) && /Dispositivo y red/.test(txt) && /Tipo de tráfico/.test(txt) && /Posible lector adicional|Principal/.test(txt), W + ' visit page sections');
  t(/Pide descargar «Propuesta Brisa\.pdf»/.test(txt) && /Pulsa «/.test(txt) && /Barcelona|Madrid/.test(txt), W + ' timeline and place');
  await p.screenshot({ path: '/tmp/claude-0/v30-visit-' + W + '.png', fullPage: false });
  await p.$eval('#vp .pn', (e) => e.scrollTop = 900); await p.waitForTimeout(200); await p.screenshot({ path: '/tmp/claude-0/v30-visit2-' + W + '.png' });
  const ow = await p.$eval('#vp .pn', (e) => e.scrollWidth - e.clientWidth); t(ow <= 0, W + ' no sideways scroll in the visit ' + ow);
  await p.keyboard.press('Escape'); await p.waitForTimeout(300);
  await p.click('#tabs [data-view="vis"]'); await p.waitForTimeout(1500);
  t(await p.$('.vseg') !== null, W + ' segmented views');
  await p.screenshot({ path: '/tmp/claude-0/v30-list-' + W + '.png' });
  for (const m of ['props', 'feed', 'alerts']) { await p.click('[data-vm="' + m + '"]'); await p.waitForTimeout(1500); await p.screenshot({ path: '/tmp/claude-0/v30-' + m + '-' + W + '.png', fullPage: m === 'alerts' }); }
  const at = await p.$eval('#vis-body', (e) => e.innerText); t(/Qué te llega al móvil/.test(at) && /Tráfico automático/.test(at), W + ' alerts view with settings');
  await p.click('[data-vm="props"]'); await p.waitForTimeout(1200); const pt = await p.$eval('#vis-body', (e) => e.innerText); t(/Brisa Tattoo/.test(pt), W + ' ranking shown');
  const ow2 = await p.evaluate(() => document.documentElement.scrollWidth - innerWidth); t(ow2 <= 0, W + ' no sideways scroll ' + ow2);
  t(!errs.length, W + ' admin errors ' + errs);
  await ctx.close();
}
// 7 · deletion of one proposal's data (a request to delete): needs the slug typed
r = await post('visits/delete/brisa', { confirm: 'otra' }); t(r.status === 400, 'deletion needs confirmation');
r = await post('visits/delete/brisa', { confirm: 'brisa' }); j = await r.json();
t(j.ok && j.visits === 2 && V.prepare("SELECT COUNT(*) n FROM v WHERE slug LIKE 'brisa%'").get().n === 0 && V.prepare("SELECT COUNT(*) n FROM e").get().n === 0 && A.prepare("SELECT COUNT(*) n FROM adminlog WHERE what = 'delete'").get().n === 1, 'deleted and logged');
await b.close();
console.log('counter calls:', [...new Set(hits.map((h) => h.split(' ')[0]))].join(' '));
console.log(`${ok} ok, ${bad} failed`);
