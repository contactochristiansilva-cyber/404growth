# python3 patch_v79.py <worker v78c> <salida>
# 19/11/2026 · admin v79: los emails salen de un subdominio solo para enviar (m.404growth.com, verificado en Resend),
# con respuesta a hola@ y la baja con un clic (RFC 8058) en los comerciales.
#  - VSL_FROM = «Christian · 404 Growth <christian@m.404growth.com>» (confirmación, recordatorios, no-show, Talento).
#  - La newsletter y el informe semanal usan el remitente de Ajustes solo si es de m.404growth.com; si no, VSL_FROM.
#    Ya no hace falta rellenar «Remitente» para que salgan.
#  - reply_to hola@404growth.com también en la newsletter y en el informe semanal.
#  - Newsletter: cabecera List-Unsubscribe-Post y POST /nl/baja?t=<token> da de baja sin abrir la página.
import sys
src, out = sys.argv[1:3]
w = open(src, encoding='utf-8').read()


def rep(old, new, n=1):
    global w
    c = w.count(old)
    assert c == n, (c, old[:80])
    w = w.replace(old, new)


rep('const VSL_FROM = "Christian · 404 Growth <hola@404growth.com>", VSL_REPLY = "hola@404growth.com",',
    'const MAIL_DOMAIN = "m.404growth.com", VSL_FROM = "Christian · 404 Growth <christian@" + MAIL_DOMAIN + ">", VSL_REPLY = "hola@404growth.com",')
# el remitente de Ajustes solo vale si es del dominio verificado
k = w.index('const MAIL_DOMAIN = ')
k = w.index('\n', k) + 1
w = w[:k] + ('const mailFrom = (cf) => { const f = String((cf && cf.nlFrom) || "").trim(); '
             'return f && /@m\\.404growth\\.com>?$/i.test(f) ? f : VSL_FROM; };   // v79\n') + w[k:]

rep('if (!cfg.nlFrom) return bad("nofrom", 409); ', '')
rep('return { from: cfg.nlFrom, to: [s.email],', 'return { from: mailFrom(cfg), reply_to: VSL_REPLY, to: [s.email],')
rep('headers: { "List-Unsubscribe": "<" + u + ">" }',
    'headers: { "List-Unsubscribe": "<" + u + ">", "List-Unsubscribe-Post": "List-Unsubscribe=One-Click" }')
rep('if (!key || !cf.nlFrom) return { sent: false, why: "nomail" };', 'if (!key) return { sent: false, why: "nomail" };')
rep('body: JSON.stringify({ from: cf.nlFrom, to: [u.email],', 'body: JSON.stringify({ from: mailFrom(cf), reply_to: VSL_REPLY, to: [u.email],')
rep('out.mail = !!(await getMeta(env, "nl_key")) && !!cf.nlFrom;', 'out.mail = !!(await getMeta(env, "nl_key"));')
# baja con un clic: Gmail y Yahoo hacen POST a la dirección de List-Unsubscribe
rep('''    if (p === "api/unsubscribe" && req.method === "POST") return unsubscribe(req, env);
    if (req.method !== "GET") return bad("method", 405);''',
    '''    if (p === "api/unsubscribe" && req.method === "POST") return unsubscribe(req, env);
    if (p === "baja" && req.method === "POST") {   // v79: RFC 8058, one-click desde el cliente de correo
      const t = new URL(req.url).searchParams.get("t") || "";
      if (/^[A-Za-z0-9_-]{10,40}$/.test(t)) await env.DB.prepare("UPDATE subs SET status = 'out' WHERE token = ?1").bind(t).run();
      return new Response("", { status: 200 });
    }
    if (req.method !== "GET") return bad("method", 405);''')
rep('placeholder=\\"Christian · 404 Growth &lt;hola@404growth.com&gt;\\"', 'placeholder=\\"Christian · 404 Growth &lt;christian@m.404growth.com&gt;\\"')
open(out, 'w', encoding='utf-8').write(w)
print('ok')
