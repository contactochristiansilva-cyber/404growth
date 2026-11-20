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
