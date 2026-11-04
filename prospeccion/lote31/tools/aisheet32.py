"""Hoja de revisión de las 15 fotos de IA de una tienda (en orden de la página). uso: aisheet32.py <slug> → l32/ai_<slug>.jpg"""
import os, sys
from PIL import Image, ImageDraw, ImageFont
L31 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 20)
def fit(p, w, h):
    im = Image.open(p).convert('RGB'); r = max(w / im.width, h / im.height); im = im.resize((int(im.width * r) + 1, int(im.height * r) + 1))
    x = (im.width - w) // 2; y = (im.height - h) // 2; return im.crop((x, y, x + w, y + h))
for s in sys.argv[1:]:
    d = f'{L31}/ai/{s}'; W, H = 230, 288
    out = Image.new('RGB', (8 * (W + 4) + 4, 2 * (H + 4) + 4 + 300), 'white'); dr = ImageDraw.Draw(out)
    ids = ['p1', 'x1', 'x2', 'x3', 'p2', 'p3', 'p4', 'p5', 'look', 'l1', 'l2', 'l3', 'l4']
    for k, i in enumerate(ids):
        X = 4 + (k % 8) * (W + 4); Y = 4 + (k // 8) * (H + 4); out.paste(fit(f'{d}/{i}.jpg', W, H), (X, Y)); dr.text((X + 4, Y + 2), i, fill='white', font=F, stroke_width=2, stroke_fill='black')
    for k, i in enumerate(['hero', 'l5']):
        X = 4 + k * 535 + (3 * (W + 4) if False else 0); Y = 2 * (H + 4) + 4
        X = 4 + 5 * (W + 4) if False else 4 + k * 540
        out.paste(fit(f'{d}/{i}.jpg', 530, 298), (X, Y)); dr.text((X + 4, Y + 2), i, fill='white', font=F, stroke_width=2, stroke_fill='black')
    out.save(f'{L31}/l32/ai_{s}.jpg', quality=82)
