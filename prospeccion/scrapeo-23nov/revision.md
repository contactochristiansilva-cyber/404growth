# Scrapeo del 23/11/2026: 50 tiendas más (`seed_20261124`)

Chris (23/11): «scrapea 50 negocios más, mismas características de filtrado que las últimas 40».

## Filtros (los del lote del 23/11, `scrapeo-22nov/`)

- Moda, joyería, perfumería y calzado. Nada de mercerías, artesanía ni muebles; nada árabe; sin Canarias ni Latinoamérica.
- Nivel de conciencia antes que seguidores (1.500–200.000):
  - A: anuncian en Meta (Biblioteca, frase exacta del nombre) y no tienen tienda online de verdad;
  - B: web rota, cerrada con contraseña, sin carrito o con muy pocos productos;
  - C: venden a distancia (envíos, pedidos por WhatsApp o MD, Bizum, directos) sin anuncios ni web.
- Activas (última publicación hace 14 días o menos), con móvil o WhatsApp, y fuera del CRM (cruce por Instagram y por número).

## Resultado

50 tiendas en `leads.json`: 18 A, 10 B y 22 C. 36 de moda, 7 de calzado, 6 de joyería y 1 perfumería.

Por día, sin dos del mismo pueblo el mismo día (contando lo que ya había en esos lotes): 13 el 24, 12 el 25, 12 el 26, 12 el 27 y 1 el lunes 30 (La Coqueta, la quinta de Jerez de la semana).

- 32 llevan `waOk: false` (el negocio no dice que el número sea WhatsApp; WhatsApp Web no se comprobó).
- 4 solo tienen fijo (prioridad 50 y «AVISO»): Pretty Rose, Joyería Azorín, Almer Joyas y Twins.
- Sin ciudad: Martín el Bisutero, Mi Bolso y Basik (con «AVISO»).
- Avisos para comprobar: la web de Santo Domingo Calzados (Cloudflare no dejó abrirla) y la de La Descreída (tiene carrito, no se ven precios).

## Cómo se buscó

- Motor de Instagram (el de `scrapeo-21nov/engine23.js`, compactado): unas 700 búsquedas de nicho + pueblo y cuentas parecidas de las buenas; 5.200 perfiles, 0 errores 429. Fuera las de Latinoamérica por la ciudad, el prefijo, «10k/14k», «S.A.S.», etc.
- Anuncios: `AdLibrarySearchPaginationQuery` capturada en la pestaña de la Biblioteca y repetida con `fetch` (frase exacta del nombre y del usuario). Unas 200 cuentas, sin bloqueos. De cada 2 cuentas con anuncios, casi siempre una ya vende online.
- Webs: r.jina.ai (`/products.json`, `/wp-json/wc/store/v1/products` y la portada). Con varias peticiones a la vez da 429 enseguida: una petición cada 3 s como mucho.
- Google Maps desde su pestaña (`/search?tbm=map&q=…`): teléfonos y la web de la ficha (así salieron trajesdeflamencamadrid.com con contraseña, twinsmoda.es caída y las webs sin tienda de Rachel & You, Cosa de Tres o Modas Naomi).
- Fuera al revisar: El Armario de Monik (su web ya vende), Hermanas Romero (el móvil es el de La Vera, ya en el CRM), Clàudia Bellera (encargos cerrados hasta 2027), Joyería Gustavo (empeños), Fátima Modas (todo a 10–20 €).

## Archivos

| Archivo | Qué hace |
|---|---|
| `mkleads.py leads.json` | las 50, con su puntuación y el día |
| `mkrows.py leads.json rows24.js` | `SEED7_KEY`/`SEED7` |
| `patch_s24.py <worker con SEED6> rows24.js <salida>` | mete el SEED7 y lo añade a `seedOnce` |
| `t_s24.mjs` | 16 comprobaciones (con `d1shim.mjs` y `w24mod.mjs`) |

Admin del Mac con la huella 96bf88138ae323d8 (copia de antes en `anterior/worker-l42-23nov-antes-seed24.js`). Falta `subir.command`.
