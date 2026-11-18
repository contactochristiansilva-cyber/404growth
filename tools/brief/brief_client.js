  /* ---------- v78 · Briefs: lo que nos cuentan los clientes en su formulario (404growth.com/brief/<id>/) ---------- */
  var BR={open:null,hide:false,last:null};
  function brWhen(ms){return ms?new Date(ms).toLocaleString('es-ES',{timeZone:'Europe/Madrid',day:'numeric',month:'short',hour:'2-digit',minute:'2-digit'}):''}
  function brSize(n){return n>=1048576?(n/1048576).toFixed(1).replace('.',',')+' MB':Math.max(1,Math.round(n/1024))+' KB'}
  function brState(b){return b.sent?'<span class="br-ch ok">Enviado el '+esc(brWhen(b.sent))+'</span>':b.started?'<span class="br-ch md">Rellenándolo</span>':'<span class="br-ch">Sin empezar</span>'}
  function brAns(q,d){var v=d[q.id],o=d[q.id+'_o'],p=d[q.id+'__p'],out='';
    if(q.type==='confirm'){out=v==='ok'?'Está bien así':v==='cambiar'?'Hay que cambiarlo'+(o?': '+o:''):''}
    else if(q.type==='many'){var L=(v||[]).map(function(x){return x==='Otro'&&o?'Otro: '+o:x});out=L.join(' · ')}
    else if(q.type==='one'){out=v==='Otro'&&o?'Otro: '+o:(v||'')}
    else if(q.type==='date'&&v){var t=new Date(v+'T12:00:00');out=isNaN(t)?v:t.toLocaleDateString('es-ES',{weekday:'long',day:'numeric',month:'long',year:'numeric'})}
    else out=v==null?'':String(v);
    return {t:String(out).trim(),p:!!p}}
  var BR_CSS='<style>#br .br-list{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:10px;margin-top:12px}#br .br-c{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:16px;display:flex;flex-direction:column;gap:8px}#br .br-c b{font-size:15.5px}#br .br-m{font-size:12.5px;color:var(--mute)}'+
    '#br .br-ch{display:inline-block;font-size:11.5px;font-weight:700;padding:2px 8px;border-radius:99px;background:var(--surface-2);color:var(--mute)}#br .br-ch.ok{background:var(--ok-soft);color:var(--ok)}#br .br-ch.md{background:var(--warn-soft);color:var(--warn)}'+
    '#br .br-bar{height:6px;border-radius:6px;background:var(--surface-2);overflow:hidden}#br .br-bar i{display:block;height:100%;background:var(--ok)}#br .br-acts{display:flex;gap:6px;flex-wrap:wrap}'+
    '#br .br-sec{margin-top:14px}#br .br-sec h3{font-size:16px;margin:0 0 10px;display:flex;gap:10px;align-items:baseline}#br .br-sec h3 small{color:var(--mute);font-weight:600;font-size:12.5px}'+
    '#br .br-q{display:grid;grid-template-columns:minmax(0,2fr) minmax(0,3fr);gap:6px 18px;padding:10px 0;border-top:1px solid var(--line)}#br .br-q:first-of-type{border-top:0}#br .br-q dt{font-size:13px;color:var(--mute);font-weight:600}#br .br-q dd{margin:0;font-size:14.5px;white-space:pre-wrap;overflow-wrap:anywhere}#br .br-q dd.no{color:var(--mute);font-style:italic}'+
    '#br .br-pend{font-size:11px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;background:var(--warn-soft);color:var(--warn);border-radius:6px;padding:2px 6px;margin-right:6px}'+
    '#br .br-files{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:8px}#br .br-f{border:1px solid var(--line);border-radius:12px;padding:8px;display:flex;flex-direction:column;gap:6px;min-width:0;text-decoration:none;color:var(--ink)}#br .br-f img{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:8px;background:var(--surface-2)}#br .br-f span{font-size:12.5px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}#br .br-f small{color:var(--mute);font-size:11.5px}#br .br-ph{width:100%;aspect-ratio:4/3;border-radius:8px;background:var(--surface-2);display:flex;align-items:center;justify-content:center;font-weight:800;font-size:12px;color:var(--mute)}'+
    '#br .br-top{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin:8px 0 4px}#br .br-tog{display:inline-flex;gap:8px;align-items:center;font-size:13px;color:var(--mute)}'+
    '@media (max-width:640px){#br .br-q{grid-template-columns:1fr;gap:2px}}</style>';
  function vBrief(){if(BR.open)return brDet();return api('GET','brief').then(function(d){var L=d.briefs||[];
    return BR_CSS+'<div id="br"><div class="head"><h2>Briefs</h2><p>Los formularios que mandas a un cliente para que te cuente su proyecto. Cada uno tiene su enlace privado: lo rellenan entre varios, se guarda solo y te avisa al móvil cuando empiezan y cuando lo envían.</p></div>'+
      (d.files?'':'<p class="hint">R2 no está conectado: el formulario no deja subir archivos (sí el enlace a una carpeta).</p>')+
      (L.length?'<div class="br-list">'+L.map(function(b){var pc=b.tot?Math.round(b.n*100/b.tot):0;
        return '<div class="br-c"><b>'+esc(b.name)+'</b><div>'+brState(b)+'</div><div class="br-bar" aria-hidden="true"><i style="width:'+pc+'%"></i></div>'+
          '<p class="br-m">'+b.n+' de '+b.tot+' preguntas · '+b.files+' '+(b.files===1?'archivo':'archivos')+(b.upd?' · último cambio '+esc(brWhen(b.upd)):'')+(b.who?' · '+esc(b.who):'')+'</p>'+
          '<div class="br-acts"><button class="btn sm pri" type="button" data-br="open" data-brid="'+esc(b.id)+'">Ver respuestas</button><button class="btn sm" type="button" data-br="copy" data-brl="'+esc(b.link)+'">Copiar enlace para el cliente</button><a class="btn sm" href="'+esc(b.link)+'" target="_blank" rel="noopener">Abrir el formulario</a></div></div>'}).join('')+'</div>':'<p class="empty">Aún no hay ningún brief.</p>')+'</div>'})}
  function brText(b,q){var d=b.data||{},out=[b.name,'Enlace: '+b.link,(b.sent?'Enviado: '+brWhen(b.sent):'Sin enviar')+' · '+b.n+' de '+b.tot+' preguntas',''];
    (q&&q.sections||[]).forEach(function(s,i){out.push('## '+(i+1<10?'0':'')+(i+1)+' · '+s.t);s.q.forEach(function(x){if(x.type==='files'){out.push('- '+x.t+': '+((b.files||[]).length?(b.files||[]).map(function(f){return f.name}).join(', '):'(ninguno)'));return}var a=brAns(x,d);out.push('- '+x.t+': '+(a.p?'[AÚN NO LO SABEN] ':'')+(a.t||(a.p?'':'(sin responder)')))});out.push('')});
    return out.join('\n')}
  function brDet(){var id=BR.open;return api('GET','brief/'+id).then(function(r){var b=r.brief,q=r.q,d=b.data||{};BR.last=r;
    if(!b.seen||b.seen<(b.upd||0))api('POST','brief/'+id+'/seen',{}).catch(function(){});
    var secs=(q&&q.sections||[]).map(function(s,i){var rows=s.q.map(function(x){
        if(x.type==='files'){var F=b.files||[];return '<div class="br-q"><dt>'+esc(x.t)+'</dt><dd'+(F.length?'':' class="no"')+'>'+(F.length?'<div class="br-files">'+F.map(function(f){var u='/admin/api/brief/'+encodeURIComponent(b.id)+'/f?k='+encodeURIComponent(f.k),img=/^image\/(jpeg|png|webp|gif|avif)$/.test(f.type||'');
          return '<a class="br-f" href="'+esc(u)+'" target="_blank" rel="noopener">'+(img?'<img src="'+esc(u)+'" alt="" loading="lazy">':'<span class="br-ph">'+esc((f.name.split('.').pop()||'archivo').toUpperCase().slice(0,5))+'</span>')+'<span>'+esc(f.name)+'</span><small>'+brSize(f.size)+'</small></a>'}).join('')+'</div>':'Ninguno')+'</dd></div>'}
        var a=brAns(x,d);if(BR.hide&&!a.t&&!a.p)return '';
        return '<div class="br-q"><dt>'+esc(x.t)+'</dt><dd'+(a.t||a.p?'':' class="no"')+'>'+(a.p?'<span class="br-pend">Aún no lo saben</span>':'')+(a.t?esc(a.t):(a.p?'':'Sin responder'))+'</dd></div>'}).join('');
      var n=s.q.filter(function(x){if(x.type==='files')return (b.files||[]).length;var a=brAns(x,d);return a.t||a.p}).length;
      return '<section class="panel br-sec"><h3>'+(i+1<10?'0':'')+(i+1)+' · '+esc(s.t)+' <small>'+n+' de '+s.q.length+'</small></h3><dl style="margin:0">'+rows+'</dl></section>'}).join('');
    return BR_CSS+'<div id="br"><div class="head"><p><button class="btn sm" type="button" data-br="back">← Briefs</button></p><h2 style="margin-top:8px">'+esc(b.name)+'</h2><p>'+b.n+' de '+b.tot+' preguntas respondidas · '+(b.files||[]).length+((b.files||[]).length===1?' archivo':' archivos')+(b.upd?' · último cambio '+esc(brWhen(b.upd)):'')+'</p></div>'+
      '<div class="br-top">'+brState(b)+'<button class="btn sm pri" type="button" data-br="text">Copiar todo en texto</button><button class="btn sm" type="button" data-br="copy" data-brl="'+esc(b.link)+'">Copiar enlace para el cliente</button><a class="btn sm" href="'+esc(b.link)+'" target="_blank" rel="noopener">Abrir el formulario</a>'+
      '<label class="br-tog"><input type="checkbox" data-br="hide"'+(BR.hide?' checked':'')+'> Ocultar lo que falta</label><button class="btn sm danger" type="button" data-br="reset" data-brid="'+esc(b.id)+'">Vaciar respuestas</button></div>'+
      (q?secs:'<p class="empty">Este brief no tiene preguntas en el admin.</p>')+'</div>'})}
  function brCopy(t){var ok=function(){toast('Copiado')};try{navigator.clipboard.writeText(t).then(ok,function(){window.prompt('Copia el texto:',t)})}catch(e){window.prompt('Copia el texto:',t)}}
  document.addEventListener('click',function(e){var b=e.target.closest('[data-br]');if(!b||!b.closest('#br'))return;var k=b.getAttribute('data-br');
    if(k==='open'){BR.open=b.getAttribute('data-brid');show();window.scrollTo(0,0);return}
    if(k==='back'){BR.open=null;show();return}
    if(k==='copy'){brCopy(b.getAttribute('data-brl'));return}
    if(k==='text'){if(BR.last)brCopy(brText(BR.last.brief,BR.last.q));return}
    if(k==='reset'){if(b.getAttribute('data-sure')!=='1'){b.setAttribute('data-sure','1');b.textContent='¿Seguro? Se borra todo lo escrito y los archivos';setTimeout(function(){b.removeAttribute('data-sure');b.textContent='Vaciar respuestas'},4000);return}
      api('POST','brief/'+b.getAttribute('data-brid')+'/reset',{}).then(function(){toast('Brief vacío: el enlace sigue siendo el mismo');show()},fail);return}});
  document.addEventListener('change',function(e){var x=e.target;if(!x.closest||!x.closest('#br')||x.getAttribute('data-br')!=='hide')return;BR.hide=x.checked;show()});
