# Propuesta v42 (21/11/2026): la de gen33v.py, más corta y con el vídeo arriba. Lo que pidió Chris (21/11, 22:45):
#   1. portada: «Esto no es una web. Es la tienda online de X.», el recorrido solo de la tienda y «Reservar 30 min».
#      Sin el texto de debajo ni las cifras (seguidores, 24/7…).
#   2. «Así se vería X online.»: la tienda entera en el navegador grande.
#   3. el vídeo: «¿Os preguntáis quién soy y por qué os he hecho esto?», con Christian nítido y quieto (fotograma fijo)
#      y el botón «Reproducir con audio». Justo debajo, «Elige día y hora» (la agenda), sin más texto.
#   4. «Cada prenda, lista para comprar.» (la ficha y los cuatro puntos).
#   5. la garantía del vídeo: vendéis online el triple de lo que os cuesta la tienda o trabajamos gratis hasta conseguirlo.
#   6. las ideas de anuncios y el plan de 15 días. Y ya: sin diagnóstico ni cierre.
#   (25/11) Entre 2 y 3, «Los números»: los casos de Kiss of Life e Intenso (numeros42.py).
#   Todo centrado y con los márgenes de la página.
# La simulación de pedido y la comparación con su web de la primera versión están en el commit afa90b1.
# Parte de la propuesta hecha con gen33v.py (out/p-<slug>.html):
# python3 gen42.py <slug> [...] [--out out42] [--vsl /v/propuesta/index.m3u8] [--poster /v/propuesta/poster.jpg]
#                  [--poster-file poster.jpg (lo mete dentro, para verla sin publicar)] [--hls /v/hls.light.min.js]
import os, re, json, html, base64, argparse
import numeros42 as N42

HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser()
ap.add_argument('slugs', nargs='+')
ap.add_argument('--src', default=os.path.join(HERE, 'out'))
ap.add_argument('--out', default=os.path.join(HERE, 'out42'))
ap.add_argument('--vsl', default='/v/propuesta/index.m3u8')
ap.add_argument('--poster', default='/v/propuesta/poster.jpg')
ap.add_argument('--poster-file')
ap.add_argument('--hls', default='/v/hls.light.min.js')
ap.add_argument('--test', help='nombre de una copia de prueba (p-<test>.html): sin contador de visitas y sin tocar el CRM')
ap.add_argument('--jpg', action='store_true', help='dejar las fotos en .jpg (por defecto, .webp: pesan la mitad)')
A = ap.parse_args()
POSTER = A.poster
if A.poster_file: POSTER = 'data:image/jpeg;base64,' + base64.b64encode(open(A.poster_file, 'rb').read()).decode()
E = html.escape
ITEMS = {'moda': 'prendas', 'sneakers': 'zapatos', 'calzado': 'zapatos', 'joya': 'piezas', 'optica': 'gafas', 'cosmetica': 'productos', 'suplementos': 'productos'}

CSS = r'''<style id="z42">
/* v42: todo centrado */
.hero h1{font-size:clamp(38px,6.2vw,82px);text-wrap:balance}
.hero .hb{padding-bottom:84px}
.hero h1 .z4-l{font-weight:300;letter-spacing:-.035em}
.hero h1 u{text-decoration:underline;text-decoration-thickness:.075em;text-underline-offset:.12em;text-decoration-color:currentColor}
.hero .lede{gap:0}
.chap{justify-content:center}
.head{grid-template-columns:1fr;justify-items:center;text-align:center;gap:18px;margin-bottom:48px}
.head h2,.head h3{text-wrap:balance}
.head p{max-width:600px;font-size:19px}
.ctarow{text-align:center}
.dark .chap .num{color:var(--tl);border-color:currentColor}
/* el vídeo */
#video{padding-top:96px}
.z4-h{text-align:center;max-width:820px;margin:0 auto}
.z4-h h2{text-wrap:balance}
.z4-h p{font-size:19px;line-height:1.4;color:var(--mute);margin:18px auto 0;letter-spacing:-.015em}
.z4-h p b{color:var(--ink);font-weight:600}
.z4-vd{max-width:900px;margin:40px auto 0;padding:10px;border-radius:30px;background:#141110;box-shadow:0 40px 90px -40px rgba(20,17,16,.6)}
.z4-scn{position:relative;aspect-ratio:16/9;border-radius:21px;overflow:hidden;background:#000 center/cover no-repeat}
.z4-scn video{position:absolute;inset:0;width:100%;height:100%;display:block;object-fit:contain;background:#000;opacity:0;transition:opacity .3s}
.z4-scn.aud video{opacity:1}
.z4-go{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);z-index:3;display:inline-flex;align-items:center;gap:13px;border:0;cursor:pointer;font-family:inherit;font-size:17px;font-weight:600;letter-spacing:-.012em;color:#141110;background:#fff;padding:10px 24px 10px 10px;border-radius:99px;white-space:nowrap;box-shadow:0 12px 44px rgba(0,0,0,.4);transition:transform .25s cubic-bezier(.2,.8,.2,1)}
.z4-go i{width:46px;height:46px;border-radius:50%;background:#141110;display:grid;place-items:center;flex:none}
.z4-go svg{width:18px;height:18px;color:#fff;margin-left:3px}
@media (hover:hover){.z4-go:hover{transform:translate(-50%,-50%) scale(1.045)}}.z4-go:active{transform:translate(-50%,-50%) scale(.97)}
.z4-scn.aud .z4-go{display:none}
/* la agenda, debajo del vídeo y centrada */
#video .ag.ag-in{padding-top:88px}
#video .ag-w{text-align:center}
#video .ag h2{margin-bottom:36px}
#video .ag-app{text-align:left;max-width:900px;margin:0 auto}
/* la ficha */
#ficha{padding-top:110px}
/* la garantía */
#garantia{background:var(--ink);color:#fff;text-align:center;overflow:hidden;position:relative}
#garantia:before{content:"";position:absolute;left:50%;top:-10%;width:900px;height:620px;transform:translateX(-50%);border-radius:50%;background:radial-gradient(closest-side,color-mix(in srgb,var(--t) 42%,transparent),transparent);opacity:.55;pointer-events:none}
#garantia .wrap{position:relative}
#garantia .chap .lb{color:var(--mute2)}
.z4-x3{font-size:clamp(130px,22vw,280px);font-weight:700;letter-spacing:-.07em;line-height:.85;margin:6px 0 26px}
.z4-x3 small{font-size:.42em;font-weight:300;letter-spacing:-.03em;vertical-align:.62em;margin-right:.04em;color:var(--mute2)}
#garantia h2{max-width:860px;margin:0 auto;text-wrap:balance}
#garantia h2 span{display:block;color:var(--mute2);font-weight:400;margin-top:.12em}
#garantia .z4-ct{margin:22px 0 0;font-size:17px;color:var(--mute2)}
#garantia .btns{margin-top:40px}
/* v42b (22/11): botón para bajar a la agenda, debajo del vídeo */
.z4-dn{display:flex;justify-content:center;margin-top:30px}
.z4-dn .cta span{display:inline-block;animation:z4b 1.8s ease-in-out infinite}
@keyframes z4b{0%,100%{transform:translateY(0)}50%{transform:translateY(4px)}}
@media (prefers-reduced-motion:reduce){.z4-dn .cta span{animation:none}}
/* v42b: menos aire entre secciones (Chris, 22/11: «en algunas hay demasiado») */
.sk .sec{padding-top:76px;padding-bottom:76px}
.hero .hb{padding-bottom:36px}
#tienda{padding-top:56px!important}
#video{padding-top:64px!important;padding-bottom:40px!important}
#video .ag.ag-in{padding-top:64px;padding-bottom:0}
#video .ag h2{margin-bottom:28px}
#ficha{padding-top:64px!important;padding-bottom:76px!important}
#ficha .head.fh{margin-top:0!important}
@media (max-width:760px){
 .sk .sec{padding-top:56px;padding-bottom:56px}
 .hero .hb{padding-bottom:24px!important}
 #tienda{padding-top:40px!important}
 #video{padding-top:48px!important;padding-bottom:28px!important}
 #video .ag.ag-in{padding-top:48px!important}
 #ficha{padding-top:48px!important;padding-bottom:56px!important}
 .z4-dn{margin-top:22px}
}
@media (max-width:760px){
 .wrap{padding-left:20px;padding-right:20px}
 .hero .hb{padding-bottom:56px}
 .head{margin-bottom:32px}.head p{font-size:17px}
 #video{padding-top:72px}
 .z4-h p{font-size:17px}
 .z4-vd{padding:6px;border-radius:22px;margin-top:30px}.z4-scn{border-radius:17px}
 .z4-go{font-size:15px;gap:10px;padding:8px 18px 8px 8px}.z4-go i{width:38px;height:38px}.z4-go svg{width:15px;height:15px}
 #video .ag.ag-in{padding-top:64px}#video .ag h2{margin-bottom:24px}
 #ficha{padding-top:80px}
 #garantia .z4-ct{font-size:15.5px}
}
/* v42 · fluidez (Chris, 21/11: «va súper lagueada… viene como inclinada y se va poniendo recta»).
   Nada inclinado ni que se enderece al bajar: la tienda aparece plana desde el principio. Sin desenfoques ni cristal
   (backdrop-filter) en nada: con el dedo rápido el móvil tenía que volver a pintarlos en cada fotograma.
   La profundidad, con sombras quietas detrás de los marcos. */
.hero .stage{perspective:none!important}
.hero .lap,.hero .stage .ph,.shopsec .bw,.sk-tilt{transform:none!important;opacity:1!important;transition:none!important;animation:none!important}
.sk .rv{opacity:1!important;transform:none!important;filter:none!important;transition:none!important}
*,*:before,*:after{-webkit-backdrop-filter:none!important;backdrop-filter:none!important}
.hero .stage:before,.sk-aur,.glow,.stage .glow{filter:none!important;animation:none!important}
.nav .wrap,.wa-fab{background:rgba(36,36,36,.95)!important}
.cta{backdrop-filter:none!important}
.shopsec>.wrap>.bw,.pdpz .bw{box-shadow:0 1px 2px rgba(0,0,0,.05),0 30px 60px -24px rgba(var(--sh),.3),0 90px 160px -60px rgba(var(--sh),.45),0 0 0 1px rgba(0,0,0,.06)!important}
</style>'''

VID = '''</div></section>
{numeros}<section class="sec" id="video"><div class="wrap">
<div class="chap"><span class="num">02</span><span class="lb">Si no me conocéis</span></div>
<div class="z4-h"><h2>¿Os preguntáis quién soy y por qué os he hecho esto?</h2><p>3 minutos. <b>Ponedlo con sonido.</b></p></div>
<div class="z4-vd"><div class="z4-scn" id="z4scn" style="background-image:url('{poster}')">
<video id="z4v" playsinline preload="none" aria-label="Vídeo de Christian · 404 Growth"></video>
<button class="z4-go" id="z4go" type="button"><i aria-hidden="true"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M7 4.5v15l13-7.5z"/></svg></i>Reproducir con audio</button>
</div></div>
<div class="z4-dn"><a class="cta" href="#agenda" data-ag="1">Agendar reunión gratuita<span>↓</span></a></div>
{agenda}
</div></section>
<section class="sec" id="ficha" style="padding-bottom:100px"><div class="wrap">'''

VID_JS = r'''<script>
/* v42: el vídeo. Se ve a Christian quieto y nítido (fotograma fijo); «Reproducir con audio» lo pone desde el principio con sonido.
   Lo que se ve lo cuenta el contador (vplay, vprog 25/50/75, vend), como en /book. */
(function(){var VSL={src:'{src}',hls:'{hls}'};var d=document,sc=d.getElementById('z4scn');if(!sc)return;
 var v=d.getElementById('z4v'),go=d.getElementById('z4go'),on=false;
 function play(){var p=v.play();if(p&&p.catch)p.catch(function(){sc.classList.remove('aud')})}
 function attach(){if(on)return;on=true;
  if(/\.m3u8(\?|$)/.test(VSL.src)&&!v.canPlayType('application/vnd.apple.mpegurl')){var s=d.createElement('script');s.src=VSL.hls;
   s.onload=function(){if(window.Hls&&Hls.isSupported()){var h=new Hls({abrEwmaDefaultEstimate:5e6});h.loadSource(VSL.src);h.attachMedia(v)}else v.src=VSL.src;play()};
   d.head.appendChild(s)}else{v.src=VSL.src;play()}}
 go.addEventListener('click',function(){sc.classList.add('aud');v.muted=false;v.volume=1;v.controls=true;if(on){try{v.currentTime=0}catch(e){}play()}else attach()});
 v.addEventListener('ended',function(){v.controls=false;sc.classList.remove('aud')});
})();
</script>'''

GAR = '''<section class="sec" id="garantia"><div class="wrap">
<div class="chap"><span class="num">03</span><span class="lb">La garantía</span></div>
<div class="z4-x3"><small>×</small>3</div>
<h2>Vendéis online el triple de lo que os cuesta la tienda.<span>O trabajamos gratis hasta conseguirlo.</span></h2>
<p class="z4-ct">Por contrato.</p>
<div class="btns"><a class="cta" href="#agenda" data-ag="1">Reservar 30 min<span>→</span></a></div>
</div></section>
'''


def cut(h, a, b):
    """quita desde a (incluido) hasta b (incluido)"""
    i = h.index(a); j = h.index(b, i) + len(b)
    return h[:i] + h[j:]


def build(slug):
    h = open(os.path.join(A.src, f'p-{slug}.html'), encoding='utf-8').read()
    d = json.load(open(os.path.join(HERE, 'data', f'{slug}.json'), encoding='utf-8'))
    name = d['name']; items = ITEMS.get(d.get('niche', 'moda'), 'productos')
    def rep(a, b):
        nonlocal h; assert h.count(a) == 1, (slug, a[:70], h.count(a)); h = h.replace(a, b)

    # cabeza: título y vista previa de WhatsApp
    h = re.sub(r'<title>[^<]*</title>', f'<title>{E(name)} · vuestra tienda online</title>', h, count=1)
    h = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{E(name)}, vuestra tienda online ya puede cobrar">', h, count=1)
    h = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="No es una web: aquí eligen, pagan y os llega el pedido. Os la he preparado con vuestras {items}.">', h, count=1)
    h = h.replace('</head>', CSS + N42.CSS + '</head>', 1)

    # menú
    h, k = re.subn(r'<div class="lk2">.*?</div>', '<div class="lk2"><a href="#tienda">Tienda</a><a href="#video">Vídeo</a><a href="#agenda">Agenda</a><a href="#garantia">Garantía</a></div>', h, count=1, flags=re.S); assert k == 1

    # portada: titular, recorrido y «Reservar 30 min»; sin el texto ni las cifras
    h, k = re.subn(r'<h1>.*?</h1>', f'<h1><span class="z4-l">Esto no es una web normal.</span><br><span class="t">Es la tienda <u>online</u> de {E(name)}.</span></h1>', h, count=1, flags=re.S); assert k == 1
    i = h.index('<div class="hb">'); j = h.index('</header>', i)
    h = h[:i] + ('<div class="hb"><div class="lede"><div class="btns"><a class="cta" href="#agenda" data-ag="1">Reservar 30 min<span>→</span></a>'
                 '<a class="cta ghost" href="#video">Ver el vídeo · 3 min</a></div></div></div>') + h[j:]

    # la tienda: solo el titular y el navegador grande
    h, k = re.subn(r'(<section class="sec shopsec" id="tienda">.*?<div class="head"><h2>.*?</h2>)<p>.*?</p>', r'\1', h, count=1, flags=re.S); assert k == 1
    h = cut(h, '<div class="ctarow">', '</div>')

    # la agenda sale de donde estaba y va debajo del vídeo, solo con «Elige día y hora.»
    a = h.index('<!--ag-->'); b = h.index('<!--/ag-->') + len('<!--/ag-->')
    ag = h[a:b]; h = h[:a] + VID.replace('{poster}', POSTER).replace('{numeros}', N42.HTML) + h[b:]
    ag, k = re.subn(r'<span class="ag-eb">[^<]*</span><h2>.*?</h2><p class="ag-sub">.*?</p>', '<span class="ag-eb">Videollamada · 30 minutos</span><h2>Elige día y hora.</h2>', ag, count=1, flags=re.S); assert k == 1, ag[:400]
    h = h.replace('{agenda}', ag, 1)

    # fuera el diagnóstico y el cierre; la garantía, antes de los anuncios
    h = cut(h, '<section class="sec" id="diagnostico">', '</section>')
    h = cut(h, '<section class="close" id="hablar"', '</section>')
    rep('<section class="sec dark" id="captacion">', GAR + '<section class="sec dark" id="captacion">')
    h = h.replace('<span class="num">03</span><span class="lb">Ideas de campaña</span>', '<span class="num">04</span><span class="lb">Ideas de campaña</span>')
    h = h.replace('<span class="num">04</span><span class="lb">Plan</span>', '<span class="num">05</span><span class="lb">Plan</span>')

    # menos texto: fuera los párrafos de las cabeceras de anuncios y plan
    for sid in ('captacion', 'plan'):
        h, k = re.subn(r'(<section class="sec[^"]*" id="' + sid + r'"[^>]*>.*?<div class="head"><h2>.*?</h2>)<p>.*?</p>', r'\1', h, count=1, flags=re.S); assert k == 1, sid

    # contador: partes de la página
    h = re.sub(r'PARTS=\[\[.*?\]\]', 'PARTS=[["tienda", 2], ["numeros", 3], ["video", 4], ["agenda", 5], ["ficha", 6], ["garantia", 7], ["captacion", 8], ["plan", 9]]', h, count=1)
    h = h.replace('</body>', VID_JS.replace('{src}', A.vsl).replace('{hls}', A.hls) + N42.JS + '</body>', 1)

    # el brillo de color detrás de los marcos del inicio: antes era su foto con filter:blur(48px), que el móvil
    # repintaba al bajar; ahora es la misma foto ya difuminada, pequeña y dentro de la página (unos KB)
    from PIL import Image, ImageFilter, ImageEnhance, ImageDraw
    import io
    g = Image.open(os.path.join(A.src, f'p-{slug}--b--h.jpg')).convert('RGB').resize((200, 120), Image.LANCZOS)
    g = ImageEnhance.Color(g.filter(ImageFilter.GaussianBlur(14))).enhance(1.3)
    m = Image.new('L', (200, 120), 0); ImageDraw.Draw(m).ellipse((30, 22, 170, 98), fill=255); m = m.filter(ImageFilter.GaussianBlur(16))
    g.putalpha(m); bb = io.BytesIO(); g.save(bb, 'WEBP', quality=70)
    glow = 'data:image/webp;base64,' + base64.b64encode(bb.getvalue()).decode()
    h = h.replace('</head>', '<style>.glow{background:url(' + glow + ') center/100% 100% no-repeat!important;border-radius:0!important;filter:none!important;left:-6%!important;right:-6%!important;top:-4%!important;bottom:-10%!important}</style></head>', 1)

    # fuera la inclinación que se endereza al bajar (portátil del inicio y tienda grande)
    rep("function frame(){tick=false;if(RM)return;", "function frame(){tick=false;return;")
    rep("if(big)big.classList.add('sk-tilt');", "")
    # los marcos de la tienda cargan antes (2.500 px de margen) y, al terminar de cargar la página, todos:
    # al bajar rápido ya están pintados
    rep("{rootMargin:'400px 0px'});F.forEach(function(f){io.observe(f)})}else F.forEach(L);",
        "{rootMargin:'2500px 0px'});F.forEach(function(f){io.observe(f)});addEventListener('load',function(){setTimeout(function(){F.forEach(L)},900)})}else F.forEach(L);")

    # la tienda de dentro: sin cristal ni desenfoques cuando va dentro de la propuesta (html.emb)
    st = open(os.path.join(A.src, f'p-{slug}--tienda.html'), encoding='utf-8').read()
    css = ('<style id="z42e">.emb *,.emb *:before,.emb *:after{-webkit-backdrop-filter:none!important;backdrop-filter:none!important}'
           '.emb .gl{background:rgba(255,255,255,.22)!important}.emb .gk{background:rgba(28,20,18,.66)!important}</style>')
    assert st.count('</head>') == 1; st = st.replace('</head>', css + '</head>')
    # dentro de la propuesta, el aviso de arriba no rota (repintaba la tienda cada 3 s)
    if 'if(an.length>1)setInterval(' in st: st = st.replace('if(an.length>1)setInterval(', 'if(an.length>1&&!emb)setInterval(', 1)

    # fotos en webp (la mitad de peso); la de la vista previa de WhatsApp sigue en jpg
    if not A.jpg:
        from PIL import Image
        rx = re.compile(r'(/p-' + re.escape(slug) + r'--b--(?!og\.)[a-z0-9]+)\.jpg')
        names = set(m.group(1) for m in rx.finditer(h + st))
        h = rx.sub(r'\1.webp', h); st = rx.sub(r'\1.webp', st)
        os.makedirs(A.out, exist_ok=True)
        for n in sorted(names):
            src = os.path.join(A.src, n.lstrip('/') + '.jpg'); dst = os.path.join(A.out, n.lstrip('/') + '.webp')
            if not os.path.exists(dst): Image.open(src).convert('RGB').save(dst, 'WEBP', quality=72, method=6)

    name_out = slug
    if A.test:
        name_out = A.test
        h = h.replace(f'/p-{slug}--tienda', f'/p-{A.test}--tienda')
        rep(f'var slug="{slug}"', 'var slug=""')
        h = h.replace(f'data-slug="{slug}"', 'data-slug="prueba-v42"').replace(f'utm_campaign={slug}', 'utm_campaign=prueba-v42')
    os.makedirs(A.out, exist_ok=True)
    out = os.path.join(A.out, f'p-{name_out}.html')
    open(out, 'w', encoding='utf-8').write(h)
    open(os.path.join(A.out, f'p-{name_out}--tienda.html'), 'w', encoding='utf-8').write(st)
    print(slug, len(h), out)


for s in A.slugs: build(s)
