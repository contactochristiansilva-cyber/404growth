#!/usr/bin/env python3
"""v72 · Entregables = fechas de entrega de la tienda con cuenta atrás; lo de antes pasa a «Accesos». Uso: patch_v72.py <worker.js> [salida]"""
import json, sys, os
src_path = sys.argv[1]; out_path = sys.argv[2] if len(sys.argv) > 2 else src_path
here = os.path.dirname(os.path.abspath(__file__))
s = open(src_path, encoding='utf-8').read()
assert 'delivApi' not in s, 'ya tiene la v72'
def rep(old, new, count=1):
    global s
    assert s.count(old) == count, (s.count(old), old[:90])
    s = s.replace(old, new)
# servidor
rep('async function quotesApi(req, env, p) {', open(os.path.join(here, 'dv_server.js'), encoding='utf-8').read() + 'async function quotesApi(req, env, p) {')
rep('if (p === "quotes" || p.startsWith("quotes/")) return quotesApi(req, env, p);',
    'if (p === "quotes" || p.startsWith("quotes/")) return quotesApi(req, env, p);\n  if (p === "deliv" || p.startsWith("deliv/")) return delivApi(req, env, p);   // v72')
# la barra lateral y el menú de secciones (SHELL_JS)
lines = s.split('\n'); i = next(k for k, l in enumerate(lines) if l.startswith('const SHELL_JS = '))
L = lines[i]
def lrep(old, new):
    global L
    assert L.count(old) == 1, (L.count(old), old[:80])
    L = L.replace(old, new)
lrep("['entregables','Accesos y entregables','key','/admin#entregables']", "['entregables','Entregables','clock','/admin#entregables'],['accesos','Accesos','key','/admin#accesos']")
lrep("['entregables','Entregables','Accesos y archivos','/admin#entregables','key','#FFFFFF','#ECE8DD','#3B3A2C']",
     "['entregables','Entregables','Fecha de entrega de cada tienda','/admin#entregables','clock','#2A2F28','#0E100E','#F2C14E'],['accesos','Accesos','Contratos, enlaces y contraseñas','/admin#accesos','key','#FFFFFF','#ECE8DD','#3B3A2C']")
lrep("key:'<circle cx=\\\"8\\\"", "clock:'<circle cx=\\\"12\\\" cy=\\\"12\\\" r=\\\"8.5\\\"/><path d=\\\"M12 7.5V12l3 2\\\"/>',key:'<circle cx=\\\"8\\\"")
lines[i] = L; s = '\n'.join(lines)
# la página del admin
i = s.index('const PAGES = '); j = s.index('\n', i); line = s[i:j]; pre = 'const PAGES = '; body = line[len(pre):]; semi = body.endswith(';')
pages = json.loads(body[:-1] if semi else body); a = pages['admin']
def arep(old, new, count=1):
    global a
    assert a.count(old) == count, (a.count(old), old[:90])
    a = a.replace(old, new)
arep("['entregables','Accesos y entregables']", "['entregables','Entregables'],['accesos','Accesos']")
arep("(S.sec==='entregables'?S.kitSel:", "(S.sec==='accesos'?S.kitSel:")
arep("entregables:vKit,", "entregables:vEnt,accesos:vKit,")
arep("if(d.kgo){S.sec='entregables';", "if(d.kgo){S.sec='accesos';")
arep("if(S.sec==='entregables')S.kitSel='inv'", "if(S.sec==='accesos')S.kitSel='inv'")
arep("S.sec='entregables';S.client=null;S.cred=null;S.kitSel='inv';", "S.sec='accesos';S.client=null;S.cred=null;S.kitSel='inv';")
arep("<h2>Entregables</h2><p>Lo que le das a cada cliente", "<h2>Accesos</h2><p>Lo que le das a cada cliente")
arep("['kit','Entregables']", "['kit','Accesos']")
arep("\">Entregables</button>", "\">Accesos</button>")
arep("«Entregables»", "«Accesos»", 4)
arep("<h3>Entregables de ", "<h3>Accesos de ")
arep("  function vPres(){", open(os.path.join(here, 'dv_client.js'), encoding='utf-8').read() + "  function vPres(){")
assert "'entregables'" in a and a.count("'entregables'") == 1
pages['admin'] = a
s = s[:i] + pre + json.dumps(pages, ensure_ascii=False) + (';' if semi else '') + s[j:]
open(out_path, 'w', encoding='utf-8').write(s)
print('ok', out_path, len(s))
