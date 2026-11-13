"""Lote 36 (como el 35, sin hd/hm): acciones de browser_batch para mandar al agente de Flow los mensajes de una tienda (1 a 3 imágenes por mensaje, como en el lote 34).
uso: python3 bat35.py <tabId> <slug> [ids,ids ...]   (sin grupos: agrupa solo h, p1…p6, l1, l2, b, hd, hm en mensajes de ≤3 imágenes y ≤3 referencias)
Cada referencia se añade con clics reales: «+» (1148,700) → escribe el nombre → primer resultado (942,107)."""
import json, sys
J = json.load(open('flow/jobs36.json'))
ORDER = ['h', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'l1', 'l2', 'b']


def msg(items):
    refs = []
    for j in items:
        for r in j['refs']:
            if r not in refs:
                refs.append(r)
    if len(items) == 1:
        j = items[0]
        t = (f'Genera 1 imagen con Nano Banana 2.1 en formato {j["fmt"]} '
             + ('usando la referencia adjunta: ' if len(j['refs']) == 1 else 'usando las referencias adjuntas: ' if j['refs'] else 'sin referencia: ') + j['text'])
    else:
        t = (f'Genera {len(items)} imágenes separadas con Nano Banana 2.1, cada una en su formato y con su referencia adjunta. '
             + ' '.join(f'IMAGEN {k} «{j["id"]}» (formato {j["fmt"]}, ' + (f'referencia {", ".join(j["refs"])}' if j['refs'] else 'sin referencia') + f'): {j["text"]}'
                        for k, j in enumerate(items, 1)))
    return refs, t


def groups(s):
    jj = {j['id']: j for j in J if j['slug'] == s}
    out, cur, cr = [], [], []
    for i in ORDER:
        j = jj[i]
        u = cr + [r for r in j['refs'] if r not in cr]
        if cur and (len(cur) >= 3 or len(u) > 3):
            out.append(cur); cur, cr = [], []
            u = list(j['refs'])
        cur.append(i); cr = u
    if cur:
        out.append(cur)
    return out


if __name__ == '__main__':
    TAB = int(sys.argv[1]); s = sys.argv[2]
    NEW = '--new' in sys.argv
    if NEW: sys.argv.remove('--new')
    G = [g.split(',') for g in sys.argv[3:]] or groups(s)
    W = "await new Promise(r=>setTimeout(r,5000));let t0=Date.now();while(__busy()&&Date.now()-t0<40000)await new Promise(r=>setTimeout(r,1500));__busy()"
    W2 = "let t0=Date.now();while(__busy()&&Date.now()-t0<40000)await new Promise(r=>setTimeout(r,1500));if(__busy())throw new Error('busy');'free'"
    A = []
    if NEW:
        A += [dict(name='javascript_tool', input=dict(action='javascript_exec', tabId=TAB, text="__btn35('Borrar petición')&&__btn35('Borrar petición').click();'ok'")),
              dict(name='computer', input=dict(action='left_click', coordinate=[1391, 100], tabId=TAB, action_summary='Starts a new agent chat session')),
              dict(name='computer', input=dict(action='wait', duration=1.5, tabId=TAB))]
    for g in G:
        items = [j for i in g for j in J if j['slug'] == s and j['id'] == i]
        refs, text = msg(items)
        if refs:
            A.append(dict(name='javascript_tool', input=dict(action='javascript_exec', tabId=TAB,
                     text="const r=await __att35(%s);if(/noinp|noitem/.test(r)||!r.endsWith('chips=%d'))throw new Error('attach '+r);r" % (json.dumps([x[:-4] for x in refs]), len(refs)))))
        A += [dict(name='javascript_tool', input=dict(action='javascript_exec', tabId=TAB, text="const e=[...document.querySelectorAll('[contenteditable=true]')].pop();e.focus();document.activeElement===e")),
              dict(name='computer', input=dict(action='type', text=text, tabId=TAB, action_summary='Types the image prompt')),
              dict(name='computer', input=dict(action='key', text='Return', tabId=TAB, action_summary='Sends the prompt to the Flow agent')),
              dict(name='javascript_tool', input=dict(action='javascript_exec', tabId=TAB, text=W)),
              dict(name='javascript_tool', input=dict(action='javascript_exec', tabId=TAB, text=W2))]
    A.append(dict(name='computer', input=dict(action='screenshot', tabId=TAB, scale=0.5)))
    print(json.dumps(A, ensure_ascii=False))
    print(len(G), 'mensajes', G, file=sys.stderr)
