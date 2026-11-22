# 22/11/2026 (lote 42): pone en el worker del admin el SEED6 con propuesta (33 tiendas) y el LEAD_PATCH nuevo (lpatch_20261123).
# uso: python3 patch_l42.py <worker con seed_20261123b sin propuesta> rows42.js <salida>
# - cambia las líneas «const SEED6_KEY» y «const SEED6» por las de rows42.js (misma clave: aún no se ha subido);
# - la lista LEAD_PATCH del 19/11 pasa a LEAD_PATCH_19NOV (ya aplicada) y su clave se quita;
# - añade LEAD_PATCH_KEY/LEAD_PATCH nuevos justo después del SEED6.
import sys
src, rows, out = sys.argv[1:4]
L = open(src, encoding='utf-8').read().split('\n')
R = open(rows, encoding='utf-8').read().rstrip('\n').split('\n')
assert len(R) == 4 and R[0].startswith('const SEED6_KEY') and R[2].startswith('const LEAD_PATCH_KEY = "lpatch_20261123"')
ix = {k: [i for i, l in enumerate(L) if l.startswith(k)] for k in ('const SEED6_KEY', 'const SEED6 ', 'const LEAD_PATCH_KEY', 'const LEAD_PATCH ')}
assert all(len(v) == 1 for v in ix.values()), {k: len(v) for k, v in ix.items()}
assert '"seed_20261123b"' in L[ix['const SEED6_KEY'][0]]
assert '"lpatch_20261119"' in L[ix['const LEAD_PATCH_KEY'][0]]
assert not any(l.startswith('const LEAD_PATCH_19NOV') for l in L)
L[ix['const SEED6_KEY'][0]] = R[0]
L[ix['const SEED6 '][0]] = R[1] + '\n' + R[2] + '\n' + R[3]
L[ix['const LEAD_PATCH '][0]] = L[ix['const LEAD_PATCH '][0]].replace('const LEAD_PATCH = ', 'const LEAD_PATCH_19NOV = ', 1)
del L[ix['const LEAD_PATCH_KEY'][0]]
open(out, 'w', encoding='utf-8').write('\n'.join(L))
print('ok')
