# Lote 44 (23/11/2026): las 30 de más potencial del scrapeo del 23/11 (scrapeo-23nov/leads.json, ya ordenado por puntuación)
# para el martes 24/11. Fuera Rociera y Modas Victoria's (serían la 3.ª y la 4.ª de Córdoba ese día); entran Pisotón y You Too.
# Propuesta v42b (gen42.py) y tienda «Editorial» (gen37a.py).
import json, os, re, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
L = json.load(open(os.path.join(HERE, '..', 'scrapeo-23nov', 'leads.json'), encoding='utf-8'))
OUT = {'rociera_moda_flamenca', 'modasvictoriass'}
SLUG = {'ladano_perfumeria': 'ladano-perfumeria', 'carmonacalzados': 'calzados-carmona', 'orquessa': 'orquessa',
        'joyeriaazorin': 'joyeria-azorin', 's.d_calzados': 'santo-domingo-calzados', 'decomodashop': 'decomoda',
        'almermadrid': 'almer-joyas', 'abigu_complementos': 'abigu-complementos', 'bali_aviles': 'bali-aviles',
        'alquilerflamencamadrid': 'los-lunares-de-piluka', 'mareamodas': 'marea-modas', 'arenaymarmoda': 'arena-y-mar',
        'sondelunares_modaflamenca': 'son-de-lunares', 'inma_benicio': 'inma-benicio', 'prettyroseboutique': 'pretty-rose',
        'carlosboutique03': 'carlos-boutique', 'modanaomi': 'modas-naomi', 'andyswomanmoda': 'andys-woman',
        'ladescreida.shop': 'la-descreida', 'isabelhernandezflamenca': 'isabel-hernandez-flamenca',
        'modaflamencavictoria': 'victoria-mena', 'cosadetresvlc': 'cosa-de-tres', 'fondodearmario_': 'fondo-de-armario',
        '_rachelandyou_': 'rachel-and-you', 'igual_roba_i_complements': 'igual-shop', 'twinsvalencia': 'twins-valencia',
        'calzadossanti': 'calzados-santi', 'zapatilleriaisabelcarballo': 'zapatilleria-isabel', 'pisoton_calzado': 'pisoton',
        'you_too_moda_hombre': 'you-too'}
out = []
for x in L:
    if x['ig'] in OUT or x['ig'] not in SLUG: continue
    out.append(dict(niche={'sneakers': 'calzado'}.get(x['niche'], x['niche']), name=x['name'], ig=x['ig'], f=x['f'], wa=x.get('mobile') or x.get('fijo'),
                    zone=x['zone'], region=x['region'], address=x.get('address', ''), shop=x['shop'], contact=x.get('mobile') or x.get('fijo'),
                    what=x['what'], slug=SLUG[x['ig']], score=x['score'], tier=x['tier'], date='24/11/2026', day='2026-11-24'))
assert len(out) == 30 and len({o['slug'] for o in out}) == 30, len(out)
json.dump(out, open(os.path.join(HERE, 'sel44.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('\n'.join(f"{o['tier']}{o['score']} {o['slug']:28} {o['niche']:9} {o['zone']}" for o in out))
