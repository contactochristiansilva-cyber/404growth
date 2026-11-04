# Envíos de las propuestas (correo visual, captura para WhatsApp y hoja del día)

En la sesión se trabaja con esta estructura: `<base>/l31` (= `prospeccion/lote31`) y `<base>/l33` (esta carpeta).
Hace falta la página ya generada en `l31/out/p-<slug>.html` y un servidor local en `l31/out` en el puerto 8733.

1. `node cap_mail.js <slug>...` → `mail/<slug>.png`: la propuesta v33 a 600 px de ancho (x2), sin animaciones y con los 6 anuncios en 2 columnas.
2. `python3 mail33.py <slug>...` → la corta en trozos `e/<slug>/NN.jpg` (van a `web117-404growth/e/<slug>/` y se publican en `404growth.com/e/<slug>/NN.jpg`), escribe el cuerpo `mail/<slug>.html` y `mail/index.json` (para y asunto). Botones a `/book?utm_source=email&utm_medium=prospeccion&utm_campaign=<slug>`.
3. `node cap_phone.js <slug>...` → `wa/<slug>.png`: el móvil del inicio con su tienda, para adjuntar en WhatsApp e Instagram.
4. `python3 envios.py <slug>... [--pend <slug>...]` → `envios.html`: por tienda, captura, WhatsApp (variante A pide permiso, B lleva el enlace; se alternan), Instagram (siempre A) y correo (Abrir Gmail con para y asunto + Copiar correo, que copia el cuerpo con imágenes para pegarlo).

El conector de Gmail quita las imágenes externas del cuerpo, así que los correos se pegan en Gmail a mano desde la hoja.

## Borradores en Gmail (hola@404growth.com)

El conector de Gmail no sirve para estos correos: quita las imágenes externas y cambia los enlaces por redirecciones de Google (comprobado el 4/11/2026).
Se hacen en Chrome, en la redacción a pantalla completa de Gmail (`mail.google.com/mail/?authuser=hola@404growth.com&view=cm&fs=1&to=…&su=…`):
`draft_js.txt` (con `__P__` cambiado por `{s, sh, nm, no, n}`) arma el cuerpo y lo pega con un evento `paste` en el cuadro del mensaje
(`execCommand('insertHTML')` no funciona por Trusted Types). Gmail guarda el borrador solo en unos segundos; se esperan 8 s antes de pasar al siguiente.
