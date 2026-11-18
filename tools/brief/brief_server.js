/* ---------- v78 · Briefs (18/11/2026): formularios para que un cliente nos cuente su proyecto ----------
   Chris: «necesito saber por parte de ellos absolutamente toda la información… vamos a preparar este formulario con el branding de ellos».
   La página es estática (404growth.com/brief/<id>/, hecha con tools/brief/build.py desde su JSON) y se abre con ?k=<clave>.
   Un mismo enlace para todo su equipo: cada respuesta se guarda sola, campo a campo (json_patch, sin pisar lo que escriba otro).
     /l/brief    GET   lo guardado (?b=<id>&k=<clave>)
     /l/brief    POST  {b, k, set:{campo: valor}} guarda · {a:'send'} «Enviar a 404 Growth» · {a:'rmfile', f} quita un archivo
     /l/briefup  PUT   un archivo (cuerpo crudo, hasta 95 MB) a R2 (binding TV, carpeta brief/<id>/)
   Avisos al móvil: cuando empiezan a rellenarlo y cuando lo envían. En el admin: sección «Briefs» (briefApi).
   La clave de cada brief la crea el admin la primera vez (no está en el código): el enlace se copia desde Briefs. */
const BRIEF_Q = /*BRIEF_JSON*/ {};
const BRIEF_SEED = [{ id: "efap-miami", name: "EFAP Miami · Open Day" }];
const BRIEF_FMAX = 95 * 1048576, BRIEF_FILES = 120, BRIEF_TOT = 3 * 1024 * 1048576;
const BRIEF_ID = /^[a-z0-9-]{3,40}$/, BRIEF_K = /^[A-Za-z0-9_-]{16,40}$/;
let briefOk = false;
async function briefReady(env) {
  if (briefOk) return;
  await env.DB.prepare("CREATE TABLE IF NOT EXISTS brief (id TEXT PRIMARY KEY, name TEXT NOT NULL, k TEXT NOT NULL, data TEXT NOT NULL DEFAULT '{}', files TEXT NOT NULL DEFAULT '[]', ts INTEGER NOT NULL, upd INTEGER, started INTEGER, sent INTEGER, seen INTEGER NOT NULL DEFAULT 0)").run();
  const now = Date.now();
  await env.DB.batch(BRIEF_SEED.map((b) => env.DB.prepare("INSERT OR IGNORE INTO brief (id, name, k, ts) VALUES (?1, ?2, ?3, ?4)").bind(b.id, b.name, (rid("") + rid("")).slice(0, 24), now)));
  briefOk = true;
}
const briefSame = (a, b) => { a = String(a || ""); b = String(b || ""); if (!a || a.length !== b.length) return false; let d = 0; for (let i = 0; i < a.length; i++) d |= a.charCodeAt(i) ^ b.charCodeAt(i); return !d; };
const briefLink = (r) => SITE + "/brief/" + r.id + "/?k=" + r.k;
// los campos que se pueden guardar, con su tipo: la pregunta, «otro / qué ponemos» (_o) y «aún no lo sabemos» (__p)
function briefKeys(id) {
  const s = BRIEF_Q[id]; if (!s) return null;
  const m = {};
  for (const sec of s.sections || []) for (const q of sec.q || []) {
    if (q.type === "files") continue;
    m[q.id] = q.type;
    if (q.other || q.type === "confirm") m[q.id + "_o"] = "text";
    if (!q.nopend) m[q.id + "__p"] = "flag";
  }
  return m;
}
function briefVal(t, v) {
  if (v === null || v === undefined || v === "") return "";
  if (t === "flag") return v ? 1 : "";
  if (t === "many") return Array.isArray(v) ? v.filter((x) => typeof x === "string").map((x) => x.trim().slice(0, 200)).filter(Boolean).slice(0, 40) : null;
  if (typeof v === "number" && Number.isFinite(v)) return String(v);
  if (typeof v !== "string") return null;
  return v.slice(0, t === "long" ? 8000 : 2000);
}
function briefCount(id, data, files) {
  const s = BRIEF_Q[id]; let n = 0, tot = 0;
  for (const sec of (s && s.sections) || []) for (const q of sec.q || []) {
    tot++;
    if (q.type === "files") { if (files.length) n++; continue; }
    const v = data[q.id];
    if (data[q.id + "__p"] || (Array.isArray(v) ? v.length : String(v == null ? "" : v).trim())) n++;
  }
  return { n, tot };
}
const briefF = (f) => ({ k: f.k, name: f.name, size: f.size, type: f.type, ts: f.ts });
function briefName(v) { const n = String(v || "").replace(/[\u0000-\u001f\u007f/\\]+/g, " ").trim().slice(-120); return n || "archivo"; }
async function briefPush(env, r, title, body) { try { await pushAll(env, { title, body, tag: "brief-" + r.id, url: "/admin#briefs" }); } catch (e) {} }
async function briefPublic(req, env, ctx, p) {
  await briefReady(env);
  const m = req.method, u = new URL(req.url), now = Date.now(), DBq = env.DB;
  const later = (pr) => { if (ctx && ctx.waitUntil) ctx.waitUntil(pr.catch(() => {})); else return pr.catch(() => {}); };
  const H = { "cache-control": "no-store" };
  if (m !== "GET") { const o = req.headers.get("origin"); if (!o || !origins(env).includes(o)) return bad("origin", 403); }
  const get = async (id, k) => {
    if (typeof id !== "string" || typeof k !== "string" || !BRIEF_ID.test(id) || !BRIEF_K.test(k)) return null;
    const r = await DBq.prepare("SELECT * FROM brief WHERE id = ?1").bind(id).first();
    return r && briefSame(r.k, k) ? r : null;
  };
  const started = async (r) => {   // el primer cambio: aviso a Chris
    const x = await DBq.prepare("UPDATE brief SET started = ?2 WHERE id = ?1 AND started IS NULL").bind(r.id, now).run();
    if (x && x.meta && x.meta.changes) await briefPush(env, r, "Brief empezado · " + r.name, "Han empezado a rellenar el brief. Lo ves en Briefs, a medida que lo escriben.");
  };
  if (p === "brief" && m === "GET") {
    const r = await get(u.searchParams.get("b"), u.searchParams.get("k")); if (!r) return bad("key", 403);
    return json({ ok: true, data: parse(r.data, {}), files: (parse(r.files, []) || []).map(briefF), sent: r.sent || null, upd: r.upd || null }, 200, H);
  }
  if (p === "briefup") {
    if (m !== "PUT") return bad("method", 405);
    if (!env.TV) return bad("nofiles", 503);
    const r = await get(u.searchParams.get("b"), u.searchParams.get("k")); if (!r) return bad("key", 403);
    const len = Number(req.headers.get("content-length") || 0);
    if (!len) return bad("empty", 411);
    if (len > BRIEF_FMAX) return bad("big", 413);
    const F0 = parse(r.files, []) || [];
    if (F0.length >= BRIEF_FILES || F0.reduce((a, f) => a + (f.size || 0), 0) + len > BRIEF_TOT) return bad("full", 409);
    const name = briefName(u.searchParams.get("n"));
    let type = str(req.headers.get("content-type") || "", 120).split(";")[0].trim().toLowerCase();
    if (!/^[a-z0-9.+-]+\/[a-z0-9.+-]+$/.test(type)) type = "application/octet-stream";
    const key = "brief/" + r.id + "/" + rid("").slice(0, 10) + "-" + (name.normalize("NFKD").replace(/[^A-Za-z0-9._-]+/g, "_").replace(/^_+|_+$/g, "").slice(-60) || "archivo");
    let obj; try { obj = await env.TV.put(key, req.body, { httpMetadata: { contentType: type }, customMetadata: { brief: r.id } }); } catch (e) { return bad("upload", 502); }
    const f = { k: key, name, size: (obj && obj.size) || len, type, ts: now };
    const cur = await DBq.prepare("SELECT files FROM brief WHERE id = ?1").bind(r.id).first(), L = parse(cur && cur.files, []) || [];
    L.push(f);
    await DBq.prepare("UPDATE brief SET files = ?2, upd = ?3 WHERE id = ?1").bind(r.id, JSON.stringify(L), now).run();
    later(started(r));
    return json({ ok: true, files: L.map(briefF) }, 200, H);
  }
  if (m !== "POST" || p !== "brief") return bad("method", 405);
  const b = await body(req, 300000); if (!b) return bad("body");
  const r = await get(b.b, b.k); if (!r) return bad("key", 403);
  if (b.a === "rmfile") {
    const L = parse(r.files, []) || [], f = L.find((x) => x.k === b.f); if (!f) return json({ ok: true, files: L.map(briefF) }, 200, H);
    try { if (env.TV) await env.TV.delete(f.k); } catch (e) {}
    const cur = await DBq.prepare("SELECT files FROM brief WHERE id = ?1").bind(r.id).first(), N = (parse(cur && cur.files, []) || []).filter((x) => x.k !== f.k);
    await DBq.prepare("UPDATE brief SET files = ?2, upd = ?3 WHERE id = ?1").bind(r.id, JSON.stringify(N), now).run();
    return json({ ok: true, files: N.map(briefF) }, 200, H);
  }
  if (b.a === "send") {
    await DBq.prepare("UPDATE brief SET sent = ?2, upd = ?2 WHERE id = ?1").bind(r.id, now).run();
    const F = parse(r.files, []) || [], c = briefCount(r.id, parse(r.data, {}) || {}, F);
    later(briefPush(env, r, "Brief enviado · " + r.name, c.n + " de " + c.tot + " preguntas respondidas" + (F.length ? " y " + F.length + (F.length === 1 ? " archivo" : " archivos") : "") + ". Míralo en Briefs."));
    return json({ ok: true, sent: now }, 200, H);
  }
  const allow = briefKeys(r.id); if (!allow) return bad("missing", 404);
  const set = b.set && typeof b.set === "object" && !Array.isArray(b.set) ? b.set : null; if (!set) return bad("body");
  const patch = {}; let n = 0;
  for (const [key, v] of Object.entries(set).slice(0, 300)) {
    const t = allow[key]; if (!t) continue;
    const x = briefVal(t, v); if (x === null) continue;
    patch[key] = x === "" || (Array.isArray(x) && !x.length) ? null : x; n++;
  }
  if (n) await DBq.prepare("UPDATE brief SET data = json_patch(data, ?2), upd = ?3 WHERE id = ?1").bind(r.id, JSON.stringify(patch), now).run();
  if (n) later(started(r));
  return json({ ok: true, n, upd: n ? now : r.upd || null }, 200, H);
}
async function briefApi(req, env, p) {
  await briefReady(env);
  const m = req.method, DBq = env.DB, now = Date.now();
  if (p === "brief" && m === "GET") {
    const rows = (await DBq.prepare("SELECT * FROM brief ORDER BY COALESCE(upd, ts) DESC").all()).results || [];
    return json({ briefs: rows.map((r) => { const d = parse(r.data, {}) || {}, F = parse(r.files, []) || [], c = briefCount(r.id, d, F); return { id: r.id, name: r.name, ts: r.ts, upd: r.upd || null, started: r.started || null, sent: r.sent || null, seen: r.seen || 0, n: c.n, tot: c.tot, files: F.length, link: briefLink(r), who: str(d.quien, 120) }; }), files: !!env.TV });
  }
  const q = /^brief\/([a-z0-9-]{3,40})(?:\/(f|seen|reset))?$/.exec(p); if (!q) return bad("missing", 404);
  const r = await DBq.prepare("SELECT * FROM brief WHERE id = ?1").bind(q[1]).first(); if (!r) return bad("missing", 404);
  const F = parse(r.files, []) || [];
  if (!q[2] && m === "GET") {
    const d = parse(r.data, {}) || {}, c = briefCount(r.id, d, F);
    return json({ brief: { id: r.id, name: r.name, ts: r.ts, upd: r.upd || null, started: r.started || null, sent: r.sent || null, seen: r.seen || 0, data: d, files: F.map(briefF), link: briefLink(r), n: c.n, tot: c.tot }, q: BRIEF_Q[r.id] || null });
  }
  if (q[2] === "seen" && m === "POST") { await DBq.prepare("UPDATE brief SET seen = ?2 WHERE id = ?1").bind(r.id, now).run(); return json({ ok: true }); }
  if (q[2] === "reset" && m === "POST") {   // vaciarlo (después de probarlo uno mismo); la clave no cambia
    try { if (env.TV && F.length) await env.TV.delete(F.map((f) => f.k)); } catch (e) {}
    await DBq.prepare("UPDATE brief SET data = '{}', files = '[]', upd = NULL, started = NULL, sent = NULL, seen = 0 WHERE id = ?1").bind(r.id).run();
    return json({ ok: true });
  }
  if (q[2] === "f" && m === "GET") {
    const f = F.find((x) => x.k === new URL(req.url).searchParams.get("k")); if (!f || !env.TV) return bad("missing", 404);
    const obj = await env.TV.get(f.k); if (!obj) return bad("missing", 404);
    // solo se abren en el navegador las fotos, los PDF y los vídeos; lo demás se descarga (nada de lo subido se ejecuta en el admin)
    const safe = /^(image\/(jpeg|png|webp|gif|heic|heif|avif)|application\/pdf|video\/(mp4|quicktime|webm))$/.test(f.type || "");
    return new Response(obj.body, { headers: Object.assign({}, SEC, { "content-type": safe ? f.type : "application/octet-stream", "content-disposition": (safe && new URL(req.url).searchParams.get("dl") !== "1" ? "inline" : "attachment") + "; filename*=UTF-8''" + encodeURIComponent(f.name), "cache-control": "private, no-store", "x-content-type-options": "nosniff" }) });
  }
  return bad("method", 405);
}
