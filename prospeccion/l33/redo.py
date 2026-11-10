# Rehace en Flow las fotos que faltan: python3 redo.py sel.json faltan.txt > cola.json  (faltan: "slug:id.id ...")
import json, sys
from mkjobs import prompts, S
sel = {x['slug']: x for x in json.load(open(sys.argv[1], encoding='utf-8'))}
miss = {}
for tok in open(sys.argv[2]).read().split():
    s, ids = tok.split(':'); miss[s] = ids.split('.')
ORDER = ['h', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'l1', 'l2', 'b']
Q = []
for s, ids in miss.items():
    J = prompts(sel[s], S[s]); ids = [i for i in ORDER if i in ids]
    for c in range(0, len(ids), 5):
        g = ids[c:c + 5]; rules, parts, refs = {}, [], []
        for n, i in enumerate(g, 1):
            fmt, r, rule, txt = J[i]
            rules.setdefault(rule, 'ABCDEFG'[len(rules)])
            ref = f'{s}-{r}.jpg' if r else None
            if ref and ref not in refs: refs.append(ref)
            parts.append(f'IMAGEN {n} «{i}» (formato {fmt}, ' + (f'referencia {ref}' if ref else 'sin referencia') + f', aplica la REGLA {rules[rule]}): {txt}')
        rt = ' '.join(f'REGLA {l}: {r}' for r, l in rules.items())
        t = (f'Genera {len(g)} imágenes separadas con Nano Banana 2.1, cada una en su formato y con su referencia (las referencias están adjuntas). '
             f'Usa los textos tal cual, sin reescribirlos ni añadir nada. {rt} ' + ' '.join(parts))
        if s == '23-sneakers':
            t = t.replace('23-sneakers-', 'twentythree-sneakers-'); refs = [x.replace('23-sneakers-', 'twentythree-sneakers-') for x in refs]
        Q.append([s, refs, t])
json.dump(Q, sys.stdout, ensure_ascii=False)
print(len(Q), file=sys.stderr)
