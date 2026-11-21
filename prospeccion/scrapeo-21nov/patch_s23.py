# python3 patch_s23.py <in.js> <rows23.js> <out.js>
# 21/11/2026 (para el 23/11) en el worker del admin: SEED6 (clave seed_20261123) después de SEED5, como sexta lista de seedOnce.
import sys
src, rows, out = sys.argv[1:4]
w = open(src, encoding='utf-8').read()
new = {l.split(' = ')[0]: l for l in open(rows, encoding='utf-8').read().split('\n') if l.startswith('const ')}

def rep(s, a, b, n=1):
    c = s.count(a)
    assert c == n, (c, a[:90])
    return s.replace(a, b)

lines = w.split('\n')
idx = [k for k, l in enumerate(lines) if l.startswith('const SEED5 = ')]
assert len(idx) == 1 and lines[idx[0]].rstrip().endswith('];')
assert not any(l.startswith('const SEED6') for l in lines)
lines[idx[0] + 1:idx[0] + 1] = [new['const SEED6_KEY'], new['const SEED6']]
w = '\n'.join(lines)
w = rep(w, "[SEED4_KEY, SEED4], [SEED5_KEY, SEED5]]) {", "[SEED4_KEY, SEED4], [SEED5_KEY, SEED5], [SEED6_KEY, SEED6]]) {")
w = rep(w, "SEED4 = 19/11, SEED5 = 20-21/11)", "SEED4 = 19/11, SEED5 = 20-21/11, SEED6 = 23/11)")
open(out, 'w', encoding='utf-8').write(w)
print('ok', len(w))
