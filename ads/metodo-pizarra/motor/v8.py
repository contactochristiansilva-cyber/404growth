from common import *

def v8():
    A = (kick('LO QUE MEJOR SE VENDE') + h2('Cuatro pistas') +
         st('a1', 56, 200, 'Cabe en una caja', 'Viaja bien', 'y llega como sale', col='yel', w=420, h=290, vs=44, r=-1, icon='box') +
         st('a2', 524, 200, 'Se gasta', 'Se repite', 'y vuelven a por más', col='mint', w=420, h=290, vs=44, r=.8, icon='repeat') +
         st('a3', 56, 530, 'Tu selección, tu marca', 'No está en todas partes', '', col='lil', w=420, h=290, vs=40, r=.7, icon='star') +
         st('a4', 524, 530, 'O es para', 'Regalar', 'y se compra con prisa', col='rose', w=420, h=290, vs=44, r=-.8, icon='gift'))
    MW = 300
    mm = mapsvg('bmap', 0, 0, MW, mring('bz', 'madrid', MW, 48, 'var(--g2)', 'rgba(46,122,100,.12)').replace('class="mring"', 'class="mring" data-fx="ring"') + mdot('bzd', 'madrid', MW, '#16191A', size=12), extra='position:relative;left:auto;top:auto')
    def opt(id, y, icon, t, s, right=''):
        return (f'<div class="card" id="{id}" style="left:56px;top:{y}px;width:888px;height:196px;padding:0 30px;display:flex;align-items:center;gap:22px">'
                f'<i class="ni g" style="flex:none;width:64px;height:64px;border-radius:18px;display:grid;place-items:center">{ic(icon,30)}</i>'
                f'<div style="flex:1"><div style="font-size:27px;font-weight:600;letter-spacing:-.02em;line-height:1.2">{t}</div><div style="font-size:19px;color:var(--mute);margin-top:6px">{s}</div></div>{right}</div>')
    sizes = '<div style="display:flex;align-items:flex-end;gap:10px;color:var(--g2)">' + ''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:6px">{ic("box",s)}<span style="font-size:15px;font-weight:600">{k}</span></div>' for s, k in [(34, 'S'), (50, 'M'), (68, 'L')]) + '</div>'
    B = (kick('SI ES DELICADO O GRANDE') + h2('Hay salidas') +
         opt('b1', 196, 'store', 'Lo compran online y lo recogen en tu tienda', 'sin envío, sin riesgo') +
         opt('b2', 412, 'pin', 'Envío solo a tu zona', 'o a las provincias que tú elijas', f'<div style="width:{MW}px;height:170px;overflow:hidden;position:relative;margin-right:-10px"><div style="position:absolute;left:0;top:-40px">{mm}</div></div>') +
         opt('b3', 628, 'truck', 'Precio de envío según el tamaño', 'para que no te coma el margen', sizes))
    C = (kick('CUÁNDO NO') + h2('¿Encaja?') +
         card('cl', 56, 200, 888, 460, '<div style="padding:12px 30px">' +
              lrow('c1', 'Vendes servicios o citas, no producto', ok=False, h=140, fs=28).replace('class="row"', 'class="row" data-fx="row"') +
              lrow('c2', 'Solo quieres una web escaparate', ok=False, h=140, fs=28).replace('class="row"', 'class="row" data-fx="row"') +
              lrow('c3', 'Tienes producto, catálogo y alguien para los pedidos', ok=True, h=140, fs=28, tag=('g', 'Encaja')).replace('class="row"', 'class="row" data-fx="row"') + '</div>') +
         ab('c4', 56, 720, '<div class="big" style="font-size:50px">Si es tu caso, <span class="gt" style="font-weight:400">encaja</span>.</div>'))
    def prod(i, col, bg):
        return f'<div style="flex:1;border-radius:14px;background:{bg};height:150px;display:grid;place-items:center;position:relative"><b style="position:absolute;left:10px;top:10px;width:28px;height:28px;border-radius:50%;background:#16191A;color:#fff;display:grid;place-items:center;font-size:14px">{i}</b>{bag(90).replace("#C98B5E",col)}</div>'
    D = (kick('EN LA LLAMADA') + h2('Con tu catálogo delante', size=54) +
         card('d1', 56, 200, 888, 180, f'<div style="height:100%;padding:0 30px;display:flex;align-items:center;gap:20px">'
              f'<i style="flex:none;width:72px;height:72px;border-radius:20px;background:linear-gradient(140deg,var(--g1),var(--g2));display:grid;place-items:center;color:#fff">{ic("video",34)}</i>'
              '<div><div style="font-size:28px;font-weight:600;letter-spacing:-.02em">Tu llamada</div><div style="font-size:19px;color:var(--mute);margin-top:4px">30 minutos, por Google Meet</div></div></div>') +
         card('d2', 56, 420, 888, 250, '<div style="padding:22px 26px"><div style="font-size:20px;font-weight:600">Qué productos subir primero</div>'
              f'<div style="display:flex;gap:14px;margin-top:16px">{prod(1,"#C98B5E","#F3E7DA")}{prod(2,"#7C8466","#E9EEE6")}{prod(3,"#2B2A28","#ECEBE8")}</div></div>') +
         card('d3', 56, 710, 888, 130, f'<div style="height:100%;padding:0 26px;display:flex;align-items:center;gap:18px"><i class="ni g" style="width:56px;height:56px;border-radius:15px;display:grid;place-items:center">{ic("truck",28)}</i>'
              '<div style="font-size:24px;font-weight:600;letter-spacing:-.02em">Y cómo enviarlos</div></div>'))
    ticks = '<div style="display:flex;gap:8px;margin-top:14px">' + ''.join(f'<i style="width:26px;height:26px;border-radius:50%;background:var(--g2);color:#fff;display:grid;place-items:center">{ic("check",15,3)}</i>' for _ in range(8)) + '</div>'
    N = nextframe('N', 600, 2360, 'Has visto', '8 de 8', '', 0, 'Nos vemos en la llamada.', final=True)
    N = N.replace('<div class="v" style="font-size:40px">8 de 8</div>', f'<div class="v" style="font-size:52px">8 de 8</div>{ticks}')
    frames = [('A', frame('A', 0, 0, 'Lo que mejor se vende', A)), ('B', frame('B', 1200, 0, 'Si es delicado o grande', B)),
              ('C', frame('C', 0, 1180, '¿Encaja?', C)), ('D', frame('D', 1200, 1180, 'En la llamada', D)), ('N', N)]
    lines = [
     'Mira. Lo que mejor se vende online tiene alguna de estas cuatro cosas.',
     '{@A} {a1} Cabe en una caja y aguanta el viaje.',
     '{a2} La gente lo repite: se gasta y vuelve a por más.',
     '{a3} No lo encuentras en cualquier sitio: tu selección, tu marca.',
     '{a4} O es para regalar.',
     '{@B} ¿Y si lo tuyo es delicado o grande? Hay salidas.',
     '{b1} Que lo compren online y lo recojan en tu tienda.',
     '{b2,bz+.4,bzd+.3} Envío solo a tu zona, o a las provincias que tú elijas.',
     '{b3} Y un precio de envío según el tamaño, para que no te coma el margen.',
     '{@C} Cuándo no tiene sentido: {c1} si vendes servicios o citas, no producto. {c2} O si solo quieres una web escaparate.',
     '{c3} Si tienes producto, catálogo y alguien para preparar los pedidos, {c4} encaja.',
     '{@D} Lo demás lo vemos en la llamada, {d1} con tu catálogo delante: {d2} qué productos subir primero {d3} y cómo enviarlos.',
     '{@ALL} Y con esto, ya lo has visto todo. {@N} {nrec} Nos vemos en la llamada. {>>play}',
    ]
    return 8, '¿Tu producto se vende online?', frames, lines

if __name__ == '__main__':
    import sys
    n, title, frames, lines = v8()
    print(build(n, title, frames, lines, sys.argv[1])['dur'])
