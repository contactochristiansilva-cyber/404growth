# Propuesta v42 (21/11/2026): la de gen33v.py + lo que pidió Chris para cerrar esta semana.
#   - portada: «Esto no es una web. Es la tienda de X.» (contesta el «ya tenemos web» antes de que lo digan)
#   - «Así os llega un pedido»: simulación automática en un móvil, sin campos ni datos (anuncio → talla → pago → aviso)
#   - si tienen web: «Vuestra web sirve para que os conozcan. Esta, para que os compren.» (en lugar del diagnóstico)
#   - a mitad de página, el VSL («¿No me conocéis…?») y justo debajo la agenda
#   - la garantía del vídeo, en grande: vendéis online el triple de lo que cuesta la tienda o trabajamos gratis hasta conseguirlo
#   - textos de la vista previa de WhatsApp nuevos
# Parte de la propuesta ya hecha con gen33v.py (out/p-<slug>.html) y escribe la nueva en <salida>.
# python3 gen42.py <slug> [--out out42] [--vsl /v/propuesta/index.m3u8] [--poster /v/propuesta/poster.jpg] [--hls /v/hls.light.min.js]
import sys, os, re, json, html, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser()
ap.add_argument('slugs', nargs='+')
ap.add_argument('--src', default=os.path.join(HERE, 'out'))
ap.add_argument('--out', default=os.path.join(HERE, 'out42'))
ap.add_argument('--vsl', default='/v/propuesta/index.m3u8')
ap.add_argument('--poster', default='/v/propuesta/poster.jpg')
ap.add_argument('--hls', default='/v/hls.light.min.js')
ap.add_argument('--lq', default=os.path.join(HERE, '..', '..', 'tools', 'book', 'lq.b64'))
A = ap.parse_args()
P42 = {}
try: P42 = json.load(open(os.path.join(HERE, 'prop42.json'), encoding='utf-8'))
except FileNotFoundError: pass
LQ = open(A.lq).read().strip()
E = html.escape

# por nicho: precio de la simulación (es un ejemplo, la propuesta lo dice), qué elige la clienta y la palabra
NICHE = {
    'moda':        dict(price='49,90', opts=['XS', 'S', 'M', 'L'], pick=2, what='talla', items='prendas', it='prenda'),
    'sneakers':    dict(price='79,90', opts=['37', '38', '39', '40'], pick=2, what='número', items='zapatos', it='par'),
    'joya':        dict(price='39,00', opts=['Plata', 'Oro'], pick=1, what='acabado', items='piezas', it='pieza'),
    'cosmetica':   dict(price='34,90', opts=['50 ml', '100 ml'], pick=1, what='tamaño', items='productos', it='producto'),
    'suplementos': dict(price='29,90', opts=['Fresa', 'Vainilla', 'Cacao'], pick=2, what='sabor', items='productos', it='producto'),
}
NICHE['optica'] = dict(NICHE['joya'], opts=['Negro', 'Carey'], pick=1, what='color')

def fill(t, **k):
    for a, b in k.items(): t = t.replace('{' + a + '}', b)
    return t

CSS = r'''<style id="z42">
/* v42 · portada */
.hero h1{font-size:clamp(40px,6.4vw,84px)}
.hero .lede p b{color:var(--ink);font-weight:600}
.z4-chap{display:flex;align-items:center;gap:16px;margin-bottom:28px;justify-content:center}
.z4-chap .num{font-family:var(--m);font-size:12px;color:var(--t);border:1px solid currentColor;padding:4px 9px;border-radius:4px}
.z4-chap .lb{font-family:var(--m);font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--mute)}
.z4-h{text-align:center;max-width:820px;margin:0 auto}.z4-h h2{text-wrap:balance}
.z4-h p{font-size:20px;line-height:1.42;color:var(--mute);margin:22px auto 0;max-width:620px;letter-spacing:-.015em}
.z4-h p b{color:var(--ink);font-weight:600}
/* v42 · así os llega un pedido */
#pedido{background:var(--cream);overflow:hidden}
.z4-sim{display:grid;grid-template-columns:1fr 330px;gap:72px;align-items:center;max-width:960px;margin:64px auto 0}
.z4-steps{list-style:none;margin:0;padding:0;display:grid;gap:10px}
.z4-steps li{display:grid;grid-template-columns:44px 1fr;gap:16px;align-items:center;padding:16px 18px;border-radius:18px;background:rgba(255,255,255,.55);opacity:.45;transform:scale(.985);transition:opacity .35s,transform .35s,background .35s}
.z4-steps li.on{opacity:1;transform:none;background:#fff;box-shadow:0 14px 34px rgba(20,17,16,.07)}
.z4-steps li.ok{opacity:.8}
.z4-steps i{font-style:normal;width:44px;height:44px;border-radius:50%;display:grid;place-items:center;font-family:var(--m);font-size:13px;color:var(--t);box-shadow:inset 0 0 0 1.5px var(--t)}
.z4-steps li.on i{background:var(--t);color:#fff;box-shadow:none}
.z4-steps b{display:block;font-size:18px;letter-spacing:-.02em}
.z4-steps span{display:block;color:var(--mute);font-size:15px;margin-top:2px}
.z4-note{margin:22px 0 0;font-size:13.5px;color:var(--mute);display:flex;gap:8px;align-items:center}
.z4-note:before{content:"";width:8px;height:8px;border-radius:50%;background:#4BA36B;flex:none}
.z4-ph{position:relative;width:330px;justify-self:center}
.z4-who{position:absolute;left:0;right:0;top:-38px;text-align:center;font-family:var(--m);font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--mute)}
.z4-who span{position:absolute;left:0;right:0;transition:opacity .4s}
.z4-who .b{opacity:0}.z4-sim[data-s="4"] .z4-who .a{opacity:0}.z4-sim[data-s="4"] .z4-who .b{opacity:1}
.z4-dev{position:relative;width:330px;height:676px;border-radius:52px;background:#111;padding:11px;box-shadow:0 40px 80px -30px rgba(20,17,16,.45),inset 0 0 0 2px #2a2624}
.z4-scr{position:relative;width:100%;height:100%;border-radius:42px;overflow:hidden;background:#fff;isolation:isolate}
.z4-scr:after{content:"";position:absolute;left:50%;top:10px;width:96px;height:28px;border-radius:20px;background:#000;transform:translateX(-50%);z-index:20}
.z4-v{position:absolute;inset:0;opacity:0;transition:opacity .45s;display:flex;flex-direction:column;font-size:13px;color:#141110}
.z4-sim[data-s="0"] .v0,.z4-sim[data-s="1"] .v1,.z4-sim[data-s="2"] .v1,.z4-sim[data-s="3"] .v1,.z4-sim[data-s="4"] .v4{opacity:1}
.z4-sb{height:50px;flex:none;display:flex;justify-content:space-between;align-items:flex-end;padding:0 30px 6px;font-weight:600;font-size:14px}
/* 0: el anuncio */
.v0 .ig{display:flex;align-items:center;gap:10px;padding:10px 14px}
.v0 .av{width:32px;height:32px;border-radius:50%;background:var(--t);color:#fff;display:grid;place-items:center;font-weight:700;font-size:14px}
.v0 .ig b{display:block;font-size:13px}.v0 .ig small{color:#8a8582;font-size:11px}
.v0 .im{aspect-ratio:4/5;background:#eee center/cover}
.v0 .bt{display:flex;justify-content:space-between;align-items:center;padding:12px 14px;border-bottom:1px solid #eee;font-weight:600;color:var(--t)}
.v0 .cp{padding:10px 14px;line-height:1.35}.v0 .cp b{font-weight:600}
/* 1–3: la ficha */
.v1 .im{height:300px;flex:none;background:#eee center/cover}
.v1 .pd{padding:16px 18px 0}
.v1 .pd .n{font-size:19px;font-weight:600;letter-spacing:-.02em}
.v1 .pd .pr{margin-top:4px;color:#6e6764}
.v1 .lb{margin:16px 0 8px;font-size:12px;color:#6e6764}
.v1 .op{display:flex;gap:8px}
.v1 .op span{flex:1;text-align:center;padding:9px 0;border-radius:10px;box-shadow:inset 0 0 0 1px #ddd;font-weight:500;transition:background .25s,color .25s,box-shadow .25s}
.z4-sim[data-s="2"] .v1 .op .pk,.z4-sim[data-s="3"] .v1 .op .pk{background:#141110;color:#fff;box-shadow:none}
.v1 .z4a{text-transform:none;letter-spacing:-.01em;font-size:14px;margin:16px 0 0;padding:14px;border-radius:99px;background:var(--t);color:#fff;text-align:center;font-weight:600}
.z4-sh{position:absolute;left:0;right:0;bottom:0;background:#fff;border-radius:26px 26px 0 0;padding:14px 20px 26px;box-shadow:0 -16px 50px rgba(0,0,0,.18);transform:translateY(105%);transition:transform .5s cubic-bezier(.2,.8,.2,1);z-index:5}
.z4-sim[data-s="3"] .z4-sh{transform:none}
.z4-sh .gr{width:38px;height:5px;border-radius:3px;background:#ddd;margin:0 auto 14px}
.z4-sh .z4r{display:flex;justify-content:space-between;align-items:baseline;padding:7px 0;border-bottom:1px solid #f0ecea;font-size:13px}.z4-sh .z4r b{font-size:13.5px}
.z4-sh .z4r span{color:#6e6764}.z4-sh .tt{font-weight:600;border:0}.z4-sh .tt b{font-size:16px}
.z4-sh .pm{display:flex;gap:6px;margin:12px 0}.z4-sh .pm span{flex:1;text-align:center;font-size:11px;padding:7px 0;border-radius:8px;background:#f4f1ef;color:#6e6764}
.z4-sh .pay{position:relative;padding:14px;border-radius:99px;background:#141110;color:#fff;text-align:center;font-weight:600;overflow:hidden}
.z4-sh .pay .k{position:absolute;inset:0;display:grid;place-items:center;background:#2E7A4F;opacity:0;transition:opacity .3s}
.z4-sim.paid .z4-sh .pay .k{opacity:1}
/* 4: vuestro móvil */
.v4{background:linear-gradient(170deg,#3b302b,#151110 70%);color:#fff;align-items:center}
.v4 .dt{margin-top:64px;font-size:15px;opacity:.8}
.v4 .hr{font-size:78px;font-weight:600;letter-spacing:-.03em;line-height:1;margin-top:2px}
.v4 .nt{position:absolute;left:12px;right:12px;top:200px;display:grid;grid-template-columns:38px 1fr;gap:10px;padding:12px;border-radius:20px;background:rgba(255,255,255,.17);transform:translateY(-14px) scale(.96);opacity:0;transition:transform .55s cubic-bezier(.2,.9,.25,1.2),opacity .35s}
.z4-sim[data-s="4"] .v4 .nt{transform:none;opacity:1;transition-delay:.55s}
.v4 .nt .ap{width:38px;height:38px;border-radius:10px;background:var(--t);display:grid;place-items:center;font-weight:700;font-size:16px}
.v4 .nt b{display:flex;justify-content:space-between;font-size:13.5px}.v4 .nt b small{font-weight:400;opacity:.65}
.v4 .nt p{margin:2px 0 0;font-size:13px;line-height:1.3;color:#fff;opacity:.92}
.v4 .n2{top:280px;transition-delay:0s}.z4-sim[data-s="4"] .v4 .n2{opacity:.55;transition-delay:1.6s}
/* el dedo */
.z4-tap{position:absolute;left:0;top:0;width:46px;height:46px;margin:-23px 0 0 -23px;border-radius:50%;background:rgba(20,17,16,.22);box-shadow:0 0 0 2px rgba(255,255,255,.7);opacity:0;z-index:30;pointer-events:none;transform:translate(var(--x,0),var(--y,0)) scale(.6);transition:transform .5s cubic-bezier(.3,.7,.2,1),opacity .2s}
.z4-tap.on{opacity:1;transform:translate(var(--x,0),var(--y,0)) scale(1)}
.z4-tap.pr{transform:translate(var(--x,0),var(--y,0)) scale(.78);transition-duration:.12s}
.z4-lab{display:inline-flex;align-items:center;gap:8px;margin:0 auto;padding:7px 14px;border-radius:99px;background:#fff;font-size:13px;color:var(--mute);box-shadow:inset 0 0 0 1px var(--line)}
.z4-lw{text-align:center;margin-top:26px}
/* v42 · vuestra web y esta tienda */
.z4-cmp{max-width:900px;margin:56px auto 0;border-radius:26px;overflow:hidden;background:#fff;box-shadow:0 0 0 1px var(--line)}
.z4-cmp .rw{display:grid;grid-template-columns:1.05fr 1fr 1fr;border-top:1px solid var(--line)}
.z4-cmp .rw:first-child{border-top:0}
.z4-cmp .rw>div{padding:20px 24px;font-size:16.5px;line-height:1.35}
.z4-cmp .hd>div{font-family:var(--m);font-size:11.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--mute);padding-top:18px;padding-bottom:16px}
.z4-cmp .k{font-weight:600}
.z4-cmp .a{color:var(--mute)}
.z4-cmp .b{background:color-mix(in srgb,var(--t) 7%,#fff);font-weight:500}
.z4-cmp .hd .b{color:var(--t)}
.z4-cmp .b:before{content:"✓";color:var(--t);font-weight:700;margin-right:8px}
.z4-cmp .hd .b:before{content:none}
.z4-src{max-width:900px;margin:16px auto 0;font-size:13.5px;color:var(--mute);text-align:center}
/* v42 · el vídeo */
#video{background:#fff}
.z4-vd{max-width:900px;margin:52px auto 0;padding:10px;border-radius:30px;background:#141110;box-shadow:0 40px 90px -40px rgba(20,17,16,.6)}
.z4-scn{position:relative;aspect-ratio:16/9;border-radius:21px;overflow:hidden;background:#000}
.z4-scn .vlq{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:blur(16px);transform:scale(1.14)}
.z4-scn .vlq.ok{filter:none;transform:none}
.z4-scn video{position:relative;width:100%;height:100%;display:block;object-fit:cover;background:transparent;opacity:0;transition:opacity .45s}
.z4-scn.vp video{opacity:1}
.z4-scn.aud video{object-fit:contain}
.z4-go{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);z-index:3;display:inline-flex;align-items:center;gap:13px;border:0;cursor:pointer;font-family:inherit;font-size:17px;font-weight:600;letter-spacing:-.012em;color:#141110;background:#fff;padding:10px 24px 10px 10px;border-radius:99px;white-space:nowrap;box-shadow:0 12px 44px rgba(0,0,0,.4);transition:transform .25s cubic-bezier(.2,.8,.2,1)}
.z4-go i{width:46px;height:46px;border-radius:50%;background:#141110;display:grid;place-items:center;flex:none}
.z4-go svg{width:18px;height:18px;color:#fff;margin-left:3px}
@media (hover:hover){.z4-go:hover{transform:translate(-50%,-50%) scale(1.045)}}.z4-go:active{transform:translate(-50%,-50%) scale(.97)}
.z4-scn.aud .z4-go{display:none}
.z4-vm{display:flex;justify-content:center;gap:22px;flex-wrap:wrap;margin-top:22px;font-size:14px;color:var(--mute)}
.z4-vm span:before{content:"·";margin-right:22px;color:var(--line)}.z4-vm span:first-child:before{content:none}
#video+.z4-ag,#video .ag{margin-top:0}
/* v42 · la garantía */
#garantia{background:var(--ink);color:#fff;text-align:center;overflow:hidden;position:relative}
#garantia:before{content:"";position:absolute;left:50%;top:-10%;width:900px;height:620px;transform:translateX(-50%);border-radius:50%;background:radial-gradient(closest-side,color-mix(in srgb,var(--t) 42%,transparent),transparent);opacity:.55;pointer-events:none}
#garantia .wrap{position:relative}
#garantia .z4-chap .lb{color:var(--mute2)}
.z4-x3{font-size:clamp(130px,22vw,280px);font-weight:700;letter-spacing:-.07em;line-height:.85;margin:6px 0 26px}
.z4-x3 small{font-size:.42em;font-weight:300;letter-spacing:-.03em;vertical-align:.62em;margin-right:.04em;color:var(--mute2)}
#garantia h2{max-width:880px;margin:0 auto}
#garantia h2 span{display:block;color:var(--mute2);font-weight:400}
.z4-g3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;max-width:900px;margin:56px auto 0;text-align:left}
.z4-g3 div{padding:22px 24px;border-radius:20px;background:rgba(255,255,255,.06);box-shadow:inset 0 0 0 1px rgba(255,255,255,.08)}
.z4-g3 b{display:block;font-size:18px;letter-spacing:-.02em}
.z4-g3 p{margin:6px 0 0;font-size:15px;line-height:1.4;color:var(--mute2)}
#garantia .btns{margin-top:44px}
#garantia .cta.ghost{background:transparent;color:#fff;box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.5)}
@media (max-width:860px){
 .z4-sim{grid-template-columns:1fr;gap:56px;margin-top:44px}
 .z4-ph{order:-1;transform:scale(.92);transform-origin:top center;margin-bottom:-54px}
 .z4-steps li{padding:12px 14px;grid-template-columns:36px 1fr;gap:12px}.z4-steps i{width:36px;height:36px}
 .z4-steps b{font-size:16.5px}.z4-steps span{font-size:14px}
 .z4-cmp .rw{grid-template-columns:1fr 1fr}
 .z4-cmp .rw>.k{grid-column:1/-1;padding:16px 18px 2px;border:0}
 .z4-cmp .rw>div{padding:8px 18px 16px;font-size:15px}
 .z4-cmp .hd{display:none}
 .z4-cmp .a:before{content:attr(data-l);display:block;font-family:var(--m);font-size:10.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--mute2);margin-bottom:4px}
 .z4-cmp .b{background:none}
 .z4-cmp .b:before{content:attr(data-l);display:block;font-family:var(--m);font-size:10.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--t);margin:0 0 4px;font-weight:400}
 .z4-g3{grid-template-columns:1fr}
 .z4-vd{padding:6px;border-radius:22px}.z4-scn{border-radius:17px}
 .z4-go{font-size:15px;gap:10px;padding:8px 18px 8px 8px}.z4-go i{width:38px;height:38px}.z4-go svg{width:15px;height:15px}
 .z4-h p{font-size:17.5px}
 .z4-h h2 br,#garantia h2 br{display:none}
 #video .ag{padding-left:0;padding-right:0}
}
@media (prefers-reduced-motion:reduce){.z4-v,.z4-steps li,.z4-sh,.v4 .nt,.z4-tap,.z4-scn video{transition:none!important}}
</style>'''

SIM = '''<section class="sec" id="pedido"><div class="wrap">
<div class="z4-chap"><span class="num">02</span><span class="lb">Un pedido</span></div>
<div class="z4-h"><h2>Así os llega<br><span class="t">un pedido.</span></h2>
<p>Una clienta de {cityto} ve vuestro anuncio a las 23:47. La tienda lleva horas cerrada. <b>Mirad lo que pasa:</b></p></div>
<div class="z4-sim" data-s="0" id="z4sim">
<div><ol class="z4-steps">
<li class="on"><i>1</i><div><b>Ve vuestro anuncio</b><span>En Instagram, a las 23:47.</span></div></li>
<li><i>2</i><div><b>Elige su {what}</b><span>En la ficha, sin escribir a nadie.</span></div></li>
<li><i>3</i><div><b>Paga en un toque</b><span>Tarjeta, Bizum o Apple Pay.</span></div></li>
<li><i>4</i><div><b>Os llega el pedido</b><span>Pagado. Mañana lo preparáis.</span></div></li>
</ol>
<p class="z4-note">Simulación: aquí no se paga nada ni se pide ningún dato.</p></div>
<div class="z4-ph"><div class="z4-who"><span class="a">El móvil de la clienta</span><span class="b">Vuestro móvil</span></div>
<div class="z4-dev"><div class="z4-scr">
<div class="z4-v v0"><div class="z4-sb"><span>23:47</span><span>●●●</span></div>
<div class="ig"><span class="av">{ini}</span><div><b>{ig}</b><small>Publicidad</small></div></div>
<div class="im" style="background-image:url('{img}')"></div>
<div class="bt"><span>Comprar ahora</span><span>›</span></div>
<div class="cp"><b>{ig}</b> {prod}. Envío a toda España.</div></div>
<div class="z4-v v1"><div class="z4-sb"><span>23:47</span><span>●●●</span></div>
<div class="im" style="background-image:url('{img}')"></div>
<div class="pd"><div class="n">{prod}</div><div class="pr">{price}&nbsp;€ · envío a toda España</div>
<div class="lb">Elige {what}</div><div class="op">{opts}</div>
<div class="z4a">Añadir y pagar</div></div>
<div class="z4-sh"><div class="gr"></div><div class="z4r"><span>{prod} · {optpick}</span><b>{price}&nbsp;€</b></div>
<div class="z4r"><span>Envío</span><b>Gratis</b></div><div class="z4r tt"><span>Total</span><b>{price}&nbsp;€</b></div>
<div class="pm"><span>Tarjeta</span><span>Bizum</span><span>Apple Pay</span></div>
<div class="pay">Pagar {price}&nbsp;€<span class="k">✓ Pagado</span></div></div></div>
<div class="z4-v v4"><div class="dt">martes</div><div class="hr">23:48</div>
<div class="nt"><span class="ap">{ini}</span><div><b>🛍️ Nuevo pedido · {price}&nbsp;€ <small>ahora</small></b><p>{prod} · {optpick} · {cityto}</p></div></div>
<div class="nt n2"><span class="ap">{ini}</span><div><b>{name} <small>hace 2 h</small></b><p>Pedido enviado a Bilbao</p></div></div></div>
<i class="z4-tap" id="z4tap"></i>
</div></div></div></div>
<div class="z4-lw"><span class="z4-lab">Precio de ejemplo · en vuestra tienda, los vuestros</span></div>
</div></section>'''

SIM_JS = r'''<script>
/* v42: «Así os llega un pedido» se mueve solo mientras se ve (solo transform y opacity) */
(function(){var s=document.getElementById('z4sim');if(!s)return;var tap=document.getElementById('z4tap'),li=s.querySelectorAll('.z4-steps li'),T=[],run=false,
 calm=window.matchMedia&&matchMedia('(prefers-reduced-motion:reduce)').matches;
 function st(n){s.setAttribute('data-s',n);var k=[0,1,1,2,3][n];
  li.forEach(function(l,i){l.className=i===k?'on':i<k?'ok':''})}
 function at(ms,f){T.push(setTimeout(f,ms))}
 function finger(x,y){tap.style.setProperty('--x',x+'px');tap.style.setProperty('--y',y+'px');tap.classList.add('on')}
 function press(){tap.classList.add('pr');setTimeout(function(){tap.classList.remove('pr')},140)}
 function loop(){T.forEach(clearTimeout);T=[];s.classList.remove('paid');tap.className='z4-tap';st(0);
  var bt=s.querySelector('.v0 .bt'),sc=s.querySelector('.z4-scr'),r=function(el){var a=el.getBoundingClientRect(),b=sc.getBoundingClientRect(),k=b.width/308;return[(a.left-b.left+a.width/2)/k,(a.top-b.top+a.height/2)/k]};
  at(1400,function(){var p=r(bt);finger(p[0],p[1])});at(2300,press);at(2500,function(){st(1)});
  at(3300,function(){var p=r(s.querySelector('.v1 .op .pk'));finger(p[0],p[1])});at(4100,press);at(4250,function(){st(2)});
  at(5000,function(){var p=r(s.querySelector('.v1 .z4a'));finger(p[0],p[1])});at(5800,press);at(5950,function(){st(3)});
  at(6900,function(){var p=r(s.querySelector('.z4-sh .pay'));finger(p[0],p[1])});at(7700,press);at(7800,function(){s.classList.add('paid')});
  at(8500,function(){tap.classList.remove('on')});at(9300,function(){st(4)});at(15000,loop)}
 if(calm){st(4);return}
 if('IntersectionObserver' in window)new IntersectionObserver(function(e){if(e[0].isIntersecting){if(!run){run=true;loop()}}else{run=false;T.forEach(clearTimeout);T=[]}},{threshold:.35}).observe(s);else loop();
})();
</script>'''

CMP = '''<section class="sec" id="web" style="background:#fff"><div class="wrap">
<div class="z4-chap"><span class="num">03</span><span class="lb">Ya tenéis web</span></div>
<div class="z4-h"><h2>Vuestra web sirve para que os conozcan. <br><span class="t">Esta, para que os compren.</span></h2></div>
<div class="z4-cmp"><div class="rw hd"><div></div><div class="a">{domain}, hoy</div><div class="b">Vuestra tienda</div></div>
{rows}</div>
<p class="z4-src">{src}</p>
</div></section>'''

VID = '''<section class="sec" id="video"><div class="wrap">
<div class="z4-chap"><span class="num">{n}</span><span class="lb">Si no me conocéis</span></div>
<div class="z4-h"><h2>¿Os preguntáis quién soy <br><span class="t">y por qué os he hecho esto?</span></h2>
<p>Son 3 minutos y os lo explico todo. <b>Ponedlo con sonido.</b></p></div>
<div class="z4-vd"><div class="z4-scn" id="z4scn">
<img class="vlq" id="z4lq" alt="" aria-hidden="true" src="data:image/jpeg;base64,{lq}">
<video id="z4v" muted loop playsinline autoplay preload="metadata" aria-label="Vídeo de Christian · 404 Growth"></video>
<button class="z4-go" id="z4go" type="button"><i aria-hidden="true"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M7 4.5v15l13-7.5z"/></svg></i>Reproducir con audio</button>
</div></div>
<div class="z4-vm"><span>Christian · 404 Growth</span><span>3 min</span><span>Debajo, eliges hora para hablarlo</span></div>
{agenda}</div></section>'''

VID_JS = r'''<script>
/* v42: el vídeo. Sin sonido y en bucle mientras se ve; «Reproducir con audio» vuelve al segundo 0 y suena.
   Lo que se ve con audio lo cuenta el contador (vplay, vprog 25/50/75, vend), igual que en /book. */
(function(){var VSL={src:'{src}',poster:'{poster}',hls:'{hls}'};var d=document,sc=d.getElementById('z4scn');if(!sc)return;
 var v=d.getElementById('z4v'),go=d.getElementById('z4go'),lq=d.getElementById('z4lq'),aud=false,on=false,want=false;
 var calm=(window.matchMedia&&matchMedia('(prefers-reduced-motion:reduce)').matches)||!!(navigator.connection&&navigator.connection.saveData);
 function sharp(){var i=new Image();i.onload=function(){lq.src=VSL.poster;lq.classList.add('ok')};i.src=VSL.poster}
 function play(){var p=v.play();if(p&&p.catch)p.catch(function(){if(!aud)sharp()})}
 function attach(){if(on)return;on=true;
  if(/\.m3u8(\?|$)/.test(VSL.src)&&!v.canPlayType('application/vnd.apple.mpegurl')){var s=d.createElement('script');s.src=VSL.hls;
   s.onload=function(){if(window.Hls&&Hls.isSupported()){var h=new Hls({abrEwmaDefaultEstimate:1e6});h.loadSource(VSL.src);h.attachMedia(v)}else v.src=VSL.src;if(aud||want)play()};
   s.onerror=sharp;d.head.appendChild(s)}else{v.src=VSL.src;if(aud||want)play()}}
 v.addEventListener('timeupdate',function(){if(v.currentTime>.05)sc.classList.add('vp')});
 if(calm)sharp();else if('IntersectionObserver' in window)new IntersectionObserver(function(e){if(aud)return;if(e[0].isIntersecting){want=true;attach();play()}else{want=false;v.pause()}},{rootMargin:'200px 0px',threshold:.1}).observe(sc);
 go.addEventListener('click',function(){aud=true;sc.classList.add('aud');v.loop=false;v.muted=false;v.removeAttribute('autoplay');v.autoplay=false;v.volume=1;v.controls=true;
  attach();try{v.currentTime=0}catch(e){}play()});
 v.addEventListener('ended',function(){aud=false;v.controls=false;sc.classList.remove('aud')});
})();
</script>'''

GAR = '''<section class="sec" id="garantia"><div class="wrap">
<div class="z4-chap"><span class="num">{n}</span><span class="lb">La garantía</span></div>
<div class="z4-x3"><small>×</small>3</div>
<h2>Vendéis online el triple de lo que os cuesta la tienda.<span>O trabajamos gratis hasta conseguirlo.</span></h2>
<div class="z4-g3">
<div><b>Por contrato</b><p>Va por escrito, firmado por los dos antes de empezar.</p></div>
<div><b>Con vuestras ventas</b><p>Se cuenta con lo que vendáis en la tienda online, no con estimaciones.</p></div>
<div><b>Sin cobrar de más</b><p>Si no llega, seguimos trabajando gratis hasta que llegue.</p></div>
</div>
<div class="btns"><a class="cta" href="#agenda" data-ag="1">Os lo explico en 30 min<span>→</span></a><a class="cta ghost" href="{wa}" target="_blank" rel="noopener">Preguntarme por WhatsApp</a></div>
</div></section>'''


def build(slug):
    src = os.path.join(A.src, f'p-{slug}.html')
    h = open(src, encoding='utf-8').read()
    d = json.load(open(os.path.join(HERE, 'data', f'{slug}.json'), encoding='utf-8'))
    o = P42.get(slug, {})
    niche = d.get('niche', 'moda'); N = dict(NICHE.get(niche, NICHE['moda'])); N.update(o.get('niche', {}))
    name, ig, city = d['name'], d.get('ig', ''), d.get('city', '')
    cityto = o.get('cityto') or ('Bilbao' if city in ('Valladolid',) else 'Valladolid')
    pr = d['prods'][0]; prod = o.get('prod', pr['name'])
    wa = re.search(r'https://wa\.me/[^"]+', h).group(0)
    n = 0
    def rep(a, b, cnt=1):
        nonlocal h; assert h.count(a) == cnt, (slug, a[:70], h.count(a)); h = h.replace(a, b)

    # cabeza: título y vista previa de WhatsApp
    h = re.sub(r'<title>[^<]*</title>', f'<title>{E(name)} · vuestra tienda ya puede cobrar</title>', h, count=1)
    h = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{E(name)}, vuestra tienda ya puede cobrar">', h, count=1)
    h = re.sub(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="No es una web: aquí eligen, pagan y os llega el pedido. Os la he preparado con vuestras ' + N['items'] + '.">', h, count=1)
    h = h.replace('</head>', CSS + '</head>', 1)

    # menú
    has_web = bool(d.get('domain'))
    lk = '<a href="#tienda">Tienda</a><a href="#pedido">Un pedido</a><a href="#video">Vídeo</a><a href="#garantia">Garantía</a>'
    h, k = re.subn(r'<div class="lk2">.*?</div>', '<div class="lk2">' + lk + '</div>', h, count=1, flags=re.S); assert k == 1

    # portada
    h, k = re.subn(r'<h1>.*?</h1>', f'<h1>Esto no es una web.<br><span class="t">Es la tienda de {E(name)}.</span></h1>', h, count=1, flags=re.S); assert k == 1
    lede = (f'<p>Con vuestras {N["items"]}, cesta y pago en un toque. Os la he montado para que no tengáis que imaginarla. '
            f'<b>Bajad: en un minuto veis cómo os llega un pedido.</b></p>')
    h, k = re.subn(r'(<div class="lede">)<p>.*?</p>', r'\1' + lede.replace('\\', '\\\\'), h, count=1, flags=re.S); assert k == 1
    h, k = re.subn(r'(<div class="lede">.*?<div class="btns">)<a class="cta" href="https://wa\.me/[^"]*"[^>]*>Quiero mi tienda<span>→</span></a>',
                   r'\1<a class="cta" href="#pedido">Ver cómo llega un pedido<span>↓</span></a>', h, count=1, flags=re.S); assert k == 1

    # la agenda sale de la tienda y va debajo del vídeo
    a = h.index('<!--ag-->'); b = h.index('<!--/ag-->') + len('<!--/ag-->')
    ag = h[a:b]; h = h[:a] + h[b:]
    rep('<a class="cta" href="#agenda" data-ag="1">Quiero esta tienda para', '<a class="cta" href="#pedido">Ver cómo os llega un pedido · ')
    h = h.replace('Ver cómo os llega un pedido · ' + E(name) + '<span>→</span>', 'Ver cómo os llega un pedido<span>↓</span>')

    # bloques nuevos, después de la tienda
    def esc(x): return E(x, quote=True)
    opts = ''.join(f'<span{" class=\"pk\"" if i == N["pick"] else ""}>{esc(x)}</span>' for i, x in enumerate(N['opts']))
    img = f'/p-{slug}--b--p1.jpg'
    sim = fill(SIM, cityto=esc(cityto), what=N['what'], ini=esc(name[:1].upper()), ig=esc(ig), img=img, prod=esc(prod),
               price=N['price'], opts=opts, optpick=esc((('Talla ' if N['what'] == 'talla' else '') + N['opts'][N['pick']])), name=esc(name))
    blocks = sim
    num = 3
    if has_web:
        rows = o.get('cmp') or [
            ['Comprar', 'Escribiros y esperar respuesta', 'Elegir, pagar y listo'],
            ['A las 3 de la mañana', 'Un mensaje sin leer', 'Un pedido pagado'],
            ['Vuestros anuncios', 'Llevan a ver, no a comprar', f'Llevan a la {N["it"]}, lista para pagar'],
            ['Qué anuncio vende', 'No se sabe', 'Cada venta, con su anuncio'],
        ]
        rr = ''.join(f'<div class="rw"><div class="k">{esc(k)}</div><div class="a" data-l="{esc(d["domain"])}">{esc(x)}</div><div class="b" data-l="Vuestra tienda">{esc(y)}</div></div>' for k, x, y in rows)
        blocks += fill(CMP, domain=esc(d['domain']), rows=rr, src=esc(o.get('cmp_src') or d.get('web_note') or ''))
        num = 4
        # el diagnóstico sobra: lo cuenta la comparación
        a = h.index('<section class="sec" id="diagnostico">'); b = h.index('</section>', a) + len('</section>')
        h = h[:a] + h[b:]
    else:
        h = h.replace('<span class="num">02</span><span class="lb">Diagnóstico</span>', '<span class="num">03</span><span class="lb">Diagnóstico</span>')
        num = 4
    blocks += fill(VID, n=f'{num:02d}', lq=LQ, agenda=ag)
    blocks += fill(GAR, n=f'{num + 1:02d}', wa=wa)
    a = h.index('<section class="sec shopsec" id="tienda">'); b = h.index('</section>', h.index('<div class="pts">', a)) + len('</section>')
    h = h[:b] + '\n' + blocks + h[b:]
    # numeración de lo que queda
    h = h.replace('<span class="num">03</span><span class="lb">Ideas de campaña</span>', f'<span class="num">{num + 2:02d}</span><span class="lb">Ideas de campaña</span>')
    h = h.replace('<span class="num">04</span><span class="lb">Plan</span>', f'<span class="num">{num + 3:02d}</span><span class="lb">Plan</span>')

    # cierre
    rep('<p>Soy Christian. Os enseño esta tienda en 30 minutos, con vuestro catálogo y en directo.</p>',
        '<p>Soy Christian. En 30 minutos os enseño la tienda en directo, con vuestro catálogo, y os explico la garantía. Sin compromiso.</p>')

    # contador: partes de la página
    h = re.sub(r'PARTS=\[\[.*?\]\]', 'PARTS=[["tienda", 2], ["pedido", 3], ["video", 5], ["garantia", 6], ["captacion", 7], ["plan", 8], ["hablar", 9]]', h, count=1)

    # scripts
    vj = VID_JS.replace('{src}', A.vsl).replace('{poster}', A.poster).replace('{hls}', A.hls)
    h = h.replace('</body>', SIM_JS + vj + '</body>', 1)
    os.makedirs(A.out, exist_ok=True)
    out = os.path.join(A.out, f'p-{slug}.html')
    open(out, 'w', encoding='utf-8').write(h)
    print(slug, len(h), out)

for s in A.slugs: build(s)
