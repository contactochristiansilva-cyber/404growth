import fs from 'node:fs';
const j = JSON.parse(fs.readFileSync('intenso-eqn.json', 'utf8'));
globalThis.window = { INTENSO_EQ_URL: 'x' };
globalThis.fetch = async () => ({ json: async () => j, ok: true });
globalThis.document = { addEventListener() {}, querySelector() { return null; }, getElementById() { return null; }, querySelectorAll() { return []; } };
globalThis.location = { pathname: '/', search: '' }; globalThis.HTMLFormElement = class {};
eval(fs.readFileSync('intenso-eq2.js', 'utf8'));
const show = (r) => r.map((x) => x.t === 'b' ? `[${x.b.n}]` : `${x.p.n} (${x.p.b.n})`).join(' | ');
for (const q of ['la', 'lan', 'lanc', 'lancome', 'lancme', 'lancome la', 'xer', 'xerj', 'jerjof', 'zerjoff', 'la vie', 'lavie', 'sauv', 'savage', 'vain', 'acqua di g', 'one mill', 'dolce', 'ysl', 'aventu', 'carolina', 'good gi', 'tom fo', 'tobaco vanile', 'hermes', 'kurkd', 'bacarat', 'baccarat', '93', 'nº 9'])
  console.log(q.padEnd(14), '->', show(await window.intensoSug(q)));
for (const q of ['La vie est belle', 'lancome la vie est belle', 'sauvage de dior', 'aventus', 'one million', 'chanel nº5', 'vainilla', 'dior', 'oud'])
  console.log('EXACT', q.padEnd(26), '->', await window.intensoEq(q));
