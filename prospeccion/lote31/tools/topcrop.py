"""Recorta por arriba (fracción de la altura) para quitar caras que se parecen a personas reales de sus fotos. El original queda en <id>.orig.jpg.
uso: topcrop.py <slug> <id>=<fracción> ..."""
import os, sys
from PIL import Image
L31 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s = sys.argv[1]
for a in sys.argv[2:]:
    i, f = a.split('='); f = float(f)
    p = f'{L31}/ai/{s}/{i}.jpg'; o = f'{L31}/ai/{s}/{i}.orig.jpg'
    if not os.path.exists(o): os.rename(p, o)
    im = Image.open(o).convert('RGB'); W, H = im.size
    im.crop((0, int(H * f), W, H)).save(p, 'JPEG', quality=92); print(s, i, f, im.size, '->', (W, H - int(H * f)))
