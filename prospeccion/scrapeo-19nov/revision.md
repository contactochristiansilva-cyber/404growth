# Scrapeo del 19/11/2026 para los lotes del 20 y el 21/11

Mismos filtros que el 18/11 (ver `../scrapeo-18nov/revision.md`):

- ya venden a distancia: envíos, pedidos por WhatsApp o por mensaje privado, Bizum o directos;
- interacción de al menos el 0,6 % (mediana de «me gusta» entre seguidores);
- unos 4.000–40.000 seguidores;
- han publicado en los últimos 10 días;
- sin tienda online que venda (se miró también la web de su ficha de Google Maps);
- un móvil publicado;
- sin cadenas, nada árabe, nada de comida, nada de Canarias y que no estén ya en el CRM.

## Resultado: `leads.json` (29)

25 de moda y 4 zapaterías (`sneakers`).

- **Lote del 20/11 (15):** Bolsos Cati, Tacones Baza, Violeta Calzados, Akira Carballo, Calzados J. Díaz, Qué Locura, Ana y Chica, Aire Modas, Isabela Mendoza, Garate, Mesa Calzados, Luvi Modas, XS Accessories, Rey Piel y Delavega Store.
- **Lote del 21/11 (14):** El Vestidor Baza, Nyc Store, Mariacaprichos, Liquet, Samoa Pinos Puente, Ana Collado, Abril Moda Mujer, Ooh Lala Peal de Becerro, Gothyka, Merakih, Embrujo Modas, Doble M, Mila García y Acaik.
- Nunca dos del mismo pueblo el mismo día:
  - Baza: Tacones el 20 y El Vestidor el 21; están en la misma calle.
  - Jerez: Isabela Mendoza el 20 y Merakih el 21.
  - Granada: XS el 20 y Liquet el 21.
- **WhatsApp:** 15 publican su móvil como WhatsApp (prioridad 85–90). Las otras 14 llevan `waOk: false` y «WhatsApp sin comprobar»; WhatsApp Web sigue sin sesión.
- **Móviles sacados de Google Maps:** los de Doble M, Mila García y Acaik, que en Instagram no ponen el número.
- **Webs que entran:**
  - Shopify cerrado («Tienda no disponible»): Ana y Chica y Delavega.
  - Web caída o rota: Isabela Mendoza (error 503), Violeta y Abril (error de certificado), El Vestidor (página de error) y Nyc Store (el dominio no existe).
  - En mantenimiento: Aire Modas.
  - Webs informativas sin carrito: Mesa Calzados, Rey Piel, Ooh Lala y Doble M (catálogo).
  - WooCommerce con muy pocos productos: Luvi (5), XS (9) y Merakih (12).

## Cómo se buscó

- Motor: el de `../scrapeo-18nov/engine19.js`, pegado en la pestaña de instagram.com. Hay que definir antes `gq()` con las consultas capturadas de la propia web.
- **Ojo:** al usar `navigate` sin `tabId`, Chrome llevó la pestaña de Instagram al admin y se perdió todo lo que había en memoria. Pasa siempre el `tabId`.
- Búsquedas: «boutique <pueblo>», «moda <pueblo>», «zapateria <pueblo>» y «complementos <pueblo>» en unos 160 pueblos y ciudades medianas, más 12 frases de señal y 2 tandas de cuentas parecidas.
  - **Las búsquedas de 3 palabras con «moda mujer» dan 0 resultados.** Las de 2 palabras sí funcionan.
  - En total, unas 485 búsquedas y 6.250 perfiles, sin ningún error 429. 104 pasaron los filtros automáticos.
- **Webs:** con r.jina.ai desde una pestaña de r.jina.ai, porque desde instagram.com lo bloquea su CSP.
  - Shopify: `/products.json`.
  - WooCommerce: `wc/store`. Si da 0, hay que mirar la portada en markdown (precios y carrito).
  - Un 422 de jina suele ser un dominio que no existe o un error de certificado. Se confirma con dns.google.
  - La pestaña de jina en segundo plano va lenta, porque Chrome frena sus temporizadores.
- **Google Maps:** `fetch('/search?tbm=map&q=…')` desde una pestaña de google.com/maps da la dirección (código postal y ciudad), el teléfono y la web de la ficha.
- **El cruce con el CRM** se hace al final, en la pestaña del admin, con `crm/state`, por Instagram y por número. Así salieron 5 que ya estaban: Carlos Pina, Elena Blanco, Iris, Coccu y La Cañada (lote 38). También se cruza con lo descartado el 18/11.

## Descartadas al revisar

- **Ya estaban en el CRM o ya se habían revisado:**
  - en el CRM: Carlos Pina, Elena Blanco, Iris, Coccu y La Cañada;
  - revisadas el 18/11: Dpaula's Closet, Hermanas Romero (comparte móvil con La Vera), Arena y Mar, Modas Belén, Elephant, El Segoviano, Tienda de Eva, Laura Sampedro, El Armario de Paula, Colo Colo, Berta y Carmen's.
- **Ya venden online:** Mari Perales, Confecciones Benito, Calzados del Río, Fionna Serra, La Naty, Módica, Difertencia, Zøre, Calzados Toñi, Mi Lola, Vicky's, Con Alma, Morena, Color de Abril, Bolsos Montse, La Gatita Presumida, Dalatalla, Víste te con B, Con Poderío, Pili y Mili, Sorgin Gazte, Cobá, Kilukamiluka, Boutique Glamour, Fugaz, Luis Rico, Frenzy, Noelia Molina, És Únic, Las Niñas, El Armario de Monik, Mía Shop y Lamona. Las cuatro últimas no se pudieron confirmar del todo, pero lo que se ve apunta a que venden.
- **No son tiendas de moda o venden comida:** pescaderías, carnicerías, flores, muebles, restaurantes, una radio, protectoras, ayuntamientos y Del Mar Para Ti (pescado a domicilio).
- **Sin ciudad clara:** Marilita y Cristina González.
- **Canarias:** House & Clo.
- **Solo publican fijo:** El Pecado, Sara, Hermanas Serrano, Vestido y Tacón, Avance, Lalín Moda, Pretty, Sucursal, Begoña Vázquez y Catarinetes.

## CRM (worker del admin)

- `mkrows.py leads.json <rows20.js>` escribe `SEED5_KEY = "seed_20261120"` y `SEED5`. Cada tienda lleva el `lotDay` que le toca (20 o 21/11) y va **sin propuesta**: el Lote de hoy solo la enseña cuando tenga `pageUrl`.
- `patch_s20.py <worker> <rows20.js> <salida>` mete `SEED5` después de `SEED4`, como quinta lista de `seedOnce`.
- La prueba es `t_s20.mjs`, con 25 comprobaciones. Necesita `d1shim.mjs` y `w20mod.mjs`: una copia del worker con una línea `export {…}` al final.
- En el Mac, el admin quedó con la huella c3d473bdb90474a0. La copia de la v80 está en `anterior/worker-v80-19nov-antes-seed20.js` y las fuentes en `fuentes-s20/`.
