// render.mjs <html> <out.mp4> <f0> <f1> [crf]  → pizarra limpia 1080×1080, PNG sin pérdidas → x264 veryslow
import {createRequire} from 'module';import {spawn} from 'child_process';import fs from 'fs';
const require=createRequire('/usr/lib/node_modules/');const {chromium}=require('playwright');
const [,,file,out,f0,f1,crf='18']=process.argv;const FPS=25;
const ff=spawn('ffmpeg',['-y','-loglevel','error','-f','image2pipe','-c:v','png','-framerate',String(FPS),'-i','-',
 '-c:v','libx264','-preset','veryslow','-tune','animation','-crf',crf,'-pix_fmt','yuv420p','-r',String(FPS),'-movflags','+faststart',out+'.tmp.mp4'],{stdio:['pipe','inherit','inherit']});
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1080}});
await p.goto('file://'+file);await p.evaluate(()=>document.fonts.ready);
for(let f=+f0;f<+f1;f++){await p.evaluate(t=>render(t),f/FPS);const buf=await p.screenshot({type:'png',clip:{x:0,y:0,width:1080,height:1080}});
 if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r))}
ff.stdin.end();await b.close();
ff.on('exit',c=>{if(c===0){fs.renameSync(out+'.tmp.mp4',out);console.log('ok',out)}else console.log('FAIL',out,c)});
