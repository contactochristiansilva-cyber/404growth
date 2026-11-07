"""Carruseles de la serie «Abierta 24 h» (404 Growth), estilo «etiqueta de envío» (elegido el 7/11/2026).

Fondo crema, cinta lima «ABIERTA 24 H ✦ 404 ✦» en cada diapositiva, etiqueta blanca con borde negro
(cabecera con la hora), sellos redondos verde bosque y subrayado lima. Sin fotos oscuras.
Uso: python3 abierta24h_gen.py <carpeta>  → escribe <carpeta>/C#.html e index.json (1080×1350, SF Pro).
"""
import json, os, sys
OUT = sys.argv[1] if len(sys.argv) > 1 else 'out'
os.makedirs(OUT, exist_ok=True)
CSS = """*{margin:0;padding:0;box-sizing:border-box}html,body{background:#000;scrollbar-width:none}::-webkit-scrollbar{display:none}
.s{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:-apple-system,"SF Pro Display",BlinkMacSystemFont,sans-serif;color:#06120D;background:#F6F1E7;letter-spacing:-.02em;-webkit-font-smoothing:antialiased}
.logo{position:absolute;right:72px;top:62px;font-size:27px;font-weight:800;letter-spacing:-.03em;z-index:3}
.logo sup{font-size:12px;vertical-align:top;position:relative;top:4px;margin-left:2px}
.tape{position:absolute;left:-160px;width:1400px;height:86px;background:#B8E351;display:flex;align-items:center;white-space:nowrap;overflow:hidden;box-shadow:0 6px 0 rgba(10,26,6,.07);z-index:1}
.tape span{font-size:31px;font-weight:900;letter-spacing:.1em;color:#0A1A06;padding-left:30px}
.stage{position:absolute;left:72px;right:72px;top:300px;bottom:150px;display:flex;flex-direction:column;justify-content:center;gap:40px;z-index:2}
mark{background:linear-gradient(transparent 12%,#B8E351 12%,#B8E351 88%,transparent 88%);color:inherit;padding:0 .06em;border-radius:.08em;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.lab{position:relative;background:#fff;border:5px solid #06120D;border-radius:28px;padding:38px 46px 42px;box-shadow:0 10px 0 rgba(6,18,13,.06)}
.row{display:flex;justify-content:space-between;gap:20px;font-size:24px;font-weight:800;letter-spacing:.12em;color:rgba(6,18,13,.55);padding-bottom:20px;border-bottom:4px solid #06120D;margin-bottom:26px}
.ft{display:grid;grid-template-columns:1fr 1fr;gap:20px;padding-bottom:22px;border-bottom:4px solid #06120D;margin-bottom:28px}
.ft small{display:block;font-size:21px;font-weight:800;letter-spacing:.12em;color:rgba(6,18,13,.5);margin-bottom:4px}
.ft b{font-size:42px;font-weight:800;letter-spacing:-.03em}
.h{font-size:92px;line-height:.98;font-weight:800;letter-spacing:-.055em}
.h.m{font-size:80px;line-height:1}.h.sm{font-size:68px;line-height:1.04;letter-spacing:-.05em}
.q{font-size:62px;line-height:1.02;font-weight:800;letter-spacing:-.04em;padding-bottom:24px;border-bottom:4px solid #06120D;margin-bottom:28px}
.p{font-size:42px;line-height:1.28;font-weight:500;color:rgba(6,18,13,.72);letter-spacing:-.015em}
.bc{display:flex;align-items:flex-end;justify-content:space-between;margin-top:30px}
.bars{width:380px;height:66px;background:repeating-linear-gradient(90deg,#06120D 0 4px,transparent 4px 9px,#06120D 9px 11px,transparent 11px 18px,#06120D 18px 24px,transparent 24px 28px)}
.bc span{font-size:22px;font-weight:800;letter-spacing:.14em}
.stamp{position:absolute;z-index:4;right:-24px;top:-162px;width:188px;height:188px;border-radius:50%;border:6px solid #235347;color:#235347;display:grid;place-items:center;text-align:center;transform:rotate(12deg);font-size:26px;font-weight:900;letter-spacing:.08em;line-height:1.1;background:rgba(246,241,231,.94)}
.stamp:after{content:"";position:absolute;inset:8px;border-radius:50%;border:2px solid rgba(35,83,71,.5)}
.stamp.big{width:236px;height:236px;top:-204px;font-size:46px;letter-spacing:.02em;line-height:1}
.bot{position:absolute;left:72px;right:72px;bottom:60px;display:flex;align-items:center;gap:26px;font-size:25px;font-weight:600;color:rgba(6,18,13,.6);letter-spacing:0}
.bar{flex:1;height:6px;border-radius:6px;background:rgba(6,18,13,.12);overflow:hidden}
.bar b{display:block;height:100%;background:#235347;border-radius:6px}
/* piezas */
.phone{align-self:center;position:relative;width:310px;height:400px;border-radius:50px;border:12px solid #163832;overflow:hidden;background:linear-gradient(170deg,#DAF1DE,#8EB69B);box-shadow:0 30px 50px -30px rgba(22,56,50,.55)}
.phone:before{content:"";position:absolute;left:50%;top:14px;width:96px;height:26px;margin-left:-48px;border-radius:20px;background:#163832;z-index:2}
.phone img{width:100%;height:100%;object-fit:cover;object-position:top;display:block}
.lock{display:flex;flex-direction:column;align-items:center;padding-top:70px;color:#06120D}
.lock small{font-size:24px;font-weight:600;opacity:.7}
.lock b{font-size:104px;font-weight:700;letter-spacing:-.04em;line-height:1}
.lock i{margin-top:28px;width:250px;padding:16px 20px;border-radius:20px;background:rgba(255,255,255,.7);font-style:normal;font-size:20px;font-weight:600;line-height:1.3;text-align:left}
.chat{max-width:760px;background:#fff;border:4px solid #06120D;border-radius:30px 30px 30px 8px;padding:24px 32px 16px;align-self:flex-start;box-shadow:0 8px 0 rgba(6,18,13,.06)}
.chat.yo{align-self:flex-end;background:#DAF1DE;border-radius:30px 30px 8px 30px}
.chat small{display:block;font-size:22px;font-weight:800;letter-spacing:.1em;color:rgba(6,18,13,.5);margin-bottom:6px}
.chat p{font-size:44px;font-weight:600;line-height:1.2;letter-spacing:-.02em}
.chat em{display:block;text-align:right;font-style:normal;font-size:22px;font-weight:600;color:rgba(6,18,13,.45);margin-top:6px}
.chats{display:flex;flex-direction:column;gap:22px}
.ab{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-bottom:28px}
.box{position:relative;border:4px solid #06120D;border-radius:22px;padding:22px 16px 20px;text-align:center;background:#fff}
.box b{display:block;font-size:150px;font-weight:900;letter-spacing:-.05em;line-height:.9}
.box span{display:block;font-size:24px;font-weight:700;letter-spacing:.02em;color:rgba(6,18,13,.6);margin-top:8px}
.box.on{background:#B8E351}.box.off{opacity:.42}
.box .stamp{top:-40px;right:-26px;width:150px;height:150px;font-size:26px}
.tb{display:grid;grid-template-columns:1.3fr 1fr 1fr;font-size:32px;font-weight:600;margin-bottom:28px;padding-bottom:22px;border-bottom:4px solid #06120D}
.tb > *{padding:12px 0;border-bottom:3px dashed rgba(6,18,13,.16)}
.tb .hd{font-size:23px;font-weight:800;letter-spacing:.12em;color:rgba(6,18,13,.55)}
.tb > :nth-last-child(-n+3){border-bottom:0}
.tb .y{justify-self:start;font-weight:800;background:#B8E351;border-radius:10px;padding:8px 14px;margin:4px 0}
.tb .n{color:rgba(6,18,13,.4)}
.minis{display:flex;flex-direction:column;gap:18px}
.mini{display:flex;justify-content:space-between;align-items:center;background:#fff;border:4px solid #06120D;border-radius:18px;padding:18px 26px;font-size:30px;font-weight:700}
.mini span{font-size:22px;font-weight:800;letter-spacing:.12em;color:rgba(6,18,13,.55)}
.mini b{font-size:24px;font-weight:800;letter-spacing:.1em;background:#B8E351;border-radius:10px;padding:8px 14px}
.cities{display:flex;flex-wrap:wrap;justify-content:center;gap:20px 22px}
.city{background:#fff;border:4px solid #06120D;border-radius:18px;padding:14px 24px 16px;box-shadow:0 8px 0 rgba(6,18,13,.06)}
.city small{display:block;font-size:19px;font-weight:800;letter-spacing:.14em;color:rgba(6,18,13,.5)}
.city b{font-size:40px;font-weight:800;letter-spacing:-.03em}
.nums{display:flex;justify-content:center;gap:22px}
.nums b{width:132px;height:132px;border-radius:50%;border:5px solid #06120D;background:#fff;display:grid;place-items:center;font-size:46px;font-weight:900;letter-spacing:-.02em}
.nums b:nth-child(odd){transform:rotate(-6deg)}.nums b:nth-child(even){transform:rotate(5deg);background:#B8E351}
.me{display:flex;align-items:center;gap:24px}
.me img{width:116px;height:116px;border-radius:50%;object-fit:cover;border:4px solid #06120D}
.me b{display:block;font-size:40px;font-weight:800;letter-spacing:-.03em}
.me span{font-size:26px;font-weight:600;color:rgba(6,18,13,.55);letter-spacing:0}
"""
TAPE = 'ABIERTA 24 H ✦ 404 ✦ ' * 5
ANG = [(-6, 168), (4, 150), (-3, 160), (5, 146), (-5, 166), (3, 154), (-4, 162)]


def lab(row, h='', cls='', ft=None, q='', stamp='', big=False, extra='', bc=''):
    """Etiqueta: cabecera (izq., dcha.), campos opcionales, cita, titular, extra y código de barras."""
    s = f'<div class="stamp{" big" if big else ""}">{stamp}</div>' if stamp else ''
    f = ''
    if ft:
        f = '<div class="ft"' + (' style="grid-template-columns:1fr"' if len(ft) == 1 else '') + '>' + ''.join(
            f'<div><small>{a}</small><b>{b}</b></div>' for a, b in ft) + '</div>'
    qq = f'<div class="q">{q}</div>' if q else ''
    hh = f'<div class="h {cls}">{h}</div>' if h else ''
    b = f'<div class="bc"><div class="bars"></div><span>{bc}</span></div>' if bc else ''
    return f'<div class="lab">{s}<div class="row"><span>{row[0]}</span><span>{row[1]}</span></div>{f}{extra}{qq}{hh}{b}</div>'


def chat(who, text, t, me=False):
    return f'<div class="chat{" yo" if me else ""}"><small>{who}</small><p>{text}</p><em>{t}</em></div>'


CHRIS = ('<div class="me"><img src="https://404growth.com/christian-hola.jpg"><div><b>Christian Silva</b>'
         '<span>Fundador de 404 Growth</span></div></div>')


def cta(head, ask=''):
    a = f'<div class="p" style="font-size:44px;font-weight:600;color:#06120D">{ask}</div>' if ask else ''
    return (f'<div class="h m">{head}</div>{a}'
            + lab(('REMITENTE', '404GROWTH.COM'), extra=CHRIS + '<div class="p" style="margin-top:26px">Escríbeme <mark>«TIENDA»</mark> por mensaje y te enseño cómo quedaría la tuya.</div>'))


BOX = lambda L, cls='', st='': (f'<div class="box {cls}">{"<div class=stamp>" + st + "</div>" if st else ""}<b>{L}</b>'
                                '<span>Moda · C/ Mayor</span><span>Cierra a las 20:30</span></div>')
NB = '&nbsp;'
C = [
 {'id': 'C8', 'name': 'C8 · POV son las 23.47', 's': [
  lab(('TU TIENDA', 'AHORA · 23:47'), f'Son las 23:47.<br>Tu tienda lleva<br><mark>3{NB}horas cerrada.</mark>', stamp='POV',
      ft=[('CERRÓ A LAS', '20:30'), ('ABRE A LAS', '10:00')]) + '<div class="p">Desliza. Esto pasa cada noche.</div>',
  '<div class="phone"><div class="lock"><small>martes</small><b>23:48</b><i>Nuevo: Vestido de lino, ya en la tienda</i></div></div>'
  + lab(('TU CLIENTA', '23:48'), 'Tu clienta, no.<br>Está en el sofá,<br><mark>con el móvil.</mark>', 'm'),
  '<div class="phone" style="transform:rotate(4deg)"><img src="https://404growth.com/demos/cards/solenne.webp"></div>'
  + lab(('LO QUE VE', '23:51'), f'Ve el vestido que subiste esta mañana.<br><mark>Le{NB}encanta.</mark>', 'm'),
  '<div class="chats">' + chat('CLIENTA', f'¡Hola! ¿Tienes la M del vestido de{NB}lino?', '23:58 · sin leer') + '</div>'
  + lab(('MENSAJE NUEVO', '23:58'), f'Te escribe: «¿Tienes{NB}la{NB}M?».<br><mark>Tú estás dormida.</mark>', 'm'),
  lab(('PEDIDO CONFIRMADO', '00:10'), f'A las 00:10 lo compra.<br><mark>En{NB}otra{NB}tienda.</mark>', stamp='VENDIDO',
      ft=[('DE', 'Otra tienda online'), ('PARA', 'Tu clienta')], bc='PEDIDO Nº 8812'),
  '<div class="chats">' + chat('CLIENTA', f'¡Hola! ¿Tienes la M del vestido de{NB}lino?', '23:58')
  + chat('TÚ', '¡Buenos días! Sí, te la guardo', '09:31 · sin respuesta', True) + '</div>'
  + lab(('TU TIENDA · ABIERTA', '09:30'), f'09:30. Subes la persiana.<br><mark>Ella ya no está.</mark>', 'm'),
  cta(f'Tu tienda cierra.<br><mark>Internet,{NB}no.</mark>', '¿A qué hora te escriben más? Dímelo en comentarios.'),
 ]},
 {'id': 'C9', 'name': 'C9 · A o B', 's': [
  lab(('JUEGO · COMENTA A O B', '23:47'), f'Misma tienda. Mismo barrio.<br><mark>Solo una vende esta{NB}noche.</mark>', 'sm', stamp='JUEGO',
      extra='<div class="ab">' + BOX('A') + BOX('B') + '</div>') + '<div class="p">¿Cuál? Comenta A o B antes de deslizar.</div>',
  lab(('LA RESPUESTA', '23:47'), 'Es la B.<br><mark>Y no por tener<br>mejor producto.</mark>', 'm',
      extra='<div class="ab">' + BOX('A', 'off') + BOX('B', 'on', 'VENDE') + '</div>'),
  lab(('A FRENTE A B', 'COMPARA'), f'Tiene las mismas prendas y los mismos precios que la A.<br><mark>Y una tienda online abierta.</mark>', 'sm',
      extra='<div class="tb"><span></span><span class="hd">TIENDA A</span><span class="hd">TIENDA B</span>'
            '<span>Prendas</span><span>las mismas</span><span>las mismas</span>'
            '<span>Precios</span><span>los mismos</span><span>los mismos</span>'
            '<span>Tienda online</span><span class="n">no</span><span class="y">ABIERTA</span></div>'),
  '<div class="minis">' + ''.join(f'<div class="mini" style="transform:rotate({r}deg)"><span>PEDIDO Nº {n} · TIENDA B</span>{t}<b>PAGADO</b></div>'
                                 for n, t, r in (('1041', '23:12', -1.5), ('1042', '23:47', 1), ('1043', '00:31', -1))) + '</div>'
  + lab(('TIENDA B · ESTA NOCHE', '3 PEDIDOS'), 'Mientras la A duerme,<br>la B <mark>sigue vendiendo.</mark>', 'm'),
  '<div class="cities">' + ''.join(f'<div class="city" style="transform:rotate({r}deg)"><small>PARA</small><b>{c}</b></div>'
                                  for c, r in (('Bilbao', -4), ('Sevilla', 3), ('Valencia', -2), ('A Coruña', 4), ('Murcia', -3), ('Madrid', 2))) + '</div>'
  + lab(('ENVÍOS · TIENDA B', 'TODA ESPAÑA'), f'Y no vende solo a su{NB}calle.<br><mark>Vende a toda España.</mark>', 'm'),
  lab(('DE LA A A LA B', 'PLAZO'), f'Pasar de la A a la B<br>no es abrir otro local.<br><mark>Son 15{NB}días.</mark>', 'm', stamp='15<br>DÍAS', big=True,
      ft=[('DE', 'Tienda A'), ('A', 'Tienda B')]),
  cta('¿Tu tienda es la A o la B?<br>Dímelo en comentarios.'),
 ]},
 {'id': 'C10', 'name': 'C10 · 5 excusas', 's': [
  '<div class="nums"><b>01</b><b>02</b><b>03</b><b>04</b><b>05</b></div>'
  + lab(('SÉ SINCERA', '5 EXCUSAS'), '5 excusas que te<br><mark>cuestan ventas</mark><br>cada noche')
  + '<div class="p">Guárdalo y dime cuál te has dicho tú.</div>',
 ] + [lab(('LO QUE TE DICES', f'0{i}/05'), a, 'sm', q=q, stamp=f'EXCUSA<br>Nº 0{i}') for i, (q, a) in enumerate((
  ('«Mis clientas son de aquí»', 'Hasta que se mudan, se van de vacaciones o <mark>te descubre alguien de Bilbao.</mark>'),
  ('«No entiendo de tecnología»', f'Si sabes usar WhatsApp,<br><mark>sabes llevar una tienda{NB}online.</mark>'),
  ('«No tengo tiempo»', 'La tienda online<br>no te quita tiempo.<br><mark>Te quita mensajes.</mark>'),
  ('«Ya vendo por Instagram»', 'Por mensaje atiendes<br>a una clienta.<br><mark>Una tienda atiende<br>a todas a la vez.</mark>'),
  ('«Eso es para grandes marcas»', 'Las grandes ya están online.<br><mark>Tu ventaja es que tú<br>eres de verdad.</mark>'),
 ), 1)] + [cta('¿Cuál te has dicho tú?<br>Comenta el número.')]},
]


def slide(i, n, body):
    a, top = ANG[i % len(ANG)]
    right = 'Desliza →' if i == 0 else ('404growth.com' if i == n - 1 else f'{i+1}/{n}')
    return (f'<div class="s"><div class="logo">404/GROWTH<sup>®</sup></div>'
            f'<div class="tape" style="top:{top}px;transform:rotate({a}deg)"><span>{TAPE}</span></div>'
            f'<div class="stage">{body}</div>'
            f'<div class="bot"><span>@1christiansilva</span><span class="bar"><b style="width:{(i+1)/n*100:.1f}%"></b></span><span>{right}</span></div></div>')


for c in C:
    n = len(c['s'])
    h = (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
         + ''.join(slide(i, n, b) for i, b in enumerate(c['s'])) + '</body></html>')
    open(f'{OUT}/{c["id"]}.html', 'w', encoding='utf8').write(h)
json.dump([{'id': c['id'], 'name': c['name'], 'n': len(c['s'])} for c in C], open(f'{OUT}/index.json', 'w'), ensure_ascii=False)
print('ok', [(c['id'], len(c['s'])) for c in C])
