import {createRequire} from 'module';import {spawn} from 'child_process';import fs from 'fs';
const require=createRequire('/usr/lib/node_modules/');const {chromium}=require('playwright');
const [,,file,outA,outB,f0,f1]=process.argv;const FPS=25;
const ff=spawn('ffmpeg',['-y','-loglevel','error','-f','image2pipe','-c:v','mjpeg','-framerate',String(FPS),'-i','-',
 '-filter_complex','[0:v]split=2[a][b];[a]crop=1080:1080:0:0[c]',
 '-map','[c]','-c:v','libx264','-preset','veryfast','-crf','17','-pix_fmt','yuv420p','-r',String(FPS),outA+'.tmp.mp4',
 '-map','[b]','-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-r',String(FPS),outB+'.tmp.mp4'],{stdio:['pipe','inherit','inherit']});
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1340}});
await p.goto('file://'+file);await p.evaluate(()=>document.fonts.ready);
for(let f=+f0;f<+f1;f++){await p.evaluate(t=>render(t),f/FPS);const buf=await p.screenshot({type:'jpeg',quality:92,clip:{x:0,y:0,width:1080,height:1340}});
 if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r));if(f%250===0)console.error(outA,f)}
ff.stdin.end();await b.close();
ff.on('exit',c=>{if(c===0){fs.renameSync(outA+'.tmp.mp4',outA);fs.renameSync(outB+'.tmp.mp4',outB);console.error('done',outA)}else console.error('ffmpeg fail',c)});
