# Lote 34 en el CRM: escribe en el worker del admin un SEED_KEY nuevo (SEED de siempre + las perfumerías nuevas de nuevos34.json)
# y un LEAD_PATCH_KEY nuevo: las 50 del lote 33 y las del lote 34 con lotDay = DAY, slug y pageUrl.
# Solo entran las del lote 34 que ya tienen su propuesta en out/ (p-<slug>.html).
# python3 crm34.py <worker.js> [DAY]
import json, re, sys, os
W = sys.argv[1]; DAY = sys.argv[2] if len(sys.argv) > 2 else '2026-11-11'
H = os.path.dirname(os.path.abspath(__file__))
src = open(W, encoding='utf-8').read()
def grab(name):
    m = re.search(r'^const %s = (\[.*\]);$' % name, src, re.M); return m, json.loads(m.group(1))
mS, S = grab('SEED'); mP, P = grab('LEAD_PATCH')
ids = {i for i, _ in S}
new = json.load(open(os.path.join(H, 'nuevos34.json'))) if os.path.exists(os.path.join(H, 'nuevos34.json')) else []
for n in new:
    if n['id'] not in ids: S.append([n['id'], n['lead']]); ids.add(n['id'])
sel = json.load(open(os.path.join(H, 'sel34.json')))
idx = {}
for i, d in S:
    for m in re.findall(r'@([\w.]+)', d.get('notes', '')): idx.setdefault(m.lower(), i)
patch = {}
for i, p in P:   # las del lote 33: al lote de DAY (las ya enviadas no salen en el lote por su etapa)
    q = dict(p); q['lotDay'] = DAY; patch[i] = q
miss = []
for s in sel + [n['sel'] for n in new]:
    lid = idx.get(s['ig'].lower())
    if not lid: miss.append(s['slug'] + ' (sin lead)'); continue
    if not os.path.exists(os.path.join(H, 'out', 'p-%s.html' % s['slug'])): miss.append(s['slug'] + ' (sin página)'); continue
    patch[lid] = dict(patch.get(lid, {}), lotDay=DAY, slug=s['slug'], pageUrl='https://404growth.com/p/%s/' % s['slug'])
LP = [[i, p] for i, p in patch.items()]
src = src.replace(mS.group(0), 'const SEED = ' + json.dumps(S, ensure_ascii=False) + ';')
src = re.sub(r'^const SEED_KEY = .*$', 'const SEED_KEY = "seed_20261111";   // 11/11: el SEED de seed_20261110b + %d perfumerías nuevas del lote 34' % len(new), src, flags=re.M)
mP, _ = grab('LEAD_PATCH')
src = src.replace(mP.group(0), 'const LEAD_PATCH = ' + json.dumps(LP, ensure_ascii=False) + ';')
src = re.sub(r'^const LEAD_PATCH_KEY = .*$', 'const LEAD_PATCH_KEY = "lpatch_20261111";   // 11/11: lote 33 (sin enviar) y lote 34 al lote del %s, con su pageUrl' % DAY, src, flags=re.M)
open(W, 'w', encoding='utf-8').write(src)
print(len(S), 'en SEED;', len(LP), 'en LEAD_PATCH; faltan:', miss)
