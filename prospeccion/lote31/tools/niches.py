"""Textos por nicho (lote 31)."""


def _sizes(c):
    s = ''.join(f'<span style="display:inline-grid;place-items:center;min-width:40px;height:36px;border:1px solid {"#1f1b19" if k == 2 else "#ddd"};font-size:12px;letter-spacing:.08em">{t}</span>' for k, t in enumerate(c.get('sizes', ['XS', 'S', 'M', 'L', 'XL'])))
    return f'<div style="margin-top:22px;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:#8a817c">Talla · <u style="color:#1f1b19">Guía de tallas</u></div><div style="display:flex;gap:8px;margin-top:10px">{s}</div>'


def _opts(label, opts):
    def f(c):
        o = c.get('opts', opts)
        s = ''.join(f'<span style="display:inline-grid;place-items:center;padding:0 14px;height:36px;border:1px solid {"#1f1b19" if k == 0 else "#ddd"};font-size:12px">{t}</span>' for k, t in enumerate(o))
        return f'<div style="margin-top:22px;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:#8a817c">{c.get("opts_label", label)}</div><div style="display:flex;gap:8px;margin-top:10px;flex-wrap:wrap">{s}</div>'
    return f


BASE_TODAY = [('Ve el post', 'Instagram'), ('Os escribe', 'DM o WhatsApp'), ('Espera', 'A que alguien conteste'),
              ('Pregunta', '{q}'), ('Paga', 'Bizum, transferencia o en tienda'), ('Recoge o espera', 'Todo a mano')]

NICHE = {
    'moda': dict(
        shop_of='tienda de moda', item_pl='prendas', item_art='la prenda',
        tienda_p='Diseñada a partir de las mejores tiendas de moda online: fotos de estudio, «compra el look», guía de tallas en la ficha, pago en un toque y vuestro estilo siempre a la vista.',
        look_small='Compra el look', look_p='Toca cada prenda de la foto y añádela a la cesta.', look_btn='Añadir el look',
        complete='Completa el look', wa_trust='te asesoramos con la talla', help2='Guía de tallas', wa_q='¿Dudas con la talla?',
        acc=['Descripción', 'Composición y cuidados', 'Envíos y cambios'], variant=_sizes,
        pdp_h3='Cada prenda,<br>lista para comprar.',
        pdp_points=[('Fotos de estudio', 'Cada prenda por delante, en detalle y puesta.'), ('Guía de tallas', 'Menos dudas, menos devoluciones.'),
                    ('Completa el look', 'Más prendas por pedido, más ticket medio.'), ('WhatsApp directo', 'La duda de talla se resuelve sin salir de la ficha.')],
        flow_today=[(a, b.replace('{q}', 'Talla, precio, stock')) for a, b in BASE_TODAY],
        flow_new=[('Ve el post', 'Instagram o anuncio'), ('Elige su talla', 'En la ficha'), ('Paga', 'Tarjeta, Bizum, Apple Pay')],
        take='La pregunta no es si vuestras clientas compran moda online, sino dónde.',
        fun_shop='Prenda, talla y pago en tres pasos. Sin escribir a nadie.', fun_bot='Responde tallas, envíos y stock al segundo y recupera carritos.',
        fun_crm='Novedades, «vuelve a estar disponible» y la talla de cada clienta guardada.', ad3_btn='Ver el look',
        cambia5='ticket medio con «Completa el look».', cambia7='Probar colecciones y tallas nuevas online antes de llenar la tienda.',
        stack1='Catálogo, tallas, stock y fichas como las de arriba.', plan_cat='Fichas, fotos, tallas y precios de las primeras prendas.',
        next2=('Selección de prendas', 'Elegimos juntos las primeras prendas para el lanzamiento.')),
    'joya': dict(
        shop_of='joyería', item_pl='joyas', item_art='la pieza',
        tienda_p='Diseñada a partir de las mejores joyerías online: fotos de detalle, materiales y quilates en la ficha, envoltorio de regalo, pago en un toque y vuestra confianza siempre a la vista.',
        look_small='Para regalar', look_p='Toca cada pieza de la foto y añádela a la cesta.', look_btn='Añadir el conjunto',
        complete='Combínala con', wa_trust='te asesoramos al momento', help2='Guía de medidas', wa_q='¿Dudas con la medida o el quilataje?',
        acc=['Material y quilates', 'Garantía y certificado', 'Envío asegurado'], variant=_opts('Medida', ['Única']),
        pdp_h3='Cada joya,<br>lista para comprar.',
        pdp_points=[('Fotos de detalle', 'Cada pieza de cerca, con su brillo real.'), ('Material y quilates', 'Todo a la vista, sin tener que preguntar.'),
                    ('Envío asegurado', 'Con seguimiento y listo para regalar.'), ('WhatsApp directo', 'La duda se resuelve sin salir de la ficha.')],
        flow_today=[(a, b.replace('{q}', 'Precio, medida, quilates')) for a, b in BASE_TODAY],
        flow_new=[('Ve el post', 'Instagram o anuncio'), ('Elige la pieza', 'En la ficha'), ('Paga', 'Tarjeta, Bizum, Apple Pay')],
        take='La pregunta no es si vuestros clientes compran joyas online, sino dónde.',
        fun_shop='Pieza, medida y pago en tres pasos. Sin escribir a nadie.', fun_bot='Responde medidas, envíos y quilates al segundo y recupera carritos.',
        fun_crm='Novedades, fechas señaladas e ideas de regalo para cada cliente.', ad3_btn='Ver el conjunto',
        cambia5='ticket medio con «Combínala con».', cambia7='Probar piezas nuevas online antes de llenar el escaparate.',
        stack1='Catálogo, medidas, quilates y fichas como las de arriba.', plan_cat='Fichas, fotos, medidas y precios de las primeras piezas.',
        next2=('Selección de piezas', 'Elegimos juntos las primeras piezas para el lanzamiento.')),
    'obrador': dict(
        shop_of='pastelería', item_pl='tartas y dulces', item_art='la tarta',
        tienda_p='Diseñada a partir de las mejores pastelerías online: fotos que abren el apetito, raciones y día de recogida en la ficha, mensaje para la tarta, pago en un toque y vuestro obrador siempre a la vista.',
        look_small='Para la celebración', look_p='Toca cada dulce de la foto y añádelo al encargo.', look_btn='Añadir todo al encargo',
        complete='Para acompañar', wa_trust='encargos y dudas al momento', help2='Alérgenos', wa_q='¿Una tarta especial o para un evento?',
        acc=['Ingredientes y alérgenos', 'Recogida y envío', 'Conservación'], variant=_opts('Raciones', ['6–8', '10–12', '15–20']),
        pdp_h3='Cada encargo,<br>en un minuto.',
        pdp_points=[('Raciones y día', 'Se elige tamaño y día de recogida en la ficha.'), ('Mensaje en la tarta', 'Sin llamadas ni notas de voz.'),
                    ('Pago por adelantado', 'Encargos confirmados, sin tartas sin recoger.'), ('WhatsApp directo', 'Lo especial se habla sin salir de la ficha.')],
        flow_today=[('Ve el post', 'Instagram'), ('Os escribe', 'WhatsApp o llamada'), ('Espera', 'A que alguien conteste'),
                    ('Pregunta', 'Raciones, precio, día'), ('Confirma', 'Notas de voz y fotos'), ('Paga al recoger', 'Si viene')],
        flow_new=[('Ve el post', 'Instagram o anuncio'), ('Elige tarta y día', 'En la ficha'), ('Paga', 'Tarjeta, Bizum, Apple Pay')],
        take='La pregunta no es si vuestros clientes encargan online, sino a quién.',
        fun_shop='Tarta, raciones, día y pago en un minuto. Sin notas de voz.', fun_bot='Responde raciones, alérgenos y horarios al segundo y confirma encargos.',
        fun_crm='Cumpleaños y fechas de cada cliente: el aviso llega antes de que lo pidan.', ad3_btn='Ver los dulces',
        cambia5='ticket medio con «Para acompañar».', cambia7='Probar dulces de temporada online antes de hornear de más.',
        stack1='Catálogo, raciones, alérgenos y fichas como las de arriba.', plan_cat='Fichas, fotos, raciones y precios de los primeros dulces.',
        next2=('Selección de dulces', 'Elegimos juntos lo que se encarga online desde el primer día.')),
    'deco': dict(
        shop_of='tienda de cerámica', item_pl='piezas', item_art='la pieza',
        tienda_p='Diseñada a partir de las mejores tiendas de hogar online: fotos de mesa puesta, «compra la mesa», medidas en la ficha, envío protegido, pago en un toque y vuestra cerámica siempre a la vista.',
        look_small='Compra la mesa', look_p='Toca cada pieza de la foto y añádela a la cesta.', look_btn='Añadir la mesa',
        complete='Completa la mesa', wa_trust='te asesoramos al momento', help2='Medidas', wa_q='¿Dudas con medidas o colores?',
        acc=['Medidas y material', 'Envío protegido', 'Cuidados'], variant=_opts('Formato', ['Pieza', 'Juego de 4', 'Juego de 6']),
        pdp_h3='Cada pieza,<br>lista para comprar.',
        pdp_points=[('Fotos en la mesa', 'Cada pieza en uso, para imaginarla en casa.'), ('Medidas a la vista', 'Menos dudas, menos devoluciones.'),
                    ('Completa la mesa', 'Más piezas por pedido, más ticket medio.'), ('Envío protegido', 'Embalaje para que llegue entera.')],
        flow_today=[(a, b.replace('{q}', 'Precio, medidas, stock')) for a, b in BASE_TODAY],
        flow_new=[('Ve el post', 'Instagram o anuncio'), ('Elige las piezas', 'En la ficha'), ('Paga', 'Tarjeta, Bizum, Apple Pay')],
        take='La pregunta no es si vuestros clientes compran cerámica online, sino dónde.',
        fun_shop='Pieza, formato y pago en tres pasos. Sin escribir a nadie.', fun_bot='Responde medidas, envíos y stock al segundo y recupera carritos.',
        fun_crm='Novedades, reposiciones e ideas de regalo para cada cliente.', ad3_btn='Ver la mesa',
        cambia5='ticket medio con «Completa la mesa».', cambia7='Probar colecciones nuevas online antes de llenar la tienda.',
        stack1='Catálogo, medidas, stock y fichas como las de arriba.', plan_cat='Fichas, fotos, medidas y precios de las primeras piezas.',
        next2=('Selección de piezas', 'Elegimos juntos las primeras colecciones para el lanzamiento.')),
    'hogar': dict(
        shop_of='tienda de textil y hogar', item_pl='piezas', item_art='la pieza',
        tienda_p='Diseñada a partir de las mejores tiendas de hogar online: fotos de cada pieza en casa, «compra el dormitorio», medidas en la ficha, envío cuidado, pago en un toque y vuestros textiles siempre a la vista.',
        look_small='Compra el dormitorio', look_p='Toca cada pieza de la foto y añádela a la cesta.', look_btn='Añadir el conjunto',
        complete='Completa el conjunto', wa_trust='te asesoramos al momento', help2='Medidas', wa_q='¿Dudas con medidas o tejidos?',
        acc=['Medidas y tejido', 'Envío y recogida', 'Lavado y cuidados'], variant=_opts('Medida', ['90 cm', '135 cm', '150 cm']),
        pdp_h3='Cada pieza,<br>lista para comprar.',
        pdp_points=[('Fotos en casa', 'Cada pieza puesta, para imaginarla en la vuestra.'), ('Medidas a la vista', 'Menos dudas, menos devoluciones.'),
                    ('Completa el conjunto', 'Sábanas, cojines y colcha juntos: más ticket medio.'), ('A medida, también', 'Cortinas y tapizados se piden desde la ficha.')],
        flow_today=[(a, b.replace('{q}', 'Precio, medidas, stock')) for a, b in BASE_TODAY],
        flow_new=[('Ve el post', 'Instagram o anuncio'), ('Elige medida y tejido', 'En la ficha'), ('Paga', 'Tarjeta, Bizum, Apple Pay')],
        take='La pregunta no es si vuestros clientes compran textil para casa online, sino dónde.',
        fun_shop='Pieza, medida y pago en tres pasos. Sin escribir a nadie.', fun_bot='Responde medidas, tejidos, envíos y stock al segundo y recupera carritos.',
        fun_crm='Novedades de temporada e ideas de regalo para cada cliente.', ad3_btn='Ver el dormitorio',
        cambia5='ticket medio con «Completa el conjunto».', cambia7='Probar colecciones nuevas online antes de llenar la tienda.',
        stack1='Catálogo, medidas, tejidos y fichas como las de arriba.', plan_cat='Fichas, fotos, medidas y precios de las primeras piezas.',
        next2=('Selección de piezas', 'Elegimos juntos las primeras colecciones para el lanzamiento.')),
}
