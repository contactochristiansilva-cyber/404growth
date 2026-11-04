# Lote 32 · fichas de tienda para las propuestas de 404 Growth

Base: `/tmp/claude-0/-home-claude/86561a8c-5895-52c1-874b-e63866019285/scratchpad/l31` (abajo, `$B`).

404 Growth (Chris) convierte tiendas físicas en tiendas online. A cada tienda le enviamos una propuesta: una página `404growth.com/p/<slug>/` con una tienda online de demostración hecha con SUS productos (fotos generadas con IA a partir de sus fotos reales de Instagram), su diagnóstico y el plan de 15 días. El generador ya existe y funciona (lote 31, 20 tiendas publicadas el 3/11). Tu trabajo es escribir, para cada tienda que te toque, las dos piezas de datos que necesita el generador. No generes imágenes ni gastes créditos.

## Qué tienes por tienda

- `$B/l32/sheets/<slug>.jpg`: hoja con sus 24 últimas fotos de Instagram, numeradas 01–24 (= `$B/src/l31/<slug>/NN.jpg`, a resolución completa; ábrelas con Read si necesitas ver un detalle).
- `$B/src/l31/<slug>/meta.json`: `header` (la cabecera de su perfil: nombre, seguidores, bio, enlaces) y `posts[].alt` (texto alternativo de cada foto, en el mismo orden 01–24; a veces trae el pie de foto literal, a veces es automático).
- `$B/l32/data.json` → `[<slug>]`: lo que ya comprobamos en el scrapeo: nombre, handle, seguidores, ciudad, dirección, `store` (none = sin web, weak = web floja), `fails` (qué falla, comprobado), teléfono, web, nº de tiendas, notas.

## Qué escribes (dos archivos por tienda)

1. `$B/l32/entries/<slug>.jobs.py`: una sola sentencia `S['<slug>'] = lambda s: build(s, ...)`, con el mismo formato que las del lote 31 en `$B/tools/jobs_all.py` (léelo entero: tiene ejemplos de moda, joyería, obrador y deco). Los prompts, en inglés, como allí.
2. `$B/l32/entries/<slug>.shop.py`: una sola sentencia `mk('<slug>', ...)`, con el mismo formato que las del lote 31 en `$B/tools/shops.py` (léelo entero; para obradores se usa `**OB`, mira `pasteleria-zoya`; para joyería, `joyeria-ferrezuelo`). Textos en español de España, hablando a la tienda de vosotros.

Comprueba cada tienda con `cd $B/tools && python3 check32.py <slug>`: tiene que imprimir 6 encargos sin «FALTA REF» y `ok <slug> … placeholders []`. Si falla, corrige y repite.

Si una tienda no sirve, no escribas sus archivos: crea `$B/l32/entries/<slug>.DESCARTE.txt` con el motivo en una línea. Motivos válidos: las fotos de producto son muy malas (movidas, pixeladas, oscuras) y no hay otras mejores suyas; o en sus 24 fotos no hay al menos 5 productos distintos y reconocibles que se puedan vender online.

## Cómo elegir las fotos (encargos de imagen)

Las 15 fotos de la tienda salen de `build(...)`: hero, p1–p5 (productos), x1–x3 (ficha del p1: vista e-commerce, foto de ambiente y detalle macro), look (shop the look, 2 prendas), l1–l4 (categorías) y l5 (banner ancho). Se generan en rejillas de 4, así que:

- Cada hueco, con un producto DISTINTO y una referencia distinta. Nada de la misma foto con otro zoom ni el mismo producto repetido en huecos cercanos (Chris lo pide expresamente). Excepción: x1–x3 son el mismo producto que p1, a propósito.
- Para p1 elige su producto más vistoso y con la foto más clara (es la ficha de producto).
- Referencias: las fotos más nítidas y donde el producto se ve entero. Un selfie en el espejo vale (el prompt ya lo limpia). Evita fotos con mucho texto encima tapando el producto.
- Describe cada producto con precisión (color, tejido, estampado, forma), porque la IA tiene que reconocerlo y no inventar otro.
- hero: una escena de campaña con su mejor producto en un sitio reconocible de SU ciudad (como en el lote 31), sujeto a la derecha. l5: el interior de su tienda si hay foto (como referencia), o una escena amplia que tenga sentido para su negocio.
- Lencería: solo producto, sin modelos (usa la forma `(n, 'desc', 'obj')` en productos y prompts de producto sin personas en el resto). Zapatillas y bolsos: también `'obj'`.
- Obradores: producto apetecible sobre fondo limpio; x1 cenital con espacio alrededor; x2 en una mesa de celebración o desayuno; x3 macro de textura.
- Joyería: fondo blanco o muy claro, nunca oscuro.
- Fondo de estudio (`bg` de `build`): un tono claro que case con su marca, con su hex, como en los ejemplos.

## Cómo escribir los textos (`mk`)

- **Solo datos reales.** Nada inventado: ni cifras, ni años, ni premios, ni opiniones. Si un dato no está en `data.json`, su bio, sus pies de foto o la foto misma, no se pone. Analiza bien qué tienen y qué no antes de afirmar nada (a Chris le aleja de un cliente decir algo falso de su negocio). `web_state`: 'none' (sin web), 'weak' (con `web_note` que diga exactamente lo comprobado en `fails`) o 'down' (web caída, con `domain`).
- **Precios:** solo si los publican (pie de foto o bio). Si no, no pongas `price`.
- **`quotes`:** 3 frases literales suyas (de la bio o de pies de foto en `alt` que sean texto suyo, no la descripción automática «Photo by…/May be an image of…»), con `'@<handle>'`. Si no hay 3 literales, usa menos o frases literales de la bio.
- **Logo:** si existe `$B/logos/<slug>.png`, `logo=LG('<slug>')`. Si no, logo de texto `logo=dict(text='…', sub='…', fs=…, ls='…', fw=…)` como `mv-laspalas` o `pasteleria-zoya`.
- **Colores:** `colors=dict(t='#…', cream='#…')` sacados de su marca (logo, fotos, bio). Joyería: claro.
- `nav` y `cats`: categorías que de verdad venden (por lo que se ve en sus fotos). `prods[].name`: nombres cortos y concretos en español. `crumb` solo en p1.
- `kpis`: 4, como en los ejemplos (seguidores reales en K, algo suyo real, lo de la web real y «24/7»). `diag.assets`: 2 datos reales suyos.
- `sub`, `diag.h2`, `diag.p`, `hero.h4`, `ads`: cortos, potentes, sin relleno ni frases «de IA». Mira cómo están escritos los del lote 31 y mantén ese nivel.
- Dirección, teléfono, nº de tiendas: de `data.json`. Si la dirección no tiene calle, no la inventes.

Al acabar, contesta con una línea por tienda: `slug: ok` (y qué referencias usaste para p1 y el hero) o `slug: DESCARTE (motivo)`, y cualquier duda real que haya que revisar.
