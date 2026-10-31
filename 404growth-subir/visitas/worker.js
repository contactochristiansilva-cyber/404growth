// 404 Growth: visit counter for the prospect pages (404growth.com/p/<slug>/, their new webs and the /collab landings).
// Nothing is stored on the visitor's device and no IP address is kept: the IP only feeds a hash that changes every day.
// v2 (22 oct 2026): each visit also keeps when it was last seen and whether the page was left (seen, ex), so the CRM can say «está
// dentro ahora» or «salió», and the buttons and links tapped on it, with the part of the page where they were (table c). Leaving and
// coming back later is a new visit (a new notification); a reload or coming back within two minutes is the same visit.
// v3 (27 oct 2026): «Proposal intelligence».
//  - Each visit also keeps what the browser and Cloudflare say about the context: device type, browser and system (from the user agent),
//    screen, viewport, pixel ratio, touch, language, time zone, dark mode; approximate region, city and network (ASN and its organisation,
//    from Cloudflare's request.cf, never from headers the visitor can set); IPv4 or IPv6. The IP itself is still never stored.
//  - Active time (visible AND with activity in the last 30 s, or a video playing), not just time open; scroll depth in %; active seconds
//    per section (ss, JSON).
//  - Typed events (table e) with a catalogue, a schema per type, an id from the page for de-duplication (UNIQUE k + i), limits per post
//    and per visit, the time it happened on the page and the time it arrived.
//  - Traffic classification with a confidence: human_likely, automation_likely, security_scanner, link_preview, search_crawler, unknown.
//    Robots by user agent are kept apart (table b, raw traffic) and never become visits, so they never notify.
const SALT = "490224e5d44505dc53dff8d21985982c";
const KEY = "dcb5e945d106273454568d05";
const SITES = ["https://404growth.com", "https://www.404growth.com"];
const DDL = "CREATE TABLE IF NOT EXISTS v (id INTEGER PRIMARY KEY AUTOINCREMENT, k TEXT NOT NULL, slug TEXT NOT NULL, ts INTEGER NOT NULL, vid TEXT NOT NULL, cc TEXT, dev TEXT, secs INTEGER NOT NULL DEFAULT 0, depth INTEGER NOT NULL DEFAULT 0)";
const IDX = "CREATE INDEX IF NOT EXISTS v_vid ON v (vid, slug, ts)";
const MIG = ["ALTER TABLE v ADD COLUMN seen INTEGER", "ALTER TABLE v ADD COLUMN ex INTEGER",
  "CREATE TABLE IF NOT EXISTS c (id INTEGER PRIMARY KEY AUTOINCREMENT, k TEXT NOT NULL, ts INTEGER NOT NULL, t INTEGER NOT NULL DEFAULT 0, s TEXT, sh TEXT, w TEXT, h TEXT, x INTEGER, y INTEGER)",
  "CREATE INDEX IF NOT EXISTS c_k ON c (k, id)",
  // v3
  "ALTER TABLE v ADD COLUMN cv INTEGER", "ALTER TABLE v ADD COLUMN act INTEGER", "ALTER TABLE v ADD COLUMN sd INTEGER", "ALTER TABLE v ADD COLUMN ss TEXT",
  "ALTER TABLE v ADD COLUMN br TEXT", "ALTER TABLE v ADD COLUMN os TEXT", "ALTER TABLE v ADD COLUMN dv TEXT", "ALTER TABLE v ADD COLUMN scr TEXT",
  "ALTER TABLE v ADD COLUMN lang TEXT", "ALTER TABLE v ADD COLUMN tz TEXT", "ALTER TABLE v ADD COLUMN dk INTEGER", "ALTER TABLE v ADD COLUMN tch INTEGER",
  "ALTER TABLE v ADD COLUMN rg TEXT", "ALTER TABLE v ADD COLUMN ci TEXT", "ALTER TABLE v ADD COLUMN asn INTEGER", "ALTER TABLE v ADD COLUMN aso TEXT",
  "ALTER TABLE v ADD COLUMN ipv INTEGER", "ALTER TABLE v ADD COLUMN ref TEXT", "ALTER TABLE v ADD COLUMN nav TEXT", "ALTER TABLE v ADD COLUMN tc TEXT",
  "ALTER TABLE v ADD COLUMN tcc INTEGER", "ALTER TABLE v ADD COLUMN tcw TEXT", "ALTER TABLE v ADD COLUMN tcm TEXT", "ALTER TABLE v ADD COLUMN evn INTEGER",
  "CREATE TABLE IF NOT EXISTS e (id INTEGER PRIMARY KEY AUTOINCREMENT, k TEXT NOT NULL, i TEXT NOT NULL, y TEXT NOT NULL, ver INTEGER NOT NULL DEFAULT 1, src TEXT NOT NULL DEFAULT 'web', ot INTEGER, rt INTEGER NOT NULL, t INTEGER NOT NULL DEFAULT 0, s TEXT, l TEXT, n INTEGER, m TEXT)",
  "CREATE UNIQUE INDEX IF NOT EXISTS e_ki ON e (k, i)",
  "CREATE INDEX IF NOT EXISTS e_y ON e (y, rt)",
  "CREATE TABLE IF NOT EXISTS b (id INTEGER PRIMARY KEY AUTOINCREMENT, ts INTEGER NOT NULL, slug TEXT, tc TEXT, tcc INTEGER, ua TEXT, cc TEXT, aso TEXT)",
  "CREATE INDEX IF NOT EXISTS b_ts ON b (ts)"];
const SAME = 120000;   // a reload, or back from their new web, within two minutes: the same visit
const MAX_EV = 600, PER_POST = 25, ACCEPT_LATE = 6 * 3600000;
const cut = (v, n) => typeof v === "string" ? v.replace(/[\u0000-\u001f\u007f]+/g, " ").trim().slice(0, n) : "";
const int = (x, lo, hi) => { const v = Math.round(Number(x)); return Number.isFinite(v) ? Math.max(lo, Math.min(hi, v)) : null; };
function head(origin, extra) { return Object.assign({ "access-control-allow-origin": origin, "vary": "origin", "cache-control": "no-store" }, extra || {}); }
function json(data, origin) { return new Response(JSON.stringify(data), { headers: head(origin, { "content-type": "application/json" }) }); }
async function hash(text) { const b = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(text)); return Array.from(new Uint8Array(b).slice(0, 12), (x) => x.toString(16).padStart(2, "0")).join(""); }

/* ---------- what the user agent says: device type, browser and system families, with the version when it is there ---------- */
function parseUA(ua) {
  const u = String(ua || "");
  let os = "Desconocido", m;
  if ((m = /iPhone OS (\d+)[_.](\d+)/.exec(u)) || (m = /CPU OS (\d+)[_.](\d+)/.exec(u))) os = (/iPad/.test(u) ? "iPadOS " : "iOS ") + m[1] + "." + m[2];
  else if ((m = /Android (\d+(?:\.\d+)?)/.exec(u))) os = "Android " + m[1];
  else if ((m = /Windows NT (\d+\.\d+)/.exec(u))) os = "Windows" + ({ "10.0": " 10/11", "6.3": " 8.1", "6.1": " 7" }[m[1]] || "");
  else if ((m = /Mac OS X (\d+)[_.](\d+)/.exec(u))) os = "macOS " + m[1] + "." + m[2];
  else if (/CrOS/.test(u)) os = "ChromeOS";
  else if (/Linux/.test(u)) os = "Linux";
  let br = "Desconocido";
  const B = [[/EdgA?\/(\d+)/, "Edge"], [/SamsungBrowser\/(\d+)/, "Samsung Internet"], [/OPR\/(\d+)/, "Opera"], [/FBAN|FBAV|FB_IAB/, "Facebook (app)"], [/Instagram/, "Instagram (app)"],
    [/LinkedInApp/, "LinkedIn (app)"], [/GSA\/(\d+)/, "Google (app)"], [/CriOS\/(\d+)/, "Chrome"], [/FxiOS\/(\d+)/, "Firefox"], [/Firefox\/(\d+)/, "Firefox"],
    [/Chrome\/(\d+)/, "Chrome"], [/Version\/(\d+)[\d.]* (?:Mobile\/\S+ )?Safari/, "Safari"]];
  for (const [re, name] of B) { const x = re.exec(u); if (x) { br = name + (x[1] && !/app/.test(name) ? " " + x[1] : ""); break; } }
  const dv = /iPad|Tablet|PlayBook|Silk/.test(u) || (/Android/.test(u) && !/Mobile/.test(u)) ? "t" : /Mobi|iPhone|iPod|Android/.test(u) ? "m" : u ? "d" : "?";
  return { br, os, dv };
}

/* ---------- traffic classification: heuristics with a confidence, never proof of who it is ---------- */
const RE = {
  crawler: /googlebot|bingbot|yandex(bot)?|baiduspider|duckduckbot|applebot|petalbot|ahrefsbot|semrushbot|mj12bot|dotbot|seznambot/i,
  preview: /whatsapp|facebookexternalhit|facebookcatalog|twitterbot|slackbot|slack-imgproxy|telegrambot|discordbot|linkedinbot|skypeuripreview|iframely|embedly|pinterest|redditbot|vkshare|viber|line\/|snapchat|google-pagerenderer|bitlybot/i,
  scanner: /safelinks|barracuda|proofpoint|mimecast|symantec|trendmicro|forcepoint|zscaler|urldefense|checkpoint|sophos|fortiguard|virustotal|scanner|appengine-google|microsoft office|ms-office|outlook-ios|bingpreview/i,
  automation: /headless|phantom|puppeteer|playwright|selenium|webdriver|python|curl|wget|okhttp|axios|node-fetch|go-http|java\/|libwww|httpclient|scrapy|guzzle|postman|insomnia|lighthouse|pagespeed|gtmetrix|pingdom|uptime|monitor/i,
  bot: /bot\b|crawl|spider|preview|fetch(er)?\b|scan/i,
  hosting: /amazon|aws|google (llc|cloud)|microsoft|azure|digitalocean|ovh|hetzner|linode|akamai|oracle|alibaba|tencent|contabo|vultr|choopa|scaleway|leaseweb|m247|datacamp|cloudflare|fastly|hostinger|ionos|online s\.a\.s|packet|equinix|servers\.com|hostwinds|kamatera|psychz|colocrossing/i,
};
function uaClass(ua) {
  if (!ua) return { tc: "automation_likely", tcc: 80, why: "sin navegador" };
  if (RE.crawler.test(ua)) return { tc: "search_crawler", tcc: 95, why: "buscador por su nombre" };
  if (RE.preview.test(ua)) return { tc: "link_preview", tcc: 95, why: "vista previa de enlace (WhatsApp, redes, chats)" };
  if (RE.scanner.test(ua)) return { tc: "security_scanner", tcc: 90, why: "escáner de seguridad del correo" };
  if (RE.automation.test(ua)) return { tc: "automation_likely", tcc: 90, why: "herramienta automática por su nombre" };
  if (RE.bot.test(ua)) return { tc: "automation_likely", tcc: 80, why: "se declara robot" };
  return null;
}
function classify(ua, cf, x) {
  const u = uaClass(ua);
  if (u) return u;
  const why = [], org = (cf && cf.asOrganization) || "";
  let tc = "human_likely", tcc = 70;
  if (x.wd) return { tc: "automation_likely", tcc: 95, why: "el navegador dice que lo maneja un programa" };
  if (x.hl) { tc = "automation_likely"; tcc = 75; why.push("señales de navegador sin pantalla"); }
  if (RE.hosting.test(org)) { if (x.it) { tc = "unknown"; tcc = 50; why.push("red de servidores (" + org + "), pero con interacción: puede ser una VPN o la red de una empresa"); } else { tc = "automation_likely"; tcc = 70; why.push("red de servidores (" + org + ") y sin interacción"); } }
  if (tc === "human_likely") { if (x.it) { tcc = 90; why.push("ha tocado, pulsado o hecho scroll"); } else why.push("abierta sin tocar todavía"); if (x.sw && x.sw < 200) { tcc -= 30; why.push("pantalla rara"); } }
  return { tc, tcc: Math.max(5, Math.min(99, tcc)), why: why.join("; ") };
}

/* ---------- the context the page sends with the entry (all optional; unknown stays unknown) ---------- */
function ctxOf(b) {
  const x = b && typeof b.x === "object" && b.x ? b.x : {};
  const sw = int(x.sw, 0, 10000), sh = int(x.sh, 0, 10000), vw = int(x.vw, 0, 10000), vh = int(x.vh, 0, 10000), dpr = Number(x.dpr) > 0 ? Math.min(8, Math.round(Number(x.dpr) * 100) / 100) : null;
  return {
    scr: sw && sh ? sw + "×" + sh + (vw && vh ? " · ventana " + vw + "×" + vh : "") + (dpr ? " · " + dpr + "x" : "") + (x.or ? " · " + (x.or === "p" ? "vertical" : "horizontal") : "") : "",
    sw: sw, lang: cut(x.lang, 40), tz: /^[A-Za-z_]+(\/[A-Za-z0-9_+-]+){0,2}$/.test(x.tz || "") ? x.tz.slice(0, 40) : "",
    dk: x.dk ? 1 : 0, tch: x.tch === undefined ? null : int(x.tch, 0, 20), wd: !!x.wd, hl: !!x.hl, it: !!x.it,
    ref: /^[a-z0-9.-]{1,80}$/i.test(x.ref || "") ? x.ref.toLowerCase() : "", nav: ["navigate", "reload", "back_forward", "prerender"].includes(x.nav) ? x.nav : "",
  };
}

async function hit(req, env, origin) {
  const b = req._b;
  const slug = b && typeof b.s === "string" ? b.s : "";
  const ua = req.headers.get("user-agent") || "";
  if (!/^[a-z0-9-]{1,60}$/.test(slug)) return json({}, origin);
  const now = Date.now(), cf = req._cf || {}, x = ctxOf(b);
  const robot = uaClass(ua);
  if (robot) {   /* raw traffic, apart: counted, never a visit, never a notice */
    const n = await env.DB.prepare("SELECT COUNT(*) AS n FROM b WHERE ts > ?1").bind(now - 3600000).first();
    if (!n || n.n < 500) await env.DB.prepare("INSERT INTO b (ts, slug, tc, tcc, ua, cc, aso) VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7)").bind(now, slug, robot.tc, robot.tcc, cut(ua, 160), cf.country || "", cut(cf.asOrganization, 80)).run();
    return json({}, origin);
  }
  const ip = req.headers.get("cf-connecting-ip") || "";   // set by Cloudflare itself; never X-Forwarded-For
  const vid = await hash(SALT + new Date(now).toISOString().slice(0, 10) + ip + ua);
  const same = await env.DB.prepare("SELECT k, ts, seen FROM v WHERE vid = ?1 AND slug = ?2 AND ts > ?3 ORDER BY ts DESC LIMIT 1").bind(vid, slug, now - 1800000).first();
  if (same && now - (same.seen || same.ts) < SAME) {
    await env.DB.prepare("UPDATE v SET seen = ?1, ex = 0 WHERE k = ?2").bind(now, same.k).run();
    await serverEvent(env, same.k, x.nav === "reload" ? "rel" : "res", now, { nav: x.nav || "" });
    return json({ k: same.k, r: 1 }, origin);
  }
  const day = await env.DB.prepare("SELECT COUNT(*) AS n FROM v WHERE vid = ?1 AND ts > ?2").bind(vid, now - 86400000).first();
  if (day && day.n >= 40) return json({}, origin);
  const k = crypto.randomUUID().replace(/-/g, "").slice(0, 20), p = parseUA(ua), c = classify(ua, cf, x);
  await env.DB.prepare("INSERT INTO v (k, slug, ts, vid, cc, dev, seen, ex, cv, act, sd, br, os, dv, scr, lang, tz, dk, tch, rg, ci, asn, aso, ipv, ref, nav, tc, tcc, tcw, evn) " +
    "VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?3, 0, 3, 0, 0, ?7, ?8, ?9, ?10, ?11, ?12, ?13, ?14, ?15, ?16, ?17, ?18, ?19, ?20, ?21, ?22, ?23, ?24, 0)")
    .bind(k, slug, now, vid, cf.country || "", p.dv === "d" ? "d" : "m", p.br, p.os, p.dv, x.scr, x.lang, x.tz, x.dk, x.tch,
      cut(cf.region, 60), cut(cf.city, 60), int(cf.asn, 0, 4294967295), cut(cf.asOrganization, 80), ip ? (ip.includes(":") ? 6 : 4) : null, x.ref, x.nav, c.tc, c.tcc, cut(c.why, 200)).run();
  await serverEvent(env, k, "open", now, { tc: c.tc });
  return json({ k: k }, origin);
}
async function serverEvent(env, k, y, now, m) {
  try { await env.DB.prepare("INSERT OR IGNORE INTO e (k, i, y, ver, src, ot, rt, t, m) VALUES (?1, ?2, ?3, 1, 'server', ?4, ?4, 0, ?5)").bind(k, "s" + now.toString(36) + y, y, now, JSON.stringify(m || {})).run(); } catch (e) { /* never blocks the visit */ }
}

async function progress(req, env, origin) {
  const b = req._b;
  if (b && typeof b.k === "string" && /^[a-f0-9]{20}$/.test(b.k)) {
    const secs = int(b.t, 0, 3600) || 0, depth = int(b.d, 0, 9) || 0, act = int(b.a, 0, 3600), sd = int(b.sd, 0, 100);
    let ss = null;
    if (b.ss && typeof b.ss === "object") {   /* active seconds per section: up to 40 sections, ids only */
      const o = {}; let n = 0;
      for (const [id, v] of Object.entries(b.ss)) { if (n >= 40) break; if (/^[A-Za-z][\w-]{0,39}$/.test(id)) { const s = int(v, 0, 3600); if (s) { o[id] = s; n++; } } }
      ss = JSON.stringify(o);
    }
    await env.DB.prepare("UPDATE v SET secs = MAX(secs, ?1), depth = MAX(depth, ?2), seen = ?3, ex = ?4, act = MAX(COALESCE(act, 0), COALESCE(?6, 0)), sd = MAX(COALESCE(sd, 0), COALESCE(?7, 0)), ss = COALESCE(?8, ss) WHERE k = ?5")
      .bind(secs, depth, Date.now(), b.e ? 1 : 0, b.k, act, sd, ss).run();
  }
  return json({}, origin);
}
/* the buttons and links tapped: what it said, where it went and the part of the page (its id and heading), up to 300 a visit */
async function clicks(req, env, origin) {
  const b = req._b;
  if (!b || typeof b.k !== "string" || !/^[a-f0-9]{20}$/.test(b.k) || !Array.isArray(b.c)) return json({}, origin);
  const v = await env.DB.prepare("SELECT k, (SELECT COUNT(*) FROM c WHERE c.k = v.k) AS n FROM v WHERE k = ?1").bind(b.k).first();
  if (!v || v.n >= 300) return json({}, origin);
  const now = Date.now(), list = b.c.slice(0, Math.min(20, 300 - v.n));
  const n = (x, hi) => Math.max(0, Math.min(hi, Math.round(Number(x) || 0)));
  const q = list.filter((x) => x && typeof x === "object").map((x) => env.DB.prepare("INSERT INTO c (k, ts, t, s, sh, w, h, x, y) VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, ?8, ?9)")
    .bind(b.k, now, n(x.t, 7200), cut(x.s, 40), cut(x.sh, 80), cut(x.w, 90), cut(x.h, 120), n(x.x, 100), n(x.y, 100)));
  q.push(env.DB.prepare("UPDATE v SET seen = ?1, ex = 0 WHERE k = ?2").bind(now, b.k));
  await env.DB.batch(q);
  return json({}, origin);
}

/* ---------- v3: typed events ----------
   y: the type (short code, the catalogue below); i: an id made by the page (de-duplication: the same event sent twice is kept once);
   t: seconds since the visit began; ot: when it happened (page clock, accepted only within 6 h of arrival); s: the section id;
   l: a short label (a heading, a video name: never anything typed by the visitor); n: a number; m: extra fields, only the ones the type allows. */
const EV = {
  hid: [], vis: [], idle: [], wake: [], end: [], rel: [], nav: ["ttfb", "dcl", "load", "lcp", "cls", "net", "save"],
  err: ["msg", "src", "line"], rerr: ["tag", "res"],
  sin: ["ord"], scr: [], exp: [], col: [], tab: [],
  vplay: [], vprog: [], vend: [], vpause: [],
  img: [], gal: [],
  form0: ["form"], form1: ["form"], copy: ["len"], print: [], share: ["ch"], dl: ["file"],
  resize: ["or"], fs: [], tick: [],
};
const META_STR = 120;
function cleanEvent(x, visitTs, now) {
  if (!x || typeof x !== "object") return null;
  const y = typeof x.y === "string" && Object.prototype.hasOwnProperty.call(EV, x.y) ? x.y : null;
  const i = typeof x.i === "string" && /^[A-Za-z0-9_-]{4,24}$/.test(x.i) ? x.i : null;
  if (!y || !i) return null;
  let ot = int(x.ot, 0, 9e15);
  if (ot && (ot < visitTs - 60000 || ot > now + 60000 || now - ot > ACCEPT_LATE)) ot = null;   // a wrong clock on the device: keep only the arrival time
  const m = {};
  if (x.m && typeof x.m === "object") for (const f of EV[y]) {
    const v = x.m[f];
    if (typeof v === "number" && Number.isFinite(v)) m[f] = Math.round(v * 1000) / 1000;
    else if (typeof v === "string") { const c = cut(v, META_STR); if (c) m[f] = c; }
  }
  if (y === "err" && m.msg) m.msg = m.msg.replace(/[\w.+-]+@[\w-]+\.[\w.]+/g, "[email]").replace(/\+?\d[\d\s-]{7,}\d/g, "[número]");
  return { y, i, ot, t: int(x.t, 0, 7200) || 0, s: /^[A-Za-z][\w-]{0,39}$/.test(x.s || "") ? x.s : "", l: cut(x.l, 80), n: int(x.n, -1e9, 1e9), m: Object.keys(m).length ? JSON.stringify(m) : null };
}
async function events(req, env, origin) {
  const b = req._b;
  if (!b || typeof b.k !== "string" || !/^[a-f0-9]{20}$/.test(b.k) || !Array.isArray(b.ev)) return json({}, origin);
  const v = await env.DB.prepare("SELECT k, ts, COALESCE(evn, 0) AS n FROM v WHERE k = ?1").bind(b.k).first();
  if (!v) return json({}, origin);
  if (v.n >= MAX_EV) return json({ full: 1 }, origin);
  const now = Date.now(), list = b.ev.slice(0, Math.min(PER_POST, MAX_EV - v.n)).map((x) => cleanEvent(x, v.ts, now)).filter(Boolean);
  if (!list.length) return json({ n: 0 }, origin);
  const q = list.map((x) => env.DB.prepare("INSERT OR IGNORE INTO e (k, i, y, ver, src, ot, rt, t, s, l, n, m) VALUES (?1, ?2, ?3, 1, 'web', ?4, ?5, ?6, ?7, ?8, ?9, ?10)")
    .bind(b.k, x.i, x.y, x.ot, now, x.t, x.s, x.l, x.n, x.m));
  q.push(env.DB.prepare("UPDATE v SET evn = (SELECT COUNT(*) FROM e WHERE e.k = ?1), seen = ?2 WHERE k = ?1").bind(b.k, now));
  /* interaction after an entry «sin tocar»: the classification gets more sure (only upwards, and never over a manual one) */
  if (list.some((x) => ["scr", "exp", "col", "tab", "vplay", "copy", "form0", "print", "sin"].includes(x.y)))
    q.push(env.DB.prepare("UPDATE v SET tcc = MAX(COALESCE(tcc, 0), 90), tcw = CASE WHEN tcw LIKE '%sin tocar%' THEN 'ha interactuado con la página' ELSE tcw END WHERE k = ?1 AND tc = 'human_likely' AND tcm IS NULL").bind(b.k));
  await env.DB.batch(q);
  return json({ n: list.length }, origin);
}

async function totals(env) {
  const now = Date.now();
  const a = await env.DB.prepare("SELECT slug, COUNT(*) AS n, SUM(ts > ?1) AS d, MIN(ts) AS f, MAX(ts) AS l, MAX(secs) AS t, MAX(depth) AS p FROM v GROUP BY slug").bind(now - 86400000).all();
  const z = await env.DB.prepare("SELECT slug, cc, dev FROM v WHERE id IN (SELECT MAX(id) FROM v GROUP BY slug)").all();
  const last = {};
  for (const r of z.results) last[r.slug] = r;
  const s = {};
  let tot = 0;
  for (const r of a.results) { tot += r.n; s[r.slug] = { n: r.n, d: r.d, f: r.f, l: r.l, t: r.t, p: r.p, c: last[r.slug].cc, m: last[r.slug].dev }; }
  return { at: now, tot: tot, pages: a.results.length, s: s };
}
async function route(req, env, cf) {
  const url = new URL(req.url);
  const o = req.headers.get("origin") || "";
  const ours = SITES.includes(o);
  const origin = ours ? o : SITES[0];
  if (req.method === "POST" && ours) {
    const txt = await req.text();   // read once, with a size limit (the content-length header is not trusted)
    if (txt.length > 32768) return new Response("", { status: 413, headers: head(origin) });
    try { req._b = JSON.parse(txt); } catch (e) { req._b = null; }
    req._cf = cf;
    if (url.pathname === "/h") return hit(req, env, origin);
    if (url.pathname === "/p") return progress(req, env, origin);
    if (url.pathname === "/c") return clicks(req, env, origin);
    if (url.pathname === "/e") return events(req, env, origin);
  }
  // the totals: /s/<KEY>, or /s/<KEY>/<anything> so a reader behind a cache can ask for a fresh copy
  if (req.method === "GET" && (url.pathname === "/s/" + KEY || url.pathname.startsWith("/s/" + KEY + "/"))) return json(await totals(env), "*");
  return new Response("", { status: 404, headers: head(origin) });
}
async function migrate(env) {
  await env.DB.batch([env.DB.prepare(DDL), env.DB.prepare(IDX)]);
  for (const m of MIG) { try { await env.DB.prepare(m).run(); } catch (x) { /* the column is there already */ } }
}
export default {
  async fetch(req, env) {
    try {
      return await route(req.clone(), env, req.cf);
    } catch (e) {
      if (!/no such table|no such column|has no column/i.test(String(e && e.message))) return new Response("error", { status: 500 });
      await migrate(env);
      return route(req, env, req.cf);
    }
  },
};
export { parseUA, classify, cleanEvent, EV };
