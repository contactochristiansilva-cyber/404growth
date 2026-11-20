"""VSL v3 (20/11/2026): sonido. La voz va TAL CUAL (ganancia 1, sin compresor, limitador ni normalizar).
Debajo, el piano (encadenado si hace falta) muy bajo y efectos muy suaves en cada animación.

uso: python3 mix3.py <vídeo> <música.mp3> <carpeta SFX> <spec.json> <salida.m4a>
"""
import json, re, subprocess, sys

V, MUS, SFX, SPEC, OUT = sys.argv[1:6]
S = json.load(open(SPEC))
DUR = S['dur']
MUSIC_BELOW = 26.0   # LU por debajo de la voz
SFX_BELOW = 24.0     # dB de pico por debajo del pico de la voz
FX = {'pop': '01-whoosh-suave.wav', 'whoosh': '15-tarjeta.wav', 'card': '15-tarjeta.wav', 'float': '10-brillo.wav'}


def loud(src, extra=[]):
    r = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', *extra, '-i', src, '-map', '0:a', '-af', 'ebur128=peak=sample', '-f', 'null', '-'],
                       capture_output=True, text=True).stderr
    I = float(re.findall(r'I:\s+(-?[\d.]+) LUFS', r)[-1])
    pk = float(re.findall(r'Peak:\s+(-?[\d.]+) dBFS', r)[-1])
    return I, pk


vI, vP = loud(V)
mI, mP = loud(MUS)
mus_db = (vI - MUSIC_BELOW) - mI
fx_lv = {}
for k, f in FX.items():
    _, p = loud(f'{SFX}/{f}')
    fx_lv[k] = (vP - SFX_BELOW) - p
print(f'voz {vI:.1f} LUFS pico {vP:.1f} · música {mus_db:+.1f} dB · efectos', {k: round(v, 1) for k, v in fx_lv.items()})

inputs = ['-i', V, '-i', MUS]
filt = []
# música: dos vueltas con fundido cruzado de 3 s, entrada 1,5 s y salida 2,5 s
mlen = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', MUS], capture_output=True, text=True).stdout)
filt.append(f'[1:a]atrim=0:{mlen:.3f},asetpts=PTS-STARTPTS[m1]')
inputs += ['-i', MUS]
filt.append(f'[2:a]atrim=0:{mlen:.3f},asetpts=PTS-STARTPTS[m2]')
filt.append(f'[m1][m2]acrossfade=d=3:c1=tri:c2=tri,atrim=0:{DUR:.3f},afade=t=in:d=1.5,afade=t=out:st={DUR - 2.5:.3f}:d=2.5,volume={mus_db:.2f}dB,aformat=sample_rates=48000:channel_layouts=stereo[mus]')
labels = ['[0:a]', '[mus]']
k = 3
for i, e in enumerate(S['sfx']):
    f = FX.get(e['s'])
    if not f:
        continue
    inputs += ['-i', f'{SFX}/{f}']
    ms = max(0, int(e['t'] * 1000))
    filt.append(f'[{k}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume={fx_lv[e["s"]]:.2f}dB,adelay={ms}|{ms}[f{i}]')
    labels.append(f'[f{i}]')
    k += 1
filt.append(''.join(labels) + f'amix=inputs={len(labels)}:normalize=0:duration=first,atrim=0:{DUR:.3f}[out]')
open(OUT + '.filter.txt', 'w').write(';\n'.join(filt))
subprocess.run(['ffmpeg', '-v', 'error', '-y', *inputs, '-filter_complex_script', OUT + '.filter.txt', '-map', '[out]',
                '-c:a', 'aac', '-b:a', '256k', OUT], check=True)
print('ok', OUT, loud(OUT))
