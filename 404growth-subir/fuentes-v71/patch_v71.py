#!/usr/bin/env python3
"""v71 · presupuesto aceptado → cobro pendiente en Facturación. Uso: patch_v71.py <worker.js> [salida]"""
import json, sys, os
src_path = sys.argv[1]; out_path = sys.argv[2] if len(sys.argv) > 2 else src_path
here = os.path.dirname(os.path.abspath(__file__))
s = open(src_path, encoding='utf-8').read()
assert 'quotesBillSweep' not in s, 'ya tiene la v71'

def rep(old, new, count=1):
    global s
    assert s.count(old) == count, (s.count(old), old[:90])
    s = s.replace(old, new)

server = open(os.path.join(here, 'qbill_server.js'), encoding='utf-8').read()
rep('async function quotesApi(req, env, p) {', server + 'async function quotesApi(req, env, p) {')

# GET: primero los aceptados que faltan en Facturación; luego, de cada uno, si su cobro está pendiente o cobrado
rep('''    const r = await DBq.prepare("SELECT id, data FROM docs WHERE coll = 'quotes'").all(), out = [];
    for (const x of r.results || []) { try { out.push(Object.assign(JSON.parse(x.data), { id: x.id })); } catch (e) {} }
    out.sort((a, b) => (b.created || 0) - (a.created || 0));
    return json({ quotes: out });''',
'''    await quotesBillSweep(env);
    const r = await DBq.prepare("SELECT id, data FROM docs WHERE coll = 'quotes'").all(), out = [];
    for (const x of r.results || []) { try { out.push(Object.assign(JSON.parse(x.data), { id: x.id })); } catch (e) {} }
    out.sort((a, b) => (b.created || 0) - (a.created || 0));
    const pids = out.filter((x) => x.status === "accepted" && x.bill && x.bill.pay).map((x) => x.bill.pay);
    if (pids.length) {
      const pm = {}; for (const y of (await DBq.prepare("SELECT id, paid FROM pay WHERE id IN (" + pids.map((_, i) => "?" + (i + 1)).join(", ") + ")").bind(...pids).all()).results || []) pm[y.id] = y.paid || "";
      for (const x of out) if (x.status === "accepted" && x.bill && x.bill.pay) x.billPaid = x.bill.pay in pm ? pm[x.bill.pay] : null;
    }
    return json({ quotes: out });''')

# POST: al aceptar entra en Facturación; al volver a pendiente o no aceptado se quita lo que no se había cobrado
rep('''    let d; try { d = JSON.parse(row.data); } catch (e) { d = {}; }
    const c = qClean(b, true); if (c.name === "") return bad("text"); Object.assign(d, c);
    if (b.status !== undefined) { if (!["pending", "accepted", "rejected"].includes(b.status)) return bad("status"); if (b.status !== d.status) { d.status = b.status; d.decided = b.status === "pending" ? null : now; } }
    await DBq.prepare("UPDATE docs SET data = ?1, updated = ?2 WHERE coll = 'quotes' AND id = ?3").bind(JSON.stringify(d), now, q[1]).run();
    return json({ ok: true });''',
'''    let d; try { d = JSON.parse(row.data); } catch (e) { d = {}; }
    const was = d.status, c = qClean(b, true); if (c.name === "") return bad("text"); Object.assign(d, c);
    if (b.status !== undefined) { if (!["pending", "accepted", "rejected"].includes(b.status)) return bad("status"); if (b.status !== d.status) { d.status = b.status; d.decided = b.status === "pending" ? null : now; } }
    let st = []; const res = { ok: true };
    if (d.status === "accepted") {
      const legacy = was === "accepted" && !d.bill ? !(await DBq.prepare("SELECT v FROM meta WHERE k = ?1").bind(QB_KEY).first()) : false;
      const x = await qBillSync(env, q[1], d, legacy); d.bill = x.bill; st = x.q; res.pay = !!x.bill.pay; res.plan = !!x.bill.plan;
    } else if (was === "accepted" && d.bill) { st = qBillUndo(env, d.bill); res.undone = !!(d.bill.payMade || d.bill.planMade); delete d.bill; }
    await DBq.batch(st.concat([DBq.prepare("UPDATE docs SET data = ?1, updated = ?2 WHERE coll = 'quotes' AND id = ?3").bind(JSON.stringify(d), now, q[1])]));
    if (res.plan) await plansRun(env);
    return json(res);''')

# Facturación: antes de enseñar los cobros, mete los presupuestos aceptados que falten
rep('''async function plansRun(env) {
  await payAddOnce(env);''', '''async function plansRun(env) {
  await payAddOnce(env); await quotesBillSweep(env);''')

# la página del admin
i = s.index('const PAGES = '); j = s.index('\n', i)
line = s[i:j]; pre = 'const PAGES = '; body = line[len(pre):]; semi = body.endswith(';')
pages = json.loads(body[:-1] if semi else body)
a = pages['admin']
def arep(old, new):
    global a
    assert a.count(old) == 1, (a.count(old), old[:90])
    a = a.replace(old, new)
arep("""api('POST','quotes/'+id,{status:k==='acc'?'accepted':k==='rej'?'rejected':'pending'}).then(function(){toast(k==='acc'?'Aceptado: lo tienes en «Aceptados»':k==='rej'?'Pasa a «No aceptados»':'Vuelve a pendientes');show()}""",
     """api('POST','quotes/'+id,{status:k==='acc'?'accepted':k==='rej'?'rejected':'pending'}).then(function(r){r=r||{};toast(k==='acc'?(r.pay||r.plan?'Aceptado: ya está en Facturación, pendiente de cobrar':'Aceptado: lo tienes en «Aceptados»'):(k==='rej'?'Pasa a «No aceptados»':'Vuelve a pendientes')+(r.undone?'. Quitado de Facturación lo que no estaba cobrado':''));show()}""")
arep("""function pqRow(q){var st=q.status||'pending',id=esc(q.id);""",
     """function pqBill(q){var b=q.bill||{},t=[];if(b.pay)t.push(q.billPaid===null?'El cobro ya no está en Facturación':q.billPaid?'Cobrado el '+esc(new Date(q.billPaid+'T00:00:00').toLocaleDateString('es-ES',{day:'numeric',month:'short'})):'<a href="#facturacion" data-sec="facturacion">En Facturación, pendiente de cobrar</a>');if(b.plan)t.push('<a href="#facturacion" data-sec="facturacion">Cuota mensual en Facturación</a>');return t.join(' · ')}
  function pqRow(q){var st=q.status||'pending',id=esc(q.id);""")
arep("""{day:'numeric',month:'short'})):'',/^https:\\/\\//.test(q.link||'')?'<a href="'+esc(q.link)+'" target="_blank" rel="noopener">Ver propuesta ↗</a>':''].filter(Boolean).join(' · ');""",
     """{day:'numeric',month:'short'})):'',st==='accepted'?pqBill(q):'',/^https:\\/\\//.test(q.link||'')?'<a href="'+esc(q.link)+'" target="_blank" rel="noopener">Ver propuesta ↗</a>':''].filter(Boolean).join(' · ');""")
pages['admin'] = a
s = s[:i] + pre + json.dumps(pages, ensure_ascii=False) + (';' if semi else '') + s[j:]
open(out_path, 'w', encoding='utf-8').write(s)
print('ok', out_path, len(s))
