#!/usr/bin/env python3
"""404 Growth · páginas SEO (de tienda física a tienda online).

Lee seo/pages/*.json (una página por archivo, esquema en seo/LEEME.md) y escribe en web117-404growth/:
  tienda-online.html y tienda-online/<sector>.html   (/tienda-online, /tienda-online/moda…)
  guia.html y guia/<guia>.html                        (/guia, /guia/cuanto-cuesta-una-tienda-online…)
  sitemap.xml                                          (portada, hubs y todas las páginas; el blog tiene el suyo)
  seo/paginas.json                                     (títulos para las métricas del admin)
Uso: python3 seo/build.py   (desde la raíz del repo)
"""
import html, json, os, re, sys, datetime
import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'seo', 'pages')
OUT = os.path.join(ROOT, 'web117-404growth')
SITE = 'https://404growth.com'
TODAY = datetime.date.today().isoformat()
MONTHS = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
def fdate(iso):
    d = datetime.date.fromisoformat(iso); return '%d de %s de %d' % (d.day, MONTHS[d.month - 1], d.year)
E = lambda s: html.escape(str(s), quote=True)

pages = []
for fn in sorted(os.listdir(SRC)):
    if fn.endswith('.json'):
        p = json.load(open(os.path.join(SRC, fn), encoding='utf-8'))
        p['_file'] = fn
        pages.append(p)
by = {'/' + p['slug']: p for p in pages}
SECTORS = [p for p in pages if p['type'] == 'sector']
GUIDES = [p for p in pages if p['type'] == 'guia']
ORDER_S = ['moda', 'moda-infantil', 'calzado', 'joyeria', 'regalos-y-artesania', 'cosmetica-y-perfumeria', 'decoracion-y-hogar', 'gourmet', 'pasteleria', 'jugueteria', 'deportes', 'libreria-y-papeleria', 'floristeria', 'mascotas']
ORDER_G = ['pasar-tienda-fisica-a-online', 'cuanto-cuesta-una-tienda-online', 'sincronizar-stock-tienda-fisica-y-online', 'tienda-fisica-vs-tienda-online', 'requisitos-legales-tienda-online', 'envios-tienda-online', 'por-que-mi-tienda-online-no-vende', 'shopify-vs-woocommerce', 'vender-por-instagram', 'click-and-collect']
rank = lambda order: (lambda p: order.index(p['slug'].split('/')[-1]) if p['slug'].split('/')[-1] in order else 99)
SECTORS.sort(key=rank(ORDER_S)); GUIDES.sort(key=rank(ORDER_G))
KNOWN = set(by) | {'/', '/blog', '/tienda-online', '/guia', '/book', '/legal'}

def book(medium, campaign):
    return '/book?utm_source=seo&utm_medium=%s&utm_campaign=%s' % (medium, campaign.replace('/', '-') or 'hub')

CSS = open(os.path.join(ROOT, 'seo', 'style.css'), encoding='utf-8').read().strip()

def counter(slug):
    # the same counter as the blog (/l/bl): v on open, r at the end of the text, c on a «Reserva» button. No cookies.
    return ("<script>(function(){try{var S=" + json.dumps(slug) + ";try{if(localStorage.getItem('c404int'))return}catch(e){}if(navigator.webdriver)return;"
            "var q=new URLSearchParams(location.search),r='';try{r=document.referrer?new URL(document.referrer).hostname:''}catch(e){}"
            "var B={s:S,r:r,u:(q.get('utm_source')||'').slice(0,40)},D={};"
            "function p(e){if(D[e])return;D[e]=1;B.e=e;try{fetch('/l/bl',{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify(B),keepalive:true}).catch(function(){})}catch(x){}}"
            "p('v');var E=document.getElementById('fin');if(E&&'IntersectionObserver' in window){var o=new IntersectionObserver(function(es){if(es[0].isIntersecting){p('r');o.disconnect()}});o.observe(E)}"
            "document.addEventListener('click',function(ev){var a=ev.target.closest&&ev.target.closest('a[data-cta]');if(a)p('c')})}catch(e){}})();</script>")

ORG = {"@type": "Organization", "@id": SITE + "/#org", "name": "404 Growth", "url": SITE + "/", "logo": SITE + "/favicon.svg",
       "description": "Convertimos tiendas físicas en tiendas online que venden en toda España.", "areaServed": {"@type": "Country", "name": "España"},
       "email": "hola@404growth.com", "telephone": "+34610594450"}
AUTH = {"@type": "Person", "@id": SITE + "/#christian", "name": "Christian Silva", "jobTitle": "Fundador de 404 Growth", "url": SITE + "/", "worksFor": {"@id": SITE + "/#org"}}

def nav(cur, slug, medium):
    a = lambda href, t: '<a href="%s"%s>%s</a>' % (href, ' aria-current="page"' if cur == href else '', t)
    return ('<nav class="n" aria-label="Principal"><div class="ww"><a class="br" href="/">404/GROWTH<sup>®</sup></a><div class="lk">'
            + a('/tienda-online', 'Sectores') + a('/guia', 'Guías') + a('/blog', 'Blog') +
            '</div><a class="cta" href="%s" data-cta="seo-nav">Reserva una llamada</a></div></nav>' % E(book(medium, slug)))

def footer():
    s = ''.join('<li><a href="/%s">%s</a></li>' % (p['slug'], E(p['nav'])) for p in SECTORS)
    g = ''.join('<li><a href="/%s">%s</a></li>' % (p['slug'], E(p['h1'])) for p in GUIDES)
    return ('<footer><div class="ww"><div class="fcols">'
            '<div><b>404 Growth</b><p>Pasamos tu tienda física a tienda online en 15 días, con tu marca y tu stock, y te traemos clientes de toda España.</p>'
            '<p><a href="mailto:hola@404growth.com">hola@404growth.com</a> · <a href="https://wa.me/34610594450">+34 610 594 450</a></p></div>'
            '<div><b><a href="/tienda-online">Tienda online por sector</a></b><ul>' + s + '</ul></div>'
            '<div><b><a href="/guia">Guías</a></b><ul>' + g + '</ul></div></div>'
            '<div class="fbot"><span>404 Growth · De tienda física a tienda online · Toda España</span><span><a href="/">Inicio</a> · <a href="/blog">Blog</a> · <a href="/legal">Aviso legal y privacidad</a></span></div></div></footer>')

def shell(o):
    ld = json.dumps({"@context": "https://schema.org", "@graph": o['ld']}, ensure_ascii=False).replace('</', '<\\/')
    return ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
            '<title>%s</title><meta name="description" content="%s"><link rel="canonical" href="%s"><meta name="robots" content="index,follow,max-image-preview:large">'
            '<meta name="theme-color" content="#0C1412"><link rel="icon" href="/favicon.svg?v=2" type="image/svg+xml"><link rel="apple-touch-icon" href="/apple-touch-icon.png">'
            '<link rel="preload" href="/inter-tight.woff2" as="font" type="font/woff2" crossorigin>'
            '<meta property="og:type" content="%s"><meta property="og:site_name" content="404 Growth"><meta property="og:locale" content="es_ES"><meta property="og:url" content="%s">'
            '<meta property="og:title" content="%s"><meta property="og:description" content="%s"><meta property="og:image" content="%s/og-404-tiendas.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">'
            '<script type="application/ld+json">%s</script><style>%s</style></head><body>%s%s%s%s</body></html>') % (
        E(o['title']), E(o['descr']), o['url'], 'article' if o.get('article') else 'website', o['url'], E(o.get('og') or o['title']), E(o['descr']), SITE,
        ld, CSS, o['nav'], o['main'], footer(), counter(o['slug']))

MD = markdown.Markdown(extensions=['tables', 'sane_lists'])
def md(t):
    MD.reset(); h = MD.convert(t)
    return h.replace('<table>', '<div class="tbl"><table>').replace('</table>', '</table></div>')

def slugid(t):
    t = t.lower()
    for a, b in zip('áéíóúüñ', 'aeiouun'): t = t.replace(a, b)
    return re.sub(r'[^a-z0-9]+', '-', t).strip('-')[:60]

def words(p):
    t = ' '.join([p['lead']] + [s['md'] for s in p['sections']] + [f['q'] + ' ' + f['a'] for f in p['faq']])
    return len(re.sub(r'[#*|\[\]()]', ' ', t).split())

problems = []
def check_links(p):
    for s in p['sections']:
        for href in re.findall(r'\]\((/[^)\s]*)\)', s['md']):
            if href.split('#')[0].rstrip('/') not in KNOWN and href != '/':
                problems.append('%s: enlace interno desconocido %s' % (p['slug'], href))
    for r in p.get('related', []):
        if r not in by: problems.append('%s: related desconocido %s' % (p['slug'], r))
    if len(p['title']) > 65: problems.append('%s: title %d caracteres' % (p['slug'], len(p['title'])))
    if not (120 <= len(p['descr']) <= 165): problems.append('%s: descr %d caracteres' % (p['slug'], len(p['descr'])))

def page(p):
    check_links(p)
    url = SITE + '/' + p['slug']
    guide = p['type'] == 'guia'
    hub, hubt = ('/guia', 'Guías') if guide else ('/tienda-online', 'Tienda online por sector')
    medium = 'guia' if guide else 'sector'
    camp = p['slug'].split('/')[-1]
    secs = p['sections']
    body = []
    for i, s in enumerate(secs):
        body.append('<h2 id="%s">%s</h2>%s' % (slugid(s['h2']), E(s['h2']), md(s['md'])))
        if i == (2 if len(secs) > 4 else 1):
            who = ('tu tienda de ' + p['nav'].lower()) if not guide else 'tu tienda física'
            body.append('<aside class="box mid"><h2>¿Y en %s, cómo sería?</h2><p>En una llamada de 30 minutos miramos tu tienda y te digo qué haría yo: qué productos subir primero, cómo traer clientes y cuánto costaría, con precio cerrado.</p>'
                        '<a class="cta" href="%s" data-cta="seo-mid">Reserva tu llamada gratis →</a></aside>' % (E(who), E(book(medium, camp))))
    body.append('<div id="fin" style="height:1px" aria-hidden="true"></div>')
    faq = ''.join('<details><summary>%s</summary><p>%s</p></details>' % (E(f['q']), E(f['a'])) for f in p['faq'])
    rel = ''.join('<a class="card" href="%s"><span class="kick">%s</span><h3>%s</h3><p>%s</p></a>' % (r, 'Guía' if by[r]['type'] == 'guia' else 'Sector', E(by[r]['h1']), E(by[r]['card'])) for r in p.get('related', []) if r in by)
    src = ''.join('<li><a href="%s" rel="nofollow noopener" target="_blank">%s</a></li>' % (E(s['u']), E(s['t'])) for s in p.get('sources', []))
    mins = max(3, round(words(p) / 220))
    toc = ''.join('<li><a href="#%s">%s</a></li>' % (slugid(s['h2']), E(s['h2'])) for s in secs) if guide else ''
    main = ('<main><div class="w"><div class="crumb"><a href="/">Inicio</a> › <a href="%s">%s</a> › <span>%s</span></div>'
            '<header class="hd"><span class="kick">%s</span><h1>%s</h1><p class="lead">%s</p>'
            '<div class="meta"><img src="/christian-hola.jpg" alt="" width="36" height="36" loading="lazy"><span>Por <b>Christian Silva</b>, fundador de 404 Growth</span><span>Actualizado el %s</span><span>%d min de lectura</span></div>'
            '<div class="hcta"><a class="cta" href="%s" data-cta="seo-hero">Reserva tu llamada gratis</a><span>30 min por Google Meet · sin compromiso</span></div></header>'
            '%s<article class="post">%s</article>'
            '<section class="faq"><h2>Preguntas frecuentes</h2>%s</section>'
            '<aside class="box"><h2>Tu tienda física, vendiendo online en 15 días</h2><p>Montamos tu tienda online con tu marca y tu stock, a tu nombre, y te traemos clientes de toda España. Primero, 30 minutos para ver si tiene sentido en tu caso.</p>'
            '<a class="cta" href="%s" data-cta="seo-end">Reserva tu llamada gratis →</a></aside>'
            '%s</div>%s</main>') % (
        hub, hubt, E(p['nav'] if not guide else p['h1']), E(p['kicker']), E(p['h1']), E(p['lead']), fdate(TODAY), mins, E(book(medium, camp)),
        ('<nav class="toc" aria-label="En esta guía"><b>En esta guía</b><ol>' + toc + '</ol></nav>') if toc else '',
        ''.join(body), faq, E(book(medium, camp)),
        ('<div class="src"><b>Fuentes</b><ul>' + src + '</ul></div>') if src else '',
        ('<div class="ww"><h2 class="relh">Sigue leyendo</h2><div class="grid">' + rel + '</div></div>') if rel else '')
    crumbs = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": hubt, "item": SITE + hub},
        {"@type": "ListItem", "position": 3, "name": p['h1'], "item": url}]}
    faqld = {"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [{"@type": "Question", "name": f['q'], "acceptedAnswer": {"@type": "Answer", "text": f['a']}} for f in p['faq']]}
    if guide:
        main_ld = {"@type": "Article", "@id": url + "#article", "headline": p['h1'], "description": p['descr'], "url": url, "mainEntityOfPage": url, "inLanguage": "es-ES",
                   "datePublished": TODAY, "dateModified": TODAY, "author": {"@id": SITE + "/#christian"}, "publisher": {"@id": SITE + "/#org"}, "image": SITE + "/og-404-tiendas.jpg", "keywords": ', '.join(p['kw'])}
    else:
        main_ld = {"@type": "Service", "@id": url + "#service", "name": p['h1'], "serviceType": "Creación de tienda online para tiendas físicas", "description": p['descr'], "url": url,
                   "provider": {"@id": SITE + "/#org"}, "areaServed": {"@type": "Country", "name": "España"}, "audience": {"@type": "BusinessAudience", "name": "Tiendas físicas de " + p['nav'].lower()}}
    return shell({'title': p['title'], 'descr': p['descr'], 'url': url, 'slug': p['slug'], 'article': guide, 'og': p['h1'],
                  'ld': [ORG, AUTH, main_ld, crumbs, faqld], 'nav': nav(hub, p['slug'], medium), 'main': main})

HUBS = json.load(open(os.path.join(ROOT, 'seo', 'hubs.json'), encoding='utf-8'))
def hubpage(key, items):
    h = HUBS[key]; url = SITE + '/' + key
    cards = ''.join('<a class="card" href="/%s"><span class="kick">%s</span><h3>%s</h3><p>%s</p></a>' % (p['slug'], E(p['kicker']), E(p['h1']), E(p['card'])) for p in items)
    secs = ''.join('<h2 id="%s">%s</h2>%s' % (slugid(s['h2']), E(s['h2']), md(s['md'])) for s in h['sections'])
    faq = ''.join('<details><summary>%s</summary><p>%s</p></details>' % (E(f['q']), E(f['a'])) for f in h.get('faq', []))
    main = ('<main><div class="ww"><div class="crumb"><a href="/">Inicio</a> › <span>%s</span></div>'
            '<header class="hd"><span class="kick">%s</span><h1>%s</h1><p class="lead">%s</p>'
            '<div class="hcta"><a class="cta" href="%s" data-cta="seo-hero">Reserva tu llamada gratis</a><span>30 min por Google Meet · sin compromiso</span></div></header>'
            '<div class="grid">%s</div></div><div class="w"><article class="post">%s</article><div id="fin" style="height:1px" aria-hidden="true"></div>%s'
            '<aside class="box"><h2>%s</h2><p>%s</p><a class="cta" href="%s" data-cta="seo-end">Reserva tu llamada gratis →</a></aside></div></main>') % (
        E(h['nav']), E(h['kicker']), E(h['h1']), E(h['lead']), E(book('hub', key)), cards, secs,
        ('<section class="faq"><h2>Preguntas frecuentes</h2>' + faq + '</section>') if faq else '', E(h['box_h']), E(h['box_p']), E(book('hub', key)))
    ld = [ORG, AUTH, {"@type": "CollectionPage", "@id": url + "#page", "name": h['h1'], "description": h['descr'], "url": url, "inLanguage": "es-ES", "isPartOf": {"@id": SITE + "/#site"},
                      "hasPart": [{"@type": "WebPage", "name": p['h1'], "url": SITE + '/' + p['slug']} for p in items]},
          {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": h['nav'], "item": url}]}]
    if faq: ld.append({"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [{"@type": "Question", "name": f['q'], "acceptedAnswer": {"@type": "Answer", "text": f['a']}} for f in h['faq']]})
    return shell({'title': h['title'], 'descr': h['descr'], 'url': url, 'slug': key, 'ld': ld, 'nav': nav('/' + key, key, 'hub'), 'main': main})

def write(rel, text):
    path = os.path.join(OUT, rel); os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write(text)

for p in pages:
    write(p['slug'] + '.html', page(p))
write('tienda-online.html', hubpage('tienda-online', SECTORS))
write('guia.html', hubpage('guia', GUIDES))

urls = [('/', '1.0'), ('/tienda-online', '0.9'), ('/guia', '0.8')] + [('/' + p['slug'], '0.8') for p in GUIDES + SECTORS] + [('/blog', '0.6')]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
    '  <url><loc>%s%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>\n' % (SITE, u if u != '/' else '/', TODAY, pr) for u, pr in urls) + '</urlset>\n'
open(os.path.join(OUT, 'sitemap.xml'), 'w', encoding='utf-8').write(sm)
meta = {p['slug']: {'t': p['h1'], 'k': p['type']} for p in pages}
meta['tienda-online'] = {'t': HUBS['tienda-online']['h1'], 'k': 'hub'}; meta['guia'] = {'t': HUBS['guia']['h1'], 'k': 'hub'}
write('seo/paginas.json', json.dumps(meta, ensure_ascii=False))

for p in pages: print('%-48s %5d palabras  title %2d  descr %3d' % (p['slug'], words(p), len(p['title']), len(p['descr'])))
print('\n'.join(problems) if problems else 'Sin problemas')
