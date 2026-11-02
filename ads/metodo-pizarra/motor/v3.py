from common import *

def heart(): return '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#16191A" stroke-width="1.8"><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/></svg>'
def bub(): return '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#16191A" stroke-width="1.8"><path d="M20 12a8 8 0 0 1-11.6 7.1L4 20l1-4A8 8 0 1 1 20 12z"/></svg>'
def snd(): return '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#16191A" stroke-width="1.8" stroke-linejoin="round"><path d="M21 3L10 14M21 3l-7 18-4-7-7-4z"/></svg>'

def callout(id, x, y, w, icon, title, sub='', col='g'):
    return (f'<div class="card" id="{id}" style="left:{x}px;top:{y}px;width:{w}px;padding:18px 20px;display:flex;gap:14px;align-items:center">'
            f'<i class="ni {col}" style="flex:none;width:48px;height:48px;border-radius:13px;display:grid;place-items:center">{ic(icon,24)}</i>'
            f'<div><div style="font-size:22px;font-weight:600;letter-spacing:-.02em">{title}</div>' + (f'<div style="font-size:17px;color:var(--mute);margin-top:3px">{sub}</div>' if sub else '') + '</div></div>')

def v3():
    PX, PY = 80, 196
    # A · lo ve
    postA = ('<div class="abs" style="left:16px;top:50px;display:flex;align-items:center;gap:10px"><i style="width:34px;height:34px;border-radius:50%;background:linear-gradient(140deg,var(--g1),var(--g2))"></i>'
             '<div><div style="font-size:15px;font-weight:600">tutienda</div><div id="a2" data-fx="fade" style="font-size:12px;color:var(--mute)">Patrocinado</div></div></div>'
             f'<div class="abs" style="left:0;top:98px;width:298px;height:298px;background:#F3E7DA;display:grid;place-items:center">{bag(190)}</div>'
             '<div class="abs" id="a3t" style="left:14px;top:346px;background:rgba(22,25,26,.85);color:#fff;font-size:13px;font-weight:600;padding:7px 12px;border-radius:8px">Ver producto ›</div>'
             '<div class="abs mring" id="a3" data-fx="ping" style="left:24px;top:330px;width:80px;height:80px;border:3px solid #fff;background:rgba(255,255,255,.25)"></div>'
             f'<div class="abs" style="left:14px;top:408px;display:flex;gap:16px">{heart()}{bub()}{snd()}</div>'
             '<div class="abs" style="left:16px;top:446px;right:16px;font-size:14px;line-height:1.45"><b>tutienda</b> Bolso de piel, hecho a mano. Colores nuevos.<div style="font-weight:700;margin-top:4px">129 €</div></div>')
    A = (kick('PASO 1') + h2('Lo ve') + phone('pa', PX, PY, postA) +
         callout('a1', 470, 330, 474, 'camera', 'En tu Instagram', 'en una publicación tuya') +
         callout('a2b', 470, 470, 474, 'mega', 'O en un anuncio', 'a gente que aún no te conoce'))
    # B · la ficha
    pdp = (f'<div class="abs" style="left:0;top:40px;width:298px;height:262px;background:#F3E7DA;display:grid;place-items:center">{bag(180)}</div>'
           '<div class="abs" style="left:18px;top:318px;font-size:20px;font-weight:600">Bolso de piel</div>'
           '<div class="abs tn" style="left:18px;top:348px;font-size:26px;font-weight:700">129 €</div>'
           '<div class="abs" style="left:18px;top:398px;display:flex;gap:10px"><i style="width:28px;height:28px;border-radius:50%;background:#C98B5E;box-shadow:0 0 0 2px #fff,0 0 0 4px #16191A"></i><i style="width:28px;height:28px;border-radius:50%;background:#2B2A28"></i><i style="width:28px;height:28px;border-radius:50%;background:#7C8466"></i></div>'
           '<div class="abs" style="left:18px;top:446px;font-size:15px;color:#A2541F;font-weight:600;display:flex;align-items:center;gap:7px"><i style="width:8px;height:8px;border-radius:50%;background:#E07B39"></i>Quedan 3</div>'
           '<div class="abs btn" id="b5" data-fx="press" style="left:18px;top:504px;width:262px;height:54px;font-size:18px">Comprar</div>'
           '<div class="abs" style="left:18px;top:572px;font-size:12px;color:var(--mute)">Envío a toda España · Recogida en tienda</div>')
    def lead(id, y0, y1): return arr(id, [(PX + 300, y0), (452, y1)], w=2, col='#9A9E9A', head=False)
    B = (kick('PASO 2') + h2('La ficha') + phone('pb', PX, PY, pdp) +
         callout('b1', 470, 250, 474, 'camera', 'Fotos de verdad', 'las tuyas, bien hechas') +
         callout('b2', 470, 390, 474, 'tag', 'Precio a la vista', 'nadie tiene que preguntar') +
         callout('b3', 470, 530, 474, 'spark', 'Su color', 'elige sin escribirte') +
         callout('b4', 470, 670, 474, 'box', 'Quedan 3', 'el stock real, al momento') +
         svg(lead('b1l', 330, 296) + lead('b2l', 562, 436) + lead('b3l', 610, 576) + lead('b4l', 652, 716)))
    # C · paga
    def opt(id, top, label, sel=False):
        return (f'<div class="abs" id="{id}" style="left:16px;top:{top}px;width:266px;height:58px;border-radius:12px;border:1.5px solid #E3E0D9;display:flex;align-items:center;gap:12px;padding:0 14px;font-size:17px;font-weight:600">'
                f'<i style="width:22px;height:22px;border-radius:50%;border:2px solid #C9C5BB;position:relative;display:block"></i>{label}</div>')
    pay = ('<div class="abs" style="left:18px;top:58px;font-size:22px;font-weight:700">Pagar</div>'
           '<div class="abs" style="left:18px;top:90px;font-size:14px;color:var(--mute)">Bolso de piel · 129 €</div>' +
           opt('c1', 140, 'Tarjeta') + opt('c2', 210, 'Bizum') + opt('c3', 280, 'Apple Pay') +
           '<div class="abs" id="c3l" data-fx="fade" style="left:30px;top:298px;width:22px;height:22px;border-radius:50%;border:7px solid var(--g2)"></div>'
           '<div class="abs" id="c3k" style="left:16px;top:280px;width:266px;height:58px;border-radius:12px;border:2px solid var(--g2);opacity:0"></div>'
           '<div class="abs" style="left:18px;top:380px;right:18px;display:flex;justify-content:space-between;font-size:16px"><span class="mut">Total</span><b class="tn">129 €</b></div>'
           '<div class="abs btn" style="left:18px;top:504px;width:262px;height:54px;font-size:18px;background:var(--g2)">Pagar 129 €</div>')
    C = (kick('PASO 3') + h2('Paga') + phone('pc', PX, PY, pay) +
         card('c4', 470, 300, 474, 196, f'<div style="padding:26px 26px;display:flex;align-items:center;gap:16px"><div class="tn" style="font-size:30px;font-weight:700;padding:10px 16px;border-radius:12px;background:#F3F2EE">129 €</div>'
              f'<div style="color:var(--g2)">{ic("arrow",34,2.2)}</div><i class="ni g" style="width:58px;height:58px;border-radius:16px;display:grid;place-items:center">{ic("bank",28)}</i>'
              '<div style="font-size:22px;font-weight:600;line-height:1.2">Va a tu<br>cuenta</div></div>') +
         ab('c5', 470, 528, f'<div class="chip" style="font-size:18px;padding:10px 16px">− una pequeña comisión por venta</div>'))
    # D · te avisa
    lock = ('<div class="abs disp" style="left:0;right:0;top:86px;text-align:center;color:#fff;font-size:72px;font-weight:300;letter-spacing:-.03em">23:15</div>'
            '<div class="abs" style="left:0;right:0;top:172px;text-align:center;color:rgba(255,255,255,.7);font-size:16px">domingo</div>'
            '<div class="abs" id="d1" data-fx="move" data-dy="-40" style="left:12px;top:226px;width:274px;padding:14px;border-radius:20px;background:rgba(255,255,255,.92);display:flex;gap:12px">'
            f'<i style="flex:none;width:40px;height:40px;border-radius:11px;background:linear-gradient(140deg,var(--g1),var(--g2));display:grid;place-items:center;color:#fff">{ic("bag",22)}</i>'
            '<div style="flex:1;min-width:0"><div style="display:flex;justify-content:space-between;font-size:11px;color:var(--mute)"><span>Tu tienda online</span><span>ahora</span></div>'
            '<div style="font-size:15px;font-weight:700;margin-top:2px">Nuevo pedido · 129 €</div><div style="font-size:13px;color:#3B403D;margin-top:1px">Bolso de piel · Envío a Bilbao</div></div></div>')
    D = (kick('PASO 4') + h2('Te avisa') + phone('pd', PX, PY, lock, dark=True) +
         card('d2c', 470, 250, 474, 300, '<div style="padding:26px 28px"><div style="font-size:18px;color:var(--mute)">Stock · Bolso de piel</div>'
              '<div style="position:relative;height:150px;margin-top:6px"><span id="d2a" data-outf="d2-0.45" class="tn disp" style="position:absolute;left:0;top:0;font-size:150px;font-weight:300;line-height:1">3</span>'
              '<span id="d2" data-fx="up" class="tn disp" style="position:absolute;left:0;top:0;font-size:150px;font-weight:300;line-height:1">2</span></div>'
              '<div id="d2l" data-fx="fade" class="chip" style="background:#E6F4EE;color:var(--g2);margin-top:4px">Baja solo</div></div>') +
         callout('d3', 470, 590, 474, 'store', 'También en la tienda', 'si tu TPV lo permite', col='k'))
    # F · lo envías
    F = (kick('PASO 5') + h2('Lo envías') +
         node('f1', 56, 214, 256, 220, 'box', 'Preparas el paquete', '', badge=('y', 'Tú'), col='y') +
         node('f2', 372, 214, 256, 220, 'truck', 'Se envía', 'a su casa') +
         node('f3', 688, 214, 256, 220, 'home', 'Le llega', 'en Bilbao') +
         svg(arr('f1a', [(318, 324), (364, 324)]) + arr('f2a', [(634, 324), (680, 324)])) +
         card('f4', 150, 500, 700, 330, f'<div style="padding:26px 30px"><div style="display:flex;align-items:center;gap:12px;color:var(--mute);font-size:17px">{ic("mail",22)}Email al cliente</div>'
              '<div style="font-size:30px;font-weight:600;letter-spacing:-.02em;margin-top:16px">Tu pedido va de camino</div>'
              '<div style="margin-top:16px;display:grid;gap:9px"><i style="display:block;height:10px;border-radius:6px;background:#EFEDE8;width:92%"></i><i style="display:block;height:10px;border-radius:6px;background:#EFEDE8;width:70%"></i></div>'
              '<div class="btn" style="margin-top:26px;width:240px;height:52px;font-size:18px">Seguir mi envío</div></div>'))
    # G · tu parte
    rows = [('g1a', 'La ficha y el precio'), ('g1b', 'El pago'), ('g1c', 'El aviso del pedido'), ('g1d', 'El stock'), ('g1e', 'El email de seguimiento')]
    lst = ''.join(lrow(i, t, tag=('g', 'Automático'), fs=25) for i, t in rows) + \
          '<div style="position:relative">' + lrow('g2', 'Preparar el paquete', tag=('y', 'Tú'), fs=25).replace('class="row"', 'class="row" data-fx="row"') + '</div>'
    G = (kick('TU PARTE') + h2('¿Qué es técnico?') +
         card('glist', 56, 196, 888, 476, f'<div style="padding:8px 30px">{lst}</div>') +
         '<div class="abs" id="g2k" style="left:44px;top:560px;width:912px;height:80px;border-radius:16px;border:3px solid #E2A23B;opacity:0"></div>' +
         ab('g3', 56, 730, '<div class="big" style="font-size:52px">Lo técnico, montado<br>por <span class="gt" style="font-weight:400">nosotros</span>.</div>'))
    N = nextframe('N', 600, 3540, 'Tu parte', 'Preparar<br>el paquete', '', 4, '¿De dónde salen los clientes de una tienda online?')
    frames = [('A', frame('A', 0, 0, 'Paso 1 · Lo ve', A)), ('B', frame('B', 1200, 0, 'Paso 2 · La ficha', B)),
              ('C', frame('C', 1200, 1180, 'Paso 3 · Paga', C)), ('D', frame('D', 0, 1180, 'Paso 4 · Te avisa', D)),
              ('F', frame('F', 0, 2360, 'Paso 5 · Lo envías', F)), ('G', frame('G', 1200, 2360, 'Tu parte', G)), ('N', N)]
    conn = ('<svg class="abs" style="left:0;top:0;width:10px;height:10px;overflow:visible">' +
            arr('ca', [(1018, 470), (1182, 470)], w=4, col='#B5B1A7') + arr('cb', [(1700, 958), (1700, 1162)], w=4, col='#B5B1A7') +
            arr('cc', [(1182, 1650), (1018, 1650)], w=4, col='#B5B1A7') + arr('cd', [(500, 2138), (500, 2342)], w=4, col='#B5B1A7') +
            arr('ce', [(1018, 2830), (1182, 2830)], w=4, col='#B5B1A7') + '</svg>')
    lines = [
     'Mira, un pedido de principio a fin.',
     '{@A} Uno: alguien ve tu bolso {a1} en Instagram {a2,a2b} o en un anuncio. {a3,a3t+0.1} Y toca.',
     '{@B,ca} Dos: llega a la ficha. {b1} Foto, {b2} precio, {b3} su color, {b4} y cuántos quedan. Sin tener que preguntarte nada.',
     '{b5,>>b5} Le da a comprar.',
     '{@C,cb} Tres: paga. {c1} Con tarjeta, {c2} con Bizum {c3,c3k+.3} o con Apple Pay. Como en cualquier tienda.',
     '{c4} Y el dinero va a tu cuenta, {c5} menos una pequeña comisión por venta.',
     '{@D,cc} Cuatro: a ti te llega un aviso. {d1} Nuevo pedido, 129 euros. Domingo, once y cuarto de la noche, para Bilbao.',
     '{d2,>d2c} Y el stock baja solo. {d3} Si tu TPV lo permite, también el de la tienda.',
     '{@F,cd} Cinco: {f1} preparas el paquete, {f1a,f2+0.25} se envía, {f2a,f3+0.25} y al cliente le llega un email {f4} para seguirlo.',
     '{@G,ce} ¿Qué parte de todo esto es técnica? {g1a,g1b+.2,g1c+.4,g1d+.6,g1e+.8} Ninguna que tengas que tocar tú.',
     '{g2,g2k+.3} Tú preparas el paquete. {g3} Todo lo demás lo dejamos montado nosotros.',
     '{@ALL} Y si te preguntas de dónde sale la gente que compra, {@N} eso es el vídeo 4. {nrec} {>>play}',
    ]
    return 3, 'Un pedido, de principio a fin', frames, lines, conn

if __name__ == '__main__':
    import sys
    n, title, frames, lines, conn = v3()
    print(build(n, title, frames, lines, sys.argv[1], world_extra=conn)['dur'])
