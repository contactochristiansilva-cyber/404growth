(function(){
var H=document.documentElement,D=document,rm=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
try{D.getElementById('yr').textContent=new Date().getFullYear()}catch(e){}

/* cargador 404: se dibuja y vuela al logo de la cabecera */
(function(){var l=D.getElementById('l404');if(!l){H.classList.remove('l404');return}
function end(ms){setTimeout(function(){H.classList.remove('l404','l404-land');l.remove()},ms)}
setTimeout(function(){var w=l.querySelector('.lw'),t=D.querySelector('.nv .nv-logo .mk'),b=t&&t.getBoundingClientRect();
 if(!b||rm||!b.width){w.style.transition='opacity .4s';w.style.opacity='0';l.classList.add('fly');H.classList.add('l404-land');end(700);return}
 var a=w.getBoundingClientRect();
 w.style.transition='transform .85s cubic-bezier(.65,0,.2,1),opacity .35s ease .6s';
 w.style.transform='translate('+(b.left-a.left)+'px,'+(b.top-a.top)+'px) scale('+(b.width/a.width)+','+(b.height/a.height)+')';
 l.classList.add('fly');
 setTimeout(function(){H.classList.add('l404-land');w.style.opacity='0'},700);
 end(1150)},rm?400:1700)})();

/* cabecera: más opaca al bajar */
var nv=D.getElementById('nv');function sc(){nv.classList.toggle('sc',scrollY>40)}sc();addEventListener('scroll',sc,{passive:true});

/* menú del móvil */
var mb=D.querySelector('.nv-mb'),mm=D.getElementById('mm');
function menu(o){mm.hidden=!o;mb.setAttribute('aria-expanded',o?'true':'false');mb.setAttribute('aria-label',o?'Cerrar menú':'Abrir menú')}
if(mb&&mm){mb.addEventListener('click',function(){menu(mm.hidden)});mm.addEventListener('click',function(e){if(e.target.closest('a'))menu(false)});D.addEventListener('keydown',function(e){if(e.key==='Escape')menu(false)})}

/* aparición al hacer scroll (solo transform y opacity) */
var io='IntersectionObserver' in window;
if(io&&!rm){var ob=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');ob.unobserve(e.target)}})},{rootMargin:'0px 0px -8% 0px',threshold:.12});D.querySelectorAll('.rv,.bars').forEach(function(el){ob.observe(el)})}
else D.querySelectorAll('.rv,.bars').forEach(function(el){el.classList.add('in')});

/* mapa: las rutas solo se mueven mientras se ve */
var map=D.getElementById('map');if(map&&io){new IntersectionObserver(function(es){map.classList.toggle('in',es[0].isIntersecting)},{threshold:.15}).observe(map)}

/* tiendas de ejemplo: cambiar la vista previa (sin enlaces a las tiendas) */
(function(){var L;try{L=JSON.parse(D.getElementById('tnd-data').textContent)}catch(e){return}
var bs=D.querySelectorAll('.ts'),im=D.getElementById('pvi'),pn=D.getElementById('pvn'),pd=D.getElementById('pvd'),ps=D.getElementById('pvs'),pre=0;
function preload(){if(pre)return;pre=1;L.forEach(function(s){var i=new Image();i.src='/demos/cards/'+s[0]+'.webp'})}
function pick(k){var s=L[k];bs.forEach(function(b,j){var on=j===k;b.classList.toggle('on',on);b.setAttribute('aria-selected',on?'true':'false')});
 im.classList.add('ld');var n=new Image();n.onload=function(){im.src=n.src;im.alt='Tienda de demostración '+s[1];requestAnimationFrame(function(){im.classList.remove('ld')})};n.src='/demos/cards/'+s[0]+'.webp';
 pn.textContent=s[1];pd.textContent=s[3];ps.textContent=s[2]}
bs.forEach(function(b){b.addEventListener('click',function(){pick(+b.dataset.i)});b.addEventListener('pointerenter',preload,{once:true});b.addEventListener('focus',preload,{once:true})});
D.querySelector('.tnd-list').addEventListener('keydown',function(e){var k=[].indexOf.call(bs,D.activeElement);if(k<0)return;var n=e.key==='ArrowDown'||e.key==='ArrowRight'?k+1:e.key==='ArrowUp'||e.key==='ArrowLeft'?k-1:-9;if(n===-9)return;e.preventDefault();n=(n+bs.length)%bs.length;bs[n].focus();pick(n)})})();

/* desplegables: uno abierto cada vez (por si el navegador no entiende name en <details>) */
D.querySelectorAll('details[name]').forEach(function(d){d.addEventListener('toggle',function(){if(!d.open)return;D.querySelectorAll('details[name="'+d.getAttribute('name')+'"]').forEach(function(o){if(o!==d&&o.open)o.open=false})})});

/* WhatsApp flotante: se esconde mientras se ven los botones de la portada; el degradado inferior, al llegar al pie */
var waf=D.querySelector('.waf'),hb=D.getElementById('hero-btns'),fd=D.querySelector('.fade'),ft=D.querySelector('.ft');
if(io&&waf&&hb)new IntersectionObserver(function(e){waf.classList.toggle('off',e[0].isIntersecting)}).observe(hb);
if(io&&fd&&ft)new IntersectionObserver(function(e){fd.classList.toggle('off',e[0].isIntersecting)}).observe(ft);

/* scroll lento con Lenis, solo con ratón o trackpad (en pantallas táctiles, el scroll del sistema) */
function lenis(){if(rm||!window.Lenis||!matchMedia('(hover: hover) and (pointer: fine)').matches)return;
 try{window.__lenis=new Lenis({duration:1.45,easing:function(t){return Math.min(1,1.001-Math.pow(2,-10*t))},wheelMultiplier:.85,anchors:true,autoRaf:true})}catch(e){}}
if(D.readyState==='loading')D.addEventListener('DOMContentLoaded',lenis);else lenis();
})();
