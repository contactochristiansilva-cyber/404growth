"""Carruseles con IA, serie «Abierta 24 h» (404 Growth). Genera un HTML por carrusel; las fotos van en img/<id>.jpg."""
import json, os, sys
OUT = sys.argv[1] if len(sys.argv) > 1 else 'out'
os.makedirs(OUT, exist_ok=True)
CSS = """*{margin:0;padding:0;box-sizing:border-box}html,body{background:#000;scrollbar-width:none}::-webkit-scrollbar{display:none}
.s{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:-apple-system,"SF Pro Display",BlinkMacSystemFont,"Helvetica Neue",sans-serif;color:#fff;background:#040806;letter-spacing:-.02em;-webkit-font-smoothing:antialiased}
.ph{position:absolute;inset:0;background:radial-gradient(70% 50% at 60% 40%,rgba(184,227,81,.25),transparent 60%),linear-gradient(160deg,#163832,#040806)}
.ph img{width:100%;height:100%;object-fit:cover;display:block}
.sh{position:absolute;inset:0;background:linear-gradient(180deg,rgba(4,8,6,.55) 0%,rgba(4,8,6,0) 22%,rgba(4,8,6,0) 42%,rgba(4,8,6,.82) 72%,#040806 100%)}
.sh.full{background:linear-gradient(180deg,rgba(4,8,6,.6),rgba(4,8,6,.88) 60%,#040806)}
.top{position:absolute;left:72px;right:72px;top:64px;display:flex;justify-content:space-between;align-items:center}
.tag{display:inline-flex;align-items:center;gap:12px;padding:14px 26px 14px 22px;border-radius:999px;background:#B8E351;color:#0A1A06;font-size:27px;font-weight:800;letter-spacing:.04em}
.tag i{width:14px;height:14px;border-radius:50%;background:#0A1A06;box-shadow:0 0 0 4px rgba(10,26,6,.18)}
.logo{font-size:27px;font-weight:800;letter-spacing:-.03em;text-shadow:0 2px 12px rgba(0,0,0,.5)}
.logo sup{font-size:12px;vertical-align:top;position:relative;top:4px;margin-left:2px}
.txt{position:absolute;left:72px;right:72px;bottom:150px;display:flex;flex-direction:column;gap:30px}
.chip{align-self:flex-start;padding:12px 24px;border-radius:999px;border:2px solid rgba(255,255,255,.35);font-size:26px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;background:rgba(4,8,6,.35)}
.h{font-size:104px;line-height:.95;font-weight:800;letter-spacing:-.055em;text-shadow:0 4px 30px rgba(0,0,0,.45)}
.h.m{font-size:88px}.h.s2{font-size:76px;line-height:1}
.h span{color:#B8E351}
.n{font-size:30px;font-weight:800;letter-spacing:.08em;color:#B8E351}
.q{font-size:84px;line-height:1;font-weight:800;letter-spacing:-.05em}
.p{font-size:42px;line-height:1.28;font-weight:500;color:rgba(255,255,255,.82);letter-spacing:-.015em}
.bot{position:absolute;left:72px;right:72px;bottom:64px;display:flex;align-items:center;gap:26px;font-size:25px;font-weight:600;color:rgba(255,255,255,.6);letter-spacing:0}
.bar{flex:1;height:6px;border-radius:6px;background:rgba(255,255,255,.18);overflow:hidden}
.bar b{display:block;height:100%;background:#B8E351;border-radius:6px}
.ab{position:absolute;top:44%;font-size:220px;font-weight:800;letter-spacing:-.06em;line-height:1;text-shadow:0 6px 40px rgba(0,0,0,.6)}
.ab.a{left:150px;color:rgba(255,255,255,.9)}.ab.b{right:150px;color:#B8E351}
.map{position:absolute;left:50%;top:150px;width:860px;transform:translateX(-50%);opacity:.95}
.me{display:flex;align-items:center;gap:24px}
.me img{width:120px;height:120px;border-radius:50%;object-fit:cover;border:3px solid #B8E351}
.me b{display:block;font-size:38px;font-weight:700;letter-spacing:-.03em}
.me span{font-size:28px;color:rgba(255,255,255,.65);font-weight:500;letter-spacing:0}
.cta{align-self:flex-start;padding:24px 38px;border-radius:999px;background:#B8E351;color:#0A1A06;font-size:40px;font-weight:800;letter-spacing:-.02em}
"""
def slide(c, i, s):
    n = len(c['s'])
    img = s.get('img')
    ph = f'<div class="ph">{"<img src=\'img/%s.jpg\' onerror=\'this.remove()\'>" % img if img else ""}</div>'
    if s.get('map'):
        ph = '<div class="ph" style="background:radial-gradient(80% 60% at 50% 40%,rgba(35,83,71,.7),transparent 70%),#040806"><img class="map" src="https://404growth.com/mapa-es.svg" style="width:860px;height:auto;position:absolute;left:110px;top:170px;object-fit:contain"></div>'
    shade = '<div class="sh full"></div>' if s.get('full') else '<div class="sh"></div>'
    ab = '<div class="ab a">A</div><div class="ab b">B</div>' if s.get('ab') else ''
    body = s['html']
    right = 'Desliza →' if i == 0 else ('404growth.com' if i == n - 1 else f'{i+1}/{n}')
    return (f'<div class="s">{ph}{shade}{ab}<div class="top"><span class="tag"><i></i>ABIERTA 24 H</span><span class="logo">404/GROWTH<sup>®</sup></span></div>'
            f'<div class="txt">{body}</div><div class="bot"><span>@1christiansilva</span><span class="bar"><b style="width:{(i+1)/n*100:.1f}%"></b></span><span>{right}</span></div></div>')
CTA = lambda q: (f'<div class="q">{q}</div><div class="p">Escríbeme <b style="color:#B8E351">«TIENDA»</b> por mensaje y te enseño cómo quedaría la tuya.</div>'
                 '<div class="me"><img src="https://404growth.com/christian-hola.jpg"><div><b>Christian Silva</b><span>Fundador de 404 Growth</span></div></div>')
C = [
 {'id': 'C8', 'name': 'C8 · POV son las 23.47', 's': [
  {'img': 'a1', 'html': '<span class="chip">POV</span><div class="h">Son las 23:47.<br>Tu tienda lleva<br><span>3 horas cerrada.</span></div><div class="p">Desliza. Esto pasa cada noche.</div>'},
  {'img': 'a2', 'html': '<div class="h m">Tu clienta, no.<br>Está en el sofá,<br><span>con el móvil.</span></div>'},
  {'img': 'a3', 'html': '<div class="h m">Ve el vestido que subiste esta mañana.<br><span>Le encanta.</span></div>'},
  {'img': 'a4', 'html': '<div class="h m">Te escribe: «¿Tienes la M?».<br><span>Tú estás dormida.</span></div>'},
  {'img': 'a5', 'html': '<div class="h m">A las 00:10 lo compra.<br><span>En otra tienda.</span></div>'},
  {'img': 'a6', 'html': '<div class="h m">09:30. Subes la persiana.<br><span>Ella ya no está.</span></div>'},
  {'img': 'a1', 'full': 1, 'html': '<div class="h m">Tu tienda cierra.<br><span>Internet, no.</span></div>' + CTA('¿A qué hora te escriben más? Dímelo en comentarios.').replace('class="q"', 'class="q" style="font-size:48px;line-height:1.15;letter-spacing:-.03em;color:rgba(255,255,255,.9)"')}]},
 {'id': 'C9', 'name': 'C9 · A o B', 's': [
  {'img': 'b1', 'ab': 1, 'html': '<span class="chip">Juego</span><div class="h s2">Misma tienda. Mismo barrio.<br><span>Solo una vende esta noche.</span></div><div class="p">¿Cuál? Comenta A o B antes de deslizar.</div>'},
  {'img': 'b2', 'html': '<div class="h m">Es la B.<br><span>Y no por tener mejor producto.</span></div>'},
  {'img': 'b2', 'full': 1, 'html': '<div class="h s2">Tiene las mismas prendas y los mismos precios que la A.</div><div class="h s2"><span>Y una tienda online abierta.</span></div>'},
  {'img': 'a5', 'html': '<div class="h m">Mientras la A duerme,<br>la B <span>sigue vendiendo.</span></div>'},
  {'map': 1, 'html': '<div class="h m">Y no vende solo a su calle.<br><span>Vende a toda España.</span></div>'},
  {'img': 'a6', 'html': '<div class="h m">Pasar de la A a la B no es abrir otro local.<br><span>Son 15 días.</span></div>'},
  {'img': 'b1', 'full': 1, 'html': CTA('¿Tu tienda es la A o la B? Dímelo en comentarios.')}]},
 {'id': 'C10', 'name': 'C10 · 5 excusas', 's': [
  {'img': 'b2', 'html': '<span class="chip">Sé sincera</span><div class="h">5 excusas que te <span>cuestan ventas</span> cada noche</div><div class="p">Guárdalo y dime cuál te has dicho tú.</div>'},
  {'img': 'a5', 'html': '<div class="n">EXCUSA 01</div><div class="h s2">«Mis clientas son de aquí»</div><div class="p">Hasta que se mudan, se van de vacaciones o te descubre alguien de Bilbao.</div>'},
  {'img': 'a3', 'html': '<div class="n">EXCUSA 02</div><div class="h s2">«No entiendo de tecnología»</div><div class="p">Si sabes usar WhatsApp, sabes llevar una tienda online.</div>'},
  {'img': 'a1', 'html': '<div class="n">EXCUSA 03</div><div class="h s2">«No tengo tiempo»</div><div class="p">La tienda online no te quita tiempo. Te quita mensajes.</div>'},
  {'img': 'a4', 'html': '<div class="n">EXCUSA 04</div><div class="h s2">«Ya vendo por Instagram»</div><div class="p">Por mensaje atiendes a una clienta. Una tienda atiende a todas a la vez.</div>'},
  {'img': 'b1', 'html': '<div class="n">EXCUSA 05</div><div class="h s2">«Eso es para grandes marcas»</div><div class="p">Las grandes ya están online. Tu ventaja es que tú eres de verdad.</div>'},
  {'img': 'a2', 'full': 1, 'html': CTA('¿Cuál te has dicho tú? Comenta el número.')}]},
]
for c in C:
    h = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>' + ''.join(slide(c, i, s) for i, s in enumerate(c['s'])) + '</body></html>'
    open(f'{OUT}/{c["id"]}.html', 'w', encoding='utf8').write(h)
json.dump([{'id': c['id'], 'name': c['name'], 'n': len(c['s'])} for c in C], open(f'{OUT}/index.json', 'w'), ensure_ascii=False)
print('ok', [c['id'] for c in C])
