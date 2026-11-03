"""Batch de Chrome: abre cada perfil de Instagram, carga ~24 posts y descarga las fotos + meta (alt de cada post) a Descargas
como l31__<slug>__NN.jpg y l31__<slug>__meta.json.  uso: python3 igdl.py <tab> <slug:handle> ..."""
import json, sys
TAB = int(sys.argv[1]); P = [x.split(':', 1) for x in sys.argv[2:]]
JS = r"""
const SL='__SLUG__'; const sleep=t=>new Promise(r=>setTimeout(r,t));
for (let k=0;k<3;k++){ window.scrollTo(0,document.body.scrollHeight); await sleep(1600); }
window.scrollTo(0,0);
const posts=[]; const seen=new Set();
document.querySelectorAll('main a[href*="/p/"], main a[href*="/reel/"]').forEach(a=>{ const i=a.querySelector('img'); if(!i) return; const u=i.currentSrc||i.src; if(!u||seen.has(u)) return; seen.add(u); posts.push({href:a.getAttribute('href'), reel:/\/reel\//.test(a.getAttribute('href')), u:u, w:i.naturalWidth, h:i.naturalHeight, alt:i.alt||''}); });
const hi=document.querySelector('header img'); const og=document.querySelector('meta[property="og:description"]');
const hd=document.querySelector('header'); const meta={slug:SL, path:location.pathname, og:og?og.content:'', header:hd?hd.innerText:'', pic:hi?(hi.currentSrc||hi.src):'', posts:posts.slice(0,24)};
async function dl(u,name){ const r=await fetch(u); const b=await r.blob(); const a=document.createElement('a'); a.href=URL.createObjectURL(b); a.download=name; document.body.appendChild(a); a.click(); a.remove(); await sleep(350); return b.size; }
let n=0, bad=0;
for (let k=0;k<meta.posts.length;k++){ try{ await dl(meta.posts[k].u,'l31__'+SL+'__'+String(k+1).padStart(2,'0')+'.jpg'); n++; }catch(e){ bad++; } }
if (meta.pic){ try{ await dl(meta.pic,'l31__'+SL+'__logo.jpg'); }catch(e){} }
const mb=new Blob([JSON.stringify(meta)],{type:'application/json'}); const a=document.createElement('a'); a.href=URL.createObjectURL(mb); a.download='l31__'+SL+'__meta.json'; document.body.appendChild(a); a.click(); a.remove();
(SL+' posts '+meta.posts.length+' ok '+n+' bad '+bad+' pic '+(meta.pic?'si':'no')).replace(/[=;&?]/g,' ')
"""
A = []
for slug, h in P:
    A += [{"name": "navigate", "input": {"tabId": TAB, "url": f"https://www.instagram.com/{h}/"}},
          {"name": "computer", "input": {"action": "wait", "tabId": TAB, "duration": 4}},
          {"name": "javascript_tool", "input": {"tabId": TAB, "action": "javascript_exec", "text": JS.replace('__SLUG__', slug)}}]
print(json.dumps(A, ensure_ascii=False))
