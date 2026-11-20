import json
W = json.load(open('../vsl2/words.json')); F = json.load(open('fix.json'))
for c, ws in F.items():
    c = float(c); a, b = c-3.2, c+3.2
    W = [w for w in W if w[1] < a] + [w for w in ws if a <= w[1] <= b] + [w for w in W if w[1] > b]
W.sort(key=lambda w: w[1])
# quitar duplicados en los bordes (misma palabra dos veces seguidas con menos de 0,25 s)
out = []
for w in W:
    if out and out[-1][0].lower().strip('.,') == w[0].lower().strip('.,') and w[1]-out[-1][1] < 0.3: continue
    if out and w[1] < out[-1][2]-0.02: w[1] = out[-1][2]
    out.append(w)
FIX = {'Cristian': 'Christian', '404€.': '404.', '404€': '404'}
for w in out: w[0] = FIX.get(w[0], w[0])
txt = ' '.join(w[0] for w in out)
txt2 = txt.replace('te lo haremos a ver', 'te lo haremos saber')
if txt2 != txt:
    for i in range(len(out)-1):
        if out[i][0] == 'a' and out[i+1][0].startswith('ver') and out[i-1][0] == 'haremos':
            out[i][0] = 'saber'; out[i][2] = out[i+1][2]; del out[i+1]; break
json.dump(out, open('words.json', 'w'), ensure_ascii=False)
print(len(out)); print(' '.join(w[0] for w in out))
