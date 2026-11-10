/* cargador 404 (v68): se dibuja, carga, onda supersónica y aterriza en el logo de la cabecera, que suelta «404 Growth» */
(function(){var l=D.getElementById('l404');if(!l){H.classList.remove('l404');return}
var w=l.querySelector('.lw'),t=D.querySelector('.nv .nv-logo .mk');
function end(ms){setTimeout(function(){H.classList.remove('l404','l404-land');l.remove()},ms)}
function soft(){w.style.transition='opacity .35s';w.style.opacity='0';l.classList.add('go');H.classList.add('l404-land');end(600)}
if(rm){setTimeout(soft,500);return}
setTimeout(function(){l.classList.add('chg')},640);
setTimeout(function(){var b=t&&t.getBoundingClientRect();if(!b||!b.width){soft();return}
 var a=w.getBoundingClientRect(),s=b.width/a.width,
  tx=b.left+b.width/2-a.left-a.width*s/2,ty=b.top+b.height/2-a.top-a.height*s/2,
  ang=Math.atan2(ty+a.height*s/2-a.height/2,tx+a.width*s/2-a.width/2)*180/Math.PI,
  T='translate('+tx+'px,'+ty+'px) scale('+s+')',sp=l.querySelector('.sp');
 if(sp)sp.style.transform='rotate('+ang+'deg)';
 var gs=[];[.42,.24,.12].forEach(function(o,i){var g=w.cloneNode(true);g.classList.add('gh');g.style.width=a.width+'px';
  g.style.left=(a.left-l.getBoundingClientRect().left)+'px';g.style.top=(a.top-l.getBoundingClientRect().top)+'px';
  w.parentNode.insertBefore(g,w);gs.push([g,o,i])});
 l.classList.remove('chg');l.classList.add('boom','go');
 requestAnimationFrame(function(){requestAnimationFrame(function(){
  w.style.transition='transform .5s cubic-bezier(.6,0,.1,1)';w.style.transform=T;
  gs.forEach(function(x){var g=x[0],d=40+x[2]*35;g.style.transition='transform .5s cubic-bezier(.6,0,.1,1) '+d+'ms,opacity .12s ease '+d+'ms';g.style.opacity=x[1];g.style.transform=T})})});
 setTimeout(function(){H.classList.add('l404-land');w.style.transition='none';w.style.opacity='0';
  gs.forEach(function(x){x[0].style.transition='opacity .14s';x[0].style.opacity='0'});
  var lg=t.parentNode,h=D.createElement('i');h.className='hit';h.style.left=(b.left-lg.getBoundingClientRect().left+b.width/2)+'px';h.style.top=(b.top-lg.getBoundingClientRect().top+b.height/2)+'px';
  lg.appendChild(h);setTimeout(function(){h.remove()},700)},520);
 end(1250)},880)})();
