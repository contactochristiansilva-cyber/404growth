/* ---------- v83: «Te preparo tu tienda» (404growth.com/tu-tienda), the lead magnet of the YouTube videos ----------
   Same lane as everyone else (Chris, 23/11/2026): the request becomes a lead in the CRM (or updates the one that is already there)
   with its UTM, Chris gets a push, the nightly batch makes its proposal, and the proposal's agenda books the call through
   /l/book like the ads and /book do. The page posts { name, biz, ig, phone, city, sec, web, ok, hp, utm } to /l/tt. */
const TT_NICHE = { moda: "moda", calzado: "sneakers", joyeria: "joya", cosmetica: "cosmetica", deporte: "deporte", deco: "deco", otro: "moda" };
const TT_PFX = { moda: "mod", sneakers: "snk", joya: "joy", cosmetica: "cos", deporte: "dep", deco: "dec" };
const TT_SEC = { moda: "Moda", calzado: "Calzado", joyeria: "Joyería", cosmetica: "Cosmética y perfumería", deporte: "Deporte", deco: "Hogar y deco", otro: "Otra cosa" };
const TT_WEB = { no: "No venden online", web: "Tienen web pero no vende", poca: "Tienen tienda online que vende poco" };
const ttIg = (v) => str(v, 160).replace(/^https?:\/\/(www\.)?instagram\.com\//i, "").replace(/^@/, "").replace(/[/?#].*$/, "").toLowerCase();
function ttPhone(v) {
  let p = str(v, 24).replace(/[^\d+]/g, "");
  if (/^[67]\d{8}$/.test(p)) p = "+34" + p; else if (/^(00)?34[67]\d{8}$/.test(p)) p = "+" + p.replace(/^00/, ""); else if (/^00\d{9,15}$/.test(p)) p = "+" + p.slice(2);
  return p;
}
const ttSlug = (s) => s.normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "").slice(0, 40) || "tienda";
async function ttApply(req, env, b, now) {
  if (str(b.hp, 80)) return json({ ok: true });   // the hidden field: only a robot fills it
  const name = str(b.name, 80), biz = str(b.biz, 120), city = str(b.city, 60), ig = ttIg(b.ig), phone = ttPhone(b.phone);
  const sec = Object.prototype.hasOwnProperty.call(TT_NICHE, b.sec) ? b.sec : "otro", web = Object.prototype.hasOwnProperty.call(TT_WEB, b.web) ? b.web : "no";
  if (name.length < 2 || biz.length < 2 || !/^[a-z0-9._]{2,30}$/.test(ig) || !/^\+\d{9,15}$/.test(phone) || b.ok !== true) return bad("fields");
  const DBq = env.DB, ih = (await sha("tt|" + (req.headers.get("cf-connecting-ip") || "local"))).slice(0, 22);
  const many = await DBq.prepare("SELECT COUNT(*) AS n FROM docs WHERE coll = 'leads' AND json_extract(data, '$.ttIh') = ?1 AND updated > ?2").bind(ih, now - 3600000).first();
  if (many && many.n >= 3) return bad("slow", 429);
  const utm = llUtm(b.utm), from = [utm.utm_source || "directo", utm.utm_medium, utm.utm_campaign].filter(Boolean).join(" · ");
  const when = new Date(now).toLocaleString("es-ES", { timeZone: CAL_TZ, day: "numeric", month: "numeric", year: "numeric", hour: "2-digit", minute: "2-digit" });
  const line = "Pidió su tienda de ejemplo en 404growth.com/tu-tienda el " + when + " (" + from + "). Contacto: " + name + ". " + TT_SEC[sec] + (city ? ", " + city : "") + ". " + TT_WEB[web] + ". Prometido: por WhatsApp en 2 días laborables.";
  const esc = ig.replace(/[\\%_]/g, (c) => "\\" + c);
  const hit = await DBq.prepare("SELECT id, data FROM docs WHERE coll = 'leads' AND (rtrim(lower(COALESCE(json_extract(data, '$.instagram'), '')), '/') LIKE ?1 ESCAPE '\\' OR json_extract(data, '$.phone') = ?2 OR json_extract(data, '$.whatsapp') = ?2) LIMIT 1")
    .bind("%instagram.com/" + esc, phone).first();
  const tomorrow = new Date(now + 86400000).toLocaleDateString("sv-SE", { timeZone: CAL_TZ });
  let id, title, body;
  if (hit) {
    let d = {}; try { d = JSON.parse(hit.data); } catch (e) {}
    const flags = Array.isArray(d.flags) ? d.flags.slice() : []; if (!flags.includes("pidio-tienda")) flags.push("pidio-tienda");
    const p = { notes: (d.notes ? d.notes + "\n" : "") + line, priority: Math.max(Number(d.priority) || 0, 95), flags, ttAt: now, ttIh: ih, ttUtm: utm };
    if (!d.whatsapp) p.whatsapp = phone;
    await DBq.batch([DBq.prepare("UPDATE docs SET data = json_patch(data, ?2), updated = ?3 WHERE coll = 'leads' AND id = ?1").bind(hit.id, JSON.stringify(p), now), bump(env)]);
    id = hit.id; title = "Pide su tienda de ejemplo · " + (d.name || biz);
    body = "Ya estaba en el CRM (" + (d.stage || "new") + (d.pageUrl ? ", con propuesta" : "") + "). @" + ig + " · " + phone + " · " + from;
  } else {
    const niche = TT_NICHE[sec], top = await DBq.prepare("SELECT COALESCE(MAX(CAST(json_extract(data, '$.order') AS INTEGER)), 0) AS m FROM docs WHERE coll = 'leads'").first();
    id = TT_PFX[niche] + "-yt-" + ttSlug(biz) + "-" + rid("").replace(/[^A-Za-z0-9]/g, "").slice(0, 4).toLowerCase();
    const d = { niche, name: biz, contact: name, phone, phoneType: "móvil", whatsapp: phone, waOk: true, email: "", website: "", zone: city, instagram: "https://www.instagram.com/" + ig + "/",
      stage: "new", flags: ["pidio-tienda"], source: "Pidió su tienda de ejemplo (" + from + ")", priority: 95, lotDay: tomorrow, notes: line,
      ttAt: now, ttIh: ih, ttUtm: utm, ttSec: sec, ttWeb: web, order: (Number(top && top.m) || 0) + 1 };
    await DBq.batch([DBq.prepare("INSERT INTO docs (coll, id, data, updated) VALUES ('leads', ?1, ?2, ?3) ON CONFLICT(coll, id) DO NOTHING").bind(id, JSON.stringify(d), now), bump(env)]);
    title = "Pide su tienda de ejemplo · " + biz;
    body = name + " · @" + ig + " · " + phone + " · " + TT_SEC[sec] + (city ? " · " + city : "") + " · " + TT_WEB[web] + " · " + from + ". Prometido en 2 días laborables.";
  }
  try { await pushAll(env, { title, body, tag: "tt" + id, url: "/admin/crm#lead=" + id }); } catch (e) {}
  return json({ ok: true });
}
