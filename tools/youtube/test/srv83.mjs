// serves tu-tienda.html and /l/tt (the real ttApply on a node:sqlite D1). Usage: node srv83.mjs <w83mod.mjs> <web dir> [port]
import http from 'node:http'; import fs from 'node:fs'; import path from 'node:path';
import { makeD1 } from './d1shim.mjs';
const { llPublic } = await import(process.argv[2]); const WEB = process.argv[3], PORT = Number(process.argv[4] || 8787);
const DB = makeD1(); DB._db.exec("CREATE TABLE docs (coll TEXT, id TEXT, data TEXT, updated INTEGER, PRIMARY KEY (coll, id)); CREATE TABLE meta (k TEXT PRIMARY KEY, v TEXT); CREATE TABLE push (ep TEXT, p256dh TEXT, auth TEXT);");
const env = { DB, DEV: 'http://localhost:' + PORT };
http.createServer(async (q, s) => {
  const u = new URL(q.url, 'http://x');
  if (u.pathname === '/__leads') { s.setHeader('content-type', 'application/json'); return s.end(JSON.stringify(DB._db.prepare("SELECT id, data FROM docs").all())); }
  if (u.pathname === '/l/tt') { let b = ''; for await (const c of q) b += c; const req = new Request('http://localhost' + q.url, { method: q.method, headers: q.headers, body: b }); const r = await llPublic(req, env, 'tt'); s.writeHead(r.status, { 'content-type': 'application/json' }); return s.end(await r.text()); }
  const f = path.join(WEB, u.pathname === '/tu-tienda' ? 'tu-tienda.html' : u.pathname);
  if (!fs.existsSync(f) || fs.statSync(f).isDirectory()) { s.writeHead(404); return s.end('404'); }
  s.writeHead(200, { 'content-type': f.endsWith('.html') ? 'text/html; charset=utf-8' : f.endsWith('.webp') ? 'image/webp' : 'application/octet-stream' }); s.end(fs.readFileSync(f));
}).listen(PORT, () => console.log('listo', PORT));
