# python3 patch_s25.py <worker con SEED7> <rows45.js> <salida>
# 25/11/2026: mete el SEED8 (seed_20261125, lote 45, 13 tiendas con propuesta) justo después del SEED7 y lo añade a la lista de seedOnce.
import sys
src, rows, out = sys.argv[1:4]
w = open(src, encoding='utf-8').read()
assert 'SEED8' not in w, 'ya tiene SEED8'
new = [l for l in open(rows, encoding='utf-8').read().split('\n') if l.startswith('const SEED8')]
assert len(new) == 2
lines = w.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('const SEED7 = ')]
assert len(idx) == 1
lines[idx[0] + 1:idx[0] + 1] = new
w = '\n'.join(lines)
old = '[SEED6_KEY, SEED6], [SEED7_KEY, SEED7]]) {'
assert w.count(old) == 1
w = w.replace(old, '[SEED6_KEY, SEED6], [SEED7_KEY, SEED7], [SEED8_KEY, SEED8]]) {')
open(out, 'w', encoding='utf-8').write(w)
print('ok', len(w))
