# Todas las tiendas en un paquete para la pestaña de Flow: localStorage.__B<n> (trozos) -> window.__Q (cola de mensajes) y __K global (slug__id)
import json, glob, sys
from pjs import comp
order = [l.strip() for l in open(sys.argv[1])] if len(sys.argv) > 1 else sorted(f[5:-5] for f in glob.glob('flow/*.json'))
Q, K = [], {}
for s in order:
    d = json.load(open(f'flow/{s}.json'))
    for m in d['msgs']:
        Q.append([s, m['refs'], comp(m['text'])])
    for k, v in d['K'].items():
        K[f'{s}__{k}'] = v
js = json.dumps(dict(Q=Q, K=K), ensure_ascii=False, separators=(',', ':'))
n = 30000; parts = [js[i:i + n] for i in range(0, len(js), n)]
for i, p in enumerate(parts):
    open(f'/tmp/claude-0/-home-claude/86561a8c-5895-52c1-874b-e63866019285/scratchpad/l33/b{i}.js', 'w').write(
        f'localStorage.__B{i}={json.dumps(p, ensure_ascii=False)};localStorage.__Bn={len(parts)};"b{i} "+localStorage.__B{i}.length')
print(len(Q), len(js), len(parts))
