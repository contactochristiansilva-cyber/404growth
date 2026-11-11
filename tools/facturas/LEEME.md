# Plantilla de factura de 404 Growth

Mismo diseño que la factura 2026-151 de Kiss of Life (9/11/2026): logo 404, SF Pro, gris verdoso y el recuadro de forma de pago. Se comprobó superponiéndola a la original y coinciden. Espaciados, colores, mis datos de emisor, la forma de pago y la nota del pie son siempre los mismos. En cada factura solo cambian el número, las fechas, el cliente, los conceptos y el concepto de la transferencia.

## En el admin (lo normal)

- Contabilidad › Ingresos (o Entregables › Facturas): «Nueva factura».
- Pon el cliente, los conceptos y el «Concepto de la transferencia». Si quieres una explicación debajo de un concepto, escríbela en el mismo campo, separada por « — ».
- En la lista, «Ver factura» la abre con esta plantilla y «Descargar PDF» abre el diálogo de imprimir: «Guardar como PDF» en el Mac, «Compartir» en el iPhone.
- El emisor y la forma de pago están fijos en el worker (`INV_ME`, v69); la plantilla es `invPage404`.

## Desde aquí (Python)

1. Copia `datos/plantilla.json` y rellena número, fechas, cliente, líneas y concepto de la transferencia. Los importes van en céntimos. Con `"total"` en la línea (IVA incluido) y `"total_con_iva"`, la base y el IVA se calculan para que el total cuadre al céntimo.
2. `python3 factura.py datos/<archivo>.json <salida>.html`. El emisor, la forma de pago y la nota del pie se toman de `datos/yo.json`.
3. Saca el PDF con el Playwright del Mac (así lleva la SF Pro): `page.pdf({format:'A4', printBackground:true, margin:{top:0,right:0,bottom:0,left:0}})`.

- Lo que se escribe entre [corchetes] sale marcado en amarillo: es un dato que falta.
- Si algún importe llega a 1.000 €, las columnas Precio e Importe se ensanchan solas.
- `datos/` no va al repositorio porque lleva NIF, direcciones e IBAN. Está en el Mac, en `~/Downloads/404growth-subir/facturas-src/facturas/datos/`.
