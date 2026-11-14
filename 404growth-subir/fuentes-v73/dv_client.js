  /* ---------- v72 · v73 · Entregables: la fecha de entrega de la tienda de cada cliente que ya ha pagado, con cuenta atrás (solo para Chris) ---------- */
  var DV={open:null};
  function dvOff(ms){var o={};new Intl.DateTimeFormat('en-US',{timeZone:'Europe/Madrid',hourCycle:'h23',year:'numeric',month:'2-digit',day:'2-digit',hour:'2-digit',minute:'2-digit',second:'2-digit'}).formatToParts(new Date(ms)).forEach(function(x){o[x.type]=x.value});
    return (Date.UTC(+o.year,+o.month-1,+o.day,(+o.hour)%24,+o.minute,+o.second)-Math.floor(ms/1000)*1000)/60000}
  function dvMs(s){var a=String(s).split(/[-T:]/).map(Number),g=Date.UTC(a[0],a[1]-1,a[2],a[3],a[4]),off=dvOff(g),ms=g-off*60000,o2=dvOff(ms);return o2!==off?g-o2*60000:ms}
  function dvDay(ms){return new Date(ms).toLocaleDateString('es-ES',{timeZone:'Europe/Madrid',weekday:'long',day:'numeric',month:'long'})}
  function dvWhen(ms){return dvDay(ms)+', '+new Date(ms).toLocaleTimeString('es-ES',{timeZone:'Europe/Madrid',hour:'2-digit',minute:'2-digit'})}
  function dvShort(ymd){return new Date(ymd+'T12:00:00Z').toLocaleDateString('es-ES',{timeZone:'UTC',day:'numeric',month:'short'})}
  function dvAdd(ymd,n){var a=ymd.split('-').map(Number),d=new Date(Date.UTC(a[0],a[1]-1,a[2]+n));return d.toISOString().slice(0,10)}
  function dvP2(n){return (n<10?'0':'')+n}
  function dvTxt(t){var x=t-Date.now(),late=x<0;x=Math.abs(x);var d=Math.floor(x/864e5),h=Math.floor(x%864e5/36e5),m=Math.floor(x%36e5/6e4),s=Math.floor(x%6e4/1e3);
    return {late:late,soon:!late&&t-Date.now()<2*864e5,html:'<span><b>'+d+'</b><small>'+(d===1?'día':'días')+'</small></span><span><b>'+dvP2(h)+'</b><small>h</small></span><span><b>'+dvP2(m)+'</b><small>min</small></span><span><b>'+dvP2(s)+'</b><small>s</small></span>'}}
  function dvTick(){var els=document.querySelectorAll('[data-dvt]');for(var i=0;i<els.length;i++){var el=els[i],r=dvTxt(+el.getAttribute('data-dvt'));
    el.querySelector('.dv-n').innerHTML=r.html;el.classList.toggle('late',r.late);el.classList.toggle('soon',r.soon);var l=el.querySelector('.dv-l');if(l)l.textContent=r.late?'Vencida hace':'Faltan'}}
  setInterval(dvTick,1000);
  function dvForm(x){var at=x.at||'',dd=at?at.slice(0,10):'',tt=at&&at.slice(11)!=='23:59'?at.slice(11):'',base=x.start||x.paidOn||'',d15=base?dvAdd(base,15):'';
    return '<form class="dv-f" data-dvf="'+esc(x.id)+'"><label><span>Día de entrega</span><input type="date" name="d" required value="'+esc(dd)+'"></label><label><span>Hora <em>(opcional)</em></span><input type="time" name="t" value="'+esc(tt)+'"></label>'+
      '<label class="dv-nt"><span>Nota <em>(opcional)</em></span><input type="text" name="n" maxlength="200" placeholder="Por ejemplo: con 300 productos" value="'+esc(x.note||'')+'"></label>'+
      '<div class="dv-fb"><button class="btn pri sm" type="submit">'+(at?'Guardar':'Poner fecha')+'</button>'+(d15&&dd!==d15?'<button class="btn sm" type="button" data-dv="d15" data-dvid="'+esc(x.id)+'" data-dvv="'+d15+'">'+(x.start?'Día 15 del arranque':'15 días desde el pago')+' ('+esc(dvShort(d15))+')</button>':'')+
      (at&&DV.open===x.id?'<button class="btn sm" type="button" data-dv="close">Cancelar</button>':'')+'</div><p class="hint">Hora de España. Sin hora, la cuenta atrás llega hasta el final de ese día.</p></form>'}
  function dvRow(x){var id=esc(x.id),at=x.at,t=at?dvMs(at):0,done=x.done,hid=x.hidden;
    var meta=[x.paidOn?'Pagado el '+esc(dvShort(x.paidOn)):'',x.start?'Arranque: '+esc(dvShort(x.start)):'',x.archived?'<span class="chip">Archivado</span>':''].filter(Boolean).join(' · ');
    var h='<div class="panel dv-r'+(done?' done':'')+(hid?' hid':'')+'" id="dv-'+id+'"><div class="dv-m"><h3>'+esc(x.name)+'</h3>'+(meta?'<p class="dv-meta">'+meta+'</p>':'')+(x.note?'<p class="dv-note">'+esc(x.note)+'</p>':'')+
      (hid?'':'<button class="dv-x" type="button" data-dv="hide" data-dvid="'+id+'">Quitar de Entregables</button>')+'</div>';
    if(hid)return h+'<div class="dv-c"><p class="dv-w">Quitado de la lista el '+esc(dvDay(hid))+'</p></div><div class="dv-a"><button class="btn sm" type="button" data-dv="unhide" data-dvid="'+id+'">Volver a la lista</button></div></div>';
    if(at&&!done){var r=dvTxt(t);h+='<div class="dv-c'+(r.late?' late':r.soon?' soon':'')+'" data-dvt="'+t+'"><p class="dv-l">'+(r.late?'Vencida hace':'Faltan')+'</p><div class="dv-n">'+r.html+'</div><p class="dv-w">Entrega: '+esc(dvWhen(t))+'</p></div>'}
    else if(done)h+='<div class="dv-c ok"><p class="dv-l">Entregada</p><p class="dv-w">el '+esc(dvWhen(done))+' · tocaba el '+esc(dvDay(t))+'</p></div>';
    h+='<div class="dv-a">';
    if(at){h+=(done?'<button class="btn sm" type="button" data-dv="undone" data-dvid="'+id+'">Volver a la cuenta atrás</button>':'<button class="btn pri sm" type="button" data-dv="done" data-dvid="'+id+'">Entregada</button>')+'<button class="btn sm" type="button" data-dv="edit" data-dvid="'+id+'">Cambiar fecha</button><button class="btn sm danger" type="button" data-dv="clear" data-dvid="'+id+'">Quitar fecha</button>'}
    h+='</div>';
    if(!at||DV.open===x.id)h+='<div class="dv-ed">'+dvForm(x)+'</div>';
    return h+'</div>'}
  function vEnt(){return api('GET','deliv').then(function(d){var all=d.items||[],now=Date.now();
    var vis=all.filter(function(x){return !x.hidden}),hidL=all.filter(function(x){return x.hidden});
    var withD=vis.filter(function(x){return x.at&&!x.done}).sort(function(a,b){return dvMs(a.at)-dvMs(b.at)});
    var noD=vis.filter(function(x){return !x.at}).sort(function(a,b){return a.paidOn<b.paidOn?-1:a.paidOn>b.paidOn?1:0});
    var doneL=vis.filter(function(x){return x.at&&x.done}).sort(function(a,b){return b.done-a.done});
    var late=withD.filter(function(x){return dvMs(x.at)<now}).length,week=withD.filter(function(x){var t=dvMs(x.at);return t>=now&&t-now<=7*864e5}).length;
    return '<style>#dv .dv-r{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1.4fr) auto;gap:14px 22px;align-items:center;margin-bottom:10px}#dv .dv-r h3{font-size:17px}#dv .dv-meta,#dv .dv-note{color:var(--mute);font-size:12.5px;margin-top:4px}#dv .dv-note{color:var(--ink)}'+
      '#dv .dv-x{background:none;border:0;padding:0;margin-top:7px;font:inherit;font-size:12px;font-weight:600;color:var(--mute);text-decoration:underline;text-underline-offset:2px;cursor:pointer}#dv .dv-x[data-sure]{color:var(--bad)}#dv .dv-r.hid{opacity:.72}#dv .head a{color:inherit;text-decoration:underline;text-underline-offset:2px}'+
      '#dv .dv-c .dv-l{font-size:11.5px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--mute)}#dv .dv-n{display:flex;gap:14px;margin:2px 0 4px;font-variant-numeric:tabular-nums}#dv .dv-n span{display:flex;align-items:baseline;gap:3px}#dv .dv-n b{font-size:30px;font-weight:800;letter-spacing:-.03em;line-height:1.1}#dv .dv-n small{font-size:12px;font-weight:700;color:var(--mute)}'+
      '#dv .dv-w{font-size:12.5px;color:var(--mute)}#dv .dv-c.soon .dv-n b,#dv .dv-c.soon .dv-l{color:var(--warn)}#dv .dv-c.late .dv-n b,#dv .dv-c.late .dv-l{color:var(--bad)}#dv .dv-c.ok .dv-l{color:var(--ok);font-size:13px}'+
      '#dv .dv-a{display:flex;gap:6px;flex-wrap:wrap;justify-content:flex-end}#dv .dv-r.done{opacity:.75}#dv .dv-ed{grid-column:1/-1}#dv .dv-f{display:flex;gap:10px 12px;align-items:flex-end;flex-wrap:wrap;border-top:1px solid var(--line);padding-top:12px}'+
      '#dv .dv-f label{display:flex;flex-direction:column;gap:5px;font-size:12.5px;font-weight:700;color:var(--mute)}#dv .dv-f label em{font-style:normal;font-weight:500}#dv .dv-f input{border:1px solid var(--line);background:var(--surface);border-radius:10px;padding:8px 10px;color:var(--ink);min-width:0}#dv .dv-f .dv-nt{flex:1 1 220px}#dv .dv-f .dv-nt input{width:100%}#dv .dv-fb{display:flex;gap:6px;flex-wrap:wrap}#dv .dv-f .hint{flex-basis:100%}'+
      '#dv .dv-sec{margin:22px 0 10px;font-size:13px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--mute)}#dv details.dv-dn>summary{cursor:pointer}'+
      '@media(max-width:860px){#dv .dv-r{grid-template-columns:1fr}#dv .dv-a{justify-content:flex-start}#dv .dv-n b{font-size:26px}}</style>'+
      '<div id="dv"><div class="head"><h2>Entregables</h2><p>La fecha de entrega de la tienda de cada cliente que ya ha pagado, con su cuenta atrás. Un cliente entra aquí cuando marcas su pago como cobrado en <a href="/admin#facturacion">Facturación</a>. Solo lo ves tú: no sale en su portal.</p></div>'+
      '<div class="kpis"><div class="kpi"><small>Con fecha</small><b>'+withD.length+'</b></div><div class="kpi"><small>En los próximos 7 días</small><b>'+week+'</b></div><div class="kpi"><small>Vencidas</small><b'+(late?' style="color:var(--bad)"':'')+'>'+late+'</b></div><div class="kpi"><small>Entregadas</small><b>'+doneL.length+'</b></div></div>'+
      (withD.length?'<p class="dv-sec">Cuenta atrás</p>'+withD.map(dvRow).join(''):'')+
      (noD.length?'<p class="dv-sec">Sin fecha todavía</p>'+noD.map(dvRow).join(''):'')+
      (!vis.length?'<p class="empty">Todavía no hay ningún cliente con el pago cobrado. Cuando en Facturación marques un pago como cobrado, el cliente aparece aquí para ponerle la fecha de entrega.</p>':'')+
      (doneL.length?'<details class="dv-dn"'+(doneL.some(function(x){return DV.open===x.id})?' open':'')+'><summary class="dv-sec">Entregadas · '+doneL.length+'</summary>'+doneL.map(dvRow).join('')+'</details>':'')+
      (hidL.length?'<details class="dv-dn dv-hd"><summary class="dv-sec">Quitados de la lista · '+hidL.length+'</summary>'+hidL.map(dvRow).join('')+'</details>':'')+'</div>'})}
  function dvSave(id,b,msg){return api('POST','deliv/'+id,b).then(function(){DV.open=null;toast(msg);show()},fail)}
  function dvSure(b,label,go){if(b.getAttribute('data-sure')){go();return}b.setAttribute('data-sure','1');b.textContent='¿Seguro? Pulsa otra vez';setTimeout(function(){if(b.isConnected){b.removeAttribute('data-sure');b.textContent=label}},3500)}
  document.addEventListener('click',function(e){var b=e.target.closest('[data-dv]');if(!b||!b.closest('#dv'))return;var k=b.getAttribute('data-dv'),id=b.getAttribute('data-dvid');
    if(k==='edit'){DV.open=id;show();return}
    if(k==='close'){DV.open=null;show();return}
    if(k==='d15'){var f=b.closest('form');f.querySelector('[name=d]').value=b.getAttribute('data-dvv');f.querySelector('[name=d]').focus();return}
    if(k==='done')return dvSave(id,{done:true},'Marcada como entregada');
    if(k==='undone')return dvSave(id,{done:false},'Vuelve a la cuenta atrás');
    if(k==='clear')return dvSure(b,'Quitar fecha',function(){dvSave(id,{at:''},'Fecha quitada')});
    if(k==='hide')return dvSure(b,'Quitar de Entregables',function(){dvSave(id,{hide:true},'Quitado de Entregables')});
    if(k==='unhide')return dvSave(id,{hide:false},'Vuelve a Entregables')});
  document.addEventListener('submit',function(e){var f=e.target.closest('[data-dvf]');if(!f)return;e.preventDefault();var id=f.getAttribute('data-dvf'),d=f.querySelector('[name=d]').value,t=f.querySelector('[name=t]').value||'23:59';
    if(!/^\d{4}-\d{2}-\d{2}$/.test(d)){toast('Elige el día de entrega.');return}
    dvSave(id,{at:d+'T'+t,note:f.querySelector('[name=n]').value},'Fecha guardada: empieza la cuenta atrás')});
