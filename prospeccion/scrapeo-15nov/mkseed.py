# Builds the SEED for the 15/11/2026 scrape (50 shops: fashion, perfumes, supplements, jewellery) from leads.json and writes it into the admin worker.
# usage: python3 mkseed.py worker.js leads.json
# The previous SEED (seed_20261111b) was already uploaded, so the new SEED only carries this batch.
import json, re, sys, unicodedata
W, L = sys.argv[1], sys.argv[2]
leads = json.load(open(L, encoding='utf-8'))
PFX = {'moda': 'mod', 'joya': 'joy', 'cosmetica': 'cos', 'suplementos': 'sup'}
NAMES = {'moda': 'moda', 'joya': 'joyería', 'cosmetica': 'perfumería', 'suplementos': 'suplementos'}

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
    wa = ('+34' + x['wa']) if x.get('wa') else ''
    notes = [f"IG @{x['ig']}: {fmt(x['f'])} seguidores; última publicación el {x['last']} (15/11/2026)",
             'Tienda online: ' + x['shop'],
             'Contacto: ' + x['contact']]
    notes.append('Dueño: ' + (x.get('owner') or 'no lo publican'))
    notes.append(x['what'])
    for a in x.get('aviso', []): notes.append('AVISO: ' + a)
    d = {"niche": ni, "name": x['name'], "phone": wa or x.get('fijo', ''), "phoneType": x.get('ptype') or ("móvil" if wa else ("fijo" if x.get('fijo') else "")),
         "whatsapp": wa, "email": x.get('email', ''), "website": x.get('web', ''), "zone": x['zone'], "address": x.get('address', ''),
         "store": x.get('store', 'none'), "notes": "\n".join(notes), "instagram": f"https://www.instagram.com/{x['ig']}/", "igFollowers": x['f'],
         "centers": x.get('centers', 1), "stage": "new", "flags": [],
         "source": "Scrapeo Instagram +3k seguidores con actividad reciente (15 nov)", "priority": x.get('priority', 80), "region": x['region']}
    if x.get('waOk') is False: d['waOk'] = False
    out.append([lid, d])

w = open(W, encoding='utf-8').read()
m = re.search(r'^const SEED_KEY = "[^"]*";[^\n]*\nconst SEED = \[.*?\];\n', w, re.M | re.S)
assert m
cnt = {}
for _, d in out: cnt[d['niche']] = cnt.get(d['niche'], 0) + 1
desc = ", ".join(f"{v} de {NAMES[k]}" for k, v in cnt.items())
new = f'const SEED_KEY = "seed_20261115";   // 15/11: {len(out)} tiendas con +3k seguidores, publicaciones recientes y sin tienda online o muy floja ({desc}), a Scrapeados\nconst SEED = ' + json.dumps(out, ensure_ascii=False) + ';\n'
w = w[:m.start()] + new + w[m.end():]
open(W, 'w', encoding='utf-8').write(w)
print(len(out), cnt)
