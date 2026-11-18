#!/usr/bin/env python3
"""Páginas de empleo de 404 Growth (404growth.com/equipo), v77 · 18/11/2026.

Uso: python3 build.py <carpeta web> [--og <carpeta para las miniaturas>]
  - <web>/equipo/index.html                  todos los puestos, quiénes somos, cómo trabajamos y el proceso
  - <web>/equipo/<puesto>/index.html         cada puesto con sus 5 puntos (rol y quiénes somos, responsabilidades, requisitos,
                                             resultados y beneficios), el proceso y la candidatura en 4 pasos
  - <web>/equipo/prueba/  y  entrevista/     la prueba técnica y elegir la hora de la entrevista (enlace personal ?t=…)
  - <web>/equipo/e.css y e.js
  - añade las páginas a <web>/sitemap.xml si faltan
  - con --og: un HTML por miniatura (1200x630) para sacarlas con el Playwright del Mac (render_og.js) a <web>/equipo/og-<x>.jpg
Todo sale de roles.json: lo mismo que lee el admin para puntuar. Cambiar un texto ahí cambia la página y lo que la IA tiene en cuenta.
"""
import hashlib, html, json, os, re, shutil, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
R = json.load(open(os.path.join(HERE, 'roles.json'), encoding='utf-8'))
SITE = 'https://404growth.com'
MAIL = 'hola' + '@' + '404growth.com'
TODAY = datetime.date(2026, 11, 18)
e = lambda s: html.escape(str(s), quote=True)

LOGO = ('<svg class="mk" viewBox="20 60 362 280" aria-hidden="true"><g transform="skewX(-12) translate(52 0)" fill="none" stroke="#111311" stroke-width="32" '
        'stroke-linecap="round" stroke-linejoin="round"><rect x="140" y="90" width="120" height="220" rx="60"/><path d="M155.1 110.2 L40 240 L140 240"/>'
        '<path d="M244.9 110.2 L360 240 L260 240"/></g></svg>')
AR = '<svg class="ar" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CHK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="m8 12.5 2.7 2.7L16.5 9"/></svg>'
SPARK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3.5v4M12 16.5v4M3.5 12h4M16.5 12h4M6 6l2.6 2.6M15.4 15.4 18 18M18 6l-2.6 2.6M8.6 15.4 6 18"/></svg>'


def ver(*names):
    h = hashlib.sha256()
    for n in names:
        h.update(open(os.path.join(HERE, 'web', n), 'rb').read())
    return h.hexdigest()[:10]


V = ver('e.css', 'e.js')


def head(title, desc, path, og, robots='index,follow', extra=''):
    url = SITE + path
    return ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
            '<title>%s</title><meta name="description" content="%s"><link rel="canonical" href="%s"><meta name="robots" content="%s">'
            '<meta property="og:type" content="website"><meta property="og:site_name" content="404 Growth"><meta property="og:locale" content="es_ES">'
            '<meta property="og:title" content="%s"><meta property="og:description" content="%s"><meta property="og:url" content="%s">'
            '<meta property="og:image" content="%s/equipo/og-%s.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">'
            '<meta name="twitter:card" content="summary_large_image"><meta name="theme-color" content="#040806">'
            '<link rel="icon" href="/favicon.ico?v=3" sizes="48x48"><link rel="icon" href="/favicon-96.png?v=3" type="image/png" sizes="96x96">'
            '<link rel="icon" href="/favicon.svg?v=3" type="image/svg+xml"><link rel="apple-touch-icon" href="/apple-touch-icon.png?v=3">'
            '<link rel="stylesheet" href="/equipo/e.css?v=%s">%s</head><body>'
            % (e(title), e(desc), url, robots, e(title), e(desc), url, SITE, og, V, extra))


def nav(cta_href='#aplicar', cta='Aplicar', links=None):
    links = links if links is not None else [('/equipo/', 'Puestos'), ('#proceso', 'Proceso'), ('/', 'Qué hacemos')]
    return ('<a class="skip" href="#main">Saltar al contenido</a><header class="nv"><div class="w nv-in"><a class="nv-logo" href="/" aria-label="404 Growth, inicio">%s<span>404 Growth</span></a>'
            '<nav class="nv-lk" aria-label="Secciones">%s</nav><a class="nv-cta" href="%s"%s>%s</a></div></header>'
            % (LOGO, ''.join('<a href="%s">%s</a>' % (h, e(t)) for h, t in links), cta_href, ' data-apply' if cta_href == '#aplicar' else '', e(cta)))


PRIV = ('<details class="priv" id="privacidad"><summary>Privacidad de las candidaturas</summary><div>'
        '<p><b>Quién:</b> Christian Silva Aguilar (404 Growth). Contacto: <a href="mailto:%s">%s</a>.</p>'
        '<p><b>Para qué:</b> valorar tu candidatura para el puesto al que te presentas y, solo si lo marcas, tenerte en cuenta para otros puestos.</p>'
        '<p><b>Con qué base:</b> tu consentimiento y las medidas previas a un posible contrato que nos pides al presentarte.</p>'
        '<p><b>Con ayuda de IA:</b> una IA ordena las candidaturas según los requisitos del puesto y lo que nos cuentas de tu trabajo; no ve tu nombre ni tus datos de contacto. '
        'No decide nada: cada paso, también un descarte, lo decide una persona. Puedes pedir que te expliquemos tu valoración.</p>'
        '<p><b>Quién más los ve:</b> Cloudflare (aloja la web y los datos), Anthropic (la IA que ordena las candidaturas, sin tus datos de contacto), Google (si hay entrevista: Calendar y Meet) '
        'y el servicio de correo con el que te escribimos. Si alguno trata datos fuera de la Unión Europea, lo hace con las garantías que exige la ley.</p>'
        '<p><b>Cuánto tiempo:</b> 6 meses desde el último paso del proceso; 12 meses si nos dejas guardarla para futuros puestos. Después se borra sola, también el CV. Si entras en el equipo, lo que exija la ley para la relación.</p>'
        '<p><b>Tus derechos:</b> puedes pedir ver, corregir o borrar tus datos, oponerte, limitar su uso o llevártelos escribiendo a <a href="mailto:%s">%s</a>. '
        'Puedes retirar tu consentimiento cuando quieras. Si crees que no se respetan, puedes reclamar ante la Agencia Española de Protección de Datos (aepd.es).</p>'
        '<p>Más en el <a href="/legal">aviso legal y privacidad</a> de la web.</p></div></details>') % (MAIL, MAIL, MAIL, MAIL)


def foot(priv=True, sticky=''):
    return ('<footer class="ft"><div class="w"><div class="ft-r"><a class="nv-logo" href="/" aria-label="404 Growth, inicio">%s<span>404 Growth</span></a>'
            '<span>De tienda física a tienda online · <a href="/equipo/">Trabaja con nosotros</a> · <a href="mailto:%s">%s</a></span></div>%s</div></footer>%s'
            '<script src="/equipo/e.js?v=%s" defer></script></body></html>') % (LOGO, MAIL, MAIL, PRIV if priv else '', sticky, V)


def process(promise=None):
    return ('<section class="sec" id="proceso"><div class="w"><div class="sh rv" style="position:static;margin-bottom:28px"><div class="sn">Proceso</div><h2>Cómo es el proceso</h2><p>Cinco pasos, sin rondas eternas.</p></div>'
            '<div class="rv"><ol class="steps">%s</ol><p class="promise">%s%s</p></div></div></section>'
            % (''.join('<li><b>%s</b><p>%s</p></li>' % (e(a), e(b)) for a, b in R['process']), CHK, e(promise or R['promise'])))


# desde dónde se puede trabajar (para Google Empleos): España y los países de Latinoamérica de habla hispana
COUNTRIES = ['España', 'Argentina', 'Bolivia', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Ecuador', 'El Salvador', 'Guatemala', 'Honduras',
             'México', 'Nicaragua', 'Panamá', 'Paraguay', 'Perú', 'Puerto Rico', 'República Dominicana', 'Uruguay', 'Venezuela']


def mode_facts(j):
    parts = [x.strip() for x in j['mode'].split('·') if x.strip()]
    return parts + ['España o Latinoamérica', 'Español nativo', 'Horario de España']


# ---------- el formulario ----------
STEPS = ['Sobre ti', 'Tu trabajo', 'El puesto', 'Lo práctico']
AUTO = {'name': 'name', 'email': 'email', 'phone': 'tel', 'city': 'address-level2', 'linkedin': 'url', 'portfolio': 'url', 'video': 'url'}
PH = {'name': 'Nombre y apellidos', 'email': 'tu@email.com', 'phone': '612 345 678', 'city': 'Ciudad, país', 'linkedin': 'linkedin.com/in/…', 'portfolio': 'https://', 'video': 'https://'}
ERR = {'text': 'Rellena este campo.', 'email': 'Revisa el email.', 'tel': 'Revisa el número (con el prefijo si no es de España).', 'url': 'Pega un enlace válido, por ejemplo https://…',
       'long': 'Cuéntanos un poco más.', 'choice': 'Elige una opción.', 'yesno': 'Elige una opción.', 'file': 'Tiene que ser un PDF de hasta 1,8 MB.'}


def field(q, j):
    i, t = q['id'], q['type']
    need = q.get('req') or (i == 'portfolio' and j.get('portfolio') == 'req')
    opt = '' if need else ' <em>(opcional)</em>'
    hp = '<span class="hp" id="h-%s">%s</span>' % (i, e(q['help'])) if q.get('help') else ''
    desc = ' aria-describedby="h-%s"' % i if q.get('help') else ''
    em = '<span class="em" role="alert">%s</span>' % ERR[t]
    if t in ('choice', 'yesno'):
        opts = q.get('opts') or ['Sí', 'No']
        vals = q.get('opts') or ['si', 'no']
        return ('<div class="fd" data-f="%s"><span class="lb" id="l-%s">%s%s</span>%s<div class="pills" role="radiogroup" aria-labelledby="l-%s">%s</div>%s</div>'
                % (i, i, e(q['label']), opt, hp, i, ''.join('<label><input type="radio" name="%s" value="%s"%s><span>%s</span></label>' % (i, e(v), ' required' if need and k == 0 else '', e(o))
                                                         for k, (o, v) in enumerate(zip(opts, vals))), em))
    if t == 'long':
        return ('<div class="fd" data-f="%s"><label for="f-%s">%s%s</label>%s<textarea id="f-%s" name="%s" maxlength="%d"%s%s></textarea><span class="cnt" aria-hidden="true"></span>%s</div>'
                % (i, i, e(q['label']), opt, hp, i, i, q.get('max', 2000), ' required' if need else '', desc, em))
    if t == 'file':
        return ('<div class="fd" data-f="%s"><span class="lb">%s%s</span>%s<div class="file"><input id="f-%s" type="file" accept="application/pdf,.pdf"%s>'
                '<label class="b-gl" for="f-%s">Elegir PDF</label><span class="fn">Ningún archivo</span></div>%s</div>' % (i, e(q['label']), opt, hp, i, desc, i, em))
    typ = {'email': 'email', 'tel': 'tel', 'url': 'url'}.get(t, 'text')
    im = {'email': ' inputmode="email" autocapitalize="off" spellcheck="false"', 'tel': ' inputmode="tel"', 'url': ' inputmode="url" autocapitalize="off" spellcheck="false"'}.get(t, '')
    return ('<div class="fd" data-f="%s"><label for="f-%s">%s%s</label>%s<input id="f-%s" name="%s" type="%s" maxlength="%d" autocomplete="%s" placeholder="%s"%s%s%s>%s</div>'
            % (i, i, e(q['label']), opt, hp, i, i, typ, q.get('max', 300), AUTO.get(i, 'off'), e(PH.get(i, '')), im, ' required' if need else '', desc, em))


def form(j):
    qs = R['base_q'] + j['q']
    by = {n: [q for q in qs if q['step'] == n] for n in (1, 2, 3, 4)}
    cfg = {'slug': j['slug'], 'portfolio': j.get('portfolio', 'opt'), 'test': bool(j.get('test')), 'steps': STEPS,
           'qs': [{'id': q['id'], 'type': q['type'], 'req': bool(q.get('req')), 'step': q['step']} for q in qs]}
    steps = ''
    for n in (1, 2, 3, 4):
        extra = ''
        if n == 4:
            extra = ('<div class="cks"><label class="c1"><input type="checkbox" name="consent" required><span>He leído <a href="#privacidad">cómo tratáis mis datos</a> y quiero que valoréis mi candidatura. '
                     'Sé que una IA ayuda a ordenarlas y que cada decisión la toma una persona.</span></label>'
                     '<label><input type="checkbox" name="keep"><span>Guardad mi candidatura 12 meses para otros puestos <em class="mut" style="font-style:normal">(opcional)</em>.</span></label></div>'
                     '<div class="hpot" aria-hidden="true"><label>Web <input type="text" name="web" tabindex="-1" autocomplete="off"></label></div>')
        steps += '<div class="fs%s" data-s="%d"><h3>%s</h3>%s%s</div>' % (' on' if n == 1 else '', n, e(STEPS[n - 1]), ''.join(field(q, j) for q in by[n]), extra)
    return ('<script type="application/json" id="eqcfg">%s</script>'
            '<form class="fm" id="fm" novalidate aria-label="Candidatura: %s"><div class="fm-top"><b>%s</b><span>Paso 1 de 4</span></div><div class="fm-pr" aria-hidden="true"><i style="width:25%%"></i></div>%s'
            '<div class="fnav"><button class="b-gl" type="button" data-prev hidden>Atrás</button><button class="b-pri" type="button" data-next>Siguiente %s</button>'
            '<button class="b-pri" type="submit" data-send hidden>Enviar candidatura</button></div><p class="fmsg" role="alert" aria-live="polite"></p></form>'
            % (json.dumps(cfg, ensure_ascii=False).replace('</', '<\\/'), e(j['title']), STEPS[0], steps, AR))


# ---------- un puesto ----------
def jsonld(j, path):
    if not j.get('emp'):
        return ''
    desc = ''.join('<p>%s</p>' % e(p) for p in j['role'] + R['about']) + '<p><b>Responsabilidades</b></p><ul>%s</ul>' % ''.join('<li>%s</li>' % e(x) for x in j['resp']) + \
        '<p><b>Requisitos</b></p><ul>%s</ul>' % ''.join('<li>%s</li>' % e(x) for x in j['req']) + \
        '<p><b>Resultados</b></p><ul>%s</ul>' % ''.join('<li>%s: %s</li>' % (e(a), e(b)) for a, b in j['results']) + \
        '<p><b>Beneficios</b></p><ul>%s</ul>' % ''.join('<li>%s</li>' % e(x) for x in j['ben'])
    o = {'@context': 'https://schema.org', '@type': 'JobPosting', 'title': j['title'], 'description': desc, 'datePosted': TODAY.isoformat(),
         'validThrough': (TODAY + datetime.timedelta(days=120)).isoformat() + 'T23:59:00+01:00', 'employmentType': j['emp'],
         'hiringOrganization': {'@type': 'Organization', 'name': '404 Growth', 'sameAs': SITE, 'logo': SITE + '/apple-touch-icon.png'},
         'jobLocationType': 'TELECOMMUTE', 'applicantLocationRequirements': [{'@type': 'Country', 'name': c} for c in COUNTRIES], 'directApply': True,
         'url': SITE + path, 'identifier': {'@type': 'PropertyValue', 'name': '404 Growth', 'value': j['slug']}}
    return '<script type="application/ld+json">%s</script>' % json.dumps(o, ensure_ascii=False).replace('</', '<\\/')


def job_page(j, others):
    path = '/equipo/%s/' % j['slug']
    title = '%s · Trabaja en 404 Growth' % j['title']
    desc = j['hook']
    h = head(title, desc, path, j['slug'], extra=jsonld(j, path)) + nav()
    toc = [('rol', 'El rol y quiénes somos'), ('responsabilidades', 'Responsabilidades'), ('requisitos', 'Requisitos'), ('resultados', 'Resultados'), ('beneficios', 'Beneficios')]
    h += '<main id="main"><section class="hero" id="top"><div class="w"><div class="hg"><div><a class="crumb" href="/equipo/">← Todos los puestos</a><br><span class="chip"><i></i>%s</span><h1>%s</h1><p class="hook">%s</p>' % (
        e(j['kicker']), e(j['title']), e(j['hook']))
    h += '<ul class="facts">%s</ul><div class="cta"><a class="b-pri" href="#aplicar" data-apply>Enviar mi candidatura %s</a><span class="mut">10 minutos · Te contestamos en menos de 24 h</span></div></div>' % (
        ''.join('<li>%s</li>' % e(x) for x in mode_facts(j)), AR)
    first = j['results'][0]
    h += ('<aside class="sum" aria-label="El puesto en breve"><h3>En breve</h3><dl><div><dt>Modalidad</dt><dd>%s</dd></div><div><dt>%s</dt><dd>%s</dd></div>'
          '<div><dt>Prueba técnica</dt><dd>%s</dd></div><div><dt>Proceso</dt><dd>%s</dd></div></dl></aside></div>') % (
        e(j['mode']), 'Tu primer mes' if first[0] == '30 días' else e(first[0]), e(first[1]),
        e('%s: %d %s de trabajo como máximo y 48 horas de plazo' % (j['test']['title'], j['test']['hours'], 'hora' if j['test']['hours'] == 1 else 'horas')) if j.get('test') else 'No hace falta: te escribimos cuando abramos tu puesto.',
        'Respuesta en menos de 24 h. Entrevista, prueba técnica y, en 7 a 12 días, sabes si entras.' if j.get('test') else 'Respuesta en menos de 24 h. Te escribimos cuando abramos tu puesto.')
    h += '<nav class="toc" aria-label="En esta página">%s</nav></div></section>' % ''.join('<a href="#%s"><b>%02d</b>%s</a>' % (a, k + 1, e(b)) for k, (a, b) in enumerate(toc))
    # 01
    h += ('<section class="sec" id="rol"><div class="w sg"><div class="sh rv"><div class="sn">01</div><h2>El rol y quiénes somos</h2></div><div class="two rv">'
          '<div class="box"><h3>El rol</h3>%s</div><div class="box"><h3>Quiénes somos</h3>%s<div class="me"><img src="/christian-hola.jpg" alt="Christian Silva" width="52" height="52" loading="lazy">'
          '<div><b>Christian Silva</b><span>Fundador · Trabajarás directamente con él</span></div></div></div></div></div></section>') % (
        ''.join('<p>%s</p>' % e(p) for p in j['role']), ''.join('<p>%s</p>' % e(p) for p in R['about']))
    # 02
    h += ('<section class="sec" id="responsabilidades"><div class="w sg"><div class="sh rv"><div class="sn">02</div><h2>Responsabilidades</h2><p>Lo que harás cada semana.</p></div>'
          '<ol class="ol rv">%s</ol></div></section>') % ''.join('<li><b>%02d</b><span>%s</span></li>' % (k + 1, e(x)) for k, x in enumerate(j['resp']))
    # 03
    plus = '<p class="sub">Se valora</p><ul class="ck pl">%s</ul>' % ''.join('<li>%s</li>' % e(x) for x in j['plus']) if j.get('plus') else ''
    h += ('<section class="sec" id="requisitos"><div class="w sg"><div class="sh rv"><div class="sn">03</div><h2>Requisitos</h2><p>Lo que necesitas para hacerlo bien desde el primer día.</p></div>'
          '<div class="rv"><ul class="ck">%s</ul>%s</div></div></section>') % (''.join('<li>%s</li>' % e(x) for x in j['req']), plus)
    # 04
    h += ('<section class="sec" id="resultados"><div class="w sg"><div class="sh rv"><div class="sn">04</div><h2>Resultados</h2><p>Cómo sabremos, tú y nosotros, que va bien.</p></div>'
          '<ol class="res%s rv">%s</ol></div></section>') % (' n1' if len(j['results']) == 1 else '', ''.join('<li><b>%s</b><p>%s</p></li>' % (e(a), e(b)) for a, b in j['results']))
    # 05
    pay = '<p class="pay"><b>Retribución:</b> %s</p>' % e(j['pay']) if j.get('pay') else ''
    h += ('<section class="sec" id="beneficios"><div class="w sg"><div class="sh rv"><div class="sn">05</div><h2>Beneficios</h2><p>Lo que te llevas.</p></div>'
          '<div class="rv"><ul class="ben">%s</ul>%s</div></div></section>') % (''.join('<li>%s<span>%s</span></li>' % (SPARK, e(x)) for x in j['ben']), pay)
    h += process(None if j.get('test') else R.get('promise_open'))
    # la candidatura
    tst = j.get('test')
    bul = ['10 minutos, en 4 pasos', 'Se guarda mientras escribes: puedes seguir luego', 'Te contestamos en menos de 24 horas'] + (
        ['Si encajas: entrevista de 30 minutos y una prueba técnica de %d %s como máximo' % (tst['hours'], 'hora' if tst['hours'] == 1 else 'horas'), 'En 7 a 12 días sabes si entras al equipo'] if tst else [])
    h += ('<section class="apl" id="aplicar"><div class="w apl-g"><div class="apl-i rv"><span class="chip"><i></i>Candidatura</span><h2 style="margin-top:18px">Cuéntanos <span class="lm">qué haces mejor.</span></h2>'
          '<p>Nos importa más tu trabajo que tu CV: enséñanos lo que has hecho y cómo lo piensas.</p><ul>%s</ul></div><div class="rv">%s</div></div></section>') % (
        ''.join('<li>%s%s</li>' % (CHK, e(x)) for x in bul), form(j))
    # otros puestos
    if others:
        h += ('<section class="sec"><div class="w"><div class="sh rv" style="position:static;margin-bottom:26px"><div class="sn">Otros puestos</div><h2>¿Encajas mejor en otro?</h2></div>'
              '<div class="jobs rv">%s</div></div></section>') % ''.join(card(o) for o in others)
    h += '</main>' + foot(sticky='<div class="sticky"><a class="b-pri" href="#aplicar" data-apply>Enviar mi candidatura %s</a></div>' % AR)
    return h


def card(j):
    return ('<a class="job" href="/equipo/%s/" data-job="%s"><span class="k"><span>%s</span><em>%s</em></span><h3>%s</h3><p>%s</p><span class="go">Ver el puesto %s</span></a>'
            % (j['slug'], j['slug'], e(j['kicker'] + ' · ' + j['mode'].split('·')[0].strip()), 'Abierto' if j.get('open') else 'Cerrado', e(j['title']), e(j['hook']), AR))


def index_page():
    path = '/equipo/'
    title = 'Trabaja en 404 Growth · Puestos abiertos'
    desc = 'Buscamos a los mejores para llevar las tiendas físicas de toda España a internet: tiendas Shopify, captación por WhatsApp y Meta Ads. En remoto, desde España o Latinoamérica.'
    h = head(title, desc, path, 'equipo') + nav('#puestos', 'Ver puestos', [('#puestos', 'Puestos'), ('#proceso', 'Proceso'), ('/', 'Qué hacemos')])
    h += ('<main id="main"><section class="hero" id="top"><div class="w"><span class="chip"><i></i>Trabaja en 404 Growth</span><h1>Llevamos las tiendas de España a internet. <span class="lm">Ven a hacerlo con nosotros.</span></h1>'
          '<p class="hook">%s</p><ul class="facts"><li>100 %% en remoto</li><li>Desde España o Latinoamérica</li><li>IA en el día a día</li><li>Directo con el fundador</li></ul>'
          '<div class="cta"><a class="b-pri" href="#puestos">Ver los puestos %s</a><span class="mut">%s</span></div></div></section>') % (e(R['about'][0]), AR, e(R['promise']))
    h += ('<section class="sec" id="puestos"><div class="w"><div class="sh rv" style="position:static;margin-bottom:28px"><div class="sn">Puestos</div><h2>Puestos abiertos</h2></div>'
          '<div class="jobs rv">%s</div></div></section>') % ''.join(card(j) for j in R['jobs'])
    h += ('<section class="sec" id="nosotros"><div class="w sg"><div class="sh rv"><div class="sn">Nosotros</div><h2>Quiénes somos</h2></div><div class="box rv">%s'
          '<div class="me"><img src="/christian-hola.jpg" alt="Christian Silva" width="52" height="52" loading="lazy"><div><b>Christian Silva</b><span>Fundador de 404 Growth</span></div></div></div></div></section>') % (
        ''.join('<p>%s</p>' % e(p) for p in R['about']))
    vals = [('Con método', 'Cada tienda se hace igual de bien, cada vez: checklist de 15 días, plantillas y revisión antes de abrir.'),
            ('Con IA, cada día', 'Fotos, textos, propuestas y análisis: la IA hace lo repetitivo para que tú hagas lo que importa.'),
            ('En remoto', 'Trabajas desde España o desde Latinoamérica, en horario de España y con tu agenda. Medimos resultados, no horas.'),
            ('Claro y directo', 'Hablas con Christian, sin capas. Las cosas se dicen pronto y claras, también cuando algo se tuerce.')]
    h += ('<section class="sec"><div class="w"><div class="sh rv" style="position:static;margin-bottom:28px"><div class="sn">Cultura</div><h2>Cómo trabajamos</h2></div>'
          '<ul class="vals rv">%s</ul></div></section>') % ''.join('<li><b>%s</b><p>%s</p></li>' % (e(a), e(b)) for a, b in vals)
    h += process() + '</main>' + foot()
    return h


def tool_page(kind):
    if kind == 'prueba':
        h = head('Tu prueba técnica · 404 Growth', 'La prueba técnica de tu candidatura en 404 Growth.', '/equipo/prueba/', 'equipo', 'noindex,nofollow')
        h += nav('/equipo/', 'Puestos', []) + ('<main id="main" class="tool"><div class="w"><span class="chip"><i></i>Prueba técnica</span><h1 id="pz-h">Tu prueba técnica.</h1><p class="lead" id="pz-l"></p>'
                                             '<div id="pz" style="margin-top:8px"><p class="load">Cargando tu prueba…</p></div></div></main>')
    else:
        h = head('Elige la hora de tu entrevista · 404 Growth', 'Elige el día y la hora de tu entrevista con 404 Growth.', '/equipo/entrevista/', 'equipo', 'noindex,nofollow')
        h += nav('/equipo/', 'Puestos', []) + ('<main id="main" class="tool"><div class="w" style="max-width:820px"><span class="chip"><i></i>Entrevista</span><h1 id="iv-h">Elige cuándo hablamos.</h1><p class="lead" id="iv-l"></p>'
                                             '<div id="iv" style="margin-top:32px"><p class="load">Cargando las horas libres…</p></div></div></main>')
    return h + foot()


# ---------- la miniatura de cada página (1200x630, SF Pro en el Mac) ----------
def og_html(chip, title, sub):
    z = 100 if len(title) <= 22 else 92 if len(title) <= 32 else 80
    return ('<!doctype html><meta charset="utf-8"><style>*{box-sizing:border-box;margin:0;padding:0}html,body{width:1200px;height:630px;overflow:hidden}'
            'body{background:#F6F7F3;color:#111311;font-family:-apple-system,BlinkMacSystemFont,"SF Pro Display",Inter,Arial,sans-serif;-webkit-font-smoothing:antialiased;position:relative}'
            '.g{position:absolute;inset:0;background:radial-gradient(520px 420px at 92%% 10%%,rgba(185,214,162,.95),rgba(201,221,184,.35) 55%%,transparent 75%%),radial-gradient(600px 420px at 0%% 105%%,rgba(201,221,184,.7),transparent 70%%),radial-gradient(240px 240px at 64%% 78%%,rgba(17,19,17,.12),transparent 70%%)}'
            '.top{position:absolute;left:64px;top:52px;display:flex;align-items:center;gap:14px;font-weight:800;font-size:28px;letter-spacing:-.03em}.top svg{width:50px;height:38px}'
            '.c{position:absolute;left:64px;right:64px;top:140px;bottom:132px;border-radius:40px;padding:40px 48px 44px;display:flex;flex-direction:column;justify-content:space-between;align-items:flex-start;background:linear-gradient(160deg,rgba(255,255,255,.86),rgba(255,255,255,.5));'
            'box-shadow:inset 0 2px 0 #fff,inset 0 0 0 1.5px rgba(255,255,255,.7),0 0 0 1px rgba(17,19,17,.05),0 40px 80px -40px rgba(30,45,25,.45);-webkit-backdrop-filter:blur(24px) saturate(160%%);backdrop-filter:blur(24px) saturate(160%%)}'
            '.chip{display:inline-flex;align-items:center;gap:12px;font-weight:600;font-size:24px;background:#E8F0E0;color:#2F4527;border-radius:99px;padding:9px 22px 9px 17px}'
            '.chip i{width:11px;height:11px;border-radius:50%%;background:#B3CE9C;box-shadow:0 0 0 6px rgba(179,206,156,.35)}'
            'h1{font-size:%dpx;line-height:.98;letter-spacing:-.05em;font-weight:500;max-width:960px;text-wrap:balance}'
            '.b{position:absolute;left:64px;right:64px;bottom:52px;display:flex;justify-content:space-between;align-items:center;font-size:24px;color:#3A3F3A}'
            '.b b{font-weight:600;color:#F3F6EF;background:linear-gradient(160deg,#22261F,#0E100E);border-radius:99px;padding:14px 26px;box-shadow:0 14px 30px -14px rgba(17,19,17,.6)}</style>'
            '<div class="g"></div><div class="top">%s<span>404 Growth</span></div><div class="c"><span class="chip"><i></i>%s</span><h1>%s</h1></div>'
            '<div class="b"><span>%s</span><b>404growth.com/equipo</b></div>') % (z, LOGO.replace('class="mk" ', ''), e(chip), e(title), e(sub))


def main():
    a = sys.argv[1:]
    web = a[0]
    og = a[a.index('--og') + 1] if '--og' in a else None
    out = os.path.join(web, 'equipo')
    os.makedirs(out, exist_ok=True)
    w = lambda rel, s: (os.makedirs(os.path.dirname(os.path.join(out, rel)) or out, exist_ok=True), open(os.path.join(out, rel), 'w', encoding='utf-8').write(s))
    for n in ('e.css', 'e.js'):
        shutil.copy(os.path.join(HERE, 'web', n), os.path.join(out, n))
    w('index.html', index_page())
    for j in R['jobs']:
        others = [o for o in R['jobs'] if o['slug'] != j['slug'] and o['slug'] != 'abierta'] + ([o for o in R['jobs'] if o['slug'] == 'abierta'] if j['slug'] != 'abierta' else [])
        w(j['slug'] + '/index.html', job_page(j, others[:3]))
    w('prueba/index.html', tool_page('prueba'))
    w('entrevista/index.html', tool_page('entrevista'))
    # el mapa del sitio
    sm = os.path.join(web, 'sitemap.xml')
    if os.path.exists(sm):
        s = open(sm, encoding='utf-8').read()
        add = ''.join('  <url><loc>%s%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>\n' % (SITE, u, TODAY.isoformat(), p)
                      for u, p in [('/equipo/', '0.5')] + [('/equipo/%s/' % j['slug'], '0.5') for j in R['jobs']] if SITE + u + '<' not in s)
        if add:
            open(sm, 'w', encoding='utf-8').write(s.replace('</urlset>', add + '</urlset>'))
    if og:
        os.makedirs(og, exist_ok=True)
        lst = {'equipo': og_html('Trabaja en 404 Growth', 'Llevamos las tiendas de España a internet.', 'Puestos en remoto')}
        for j in R['jobs']:
            lst[j['slug']] = og_html(j['og'][0], j['og'][1], j['mode'])
        for k, v in lst.items():
            open(os.path.join(og, 'og-%s.html' % k), 'w', encoding='utf-8').write(v)
        json.dump(sorted(lst), open(os.path.join(og, 'lista.json'), 'w'))
    print('ok', out, 'v=' + V, '(%d puestos)' % len(R['jobs']))


if __name__ == '__main__':
    main()
