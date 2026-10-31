"""Admin v30 = v29 + «proposal intelligence» (27 oct 2026). Chris: «necesito ampliar el traqueo de las acciones que hacen» each prospect in
the proposals (and each client in 404 Content). With the counter v3 (VIS): the visit page shows active time, scroll %, time per part,
everything they did in order (events + taps), device and network (approximate, no IP), the traffic type with its confidence (and a way
to correct it); each proposal gets an interest score 0-100 with its factors and reliability, possible extra readers said with care;
alerts (contact, meeting, documents, high interest, another reader, no activity) with settings; the «Visitas» tab gets Propuestas,
Movimientos and Avisos; export and deletion of one proposal's data; robots apart; retention. The notices of 404 Content (p_events) get
their own titles (the platform is only 404 Content now) and its clients' activity milestones (kind c_act).
usage: python3 patch_v30.py worker.v29.js worker.v30.js"""
import sys, json, os
H = os.path.dirname(os.path.abspath(__file__))
src, dst = sys.argv[1], sys.argv[2]
w = open(src, encoding='utf-8').read()
def rep(s, a, b, n=1):
    assert s.count(a) == n, (s.count(a), a[:140]); return s.replace(a, b)

SERVER = open(os.path.join(H, 'v30_server.js'), encoding='utf-8').read()
UI = open(os.path.join(H, 'v30_ui.js'), encoding='utf-8').read()

# ---------------- server ----------------
w = rep(w, "\n/* ---------- v22: the page of each visit ----------", SERVER + "\n/* ---------- v22: the page of each visit ----------")

w = rep(w, """  "CREATE INDEX IF NOT EXISTS c_k ON c (k, id)"];
const LIVE_MS""", """  "CREATE INDEX IF NOT EXISTS c_k ON c (k, id)",
  // v30: the counter v3 adds these by itself; the admin adds them too if it reads first
  "ALTER TABLE v ADD COLUMN cv INTEGER", "ALTER TABLE v ADD COLUMN act INTEGER", "ALTER TABLE v ADD COLUMN sd INTEGER", "ALTER TABLE v ADD COLUMN ss TEXT",
  "ALTER TABLE v ADD COLUMN br TEXT", "ALTER TABLE v ADD COLUMN os TEXT", "ALTER TABLE v ADD COLUMN dv TEXT", "ALTER TABLE v ADD COLUMN scr TEXT",
  "ALTER TABLE v ADD COLUMN lang TEXT", "ALTER TABLE v ADD COLUMN tz TEXT", "ALTER TABLE v ADD COLUMN dk INTEGER", "ALTER TABLE v ADD COLUMN tch INTEGER",
  "ALTER TABLE v ADD COLUMN rg TEXT", "ALTER TABLE v ADD COLUMN ci TEXT", "ALTER TABLE v ADD COLUMN asn INTEGER", "ALTER TABLE v ADD COLUMN aso TEXT",
  "ALTER TABLE v ADD COLUMN ipv INTEGER", "ALTER TABLE v ADD COLUMN ref TEXT", "ALTER TABLE v ADD COLUMN nav TEXT", "ALTER TABLE v ADD COLUMN tc TEXT",
  "ALTER TABLE v ADD COLUMN tcc INTEGER", "ALTER TABLE v ADD COLUMN tcw TEXT", "ALTER TABLE v ADD COLUMN tcm TEXT", "ALTER TABLE v ADD COLUMN evn INTEGER",
  "CREATE TABLE IF NOT EXISTS e (id INTEGER PRIMARY KEY AUTOINCREMENT, k TEXT NOT NULL, i TEXT NOT NULL, y TEXT NOT NULL, ver INTEGER NOT NULL DEFAULT 1, src TEXT NOT NULL DEFAULT 'web', ot INTEGER, rt INTEGER NOT NULL, t INTEGER NOT NULL DEFAULT 0, s TEXT, l TEXT, n INTEGER, m TEXT)",
  "CREATE UNIQUE INDEX IF NOT EXISTS e_ki ON e (k, i)", "CREATE INDEX IF NOT EXISTS e_y ON e (y, rt)",
  "CREATE TABLE IF NOT EXISTS b (id INTEGER PRIMARY KEY AUTOINCREMENT, ts INTEGER NOT NULL, slug TEXT, tc TEXT, tcc INTEGER, ua TEXT, cc TEXT, aso TEXT)", "CREATE INDEX IF NOT EXISTS b_ts ON b (ts)"];
const LIVE_MS""")
w = rep(w, "  try { const r = await watchVisits(env); return r && typeof r === \"object\" ? Object.assign(r, { obra: ob }) : r; }", "  try { const r = await visQ(env, () => watchVisits(env)); return r && typeof r === \"object\" ? Object.assign(r, { obra: ob }) : r; }   // v30: visQ adds the counter's v3 columns if they are not there yet")
w = rep(w, "// Data: D1 database DB (this Worker's own) and, read only, VIS (the visit counter of the prospect landings).", "// Data: D1 database DB (this Worker's own) and VIS (the visit counter of the prospect landings: read, plus, since v30, a manual correction of a\n// visit's traffic type and the deletion of one proposal's data when asked).")

# the visit row carries what v3 adds (unknown stays unknown)
w = rep(w, 'const visRow = (v, now) => { const s = visState(v, now); return { id: v.id, slug: v.slug, kind: /--web$/.test(v.slug) ? "web" : "prop", ts: v.ts, secs: v.secs || 0, depth: v.depth || 0, cc: v.cc || "", dev: v.dev || "", seen: s.last, live: s.live }; };',
  'const visRow = (v, now) => { const s = visState(v, now); return { id: v.id, slug: v.slug, kind: /--web$/.test(v.slug) ? "web" : "prop", ts: v.ts, secs: v.secs || 0, depth: v.depth || 0, cc: v.cc || "", dev: v.dev || "", seen: s.last, live: s.live,\n'
  '  act: v.act == null ? null : v.act, sd: v.sd || 0, ss: parse(v.ss, {}), br: v.br || "", os: v.os || "", dv: v.dv || "", scr: v.scr || "", lang: v.lang || "", tz: v.tz || "", dk: v.dk || 0, tch: v.tch == null ? null : v.tch,\n'
  '  rg: v.rg || "", ci: v.ci || "", asn: v.asn || null, aso: v.aso || "", ipv: v.ipv || null, ref: v.ref || "", nav: v.nav || "", tc: v.tc || "", tcc: v.tcc || 0, tcw: v.tcw || "", tcm: v.tcm || "", evn: v.evn || 0 }; };   // v30')
w = rep(w, "  row.clicks = await visClicks(env, v.k);\n",
  "  row.clicks = await visClicks(env, v.k);\n"
  "  try { row.events = ((await env.VIS.prepare(\"SELECT id, y, t, s, l, n, m, src, rt FROM e WHERE k = ?1 AND y != 'tick' ORDER BY t, id LIMIT 600\").bind(v.k).all()).results || []).map((e) => Object.assign(e, { m: parse(e.m, null) })); } catch (e) { row.events = []; }   // v30\n")
w = rep(w, "  return { now: now, visit: row, pair: pair, history: hist, who: who };",
  "  let intel = null; try { intel = await intelOf(env, base); intel.outcome = await outcomeOf(env, base); } catch (e) { intel = null; }   // v30\n"
  "  return { now: now, visit: row, pair: pair, history: hist, who: who, intel: intel };")
w = rep(w, "async function visitApi(req, env, p) {\n  if (req.method !== \"GET\") return bad(\"method\", 405);\n  if (!env.VIS) return json({ off: true });",
  "async function visitApi(req, env, p) {\n  if (!env.VIS) return json({ off: true });\n"
  "  if ((p.startsWith(\"visits/\") && p !== \"visits/recent\") || /^visit\\/\\d{1,12}\\/class$/.test(p)) return visQ(env, () => v30Api(req, env, p));   // v30\n"
  "  if (req.method !== \"GET\") return bad(\"method\", 405);")
w = rep(w, 'if (p.startsWith("visit/") || p === "visits/recent") return visitApi(req, env, p);', 'if (p.startsWith("visit/") || p.startsWith("visits/")) return visitApi(req, env, p);')
# the entry: robots do not notify; a new device may be another reader; each entry is also an alert in the list
w = rep(w, """    if (!web && now - v.ts < 30 * 60000 && sent < 10) {   /* the first one: they are reading it now */
      const n = (await env.VIS.prepare("SELECT COUNT(*) AS n FROM v WHERE slug = ?1 AND id <= ?2").bind(v.slug, v.id).first()).n || 1;
      await pushAll(env, { title: w.name, body: "Está viendo su propuesta ahora mismo, " + whereOf(v.cc, v.dev) + ". " + nth(n) + " Toca para verla en directo.", tag: "v" + v.id, url: "/admin/crm#visita=" + v.id });   // v22: straight to the visit
      await env.DB.prepare("UPDATE vwatch SET sent = 1 WHERE id = ?1").bind(v.id).run(); sent++;
    }""", """    if (!web && now - v.ts < 30 * 60000 && sent < 10) {   /* the first one: they are reading it now */
      const ec = await entryCheck(env, v, w, cfg30 || (cfg30 = await acfgOf(env)));   // v30: a robot never notifies; another device may be another reader
      if (!ec.robot) {
        const n = (await env.VIS.prepare("SELECT COUNT(*) AS n FROM v WHERE slug = ?1 AND id <= ?2 AND (tc IS NULL OR COALESCE(tcm, tc) IN ('human_likely','unknown'))").bind(v.slug, v.id).first()).n || 1;
        await alertAdd(env, { slug: base, kind: "entry", dk: "v" + v.id, title: w.name, body: "Está viendo su propuesta ahora mismo, " + whereOf(v.cc, v.dev) + ". " + nth(n) + (ec.note || "") + " Toca para verla en directo.", url: "/admin/crm#visita=" + v.id, visit: v.id }, ec.push);   // v22: straight to the visit
        sent++;
      }
      await env.DB.prepare("UPDATE vwatch SET sent = 1 WHERE id = ?1").bind(v.id).run();
    }""")
w = rep(w, "  let sent = 0;\n  const fresh = (await env.VIS.prepare(\"SELECT id, slug, ts, vid, cc, dev, secs, depth FROM v WHERE id > ?1 ORDER BY id LIMIT 40\")",
  "  let sent = 0, cfg30 = null;\n  const fresh = (await env.VIS.prepare(\"SELECT id, slug, ts, vid, cc, dev, secs, depth FROM v WHERE id > ?1 ORDER BY id LIMIT 40\")")
w = rep(w, "async function scheduledRun(env) {\n  try { await partnerNotices(env); } catch (e) { /* never stops the rest */ }   // v29\n",
  "async function scheduledRun(env) {\n  try { await partnerNotices(env); } catch (e) { /* never stops the rest */ }   // v29\n"
  "  try { await visQ(env, () => alertsRun(env)); } catch (e) { /* v30: never stops the rest */ }\n")
# 404 Content notices: the platform sells only 404 Content now; its clients' milestones come as c_act
w = rep(w, 'const P404_TITLE = { c_pago: "Partner 404 · nuevo cliente", c_checkout: "Partner 404 · pago abierto", c_web: "Partner 404 · web por revisar", c_reset: "Partner 404 · contraseña", c_error: "Partner 404 · error", c_conn: "Partner 404 · conexión", c_alta: "Partner 404 · ha entrado", c_sub: "Partner 404 · suscripción" };',
  'const P404_TITLE = { c_pago: "404 Content · nuevo cliente", c_checkout: "404 Content · pago abierto", c_web: "404 Content · web por revisar", c_reset: "404 Content · contraseña", c_error: "404 Content · error", c_conn: "404 Content · conexión", c_alta: "404 Content · ha entrado", c_sub: "404 Content · suscripción", c_act: "404 Content · actividad" };   // v30')
w = rep(w, 'title: P404_TITLE[r.kind] || "Partner 404", body: String(r.text).slice(0, 200), tag: "p404" + r.id, url: "https://app.404growth.com/admin" + (r.kind === "c_web" ? "#webs" : r.kind === "c_checkout" ? "#altas" : r.kind === "c_reset" ? "#clientes" : "") });',
  'title: P404_TITLE[r.kind] || "404 Content", body: String(r.text).slice(0, 200), tag: "p404" + r.id, url: "https://app.404growth.com/admin" + (r.kind === "c_checkout" ? "#altas" : r.kind === "c_reset" || r.kind === "c_act" ? "#clientes" + (r.tenant_id ? "=" + r.tenant_id : "") : "") });')
w = rep(w, 'rows = (await env.DB.prepare("SELECT id, kind, text FROM p_events WHERE sent = 0 AND substr(kind, 1, 2) = \'c_\' ORDER BY id LIMIT 20").all()).results || [];',
  'rows = (await env.DB.prepare("SELECT id, kind, text, tenant_id FROM p_events WHERE sent = 0 AND substr(kind, 1, 2) = \'c_\' ORDER BY id LIMIT 20").all()).results || [];')

# ---------------- the CRM page ----------------
i = w.find(', crm: "'); j = w.find('", portal: "', i)
assert i > 0 and j > i
crm = json.loads(w[i + 7:j + 1])
assert json.dumps(crm, ensure_ascii=False) == w[i + 7:j + 1]
CSS = (
  "'#vp .kv{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;margin-bottom:8px}#vp .kv div{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:10px 12px}#vp .kv b{display:block;font:700 18px var(--mono)}#vp .kv span{color:var(--mute);font-size:12px;line-height:1.3;display:block;margin-top:2px}' +\n"
  "    '#vp .scrollbar{height:8px;border-radius:99px;background:var(--surface-2);overflow:hidden}#vp .scrollbar i{display:block;height:100%;background:var(--accent);border-radius:99px}' +\n"
  "    '#vp .bars{display:grid;gap:6px}#vp .br{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr) 64px;gap:10px;align-items:center;font-size:13px}#vp .br span{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}#vp .br i{height:8px;border-radius:99px;background:var(--surface-2);overflow:hidden}#vp .br i b{display:block;height:100%;background:var(--accent);border-radius:99px}#vp .br em{font:600 12px var(--mono);font-style:normal;color:var(--mute);text-align:end}' +\n"
  "    '#vp .dv{display:grid;grid-template-columns:auto minmax(0,1fr);gap:6px 14px;margin:0;background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:12px 14px;font-size:13.5px}#vp .dv dt{color:var(--mute)}#vp .dv dd{margin:0;overflow-wrap:anywhere}' +\n"
  "    '#vp .fine,.vlist .fine,.cfgbox .fine{color:var(--mute);font-size:12.5px;line-height:1.45;margin:8px 2px 0}' +\n"
  "    '#vp .tcard{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:12px 14px}#vp .tcard p{margin:8px 0 0;font-size:13px}#vp .row,.cfgbox .row{display:flex;gap:8px;flex-wrap:wrap;margin-top:10px;align-items:center}' +\n"
  "    '.tchip{display:inline-block;font-weight:700;font-size:13px;padding:4px 10px;border-radius:99px;background:var(--surface-2)}.tchip.ok{background:var(--ok-soft,var(--surface-2));color:var(--ok)}.tchip.mid{background:var(--warn-soft,var(--surface-2));color:var(--warn)}.tchip.bad{background:var(--hot-soft,var(--surface-2));color:var(--hot)}' +\n"
  "    '#vp .ic{display:flex;gap:14px;align-items:center;background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:14px 16px;margin:6px 0 8px}#vp .ic .sc{min-width:74px;text-align:center}#vp .ic .sc b{font:800 34px/1 var(--mono)}#vp .ic .sc small{display:block;color:var(--mute);font-size:12px}#vp .ic.hot .sc b{color:var(--hot)}#vp .ic.warm .sc b{color:var(--warn)}#vp .ic .t{font-weight:800;margin:0}#vp .ic .t em{font-style:normal;color:var(--accent)}#vp .ic .c{color:var(--mute);font-size:13px;margin:4px 0 0}' +\n"
  "    '#vp .fx{list-style:none;margin:0 0 4px;padding:0;display:grid;gap:4px}#vp .fx li{font-size:13.5px;display:flex;gap:8px}#vp .fx em{font:700 12px var(--mono);font-style:normal;color:var(--ok);min-width:42px}' +\n"
  "    '#vp .rd{list-style:none;margin:0;padding:0;display:grid;gap:6px}#vp .rd li{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:10px 12px;display:grid;gap:2px}#vp .rd span{color:var(--mute);font-size:12.5px}#vp .rd .lvl{font-weight:700;font-size:12px}#vp .rd .lvl.posible{color:var(--warn)}#vp .rd .lvl.principal{color:var(--ok)}' +\n"
  "    '#vp .acts{display:flex;gap:8px;flex-wrap:wrap;margin-top:24px}' +\n"
  "    '.vseg{display:flex;gap:4px;background:var(--surface-2);border-radius:12px;padding:4px;margin-bottom:12px;overflow-x:auto}.vseg button{flex:1;border:0;background:none;border-radius:9px;padding:8px 10px;font-weight:700;font-size:13.5px;color:var(--mute);cursor:pointer;white-space:nowrap}.vseg button[aria-selected=\"true\"]{background:var(--surface);color:var(--text,inherit);box-shadow:var(--shadow)}' +\n"
  "    '.vfil{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:10px}.vfil select{border:1px solid var(--line);background:var(--surface);border-radius:10px;padding:7px 10px;font:inherit;font-size:13px}' +\n"
  "    '.prow{grid-template-columns:auto minmax(0,1fr) auto}.prow .pscore{grid-column:1;grid-row:1 / span 3;align-self:start}.prow b{grid-column:2;grid-row:1}.prow .w{grid-column:3;grid-row:1}.prow span:not(.pscore):not(.w){grid-column:2/-1}.pscore{font:800 17px var(--mono);min-width:40px;text-align:center;border-radius:10px;padding:6px 4px;background:var(--surface-2)}.pscore.hot{background:var(--hot);color:var(--bg)}.pscore.warm{background:var(--warn-soft,var(--surface-2));color:var(--warn)}.prow .top{grid-column:2/-1;font-size:12.5px;color:var(--mute)}' +\n"
  "    '.cl.feed{list-style:none;margin:0;padding:0;background:var(--surface);border:1px solid var(--line);border-radius:14px;overflow:hidden}.cl.feed li{display:grid;gap:2px 10px;padding:11px 14px;border-bottom:1px solid var(--line);grid-template-columns:62px minmax(0,1fr)}.cl.feed li:last-child{border-bottom:0}.cl.feed time{font:600 12.5px var(--mono);color:var(--mute);grid-row:span 2;padding-top:1px}.cl.feed b{font-size:14px}.cl.feed li>span{color:var(--mute);font-size:13px;overflow-wrap:anywhere}.cl.feed small{color:var(--mute);font-weight:500}.cl.feed li.new{background:color-mix(in srgb,var(--accent) 7%,transparent)}.lk{border:0;background:none;padding:0;font:inherit;font-weight:700;color:var(--accent);cursor:pointer;text-decoration:none}.ak{font-size:11.5px;font-weight:700;padding:2px 7px;border-radius:99px;background:var(--surface-2);color:var(--mute)}.ak.contact,.ak.meeting,.ak.high{background:var(--accent-soft);color:var(--accent)}.ak.robot{opacity:.7}' +\n"
  "    '.cfgbox{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:12px 14px;display:grid;gap:8px;font-size:13.5px}.sw2{display:flex;gap:8px;align-items:flex-start}.sw2 input[type=checkbox]{margin-top:3px}.sw2 .num{margin:0 4px}.num{width:70px;border:1px solid var(--line);border-radius:8px;padding:4px 6px;font:inherit;background:var(--bg)}.wgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:8px;margin-top:8px}.wgrid label{display:flex;justify-content:space-between;gap:6px;align-items:center;font-size:12.5px}.vrowh{display:flex;justify-content:space-between;align-items:center}' +\n"
  "    '@media (max-width:520px){#vp .kv{grid-template-columns:1fr 1fr 1fr}#vp .br{grid-template-columns:minmax(0,1fr) 70px 56px}}' +\n"
  "    ")
crm = rep(crm, "    '.tabs .vlive{display:inline-block;", CSS + "'.tabs .vlive{display:inline-block;")
crm = rep(crm, "  /* ---------- the page of one visit ---------- */", UI + "\n  /* ---------- the page of one visit ---------- */")
crm = rep(crm, "    var L = S.list.visits || [], t0 = now(), live = L.filter(", "    var L = filt(S.list.visits || []), t0 = now(), live = L.filter(")
crm = rep(crm, "  function paintList() { var w = document.getElementById('vis-wrap'); if (w) w.innerHTML = listHtml() }",
  "  function paintList() { var w = document.getElementById('vis-wrap'); if (w) w.innerHTML = tabHtml() }")
crm = rep(crm, "return '<div id=\"vis-wrap\">' + listHtml() + '</div>' }", "loadMode(); return '<div id=\"vis-wrap\">' + tabHtml() + '</div>' }")
crm = rep(crm, "setInterval(function () { if (S.list && S.live && document.getElementById('vis-wrap')", "setInterval(function () { if (S.list && S.live && M.mode === 'list' && document.getElementById('vis-wrap')")
crm = rep(crm, "    h += '<p class=\"meta\">Entró ' + esc(day(v.ts)) + ' · ' + esc(nth(v.nth)) + ' · ' + esc(place(v)) + '</p>';\n",
  "    h += '<p class=\"meta\">Entró ' + esc(day(v.ts)) + ' · ' + esc(nth(v.nth)) + ' · ' + esc(place(v)) + '</p>';\n"
  "    if (!web && d.intel) h += scoreCard(d.intel);   /* v30 */\n")
crm = rep(crm, "    h += '<h3>Clics<em>' + (v.clicks.length || '') + '</em></h3>' + clicks(v.clicks, v.kind);\n", "    h += paintV30(d);   /* v30: reading, everything done in order, device and network, traffic type */\n")
crm = rep(crm, "    b.innerHTML = h;\n  }\n  function tickClocks()",
  "    var base = v.slug.replace(/--web$/, '');\n"
  "    h += '<div class=\"acts\"><a class=\"btn sm\" href=\"/admin/api/visits/export/' + esc(base) + '\" download>Exportar sus datos</a><button type=\"button\" class=\"btn sm\" data-vp-del=\"' + esc(base) + '\">Borrar sus datos</button></div>';\n"
  "    b.innerHTML = h;\n  }\n  function tickClocks()")
w = w[:i + 7] + json.dumps(crm, ensure_ascii=False) + w[j + 1:]
w = rep(w, "// 404 Growth (v29):", "// 404 Growth (v30):")
open(dst, 'w', encoding='utf-8').write(w)
print('ok', len(w))
