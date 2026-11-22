# Scrapeo del 21-22/11/2026 para el lunes 23/11 (`seed_20261123b`)

Sustituye al lote del 21/11 (`scrapeo-21nov/`, `seed_20261123`), que no se llegó a subir.

## Lo que pidió Chris (21/11/2026)

- Unas 35 o 40 tiendas para las prospecciones del lunes; las propuestas, solo cuando lo diga.
- Nichos: moda (mujer, hombre, deporte, flamenca, ceremonia…), perfumería y cosmética, joyería y suplementos. **Nada de mercerías, artesanía ni muebles.**
- Conciencia alta, por encima de los seguidores:
  - que anuncien en Meta;
  - o que tengan una web rota o floja.
- Además:
  - que ya vendan a distancia;
  - que estén activas;
  - que tengan móvil o WhatsApp publicado;
  - mejor si tienen varias tiendas.
- Que no estén en el CRM, nada árabe y nada de Canarias.

## Resultado: 36 tiendas

- **Por nicho:** 26 de moda, 7 de joyería y 3 de zapatería.
- **Por día:** 31 el lunes 23, 3 el martes 24 y 2 el miércoles 25.
- **Por nivel:**
  - A, 18: anuncian en Meta y no tienen tienda online de verdad;
  - B, 11: web rota, caída, cerrada o en un marketplace;
  - C, 7: venden a distancia con buena interacción o dos tiendas, sin anuncios ni web.
- **Del lote del 21/11 se quedan 19:** las de nivel A y B que no son mercerías.
- **Fuera de ese lote:** las 14 mercerías, todo el nivel C y Calzados Isacio, que solo publica fijo.
- **17 nuevas:** 6 A, 4 B y 7 C. Están en `mkleads.py`, cada una con su prueba (anuncios, web y frases de venta a distancia).

### Mismo pueblo, días distintos

| Pueblo | Lunes 23 | Martes 24 | Miércoles 25 |
|---|---|---|---|
| Vigo | Oops | I Love Complementos | Glamour Moda |
| Jerez | Amancia | Namá | Chabeli |
| Plasencia | Ábaco | Modas Cereza | |

### Sin ciudad

- La Platería del Sur, Modas Carisma y Crisly Coquette no la ponen en Instagram (las tres están en «AVISO»).
- Cambia-T: la dirección sale de sus publicaciones.

### WhatsApp

- 13 llevan `waOk: false`: el negocio no dice que el móvil sea WhatsApp.
- WhatsApp Web no tenía sesión, así que no se comprobó ninguno.

## Cómo se buscó

- **El motor de Instagram** (`scrapeo-21nov/engine23.js`, en la pestaña de Instagram):
  - búsquedas por palabra clave de nicho + ciudad;
  - cuentas parecidas de las buenas;
  - perfil y últimas publicaciones de cada candidata.
- De 97 candidatas, 66 no estaban en el CRM ni entre las descartadas (`ex24.json`, 665 cuentas).
- **Cruce con el CRM:** `crm/state` desde una pestaña del admin, por Instagram y por número.
- **Anuncios:** en la Biblioteca de Meta, por frase exacta del nombre (`keyword_exact_phrase`), con el lector en `sessionStorage.r`. Sin bloqueos.
- **Webs:**
  - `r.jina.ai` desde su propia pestaña;
  - `/wp-json/wc/store/v1/products` (`x-wp-total`) y `/products.json`;
  - dns.google para los dominios que no existen.
  - Algunas webs (joyeriatena.es, joyasdelsur.com) dejan la pestaña colgada: se cierra y se mira con jina.

## Descartadas en la segunda vuelta

Ya venden online con una tienda de verdad, son franquicias, solo publican fijo o no tienen tienda física: casi todas las joyerías y perfumerías grandes que anuncian, y la mayoría de las tiendas de suplementos.

## Archivos

| Archivo | Qué hace |
|---|---|
| `mkleads.py leads.json` | 19 del lote anterior + 17 nuevas, con el día de cada una |
| `mkrows.py leads.json rows23b.js` | `SEED6_KEY`/`SEED6` |
| `patch_s23b.py <worker con SEED6 del 21/11> rows23b.js <salida>` | cambia las dos líneas del SEED6 |
| `t_s23b.mjs` | 25 comprobaciones, con `d1shim.mjs` y `w23mod.mjs` (la copia del worker con `export {…}`) |

Admin del Mac con la huella d9577e3d979769f1. La copia de antes está en `anterior/worker-seed23-22nov-antes-seed23b.js`.

## Lote 42 (22/11/2026): propuestas

- 33 con propuesta v42. Fuera: Más que Divas (réplicas), TJ Moda y Calzado (cierra) y Modas Carisma (ya vende en Shopify).
- La Platería del Sur es de Jerez (C. Fresa, 2): pasa al jueves 26. Crisly Coquette es de Motril.
- `mkrows.py leads.json rows42.js ../l33/sel42.json` y `patch_l42.py`; prueba `t_l42.mjs` (A y B).
