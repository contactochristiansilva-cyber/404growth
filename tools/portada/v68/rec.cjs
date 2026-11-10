const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
for(const [n,w,h] of [['d',1440,900],['m',390,844]]){
 const c=await b.newContext({viewport:{width:w,height:h},recordVideo:{dir:'vid_'+n,size:{width:w,height:h}}});
 const p=await c.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('http://localhost:8765/index.html');await p.waitForTimeout(2600);
 console.log(n,'errs',errs, await p.evaluate(()=>[!!document.getElementById('l404'),document.documentElement.className]));
 await c.close()}
await b.close()})();
