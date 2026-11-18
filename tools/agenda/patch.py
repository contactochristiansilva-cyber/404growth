"""Mete la agenda (/agenda.js) dentro de las propuestas de tienda online (18/11/2026).

uso: python3 patch.py <carpeta con p-*.html> [--solo slug1,slug2] [--datos <carpeta l33/data>]

En cada propuesta principal (p-<slug>.html, sin «--» en el nombre) que tenga la sección de cierre (id="hablar") y botones de reserva:
  - los botones que iban a /book o a Calendly bajan ahora a la agenda (#agenda), sin abrir otra pestaña;
  - la agenda va dentro de «01 La tienda», justo encima de la página de producto (Chris, 18/11/2026): después de la tienda grande
    y su botón, antes de «Cada producto, listo para comprar» (<div class="head fh"> o <div class="pdpx">). Si una propuesta no
    tiene esa parte, va después del cierre (antes del pie);
  - <style id="ag-sc">: las tiendas metidas con iframe no cogen la rueda ni el dedo (pointer-events:none). Si no, al deslizar
    rápido encima de una se movía la tienda de dentro y la página se quedaba parada.
Se puede pasar todas las veces que haga falta: si ya tiene la agenda, solo rehace ese bloque (entre <!--ag--> y <!--/ag-->).
Las propuestas de la oferta antigua (web + asistente + CRM), los concesionarios y las páginas especiales no se tocan.
Escribe en la misma carpeta y dice cuántas cambió."""
import html, json, os, re, sys

SKIP = {'aiguamarina-joies-reservas', 'carmen-valencia'}          # páginas hechas a mano: la de reservas es una demo de talleres
SEC = [('joyer', 'joyeria'), ('bisuter', 'joyeria'), ('zapat', 'calzado'), ('calzado', 'calzado'), ('sneaker', 'calzado'),
       ('perfum', 'cosmetica'), ('cosm', 'cosmetica'), ('belleza', 'cosmetica'), ('deport', 'deporte'), ('suplement', 'deporte'),
       ('hogar', 'deco'), ('decora', 'deco'), ('mueble', 'deco'), ('moda', 'moda'), ('boutique', 'moda'), ('ropa', 'moda'), ('lencer', 'moda')]
NICHE = {'moda': 'moda', 'calzado': 'calzado', 'sneakers': 'calzado', 'joya': 'joyeria', 'joyeria': 'joyeria', 'cosmetica': 'cosmetica',
         'deporte': 'deporte', 'suplementos': 'deporte', 'deco': 'deco'}
BOOK = re.compile(r'<a\b([^>]*?)href="https://(?:404growth\.com/book\?[^"]*|calendly\.com/hola-404growth/[^"]*)"([^>]*)>')


_MAP = {}


def sector(slug, title, datos):
    if datos and datos.endswith('.json'):   # {slug: nicho}, para usarlo donde no está prospeccion/l33/data (el Mac)
        if not _MAP:
            _MAP.update(json.load(open(datos, encoding='utf-8')))
        if slug in _MAP:
            return NICHE.get(_MAP[slug], 'otro')
    p = os.path.join(datos, slug + '.json') if datos and not datos.endswith('.json') else ''
    if p and os.path.exists(p):
        return NICHE.get(json.load(open(p, encoding='utf-8')).get('niche', ''), 'otro')
    t = title.split('·', 1)[-1].lower()
    return next((v for k, v in SEC if k in t), 'otro')


SC = '<style id="ag-sc">iframe[data-src*="--tienda"],iframe[src*="--tienda"]{pointer-events:none}</style>'
PDP = re.compile(r'<div class="(?:head fh|pdpx)"')


def block(slug, biz, sec, inn):
    return ('<!--ag-->%s<section class="ag%s" id="agenda" data-slug="%s" data-biz="%s" data-sec="%s"><div class="ag-w">'
            '<span class="ag-eb">Agenda · 30 minutos</span><h2>Elige día y hora.<br><span>Te enseño la tienda en directo.</span></h2>'
            '<p class="ag-sub">Una videollamada de 30 minutos por Google Meet: te enseño la tienda de %s con vuestro catálogo y te doy el precio cerrado. Sin compromiso.</p>'
            '<div class="ag-app"><noscript><a href="https://404growth.com/book?utm_source=propuesta&amp;utm_campaign=%s">Reservar la llamada</a></noscript></div>'
            '</div></section><script src="/agenda.js" defer></script><!--/ag-->') % (SC, ' ag-in' if inn else '', slug, html.escape(biz), sec, html.escape(biz), slug)


def patch(path, datos):
    slug = os.path.basename(path)[2:-5]
    h = open(path, encoding='utf-8').read()
    if slug in SKIP or 'id="hablar"' not in h:
        return None
    had = '<!--ag-->' in h
    h = re.sub(r'<!--ag-->.*?<!--/ag-->', '', h, flags=re.S)   # si ya la tenía, se rehace
    if not BOOK.search(h) and not had:
        return None
    m = re.search(r'<title>(.*?)</title>', h, re.S)
    title = html.unescape(m.group(1)) if m else ''
    biz = re.split(r'\s+[×·|]\s+', title)[0].strip() or slug
    sec = sector(slug, title, datos)
    n = len(BOOK.findall(h))

    def link(m):   # el mismo botón, sin abrir otra pestaña: baja a la agenda
        attrs = ' '.join(re.sub(r'\s(?:target|rel|data-cal)="[^"]*"', '', ' ' + m.group(1) + ' ' + m.group(2)).split())
        return '<a %s href="#agenda" data-ag="1">' % attrs if attrs else '<a href="#agenda" data-ag="1">'
    h = BOOK.sub(link, h)
    t = h.find('id="tienda"')
    m = PDP.search(h, t) if t >= 0 else None
    if m:   # dentro de «01 La tienda», justo encima de la página de producto
        j, inn = m.start(), True
    else:   # sin página de producto: después del cierre
        i = h.find('<section class="close" id="hablar"')
        j = h.find('</section>', i) + len('</section>') if i >= 0 else -1
        if j <= 0:
            j = h.find('<footer')
        inn = False
    h = h[:j] + block(slug, biz, sec, inn) + h[j:]
    open(path, 'w', encoding='utf-8').write(h)
    return slug, biz, sec, n, 'tienda' if inn else 'cierre'


if __name__ == '__main__':
    a = sys.argv[1:]
    d = a[0]
    solo = set(a[a.index('--solo') + 1].split(',')) if '--solo' in a else None
    datos = a[a.index('--datos') + 1] if '--datos' in a else ''
    out = []
    for f in sorted(os.listdir(d)):
        if not (f.startswith('p-') and f.endswith('.html')) or '--' in f:
            continue
        if solo and f[2:-5] not in solo:
            continue
        r = patch(os.path.join(d, f), datos)
        if r:
            out.append(r)
    for r in out[:5]:
        print('  %s · %s · %s · %d botones · %s' % r)
    print(len(out), 'propuestas con la agenda;', sum(1 for r in out if r[2] == 'otro'), 'con sector «otro»;',
          sum(1 for r in out if r[4] == 'tienda'), 'encima de la página de producto')
