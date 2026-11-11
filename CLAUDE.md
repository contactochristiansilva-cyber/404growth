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
- **Es también la página de gracias (v52):** al reservar, /book lleva a `/metodo?c=<lead>` (ya no a /gracias; `gracias.html` solo redirige a /metodo con el lead de `sessionStorage.c404bk`). Si viene de reservar en esa pestaña (`JB`), arriba sale «Llamada reservada», «Hecho, Ana. Nos vemos … a las …» y el aviso de aceptar la invitación del correo. Esa primera visita automática se manda con `fr: 1` y el Worker no avisa a Chris (avisa la primera vez que la abre él desde la invitación y cuando vuelve tras 6 h). **Vídeo de gracias** (`TY` en el script, v63 del 6/11/2026): `~/Contenidos/Videos Metodo/video de gracias .metodo.mov`, en horizontal (1920×1080, 27 s). Está publicado en HLS en `v/metodo/00/`, con 1080 (1920×1080, CRF 21) y 720 (1280×720, CRF 22). El póster (1280×720) es el fotograma de 3,0 s y el SSIM es 0,992. Con `TY.h = 1`, la caja va en 16:9 (`.ty.h`):
  - en el ordenador, a la derecha del texto (columnas 1fr / 1.12fr, título más pequeño);
  - en el móvil, a todo el ancho, debajo de la fecha.

  El botón «Activar audio» va abajo para que se vea la cara. Arranca sin sonido y en bucle; al tocarlo empieza desde el principio con sonido.

  Para que no se vea negro mientras carga (v63b), lleva el fotograma metido en la propia página (`.tyimg`, 768×432 en base64, unos 27 KB). El vídeo está encima, transparente, y aparece cuando de verdad se mueve (`.ty.vp`). En su lista maestra va primero la 720, así Safari y hls.js (`abrEwmaDefaultEstimate: 1e6`) empiezan por la ligera.
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

## Métricas del blog (v54, 4/11/2026)

- En el admin: LinkedIn y blog › «Métricas del blog» (o `/admin#blog`). Visitas, leídos hasta el final, clics en «Reservar» y reservas, con 7/30/90 días y comparación con el periodo anterior (solo si antes hubo 5 o más), visitas por día, de dónde vienen y una tabla por artículo. En «Publicados» cada artículo lleva sus visitas desde el inicio.
- Cada página del blog llama a `/l/bl` (`blHit`): `v` al abrirla, `r` al ver `#fin` (el final del artículo) y `c` al tocar un `a[data-cta]`. Sin cookies ni nada guardado en el navegador del lector: cuenta una vez al día por persona, artículo y cosa con una huella (sha de sal `bl_salt` + IP + navegador + día) en `bseen`, que solo guarda hoy y ayer (se limpia en `socialCron`). Totales por día, artículo y origen en `bstat` (`blSrc`: LinkedIn, Google, otros buscadores, IA, redes, 404growth.com, directo, otras). No cuenta robots, ni la sesión del admin, ni navegadores con `c404int` (`/book?interno=1`).
- Los botones del blog (menú y recuadro final) van a `/book?utm_source=blog&utm_medium=menu|articulo&utm_campaign=<slug>` (`portada` desde /blog), ya no a Calendly; el recuadro dice `GB_DUR` minutos (30). Las reservas del blog son los leads con `utm_source=blog` (`blStats`). El prompt del artículo con IA también dice 30 minutos.

## Post diario de LinkedIn: enlace a la web (v65, 7/11/2026)

- Cada post de LinkedIn empieza con «Visita mi web: https://404growth.com» y una línea en blanco, encima del gancho (`LI_WEB` y `liWeb()` en el worker del admin). Chris lo pidió solo para LinkedIn: ni el artículo del blog ni Instagram lo llevan.
- `liDraft` lo pone ya en el borrador (se ve y se puede tocar en el admin). Al publicar en LinkedIn (`li/publish`) se añade si falta, también en los posts escritos a mano, y se guarda así en `lpost.li`. Si la primera línea ya nombra 404growth.com, no se repite.

## Varias cuentas de Instagram en Redes (v66, 7/11/2026)

- En el admin › Redes se conectan todas las cuentas que haga falta («+ Añadir cuenta»), cada una con su token. Arriba salen como pastillas para cambiar de una a otra, y cada cuenta tiene su selector «Marca»: Christian (B2C), 404 Growth (B2B) o sin asignar.
- Las cuentas están en `meta.ig_accts` (lista con `id`, `t`, `fb`, `uid`, `user`, `exp` y `role`; helpers `igAccts`, `igSave`, `igPick` e `igIds`). Las cifras van por cuenta: `ig_acct:<id>`, `ig_fol:<id>`, `ig_sync:<id>` e `ig_ai:<id>`. Cada publicación de `igm` lleva su `acct`.
  - La primera vez, la cuenta que había (`ig_tok`, @1christiansilva) pasa sola a la lista con sus publicaciones y su histórico de seguidores.
- Dos tipos de token:
  - `EAA…`, el del inicio de sesión unificado de Meta: va a graph.facebook.com y no caduca;
  - `IG…`, el del inicio de sesión con Instagram: va a graph.instagram.com, dura 60 días y se renueva solo cada semana.
- API: `GET social/ig?a=<id>`, `ig/token` (con `role`), `ig/sync` e `ig/ai` (con `{a}`), `ig/role {a, role}` y `disconnect {k:'ig', a}`. Al desconectar una cuenta se quita de la lista, pero sus publicaciones se quedan guardadas.
- El cron (`socialCron`) sincroniza, a partir de las 6, una cuenta por minuto y cada una una vez al día (`ig_sync_day:<id>`).
- El análisis con IA de una cuenta de Christian usa su voz (`CHR_VOICE`); el resto, la de 404 (`SOC_VOICE`).
  - Los ganchos del post de LinkedIn salen solo de las cuentas marcadas 404 Growth.
- **v66b (7/11/2026):** Chris quitó el «Banco de ideas · reels» de Redes. La página ya no lo pide ni lo enseña, pero la tabla `rideas` y las rutas `social/ideas*` siguen ahí. Las ideas solo se generaban con el botón, así que no hay nada programado que apagar.
- El campo del formulario se llama «Número de la cuenta: 1784…». Es el número que sale bajo el nombre de la cuenta en Meta, en «2. Genera identificadores de acceso». Si alguien escribe el @usuario, el admin avisa y no envía nada: el 7/11/2026 Chris puso «@christiaansilva» y el admin no encontró la cuenta.
- Conectadas el 7/11/2026:
  - @1christiansilva (17841477418546809) → 404 Growth;
  - @christiaansilva (17841402074027493, personal, 6.717 seguidores) → Christian;
  - @404growth (17841441920710616) → 404 Growth.

  El 9/11/2026 las tres se sincronizaron solas por la mañana, una por minuto.

  Las tres son «Evaluador de Instagram» en la app «404 Growth Admin», que no está publicada. Las invitaciones se aceptan en la web de Instagram: instagram.com/accounts/manage_access/ › «Invitaciones para evaluadores», con esa cuenta abierta. En la app del móvil no salen.
- Prueba: `t_v66.mjs` en el scratchpad de la sesión del 7/11/2026 (23 comprobaciones con node:sqlite y la Graph API simulada).

## SEO (v55, 4/11/2026): todo sobre «de tienda física a tienda online»

- Páginas estáticas generadas con `python3 seo/build.py` desde `seo/pages/*.json` (una por página; esquema y reglas de contenido en `seo/LEEME.md`) y `seo/hubs.json`: `/tienda-online` + 14 sectores (`/tienda-online/moda`…) y `/guia` + 10 guías (`/guia/cuanto-cuesta-una-tienda-online`…). Escribe también `sitemap.xml` y `seo/paginas.json` (títulos para las métricas del admin). Estilo en `seo/style.css` (el del blog). Botones a `/book?utm_source=seo&utm_medium=sector|guia|hub&utm_campaign=<slug>`.
- Mapa de palabras clave en `seo/palabras-clave.json`, cargado en el admin › SEO (tabla `keywords`): «publicada» = ya tiene su página; «idea» = tema para el artículo diario del blog, con `page` = la página a la que debe enlazar. `liDraft` coge la primera «idea» (por `updated` desc), le pide a la IA que enlace a su página y la pasa a «en curso». Las palabras de la oferta antigua (chatbots, CRM, concesionarios) quedaron «descartada».
- Los temas del blog (`SOC_PILLARS`) son todos de físico → online. El blog enlaza a Sectores y Guías en el menú, el pie y al final de cada artículo.
- La portada: 15 días (ya no 21), llamada de 30 min, los 9 botones van a `/book?utm_source=web&utm_medium=portada&utm_campaign=<sitio>` (ya no Calendly), y enlaza a los sectores y guías. `/content` (404 Content) lleva `noindex`: tiene su propio dominio.
- Las métricas del admin (LinkedIn y blog › Métricas) cuentan también estas páginas (`BL_PAGE`) y sus reservas (`utm_source=seo`).
- Nada de páginas por ciudad ni de relleno: cada página tiene contenido propio del sector o de la duda. Cifras y datos legales, solo con fuente (campo `sources`).

## Propuestas de tienda online con Apimart (lote 31)

- Generador en `prospeccion/lote31/` (ver `LEEME.md`): formato del lote 30, con todas las fotos de la tienda (hero, productos, ficha, categorías y banner) hechas con Apimart a partir de sus productos reales de Instagram. Nano Banana Pro (`gemini-3-pro-image-preview`) a 2K cuesta 0,02 $ por imagen; 15 por tienda.
- Se publican en `404growth.com/p/<slug>/` (archivos en `web117-404growth/`). **Desde el 10/11/2026 ya no van líneas en `_redirects`:** Cloudflare solo admite 100 reglas «dinámicas» y las 906 reglas 200 de las propuestas hacían fallar `subir-web.command` («Maximum number of dynamic _redirects rules limit of 100 exceeded»). Ahora `subir-web.command` copia cada `p-<slug>.html` a `p/<slug>/index.html` (y `p-<a>--<b>.html` a `p/<a>/<b>/index.html` si esa carpeta existe) antes de subir. Copia del `_redirects` viejo en `anterior/_redirects-2026-11-10`. Los botones van a `/book` con `utm_campaign=<slug>`, no a Calendly. El plan de la propuesta es el de 15 días del portal.
- Las fotos descargadas de Instagram solo sirven de referencia: cuando las propuestas están publicadas se borran del Mac (Chris solo quiere `subir.command` y las imágenes de IA).
- **Qué vendemos en las propuestas (desde el 4/11/2026):** solo la tienda online (web) y los anuncios. Nunca el asistente de IA ni el CRM, ni en textos ni en el plan.
- **Página v32 (lote 32 en adelante; el lote 31 ya se envió y no se toca):** menú en píldora gris oscura con el logo de la tienda en blanco, enlaces y botón blanco «Hablamos» que abre WhatsApp; la letra que era monoespaciada («Propuesta privada…», etiquetas, números) es ahora SF Pro (`--m`); nota de Christian arriba con su foto (`/christian-hola.jpg`); botón fijo «Escribir a Christian» por WhatsApp con el mensaje ya escrito («Hola Christian, he visto la propuesta de …»); la llamada es de 30 minutos; captación en 3 pasos (contenido, anuncios, tienda). Todo en `V32` y `wa()` de `gen.py`. `inline32.py` saca cada propuesta en un solo .html para verla sin publicar.
- **Página v33 (4/11/2026, las 21 del lote 32):** más corta (en el móvil, de 23.000 a 7.000 px). Primer pantallazo con poco texto: chip «Christian · propuesta para X», «X, abierta 24 horas.» y la tienda a la vista; en el móvil solo el teléfono, grande y centrado. El portátil y el móvil del inicio recorren la tienda solos (`TOUR_JS`, envoltorio `.tw`; el hero de su tienda se queda unos 6 s al cargar y 5,5 s cada vez que vuelve arriba, porque Chris lo quiere ver más; se para fuera de pantalla y al pasar el ratón). Secciones: 01 la tienda completa en el navegador grande, como en v32 (Chris la quiere entera al hacer scroll), y debajo su ficha; 02 diagnóstico (pasos de hoy frente a los de la tienda y la búsqueda en Google si no tienen web), 03 «Ideas de campaña» (los 6 anuncios; carrusel en el móvil), 04 plan en 4 hitos con lo que incluye, y cierre con la nota de Christian. Fuera «antes y después», «mercado», «lo que cambia», el embudo y el gantt. Estilos en `V33` de `gen.py`.
- **Envíos (4/11/2026):** correo visual, captura del móvil para WhatsApp e Instagram y hoja del día en `prospeccion/lote31/envios/` (ver su `LEEME.md`). Las imágenes del correo van a `web117-404growth/e/<slug>/NN.jpg`. Los borradores de Gmail se hacen en Chrome pegando el cuerpo (el conector de Gmail quita las imágenes y reescribe los enlaces). Los avisos «DMARC» de hola@ son los informes diarios de Google, Microsoft y Yahoo (no es un bloqueo); lo que sí hubo fueron rebotes de direcciones que no existen: comprobar el email antes de enviar.
- **Contactos de cada tienda (revisión del 5/11/2026, las 21 del lote 32):** buscar siempre en este orden y solo en lo que publica el negocio:
  - **la bio de Instagram**, abriendo el perfil y pulsando «más» y el botón de enlaces (la API `web_profile_info` da 404);
  - **la página de Facebook del negocio**, en `facebook.com/<página>/about`. Se ve sin iniciar sesión y suele traer correo, móvil y si es WhatsApp. De ahí salieron 10 de los 12 correos;
  - **su web**: aviso legal, contacto y condiciones;
  - **directorios** (Cylex, Firmania, Mil Tartas) para el fijo, marcado «comprobar».
- Del dueño o la dueña solo se apunta lo que publica el propio negocio: nombre del perfil, correo con nombre, la marca que es él. Nada de perfiles personales ni teléfonos sacados de otros sitios. Ninguna de las 21 enlaza el Instagram personal de quien la lleva.
- Antes de enviar, comprobar que no venden ya online con otra web o cuenta. Babilonia by Terreta es de Babilonia Shop S.L., que ya vende en modababilonia.com (Shopify, más de 250 productos), y quedó fuera.
- `contactos-5nov.json` guarda lo encontrado. Las notas del CRM llevan «Contacto:», «Dueño:» y, si hace falta, «AVISO:». `envios.py` enseña esas notas y acepta `--fuera <slug>`.
- **Lote 32 (4/11/2026, 21 de 30 publicadas en el Mac a falta de `subir.command`):** rejilla 3x3 a 4K (`jobs_lib.GRID = 3`, `run32.py`): 4 llamadas y 0,09 $ por tienda. Lo que se aprendió:
  - Cuando en sus fotos posa la dueña o alguien del equipo, la IA tiende a copiar su cara. La regla de `KEEP['moda']` y la de las rejillas lo frenan, pero se revisa siempre con `cmpref.py <slug>` (referencias frente a resultado) y, si alguna se parece, se recorta la cara a la altura de los labios con `topcrop.py <slug> <id>=<fracción>` (el original queda en `<id>.orig.jpg`). El banner (l5) con referencias de su tienda también puede sacar a la dueña: se rehace sin referencias.
  - El hero salía a veces como pantalla partida (una franja borrosa a la izquierda): el prompt ya pide «one single continuous photograph». Revisarlos antes de publicar.
  - Apimart no deja lanzar una imagen con menos de 0,05 $ de saldo.
  - Higgsfield (plan gratis): una generación a la vez (si no, error 429) y unos 4,25 créditos por imagen a 2K.
  - El puente con el Mac no acepta archivos de más de 20 MB: el paquete para publicar se parte con `split -b 19m` y se une con `cat` en el Mac.
- **Fotos gratis con Google Flow (5/11/2026):** sin saldo en Apimart, las 15 fotos se hacen en Google Flow (cuenta hola@, `/u/1`) con su agente y Nano Banana 2.1 (Pro tiene unas 20 al día). Herramientas y pasos en `prospeccion/lote31/flow/LEEME.md`. Así salieron las 9 del 5/11/2026 (Mumbai, Corazón, De Rosa, Estela, Mono Mona, Provenza, Punto y Aparte, Quattro y Raza), con sus borradores de Gmail y la hoja `~/Downloads/envios-9-5nov.html`.
- Al publicar, el paquete lleva también `p-<slug>--b--logo.png` cuando la tienda usa su logo en imagen (`LG(...)` en su `shop.py`). El 6/11/2026 faltaba en 5 de las 9 del 5/11 (Corazón, Estela, Mono Mona, Provenza y Raza): la propuesta salía sin logo y el registro de visitas se llenaba de «No carga …logo.png». Antes de subir, comprobar que existe cada archivo `p-<slug>--b--…` que nombra el HTML.
- **6/11/2026:** 5 propuestas más con fotos de Flow (Todo Textil, Flag Sevilla, Tarta Isa, Delia Núñez y Studio Vintage), con sus correos (`e/<slug>/`), borradores en Gmail y la hoja `~/Downloads/envios-5-6nov.html`. Del CRM salieron 5 descartadas con «AVISO (6/11)» (ya venden online, no es tienda o cerró). Cómo se hacen las fotos en Flow sin tocar el menú de descarga: `prospeccion/lote31/flow/LEEME.md`.
- **6/11/2026 por la tarde: 14 propuestas más de moda con fotos de Flow** (Café con Bacon, Boutique Torero, Imperio Moda, Cattalina, Sin Código, El Desván del Regalo, Modas Jade, Myriam, Marai, Serrano, Zaalc, Sara, Chic Glam y Amico), publicadas en `web117-404growth` con sus correos (`e/<slug>/`). Hojas `~/Downloads/envios-8-6nov.html` y `envios-6-6nov.html`; borradores en hola@ para Myriam, Zaalc y Chic Glam (las únicas con correo). Cómo se llevaron 8 proyectos de Flow a la vez: `prospeccion/lote31/flow/LEEME.md`.
- **Ojo con el Chrome del Mac:** el 6/11/2026 daba `DNS_PROBE_FINISHED_NXDOMAIN` falsos (mamenalbero.com y pimara.es sí existen y venden). Antes de decir que una web no existe, comprobarlo desde fuera: `dns.google/resolve?name=<dominio>` y `r.jina.ai/<url>`.
- Si el lote del `SEED` ya está subido, los cambios a esos leads (notas, `slug`, `pageUrl`, teléfono) se hacen con `POST /admin/api/crm/lead/<id>` y `{patch:{…}}` (cabecera `x-404: 1`) desde la pestaña del CRM, no en el `SEED` (que solo inserta los que no existen).
- En las referencias nunca fotos con menores (ni de fondo). Y si la tienda vende diseños con personajes conocidos (tartas de Disney, Mario…), solo se usan las que no los llevan.
- Antes de decir «sin web», abrir la web que salga en su bio, Facebook o Google: Provenza (provenzastore.com, Shopify con 39 productos) y Estela (estelahojaldre.es, catálogo sin compra) sí tenían; sus propuestas lo dicen así.
- **Rejillas (4/11/2026):** `jobs_all.py --rejilla <slug>` hace las 15 fotos en 6 llamadas (hero, banner y look sueltas; ficha, productos y categorías en rejillas 2x2 que `runjobs.py` corta). Misma calidad en la página y 0,12 $ por tienda en vez de 0,30 $. También se puede generar en Higgsfield (créditos gratis; la prueba a 2K descontó 3,5 créditos): referencias con `media_import_url` y resultado descargado con Chrome (ver `prospeccion/lote31/LEEME.md`).

## Portada en el móvil (v56, 4/11/2026)

- Los ajustes del móvil de la portada (`index.html`) van juntos en `<style id="m404">`, justo antes de `</body>`: menos aire entre bloques (secciones a 56 px), tarjetas con su relleno, cifras que no se salen, títulos sin cortes a media palabra (`text-wrap:balance`), las cuatro tarjetas pequeñas de «Lo que cambia» en una columna (≤560 px), los pasos de «Cómo te compran» con la explicación debajo, botones del mismo ancho (hasta 340 px) en una sola línea y el teléfono del pie como enlace `tel:`.
- A 360 px el botón «Reservar» del menú salía vacío (una regla vieja ocultaba todos sus `span`): arreglado.
- El carrusel de sectores (`#nichos`) en el móvil se para en cada sector (20 % del recorrido antes y después) y cada paso dura 1,5 veces el ancho de pantalla; en el ordenador no cambia.
- Se revisa con Playwright a 360, 375 y 390 px: sin scroll lateral y sin palabras partidas.

## Portada: visual del inicio (v61, 5/11/2026)

- Ojo: la portada buena es la del Mac (`~/Downloads/web117-404growth/index.html`). Llegó a la v60 sin pasar por el repositorio; el 5/11/2026 se copió aquí con la v61. Antes de tocar la portada, comparar las dos copias.
- Bajo «Tu tienda. Abierta 24 horas.» va el mapa de España (la opción D de 4; Chris la eligió el 5/11/2026): «Esta noche, desde tu tienda a toda España», con líneas que salen de «Tu tienda» hacia 6 ciudades y la lista de esos pedidos (en el móvil, 3). Pone «Ejemplo con pedidos de muestra». Sustituye a la foto de la tienda con las notificaciones «Nuevo pedido» (v60), que no se entendía.
- Pensado para que el móvil no vaya a tirones (Chris no quiere animaciones lentas en el móvil):
  - nada de `backdrop-filter` ni filtros;
  - los puntos del mapa son una imagen fija (`mapa-es.svg`, 27 KB) y las líneas, un SVG pequeño encima;
  - el pulso de «Tu tienda» solo usa transform y opacity, y se para fuera de pantalla;
  - las miniaturas son `home--t--*.jpg` de 80×80 (unos 2 KB cada una).
- Se anima una vez al verse (IntersectionObserver, clase `.od.in`). Con «reducir movimiento», sale ya completo.
- Se genera con `tools/portada/`:
  - `mk.py` hace los puntos con `es.json` (España de `world-atlas@2.0.2`, `countries-50m`, id 724) y Canarias en un recuadro;
  - `mk_patch.py` crea `od_patch.py`, que cambia `index.html`, escribe `mapa-es.svg` y hace las miniaturas.
- La copia de la v60 está en `~/Downloads/404growth-subir/anterior/index-portada-v60.html`.

## Portada v64 (6/11/2026): Designjoy + Ask Phill + cifras grandes

- Chris eligió esta línea tras comparar 10 webs de agencias (artifact «Agencias de referencia»):
  - la estructura de Designjoy: Christian delante, 3 pasos, qué incluye y preguntas con una tarjeta para hablar;
  - el aspecto de Ask Phill: negro, titular enorme, botones en píldora y tiendas en abanico;
  - de Product Hackers, una cifra enorme por tarjeta.
- Colores de siempre: verde bosque, menta y lima. Letra SF Pro.
- **Sin precio**, como antes: «Precio cerrado, sin sorpresas… te lo damos en la llamada». Las cifras son del proceso y del sector:
  - 15 días;
  - 114.800 M€ y +20,6 % (CNMC);
  - 70 % de cestas abandonadas (Baymard).
  Cuando haya casos reales de clientes, van ahí.
- El abanico de la portada, la sección «Tiendas de ejemplo» y el abanico pequeño del cierre usan las tiendas de demostración de la landing VSL (`/demos/cards/<x>.webp`, enlazan a `/demo-<x>`): Áurea, Pulso, Solenne, Nácar y Forma. Se dice siempre que son proyectos de demostración, no tiendas de clientes.
- El abanico se abre cuando termina el cargador (clase `.fan.pre`, solo transform).
- Se conservan de la v61:
  - el cargador 404;
  - el mapa de España (`.od`), ahora en «Lo que cambia»;
  - las 9 preguntas, que salen del schema FAQPage;
  - los enlaces a sectores y guías y el pie;
  - el WhatsApp flotante, que ahora se esconde mientras se ven los botones de la portada.
- En el móvil se ocultan las píldoras de herramientas, 2 de las 6 ventajas y los textos de captación. «Lo que aportas tú» y «Costes externos» van plegados. No hay blur ni filtros. Revisada con Playwright a 360, 375, 390 y 1440 px.
- Se genera con `tools/portada/v64/build.py <index-v61.html> <salida>` (estilos en `v64.css`; la v61 está al lado).
- Copia de la v61 en `~/Downloads/404growth-subir/anterior/index-portada-v61.html`.

## Portada v67 (9/11/2026): diseñada sección a sección en Claude Design

- Sustituye a la v64. Chris la diseñó en el lienzo «Nueva home · 404growth.com» (artifact de Design): eligió una de tres opciones por sección, viendo a la vez la versión de ordenador y la del móvil. Las elegidas llevan «ELEGIDA» en el título del tablero.
  - Las referencias que pidió fueron Creovibe y Renev: letra y scroll profesionales, scroll lento, degradado inferior transparente y cristal líquido bien usado.
- Las 10 secciones, en orden (con su `id`):
  1. Portada (`#inicio`): un panel de cristal sobre un muro inclinado de tiendas de ejemplo. Dice «Pasamos tu tienda física a tienda online en 15 días.» y lleva 3 píldoras (15 días, Shopify, 30 min).
  2. Cómo funciona (`#como`): línea de tiempo Día 0 → Días 1–14 → Día 15. En el móvil va en vertical.
  3. Tiendas de ejemplo (`#tiendas`): una lista de 5 tiendas y una vista previa en un navegador de cristal. Tocar una tienda cambia la imagen. **Las tiendas no enlazan a sus páginas** (Chris no quiere que se pueda entrar).
  4. Lo que cambia (`#cambia`): el mapa de España con las rutas, 3 tickets de pedidos de muestra y las 6 ventajas.
  5. Captación (`#captacion`): «pajarita» de 5 tarjetas que se estrechan hasta «Te compran» (en lima) y vuelven a abrirse. En el móvil, y por debajo de 1100 px, va en vertical.
  6. En cifras (`#cifras`): bento. Lleva:
     - una tarjeta lima de 15 días con la línea Día 0 a Día 15;
     - una de 114.800 M€;
     - una de +20,6 % con barras de 2024 y 2025 (la de 2024 se calcula desde el +20,6 %);
     - una de 70 % con 10 cestas.
     Las fuentes enlazan a CNMC (ondavasca) y Baymard.
  7. Qué incluye (`#plan`): el precio (sin cifra) y los botones a la izquierda, y 5 desplegables a la derecha. Solo hay uno abierto a la vez (`<details name>`).
  8. Quién te atiende (`#christian`): tarjeta centrada con «CHRISTIAN» gigante en contorno detrás.
  9. Preguntas (`#preguntas`): las 9 en desplegables; salen del schema FAQPage del `<head>`. La tarjeta «¿No está tu duda?» se queda fija al bajar.
  10. Cierre y pie (`#cierre`):
      - los 6 sectores en píldoras y las 6 guías;
      - «¿Abrimos tu tienda a toda España?» en letras enormes;
      - el pie, con «404/GROWTH» gigante en lima que se desvanece hacia abajo (`<svg>` con `textLength`, para que quepa con cualquier letra).
- Detalles:
  - Letra SF Pro (la del sistema); ya no se precarga `inter-tight.woff2`.
  - Scroll lento con Lenis 1.3.26 (`/lenis.min.js`), solo con ratón o trackpad. En pantallas táctiles se usa el scroll del sistema.
  - Degradado inferior fijo (`.fade`), que se quita al llegar al pie.
  - El cristal (`backdrop-filter`) solo se aplica en el ordenador. En el móvil, fondos opacos y nada de filtros.
  - Las animaciones solo usan transform y opacity: aparición al bajar, rutas del mapa solo mientras se ve, y el muro que se mueve despacio solo en el ordenador.
  - Se conserva el cargador 404 de la v64, que ahora vuela al logo de la cabecera.
  - El WhatsApp flotante se esconde mientras se ven los botones de la portada.
  - Menú de hamburguesa en el móvil.
- Enlaces y `data-cta`:
  - /book con `utm_source=web&utm_medium=portada` y `utm_campaign` = `portada`, `menu`, `plan`, `christian` o `cierre`;
  - WhatsApp con `data-cta="wa-<sitio>"`; «Hablamos», en la cabecera, abre WhatsApp.
- El muro de la portada usa miniaturas propias (`/home--w--<tienda>.webp`, 380×520, unos 20 KB cada una; `*.webp` está en `.gitignore`: están en el Mac). La vista previa usa `/demos/cards/<tienda>.webp`.
- Se genera con `python3 tools/portada/v67/build.py <index-v64.html> <salida>`:
  - estilos en `v67.css` y scripts en `v67.js`;
  - la v64 está al lado (`index-v64.html`): de ella solo se toman el `<head>` (SEO, Open Graph y schema) y el cargador.
- Revisada con Playwright a 360, 375, 390, 1024 y 1440 px (sin scroll lateral) y en el Mac con la SF Pro real.
- Copia de la v64 en `~/Downloads/404growth-subir/anterior/index-portada-v64.html`.
- Para publicarla, la nueva está en `~/Downloads/web117-404growth/` junto con `lenis.min.js` y las 5 miniaturas, y se sube con `subir-web.command`.

## Cargador 404 de la portada (v68c, 10/11/2026)

- En la v67 el cargador no se animaba: `build.py` sacaba las reglas de «reducir movimiento» de la v64 fuera de su `@media`, así que los trazos salían ya dibujados y el 404 solo aparecía y se iba.
- **Ojo en el móvil:** `v67.css` tiene `.d{display:none!important}` (bloques solo de ordenador). Los trazos del cargador se llamaban `.d` y en el móvil no se veían. Ahora son `.l4s`: no uses clases genéricas de una letra en el cargador.
- La v68 (onda de choque, temblor, líneas de velocidad) y la v68b (halo, anillo, estelas, pulso) no le gustaron a Chris: **sin círculos, destellos ni efectos raros, solo el logo.** La v68c (`tools/portada/v68/`: `loader.html`, `loader.css`, `loader.js`):
  - el reloj empieza cuando la página ya se ha pintado (doble `requestAnimationFrame`), para que en el móvil se vea desde el principio;
  - el 404 blanco se dibuja desde cero (tres trazos de 0,8 s, escalonados);
  - a los 1,15 s vuela en arco (x e y con curvas distintas, 0,95 s) hacia el logo de la cabecera, pasando a lima (#D4F27A) y **deshaciéndose** por el camino (`stroke-dashoffset` de 0 a −1);
  - a la vez, el logo de la cabecera se dibuja (sus trazos con `pathLength` 1, clase `l404-draw`) y después sale «404 Growth» desde detrás del símbolo (`l404-land`);
  - con «reducir movimiento», solo un fundido. Si algo falla, a los 6 s se quita solo.
- Se aplica a la portada con `python3 tools/portada/v68/patch_loader.py <index.html> <salida>` (parte de la v67). Copia de la v67 en `~/Downloads/404growth-subir/anterior/index-portada-v67.html`.

## Carruseles de Instagram (7/11/2026)

- Van a `~/Contenidos/Carruseles/<serie o semana>/<C# · título (día)>/` con las diapositivas en orden (`01.png`, `02.png`…, 1080×1350) y `texto del post.txt`. La primera semana es `Semana 9-15 nov` (C1–C7, tipográficos). El calendario, los guiones de reels y los textos están en el doc «Contenido de la semana 9–15 nov».
- Se dibujan en HTML y se capturan con el Playwright del Mac, para que salga la letra de Apple (en el contenedor no está).
- **Serie «Abierta 24 h»:** es la firma que hace reconocible a 404. En `Serie Abierta 24 h (IA)/` están C8 (POV 23:47), C9 (¿A o B?) y C10 (5 excusas).
  - **Estilo «etiqueta de envío»** (Chris lo eligió el 7/11/2026 entre 3 direcciones claras; muestras en `Carruseles/Direcciones de marca/`). La primera versión, con fotos de IA de noche, le pareció «tétrica»: está en `_to_delete/oscuro/`.
  - Fondo crema #F6F1E7. En cada diapositiva va una cinta lima inclinada «ABIERTA 24 H ✦ 404 ✦», que es la firma.
  - El mensaje va en una etiqueta blanca con borde negro: cabecera con la hora (23:47, 00:10, 09:30…), campos DE / PARA y código de barras.
  - Para remarcar se usan sellos redondos verde bosque (POV, JUEGO, EXCUSA Nº 0X, 15 DÍAS) y el subrayado lima.
  - Piezas propias de cada diapositiva: el móvil (pantalla de bloqueo o la tienda demo Solenne), los mensajes de chat, las cajas A y B, la tabla, los pedidos y las etiquetas de ciudades. Nada de fotos oscuras.
  - Abajo va una barra de avance verde bosque. Cada carrusel termina con la etiqueta «REMITENTE» (foto de Christian y «Escríbeme TIENDA») y pidiendo un comentario concreto.
  - Plantillas en `tools/carruseles/abierta24h_gen.py <carpeta>`, que escribe `C#.html`. Se copian a `_src/` y se capturan desde `file://` con el Playwright del Mac.
  - Ojo: no uses `s` como clase de texto, porque `.s` es la diapositiva.
- Las 8 fotos de la primera versión (7/11/2026) salieron de Higgsfield con `z_image`, a 0,15 créditos cada una. Ahora quedan 0,05 créditos.
  - El plan gratis solo deja una generación a la vez; si no, da error 429.
  - Desde el Mac se bajan con `page.request.get` y se guardan haciendo una captura de la imagen a su tamaño real.
- **Reels de la semana 9–15 nov:** en el doc «Contenido de la semana 9–15 nov» está cómo se graba cada reel: formato (A a cámara, B 50/50, C pantalla con la cara en un círculo, D plano de recurso), lo que hay que preparar, las tomas con segundos y frase, y el orden del domingo. Las piezas hechas por nosotros están en `~/Contenidos/Reels semana 9-15 nov/` (R6 web folleto de una joyería inventada, R7 bandeja de «¿precio?», R11 ticket; los HTML en `_src/`). Se graban como vídeo con el Playwright del Mac, fotograma a fotograma (JPEG q92), y se montan con ffmpeg a 1080×1920 y 25 fps.
- **7/11/2026:** la cuenta de Google Workspace de hola@ está suspendida por un fallo en el pago, así que Flow no funciona con `/u/1`. Flow con la cuenta personal (`/u/0`) pide que Chris acepte las condiciones. Apimart tiene 0,05 $.

## Banner de YouTube (7/11/2026)

- Hay cinco opciones con la frase de siempre, «Todos podemos, pero / no todos estamos dispuestos.»: A Amanecer, B Foco, C Cumbre, D Rayo de luz y E Escalera.
  - Están en `~/Contenidos/Banner YouTube/` como `opcion-a.png` … `opcion-e.png` (2560×1440), con `comparativa.jpg` al lado.
  - La letra es SF Pro. El logo es la marca 404 del favicon, en gris claro (#D4D4D4) y sin fondo, abajo a la derecha de la zona segura.
- Los fondos se hicieron con la IA de imágenes de Figma (`generate_image`, gpt-image-2.5-flare) en el archivo «Banner YouTube · fondos IA». Higgsfield se había quedado con 0,05 créditos.
  - Desde el contenedor no se puede descargar de figma.com. Por eso se bajan con el Playwright del Mac (captura de la imagen) y se amplían de 1536×864 a 2560×1440 con ffmpeg lanczos.
- Para cambiar una opción se toca `_src/banner.html` y se vuelve a capturar con el Playwright del Mac. Cada opción se elige con `#a`…`#e` en la dirección y tiene su escala, su posición y el estilo de la letra.
- Zonas del banner:
  - lo que se ve en el ordenador es la franja central de 2560×423 (y 508–931);
  - lo que se ve en todos los dispositivos, 1546×423 (x 507–2053);
  - el texto y el logo van siempre dentro de esa zona.

## Scrapeos de tiendas con +20k en Instagram (lotes del 3 y 4/11/2026)

- Filtros: tienda física en España (calle en la bio, su web o Google), +20.000 seguidores comprobados en Instagram, sin tienda online o floja (ayer y hoy: menos de ~30 productos para su tamaño, web caída o en mantenimiento, web sin carrito), nicho que se pueda enviar o recoger, sin cadenas ni franquicias, y que no estén ya en el CRM. Contacto solo de fuentes públicas del negocio (bio, su web, Google).
- Cómo se buscan (lo que funciona): Yahoo (`search.yahoo.com`, en Chrome) con `site:instagram.com` + palabras de la bio que delatan venta sin web («Bizum», «pedidos por WhatsApp», «pedidos por MD») + ciudad; el resultado trae los seguidores. DuckDuckGo y Brave piden CAPTCHA tras ~10-20 búsquedas (no se resuelve). Los seguidores se confirman con `fetch('/<cuenta>/')` desde una pestaña de instagram.com (meta `og:description`); la bio y los enlaces, abriendo el perfil. La web se comprueba en su propia pestaña: Shopify `/products.json`, WooCommerce `/wp-json/wc/store/v1/products` (`x-wp-total`).
- Ojo: muchas cuentas con «Córdoba», «Cartagena», «Toledo» o «boutique» son de Argentina, Colombia, Venezuela o Brasil; se miran la calle y el país.
- Entran en el CRM como Scrapeados con el `SEED` del worker del admin (`SEED_KEY` nuevo cada lote; los que ya existen no se tocan) y Chris ejecuta `subir.command`.
- Si cambias el `SEED_KEY` antes de que Chris haya subido el anterior, deja también los leads del anterior en `SEED`: con la clave nueva, el lote viejo ya no entraría.
- **6/11/2026 (10 de moda, `seed_20261106b`):** lo que funcionó fue la búsqueda por palabra clave de Instagram (`instagram.com/explore/search/keyword/?q=boutique%20<ciudad>`): se juntan los enlaces de las publicaciones y, para cada una, se saca el dueño con `/p/<código>/embed/captioned/` (clase `UsernameText`) y sus seguidores con la meta de `/<cuenta>/`. Abrir la publicación directamente (`/p/<código>/`) da 429 enseguida; la versión `embed` no. Las frases de 3 palabras o más no dan resultados. Yahoo se bloqueó a las ~30 búsquedas.
  - Solo 1 de cada 8 o 10 boutiques de +20k no vende ya online. Las que encajan suelen ser de pueblo o de barrio, outlets, low cost o tiendas que venden en directos y por WhatsApp.
  - Para teléfonos y correos: Google Maps (`google.com/maps/search/<nombre>+<calle>`) y la página de Facebook del negocio (`/about`).
  - Ojo con Facebook: los números sueltos de la pestaña Información pueden ser las visitas de los reels, no un teléfono.
  - Chris prefiere las que publican móvil o WhatsApp: «con tantos fijos es muy difícil llegar a ellos». Desde el 6/11/2026 vale +15.000 seguidores. Las que solo tienen fijo entran con prioridad 50 y «AVISO: solo publican fijo». El móvil se busca en la bio, en los textos de sus últimas 24 publicaciones (`/p/<código>/embed/captioned/`, clase `Caption`), en Facebook `/about` y en Google Maps.

## Tienda demo del Antequera CF (4/11/2026)

- `404growth.com/antequeracf/` = carpeta `web117-404growth/antequeracf/` (`index.html`, `lenis.min.js` y `img/`, unos 7 MB; las imágenes se quedan en el Mac). Cloudflare sirve `index.html` de la carpeta y `/antequeracf` redirige solo a `/antequeracf/`. Todas las rutas son absolutas (`/antequeracf/img/…`).
- Funciona entera sin pagos: cesta guardada en el navegador (`acf-bag`), finalizar compra con datos y entrega (domicilio 4,95 €, gratis desde 80 €, o recogida en El Maulí) que termina en un pedido de prueba `ACF-xxxxxx`, buscador, guía de tallas, avisos de equipaciones y entradas (sin enlace a la taquilla) y alta en el club. `noindex`.
- Se genera desde la maqueta del artifact con `live/build.py` del scratchpad de la sesión (copia del HTML, rutas, textos y `extra.js`/`extra.css`).
- **Portada en el móvil (5/11/2026):** en vertical cada foto llena toda la portada, sin fondo difuminado ni máscara: usa fotos verticales propias (`img/hero-torcal-m.jpg`, `hero-menga-m.jpg`, `hero-m.jpg`, con `m`, `mw`, `mh` y `mbox` en `SLIDES` y sus puntos en `SPOTS['…-m']`). La de El Torcal se amplió hacia arriba y abajo con el outpaint de Higgsfield y se le devolvió encima la foto original, para que las camisetas sean las de siempre (el outpaint rehacía las letras). En pantallas táctiles (`touchUI`): scroll nativo sin Lenis, sin parallax ni desenfoques, y la portada no se recalcula cuando solo cambia la altura (la barra del navegador). Los puntos que caerían sobre el texto de la portada se ocultan en el móvil.
- Las correcciones de las fotos (escudos, letras, la Peña) se regeneran en Higgsfield, nunca retocadas a mano. La camiseta DÓLMENES colgada (`img/manga-larga.jpg`) se rehízo el 4/11/2026 con el escudo, como en su foto de producto.
- **Propuesta al club (5/11/2026):** `404growth.com/antequeracf/propuesta/` = `antequeracf/propuesta/` (`index.html` e `img/`, unos 3,3 MB; las imágenes se quedan en el Mac). Rutas relativas, `noindex`, SF Pro. Calculadora de escenarios (prudente, base, ambicioso; año 1 y año 3) con cinco públicos: abonados, público de El Maulí, cantera, seguidores y turistas, más público nuevo con anuncios en Meta. Base: unos 122.000 € el año 1 y 203.000 € el año 3. Lo que no es público (abonados 2026-27, asistencia, cantera, contrato con Hummel) va como «a confirmar». La misma propuesta en diapositivas es el artifact de Slides «Antequera CF · Propuesta tienda oficial».
- **Contador de visitas (5/11/2026):** la propuesta lleva el contador de las propuestas con el slug `antequeracf` (avisa a Chris al abrirla, como las de `/p/`) y la tienda con `antequeracf-tienda` (desde el 5/11/2026 cuenta como otra propuesta y también avisa al abrirla; antes era `antequeracf--web`, sin aviso). El PDF no se puede contar: lleva enlaces a la propuesta online y a la tienda en la última diapositiva. Si en el CRM no hay un lead con `slug` = `antequeracf`, el aviso sale con ese nombre.

## Plan de Kiss of Life (6/11/2026)

- `404growth.com/kissoflife/` = `web117-404growth/kissoflife/index.html`: un solo HTML (unos 1 MB, con las imágenes dentro), `noindex`, SF Pro. Es la página que Chris enseñó en la llamada con Kiss of Life (Oviedo y Gijón).
- Contenido:
  - el método de lanzamientos (2 o 3 por semana con stock ajustado, lista de espera, básicos siempre en la web);
  - una simulación animada de un lanzamiento (story, web y pedidos);
  - el círculo de lanzamientos;
  - la tienda de ejemplo;
  - los precios: tienda 1.140 €, plan socio online 490 €/mes sin permanencia y 8–12 lanzamientos al mes, con un estimador de ventas que se toca en directo;
  - el anual: 4.900 € IVA incluido, con la tienda y 2 meses gratis y la garantía x3 por contrato (si no venden 14.700 € online en el año, 12 meses más gratis).
- Contador de visitas con el slug `kissoflife` (avisa a Chris al abrirla).
- Se genera con `build2.py` en el scratchpad de la sesión del 6/11/2026; aquí solo está el HTML final.

## Presupuestos (admin v62, 6/11/2026)

- En el admin, Dinero › «Presupuestos» (`/admin#presupuestos`): los presupuestos enviados y pendientes de aceptación. Arriba van los totales pendientes (pagos únicos y cuotas al mes) y debajo tres pestañas: Pendientes, Aceptados y No aceptados.
- Cada presupuesto se puede marcar como aceptado o no aceptado, volver a pendiente, editar y borrar (pide confirmación al segundo clic). «Nuevo presupuesto» está arriba y en el botón «+ Nuevo».
- Cada uno guarda el cliente, qué incluye, el pago único, la cuota al mes, la fecha de envío, el enlace a la propuesta y una nota.
- Se guardan en `docs` con `coll = 'quotes'` (`quotesApi`, rutas `/admin/api/quotes` y `/admin/api/quotes/<id>`); la interfaz es `vPres` en `PAGES.admin`.
- La primera vez se cargan solos los cuatro del 6/11/2026: Carmen Valencia (1.380 €), Kiss of Life (1.140 € + 490 €/mes), Open Fit (3.350 €) y Antequera CF (2.800 €). La marca `meta.quotes_seed` evita que vuelvan si se borran.


## Contabilidad (admin v67, 9/11/2026)

- En el admin, Dinero › «Contabilidad» (`/admin#contabilidad`), justo debajo de Facturación. Guarda todas las facturas de ingresos y de gastos y calcula lo que entra, lo que sale y lo que queda. Tres pestañas:
  - **Resumen:** periodo (mes, trimestre, año o todo, con flechas para ir hacia atrás) y moneda. Ocho cifras: ingresos cobrados, gastos, beneficio neto, facturado, por cobrar, gastos fijos al mes, IVA del trimestre y gastos sin factura. Debajo, la gráfica de ingresos y gastos de los últimos 12 meses (con tabla), los gastos por categoría, el IVA del trimestre y «Para tu gestor» (CSV con `;`, decimales con coma y BOM, para Excel o Numbers).
  - **Ingresos:** el generador de facturas de siempre (`invHtml`) y debajo «Facturas de ingresos hechas fuera», para apuntar y subir las que no salen del admin.
  - **Gastos:** formulario «Apuntar un gasto» con dos modos: **Puntual** (una factura suelta) o **Cada mes** (se apunta solo cada mes el día del primer cargo). Debajo, la lista de gastos mensuales (parar, reanudar o borrar; los meses ya apuntados se quedan) y la de gastos del periodo con el filtro «Sin factura».
- Cómo se calcula (todo con IVA incluido, en céntimos):
  - ingresos = cobros de Facturación (`pay`) con fecha de cobro en el periodo;
  - gastos = gastos apuntados con fecha de factura en el periodo;
  - beneficio neto = ingresos − gastos;
  - facturado = facturas del generador + facturas de ingresos hechas fuera;
  - IVA del trimestre = IVA de las facturas (repercutido) − IVA de los gastos (soportado). Es una estimación: el 303 lo confirma el gestor.
- Cada factura (PDF, JPG, PNG o WEBP, hasta 1,8 MB) se sube desde su fila («Subir», «Cambiar», «Ver», «Descargar»). Las fotos se reducen en el navegador (2000 px, JPEG). El tipo se comprueba por los primeros bytes.
- «Nueva factura» (en Contabilidad, en un cliente o en el botón «+ Nuevo») abre el generador en Contabilidad › Ingresos; dentro de Entregables › Facturas se queda donde estaba. «+ Nuevo» tiene también «Nuevo gasto».
- Facturación enseña arriba la tarjeta «Contabilidad · <mes>» (ingresos, gastos, beneficio y facturado) con un enlace a Contabilidad.
- Las dos gráficas (Contabilidad y Facturación) se dibujan al ancho de su caja y se vuelven a dibujar si la caja cambia (`cbWatch`, con ResizeObserver). En el móvil, las tablas de gastos son tarjetas.
- Datos (D1, se crean solos con `finReady`):
  - `fin`: cada factura (`kind` `in`/`out`, `date`, `who`, `concept`, `cat`, `num`, `total`, `rate`, `cur`, `rec`, `note` y los datos del archivo);
  - `finfile`: el archivo de cada una;
  - `finrec`: los gastos mensuales (`start`, `upto`, `active`, `ended`). `finRecRun` apunta los meses que falten cada vez que se abre (id `x_<rec>_<k>`).
- Categorías de gasto (`FIN_CATS`, rótulos en `CBCAT`): publicidad, software y suscripciones, herramientas de IA, colaboradores y freelance, gestoría, cuota de autónomos, equipo y material, viajes, formación, banco y comisiones, oficina y suministros, y otros.
- API (`finApi`): `GET|POST fin`, `POST|DELETE fin/<id>`, `PUT|GET|DELETE fin/<id>/file`, `POST finrec` y `POST|DELETE finrec/<id>`.
- Interfaz: `vConta` y las funciones `cb…` en `PAGES.admin`.
- Se genera con `patch_v67.py` (con `cb_server.js` y `cb_client.js`) en el scratchpad de la sesión del 9/11/2026 (`fin68/`). Prueba: `t_v67.mjs` (37 comprobaciones con node:sqlite) y `ui67.cjs` (Playwright: apuntar, subir PDF, gasto mensual, editar, filtro y móvil). `t_v66.mjs` sigue pasando.
- Copia del worker anterior en `~/Downloads/404growth-subir/anterior/worker-v66b.js`.

## Scrapeo de +5k seguidores con WhatsApp (10/11/2026, `seed_20261110b`)

- Criterios de Chris: +5.000 seguidores en Instagram, WhatsApp o móvil publicado, sin tienda online o con web que no vende, tienda física en España, sin cadenas y que no estén ya en el CRM. 20 por nicho, en este orden: moda multimarca y boutique, joyería y complementos, cosmética y perfumería, suplementación deportiva, sneakers y ópticas.
- Resultado: 42 leads con +5k (moda 20, joyería 10, cosmética 5, suplementos 2, sneakers 3, ópticas 2). Chris pidió completar los nichos cortos con +1.000 seguidores: segunda búsqueda (550 búsquedas) con 67 más. Total 109: moda 20, joyería 20, cosmética 20, sneakers 20 (la mayoría zapaterías, con «AVISO»), ópticas 20 y suplementos 9 (las tiendas de suplementos casi todas venden online; se añadieron herbolarios y un gimnasio con tienda). Todo en `prospeccion/scrapeo-10nov/leads.json`; `mkseed.py` escribe el `SEED` (el lote no se había subido, así que va entero con la clave nueva).
- Se revisaron unos 3.400 perfiles de 748 búsquedas. Fuera de moda casi todas las tiendas con +5k ya venden online (sobre todo suplementos, ópticas y joyerías grandes), o solo publican fijo, o son franquicias; muchas cuentas de «sneakers» venden réplicas sin tienda física (descartadas).
- **Nichos nuevos en el CRM:** `cosmetica`, `suplementos`, `sneakers` y `optica` (`patch_niches.py`): pestaña propia, mismos textos por defecto que Deporte.
- **Cómo se buscó, sin abrir páginas (lo que funciona):** desde una pestaña de instagram.com, con el cuerpo de la petición capturado de la propia web (enganchando `XMLHttpRequest` y navegando con `history.pushState` + `popstate`):
  - `PolarisKeywordSearchExplorePageRelayQuery` (`POST /api/graphql`, `variables.query`) da unos 20 dueños por búsqueda con su `pk`;
  - `PolarisProfilePageContentQuery` (`variables.id` = pk) da la bio completa, los enlaces, `follower_count`, `address_street` y `city_name`;
  - unas 6-7 búsquedas por minuto, 4 perfiles a la vez, sin errores 429. `/api/v1/users/<id>/info/` y `web_profile_info` dan 429/404.
  - Para leer mucho texto de la pestaña: volcarlo en un `<article>` a pantalla completa y leerlo con `get_page_text` (el resultado de `javascript_tool` se corta a unos 1.000 caracteres).
  - Las webs se comprueban en otra pestaña (Shopify `/products.json`, Woo `x-wp-total`); WebFetch pide permiso por URL y desde el contenedor y el Mac no se llega a esas webs.

## Lote 33 (10/11/2026): 50 propuestas con tienda de ejemplo por nicho

- Generador en `prospeccion/l33/` (ver `LEEME.md`): `specs.py` + `sel.json` → `mkjobs.py` (textos para Flow) → `gen33.py <slug>` (`out/p-<slug>.html`, la propuesta común, y `out/p-<slug>--tienda.html`, la tienda de ejemplo del nicho, metida en la propuesta con iframes). Fotos en `ai/<slug>/{h,b,p1..p6,l1,l2}.jpg` (o `L33_AI`), todas de Google Flow (cuenta personal) a partir de sus productos reales de Instagram.
- 10 por nicho (moda, joyería, cosmética, sneakers/calzado, óptica); los 9 de suplementos y los otros 59 quedan para el miércoles.
- Publicadas el 10/11 en el Mac (a falta de `subir-web.command`): 21 tiendas con sus 10 fotos (sin líneas en `_redirects`: ver arriba). Su `slug`/`pageUrl` va en el `SEED` (`seed_20261110b`, aún sin subir). Las otras 29 esperan ~100 fotos (`l33/faltan.txt`) porque Flow cortó por cupo diario; al subirlas, sus leads ya estarán en el CRM y se marcan con `POST /admin/api/crm/lead/<id>`.
- **10/11 por la tarde:** hechas las ~100 fotos que faltaban y los heroes nuevos (16:9 `hd.jpg` + 9:16 `hm.jpg`) de las 29 restantes con la cuenta de Flow christiansilvaaguilar15. Las 50 tiendas están completas y en el Mac (`web117-404growth`), con su `slug`/`pageUrl` en el `SEED`. Si el `SEED` ya estaba subido, los 29 nuevos se marcan con `POST /admin/api/crm/lead/<id>`. Las fotos se bajan todas juntas en un solo `.json` (Chrome bloquea las descargas múltiples de flow.google.com si no se permiten) y el chat del agente solo enseña 4 de cada 5 imágenes: la quinta se busca en «Imágenes».
- **Fluidez (10/11/2026, `perf34.py`):** las propuestas iban a tirones y el recorrido de la tienda casi no se movía. Con la CPU a 1/4 en Playwright, de 7 fps (ordenador) y 28 fotogramas lentos de 167 (móvil) a 60 fps sin ninguno lento:
  - la tienda tiene `scroll-behavior:smooth`, así que cada `scrollTo` del recorrido empezaba una animación que se cortaba en el fotograma siguiente: con `?tour=1` / `?embed=1` ahora se pone `scrollBehavior='auto'` (en `gen33.py`);
  - la aurora del inicio (`.sk-aur`, `blur(70px)`) se movía sin parar y obligaba a repintar el desenfoque en cada fotograma: ahora está quieta (en `gen33v.py`);
  - los marcos de la tienda se cargan con 400 px de margen (antes 900).
  `perf34.py <carpeta>` lo aplica a las ya generadas (se puede pasar dos veces). Ojo en las propuestas nuevas: nada de capas con `filter:blur` grande que se animen.
- Flow: referencias con personas → cara tapada (`noface.py`); el modo manual solo a mano (con scripts en la página sale «actividad inusual»). Detalles en `l33/LEEME.md`.

## Lote de hoy sin mensaje: audio por WhatsApp (admin v68, 10/11/2026)

- En el CRM › Lote de hoy (nichos con propuesta), el botón «WhatsApp» abre el chat con **solo el enlace de su propuesta** (`text` = `pageUrl`, v68b): Chris añade a cada uno un audio personalizado. Si no tienen WhatsApp (sin móvil), sale solo «Instagram», que copia el enlace y abre su chat (`ig.me/m/<usuario>`). Si el contacto no dice que el móvil sea WhatsApp (`waOk: false`), «Instagram» va primero y «WhatsApp (sin confirmar)» al lado. Los dos marcan el lead como enviado (con «Deshacer»).
- `lotDay` (AAAA-MM-DD) mete un lead en el lote de ese día: va primero y el tope (`lotCap`) nunca lo deja fuera (`dayS()`, `lord` en `vHoy`).
- Cambios a leads que ya están en el CRM: `LEAD_PATCH` + `LEAD_PATCH_KEY` en el worker (`patchOnce`, `json_patch`, una sola vez). El 10/11 puso `lotDay` 2026-11-10 y `slug`/`pageUrl` en las 50 del lote 33, y `waOk: false` en las 12 cuyo contacto no dice WhatsApp.


## Lote 34 (11/11/2026): 20 propuestas (10 de moda + 10 perfumerías árabes)

- Mismo generador que el lote 33 (`prospeccion/l33/`): `sel34.json` (las 20), `nuevos34.json` (las 8 perfumerías que no estaban en el CRM), `jobs34.py` (textos cortos para Flow, de 1 a 3 imágenes por mensaje), `match34.py` (empareja cada imagen de Flow con su trabajo por el texto de la petición), `inline34.py` (una propuesta en un solo .html con su tienda dentro, para revisarla sin publicar) y `crm34.py <worker.js> <día> <sufijo>` (SEED + LEAD_PATCH con `lotDay`; solo entran las que ya tienen página en `out/`).
- Publicadas en el Mac (`web117-404growth`, con sus carpetas `p/<slug>/`). En el worker: `seed_20261111b` y `lpatch_20261111b` (las 20 nuevas y las 50 del lote 33 con `lotDay` 2026-11-11; las ya enviadas no salen por su etapa).
- Lo que se aprendió en Flow:
  - Con 5 imágenes por mensaje y la regla larga, Flow lo rechaza todo; con mensajes cortos de 1 a 3 imágenes va bien (unos 40 s cada uno).
  - **Una sesión de chat nueva por tienda** (botón «Nueva sesión», arriba a la derecha del chat, con clic real). Si se siguen varias tiendas en la misma sesión, el agente mezcla los productos de una con los de otra (salieron frascos de otra tienda en 3 de las 8 perfumerías y hubo que rehacerlos).
  - En el selector de referencias, pulsar el nombre del archivo ya lo añade a la petición. El botón «Añadir a petición» añade el que está resaltado (el primero de la lista, normalmente la última imagen generada): no pulsarlo después. Comprobar que el número de miniaturas de la petición coincide con las referencias.
  - El botón de enviar solo responde a un clic real (no a `click()` desde un script).
  - Tras unas 150 imágenes seguidas sale «Estás preguntando demasiado rápido»; se pasa en una hora más o menos.
  - Las imágenes se bajan de la rejilla con la dirección de la miniatura acabada en `=s0`, o abriendo cada una (`/edit/<id>`) y leyendo su petición (`.text-part`).
- En el Mac, `tar` no puede sustituir archivos que ya existen en una carpeta conectada (no hay permiso de borrado): se extrae fuera (`$HOME/x`) y se copia con `cp`.
- Antes de coger una tienda para un lote, comprobar que no tiene ya `slug` en `sel.json` o en el `LEAD_PATCH` (Madina Perfumes ya estaba en el lote 33).
