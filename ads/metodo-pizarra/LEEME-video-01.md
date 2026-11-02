# /metodo · Vídeo 1 · formato cámara + pizarra (2 nov 2026)

Formato pedido por Chris, como el Ad 3: arranca a cámara en plano completo y después pasa a 50/50 hasta el final. Arriba va él (webcam) y abajo la pizarra tipo Miro, en vídeo 1:1. Él narra mientras la ve. Si le gusta, los otros 7 vídeos se hacen igual.

## Archivos
- `metodo-01-pizarra.mp4`: 1080×1080, 25 fps, 1:59, sin sonido. Es el que va al montaje.
- `metodo-01-pizarra-guia.mp4`: el mismo, con una franja debajo (1080×1340) con la frase que toca, la siguiente y el tiempo. Solo para grabar.
- `metodo-01-maqueta-9x16.jpg`: cómo queda montado (1080×1920: cámara 1080×840 arriba, pizarra 1080×1080 abajo).
- Fuente: `claude/metodo/pizarra-board.html` (en el proyecto). Todo se dibuja desde `render(t)`: cámara (`CAM`), cursor «Christian» (`CUR`, `CLICK`), apariciones (`POP`) y frases de la guía (`LINES`). El mapa de España sale de world-atlas 50m (península y Baleares), proyección cónica.

## Diseño
- Pizarra clara con puntos, marcos blancos con nombre encima, pósits (amarillo, rosa, menta, lila), cursor con etiqueta «Christian», indicador de zoom.
- Letra Inter / Inter Display (SF Pro no se puede renderizar en el contenedor).
- Verde 404 (degradado #7FD3B6 → #2E7A64) solo en palabras clave sobre blanco: «online», «15 días», «Clientes», «otra puerta».
- Números siempre marcados como «Números de ejemplo».

## Guion

**A cámara (≈20 s)**
> Antes de nuestra llamada, empieza por aquí. Si tu tienda ya va bien, este vídeo es para ti. Porque cuando una tienda va bien, tarde o temprano aparece la misma idea: abrir otra. Otro local, en otro barrio o en otra ciudad. Antes de firmar nada, haz conmigo las cuentas.

**50/50 con la pizarra (tiempos de la pizarra)**
| Entra | Frase | En la pizarra |
|---|---|---|
| 0:00 | Mira, lo pongo en la pizarra. Dos opciones. | Vista general |
| 0:04 | Opción A: abrir otro local. Con números de ejemplo. | Marco A |
| 0:08 | El alquiler: pongamos 2.000 euros al mes. | Pósit 2.000 € |
| 0:12 | Para firmar, fianza de dos meses: 4.000 euros. | Pósit 4.000 € |
| 0:17 | La obra y los muebles: otros 30.000. | Pósit 30.000 € |
| 0:22 | Y llenarlo de producto: 20.000 más. | Pósit 20.000 € |
| 0:26 | Y alguien que lo atienda: unos 2.000 al mes. | Pósit 2.000 € |
| 0:31 | Más de 50.000 euros antes de vender una sola cosa. Y 4.000 al mes, vendas o no vendas. | 54.000 € rodeado + 4.000 €/mes |
| 0:39 | Y no abre mañana: buscar local, permisos, obra… meses. | Pósit «Meses» |
| 0:45 | ¿Y a quién le vende? A la gente que pasa por esa calle. Un círculo así de pequeño. | Mapa: dos círculos pequeños |
| 0:52 | Opción B: tu tienda online. | Marco B |
| 0:56 | Alquiler, fianza y obra: cero. Stock nuevo: cero, vendes el que ya tienes. | Pósits 0 € |
| 1:03 | Para abrirla no contratas a nadie: la montamos nosotros. | Pósit «Nadie» |
| 1:07 | Y abre en 15 días. No en meses: en 15 días. | Barras meses / 15 días |
| 1:12 | Y no le vende a una calle: le vende a toda España. A las once de la noche y en domingo. | Mapa con pedidos + aviso 23:04 |
| 1:21 | El dinero no se va en paredes: se va en traer clientes. Y eso se ajusta cada semana. Un contrato de alquiler, no. | Paredes / Clientes, deslizador, candado |
| 1:30 | ¿Que tu tienda ya va bien? Por eso mismo. | Pósit «Mi tienda ya va bien» |
| 1:36 | Ya tienes lo más difícil: un producto que se vende, clientes que repiten y una marca que ya conocen. | Lista ✓✓✓ |
| 1:43 | Lo que te falta no es otro local. Es otra puerta. | ✗ + «otra puerta» |
| 1:48 | Cuánto cuesta y cuánto te devuelve, te lo enseño en el vídeo 5. | Vista general → siguiente |
| 1:53 | Ahora mira el siguiente: cuánto tiempo te quita de verdad. | Tarjeta vídeo 2, clic |

Total: ≈2:20 (20 s a cámara + 1:59 de pizarra).

## Montaje en DaVinci
- Línea de tiempo 1080×1920, 25 fps.
- Plano completo a cámara durante la intro. En el 50/50: la cámara recortada a 1080×840 arriba y la pizarra 1080×1080 abajo (posición Y para que quede pegada al borde inferior).
- Para sincronizar: el inicio de la pizarra coincide con «Mira, lo pongo en la pizarra».

## Pendiente
- Opinión de Chris sobre el vídeo 1. Si le gusta, mismo formato para los vídeos 2 a 8.
