"""VSL v4: guion de edición. Subtítulos de todo lo que dice (lo importante, con fondo blanco),
escenas de monigotes cuando no sale Chris y el recorrido del calendario de /book.
uso: python3 mkspec4.py words.json spec4.json"""
import json, re, sys, unicodedata

W = json.load(open(sys.argv[1]))
VOICE = 223.32          # fin de la voz
OUTRO = 4.5             # segundos de más al final para acabar el recorrido del calendario
DUR = VOICE + OUTRO


def norm(s):
    s = unicodedata.normalize('NFKD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9%]', '', s)


NW = [norm(x[0]) for x in W]


def idx(phrase, after=0.0):
    toks = [norm(t) for t in phrase.split()]
    for i in range(len(W)):
        if W[i][1] < after - 0.01:
            continue
        if NW[i:i + len(toks)] == toks:
            return i, i + len(toks) - 1
    raise SystemExit(f'no encuentro: {phrase!r} después de {after}')


def st(p, after=0.0): return W[idx(p, after)[0]][1]


def ep(p, pad, after=0.0):
    """Fin de una escena: el final de la frase más un respiro, pero sin pisar la frase siguiente."""
    e = W[idx(p, after)[1]][2]
    nxt = min([w[1] for w in W if w[1] >= e - 0.02] or [VOICE])
    return min(e + pad, max(e, nxt - 0.04))

def en(p, after=0.0): return W[idx(p, after)[1]][2]


# ---------- 1. Partes importantes (fondo blanco) ----------
KEYS = ["abrir un nuevo local", "sino en internet", "Christian Silva", "más de seis años",
        "solamente vende a personas que pasan por esa calle", "no tiene alquiler", "las 24 horas del día",
        "365 días del año", "cualquiera en España", "sin límite de crecimiento", "descaradamente más baja",
        "Yo ya tengo web y no vende", "estas tres razones", "tal cual está en la tienda física",
        "readaptación completa de la oferta", "no está conectada con el día a día", "el más grave de todos",
        "la abren y esperan", "un polígono sin cartel", "No entra absolutamente nadie",
        "el problema nunca fue lo online", "una buena noticia", "Un producto que vende",
        "una marca que en tu zona ya conocen", "evitamos los tres errores", "montamos tu tienda completa",
        "todo el stock conectado en tiempo real", "en tan solo 15 días", "20-30% de las ventas",
        "muy poquita cosa", "replicamos y escalamos", "el más rentable de tu negocio",
        "no te puedo prometer ventas", "garantizamos por contrato", "triplicar el coste",
        "trabajamos gratis hasta conseguirlo", "esto no es para todo el mundo", "más de 30.000 euros al mes",
        "reunión totalmente gratuita", "te llevarás el diagnóstico igual", "elige día y hora"]
key = [False] * len(W)
brk = set()            # cortes obligados (índice de la palabra que empieza subtítulo)
last = 0.0
for k in KEYS:
    a, b = idx(k, last)
    last = W[a][1]
    for i in range(a, b + 1): key[i] = True
    brk.add(a); brk.add(b + 1)

# ---------- 2. Subtítulos: una línea, 4 palabras como mucho ----------
WEAK = {"de", "del", "la", "las", "el", "los", "un", "una", "y", "e", "o", "a", "al", "en", "con", "por", "para", "que",
        "su", "tu", "mi", "se", "lo", "es", "no", "me", "te", "si", "pero", "sino", "como", "más", "muy", "ya"}
MAXW, MAXC = 4, 26
chunks, cur = [], []


def flush():
    global cur
    if cur: chunks.append(cur); cur = []


for i, (w, s, e) in enumerate(W):
    if i in brk: flush()
    if cur:
        txt = ' '.join(W[j][0] for j in cur)
        gap = s - W[cur[-1]][2]
        if len(cur) >= MAXW or len(txt) + 1 + len(w) > MAXC or gap > 0.45 or key[i] != key[cur[0]]:
            flush()
    cur.append(i)
    if re.search(r'[.,;:?!]$', w): flush()
flush()
# no dejar una palabra floja sola al final de un subtítulo si cabe en el siguiente
for a, b in zip(chunks, chunks[1:]):
    if len(a) > 1 and norm(W[a[-1]][0]) in WEAK and not re.search(r'[.,;:?!]$', W[a[-1]][0]) \
            and key[a[-1]] == key[b[0]] and len(b) < MAXW and a[-1] + 1 not in brk \
            and len(' '.join(W[j][0] for j in b)) + len(W[a[-1]][0]) + 1 <= MAXC:
        b.insert(0, a.pop())
# palabras sueltas: se juntan con el subtítulo de al lado o se reparte
def L(c): return len(' '.join(W[j][0] for j in c))
def endp(c): return bool(re.search(r'[.,;:?!]$', W[c[-1]][0]))
ch = [c for c in chunks if c]
i = 0
while i < len(ch):
    c = ch[i]
    if len(c) == 1:
        prev = ch[i - 1] if i else None
        nxt = ch[i + 1] if i + 1 < len(ch) else None
        gp = W[c[0]][1] - W[prev[-1]][2] if prev else 9
        gn = W[nxt[0]][1] - W[c[-1]][2] if nxt else 9
        samep = prev and key[prev[0]] == key[c[0]] and not endp(prev) and gp < 0.45
        if samep and len(prev) <= 4 and L(prev) + 1 + L(c) <= 28:
            prev.extend(c); ch.pop(i); continue
        if samep and len(prev) >= 3:
            c.insert(0, prev.pop()); i += 1; continue
        if nxt and not endp(c) and gn < 0.45 and len(nxt) <= 4 and L(nxt) + 1 + L(c) <= 30 and (key[nxt[0]] or not key[c[0]]):
            if key[nxt[0]]: key[c[0]] = True
            nxt.insert(0, c[0]); ch.pop(i); continue
        if prev and not endp(prev) and gp < 0.45 and len(prev) <= 4 and L(prev) + 1 + L(c) <= 30 and key[prev[0]]:
            key[c[0]] = True; prev.extend(c); ch.pop(i); continue
    i += 1
chunks = ch
SUB = []
for n, c in enumerate(chunks):
    t0 = W[c[0]][1] - 0.04
    nxt = W[chunks[n + 1][0]][1] - 0.04 if n + 1 < len(chunks) else VOICE
    t1 = nxt if nxt - W[c[-1]][2] < 0.7 else W[c[-1]][2] + 0.35
    words = [[re.sub(r'[.,;:]+$', '', W[j][0]), round(W[j][1], 2)] for j in c]
    SUB.append(dict(t0=round(max(0, t0), 2), t1=round(t1, 2), w=words, key=key[c[0]]))

# ---------- 3. Escenas de monigotes (pantalla completa, corte seco) ----------
CUT = []


def cut(cid, t0, t1, dark=False):
    CUT.append(dict(id=cid, t0=round(t0, 2), t1=round(t1, 2), dark=dark))


cut('c1a', st('un nuevo alquiler'), st('y aún así'))
cut('c1b', st('y aún así'), ep('un horario concreto', 0.25))
cut('c2', st('piensa en una tienda online'), st('y le vende a cualquiera'), dark=True)
cut('c3', st('y le vende a cualquiera'), ep('en su mano', 0.3))
cut('c4', st('se sube el catálogo'), ep('especificaciones del producto', 0.2))
cut('c5', st('la tienda online no está conectada'), ep('siendo un lío', 0.3))
cut('c6', st('una tienda online sin anuncios'), ep('absolutamente nadie', 0.3))
cut('c7', st('un producto que vende'), ep('ya conocen', 0.3))
cut('c8a', st('montamos tu tienda completa'), st('envíos a toda españa'))
cut('c8b', st('envíos a toda españa'), st('y en tan solo'))
cut('c9', st('lanzamos los primeros anuncios'), ep('confían en la marca', 0.3))
cut('c10', st('contarnos cómo funciona'), ep('cada uno de ellos', 0.1))
cut('c11', st('replicamos y escalamos'), ep('de tu negocio', 0.3, st('replicamos y escalamos')))
cut('c12', st('garantizamos por contrato'), ep('hasta conseguirlo', 0.35))
cut('c13', st('vendes algo que se puede enviar'), st('aquí abajo tienes el calendario'))
cut('c15', st('vende por toda españa', st('así que si quieres')), st('elige día y hora'))

# sin destellos: si entre dos escenas queda menos de 1 s de Chris, la primera aguanta hasta la siguiente
for a_, b_ in zip(CUT, CUT[1:]):
    if 0 < b_['t0'] - a_['t1'] < 1.0:
        a_['t1'] = b_['t0']

# ---------- 4. Calendario de /book ----------
CAL = [dict(kind='cal1', t0=round(st('aquí abajo tienes el calendario'), 2), t1=round(en('decidimos juntos') + 0.2, 2)),
       dict(kind='cal2', t0=round(st('elige día y hora'), 2), t1=round(DUR, 2))]

# ---------- 5. Lo demás ----------
FLOAT = [dict(kind='phone', t0=round(st('no debería'), 2), t1=round(en('sino en internet') + 0.08, 2)),
         dict(kind='n15', t0=round(st('en tan solo 15 días'), 2), t1=round(st('lanzamos los primeros anuncios') - 0.05, 2))]
BW = [[round(st('yo ya tengo web'), 2), round(en('en la tienda online', st('nadie entraba')) + 0.1, 2)]]
TOPNUM = [dict(t0=round(st('si facturas más de'), 2), t1=round(st('vendes algo que se puede enviar') - 0.05, 2))]

cuts = [0.0]
for i in range(1, len(W)):
    gap = W[i][1] - W[i - 1][2]
    if W[i - 1][0][-1:] in '.,?!:' or gap > 0.18:
        if W[i][1] - cuts[-1] > 2.0:
            cuts.append(round(W[i][1] - 0.04, 2))

S = dict(dur=DUR, voice=VOICE, sub=SUB, cut=CUT, cal=CAL, float=FLOAT, bw=BW, topnum=TOPNUM, cuts=cuts)
json.dump(S, open(sys.argv[2], 'w'), ensure_ascii=False, indent=0)
print(len(SUB), 'subtítulos,', sum(1 for s in SUB if s['key']), 'destacados,', len(CUT), 'escenas')
for c in CUT + CAL: print('%-5s %6.2f-%6.2f  %.1f s' % (c.get('id', c.get('kind')), c['t0'], c['t1'], c['t1'] - c['t0']))
if '-v' in sys.argv:
    for s in SUB: print('%6.2f-%6.2f %s %s' % (s['t0'], s['t1'], '■' if s['key'] else ' ', ' '.join(w[0] for w in s['w'])))
