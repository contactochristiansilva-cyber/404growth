"""Cambia el cargador 404 de la portada (v67) por el de la v68: python3 patch_loader.py <index.html> <salida>"""
import re, sys, pathlib
H = pathlib.Path(__file__).parent
src, out = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
html = (H/'loader.html').read_text().strip(); css = (H/'loader.css').read_text().strip(); js = (H/'loader.js').read_text().strip()
s, n1 = re.subn(r'<div id="l404".*?</svg></div></div>', lambda m: html, s, count=1, flags=re.S)
i = s.find('/* cargador 404 (de la v64) */'); j = s.find('</style>', i)
assert i > 0 and j > i; s = s[:i] + css + '\n' + s[j:]
s = s.replace('/* cargador: el 404 vuela al logo de la cabecera */\nhtml.l404 .nv-logo .mk{opacity:0}\nhtml.l404.l404-land .nv-logo .mk{opacity:1;transition:opacity .4s}\n', '')
i = s.find('/* cargador 404: se dibuja y vuela'); j = s.find('/* cabecera: más opaca', i)
assert i > 0 and j > i; s = s[:i] + js + '\n\n' + s[j:]
assert n1 == 1 and 'l404-land .nv-logo .mk{opacity:1;transition' not in s
open(out, 'w', encoding='utf-8').write(s); print('ok', len(s))
