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
   - **Higgsfield** (créditos gratis; Nano Banana Pro a 2K = 2 créditos, a 4K = 4): ni este contenedor ni la terminal del Mac llegan a sus servidores, así que va por las herramientas de Higgsfield y Chrome. Referencias con `media_import_url` usando las URL de Instagram de `src/l31/<slug>/meta.json` (caducan a los ~4 días), el mismo `prompt` del `jobs_<slug>.json` en `generate_image` (`nano_banana_pro`, `4:5`, `2k`), el resultado se abre en una pestaña y se descarga con `fetch` + `<a download>` a Descargas como `hf__<slug>__<grupo>.png`, y se corta con `gridsplit.py hf__….png ai/<slug>/ p1 x1 x2 x3`.
3. **Logos:** `logos.py` recorta el logo de su perfil a PNG transparente; si es una foto, se usa un logotipo de texto (`logo=dict(text=…)` en `shops.py`).
4. **Datos:** `shops.py` (solo datos reales: dirección, seguidores, precios si los publican, pies de foto literales) y `niches.py` (textos por nicho: moda, joya, obrador, deco).
5. **Página:** `gen.py <slug>` → `out/p-<slug>.html` + `p-<slug>--b--*.jpg` + `--b--og.jpg`; `shots.py <slug>` → `--antes.jpg` (su Instagram de hoy), `--despues.jpg` (la tienda) y capturas a 1440 y 390 px.
6. **Publicar:** copiar `out/` a `~/Downloads/web117-404growth/`, añadir `/p/<slug>/ /p-<slug> 200` (y sin barra) a `_redirects`, y Chris ejecuta `subir.command`.
7. **CRM:** en cada ficha, `slug` y `pageUrl` = `https://404growth.com/p/<slug>/`; con eso entran en «Lote de hoy».

Los botones de la propuesta van a `404growth.com/book?utm_source=propuesta&utm_campaign=<slug>` y a WhatsApp; el contador de visitas es el mismo del lote 30 (con el slug de cada página).
