# python3 patch_l38.py <in.js> <seed3.js> <out.js>
# Lote 38 (17/11/2026) in the admin worker:
#  - SEED2 (same key seed_20261116w, never uploaded) = the 30 of the lote 38 (19 of crm30 without furniture/Matia + 11 new)
#  - LEAD_PATCH (new key lpatch_20261117): slug, pageUrl and lotDay 2026-11-17 for the 30; the old list stays as LEAD_PATCH_16NOV (already applied)
#  - outOnce: the unsent leads of the 16/11 batch go out of the CRM to coll 'leads_out' (reversible), once
import re, sys
src, seed, out = sys.argv[1:4]
s = open(src, encoding='utf-8').read()
n = open(seed, encoding='utf-8').read().split('\n')
new = {l.split(' = ')[0]: l for l in n if l.startswith('const ')}
lines = s.split('\n')

def find(prefix):
    idx = [i for i, l in enumerate(lines) if l.startswith(prefix)]
    assert len(idx) == 1, (prefix, idx)
    return idx[0]

i = find('const SEED2_KEY = '); lines[i] = new['const SEED2_KEY']
i = find('const SEED2 = '); assert lines[i].rstrip().endswith('];'); lines[i] = new['const SEED2']
i = find('const LEAD_PATCH_KEY = ')
lines[i] = new['const LEAD_PATCH_KEY'] + '   // antes lpatch_20261116c (lote 37, ya aplicado: su lista es LEAD_PATCH_16NOV)'
j = find('const LEAD_PATCH = ')
assert lines[j].rstrip().endswith('];')
lines[j] = lines[j].replace('const LEAD_PATCH = ', 'const LEAD_PATCH_16NOV = ', 1)
lines.insert(j + 1, new['const LEAD_PATCH'])
s = '\n'.join(lines)

OUT = '''const LEAD_OUT_KEY = "lout_20261117";   // 17/11 (Chris: «saca del CRM las del lote de hoy que se quedaron sin enviar»): las del lote del 16/11 sin enviar salen del CRM a la colección leads_out (se pueden devolver; los ids quedan en meta)
const LEAD_OUT_DAY = "2026-11-16";
let lmoved = false;
async function outOnce(env) {   /* v77: the unsent leads of one day's batch leave the CRM once; they are kept as coll 'leads_out' */
  if (lmoved || !LEAD_OUT_DAY || (env.DEV && !env.SEED_LOCAL)) return;
  try {
    if (await env.DB.prepare("SELECT v FROM meta WHERE k = ?1").bind(LEAD_OUT_KEY).first()) { lmoved = true; return; }
    const ids = ((await env.DB.prepare("SELECT id FROM docs WHERE coll = 'leads' AND json_extract(data, '$.lotDay') = ?1 AND COALESCE(json_extract(data, '$.stage'), 'new') = 'new' AND json_extract(data, '$.contactedAt') IS NULL").bind(LEAD_OUT_DAY).all()).results || []).map((r) => r.id);
    const j = JSON.stringify(ids);
    await env.DB.batch([
      env.DB.prepare("INSERT INTO docs (coll, id, data, updated) SELECT 'leads_out', id, data, updated FROM docs WHERE coll = 'leads' AND id IN (SELECT value FROM json_each(?1)) ON CONFLICT(coll, id) DO UPDATE SET data = excluded.data, updated = excluded.updated").bind(j),
      env.DB.prepare("DELETE FROM docs WHERE coll = 'leads' AND id IN (SELECT value FROM json_each(?1))").bind(j),
      env.DB.prepare("INSERT INTO meta (k, v) VALUES (?1, ?2) ON CONFLICT(k) DO NOTHING").bind(LEAD_OUT_KEY, j),
      env.DB.prepare("INSERT INTO meta (k, v) VALUES ('crm_rev', '1') ON CONFLICT(k) DO UPDATE SET v = CAST(CAST(v AS INTEGER) + 1 AS TEXT)")
    ]);
    lmoved = true;
  } catch (e) { /* tried again on the next request */ }
}
'''
a = 'let lpatched = false;\nasync function patchOnce(env) {'
assert s.count(a) == 1
s = s.replace(a, OUT + a)
b = '    if (admin) await delOnce(env);\n'
assert s.count(b) == 1
s = s.replace(b, b + '    if (admin) await outOnce(env);\n')
open(out, 'w', encoding='utf-8').write(s)
print('ok', len(s))
