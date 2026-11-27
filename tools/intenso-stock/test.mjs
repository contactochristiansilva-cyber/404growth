import main from './run_code.js';
const prod = (id,t,type,mlv)=>({id:'gid://p/'+id,title:t,productType:type,mlEnStock: mlv==null?null:{value:String(mlv)},variants:['30 ml','50 ml','100 ml','500 ml'].map((x,i)=>({title:x,inventoryItem:{id:'gid://ii/'+id+'-'+i}}))});
const input={order:{lineItems:[
 {quantity:2,variantTitle:'100 ml',product:{productType:'Esenciales',title:'Nº 10'},customAttributes:[]},
 {quantity:1,variantTitle:'Nicho',product:{productType:'Decant',title:'Decant 5 ml'},customAttributes:[{key:'Perfume',value:'Nº 7'},{key:'_u',value:'/x'}]},
 {quantity:1,variantTitle:'50 ml',product:{productType:'Pack',title:'Trío Esenciales'},customAttributes:[{key:'Perfume 1',value:'Nº 10'},{key:'Perfume 2',value:'Nº 12'},{key:'Perfume 3',value:'Nº 10'}]},
 {quantity:1,variantTitle:'Gratis',product:{productType:'Regalo',title:'2 decants'},customAttributes:[]},
]},getProductData:[prod(1,'Nº 10','Esenciales',null),prod(2,'Nº 7','Nicho',152),prod(3,'Nº 12','Esenciales',40),prod(4,'Nº 100','Esenciales',500)]};
console.log(JSON.stringify(main(input),null,1));
