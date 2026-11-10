"""Lote 33 · arreglos de fluidez de las propuestas ya generadas (10/11/2026). uso: python3 perf34.py <carpeta con p-*.html>
- la tienda tenía scroll-behavior:smooth: cada scrollTo del recorrido empezaba una animación y se cortaba (en el móvil casi no bajaba).
- la aurora del inicio (.sk-aur, blur 70px) se movía sin parar: con ese desenfoque, el navegador la repintaba en cada fotograma.
- los marcos de la tienda se cargaban con 900 px de margen: ahora 400 px, para no cargar la tienda entera mientras corre el recorrido."""
import glob, os, sys
R_SHOP = [("var emb=/[?&](embed|tour)=1/.test(location.search);if(emb)d.documentElement.classList.add('emb');",
           "var emb=/[?&](embed|tour)=1/.test(location.search);if(emb){d.documentElement.classList.add('emb');d.documentElement.style.scrollBehavior='auto'}")]
R_PROP = [("animation:skaur 20s ease-in-out infinite alternate", "animation:none"),
          ("{rootMargin:'900px 0px'}", "{rootMargin:'400px 0px'}")]
def fix(path, reps):
    s = open(path, encoding='utf-8').read(); n = 0
    for a, b in reps:
        if a in s: s = s.replace(a, b); n += 1
        elif b not in s: raise SystemExit(f'{path}: no encuentro «{a[:40]}…»')
    open(path, 'w', encoding='utf-8').write(s); return n
if __name__ == '__main__':
    d = sys.argv[1]; t = 0
    for f in sorted(glob.glob(os.path.join(d, 'p-*--tienda.html'))):
        slug = os.path.basename(f)[2:-len('--tienda.html')]
        t += fix(f, R_SHOP) + fix(os.path.join(d, f'p-{slug}.html'), R_PROP)
    print('cambios', t)
