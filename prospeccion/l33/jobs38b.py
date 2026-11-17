"""Lote 38b (16/11/2026): los 11 nuevos. Igual que jobs37.py, pero respeta la modelo «curvy» o «madura» y la escena de lencería.
uso: python3 jobs38b.py sel38b.json > flow/jobs38b.json"""
import json, sys
import jobs37
from specs import S

SC = {'venus-lenceria-jerez': 'a soft blush pink velvet surface in a softly lit lingerie boutique'}


def jobs(x):
    out = jobs37.jobs(x)
    s = x['slug']; who = S[s].get('who')
    for j in out:
        t = j['text']
        if who == 'curvy':
            t = t.replace('shown on a professional female fashion model', 'shown on a curvy plus-size female model in her forties')
        elif who == 'mature':
            t = t.replace('shown on a professional female fashion model', 'shown on an elegant female model in her fifties')
        if s in SC:
            t = t.replace(jobs37.SCENE['moda'], SC[s])
        j['text'] = t
    return out


if __name__ == '__main__':
    sel = json.load(open(sys.argv[1], encoding='utf-8'))
    out = [j for x in sel for j in jobs(x)]
    json.dump(out, sys.stdout, ensure_ascii=False, indent=0)
    print(len(out), 'trabajos;', sum(len(j['refs']) == 0 for j in out), 'sin referencia', file=sys.stderr)
