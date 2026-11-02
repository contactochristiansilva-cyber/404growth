# Teleprompter de cada vídeo: mismas palabras y mismos tiempos que su pizarra.
import json, re, sys, os, importlib
from common import RATE, GAP, TOK
HERE = os.path.dirname(os.path.abspath(__file__))
INTRO = {
 1: 'Antes de nuestra llamada, empieza por aquí. Si tu tienda ya va bien, este vídeo es para ti. Porque cuando una tienda va bien, tarde o temprano aparece la misma idea: abrir otra. Otro local, en otro barrio o en otra ciudad. Antes de firmar nada, haz conmigo las cuentas.',
 2: '«No tengo tiempo, ya tengo bastante con la tienda.» Si es lo que piensas, lo entiendo: abres, cierras, haces caja, hablas con proveedores… No te sobra ni una hora. Así que te voy a enseñar exactamente qué te toca a ti y qué nos toca a nosotros.',
 3: 'Si te pierdes cada vez que alguien te habla de plataformas, pasarelas o plugins, tranquilo: no te hace falta saber nada de eso. Te voy a enseñar un pedido de principio a fin, como si lo vieras por dentro. Y vas a ver que se parece mucho más a tu tienda de lo que crees.',
 4: 'Hay una idea que hace perder mucho dinero: «monto la web y ya vendrán». No vienen. Una tienda online sin nadie que la empuje es un local precioso en una calle por la que no pasa nadie. Te enseño de dónde salen de verdad los clientes.',
 5: '«Es mucho dinero. ¿Y si no funciona?» Es la pregunta más sensata que me puedes hacer. Así que vamos a contestarla bien: qué pagas, qué incluye, qué va aparte y cómo se recupera. Sin cifras mágicas.',
 6: 'Si ya tienes web y no te entra ni un pedido, no eres el único. Casi siempre es por las mismas cinco cosas, y casi nunca es culpa del producto. Te las enseño, y cómo se arreglan.',
 7: 'Si alguna vez te hicieron una web y luego nadie te cogía el teléfono, entiendo que desconfíes. «Me la montan y me dejan tirado.» Te enseño qué pasa exactamente del día 15 en adelante.',
 8: '«Lo mío no se puede vender por internet.» Es una de las dudas más normales. Y a veces hay parte de razón, pero casi nunca del todo. Te enseño qué funciona mejor online y qué hacer si lo tuyo es delicado o grande.'}
COUNT = 3.0      # cuenta atrás; el pitido suena al acabar
SWITCH = 1.5     # entre la última palabra de la intro y el arranque de la pizarra

def board_words(v):
    """[(t, palabra, nº de frase)] con los tiempos exactos de la pizarra."""
    if v == 1:
        s = open(os.path.join(HERE, '..', 'board.html')).read()
        L = json.loads(re.search(r"var LINES=(\[.*?\]);", s, re.S).group(1).replace("'", '"'))
        out = []
        for i, (t0, txt) in enumerate(L):
            for k, w in enumerate(txt.split()): out.append((round(t0 + k / RATE, 3), w, i))
        return out, 119.0, [l[1] for l in L if l[1]]
    mod = importlib.import_module(f'v{v}'); res = getattr(mod, f'v{v}')()
    lines = res[2] if len(res) == 4 else res[2]
    lines = res[3]
    t = 0.6; out = []
    for i, ln in enumerate(lines):
        for tk in TOK.findall(ln):
            if tk.startswith('{') and tk.endswith('}'):
                for part in tk[1:-1].split(','):
                    part = part.strip()
                    if part.startswith('p:'): t += float(part[2:])
                continue
            out.append((round(t, 3), tk, i)); t += 1 / RATE
        t += GAP
    dur = round(t + 2.2, 2)
    texts = [' '.join(tk for tk in TOK.findall(ln) if not tk.startswith('{')) for ln in lines]
    return out, dur, texts

def plan(v):
    bw, bdur, btexts = board_words(v)
    # intro en frases
    sents = re.findall(r'[^.?!…»]+(?:[.?!…]+»?|»)?', INTRO[v])
    sents = [s.strip() for s in sents if s.strip()]
    blocks = []; t = COUNT + 0.35
    for s in sents:
        ws = []
        for w in s.split(): ws.append([round(t, 3), w]); t += 1 / RATE
        t += 0.35
        blocks.append({'k': 'intro', 'w': ws})
    intro_end = t
    blocks.append({'k': 'mark', 'w': [[round(intro_end + 0.1, 3), '50/50 · empieza la pizarra']]})
    TB = round(intro_end + SWITCH, 2)
    cur = {}
    for tt, w, i in bw: cur.setdefault(i, []).append([round(TB + tt, 3), w])
    for i in sorted(cur): blocks.append({'k': 'board', 'w': cur[i]})
    total = round(TB + bdur, 2)
    return {'v': v, 'blocks': blocks, 'TB': TB, 'tb_after_beep': round(TB - COUNT, 2), 'total': total, 'bdur': bdur,
            'intro': INTRO[v], 'btexts': btexts}

if __name__ == '__main__':
    for v in range(1, 9):
        p = plan(v)
        json.dump(p, open(os.path.join(HERE, f'tp{v}.json'), 'w'), ensure_ascii=False)
        print(v, 'pizarra a', p['tb_after_beep'], 's del pitido · total', p['total'])
