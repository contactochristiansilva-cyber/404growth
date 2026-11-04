"""Corta una rejilla 2x2 en 4 fotos. Busca las calles (líneas de un solo color de lado a lado) cerca del centro;
si no las encuentra, corta por la mitad con un pequeño margen.
Uso: gridsplit.py rejilla.jpg ai/<slug>/ p1 x1 x2 x3  → ai/<slug>/p1.jpg … (sirve también para las de Higgsfield)"""
import os, sys
import numpy as np
from PIL import Image


def gutter(a, axis):
    """a: imagen HxWx3 float. axis=1 → busca columna; axis=0 → fila. Devuelve (ini, fin) de la calle o None."""
    n = a.shape[1] if axis == 1 else a.shape[0]
    lo, hi = int(n * .40), int(n * .60)
    # desviación a lo largo de la línea (una calle es uniforme de punta a punta)
    sd = a.std(axis=0).mean(axis=1) if axis == 1 else a.std(axis=1).mean(axis=1)
    seg = sd[lo:hi]; i = lo + int(seg.argmin())
    if sd[i] > 12:
        return None
    thr = max(6.0, sd[i] * 2.5)
    s = i
    while s > lo and sd[s - 1] < thr:
        s -= 1
    e = i
    while e < hi - 1 and sd[e + 1] < thr:
        e += 1
    return s, e + 1


def split(path):
    im = Image.open(path).convert('RGB'); a = np.asarray(im).astype(np.float32)
    H, W = a.shape[:2]
    gx = gutter(a, 1); gy = gutter(a, 0)
    pad = max(4, int(W * .004))
    x0, x1 = (gx[0] - pad, gx[1] + pad) if gx else (int(W / 2 - W * .012), int(W / 2 + W * .012))
    y0, y1 = (gy[0] - pad, gy[1] + pad) if gy else (int(H / 2 - H * .012), int(H / 2 + H * .012))
    # borde exterior: recorta si el modelo dejó marco
    boxes = [(0, 0, x0, y0), (x1, 0, W, y0), (0, y1, x0, H), (x1, y1, W, H)]
    tiles = []
    for b in boxes:
        t = im.crop(b)
        t = trim_frame(t)
        tiles.append(to_45(t))
    return tiles, gx, gy


def trim_frame(t):
    a = np.asarray(t).astype(np.float32); H, W = a.shape[:2]
    def edge(get, n):
        k = 0
        while k < n * .04 and get(k).std(axis=0).mean() < 5 and abs(get(k).mean() - 0) < 25:
            k += 1
        return k
    l = edge(lambda k: a[:, k], W); r = edge(lambda k: a[:, W - 1 - k], W)
    tp = edge(lambda k: a[k], H); bt = edge(lambda k: a[H - 1 - k], H)
    return t.crop((l, tp, W - r, H - bt))


def to_45(t):
    W, H = t.size
    if W / H > .8:
        nw = int(H * .8); x = (W - nw) // 2; return t.crop((x, 0, x + nw, H))
    nh = int(W / .8); y = (H - nh) // 2; return t.crop((0, y, W, y + nh))


def place(src, ids, outdir):
    """Guarda cada trozo como <outdir>/<id>.jpg. Devuelve (calle_x, calle_y); None = no encontró la calle (revisar)."""
    tiles, gx, gy = split(src)
    for i, t in zip(ids, tiles):
        t.save(os.path.join(outdir, i + '.jpg'), 'JPEG', quality=92)
    return gx, gy


if __name__ == '__main__':
    src, base = sys.argv[1], sys.argv[2]; ids = sys.argv[3:] or ['1', '2', '3', '4']
    tiles, gx, gy = split(src)
    print('calles', gx, gy)
    for i, t in zip(ids, tiles):
        out = f'{base}{i}.jpg'; t.save(out, 'JPEG', quality=92); print(out, t.size)
