# v84 (27/11/2026): «Facturado» de Contabilidad cuenta también cada cobro marcado como cobrado.
# Una factura (del generador o hecha fuera) que corresponde a un cobro (mismo cliente e importe) cuenta una sola vez.
import sys
src, out = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b):
    global s
    n = s.count(a)
    assert n == 1, (n, a[:80])
    s = s.replace(a, b)
# servidor: client_id en facturas y cobros
rep('"SELECT id, num, client, date, cur, total, data FROM invoices ORDER BY date DESC, created DESC LIMIT 3000"',
    '"SELECT id, num, client_id, client, date, cur, total, data FROM invoices ORDER BY date DESC, created DESC LIMIT 3000"')
rep('return { id: r.id, num: r.num, client: r.client, date: r.date, cur: r.cur, total: r.total, sub: s.sub, tax: s.tax };',
    'return { id: r.id, num: r.num, client_id: r.client_id, client: r.client, date: r.date, cur: r.cur, total: r.total, sub: s.sub, tax: s.tax };')
rep('"SELECT id, client, concept, amount, cur, due, paid FROM pay ORDER BY created DESC LIMIT 5000"',
    '"SELECT id, client_id, client, concept, amount, cur, due, paid FROM pay ORDER BY created DESC LIMIT 5000"')
# cliente: lista de lo facturado = facturas + cobros cobrados sin factura (IVA 21 % si no hay factura)
FAC = ("/* v84: lo facturado = las facturas (generador y hechas fuera) y cada cobro ya cobrado que no tenga su factura (mismo cliente e importe); sin factura se calcula con IVA del 21 % */\\n"
 "  function cbFac(d,cur){var used={},L=[],nm=function(t){return String(t||'').toLowerCase().normalize('NFD').replace(/[^a-z0-9]/g,'')},"
 "P=d.pays.filter(function(p){return p.cur===cur&&p.paid});"
 "var take=function(cl,who,tot){for(var i=0;i<P.length;i++){var p=P[i];if(!used[p.id]&&p.amount===tot&&((cl&&p.client_id===cl)||(who&&nm(p.client)===nm(who)))){used[p.id]=1;return p}}return null};"
 "d.inv.forEach(function(x){if(x.cur!==cur)return;take(x.client_id,x.client,x.total);L.push({date:x.date,total:x.total,sub:x.sub,tax:x.tax})});"
 "d.items.forEach(function(x){if(x.cur!==cur||x.kind!=='in')return;var b=cbBase(x);take('',x.who,x.total);L.push({date:x.date,total:x.total,sub:b,tax:x.total-b})});"
 "P.forEach(function(p){if(used[p.id])return;var b=Math.round(p.amount*100/121);L.push({date:p.paid,total:p.amount,sub:b,tax:p.amount-b,pay:1})});return L}\\n"
 "  function cbCalc(d,cur,R,today){")
rep("  function cbCalc(d,cur,R,today){", "  " + FAC)
rep("var G=d.inv.filter(function(x){return x.cur===cur&&cbIn(x.date,R)}),ing=s(paid,am)",
    "var G=cbFac(d,cur).filter(function(x){return cbIn(x.date,R)}),ing=s(paid,am)")
rep("fac:s(G,tt)+s(inU,tt),facB:s(G,function(x){return x.sub})+s(inU,cbBase),nFac:G.length+inU.length",
    "fac:s(G,tt),facB:s(G,function(x){return x.sub}),nFac:G.length")
rep("d.inv.forEach(function(x){if(x.cur===cur&&cbIn(x.date,Q))rep+=x.tax});d.items.forEach(function(x){if(x.cur!==cur||!cbIn(x.date,Q))return;var t=x.total-cbBase(x);if(x.kind==='in')rep+=t;else sop+=t})",
    "cbFac(d,cur).forEach(function(x){if(cbIn(x.date,Q))rep+=x.tax});d.items.forEach(function(x){if(x.cur!==cur||x.kind!=='out'||!cbIn(x.date,Q))return;sop+=x.total-cbBase(x)})")
open(out, 'w', encoding='utf-8').write(s)
print('ok')
