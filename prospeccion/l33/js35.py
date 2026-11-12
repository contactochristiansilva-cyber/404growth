"""Lote 35: JS para la pestaña de Flow con los mensajes de una tienda ya armados (frases repetidas comprimidas con §NN).
  python3 js35.py --tok        → guarda el diccionario (localStorage.__tok35) y define __go35 (adjunta referencias y escribe el mensaje)
  python3 js35.py <slug> ...   → window.__Q35[slug] = [{refs, text}] (un elemento por mensaje, agrupados como bat35.groups)
Después, por mensaje: __go35(slug, k) → tecla Return real → esperar a que el agente termine (__busy)."""
import json, re, sys, collections
from bat35 import J, msg, groups

def sentences(t):
    return [s.strip() for s in re.split(r'(?<=[.:])\s+', t) if s.strip()]

C = collections.Counter(s for j in J for s in set(sentences(j['text'])))
TOK = sorted([s for s, n in C.items() if n >= 4 and len(s) >= 30], key=len, reverse=True)
TOK += ['Genera 3 imágenes separadas con Nano Banana 2.1, cada una en su formato y con su referencia adjunta.',
        'Genera 2 imágenes separadas con Nano Banana 2.1, cada una en su formato y con su referencia adjunta.',
        ' from the reference', ' (formato 3:4, referencia ', ' (formato 16:9, referencia ']


def comp(t):
    for k, p in enumerate(TOK):
        t = t.replace(p, f'§{k:02d}')
    return t


GO = r"""
window.__X35=t=>t.replace(/§(\d\d)/g,(m,k)=>JSON.parse(localStorage.__tok35)[+k]);
window.__Q35=window.__Q35||{};
window.__go35=async function(s,k){const m=__Q35[s][k];const bp=__btn35('Borrar petición');if(bp){bp.click();await __sl(500)}
 if(m.refs.length){const r=await __att35(m.refs);if(/noinp|noitem/.test(r)||!r.endsWith('chips='+m.refs.length))throw new Error('attach '+r)}
 const e=__ed();e.focus();document.execCommand('insertText',false,__X35(m.text));await __sl(300);
 const n=e.innerText.length;if(n<100)throw new Error('text '+n);return s+' '+k+'/'+__Q35[s].length+' chips='+__chips35()+' len='+n};
window.__jt35=function(s){const out=[];for(const m of __Q35[s]){const t=__X35(m.text);if(m.ids.length===1){out.push([s,m.ids[0],__tok(t.slice(t.indexOf(': ')+2))])}else{const parts=t.split(/IMAGEN \d+ «/).slice(1);parts.forEach((p,k)=>{out.push([s,m.ids[k],__tok(p.slice(p.indexOf('): ')+3))])})}}window.__JT=(window.__JT||[]).filter(x=>x[0]!==s).concat(out);return out.length};
window.__wait35=async function(ms){await __sl(5000);let t0=Date.now();while(__busy()&&Date.now()-t0<ms)await __sl(1500);return __busy()?'busy':'free'};
"""

if __name__ == '__main__':
    if sys.argv[1] == '--tok':
        print('localStorage.__tok35=%s;%s"tok "+JSON.parse(localStorage.__tok35).length' % (json.dumps(json.dumps(TOK, ensure_ascii=False), ensure_ascii=False), GO))
    else:
        out = []
        for s in sys.argv[1:]:
            Q = []
            for g in groups(s):
                items = [j for i in g for j in J if j['slug'] == s and j['id'] == i]
                refs, text = msg(items)
                Q.append(dict(ids=g, refs=[r[:-4] for r in refs], text=comp(text)))
            out.append('__Q35[%s]=%s;' % (json.dumps(s), json.dumps(Q, ensure_ascii=False)))
            print(s, len(Q), [g for g in groups(s)], file=sys.stderr)
        print('window.__Q35=window.__Q35||{};' + ''.join(out) + '"Q "+Object.keys(__Q35).join(",")')
