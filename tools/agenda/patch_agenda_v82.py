import sys
p=sys.argv[1]
w=open(p,encoding="utf-8").read()
assert "__c404ev" not in w
for o,n in [["------- los huec", "------- v82 (23/11/2026): cada paso de la agenda va al contador de la propuesta, para que el admin avise a Chris.\n     1 pulsa Reservar · 2 elige día · 3 elige hora · 4 pone su nombre · 5 pulsa Confirmar · 6 reservada · 7 le faltan datos · 8 hora ocupada · 9 falla.\n     Nunca va nada de lo que escribe: solo el paso y, como mucho, el día o la hora que elige. ---------- */\n  function T(n, l) { try { if (window.__c404ev) window.__c404ev('ag', { n: n, l: String(l || '').slice(0, 80) }); } catch (e) {} }\n\n  /* ---------- los huec"], ["ay = k; var hr =", "ay = k; T(2, fD.format(new Date(k + 'T12:00:00Z')).replace('.', '')); var hr ="], [" = iso; $('ag-se", " = iso; T(3, cap(fL.format(new Date(iso))));$('ag-se"], ["us(); } q(2); }\n", "us(); } T(4); q(2); }\n"], ["!all) { err.text", "!all) { T(7, !ok.email && !ok.phone ? 'sin email ni WhatsApp' : !ok.email ? 'sin email válido' : 'sin WhatsApp válido'); err.text"], ["n = true; var go", "n = true; T(5); var go"], [" j.ok) {\n       ", " j.ok) { T(6, cap(fL.format(new Date(j.start || pick))));\n       "], ["ken') { SL = j.s", "ken') { T(8, cap(fL.format(new Date(pick)))); SL = j.s"], [" }\n      err.inn", " }\n      T(9, j && j.error ? String(j.error) : 'sin respuesta'); err.inn"], ["); load();\n    r", "); load(); T(1, (a.textContent || '').replace(/[→↓]/g, '').trim());\n    r"]]:
    assert w.count(o)==1,o
    w=w.replace(o,n)
open(sys.argv[2],"w",encoding="utf-8").write(w)
print("ok",len(w))
