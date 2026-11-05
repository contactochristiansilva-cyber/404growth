"""Hoja de envíos del día: por tienda, propuesta, WhatsApp (A/B con su captura), Instagram, correo (copiar el cuerpo visual)
y llamada si solo hay fijo. uso: python3 envios.py <slug>... → l33/envios.html"""
import base64, html, io, json, os, re, sys, urllib.parse
from PIL import Image
S = os.path.dirname(os.path.abspath(__file__)); B = os.path.dirname(S); L31 = os.path.join(B, 'l31')
sys.path.insert(0, os.path.join(L31, 'tools'))
from shops import SHOPS
E = html.escape
NOUN = {'moda': 'vuestras prendas', 'joya': 'vuestras joyas', 'obrador': 'vuestros dulces', 'deco': 'vuestras piezas', 'hogar': 'vuestros textiles'}
D = {}
for f in ['l31/l32/data.json', 'l33/data.json']:
    p = os.path.join(B, f)
    if os.path.exists(p): D.update(json.load(open(p)))
MAIL = json.load(open(os.path.join(S, 'mail', 'index.json'))) if os.path.exists(os.path.join(S, 'mail', 'index.json')) else {}


def num(d):
    w = d.get('whatsapp') or (d.get('phone') if d.get('phone_type') == 'móvil' else '')
    w = re.sub(r'\D', '', w or '')
    if w and not w.startswith('34') and len(w) == 9: w = '34' + w
    return w


NOUN_TU = {'moda': 'tus prendas', 'joya': 'tus joyas', 'obrador': 'tus dulces', 'deco': 'tus piezas', 'hogar': 'tus textiles'}


def msgs(c, d=None):
    sh = c['short']; noun = NOUN.get(c['niche'], 'vuestros productos'); n = (d or {}).get('owner_first')
    if n:  # sabemos quién la lleva (lo publica la propia tienda): de tú y por su nombre
        nt = NOUN_TU.get(c['niche'], 'tus productos')
        a = (f'Hola {n}, soy Christian, de 404 Growth. He visto el Instagram de {sh} y te he montado cómo quedaría como tienda online, '
             f'con {nt} y tu marca (te dejo una captura). ¿Te paso el enlace para que la veas entera?')
        b = (f'Hola {n}, soy Christian, de 404 Growth. Te he montado cómo quedaría {sh} como tienda online, con {nt} y tu marca. '
             f'Aquí la tienes, se ve mejor en el móvil:\n404growth.com/p/{c["slug"]}/\nSi te gusta, te cuento por aquí o en una llamada corta cómo la dejamos vendiendo en 15 días.')
        return a, b
    a = (f'Hola, ¿sois {sh}? Soy Christian, de 404 Growth. He visto vuestro Instagram y os he montado cómo quedaría {sh} como tienda online, '
         f'con {noun} y vuestra marca (os dejo una captura). ¿Os paso el enlace para que la veáis entera?')
    b = (f'Hola, soy Christian, de 404 Growth. Os he montado cómo quedaría {sh} como tienda online, con {noun} y vuestra marca. '
         f'Aquí la tenéis, se ve mejor en el móvil:\n404growth.com/p/{c["slug"]}/\nSi os gusta, os cuento por aquí o en una llamada corta cómo la dejamos vendiendo en 15 días.')
    return a, b


def thumb(s):
    p = os.path.join(S, 'wa', s + '.png')
    if not os.path.exists(p): return ''
    im = Image.open(p).convert('RGB'); im.thumbnail((750, 1500)); bio = io.BytesIO(); im.save(bio, 'JPEG', quality=82)
    return 'data:image/jpeg;base64,' + base64.b64encode(bio.getvalue()).decode()


def card(k, s):
    c = SHOPS[s]; c['slug'] = s; d = D.get(s, {}); a, b = msgs(c, d); var = 'A' if k % 2 == 0 else 'B'; txt = a if var == 'A' else b
    w = num(d); im = thumb(s); mail = MAIL.get(s, {}); em = (d.get('email') or '').strip()
    body = open(os.path.join(S, 'mail', s + '.html')).read() if os.path.exists(os.path.join(S, 'mail', s + '.html')) else ''
    page = f'https://404growth.com/p/{s}/'
    h = (f'<article class="c" id="{s}"><header><div><b>{E(c["name"])}</b><span>{E(d.get("city", c.get("city", "")))} · {E(str(d.get("followers", "")))} seguidores · {E(c["niche"])}</span></div>'
         f'<label class="ok"><input type="checkbox" data-k="{s}"> Hecho</label></header><div class="g">')
    if im: h += f'<a class="ph" href="{im}" download="{s}.jpg" title="Descargar captura"><img src="{im}" alt=""><em>Descargar captura</em></a>'
    h += '<div class="ch">'
    if d.get('warn'): h += f'<p class="warn">{E(d["warn"])}</p>'
    if d.get('contact_source'): h += f'<p class="src"><b>Contacto:</b> {E(d["contact_source"])}<br><b>Dueño/a:</b> {E(d.get("owner_note", ""))}</p>'
    h += f'<p class="ln"><a href="{page}" target="_blank">{page.replace("https://", "")}</a></p>'
    if w:
        h += (f'<section><h4>WhatsApp · variante {var}</h4><pre>{E(txt)}</pre><div class="bt"><a class="b1" href="https://wa.me/{w}?text={urllib.parse.quote(txt)}" target="_blank">Abrir WhatsApp</a>'
              f'<button data-copy="{E(txt)}">Copiar texto</button></div><small>Adjunta la captura antes de enviar.</small></section>')
    elif d.get('phone'):
        h += (f'<section><h4>Teléfono {E(d.get("phone_type", ""))} · sin WhatsApp</h4><p><a href="tel:{E(d["phone"])}">{E(d["phone"])}</a> — llamad y pedid por la dueña: '
              '«Os he montado vuestra tienda online con vuestros productos, ¿os la mando por WhatsApp o por correo?»</p></section>')
    ig = d.get('handle') or c.get('handle')
    if ig:
        h += (f'<section><h4>Instagram · @{E(ig)}</h4><pre>{E(a)}</pre><div class="bt"><a class="b1" href="https://ig.me/m/{E(ig)}" target="_blank">Abrir mensaje</a>'
              f'<button data-copy="{E(a)}">Copiar texto</button></div><small>Adjunta la captura. El enlace, cuando contesten.</small></section>')
    if em:
        su = mail.get('subject') or f'{c["name"]}: vuestra tienda online, ya montada'
        gm = 'https://mail.google.com/mail/?authuser=hola@404growth.com#search/' + urllib.parse.quote('in:draft "' + su + '"')
        h += (f'<section><h4>Correo · {E(em)}</h4><p class="su">{E(su)}</p><div class="bt"><a class="b1" href="{E(gm)}" target="_blank">Abrir el borrador</a></div>'
              f'<small>El borrador ya está en Gmail (hola@) con este destinatario: ábrelo y envía.</small></section>')
    elif True:
        h += '<section><h4>Correo</h4><p class="mu">No tienen correo público.</p></section>'
    return h + '</div></div></article>'


def main(slugs, pend, fuera=()):
    css = ('*{box-sizing:border-box}body{margin:0;font:15px/1.45 -apple-system,BlinkMacSystemFont,"SF Pro Text","Helvetica Neue",Arial,sans-serif;background:#f4f3f1;color:#161514}'
           '.w{max-width:1100px;margin:0 auto;padding:28px 16px 80px}h1{font:600 30px/1.1 -apple-system,BlinkMacSystemFont,"SF Pro Display",sans-serif;letter-spacing:-.02em;margin:0 0 6px}'
           '.lead{color:#6b6762;margin:0 0 22px}.tips{background:#fff;border-radius:16px;padding:16px 20px;margin-bottom:22px;box-shadow:inset 0 0 0 1px #e7e4e0}.tips b{display:block;margin-bottom:6px}'
           '.tips ol{margin:0;padding-left:20px}.tips li{margin:4px 0}.c{background:#fff;border-radius:18px;margin:0 0 16px;box-shadow:inset 0 0 0 1px #e7e4e0;overflow:hidden}'
           '.c header{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:14px 18px;border-bottom:1px solid #eeebe7}.c header b{font-size:17px;display:block}.c header span{color:#6b6762;font-size:13px}'
           '.ok{font-size:13px;white-space:nowrap}.c.done{opacity:.45}.g{display:grid;grid-template-columns:150px 1fr;gap:18px;padding:16px 18px}'
           '.ph{display:block;text-decoration:none;color:#6b6762;font-size:12px;text-align:center}.ph img{width:100%;border-radius:14px;display:block;margin-bottom:6px}'
           'section{padding:10px 0;border-top:1px solid #f0eeeb}section:first-of-type{border-top:0}h4{margin:0 0 6px;font-size:13px;font-weight:600;color:#3a3734}'
           'pre{white-space:pre-wrap;font-family:inherit;font-size:14px;line-height:1.45;background:#f7f6f4;border-radius:10px;padding:10px 12px;margin:0 0 8px}.bt{display:flex;gap:8px;flex-wrap:wrap}'
           '.bt a,.bt button{font:600 13px/1 inherit;padding:10px 14px;border-radius:99px;border:0;cursor:pointer;text-decoration:none;background:#ecebe8;color:#161514}'
           '.bt .b1{background:#161514;color:#fff}small{display:block;color:#8a857f;font-size:12px;margin-top:6px}.ln{margin:0 0 4px;font-size:13px}.ln a{color:#2e7a64}'
           '.rs{width:100%;border-collapse:collapse;font-size:13px;margin-top:6px}.rs th{text-align:left;color:#6b6762;font-weight:600;padding:6px 8px;border-bottom:1px solid #e7e4e0}.rs td{padding:6px 8px;border-bottom:1px solid #f0eeeb;vertical-align:top}.rs a{color:#161514}@media(max-width:640px){.rs th:nth-child(4),.rs td:nth-child(4){display:none}}.warn{background:#fdecea;color:#8a1f17;border-radius:10px;padding:10px 12px;margin:0 0 10px;font-weight:600}.src{font-size:13px;color:#4a4642;background:#f7f6f4;border-radius:10px;padding:8px 12px;margin:0 0 8px}.su{margin:0 0 8px;font-weight:600}.mu{color:#8a857f;margin:0}.pend{background:#fff;border-radius:14px;padding:14px 18px;color:#6b6762;box-shadow:inset 0 0 0 1px #e7e4e0}'
           '#t{position:fixed;left:50%;bottom:20px;transform:translateX(-50%);background:#161514;color:#fff;padding:10px 16px;border-radius:99px;font-size:13px;opacity:0;transition:opacity .2s}'
           '@media(max-width:640px){.g{grid-template-columns:1fr}.ph{max-width:200px}}')
    js = ("<script>(function(){var t=document.getElementById('t');function tip(s){t.textContent=s;t.style.opacity=1;setTimeout(function(){t.style.opacity=0},1600)}"
          "function cp(html,plain){var d=document.createElement('div');d.contentEditable=true;d.style.position='fixed';d.style.left='-9999px';if(html)d.innerHTML=html;else d.textContent=plain;"
          "document.body.appendChild(d);var r=document.createRange();r.selectNodeContents(d);var s=getSelection();s.removeAllRanges();s.addRange(r);var ok=false;try{ok=document.execCommand('copy')}catch(e){}s.removeAllRanges();d.remove();return ok}"
          "document.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;if(b.dataset.copy!=null){if(navigator.clipboard)navigator.clipboard.writeText(b.dataset.copy).then(function(){tip('Texto copiado')},function(){cp(null,b.dataset.copy);tip('Texto copiado')});else{cp(null,b.dataset.copy);tip('Texto copiado')}}"
          "if(b.dataset.mail){var m=document.getElementById('m-'+b.dataset.mail);cp(m.innerHTML);tip('Correo copiado: pégalo en Gmail')}});"
          "var K='env404';var st={};try{st=JSON.parse(localStorage.getItem(K)||'{}')}catch(e){}"
          "document.querySelectorAll('input[data-k]').forEach(function(i){var c=i.closest('.c');i.checked=!!st[i.dataset.k];c.classList.toggle('done',i.checked);"
          "i.addEventListener('change',function(){st[i.dataset.k]=i.checked;c.classList.toggle('done',i.checked);try{localStorage.setItem(K,JSON.stringify(st))}catch(e){}})})})();</script>")
    tips = ('<div class="tips"><b>Cómo enviar</b><ol><li>WhatsApp: descarga la captura, abre WhatsApp (el texto va puesto), adjunta la captura y envía. A la mitad les toca la variante A (pide permiso) y a la otra mitad la B (enlace).</li>'
            '<li>Instagram: abre el mensaje, pega el texto y adjunta la captura. El enlace, cuando contesten.</li>'
            '<li>Correo: ya están los borradores en Gmail (hola@), con destinatario: solo abrir y enviar.</li>'
            '<li>Seguimiento: día 2 un recordatorio corto con un detalle suyo; día 4 llamada; día 7 Instagram; día 10 último mensaje.</li></ol></div>')
    def row(s):
        c = SHOPS[s]; d = D.get(s, {}); w = num(d); em = (d.get('email') or '').strip(); ig = d.get('handle') or c.get('handle')
        who = d.get('owner_first') or ''
        return (f'<tr><td><a href="#{s}">{E(c["name"])}</a>{(" · " + E(who)) if who else ""}{" ⚠️" if d.get("warn") else ""}</td>'
                f'<td>{("WhatsApp +" + w) if w else (("Llamar " + E(d.get("phone", ""))) if d.get("phone") else "—")}</td>'
                f'<td>{("Borrador → " + E(em)) if em else "—"}</td><td>@{E(ig)}</td></tr>')
    resumen = ('<div class="tips"><b>Resumen: ' + str(len(slugs)) + ' tiendas</b><table class="rs"><tr><th>Tienda</th><th>WhatsApp / teléfono</th><th>Correo</th><th>Instagram</th></tr>'
               + ''.join(row(s) for s in slugs) + '</table></div>')
    body = resumen + ''.join(card(k, s) for k, s in enumerate(slugs))
    if fuera: body += '<div class="pend"><b>Fuera del lote (no enviar):</b> ' + '; '.join(E(D.get(f, {}).get('name', f) + ': ' + D.get(f, {}).get('warn', '')) for f in fuera) + '</div>'
    if pend: body += '<div class="pend"><b>Pendientes de imágenes:</b> ' + ', '.join(E(p) for p in pend) + '</div>'
    out = (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Envíos de propuestas</title><style>{css}</style></head>'
           f'<body><div class="w"><h1>Envíos de propuestas</h1><p class="lead">{len(slugs)} tiendas listas.</p>{tips}{body}</div><div id="t"></div>{js}</body></html>')
    open(os.path.join(S, 'envios.html'), 'w').write(out); print('ok', len(slugs), len(out) // 1024, 'KB')


if __name__ == '__main__':
    a = sys.argv[1:]; pend = []
    fuera = []
    if '--fuera' in a: i = a.index('--fuera'); fuera = a[i + 1:]; a = a[:i]
    if '--pend' in a: i = a.index('--pend'); pend = a[i + 1:]; a = a[:i]
    main(a, pend, fuera)
