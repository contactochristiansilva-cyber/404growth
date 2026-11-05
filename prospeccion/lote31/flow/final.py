# final.py <slug>: mensajes para Nano Banana 2.1 (sin «Category photo 'X':», que hace que escriba la palabra) y claves por foto
import json, re, sys
s = sys.argv[1]
d = json.load(open(f'{s}.json'))
msgs, K, SEG = [], {}, {}
for m in d['msgs']:
    t = m['text'].replace('Nano Banana Pro', 'Nano Banana 2.1')
    t = re.sub(r"Category photo '[^']+': (\w)", lambda g: g.group(1).upper(), t)
    t = t.replace('no frames, no collage.', 'no frames, no collage, no words or labels anywhere in the image.', 1)
    for mm in re.finditer(r'IMAGEN \d+ «(\w+)» \([^)]*\): (.*?)(?= IMAGEN \d+ «|$)', t):
        ok = json.load(open(f'{s}.keys.json')).get(mm.group(1), '')
        K[mm.group(1)] = ok if ok and ok in mm.group(2) else mm.group(2)[:70]
    msgs.append(dict(refs=m['refs'], text=t))
    SEG.update({mm.group(1): mm.group(2) for mm in re.finditer(r'IMAGEN \d+ «(\w+)» \([^)]*\): (.*?)(?= IMAGEN \d+ «|$)', t)})
for i in K:
    if list(K.values()).count(K[i]) > 1:
        seg = SEG[i]
        for o in range(0, len(seg) - 50, 5):
            c = seg[o:o + 60]
            if sum(c in v for v in SEG.values()) == 1: K[i] = c; break
vals = list(K.values()); assert len(set(vals)) == len(vals), 'claves repetidas'
json.dump(dict(msgs=msgs, K=K), open(f'{s}.final.json', 'w'), ensure_ascii=False)
print(len(K), 'claves')
