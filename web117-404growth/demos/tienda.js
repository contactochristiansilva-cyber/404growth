/* Motor común de las tiendas de demostración de 404 Growth.
   Cada tienda pone su diseño (HTML y CSS) y llama a Tienda({...}) con sus productos y plantillas.
   Vistas: [data-view="home|shop|product"]. Rutas: #inicio, #tienda, #tienda/<categoria>, #p/<id>.
   Cesta guardada en localStorage por tienda. El pago está desactivado: es una demo. */
(function(){
  var d=document;
  function $(s,r){return (r||d).querySelector(s)}
  function $$(s,r){return [].slice.call((r||d).querySelectorAll(s))}
  function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}

  window.Tienda=function(cfg){
    var P={};cfg.products.forEach(function(p){P[p.id]=p});
    var KEY='demo404-'+cfg.key,cart=[];
    try{cart=JSON.parse(localStorage.getItem(KEY)||'[]')}catch(e){cart=[]}
    var money=cfg.money||function(n){return (Math.round(n*100)/100).toLocaleString('es-ES',{minimumFractionDigits:n%1?2:0,maximumFractionDigits:2})+' €'};
    var T={money:money,esc:esc,img:img,P:P,stars:stars};

    /* imágenes con respaldo: si la foto aún no existe, se ve un fondo de marca con el nombre */
    function img(src,alt,cls){return '<span class="tc-img '+(cls||'')+'" data-ph="'+esc(alt||'')+'"><img src="'+esc(src)+'" alt="'+esc(alt||'')+'" loading="lazy" onerror="this.parentNode.classList.add(\'ph\');this.remove()"></span>'}
    function stars(n){var s='';for(var i=1;i<=5;i++)s+='<i class="'+(i<=Math.round(n)?'on':'')+'">★</i>';return '<span class="tc-stars" aria-label="'+n+' de 5">'+s+'</span>'}

    /* ---------- aviso de demo ---------- */
    var bn=d.createElement('div');bn.className='tc-demo';bn.innerHTML='<span>'+(cfg.banner||'Tienda de demostración · Proyecto conceptual de 404 Growth')+'</span><a href="/book" class="tc-demo-a">Quiero una así →</a>';
    d.body.insertBefore(bn,d.body.firstChild);

    /* ---------- cesta ---------- */
    var dr=d.createElement('aside');dr.className='tc-cart';dr.setAttribute('aria-label','Cesta');dr.setAttribute('aria-hidden','true');
    dr.innerHTML='<div class="tc-ov" data-close-cart></div><div class="tc-panel" role="dialog" aria-modal="true" aria-labelledby="tc-ct"><header><h2 id="tc-ct">Tu cesta</h2><button type="button" class="tc-x" data-close-cart aria-label="Cerrar">×</button></header><div class="tc-ship"></div><div class="tc-lines"></div><footer><div class="tc-sub"><span>Subtotal</span><b></b></div><p class="tc-note">Impuestos incluidos. Envío calculado en el pago.</p><button type="button" class="tc-go">Finalizar compra</button></footer></div>';
    d.body.appendChild(dr);
    var md=d.createElement('div');md.className='tc-modal';md.hidden=true;
    md.innerHTML='<div class="tc-ov" data-close-modal></div><div class="tc-mbox" role="dialog" aria-modal="true"><b>Esto es una tienda de demostración</b><p>El pago está desactivado. Así de fácil sería comprar en tu tienda: tarjeta, Bizum o Apple Pay en un paso.</p><a href="/book" class="tc-go">Quiero una tienda así</a><button type="button" class="tc-link" data-close-modal>Seguir mirando</button></div>';
    d.body.appendChild(md);
    function save(){try{localStorage.setItem(KEY,JSON.stringify(cart))}catch(e){}}
    function count(){return cart.reduce(function(a,l){return a+l.q},0)}
    function total(){return cart.reduce(function(a,l){var p=P[l.id];return a+(p?p.price*l.q:0)},0)}
    function renderCart(){
      $$('[data-count]').forEach(function(e){e.textContent=count();e.classList.toggle('on',count()>0)});
      var t=total(),fs=cfg.freeShip||0,left=Math.max(0,fs-t);
      $('.tc-ship',dr).innerHTML=fs?('<p>'+(left>0?'Te faltan <b>'+money(left)+'</b> para el envío gratis':'<b>¡Tienes envío gratis!</b>')+'</p><i><s style="width:'+Math.min(100,t/fs*100)+'%"></s></i>'):'';
      $('.tc-lines',dr).innerHTML=cart.length?cart.map(function(l,i){var p=P[l.id];if(!p)return '';
        return '<div class="tc-line">'+img(p.img,p.name,'tc-li')+'<div><b>'+esc(p.name)+'</b>'+(l.v?'<small>'+esc(l.v)+'</small>':'')+'<div class="tc-q"><button type="button" data-dq="'+i+'" aria-label="Quitar uno">−</button><span>'+l.q+'</span><button type="button" data-iq="'+i+'" aria-label="Añadir uno">+</button></div></div><div class="tc-lp">'+money(p.price*l.q)+'<button type="button" class="tc-link" data-rm="'+i+'">Quitar</button></div></div>'}).join(''):'<p class="tc-empty">Tu cesta está vacía.</p>';
      $('.tc-sub b',dr).textContent=money(t);
      $('.tc-go',dr).disabled=!cart.length;
    }
    function add(id,v,q){var p=P[id];if(!p)return;q=q||1;var l=cart.filter(function(x){return x.id===id&&x.v===v})[0];if(l)l.q+=q;else cart.push({id:id,v:v||'',q:q});save();renderCart();toast(p.name);bump()}
    function open(){dr.classList.add('on');dr.setAttribute('aria-hidden','false');d.documentElement.classList.add('tc-lock');setTimeout(function(){var x=$('.tc-x',dr);x&&x.focus()},50)}
    function close(){dr.classList.remove('on');dr.setAttribute('aria-hidden','true');d.documentElement.classList.remove('tc-lock')}
    function bump(){$$('[data-open-cart]').forEach(function(b){b.classList.remove('tc-bump');void b.offsetWidth;b.classList.add('tc-bump')})}
    var tt;function toast(name){var t=$('.tc-toast')||d.body.appendChild(Object.assign(d.createElement('div'),{className:'tc-toast'}));t.innerHTML='<b>Añadido a la cesta</b><span>'+esc(name)+'</span><button type="button" data-open-cart>Ver cesta</button>';t.classList.add('on');clearTimeout(tt);tt=setTimeout(function(){t.classList.remove('on')},2600)}

    /* ---------- vistas y rutas ---------- */
    function grid(el,list){el.innerHTML=list.map(function(p){return cfg.card(p,T)}).join('');reveal(el)}
    function route(){
      var h=decodeURIComponent(location.hash.slice(1)),view='home',arg='';
      if(h.indexOf('p/')===0){view='product';arg=h.slice(2)}else if(h.indexOf('tienda')===0){view='shop';arg=h.split('/')[1]||''}
      if(view==='product'&&!P[arg])view='home';
      $$('[data-view]').forEach(function(v){v.hidden=v.getAttribute('data-view')!==view});
      $$('[data-nav]').forEach(function(a){a.classList.toggle('on',a.getAttribute('data-nav')===(view==='shop'?(arg||'all'):view))});
      if(view==='shop'){var list=cfg.products.filter(function(p){return !arg||p.cat===arg});
        var srt=$('[data-sort]');if(srt&&srt.value==='lo')list=list.slice().sort(function(a,b){return a.price-b.price});if(srt&&srt.value==='hi')list=list.slice().sort(function(a,b){return b.price-a.price});
        $$('[data-filter]').forEach(function(b){b.classList.toggle('on',b.getAttribute('data-filter')===(arg||''))});
        var g=$('[data-grid]');if(g)grid(g,list);var c=$('[data-shop-count]');if(c)c.textContent=list.length+(list.length===1?' producto':' productos')}
      if(view==='product'){var p=P[arg],el=$('[data-pdp]');el.innerHTML=cfg.pdp(p,T);
        var rel=$('[data-related]');if(rel)grid(rel,cfg.products.filter(function(x){return x.id!==p.id&&(x.cat===p.cat||true)}).slice(0,4));
        d.title=p.name+' · '+cfg.name;reveal(el);syncBuy(el)}else d.title=cfg.title||cfg.name;
      if(!route.first||view!=='home'||!h)scrollTo(0,0);route.first=true;
      if(cfg.onRoute)cfg.onRoute(view,arg,T);
    }
    function syncBuy(root){$$('[data-buy]',root).forEach(function(f){
      function upd(){var v=$$('input[type=radio]:checked',f).map(function(i){return i.value}).join(' · ');$$('[data-vlabel]',f).forEach(function(e){e.textContent=v});
        var sel=$('input[type=radio]:checked[data-img]',f);if(sel){var m=$('[data-main] img',root);if(m)m.src=sel.getAttribute('data-img')}}
      f.addEventListener('change',upd);upd()})}

    /* ---------- eventos ---------- */
    d.addEventListener('click',function(e){var t=e.target;
      var a=t.closest('[data-add]');if(a){e.preventDefault();var f=a.closest('[data-buy]'),v='',q=1;
        if(f){v=$$('input[type=radio]:checked',f).map(function(i){return i.value}).join(' · ');var qi=$('[data-qv]',f);if(qi)q=+qi.textContent||1}
        add(a.getAttribute('data-add'),v,q);if(a.hasAttribute('data-and-open'))open();return}
      var ab=t.closest('[data-add-many]');if(ab){e.preventDefault();ab.getAttribute('data-add-many').split(',').forEach(function(id){add(id.trim(),'',1)});open();return}
      if(t.closest('[data-open-cart]')){e.preventDefault();var to=$('.tc-toast');to&&to.classList.remove('on');open();return}
      if(t.closest('[data-close-cart]')){close();return}
      if(t.closest('[data-close-modal]')){md.hidden=true;return}
      if(t.closest('.tc-go')&&!t.closest('.tc-modal')){md.hidden=false;return}
      var iq=t.closest('[data-iq]');if(iq){cart[+iq.getAttribute('data-iq')].q++;save();renderCart();return}
      var dq=t.closest('[data-dq]');if(dq){var l=cart[+dq.getAttribute('data-dq')];l.q--;if(l.q<1)cart.splice(cart.indexOf(l),1);save();renderCart();return}
      var rm=t.closest('[data-rm]');if(rm){cart.splice(+rm.getAttribute('data-rm'),1);save();renderCart();return}
      var qb=t.closest('[data-qty]');if(qb){var qv=$('[data-qv]',qb.closest('[data-buy]'));var n=Math.max(1,(+qv.textContent||1)+(+qb.getAttribute('data-qty')));qv.textContent=n;return}
      var th=t.closest('[data-thumb]');if(th){var root=th.closest('[data-pdp]')||d;var m=$('[data-main] img',root);if(m)m.src=th.getAttribute('data-thumb');$$('[data-thumb]',root).forEach(function(x){x.classList.toggle('on',x===th)});return}
      var fl=t.closest('[data-filter]');if(fl){location.hash='tienda'+(fl.getAttribute('data-filter')?'/'+fl.getAttribute('data-filter'):'');return}
    });
    d.addEventListener('keydown',function(e){if(e.key==='Escape'){close();md.hidden=true}});
    d.addEventListener('change',function(e){if(e.target.matches('[data-sort]'))route()});
    addEventListener('hashchange',route);

    /* ---------- apariciones ---------- */
    var io='IntersectionObserver' in window?new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target)}})},{rootMargin:'0px 0px -6% 0px'}):null;
    function reveal(root){$$('[data-rv]',root||d).forEach(function(el){if(io&&!el.classList.contains('in'))io.observe(el);else el.classList.add('in')})}

    /* rejillas de inicio: data-home-grid="id1,id2,…" */
    $$('[data-home-grid]').forEach(function(el){grid(el,el.getAttribute('data-home-grid').split(',').map(function(id){return P[id.trim()]}).filter(Boolean))});
    renderCart();route();reveal();
    return {add:add,open:open,T:T,route:route};
  };
})();
