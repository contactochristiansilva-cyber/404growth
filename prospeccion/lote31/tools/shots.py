"""Antes (su Instagram de hoy, maquetado con sus fotos reales) y después (la portada de la tienda) a 1280×697, y capturas de revisión.
uso: python3 shots.py <slug> ...   (con gen.py ya ejecutado)"""
import html, json, os, re, shutil, subprocess, sys, time
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); L31 = os.path.dirname(HERE); OUT = os.path.join(L31, 'out')
sys.path.insert(0, HERE)
from shops import SHOPS
E = html.escape
PORT = 8931


def ig_html(slug):
    c = SHOPS[slug]; src = os.path.join(L31, 'src/l31', slug); m = json.load(open(os.path.join(src, 'meta.json')))
    ln = [x.strip() for x in m['header'].split('\n') if x.strip()]
    def num(word):
        for x in ln:
            if x.endswith(word): return x[:-len(word)].strip()
        return ''
    try:
        k = max(i for i, x in enumerate(ln) if x.endswith('seguidos'))
    except ValueError:
        k = 4
    stop = {'Seguir', 'Enviar mensaje', 'más', 'Siguiendo'}
    bio = []
    for x in ln[k + 1:]:
        if x in stop: break
        bio.append(x)
    name = ln[1] if len(ln) > 1 else c['name']
    bio = [b.replace('...', '…') for b in bio[:6]]
    thumbs = []
    for i in range(1, 7):
        f = os.path.join(src, '%02d.jpg' % i)
        if os.path.exists(f):
            t = f'_ig-{slug}-{i}.jpg'; im = Image.open(f).convert('RGB'); w, h = im.size; r = 3 / 4
            cw, ch = (w, int(w / r)) if w / h < r else (int(h * r), h)
            im.crop(((w - cw) // 2, (h - ch) // 2, (w - cw) // 2 + cw, (h - ch) // 2 + ch)).resize((300, 400)).save(os.path.join(OUT, t), quality=86)
            thumbs.append(t)
    av = f'_ig-{slug}-av.jpg'; Image.open(os.path.join(src, 'logo.jpg')).convert('RGB').resize((300, 300)).save(os.path.join(OUT, av), quality=88)
    side = ''.join(f'<div class="si"><i></i><span>{x}</span></div>' for x in ['Inicio', 'Buscar', 'Explorar', 'Reels', 'Mensajes', 'Notificaciones', 'Crear', 'Perfil'])
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
*{{box-sizing:border-box}}body{{margin:0;width:1280px;height:697px;overflow:hidden;background:#fff;font:14px/1.35 -apple-system,BlinkMacSystemFont,"SF Pro Text",Inter,Helvetica,Arial,sans-serif;color:#000}}
.sb{{position:fixed;left:0;top:0;bottom:0;width:244px;border-right:1px solid #dbdbdb;padding:34px 18px}}.lg{{font:italic 600 26px/1 "Snell Roundhand","Brush Script MT",cursive;margin:0 12px 34px}}
.si{{display:flex;align-items:center;gap:14px;padding:12px;font-size:15px}}.si i{{width:24px;height:24px;border:2px solid #111;border-radius:7px}}
.mn{{position:absolute;left:244px;right:0;top:0;padding:30px 0 0}}.w{{width:935px;margin:0 auto}}
.hd{{display:flex;gap:80px;padding:0 0 34px 60px;border-bottom:1px solid #dbdbdb}}.av{{width:150px;height:150px;border-radius:50%;background:url({av}) center/cover;flex:none;box-shadow:0 0 0 1px #dbdbdb}}
.r1{{display:flex;align-items:center;gap:10px;font-size:20px}}.b{{font-size:14px;font-weight:600;padding:7px 16px;border-radius:8px;background:#efefef}}.b.bl{{background:#0095f6;color:#fff}}
.r2{{display:flex;gap:40px;margin:20px 0;font-size:16px}}.r2 b{{font-weight:600}}.nm{{font-weight:600}}.bio{{white-space:pre-line}}
.tb{{display:flex;justify-content:center;gap:60px;font-size:12px;letter-spacing:1px;font-weight:600;color:#737373;padding:16px 0}}.tb span:first-child{{color:#000;border-top:1px solid #000;margin-top:-17px;padding-top:16px}}
.gr{{display:grid;grid-template-columns:repeat(3,1fr);gap:3px}}.gr i{{display:block;aspect-ratio:3/4;background-size:cover;background-position:center}}
</style></head><body><div class="sb"><div class="lg">Instagram</div>{side}</div><div class="mn"><div class="w">
<div class="hd"><div class="av"></div><div><div class="r1"><span>{E(c['handle'])}</span><span class="b bl">Seguir</span><span class="b">Enviar mensaje</span></div>
<div class="r2"><span><b>{E(num('publicaciones'))}</b> publicaciones</span><span><b>{E(num('seguidores'))}</b> seguidores</span><span><b>{E(num('seguidos'))}</b> seguidos</span></div>
<div class="nm">{E(name)}</div><div class="bio">{E(chr(10).join(bio))}</div></div></div>
<div class="tb"><span>PUBLICACIONES</span><span>REELS</span><span>ETIQUETADAS</span></div>
<div class="gr">{''.join(f'<i style="background-image:url({t})"></i>' for t in thumbs)}</div></div></div></body></html>'''


def main(slugs):
    srv = subprocess.Popen([sys.executable, '-m', 'http.server', str(PORT), '-d', OUT], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1.2)
    from playwright.sync_api import sync_playwright
    try:
        with sync_playwright() as p:
            b = p.chromium.launch()
            for s in slugs:
                open(os.path.join(OUT, f'_ig-{s}.html'), 'w').write(ig_html(s))
                shutil.copy(os.path.join(L31, 'shots', f'{s}-shop.html'), os.path.join(OUT, f'_shop-{s}.html'))
                pg = b.new_page(viewport={'width': 1280, 'height': 697})
                for name, out in [(f'_ig-{s}.html', f'p-{s}--antes.jpg'), (f'_shop-{s}.html', f'p-{s}--despues.jpg')]:
                    pg.goto(f'http://localhost:{PORT}/{name}'); pg.wait_for_load_state('networkidle'); time.sleep(.6)
                    pg.screenshot(path=os.path.join(OUT, out), type='jpeg', quality=86)
                pg.close()
                for f in os.listdir(OUT):
                    if f.startswith(f'_ig-{s}') or f.startswith(f'_shop-{s}'): os.remove(os.path.join(OUT, f))
                # review captures of the proposal itself
                for vw, tag in [(1440, 'd'), (390, 'm')]:
                    pg = b.new_page(viewport={'width': vw, 'height': 900}, device_scale_factor=1)
                    pg.goto(f'http://localhost:{PORT}/p-{s}.html'); pg.wait_for_load_state('networkidle')
                    pg.evaluate("document.documentElement.classList.remove('sk')"); pg.add_style_tag(content='*{transition:none!important;animation:none!important}.bw,.ph,.stage,.lap{transform:none!important;opacity:1!important;filter:none!important}')
                    h = pg.evaluate('document.documentElement.scrollHeight')
                    for y in range(0, h, 700):
                        pg.evaluate(f'scrollTo(0,{y})'); time.sleep(.08)
                    pg.evaluate('scrollTo(0,0)'); time.sleep(.5)
                    sw = pg.evaluate('document.documentElement.scrollWidth')
                    pg.screenshot(path=os.path.join(L31, 'shots', f'{s}-{tag}.jpg'), type='jpeg', quality=70, full_page=True)
                    print(s, tag, 'alto', h, 'ancho', sw, '(desborde)' if sw > vw else '')
                    pg.close()
            b.close()
    finally:
        srv.terminate()


if __name__ == '__main__':
    main(sys.argv[1:])
