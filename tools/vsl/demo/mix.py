#!/usr/bin/env python3
"""Mezcla de la demo: voz (-16 LUFS), música con ducking y efectos colocados por su golpe.
uso: python3 mix.py <video base> <musica.mp3> <carpeta sfx> <duración s> <salida.wav>"""
import sys, subprocess, numpy as np, soundfile as sf, os, tempfile

V, MUS, SFX, DUR, OUT = sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]), sys.argv[5]
SR = 48000
tmp = tempfile.mkdtemp()


def load(cmd_in, extra=[]):
    p = os.path.join(tmp, 'x.wav')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', *cmd_in, *extra, '-ac', '2', '-ar', str(SR), p], check=True)
    a, _ = sf.read(p, dtype='float32'); return a


n = int(DUR * SR) + SR
voice = load(['-t', f'{DUR+.5}', '-i', V], ['-af', 'highpass=f=80,afftdn=nf=-25,loudnorm=I=-16:TP=-2:LRA=9'])
music = load(['-i', MUS])
pad = lambda a: np.pad(a, ((0, max(0, n - len(a))), (0, 0)))[:n]
voice, music = pad(voice), pad(music)

# ducking: envolvente de la voz (RMS 60 ms) -> la música baja ~20 dB con voz y sube 5 dB en los huecos
w = int(.06 * SR)
env = np.sqrt(np.convolve((voice ** 2).mean(1), np.ones(w) / w, 'same'))
talk = (env > 10 ** (-38 / 20)).astype(np.float32)
# suavizado asimétrico: ataque 40 ms, suelta 350 ms
g = np.zeros_like(talk); a_at, a_rel = np.exp(-1 / (.04 * SR)), np.exp(-1 / (.35 * SR)); s = 0.
for i in range(0, len(talk), 64):
    tgt = talk[i]; c = a_at if tgt > s else a_rel; s = tgt + (s - tgt) * c ** 64; g[i:i + 64] = s
mus_db = -27 + (1 - g) * 5        # nivel de la música (dBFS aprox. de su RMS) bajo la voz / en huecos
mrms = np.sqrt((music[SR * 2:SR * 30] ** 2).mean()) + 1e-9
music = music / mrms * (10 ** (mus_db / 20))[:, None] * .5
fade = int(.8 * SR); end = int(DUR * SR)
music[end - fade:end] *= np.linspace(1, 0, fade)[:, None]; music[end:] = 0
music[:int(.3 * SR)] *= np.linspace(0, 1, int(.3 * SR))[:, None]

# efectos: (segundo del golpe, archivo, dB, recorte s o None, 'peak'|'start')
PK = {'01': .507, '02': .273, '03': .136, '04': .005, '05': .009, '06': .005, '07': 1.406, '08': .01, '09': 1.727,
      '10': .188, '11': .404, '12': .837, '13': .459, '14': .015, '15': .407, '16': .007}
FX = [(1.20, '04', -12), (1.92, '15', -14), (3.68, '04', -13), (4.64, '02', -15), (5.92, '04', -14), (8.96, '04', -14),
      (9.38, '02', -13), (9.44, '08', -9), (11.0, '15', -14), (12.35, '07', -18, .6, 'start'), (14.72, '12', -22, .9, 'start'),
      (16.95, '03', -17), (20.16, '04', -13), (20.75, '01', -11), (21.02, '05', -14), (21.82, '05', -14), (22.38, '05', -14),
      (23.66, '05', -14), (25.92, '13', -13), (28.24, '04', -14), (29.62, '06', -12), (30.50, '15', -14), (31.51, '04', -13),
      (32.10, '08', -10), (32.36, '05', -15), (33.24, '05', -15), (33.60, '07', -19, .8, 'start'), (35.46, '05', -15),
      (35.52, '07', -19, 1.0, 'start'), (37.25, '01', -12), (37.60, '10', -16), (38.13, '16', -11), (40.05, '11', -15),
      (41.11, '04', -14), (41.83, '04', -15), (42.63, '08', -9), (44.15, '15', -14), (45.75, '16', -11), (46.32, '13', -12)]
names = {f[:2]: f for f in os.listdir(SFX) if f[:2].isdigit()}
fx = np.zeros((n, 2), np.float32)
for e in FX:
    t, k, db = e[:3]; cut = e[3] if len(e) > 3 else None; mode = e[4] if len(e) > 4 else 'peak'
    a, sr = sf.read(os.path.join(SFX, names[k]), dtype='float32')
    if a.ndim == 1: a = np.stack([a, a], 1)
    if cut:
        m = int(cut * SR); a = a[:m].copy(); f = min(len(a), int(.08 * SR)); a[-f:] *= np.linspace(1, 0, f)[:, None]
    st = int((t - (0 if mode == 'start' else PK[k])) * SR)
    a = a / (np.abs(a).max() + 1e-9) * 10 ** (db / 20)
    if st < 0: a = a[-st:]; st = 0
    e2 = min(n, st + len(a)); fx[st:e2] += a[:e2 - st]

mix = voice + music + fx
mix = mix[:int(DUR * SR)]
p = os.path.join(tmp, 'm.wav'); sf.write(p, mix, SR, subtype='FLOAT')
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', p, '-af', 'alimiter=limit=0.89:attack=3:release=60,afade=t=out:st=%.2f:d=0.35' % (DUR - .35),
                '-ar', str(SR), '-c:a', 'pcm_s24le', OUT], check=True)
print('ok')
