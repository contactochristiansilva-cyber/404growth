#!/usr/bin/env python3
"""v77 · Talento: el sistema de contratación (puestos, candidaturas, nota de la IA, etapas y mensajes).
Uso: patch_v77.py <worker.js> [salida]
Mete tal_server.js (con roles.json dentro, como TAL), las rutas /l/job* y /admin/api/tal*, la sección «Talento» (grupo «Equipo») en la barra
lateral y en el menú, y la vista vTal (tal_client.js)."""
import json, sys, os
src_path = sys.argv[1]; out_path = sys.argv[2] if len(sys.argv) > 2 else src_path
here = os.path.dirname(os.path.abspath(__file__))
s = open(src_path, encoding='utf-8').read()
assert 'async function talApi(' not in s, 'ya tiene la v77'
roles = json.load(open(os.path.join(here, 'roles.json'), encoding='utf-8'))
srv = open(os.path.join(here, 'tal_server.js'), encoding='utf-8').read()
assert srv.count('/*TAL_JSON*/ {}') == 1
srv = srv.replace('/*TAL_JSON*/ {}', json.dumps(roles, ensure_ascii=False, separators=(',', ':')))


def rep(old, new, count=1):
    global s
    assert s.count(old) == count, (s.count(old), old[:90])
    s = s.replace(old, new)


# servidor
rep('async function quotesApi(req, env, p) {', srv + '\nasync function quotesApi(req, env, p) {')
rep('  if (p === "arch" || p.startsWith("arch/") || p === "archf") return archApi(req, env, p);   // v70 · archivos',
    '  if (p === "arch" || p.startsWith("arch/") || p === "archf") return archApi(req, env, p);   // v70 · archivos\n'
    '  if (p === "tal" || p.startsWith("tal/") || p.startsWith("taljob/") || p === "taldev") return talApi(req, env, p, ctx);   // v77 · talento')
rep('  if (path.startsWith("/l/")) return llPublic(req, env, path.slice(3));',
    '  if (/^\\/l\\/job(?:s|cv|t|ts|m|mb|v|vp)?$/.test(path)) return talPublic(req, env, ctx, path.slice(3));   // v77: las páginas de empleo (/equipo)\n'
    '  if (path.startsWith("/l/")) return llPublic(req, env, path.slice(3));')

# la barra lateral, el menú de secciones y las tarjetas de Inicio (SHELL_JS)
lines = s.split('\n'); i = next(k for k, l in enumerate(lines) if l.startswith('const SHELL_JS = '))
L = lines[i]


def lrep(old, new):
    global L
    assert L.count(old) == 1, (L.count(old), old[:80])
    L = L.replace(old, new)


lrep("['presupuestos','Presupuestos','doc','/admin#presupuestos']]],",
     "['presupuestos','Presupuestos','doc','/admin#presupuestos']]],     ['Equipo',[['talento','Talento','hire','/admin#talento']]],")
lrep("['presupuestos','Presupuestos','Pendientes de aceptar','/admin#presupuestos','doc','#F1EBDA','#D6C9A4','#3B3A2C']]],",
     "['presupuestos','Presupuestos','Pendientes de aceptar','/admin#presupuestos','doc','#F1EBDA','#D6C9A4','#3B3A2C']]],\\n"
     "    ['Equipo',[['talento','Talento','Candidaturas y puestos','/admin#talento','hire','#1F2B1C','#0B120A','#D4F27A']]],")
lrep("clock:'<circle cx=\\\"12\\\"",
     "hire:'<circle cx=\\\"10\\\" cy=\\\"8\\\" r=\\\"3.5\\\"/><path d=\\\"M3.5 20c.8-3.6 3.3-5.5 6.5-5.5 1.5 0 2.9.4 4 1.3\\\"/><path d=\\\"M18 13.5v7M14.5 17h7\\\"/>',clock:'<circle cx=\\\"12\\\"")
lines[i] = L; s = '\n'.join(lines)

# la página del admin
i = s.index('const PAGES = '); j = s.index('\n', i); line = s[i:j]; pre = 'const PAGES = '; body = line[len(pre):]; semi = body.endswith(';')
pages = json.loads(body[:-1] if semi else body); a = pages['admin']


def arep(old, new, count=1):
    global a
    assert a.count(old) == count, (a.count(old), old[:90])
    a = a.replace(old, new)


arep("['presupuestos','Presupuestos'],", "['presupuestos','Presupuestos'],['talento','Talento'],")
arep("presupuestos:vPres,", "presupuestos:vPres,talento:vTal,")
arep("  function vPres(){", open(os.path.join(here, 'tal_client.js'), encoding='utf-8').read() + "  function vPres(){")
pages['admin'] = a
s = s[:i] + pre + json.dumps(pages, ensure_ascii=False) + (';' if semi else '') + s[j:]
open(out_path, 'w', encoding='utf-8').write(s)
print('ok', out_path, len(s))
