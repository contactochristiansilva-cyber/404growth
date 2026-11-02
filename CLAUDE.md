# 404 Growth: notas para Claude

## Animaciones y gráficos para vídeo (DaVinci Resolve gratis, Mac)

Cualquier animación, título o gráfico con fondo transparente se entrega SIEMPRE así:

- **Formato:** `.mov` con códec **PNG** y transparencia (es el único que ha funcionado en el DaVinci de Christian).
  ```bash
  ffmpeg -framerate 25 -i frames/%04d.png [-i sonido.wav] \
    -c:v png -pix_fmt rgba [-c:a pcm_s16le -shortest] salida.mov
  ```
  No entregar ProRes 4444 con alpha como archivo principal: en su DaVinci no quita el fondo.
- **Resolución y fps:** 1080×1920 (9:16), 25 fps.
- **En DaVinci:** pista por encima del vídeo, Clip Attributes → Alpha Mode: **Straight**.
- Si lleva efecto de sonido, va dentro del mismo `.mov` (PCM) y también como `.wav` suelto.
- Comprobar antes de enviar que el fondo es alpha 0 (`alphaextract`) y mandar una prueba `.mp4` montada sobre su plano.

## Estilo de subtítulos y gráficos de los ads

- Siempre una sola línea centrada, de 4–5 palabras como máximo. Nunca varias líneas apiladas.
- Letra Inter fina (400 o 300). Cuando se ve a Christian, en blanco y sin verde.
- El verde 404 (degradado #7FD3B6 → #2E7A64) solo en alguna palabra muy importante y sobre fondo blanco.
- Espaciado ancho entre palabras: el de los espacios de Noto Color Emoji, con las letras en Inter.
- Sombras mínimas: nada de sombras difusas grandes que se vean como un fondo.
- Minimalista, sin sobrecargar.

## Vídeos de /metodo (página que se envía tras reservar)

- Archivo: `web117-404growth/metodo.html`. Los 8 vídeos están en el array `V` del script: `src`, `poster` y `dur` (duración real, «4:32»). Sin `src`, la tarjeta sale como «Muy pronto».
- Cloudflare (assets del Worker) no acepta archivos de más de 25 MB: cada vídeo se publica en **HLS** dentro de `web117-404growth/v/metodo/0N/` (vertical 720×1280, segmentos de 6 s). Safari lo reproduce solo; el resto usa `/v/hls.light.min.js` (hls.js 1.5.20, ya incluido).
  ```bash
  ffmpeg -i entrada.mov -vf "scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280" \
    -c:v libx264 -preset veryfast -crf 23 -maxrate 1800k -bufsize 3600k -g 50 -keyint_min 50 -sc_threshold 0 \
    -c:a aac -b:a 96k -ac 2 -hls_time 6 -hls_playlist_type vod -hls_segment_filename "v/metodo/0N/s%03d.ts" v/metodo/0N/index.m3u8
  ffmpeg -ss 2 -i entrada.mov -frames:v 1 -vf "scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280" -q:v 3 v/metodo/0N/poster.jpg
  ```
- Enlace personal: `404growth.com/metodo?c=<id del lead>`. Va solo en la invitación de Google al reservar; en el admin › Landing (la ficha de cada visita que reservó) hay botones para mandarlo por WhatsApp o email. La página avisa a Chris cuando el lead la abre y cuando termina cada vídeo, y esa ficha muestra cuántos ha visto. (La página /admin/llamadas ya no existe.)

- **Formato de los vídeos (desde el vídeo 1):** como el Ad 3. Intro a cámara en plano completo y después 50/50 hasta el final: Chris arriba (webcam, 1080×840) y abajo una pizarra tipo Miro en vídeo 1:1 (1080×1080, 25 fps, sin sonido) que él narra mientras la ve. Las pizarras se generan con `ads/metodo-pizarra/` (vídeo 1: `board.html`; vídeos 2–8: `motor/`, ver `LEEME.md`). Se entrega solo la pizarra limpia (sin franja de guion), PNG sin pérdida → x264 veryslow CRF 18. Los guiones (intro a cámara + frases con tiempo) están en el doc «Guiones de /metodo · cámara + pizarra».

## Ficha de arranque (llamada de arranque con cada cliente)

- `/admin/arranque/<id del cliente>` (botón «Ficha de arranque» en Clientes). Se comparte en pantalla en la llamada y se guarda sola, campo a campo.
- Los campos están en `ficha` (7 apartados, 38 campos) dentro de `PAGES.kick` y del portal: usa las claves del brief que ya existían (b_name, o_main, a_who…) y las suyas `k_…` (lista `KICK` en worker.js), todas en `clients.brief`.
- El cliente la ve en su portal, en Onboarding → Bienvenida, como «Lo que hablamos en la llamada de arranque» (solo lectura).

## Alta del cliente por su cuenta (/onboarding) y llamada de arranque

- `404growth.com/onboarding` (ruta del Worker del admin; está en `wrangler.jsonc`): el cliente pone sus datos, su tienda y su contraseña, y entra directo a `/portal`. Crea el cliente (`clients.self = 1`, `clients.contact`) y su usuario. Freno: 5 altas al día por sitio y un campo oculto para bots. Avisa a Chris en cada alta.
- En el Inicio del portal agenda su **llamada de arranque** (60 min, `KICK_MIN`): dos medias horas libres seguidas de `gbSlots`, evento en Google con Meet (`gbCreate`), se guarda en `clients.kcall` y, si no tenía, pone el día de arranque (empiezan sus 15 días).

## Portal del cliente: contrato y facturas, y el chat (v47)

- **Contrato y facturas** (vista `docs` del portal; en el admin, pestaña «Contrato y facturas» de cada cliente). El contrato es un PDF que Chris sube ahí (hasta 1,8 MB, tabla `cdocs` en D1); no se sustituye: las versiones anteriores siguen descargables hasta que las quite. Las facturas son las de Facturación con ese `client_id` y salen solas (`invPdf`). Descargas: `/portal/api/docs/<id>` y `/portal/api/invoices/<id>/pdf` (solo las suyas).
- **Chat «Pregúntame»** (botón flotante del portal; en el admin, pestaña «Chat del portal»). Contesta una IA con el criterio de Chris (`pchatAI`, la clave de Anthropic de LinkedIn y blog): sabe `BOT_FACTS`, lo que Chris escribe en «Tu cerebro» (meta `bot_brain`, común a todos y manda sobre lo demás) y el estado de ese cliente (`pchatCtx`). Nunca dice que es Chris. Lo que no sabe seguro, o si piden cambiar precio, pagos, contrato o plazos, quejas o urgencias: se lo pasa a Chris (aviso push + chip en Clientes) y él contesta desde el admin. Tabla `pchat` (`esc` 1 = espera a Chris, 2 = ya contestó). Límite: 40 mensajes al día por cliente.
- `portalView` da `who` (el nombre de la persona del cliente); `contact` es el de Chris (WhatsApp de los botones).

## Formulario de /book (landing VSL)

- Si marcan «Menos de 1.500 €» (`bud = b0`) no avanza: sale el mensaje de que con esas cantidades no trabajamos y que, si fue un error, pueden elegir otra opción. El Worker también rechaza `b0` (`vslBook` → 422 `budget`).
