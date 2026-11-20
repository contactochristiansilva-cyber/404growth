"""VSL v3 (20/11/2026): monta un tramo de fotogramas [a, b) del vídeo con la capa de textos y gráficos.

uso: python3 compose3.py <vídeo> <spec.json> <frames> <masks> <a> <b> <salida.mp4>
  frames/front/NNNNN.png  capa de delante (textos, gráficos, pantallas compartidas; agujero transparente)
  frames/behind/NNNNN.png capa de detrás (lo que flota detrás de Christian)
  masks/NNNNN.png         silueta de Christian (960x540) en los tramos que flotan
Cortes de zoom: un plano por frase, alternando 1,00 y 1,12 (centro en la cara).
"""
import json, os, subprocess, sys
import numpy as np, cv2

V, SPEC, FR, MK, A, B, OUT = sys.argv[1:8]
A, B = int(A), int(B)
S = json.load(open(SPEC))
FPS, W, H = 25, 1920, 1080
CX, CY = 960, 420          # centro del zoom (cara)
ZOOM = 1.12
HOLE = (60, 60, 860, 960)  # x, y, ancho, alto del vídeo en las pantallas compartidas

cuts = S['cuts']


def zoom_at(t):
    k = 0
    for i, c in enumerate(cuts):
        if t >= c:
            k = i
    return 1.0 if k % 2 == 0 else ZOOM


def in_any(lst, t):
    for s in lst:
        if s['t0'] <= t < s['t1']:
            return s
    return None


def zoomed(img, z):
    if z == 1.0:
        return img
    w, h = W / z, H / z
    x0 = min(max(CX - w * (CX / W) * 1.0, 0), W - w)
    y0 = min(max(CY - h * (CY / H), 0), H - h)
    M = np.float32([[z, 0, -x0 * z], [0, z, -y0 * z]])
    return cv2.warpAffine(img, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)


def over(dst, png):
    """Pone una capa RGBA (BGRA de OpenCV) encima de dst (BGR, float32)."""
    if png.ndim == 2 or png.shape[2] == 3:      # captura sin transparencia: tapa todo
        dst[:] = (png if png.ndim == 3 else cv2.cvtColor(png, cv2.COLOR_GRAY2BGR)).astype(np.float32)
        return dst
    a = png[:, :, 3:4].astype(np.float32) / 255.0
    dst *= (1.0 - a)
    dst += png[:, :, :3].astype(np.float32) * a
    return dst


def load(p):
    return cv2.imread(p, cv2.IMREAD_UNCHANGED) if os.path.exists(p) else None


# vídeo de entrada (solo el tramo)
dec = subprocess.Popen(['ffmpeg', '-v', 'error', '-ss', f'{A / FPS:.4f}', '-i', V, '-frames:v', str(B - A),
                        '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], stdout=subprocess.PIPE, bufsize=10**8)
tmp = OUT[:-4] + '.part.mp4'
enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS),
                        '-i', '-', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p',
                        '-g', '50', '-movflags', '+faststart', tmp], stdin=subprocess.PIPE)
bg = np.full((H, W, 3), 242, np.float32)
n = A
while n < B:
    raw = dec.stdout.read(W * H * 3)
    if len(raw) < W * H * 3:
        break
    fr = np.frombuffer(raw, np.uint8).reshape(H, W, 3)
    t = n / FPS
    sp = in_any(S['split'], t)
    if sp:
        x, y, w, h = HOLE
        s = h / H
        sm = cv2.resize(fr, (int(W * s), h), interpolation=cv2.INTER_AREA)
        cx = (sm.shape[1] - w) // 2
        img = bg.copy()
        img[y:y + h, x:x + w] = sm[:, cx:cx + w]
    else:
        z = zoom_at(t)
        img = zoomed(fr, z).astype(np.float32)
        beh = load(f'{FR}/behind/{n:05d}.png')
        if beh is not None:
            orig = img.copy()
            over(img, beh)
            m = load(f'{MK}/{n:05d}.png')
            if m is not None:
                if m.ndim == 3:
                    m = m[:, :, 0]
                m = cv2.resize(m, (W, H), interpolation=cv2.INTER_LINEAR)
                m = zoomed(m, z).astype(np.float32) / 255.0
                m = cv2.GaussianBlur(m, (0, 0), 1.2)[:, :, None]
                img = img * (1 - m) + orig * m
    fro = load(f'{FR}/front/{n:05d}.png')
    if fro is not None:
        over(img, fro)
    enc.stdin.write(np.clip(img, 0, 255).astype(np.uint8).tobytes())
    n += 1
enc.stdin.close(); enc.wait(); dec.stdout.close(); dec.wait()
if enc.returncode == 0 and n == B:
    os.replace(tmp, OUT)
    print('ok', A, B)
else:
    print('FALLO', A, B, n, enc.returncode)
