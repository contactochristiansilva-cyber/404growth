"""Correo de prospección con la propuesta v33 en imágenes (como el 30/10): corta l33/mail/<slug>.png en trozos para
404growth.com/e/<slug>/NN.jpg y escribe l33/mail/<slug>.html (cuerpo) + l33/mail/index.json (para, asunto).
uso: python3 mail33.py <slug>..."""
import html, json, os, sys
from PIL import Image
S = os.path.dirname(os.path.abspath(__file__)); L31 = os.path.join(os.path.dirname(S), 'l31')
if not os.path.isdir(L31): L31 = os.path.dirname(S)   # en el repositorio: prospeccion/lote31/envios
sys.path.insert(0, os.path.join(L31, 'tools'))
from shops import SHOPS
from niches import NICHE
E = html.escape
CUT = 1500  # px de la captura (x2) por trozo
NOUN = {'moda': 'vuestras prendas', 'joya': 'vuestras joyas', 'obrador': 'vuestros dulces', 'deco': 'vuestras piezas'}


def slices(slug):
    im = Image.open(os.path.join(S, 'mail', slug + '.png')).convert('RGB'); W, H = im.size
    out = os.path.join(S, 'e', slug); os.makedirs(out, exist_ok=True)
    for f in os.listdir(out): os.remove(os.path.join(out, f))
    n = 0; y = 0
    while y < H:
        h = min(CUT, H - y)
        if H - (y + h) < 300: h = H - y          # no dejar un trozo final diminuto
        n += 1; im.crop((0, y, W, y + h)).save(os.path.join(out, f'{n:02d}.jpg'), 'JPEG', quality=72, optimize=True, progressive=True); y += h
    return n


def body(c, n):
    s = c['slug']; nm = E(c['name']); sh = E(c['short']); noun = NOUN.get(c['niche'], 'vuestros productos')
    page = f'https://404growth.com/p/{s}/?utm_source=email&amp;utm_medium=prospeccion&amp;utm_campaign={s}'
    book = f'https://404growth.com/book?utm_source=email&amp;utm_medium=prospeccion&amp;utm_campaign={s}'
    img = lambda k, href: (f'<a href="{href}" target="_blank"><img src="https://404growth.com/e/{s}/{k:02d}.jpg" alt="Propuesta de 404 Growth para {nm} ({k} de {n})" width="600" '
                           'style="display:block;width:100%;max-width:600px;height:auto;border:0"></a>')
    return ('<div style="font-family:-apple-system,Segoe UI,Helvetica,Arial,sans-serif;font-size:16px;line-height:1.55;color:#1a1a1a;max-width:600px">'
            '<p style="margin:0 0 12px">Hola familia!! Soy Christian, founder de 404 (mi consultoría).</p>'
            f'<p style="margin:0 0 12px">He montado cómo quedaría {sh} como tienda online, con {noun} y vuestra marca, y cómo os traeríamos clientes con anuncios. '
            'Os la dejo aquí abajo, solo tenéis que bajar (en el móvil se ve todavía mejor).</p>'
            f'<p style="margin:0 0 16px"><a href="{page}" target="_blank">Ver la propuesta en la web</a></p>'
            + ''.join(img(k, book if k == n else page) for k in range(1, n + 1)) +
            '<p style="margin:22px 0 14px">Si os encaja, os la enseño en 30 minutos por videollamada, con vuestro catálogo delante:</p>'
            f'<p style="margin:0 0 18px"><a href="{book}" style="display:inline-block;background:#1a1a1a;color:#ffffff;text-decoration:none;font-weight:600;padding:13px 22px;border-radius:99px" target="_blank">Reservar la llamada</a></p>'
            '<p style="margin:0 0 14px">O respondedme a este correo y lo vemos por aquí. Y si no es para vosotros, decídmelo y no os vuelvo a escribir.</p>'
            '<p style="margin:0">Un abrazo,<br>Christian<br><span style="color:#777777">404 Growth</span></p></div>')


def main(slugs, emails):
    idx_p = os.path.join(S, 'mail', 'index.json'); idx = json.load(open(idx_p)) if os.path.exists(idx_p) else {}
    for s in slugs:
        c = SHOPS[s]; c['slug'] = s; n = slices(s)
        open(os.path.join(S, 'mail', s + '.html'), 'w').write(body(c, n))
        idx[s] = dict(to=emails.get(s, ''), subject=f'{c["name"]}: vuestra tienda online, ya montada', n=n)
        print('ok', s, n, 'trozos', emails.get(s, '(sin email)'))
    json.dump(idx, open(idx_p, 'w'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    D = {}
    for f in ['l31/l32/data.json', 'l33/data.json']:
        p = os.path.join(os.path.dirname(S), f)
        if os.path.exists(p): D.update(json.load(open(p)))
    main(sys.argv[1:], {k: v.get('email', '') for k, v in D.items()})
