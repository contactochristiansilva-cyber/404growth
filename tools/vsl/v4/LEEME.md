# VSL v4 (20/11/2026): solo su voz, subtítulos siempre, monigotes y el calendario

Sustituye a la v3 (`../v3/`). Lo que Chris dijo de la v3:

- no le gustó la música de fondo ni ningún efecto de sonido («ese woosh es malísimo»): **la música y los efectos los pone él**;
- los subtítulos solo salían a ratos: los quiere **todo el rato**, con lo importante sobre fondo blanco y la letra de Apple, de gris a gris oscuro;
- muy pocas animaciones y nada de los **monigotes** de los anuncios: cuando él no sale en pantalla tiene que verse lo que está contando;
- al decir «elige día y hora» tiene que salir **un recorrido de nuestro calendario**, para que luego sepan usarlo;
- los anuncios (9:16) son solo la referencia de estilo: las escenas se hacen nuevas, en horizontal, con Apimart.

## Qué lleva

- **Sonido:** la pista de audio original copiada tal cual (`-c copy`; la huella del audio es la misma que la del original). Sin música ni efectos. El vídeo dura 4,5 s más que la voz, en silencio, para acabar el recorrido del calendario.
- **Subtítulos** (273): una línea, 4 palabras como mucho, SF Pro 46 px, corte seco entre uno y otro.
  - Sobre Chris: blancos; la palabra que aún no ha dicho, al 50 %.
  - Lo importante (58, lista `KEYS` de `mkspec4.py`): píldora blanca con la letra de gris (#A6A6AB) a gris oscuro (#1D1D1F) según la dice.
  - Sobre las escenas de monigotes: siempre en píldora blanca (más fina si no es importante), porque algunas escenas llegan hasta abajo.
- **16 escenas de monigotes** a pantalla completa, con corte seco, mientras cuenta cada idea (`scenes.py`: referencias, imagen y movimiento de cada una). Cada escena acaba justo antes de la frase siguiente; si entre dos escenas queda menos de 1 s de Chris, la primera aguanta hasta la siguiente.
- **Calendario de /book** (2 veces): Chris en una tarjeta a la izquierda y, a la derecha, un móvil con las capturas reales de /book y un punto que toca el día, la hora, «Moda», la inversión y «Continuar».
  - La primera, al decir «aquí abajo tienes el calendario»: baja desde arriba de la página hasta el calendario y hace las selecciones.
  - La segunda, al decir «elige día y hora»; cuando acaba la voz, se va Chris, sale «Elige día y hora» y el móvil termina en «Hecho, Lucía. Nos vemos.».
- Se conservan de la v3: el corte de zoom por frase (1,00 / 1,12), el móvil con la tienda y «15 días» por detrás de él (ahora se mueven con el zoom), el blanco y negro cuando cita las objeciones y «+30.000 € al mes» arriba.

## Escenas de monigotes con Apimart

1. `genimg.py [ids]`: imagen con `gemini-3-pro-image-preview`, 16:9 a 2K, con fotogramas de los Ads 2 y 4 como referencia de estilo (`refs/`; los fotogramas están en el Mac, en `_render/v4/ads/`). 0,02 $ cada una.
2. `genvid.py [ids]`: sube la imagen (`POST /v1/uploads/images`, devuelve una dirección que dura 3 días) y la anima con `MiniMax-Hailuo-2.3-Fast` (`first_frame_image`, 768P, 6 o 10 s). Sale a 1364×768 y 24 fps; 0,149 $ los 6 s y tarda de 1 a 3 minutos.
   - `first_frame_image` no admite base64: tiene que ser una dirección http.
   - Seedance 2.0 Fast (0,0856 $/s) salía tres veces más caro.
3. Se revisan en hojas de contacto. En la v4 se rehízo c5 (las cajas se deformaban: en el texto del movimiento hay que decir que lo rígido «se queda quieto») y de c11 solo se usan los primeros 5,6 s (después la flecha se dobla hacia abajo; `USE` en `compose4.py`).
4. `compose4.py` ajusta cada clip a su escena: velocidad entre 0,8 y 1,12 y, si sobra, corta el final.

Coste de la v4: 3,15 $ (16 imágenes, 17 vídeos y pruebas). Quedaron 6,82 $.

## Capturas del calendario

Hechas con el Playwright del Mac en `/book`, a 402×874 @2x, con el aviso de cookies escondido y las peticiones a `/l/book` bloqueadas: **no se envía ninguna reserva**. La pantalla final («Hecho, Lucía») se pinta en local con el mismo HTML que usa la página (`ok2()` de `book.html`). Están en `~/Contenidos/VSL edición/_render/v4/pkg/cal/` (`long.png`, `s0`…`s7`). En `long.png` hubo que tapar la barra fija «Reservar mi llamada» con el trozo equivalente de `s0`.

## Archivos

- `words.json`: tiempos por palabra (Parakeet), corregidos con `asr_fix.py` (vuelve a transcribir 16 s alrededor de cada corte de 30 s, donde el primer pase se comía palabras) y `fix.json`.
- `mkspec4.py words.json spec4.json [-v]`: el guion (subtítulos, escenas, calendario, elementos de detrás, blanco y negro, cifra y cortes de zoom). Cada momento se busca por lo que dice (`st('frase')`).
- `ov4.html` + `spec4.js` (`window.SPEC=` + el JSON): `window.R(t, 'front' | 'behind')` deja la página en el segundo `t`.
- `compose4.py <vídeo> spec4.json <frames> <masks> <clips> <a> <b> <salida>`: monta un tramo. Las máscaras de Chris son las de la v3 (`../v3/masks.py`).

## Cómo se hizo en el Mac

Todo en `~/Contenidos/VSL edición/_render/v4/` (`pkg/` son estas fuentes más `cal/` y `clips/`).

1. Fotogramas con el Playwright del Mac (unos 20 por segundo, llamadas de 62 s): `frames/front/NNNNN.png` (los 5.696) y `frames/behind/`.
2. `compose4.py` de 4 en 4 tramos de 400 fotogramas (unos 80 s por llamada), en `o2/cNNNNN.mp4`.
3. `concat -c copy` y el audio del original con `-map 0:v -map 1:a -c copy`.

Resultado: `~/Contenidos/VSL edición/VSL editado v4 (20 nov).mp4` (1920×1080, 25 fps, 3:48, 97 MB).

Para cambiar algo: se toca `mkspec4.py` u `ov4.html`, se vuelven a capturar solo los fotogramas de ese tramo, se monta su `cNNNNN.mp4` y se repite el `concat`. En el Mac no se pueden borrar archivos: `compose4.py` solo usa las capturas de detrás que caen dentro de su tramo del guion, así que las viejas no molestan.

## v5 (20/11/2026, mismas fuentes): inicio, tarjetas blancas y sonido

La v4 le gustó «mucho más». Lo que pidió encima:

- **El inicio le parecía soso.** Ahora el vídeo empieza desenfocado y un poco más cerca (0,9 s) y, hasta la primera escena, hay 12 planos con zoom (`INTRO` en `mkspec4.py`: zoom al empezar y al acabar cada plano, y si entra con un acercamiento rápido de 0,2 s o con corte seco). `compose4.py` los aplica en `zoom_at()` y desenfoca con `GaussianBlur`.
- **«Subtítulos tipo Apple con fondo blanco», como en la v3.** No eran las píldoras: son tarjetas blancas a pantalla completa con su frase en grande, que pasa de gris a gris oscuro según la dice. Hay 9 (`card()` en `mkspec4.py`; `#card` en `ov4.html`): fondo #F2F2F2, línea fina de 62 px y línea gruesa de 116 px, entran subiendo desde abajo y se van con corte seco. Mientras hay tarjeta no sale el subtítulo de abajo. La de «tres razones» lleva las casillas 1 2 3.
- **Sonido** (`mix5.py`). Primero dijo que la música y los efectos los ponía él; después pidió estos, y solo estos:
  - clic de ratón en cada toque del calendario (10);
  - disparo de cámara en cada cambio de plano o animación: 45 a −19 dB de pico (entra o sale una escena, una tarjeta o el calendario, o aparece algo por detrás) y 20 más flojos, a −25 dB, en los cortes de zoom;
  - «ruleta» para las palabras: un tic por cada palabra que se enciende en las tarjetas blancas (99, a −25 dB). No se puso en los subtítulos de abajo: serían más de 900 tics debajo de la voz;
  - música alegre sin voz, muy bajita: 24 LU por debajo de la voz (voz −21,9 LUFS, música −45,7), con 6 dB más en el cierre.
  - La voz va con ganancia 1 y sin procesar. Lo añadido queda unos 21 dB por debajo de ella.
- Los sonidos son grabaciones de Pixabay (licencia de Pixabay), bajadas con el Chrome del Mac porque el contenedor no llega a pixabay.com: en la página de búsqueda, `window.__BOOTSTRAP__.page.results` trae `sources.src` de cada pista; se bajan con `fetch` y se guardan juntas en un `.bin` con `a.download`.
  - Música: «Acoustic Upbeat - Happy Strums» de Sonican (82 bpm, 2 min). Se alarga volviendo al mismo pasaje (de 107,915 s a 49,305 s, 80 pulsos) con un fundido cruzado de 1 s. Que no lleva voz se comprobó pasándole Parakeet: no saca ninguna palabra.
  - Clic: «Mouse click» de MatthewVakaliuk. Disparo: «Camera Shutter» de Universfield. Tic: el último golpe de «Wheel Spin Click Slow Down» (freesound_community).
  - En el Mac: `Música/Alegre/` (4 opciones, A1 es la usada) y `SFX/Reales (Pixabay)/`.
- Resultado: `VSL editado v5 (20 nov).mp4` (con todo), `VSL editado v5 · solo voz (20 nov).mp4` y, en `v5 · sonido por separado/`, la música y los efectos en WAV ya al volumen de la mezcla, para moverlos en DaVinci.
- `python3 mix5.py <vídeo original> spec4.json <carpeta audio> <salida>` escribe `mezcla.m4a`, `musica.wav`, `efectos.wav` y `eventos.json`. Se ejecuta en el Mac (decodifica y codifica con ffmpeg; solo necesita numpy).

## v6 (20/11/2026, misma imagen): sin disparos de cámara y sin nuestra música

Lo que dijo de la v5:

- «No me gusta nada la música de fondo, necesito elegir yo la música.» Quiere la de fondo del vídeo «Iman Gadzhi | Video Sales Letter» (youtube.com/watch?v=oj0lMQfti8E, canal AC-MEDIA, 54 s). Su página no tiene descripción ni créditos de música: no se sabe qué pista es. Del vídeo no se puede sacar, porque lleva la voz encima.
- El disparo de cámara se repetía muchísimo (65 veces) y sonaba «súper digital». Al momento: «quita todos los shots de cámara, no quiero que uses ninguno».

Qué lleva la v6:

- la imagen de la v5, sin tocar (`_render/v4/o2/video.mp4`);
- su voz tal cual, los 10 clics del calendario y los 99 tics de las tarjetas blancas. Nada más: la mezcla mide lo mismo que la voz sola (−21,9 LUFS, pico −6,3 dBFS);
- `mix6.py <vídeo original> spec4.json <carpeta audio> <salida> [música]`: es `mix5.py` sin disparos. La música es opcional: si se le pasa una pista, mide su volumen (`ebur128`), la deja 24 LU por debajo de la voz, la repite con un fundido cruzado de 2 s si dura menos que el vídeo, la sube 6 dB en el cierre y escribe también `musica.wav`.

Resultado: `VSL editado v6 (20 nov).mp4` y `v6 · sonido por separado/efectos (clics y tics).wav`. En el Mac, la mezcla está en `_render/v6/snd/`.

Cuando Chris deje su pista en `Música/`: `mix6.py` con ella y el mismo `ffmpeg -map 0:v -map 1:a -c copy` sobre `o2/video.mp4`.
