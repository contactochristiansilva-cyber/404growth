# Recortes de alta resolución del montaje de día, para el recorrido con zoom (mismo resultado que mock.py, a más píxeles)
import numpy as np, cv2, json
from PIL import Image
SRC='/mnt/user-data/uploads/Downloads/Open Fit cartel/_src/'
clean=cv2.imread('q/clean.jpg'); H,W=clean.shape[:2]
reg=np.zeros((H,W),np.uint8); cv2.rectangle(reg,(830,1600),(2730,2500),255,-1)
hsv=cv2.cvtColor(clean,cv2.COLOR_BGR2HSV)
b,gg,r=[clean[...,i].astype(int) for i in range(3)]
brown=((r-b>18)&(r>gg)&(hsv[...,1]>35)&(hsv[...,2]<215)&(hsv[...,2]>50)).astype(np.uint8)*255
brown=cv2.bitwise_and(brown,reg)
below=np.zeros((H,W),np.uint8); cv2.fillPoly(below,[np.int32([[830,1650],[2730,1630],[2730,2500],[830,2500]])],255)
brown=cv2.bitwise_and(brown,below)
brown=cv2.morphologyEx(brown,cv2.MORPH_OPEN,np.ones((5,5),np.uint8))
brown=cv2.morphologyEx(brown,cv2.MORPH_CLOSE,np.ones((15,15),np.uint8))
face=np.zeros((H,W),np.uint8)
cv2.fillPoly(face,[np.int32([[922,1645],[2682,1625],[2694,1724],[2694,1752],[909,1760],[909,1738]])],255)
M=np.maximum(brown,face)
SIGNS=[(SRC+'roof.png',[[1812,690],[3425,617],[3517,937],[1805,992]]),(SRC+'lona.png',[[318,1092],[3512,975],[3745,1792],[5,1840]])]
srcs={p:np.asarray(Image.open(p).convert('RGBA')).astype(np.float32) for p,_ in SIGNS}
def patch(name,x0,y0,x1,y1,k):
    cw,ch=int((x1-x0)*k),int((y1-y0)*k)
    base=cv2.resize(clean[y0:y1,x0:x1],(cw,ch),interpolation=cv2.INTER_LANCZOS4).astype(np.float32)
    mm=cv2.resize(M[y0:y1,x0:x1],(cw,ch),interpolation=cv2.INTER_LINEAR)
    out=base
    for p,quad in SIGNS:
        a=srcs[p]; h,w=a.shape[:2]
        q=(np.float32(quad)-np.float32([x0,y0]))*k
        Hm=cv2.getPerspectiveTransform(np.float32([[0,0],[w,0],[w,h],[0,h]]),q)
        rgb=a[...,:3][...,::-1].copy(); al=a[...,3]/255.0
        wr=cv2.warpPerspective(rgb,Hm,(cw,ch),flags=cv2.INTER_AREA)
        wa=cv2.warpPerspective(al,Hm,(cw,ch),flags=cv2.INTER_LINEAR)[...,None]
        wr=cv2.GaussianBlur(wr,(0,0),0.5)
        out=out*(1-wa)+wr*wa
    lum=cv2.cvtColor(np.clip(base,0,255).astype(np.uint8),cv2.COLOR_BGR2GRAY).astype(np.float32)
    graf=np.stack([lum*0.30+14,lum*0.30+12,lum*0.30+10],-1)
    Mf=(cv2.GaussianBlur(mm,(0,0),1.2*k)/255.0)[...,None]
    out=out*(1-Mf)+graf*Mf
    cv2.imwrite(f'q/web/{name}.jpg',np.clip(out,0,255).astype(np.uint8),[cv2.IMWRITE_JPEG_QUALITY,82])
    return {'n':name,'x':x0,'y':y0,'w':x1-x0,'h':y1-y0}
import os; os.makedirs('q/web',exist_ok=True)
P=[patch('d-rotulo',1720,560,3580,1040,1.9),
   patch('d-titular',1020,1080,2600,1600,2.0),
   patch('d-ella',20,1040,1040,1890,2.5),
   patch('d-el',2420,960,3760,1660,2.0)]
json.dump(P,open('q/web/patches.json','w'))
# bases: día y noche a 4032 y 2400
for n,f in [('dia','q/mock-full.jpg'),('noche','q/night-full.jpg')]:
    im=Image.open(f); im.save(f'q/web/{n}-4032.jpg',quality=80,progressive=True,optimize=True)
    im.resize((2400,1800),Image.LANCZOS).save(f'q/web/{n}-2400.jpg',quality=82,progressive=True,optimize=True)
Image.open('/mnt/user-data/uploads/Downloads/Open Fit cartel/_src/lona.png').save('q/web/plano-lona.png',optimize=True)
Image.open('/mnt/user-data/uploads/Downloads/Open Fit cartel/_src/roof.png').convert('RGB').save('q/web/plano-rotulo.jpg',quality=88)
print(P)
for f in sorted(os.listdir('q/web')): print(f, os.path.getsize('q/web/'+f)//1024,'KB', Image.open('q/web/'+f).size if f.endswith(('jpg','png')) else '')
