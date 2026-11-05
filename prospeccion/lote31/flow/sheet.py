# sheet.py <slug>: hoja con referencias (izq.) y resultado (der.) por foto, para revisar prendas y caras
import json, sys, os
from PIL import Image
L31 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s = sys.argv[1]; H = int(sys.argv[2]) if len(sys.argv) > 2 else 260
J = json.load(open(f'{L31}/ai/jobs15_{s}.json'))
rows = []
for j in J:
    i = os.path.basename(j['out'])[:-4]
    refs = [Image.open(p).convert('RGB') for p in j['refs'][:2]]
    out = Image.open(f'{L31}/ai/{s}/{i}.jpg').convert('RGB')
    ims = [x.resize((max(1, int(x.width * H / x.height)), H)) for x in refs + [out]]
    rows.append(ims)
W = max(sum(x.width + 6 for x in r) + 20 for r in rows)
# dos columnas para que no sea muy alta
half = (len(rows) + 1) // 2
o = Image.new('RGB', (W * 2, half * (H + 6)), 'white')
for n, r in enumerate(rows):
    x = (n // half) * W; y = (n % half) * (H + 6)
    for k, im in enumerate(r):
        if k == len(r) - 1: x += 14
        o.paste(im, (x, y)); x += im.width + 6
o.save(f'{L31}/../flow/sheet_{s}.jpg', quality=78); print(o.size)
