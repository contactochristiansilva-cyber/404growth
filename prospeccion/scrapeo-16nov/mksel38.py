# Lote 38 (16/11/2026): de crm30.json (+ nuevos10.json) a l33/sel38.json para mkjobs/gen37a/gen33v. Sin muebles (Chris: «no veo bien muebles»).
# uso: python3 mksel38.py crm30.json [nuevos10.json] ../l33/sel38.json
import json, sys
SLUG = {'Luxoro': 'luxoro', 'Matia': 'matia-joyeria', 'GM Joyerías': 'gm-joyerias', 'Mantones y Complementos África': 'mantones-africa',
        'Mirage Pamplona': 'mirage-pamplona', 'Tete Plata': 'tete-plata', 'La Cañada': 'la-canada-showroom', 'Déjà Vu Villafranca': 'deja-vu-villafranca',
        'Amelie': 'amelie-bilbao', 'Pepita Mariquita': 'pepita-mariquita', 'Kisco': 'kisco-calzados', 'Zona Coolto': 'zona-coolto',
        'Azalea moda hombre': 'azalea-moda', 'Bellamoda': 'bellamoda', 'MH Mercedes Henares': 'mh-mercedes-henares', 'Libe Boutique': 'libe-boutique',
        'Pilm': 'pilm', 'Mía Möll': 'mia-moll', 'Calzados Toñi (Cocoshoes 1984)': 'calzados-toni', 'Livorno Calzados': 'livorno-calzados'}
WEB = {'Luxoro': ('luxoro.es', 'luxoro.es es de compraventa de oro: vuestras joyas no se pueden comprar online. Quien os ve en Instagram fuera de vuestros centros solo puede escribiros.'),
       'Matia': ('joyeriamatia.com', None), 'GM Joyerías': ('gmjoyerias.es', 'gmjoyerias.es es de compraventa de oro y su «Tienda» no tiene productos: quien os encuentra fuera de vuestras cuatro tiendas solo puede escribiros.'),
       'Mirage Pamplona': ('miragepamplona.com', None), 'Tete Plata': ('teteplata.com', None), 'Amelie': ('ameliebilbao.com', None),
       'Zona Coolto': ('zonacoolto.com', None), 'Mía Möll': ('miamoll.es', None),
       'Libe Boutique': ('libeboutique.com', 'libeboutique.com tiene solo 14 productos a la venta: casi nada de lo que enseñáis en Instagram se puede comprar online.'),
       'Pilm': ('pilm.es', 'pilm.es tiene 36 productos a la venta: menos de lo que enseñáis en un mes en Instagram, y el resto solo se puede pedir escribiendo.')}
src = json.load(open(sys.argv[1], encoding='utf-8'))
if len(sys.argv) > 3:
    src += json.load(open(sys.argv[2], encoding='utf-8'))
out = []
for x in src:
    if x['niche'] == 'deco' or x['name'] == 'Matia':   # Matia cerró el 30/07/2026 (su Instagram lo anuncia)
        continue
    s = x.get('slug') or SLUG[x['name']]
    y = dict(niche=x['niche'], name=x['name'], ig=x['ig'], f=x['f'], last=x['last'], wa=x['wa'], zone=x['zone'], region=x['region'],
             address=x.get('address', ''), shop=x['shop'], contact=f"WhatsApp {x['wa']} (comprobado el 16/11/2026)", what=x['what'], slug=s, date='16/11/2026')
    w = WEB.get(x['name']) or ((x.get('web'), x.get('web_note')) if x.get('web') else None)
    if w:
        y['web'] = 'https://' + w[0]
        if w[1]:
            y['web_note'] = w[1]
    out.append(y)
assert len({y['slug'] for y in out}) == len(out)
json.dump(out, open(sys.argv[-1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'tiendas')
