# python3 patch_l40.py <worker.js> <out.js>
# 18–19/11/2026, lote 40 (propuesta nueva, gen40.py) en el worker del admin:
#  - SEED4 (seed_20261119, aún sin subir): cada fila con su slug, pageUrl y el día de su lote;
#  - LEAD_PATCH nuevo (lpatch_20261119) con lo mismo, por si el SEED4 ya hubiera entrado sin ellos;
#  - Vichy Motril queda fuera: ya vende online en vichymotril.com (tienda con carrito). Sin lotDay, prioridad 30 y AVISO.
#  - Cent-Vuit, Casual Coria, Doble Ele, Marga Piñeiro y Novojoya: al 20/11 sin propuesta (fotos pendientes, cupo de Flow).
#  - Mismo pueblo, días distintos: Coria del Río (Sígueme 19, Casual Coria 20, Modas Rocío 21) y Antequera (Ooh la la 19, Mercedes Beltrán 20).
import json, re, sys
src, out = sys.argv[1:3]
w = open(src, encoding='utf-8').read()
SLUG = {
    'oohlalaantequera': 'ooh-la-la', 'paubypilarpau': 'pau-valencia', 'marga.pineiro': 'marga-pineiro', 'turquesa_elche': 'turquesa-elche',
    'kontiki_lloretdemar': 'kontiki', 'principessass': 'principessas', 'koko.ropaycomplementos': 'kokoro', 'mjuncocomplementos': 'marta-junco',
    'doble_ele_moda': 'doble-ele', 'cachibachegetafe': 'cachibache', 'mercedesbeltrantienda': 'mercedes-beltran', 'lura_shopmataro': 'lura',
    'nairobi.shop': 'nairobi-shop', 'estrena_alcoy': 'estrena-alcoy', 'modasrocio_': 'modas-rocio', 'brava_shoop': 'brava',
    'silviaromeobcn': 'silvia-romeo', 'centvuit108': 'cent-vuit', 'benditalocurabyluzduran': 'bendita-locura', 'nopmodahuesca': 'nop-moda',
    'beabeabarcelona': 'bea-bea', 'inarkadia': 'inarkadia', 'azulkleinshop': 'azulklein', 'ndenua': 'ndenua', 'rasgosbarcelona2.0': 'rasgos',
    '_siguemeee': 'sigueme', 'laveraelrocio': 'la-vera', 'casualcoria': 'casual-coria', 'modas.mati': 'modas-mati',
    'miranda.shopcarballo': 'miranda-shop', 'zapateriacapricho_andujar': 'zapateria-capricho', 'lenceriaaguedaherrera': 'agueda-herrera',
    'joyeriasarang': 'joyeria-sarang', 'novojoya': 'novojoya'}
DAY = {'casual-coria': '2026-11-20', 'mercedes-beltran': '2026-11-20', 'modas-rocio': '2026-11-21',
       'cent-vuit': '2026-11-20', 'doble-ele': '2026-11-20', 'marga-pineiro': '2026-11-20', 'novojoya': '2026-11-20'}
# Sin propuesta todavía: el cupo diario de Flow se acabó antes de sus últimas fotos (cent-vuit 8, casual-coria 4, doble-ele 2,
# marga-pineiro 1, novojoya 1). Pasan al 20/11 sin slug ni pageUrl (el Lote de hoy no las enseña) hasta que se terminen.
PENDING = {'cent-vuit', 'casual-coria', 'doble-ele', 'marga-pineiro', 'novojoya'}
PEND_NOTE = 'Propuesta del lote 40 a medias (18/11): faltan fotos por el cupo diario de Flow. Sale cuando esté.'
OUT_IG = 'vichy_motril'
VICHY = 'AVISO (18/11): ya vende online en vichymotril.com (tienda con categorías y carrito). Sin propuesta.'

lines = w.split('\n')
k4 = [k for k, l in enumerate(lines) if l.startswith('const SEED4 = ')]
assert len(k4) == 1
rows = json.loads(re.match(r'const SEED4 = (\[.*\]);$', lines[k4[0]]).group(1))
patch = []
for lid, d in rows:
    ig = d['instagram'].rstrip('/').split('/')[-1]
    if ig == OUT_IG:
        d.pop('lotDay', None); d['priority'] = 30
        if VICHY not in d['notes']:
            d['notes'] += '\n' + VICHY
        patch.append([lid, {'lotDay': None, 'priority': 30}])
        continue
    s = SLUG[ig]
    if s in PENDING:
        d['lotDay'] = DAY[s]
        if PEND_NOTE not in d['notes']:
            d['notes'] += '\n' + PEND_NOTE
        patch.append([lid, {'lotDay': d['lotDay']}])
        continue
    d['slug'], d['pageUrl'], d['lotDay'] = s, f'https://404growth.com/p/{s}/', DAY.get(s, '2026-11-19')
    d['notes'] = d['notes'].replace('Falta su propuesta.', 'Propuesta (lote 40): ' + d['pageUrl'])
    patch.append([lid, {'lotDay': d['lotDay'], 'slug': s, 'pageUrl': d['pageUrl']}])
assert len(patch) == 35 and sum(1 for _, p in patch if 'slug' in p) == 29
lines[k4[0]] = 'const SEED4 = ' + json.dumps(rows, ensure_ascii=False) + ';'

kp = [k for k, l in enumerate(lines) if l.startswith('const LEAD_PATCH = ')]
kk = [k for k, l in enumerate(lines) if l.startswith('const LEAD_PATCH_KEY = ')]
assert len(kp) == 1 and len(kk) == 1 and '"lpatch_20261118"' in lines[kk[0]]
assert not any(l.startswith('const LEAD_PATCH_18NOV') for l in lines)
lines[kp[0]] = lines[kp[0]].replace('const LEAD_PATCH = ', 'const LEAD_PATCH_18NOV = ', 1)
lines[kk[0]] = ('const LEAD_PATCH_KEY = "lpatch_20261119";   // 18/11: lote 40 (propuesta nueva): 29 del SEED4 con su slug, pageUrl y lotDay '
                '(19/11; Casual Coria y Mercedes Beltrán el 20, Modas Rocío el 21, para no escribir el mismo día a tiendas del mismo pueblo). '
                'Cent-Vuit, Casual Coria, Doble Ele, Marga Piñeiro y Novojoya pasan al 20/11 sin propuesta (faltan fotos por el cupo de Flow). '
                'Vichy Motril sale del lote: ya vende online. La lista del 18/11 queda como LEAD_PATCH_18NOV.')
lines.insert(kp[0] + 1, 'const LEAD_PATCH = ' + json.dumps(patch, ensure_ascii=False) + ';')
open(out, 'w', encoding='utf-8').write('\n'.join(lines))
print('ok', len(patch), sum(1 for _, p in patch if p.get('lotDay') == '2026-11-19'))
