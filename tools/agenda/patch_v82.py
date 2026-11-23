# python3 patch_v82.py <admin worker v81> <salida admin> <visitas worker> <salida visitas>
# 23/11/2026 (admin v82): avisos de la agenda de las propuestas. /agenda.js manda al contador el evento «ag» con el paso (n)
# y, como mucho, el día o la hora (l). El admin avisa al móvil:
#   - en directo, del paso más avanzado de cada visita en cada pasada del cron (1 pulsa Reservar, 2 día, 3 hora, 4 nombre);
#   - de los fallos (7 le faltan datos, 8 hora ocupada, 9 falla la reserva);
#   - si se queda a medias: 20 min sin reservar y 10 min sin moverse por la página → «Se quedó en …».
# La reserva (6) ya la avisa /l/book («Llamada reservada · …»). Un aviso de cada por visita. Interruptor «agenda» en Avisos.
import sys
a_src, a_out, v_src, v_out = sys.argv[1:5]

w = open(a_src, encoding='utf-8').read()
assert 'kind: "video"' in w, 'falta la v81'
assert 'kind: "agenda"' not in w, 'ya tiene la v82'
def rep(old, new):
    global w
    assert w.count(old) == 1, ('no está una sola vez', old[:70], w.count(old))
    w = w.replace(old, new)

rep('docs: 1, video: 1, high: 1,', 'docs: 1, video: 1, agenda: 1, high: 1,')
rep('"SELECT e.id, e.y, e.m, v.id AS vid, v.slug, v.tc, v.tcm FROM e JOIN v ON v.k = e.k WHERE e.id > ?1 ORDER BY e.id LIMIT 400"',
    '"SELECT e.id, e.y, e.m, e.n, e.l, v.id AS vid, v.slug, v.tc, v.tcm FROM e JOIN v ON v.k = e.k WHERE e.id > ?1 ORDER BY e.id LIMIT 400"')
# in the loop: keep, for each visit, the furthest step seen in this pass; failures alert at once
rep('      if ((r.y === "vplay" || r.y === "vend") && isHuman(r)) {',
    '      if (r.y === "ag" && isHuman(r)) {   /* v82: the agenda of the proposal */\n'
    '        const n = Number(r.n) || 0;\n'
    '        if (n >= 1 && n <= 4) { if (!agTop[r.vid] || n > agTop[r.vid].n) agTop[r.vid] = { n, l: r.l || "", slug: r.slug, vid: r.vid }; }\n'
    '        else if (n >= 5) agStop[r.vid] = 1;\n'
    '        if (n >= 7 && n <= 9) { const base = r.slug.replace(/--web$/, ""); memo[base] = memo[base] || await whoOf(env, base);\n'
    '          if (await alertAdd(env, { slug: base, kind: "agenda", dk: "v" + r.vid + ":ag" + n, title: memo[base].name, body: agText(n, r.l), url: "/admin/crm#visita=" + r.vid, visit: r.vid }, !!cfg.agenda)) out.e++; }\n'
    '      }\n'
    '      if ((r.y === "vplay" || r.y === "vend") && isHuman(r)) {')
rep('    const T = { dl: "ha descargado", print: "ha pedido imprimir", share: "ha usado el botón de compartir", form1: "ha enviado un formulario" };',
    '    const T = { dl: "ha descargado", print: "ha pedido imprimir", share: "ha usado el botón de compartir", form1: "ha enviado un formulario" };\n'
    '    const agTop = {}, agStop = {};')
rep('  } catch (e) { if (!/no such table/i.test(String(e && e.message))) throw e; }\n  /* 3) high interest',
    '    for (const vid of Object.keys(agTop)) {   /* v82: one live alert per visit and pass: the furthest step (not once it is confirming or booked) */\n'
    '      if (agStop[vid]) continue; const x = agTop[vid], base = x.slug.replace(/--web$/, ""); memo[base] = memo[base] || await whoOf(env, base);\n'
    '      if (await alertAdd(env, { slug: base, kind: "agenda", dk: "v" + x.vid + ":ag" + x.n, title: memo[base].name, body: agText(x.n, x.l), url: "/admin/crm#visita=" + x.vid, visit: x.vid }, !!cfg.agenda)) out.e++;\n'
    '    }\n'
    '    /* v82: left the agenda half way: 20 min after its last step, 10 min without moving on the page, and no booking */\n'
    '    const half = (await env.VIS.prepare("SELECT v.id AS vid, v.slug, v.tc, v.tcm, MAX(CASE WHEN e.n BETWEEN 1 AND 5 THEN e.n WHEN e.n = 7 THEN 4 ELSE 0 END) AS mx, SUM(CASE WHEN e.n = 6 THEN 1 ELSE 0 END) AS ok, MAX(e.rt) AS lt FROM e JOIN v ON v.k = e.k WHERE e.y = \'ag\' AND e.rt > ?1 AND COALESCE(v.seen, v.ts) < ?2 GROUP BY e.k HAVING ok = 0 AND mx > 0 AND lt < ?3 LIMIT 50").bind(now - 3 * 3600000, now - 600000, now - 1200000).all()).results || [];\n'
    '    for (const h of half) { if (!isHuman(h)) continue; const base = h.slug.replace(/--web$/, ""); memo[base] = memo[base] || await whoOf(env, base);\n'
    '      if (await alertAdd(env, { slug: base, kind: "agenda", dk: "v" + h.vid + ":agx", title: memo[base].name, body: "Se fue sin reservar. Llegó hasta: " + AG_STEP[h.mx] + ".", url: "/admin/crm#visita=" + h.vid, visit: h.vid }, !!cfg.agenda)) out.e++; }\n'
    '  } catch (e) { if (!/no such table/i.test(String(e && e.message))) throw e; }\n  /* 3) high interest')
rep('async function alertsRun(env) {',
    '/* v82: the steps of the agenda of a proposal (event «ag», n = the step; l = the button, the day or the hour, never what is typed) */\n'
    'const AG_STEP = { 1: "pulsar «Reservar»", 2: "elegir día", 3: "elegir hora", 4: "poner su nombre", 5: "pulsar «Confirmar llamada»" };\n'
    'function agText(n, l) { l = String(l || "").slice(0, 80);\n'
    '  return n === 1 ? "Ha pulsado «" + (l || "Reservar") + "» y ha bajado a la agenda." : n === 2 ? "Está en la agenda: ha elegido día" + (l ? " (" + l + ")" : "") + "." :\n'
    '    n === 3 ? "Ha elegido hora en la agenda: " + (l || "—") + ". Le faltan sus datos." : n === 4 ? "Ha puesto su nombre en la agenda. Le falta el email y el WhatsApp." :\n'
    '    n === 7 ? "Ha pulsado «Confirmar llamada», pero le faltaba algo (" + (l || "datos") + ")." : n === 8 ? "Quería reservar a una hora que se acababa de ocupar" + (l ? " (" + l + ")" : "") + "." :\n'
    '    n === 9 ? "Ha intentado reservar y ha fallado (" + (l || "error") + "). Escríbele." : "Agenda: paso " + n + "."; }\n'
    'async function alertsRun(env) {')
# the admin page: the label of the alert, its switch and the step in the timeline of a visit
rep("docs: 'Documento', video: 'Vídeo', high:", "docs: 'Documento', video: 'Vídeo', agenda: 'Agenda', high:")
rep("sw('video', 'Si empieza a ver el vídeo de su propuesta o lo termina') +",
    "sw('video', 'Si empieza a ver el vídeo de su propuesta o lo termina') + sw('agenda', 'Si pulsa Reservar, avanza en la agenda, falla o se va a medias') +")
rep("      case 'form0': return 'Empieza a rellenar un formulario';",
    "      case 'ag': return 'Agenda: ' + ({1:'pulsa Reservar',2:'elige día',3:'elige hora',4:'pone su nombre',5:'pulsa Confirmar llamada',6:'reservada',7:'le faltan datos',8:'la hora se acaba de ocupar',9:'falla la reserva'}[e.n] || 'paso ' + e.n) + (l ? ' ' + l : '');\\n      case 'form0': return 'Empieza a rellenar un formulario';")
open(a_out, 'w', encoding='utf-8').write(w)

v = open(v_src, encoding='utf-8').read()
assert ' ag: [],' not in v, 'el contador ya tiene «ag»'
old = '  form0: ["form"], form1: ["form"],'
assert v.count(old) == 1
v = v.replace(old, '  ag: [],\n' + old)
old = '["scr", "exp", "col", "tab", "vplay", "copy", "form0", "print", "sin"]'
assert v.count(old) == 1
v = v.replace(old, '["scr", "exp", "col", "tab", "vplay", "copy", "form0", "print", "sin", "ag"]')
open(v_out, 'w', encoding='utf-8').write(v)
print('ok', len(w), len(v))
