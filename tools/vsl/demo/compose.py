#!/usr/bin/env python3
"""Monta la demo del VSL: vídeo base con zooms + recortes de B-roll + capa de animación (PNG) + glass.
uso: python3 compose.py <video base> <carpeta frames png> <b1.mp4> <b2.mp4> <salida_video_mudo.mp4>
Los tiempos (zoom, B-roll, glass) van en las tablas de abajo, en segundos del VSL."""
import sys, subprocess, numpy as np, cv2, os

V, FR, B1, B2, OUT = sys.argv[1:6]
FPS, W, H = 25, 1920, 1080
N = len([f for f in os.listdir(FR) if f.endswith('.png')])
DUR = N / FPS

cl = lambda x, a=0., b=1.: max(a, min(b, x))
eo = lambda x: 1 - (1 - cl(x)) ** 3
eio = lambda x: (4 * cl(x) ** 3) if cl(x) < .5 else 1 - (-2 * cl(x) + 2) ** 3 / 2
P = lambda t, a, d: cl((t - a) / d)

# --- zoom: (t0, t1, escala inicial, escala final). Entre tramos, corte seco salvo los marcados con ease ---
Z = [(0.00, 1.84, 1.00, 1.06), (1.84, 4.16, 1.20, 1.23), (4.16, 5.44, 1.04, 1.07), (5.44, 8.48, 1.12, 1.16),
     (8.48, 9.30, 1.18, 1.20), (9.30, 10.00, 1.30, 1.33), (10.00, 17.20, 1.00, 1.05), (17.20, 20.70, 1.17, 1.22),
     (20.70, 25.92, 1.10, 1.10), (25.92, 28.20, 1.12, 1.16), (28.20, 30.35, 1.00, 1.04), (30.35, 32.10, 1.24, 1.28),
     (32.10, 40.00, 1.10, 1.10), (40.00, 42.15, 1.10, 1.14), (42.15, 44.00, 1.26, 1.30), (44.00, 99.0, 1.00, 1.05)]
EASE = {9.30: .14, 10.00: .40}   # transiciones suaves (duración) al empezar esos tramos
CX, CY = 950, 400


def zoom_at(t):
    for k, (a, b, s0, s1) in enumerate(Z):
        if a <= t < b:
            s = s0 + (s1 - s0) * (t - a) / (b - a if b < 90 else DUR - a)
            d = EASE.get(a)
            if d and t < a + d and k:
                pa, pb, ps0, ps1 = Z[k - 1]
                prev = ps1
                s = prev + (s - prev) * eio((t - a) / d)
            return s
    return 1.0


def crop_zoom(img, s):
    if abs(s - 1) < 1e-3:
        return img
    w, h = W / s, H / s
    x = cl(CX - w / 2, 0, W - w); y = cl(CY - h * 0.47, 0, H - h)
    M = np.float32([[s, 0, -x * s], [0, s, -y * s]])
    return cv2.warpAffine(img, M, (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)


def rrect_mask(w, h, r):
    m = np.zeros((h, w), np.uint8)
    cv2.rectangle(m, (r, 0), (w - r - 1, h - 1), 255, -1); cv2.rectangle(m, (0, r), (w - 1, h - r - 1), 255, -1)
    for cx, cy in ((r, r), (w - r - 1, r), (r, h - r - 1), (w - r - 1, h - r - 1)):
        cv2.circle(m, (cx, cy), r, 255, -1, cv2.LINE_AA)
    return cv2.GaussianBlur(m, (3, 3), 0).astype(np.float32) / 255


# --- B-roll en tarjeta: (archivo, entra, sale, segundo del clip donde empieza) ---
BR = [(B1, 1.90, 4.16, 0.6), (B2, 30.45, 32.04, 0.8)]
CW, CHh, CXp, CYp, CR = 600, 338, 1250, 120, 28
clips = {}
for f, *_ in BR:
    cap = cv2.VideoCapture(f); fr = []; fps = cap.get(cv2.CAP_PROP_FPS) or 24
    while True:
        ok, im = cap.read()
        if not ok: break
        fr.append(cv2.resize(im, (CW, CHh), interpolation=cv2.INTER_AREA))
    clips[f] = (fr, fps)
CMASK = rrect_mask(CW, CHh, CR)
# sombra suave neutra
SH = np.zeros((H, W), np.float32)


def put_card(img, t):
    for f, a, b, off in BR:
        if a - .01 <= t <= b + .2:
            fr, fps = clips[f]
            k = min(len(fr) - 1, int((t - a + off) * fps))
            i = eo(P(t, a, .24)); o = P(t, b, .18)
            op = i * (1 - o)
            if op <= 0: return img
            sc = .9 + .1 * i - .04 * o
            w, h = int(CW * sc), int(CHh * sc)
            tile = cv2.resize(fr[k], (w, h), interpolation=cv2.INTER_AREA).astype(np.float32)
            m = cv2.resize(CMASK, (w, h))
            x = int(CXp + (CW - w) / 2); y = int(CYp + (CHh - h) / 2 + 30 * (1 - i))
            # sombra (neutra, desplazada)
            sm = np.zeros((h + 120, w + 120), np.float32); sm[60:60 + h, 60:60 + w] = m
            sm = cv2.GaussianBlur(sm, (0, 0), 22) * .38 * op
            sy, sx = y - 60 + 18, x - 60
            reg = img[sy:sy + sm.shape[0], sx:sx + sm.shape[1]]
            reg *= (1 - sm[:reg.shape[0], :reg.shape[1], None])
            # borde fino claro
            reg = img[y:y + h, x:x + w]
            mm = (m * op)[:, :, None]
            img[y:y + h, x:x + w] = reg * (1 - mm) + tile * mm
            edge = (cv2.dilate(m, np.ones((3, 3))) - cv2.erode(m, np.ones((3, 3)))) * .35 * op
            img[y:y + h, x:x + w] += (255 - img[y:y + h, x:x + w]) * edge[:, :, None]
    return img


# --- cristal: desenfoca el vídeo detrás de las tarjetas (rect, radio, entra, sale, dx, dy, din, dout) ---
GL = [((96, 838, 434, 132), 26, 10.96, 16.85, -60, 0, .28, .2), ((1242, 190, 538, 93), 46, 29.62, 30.30, 0, -20, .22, .16),
      ((1320, 130, 470, 560), 34, 44.10, 46.20, 50, 0, .28, .2)]
GM = {g[0]: rrect_mask(g[0][2], g[0][3], g[1]) for g in GL}


def glass(img, t):
    for (x, y, w, h), r, a, b, dx, dy, din, dout in GL:
        if a <= t <= b + dout:
            i = eo(P(t, a, din)); o = P(t, b, dout); op = i * (1 - o)
            if op <= 0: continue
            X = int(x + dx * (1 - i)); Y = int(y + dy * (1 - i) - 10 * o)
            X = int(cl(X, 0, W - w)); Y = int(cl(Y, 0, H - h))
            pad = 40
            x0, y0, x1, y1 = max(0, X - pad), max(0, Y - pad), min(W, X + w + pad), min(H, Y + h + pad)
            bl = cv2.GaussianBlur(img[y0:y1, x0:x1], (0, 0), 18)[Y - y0:Y - y0 + h, X - x0:X - x0 + w]
            m = (GM[(x, y, w, h)] * op)[:, :, None]
            img[Y:Y + h, X:X + w] = img[Y:Y + h, X:X + w] * (1 - m) + bl * m
    return img


dec = subprocess.Popen(['ffmpeg', '-v', 'error', '-t', f'{DUR:.3f}', '-i', V, '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'],
                       stdout=subprocess.PIPE, bufsize=10 ** 8)
enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS),
                        '-i', '-', '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', OUT + '.tmp.mp4'],
                       stdin=subprocess.PIPE)
for n in range(N):
    raw = dec.stdout.read(W * H * 3)
    if len(raw) < W * H * 3: break
    t = n / FPS
    img = crop_zoom(np.frombuffer(raw, np.uint8).reshape(H, W, 3), zoom_at(t)).astype(np.float32)
    img = put_card(img, t)
    img = glass(img, t)
    o = cv2.imread(f'{FR}/{n:04d}.png', cv2.IMREAD_UNCHANGED)
    if o.shape[2] == 3:
        img = o.astype(np.float32)
    else:
        a = o[:, :, 3:4].astype(np.float32) / 255
        if a.max() > 0:
            img = o[:, :, :3].astype(np.float32) * a + img * (1 - a)
    enc.stdin.write(np.clip(img, 0, 255).astype(np.uint8).tobytes())
    if n % 100 == 0: print(n, flush=True)
enc.stdin.close(); enc.wait(); dec.terminate()
os.replace(OUT + '.tmp.mp4', OUT)
print('ok', N)
