# Lote 33 (10/11/2026): propuestas con una tienda de ejemplo por nicho (moda, joya, cosmética, sneakers, óptica)
# y una propuesta común para todas, con los datos de cada tienda.
#   python3 gen33.py <slug> [<slug> ...]      → out/p-<slug>.html, out/p-<slug>--tienda.html y sus imágenes
# Datos: data/<slug>.json (ver LEEME.md). Fotos: ai/<slug>/<id>.jpg (h, b = 16:9; p1–p6, l1, l2 = 3:4).
import html, json, os, re, sys, urllib.parse
from PIL import Image

D = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(D, 'out')
AI = os.environ.get('L33_AI', os.path.join(D, 'ai'))
E = html.escape
BOOK = 'https://404growth.com/book?utm_source=propuesta&utm_medium=web&utm_campaign='
WA = 'https://wa.me/34610594450'
IDS = ['h', 'b', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'l1', 'l2', 'hd', 'hm']
FONT = "-apple-system,BlinkMacSystemFont,'SF Pro Display','SF Pro Text','Helvetica Neue',Inter,Arial,sans-serif"


def wa(c):
    return WA + '?text=' + urllib.parse.quote(f'Hola Christian, he visto la propuesta de {c["name"]}. ')


# ---------------------------------------------------------------- nichos
# tema: colores de la tienda (bg, superficie, tinta, acento), forma del hero y textos de la tienda (hablan al cliente: tú)
NICHE = {
    'moda': dict(
        bg='#F3EEE6', surf='#FFFFFF', ink='#15120F', mute='#6F675E', acc='#15120F', on='#FFFFFF', line='rgba(21,18,15,.12)',
        hero='full', up=True, eyebrow='Nueva temporada', h1='Lo nuevo<br>ya está aquí.', sub='Prendas elegidas una a una en nuestra tienda de {city}. Ahora, también online.',
        btn='Comprar novedades', marquee=['Nueva colección', 'Envío a toda España', 'Recogida gratis en {city}', 'Cambios fáciles', 'Pago con Bizum'],
        grid_h='Lo más deseado', grid_s='Lo que más nos pedís por Instagram, ya con talla y cesta.',
        opts_l='Talla', opts=['XS', 'S', 'M', 'L', 'XL'], ban_e='Look de la semana', ban_h='Vístete como<br>te apetezca.', ban_b='Ver el look',
        feat_e='La prenda estrella', item='prenda', items='prendas', badge='Nuevo',
        usp=[('truck', 'Envío a toda España', 'Pídelo hoy y te llega a casa.'), ('store', 'Recogida en {city}', 'Gratis, en nuestra tienda.'), ('swap', 'Cambios fáciles', 'Si no te queda bien, lo cambiamos.'), ('card', 'Tarjeta, Bizum y Apple Pay', 'Pago seguro en un toque.')],
        visit_h='Ven a probártelo.', club='Las novedades, antes que nadie', ad_h=['De {city}<br>a tu armario.', 'Lo que viste<br>en Instagram, ya online.', 'Nueva temporada.<br>Pídela hoy.']),
    'joya': dict(
        bg='#FBF8F2', surf='#FFFFFF', ink='#1B1712', mute='#7A6F60', acc='#A8834B', on='#FFFFFF', line='rgba(27,23,18,.12)',
        hero='split', up=False, eyebrow='Joyas para siempre', h1='Brillar<br>es un detalle.', sub='Piezas elegidas con mimo en nuestra joyería de {city}. Ahora, a un clic y con envío asegurado.',
        btn='Ver la colección', marquee=['Envío asegurado', 'Estuche de regalo', 'Recogida en {city}', 'Pago con Bizum', 'Grabado a mano'],
        grid_h='Las más deseadas', grid_s='Las piezas que más nos pedís, con su ficha, fotos y cesta.',
        opts_l='Acabado', opts=['Oro', 'Plata', 'Oro rosa'], ban_e='Para regalar', ban_h='Un regalo<br>que no se olvida.', ban_b='Ideas para regalar',
        feat_e='La pieza estrella', item='pieza', items='piezas', badge='Nuevo',
        usp=[('shield', 'Envío asegurado', 'Bien protegido, hasta tu puerta.'), ('gift', 'Listo para regalar', 'En su estuche, con tarjeta.'), ('store', 'Recogida en {city}', 'Gratis, en nuestra joyería.'), ('card', 'Tarjeta, Bizum y Apple Pay', 'Pago seguro en un toque.')],
        visit_h='Ven a verlas en persona.', club='Las piezas nuevas, antes que nadie', ad_h=['Joyas de {city}<br>para toda España.', 'Un regalo<br>que se queda.', 'La pieza que viste,<br>ya online.']),
    'cosmetica': dict(
        bg='#F7EEEA', surf='#FFFFFF', ink='#231518', mute='#7E6A6C', acc='#8E3B52', on='#FFFFFF', line='rgba(35,21,24,.12)',
        hero='full', up=False, eyebrow='Belleza y perfumería', h1='Tu ritual,<br>a un clic.', sub='Las marcas y los perfumes que te recomendamos en {city}, ahora con envío a casa.',
        btn='Descubrir', marquee=['Envío a toda España', 'Muestras de regalo', 'Recogida en {city}', 'Asesoramiento por WhatsApp', 'Pago con Bizum'],
        grid_h='Los favoritos', grid_s='Lo que más nos pedís, con su ficha y su cesta.',
        opts_l='Formato', opts=['30 ml', '50 ml', '100 ml'], ban_e='Rutina de la semana', ban_h='Piel bonita,<br>sin complicarte.', ban_b='Ver la rutina',
        feat_e='El favorito', item='producto', items='productos', badge='Top',
        usp=[('truck', 'Envío a toda España', 'Pídelo hoy y te llega a casa.'), ('gift', 'Muestras de regalo', 'En cada pedido.'), ('chat', 'Te asesoramos', 'Por WhatsApp, como en la tienda.'), ('card', 'Tarjeta, Bizum y Apple Pay', 'Pago seguro en un toque.')],
        visit_h='Ven a probarlo.', club='Las novedades y los regalos, antes que nadie', ad_h=['Tu perfume,<br>en casa.', 'De {city}<br>a toda España.', 'Lo que te recomendamos,<br>ya online.']),
    'sneakers': dict(
        bg='#0C0C0C', surf='#161616', ink='#F5F5F2', mute='#9A9A94', acc='#D7FF3A', on='#0C0C0C', line='rgba(245,245,242,.14)',
        hero='full', up=True, eyebrow='Drop nuevo', h1='Las que buscas.<br>Ya.', sub='Pares elegidos en nuestra tienda de {city}. Pídelos hoy y te llegan a casa.',
        btn='Comprar ahora', marquee=['Drop nuevo', 'Envío a toda España', 'Recogida en {city}', 'Cambio de talla fácil', 'Pago con Bizum'],
        grid_h='Lo más buscado', grid_s='Los pares que más nos pedís, con talla y cesta.',
        opts_l='Talla', opts=['38', '39', '40', '41', '42', '43', '44'], ban_e='Fresh in', ban_h='Pisa<br>diferente.', ban_b='Ver novedades',
        feat_e='El par de la semana', item='par', items='pares', badge='Nuevo',
        usp=[('truck', 'Envío a toda España', 'Pídelas hoy, estrénalas ya.'), ('swap', 'Cambio de talla', 'Si no te quedan, las cambiamos.'), ('store', 'Recogida en {city}', 'Gratis, en nuestra tienda.'), ('card', 'Tarjeta, Bizum y Apple Pay', 'Pago seguro en un toque.')],
        visit_h='Ven a probártelas.', club='Los drops, antes que nadie', ad_h=['Drop nuevo.<br>Ya online.', 'De {city}<br>a toda España.', 'Tu talla,<br>a un clic.']),
    'calzado': dict(
        bg='#F4EFE8', surf='#FFFFFF', ink='#1A1512', mute='#74695F', acc='#7A2E2A', on='#FFFFFF', line='rgba(26,21,18,.12)',
        hero='full', up=True, eyebrow='Calzado para toda la familia', h1='Tus zapatos,<br>a un clic.', sub='Los pares de nuestra zapatería de {city}, ahora con envío a casa y cambio de talla fácil.',
        btn='Comprar ahora', marquee=['Nueva temporada', 'Envío a toda España', 'Recogida en {city}', 'Cambio de talla fácil', 'Pago con Bizum'],
        grid_h='Lo más vendido', grid_s='Los pares que más nos pedís, con talla y cesta.',
        opts_l='Talla', opts=['36', '37', '38', '39', '40', '41', '42'], ban_e='Nueva temporada', ban_h='Pisa fuerte<br>esta temporada.', ban_b='Ver novedades',
        feat_e='El par de la semana', item='par', items='pares', badge='Nuevo',
        usp=[('truck', 'Envío a toda España', 'Pídelos hoy y te llegan a casa.'), ('swap', 'Cambio de talla', 'Si no te quedan, los cambiamos.'), ('store', 'Recogida en {city}', 'Gratis, en nuestra tienda.'), ('card', 'Tarjeta, Bizum y Apple Pay', 'Pago seguro en un toque.')],
        visit_h='Ven a probártelos.', club='La nueva temporada, antes que nadie', ad_h=['Tus zapatos,<br>en casa.', 'De {city}<br>a toda España.', 'Tu talla,<br>a un clic.']),
    'optica': dict(
        bg='#F2F5F7', surf='#FFFFFF', ink='#0E1A24', mute='#5E6C78', acc='#1F4E79', on='#FFFFFF', line='rgba(14,26,36,.12)',
        hero='split', up=False, eyebrow='Gafas de sol y graduadas', h1='Mira bien.<br>Mírate mejor.', sub='Las monturas de nuestra óptica de {city}, ahora online. Y tu revisión, reservada en un minuto.',
        btn='Ver monturas', marquee=['Reserva tu revisión', 'Envío a toda España', 'Ajuste gratis en {city}', 'Gafas de sol', 'Pago con Bizum'],
        grid_h='Monturas favoritas', grid_s='Las que más os probáis, con su ficha y su cesta.',
        opts_l='Uso', opts=['Graduada', 'De sol'], ban_e='Gafas de sol', ban_h='Que el sol<br>te pille guapo.', ban_b='Ver gafas de sol',
        feat_e='La montura estrella', item='montura', items='monturas', badge='Nuevo',
        usp=[('eye', 'Reserva tu revisión', 'Elige día y hora, sin llamar.'), ('truck', 'Envío a toda España', 'Bien protegidas, hasta tu puerta.'), ('store', 'Ajuste en {city}', 'Gratis, en nuestra óptica.'), ('card', 'Tarjeta, Bizum y Apple Pay', 'Pago seguro en un toque.')],
        visit_h='Ven a probártelas.', club='Las monturas nuevas, antes que nadie', ad_h=['Tu revisión,<br>en un minuto.', 'Monturas de {city}<br>para toda España.', 'La montura que viste,<br>ya online.']),
}

ICONS = {
    'plus': '<path d="M12 5v14M5 12h14"/>',
    'truck': '<path d="M3 7h11v9H3zM14 10h4l3 3v3h-7z"/><circle cx="7" cy="17.5" r="1.6"/><circle cx="17" cy="17.5" r="1.6"/>',
    'store': '<path d="M4 9l1.5-4h13L20 9M4 9h16v11H4zM4 9c0 1.7 1.3 3 3 3s3-1.3 3-3c0 1.7 1.3 3 3 3s3-1.3 3-3c0 1.7 1.3 3 3 3"/><path d="M10 20v-5h4v5"/>',
    'swap': '<path d="M7 7h11l-3-3M17 17H6l3 3"/>',
    'card': '<rect x="3" y="6" width="18" height="12" rx="2"/><path d="M3 10h18M7 15h3"/>',
    'shield': '<path d="M12 3l7 3v6c0 4-3 7.5-7 9-4-1.5-7-5-7-9V6z"/><path d="M9 12l2 2 4-4"/>',
    'gift': '<rect x="4" y="9" width="16" height="11" rx="1"/><path d="M3 9h18M12 9v11M12 9c-2-4-6-4-6-1.5S10 9 12 9c2 0 6 0 6-1.5S14 5 12 9"/>',
    'chat': '<path d="M20 12a8 8 0 0 1-11.7 7.1L4 20l1-4.1A8 8 0 1 1 20 12z"/>',
    'eye': '<path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
    'bag': '<path d="M5 8h14l-1 12H6z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/>',
    'search': '<circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/>',
    'user': '<circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/>',
    'heart': '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>',
    'menu': '<path d="M4 7h16M4 12h16M4 17h16"/>',
    'pin': '<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
    'insta': '<rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r=".9" fill="currentColor"/>',
    'x': '<path d="M6 6l12 12M18 6L6 18"/>',
    'arrow': '<path d="M5 12h14M13 6l6 6-6 6"/>',
    'check': '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
    'spark': '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5L18 18M6 18l2.5-2.5M15.5 8.5L18 6"/>',
    'box': '<path d="M3 7l9-4 9 4v10l-9 4-9-4z"/><path d="M3 7l9 4 9-4M12 11v10"/>',
    'chart': '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    'phone': '<rect x="6" y="2.5" width="12" height="19" rx="3"/><path d="M10.5 18.5h3"/>',
}


def ic(k, w=20, sw=1.6):
    return f'<svg class="ic" viewBox="0 0 24 24" width="{w}" height="{w}" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[k]}</svg>'


def T(s, c):
    return s.replace('{city}', c['city'])


def img(c, i):
    return f'/p-{c["slug"]}--b--{i}.jpg'


def logo(c, cls='lg'):
    L = c.get('logo') or {}
    if L.get('img'):
        return f'<img class="{cls} lgi" src="/p-{c["slug"]}--b--logo.png" alt="{E(c["name"])}">'
    t = L.get('text', c['name'])
    if 'fs' not in L and len(t) > 14:
        L = dict(L, fs=round(max(.56, 14 / len(t)), 2), ls=L.get('ls', '.1em'))
    return (f'<span class="{cls} lgt" style="--lfs:{L.get("fs", 1)};--lls:{L.get("ls", ".14em")};--lfw:{L.get("fw", 700)}">{E(t)}'
            + (f'<small>{E(L["sub"])}</small>' if L.get('sub') else '') + '</span>')


def price(c, p):
    return E(p.get('price') or 'Vuestro precio')


# ---------------------------------------------------------------- la tienda (página propia, se ve dentro de la propuesta)
STORE_CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{font-family:var(--f);background:var(--bg);color:var(--ink);-webkit-font-smoothing:antialiased;line-height:1.45;overflow-x:clip}html{overflow-x:clip}
a{color:inherit;text-decoration:none}button{font:inherit;color:inherit;background:none;border:0;cursor:pointer}img{display:block;max-width:100%}
.ic{flex:none}.w{max-width:1320px;margin:0 auto;padding:0 clamp(16px,3.4vw,44px)}
html.emb::-webkit-scrollbar{display:none}html.emb{scrollbar-width:none}
/* barra de aviso */
.ann{background:var(--acc);color:var(--on);font-size:12.5px;font-weight:600;letter-spacing:.04em;text-align:center;height:34px;overflow:hidden;position:relative}
.ann span{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;opacity:0;transform:translateY(8px);transition:.5s}
.ann span.on{opacity:1;transform:none}
/* cabecera */
.hd{position:sticky;top:0;z-index:30;background:color-mix(in srgb,var(--bg) 94%,transparent);border-bottom:1px solid var(--line)}
.hd .w{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;height:72px;gap:16px}
.nv{display:flex;gap:26px;font-size:14px;font-weight:500}.nv a{opacity:.82}.nv a:hover{opacity:1}
.lg{justify-self:center;display:flex;align-items:center}.lgi{height:44px;width:auto;max-width:200px;object-fit:contain}
.lgt{font-size:calc(22px * var(--lfs));font-weight:var(--lfw);letter-spacing:var(--lls);text-transform:uppercase;white-space:nowrap;display:flex;flex-direction:column;align-items:center;line-height:1}
.lgt small{font-size:9.5px;letter-spacing:.32em;font-weight:500;margin-top:5px;opacity:.7}
.ia{justify-self:end;display:flex;gap:6px;align-items:center}.ia button{width:40px;height:40px;border-radius:50%;display:grid;place-items:center;position:relative}
.ia button:hover{background:var(--line)}.bq{position:absolute;top:3px;right:2px;min-width:17px;height:17px;padding:0 4px;border-radius:9px;background:var(--acc);color:var(--on);font-size:10.5px;font-weight:700;display:grid;place-items:center;transform:scale(0);transition:transform .3s cubic-bezier(.3,1.6,.5,1)}
.bq.on{transform:scale(1)}.mb{display:none!important}
/* hero */
.hero{position:relative;min-height:min(92vh,860px);display:flex;align-items:flex-end;overflow:hidden;color:#fff;isolation:isolate}
.hero>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:var(--hp,center);z-index:-2;transform:scale(1.04);animation:kb 14s ease-out forwards}
@keyframes kb{to{transform:scale(1)}}
.hero:after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(90deg,rgba(0,0,0,.62) 0%,rgba(0,0,0,.34) 38%,rgba(0,0,0,0) 66%),linear-gradient(0deg,rgba(0,0,0,.55) 0%,rgba(0,0,0,0) 45%)}
.hero .w{width:100%;padding-bottom:clamp(40px,7vh,84px)}
.hc{max-width:720px}
.eb{display:inline-flex;align-items:center;gap:8px;font-size:12.5px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;padding:8px 14px;border-radius:99px;background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.32)}
.eb:before{content:"";width:7px;height:7px;border-radius:50%;background:var(--acc2,#fff)}
.hero h1{font-size:clamp(46px,7.6vw,118px);line-height:.94;letter-spacing:-.035em;font-weight:800;margin:20px 0 18px;text-wrap:balance}
.up .hero h1{text-transform:uppercase;letter-spacing:-.025em}
.hero p{font-size:clamp(16px,1.35vw,19px);max-width:470px;opacity:.92;font-weight:450}
.bt{display:inline-flex;align-items:center;gap:10px;white-space:nowrap;height:54px;padding:0 28px;border-radius:99px;font-weight:650;font-size:15.5px;transition:transform .2s,background .2s}
.bt:active{transform:scale(.97)}.bt.w1{background:#fff;color:#111}.bt.w1:hover{transform:translateY(-2px)}
.bt.g1{border:1.5px solid rgba(255,255,255,.7);color:#fff}.bt.g1:hover{background:rgba(255,255,255,.12)}
.bt.k{background:var(--ink);color:var(--bg)}.bt.a{background:var(--acc);color:var(--on)}
.hb{display:flex;gap:12px;flex-wrap:wrap;margin-top:30px}
.hm{position:absolute;right:clamp(16px,3.4vw,44px);bottom:clamp(40px,7vh,84px);display:flex;gap:10px;align-items:center;font-size:13px;font-weight:600;background:rgba(255,255,255,.94);color:#111;padding:9px 14px 9px 9px;border-radius:99px;box-shadow:0 10px 30px rgba(0,0,0,.18)}
.hm img{width:40px;height:40px;border-radius:50%;object-fit:cover}.hm small{display:block;font-weight:500;color:#666;font-size:11.5px}
/* hero partido (joyería, óptica): texto oscuro sobre el fondo claro, siempre legible */
.hero.sp{color:var(--ink);align-items:stretch;min-height:min(86vh,800px)}
.hero.sp:after{display:none}.hero.sp>img{left:42%;width:58%;animation:none;transform:none}
.hero.sp .w{display:flex;align-items:center;padding-top:40px;padding-bottom:40px}.hero.sp .hc{max-width:44%}
.hero.sp .eb{background:transparent;border-color:var(--line);color:var(--acc)}.hero.sp .eb:before{background:var(--acc)}
.hero.sp h1{font-weight:300;letter-spacing:-.04em;font-size:clamp(40px,4.4vw,70px)}.hero.sp h1 em{font-style:normal;font-weight:700;color:var(--acc)}
.hero.sp p{opacity:1;color:var(--mute)}.hero.sp .bt.w1{background:var(--ink);color:var(--bg)}.hero.sp .bt.g1{border-color:var(--ink);color:var(--ink)}
/* hero de producto (10/11) */
.hx{background:var(--bg);color:var(--ink);padding:clamp(28px,4vw,56px) 0 clamp(36px,5vw,64px)}
.hxg{display:grid;grid-template-columns:minmax(0,.92fr) minmax(0,1.08fr);gap:clamp(28px,4vw,64px);align-items:center}
.hx .eb{background:transparent;border:1px solid var(--line);color:var(--acc)}.hx .eb:before{background:var(--acc)}
.hx h1{font-size:clamp(44px,5.4vw,84px);line-height:.96;letter-spacing:-.04em;font-weight:800;margin:22px 0 18px;text-wrap:balance}
.up .hx h1{text-transform:uppercase;letter-spacing:-.03em}
.hx p{font-size:clamp(16px,1.25vw,18.5px);color:var(--mute);max-width:470px;line-height:1.5}
.bt.o1{border:1.5px solid var(--ink);color:var(--ink)}.bt.o1:hover{background:var(--line)}
.tr{display:flex;flex-wrap:wrap;gap:8px 18px;margin-top:26px;font-size:13.5px;font-weight:550;color:var(--mute)}.tr span{display:inline-flex;align-items:center;gap:7px}.tr svg{color:var(--acc)}
.hxm{display:grid;grid-template-columns:1.15fr 1fr 1fr;grid-template-rows:1fr 1fr;gap:12px;height:min(660px,74vh);min-height:480px}
.ht{position:relative;border-radius:20px;overflow:hidden;background:var(--surf)}
.ht img{width:100%;height:100%;object-fit:cover;object-position:center 32%;transition:transform .7s cubic-bezier(.2,.8,.2,1)}.ht:hover img{transform:scale(1.04)}
.ht.t0{grid-row:1/3}.ht.t0 img{object-position:var(--hx,74%) center}
.ht img{object-position:center 40%}
.tg{position:absolute;left:14px;top:14px;font-size:12px;font-weight:650;letter-spacing:.12em;text-transform:uppercase;color:#fff;background:rgba(0,0,0,.35);padding:6px 11px;border-radius:99px}
.tl{position:absolute;left:12px;bottom:12px;right:60px;background:rgba(255,255,255,.94);color:#111;border-radius:14px;padding:9px 12px;box-shadow:0 8px 24px rgba(0,0,0,.12)}
.tl b{display:block;font-size:14px;font-weight:650;line-height:1.2}.tl small{font-size:12px;color:#666}
.ta{position:absolute;right:12px;bottom:12px;width:42px;height:42px;border-radius:50%;background:var(--ink);color:var(--bg);display:grid;place-items:center;box-shadow:0 8px 20px rgba(0,0,0,.18)}
.dark .hx .eb{color:var(--acc)}.dark .tl{background:rgba(22,22,22,.92);color:#f5f5f2}.dark .tl small{color:#aaa}.dark .ta{background:var(--acc);color:var(--on)}.dark .hx h1{font-weight:900}
@media (max-width:900px){
 .hx{padding:18px 0 26px}.hxg{grid-template-columns:minmax(0,1fr);gap:16px}
 .hx .eb{font-size:11px;padding:6px 11px}.hx h1{font-size:clamp(34px,9.6vw,46px);margin:12px 0 8px}.hx p{display:none}
 .hb{margin-top:14px}.hb .bt{height:48px}.tr{display:none}
 .hxm{order:2;height:auto;min-height:0;grid-template-columns:1fr 1fr;grid-template-rows:auto auto;gap:8px}
 .ht{aspect-ratio:4/5;border-radius:16px}.ht.t0{grid-row:auto}.ht.t4{display:none}
 .tl{left:8px;bottom:8px;right:52px;padding:7px 9px;border-radius:11px}.tl b{font-size:12.5px}.tl small{font-size:11px}.ta{right:8px;bottom:8px;width:36px;height:36px}
}
.hero.hz picture{position:absolute;inset:0;z-index:-2}.hero.hz picture img{width:100%;height:100%;object-fit:cover;object-position:center}
@media (max-width:900px){.hero.hz picture img{object-position:center top}.hero.hz:after{background:linear-gradient(0deg,rgba(0,0,0,.78) 0%,rgba(0,0,0,.45) 34%,rgba(0,0,0,0) 56%)}}
/* cinta */
.mq{background:var(--ink);color:var(--bg);overflow:hidden;white-space:nowrap;padding:17px 0;font-weight:700;font-size:clamp(15px,1.4vw,19px);letter-spacing:.01em}
.up .mq{text-transform:uppercase}.dark .mq{background:var(--acc);color:var(--on)}
.mq div{display:inline-flex;animation:mq 34s linear infinite}.mq span{display:inline-flex;align-items:center;gap:28px;padding-right:28px}
.mq span:after{content:"✦";font-size:.8em;opacity:.7}@keyframes mq{to{transform:translateX(-50%)}}
/* secciones */
.sx{padding:clamp(64px,9vw,120px) 0}.sh{display:flex;justify-content:space-between;align-items:flex-end;gap:24px;margin-bottom:clamp(26px,3.5vw,44px)}
.sh h2{font-size:clamp(34px,4.6vw,66px);line-height:.98;letter-spacing:-.035em;font-weight:780;text-wrap:balance}.up .sh h2{text-transform:uppercase;letter-spacing:-.02em}
.sh p{color:var(--mute);max-width:360px;font-size:15.5px}.sh a{font-weight:650;font-size:15px;display:inline-flex;gap:8px;align-items:center;border-bottom:1.5px solid currentColor;padding-bottom:3px;white-space:nowrap}
/* categorías */
.cg{display:grid;grid-template-columns:1.25fr 1fr 1fr;gap:14px}
.ct{position:relative;border-radius:20px;overflow:hidden;aspect-ratio:3/4;display:flex;align-items:flex-end;color:#fff;isolation:isolate}
.ct:first-child{aspect-ratio:auto}.ct img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:-2;transition:transform .9s cubic-bezier(.2,.7,.2,1)}
.ct:hover img{transform:scale(1.05)}.ct:after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(0deg,rgba(0,0,0,.6),rgba(0,0,0,0) 52%)}
.ct div{padding:24px;width:100%;display:flex;justify-content:space-between;align-items:flex-end;gap:12px}.ct b{font-size:clamp(24px,2.4vw,34px);letter-spacing:-.025em;line-height:1;font-weight:760}
.up .ct b{text-transform:uppercase}.ct span{width:46px;height:46px;border-radius:50%;background:#fff;color:#111;display:grid;place-items:center;flex:none;transition:transform .3s}.ct:hover span{transform:rotate(-45deg)}
/* productos */
.pg{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(12px,1.6vw,22px)}
.pc{position:relative}.pi{position:relative;border-radius:18px;overflow:hidden;aspect-ratio:4/5;background:var(--surf)}
.pi img{width:100%;height:100%;object-fit:cover;object-position:center 30%;transition:transform .9s cubic-bezier(.2,.7,.2,1)}.pc:hover .pi img{transform:scale(1.045)}
.bd{position:absolute;top:14px;left:14px;font-size:11.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;background:var(--surf);color:var(--ink);padding:6px 11px;border-radius:99px}
.hr{position:absolute;top:10px;right:10px;width:38px;height:38px;border-radius:50%;background:var(--surf);color:var(--ink);display:grid;place-items:center;transition:.2s}
.hr.on{color:#E0334E}.hr.on svg{fill:currentColor}
.qa{position:absolute;left:12px;right:12px;bottom:12px;height:48px;border-radius:99px;background:var(--ink);color:var(--bg);font-weight:650;font-size:14.5px;display:flex;align-items:center;justify-content:center;gap:8px;transform:translateY(16px);opacity:0;transition:.3s}
.pc:hover .qa{transform:none;opacity:1}.qa.ok{background:var(--acc);color:var(--on)}
.pm{display:flex;justify-content:space-between;gap:12px;padding:14px 4px 0;align-items:baseline}.pm b{font-weight:620;font-size:16px;letter-spacing:-.01em}.pm span{color:var(--mute);font-size:14.5px;white-space:nowrap}
.sw{display:flex;gap:6px;padding:8px 4px 0}.sw i{width:14px;height:14px;border-radius:50%;border:1px solid var(--line)}
/* banner */
.bn{position:relative;border-radius:28px;overflow:hidden;min-height:clamp(420px,52vw,640px);display:flex;align-items:center;color:#fff;isolation:isolate}
.bn img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:var(--bp,center);z-index:-2}
.bn:after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(90deg,rgba(0,0,0,.58),rgba(0,0,0,.18) 55%,rgba(0,0,0,0))}
.bn div{padding:clamp(28px,5vw,72px);max-width:640px}.bn small{font-size:12.5px;font-weight:650;letter-spacing:.16em;text-transform:uppercase;opacity:.9}
.bn h3{font-size:clamp(36px,4.4vw,68px);line-height:.95;letter-spacing:-.04em;font-weight:800;margin:14px 0 26px;text-wrap:balance}.up .bn h3{text-transform:uppercase;letter-spacing:-.025em}
/* destacado */
.ft{display:grid;grid-template-columns:1.1fr 1fr;gap:clamp(24px,4vw,64px);align-items:center}
.fg{display:grid;grid-template-columns:1.5fr 1fr;grid-template-rows:1fr 1fr;gap:12px}.fg img{width:100%;height:100%;object-fit:cover;object-position:center 25%;border-radius:18px}.fg img:first-child{grid-row:1/3;aspect-ratio:4/5}
.fi small{font-size:12.5px;font-weight:650;letter-spacing:.16em;text-transform:uppercase;color:var(--acc)}.dark .fi small{color:var(--acc)}
.fi h3{font-size:clamp(32px,3.6vw,52px);line-height:1;letter-spacing:-.03em;font-weight:760;margin:12px 0 10px}.up .fi h3{text-transform:uppercase}
.fi .pr{font-size:22px;font-weight:600;margin-bottom:18px}.fi .pr small{font-size:13px;color:var(--mute);letter-spacing:0;text-transform:none;font-weight:450}
.fi p{color:var(--mute);margin-bottom:24px;max-width:440px}.ol{font-size:13px;font-weight:650;margin-bottom:10px}
.os{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:22px}.os button{min-width:52px;height:46px;padding:0 16px;border-radius:12px;border:1.5px solid var(--line);font-weight:600;font-size:14.5px;transition:.15s}
.os button.on{border-color:var(--ink);background:var(--ink);color:var(--bg)}
.fa{display:flex;gap:10px}.fa .bt{flex:1;justify-content:center;height:58px}
.py{display:flex;gap:8px;margin-top:16px;flex-wrap:wrap}.py span{font-size:12px;font-weight:650;padding:6px 10px;border-radius:8px;border:1px solid var(--line);color:var(--mute)}
.fl{margin-top:22px;border-top:1px solid var(--line)}.fl div{display:flex;gap:12px;align-items:center;padding:14px 0;border-bottom:1px solid var(--line);font-size:14.5px}.fl svg{color:var(--acc)}
/* ventajas */
.us{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.us div{background:var(--surf);border-radius:20px;padding:26px 22px;border:1px solid var(--line)}
.us svg{color:var(--acc);margin-bottom:18px}.us b{display:block;font-size:17px;letter-spacing:-.01em;margin-bottom:4px;font-weight:650}.us p{color:var(--mute);font-size:14.5px}
/* visítanos */
.vs{display:grid;grid-template-columns:1fr 1fr;border-radius:28px;overflow:hidden;background:var(--surf);border:1px solid var(--line)}
.vs img{width:100%;height:100%;min-height:460px;object-fit:cover}.vs div{padding:clamp(28px,5vw,64px);display:flex;flex-direction:column;justify-content:center}
.vs small{font-size:12.5px;font-weight:650;letter-spacing:.16em;text-transform:uppercase;color:var(--acc)}
.vs h3{font-size:clamp(34px,4vw,58px);letter-spacing:-.035em;line-height:.98;font-weight:780;margin:12px 0 22px}.up .vs h3{text-transform:uppercase}
.vs ul{list-style:none;display:grid;gap:12px;margin-bottom:28px}.vs li{display:flex;gap:12px;align-items:flex-start;font-size:15.5px}.vs li svg{color:var(--acc);margin-top:1px}
/* club */
.cl{background:var(--ink);color:var(--bg);border-radius:28px;padding:clamp(32px,5vw,64px);display:grid;grid-template-columns:1.2fr 1fr;gap:28px;align-items:center}
.dark .cl{background:var(--acc);color:var(--on)}
.cl h3{font-size:clamp(30px,3.6vw,50px);letter-spacing:-.035em;line-height:1;font-weight:780}.up .cl h3{text-transform:uppercase}
.cl form{display:flex;gap:8px;background:color-mix(in srgb,var(--bg) 12%,transparent);border-radius:99px;padding:6px}
.cl input{flex:1;min-width:0;background:none;border:0;color:inherit;font:inherit;font-size:15.5px;padding:0 16px;outline:0}.cl input::placeholder{color:inherit;opacity:.6}
.cl button{height:50px;padding:0 24px;border-radius:99px;background:var(--bg);color:var(--ink);font-weight:650}
.dark .cl button{background:var(--on);color:var(--acc)}
/* pie */
.fo{padding:64px 0 40px;border-top:1px solid var(--line);margin-top:clamp(64px,9vw,120px)}
.fo .w{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:28px}.fo b{display:block;font-size:13px;letter-spacing:.08em;text-transform:uppercase;margin-bottom:14px}
.fo p,.fo a{display:block;color:var(--mute);font-size:14.5px;margin-bottom:8px}.fo .lg{justify-self:start;margin-bottom:16px}
.fx{max-width:1320px;margin:40px auto 0;padding:24px clamp(16px,3.4vw,44px) 0;border-top:1px solid var(--line);display:flex;justify-content:space-between;gap:16px;color:var(--mute);font-size:12.5px;flex-wrap:wrap}
/* cesta */
.ov{position:fixed;inset:0;background:rgba(0,0,0,.42);opacity:0;pointer-events:none;transition:.3s;z-index:60}.ov.on{opacity:1;pointer-events:auto}
.dr{position:fixed;top:0;right:0;bottom:0;width:min(420px,92vw);background:var(--bg);color:var(--ink);z-index:61;transform:translateX(102%);visibility:hidden;transition:transform .45s cubic-bezier(.2,.8,.2,1),visibility 0s .45s;display:flex;flex-direction:column}
.dr.on{transform:none;visibility:visible;transition:transform .45s cubic-bezier(.2,.8,.2,1)}.dh{display:flex;justify-content:space-between;align-items:center;padding:20px 22px;border-bottom:1px solid var(--line)}.dh b{font-size:19px;letter-spacing:-.01em}
.dl{flex:1;overflow:auto;padding:12px 22px}.di{display:grid;grid-template-columns:72px 1fr auto;gap:14px;align-items:center;padding:12px 0;border-bottom:1px solid var(--line)}
.di img{width:72px;height:90px;object-fit:cover;border-radius:10px}.di b{display:block;font-size:15px;font-weight:620}.di small{color:var(--mute);font-size:13px}
.de{color:var(--mute);text-align:center;padding:56px 10px}.df{padding:20px 22px;border-top:1px solid var(--line)}
.df .bt{width:100%;justify-content:center;height:56px}.df p{font-size:12.5px;color:var(--mute);text-align:center;margin-top:10px}
.tz{position:fixed;left:50%;bottom:24px;transform:translate(-50%,20px);background:var(--ink);color:var(--bg);padding:13px 20px;border-radius:14px;font-size:14px;font-weight:550;opacity:0;transition:.35s;z-index:70;max-width:min(520px,92vw);text-align:center;pointer-events:none}
.tz.on{opacity:1;transform:translate(-50%,0)}
/* aparición */
.rv{opacity:0;transform:translateY(26px);transition:opacity .8s,transform .8s cubic-bezier(.2,.7,.2,1)}.rv.in{opacity:1;transform:none}
/* oscuro (sneakers) */
.dark .hd{background:color-mix(in srgb,var(--bg) 92%,transparent)}.dark .pi{background:#1c1c1c}
.dark .eb:before{background:var(--acc)}.dark .hero h1 .a,.dark .bn h3 .a{color:var(--acc)}
.dark .bt.w1{background:var(--acc);color:var(--on)}.dark .qa{background:var(--acc);color:var(--on)}
.dark .ct span{background:var(--acc)}.dark .us div,.dark .vs{background:var(--surf)}
.dark .hero h1{font-weight:900}
/* móvil */
@media (max-width:900px){
 .nv{display:none}.mb{display:grid!important}.hd .w{height:60px;grid-template-columns:auto 1fr auto}.lg{justify-self:start}.lgi{height:34px;max-width:150px}.lgt{font-size:calc(17px * var(--lfs))}
 .ia .hs{display:none}
 .hero{min-height:calc(100svh - 94px);max-height:760px}.hero:after{background:linear-gradient(0deg,rgba(0,0,0,.74) 0%,rgba(0,0,0,.38) 46%,rgba(0,0,0,.05) 72%)}
 .hero>img{object-position:var(--hpm,var(--hp,center))}.hero h1{font-size:clamp(42px,12.4vw,64px);margin:16px 0 12px}.hero p{font-size:15.5px}
 .hb .bt{flex:1;justify-content:center;padding:0 12px;font-size:14.5px;gap:6px}.hm{display:none}
 .hero.sp{flex-direction:column;min-height:0;max-height:none}.hero.sp>img{position:relative;left:0;width:100%;height:auto;aspect-ratio:4/3.4;order:-1}
 .hero.sp .w{padding-top:30px;padding-bottom:36px}.hero.sp .hc{max-width:none}
 .cg{grid-template-columns:1fr 1fr}.ct:first-child{grid-column:1/-1;aspect-ratio:16/11}.ct div{padding:16px}.ct span{width:38px;height:38px}
 .pg{grid-template-columns:1fr 1fr}.qa{opacity:1;transform:none;height:40px;font-size:13px;left:8px;right:8px;bottom:8px}.pm{flex-direction:column;gap:2px;padding-top:10px}.pm b{font-size:14.5px}
 .sh{flex-direction:column;align-items:flex-start}.ft,.vs,.cl{grid-template-columns:minmax(0,1fr)}.fg{grid-template-columns:1.4fr 1fr}.vs img{min-height:0;aspect-ratio:4/3}
 .us{grid-template-columns:1fr 1fr}.us div{padding:18px 16px}.fo .w{grid-template-columns:1fr 1fr}.fo .w>div:first-child{grid-column:1/-1}
 .bn{border-radius:20px;min-height:480px;align-items:flex-end}.bn:after{background:linear-gradient(0deg,rgba(0,0,0,.7),rgba(0,0,0,0) 65%)}.bn img{object-position:var(--bpm,var(--bp,center))}
}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}.rv{opacity:1;transform:none}}
"""

STORE_JS = r"""
(function(){var d=document,q=function(s,e){return (e||d).querySelector(s)},qa=function(s,e){return [].slice.call((e||d).querySelectorAll(s))};
var emb=/[?&](embed|tour)=1/.test(location.search);if(emb)d.documentElement.classList.add('emb');
/* dentro de la propuesta v33: ?embed=1 dice su alto a la página de fuera; ?at=<id> se queda en esa sección */
if(/[?&]embed=1/.test(location.search)&&parent!==window){var ph=function(){parent.postMessage({h404:d.documentElement.scrollHeight,q:location.search},'*')};addEventListener('load',ph);setTimeout(ph,800);setTimeout(ph,2500);if(window.ResizeObserver)new ResizeObserver(ph).observe(d.body)}
var at=(location.search.match(/[?&]at=([a-z]+)/)||[])[1];if(at){d.documentElement.classList.add('at');var go=function(){var el=d.getElementById(at);if(el)scrollTo(0,el.getBoundingClientRect().top+scrollY-20)};addEventListener('load',go);setTimeout(go,300);setTimeout(go,1200)}
/* aviso que rota */var an=qa('.ann span'),ai=0;if(an.length>1)setInterval(function(){an[ai].classList.remove('on');ai=(ai+1)%an.length;an[ai].classList.add('on')},3200);
/* cesta */var bag=[],dr=q('.dr'),ov=q('.ov'),tz=q('.tz'),tt;
function toast(t){tz.textContent=t;tz.classList.add('on');clearTimeout(tt);tt=setTimeout(function(){tz.classList.remove('on')},2600)}
function draw(){var n=bag.length,b=q('.bq');b.textContent=n;b.classList.toggle('on',n>0);var l=q('.dl');
 l.innerHTML=n?bag.map(function(x,i){return '<div class="di"><img src="'+x.i+'" alt=""><div><b>'+x.n+'</b><small>'+x.o+' · '+x.p+'</small></div><button data-rm="'+i+'" aria-label="Quitar">'+X+'</button></div>'}).join(''):'<p class="de">Tu cesta está vacía.</p>'}
var X=q('.dh button').innerHTML;function open(o){dr.classList.toggle('on',o);ov.classList.toggle('on',o)}
d.addEventListener('click',function(e){var t=e.target.closest('[data-add],[data-bag],[data-rm],[data-close],.hr,.os button,[data-pay],[data-demo]');if(!t)return;
 if(t.hasAttribute('data-add')){e.preventDefault();var o=q('.os button.on'),f=t.closest('.ft');bag.push({n:t.dataset.n,i:t.dataset.i,p:t.dataset.p,o:f&&o?o.textContent:t.dataset.o});draw();
  if(t.classList.contains('qa')){var h=t.innerHTML;t.classList.add('ok');t.innerHTML='Añadido ✓';setTimeout(function(){t.classList.remove('ok');t.innerHTML=h},1400)}else open(true)}
 else if(t.hasAttribute('data-bag')){open(true)}else if(t.hasAttribute('data-close')){open(false)}
 else if(t.hasAttribute('data-rm')){bag.splice(+t.dataset.rm,1);draw()}
 else if(t.classList.contains('hr')){t.classList.toggle('on')}
 else if(t.parentNode.classList.contains('os')){qa('button',t.parentNode).forEach(function(b){b.classList.toggle('on',b===t)})}
 else if(t.hasAttribute('data-pay')){toast('Tienda de ejemplo: aquí pagarías con tarjeta, Bizum o Apple Pay.')}
 else if(t.hasAttribute('data-demo')){e.preventDefault();toast('Tienda de ejemplo hecha por 404 Growth.')}});
ov.addEventListener('click',function(){open(false)});
qa('form').forEach(function(f){f.addEventListener('submit',function(e){e.preventDefault();toast('Tienda de ejemplo: aquí te apuntarías al club.')})});
draw();
/* aparición */var rv=qa('.rv');if('IntersectionObserver' in window){var io=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target)}})},{rootMargin:'0px 0px -8% 0px'});rv.forEach(function(e){io.observe(e)})}else rv.forEach(function(e){e.classList.add('in')});
/* recorrido solo (dentro de la propuesta): baja despacio, se para arriba y al tocar */
if(/[?&]tour=1/.test(location.search)&&!matchMedia('(prefers-reduced-motion: reduce)').matches){var y=0,hold=Date.now()+6000,stop=0,last=0,vis=true;
 addEventListener('message',function(m){if(m.data&&m.data.t404!=null)vis=!!m.data.t404});
 ['wheel','touchstart','pointerdown','keydown'].forEach(function(k){addEventListener(k,function(){stop=Date.now()+9000},{passive:true})});
 function st(ts){var dt=Math.min(64,ts-(last||ts));last=ts;var n=Date.now(),H=d.documentElement.scrollHeight-innerHeight;
  if(vis&&n>stop&&n>hold){if(y<1)y=scrollY;y+=dt*.06;if(y>=H-2){hold=n+2500;setTimeout(function(){scrollTo(0,0);y=0;hold=Date.now()+5500},2400);y=H}scrollTo(0,y)}else if(n<=stop)y=scrollY;requestAnimationFrame(st)}requestAnimationFrame(st)}
})();
"""


# titular del hero: qué vende la tienda, dicho claro (10/11). Si no está aquí, sale de sus tres categorías.
HX = {
    'amusko': 'Perfumes y cosmética<br>de autor.', 'antonio-martin-centro-optico': 'Gafas de sol<br>y graduadas.',
    'cache-vila': 'Punto, vestidos<br>y camisas.', 'calzados-carrillo': 'Botines, botas<br>y zapatillas.',
    'centro-optico-emperatriz': 'Gafas de sol<br>y graduadas.', 'intenso-fragancias': 'Perfumes y extractos<br>de autor.',
    'joyeria-benito-hidalgo': 'Relojes, anillos<br>y alianzas.', 'joyeria-coca': 'Medallas, pendientes<br>y collares.',
    'la-marquesa-perfumeria': 'Perfumes árabes<br>y de autor.', 'perfumeria-hebe': 'Perfumes, tratamiento<br>y maquillaje.',
    'perfumeria-paris': 'Perfumes, estuches<br>y bolsos.', 'perfumoon': 'Perfumes árabes<br>y de autor.',
    'rosa-rosae': 'Perfumes, bisutería<br>y cuidado.', 'scarpa': 'Abrigos, conjuntos<br>y bolsos.',
    'urban-fragance': 'Perfumes de autor<br>y regalos.',
}


def store(c):
    N = NICHE[c['niche']]; nm = E(c['name']); P_ = c['prods']; city = c['city']
    th = c.get('theme', {})
    col = {k: th.get(k, N[k]) for k in ('bg', 'surf', 'ink', 'mute', 'acc', 'on', 'line')}
    dark = c['niche'] == 'sneakers'
    root = (':root{--f:%s;--bg:%s;--surf:%s;--ink:%s;--mute:%s;--acc:%s;--on:%s;--line:%s;--hp:%s;--hpm:%s;--bp:%s;--bpm:%s}'
            % (FONT, col['bg'], col['surf'], col['ink'], col['mute'], col['acc'], col['on'], col['line'], c.get('hp', 'center'), c.get('hpm', '74% 45%'),
               c.get('bp', 'center'), c.get('bpm', c.get('bp', 'center'))))
    cls = ' '.join(x for x in ['up' if N['up'] else '', 'dark' if dark else ''] if x)
    cats = c['cats']  # [(nombre, id de imagen)] x3
    h1 = c.get('h1') or N['h1']
    o = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
         f'<meta name="robots" content="noindex,nofollow"><title>{nm} · Tienda online (ejemplo)</title><meta name="theme-color" content="{col["bg"]}">'
         f'<link rel="preload" as="image" href="{img(c, "h")}"><style>{root}{STORE_CSS}</style></head><body class="{cls}">')
    ann = [f'Envío a toda España', f'Recogida gratis en {city}', 'Paga con tarjeta, Bizum o Apple Pay']
    o += '<div class="ann">' + ''.join(f'<span{" class=on" if i == 0 else ""}>{E(t)}</span>' for i, t in enumerate(ann)) + '</div>'
    nav = ''.join(f'<a href="#cat" data-demo>{E(n)}</a>' for n, _ in cats)
    o += (f'<header class="hd"><div class="w"><nav class="nv"><a href="#nuevo" data-demo>Novedades</a>{nav}</nav>'
          f'<button class="mb" aria-label="Menú" data-demo>{ic("menu", 22)}</button><a class="lg" href="#" data-demo>{logo(c)}</a>'
          f'<div class="ia"><button class="hs" aria-label="Buscar" data-demo>{ic("search")}</button><button class="hs" aria-label="Cuenta" data-demo>{ic("user")}</button>'
          f'<button aria-label="Cesta" data-bag>{ic("bag", 22)}<span class="bq">0</span></button></div></div></header>')
    # hero (10/11: primero el producto. Qué venden se lee en el titular y se ve en las fotos de producto, también en el móvil)
    cn = [n for n, _ in cats]
    h1 = HX.get(c['slug']) or (E(cn[0]) + ', ' + E(cn[1].lower()) + '<br>y ' + E(cn[2].lower()) + '.')
    tiles = [('h', None)] + [(p['id'], p) for p in P_[:4]]
    def tile(i, p, k):
        if not p:
            return f'<div class="ht t{k}"><img src="{img(c, i)}" alt="{nm}" fetchpriority="high"><span class="tg">{E(city)}</span></div>'
        return (f'<div class="ht t{k}"><img src="{img(c, i)}" alt="{E(p["name"])}"{" fetchpriority=high" if k == 1 else ""}>'
                f'<div class="tl"><b>{E(p["name"])}</b><small>{"Lo más vendido" if k == 1 else price(c, p)}</small></div>'
                f'<button class="ta" data-add data-n="{E(p["name"])}" data-i="{img(c, i)}" data-p="{price(c, p)}" data-o="{E(p.get("opt", N["opts"][min(2, len(N["opts"]) - 1)]))}" aria-label="Añadir">{ic("plus", 18, 2)}</button></div>')
    sp = N['hero'] == 'split'
    if c.get('hd'):  # heroes nuevos de IA (10/11): 16:9 en el ordenador y 9:16 en el móvil
        o += (f'<section class="hero hz"><picture><source media="(max-width:900px)" srcset="{img(c, "hm")}"><img src="{img(c, "hd")}" alt="{nm}" fetchpriority="high"></picture>'
              f'<div class="w"><div class="hc"><span class="eb">{E(c.get("short", c["name"]))} · {E(city)}</span><h1>{HX.get(c["slug"]) or c.get("h1") or N["h1"]}</h1><p>{E(T(c.get("sub", N["sub"]), c))}</p>'
              f'<div class="hb"><a class="bt w1" href="#nuevo">{E(N["btn"])} {ic("arrow", 18, 2)}</a><a class="bt g1" href="#visita">Visítanos en {E(city)}</a></div></div></div></section>')
    elif c['niche'] in ('cosmetica', 'joya', 'optica') and not c.get('mosaic'):
        o += (f'<section class="hero{" sp" if sp else ""}"><img src="{img(c, "h")}" alt="{nm}" fetchpriority="high"><div class="w"><div class="hc">'
              f'<span class="eb">{E(c.get("short", c["name"]))} · {E(city)}</span><h1>{HX.get(c["slug"]) or c.get("h1") or N["h1"]}</h1><p>{E(T(c.get("sub", N["sub"]), c))}</p>'
              f'<div class="hb"><a class="bt w1" href="#nuevo">{E(N["btn"])} {ic("arrow", 18, 2)}</a><a class="bt g1" href="#visita">Visítanos en {E(city)}</a></div></div></div>'
              + ('' if sp else f'<div class="hm"><img src="{img(c, P_[0]["id"])}" alt=""><span>{E(P_[0]["name"])}<small>{price(c, P_[0])}</small></span></div>')
              + '</section>')
    else:
        o += (f'<section class="hx"' + (f' style="--hx:{c["hx"]}"' if c.get('hx') else '') + f'><div class="w hxg"><div class="hxt"><span class="eb">{E(c.get("short", c["name"]))} · {E(city)}</span><h1>{h1}</h1>'
              f'<p>{E(T(c.get("sub", N["sub"]), c))}</p>'
              f'<div class="hb"><a class="bt k" href="#nuevo">{E(N["btn"])} {ic("arrow", 18, 2)}</a><a class="bt o1" href="#visita">Visítanos en {E(city)}</a></div>'
              f'<div class="tr"><span>{ic("truck", 18)}Envío a toda España</span><span>{ic("store", 18)}Recogida en {E(city)}</span><span>{ic("card", 18)}Bizum y Apple Pay</span></div></div>'
              '<div class="hxm">' + ''.join(tile(i, p, k) for k, (i, p) in enumerate(tiles)) + '</div></div></section>')
    mq = [T(x, c) for x in N['marquee']]
    o += '<div class="mq"><div>' + ''.join(f'<span>{E(x)}</span>' for x in mq * 4) + '</div></div>'
    # categorías
    o += (f'<section class="sx" id="cat"><div class="w"><div class="sh rv"><h2>Compra por<br>categoría</h2><a href="#nuevo">Ver todo {ic("arrow", 16, 2)}</a></div><div class="cg">'
          + ''.join(f'<a class="ct rv" href="#nuevo"><img src="{img(c, i)}" alt="{E(n)}" loading="lazy"><div><b>{E(n)}</b><span>{ic("arrow", 18, 2)}</span></div></a>' for n, i in cats)
          + '</div></div></section>')
    # productos
    def card(p, k):
        return (f'<div class="pc rv"><div class="pi"><img src="{img(c, p["id"])}" alt="{E(p["name"])}" loading="lazy">'
                + (f'<span class="bd">{E(N["badge"])}</span>' if k in (0, 3) else '')
                + f'<button class="hr" aria-label="Favorito">{ic("heart", 18)}</button>'
                f'<button class="qa" data-add data-n="{E(p["name"])}" data-i="{img(c, p["id"])}" data-p="{price(c, p)}" data-o="{E(p.get("opt", N["opts"][min(2, len(N["opts"]) - 1)]))}">{ic("bag", 17)} Añadir</button></div>'
                f'<div class="pm"><b>{E(p["name"])}</b><span>{price(c, p)}</span></div></div>')
    o += (f'<section class="sx" id="nuevo" style="padding-top:0"><div class="w"><div class="sh rv"><h2>{E(N["grid_h"])}</h2><p>{E(N["grid_s"])}</p></div>'
          '<div class="pg">' + ''.join(card(p, k) for k, p in enumerate(P_[:6])) + '</div></div></section>')
    # banner
    o += (f'<section class="w"><div class="bn rv"><img src="{img(c, "b")}" alt="" loading="lazy"><div><small>{E(c.get("ban_e", N["ban_e"]))}</small>'
          f'<h3>{c.get("ban_h", N["ban_h"])}</h3><a class="bt w1" href="#destacado">{E(N["ban_b"])} {ic("arrow", 18, 2)}</a></div></div></section>')
    # destacado
    f0 = P_[0]
    o += (f'<section class="sx" id="destacado"><div class="w ft"><div class="fg rv"><img src="{img(c, f0["id"])}" alt="{E(f0["name"])}" loading="lazy">'
          f'<img src="{img(c, c.get("feat2", "l1"))}" alt="" loading="lazy"><img src="{img(c, c.get("feat3", P_[1]["id"]))}" alt="" loading="lazy"></div>'
          f'<div class="fi rv"><small>{E(N["feat_e"])}</small><h3>{E(f0["name"])}</h3><div class="pr">{price(c, f0)} <small>IVA incluido</small></div>'
          f'<p>{E(f0.get("desc") or "")}</p><div class="ol">{E(N["opts_l"])}</div><div class="os">'
          + ''.join(f'<button{" class=on" if k == min(2, len(N["opts"]) - 1) else ""}>{E(x)}</button>' for k, x in enumerate(f0.get('opts') or N['opts'])) + '</div>'
          f'<div class="fa"><button class="bt k" data-add data-n="{E(f0["name"])}" data-i="{img(c, f0["id"])}" data-p="{price(c, f0)}">Añadir a la cesta</button>'
          f'<button class="bt" style="border:1.5px solid var(--line);width:58px;padding:0;justify-content:center;flex:none" aria-label="Favorito" data-demo>{ic("heart", 20)}</button></div>'
          '<div class="py"><span>Tarjeta</span><span>Bizum</span><span>Apple Pay</span><span>Google Pay</span></div>'
          f'<div class="fl"><div>{ic("truck")}Envío a toda España</div><div>{ic("store")}Recogida gratis en {E(city)}</div></div></div></div></section>')
    # ventajas
    o += '<section class="w"><div class="us">' + ''.join(f'<div class="rv">{ic(i, 26)}<b>{E(T(a, c))}</b><p>{E(T(b, c))}</p></div>' for i, a, b in N['usp']) + '</div></section>'
    # visítanos
    addr = c.get('address') or ''
    maps = 'https://www.google.com/maps/search/' + urllib.parse.quote(f'{c["name"]} {addr} {city}')
    li = ''
    if addr:
        li += f'<li>{ic("pin")}<span>{E(addr)}<br>{E(c.get("cityfull", city))}</span></li>'
    else:
        li += f'<li>{ic("pin")}<span>{E(c.get("cityfull", city))}</span></li>'
    li += f'<li>{ic("insta")}<span>@{E(c["ig"])} · {c["fk"]} seguidores</span></li>'
    o += (f'<section class="sx" id="visita"><div class="w"><div class="vs rv"><img src="{img(c, c.get("visit", "l2"))}" alt="" loading="lazy"><div><small>Nuestra tienda</small>'
          f'<h3>{E(N["visit_h"])}</h3><ul>{li}</ul><a class="bt k" href="{maps}" target="_blank" rel="noopener" style="align-self:flex-start">Cómo llegar {ic("arrow", 18, 2)}</a></div></div></div></section>')
    # club
    o += (f'<section class="w"><div class="cl rv"><h3>{E(N["club"])}</h3><form><input type="email" placeholder="Tu email" aria-label="Tu email"><button>Unirme</button></form></div></section>')
    # pie
    o += (f'<footer class="fo"><div class="w"><div>{logo(c)}<p>{E(c.get("cityfull", city))}</p><p>@{E(c["ig"])}</p></div>'
          '<div><b>Tienda</b>' + ''.join(f'<a href="#cat" data-demo>{E(n)}</a>' for n, _ in cats) + '<a href="#nuevo">Novedades</a></div>'
          '<div><b>Ayuda</b><a href="#" data-demo>Envíos</a><a href="#" data-demo>Cambios y devoluciones</a><a href="#" data-demo>Contacto</a></div>'
          '<div><b>Pago seguro</b><p>Tarjeta · Bizum<br>Apple Pay · Google Pay</p></div></div>'
          f'<div class="fx"><span>© {nm}</span><span>Tienda de ejemplo hecha por 404 Growth. No es la web oficial.</span></div></footer>')
    o += (f'<div class="ov"></div><aside class="dr" aria-label="Cesta"><div class="dh"><b>Tu cesta</b><button data-close aria-label="Cerrar">{ic("x", 22)}</button></div>'
          '<div class="dl"></div><div class="df"><button class="bt k" data-pay>Finalizar compra</button><p>Envío a toda España · Recogida gratis en ' + E(city) + '</p></div></aside><div class="tz"></div>')
    o += f'<script>{STORE_JS}</script></body></html>'
    return o


# ---------------------------------------------------------------- la propuesta (igual para todas)
PROP_CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}html{-webkit-text-size-adjust:100%}
:root{--f:-apple-system,BlinkMacSystemFont,'SF Pro Display','SF Pro Text','Helvetica Neue',Inter,Arial,sans-serif;--bg:#0B0D0C;--ink:#F3F4F1;--mute:#A3A8A3;--line:rgba(243,244,241,.12);--mint:#7FD3B6;--lime:#D9F99D;--forest:#2E7A64;--cream:#F5F2EA;--k:#111311}
body{font-family:var(--f);background:var(--bg);color:var(--ink);-webkit-font-smoothing:antialiased;line-height:1.45;overflow-x:hidden}
a{color:inherit;text-decoration:none}img{display:block;max-width:100%}.ic{flex:none}
.wrap{max-width:1240px;margin:0 auto;padding:0 clamp(16px,3.6vw,40px)}
.g{background:linear-gradient(100deg,var(--mint),var(--forest));-webkit-background-clip:text;background-clip:text;color:transparent}
.cta{display:inline-flex;align-items:center;gap:10px;white-space:nowrap;height:54px;padding:0 26px;border-radius:99px;background:var(--lime);color:#0B0D0C;font-weight:680;font-size:15.5px;transition:transform .2s}
.cta:hover{transform:translateY(-2px)}.cta.gh{background:transparent;color:var(--ink);border:1.5px solid rgba(243,244,241,.35)}
.lt .cta.gh{color:var(--k);border-color:rgba(17,19,17,.25)}
/* nav */
.nav{position:fixed;top:14px;left:0;right:0;z-index:40;pointer-events:none}
.nav .wrap{display:flex;justify-content:space-between;align-items:center}
.pill{pointer-events:auto;display:flex;align-items:center;gap:22px;background:rgba(24,26,25,.86);border:1px solid var(--line);border-radius:99px;padding:7px 7px 7px 20px;backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px)}
.pill .br{font-weight:750;font-size:15px;letter-spacing:-.01em;white-space:nowrap}.pill .lk{display:flex;gap:20px;font-size:14px;color:var(--mute)}.pill .lk a:hover{color:var(--ink)}
.pill .cta{height:40px;padding:0 18px;font-size:14px;background:#fff}
/* hero */
.hero{padding:118px 0 0;position:relative;overflow:hidden}
.hero:before{content:"";position:absolute;inset:-10% -10% auto;height:80%;background:radial-gradient(60% 60% at 70% 30%,rgba(127,211,182,.22),transparent 70%),radial-gradient(40% 50% at 15% 10%,rgba(217,249,157,.12),transparent 70%);pointer-events:none}
.chip{display:inline-flex;align-items:center;gap:10px;background:rgba(243,244,241,.07);border:1px solid var(--line);border-radius:99px;padding:5px 14px 5px 5px;font-size:14px;color:var(--mute)}
.chip img{width:32px;height:32px;border-radius:50%;object-fit:cover}.chip b{color:var(--ink);font-weight:650}
.hero h1{font-size:clamp(48px,8.4vw,128px);line-height:.92;letter-spacing:-.045em;font-weight:800;margin:24px 0 0;max-width:12ch;text-wrap:balance}
.hl{display:grid;grid-template-columns:1fr auto;gap:40px;align-items:end;margin-top:26px}
.hl p{font-size:clamp(17px,1.5vw,20px);color:var(--mute);max-width:560px}.hl p b{color:var(--ink);font-weight:600}
.btns{display:flex;gap:10px;flex-wrap:wrap}
/* escenario: portátil + móvil con la tienda en vivo */
.stage{position:relative;margin:56px auto 0;max-width:1180px;padding:0 clamp(16px,3.6vw,40px)}
.lap{position:relative;width:86%;border-radius:16px 16px 0 0;background:#1c1e1d;padding:10px 10px 0;box-shadow:0 40px 120px rgba(0,0,0,.6),0 0 0 1px rgba(255,255,255,.08) inset}
.lap:after{content:"";position:absolute;left:-6%;right:-6%;bottom:-16px;height:16px;background:linear-gradient(#2a2c2b,#141615);border-radius:0 0 14px 14px}
.scr{position:relative;width:100%;aspect-ratio:16/10;overflow:hidden;border-radius:6px 6px 0 0;background:#fff}
.scr iframe{position:absolute;top:0;left:0;border:0;transform-origin:0 0;background:#fff}
.phn{position:absolute;right:clamp(16px,3.6vw,40px);bottom:-30px;width:23%;min-width:180px;max-width:280px;border-radius:44px;background:#0d0e0e;padding:10px;box-shadow:0 30px 80px rgba(0,0,0,.65),0 0 0 1.5px rgba(255,255,255,.14) inset}
.phn .scr{aspect-ratio:9/19.5;border-radius:34px}.phn:before{content:"";position:absolute;top:20px;left:50%;width:30%;height:22px;margin-left:-15%;background:#000;border-radius:20px;z-index:2}
.kp{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--line);margin-top:92px}
.kp div{padding:26px 22px 30px;border-right:1px solid var(--line)}.kp div:last-child{border-right:0}
.kp b{display:block;font-size:clamp(30px,3.4vw,46px);letter-spacing:-.035em;font-weight:760;line-height:1}.kp span{display:block;color:var(--mute);font-size:14.5px;margin-top:8px}
/* secciones */
.sec{padding:clamp(80px,10vw,140px) 0;position:relative}.lt{background:var(--cream);color:var(--k)}.lt .mu{color:#5f645f}
.chap{display:flex;gap:14px;align-items:center;font-size:13px;font-weight:650;letter-spacing:.16em;text-transform:uppercase;color:var(--mute);margin-bottom:22px}
.lt .chap{color:#6b706b}.chap i{font-style:normal;color:var(--mint)}.lt .chap i{color:var(--forest)}
.hd2{display:grid;grid-template-columns:1.2fr 1fr;gap:40px;align-items:end;margin-bottom:clamp(36px,5vw,60px)}
.hd2 h2{font-size:clamp(38px,4.8vw,72px);line-height:.95;letter-spacing:-.045em;font-weight:800;text-wrap:balance}.hd2 p{font-size:17.5px;color:var(--mute);max-width:480px}.lt .hd2 p{color:#5f645f}
/* navegador grande */
.bw{border-radius:18px;overflow:hidden;background:#fff;box-shadow:0 40px 100px rgba(0,0,0,.18),0 0 0 1px rgba(0,0,0,.08)}
.bb{height:44px;background:#EDEDEA;display:flex;align-items:center;gap:7px;padding:0 16px}.bb i{width:11px;height:11px;border-radius:50%;background:#D4D4CF}
.bb span{margin:0 auto;background:#fff;border-radius:8px;padding:5px 40px;font-size:12.5px;color:#666;max-width:60%;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.bw .scr{aspect-ratio:auto;height:min(78vh,820px);border-radius:0}
.bw .scr iframe{position:static;width:100%;height:100%;transform:none}
.tip{display:flex;gap:10px;align-items:center;justify-content:center;margin-top:18px;font-size:14.5px;color:#5f645f}
.row2{display:flex;justify-content:center;gap:12px;margin-top:30px;flex-wrap:wrap}
/* comparación */
.cmp{display:grid;gap:14px}
.rw{display:grid;grid-template-columns:200px 1fr;gap:20px;align-items:center;border:1px solid var(--line);border-radius:22px;padding:22px}
.rw.on{background:linear-gradient(100deg,rgba(127,211,182,.12),rgba(127,211,182,.02));border-color:rgba(127,211,182,.35)}
.rw .n b{display:block;font-size:54px;font-weight:800;letter-spacing:-.04em;line-height:1}.rw.on .n b{color:var(--mint)}.rw .n span{color:var(--mute);font-size:14px}
.st{display:flex;flex-wrap:wrap;gap:8px;align-items:center}.st span{background:rgba(243,244,241,.06);border:1px solid var(--line);border-radius:12px;padding:10px 14px;font-size:14.5px;font-weight:550}
.st span small{display:block;font-weight:450;color:var(--mute);font-size:12.5px}.st i{font-style:normal;color:var(--mute)}
.rw.on .st span{border-color:rgba(127,211,182,.3)}
.fx3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:14px}
.fx3 div{border:1px solid var(--line);border-radius:22px;padding:24px}.fx3 b{display:block;font-size:18px;margin:14px 0 6px;letter-spacing:-.01em}.fx3 p{color:var(--mute);font-size:15px}.fx3 svg{color:var(--mint)}
/* anuncios */
.adg{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.ad{background:#fff;color:#111;border-radius:18px;overflow:hidden;box-shadow:0 20px 60px rgba(0,0,0,.35)}
.ah{display:flex;align-items:center;gap:10px;padding:12px 14px;font-size:13.5px}.ah i{width:32px;height:32px;border-radius:50%;background:#111;color:#fff;display:grid;place-items:center;font-style:normal;font-weight:700;font-size:13px;overflow:hidden}
.ah i img{width:100%;height:100%;object-fit:contain;background:#fff}.ah b{font-weight:650}.ah small{display:block;color:#777;font-size:11.5px}
.am{position:relative;aspect-ratio:4/5;overflow:hidden;color:#fff}.am img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.am:after{content:"";position:absolute;inset:0;background:linear-gradient(0deg,rgba(0,0,0,.66),rgba(0,0,0,0) 55%)}
.am h6{position:absolute;left:20px;right:20px;bottom:22px;z-index:1;font-size:clamp(24px,2.3vw,32px);line-height:1;letter-spacing:-.03em;font-weight:800}
.af{display:flex;justify-content:space-between;align-items:center;padding:12px 14px;background:#F2F2F0;font-size:13.5px;font-weight:650}
.af span{background:#111;color:#fff;border-radius:8px;padding:7px 12px;font-size:12.5px}
.al{margin-top:14px;font-size:14.5px;color:var(--mute)}.al b{color:var(--ink);display:block;font-size:16px;margin-bottom:2px}
/* plan */
.ms{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;counter-reset:m}
.ms div{background:#fff;border-radius:22px;padding:26px 22px;border:1px solid rgba(17,19,17,.08)}
.ms small{font-size:12.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--forest)}.ms b{display:block;font-size:20px;letter-spacing:-.02em;margin:14px 0 6px}.ms p{color:#5f645f;font-size:15px}
.bar{position:relative;height:6px;background:rgba(17,19,17,.08);border-radius:6px;margin:0 0 22px;overflow:hidden}.bar i{position:absolute;inset:0;width:0;background:linear-gradient(90deg,var(--mint),var(--forest));border-radius:6px;transition:width 2.2s cubic-bezier(.2,.7,.2,1)}
.in .bar i{width:100%}
.inc{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px;align-items:center}.inc>span{font-weight:700;margin-right:6px}
.inc em{font-style:normal;display:inline-flex;gap:8px;align-items:center;background:#fff;border:1px solid rgba(17,19,17,.08);border-radius:99px;padding:10px 16px;font-size:14.5px;font-weight:550}.inc svg{color:var(--forest)}
.pr3{margin-top:22px;color:#5f645f;font-size:15px}
/* cierre */
.close{padding:clamp(90px,12vw,160px) 0;position:relative;overflow:hidden;isolation:isolate}
.close>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:-2;opacity:.9}
.close:after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(180deg,rgba(11,13,12,.55),rgba(11,13,12,.92) 75%)}
.close h2{font-size:clamp(46px,7.6vw,116px);line-height:.92;letter-spacing:-.045em;font-weight:800;max-width:13ch;text-wrap:balance}
.cn{display:flex;gap:16px;align-items:center;margin:34px 0 28px;max-width:560px}.cn img{width:62px;height:62px;border-radius:50%;object-fit:cover;flex:none}.cn p{font-size:17px;color:#d6d9d5}
footer{padding:30px 0 120px;color:var(--mute);font-size:13px}footer .wrap{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}
.wa-fab{position:fixed;right:18px;bottom:18px;z-index:50;display:flex;align-items:center;gap:10px;background:#fff;color:#111;border-radius:99px;padding:6px 18px 6px 6px;box-shadow:0 14px 40px rgba(0,0,0,.35);transform:translateY(120px);transition:transform .4s cubic-bezier(.2,.8,.2,1);font-weight:650;font-size:14.5px}
.wa-fab.on{transform:none}.wa-fab img{width:42px;height:42px;border-radius:50%;object-fit:cover}.wa-fab small{display:block;font-weight:450;color:#666;font-size:12px}
.rv{opacity:0;transform:translateY(24px);transition:opacity .8s,transform .8s cubic-bezier(.2,.7,.2,1)}.rv.in{opacity:1;transform:none}
@media (max-width:900px){
 .pill .lk{display:none}.pill{padding-left:16px;gap:12px}
 .hero{padding-top:96px}.hero h1{font-size:clamp(44px,13vw,70px)}.hl{grid-template-columns:1fr;gap:22px}.btns .cta{flex:1;justify-content:center;padding:0 12px;font-size:14.5px;gap:6px}
 .stage{margin-top:40px}.lap{display:none}.phn{position:relative;right:auto;bottom:auto;width:min(78vw,320px);max-width:none;margin:0 auto}
 .kp{grid-template-columns:1fr 1fr;margin-top:44px}.kp div:nth-child(2){border-right:0}.kp div:nth-child(-n+2){border-bottom:1px solid var(--line)}.kp div{padding:20px 16px}
 .hd2{grid-template-columns:1fr;gap:16px}.bw .scr{height:72vh}.bw.d{display:none}.mobshop{display:block!important}
 .rw{grid-template-columns:1fr;gap:12px;padding:18px}.rw .n{display:flex;gap:12px;align-items:baseline}.rw .n b{font-size:40px}.fx3{grid-template-columns:1fr}
 .adg{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;gap:12px;margin:0 -16px;padding:0 16px 10px;scrollbar-width:none}.adg::-webkit-scrollbar{display:none}.adg>div{flex:0 0 78%;scroll-snap-align:center}
 .ms{grid-template-columns:1fr 1fr}.ms div{padding:20px 16px}.ms b{font-size:17px}
}
@media (max-width:520px){.ms{grid-template-columns:1fr}}
.mobshop{display:none}.mobshop .phn{position:relative;right:auto;bottom:auto;margin:0 auto;width:min(84vw,360px)}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}.rv{opacity:1;transform:none}}
"""

PROP_JS = r"""
(function(){var d=document,qa=function(s){return [].slice.call(d.querySelectorAll(s))};
/* iframes escalados: la tienda se dibuja a 1440 (portátil) o 390 (móvil) y se encoge a su marco */
function fit(){qa('.scr[data-w] iframe').forEach(function(f){var s=f.parentNode,W=+s.dataset.w,k=s.clientWidth/W;f.style.width=W+'px';f.style.height=(s.clientHeight/k)+'px';f.style.transform='scale('+k+')'})}
addEventListener('resize',fit);fit();
/* los iframes del inicio solo cargan y se mueven cuando se ven */
var io2=new IntersectionObserver(function(en){en.forEach(function(x){var f=x.target;if(x.isIntersecting&&!f.src)f.src=f.dataset.src;try{f.contentWindow.postMessage({t404:x.isIntersecting},'*')}catch(e){}})},{rootMargin:'200px'});
qa('iframe[data-src]').forEach(function(f){io2.observe(f)});
var rv=qa('.rv');var io=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target)}})},{rootMargin:'0px 0px -10% 0px'});rv.forEach(function(e){io.observe(e)});
var b=d.querySelector('.wa-fab');function f(){b.classList.toggle('on',scrollY>700)}addEventListener('scroll',f,{passive:true});f();
})();
"""

FLOW_TODAY = {
    'moda': [('Ve la prenda', 'en Instagram'), ('Escribe por DM', 'o WhatsApp'), ('Pregunta talla y precio', 'y espera respuesta'), ('Bizum o transferencia', 'a mano'), ('Envío', 'coordinado a mano')],
    'joya': [('Ve la pieza', 'en Instagram'), ('Escribe por DM', 'o WhatsApp'), ('Pregunta precio y acabado', 'y espera respuesta'), ('Bizum o transferencia', 'a mano'), ('Envío', 'coordinado a mano')],
    'cosmetica': [('Ve el producto', 'en Instagram'), ('Escribe por DM', 'o WhatsApp'), ('Pregunta precio y stock', 'y espera respuesta'), ('Bizum o transferencia', 'a mano'), ('Envío', 'coordinado a mano')],
    'sneakers': [('Ve el par', 'en Instagram'), ('Escribe por DM', 'o WhatsApp'), ('Pregunta talla y precio', 'y espera respuesta'), ('Bizum o transferencia', 'a mano'), ('Envío', 'coordinado a mano')],
    'calzado': [('Ve el par', 'en Instagram'), ('Escribe por DM', 'o WhatsApp'), ('Pregunta talla y precio', 'y espera respuesta'), ('Bizum o transferencia', 'a mano'), ('Envío', 'coordinado a mano')],
    'optica': [('Ve la montura', 'en Instagram'), ('Escribe o llama', 'para preguntar'), ('Pregunta precio y modelo', 'y espera respuesta'), ('Va a la óptica', 'en horario de tienda'), ('Pide cita', 'por teléfono')],
}
FLOW_NEW = {
    'optica': [('Ve la montura', 'en Instagram o Google'), ('Ficha con precio', 'y fotos'), ('Compra o reserva cita', 'en un minuto')],
}


def proposal(c):
    N = NICHE[c['niche']]; nm = E(c['name']); sh = E(c.get('short', c['name'])); s = c['slug']; city = E(c['city'])
    tienda = f'/p-{s}--tienda'
    o = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
         '<meta name="robots" content="noindex,nofollow">'
         f'<title>{nm} × 404 Growth · Vuestra tienda online</title><meta name="description" content="Así se vería la tienda online de {nm}, con vuestras {E(N["items"])}, lista para vender en toda España.">'
         f'<meta property="og:type" content="website"><meta property="og:site_name" content="404 Growth"><meta property="og:title" content="{nm} × 404 Growth · Vuestra tienda online">'
         f'<meta property="og:description" content="Así se vería vuestra tienda online. Abierta 24 horas, para toda España."><meta property="og:image" content="https://404growth.com/p-{s}--b--og.jpg">'
         '<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">'
         f'<link rel="icon" href="/favicon.svg" type="image/svg+xml"><style>{PROP_CSS}</style></head><body>')
    o += (f'<div class="nav"><div class="wrap"><div class="pill"><span class="br">{nm}</span><div class="lk"><a href="#tienda">Tienda</a><a href="#hoy">Hoy</a><a href="#anuncios">Anuncios</a><a href="#plan">Plan</a></div>'
          f'<a class="cta" href="{wa(c)}" target="_blank" rel="noopener">Hablamos</a></div></div></div>')
    kp = [(c['fk'], f'seguidores en Instagram'), ('24/7', 'abierta, también de noche'), ('15 días', 'para tenerla vendiendo'), ('España', f'entera, no solo {city}')]
    o += (f'<header class="hero" id="inicio"><div class="wrap"><span class="chip"><img src="/christian-hola.jpg" alt="Christian" width="32" height="32"><span><b>Christian</b> · propuesta para {sh}</span></span>'
          f'<h1>{sh},<br><span class="g">abierta 24&nbsp;horas.</span></h1>'
          f'<div class="hl"><p>Así se vería <b>vuestra tienda online</b>, hecha con vuestras {E(N["items"])}. Tocadla: funciona, tiene cesta y se ve igual de bien en el móvil.</p>'
          f'<div class="btns"><a class="cta" href="{wa(c)}" target="_blank" rel="noopener">Quiero mi tienda {ic("arrow", 18, 2)}</a><a class="cta gh" href="{BOOK}{s}&amp;utm_content=cta-2" target="_blank" rel="noopener">Reservar 30 min</a></div></div></div>'
          f'<div class="stage"><div class="lap"><div class="scr" data-w="1440"><iframe data-src="{tienda}?tour=1" title="Tienda de {nm} en el ordenador" loading="lazy" tabindex="-1"></iframe></div></div>'
          f'<div class="phn"><div class="scr" data-w="390"><iframe data-src="{tienda}?tour=1" title="Tienda de {nm} en el móvil" loading="lazy" tabindex="-1"></iframe></div></div></div>'
          '<div class="wrap"><div class="kp">' + ''.join(f'<div class="rv"><b>{E(a)}</b><span>{b}</span></div>' for a, b in kp) + '</div></div></header>')
    # 01 tienda en grande, interactiva
    o += (f'<section class="sec lt" id="tienda"><div class="wrap"><div class="chap"><i>01</i>La tienda</div>'
          f'<div class="hd2 rv"><h2>Así se vería {nm} online.</h2><p>Con vuestras {E(N["items"])}, vuestra marca y vuestra tienda de {city}. Bajad, añadid algo a la cesta, abrid la ficha: es la tienda de verdad.</p></div>'
          f'<div class="bw d rv"><div class="bb"><i></i><i></i><i></i><span>{E(c.get("domain", s.replace("-", "") + ".es"))}</span></div><div class="scr"><iframe data-src="{tienda}?embed=1" title="Tienda de {nm}"></iframe></div></div>'
          f'<div class="mobshop"><div class="phn"><div class="scr" data-w="390"><iframe data-src="{tienda}?embed=1" title="Tienda de {nm} en el móvil"></iframe></div></div></div>'
          f'<p class="tip">{ic("spark", 18)} Fotos hechas con IA a partir de vuestros productos reales de Instagram.</p>'
          f'<div class="row2"><a class="cta" style="background:#111;color:#fff" href="{wa(c)}" target="_blank" rel="noopener">Quiero esta tienda para {sh} {ic("arrow", 18, 2)}</a>'
          f'<a class="cta gh" href="{tienda}" target="_blank" rel="noopener">Abrir a pantalla completa</a></div></div></section>')
    # 02 hoy frente a la tienda
    today = FLOW_TODAY[c['niche']]
    new = FLOW_NEW.get(c['niche'], [('Ve la ' + N['item'] if N['item'] in ('prenda', 'pieza', 'montura') else 'Ve el ' + N['item'], 'en Instagram o Google'), ('Elige ' + N['opts_l'].lower(), 'en la ficha'), ('Paga', 'con Bizum o Apple Pay')])
    row = lambda st: '<i>›</i>'.join(f'<span>{E(a)}<small>{E(b)}</small></span>' for a, b in st)
    web = c.get('web_note') or 'Hoy no tenéis tienda online: quien os encuentra fuera de ' + city + ' solo puede escribiros.'
    o += (f'<section class="sec" id="hoy"><div class="wrap"><div class="chap"><i>02</i>Cómo os compran hoy</div>'
          f'<div class="hd2 rv"><h2>Cada mensaje es una venta que espera.</h2><p>{E(web)}</p></div><div class="cmp">'
          f'<div class="rw rv"><div class="n"><b>{len(today)}</b><span>pasos para comprar hoy</span></div><div class="st">{row(today)}</div></div>'
          f'<div class="rw on rv"><div class="n"><b>{len(new)}</b><span>con vuestra tienda</span></div><div class="st">{row(new)}</div></div></div>'
          '<div class="fx3">'
          f'<div class="rv">{ic("clock", 26)}<b>Vende mientras dormís</b><p>Un pedido a las 23:47 no espera a que abráis por la mañana.</p></div>'
          f'<div class="rv">{ic("truck", 26)}<b>Toda España, no solo {city}</b><p>Vuestros {c["fk"]} seguidores no viven todos cerca de la tienda.</p></div>'
          f'<div class="rv">{ic("chat", 26)}<b>Menos «¿precio?» por DM</b><p>Precio, tallas y stock en la ficha. Vosotros atendéis lo que de verdad necesita una persona.</p></div>'
          '</div></div></section>')
    # 03 anuncios
    ah = [T(x, c) for x in N['ad_h']]
    av = f'<img src="/p-{s}--b--logo.png" alt="">' if (c.get('logo') or {}).get('img') else E(c['name'][0].upper())
    ads = [('h', ah[0], 'Comprar ahora', 'Captación', f'Personas de toda España a las que les encaja {nm}.'),
           (c.get('ad2', 'p2'), ah[1], 'Comprar ahora', 'Recuperar', 'Quien vio vuestras fotos o entró en la tienda y no compró.'),
           (c.get('ad3', 'l1'), ah[2], 'Ver colección', 'Novedades', 'Cada novedad, delante de vuestros seguidores y de gente parecida.')]
    o += (f'<section class="sec" id="anuncios" style="padding-top:0"><div class="wrap"><div class="chap"><i>03</i>Anuncios</div>'
          f'<div class="hd2 rv"><h2>Y gente nueva entrando cada día.</h2><p>Anuncios en Instagram y Facebook hechos con vuestras fotos, que llevan directos a la ficha. Medimos cada venta.</p></div><div class="adg">'
          + ''.join(f'<div class="rv"><div class="ad"><div class="ah"><i>{av}</i><span><b>{E(c["ig"])}</b><small>Publicidad</small></span></div><div class="am"><img src="{img(c, i)}" alt="" loading="lazy"><h6>{h}</h6></div>'
                    f'<div class="af">{E(c.get("domain", s.replace("-", "") + ".es"))}<span>{E(btn)}</span></div></div><p class="al"><b>{E(t)}</b>{E(d_)}</p></div>' for i, h, btn, t, d_ in ads)
          + '</div></div></section>')
    # 04 plan
    ms = [('Día 0', 'Llamada de arranque', 'Nos contáis cómo funciona la tienda y preparamos los accesos.'),
          ('Días 1–10', 'Diseño y catálogo', f'Vuestra marca, vuestras fotos y las primeras {N["items"]} subidas.'),
          ('Días 8–14', 'Pagos, envíos y prueba', 'Tarjeta, Bizum, envíos, stock y un pedido de prueba real.'),
          ('Día 15', 'Abierta', 'Tienda online vendiendo y anuncios en marcha.')]
    inc = [('store', 'Tienda online propia'), ('card', 'Tarjeta, Bizum y Apple Pay'), ('box', 'Stock unido con la tienda física'),
           ('insta', 'Instagram Shopping'), ('spark', 'Anuncios en Meta'), ('chart', 'Medición de cada venta')]
    o += ('<section class="sec lt" id="plan"><div class="wrap"><div class="chap"><i>04</i>El plan</div>'
          '<div class="hd2 rv"><h2>En 15 días, vendiendo online.</h2><p>Lo montamos nosotros, con vosotros, mientras la tienda sigue abierta como siempre.</p></div>'
          '<div class="rv"><div class="bar"><i></i></div></div><div class="ms">' + ''.join(f'<div class="rv"><small>{a}</small><b>{E(b)}</b><p>{E(p)}</p></div>' for a, b, p in ms) + '</div>'
          '<div class="inc rv"><span>Incluye</span>' + ''.join(f'<em>{ic(i, 18)}{E(t)}</em>' for i, t in inc) + '</div>'
          '<p class="pr3 rv">Precio cerrado, sin sorpresas. Os lo damos en la llamada, con vuestro catálogo delante.</p>'
          f'<div class="row2" style="justify-content:flex-start"><a class="cta" style="background:#111;color:#fff" href="{BOOK}{s}&amp;utm_content=cta-7" target="_blank" rel="noopener">Reservar la llamada · 30 min {ic("arrow", 18, 2)}</a></div></div></section>')
    o += (f'<section class="close" id="hablar"><img src="{img(c, "b")}" alt="" loading="lazy"><div class="wrap"><div class="chap"><i>→</i>Siguiente paso</div>'
          f'<h2>¿Abrimos {sh} <span class="g">a toda España?</span></h2>'
          '<div class="cn"><img src="/christian-hola.jpg" alt="Christian" width="62" height="62"><p>Soy Christian. Os enseño esta tienda en 30 minutos, con vuestro catálogo y en directo.</p></div>'
          f'<div class="btns"><a class="cta" href="{wa(c)}" target="_blank" rel="noopener">Escribidme por WhatsApp {ic("arrow", 18, 2)}</a>'
          f'<a class="cta gh" href="{BOOK}{s}&amp;utm_content=cta-8" target="_blank" rel="noopener">Reservar videollamada</a></div></div></section>'
          f'<footer><div class="wrap"><span>Demo de concepto de 404 Growth. No es la web oficial.</span><span>Marca y productos: {nm} · @{E(c["ig"])}. Fotos creadas con IA a partir de sus productos reales.</span></div></footer>'
          f'<a class="wa-fab" href="{wa(c)}" target="_blank" rel="noopener"><img src="/christian-hola.jpg" alt="" width="42" height="42"><span>Escribir a Christian<small>por WhatsApp</small></span></a>')
    cnt = open(os.path.join(D, 'tpl', 'counter.html'), encoding='utf-8').read()
    cnt = re.sub(r'var slug="[^"]*"', f'var slug="{s}"', cnt)
    cnt = re.sub(r'PARTS=\[.*?\]\]', 'PARTS=[["tienda",3],["hoy",4],["anuncios",5],["plan",8],["hablar",9]]', cnt)
    assert f'var slug="{s}"' in cnt and '["hoy",4]' in cnt
    o += f'<script>{PROP_JS}</script>{cnt}</body></html>'
    return o


# ---------------------------------------------------------------- imágenes y salida
SIZE = {'h': 2400, 'b': 2000, 'hd': 2400, 'hm': 1400}


def images(c):
    s = c['slug']; src = os.path.join(AI, s)
    for i in IDS:
        f = os.path.join(src, i + '.jpg')
        if not os.path.exists(f):
            if i not in ('hd', 'hm'):
                print('  falta', s, i)
            continue
        im = Image.open(f).convert('RGB'); mx = SIZE.get(i, 1100)
        if max(im.size) > mx:
            im.thumbnail((mx, mx), Image.LANCZOS)
        im.save(os.path.join(OUT, f'p-{s}--b--{i}.jpg'), 'JPEG', quality=84, optimize=True, progressive=True)
    f = os.path.join(src, 'h.jpg')
    if os.path.exists(f):
        im = Image.open(f).convert('RGB'); w, h = im.size; r = 1200 / 630
        cw, ch = (w, int(w / r)) if w / h < r else (int(h * r), h)
        x0 = int((w - cw) * c.get('og_fx', .5)); y0 = (h - ch) // 2
        im.crop((x0, y0, x0 + cw, y0 + ch)).resize((1200, 630), Image.LANCZOS).save(os.path.join(OUT, f'p-{s}--b--og.jpg'), 'JPEG', quality=86, optimize=True)
    lg = os.path.join(src, 'logo.png')
    if (c.get('logo') or {}).get('img') and os.path.exists(lg):
        Image.open(lg).save(os.path.join(OUT, f'p-{s}--b--logo.png'), optimize=True)


def fk(n):
    return f'{n / 1000:.1f}'.replace('.0', '').replace('.', ',') + 'K' if n >= 1000 else str(n)


def load(slug):
    c = json.load(open(os.path.join(D, 'data', slug + '.json'), encoding='utf-8'))
    c['slug'] = slug
    c.setdefault('fk', fk(c['f']))
    c['hd'] = all(os.path.exists(os.path.join(AI, slug, i + '.jpg')) for i in ('hd', 'hm'))
    return c


def build(slug, imgs=True):
    c = load(slug); os.makedirs(OUT, exist_ok=True)
    if imgs:
        images(c)
    a = store(c); b = proposal(c)
    open(os.path.join(OUT, f'p-{slug}--tienda.html'), 'w', encoding='utf-8').write(a)
    open(os.path.join(OUT, f'p-{slug}.html'), 'w', encoding='utf-8').write(b)
    for h in (a, b):
        txt = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', h, flags=re.S)
        assert not re.findall(r'\{[a-z_]+\}', txt), re.findall(r'\{[a-z_]+\}', txt)[:3]
    print('ok', slug, len(a), len(b))


if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if not x.startswith('-')]
    for s in a:
        build(s, '--noimg' not in sys.argv)
