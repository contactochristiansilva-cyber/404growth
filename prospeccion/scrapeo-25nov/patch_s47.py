# python3 patch_s47.py <worker con SEED8> <rows45.js> <salida>
# 25/11/2026: mete el SEED9 (seed_20261125b, lote 47, 35 tiendas con propuesta) justo después del SEED8 y lo añade a la lista de seedOnce.
import sys
src, rows, out = sys.argv[1:4]
w = open(src, encoding='utf-8').read()
assert 'SEED9' not in w, 'ya tiene SEED9'
new = [l for l in open(rows, encoding='utf-8').read().split('\n') if l.startswith('const SEED9')]
assert len(new) == 2
lines = w.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('const SEED8 = ')]
assert len(idx) == 1
lines[idx[0] + 1:idx[0] + 1] = new
w = '\n'.join(lines)
old = '[SEED7_KEY, SEED7], [SEED8_KEY, SEED8]]) {'
assert w.count(old) == 1
w = w.replace(old, '[SEED7_KEY, SEED7], [SEED8_KEY, SEED8], [SEED9_KEY, SEED9]]) {')
open(out, 'w', encoding='utf-8').write(w)
print('ok', len(w))
