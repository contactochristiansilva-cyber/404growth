/* cargador 404 (v68b): el 404 se dibuja con calma, respira y vuela en arco hasta el logo de la cabecera con una estela; allí sale «404 Growth».
   El reloj empieza cuando la página ya se ha pintado, para que en el móvil se vea desde el principio. */
(function(){var l=D.getElementById('l404');if(!l){H.classList.remove('l404');return}
var w=l.querySelector('.lw'),t=D.querySelector('.nv .nv-logo .mk'),done=0;
function end(ms){setTimeout(function(){H.classList.remove('l404','l404-land');l.remove()},ms)}
function soft(){if(done)return;done=1;w.style.transition='opacity .4s';w.style.opacity='0';l.classList.add('go');H.classList.add('l404-land');end(700)}
if(rm){l.querySelectorAll('.l4s').forEach(function(p){p.style.strokeDashoffset=0});setTimeout(soft,500);return}
setTimeout(soft,6000);   /* por si algo falla, nunca se queda tapando la página */
function fly(){if(done)return;var b=t&&t.getBoundingClientRect();if(!b||!b.width){soft();return}done=1;
 var y=w.querySelector('.ly'),a=w.getBoundingClientRect(),s=b.width/a.width,
  tx=b.left+b.width/2-a.left-a.width*s/2,ty=b.top+b.height/2-a.top-a.height*s/2,o=l.getBoundingClientRect(),gs=[];
 [.26,.17,.11,.06].forEach(function(op,i){var g=w.cloneNode(true);g.classList.add('gh');g.style.width=a.width+'px';g.style.left=(a.left-o.left)+'px';g.style.top=(a.top-o.top)+'px';w.parentNode.insertBefore(g,w);gs.push([g,op,i])});
 l.classList.remove('br');l.classList.add('go');
 var DX='transform .85s cubic-bezier(.55,0,.2,1)',DY='transform .85s cubic-bezier(.3,0,.25,1)';   /* x e y con curvas distintas: vuela en arco */
 function move(el,d){var yy=el.querySelector('.ly');el.style.transition=DX+(d?' '+d+'ms':'')+',opacity .28s ease';yy.style.transition=DY+(d?' '+d+'ms':'');
  el.style.transform='translateX('+tx+'px)';yy.style.transform='translateY('+ty+'px) scale('+s+')'}
 requestAnimationFrame(function(){requestAnimationFrame(function(){move(w,0);
  gs.forEach(function(x){move(x[0],45*(x[2]+1));x[0].style.opacity=x[1]})})});
 var landed=0;function land(){if(landed)return;landed=1;H.classList.add('l404-land');w.style.opacity='0';
  gs.forEach(function(x){x[0].style.opacity='0'});
  var lg=t.parentNode,r=lg.getBoundingClientRect(),h=D.createElement('i');h.className='hit';h.style.left=(b.left-r.left+b.width/2)+'px';h.style.top=(b.top-r.top+b.height/2)+'px';
  lg.appendChild(h);setTimeout(function(){h.remove()},900);end(840)}
 y.addEventListener('transitionend',function(e){if(e.target===y&&e.propertyName==='transform')land()});setTimeout(land,1250)}
requestAnimationFrame(function(){requestAnimationFrame(function(){l.classList.add('run');
 setTimeout(function(){l.classList.add('br')},950);
 setTimeout(fly,1320)})})})();
