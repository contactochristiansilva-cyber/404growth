"""404 Growth · efectos de sonido propios para el VSL (sintetizados: sin licencias).
uso: python3 make_sfx.py <carpeta de salida>
Escribe WAV 48 kHz estéreo 24 bits (pico -3 dBFS) y `muestrario.mp3` con todos seguidos.
Pensados «brutales pero suaves»: transitorio corto, cola limpia, nada de agudos chillones (todo pasa por un pasa-bajos suave).
"""
import os, sys
import numpy as np
import soundfile as sf
from scipy import signal

SR = 48000
rng = np.random.default_rng(404)
OUT = sys.argv[1] if len(sys.argv) > 1 else 'sfx'
os.makedirs(OUT, exist_ok=True)


def t(d):
    return np.arange(int(round(SR * d))) / SR


def ts(m):
    return np.arange(m) / SR


def env_adsr(n, a, d, s, r, sus=0.6):
    a, d, r = int(a * SR), int(d * SR), int(r * SR)
    s = max(0, n - a - d - r)
    e = np.concatenate([np.linspace(0, 1, a, endpoint=False) ** 2,
                        np.linspace(1, sus, d, endpoint=False),
                        np.full(s, sus),
                        sus * np.linspace(1, 0, r) ** 2])
    return np.pad(e, (0, max(0, n - len(e))))[:n]


def bell(n, peak=0.5, sharp=2.0):
    x = np.linspace(0, 1, n)
    return np.exp(-((x - peak) ** 2) / (2 * (0.18 / sharp) ** 2))


def sweep_filter(x, f0, f1, q=1.2, steps=64, shape='lin'):
    """band-pass that moves from f0 to f1 (block by block, overlap-add)"""
    n = len(x); out = np.zeros(n); hop = n // steps or 1; win = np.hanning(hop * 2)
    for k in range(steps):
        i = k * hop
        seg = x[i:i + hop * 2]
        if len(seg) < 8: break
        u = k / (steps - 1)
        f = f0 * (f1 / f0) ** u if shape == 'log' else f0 + (f1 - f0) * u
        f = min(max(f, 40), SR / 2 - 500)
        b, a = signal.butter(2, [f / (1 + 1 / (2 * q)), f * (1 + 1 / (2 * q))], btype='band', fs=SR)
        y = signal.lfilter(b, a, seg) * win[:len(seg)]
        out[i:i + len(y)] += y
    return out


def lp(x, f, o=2):
    b, a = signal.butter(o, f, btype='low', fs=SR); return signal.lfilter(b, a, x)


def hp(x, f, o=2):
    b, a = signal.butter(o, f, btype='high', fs=SR); return signal.lfilter(b, a, x)


def reverb(x, secs=1.2, mix=0.25, damp=5000):
    n = int(SR * secs); ir = rng.standard_normal(n) * np.exp(-np.linspace(0, 7, n)); ir = lp(ir, damp)
    ir /= np.abs(ir).sum() ** 0.5 * 6
    if x.ndim == 2:   # stereo: each side with its own tail, so it stays wide
        return np.stack([reverb(x[:, c], secs, mix, damp) for c in range(2)], 1)
    wet = signal.fftconvolve(x, ir)
    dry = np.pad(x, (0, len(wet) - len(x)))
    return dry * (1 - mix) + wet * mix


def stereo(x, pan=0.0, width=0.0, mov=None):
    """pan -1..1; width adds a tiny decorrelated delay; mov = (from, to) pan sweep"""
    n = len(x)
    p = np.linspace(mov[0], mov[1], n) if mov else np.full(n, pan)
    l = x * np.cos((p + 1) * np.pi / 4); r = x * np.sin((p + 1) * np.pi / 4)
    if width:
        d = int(width * SR); r = np.concatenate([np.zeros(d), r])[:n]
    return np.stack([l, r], 1)


def norm(y, peak_db=-3.0, fade=0.004):
    y = np.asarray(y, float)
    if y.ndim == 1: y = np.stack([y, y], 1)
    f = int(fade * SR)
    if f: y[-f:] *= np.linspace(1, 0, f)[:, None]
    m = np.abs(y).max() or 1
    return y / m * 10 ** (peak_db / 20)


def save(name, y, peak=-3.0):
    y = norm(y, peak)
    sf.write(os.path.join(OUT, name + '.wav'), y, SR, subtype='PCM_24')
    return name, len(y) / SR


noise = lambda d: rng.standard_normal(int(round(SR * d)))
made = []

# 01 · whoosh suave (paso de una idea a otra)
d = 0.75; x = sweep_filter(noise(d), 250, 2600, q=0.9, shape='log') * bell(int(SR * d), 0.62, 1.4)
x = lp(x, 6000); made.append(save('01-whoosh-suave', reverb(stereo(x, mov=(-0.7, 0.7), width=0.004), 0.6, 0.18)))
# 02 · whoosh rápido (entrada de palabra grande)
d = 0.38; x = sweep_filter(noise(d), 500, 4200, q=1.1, shape='log') * bell(int(SR * d), 0.7, 2.2)
made.append(save('02-whoosh-rapido', stereo(lp(x, 7000), mov=(-0.5, 0.5), width=0.003)))
# 03 · swoosh de salida (la palabra se va)
d = 0.5; x = sweep_filter(noise(d), 3500, 300, q=1.0, shape='log') * bell(int(SR * d), 0.3, 1.6)
made.append(save('03-swoosh-salida', stereo(lp(x, 6500), mov=(0.4, -0.6), width=0.003)))
# 04 · pop de palabra (la palabra clave aparece)
d = 0.16; tt = t(d); f = 520 * np.exp(-tt * 30) + 160
x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 28)
x += 0.25 * hp(noise(d), 2000) * np.exp(-tt * 160)
made.append(save('04-pop-palabra', reverb(lp(x, 5000), 0.4, 0.12)))
# 05 · burbuja (icono o emoji que entra)
d = 0.22; tt = t(d); f = 300 + 900 * (1 - np.exp(-tt * 25))
x = np.sin(2 * np.pi * np.cumsum(f) / SR) * env_adsr(len(tt), 0.004, 0.05, 0, 0.12, 0.3)
made.append(save('05-burbuja', reverb(lp(x, 4000), 0.5, 0.15)))
# 06 · clic de interfaz (cursor, botón, marcar)
d = 0.07; tt = t(d)
x = signal.lfilter(*signal.butter(2, [1800, 4200], btype='band', fs=SR), noise(d)) * np.exp(-tt * 250)
x += 0.5 * np.sin(2 * np.pi * 2300 * tt) * np.exp(-tt * 90)
made.append(save('06-clic', lp(x, 7000), -6))
# 07 · contador (cifra que sube: 3 % → 30 %), 1,4 s acelerando
d = 1.4; n = int(SR * d); x = np.zeros(n); pos = 0.0; gap = 0.11
while pos < d - 0.05:
    i = int(pos * SR); m = min(int(0.03 * SR), n - i); tt = ts(m)
    pitch = 1600 + 1400 * pos / d
    x[i:i + m] += (np.sin(2 * np.pi * pitch * tt) * np.exp(-tt * 180))[:m] if len(tt) == m else 0
    pos += gap; gap = max(0.035, gap * 0.9)
x[-int(0.25 * SR):] += 0.0
end = np.sin(2 * np.pi * 1320 * t(0.35)) * np.exp(-t(0.35) * 9) * 0.8 + np.sin(2 * np.pi * 1980 * t(0.35)) * np.exp(-t(0.35) * 12) * 0.4
x = np.concatenate([x, end]); made.append(save('07-contador', reverb(lp(x, 8000), 0.8, 0.2), -5))
# 08 · golpe sub (cambio de escena importante; se siente más que se oye)
d = 1.6; tt = t(d); f = 85 * np.exp(-tt * 6) + 38
x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 2.6)
x += 0.35 * lp(noise(d), 900) * np.exp(-tt * 25)
x = np.tanh(x * 1.6)
made.append(save('08-golpe-sub', x, -2))
# 09 · subida (riser corto antes de un dato o del cierre)
d = 1.8; tt = t(d); u = tt / d
nz = sweep_filter(noise(d), 400, 5200, q=1.6, shape='log') * u ** 2.2
tone = sum(np.sin(2 * np.pi * np.cumsum(fr * (1 + u ** 2)) / SR) for fr in (220, 330, 440)) / 3 * u ** 3 * 0.6
x = lp(nz + tone, 7500); x[-int(0.02 * SR):] *= np.linspace(1, 0, int(0.02 * SR))
made.append(save('09-subida', stereo(x, width=0.006)))
# 10 · brillo (dato bueno, check, «hecho»)
d = 1.4; tt = t(d); x = np.zeros(len(tt))
for k in range(14):
    st = rng.uniform(0, 0.35); fr = rng.choice([1568, 1760, 2093, 2349, 2637, 3136])
    m = tt >= st; x[m] += np.sin(2 * np.pi * fr * (tt[m] - st)) * np.exp(-(tt[m] - st) * rng.uniform(4, 9)) * rng.uniform(0.3, 1)
made.append(save('10-brillo', reverb(lp(x, 9000), 1.4, 0.35)))
# 11 · glitch (transición con barras / rayas)
d = 0.42; n = int(SR * d); x = np.zeros(n); i = 0
while i < n:
    m = int(rng.uniform(0.01, 0.045) * SR); seg = rng.standard_normal(m) if rng.random() < 0.5 else np.sign(np.sin(2 * np.pi * rng.uniform(150, 900) * ts(m)))
    seg = (seg * rng.uniform(0.3, 1))[:max(0, n - i)]; x[i:i + len(seg)] = seg; i += m + int(rng.uniform(0, 0.02) * SR)
x = np.round(x * 6) / 6
made.append(save('11-glitch', stereo(lp(x, 6000), width=0.002), -6))
# 12 · tecleo (palabras que se escriben)
d = 0.9; n = int(SR * d); x = np.zeros(n)
for st in np.cumsum(rng.uniform(0.05, 0.11, 12)):
    i = int(st * SR)
    if i >= n - 400: break
    m = int(0.025 * SR); tt = ts(m)
    k = signal.lfilter(*signal.butter(2, [1500, 5000], btype='band', fs=SR), rng.standard_normal(m)) * np.exp(-tt * 300)
    x[i:i + m] += k[:n - i] * rng.uniform(0.5, 1)
made.append(save('12-tecleo', x, -8))
# 13 · destello (fundido a blanco entre escenas)
d = 1.0; tt = t(d)
pad = sum(np.sin(2 * np.pi * fr * tt) for fr in (261.6, 392.0, 523.3, 659.3)) / 4
x = (pad * 0.6 + 0.4 * sweep_filter(noise(d), 600, 3000, q=0.8)) * bell(len(tt), 0.45, 1.2)
made.append(save('13-destello', reverb(lp(x, 6000), 1.6, 0.4)))
# 14 · rotura en partículas (la tarjeta se rompe al final)
d = 1.6; n = int(SR * d); x = np.zeros(n)
for k in range(260):
    st = rng.exponential(0.25); i = int(st * SR)
    if i >= n - 600: continue
    m = int(rng.uniform(0.004, 0.02) * SR); tt = ts(m); fr = rng.uniform(2500, 7000)
    x[i:i + m] += np.sin(2 * np.pi * fr * tt) * np.exp(-tt * 400) * rng.uniform(0.2, 1) * np.exp(-st * 2)
x += 0.8 * lp(noise(d), 300) * np.exp(-t(d) * 14)
made.append(save('14-particulas', reverb(stereo(lp(x, 9000), width=0.008), 1.0, 0.3)))
# 15 · tarjeta que se desliza (gráfico o tarjeta que entra)
d = 0.55; tt = t(d)
x = sweep_filter(noise(d), 180, 1100, q=0.8, shape='log') * bell(len(tt), 0.45, 1.3)
th = np.sin(2 * np.pi * 70 * tt) * np.exp(-np.maximum(tt - 0.4, 0) * 30) * (tt > 0.4)
made.append(save('15-tarjeta', lp(x + 0.8 * th, 5000)))
# 16 · impacto suave (titular grande que cae)
d = 1.3; tt = t(d)
x = np.sin(2 * np.pi * np.cumsum(60 * np.exp(-tt * 4) + 45) / SR) * np.exp(-tt * 5)
x += 0.6 * lp(noise(d), 2500) * np.exp(-tt * 18)
made.append(save('16-impacto-suave', reverb(np.tanh(x * 1.3), 1.4, 0.3)))

# muestrario: todos seguidos con 0,6 s de silencio
gap = np.zeros((int(0.6 * SR), 2)); parts = []
for name, _ in made:
    y, _sr = sf.read(os.path.join(OUT, name + '.wav')); parts += [y, gap]
sf.write(os.path.join(OUT, '_muestrario.wav'), np.concatenate(parts), SR, subtype='PCM_16')
for name, dur in made:
    print(f'{name}  {dur:.2f} s')
