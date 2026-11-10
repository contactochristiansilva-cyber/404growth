/* cargador 404 (v68c): solo el logo. Se dibuja desde cero; luego vuela en arco al logo de la cabecera deshaciéndose por el camino,
   mientras el de la cabecera se dibuja, y sale «404 Growth». El reloj empieza cuando la página ya se ha pintado. */
(function(){var l=D.getElementById('l404');if(!l){H.classList.remove('l404');return}
var w=l.querySelector('.lw'),t=D.querySelector('.nv .nv-logo .mk'),done=0;
if(t)t.querySelectorAll('rect,path').forEach(function(p){p.setAttribute('pathLength','1')});
function end(ms){setTimeout(function(){H.classList.remove('l404','l404-draw','l404-land');l.remove()},ms)}
function soft(){if(done)return;done=1;w.style.transition='opacity .4s';w.style.opacity='0';l.classList.add('go');H.classList.add('l404-draw','l404-land');end(1100)}
if(rm){setTimeout(soft,400);return}
setTimeout(soft,6000);   /* por si algo falla, nunca se queda tapando la página */
function fly(){if(done)return;var b=t&&t.getBoundingClientRect();if(!b||!b.width){soft();return}done=1;
 var y=w.querySelector('.ly'),a=w.getBoundingClientRect(),s=b.width/a.width,
  tx=b.left+b.width/2-a.left-a.width*s/2,ty=b.top+b.height/2-a.top-a.height*s/2;
 l.classList.add('go');
 requestAnimationFrame(function(){requestAnimationFrame(function(){   /* x e y con curvas distintas: vuela en arco */
  w.style.transition='transform .95s cubic-bezier(.55,0,.2,1)';y.style.transition='transform .95s cubic-bezier(.3,0,.25,1)';
  w.style.transform='translateX('+tx+'px)';y.style.transform='translateY('+ty+'px) scale('+s+')'})});
 setTimeout(function(){H.classList.add('l404-draw')},420);
 setTimeout(function(){H.classList.add('l404-land')},900);
 end(1900)}
requestAnimationFrame(function(){requestAnimationFrame(function(){l.classList.add('run');setTimeout(fly,1150)})})})();
