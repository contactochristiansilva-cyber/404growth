# Lote 43: lotes de browser_batch por tienda, cambiando de formato con __fmt(f) (clic en el chip por JS) + Escape real.
# python3 mkbat43b.py <tab> <fmt inicial> <i,i,...> [y del botón de enviar: 686 en la ventana de 745, 741 en la de 801]
import json, sys
tab = int(sys.argv[1]); cur = sys.argv[2]; idx = [int(x) for x in sys.argv[3].split(',')]
Y = int(sys.argv[4]) if len(sys.argv) > 4 else 686
Q = json.load(open('flow/q43.json'))
A = []
K = lambda t, s='Adds the reference': A.append({"name": "computer", "input": {"action": "key", "text": t, "action_summary": s, "tabId": tab}})
J = lambda t: A.append({"name": "javascript_tool", "input": {"action": "javascript_exec", "tabId": tab, "text": t}})
C = lambda: A.append({"name": "computer", "input": {"action": "left_click", "coordinate": [1032, Y], "action_summary": "Sends the image request", "tabId": tab}})
for i in idx:
    f = Q[i]['f']
    if f != cur:
        J(f"await __s(2300); await __fmt('{f}')"); K('Escape', 'Closes the format menu'); cur = f
    n = len(Q[i]['r'])
    if n == 0:
        J(f"await __go0({i})"); C(); continue
    J(f"await __go({i})"); K('Down Return')
    for k in range(1, n):
        J(f"await __gk({i},{k})"); K('Down Return')
    C()
J("await __s(2500); [__F, __busy()]")
print(json.dumps(A, separators=(',', ':')))
