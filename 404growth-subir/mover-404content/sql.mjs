// 19/11/2026 · ayudante del traslado de 404 Content (mover-404content.command). Lee por la entrada lo que da wrangler con --json.
//   node sql.mjs tablas            → los nombres de las tablas p_* (separados por espacios)
//   node sql.mjs admins            → admins.sql: las tablas users y attempts vacías (el Worker las consulta) y los admins de Chris en p_admins
//   node sql.mjs dbid <nombre>     → el id de esa base D1 (de «d1 list --json»), o nada
//   node sql.mjs reseal            → resumen de lo que respondió /__reseal
import { readFileSync } from 'node:fs';
const raw = readFileSync(0, 'utf8');
const js = () => { const a = raw.indexOf('['), o = raw.indexOf('{'); const i = a < 0 ? o : o < 0 ? a : Math.min(a, o); const last = Math.max(raw.lastIndexOf(']'), raw.lastIndexOf('}')); return JSON.parse(raw.slice(i, last + 1)); };
const rows = (j) => (Array.isArray(j) ? j : [j]).flatMap((x) => (x && x.results) || []);
const q = (v) => v === null || v === undefined ? 'NULL' : typeof v === 'number' ? String(v) : "'" + String(v).replace(/'/g, "''") + "'";
const [mode, arg] = process.argv.slice(2);
if (mode === 'tablas') {
  console.log(rows(js()).map((r) => r.name).filter((n) => /^p_[a-z_]+$/.test(n) && n !== 'p_reseal').concat(['p_reseal']).join(' '));
} else if (mode === 'admins') {
  const out = [
    "CREATE TABLE IF NOT EXISTS users (id TEXT PRIMARY KEY, email TEXT NOT NULL, role TEXT NOT NULL DEFAULT 'admin', disabled INTEGER NOT NULL DEFAULT 0, salt TEXT, hash TEXT, iter INTEGER);",
    "CREATE TABLE IF NOT EXISTS attempts (k TEXT NOT NULL, ts INTEGER NOT NULL);",
  ];
  for (const u of rows(js())) {
    if (!u.email || !u.salt || !u.hash || !u.iter) continue;
    const id = 'pa_' + String(u.id).replace(/[^A-Za-z0-9_-]/g, '').slice(0, 24);
    out.push(`INSERT OR IGNORE INTO p_admins (id, email, salt, hash, iter, created, last_login, disabled, invited_by) VALUES (${q(id)}, ${q(u.email)}, ${q(u.salt)}, ${q(u.hash)}, ${q(Number(u.iter))}, ${q(Date.now())}, NULL, 0, 'traslado');`);
  }
  console.log(out.join('\n'));
} else if (mode === 'dbid') {
  const j = js(); const d = (Array.isArray(j) ? j : []).find((x) => x && x.name === arg);
  console.log(d ? (d.uuid || d.id || '') : '');
} else if (mode === 'reseal') {
  const j = js();
  console.log(`  ${j.cfg} claves (Stripe, Anthropic, Meta…) y ${j.conn} conexiones de Instagram y WhatsApp cifradas con la clave nueva.`);
  if (j.fail && j.fail.length) console.log(`  Ya estaban ilegibles con la clave vieja (no cambia nada): ${j.fail.join(', ')}`);
} else { console.error('modo desconocido'); process.exit(2); }
