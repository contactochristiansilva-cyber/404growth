// Servidor de prueba de la v78: la página del brief (web/), su API pública /l/brief* y la vista Briefs del admin, sobre node:sqlite.
// Antes: w78mod.mjs (ver t_v78.mjs) y web/ con ../build.py. Uso: node srv78.mjs
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { makeD1 } from './d1shim.mjs';
import { makeR2 } from './r2.mjs';
globalThis.__push = [];
const { briefPublic, briefApi } = await import('./w78mod.mjs');
const env = { DB: makeD1(), DEV: 'http://localhost:8778', TV: makeR2() };
const view = fs.readFileSync(new URL('../brief_client.js', import.meta.url), 'utf8');
const admin = `<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>
:root{--bg:#F4F5F8;--surface:#fff;--surface-2:#F0F2F6;--ink:#1F232A;--mute:#667085;--line:#E1E5EC;--accent:#2F6BFF;--ok:#157F4F;--ok-soft:#E2F5EB;--warn:#9A6400;--warn-soft:#FBF0D9;--bad:#B4322F;--bad-soft:#FBE6E5}
*{box-sizing:border-box}body{margin:0;padding:16px;background:var(--bg);color:var(--ink);font:500 15px/1.5 -apple-system,system-ui,sans-serif}h2,h3,p{margin:0}
.btn{display:inline-flex;align-items:center;gap:7px;border:1px solid var(--line);background:var(--surface);border-radius:10px;padding:8px 13px;font-weight:700;font-size:13.5px;cursor:pointer;white-space:nowrap;color:var(--ink);text-decoration:none}.btn.pri{background:var(--accent);color:#fff;border-color:var(--accent)}.btn.sm{padding:6px 10px;font-size:12.5px}.btn.danger{color:var(--bad)}
.panel{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:18px;min-width:0}.hint{color:var(--mute);font-size:12.5px}.empty{color:var(--mute)}.head p{color:var(--mute);margin-top:4px}
#toast-b{position:fixed;bottom:12px;left:12px;background:#000;color:#fff;padding:4px 8px;border-radius:6px;font-size:12px}</style></head><body><div id="view"></div><div id="toast-b"></div><script>
(function(){'use strict';var $=function(s){return document.querySelector(s)};
var esc=function(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})};
function api(m,p,b){return fetch('/admin/api/'+p,{method:m,headers:{'content-type':'application/json','x-404':'1'},body:b===undefined?undefined:JSON.stringify(b)}).then(function(r){return r.json().then(function(j){if(!r.ok){var e=new Error(j.error);e.code=j.error;throw e}return j})})}
function toast(t){$('#toast-b').textContent=t}function fail(e){toast('error '+(e&&e.code))}
function show(){vBrief().then(function(h){$('#view').innerHTML=h})}
${view}
show();window.__BR=BR;})();</script></body></html>`;
const TYPES = { '.html': 'text/html; charset=utf-8', '.png': 'image/png', '.js': 'text/javascript', '.css': 'text/css' };
http.createServer(async (q, s) => {
  const u = new URL(q.url, 'http://localhost:8778'); const chunks = []; for await (const c of q) chunks.push(c); const buf = Buffer.concat(chunks);
  const mk = () => new Request('http://localhost:8778' + q.url, { method: q.method, headers: q.headers, body: ['GET', 'HEAD'].includes(q.method) ? undefined : buf });
  let r;
  if (u.pathname === '/l/brief' || u.pathname === '/l/briefup') r = await briefPublic(mk(), env, {}, u.pathname.slice(3));
  else if (u.pathname.startsWith('/admin/api/')) r = await briefApi(mk(), env, u.pathname.slice(11));
  else if (u.pathname === '/__push') { s.writeHead(200, { 'content-type': 'application/json' }); s.end(JSON.stringify(globalThis.__push)); return; }
  else if (u.pathname === '/admin/' || u.pathname === '/admin') { s.writeHead(200, { 'content-type': 'text/html; charset=utf-8' }); s.end(admin); return; }
  else {
    let f = path.join('web', decodeURIComponent(u.pathname)); if (f.endsWith('/')) f += 'index.html';
    if (fs.existsSync(f) && fs.statSync(f).isDirectory()) { s.writeHead(301, { location: u.pathname + '/' }); s.end(); return; }
    if (!fs.existsSync(f)) { s.writeHead(404); s.end('404'); return; }
    s.writeHead(200, { 'content-type': TYPES[path.extname(f)] || 'application/octet-stream' }); s.end(fs.readFileSync(f)); return;
  }
  const h = {}; r.headers.forEach((v, k) => { h[k] = v; }); s.writeHead(r.status, h); s.end(Buffer.from(await r.arrayBuffer()));
}).listen(8778, () => console.log('ok 8778'));
