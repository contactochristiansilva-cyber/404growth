# Pizarras de los vídeos de /metodo

Pizarra tipo Miro en 1:1 (1080×1080, 25 fps, sin sonido) para la parte 50/50 de cada vídeo. Arriba va Chris a cámara y abajo la pizarra, que él narra mientras la ve.

Los guiones (la intro a cámara y las frases con su tiempo) están en el documento «Guiones de /metodo · cámara + pizarra».

## Vídeo 1
- `board.html`: la pizarra.
- El mapa se inyecta antes de renderizar: sustituye `__MAP__` por el contenido de `map.json`.
- Su guion está en `LEEME-video-01.md`.

## Vídeos 2 a 8 (`motor/`)
- `engine.html` es la plantilla común: cámara, cursor «Christian», animaciones y aspecto.
- `common.py` reúne las piezas (marcos, pósits, móviles, mapa y flechas) y la sincronía.
- Cada `vN.py` define los marcos y las frases.
- En las frases van marcas que el motor convierte en tiempos, a 2,5 palabras por segundo:

| Marca | Qué hace |
|---|---|
| `{id}` | Aparece ese elemento en esa palabra. |
| `{@marco}` | La cámara vuela a ese marco. `{@ALL}` muestra la vista general. |
| `{>id}` | El cursor va a ese elemento. |
| `{>>id}` | El cursor va a ese elemento y hace clic. |
| `{p:0.6}` | Pausa de 0,6 s. |
| `{c2_*}` | Aparecen escalonados todos los elementos cuyo id empieza por `c2_`. |

Algunos elementos siguen solos a otro, sin marca propia:
- `idl`: la etiqueta de `id`.
- `idh`: la punta de la flecha de `id`.
- `id-p`: el destello de `id`.

Para renderizar, desde `motor/`, ejecuta `./one.sh N`:
1. Genera `vN.html`.
2. Captura cada fotograma en PNG, sin pérdida.
3. Codifica con x264 `veryslow`, `-tune animation` y CRF 18.
4. Guarda el resultado en `out/metodo-0N-pizarra.mp4`.

El vídeo 1 se renderiza igual con `rend.mjs`, a partir de `board.html` con el mapa ya inyectado.

## Teleprompter (`motor/tele.py`)

Cada vídeo tiene su teleprompter, que se genera con las mismas palabras y los mismos tiempos que su pizarra. Mide 1280×720:

- Una cuenta atrás de 3 s y un pitido.
- La intro a cámara.
- La marca «50/50 · empieza la pizarra».
- Las frases de la pizarra, iluminadas palabra a palabra, con la pizarra en miniatura al lado.

Para generarlo:

1. `python3 tele.py` crea `tpN.json` (`tb_after_beep` es el segundo en que entra la pizarra tras el pitido).
2. `./tp.sh N <pizarra.mp4>` crea `out3/metodo-0N-teleprompter.mp4`.

**Regla:** si se cambia una frase en `vN.py`, hay que volver a renderizar la pizarra y el teleprompter de ese vídeo.
