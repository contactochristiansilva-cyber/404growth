// Servidor de prueba de la v77: las páginas de /equipo (web/), la API pública /l/job* y la vista Talento del admin con su API, sobre node:sqlite.
// Antes: cp <worker v77> w77mod.mjs && echo "export { talPublic, talApi, talReady, DDL, TAL };" >> w77mod.mjs ; python3 ../build.py web
// Uso: node srv77.mjs  (antes: w77mod.mjs y web/ hechos con build.py)
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { makeD1 } from './d1shim.mjs';
import { makeR2 } from './r2mock.mjs';
const real = globalThis.fetch;
globalThis.fetch = async (url, o) => {
  const u = String(url);
  if (u.startsWith('https://api.anthropic.com/')) {
    const b = JSON.parse(o.body), ids = b.tools[0].input_schema.properties.scores.items.properties.id.enum, txt = b.messages[0].content;
    const base = txt.length > 1800 ? 4 : txt.length > 1200 ? 3 : 2;
    return new Response(JSON.stringify({ content: [{ type: 'tool_use', name: 'puntuar', input: { scores: ids.map((id, k) => ({ id, score: Math.max(0, Math.min(5, base + (k % 2 ? 1 : 0) - (k === ids.length - 1 ? 1 : 0))), why: 'Explica con ejemplos concretos lo que hizo en cada proyecto y cómo lo midió.' })), summary: 'Perfil con experiencia real y buena escritura; falta ver más resultados medibles.', strengths: ['Tiendas reales en su portfolio', 'Usa IA con un flujo concreto'], risks: ['No da cifras de ventas'], rec: base >= 3 ? 'avanzar' : 'dudoso', questions: ['¿Qué tienda te costó más y por qué?', '¿Cómo organizas 15 días con tres tiendas a la vez?'] } }] }), { status: 200 });
  }
  if (u.includes('/emails')) return new Response('{}', { status: 200 });
  return real(url, o);
};
const { talPublic, talApi, DDL } = await import('./w77mod.mjs');
const env = { DB: makeD1(), DEV: 'http://localhost:8777' };
if (process.env.NOVID !== '1') env.TV = makeR2();   // el R2 de mentira (v77f); NOVID=1 para probar sin R2
for (const s of DDL) env.DB._db.exec(s);
env.DB._db.prepare("INSERT INTO meta (k, v) VALUES ('soc_cfg', ?)").run(JSON.stringify({ aiKey: 'k' }));
const view = fs.readFileSync(new URL('../tal_client.js', import.meta.url), 'utf8');
const admin = `<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>
:root{--bg:#F4F5F8;--surface:#fff;--surface-2:#F0F2F6;--ink:#1F232A;--mute:#667085;--line:#E1E5EC;--accent:#2F6BFF;--accent-ink:#fff;--accent-soft:#E8EFFF;--ok:#157F4F;--ok-soft:#E2F5EB;--warn:#9A6400;--warn-soft:#FBF0D9;--bad:#B4322F;--bad-soft:#FBE6E5}
*{box-sizing:border-box}body{margin:0;padding:16px;background:var(--bg);color:var(--ink);font:500 15px/1.5 -apple-system,system-ui,sans-serif}h2,h3,p{margin:0}
.btn{display:inline-flex;align-items:center;gap:7px;border:1px solid var(--line);background:var(--surface);border-radius:10px;padding:8px 13px;font-weight:700;font-size:13.5px;cursor:pointer;white-space:nowrap;color:var(--ink);text-decoration:none}.btn.pri{background:var(--accent);color:#fff;border-color:var(--accent)}.btn.sm{padding:6px 10px;font-size:12.5px}.btn.danger{color:var(--bad)}
.panel{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:18px;min-width:0}.chip{font-size:11.5px;font-weight:700;padding:2px 8px;border-radius:99px;background:var(--surface-2)}.hint{color:var(--mute);font-size:12.5px}.empty{color:var(--mute)}
.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:12px 0}.kpi{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:12px}.kpi small{display:block;color:var(--mute)}.kpi b{font-size:22px}.head{margin-bottom:8px}.head p{color:var(--mute);margin-top:4px}
@media (max-width:600px){.kpis{grid-template-columns:1fr 1fr}}#toast-b{position:fixed;bottom:12px;left:12px;background:#000;color:#fff;padding:4px 8px;border-radius:6px;font-size:12px}</style></head><body><div id="view"></div><div id="toast-b"></div><script>
(function(){'use strict';var $=function(s){return document.querySelector(s)};
var esc=function(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})};
function api(m,p,b){return fetch('/admin/api/'+p,{method:m,headers:{'content-type':'application/json','x-404':'1'},body:b===undefined?undefined:JSON.stringify(b)}).then(function(r){return r.json().then(function(j){if(!r.ok){var e=new Error(j.error);e.code=j.error;throw e}return j})})}
function toast(t){$('#toast-b').textContent=t}function fail(e){toast('error '+(e&&e.code))}
function show(){vTal().then(function(h){$('#view').innerHTML=h})}
${view}
show();window.__TL=TL;})();</script></body></html>`;
const TYPES = { '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'text/javascript', '.jpg': 'image/jpeg', '.svg': 'image/svg+xml', '.xml': 'application/xml' };
http.createServer(async (q, s) => {
  const u = new URL(q.url, 'http://localhost:8777'); const chunks = []; for await (const c of q) chunks.push(c); const buf = Buffer.concat(chunks);
  const mk = () => new Request('http://localhost:8777' + q.url, { method: q.method, headers: Object.assign({}, q.headers, { 'cf-connecting-ip': '9.9.9.' + (q.headers['x-ip'] || '1') }), body: ['GET', 'HEAD'].includes(q.method) ? undefined : buf });
  let r;
  if (/^\/l\/job(?:s|cv|t|ts|m|mb|v|vp)?$/.test(u.pathname)) r = await talPublic(mk(), env, {}, u.pathname.slice(3));
  else if (u.pathname.startsWith('/admin/api/')) r = await talApi(mk(), env, u.pathname.slice(11), {});
  else if (u.pathname === '/admin/' || u.pathname === '/admin') { s.writeHead(200, { 'content-type': 'text/html; charset=utf-8' }); s.end(admin); return; }
  else {
    let f = path.join('web', decodeURIComponent(u.pathname)); if (f.endsWith('/')) f += 'index.html';
    if (fs.existsSync(f) && fs.statSync(f).isDirectory()) { s.writeHead(301, { location: u.pathname + '/' }); s.end(); return; }
    if (!fs.existsSync(f)) { s.writeHead(404); s.end('404'); return; }
    s.writeHead(200, { 'content-type': TYPES[path.extname(f)] || 'application/octet-stream' }); s.end(fs.readFileSync(f)); return;
  }
  const h = {}; r.headers.forEach((v, k) => { h[k] = v; }); s.writeHead(r.status, h); s.end(Buffer.from(await r.arrayBuffer()));
}).listen(8777, () => console.log('ok 8777'));
