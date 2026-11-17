"""Lote 37 (15/11/2026): una petición por imagen para Google Flow en modo manual (sin agente), con Nano Banana Pro
cuando hay cupo, y los dos heroes hd (16:9) y hm (9:16) para que la portada salga con la máxima calidad.
uso: python3 jobs37.py sel37.json > flow/jobs37.json
Cada trabajo: slug, id (h, hd, hm, p1…p6, l1, l2, b), fmt (16:9, 4:3, 3:4, 9:16), refs (nombres de las referencias
subidas a Flow, con la cara tapada: n<slug>-NN.jpg) y text (la petición, en inglés)."""
import json, sys
from specs import S
from mkjobs import prompts, OBJ, niche

SHORT_W = 'Use the exact garments and accessories from the reference (same cut, colour, fabric, print and details), shown on a professional {g} fashion model. Photorealistic, no text, no logos.'
SHORT_O = 'Reproduce the exact product from the reference (same shape, colours, materials and details). Photorealistic, no text, no logos, no people.'
SHORT_C = 'Photorealistic, no text, no logos, no people.'
SHORT_N = 'Photorealistic, no text, no logos.'
HERO_RULE = ('Reproduce the EXACT products from the reference: identical shape, colours, materials and details; do not redesign them. '
             'Photorealistic high-end commercial photography, no people, no hands, no text, no letters, no logos, no watermark. One single continuous photograph.')
SCENE = {
    'moda': 'a minimalist brass clothing rail in a softly lit boutique corner with warm stone walls (the garments hang on the rail)',
    'joya': 'pale travertine stone with soft late-afternoon sunlight',
    'cosmetica': 'a marble plinth with soft cinematic light and a gentle blur behind',
    'calzado': 'a warm wooden floor in a softly lit shoe boutique',
    'suplementos': 'a clean concrete plinth in a bright modern gym with crisp daylight and a gentle blur behind',
    'herbolario': 'a wooden counter in a bright herbalist shop with dried herbs, green plants and soft daylight',
}
import niches39 as _n39   # lote 39
SCENE.update(_n39.SCENE)
HERB = {'herbolari-de-lina', 'herbolario-tienda-verde'}


def herb(t):
    return (t.replace('Sports nutrition campaign still life', 'Natural health campaign still life')
             .replace('in a bright modern gym', 'in a bright herbalist shop with wooden shelves and green plants')
             .replace('Crisp daylight, energetic and premium', 'Soft daylight, calm and natural')
             .replace('Sports nutrition e-commerce product photo', 'Natural health e-commerce product photo'))


def jobs(x):
    s = x['slug']; sp = S[s]; J = prompts(x, sp); out = []
    for i in ['h', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'l1', 'l2', 'b']:
        fmt, r, rule, txt = J[i]
        if rule == OBJ:
            rr = SHORT_O if r else SHORT_C
        elif rule.startswith('Use the EXACT garment'):
            rr = SHORT_W.format(g='male' if 'male fashion model (a man)' in rule else 'female')
        else:
            rr = SHORT_C
        if not r:
            rr = SHORT_N if any(w in txt for w in ('woman', ' man', 'model', 'hand')) else SHORT_C
        txt = txt.replace('A stylish Spanish woman in her thirties', 'A professional female fashion model').replace('A stylish Spanish man in his thirties', 'A professional male fashion model')
        txt = txt.replace('framed from just above the lips (face cropped at the mouth) down to the shoes', 'framed from the shoulders down to the shoes')
        if not r:
            txt = txt.replace(' from the reference', '').replace(', like in the reference', '').replace(', inspired by the reference', '')
        if s in HERB:
            txt = herb(txt)
        out.append(dict(slug=s, id=i, fmt=fmt, refs=[f'n{s}-{r}.jpg'] if r else [], text=f'{txt} {rr}'))
    ni = niche(x, sp)
    p = sp['prods'][:3]
    refs = [f'n{s}-{r}.jpg' for r, _, _ in p if r]
    prod = ', '.join(d for _, d, _ in p)
    sc = SCENE['herbolario'] if s in HERB else SCENE.get(ni, SCENE['moda'])
    rule = HERO_RULE if refs else 'Photorealistic high-end commercial photography, no people, no hands, no text, no letters, no logos, no watermark. One single continuous photograph.'
    out.append(dict(slug=s, id='hd', fmt='16:9', refs=refs,
                    text=f'Hero campaign image for an online shop: {prod}, displayed together as a hero product arrangement on {sc}. '
                         'The products are large and sharp in the right half of the frame; the left half is calm, clean and softly lit, with space for a headline. ' + rule))
    out.append(dict(slug=s, id='hm', fmt='9:16', refs=refs,
                    text=f'Vertical hero image for a mobile online shop: {prod}, displayed together as a hero product arrangement on {sc}. '
                         'The products are large and sharp in the upper half of the frame; the lower 40% is calm, darker and empty, with space for a headline. ' + rule))
    return out


if __name__ == '__main__':
    sel = json.load(open(sys.argv[1], encoding='utf-8'))
    out = [j for x in sel for j in jobs(x)]
    json.dump(out, sys.stdout, ensure_ascii=False, indent=0)
    print(len(out), 'trabajos;', sum(len(j['refs']) == 0 for j in out), 'sin referencia', file=sys.stderr)
