// Motor de Instagram del 25-26/11/2026 (negocios con varias tiendas y sin tienda online).
// Antes: window.__cap con las consultas capturadas (XMLHttpRequest) y gq(name, vars) (ver cap48.js).
window.S = window.S || {seen:{}, queue:[], prof:{}, qdone:[], st:{q:0,p:0,pp:0,err:0,e429:0}, stop:false};
S.sleep=(ms)=>new Promise(r=>setTimeout(r,ms));
S.users=(j)=>{const out=[];const w=(o,d)=>{if(d>12||!o||typeof o!=='object')return;if(Array.isArray(o)){o.forEach(x=>w(x,d+1));return;}if(o.username&&(o.pk||o.id)&&typeof o.username==='string')out.push({u:o.username.toLowerCase(),pk:String(o.pk||o.id)});for(const k in o)w(o[k],d+1);};w(j,0);const m=new Map();out.forEach(x=>m.set(x.u,x));return[...m.values()];};
S.add=(list,src)=>{let n=0;for(const x of list){if(S.seen[x.u])continue;S.seen[x.u]=src;S.queue.push(x);n++;}return n;};
S.search=async(q)=>{try{const j=await gq('PolarisKeywordSearchExplorePageRelayQuery',{query:q});if(j.err){S.st.err++;if(j.err==429)S.st.e429++;return -1;}S.st.q++;const n=S.add(S.users(j),'q:'+q);S.qdone.push([q,n]);return n;}catch(e){S.st.err++;return -1;}};
S.similar=async(pk,from)=>{try{const j=await gq('PolarisProfileSuggestedUsersWithPreloadableQuery',{module:'profile',target_id:pk});if(j.err){S.st.err++;return -1;}return S.add(S.users(j),'sim:'+from);}catch(e){S.st.err++;return -1;}};
S.phones=(t)=>{const s=new Set();const n=(t||'').normalize('NFKD');let m;const re=/(?:\+?34[\s.\-]?)?\b([67](?:[\s.\-]?\d){8})\b/g;while((m=re.exec(n))){const d=m[1].replace(/\D/g,'');if(d.length===9)s.add(d);}const re2=/wa\.me\/(?:34)?([67]\d{8})/g;while((m=re2.exec(n)))s.add(m[1]);const re3=/phone=(?:\+?34)?([67]\d{8})/g;while((m=re3.exec(n)))s.add(m[1]);return[...s];};
S.fijos=(t)=>{const s=new Set();const n=(t||'').normalize('NFKD');let m;const re=/(?:\+?34[\s.\-]?)?\b([89](?:[\s.\-]?\d){8})\b/g;while((m=re.exec(n))){const d=m[1].replace(/\D/g,'');if(d.length===9)s.add(d);}return[...s];};
S.SIG=/(env[ií]os?\b|enviamos|hacemos env|env[ií]o gratis|toda espa[ñn]a|pen[ií]nsula|pedidos? (?:por|al|v[ií]a) (?:whats|wasap|wassap|wsp|wa\b|md|dm|privado|mensaje)|bizum|reserv\w* (?:por|al|en) (?:privado|md|dm|whats)|en directo|directo de|venta online|compra online|escr[ií]be(?:nos|me) (?:por|al) (?:whats|md|dm|privado)|pregunta\w* (?:por|al) (?:md|dm|privado|whats)|contra ?reembolso|link de pago)/ig;
// varias tiendas: «2 tiendas», «nuestras tiendas», «ambas tiendas», varios 📍, varias calles
S.MULTI=/(\b(?:2|3|4|5|6|7|8|dos|tres|cuatro|cinco|seis|siete|ocho)\s+(?:tiendas|establecimientos|locales|puntos de venta|centros)|nuestras tiendas|ambas tiendas|todas (?:nuestras )?(?:las )?tiendas|en cualquiera de nuestras|nuestros? (?:locales|establecimientos|puntos de venta)|tiendas en\b|tienda de [A-ZÁÉÍÓÚ][\wáéíóú]+ y (?:de )?[A-ZÁÉÍÓÚ])/ig;
S.ARAB=/(árabe|arabe|abaya|caft[aá]n|kaftan|hijab|modest|isl[aá]m|halal|bakhoor|bukhoor|\boud\b|almizcle|lattafa|dubai)/i;
S.LATAM=/(argentina|m[eé]xico|cdmx|colombia|venezuela|per[uú]\b|chile\b|ecuador|bolivia|uruguay|paraguay|guatemala|honduras|costa rica|panam[aá]|rep[uú]blica dominicana|puerto rico|bogot[aá]|medell[ií]n|caracas|quito|monterrey|buenos aires|\+5[1-9]|\+59|cuotas sin inter|todo el pa[ií]s|mercado ?libre|\$\s?\d|s\.a\.s|\b1[0-9]k\b)/i;
S.KIDS=/(infantil|beb[eé]s?\b|ni[ñn]os?\b|ni[ñn]as?\b|kids|ceremonia infantil|comuni[oó]n|canastilla|puericultura)/i;
S.prices=(t)=>{const out=[];const re=/(\d{1,4}(?:[.,]\d{1,2})?)\s?(?:€|eur\b|euros)/ig;let m;while((m=re.exec(t||''))){const v=parseFloat(m[1].replace(',','.'));if(v>=3&&v<=3000)out.push(v);}return out;};
S.med=(a)=>{if(!a.length)return 0;const s=a.slice().sort((x,y)=>x-y);return s[Math.floor(s.length/2)];};
S.pins=(t)=>((t||'').match(/📍/g)||[]).length;
S.streets=(t)=>((t||'').match(/\b(?:c\/|calle|avda\.?|avenida|plaza|pza\.?|paseo|c\.c\.|centro comercial|pol[ií]gono)\s/ig)||[]).length;
S.profile=async(x)=>{
 try{
  const c=await gq('PolarisProfilePageContentQuery',{id:x.pk});if(c.err){S.st.err++;if(c.err==429)S.st.e429++;x.retry=(x.retry||0)+1;if(x.retry<3)S.queue.push(x);return;}
  S.st.p++;const u=c.data&&c.data.user;if(!u){S.prof[x.u]={skip:'nouser'};return;}
  const f=u.follower_count||0;const links=(u.bio_links||[]).map(l=>l.url||l.lynx_url||'').concat([u.external_url||'']).filter(Boolean);
  const r={u:x.u,pk:x.pk,name:u.full_name||'',f,bio:u.biography||'',city:u.city_name||'',addr:u.address_street||'',cat:u.category||'',priv:!!u.is_private,links,src:S.seen[x.u],fb:((u.linked_fb_info||{}).linked_fb_page||{}).id||''};
  if(r.priv||f<2500||f>250000){S.prof[x.u]={skip:'f',f};return;}
  const head=r.bio+' '+r.city+' '+r.addr+' '+links.join(' ');
  if(S.ARAB.test(head+' '+r.name)){S.prof[x.u]={skip:'arab',f};return;}
  if(S.LATAM.test(head)){S.prof[x.u]={skip:'latam',f};return;}
  const p=await gq('PolarisProfilePostsQuery',{username:x.u});S.st.pp++;
  const conn=p.data&&p.data.xdt_api__v1__feed__user_timeline_graphql_connection;const ed=(conn&&conn.edges)||[];
  const now=Date.now()/1000;const ts=[],likes=[];let cap='';
  for(const e of ed){const n=e.node;if(!n)continue;ts.push(n.taken_at||0);if(typeof n.like_count==='number')likes.push(n.like_count);const t=n.caption&&n.caption.text;if(t)cap+=' ¦ '+t.slice(0,600);}
  const last=ts.length?Math.max(...ts):0;r.lastDays=last?Math.round((now-last)/86400):999;r.n30=ts.filter(t=>now-t<30*86400).length;
  r.medL=S.med(likes);r.eng=f?Math.round(10000*r.medL/f)/100:0;
  const all=(r.bio+' '+cap).normalize('NFKC');
  r.sig=[...new Set((all.match(S.SIG)||[]).map(s=>s.toLowerCase()))].slice(0,8);
  r.multi=[...new Set(((r.bio+' '+cap).match(S.MULTI)||[]).map(s=>s.toLowerCase()))].slice(0,6);
  r.pins=S.pins(r.bio);r.streets=S.streets(r.bio);
  r.ph=S.phones(r.bio+' '+links.join(' ')+' '+cap);r.fx=S.fijos(r.bio+' '+links.join(' '));
  r.wa=/whats|wasap|wassap|wsp|wa\.me|📲|💬/i.test(r.bio+' '+links.join(' '));
  r.arab=S.ARAB.test(cap);r.latam=S.LATAM.test(cap);r.kids=S.KIDS.test(r.bio+' '+r.name);
  r.pr=S.med(S.prices(cap));r.cap=cap.slice(0,1500);
  S.prof[x.u]=r;
 }catch(e){S.st.err++;}
};
S.workers=async(k)=>{if(S.wrun)return;S.wrun=1;const one=async()=>{while(!S.stop){const x=S.queue.shift();if(!x){await S.sleep(1500);continue;}await S.profile(x);await S.sleep(700+Math.random()*600);}};Promise.all(Array.from({length:k},one)).then(()=>S.wrun=0);};
S.searchLoop=async(qs,gap)=>{S.srun=(S.srun||0)+1;for(const q of qs){if(S.stop)break;await S.search(q);await S.sleep(gap+Math.random()*1500);}S.srun--;};
S.NICHE=(r)=>{const t=(r.name+' '+r.u+' '+r.bio+' '+r.cat).toLowerCase();
 if(/perfum|fragan|cosm[eé]tic|maquillaje|droguer/.test(t))return'cosmetica';
 if(/merc[eé]r|lanas|hilos|tejidos|telas|costura|mueble|sof[aá]s|colch|decoraci/.test(t))return'fuera';
 if(/zapater|calzado|sneaker|zapatillas|shoes|botas/.test(t))return'sneakers';
 if(/joy|plata|oro\b|bisuter|jewel|joie|anillos|pendientes|relojer/.test(t))return'joya';
 if(/boutique|moda|ropa|showroom|fashion|outfit|vestidos|complementos|multimarca|closet|armario|lencer|flamenc|novia/.test(t))return'moda';
 return'?';};
S.web=(r)=>{const own=(r.links||[]).map(u=>{try{let x=decodeURIComponent(u);const m=x.match(/[?&]u=([^&]+)/);if(m)x=decodeURIComponent(m[1]);return new URL(x).hostname.replace(/^www\./,'');}catch(e){return'';}}).filter(h=>h&&!/instagram|facebook|fb\.me|wa\.me|whatsapp|linktr\.ee|linkin\.bio|tiktok|google|goo\.gl|maps\.app|bit\.ly|beacons|linkbio|campsite|taplink|youtube|threads|vinted|wallapop|later\.com|bento|lnk\.bio|carrd|msha\.ke/.test(h));return[...new Set(own)];};
S.score=(r)=>{let s=0;const why=[];
 const m=r.multi.length+(r.pins>=2?1:0)+(r.streets>=2?1:0);if(m>=2)s+=5;else if(m===1)s+=3;else{s-=3;why.push('1 tienda?');}
 if(r.lastDays<=7)s+=2;else if(r.lastDays<=14)s+=1;else{s-=4;why.push('inactiva');}
 if(r.ph.length)s+=2;else if(r.fx.length){s-=1;why.push('solo fijo');}else{s-=3;why.push('sin tel');}if(r.wa)s+=1;
 if(r.eng>=1)s+=2;else if(r.eng>=0.3)s+=1;else{s-=1;why.push('eng-');}
 if(r.f>=8000)s+=1;if(r.f>=25000)s+=1;
 if(S.web(r).length){why.push('web?');}
 if(r.sig.length)s+=1;
 if(r.kids){s-=3;why.push('kids');}
 const ni=S.NICHE(r);if(ni==='fuera'){s-=10;why.push('fuera');}if(ni==='?'){s-=2;why.push('nicho?');}
 if(r.arab){s-=10;why.push('ARAB');}if(r.latam){s-=10;why.push('latam');}
 return{s,why};};
S.cands=(min)=>Object.values(S.prof).filter(r=>!r.skip).map(r=>{const sc=S.score(r);return Object.assign({},r,{sc:sc.s,why:sc.why,niche:S.NICHE(r),web:S.web(r)});}).filter(r=>r.sc>=(min||0)).sort((a,b)=>b.sc-a.sc);
S.pkOf=async(u)=>{if(S.prof[u]&&S.prof[u].pk)return S.prof[u].pk;const p=await gq('PolarisProfilePostsQuery',{username:u});const e=p.data&&p.data.xdt_api__v1__feed__user_timeline_graphql_connection;const n=e&&e.edges&&e.edges[0]&&e.edges[0].node;return n&&n.user&&String(n.user.pk||n.user.id);};
S.simLoop=async(seeds)=>{for(const u of seeds){const pk=await S.pkOf(u);if(pk)await S.similar(pk,u);await S.sleep(3500+Math.random()*1500);}};
'engine48 ok';
