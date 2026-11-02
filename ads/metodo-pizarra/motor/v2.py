from common import *

def v2():
    # ---------- A · los 15 días (diagrama de barras) ----------
    X0, LW, CW = 56, 150, (944 - 206) / 15
    def cx(d): return 206 + (d - 1) * CW
    days = ''.join(f'<div class="abs tn" style="left:{cx(d):.0f}px;top:206px;width:{CW:.0f}px;text-align:center;font-size:16px;color:{"var(--g2)" if d==15 else "#9A9E9A"};font-weight:{700 if d==15 else 500}">{d}</div>' for d in range(1, 16))
    vlines = ''.join(f'<div class="abs" style="left:{cx(d):.0f}px;top:236px;width:1px;height:616px;background:#EFEDE7"></div>' for d in range(1, 16))
    def gbar(id, d0, d1, top, label, kind, out=None):
        x = cx(d0) + 3; w = (d1 - d0 + 1) * CW - 6
        bg = 'background:#FFE27A;color:#4D3B00' if kind == 'tu' else 'background:#BFE9D6;color:#1E5A47'
        o = f'<div class="glab" id="{id}l" data-fx="fade" style="left:{x+w+12:.0f}px;top:{top+11}px">{out}</div>' if out else ''
        return f'<div class="gbar" id="{id}" data-fx="grow" style="left:{x:.0f}px;top:{top}px;width:{w:.0f}px;{bg}">{label}</div>' + o
    A = (kick('LOS 15 DÍAS') + h2('Quién hace qué') +
         f'<div class="lane" style="left:56px;top:240px;width:888px;height:206px;background:#FFF9E0"></div>'
         f'<div class="lane" style="left:56px;top:462px;width:888px;height:390px;background:#EDF7F2"></div>' + vlines + days +
         ab('lt', 74, 258, f'<div style="display:flex;align-items:center;gap:8px;font-size:22px;font-weight:600">{ic("users",22)}Tú</div>', cls='') +
         ab('ln', 74, 480, f'<div style="display:flex;align-items:center;gap:8px;font-size:22px;font-weight:600;color:#1E5A47">{ic("spark",22)}Nosotros</div>') +
         gbar('t1', 1, 1, 300, '', 'tu', 'Llamada de arranque · 1 hora') +
         gbar('t2', 1, 3, 372, '', 'tu', 'Fotos y precios por WhatsApp') +
         gbar('n1', 1, 3, 524, '', 'us', 'Fichas de cada producto') +
         gbar('n2', 4, 8, 588, 'Tu marca y el diseño', 'us') +
         gbar('n3', 4, 8, 652, 'Pagos', 'us', 'Bizum, Apple Pay y tarjeta') +
         gbar('n4', 9, 14, 716, 'Envíos y stock', 'us') +
         gbar('n5', 9, 14, 780, 'Pruebas de compra', 'us') +
         f'<div class="abs" id="n6" data-fx="growy" style="left:{cx(15)+4:.0f}px;top:240px;width:{CW-8:.0f}px;height:612px;border-radius:10px;background:linear-gradient(180deg,var(--g1),var(--g2));transform-origin:50% 100%"></div>'
         f'<div class="abs" id="n6l" data-fx="up" style="right:56px;top:868px;font-size:20px;font-weight:600;color:var(--g2);white-space:nowrap">Día 15: abres</div>' +
         svg(f'<rect id="tbox" data-fx="draw" data-d="1" x="48" y="232" width="904" height="222" rx="18" pathLength="1" fill="none" stroke="#E2A23B" stroke-width="4" class="dash"/>'))
    # ---------- B · después del día 15 ----------
    B = (kick('DESPUÉS DEL DÍA 15') + h2('Tu parte: preparar los pedidos', size=54) +
         node('b1', 56, 214, 256, 206, 'bell', 'Nuevo pedido', 'te llega un aviso') +
         node('b2', 372, 214, 256, 206, 'box', 'Lo preparas', 'como en el mostrador', badge=('y', 'Tú'), col='y') +
         node('b3', 688, 214, 256, 206, 'truck', 'Se envía', 'a toda España') +
         svg(arr('b1a', [(318, 317), (364, 317)]) + arr('b2a', [(634, 317), (680, 317)])) +
         card('btu', 56, 470, 428, 380,
              '<div style="padding:28px 30px"><b class="tg y" style="font-size:17px;padding:7px 14px;border-radius:99px">Tú</b>'
              '<div class="big" style="font-size:40px;margin-top:22px">Preparar los pedidos</div>'
              '<div style="font-size:20px;color:var(--mute);margin-top:14px;line-height:1.4">O alguien de tu equipo.<br>Coger el producto, meterlo<br>en una caja, y listo.</div></div>') +
         card('bus', 516, 470, 428, 380,
              '<div style="padding:28px 30px"><b class="tg g" style="font-size:17px;padding:7px 14px;border-radius:99px">Nosotros</b>'
              + ''.join(f'<div style="display:flex;gap:14px;align-items:center;font-size:23px;margin-top:{26 if i==0 else 16}px;letter-spacing:-.02em"><i style="flex:none;width:44px;height:44px;border-radius:12px;background:#E6F4EE;color:var(--g2);display:grid;place-items:center">{ic(n,22)}</i>{t}</div>'
                        for i, (n, t) in enumerate([('mega', 'Traer clientes'), ('mail', 'Anuncios y emails'), ('chart', 'Mirar los números'), ('repeat', 'Ajustar lo que falle')])) + '</div>'))
    # ---------- C · comparado con otro local ----------
    def brick(id, y, t, k, h=86): return f'<div class="brk {k}" id="{id}" style="left:{56 if k=="r" else 524}px;top:{y}px;width:420px;height:{h}px">{t}</div>'
    C = (kick('COMPÁRALO') + h2('Con abrir otro local') +
         ab('', 56, 210, '<div style="font-size:17px;font-weight:600;letter-spacing:.12em" class="red">OTRO LOCAL</div><div class="big" style="font-size:50px;margin-top:4px">Te quita</div>') +
         ab('', 524, 210, '<div style="font-size:17px;font-weight:600;letter-spacing:.12em" class="grn">TIENDA ONLINE</div><div class="big" style="font-size:50px;margin-top:4px">Te quita</div>') +
         brick('c1', 762, 'Buscar sitio', 'r') + brick('c2', 666, 'La obra', 'r') + brick('c3', 570, 'Contratar', 'r') + brick('c4', 474, 'Estar encima cada día', 'r') +
         brick('c5', 762, 'Una llamada · 1 hora', 'g') + brick('c6', 666, 'Tus fotos y precios', 'g'))
    # ---------- D · la duda ----------
    D = (st('dq', 56, 70, '', '«No tengo<br>tiempo»', 'lo que piensas ahora', col='yel', w=430, h=250, vs=46, r=-2.2) +
         ab('dt', 56, 420, '<div class="big" style="font-size:60px">Precisamente<br>por eso lo montamos<br><span class="gt" style="font-weight:400">nosotros</span>.</div>') +
         ab('dt2', 560, 150, f'<div class="chip" style="font-size:19px;padding:10px 16px">{ic("clock",20)}Tu parte: 1 llamada + tus fotos</div>'))
    N = nextframe('N', 600, 2360, 'Tu parte', '1 llamada<br>+ tus fotos', '', 3, '¿Cómo es una tienda online por dentro?')
    frames = [('A', frame('A', 0, 0, 'Los 15 días', A)), ('B', frame('B', 1200, 0, 'Después del día 15', B)),
              ('C', frame('C', 0, 1180, 'Comparado con otro local', C)), ('D', frame('D', 1200, 1180, 'La duda', D)), ('N', N)]
    lines = [
     'Mira, estos son los 15 días. {@A} {lt} Arriba lo tuyo, {ln} abajo lo nuestro.',
     'Lo tuyo: {t1} una llamada de arranque, de una hora, donde lo más técnico lo hacemos juntos.',
     'Y {t2} pasarnos fotos y precios por WhatsApp. Los tres primeros días.',
     'Ya está. {tbox} Esa es tu parte.',
     'Lo nuestro: {n1} las fichas de cada producto, {n2} tu marca y el diseño, {n3} los pagos con Bizum, Apple Pay y tarjeta,',
     '{n4} los envíos y el stock, {n5} las pruebas de compra. Y el día 15, {n6} abres.',
     '{@B} ¿Y después? Después tu parte es una: {b1} preparar los pedidos.',
     'Que es lo mismo que ya haces en el mostrador: {b1a,b2+0.25} coges el producto, lo metes en una caja, {b2a,b3+0.25} y se envía.',
     '{btu} Y si no puedes tú, alguien de tu equipo.',
     '{bus} Lo de traer clientes, los anuncios, los emails y mirar los números, eso es nuestro.',
     '{@C} Compáralo con abrir otro local: {c1} buscar sitio, {c2} la obra, {c3} contratar, {c4} y estar encima todos los días.',
     '{c5} Aquí, una llamada {c6} y tus fotos.',
     '{@D} Así que sí: {dq} no tienes tiempo. {dt} Precisamente por eso lo montamos nosotros. {dt2}',
     '{@ALL} En el siguiente te enseño {p:.6} {@N} cómo es una tienda online por dentro. {nrec} Sin tecnicismos. {>>play}',
    ]
    return 2, '¿Cuánto tiempo te quita?', frames, lines

if __name__ == '__main__':
    import sys
    n, title, frames, lines = v2()
    spec = build(n, title, frames, lines, sys.argv[1])
    print(spec['dur'])
