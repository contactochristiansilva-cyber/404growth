# Lote 42: lotes de browser_batch para Flow (como mkbat40c.py, con la caja de peticiones nueva: enviar en (1032, 686)).
# python3 mkbat42.py <tab> <a-b,c,...>
import json, sys
tab = int(sys.argv[1]); idx = []
for part in sys.argv[2].split(','):
    a, _, b = part.partition('-'); idx += list(range(int(a), int(b or a) + 1))
Q = json.load(open('flow/q42.json'))
A = []
K = lambda t: A.append({"name": "computer", "input": {"action": "key", "text": t, "action_summary": "Adds the reference", "tabId": tab}})
J = lambda t: A.append({"name": "javascript_tool", "input": {"action": "javascript_exec", "tabId": tab, "text": t}})
C = lambda: A.append({"name": "computer", "input": {"action": "left_click", "coordinate": [1032, 686], "action_summary": "Sends the image request", "tabId": tab}})
for i in idx:
    n = len(Q[i]['r'])
    if n == 0:
        J(f"await __go0({i})"); C(); continue
    J(f"await __go({i})"); K('Down Return')
    for k in range(1, n):
        J(f"await __gk({i},{k})"); K('Down Return')
    C()
print(json.dumps(A, separators=(',', ':')))
