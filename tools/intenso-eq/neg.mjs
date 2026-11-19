import fs from 'node:fs';
const j = JSON.parse(fs.readFileSync('intenso-eq.json', 'utf8'));
globalThis.window = { INTENSO_EQ_URL: 'x' }; window.crypto = globalThis.crypto;
globalThis.fetch = async () => ({ json: async () => j, ok: true });
globalThis.document = { addEventListener() {}, querySelector() { return null; }, getElementById() { return null; } };
globalThis.location = { pathname: '/', search: '' }; globalThis.HTMLFormElement = class {};
eval(fs.readFileSync('intenso-eq.js', 'utf8'));
const neg = JSON.parse(fs.readFileSync('neg.json', 'utf8')); const hit = [];
for (const q of neg) { const r = await window.intensoEq(q); if (r) hit.push([q, r]); }
console.log(neg.length, 'búsquedas de notas/familias; coinciden con un perfume:', hit.length, JSON.stringify(hit.slice(0, 30)));
