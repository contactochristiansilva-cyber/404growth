# Demo de edición del VSL (19/11/2026)

Primeros 46 s de `~/Contenidos/VSL Recortado.mov` editados con el estilo de la skill `vsl-edicion-404`, para que Chris dé el visto bueno antes de editar el vídeo entero.

- `ov.html`: la capa de texto y gráficos. `window.R(t)` deja la página en el segundo `t`; nada se mueve solo.
  - Tiempos de cada palabra en `KW` (sacados de Parakeet): `[entra, sale, y, tamaño de la gruesa, [[texto, 'f'|'h', segundo]]]`.
  - Gráficos a pantalla completa: `#sA` (lo que supone un local), `#sB` (0 € · 24 h · 365 días), `#map` (toda España, con `mapa-es.svg` de la portada al lado).
  - Lettering: fina SF Pro 300 + clave en blanco grueso SF Pro 900 (Chris: «blanco grueso»), una sola línea, a la altura del pecho.
- Se captura en el Mac (SF Pro y emoji de Apple) con su Playwright: `page.screenshot({omitBackground:true})` fotograma a fotograma, 25 fps, a `~/Contenidos/VSL edición/_render/frames/NNNN.png` (unos 50 por segundo).
  - Los fotogramas de pantalla completa salen en RGB (sin alfa); `compose.py` lo tiene en cuenta.
- `compose.py <vídeo> <frames> <b1.mp4> <b2.mp4> <salida>`: zooms (tabla `Z`, cortes secos y dos suaves), recortes de B-roll de Apimart en tarjeta (`BR`), desenfoque de cristal detrás de las tarjetas (`GL`) y la capa encima. Unos 15 fotogramas por segundo con 2 CPU.
- `mix.py <vídeo> <música> <carpeta sfx> <duración> <salida.wav>`: voz a −16 LUFS, música con ducking (unos 17 dB por debajo cuando habla) y los efectos colocados por su golpe (tabla `FX`).
- B-roll: `seedance-2.0-fast`, 720p, 5 s, unos 0,43 $ cada uno (`vid.py` del scratchpad de la sesión).
