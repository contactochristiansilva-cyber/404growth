# Facturas con el diseño de 404 Growth

Mismo diseño que la factura 2026-151 de Kiss of Life (9/11/2026): logo 404, SF Pro, gris verdoso y el recuadro de forma de pago. Se comprobó superponiéndola a la original: coinciden.

1. Copia un archivo de `datos/` y cambia número, fechas, cliente, líneas y concepto de la transferencia. Los importes van en céntimos. Con `"total"` en la línea (IVA incluido) y `"total_con_iva"`, la base y el IVA se calculan para que el total cuadre al céntimo.
2. `python3 factura.py datos/<archivo>.json <salida>.html`
3. Saca el PDF con el Playwright del Mac (así lleva la SF Pro): `page.pdf({format:'A4', printBackground:true, margin:{top:0,right:0,bottom:0,left:0}})`.

- Lo que se escribe entre [corchetes] sale marcado en amarillo: es un dato que falta.
- Si algún importe es de 1.000 € o más, las columnas Precio e Importe se ensanchan solas.
- `datos/` (NIF, direcciones, IBAN) no va al repositorio: está en el Mac, en `~/Downloads/404growth-subir/facturas-src/facturas/datos/`.
