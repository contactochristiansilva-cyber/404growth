"""Lote 44 (23/11/2026): cola de Google Flow (modo manual) para las 30 de sel44.json, como la de los lotes 42 y 43.
uso: python3 jobs44.py sel44.json > flow/q44.json
Por tienda 11 fotos: p1…p6, l1, l2 (3:4), hd y b (16:9) y hm (9:16); la «h» de la tienda es una copia de hd.
Cada trabajo: {s, id, f, r: [n<slug>-NN.jpg], t, i}, ordenados por formato (3:4, 16:9, 9:16) y por tienda."""
import json, sys
import jobs38b

ORDER = {'3:4': 0, '16:9': 1, '9:16': 2}
if __name__ == '__main__':
    sel = json.load(open(sys.argv[1], encoding='utf-8'))
    q = [dict(s=j['slug'], id=j['id'], f=j['fmt'], r=j['refs'], t=j['text']) for x in sel for j in jobs38b.jobs(x) if j['id'] != 'h']
    q.sort(key=lambda j: (ORDER[j['f']], [x['slug'] for x in sel].index(j['s'])))
    for j in q:
        if j['id'] in ('hd', 'hm'):
            j['t'] = j['t'].replace(' (flat lay)', '')
    for i, j in enumerate(q):
        j['i'] = i
    assert len({j['t'] for j in q}) == len(q), 'textos repetidos'
    json.dump(q, sys.stdout, ensure_ascii=False, indent=0)
    print(len(q), 'trabajos;', sum(not j['r'] for j in q), 'sin referencia;', {f: sum(j['f'] == f for j in q) for f in ORDER}, file=sys.stderr)
