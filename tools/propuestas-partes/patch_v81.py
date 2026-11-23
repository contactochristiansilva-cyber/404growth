# python3 patch_v81.py <worker.js> <salida>
# 23/11/2026 (admin v81): aviso al móvil cuando alguien empieza el vídeo de su propuesta (vplay) y cuando lo termina (vend).
# Un aviso de cada por visita (dk = v<visita>:vplay|vend). Interruptor nuevo en Avisos: «Si empieza a ver el vídeo o lo termina».
import sys
src, out = sys.argv[1:3]
w = open(src, encoding='utf-8').read()
assert 'kind: "video"' not in w, 'ya tiene la v81'

def rep(old, new):
    global w
    assert w.count(old) == 1, ('no está una sola vez', old[:60], w.count(old))
    w = w.replace(old, new)

rep('const ACFG = { entry: 1, contact: 1, meeting: 1, docs: 1, high: 1,',
    'const ACFG = { entry: 1, contact: 1, meeting: 1, docs: 1, video: 1, high: 1,')
rep('      await setMeta(env, "al_e", String(r.id));',
    '      if ((r.y === "vplay" || r.y === "vend") && isHuman(r)) {   /* v81: the video of the proposal */\n'
    '        const base = r.slug.replace(/--web$/, ""); memo[base] = memo[base] || await whoOf(env, base);\n'
    '        if (await alertAdd(env, { slug: base, kind: "video", dk: "v" + r.vid + ":" + r.y, title: memo[base].name, body: r.y === "vplay" ? "Ha empezado a ver el vídeo de su propuesta." : "Ha visto el vídeo de su propuesta hasta el final.", url: "/admin/crm#visita=" + r.vid, visit: r.vid }, !!cfg.video)) out.e++;\n'
    '      }\n'
    '      await setMeta(env, "al_e", String(r.id));')
rep("docs: 'Documento', high:", "docs: 'Documento', video: 'Vídeo', high:")
rep("sw('docs', 'Si descarga, imprime, comparte o envía un formulario') +",
    "sw('docs', 'Si descarga, imprime, comparte o envía un formulario') + sw('video', 'Si empieza a ver el vídeo de su propuesta o lo termina') +")
open(out, 'w', encoding='utf-8').write(w)
print('ok', len(w))
