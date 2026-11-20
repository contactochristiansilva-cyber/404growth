"""VSL v4 (20/11/2026): monta un tramo de fotogramas [a, b) del vídeo.

uso: python3 compose4.py <vídeo> <spec4.json> <frames> <masks> <clips> <a> <b> <salida.mp4>
  frames/front/NNNNN.png   subtítulos, recorrido del calendario y cifra (con transparencia)
  frames/behind/NNNNN.png  lo que flota detrás de Christian
  masks/NNNNN.png          silueta de Christian (960x540) en los tramos que flotan
  clips/<id>.mp4           escenas de monigotes (se ajustan a la duración de cada escena)
Lo que hace con el vídeo de Christian: un corte de zoom por frase (1,00 / 1,12), blanco y negro cuando
cita las objeciones, y en el calendario lo mete en una tarjeta a la izquierda. Cuando hay escena de
monigotes, va la escena a pantalla completa. Después de la voz (cierre), fondo claro.
"""
import json, math, os, subprocess, sys
import numpy as np, cv2

V, SPEC, FR, MK, CL, A, B, OUT = sys.argv[1:9]
A, B = int(A), int(B)
S = json.load(open(SPEC))
FPS, W, H = 25, 1920, 1080
CX, CY = 960, 420          # centro del zoom (cara)
ZOOM = 1.12
HOLE = (60, 60, 860, 960)  # x, y, ancho, alto de la tarjeta de Christian en el calendario
NV = int(S['voice'] * FPS + 1e-6)   # fotogramas del vídeo original
# trozo de cada clip que se usa (segundos); el resto se descarta
USE = {'c11': 5.6, 'c9': 9.9}
cuts = S['cuts']


def fi(t):                      # primer fotograma con n/FPS >= t
    return int(math.ceil(t * FPS - 1e-6))


for c in S['cut']:
    c['n0'], c['n1'] = fi(c['t0']), fi(c['t1'])


def zoom_at(t):
    if t < S.get('intro_end', 0):
        I = S['intro']
        k = max(i for i, s in enumerate(I) if t >= s[0])
        t0, a, b, snap = I[k]
        t1 = I[k + 1][0] if k + 1 < len(I) else S['intro_end']
        z = a + (b - a) * (t - t0) / max(t1 - t0, 0.01)
        if snap and k and t - t0 < 0.2:          # acercamiento rápido desde el zoom del plano anterior
            u = 1 - (1 - (t - t0) / 0.2) ** 3
            z = I[k - 1][2] + (z - I[k - 1][2]) * u
        bl = S.get('blur', 0)
        if t < bl:                                # el vídeo empieza desenfocado y un poco más cerca
            z *= 1 + 0.14 * (1 - t / bl) ** 2
        return z
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
    if png.ndim == 2 or png.shape[2] == 3:
        dst[:] = (png if png.ndim == 3 else cv2.cvtColor(png, cv2.COLOR_GRAY2BGR)).astype(np.float32)
        return dst
    a = png[:, :, 3:4].astype(np.float32) / 255.0
    dst *= (1.0 - a)
    dst += png[:, :, :3].astype(np.float32) * a
    return dst


def load(p):
    return cv2.imread(p, cv2.IMREAD_UNCHANGED) if os.path.exists(p) else None


class Clip:
    """Escena de monigotes ajustada a N fotogramas (velocidad entre 0,8 y 1,12; si sobra, se corta el final)."""

    def __init__(self, c, skip):
        p = f"{CL}/{c['id']}.mp4"
        d = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p],
                                 capture_output=True, text=True).stdout.strip())
        u = min(USE.get(c['id'], d), d) - 0.05
        n = c['n1'] - c['n0']
        L = n / FPS
        f = min(max(u / L, 0.8), 1.12)
        vf = (f"trim=0:{min(u, f * L):.3f},setpts=(PTS-STARTPTS)/{f:.4f},fps={FPS},scale={W}:{H}:flags=lanczos,"
              f"unsharp=5:5:0.4,tpad=stop_mode=clone:stop_duration=4")
        self.p = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', p, '-vf', vf, '-frames:v', str(n), '-f', 'rawvideo',
                                   '-pix_fmt', 'bgr24', '-'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, bufsize=10**8)
        self.id = c['id']
        self.last = None
        for _ in range(skip):
            self.read()

    def read(self):
        raw = self.p.stdout.read(W * H * 3)
        if len(raw) == W * H * 3:
            self.last = np.frombuffer(raw, np.uint8).reshape(H, W, 3)
        return self.last

    def close(self):
        self.p.terminate(); self.p.stdout.close(); self.p.wait()


dec = None
if A < NV:
    dec = subprocess.Popen(['ffmpeg', '-v', 'error', '-ss', f'{A / FPS:.4f}', '-i', V, '-frames:v', str(min(B, NV) - A),
                            '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], stdout=subprocess.PIPE, bufsize=10**8)
tmp = OUT[:-4] + '.part.mp4'
enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS),
                        '-i', '-', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p',
                        '-g', '50', '-movflags', '+faststart', tmp], stdin=subprocess.PIPE)
bg = np.full((H, W, 3), 242, np.float32)
clip = None
n = A
while n < B:
    fr = None
    if n < NV:
        raw = dec.stdout.read(W * H * 3)
        if len(raw) == W * H * 3:
            fr = np.frombuffer(raw, np.uint8).reshape(H, W, 3)
    t = n / FPS
    cut = next((c for c in S['cut'] if c['n0'] <= n < c['n1']), None)
    cal = in_any(S['cal'], t)
    if cut:
        if clip is None or clip.id != cut['id']:
            if clip: clip.close()
            clip = Clip(cut, n - cut['n0'])
        img = clip.read().astype(np.float32)
        if in_any(S.get('side', []), t):          # con las cuentas al lado, la escena va más pequeña y a la izquierda
            k, sx, sy = S['side_box']
            img = cv2.warpAffine(img, np.float32([[k, 0, sx], [0, k, sy]]), (W, H), flags=cv2.INTER_AREA,
                                 borderMode=cv2.BORDER_REPLICATE)
    elif fr is None:
        img = bg.copy()
    elif cal:
        x, y, w, h = HOLE
        s = h / H
        sm = cv2.resize(fr, (int(W * s), h), interpolation=cv2.INTER_AREA)
        cx = (sm.shape[1] - w) // 2
        img = bg.copy()
        img[y:y + h, x:x + w] = sm[:, cx:cx + w]
    else:
        z = zoom_at(t)
        src = fr
        if any(a <= t < b for a, b in S['bw']):
            g = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
            src = cv2.cvtColor(g, cv2.COLOR_GRAY2BGR)
        img = src.astype(np.float32)
        beh = load(f'{FR}/behind/{n:05d}.png') if in_any(S['float'], t) else None
        if beh is not None:
            orig = img.copy()
            over(img, beh)
            m = load(f'{MK}/{n:05d}.png')
            if m is not None:
                if m.ndim == 3:
                    m = m[:, :, 0]
                m = cv2.resize(m, (W, H), interpolation=cv2.INTER_LINEAR).astype(np.float32) / 255.0
                m = cv2.GaussianBlur(m, (0, 0), 1.2)[:, :, None]
                img = img * (1 - m) + orig * m
        img = zoomed(img, z)
        if t < S.get('blur', 0):
            sg = 30.0 * (1 - t / S['blur']) ** 2
            if sg > 0.3:
                img = cv2.GaussianBlur(img, (0, 0), sg)
    fro = load(f'{FR}/front/{n:05d}.png')
    if fro is not None:
        over(img, fro)
    enc.stdin.write(np.clip(img, 0, 255).astype(np.uint8).tobytes())
    n += 1
enc.stdin.close(); enc.wait()
if dec: dec.stdout.close(); dec.wait()
if clip: clip.close()
if enc.returncode == 0 and n == B:
    os.replace(tmp, OUT)
    print('ok', A, B)
else:
    print('FALLO', A, B, n, enc.returncode)
