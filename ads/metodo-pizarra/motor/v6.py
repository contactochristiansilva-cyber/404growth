from common import *

def mk(id, x, y, n):
    return f'<div class="abs" id="{id}" data-fx="pop" style="left:{x}px;top:{y}px;width:34px;height:34px;border-radius:50%;background:var(--red);color:#fff;display:grid;place-items:center;font-size:17px;font-weight:700;box-shadow:0 0 0 3px #fff,0 6px 14px -4px rgba(194,81,58,.6);z-index:4">{n}</div>'

def badweb():
    tile = '<div style="border-radius:8px;background:#ECEBE8;height:96px"></div><div style="font-size:12px;color:#8A8E8A;margin-top:6px">Consultar precio</div>'
    return ('<div class="abs" style="left:0;right:0;top:40px;height:44px;display:flex;align-items:center;justify-content:center;font-family:Georgia,serif;font-size:17px;letter-spacing:.2em;color:#555">TU TIENDA</div>'
            '<div class="abs" style="left:14px;right:14px;top:92px;height:110px;border-radius:10px;background:#E4E2DD;display:grid;place-items:center;font-family:Georgia,serif;font-size:22px;color:#777">¡Bienvenidos!</div>'
            f'<div class="abs" style="left:14px;right:14px;top:216px;display:grid;grid-template-columns:1fr 1fr;gap:10px 10px"><div>{tile}</div><div>{tile}</div><div>{tile}</div><div>{tile}</div></div>'
            '<div class="abs" style="left:14px;right:14px;top:494px;height:46px;border-radius:10px;border:1.5px solid #BDBAB3;display:grid;place-items:center;font-size:14px;color:#555">Llámanos para comprar</div>'
            '<div class="abs" style="left:14px;right:14px;top:552px;font-size:11px;color:#8A8E8A;text-align:center">Pago por transferencia</div>'
            '<div class="abs" id="a3s" style="left:0;top:0;right:0;bottom:0;background:rgba(255,255,255,.72);display:grid;place-items:center;opacity:0"><div style="display:flex;flex-direction:column;align-items:center;gap:10px;color:#6E736F;font-size:14px"><i style="width:36px;height:36px;border-radius:50%;border:4px solid #DDD;border-top-color:#888"></i>Cargando…</div></div>')

def goodweb():
    return (f'<div class="abs" style="left:0;top:40px;width:278px;height:250px;background:#F3E7DA;display:grid;place-items:center">{bag(170)}</div>'
            '<div class="abs" style="left:16px;top:302px;font-size:18px;font-weight:600">Bolso de piel</div>'
            '<div class="abs tn" style="left:16px;top:330px;font-size:24px;font-weight:700">129 €</div>'
            '<div class="abs" style="left:16px;top:374px;display:flex;gap:8px">' + ''.join(f'<span style="font-size:13px;font-weight:600;padding:6px 11px;border-radius:8px;border:1.5px solid {"#16191A" if k=="M" else "#DDD"}">{k}</span>' for k in 'SML') + '</div>'
            '<div class="abs btn" style="left:16px;top:470px;width:246px;height:50px;font-size:17px">Comprar</div>'
            '<div class="abs" style="left:16px;top:532px;right:16px;display:flex;gap:6px;justify-content:center">' + ''.join(f'<span style="font-size:11px;font-weight:600;padding:5px 8px;border-radius:6px;background:#F3F2EE">{k}</span>' for k in ['Bizum', 'Apple Pay', 'Tarjeta']) + '</div>')

def v6():
    PX, PY = 70, 196
    iss = [('a1', 'No se puede comprar', 'es un escaparate'), ('a2', 'Precio y talla, escondidos', 'quien tiene que preguntar, se va'),
           ('a3', 'Lenta en el móvil', 'y ahí está casi todo el mundo'), ('a4', 'Pagar es un lío', 'transferencia o formulario'), ('a5', 'Nadie la empuja', 'sin anuncios, Instagram ni emails')]
    lst = ''.join(f'<div class="row" id="{i}" data-fx="row" style="height:118px;font-size:25px"><b style="flex:none;width:34px;height:34px;border-radius:50%;background:var(--red);color:#fff;display:grid;place-items:center;font-size:17px">{n+1}</b><span class="rt" style="font-weight:600">{t}<span class="rs" style="font-weight:400">{s}</span></span></div>' for n, (i, t, s) in enumerate(iss))
    A = (kick('TU WEB, HOY') + h2('Cómo la ve un cliente', size=54) + phone('pa', PX, PY, badweb(), w=300, h=620) +
         mk('a1m', PX + 252, PY + 500, 1) + mk('a2m', PX + 252, PY + 300, 2) + mk('a3m', PX + 252, PY + 60, 3) + mk('a4m', PX + 252, PY + 560, 4) +
         f'<div class="abs" id="a5m" data-fx="pop" style="left:{PX+40}px;top:{PY+640}px;display:flex;align-items:center;gap:10px"><b style="width:34px;height:34px;border-radius:50%;background:var(--red);color:#fff;display:grid;place-items:center;font-size:17px">5</b><span class="chip">0 visitas hoy</span></div>' +
         f'<div class="abs" style="left:420px;top:196px;width:524px">{lst}</div>')
    A = A.replace('id="a3s" style="', 'id="a3s" data-fx="fade" data-outf="a4-0.2" style="')
    fx = [('b1', 'Botón de compra en cada producto'), ('b2', 'Precio y talla a la vista'), ('b3', 'Rápida en el móvil'), ('b4', 'Bizum, Apple Pay y tarjeta'), ('b5', 'La captación en marcha', 'anuncios, Instagram y email')]
    rows = ''.join(lrow(r[0], r[1], sub=(r[2] if len(r) > 2 else ''), h=100, fs=28).replace('class="row"', 'class="row" data-fx="row"') for r in fx)
    B = kick('CÓMO SE ARREGLA') + h2('Las cinco, resueltas') + card('bl', 56, 196, 888, 540, f'<div style="padding:10px 30px">{rows}</div>')
    C = (kick('ANTES Y DESPUÉS') + h2('La misma tienda') +
         ab('c1l', 90, 196, '<div style="font-size:17px;font-weight:600;letter-spacing:.12em" class="red">ANTES</div>') +
         ab('c2l', 600, 196, '<div style="font-size:17px;font-weight:600;letter-spacing:.12em" class="grn">DESPUÉS</div>') +
         phone('c1', 90, 236, badweb().replace('id="a3s"', 'id="x3s"'), w=300, h=620, extra='filter:grayscale(1);') +
         phone('c2', 600, 236, goodweb(), w=300, h=620) +
         svg(arr('c2a', [(420, 546), (570, 546)], w=4, col='#2E7A64')))
    C = C.replace('class="phone" id="c1"', 'class="phone" id="c1" data-fx="up"').replace('class="phone" id="c2"', 'class="phone" id="c2" data-fx="up"')
    res = ('<div style="padding:26px 30px"><div style="font-size:15px;color:#3B6E2F">tutienda.es › bolsos</div>'
           '<div style="font-size:26px;color:#1A47A8;margin-top:6px;letter-spacing:-.01em">Bolsos de piel hechos a mano | Tu Tienda</div>'
           '<div style="font-size:17px;color:var(--mute);margin-top:8px;line-height:1.45">Bolsos de piel en varios colores. Envío a toda España…</div></div>')
    D = (kick('¿Y LO QUE YA TIENES?') + h2('Lo que ya tienes en Google', size=54) +
         card('d0', 56, 196, 888, 74, f'<div style="height:100%;display:flex;align-items:center;gap:14px;padding:0 24px;font-size:20px;color:#3B403D">{ic("search",22)}bolsos de piel tu tienda</div>', extra='border-radius:99px') +
         card('d1', 56, 300, 888, 170, res) +
         ab('d2', 56, 520, f'<div style="display:flex;align-items:center;gap:16px"><span class="chip" style="font-size:19px;padding:12px 18px">{ic("store",20)}Tu dominio de siempre</span><span class="grn">{ic("arrow",28,2.2)}</span><span class="chip" style="font-size:19px;padding:12px 18px;background:#E6F4EE;color:var(--g2)">Tu tienda nueva</span></div>') +
         ab('d3', 56, 610, '<div style="display:flex;gap:12px;align-items:center;font-size:19px;color:#3B403D"><code style="font-family:inherit;padding:8px 12px;border-radius:8px;background:#F3F2EE">/bolsos</code><span class="grn">→</span><code style="font-family:inherit;padding:8px 12px;border-radius:8px;background:#E6F4EE;color:var(--g2)">/bolsos-de-piel</code><span class="mut" style="margin-left:6px">redirigida</span></div>') +
         ab('d4', 56, 720, '<div class="big" style="font-size:50px">No pierdes <span class="gt" style="font-weight:400">lo que ya tienes</span>.</div>'))
    N = nextframe('N', 600, 2360, 'Se arregla', 'Comprar, precio, rápida, pago y visitas', '', 7, '¿Qué pasa después del día 15?')
    N = N.replace('<div class="v" style="font-size:40px">Comprar, precio, rápida, pago y visitas</div>', '<div class="v" style="font-size:28px;line-height:1.15">Comprar, precio, rápida, pago y visitas</div>')
    frames = [('A', frame('A', 0, 0, 'Tu web, hoy', A)), ('B', frame('B', 1200, 0, 'Cómo se arregla', B)),
              ('C', frame('C', 0, 1180, 'Antes y después', C)), ('D', frame('D', 1200, 1180, 'Google', D)), ('N', N)]
    lines = [
     'Mira tu web como la ve un cliente desde el móvil.',
     '{@A} Uno: {a1,a1m} no se puede comprar. Es un escaparate: «llámanos» o «escríbenos».',
     'Dos: {a2,a2m} el precio y la talla, escondidos. Y quien tiene que preguntar, se va.',
     'Tres: {a3,a3m,a3s+.2} tarda en cargar en el móvil. Y el móvil es desde donde entra casi todo el mundo.',
     'Cuatro: {a4,a4m} pagar es un lío. Una transferencia, o un formulario.',
     'Cinco: {a5,a5m} aunque estuviera perfecta, nadie la empuja. Sin anuncios, sin Instagram, sin emails.',
     '{@B} Cómo se arregla: {b1} botón de compra en cada producto. {b2} Precio y talla a la vista. {b3} Rápida en el móvil. {b4} Bizum, Apple Pay y tarjeta. {b5} Y la captación en marcha.',
     '{@C} {c1l,c1} Esta es la de antes. {c2a,c2l+.3,c2+.4} Y esta, la de después.',
     '{@D} ¿Y lo que ya tienes en Google? {d0,d1+.3} No se pierde. {d2} La rehacemos en tu dominio {d3} y redirigimos las direcciones antiguas. {d4}',
     '{@ALL} ¿Y qué pasa cuando ya está abierta? {@N} Eso, en el vídeo 7. {nrec} {>>play}',
    ]
    return 6, '¿Por qué tu web no vende?', frames, lines

if __name__ == '__main__':
    import sys
    n, title, frames, lines = v6()
    print(build(n, title, frames, lines, sys.argv[1])['dur'])
