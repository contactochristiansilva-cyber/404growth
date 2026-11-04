"""Lote 32: encargos en rejilla 3x3 (4 llamadas, 0,09 $ por tienda), imágenes, página y capturas.
uso: python3 run32.py <slug> ...   (salta lo que ya existe; el log va a ai/log.txt)"""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import jobs_lib, jobs_all
jobs_lib.GRID = 3
L31 = jobs_lib.L31; slugs = sys.argv[1:]; J = []
for s in slugs:
    j = jobs_all.S[s](s); json.dump(j, open(f'{L31}/ai/jobs_{s}.json', 'w')); J += j
batch = f'{L31}/ai/_batch32.json'; json.dump(J, open(batch, 'w'))
print('encargos', len(J), flush=True)
subprocess.run([sys.executable, os.path.join(HERE, 'runjobs.py'), batch, '12'], check=True)
ok = [s for s in slugs if all(os.path.exists(f'{L31}/ai/{s}/{i}.jpg') for i in ['hero', 'l5', 'look', 'p1', 'p2', 'p3', 'p4', 'p5', 'x1', 'x2', 'x3', 'l1', 'l2', 'l3', 'l4'])]
print('con todas las fotos:', ok, 'sin:', [s for s in slugs if s not in ok], flush=True)
if ok:
    subprocess.run([sys.executable, os.path.join(HERE, 'gen.py')] + ok, check=True)
    subprocess.run([sys.executable, os.path.join(HERE, 'shots.py')] + ok, check=True)
