# python3 patch_c404ev.py <archivo o carpeta> [...]
# 23/11/2026 (v82): el contador de las propuestas expone window.__c404ev(tipo, datos) para que /agenda.js le pase
# los pasos de la agenda (evento «ag»). Lo envía al momento (flush). Se puede pasar dos veces: no repite.
# Solo toca los archivos con el contador v3 (function ev(y,o){o=o||{};o.y=y; y function flush().
import os, re, sys
NEW = 'window.__c404ev=function(y,o){ev(y,o);flush()};'
PAT = re.compile(r'(function sec\(\)\{return Math\.round\(\(Date\.now\(\)-T0\)/1000\)\}\s*)(function ev\(y,o\)\{o=o\|\|\{\};o\.y=y;)')
files = []
for a in sys.argv[1:]:
    if os.path.isdir(a):
        files += [os.path.join(a, f) for f in sorted(os.listdir(a)) if f.endswith('.html')]
    else:
        files.append(a)
done = skip = already = 0
for f in files:
    s = open(f, encoding='utf-8').read()
    if NEW in s:
        already += 1; continue
    if 'function flush(' not in s or len(PAT.findall(s)) != 1:
        skip += 1; continue
    open(f, 'w', encoding='utf-8').write(PAT.sub(lambda m: m.group(1) + NEW + m.group(2), s))
    done += 1
print('cambiados', done, '· ya estaban', already, '· sin contador v3', skip)
