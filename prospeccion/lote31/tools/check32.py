"""Comprueba la ficha de una tienda del lote 32 sin gastar: encargos (modo rejilla) y página (sin imágenes).
uso: python3 check32.py <slug> ...  → imprime los 6 encargos y 'ok' si la página se monta."""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import jobs_lib, jobs_all, gen
jobs_lib.GRID = True
for s in sys.argv[1:]:
    J = jobs_all.S[s](s)
    for j in J:
        miss = [r for r in j['refs'] if not os.path.exists(r)]
        print(' ', os.path.basename(j['out']), j['size'], [os.path.basename(r) for r in j['refs']], 'FALTA REF ' + str(miss) if miss else '')
    c = gen.SHOPS[s]; c['slug'] = s
    ids = ['h', 'p1', 'p2', 'p3', 'p4', 'p5', 'x1', 'x2', 'x3', 'look', 'l1', 'l2', 'l3', 'l4', 'l5']
    h = gen.head(c, ids) + gen.body(c) + gen.scripts(c); gen.shot_html(c)
    left = re.findall(r'\{[a-z_]+\}', re.sub(r'<(script|style)[^>]*>.*?</\1>', '', h, flags=re.S))
    print('ok', s, len(h), 'placeholders', left[:5])
