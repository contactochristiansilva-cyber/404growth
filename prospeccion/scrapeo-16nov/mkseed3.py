# Lote 38 (17/11/2026): SEED2 + LEAD_PATCH for the 30 shops with proposal (19 of crm30.json without furniture or Matia + nuevos11.json).
# usage: python3 mkseed3.py crm30.json nuevos11.json seed3.js
# Writes SEED2_KEY/SEED2 (same key seed_20261116w: SEED2 was never uploaded) and LEAD_PATCH_KEY/LEAD_PATCH (slug, pageUrl, lotDay 2026-11-17).
# It does not touch the worker: tools/… or a copy-and-replace script puts the four lines in.
import json, re, sys, unicodedata
src, new, out = sys.argv[1], sys.argv[2], sys.argv[3]
SLUG = {'Luxoro': 'luxoro', 'GM Joyerías': 'gm-joyerias', 'Mantones y Complementos África': 'mantones-africa',
        'Mirage Pamplona': 'mirage-pamplona', 'Tete Plata': 'tete-plata', 'La Cañada': 'la-canada-showroom', 'Déjà Vu Villafranca': 'deja-vu-villafranca',
        'Amelie': 'amelie-bilbao', 'Pepita Mariquita': 'pepita-mariquita', 'Kisco': 'kisco-calzados', 'Zona Coolto': 'zona-coolto',
        'Azalea moda hombre': 'azalea-moda', 'Bellamoda': 'bellamoda', 'MH Mercedes Henares': 'mh-mercedes-henares', 'Libe Boutique': 'libe-boutique',
        'Pilm': 'pilm', 'Mía Möll': 'mia-moll', 'Calzados Toñi (Cocoshoes 1984)': 'calzados-toni', 'Livorno Calzados': 'livorno-calzados'}
DAY = '2026-11-17'
leads = [x for x in json.load(open(src, encoding='utf-8')) if x['niche'] != 'deco' and x['name'] != 'Matia']   # Chris: «no veo bien muebles»; Matia cerró
for x in leads:
    x['slug'] = SLUG[x['name']]
leads += json.load(open(new, encoding='utf-8'))
leads.sort(key=lambda x: -x['score'])
PFX = {'moda': 'mod', 'joya': 'joy', 'sneakers': 'snk'}
NAMES = {'moda': 'moda', 'joya': 'joyería', 'sneakers': 'calzado'}

def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')

def fmt(n):
    return f"{n:,}".replace(',', '.')

rows, patch, seen = [], [], set()
for x in leads:
    ni = x['niche']
    lid = f"{PFX[ni]}-{slug(x['name'])}-{slug(x['zone'])}"[:60].rstrip('-')
    assert lid not in seen, lid
    seen.add(lid)
    wa = '+34' + x['wa']
    notes = []
    eng = f"; interacción {str(x['eng']).replace('.', ',')} % (mediana de «me gusta» y comentarios de sus 12 últimas publicaciones entre seguidores)" if x.get('eng') is not None else ''
    notes.append(f"IG @{x['ig']}: {fmt(x['f'])} seguidores{eng}; última publicación el {x['last']}")
    notes.append('Anuncios en Meta: ' + x['ads'])
    notes.append('Tienda online: ' + x['shop'])
    c = f"WhatsApp {x['wa'][:3]} {x['wa'][3:5]} {x['wa'][5:7]} {x['wa'][7:]} comprobado en WhatsApp Web el 16/11/2026"
    if x.get('fijo'):
        c += f" · fijo {x['fijo']}"
    if x.get('email'):
        c += f" · {x['email']}"
    notes.append('Contacto: ' + c)
    if x.get('centers', 1) > 1:
        notes.append(f"Tiendas: {x['centers']}")
    notes.append(x['what'])
    notes.append(f"Puntuación del piloto: {x['score']}/10 (tiendas, anuncios, web e interacción)")
    notes.append(f"Propuesta (lote 38): https://404growth.com/p/{x['slug']}/")
    for a in x.get('aviso', []):
        notes.append('AVISO: ' + a)
    d = {"niche": ni, "name": x['name'], "phone": wa, "phoneType": "WhatsApp", "whatsapp": wa, "email": x.get('email', ''),
         "website": "", "zone": x['zone'], "address": x.get('address', ''), "store": "none", "notes": "\n".join(notes),
         "instagram": f"https://www.instagram.com/{x['ig']}/", "igFollowers": x.get('f') or 0,
         "centers": x.get('centers', 1), "stage": "new", "flags": [],
         "source": "Scrapeo: tiendas con anuncios en Meta, sin tienda online y con WhatsApp (16 nov)",
         "priority": 60 + 4 * x['score'], "region": x['region']}
    rows.append([lid, d])
    patch.append([lid, {"lotDay": DAY, "slug": x['slug'], "pageUrl": f"https://404growth.com/p/{x['slug']}/"}])

cnt = {}
for _, d in rows:
    cnt[d['niche']] = cnt.get(d['niche'], 0) + 1
desc = ", ".join(f"{v} de {NAMES[k]}" for k, v in cnt.items())
js = (f'const SEED2_KEY = "seed_20261116w";   // 16/11 (lote 38): {len(rows)} tiendas con anuncios en Meta (activos o en el último año), sin tienda online o con una floja y con WhatsApp comprobado ({desc}), a Scrapeados; sin muebles (Chris: «no veo bien muebles») ni Matia (cerró)\n'
      'const SEED2 = ' + json.dumps(rows, ensure_ascii=False) + ';\n'
      f'const LEAD_PATCH_KEY = "lpatch_20261117";   // 17/11: las {len(patch)} del lote 38 (SEED2) al lote del {DAY}, con su propuesta (corre después de los SEED)\n'
      'const LEAD_PATCH = ' + json.dumps(patch, ensure_ascii=False) + ';\n')
open(out, 'w', encoding='utf-8').write(js)
print(len(rows), cnt)
