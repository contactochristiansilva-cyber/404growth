"""cmp.py <gen.png> <out.jpg>: original (enlarged) vs generated, same regions, side by side."""
import sys
from PIL import Image, ImageDraw
SRC = '/tmp/claude-0/-home-claude/a676b6bb-0020-5a51-9455-0108b5df14a8/scratchpad/intenso/theme/assets/tienda.jpg'
o = Image.open(SRC).convert('RGB'); g = Image.open(sys.argv[1]).convert('RGB')
oW, oH = o.size; gW, gH = g.size
# regions as fractions of the photo: the desktop strip, the logo, the shelves
R = {'franja': (0, 0.315, 1, 0.52), 'logo': (0.02, 0.33, 0.33, 0.43), 'baldas': (0.55, 0.36, 0.9, 0.5)}
rows = []
for name, (x0, y0, x1, y1) in R.items():
    a = o.crop((int(x0*oW), int(y0*oH), int(x1*oW), int(y1*oH)))
    b = g.crop((int(x0*gW), int(y0*gH), int(x1*gW), int(y1*gH)))
    w = 900; h = int(w * b.height / b.width)
    a = a.resize((w, h), Image.BICUBIC); b = b.resize((w, h), Image.LANCZOS)
    row = Image.new('RGB', (2*w + 20, h + 30), 'white'); d = ImageDraw.Draw(row)
    row.paste(a, (0, 30)); row.paste(b, (w + 20, 30))
    d.text((6, 8), name + ' · original', fill='black'); d.text((w + 26, 8), name + ' · nueva ' + '%dx%d' % g.size, fill='black')
    rows.append(row)
H = sum(r.height for r in rows) + 10*len(rows)
out = Image.new('RGB', (rows[0].width, H), 'white'); y = 0
for r in rows: out.paste(r, (0, y)); y += r.height + 10
out.save(sys.argv[2], quality=88)
print(out.size)
