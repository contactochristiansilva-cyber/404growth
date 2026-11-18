/* Páginas de empleo de 404 Growth (/equipo) · v77, 18/11/2026.
   La candidatura (pasos, borrador en el navegador, CV), la prueba técnica (/equipo/prueba/?t=…) y la entrevista (/equipo/entrevista/?t=…).
   Todo va al admin de 404 Growth (/l/job*), que la guarda, la puntúa con IA y avisa a Christian. */
(function(){
'use strict';
var D=document,H=D.documentElement,W=window,TZ='Europe/Madrid';
H.classList.add('js');
function $(s,r){return (r||D).querySelector(s)}function $$(s,r){return Array.prototype.slice.call((r||D).querySelectorAll(s))}
function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
function post(p,b,raw){return fetch('/l/'+p,{method:'POST',headers:{'content-type':raw?'application/pdf':'application/json'},body:raw||JSON.stringify(b)}).then(function(r){return r.json().catch(function(){return {}}).then(function(j){if(!r.ok){var e=new Error(j.error||'net');e.code=j.error||'net';e.data=j;throw e}return j})})}
var ls={get:function(k){try{return JSON.parse(localStorage.getItem(k)||'null')}catch(e){return null}},set:function(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}},del:function(k){try{localStorage.removeItem(k)}catch(e){}}};
var ss={get:function(k){try{return JSON.parse(sessionStorage.getItem(k)||'null')}catch(e){return null}},set:function(k,v){try{sessionStorage.setItem(k,JSON.stringify(v))}catch(e){}}};
var TICK='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5.5 12.5 4 4 9-9.5"/></svg>';
function day(ms,o){return new Intl.DateTimeFormat('es-ES',Object.assign({timeZone:TZ},o)).format(new Date(ms))}
function when(ms){return day(ms,{weekday:'long',day:'numeric',month:'long'})+' a las '+day(ms,{hour:'2-digit',minute:'2-digit'})}

/* prueba interna: los navegadores marcados con ?interno=1 (el mismo de la agenda y de /book; ?interno=0 lo quita). Las candidaturas salen
   en el admin como «Prueba interna», no cuentan en las cifras, se pueden repetir y la entrevista no crea evento en Google. */
var DEV=false;try{var iq=/[?&]interno=([01])/.exec(location.search);if(iq){if(iq[1]==='1')localStorage.setItem('c404int','1');else localStorage.removeItem('c404int')}DEV=!!localStorage.getItem('c404int')}catch(e){}
if(DEV){var bn=D.createElement('div');bn.className='devb';bn.innerHTML='<b>Prueba interna</b> · lo que envíes sale en el admin marcado como prueba y no cuenta en las cifras. <a href="?interno=0">Quitar</a>';var nv0=$('.nv');if(nv0&&nv0.parentNode)nv0.parentNode.insertBefore(bn,nv0.nextSibling);else D.body.insertBefore(bn,D.body.firstChild)}

/* la UTM de la primera visita (LinkedIn, Instagram…) viaja con la candidatura */
(function(){var q=new URLSearchParams(location.search),u={};['utm_source','utm_medium','utm_campaign','utm_content'].forEach(function(k){var v=q.get(k);if(v)u[k]=v.slice(0,80)});if(Object.keys(u).length)ss.set('eq:utm',u);if(!ss.get('eq:ref')&&D.referrer&&D.referrer.indexOf(location.host)<0)ss.set('eq:ref',D.referrer.slice(0,200))})();

/* cabecera y aparición */
var nv=$('.nv');if(nv){var onS=function(){nv.classList.toggle('on',W.scrollY>8)};W.addEventListener('scroll',onS,{passive:true});onS()}
if('IntersectionObserver' in W&&!(W.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches)){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -8% 0px'});$$('.rv').forEach(function(x){io.observe(x)})}else $$('.rv').forEach(function(x){x.classList.add('in')});

/* el enlace a la privacidad abre su desplegable */
D.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[href="#privacidad"]');if(a){var d=D.getElementById('privacidad');if(d)d.open=true}});

/* puestos abiertos o cerrados (lo decide Christian en el admin) */
var cfgEl=$('#eqcfg'),CFG=cfgEl?JSON.parse(cfgEl.textContent):null;
if($('[data-job]')||CFG)fetch('/l/jobs').then(function(r){return r.ok?r.json():null}).then(function(j){if(!j||!j.open)return;
  $$('[data-job]').forEach(function(a){var off=j.open[a.getAttribute('data-job')]===false;a.classList.toggle('off',off);var em=$('.k em',a);if(em)em.textContent=off?'Cerrado':'Abierto'});
  if(CFG&&j.open[CFG.slug]===false)closed()}).catch(function(){});
function closed(){var f=$('#fm');if(!f)return;f.innerHTML='<div class="closed"><p><b>Este puesto está cerrado ahora mismo.</b></p><p>Si quieres que te tengamos en cuenta para cuando lo volvamos a abrir, déjanos tu <a href="/equipo/abierta/#aplicar">candidatura abierta</a> y te escribimos los primeros.</p></div>';
  $$('[data-apply]').forEach(function(a){a.textContent='Puesto cerrado';a.setAttribute('href','/equipo/abierta/')})}

/* botón fijo en el móvil: solo cuando no se ven ni el de arriba ni el formulario */
var stk=$('.sticky');if(stk&&'IntersectionObserver' in W){var vis={};var o2=new IntersectionObserver(function(es){es.forEach(function(e){vis[e.target.id||'x']=e.isIntersecting});stk.classList.toggle('on',!vis.top&&!vis.aplicar&&W.scrollY>300)});['top','aplicar'].forEach(function(id){var x=D.getElementById(id);if(x)o2.observe(x)})}

/* ---------- la candidatura ---------- */
var fm=$('#fm');
if(fm&&CFG){
  var KEY='eq:'+CFG.slug,steps=$$('.fs',fm),N=steps.length,cur=1,file=null,busy=false;
  var Q={};CFG.qs.forEach(function(q){Q[q.id]=q});
  var val=function(id){var q=Q[id];if(!q)return '';if(q.type==='choice'||q.type==='yesno'){var c=$('input[name="'+id+'"]:checked',fm);return c?c.value:''}var x=$('[name="'+id+'"]',fm);return x?x.value.trim():''};
  var answers=function(){var a={};CFG.qs.forEach(function(q){if(q.type!=='file'){var v=val(q.id);if(v)a[q.id]=v}});return a};
  var okUrl=function(v){return /^(https?:\/\/)?[^\s\/]+\.[^\s]{2,}/i.test(v)};
  var okTel=function(v){var t=v.replace(/[^\d+]/g,'');if(t.indexOf('00')===0)t='+'+t.slice(2);if(/^[6789]\d{8}$/.test(t))return true;return /^\+\d{9,15}$/.test(t)};
  var check=function(q){var v=val(q.id),need=q.req||(q.id==='portfolio'&&CFG.portfolio==='req')||(q.id==='video'&&CFG.video==='req');
    if(q.type==='file')return !file||(file.size<=1800000&&/pdf$/i.test(file.type||file.name));
    if(!v)return !need;
    if(q.type==='email')return /^[^\s@,;<>"']+@[^\s@,;<>"']+\.[^\s@,;<>"']{2,}$/.test(v);
    if(q.type==='tel')return okTel(v);
    if(q.type==='url')return okUrl(v);
    if(q.type==='long')return v.length>=15;
    if(q.type==='text'&&need)return v.length>=2;
    return true};
  var mark=function(id,bad){var f=$('[data-f="'+id+'"]',fm);if(f)f.classList.toggle('err',!!bad)};
  var pr=$('.fm-pr i',fm),lab=$('.fm-top span',fm),ttl=$('.fm-top b',fm);
  var go=function(n,focus){cur=Math.max(1,Math.min(N,n));steps.forEach(function(s,i){s.classList.toggle('on',i===cur-1)});
    if(pr)pr.style.width=(cur/N*100)+'%';if(lab)lab.textContent='Paso '+cur+' de '+N;if(ttl)ttl.textContent=CFG.steps[cur-1];
    $('[data-prev]',fm).hidden=cur===1;$('[data-next]',fm).hidden=cur===N;$('[data-send]',fm).hidden=cur!==N;
    if(focus){var top=fm.getBoundingClientRect().top+W.scrollY-90;if(Math.abs(W.scrollY-top)>40)W.scrollTo({top:top,behavior:'smooth'});var first=$('.fs.on input:not([type=hidden]),.fs.on textarea',fm);if(first)setTimeout(function(){try{first.focus({preventScroll:true})}catch(e){}},250)}
    save()};
  var stepOk=function(n){var bad=null;CFG.qs.forEach(function(q){if(q.step!==n)return;var ok=check(q);mark(q.id,!ok);if(!ok&&!bad)bad=q.id});return bad};
  var save=function(){ls.set(KEY,{a:answers(),s:cur,keep:!!($('[name=keep]',fm)||{}).checked,at:Date.now()})};
  /* el borrador: lo que llevaba escrito, si vuelve en menos de 14 días */
  var dr=ls.get(KEY);if(dr&&dr.a&&Date.now()-(dr.at||0)<14*864e5){Object.keys(dr.a).forEach(function(k){var q=Q[k];if(!q)return;if(q.type==='choice'||q.type==='yesno'){var r=$('input[name="'+k+'"][value="'+String(dr.a[k]).replace(/"/g,'')+'"]',fm);if(r)r.checked=true}else{var x=$('[name="'+k+'"]',fm);if(x)x.value=dr.a[k]}});if(dr.keep&&$('[name=keep]',fm))$('[name=keep]',fm).checked=true}
  var cnt=function(t){var c=t.parentNode.querySelector('.cnt');if(c)c.textContent=t.value.length+' / '+t.maxLength};$$('textarea',fm).forEach(cnt);
  fm.addEventListener('input',function(e){var t=e.target;if(t.tagName==='TEXTAREA')cnt(t);var f=t.closest('.fd');if(f&&f.classList.contains('err')){var q=Q[f.getAttribute('data-f')];if(q&&check(q))f.classList.remove('err')}save()});
  fm.addEventListener('change',function(e){var t=e.target;if(t.type==='file'){var f=t.files&&t.files[0];file=f||null;var fn=$('.fn',t.closest('.fd'));if(fn)fn.textContent=f?f.name+' · '+(f.size/1048576).toFixed(1).replace('.',',')+' MB':'Ningún archivo';mark('cv',f&&!check(Q.cv));return}
    var fd=t.closest('.fd');if(fd&&fd.classList.contains('err')){var q=Q[fd.getAttribute('data-f')];if(q&&check(q))fd.classList.remove('err')}if(t.name==='consent'&&t.checked){$('.cks .c1',fm).classList.remove('err');$('.fmsg',fm).textContent=''}save()});
  fm.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;
    if(b.hasAttribute('data-next')){e.preventDefault();var bad=stepOk(cur);if(bad){var el=$('[data-f="'+bad+'"] input,[data-f="'+bad+'"] textarea',fm);if(el)el.focus();return}go(cur+1,true)}
    if(b.hasAttribute('data-prev')){e.preventDefault();go(cur-1,true)}});
  fm.addEventListener('submit',function(e){e.preventDefault();if(busy)return;var msg=$('.fmsg',fm);msg.textContent='';
    for(var n=1;n<=N;n++){var bad=stepOk(n);if(bad){go(n,true);msg.textContent='Revisa lo que está marcado en rojo.';return}}
    var c1=$('[name=consent]',fm);if(!c1.checked){$('.cks .c1',fm).classList.add('err');msg.textContent='Marca la casilla de la privacidad para poder enviarla.';return}
    busy=true;var btn=$('[data-send]',fm);btn.disabled=true;btn.textContent='Enviando…';
    var body={job:CFG.slug,dev:DEV?1:0,a:answers(),consent:true,keep:!!($('[name=keep]',fm)||{}).checked,web:($('[name=web]',fm)||{}).value||'',utm:ss.get('eq:utm')||{},ref:ss.get('eq:ref')||''};
    post('job',body).then(function(r){var name=(body.a.name||'').split(/\s+/)[0];
      var fin=function(cvOk){ls.del(KEY);fm.innerHTML='<div class="done" role="status"><div class="tick">'+TICK+'</div><h3>Recibida, '+esc(name)+'.</h3><p>Gracias por tu tiempo. Te contestamos en menos de 24 horas'+(CFG.test?'. Si encajas, el siguiente paso es una videollamada de 30 minutos con Christian, el día y la hora que tú elijas.':'.')+'</p>'+(cvOk===false?'<p>Tu CV no se pudo subir. No pasa nada: si te interesa que lo veamos, mándalo respondiendo al correo que te escribamos.</p>':'')+'<p class="mut">Mientras, puedes ver <a href="/equipo/">los demás puestos</a> o cómo trabajamos en <a href="/">404growth.com</a>.</p></div>';fm.scrollIntoView({behavior:'smooth',block:'center'})};
      if(file&&r.cvt)post('jobcv?c='+encodeURIComponent(r.cvt),null,file).then(function(){fin(true)},function(){fin(false)});else fin()},
    function(err){busy=false;btn.disabled=false;btn.textContent='Enviar candidatura';
      if(err.code==='fields'&&err.data&&err.data.fields){var f=err.data.fields,st=N;f.forEach(function(id){mark(id,true);if(Q[id]&&Q[id].step<st)st=Q[id].step});go(st,true);msg.textContent='Revisa lo que está marcado en rojo.';return}
      if(err.code==='closed'){closed();return}
      msg.textContent=({dup:'Ya tenemos una candidatura tuya para este puesto: te contestamos en menos de 24 horas.',slow:'Se han enviado varias candidaturas hoy desde esta conexión. Prueba mañana o escríbenos.',consent:'Marca la casilla de la privacidad para poder enviarla.'})[err.code]||'No se ha podido enviar. Revisa la conexión e inténtalo otra vez: no se ha perdido nada.'})});
  go(dr&&dr.s?Math.min(dr.s,N):1,false);
}

/* ---------- la prueba técnica ---------- */
var pz=$('#pz');
if(pz){var t=new URLSearchParams(location.search).get('t')||'';
  var bad=function(m){pz.innerHTML='<p class="closed">'+m+'</p>'};
  if(!t)bad('Falta el código de tu prueba. Abre el enlace del mensaje que te mandamos.');
  else post('jobt',{t:t}).then(function(r){var T=r.test,late=r.due&&r.due<Date.now();
    $('#pz-h').innerHTML='Hola, '+esc(r.name)+'. <span class="lm">Tu prueba técnica.</span>';$('#pz-l').textContent=r.job+' · '+T.title;
    pz.innerHTML='<div class="due'+(late?' late':'')+'">'+(r.due?(late?'El plazo terminó el ':'Tienes hasta el ')+esc(when(r.due)):'Sin fecha límite')+' · '+T.hours+' '+(T.hours===1?'hora':'horas')+' como máximo</div>'+
      '<div class="tg"><div class="box brief"><h3>Qué hay que hacer</h3>'+T.brief.map(function(p){return '<p>'+esc(p)+'</p>'}).join('')+'<p class="sub">Qué nos entregas</p><ul class="ck">'+T.deliver.map(function(x){return '<li>'+esc(x)+'</li>'}).join('')+'</ul></div>'+
      '<form class="fm" id="pzf" novalidate>'+(r.done?'<p class="closed" style="margin-bottom:18px"><b>Ya la entregaste el '+esc(when(r.done))+'.</b> Si quieres, puedes mandar una versión nueva: sustituye a la anterior.</p>':'')+
      '<div class="fd"><span class="lb">Enlaces <em>(tu tienda, documento, carpeta, audio…)</em></span><div class="lnks">'+[0,1,2].map(function(i){return '<input type="url" inputmode="url" name="l" placeholder="https://" maxlength="300" aria-label="Enlace '+(i+1)+'">'}).join('')+'</div><button class="addl" type="button">+ Añadir otro enlace</button></div>'+
      '<div class="fd"><label for="pz-t">Tu explicación <em>(y contraseñas, si hacen falta)</em></label><textarea id="pz-t" name="text" maxlength="8000" placeholder="Lo que quieras contarnos de tu entrega"></textarea><span class="cnt"></span></div>'+
      '<button class="b-pri" type="submit" style="width:100%">Entregar la prueba</button><p class="fmsg" role="alert"></p></form></div>';
    var f=$('#pzf'),k='eq:pz:'+t.split('.')[0],sv=ls.get(k);if(sv){var ins=$$('[name=l]',f);(sv.l||[]).forEach(function(v,i){if(!ins[i]){var x=D.createElement('input');x.type='url';x.name='l';x.maxLength=300;x.placeholder='https://';$('.lnks',f).appendChild(x);ins.push(x)}ins[i].value=v});$('[name=text]',f).value=sv.text||''}
    var cn=function(){var a=$('[name=text]',f);$('.cnt',f).textContent=a.value.length+' / 8000'};cn();
    f.addEventListener('input',function(){cn();ls.set(k,{l:$$('[name=l]',f).map(function(x){return x.value}),text:$('[name=text]',f).value})});
    $('.addl',f).addEventListener('click',function(){if($$('[name=l]',f).length>=6)return;var x=D.createElement('input');x.type='url';x.name='l';x.maxLength=300;x.placeholder='https://';$('.lnks',f).appendChild(x);x.focus()});
    f.addEventListener('submit',function(e){e.preventDefault();var links=$$('[name=l]',f).map(function(x){return x.value.trim()}).filter(Boolean),text=$('[name=text]',f).value.trim(),m=$('.fmsg',f);
      if(!links.length&&text.length<30){m.textContent='Añade al menos un enlace o explica tu entrega.';return}
      var b=$('button[type=submit]',f);b.disabled=true;b.textContent='Enviando…';
      post('jobts',{t:t,links:links,text:text}).then(function(){ls.del(k);f.innerHTML='<div class="done" role="status"><div class="tick">'+TICK+'</div><h3>Entregada.</h3><p>Gracias, '+esc(r.name)+'. Christian la revisa y te escribimos en menos de 24 horas con el siguiente paso.</p></div>'},
        function(err){b.disabled=false;b.textContent='Entregar la prueba';m.textContent=err.code==='closed'?'Esta prueba ya no está abierta.':err.code==='fields'?'Añade al menos un enlace o explica tu entrega.':'No se ha podido enviar. Inténtalo otra vez: no se ha perdido nada.'})})},
  function(err){bad(err.code==='closed'?'Esta prueba ya no está abierta. Si crees que es un error, contesta al mensaje que te mandamos.':'Este enlace no es válido o ya no está activo. Si crees que es un error, contesta al mensaje que te mandamos.')})}

/* ---------- la entrevista ---------- */
var iv=$('#iv');
if(iv){var tk=new URLSearchParams(location.search).get('t')||'',S={d:null,h:null,slots:[]};
  var msg=function(m){iv.innerHTML='<p class="closed">'+m+'</p>'};
  var local=(function(){try{return Intl.DateTimeFormat().resolvedOptions().timeZone}catch(e){return TZ}})();
  var ymd=function(ms){return day(ms,{year:'numeric',month:'2-digit',day:'2-digit'})};
  var draw=function(){var by={};S.slots.forEach(function(s){var ms=Date.parse(s),k=ymd(ms);(by[k]=by[k]||[]).push(ms)});var ks=Object.keys(by).slice(0,10);
    if(!ks.length){msg('Ahora mismo no quedan horas libres. Contesta al mensaje que te mandamos y la buscamos juntos.');return}
    if(!S.d||!by[S.d])S.d=ks[0];
    iv.innerHTML='<div class="fm"><span class="lb" style="display:block;font-weight:650;margin-bottom:12px">Elige el día</span><div class="days" role="group" aria-label="Días">'+ks.map(function(k){var ms=by[k][0];return '<button type="button" data-d="'+k+'" aria-pressed="'+(k===S.d)+'"><small>'+esc(day(ms,{weekday:'short'}))+'</small><b>'+esc(day(ms,{day:'numeric'}))+'</b><small>'+esc(day(ms,{month:'short'}))+'</small></button>'}).join('')+'</div>'+
      '<span class="lb" style="display:block;font-weight:650;margin:22px 0 0">Y la hora <em class="mut" style="font-style:normal;font-weight:500">(hora de España)</em></span><div class="hours" role="group" aria-label="Horas">'+by[S.d].map(function(ms){return '<button type="button" data-h="'+ms+'" aria-pressed="'+(S.h===ms)+'">'+esc(day(ms,{hour:'2-digit',minute:'2-digit'}))+'</button>'}).join('')+'</div>'+
      (local&&local!==TZ&&S.h?'<p class="tz">En tu hora ('+esc(local.replace(/_/g,' '))+'): '+esc(new Intl.DateTimeFormat('es-ES',{timeZone:local,weekday:'long',hour:'2-digit',minute:'2-digit'}).format(new Date(S.h)))+'</p>':'')+
      '<button class="b-pri" type="button" data-ok style="width:100%;margin-top:22px"'+(S.h?'':' disabled')+'>'+(S.h?'Confirmar: '+esc(when(S.h)):'Elige una hora')+'</button><p class="fmsg" role="alert"></p></div>'};
  var load=function(note){post('jobm',{t:tk}).then(function(r){$('#iv-h').innerHTML='Hola, '+esc(r.name)+'. <span class="lm">Elige cuándo hablamos.</span>';$('#iv-l').textContent='Videollamada de '+r.dur+' minutos con Christian sobre el puesto de '+r.job+'. Al confirmar, te llega la invitación de Google con el enlace de Meet.';
      if(r.booked&&r.booked.start>Date.now()){iv.innerHTML='<div class="fm done"><div class="tick">'+TICK+'</div><h3>Ya tienes tu entrevista.</h3><p>'+esc(when(r.booked.start))+' (hora de España).</p>'+(r.booked.join?'<p><a class="b-gl" href="'+esc(r.booked.join)+'" target="_blank" rel="noopener">Enlace de Meet</a></p>':'')+'<p class="mut">Si necesitas cambiarla, contesta al mensaje que te mandamos.</p></div>';return}
      S.slots=r.slots||[];draw();if(note){var m=$('.fmsg',iv);if(m)m.textContent=note}},
    function(err){msg(err.code==='closed'?'Esta invitación ya no está abierta. Si crees que es un error, contesta al mensaje que te mandamos.':err.code==='nocal'?'Ahora mismo no podemos enseñarte las horas. Contesta al mensaje que te mandamos y la cerramos a mano.':'Este enlace no es válido o ya no está activo. Si crees que es un error, contesta al mensaje que te mandamos.')})};
  if(!tk)msg('Falta el código de tu invitación. Abre el enlace del mensaje que te mandamos.');else load();
  iv.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;
    if(b.hasAttribute('data-d')){S.d=b.getAttribute('data-d');S.h=null;draw();return}
    if(b.hasAttribute('data-h')){S.h=+b.getAttribute('data-h');draw();var ok=$('[data-ok]',iv);if(ok&&W.innerWidth<900)ok.scrollIntoView({behavior:'smooth',block:'center'});return}
    if(b.hasAttribute('data-ok')&&S.h){b.disabled=true;b.textContent='Reservando…';post('jobmb',{t:tk,start:new Date(S.h).toISOString()}).then(function(r){iv.innerHTML='<div class="fm done" role="status"><div class="tick">'+TICK+'</div><h3>Hecho. Hablamos el '+esc(when(Date.parse(r.start)))+'.</h3>'+(r.dev?'<p><b>Prueba interna:</b> no se ha creado el evento en Google ni se ha mandado invitación.</p>':'<p>Te llega ahora la invitación de Google Calendar con el enlace de Meet: acéptala para que quede en tu calendario.</p>')+'</div>'},
      function(err){if(err.code==='taken'){S.h=null;load('Esa hora se acaba de ocupar. Elige otra.');return}if(err.code==='booked'){load();return}b.disabled=false;b.textContent='Confirmar: '+when(S.h);var m=$('.fmsg',iv);if(m)m.textContent='No se ha podido reservar. Inténtalo otra vez o contesta al mensaje que te mandamos.'})}})}
})();
