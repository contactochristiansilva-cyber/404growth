# 17/11/2026 (for 18/11): CRM rows for the 30 of candidatos.json (IG only, +10k followers, active, no online shop, no moda or food).
# usage: python3 mkrows.py candidatos.json rows18.js
# Writes SEED3_KEY/SEED3 (new leads, Scrapeados, no proposal yet) and LEAD_PATCH_KEY/LEAD_PATCH
# (the 5 unsent of the lote 38 to the batch of 18/11). It does not touch the worker: patch_l39.py puts the lines in.
import json, re, sys, unicodedata
src, out = sys.argv[1], sys.argv[2]
DAY = '2026-11-18'
UNSENT38 = ['mod-ailec-modas-y-complementos-algeciras', 'snk-calzados-bergillos-estacion-de-cartama',
            'snk-calzados-toni-cocoshoes-1984-chauchina', 'snk-kisco-jerez-de-la-frontera', 'snk-livorno-calzados-mieres']
PFX = {'joya': 'joy', 'cosmetica': 'cos', 'suplementos': 'sup', 'toys': 'jug', 'deporte': 'dep',
       'merceria': 'mer', 'arte': 'art', 'artesania': 'atn', 'electro': 'ele'}
NAMES = {'joya': 'joyería', 'cosmetica': 'perfumería', 'suplementos': 'herbolario', 'toys': 'juguetes y juegos', 'deporte': 'hípica',
         'merceria': 'mercería, lanas y telas', 'arte': 'bellas artes y scrap', 'artesania': 'artesanía', 'electro': 'electrodomésticos'}
leads = json.load(open(src, encoding='utf-8'))
# 17/11 (por la noche): las 30 ya tienen propuesta (lote 39, prospeccion/l33/sel39.json): slug por la cuenta de Instagram
SLUG = {x['ig']: x['slug'] for x in json.load(open(__file__.rsplit('/', 1)[0] + '/../l33/sel39.json', encoding='utf-8'))}

def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')

def fmt(n):
    return f"{n:,}".replace(',', '.')

def tel(n):
    return f"{n[:3]} {n[3:5]} {n[5:7]} {n[7:]}" if n.startswith(('6', '7')) else f"{n[:3]} {n[3:6]} {n[6:]}"

def day(d):
    y, m, dd = d.split('-')
    return f"{int(dd)}/{int(m)}/{y}"

rows, seen = [], set()
for x in leads:
    ni = x['niche']
    lid = f"{PFX[ni]}-{slug(x['name'])}-{slug(x['zone'])}"[:60].rstrip('-')
    assert lid not in seen, lid
    seen.add(lid)
    mob, fijo, pub = x.get('mobile', ''), x.get('fijo', ''), bool(x.get('waPub'))
    if mob:
        phone, ptype, wa = '+34' + mob, 'móvil', '+34' + mob
    elif pub:   # a landline they give as WhatsApp
        phone, ptype, wa = '+34' + fijo, 'fijo con WhatsApp', '+34' + fijo
    else:
        phone, ptype, wa = '+34' + fijo, 'fijo', ''
    eng = round(100 * x['med'] / x['f'], 2)
    notes = [f"IG @{x['ig']}: {fmt(x['f'])} seguidores; {x['n30']} publicaciones en 30 días, la última el {day(x['last'])}; "
             f"mediana de {fmt(x['med'])} «me gusta» por publicación ({str(eng).replace('.', ',')} % de los seguidores)",
             'Tienda online: ' + x['shop']]
    c = []
    if mob:
        c.append(f"móvil {tel(mob)}" + (' (lo publican como WhatsApp)' if pub else ' (WhatsApp sin comprobar)'))
    if x.get('mobile2'):
        c.append(f"otro móvil {tel(x['mobile2'])}")
    if fijo:
        c.append(f"fijo {tel(fijo)}" + (' (lo publican como WhatsApp)' if pub and not mob else ''))
    if x.get('email'):
        c.append(x['email'])
    notes.append('Contacto: ' + ' · '.join(c) + ' (publicados por el negocio en Instagram, su web o Google Maps)')
    notes.append(x['what'])
    sl = SLUG[x['ig']]
    notes.append(f'Propuesta (lote 39, fotos de Google Flow): https://404growth.com/p/{sl}/ (scrapeo del 17/11 para el 18/11)')
    for a in x.get('aviso', []):
        notes.append('AVISO: ' + a)
    pr = 50 if not wa else (80 if pub else 75)
    if 100 * x['med'] / x['f'] < 0.15:
        pr -= 10
    d = {"niche": ni, "name": x['name'], "phone": phone, "phoneType": ptype, "whatsapp": wa, "email": x.get('email', ''),
         "website": ('https://' + x['web'] + '/') if x.get('web') else '', "zone": x['zone'], "address": x.get('address', ''),
         "store": "none", "notes": "\n".join(notes), "instagram": f"https://www.instagram.com/{x['ig']}/", "igFollowers": x['f'],
         "centers": 1, "stage": "new", "flags": [],
         "source": "Scrapeo Instagram: +10k seguidores, activas y sin tienda online, sin moda ni comida (17 nov)",
         "priority": pr, "region": x['region'], "slug": sl, "pageUrl": f"https://404growth.com/p/{sl}/", "lotDay": DAY}
    if wa and not pub:
        d['waOk'] = False   # the shop does not say this number has WhatsApp: «Instagram» goes first
    rows.append([lid, d])

cnt = {}
for _, d in rows:
    cnt[d['niche']] = cnt.get(d['niche'], 0) + 1
desc = ", ".join(f"{v} de {NAMES[k]}" for k, v in sorted(cnt.items(), key=lambda kv: -kv[1]))
patch = [[i, {"lotDay": DAY}] for i in UNSENT38] + [[i, {"lotDay": DAY, "slug": d['slug'], "pageUrl": d['pageUrl']}] for i, d in rows]
js = (f'const SEED3_KEY = "seed_20261118";   // 17/11 (para el 18/11): {len(rows)} tiendas con +10k seguidores en Instagram, activas, sin tienda online o con una floja, sin moda ni comida ({desc}), a Scrapeados, con su propuesta (lote 39) en el lote del {DAY}\n'
      'const SEED3 = ' + json.dumps(rows, ensure_ascii=False) + ';\n'
      f'const LEAD_PATCH_KEY = "lpatch_20261118";   // 17/11: las 5 del lote 38 que se quedaron sin enviar, al lote del {DAY} (Chris: se mandan mañana) y las 30 del SEED3 con su propuesta (lote 39)\n'
      'const LEAD_PATCH = ' + json.dumps(patch, ensure_ascii=False) + ';\n')
open(out, 'w', encoding='utf-8').write(js)
print(len(rows), cnt, 'waOk false:', sum(1 for _, d in rows if d.get('waOk') is False), 'sin WhatsApp:', sum(1 for _, d in rows if not d['whatsapp']))
