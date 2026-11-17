# Lote 39: lotes de browser_batch para mandar trabajos de q39s.json a Flow (ver flow/flow39.js).
# uso: python3 mkbat39.py <tabId> <i0-i1>  (cada trabajo: __pr por referencia + Down/Return reales, __pt2 + Return real)
import json, sys
tab = int(sys.argv[1]); a, b = map(int, sys.argv[2].split('-'))
Q = json.load(open('flow/q39s.json'))
A = []
K = lambda t: A.append({"name": "computer", "input": {"action": "key", "text": t, "action_summary": "k", "tabId": tab}})
J = lambda t: A.append({"name": "javascript_tool", "input": {"action": "javascript_exec", "tabId": tab, "text": t}})
pre = 'await __s(1500);'
for i in range(a, b + 1):
    for k in range(len(Q[i]['r'])):
        J(f"{pre}await __pr({i},{k})"); K('Down'); K('Return'); pre = 'await __s(700);'
    J(f"{pre}__pt2({i})"); K('Return'); pre = 'await __s(2200);'
A.append({"name": "computer", "input": {"action": "screenshot", "tabId": tab, "scale": 0.3}})
print(json.dumps(A, separators=(',', ':')))
