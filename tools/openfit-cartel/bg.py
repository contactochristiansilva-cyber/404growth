import numpy as np, cv2
from PIL import Image, ImageFilter, ImageOps
F='/mnt/user-data/uploads/Downloads/Open Fit cartel/fotos Flow/'
W,H=5000,920
def load(n): return Image.open(F+n+'.jpg').convert('RGB')
# fondo: la nave por dentro, oscurecida, con los lados casi negros
nave=load('nave1'); s=W/nave.width; nv=nave.resize((W,int(nave.height*s)),Image.LANCZOS)
oy=int(0.36*nv.height); bg=np.asarray(nv.crop((0,oy,W,oy+H))).astype(np.float32)/255
bg=cv2.GaussianBlur(bg,(0,0),1.6)
x=np.linspace(0,1,W)[None,:,None]
side=np.clip(1-np.abs(x-0.48)/0.48,0,1)**1.3          # 1 en el centro, 0 en los extremos
bri=0.10+0.42*side
y=np.linspace(0,1,H)[:,None,None]
bri=bri*(0.75+0.25*np.sin(np.pi*np.clip(y,0,1)))         # un poco más oscuro arriba y abajo
bg=bg*bri
def athlete(name, mirror, height_px, top_frac, bottom_frac):
    im=load(name)
    if mirror: im=ImageOps.mirror(im)
    a=np.asarray(Image.open('cut/'+name+'.png').split()[-1]).astype(np.float32)/255
    if mirror: a=a[:,::-1]
    lum=np.asarray(im.convert('L')).astype(np.float32)/255
    near=cv2.GaussianBlur(cv2.dilate(a,np.ones((71,71),np.uint8)),(0,0),18)
    m=np.maximum(a, np.clip((lum-0.12)/0.12,0,1)*near)      # el atleta + lo que tiene luz cerca de él (discos, tiza)
    m=cv2.dilate(m,np.ones((5,5),np.uint8)); m=cv2.GaussianBlur(m,(0,0),6)
    h,w=m.shape; ex=np.minimum(np.arange(w)/(0.06*w),1)*np.minimum((w-1-np.arange(w))/(0.06*w),1)
    ey=np.minimum((h-1-np.arange(h))/(0.05*h),1)
    m=m*ex[None,:]*ey[:,None]
    s=height_px/((bottom_frac-top_frac)*im.height)
    im=im.resize((int(im.width*s),int(im.height*s)),Image.LANCZOS)
    m=cv2.resize(m,im.size,interpolation=cv2.INTER_LINEAR)
    return np.asarray(im).astype(np.float32)/255, np.clip(m,0,1)[...,None], s
def paste(bg,img,m,x0,y0):
    h,w=img.shape[:2]; X0,Y0=max(0,x0),max(0,y0); X1,Y1=min(W,x0+w),min(H,y0+h)
    sub=img[Y0-y0:Y1-y0,X0-x0:X1-x0]; mm=m[Y0-y0:Y1-y0,X0-x0:X1-x0]
    bg[Y0:Y1,X0:X1]=bg[Y0:Y1,X0:X1]*(1-mm)+sub*mm
# ella a la izquierda (espejada, mira al centro); él a la derecha
wi,wm,ws=athlete('woman2',True,850,0.05,0.97)
paste(bg,wi,wm,260-int(0.06*wi.shape[1]),40-int(0.05*wi.shape[0]))
mi,mm,ms=athlete('man2',False,860,0.08,0.95)
paste(bg,mi,mm,4920-int(0.97*mi.shape[1]),36-int(0.08*mi.shape[0]))
out=(np.clip(bg,0,1)*255).astype(np.uint8)
Image.fromarray(out).save('q/lona-bg.jpg',quality=93)
Image.fromarray(out).resize((1250,230)).save('q/lona-bg-prev.jpg',quality=85)
print('ok', wi.shape, mi.shape)
