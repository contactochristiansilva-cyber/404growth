# Scrapeo del 18/11/2026 para el 19/11: 35 tiendas con los filtros nuevos

## Por qué se cambiaron los filtros (datos de noviembre)

Datos del CRM y del contador de visitas a 18/11, con 252 propuestas enviadas del 2 al 18/11:

- **Se abren el 44 %.** De las abiertas:
  - la mitad se cierra en menos de 1 minuto;
  - 7 de cada 10 no pasan del primer tercio;
  - solo el 10 % llega al final.
- **El 21 % muestra interés de verdad** (más de 2 minutos, o vuelve otro día). Son 54 tiendas, y 9 pulsaron «Escribir a Christian».
- **Interés por nicho:**
  - perfumería y cosmética: 47 %;
  - suplementos: 44 %;
  - mercería: 38 %;
  - joyería: 26 %;
  - sneakers: 22 %;
  - moda: 18 %;
  - ópticas: 15 %.
- **Por seguidores:** las de más de 50.000 son las que peor responden (10 %). Las mejores son las de 10.000 a 20.000 y las de menos de 5.000 (24–25 %).
- **Los lotes del 17 y el 18/11** (el de anuncios de Meta y el de sin moda) se abrieron el 32–38 %, frente al 54 % del 13/11.
- **Tener una web informativa no les quita interés:** se abren el 53 % de las que la tienen.
- **En noviembre nadie está marcado como «respondió» ni «reunión»** (Kiss of Life sigue en «Caliente»). Por eso no se puede medir qué perfil contesta. Desde ahora hay que marcarlo.
- **Lo que tienen en común Kiss of Life, Intenso y Carmen Valencia:** ya vendían a distancia, a mano (WhatsApp, Instagram, envíos).

## Filtros que se usaron

1. **Obligatorio: que ya vendan a distancia.** En la bio o en sus últimas 12 publicaciones tiene que salir alguna de estas señales:
   - envíos, o «toda España»;
   - pedidos por WhatsApp o por mensaje privado;
   - Bizum;
   - directos de venta;
   - «ventas por Instagram».
2. Interacción real: una mediana de «me gusta» de al menos el 0,6 % de los seguidores (casi todas superan el 1 %).
3. Entre 3.500 y 50.000 seguidores; casi todas tienen entre 4.000 y 20.000.
4. Que hayan publicado en los últimos 10 días.
5. Que no tengan tienda online que venda. Valen las que tienen:
   - ninguna web;
   - una web vacía, informativa o que solo enseña su Instagram;
   - una web que no carga, en obras o en mantenimiento;
   - un Shopify con 9 productos.
6. Un número para WhatsApp: móvil publicado, o un fijo que publican como WhatsApp.
7. Fuera, como siempre: cadenas, árabe, comida, Canarias y las que ya están en el CRM. Se cruzó por Instagram, teléfono y nombre.

## Cómo se buscó (solo Instagram, sin la Biblioteca de anuncios)

- `engine19.js` es el motor que se pegó en la pestaña de instagram.com.
  - Hay que capturar antes las consultas de la propia web (`PolarisKeywordSearchExplorePageRelayQuery`, `PolarisProfilePageContentQuery`, `PolarisProfilePostsQuery` y `PolarisProfileSuggestedUsersWithPreloadableQuery`) y definir `gq()`.
  - Usa 3 bucles de búsqueda, 8 perfiles en paralelo y cuentas parecidas a partir de las buenas y de los clientes. No hubo ni un error 429.
- Se hicieron 470 búsquedas: boutique, moda mujer, tienda de ropa, moda hombre, perfumería, joyería, ropa deportiva, suplementos, perfumes de equivalencia, cosmética coreana y showroom, por unas 100 ciudades. Se añadieron 30 frases de señal («pedidos por whatsapp boutique», «venta en directo ropa»…) y 36 tandas de cuentas parecidas.
- Salieron unos 4.400 perfiles. 2.000 estaban en el rango de seguidores y se miraron con sus publicaciones. 114 pasaron los filtros automáticos y se revisaron a mano.
- **Webs:** por `r.jina.ai` desde una pestaña suya (Shopify `products.json` y WooCommerce `wc/store`). Da error 429 con más de unas 20 peticiones por minuto, así que hay que esperar 3–4 s entre una y otra. Con `Accept: application/json` devuelve el JSON escapado dentro de `data.text`: hay que buscar `\"products\"`.
- **Google Maps** (`/search?tbm=map`, desde una pestaña de google.com/maps): de ahí salieron móviles que no estaban en Instagram, y webs que no enlazan en la bio (así se vio que El Armario de Paula y Colo Colo sí venden online).
- **WhatsApp Web no tenía la sesión abierta** en ninguno de los dos Chrome (los dos piden el QR), así que no se pudo comprobar. Las 22 que publican el número como WhatsApp van con prioridad 85–90. Las 13 que no lo dicen llevan `waOk: false` y «WhatsApp sin comprobar».

## Lo que se aprendió

- **Las mejores señales salen de sus propias publicaciones.** Ooh la la: «Muchas nos preguntáis cómo podéis comprar online si no tenemos página web». Kokoro: «De momento no disponemos de página web… escríbenos por WhatsApp». Eso vale más que los seguidores.
- **Perfumería, suplementos y joyería con estos filtros casi siempre venden ya online:** Maison de Pat, Ibarrondo, L'Atelier 8 Sens, Ramos Joyería, Laura Sampedro… En este lote solo entraron 2 joyerías. Para estos nichos hay que buscar las que se quedan fuera (sin web) en pueblos y barrios.
- **Moda de hombre:** las buenas son mixtas (mujer y hombre). Las de hombre puro con marcas (Harcher, Kiko Bigot, Mr. V) ya tienen web o solo publican fijo.
- Muchas webs que no se ven en la bio salen en Google Maps. Hay que mirarlas siempre antes de dar una tienda por buena.

## Resultado: `leads.json` (35)

32 de moda (25 de mujer y 5 mixtas, más complementos y lencería), 1 zapatería y 2 joyerías.

Destacadas (prioridad 90):

- **Ooh la la:** dice que no tiene web y vende por WhatsApp y en directos.
- **Kokoro:** igual.
- **Cachibache:** directos de venta los jueves.
- **Bea-Bea:** 3 tiendas en Barcelona, con un Shopify de 9 productos.
- **Cent-Vuit:** 50.000 seguidores, pedidos por mensaje privado y WhatsApp.
- **Bendita Locura:** directos en Instagram, Facebook y TikTok, y una interacción del 3,1 %.

Avisos:

- **Coria del Río:** Sigueme, Casual Coria y Modas Rocío son del mismo pueblo, así que mejor no mandarlas a la vez.
- **Antequera:** Ooh la la y Mercedes Beltrán son de la misma ciudad.
- **Webs en obras:** NdeNua tiene la web «próximamente» y Novojoya, «en mantenimiento». Puede que ya tengan a alguien haciéndolas.
- **La Vera:** comparte móvil con Hermanas Romero, que se queda fuera.
- **Móviles sacados de Google Maps:** los de Bendita Locura y Miranda Shop.

Descartadas al revisar:

- **Ya venden online:** Miram Shop, Dondola, Malva, Azul, Tissè, Alana, Arena y Mar, Modas Belén, Zøre, Startara, Ana García, Woman Diez, Cotton Grey, Elephant, Kiko Bigot, Mr. V, La Traviata (Wix con tienda), Guillermina, Fionna Serra, El Armario de Paula, Colo Colo, Elsegoviano (estrena una web con 16 productos), Tienda de Eva, Ramos Joyería, Ibarrondo, L'Atelier 8 Sens y Maison de Pat.
- **Anuncian tienda online «pronto»:** Limere.
- **Sin ninguna señal de venta a distancia:** Lino Sartoria y Harcher (este, además, solo publica fijo).
- **Solo fijo:** Montserrat42, Teresa Izuel, Inusual, Tólf y La Regadera.

## CRM (worker del admin)

- `mkrows.py leads.json <rows19.js>` escribe `SEED4_KEY = "seed_20261119"` y `SEED4`. Todas van con `lotDay` 2026-11-19 y **sin propuesta**: el Lote de hoy solo las enseña cuando tengan `pageUrl`.
- `patch_s19.py <worker> <rows19.js> <salida>` mete `SEED4` después de `SEED3` y la añade como cuarta lista de `seedOnce`.
- La prueba es `t_s19.mjs`, con 23 comprobaciones. Necesita `d1shim.mjs` y el worker como módulo: una copia más una línea `export {…}`, hechas en comandos aparte.
- En el Mac quedó el admin con huella 66cd4035c6ed85b1. La copia de la v78 está en `anterior/worker-v78-18nov-antes-seed19.js`.
