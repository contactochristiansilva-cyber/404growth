import fs from 'fs';
import {createRequire} from 'module';
const require=createRequire(process.argv[2]+'/');
const topo=require('world-atlas/countries-50m.json');
const {feature}=require('topojson-client');
const d3=require('d3-geo');
const fc=feature(topo,topo.objects.countries);
const es=fc.features.find(f=>f.id==='724');
// keep peninsula + Baleares
const polys=(es.geometry.type==='MultiPolygon'?es.geometry.coordinates:[es.geometry.coordinates]).filter(p=>{const r=p[0];const lat=r.reduce((a,c)=>a+c[1],0)/r.length;const lon=r.reduce((a,c)=>a+c[0],0)/r.length;return lat>36&&lon>-10&&!(lat<36.2)});
const g={type:'Feature',geometry:{type:'MultiPolygon',coordinates:polys}};
const W=+process.argv[3],H=+process.argv[4];
const proj=d3.geoConicConformal().parallels([37,43]).rotate([3.5,0]).fitExtent([[10,10],[W-10,H-10]],g);
const path=d3.geoPath(proj);
const cities={madrid:[-3.70,40.42],barcelona:[2.17,41.39],valencia:[-0.38,39.47],sevilla:[-5.98,37.39],bilbao:[-2.93,43.26],coruna:[-8.41,43.36],malaga:[-4.42,36.72],zaragoza:[-0.88,41.65],palma:[2.65,39.57],murcia:[-1.13,37.99],valladolid:[-4.72,41.65],granada:[-3.60,37.18],oviedo:[-5.85,43.36],pamplona:[-1.64,42.81],alicante:[-0.48,38.35],santander:[-3.80,43.46],salamanca:[-5.66,40.97],badajoz:[-6.97,38.88],girona:[2.82,41.98],vigo:[-8.72,42.24],cadiz:[-6.29,36.53],cordoba:[-4.78,37.88],logrono:[-2.45,42.47],toledo:[-4.02,39.86],castellon:[-0.04,39.99],almeria:[-2.46,36.84],lleida:[0.62,41.62],leon:[-5.57,42.60],burgos:[-3.70,42.34],albacete:[-1.86,38.99],caceres:[-6.37,39.47],huelva:[-6.95,37.26],jaen:[-3.79,37.77],tarragona:[1.25,41.12],cuenca:[-2.13,40.07],lugo:[-7.56,43.01],ourense:[-7.86,42.34],teruel:[-1.11,40.34],soria:[-2.47,41.76],ciudadreal:[-3.93,38.98],ibiza:[1.43,38.91],menorca:[4.0,39.95]};
const pts={};for(const k in cities){const p=proj(cities[k]);pts[k]=[+p[0].toFixed(1),+p[1].toFixed(1)]}
fs.writeFileSync(process.argv[5],JSON.stringify({d:path(g),pts,W,H}));
console.log('ok',path(g).length,pts.madrid);
