from common import *
import math

def v7():
    # A · día 15
    def mini(id, x, icon, t):
        return (f'<div class="card" id="{id}" style="left:{x}px;top:470px;width:272px;height:190px;padding:24px">'
                f'<i class="ni g" style="width:52px;height:52px;border-radius:14px;display:grid;place-items:center">{ic(icon,26)}</i>'
                f'<div style="font-size:23px;font-weight:600;letter-spacing:-.02em;margin-top:18px;line-height:1.2">{t}</div></div>')
    A = (kick('DÍA 15') + h2('Tu tienda abre') +
         card('a1', 56, 200, 888, 200, f'<div style="height:100%;padding:0 34px;display:flex;align-items:center;gap:24px">'
              f'<i style="flex:none;width:96px;height:96px;border-radius:26px;background:linear-gradient(140deg,var(--g1),var(--g2));display:grid;place-items:center;color:#fff">{ic("store",48)}</i>'
              '<div><div class="big" style="font-size:56px">Día 15</div><div class="chip" style="margin-top:10px;background:#E6F4EE;color:var(--g2);font-weight:600"><i style="width:8px;height:8px;border-radius:50%;background:var(--g2)"></i>Abierta</div></div></div>') +
         ab('ak', 56, 432, '<div style="font-size:17px;font-weight:600;letter-spacing:.12em" class="mut">TE ENSEÑAMOS A USARLA</div>') +
         mini('a2', 56, 'bell', 'Ver un pedido') + mini('a3', 364, 'box', 'Subir un producto') + mini('a4', 672, 'tag', 'Cambiar un precio') +
         card('a5', 56, 700, 888, 130, f'<div style="height:100%;padding:0 28px;display:flex;align-items:center;gap:18px">'
              f'<i style="flex:none;width:64px;height:64px;border-radius:50%;background:#16191A;color:#fff;display:grid;place-items:center">{ic("play",26)}</i>'
              '<div><div style="font-size:24px;font-weight:600;letter-spacing:-.02em">«Cómo usar tu tienda»</div><div style="font-size:18px;color:var(--mute);margin-top:3px">en vídeo, en tu portal</div></div></div>'))
    # B · el ciclo
    CX, CY, R = 500, 560, 250
    pos = {'b1': (CX, CY - R), 'b2': (CX + R, CY), 'b3': (CX, CY + R), 'b4': (CX - R, CY)}
    labs = {'b1': ('mega', 'Anuncios'), 'b2': ('users', 'Visitas'), 'b3': ('bag', 'Pedidos'), 'b4': ('chart', 'Medimos')}
    nodes = ''.join(f'<div class="card" id="{k}" style="left:{x-110}px;top:{y-44}px;width:220px;height:88px;display:flex;align-items:center;justify-content:center;gap:12px;font-size:24px;font-weight:600;letter-spacing:-.02em;border-radius:99px">'
                    f'<span class="grn">{ic(labs[k][0],26)}</span>{labs[k][1]}</div>' for k, (x, y) in pos.items())
    def arc(id, a0, a1):
        r = R + 0; p0 = (CX + r * math.cos(math.radians(a0)), CY + r * math.sin(math.radians(a0))); p1 = (CX + r * math.cos(math.radians(a1)), CY + r * math.sin(math.radians(a1)))
        am = math.radians((a0 + a1) / 2); k = r / math.cos(math.radians((a1 - a0) / 2))
        c = (CX + k * math.cos(am), CY + k * math.sin(am))
        return carr(id, round(p0[0]), round(p0[1]), round(c[0]), round(c[1]), round(p1[0]), round(p1[1]), w=4, col='#2E7A64', d=.6)
    B = (kick('A PARTIR DE AHÍ') + h2('Traer clientes') +
         svg(arc('b1a', -66, -24) + arc('b2a', 24, 66) + arc('b3a', 114, 156) + arc('b5', 204, 246)) +
         nodes +
         ab('b5l', 150, 330, '<div style="font-size:22px;font-weight:600" class="grn">ajustamos</div>') +
         ab('b6', CX - 150, CY - 44, '<div style="width:300px;text-align:center"><div class="big" style="font-size:44px">Cada <span class="gt" style="font-weight:400">semana</span></div><div style="font-size:18px;color:var(--mute);margin-top:6px">y vuelta a empezar</div></div>'))
    # C · por escrito
    doc = ('<div style="padding:40px 46px"><div style="display:flex;justify-content:space-between;align-items:center"><div class="big" style="font-size:44px">Propuesta</div>'
           '<div style="font-size:16px;color:var(--mute)">404 Growth</div></div>'
           '<div style="margin-top:26px;display:grid;gap:12px"><i style="display:block;height:11px;border-radius:6px;background:#EFEDE8;width:96%"></i><i style="display:block;height:11px;border-radius:6px;background:#EFEDE8;width:88%"></i><i style="display:block;height:11px;border-radius:6px;background:#EFEDE8;width:70%"></i></div>'
           + ''.join(f'<div id="{i}" data-fx="row" style="display:flex;align-items:center;gap:16px;margin-top:{30 if n==0 else 18}px;font-size:27px;letter-spacing:-.02em"><i style="flex:none;width:36px;height:36px;border-radius:9px;background:var(--g2);color:#fff;display:grid;place-items:center">{ic("check",22,2.6)}</i>{t}</div>'
                     for n, (i, t) in enumerate([('c1', 'Mantenimiento técnico'), ('c2', 'Captación continua')])) +
           '<div style="margin-top:34px;display:grid;gap:12px"><i style="display:block;height:11px;border-radius:6px;background:#EFEDE8;width:92%"></i><i style="display:block;height:11px;border-radius:6px;background:#EFEDE8;width:60%"></i></div></div>')
    C = (kick('POR ESCRITO') + h2('Nada en el aire') +
         card('cdoc', 120, 190, 620, 680, doc) +
         svg('<path id="c3" data-fx="draw" data-d="1.1" d="M180 780 C 220 730, 250 800, 290 760 S 350 740, 380 770 S 440 760, 470 748" pathLength="1" fill="none" stroke="#16191A" stroke-width="3" stroke-linecap="round" class="dash"/>') +
         ab('c3l', 180, 800, '<div style="font-size:16px;color:var(--mute)">antes de empezar</div>') +
         st('c4', 640, 560, '', 'Según lo que necesites', '', col='mint', w=300, h=200, vs=34, r=2.2))
    # D · tu portal
    portal = ('<div style="position:absolute;left:0;top:0;bottom:0;width:200px;background:#0F2A22;padding:26px 20px;color:rgba(255,255,255,.75);font-size:17px">'
              '<div style="display:flex;align-items:center;gap:10px;color:#fff;font-weight:600;margin-bottom:26px"><b style="width:28px;height:28px;border-radius:8px;background:linear-gradient(140deg,var(--g1),var(--g2));display:grid;place-items:center;font-size:11px">404</b>Tu portal</div>'
              + ''.join(f'<div style="padding:10px 12px;border-radius:9px;margin-top:4px;{"background:rgba(255,255,255,.1);color:#fff" if n==0 else ""}">{t}</div>' for n, t in enumerate(['Inicio', 'Tu tienda', 'Vídeos', 'Lo que hablamos'])) +
              '</div><div style="position:absolute;left:230px;right:30px;top:30px">'
              '<div style="font-size:18px;color:var(--mute)">Hola</div><div class="big" style="font-size:40px;margin-top:2px">Tu tienda</div>'
              '<div id="d1" data-fx="up" style="margin-top:22px;border-radius:14px;border:1.5px solid var(--line);padding:20px 22px">'
              '<div style="display:flex;justify-content:space-between;align-items:center"><span style="font-size:19px;font-weight:600">Los 15 días</span><span class="chip" style="background:#E6F4EE;color:var(--g2);font-weight:600">Abierta</span></div>'
              '<div style="display:flex;gap:4px;margin-top:16px">' + ''.join('<i style="flex:1;height:10px;border-radius:5px;background:var(--g2)"></i>' for _ in range(15)) + '</div>'
              '<div style="font-size:16px;color:var(--mute);margin-top:12px">15 de 15 · lo siguiente, en marcha</div></div>'
              '<div style="margin-top:16px;display:grid;grid-template-columns:1fr 1fr;gap:14px"><div style="border-radius:14px;background:#F3F2EE;height:110px;padding:16px;font-size:17px;font-weight:600">Vídeos</div><div style="border-radius:14px;background:#F3F2EE;height:110px;padding:16px;font-size:17px;font-weight:600">Lo que hablamos<br>en la llamada</div></div></div>')
    D = (kick('TU PORTAL') + h2('Todo, a la vista') + card('dp', 56, 196, 888, 640, portal, extra='overflow:hidden'))
    N = nextframe('N', 600, 2360, 'Después del 15', 'No te dejamos solo', 'te enseñamos, medimos y ajustamos', 8, '¿Tu producto se puede vender online?')
    N = N.replace('<div class="v" style="font-size:40px">No te dejamos solo</div>', '<div class="v" style="font-size:34px">No te dejamos solo</div>')
    frames = [('A', frame('A', 0, 0, 'Día 15', A)), ('B', frame('B', 1200, 0, 'Lo que sigue', B)),
              ('C', frame('C', 0, 1180, 'Por escrito', C)), ('D', frame('D', 1200, 1180, 'Tu portal', D)), ('N', N)]
    lines = [
     'Mira. Esto es lo que pasa desde el día 15.',
     '{@A} {a1} Día 15: tu tienda abre.',
     'Lo primero: {ak} te enseñamos a usarla. {a2} Cómo ver un pedido, {a3} cómo subir un producto, {a4} cómo cambiar un precio. {a5} Lo tienes también en vídeo, en tu portal.',
     '{@B} Y a partir de ahí empieza lo importante: traer clientes.',
     '{b1} Anuncios, {b1a,b2+.3} visitas, {b2a,b3+.3} pedidos. {b3a,b4+.3} Medimos qué funciona y qué no, {b5} y ajustamos. Y vuelta a empezar.',
     '{b6} Esto no se monta y se olvida: se mejora cada semana.',
     '{@C} ¿Qué seguimos haciendo nosotros, y hasta cuándo? Eso no se deja en el aire.',
     '{c1} El mantenimiento técnico {c2} y la captación continua se acuerdan en la propuesta, {c3} por escrito, antes de empezar. {c4} Según lo que necesites.',
     '{@D} Y tienes tu portal, {d1} donde ves en qué punto está todo.',
     '{@ALL} Y si dudas de si tu producto se puede vender online, {@N} mira el vídeo 8. {nrec} {>>play}',
    ]
    return 7, '¿Qué pasa después del día 15?', frames, lines

if __name__ == '__main__':
    import sys
    n, title, frames, lines = v7()
    print(build(n, title, frames, lines, sys.argv[1])['dur'])
