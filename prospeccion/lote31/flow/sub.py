# sub.py <slug> id1,id2,... [id=ref,...]: mensaje con solo esas fotos (renumeradas), para repetir las que fallaron
import json, re, sys
s, ids = sys.argv[1], sys.argv[2].split(',')
over = dict(a.split('=') for a in sys.argv[3].split(',')) if len(sys.argv) > 3 and sys.argv[3] else {}
d = json.load(open(f'{s}.final.json'))
seg, head = {}, None
for m in d['msgs']:
    t = m['text']; k = t.find(' IMAGEN 1 «')
    head = head or t[:k]
    for mm in re.finditer(r'IMAGEN \d+ «(\w+)» \(([^)]*)\): (.*?)(?= IMAGEN \d+ «|$)', t):
        seg[mm.group(1)] = (mm.group(2), mm.group(3))
head = re.sub(r'Genera \d+ imágenes', f'Genera {len(ids)} imágenes', head)
parts, refs = [], []
for n, i in enumerate(ids, 1):
    meta, body = seg[i]
    if i in over:
        r = over[i]
        if r == 'none':
            meta = re.sub(r', referencia [^,]*(, aplica la REGLA \w)?', '', meta) + ', sin referencia'
        else:
            meta = re.sub(r'referencia [^,]*', 'referencia ' + ' y '.join(x + '.jpg' for x in r.split('+')), meta)
    for x in re.findall(r'(\d+\.jpg)', meta):
        if x not in refs: refs.append(x)
    parts.append(f'IMAGEN {n} «{i}» ({meta}): {body}')
txt = head + ' ' + ' '.join(parts)
json.dump(dict(refs=refs, text=txt), open(f'sub_{s}.json', 'w'), ensure_ascii=False)
print(refs, len(txt)); print(txt[:400])
