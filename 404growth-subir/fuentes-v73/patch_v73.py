#!/usr/bin/env python3
"""v73 · Entregables solo con los clientes que han pagado (cobro marcado en Facturación). Parte de la v72.
Uso: patch_v73.py <worker.js> [salida]"""
import json, sys, os
src_path = sys.argv[1]; out_path = sys.argv[2] if len(sys.argv) > 2 else src_path
here = os.path.dirname(os.path.abspath(__file__))
s = open(src_path, encoding='utf-8').read()
assert 'delivApi' in s, 'falta la v72'
assert 'DELIV_FROM' not in s, 'ya tiene la v73'
# servidor: se cambia el bloque entero de la v72 (desde su comentario hasta quotesApi)
a0 = s.index('/* ---------- v72 · Entregables (14/11/2026)'); a1 = s.index('async function quotesApi(req, env, p) {')
assert a0 < a1 and s.count('async function delivApi(') == 1 and a0 < s.index('async function delivApi(') < a1
s = s[:a0] + open(os.path.join(here, 'dv_server.js'), encoding='utf-8').read() + s[a1:]
# la página del admin: se cambia la vista de la v72
i = s.index('const PAGES = '); j = s.index('\n', i); line = s[i:j]; pre = 'const PAGES = '; body = line[len(pre):]; semi = body.endswith(';')
pages = json.loads(body[:-1] if semi else body); a = pages['admin']
b0 = a.index('  /* ---------- v72 · Entregables: la fecha'); b1 = a.index('  function vPres(){')
assert b0 < b1 and a.count('function vEnt(){') == 1
a = a[:b0] + open(os.path.join(here, 'dv_client.js'), encoding='utf-8').read() + a[b1:]
assert a.count('function vEnt(){') == 1 and a.count('var DV={open:null}') == 1
pages['admin'] = a
s = s[:i] + pre + json.dumps(pages, ensure_ascii=False) + (';' if semi else '') + s[j:]
open(out_path, 'w', encoding='utf-8').write(s)
print('ok', out_path, len(s))
