# 25/11/2026 por la tarde (lote 47): SEED9 (seed_20261125b) con las 35 tiendas del segundo scrapeo del 25/11, ya con su propuesta v42b
# (con «Los números»), para el segundo teléfono (35 desde el WhatsApp Business y 35 desde el personal).
# uso: python3 mkrows47.py ../l33/sel47.json rows47.js   ·   patch_s47.py mete las dos líneas en el worker, después del SEED8.
import json, re, sys, unicodedata
src, out = sys.argv[1], sys.argv[2]
sel = json.load(open(src, encoding='utf-8'))
TIER = {'A': 'anuncia en Meta y no tiene tienda online', 'B': 'web rota, sin tienda o con muy pocos productos', 'C': 'vende a distancia (WhatsApp, MD, directos) sin anuncios ni web'}
NI = {'moda': ('moda', 'mod'), 'calzado': ('sneakers', 'snk'), 'joya': ('joya', 'joy')}

def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')

fmt = lambda n: f"{n:,}".replace(',', '.')
tel = lambda n: f"{n[:3]} {n[3:5]} {n[5:7]} {n[7:]}"
rows = []
for k, x in enumerate(sorted(sel, key=lambda e: -e['score'])):
    ni, pfx = NI[x['niche']]
    lid = f"{pfx}-{slug(x['name'])}-{slug(x['zone'])}"[:60].rstrip('-')
    mob = x['wa']
    assert re.fullmatch(r'[67]\d{8}', mob), mob
    notes = [f"IG @{x['ig']}: {fmt(x['f'])} seguidores",
             'Tienda online: ' + x['shop'],
             f"Nivel {x['tier']} ({TIER[x['tier']]}), puntuación {x['score']}/100",
             f"Contacto: móvil {tel(mob)} (publicado por el negocio en Instagram{'; lo da como WhatsApp' if x.get('waBio') else ''}; WhatsApp sin comprobar en WhatsApp Web)",
             x['what'],
             f"Scrapeo del 25/11 por la tarde (nivel de conciencia; ya venden a distancia). Propuesta (lote 47, con «Los números»): 404growth.com/p/{x['slug']}/"]
    if x.get('aviso'):
        notes.append('AVISO: ' + x['aviso'])
    d = {"niche": ni, "name": x['name'], "phone": '+34' + mob, "phoneType": 'móvil', "whatsapp": '+34' + mob, "email": "",
         "website": "", "zone": x['zone'], "address": x['address'], "store": 'none', "notes": "\n".join(notes),
         "instagram": f"https://www.instagram.com/{x['ig']}/", "igFollowers": x['f'], "centers": x.get('centers', 1),
         "stage": "new", "flags": [], "source": "Scrapeo 25/11 (tarde): nivel de conciencia, ya venden a distancia",
         "priority": {'A': 90, 'B': 85, 'C': 80}[x['tier']], "region": x['region'], "lotDay": x['day'],
         "slug": x['slug'], "pageUrl": f"https://404growth.com/p/{x['slug']}/", "order": 2001 + k}
    if not x.get('waBio'):
        d['waOk'] = False
    m = re.match(r'([a-z0-9.-]+\.(?:com|es))', x['shop'])
    if m:
        d['website'] = 'https://' + m.group(1) + '/'
    rows.append([lid, d])
assert len({r[0] for r in rows}) == len(rows)
js = (f'const SEED9_KEY = "seed_20261125b";   // 25/11 tarde (lote 47): {len(rows)} tiendas (moda, calzado y joyería) con nivel de conciencia alto que ya venden a distancia, en el lote del 25/11 con su propuesta (segundo teléfono)\n'
      'const SEED9 = ' + json.dumps(rows, ensure_ascii=False) + ';\n')
open(out, 'w', encoding='utf-8').write(js)
for r in rows:
    print(r[0], r[1]['order'], r[1]['website'], r[1].get('waOk', ''))
