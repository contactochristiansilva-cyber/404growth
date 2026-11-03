"""Prompt building blocks for lote 31 (Apimart / Nano Banana Pro). Every image starts from the shop's real product photos."""
import os
L31 = os.environ.get('L31', os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NO = ("Photorealistic, high-end commercial photography, natural skin texture, crisp fabric and material detail, "
      "no text, no letters, no watermark, no logos added, no frames, no collage.")
KEEP = {
    'obj': ("Use the EXACT product from the reference image: identical shape, colour, material, hardware and proportions. "
            "Do not redesign it. No people, no hands."),
    'moda': ("Use the EXACT garment(s) from the reference image: identical cut, length, fabric, colour, print, buttons, "
             "trims and details. Do not redesign, recolour or add garments. The model must be a different woman from the "
             "person in the reference (new face), elegant and natural, Spanish look. If the reference is a mirror selfie, the new photo has no phone, no mirror and no selfie pose."),
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
            'model': 'gemini-3-pro-image-preview', 'prompt': KEEP[niche] + ' ' + prompt + ' ' + NO}


MODEL = {}


def studio_moda(slug, iid, n, garment, bg, extra=''):
    extra = (extra + ' ' + MODEL.get(slug, '')).strip()
    return job(slug, iid, [n], '4:5',
               f"E-commerce product photo for a luxury boutique: a model wearing {garment} from the reference, standing "
               f"naturally, framed from just above the lips (face cropped at the mouth) down to the shoes so the whole outfit is "
               f"visible, centred, on a seamless {bg} studio background with a soft natural floor shadow, soft diffused "
               f"daylight from the left. {extra}", 'moda')


def build(slug, niche, bg, hero, prods, pdp, look, cats, banner, city=''):
    """hero=(refs, prompt) · prods=[(ref, desc)]×5 (p1..p5) · pdp=(desc_p1, x1_prompt, x2_prompt, x3_prompt)
    look=(refs, prompt) · cats=[(refs, prompt)]×4 · banner=(refs, prompt)"""
    J = [job(slug, 'hero', hero[0], '16:9', hero[1] + ' The subject sits in the right half of the frame; the left 45% is calm, softly blurred background for a headline. Wide editorial campaign image, cinematic natural light.', niche)]
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
    J.append(job(slug, 'l5', banner[0], '16:9', banner[1] + ' Wide banner composition, inviting, no people unless described.', niche))
    return J
