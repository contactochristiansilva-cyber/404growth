"""Mensajes para el agente de Google Flow: 15 fotos por tienda en 3 mensajes (prefijo y sufijo comunes una vez).
uso: python3 msgs.py <slug>  -> imprime JSON {slug, msgs:[{ids, refs, text}]}"""
import json, os, sys
B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # = l31 (prospeccion/lote31)
sys.path.insert(0, B + '/tools')
import jobs_lib, jobs_all
jobs_lib.GRID = False
FMT = {'16:9': '16:9', '4:5': '3:4', '3:4': '3:4', '1:1': '1:1'}
GROUPS = [['hero', 'p1', 'p2', 'p3', 'p4'], ['p5', 'x1', 'x2', 'x3', 'look'], ['l1', 'l2', 'l3', 'l4', 'l5']]

def common_prefix(a):
    p = os.path.commonprefix(a)
    k = p.rfind('. ');  return p[:k + 2] if k > 0 else ''

def common_suffix(a):
    r = os.path.commonprefix([x[::-1] for x in a])[::-1]
    k = r.find('Photorealistic');  return r[k:] if k >= 0 else ''

PRE = os.environ.get('PRE', '')
import re
def sents(p):
    return [x.strip() for x in re.split(r'(?<=\.)\s+', p.strip()) if x.strip()]

def build(slug, groups=None):
    J = {os.path.basename(j['out'])[:-4]: j for j in jobs_all.S[slug](slug)}
    out = []
    for g in (groups or GROUPS):
        ids = [i for i in g if i in J]; jobs = [J[i] for i in ids]
        S = [sents(j['prompt']) for j in jobs]
        cnt = {}
        for ss in S:
            for x in set(ss): cnt[x] = cnt.get(x, 0) + 1
        common = {x for x, c in cnt.items() if c >= 2 and len(jobs) > 1}
        rules, labels, parts, refs = {}, 'ABCDEFG', [], []
        for n, (i, j, ss) in enumerate(zip(ids, jobs, S), 1):
            rk = tuple(x for x in ss if x in common)
            if rk and rk not in rules: rules[rk] = labels[len(rules)]
            mid = ' '.join(x for x in ss if x not in common)
            for r in j['refs']:
                b = PRE + os.path.basename(r)
                if b not in refs: refs.append(b)
            rr = ' y '.join(PRE + os.path.basename(r) for r in j['refs'])
            parts.append(f'IMAGEN {n} «{i}» (formato {FMT.get(j["size"], j["size"])}, referencia {rr}' + (f', aplica la REGLA {rules[rk]}' if rk else '') + f'): {mid}')
        rtxt = ' '.join(f'REGLA {l}: {" ".join(rk)}' for rk, l in rules.items())
        text = (f'Genera {len(jobs)} imágenes separadas con Nano Banana Pro, cada una en su formato y con su referencia (las referencias están adjuntas). '
                f'Usa los textos tal cual, sin reescribirlos ni añadir nada. {rtxt} ' + ' '.join(parts))
        out.append(dict(ids=ids, refs=refs, text=text))
    return out

if __name__ == '__main__':
    s = sys.argv[1]; G = [a.split(',') for a in sys.argv[2:]] or None; m = build(s, G)
    json.dump(dict(slug=s, msgs=m), open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{s}.json'), 'w'), ensure_ascii=False, indent=1)
    for x in m: print(x['ids'], x['refs'], len(x['text']))
