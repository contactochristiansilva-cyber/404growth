"""Prompt building blocks for lote 31 (Apimart / Nano Banana Pro). Every image starts from the shop's real product photos."""
import os, re
L31 = os.environ.get('L31', os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NO = ("Photorealistic, high-end commercial photography, natural skin texture, crisp fabric and material detail, "
      "no text, no letters, no watermark, no logos added, no frames, no collage.")
KEEP = {
    'obj': ("Use the EXACT product from the reference image: identical shape, colour, material, hardware and proportions. "
            "Do not redesign it. No people, no hands."),
    'moda': ("Use the EXACT garment(s) from the reference image: identical cut, length, fabric, colour, print, buttons, "
             "trims and details. Do not redesign, recolour or add garments. The model must be a completely different woman from anyone in the "
             "reference: a new face and a different hairstyle, and no glasses unless they are the product; never reproduce the face or "
             "likeness of a real person from the reference. Elegant and natural, Spanish look. If the reference is a mirror selfie, the new photo has no phone, no mirror and no selfie pose."),
    'joya': ("Use the EXACT piece(s) of jewellery from the reference image: identical design, metal colour, stones, chain "
             "and proportions. Do not redesign or add elements. Remove any price tags, hands holding cards or text."),
    'obrador': ("Use the EXACT cake / pastry from the reference image: identical shape, decoration, colours, toppings and "
                "proportions, so a customer recognises it. Do not invent other decorations. Remove any text, stickers or logos."),
    'deco': ("Use the EXACT ceramic pieces from the reference image: identical shapes, glaze colours, hand-painted patterns "
             "and proportions. Do not redesign or add patterns. Remove any price signs or text."),
}


def ref(slug, n):
    return '%s/src/l31/%s/%02d.jpg' % (L31, slug, n) if isinstance(n, int) else n


def job(slug, iid, refs, size, prompt, niche, res='2K'):
    return {'out': '%s/ai/%s/%s.jpg' % (L31, slug, iid), 'refs': [ref(slug, r) for r in refs], 'size': size, 'res': res,
            'model': 'gemini-3-pro-image-preview', 'prompt': KEEP[niche] + ' ' + prompt + ' ' + NO, 'mid': prompt, 'nk': niche}


MODEL = {}


def studio_moda(slug, iid, n, garment, bg, extra=''):
    extra = (extra + ' ' + MODEL.get(slug, '')).strip()
    return job(slug, iid, [n], '4:5',
               f"E-commerce product photo for a luxury boutique: a model wearing {garment} from the reference, standing "
               f"naturally, framed from just above the lips (face cropped at the mouth) down to the shoes so the whole outfit is "
               f"visible, centred, on a seamless {bg} studio background with a soft natural floor shadow, soft diffused "
               f"daylight from the left. {extra}", 'moda')


def build(slug, niche, bg, hero, prods, pdp, look, cats, banner, city='', grid=None):
    """hero=(refs, prompt) · prods=[(ref, desc)]×5 (p1..p5) · pdp=(desc_p1, x1_prompt, x2_prompt, x3_prompt)
    look=(refs, prompt) · cats=[(refs, prompt)]×4 · banner=(refs, prompt)"""
    J = [job(slug, 'hero', hero[0], '16:9', hero[1] + ' One single continuous photograph, never a split screen, diptych, panel or collage. The subject stands in the right third of the frame and the same scene continues to the left, softly out of focus and calm, with room for a headline. Wide editorial campaign image, cinematic natural light.', niche)]
    for k, pr in enumerate(prods):
        r, d = pr[0], pr[1]
        if len(pr) > 2 and pr[2] == 'obj':
            J.append(job(slug, 'p%d' % (k + 1), [r], '4:5', f"Luxury e-commerce product photo of {d} from the reference, alone, centred, on a seamless {bg} background with a soft natural shadow, soft studio light, crisp detail. Remove any readable brand logo or text from the product.", 'obj'))
        elif niche == 'moda':
            J.append(studio_moda(slug, 'p%d' % (k + 1), r, d, bg))
        elif niche == 'joya':
            J.append(job(slug, 'p%d' % (k + 1), [r], '4:5', f"Luxury e-commerce jewellery photo of {d} from the reference, alone, centred, on a seamless {bg} background with a soft shadow and a subtle reflection, soft studio light, macro sharpness, every detail and stone visible.", niche))
        elif niche == 'obrador':
            J.append(job(slug, 'p%d' % (k + 1), [r], '4:5', f"Appetising e-commerce photo of {d} from the reference, alone on a simple cake stand or plate, centred, on a seamless {bg} background, soft window light from the left, slight three-quarter top angle, crisp detail, mouth-watering.", niche))
        else:
            J.append(job(slug, 'p%d' % (k + 1), [r], '4:5', f"E-commerce product photo of {d} from the reference, centred on a seamless {bg} background with a soft natural shadow, soft daylight, crisp detail of the glaze and hand-painted pattern.", niche))
    J.append(job(slug, 'x1', [prods[0][0]], '3:4', pdp[0], niche))
    J.append(job(slug, 'x2', [prods[0][0]], '4:5', pdp[1], niche))
    J.append(job(slug, 'x3', [prods[0][0]], '4:5', pdp[2], niche))
    J.append(job(slug, 'look', look[0], '4:5', look[1], niche))
    for k, (r, p) in enumerate(cats):
        J.append(job(slug, 'l%d' % (k + 1), r, '4:5', p, niche))
    J.append(job(slug, 'l5', banner[0], '16:9', banner[1] + ' Wide banner composition, inviting.' + ('' if re.search(r'\b(a woman|a man|a model|models|people|a person|hands?)\b', banner[1]) else ' No people at all.'), niche))
    return to_grid(slug, J, niche) if (GRID if grid is None else grid) else J


# ---------------- rejillas: 4 fotos por llamada (probado el 4/11/2026 con brilla-fashion) ----------------
# 15 fotos en 6 llamadas: hero, l5 y look sueltas; ficha (p1, x1, x2, x3: el mismo producto), productos (p2–p5)
# y categorías (l1–l4) en rejillas 2x2 a 2K. Cada trozo sale de ~910x1140 y gen.py publica a 1100 px como máximo.
GRID = False   # False = 15 llamadas · True (o 2) = rejillas 2x2 · 3 = una rejilla 3x3 a 4K + categorías 2x2 (en prueba)
GROUPS = [('ficha', ['p1', 'x1', 'x2', 'x3']), ('productos', ['p2', 'p3', 'p4', 'p5']), ('categorias', ['l1', 'l2', 'l3', 'l4'])]
GROUPS3 = [('todo', ['p1', 'x1', 'x2', 'x3', 'p2', 'p3', 'p4', 'p5', 'look']), ('categorias', ['l1', 'l2', 'l3', 'l4'])]
POS = {4: ['top-left', 'top-right', 'bottom-left', 'bottom-right'],
       9: ['top-left', 'top-centre', 'top-right', 'middle-left', 'centre', 'middle-right', 'bottom-left', 'bottom-centre', 'bottom-right']}
NO_G = ("Photorealistic, high-end commercial photography, natural skin texture, crisp fabric and material detail, "
        "no text, no letters, no watermark, no logos added.")


def grid_job(slug, name, panels, niche, res='2K'):
    ids = [os.path.basename(j['out'])[:-4] for j in panels]; n = len(panels); side = 3 if n == 9 else 2
    refs = []
    for j in panels:
        for r in j['refs']:
            if r not in refs:
                refs.append(r)
    word = {4: 'FOUR', 9: 'NINE'}[n]
    s = (f"A {side}x{side} grid of {word} separate, independent photographs of identical size, each with a 4:5 vertical frame, "
         "separated by perfectly straight thin pure black (#000000) gutters, about 1.5% of the image width, with no outer border. "
         "Every panel is a complete photo on its own (nothing crosses the gutters). ")
    if len(refs) == 1:
        s += ("All panels show the SAME product from the reference, identical in every panel. Rules for every panel: "
              + KEEP[niche] + " If there is a model, it is the same model in every panel. ")
    else:
        s += ("Each panel uses ONLY the reference image(s) named for it; never swap or mix items between panels. "
              "Panels that name the same reference show the same item, identical. Rules for every panel: "
              + KEEP[niche].replace('from the reference image', "from that panel's own reference image") + ' ')
        if niche == 'moda':
            s += ("Never copy a reference photo: every panel has a new pose and a new setting, and any person in it has a different face, "
                  "a different hair colour and a different hairstyle from the person in the reference. ")
    for k, j in enumerate(panels):
        mid = re.sub(r"^Category photo '[^']*':\s*", '', j['mid']).strip()
        if j['nk'] == 'obj' and niche != 'obj':
            mid += ' Product only, no people, no hands.'
        own = '' if len(refs) == 1 else ', from ' + ' and '.join('reference image %d' % (refs.index(r) + 1) for r in j['refs'])
        s += 'Panel %d (%s)%s: %s ' % (k + 1, POS[n][k], own, mid)
    return {'out': '%s/ai/%s/_grid_%s.jpg' % (L31, slug, name), 'refs': refs, 'size': '4:5', 'res': res,
            'model': 'gemini-3-pro-image-preview', 'prompt': s + NO_G, 'split': ids}


def to_grid(slug, J, niche):
    by = {os.path.basename(j['out'])[:-4]: j for j in J}
    if GRID == 3:
        return [by['hero'], by['l5'], grid_job(slug, 'todo', [by[i] for i in GROUPS3[0][1]], niche, '4K'),
                grid_job(slug, 'categorias', [by[i] for i in GROUPS3[1][1]], niche)]
    return [by['hero'], by['l5'], by['look']] + [grid_job(slug, n, [by[i] for i in ids], niche) for n, ids in GROUPS]
