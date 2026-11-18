import fs from 'node:fs';
const s = fs.readFileSync(process.argv[2], 'utf8');
const i = s.indexOf('const PAGES = '), j = s.indexOf('\n', i);
const P = JSON.parse(s.slice(i + 14, j).replace(/;$/, ''));
let n = 0, bad = 0;
for (const m of P.admin.matchAll(/<script(?![^>]*src)[^>]*>([\s\S]*?)<\/script>/g)) { n++; try { new Function(m[1]); } catch (e) { bad++; console.log('ERROR script', n, e.message); } }
const L = s.split('\n').find((l) => l.startsWith('const SHELL_JS = '));
try { const js = eval(L.slice('const SHELL_JS = '.length).replace(/;\s*$/, '')); new Function(js); console.log('shell ok', js.includes("['talento','Talento','hire'"), js.includes('Candidaturas y puestos')); } catch (e) { console.log('SHELL ERROR', e.message); }
console.log('admin scripts', n, 'bad', bad, 'vTal', P.admin.includes('function vTal('), P.admin.includes('talento:vTal'));
