#!/usr/bin/env python3
"""v78 · Briefs: formularios para que un cliente nos cuente su proyecto (el primero, EFAP Miami · Open Day).
Uso: patch_v78.py <worker.js con la v77g> [salida]
Mete brief_server.js (con las preguntas de cada brief dentro, como BRIEF_Q), las rutas /l/brief y /l/briefup, /admin/api/brief*,
«Briefs» en el grupo Ventas de la barra lateral y del Inicio, y la vista vBrief (brief_client.js)."""
import glob
import json
import os
import sys

src_path = sys.argv[1]; out_path = sys.argv[2] if len(sys.argv) > 2 else src_path
here = os.path.dirname(os.path.abspath(__file__))
s = open(src_path, encoding='utf-8').read()
assert 'async function briefApi(' not in s, 'ya tiene la v78'
Q = {}
for f in sorted(glob.glob(os.path.join(here, '*.json'))):
    b = json.load(open(f, encoding='utf-8'))
    if isinstance(b, dict) and b.get('sections'):
        Q[b['id']] = {'id': b['id'], 'name': b['name'], 'sections': [{'id': x['id'], 't': x['t'], 'q': [{k: q[k] for k in ('id', 't', 'type', 'o', 'other', 'nopend', 'web') if k in q} for q in x['q']]} for x in b['sections']]}
assert 'efap-miami' in Q
srv = open(os.path.join(here, 'brief_server.js'), encoding='utf-8').read()
assert srv.count('/*BRIEF_JSON*/ {}') == 1
srv = srv.replace('/*BRIEF_JSON*/ {}', json.dumps(Q, ensure_ascii=False, separators=(',', ':')))


def rep(old, new, count=1):
    global s
    assert s.count(old) == count, (s.count(old), old[:90])
    s = s.replace(old, new)


# servidor
rep('async function quotesApi(req, env, p) {', srv + '\nasync function quotesApi(req, env, p) {')
rep('  if (p === "tal" || p.startsWith("tal/") || p.startsWith("taljob/") || p === "taldev") return talApi(req, env, p, ctx);   // v77 · talento',
    '  if (p === "tal" || p.startsWith("tal/") || p.startsWith("taljob/") || p === "taldev") return talApi(req, env, p, ctx);   // v77 · talento\n'
    '  if (p === "brief" || p.startsWith("brief/")) return briefApi(req, env, p);   // v78 · briefs')
rep('  if (/^\\/l\\/job(?:s|cv|t|ts|m|mb|v|vp)?$/.test(path)) return talPublic(req, env, ctx, path.slice(3));   // v77: las páginas de empleo (/equipo)',
    '  if (/^\\/l\\/job(?:s|cv|t|ts|m|mb|v|vp)?$/.test(path)) return talPublic(req, env, ctx, path.slice(3));   // v77: las páginas de empleo (/equipo)\n'
    '  if (path === "/l/brief" || path === "/l/briefup") return briefPublic(req, env, ctx, path.slice(3));   // v78: los briefs de clientes (/brief/<id>/)')

# la barra lateral y las tarjetas de Inicio (SHELL_JS): «Briefs» en Ventas
lines = s.split('\n'); i = next(k for k, l in enumerate(lines) if l.startswith('const SHELL_JS = '))
L = lines[i]


def lrep(old, new):
    global L
    assert L.count(old) == 1, (L.count(old), old[:80])
    L = L.replace(old, new)


lrep("['landing','Landing /book','chart','/admin/landing']]],",
     "['landing','Landing /book','chart','/admin/landing'],['briefs','Briefs','doc','/admin#briefs']]],")
lrep("['landing','Landing','/book: vídeo, clics y reservas','/admin/landing','chart','#E4ECDB','#C0D1B1','#2F4527']]],",
     "['landing','Landing','/book: vídeo, clics y reservas','/admin/landing','chart','#E4ECDB','#C0D1B1','#2F4527'],['briefs','Briefs','Lo que te cuentan los clientes','/admin#briefs','doc','#F4F0E5','#DAD2BB','#3B3A2C']]],")
lines[i] = L; s = '\n'.join(lines)

# la página del admin
i = s.index('const PAGES = '); j = s.index('\n', i); line = s[i:j]; pre = 'const PAGES = '; body = line[len(pre):]; semi = body.endswith(';')
pages = json.loads(body[:-1] if semi else body); a = pages['admin']


def arep(old, new, count=1):
    global a
    assert a.count(old) == count, (a.count(old), old[:90])
    a = a.replace(old, new)


arep("['presupuestos','Presupuestos'],['talento','Talento'],", "['presupuestos','Presupuestos'],['talento','Talento'],['briefs','Briefs'],")
arep("presupuestos:vPres,talento:vTal,", "presupuestos:vPres,talento:vTal,briefs:vBrief,")
arep("  function vPres(){", open(os.path.join(here, 'brief_client.js'), encoding='utf-8').read() + "  function vPres(){")
pages['admin'] = a
s = s[:i] + pre + json.dumps(pages, ensure_ascii=False) + (';' if semi else '') + s[j:]
open(out_path, 'w', encoding='utf-8').write(s)
print('ok', out_path, len(s), 'briefs:', ', '.join(Q))
