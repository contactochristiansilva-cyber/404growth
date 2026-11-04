"""Coloca una imagen de Higgsfield (descargada a Descargas y pasada a uploads) como ai/<slug>/<id>.jpg; el anterior queda en <id>.orig.jpg.
uso: hfplace.py <png> <slug> <id>"""
import os, sys
from PIL import Image
L31 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src, s, i = sys.argv[1:4]
p = f'{L31}/ai/{s}/{i}.jpg'; o = f'{L31}/ai/{s}/{i}.orig.jpg'
if os.path.exists(p) and not os.path.exists(o): os.rename(p, o)
im = Image.open(src).convert('RGB'); im.save(p, 'JPEG', quality=93); print(s, i, im.size)
