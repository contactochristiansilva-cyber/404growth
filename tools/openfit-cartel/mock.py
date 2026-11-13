import numpy as np, cv2
from PIL import Image
SRC='/mnt/user-data/uploads/Downloads/Open Fit cartel/_src/'
ph=cv2.imread('nave-orig.jpg')                         # BGR 4032x3024
H,W=ph.shape[:2]
clean=cv2.imread('q/clean.jpg')   # sin las marcas verdes (q/clean2.py)
# 2) marquesina y pilares (marrón) → grafito
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
Mf=(cv2.GaussianBlur(M,(0,0),1.2)/255.0)[...,None]
lum=cv2.cvtColor(clean,cv2.COLOR_BGR2GRAY).astype(np.float32)
graf=np.stack([lum*0.30+14,lum*0.30+12,lum*0.30+10],-1)   # gris muy oscuro con su sombreado
# 3) poner los carteles
def warp(png,quad,canvas):
    a=np.asarray(Image.open(png).convert('RGBA')).astype(np.float32)
    rgb=a[...,:3][...,::-1]; al=a[...,3:]/255.0
    h,w=a.shape[:2]
    Hm=cv2.getPerspectiveTransform(np.float32([[0,0],[w,0],[w,h],[0,h]]),np.float32(quad))
    wr=cv2.warpPerspective(rgb,Hm,(W,H),flags=cv2.INTER_AREA if w>2000 else cv2.INTER_LINEAR)
    wa=cv2.warpPerspective(al,Hm,(W,H),flags=cv2.INTER_LINEAR)[...,None]
    wr=cv2.GaussianBlur(wr,(0,0),0.6)
    return canvas*(1-wa)+wr*wa
out=clean.astype(np.float32)
out=warp(SRC+'roof.png',[[1812,690],[3425,617],[3517,937],[1805,992]],out)
out=warp(SRC+'lona.png',[[318,1092],[3512,975],[3745,1792],[5,1840]],out)
out=out*(1-Mf)+graf*Mf
signs=np.zeros((H,W),np.float32)
for png,quad in [(SRC+'roof.png',[[1812,690],[3425,617],[3517,937],[1805,992]]),(SRC+'lona.png',[[318,1092],[3512,975],[3745,1792],[5,1840]])]:
    a=np.asarray(Image.open(png).convert('RGBA'))[...,3].astype(np.float32)/255; h,w=a.shape
    Hm=cv2.getPerspectiveTransform(np.float32([[0,0],[w,0],[w,h],[0,h]]),np.float32(quad))
    signs=np.maximum(signs,cv2.warpPerspective(a,Hm,(W,H)))
signs=signs*(1-Mf[...,0])
np.save('q/signs.npy',cv2.resize(signs,(W//2,H//2)))
night=clean.astype(np.float32)*np.array([0.30,0.20,0.17])        # BGR: azul de anochecer
night=night*(1-Mf)+graf*0.35*Mf
yy=np.linspace(0,1,H)[:,None,None]
night=night*(0.75+0.35*yy)
lit=out*1.0
glow=cv2.GaussianBlur(lit*signs[...,None],(0,0),40)*0.55
nout=night*(1-signs[...,None])+lit*signs[...,None]+glow*(1-signs[...,None])
# luz que cae de los carteles sobre la pared y la acera
spill=cv2.GaussianBlur(signs,(0,0),120)[...,None]*np.array([34,42,52])*(1-signs[...,None])
nout=nout+spill
cv2.imwrite('q/night-full.jpg',np.clip(nout,0,255).astype(np.uint8),[cv2.IMWRITE_JPEG_QUALITY,90])
cv2.imwrite('q/night-1600.jpg',cv2.resize(np.clip(nout,0,255).astype(np.uint8),(1600,1200),interpolation=cv2.INTER_AREA),[cv2.IMWRITE_JPEG_QUALITY,88])
out=np.clip(out,0,255).astype(np.uint8)
cv2.imwrite('q/mock-full.jpg',out,[cv2.IMWRITE_JPEG_QUALITY,90])
cv2.imwrite('q/mock-1600.jpg',cv2.resize(out,(1600,1200),interpolation=cv2.INTER_AREA),[cv2.IMWRITE_JPEG_QUALITY,88])
print('ok')
