# python3 patch_l39.py <in.js> <rows18.js> <out.js>
# 17/11/2026 (for the 18/11) in the admin worker:
#  - four new CRM niches: merceria (mercería, lanas y telas), arte (bellas artes y scrap), artesania and electro,
#    with the same default texts as Deporte (same steps as scrapeo-10nov/patch_niches.py, anchored after «optica»)
#  - SEED3 (key seed_20261118): the 30 of candidatos.json, as a third list in seedOnce
#  - LEAD_PATCH (key lpatch_20261118): the 5 unsent of the lote 38 to the batch of 18/11; the old list stays as LEAD_PATCH_17NOV
import json, re, sys
src, rows, out = sys.argv[1:4]
w = open(src, encoding='utf-8').read()
new = {l.split(' = ')[0]: l for l in open(rows, encoding='utf-8').read().split('\n') if l.startswith('const ')}

NEW = [('merceria', 'Mercería, lanas y telas', 'Mercería', 'mercería'),
       ('arte', 'Bellas artes y scrap', 'Bellas artes', 'tienda de bellas artes'),
       ('artesania', 'Artesanía', 'Artesanía', 'taller artesano'),
       ('electro', 'Electrodomésticos', 'Electro', 'tienda de electrodomésticos')]

def rep(s, a, b, n=1):
    c = s.count(a)
    assert c == n, (c, a[:90])
    return s.replace(a, b)

# 1. niches inside PAGES (one JSON line)
i = w.index('const PAGES = '); j = w.index('\n', i)
raw = w[i + 14:j].rstrip()
assert raw.endswith(';')
P = json.loads(raw[:-1])
assert json.dumps(P, ensure_ascii=False) == raw[:-1], 'PAGES does not round-trip'
ones = ''.join(",%s:1" % k for k, _, _, _ in NEW)
for page in ('admin', 'crm'):
    s = P[page]
    s = rep(s, "sneakers:'Sneakers',optica:'Ópticas'}", "sneakers:'Sneakers',optica:'Ópticas'," + ",".join("%s:'%s'" % (k, short) for k, _, short, _ in NEW) + "}")
    s = rep(s, "sneakers: 'Sneakers', optica: 'Ópticas' }", "sneakers: 'Sneakers', optica: 'Ópticas', " + ", ".join("%s: '%s'" % (k, lab) for k, lab, _, _ in NEW) + " }")
    P[page] = s
c = P['crm']
m = re.search(r"\n    deal_deporte:2500,.*?em1s_deporte:\"(?:[^\"\\]|\\.)*\",", c, re.S)
assert m
blk = m.group(0)
assert blk.count('_deporte:') >= 5
c = c[:m.end()] + ''.join(blk.replace('_deporte:', '_%s:' % k) for k, _, _, _ in NEW) + c[m.end():]
c = rep(c, "optica:'_optica'}", "optica:'_optica'," + ",".join("%s:'_%s'" % (k, k) for k, _, _, _ in NEW) + "}")
c = rep(c, "['optica','Ópticas']]", "['optica','Ópticas']," + ",".join("['%s','%s']" % (k, lab) for k, lab, _, _ in NEW) + "]")
for pre in ('var SHOPN={', 'var ESN={', 'NOPAGE={', 'var IGN={'):
    a = c.index(pre); b = c.index('}', a)
    seg = c[a:b + 1]
    assert seg.endswith(',optica:1}'), (pre, seg[-40:])
    c = c[:a] + seg[:-1] + ones + '}' + c[b + 1:]
c = rep(c, "optica:'óptica'}", "optica:'óptica'," + ",".join("%s:'%s'" % (k, wd) for k, _, _, wd in NEW) + "}")
c = rep(c, "optica:['tienda','tiendas']}", "optica:['tienda','tiendas']," + ",".join("%s:['tienda','tiendas']" % k for k, _, _, _ in NEW) + "}")
c = rep(c, "optica:15}", "optica:15," + ",".join("%s:%d" % (k, 16 + n) for n, (k, _, _, _) in enumerate(NEW)) + "}")
P['crm'] = c
w = w[:i] + 'const PAGES = ' + json.dumps(P, ensure_ascii=False) + ';' + w[j:]

# 2. SEED3 after SEED2, and a third list in seedOnce
lines = w.split('\n')
def find(prefix):
    idx = [k for k, l in enumerate(lines) if l.startswith(prefix)]
    assert len(idx) == 1, (prefix, idx)
    return idx[0]
k = find('const SEED2 = ')
assert lines[k].rstrip().endswith('];')
lines[k + 1:k + 1] = [new['const SEED3_KEY'], new['const SEED3']]
# 3. LEAD_PATCH: the 17/11 list keeps its data under another name; the new one goes after it
k = find('const LEAD_PATCH_KEY = ')
lines[k] = new['const LEAD_PATCH_KEY'] + '   // antes lpatch_20261117 (lote 38, ya aplicado: su lista es LEAD_PATCH_17NOV)'
k = find('const LEAD_PATCH = ')
assert lines[k].rstrip().endswith('];')
lines[k] = lines[k].replace('const LEAD_PATCH = ', 'const LEAD_PATCH_17NOV = ', 1)
lines.insert(k + 1, new['const LEAD_PATCH'])
w = '\n'.join(lines)
w = rep(w, "for (const [KEY, LIST] of [[SEED_KEY, SEED], [SEED2_KEY, SEED2]]) {", "for (const [KEY, LIST] of [[SEED_KEY, SEED], [SEED2_KEY, SEED2], [SEED3_KEY, SEED3]]) {")
w = rep(w, "/* v76: two lists, each inserted once with its own key (SEED2 = 16/11, so the old SEED is never re-run) */",
        "/* v76: several lists, each inserted once with its own key (SEED2 = 16/11, SEED3 = 18/11), so an old list is never re-run */")
open(out, 'w', encoding='utf-8').write(w)
print('ok', len(w))
