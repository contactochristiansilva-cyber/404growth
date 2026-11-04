"""Referencias frente a fotos generadas, para revisar parecidos con personas reales. uso: cmpref.py <slug> → l32/cmp_<slug>.jpg"""
import json, os, sys
from PIL import Image
L31 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for s in sys.argv[1:]:
    J = {j['out'].split('/')[-1][:-4]: j for j in json.load(open(f'{L31}/ai/jobs_{s}.json'))}
    rows = []
    for g in J.values():
        if g.get('split'):
            refs = g['refs']; outs = [f'{L31}/ai/{s}/{i}.jpg' for i in g['split']]
        else:
            refs = g['refs']; outs = [g['out']]
        rows.append((refs, outs))
    H = 200
    def strip(ps):
        ims = [Image.open(p).convert('RGB') for p in ps]; ims = [i.resize((max(1, int(i.width * H / i.height)), H)) for i in ims]
        return ims
    lines = []
    for refs, outs in rows:
        a = strip(refs); b = strip(outs); lines.append(a + [None] + b)
    W = max(sum((i.width + 4) if i else 30 for i in l) for l in lines)
    out = Image.new('RGB', (W, len(lines) * (H + 8)), 'white')
    for r, l in enumerate(lines):
        x = 0
        for i in l:
            if i is None: x += 30; continue
            out.paste(i, (x, r * (H + 8))); x += i.width + 4
    out.save(f'{L31}/l32/cmp_{s}.jpg', quality=80)
