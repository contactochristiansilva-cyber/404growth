"""Genera spec.json del VSL v3 a partir de words.json (tiempos de Parakeet)."""
import json, re, sys, unicodedata

W = json.load(open(sys.argv[1]))
DUR = 223.32


def norm(s):
    s = unicodedata.normalize('NFKD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9%]', '', s)


NW = [norm(x[0]) for x in W]


def find(phrase, after=0.0):
    """(inicio, fin) de la primera aparición de la frase a partir de 'after'."""
    toks = [norm(t) for t in phrase.split()]
    for i in range(len(W)):
        if W[i][1] < after - 0.01:
            continue
        if NW[i:i + len(toks)] == toks:
            return W[i][1], W[i + len(toks) - 1][2]
    raise SystemExit(f'no encuentro: {phrase!r} después de {after}')


def st(phrase, after=0.0):
    return find(phrase, after)[0]


def en(phrase, after=0.0):
    return find(phrase, after)[1]


S = {'side': [], 'slide': [], 'split': [], 'float': [], 'sfx': []}


def side(t0, t1, side_, f, k):
    S['side'].append(dict(t0=round(t0 - 0.06, 2), t1=round(t1, 2), side=side_, f=f, k=k))
    S['sfx'].append(dict(t=round(t0 - 0.06, 2), s='pop'))


def slide(t0, t1, kind, **kw):
    S['slide'].append(dict(t0=round(t0, 2), t1=round(t1, 2), kind=kind, **{k: v for k, v in kw.items()}))
    S['sfx'].append(dict(t=round(t0 - 0.04, 2), s='whoosh'))


def split(t0, t1, kind, **kw):
    S['split'].append(dict(t0=round(t0, 2), t1=round(t1, 2), kind=kind, **kw))
    S['sfx'].append(dict(t=round(t0 - 0.04, 2), s='card'))


def flt(t0, t1, kind):
    S['float'].append(dict(t0=round(t0, 2), t1=round(t1, 2), kind=kind))
    S['sfx'].append(dict(t=round(t0, 2), s='float'))


# 0:00 gancho
side(st('abrir un nuevo local'), en('abrir un nuevo local') + 0.5, 'l', 'abrir un', 'nuevo local')
flt(st('no debería'), en('sino en internet') + 0.9, 'phone')
side(st('sino en internet'), en('sino en internet') + 0.8, 'r', 'no en otra calle,', 'en internet.')
# 0:10 presentación
side(st('soy cristian silva'), en('soy cristian silva') + 0.4, 'r', 'soy', 'Christian Silva')
side(st('más de seis años'), en('vertical online'), 'l', 'más de 6 años', 'en online')
# 0:20 lo que supone un local
t = st('un nuevo alquiler')
slide(t, en('en un horario concreto') + 0.3, 'local',
      a=round(st('una obra', t), 2), b=round(st('una persona más', t), 2),
      c=round(st('meses hasta', t), 2), d=round(st('esa tienda solamente', t), 2))
# 0:30 tienda online
t = st('piensa en una tienda online')
slide(t, st('y le vende a cualquiera') - 0.02, 'nums',
      a=round(st('no tiene alquiler', t), 2), b=round(st('las 24 horas', t), 2), c=round(st('365 días', t), 2))
t = st('y le vende a cualquiera')
split(t, en('en su mano') + 0.4, 'map', a=round(st('cualquiera en españa', t), 2))
side(st('mismo producto'), en('sin límite de crecimiento') + 0.3, 'r', 'misma marca,', 'sin límite')
side(st('descaradamente'), en('descaradamente más baja') + 0.4, 'l', 'inversión', 'mucho más baja')
# 0:46 objeciones
side(st('yo ya tengo web'), en('y no vende') + 0.3, 'r', '«ya tengo web', 'y no vende»')
side(st('nadie entraba'), en('en la tienda online', st('nadie entraba')) + 0.3, 'l', '«nadie', 'entraba»')
t = st('por una de estas tres razones')
slide(t, en('tres razones') + 0.9, 'three', n=0)
side(st('se sube el catálogo'), en('tal cual está') + 0.4, 'r', 'el catálogo,', 'tal cual')
side(st('en una pantalla'), en('especificaciones del producto') + 0.2, 'l', 'en una pantalla,', 'nadie te lo explica')
side(st('readaptación completa'), en('para la tienda online', st('readaptación')) + 0.2, 'r', 'readaptación', 'completa')
t = st('la tienda online no está conectada')
split(t, en('termina siendo un lío') + 0.4, 'broken',
      a=round(st('el stock', t), 2), b=round(st('los envíos', t), 2), c=round(st('los cobros', t), 2), d=round(st('un lío', t), 2))
side(st('el más grave'), en('el más grave de todos') + 0.4, 'r', 'el más', 'grave')
side(st('la abren y esperan'), en('la abren y esperan') + 0.4, 'l', 'la abren', 'y esperan')
t = st('una tienda online sin anuncios')
slide(t, en('absolutamente nadie') + 0.4, 'poligono', a=round(st('lo mismo que', t), 2), b=round(st('no entra', t), 2))
side(st('el problema nunca fue'), en('lo online', st('el problema nunca fue')) + 0.5, 'r', 'el problema', 'nunca fue lo online')
side(st('cuáles fueron los métodos'), en('y entonces vender') + 0.3, 'l', 'el método', 'para llenarla de tráfico')
side(st('una buena noticia'), en('una buena noticia') + 0.5, 'l', 'una', 'buena noticia')
t = st('un producto que vende')
slide(t, en('en tu zona ya conocen') + 0.4, 'assets',
      a=round(st('gente real', t), 2), b=round(st('que repite', t), 2), c=round(st('además de fotos', t), 2),
      d=round(st('seguidores', t), 2), e=round(st('una marca', t), 2))
side(st('súper específico'), en('súper específico') + 0.4, 'r', 'lo que', 'hacemos')
side(st('evitamos los tres errores'), en('vengo comentando') + 0.3, 'l', 'sin los', 'tres errores')
t = st('montamos tu tienda completa')
split(t, st('y en tan solo') - 0.05, 'store',
      a=round(st('cobros por tarjeta', t), 2), b=round(st('envíos a toda españa', t), 2),
      c=round(st('recogida en tienda', t), 2), d=round(st('todo el stock', t), 2))
flt(st('en tan solo 15 días'), st('lanzamos los primeros anuncios') - 0.05, 'n15')
t = st('lanzamos los primeros anuncios')
slide(t, en('ya confían en la marca') + 0.4, 'bars', a=round(st('email marketing', t), 2), b=round(st('20-30%', t), 2))
side(st('muy poquita cosa'), en('muy poquita cosa') + 0.4, 'r', 'por tu parte,', 'muy poquita cosa')
side(st('cómo funciona tu marca'), en('de manera online') + 0.3, 'l', 'tu marca y', 'tus productos')
side(st('replicamos y escalamos'), en('replicamos y escalamos') + 0.5, 'r', 'replicamos', 'y escalamos')
side(st('el más rentable'), en('de tu negocio', st('el más rentable')) + 0.3, 'l', 'el canal', 'más rentable')
side(st('no te puedo prometer ventas'), en('prometer ventas') + 0.5, 'r', 'no te puedo', 'prometer ventas')
side(st('como garantía'), en('que tenemos', st('como garantía')) + 0.3, 'l', 'y como', 'garantía')
side(st('analizamos tu caso'), en('caso de éxito', st('analizamos tu caso')) + 0.2, 'r', 'si es un', 'caso de éxito')
t = st('garantizamos por contrato')
slide(t, en('hasta conseguirlo', t) + 0.6, 'x3', a=round(st('y si no', t), 2))
t = st('esto no es para todo el mundo')
slide(t, en('no es para ti') + 0.5, 'notfor',
      a=round(st('no se puede enviar', t), 2), b=round(st('no vende lo suficiente', t), 2), c=round(st('compromiso por parte', t), 2))
t = st('si facturas más de')
slide(t, en('unión europea') + 0.4, 'fit', a=round(st('vendes algo', t), 2), b=round(st('portugal', t), 2))
side(st('reunión totalmente gratuita'), en('reunión totalmente gratuita') + 0.5, 'r', 'reunión', 'gratuita')
side(st('decidimos juntos'), en('decidimos juntos') + 0.4, 'l', 'decidimos', 'juntos')
side(st('el diagnóstico igual'), en('el diagnóstico igual') + 0.4, 'r', 'diagnóstico', 'igualmente')
side(st('jamás pasarían por tu calle'), en('jamás pasarían por tu calle') + 0.4, 'r', 'gente que jamás', 'pasaría por tu calle')
flt(st('pero que llevan'), DUR, 'cal')
side(st('elige día y hora'), DUR, 'r', 'elige', 'día y hora')

# Cortes de zoom: un plano por frase (pausas de más de 0,22 s o puntuación), alternando 1,00 y 1,12
cuts = [0.0]
for i in range(1, len(W)):
    gap = W[i][1] - W[i - 1][2]
    if W[i - 1][0][-1:] in '.,?!:' or gap > 0.18:
        if W[i][1] - cuts[-1] > 2.0:
            cuts.append(round(W[i][1] - 0.04, 2))
S['cuts'] = cuts
S['dur'] = DUR

# arreglar solapes: los textos ceden ante los gráficos y ante el texto siguiente
full = S['slide'] + S['split']
for a in S['side']:
    for b in full:
        if a['t0'] < b['t1'] and b['t0'] < a['t1']:
            if a['t0'] >= b['t0']:
                a['t0'] = round(b['t1'] + 0.05, 2)
            else:
                a['t1'] = round(b['t0'] - 0.05, 2)
S['side'] = [a for a in S['side'] if a['t1'] - a['t0'] >= 0.8]
S['side'].sort(key=lambda a: a['t0'])
for a, b in zip(S['side'], S['side'][1:]):
    if a['t1'] > b['t0'] - 0.05:
        a['t1'] = round(b['t0'] - 0.05, 2)
# comprobar solapes
for a in S['side']:
    for b in S['side']:
        if a is not b and a['t0'] < b['t0'] < a['t1']:
            print('solape texto', a['k'], '/', b['k'], a['t1'], b['t0'])
full = S['slide'] + S['split']
for a in S['side']:
    for b in full:
        if a['t0'] < b['t1'] and b['t0'] < a['t1']:
            print('texto sobre gráfico', a['k'], b['kind'])
json.dump(S, open(sys.argv[2], 'w'), ensure_ascii=False, indent=1)
print(len(S['side']), 'textos', len(S['slide']), 'gráficos', len(S['split']), 'compartidas', len(S['float']), 'flotan', len(cuts), 'planos')
