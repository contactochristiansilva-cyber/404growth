"""Lote 36: como jobs35 (mensajes cortos de 1 a 3 imágenes para el agente de Flow), sin heroes hd/hm (ahorra cupo: la tienda usa h).
uso: python3 jobs36.py sel36.json > flow/jobs36.json"""
import json, sys
from specs import S
from mkjobs import prompts, OBJ
sel = json.load(open(sys.argv[1], encoding='utf-8'))
SHORT_W = 'Use the exact garments and accessories from the reference (same cut, colour, fabric, print and details), shown on a professional {g} fashion model. Photorealistic, no text, no logos.'
SHORT_O = 'Reproduce the exact product from the reference (same shape, colours, materials and details). Photorealistic, no text, no logos, no people.'
SHORT_C = 'Photorealistic, no text, no logos, no people.'
SHORT_N = 'Photorealistic, no text, no logos.'
out = []
for x in sel:
    s = x['slug']; sp = S[s]; J = prompts(x, sp)
    for i in ['h', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'l1', 'l2', 'b']:
        fmt, r, rule, txt = J[i]
        if rule == OBJ: rr = SHORT_O if r else SHORT_C
        elif rule.startswith('Use the EXACT garment'):
            rr = SHORT_W.format(g='male' if 'male fashion model (a man)' in rule else 'female')
        else: rr = SHORT_C
        if not r:
            rr = SHORT_N if any(w in txt for w in ('woman', ' man', 'model', 'hiker', 'optometrist', 'audiologist', 'player')) else SHORT_C
        txt = txt.replace('A stylish Spanish woman in her thirties', 'A professional female fashion model').replace('A stylish Spanish man in his thirties', 'A professional male fashion model')
        txt = txt.replace('framed from just above the lips (face cropped at the mouth) down to the shoes', 'framed from the shoulders down to the shoes')
        if not r: txt = txt.replace(' from the reference', '').replace(', like in the reference', '').replace(', inspired by the reference', '')
        out.append(dict(slug=s, id=i, fmt=fmt, refs=[f'n{s}-{r}.jpg'] if r else [], text=f'{txt} {rr}'))
json.dump(out, sys.stdout, ensure_ascii=False, indent=0)
print(len(out), file=sys.stderr)
