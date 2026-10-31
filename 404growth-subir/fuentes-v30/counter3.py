"""The visit counter on the pages, version 3 (27 oct 2026, «proposal intelligence»). It keeps the v2 counter as it is and adds, before it,
one small script (c404 v3) that the v2 one talks to through three hooks:
  __c404x()  the context sent with the entry: screen, viewport, pixel ratio, orientation, touch points, language, time zone, dark mode,
             the site it came from (host only), how the page was opened (link, reload, back) and signals of automation (webdriver,
             headless). Nothing that identifies the person; unknown stays unknown.
  __c404p()  added to every progress post: active seconds (visible AND activity in the last 30 s or a video playing), scroll depth in %,
             active seconds per section.
  __c404on() called with the visit key: from then on the typed events go to the counter (/e), in batches, with an id each (the counter
             keeps each one once), the second of the visit and the page clock.
Events: sin (a section seen for 1 s, with its heading and order), scr (scroll 25/50/75/90/100 %), exp/col (a «details» opened/closed),
tab, vplay/vprog/vpause/vend (videos), copy (only how many characters, never the text), print, share (the page's own share button), dl
(a document link), form0/form1 (a form started/sent: never what was typed), hid/vis (tab hidden/visible), idle/wake, end (page left),
rel (reload), err/rerr (script and resource errors, 5 and 10 at most), nav (load times: TTFB, DOMContentLoaded, load, LCP, CLS, network
type), resize (orientation change), fs (full screen).
Pages already on v3 are left as they are; pages without the v2 counter are skipped. Run after counter.py and counter2.py when packaging.
usage: python3 counter3.py <site folder>"""
import os, sys
V3 = 'c404 v3'
ADDON = r"""<script>
/* c404 v3 (27 oct 2026): more detail for the visit counter below. No cookies, nothing kept on the device, never what is typed or copied. */
(function(){
  if(!/(^|\.)404growth\.com$/.test(location.hostname)||!window.fetch)return;
  try{if(localStorage.getItem('c404int')&&!/[?&]interno=0/.test(location.search))return}catch(e){}
  var EP='https://404growth-visits.contactochristiansilva.workers.dev',key='',Q=[],seq=0,T0=Date.now(),act=0,last=0,it=0,maxs=0,ms={},SS={},cur=null,curT=0,seenS={},ord=0,idle=false,playing=0,errs=0,rerrs=0,sz=0,sentNav=false,iv;
  var rid=Math.random().toString(36).slice(2,8);
  function sec(){return Math.round((Date.now()-T0)/1000)}
  function ev(y,o){o=o||{};o.y=y;o.i=rid+(seq++).toString(36);o.t=sec();o.ot=Date.now();Q.push(o);if(Q.length>200)Q.shift();if(Q.length>=20)flush()}
  function flush(beacon){if(!key||!Q.length)return;var b=JSON.stringify({k:key,ev:Q.splice(0,25)});
    try{if(beacon&&navigator.sendBeacon&&navigator.sendBeacon(EP+'/e',b)){}else fetch(EP+'/e',{method:'POST',body:b,keepalive:true}).catch(function(){})}catch(e){}if(Q.length)setTimeout(function(){flush(beacon)},300)}
  function txt(s,n){return String(s||'').replace(/\s+/g,' ').trim().slice(0,n||80)}
  function vis(){return document.visibilityState==='visible'}
  function poke(){last=Date.now();if(!it)it=1;if(idle){idle=false;ev('wake')}}
  ['scroll','pointerdown','touchstart','keydown','wheel','mousemove'].forEach(function(e){addEventListener(e,poke,{capture:true,passive:true})});
  var SECS=[].slice.call(document.querySelectorAll('section[id],header[id],footer[id],article[id],main[id]')).filter(function(s){return /^[A-Za-z][\w-]{0,39}$/.test(s.id)}).slice(0,40);
  function head(s){var h=s.querySelector('h1,h2,h3');return txt((h&&h.textContent)||s.getAttribute('aria-label')||s.id,60)}
  function current(){var y=innerHeight/2,best=null;for(var i=0;i<SECS.length;i++){var r=SECS[i].getBoundingClientRect();if(r.top<=y&&r.bottom>=y){if(!best||r.height<best.r.height)best={s:SECS[i],r:r}}}return best&&best.s}
  function scrollPct(){var de=document.documentElement,h=Math.max(1,de.scrollHeight);return Math.min(100,Math.round((scrollY+innerHeight)/h*100))}
  function tick(){var now=Date.now(),on=vis()&&(now-last<30000||playing>0);
    if(vis()&&!on&&!idle&&last){idle=true;ev('idle')}
    if(on){act+=1;var s=current();if(s){SS[s.id]=(SS[s.id]||0)+1;if(s!==cur){cur=s;curT=0}curT++;if(curT===1&&!seenS[s.id]){seenS[s.id]=1;ev('sin',{s:s.id,l:head(s),m:{ord:++ord}})}}}
    var p=scrollPct();if(p>maxs){maxs=p;[25,50,75,90,100].forEach(function(m){if(p>=m&&!ms[m]){ms[m]=1;ev('scr',{n:m})}})}
    if(++sz%5===0)flush()}
  window.__c404x=function(){var o={sw:screen.width,sh:screen.height,vw:innerWidth,vh:innerHeight,dpr:window.devicePixelRatio||1,or:innerHeight>=innerWidth?'p':'l',tch:navigator.maxTouchPoints||0,it:it};
    try{o.lang=(navigator.languages&&navigator.languages[0])||navigator.language||''}catch(e){}
    try{o.tz=Intl.DateTimeFormat().resolvedOptions().timeZone||''}catch(e){}
    try{o.dk=matchMedia('(prefers-color-scheme: dark)').matches?1:0}catch(e){}
    try{var r=document.referrer&&new URL(document.referrer);if(r&&r.host!==location.host)o.ref=r.host}catch(e){}
    try{var n=performance.getEntriesByType('navigation')[0];if(n)o.nav=n.type}catch(e){}
    o.wd=navigator.webdriver?1:0;o.hl=(/HeadlessChrome/.test(navigator.userAgent)||(navigator.languages&&navigator.languages.length===0))?1:0;return o};
  window.__c404p=function(){var o={a:act,sd:maxs},n=0,ss={};for(var k in SS){if(n++>=40)break;ss[k]=SS[k]}o.ss=ss;return o};
  window.__c404on=function(k){if(!k||key)return;key=k;flush()};
  iv=setInterval(tick,1000);
  document.addEventListener('visibilitychange',function(){ev(vis()?'vis':'hid');if(!vis()){navTimes();flush(true)}});
  addEventListener('pagehide',function(){ev('end',{n:act});navTimes();flush(true)});
  document.addEventListener('toggle',function(e){var d=e.target;if(d&&d.tagName==='DETAILS'){var s=d.querySelector('summary');ev(d.open?'exp':'col',{l:txt(s&&s.textContent,60),s:(d.closest('[id]')||{}).id||''})}},true);
  document.addEventListener('click',function(e){try{var el=e.target&&e.target.closest&&e.target.closest('[role="tab"],a[href],[data-share]');if(!el)return;
    var sc=el.closest('section[id],header[id],footer[id],article[id]'),sid=sc?sc.id:'';
    if(el.getAttribute('role')==='tab')ev('tab',{l:txt(el.textContent,60),s:sid});
    else if(el.hasAttribute('data-share'))ev('share',{s:sid,m:{ch:txt(el.getAttribute('data-share'),20)}});
    else{var h=el.getAttribute('href')||'';if(el.hasAttribute('download')||/\.(pdf|zip|docx?|xlsx?|pptx?|key|numbers)(\?|#|$)/i.test(h)){var f=h.split(/[?#]/)[0].split('/').pop();ev('dl',{s:sid,m:{file:txt(decodeURIComponent(f),80)}})}}}catch(x){}},true);
  document.addEventListener('copy',function(){var n=0;try{n=String(getSelection()).length}catch(e){}ev('copy',{m:{len:n}})},true);
  addEventListener('beforeprint',function(){ev('print')});
  document.addEventListener('fullscreenchange',function(){if(document.fullscreenElement)ev('fs')});
  var forms={};document.addEventListener('focusin',function(e){var f=e.target&&e.target.form;if(f){var id=txt(f.id||f.getAttribute('name')||'form',30);if(!forms[id]){forms[id]=1;ev('form0',{m:{form:id}})}}},true);
  document.addEventListener('submit',function(e){var f=e.target;ev('form1',{m:{form:txt(f.id||f.getAttribute('name')||'form',30)}})},true);
  try{if(navigator.share){var sh=navigator.share.bind(navigator);navigator.share=function(d){ev('share',{m:{ch:'sistema'}});return sh(d)}}}catch(e){}
  var orient=innerHeight>=innerWidth;addEventListener('resize',function(){var o=innerHeight>=innerWidth;if(o!==orient&&sz<9999){orient=o;ev('resize',{m:{or:o?'vertical':'horizontal'}})}});
  function vname(v){return txt(v.getAttribute('aria-label')||v.title||(v.currentSrc||v.src||'').split('/').pop().split('?')[0]||'vídeo',60)}
  document.addEventListener('play',function(e){var v=e.target;if(v.tagName!=='VIDEO'||v.muted&&v.autoplay&&v.loop)return;playing++;v.__q=v.__q||{};var sc=v.closest('[id]');ev('vplay',{l:vname(v),s:sc?sc.id:''})},true);
  document.addEventListener('pause',function(e){var v=e.target;if(v.tagName!=='VIDEO'||v.muted&&v.autoplay&&v.loop)return;playing=Math.max(0,playing-1);if(!v.ended)ev('vpause',{l:vname(v),n:Math.round(v.currentTime/Math.max(1,v.duration||1)*100)})},true);
  document.addEventListener('timeupdate',function(e){var v=e.target;if(v.tagName!=='VIDEO'||!v.duration||v.muted&&v.autoplay&&v.loop)return;var p=v.currentTime/v.duration*100;v.__q=v.__q||{};[25,50,75].forEach(function(m){if(p>=m&&!v.__q[m]){v.__q[m]=1;ev('vprog',{l:vname(v),n:m})}})},true);
  document.addEventListener('ended',function(e){var v=e.target;if(v.tagName!=='VIDEO'||v.muted&&v.autoplay&&v.loop)return;ev('vend',{l:vname(v)})},true);
  addEventListener('error',function(e){try{var t=e.target;if(t&&t!==window&&t.tagName){if(rerrs++<10){var u=t.currentSrc||t.src||t.href||'';ev('rerr',{m:{tag:t.tagName.toLowerCase(),res:txt(u.split('?')[0].split('/').pop(),80)}})}}else if(errs++<5)ev('err',{m:{msg:txt(e.message,120),src:txt(String(e.filename||'').split('?')[0].split('/').pop(),60),line:e.lineno||0}})}catch(x){}},true);
  addEventListener('unhandledrejection',function(e){if(errs++<5)ev('err',{m:{msg:txt(e.reason&&(e.reason.message||e.reason),120)}})});
  var lcp=0,cls=0;try{new PerformanceObserver(function(l){l.getEntries().forEach(function(x){lcp=Math.round(x.startTime)})}).observe({type:'largest-contentful-paint',buffered:true})}catch(e){}
  try{new PerformanceObserver(function(l){l.getEntries().forEach(function(x){if(!x.hadRecentInput)cls+=x.value})}).observe({type:'layout-shift',buffered:true})}catch(e){}
  function navTimes(){if(sentNav)return;sentNav=true;var m={};try{var n=performance.getEntriesByType('navigation')[0];if(n){m.ttfb=Math.round(n.responseStart);m.dcl=Math.round(n.domContentLoadedEventEnd);m.load=Math.round(n.loadEventEnd)}}catch(e){}
    if(lcp)m.lcp=lcp;m.cls=Math.round(cls*1000)/1000;try{var c=navigator.connection;if(c){if(c.effectiveType)m.net=c.effectiveType;if(c.saveData)m.save='sí'}}catch(e){}ev('nav',{m:m})}
  addEventListener('load',function(){setTimeout(navTimes,6000)});
})();
</script>
"""
STEPS = [
  ("fetch(EP+'/h',{method:'POST',body:JSON.stringify({s:slug})", "fetch(EP+'/h',{method:'POST',body:JSON.stringify({s:slug,x:window.__c404x?__c404x():{}})"),
  (".then(function(j){key=(j&&j.k)||'';push();cflush()})", ".then(function(j){key=(j&&j.k)||'';push();cflush();if(key&&window.__c404on)__c404on(key)})"),
  ("var b=JSON.stringify({k:key,t:Math.round(seen/1000),d:depth,e:gone?1:0});", "var b=JSON.stringify(Object.assign({k:key,t:Math.round(seen/1000),d:depth,e:gone?1:0},window.__c404p?__c404p():{}));"),
]
MARK = '/* visit counter ('
def upgrade(h):
    if V3 in h or 'c404 v2' not in h: return None
    for a, b in STEPS:
        if h.count(a) != 1: return False
    i = h.find('404growth-visits'); s = h.rfind('<script', 0, i)
    if s < 0: return False
    for a, b in STEPS: h = h.replace(a, b)
    return h[:s] + ADDON + h[s:]
if __name__ == '__main__':
    D = sys.argv[1]
    done, skip = [], []
    for f in sorted(os.listdir(D)):
        if not f.endswith('.html'): continue
        p = os.path.join(D, f); h = open(p, encoding='utf-8').read()
        u = upgrade(h)
        if u is None: continue
        if u is False: skip.append(f); continue
        open(p, 'w', encoding='utf-8').write(u); done.append(f)
    print(len(done), 'pages on counter v3;', len(skip), 'with a counter that does not match:', ' '.join(skip))
