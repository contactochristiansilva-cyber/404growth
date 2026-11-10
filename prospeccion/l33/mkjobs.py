# Lote 33: de specs.py + sel.json a data/<slug>.json (la tienda) y flow/<slug>.json (los 2 mensajes para el agente de Flow).
#   python3 mkjobs.py <sel.json> [slug ...]
import json, os, re, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, D)
from specs import S

COMMON = ('Photorealistic, high-end commercial photography, natural skin texture, crisp material detail, no text, no letters, no watermark, '
          'no logos, no brand names, no frames, no collage, no words or labels anywhere in the image.')
WEAR = ('Use the EXACT garment(s) and accessories from the reference image: identical cut, length, fabric, colour, print, buttons, trims and details. '
        'Do not redesign, recolour or add garments. Show the clothes on a professional {adj} fashion model (a {who}). If the reference is a mirror selfie, the new photo has no phone, '
        'no mirror and no selfie pose. ' + COMMON)
OBJ = ('Reproduce the EXACT product from the reference image: identical shape, proportions, materials, colours, stones and details; do not redesign it. '
       'Leave out any hands, price tags, stickers, shop text and the original background. ' + COMMON)
OBJ_W = re.compile(r'\b(umbrella|fan|bag|handbag|tote|clutch|loafers?|boots?|sneakers?|shoes?|cap|scarf|stoles|belts|case|bottle|bottles|jar|box|boxes|diffuser|strap)\b', re.I)
CITY_BG = {'moda': '#ECE7E0', 'joya': '#F4EFE6', 'cosmetica': '#F3E6E1', 'sneakers': '#E6E5E1', 'calzado': '#EEE9E2', 'optica': '#EEF2F5'}
NAMES = dict(woman='woman', man='man')


def wear(who):
    w = NAMES.get(who, 'woman')
    return WEAR.format(who=w, adj='male' if w == 'man' else 'female')


def niche(x, sp):
    return sp.get('niche') or ('calzado' if sp.get('light') else x['niche'])


def worn(desc):
    return not OBJ_W.search(desc) or re.search(r'\b(wearing|worn|over|with .*(trousers|jeans|skirt))\b', desc)


def prompts(x, sp):
    ni = niche(x, sp); who = sp.get('who', 'none'); bg = CITY_BG[ni]; city = x['zone']
    J = {}
    person = {'woman': 'A stylish Spanish woman in her thirties', 'man': 'A stylish Spanish man in his thirties'}.get(who, 'A stylish Spanish woman in her thirties')
    # hero
    r, d = sp['hero']
    if ni in ('joya', 'optica') and who == 'none':
        J['h'] = ('4:3', r, OBJ, f'Luxury campaign still life of {d} from the reference, arranged on pale travertine stone with soft late-afternoon sunlight and delicate shadows, '
                               'the piece filling the centre-right of the frame, warm ivory tones, macro-sharp detail. One single continuous photograph.')
    elif ni == 'cosmetica':
        J['h'] = ('16:9', r, OBJ, f'Luxury beauty campaign still life of {d} from the reference. The product stands in the right third of the frame and the scene continues to the left, '
                                 'softly out of focus and calm, with room for a headline. Warm cinematic light, rich textures. One single continuous photograph, never a split screen or collage.')
    else:
        J['h'] = ('16:9', r, wear(who),
                  f'{person} wearing {d} from the reference, walking at {sp["place"]}, golden hour. One single continuous photograph, never a split screen, diptych, panel or collage. '
                  'The subject stands in the right third of the frame and the same scene continues to the left, softly out of focus and calm, with room for a headline. '
                  'Wide editorial campaign image, cinematic natural light.')
    # productos
    for k, (r, d, _) in enumerate(sp['prods'], 1):
        if ni in ('moda',) or (ni in ('sneakers', 'calzado') and worn(d) and not re.search(r'sneaker|shoe|boot|cap|loafer', d, re.I)):
            if worn(d):
                J[f'p{k}'] = ('3:4', r, wear(who),
                              f'E-commerce product photo for a fashion boutique: a model wearing {d} from the reference, standing naturally, framed from just above the lips '
                              f'(face cropped at the mouth) down to the shoes so the whole outfit is visible, centred, on a seamless warm light ({bg}) studio background '
                              'with a soft natural floor shadow, soft diffused daylight from the left.')
                continue
        if ni == 'joya':
            J[f'p{k}'] = ('3:4', r, OBJ if 'worn' not in d else wear('woman'),
                          f'Luxury jewellery e-commerce photo of {d} from the reference, centred on a seamless ivory ({bg}) background with a soft natural shadow, '
                          'the whole piece visible and large in the frame, macro-sharp metal and stone detail, soft diffused daylight.')
        elif ni == 'cosmetica':
            J[f'p{k}'] = ('3:4', r, OBJ, f'Beauty e-commerce product photo of {d} from the reference, centred on a seamless soft blush ({bg}) background with a couple of natural props '
                                         '(a petal, a pale stone) and a soft shadow, the whole product visible and large in the frame, crisp glass and material detail.')
        elif ni == 'optica' and not re.search(r'\b(box|tray|wall|cabinet)\b', d):
            J[f'p{k}'] = ('3:4', r, OBJ, f'Eyewear e-commerce photo of {d} from the reference, front three-quarter view, centred and large in the frame on a seamless cool light '
                                         f'({bg}) background with a soft shadow, crisp acetate, metal and lens detail.')
        elif re.search(r'sneaker|shoe|boot|loafer|derby', d, re.I):
            J[f'p{k}'] = ('3:4', r, OBJ, f'Footwear e-commerce photo of {d} from the reference, a pair shown at a three-quarter angle, centred and large in the frame on a seamless '
                                         f'light ({bg}) background with a soft floor shadow, crisp leather, suede and sole detail.')
        elif re.search(r'\bcap\b', d, re.I):
            J[f'p{k}'] = ('3:4', r, OBJ, f'Product photo of {d} from the reference, three-quarter front view, centred and large in the frame on a seamless light ({bg}) background with a soft shadow, '
                                         'crisp embroidery and fabric detail.')
        else:
            J[f'p{k}'] = ('3:4', r, OBJ, f'E-commerce product photo of {d} from the reference, centred and large in the frame on a seamless light ({bg}) background with a soft shadow, crisp detail.')
    # estilo de vida
    for k in ('l1', 'l2'):
        r, d = sp[k]
        if ni in ('moda', 'sneakers', 'calzado') and who != 'none' and worn(d) and not re.search(r'^(dark|burgundy|beige|three|a guy|a woman seen|grey cargo)', d):
            J[k] = ('3:4', r, wear(who),
                    f'Lifestyle fashion photo: a model wearing {d} from the reference, candid and relaxed in a sunny street of {city}, Spain, natural light, '
                    'framed from the knees up, editorial, shallow depth of field.')
        else:
            J[k] = ('3:4', r, (wear('man' if re.search(r'\b(man|guy)\b', d) else who if who in ('woman', 'man') else 'woman') if re.search(r'\b(woman|man|guy|bride|hand|wrist|neck)\b', d) else OBJ),
                    f'Lifestyle photo: {d}, like in the reference, soft natural light, editorial, warm and inviting, shallow depth of field.')
    r, d = sp['banner']
    J['b'] = ('16:9', r, COMMON, f'Wide interior photo: {d}, inspired by the reference, photographed like a design magazine, beautiful natural light, inviting and tidy. '
                                 'One single continuous photograph, never a split screen or collage.')
    return J


GROUPS = [['h', 'p1', 'p2', 'p3', 'p4'], ['p5', 'p6', 'l1', 'l2', 'b']]


def msgs(slug, J):
    out = []
    for g in GROUPS:
        rules, parts, refs = {}, [], []
        for n, i in enumerate(g, 1):
            fmt, r, rule, txt = J[i]
            if rule not in rules:
                rules[rule] = 'ABCDEFG'[len(rules)]
            ref = f'{slug}-{r}.jpg' if r else None
            if ref and ref not in refs:
                refs.append(ref)
            parts.append(f'IMAGEN {n} «{i}» (formato {fmt}, ' + (f'referencia {ref}' if ref else 'sin referencia') + f', aplica la REGLA {rules[rule]}): {txt}')
        rt = ' '.join(f'REGLA {l}: {r}' for r, l in rules.items())
        out.append(dict(ids=g, refs=refs, text=f'Genera {len(g)} imágenes separadas con Nano Banana 2.1, cada una en su formato y con su referencia (las referencias están adjuntas). '
                                              f'Usa los textos tal cual, sin reescribirlos ni añadir nada. {rt} ' + ' '.join(parts)))
    return out


def keys(J):
    T = {i: v[3] for i, v in J.items()}; K = {}
    for i, t in T.items():
        for L in (60, 80, 110):
            for o in range(0, max(1, len(t) - L), 4):
                c = t[o:o + L]
                if sum(c in v for v in T.values()) == 1:
                    K[i] = c; break
            if i in K:
                break
        assert i in K, i
    return K


def fk(n):
    return f'{n / 1000:.1f}'.replace('.0', '').replace('.', ',') + 'K' if n >= 1000 else str(n)


def data(x, sp):
    ni = niche(x, sp)
    web = x.get('web') or ''
    dom = re.sub(r'^https?://(www\.)?', '', web).strip('/') if web else ''
    if dom and 'contraseña' in x['shop']:
        note = f'{dom} está cerrada con contraseña: hoy no vende. Quien os encuentra fuera de {x["zone"]} solo puede escribiros.'
    elif dom:
        note = f'{dom} enseña quiénes sois, pero no tiene tienda ni carrito: quien os encuentra fuera de {x["zone"]} solo puede escribiros.'
    else:
        note = None
    c = dict(niche=ni, name=x['name'], ig=x['ig'], f=x['f'], city=x['zone'], cityfull=f'{x["zone"]} ({x["region"]})' if x.get('region') and x['region'] != x['zone'] else x['zone'],
             address=x.get('address', ''), logo=sp.get('logo') or dict(text=x['name']), cats=[list(t) for t in sp['cats']],
             prods=[dict(id=f'p{k}', name=n) for k, (_, _, n) in enumerate(sp['prods'], 1)], theme=sp.get('theme', {}))
    if dom:
        c['domain'] = dom
    if note:
        c['web_note'] = note
    for k in ('h1', 'eyebrow', 'sub', 'hp', 'hpm', 'bp', 'bpm', 'ban_h', 'ban_e', 'short', 'hx'):
        if sp.get(k):
            c[k] = sp[k]
    return c


if __name__ == '__main__':
    sel = {x['slug']: x for x in json.load(open(sys.argv[1], encoding='utf-8'))}
    todo = sys.argv[2:] or [s for s in S if s in sel]
    os.makedirs(os.path.join(D, 'data'), exist_ok=True); os.makedirs(os.path.join(D, 'flow'), exist_ok=True)
    for s in todo:
        x = sel[s]; sp = S[s]; J = prompts(x, sp)
        json.dump(data(x, sp), open(os.path.join(D, 'data', s + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        json.dump(dict(slug=s, msgs=msgs(s, J), K=keys(J)), open(os.path.join(D, 'flow', s + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print('ok', s, sorted({r for m in msgs(s, J) for r in m['refs']}))
