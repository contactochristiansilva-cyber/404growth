#!/usr/bin/env python3
"""Propuesta de 404 Growth para EFAP Miami (estrategia + Meta Business + gestión de la campaña), con la marca del club.

    python3 build.py web    <web117-404growth>   -> <web117>/efap-miami/index.html + escudo.png (con el contador de visitas, slug efap-miami)
    python3 build.py inline <salida.html>        -> un solo HTML con el escudo dentro y sin contador, para verlo o enviarlo
"""
import base64
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ESC = os.path.join(ROOT, 'tools', 'brief', 'efap-escudo.png')
SLUG = 'efap-miami'
PARTS = '[["reparto", 2], ["estrategia", 4], ["meta", 5], ["campana", 6], ["calendario", 7], ["inversion", 8], ["siguiente", 9]]'


def counter():
    s = open(os.path.join(ROOT, 'prospeccion', 'l33', 'tpl', 'counter.html'), encoding='utf-8').read()
    a = s.index('var slug="') + len('var slug="')
    s = s[:a] + SLUG + s[s.index('"', a):]
    a = s.index('PARTS=') + len('PARTS=')
    b = s.index(';', a)
    return s[:a] + PARTS + s[b:]


def main():
    mode, out = sys.argv[1], sys.argv[2]
    t = open(os.path.join(HERE, 'tpl.html'), encoding='utf-8').read()
    if mode == 'web':
        d = os.path.join(out, SLUG)
        os.makedirs(d, exist_ok=True)
        shutil.copyfile(ESC, os.path.join(d, 'escudo.png'))
        t = t.replace('{{ESCUDO}}', '/efap-miami/escudo.png').replace('{{COUNTER}}', counter())
        open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(t)
        print(os.path.join(d, 'index.html'))
    else:
        uri = 'data:image/png;base64,' + base64.b64encode(open(ESC, 'rb').read()).decode()
        t = t.replace('{{ESCUDO}}', uri).replace('{{COUNTER}}', '')
        open(out, 'w', encoding='utf-8').write(t)
        print(out)


if __name__ == '__main__':
    main()
