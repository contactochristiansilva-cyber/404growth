/* ---------- v70 · Archivos (13/11/2026): documentos importantes del ordenador de Chris, guardados aquí para siempre ----------
   Chris: «en contabilidad meter una carpeta donde suba archivos de mi ordenador importantes a tener ahí siempre guardados».
   Cualquier tipo de archivo, hasta 50 MB, en carpetas (un nombre por archivo; «General» si no se elige). D1 no guarda más de 2 MB en una
   fila, así que cada archivo va en trozos de 1,5 MB (archp) que el navegador sube uno a uno y que se juntan al descargarlo. Mientras no
   llegan todos, el archivo no sale en la lista (done = 0) y a las 6 horas se borra solo. La base es la del admin (500 MB en el plan
   gratis de D1): no se sube nada que la deje por encima de ARCH_DB_MAX. Solo se abren en el navegador los PDF y las fotos (por sus
   primeros bytes); todo lo demás se descarga, para que ningún archivo subido se ejecute dentro del admin. */
const ARCH_PART = 1500000;
const ARCH_MAX = 50 * 1048576;
const ARCH_DB_MAX = 450 * 1048576;
let archOk = false;
async function archReady(env) {
  if (archOk) return;
  await env.DB.batch([
    env.DB.prepare("CREATE TABLE IF NOT EXISTS arch (id TEXT PRIMARY KEY, folder TEXT NOT NULL, name TEXT NOT NULL, type TEXT, size INTEGER NOT NULL, parts INTEGER NOT NULL, note TEXT, done INTEGER NOT NULL DEFAULT 0, created INTEGER NOT NULL, updated INTEGER)"),
    env.DB.prepare("CREATE TABLE IF NOT EXISTS archp (id TEXT NOT NULL, k INTEGER NOT NULL, data BLOB NOT NULL, PRIMARY KEY (id, k))"),
  ]);
  archOk = true;
}
const archName = (v) => str(v, 160).replace(/[\\/:*?"<>|\u0000-\u001f]+/g, "-").replace(/^[.\s-]+/, "");
const archFolder = (v) => str(v, 60).replace(/[\\/:*?"<>|\u0000-\u001f]+/g, "-").replace(/\s+/g, " ").trim() || "General";
// what can be opened in the browser, by its first bytes (anything else is only downloaded)
const archType = (b) => finType(b) || (b.length > 6 && String.fromCharCode(b[0], b[1], b[2], b[3], b[4], b[5]) === "GIF89a" ? "image/gif" : "");
// the size of the whole database (D1 tells it after each query); null if it does not
async function archDbSize(env) {
  try { const r = await env.DB.prepare("SELECT 1 AS x").run(); const s = r && r.meta && r.meta.size_after; return typeof s === "number" ? s : null; } catch (e) { return null; }
}
async function archGone(env, ids) {
  const q = [];
  for (const id of ids) q.push(env.DB.prepare("DELETE FROM archp WHERE id = ?1").bind(id), env.DB.prepare("DELETE FROM arch WHERE id = ?1").bind(id));
  for (let i = 0; i < q.length; i += 80) await env.DB.batch(q.slice(i, i + 80));
}
async function archList(env) {
  const old = (await env.DB.prepare("SELECT id FROM arch WHERE done = 0 AND created < ?1").bind(Date.now() - 6 * 3600000).all()).results || [];
  if (old.length) await archGone(env, old.map((r) => r.id));                       // uploads that were cut off
  const files = (await env.DB.prepare("SELECT id, folder, name, type, size, note, created, updated FROM arch WHERE done = 1 ORDER BY created DESC LIMIT 5000").all()).results || [];
  const used = files.reduce((t, f) => t + f.size, 0), db = await archDbSize(env);
  return json({ files: files, used: used, db: db, dbMax: ARCH_DB_MAX, max: ARCH_MAX, part: ARCH_PART });
}
async function archNew(req, env) {
  const b = await body(req); if (!b) return bad("body");
  const name = archName(b.name); if (!name) return bad("name");
  const size = Number(b.size);
  if (!Number.isInteger(size) || size <= 0) return bad("empty");
  if (size > ARCH_MAX) return bad("toobig", 413);
  const db = await archDbSize(env);
  if (db !== null && db + size > ARCH_DB_MAX) return bad("full", 507);
  const id = rid("ar_"), parts = Math.ceil(size / ARCH_PART);
  await env.DB.prepare("INSERT INTO arch (id, folder, name, type, size, parts, note, done, created) VALUES (?1, ?2, ?3, '', ?4, ?5, ?6, 0, ?7)")
    .bind(id, archFolder(b.folder), name, size, parts, str(b.note, 300), Date.now()).run();
  return json({ ok: true, id: id, part: ARCH_PART, parts: parts });
}
async function archPut(req, env, id, k) {
  const r = await env.DB.prepare("SELECT size, parts, done FROM arch WHERE id = ?1").bind(id).first();
  if (!r) return bad("missing", 404); if (r.done) return bad("done", 409);
  if (!(k >= 0 && k < r.parts)) return bad("part");
  const want = k < r.parts - 1 ? ARCH_PART : r.size - ARCH_PART * (r.parts - 1);
  if (Number(req.headers.get("content-length") || 0) > ARCH_PART) return bad("big", 413);
  const buf = new Uint8Array(await req.arrayBuffer());
  if (buf.length !== want) return bad("part");
  await env.DB.prepare("INSERT INTO archp (id, k, data) VALUES (?1, ?2, ?3) ON CONFLICT(id, k) DO UPDATE SET data = excluded.data").bind(id, k, buf).run();
  return json({ ok: true });
}
async function archDone(env, id) {
  const r = await env.DB.prepare("SELECT size, parts, done FROM arch WHERE id = ?1").bind(id).first();
  if (!r) return bad("missing", 404); if (r.done) return json({ ok: true });
  const c = await env.DB.prepare("SELECT COUNT(*) AS n, SUM(LENGTH(data)) AS s FROM archp WHERE id = ?1").bind(id).first();
  if (!c || Number(c.n) !== r.parts || Number(c.s) !== r.size) return bad("incomplete", 409);
  const h = await env.DB.prepare("SELECT substr(data, 1, 16) AS h FROM archp WHERE id = ?1 AND k = 0").bind(id).first();
  const type = h && h.h ? archType(new Uint8Array(h.h)) : "";
  await env.DB.prepare("UPDATE arch SET done = 1, type = ?1, updated = ?2 WHERE id = ?3").bind(type, Date.now(), id).run();
  return json({ ok: true, type: type });
}
async function archGet(env, id, inline) {
  const r = await env.DB.prepare("SELECT name, type, size, parts FROM arch WHERE id = ?1 AND done = 1").bind(id).first();
  if (!r) return bad("missing", 404);
  const view = inline && !!r.type, name = r.name || "archivo", ascii = name.replace(/[^A-Za-z0-9_.-]+/g, "-");
  let k = 0;
  const stream = new ReadableStream({
    async pull(c) {
      if (k >= r.parts) { c.close(); return; }
      const p = await env.DB.prepare("SELECT data FROM archp WHERE id = ?1 AND k = ?2").bind(id, k).first();
      if (!p) { c.error(new Error("part")); return; }
      c.enqueue(new Uint8Array(p.data)); k++;
    },
  });
  return new Response(stream, { status: 200, headers: Object.assign({}, SEC, {
    "content-type": view ? r.type : "application/octet-stream", "content-length": String(r.size),
    "content-disposition": (view ? "inline" : "attachment") + '; filename="' + ascii + '"; filename*=UTF-8\'\'' + encodeURIComponent(name),
    "cache-control": "private, no-store",
  }) });
}
async function archApi(req, env, p) {
  await archReady(env);
  const m = req.method;
  if (p === "arch" && m === "GET") return archList(env);
  if (p === "arch" && m === "POST") return archNew(req, env);
  if (p === "archf" && m === "POST") {                                            // rename a folder: every file in it moves
    const b = await body(req); if (!b) return bad("body");
    const from = archFolder(b.from), to = archFolder(b.to);
    if (from !== to) await env.DB.prepare("UPDATE arch SET folder = ?1, updated = ?2 WHERE folder = ?3").bind(to, Date.now(), from).run();
    return json({ ok: true, folder: to });
  }
  let x = /^arch\/(ar_[A-Za-z0-9_-]{6,30})\/p\/(\d{1,4})$/.exec(p);
  if (x && m === "PUT") return archPut(req, env, x[1], Number(x[2]));
  x = /^arch\/(ar_[A-Za-z0-9_-]{6,30})(\/done)?$/.exec(p);
  if (!x) return bad("missing", 404);
  if (x[2] && m === "POST") return archDone(env, x[1]);
  if (x[2]) return bad("missing", 404);
  if (m === "GET") return archGet(env, x[1], new URL(req.url).searchParams.get("ver") === "1");
  if (m === "DELETE") { await archGone(env, [x[1]]); return json({ ok: true }); }
  if (m === "POST") {                                                              // rename, move to another folder or change the note
    const b = await body(req); if (!b) return bad("body");
    if (!(await env.DB.prepare("SELECT 1 AS x FROM arch WHERE id = ?1").bind(x[1]).first())) return bad("missing", 404);
    const q = [], now = Date.now(), set = (col, v) => q.push(env.DB.prepare("UPDATE arch SET " + col + " = ?1, updated = ?2 WHERE id = ?3").bind(v, now, x[1]));
    if (b.name !== undefined) { const n = archName(b.name); if (!n) return bad("name"); set("name", n); }
    if (b.folder !== undefined) set("folder", archFolder(b.folder));
    if (b.note !== undefined) set("note", str(b.note, 300));
    if (q.length) await env.DB.batch(q);
    return json({ ok: true });
  }
  return bad("missing", 404);
}

