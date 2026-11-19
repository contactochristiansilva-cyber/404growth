# python3 patch_v80.py <admin worker v79> <salida>
# v80 (19/11/2026) · «Hasta dónde ha llegado» de cada propuesta, con las partes de su página.
# Chris: «a veces cuando 404 me notifica de actividad de un prospecto en la propuesta me dice que va por CRM IA… siendo nuevas».
# Antes, el tipo de propuesta se adivinaba por el nicho del lead:
#  - en la visita (whoOf): solo moda y joyería eran «tienda»; cosmética, suplementos, sneakers, ópticas, deco, mercería… se leían como
#    la oferta antigua (web, vídeo, WhatsApp + IA, CRM): llegar a la tienda salía como «WhatsApp + IA» y a captación como «CRM»;
#  - en la ficha del CRM (vPart): todas las de tienda se leían como la oferta de contenido: «llegó a la web», «llegó al asistente»…
# Ahora lo dice la propia página: las secciones en las que han estado sus visitas (ss del contador). es = contenido + web + asistente +
# CRM; tv = tiendas de los lotes 30–39 (tienda, diagnóstico, captación, plan); t4 = lote 40 (gen40.py: tienda, ficha, agenda, pedidos,
# garantía, Navidad, anuncios); dx = concesionarios. Si aún no hay secciones, lo dice el lead (nicho y día del lote).
import sys
src, out = sys.argv[1:3]
w = open(src, encoding='utf-8').read()

def rep(old, new, n=1):
    global w
    c = w.count(old)
    assert c == n, (c, old[:90])
    w = w.replace(old, new)

# ---------- servidor: el tipo de propuesta, por su página ----------
rep("""const ES_NICHES = ["gym", "real", "clinic", "aesth", "tattoo"];""",
"""const ES_NICHES = ["gym", "real", "clinic", "aesth", "tattoo"];
/* v80 (19/11/2026): which parts a proposal has comes from the page itself (the sections its visits have been in), not from the lead's
   niche. Before, every shop proposal outside fashion and jewellery was read as the old offer (web, vídeo, WhatsApp + IA, CRM), so
   reaching the shop said «WhatsApp + IA» and reaching captación said «CRM». es: content + web + assistant + CRM; tv: the shop
   proposals of lotes 30–39 (tienda, diagnóstico, captación, plan); t4: lote 40 on (gen40.py); dx: the dealers' pages. */
const SC_ES = ["p-contenido", "rodaje", "reels", "publicamos", "p-web", "p-asistente", "p-crm", "p-cliente", "incluye", "sistema", "garantias"];
const SC_T4 = ["producto", "pedido", "ahora", "anuncios"];
const SC_TV = ["diagnostico", "mercado", "captacion", "cambia", "plan", "valor"];
const T4_FROM = "2026-11-19";   // the first lote with the gen40.py proposals; the proposals sent from that day on are made with it
async function scOf(env, base, l) {
  if (env.VIS) try {
    const rows = (await env.VIS.prepare("SELECT ss FROM v WHERE slug = ?1 AND ss IS NOT NULL AND ss != '{}' ORDER BY id DESC LIMIT 40").bind(base).all()).results || [];
    const seen = new Set(); for (const r of rows) for (const k of Object.keys(parse(r.ss, {}) || {})) seen.add(k);
    if (SC_ES.some((k) => seen.has(k))) return "es";
    if (SC_T4.some((k) => seen.has(k))) return "t4";
    if (SC_TV.some((k) => seen.has(k))) return "tv";
  } catch (e) { /* a counter without sections: what the lead says */ }
  if (!l) return "";
  if (ES_NICHES.includes(l.niche)) return "es";
  if (!l.niche || l.niche === "dealer" || l.niche === "rent") return "dx";
  return String(l.lot || "") >= T4_FROM ? "t4" : "tv";
}""")
rep("""SELECT id, json_extract(data, '$.name') AS name, json_extract(data, '$.niche') AS niche FROM docs WHERE coll = 'leads' AND (json_extract(data, '$.pageUrl') LIKE ?1""",
    """SELECT id, json_extract(data, '$.name') AS name, json_extract(data, '$.niche') AS niche, json_extract(data, '$.lotDay') AS lot FROM docs WHERE coll = 'leads' AND (json_extract(data, '$.pageUrl') LIKE ?1""")
rep("""sc: ES_NICHES.includes(l.niche) ? "es" : (TV_NICHES.includes(l.niche) || /^(mod|joy)/.test(l.id || "")) ? "tv" : "dx", url: "/admin/crm#lead=\"""",
    """sc: await scOf(env, base, l), url: "/admin/crm#lead=\"""")
rep("""return { lead: "", name: base, sc: "dx", url: "/admin/crm" };""",
    """return { lead: "", name: base, sc: await scOf(env, base, null), url: "/admin/crm" };""")
rep("""function partOf(sc, d) { d = Math.max(0, Number(d) || 0); if (sc === "tv")""",
    """const PART_T4 = ["se quedó en la portada", "llegó a la tienda", "llegó a la ficha de producto", "llegó a la agenda", "llegó a «menos mensajes»", "llegó a la garantía", "llegó a «antes de Navidad»", "llegó a los anuncios", "llegó al final"];
function partOf(sc, d) { d = Math.max(0, Number(d) || 0); if (sc === "t4") return PART_T4[d >= 9 ? 8 : d >= 3 ? 1 : 0]; if (sc === "tv")""")

# ---------- la página de cada visita: sus partes y hasta dónde llegó ----------
rep("""var PART_DX = ['Portada', 'Web', 'Vídeo', 'WhatsApp + IA', 'CRM', 'Quiénes somos', 'Final'];""",
    """var PART_DX = ['Portada', 'Web', 'Vídeo', 'WhatsApp + IA', 'CRM', 'Quiénes somos', 'Final'];\\n  /* v80: the lote 40 proposals (gen40.py), in the order of the page; how far is worked out from the sections they were in */\\n  var T4_IDS = ['inicio', 'tienda', 'producto', 'agenda', 'pedido', 'garantia', 'ahora', 'anuncios', 'hablar'];\\n  var PART_T4 = ['Portada', 'La tienda', 'La ficha', 'La agenda', 'Menos mensajes', 'La garantía', 'Antes de Navidad', 'Los anuncios', 'Final'];\\n  var REACH_T4 = ['se quedó en la portada', 'llegó a la tienda', 'llegó a la ficha de producto', 'llegó a la agenda', 'llegó a «menos mensajes»', 'llegó a la garantía', 'llegó a «antes de Navidad»', 'llegó a los anuncios', 'llegó al final'];""")
rep("""function parts(sc) { return sc === 'tv' ? PART_TV : """,
    """function dep(sc, v) { var d = (v && v.depth) || 0; if (sc !== 't4') return d; var s = (v && v.ss) || {}, i = d >= 9 ? 8 : d >= 3 ? 1 : 0; T4_IDS.forEach(function (id, k) { if (s[id] > 0 && k > i) i = k }); return i }\\n  function parts(sc) { return sc === 't4' ? PART_T4 : sc === 'tv' ? PART_TV : """)
rep("""function partTxt(sc, d) { var R = sc === 'tv' ? REACH_TV : """,
    """function partTxt(sc, d) { var R = sc === 't4' ? REACH_T4 : sc === 'tv' ? REACH_TV : """)
rep("""P = web ? null : parts(w.sc);""", """P = web ? null : parts(w.sc), dv = dep(w.sc, v);""")
rep("""(i === v.depth ? 'cur' : i < v.depth ? 'ok' : '')""", """(i === dv ? 'cur' : i < dv ? 'ok' : '')""")
rep("""partTxt(v.sc, v.depth)""", """partTxt(v.sc, dep(v.sc, v))""", 2)
rep("""partTxt(w.sc, x.depth)""", """partTxt(w.sc, dep(w.sc, x))""")
rep("""visita: 'Visítanos' };""",
    """visita: 'Visítanos',\\n    tienda: 'La tienda', producto: 'La ficha de producto', agenda: 'La agenda', pedido: 'Menos mensajes', ahora: 'Antes de Navidad', anuncios: 'Los anuncios', hablar: 'El cierre',\\n    diagnostico: 'El diagnóstico', mercado: 'El mercado', captacion: 'Captación', cambia: 'Lo que cambia', plan: 'El plan', valor: 'Lo que vale', antes: 'Antes y después', pie: 'El pie' };""")

# ---------- la ficha del CRM: «última … · llegó a …» ----------
rep("""var VPART_ES=['solo vio la portada','llegó al contenido','llegó a los 15 reels','llegó a la web','llegó al asistente','llegó al CRM','llegó al cliente','llegó a la garantía','llegó a lo que incluye','llegó al final'];""",
    """var VPART_ES=['solo vio la portada','llegó al contenido','llegó a los 15 reels','llegó a la web','llegó al asistente','llegó al CRM','llegó al cliente','llegó a la garantía','llegó a lo que incluye','llegó al final'];\\n  /* v80: the online shop proposals (all the shop niches): 3 the shop, 4–7 captación, 8 the plan, 9 the end (lote 40 sends 0, 3 and 9) */\\n  var VPART_TV=['solo vio la portada','solo vio la portada','solo vio la portada','llegó a la tienda','llegó a captación','llegó a captación','llegó a captación','llegó a captación','llegó al plan','llegó al final'];""")
rep("""function vPart(v){return v&&v.es?""", """function vPart(v){return v&&v.tv?VPART_TV[Math.max(0,Math.min(9,v.p||0))]:v&&v.es?""")
rep("""return ESN[nicheOf(l)]?Object.assign({es:1},v):v}""",
    """var n=nicheOf(l);return SHOPN[n]?Object.assign({tv:1},v):ESN[n]?Object.assign({es:1},v):v}""")
rep("""vPart({es:1,p:h.p})""", """vPart(SHOPN[nicheOf(l)]?{tv:1,p:h.p}:{es:1,p:h.p})""")

open(out, 'w', encoding='utf-8').write(w)
print('ok')
