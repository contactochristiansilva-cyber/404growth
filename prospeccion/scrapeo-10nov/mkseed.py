# Builds the SEED for the 10/11/2026 scrape from leads.json and writes it into the admin worker.
# usage: python3 mkseed.py worker.js leads.json
import json, re, sys, unicodedata
W, L = sys.argv[1], sys.argv[2]
leads = json.load(open(L, encoding='utf-8'))
PFX = {'moda': 'mod', 'joya': 'joy', 'cosmetica': 'cos', 'suplementos': 'sup', 'sneakers': 'snk', 'optica': 'opt'}
NAMES = {'moda': 'moda', 'joya': 'joyería', 'cosmetica': 'cosmética', 'suplementos': 'suplementos', 'sneakers': 'sneakers', 'optica': 'ópticas'}

def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')

def fmt(n):
    return f"{n:,}".replace(',', '.')

out, seen = [], set()
for x in leads:
    ni = x['niche']
    lid = f"{PFX[ni]}-{slug(x['name'])}-{slug(x['zone'])}"[:60].rstrip('-')
    assert lid not in seen, lid
    seen.add(lid)
    wa = '+34' + x['wa']
    notes = [f"IG @{x['ig']}: {fmt(x['f'])} seguidores ({x.get('date','9/11/2026')})",
             'Tienda online: ' + x['shop'],
             'Contacto: ' + x['contact']]
    if x.get('owner'): notes.append('Dueño: ' + x['owner'])
    else: notes.append('Dueño: no lo publican')
    notes.append(x['what'])
    for a in x.get('aviso', []): notes.append('AVISO: ' + a)
    d = {"niche": ni, "name": x['name'], "phone": wa, "phoneType": "móvil", "whatsapp": wa, "email": x.get('email', ''),
         "website": x.get('web', ''), "zone": x['zone'], "address": x.get('address', ''), "store": x.get('store', 'none'),
         "notes": "\n".join(notes), "instagram": f"https://www.instagram.com/{x['ig']}/", "igFollowers": x['f'],
         "centers": x.get('centers', 1), "stage": "new", "flags": [],
         "source": x.get("source", "Scrapeo Instagram +5k seguidores con WhatsApp (10 nov)"), "priority": x.get('priority', 80), "region": x['region']}
    if x.get('slug'):
        d['slug'] = x['slug']; d['pageUrl'] = f"https://404growth.com/p/{x['slug']}/"
    out.append([lid, d])

w = open(W, encoding='utf-8').read()
m = re.search(r'^const SEED_KEY = "[^"]*";[^\n]*\nconst SEED = \[.*?\];\n', w, re.M | re.S)
assert m
cnt = {}
for _, d in out: cnt[d['niche']] = cnt.get(d['niche'], 0) + 1
desc = ", ".join(f"{v} de {NAMES[k]}" for k, v in cnt.items())
new = f'const SEED_KEY = "seed_20261110b";   // 10/11: {len(out)} tiendas con WhatsApp y sin tienda online (+5k seguidores y, en la segunda búsqueda, +1k) ({desc}), a Scrapeados\nconst SEED = ' + json.dumps(out, ensure_ascii=False) + ';\n'
w = w[:m.start()] + new + w[m.end():]
open(W, 'w', encoding='utf-8').write(w)
print(len(out), cnt)
