"""Hoja de contacto de las 24 fotos de Instagram de una tienda (numeradas como NN.jpg). uso: igsheet.py <slug>... → l32/sheets/<slug>.jpg"""
import os, sys, json
from PIL import Image, ImageDraw, ImageFont
L31 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 30)
def sheet(s):
    d = f'{L31}/src/l31/{s}'; W, H, C = 330, 412, 6
    out = Image.new('RGB', (C * W + 7 * 6, 4 * H + 5 * 6), 'white'); dr = ImageDraw.Draw(out)
    for k in range(24):
        p = f'{d}/{k + 1:02d}.jpg'
        if not os.path.exists(p): continue
        im = Image.open(p).convert('RGB'); r = max(W / im.width, H / im.height)
        im = im.resize((int(im.width * r) + 1, int(im.height * r) + 1)); x = (im.width - W) // 2; y = (im.height - H) // 2
        im = im.crop((x, y, x + W, y + H)); X = 6 + (k % C) * (W + 6); Y = 6 + (k // C) * (H + 6); out.paste(im, (X, Y))
        dr.rectangle((X, Y, X + 52, Y + 38), fill='black'); dr.text((X + 6, Y + 2), f'{k + 1:02d}', fill='white', font=F)
    os.makedirs(f'{L31}/l32/sheets', exist_ok=True); out.save(f'{L31}/l32/sheets/{s}.jpg', quality=85)
for s in sys.argv[1:]: sheet(s)
