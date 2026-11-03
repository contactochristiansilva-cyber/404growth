import os, sys
from PIL import Image, ImageDraw
L = os.environ.get('L31', os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FS = ['hero', 'p1', 'p2', 'p3', 'p4', 'p5', 'x1', 'x2', 'x3', 'look', 'l1', 'l2', 'l3', 'l4', 'l5']
def sheet(slugs, out):
    W, H = 160, 200
    sh = Image.new('RGB', (len(FS) * W, len(slugs) * (H + 18)), 'white'); dr = ImageDraw.Draw(sh)
    for r, s in enumerate(slugs):
        dr.text((4, r * (H + 18) + 2), s, fill='black')
        for k, f in enumerate(FS):
            p = f'{L}/ai/{s}/{f}.jpg'
            if not os.path.exists(p): continue
            im = Image.open(p).convert('RGB'); im.thumbnail((W - 4, H)); sh.paste(im, (k * W, r * (H + 18) + 16))
            dr.text((k * W + 3, r * (H + 18) + 18), f, fill='red')
    sh.save(out, quality=80)
if __name__ == '__main__':
    sheet(sys.argv[2:], sys.argv[1])
