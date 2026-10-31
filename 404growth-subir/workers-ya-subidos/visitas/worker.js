// 404 Growth: visit counter for the prospect pages (404growth.com/p/<slug>/, their new webs and the /collab landings).
// Nothing is stored on the visitor's device and no IP address is kept: the IP only feeds a hash that changes every day.
// v2 (22 oct 2026): each visit also keeps when it was last seen and whether the page was left (seen, ex), so the CRM can say «está
// dentro ahora» or «salió», and the buttons and links tapped on it, with the part of the page where they were (table c). Leaving and
// coming back later is a new visit (a new notification); a reload or coming back within two minutes is the same visit.
const SALT = "490224e5d44505dc53dff8d21985982c";
const KEY = "dcb5e945d106273454568d05";
const SITES = ["https://404growth.com", "https://www.404growth.com"];
const BOT = /bot|crawl|spider|preview|scan|headless|lighthouse|monitor|whatsapp|facebookexternalhit|slack|telegram|discord|curl|wget|python|okhttp|http-client|axios|node-fetch|phantom|puppeteer|playwright/i;
const DDL = "CREATE TABLE IF NOT EXISTS v (id INTEGER PRIMARY KEY AUTOINCREMENT, k TEXT NOT NULL, slug TEXT NOT NULL, ts INTEGER NOT NULL, vid TEXT NOT NULL, cc TEXT, dev TEXT, secs INTEGER NOT NULL DEFAULT 0, depth INTEGER NOT NULL DEFAULT 0)";
const IDX = "CREATE INDEX IF NOT EXISTS v_vid ON v (vid, slug, ts)";
const MIG = ["ALTER TABLE v ADD COLUMN seen INTEGER", "ALTER TABLE v ADD COLUMN ex INTEGER",
  "CREATE TABLE IF NOT EXISTS c (id INTEGER PRIMARY KEY AUTOINCREMENT, k TEXT NOT NULL, ts INTEGER NOT NULL, t INTEGER NOT NULL DEFAULT 0, s TEXT, sh TEXT, w TEXT, h TEXT, x INTEGER, y INTEGER)",
  "CREATE INDEX IF NOT EXISTS c_k ON c (k, id)"];
const SAME = 120000;   // a reload, or back from their new web, within two minutes: the same visit
const cut = (v, n) => typeof v === "string" ? v.replace(/[\u0000-\u001f]+/g, " ").trim().slice(0, n) : "";
function head(origin, extra) { return Object.assign({ "access-control-allow-origin": origin, "vary": "origin", "cache-control": "no-store" }, extra || {}); }
function json(data, origin) { return new Response(JSON.stringify(data), { headers: head(origin, { "content-type": "application/json" }) }); }
async function hash(text) { const b = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(text)); return Array.from(new Uint8Array(b).slice(0, 12), (x) => x.toString(16).padStart(2, "0")).join(""); }
async function hit(req, env, origin) {
  const b = await req.json().catch(() => null);
  const slug = b && typeof b.s === "string" ? b.s : "";
  const ua = req.headers.get("user-agent") || "";
  if (!/^[a-z0-9-]{1,60}$/.test(slug) || !ua || BOT.test(ua)) return json({}, origin);
  const now = Date.now();
  const vid = await hash(SALT + new Date(now).toISOString().slice(0, 10) + (req.headers.get("cf-connecting-ip") || "") + ua);
  const same = await env.DB.prepare("SELECT k, ts, seen FROM v WHERE vid = ?1 AND slug = ?2 AND ts > ?3 ORDER BY ts DESC LIMIT 1").bind(vid, slug, now - 1800000).first();
  if (same && now - (same.seen || same.ts) < SAME) {
    await env.DB.prepare("UPDATE v SET seen = ?1, ex = 0 WHERE k = ?2").bind(now, same.k).run();
    return json({ k: same.k }, origin);
  }
  const day = await env.DB.prepare("SELECT COUNT(*) AS n FROM v WHERE vid = ?1 AND ts > ?2").bind(vid, now - 86400000).first();
  if (day && day.n >= 40) return json({}, origin);
  const k = crypto.randomUUID().replace(/-/g, "").slice(0, 20);
  await env.DB.prepare("INSERT INTO v (k, slug, ts, vid, cc, dev, seen, ex) VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?3, 0)").bind(k, slug, now, vid, (req.cf && req.cf.country) || "", /Mobi|Android|iPhone/i.test(ua) ? "m" : "d").run();
  return json({ k: k }, origin);
}
async function progress(req, env, origin) {
  const b = await req.json().catch(() => null);
  if (b && typeof b.k === "string" && /^[a-f0-9]{20}$/.test(b.k)) {
    const secs = Math.max(0, Math.min(3600, Math.round(Number(b.t) || 0)));
    const depth = Math.max(0, Math.min(9, Math.round(Number(b.d) || 0)));
    await env.DB.prepare("UPDATE v SET secs = MAX(secs, ?1), depth = MAX(depth, ?2), seen = ?3, ex = ?4 WHERE k = ?5").bind(secs, depth, Date.now(), b.e ? 1 : 0, b.k).run();
  }
  return json({}, origin);
}
/* the buttons and links tapped: what it said, where it went and the part of the page (its id and heading), up to 300 a visit */
async function clicks(req, env, origin) {
  const b = await req.json().catch(() => null);
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
async function route(req, env) {
  const url = new URL(req.url);
  const o = req.headers.get("origin") || "";
  const ours = SITES.includes(o);
  const origin = ours ? o : SITES[0];
  if (req.method === "POST" && ours && url.pathname === "/h") return hit(req, env, origin);
  if (req.method === "POST" && ours && url.pathname === "/p") return progress(req, env, origin);
  if (req.method === "POST" && ours && url.pathname === "/c") return clicks(req, env, origin);
  // the totals: /s/<KEY>, or /s/<KEY>/<anything> so a reader behind a cache can ask for a fresh copy
  if (req.method === "GET" && (url.pathname === "/s/" + KEY || url.pathname.startsWith("/s/" + KEY + "/"))) return json(await totals(env), "*");
  return new Response("", { status: 404, headers: head(origin) });
}
export default {
  async fetch(req, env) {
    try {
      return await route(req.clone(), env);
    } catch (e) {
      if (!/no such table|no such column/i.test(String(e && e.message))) return new Response("error", { status: 500 });
      await env.DB.batch([env.DB.prepare(DDL), env.DB.prepare(IDX)]);
      for (const m of MIG) { try { await env.DB.prepare(m).run(); } catch (x) { /* the column is there already */ } }
      return route(req, env);
    }
  },
};
