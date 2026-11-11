# Una propuesta del lote 33/34 en un solo .html para verla sin publicar (tienda incluida en los marcos).
# python3 inline34.py <dir out> <slug> <salida.html>
import sys, re, os, io, base64, json
from PIL import Image
D, s, OUT = sys.argv[1:4]
cache = {}
def uri(path):
    p = os.path.join(D, path.lstrip('/'))
    if p in cache: return cache[p]
    if not os.path.exists(p): cache[p] = path; return path
    if p.endswith('.svg'): u = 'data:image/svg+xml;base64,' + base64.b64encode(open(p, 'rb').read()).decode()
    else:
        im = Image.open(p); im = im.convert('RGBA' if p.endswith('.png') else 'RGB'); im.thumbnail((1400, 1400))
        b = io.BytesIO(); fmt = 'PNG' if p.endswith('.png') else 'JPEG'
        im.save(b, fmt, **({} if fmt == 'PNG' else dict(quality=78)))
        u = f'data:image/{fmt.lower()};base64,' + base64.b64encode(b.getvalue()).decode()
    cache[p] = u; return u
IMG = re.compile(r'/(?:p-[a-z0-9-]+--b--[a-z0-9.-]+|christian-hola\.jpg|favicon\.svg)')
store = open(os.path.join(D, f'p-{s}--tienda.html'), encoding='utf-8').read()
store = IMG.sub(lambda m: uri(m.group(0)), store).replace('location.search', '__QS')
store = store.replace('<head>', '<head><script>var __QS="__QSV__";</script>', 1)
page = open(os.path.join(D, f'p-{s}.html'), encoding='utf-8').read()
page = IMG.sub(lambda m: uri(m.group(0)), page)
js = ('<script>(function(){var S=%s;var B={};document.querySelectorAll("iframe[data-src]").forEach(function(f){var q=(f.getAttribute("data-src").split("?")[1]||"");'
      'if(!B[q])B[q]=URL.createObjectURL(new Blob([S.replace("__QSV__","?"+q)],{type:"text/html"}));f.setAttribute("data-src",B[q])})})();</script>') % json.dumps(store, ensure_ascii=False).replace('</', '<\\/')
i = page.rfind('</body>'); page = page[:i] + js + page[i:]
open(OUT, 'w', encoding='utf-8').write(page)
print(s, round(os.path.getsize(OUT) / 1e6, 1), 'MB')
