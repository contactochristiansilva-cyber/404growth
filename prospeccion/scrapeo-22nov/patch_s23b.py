# python3 patch_s23b.py <in.js> <rows23b.js> <out.js>
# 22/11/2026: cambia el SEED6 del lote del 23/11 (clave seed_20261123, sin subir) por el nuevo (seed_20261123b: 36 tiendas, sin mercerías).
# El worker de entrada ya tiene SEED6 (lo puso scrapeo-21nov/patch_s23.py).
import sys
src, rows, out = sys.argv[1:4]
w = open(src, encoding='utf-8').read()
new = {l.split(' = ')[0]: l for l in open(rows, encoding='utf-8').read().split('\n') if l.startswith('const ')}
lines = w.split('\n')
for k in ('const SEED6_KEY', 'const SEED6'):
    idx = [i for i, l in enumerate(lines) if l.startswith(k + ' = ')]
    assert len(idx) == 1, (k, idx)
    assert k != 'const SEED6_KEY' or '"seed_20261123"' in lines[idx[0]], 'SEED6_KEY no es el del 21/11'
    lines[idx[0]] = new[k]
w = '\n'.join(lines)
assert w.count('[SEED5_KEY, SEED5], [SEED6_KEY, SEED6]]) {') == 1
open(out, 'w', encoding='utf-8').write(w)
print('ok', len(w))
