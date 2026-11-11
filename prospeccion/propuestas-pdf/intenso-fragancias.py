# Propuesta de una carilla para Intenso Fragancias (11/11/2026)
# python3 build.py <carpeta de imágenes out/> <salida.html>
import base64, io, subprocess, sys, segno

SRC, OUT = sys.argv[1], sys.argv[2]
PRE = SRC + '/p-intenso-fragancias--b--'

REL = len(sys.argv) > 3 and sys.argv[3]   # carpeta relativa de las fotos (versión para el Mac)

def img(name, w, h):
    if REL:
        return REL + '/p-intenso-fragancias--b--' + name + '.jpg'

    # recorte centrado a w×h (px) y JPEG q82, en data URI
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', PRE + name + '.jpg', '-vf',
                          'scale=%d:%d:force_original_aspect_ratio=increase,crop=%d:%d' % (w, h, w, h),
                          '-q:v', '3', '-f', 'mjpeg', '-'], capture_output=True, check=True).stdout
    return 'data:image/jpeg;base64,' + base64.b64encode(raw).decode()

QR_URL = 'https://404growth.com/p/intenso-fragancias/'
buf = io.BytesIO()
segno.make(QR_URL, error='m').save(buf, kind='svg', scale=1, border=0, dark='#0B2B26', xmldecl=False, svgns=True, nl=False)
qr = buf.getvalue().decode()
qr = qr.replace('<svg ', '<svg class="qr" ', 1)

PHOTOS = ''.join('<img src="%s" alt="">' % img(n, 400, 304) for n in ['p1', 'p2', 'p3', 'p4', 'p5', 'p6'])

MARK = ('<svg viewBox="20 60 362 280" fill="none" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        '<g transform="skewX(-12) translate(52 0)" stroke-width="34" stroke="#D4F27A">'
        '<rect x="140" y="90" width="120" height="220" rx="60"/>'
        '<path d="M155.1 110.2 L40 240 L140 240"/><path d="M244.9 110.2 L360 240 L260 240"/></g></svg>')

BLOCKS = [
    ('Tienda Shopify con vuestra marca', [
        'Diseño y desarrollo con el <b>branding de Intenso</b>: logo, colores, letra y tono.',
        'Catálogo por familias con buscador y filtros, pensado para el móvil y en vuestro dominio.']),
    ('Los 150 productos, desde el primer día', [
        'Alta de los <b>150 productos</b>: nombre, descripción, precio, tamaños y stock.',
        '<b>Las fotos de los 150 las hacemos nosotros con IA</b> a partir de vuestros productos, con el mismo estilo.']),
    ('Pagos, envíos y la app de Shopify', [
        '<b>Pasarelas de pago</b> (tarjeta, Apple Pay, Google Pay y Bizum o PayPal si los queréis), envíos a toda España y recogida en tienda.',
        '<b>La app de Shopify en vuestro móvil</b>, totalmente sincronizada con vuestro sistema de envíos.']),
    ('Conexiones y sincronización interna', [
        'Stock, pedidos, clientes, correos y avisos <b>conectados entre sí</b>: lo vendido se descuenta solo y nada se pasa a mano.',
        'Instagram y Facebook Shopping, píxel de Meta y medición de ventas desde el primer pedido.']),
    ('Todas las políticas de la tienda', [
        'Aviso legal, privacidad, cookies, condiciones de venta, envíos, cambios y devoluciones, adaptadas a vuestra tienda y enlazadas en el pie y en el pago.']),
    ('Lista de espera de los agotados', [
        'Si un perfume se agota, el cliente deja <b>su correo o su teléfono</b> y le avisamos en cuanto vuelve. Y veis cuánta gente espera cada uno antes de reponer.']),
    ('Email marketing', [
        '<b>Bienvenida</b> para quien os deja su correo o su teléfono, y <b>recordatorio</b> para quien empieza la compra y no la termina.',
        '<b>Después de comprar:</b> gracias, seguimiento del envío, reseña y recompra. Lo construimos nosotros, con vuestra marca.']),
    ('12 meses de cambios incluidos', [
        'Durante 12 meses, <b>los cambios pequeños de la web los hacemos nosotros</b>: por ejemplo, 2–3 productos nuevos cada 2–3 semanas, <b>de 5 a 10 al mes</b>. Nos lo pedís por WhatsApp.']),
]

STD = [
    'Tienda abierta en <b>15 días</b> desde la llamada de arranque',
    'Llamada de arranque de 60 min para dejarlo todo definido',
    'Vuestro portal: el avance de la tienda, el contrato y las facturas',
    '9 guías paso a paso para usar Shopify y un chat para dudas',
    'Informe semanal por correo durante el lanzamiento',
    'Os enseñamos a gestionar pedidos y productos',
    'Todo a vuestro nombre: tienda, dominio y cuenta de pagos',
    'Habláis conmigo, Christian, no con un formulario',
]

CHECK = '<svg viewBox="0 0 12 12" aria-hidden="true"><path d="M2.5 6.3l2.3 2.3 4.7-5" fill="none" stroke="#2E7A64" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>'

blocks = ''.join(
    '<section class="b"><div class="n">%02d</div><div><h3>%s</h3><ul>%s</ul></div></section>'
    % (i + 1, t, ''.join('<li>%s</li>' % x for x in xs)) for i, (t, xs) in enumerate(BLOCKS))
std = ''.join('<li>%s<span>%s</span></li>' % (CHECK, x) for x in STD)

CSS = r'''
@page{size:A4;margin:0}
:root{--deep:#0B2B26;--lime:#D4F27A;--mint:#7FD3B6;--green:#2E7A64;--ink:#0F1E1A;--txt:#33433E;--mut:#66756F;--line:#DFE6E1;--soft:#F3F6F2;
--f:-apple-system,BlinkMacSystemFont,"SF Pro Text","SF Pro Display","Helvetica Neue",Helvetica,Arial,sans-serif}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:210mm;height:297mm;background:#fff}
body{font-family:var(--f);color:var(--txt);-webkit-print-color-adjust:exact;print-color-adjust:exact;font-size:7.6pt;line-height:1.36;-webkit-font-smoothing:antialiased}
b{font-weight:600;color:var(--ink)}
ul{list-style:none}
.pg{width:210mm;height:297mm;overflow:hidden;display:flex;flex-direction:column}
.hd{background:var(--deep);color:#EEF3EC;padding:8mm 12mm 0}
.top{display:flex;justify-content:space-between;align-items:center}
.brand{display:flex;align-items:center;gap:2mm;font-weight:700;font-size:10.5pt;letter-spacing:-.015em;color:#EEF3EC}
.brand svg{height:5.4mm;width:auto}
.date{font-size:7.4pt;color:rgba(238,243,236,.62);letter-spacing:.01em}
.chip{display:inline-block;margin-top:5.2mm;border:.25mm solid rgba(238,243,236,.28);border-radius:99px;padding:1mm 3mm;font-size:7.4pt;color:rgba(238,243,236,.88)}
h1{font-size:21pt;line-height:1.05;letter-spacing:-.028em;font-weight:700;margin-top:3.2mm;max-width:158mm;color:#fff}
h1 em{font-style:normal;color:var(--lime)}
.sub{margin-top:3mm;font-size:8.7pt;line-height:1.42;color:rgba(238,243,236,.8);max-width:180mm}
.ph{margin-top:1mm;display:grid;grid-template-columns:repeat(6,1fr);gap:1.8mm;transform:translateY(8mm);margin-bottom:0}
.ph img{width:100%;aspect-ratio:1.32/1;object-fit:cover;border-radius:1.8mm;display:block;border:.5mm solid #fff}
.cap{margin:10mm 12mm 0;display:flex;justify-content:space-between;font-size:6.9pt;color:var(--mut)}
.cap b{color:var(--green);font-weight:600}
.grid{margin:3.6mm 12mm 0;display:grid;grid-template-columns:1fr 1fr;column-gap:7mm;row-gap:2.8mm}
.b{display:grid;grid-template-columns:6.6mm 1fr;align-items:start;border-top:.25mm solid var(--line);padding-top:2.3mm}
.n{font-size:7.2pt;font-weight:700;color:var(--green);letter-spacing:.02em;padding-top:.5mm;font-variant-numeric:tabular-nums}
h3{font-size:9.1pt;line-height:1.2;letter-spacing:-.01em;color:var(--ink);font-weight:700;margin-bottom:.8mm}
.b li{position:relative;padding-left:2.9mm;margin-top:.55mm}
.b li:before{content:"";position:absolute;left:.2mm;top:1.45mm;width:1.15mm;height:1.15mm;border-radius:50%;background:var(--mint)}
.std{margin:3.6mm 12mm 0;background:var(--soft);border-radius:2.6mm;padding:3mm 4.4mm 3.2mm}
.std h4,.cost h4{font-size:7pt;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--green)}
.std ul{margin-top:2.1mm;display:grid;grid-template-columns:1fr 1fr;column-gap:6mm;row-gap:1.15mm}
.std li{display:flex;gap:1.6mm;align-items:flex-start}
.std li svg{width:2.9mm;height:2.9mm;flex:none;margin-top:.15mm}
.end{margin:3.6mm 12mm 0;display:grid;grid-template-columns:76mm 1fr;gap:5mm}
.price{background:var(--deep);color:#EEF3EC;border-radius:2.6mm;padding:3.4mm 4.4mm 3.6mm}
.price .k{font-size:7pt;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:rgba(238,243,236,.6)}
.price .v{font-size:25pt;font-weight:700;letter-spacing:-.035em;line-height:1;color:var(--lime);margin-top:1.4mm;font-variant-numeric:tabular-nums}
.price .iva{font-size:8.4pt;font-weight:600;color:#fff;margin-top:1mm}
.price p{text-wrap:pretty;font-size:7pt;line-height:1.4;color:rgba(238,243,236,.72);margin-top:1.6mm}
.price p b{color:#fff}
.cost{display:grid;grid-template-columns:1fr 1fr;column-gap:5mm;align-content:start;padding-top:.6mm}
.cost ul{margin-top:1.6mm}
.cost li{position:relative;padding-left:2.9mm;margin-top:.6mm}
.cost li:before{content:"";position:absolute;left:.2mm;top:1.45mm;width:1.15mm;height:1.15mm;border-radius:50%;background:#BAC7C0}
.cost .note{grid-column:1/-1;margin-top:2.4mm;font-size:6.9pt;color:var(--mut)}
.ft{margin:auto 12mm 8mm;padding-top:3mm;border-top:.25mm solid var(--line);display:flex;align-items:center;gap:4mm}
.qr{width:13mm;height:13mm;flex:none}
.ft .t{flex:1;font-size:7.3pt;line-height:1.45}
.ft .t b{font-size:8.2pt}
.ft .r{text-align:right;font-size:7.3pt;line-height:1.45;color:var(--txt)}
.ft .r b{font-size:8.2pt}
'''

HTML = '''<!doctype html><html lang="es"><head><meta charset="utf-8">
<title>Propuesta · Intenso Fragancias · 404 Growth</title><style>%s</style></head><body><div class="pg">
<header class="hd">
 <div class="top"><div class="brand">%s<span>404 Growth</span></div><div class="date">Propuesta · 11 de noviembre de 2026</div></div>
 <div class="chip">Para Intenso Fragancias · C/ Hoyo 11, Torremolinos (Málaga)</div>
 <h1>Vuestra tienda online, con los <em>150 productos</em> dentro desde el primer día.</h1>
 <p class="sub">En 15 días pasamos Intenso Fragancias de Torremolinos a toda España. Nos encargamos de todo, de la tienda al email marketing, y durante 12 meses seguimos haciendo los cambios pequeños.</p>
 <div class="ph">%s</div>
</header>
<div class="cap"><span><b>Fotos hechas con IA</b> a partir de vuestros productos · muestra de vuestra propuesta online</span></div>
<div class="grid">%s</div>
<div class="std"><h4>Y todo lo que ya incluye nuestra oferta</h4><ul>%s</ul></div>
<div class="end">
 <div class="price"><div class="k">Inversión</div><div class="v">1.740 €</div><div class="iva">IVA incluido · precio cerrado</div>
  <p>Con menos de 100 productos, la tienda es 1.440 €. Con vuestros 150, 1.740 €. <b>Los 12 meses de cambios van dentro.</b></p></div>
 <div class="cost">
  <div><h4>Aparte, a vuestro nombre</h4><ul><li>Envíos, según transportista</li><li>Anuncios, si hacéis campañas</li></ul></div>
  <div><h4>Lo que aportáis</h4><ul><li>Vuestros productos, precios y stock</li><li>Acceso a vuestro dominio y redes</li><li>Una persona que prepare los pedidos</li></ul></div>
  <div class="note">Os detallamos cualquier coste aparte antes de empezar.</div>
 </div>
</div>
<footer class="ft">%s
 <div class="t"><b>Mirad cómo quedaría vuestra tienda</b><br>404growth.com/p/intenso-fragancias</div>
 <div class="r"><b>Christian · fundador de 404 Growth</b><br>WhatsApp 610 594 450 · hola@404growth.com</div>
</footer>
</div></body></html>''' % (CSS, MARK, PHOTOS, blocks, std, qr)

open(OUT, 'w', encoding='utf-8').write(HTML)
print(OUT, len(HTML) // 1024, 'KB')
