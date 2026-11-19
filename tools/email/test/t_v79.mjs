// admin v79: remitente en m.404growth.com, respuesta a hola@ y baja con un clic.
import { makeD1 } from './d1shim.mjs';
import W, { sendMail, nlSend, mailFrom, VSL_FROM, VSL_REPLY, DDL, setMeta } from './w79mod.mjs';
let ok = 0, ko = 0; const t = (c, m) => { if (c) ok++; else { ko++; console.log('FALLO:', m); } };
const sent = [];
globalThis.fetch = async (url, o) => { sent.push({ url: String(url), body: JSON.parse(o.body) }); return new Response('{"id":"x"}', { status: 200 }); };
const env = { DB: makeD1(), MAILAPI: 'https://mock' }; for (const s of DDL) env.DB._db.exec(s); const db = env.DB._db;

t(VSL_FROM === 'Christian · 404 Growth <christian@m.404growth.com>', 'VSL_FROM en el subdominio');
t(VSL_REPLY === 'hola@404growth.com', 'respuesta a hola@');
t(mailFrom({}) === VSL_FROM, 'sin remitente en Ajustes, VSL_FROM');
t(mailFrom({ nlFrom: 'Christian · 404 Growth <hola@404growth.com>' }) === VSL_FROM, 'un remitente de otro dominio no se usa');
t(mailFrom({ nlFrom: 'Chris <chris@m.404growth.com>' }) === 'Chris <chris@m.404growth.com>', 'un remitente del subdominio sí');

// sin clave no sale nada
t((await sendMail(env, 'a@b.com', 's', '<p>h</p>', 'h')).why === 'nomail' && sent.length === 0, 'sin clave no envía');
await setMeta(env, 'nl_key', 're_test');
const r1 = await sendMail(env, 'ana@tienda.es', 'Tu llamada', '<p>h</p>', 'h');
t(r1.ok && sent.length === 1, 'con clave envía');
t(sent[0].url === 'https://mock/emails' && sent[0].body.from === VSL_FROM && sent[0].body.reply_to === VSL_REPLY, 'confirmación desde el subdominio con respuesta a hola@');

// newsletter: ya no pide remitente, lleva reply_to y la baja con un clic
await setMeta(env, 'cfg', JSON.stringify({ nlFooter: '404 Growth · Calle X' }));
db.prepare("INSERT INTO campaigns (id, subject, body, status, created) VALUES ('c1', 'Asunto', 'Cuerpo', 'draft', 1)").run();
db.prepare("INSERT INTO subs (id, email, status, token, created) VALUES ('s1', 'x@y.es', 'active', 'tok_abcdefghij12', 1)").run();
sent.length = 0;
const r2 = await nlSend(env, 'c1');
t(r2.status === 200 && sent.length === 1 && sent[0].url === 'https://mock/emails/batch', 'la newsletter sale sin «Remitente» en Ajustes');
const m = sent[0] && sent[0].body[0];
t(m && m.from === VSL_FROM && m.reply_to === VSL_REPLY, 'newsletter: remitente y respuesta');
t(m && m.headers['List-Unsubscribe'] === '<https://404growth.com/nl/baja?t=tok_abcdefghij12>', 'newsletter: List-Unsubscribe con su enlace');
t(m && m.headers['List-Unsubscribe-Post'] === 'List-Unsubscribe=One-Click', 'newsletter: baja con un clic');

// el POST de Gmail a la dirección de baja da de baja
const res = await W.fetch(new Request('https://404growth.com/nl/baja?t=tok_abcdefghij12', { method: 'POST', body: 'List-Unsubscribe=One-Click', headers: { 'content-type': 'application/x-www-form-urlencoded' } }), env, { waitUntil() {} });
t(res.status === 200, 'POST /nl/baja responde 200');
t(db.prepare("SELECT status FROM subs WHERE id = 's1'").get().status === 'out', 'el suscriptor queda de baja');
const res2 = await W.fetch(new Request('https://404growth.com/nl/baja?t=x', { method: 'POST' }), env, { waitUntil() {} });
t(res2.status === 200, 'un token raro no rompe nada');
const res3 = await W.fetch(new Request('https://404growth.com/nl/baja?t=tok_abcdefghij12'), env, { waitUntil() {} });
t(res3.status === 200, 'la página de baja (GET) sigue');
console.log(ok + ' bien, ' + ko + ' mal'); process.exit(ko ? 1 : 0);
