import base64, json, re, unicodedata, hashlib, collections, secrets, sys
S = '/tmp/claude-0/-home-claude/a676b6bb-0020-5a51-9455-0108b5df14a8/scratchpad/'
def norm(s):
    s = unicodedata.normalize('NFD', s); s = ''.join(c for c in s if not unicodedata.combining(c)).lower()
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()
cat = [c for c in json.load(open(S + 'intenso/cat/catalogo.json')) if c['status'] == 'Activo']
st = [p for p in json.load(open(S + 'v5/catalog.json')) if p['status'] == 'ACTIVE' and p['productType'] in ('Esenciales', 'Nicho', 'Extractos')]
by = {}
for p in st: by.setdefault(p['title'].replace('Nº', '').strip(), []).append((p['handle'], p['productType']))
LM = {'Comercial': 'Esenciales', 'Nicho': 'Nicho', 'Extracto EDP nicho': 'Extractos'}
ALIAS = {'D&G': ['dolce gabbana', 'dolce and gabbana', 'dolce y gabbana', 'dyg', 'd g'], 'YSL': ['yves saint laurent', 'saint laurent', 'ysl'],
 'Paco Rabanne': ['rabanne'], 'Rabanne': ['paco rabanne'], 'Armani': ['giorgio armani'], 'Armani Privé': ['armani', 'giorgio armani'],
 'MFK': ['maison francis kurkdjian', 'francis kurkdjian', 'kurkdjian'], 'Kilian': ['by kilian', 'kilian paris'], 'Jean Paul Gaultier': ['gaultier', 'jpg'],
 'Carolina Herrera': ['herrera', 'ch'], 'Hugo Boss': ['boss', 'hugo'], 'Bvlgari': ['bulgari'], 'Viktor&Rolf': ['viktor and rolf', 'viktor rolf', 'viktor y rolf'],
 'Zadig & Voltaire': ['zadig'], 'Mugler': ['thierry mugler'], 'Calvin Klein': ['ck'], 'Narciso Rodriguez': ['narciso'], 'Issey Miyake': ['issey'],
 'Parfums de Marly': ['pdm', 'marly', 'de marly'], 'Jo Malone': ['jo malone london'], 'Louis Vuitton': ['lv'], 'Abercrombie & Fitch': ['abercrombie'],
 'Tiffany': ['tiffany co'], 'Montblanc': ['mont blanc'], 'Frédéric Malle': ['frederic malle', 'malle'], 'Maison Crivelli': ['crivelli'],
 'Acqua di Parma': ['acqua parma'], 'Victorio & Lucchino': ['victorio lucchino', 'victorio y lucchino'], 'Estée Lauder': ['lauder']}
# words that are notes or families: a one-word key equal to them is not added (people search notes)
notes = set()
for p in st:
    m = {x['key']: x['value'] for x in p['mf']['nodes']}
    for k in ('salida', 'corazon', 'fondo', 'familia', 'grupo'):
        for n in (m.get(k) or '').split(','):
            for w in norm(n).split(): notes.add(w)
notes |= {'vanilla', 'vanille', 'oud', 'musk', 'rose', 'amber', 'ambre', 'tobacco', 'leather', 'cuir', 'iris', 'vetiver', 'santal', 'neroli', 'jasmine', 'tonka', 'black', 'white', 'gold', 'blue', 'red', 'pink', 'noir', 'intense', 'man', 'woman', 'homme', 'femme', 'sport'}
STOP = {'de','del','la','le','les','the','of','d','di','l','el','y','and','pour','for','a','an','du','des','da','en','et','eau'}
items = []   # (keys, handles)
for c in cat:
    if '·' not in c['ref']: continue
    code = c['code'].lstrip("'"); ln = LM.get(c['line'], c['line'])
    hs = [h for h, t in by.get(code, []) if t == ln] or [h for h, t in by.get(code, [])]
    name, brand = [x.strip() for x in c['ref'].rsplit('·', 1)]
    items.append((norm(name), [norm(brand)] + [norm(a) for a in ALIAS.get(brand, [])], hs[0], code, ln))
names = collections.Counter(n for n, *_ in items)
K = collections.defaultdict(list)
def add(k, h):
    if not k: return
    if re.fullmatch(r'[0-9 ]+', k): return            # nunca tapar nuestros números
    if ' ' not in k and (k in notes or len(k) < 3): return
    if h not in K[k]: K[k].append(h)
for name, brands, h, code, ln in items:
    nm = name
    # sin la marca repetida al principio ("dior homme" ya la lleva)
    add(nm, h)
    for b in brands:
        add(f'{nm} {b}', h); add(f'{b} {nm}', h)
        if nm.startswith(b + ' '): add(nm[len(b) + 1:], h) if len(nm[len(b) + 1:].split()) >= 2 else None
    w = nm.split()
    for j in range(2, len(w)):           # prefijos de 2+ palabras, solo si son únicos
        pre = ' '.join(w[:j])
        if w[j-1] in STOP or len(w[j-1]) < 3 or len(pre.replace(' ', '')) < 6: continue
        if sum(1 for n, *_ in items if n == pre or n.startswith(pre + ' ')) == 1 and pre not in names:
            add(pre, h)
            for b in brands: add(f'{pre} {b}', h); add(f'{b} {pre}', h)
# Nº5 y similares: la base sin "edp"
for name, brands, h, code, ln in items:
    m = re.match(r'^(n \d+)\b', name)
    if m and names[m.group(1)] == 0:
        for b in brands: add(f'{m.group(1)} {b}', h); add(f'{b} {m.group(1)}', h)
# variantes: 1 -> one, n 5 -> n5 / no 5 / numero 5
NW = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '7': 'seven', '9': 'nine'}
for k in list(K):
    w = k.split()
    if any(x in NW for x in w): add(' '.join(NW.get(x, x) for x in w), K[k][0])
    if 'n 5' in k:
        for v in ('n5', 'no 5', 'numero 5', 'number 5', 'nro 5'): add(k.replace('n 5', v), K[k][0])
# también sin espacios
# (sin variantes sin espacios: el índice va dentro del tema y conviene que pese poco)
salt = 'i' + secrets.token_hex(4)
H = {}
for k, hs in K.items():
    hk = base64.urlsafe_b64encode(hashlib.sha256((salt + k).encode()).digest()[:6]).decode()[:6]
    if hk in H and H[hk] != hs: print('colision', k, file=sys.stderr)
    H[hk] = hs
HL = sorted({'|'.join(hs) for hs in H.values()})
ix = {v: i for i, v in enumerate(HL)}
def b36(n):
    a = '0123456789abcdefghijklmnopqrstuvwxyz'; return a[n // 36] + a[n % 36]
blob = ''.join(hk + b36(ix['|'.join(hs)]) for hk, hs in sorted(H.items()))
out = {'s': salt, 'h': HL, 'k': blob}
json.dump(out, open('intenso-eq.json', 'w'), separators=(',', ':'))
multi = {k: hs for k, hs in K.items() if len(hs) > 1}
print('perfumes', len(items), 'claves', len(K), 'multi', len(multi), list(multi.items())[:6])
json.dump({k: hs for k, hs in K.items()}, open('claves-interno.json', 'w'), ensure_ascii=False, indent=0)
