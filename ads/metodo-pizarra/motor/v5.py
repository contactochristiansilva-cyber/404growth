from common import *

def v5():
    # A · el precio
    def fac(id, x, icon, t, s):
        return (f'<div class="card" id="{id}" style="left:{x}px;top:200px;width:272px;height:180px;padding:24px">'
                f'<i class="ni g" style="width:52px;height:52px;border-radius:14px;display:grid;place-items:center">{ic(icon,26)}</i>'
                f'<div style="font-size:24px;font-weight:600;letter-spacing:-.02em;margin-top:16px">{t}</div><div style="font-size:18px;color:var(--mute);margin-top:4px">{s}</div></div>')
    A = (kick('EL PRECIO') + h2('Depende de tres cosas') +
         fac('a1', 56, 'box', 'Productos', '¿cuántos tienes?') + fac('a2', 364, 'store', 'Tu TPV', '¿lo conectamos?') + fac('a3', 672, 'mega', 'Anuncios y email', '¿los incluimos?') +
         svg(carr('a1a', 192, 392, 250, 470, 400, 520, col='#9A9E9A') + carr('a2a', 500, 392, 500, 450, 500, 512, col='#9A9E9A') + carr('a3a', 808, 392, 750, 470, 600, 520, col='#9A9E9A')) +
         card('a4', 200, 540, 600, 220, f'<div style="height:100%;padding:0 40px;display:flex;gap:26px;align-items:center"><i style="flex:none;width:80px;height:80px;border-radius:22px;background:linear-gradient(140deg,var(--g1),var(--g2));display:grid;place-items:center;color:#fff">{ic("lock",40)}</i>'
              '<div><div class="big" style="font-size:52px">Precio cerrado</div><div style="font-size:20px;color:var(--mute);margin-top:8px">en la llamada · sin sorpresas</div></div></div>'))
    # B · qué incluye
    inc = [('b1', 'Tu tienda, con tu marca y tu dominio'), ('b2', 'Las fichas de tus productos'), ('b3', 'Pagos: Bizum, Apple Pay y tarjeta'),
           ('b4', 'Envíos a toda España y recogida en tienda'), ('b5', 'Stock con tu TPV', 'si tu TPV lo permite'), ('b6', 'Tu Instagram conectado a la tienda'), ('b7', 'Anuncios listos para empezar')]
    rows = ''.join(lrow(r[0], r[1], sub=(r[2] if len(r) > 2 else ''), h=78, fs=25).replace('class="row"', 'class="row" data-fx="row"') for r in inc)
    B = kick('QUÉ INCLUYE') + h2('Lo que montamos') + card('bl', 56, 190, 888, 572, f'<div style="padding:4px 30px">{rows}</div>')
    # C · qué va aparte
    C = (kick('QUÉ VA APARTE') + h2('Para que no te pille') +
         st('c1', 56, 200, 'Aparte', 'Dominio', 'tu dirección web', col='rose', w=420, h=200, vs=40, r=-.8) +
         st('c2', 524, 200, 'Aparte', 'Comisión', 'de la pasarela, por venta', col='rose', w=420, h=200, vs=40, r=.7) +
         st('c3', 56, 432, 'Aparte', 'Envíos', 'lo que cobra la empresa de envíos', col='rose', w=420, h=200, vs=40, r=.6) +
         st('c4', 524, 432, 'Aparte', 'Anuncios', 'lo que decidas invertir', col='rose', w=420, h=200, vs=40, r=-.9) +
         card('c5', 56, 690, 888, 140, f'<div style="height:100%;padding:0 30px;display:flex;align-items:center;gap:18px"><i class="ni k" style="width:56px;height:56px;border-radius:15px;display:grid;place-items:center">{ic("doc",28)}</i>'
              '<div style="font-size:26px;font-weight:500;letter-spacing:-.02em">Te los detallamos antes de empezar.</div></div>'))
    # D · cómo se recupera (ticket)
    def rr(id, label, val, red=True, big=False):
        return (f'<div id="{id}" data-fx="row" style="display:flex;justify-content:space-between;align-items:baseline;padding:16px 0;border-bottom:1.5px dashed #E5E2DB;font-size:{30 if big else 25}px">'
                f'<span style="color:{"#16191A" if not red else "#3B403D"}">{label}</span><b class="tn" style="font-weight:600;color:{"var(--red)" if red else "#16191A"}">{val}</b></div>')
    tk = (rr('d0', 'Un pedido', '60 €', red=False, big=True) + rr('d1', 'Producto', '−25 €') + rr('d2', 'Envío', '−5 €') + rr('d3', 'Comisión', '−1 €') + rr('d4', 'Traer a ese cliente', '−12 €') +
          '<div id="d5" data-fx="up" style="display:flex;justify-content:space-between;align-items:baseline;padding:22px 0 0">'
          '<span style="font-size:30px;font-weight:600">Te quedan</span><b class="tn disp gt" style="font-size:84px;font-weight:400;letter-spacing:-.04em;line-height:1"><span id="d5n" data-fx="count" data-to="17" data-d="1">0</span> €</b></div>')
    D = (kick('CÓMO SE RECUPERA') + h2('Por pedido') + pill('Números de ejemplo') +
         card('dk', 150, 200, 700, 600, f'<div style="padding:22px 44px">{tk}</div>'))
    # E · la cuenta
    def box(id, x, w, t, s, col='#fff'):
        return (f'<div class="card" id="{id}" style="left:{x}px;top:250px;width:{w}px;height:220px;padding:26px;background:{col};display:flex;flex-direction:column;justify-content:center">'
                f'<div style="font-size:25px;font-weight:600;letter-spacing:-.02em;line-height:1.2">{t}</div><div style="font-size:18px;color:var(--mute);margin-top:8px;line-height:1.3">{s}</div></div>')
    op = lambda x, s: f'<div class="abs disp" style="left:{x}px;top:318px;font-size:64px;font-weight:300;color:#9A9E9A">{s}</div>'
    boxes = ''.join(f'<i id="e4_{i:02d}" data-fx="pop" style="display:block;width:56px;height:56px;border-radius:12px;background:{"linear-gradient(140deg,var(--g1),var(--g2))" if i < 20 else "#EFEDE8"};color:#fff;display:grid;place-items:center">{ic("box",26)}</i>' for i in range(13))
    E = (kick('LA CUENTA') + h2('Cuántos pedidos necesitas') +
         box('e1', 56, 248, 'Lo que inviertes', 'el precio cerrado') + op(318, '÷') +
         box('e2', 370, 270, 'Lo que te queda por pedido', '17 € en el ejemplo') + op(654, '=') +
         box('e3', 706, 238, 'Pedidos para recuperarlo', 'tu número', col='#F1FAF6') +
         ab('e4', 56, 560, f'<div style="font-size:19px;color:var(--mute);margin-bottom:16px">Cada pedido, un trozo</div><div style="display:flex;gap:9px">{boxes}</div>'))
    # F · sin humo
    F = (kick('SIN HUMO') +
         ab('f1', 56, 96, '<div class="big" style="font-size:58px">No te puedo<br>garantizar ventas.</div><div style="font-size:22px;color:var(--mute);margin-top:16px">Dependen de tu producto, tus precios y el mercado.</div>') +
         card('f2', 56, 400, 888, 120, f'<div style="height:100%;padding:0 30px;display:flex;align-items:center;gap:18px">{chk(True)}<div style="font-size:25px;letter-spacing:-.02em">Lo que sí: <b style="font-weight:600">medir desde el primer pedido</b> y mejorar lo que funciona.</div></div>', cls='rowc') +
         card('f3', 56, 570, 420, 270, '<div style="padding:28px"><div style="font-size:17px;font-weight:600;letter-spacing:.12em" class="red">OTRO LOCAL · VÍDEO 1</div>'
              '<div class="disp tn red" style="font-size:66px;font-weight:600;letter-spacing:-.045em;margin-top:14px">+50.000 €</div><div style="font-size:19px;color:var(--mute);margin-top:6px">antes de vender nada</div></div>') +
         card('f4', 524, 570, 420, 270, f'<div style="padding:28px"><div style="font-size:17px;font-weight:600;letter-spacing:.12em" class="grn">TU TIENDA ONLINE</div>'
              f'<div class="disp" style="font-size:52px;font-weight:400;letter-spacing:-.035em;margin-top:18px;display:flex;align-items:center;gap:14px"><span class="grn">{ic("lock",40,2)}</span>Precio cerrado</div><div style="font-size:19px;color:var(--mute);margin-top:10px">en la llamada</div></div>'))
    F = F.replace('class="card rowc"', 'class="card rowc"').replace(chk(True), '<i class="ok" style="flex:none;width:40px;height:40px;border-radius:50%;background:#E3F4EC;display:grid;place-items:center;color:var(--g2)">' + ic('check', 22, 2.6) + '</i>')
    N = nextframe('N', 600, 3540, 'El precio', 'Cerrado', 'en la llamada, sin sorpresas', 6, '¿Por qué tu web actual no vende?')
    frames = [('A', frame('A', 0, 0, 'El precio', A)), ('B', frame('B', 1200, 0, 'Qué incluye', B)),
              ('C', frame('C', 0, 1180, 'Qué va aparte', C)), ('D', frame('D', 1200, 1180, 'Cómo se recupera', D)),
              ('E', frame('E', 0, 2360, 'La cuenta', E)), ('F', frame('F', 1200, 2360, 'Sin humo', F)), ('N', N)]
    lines = [
     'Mira. Vamos por partes. Primero, el precio.',
     '{@A} No es igual para todos. Depende de tres cosas: {a1} cuántos productos tienes, {a2} si conectamos tu TPV, {a3} y si quieres anuncios y email.',
     'Con eso, {a1a,a2a+.1,a3a+.2,a4+.6} en la llamada te damos un precio cerrado. Sin sorpresas.',
     '{@B} Qué incluye: {b1} tu tienda con tu marca, {b2} las fichas, {b3} los pagos, {b4} los envíos y la recogida en tienda, {b5} el stock, {b6} tu Instagram {b7} y los anuncios listos para empezar.',
     '{@C} Y qué va aparte, para que no te pille: {c1} el dominio, {c2} la comisión por venta, {c3} los envíos {c4} y lo que metas en anuncios. {c5} Te lo detallamos antes de empezar.',
     '{@D} Ahora, cómo se recupera. Con números de ejemplo.',
     '{d0} Un pedido de 60 euros. Quitas {d1} el producto, 25. {d2} El envío, 5. {d3} La comisión, 1. {d4} Y lo que costó traer a ese cliente, 12.',
     '{d5,d5n+.1} Te quedan 17 euros por pedido.',
     '{@E} Cada pedido devuelve un trozo. La cuenta es esta: {e1} lo que inviertes, {e2} entre lo que te queda por pedido. {e3} Eso son los pedidos que necesitas. {e4,e4_*}',
     '{@F} Y te digo algo que no me conviene: {f1} no te puedo garantizar ventas. Dependen de tu producto, tus precios y el mercado.',
     '{f2} Lo que sí hacemos es medir desde el primer pedido y mejorar lo que funciona.',
     '{f3} Y acuérdate del vídeo 1: un local eran más de 50.000 euros antes de vender nada. {f4} En la llamada pones los dos números juntos.',
     '{@ALL} Si ya tienes web y no vende, {@N} el vídeo 6 es para ti. {nrec} {>>play}',
    ]
    return 5, '¿Cuánto cuesta y cuánto te devuelve?', frames, lines

if __name__ == '__main__':
    import sys
    n, title, frames, lines = v5()
    print(build(n, title, frames, lines, sys.argv[1])['dur'])
