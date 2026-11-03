# Propuestas de tienda online · lote 31 (3/11/2026)

Generador de las propuestas `404growth.com/p/<slug>/` con el formato del lote 30 (tienda demo con home, ficha de producto, diagnóstico, captación, plan de 15 días y cierre). Todas las fotos de la tienda las hace Apimart (Nano Banana Pro, `gemini-3-pro-image-preview`, 2K, 0,02 $ por imagen) a partir de los productos reales de su Instagram.

## Carpeta de trabajo

Se trabaja en una carpeta con esta forma (no está en el repositorio):
`tools/` (estos scripts), `tpl/lola_parts.json` (CSS y scripts de la plantilla del lote 30), `src/l31/<slug>/NN.jpg + logo.jpg + meta.json` (Instagram), `ai/<slug>/*.jpg` (Apimart), `logos/<slug>.png`, `out/` (lo que se publica) y `shots/` (capturas de revisión).

La clave de Apimart va en `tools/.ak` (sale de `~/Downloads/apimart-key.txt/api apimart.docx`). Nunca se sube al repositorio ni se imprime.

## Pasos

1. **Instagram:** `igdl.py <tab> <slug:handle> …` crea el lote de Chrome; cada perfil descarga sus 24 últimas fotos, el logo y `meta.json` a Descargas (`l31__<slug>__NN.jpg`).
2. **Imágenes:** `jobs_all.py <slug>` escribe `ai/jobs_<slug>.json` (15 por tienda: hero, p1–p5, x1–x3 de la ficha, look, l1–l4 categorías y l5 banner) y `runjobs.py <json> 10` las genera (salta las que ya existen). `aisheet.py` hace una hoja para revisarlas.
3. **Logos:** `logos.py` recorta el logo de su perfil a PNG transparente; si es una foto, se usa un logotipo de texto (`logo=dict(text=…)` en `shops.py`).
4. **Datos:** `shops.py` (solo datos reales: dirección, seguidores, precios si los publican, pies de foto literales) y `niches.py` (textos por nicho: moda, joya, obrador, deco).
5. **Página:** `gen.py <slug>` → `out/p-<slug>.html` + `p-<slug>--b--*.jpg` + `--b--og.jpg`; `shots.py <slug>` → `--antes.jpg` (su Instagram de hoy), `--despues.jpg` (la tienda) y capturas a 1440 y 390 px.
6. **Publicar:** copiar `out/` a `~/Downloads/web117-404growth/`, añadir `/p/<slug>/ /p-<slug> 200` (y sin barra) a `_redirects`, y Chris ejecuta `subir.command`.
7. **CRM:** en cada ficha, `slug` y `pageUrl` = `https://404growth.com/p/<slug>/`; con eso entran en «Lote de hoy».

Los botones de la propuesta van a `404growth.com/book?utm_source=propuesta&utm_campaign=<slug>` y a WhatsApp; el contador de visitas es el mismo del lote 30 (con el slug de cada página).
