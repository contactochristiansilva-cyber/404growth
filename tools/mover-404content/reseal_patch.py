# python3 reseal_patch.py <partner/worker.js> <salida>
# 19/11/2026 · traslado de 404 Content a la cuenta de Cloudflare de Javier.
# Añade al Worker viejo (cuenta de Chris) la ruta POST /__reseal: vuelve a cifrar con la clave nueva (secreto P404_KEY_NEW, la que
# tendrá el Worker en la cuenta de Javier) todo lo que está cifrado con P404_KEY: las claves de p_cfg (Stripe, Anthropic, Meta…)
# y los tokens de p_conn (Instagram y WhatsApp de cada cliente). Lo escribe en p_reseal, sin tocar lo que usa este Worker; el script
# del traslado copia p_reseal a la base nueva y lo aplica allí. Así nadie tiene que volver a conectar nada.
# Solo responde si la cabecera x-p404-reseal es el SHA-256 (hex) de P404_KEY_NEW.
import sys
src, out = sys.argv[1:3]
w = open(src, encoding='utf-8').read()

FN = r'''
/* 19 nov 2026: traslado a la cuenta de Javier. Lo cifrado con P404_KEY, otra vez cifrado con P404_KEY_NEW, en p_reseal (ver reseal_patch.py). */
async function reseal(req, env) {
  const hex = (u8) => Array.from(u8).map((x) => x.toString(16).padStart(2, "0")).join("");
  const want = hex(new Uint8Array(await crypto.subtle.digest("SHA-256", enc.encode(env.P404_KEY_NEW))));
  if ((req.headers.get("x-p404-reseal") || "") !== want) return new Response("", { status: 404 });
  const nk = await crypto.subtle.importKey("raw", new Uint8Array(await crypto.subtle.digest("SHA-256", enc.encode("p404-seal|" + env.P404_KEY_NEW))), "AES-GCM", false, ["encrypt", "decrypt"]);
  const seal2 = async (t) => { const iv = rand(12), ct = new Uint8Array(await crypto.subtle.encrypt({ name: "AES-GCM", iv }, nk, enc.encode(t))); const all = new Uint8Array(12 + ct.length); all.set(iv); all.set(ct, 12); return "e1:" + b64(all); };
  const open2 = async (s) => { const all = unb64(s.slice(3)); return new TextDecoder().decode(await crypto.subtle.decrypt({ name: "AES-GCM", iv: all.slice(0, 12) }, nk, all.slice(12))); };
  await env.DB.prepare("CREATE TABLE IF NOT EXISTS p_reseal (t TEXT NOT NULL, a TEXT NOT NULL, b TEXT NOT NULL, v TEXT NOT NULL, PRIMARY KEY (t, a, b))").run();
  await env.DB.prepare("DELETE FROM p_reseal").run();
  const ins = [], fail = []; let cfg = 0, conn = 0;
  const one = async (t, a, b, old) => {
    const p = await unseal(env, old);
    if (!p) { fail.push(t + ":" + a + (b ? "/" + b : "")); return false; }
    const v = await seal2(p);
    if ((await open2(v)) !== p) { fail.push(t + ":" + a + " (comprobación)"); return false; }
    ins.push(env.DB.prepare("INSERT INTO p_reseal (t, a, b, v) VALUES (?1, ?2, ?3, ?4)").bind(t, a, b, v));
    return true;
  };
  for (const r of (await env.DB.prepare("SELECT k, v FROM p_cfg WHERE v LIKE 'e1:%'").all()).results || []) if (await one("cfg", r.k, "", r.v)) cfg++;
  for (const r of (await env.DB.prepare("SELECT tenant_id, kind, token FROM p_conn WHERE token LIKE 'e1:%'").all()).results || []) if (await one("conn", r.tenant_id, r.kind, r.token)) conn++;
  for (let i = 0; i < ins.length; i += 50) await env.DB.batch(ins.slice(i, i + 50));
  return json({ ok: true, cfg, conn, fail });
}
'''
k = w.index('async function route(req, env, ctx) {')
assert w.count('async function route(req, env, ctx) {') == 1
w = w[:k] + FN.lstrip('\n') + w[k:]
old = 'async function route(req, env, ctx) {\n  const url = new URL(req.url), path = url.pathname, M = req.method;\n'
assert w.count(old) == 1, 'route head'
w = w.replace(old, old + '  if (path === "/__reseal" && M === "POST" && env.P404_KEY_NEW) return reseal(req, env);   // 19 nov 2026: traslado\n')
open(out, 'w', encoding='utf-8').write(w)
print('ok')
