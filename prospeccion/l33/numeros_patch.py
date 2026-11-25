# Mete «Los números» (numeros42.py) en propuestas v42 ya hechas, sin rehacerlas: entre la tienda y el vídeo.
# Se puede pasar dos veces: si ya la llevan, la cambia por la versión actual.
# python3 numeros_patch.py <p-slug.html> [...]
import sys, re, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numeros42 as N

for f in sys.argv[1:]:
    h = open(f, encoding='utf-8').read()
    if 'id="z4scn"' not in h:
        print('no es v42, no se toca:', f); continue
    h = re.sub(r'<style id="z4n">.*?</style>', '', h, flags=re.S)
    h = re.sub(r'<section id="numeros">.*?</div></section>\n', '', h, flags=re.S)
    h = re.sub(r'<script>\n/\* «Los números».*?</script>', '', h, flags=re.S)
    assert h.count('<section class="sec" id="video">') == 1, f
    h = h.replace('</head>', N.CSS + '</head>', 1)
    h = h.replace('<section class="sec" id="video">', N.HTML + '<section class="sec" id="video">', 1)
    h = h.replace('</body>', N.JS + '</body>', 1)
    h = h.replace('PARTS=[["tienda", 2], ["video", 4]', 'PARTS=[["tienda", 2], ["numeros", 3], ["video", 4]', 1)
    open(f, 'w', encoding='utf-8').write(h)
    print('ok', f, h.count('id="numeros"'))
