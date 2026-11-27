import fs from 'fs';
const code=fs.readFileSync('client_fns.js','utf8');
const f=new Function(code+';return {cbFac,cbCalc,cbIva};')();
let ok=0,bad=0;const eq=(a,b,m)=>{if(JSON.stringify(a)===JSON.stringify(b)){ok++}else{bad++;console.log('FALLA',m,a,b)}};
const d={items:[],recs:[],inv:[{id:'f1',num:'2026-151',client_id:'c_kol',client:'KOL 2025 SL',date:'2026-11-09',cur:'EUR',total:114000,sub:94215,tax:19785}],
pays:[{id:'p_of',client_id:'c_of',client:'Open Fit',amount:205000,cur:'EUR',due:'2026-12-04',paid:''},
{id:'p_in',client_id:'',client:'Intenso Fragancias',amount:144000,cur:'EUR',due:'2026-11-11',paid:'2026-11-13'},
{id:'p_kol',client_id:'c_kol',client:'Kiss of Life',amount:114000,cur:'EUR',due:'2026-11-09',paid:'2026-11-10'},
{id:'p_mi',client_id:'c_mi',client:'Miguel Ángel Fernández',amount:27000,cur:'EUR',due:'2026-10-26',paid:'2026-10-26'}]};
const N={from:'2026-11-01',to:'2026-11-31'},O={from:'2026-10-01',to:'2026-10-31'};
let c=f.cbCalc(d,'EUR',N,'2026-11-27');
eq(c.fac,258000,'noviembre: KoL 1140 + Intenso 1440');eq(c.nFac,2,'2 facturas');eq(c.ing,258000,'ingresos nov');eq(c.porC,205000,'por cobrar Open Fit');
eq(c.facB,94215+Math.round(144000*100/121),'sin IVA');
c=f.cbCalc(d,'EUR',O,'2026-11-27');eq(c.fac,27000,'octubre Miguel');
// Open Fit cobrado hoy -> entra al momento
d.pays[0].paid='2026-11-27';c=f.cbCalc(d,'EUR',N,'2026-11-27');eq(c.fac,463000,'Open Fit cobrado suma');eq(c.nFac,3,'3');eq(c.porC,0,'nada por cobrar');
// si luego se le hace factura con el mismo importe no se duplica
d.inv.push({id:'f2',num:'2026-153',client_id:'c_of',client:'Gimnasio Open Fit SL',date:'2026-11-28',cur:'EUR',total:205000,sub:169421,tax:35579});
c=f.cbCalc(d,'EUR',N,'2026-11-27');eq(c.fac,463000,'factura de Open Fit no duplica');eq(c.nFac,3,'sigue en 3');
// factura hecha fuera (fin in) que coincide por nombre con Intenso
d.items.push({id:'x1',kind:'in',date:'2026-11-12',who:'Intenso Fragancias',total:144000,rate:21,cur:'EUR'});
c=f.cbCalc(d,'EUR',N,'2026-11-27');eq(c.fac,463000,'fuera de Intenso no duplica');
// factura sin cobro cuenta igual
d.inv.push({id:'f3',num:'2026-154',client_id:'c_z',client:'Z',date:'2026-11-20',cur:'EUR',total:10000,sub:8264,tax:1736});
c=f.cbCalc(d,'EUR',N,'2026-11-27');eq(c.fac,473000,'factura suelta cuenta');
const iv=f.cbIva(d,'EUR',{from:'2026-10-01',to:'2026-12-31'});eq(iv.rep>0,true,'IVA repercutido');
console.log(ok,'bien',bad,'mal');process.exit(bad?1:0);
