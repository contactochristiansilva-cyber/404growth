# Genera od_patch.py: aplica la opción D (mapa) a index.html de 404growth.com (v61)
import json, os, base64, gzip
H = os.path.dirname(os.path.abspath(__file__))
M = json.load(open(os.path.join(H, 'map.json')))
W, Hh = M['W'], M['H']
cx, cy = M['cities']['shop']

SVG = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {Hh}" width="{W}" height="{Hh}">'
       f'<path d="{M["d1"]}" stroke="#8EB69B" stroke-opacity=".34" stroke-width="4.2" stroke-linecap="round" fill="none"/>'
       f'<rect x="{M["can"][0]}" y="{M["can"][1]}" width="{M["can"][2]-M["can"][0]}" height="{M["can"][3]-M["can"][1]}" rx="8" fill="none" stroke="#8EB69B" stroke-opacity=".18"/>'
       f'<path d="{M["d2"]}" fill="#8EB69B" fill-opacity=".4"/></svg>')

OD = [  # hora, producto, precio, ciudad, clave, foto  (pedidos de muestra)
    ('23:14', 'Abrigo de lana', 129, 'Sevilla', 'sevilla', 'abrigo-camel'),
    ('00:32', 'Gafas de sol', 119, 'Barcelona', 'barcelona', 'opt-sol'),
    ('01:50', 'Colgante de oro', 149, 'Bilbao', 'bilbao', 'joya-colgante'),
    ('03:05', 'Pendientes de plata', 59, 'A Coruña', 'coruna', 'joya-cuello'),
    ('07:05', 'Bolso de piel', 89, 'Valencia', 'valencia', 'bolso-cuero'),
    ('07:40', 'Jersey de punto', 69, 'Palma', 'palma', 'punto-crudo'),
]
lab = {'sevilla': ('start', 11, 5), 'barcelona': ('middle', 0, -14), 'bilbao': ('start', 11, -6), 'coruna': ('start', 11, -6), 'valencia': ('middle', 0, 24), 'palma': ('middle', 0, 24)}
def arc(k):
    x, y = M['cities'][k]; mx, my = (cx + x) / 2, (cy + y) / 2
    dx, dy = x - cx, y - cy; L = (dx * dx + dy * dy) ** .5
    nx, ny = -dy / L, dx / L
    if ny > 0: nx, ny = -nx, -ny
    h = L * .28
    return f'M{cx} {cy}Q{mx+nx*h:.1f} {my+ny*h:.1f} {x} {y}'

OV = (f'<svg class="od-ov" viewBox="0 0 {W} {Hh}" aria-hidden="true">'
      + ''.join(f'<path class="od-a" style="--d:{i}" d="{arc(k)}" pathLength="1"/>' for i, (t, p, e, c, k, f) in enumerate(OD))
      + ''.join(f'<g class="od-p" style="--d:{i}"><circle cx="{M["cities"][k][0]}" cy="{M["cities"][k][1]}" r="5"/><text x="{M["cities"][k][0]+lab[k][1]}" y="{M["cities"][k][1]+lab[k][2]}" text-anchor="{lab[k][0]}">{c}</text></g>' for i, (t, p, e, c, k, f) in enumerate(OD))
      + f'<g class="od-shop"><circle cx="{cx}" cy="{cy}" r="8"/><text x="{cx-16}" y="{cy+5}" text-anchor="end">Tu tienda</text></g></svg>')

HTML = (f'<div class="scene"><div class="od" aria-hidden="true">'
        f'<div class="od-tx"><p class="od-t">Esta noche, desde tu tienda a <span>toda España</span>.</p>'
        f'<div class="od-ls">' + ''.join(f'<div class="od-o" style="--d:{i}"><img src="/home--t--{f}.jpg" width="40" height="40" alt="" loading="lazy" decoding="async"><div><b>{c}</b><span>{p} · {t}</span></div><em>{e}&nbsp;€</em></div>' for i, (t, p, e, c, k, f) in enumerate(OD)) + '</div></div>'
        f'<div class="od-mw"><img class="od-bg" src="/mapa-es.svg" width="{W}" height="{Hh}" alt="" decoding="async">{OV}'
        f'<i class="od-pu" style="left:{cx/W*100:.2f}%;top:{cy/Hh*100:.2f}%"></i></div>'
        f'</div><p class="od-ex">Ejemplo con pedidos de muestra</p></div>\n')

# Rendimiento en el móvil: nada de backdrop-filter ni filtros; el mapa de puntos es una imagen (se pinta una vez);
# las líneas son un SVG pequeño aparte; el pulso de «Tu tienda» es transform+opacity y se para fuera de pantalla.
CSS = '''/* v61 · inicio: mapa de España con los pedidos de una noche (opción D). Ligero en el móvil: sin blur ni filtros */
.scene{height:auto!important;margin-top:64px}.scene:before{display:none}
.od{display:grid;grid-template-columns:340px 1fr;gap:28px;align-items:center;padding:36px 36px 30px 40px;border-radius:32px;text-align:left;background:linear-gradient(160deg,#0D2621,#060E0A 60%);border:1px solid rgba(218,241,222,.14);box-shadow:0 50px 100px -50px rgba(0,0,0,.9)}
.od-t{font-size:clamp(26px,3vw,34px);font-weight:700;letter-spacing:-.04em;line-height:1.1;color:#fff;text-wrap:balance}
.od-t span{color:var(--lime)}
.od-ls{margin-top:24px;display:flex;flex-direction:column;gap:8px}
.od-o{display:flex;align-items:center;gap:12px;padding:8px 14px 8px 8px;border-radius:16px;background:#0F1F19;border:1px solid rgba(255,255,255,.08);opacity:.2}
.od.in .od-o{opacity:1;transition:opacity .5s;transition-delay:calc(1.4s + var(--d)*1.1s)}
.od-o img{width:40px;height:40px;border-radius:10px;object-fit:cover;background:#1A2A23}
.od-o div{flex:1;min-width:0}.od-o b{display:block;font-size:15px;font-weight:650;color:#fff}.od-o span{display:block;font-size:12.5px;color:rgba(226,238,228,.6);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.od-o em{font-style:normal;font-weight:650;font-size:15px;color:#fff;font-variant-numeric:tabular-nums}
.od-mw{position:relative;contain:layout paint}
.od-bg{display:block;width:100%;height:auto}
.od-ov{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.od-a{fill:none;stroke:var(--lime);stroke-width:2.2;stroke-linecap:round;stroke-dasharray:1;stroke-dashoffset:1}
.od.in .od-a{stroke-dashoffset:0;transition:stroke-dashoffset .9s cubic-bezier(.5,0,.3,1);transition-delay:calc(.5s + var(--d)*1.1s)}
.od-p{opacity:0}.od.in .od-p{opacity:1;transition:opacity .4s;transition-delay:calc(1.3s + var(--d)*1.1s)}
.od-p circle{fill:#fff;stroke:rgba(184,227,81,.5);stroke-width:4}
.od-ov text{font:600 14px var(--f);fill:#fff;letter-spacing:-.01em;paint-order:stroke;stroke:#08130F;stroke-width:5px;stroke-linejoin:round}
.od-shop circle{fill:var(--lime)}.od-shop text{font-weight:700;fill:var(--lime)}
.od-pu{position:absolute;width:20px;height:20px;margin:-10px 0 0 -10px;border-radius:50%;border:2px solid var(--lime);opacity:0;pointer-events:none;animation:odP 2.4s ease-out infinite paused}
.od.vis .od-pu{animation-play-state:running}
@keyframes odP{0%{transform:scale(1);opacity:.9}100%{transform:scale(3.2);opacity:0}}
.od-ex{margin-top:14px;text-align:center;font-size:12px;color:rgba(226,238,228,.4)}
@media (max-width:860px){
.scene{margin-top:38px}
.od{grid-template-columns:1fr;gap:6px;padding:24px 16px 18px;border-radius:24px}
.od-tx{display:contents}.od-t{order:0;font-size:25px;padding:0 4px}.od-mw{order:1;margin:10px -4px 0}.od-ls{order:2;margin-top:6px}
.od-o:nth-child(n+4){display:none}
.od-ov text{font-size:22px;stroke-width:7px}
.od-a{stroke-width:2.8}
}
@media (prefers-reduced-motion:reduce){.od-a{stroke-dashoffset:0}.od-p,.od-o{opacity:1}.od-pu{display:none}}
'''

JS = '''<script>/*od61*/(function(){var o=document.querySelector('.od');if(!o)return;if(!('IntersectionObserver' in window)||matchMedia('(prefers-reduced-motion: reduce)').matches){o.classList.add('in');return}new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)o.classList.add('in','vis');else o.classList.remove('vis')})},{threshold:.3}).observe(o)})()</script>'''

THUMBS = sorted({f for *_, f in OD})
svgz = base64.b64encode(gzip.compress(SVG.encode(), 9)).decode()

PATCH = f'''# v61 · portada: visual del inicio = mapa de España (opción D). Uso: python3 od_patch.py <carpeta web117-404growth>
import sys, os, base64, gzip
D = sys.argv[1]
p = os.path.join(D, 'index.html')
s = open(p, encoding='utf-8').read()
HTML = {HTML!r}
CSS = {CSS!r}
JS = {JS!r}
# 1 · el bloque del visual
a = s.index('<div class="scene"')
b = s.index('<div class="with"', a)
s = s[:a] + HTML + s[b:]
# 2 · CSS: fuera el de v60 (foto + notificaciones con blur), dentro el del mapa
a = s.find('/* v60 · inicio')
if a < 0: a = s.index('/* v61 · inicio')
b = s.index('/* v60 · móvil más ligero', a)
s = s[:a] + CSS + s[b:]
# 3 · JS (antes de </body>)
if '/*od61*/' not in s:
    s = s.replace('</body>', JS + '</body>', 1)
open(p, 'w', encoding='utf-8').write(s)
# 4 · mapa de puntos (imagen fija)
open(os.path.join(D, 'mapa-es.svg'), 'wb').write(gzip.decompress(base64.b64decode({svgz!r})))
# 5 · miniaturas 80x80 de los productos
from PIL import Image, ImageOps
for n in {THUMBS!r}:
    im = Image.open(os.path.join(D, 'home--a--' + n + '.jpg')).convert('RGB')
    ImageOps.fit(im, (80, 80), Image.LANCZOS, centering=(.5, .35)).save(os.path.join(D, 'home--t--' + n + '.jpg'), quality=80, optimize=True, progressive=True)
print('ok', len(s))
'''
open(os.path.join(H, 'od_patch.py'), 'w').write(PATCH)
print('patch', len(PATCH), 'svg', len(SVG), 'gz', len(svgz))
