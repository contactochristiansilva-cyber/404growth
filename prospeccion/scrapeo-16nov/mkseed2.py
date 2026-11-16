# Builds the SEED2 constant (30 shops with Meta ads, no real online shop and WhatsApp checked, 16/11/2026) from crm30.json.
# usage: python3 mkseed2.py crm30.json seed2.js
# It does not touch the worker: the two lines it writes are pasted into worker.js by hand (Edit), next to SEED.
import json, re, sys, unicodedata
src, out = sys.argv[1], sys.argv[2]
leads = json.load(open(src, encoding='utf-8'))
PFX = {'moda': 'mod', 'joya': 'joy', 'sneakers': 'snk', 'deco': 'dec'}
NAMES = {'moda': 'moda', 'joya': 'joyería', 'sneakers': 'calzado', 'deco': 'muebles y decoración'}

def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')

def fmt(n):
    return f"{n:,}".replace(',', '.')

rows, seen = [], set()
for x in leads:
    ni = x['niche']
    lid = f"{PFX[ni]}-{slug(x['name'])}-{slug(x['zone'])}"[:60].rstrip('-')
    assert lid not in seen, lid
    seen.add(lid)
    wa = '+34' + x['wa']
    notes = []
    if x.get('ig'):
        notes.append(f"IG @{x['ig']}: {fmt(x['f'])} seguidores; interacción {str(x['eng']).replace('.', ',')} % (mediana de «me gusta» y comentarios de sus 12 últimas publicaciones entre seguidores); última publicación el {x['last']}")
    else:
        notes.append(x.get('fb', 'Sin Instagram'))
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
    for a in x.get('aviso', []):
        notes.append('AVISO: ' + a)
    d = {"niche": ni, "name": x['name'], "phone": wa, "phoneType": "WhatsApp", "whatsapp": wa, "email": x.get('email', ''),
         "website": "", "zone": x['zone'], "address": x.get('address', ''), "store": "none", "notes": "\n".join(notes),
         "instagram": f"https://www.instagram.com/{x['ig']}/" if x.get('ig') else "", "igFollowers": x.get('f') or 0,
         "centers": x.get('centers', 1), "stage": "new", "flags": [],
         "source": "Scrapeo: tiendas con anuncios en Meta, sin tienda online y con WhatsApp (16 nov)",
         "priority": 60 + 4 * x['score'], "region": x['region']}
    rows.append([lid, d])

cnt = {}
for _, d in rows:
    cnt[d['niche']] = cnt.get(d['niche'], 0) + 1
desc = ", ".join(f"{v} de {NAMES[k]}" for k, v in cnt.items())
js = (f'const SEED2_KEY = "seed_20261116w";   // 16/11: {len(rows)} tiendas con anuncios en Meta (activos o en el último año), sin tienda online o con una floja y con WhatsApp comprobado ({desc}), a Scrapeados\n'
      'const SEED2 = ' + json.dumps(rows, ensure_ascii=False) + ';\n')
open(out, 'w', encoding='utf-8').write(js)
print(len(rows), cnt)
