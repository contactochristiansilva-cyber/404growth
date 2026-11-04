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
- Cloudflare (assets del Worker) no acepta archivos de más de 25 MB: cada vídeo se publica en **HLS** dentro de `web117-404growth/v/metodo/0N/`, con dos calidades: `1080/` (1080×1920, CRF 21) y `720/` (720×1280, CRF 22), x264 `slow`, GOP de 2 s cerrado, segmentos de 4 s y audio AAC 128k. `0N/index.m3u8` es la lista maestra (1080 primero) y `0N/poster.jpg` el póster (720×1280). Safari lo reproduce solo; el resto usa `/v/hls.light.min.js` (hls.js 1.5.20) con `abrEwmaDefaultEstimate: 5e6`, para que empiece en 1080 si la conexión da. Los segmentos no van al repositorio (se quedan en el Mac).
- Los originales están en `~/Contenidos/Videos Metodo/Metodo N def.mov` (HEVC 10 bits). Se comprimieron el 4/11/2026 en el Cowork del Mac (las llamadas duran 180 s como máximo): por trozos de 60 s (los dos tamaños a la vez), uniéndolos con `concat -c copy` y troceando a HLS con `-c copy`. Con CRF 21 el SSIM frente al original es 0,993: no se nota. De 436 MB a 168 MB en 1080.
  ```bash
  # cada trozo K (de 60 s) del vídeo N
  ffmpeg -ss $((K*60)) -i "Metodo N def.mov" -an -filter_complex "[0:v]split=2[a][b];[a]format=yuv420p[a2];[b]scale=720:1280:flags=lanczos,format=yuv420p[b2]" \
    -map "[a2]" -frames:v 1500 -c:v libx264 -preset slow -profile:v high -g 50 -keyint_min 50 -sc_threshold 0 -crf 21 -maxrate 6000k -bufsize 12000k -level 4.0 cK_1080.mp4 \
    -map "[b2]" -frames:v 1500 -c:v libx264 -preset slow -profile:v high -g 50 -keyint_min 50 -sc_threshold 0 -crf 22 -maxrate 3000k -bufsize 6000k -level 3.1 cK_720.mp4
  # después, por calidad: concat de los trozos + audio (-c:a aac -b:a 128k) y
  ffmpeg -i v1080.mp4 -i a.m4a -map 0:v -map 1:a -c copy -f hls -hls_time 4 -hls_playlist_type vod -hls_flags independent_segments -hls_segment_filename "0N/1080/s%03d.ts" 0N/1080/index.m3u8
  ```
- **Página (v51, 4/11/2026):** portada corta (saludo y una línea) y debajo, enseguida, los 8 vídeos en orden (1→8), 2 columnas en el móvil y 4 en el ordenador; ya no hay vídeo «destacado». La tarjeta de la llamada (fecha, cuenta atrás, Meet, calendario) va después, junto a los 3 pasos.
- **Es también la página de gracias (v52):** al reservar, /book lleva a `/metodo?c=<lead>` (ya no a /gracias; `gracias.html` solo redirige a /metodo con el lead de `sessionStorage.c404bk`). Si viene de reservar en esa pestaña (`JB`), arriba sale «Llamada reservada», «Hecho, Ana. Nos vemos … a las …» y el aviso de aceptar la invitación del correo. Esa primera visita automática se manda con `fr: 1` y el Worker no avisa a Chris (avisa la primera vez que la abre él desde la invitación y cuando vuelve tras 6 h). Hueco del **vídeo de gracias** (`TY` en el script): cuando exista, se comprime como los otros en `v/metodo/00/` y se pone `src`/`poster`; sale arriba (a la derecha en el ordenador, debajo del aviso en el móvil) sin sonido y en bucle con «Activar audio», y al tocarlo empieza desde el principio con sonido.
- **Portada (v53):** si sabemos la hora de la llamada (por la reserva de esa pestaña o por `?c=`): check animado (círculo que se dibuja y check), «Ana, tu llamada está confirmada.», el día y la hora con el calendario pequeño (y la hora local si no está en España) y, solo recién reservado, una línea para aceptar la invitación del correo. Debajo, la frase «Justo debajo tienes las 8 dudas que más nos preguntan, resueltas en vídeo» con flecha a los vídeos. Con `?c=` y sin datos aún, la portada espera (hasta 1,5 s) a tener nombre y hora para no parpadear. En el móvil, `fitTy()` ajusta el ancho del vídeo de gracias para que él y la frase quepan en la primera pantalla.
- **Tarjetas y miniaturas:** `0N/poster.jpg` (720×1280) es un fotograma real del vídeo en la parte 50/50, con Chris mirando a cámara, ojos abiertos y gesto normal (se eligen a mano: 1 64,2 s · 2 68 s · 3 53,6 s · 4 29 s · 5 52 s · 6 18 s · 7 39 s · 8 42 s). En la tarjeta se ve solo la parte de arriba (él); la de abajo (donde en el vídeo está la pizarra) la tapa un panel claro con la frase del vídeo en grande (campo `f` del array `V`; la palabra entre *asteriscos* sale con el degradado verde 404). La letra es la del sistema (SF Pro en Apple).
- **Reproductor:** cada vídeo arranca sin sonido, en bucle y con el botón «Activar audio» encima; al tocarlo vuelve al principio con sonido. Una vez activado, los siguientes empiezan ya con sonido (si el navegador no lo permite, vuelve a salir el botón). Solo cuenta lo que se ve con el audio activado, segundo a segundo: «Visto» es verlo entero (todos los segundos salvo 2–3 y hasta el final); saltar al final no cuenta. Se envían a `/l/mv` los hitos 25, 50, 80 y 100; el admin cuenta como visto solo el 100 y avisa a Chris en ese momento.
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

## Funnel de anuncios, llamadas y clientes (v48)

- **Meta:** el ID del píxel, el token de la API de conversiones, la cuenta publicitaria y el token de lectura (ads_read) se ponen en Landing › Meta (cifrados en `meta`; nunca en las páginas). `/l/px.js` da el ID a /book, /gracias y /metodo. Solo si el visitante acepta la cookie de Meta (`ll.mc = 1`) se envían por servidor: Lead y Schedule al reservar (mismo `event_id` que el píxel: `lead_<id>`, `sch_<id>`), y LlamadaAsistida, LeadCualificado y Purchase (con importe) al marcarlo en Landing. Registro en `mevents`. Graph API `v26.0` (`META_V`).
- **Gasto:** cada 3 h (`callCron` → `adsPull`) el gasto por anuncio y día en `mads`; se cruza con reservas y ventas por el nombre del anuncio (`utm_content={{ad.name}}`; línea completa en `UTM_LINE`).
- **Llamadas:** Landing › Llamadas para marcar vino / encaja / cliente + importe (usa `llam/lead`). Emails 24 h y 1 h antes (`r24`, `r1`), aviso a Chris para marcar (`ap`), email a quien no vino (`ns`). Cambiar hora o cancelar: `/l/r/<lead>.<token>` (`rsTok`), mueve el evento de Google y el del admin.
- **Lead → cliente:** `/onboarding?l=<lead>.<token>` rellena el alta y une `clients.lead` ↔ `ll.cid` (el cliente queda unido a su anuncio).
- **Cliente:** email semanal los lunes (días 1–15, `weekCron`, tabla `wrep`); email de apertura al marcar «live» como hecho (`openMail`, `clients.opened`); satisfacción días 7 y 15 y testimonio si la nota es alta (`csat`); contrato firmado por los dos en el portal (`pkContract`/`pkSign`, mismas tablas que las obras: `bcontract`, `bsign`; PDF por impresión).
- Los días se cuentan como en el portal: el día de arranque es el día 0 y la tienda abre el día 15.
- Esquema nuevo: `v48Ready` (tablas `mevents`, `mads`, `wrep`, `csat` y columnas de `ll` y `clients`).
- Meta quedó conectado el 3/11/2026: el token de la API de conversiones salió del píxel (Configuración › «Generar identificador de acceso»); el del gasto, del usuario del sistema «Conversions API System User» con la app «404 Growth Admin» (caso de uso «Mide los datos de rendimiento de tus anuncios», permiso `ads_read`, sin caducidad). El código de prueba se deja vacío.

## Guías de Shopify en el portal (v49)

- En «Tu tienda» (vista `entrega`), sección «Aprende a usar tu tienda»: 9 guías paso a paso, en el ordenador y en el móvil, de lo básico que hace el cliente solo: entrar, añadir un producto, cambiar fotos, precio u oferta («Precio de comparación»), código de descuento, stock, ocultar o archivar, preparar un pedido e imagen de la portada.
- Cada guía tiene su dirección `#entrega/<clave>` (`entrar`, `producto`, `fotos`, `precio`, `descuento`, `stock`, `ocultar`, `pedido`, `portada`); `#entrega/aprende` baja a la lista. Las vistas se marcan en el navegador del cliente.
- Debajo, «Lo demás, lo hacemos nosotros»: los cambios grandes (diseño, categorías, pagos y envíos, dominio y apps, TPV, devoluciones, legal, Instagram Shopping, píxel y anuncios, subidas masivas) los hace siempre Chris. El botón abre el chat con el texto puesto.
- Textos en `SH` (es/en) dentro de `PAGES.portal`. Los rótulos entre «» son los del panel de Shopify en español, comprobados en help.shopify.com/es el 3/11/2026; si Shopify los cambia, se cambian ahí. No sale en portales con plan propio (`PL`, como Open Fit). En Inicio sale una tarjeta con las guías cuando la tienda ya está abierta.
- El chat «Pregúntame» lo sabe (`BOT_FACTS`): explica lo básico en dos o tres pasos y manda a la guía; los cambios grandes se los pasa a Chris.

## Propuestas de tienda online con Apimart (lote 31)

- Generador en `prospeccion/lote31/` (ver `LEEME.md`): formato del lote 30, con todas las fotos de la tienda (hero, productos, ficha, categorías y banner) hechas con Apimart a partir de sus productos reales de Instagram. Nano Banana Pro (`gemini-3-pro-image-preview`) a 2K cuesta 0,02 $ por imagen; 15 por tienda.
- Se publican en `404growth.com/p/<slug>/` (archivos en `web117-404growth/`, líneas en `_redirects`). Los botones van a `/book` con `utm_campaign=<slug>`, no a Calendly. El plan de la propuesta es el de 15 días del portal.
- Las fotos descargadas de Instagram solo sirven de referencia: cuando las propuestas están publicadas se borran del Mac (Chris solo quiere `subir.command` y las imágenes de IA).
