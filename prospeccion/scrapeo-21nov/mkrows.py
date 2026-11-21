# 21/11/2026 (para el lunes 23/11): filas del CRM para las 40 de leads.json, con el criterio nuevo: nivel de conciencia (anuncios en Meta,
# web rota o sin tienda) antes que seguidores. Sin propuesta todavía.
# uso: python3 mkrows.py leads.json rows23.js
# Escribe SEED6_KEY/SEED6. patch_s23.py mete las líneas en el worker.
import json, re, sys, unicodedata
src, out = sys.argv[1], sys.argv[2]
PFX = {'merceria': 'mer', 'moda': 'mod', 'joya': 'joy', 'cosmetica': 'cos', 'suplementos': 'sup', 'deporte': 'dep', 'sneakers': 'snk'}
NAMES = {'merceria': 'mercería', 'moda': 'moda', 'joya': 'joyería', 'cosmetica': 'perfumería y cosmética', 'suplementos': 'suplementación',
         'deporte': 'moda deportiva', 'sneakers': 'zapatería'}
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
             'Tienda online: ' + x['shop'],
             'Anuncios en Meta: ' + x['ads'],
             f"Nivel {x['tier']} ({ {'A': 'anuncia en Meta', 'B': 'web rota o sin tienda', 'C': 'relleno: vende a distancia sin anuncios ni web'}[x['tier']] }), puntuación {x['score']}/100"]
    c = []
    if mob:
        c.append(f"móvil {tel(mob)}" + (' (lo publican como WhatsApp)' if x.get('waPub') else ' (WhatsApp sin comprobar)'))
    if x.get('mobile2'):
        c.append(f"otro móvil {tel(x['mobile2'])}")
    if fijo:
        c.append(f"fijo {tel(fijo)}" + (' (lo publican como WhatsApp)' if x.get('waFijo') else ''))
    notes.append('Contacto: ' + ' · '.join(c) + ' (publicados por el negocio en Instagram o en su web)' + (('; ' + x['mobileNote']) if x.get('mobileNote') else ''))
    notes.append(x['what'])
    notes.append("Scrapeo del 21/11 para el 23/11 con el criterio nuevo (nivel de conciencia antes que seguidores). Falta su propuesta.")
    for a in x.get('aviso', []):
        notes.append('AVISO: ' + a)
    pr = x.get('priority') or (85 if wa_pub else 75)
    d = {"niche": ni, "name": x['name'], "phone": phone, "phoneType": ptype, "whatsapp": wa, "email": "",
         "website": ('https://' + x['web'] + '/') if x.get('web') else '', "zone": x['zone'], "address": x.get('address', ''),
         "store": x.get('store', 'none'), "notes": "\n".join(notes), "instagram": f"https://www.instagram.com/{x['ig']}/",
         "igFollowers": x['f'], "centers": x.get('centers', 1), "stage": "new", "flags": [],
         "source": "Scrapeo 21/11 (para el 23/11): anuncios en Meta o web rota, ya venden a distancia",
         "priority": pr, "region": x['region'], "lotDay": x['day']}
    if wa and not wa_pub:
        d['waOk'] = False   # el negocio no dice que ese número tenga WhatsApp: «Instagram» sale primero
    rows.append([lid, d])

cnt = {}
for _, d in rows:
    cnt[d['niche']] = cnt.get(d['niche'], 0) + 1
desc = ", ".join(f"{v} de {NAMES[k]}" for k, v in sorted(cnt.items(), key=lambda kv: -kv[1]))
js = (f'const SEED6_KEY = "seed_20261123";   // 21/11 (para el 23/11): {len(rows)} tiendas con nivel de conciencia alto (anuncios en Meta o web rota o sin tienda) que ya venden a distancia ({desc}), a Scrapeados en el lote del 23/11 (sin propuesta todavía)\n'
      'const SEED6 = ' + json.dumps(rows, ensure_ascii=False) + ';\n')
open(out, 'w', encoding='utf-8').write(js)
print(len(rows), cnt, 'waOk false:', sum(1 for _, d in rows if d.get('waOk') is False), 'sin WhatsApp:', sum(1 for _, d in rows if not d['whatsapp']))
