# 25/11/2026 (lote 45): SEED8 (seed_20261125) con las 13 tiendas del scrapeo del 25/11, ya con su propuesta v42b (con «Los números»).
# uso: python3 mkrows45.py ../l33/sel45.json rows45.js   ·   patch_s25.py mete las dos líneas en el worker, después del SEED7.
import json, re, sys, unicodedata
src, out = sys.argv[1], sys.argv[2]
sel = json.load(open(src, encoding='utf-8'))
TIER = {'A': 'anuncia en Meta y su web no vende', 'B': 'web rota, sin tienda o sin carrito', 'C': 'vende a distancia sin anuncios ni web'}

def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')

def fmt(n):
    return f"{n:,}".replace(',', '.')

def tel(n):
    return f"{n[:3]} {n[3:5]} {n[5:7]} {n[7:]}"

rows = []
for k, x in enumerate(sorted(sel, key=lambda e: -e['score'])):
    lid = f"mod-{slug(x['name'])}-{slug(x['zone'])}"[:60].rstrip('-')
    mob = x['wa']
    assert re.fullmatch(r'[67]\d{8}', mob), mob
    notes = [f"IG @{x['ig']}: {fmt(x['f'])} seguidores",
             'Tienda online: ' + x['shop'],
             f"Nivel {x['tier']} ({TIER[x['tier']]}), puntuación {x['score']}/100",
             f"Contacto: móvil {tel(mob)} (publicado por el negocio en Instagram, su web o su ficha de Google; WhatsApp sin comprobar en WhatsApp Web)",
             x['what'],
             f"Scrapeo del 25/11 (nivel de conciencia: anuncios en Meta o web que no vende; ya venden a distancia). Propuesta (lote 45, con «Los números»): 404growth.com/p/{x['slug']}/"]
    d = {"niche": "moda", "name": x['name'], "phone": '+34' + mob, "phoneType": 'móvil', "whatsapp": '+34' + mob, "email": "",
         "website": "", "zone": x['zone'], "address": x['address'], "store": 'none', "notes": "\n".join(notes),
         "instagram": f"https://www.instagram.com/{x['ig']}/", "igFollowers": x['f'], "centers": 6 if x['slug'] == 'tiendas-pillados' else 1,
         "stage": "new", "flags": [], "source": "Scrapeo 25/11: anuncios en Meta o web que no vende, ya venden a distancia",
         "priority": 90 if x['tier'] == 'A' else 85, "region": x['region'], "lotDay": x['day'],
         "slug": x['slug'], "pageUrl": f"https://404growth.com/p/{x['slug']}/", "order": 1001 + k}
    m = re.match(r'([a-z0-9.-]+\.(?:com|es))', x['shop'])
    if m:
        d['website'] = 'https://' + m.group(1) + '/'
    rows.append([lid, d])
assert len({r[0] for r in rows}) == len(rows)
js = (f'const SEED8_KEY = "seed_20261125";   // 25/11 (lote 45): {len(rows)} tiendas de moda con nivel de conciencia alto (anuncios en Meta o web que no vende) que ya venden a distancia, a Scrapeados en el lote del 25/11, con su propuesta\n'
      'const SEED8 = ' + json.dumps(rows, ensure_ascii=False) + ';\n')
open(out, 'w', encoding='utf-8').write(js)
for r in rows:
    print(r[0], r[1]['order'], r[1]['website'])
