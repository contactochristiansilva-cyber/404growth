# VSL v3 (20/11/2026): el vídeo entero con el estilo nuevo

Sustituye a la demo de `../demo/`, que a Chris no le gustó: los efectos tapaban la voz, la música era «metálica», las animaciones no le gustaron y los textos eran desproporcionados.

## Qué pidió Chris

Lo eligió en la página «Referencias del VSL».

- **Sonido**
  - Su voz va tal cual (ganancia 1, sin compresor, limitador ni normalización).
  - Debajo, piano solo muy bajo (P6, «Flowing» de leberch, en Pixabay), unos 26 LU por debajo de la voz.
  - Un efecto muy suave en cada animación, con el pico 24 dB por debajo del de la voz.
- **Textos**
  - En SF Pro, en blanco, sin caja ni color.
  - A su derecha o a su izquierda, alternando.
  - El estilo es el de sus reels: la parte normal fina (38 px) y la palabra clave más grande y en negrita (64 px, que se reduce si no cabe).
- **Gráficos**
  - Uno por idea, a pantalla completa, blancos como la guía de animación de Apple: gris fino y negro grueso.
  - Entran subiendo desde abajo y se van con un corte seco.
- **Pantalla compartida** (la de su referencia, Devin Jatho): él en una tarjeta a la izquierda y el panel a la derecha.
- **Elementos detrás de él:** solo 3 en todo el vídeo (el móvil con la tienda, «15 días» y el calendario), con él recortado delante.
- **Zoom:** un corte de zoom en cada frase, alternando 1,00 y 1,12.

## Archivos

- `words.json`: los tiempos de cada palabra, sacados con Parakeet.
- `mkspec.py words.json spec.json`: el guion de edición.
  - Textos, gráficos, pantallas compartidas, elementos de detrás, efectos y cortes.
  - Cada momento se busca por las palabras que dice Chris (`st('frase')`).
- `ov3.html` + `spec.js`:
  - Se genera con `window.SPEC=` seguido del contenido de spec.json.
  - `window.R(t, 'front' | 'behind')` deja la página en el segundo `t`.
- `masks.py <vídeo>`: recorta a Chris con rembg (`u2net_human_seg`, 960×540) en los tramos de los elementos de detrás. Se hace en el contenedor.
- `compose3.py <vídeo> spec.json frames masks <a> <b> <salida>`: monta un tramo de fotogramas.
  - Una captura sin transparencia tapa el fotograma entero.
  - Se ejecuta en el Mac de 4 en 4 tramos de unos 400 fotogramas, más o menos 80 s por llamada.
- `mix3.py <vídeo> <música> <carpeta SFX> spec.json <salida.m4a>`: el sonido.

## Cómo se hizo en el Mac

Todo en `~/Contenidos/VSL edición/_render/v3/`.

1. Fotogramas con el Playwright del Mac, a unos 20 por segundo. Cada llamada para a los 65 s, porque el puente corta a los 80 s.
   - Se guardan en `frames/front/NNNNN.png` y `frames/behind/NNNNN.png`.
   - Solo se guardan los fotogramas en los que hay algo.
2. `compose3.py` por tramos, en `out/cNNNNN.mp4` (x264 veryfast, CRF 18).
3. `mix3.py`.
4. `concat -c copy` más el audio.

El resultado es `~/Contenidos/VSL edición/VSL editado v3 (20 nov).mp4`: 1920×1080, 25 fps, 3:43, unos 90 MB.

Para cambiar algo, se toca `ov3.html` o `mkspec.py`, se vuelven a capturar solo los fotogramas de ese tramo, se monta de nuevo su `cNNNNN.mp4` y se repite el `concat`.
