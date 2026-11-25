# 26/11/2026 (lote 48): SEED10 (seed_20261126) con las 70 tiendas del scrapeo nocturno del 25-26/11 (negocios más grandes:
# varias tiendas físicas y sin tienda online), en el lote del 26/11. Solo llevan slug/pageUrl las que ya tienen propuesta publicada.
# uso: python3 mkrows48.py leads.json <publicadas.txt (un slug por línea)> rows48.js   ·   patch_s48.py mete las dos líneas después del SEED9.
import json, re, sys, unicodedata
src, pubf, out = sys.argv[1:4]
L = json.load(open(src, encoding='utf-8'))
pub = {l.strip() for l in open(pubf, encoding='utf-8') if l.strip()}
TIER = {'A': 'varias tiendas físicas y sin tienda online', 'B': 'tienda grande (muchos seguidores) sin tienda online',
        'C': 'vende a distancia (WhatsApp, MD, directos) sin tienda online'}
NI = {'moda': ('moda', 'mod'), 'calzado': ('sneakers', 'snk'), 'joya': ('joya', 'joy')}


def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')


fmt = lambda n: f"{n:,}".replace(',', '.')
tel = lambda n: f"{n[:3]} {n[3:5]} {n[5:7]} {n[7:]}"
NIORD = {'moda': 0, 'joya': 1, 'calzado': 2}
rows = []
order = sorted(L, key=lambda e: (0 if e['slug'] in pub else 1, NIORD.get(e['niche'], 3), -e['score']))
for k, x in enumerate(order):
    ni, pfx = NI[x['niche']]
    lid = f"{pfx}-{slug(x['name'])}-{slug(x['zone'])}"[:60].rstrip('-')
    mob = x.get('wa') or ''
    fijo = x.get('fijo') or ''
    has = x['slug'] in pub
    notes = [f"IG @{x['ig']}: {fmt(x['f'])} seguidores",
             'Tienda online: ' + x['shop'],
             f"Nivel {x['tier']} ({TIER[x['tier']]}), puntuación {x['score']}/100" + (f"; {x['centers']} tiendas físicas" if x.get('centers', 1) > 1 else ''),
             (f"Contacto: móvil {tel(mob)} (publicado por el negocio{'; lo da como WhatsApp' if x.get('waBio') else ''}; WhatsApp sin comprobar en WhatsApp Web)"
              if mob else f"Contacto: solo publican fijo {tel(fijo) if fijo else '(sin número)'}"),
             x['what'],
             'Scrapeo del 25-26/11 por la noche (negocios más grandes, varias tiendas físicas, sin tienda online). '
             + (f"Propuesta (lote 48, v42b con «Los números»): 404growth.com/p/{x['slug']}/" if has else 'Sin propuesta todavía.')]
    if x.get('aviso'):
        notes.append('AVISO: ' + x['aviso'])
    if not mob:
        notes.append('AVISO: solo publican fijo')
    num = mob or fijo
    d = {"niche": ni, "name": x['name'], "phone": ('+34' + num) if num else '', "phoneType": 'móvil' if mob else 'fijo',
         "whatsapp": ('+34' + mob) if mob else '', "email": "", "website": "", "zone": x['zone'], "address": x['address'],
         "store": 'none', "notes": "\n".join(notes), "instagram": f"https://www.instagram.com/{x['ig']}/", "igFollowers": x['f'],
         "centers": x.get('centers', 1), "stage": "new", "flags": [],
         "source": "Scrapeo 25-26/11 (noche): negocios más grandes, varias tiendas, sin tienda online",
         "priority": 50 if not mob else {'A': 92, 'B': 85, 'C': 78}[x['tier']], "region": x['region'], "lotDay": x['day'],
         "order": 3001 + k}
    if has:
        d['slug'] = x['slug']; d['pageUrl'] = f"https://404growth.com/p/{x['slug']}/"
    if mob and not x.get('waBio'):
        d['waOk'] = False
    m = re.search(r'([a-z0-9-]+(?:\.[a-z0-9-]+)*\.(?:com|es|net|cat|eu|shop|store))', x['shop'])
    if m:
        d['website'] = 'https://' + m.group(1) + '/'
    rows.append([lid, d])
ids = [r[0] for r in rows]
assert len(set(ids)) == len(ids), [i for i in ids if ids.count(i) > 1]
js = (f'const SEED10_KEY = "seed_20261126";   // 26/11 (lote 48): {len(rows)} tiendas más grandes (varias tiendas físicas, sin tienda online), en el lote del 26/11; {sum(1 for r in rows if "slug" in r[1])} con propuesta\n'
      'const SEED10 = ' + json.dumps(rows, ensure_ascii=False) + ';\n')
open(out, 'w', encoding='utf-8').write(js)
for r in rows:
    print(r[0], r[1]['order'], r[1].get('slug', '-'), r[1]['website'], r[1].get('waOk', ''), r[1]['priority'])
