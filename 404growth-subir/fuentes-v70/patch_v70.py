# v70 · Contabilidad › Archivos. python3 patch_v70.py <worker.js> [salida]
import sys, json, os
D = os.path.dirname(os.path.abspath(__file__))
src = sys.argv[1]; out = sys.argv[2] if len(sys.argv) > 2 else src
w = open(src, encoding='utf-8').read()
assert 'archApi' not in w, 'ya tiene la v70'
srv = open(os.path.join(D, 'arch_server.js'), encoding='utf-8').read()
cli = open(os.path.join(D, 'arch_client.js'), encoding='utf-8').read()
def rep(s, a, b, n=1):
    assert s.count(a) == n, (a[:80], s.count(a)); return s.replace(a, b)
# server
w = rep(w, "\n/* ---------- the admin's API ---------- */", "\n" + srv + "/* ---------- the admin's API ---------- */")
w = rep(w, 'return finApi(req, env, p);   // v67 · contabilidad\n',
        'return finApi(req, env, p);   // v67 · contabilidad\n  if (p === "arch" || p.startsWith("arch/") || p === "archf") return archApi(req, env, p);   // v70 · archivos\n')
# admin page
L = w.split('\n'); i = next(k for k, l in enumerate(L) if l.startswith('const PAGES = '))
P = json.loads(L[i][len('const PAGES = '):-1]); a = P['admin']
a = rep(a, "var CB={tab:'res',", "var CBTABS=[['res','Resumen'],['in','Ingresos'],['out','Gastos'],['arch','Archivos']];\n  var CB={tab:location.hash==='#archivos'?'arch':'res',")
a = rep(a, "function vConta(){return Promise.all(", "function vConta(){if(CB.tab==='arch')return vArch();return Promise.all(")
a = rep(a, "[['res','Resumen'],['in','Ingresos'],['out','Gastos']].map(", "CBTABS.map(")
a = rep(a, "cbAfter();var kq=", "cbAfter();if($('#ar-q'))arFilter();var kq=")
a = rep(a, "if(h==='blog'){S.sec='linkedin';S.liTab='m'}}catch(e){}", "if(h==='blog'){S.sec='linkedin';S.liTab='m'}if(h==='archivos')S.sec='contabilidad'}catch(e){}")
a = rep(a, "window.addEventListener('hashchange',function(){var h=location.hash.replace('#','');",
        "window.addEventListener('hashchange',function(){var h=location.hash.replace('#','');if(h==='archivos'){S.sec='contabilidad';CB.tab='arch';S.client=null;show();return}")
a = rep(a, "\n  function vPend(){", "\n" + cli + "  function vPend(){")
P['admin'] = a
L[i] = 'const PAGES = ' + json.dumps(P, ensure_ascii=False) + ';'
open(out, 'w', encoding='utf-8').write('\n'.join(L))
print('ok', len(w), '->', os.path.getsize(out))
