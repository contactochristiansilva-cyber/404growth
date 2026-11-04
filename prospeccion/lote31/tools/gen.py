"""Lote 31 · propuesta de tienda online (formato del lote 30) con imágenes de Apimart.
uso: python3 gen.py <slug> [<slug> ...]   → escribe en ../out/: p-<slug>.html y p-<slug>--b--*.jpg (+ og)"""
import colorsys, html, json, os, re, sys, urllib.parse
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); L31 = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from niches import NICHE
from shops import SHOPS
P = json.load(open(os.path.join(L31, 'tpl/lola_parts.json')))
E = html.escape
OUT = os.path.join(L31, 'out')
BOOK = 'https://404growth.com/book?utm_source=propuesta&utm_medium=web&utm_campaign='
WA = 'https://wa.me/34610594450'


def wa(c):
    """WhatsApp de Christian con el mensaje ya escrito (lote 32)"""
    return WA + '?text=' + urllib.parse.quote(f'Hola Christian, he visto la propuesta de {c["name"]}. ')


# v32 (4/11/2026): menú en píldora oscura con su logo, letra SF Pro donde antes era monoespaciada, nota de Christian
# arriba y botón fijo de WhatsApp. Sin asistente ni CRM: solo tienda y anuncios.
V32 = ('<style id="v32">'
       ':root{--m:-apple-system,BlinkMacSystemFont,"SF Pro Text","SF Pro Display","Helvetica Neue",Inter,Arial,sans-serif}'
       '.mono,.chap .lb,.fun-h,.gl small,.fs small,.mk small,.src,footer,.fx .note{letter-spacing:.07em;font-weight:500}'
       'html.sk{padding:0!important;border:0!important}'
       '.nav{position:fixed;top:0;left:0;right:0;z-index:60;background:transparent!important;border:0!important;backdrop-filter:none!important;-webkit-backdrop-filter:none!important;padding:12px 16px 0;pointer-events:none}'
       '.hero{padding-top:156px!important}'
       '.nav .wrap{pointer-events:auto;width:max-content;max-width:100%;height:auto;margin:0 auto;display:flex;align-items:center;gap:4px;padding:7px 7px 7px 24px;border-radius:999px;'
       'background:rgba(58,58,58,.8);backdrop-filter:saturate(160%) blur(18px);-webkit-backdrop-filter:saturate(160%) blur(18px);box-shadow:0 12px 32px rgba(0,0,0,.18),inset 0 0 0 1px rgba(255,255,255,.08)}'
       '.nav .br{color:#fff!important;margin-right:14px;text-decoration:none;display:flex;align-items:center}'
       '.nav .br .wm{color:#fff!important}.nav .br img{height:26px;width:auto;max-width:150px;object-fit:contain;filter:brightness(0) invert(1)}.nav .br svg{height:30px;width:auto}'
       '.nav .lk2{display:flex;gap:2px;margin:0}'
       '.nav .lk2 a{font-family:var(--f);font-size:16px;font-weight:500;letter-spacing:-.01em;text-transform:none;color:#fff;padding:12px 16px;border-radius:999px;text-decoration:none;transition:background .2s}'
       '.nav .lk2 a:hover{background:rgba(255,255,255,.12)}'
       '.nav .cta{margin-left:8px!important;background:#fff!important;color:#111!important;border:0!important;border-radius:999px!important;padding:14px 26px!important;font-size:16px!important;font-weight:500;box-shadow:none!important}'
       '.nav .cta span{display:none}'
       '.hi{display:flex;align-items:center;gap:12px;width:max-content;max-width:100%;margin:0 auto 26px;padding:8px 20px 8px 8px;border-radius:999px;background:rgba(255,255,255,.78);'
       'box-shadow:inset 0 0 0 1px rgba(0,0,0,.05),0 10px 26px rgba(0,0,0,.06);text-align:left}'
       '.hi img{width:46px;height:46px;border-radius:50%;object-fit:cover;flex:none}.hi p{margin:0;max-width:470px;font-size:14.5px;line-height:1.38;color:var(--ink)}.hi b{display:inline;font-weight:600;font-size:inherit;letter-spacing:0;margin:0}'
       '.wa-fab{position:fixed;right:20px;bottom:20px;z-index:70;display:flex;align-items:center;gap:12px;padding:8px 22px 8px 8px;border-radius:999px;background:rgba(58,58,58,.88);'
       'backdrop-filter:saturate(160%) blur(16px);-webkit-backdrop-filter:saturate(160%) blur(16px);color:#fff;text-decoration:none;font:500 15.5px/1.2 var(--f);'
       'box-shadow:0 14px 34px rgba(0,0,0,.24),inset 0 0 0 1px rgba(255,255,255,.08);transform:translateY(140%);opacity:0;transition:transform .5s cubic-bezier(.2,.8,.2,1),opacity .4s}'
       '.wa-fab.on{transform:none;opacity:1}.wa-fab img{width:38px;height:38px;border-radius:50%;object-fit:cover}'
       '.wa-fab small{display:block;font-size:12px;font-weight:400;color:rgba(255,255,255,.7)}'
       '.fun{grid-template-columns:repeat(3,1fr)!important}'
       '@media (max-width:760px){.nav{padding:10px 12px 0}.hero{padding-top:116px!important}.nav .lk2{display:none}.nav .wrap{padding-left:18px}.nav .br img{height:22px;max-width:120px}'
       '.nav .cta{padding:12px 20px!important;font-size:15px!important}.hi{border-radius:20px;padding:10px 14px 10px 10px}.hi p{font-size:13.5px}'
       '.wa-fab{left:12px;right:12px;bottom:12px;justify-content:center;padding-right:16px}.fun{grid-template-columns:1fr!important}}'
       '</style>')
# v33 (4/11/2026): página más corta. Primer pantallazo con poco texto y la tienda a la vista: el portátil y el móvil
# recorren solos su tienda (TOUR_JS). Fuera «antes y después», «mercado», «lo que cambia» y el embudo; los anuncios son «ideas de campaña».
V33 = ('<style id="v33">'
       # hero
       '.hero{padding-top:122px!important}'
       '.hero .hi{gap:10px;padding:5px 18px 5px 5px;margin:0 auto 24px}.hero .hi img{width:32px;height:32px}'
       '.hero .hi span{font-size:14px;line-height:1.2;color:var(--ink);letter-spacing:-.005em}.hero .hi b{font-weight:600}'
       '.hero h1{font-size:clamp(44px,5.6vw,80px)!important;line-height:1!important}'
       '.hero .stage{margin-top:46px}'
       '.stage .glow{position:absolute;left:12%;right:12%;top:8%;bottom:-6%;z-index:-1;border-radius:50%;filter:blur(64px) saturate(1.25);opacity:.42;pointer-events:none}'
       '.hero .stage .ph{animation:rise33 1.3s .55s cubic-bezier(.16,1,.3,1) backwards}'
       '@keyframes rise33{from{translate:0 70px;scale:.9;opacity:0}to{translate:0 0;scale:1;opacity:1}}'
       '.hb{padding:110px 40px 72px}.lede{display:flex;flex-direction:column;align-items:center;gap:26px;text-align:center}'
       '.lede p{font-size:20px;line-height:1.42;color:var(--mute);max-width:640px;margin:0;letter-spacing:-.015em}'
       '.hero .kpis{margin-top:64px}'
       '.tw{position:relative;z-index:1;will-change:transform}'
       '.shop>.s-ann,.shop>.s-hdr{position:relative;z-index:2}.shop>.s-hdr{background:#fff}'
       '.s-hero.m.bn{height:400px}.s-hero.m.bn:after{background:linear-gradient(transparent 35%,rgba(20,14,10,.55))!important}'
       '.s-hero.m.bn .s-ht{color:#fff!important}.s-hero.m.bn .s-ht a{border-color:#fff!important}.s-hero.m.bn h4{font-size:30px}'
       # secciones
       '.sec{padding:96px 0}.head{margin-bottom:52px}'
       # ficha
       '.fh{margin-top:130px}.fh h3{font-size:clamp(34px,4.2vw,52px);letter-spacing:-.045em;line-height:1.02;margin:0}'
       '.pdpz{position:relative;padding-right:150px}'
       '.pdpz .bw .scaler{height:auto!important;aspect-ratio:1280/800}'
       '.pdpz .ph{position:absolute;right:0;bottom:-44px;width:250px;box-shadow:0 2px 4px rgba(0,0,0,.05),0 30px 60px -20px rgba(var(--sh),.45),0 70px 120px -40px rgba(var(--sh),.5),0 0 0 1px rgba(0,0,0,.08)}'
       '.pts{display:grid;grid-template-columns:repeat(4,1fr);gap:0 28px;margin-top:84px;border-top:1px solid var(--line)}'
       '.pts div{padding-top:22px}.pts b{display:block;font-size:18px;letter-spacing:-.02em}.pts p{margin:6px 0 0;color:var(--mute);font-size:15px;line-height:1.42}'
       # diagnóstico
       '.cmp{border:1px solid var(--line);border-radius:20px;overflow:hidden;background:#fff}'
       '.cmp .rw{display:grid;grid-template-columns:190px 1fr;gap:28px;align-items:center;padding:28px 32px}'
       '.cmp .rw+.rw{border-top:1px solid var(--line);background:var(--cream)}'
       '.cmp .lb2 b{display:block;font-size:60px;font-weight:700;letter-spacing:-.06em;line-height:.85}'
       '.cmp .lb2 span{display:block;margin-top:8px;font-size:14px;line-height:1.3;color:var(--mute)}.cmp .on .lb2 b{color:var(--t)}'
       '.cmp .st{display:flex;flex-wrap:wrap;align-items:center;gap:8px}'
       '.cmp .st span{display:inline-flex;flex-direction:column;padding:9px 14px;border-radius:12px;background:#fff;box-shadow:inset 0 0 0 1px var(--line);font-size:14.5px;font-weight:600;letter-spacing:-.01em;line-height:1.25}'
       '.cmp .st small{font-size:12px;font-weight:400;color:var(--mute);letter-spacing:0}.cmp .st i{font-style:normal;color:var(--mute);opacity:.6}'
       '.cmp .on .st span{background:var(--t);color:#fff;box-shadow:none}.cmp .on .st small{color:rgba(255,255,255,.78)}'
       '.gs{display:flex;gap:14px;align-items:center;margin-top:16px;padding:18px 22px;border-radius:16px;background:var(--ink);color:#fff}'
       '.gs .ic{width:22px;height:22px;flex:none;color:#fff;opacity:.8}.gs p{margin:0;font-size:17px;line-height:1.4;letter-spacing:-.01em;color:#fff}'
       # ideas de campaña
       '#captacion .adsx{margin-top:0}.adsx .al .ix{display:block;margin-bottom:4px;font-size:12px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--ta)}'
       '.adsx .al .ob{display:block;margin-top:2px}'
       '.swp{display:none}'
       # plan
       '.ms{display:grid;grid-template-columns:repeat(4,1fr);position:relative}'
       '.ms:before{content:"";position:absolute;left:0;right:0;top:7px;height:2px;background:linear-gradient(90deg,var(--t),rgba(var(--tr),.2))}'
       '.ms div{position:relative;padding:34px 24px 0 0}'
       '.ms div:before{content:"";position:absolute;left:0;top:0;width:16px;height:16px;border-radius:50%;background:var(--cream);box-shadow:inset 0 0 0 2px var(--t)}'
       '.ms div:last-child:before{background:var(--t)}'
       '.ms small{font-size:13px;font-weight:600;color:var(--t)}.ms b{display:block;font-size:22px;letter-spacing:-.03em;margin:8px 0 6px}.ms p{margin:0;color:var(--mute);font-size:15px;line-height:1.42}'
       '.inc{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:60px}'
       '.inc>span{margin-right:6px;font-size:12.5px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--mute)}'
       '.inc em{font-style:normal;display:inline-flex;align-items:center;gap:8px;padding:10px 16px;border-radius:999px;background:#fff;box-shadow:inset 0 0 0 1px var(--line);font-size:14.5px;font-weight:500}'
       '.inc .i2{width:17px;height:17px;color:var(--t)}'
       # cierre
       '.close{min-height:640px}.close .cn{display:flex;gap:16px;align-items:center;max-width:520px}'
       '.close .cn img{width:56px;height:56px;border-radius:50%;object-fit:cover;flex:none;box-shadow:0 0 0 2px rgba(255,255,255,.55)}.close .cn p{font-size:19px;line-height:1.4}'
       '@media (prefers-reduced-motion:reduce){.hero .stage .ph{animation:none}}'
       # móvil
       '@media (max-width:760px){'
       '.hero{padding-top:90px!important}.hero .hi{margin-bottom:16px;padding:4px 14px 4px 4px}.hero .hi img{width:28px;height:28px}.hero .hi span{font-size:13px}'
       '.hero h1{font-size:clamp(31px,9.2vw,40px)!important}'
       '.hero .stage{margin-top:24px;padding:0;max-width:none}.hero .stage .lap{display:none}'
       '.hero .stage .ph{position:relative;right:auto;bottom:auto;margin:0 auto;border-radius:26px;transform:none!important;width:min(64vw,290px);width:clamp(210px,min(64vw,calc((100svh - 205px) * .486)),290px)}'
       '.stage .glow{left:4%;right:4%;top:4%;bottom:0;opacity:.5;filter:blur(48px) saturate(1.3)}'
       '.hb{padding:46px 20px 56px}.lede{gap:20px}.lede p{font-size:17px}.lede .btns{flex-direction:column;align-items:stretch;width:100%;max-width:340px}.lede .cta{justify-content:center}'
       '.hero .kpis{margin-top:40px}'
       '.sec{padding:64px 0}.head{margin-bottom:28px}'
       '.fh{margin-top:72px}.fh h3{font-size:30px}'
       '.pdpz{padding:0}.pdpz .bw{display:none}.pdpz .ph{position:relative;right:auto;bottom:auto;width:min(68vw,300px);margin:0 auto}'
       '.pts{grid-template-columns:1fr 1fr;gap:0 18px;margin-top:40px}.pts div{padding-top:18px}.pts b{font-size:16px}.pts p{font-size:14px}'
       '.cmp .rw{grid-template-columns:1fr;gap:14px;padding:22px 18px}.cmp .lb2{display:flex;align-items:baseline;gap:10px}.cmp .lb2 b{font-size:46px}.cmp .lb2 span{margin:0}'
       '.cmp .st{gap:6px}.cmp .st span{font-size:13.5px;padding:8px 11px}.cmp .st small{display:none}.gs{padding:16px 18px}.gs p{font-size:15.5px}'
       '#captacion .adsx .adg{display:grid;grid-template-columns:none!important;grid-auto-flow:column;grid-auto-columns:80%;gap:14px;overflow-x:auto;scroll-snap-type:x mandatory;'
       'margin:0 -20px;padding:6px 20px 20px;scrollbar-width:none;-webkit-overflow-scrolling:touch;overscroll-behavior-x:contain}'
       '#captacion .adg::-webkit-scrollbar{display:none}#captacion .adg>*{scroll-snap-align:center}'
       '.swp{display:block;margin:4px 0 0;font-size:13.5px;color:var(--mute2)}'
       '.ms{grid-template-columns:1fr}.ms:before{left:7px;right:auto;top:8px;bottom:30px;width:2px;height:auto;background:linear-gradient(var(--t),rgba(var(--tr),.2))}'
       '.ms div{padding:0 0 24px 36px}.ms div:before{top:1px}.ms b{font-size:19px;margin:4px 0}.ms p{font-size:14.5px}'
       '.inc{margin-top:24px}.inc>span{width:100%;margin-bottom:2px}.inc em{font-size:13.5px;padding:9px 13px}'
       '.close{min-height:560px}.close .cn p{font-size:17px}'
       '}'
       '</style>')
WA_JS = "<script>(function(){var b=document.querySelector('.wa-fab');if(!b)return;function f(){b.classList.toggle('on',scrollY>600)}addEventListener('scroll',f,{passive:true});f()})();</script>"
TOUR_JS = ("<script>/* v33: el portátil y el móvil del inicio recorren la tienda solos (se para fuera de pantalla y al pasar el ratón) */"
           "(function(){var d=document,RM=matchMedia('(prefers-reduced-motion: reduce)').matches;"
           # aparición de los bloques nuevos
           "var R=[].slice.call(d.querySelectorAll('.pdpz,.pts>div,.cmp .rw,.gs,.ms>div,.inc'));"
           "if('IntersectionObserver' in window){var io=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target)}})},{rootMargin:'0px 0px -10% 0px',threshold:.08});"
           "R.forEach(function(el){var k=[].indexOf.call(el.parentNode.children,el);el.classList.add('rv');el.style.setProperty('--d',Math.min(k*.08,.4)+'s');io.observe(el)})}"
           "if(RM)return;var T=[];"
           "function ez(t){return t<.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2}"
           "[].forEach.call(d.querySelectorAll('.hero .tw'),function(tr){var box=tr.closest('.scaler,.scr');if(!box)return;"
           "var o={tr:tr,box:box,base:box.classList.contains('scr')?375:1280,y:0,seq:null,i:0,t0:0,vis:true,hov:false,off:false};o.wait=o.base===375?6500:6000;T.push(o);"
           "if('IntersectionObserver' in window)new IntersectionObserver(function(e){o.vis=e[0].isIntersecting}).observe(box);"
           "if(matchMedia('(pointer:fine)').matches){box.addEventListener('pointerenter',function(){o.hov=true});box.addEventListener('pointerleave',function(){o.hov=false})}});"
           "if(!T.length)return;"
           "function plan(o){var w=o.box.clientWidth;if(!w){o.off=true;return null}var k=w/o.base,vh=o.box.clientHeight/k,top=o.tr.offsetTop,max=Math.max(0,o.tr.offsetHeight-(vh-top));if(max<40)return null;"
           "var st=[0];[].forEach.call(o.tr.children,function(ch){var y=Math.min(ch.offsetTop,max);if(y-st[st.length-1]>vh*.36)st.push(y)});if(max-st[st.length-1]>40)st.push(max);"
           "var q=[];for(var i=1;i<st.length;i++)q.push([st[i-1],st[i],1150,i==st.length-1?2300:1500]);q.push([st[st.length-1],0,1600,5500]);return q}"
           "var last=performance.now(),t00=last;function ld(){t00=performance.now()}if(d.readyState==='complete')ld();else addEventListener('load',ld);"
           "function frame(now){var dt=now-last;last=now;T.forEach(function(o){if(o.off)return;"
           "if(now-t00<o.wait||!o.vis||o.hov||d.hidden){o.t0+=dt;return}"
           "if(!o.seq){o.seq=plan(o);o.i=0;o.t0=now;if(!o.seq)return}"
           "var s=o.seq[o.i],t=now-o.t0;if(t<s[2])o.y=s[0]+(s[1]-s[0])*ez(t/s[2]);else{o.y=s[1];if(t>s[2]+s[3]){o.i++;o.t0=now;if(o.i>=o.seq.length)o.seq=null}}"
           "o.tr.style.transform='translate3d(0,'+(-o.y).toFixed(1)+'px,0)'});requestAnimationFrame(frame)}"
           "requestAnimationFrame(frame);addEventListener('resize',function(){T.forEach(function(o){o.off=false;o.seq=null;o.y=0;o.tr.style.transform=''})})"
           "})();</script>")
WA_IC = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M20 12a8 8 0 0 1-11.7 7.1L4 20l1-4.1A8 8 0 1 1 20 12z"/></svg>'

IC = {
 'truck': '<path d="M3 7h11v9H3zM14 10h4l3 3v3h-7z"/><circle cx="7" cy="17.5" r="1.6"/><circle cx="17" cy="17.5" r="1.6"/>',
 'store': '<path d="M4.5 10.5V20h15v-9.5M3 10.5 5 4h14l2 6.5c0 1.4-1.3 2.3-2.6 2.3s-2.5-1-2.5-2.3c0 1.4-1.4 2.3-2.9 2.3s-2.9-1-2.9-2.3c0 1.4-1.2 2.3-2.5 2.3S3 11.9 3 10.5zM10 20v-5h4v5"/>',
 'card': '<rect x="2.5" y="5" width="19" height="14" rx="2.5"/><path d="M2.5 9.5h19M6 15h4"/>',
 'chat': '<path d="M20 12a8 8 0 0 1-11.7 7.1L4 20l1-4.1A8 8 0 1 1 20 12z"/>',
 'insta': '<rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r=".6" fill="currentColor"/>',
 'bag': '<path d="M5 8h14l-1 12.5H6zM9 8V6.5a3 3 0 0 1 6 0V8"/>',
 'box': '<path d="M3.5 7.5 12 3l8.5 4.5v9L12 21l-8.5-4.5zM3.5 7.5 12 12l8.5-4.5M12 12v9"/>',
 'chart': '<path d="M4 20V4M4 20h16"/><path d="M8 16v-4M12 16V8M16 16v-6"/>',
 'spark': '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M18 6l-2.5 2.5M8.5 15.5 6 18"/>',
 'bot': '<rect x="4" y="7" width="16" height="12" rx="3"/><path d="M12 7V4M9 13h.01M15 13h.01M9 16.5h6"/>',
 'search': '<circle cx="11" cy="11" r="6.5"/><path d="m20 20-4.2-4.2"/>',
}
def ic(k, c='ic'):
    return f'<svg class="{c}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{IC[k]}</svg>'


def wm(c, size='m'):
    """the shop's logo: their own (transparent PNG) or a wordmark in SF Pro"""
    L = c['logo']
    if L.get('png'):
        return f'<span class="wm"><img src="/p-{c["slug"]}--b--logo.png" alt="{E(c["name"])}"></span>'
    t, sub = L['text'], L.get('sub', '')
    W = 220; tx = W / 2
    fs = L.get('fs', 24); ls = L.get('ls', '0.16em'); fw = L.get('fw', 500)
    s = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 46" role="img" aria-label="{E(c["name"])}">'
         f'<text x="{tx}" y="{27 if sub else 31}" text-anchor="middle" font-family="-apple-system,BlinkMacSystemFont,&#x27;SF Pro Display&#x27;,Inter,Helvetica,sans-serif" font-weight="{fw}" font-size="{fs}" letter-spacing="{ls}" fill="currentColor">{E(t)}</text>')
    if sub:
        s += (f'<text x="{tx}" y="42" text-anchor="middle" font-family="-apple-system,BlinkMacSystemFont,Inter,Helvetica,sans-serif" '
              f'font-size="8.5" letter-spacing="0.3em" fill="currentColor" opacity=".7">{E(sub)}</text>')
    return f'<span class="wm" style="color:var(--wmc)">{s}</svg></span>'


def bi(i, pos='center 40%'):
    return f'data-i="{i}" style="background-position:{pos}"'


# ---------------- the shop (home, mobile home, PDP desktop and mobile) ----------------
def hdr(c, m=False):
    if m:
        return f'<div class="s-hdr m"><span class="burg"><i></i><i></i><i></i></span>{wm(c)}{ic("bag")}</div>'
    return ('<div class="s-hdr"><nav>' + ''.join(f'<span>{E(x)}</span>' for x in c['nav'][:3]) + '</nav>' + wm(c) +
            '<div class="s-r"><span>Buscar</span><span>Cuenta</span><span>Cesta (0)</span></div></div>')


def mq(c):
    x = ''.join(f'<span>{E(s)}</span><i>✦</i>' for s in c['mq'])
    return f'<div class="s-mq"><div>{x}{x}</div></div>'


def pc(c, i, new=False):
    p = c['prods'][i]
    return (f'<div class="pc"><div class="pi" {bi(p["id"], p.get("pos", "center 30%"))}>{"<em>Nuevo</em>" if new else ""}</div>'
            f'<b>{E(p["name"])}</b><span>{E(p.get("price") or c.get("price_txt", "Vuestro precio"))}</span></div>')


def shop_home(c, full=True, tour=False):
    N = NICHE[c['niche']]; h = c['hero']
    s = f'<div class="shop"><div class="s-ann">{E(c["ann"])}</div>{hdr(c)}' + ('<div class="tw">' if tour else '')
    s += (f'<div class="s-hero2"><div class="a" {bi("h", c.get("hero_pos", "center"))}></div><div class="s-ht2"><small>{E(h["small"])}</small>'
          f'<h4>{h["h4"]}</h4><div class="bt2"><a class="w">{E(h["b1"])}</a><a>{E(h["b2"])}</a></div></div></div>')
    s += mq(c)
    if not full:
        return s + '</div>'
    s += '<div class="s-cats2">' + ''.join(f'<div {bi(k["id"], k.get("pos", "center 30%"))}><span>{E(k["label"])}<b>→</b></span></div>' for k in c['cats']) + '</div>'
    s += f'<div class="s-sec"><div class="s-h"><h5>{E(c.get("new_h", "Recién llegado"))}</h5><a>Ver todo</a></div><div class="s-grid">' + ''.join(pc(c, i, i < 2) for i in [1, 2, 3, 0]) + '</div></div>'
    lk = c['look']; p0, p1 = [it if isinstance(it, dict) else c['prods'][it] for it in lk['items'][:2]]
    s += (f'<div class="s-stl"><div class="img" {bi("look", lk.get("pos", "center 30%"))}>'
          f'<span class="hs" style="left:{lk["hs"][0][0]}%;top:{lk["hs"][0][1]}%"><i>+</i><em>{E(lk["hs_label"])}</em></span>'
          f'<span class="hs" style="left:{lk["hs"][1][0]}%;top:{lk["hs"][1][1]}%"><i>+</i></span></div>'
          f'<div class="tx"><small>{E(N["look_small"])}</small><h5>{lk["h5"]}</h5><p>{E(N["look_p"])}</p><div class="ls">'
          + ''.join(f'<div><i {bi(p["id"], p.get("pos", "center 30%"))}></i><span><b>{E(p["name"])}</b>{E(p.get("price") or c.get("price_txt", "Vuestro precio"))}</span><em>+</em></div>' for p in (p0, p1))
          + f'</div><a class="btn2">{E(N["look_btn"])}</a></div></div>')
    b = c['big']
    s += f'<div class="s-big" {bi("l5", b.get("pos", "center"))}><div><small>{E(b["small"])}</small><h5>{b["h5"]}</h5><a class="w">{E(b["btn"])}</a></div></div>'
    s += f'<div class="s-rev"><small>{E(c["rev_h"])}</small><div>' + ''.join(f'<figure><blockquote>“{E(q)}”</blockquote><figcaption>{E(a)}</figcaption></figure>' for q, a in c['quotes']) + '</div></div>'
    s += (f'<div class="s-ig"><div class="s-h"><h5>@{E(c["handle"])} en Instagram</h5><a>{ic("insta")}Seguir</a></div><div class="igs">'
          + ''.join(f'<i data-i="{k}"></i>' for k in c['igrid']) + '</div></div>')
    tr = [('truck', 'Envío a domicilio', 'a toda España'), ('store', c['trust_store'][0], c['trust_store'][1]),
          ('card', 'Tarjeta, Bizum, Apple Pay', 'pago seguro'), ('chat', 'WhatsApp', N['wa_trust'])]
    s += '<div class="s-trust">' + ''.join(f'<div>{ic(a)}<b>{E(b_)}</b><span>{E(cc)}</span></div>' for a, b_, cc in tr) + '</div>'
    s += (f'<div class="s-foot"><div>{wm(c)}<p>{E(c["foot_addr"])}</p></div><div><b>Tienda</b><p>{E(c["foot_store"])}</p></div>'
          f'<div><b>Ayuda</b><p>Envíos y cambios<br>{E(N["help2"])}<br>WhatsApp</p></div><div><b>Síguenos</b><p>@{E(c["handle"])}<br>{E(c["followers"])} seguidores</p></div></div>')
    return s + ('</div>' if tour else '') + '</div>'


def shop_home_m(c, tour=False):
    h = c['hero']
    s = f'<div class="shop sm"><div class="s-ann">{E(c["ann_m"])}</div>{hdr(c, True)}' + ('<div class="tw">' if tour else '')
    s += f'<div class="s-hero m"><div {bi("h", c.get("hero_pos_m", "72% center"))}></div><div class="s-ht"><small>{E(h["small_m"])}</small><h4>{h["h4"]}</h4><a>{E(h["b1"])}</a></div></div>'
    s += '<div class="s-mq m"><div>' + ''.join(f'<span>{E(x)}</span><i>✦</i>' for x in c['mq']) + '</div></div>'
    s += '<div class="s-cats m">' + ''.join(f'<div><i {bi(k["id"], k.get("pos", "center 30%"))}></i><span>{E(k["label"])}</span></div>' for k in c['cats'][:3]) + '</div>'
    s += (f'<div class="s-sec"><div class="s-h"><h5>{E(c.get("new_h", "Recién llegado"))}</h5><a>Ver todo</a></div><div class="s-grid">' + pc(c, 1, True) + pc(c, 2, True)
          + (pc(c, 3) + pc(c, 4) if tour else '') + '</div></div>')
    if tour:
        b = c['big']
        s += (f'<div class="s-hero m bn"><div {bi("l5", b.get("pos", "center"))}></div><div class="s-ht"><small>{E(b["small"])}</small><h4>{b["h5"]}</h4><a>{E(b["btn"])}</a></div></div>'
              '</div>')
    return s + '</div>'


def pdp_inf(c, m=False):
    N = NICHE[c['niche']]; p = c['prods'][0]
    acc = ''.join(f'<div>{E(a)} <i>+</i></div>' for a in N['acc'])
    return (f'<div class="inf{" m" if m else ""}"><div class="crumb">{E(p["crumb"])}</div><h4>{E(p["name"])}</h4>'
            f'<div class="price">{E(p.get("price") or c.get("price_txt", "Vuestro precio"))} <small>IVA incluido</small></div>'
            + (N['variant'](c) if not m and N.get('variant') else '') +
            f'<div class="add">Añadir a la cesta</div><div class="pay"><span>Apple Pay</span><span>Bizum</span><span>Visa</span><span>Mastercard</span></div>'
            f'<div class="acc">{acc}</div><div class="wa">{ic("chat")}<div><b>{E(N["wa_q"])}</b><span>Escribidnos por WhatsApp y os ayudamos.</span></div></div></div>')


def shop_pdp(c):
    N = NICHE[c['niche']]; g = c['pdp']
    s = f'<div class="shop"><div class="s-ann">{E(c["ann"])}</div>{hdr(c)}<div class="s-pdp"><div class="g">'
    s += f'<div class="tag" {bi("p1", c["prods"][0].get("pos", "center 30%"))}><em>{E(g["t1"])}</em></div>'
    s += f'<div class="ifg" {bi("x1", g.get("x1pos", "center"))}><span class="t">{E(g["ifg_t"])}</span>'
    for k, (b, sp) in enumerate(g['callouts']):
        s += f'<span class="c c{k + 1}"><i></i><span><b>{E(b)}</b>{E(sp)}</span></span>'
    s += f'</div><div class="tag" {bi("x2", g.get("x2pos", "center 30%"))}><em>{E(g["t2"])}</em></div><div class="tag" {bi("x3", "center")}><em>{E(g["t3"])}</em></div></div>'
    s += pdp_inf(c) + '</div>'
    s += f'<div class="s-sec"><div class="s-h"><h5>{E(N["complete"])}</h5></div><div class="s-grid">' + ''.join(pc(c, i) for i in [1, 2, 4, 3]) + '</div></div>'
    return s + '</div>'


def shop_pdp_m(c):
    s = f'<div class="shop sm"><div class="s-ann">{E(c["ann_m"])}</div>{hdr(c, True)}'
    s += f'<div class="s-pm" {bi("p1", c["prods"][0].get("pos", "center 30%"))}><div class="dots"><i class="on"></i><i></i><i></i><i></i></div></div>'
    return s + pdp_inf(c, True) + '</div>'


def bw(c, inner):
    return f'<div class="bw"><div class="bar"><i></i><i></i><i></i><span>{E(c["domain"])}</span></div><div class="scaler" data-w="1280">{inner}</div></div>'


def phone(c, inner):
    return f'<div class="ph"><div class="mb"><span>{E(c["domain"])}</span></div><div class="scr"><div class="pin">{inner}</div></div></div>'


def cta(c, n, label, small=''):
    return (f'<a class="cta" href="{BOOK}{c["slug"]}&amp;utm_content=cta-{n}" target="_blank" rel="noopener">{label}<span>→</span></a>'
            + (f'<small>{E(small)}</small>' if small else ''))


# ---------------- the proposal (v33, 4/11/2026: más corta; la tienda se recorre sola en el primer pantallazo) ----------------
def body(c):
    N = NICHE[c['niche']]; nm = E(c['name']); sh = E(c['short']); d = c['diag']
    o = ('<body>\n<div class="nav"><div class="wrap"><a class="br" href="#inicio">' + wm(c) + '</a>'
         '<div class="lk2"><a href="#tienda">Tienda</a><a href="#diagnostico">Diagnóstico</a><a href="#captacion">Anuncios</a><a href="#plan">Plan</a></div>'
         f'<a class="cta" href="{wa(c)}" target="_blank" rel="noopener">Hablamos<span>→</span></a></div></div>\n')
    # hero: poco texto y la tienda a la vista (portátil + móvil que se recorren solos)
    o += (f'<header class="hero" id="inicio"><div class="wrap"><div class="hi"><img src="/christian-hola.jpg" alt="Christian" width="32" height="32">'
          f'<span><b>Christian</b> · propuesta para {sh}</span></div>'
          f'<h1>{c.get("h1", sh + ",<br><span class=\"t\">abierta 24&nbsp;horas.</span>")}</h1></div>'
          f'<div class="stage"><i class="glow" data-i="h"></i><div class="lap">{bw(c, shop_home(c, True, True))}</div>{phone(c, shop_home_m(c, True))}</div>'
          f'<div class="hb"><div class="lede"><p>{c["sub"]}</p><div class="btns"><a class="cta" href="{wa(c)}" target="_blank" rel="noopener">Quiero mi tienda<span>→</span></a>'
          f'<a class="cta ghost" href="{BOOK}{c["slug"]}&amp;utm_content=cta-2" target="_blank" rel="noopener">Reservar 30 min</a></div></div>'
          '<div class="kpis">' + ''.join(f'<div><b{" class=t" if k == 3 else ""}>{a}</b><span>{E(b)}</span></div>' for k, (a, b) in enumerate(c['kpis'])) + '</div></div></header>\n')
    # 01 · la tienda completa (como en v32) y su ficha de producto
    o += (f'<section class="sec shopsec" id="tienda"><div class="wrap"><div class="chap"><span class="num">01</span><span class="lb">La tienda</span></div>'
          f'<div class="head"><h2>Así se vería<br>{nm} online.</h2><p>{E(N["tienda_p"])}</p></div>'
          f'{bw(c, shop_home(c))}<div class="ctarow">{cta(c, 3, "Quiero esta tienda para " + sh)}</div>'
          f'<div class="head fh"><h3>{N["pdp_h3"]}</h3><p>{E(N["item_art"]).capitalize()} que enseñáis en Instagram, con su ficha, cesta y pago con tarjeta, Bizum o Apple&nbsp;Pay.</p></div>'
          f'<div class="pdpz">{bw(c, shop_pdp(c))}{phone(c, shop_pdp_m(c))}</div>'
          '<div class="pts">' + ''.join(f'<div><b>{E(a)}</b><p>{E(b)}</p></div>' for a, b in N['pdp_points']) + '</div></div></section>\n')
    # 02 · diagnóstico: lo suyo, con sus datos, y los pasos de hoy frente a los de la tienda
    today = [(a, b.replace('{city}', c['city'])) for a, b in N['flow_today']]
    row = lambda st: '<i>›</i>'.join(f'<span>{E(a)}<small>{E(b)}</small></span>' for a, b in st)
    o += (f'<section class="sec" id="diagnostico"><div class="wrap"><div class="chap"><span class="num">02</span><span class="lb">Diagnóstico</span></div>'
          f'<div class="head"><h2>{d["h2"]}</h2><p>{d["p"]}</p></div><div class="cmp">'
          f'<div class="rw"><div class="lb2"><b>{len(today)}</b><span>pasos para comprar hoy</span></div><div class="st">{row(today)}</div></div>'
          f'<div class="rw on"><div class="lb2"><b>{len(N["flow_new"])}</b><span>con vuestra tienda online</span></div><div class="st">{row(N["flow_new"])}</div></div></div>'
          + (f'<div class="gs">{ic("search")}<p>{E(d["leaks"][0][1])}</p></div>' if c['web_state'] == 'none' else '')
          + '</div></section>\n')
    # 03 · ideas de campaña (los creativos estáticos)
    o += ('<section class="sec dark" id="captacion"><div class="wrap"><div class="chap"><span class="num">03</span><span class="lb">Ideas de campaña</span></div>'
          f'<div class="head"><h2>Seis anuncios,<br>listos para lanzar.</h2><p>Hechos con vuestras fotos. Cada uno con un objetivo: vender fuera de {E(c["city_short"])}, recuperar a quien ya os vio o subir el ticket medio.</p></div>'
          + ads(c) + '<p class="swp">Deslizad para ver las seis →</p>'
          + f'<div class="ctarow dk">{cta(c, 5, "Lanzar estas campañas", "Os preparamos la primera tanda")}</div></div></section>\n')
    o += plan(c)
    o += (f'<section class="close" id="hablar" data-i="h"><div class="wrap"><div class="chap"><span class="num">→</span><span class="lb">Siguiente paso</span></div>'
          f'<h2>¿Abrimos {sh}<br><span class="t">a toda España?</span></h2><div class="row"><div class="cn"><img src="/christian-hola.jpg" alt="Christian" width="56" height="56">'
          '<p>Soy Christian. Os enseño esta tienda en 30 minutos, con vuestro catálogo y en directo.</p></div>'
          f'<div class="btns"><a class="cta" href="{wa(c)}" target="_blank" rel="noopener">Escribidme por WhatsApp<span>→</span></a>'
          f'<a class="cta ghost" href="{BOOK}{c["slug"]}&amp;utm_content=cta-8" target="_blank" rel="noopener">Reservar videollamada</a></div></div></div></section>\n'
          f'<footer id="pie"><div class="wrap"><span>Demo de concepto de 404 Growth. No es la web oficial.</span><span>Marca y productos: {nm} · @{E(c["handle"])}. Fotos de la tienda creadas con IA a partir de sus productos reales.</span></div></footer>\n'
          f'<a class="wa-fab" href="{wa(c)}" target="_blank" rel="noopener"><img src="/christian-hola.jpg" alt="" width="38" height="38"><span>Escribir a Christian<small>por WhatsApp</small></span>{WA_IC}</a>\n')
    return o


def ad(c, inner, foot, label, n):
    a = E(c['handle']); ini = E(c['name'][0].upper())
    return (f'<div class="adw"><div class="ad"><div class="ah"><span class="av"><i>{ini}</i></span><b>{a}</b><small>Publicidad</small><em>···</em></div>'
            f'<div class="am">{inner}</div><div class="af"><span>{E(foot)}</span><b>›</b></div></div><p class="al"><span class="ix">Idea {n}</span>{_lab(label)}</p></div>')


def _lab(label):
    """'<b>Envío</b> · captación fuera de X' → título y objetivo en dos líneas, sin el punto"""
    m = re.match(r'(<b>.*?</b>)\s*·\s*(.+)$', label)
    if not m:
        return label
    ob = m.group(2)
    return m.group(1) + f'<span class="ob">{ob[0].upper() + ob[1:]}</span>'


def ads(c):
    N = NICHE[c['niche']]; A = c['ads']; p = c['prods']
    g = ad(c, f'<div class="ab" {bi("x2", "center 30%")}></div><div class="ao bl"><small>{E(A.get("a1s", "Nueva colección"))}</small><h6 style="font-size:26px">{A["a1"]}</h6><span class="pill">Comprar</span></div>',
           'Comprar ahora', '<b>Producto estrella</b> · retargeting a quien vio el post', 1)
    g += ad(c, f'<div class="ab" {bi("l1", "center 30%")}></div><div class="ao tp"><h6>De {E(c["city_short"])}<br>a toda España.</h6></div>',
            'Comprar ahora', f'<b>Envío</b> · captación fuera de {E(c["city_short"])}', 2)
    g += ad(c, f'<div class="ab cr"><div class="col"><i data-i="{p[1]["id"]}"></i><b>+</b><i data-i="{p[2]["id"]}"></i><b>+</b><i data-i="{p[3]["id"]}"></i></div><h6 class="dk">{A["a3"]}</h6></div>',
            N['ad3_btn'], f'<b>{E(N["complete"])}</b> · sube el ticket medio', 3)
    g += ad(c, f'<div class="ab tc"><div class="qt">“{E(c["quotes"][0][0])}”<small>{E(c["quotes"][0][1])}</small></div><i class="rd" data-i="l3"></i></div>',
            'Comprar ahora', '<b>Vuestra voz</b> · lo que ya contáis en Instagram', 4)
    g += ad(c, f'<div class="ab sp"><i data-i="look"></i><div class="bl2"><small>En {E(c["short"])}</small>' + ''.join(f'<span>{E(k["label"])}</span>' for k in c['cats']) + '<span>Novedades</span></div></div>',
            'Descubrir', '<b>Catálogo</b> · todo lo que tenéis, a un toque', 5)
    g += ad(c, f'<div class="ab" {bi("l4", "center 30%")}></div><div class="ao bl"><small>{E(A["a6s"])}</small><h6>{A["a6"]}</h6><span class="pill">{E(A["a6b"])}</span></div>',
            'Enviar mensaje', A['a6l'], 6)
    return f'<div class="adsx"><div class="adg">{g}</div></div>'


def plan(c):
    N = NICHE[c['niche']]
    ms = [('Día 0', 'Llamada de arranque', 'Nos contáis cómo funciona la tienda y preparamos los accesos.'),
          ('Días 3–10', 'Diseño y catálogo', f'Vuestra marca, vuestras fotos y las primeras {N["item_pl"]} subidas.'),
          ('Días 8–14', 'Pagos, envíos y prueba', 'Checkout, envíos, stock unificado y un pedido de prueba real.'),
          ('Día 15', 'Lanzamiento', 'Tienda abierta, Instagram Shopping y medición activa.')]
    inc = [('store', 'Tienda online propia'), ('card', 'Tarjeta, Bizum y Apple Pay'), ('box', 'Stock unificado con la tienda'),
           ('insta', 'Instagram Shopping'), ('spark', 'Anuncios en Meta'), ('chart', 'Medición de cada venta')]
    return (f'<section class="sec" id="plan" style="background:var(--cream)"><div class="wrap"><div class="chap"><span class="num">04</span><span class="lb">Plan</span></div>'
            '<div class="head"><h2>En 15 días,<br>vendiendo online.</h2><p>Lo montamos nosotros, con vosotros, mientras la tienda sigue abierta como siempre.</p></div>'
            '<div class="ms">' + ''.join(f'<div><small>{a}</small><b>{E(b)}</b><p>{E(p)}</p></div>' for a, b, p in ms) + '</div>'
            '<div class="inc"><span>Incluye</span>' + ''.join(f'<em>{ic(i, "i2")}{E(t)}</em>' for i, t in inc) + '</div>'
            f'<div class="ctarow">{cta(c, 7, "Reservar la llamada", "30 minutos · sin compromiso")}</div></div></section>\n')


def _rgb(h):
    h = h.lstrip('#'); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _hex(r):
    return '#%02X%02X%02X' % tuple(max(0, min(255, int(round(x)))) for x in r)


def _hls(h, dl=0.0, ds=0.0, dh=0.0, l=None, s=None):
    r, g, b = [x / 255 for x in _rgb(h)]; H, L_, S = colorsys.rgb_to_hls(r, g, b)
    H = (H + dh) % 1; L_ = l if l is not None else min(1, max(0, L_ + dl)); S = s if s is not None else min(1, max(0, S + ds))
    return _hex([x * 255 for x in colorsys.hls_to_rgb(H, L_, S)])


def palette(c):
    col = c['colors']; t = col['t']; td = col.get('td') or _hls(t, -.12); tl = col.get('tl') or _hls(t, l=.78)
    rgb = lambda h: ','.join(str(x) for x in _rgb(h))
    a1 = _hls(t, l=.80, s=.55); a2 = col.get('a2') or _hls(t, l=.86, s=.35, dh=.08)
    deep = _hls(t, l=.08, s=.35); ink = col.get('ink', '#141110')
    return (':root{--t:%s;--td:%s;--tl:%s;--ta:%s;--tr:%s;--a1:%s;--a2:%s;--sh:%s;--gb:%s;--rim:%s;--cream:%s;--ink:%s;--deep:%s;--deep3:%s;--tl2:%s;--tl3:%s;'
            "--wmf:-apple-system,BlinkMacSystemFont,'SF Pro Display',Inter,Helvetica,sans-serif;--wmw:500;--wml:.12em;--wmt:uppercase}"
            % (t, td, tl, tl, rgb(t), rgb(a1), rgb(a2), rgb(_hls(t, l=.14)), rgb(td), rgb(tl), col['cream'], ink, deep, rgb(deep), _hls(t, l=.68), rgb(_hls(t, l=.68))))


# ---------------- head, images, scripts ----------------
IMG_MAX = {'h': 2400, 'l5': 2000, 'x1': 1200}


def head(c, ids):
    s = c['slug']; nm = E(c['name']); N = NICHE[c['niche']]
    title = f'{nm} × 404 Growth · Vuestra {N["shop_of"]} online'
    desc = f'Así se vería la tienda online de {nm}: con vuestras {N["item_pl"]} y vuestro estilo, lista para vender en toda España.'
    st0 = P['styles'][0]
    col = c['colors']
    st0 = st0.replace('</style>', palette(c) + '</style>')
    v2 = (f'<style id="v2">[data-i="h"]{{background-image:url(/p-{s}--b--h.jpg)!important;background-size:cover;background-position:{c.get("hero_pos", "center")}}}'
          '.s-ht2 h4{font-size:66px!important}.s-hero2{grid-template-columns:1fr!important}'
          f'.s-hero.m [data-i="h"]{{background-position:{c.get("hero_pos_m", "72% center")}}}.close[data-i="h"]{{background-position:{c.get("close_pos", "center 40%")}!important}}'
          + (c.get('hero_css') or '.s-hero2:after,.s-hero.m:after{background:linear-gradient(90deg,rgba(20,14,10,.55),rgba(20,14,10,.25) 40%,rgba(20,14,10,0) 65%)!important}') +
          '.s-ht2 h4 em,.s-ht h4 em{font-style:normal!important;font-weight:500!important}.wm{color:var(--wmc)}:root{--wmc:var(--ink)}'
          '.gantt.g15 .gh div:last-child,.gantt.g15 .gt{grid-template-columns:repeat(15,1fr)!important}'
          '.close:before{background:linear-gradient(180deg,rgba(14,10,9,.3),rgba(14,10,9,.86) 76%)!important}</style>')
    v3i = '<style id="v3i">' + ''.join(f'[data-i="{i}"]{{background-image:url(/p-{s}--b--{i}.jpg)!important}}' for i in ids if i != 'h') + '</style>'
    return ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow">'
            f'<title>{title}</title><meta name="description" content="{desc}"><meta property="og:type" content="website"><meta property="og:site_name" content="404 Growth">'
            f'<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="https://404growth.com/p-{s}--b--og.jpg">'
            '<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">'
            '<link rel="icon" href="/favicon.svg" type="image/svg+xml">' + P['scripts_head'][0] + st0 + v2 + P['styles'][2] + P['styles'][3] + v3i + V32 + V33 + '</head>')


def scripts(c):
    sb = P['scripts_body']
    cnt = sb[2].replace('var slug="lola-shop-madrid"', f'var slug="{c["slug"]}"')
    assert f'var slug="{c["slug"]}"' in cnt
    return sb[0] + sb[1] + cnt + sb[4] + WA_JS + TOUR_JS + '</body></html>'


def images(c):
    s = c['slug']; src = os.path.join(L31, 'ai', s); ids = []
    m = {'h': 'hero'}
    for i in ['h', 'p1', 'p2', 'p3', 'p4', 'p5', 'x1', 'x2', 'x3', 'look', 'l1', 'l2', 'l3', 'l4', 'l5']:
        f = os.path.join(src, m.get(i, i) + '.jpg')
        if not os.path.exists(f):
            print('  falta', s, i); continue
        im = Image.open(f).convert('RGB'); mx = IMG_MAX.get(i, 1100)
        if max(im.size) > mx:
            im.thumbnail((mx, mx), Image.LANCZOS)
        im.save(os.path.join(OUT, f'p-{s}--b--{i}.jpg'), 'JPEG', quality=84, optimize=True, progressive=True)
        ids.append(i)
    # og 1200x630 from the hero
    im = Image.open(os.path.join(src, 'hero.jpg')).convert('RGB'); w, h = im.size; r = 1200 / 630
    cw, ch = (w, int(w / r)) if w / h < r else (int(h * r), h)
    fx = c.get('og_fx', .5); x0 = int((w - cw) * fx); y0 = (h - ch) // 2
    im.crop((x0, y0, x0 + cw, y0 + ch)).resize((1200, 630), Image.LANCZOS).save(os.path.join(OUT, f'p-{s}--b--og.jpg'), 'JPEG', quality=86, optimize=True)
    if c['logo'].get('png'):
        Image.open(c['logo']['png']).save(os.path.join(OUT, f'p-{s}--b--logo.png'), optimize=True)
    return ids


def build(slug):
    c = SHOPS[slug]; c['slug'] = slug
    os.makedirs(OUT, exist_ok=True); os.makedirs(os.path.join(L31, 'shots'), exist_ok=True)
    ids = images(c)
    h = head(c, ids) + body(c) + scripts(c)
    open(os.path.join(OUT, f'p-{slug}.html'), 'w').write(h)
    open(os.path.join(L31, 'shots', f'{slug}-shop.html'), 'w').write(shot_html(c))
    left = re.findall(r'\{[a-z_]+\}', re.sub(r'<(script|style)[^>]*>.*?</\1>', '', h, flags=re.S))
    print('ok', slug, len(h), 'imgs', len(ids), 'placeholders', left[:5])


def shot_html(c):
    """just the shop home at 1280 px, for the «después» screenshot"""
    ids = [i for i in ['h', 'p1', 'p2', 'p3', 'p4', 'p5', 'x1', 'x2', 'x3', 'look', 'l1', 'l2', 'l3', 'l4', 'l5']]
    return (head(c, ids) + '<body style="margin:0;width:1280px;overflow:hidden"><div style="position:relative;width:1280px">'
            + shop_home(c).replace('<div class="shop">', '<div class="shop" style="position:relative;transform:none">', 1) + '</div></body></html>')


if __name__ == '__main__':
    for s in sys.argv[1:]:
        build(s)
