# Versión «para cerrar en la llamada» de la propuesta de Carmen Valencia: la oferta arriba, sin precios.
import re, sys, urllib.parse
src, dst = sys.argv[1], sys.argv[2]
t = open(src, encoding='utf-8').read()
WA = 'https://wa.me/34610594450?text=' + urllib.parse.quote('Hola Christian, queremos empezar con la tienda online de Carmen Valencia.')
ck = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.2 4.2L19 7"/></svg>'
def li(x): return f'<li>{ck}<span>{x}</span></li>'
OFFER = f'''<section class="sec" id="propuesta"><div class="wrap">
<div class="chap"><span class="num">✦</span><span class="lb">Lo que os proponemos</span></div>
<div class="head"><h2>Vuestra tienda online, abierta en 15 días.<br><span class="t">Y clientas nuevas desde el primer mes.</span></h2>
<p>Nosotros lo hacemos todo: la tienda, las fotos, el catálogo y los anuncios. Vosotras seguís en San Agustín como siempre.</p></div>
<div class="of3">
<div class="ofc"><small>01</small><h3>La tienda online de Carmen Valencia</h3><p>Como la que veis abajo, con vuestra marca y vuestras prendas.</p><ul>
{li('Diseño propio con vuestro logo y vuestros colores')}{li('Fotos de producto nuevas para cada prenda, como las de esta propuesta')}{li('Fichas con tallas, guía de tallas y «shop the look»')}{li('Pago con tarjeta, Bizum y Apple Pay')}{li('Envíos a toda España y recogida en San Agustín 15')}{li('Vuestro dominio, carmenvalencia.es')}</ul></div>
<div class="ofc"><small>02</small><h3>Clientas nuevas con anuncios</h3><p>Para que la tienda venda desde el primer día, no solo que exista.</p><ul>
{li('Campañas en Instagram y Facebook para León y para toda España')}{li('Los anuncios los preparamos nosotros, con vuestras prendas')}{li('Abrigos y peletería, temporada de invitada, Navidad y rebajas')}{li('Vuestras seguidoras y vuestras clientas de Google, a la tienda')}{li('Cada semana, lo que se ha vendido y lo que ha costado')}</ul></div>
<div class="ofc"><small>03</small><h3>Os acompañamos siempre</h3><p>Sin que tengáis que aprender nada técnico.</p><ul>
{li('Subimos nosotros el catálogo y las novedades de cada temporada')}{li('Stock unificado con la tienda física')}{li('Os enseñamos a preparar un pedido en 10 minutos')}{li('Soporte directo por WhatsApp con Christian')}{li('La tienda es vuestra: dominio, clientas y datos')}</ul></div>
</div>
<div class="of15"><div><b>Hoy</b><span>Decimos que sí</span></div><div><b>Día 0</b><span>Llamada de arranque</span></div><div><b>Días 3–10</b><span>Diseño, fotos y catálogo</span></div><div><b>Días 8–14</b><span>Pagos, envíos y prueba</span></div><div><b>Día 15</b><span>Tienda abierta y primeros anuncios</span></div></div>
<div class="ofn"><div><h4>Lo único que necesitamos de vosotras</h4><p>Una llamada de una hora para arrancar, la lista de prendas y tallas, y vuestro visto bueno a las fotos.</p></div>
<a class="cta" href="{WA}" target="_blank" rel="noopener">Empezamos<span>→</span></a></div>
</div></section>'''
CSS = '''<style id="cv-offer">
#propuesta .head h2 .t{color:var(--t,#9C7B3C)}
.of3{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:34px}
.ofc{background:#fff;border:1px solid rgba(0,0,0,.08);border-radius:22px;padding:26px 24px;box-shadow:0 20px 40px -32px rgba(0,0,0,.35)}
.ofc small{font-size:12px;letter-spacing:.14em;color:var(--t,#9C7B3C);font-weight:600}
.ofc h3{font-size:21px;line-height:1.2;letter-spacing:-.02em;margin:10px 0 6px}
.ofc p{font-size:14.5px;color:rgba(0,0,0,.6);margin:0 0 14px}
.ofc ul{list-style:none;padding:0;margin:0;display:grid;gap:10px}
.ofc li{display:flex;gap:10px;font-size:14.5px;line-height:1.4}
.ofc li svg{width:18px;height:18px;flex:none;color:var(--t,#9C7B3C);margin-top:1px}
.of15{display:grid;grid-template-columns:repeat(5,1fr);gap:0;margin-top:26px;border:1px solid rgba(0,0,0,.08);border-radius:18px;overflow:hidden;background:#fff}
.of15 div{padding:16px 16px;border-left:1px solid rgba(0,0,0,.07)}.of15 div:first-child{border-left:0;background:var(--t,#9C7B3C);color:#fff}
.of15 b{display:block;font-size:13px;letter-spacing:.04em}.of15 span{display:block;font-size:14px;margin-top:4px;opacity:.85}
.ofn{display:flex;align-items:center;justify-content:space-between;gap:24px;margin-top:26px;padding:24px 26px;border-radius:22px;background:#111;color:#fff}
.ofn h4{margin:0 0 6px;font-size:18px}.ofn p{margin:0;font-size:14.5px;opacity:.75;max-width:560px}
.ofn .cta{flex:none}
@media (max-width:860px){.of3{grid-template-columns:1fr}.of15{grid-template-columns:1fr 1fr}.of15 div{border-left:0;border-top:1px solid rgba(0,0,0,.07)}.of15 div:first-child{grid-column:1/-1;border-top:0}.ofn{flex-direction:column;align-items:flex-start}}
</style>'''
# 1 · la oferta, justo después del primer pantallazo
i = t.index('<section class="sec shopsec" id="tienda">')
t = t[:i] + OFFER + t[i:]
t = t.replace('</head>', CSS + '</head>', 1)
# 2 · menú: «Propuesta» primero
t = re.sub(r'(<a[^>]*href="#tienda"[^>]*>)', r'<a href="#propuesta">Propuesta</a>\1', t, count=1)
# 3 · los botones de reservar llamada pasan a «Empezamos» (estamos ya en la llamada)
t = re.sub(r'<a class="cta ghost" href="https://404growth\.com/book[^"]*"[^>]*>Reservar videollamada</a>', f'<a class="cta ghost" href="#propuesta">Ver lo que incluye</a>', t)
t = re.sub(r'href="https://404growth\.com/book\?[^"]*"', f'href="{WA}"', t)
t = t.replace('Reservar 30 min', 'Empezamos').replace('Reservar videollamada', 'Empezamos')
t = re.sub(r'(<section class="close"[^>]*>.*?<h2>).*?(</h2>)', r'\1¿Abrimos Carmen Valencia<br><span class="t">a toda España?</span>\2', t, count=1, flags=re.S)
t = t.replace('Os enseño esta tienda en 30 minutos, con vuestro catálogo y en directo.', 'Si os encaja, hoy lo dejamos cerrado y en 15 días vuestra tienda está abierta.')
t = t.replace('Escribidme por WhatsApp', 'Empezamos')
open(dst, 'w', encoding='utf-8').write(t)
print('ok', len(t), 'book left:', t.count('404growth.com/book'), 'precio€:', len(re.findall(r'\d+\s?€', t)))
