
/* ---------- v30: proposal intelligence (27 oct 2026) ----------
   Asked: «ampliar el traqueo de las acciones que hacen» each prospect inside the proposal. The counter v3 (VIS) adds, per visit, the
   context (device, browser, system, screen, language, zone; approximate city, region and network from Cloudflare; never the IP), active
   time, scroll %, seconds per section, typed events (table e), a traffic classification with its confidence, and robots apart (table b).
   Here: the interest score of each proposal (0-100, with its factors, weights in meta «intel_w», and how sure it is), possible extra
   readers (said with care: a different device is not proof the link was forwarded), alerts (table palerts, one per reason, settings in
   meta «alert_cfg»), the activity feed, manual correction of a classification, export and deletion of one proposal's data, retention.
   Observed data (v, c, e) and what is inferred from them (score, readers, alerts) are kept apart: the inferences are worked out when
   asked, or stored only as alerts with their reason. */
const V30_DDL = [
  "CREATE TABLE IF NOT EXISTS palerts (id INTEGER PRIMARY KEY AUTOINCREMENT, ts INTEGER NOT NULL, slug TEXT NOT NULL, kind TEXT NOT NULL, dk TEXT NOT NULL, title TEXT, body TEXT, url TEXT, visit INTEGER, pushed INTEGER NOT NULL DEFAULT 0, seen INTEGER NOT NULL DEFAULT 0)",
  "CREATE UNIQUE INDEX IF NOT EXISTS palerts_dk ON palerts (slug, kind, dk)",
  "CREATE INDEX IF NOT EXISTS palerts_ts ON palerts (ts)",
  "CREATE TABLE IF NOT EXISTS adminlog (id INTEGER PRIMARY KEY AUTOINCREMENT, ts INTEGER NOT NULL, what TEXT NOT NULL, detail TEXT)"];
async function v30Ready(env) {
  if (v30Ready.ok) return;
  for (const q of V30_DDL) await env.DB.prepare(q).run();
  v30Ready.ok = true;
}
const ACFG = { entry: 1, contact: 1, meeting: 1, docs: 1, high: 1, highAt: 60, reader: 1, idle: 0, idleDays: 5, retDays: 365 };
const IW = { ret: 8, retMax: 24, minPts: 3, minMax: 25, scroll: 10, price: 10, priceAgain: 5, parts: 5, web: 8, contact: 15, meeting: 20, docs: 5, docsMax: 10, video: 3, reader: 5 };
async function acfgOf(env) { const o = parse(await getMeta(env, "alert_cfg"), {}); const c = {}; for (const k of Object.keys(ACFG)) c[k] = typeof o[k] === "number" && isFinite(o[k]) ? o[k] : ACFG[k]; return c; }
async function iwOf(env) { const o = parse(await getMeta(env, "intel_w"), {}); const c = {}; for (const k of Object.keys(IW)) c[k] = typeof o[k] === "number" && isFinite(o[k]) && o[k] >= 0 && o[k] <= 100 ? o[k] : IW[k]; return c; }
const tcOf = (v) => v.tcm || v.tc || "";   // a manual correction wins; old visits (before v3) have none
const isHuman = (v) => { const t = tcOf(v); return !t || t === "human_likely" || t === "unknown"; };
function clickKind(h) {
  h = String(h || "");
  if (/calendly|cal\.com|zcal|savvycal|^\/llamada|hubspot\.com\/meetings|meet\.google|zoom\.us/i.test(h)) return "meeting";
  if (/^wa\.me|whatsapp|^tel:|^mailto:|instagram|ig\.me|m\.me|t\.me/i.test(h)) return "contact";
  if (/^\/p\/[^/]+\/web\/?$/.test(h)) return "web";
  return "";
}
const contactName = (h) => /^wa\.me|whatsapp/i.test(h) ? "WhatsApp" : /^tel:/i.test(h) ? "llamar" : /^mailto:/i.test(h) ? "el email" : /instagram|ig\.me/i.test(h) ? "Instagram" : /calendly|cal\.com|zcal|savvycal|hubspot|meet\.google|zoom/i.test(h) ? "reservar una reunión" : /^\/llamada/i.test(h) ? "pedir una llamada" : "contacto";
const PRICE_RE = /incluye|precio|tarifa|plan(es)?\b|oferta|inversi|garant|condicion|cuota|presupuesto|pricing|price|package|paquete/i;
const PART_RE = /reels|contenido|p-web|web|asistente|crm|cliente|video|whatsapp|sistema|entregable/i;
function devLabel(v) {
  const d = v.dv || (v.dev === "d" ? "d" : v.dev === "m" ? "m" : "?");
  return [{ m: "Móvil", t: "Tablet", d: "Ordenador" }[d] || "Dispositivo", v.os && v.os !== "Desconocido" ? v.os.replace(/ [\d.\/]+$/, "") : "", v.br && v.br !== "Desconocido" ? v.br.replace(/ \d+$/, "") : ""].filter(Boolean).join(" · ");
}
const devSig = (v) => [v.dv || v.dev || "?", (v.os || "").split(" ")[0] || "?", (v.br || "").replace(/ \d+$/, "") || "?", (v.scr || "").split(" ·")[0] || "?"].join("|");

/* everything observed about one proposal (and its new web), then what it suggests */
async function intelOf(env, base, w) {
  w = w || await iwOf(env);
  const now = Date.now();
  const rows = (await env.VIS.prepare("SELECT * FROM v WHERE slug = ?1 OR slug = ?2 ORDER BY ts LIMIT 400").bind(base, base + "--web").all()).results || [];
  const keys = rows.map((v) => v.k);
  const nc = {}, clicks = [], evs = [];
  if (keys.length) {
    for (const r of (await env.VIS.prepare("SELECT k, h, w, s FROM c WHERE k IN (SELECT value FROM json_each(?1)) ORDER BY id LIMIT 3000").bind(JSON.stringify(keys)).all()).results || []) { nc[r.k] = (nc[r.k] || 0) + 1; clicks.push(r); }
    try { for (const r of (await env.VIS.prepare("SELECT k, y, s, l, n FROM e WHERE k IN (SELECT value FROM json_each(?1)) AND y IN ('sin','dl','print','copy','share','vplay','vend','form1','exp','tab') ORDER BY id LIMIT 4000").bind(JSON.stringify(keys)).all()).results || []) evs.push(r); } catch (e) { /* counter not on v3 yet */ }
  }
  const robots = rows.filter((v) => !isHuman(v));
  const hum = rows.filter(isHuman);
  const evn = {}; for (const e of evs) evn[e.k] = (evn[e.k] || 0) + 1;
  const real = (v) => (v.act != null ? v.act : v.secs) >= 5 || nc[v.k] || (evn[v.k] || 0) > 1;
  const props = hum.filter((v) => v.slug === base && real(v)), webs = hum.filter((v) => v.slug !== base && real(v));
  const out = { slug: base, visits: props.length, bounces: hum.filter((v) => v.slug === base && !real(v)).length, robots: robots.length, webVisits: webs.length,
    first: props.length ? props[0].ts : null, last: props.length ? props[props.length - 1].ts : null, act: 0, open: 0, sd: 0, depth: 0, sections: [], factors: [], readers: [], simultaneous: false,
    contacts: [], meetings: 0, downloads: 0, prints: 0, copies: 0, shares: 0, videos: 0, forms: 0, returns: 0, gaps: [] };
  if (!props.length && !webs.length) { out.score = 0; out.conf = robots.length ? "baja" : "sin datos"; out.why = robots.length ? "Solo la han abierto robots o escáneres." : "Nadie la ha abierto todavía."; return out; }
  const keyOf = new Set(props.concat(webs).map((v) => v.k));
  /* time, depth, sections */
  const secT = {}, labels = {};
  for (const v of props) {
    out.act += v.act != null ? v.act : v.secs; out.open += v.secs; out.sd = Math.max(out.sd, v.sd || 0); out.depth = Math.max(out.depth, v.depth || 0);
    const ss = parse(v.ss, {}); for (const [id, s] of Object.entries(ss)) secT[id] = (secT[id] || 0) + s;
  }
  for (const v of webs) out.act += v.act != null ? v.act : v.secs;
  for (const e of evs) if (e.y === "sin" && e.l && !labels[e.s]) labels[e.s] = e.l;
  out.sections = Object.entries(secT).sort((a, b) => b[1] - a[1]).slice(0, 20).map(([id, s]) => ({ id, label: labels[id] || id, secs: s }));
  /* returns: a visit that starts more than 30 min after the previous one ended */
  for (let i = 1; i < props.length; i++) { const prevEnd = props[i - 1].seen || props[i - 1].ts + props[i - 1].secs * 1000, gap = props[i].ts - prevEnd; if (gap > 30 * 60000) { out.returns++; out.gaps.push(gap); } }
  /* actions */
  const seenC = new Set();
  for (const c of clicks) { if (!keyOf.has(c.k)) continue; const k = clickKind(c.h); const id = c.k + ":" + contactName(c.h);
    if ((k === "contact" || k === "meeting") && !seenC.has(id)) { seenC.add(id); out.contacts.push(contactName(c.h)); if (k === "meeting") out.meetings++; } }
  for (const e of evs) { if (!keyOf.has(e.k)) continue; if (e.y === "dl") out.downloads++; else if (e.y === "print") out.prints++; else if (e.y === "copy") out.copies++; else if (e.y === "share") out.shares++; else if (e.y === "vplay") out.videos++; else if (e.y === "form1") out.forms++; }
  /* devices: possible extra readers, said with care */
  const groups = new Map();
  for (const v of props.concat(webs)) { const s = devSig(v); const g = groups.get(s) || { sig: s, label: devLabel(v), n: 0, first: v.ts, last: v.ts, asn: new Set(), city: new Set(), cc: new Set(), legacy: !v.br }; g.n++; g.last = v.ts; if (v.asn) g.asn.add(v.asn); if (v.ci) g.city.add(v.ci); if (v.cc) g.cc.add(v.cc); groups.set(s, g); }
  const G = [...groups.values()].sort((a, b) => a.first - b.first), main = G[0];
  for (const g of G) {
    let level = "principal", note = "el primero que la abrió";
    if (g !== main) {
      const sameNet = [...g.asn].some((a) => main.asn.has(a)), sameCity = [...g.city].some((c) => main.city.has(c));
      if (g.legacy || main.legacy) { level = "ambiguo"; note = "visitas antiguas sin detalle del dispositivo"; }
      else if (!sameNet && !sameCity && g.asn.size && main.asn.size) { level = "posible"; note = "otro dispositivo y otra red: puede ser otra persona, o la misma desde otro sitio"; }
      else { level = "ambiguo"; note = sameNet ? "otro dispositivo en la misma red: puede ser la misma persona o alguien de su equipo" : "otro dispositivo; no hay datos de red para comparar"; }
    }
    out.readers.push({ label: g.label, visits: g.n, first: g.first, last: g.last, level, note, place: [...g.city][0] || [...g.cc][0] || "" });
  }
  const all = props.concat(webs).map((v) => ({ s: devSig(v), a: v.ts, b: v.seen || v.ts + v.secs * 1000 }));
  for (let i = 0; i < all.length && !out.simultaneous; i++) for (let j = i + 1; j < all.length; j++) if (all[i].s !== all[j].s && all[i].a < all[j].b && all[j].a < all[i].b) { out.simultaneous = true; break; }
  /* the score: each factor once, capped, with its reason */
  const F = (k, pts, txt) => { pts = Math.round(pts * 10) / 10; if (pts > 0) out.factors.push({ k, pts, txt }); };
  F("ret", Math.min(w.retMax, out.returns * w.ret), out.returns ? "Ha vuelto " + out.returns + (out.returns === 1 ? " vez" : " veces") + " en otro momento" : "");
  F("time", Math.min(w.minMax, out.act / 60 * w.minPts), "Tiempo activo: " + Math.round(out.act / 6) / 10 + " min" + (out.open > out.act + 30 ? " (de " + Math.round(out.open / 6) / 10 + " min abierta)" : ""));
  F("scroll", (Math.max(out.sd, out.depth * 11) / 100) * w.scroll, "Ha bajado hasta el " + Math.min(100, Math.max(out.sd, out.depth * 11)) + " % de la página");
  const price = out.sections.filter((s) => PRICE_RE.test(s.id + " " + s.label) && s.secs >= 15);
  if (price.length) F("price", w.price + (props.filter((v) => Object.entries(parse(v.ss, {})).some(([id, s]) => s >= 10 && PRICE_RE.test(id + " " + (labels[id] || "")))).length > 1 ? w.priceAgain : 0), "Ha leído lo económico o las condiciones (" + price.map((s) => s.label).slice(0, 2).join(", ") + ")");
  const parts = out.sections.filter((s) => PART_RE.test(s.id + " " + s.label) && s.secs >= 10);
  if (parts.length >= 3) F("parts", w.parts, "Ha mirado " + parts.length + " partes de lo que incluye");
  if (out.webVisits) F("web", w.web, "Ha abierto su web nueva" + (out.webVisits > 1 ? " " + out.webVisits + " veces" : ""));
  if (out.meetings) F("meeting", w.meeting, "Ha pulsado para reservar una reunión");
  else if (out.contacts.length) F("contact", w.contact, "Ha pulsado para contactar (" + [...new Set(out.contacts)].join(", ") + ")");
  const docs = out.downloads + out.prints + out.shares; if (docs) F("docs", Math.min(w.docsMax, docs * w.docs), [out.downloads ? out.downloads + " descarga" + (out.downloads > 1 ? "s" : "") : "", out.prints ? "imprimir" : "", out.shares ? "compartir" : ""].filter(Boolean).join(", "));
  if (out.videos) F("video", w.video, "Ha reproducido " + out.videos + (out.videos === 1 ? " vídeo" : " vídeos"));
  if (out.readers.some((r) => r.level === "posible")) F("reader", w.reader, "Posible lector adicional");
  out.score = Math.min(100, Math.round(out.factors.reduce((a, f) => a + f.pts, 0)));
  const share = robots.length / Math.max(1, rows.length);
  out.conf = props.length >= 2 && out.act >= 120 && share < 0.5 ? "alta" : props.length >= 1 && out.act >= 30 ? "media" : "baja";
  out.why = out.conf === "alta" ? "Varias visitas de personas con tiempo activo." : out.conf === "media" ? "Hay actividad, pero poca para estar seguros." : "Muy pocos datos: una visita corta o casi sin interacción.";
  if (props.some((v) => !v.br)) out.why += " Parte de las visitas son de antes del contador v3 (sin detalle de secciones ni dispositivo).";
  out.lastAct = Math.max(...props.concat(webs).map((v) => v.seen || v.ts));
  return out;
}
async function outcomeOf(env, base) {
  const w = await whoOf(env, base);
  if (!w.lead) return { lead: "", name: w.name, stage: "" };
  const l = await env.DB.prepare("SELECT json_extract(data, '$.stage') AS s, json_extract(data, '$.estage') AS e FROM docs WHERE coll = 'leads' AND id = ?1").bind(w.lead).first();
  const st = (l && ([l.s, l.e].find((x) => x === "won") || [l.s, l.e].find((x) => x === "meet") || [l.s, l.e].find((x) => x === "lost") || l.s)) || "";
  return { lead: w.lead, name: w.name, stage: st, sc: w.sc };
}
const STAGE_TXT = { won: "Cerrado: la venta manda sobre cualquier puntuación", meet: "Reunión pendiente", lost: "No cerrado" };

/* ---------- alerts: one per reason (slug + kind + dk); the push only if that alert is switched on ---------- */
async function alertAdd(env, a, push) {
  await v30Ready(env);
  const r = await env.DB.prepare("INSERT OR IGNORE INTO palerts (ts, slug, kind, dk, title, body, url, visit, pushed) VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, ?8, 0) RETURNING id")
    .bind(Date.now(), a.slug, a.kind, a.dk, a.title, a.body, a.url, a.visit || null).all();
  const id = r.results && r.results[0] && r.results[0].id;
  if (!id) return false;
  if (push) { try { await pushAll(env, { title: a.title, body: a.body, tag: "al" + id, url: a.url }); await env.DB.prepare("UPDATE palerts SET pushed = 1 WHERE id = ?1").bind(id).run(); } catch (e) { /* the alert stays in the list */ } }
  return true;
}
async function alertsRun(env) {
  if (!env.VIS) return { off: true };
  await v30Ready(env);
  const cfg = await acfgOf(env), now = Date.now(), out = { c: 0, e: 0, high: 0, idle: 0 };
  /* 1) contact and meeting taps */
  let cc = await getMeta(env, "al_c");
  if (cc === null) { const t = await env.VIS.prepare("SELECT COALESCE(MAX(id), 0) AS m FROM c").first(); await setMeta(env, "al_c", String((t && t.m) || 0)); cc = String((t && t.m) || 0); }
  const cs = (await env.VIS.prepare("SELECT c.id, c.h, c.w, v.id AS vid, v.slug, v.tc, v.tcm FROM c JOIN v ON v.k = c.k WHERE c.id > ?1 ORDER BY c.id LIMIT 200").bind(Number(cc)).all()).results || [];
  const memo = {};
  for (const r of cs) {
    const k = clickKind(r.h), base = r.slug.replace(/--web$/, "");
    if ((k === "contact" || k === "meeting") && isHuman(r)) {
      memo[base] = memo[base] || await whoOf(env, base);
      const what = contactName(r.h), web = /--web$/.test(r.slug);
      if (await alertAdd(env, { slug: base, kind: k, dk: "v" + r.vid + ":" + what, title: memo[base].name, body: "Ha pulsado «" + (r.w || what).slice(0, 60) + "» (" + what + ") en " + (web ? "su web nueva" : "su propuesta") + ".", url: "/admin/crm#visita=" + r.vid, visit: r.vid }, !!cfg[k])) out.c++;
    }
    await setMeta(env, "al_c", String(r.id));
  }
  /* 2) documents, printing, sharing, a form sent */
  let ec = await getMeta(env, "al_e");
  try {
    if (ec === null) { const t = await env.VIS.prepare("SELECT COALESCE(MAX(id), 0) AS m FROM e").first(); await setMeta(env, "al_e", String((t && t.m) || 0)); ec = String((t && t.m) || 0); }
    const es = (await env.VIS.prepare("SELECT e.id, e.y, e.m, v.id AS vid, v.slug, v.tc, v.tcm FROM e JOIN v ON v.k = e.k WHERE e.id > ?1 ORDER BY e.id LIMIT 400").bind(Number(ec)).all()).results || [];
    const T = { dl: "ha descargado", print: "ha pedido imprimir", share: "ha usado el botón de compartir", form1: "ha enviado un formulario" };
    for (const r of es) {
      if (T[r.y] && isHuman(r)) {
        const base = r.slug.replace(/--web$/, ""); memo[base] = memo[base] || await whoOf(env, base);
        const m = parse(r.m, {}), file = r.y === "dl" && m.file ? " «" + String(m.file).slice(0, 60) + "»" : "";
        if (await alertAdd(env, { slug: base, kind: "docs", dk: "v" + r.vid + ":" + r.y + file, title: memo[base].name, body: "En su propuesta " + T[r.y] + file + ".", url: "/admin/crm#visita=" + r.vid, visit: r.vid }, !!cfg.docs)) out.e++;
      }
      await setMeta(env, "al_e", String(r.id));
    }
  } catch (e) { if (!/no such table/i.test(String(e && e.message))) throw e; }
  /* 3) high interest: proposals with activity in the last 3 minutes */
  const act = (await env.VIS.prepare("SELECT DISTINCT slug FROM v WHERE seen > ?1 LIMIT 30").bind(now - 180000).all()).results || [];
  const W = await iwOf(env);
  for (const { slug } of act) {
    const base = slug.replace(/--web$/, ""); const it = await intelOf(env, base, W);
    if (it.score >= cfg.highAt && it.conf !== "baja") {
      memo[base] = memo[base] || await whoOf(env, base);
      const lvl = it.score >= Math.max(85, cfg.highAt + 20) ? "2" : "1";
      if (await alertAdd(env, { slug: base, kind: "high", dk: "h" + lvl, title: memo[base].name + " · interés " + it.score + "/100", body: it.factors.slice().sort((a, b) => b.pts - a.pts).slice(0, 3).map((f) => f.txt).join(". ") + ".", url: "/admin/crm#visita=s:" + base }, !!cfg.high)) out.high++;
    }
  }
  /* 4) no activity for a while (once an hour): proposals opened before whose lead is still waiting */
  const lastIdle = Number((await getMeta(env, "al_idle")) || 0);
  if (now - lastIdle > 3600000) {
    await setMeta(env, "al_idle", String(now));
    const since = now - cfg.idleDays * DAY;
    const L = (await env.VIS.prepare("SELECT slug, MAX(COALESCE(seen, ts)) AS l, MAX(id) AS vid FROM v WHERE slug NOT LIKE '%--web' AND (tc IS NULL OR tc IN ('human_likely','unknown')) GROUP BY slug HAVING l < ?1 AND l > ?2 LIMIT 300").bind(since, since - 30 * DAY).all()).results || [];
    for (const r of L) {
      const o = await outcomeOf(env, r.slug);
      if (!o.lead || ["won", "lost", "meet"].includes(o.stage)) continue;
      if (await alertAdd(env, { slug: r.slug, kind: "idle", dk: "last" + r.vid, title: o.name, body: "Sin actividad en su propuesta desde hace " + Math.round((now - r.l) / DAY) + " días. Buen momento para un seguimiento.", url: "/admin/crm#lead=" + encodeURIComponent(o.lead) }, !!cfg.idle)) out.idle++;
    }
  }
  /* 5) retention (once a day): events and raw robot traffic older than the limit */
  const lastRet = Number((await getMeta(env, "al_ret")) || 0);
  if (now - lastRet > DAY) {
    await setMeta(env, "al_ret", String(now));
    try { await env.VIS.prepare("DELETE FROM e WHERE rt < ?1").bind(now - cfg.retDays * DAY).run(); await env.VIS.prepare("DELETE FROM b WHERE ts < ?1").bind(now - 90 * DAY).run(); } catch (e) { /* tables not there yet */ }
    await env.DB.prepare("DELETE FROM palerts WHERE ts < ?1").bind(now - 365 * DAY).run();
  }
  return out;
}
/* called by watchVisits for each new visit: a robot does not notify; a new device may be another reader */
async function entryCheck(env, v, w, cfg) {
  const full = await env.VIS.prepare("SELECT * FROM v WHERE id = ?1").bind(v.id).first();
  if (!full) return { push: !!cfg.entry, note: "" };
  if (!isHuman(full)) {
    await alertAdd(env, { slug: v.slug.replace(/--web$/, ""), kind: "robot", dk: "v" + v.id, title: w.name, body: "Apertura automática (" + ({ automation_likely: "programa o robot", security_scanner: "escáner de seguridad", link_preview: "vista previa de enlace", search_crawler: "buscador" }[tcOf(full)] || tcOf(full)) + ", " + (full.tcc || 0) + " % seguro): no cuenta como visita. " + (full.tcw || ""), url: "/admin/crm#visita=" + v.id, visit: v.id }, false);
    return { push: false, robot: true };
  }
  let note = tcOf(full) === "unknown" ? " Red de servidores o VPN: puede no ser una persona." : "";
  if (!/--web$/.test(v.slug)) {
    const prev = (await env.VIS.prepare("SELECT * FROM v WHERE slug = ?1 AND id < ?2 ORDER BY id DESC LIMIT 60").bind(v.slug, v.id).all()).results || [];
    const ph = prev.filter(isHuman), sig = devSig(full);
    if (ph.length && full.br && !ph.some((p) => devSig(p) === sig)) {
      const nets = new Set(ph.map((p) => p.asn).filter(Boolean)), cities = new Set(ph.map((p) => p.ci).filter(Boolean));
      const other = full.asn && nets.size && !nets.has(full.asn) && !(full.ci && cities.has(full.ci));
      const body = other ? "Posible lector adicional: la abre otro dispositivo (" + devLabel(full) + ") desde otra red" + (full.ci ? " (" + full.ci + ")" : "") + ". No es prueba de que la hayan reenviado."
        : "La abre otro dispositivo (" + devLabel(full) + ")" + (full.asn && nets.has(full.asn) ? " en la misma red: puede ser la misma persona o alguien de su equipo." : ".");
      await alertAdd(env, { slug: v.slug, kind: "reader", dk: sig, title: w.name, body, url: "/admin/crm#visita=" + v.id, visit: v.id }, !!cfg.reader && other);
      if (other) note += " Otro dispositivo y otra red.";
    }
  }
  return { push: !!cfg.entry, note };
}

/* ---------- v30 API (admin only) ---------- */
const TC_OK = ["human_likely", "automation_likely", "security_scanner", "link_preview", "search_crawler", "unknown"];
async function v30Api(req, env, p) {
  const m = req.method;
  await v30Ready(env);
  let r;
  if (m === "GET" && (r = /^visits\/intel\/([a-z0-9-]{1,80})$/.exec(p))) { const it = await intelOf(env, r[1]); it.outcome = await outcomeOf(env, r[1]); return json(it); }
  if (m === "GET" && p === "visits/intel") {   /* the ranking: proposals opened in the last 60 days */
    const S = (await env.VIS.prepare("SELECT slug, MAX(ts) AS l FROM v WHERE ts > ?1 AND slug NOT LIKE '%--web' GROUP BY slug ORDER BY l DESC LIMIT 80").bind(Date.now() - 60 * DAY).all()).results || [];
    const W = await iwOf(env), out = [];
    for (const s of S) { const it = await intelOf(env, s.slug, W); const o = await outcomeOf(env, s.slug);
      out.push({ slug: s.slug, name: o.name, lead: o.lead, stage: o.stage, score: it.score, conf: it.conf, visits: it.visits, returns: it.returns, act: it.act, last: it.last || s.l, robots: it.robots, readers: it.readers.length, possible: it.readers.filter((x) => x.level === "posible").length, contacts: it.contacts.length, top: it.factors.slice().sort((a, b) => b.pts - a.pts).slice(0, 2).map((f) => f.txt) }); }
    return json({ now: Date.now(), list: out });
  }
  if (m === "GET" && p === "visits/feed") {   /* the latest actions, across all proposals */
    const since = Date.now() - 3 * DAY, memo = {};
    let E = [];
    try { E = (await env.VIS.prepare("SELECT e.id, e.y, e.s, e.l, e.n, e.m, e.rt AS ts, v.id AS vid, v.slug, v.tc, v.tcm FROM e JOIN v ON v.k = e.k WHERE e.rt > ?1 AND e.y NOT IN ('tick','hid','vis','idle','wake','nav','resize','rerr','res') ORDER BY e.id DESC LIMIT 80").bind(since).all()).results || []; } catch (e) {}
    const C = (await env.VIS.prepare("SELECT c.id, c.h, c.w, c.sh, c.s, c.ts, v.id AS vid, v.slug, v.tc, v.tcm FROM c JOIN v ON v.k = c.k WHERE c.ts > ?1 ORDER BY c.id DESC LIMIT 60").bind(since).all()).results || [];
    const items = E.map((x) => ({ t: "e", y: x.y, s: x.s, l: x.l, n: x.n, m: parse(x.m, null), ts: x.ts, vid: x.vid, slug: x.slug, human: isHuman(x) }))
      .concat(C.map((x) => ({ t: "c", h: x.h, w: x.w, sh: x.sh, s: x.s, ts: x.ts, vid: x.vid, slug: x.slug, human: isHuman(x), kind: clickKind(x.h) })))
      .sort((a, b) => b.ts - a.ts).slice(0, 100);
    for (const it of items) { const base = it.slug.replace(/--web$/, ""); memo[base] = memo[base] || await whoOf(env, base); it.name = memo[base].name; it.web = /--web$/.test(it.slug); }
    return json({ now: Date.now(), items });
  }
  if (m === "GET" && p === "visits/alerts") {
    const L = (await env.DB.prepare("SELECT * FROM palerts ORDER BY id DESC LIMIT 150").all()).results || [];
    const memo = {};
    for (const a of L) { memo[a.slug] = memo[a.slug] || await whoOf(env, a.slug); a.name = memo[a.slug].name; }
    return json({ now: Date.now(), alerts: L, unseen: L.filter((a) => !a.seen).length });
  }
  if (m === "POST" && p === "visits/alerts/seen") { await env.DB.prepare("UPDATE palerts SET seen = 1 WHERE seen = 0").run(); return json({ ok: true }); }
  if (p === "visits/cfg") {
    if (m === "GET") return json({ alerts: await acfgOf(env), weights: await iwOf(env), defaults: { alerts: ACFG, weights: IW } });
    if (m === "POST") {
      const b = await body(req); if (!b) return bad("body");
      const a = {}, wgt = {};
      for (const k of Object.keys(ACFG)) if (b.alerts && b.alerts[k] !== undefined) { const v = Number(b.alerts[k]); if (!isFinite(v)) return bad("value"); a[k] = k === "highAt" ? Math.max(10, Math.min(100, Math.round(v))) : k === "idleDays" ? Math.max(1, Math.min(60, Math.round(v))) : k === "retDays" ? Math.max(30, Math.min(730, Math.round(v))) : v ? 1 : 0; }
      for (const k of Object.keys(IW)) if (b.weights && b.weights[k] !== undefined) { const v = Number(b.weights[k]); if (!isFinite(v) || v < 0 || v > 100) return bad("value"); wgt[k] = v; }
      await setMeta(env, "alert_cfg", JSON.stringify(Object.assign(await acfgOf(env), a)));
      if (b.weights) await setMeta(env, "intel_w", JSON.stringify(Object.assign(await iwOf(env), wgt)));
      await env.DB.prepare("INSERT INTO adminlog (ts, what, detail) VALUES (?1, 'cfg', ?2)").bind(Date.now(), JSON.stringify({ alerts: a, weights: wgt })).run();
      return json({ alerts: await acfgOf(env), weights: await iwOf(env) });
    }
  }
  if (m === "GET" && p === "visits/robots") {
    let rows = [];
    try { rows = (await env.VIS.prepare("SELECT tc, slug, COUNT(*) AS n, MAX(ts) AS l FROM b WHERE ts > ?1 GROUP BY tc, slug ORDER BY n DESC LIMIT 60").bind(Date.now() - 30 * DAY).all()).results || []; } catch (e) {}
    const auto = (await env.VIS.prepare("SELECT COALESCE(tcm, tc) AS tc, COUNT(*) AS n FROM v WHERE ts > ?1 GROUP BY 1").bind(Date.now() - 30 * DAY).all()).results || [];
    return json({ raw: rows, visits: auto });
  }
  if (m === "POST" && (r = /^visit\/(\d{1,12})\/class$/.exec(p))) {   /* correct a classification by hand */
    const b = await body(req); if (!b || !TC_OK.includes(b.tc)) return bad("tc");
    const v = await env.VIS.prepare("SELECT id, tc FROM v WHERE id = ?1").bind(Number(r[1])).first(); if (!v) return bad("notfound", 404);
    await env.VIS.prepare("UPDATE v SET tcm = ?1 WHERE id = ?2").bind(b.tc, v.id).run();
    await env.DB.prepare("INSERT INTO adminlog (ts, what, detail) VALUES (?1, 'class', ?2)").bind(Date.now(), JSON.stringify({ visit: v.id, from: v.tc, to: b.tc })).run();
    return json({ ok: true, tc: b.tc });
  }
  if (m === "GET" && (r = /^visits\/export\/([a-z0-9-]{1,80})$/.exec(p))) {   /* everything kept about one proposal */
    const V = (await env.VIS.prepare("SELECT * FROM v WHERE slug = ?1 OR slug = ?2 ORDER BY ts").bind(r[1], r[1] + "--web").all()).results || [];
    const ks = JSON.stringify(V.map((v) => v.k));
    const C = (await env.VIS.prepare("SELECT * FROM c WHERE k IN (SELECT value FROM json_each(?1)) ORDER BY id").bind(ks).all()).results || [];
    let E = []; try { E = (await env.VIS.prepare("SELECT * FROM e WHERE k IN (SELECT value FROM json_each(?1)) ORDER BY id").bind(ks).all()).results || []; } catch (e) {}
    await env.DB.prepare("INSERT INTO adminlog (ts, what, detail) VALUES (?1, 'export', ?2)").bind(Date.now(), r[1]).run();
    return new Response(JSON.stringify({ slug: r[1], exported: new Date().toISOString(), note: "Datos observados por el contador de 404 Growth. Sin direcciones IP.", visits: V.map(({ vid, ...x }) => x), clicks: C, events: E }, null, 1),
      { headers: Object.assign({ "content-type": "application/json; charset=utf-8", "content-disposition": 'attachment; filename="visitas-' + r[1] + '.json"', "cache-control": "no-store" }, SEC) });
  }
  if (m === "POST" && (r = /^visits\/delete\/([a-z0-9-]{1,80})$/.exec(p))) {   /* a deletion request: the proposal's tracking data */
    const b = await body(req); if (!b || b.confirm !== r[1]) return bad("confirm");
    const V = (await env.VIS.prepare("SELECT k FROM v WHERE slug = ?1 OR slug = ?2").bind(r[1], r[1] + "--web").all()).results || [];
    const ks = JSON.stringify(V.map((v) => v.k));
    await env.VIS.prepare("DELETE FROM c WHERE k IN (SELECT value FROM json_each(?1))").bind(ks).run();
    try { await env.VIS.prepare("DELETE FROM e WHERE k IN (SELECT value FROM json_each(?1))").bind(ks).run(); } catch (e) {}
    await env.VIS.prepare("DELETE FROM v WHERE slug = ?1 OR slug = ?2").bind(r[1], r[1] + "--web").run();
    await env.DB.prepare("DELETE FROM vwatch WHERE base = ?1").bind(r[1]).run();
    await env.DB.prepare("DELETE FROM palerts WHERE slug = ?1").bind(r[1]).run();
    await env.DB.prepare("INSERT INTO adminlog (ts, what, detail) VALUES (?1, 'delete', ?2)").bind(Date.now(), JSON.stringify({ slug: r[1], visits: V.length })).run();
    return json({ ok: true, visits: V.length });
  }
  return bad("missing", 404);
}
