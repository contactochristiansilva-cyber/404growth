// v82: avisos de la agenda de las propuestas (y el del vídeo de la v81). node t_v82.mjs
import { makeD1 } from './d1shim.mjs';
import { alertsRun, agText, AG_STEP, DDL, ACFG, PAGES } from './w82mod.mjs';
import { EV } from './v82mod.mjs';
let ok = 0, ko = 0; const t = (c, m) => { if (c) ok++; else { ko++; console.log('FALLO:', m); } };

t(Array.isArray(EV.ag), 'el contador acepta «ag»');
t(ACFG.agenda === 1 && ACFG.video === 1, 'interruptores agenda y vídeo encendidos');
t(/Ha elegido hora en la agenda: Martes/.test(agText(3, 'Martes, 24 de noviembre, 11:00')), 'texto del paso 3');
t(AG_STEP[4] === 'poner su nombre', 'pasos');
// the admin page scripts still compile
let bad = 0; for (const [k, html] of Object.entries(PAGES)) { if (typeof html !== 'string') continue;
  for (const m of html.matchAll(/<script(?![^>]*src)[^>]*>([\s\S]*?)<\/script>/g)) { try { new Function(m[1]); } catch (e) { bad++; console.log('script de', k, e.message); } } }
t(!bad, 'los scripts de las páginas del admin compilan');
t(Object.values(PAGES).some((h) => typeof h === 'string' && h.includes("case 'ag': return 'Agenda: '")), 'la ficha de la visita sabe leer «ag»');

const DB = makeD1(), VIS = makeD1(); const env = { DB, VIS };
for (const s of DDL) DB._db.exec(s);
const vdl = await import('./v82mod.mjs'); // DDL of the counter is not exported: build it here
VIS._db.exec("CREATE TABLE v (id INTEGER PRIMARY KEY AUTOINCREMENT, k TEXT NOT NULL, slug TEXT NOT NULL, ts INTEGER NOT NULL, vid TEXT NOT NULL, cc TEXT, dev TEXT, secs INTEGER NOT NULL DEFAULT 0, depth INTEGER NOT NULL DEFAULT 0, seen INTEGER, ex INTEGER, cv INTEGER, act INTEGER, sd INTEGER, ss TEXT, br TEXT, os TEXT, dv TEXT, scr TEXT, lang TEXT, tz TEXT, dk INTEGER, tch INTEGER, rg TEXT, ci TEXT, asn INTEGER, aso TEXT, ipv INTEGER, ref TEXT, nav TEXT, tc TEXT, tcc INTEGER, tcw TEXT, tcm TEXT, evn INTEGER)");
VIS._db.exec("CREATE TABLE c (id INTEGER PRIMARY KEY AUTOINCREMENT, k TEXT NOT NULL, ts INTEGER NOT NULL, t INTEGER NOT NULL DEFAULT 0, s TEXT, sh TEXT, w TEXT, h TEXT, x INTEGER, y INTEGER)");
VIS._db.exec("CREATE TABLE e (id INTEGER PRIMARY KEY AUTOINCREMENT, k TEXT NOT NULL, i TEXT NOT NULL, y TEXT NOT NULL, ver INTEGER NOT NULL DEFAULT 1, src TEXT NOT NULL DEFAULT 'web', ot INTEGER, rt INTEGER NOT NULL, t INTEGER NOT NULL DEFAULT 0, s TEXT, l TEXT, n INTEGER, m TEXT)");
VIS._db.exec("CREATE TABLE b (id INTEGER PRIMARY KEY AUTOINCREMENT, ts INTEGER NOT NULL, slug TEXT, tc TEXT, tcc INTEGER, ua TEXT, cc TEXT, aso TEXT)");
const now = Date.now(), M = 60000;
const visit = (k, slug, seen, tc) => VIS._db.prepare("INSERT INTO v (k, slug, ts, vid, dev, seen, tc) VALUES (?, ?, ?, 'x', 'm', ?, ?)").run(k, slug, seen - 5 * M, seen, tc || 'human_likely').lastInsertRowid;
const ev = (k, y, n, l, rt) => VIS._db.prepare("INSERT INTO e (k, i, y, rt, n, l) VALUES (?, ?, ?, ?, ?, ?)").run(k, Math.random().toString(36).slice(2, 10), y, rt || now, n == null ? null : n, l || null);
const v1 = visit('k1', 'sinu-and-son', now);                  // live: day and hour in the same pass → one alert, the hour
ev('k1', 'ag', 1, 'Reservar 30 min'); ev('k1', 'ag', 2, 'mar, 24 nov'); ev('k1', 'ag', 3, 'Martes, 24 de noviembre, 11:00'); ev('k1', 'vplay');
const v2 = visit('k2', 'amancia', now);                       // booked: no agenda alert (the booking has its own)
for (const n of [1, 2, 3, 4, 5, 6]) ev('k2', 'ag', n);
const v3 = visit('k3', 'tu-esencia', now - 25 * M);           // left half way 30 min ago
ev('k3', 'ag', 1, 'Reservar 30 min', now - 31 * M); ev('k3', 'ag', 2, 'mié, 25 nov', now - 30 * M);
const v4 = visit('k4', 'ria-pita', now);                      // failures
ev('k4', 'ag', 4); ev('k4', 'ag', 7, 'sin WhatsApp válido'); ev('k4', 'ag', 5); ev('k4', 'ag', 9, 'sin respuesta');
const v5 = visit('k5', 'robot', now, 'automation_likely');    // a robot: nothing
ev('k5', 'ag', 3, 'x');
DB._db.prepare("INSERT OR REPLACE INTO meta (k, v) VALUES ('al_c', '0')").run(); DB._db.prepare("INSERT OR REPLACE INTO meta (k, v) VALUES ('al_e', '0')").run();

await alertsRun(env);
const A = () => DB._db.prepare("SELECT dk, kind, body FROM palerts ORDER BY id").all();
let L = A(); const has = (dk) => L.find((a) => a.dk === dk);
t(has('v' + v1 + ':ag3') && !has('v' + v1 + ':ag1') && !has('v' + v1 + ':ag2'), 'visita 1: solo el paso más avanzado (hora): ' + JSON.stringify(L.map((a) => a.dk)));
t(has('v' + v1 + ':vplay'), 'visita 1: aviso del vídeo (v81)');
t(!L.some((a) => a.dk.startsWith('v' + v2 + ':')), 'visita 2 (reservada): sin avisos de agenda');
t(has('v' + v3 + ':ag2') && has('v' + v3 + ':agx') && /Llegó hasta: elegir día/.test(has('v' + v3 + ':agx').body), 'visita 3: a medias → «Se fue sin reservar»');
t(has('v' + v4 + ':ag7') && has('v' + v4 + ':ag9') && !has('v' + v4 + ':ag4'), 'visita 4: avisos de los fallos, no del nombre');
t(!L.some((a) => a.dk.startsWith('v' + v5 + ':')), 'robot: nada');
t(L.filter((a) => a.kind === 'agenda').every((a) => a.body && !/undefined/.test(a.body)), 'textos sin «undefined»');
// next pass: she goes on to her name → a new alert; nothing repeats
ev('k1', 'ag', 4); const n0 = L.length;
await alertsRun(env); L = A();
t(has('v' + v1 + ':ag4') && L.length === n0 + 1, 'siguiente pasada: un aviso nuevo (nombre) y nada repetido');
await alertsRun(env); t(A().length === L.length, 'tercera pasada: nada nuevo');
console.log(L.map((a) => a.dk + ' · ' + a.body).join('\n'));
console.log(`${ok} bien, ${ko} mal`); process.exit(ko ? 1 : 0);
