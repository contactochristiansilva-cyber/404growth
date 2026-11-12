# Lote 35 en el CRM: las 25 ya están en el CRM (lote del 10/11). Solo LEAD_PATCH_KEY nuevo:
# las del LEAD_PATCH anterior (lotes 33 y 34) y las 25 del lote 35 con lotDay = DAY, slug, pageUrl y waOk.
# Solo entran las del lote 35 que ya tienen su propuesta en out/ (p-<slug>.html).
# python3 crm35.py <worker.js> [DAY] [sufijo de la clave]
import json, re, sys, os
W = sys.argv[1]; DAY = sys.argv[2] if len(sys.argv) > 2 else "2026-11-12"; K = sys.argv[3] if len(sys.argv) > 3 else "20261112"
H = os.path.dirname(os.path.abspath(__file__))
src = open(W, encoding='utf-8').read()
def grab(name):
    m = re.search(r'^const %s = (\[.*\]);$' % name, src, re.M); return m, json.loads(m.group(1))
mS, S = grab('SEED'); mP, P = grab('LEAD_PATCH')
idx = {}
for i, d in S:
    for m in re.findall(r'@([\w.]+)', d.get('notes', '')): idx.setdefault(m.lower(), i)
patch = {}
for i, p in P:
    q = dict(p); q['lotDay'] = DAY; patch[i] = q
sel = json.load(open(os.path.join(H, 'sel35.json')))
miss, ok = [], 0
for s in sel:
    lid = idx.get(s['ig'].lower())
    if not lid: miss.append(s['slug'] + ' (sin lead)'); continue
    if not os.path.exists(os.path.join(H, 'out', 'p-%s.html' % s['slug'])): miss.append(s['slug'] + ' (sin página)'); continue
    q = dict(patch.get(lid, {}), lotDay=DAY, slug=s['slug'], pageUrl='https://404growth.com/p/%s/' % s['slug'])
    if s.get('wa') and 'whatsapp' not in (s.get('contact') or '').lower(): q['waOk'] = False
    patch[lid] = q; ok += 1
LP = [[i, p] for i, p in patch.items()]
src = src.replace(mP.group(0), 'const LEAD_PATCH = ' + json.dumps(LP, ensure_ascii=False) + ';')
src = re.sub(r'^const LEAD_PATCH_KEY = .*$', 'const LEAD_PATCH_KEY = "lpatch_%s";   // 12/11: lotes 33 y 34 (sin enviar) y lote 35 al lote del %s, con su pageUrl' % (K, DAY), src, flags=re.M)
open(W, 'w', encoding='utf-8').write(src)
print(ok, 'del lote 35;', len(LP), 'en LEAD_PATCH; faltan:', miss)
