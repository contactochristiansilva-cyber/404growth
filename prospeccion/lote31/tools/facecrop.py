"""Quita las caras de las fotos de IA (recorte a la altura de los labios, como las fotos de producto), para que nadie
se parezca a una persona real de sus fotos de Instagram. Guarda el original como <id>.orig.jpg.
uso: facecrop.py <slug> <id> [<id> ...]   (o --check para solo listar)"""
import os, sys
import cv2
from PIL import Image
L31 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAS = [cv2.CascadeClassifier(cv2.data.haarcascades + f) for f in ['haarcascade_frontalface_default.xml', 'haarcascade_frontalface_alt2.xml', 'haarcascade_profileface.xml']]


def faces(p):
    g = cv2.cvtColor(cv2.imread(p), cv2.COLOR_BGR2GRAY); H, W = g.shape; out = []
    for c in CAS:
        for f in c.detectMultiScale(g, 1.06, 5, minSize=(int(W * .035), int(W * .035))):
            out.append(tuple(int(v) for v in f))
        for f in (c.detectMultiScale(cv2.flip(g, 1), 1.06, 5, minSize=(int(W * .035), int(W * .035))) if c is CAS[2] else []):
            x, y, w, h = f; out.append((W - x - w, y, w, h))
    return out, W, H


def crop(slug, i, check=False):
    p = f'{L31}/ai/{slug}/{i}.jpg'; o = f'{L31}/ai/{slug}/{i}.orig.jpg'
    src = o if os.path.exists(o) else p
    fs, W, H = faces(src)
    fs = [f for f in fs if f[1] + f[3] / 2 < H * .36 and f[2] < W * .5]   # caras en la parte de arriba (las de más abajo suelen ser estampados)
    if not fs:
        return f'{i}: sin cara'
    big = max(f[2] for f in fs); fs = [f for f in fs if f[2] > big * .55]
    cut = max(y + int(h * .78) for x, y, w, h in fs)
    if cut > H * .4:
        return f'{i}: cara demasiado baja ({cut / H:.0%}), revisar a mano'
    if check:
        return f'{i}: recortaría {cut / H:.0%}'
    if not os.path.exists(o):
        os.rename(p, o)
    Image.open(o).convert('RGB').crop((0, cut, W, H)).save(p, 'JPEG', quality=92)
    return f'{i}: recortado {cut / H:.0%}'


if __name__ == '__main__':
    a = sys.argv[1:]; check = '--check' in a; a = [x for x in a if x != '--check']
    for i in a[1:]:
        print(a[0], crop(a[0], i, check))
