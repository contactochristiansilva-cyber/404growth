// the visit counter v3 in Node (D1 = SQLite): a v2 table upgrades itself; everything v2 did still works; context, classification, events
import { DatabaseSync } from 'node:sqlite';
let ok = 0, bad = 0; const t = (c, m) => { if (c) ok++; else { bad++; console.log('FAIL', m) } };
function d1(db) {
  const stmt = (sql, args = []) => ({ bind: (...a) => stmt(sql, a),
    first: async () => { const r = db.prepare(sql).get(...args); return r === undefined ? null : { ...r } },
    all: async () => ({ results: db.prepare(sql).all(...args).map((r) => ({ ...r })) }),
    run: async () => { db.prepare(sql).run(...args); return {} } });
  return { prepare: (sql) => stmt(sql), batch: async (l) => { for (const s of l) await s.run() } };
}
const V = new DatabaseSync(':memory:');
// the live table as it is today (v2), with one old visit and one old click
V.exec("CREATE TABLE v (id INTEGER PRIMARY KEY AUTOINCREMENT, k TEXT NOT NULL, slug TEXT NOT NULL, ts INTEGER NOT NULL, vid TEXT NOT NULL, cc TEXT, dev TEXT, secs INTEGER NOT NULL DEFAULT 0, depth INTEGER NOT NULL DEFAULT 0, seen INTEGER, ex INTEGER)");
V.exec("CREATE TABLE c (id INTEGER PRIMARY KEY AUTOINCREMENT, k TEXT NOT NULL, ts INTEGER NOT NULL, t INTEGER NOT NULL DEFAULT 0, s TEXT, sh TEXT, w TEXT, h TEXT, x INTEGER, y INTEGER)");
V.prepare("INSERT INTO v (k, slug, ts, vid, cc, dev, secs, depth) VALUES ('aaaaaaaaaaaaaaaaaaaa', 'zima', 1, 'old', 'ES', 'm', 30, 2)").run();
const env = { DB: d1(V) };
const W = (await import('./worker.v3.js')).default;
const { parseUA, classify, cleanEvent } = await import('./worker.v3.js');
const UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.6 Mobile/15E148 Safari/604.1';
const CF = { country: 'ES', region: 'Madrid', city: 'Madrid', asn: 3352, asOrganization: 'Telefonica de Espana' };
let now = Date.now(); const realNow = Date.now; Date.now = () => now;
const call = async (p, b, h = {}, cf = CF) => { const req = new Request('https://404growth-visits.x.workers.dev' + p, { method: 'POST', body: JSON.stringify(b), headers: { origin: 'https://404growth.com', 'user-agent': UA, 'cf-connecting-ip': '1.2.3.4', ...h } }); Object.defineProperty(req, 'cf', { value: cf }); const r = await W.fetch(req, env); return { s: r.status, j: await r.json().catch(() => null), h: r.headers } };
const X = { sw: 393, sh: 852, vw: 393, vh: 659, dpr: 3, or: 'p', tch: 5, lang: 'es-ES', tz: 'Europe/Madrid', dk: 1, it: 1, ref: 'mail.google.com', nav: 'navigate' };
let r = await call('/h', { s: 'zima', x: X });
t(r.s === 200 && /^[a-f0-9]{20}$/.test(r.j.k), 'entry gives a key ' + JSON.stringify(r.j));
const k1 = r.j.k;
let row = V.prepare("SELECT * FROM v WHERE k = ?").get(k1);
t(row && row.cv === 3 && row.br === 'Safari 18' && row.os === 'iOS 18.6' && row.dv === 'm' && row.dev === 'm', 'device from the user agent ' + JSON.stringify(row && [row.br, row.os, row.dv]));
t(row.scr === '393×852 · ventana 393×659 · 3x · vertical' && row.lang === 'es-ES' && row.tz === 'Europe/Madrid' && row.dk === 1 && row.tch === 5, 'screen, language, zone ' + row.scr);
t(row.cc === 'ES' && row.rg === 'Madrid' && row.ci === 'Madrid' && row.asn === 3352 && row.aso === 'Telefonica de Espana' && row.ipv === 4 && row.ref === 'mail.google.com', 'network from cf, no IP');
t(!Object.values(row).some((v) => v === '1.2.3.4'), 'the IP is not stored');
t(row.tc === 'human_likely' && row.tcc === 90, 'classified human ' + row.tc + row.tcc + row.tcw);
t(V.prepare("SELECT COUNT(*) n FROM e WHERE k = ? AND y = 'open' AND src = 'server'").get(k1).n === 1, 'server event: opened');
// v2 still works: progress, clicks
now += 20000; await call('/p', { k: k1, t: 20, d: 2, e: 0, a: 14, sd: 46, ss: { 'p-web': 9, reels: 5, 'bad id!': 3, x: 'no' } });
row = V.prepare("SELECT * FROM v WHERE k = ?").get(k1);
t(row.secs === 20 && row.depth === 2 && row.act === 14 && row.sd === 46 && row.ss === '{"p-web":9,"reels":5}', 'progress with active time, scroll and sections ' + row.ss);
await call('/p', { k: k1, t: 25, d: 1, a: 10, sd: 30 }); row = V.prepare("SELECT * FROM v WHERE k = ?").get(k1); t(row.act === 14 && row.sd === 46 && row.depth === 2 && row.ss === '{"p-web":9,"reels":5}', 'never goes down');
await call('/c', { k: k1, c: [{ t: 25, s: 'p-web', sh: 'Vuestra web nueva', w: 'Ver vuestra web nueva', h: '/p/zima/web/', x: 40, y: 51 }] });
t(V.prepare("SELECT COUNT(*) n FROM c WHERE k = ?").get(k1).n === 1, 'clicks');
// events
const ev = [{ i: 'aa11', y: 'sin', t: 3, s: 'reels', l: 'Vuestros 15 reels', m: { ord: 2, evil: 'x' } }, { i: 'aa12', y: 'scr', t: 4, n: 50 },
  { i: 'aa13', y: 'err', t: 5, m: { msg: 'fallo de pepe@x.com al 600 123 456', src: 'p-zima.html', line: 9 } }, { i: 'aa14', y: 'hack', t: 1 }, { i: 'x', y: 'scr' },
  { i: 'aa15', y: 'vplay', t: 6, l: 'reel 3', ot: now - 999999999 }, { i: 'aa16', y: 'copy', t: 7, m: { len: 120 } }];
r = await call('/e', { k: k1, ev });
let E = V.prepare("SELECT * FROM e WHERE k = ? AND src = 'web' ORDER BY id").all(k1);
t(r.j.n === 5 && E.length === 5, 'valid events stored, unknown types and bad ids dropped ' + JSON.stringify(r.j));
t(E[0].y === 'sin' && E[0].s === 'reels' && E[0].m === '{"ord":2}' && E[0].rt === now, 'schema per type: unknown fields dropped');
t(JSON.parse(E[2].m).msg === 'fallo de [email] al [número]', 'no emails or phones in errors ' + E[2].m);
t(E[3].ot === null, 'a wrong device clock is not trusted');
r = await call('/e', { k: k1, ev }); t(V.prepare("SELECT COUNT(*) n FROM e WHERE k = ? AND src = 'web'").get(k1).n === 5, 'the same events twice are kept once');
t(V.prepare("SELECT evn FROM v WHERE k = ?").get(k1).evn === 6, 'event count on the visit');
r = await call('/e', { k: 'bbbbbbbbbbbbbbbbbbbb', ev }); t(V.prepare("SELECT COUNT(*) n FROM e WHERE k = 'bbbbbbbbbbbbbbbbbbbb'").get().n === 0, 'events need a real visit');
r = await call('/e', { k: k1, ev }, { origin: 'https://evil.com' }); t(r.s === 404, 'events only from our site');
r = await call('/e', { k: k1, ev: [{ i: 'big1', y: 'scr', l: 'x'.repeat(40000) }] }); t(r.s === 413, 'big payload refused');
// cap of events per visit
for (let j = 0; j < 30; j++) await call('/e', { k: k1, ev: Array.from({ length: 25 }, (_, q) => ({ i: 'c' + j + 'q' + q, y: 'tick' })) });
t(V.prepare("SELECT COUNT(*) n FROM e WHERE k = ?").get(k1).n === 600, 'cap 600 a visit');
// reload within two minutes: same visit + a «reload» event
now += 30000; r = await call('/h', { s: 'zima', x: { ...X, nav: 'reload' } }); t(r.j.k === k1 && r.j.r === 1, 'reload keeps the visit');
// robots by name: raw traffic apart, never a visit
const before = V.prepare("SELECT COUNT(*) n FROM v").get().n;
for (const [ua, tc] of [['WhatsApp/2.23.20.0', 'link_preview'], ['Mozilla/5.0 (compatible; Googlebot/2.1)', 'search_crawler'], ['Mozilla/5.0 HeadlessChrome/120', 'automation_likely'], ['Barracuda Sentinel (EE)', 'security_scanner']]) {
  r = await call('/h', { s: 'zima' }, { 'user-agent': ua }); t(r.j && !r.j.k, 'robot gets no key ' + ua);
  t(V.prepare("SELECT tc FROM b ORDER BY id DESC LIMIT 1").get().tc === tc, 'robot kept apart as ' + tc);
}
t(V.prepare("SELECT COUNT(*) n FROM v").get().n === before, 'robots never become visits');
// automation by context
r = await call('/h', { s: 'otra', x: { ...X, wd: 1 } }, { 'user-agent': UA.replace('18_6', '17_1'), 'cf-connecting-ip': '9.9.9.9' }); row = V.prepare("SELECT * FROM v WHERE k = ?").get(r.j.k);
t(row.tc === 'automation_likely' && row.tcc === 95, 'webdriver = automation ' + row.tc);
r = await call('/h', { s: 'otra', x: { ...X, it: 0 } }, { 'cf-connecting-ip': '8.8.8.8' }, { country: 'US', asn: 16509, asOrganization: 'Amazon.com, Inc.' }); row = V.prepare("SELECT * FROM v WHERE k = ?").get(r.j.k);
t(row.tc === 'automation_likely' && /servidores/.test(row.tcw), 'data centre and no interaction ' + row.tcw);
r = await call('/h', { s: 'otra', x: { ...X, it: 1 } }, { 'cf-connecting-ip': '7.7.7.7' }, { country: 'ES', asn: 16509, asOrganization: 'Amazon.com, Inc.' }); row = V.prepare("SELECT * FROM v WHERE k = ?").get(r.j.k);
t(row.tc === 'unknown' && /VPN/.test(row.tcw), 'data centre with interaction is unknown ' + row.tc);
r = await call('/h', { s: 'otra', x: { ...X, it: 0 } }, { 'cf-connecting-ip': '6.6.6.6' }); const k3 = r.j.k; row = V.prepare("SELECT * FROM v WHERE k = ?").get(k3);
t(row.tc === 'human_likely' && row.tcc === 70, 'opened without touching: less sure');
await call('/e', { k: k3, ev: [{ i: 'zz01', y: 'scr', n: 25 }] }); row = V.prepare("SELECT * FROM v WHERE k = ?").get(k3); t(row.tcc === 90 && /interactuado/.test(row.tcw), 'interaction raises the confidence');
// IPv6 and an old desktop
r = await call('/h', { s: 'otra', x: {} }, { 'cf-connecting-ip': '2a02:9130::1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0' });
row = V.prepare("SELECT * FROM v WHERE k = ?").get(r.j.k); t(row.ipv === 6 && row.br === 'Edge 141' && row.os === 'Windows 10/11' && row.dv === 'd' && row.dev === 'd' && row.scr === '' && row.lang === '', 'unknown stays unknown, IPv6, Edge ' + JSON.stringify([row.br, row.os, row.scr]));
// parsers
t(parseUA('Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/25.0 Chrome/121.0 Mobile Safari/537.36').br === 'Samsung Internet 25', 'samsung');
t(parseUA('Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1').dv === 't', 'ipad = tablet');
t(parseUA('Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 330.0').br === 'Instagram (app)', 'instagram in-app');
t(classify('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141 Safari/537.36', {}, { hl: true, it: false }).tc === 'automation_likely', 'headless hints');
// totals keep their shape
const s = await (await W.fetch(new Request('https://x/s/dcb5e945d106273454568d05', { method: 'GET' }), env)).json();
t(s.s.zima.n === 2 && s.s.zima.p === 2, 'totals ' + JSON.stringify(s.s.zima));
Date.now = realNow; console.log(`${ok} ok, ${bad} failed`);
