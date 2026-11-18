# Lote 40: lotes de browser_batch para mandar a Flow los trabajos de flow/q40b.json.
# Por trabajo: JS (escribe el texto y busca la 1.ª referencia; devuelve cuántas imágenes tenía ya la petición, debe ser 0)
# + tecla real «Down Return» por referencia + tecla real «Return» para enviar.
# uso: python3 mkbat40.py <tabId> <i0-i1>   (antes, en la pestaña: window.__nimg = () => __ed().parentElement.parentElement.parentElement.querySelectorAll('img').length)
import json, sys
tab = int(sys.argv[1]); a, b = map(int, sys.argv[2].split('-'))
Q = json.load(open('flow/q40b.json'))
A = []
K = lambda t: A.append({"name": "computer", "input": {"action": "key", "text": t, "action_summary": "k", "tabId": tab}})
J = lambda t: A.append({"name": "javascript_tool", "input": {"action": "javascript_exec", "tabId": tab, "text": t}})
for i in range(a, b + 1):
    if not Q[i]['r']:
        J(f"await __s(2000);const n=__nimg();__pt({i});n"); K('Return'); continue
    J(f"await __s(2000);const n=__nimg();__pt({i});await __pr({i},0);n")
    K('Down Return')
    for k in range(1, len(Q[i]['r'])):
        J(f"await __s(700);await __pr({i},{k})"); K('Down Return')
    J("await __s(600);__nimg()") if len(Q[i]['r']) > 1 else None
    K('Return')
A.append({"name": "computer", "input": {"action": "screenshot", "tabId": tab, "scale": 0.3}})
print(json.dumps(A, separators=(',', ':')))
