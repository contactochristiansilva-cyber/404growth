# Lote 42 (22/11/2026): las 36 del scrapeo del 21-22/11 (scrapeo-22nov/leads.json) → sel42.json, con la propuesta v42 (gen42.py)
import json, re, unicodedata, os
HERE = os.path.dirname(os.path.abspath(__file__))
L = json.load(open(os.path.join(HERE, '..', 'scrapeo-22nov', 'leads.json'), encoding='utf-8'))
def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')
SL = {'Sinu & Son': 'sinu-and-son', "L'Àlex Joies": 'lalex-joies', 'Regala-T Complementos & Moda': 'regala-t', 'Cambia-T Personal Shopper': 'cambia-t',
      'Riá Pitá Moda Flamenca': 'ria-pita', 'Sabrina Ortega Complementos': 'sabrina-ortega', 'Antollos Espacio de Moda': 'antollos',
      'Joyería Esencia Mojácar': 'joyeria-esencia', 'TJ Moda y Calzado': 'tj-moda'}
out = []
for x in L:
    ni = {'sneakers': 'calzado'}.get(x['niche'], x['niche'])
    out.append(dict(niche=ni, name=x['name'], ig=x['ig'], f=x['f'], wa=x['mobile'], zone=x['zone'], region=x['region'], address=x.get('address', ''),
                    shop=x['shop'], contact=x['mobile'], what=x['what'], slug=SL.get(x['name'], slug(x['name'])), date='23/11/2026', day=x['day'], tier=x['tier']))
assert len({o['slug'] for o in out}) == len(out)
json.dump(out, open(os.path.join(HERE, 'sel42.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('\n'.join(f"{o['slug']:28} {o['niche']:8} {o['zone']}" for o in out))
