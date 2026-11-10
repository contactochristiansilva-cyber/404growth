# JS para la pestaña de Flow con los mensajes de una tienda, comprimidos con el diccionario TOK (se guarda una vez en localStorage.__tok)
import json, sys, re, glob
from mkjobs import COMMON, OBJ, wear
TOK = [wear('woman'), wear('man'), OBJ, COMMON,
       'Genera 5 imágenes separadas con Nano Banana 2.1, cada una en su formato y con su referencia (las referencias están adjuntas). Usa los textos tal cual, sin reescribirlos ni añadir nada. ',
       'E-commerce product photo for a fashion boutique: a model wearing ',
       ' from the reference, standing naturally, framed from just above the lips (face cropped at the mouth) down to the shoes so the whole outfit is visible, centred, on a seamless warm light (',
       ') studio background with a soft natural floor shadow, soft diffused daylight from the left.',
       'One single continuous photograph, never a split screen, diptych, panel or collage. The subject stands in the right third of the frame and the same scene continues to the left, softly out of focus and calm, with room for a headline. Wide editorial campaign image, cinematic natural light.',
       ', inspired by the reference, photographed like a design magazine, beautiful natural light, inviting and tidy. One single continuous photograph, never a split screen or collage.',
       'Luxury jewellery e-commerce photo of ', ' from the reference, centred on a seamless ivory (',
       ') background with a soft natural shadow, the whole piece visible and large in the frame, macro-sharp metal and stone detail, soft diffused daylight.',
       'Beauty e-commerce product photo of ', ' from the reference, centred on a seamless soft blush (',
       ') background with a couple of natural props (a petal, a pale stone) and a soft shadow, the whole product visible and large in the frame, crisp glass and material detail.',
       'Lifestyle fashion photo: a model wearing ', ' from the reference, candid and relaxed in a sunny street of ',
       ', Spain, natural light, framed from the knees up, editorial, shallow depth of field.',
       ', like in the reference, soft natural light, editorial, warm and inviting, shallow depth of field.',
       'Footwear e-commerce photo of ', ' from the reference, a pair shown at a three-quarter angle, centred and large in the frame on a seamless light (',
       ') background with a soft floor shadow, crisp leather, suede and sole detail.',
       ' from the reference, three-quarter front view, centred and large in the frame on a seamless light (', ') background with a soft shadow, crisp embroidery and fabric detail.',
       'E-commerce product photo of ', ') background with a soft shadow, crisp detail.', 'Luxury campaign still life of ',
       ' from the reference, arranged on pale travertine stone with soft late-afternoon sunlight and delicate shadows, the piece filling the centre-right of the frame, warm ivory tones, macro-sharp detail. One single continuous photograph.',
       'Luxury beauty campaign still life of ', ' from the reference. The product stands in the right third of the frame and the scene continues to the left, softly out of focus and calm, with room for a headline. Warm cinematic light, rich textures. One single continuous photograph, never a split screen or collage.',
       'Wide interior photo: ', 'A stylish Spanish woman in her thirties wearing ', 'A stylish Spanish man in his thirties wearing ', ' from the reference, walking at ',
       'Lifestyle photo: ', ', aplica la REGLA ', ' (formato 3:4, referencia ', ' (formato 16:9, referencia ', ' (formato 4:3, referencia ']
TOK = sorted(set(TOK), key=len, reverse=True)
def comp(t):
    for k, p in enumerate(TOK):
        t = t.replace(p, f'§{k:02d}')
    return t
if __name__ == '__main__':
    if sys.argv[1] == '--tok':
        print('localStorage.__tok=%s;window.__X=t=>t.replace(/\\u00a7(\\d\\d)/g,(m,k)=>JSON.parse(localStorage.__tok)[+k]);"tok "+JSON.parse(localStorage.__tok).length' % json.dumps(json.dumps(TOK, ensure_ascii=False), ensure_ascii=False))
    else:
        s = sys.argv[1]; d = json.load(open(f'flow/{s}.json'))
        M = [dict(refs=m['refs'], text=comp(m['text'])) for m in d['msgs']]
        for m, o in zip(M, d['msgs']):
            assert '§' not in o['text']
        K = {k: comp(v) if False else v for k, v in d['K'].items()}
        print('if(!window.__put)eval(localStorage.__fc);localStorage.__cur=%s;window.__X=t=>t.replace(/\\u00a7(\\d\\d)/g,(m,k)=>JSON.parse(localStorage.__tok)[+k]);window.__SLUG=%s;window.__K=%s;window.__M=%s.map(m=>({refs:m.refs,text:__X(m.text)}));"ok "+__M.map(m=>m.text.length)'
              % (json.dumps(s), json.dumps(s), json.dumps(K, ensure_ascii=False), json.dumps(M, ensure_ascii=False)))
