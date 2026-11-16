# Una propuesta del lote 37 (tienda A) en un solo .html para verla sin publicar.
# Como inline34.py, pero las fotos de la tienda van una sola vez (la tienda se repite muchas): se guardan en
# window.__IM y se ponen al montar cada marco. python3 inline37.py <dir out> <slug> <salida.html>
import sys, re, os, io, base64
from PIL import Image
D, s, OUT = sys.argv[1:4]
cache = {}
def uri(path):
    p = os.path.join(D, path.lstrip('/'))
    if p in cache: return cache[p]
    if not os.path.exists(p): cache[p] = path; return path
    if p.endswith('.svg'): u = 'data:image/svg+xml;base64,' + base64.b64encode(open(p, 'rb').read()).decode()
    else:
        im = Image.open(p); im = im.convert('RGBA' if p.endswith('.png') else 'RGB'); im.thumbnail((1100, 1100))
        b = io.BytesIO(); fmt = 'PNG' if p.endswith('.png') else 'JPEG'
        im.save(b, fmt, **({} if fmt == 'PNG' else dict(quality=74)))
        u = f'data:image/{fmt.lower()};base64,' + base64.b64encode(b.getvalue()).decode()
    cache[p] = u; return u
IMG = re.compile(r'/(?:p-[a-z0-9-]+--b--[a-z0-9.-]+|christian-hola\.jpg|favicon\.svg)')
store = open(os.path.join(D, f'p-{s}--tienda.html'), encoding='utf-8').read()
keys = []
def tok(m):
    k = m.group(0)
    if k not in keys: keys.append(k)
    return f'__IM{keys.index(k)}__'
store = IMG.sub(tok, store).replace('location.search', '__QS')
store = store.replace('<head>', '<head><script>var __QS="__QSV__";</script>', 1)
page = open(os.path.join(D, f'p-{s}.html'), encoding='utf-8').read()
page = IMG.sub(lambda m: uri(m.group(0)), page)
L0 = "function L(f){if(!f.src)f.src=f.dataset.src}"
assert L0 in page
page = page.replace(L0, "function L(f){if(!f.__l){f.__l=1;f.srcdoc=window.__S34.replace('__QSV__','?'+(f.dataset.src.split('?')[1]||'')).replace(/__IM(\\d+)__/g,function(m,k){return window.__IM[k]})}}")
im = '[' + ','.join('"%s"' % uri(k) for k in keys) + ']'
js = ('<script>window.__IM=%s;window.__S34=new TextDecoder().decode(Uint8Array.from(atob("%s"),function(c){return c.charCodeAt(0)}));</script>'
      % (im, base64.b64encode(store.encode('utf-8')).decode()))
i = page.find('</head>'); page = page[:i] + js + page[i:]
open(OUT, 'w', encoding='utf-8').write(page)
print(s, round(os.path.getsize(OUT) / 1e6, 1), 'MB')
