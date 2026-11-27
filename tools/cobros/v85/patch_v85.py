# v85 (27/11/2026): avisos al móvil de las mensualidades (el día antes y el mismo día). Uso: patch_v85.py <worker> <salida>
import sys, os
src, out = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
srv = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'br_server.js'), encoding='utf-8').read()
assert 'async function billRemind' not in s, 'ya aplicado'
a = "  try { await callCron(env); } catch (e) { /* v48: reminders, «did he come?», the ad spend */ }\n"
assert s.count(a) == 1
s = s.replace(a, a + "  try { await billRemind(env); } catch (e) { /* v85: avisos de las mensualidades; never stops the rest */ }\n")
b = "async function scheduledRun(env) {"
assert s.count(b) == 1
s = s.replace(b, srv.strip() + "\n\n" + b)
open(out, 'w', encoding='utf-8').write(s)
print('ok')
