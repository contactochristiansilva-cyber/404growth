"""Lote 33 · la propuesta v33 de la semana pasada (lote 32, prospeccion/lote31/tools/gen.py) con la tienda nueva del lote 33 dentro.
uso: python3 gen33v.py <slug> [...]   → reescribe out/p-<slug>.html (la tienda p-<slug>--tienda.html la hace gen33.py)
La página, sus estilos (V32, V33, plantilla del lote 30) y sus secciones son las de gen.py; solo cambia lo de dentro de los marcos:
en vez de la maqueta de la tienda, la tienda de verdad en un iframe (portátil y móvil del inicio con ?tour=1, la tienda entera con ?embed=1
y la ficha con ?embed=1&at=destacado)."""
import html, json, os, re, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, '..', 'lote31', 'tools'))
import gen as G  # noqa: E402
sys.path.insert(0, D)
import gen33 as N33  # noqa: E402

E = html.escape
IDS = ['h', 'b', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'l1', 'l2']

# textos por nicho para la propuesta (moda y joya, los de la semana pasada; el resto, nuevos)
NV = {k: dict(G.NICHE[k]) for k in ('moda', 'joya')}
_base = dict(NV['moda'])
NV['cosmetica'] = dict(_base, shop_of='perfumería', item_pl='productos', item_art='el producto',
                       tienda_p='Diseñada a partir de las mejores perfumerías online: fotos que dan ganas, formato y precio en la ficha, muestras de regalo, pago en un toque y vuestro consejo siempre a mano.',
                       complete='Completa tu rutina', ad3_btn='Ver la rutina', pdp_h3='Cada producto,<br>listo para comprar.',
                       pdp_points=[('Fotos que venden', 'Cada frasco y cada textura, como en la tienda.'), ('Formato y precio', 'Sin preguntar por DM.'),
                                   ('Completa tu rutina', 'Más productos por pedido, más ticket medio.'), ('Asesoramiento', 'La duda se resuelve por WhatsApp sin salir de la ficha.')],
                       flow_new=[('Ve el producto', 'Instagram o anuncio'), ('Elige formato', 'En la ficha'), ('Paga', 'Tarjeta, Bizum, Apple Pay')])
NV['sneakers'] = dict(_base, shop_of='tienda de sneakers', item_pl='pares', item_art='el par',
                      tienda_p='Diseñada a partir de las mejores tiendas de sneakers: drops a la vista, talla en la ficha, cambio fácil, pago en un toque y vuestro estilo de siempre.',
                      complete='Completa el outfit', ad3_btn='Ver el drop', pdp_h3='Cada par,<br>listo para comprar.',
                      pdp_points=[('Fotos de cada par', 'Por delante, de lado y puestas.'), ('Talla en la ficha', 'Menos dudas, menos cambios.'),
                                  ('Completa el outfit', 'Más artículos por pedido.'), ('WhatsApp directo', 'La duda de talla, sin salir de la ficha.')],
                      flow_new=[('Ve el drop', 'Instagram o anuncio'), ('Elige su talla', 'En la ficha'), ('Paga', 'Tarjeta, Bizum, Apple Pay')])
NV['calzado'] = dict(NV['sneakers'], shop_of='zapatería',
                     tienda_p='Diseñada a partir de las mejores zapaterías online: cada par con sus fotos, talla en la ficha, cambio fácil, pago en un toque y la confianza de vuestra tienda de siempre.',
                     complete='Completa el look', ad3_btn='Ver novedades',
                     flow_new=[('Ve el par', 'Instagram o anuncio'), ('Elige su talla', 'En la ficha'), ('Paga', 'Tarjeta, Bizum, Apple Pay')])
NV['optica'] = dict(_base, shop_of='óptica', item_pl='monturas', item_art='la montura',
                    tienda_p='Diseñada a partir de las mejores ópticas online: cada montura con sus fotos, gafas de sol a un clic, revisión reservada en un minuto y pago en un toque.',
                    complete='Gafas de sol a juego', ad3_btn='Ver monturas', pdp_h3='Cada montura,<br>lista para comprar.',
                    pdp_points=[('Fotos de cada montura', 'De frente, de lado y puestas.'), ('Graduada o de sol', 'Se elige en la ficha.'),
                                ('Reserva de revisión', 'Día y hora sin llamar.'), ('Ajuste en tienda', 'Compra online, ajuste gratis en la óptica.')],
                    flow_new=[('Ve la montura', 'Instagram o Google'), ('Compra o reserva cita', 'En la ficha'), ('Paga', 'Tarjeta, Bizum, Apple Pay')])
for k, v in N33.FLOW_TODAY.items():
    NV[k]['flow_today'] = v
G.NICHE.update(NV)

# los marcos de la página con la tienda nueva dentro
FRAME_CSS = ('<style id="v33i">.scaler>iframe{position:absolute;left:0;top:0;width:1280px;border:0;display:block;transform-origin:0 0;background:#fff}'
             '.ph .pin{position:relative}.ph .pin iframe{width:375px;height:860px;border:0;display:block;background:#fff}'
             '.shopsec .bw .scaler{min-height:300px}</style>')
FRAME_JS = ("<script>(function(){var F=[].slice.call(document.querySelectorAll('iframe[data-src]'));"
            "function L(f){if(!f.src)f.src=f.dataset.src}"
            "if('IntersectionObserver' in window){var io=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting)L(x.target);"
            "try{x.target.contentWindow&&x.target.contentWindow.postMessage({t404:x.isIntersecting},'*')}catch(e){}})},{rootMargin:'900px 0px'});F.forEach(function(f){io.observe(f)})}else F.forEach(L);"
            "addEventListener('message',function(m){var d=m.data;if(!d||!d.h404)return;F.forEach(function(f){if(f.contentWindow===m.source&&f.dataset.full){f.style.height=d.h404+'px';if(window.fit)fit()}})});"
            "})();</script>")


def frame(c, q, h=768, full=False):
    return (f'<iframe data-src="/p-{c["slug"]}--tienda?{q}" title="Tienda de {E(c["name"])}" tabindex="-1" style="height:{h}px"'
            + (' data-full="1"' if full else '') + '></iframe>')


def shop_home(c, full=True, tour=False):
    return frame(c, 'tour=1') if tour else frame(c, 'embed=1', 5200, full=True)


def shop_home_m(c, tour=False):
    return frame(c, 'tour=1' if tour else 'embed=1', 860)


def shop_pdp(c):
    return frame(c, 'embed=1&at=destacado', 780)


def shop_pdp_m(c):
    return frame(c, 'embed=1&at=destacado', 860)


G.shop_home, G.shop_home_m, G.shop_pdp, G.shop_pdp_m = shop_home, shop_home_m, shop_pdp, shop_pdp_m


def ads(c):
    """los seis anuncios de la semana pasada, con las fotos que tiene ahora cada tienda"""
    N = G.NICHE[c['niche']]; A = c['ads']; ad, bi = G.ad, G.bi
    g = ad(c, f'<div class="ab" {bi("p1", "center 30%")}></div><div class="ao bl"><small>{E(A["a1s"])}</small><h6 style="font-size:26px">{A["a1"]}</h6><span class="pill">Comprar</span></div>',
           'Comprar ahora', '<b>Producto estrella</b> · retargeting a quien vio el post', 1)
    g += ad(c, f'<div class="ab" {bi("l1", "center 30%")}></div><div class="ao tp"><h6>De {E(c["city_short"])}<br>a toda España.</h6></div>',
            'Comprar ahora', f'<b>Envío</b> · captación fuera de {E(c["city_short"])}', 2)
    g += ad(c, f'<div class="ab cr"><div class="col"><i data-i="p2"></i><b>+</b><i data-i="p3"></i><b>+</b><i data-i="p4"></i></div><h6 class="dk">{A["a3"]}</h6></div>',
            N['ad3_btn'], f'<b>{E(N["complete"])}</b> · sube el ticket medio', 3)
    g += ad(c, f'<div class="ab" {bi("b", "center")}></div><div class="ao bl"><small>{E(c["city_short"])}</small><h6>Vuestra tienda,<br>abierta 24 horas.</h6><span class="pill">Visitar</span></div>',
            'Comprar ahora', '<b>Vuestra tienda</b> · lo que ya conocen, ahora online', 4)
    g += ad(c, f'<div class="ab sp"><i data-i="l2"></i><div class="bl2"><small>En {E(c["short"])}</small>' + ''.join(f'<span>{E(k["label"])}</span>' for k in c['cats']) + '<span>Novedades</span></div></div>',
            'Descubrir', '<b>Catálogo</b> · todo lo que tenéis, a un toque', 5)
    g += ad(c, f'<div class="ab" {bi("h", "70% center")}></div><div class="ao bl"><small>{E(A["a6s"])}</small><h6>{A["a6"]}</h6><span class="pill">{E(A["a6b"])}</span></div>',
            'Enviar mensaje', A['a6l'], 6)
    return f'<div class="adsx"><div class="adg">{g}</div></div>'


G.ads = ads


def ctx(slug):
    d = N33.load(slug); ni = d['niche']; T = N33.NICHE[ni]; city = d['city']
    th = d.get('theme') or {}
    logo = dict(d.get('logo') or dict(text=d['name']))
    if not logo.get('img'):
        n = len(logo['text']); logo.setdefault('fs', round(min(24, 205 / (n * 0.8)), 1)); logo.setdefault('ls', '0.12em' if n > 12 else '0.16em')
    if logo.get('img'):
        logo = dict(logo, png=os.path.join(N33.AI, slug, 'logo.png'))
    dom = d.get('domain') or slug.replace('-', '') + '.es'
    ah = [N33.T(x, d) for x in T['ad_h']]
    items = NV[ni]['item_pl']
    c = dict(slug=slug, niche=ni, name=d['name'], short=d.get('short', d['name']), handle=d['ig'], city=city, city_short=city,
             domain=dom, web_state='web' if d.get('domain') else 'none', logo=logo,
             colors=dict(t=th.get('acc', T['acc']) if T['acc'] not in ('#D7FF3A',) else '#2B2B2B', cream=th.get('bg', T['bg']) if T['bg'] != '#0C0C0C' else '#EFEDE8'),
             kpis=[(d['fk'], 'seguidores en Instagram'), ('24/7', 'abierta, también de noche'), ('15 días', 'para tenerla vendiendo'), ('España', f'entera, no solo {city}')],
             sub=f'Así se vería vuestra tienda online, hecha con vuestras {E(items)}. Tocadla: funciona, tiene cesta y se ve igual de bien en el móvil.',
             diag=dict(h2='Cada mensaje es una venta que espera.',
                       p=E(d.get('web_note') or f'Hoy no tenéis tienda online: quien os encuentra fuera de {city} solo puede escribiros.'),
                       leaks=[('Google', f'Quien busca «{d["name"]}» en Google no encuentra dónde comprar: solo vuestro Instagram.')]),
             cats=[dict(id=i, label=l) for l, i in d['cats']],
             ads=dict(a1s=f'Nuevo en {d.get("short", d["name"])}', a1=ah[2], a3=N33.T(T.get('a3', 'Completa<br>tu pedido.'), d),
                      a6s=f'{d["fk"]} seguidores ya os conocen', a6=ah[0], a6b='Escribir', a6l='<b>Mensajes</b> · conversaciones que acaban en venta'),
             hero_pos='72% center', hero_pos_m='70% center', close_pos='center 40%')
    return c


def images(c):
    """la og y el logo los deja gen33.py en out/; aquí solo se comprueba que están las 10"""
    miss = [i for i in IDS if not os.path.exists(os.path.join(N33.OUT, f'p-{c["slug"]}--b--{i}.jpg'))]
    assert not miss, (c['slug'], miss)
    return IDS


def build(slug):
    c = ctx(slug); ids = images(c)
    h = G.head(c, ids).replace('</head>', FRAME_CSS + '</head>') + G.body(c) + G.scripts(c).replace('</body>', FRAME_JS + '</body>')
    h = h.replace('href="/p-' + slug + '--tienda?embed=1', 'href="/p-' + slug + '--tienda')
    left = re.findall(r'\{[a-z_]+\}', re.sub(r'<(script|style)[^>]*>.*?</\1>', '', h, flags=re.S))
    assert not left, left[:5]
    open(os.path.join(N33.OUT, f'p-{slug}.html'), 'w', encoding='utf-8').write(h)
    print('ok', slug, len(h))


if __name__ == '__main__':
    for s in sys.argv[1:]:
        build(s)
