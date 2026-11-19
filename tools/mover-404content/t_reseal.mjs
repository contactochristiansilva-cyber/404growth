// traslado de 404 Content: lo cifrado con la clave vieja se vuelve a cifrar con la nueva y el Worker nuevo lo lee.
import { createHash } from 'node:crypto';
import { readFileSync } from 'node:fs';
import { makeD1 } from './d1shim.mjs';
const OLD = await import('./wv.mjs');
const NEW = await import('./wn.mjs');
let ok = 0, ko = 0; const t = (c, m) => { if (c) ok++; else { ko++; console.log('FALLO:', m); } };
const DB = makeD1(); for (const s of OLD.DDL) DB._db.exec(s);
const envOld = { DB, P404_KEY: 'clave-vieja-123', P404_KEY_NEW: 'clave-nueva-456' };
const ctx = { waitUntil() {} };
// datos cifrados con la clave vieja
DB._db.prepare("INSERT INTO p_cfg (k, v) VALUES (?, ?)").run('stripe_sk', await OLD.seal(envOld, 'sk_live_abc'));
DB._db.prepare("INSERT INTO p_cfg (k, v) VALUES (?, ?)").run('anthropic', await OLD.seal(envOld, 'sk-ant-xyz'));
DB._db.prepare("INSERT INTO p_cfg (k, v) VALUES (?, ?)").run('plano', 'p0:hola');
DB._db.prepare("INSERT INTO p_cfg (k, v) VALUES (?, ?)").run('normal', '{"a":1}');
DB._db.prepare("INSERT INTO p_cfg (k, v) VALUES (?, ?)").run('roto', 'e1:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA');
const conn = (tid, kind, tok) => DB._db.prepare("INSERT INTO p_conn (tenant_id, kind, ext, token, created) VALUES (?, ?, ?, ?, 1)").run(tid, kind, 'x' + tid, tok);
conn('t1', 'ig', await OLD.seal(envOld, 'IGQ-token-1'));
conn('t1', 'wa', await OLD.seal(envOld, 'EAA-token-2'));
conn('t2', 'ig', await OLD.seal(envOld, 'IGQ-token-3'));
const before = DB._db.prepare("SELECT k, v FROM p_cfg ORDER BY k").all().map((r) => r.k + '=' + r.v).join('|');

const call = (h) => OLD.route(new Request('https://app.404growth.com/__reseal', { method: 'POST', headers: h || {} }), envOld, ctx);
t((await call()).status === 404, 'sin cabecera, 404');
t((await call({ 'x-p404-reseal': 'mal' })).status === 404, 'cabecera mala, 404');
const r0 = await OLD.route(new Request('https://app.404growth.com/__reseal', { method: 'POST' }), { DB, P404_KEY: 'clave-vieja-123' }, ctx);
t(r0.status !== 200, 'sin P404_KEY_NEW no hace nada');
const hdr = createHash('sha256').update('clave-nueva-456').digest('hex');
const r = await call({ 'x-p404-reseal': hdr }); const j = await r.json();
t(r.status === 200 && j.ok, 'con la cabecera buena responde');
t(j.cfg === 2 && j.conn === 3, 'vuelve a cifrar 2 claves y 3 conexiones: ' + JSON.stringify(j));
t(j.fail.length === 1 && j.fail[0] === 'cfg:roto', 'lo que ya estaba roto sale en fail');
const after = DB._db.prepare("SELECT k, v FROM p_cfg ORDER BY k").all().map((r) => r.k + '=' + r.v).join('|');
t(before === after, 'no toca lo que usa el Worker viejo');
t((await OLD.unseal(envOld, DB._db.prepare("SELECT v FROM p_cfg WHERE k='stripe_sk'").get().v)) === 'sk_live_abc', 'el viejo sigue leyendo sus claves');

// lo que hace el script en la base nueva
DB._db.exec(readFileSync('/home/claude/404growth/tools/mover-404content/aplicar.sql', 'utf8'));
t(!DB._db.prepare("SELECT name FROM sqlite_master WHERE name='p_reseal'").get(), 'p_reseal se borra');
const envNew = { DB, P404_KEY: 'clave-nueva-456' };
const g = (k) => DB._db.prepare("SELECT v FROM p_cfg WHERE k=?").get(k).v;
t((await NEW.unseal(envNew, g('stripe_sk'))) === 'sk_live_abc', 'el nuevo lee la clave de Stripe');
t((await NEW.unseal(envNew, g('anthropic'))) === 'sk-ant-xyz', 'el nuevo lee la de Anthropic');
t((await NEW.unseal(envNew, g('plano'))) === 'hola' && g('normal') === '{"a":1}', 'lo que no iba cifrado sigue igual');
const tk = (tid, kind) => DB._db.prepare("SELECT token FROM p_conn WHERE tenant_id=? AND kind=?").get(tid, kind).token;
t((await NEW.unseal(envNew, tk('t1', 'ig'))) === 'IGQ-token-1' && (await NEW.unseal(envNew, tk('t1', 'wa'))) === 'EAA-token-2' && (await NEW.unseal(envNew, tk('t2', 'ig'))) === 'IGQ-token-3', 'el nuevo lee los tokens de cada cliente');
t((await NEW.unseal(envNew, g('roto'))) === '', 'lo roto sigue roto (no inventa nada)');
console.log(ok + ' bien, ' + ko + ' mal'); process.exit(ko ? 1 : 0);
