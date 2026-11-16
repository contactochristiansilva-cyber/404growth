# Búsqueda piloto de 30 prospectos más grandes (16/11/2026)

Lo que pidió Chris: negocios más grandes, con varias tiendas, más recorrido y más presupuesto. Cualquier nicho. Criterios que se miraron en cada uno:

- tienda física en España (y cuántas);
- anuncios en Meta en los últimos 12 meses (Biblioteca de anuncios), sobre todo los que mandan a WhatsApp o a Instagram;
- sin tienda online, o con una web caída, privada, sin carrito o con muy pocos productos;
- seguidores e interacción real (mediana de «me gusta» + comentarios de sus 12 últimas publicaciones entre seguidores);
- años, varias tiendas o equipo.

La lista está en `leads.json` (30, con `tier`, `score` y notas). No están en el CRM: se cruzaron con `prospeccion/` y el `SEED` del worker. Fuera por estar ya: Lenceshop, Joyería Ferrezuelo, Jerez L12, Caprichosa, Cattalina, Modas Jade, Quattro, Frecuencia, Benezit, Coccu, GRQ Jerez, Boutique N7, Carmen's Boutique, Last Price, Maribel Torero.

## Puntuación (0 a 10)

- Tiendas: 1 → 0; 2 → 2; 3 o más → 3.
- Anuncios: activos hoy → 3; en los últimos 12 meses → 2; ninguno → 0.
- Web: sin web, caída, privada o sin carrito → 2; floja (≤ 20 productos o «próxima apertura») → 1.
- Instagram: ≥ 20.000 seguidores con ≥ 0,3 % de interacción → 2; ≥ 5.000 con ≥ 0,3 % (o ≥ 20.000 con 0,1–0,3 %) → 1.

## Resultado

- **A (18): cumplen todo** (tienda física + anuncios en el último año + sin tienda online de verdad).
- **B (12): les falta un criterio**, casi siempre los anuncios. Las de abajo son pequeñas: relleno para llegar a 30.

## Lo que se aprendió

- **Anuncios + sin tienda online existe, pero es raro en las grandes.** De 72 tiendas de Instagram con página de Facebook, 43 habían hecho anuncios en el último año; de esas, casi todas ya venden online (Shopify o WooCommerce con 100 o más productos). Lo mismo con los muebles y las colchonerías con anuncios: todas tenían web con carrito (Guerrilleros Utrera, Gonzamar, El Danubio, El Hogar del Descanso, El Castor).
- **Los seguidores engañan.** Muchas cuentas de 50.000 a 150.000 seguidores tienen 3 a 50 «me gusta» de media (Riverropa 155.000 → 3; Sesamo 60.000 → 3; Zona Coolto 107.000 → 48). La interacción es mejor filtro que los seguidores.
- **Nichos que dan más «anuncios sin tienda online»:** flamenca (mantones, trajes, tiendas de baile), muebles y sofás de exposición grande, outlets de marcas y joyerías de varias tiendas (compro oro). Moda multimarca con varias tiendas casi siempre tiene ya web.
- **Volumen:** unas 3 horas de búsqueda dan unos 15 a 20 prospectos de verdad buenos. Para 30 diarios de este nivel hace falta ampliar ciudades y nichos (flamenca y muebles por provincias) o aceptar los de tipo B.

## Cómo se buscó (para repetirlo)

1. **Instagram, por palabra clave** (`PolarisKeywordSearchExplorePageRelayQuery`, 280 búsquedas de nicho × ciudad, 3.605 perfiles): bio con calle o varias ciudades, España, seguidores. El perfil (`PolarisProfilePageContentQuery`) da `linked_fb_info.linked_fb_page.id`.
2. **Biblioteca de anuncios** (facebook.com/ads/library, sesión de Chris): se captura la petición `AdLibrarySearchPaginationQuery` al bajar por los resultados y se repite desde la pestaña con otras variables.
   - Por página: `searchType: 'page'`, `viewAllPageID`, `activeStatus: 'all'`. Cada anuncio trae `start_date`, `is_active`, `snapshot.cta_type`, `snapshot.link_url` y `page_like_count`.
   - Por nombre (cuentas sin página enlazada): `searchType: 'keyword_unordered'` con el nombre exacto del negocio; se queda el resultado cuyo `page_name` coincide.
   - Al revés (primero anuncios): frases como «trajes de flamenca», «sofás», «pedidos por WhatsApp», «todas nuestras tiendas», con `activeStatus: 'active'` y `countries: ['ES']`. Se quedan las páginas cuyos anuncios no llevan a una web propia (solo Instagram, WhatsApp, Messenger o «cómo llegar») y sin `SHOP_NOW`.
   - La respuesta viene en líneas con el prefijo `for (;;);`. No hay recuento de anuncios: se cuentan las fechas.
3. **Webs**, desde una pestaña de r.jina.ai (`fetch('/https://dominio/...')`), una petición cada 3,3 s (si no, error 429): `/products.json` (Shopify), `/wp-json/wc/store/v1/products` y `/wp-json/wp/v2/product?per_page=100&_fields=id` (WooCommerce, este último da el número real), y la portada en markdown.
4. **Interacción y teléfonos**: `PolarisProfilePostsQuery` (12 publicaciones). **Google Maps**: `fetch('/search?tbm=map&hl=es&gl=es&q=…')` desde una pestaña de google.com/maps.

Falta, si se meten en el CRM: comprobar en WhatsApp Web los móviles que no dicen WhatsApp, y la ciudad de Pepa Guirola.
