"""Una propuesta en un solo .html (imágenes y letras dentro) para verla sin publicar. uso: inline32.py <slug> ... → l32/html/<slug>.html"""
import base64, io, os, re, sys
from PIL import Image
L31 = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); OUT = os.path.join(L31, 'out')
WEB = '/home/claude/404growth/web117-404growth'
MAX = {'h': 1800, 'l5': 1600, 'antes': 1280, 'despues': 1280}


def img(name):
    p = os.path.join(OUT, name)
    if name.endswith('.png'):
        return 'data:image/png;base64,' + base64.b64encode(open(p, 'rb').read()).decode()
    key = re.sub(r'^p-[a-z0-9-]+--(b--)?', '', name)[:-4]
    im = Image.open(p).convert('RGB'); m = MAX.get(key, 1000)
    if max(im.size) > m: im.thumbnail((m, m), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, 'JPEG', quality=80, optimize=True, progressive=True)
    return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()


def font(rel):
    return 'data:font/woff2;base64,' + base64.b64encode(open(os.path.join(WEB, rel), 'rb').read()).decode()


for s in sys.argv[1:]:
    h = open(os.path.join(OUT, f'p-{s}.html')).read(); cache = {}
    def sub(m):
        n = m.group(2)
        if n not in cache:
            cache[n] = img(n)
        return m.group(1) + cache[n]
    h = re.sub(r'(src="|url\()/(p-[a-z0-9-]+--[a-z0-9-]+\.(?:jpg|png))', sub, h)
    h = h.replace('url(/inter-tight.woff2)', 'url(' + font('inter-tight.woff2') + ')').replace('url(/_f/tenor.woff2)', 'url(' + font('_f/tenor.woff2') + ')')
    h = h.replace('href="/favicon.svg"', 'href="data:image/svg+xml;base64,' + base64.b64encode(open(os.path.join(WEB, 'favicon.svg'), 'rb').read()).decode() + '"')
    os.makedirs(os.path.join(L31, 'l32', 'html'), exist_ok=True)
    o = os.path.join(L31, 'l32', 'html', f'{s}.html'); open(o, 'w').write(h)
    left = re.findall(r'(?:src="|url\()/[^")]+', h)
    print(s, round(os.path.getsize(o) / 1e6, 1), 'MB', 'quedan rutas:' if left else '', left[:3])
