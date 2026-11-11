# 404 Growth · factura en PDF con el mismo diseño que la 2026-151 de Kiss of Life (9/11/2026): logo, SF Pro, colores y bloques.
# python3 factura.py <datos.json> <salida.html>
#   y después el PDF con el Playwright del Mac (para que lleve la SF Pro): page.pdf({format:'A4', printBackground:true, margin 0}).
# Los importes van en céntimos. Si «total» viene con IVA incluido, la base y el IVA se calculan desde él (redondeo al céntimo).
# Un dato entre [corchetes] sale marcado en amarillo: falta por rellenar.
import base64, html, json, os, re, sys

H = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(sys.argv[1], encoding='utf-8'))
OUT = sys.argv[2]

def eur(c):
    s = '{:,.2f}'.format(c / 100).replace(',', 'X').replace('.', ',').replace('X', '.')
    return s + ' €'

def t(x):
    # texto escapado; lo que va entre [corchetes] se marca como pendiente
    return re.sub(r'\[([^\]]*)\]', r'<mark>[\1]</mark>', html.escape(str(x)))

rate = D.get('iva', 21)
lines = D['lineas']
for l in lines:
    if 'total' in l and 'precio' not in l:       # precio con IVA incluido → precio sin IVA por unidad
        l['precio'] = round(l['total'] / (1 + rate / 100) / l.get('uds', 1))
base = sum(l['precio'] * l.get('uds', 1) for l in lines)
iva = round(base * rate / 100)
if 'total_con_iva' in D:                          # cuadra el total exacto que se ha cerrado con el cliente
    iva = D['total_con_iva'] - base
total = base + iva

logo = 'data:image/jpeg;base64,' + base64.b64encode(open(os.path.join(H, 'logo-404.jpg'), 'rb').read()).decode()
E, C = D['emisor'], D['cliente']

def block(lbl, rows, first_bold=True):
    out = '<div class="who"><div class="lbl">%s</div>' % lbl
    for i, r in enumerate(rows):
        if not r: continue
        out += '<div%s>%s</div>' % (' class="b"' if i == 0 and first_bold else '', r)
    return out + '</div>'

cli_name = '<b>%s</b>%s' % (t(C['nombre']), (' (%s)' % t(C['marca'])) if C.get('marca') else '')
rows = ''.join(
    '<tr><td class="c"><div class="it">%s</div>%s</td><td class="n">%s</td><td class="n">%s</td><td class="n">%s</td></tr>' % (
        t(l['concepto']), ('<div class="ds">%s</div>' % t(l['detalle'])) if l.get('detalle') else '',
        l.get('uds', 1), eur(l['precio']), eur(l['precio'] * l.get('uds', 1)))
    for l in lines)

CSS = '''
@page{size:A4;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:794px;height:1123px;background:#fff}
body{font-family:-apple-system,BlinkMacSystemFont,"SF Pro Text","SF Pro Display","Helvetica Neue",Helvetica,Arial,sans-serif;color:#141A16;font-size:13.5px;line-height:19.5px;-webkit-font-smoothing:antialiased;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.pg{position:relative;width:794px;height:1123px;padding:76px 75.6px 0}
b,.b{font-weight:600}
mark{background:#FFF2A8;color:inherit;border-radius:3px;padding:0 2px}
.hd{display:flex;justify-content:space-between;align-items:flex-start;height:136px;border-bottom:1px solid #141A16}
.brand{display:flex;align-items:center;gap:10px;font-size:20px;line-height:38px;font-weight:600;letter-spacing:-.01em}
.brand img{width:38px;height:38px;border-radius:8.5px;display:block}
.ttl{text-align:right}
.ttl h1{font-size:34px;line-height:34px;font-weight:700;letter-spacing:-.035em;margin:-2px 0 7px}
.ttl div{color:#4A524C}
.ttl div b{color:#141A16}
.parts{display:grid;grid-template-columns:344px 1fr;margin-top:33px}
.lbl{font-size:10px;line-height:14px;font-weight:500;letter-spacing:.06em;text-transform:uppercase;color:#6B736D;margin-bottom:6px}
table{width:100%;border-collapse:collapse;margin-top:38px}
th{font-size:10.5px;line-height:14px;font-weight:600;color:#6B736D;text-align:right;padding:0 0 10px;border-bottom:1px solid #CFD5D0;white-space:nowrap}
th.c{text-align:left}
td{vertical-align:top;padding:12px 0 13px;border-bottom:1px solid #E3E7E4}
td.n{text-align:right;white-space:nowrap;font-size:13.5px}
.it{font-size:14px;line-height:19px;font-weight:600}
.ds{font-size:11.3px;line-height:16.3px;color:#5D665F;margin-top:3px;max-width:395px}
.tot{margin:26px 0 0 auto;width:295px}
.tot .r{display:flex;justify-content:space-between;font-size:13.7px;line-height:20px;padding:4px 0 5px}
.tot .g{display:flex;justify-content:space-between;font-size:19.2px;line-height:26px;font-weight:700;border-top:1px solid #141A16;margin-top:4px;padding-top:9.5px}
.pay{position:absolute;left:75.6px;right:75.6px;top:902px;background:#EEF2EF;border-radius:11px;padding:22px 22.5px 24px;display:grid;grid-template-columns:310px 1fr;font-size:14.2px;line-height:19.6px}
.foot{position:absolute;left:75.6px;top:1048.7px;font-size:9.8px;line-height:14px;color:#7A827C}
'''

DOC = '''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Factura %(num)s %(cli)s</title><style>%(css)s</style></head><body><div class="pg">
<div class="hd"><div class="brand"><img src="%(logo)s" alt="">404 Growth</div>
<div class="ttl"><h1>Factura</h1><div>N.º <b>%(num)s</b></div><div>Fecha <b>%(fecha)s</b></div>%(venc)s</div></div>
<div class="parts">%(emi)s%(cli_b)s</div>
<table><thead><tr><th class="c">Concepto</th><th style="width:40px">Uds.</th><th style="width:%(cw)spx">Precio</th><th style="width:%(cw)spx">Importe</th></tr></thead><tbody>%(rows)s</tbody></table>
<div class="tot"><div class="r"><span>Base imponible</span><span>%(base)s</span></div><div class="r"><span>IVA %(rate)s %%</span><span>%(iva)s</span></div><div class="g"><span>Total</span><span>%(total)s</span></div></div>
<div class="pay"><div><div class="lbl">Forma de pago</div>%(pago)s</div><div><div class="lbl">Concepto de la transferencia</div><div>%(ctrans)s</div></div></div>
<div class="foot">%(nota)s</div>
</div></body></html>''' % dict(
    cw=66 if max(l['precio'] * l.get('uds', 1) for l in lines) < 100000 else 84,   # columnas más anchas con importes de 1.000 € o más
    css=CSS, logo=logo, num=t(D['numero']), cli=html.escape(C.get('nombre', '')), fecha=t(D['fecha']),
    venc=('<div>Vencimiento <b>%s</b></div>' % t(D['vencimiento'])) if D.get('vencimiento') else '',
    emi=block('Emisor', [t(E['nombre']), t(E['nif']), t(E['calle']), t(E['cp_ciudad']), t(E.get('telefono', '')), t(E.get('email', ''))]),
    cli_b=block('Cliente', [cli_name, t(C['nif']), t(C['calle']), t(C['cp_ciudad']), t(C.get('telefono', '')), t(C.get('email', ''))], first_bold=False),
    rows=rows, base=eur(base), rate=str(rate).replace('.', ','), iva=eur(iva), total=eur(total),
    pago=''.join('<div>%s</div>' % t(x) for x in D['pago']), ctrans=t(D['concepto_transferencia']),
    nota=t(D.get('nota', 'Factura sin retención de IRPF.')))

open(OUT, 'w', encoding='utf-8').write(DOC)
print(OUT, 'base', base, 'iva', iva, 'total', total)
