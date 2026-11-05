# Fotos gratis con Google Flow (5/11/2026)

Cuando Apimart no tiene saldo, las 15 fotos de cada propuesta se hacen gratis en **Google Flow** (flow.google.com, cuenta hola@ = `/u/1`), con su agente y el modelo **Nano Banana 2.1**. Así se hicieron las 9 del 5/11/2026 (Mumbai, Corazón, De Rosa, Estela, Mono Mona, Provenza, Punto y Aparte, Quattro y Raza).

## Cuotas

- **Nano Banana Pro:** unas 20 imágenes al día por cuenta; al pasarse sale «Has alcanzado el límite de cuota diaria…». Se cambia a 2.1 diciéndoselo al agente («Usa Nano Banana 2.1»); 2.1 es además el modelo por defecto en los ajustes.
- **Nano Banana 2.1:** rápido (5 imágenes en 40–60 s). Con la misma calidad en la página.
- La cuenta personal (`/u/0`) pide aceptar el alta de Flow: eso lo hace Chris (aceptar condiciones no lo hace Claude). Lo mismo con «Permitir varias descargas» en Chrome.

## Paso a paso (por tienda)

1. `python3 msgs.py <slug>` → `<slug>.json`: las 15 fotos de `jobs_all` en 3 mensajes (5 por mensaje, con sus referencias). `python3 keys.py <slug> > <slug>.keys.json` y `python3 final.py <slug>` → `<slug>.final.json` (Pro → 2.1, fuera el «Category photo 'X':», que hace que escriba la palabra en la foto, y «no words or labels anywhere in the image»).
2. En Flow, un proyecto por tienda. Ajustes del agente: Confirmar «Nunca», 3:4, x1. Se suben las referencias («Subir archivo») y se manda cada mensaje. `boot.py <slug> <prefijo>` da el JS de ayuda para la pestaña (`__attach`, `__ren` para poner a cada imagen el nombre `<slug>__<id>`, `__pos`).
3. Descarga a 2K («Resolución mejorada 2K» en el menú de descarga de la vista de edición; la flecha derecha pasa a la siguiente). En el Mac, `org.sh <slug>` mueve `~/Downloads/<slug>__<id>_…_2K.jpg` a `~/Downloads/flow-out/<slug>/<id>.jpg`.
4. `python3 post.py <slug> <carpeta>` recorta y escala al tamaño del generador (`ai/<slug>/`). **Ojo:** sobrescribe los recortes de cara: repetir `tools/topcrop.py` después.
5. `python3 sheet.py <slug>` (referencias frente a resultado) para revisar prendas y caras; si alguna cara se parece a la dueña, `topcrop.py <slug> <id>=<fracción>`.

## Lo que se aprendió

- Si una referencia muestra personas, a veces Flow da error de política: usar recortes solo del producto o pedir la foto sin referencia.
- Si dos fotos comparten la misma clave, `__ren` no sabe cuál es: esas se renombran a mano en el Mac.
- Hay que esperar a que termine cada descarga antes de cambiar de imagen; si falta alguna, se vuelve a bajar desde la cuadrícula.
