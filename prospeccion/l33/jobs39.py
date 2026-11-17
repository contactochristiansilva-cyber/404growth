"""Lote 39 (17/11/2026): las peticiones de Google Flow (modo manual, una por foto) para las 30 del scrapeo del 17/11.
Igual que jobs37.py, con tres cambios:
 - sin «hd»: el hero «h» ya es un bodegón 16:9 con el producto en el tercio derecho, y se copia como hd.jpg;
 - en los nichos que no son de ropa, las fotos con manos o personas usan la regla corta de producto, no la de modelo de moda;
 - el herbolario usa los textos de herbolario (herb()).
uso: python3 jobs39.py sel39.json > flow/q39.json   (formato de q38C: i, s, id, f, r, t)"""
import json, sys
import jobs37
from specs import S

SHORT_P = 'Use the exact products from the reference (same shape, colours, materials and details). Photorealistic, no text, no logos.'
HERB = {'herbolario-cai-salud'}


def jobs(x):
    out = []
    for j in jobs37.jobs(x):
        if j['id'] == 'hd':
            continue
        t = j['text']
        if 'fashion model' in t and x['niche'] not in ('moda', 'calzado', 'sneakers'):
            for g in ('female', 'male'):
                t = t.replace(jobs37.SHORT_W.format(g=g), SHORT_P if j['refs'] else jobs37.SHORT_N)
        if x['slug'] in HERB:
            t = jobs37.herb(t)
        j['text'] = t
        out.append(j)
    return out


if __name__ == '__main__':
    sel = json.load(open(sys.argv[1], encoding='utf-8'))
    Q = []
    for x in sel:
        for j in jobs(x):
            Q.append(dict(i=len(Q), s=j['slug'], id=j['id'], f=j['fmt'], r=[r[:-4] for r in j['refs']], t=j['text']))
    json.dump(Q, sys.stdout, ensure_ascii=False, indent=0)
    refs = sorted({r for q in Q for r in q['r']})
    print(len(Q), 'trabajos;', sum(not q['r'] for q in Q), 'sin referencia;', len(refs), 'referencias', file=sys.stderr)
