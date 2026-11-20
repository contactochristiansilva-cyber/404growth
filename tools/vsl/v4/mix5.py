"""VSL v5 (20/11/2026): el sonido. La voz de Christian tal cual (ganancia 1, sin procesar) y, por debajo:
  - clic de ratón en cada toque del recorrido del calendario;
  - disparo de cámara en cada cambio de plano o animación (más flojo en los cortes de zoom);
  - un «tic» de ruleta en cada palabra que se enciende en las tarjetas blancas;
  - música alegre sin voz, muy bajita (24 LU por debajo de la voz).

uso: python3 mix5.py <vídeo original> <spec4.json> <carpeta audio> <carpeta salida>
escribe mezcla.m4a (voz + todo), musica.wav y efectos.wav (por separado, para ajustar en DaVinci).
"""
import json, math, subprocess, sys
import numpy as np

V, SPEC, AUD, OUT = sys.argv[1:5]
S = json.load(open(SPEC))
SR, FPS = 48000, 25
N = int(round(S['dur'] * SR))

# niveles (dB respecto a escala completa, pico de cada efecto) y música
DB_SHOT, DB_SHOT_ZOOM, DB_CLICK, DB_TICK = -19.0, -25.0, -17.0, -25.0
VOICE_LUFS, MUSIC_LUFS, MUSIC_UNDER = -21.9, -10.6, 24.0     # medidos con ebur128
MUSIC = 'mus-270783.mp3'          # «Acoustic Upbeat - Happy Strums» (Sonican, Pixabay), sin voz
LOOP_A, LOOP_B = 49.305, 107.915  # mismo pasaje dos vueltas después (80 pulsos a 82 bpm)


def dec(p):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-vn', '-ac', '2', '-ar', str(SR), '-f', 'f32le', '-'],
                         capture_output=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, 2).astype(np.float32)


def fx(name, a, b, pre):
    """Recorta [a, b] s, lo deja con pico 1 y un fundido final; pre = segundos antes del golpe."""
    x = dec(f'{AUD}/{name}')[int(a * SR):int(b * SR)].copy()
    x /= np.abs(x).max() + 1e-9
    n = min(len(x), int(0.03 * SR))
    x[-n:] *= np.linspace(1, 0, n)[:, None]
    x[:48] *= np.linspace(0, 1, 48)[:, None]
    return x, pre


SHOT = fx('shut-199580.mp3', 0.07, 0.62, 0.025)
CLICK = fx('click-290204.mp3', 0.035, 0.26, 0.015)
TICK = fx('wheel-101152.mp3', 2.105, 2.30, 0.015)

sfx = np.zeros((N, 2), np.float32)


def put(s, t, db):
    x, pre = s
    i = int(round((t - pre) * SR))
    if i < 0:
        x, i = x[-i:], 0
    x = x[:max(0, N - i)]
    sfx[i:i + len(x)] += x * 10 ** (db / 20)


def fi(t):
    return math.ceil(t * FPS - 1e-6) / FPS


def inside(lst, t, eps=0.02):
    return any(s['t0'] - eps <= t < s['t1'] - eps for s in lst)


blocks = S['cut'] + S['card'] + S['cal']
# 1) cambios de plano: entra o sale una escena, una tarjeta o el calendario; aparece algo por detrás
big = set()
for s in blocks:
    big.add(round(fi(s['t0']) if s in S['cut'] else s['t0'], 2))
    if s['t1'] < S['dur'] - 0.1:
        big.add(round(fi(s['t1']) if s in S['cut'] else s['t1'], 2))
big.add(round(S['voice'], 2))                      # cierre: se va Christian y queda el móvil
for f in S['float']:
    big.add(round(f['t0'], 2))
big = sorted(big)
keep = []
for t in big:
    if not keep or t - keep[-1] > 0.35:
        keep.append(t)
big = keep
# 2) cortes de zoom sobre Christian (los del inicio y uno por frase), si no coinciden con lo anterior
zoom = [s[0] for s in S['intro'][1:]] + [t for t in S['cuts'] if t >= S['intro_end']]
zoom = [t for t in zoom if not inside(blocks, t) and all(abs(t - b) > 0.5 for b in big)]
for t in big:
    put(SHOT, t, DB_SHOT)
for t in zoom:
    put(SHOT, t, DB_SHOT_ZOOM)
# 3) clics del calendario (los mismos tiempos que CALSEQ de ov4.html)
TAPS = {'cal1': [2.5, 3.4, 4.3, 5.2, 6.1], 'cal2': [0.7, 1.5, 2.9, 3.7, 4.5]}
clicks = [round(c['t0'] + u, 2) for c in S['cal'] for u in TAPS[c['kind']]]
for t in clicks:
    put(CLICK, t - 0.02, DB_CLICK)
# 4) tic de ruleta en cada palabra de las tarjetas blancas
ticks = []
for c in S['card']:
    ws = sorted([w[1] for l in c['lines'] for w in l['w']] + ([c['nums']] if c.get('nums') else []))
    for t in ws:
        if not ticks or t - ticks[-1] > 0.07:
            ticks.append(t)
for t in ticks:
    put(TICK, t - 0.03, DB_TICK)

# música: una pasada y después vueltas al mismo pasaje, con fundido cruzado de 1 s
m = dec(f'{AUD}/{MUSIC}')
a, b, xf = int(LOOP_A * SR), int(LOOP_B * SR), int(1.0 * SR)
out = m[:b + xf // 2].copy()
while len(out) < N + SR:
    nxt = m[a - xf // 2:b + xf // 2].copy()
    w = np.sin(np.linspace(0, np.pi / 2, xf))[:, None]
    out[-xf:] = out[-xf:] * np.cos(np.linspace(0, np.pi / 2, xf))[:, None] + nxt[:xf] * w
    out = np.concatenate([out, nxt[xf:]])
mus = out[:N] * 10 ** ((VOICE_LUFS - MUSIC_UNDER - MUSIC_LUFS) / 20)
env = np.ones(N, np.float32)
env[:int(0.4 * SR)] = np.linspace(0, 1, int(0.4 * SR))
v = int(S['voice'] * SR)                                   # en el cierre sube 6 dB y se apaga al final
up = int(0.6 * SR)
env[v:v + up] = np.linspace(1, 2, up)
env[v + up:] = 2
fo = int(1.4 * SR)
env[-fo:] *= np.linspace(1, 0, fo)
mus *= env[:, None]

voice = dec(V)
mix = np.zeros((N, 2), np.float32)
mix[:min(N, len(voice))] = voice[:N]
mix += sfx + mus
pk = float(np.abs(mix).max())
if pk > 0.985:
    mix *= 0.985 / pk            # solo si hiciera falta: baja todo por igual, sin compresión


def enc(x, path, args):
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-'] + args + [path],
                         stdin=subprocess.PIPE)
    p.stdin.write(x.astype(np.float32).tobytes()); p.stdin.close(); p.wait()


enc(mix, f'{OUT}/mezcla.m4a', ['-c:a', 'aac', '-b:a', '320k'])
enc(mus, f'{OUT}/musica.wav', ['-c:a', 'pcm_s24le'])
enc(sfx, f'{OUT}/efectos.wav', ['-c:a', 'pcm_s24le'])
json.dump(dict(disparos=big, disparos_zoom=zoom, clics=clicks, tics=ticks), open(f'{OUT}/eventos.json', 'w'))
print('disparos', len(big), '+ zoom', len(zoom), '| clics', len(clicks), '| tics', len(ticks), '| pico', round(pk, 3),
      '| pico voz', round(float(np.abs(voice).max()), 3))
