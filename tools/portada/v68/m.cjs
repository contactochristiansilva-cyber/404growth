const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
for(const [w,h] of [[1440,900],[390,844]]){const p=await b.newPage({viewport:{width:w,height:h}});
 await p.goto('http://localhost:8765/index.html',{waitUntil:'commit'});
 const r=await p.evaluate(()=>new Promise(res=>{const f=()=>{const c=document.documentElement.className;if(c.includes('l404-land')){const q=e=>{const x=document.querySelector(e).getBoundingClientRect();return [x.left,x.top,x.width,x.height].map(v=>Math.round(v))};res({lw:q('#l404 .lw:not(.gh)'),mk:q('.nv-logo .mk'),t:performance.now()|0})}else requestAnimationFrame(f)};f()}));
 console.log(w,JSON.stringify(r))}
await b.close()})();
