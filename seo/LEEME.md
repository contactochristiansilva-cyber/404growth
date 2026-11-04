# Páginas SEO de 404growth.com (de tienda física a tienda online)

Cómo se hacen: un JSON por página en `seo/pages/` (esquema abajo) y `python3 seo/build.py` desde la raíz del repo. El generador escribe el HTML en `web117-404growth/` (`tienda-online/…`, `guia/…`, los dos hubs), `sitemap.xml` y `seo/paginas.json`, y avisa de enlaces internos que no existen y de títulos o descripciones fuera de medida. Para una página nueva: su JSON, su ruta en la lista de enlaces de abajo y en `ORDER_S`/`ORDER_G` de `build.py`, y sus palabras en `seo/palabras-clave.json`.

Escribes el contenido de varias páginas nuevas de 404growth.com. Cada página es un archivo `seo/pages/<slug con / cambiado por __>.json` (ej. `tienda-online/moda` → `tienda-online__moda.json`).

## Quién es 404 Growth (los únicos datos de la empresa que puedes usar)

- Marca de Christian Silva (autónomo, Málaga). Trabaja en toda España, por videollamada.
- Qué hace: convierte tiendas físicas (moda, joyería, calzado, gourmet, juguetes, decoración…) en tiendas online que venden en toda España.
- Plazo: la tienda online abre en **15 días** desde la llamada de arranque (el día de arranque es el día 0; abre el día 15).
- Plataforma: **Shopify**. La tienda, el dominio y la cuenta de pagos quedan **a nombre del cliente**: si deja de trabajar con 404, se lo queda todo.
- Lo que hace el cliente: una llamada de arranque de 1 hora (lo técnico, como accesos, se hace juntos) y pasar fotos, precios y productos por WhatsApp los primeros días. Después, preparar los pedidos (lo mismo que hace en el mostrador) o alguien de su equipo.
- Lo que hace 404: fichas de producto, marca y diseño, pagos (tarjeta, Bizum, Apple Pay), envíos y recogida en tienda, stock, conexión con Instagram, pruebas de compra; y después traer clientes con anuncios (Meta) y email marketing, medir y ajustar cada semana.
- Stock: si el TPV de la tienda lo permite, el stock se sincroniza con la web; depende del TPV.
- Lo básico de Shopify (subir un producto, cambiar un precio o una foto, crear un descuento) lo aprende el cliente con guías en su portal; los cambios grandes los hace 404.
- Precio: no se publica. Depende de cuántos productos tienes, si se conecta el TPV y si incluye anuncios y email. En la llamada se da un precio cerrado. Aparte (costes externos): dominio, la cuota de Shopify, comisiones por venta, envíos y lo que se invierta en anuncios.
- 404 no garantiza ventas (dependen del producto, precio y mercado); lo que hace es medir desde el primer pedido y mejorar.
- El mantenimiento y la captación continua se acuerdan por escrito antes de empezar.
- Llamada de diagnóstico: **gratis, 30 minutos, por Google Meet**, con Christian. Se reserva en `/book`.
- Los cuatro sitios de donde salen clientes de una tienda online de una tienda física: sus clientes actuales (mostrador, bolsa, ticket), su Instagram, anuncios en Instagram y Facebook, y el email.
- Los cinco fallos típicos de webs que no venden: no se puede comprar (solo «escríbenos»), precio y talla escondidos, lenta en el móvil, pagar es un lío, nadie la empuja (sin anuncios, Instagram ni emails).

NO inventes nada más de 404: ni clientes, ni casos, ni testimonios, ni cifras de resultados, ni años de experiencia, ni premios, ni equipo.

## Reglas de contenido

- Español de España, de tú, claro y directo, frases cortas. Nada de relleno ni frases de IA («en el mundo digital de hoy», «sin duda», «en definitiva», «potenciar», «sinergia»). Tono de alguien que sabe de tiendas y te habla como al dueño de una.
- El lector es el dueño de una tienda física (de barrio o de centro), poco técnico, que se plantea vender online. Escribe para él.
- **Cifras y datos legales o de precios: solo si los compruebas** con búsqueda web en fuentes fiables (web oficial de Shopify España, BOE, Agencia Tributaria, Correos, CNMC, INE…) y los pones en `sources`. Si no puedes comprobar algo, no lo pongas o dilo de forma general («depende de…»). Nada de estadísticas sin fuente. Pon la fecha cuando un precio pueda cambiar («a noviembre de 2026»).
- Nada de consejos peligrosos o falsos: si algo depende de normativa (alimentos, alcohol, cosméticos, devoluciones), di lo esencial y recomienda confirmarlo con su gestoría o con el organismo, enlazando la fuente oficial si la encuentras.
- Cada página debe ser **única** (no una plantilla con el sector cambiado): problemas propios del sector, qué se vende bien online en ese sector y qué no, fotos, tallas, envíos, devoluciones, temporadas, ideas de anuncios propias del sector, etc.
- Usa la palabra clave principal en el `title`, el `h1`, el `lead` y en un `h2`, sin forzar. Las secundarias, repartidas con naturalidad (también variantes como las busca la gente: «cómo vender joyas online», «tienda online de joyería»).
- 900–1.400 palabras por página (las guías pueden llegar a 1.800). 4–7 secciones. 4–6 preguntas frecuentes con respuestas de 2–4 frases.
- Menciona 404 Growth con naturalidad en 1–2 secciones (cómo lo hacemos nosotros), sin convertir la página en un anuncio. El generador ya pone el botón de reservar llamada.
- Enlaces internos dentro del texto (Markdown `[texto](/ruta)`): 2–4 por página, solo a estas rutas:
  `/` (portada), `/blog`, `/guia/pasar-tienda-fisica-a-online`, `/guia/cuanto-cuesta-una-tienda-online`, `/guia/sincronizar-stock-tienda-fisica-y-online`, `/guia/tienda-fisica-vs-tienda-online`, `/guia/requisitos-legales-tienda-online`, `/guia/envios-tienda-online`, `/guia/por-que-mi-tienda-online-no-vende`, `/guia/shopify-vs-woocommerce`, `/guia/vender-por-instagram`, `/guia/click-and-collect`, `/tienda-online/moda`, `/tienda-online/moda-infantil`, `/tienda-online/calzado`, `/tienda-online/joyeria`, `/tienda-online/regalos-y-artesania`, `/tienda-online/cosmetica-y-perfumeria`, `/tienda-online/decoracion-y-hogar`, `/tienda-online/gourmet`, `/tienda-online/pasteleria`, `/tienda-online/jugueteria`, `/tienda-online/deportes`, `/tienda-online/libreria-y-papeleria`, `/tienda-online/floristeria`, `/tienda-online/mascotas`.
- Enlaces externos solo en `sources` (o, como mucho, uno dentro del texto a una fuente oficial).

## Esquema JSON (exacto)

```json
{
  "slug": "tienda-online/joyeria",
  "type": "sector",                       // "sector" o "guia"
  "title": "Tienda online para joyerías: vende joyas online | 404 Growth",   // <= 62 caracteres contando « | 404 Growth»
  "h1": "Tienda online para tu joyería",
  "descr": "Meta descripción de 140 a 155 caracteres, con la palabra clave y un motivo para hacer clic.",
  "kicker": "Joyería y bisutería",       // 1–4 palabras sobre el h1
  "lead": "Entradilla de 1–2 frases (máx. 240 caracteres).",
  "kw": ["palabra clave principal", "secundaria 1", "secundaria 2", "…"],   // 5–12, en minúsculas, sin tildes si la gente busca sin tildes
  "nav": "Joyería",                       // nombre corto para menús (1–2 palabras)
  "card": "Frase de 1 línea para la tarjeta en los listados (máx. 110 caracteres).",
  "sections": [
    {"h2": "Título de la sección", "md": "Texto en Markdown: párrafos, listas con -, **negrita**, [enlaces](/ruta), tablas | sencillas |. Sin títulos # ni ## dentro (usa ### si necesitas subtítulos)."}
  ],
  "faq": [ {"q": "¿Pregunta tal como la buscaría alguien?", "a": "Respuesta de 2–4 frases, en texto plano."} ],
  "related": ["/guia/…", "/tienda-online/…"],   // 3 rutas de la lista, las más útiles para seguir leyendo
  "sources": [ {"t": "Título de la fuente", "u": "https://…"} ]   // [] si no hay datos que citar
}
```
