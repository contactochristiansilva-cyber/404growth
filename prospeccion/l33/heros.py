"""Heroes nuevos (10/11): dos por tienda, hechos con IA a partir de su producto estrella real.
   hd = 16:9 para el ordenador: el producto grande en el tercio derecho, espacio limpio a la izquierda para el titular.
   hm = 9:16 para el móvil: el producto grande en la mitad de arriba, la mitad de abajo tranquila y oscura para el texto.
uso: python3 heros.py sel.json > heros.json"""
import json, sys
from specs import S
sel = {x['slug']: x for x in json.load(open(sys.argv[1], encoding='utf-8'))}
SCENE = {
    'moda': 'a minimalist brass clothing rail in a softly lit boutique corner with warm stone walls (the garments hang on the rail)',
    'joya': 'pale travertine stone with soft late-afternoon sunlight',
    'cosmetica': 'a marble plinth with soft cinematic light and a gentle blur behind',
    'sneakers': 'a dark concrete studio floor with a single hard spotlight',
    'calzado': 'a warm wooden floor in a softly lit shoe boutique',
    'optica': 'pale travertine stone with crisp sunlight and soft shadows',
}
RULE = ('Reproduce the EXACT products from the reference: identical shape, colours, materials and details; do not redesign them. '
        'Photorealistic high-end commercial photography, no people, no hands, no text, no letters, no logos, no watermark. One single continuous photograph.')
out = []
for s, sp in S.items():
    if s not in sel:
        continue
    x = sel[s]; ni = sp.get('niche') or x['niche']
    p = sp['prods'][:3]
    refs = [f'n{s}-{r}.jpg'.replace('n23-sneakers-', 'ntwentythree-sneakers-') for r, _, _ in p if r]
    prod = ', '.join(d for _, d, _ in p)
    sc = SCENE.get(ni, SCENE['moda'])
    out.append(dict(slug=s, id='hd', fmt='16:9', refs=refs,
                    text=f'Hero campaign image for an online shop: {prod}, displayed together as a hero product arrangement on {sc}. '
                         'The products are large and sharp in the right half of the frame; the left half is calm, clean and softly lit, with space for a headline. ' + RULE))
    out.append(dict(slug=s, id='hm', fmt='9:16', refs=refs,
                    text=f'Vertical hero image for a mobile online shop: {prod}, displayed together as a hero product arrangement on {sc}. '
                         'The products are large and sharp in the upper half of the frame; the lower 40% is calm, darker and empty, with space for a headline. ' + RULE))
json.dump(out, sys.stdout, ensure_ascii=False, indent=1)
print(len(out), file=sys.stderr)
