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

## Lo que se aprendió el 6/11/2026

- **Subir referencias:** el clic de «Subir archivo…» se captura con el `click` parcheado (`__fi`), pero ese input solo vale para una subida: antes de cada subida nueva hay que volver a pulsar «Subir archivo…». Las rutas que acepta la subida son las de la sesión (`/mnt/user-data/uploads/…`, lo que se ha traído del Mac), no las del Mac.
- **Pegar el mensaje:** el cuadro del agente es un `div` editable; `document.execCommand('insertText')` funciona (el `paste` simulado no siempre).
- **Descargar sin el menú:** en la vista de una imagen (clic en la imagen y flecha derecha para pasar), la miniatura de la derecha es `flow.google.com/…=s512-rw?authuser=1`; cambiando `=s512-rw` por `=s1600` se baja la imagen entera (896×1200 en 3:4, 1376×768 en 16:9). `__dl(slug)` reconoce la foto por su clave (`__K`) y la baja como `<slug>__<id>.jpg`; las referencias las salta solas.
- **Errores de política:** fallan a veces sin motivo y al repetirlas (solo las que faltan, con `sub.py <slug> id,id`) suelen salir. En Tarta Isa falló «wine glasses» en una mesa de celebración: con «crystal water glasses» salió.
- **Nunca referencias con menores:** Flow no deja subir fotos con niños (y no se usan). En Delia Núñez la 22 y la 19 eran niñas: se cambió la 22 por la 23 y el banner va solo con la 16.
- **Caras:** en Delia Núñez, el «look» copió la cara, el sombrero y la puerta de la foto 15: se recortó con `topcrop.py delia-nunez look=0.355`.
- El nicho `deco` de `jobs_lib` está pensado para cerámica («ceramic pieces»); para muebles (Studio Vintage) se cambió esa frase en el mensaje por «furniture and design pieces».
- Se pueden llevar varias tiendas a la vez, cada una en su pestaña y su proyecto.

## Lo que se aprendió el 6/11/2026 por la tarde (14 tiendas de moda en paralelo)

- **Varias tiendas a la vez:** un proyecto por pestaña. Con más de 4 o 5 generaciones a la vez, Flow contesta «Hay demasiadas generaciones en curso» (o «Hemos detectado actividad inusual»): se espera un minuto y se pulsa «Reintentar», que deja el mensaje otra vez en el cuadro; hay que volver a enviarlo.
- **Ayudas en la pestaña:** `ayudas_flow.js` guarda en `localStorage.__fc` (de flow.google.com) `__attach`, `__put`, `__mkin`/`__xfer` (subir referencias), `__dl`, `__dlall`, `__findl` y `__dlid`. Cada tienda carga `P_<slug>.js` (claves `__K` y mensajes `__M`, que también se guardan en `localStorage['__P_<slug>']`).
- **Ajustes del agente** (Confirmar «Nunca», 3:4, x1): son de cada proyecto; se ponen en cada uno.
- **Descargar:** en la vista de una imagen, `__dlall(40)` va al principio con la flecha izquierda y recorre todas hacia la derecha bajando la imagen grande (`flow-content.google`, la de mejor calidad). Si la grande no carga, baja la miniatura `=s1600`. Solo funciona bien con la pestaña **delante**: en segundo plano Chrome frena los temporizadores y no carga las imágenes. Se bajan de una en una pestaña.
- **Claves repetidas:** si la clave de una foto aparece también en el texto de otra («a model wearing the lo…» vale para «long» y «loose»), `__dlall` la salta. `final.py` ya busca claves que solo estén en su foto; si aun así falta una, se abre y se baja con `__dlid('<id>')`.
- **Agente atascado:** a veces contesta «Voy a generar…» y solo escribe etiquetas `<gflux_tool_call>` sin generar nada. Se abre una sesión nueva del agente (icono de arriba del panel) y se manda otra vez.
- **Referencias que no sube o que bloquean el mensaje:** se recorta la prenda sin la cara (Café con Bacon 23 → `23c.jpg`) o se cambia el producto (Modas Jade: la sudadera con dibujo bloqueaba todo el mensaje; se cambió por la parka, `17c.jpg`).
- `file_upload` no acepta más de 10 MB por llamada: las referencias de más de 700 KB se reducen a 1600 px.
- En el Mac, `~/org2.py <slug>` (en el $HOME del Cowork) mueve `~/Downloads/<slug>__<id>*.jpg` a `flow-out/<slug>/<id>.jpg` quedándose con la más grande.
