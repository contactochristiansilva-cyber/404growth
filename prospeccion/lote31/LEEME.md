# Propuestas de tienda online · lote 31 (3/11/2026)

Generador de las propuestas `404growth.com/p/<slug>/` con el formato del lote 30 (tienda demo con home, ficha de producto, diagnóstico, captación, plan de 15 días y cierre). Todas las fotos de la tienda las hace Apimart (Nano Banana Pro, `gemini-3-pro-image-preview`, 2K, 0,02 $ por imagen) a partir de los productos reales de su Instagram.

## Carpeta de trabajo

Se trabaja en una carpeta con esta forma (no está en el repositorio):
`tools/` (estos scripts), `tpl/lola_parts.json` (CSS y scripts de la plantilla del lote 30), `src/l31/<slug>/NN.jpg + logo.jpg + meta.json` (Instagram), `ai/<slug>/*.jpg` (Apimart), `logos/<slug>.png`, `out/` (lo que se publica) y `shots/` (capturas de revisión).

La clave de Apimart va en `tools/.ak` (sale de `~/Downloads/apimart-key.txt/api apimart.docx`). Nunca se sube al repositorio ni se imprime.

## Pasos

1. **Instagram:** `igdl.py <tab> <slug:handle> …` crea el lote de Chrome; cada perfil descarga sus 24 últimas fotos, el logo y `meta.json` a Descargas (`l31__<slug>__NN.jpg`).
2. **Imágenes:** `jobs_all.py <slug>` escribe `ai/jobs_<slug>.json` (15 por tienda: hero, p1–p5, x1–x3 de la ficha, look, l1–l4 categorías y l5 banner) y `runjobs.py <json> 10` las genera (salta las que ya existen). `aisheet.py` hace una hoja para revisarlas.
   - **Con rejillas (desde el 4/11/2026, lo normal):** `jobs_all.py --rejilla <slug>` saca las mismas 15 fotos en **6 llamadas**: hero, l5 y look sueltas, y tres rejillas 2x2 a 2K (`ficha` = p1, x1, x2, x3 del mismo producto; `productos` = p2–p5; `categorias` = l1–l4). `runjobs.py` corta cada rejilla (`gridsplit.py`, calles negras) en `ai/<slug>/<id>.jpg`, así que `gen.py` no cambia. Cada trozo sale de unos 910×1140 y la página publica a 1100 px como máximo: no se pierde nada. Coste: 0,12 $ por tienda en vez de 0,30 $. Si en el log sale `¡REVISAR!` (no encontró la calle) o un trozo no se parece al producto, se rehace solo esa foto suelta (0,02 $).
   - **Rejilla 3x3 (lote 32):** `jobs_lib.GRID = 3` junta p1, x1–x3, p2–p5 y look en una sola rejilla 3x3 a 4K (trozos de ~1200×1500) y deja las categorías en 2x2: 4 llamadas y **0,09 $ por tienda**. Probado el 4/11 con brilla-fashion: igual de fiel salvo detalles pequeños (un lazo burdeos salió negro). `run32.py <slug> …` lo hace todo: encargos, imágenes, página y capturas.
   - **Higgsfield** (créditos gratis; Nano Banana Pro a 2K: la consulta de precio dice 2 créditos, pero la prueba del 4/11 descontó 3,5): ni este contenedor ni la terminal del Mac llegan a sus servidores, así que va por las herramientas de Higgsfield y Chrome. Referencias con `media_import_url` usando las URL de Instagram de `src/l31/<slug>/meta.json` (caducan a los ~4 días), el mismo `prompt` del `jobs_<slug>.json` en `generate_image` (`nano_banana_pro`, `4:5`, `2k`), el resultado se abre en una pestaña y se descarga con `fetch` + `<a download>` a Descargas como `hf__<slug>__<grupo>.png`, y se corta con `gridsplit.py hf__….png ai/<slug>/ p1 x1 x2 x3`.
3. **Logos:** `logos.py` recorta el logo de su perfil a PNG transparente; si es una foto, se usa un logotipo de texto (`logo=dict(text=…)` en `shops.py`).
4. **Datos:** `shops.py` (solo datos reales: dirección, seguidores, precios si los publican, pies de foto literales) y `niches.py` (textos por nicho: moda, joya, obrador, deco).
5. **Página:** `gen.py <slug>` → `out/p-<slug>.html` + `p-<slug>--b--*.jpg` + `--b--og.jpg`; `shots.py <slug>` → `--antes.jpg` (su Instagram de hoy), `--despues.jpg` (la tienda) y capturas a 1440 y 390 px.
6. **Publicar:** copiar `out/` a `~/Downloads/web117-404growth/`, añadir `/p/<slug>/ /p-<slug> 200` (y sin barra) a `_redirects`, y Chris ejecuta `subir.command`.
7. **CRM:** en cada ficha, `slug` y `pageUrl` = `https://404growth.com/p/<slug>/`; con eso entran en «Lote de hoy».

Los botones de la propuesta van a `404growth.com/book?utm_source=propuesta&utm_campaign=<slug>` y a WhatsApp; el contador de visitas es el mismo del lote 30 (con el slug de cada página).

## Lote 32 (4/11/2026)

- 30 tiendas del CRM (lote del 4/11). Fotos de Instagram con `igdl.py` (más rápido: la función se guarda en `localStorage.__igdl` de la pestaña de Instagram y cada tienda es navegar + `await (eval(localStorage.getItem('__igdl')))('<slug>')`), comprimidas en un zip en Descargas y pasadas a `src/l31/<slug>/`.
- `igsheet.py <slug>` hace la hoja de contacto de sus 24 fotos (`l32/sheets/`). Los datos del scrapeo están en `l32/data.json`.
- Cada tienda tiene dos archivos en `l32/entries/`: `<slug>.jobs.py` (encargos) y `<slug>.shop.py` (textos y datos); `jobs_all.py` y `shops.py` los cargan solos. `check32.py <slug>` comprueba sin gastar que todo monta. Las instrucciones que se siguieron para escribirlos están en `l32/BRIEF.md`.

### Revisión antes de publicar (lote 32)

1. `aisheet32.py <slug>`: hoja con las 15 fotos de IA.
2. `cmpref.py <slug>`: cada encargo con sus referencias al lado. Si una cara se parece a la de la dueña o su equipo, `topcrop.py <slug> p1=.07 look=.19 …` la recorta a la altura de los labios.
3. Heroes: que no salgan como pantalla partida.
4. Banner (l5) con gente parecida a la dueña o hecho collage: se rehace sin referencias, solo con el texto del prompt y «No people at all».
5. `gen.py` + `shots.py` otra vez y se revisan las capturas.

## Hecho el 6/11/2026

- Publicadas 5 más (fotos en Flow, gratis): **todo-textil**, **flag-sevilla**, **tartaisa**, **delia-nunez** (es @flamencapolnunez: delianunez.com tiene la tienda PrestaShop montada pero vacía) y **studio-vintage**. Correos visuales en `e/<slug>/`, borradores de Flag, Delia Núñez y Studio Vintage en Gmail (hola@) y hoja `~/Downloads/envios-5-6nov.html`. Todo Textil no tiene correo ni teléfono: solo Instagram.
- Del CRM (7 con +20k sin propuesta) quedaron fuera, con su «AVISO (6/11)» en las notas: Samsara (WooCommerce con 541 productos), Morueco (Shopify con 250+ productos y cesta), Cocoon (PrestaShop con cesta), Mundo Alopeke (escuela infantil, no tienda) y Dekopalace (cerró a finales de 2023: liquidación y despedida en Instagram).
- Todo Textil, Flag Sevilla y Delia Núñez entran al CRM con el `SEED` del admin (`seed_20261106a`); Tartaisa y Studio Vintage ya estaban y se les puso `slug` y `pageUrl`.
- Flag Sevilla: celebraban sus 10 años el 5/11; mejor escribir a partir del lunes 9 (sale en la hoja).

## Pendiente (5/11/2026, para seguir)

- De las 24 del día, hechas 9 (Mumbai, Corazón, De Rosa, Estela, Mono Mona, Provenza, Punto y Aparte, Quattro y Raza), y el 6/11 las 5 de arriba.
- Descartadas el 5/11 por vender ya online: tacatucazaragoza, mamasitasmoda2024, impulsomodasgranada, anacamposcollection, aires_desoniaycris, princessnatalia_modas, ottro_shop, latiendadeluca, belaobisuteria, rafimora_huelva, belove.es, saroemmoda, bravebetty_moda (y atelier.badajoz, con la web en mantenimiento).
- Búsqueda que mejor ha ido: Yahoo con `site:instagram.com <ciudad> ("Bizum" OR "pedidos por WhatsApp" OR "pedidos por MD" OR "pedidos por privado") ("20K Followers" OR … OR "30K Followers")` (los OR, entre paréntesis) y las «Cuentas similares» de Instagram de las tiendas que ya tenemos. Yahoo deja de responder tras unas 60 búsquedas seguidas.
