# python3 patch_s19.py <in.js> <rows19.js> <out.js>
# 18/11/2026 (para el 19/11) en el worker del admin: SEED4 (clave seed_20261119) después de SEED3, como cuarta lista de seedOnce.
import sys
src, rows, out = sys.argv[1:4]
w = open(src, encoding='utf-8').read()
new = {l.split(' = ')[0]: l for l in open(rows, encoding='utf-8').read().split('\n') if l.startswith('const ')}

def rep(s, a, b, n=1):
    c = s.count(a)
    assert c == n, (c, a[:90])
    return s.replace(a, b)

lines = w.split('\n')
idx = [k for k, l in enumerate(lines) if l.startswith('const SEED3 = ')]
assert len(idx) == 1 and lines[idx[0]].rstrip().endswith('];')
assert not any(l.startswith('const SEED4') for l in lines)
lines[idx[0] + 1:idx[0] + 1] = [new['const SEED4_KEY'], new['const SEED4']]
w = '\n'.join(lines)
w = rep(w, "for (const [KEY, LIST] of [[SEED_KEY, SEED], [SEED2_KEY, SEED2], [SEED3_KEY, SEED3]]) {",
        "for (const [KEY, LIST] of [[SEED_KEY, SEED], [SEED2_KEY, SEED2], [SEED3_KEY, SEED3], [SEED4_KEY, SEED4]]) {")
w = rep(w, "(SEED2 = 16/11, SEED3 = 18/11)", "(SEED2 = 16/11, SEED3 = 18/11, SEED4 = 19/11)")
open(out, 'w', encoding='utf-8').write(w)
print('ok', len(w))
