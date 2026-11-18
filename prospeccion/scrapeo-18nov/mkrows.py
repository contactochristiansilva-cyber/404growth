# 18/11/2026 (para el 19/11): filas del CRM para las 35 de leads.json (filtros nuevos: ya venden a distancia, interacción real,
# 5k-40k seguidores, activas, sin tienda online de verdad, móvil publicado). Sin propuesta todavía.
# uso: python3 mkrows.py leads.json rows19.js
# Escribe SEED4_KEY/SEED4 (leads nuevos en Scrapeados con lotDay 2026-11-19). patch_s19.py mete las líneas en el worker.
import json, re, sys, unicodedata
src, out = sys.argv[1], sys.argv[2]
DAY = '2026-11-19'
PFX = {'moda': 'mod', 'joya': 'joy', 'cosmetica': 'cos', 'suplementos': 'sup', 'deporte': 'dep', 'sneakers': 'snk'}
NAMES = {'moda': 'moda', 'joya': 'joyería', 'cosmetica': 'perfumería y cosmética', 'suplementos': 'suplementación',
         'deporte': 'moda deportiva', 'sneakers': 'calzado'}
leads = json.load(open(src, encoding='utf-8'))

def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')

def fmt(n):
    return f"{n:,}".replace(',', '.')

def tel(n):
    return f"{n[:3]} {n[3:5]} {n[5:7]} {n[7:]}" if n.startswith(('6', '7')) else f"{n[:3]} {n[3:6]} {n[6:]}"

rows, seen = [], set()
for x in leads:
    ni = x['niche']
    lid = f"{PFX[ni]}-{slug(x['name'])}-{slug(x['zone'])}"[:60].rstrip('-')
    assert lid not in seen, lid
    seen.add(lid)
    mob, fijo = x.get('mobile', ''), x.get('fijo', '')
    wa_pub = bool(x.get('waPub') or x.get('waFijo'))   # el negocio publica el número como WhatsApp (no se pudo comprobar: WhatsApp Web sin sesión)
    if mob:
        phone, ptype, wa = '+34' + mob, 'móvil', '+34' + mob
    elif x.get('waFijo'):
        phone, ptype, wa = '+34' + fijo, 'fijo con WhatsApp', '+34' + fijo
    else:
        phone, ptype, wa = '+34' + fijo, 'fijo', ''
    notes = [f"IG @{x['ig']}: {fmt(x['f'])} seguidores; {x['n30']} publicaciones en 30 días, la última hace {x['lastDays']} días; "
             f"mediana de {fmt(x['med'])} «me gusta» ({str(x['eng']).replace('.', ',')} % de los seguidores)",
             'Ya vende a distancia: ' + x['sig'],
             'Tienda online: ' + x['shop']]
    c = []
    if mob:
        c.append(f"móvil {tel(mob)}" + (' (lo publican como WhatsApp)' if x.get('waPub') else ' (WhatsApp sin comprobar)'))
    if fijo:
        c.append(f"fijo {tel(fijo)}" + (' (lo publican como WhatsApp)' if x.get('waFijo') else ''))
    notes.append('Contacto: ' + ' · '.join(c) + ' (publicados por el negocio en Instagram, su web o Google Maps)')
    notes.append(x['what'])
    notes.append('Scrapeo del 18/11 para el 19/11 con los filtros nuevos (ya venden a distancia + interacción real). Falta su propuesta.')
    for a in x.get('aviso', []):
        notes.append('AVISO: ' + a)
    pr = x.get('priority') or (85 if wa_pub else 75)
    d = {"niche": ni, "name": x['name'], "phone": phone, "phoneType": ptype, "whatsapp": wa, "email": "",
         "website": ('https://' + x['web'] + '/') if x.get('web') else '', "zone": x['zone'], "address": x.get('address', ''),
         "store": x.get('store', 'none'), "notes": "\n".join(notes), "instagram": f"https://www.instagram.com/{x['ig']}/",
         "igFollowers": x['f'], "centers": x.get('centers', 1), "stage": "new", "flags": [],
         "source": "Scrapeo Instagram 18/11: ya venden a distancia, interacción real, 5k-40k seguidores (para el 19/11)",
         "priority": pr, "region": x['region'], "lotDay": DAY}
    if wa and not wa_pub:
        d['waOk'] = False   # el negocio no dice que ese número tenga WhatsApp: «Instagram» sale primero
    rows.append([lid, d])

cnt = {}
for _, d in rows:
    cnt[d['niche']] = cnt.get(d['niche'], 0) + 1
desc = ", ".join(f"{v} de {NAMES[k]}" for k, v in sorted(cnt.items(), key=lambda kv: -kv[1]))
js = (f'const SEED4_KEY = "seed_20261119";   // 18/11 (para el 19/11): {len(rows)} tiendas que ya venden a distancia (envíos, pedidos por WhatsApp o mensaje, Bizum, directos), con interacción real, activas y sin tienda online de verdad ({desc}), a Scrapeados en el lote del {DAY} (sin propuesta todavía)\n'
      'const SEED4 = ' + json.dumps(rows, ensure_ascii=False) + ';\n')
open(out, 'w', encoding='utf-8').write(js)
print(len(rows), cnt, 'waOk false:', sum(1 for _, d in rows if d.get('waOk') is False), 'sin WhatsApp:', sum(1 for _, d in rows if not d['whatsapp']))
