import json,subprocess,os,sys,numpy as np
from rembg import new_session, remove
from PIL import Image
S=json.load(open('spec.json'));V=sys.argv[1];os.makedirs('masks',exist_ok=True)
sess=new_session('u2net_human_seg')
FPS=25
for f in S['float']:
    a=int(f['t0']*FPS)-2;b=min(int(f['t1']*FPS)+2,int(S['dur']*FPS)-1)
    r=subprocess.run(['ffmpeg','-v','error','-ss',str(a/FPS),'-i',V,'-frames:v',str(b-a+1),'-vf','scale=960:540','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True)
    fr=np.frombuffer(r.stdout,np.uint8).reshape(-1,540,960,3)
    for k,im in enumerate(fr):
        n=a+k
        if os.path.exists(f'masks/{n:05d}.png'):continue
        m=remove(Image.fromarray(im),session=sess,only_mask=True)
        m.save(f'masks/{n:05d}.png')
    print(f['kind'],a,b,flush=True)
print('fin')
