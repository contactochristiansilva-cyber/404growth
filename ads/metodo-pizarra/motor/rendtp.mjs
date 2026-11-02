import {createRequire} from 'module';import {spawn} from 'child_process';import fs from 'fs';
const require=createRequire('/usr/lib/node_modules/');const {chromium}=require('playwright');
const [,,file,out]=process.argv;const FPS=25;
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1280,height:720}});
await p.goto('file://'+file);await p.evaluate(()=>document.fonts.ready);const total=await p.evaluate(()=>TOTAL);const n=Math.ceil(total*FPS);
const ff=spawn('ffmpeg',['-y','-loglevel','error','-f','image2pipe','-c:v','mjpeg','-framerate',String(FPS),'-i','-','-c:v','libx264','-preset','veryfast','-crf','24','-pix_fmt','yuv420p','-r',String(FPS),out+'.tmp.mp4'],{stdio:['pipe','inherit','inherit']});
for(let f=0;f<n;f++){await p.evaluate(t=>render(t),f/FPS);const buf=await p.screenshot({type:'jpeg',quality:88});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r))}
const done=new Promise(r=>ff.on('exit',r));ff.stdin.end();await b.close();const c=await done;if(c===0){fs.renameSync(out+'.tmp.mp4',out);console.log('ok',out)}else{console.log('FAIL',out);process.exit(1)}
