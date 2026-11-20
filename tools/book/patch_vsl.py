"""/book con el VSL otra vez (20/11/2026).

uso: python3 patch_vsl.py <book.html sin vídeo (13/11)> <lq.b64> <salida>

En la primera pantalla tienen que verse siempre el titular, el vídeo y el botón de reservar (móvil y ordenador).
El vídeo arranca solo, sin sonido y en bucle; mientras carga se ve un fotograma borroso metido en la página
(lq.b64: JPEG de 96x54 en base64). En el centro, siempre, el botón «Reproducir con audio»: al pulsarlo vuelve
al segundo 0 y suena. Solo se cuenta (admin y píxel) lo que se ve con el audio activado.
"""
import sys

SRC, LQ, OUT = sys.argv[1:4]
s = open(SRC, encoding='utf-8').read()
lq = open(LQ).read().strip()
n = 0


def rep(a, b):
    global s, n
    assert s.count(a) == 1, (a[:70], s.count(a))
    s = s.replace(a, b)
    n += 1


# ---------- textos que hablaban del vídeo ----------
rep('con tu stock y tu marca. Reserva una llamada de 30 minutos.">',
    'con tu stock y tu marca. Mira el vídeo y reserva 30 minutos.">')
rep('vendiendo online en toda España en 15 días. Reserva una llamada de 30 minutos.">',
    'vendiendo online en toda España en 15 días. Mira el vídeo y reserva una llamada de 30 minutos.">')
rep('he%20visto%20tu%20web%20y%20quiero', 'he%20visto%20el%20v%C3%ADdeo%20y%20quiero')

# ---------- estilos ----------
rep('''/* ordenador: H1 y primer botón caben en la primera pantalla (desde el 13/11/2026, sin vídeo) */''',
    '''/* VSL (20/11/2026): fotograma borroso mientras carga, el vídeo encima y el botón «Reproducir con audio» en el centro */
.screen .vlq{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:blur(16px);transform:scale(1.14)}
.screen .vlq.ok{filter:none;transform:none}
.screen video{position:relative;background:transparent;opacity:0;transition:opacity .45s}
.screen.vp video{opacity:1}
.vgo{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);z-index:3;display:inline-flex;align-items:center;gap:13px;border:0;cursor:pointer;
 font-family:inherit;font-size:17px;font-weight:600;letter-spacing:-.012em;color:#0B1512;background:#fff;padding:10px 24px 10px 10px;border-radius:99px;white-space:nowrap;
 box-shadow:0 12px 44px rgba(0,0,0,.4);transition:transform .25s cubic-bezier(.2,.8,.2,1)}
.vgo i{width:46px;height:46px;border-radius:50%;background:#0B1512;display:grid;place-items:center;flex:none}
.vgo svg{width:18px;height:18px;color:#fff;margin-left:3px}
@media (hover:hover){.vgo:hover{transform:translate(-50%,-50%) scale(1.045)}}.vgo:active{transform:translate(-50%,-50%) scale(.97)}
.vgo:focus-visible{outline:2px solid var(--t2);outline-offset:4px}
.screen.aud .vgo{display:none}
@media (prefers-reduced-motion:reduce){.screen video,.vgo{transition:none}}
/* el titular, el vídeo y el botón caben siempre en la primera pantalla: el vídeo se encoge si la pantalla es baja */
@media (max-width:900px){
 .hero .wrap{padding-left:16px;padding-right:16px}
 .hero h1{margin-top:12px}
 .eyebrow{margin-top:12px}
 .stage{margin-top:18px;padding-bottom:0}
 .device{max-width:min(100%,max(240px,calc((100svh - 372px) * 16 / 9 + 14px)))}
 .hero .cta{margin-top:16px;gap:12px}
 .vgo{font-size:15px;gap:10px;padding:8px 18px 8px 8px}.vgo i{width:38px;height:38px}.vgo svg{width:15px;height:15px}
}
@media (max-width:560px){.top{padding-top:16px}}

/* ordenador: H1, vídeo y primer botón caben en la primera pantalla */''')
rep(''' .stage{margin-top:24px;max-width:1140px}
 .device{max-width:min(1080px,max(480px,calc((100vh - 470px) * 16 / 9 + 24px)));padding:10px;border-radius:28px}
 .screen{border-radius:20px}
 .hero .cta{margin-top:34px;gap:12px}
}''',
    ''' .stage{margin-top:22px;max-width:1140px;padding-bottom:0}
 .device{max-width:min(1080px,max(360px,calc((100vh - 255px - 2.92 * clamp(40px,min(4.5vw,7vh),66px)) * 16 / 9 + 20px)));padding:10px;border-radius:28px}
 .screen{border-radius:20px}
 .hero .cta{margin-top:20px;gap:12px}
}
/* pantallas muy bajas (móvil tumbado): sin el aviso de arriba y con el titular en pequeño */
@media (max-height:540px) and (min-width:561px){
 .top{padding-top:10px}.top:after{display:none}
 .eyebrow{display:none}
 .hero h1{font-size:clamp(19px,6vh,32px);line-height:1.04;margin-top:8px;max-width:none}
 .hero h1>span{display:inline}.hero h1 .ha{font-size:1em;margin:0}
 .stage{margin-top:10px}
 .device{max-width:max(190px,calc((100vh - 168px - 2.2 * clamp(19px,6vh,32px)) * 16 / 9 + 12px));padding:6px;border-radius:18px}
 .screen{border-radius:13px}
 .hero .cta{margin-top:10px}
 .hero .cta .btn{font-size:15px;padding:5px 5px 5px 20px}
 .vgo{font-size:14px;gap:9px;padding:6px 15px 6px 6px}.vgo i{width:32px;height:32px}.vgo svg{width:13px;height:13px}
}''')
rep(''' .stage{margin-top:36px}
 .device{padding:7px;border-radius:24px}.screen{border-radius:18px}''',
    ''' .device{padding:7px;border-radius:24px}.screen{border-radius:18px}''')

# ---------- el hueco del vídeo, entre el titular y el botón ----------
rep('''</span></span></h1>
    <div class="cta">''',
    '''</span></span></h1>
    <div class="stage">
      <div class="arc2" aria-hidden="true"></div><div class="arc" aria-hidden="true"></div>
      <figure class="device" id="vsl" style="margin-top:0;margin-bottom:0">
        <div class="screen" id="screen">
          <img class="vlq" id="vlq" alt="" aria-hidden="true" src="data:image/jpeg;base64,%s">
          <video id="vv" muted loop playsinline preload="auto" aria-label="Vídeo de Christian: cómo tu tienda física puede vender online"></video>
          <button class="vgo" id="vgo" type="button"><i aria-hidden="true"><svg><use href="#i-play"/></svg></i>Reproducir con audio</button>
        </div>
      </figure>
    </div>
    <div class="cta">''' % lq)

# ---------- el script ----------
rep('''     VSL:    desde el 13/11/2026 la página va sin vídeo (se quitó el hueco del héroe); esto solo vale si se vuelve a poner el <figure id="vsl">.
             src = mp4 con subtítulos quemados; poster = foto fija; ratio "16/9" o "9/16". src vacío = el hueco con el botón de play.''',
    '''     VSL:    el vídeo del héroe (desde el 20/11/2026). src = lista HLS (o un mp4); poster = fotograma nítido por si el navegador no deja
             arrancar solo. Arranca sin sonido y en bucle; con «Reproducir con audio» vuelve al segundo 0 y suena.''')
rep("var VSL={src:'',poster:'',ratio:'16/9'};", "var VSL={src:'/v/book/index.m3u8',poster:'/v/book/poster.jpg',ratio:'16/9'};")

a = s.index("  /* ---------- el vídeo ---------- */")
b = s.index("  /* ---------- clics en los botones ---------- */")
s = s[:a] + '''  /* ---------- el vídeo ---------- */
  if(VSL.src&&$('vsl')){
    var sc=$('screen'),v=$('vv'),go=$('vgo'),lq=$('vlq'),aud=false,on=false,hl=null,tapT=0,want=false;
    var calm=(window.matchMedia&&matchMedia('(prefers-reduced-motion:reduce)').matches)||!!(navigator.connection&&navigator.connection.saveData);
    function sharp(){var i=new Image();i.onload=function(){lq.src=VSL.poster;lq.classList.add('ok')};i.src=VSL.poster}
    function go2(){var p=v.play();if(p&&p.catch)p.catch(function(){if(!aud)sharp()})}
    function attach(){if(on)return;on=true;
      if(/\\.m3u8(\\?|$)/.test(VSL.src)&&!v.canPlayType('application/vnd.apple.mpegurl')){
        var s=d.createElement('script');s.src='/v/hls.light.min.js';
        s.onload=function(){if(window.Hls&&Hls.isSupported()){hl=new Hls({capLevelToPlayerSize:false,abrEwmaDefaultEstimate:1e6});hl.loadSource(VSL.src);hl.attachMedia(v)}else v.src=VSL.src;if(aud||want)go2()};
        s.onerror=sharp;d.head.appendChild(s)}
      else{v.src=VSL.src;if(aud||want)go2()}}
    /* de fondo: sin sonido, en bucle y solo mientras se ve */
    if(calm)sharp();else{want=true;attach();
      if('IntersectionObserver' in window)new IntersectionObserver(function(en){if(aud)return;if(en[0].isIntersecting){want=true;go2()}else{want=false;v.pause()}},{threshold:.15}).observe(sc)}
    v.addEventListener('timeupdate',function(){if(v.currentTime>.05)sc.classList.add('vp')});
    /* con audio: desde el segundo 0 */
    go.addEventListener('click',function(){aud=true;tapT=Date.now();lastT=0;sc.classList.add('aud');v.loop=false;v.muted=false;v.volume=1;v.controls=true;
      attach();try{v.currentTime=0}catch(e){}go2();
      VS.plays++;VS.unm=1;ev('vplay','audio',0);if(!played){played=true;px('VSLPlay',{},true)}});
    /* solo cuenta lo que se ve con el audio activado */
    var played=false,marks={},lastT=0,wasMuted=true;
    v.addEventListener('play',function(){if(!aud||Date.now()-tapT<900)return;VS.plays++;ev('vplay','',Math.round(v.currentTime))});
    v.addEventListener('pause',function(){if(aud&&!v.ended&&Date.now()-tapT>900)ev('vpause','',Math.round(v.currentTime))});
    v.addEventListener('ended',function(){if(!aud)return;VS.end=1;VS.max=100;ev('vend','',Math.round(v.duration||0));ping();aud=false;v.controls=false;sc.classList.remove('aud')});
    v.addEventListener('seeked',function(){if(aud&&Date.now()-tapT>900&&Math.abs(v.currentTime-lastT)>2)ev('vseek',Math.round(lastT)+'>'+Math.round(v.currentTime),Math.round(v.currentTime))});
    v.addEventListener('volumechange',function(){if(!aud){wasMuted=v.muted;return}if(v.muted!==wasMuted){wasMuted=v.muted;ev('vmute',v.muted?'on':'off',Math.round(v.currentTime))}});
    v.addEventListener('ratechange',function(){if(aud)ev('vrate',String(v.playbackRate),Math.round(v.currentTime))});
    d.addEventListener('fullscreenchange',function(){if(aud&&d.fullscreenElement)ev('vfs','',Math.round(v.currentTime))});
    v.addEventListener('timeupdate',function(){if(!aud||!v.duration)return;var t=v.currentTime,dt=t-lastT;if(dt>0&&dt<1.5&&!v.paused)VS.secs+=dt;lastT=t;VS.dur=Math.round(v.duration);
      var p=t/v.duration*100;if(p>VS.max)VS.max=Math.min(100,Math.round(p));
      [10,25,50,75,95].forEach(function(m){if(p>=m&&!marks[m]){marks[m]=1;ev('vq','',m);if(m!==10)px(m===50?'ViewContent':'VSL'+m,{content_name:'VSL '+m+'%'},m!==50)}})});
  }

''' + s[b:]
n += 1
open(OUT, 'w', encoding='utf-8').write(s)
print('ok', n, len(s))
