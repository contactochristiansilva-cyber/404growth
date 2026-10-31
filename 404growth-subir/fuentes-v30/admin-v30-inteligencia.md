# Admin v30 + contador v3 · inteligencia de propuestas (27 oct 2026)

Chris: «ampliar el traqueo de las acciones que hacen» los prospectos en las propuestas (y cada cliente en 404 Content).

## Arquitectura (sobre lo que ya había)
- **Contador v3** (`404growth-visits`, `vis/worker.v3.js`; en el Mac `404growth-subir/visitas/`). Migra solo desde v2.
  - Por visita: dispositivo, navegador y sistema (user agent), pantalla/ventana/densidad/orientación, táctil, idioma, zona, modo oscuro, de dónde llega (solo host), cómo se abrió; ciudad, región, ASN y organización de red, IPv4/6 desde `request.cf` (nunca cabeceras del visitante). **La IP no se guarda** (solo el hash diario de siempre).
  - Tiempo activo (visible y con actividad en 30 s o vídeo), scroll %, segundos activos por sección (`ss`).
  - Eventos tipados (tabla `e`): catálogo con esquema por tipo, id de la página (UNIQUE k+i: sin duplicados), 25 por envío, 600 por visita, 32 KB por petición, hora de la página validada (±6 h) y hora de llegada; errores sin emails ni teléfonos.
  - Clasificación: human_likely, automation_likely, security_scanner, link_preview, search_crawler, unknown, con % de confianza y motivo. Robots por nombre van a la tabla `b` (tráfico bruto) y nunca son visitas ni avisan. Red de servidores sin interacción = automático; con interacción = sin clasificar (VPN/empresa). La interacción sube la confianza.
- **Script v3 en 211 páginas** (`crm21/counter3.py`, se ejecuta después de counter.py y counter2.py): añade un script antes del v2 y 3 ganchos (`__c404x`, `__c404p`, `__c404on`). openfit.html tiene otro contador y se queda igual.
  - Eventos: sin, scr 25/50/75/90/100, exp/col, tab, vplay/vprog/vpause/vend, copy (solo longitud), print, share, dl, form0/form1, hid/vis, idle/wake, end, rel/res, err/rerr, nav (TTFB, DCL, load, LCP, CLS, red), resize, fs.
- **Admin v30** (`crm30/patch_v30.py` sobre v29; código en `v30_server.js` y `v30_ui.js`).
  - Ficha de visita: interés 0-100 con factores y fiabilidad, quién la abre (principal / posible lector adicional / ambiguo, acceso simultáneo, compartida a propósito), lectura (activo vs a la vista, scroll, tiempo por parte), «Lo que ha hecho» (eventos + clics en orden), dispositivo y red, tipo de tráfico con botones para corregirlo, exportar y borrar los datos.
  - Pestaña Visitas: Visitas (filtros personas/todo y dispositivo) · Propuestas (ranking por interés) · Movimientos (últimos 3 días, cada 10 s) · Avisos (lista, ajustes, pesos, tráfico automático).
  - Avisos (tabla `palerts`, uno por motivo): entrada (los robots no avisan), contacto (WhatsApp, llamar, email, Instagram), reunión (Calendly, /llamada…), documentos (descarga, imprimir, compartir, formulario), interés alto (umbral, por defecto 60), otro lector (otro dispositivo y otra red), sin actividad N días (apagado por defecto). Ajustes en meta `alert_cfg`, pesos en `intel_w`. Retención de eventos configurable (365 días por defecto), robots 90.
  - API: `visits/intel[/<slug>]`, `visits/feed`, `visits/alerts` (+`/seen`), `visits/cfg`, `visits/robots`, `visit/<id>/class`, `visits/export/<slug>`, `visits/delete/<slug>` (pide escribir el slug). Registro en `adminlog`.
  - Avisos de 404 Content con títulos «404 Content · …» y `c_act` (actividad de clientes) → `/admin#clientes=<id>`.

## Puntuación (pesos por defecto)
Vueltas en otro momento 8 c/u (máx 24) · minuto activo 3 (máx 25) · leerla entera 10 · lo económico/condiciones ≥15 s 10 (+5 si vuelve) · 3+ partes 5 · abre su web nueva 8 · contactar 15 · reunión 20 · descarga/imprimir/compartir 5 (máx 10) · vídeo 3 · posible otro lector 5. Fiabilidad alta/media/baja. Cerrado/Reunión manda sobre la puntuación.

## Límites reales (no se fingen)
Capturas de pantalla y grabaciones: no detectables. Reenvío del enlace: solo «posible lector adicional», nunca afirmado. Modelo exacto del móvil, teléfono, operador: no. Descarga «pedida», no «guardada». Las propuestas son páginas estáticas sin enlaces por destinatario, así que no hay revocación, caducidad ni invitados (haría falta servir las propuestas desde un Worker con tokens). Vistas previas de WhatsApp y escáneres de correo casi nunca ejecutan JavaScript: los que sí se apartan.

## Pruebas
- vis/t_vis3.mjs 41 · t_vis.mjs sobre v3 16 · crm30/t_e2e30.mjs 64 (propuesta real de Brisa en Chromium → contador v3 → admin v30: contexto, tiempo activo, secciones, eventos, avisos de entrada/WhatsApp/descarga/otro lector, robots aparte, API, páginas en iPhone y ordenador, borrado).
- Sin regresiones: t_v22 45, t_v23 34, t_v24 6, t_v28 38, t_v29 4, t_v21ui 12, t_v24ui 17; t_v25-27 el mismo fallo de fecha que ya daba v29; t_v22ui 21/22 (cambió a propósito el texto de «sin clics»).

## En el Mac
- `404growth-subir/visitas/` (nuevo: subir.command lo sube primero), `admin/worker.js`, `partner/worker.js`, `subir.command` (no publica `anterior/` ni `_to_delete/`), 211 páginas en web117. Copias: `anterior/admin-v29.js`, `visitas-v2.js`, `partner-worker-antes-de-actividad.js`.
- Ojo: otra sesión ya dejó encima un admin **v31** (incluye este v30 + 245 negocios nuevos). Ese es el que se sube.
