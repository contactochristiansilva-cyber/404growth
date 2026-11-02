from common import *

def src(id, y, icon, title, sub):
    return (f'<div class="card" id="{id}" style="left:56px;top:{y}px;width:400px;height:128px;padding:0 22px;display:flex;align-items:center;gap:18px">'
            f'<i class="ni g" style="flex:none;width:58px;height:58px;border-radius:16px;display:grid;place-items:center">{ic(icon,28)}</i>'
            f'<div><div style="font-size:24px;font-weight:600;letter-spacing:-.02em">{title}</div><div style="font-size:18px;color:var(--mute);margin-top:4px">{sub}</div></div></div>')

def v4():
    # A · abrir no basta
    browser = ('<div style="height:48px;border-bottom:1.5px solid var(--line);display:flex;align-items:center;gap:8px;padding:0 18px">'
               '<i style="width:12px;height:12px;border-radius:50%;background:#E8E5DE"></i><i style="width:12px;height:12px;border-radius:50%;background:#E8E5DE"></i><i style="width:12px;height:12px;border-radius:50%;background:#E8E5DE"></i>'
               '<div style="margin-left:14px;font-size:15px;color:var(--mute);background:#F3F2EE;border-radius:99px;padding:5px 16px">tutienda.es</div></div>'
               '<div style="position:absolute;left:36px;top:96px"><div class="big" style="font-size:44px">Nueva colección</div><div class="btn" style="width:170px;height:48px;font-size:17px;margin-top:20px">Ver tienda</div></div>'
               f'<div style="position:absolute;left:470px;top:84px;width:170px;height:200px;border-radius:12px;background:#F3E7DA;display:grid;place-items:center">{bag(110)}</div>'
               f'<div style="position:absolute;left:660px;top:84px;width:170px;height:200px;border-radius:12px;background:#E9EEE6;display:grid;place-items:center">{bag(110).replace("#C98B5E","#7C8466").replace("#B0764B","#6A7257")}</div>')
    A = (kick('ABRIR NO BASTA') + h2('Tu tienda, abierta') +
         card('ab', 56, 196, 888, 330, browser, extra='overflow:hidden') +
         ab('a1', 790, 214, '<div class="chip" style="background:#E6F4EE;color:var(--g2);font-weight:600"><i style="width:8px;height:8px;border-radius:50%;background:var(--g2)"></i>Abierta</div>') +
         card('a2', 56, 560, 888, 190, '<div style="position:absolute;left:30px;top:26px;font-size:18px;color:var(--mute)">Visitas hoy</div>'
              '<div class="abs disp tn" style="left:28px;top:56px;font-size:110px;font-weight:300;line-height:1">0</div>' +
              svg(arr('a2l', [(220, 120), (850, 120)], w=3, col='#C9C5BB', head=False), w=888, h=190)) +
         ab('a3', 56, 790, '<div class="big" style="font-size:54px">Nadie sabe que existe.</div>'))
    # B · las cuatro puertas
    def carrow(id, y): return carr(id, 462, y, 560, y, 628, 480, w=3, col='#2E7A64')
    B = (kick('DE DÓNDE SALEN') + h2('Cuatro puertas') +
         src('b1', 196, 'store', 'Tus clientes de ahora', 'mostrador, bolsa, ticket') +
         src('b2', 340, 'camera', 'Tu Instagram', 'compran desde tu perfil') +
         src('b3', 484, 'mega', 'Anuncios', 'en Instagram y Facebook') +
         src('b4', 628, 'mail', 'Email', 'a los que ya pasaron por ella') +
         svg(carrow('b1a', 260) + carrow('b2a', 404) + carrow('b3a', 548) + carrow('b4a', 692)) +
         f'<div class="card" style="left:640px;top:340px;width:304px;height:280px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px">'
         f'<i style="width:86px;height:86px;border-radius:24px;background:linear-gradient(140deg,var(--g1),var(--g2));display:grid;place-items:center;color:#fff">{ic("bag",44)}</i>'
         '<div style="font-size:26px;font-weight:600;letter-spacing:-.02em">Tu tienda online</div></div>'
         '<div class="mring" id="bping" data-fx="ping" style="left:642px;top:330px;width:300px;height:300px;border:4px solid var(--g2)"></div>' +
         ab('bar', 56, 806, '<div class="big" style="font-size:44px">Las cuatro, apuntando <span class="gt" style="font-weight:400">a tu tienda</span>.</div>'))
    # C · anuncios: toda España
    MW = 560
    cities = ['bilbao', 'barcelona', 'sevilla', 'valencia', 'coruna', 'malaga', 'zaragoza', 'palma', 'murcia', 'oviedo', 'alicante', 'granada', 'pamplona', 'vigo', 'santander', 'cadiz', 'girona', 'badajoz', 'valladolid', 'salamanca']
    pts = ''.join(mdot('c2_' + k, k, MW, '#2E7A64', size=14) + mring('c2_' + k + '-p', k, MW, 20, '#2E7A64', 'transparent', dashed=False).replace('class="mring"', 'class="mring" data-fx="ping"') for k in cities)
    pts += mring('c1', 'madrid', MW, 40, 'rgba(22,25,26,.4)', 'rgba(22,25,26,.06)').replace('class="mring"', 'class="mring" data-fx="ring"') + mdot('ct', 'madrid', MW, '#16191A', 'Tu tienda', 1)
    adc = (f'<div style="padding:14px 16px;display:flex;align-items:center;gap:10px"><i style="width:30px;height:30px;border-radius:50%;background:linear-gradient(140deg,var(--g1),var(--g2))"></i>'
           '<div><div style="font-size:14px;font-weight:600">tutienda</div><div style="font-size:12px;color:var(--mute)">Patrocinado</div></div></div>'
           f'<div style="height:250px;background:#F3E7DA;display:grid;place-items:center">{bag(150)}</div>'
           '<div style="padding:14px 16px;display:flex;justify-content:space-between;align-items:center"><div style="font-size:15px;font-weight:600">Bolso de piel<div class="tn" style="font-weight:700;margin-top:2px">129 €</div></div><div class="btn" style="width:100px;height:40px;font-size:14px">Comprar</div></div>')
    C = (kick('PUERTA 3 · ANUNCIOS') + h2('A toda España') +
         mapsvg('cmap', 56, 230, MW, pts) +
         card('cad', 650, 230, 294, 404, adc, extra='overflow:hidden') +
         ab('c3', 56, 790, f'<div class="chip" style="font-size:20px;padding:12px 18px">{ic("users",22)}A gente parecida a la que ya te compra</div>'))
    # D · email
    def mail(id, y, who, subj, body, btn, thumbs):
        return card(id, 56, y, 888, 300,
                    f'<div style="position:absolute;left:30px;top:26px;display:flex;align-items:center;gap:10px;font-size:17px;color:var(--mute)">{ic("mail",20)}{who}</div>'
                    f'<div style="position:absolute;left:30px;top:66px;font-size:30px;font-weight:600;letter-spacing:-.02em">{subj}</div>'
                    f'<div style="position:absolute;left:30px;top:116px;font-size:19px;color:#3B403D">{body}</div>'
                    f'<div class="btn" style="position:absolute;left:30px;bottom:30px;height:52px;padding:0 24px;font-size:18px">{btn}</div>'
                    f'<div style="position:absolute;right:30px;top:60px;display:flex;gap:12px">{thumbs}</div>')
    def th(c1='#C98B5E', c2='#B0764B', bg='#F3E7DA'): return f'<div style="width:120px;height:150px;border-radius:12px;background:{bg};display:grid;place-items:center">{bag(84).replace("#C98B5E",c1).replace("#B0764B",c2)}</div>'
    D = (kick('PUERTA 4 · EMAIL') + h2('Los que vuelven') +
         ab('d1k', 56, 172, '<div style="font-size:17px;font-weight:600;letter-spacing:.12em" class="red">CARRITO A MEDIAS</div>') +
         mail('d1', 204, 'Tu tienda', '¿Te lo has pensado? Te lo guardamos', 'Bolso de piel · 129 €', 'Terminar mi compra', th()) +
         ab('d2k', 56, 542, '<div style="font-size:17px;font-weight:600;letter-spacing:.12em" class="grn">YA TE COMPRÓ</div>') +
         mail('d2', 574, 'Tu tienda', 'Ha llegado lo nuevo', 'Colores nuevos, solo online esta semana', 'Ver novedades', th('#7C8466', '#6A7257', '#E9EEE6') + th('#2B2A28', '#1C1B1A', '#ECEBE8')))
    D = D.replace('Colores nuevos, solo online esta semana', 'Lo nuevo de la colección, ya en la tienda')
    # E · medimos
    def fb(id, y, w, label, a):
        return (f'<div class="abs" id="{id}" data-fx="grow" style="left:{500-w/2:.0f}px;top:{y}px;width:{w}px;height:88px;border-radius:14px;background:rgba(46,122,100,{a});transform-origin:50% 50%;display:flex;align-items:center;justify-content:center;font-size:24px;font-weight:600;color:{"#fff" if a>.5 else "#1E5A47"}">{label}</div>')
    E = (kick('NADA A CIEGAS') + h2('Medimos cada paso') +
         fb('e1', 210, 880, 'Entran', .18) + fb('e2', 312, 660, 'Ven el producto', .32) + fb('e3', 414, 400, 'Llegan al carrito', .6) + fb('e4', 516, 260, 'Compran', .9) +
         svg(f'<path id="e5" data-fx="draw" data-d="1" d="M820 330 C 900 360, 900 470, 760 480 C 640 488, 600 440, 640 400 C 680 362, 760 352, 830 364" pathLength="1" fill="none" stroke="#C2513A" stroke-width="4" stroke-linecap="round" class="dash"/>') +
         ab('e5l', 640, 620, '<div style="font-size:22px;font-weight:600" class="red">Aquí se cae la gente</div>', extra='') +
         ab('e6', 56, 730, '<div class="big" style="font-size:54px">Donde se cae, <span class="gt" style="font-weight:400">ahí arreglamos</span>.</div>'))
    N = nextframe('N', 1200, 2360, '4 puertas', 'Clientes, Instagram, anuncios y email', '', 5, '¿Cuánto cuesta y cuánto te devuelve?')
    N = N.replace('<div class="v" style="font-size:40px">Clientes, Instagram, anuncios y email</div>', '<div class="v" style="font-size:30px;line-height:1.15">Clientes, Instagram, anuncios y email</div>')
    frames = [('A', frame('A', 0, 0, 'Abrir no basta', A)), ('B', frame('B', 1200, 0, 'Las cuatro puertas', B)),
              ('C', frame('C', 0, 1180, 'Anuncios', C)), ('D', frame('D', 1200, 1180, 'Email', D)),
              ('E', frame('E', 0, 2360, 'Medimos', E)), ('N', N)]
    lines = [
     'Mira. Abres la tienda online, y esto es lo que pasa.',
     '{@A} {a1} Abierta. {a2} Cero visitas. {a3} Nadie sabe que existe.',
     '{@B} Los clientes entran por cuatro puertas.',
     'Una: {b1,b1a+.3} tus clientes de ahora. Los que ya entran en tu tienda. Se lo dices en el mostrador, en la bolsa, en el ticket.',
     'Dos: {b2,b2a+.3} tu Instagram. Tus seguidores ven el producto y lo compran desde ahí.',
     'Tres: {b3,b3a+.3} anuncios en Instagram y Facebook. A gente que no te conoce, pero se parece a tus clientes.',
     'Cuatro: {b4,b4a+.3} el email. Para los que ya han pasado por tu tienda online.',
     '{bar,bping+.3} Las cuatro, apuntando a tu tienda.',
     '{@C} Los anuncios, por ejemplo: {c1,ct} no le hablan solo a tu barrio. {c2_*} Le hablan a toda España. {cad,c3+.5} A gente parecida a la que ya te compra.',
     '{@D} Y el email: {d1k,d1+.2} al que dejó el carrito a medias, le recordamos lo que se dejó. {d2k,d2+.2} Y al que ya compró, le avisamos cuando hay algo nuevo.',
     '{@E} Y nada de esto se hace a ciegas. {e1} Medimos cuántos entran, {e2} cuántos ven el producto, {e3} cuántos llegan al carrito {e4} y cuántos compran.',
     '{e5} Donde se cae la gente, {e6} ahí arreglamos.',
     '{@ALL} ¿Cuánto cuesta todo esto, y cuánto te devuelve? {@N} En el vídeo 5. {nrec} {>>play}',
    ]
    return 4, '¿De dónde salen los clientes?', frames, lines

if __name__ == '__main__':
    import sys
    n, title, frames, lines = v4()
    print(build(n, title, frames, lines, sys.argv[1])['dur'])
