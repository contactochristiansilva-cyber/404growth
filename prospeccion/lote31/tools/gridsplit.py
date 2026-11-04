"""Corta una rejilla 2x2 en 4 fotos. Busca las calles (líneas de un solo color de lado a lado) cerca del centro;
si no las encuentra, corta por la mitad con un pequeño margen.
Uso: gridsplit.py rejilla.jpg ai/<slug>/ p1 x1 x2 x3  → ai/<slug>/p1.jpg … (sirve también para las de Higgsfield)"""
import os, sys
import numpy as np
from PIL import Image


def gutter(a, axis, f=.5):
    """a: imagen HxWx3 float. axis=1 → busca columna; axis=0 → fila, cerca de la fracción f. Devuelve (ini, fin) o None."""
    n = a.shape[1] if axis == 1 else a.shape[0]
    lo, hi = int(n * (f - .1)), int(n * (f + .1))
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


def split(path, n=2):
    """Rejilla n×n → n·n trozos en orden de lectura (izquierda a derecha, arriba a abajo)."""
    im = Image.open(path).convert('RGB'); a = np.asarray(im).astype(np.float32)
    H, W = a.shape[:2]; pad = max(4, int(W * .004))
    def cuts(axis, N):
        r = []
        for k in range(1, n):
            g = gutter(a, axis, k / n)
            r.append((g[0] - pad, g[1] + pad) if g else (int(N * k / n - N * .012), int(N * k / n + N * .012)))
        return r, all(gutter(a, axis, k / n) for k in range(1, n))
    gx, okx = cuts(1, W); gy, oky = cuts(0, H)
    xs = [0] + [v for g in gx for v in g] + [W]; ys = [0] + [v for g in gy for v in g] + [H]
    tiles = []
    for r in range(n):
        for c in range(n):
            t = im.crop((xs[2 * c], ys[2 * r], xs[2 * c + 1], ys[2 * r + 1]))
            tiles.append(to_45(trim_frame(t)))
    return tiles, (gx if okx else None), (gy if oky else None)


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
    """Guarda cada trozo como <outdir>/<id>.jpg (4 ids = 2x2, 9 ids = 3x3). Devuelve (calles_x, calles_y); None = no las encontró (revisar)."""
    tiles, gx, gy = split(src, 3 if len(ids) == 9 else 2)
    for i, t in zip(ids, tiles):
        t.save(os.path.join(outdir, i + '.jpg'), 'JPEG', quality=92)
    return gx, gy


if __name__ == '__main__':
    src, base = sys.argv[1], sys.argv[2]; ids = sys.argv[3:] or ['1', '2', '3', '4']
    tiles, gx, gy = split(src, 3 if len(ids) == 9 else 2)
    print('calles', gx, gy)
    for i, t in zip(ids, tiles):
        out = f'{base}{i}.jpg'; t.save(out, 'JPEG', quality=92); print(out, t.size)
