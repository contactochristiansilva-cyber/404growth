# 10/11/2026: cuatro nichos nuevos en el CRM (cosmética y perfumería, suplementación deportiva, sneakers y ópticas),
# con los mismos textos por defecto que Deporte («vuestros productos»).
import json, re, sys
P_ = sys.argv[1]
w = open(P_, encoding='utf-8').read()

NEW = [('cosmetica', 'Cosmética y perfumería', 'Cosmética', 'tienda de cosmética'),
       ('suplementos', 'Suplementación deportiva', 'Suplementos', 'tienda de suplementos'),
       ('sneakers', 'Sneakers', 'Sneakers', 'tienda de sneakers'),
       ('optica', 'Ópticas', 'Ópticas', 'óptica')]

def rep(s, a, b, n=1):
    c = s.count(a)
    assert c == n, (c, a[:90])
    return s.replace(a, b)

i = w.index('const PAGES = '); j = w.index('\n', i)
P = json.loads(w[i + 14:j].rstrip().rstrip(';'))

for page in ('admin', 'crm'):
    s = P[page]
    s = rep(s, "toys:'Jugueterías',optica:'Ópticas'}", "toys:'Jugueterías'," + ",".join("%s:'%s'" % (k, short) for k, _, short, _ in NEW) + "}")
    s = rep(s, "toys: 'Jugueterías', deporte: 'Deporte' }", "toys: 'Jugueterías', deporte: 'Deporte', " + ", ".join("%s: '%s'" % (k, lab) for k, lab, _, _ in NEW) + " }")
    P[page] = s

c = P['crm']
# textos por defecto: copia de los de Deporte
m = re.search(r"\n    deal_deporte:2500,.*?em1s_deporte:\"(?:[^\"\\]|\\.)*\",", c, re.S)
assert m
blk = m.group(0)
add = ''.join(blk.replace('_deporte:', '_%s:' % k) for k, _, _, _ in NEW)
c = c[:m.end()] + add + c[m.end():]
c = rep(c, "toys:'_toys',deporte:'_deporte'}", "toys:'_toys',deporte:'_deporte'," + ",".join("%s:'_%s'" % (k, k) for k, _, _, _ in NEW) + "}")
c = rep(c, "['toys','Jugueterías'],['deporte','Deporte']]", "['toys','Jugueterías'],['deporte','Deporte']," + ",".join("['%s','%s']" % (k, lab) for k, lab, _, _ in NEW) + "]")
ones = "," + ",".join("%s:1" % k for k, _, _, _ in NEW)
c = rep(c, "var SHOPN={joya:1,moda:1,gourmet:1,obrador:1,deco:1,toys:1,deporte:1}", "var SHOPN={joya:1,moda:1,gourmet:1,obrador:1,deco:1,toys:1,deporte:1" + ones + "}")
c = rep(c, "toys:'juguetería',deporte:'tienda de deporte'}", "toys:'juguetería',deporte:'tienda de deporte'," + ",".join("%s:'%s'" % (k, wd) for k, _, _, wd in NEW) + "}")
c = rep(c, "var ESN={gym:1,real:1,clinic:1,aesth:1,tattoo:1,joya:1,moda:1,gourmet:1,obrador:1,deco:1,toys:1,deporte:1}", "var ESN={gym:1,real:1,clinic:1,aesth:1,tattoo:1,joya:1,moda:1,gourmet:1,obrador:1,deco:1,toys:1,deporte:1" + ones + "}")
c = rep(c, "NOPAGE={real:1,clinic:1,aesth:1,tattoo:1,joya:1,moda:1,gourmet:1,obrador:1,deco:1,toys:1,deporte:1}", "NOPAGE={real:1,clinic:1,aesth:1,tattoo:1,joya:1,moda:1,gourmet:1,obrador:1,deco:1,toys:1,deporte:1" + ones + "}")
c = rep(c, "toys:['tienda','tiendas'],deporte:['tienda','tiendas']}", "toys:['tienda','tiendas'],deporte:['tienda','tiendas']," + ",".join("%s:['tienda','tiendas']" % k for k, _, _, _ in NEW) + "}")
c = rep(c, "var IGN={tattoo:1,joya:1,moda:1,gourmet:1,obrador:1,deco:1,toys:1,deporte:1}", "var IGN={tattoo:1,joya:1,moda:1,gourmet:1,obrador:1,deco:1,toys:1,deporte:1" + ones + "}")
c = rep(c, "deco:9,toys:10,deporte:11}", "deco:9,toys:10,deporte:11," + ",".join("%s:%d" % (k, 12 + n) for n, (k, _, _, _) in enumerate(NEW)) + "}")
P['crm'] = c

w = w[:i] + 'const PAGES = ' + json.dumps(P, ensure_ascii=False) + ';' + w[j:]
open(P_, 'w', encoding='utf-8').write(w)
print('nichos ok', len(w))
