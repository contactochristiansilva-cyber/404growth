# Scrapeo del 17/11/2026 para el 18/11: 30 tiendas sin moda ni comida

## Lo que pidió Chris

Empezó como «30 tiendas con anuncios en Meta y WhatsApp comprobado». Durante la noche cambió así:

- **WhatsApp:** «mientras tenga teléfono publicado en algún lado no importa, no hace falta verificarlo».
- **Meta:** nada de la Biblioteca de anuncios («no quiero que me bloqueen nada»). Solo Instagram.
- **Instagram:** tiendas con **más de 10.000 seguidores** y actividad constante.
- **Nichos:** «carnicería tampoco… empresas que vendan productos propios, creados por ellos, reventa de sneakers, suplementos… pero no de comida o productos perecederos», porque los envíos son delicados.

Se mantiene lo de siempre: tienda física en España (sin Canarias), sin tienda online de verdad, que no estén en el CRM, sin cadenas, nada árabe y sin moda.

## Filtros que se usaron

- Más de 10.000 seguidores.
- Última publicación hace 14 días o menos, y 4 o más publicaciones en 30 días.
- Teléfono publicado en la bio, en sus publicaciones, en su web o en Google Maps.
- Web ninguna, rota, en obras, de catálogo sin carrito o con muy pocos productos (25 o menos).
- Cruzadas con el CRM (Instagram, teléfonos y nombre) y con todas las listas de `prospeccion/`.

## Cómo se buscó

1. **Instagram por palabra clave** (`PolarisKeywordSearchExplorePageRelayQuery`): nicho × ciudad, unas 1.200 búsquedas y unos 25.700 perfiles. Perfil completo con `PolarisProfilePageContentQuery`; actividad y teléfonos de los textos con `PolarisProfilePostsQuery`.
2. **Cuentas parecidas** (`PolarisProfileSuggestedUsersWithPreloadableQuery`, `module: 'profile'`): desde cada tienda buena salen unas 30 parecidas. Es lo que más rindió en mercerías, telas, bordados, aderezos y belén.
3. **Webs** por r.jina.ai: Shopify `/products.json`, WooCommerce (`wc/store` y `wp/v2/product`), PrestaShop, precios y carrito. Si WooCommerce dice 0 productos, se mira la tienda en Chrome: a veces la API está apagada y la tienda sí vende (Magic Barcelona tenía 387).
4. **Dominios ocultos**: se buscan dominios en los textos de sus publicaciones (así salieron allyours.com y perfumeriaslaguna.com, que ya venden) y se prueba el DNS con `dns.google/resolve`.
5. **Google Maps** (`/search?tbm=map` con la calle, la ciudad y «España»): teléfono, web y dirección de la ficha.

## Lo que se aprendió

- Más de 10.000 seguidores, actividad y sin tienda online es raro en herbolarios, suplementos, perfumerías, ópticas y mascotas: casi todas venden ya online.
- **Donde sí sale:**
  - mercerías, lanas y telas (12 de las 30);
  - aderezos de fallera y joyería de taller;
  - bellas artes y scrap;
  - cerámica, bordado en oro, belén y esparto.
- «Córdoba», «Valencia», «Granada» o «Mérida» traen muchas cuentas de Latinoamérica: hay que filtrar por país.
- Los fijos son muchos. 6 de las 30 solo publican fijo.

## Resultado: `candidatos.json` (30)

| Nicho en el CRM | Tiendas |
|---|---|
| `merceria` (nuevo) | 12: Mercería Mari Carmen, Lanas Paloma, Fernández-Cruz Miguel, Lanas Cachemir, Mercería San García, Mina Mina, Cocorola, Madejas Tejerlo, Dmario Tejidos, Teixits Donna, Cast Tejidos, Sederías Natalia |
| `joya` | 5: Botones de Plata, Magdala, Bisuterapia, Art-Antic, Roda |
| `artesania` (nuevo) | 4: Cerámica Fajalauza, Bordados Perales, Alfares, Esparto Antonio López |
| `arte` (nuevo) | 3: Jaspe Art, My Scrap Place, Scrapa2 |
| `toys` | 2: Nexus Tabletop, Juguetes Duba |
| `cosmetica` | Only Today Perfumería (perfumes propios) |
| `suplementos` | Herbolario Cai Salud |
| `deporte` | FGA Equitación |
| `electro` (nuevo) | Factory Electrodomésticos (outlet) |

### Contacto de las 30

- **8 publican el número como WhatsApp:** Botones de Plata, Mercería San García, Mina Mina, Cocorola, Cast Tejidos, Alfares, Esparto Antonio López y Sederías Natalia (un fijo con WhatsApp).
- **16 tienen móvil sin comprobar.** En el CRM llevan `waOk: false`, así que sale primero «Instagram».
- **6 tienen solo fijo** y van con prioridad 50 y «AVISO»: Herbolario Cai Salud, Jaspe Art, Lanas Cachemir, My Scrap Place, Dmario Tejidos y Juguetes Duba.

### Avisos

- Las de poca interacción: FGA Equitación (mediana de 4 «me gusta»), Esparto Antonio López (9) y Scrapa2 (12).
- Factory Electrodomésticos es un outlet: su stock no es fijo.
- La cuenta de Mercería Mari Carmen es la de la dueña.
- Cocorola es un puesto de los Encants.

**Reserva:** Daniel Bada (Valencia, aderezos de valenciana, 13.400 seguidores, mediana de 274 «me gusta»). Su web danielbada.com es WooCommerce con 18 productos.

## CRM (worker del admin)

Se hace con `patch_l39.py` + `mkrows.py`. La prueba es `t_l39.mjs`, con 32 comprobaciones.

- **Nichos nuevos:** `merceria`, `arte`, `artesania` y `electro`, con los textos de Deporte, como `scrapeo-10nov/patch_niches.py`.
- **`SEED3_KEY = "seed_20261118"`:** las 30 entran en Scrapeados como tercera lista de `seedOnce`. Van **sin propuesta**, así que todavía no salen en el Lote de hoy, que solo coge leads con `pageUrl`.
- **`LEAD_PATCH_KEY = "lpatch_20261118"`:** las 5 del lote 38 que se quedaron sin enviar pasan al lote del 18/11. Son Ailec Modas, Calzados Bergillos, Calzados Toñi, Kisco y Livorno. La lista anterior queda como `LEAD_PATCH_17NOV`.
