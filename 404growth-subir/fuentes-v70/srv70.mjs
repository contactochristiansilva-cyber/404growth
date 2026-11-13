import http from 'node:http';
import fs from 'node:fs';
import { makeD1 } from './d1shim.mjs';
import { archApi } from './w70mod.mjs';
const env = { DB: makeD1() }, page = fs.readFileSync('admin70.html', 'utf8');
const FIN = { items: [], recs: [], inv: [], pays: [], curs: ['EUR'], cats: [] };
http.createServer(async (q, s) => {
  const u = new URL(q.url, 'http://x'); const chunks = []; for await (const c of q) chunks.push(c); const buf = Buffer.concat(chunks);
  if (u.pathname === '/admin') { s.writeHead(200, { 'content-type': 'text/html; charset=utf-8' }); s.end(page); return; }
  const p = u.pathname.replace('/admin/api/', '');
  if (/^arch|^archf/.test(p)) {
    const r = await archApi(new Request('http://x' + q.url, { method: q.method, headers: q.headers, body: ['GET', 'HEAD'].includes(q.method) ? undefined : buf }), env, p);
    const h = {}; r.headers.forEach((v, k) => h[k] = v); s.writeHead(r.status, h); s.end(Buffer.from(await r.arrayBuffer())); return;
  }
  s.writeHead(200, { 'content-type': 'application/json' });
  s.end(JSON.stringify(p === 'fin' ? FIN : p === 'me' ? { email: 'chris@x' } : {}));
}).listen(8770, () => console.log('ok'));
