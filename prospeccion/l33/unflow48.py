# Lote 48: pasa las fotos de Flow (.json de la pestaña receptora: {"<slug>__<id>": {"d": dataURL, "w", "h", "i"}}) a <carpeta>/<slug>/<id>.jpg
# uso: python3 unflow48.py <carpeta destino> f48_01.json [f48_02.json …]   (h.jpg = copia de hd.jpg)
import base64, json, os, shutil, sys
dst = sys.argv[1]
n = 0
for f in sys.argv[2:]:
    for k, v in json.load(open(f)).items():
        s, i = k.split('__')
        os.makedirs(os.path.join(dst, s), exist_ok=True)
        p = os.path.join(dst, s, i + '.jpg')
        open(p, 'wb').write(base64.b64decode(v['d'].split(',', 1)[1])); n += 1
        if i == 'hd':
            shutil.copyfile(p, os.path.join(dst, s, 'h.jpg'))
print(n, 'fotos')
for s in sorted(os.listdir(dst)):
    have = sorted(x[:-4] for x in os.listdir(os.path.join(dst, s)) if x.endswith('.jpg'))
    print(s, len(have), ' '.join(have))
