import fs from 'node:fs';

const j = JSON.parse(fs.readFileSync('intenso-eq.json', 'utf8'));
globalThis.window = { INTENSO_EQ_URL: 'x' };
globalThis.fetch = async () => ({ json: async () => j, ok: true });
globalThis.window.crypto = globalThis.crypto; globalThis.document = { addEventListener() {}, querySelector() { return null; }, getElementById() { return null; } };
globalThis.location = { pathname: '/', search: '' }; globalThis.HTMLFormElement = class {};
eval(fs.readFileSync('intenso-eq.js', 'utf8'));
const qs = ['La vie est belle', 'perfume la vie est belle de lancome', 'Lancôme La Vie Est Belle', 'lavieestbelle', 'Sauvage', 'sauvage de dior', 'aventus creed', 'chanel nº5', 'one million paco rabanne', 'Light Blue', 'vainilla', 'oud', 'Nº 93', '93', 'ambar', 'dior', 'good girl carolina herrera', 'Terre d\'Hermès', 'black opium ysl', 'equivalencia invictus', 'tobacco vanille'];
for (const q of qs) console.log(JSON.stringify(q), '->', await window.intensoEq(q));
