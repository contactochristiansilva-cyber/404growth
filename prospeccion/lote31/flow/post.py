# Flow (3:4 / 16:9, 2K) -> tamaños del pipeline de propuestas. Uso: python3 post.py <slug> <carpeta origen>
import sys, os
from PIL import Image
slug, src = sys.argv[1], sys.argv[2]
out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ai', slug)  # l31/ai/<slug>
os.makedirs(out, exist_ok=True)
SZ = {'hero': (2752, 1536), 'l5': (2752, 1536)}
for k in ['p1','p2','p3','p4','p5','x1','x2','x3','look']: SZ[k] = (1209, 1511)
for k in ['l1','l2','l3','l4']: SZ[k] = (912, 1140)
for k, (W, H) in SZ.items():
    f = os.path.join(src, k + '.jpg')
    if not os.path.exists(f): print('FALTA', k); continue
    im = Image.open(f).convert('RGB'); w, h = im.size
    r = W / H
    if abs(w / h - r) > .01:
        if w / h > r:  # demasiado ancha: recorta a los lados
            nw = round(h * r); x = (w - nw) // 2; im = im.crop((x, 0, x + nw, h))
        else:          # demasiado alta (3:4 -> 4:5): recorta arriba y abajo a partes iguales
            nh = round(w / r); y = (h - nh) // 2; im = im.crop((0, y, w, y + nh))
    im = im.resize((W, H), Image.LANCZOS)
    im.save(os.path.join(out, k + '.jpg'), quality=90, optimize=True, progressive=True)
    print(k, im.size)
