import json, sys
from msg34 import msg, J
TAB = int(sys.argv[1]); s = sys.argv[2]; groups = [g.split(',') for g in sys.argv[3:]]
A = []
W = "await new Promise(r=>setTimeout(r,4000));let t0=Date.now();while(__busy()&&Date.now()-t0<38000)await new Promise(r=>setTimeout(r,1500));__busy()"
for g in groups:
    items = [j for i in g for j in J if j['slug'] == s and j['id'] == i]
    refs, text = msg(items)
    for r in refs:
        A += [dict(name='computer', input=dict(action='left_click', coordinate=[1148, 700], tabId=TAB, action_summary='Opens add-media menu')),
              dict(name='computer', input=dict(action='type', text=r[:-4], tabId=TAB, action_summary='Searches reference')),
              dict(name='computer', input=dict(action='wait', duration=1.5, tabId=TAB)),
              dict(name='javascript_tool', input=dict(action='javascript_exec', tabId=TAB, text='__add()'))]
    A += [dict(name='javascript_tool', input=dict(action='javascript_exec', tabId=TAB, text="const e=document.querySelector('[contenteditable=true]');e.focus();document.activeElement===e")),
          dict(name='computer', input=dict(action='type', text=text, tabId=TAB, action_summary='Types the image prompt')),
          dict(name='computer', input=dict(action='key', text='Return', tabId=TAB, action_summary='Sends the prompt')),
          dict(name='javascript_tool', input=dict(action='javascript_exec', tabId=TAB, text=W)),
          dict(name='javascript_tool', input=dict(action='javascript_exec', tabId=TAB, text=W)),
          dict(name='javascript_tool', input=dict(action='javascript_exec', tabId=TAB, text=W))]
A.append(dict(name='computer', input=dict(action='screenshot', tabId=TAB, scale=0.5)))
print(json.dumps(A, ensure_ascii=False))
