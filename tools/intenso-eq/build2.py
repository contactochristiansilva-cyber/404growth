# Índice en claro para las sugerencias del buscador: marcas (con alias) y perfumes -> número de Intenso.
import json, re, unicodedata, collections
S = '/tmp/claude-0/-home-claude/a676b6bb-0020-5a51-9455-0108b5df14a8/scratchpad/'
def norm(s):
    s = unicodedata.normalize('NFD', s); s = ''.join(c for c in s if not unicodedata.combining(c)).lower()
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()
cat = [c for c in json.load(open(S + 'intenso/cat/catalogo.json')) if c['status'] == 'Activo']
st = [p for p in json.load(open(S + 'v5/catalog.json')) if p['status'] == 'ACTIVE' and p['productType'] in ('Esenciales', 'Nicho', 'Extractos')]
by = {}
for p in st: by.setdefault(p['title'].replace('Nº', '').strip(), []).append((p['handle'], p['productType']))
LM = {'Comercial': 'Esenciales', 'Nicho': 'Nicho', 'Extracto EDP nicho': 'Extractos'}
DISP = {'D&G': 'Dolce & Gabbana', 'YSL': 'Yves Saint Laurent', 'MFK': 'Maison Francis Kurkdjian', 'Rabanne': 'Paco Rabanne', 'Dubái': 'Dubái'}
ALIAS = {'Dolce & Gabbana': ['d&g', 'dyg', 'dolce gabbana', 'dolce y gabbana', 'dolce and gabbana'], 'Yves Saint Laurent': ['ysl', 'saint laurent'],
 'Paco Rabanne': ['rabanne'], 'Armani': ['giorgio armani'], 'Armani Privé': ['giorgio armani prive'], 'Maison Francis Kurkdjian': ['mfk', 'francis kurkdjian', 'kurkdjian'],
 'Kilian': ['by kilian'], 'Jean Paul Gaultier': ['gaultier', 'jpg'], 'Carolina Herrera': ['herrera'], 'Hugo Boss': ['boss'], 'Bvlgari': ['bulgari'],
 'Viktor&Rolf': ['viktor and rolf', 'viktor y rolf', 'viktor rolf'], 'Zadig & Voltaire': ['zadig'], 'Mugler': ['thierry mugler'], 'Calvin Klein': ['ck'],
 'Parfums de Marly': ['pdm', 'marly'], 'Louis Vuitton': ['lv'], 'Abercrombie & Fitch': ['abercrombie'], 'Montblanc': ['mont blanc'], 'Frédéric Malle': ['malle'],
 'Victorio & Lucchino': ['victorio lucchino', 'victorio y lucchino'], 'Estée Lauder': ['lauder'], 'Tiffany': ['tiffany co']}
notes = set()
for p in st:
    m = {x['key']: x['value'] for x in p['mf']['nodes']}
    for k in ('salida', 'corazon', 'fondo', 'familia', 'grupo'):
        for n in (m.get(k) or '').split(','):
            for w in norm(n).split(): notes.add(w)
notes |= {'vanilla', 'vanille', 'oud', 'musk', 'rose', 'amber', 'ambre', 'tobacco', 'leather', 'cuir', 'iris', 'vetiver', 'santal', 'neroli', 'jasmine', 'tonka', 'black', 'white', 'gold', 'blue', 'red', 'pink', 'noir', 'intense', 'man', 'woman', 'homme', 'femme', 'sport'}
brands = {}; P = {}
for c in cat:
    if '·' not in c['ref']: continue
    code = c['code'].lstrip("'"); ln = LM.get(c['line'], c['line'])
    hs = [h for h, t in by.get(code, []) if t == ln] or [h for h, t in by.get(code, [])]
    name, brand = [x.strip() for x in c['ref'].rsplit('·', 1)]
    brand = DISP.get(brand, brand)
    if brand not in brands: brands[brand] = len(brands)
    key = (name, brand)
    if key in P: P[key][2].append(hs[0])
    else: P[key] = [name, brands[brand], [hs[0]]]
bl = [[b, ALIAS.get(b, [])] for b in brands]
pl = []
for (name, brand), (n, bi, hs) in sorted(P.items(), key=lambda x: (x[0][1], x[0][0])):
    k = norm(n); auto = 0 if (re.fullmatch(r'[0-9 ]+', k) or (' ' not in k and (k in notes or len(k) < 3))) else 1
    pl.append([n, bi, '|'.join(hs), auto])
json.dump({'b': bl, 'p': pl}, open('intenso-eqn.json', 'w'), ensure_ascii=False, separators=(',', ':'))
print('marcas', len(bl), 'perfumes', len(pl), 'no-auto', sum(1 for x in pl if not x[3]))
