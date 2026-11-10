# Lote 33 (10/11/2026): 50 propuestas, 10 por nicho (moda, joyería, cosmética, sneakers/calzado, óptica)

- `sel.json`: los 50 (de `scrapeo-10nov/leads.json`; fuera Isabel Domínguez, que es cabina, y Pam's, que cerró el 30/9; entran Perfums Alomar y Calzados Moreno).
- `specs.py`: por tienda, lo que se ve en su Instagram (referencias `NN` = `~/Downloads/l33src/<slug>/NN.jpg`), productos, categorías y el sitio de su ciudad para el hero.
- `mkjobs.py sel.json [slug…]` → `data/<slug>.json` (la tienda) y `flow/<slug>.json` (2 mensajes de 5 fotos para el agente de Google Flow, con claves para bajarlas).
- `pjs.py --tok` (una vez, diccionario en `localStorage.__tok` de flow.google.com) y `pjs.py <slug>`: JS comprimido con `__SLUG`, `__K` y `__M`.
- `gen33.py <slug>` → `out/p-<slug>.html` (propuesta común) y `out/p-<slug>--tienda.html` (tienda de ejemplo por nicho; se ve en vivo dentro de la propuesta con iframes, `?tour=1` se recorre sola). Fotos en `ai/<slug>/{h,b,p1..p6,l1,l2}.jpg`.
- Contador de visitas: `tpl/counter.html` (slug y `PARTS` se cambian solos).
- Flow con la cuenta personal: el 10/11 al subir referencias salió «Derechos para usar esta imagen · Acepto» (lo acepta Chris).

## Flow: lo que se aprendió el 10/11/2026
- **Referencias con personas:** Flow las rechaza («podría infringir nuestras políticas»). Se suben con la cara tapada (`noface.py` con YuNet, prefijo `n`). La frase «never reproduce the face or likeness of a real person…» también provoca rechazos: la regla WEAR dice ahora «Show the clothes on a professional female/male fashion model» (`wear()` en `mkjobs.py`).
- **Nombres que empiezan por número** no salen en el buscador de recursos: las de 23 Sneakers se subieron como `ntwentythree-sneakers-NN.jpg`.
- **Cupo:** el agente de Flow tiene un cupo diario («Has alcanzado tu límite de cuota del agente»). Después, el modo manual (quitar «Agente», Nano Banana 2.1, x1, 0 puntos) sigue un rato hasta «Has alcanzado tu límite de uso». El 10/11 dieron unas 450 fotos con el agente y unas 40 a mano.
- **Modo manual sin scripts:** con la página modificada por scripts (el parche de `HTMLInputElement.click`, `execCommand`) Flow responde «Hemos detectado actividad inusual». A mano funciona: recargar la página, «+» → buscar la referencia → «Añadir a petición» → escribir el texto → enviar, todo con clics y teclado reales.
- **Descargar:** en el visor, la imagen grande es de `flow-content.google` y se baja con `fetch(src)` sin `credentials` (con `credentials:'include'` falla). Las de Carlos Joyería se hicieron con una plantilla anterior: se encuentran con el buscador del proyecto («sapphire», «emerald», «velvet»…).
- `redo.py sel.json faltan.txt` arma los mensajes del agente solo con las fotos que faltan; `faltan.txt` = lo pendiente («slug:id.id …»).
