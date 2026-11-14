// Servidor de prueba de la vista Entregables (v72): la vista sola (dv_client.js) con la API de verdad (delivApi) sobre node:sqlite.
// Uso: node srv72.mjs  (antes: cp ../admin/worker.js w72mod.mjs && echo "export { delivApi, DDL };" >> w72mod.mjs)
import http from 'node:http';
import fs from 'node:fs';
import { makeD1 } from './d1shim.mjs';
import { delivApi, DDL } from './w72mod.mjs';
const env = { DB: makeD1() };
for (const s of DDL) env.DB._db.exec(s);
const ymd = (d) => d.toISOString().slice(0, 10), add = (n) => ymd(new Date(Date.now() + n * 864e5));
env.DB._db.prepare("INSERT INTO clients (id, name, created, start_date, archived) VALUES ('c_AAA111','Cliente Uno',1,?,0),('c_BBB222','Cliente Dos',2,?,0),('c_CCC333','Cliente Tres',3,?,0),('c_DDD444','Cliente Cuatro',4,'',0),('c_EEE555','Cliente Archivado',5,'',1)").run(add(-3), add(-20), add(-10));
const put = (id, d) => env.DB._db.prepare("INSERT INTO docs (coll,id,data,updated) VALUES ('deliv',?,?,1)").run(id, JSON.stringify(d));
put('c_BBB222', { at: add(-1) + 'T20:00', note: 'nota dos' });
put('c_CCC333', { at: add(1) + 'T23:59', note: 'nota tres' });
const view = fs.readFileSync(new URL('./dv_client.js', import.meta.url), 'utf8');
const page = `<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>
:root{--bg:#F4F5F8;--surface:#fff;--surface-2:#F0F2F6;--ink:#1F232A;--mute:#667085;--line:#E1E5EC;--accent:#2F6BFF;--accent-ink:#fff;--ok:#157F4F;--ok-soft:#E2F5EB;--warn:#9A6400;--warn-soft:#FBF0D9;--bad:#B4322F;--bad-soft:#FBE6E5}
*{box-sizing:border-box}body{margin:0;padding:16px;background:var(--bg);color:var(--ink);font:500 15px/1.5 system-ui,sans-serif}h2,h3,p{margin:0}
.btn{display:inline-flex;align-items:center;gap:7px;border:1px solid var(--line);background:var(--surface);border-radius:10px;padding:8px 13px;font-weight:700;font-size:13.5px;cursor:pointer;white-space:nowrap}.btn.pri{background:var(--accent);color:#fff;border-color:var(--accent)}.btn.sm{padding:6px 10px;font-size:12.5px}.btn.danger{color:var(--bad)}
.panel{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:18px;min-width:0}.chip{font-size:11.5px;font-weight:700;padding:2px 8px;border-radius:99px;background:var(--surface-2)}.hint{color:var(--mute);font-size:12.5px}
.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:12px 0}.kpi{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:12px}.kpi small{display:block;color:var(--mute)}.kpi b{font-size:22px}.head{margin-bottom:8px}
@media (max-width:600px){.kpis{grid-template-columns:1fr 1fr}}</style></head><body><div id="view"></div><div id="toast-b"></div><script>
(function(){'use strict';var $=function(s){return document.querySelector(s)};
var esc=function(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})};
function api(m,p,b){return fetch('/admin/api/'+p,{method:m,headers:{'content-type':'application/json'},body:b===undefined?undefined:JSON.stringify(b)}).then(function(r){return r.json().then(function(j){if(!r.ok){var e=new Error(j.error);e.code=j.error;throw e}return j})})}
function toast(t){$('#toast-b').textContent=t}function fail(e){toast('error '+(e&&e.code))}
function show(){vEnt().then(function(h){$('#view').innerHTML=h})}
${view}
show();})();</script></body></html>`;
http.createServer(async (q, s) => {
  const u = new URL(q.url, 'http://x'); const chunks = []; for await (const c of q) chunks.push(c); const buf = Buffer.concat(chunks);
  if (u.pathname === '/') { s.writeHead(200, { 'content-type': 'text/html; charset=utf-8' }); s.end(page); return; }
  const p = u.pathname.replace('/admin/api/', '');
  const r = await delivApi(new Request('http://x' + q.url, { method: q.method, headers: q.headers, body: ['GET', 'HEAD'].includes(q.method) ? undefined : buf }), env, p);
  s.writeHead(r.status, { 'content-type': 'application/json' }); s.end(Buffer.from(await r.arrayBuffer()));
}).listen(8772, () => console.log('ok'));
