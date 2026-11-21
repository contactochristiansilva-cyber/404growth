# Scrapeo del 21/11/2026 para el lunes 23/11: 40 tiendas por nivel de conciencia

Chris (21/11): «un nivel de conciencia mayor no es lo mismo que tener muchos seguidores». Los seguidores ya no son un filtro; solo suman un poco en la puntuación.

## Criterio

1. **Conciencia (lo que más pesa):**
   - anuncios en Meta en los últimos 12 meses (Biblioteca de anuncios, búsqueda por frase exacta del nombre);
   - o una web que no vende: rota, caída, sin tienda, catálogo sin carrito o con muy pocos productos.
2. Ya venden a distancia: envíos, pedidos por WhatsApp o mensaje, Bizum o directos.
3. Activas: última publicación hace 14 días o menos (casi todas, 5 o menos).
4. Un móvil o WhatsApp publicado. Solo Calzados Isacio tiene únicamente fijo (prioridad 50).
5. Nichos: primero mercería, calzado, cosmética y perfumería, y suplementos; después joyería. Moda solo si anuncia o tiene la web rota.
6. Sin cadenas, sin Canarias, nada árabe y nada que ya esté en el CRM (cruzado por Instagram, nombre y teléfono con `crm/state`).

## Resultado

40 tiendas en `leads.json`, ordenadas por puntuación (0–100):

| Nivel | Cuántas | Qué es |
|---|---|---|
| A | 16 | anuncian en Meta y no tienen tienda online de verdad (3 de ellas con la web rota) |
| B | 11 | web rota o sin tienda, sin anuncios encontrados |
| C | 13 | relleno: nichos prioritarios que venden a distancia, sin anuncios ni web |

Por nicho: 14 mercerías, 12 moda (todas con anuncios o web rota), 8 calzado, 5 joyería y 1 herbolario.

Puntuación: A 70, B 55 y C 40, más el nicho (cosmética y suplementos 10, mercería y calzado 8, joyería 5, moda 0), +5 si la interacción es de al menos el 1,5 %, +3 si publican el WhatsApp, +3 con 10.000 seguidores o más y +3 si publicaron hace 4 días o menos.

## Lo que se aprendió

- **Quien anuncia casi siempre vende ya online.** De unas 90 cuentas con anuncios, solo 16 no tenían tienda de verdad. Las que más rinden son las mercerías de barrio, las joyerías pequeñas y la moda de pueblo.
- **Las webs rotas son una buena fuente.** 11 tiendas tienen en la bio una web que no carga:
  - error de certificado en dominios que apuntan a Shopify;
  - dominios que ya no existen;
  - error 500;
  - Wix sin dominio;
  - la web de Google («negocio.site»), que Google cerró.
- Perfumería, cosmética y suplementos con anuncios venden ya online casi todas. Muchas perfumerías que anuncian son de perfumes árabes y quedan fuera.
- En la Biblioteca de anuncios, la búsqueda por palabra clave («mercería envíos», «zapatería whatsapp», «perfumería tienda física»…) da los anunciantes del nicho. Sirve para encontrar tiendas que anuncian; después se busca su Instagram por el nombre.

## Descartadas al revisar

- Venden ya online:
  - Tedín, Manuela León, El Armario de Monik, La Maison de Pat, Ana Faura, Soraya Glow, Con Alma, Tuareg y Castello Parfums;
  - Mercería Baptista, Tejidos Yasmina (su taplink lleva a tejidosyasmina.com) y Marydory (estrena web con carrito);
  - El Duende del Patchwork (90 productos), Urban Store Oviedo, Consuelo by Carol y Joyería Alcalá 181.
- No son tienda física (marca o divulgadora): Reset Free Beauty y Miriam Llantada.
- Cadena: Muscle Cult (varios locales). Esenzzia (970 anuncios, cadena de equivalencias).
- Perfumes árabes: Fragancia Huelva (y las que salieron con «árabe» u «oud»).
- Inactivas: Trainer Shop (19 días).

## Avisos para el envío

- **Valencia:** El Cantó de Greses, Nicolina, Lana Negra y Tejidos Laine son mercerías de la misma ciudad, y Gironés Seda está en Manises. Todas van el mismo día. Si hace falta, dos de ellas pasan al martes.
- **Jerez:** Namá y Chabeli Modas el mismo día.
- **Sin ciudad:** La Platería del Sur, Paqui Gutiérrez, Crisly Coquette y Modas Carisma. Se sabrá al hablar con ellas o al preparar la propuesta.
- **WhatsApp:** 13 no publican el móvil como WhatsApp (`waOk: false`). WhatsApp Web no se comprobó.

## Archivos y cómo se repite

- `engine23.js`: el motor de Instagram del 18/11, con los seguidores entre 1.500 y 200.000 y la puntuación por conciencia.
  - También tiene el nicho `merceria` y el filtro de servicios (estética, peluquería, farmacia…), metido en la consola.
  - Ojo: el `Worker` de blob como temporizador no funciona en Instagram, porque su CSP lo bloquea sin avisar y los bucles se quedan parados. Hay que usar `setTimeout`.
- `mkleads.py leads.json`: los 40 con sus datos, avisos y puntuación.
- `mkrows.py leads.json rows23.js`: escribe `SEED6_KEY = "seed_20261123"` y `SEED6`.
- `patch_s23.py <worker> rows23.js <salida>`: mete el `SEED6` después del `SEED5`, como sexta lista de `seedOnce`.
- `t_s23.mjs`: 23 comprobaciones (necesita `d1shim.mjs` y `w23mod.mjs`).
- Las webs se comprueban:
  - con r.jina.ai (`/products.json`, `/wp-json/wc/store/v1/products`);
  - con dns.google cuando r.jina.ai da 422;
  - y abriéndolas en Chrome cuando hace falta ver el error.
