/* ---------- v77 · Talento (18/11/2026): el sistema de contratación ----------
   Chris: «crear este sistema de captación lo más bueno posible para siempre tener talento disponible que entre al equipo conforme crezca la empresa».
   Las páginas de empleo son estáticas (404growth.com/equipo/<puesto>/, hechas con tools/talento/build.py desde roles.json) y mandan aquí:
     /l/jobs  GET   qué puestos están abiertos
     /l/job   POST  la candidatura (la IA la puntúa sola con la rúbrica del puesto y avisa a Chris)
     /l/jobcv POST  su CV en PDF (cuerpo crudo, hasta 1,8 MB), con el código que da /l/job
     /l/jobt  POST  la prueba técnica: qué hay que hacer (enlace /equipo/prueba/?t=<id>.<código>)
     /l/jobts POST  la entrega de la prueba (la IA la precorrige)
     /l/jobm  POST  la entrevista: huecos libres (los mismos de Google que las llamadas de venta)
     /l/jobmb POST  reserva la entrevista: evento en Google con Meet
     /l/jobv  POST  su vídeo selfie: empezar ({a:'start'}), terminar ({a:'done'}) o tirarlo ({a:'abort'}). Va a R2 (binding TV), por partes
     /l/jobvp PUT   una parte del vídeo (8 MiB), con el código que da /l/jobv. Sin R2, las páginas piden el enlace del vídeo como antes.
   En el admin, la sección Talento (/admin#talento): talApi. La IA ordena y explica; mover, descartar o contratar lo decide Chris.
   Mensajes de cada etapa: por email desde hola@ si hay clave de Resend (Ajustes › Newsletter) y, si no, listos para WhatsApp.
   RGPD: se borran solas a los 6 meses sin moverse (12 si dejaron guardarlas para futuros puestos), salvo las del equipo.
   Prueba interna (`dev`): desde un navegador marcado con ?interno=1, como en la agenda. Sale en el admin marcada, no cuenta en las cifras,
   no se mira si está repetida y la entrevista no crea evento en Google. */
const TAL = /*TAL_JSON*/ {};
const TAL_CV = 1800000, TAL_DAYMAX = 5;
// el vídeo selfie (v77f): grabado en la página o subido de la galería, hasta 150 MB, en partes de 8 MiB a R2
const TAL_VMAX = 150 * 1048576, TAL_VPART = 8 * 1048576, TAL_VDAY = 12;
const TAL_VK = /^v\/\d{6}\/[A-Za-z0-9_-]{8,24}$/, TAL_VT = /^[A-Za-z0-9_-]{16}$/;
const TAL_ID = /^T[A-Za-z0-9_-]{8,16}$/, TAL_TOK = /^(T[A-Za-z0-9_-]{8,16})\.([A-Za-z0-9_-]{16})$/;
const TAL_ST = TAL.stages ? TAL.stages.map((x) => x[0]) : [];
let talOk = false;
async function talReady(env) {
  if (talOk) return;
  await env.DB.batch([
    env.DB.prepare("CREATE TABLE IF NOT EXISTS tcand (id TEXT PRIMARY KEY, job TEXT NOT NULL, ts INTEGER NOT NULL, upd INTEGER NOT NULL, stage TEXT NOT NULL, name TEXT NOT NULL, email TEXT NOT NULL, phone TEXT, city TEXT, data TEXT NOT NULL, ko TEXT, score INTEGER, ai TEXT, test TEXT, meet TEXT, msgs TEXT, notes TEXT, tok TEXT NOT NULL, ih TEXT, keep INTEGER NOT NULL DEFAULT 0, cv INTEGER NOT NULL DEFAULT 0, seen INTEGER NOT NULL DEFAULT 0, dev INTEGER NOT NULL DEFAULT 0)"),
    env.DB.prepare("CREATE INDEX IF NOT EXISTS tcand_job ON tcand (job, stage)"),
    env.DB.prepare("CREATE TABLE IF NOT EXISTS tcvf (id TEXT PRIMARY KEY, data BLOB NOT NULL, size INTEGER NOT NULL)"),
    env.DB.prepare("CREATE TABLE IF NOT EXISTS tvid (k TEXT PRIMARY KEY, up TEXT NOT NULL, tok TEXT NOT NULL, ts INTEGER NOT NULL, size INTEGER NOT NULL, type TEXT NOT NULL, dur REAL, src TEXT, ih TEXT, job TEXT, cid TEXT, done INTEGER NOT NULL DEFAULT 0)"),
  ]);
  talOk = true;
}
const talJob = (s) => (TAL.jobs || []).find((j) => j.slug === s) || null;
async function talOpen(env) {
  const o = parse(await getMeta(env, "tal_open"), {}) || {}, r = {};
  for (const j of TAL.jobs || []) r[j.slug] = Object.prototype.hasOwnProperty.call(o, j.slug) ? !!o[j.slug] : !!j.open;
  return r;
}
const talQs = (j) => (TAL.base_q || []).concat(j.q || []);
const talFirst = (n) => String(n || "").trim().split(/\s+/)[0] || "";
function talUrl(v) {
  let u = str(v, 300); if (!u) return "";
  if (!/^https?:\/\//i.test(u)) u = "https://" + u;
  try { const x = new URL(u); return (x.protocol === "https:" || x.protocol === "http:") && /\./.test(x.hostname) ? x.href.slice(0, 300) : null; } catch (e) { return null; }
}
function talTel(v) {
  let t = str(v, 24).replace(/[^\d+]/g, ""); if (t.startsWith("00")) t = "+" + t.slice(2);
  if (/^[6789]\d{8}$/.test(t)) t = "+34" + t;
  return /^\+\d{9,15}$/.test(t) ? t : "";
}
/* the answers, checked against the questions of the job (the same roles.json the page was built from) */
function talCheck(j, a, hasVid) {
  const out = {}, ko = [], err = [];
  a = a && typeof a === "object" ? a : {};
  for (const q of talQs(j)) {
    if (q.type === "file") continue;
    const v = a[q.id]; let x = "";
    if (q.type === "email") { x = str(v, 160).toLowerCase(); if (x && !okEmail(x)) { err.push(q.id); continue; } }
    else if (q.type === "tel") { x = v ? talTel(v) : ""; if (v && !x) { err.push(q.id); continue; } }
    else if (q.type === "url") { x = talUrl(v); if (x === null) { err.push(q.id); continue; } }
    else if (q.type === "choice") { x = (q.opts || []).includes(v) ? v : ""; }
    else if (q.type === "yesno") { x = v === "si" || v === "no" ? v : ""; }
    else { x = str(v, q.max || 300); }
    const need = (q.req || (q.id === "portfolio" && j.portfolio === "req") || (q.id === "video" && j.video === "req")) && !(q.id === "video" && hasVid);
    if (need && (!x || (q.type === "long" && x.length < 15) || (q.type === "text" && x.length < 2))) { err.push(q.id); continue; }
    if (x) out[q.id] = x;
    if (q.ko && x === q.ko) ko.push(q.id);
  }
  return { a: out, ko, err };
}
const talRow = (c) => ({ id: c.id, vid: c.vid ? 1 : 0, job: c.job, ts: c.ts, upd: c.upd, stage: c.stage, name: c.name, city: c.city || "", score: c.score == null ? null : c.score,
  dev: !!c.dev, rec: (parse(c.ai, {}) || {}).rec || "", aierr: (parse(c.ai, {}) || {}).err || "", ko: parse(c.ko, []) || [], keep: !!c.keep, cv: !!c.cv, seen: !!c.seen,
  test: (function () { const t = parse(c.test, null); return t ? { sent: t.sent || null, due: t.due || null, done: t.sub ? t.sub.ts : null, score: t.ai && t.ai.total != null ? t.ai.total : null } : null; })(),
  meet: (function () { const m = parse(c.meet, null); return m && m.start ? { start: m.start } : null; })() });
const talSame = (a, b) => { a = String(a || ""); b = String(b || ""); if (!a || a.length !== b.length) return false; let d = 0; for (let i = 0; i < a.length; i++) d |= a.charCodeAt(i) ^ b.charCodeAt(i); return !d; };
/* the videos nobody will look at: uploads never sent with a candidature (after a day) and those of candidatures already deleted */
async function talVidSweep(env, now) {
  if (!env.TV) return;
  const rows = (await env.DB.prepare("SELECT k, up, done FROM tvid WHERE (cid IS NULL AND ts < ?1) OR (cid IS NOT NULL AND cid NOT IN (SELECT id FROM tcand)) LIMIT 300").bind(now - DAY).all()).results || [];
  if (!rows.length) return;
  const keys = [];
  for (const v of rows) { if (v.done) keys.push(v.k); else { try { await env.TV.resumeMultipartUpload(v.k, v.up).abort(); } catch (e) {} } }
  try { if (keys.length) await env.TV.delete(keys); } catch (e) { return; }
  await env.DB.batch(rows.map((v) => env.DB.prepare("DELETE FROM tvid WHERE k = ?1").bind(v.k)));
}
async function talByTok(env, v) {
  const m = TAL_TOK.exec(String(v || "")); if (!m) return null;
  const c = await env.DB.prepare("SELECT * FROM tcand WHERE id = ?1").bind(m[1]).first();
  if (!c || c.tok.length !== m[2].length) return null;
  let d = 0; for (let i = 0; i < m[2].length; i++) d |= c.tok.charCodeAt(i) ^ m[2].charCodeAt(i);   // the same time whatever the code
  return d ? null : c;
}
const talLink = (c, kind) => SITE + "/equipo/" + kind + "/?t=" + c.id + "." + c.tok;

/* ---------- the AI: scores with the job's rubric. It never sees the name, the email, the phone or the city ---------- */
async function talAsk(env, sys, user, schema) {
  const s = await socCfg(env); if (!s.aiKey) { const e = new Error("noai"); e.code = "noai"; throw e; }
  const r = await fetch("https://api.anthropic.com/v1/messages", { method: "POST", headers: { "x-api-key": s.aiKey, "anthropic-version": "2023-06-01", "content-type": "application/json" },
    body: JSON.stringify({ model: s.model || "claude-sonnet-5-5", max_tokens: 1800, system: sys, messages: [{ role: "user", content: user }], tools: [{ name: "puntuar", description: "Entrega la evaluación.", input_schema: schema }], tool_choice: { type: "tool", name: "puntuar" } }),
    signal: AbortSignal.timeout(60000) });
  const j = await r.json().catch(() => ({}));
  if (!r.ok) { const e = new Error("ai: " + ((j.error && j.error.message) || r.status)); e.code = "ai"; throw e; }
  const tu = (j.content || []).find((x) => x.type === "tool_use"); if (!tu || !tu.input) { const e = new Error("ai: sin respuesta"); e.code = "ai"; throw e; }
  return { o: tu.input, model: s.model || "claude-sonnet-5-5" };
}
const TAL_SYS = "Eres el asistente de selección de 404 Growth, una empresa pequeña que pasa tiendas físicas de España a tienda online en 15 días y después las hace vender con anuncios y email marketing. " +
  "Evalúas con una rúbrica, con criterio exigente y justo, como lo haría un responsable de selección muy bueno. Reglas: puntúa solo lo que la persona ha escrito o enlazado; no supongas lo que no dice; " +
  "un enlace que no puedes abrir no suma ni resta por sí solo, pero sí lo que la persona cuenta de él; no tengas en cuenta nada personal (edad, género, origen, nacionalidad, estado civil, salud, ni nada parecido), solo la experiencia, el trabajo y cómo escribe; " +
  "las faltas de ortografía cuentan solo en «comunicación» o «escritura». Escribe en español de España, frases cortas y concretas, sin adornos. Entrega el resultado llamando a la herramienta «puntuar».";
function talRubric(rb) { return rb.map((r) => "- " + r.id + " · " + r.name + " (peso " + r.w + "): " + (r.d || "") + (r.a0 ? " | 0: " + r.a0 + " | 3: " + r.a3 + " | 5: " + r.a5 : "")).join("\n"); }
const talSchema = (ids) => ({ type: "object", required: ["scores", "summary", "rec"], properties: {
  scores: { type: "array", items: { type: "object", required: ["id", "score", "why"], properties: { id: { type: "string", enum: ids }, score: { type: "integer", minimum: 0, maximum: 5 }, why: { type: "string" } } } },
  summary: { type: "string" }, strengths: { type: "array", items: { type: "string" } }, risks: { type: "array", items: { type: "string" } },
  rec: { type: "string", enum: ["avanzar", "dudoso", "no encaja"] }, questions: { type: "array", items: { type: "string" } } } });
function talTotal(rb, scores) {
  const by = {}; for (const s of scores || []) if (s && typeof s.id === "string") by[s.id] = s;
  let t = 0, w = 0; const out = [];
  for (const r of rb) { const s = by[r.id], v = s ? Math.max(0, Math.min(5, Math.round(Number(s.score) || 0))) : 0; t += r.w * v / 5; w += r.w; out.push({ id: r.id, name: r.name, w: r.w, score: v, why: s ? str(s.why, 300) : "" }); }
  return { total: w ? Math.round(t * 100 / w) : 0, scores: out };
}
const talList = (x, n, m) => (Array.isArray(x) ? x : []).map((v) => str(v, m || 240)).filter(Boolean).slice(0, n);
async function talScore(env, id, quiet) {
  await talReady(env);
  const c = await env.DB.prepare("SELECT * FROM tcand WHERE id = ?1").bind(id).first(); if (!c) return null;
  const j = talJob(c.job); if (!j) return null;
  const d = parse(c.data, {}) || {}, a = d.a || {}, ko = parse(c.ko, []) || [];
  // the LinkedIn address usually carries the name: the AI only learns whether there is one
  const qa = talQs(j).filter((q) => !["name", "email", "phone", "city", "cv", "src"].includes(q.id)).map((q) => "· " + q.label + "\n" + (q.id === "video" && d.vid ? "(sí, ha grabado o subido su vídeo de presentación, que no ves)" : !a[q.id] ? "(sin responder)" : q.id === "linkedin" ? "(sí, ha enlazado su LinkedIn)" : (q.type === "url" ? "(enlace) " : "") + a[q.id])).join("\n\n");
  const user = "Puesto: " + j.title + "\n" + (j.role || []).join(" ") + "\n\nQué tendrá que hacer:\n- " + (j.resp || []).join("\n- ") + "\n\nRequisitos:\n- " + (j.req || []).join("\n- ") + (j.plus && j.plus.length ? "\nSe valora:\n- " + j.plus.join("\n- ") : "") +
    "\n\nRúbrica (puntúa cada criterio de 0 a 5; 0, 3 y 5 están descritos):\n" + talRubric(j.rubric) +
    "\n\nLa candidatura:\n" + qa + (c.cv ? "\n\n(Ha adjuntado su CV en PDF, que no ves.)" : "") +
    (ko.length ? "\n\nNo cumple estas condiciones eliminatorias: " + ko.map((k) => (talQs(j).find((q) => q.id === k) || {}).label || k).join("; ") + ". Tenlo en cuenta en la recomendación." : "") +
    "\n\nDevuelve: la nota de cada criterio con su porqué en una frase; un resumen de 2 frases; hasta 3 puntos fuertes y hasta 3 riesgos; la recomendación (avanzar, dudoso o no encaja); y hasta 3 preguntas para la entrevista que aclaren las dudas.";
  let ai;
  try {
    const r = await talAsk(env, TAL_SYS, user, talSchema(j.rubric.map((x) => x.id))), o = r.o, t = talTotal(j.rubric, o.scores);
    ai = { at: Date.now(), model: r.model, total: t.total, scores: t.scores, summary: str(o.summary, 600), strengths: talList(o.strengths, 3), risks: talList(o.risks, 3), rec: ["avanzar", "dudoso", "no encaja"].includes(o.rec) ? o.rec : "dudoso", questions: talList(o.questions, 3, 300) };
  } catch (e) { ai = { at: Date.now(), err: e.code === "noai" ? "noai" : "ai", detail: str(String(e.message || ""), 160) }; }
  await env.DB.prepare("UPDATE tcand SET ai = ?2, score = ?3 WHERE id = ?1").bind(id, JSON.stringify(ai), ai.total == null ? null : ai.total).run();
  if (!quiet) {
    try { await pushAll(env, { title: (c.dev ? "Prueba interna · " : "") + "Nueva candidatura · " + j.short + " · " + c.name, body: (ai.total != null ? ai.total + "/100 · " + ai.rec : "Sin nota de la IA") + (ko.length ? " · no cumple: " + ko.map((k) => ({ tz: "horario", lang: "idioma", ko1: "experiencia" })[k] || k).join(", ") : "") + (ai.summary ? ". " + ai.summary.slice(0, 160) : ""), tag: "tal" + id, url: "/admin#talento" }); } catch (e) {}
  }
  return ai;
}
async function talTestScore(env, id) {
  const c = await env.DB.prepare("SELECT * FROM tcand WHERE id = ?1").bind(id).first(); if (!c) return null;
  const j = talJob(c.job), t = parse(c.test, {}) || {}; if (!j || !j.test || !t.sub) return null;
  const rb = j.test.rubric.map((r) => Object.assign({ d: "" }, r));
  const user = "Puesto: " + j.title + "\nPrueba técnica: " + j.test.title + "\n" + j.test.brief.join("\n") + "\nQué tenía que entregar: " + j.test.deliver.join("; ") +
    "\n\nRúbrica (de 0 a 5 cada criterio):\n" + talRubric(rb) + "\n\nLo que ha entregado:\nEnlaces: " + ((t.sub.links || []).join(" · ") || "ninguno") + "\nTexto:\n" + (t.sub.text || "(sin texto)") +
    "\n\nSi lo importante está en enlaces que no puedes abrir, dilo en el resumen y puntúa solo lo que ves escrito. Devuelve la nota de cada criterio con su porqué, un resumen de 2 frases, la recomendación y hasta 3 preguntas para la entrevista.";
  let ai;
  try { const r = await talAsk(env, TAL_SYS, user, talSchema(rb.map((x) => x.id))), o = r.o, tt = talTotal(rb, o.scores);
    ai = { at: Date.now(), total: tt.total, scores: tt.scores, summary: str(o.summary, 600), rec: ["avanzar", "dudoso", "no encaja"].includes(o.rec) ? o.rec : "dudoso", questions: talList(o.questions, 3, 300) };
  } catch (e) { ai = { at: Date.now(), err: e.code === "noai" ? "noai" : "ai" }; }
  t.ai = ai;
  await env.DB.prepare("UPDATE tcand SET test = ?2 WHERE id = ?1").bind(id, JSON.stringify(t)).run();
  try { await pushAll(env, { title: (c.dev ? "Prueba interna · " : "") + "Prueba entregada · " + j.short + " · " + c.name, body: (ai.total != null ? "La IA le da " + ai.total + "/100 (" + ai.rec + "). " + (ai.summary || "").slice(0, 140) : "Mírala tú: la IA no pudo puntuarla."), tag: "talt" + id, url: "/admin#talento" }); } catch (e) {}
  return ai;
}

/* ---------- the messages of each stage: by email from hola@ when there is a key; otherwise ready for WhatsApp ---------- */
function talMsg(c, kind) {
  const j = talJob(c.job) || { title: "", short: "" }, n = talFirst(c.name), t = parse(c.test, {}) || {}, d = parse(c.data, {}) || {};
  const due = t.due ? new Date(t.due).toLocaleDateString("es-ES", { timeZone: CAL_TZ, weekday: "long", day: "numeric", month: "long" }) : "";
  const M = {
    got: ["Hemos recibido tu candidatura · " + j.title, ["Hola " + n + ", gracias por escribirnos para el puesto de " + j.title + ".", "Te contestamos en menos de 24 horas. Si encajas, el siguiente paso es una videollamada de 30 minutos conmigo."], null],
    test: ["Tu prueba técnica para " + j.title, ["Hola " + n + ", gracias por la entrevista: me ha gustado hablar contigo y ahora quiero ver cómo trabajas.", "Aquí tienes la prueba técnica: " + (j.test ? j.test.hours + (j.test.hours === 1 ? " hora" : " horas") + " como máximo" : "corta") + (due ? ", con plazo hasta el " + due : "") + ". Si tienes cualquier duda, contesta a este mensaje."], [talLink(c, "prueba"), "Ver la prueba"]],
    meet: ["Hablamos 30 minutos · " + j.title, ["Hola " + n + ", gracias por tu candidatura para " + j.title + ": nos ha gustado.", "El siguiente paso es una videollamada de 30 minutos conmigo. Elige el día y la hora que mejor te vengan:"], [talLink(c, "entrevista"), "Elegir día y hora"]],
    trial: ["Te proponemos una semana de prueba", ["Hola " + n + ", tu prueba técnica me ha gustado mucho.", "Te propongo una semana de prueba, pagada y con trabajo real. Te escribo ahora con los detalles: qué haremos, cuánto se paga y cómo mediremos la semana."], null],
    hired: ["Te damos la bienvenida a 404 Growth", ["Hola " + n + ", ¡ya formas parte del equipo de 404 Growth!", "En las próximas horas te llegan los accesos, el manual de procesos y tu plan de 30, 60 y 90 días. Cualquier cosa, me escribes."], null],
    bank: ["Tu candidatura para " + j.title, ["Hola " + n + ", gracias por tu candidatura para " + j.title + ".", c.keep ? "Ahora seguimos con otras personas, pero tu perfil nos ha gustado y lo guardamos en nuestro banco de talento: te escribiremos en cuanto abramos algo que encaje contigo." : "Ahora seguimos con otras personas, pero tu perfil nos ha gustado. ¿Quieres que guardemos tu candidatura para futuros puestos? Contesta «sí» y te escribiremos en cuanto abramos algo que encaje contigo."], null],
    no: ["Tu candidatura para " + j.title, ["Hola " + n + ", gracias por tu tiempo y por tu candidatura para " + j.title + ".", "Esta vez no vamos a seguir adelante contigo. Te deseamos lo mejor y, si las cosas cambian, vuelve a escribirnos cuando quieras."], null],
  }[kind];
  if (!M) return null;
  const text = M[1].join("\n\n") + (M[2] ? "\n\n" + M[2][0] : "") + "\n\nUn abrazo,\nChristian · 404 Growth";
  const phone = String(c.phone || "").replace(/[^\d]/g, "");
  return { kind, subject: M[0], text, to: c.email, wa: phone ? "https://wa.me/" + phone + "?text=" + encodeURIComponent(text) : "", html: mailShell(M[0], M[1], M[2] ? [[M[2][0], M[2][1], true]] : [], "") };
}
async function talSend(env, c, kind, send, via) {
  const m = talMsg(c, kind); if (!m) return null;
  let sent = "";
  if (send && !via) { const r = await sendMail(env, c.email, m.subject, m.html, m.text); if (r.ok) sent = "email"; }
  if (via === "wa") sent = "wa";
  if (sent) { const L = parse(c.msgs, []) || []; L.push({ k: kind, at: Date.now(), via: sent }); await env.DB.prepare("UPDATE tcand SET msgs = ?2 WHERE id = ?1").bind(c.id, JSON.stringify(L.slice(-40))).run(); }
  return { kind: m.kind, subject: m.subject, text: m.text, wa: m.wa, to: m.to, sent };
}

/* ---------- the public side: /l/jobs, /l/job, /l/jobcv, /l/jobt, /l/jobts, /l/jobm, /l/jobmb ---------- */
async function talPublic(req, env, ctx, p) {
  await talReady(env);
  const H = { "access-control-allow-origin": SITE };
  if (p === "jobs" && req.method === "GET") return json({ open: await talOpen(env), vid: !!env.TV, vmax: TAL_VMAX }, 200, Object.assign({ "cache-control": "public, max-age=60" }, H));
  if (req.method !== "POST" && !(p === "jobvp" && req.method === "PUT")) return bad("method", 405);
  const o = req.headers.get("origin"); if (!o || !origins(env).includes(o)) return bad("origin", 403);
  const now = Date.now(), DBq = env.DB, later = (pr) => { if (ctx && ctx.waitUntil) ctx.waitUntil(pr.catch(() => {})); else return pr.catch(() => {}); };
  if (p === "jobvp") {   // one part of the video, straight to R2
    if (req.method !== "PUT") return bad("method", 405);
    if (!env.TV) return bad("novid", 503);
    const u = new URL(req.url), k = u.searchParams.get("k") || "", t = u.searchParams.get("t") || "", n = Number(u.searchParams.get("n"));
    if (!TAL_VK.test(k) || !TAL_VT.test(t) || !Number.isInteger(n) || n < 1) return bad("missing", 404);
    const v = await DBq.prepare("SELECT * FROM tvid WHERE k = ?1").bind(k).first();
    if (!v || !talSame(v.tok, t) || v.done || v.cid || now - v.ts > DAY) return bad("missing", 404);
    if (n > Math.ceil(v.size / TAL_VPART)) return bad("part", 400);
    const len = Number(req.headers.get("content-length") || 0);
    if (!len || len > TAL_VPART) return bad("big", 413);
    try { const part = await env.TV.resumeMultipartUpload(k, v.up).uploadPart(n, req.body); return json({ ok: true, n, etag: part.etag }); }
    catch (e) { return bad("part", 502); }
  }
  if (p === "jobcv") {
    const c = await talByTok(env, new URL(req.url).searchParams.get("c")); if (!c) return bad("missing", 404);
    if (c.cv || now - c.ts > 3600000) return bad("late", 409);
    const len = Number(req.headers.get("content-length") || 0); if (len > TAL_CV) return bad("big", 413);
    const buf = new Uint8Array(await req.arrayBuffer());
    if (buf.length > TAL_CV) return bad("big", 413);
    if (!(buf.length > 4 && buf[0] === 0x25 && buf[1] === 0x50 && buf[2] === 0x44 && buf[3] === 0x46)) return bad("type", 415);
    await DBq.batch([DBq.prepare("INSERT OR REPLACE INTO tcvf (id, data, size) VALUES (?1, ?2, ?3)").bind(c.id, buf, buf.length), DBq.prepare("UPDATE tcand SET cv = 1 WHERE id = ?1").bind(c.id)]);
    return json({ ok: true });
  }
  const b = await body(req, 40000); if (!b) return bad("body");
  if (p === "jobv") {
    if (!env.TV) return bad("novid", 503);
    if (b.a === "start") {
      const j = talJob(typeof b.job === "string" ? b.job : ""); if (!j) return bad("job", 404);
      if (!(await talOpen(env))[j.slug]) return bad("closed", 409);
      const size = Math.floor(Number(b.size) || 0), type = (str(b.type, 80).toLowerCase().split(";")[0] || "video/mp4").trim();
      if (size < 20000) return bad("small", 400);
      if (size > TAL_VMAX) return bad("big", 413);
      if (!/^video\/[a-z0-9.+-]{2,40}$/.test(type)) return bad("type", 415);
      const ih = (await sha("tal|" + (req.headers.get("cf-connecting-ip") || "local"))).slice(0, 22);
      const many = await DBq.prepare("SELECT COUNT(*) AS n FROM tvid WHERE ih = ?1 AND ts > ?2").bind(ih, now - DAY).first();
      if (many && many.n >= TAL_VDAY) return bad("slow", 429);
      const iso = new Date(now).toISOString(), k = "v/" + iso.slice(2, 4) + iso.slice(5, 7) + iso.slice(8, 10) + "/" + (rid("") + rid("")).slice(0, 18), tok = (rid("") + rid("")).slice(0, 16);
      let mu; try { mu = await env.TV.createMultipartUpload(k, { httpMetadata: { contentType: type }, customMetadata: { job: j.slug } }); } catch (e) { return bad("novid", 503); }
      await DBq.prepare("INSERT INTO tvid (k, up, tok, ts, size, type, dur, src, ih, job) VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, ?8, ?9, ?10)")
        .bind(k, mu.uploadId, tok, now, size, type, Math.min(900, Math.max(0, Number(b.dur) || 0)), b.src === "rec" ? "rec" : "file", ih, j.slug).run();
      return json({ ok: true, k, t: tok, ps: TAL_VPART, parts: Math.ceil(size / TAL_VPART) });
    }
    const k = typeof b.k === "string" ? b.k : "", t = typeof b.t === "string" ? b.t : "";
    if (!TAL_VK.test(k) || !TAL_VT.test(t)) return bad("missing", 404);
    const v = await DBq.prepare("SELECT * FROM tvid WHERE k = ?1").bind(k).first();
    if (!v || !talSame(v.tok, t) || v.cid) return bad("missing", 404);
    if (b.a === "abort") {
      try { if (v.done) await env.TV.delete(k); else await env.TV.resumeMultipartUpload(k, v.up).abort(); } catch (e) {}
      await DBq.prepare("DELETE FROM tvid WHERE k = ?1").bind(k).run();
      return json({ ok: true });
    }
    if (b.a === "done") {
      if (v.done) return json({ ok: true, vk: k + "|" + t, size: v.size });
      const parts = (Array.isArray(b.parts) ? b.parts : []).map((x) => ({ partNumber: Math.floor(Number(x && x.n)), etag: str(x && x.etag, 200) })).filter((x) => x.partNumber >= 1 && x.etag).sort((x, y) => x.partNumber - y.partNumber);
      if (parts.length !== Math.ceil(v.size / TAL_VPART) || parts.some((x, i) => x.partNumber !== i + 1)) return bad("parts", 400);
      let obj; try { obj = await env.TV.resumeMultipartUpload(k, v.up).complete(parts); } catch (e) { return bad("parts", 400); }
      const size = obj && obj.size ? obj.size : v.size;
      if (size > TAL_VMAX) { try { await env.TV.delete(k); } catch (e) {} await DBq.prepare("DELETE FROM tvid WHERE k = ?1").bind(k).run(); return bad("big", 413); }
      await DBq.prepare("UPDATE tvid SET done = 1, size = ?2 WHERE k = ?1").bind(k, size).run();
      return json({ ok: true, vk: k + "|" + t, size });
    }
    return bad("missing", 404);
  }
  if (p === "job") {
    const j = talJob(typeof b.job === "string" ? b.job : ""); if (!j) return bad("job", 404);
    if (!(await talOpen(env))[j.slug]) return bad("closed", 409);
    if (b.web) return json({ ok: true, id: "Tok" });                                          // the hidden field: only robots fill it
    if (b.consent !== true) return bad("consent");
    let vrow = null;   // the video uploaded from the page (k|token), if any
    if (env.TV && typeof b.vk === "string") { const vm = /^(v\/\d{6}\/[A-Za-z0-9_-]{8,24})\|([A-Za-z0-9_-]{16})$/.exec(b.vk); if (vm) { const v = await DBq.prepare("SELECT * FROM tvid WHERE k = ?1").bind(vm[1]).first(); if (v && v.done && !v.cid && v.job === j.slug && talSame(v.tok, vm[2])) vrow = v; } }
    const ck = talCheck(j, b.a, !!vrow); if (ck.err.length) return json({ error: "fields", fields: ck.err }, 400);
    const ih = (await sha("tal|" + (req.headers.get("cf-connecting-ip") || "local"))).slice(0, 22);
    const many = await DBq.prepare("SELECT COUNT(*) AS n FROM tcand WHERE ih = ?1 AND ts > ?2").bind(ih, now - DAY).first();
    if (many && many.n >= TAL_DAYMAX) return bad("slow", 429);
    const dev = b.dev === 1 || b.dev === true ? 1 : 0;   // prueba interna: se puede repetir
    const dup = dev ? null : await DBq.prepare("SELECT id FROM tcand WHERE job = ?1 AND email = ?2 AND ts > ?3 AND dev = 0").bind(j.slug, ck.a.email, now - 30 * DAY).first();
    if (dup) return bad("dup", 409);
    const utm = {}; if (b.utm && typeof b.utm === "object") for (const k of ["utm_source", "utm_medium", "utm_campaign", "utm_content"]) { const v = str(b.utm[k], 80); if (v) utm[k] = v; }
    const id = "T" + rid(""), tok = (rid("") + rid("")).slice(0, 16);
    const data = { a: ck.a, utm, ref: str(b.ref, 200), ua: str(req.headers.get("user-agent") || "", 160) };
    if (vrow) data.vid = { k: vrow.k, size: vrow.size, type: vrow.type, dur: vrow.dur || 0, src: vrow.src || "file" };
    await DBq.prepare("INSERT INTO tcand (id, job, ts, upd, stage, name, email, phone, city, data, ko, tok, ih, keep, dev) VALUES (?1, ?2, ?3, ?3, 'new', ?4, ?5, ?6, ?7, ?8, ?9, ?10, ?11, ?12, ?13)")
      .bind(id, j.slug, now, ck.a.name, ck.a.email, ck.a.phone || "", ck.a.city || "", JSON.stringify(data), JSON.stringify(ck.ko), tok, ih, b.keep ? 1 : 0, dev).run();
    if (vrow) await DBq.prepare("UPDATE tvid SET cid = ?2 WHERE k = ?1").bind(vrow.k, id).run();
    const c = await DBq.prepare("SELECT * FROM tcand WHERE id = ?1").bind(id).first();
    await later((async () => { try { await talSend(env, c, "got", true); } catch (e) {} await talScore(env, id); })());
    return json({ ok: true, id, cvt: id + "." + tok, dev: !!dev });
  }
  const c = await talByTok(env, b.t); if (!c) return bad("missing", 404);
  const j = talJob(c.job); if (!j) return bad("missing", 404);
  if (p === "jobt" || p === "jobts") {
    const t = parse(c.test, null); if (!j.test || !t || !t.sent) return bad("closed", 409);
    if (p === "jobt") return json({ ok: true, name: talFirst(c.name), job: j.title, test: j.test, due: t.due || null, done: t.sub ? t.sub.ts : null, dev: !!c.dev });
    if (["no", "hired"].includes(c.stage)) return bad("closed", 409);
    const links = (Array.isArray(b.links) ? b.links : []).map(talUrl).filter(Boolean).slice(0, 6), text = str(b.text, 8000);
    if (!links.length && text.length < 30) return bad("fields");
    t.sub = { ts: now, links, text, late: t.due && now > t.due ? 1 : 0 }; delete t.ai;
    await DBq.prepare("UPDATE tcand SET test = ?2, stage = CASE WHEN stage IN ('new', 'short', 'test') THEN 'testd' ELSE stage END, upd = ?3 WHERE id = ?1").bind(c.id, JSON.stringify(t), now).run();
    await later(talTestScore(env, c.id));
    return json({ ok: true });
  }
  if (p === "jobm" || p === "jobmb") {
    if (!["meet", "test", "testd", "trial"].includes(c.stage) && !parse(c.meet, null)) return bad("closed", 409);
    const mt = parse(c.meet, {}) || {};
    if (p === "jobm") { let slots = []; try { slots = await gbSlots(env, false); } catch (e) { return json({ error: "nocal" }, 503); } return json({ ok: true, name: talFirst(c.name), job: j.title, dur: GB_DUR, tz: CAL_TZ, slots, booked: mt.start ? { start: mt.start, join: mt.join || "" } : null, dev: !!c.dev }); }
    if (mt.start && mt.start > now) return bad("booked", 409);
    const start = typeof b.start === "string" ? b.start : "", s = Date.parse(start);
    let slots; try { slots = await gbSlots(env, true); } catch (e) { return json({ error: "nocal" }, 503); }
    if (!slots.some((x) => Date.parse(x) === s)) return json({ error: "taken", slots }, 409);
    if (c.dev) {   // prueba interna: todo el recorrido, sin evento en Google ni invitación
      const m0 = { start: s, join: "", gid: "", at: now, dry: 1 };
      await DBq.prepare("UPDATE tcand SET meet = ?2, upd = ?3 WHERE id = ?1").bind(c.id, JSON.stringify(m0), now).run();
      try { await pushAll(env, { title: "Prueba interna · Entrevista reservada · " + c.name, body: j.title + " · " + vslWhen(new Date(s).toISOString(), CAL_TZ) + ". Es una prueba: no se ha creado el evento en Google.", tag: "talm" + c.id, url: "/admin#talento" }); } catch (e) {}
      return json({ ok: true, start: new Date(s).toISOString(), join: "", dev: true });
    }
    const notes = "Entrevista para " + j.title + ".\nCandidatura: " + SITE + "/admin#talento";
    let g; try { g = await gbCreate(env, { s, e: s + GB_DUR * 60000, name: c.name, email: c.email, biz: j.short, summary: "Entrevista 404 Growth · " + j.title + " · " + c.name, title: "Entrevista · " + c.name + " (" + j.short + ")", notes: "Videollamada de 30 minutos con Christian sobre el puesto de " + j.title + ".", inner: notes }); }
    catch (e) { return json({ error: e.code === "nogoogle" ? "nocal" : "book" }, 502); }
    const m2 = { start: s, join: g.join || "", gid: g.id || "", at: now };
    await DBq.prepare("UPDATE tcand SET meet = ?2, upd = ?3 WHERE id = ?1").bind(c.id, JSON.stringify(m2), now).run();
    try { await pushAll(env, { title: "Entrevista reservada · " + c.name, body: j.title + " · " + vslWhen(new Date(s).toISOString(), CAL_TZ) + ". Google le ha mandado la invitación con el Meet.", tag: "talm" + c.id, url: "/admin#talento" }); } catch (e) {}
    return json({ ok: true, start: new Date(s).toISOString(), join: m2.join });
  }
  return bad("missing", 404);
}

/* ---------- the admin side: /admin/api/tal… ---------- */
async function talApi(req, env, p, ctx) {
  await talReady(env);
  const m = req.method, DBq = env.DB, now = Date.now();
  if (p === "tal" && m === "GET") {
    // RGPD: what nobody has touched in 6 months goes (12 if they let us keep it), except the people in the team
    await DBq.batch([DBq.prepare("DELETE FROM tcvf WHERE id IN (SELECT id FROM tcand WHERE stage NOT IN ('hired', 'trial') AND ((keep = 0 AND upd < ?1) OR (keep = 1 AND upd < ?2)))").bind(now - 182 * DAY, now - 365 * DAY),
      DBq.prepare("DELETE FROM tcand WHERE stage NOT IN ('hired', 'trial') AND ((keep = 0 AND upd < ?1) OR (keep = 1 AND upd < ?2))").bind(now - 182 * DAY, now - 365 * DAY)]);
    try { await talVidSweep(env, now); } catch (e) {}
    const rows = (await DBq.prepare("SELECT id, job, ts, upd, stage, name, city, score, ai, ko, keep, cv, seen, test, meet, dev, (json_extract(data, '$.vid.k') IS NOT NULL) AS vid FROM tcand ORDER BY ts DESC LIMIT 2000").all()).results || [];
    const s = await socCfg(env), open = await talOpen(env);
    return json({ jobs: (TAL.jobs || []).map((j) => ({ slug: j.slug, title: j.title, short: j.short, open: open[j.slug], test: !!j.test })), stages: TAL.stages, cands: rows.map(talRow), mail: !!(await getMeta(env, "nl_key")), ai: !!s.aiKey });
  }
  if (p === "taldev" && m === "DELETE") {   // borrar todas las pruebas internas
    await DBq.batch([DBq.prepare("DELETE FROM tcvf WHERE id IN (SELECT id FROM tcand WHERE dev = 1)"), DBq.prepare("DELETE FROM tcand WHERE dev = 1")]);
    try { await talVidSweep(env, now); } catch (e) {}
    return json({ ok: true });
  }
  const tj = /^taljob\/([a-z]{3,20})$/.exec(p);
  if (tj && m === "POST") {
    if (!talJob(tj[1])) return bad("missing", 404);
    const b = await body(req); if (!b) return bad("body");
    const o = parse(await getMeta(env, "tal_open"), {}) || {}; o[tj[1]] = !!b.open; await setMeta(env, "tal_open", JSON.stringify(o));
    return json({ ok: true, open: await talOpen(env) });
  }
  const q = /^tal\/(T[A-Za-z0-9_-]{8,16})(?:\/(ai|cv|msg|video))?$/.exec(p); if (!q) return bad("missing", 404);
  let c = await DBq.prepare("SELECT * FROM tcand WHERE id = ?1").bind(q[1]).first(); if (!c) return bad("missing", 404);
  const j = talJob(c.job);
  if (q[2] === "cv" && m === "GET") {
    const f = await DBq.prepare("SELECT data FROM tcvf WHERE id = ?1").bind(c.id).first(); if (!f) return bad("missing", 404);
    const name = "CV " + String(c.name).replace(/[^\p{L}\p{N} ._-]/gu, "").slice(0, 60) + ".pdf";
    return new Response(f.data instanceof Uint8Array ? f.data : new Uint8Array(f.data), { headers: Object.assign({ "content-type": "application/pdf", "content-disposition": "inline; filename*=UTF-8''" + encodeURIComponent(name), "cache-control": "private, no-store" }, SEC) });
  }
  if (q[2] === "video" && m === "GET") {   // the selfie video, with byte ranges (Safari needs them to play it)
    const v = (parse(c.data, {}) || {}).vid; if (!v || !v.k || !env.TV) return bad("missing", 404);
    const hd = await env.TV.head(v.k); if (!hd) return bad("missing", 404);
    const size = hd.size, type = (hd.httpMetadata && hd.httpMetadata.contentType) || v.type || "video/mp4";
    let a = 0, z = size - 1, part = false;
    const rg = /^bytes=(\d*)-(\d*)$/.exec(req.headers.get("range") || "");
    if (rg && (rg[1] || rg[2])) {
      if (rg[1]) { a = Number(rg[1]); z = rg[2] ? Math.min(Number(rg[2]), size - 1) : size - 1; } else { a = Math.max(0, size - Number(rg[2])); }
      if (a > z || a >= size) return new Response(null, { status: 416, headers: { "content-range": "bytes */" + size } });
      part = true;
    }
    const obj = await env.TV.get(v.k, part ? { range: { offset: a, length: z - a + 1 } } : undefined); if (!obj) return bad("missing", 404);
    const ext = /quicktime/.test(type) ? "mov" : /webm/.test(type) ? "webm" : "mp4";
    const hh = Object.assign({ "content-type": type, "accept-ranges": "bytes", "content-length": String(z - a + 1), "cache-control": "private, max-age=3600" }, SEC);
    if (part) hh["content-range"] = "bytes " + a + "-" + z + "/" + size;
    if (new URL(req.url).searchParams.get("dl")) hh["content-disposition"] = "attachment; filename*=UTF-8''" + encodeURIComponent("Vídeo " + String(c.name).replace(/[^\p{L}\p{N} ._-]/gu, "").slice(0, 60) + "." + ext);
    return new Response(obj.body, { status: part ? 206 : 200, headers: hh });
  }
  if (q[2] === "ai" && m === "POST") { const ai = await talScore(env, c.id, true); return json({ ok: true, ai }); }
  if (q[2] === "msg" && m === "POST") {
    const b = await body(req) || {}; const kind = typeof b.kind === "string" ? b.kind : c.stage;
    const r = await talSend(env, c, kind, !!b.send, b.via === "wa" ? "wa" : ""); if (!r) return bad("kind");
    return json({ ok: true, msg: r });
  }
  if (!q[2] && m === "GET") {
    if (!c.seen) await DBq.prepare("UPDATE tcand SET seen = 1 WHERE id = ?1").bind(c.id).run();
    const d = parse(c.data, {}) || {};
    return json({ cand: Object.assign(talRow(c), { email: c.email, phone: c.phone || "", data: d, ai: parse(c.ai, null), testFull: parse(c.test, null), meetFull: parse(c.meet, null), msgs: parse(c.msgs, []) || [], notes: c.notes || "",
      links: { test: j && j.test ? talLink(c, "prueba") : "", meet: talLink(c, "entrevista") } }),
      qs: j ? talQs(j).map((x) => ({ id: x.id, label: x.label, type: x.type })) : [], job: j ? { slug: j.slug, title: j.title, short: j.short, test: j.test ? { title: j.test.title, days: j.test.days, hours: j.test.hours } : null, rubric: j.rubric.map((r) => ({ id: r.id, name: r.name, w: r.w })) } : null });
  }
  if (!q[2] && m === "DELETE") { await DBq.batch([DBq.prepare("DELETE FROM tcvf WHERE id = ?1").bind(c.id), DBq.prepare("DELETE FROM tcand WHERE id = ?1").bind(c.id)]); try { await talVidSweep(env, now); } catch (e) {} return json({ ok: true }); }
  if (!q[2] && m === "POST") {
    const b = await body(req, 20000); if (!b) return bad("body");
    const st = [], set = (sql, ...v) => st.push(DBq.prepare(sql).bind(...v));
    if (typeof b.notes === "string") set("UPDATE tcand SET notes = ?2 WHERE id = ?1", c.id, str(b.notes, 6000));
    if (b.keep !== undefined) set("UPDATE tcand SET keep = ?2 WHERE id = ?1", c.id, b.keep ? 1 : 0);
    let moved = "";
    if (typeof b.stage === "string" && b.stage !== c.stage) {
      if (!TAL_ST.includes(b.stage)) return bad("stage");
      if (b.stage === "test" && !(j && j.test)) return bad("notest");
      moved = b.stage; set("UPDATE tcand SET stage = ?2, upd = ?3 WHERE id = ?1", c.id, b.stage, now);
      if (b.stage === "test") { const t = parse(c.test, {}) || {}; if (!t.sent) { t.sent = now; t.due = now + ((j.test.days || 4) * DAY); set("UPDATE tcand SET test = ?2 WHERE id = ?1", c.id, JSON.stringify(t)); } }
    }
    if (st.length) await DBq.batch(st);
    c = await DBq.prepare("SELECT * FROM tcand WHERE id = ?1").bind(c.id).first();
    let msg = null; if (moved && b.send !== false) msg = await talSend(env, c, moved, true);
    return json({ ok: true, cand: talRow(c), msg });
  }
  return bad("missing", 404);
}
