# Una propuesta del lote 40 (gen40.py) en un solo .html, con las fotos y la agenda dentro, para verla sin publicar.
# Es inline37.py más la agenda (/agenda.js pasa a ir dentro de la página).
# python3 inline40.py <dir out> <agenda.js> <salida dir> <slug> [<slug> ...]
import sys, os, subprocess, re, base64
D, AG, OUTD, *slugs = sys.argv[1:]
here = os.path.dirname(os.path.abspath(__file__))
ag = open(AG, encoding='utf-8').read().replace('</script', '<\\/script')
# La agenda enseña la foto de Christian: va dentro también.
ag = ag.replace('/christian-hola.jpg', 'data:image/jpeg;base64,' + base64.b64encode(open(os.path.join(D, 'christian-hola.jpg'), 'rb').read()).decode())
assert not re.search(r'["\'(]/[a-z0-9-]+\.(jpg|png|svg|webp)', ag)
os.makedirs(OUTD, exist_ok=True)
for s in slugs:
    out = os.path.join(OUTD, f'p-{s}.html')
    subprocess.run([sys.executable, os.path.join(here, 'inline37.py'), D, s, out], check=True)
    page = open(out, encoding='utf-8').read()
    tag = '<script src="/agenda.js" defer></script>'
    assert page.count(tag) == 1, s
    page = page.replace(tag, '<script>' + ag + '</script>')
    open(out, 'w', encoding='utf-8').write(page)
