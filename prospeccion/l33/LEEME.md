# Lote 33 (10/11/2026): 50 propuestas, 10 por nicho (moda, joyería, cosmética, sneakers/calzado, óptica)

- `sel.json`: los 50 (de `scrapeo-10nov/leads.json`; fuera Isabel Domínguez, que es cabina, y Pam's, que cerró el 30/9; entran Perfums Alomar y Calzados Moreno).
- `specs.py`: por tienda, lo que se ve en su Instagram (referencias `NN` = `~/Downloads/l33src/<slug>/NN.jpg`), productos, categorías y el sitio de su ciudad para el hero.
- `mkjobs.py sel.json [slug…]` → `data/<slug>.json` (la tienda) y `flow/<slug>.json` (2 mensajes de 5 fotos para el agente de Google Flow, con claves para bajarlas).
- `pjs.py --tok` (una vez, diccionario en `localStorage.__tok` de flow.google.com) y `pjs.py <slug>`: JS comprimido con `__SLUG`, `__K` y `__M`.
- `gen33.py <slug>` → `out/p-<slug>.html` (propuesta común) y `out/p-<slug>--tienda.html` (tienda de ejemplo por nicho; se ve en vivo dentro de la propuesta con iframes, `?tour=1` se recorre sola). Fotos en `ai/<slug>/{h,b,p1..p6,l1,l2}.jpg`.
- Contador de visitas: `tpl/counter.html` (slug y `PARTS` se cambian solos).
- Flow con la cuenta personal: el 10/11 al subir referencias salió «Derechos para usar esta imagen · Acepto» (lo acepta Chris).
