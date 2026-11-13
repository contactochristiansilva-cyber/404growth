  /* ---------- v70 · Contabilidad › Archivos: lo importante del ordenador de Chris, guardado aquí para siempre ----------
     Cualquier archivo hasta 50 MB, en carpetas. Se sube por trozos de 1,5 MB (uno detrás de otro, con 3 intentos cada uno); mientras
     sube se puede seguir usando el admin, y si se cierra la pestaña a medias, el navegador avisa. PDF y fotos se pueden ver; lo demás se descarga. */
  var AR={f:'',q:'',up:[],n:0,busy:false,edit:null,nf:null,rf:false,d:null};
  var ARERR={toobig:'Pesa más de 50 MB.',full:'No queda sitio en el admin. Borra algo que no necesites.',incomplete:'La subida se cortó. Vuelve a subirlo.',empty:'El archivo está vacío.',name:'Falta el nombre.',part:'La subida se cortó. Vuelve a subirlo.'};
  var ARCSS='#cb .ar-fold{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 14px}#cb .ar-fold button{display:inline-flex;align-items:center;gap:6px}#cb .ar-fold button small{font-weight:700;color:var(--mute);font-size:11.5px}#cb .ar-fold button[aria-pressed=true] small{color:inherit;opacity:.75}'+
    '#cb .ar-drop{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;text-align:center;padding:26px 18px;border:1.5px dashed var(--line);border-radius:14px;background:var(--surface);cursor:pointer;margin:0 0 14px;transition:background .15s,border-color .15s}'+
    '#cb .ar-drop b{font-size:15px}#cb .ar-drop span{font-size:13px;color:var(--mute)}#cb .ar-drop.on,#cb .ar-drop:hover{border-color:var(--accent);background:var(--accent-soft)}#cb .ar-drop:focus-within{outline:2px solid var(--accent);outline-offset:2px}'+
    '#cb .ar-up{display:flex;flex-direction:column;gap:8px;margin:0 0 14px}#cb .ar-up:empty{display:none}#cb .ar-ui{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:4px 12px;align-items:center;padding:10px 12px;border:1px solid var(--line);border-radius:12px;background:var(--surface);font-size:13.5px}'+
    '#cb .ar-ui b{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}#cb .ar-ui .hint{white-space:nowrap}#cb .ar-ui .bar{grid-column:1/-1;height:6px;border-radius:99px;background:var(--surface-2);overflow:hidden}#cb .ar-ui .bar i{display:block;height:100%;width:0;border-radius:99px;background:var(--accent);transition:width .2s}'+
    '#cb .ar-ui.err{border-color:var(--bad)}#cb .ar-ui.err .hint{color:var(--bad);white-space:normal}#cb .ar-ui.ok .bar i{background:var(--ok)}'+
    '#cb .ar-tools{margin:0 0 12px;gap:10px;align-items:center}#cb .ar-tools input{flex:1 1 220px;max-width:360px}'+
    '#cb .ar-t td{vertical-align:middle}#cb .ar-n{display:flex;align-items:center;gap:12px;min-width:0}#cb .ar-n>div{min-width:0}#cb .ar-n b{display:block;overflow-wrap:anywhere}'+
    '#cb .ar-x{flex:0 0 40px;height:40px;border-radius:10px;background:var(--surface-2);display:flex;align-items:center;justify-content:center;font-size:10.5px;font-weight:800;letter-spacing:.02em;color:var(--mute)}'+
    '#cb .ar-x.pdf{background:#FDE8E6;color:#B3261E}#cb .ar-x.img{background:#E3F1EC;color:#2E7A64}#cb .ar-x.doc{background:#E6EEFB;color:#2B5DB8}#cb .ar-x.xls{background:#E5F4E8;color:#1E7B3A}#cb .ar-x.zip{background:#F3ECDD;color:#8A6A1F}'+
    '@media (prefers-color-scheme:dark){#cb .ar-x.pdf{background:#3A2422;color:#F2A49C}#cb .ar-x.img{background:#1F3530;color:#8FD3BC}#cb .ar-x.doc{background:#1F2A3D;color:#9DBBF0}#cb .ar-x.xls{background:#1E3324;color:#8FD3A2}#cb .ar-x.zip{background:#352E1F;color:#E2C47E}}'+
    '#cb .ar-t td.ar-a{white-space:nowrap}#cb .ar-t td.ar-a .row{flex-wrap:nowrap;justify-content:flex-end}#cb .ar-t td.n{white-space:nowrap}#cb tr.ar-ed>td{background:var(--surface-2)}#cb .ar-sp{margin-top:12px}'+
    '#cb .ar-nf{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:-4px 0 14px}#cb .ar-nf input{flex:1 1 200px;max-width:280px}'+
    '@media (max-width:640px){#cb .ar-t thead{display:none}#cb .ar-t,#cb .ar-t tbody{display:block}#cb .ar-t tr{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:8px 12px;padding:13px 14px;border-bottom:1px solid var(--line);align-items:center}#cb .ar-t tr:last-child{border-bottom:0}'+
    '#cb .ar-t td{display:block;padding:0;border:0;min-width:0}#cb .ar-t td.ar-f{display:none}#cb .ar-t td.ar-d{display:none}#cb .ar-t td.ar-a{grid-column:1/-1}#cb .ar-t td.ar-a .row{justify-content:flex-start;flex-wrap:wrap}#cb .ar-t td.empty{grid-column:1/-1}'+
    '#cb .ar-t tr.ar-ed{display:block;padding:0}#cb .ar-t tr.ar-ed>td{padding:14px}#cb .ar-drop{padding:22px 14px}}';
  function arSize(n){n=Number(n)||0;return n<1024?n+' B':n<1048576?Math.max(1,Math.round(n/1024))+' KB':(n/1048576).toFixed(n<10485760?1:0).replace('.',',')+' MB'}
  function arKind(n){var e=(/\.([a-z0-9]{1,5})$/i.exec(n||'')||['',''])[1].toLowerCase();
    return {e:e?e.toUpperCase().slice(0,4):'?',c:e==='pdf'?'pdf':/^(jpe?g|png|webp|gif|heic|heif|svg|tiff?)$/.test(e)?'img':/^(docx?|pages|odt|rtf|txt)$/.test(e)?'doc':/^(xlsx?|numbers|ods|csv)$/.test(e)?'xls':/^(zip|rar|7z|gz|tar)$/.test(e)?'zip':''}}
  function arFolders(d){var n={};d.files.forEach(function(f){n[f.folder]=(n[f.folder]||0)+1});if(AR.nf&&!n[AR.nf])n[AR.nf]=0;
    return Object.keys(n).sort(function(a,b){return (a==='General'?-1:b==='General'?1:0)||a.localeCompare(b,'es')}).map(function(k){return [k,n[k]]})}
  function arUpHtml(){return AR.up.map(function(it){var pc=it.size?Math.round(it.done*100/it.size):0;
    return '<div class="ar-ui '+(it.st==='err'?'err':it.st==='ok'?'ok':'')+'" id="'+it.k+'"><b title="'+esc(it.name)+'">'+esc(it.name)+'</b><span class="hint">'+
      (it.st==='err'?esc(it.msg||'No se pudo subir.')+' <button type="button" class="btn sm" data-arx="'+it.k+'">Quitar</button>':it.st==='ok'?'Guardado en «'+esc(it.dest)+'»':it.st==='wait'?'En cola · '+arSize(it.size):pc+' % de '+arSize(it.size))+
      '</span>'+(it.st==='err'?'':'<div class="bar"><i style="width:'+(it.st==='ok'?100:pc)+'%"></i></div>')+'</div>'}).join('')}
  function arPaint(){var u=document.getElementById('ar-up');if(u)u.innerHTML=arUpHtml()}
  function arRow(f){if(AR.edit===f.id)return arEdit(f);var k=arKind(f.name),q=(f.name+' '+(f.note||'')+' '+f.folder).toLowerCase();
    return '<tr data-arq="'+esc(q)+'"><td><div class="ar-n"><span class="ar-x '+k.c+'" aria-hidden="true">'+esc(k.e)+'</span><div><b>'+esc(f.name)+'</b>'+(f.note?'<span class="hint">'+esc(f.note)+'</span>':'')+'</div></div></td>'+
      '<td class="ar-f">'+(AR.f?'':'<span class="chip">'+esc(f.folder)+'</span>')+'</td><td class="n"><span class="hint">'+arSize(f.size)+'</span></td><td class="ar-d"><span class="hint">'+dmy(ymd(new Date(f.created)))+'</span></td>'+
      '<td class="ar-a"><div class="row">'+(f.type?'<a class="btn sm" href="/admin/api/arch/'+esc(f.id)+'?ver=1" target="_blank" rel="noopener">Ver</a>':'')+'<a class="btn sm" href="/admin/api/arch/'+esc(f.id)+'" download="'+esc(f.name)+'">Descargar</a>'+
      '<button type="button" class="btn sm" data-ared="'+esc(f.id)+'">Editar</button><button type="button" class="btn sm danger" data-ardel="'+esc(f.id)+'">Borrar</button></div></td></tr>'}
  function arEdit(f){var fl=arFolders(AR.d);
    return '<tr class="ar-ed"><td colspan="5"><form id="f-ared" data-id="'+esc(f.id)+'"><div class="three"><div class="field"><label for="ae-name">Nombre</label><input id="ae-name" type="text" maxlength="160" value="'+esc(f.name)+'" required></div>'+
      '<div class="field"><label for="ae-folder">Carpeta</label><input id="ae-folder" type="text" maxlength="60" list="ae-fl" value="'+esc(f.folder)+'"><datalist id="ae-fl">'+fl.map(function(x){return '<option value="'+esc(x[0])+'">'}).join('')+'</datalist></div>'+
      '<div class="field"><label for="ae-note">Nota</label><input id="ae-note" type="text" maxlength="300" value="'+esc(f.note||'')+'" placeholder="Para qué es, hasta cuándo vale…"></div></div>'+
      '<div class="row"><button class="btn pri sm" type="submit">Guardar</button><button type="button" class="btn sm" data-arcancel>Cancelar</button></div></form></td></tr>'}
  function vArch(){return api('GET','arch').then(function(d){AR.d=d;AR.up=AR.up.filter(function(it){return it.st!=='ok'});
    var fl=arFolders(d);if(AR.f&&!fl.some(function(x){return x[0]===AR.f}))AR.f='';
    var list=AR.f?d.files.filter(function(f){return f.folder===AR.f}):d.files,dest=AR.f||'General';
    var h='<style>'+CBCSS+ARCSS+'</style><div id="cb"><div class="head"><h2>Contabilidad</h2><p>Tus facturas de ingresos y de gastos: lo que entra, lo que sale y lo que te queda.</p><div class="sp"><button type="button" class="btn sm" id="gasto-new" data-cb="newout">Apuntar un gasto</button><button type="button" class="btn pri sm" id="inv-new" data-cb="newinv">Nueva factura</button></div></div>'+
      '<div class="sub" role="group" aria-label="Apartados">'+CBTABS.map(function(x){return '<button type="button" data-cbtab="'+x[0]+'" aria-pressed="'+(CB.tab===x[0])+'">'+x[1]+'</button>'}).join('')+'</div>'+
      '<div class="head" style="margin-top:6px"><h2>Archivos</h2><p>Lo importante de tu ordenador, guardado aquí para siempre: escrituras, modelos de Hacienda, contratos, seguros… Cualquier tipo de archivo, hasta 50 MB.</p></div>';
    h+='<div class="ar-fold" role="group" aria-label="Carpetas"><button type="button" class="btn sm" data-arf="" aria-pressed="'+(!AR.f)+'">Todas <small>'+d.files.length+'</small></button>'+
      fl.map(function(x){return '<button type="button" class="btn sm" data-arf="'+esc(x[0])+'" aria-pressed="'+(AR.f===x[0])+'">'+esc(x[0])+' <small>'+x[1]+'</small></button>'}).join('')+
      '<button type="button" class="btn sm" data-arnew>+ Nueva carpeta</button>'+(AR.f&&fl.some(function(x){return x[0]===AR.f&&x[1]>0})?'<button type="button" class="btn sm" data-arren>Cambiar nombre</button>':'')+'</div>';
    if(AR.nf===''||AR.rf)h+='<form class="ar-nf" id="f-arnf"><input id="ar-nfn" type="text" maxlength="60" placeholder="'+(AR.rf?'Nuevo nombre de la carpeta':'Nombre de la carpeta: Hacienda, Contratos…')+'" value="'+(AR.rf?esc(AR.f):'')+'" required><button class="btn pri sm" type="submit">'+(AR.rf?'Cambiar':'Crear')+'</button><button type="button" class="btn sm" data-arnfx>Cancelar</button></form>';
    h+='<label class="ar-drop" id="ar-drop" tabindex="0"><input type="file" id="ar-in" multiple hidden><b>Arrastra aquí tus archivos o pulsa para elegirlos</b><span>Se guardan en «'+esc(dest)+'». PDF, fotos, Word, Excel, ZIP… hasta 50 MB cada uno.</span></label>'+
      '<div class="ar-up" id="ar-up" aria-live="polite">'+arUpHtml()+'</div>';
    var tot=list.reduce(function(t,f){return t+f.size},0);
    h+='<div class="row ar-tools"><input type="search" id="ar-q" placeholder="Buscar por nombre, nota o carpeta" value="'+esc(AR.q)+'" aria-label="Buscar archivos"><span class="hint">'+(list.length===1?'1 archivo':list.length+' archivos')+' · '+arSize(tot)+'</span></div>'+
      '<div class="tw"><table class="ar-t"><thead><tr><th>Archivo</th><th>'+(AR.f?'':'Carpeta')+'</th><th class="n">Tamaño</th><th>Subido</th><th></th></tr></thead><tbody>'+
      (list.length?list.map(arRow).join(''):'<tr><td colspan="5" class="empty">'+(AR.f?'Esta carpeta está vacía. Sube aquí sus archivos.':'Aún no has guardado ningún archivo. Arrástralos arriba.')+'</td></tr>')+
      '<tr id="ar-none" hidden><td colspan="5" class="empty">Ningún archivo coincide con la búsqueda.</td></tr></tbody></table></div>';
    if(d.db!==null&&d.db!==undefined)h+='<p class="hint ar-sp">Espacio del admin: '+arSize(d.db)+' de '+arSize(d.dbMax)+' usados'+(d.used?' (tus archivos, '+arSize(d.used)+')':'')+'.</p>';
    else if(d.used)h+='<p class="hint ar-sp">Tus archivos ocupan '+arSize(d.used)+'.</p>';
    return h+'</div>'})}
  function arFilter(){var q=(AR.q||'').trim().toLowerCase(),n=0;$$('#cb .ar-t tr[data-arq]').forEach(function(r){var on=!q||r.getAttribute('data-arq').indexOf(q)>=0;r.hidden=!on;if(on)n++});var z=document.getElementById('ar-none');if(z)z.hidden=!(q&&!n&&$$('#cb .ar-t tr[data-arq]').length)}
  function arQueue(fs){var dest=AR.f||'General',max=(AR.d&&AR.d.max)||52428800;
    [].forEach.call(fs||[],function(f){var it={k:'aru'+(++AR.n),name:f.name||'archivo',size:f.size,done:0,st:'wait',file:f,dest:dest};
      if(!f.size){it.st='err';it.msg=ARERR.empty}else if(f.size>max){it.st='err';it.msg=ARERR.toobig}AR.up.push(it)});
    arPaint();arRun()}
  function arPut(it,id,k,part){var a=k*part,b=Math.min(it.size,a+part),tries=0;
    var go=function(){return fetch('/admin/api/arch/'+id+'/p/'+k,{method:'PUT',headers:{'content-type':'application/octet-stream','x-404':'1'},body:it.file.slice(a,b)}).then(function(r){
      if(r.status===401){location.reload();throw new Error('auth')}if(r.ok)return;return r.json().catch(function(){return {}}).then(function(j){var e=new Error(j.error||'error');e.code=j.error;e.st=r.status;throw e})}).catch(function(e){
      if(e&&e.message==='auth')throw e;if(++tries<3&&!(e&&e.st===404))return new Promise(function(res){setTimeout(res,1500*tries)}).then(go);throw e})};
    return go().then(function(){it.done=b;arPaint()})}
  function arRun(){if(AR.busy)return;var it=AR.up.filter(function(x){return x.st==='wait'})[0];if(!it)return;AR.busy=true;it.st='up';arPaint();var id=null;
    api('POST','arch',{name:it.name,size:it.size,folder:it.dest}).then(function(r){id=r.id;var k=0,next=function(){if(k>=r.parts)return null;return arPut(it,id,k++,r.part).then(next)};return next()})
      .then(function(){return api('POST','arch/'+id+'/done')})
      .then(function(){it.st='ok';it.file=null;AR.busy=false;arPaint();if(AR.up.some(function(x){return x.st==='wait'})){arRun();return}toast(AR.up.filter(function(x){return x.st==='ok'}).length>1?'Archivos guardados':'Archivo guardado');if(S.sec==='contabilidad'&&CB.tab==='arch'&&!AR.edit)show()},
        function(e){it.st='err';it.file=null;it.msg=ARERR[e&&e.code]||'No se pudo subir. Inténtalo otra vez.';AR.busy=false;if(id)api('DELETE','arch/'+id).catch(function(){});arPaint();if(e&&e.message==='auth')return;arRun()})}
  window.addEventListener('beforeunload',function(e){if(AR.busy||AR.up.some(function(x){return x.st==='wait'})){e.preventDefault();e.returnValue=''}});
  document.addEventListener('click',function(e){var t=e.target.closest('[data-arf],[data-arnew],[data-arren],[data-arnfx],[data-arx],[data-ared],[data-arcancel],[data-ardel]');if(!t||!t.closest('#cb'))return;var g=function(k){return t.getAttribute(k)};
    if(t.hasAttribute('data-arf')){AR.f=g('data-arf');AR.edit=null;AR.rf=false;if(AR.nf!==null&&AR.f!==AR.nf)AR.nf=null;show();return}
    if(t.hasAttribute('data-arnew')){AR.nf='';AR.rf=false;show();setTimeout(function(){var i=document.getElementById('ar-nfn');if(i)i.focus()},300);return}
    if(t.hasAttribute('data-arren')){AR.rf=true;AR.nf=null;show();setTimeout(function(){var i=document.getElementById('ar-nfn');if(i){i.focus();i.select()}},300);return}
    if(t.hasAttribute('data-arnfx')){if(AR.nf==='')AR.nf=null;AR.rf=false;show();return}
    if(t.hasAttribute('data-arx')){AR.up=AR.up.filter(function(x){return x.k!==g('data-arx')});arPaint();return}
    if(t.hasAttribute('data-ared')){AR.edit=g('data-ared');show();return}
    if(t.hasAttribute('data-arcancel')){AR.edit=null;show();return}
    if(t.hasAttribute('data-ardel')){if(t.dataset.sure!=='1'){t.dataset.sure='1';var o=t.textContent;t.textContent='¿Seguro? Pulsa otra vez';setTimeout(function(){if(t.isConnected){t.dataset.sure='';t.textContent=o}},4000);return}
      t.disabled=true;api('DELETE','arch/'+g('data-ardel')).then(function(){toast('Borrado');show()},function(x){t.disabled=false;fail(x)});return}});
  document.addEventListener('submit',function(e){var f=e.target;if(f.id!=='f-arnf'&&f.id!=='f-ared')return;e.preventDefault();var v=function(i){var x=document.getElementById(i);return x?String(x.value||'').trim():''},btn=f.querySelector('button[type=submit]');
    if(f.id==='f-arnf'){var n=v('ar-nfn').replace(/[\\\/:*?"<>|]+/g,'-').replace(/\s+/g,' ').slice(0,60);if(!n){toast('Escribe el nombre de la carpeta.');return}
      if(AR.rf){btn.disabled=true;api('POST','archf',{from:AR.f,to:n}).then(function(r){AR.f=r.folder;AR.rf=false;toast('Carpeta cambiada');show()},function(x){btn.disabled=false;fail(x)});return}
      AR.nf=n;AR.f=n;show();return}
    btn.disabled=true;api('POST','arch/'+f.getAttribute('data-id'),{name:v('ae-name'),folder:v('ae-folder'),note:v('ae-note')}).then(function(){toast('Guardado');AR.edit=null;show()},function(x){btn.disabled=false;toast(ARERR[x&&x.code]||ERR[x&&x.code]||'No se pudo guardar.')})});
  document.addEventListener('change',function(e){if(e.target.id==='ar-in'&&e.target.files&&e.target.files.length){arQueue(e.target.files);e.target.value=''}});
  document.addEventListener('input',function(e){if(e.target.id==='ar-q'){AR.q=e.target.value;arFilter()}});
  /* while Archivos is on screen a file dropped anywhere on the page is saved (and the browser does not leave the admin to open it) */
  var arHas=function(e){return !!document.getElementById('ar-drop')&&e.dataTransfer&&[].indexOf.call(e.dataTransfer.types||[],'Files')>=0};
  ['dragenter','dragover'].forEach(function(n){document.addEventListener(n,function(e){if(!arHas(e))return;e.preventDefault();document.getElementById('ar-drop').classList.add('on')})});
  document.addEventListener('dragleave',function(e){var z=document.getElementById('ar-drop');if(z&&!e.relatedTarget)z.classList.remove('on')});
  document.addEventListener('drop',function(e){if(!arHas(e))return;e.preventDefault();document.getElementById('ar-drop').classList.remove('on');if(e.dataTransfer.files&&e.dataTransfer.files.length)arQueue(e.dataTransfer.files)});
  document.addEventListener('keydown',function(e){if(e.target.id==='ar-drop'&&(e.key==='Enter'||e.key===' ')){e.preventDefault();var i=document.getElementById('ar-in');if(i)i.click()}});

