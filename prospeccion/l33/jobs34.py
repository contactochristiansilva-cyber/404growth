"""Lote 34: mensajes cortos para el agente de Flow (de 1 a 3 imágenes por mensaje; con 5 y la regla larga, Flow lo rechazó todo el 11/11).
uso: python3 jobs34.py sel34.json > flow/jobs34.json"""
import json, sys, re
from specs import S
from mkjobs import prompts, WEAR, OBJ
sel = json.load(open(sys.argv[1], encoding='utf-8'))
H = {(h['slug'], h['id']): h for h in json.load(open('heros34.json'))} if True else {}
SHORT_W = 'Use the exact garments and accessories from the reference (same cut, colour, fabric, print and details), shown on a professional {g} fashion model. Photorealistic, no text, no logos.'
SHORT_O = 'Reproduce the exact product from the reference (same shape, colours, materials and details). Photorealistic, no text, no logos, no people.'
SHORT_C = 'Photorealistic, no text, no logos, no people.'
out = []
for x in sel:
    s = x['slug']; sp = S[s]; J = prompts(x, sp)
    for i in ['h', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'l1', 'l2', 'b']:
        fmt, r, rule, txt = J[i]
        if rule == OBJ: rr = SHORT_O
        elif rule.startswith('Use the EXACT garment'):
            rr = SHORT_W.format(g='male' if 'male fashion model (a man)' in rule else 'female')
        else: rr = SHORT_C
        txt = txt.replace('A stylish Spanish woman in her thirties', 'A professional female fashion model').replace('A stylish Spanish man in his thirties', 'A professional male fashion model')
        txt = txt.replace('framed from just above the lips (face cropped at the mouth) down to the shoes', 'framed from the shoulders down to the shoes')
        out.append(dict(slug=s, id=i, fmt=fmt, refs=[f'n{s}-{r}.jpg'] if r else [], text=f'{txt} {rr}'))
    for i in ('hd', 'hm'):
        h = H[(s, i)]
        out.append(dict(slug=s, id=i, fmt=h['fmt'], refs=h['refs'], text=h['text']))
json.dump(out, sys.stdout, ensure_ascii=False, indent=0)
print(len(out), file=sys.stderr)
