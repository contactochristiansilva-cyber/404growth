#!/usr/bin/env python3
"""Textos de las ofertas para LinkedIn Empleos, sacados de roles.json (los mismos 5 puntos que la página).

    python3 li.py <carpeta de salida>

Escribe li-<puesto>.txt (uno por puesto, sin la candidatura abierta) y li.json con todos.
Cada texto empieza y termina con el enlace a su página con utm_medium=empleo, para que en
admin › Talento se vea qué candidaturas llegan desde LinkedIn.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
R = json.load(open(os.path.join(HERE, 'roles.json'), encoding='utf-8'))
SITE = 'https://404growth.com'
WHERE = 'En remoto, desde España o Latinoamérica.'


def text(j):
    url = '%s/equipo/%s/?utm_source=linkedin&utm_medium=empleo&utm_campaign=%s' % (SITE, j['slug'], j['slug'])
    b = lambda xs: '\n'.join('• ' + x for x in xs)
    t = [R['about'][0] + '\n' + WHERE,
         '→ Candidatura en 15 minutos, con un vídeo selfie de 30 a 60 segundos: ' + url + '\n' + R['promise'].replace('Te contestamos en menos de 24 horas. En 7 a 12 días sabes si entras al equipo.',
                                                                           'Te contestamos en menos de 24 horas y en 7 a 12 días sabes si entras.'),
         '1. EL ROL Y QUIÉNES SOMOS\n' + '\n'.join(j['role'] + R['about'][1:]),
         '2. RESPONSABILIDADES\n' + b(j['resp']),
         '3. REQUISITOS\n' + b(j['req']) + ('\nSe valora:\n' + b(j['plus']) if j.get('plus') else ''),
         '4. RESULTADOS\n' + '\n'.join('• %s: %s' % (a, c) for a, c in j['results']),
         '5. BENEFICIOS\n' + b(j['ben']),
         'PROCESO\n' + '\n'.join('%d. %s. %s' % (i + 1, a, c) for i, (a, c) in enumerate(R['process'])),
         '→ Envía tu candidatura aquí: ' + url]
    return '\n\n'.join(t)


if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '.'
    os.makedirs(out, exist_ok=True)
    allj = {}
    for j in R['jobs']:
        if not j.get('test'):  # la candidatura abierta no va como oferta
            continue
        allj[j['slug']] = text(j)
        open(os.path.join(out, 'li-%s.txt' % j['slug']), 'w', encoding='utf-8').write(allj[j['slug']] + '\n')
    json.dump(allj, open(os.path.join(out, 'li.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    for k, v in allj.items():
        print(k, len(v), 'caracteres')
