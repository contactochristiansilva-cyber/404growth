#!/usr/bin/env python3
"""v77g (18/11/2026): posts «solo LinkedIn» en el admin (LinkedIn y blog), para las ofertas de empleo.

    python3 patch_v77g.py <worker.js con la v77f> [salida]

- lpost.auto = 2 es un post solo de LinkedIn: no crea artículo en el blog, no lleva «Visita mi web» delante,
  no necesita título ni artículo y publicarlo no borra el borrador del día.
- Los 3 posts de las ofertas (li-posts.json) entran una sola vez como borradores (LIJOB_KEY) al abrir LinkedIn y blog.
- El blog, sus métricas y el borrador diario con IA no los tienen en cuenta.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
src = sys.argv[1]
out = sys.argv[2] if len(sys.argv) > 2 else src
s = open(src, encoding='utf-8').read()
assert 'async function liJobSeed(' not in s, 'ya tiene la v77g'
POSTS = json.load(open(os.path.join(HERE, 'li-posts.json'), encoding='utf-8'))


def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (a[:90], c)
    s = s.replace(a, b)


def js(x):   # un trozo del admin tal y como va dentro de PAGES (cadena JSON)
    return json.dumps(x, ensure_ascii=False)[1:-1]


# ---------- servidor ----------
rep('const LI_WEB = "Visita mi web: https://404growth.com";',
    '/* v77g (18/11/2026): posts solo de LinkedIn (lpost.auto = 2), sin blog ni «Visita mi web». Los 3 de las ofertas de empleo entran una vez como borradores. */\n'
    'const LIJOB_KEY = "lijob_20261118";\n'
    'const LIJOB = ' + json.dumps(POSTS, ensure_ascii=False) + ';\n'
    'async function liJobSeed(env) {\n'
    '  if (await getMeta(env, LIJOB_KEY)) return;\n'
    '  await setMeta(env, LIJOB_KEY, "1");\n'
    '  const now = Date.now();\n'
    '  for (let i = 0; i < LIJOB.length; i++) { const p = LIJOB[i]; await env.DB.prepare("INSERT OR IGNORE INTO lpost (slug, title, descr, kw, li, body, status, created, updated, auto) VALUES (?1, ?2, \'\', \'\', ?3, \'\', \'draft\', ?4, ?4, 2)").bind(p.slug, p.title, p.li, now - i * 1000).run(); }\n'
    '}\n'
    'const LI_WEB = "Visita mi web: https://404growth.com";')
rep('  if (p === "li" && m === "GET") {\n',
    '  if (p === "li" && m === "GET") {\n    try { await liJobSeed(env); } catch (e) {}   // v77g\n')
rep('    const r = await DBq.prepare("SELECT * FROM lpost WHERE slug = ?1").bind(str(b.slug, 120)).first(); if (!r) return bad("missing", 404);\n    if (!r.title || !r.body) return bad("empty");',
    '    const r = await DBq.prepare("SELECT * FROM lpost WHERE slug = ?1").bind(str(b.slug, 120)).first(); if (!r) return bad("missing", 404);\n'
    '    if (r.auto === 2) {   // v77g: solo LinkedIn, tal cual (sin «Visita mi web», sin blog, sin tocar el borrador del día)\n'
    '      if (r.li_url) return json({ ok: true, slug: r.slug, li: r.li_url, lionly: true });\n'
    '      if (!b.li || !String(r.li || "").trim()) return bad("nopost");\n'
    '      let li; try { li = await liPost(env, String(r.li).trim()); } catch (e) { return json({ error: e.code || "lipost", detail: e.detail || String(e.message).slice(0, 200) }, e.code === "noli" ? 400 : 502); }\n'
    '      await DBq.prepare("UPDATE lpost SET status = \'published\', published = COALESCE(published, ?1), updated = ?1, li_url = ?2 WHERE slug = ?3").bind(now, li, r.slug).run();\n'
    '      return json({ ok: true, slug: r.slug, li, lionly: true });\n'
    '    }\n'
    '    if (!r.title || !r.body) return bad("empty");')
rep('SELECT COUNT(*) AS n FROM lpost WHERE created >= ?1 OR published >= ?1 OR status = \'draft\'',
    'SELECT COUNT(*) AS n FROM lpost WHERE (created >= ?1 OR published >= ?1 OR status = \'draft\') AND auto != 2')
rep('SELECT 1 AS x FROM lpost WHERE slug = ?1 AND status = \'published\'', 'SELECT 1 AS x FROM lpost WHERE slug = ?1 AND status = \'published\' AND auto != 2')
rep('SELECT slug, title, published FROM lpost WHERE status = \'published\' ORDER BY published DESC', 'SELECT slug, title, published FROM lpost WHERE status = \'published\' AND auto != 2 ORDER BY published DESC')
rep('SELECT slug, title, descr, kw, body, published, updated FROM lpost WHERE status = \'published\' ORDER BY published DESC',
    'SELECT slug, title, descr, kw, body, published, updated FROM lpost WHERE status = \'published\' AND auto != 2 ORDER BY published DESC')

# ---------- admin (LinkedIn y blog) ----------
rep(js("    if(cur){var first=(cur.li||'').split('\\n').slice(0,3).join('\\n');\n      h+='<form class=\"panel li-ed\""),
    js("    if(cur){var first=(cur.li||'').split('\\n').slice(0,3).join('\\n');\n      if(cur.auto===2)h+=liJobForm(cur,first,d);else h+='<form class=\"panel li-ed\""))
rep(js("function soForm(){"),
    js("function liJobForm(cur,first,d){return '<form class=\"panel li-ed\" id=\"li-ed\" data-slug=\"'+esc(cur.slug)+'\"><div class=\"row\" style=\"align-items:center\"><b style=\"flex:1\">Solo LinkedIn · '+esc(cur.title||'Post')+'</b><button type=\"button\" class=\"btn sm\" data-so=\"del\">Borrar</button></div>'+\n"
       "    '<p class=\"hint\" style=\"margin:6px 0 0\">Va solo a tu perfil de LinkedIn, tal cual: no crea artículo en el blog ni le pone «Visita mi web» delante.</p>'+\n"
       "    '<label>Post de LinkedIn <span class=\"cnt\" id=\"li-n\">'+(cur.li||'').length+' / 3.000</span></label><textarea name=\"li\" rows=\"20\" maxlength=\"3000\">'+esc(cur.li||'')+'</textarea>'+\n"
       "    '<label>Así se verá antes de «ver más»</label><div class=\"li-pv\" id=\"li-pv\">'+esc(first.slice(0,210))+((cur.li||'').length>210?'<i>… ver más</i>':'')+'</div>'+\n"
       "    '<label>Nombre (solo lo ves tú) <span class=\"cnt\" id=\"ti-n\" hidden></span><span id=\"de-n\" hidden></span></label><input name=\"title\" maxlength=\"120\" value=\"'+esc(cur.title||'')+'\">'+\n"
       "    '<input type=\"hidden\" name=\"kw\" value=\"\"><input type=\"hidden\" name=\"descr\" value=\"\"><textarea name=\"body\" hidden></textarea>'+\n"
       "    '<div class=\"row\" style=\"margin-top:16px;flex-wrap:wrap\"><button class=\"btn\" type=\"submit\">Guardar</button><span style=\"flex:1\"></span><button type=\"button\" class=\"btn pri\" data-so=\"pub\" data-lionly=\"1\"'+(d.connected?'':' disabled title=\"Conecta LinkedIn primero\"')+'>Publicar en LinkedIn</button></div></form>'}\n"
       "  function soForm(){"))
rep(js("if(a==='pub'&&!confirm('Se publica ahora en tu perfil de LinkedIn y en el blog. ¿Seguro?'))return;"),
    js("if(a==='pub'&&!confirm(b.dataset.lionly?'Se publica ahora en tu perfil de LinkedIn, tal cual (no va al blog). ¿Seguro?':'Se publica ahora en tu perfil de LinkedIn y en el blog. ¿Seguro?'))return;"))
rep(js("toast(r.li?'Publicado en LinkedIn y en el blog':'Publicado en el blog')"),
    js("toast(r.lionly?'Publicado en LinkedIn':r.li?'Publicado en LinkedIn y en el blog':'Publicado en el blog')"))
rep(js("+'</td><td><a href=\"/blog/'+esc(p.slug)+'\" target=\"_blank\" rel=\"noopener\">'+esc(p.title)+'</a><br><span class=\"hint\">'+esc(p.kw||'')+'</span></td><td>'"),
    js("+'</td><td>'+(p.auto===2?esc(p.title)+'<br><span class=\"hint\">Solo LinkedIn</span>':'<a href=\"/blog/'+esc(p.slug)+'\" target=\"_blank\" rel=\"noopener\">'+esc(p.title)+'</a><br><span class=\"hint\">'+esc(p.kw||'')+'</span>')+'</td><td>'"))
rep(js("<td class=\"n\"><button type=\"button\" class=\"btn sm\" data-sounpub=\"'+esc(p.slug)+'\">Retirar</button></td></tr>'"),
    js("<td class=\"n\">'+(p.auto===2?'':'<button type=\"button\" class=\"btn sm\" data-sounpub=\"'+esc(p.slug)+'\">Retirar</button>')+'</td></tr>'"))

open(out, 'w', encoding='utf-8').write(s)
print('ok', out, len(s))
