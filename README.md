# 404 Growth

Código de 404 Growth, copiado del Mac (carpeta Descargas) el 31 oct 2026.

- `404growth-subir/` — los workers de Cloudflare y el script de subida:
  - `admin/worker.js` — el admin, el CRM, Redes (Instagram), LinkedIn y el blog `/blog` (worker «404growth-admin»).
  - `partner/`, `visitas/` — Partner 404 y el contador de visitas.
  - `subir.command` — publica todo con wrangler (se ejecuta en el Mac).
- `web117-404growth/` — la web 404growth.com (HTML, CSS, JS, fuentes). **Sin imágenes ni vídeos**: esos están solo en el Mac.

## Cómo se trabaja

1. Los cambios de código se hacen aquí (por ejemplo desde claude.ai/code).
2. Para publicarlos, se copian los archivos cambiados a la misma ruta en `~/Downloads/` del Mac y se ejecuta `404growth-subir/subir.command`.

No hay contraseñas ni claves en el repositorio: los secretos están guardados en Cloudflare y en la base de datos del admin.
