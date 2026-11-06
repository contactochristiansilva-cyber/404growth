"""Portada v64 de 404growth.com: monta index.html a partir de la v61 (cabecera, cargador, mapa) y el diseño nuevo.
Uso: python3 tools/portada/v64/build.py tools/portada/v64/index-v61.html web117-404growth/index.html"""
import re, json, html, sys, os
D = os.path.dirname(os.path.abspath(__file__))
SRC = sys.argv[1]          # index.html v61
OUT = sys.argv[2]
h = open(SRC, encoding='utf8').read()
bi = h.find('<body')
head = h[:bi]
css = open(f'{D}/v64.css', encoding='utf8').read()

# reglas del mapa (.od) de la v61, sin la escena ni el bloque móvil general
old_css = re.search(r'<style[^>]*>([\s\S]*?)</style>', head).group(1)
rules, depth, cur = [], 0, ''
for ch in old_css:
    cur += ch
    if ch == '{': depth += 1
    elif ch == '}':
        depth -= 1
        if depth == 0: rules.append(cur); cur = ''
od_css = []
for r in rules:
    rs = r.strip()
    if rs.startswith('@media (max-width:760px)'): continue
    if re.search(r'\.od\b|\.od-|@keyframes odP', r) and '.scene' not in r.split('{')[0]:
        od_css.append(rs)
    elif '@media (max-width:860px)' in rs and '.od' in rs:
        od_css.append(re.sub(r'\.scene\{[^}]*\}', '', rs))
od_css = '\n'.join(od_css)
head = re.sub(r'<style[^>]*>[\s\S]*?</style>', lambda m: '<style>' + css + '\n/* mapa de España (v61) */\n' + od_css + '\n.od-wrap{margin-top:8px}\n</style>', head, count=1)

lo_end = h.find('<!-- /404 loader v3 -->') + len('<!-- /404 loader v3 -->')
loader = h[bi + len('<body>'):lo_end]

def bal_div(start):
    depth = 0
    for m in re.finditer(r'<(/?)div\b', h[start:]):
        depth += 1 if m.group(1) == '' else -1
        if depth == 0:
            return start + h[start:].find('>', m.end()) + 1
od_s = h.rfind('<div', 0, h.find('class="od"') + 5)
od = h[od_s:bal_div(od_s)]

footer = h[h.find('<footer'):h.find('</footer>') + 9]
waf = h[h.find('<a class="waf"'):h.find('</a>', h.find('<a class="waf"')) + 4]
WA_ICON = re.search(r'<svg[\s\S]*?</svg>', waf).group(0)
WA = 'https://wa.me/34610594450?text=Hola%20Christian%2C%20tengo%20una%20tienda%20f%C3%ADsica%20y%20quiero%20venderla%20online.%20Mi%20tienda%20es%3A%20'
ARR = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
def wa(txt, cls='btn lm', cta='wa'): return f'<a class="{cls}" href="{WA}" target="_blank" rel="noopener" data-cta="{cta}">{WA_ICON}{txt}</a>'
def bk(txt, camp, cls='btn gh'): return f'<a class="{cls}" href="/book?utm_source=web&amp;utm_medium=portada&amp;utm_campaign={camp}" data-cta="{camp}">{txt}{ARR}</a>'

# preguntas: las mismas del schema (FAQPage)
ld = json.loads(re.search(r'<script type="application/ld\+json">([\s\S]*?)</script>', h).group(1))
faq = next(g for g in ld['@graph'] if g.get('@type') == 'FAQPage')['mainEntity']
faq_html = ''.join(f'<details><summary>{html.escape(q["name"])}<i></i></summary><p>{html.escape(q["acceptedAnswer"]["text"])}</p></details>' for q in faq)

# tiendas de ejemplo de la landing VSL (proyectos conceptuales de 404 Growth)
DEMOS = [
 ('aurea', 'Áurea', 'Joyería', 'Joyería de oro de 18 k con grabado, caja de regalo y envío asegurado.'),
 ('pulso', 'Pulso', 'Sneakers', 'Tienda multimarca: lanzamientos, stock por talla y entrega en 24 h.'),
 ('solenne', 'Solenne', 'Moda mujer', 'Moda mediterránea premium: campaña editorial, tallas y «completa el look».'),
 ('nacar', 'Nácar', 'Cosmética', 'Skincare moderno: rutinas en packs, muestras de regalo y envío en 24 h.'),
 ('forma', 'Forma', 'Suplementos', 'Nutrición deportiva premium con suscripción y precios por toma.'),
]
FAN = [('-112%', '-17deg'), ('-58%', '-8deg'), ('0%', '0deg'), ('58%', '8deg'), ('112%', '17deg')]
fan = ''.join(
    f'<a class="fc c{i+1}" href="/demo-{k}" style="--x:{x};--r:{r};--i:{abs(i-2)}" aria-label="Tienda de ejemplo {n}, {s}">'
    f'<img src="/demos/cards/{k}.webp" alt="" width="760" height="1040"{"" if i == 2 else " loading=lazy"} decoding="async"><b>{n}</b></a>'
    for i, ((k, n, s, d), (x, r)) in enumerate(zip(DEMOS, FAN)))
order = [2, 0, 1, 3, 4]
tk = ''.join(
    f'<a class="tc" href="/demo-{DEMOS[j][0]}"><img src="/demos/cards/{DEMOS[j][0]}.webp" alt="Tienda de ejemplo {DEMOS[j][1]}" width="760" height="1040" loading="lazy" decoding="async">'
    f'<div class="in"><span class="sc">{DEMOS[j][2]}</span><h3>{DEMOS[j][1]}</h3><p>{DEMOS[j][3]}</p><div class="go">Ver la tienda →</div></div></a>'
    for j in order)
MINI = [('solenne', '-60%', '-10deg', 1), ('aurea', '0%', '0deg', 0), ('pulso', '60%', '10deg', 1)]
mini = ''.join(f'<a class="fc" href="/demo-{k}" style="--x:{x};--r:{r};--i:{i}" tabindex="-1" aria-hidden="true"><img src="/demos/cards/{k}.webp" alt="" width="760" height="1040" loading="lazy" decoding="async"></a>' for k, x, r, i in MINI)

SECT = [('moda', 'abrigo-beige', 'Moda'), ('joyeria', 'joya-cuello', 'Joyería'), ('deportes', 'dep-zapatillas', 'Deporte'),
        ('decoracion-y-hogar', 'deco-jarron', 'Decoración'), ('pasteleria', 'obr-vitrina', 'Obradores'), ('regalos-y-artesania', 'opt-sol', 'Regalos')]
sx = ''.join(f'<a href="/tienda-online/{s}"><img src="/home--a--{im}.jpg" alt="Tienda online de {n.lower()}" width="980" height="1225" loading="lazy" decoding="async"><span>{n}<em>→</em></span></a>' for s, im, n in SECT)

body = f'''<a class="skip" href="#contenido">Saltar al contenido</a>
<header class="nv"><div class="nv-in"><a class="nv-logo" href="/" aria-label="404 Growth, inicio"><span class="w404">404/GROWTH<sup>®</sup></span></a>
<nav class="nv-lk" aria-label="Secciones"><a href="#como">Cómo funciona</a><a href="#tiendas">Tiendas</a><a href="#plan">Qué incluye</a><a href="#preguntas">Preguntas</a><a href="/guia">Guías</a></nav>
{bk('Reservar llamada', 'cabecera')}{wa('Escríbeme', 'btn lm', 'wa-cabecera')}</div></header>
<main id="contenido">
<section class="hero">
 <div class="wrap"><p class="lbl"><i></i>De tienda física a tienda online · toda España</p>
 <h1><span class="l1">Tu tienda.</span> <span class="l2 gr">Abierta 24 horas.</span></h1></div>
 <div class="fan pre" id="fan">{fan}</div>
 <div class="wrap hero-b">
  <p class="sub">Convertimos tu tienda física en una tienda online que vende en toda España, también de noche y en festivos. <b>Lista en 15 días</b>, sin abrir otro local.</p>
  <div class="btns">{wa('Escríbeme por WhatsApp', 'btn lm', 'portada-wa')}{bk('Reserva una llamada de 30 min', 'portada')}</div>
  <p class="note"><img src="/christian-hola.jpg" alt="" width="30" height="30">Te contesto yo, Christian. Sin compromiso.</p>
  <div class="tools"><span>Shopify</span><span>Bizum</span><span>Apple Pay</span><span>Instagram Shopping</span><span>Anuncios en Meta</span><span>Email marketing</span></div>
  <p class="ex">Arriba, tiendas de ejemplo diseñadas por 404 Growth.</p>
 </div>
</section>

<section class="sec" id="como"><div class="wrap">
 <div class="sh c"><p class="eb">Cómo funciona</p><h2>Tres pasos. <span class="gr">Quince días.</span></h2><p>De tu mostrador a toda España, sin que tengas que saber de tecnología.</p></div>
 <ol class="st3">
  <li class="s s1"><div class="vis"><div class="bub">Hola Christian, tengo una tienda física y quiero venderla online. Mi tienda es: …<small>Tu primer mensaje, ya escrito</small></div></div><span class="d">Día 0</span><h3>Hablamos</h3><p>Me escribes por WhatsApp o reservas una llamada. En la llamada de arranque (una hora) hacemos juntos lo más técnico, como los accesos.</p></li>
  <li class="s s2"><div class="vis"><div class="chips"><span>Tu marca</span><span>Fichas de producto</span><span>Bizum y Apple Pay</span><span>Envíos</span><span>Stock</span><span>Pruebas de compra</span></div></div><span class="d">Días 1–14</span><h3>Montamos tu tienda</h3><p>Nos pasas fotos, precios y productos por WhatsApp. Nosotros diseñamos la tienda con tu marca y dejamos pagos y envíos listos.</p></li>
  <li class="s s3"><div class="vis"><div class="open"><span class="st"><i></i>Tienda abierta</span><small>Instagram Shopping · ventas medidas</small></div></div><span class="d">Día 15</span><h3>Abres online</h3><p>Tu tienda abierta y midiendo ventas. Después, anuncios en Meta y email marketing para traer compradores.</p></li>
 </ol>
</div></section>

<section class="sec" style="padding-top:0"><div class="wrap"><div class="me">
 <img src="/christian-hola.jpg" alt="Christian Silva, fundador de 404 Growth" width="400" height="400" loading="lazy">
 <div><p class="eb">Quién te atiende</p><h2 style="margin-top:10px">Hablas conmigo, no con un formulario.</h2>
 <p>Soy Christian, fundador de 404 Growth. Mándame un WhatsApp con el nombre de tu tienda o tu Instagram y te digo, sin compromiso, cómo la pasaría a online y qué haría primero para que venda.</p>
 <div class="btns">{wa('Escribir a Christian', 'btn lm', 'quien')}</div></div>
</div></div></section>

<section class="sec" id="tiendas" style="padding-top:0"><div class="wrap">
 <div class="sh"><p class="eb">Tiendas de ejemplo</p><h2>Así puede verse la tuya.</h2><p>Tiendas de demostración que hemos diseñado en 404 Growth. Ábrelas y pruébalas: fichas, tallas, cesta y pago.</p></div>
 <div class="tk">{tk}</div>
 <p class="tk-n">Proyectos de demostración de 404 Growth, no son tiendas de clientes.</p>
</div></section>

<section class="sec" id="cambia" style="padding-top:0"><div class="wrap">
 <div class="sh"><p class="eb">Lo que cambia</p><h2>Más canales de venta. Sin abrir otro local.</h2></div>
 <div class="od-wrap">{od}</div>
 <div class="ben">
  <div class="bc"><b><em>24/7</em></b><p>Pueden comprarte fuera de horario, en festivos y en vacaciones.</p></div>
  <div class="bc"><b>Toda España</b><p>Vendes fuera de tu zona, no solo a quien pasa por la puerta.</p></div>
  <div class="bc"><b>Menos mensajes</b><p>Precio, talla y pago en la ficha: menos ventas a golpe de DM.</p></div>
  <div class="bc"><b>Recogida en tienda</b><p>Compran online y recogen en tu tienda: más visitas al mostrador.</p></div>
  <div class="bc"><b>Datos</b><p>Ves qué vende, a quién y desde dónde, sin suposiciones.</p></div>
  <div class="bc"><b>Recompra</b><p>«Completa el look», productos relacionados y novedades para quien ya te compró.</p></div>
 </div>
</div></section>

<section class="sec" id="captacion" style="padding-top:0"><div class="wrap">
 <div class="sh"><p class="eb">Captación</p><h2>Una tienda sin visitas es un escaparate cerrado.</h2><p>Por eso no entregamos solo una web: con anuncios y email marketing llevamos a tus clientes del anuncio a la compra, y de la compra a la siguiente.</p></div>
 <ol class="cap">
  <li class="cp"><span class="n">1</span><small>Anuncios en Meta</small><h3>Te descubren</h3><p>Tus productos delante de quien aún no te conoce, en toda España.</p></li>
  <li class="cp"><span class="n">2</span><small>Retargeting</small><h3>Te consideran</h3><p>Volvemos a mostrar tus productos a quien ya visitó la tienda.</p></li>
  <li class="cp"><span class="n">3</span><small>Tienda</small><h3>Te compran</h3><p>Talla, stock y pago en tres pasos. Sin escribir a nadie.</p></li>
  <li class="cp"><span class="n">4</span><small>Email de cesta</small><h3>Vuelven</h3><p>Cada cesta abandonada recibe un recordatorio para terminar la compra.</p></li>
  <li class="cp"><span class="n">5</span><small>Email marketing</small><h3>Repiten</h3><p>Novedades y «vuelve a estar disponible» para quien ya te compró.</p></li>
 </ol>
</div></section>

<section class="sec lt" id="cifras"><div class="wrap">
 <div class="sh"><p class="eb">En cifras</p><h2>Las cifras que importan.</h2><p>Lo que tarda tu tienda en abrir y lo que se mueve hoy en el comercio online en España.</p></div>
 <div class="kp">
  <div class="k big"><b>15 días</b><p>Desde la llamada de arranque hasta que tu tienda abre online.</p><small>Nuestro plazo</small></div>
  <div class="k wide"><b>114.800&nbsp;M€</b><p>facturó el comercio electrónico en España en 2025.</p><small>Fuente: <a href="https://www.ondavasca.com/el-comercio-electronico-factura-114-800-millones-en-2025/" target="_blank" rel="noopener">CNMC, 2025</a></small></div>
  <div class="k"><b>+20,6&nbsp;%</b><p>creció en un solo año, de 2024 a 2025.</p><small>Fuente: <a href="https://www.ondavasca.com/el-comercio-electronico-factura-114-800-millones-en-2025/" target="_blank" rel="noopener">CNMC, 2025</a></small></div>
  <div class="k"><b>70&nbsp;%</b><p>de las cestas online se abandonan antes de pagar. Por eso las recuperamos por email.</p><small>Fuente: <a href="https://baymard.com/lists/cart-abandonment-rate" target="_blank" rel="noopener">Baymard Institute</a></small></div>
 </div>
</div></section>

<section class="sec" id="plan"><div class="wrap">
 <div class="sh"><p class="eb">Qué incluye</p><h2>Tu tienda online, <span class="gr">lista en 15 días.</span></h2></div>
 <div class="pl">
  <div class="pk"><span class="lbl"><i></i>Tienda online · 15 días</span><h3>Todo listo para vender.</h3>
   <ul class="ck"><li>Diseño y desarrollo de la tienda con tu marca</li><li>Fichas de producto, catálogo y pago</li><li>Pagos, envíos y recogida en tienda configurados</li><li>Instagram Shopping y medición de ventas</li><li>Te enseñamos a gestionar pedidos y productos</li></ul>
   <div class="pr"><b>Precio cerrado, sin sorpresas.</b><span>Depende de cuántos productos tienes, si se conecta tu TPV y si incluye anuncios y email marketing. Te lo damos en la llamada.</span></div>
   <div class="btns">{wa('Empezar por WhatsApp', 'btn lm', 'plan-wa')}{bk('Reservar la llamada', 'plan')}</div>
  </div>
  <div class="ps">
   <details class="pc"><summary><h3>Lo que aportas tú</h3><i></i></summary><ul class="dl"><li>Tus productos, precios y stock</li><li>Las fotos que ya tienes (si faltan, lo vemos contigo)</li><li>Acceso a tu dominio y redes, si ya los tienes</li><li>Una persona que prepare los pedidos</li></ul></details>
   <details class="pc"><summary><h3>Costes externos posibles</h3><i></i></summary><ul class="dl"><li>Dominio, si aún no tienes</li><li>Cuota de Shopify</li><li>Comisión de la pasarela de pago por venta</li><li>Envíos, según transportista</li><li>Presupuesto de anuncios, si haces campañas</li></ul></details>
  </div>
 </div>
 <div class="tw"><div><b>Todo queda a tu nombre</b>La tienda, el dominio y la cuenta de pagos son tuyos. Si un día dejamos de trabajar juntos, te lo quedas todo.</div><div><b>La tienda la manejas tú</b>Subir productos, cambiar fotos o poner una oferta lo haces tú en minutos. Los cambios grandes, nosotros.</div></div>
 <p class="disc">Abrir la tienda no garantiza ventas desde el primer día: dependen de tu producto, tus precios y la captación. Por eso medimos desde el primer pedido y ajustamos.</p>
</div></section>

<section class="sec" style="padding-top:0"><div class="wrap">
 <div class="sx-h"><h3>Mira cómo sería en tu sector</h3><a href="/tienda-online">Todos los sectores →</a></div>
 <div class="sx">{sx}</div>
</div></section>

<section class="sec" id="preguntas" style="padding-top:0"><div class="wrap"><div class="fq">
 <div class="fq-l"><p class="eb">Preguntas</p><h2>Lo que suelen preguntarnos.</h2>
  <div class="fq-c"><div class="who"><img src="/christian-hola.jpg" alt="" width="52" height="52" loading="lazy"><b>¿No está tu duda?</b></div><p>Pregúntamela por WhatsApp y te contesto yo.</p>{wa('Preguntar por WhatsApp', 'btn dk', 'preguntas')}</div></div>
 <div><div class="qs">{faq_html}</div>
 <nav class="seo-lk" aria-label="Guías para crear tu tienda online"><b>Por si quieres leer antes:</b><a href="/diseno-tienda-online">Diseño de tienda online</a><a href="/crear-tienda-online">Cómo crear una tienda online</a><a href="/guia/cuanto-cuesta-una-tienda-online">Cuánto cuesta hacer una tienda online</a><a href="/guia/pasar-tienda-fisica-a-online">Pasar tu tienda física a online</a><a href="/tienda-online">Tienda online por sector</a><a href="/guia/shopify-vs-woocommerce">Shopify o WooCommerce</a></nav></div>
</div></div></section>

<section class="sec" id="contacto" style="padding-top:0"><div class="wrap"><div class="end">
 <h2>¿Abrimos tu tienda<br><span class="gr">a toda España?</span></h2>
 <p>Escríbeme por WhatsApp con el nombre de tu tienda. Te digo cómo la pasaría a online y si tiene sentido en tu caso.</p>
 <div class="btns">{wa('Escríbeme por WhatsApp', 'btn lm', 'cierre-wa')}{bk('Reserva una llamada de 30 min', 'cierre')}</div>
 <p class="note"><img src="/christian-hola.jpg" alt="" width="30" height="30" loading="lazy">Te contesto yo, Christian.</p>
 <div class="fan mini">{mini}</div>
</div></div></section>
</main>
{footer}
{waf}
<script>try{{document.getElementById("yr").textContent=new Date().getFullYear()}}catch(e){{}}if(innerWidth>860)document.querySelectorAll("details.pc").forEach(function(d){{d.open=true}})</script>
<script>/*od61*/(function(){{var o=document.querySelector('.od');if(!o)return;if(!('IntersectionObserver' in window)||matchMedia('(prefers-reduced-motion: reduce)').matches){{o.classList.add('in');return}}new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting)o.classList.add('in','vis');else o.classList.remove('vis')}})}},{{threshold:.3}}).observe(o)}})()</script>
<script>/*v64 abanico: se abre cuando termina el cargador*/(function(){{var f=document.getElementById('fan');if(!f)return;var H=document.documentElement,done=0;function go(){{if(done)return;done=1;requestAnimationFrame(function(){{f.classList.remove('pre')}})}}
if(matchMedia('(prefers-reduced-motion: reduce)').matches){{go();return}}
if(H.classList.contains('l404')&&'MutationObserver' in window){{var mo=new MutationObserver(function(){{if(!H.classList.contains('l404')){{mo.disconnect();go()}}}});mo.observe(H,{{attributes:true,attributeFilter:['class']}});setTimeout(go,4000)}}else setTimeout(go,150)}})()</script>
<script>/*v64: el WhatsApp flotante se esconde mientras se ven los botones de la portada*/(function(){{var w=document.querySelector('.waf'),t=document.querySelector('.hero-b .btns');if(!w||!t||!('IntersectionObserver' in window))return;new IntersectionObserver(function(e){{w.classList.toggle('off',e[0].isIntersecting)}}).observe(t)}})()</script>
</body></html>
'''
# el cargador va primero, como en la v61
out = head + '<body>' + loader + '\n' + body
open(OUT, 'w', encoding='utf8').write(out)
print('ok', len(out), 'bytes; od css', len(od_css))
