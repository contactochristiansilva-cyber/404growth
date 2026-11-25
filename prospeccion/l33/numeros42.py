# «Los números» (25/11/2026): sección de las propuestas v42 entre la tienda («Así se vería X online.») y el vídeo.
# Chris: muchos responden «qué bonito, pero ahora no lo necesitamos»; aquí ven dos tiendas reales que hemos hecho.
# Dos cuadrados 1:1 (hero en móvil oscurecido + logo); al tocar uno se despliega debajo su historia
# (Antes · Qué hicimos · Ahora) y 4 cifras; tocarlo otra vez lo recoge; tocar el otro cambia de caso.
# Colores de 404 (verde bosque, menta, lima), sin backdrop-filter ni blur (fluidez en el móvil).
# Fotos en /casos/ (web117-404growth/casos/, fuente en prospeccion/l33/casos/).
# Cifras de Chris (25/11/2026): facturado el primer mes, Kiss of Life 4.237 € e Intenso 6.291 €.

CSS = r'''<style id="z4n">
#numeros{--mint:#7FD3B6;--mintl:#9FCFBE;--lime:#D4F27A;--card:#0F352E;--line:rgba(127,211,182,.16);
 color:#fff;padding:96px 0 88px;text-align:center;
 background:radial-gradient(70% 40% at 50% 0%,rgba(127,211,182,.16),transparent 70%),radial-gradient(60% 50% at 100% 100%,rgba(46,122,100,.2),transparent 70%),linear-gradient(180deg,#0B2B26 0%,#0A2722 60%,#071D19 100%)}
#numeros [hidden]{display:none!important}
#numeros .zn-w{max-width:1080px;margin:0 auto;padding:0 max(20px,env(safe-area-inset-left,0px));display:flex;flex-direction:column;align-items:center;gap:34px}
#numeros .zn-eb{display:inline-block;border-radius:99px;padding:8px 16px;font-size:12px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--mint);
 background:linear-gradient(180deg,rgba(255,255,255,.13),rgba(255,255,255,.04));border:1px solid rgba(255,255,255,.16);box-shadow:inset 0 1px 0 rgba(255,255,255,.3)}
#numeros h2.zn-t{margin:0;font-size:clamp(36px,5.2vw,58px);line-height:1.04;letter-spacing:-.035em;font-weight:300;color:var(--mintl);text-wrap:balance}
#numeros h2.zn-t b{display:block;font-size:1em;line-height:inherit;letter-spacing:inherit;font-weight:700;color:#fff;margin:0}
#numeros p.zn-sub{margin:-16px 0 0;max-width:520px;font-size:17px;line-height:1.5;color:rgba(255,255,255,.72)}
#numeros .zn-cases{width:100%;max-width:820px;display:grid;grid-template-columns:1fr 1fr;gap:20px}
#numeros .zn-case{position:relative;aspect-ratio:1/1;border:0;padding:0;margin:0;border-radius:28px;overflow:hidden;cursor:pointer;background:#071A17;font:inherit;color:#fff;-webkit-tap-highlight-color:transparent;
 box-shadow:0 0 0 1px rgba(127,211,182,.14),0 2px 4px rgba(0,0,0,.35),0 24px 48px -16px rgba(0,0,0,.6),0 60px 110px -30px rgba(0,0,0,.65);transition:opacity .25s ease,box-shadow .25s ease}
#numeros .zn-case img.zn-bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.5;transition:opacity .3s ease}
#numeros .zn-case:after{content:"";position:absolute;inset:0;background:radial-gradient(60% 55% at 50% 50%,rgba(7,26,23,.35),rgba(7,26,23,.75))}
#numeros .zn-in{position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;padding:20px}
#numeros .zn-logo{display:block;width:auto}
#numeros .zn-logo.k{height:72px}#numeros .zn-logo.i{height:54px;margin-bottom:8px}
#numeros .zn-what{font-size:14px;color:rgba(255,255,255,.8)}
#numeros .zn-more{position:absolute;left:50%;bottom:20px;transform:translateX(-50%);z-index:1;display:inline-flex;align-items:center;gap:8px;white-space:nowrap;border-radius:99px;padding:9px 16px;font-size:14px;font-weight:600;color:#fff;
 background:linear-gradient(180deg,rgba(255,255,255,.16),rgba(255,255,255,.05));border:1px solid rgba(255,255,255,.2);box-shadow:inset 0 1px 0 rgba(255,255,255,.35),0 8px 20px -8px rgba(0,0,0,.5)}
#numeros .zn-more svg{width:16px;height:16px;transition:transform .3s ease}
@media (hover:hover){#numeros .zn-case:hover img.zn-bg{opacity:.62}}
#numeros .zn-case[aria-expanded="true"]{box-shadow:0 0 0 2px var(--lime),0 2px 4px rgba(0,0,0,.35),0 24px 48px -16px rgba(0,0,0,.6)}
#numeros .zn-case[aria-expanded="true"] img.zn-bg{opacity:.62}
#numeros .zn-case[aria-expanded="true"] .zn-more{background:var(--lime);color:#0B2B26;border-color:transparent}
#numeros .zn-case[aria-expanded="true"] .zn-more svg{transform:rotate(180deg)}
#numeros .zn-cases.on .zn-case[aria-expanded="false"]{opacity:.62}
#numeros .zn-dr{width:100%;display:grid;grid-template-rows:0fr;transition:grid-template-rows .45s cubic-bezier(.2,.7,.2,1),margin .45s ease;margin-top:-34px}
#numeros .zn-dr.open{grid-template-rows:1fr;margin-top:0}
#numeros .zn-dr>div{min-height:0;overflow:hidden}
#numeros .zn-st{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);gap:40px;align-items:center;text-align:left;padding:8px 4px 4px;opacity:0;transform:translateY(-8px);transition:opacity .35s ease .1s,transform .35s ease .1s}
#numeros .zn-dr.open .zn-st{opacity:1;transform:none}
#numeros .zn-shot{display:flex;justify-content:center}
#numeros .zn-ph{width:240px;border-radius:44px;padding:9px;background:#071A17;border:1px solid rgba(255,255,255,.07);box-shadow:inset 0 1px 0 rgba(255,255,255,.07),0 2px 4px rgba(0,0,0,.35),0 24px 48px -16px rgba(0,0,0,.6),0 60px 110px -30px rgba(0,0,0,.65)}
#numeros .zn-ph img{display:block;width:100%;aspect-ratio:9/16;object-fit:cover;object-position:top;border-radius:35px}
#numeros .zn-tx{display:flex;flex-direction:column;gap:20px;align-items:flex-start}
#numeros .zn-who{font-size:13px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--mint)}
#numeros h3.zn-h{margin:-8px 0 0;font-size:34px;line-height:1.1;letter-spacing:-.025em;font-weight:700;color:#fff;text-wrap:balance}
#numeros h3.zn-h span{font-weight:300;color:var(--mintl)}
#numeros ul.zn-b{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:14px;max-width:560px}
#numeros ul.zn-b li{display:grid;grid-template-columns:96px minmax(0,1fr);gap:12px;align-items:start;font-size:16px;line-height:1.5;color:rgba(255,255,255,.72);margin:0;padding:0}
#numeros ul.zn-b li:before{display:none}
#numeros ul.zn-b li b{align-self:start;font-size:12px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--mint);padding-top:3px}
#numeros .zn-k{width:100%;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px}
#numeros .zn-k>div{border-radius:18px;padding:14px 14px 12px;background:var(--card);border:1px solid var(--line);box-shadow:inset 0 1px 0 rgba(255,255,255,.05),0 12px 24px -12px rgba(0,0,0,.5);display:flex;flex-direction:column;gap:2px}
#numeros .zn-k strong{font-size:24px;font-weight:700;letter-spacing:-.02em;color:#fff;font-variant-numeric:tabular-nums;white-space:nowrap}
#numeros .zn-k .hl strong{color:var(--lime)}
#numeros .zn-k span{font-size:12.5px;line-height:1.35;color:rgba(255,255,255,.72)}
#numeros a.zn-cta{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:56px;padding:0 28px;border-radius:99px;background:var(--lime);color:#0B2B26;font-size:17px;font-weight:600;text-decoration:none;box-shadow:inset 0 1px 0 rgba(255,255,255,.5),0 12px 28px -10px rgba(212,242,122,.45)}
#numeros .zn-case:focus-visible,#numeros a.zn-cta:focus-visible{outline:2px solid var(--lime);outline-offset:3px}
@media (prefers-reduced-motion:reduce){#numeros .zn-dr,#numeros .zn-st,#numeros .zn-case,#numeros .zn-bg,#numeros .zn-more svg{transition:none}}
@media (max-width:700px){
 #numeros{padding:64px 0 56px}
 #numeros .zn-w{gap:28px;padding:0 16px}
 #numeros p.zn-sub{font-size:15px;margin-top:-12px}
 #numeros .zn-cases{gap:10px}
 #numeros .zn-case{border-radius:20px}
 #numeros .zn-logo.k{height:44px}#numeros .zn-logo.i{height:30px}
 #numeros .zn-what{display:none}
 #numeros .zn-more{bottom:10px;padding:7px 11px;font-size:12.5px;gap:5px}
 #numeros .zn-more svg{width:13px;height:13px}
 #numeros .zn-dr{margin-top:-28px}
 #numeros .zn-st{grid-template-columns:1fr;gap:24px}
 #numeros .zn-shot{display:none}
 #numeros h3.zn-h{font-size:26px}
 #numeros ul.zn-b li{grid-template-columns:1fr;gap:2px;font-size:15px}
 #numeros .zn-k{grid-template-columns:1fr 1fr}
 #numeros .zn-k strong{font-size:22px}
}
</style>'''

CHEV = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>'

HTML = '''<section id="numeros"><div class="zn-w">
<span class="zn-eb">Los números</span>
<h2 class="zn-t">Todo esto, muy bonito.<b>Pero vamos con los números.</b></h2>
<p class="zn-sub">Dos tiendas que hemos abierto este mes. Tocad una para ver cómo fue.</p>
<div class="zn-cases" id="zncases">
<button class="zn-case" type="button" aria-expanded="false" aria-controls="zndr" data-c="kol"><img class="zn-bg" src="/casos/kol-sq.webp" alt="" loading="lazy" decoding="async"><span class="zn-in"><img class="zn-logo k" src="/casos/kol-logo-w.png" alt="Kiss of Life"><span class="zn-what">Boutique de moda · Oviedo y Gijón</span></span><span class="zn-more">Ver el caso ''' + CHEV + '''</span></button>
<button class="zn-case" type="button" aria-expanded="false" aria-controls="zndr" data-c="int"><img class="zn-bg" src="/casos/int-sq.webp" alt="" loading="lazy" decoding="async"><span class="zn-in"><img class="zn-logo i" src="/casos/int-logo-w.svg" alt="Intenso Fragancias"><span class="zn-what">Perfumería · Torremolinos</span></span><span class="zn-more">Ver el caso ''' + CHEV + '''</span></button>
</div>
<div class="zn-dr" id="zndr" aria-live="polite"><div>
<article class="zn-st" data-s="kol" hidden>
<div class="zn-shot"><div class="zn-ph"><img src="/casos/kol-movil.webp" alt="La tienda de Kiss of Life en el móvil" loading="lazy" decoding="async"></div></div>
<div class="zn-tx"><span class="zn-who">Kiss of Life · moda</span>
<h3 class="zn-h">Lo intentaron tres veces. <span>La cuarta, con lanzamientos.</span></h3>
<ul class="zn-b">
<li><b>Antes</b><span>Lo que entraba en tienda se agotaba en días. Ya habían probado a vender online tres veces y no funcionó: nadie podía actualizar una web a diario.</span></li>
<li><b>Qué hicimos</b><span>Una tienda a medida con lanzamientos cada martes y viernes a las 20:00, lista de espera para lo agotado y los básicos siempre a la venta. Ellas suben las prendas el lunes; el resto lo llevamos nosotros.</span></li>
<li><b>Ahora</b><span>Dos lanzamientos por semana y envíos a toda España. El primer mes, 4.237 € facturados online.</span></li>
</ul>
<div class="zn-k"><div><strong>40.700</strong><span>seguidores en Instagram</span></div><div><strong>2</strong><span>lanzamientos por semana</span></div><div><strong>15 días</strong><span>para tener la tienda lista</span></div><div class="hl"><strong>4.237 €</strong><span>facturados el primer mes</span></div></div>
</div></article>
<article class="zn-st" data-s="int" hidden>
<div class="zn-shot"><div class="zn-ph"><img src="/casos/int-perfume.webp" alt="Un perfume de la tienda de Intenso" loading="lazy" decoding="async"></div></div>
<div class="zn-tx"><span class="zn-who">Intenso Fragancias · perfumería</span>
<h3 class="zn-h">468 perfumes. <span>En Instagram no cabían.</span></h3>
<ul class="zn-b">
<li><b>Antes</b><span>Una perfumería en Torremolinos con cientos de fragancias por número. En redes solo se veía una parte, y para comprar había que ir a la tienda o escribir.</span></li>
<li><b>Qué hicimos</b><span>Su tienda con los 468 perfumes, fotos de todos hechas con IA y un buscador por perfume favorito, nota o número. Envío en 72 horas y dos decants de regalo en cada pedido.</span></li>
<li><b>Ahora</b><span>Vende a toda la Península, también cuando la tienda está cerrada. El primer mes, 6.291 € facturados online.</span></li>
</ul>
<div class="zn-k"><div><strong>468</strong><span>perfumes a la venta</span></div><div><strong>72 h</strong><span>de envío en la Península</span></div><div><strong>6.070</strong><span>seguidores en Instagram</span></div><div class="hl"><strong>6.291 €</strong><span>facturados el primer mes</span></div></div>
</div></article>
</div></div>
<a class="zn-cta" href="#agenda" data-ag="1">Hacemos la vuestra en 30 min</a>
</div></section>
'''

JS = r'''<script>
/* «Los números»: tocar un caso lo despliega; tocarlo otra vez lo recoge; tocar el otro cambia. */
(function(){var d=document,cs=d.getElementById('zncases'),dr=d.getElementById('zndr');if(!cs||!dr)return;
 var open=null,t=null;
 function show(c){
  cs.querySelectorAll('.zn-case').forEach(function(b){b.setAttribute('aria-expanded',b.getAttribute('data-c')===c?'true':'false')});
  cs.classList.toggle('on',!!c);clearTimeout(t);
  if(!c){try{if(window.__c404ev&&open)window.__c404ev('col',{l:'Caso '+open,s:'numeros'})}catch(e){}dr.classList.remove('open');t=setTimeout(function(){dr.querySelectorAll('[data-s]').forEach(function(s){s.hidden=true})},450);open=null;return}
  var sw=open&&open!==c;
  function rv(){dr.querySelectorAll('[data-s]').forEach(function(s){s.hidden=s.getAttribute('data-s')!==c});requestAnimationFrame(function(){dr.classList.add('open')})}
  if(sw){dr.classList.remove('open');t=setTimeout(rv,300)}else rv();
  open=c;
  try{if(window.__c404ev)window.__c404ev('exp',{l:'Caso '+c,s:'numeros'})}catch(e){}
 }
 cs.querySelectorAll('.zn-case').forEach(function(b){b.addEventListener('click',function(){var c=b.getAttribute('data-c');show(open===c?null:c)})});
})();
</script>'''
