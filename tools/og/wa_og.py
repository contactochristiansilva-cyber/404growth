"""Miniatura del enlace de cada propuesta en WhatsApp (og:image), opción C que eligió Chris el 18/11/2026:
la foto de la portada de su tienda a todo el ancho, oscurecida a la izquierda, con «<Tienda>, abierta 24 horas.»
en blanco, la píldora «Propuesta para vosotros» y «Christian · 404 Growth» abajo. 1200x630, SF Pro.

Tres pasos (la letra SF Pro solo está en el Mac, así que la foto se saca con el Playwright del Mac):
  1. python3 wa_og.py src  <carpeta web> <carpeta src> [--solo a,b]   -> <src>/<slug>.html + <src>/lista.json
  2. en el Mac: render_mac.js (Playwright del Mac) pasa cada <src>/<slug>.html a <web>/p-<slug>--wa.jpg
  3. python3 wa_og.py meta <carpeta web> [--solo a,b] [--forzar]       -> og:title, og:description y og:image
     (solo en las que ya tienen su p-<slug>--wa.jpg; si no, la propuesta se queda con su miniatura de antes)

Solo toca las propuestas de tienda online (p-<slug>.html con la agenda, <!--ag-->). Se puede repetir.
El nombre de la imagen es nuevo (--wa.jpg) para que ni WhatsApp ni Cloudflare enseñen la vieja.
"""
import html, json, os, re, sys

FONT = "-apple-system,BlinkMacSystemFont,'SF Pro Display','SF Pro Text',Inter,'Helvetica Neue',Arial,sans-serif"
DESC = 'Así se vería vuestra tienda online, con vuestros productos. Os la he preparado: echadle un vistazo.'


def props(web, solo=None):
    for f in sorted(os.listdir(web)):
        if not (f.startswith('p-') and f.endswith('.html')) or '--' in f:
            continue
        s = f[2:-5]
        if solo and s not in solo:
            continue
        h = open(os.path.join(web, f), encoding='utf-8').read()
        if '<!--ag-->' not in h:
            continue
        t = html.unescape(re.search(r'<title>(.*?)</title>', h, re.S).group(1))
        yield s, re.sub(r' · vuestra tienda online$', '', t.split(' × ')[0].strip(), flags=re.I), h   # v42: «X · vuestra tienda online»


def size(path):
    try:
        from PIL import Image
        return Image.open(path).size
    except Exception:
        return (1600, 900)


def hero(web, s):
    """La foto de su portada: la de la tienda nueva (hd, h) o la del hero de la v32 (vN--hero, la más nueva).
    Si no hay (propuestas del lote 30), la foto más grande de las suyas (a--*), nunca la captura de la tienda (a--tienda)
    ni la miniatura vieja (a--og). Devuelve (archivo, ancho/alto)."""
    def ok(f):
        w, h = size(os.path.join(web, f))
        return f, w / float(h)
    for k in ('b--hd', 'b--h'):
        for ext in ('jpg', 'webp'):   # las propuestas v42 (gen42.py) solo llevan .webp
            f = 'p-%s--%s.%s' % (s, k, ext)
            if os.path.exists(os.path.join(web, f)):
                return ok(f)
    vs = sorted((int(m.group(1)), f) for f in os.listdir(web) for m in [re.match(r'p-%s--v(\d+)--hero\.jpg$' % re.escape(s), f)] if m)
    if vs:
        return ok(vs[-1][1])
    own = [f for f in os.listdir(web) if re.match(r'p-%s--(?:a|b)--(?!og\.|tienda\.|logo)[a-z0-9-]+\.jpg$' % re.escape(s), f)]
    if own:
        best = max(sorted(own), key=lambda f: (lambda w, h: w * h)(*size(os.path.join(web, f))))
        return ok(best)
    f = 'p-%s--a--tienda.jpg' % s
    return ok(f) if os.path.exists(os.path.join(web, f)) else (None, 0)


def fs(name):
    n = len(name)
    return 78 if n <= 14 else 70 if n <= 20 else 62 if n <= 27 else 54


def page(name, img, ratio=1.9):
    """Foto apaisada: a todo el ancho. Foto vertical o cuadrada (lote 30): a la derecha, entera de alto, y detrás la misma foto
    desenfocada y oscura."""
    z = fs(name)
    if ratio < 1.25:
        w = int(min(600, 630 * ratio))
        bg = ('.bg{position:absolute;inset:-60px;background:url("%s") center/cover;filter:blur(30px) brightness(.5)}'
              '.ph{position:absolute;right:0;top:0;bottom:0;width:%dpx;background:url("%s") center/cover}' % (img, w, img))
        lay = '<div class="bg"></div><div class="ph"></div>'
    else:
        bg = '.bg{position:absolute;inset:0;background:url("%s") center/cover}' % img
        lay = '<div class="bg"></div>'
    return ('<!doctype html><meta charset="utf-8"><style>*{box-sizing:border-box;margin:0;padding:0}'
            'html,body{width:1200px;height:630px;overflow:hidden}body{font-family:%s;-webkit-font-smoothing:antialiased;position:relative;background:#111}'
            '%s'
            '.sh{position:absolute;inset:0;background:linear-gradient(90deg,rgba(12,10,8,.86) 0%%,rgba(12,10,8,.62) 42%%,rgba(12,10,8,.08) 78%%),linear-gradient(0deg,rgba(12,10,8,.35),rgba(12,10,8,0) 40%%)}'
            '.l{position:absolute;left:72px;top:0;bottom:0;width:680px;display:flex;flex-direction:column;justify-content:center}'
            '.chip{align-self:flex-start;display:inline-flex;align-items:center;gap:12px;font-weight:600;font-size:25px;color:#fff;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.28);border-radius:99px;padding:11px 22px 11px 17px;margin-bottom:28px}'
            '.chip i{width:10px;height:10px;border-radius:50%%;background:#D4F27A}'
            'h1{font-weight:800;font-size:%dpx;line-height:1.02;letter-spacing:-.035em;color:#fff;text-wrap:balance}'
            'h2{font-weight:300;font-size:%dpx;line-height:1.05;letter-spacing:-.03em;color:rgba(255,255,255,.86);margin-top:4px}'
            '.by{position:absolute;left:72px;bottom:40px;font-size:23px;color:rgba(255,255,255,.75)}.by b{color:#fff;font-weight:700}'
            '</style>%s<div class="sh"></div>'
            '<div class="l"><span class="chip"><i></i>Propuesta para vosotros</span><h1>%s,</h1><h2>abierta 24 horas.</h2></div>'
            '<div class="by"><b>Christian</b> · 404 Growth</div>' % (FONT, bg, z, z, lay, html.escape(name)))


def src(web, out, solo):
    os.makedirs(out, exist_ok=True)
    rel = os.path.relpath(web, out)
    lst, sin = [], []
    for s, name, _ in props(web, solo):
        img, ratio = hero(web, s)
        if not img:
            sin.append(s)
            continue
        open(os.path.join(out, s + '.html'), 'w', encoding='utf-8').write(page(name, rel + '/' + img, ratio))
        lst.append(s)
    json.dump(lst, open(os.path.join(out, 'lista.json'), 'w'))
    print(len(lst), 'miniaturas por hacer;', len(sin), 'sin foto:', ', '.join(sin) or '-')


def tag(h, prop, val):
    """Pone <meta property="prop" content="val">: cambia la que hay o la añade después de og:site_name / antes de </head>."""
    v = html.escape(val, quote=True)
    r = re.compile(r'<meta property="%s" content="[^"]*">' % re.escape(prop))
    new = '<meta property="%s" content="%s">' % (prop, v)
    if r.search(h):
        return r.sub(lambda m: new, h, count=1)
    i = h.find('</head>')
    return h[:i] + new + h[i:]


def meta(web, solo, forzar=False):
    n = falta = 0
    for s, name, h in props(web, solo):
        if not forzar and not os.path.exists(os.path.join(web, 'p-%s--wa.jpg' % s)):
            falta += 1
            continue
        h2 = tag(h, 'og:title', '%s × 404 Growth' % name)
        h2 = tag(h2, 'og:description', DESC)
        h2 = tag(h2, 'og:image', 'https://404growth.com/p-%s--wa.jpg' % s)
        h2 = tag(h2, 'og:image:width', '1200')
        h2 = tag(h2, 'og:image:height', '630')
        if h2 != h:
            open(os.path.join(web, 'p-%s.html' % s), 'w', encoding='utf-8').write(h2)
            n += 1
    print(n, 'propuestas con la miniatura nueva;', falta, 'sin p-<slug>--wa.jpg (se quedan como estaban)')


if __name__ == '__main__':
    a = sys.argv[1:]
    solo = set(a[a.index('--solo') + 1].split(',')) if '--solo' in a else None
    if a[0] == 'src':
        src(a[1], a[2], solo)
    elif a[0] == 'meta':
        meta(a[1], solo, '--forzar' in a)   # --forzar: sin mirar si está la imagen (la copia del repo, cuyas fotos están en el Mac)
