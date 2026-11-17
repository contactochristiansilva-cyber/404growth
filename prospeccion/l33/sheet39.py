import os, sys
from PIL import Image, ImageDraw
ai = sys.argv[1]; out = sys.argv[2]; os.makedirs(out, exist_ok=True)
slugs = sorted(os.listdir(ai)); order = ['h','b','hm','p1','p2','p3','p4','p5','p6','l1','l2']
H = 170
for g in range(0, len(slugs), 3):
    rows = []
    for s in slugs[g:g+3]:
        ims = []
        for k in order:
            p = f'{ai}/{s}/{k}.jpg'
            if os.path.exists(p):
                im = Image.open(p).convert('RGB'); im.thumbnail((10000, H)); ims.append((k, im))
        w = sum(i.width for _, i in ims) + 4*len(ims) + 160
        row = Image.new('RGB', (w, H+4), 'white'); d = ImageDraw.Draw(row)
        d.text((4, 4), s, fill='black'); x = 160
        for k, im in ims:
            row.paste(im, (x, 2)); d.text((x+3, 3), k, fill='red'); x += im.width + 4
        rows.append(row)
    W = max(r.width for r in rows); sh = Image.new('RGB', (W, sum(r.height for r in rows)), 'white'); y = 0
    for r in rows: sh.paste(r, (0, y)); y += r.height
    sh.save(f'{out}/s{g//3:02d}.jpg', quality=82)
print('ok')
