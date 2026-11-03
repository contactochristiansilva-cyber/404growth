"""Lote 31 · propuesta de tienda online (formato del lote 30) con imágenes de Apimart.
uso: python3 gen.py <slug> [<slug> ...]   → escribe en ../out/: p-<slug>.html y p-<slug>--b--*.jpg (+ og)"""
import colorsys, html, json, os, re, sys
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); L31 = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from niches import NICHE
from shops import SHOPS
P = json.load(open(os.path.join(L31, 'tpl/lola_parts.json')))
E = html.escape
OUT = os.path.join(L31, 'out')
BOOK = 'https://404growth.com/book?utm_source=propuesta&utm_medium=web&utm_campaign='
WA = 'https://wa.me/34610594450'

IC = {
 'truck': '<path d="M3 7h11v9H3zM14 10h4l3 3v3h-7z"/><circle cx="7" cy="17.5" r="1.6"/><circle cx="17" cy="17.5" r="1.6"/>',
 'store': '<path d="M4.5 10.5V20h15v-9.5M3 10.5 5 4h14l2 6.5c0 1.4-1.3 2.3-2.6 2.3s-2.5-1-2.5-2.3c0 1.4-1.4 2.3-2.9 2.3s-2.9-1-2.9-2.3c0 1.4-1.2 2.3-2.5 2.3S3 11.9 3 10.5zM10 20v-5h4v5"/>',
 'card': '<rect x="2.5" y="5" width="19" height="14" rx="2.5"/><path d="M2.5 9.5h19M6 15h4"/>',
 'chat': '<path d="M20 12a8 8 0 0 1-11.7 7.1L4 20l1-4.1A8 8 0 1 1 20 12z"/>',
 'insta': '<rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r=".6" fill="currentColor"/>',
 'bag': '<path d="M5 8h14l-1 12.5H6zM9 8V6.5a3 3 0 0 1 6 0V8"/>',
 'box': '<path d="M3.5 7.5 12 3l8.5 4.5v9L12 21l-8.5-4.5zM3.5 7.5 12 12l8.5-4.5M12 12v9"/>',
 'chart': '<path d="M4 20V4M4 20h16"/><path d="M8 16v-4M12 16V8M16 16v-6"/>',
 'spark': '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M18 6l-2.5 2.5M8.5 15.5 6 18"/>',
 'bot': '<rect x="4" y="7" width="16" height="12" rx="3"/><path d="M12 7V4M9 13h.01M15 13h.01M9 16.5h6"/>',
 'search': '<circle cx="11" cy="11" r="6.5"/><path d="m20 20-4.2-4.2"/>',
}
def ic(k, c='ic'):
    return f'<svg class="{c}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{IC[k]}</svg>'


def wm(c, size='m'):
    """the shop's logo: their own (transparent PNG) or a wordmark in SF Pro"""
    L = c['logo']
    if L.get('png'):
        return f'<span class="wm"><img src="/p-{c["slug"]}--b--logo.png" alt="{E(c["name"])}"></span>'
    t, sub = L['text'], L.get('sub', '')
    W = 220; tx = W / 2
    fs = L.get('fs', 24); ls = L.get('ls', '0.16em'); fw = L.get('fw', 500)
    s = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 46" role="img" aria-label="{E(c["name"])}">'
         f'<text x="{tx}" y="{27 if sub else 31}" text-anchor="middle" font-family="-apple-system,BlinkMacSystemFont,&#x27;SF Pro Display&#x27;,Inter,Helvetica,sans-serif" font-weight="{fw}" font-size="{fs}" letter-spacing="{ls}" fill="currentColor">{E(t)}</text>')
    if sub:
        s += (f'<text x="{tx}" y="42" text-anchor="middle" font-family="-apple-system,BlinkMacSystemFont,Inter,Helvetica,sans-serif" '
              f'font-size="8.5" letter-spacing="0.3em" fill="currentColor" opacity=".7">{E(sub)}</text>')
    return f'<span class="wm" style="color:var(--wmc)">{s}</svg></span>'


def bi(i, pos='center 40%'):
    return f'data-i="{i}" style="background-position:{pos}"'


# ---------------- the shop (home, mobile home, PDP desktop and mobile) ----------------
def hdr(c, m=False):
    if m:
        return f'<div class="s-hdr m"><span class="burg"><i></i><i></i><i></i></span>{wm(c)}{ic("bag")}</div>'
    return ('<div class="s-hdr"><nav>' + ''.join(f'<span>{E(x)}</span>' for x in c['nav'][:3]) + '</nav>' + wm(c) +
            '<div class="s-r"><span>Buscar</span><span>Cuenta</span><span>Cesta (0)</span></div></div>')


def mq(c):
    x = ''.join(f'<span>{E(s)}</span><i>✦</i>' for s in c['mq'])
    return f'<div class="s-mq"><div>{x}{x}</div></div>'


def pc(c, i, new=False):
    p = c['prods'][i]
    return (f'<div class="pc"><div class="pi" {bi(p["id"], p.get("pos", "center 30%"))}>{"<em>Nuevo</em>" if new else ""}</div>'
            f'<b>{E(p["name"])}</b><span>{E(p.get("price") or c.get("price_txt", "Vuestro precio"))}</span></div>')


def shop_home(c, full=True):
    N = NICHE[c['niche']]; h = c['hero']
    s = f'<div class="shop"><div class="s-ann">{E(c["ann"])}</div>{hdr(c)}'
    s += (f'<div class="s-hero2"><div class="a" {bi("h", c.get("hero_pos", "center"))}></div><div class="s-ht2"><small>{E(h["small"])}</small>'
          f'<h4>{h["h4"]}</h4><div class="bt2"><a class="w">{E(h["b1"])}</a><a>{E(h["b2"])}</a></div></div></div>')
    s += mq(c)
    if not full:
        return s + '</div>'
    s += '<div class="s-cats2">' + ''.join(f'<div {bi(k["id"], k.get("pos", "center 30%"))}><span>{E(k["label"])}<b>→</b></span></div>' for k in c['cats']) + '</div>'
    s += f'<div class="s-sec"><div class="s-h"><h5>{E(c.get("new_h", "Recién llegado"))}</h5><a>Ver todo</a></div><div class="s-grid">' + ''.join(pc(c, i, i < 2) for i in [1, 2, 3, 0]) + '</div></div>'
    lk = c['look']; p0, p1 = [it if isinstance(it, dict) else c['prods'][it] for it in lk['items'][:2]]
    s += (f'<div class="s-stl"><div class="img" {bi("look", lk.get("pos", "center 30%"))}>'
          f'<span class="hs" style="left:{lk["hs"][0][0]}%;top:{lk["hs"][0][1]}%"><i>+</i><em>{E(lk["hs_label"])}</em></span>'
          f'<span class="hs" style="left:{lk["hs"][1][0]}%;top:{lk["hs"][1][1]}%"><i>+</i></span></div>'
          f'<div class="tx"><small>{E(N["look_small"])}</small><h5>{lk["h5"]}</h5><p>{E(N["look_p"])}</p><div class="ls">'
          + ''.join(f'<div><i {bi(p["id"], p.get("pos", "center 30%"))}></i><span><b>{E(p["name"])}</b>{E(p.get("price") or c.get("price_txt", "Vuestro precio"))}</span><em>+</em></div>' for p in (p0, p1))
          + f'</div><a class="btn2">{E(N["look_btn"])}</a></div></div>')
    b = c['big']
    s += f'<div class="s-big" {bi("l5", b.get("pos", "center"))}><div><small>{E(b["small"])}</small><h5>{b["h5"]}</h5><a class="w">{E(b["btn"])}</a></div></div>'
    s += f'<div class="s-rev"><small>{E(c["rev_h"])}</small><div>' + ''.join(f'<figure><blockquote>“{E(q)}”</blockquote><figcaption>{E(a)}</figcaption></figure>' for q, a in c['quotes']) + '</div></div>'
    s += (f'<div class="s-ig"><div class="s-h"><h5>@{E(c["handle"])} en Instagram</h5><a>{ic("insta")}Seguir</a></div><div class="igs">'
          + ''.join(f'<i data-i="{k}"></i>' for k in c['igrid']) + '</div></div>')
    tr = [('truck', 'Envío a domicilio', 'a toda España'), ('store', c['trust_store'][0], c['trust_store'][1]),
          ('card', 'Tarjeta, Bizum, Apple Pay', 'pago seguro'), ('chat', 'WhatsApp', N['wa_trust'])]
    s += '<div class="s-trust">' + ''.join(f'<div>{ic(a)}<b>{E(b_)}</b><span>{E(cc)}</span></div>' for a, b_, cc in tr) + '</div>'
    s += (f'<div class="s-foot"><div>{wm(c)}<p>{E(c["foot_addr"])}</p></div><div><b>Tienda</b><p>{E(c["foot_store"])}</p></div>'
          f'<div><b>Ayuda</b><p>Envíos y cambios<br>{E(N["help2"])}<br>WhatsApp</p></div><div><b>Síguenos</b><p>@{E(c["handle"])}<br>{E(c["followers"])} seguidores</p></div></div>')
    return s + '</div>'


def shop_home_m(c):
    h = c['hero']
    s = f'<div class="shop sm"><div class="s-ann">{E(c["ann_m"])}</div>{hdr(c, True)}'
    s += f'<div class="s-hero m"><div {bi("h", c.get("hero_pos_m", "72% center"))}></div><div class="s-ht"><small>{E(h["small_m"])}</small><h4>{h["h4"]}</h4><a>{E(h["b1"])}</a></div></div>'
    s += '<div class="s-mq m"><div>' + ''.join(f'<span>{E(x)}</span><i>✦</i>' for x in c['mq']) + '</div></div>'
    s += '<div class="s-cats m">' + ''.join(f'<div><i {bi(k["id"], k.get("pos", "center 30%"))}></i><span>{E(k["label"])}</span></div>' for k in c['cats'][:3]) + '</div>'
    s += f'<div class="s-sec"><div class="s-h"><h5>{E(c.get("new_h", "Recién llegado"))}</h5><a>Ver todo</a></div><div class="s-grid">' + pc(c, 1, True) + pc(c, 2, True) + '</div></div>'
    return s + '</div>'


def pdp_inf(c, m=False):
    N = NICHE[c['niche']]; p = c['prods'][0]
    acc = ''.join(f'<div>{E(a)} <i>+</i></div>' for a in N['acc'])
    return (f'<div class="inf{" m" if m else ""}"><div class="crumb">{E(p["crumb"])}</div><h4>{E(p["name"])}</h4>'
            f'<div class="price">{E(p.get("price") or c.get("price_txt", "Vuestro precio"))} <small>IVA incluido</small></div>'
            + (N['variant'](c) if not m and N.get('variant') else '') +
            f'<div class="add">Añadir a la cesta</div><div class="pay"><span>Apple Pay</span><span>Bizum</span><span>Visa</span><span>Mastercard</span></div>'
            f'<div class="acc">{acc}</div><div class="wa">{ic("chat")}<div><b>{E(N["wa_q"])}</b><span>Te contestamos al momento por WhatsApp.</span></div></div></div>')


def shop_pdp(c):
    N = NICHE[c['niche']]; g = c['pdp']
    s = f'<div class="shop"><div class="s-ann">{E(c["ann"])}</div>{hdr(c)}<div class="s-pdp"><div class="g">'
    s += f'<div class="tag" {bi("p1", c["prods"][0].get("pos", "center 30%"))}><em>{E(g["t1"])}</em></div>'
    s += f'<div class="ifg" {bi("x1", g.get("x1pos", "center"))}><span class="t">{E(g["ifg_t"])}</span>'
    for k, (b, sp) in enumerate(g['callouts']):
        s += f'<span class="c c{k + 1}"><i></i><span><b>{E(b)}</b>{E(sp)}</span></span>'
    s += f'</div><div class="tag" {bi("x2", g.get("x2pos", "center 30%"))}><em>{E(g["t2"])}</em></div><div class="tag" {bi("x3", "center")}><em>{E(g["t3"])}</em></div></div>'
    s += pdp_inf(c) + '</div>'
    s += f'<div class="s-sec"><div class="s-h"><h5>{E(N["complete"])}</h5></div><div class="s-grid">' + ''.join(pc(c, i) for i in [1, 2, 4, 3]) + '</div></div>'
    return s + '</div>'


def shop_pdp_m(c):
    s = f'<div class="shop sm"><div class="s-ann">{E(c["ann_m"])}</div>{hdr(c, True)}'
    s += f'<div class="s-pm" {bi("p1", c["prods"][0].get("pos", "center 30%"))}><div class="dots"><i class="on"></i><i></i><i></i><i></i></div></div>'
    return s + pdp_inf(c, True) + '</div>'


def bw(c, inner):
    return f'<div class="bw"><div class="bar"><i></i><i></i><i></i><span>{E(c["domain"])}</span></div><div class="scaler" data-w="1280">{inner}</div></div>'


def phone(c, inner):
    return f'<div class="ph"><div class="mb"><span>{E(c["domain"])}</span></div><div class="scr"><div class="pin">{inner}</div></div></div>'


def cta(c, n, label, small=''):
    return (f'<a class="cta" href="{BOOK}{c["slug"]}&amp;utm_content=cta-{n}" target="_blank" rel="noopener">{label}<span>→</span></a>'
            + (f'<small>{E(small)}</small>' if small else ''))


# ---------------- the proposal ----------------
def body(c):
    N = NICHE[c['niche']]; nm = E(c['name']); sh = E(c['short'])
    o = ('<body>\n<div class="nav"><div class="wrap"><div class="br">' + wm(c) + '<em>×</em>404 Growth</div>'
         '<div class="lk2"><a href="#tienda">01 Tienda</a><a href="#diagnostico">02 Diagnóstico</a><a href="#captacion">03 Captación</a><a href="#plan">04 Plan</a></div>'
         + cta(c, 1, 'Hablamos') + '</div></div>\n')
    o += (f'<header class="hero" id="inicio"><div class="wrap"><div class="hmeta mono"><span>Propuesta privada</span><span>{nm} · {E(c["city"])}</span><span>Noviembre 2026</span></div>'
          f'<h1>{c.get("h1", "Vuestra tienda. <br><span class=\"t\">Abierta 24&nbsp;horas.</span>")}</h1>'
          f'<div class="sub"><p>{c["sub"]}</p><div class="btns">{cta(c, 2, "Quiero mi tienda")}<a class="cta ghost" href="#tienda">Ver la tienda</a></div></div></div>'
          f'<div class="stage"><div class="lap">{bw(c, shop_home(c, False))}</div>{phone(c, shop_home_m(c))}</div>'
          '<div style="padding:0 40px 70px"><div class="kpis">' + ''.join(f'<div><b{" class=t" if k == 3 else ""}>{a}</b><span>{E(b)}</span></div>' for k, (a, b) in enumerate(c['kpis'])) + '</div></div></header>\n')
    o += (f'<section class="sec ba" id="antes"><div class="wrap"><div class="chap"><span class="num">↔</span><span class="lb">Antes y después</span></div>'
          f'<div class="head"><h2>{c["ba_h2"]}</h2><p>{c["ba_p"]}</p></div>'
          f'<div class="baw" style="--p:50%"><img class="b0" src="/p-{c["slug"]}--antes.jpg" width="1280" height="697" alt="{E(c["before_label"])} hoy">'
          f'<img class="b1" src="/p-{c["slug"]}--despues.jpg" width="1280" height="697" alt="La tienda online de {nm} que proponemos">'
          f'<span class="bl l">Hoy · {E(c["before_label"])}</span><span class="bl r">Con 404 Growth</span><div class="bh"><i>‹ ›</i></div>'
          '<input type="range" min="0" max="100" value="50" aria-label="Comparar antes y después"></div>'
          '<p class="bahint">Arrastrad el círculo hacia los lados</p></div></section>\n')
    o += (f'<section class="sec shopsec" id="tienda"><div class="wrap"><div class="chap"><span class="num">01</span><span class="lb">La tienda</span></div>'
          f'<div class="head"><h2>Así se vería<br>{nm} online.</h2><p>{E(N["tienda_p"])}</p></div>'
          f'{bw(c, shop_home(c))}<div class="ctarow">{cta(c, 3, "Quiero esta tienda para " + sh)}</div>'
          f'<div class="pdpx"><div><h3 style="font-size:44px;letter-spacing:-.04em;margin-bottom:30px">{N["pdp_h3"]}</h3><div class="cas">'
          + ''.join(f'<div class="ca"><span class="n">{k + 1:02d}</span><div><b>{E(a)}</b><p>{E(b)}</p></div></div>' for k, (a, b) in enumerate(N['pdp_points']))
          + f'</div></div>{phone(c, shop_pdp_m(c))}</div><div class="pdpd">{bw(c, shop_pdp(c))}</div></div></section>\n')
    d = c['diag']
    o += (f'<section class="sec" id="diagnostico"><div class="wrap"><div class="chap"><span class="num">02</span><span class="lb">Diagnóstico</span></div>'
          f'<div class="head"><h2>{d["h2"]}</h2><p>{d["p"]}</p></div><div class="flowx">'
          f'<div class="fx"><div class="top"><span class="mono" style="color:var(--mute)">Cómo se compra hoy</span><b>{len(N["flow_today"])}<small>pasos</small></b></div><div class="tl">'
          + ''.join(f'<div class="nd"><i></i><b>{E(a)}</b><span>{E(b.replace("{city}", c["city"]))}</span></div>' for a, b in N['flow_today'])
          + f'</div></div><div class="fx"><div class="top"><span class="mono t">Con vuestra tienda</span><b class="t">{len(N["flow_new"])}<small>pasos</small></b></div><div class="tl on">'
          + ''.join(f'<div class="nd"><i></i><b>{E(a)}</b><span>{E(b)}</span></div>' for a, b in N['flow_new'])
          + '</div><div class="note">Sin esperas · a cualquier hora · desde cualquier sitio</div></div></div>')
    o += '<div class="assets">' + ''.join(f'<div class="as"><div class="big t">{a}</div><b>{E(b)}</b><p>{E(p)}</p></div>' for a, b, p in d['assets'])
    o += ('<div class="as"><div class="ph5">' + ''.join(f'<i data-i="{k}"></i>' for k in ['l1', 'p2', 'l3', 'p4', 'x2', 'l4']) +
          '</div><b>Contenido que vende</b><p>Fotos con nivel de marca, listas para la tienda y para anuncios.</p></div></div>')
    o += ('<h3 style="font-size:34px;letter-spacing:-.035em;margin:110px 0 30px">Dónde se escapan hoy las ventas</h3><div class="leaks">'
          + ''.join(f'<div class="lk"><span class="n">{k + 1:02d}</span><b>{E(a)}</b><p>{E(b)}</p></div>' for k, (a, b) in enumerate(d['leaks']))
          + f'</div><div class="ctarow">{cta(c, 4, "Recuperar esas ventas", "15 minutos · sin compromiso")}</div></div></section>\n')
    o += ('<section class="sec dark" id="mercado"><div class="wrap"><div class="chap"><span class="num">+</span><span class="lb">Contexto de mercado</span></div><div class="mkt two">'
          '<div class="mk"><b>114.800<em> M€</em></b><p>facturó el comercio electrónico en España en 2025.</p><small>Fuente: CNMC · <a href="https://www.alimarket.es/electro/noticia/428689/el-comercio-electronico-supero-en-espana-los-114-800-m-en-2025" target="_blank" rel="noopener">CNMCData, 2026</a></small></div>'
          '<div class="mk"><b>70<em>%</em></b><p>de los carritos se abandonan. Por eso la tienda recupera cada uno por email y WhatsApp.</p><small>Fuente: <a href="https://baymard.com/lists/cart-abandonment-rate" target="_blank" rel="noopener">Baymard Institute</a> · media de 50 estudios</small></div>'
          f'</div><div class="takeaway"><p>El comercio online no deja de crecer en España. <em>{E(N["take"])}</em></p></div></div></section>\n')
    o += ('<section class="sec dark" id="captacion"><div class="wrap"><div class="chap"><span class="num">03</span><span class="lb">Captación</span></div>'
          '<div class="head"><h2>Una tienda sin tráfico<br>es un escaparate cerrado.</h2><p>Por eso no entregamos solo una web: montamos el sistema completo que lleva al cliente del post a la compra, y de la compra a la siguiente.</p></div>'
          '<div class="fun-h"><span>Descubre</span><span>Considera</span><span>Compra</span><span>Resuelve</span><span>Repite</span></div><div class="fun">'
          + ''.join(f'<div class="fs"><span class="n">{k + 1:02d}</span><b>{a}</b><em>{b}</em><p>{p}</p><small>{s_}</small></div>' for k, (a, b, p, s_) in enumerate([
              ('Contenido', f'Instagram · {E(c["followers"])}', f'Los reels y posts que ya hacéis, ahora con {N["item_pl"]} etiquetadas.', 'Alcance · guardados'),
              ('Anuncios', 'Meta Ads', f'Captación en toda España y retargeting a quien ya os vio.', 'CTR · CPC'),
              ('Tienda', 'Ficha + checkout', N['fun_shop'], 'Conversión · ticket medio'),
              ('Asistente IA', 'WhatsApp 24/7', N['fun_bot'], 'Respuesta · recuperadas'),
              ('Recompra', 'CRM + email', N['fun_crm'], 'Recompra · valor de cliente')]))
          + '</div>' + ads(c) + f'<div class="ctarow dk">{cta(c, 5, "Lanzar estas campañas", "Os preparamos la primera tanda")}</div></div></section>\n')
    o += (f'<section class="sec" id="cambia"><div class="wrap"><div class="chap"><span class="num">+</span><span class="lb">Lo que cambia</span></div>'
          f'<div class="head"><h2>Más ventas.<br>Sin abrir otro local.</h2><p>Un segundo canal de ingresos que trabaja con el mismo stock, el mismo equipo y {E(c["the_store"])}.</p></div><div class="chg">'
          '<div class="cg w"><span class="n">01</span><div><b>24/7</b><p>Compran solas: de noche, en festivos y también en vacaciones.</p></div></div>'
          f'<div class="cg"><span class="n">02</span><div><b>{len(N["flow_new"])}</b><p>pasos para comprar, en lugar de {len(N["flow_today"])}.</p></div></div>'
          '<div class="cg"><span class="n">03</span><div><b>2º</b><p>canal de ingresos, sin alquiler ni personal extra.</p></div></div>'
          f'<div class="cg im" data-i="l2"><div><span class="n" style="color:#fff">04</span><b style="margin-top:12px">Cada post,<br>comprable.</b><p>De la foto de Instagram a la cesta en un toque.</p></div></div>'
          f'<div class="cg"><span class="n">05</span><div><b>+</b><p>{E(N["cambia5"])}</p></div></div>'
          '<div class="cg"><span class="n">06</span><div><b>100%</b><p>de las ventas medidas: qué, a quién y desde dónde.</p></div></div>'
          f'<div class="cg c2"><span class="n">07</span><div><b style="font-size:34px;letter-spacing:-.04em">Sin riesgo</b><p>{E(N["cambia7"])}</p></div></div>'
          '<div class="cg c2"><span class="n">08</span><div><b style="font-size:34px;letter-spacing:-.04em">Datos</b><p>Saber en qué ciudades os compran antes de dar el siguiente paso.</p></div></div>'
          f'</div><div class="ctarow">{cta(c, 6, "Lo quiero para " + sh)}</div></div></section>\n')
    o += plan(c)
    o += (f'<section class="close" id="hablar" data-i="h"><div class="wrap"><div class="chap"><span class="num">→</span><span class="lb">Siguiente paso</span></div>'
          f'<h2>¿Abrimos {sh}<br><span class="t">a toda España?</span></h2><div class="row"><p>Os lo enseñamos en 15 minutos, con vuestro catálogo y en directo.</p>'
          f'<div class="btns"><a class="cta" href="{WA}" target="_blank" rel="noopener">Escribidnos por WhatsApp<span>→</span></a>'
          f'<a class="cta ghost" href="{BOOK}{c["slug"]}&amp;utm_content=cta-8" target="_blank" rel="noopener">Reservar videollamada</a></div></div></div></section>\n'
          f'<footer id="pie"><div class="wrap"><span>Demo de concepto de 404 Growth. No es la web oficial.</span><span>Marca y productos: {nm} · @{E(c["handle"])}. Fotos de la tienda creadas con IA a partir de sus productos reales.</span></div></footer>\n')
    return o


def ad(c, inner, foot, label):
    a = E(c['handle']); ini = E(c['name'][0].upper())
    return (f'<div class="adw"><div class="ad"><div class="ah"><span class="av"><i>{ini}</i></span><b>{a}</b><small>Publicidad</small><em>···</em></div>'
            f'<div class="am">{inner}</div><div class="af"><span>{E(foot)}</span><b>›</b></div></div><p class="al">{label}</p></div>')


def ads(c):
    N = NICHE[c['niche']]; A = c['ads']; p = c['prods']
    g = ad(c, f'<div class="ab" {bi("x2", "center 30%")}></div><div class="ao bl"><small>{E(A.get("a1s", "Nueva colección"))}</small><h6 style="font-size:26px">{A["a1"]}</h6><span class="pill">Comprar</span></div>',
           'Comprar ahora', '<b>Producto estrella</b> · retargeting a quien vio el post')
    g += ad(c, f'<div class="ab" {bi("l1", "center 30%")}></div><div class="ao tp"><h6>De {E(c["city_short"])}<br>a toda España.</h6></div>',
            'Comprar ahora', f'<b>Envío</b> · captación fuera de {E(c["city_short"])}')
    g += ad(c, f'<div class="ab cr"><div class="col"><i data-i="{p[1]["id"]}"></i><b>+</b><i data-i="{p[2]["id"]}"></i><b>+</b><i data-i="{p[3]["id"]}"></i></div><h6 class="dk">{A["a3"]}</h6></div>',
            N['ad3_btn'], f'<b>{E(N["complete"])}</b> · sube el ticket medio')
    g += ad(c, f'<div class="ab tc"><div class="qt">“{E(c["quotes"][0][0])}”<small>{E(c["quotes"][0][1])}</small></div><i class="rd" data-i="l3"></i></div>',
            'Comprar ahora', '<b>Vuestra voz</b> · lo que ya contáis en Instagram')
    g += ad(c, f'<div class="ab sp"><i data-i="look"></i><div class="bl2"><small>En {E(c["short"])}</small>' + ''.join(f'<span>{E(k["label"])}</span>' for k in c['cats']) + '<span>Novedades</span></div></div>',
            'Descubrir', '<b>Catálogo</b> · todo lo que tenéis, a un toque')
    g += ad(c, f'<div class="ab" {bi("l4", "center 30%")}></div><div class="ao bl"><small>{E(A["a6s"])}</small><h6>{A["a6"]}</h6><span class="pill">{E(A["a6b"])}</span></div>',
            'Enviar mensaje', A['a6l'])
    return ('<div class="adsx"><div class="adsh"><h3>Primeras creatividades</h3><p>Hechas con vuestras fotos. Cada una con un objetivo distinto dentro del embudo.</p></div>'
            f'<div class="adg">{g}</div></div>')


def plan(c):
    N = NICHE[c['niche']]
    st = [('store', 'Tienda online propia', N['stack1']), ('card', 'Pagos', 'Tarjeta, Bizum y Apple Pay en el checkout.'),
          ('box', 'Stock unificado', f'Lo que se vende en {c["stock_where"]} se descuenta online, y al revés.'),
          ('insta', 'Instagram Shopping', f'Cada post y cada reel, con {N["item_art"]} etiquetada.'),
          ('chart', 'Píxel + API de conversiones', 'Medición fiable de cada venta que llega por anuncios.'),
          ('bot', 'Asistente IA + CRM', 'WhatsApp que responde 24/7 y ficha de cada cliente.')]
    ph = [('Día 0', 'Llamada de arranque', 'Os escuchamos y nos contáis cómo funciona la tienda.', 0, 1),
          ('Días 0–3', 'Accesos y vuestra tienda', 'Dominio, pagos y lo que haga falta, con vosotros.', 0, 3),
          ('Días 3–8', 'Diseño', 'La tienda con vuestra marca y vuestras fotos.', 3, 5),
          ('Días 3–10', 'Catálogo', N['plan_cat'], 3, 7),
          ('Días 8–13', 'Pagos, envíos y stock', 'Checkout, tarifas de envío y stock unificado.', 8, 5),
          ('Días 13–14', 'Pedido de prueba', 'Compramos de verdad para comprobarlo todo.', 13, 2),
          ('Día 15', 'Lanzamiento', 'Tienda abierta, Instagram Shopping y medición activa.', 14, 1)]
    g = ('<div class="gantt g15"><div class="gh"><span style="border:0;padding-left:0">Los 15 días</span><div>'
         + ''.join(f'<span>{k}</span>' for k in range(1, 16)) + '</div></div>')
    for a, b, p, s0, w in ph:
        g += (f'<div class="gr"><div class="gl"><small>{a}</small><b>{b}</b><p>{p}</p></div><div class="gt">' + '<i></i>' * 15 +
              f'<span style="left:{s0 / 15 * 100:.2f}%;width:{w / 15 * 100:.2f}%"></span></div></div>')
    g += '</div>'
    return (f'<section class="sec" id="plan" style="background:var(--cream)"><div class="wrap"><div class="chap"><span class="num">04</span><span class="lb">Plan y sistema</span></div>'
            '<div class="head"><h2>Todo lo que montamos,<br>conectado.</h2><p>Una sola pieza: tienda, pagos, stock, Instagram, anuncios, asistente y CRM hablando entre sí desde el primer día.</p></div>'
            '<div class="stack">' + ''.join(f'<div class="sk">{ic(i)}<b>{E(b)}</b><p>{E(p)}</p></div>' for i, b, p in st) + '</div>' + g +
            '<div class="next"><div class="nx"><span class="n">Paso 1</span><b>Llamada de 15 min</b><p>Os enseñamos esta propuesta con vuestro catálogo, en directo.</p></div>'
            f'<div class="nx"><span class="n">Paso 2</span><b>{E(N["next2"][0])}</b><p>{E(N["next2"][1])}</p></div>'
            f'<div class="nx"><span class="n">Paso 3</span><b>Arrancamos</b><p>En 15 días, {E(c["short"])} vende online.</p></div></div>'
            f'<div class="ctarow">{cta(c, 7, "Reservar la llamada", "Sin compromiso")}</div></div></section>\n')


def _rgb(h):
    h = h.lstrip('#'); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _hex(r):
    return '#%02X%02X%02X' % tuple(max(0, min(255, int(round(x)))) for x in r)


def _hls(h, dl=0.0, ds=0.0, dh=0.0, l=None, s=None):
    r, g, b = [x / 255 for x in _rgb(h)]; H, L_, S = colorsys.rgb_to_hls(r, g, b)
    H = (H + dh) % 1; L_ = l if l is not None else min(1, max(0, L_ + dl)); S = s if s is not None else min(1, max(0, S + ds))
    return _hex([x * 255 for x in colorsys.hls_to_rgb(H, L_, S)])


def palette(c):
    col = c['colors']; t = col['t']; td = col.get('td') or _hls(t, -.12); tl = col.get('tl') or _hls(t, l=.78)
    rgb = lambda h: ','.join(str(x) for x in _rgb(h))
    a1 = _hls(t, l=.80, s=.55); a2 = col.get('a2') or _hls(t, l=.86, s=.35, dh=.08)
    deep = _hls(t, l=.08, s=.35); ink = col.get('ink', '#141110')
    return (':root{--t:%s;--td:%s;--tl:%s;--ta:%s;--tr:%s;--a1:%s;--a2:%s;--sh:%s;--gb:%s;--rim:%s;--cream:%s;--ink:%s;--deep:%s;--deep3:%s;--tl2:%s;--tl3:%s;'
            "--wmf:-apple-system,BlinkMacSystemFont,'SF Pro Display',Inter,Helvetica,sans-serif;--wmw:500;--wml:.12em;--wmt:uppercase}"
            % (t, td, tl, tl, rgb(t), rgb(a1), rgb(a2), rgb(_hls(t, l=.14)), rgb(td), rgb(tl), col['cream'], ink, deep, rgb(deep), _hls(t, l=.68), rgb(_hls(t, l=.68))))


# ---------------- head, images, scripts ----------------
IMG_MAX = {'h': 2400, 'l5': 2000, 'x1': 1200}


def head(c, ids):
    s = c['slug']; nm = E(c['name']); N = NICHE[c['niche']]
    title = f'{nm} × 404 Growth · Vuestra {N["shop_of"]} online'
    desc = f'Así se vería la tienda online de {nm}: con vuestras {N["item_pl"]} y vuestro estilo, lista para vender en toda España.'
    st0 = P['styles'][0]
    col = c['colors']
    st0 = st0.replace('</style>', palette(c) + '</style>')
    v2 = (f'<style id="v2">[data-i="h"]{{background-image:url(/p-{s}--b--h.jpg)!important;background-size:cover;background-position:{c.get("hero_pos", "center")}}}'
          '.s-ht2 h4{font-size:66px!important}.s-hero2{grid-template-columns:1fr!important}'
          f'.s-hero.m [data-i="h"]{{background-position:{c.get("hero_pos_m", "72% center")}}}.close[data-i="h"]{{background-position:{c.get("close_pos", "center 40%")}!important}}'
          + (c.get('hero_css') or '.s-hero2:after,.s-hero.m:after{background:linear-gradient(90deg,rgba(20,14,10,.55),rgba(20,14,10,.25) 40%,rgba(20,14,10,0) 65%)!important}') +
          '.s-ht2 h4 em,.s-ht h4 em{font-style:normal!important;font-weight:500!important}.wm{color:var(--wmc)}:root{--wmc:var(--ink)}'
          '.gantt.g15 .gh div:last-child,.gantt.g15 .gt{grid-template-columns:repeat(15,1fr)!important}'
          '.close:before{background:linear-gradient(180deg,rgba(14,10,9,.3),rgba(14,10,9,.86) 76%)!important}</style>')
    v3i = '<style id="v3i">' + ''.join(f'[data-i="{i}"]{{background-image:url(/p-{s}--b--{i}.jpg)!important}}' for i in ids if i != 'h') + '</style>'
    return ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow">'
            f'<title>{title}</title><meta name="description" content="{desc}"><meta property="og:type" content="website"><meta property="og:site_name" content="404 Growth">'
            f'<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="https://404growth.com/p-{s}--b--og.jpg">'
            '<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">'
            '<link rel="icon" href="/favicon.svg" type="image/svg+xml">' + P['scripts_head'][0] + st0 + v2 + P['styles'][2] + P['styles'][3] + v3i + '</head>')


def scripts(c):
    sb = P['scripts_body']
    cnt = sb[2].replace('var slug="lola-shop-madrid"', f'var slug="{c["slug"]}"')
    assert f'var slug="{c["slug"]}"' in cnt
    return sb[0] + sb[1] + cnt + sb[4] + sb[5] + '</body></html>'


def images(c):
    s = c['slug']; src = os.path.join(L31, 'ai', s); ids = []
    m = {'h': 'hero'}
    for i in ['h', 'p1', 'p2', 'p3', 'p4', 'p5', 'x1', 'x2', 'x3', 'look', 'l1', 'l2', 'l3', 'l4', 'l5']:
        f = os.path.join(src, m.get(i, i) + '.jpg')
        if not os.path.exists(f):
            print('  falta', s, i); continue
        im = Image.open(f).convert('RGB'); mx = IMG_MAX.get(i, 1100)
        if max(im.size) > mx:
            im.thumbnail((mx, mx), Image.LANCZOS)
        im.save(os.path.join(OUT, f'p-{s}--b--{i}.jpg'), 'JPEG', quality=84, optimize=True, progressive=True)
        ids.append(i)
    # og 1200x630 from the hero
    im = Image.open(os.path.join(src, 'hero.jpg')).convert('RGB'); w, h = im.size; r = 1200 / 630
    cw, ch = (w, int(w / r)) if w / h < r else (int(h * r), h)
    fx = c.get('og_fx', .5); x0 = int((w - cw) * fx); y0 = (h - ch) // 2
    im.crop((x0, y0, x0 + cw, y0 + ch)).resize((1200, 630), Image.LANCZOS).save(os.path.join(OUT, f'p-{s}--b--og.jpg'), 'JPEG', quality=86, optimize=True)
    if c['logo'].get('png'):
        Image.open(c['logo']['png']).save(os.path.join(OUT, f'p-{s}--b--logo.png'), optimize=True)
    return ids


def build(slug):
    c = SHOPS[slug]; c['slug'] = slug
    os.makedirs(OUT, exist_ok=True); os.makedirs(os.path.join(L31, 'shots'), exist_ok=True)
    ids = images(c)
    h = head(c, ids) + body(c) + scripts(c)
    open(os.path.join(OUT, f'p-{slug}.html'), 'w').write(h)
    open(os.path.join(L31, 'shots', f'{slug}-shop.html'), 'w').write(shot_html(c))
    left = re.findall(r'\{[a-z_]+\}', re.sub(r'<(script|style)[^>]*>.*?</\1>', '', h, flags=re.S))
    print('ok', slug, len(h), 'imgs', len(ids), 'placeholders', left[:5])


def shot_html(c):
    """just the shop home at 1280 px, for the «después» screenshot"""
    ids = [i for i in ['h', 'p1', 'p2', 'p3', 'p4', 'p5', 'x1', 'x2', 'x3', 'look', 'l1', 'l2', 'l3', 'l4', 'l5']]
    return (head(c, ids) + '<body style="margin:0;width:1280px;overflow:hidden"><div style="position:relative;width:1280px">'
            + shop_home(c).replace('<div class="shop">', '<div class="shop" style="position:relative;transform:none">', 1) + '</div></body></html>')


if __name__ == '__main__':
    for s in sys.argv[1:]:
        build(s)
