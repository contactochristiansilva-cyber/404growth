import json, sys
J = json.load(open('flow/jobs34.json'))
def msg(items):
    refs = []
    for j in items:
        for r in j['refs']:
            if r not in refs: refs.append(r)
    if len(items) == 1:
        j = items[0]
        t = f'Genera 1 imagen con Nano Banana 2.1 en formato {j["fmt"]} usando ' + ('la referencia adjunta: ' if len(j['refs']) == 1 else 'las referencias adjuntas: ') + j['text']
    else:
        t = f'Genera {len(items)} imágenes separadas con Nano Banana 2.1, cada una en su formato y con su referencia adjunta. ' + ' '.join(
            f'IMAGEN {k} «{j["id"]}» (formato {j["fmt"]}, referencia {", ".join(j["refs"])}): {j["text"]}' for k, j in enumerate(items, 1))
    return refs, t
if __name__ == '__main__':
    s = sys.argv[1]; ids = sys.argv[2].split(',')
    items = [j for i in ids for j in J if j['slug'] == s and j['id'] == i]
    refs, t = msg(items)
    print(json.dumps(dict(refs=refs, text=t), ensure_ascii=False))
