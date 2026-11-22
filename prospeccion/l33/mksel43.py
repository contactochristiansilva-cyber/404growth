# Lote 43 (22/11/2026): 13 del scrapeo del 19/11 que quedaban sin propuesta (scrapeo-19nov/leads.json) → sel43.json,
# para el lunes 23/11 (con las 27 del lote 42 son 40). Propuesta v42 (gen42.py) y tienda «Editorial» (gen37a.py).
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
L = {x['ig']: x for x in json.load(open(os.path.join(HERE, '..', 'scrapeo-19nov', 'leads.json'), encoding='utf-8'))}
PICK = [('taconesbaza', 'tacones-baza', 'Tacones Baza'), ('calzadosjuliandiaz', 'calzados-j-diaz', 'Calzados J. Díaz'),
        ('quelocuramodaycomplementos', 'que-locura', 'Qué Locura'), ('garatedenda', 'garate', 'Garate'),
        ('mesacalzados', 'mesa-calzados', 'Mesa Calzados'), ('liquet.almunia', 'liquet', 'Liquet'),
        ('samoapinospuente', 'samoa-pinos-puente', 'Samoa'), ('vasdecollado', 'ana-collado', 'Ana Collado'),
        ('oohlala.moda', 'ooh-lala-peal', 'Ooh Lala'), ('gothyka_estella', 'gothyka', 'Gothyka'),
        ('doble_m.calahorra', 'doble-m-calahorra', 'Doble M'), ('milagarcia.mg', 'mila-garcia', 'Mila García'),
        ('acaik_almudena', 'acaik', 'Acaik')]
out = []
for ig, slug, name in PICK:
    x = L[ig]
    out.append(dict(niche={'sneakers': 'calzado'}.get(x['niche'], x['niche']), name=name, ig=ig, f=x['f'], wa=x['mobile'], zone=x['zone'],
                    region=x['region'], address=x.get('address', ''), shop=x['shop'], contact=x['mobile'], what=x['what'], slug=slug,
                    date='23/11/2026', day='2026-11-23'))
assert len({o['slug'] for o in out}) == len(out) == 13
json.dump(out, open(os.path.join(HERE, 'sel43.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('\n'.join(f"{o['slug']:22} {o['niche']:8} {o['zone']} ({o['region']})  {o['what'][:60]}" for o in out))
