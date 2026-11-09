#!/usr/bin/env python3
"""Portada v67 (9/11/2026): las 10 secciones elegidas en el lienzo «Nueva home · 404growth.com».

Uso: python3 build.py <index-actual.html> <salida.html>
Del index actual solo se reutilizan el <head> (SEO, Open Graph y schema con las 9 preguntas)
y el cargador 404. Todo lo demás sale de aquí y de v67.css.
"""
import re, sys, pathlib

SRC, OUT = sys.argv[1], sys.argv[2]
HERE = pathlib.Path(__file__).parent
old = open(SRC, encoding='utf-8').read()

# ---------- lo que se conserva del index actual
head = old[:old.find('<style')]
head = head.replace('<link rel="preload" href="/inter-tight.woff2" as="font" type="font/woff2" crossorigin>\n', '')
loader = re.search(r'<div id="l404".*?</svg></div></div>', old, flags=re.S).group(0)
loader_css = []
css_old = '\n'.join(re.findall(r'<style[^>]*>(.*?)</style>', old, flags=re.S))
for m in re.finditer(r'(#l404[^{]*\{[^}]*\})', css_old):
    loader_css.append(m.group(1))
for m in re.finditer(r'(@keyframes l404\w+\{(?:[^{}]*\{[^}]*\})+\})', css_old):
    loader_css.append(m.group(1))
LOADER_CSS = '\n'.join(dict.fromkeys(loader_css)) + '\n@media (prefers-reduced-motion:reduce){#l404 .d,#l404 .tr,#l404 .sh{animation:none;stroke-dashoffset:0}#l404 .tr{opacity:0}#l404 .lw{transition:opacity .3s!important}}'

CSS = (HERE / 'v67.css').read_text(encoding='utf-8')

# ---------- enlaces
WA = 'https://wa.me/34610594450?text=Hola%20Christian%2C%20tengo%20una%20tienda%20f%C3%ADsica%20y%20quiero%20venderla%20online.%20Mi%20tienda%20es%3A%20'
def book(c): return f'/book?utm_source=web&amp;utm_medium=portada&amp;utm_campaign={c}'
def wa_attrs(c): return f'href="{WA}" target="_blank" rel="noopener" data-cta="wa-{c}"'

# ---------- iconos
I_ARROW = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17L17 7"/><path d="M8 7h9v9"/></svg>'
I_WA = re.search(r'<a class="waf"[^>]*>(<svg.*?</svg>)', old, flags=re.S).group(1)
I_CHECK = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
I_PLUS = '<svg viewBox="0 0 14 14" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M7 1v12M1 7h12"/></svg>'
I_MENU = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 8h16M4 16h16"/></svg>'
I_DOWN = '<svg viewBox="0 0 12 12" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M6 1v10M2 7l4 4 4-4"/></svg>'
I_BAG = '<svg viewBox="0 0 24 24" aria-hidden="true" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 8h14l-1.2 12H6.2z"/><path d="M9 8V7a3 3 0 0 1 6 0v1" fill="none"/></svg>'
MARK = '<svg class="mk" viewBox="20 60 362 280" aria-hidden="true"><g transform="skewX(-12) translate(52 0)" fill="none" stroke="#D4F27A" stroke-width="32" stroke-linecap="round" stroke-linejoin="round"><rect x="140" y="90" width="120" height="220" rx="60"/><path d="M155.1 110.2 L40 240 L140 240"/><path d="M244.9 110.2 L360 240 L260 240"/></g></svg>'

def btn_lime(text, href, cta, extra=''):
    return f'<a class="b-lime{extra}" href="{href}" data-cta="{cta}">{text}<span class="ic">{I_ARROW}</span></a>'
def btn_wa(text, c, extra=''):
    return f'<a class="b-lime wa{extra}" {wa_attrs(c)}>{text}<span class="ic">{I_WA}</span></a>'
def btn_gl(text, href, cta=None, extra=''):
    d = f' data-cta="{cta}"' if cta else ''
    return f'<a class="b-gl{extra}" href="{href}"{d}>{text}</a>'
def chip(t): return f'<span class="chip"><i></i>{t}</span>'

# ---------- datos
STORES = [
    ('solenne', 'Solenne', 'Moda mujer', 'Moda mediterránea premium: campaña editorial, tallas y «completa el look».'),
    ('aurea', 'Áurea', 'Joyería', 'Joyería de oro de 18 k con grabado, caja de regalo y envío asegurado.'),
    ('pulso', 'Pulso', 'Sneakers', 'Tienda multimarca: lanzamientos, stock por talla y entrega en 24 h.'),
    ('nacar', 'Nácar', 'Cosmética', 'Skincare moderno: rutinas en packs, muestras de regalo y envío en 24 h.'),
    ('forma', 'Forma', 'Suplementos', 'Nutrición deportiva premium con suscripción y precios por toma.'),
]
STEPS = [
    ('Día 0', 'Hablamos', 'Me escribes por WhatsApp o reservas una llamada. En la llamada de arranque, de una hora, hacemos juntos lo más técnico, como los accesos.', ['WhatsApp', 'Llamada de arranque']),
    ('Días 1–14', 'Montamos tu tienda', 'Nos pasas fotos, precios y productos por WhatsApp. Nosotros diseñamos la tienda con tu marca y dejamos pagos y envíos listos.', ['Tu marca', 'Fichas de producto', 'Bizum y Apple Pay', 'Envíos', 'Stock']),
    ('Día 15', 'Abres online', 'Tu tienda abierta y midiendo ventas. Después, anuncios en Meta y email marketing para traer compradores.', ['Tienda abierta', 'Instagram Shopping', 'Ventas medidas']),
]
BENEFITS = [
    ('24/7', 'Pueden comprarte fuera de horario, en festivos y en vacaciones.'),
    ('Toda España', 'Vendes fuera de tu zona, no solo a quien pasa por la puerta.'),
    ('Menos mensajes', 'Precio, talla y pago en la ficha: menos ventas a golpe de DM.'),
    ('Recogida en tienda', 'Compran online y recogen en tu tienda: más visitas al mostrador.'),
    ('Datos', 'Ves qué vende, a quién y desde dónde, sin suposiciones.'),
    ('Recompra', '«Completa el look», productos relacionados y novedades para quien ya te compró.'),
]
FUNNEL = [
    ('01', 'Anuncios en Meta', 'Te descubren', 'Tus productos delante de quien aún no te conoce, en toda España.'),
    ('02', 'Retargeting', 'Te consideran', 'Volvemos a mostrar tus productos a quien ya visitó la tienda.'),
    ('03', 'Tienda', 'Te compran', 'Talla, stock y pago en tres pasos. Sin escribir a nadie.'),
    ('04', 'Email de cesta', 'Vuelven', 'Cada cesta abandonada recibe un recordatorio para terminar la compra.'),
    ('05', 'Email marketing', 'Repiten', 'Novedades y «vuelve a estar disponible» para quien ya te compró.'),
]
INC = ['Diseño y desarrollo de la tienda con tu marca', 'Fichas de producto, catálogo y pago', 'Pagos, envíos y recogida en tienda configurados', 'Instagram Shopping y medición de ventas', 'Te enseñamos a gestionar pedidos y productos']
APO = ['Tus productos, precios y stock', 'Las fotos que ya tienes (si faltan, lo vemos contigo)', 'Acceso a tu dominio y redes, si ya los tienes', 'Una persona que prepare los pedidos']
COS = ['Dominio, si aún no tienes', 'Cuota de Shopify', 'Comisión de la pasarela de pago por venta', 'Envíos, según transportista', 'Presupuesto de anuncios, si haces campañas']
# las preguntas salen del schema FAQPage del <head>, para que la página y el schema digan lo mismo
FAQ = re.findall(r'"@type":"Question","name":"(.*?)","acceptedAnswer":\{"@type":"Answer","text":"(.*?)"\}', head)
assert len(FAQ) == 9, len(FAQ)
SECT = [('Moda', '/tienda-online/moda'), ('Joyería', '/tienda-online/joyeria'), ('Deporte', '/tienda-online/deportes'), ('Decoración', '/tienda-online/decoracion-y-hogar'), ('Obradores', '/tienda-online/pasteleria'), ('Regalos', '/tienda-online/regalos-y-artesania')]
GUIDES = [('Diseño de tienda online', '/diseno-tienda-online'), ('Cómo crear una tienda online', '/crear-tienda-online'), ('Cuánto cuesta hacer una tienda online', '/guia/cuanto-cuesta-una-tienda-online'), ('Pasar tu tienda física a online', '/guia/pasar-tienda-fisica-a-online'), ('Tienda online por sector', '/tienda-online'), ('Shopify o WooCommerce', '/guia/shopify-vs-woocommerce')]
FOOT = [('Diseño de tienda online', '/diseno-tienda-online'), ('Crear tienda online', '/crear-tienda-online'), ('Tienda online por sector', '/tienda-online'), ('Guías', '/guia'), ('Blog', '/blog'), ('Aviso legal y privacidad', '/legal')]
CNMC = 'https://www.ondavasca.com/el-comercio-electronico-factura-114-800-millones-en-2025/'
BAYMARD = 'https://baymard.com/lists/cart-abandonment-rate'

# ---------- 0 · cabecera fija y menú del móvil
NAV = f'''<a class="skip" href="#contenido">Saltar al contenido</a>
<header class="nv" id="nv"><div class="nv-in">
<a class="nv-logo" href="/" aria-label="404 Growth, inicio">{MARK}<span>404 Growth</span></a>
<nav class="nv-lk" aria-label="Secciones"><a href="#como">Cómo funciona</a><a href="#tiendas">Tiendas</a><a href="#plan">Qué incluye</a><a href="#preguntas">Preguntas</a><a href="/guia">Guías</a></nav>
<a class="nv-cta" {wa_attrs('cabecera')}>Hablamos</a>
<button class="nv-mb" type="button" aria-label="Abrir menú" aria-expanded="false" aria-controls="mm">{I_MENU}</button>
</div></header>
<div class="mm" id="mm" hidden><nav aria-label="Menú"><a href="#como">Cómo funciona</a><a href="#tiendas">Tiendas de ejemplo</a><a href="#plan">Qué incluye</a><a href="#preguntas">Preguntas</a><a href="/guia">Guías</a></nav>
<div class="mm-b">{btn_lime('Reservar llamada de 30 min', book('menu'), 'menu', ' full')}{btn_gl('Escríbeme por WhatsApp', WA, 'wa-menu', ' full')}</div></div>'''
NAV = NAV.replace(f'class="b-gl full" href="{WA}" data-cta="wa-menu"', f'class="b-gl full" {wa_attrs("menu")}')

# ---------- 1 · portada (C · cristal sobre tus tiendas)
order = ['solenne', 'pulso', 'nacar', 'aurea', 'forma']
cols = []
for c in range(6):
    imgs = ''.join(f'<img src="/home--w--{order[(c * 2 + r) % 5]}.webp" alt="" width="380" height="520" decoding="async">' for r in range(5))
    cols.append(f'<div class="wc">{imgs}</div>')
HERO = f'''<section class="hero" id="inicio">
<div class="wall" aria-hidden="true"><div class="wall-in">{''.join(cols)}</div></div>
<div class="hero-ov" aria-hidden="true"></div>
<div class="hero-in">
<div class="hero-p gx">
{chip('De tienda física a tienda online').replace('class="chip"', 'class="chip dk"')}
<h1>Pasamos tu tienda física <br class="d"><span class="lm">a tienda online en 15 días.</span></h1>
<p>Tienda en Shopify con tu marca y a tu nombre, y anuncios y contenido que te traen clientes de toda España. Abierta 24 horas; tú sigues en tu local.</p>
<div class="btns" id="hero-btns">{btn_lime('Reservar llamada de 30 min', book('portada'), 'portada')}{btn_gl('Ver tiendas de ejemplo', '#tiendas')}</div>
</div>
<ul class="hchips"><li><b>15 días</b><span>hasta abrir</span></li><li><b>Shopify</b><span>a tu nombre</span></li><li><b>30 min</b><span>de llamada<span class="d"> para empezar</span></span></li></ul>
</div>
<p class="hnote">Tiendas de demostración de fondo</p>
</section>'''

# ---------- 2 · cómo funciona (A · línea de tiempo)
st = ''.join(f'''<li class="st rv" style="--d:{i * 90}ms"><span class="day">{d}</span><span class="dot" aria-hidden="true"></span>
<article class="card gl"><span class="day-m">{d}</span><h3>{t}</h3><p>{p}</p><div class="tags">{''.join(f'<span>{x}</span>' for x in tags)}</div></article></li>''' for i, (d, t, p, tags) in enumerate(STEPS))
COMO = f'''<section class="sec como" id="como"><div class="w">
<header class="sh c rv">{chip('Cómo funciona')}<h2>Tres pasos. <br class="m"><span class="lm">Quince días.</span></h2><p>De tu mostrador a toda España, sin que tengas que saber de tecnología.</p></header>
<ol class="tl">{st}</ol>
</div></section>'''

# ---------- 3 · tiendas de ejemplo (C · lista con vista previa, sin enlaces)
lst = ''.join(f'''<button type="button" class="ts{' on' if i == 0 else ''}" role="tab" aria-selected="{'true' if i == 0 else 'false'}" aria-controls="pv" data-i="{i}"><span class="n">0{i + 1}</span><span class="nm">{n}</span><span class="sc">{s}<i aria-hidden="true">{I_ARROW}</i></span></button>''' for i, (k, n, s, d) in enumerate(STORES))
data = ','.join(f'["{k}","{n}","{s}","{d}"]' for k, n, s, d in STORES)
TIENDAS = f'''<section class="sec tnd" id="tiendas"><div class="w tnd-g">
<header class="sh tnd-h rv">{chip('Tiendas de ejemplo')}<h2>Así puede verse <span class="lm">la tuya.</span></h2><p>Tiendas de demostración que hemos diseñado. Elige una y mira cómo queda.</p></header>
<div class="tnd-list" role="tablist" aria-label="Tiendas de demostración">{lst}</div>
<figure class="tnd-pv gx rv" id="pv" role="tabpanel" aria-live="polite">
<div class="bar"><span class="tl3" aria-hidden="true"><i></i><i></i><i></i></span><span class="url">Tienda de demostración · <b id="pvn">Solenne</b></span></div>
<div class="scr"><img id="pvi" src="/demos/cards/solenne.webp" alt="Tienda de demostración Solenne" width="760" height="1040" loading="lazy" decoding="async"></div>
<figcaption><p id="pvd">{STORES[0][3]}</p><span id="pvs">{STORES[0][2]}</span></figcaption>
</figure>
<p class="note tnd-note">Proyectos de demostración de 404 Growth, no son tiendas de clientes.</p>
</div><script type="application/json" id="tnd-data">[{data}]</script></section>'''

# ---------- 4 · más canales de venta (A · mapa protagonista)
ROUTES = ['M256.7 203.3Q172.7 269.5 157.5 375.4', 'M256.7 203.3Q305.7 129.3 290.2 42.0', 'M256.7 203.3Q318.1 259.2 401.2 257.3', 'M256.7 203.3Q187.6 78.9 51.8 36.4', 'M256.7 203.3Q395.4 226.8 512.1 148.2', 'M256.7 203.3Q385.2 282.7 533.0 251.6']
ENDS = [(157.5, 375.4), (290.2, 42.0), (401.2, 257.3), (51.8, 36.4), (512.1, 148.2), (533.0, 251.6)]
LABELS = '<text x="168" y="380">Sevilla</text><text x="300" y="38">Bilbao</text><text x="401" y="281" text-anchor="middle">Valencia</text><text class="lx" x="62" y="32">A Coruña</text><text x="512" y="134" text-anchor="middle">Barcelona</text><text class="lx" x="533" y="275" text-anchor="middle">Palma</text>'
TICKETS = [('Barcelona', '00:32', 'Gafas de sol', '119 €', 't1'), ('Sevilla', '23:14', 'Abrigo de lana', '129 €', 't2'), ('Palma', '07:40', 'Jersey de punto', '69 €', 't3')]
tks = ''.join(f'<div class="tk {c} gm"><span class="tk-c">{city} · {h}</span><span class="tk-p"><span>{p}</span><span>{e.replace(" ", "&nbsp;")}</span></span></div>' for city, h, p, e, c in TICKETS)
ben = ''.join(f'<li class="rv" style="--d:{i * 60}ms"><b>{t}</b><span>{d}</span></li>' for i, (t, d) in enumerate(BENEFITS))
CANALES = f'''<section class="sec can" id="cambia"><div class="w can-g">
<header class="sh can-h rv">{chip('Lo que cambia')}<h2>Más canales de venta. <span class="lm">Sin abrir otro local.</span></h2><p>Esta noche, desde tu tienda a toda España.</p></header>
<div class="map rv" id="map">
<div class="map-in"><img src="/mapa-es.svg" alt="" width="616" height="474" loading="lazy">
<svg viewBox="0 0 616 474" role="img" aria-label="Pedidos de muestra desde tu tienda a seis ciudades de España">
<defs><linearGradient id="lnA" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#D4F27A" stop-opacity=".95"/><stop offset="1" stop-color="#D4F27A" stop-opacity=".35"/></linearGradient></defs>
<g class="rt" fill="none" stroke="url(#lnA)" stroke-linecap="round" stroke-dasharray="6 4">{''.join(f'<path d="{d}"/>' for d in ROUTES)}</g>
<g fill="#D4F27A">{''.join(f'<circle cx="{x}" cy="{y}" r="4.5"/>' for x, y in ENDS)}</g>
<g class="lb">{LABELS}</g>
<circle class="pu" cx="256.7" cy="203.3" r="8" fill="#D4F27A"/>
<circle cx="256.7" cy="203.3" r="8" fill="#D4F27A" stroke="#040806" stroke-width="3"/>
<text class="lt" x="240" y="197" text-anchor="end">Tu tienda</text>
</svg></div>
<div class="tks">{tks}</div>
</div>
<p class="note can-note">Ejemplo con pedidos de muestra.</p>
<ul class="ben">{ben}</ul>
</div></section>'''

# ---------- 5 · captación (A · pajarita)
def fs(i, n, lab, verb, desc):
    return f'<article class="fs f{i + 1}{" on" if i == 2 else ""} rv" style="--d:{i * 70}ms"><span class="fs-t"><span class="lab">{lab}</span><span class="num">{n}</span></span><span class="fs-b"><span class="vb">{verb}</span><span class="ds">{desc}</span></span></article>'
cap_m = lambda t: f'<div class="fc" aria-hidden="true">{t}{I_DOWN}</div>'
CAPTA = f'''<section class="sec cap" id="captacion"><div class="w">
<header class="sh row rv"><div>{chip('Captación')}<h2>Una tienda sin visitas es un <span class="lm">escaparate cerrado.</span></h2></div><p>Por eso no entregamos solo una web: con anuncios y email marketing llevamos a tus clientes del anuncio a la compra, y de la compra a la siguiente.</p></header>
<div class="bt">
<div class="brk" aria-hidden="true"><span class="b1"><em>Del anuncio a la compra</em></span><span class="b2"><em>Y de la compra a la siguiente</em></span></div>
<div class="bow">{cap_m('Del anuncio a la compra')}{fs(0, *FUNNEL[0])}{fs(1, *FUNNEL[1])}{fs(2, *FUNNEL[2])}{cap_m('Y de la compra a la siguiente')}{fs(3, *FUNNEL[3])}{fs(4, *FUNNEL[4])}</div>
</div>
</div></section>'''

# ---------- 6 · en cifras (B · bento con gráficos)
def src(t, href): return f'<a class="src" href="{href}" target="_blank" rel="noopener nofollow">{t}</a>'
bags = ''.join(f'<i class="{"bx" if k < 7 else "bo"}">{I_BAG}</i>' for k in range(10))
r24 = round(100 / 120.6 * 100, 1)  # 2024 = 2025 / 1,206 (CNMC)
CIFRAS = f'''<section class="sec cif" id="cifras"><div class="w">
<header class="sh row rv"><div>{chip('En cifras')}<h2>Las cifras <span class="lm">que importan.</span></h2></div><p>Lo que tarda tu tienda en abrir y lo que se mueve hoy en el comercio online en España.</p></header>
<div class="bento">
<article class="bb rv"><span class="kk">Nuestro plazo</span><span class="bb-n"><span class="big">15</span><span>días</span></span><p>Desde la llamada de arranque hasta que tu tienda abre online.</p>
<div class="tl2"><div class="ln" aria-hidden="true"><i class="a"></i><i class="b"></i><i class="c"></i></div><div class="lbs"><span><b>Día 0</b>Hablamos</span><span><b>Días 1–14</b>Montamos tu tienda</span><span><b>Día 15</b>Abres online</span></div></div></article>
<article class="bw gl rv" style="--d:80ms"><span class="num">114.800&nbsp;M€</span><span class="tx"><span>facturó el comercio electrónico en España en 2025.</span>{src('Fuente: CNMC, 2025', CNMC)}</span></article>
<article class="br2 gl rv" style="--d:140ms"><span class="tx"><span class="num">+20,6&nbsp;%</span><span class="tx2"><span>creció en un solo año, de 2024 a 2025.</span>{src('Fuente: CNMC, 2025', CNMC)}</span></span>
<span class="bars" role="img" aria-label="Facturación de 2025 frente a 2024: un 20,6 % más"><span><i style="height:{r24}%"></i><em>2024</em></span><span class="on"><i style="height:100%"></i><em>2025</em></span></span></article>
<article class="bg2 gl rv" style="--d:200ms"><span class="num">70&nbsp;%</span><span class="bags" role="img" aria-label="De cada 10 cestas, 7 se abandonan">{bags}</span><span class="tx2"><span>de las cestas online se abandonan antes de pagar. Por eso las recuperamos por email.</span>{src('Fuente: Baymard Institute', BAYMARD)}</span></article>
</div>
</div></section>'''

# ---------- 7 · qué incluye (B · precio fijo y desplegables)
def lst_check(items): return '<ul class="ck">' + ''.join(f'<li><i>{I_CHECK}</i><span>{t}</span></li>' for t in items) + '</ul>'
def lst_dash(items): return '<ul class="dl">' + ''.join(f'<li>{t}</li>' for t in items) + '</ul>'
def det(name, title, inner, open_=False, count=None):
    c = f'<span class="cnt">{count}</span>' if count else ''
    return f'<details name="{name}"{" open" if open_ else ""}><summary><span class="q">{title}</span>{c}<span class="pl" aria-hidden="true">{I_PLUS}</span></summary><div class="ans">{inner}</div></details>'
inc_acc = ''.join([
    det('inc', 'Incluido en tu tienda', lst_check(INC), True, 5),
    det('inc', 'Lo que aportas tú', lst_dash(APO), False, 4),
    det('inc', 'Costes externos posibles', lst_dash(COS), False, 5),
    det('inc', 'Todo queda a tu nombre', '<p>La tienda, el dominio y la cuenta de pagos son tuyos. Si un día dejamos de trabajar juntos, te lo quedas todo.</p>'),
    det('inc', 'La tienda la manejas tú', '<p>Subir productos, cambiar fotos o poner una oferta lo haces tú en minutos. Los cambios grandes, nosotros.</p>'),
])
INCLUYE = f'''<section class="sec inc" id="plan"><div class="w inc-g">
<header class="sh inc-h rv">{chip('Qué incluye')}<h2>Tu tienda online, <br class="d"><span class="lm">lista en 15 días.</span></h2></header>
<div class="price gx rv"><span class="kk">Tienda online · 15 días</span><h3>Precio cerrado, sin sorpresas.</h3><p>Depende de cuántos productos tienes, si se conecta tu TPV y si incluye anuncios y email marketing. Te lo damos en la llamada.</p>
<div class="btns col">{btn_lime('Reservar la llamada', book('plan'), 'plan', ' full')}{btn_gl(I_WA + 'Empezar por WhatsApp', WA, None, ' full wa-g')}</div></div>
<p class="disc">Abrir la tienda no garantiza ventas desde el primer día: dependen de tu producto, tus precios y la captación. Por eso medimos desde el primer pedido y ajustamos.</p>
<div class="acc inc-acc rv">{inc_acc}</div>
</div></section>'''
INCLUYE = INCLUYE.replace(f'class="b-gl full wa-g" href="{WA}"', f'class="b-gl full wa-g" {wa_attrs("plan")}')

# ---------- 8 · quién te atiende (B · tarjeta con su nombre detrás)
CHRIS = f'''<section class="sec chr" id="christian">
<div class="chr-bg" aria-hidden="true"><span class="d">CHRISTIAN</span><span class="m">CHRIS<br>TIAN</span></div>
<div class="w"><div class="chr-c gx rv">
<span class="av"><img src="/christian-hola.jpg" alt="Christian, fundador de 404 Growth" width="400" height="400" loading="lazy"><i></i></span>
<span class="kk"><span class="d">Quién te atiende · Christian, fundador de 404 Growth</span><span class="m">Quién te atiende</span></span>
<h2>Hablas conmigo, <br class="d"><span class="lm">no con un formulario.</span></h2>
<p>Soy Christian, fundador de 404 Growth. Mándame un WhatsApp con el nombre de tu tienda o tu Instagram y te digo, sin compromiso, cómo la pasaría a online y qué haría primero para que venda.</p>
<div class="btns">{btn_wa('Escribir a Christian', 'christian')}{btn_gl('Reservar una llamada de 30 min', book('christian'), 'christian')}</div>
<span class="micro">Te contesto yo, Christian. Sin compromiso.</span>
</div></div>
</section>'''

# ---------- 9 · preguntas (A · lista desplegable)
faq_acc = ''.join(det('faq', q, f'<p>{a}</p>', i == 0) for i, (q, a) in enumerate(FAQ))
FAQS = f'''<section class="sec faq" id="preguntas"><div class="w faq-g">
<header class="sh faq-h rv">{chip('Preguntas')}<h2>Lo que suelen <br class="d"><span class="lm">preguntarnos.</span></h2></header>
<div class="acc faq-acc rv">{faq_acc}</div>
<aside class="duda gx rv"><span class="av sm"><img src="/christian-hola.jpg" alt="" width="400" height="400" loading="lazy"><i></i></span><h3>¿No está tu duda?</h3><p>Pregúntamela por WhatsApp y te contesto yo.</p>{btn_wa('Escribir a Christian', 'preguntas', ' full')}</aside>
</div></section>'''

# ---------- 10 · cierre y pie (A · letras enormes y la marca al pie)
pills = ''.join(f'<a href="{h}">{t}<span aria-hidden="true">→</span></a>' for t, h in SECT)
guides = ''.join(f'<a href="{h}">{t}</a>' for t, h in GUIDES)
foot = ''.join(f'<a href="{h}">{t}</a>' for t, h in FOOT)
CIERRE = f'''<section class="sec cie" id="cierre"><div class="w">
<div class="sect"><span class="sect-t">Mira cómo sería en tu sector</span><div class="pills">{pills}</div><a class="all" href="/tienda-online"><span class="d">Todos los sectores</span><span class="m">Todos</span> →</a></div>
<div class="guides"><span>Por si quieres leer antes:</span>{guides}</div>
<div class="close rv"><h2>¿Abrimos <br class="m">tu tienda<br><span class="lm">a toda España?</span></h2>
<p>Escríbeme por WhatsApp con el nombre de tu tienda. Te digo cómo la pasaría a online y si tiene sentido en tu caso.</p>
<div class="btns">{btn_wa('Escríbeme por WhatsApp', 'cierre')}{btn_gl('Reserva una llamada de 30 min', book('cierre'), 'cierre')}</div>
<span class="micro">Te contesto yo, Christian.</span></div>
</div></section>
</main>
<footer class="ft"><div class="w">
<div class="ft-r1"><a class="nv-logo" href="/" aria-label="404 Growth, inicio">{MARK}<span>404 Growth</span></a><span class="ct">404 Growth · De tienda física a tienda online · Toda España · <a href="mailto:hola@404growth.com">hola@404growth.com</a> · <a href="tel:+34610594450">+34 610 594 450</a></span></div>
<div class="ft-r2"><nav class="fl" aria-label="Pie">{foot}</nav><span class="cp">© <span id="yr">2026</span> 404 Growth</span></div>
</div>
<svg class="wm" viewBox="0 0 1000 200" aria-hidden="true"><defs><linearGradient id="wmg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#D4F27A" stop-opacity=".5"/><stop offset=".7" stop-color="#D4F27A" stop-opacity=".07"/><stop offset="1" stop-color="#D4F27A" stop-opacity="0"/></linearGradient></defs><text x="0" y="178" textLength="1000" lengthAdjust="spacingAndGlyphs" font-size="232" font-weight="800" letter-spacing="-10" fill="url(#wmg)">404/GROWTH</text></svg>
</footer>
<a class="waf" {wa_attrs('flotante')} aria-label="Escríbeme por WhatsApp">{I_WA}<span>WhatsApp</span></a>
<div class="fade" aria-hidden="true"></div>'''

JS = (HERE / 'v67.js').read_text(encoding='utf-8')

html = (head + '<style>\n' + CSS + '\n/* cargador 404 (de la v64) */\n' + LOADER_CSS + '\n</style>\n</head>\n<body>\n'
        + "<script>document.documentElement.classList.add('js','l404')</script>\n" + loader + '\n'
        + NAV + '\n<main id="contenido">\n' + HERO + '\n' + COMO + '\n' + TIENDAS + '\n' + CANALES + '\n' + CAPTA + '\n' + CIFRAS + '\n' + INCLUYE + '\n' + CHRIS + '\n' + FAQS + '\n' + CIERRE + '\n'
        + '<script src="/lenis.min.js" defer></script>\n<script>\n' + JS + '\n</script>\n</body></html>\n')
html = html.replace('<main id="contenido">\n<main id="contenido">', '<main id="contenido">')
open(OUT, 'w', encoding='utf-8').write(html)
print('ok', OUT, len(html))
