import sys, io
src, out = sys.argv[1], sys.argv[2]
w = io.open(src, encoding="utf-8").read()
tt = io.open(__file__.replace("patch_v83.py", "tt_server.js"), encoding="utf-8").read()
if "async function ttApply(" in w:
    sys.exit("ya aplicado")
a = "async function llPublic(req, env, p) {"
assert w.count(a) == 1, "llPublic"
w = w.replace(a, tt + "\n" + a, 1)
b = '    if (p === "rs") return rsPost(req, env, b);'
assert w.count(b) == 1, "rs"
w = w.replace(b, b + '\n    if (p === "tt") return ttApply(req, env, b, now);                                     // v83: «Te preparo tu tienda» (YouTube)', 1)
io.open(out, "w", encoding="utf-8").write(w)
print("ok", len(w))
