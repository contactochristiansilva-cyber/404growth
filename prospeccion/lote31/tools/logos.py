"""Su logo de Instagram → PNG transparente en tinta oscura para la cabecera de la tienda."""
import numpy as np, os, sys
from PIL import Image
L31 = os.environ.get('L31', os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CFG = {  # slug: crop box in fractions (x0, y0, x1, y1)
    'alouza-ceramics': (.13, .405, .87, .63), 'apparel-boutique': (.05, .05, .95, .95), 'boutique-alba': (.05, .2, .95, .8),
    'boutique-chica': (.08, .33, .92, .67), 'brilla-fashion': (.05, .2, .98, .625), 'casa-kiki': (.1, .2, .9, .8),
    'con-i-de-iria': (.25, .15, .75, .88), 'el-ropero': (.0, .3, 1, .72), 'maricruz-montecarlo': (.0, .2, 1, .8),
    'modas-pascual': (.05, .3, .95, .7), 'oliver-shopping': (.05, .35, .95, .65), 'rasa-murcia': (.2, .3, .8, .7),
}


def make(slug, ink=(0x14, 0x11, 0x10)):
    im = Image.open(f'{L31}/src/l31/{slug}/logo.jpg').convert('RGB'); w, h = im.size
    x0, y0, x1, y1 = CFG[slug]; im = im.crop((int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h)))
    a = np.asarray(im).astype(float) / 255; lum = a @ [.299, .587, .114]
    b = np.concatenate([a[0], a[-1], a[:, 0], a[:, -1]]); bg = np.median(b, axis=0)
    d = np.sqrt(((a - bg) ** 2).sum(-1))
    al = np.clip((d - .10) / .35, 0, 1)
    ys, xs = np.where(al > .35)
    if not len(ys): print('vacío', slug); return None
    pad = 4; al = al[max(0, ys.min() - pad):ys.max() + pad, max(0, xs.min() - pad):xs.max() + pad]
    o = np.zeros(al.shape + (4,), np.uint8); o[..., :3] = ink; o[..., 3] = (al * 255).astype(np.uint8)
    os.makedirs(f'{L31}/logos', exist_ok=True); p = f'{L31}/logos/{slug}.png'
    Image.fromarray(o, 'RGBA').save(p); print(slug, o.shape[1], 'x', o.shape[0]); return p


if __name__ == '__main__':
    for s in (sys.argv[1:] or CFG):
        make(s)
    # review sheet on white
    ss = sorted(f for f in os.listdir(f'{L31}/logos') if f.endswith('.png'))
    sh = Image.new('RGB', (900, 70 * len(ss)), 'white')
    for k, f in enumerate(ss):
        im = Image.open(f'{L31}/logos/{f}'); r = 50 / im.size[1]; im = im.resize((max(1, int(im.size[0] * r)), 50))
        sh.paste(im, (10, 10 + 70 * k), im)
    sh.save(f'{L31}/logos_check.jpg', quality=85)
