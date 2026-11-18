#!/usr/bin/env python3
"""Página del brief de un cliente (404growth.com/brief/<id>/), hecha desde su JSON de preguntas.

    python3 build.py <brief.json> <web117-404growth> [--escudo <png>]

Escribe <web117>/brief/<id>/index.html (todo dentro: estilos, script y preguntas) y, si se pasa --escudo,
<web117>/brief/<id>/escudo.png. Las respuestas van al admin (/l/brief) con la clave del enlace (?k=…).
El mismo JSON va dentro del worker del admin (patch_v78.py), para que el admin sepa qué es cada respuesta."""
import html
import json
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
E = lambda s: html.escape(str(s), quote=True)


def field(q):
    t, i = q['type'], q['id']
    ph = ' placeholder="%s"' % E(q['ph']) if q.get('ph') else ''
    out = []
    if t == 'confirm':
        out.append('<div class="web"><small>%s</small><p>%s</p></div>' % (E(q.get('lbl', 'Lo que pone vuestra web')), E(q['web'])))
        out.append('<div class="chips" role="radiogroup" aria-labelledby="l-%s">' % i)
        for v, l in (('ok', 'Está bien así'), ('cambiar', 'Hay que cambiarlo')):
            out.append('<label class="chip"><input type="radio" name="%s" value="%s"><span>%s</span></label>' % (i, v, l))
        out.append('</div><div class="oth" hidden><label class="sr" for="f-%s_o">¿Qué ponemos?</label>'
                   '<textarea id="f-%s_o" name="%s_o" rows="2" placeholder="¿Qué ponemos?"></textarea></div>' % (i, i, i))
    elif t in ('one', 'many'):
        it = 'radio' if t == 'one' else 'checkbox'
        out.append('<div class="chips" role="%s" aria-labelledby="l-%s">' % ('radiogroup' if t == 'one' else 'group', i))
        for o in q['o'] + (['Otro'] if q.get('other') else []):
            out.append('<label class="chip"><input type="%s" name="%s" value="%s"><span>%s</span></label>' % (it, i, E(o), E(o)))
        out.append('</div>')
        if q.get('other'):
            out.append('<div class="oth" hidden><label class="sr" for="f-%s_o">Otro: ¿cuál?</label>'
                       '<input type="text" id="f-%s_o" name="%s_o" placeholder="¿Cuál?"></div>' % (i, i, i))
    elif t == 'long':
        out.append('<textarea id="f-%s" name="%s" rows="%d"%s></textarea>' % (i, i, q.get('rows', 3), ph))
    elif t == 'files':
        out.append('<label class="drop" id="drop" for="fin"><b>Arrastrad aquí los archivos</b><small>o tocad para elegirlos · hasta 95 MB cada uno</small>'
                   '<input type="file" id="fin" multiple></label><ul class="files" id="fl" aria-live="polite"></ul>')
    else:
        typ = {'text': 'text', 'url': 'url', 'number': 'number', 'date': 'date'}[t]
        extra = ' inputmode="numeric" min="0"' if t == 'number' else (' inputmode="url"' if t == 'url' else '')
        out.append('<input type="%s" id="f-%s" name="%s"%s%s>' % (typ, i, i, ph, extra))
    if not q.get('nopend') and t != 'files':
        out.append('<label class="pend"><input type="checkbox" name="%s__p" value="1">Aún no lo sabemos</label>' % i)
    return ''.join(out)


def page(B):
    nav, secs = [], []
    for n, s in enumerate(B['sections'], 1):
        nav.append('<a href="#%s"><b>%02d</b>%s<i>0/%d</i></a>' % (s['id'], n, E(s['t']), len(s['q'])))
        qs = []
        for q in s['q']:
            lab = ('<span class="ql" id="l-%s">%s</span>' if q['type'] in ('one', 'many', 'confirm', 'files')
                   else '<label class="ql" id="l-%s" for="f-' + q['id'] + '">%s</label>') % (q['id'], E(q['t']))
            qs.append('<div class="q" data-q="%s">%s%s%s</div>' % (q['id'], lab, '<p class="qh">%s</p>' % E(q['h']) if q.get('h') else '', field(q)))
        secs.append('<section class="sec" id="%s" aria-labelledby="h-%s"><div class="sec-h"><span class="sec-n" aria-hidden="true">%02d</span><h2 id="h-%s">%s</h2></div>'
                    '<p class="why">%s</p>%s</section>' % (s['id'], s['id'], n, s['id'], E(s['t']), E(s['why']), ''.join(qs)))
    cfg = {'id': B['id'], 'sections': [{'id': s['id'], 'q': [{k: q[k] for k in ('id', 'type', 'other', 'nopend') if k in q} for q in s['q']]} for s in B['sections']]}
    css = open(os.path.join(HERE, 'brief.css'), encoding='utf-8').read()
    js = open(os.path.join(HERE, 'brief.js'), encoding='utf-8').read()
    facts = ''.join('<li>%s</li>' % E(f) for f in B.get('facts', []))
    return '''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>%(client)s · Brief de la campaña</title>
<meta name="robots" content="noindex,nofollow">
<meta name="referrer" content="same-origin">
<meta name="theme-color" content="#000000">
<link rel="icon" href="escudo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>%(css)s</style>
</head>
<body>
<header class="top"><div class="top-in">
  <a class="brand" href="#inicio"><img src="escudo.png" alt="" width="34" height="42"><b>%(client_u)s</b></a>
  <div class="prog"><div class="bar" aria-hidden="true"><i></i></div><span class="cnt" aria-live="polite">0 de 0</span><span class="st" id="st" role="status"><span>Cargando…</span></span></div>
</div></header>
<main>
<section class="hero" id="inicio"><div class="hero-in">
  <img class="crest" src="escudo.png" alt="Escudo de %(client)s" width="92" height="113">
  <span class="kick">%(kicker)s</span>
  <h1>%(t1)s <span>%(t2)s</span></h1>
  <p class="lead">%(intro)s</p>
  <ul class="facts">%(facts)s</ul>
  <a class="go" href="#%(first)s">Empezar <span aria-hidden="true">→</span></a>
  <p class="tips">%(tips)s</p>
  <p class="by">Preparado por 404 Growth</p>
</div></section>
<form class="wrap" id="bf" autocomplete="off" novalidate>
  <nav class="nav" aria-label="Apartados">%(nav)s</nav>
  <div>
    %(secs)s
    <section class="send" id="enviar">
      <h2>¿Lo tenéis?</h2>
      <p>Lleváis <b id="sendc">0 de 0</b> preguntas. Todo se guarda solo: podéis enviarlo aunque falte algo y lo cerramos juntos en la llamada.</p>
      <button type="button" class="go" id="sendb">Enviar a 404 Growth <span aria-hidden="true">→</span></button>
      <p id="sendm" role="status"></p>
      <p class="share">¿Lo rellena alguien más del equipo? <button type="button" id="copyl">Copiar el enlace</button> y pasádselo: veréis lo mismo y se guarda en el mismo sitio.</p>
    </section>
  </div>
</form>
</main>
<footer class="foot">Formulario preparado por <b>404 Growth</b> para %(client)s. Solo lo lee el equipo de 404 Growth, para preparar vuestra campaña.</footer>
<div class="gate" id="gate" hidden><div><img src="escudo.png" alt=""><h2>Enlace no válido</h2><p>Este formulario es privado. Abridlo desde el enlace que os hemos enviado o pedídnoslo de nuevo.</p></div></div>
<script>window.BRIEF=%(cfg)s;</script>
<script>%(js)s</script>
</body>
</html>
''' % {'client': E(B['client']), 'client_u': E(B['client'].upper()), 'kicker': E(B['kicker']), 't1': E(B['title1']), 't2': E(B['title2']),
       'intro': E(B['intro']), 'facts': facts, 'tips': E(B.get('tips', '')), 'first': B['sections'][0]['id'], 'nav': ''.join(nav),
       'secs': ''.join(secs), 'css': css, 'js': js, 'cfg': json.dumps(cfg, ensure_ascii=False, separators=(',', ':'))}


if __name__ == '__main__':
    B = json.load(open(sys.argv[1], encoding='utf-8'))
    out = os.path.join(sys.argv[2], 'brief', B['id']); os.makedirs(out, exist_ok=True)
    open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(page(B))
    if '--escudo' in sys.argv:
        shutil.copy(sys.argv[sys.argv.index('--escudo') + 1], os.path.join(out, 'escudo.png'))
    n = sum(len(s['q']) for s in B['sections'])
    print('ok', out, n, 'preguntas')
