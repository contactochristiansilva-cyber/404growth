"""VSL v6 (20/11/2026): el sonido. La voz de Christian tal cual (ganancia 1, sin procesar) y, por debajo:
  - clic de ratón en cada toque del recorrido del calendario;
  - un «tic» de ruleta en cada palabra que se enciende en las tarjetas blancas;
  - la música que elige Christian (opcional), muy bajita: 24 LU por debajo de la voz.
Sin disparos de cámara (Christian los quitó todos el 20/11/2026) y sin música elegida por nosotros.

uso: python3 mix6.py <vídeo original> <spec4.json> <carpeta audio> <carpeta salida> [música]
escribe mezcla.m4a (voz + todo), efectos.wav y, si hay música, musica.wav (por separado, para DaVinci).
"""
import json, re, subprocess, sys
import numpy as np

V, SPEC, AUD, OUT = sys.argv[1:5]
MUSIC = sys.argv[5] if len(sys.argv) > 5 else None
S = json.load(open(SPEC))
SR = 48000
N = int(round(S['dur'] * SR))

DB_CLICK, DB_TICK = -17.0, -25.0         # pico de cada efecto, dB respecto a escala completa
VOICE_LUFS, MUSIC_UNDER = -21.9, 24.0    # la voz, medida con ebur128; la música, 24 LU por debajo


def dec(p):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-vn', '-ac', '2', '-ar', str(SR), '-f', 'f32le', '-'],
                         capture_output=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, 2).astype(np.float32)


def lufs(p):
    e = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-i', p, '-vn', '-af', 'ebur128', '-f', 'null', '-'],
                       capture_output=True, text=True).stderr
    return float(re.findall(r'I:\s+(-?[\d.]+) LUFS', e)[-1])


def fx(name, a, b, pre):
    """Recorta [a, b] s, lo deja con pico 1 y un fundido final; pre = segundos antes del golpe."""
    x = dec(f'{AUD}/{name}')[int(a * SR):int(b * SR)].copy()
    x /= np.abs(x).max() + 1e-9
    n = min(len(x), int(0.03 * SR))
    x[-n:] *= np.linspace(1, 0, n)[:, None]
    x[:48] *= np.linspace(0, 1, 48)[:, None]
    return x, pre


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


# clics del calendario (los mismos tiempos que CALSEQ de ov4.html)
TAPS = {'cal1': [2.5, 3.4, 4.3, 5.2, 6.1], 'cal2': [0.7, 1.5, 2.9, 3.7, 4.5]}
clicks = [round(c['t0'] + u, 2) for c in S['cal'] for u in TAPS[c['kind']]]
for t in clicks:
    put(CLICK, t - 0.02, DB_CLICK)
# tic de ruleta en cada palabra de las tarjetas blancas
ticks = []
for c in S['card']:
    ws = sorted([w[1] for l in c['lines'] for w in l['w']] + ([c['nums']] if c.get('nums') else []))
    for t in ws:
        if not ticks or t - ticks[-1] > 0.07:
            ticks.append(t)
for c in S.get('side', []):       # y en cada cifra de las cuentas que van a un lado
    for r in c['rows']:
        ticks += [r['t']] + ([r['t2']] if r.get('t2') else [])
    if c.get('total'):
        ticks.append(c['total']['t'])
ticks = sorted(ticks)
for t in ticks:
    put(TICK, t - 0.03, DB_TICK)

mus = np.zeros((N, 2), np.float32)
if MUSIC:
    m = dec(MUSIC)
    xf = int(2.0 * SR)                     # si la canción dura menos que el vídeo, vuelve a empezar con fundido cruzado
    out = m.copy()
    while len(out) < N + SR:
        a = np.cos(np.linspace(0, np.pi / 2, xf))[:, None]
        out[-xf:] = out[-xf:] * a + m[:xf] * np.sin(np.linspace(0, np.pi / 2, xf))[:, None]
        out = np.concatenate([out, m[xf:]])
    mus = out[:N] * 10 ** ((VOICE_LUFS - MUSIC_UNDER - lufs(MUSIC)) / 20)
    env = np.ones(N, np.float32)
    env[:int(0.4 * SR)] = np.linspace(0, 1, int(0.4 * SR))
    v, up, fo = int(S['voice'] * SR), int(0.6 * SR), int(1.4 * SR)
    env[v:v + up] = np.linspace(1, 2, up)   # en el cierre sube 6 dB y se apaga al final
    env[v + up:] = 2
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
enc(sfx, f'{OUT}/efectos.wav', ['-c:a', 'pcm_s24le'])
if MUSIC:
    enc(mus, f'{OUT}/musica.wav', ['-c:a', 'pcm_s24le'])
json.dump(dict(clics=clicks, tics=ticks, musica=MUSIC), open(f'{OUT}/eventos.json', 'w'))
print('clics', len(clicks), '| tics', len(ticks), '| música', bool(MUSIC), '| pico', round(pk, 3),
      '| pico voz', round(float(np.abs(voice).max()), 3))
