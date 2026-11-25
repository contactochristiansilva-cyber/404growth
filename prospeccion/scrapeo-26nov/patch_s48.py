# python3 patch_s48.py <worker con SEED9> <rows48.js> <salida>
# 26/11/2026: mete el SEED10 (seed_20261126, lote 48) justo después del SEED9 y lo añade a la lista de seedOnce.
import sys
src, rows, out = sys.argv[1:4]
w = open(src, encoding='utf-8').read()
assert 'SEED10' not in w, 'ya tiene SEED10'
new = [l for l in open(rows, encoding='utf-8').read().split('\n') if l.startswith('const SEED10')]
assert len(new) == 2
lines = w.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('const SEED9 = ')]
assert len(idx) == 1
lines[idx[0] + 1:idx[0] + 1] = new
w = '\n'.join(lines)
old = '[SEED8_KEY, SEED8], [SEED9_KEY, SEED9]]) {'
assert w.count(old) == 1
w = w.replace(old, '[SEED8_KEY, SEED8], [SEED9_KEY, SEED9], [SEED10_KEY, SEED10]]) {')
open(out, 'w', encoding='utf-8').write(w)
print('ok', len(w))
