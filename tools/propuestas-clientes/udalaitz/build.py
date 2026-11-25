# python3 build.py <salida index.html>: la landing de Udalaitz con el contador de visitas (slug udalaitz-presupuesto, avisa a Chris al abrirla).
import sys, pathlib
here = pathlib.Path(__file__).parent
html = (here / 'landing.html').read_text(encoding='utf-8')
cnt = (here / '../../../prospeccion/l33/tpl/counter.html').resolve().read_text(encoding='utf-8')
assert cnt.count('slug="cafe-con-bacon"') == 1
cnt = cnt.replace('slug="cafe-con-bacon"', 'slug="udalaitz-presupuesto"')
out = html.replace('</body>', cnt + '\n</body>')
pathlib.Path(sys.argv[1]).write_text(out, encoding='utf-8')
print('ok', len(out))
