import {createRequire} from 'module';const require=createRequire('/usr/lib/node_modules/');
let pw;try{pw=require('playwright')}catch(e){pw=createRequire(process.cwd()+'/')('playwright')}
const {chromium}=pw;
const [,,file,out,...ts]=process.argv;
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1340}});
await p.goto('file://'+file);await p.evaluate(()=>document.fonts.ready);
for(const t of ts){await p.evaluate(t=>render(+t),t);await p.screenshot({path:`${out}/s_${t}.jpg`,type:'jpeg',quality:90,clip:{x:0,y:0,width:1080,height:1340}})}
await b.close();
