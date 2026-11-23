// v83: «Te preparo tu tienda» → POST /l/tt → lead in the CRM. Usage: node t_v83.mjs <w83mod.mjs>
import { makeD1 } from './d1shim.mjs';
const mod = await import(process.argv[2]);
const { llPublic } = mod;
const DB = makeD1();
DB._db.exec(`CREATE TABLE docs (coll TEXT, id TEXT, data TEXT, updated INTEGER, PRIMARY KEY (coll, id));
CREATE TABLE meta (k TEXT PRIMARY KEY, v TEXT);
CREATE TABLE push (ep TEXT, p256dh TEXT, auth TEXT);`);
DB._db.prepare("INSERT INTO docs VALUES ('leads', 'mod-ya-esta', ?, 1)").run(JSON.stringify({ niche: 'moda', name: 'Ya Está Boutique', instagram: 'https://www.instagram.com/ya_esta_boutique/', phone: '+34600111222', stage: 'contacted', priority: 60, flags: [], notes: 'nota vieja', pageUrl: 'https://404growth.com/p/ya-esta/', order: 7 }));
const env = { DB };
let n = 0, bad = 0;
const ok = (c, m) => { n++; if (!c) { bad++; console.log('FALLA:', m); } else console.log('ok', m); };
let ip = 1;
const call = async (b, o = {}) => {
  const req = new Request('https://404growth.com/l/tt', { method: 'POST', headers: { origin: o.origin || 'https://404growth.com', 'content-type': 'application/json', 'cf-connecting-ip': o.ip || ('10.0.0.' + (ip++)) }, body: JSON.stringify(b) });
  const r = await llPublic(req, env, 'tt'); return [r.status, await r.json()];
};
const lead = (id) => { const r = DB._db.prepare("SELECT data FROM docs WHERE coll='leads' AND id=?").get(id); return r && JSON.parse(r.data); };
const all = () => DB._db.prepare("SELECT id, data FROM docs WHERE coll='leads'").all().map((r) => [r.id, JSON.parse(r.data)]);
const base = { name: 'Lucía', biz: 'Boutique Lucía Moda', ig: '@Lucia.Moda_', phone: '612 345 678', city: 'Jaén', sec: 'moda', web: 'web', ok: true, hp: '', utm: { utm_source: 'youtube', utm_medium: 'video', utm_campaign: 'tienes-web' } };

let [s, j] = await call(base);
ok(s === 200 && j.ok, 'alta nueva responde ok');
let L = all().filter(([id]) => id !== 'mod-ya-esta');
ok(L.length === 1, 'crea un lead');
const [nid, d] = L[0];
ok(/^mod-yt-boutique-lucia-moda-[a-z0-9]{2,4}$/.test(nid), 'id con prefijo del nicho: ' + nid);
ok(d.instagram === 'https://www.instagram.com/lucia.moda_/', 'Instagram normalizado');
ok(d.phone === '+34612345678' && d.whatsapp === '+34612345678' && d.waOk === true, 'móvil con +34 y WhatsApp');
ok(d.stage === 'new' && d.priority === 95 && d.flags.includes('pidio-tienda'), 'etapa, prioridad y marca');
ok(/^\d{4}-\d{2}-\d{2}$/.test(d.lotDay), 'lotDay de mañana');
ok(d.ttUtm.utm_source === 'youtube' && d.ttUtm.utm_campaign === 'tienes-web', 'guarda la UTM');
ok(/youtube · video · tienes-web/.test(d.notes) && /Tienen web pero no vende/.test(d.notes) && /Contacto: Lucía/.test(d.notes), 'nota con origen, web y contacto');
ok(d.order === 8, 'order al final');
ok(Number(DB._db.prepare("SELECT v FROM meta WHERE k='crm_rev'").get().v) >= 1, 'sube crm_rev');

[s, j] = await call(Object.assign({}, base, { biz: 'Ya Está', ig: 'https://instagram.com/ya_esta_boutique?igsh=x', phone: '699 999 999' }));
let y = lead('mod-ya-esta');
ok(s === 200 && all().length === 2, 'si ya está en el CRM no duplica');
ok(y.stage === 'contacted' && y.priority === 95 && y.flags.includes('pidio-tienda') && y.notes.startsWith('nota vieja\n') && y.whatsapp === '+34699999999', 'actualiza el que ya estaba');

[s, j] = await call(Object.assign({}, base, { ig: 'yaXesta', phone: '600 111 222' }));
ok(s === 200 && all().length === 2, 'reconoce también por el teléfono');

[s, j] = await call(Object.assign({}, base, { ig: 'ya%esta_boutique', phone: '611000000' }));
ok(s === 400, 'Instagram con caracteres raros se rechaza');

[s, j] = await call(Object.assign({}, base, { ok: false }));
ok(s === 400 && j.error === 'fields', 'sin aceptar la privacidad no entra');
[s, j] = await call(Object.assign({}, base, { phone: '123' }));
ok(s === 400, 'teléfono malo no entra');
[s, j] = await call(Object.assign({}, base, { hp: 'http://spam' }));
ok(s === 200 && all().length === 2, 'campo oculto relleno: responde ok pero no guarda');
[s, j] = await call(base, { origin: 'https://otra.com' });
ok(s === 403, 'otro origen: 403');

const n0 = all().length;
for (let i = 0; i < 3; i++) await call(Object.assign({}, base, { ig: 'robot' + i, phone: '62000000' + i, biz: 'Robot ' + i }), { ip: '9.9.9.9' });
[s, j] = await call(Object.assign({}, base, { ig: 'robot9', phone: '620000009', biz: 'Robot 9' }), { ip: '9.9.9.9' });
ok(all().length === n0 + 3 && s === 429, 'más de 3 por hora desde la misma conexión: 429');

[s, j] = await call(Object.assign({}, base, { ig: 'joyas.ana', phone: '0034655443322', biz: 'Joyas Ana', sec: 'joyeria', utm: {} }));
const ja = all().find(([id]) => id.startsWith('joy-yt-joyas-ana'));
ok(ja && ja[1].niche === 'joya' && ja[1].phone === '+34655443322' && /\(directo\)/.test(ja[1].notes), 'joyería sin UTM: nicho joya y origen directo');

console.log(`\n${n - bad}/${n} comprobaciones`);
process.exit(bad ? 1 : 0);
