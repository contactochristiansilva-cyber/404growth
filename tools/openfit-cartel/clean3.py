import numpy as np, cv2
o=cv2.imread('nave-orig.jpg'); H,W=o.shape[:2]
c=cv2.imread('/mnt/user-data/uploads/Downloads/Open Fit cartel/_src/clean1.jpg')     # limpia hecha con Flow (Nano Banana Pro)
cu=cv2.resize(c,(W,H),interpolation=cv2.INTER_LANCZOS4)
# un poco de nitidez para que el parche no se vea blando
cu=cv2.addWeighted(cu,1.5,cv2.GaussianBlur(cu,(0,0),2.2),-0.5,0)
hsv=cv2.cvtColor(o,cv2.COLOR_BGR2HSV)
g=((hsv[...,0]>50)&(hsv[...,0]<100)&(hsv[...,1]>70)&(hsv[...,2]>120)).astype(np.uint8)*255
g=cv2.dilate(g,np.ones((31,31),np.uint8))
a=(cv2.GaussianBlur(g,(0,0),8)/255.0)[...,None]
out=(o*(1-a)+cu*a).astype(np.uint8)
cv2.imwrite('q/clean.jpg',out,[cv2.IMWRITE_JPEG_QUALITY,93])
print('ok')
