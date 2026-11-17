"""Lote 39 (17/11/2026): los nichos nuevos de la tienda y la propuesta (mercería, bellas artes, artesanía, electrodomésticos,
juegos y juguetes, equitación). Lo cargan gen33.py, gen37a.py, gen33v.py, mkjobs.py y jobs37.py al final de su NICHE/NA/NV."""

_USP = lambda city_txt='Gratis, en nuestra tienda.': [('truck', 'Envío a toda España', 'Pídelo hoy y te llega a casa.'), ('store', 'Recogida en {city}', city_txt),
                                                        ('chat', 'Te asesoramos', 'Por WhatsApp, como en la tienda.'), ('card', 'Tarjeta, Bizum y Apple Pay', 'Pago seguro en un toque.')]
_MQ = lambda extra: ['Envío a toda España', 'Recogida en {city}', 'Te asesoramos por WhatsApp', extra, 'Pago con Bizum']

# tienda (gen33.NICHE)
NICHE = {
    'merceria': dict(
        bg='#F6F1EA', surf='#FFFFFF', ink='#1F1A16', mute='#73685D', acc='#A0503F', on='#FFFFFF', line='rgba(31,26,22,.12)',
        hero='full', up=False, eyebrow='Mercería y labores', h1='Tus labores,<br>a un clic.', sub='Lanas, hilos y telas de nuestra tienda de {city}, ahora con envío a casa.',
        btn='Comprar ahora', marquee=_MQ('Novedades cada semana'),
        grid_h='Lo más vendido', grid_s='Lo que más nos pedís en la tienda, con su ficha y su cesta.',
        opts_l='Color', opts=['Crudo', 'Rosa', 'Mostaza', 'Verde', 'Azul'], ban_e='Ideas para tu próxima labor', ban_h='Hecho a mano,<br>hecho por ti.', ban_b='Ver novedades',
        feat_e='El más vendido', item='producto', items='productos', badge='Nuevo', usp=_USP(),
        visit_h='Ven a vernos.', club='Las novedades, antes que nadie', a3='Completa<br>tu labor.',
        ad_h=['Tus labores,<br>en casa.', 'De {city}<br>a toda España.', 'Lo que viste,<br>ya online.']),
    'arte': dict(
        bg='#F4F3EF', surf='#FFFFFF', ink='#151922', mute='#5F6573', acc='#2E4A7A', on='#FFFFFF', line='rgba(21,25,34,.12)',
        hero='full', up=False, eyebrow='Bellas artes y manualidades', h1='Todo para crear,<br>a un clic.', sub='El material de nuestra tienda de {city}, ahora con envío a casa.',
        btn='Comprar ahora', marquee=_MQ('Talleres en la tienda'),
        grid_h='Lo más vendido', grid_s='Lo que más nos pedís en la tienda, con su ficha y su cesta.',
        opts_l='Formato', opts=['Unidad', 'Pack'], ban_e='Talleres', ban_h='Aprende<br>con nosotras.', ban_b='Ver talleres',
        feat_e='El más vendido', item='producto', items='productos', badge='Nuevo', usp=_USP(),
        visit_h='Ven a vernos.', club='Las novedades y los talleres, antes que nadie', a3='Completa<br>tu kit.',
        ad_h=['Todo para crear,<br>en casa.', 'De {city}<br>a toda España.', 'Lo que viste,<br>ya online.']),
    'artesania': dict(
        bg='#F4EEE5', surf='#FFFFFF', ink='#1E1812', mute='#76695B', acc='#8B5A2B', on='#FFFFFF', line='rgba(30,24,18,.12)',
        hero='full', up=False, eyebrow='Hecho a mano', h1='Hecho a mano,<br>a un clic.', sub='Piezas de nuestro taller de {city}, ahora con envío a toda España.',
        btn='Ver las piezas', marquee=['Hecho a mano', 'Envío a toda España', 'Recogida en {city}', 'Encargos por WhatsApp', 'Pago con Bizum'],
        grid_h='Las más deseadas', grid_s='Las piezas que más nos pedís, con su ficha y su cesta.',
        opts_l='Tamaño', opts=['Pequeño', 'Mediano', 'Grande'], ban_e='Del taller', ban_h='Cada pieza,<br>única.', ban_b='Ver el taller',
        feat_e='La pieza estrella', item='pieza', items='piezas', badge='Nuevo',
        usp=[('shield', 'Envío protegido', 'Bien embalado, hasta tu puerta.'), ('store', 'Recogida en {city}', 'Gratis, en nuestro taller.'),
             ('chat', 'Encargos', 'Por WhatsApp, a tu medida.'), ('card', 'Tarjeta, Bizum y Apple Pay', 'Pago seguro en un toque.')],
        visit_h='Ven al taller.', club='Las piezas nuevas, antes que nadie', a3='Completa<br>el regalo.',
        ad_h=['Hecho a mano<br>en {city}.', 'De {city}<br>a toda España.', 'La pieza que viste,<br>ya online.']),
    'electro': dict(
        bg='#F2F4F7', surf='#FFFFFF', ink='#0F1720', mute='#5D6875', acc='#1E5BD8', on='#FFFFFF', line='rgba(15,23,32,.12)',
        hero='full', up=False, eyebrow='Outlet de electrodomésticos', h1='Electrodomésticos<br>a precio outlet.', sub='Lo que tenemos en nuestra tienda de {city}, ahora online y con entrega a domicilio.',
        btn='Ver ofertas', marquee=['Precios outlet', 'Entrega a domicilio', 'Con garantía', 'Exposición en {city}', 'Pago con Bizum'],
        grid_h='Ofertas de la semana', grid_s='Lo que acaba de entrar en la tienda, con su ficha y su precio.',
        opts_l='Color', opts=['Blanco', 'Inox', 'Negro'], ban_e='Ofertas outlet', ban_h='Lo mismo,<br>mucho más barato.', ban_b='Ver ofertas',
        feat_e='La oferta estrella', item='electrodoméstico', items='electrodomésticos', badge='Oferta',
        usp=[('truck', 'Entrega a domicilio', 'Te lo llevamos a casa.'), ('shield', 'Con garantía', 'Todos los aparatos, revisados.'),
             ('store', 'Exposición en {city}', 'Ven a verlo en persona.'), ('card', 'Tarjeta, Bizum y Apple Pay', 'Pago seguro en un toque.')],
        visit_h='Ven a verlo.', club='Las ofertas, antes que nadie', a3='Equipa<br>tu cocina.',
        ad_h=['Tu nevera nueva,<br>a precio outlet.', 'De {city}<br>a tu casa.', 'La oferta que viste,<br>ya online.']),
    'toys': dict(
        bg='#F5F2EC', surf='#FFFFFF', ink='#17140F', mute='#6E665B', acc='#C2501E', on='#FFFFFF', line='rgba(23,20,15,.12)',
        hero='full', up=False, eyebrow='Juegos y juguetes', h1='A jugar,<br>a un clic.', sub='Los juegos de nuestra tienda de {city}, ahora con envío a casa.',
        btn='Comprar ahora', marquee=_MQ('Novedades cada semana'),
        grid_h='Lo más vendido', grid_s='Lo que más nos pedís en la tienda, con su ficha y su cesta.',
        opts_l='Edición', opts=['Estándar', 'Edición especial'], ban_e='Novedades', ban_h='Lo nuevo,<br>antes que nadie.', ban_b='Ver novedades',
        feat_e='El más vendido', item='producto', items='productos', badge='Nuevo', usp=_USP(),
        visit_h='Ven a la tienda.', club='Las novedades, antes que nadie', a3='Completa<br>tu colección.',
        ad_h=['Tu próximo juego,<br>en casa.', 'De {city}<br>a toda España.', 'Lo que viste,<br>ya online.']),
    'deporte': dict(
        bg='#F3EFE8', surf='#FFFFFF', ink='#1C1712', mute='#72675B', acc='#6B4423', on='#FFFFFF', line='rgba(28,23,18,.12)',
        hero='full', up=False, eyebrow='Equitación', h1='Todo para montar,<br>a un clic.', sub='Lo que tenemos en nuestra tienda de {city}, ahora con envío a toda España.',
        btn='Comprar ahora', marquee=_MQ('Doma vaquera y clásica'),
        grid_h='Lo más vendido', grid_s='Lo que más nos pedís en la tienda, con su ficha y su cesta.',
        opts_l='Talla', opts=['S', 'M', 'L', 'XL'], ban_e='Para el jinete', ban_h='Monta con<br>lo mejor.', ban_b='Ver novedades',
        feat_e='El más vendido', item='producto', items='productos', badge='Nuevo', usp=_USP(),
        visit_h='Ven a vernos.', club='Las novedades, antes que nadie', a3='Completa<br>tu equipo.',
        ad_h=['Todo para montar,<br>en casa.', 'De {city}<br>a toda España.', 'Lo que viste,<br>ya online.']),
}

FLOW_TODAY = {
    'merceria': [('Ve el producto', 'en Instagram'), ('Escribe por DM', 'o WhatsApp'), ('Pregunta color, precio y stock', 'y espera respuesta'), ('Bizum o transferencia', 'a mano'), ('Envío', 'coordinado a mano')],
    'arte': [('Ve el producto', 'en Instagram'), ('Escribe por DM', 'o WhatsApp'), ('Pregunta precio y stock', 'y espera respuesta'), ('Bizum o transferencia', 'a mano'), ('Envío', 'coordinado a mano')],
    'artesania': [('Ve la pieza', 'en Instagram'), ('Escribe por DM', 'o WhatsApp'), ('Pregunta precio y medidas', 'y espera respuesta'), ('Bizum o transferencia', 'a mano'), ('Envío', 'coordinado a mano')],
    'electro': [('Ve la oferta', 'en Instagram'), ('Escribe o llama', 'para preguntar'), ('Pregunta precio y medidas', 'y espera respuesta'), ('Va a la tienda', 'a verlo en persona'), ('Entrega', 'coordinada a mano')],
    'toys': [('Ve el juego', 'en Instagram'), ('Escribe por DM', 'o WhatsApp'), ('Pregunta precio y stock', 'y espera respuesta'), ('Bizum o transferencia', 'a mano'), ('Envío', 'coordinado a mano')],
    'deporte': [('Ve el producto', 'en Instagram'), ('Escribe por DM', 'o WhatsApp'), ('Pregunta talla y precio', 'y espera respuesta'), ('Bizum o transferencia', 'a mano'), ('Envío', 'coordinado a mano')],
}

# tienda «Editorial» (gen37a.NA)
_T = [('truck', 'Envío a toda España'), ('card', 'Bizum'), ('store', 'Recogida en tienda')]
NA = {
    'merceria': dict(chip='Novedades · ya en la mercería', sub='Elegido en nuestra tienda de {city}. Ahora, con envío a toda España.', trust=_T,
                     new_e='Recién llegado a la tienda', new_h='Lo nuevo de la semana', cat_h='¿Qué vas a hacer hoy?',
                     look_e='En un solo pedido', look_h='Todo para tu próxima labor', look_s='Tres productos de la tienda que van juntos. Llévatelos a la vez o elige el que te falta.',
                     look_b='Añadir los 3', best_e='Lo más vendido', best_h='Lo que más nos pedís en la tienda'),
    'arte': dict(chip='Novedades · ya en la tienda', sub='Elegido en nuestra tienda de {city}. Ahora, con envío a toda España.', trust=_T,
                 new_e='Recién llegado a la tienda', new_h='Lo nuevo de la semana', cat_h='¿Qué vas a crear hoy?',
                 look_e='En un solo pedido', look_h='Tu kit, en un solo pedido', look_s='Tres básicos de la tienda para empezar tu próximo proyecto.',
                 look_b='Añadir los 3', best_e='Lo más vendido', best_h='Lo que más nos pedís en la tienda'),
    'artesania': dict(chip='Piezas nuevas · recién salidas del taller', sub='Hecho a mano en nuestro taller de {city}. Ahora, con envío a toda España.',
                      trust=[('shield', 'Envío protegido'), ('card', 'Bizum'), ('store', 'Recogida en el taller')],
                      new_e='Recién salido del taller', new_h='Las piezas nuevas', cat_h='¿Qué buscas hoy?',
                      look_e='Para regalar', look_h='Un regalo hecho a mano', look_s='Tres piezas del taller para acertar seguro.',
                      look_b='Añadir las 3', best_e='Las más deseadas', best_h='Lo que más nos pedís por Instagram',
                      fdet=[('shield', 'Envío protegido a toda España'), ('store', 'Recogida gratis en el taller de {city}'), ('card', 'Tarjeta, Bizum, Apple Pay o Google Pay')]),
    'electro': dict(chip='Ofertas nuevas · ya en la tienda', sub='Lo que acaba de entrar en nuestra tienda de {city}. Ahora, con entrega a domicilio.',
                    trust=[('truck', 'Entrega a domicilio'), ('shield', 'Con garantía'), ('store', 'Exposición en tienda')],
                    new_e='Recién llegado', new_h='Las ofertas de la semana', cat_h='¿Qué necesitas para tu casa?',
                    look_e='Equipa tu cocina', look_h='Tres aparatos, un solo pedido', look_s='Tres ofertas de la tienda para renovar la cocina de una vez.',
                    look_b='Añadir los 3', best_e='Lo más vendido', best_h='Lo que más nos pedís en la tienda',
                    visit_p='Ven a verlo en persona antes de llevártelo.',
                    fdet=[('truck', 'Entrega a domicilio'), ('store', 'Ven a verlo a la tienda de {city}'), ('card', 'Tarjeta, Bizum, Apple Pay o Google Pay')],
                    drp='Entrega a domicilio · Exposición en {city}'),
    'toys': dict(chip='Novedades · ya en la tienda', sub='Elegido en nuestra tienda de {city}. Ahora, con envío a toda España.', trust=_T,
                 new_e='Recién llegado a la tienda', new_h='Lo nuevo de la semana', cat_h='¿A qué jugamos hoy?',
                 look_e='En un solo pedido', look_h='Para la próxima partida', look_s='Tres productos de la tienda que van juntos.',
                 look_b='Añadir los 3', best_e='Lo más vendido', best_h='Lo que más nos pedís en la tienda'),
    'deporte': dict(chip='Novedades · ya en la tienda', sub='Elegido en nuestra tienda de {city}. Ahora, con envío a toda España.', trust=_T,
                    new_e='Recién llegado a la tienda', new_h='Lo nuevo de la semana', cat_h='¿Qué buscas hoy?',
                    look_e='Para el jinete', look_h='Tu equipo, en un solo pedido', look_s='Tres productos de la tienda que van juntos.',
                    look_b='Añadir los 3', best_e='Lo más vendido', best_h='Lo que más nos pedís en la tienda'),
}

# reseñas de ejemplo (la página dice que son de ejemplo)
_R = lambda a, b, c, d, e, f: [('Lucía', 'Sevilla', 0, a), ('Rocío', 'Madrid', 1, b), ('Marta', 'Valencia', 2, c), ('Carmen', '*', 3, d), ('Ana', 'Málaga', 4, e), ('Paula', 'Bilbao', 5, f)]
REV = {
    'merceria': _R('Lo pedí un domingo por la noche y llegó tal cual se ve en las fotos.', 'Os sigo desde hace años y por fin puedo comprar sin escribir por privado.',
                   'Me ayudaron a elegir el color por WhatsApp en un momento.', 'Lo recogí en la tienda y aproveché para llevarme dos ovillos más.',
                   'Pagué con Bizum en un minuto. Repetiré seguro.', 'La calidad se nota. Ya tengo fichado lo siguiente.'),
    'arte': _R('Lo pedí el domingo y el martes ya estaba pintando.', 'Os sigo desde hace años y por fin puedo comprar sin escribir por privado.',
               'Me aconsejaron por WhatsApp qué material comprar para empezar.', 'Lo recogí en la tienda y me apunté al taller del sábado.',
               'Pagué con Bizum en un minuto. Repetiré seguro.', 'Todo llegó perfecto y muy bien embalado.'),
    'artesania': _R('Llegó muy bien embalada y es aún más bonita en persona.', 'Os sigo en Instagram y por fin puedo comprar sin escribir por privado.',
                    'Me resolvieron las dudas de medidas por WhatsApp antes de comprar.', 'La recogí en el taller y me enseñaron cómo se hace.',
                    'Pagué con Bizum en un minuto. Un regalo perfecto.', 'Se nota que está hecha a mano. Ya tengo fichada la siguiente.'),
    'electro': [('Javier', 'Sevilla', 0, 'Me lo trajeron a casa a los dos días y funcionando.'), ('Laura', 'Madrid', 1, 'Mucho más barato que en las grandes superficies.'),
                ('Sergio', 'Valencia', 2, 'Me pasaron las medidas por WhatsApp antes de comprar. Encaja perfecto.'), ('Carmen', '*', 3, 'Fui a verlo a la tienda y lo terminé de pedir desde casa.'),
                ('Dani', 'Málaga', 4, 'Pagué con Bizum en un minuto. Repetiremos con la lavadora.'), ('Marta', 'Bilbao', 5, 'Como nuevo y con garantía. Muy contentos.')],
    'toys': [('Javier', 'Sevilla', 0, 'Lo pedí el domingo y el miércoles ya estábamos jugando.'), ('Laura', 'Madrid', 1, 'Por fin puedo comprar sin escribir por privado.'),
             ('Sergio', 'Valencia', 2, 'Me aconsejaron por WhatsApp qué caja comprar para empezar.'), ('Carmen', '*', 3, 'Lo recogí en la tienda y me quedé a la partida del viernes.'),
             ('Dani', 'Málaga', 4, 'Pagué con Bizum en un minuto. Repetiré seguro.'), ('Marta', 'Bilbao', 5, 'Llegó perfecto y muy bien embalado.')],
    'deporte': [('Javier', 'Sevilla', 0, 'Lo pedí el domingo por la noche y llegó tal cual se ve en las fotos.'), ('Laura', 'Madrid', 1, 'Por fin puedo comprar sin escribir por privado.'),
                ('Sergio', 'Jerez', 2, 'Me ayudaron con la talla por WhatsApp en un momento.'), ('Carmen', '*', 3, 'Lo recogí en la tienda y aproveché para mirar monturas.'),
                ('Dani', 'Córdoba', 4, 'Pagué con Bizum en un minuto. Repetiré seguro.'), ('Marta', 'Huelva', 5, 'La calidad se nota. Ya tengo fichado lo siguiente.')],
}

# propuesta (gen33v.NV): se mezcla con los textos de moda (_base)
NV = {
    'merceria': dict(shop_of='mercería', item_pl='productos', item_art='el producto',
                     tienda_p='Diseñada a partir de las mejores mercerías online: cada lana, hilo y tela con su ficha, los colores a la vista, pago en un toque y vuestro consejo siempre a mano.',
                     complete='Completa tu labor', ad3_btn='Ver novedades', pdp_h3='Cada producto,<br>listo para comprar.',
                     pdp_points=[('Fotos que venden', 'Cada color y cada textura, como en la tienda.'), ('Color y cantidad', 'Se eligen en la ficha, sin preguntar por DM.'),
                                 ('Completa tu labor', 'Más productos por pedido, más ticket medio.'), ('Asesoramiento', 'La duda se resuelve por WhatsApp sin salir de la ficha.')],
                     flow_new=[('Ve el producto', 'Instagram o anuncio'), ('Elige color y cantidad', 'En la ficha'), ('Paga', 'Tarjeta, Bizum, Apple Pay')]),
    'arte': dict(shop_of='tienda de bellas artes', item_pl='productos', item_art='el producto',
                 tienda_p='Diseñada a partir de las mejores tiendas de bellas artes online: cada material con su ficha, formatos a la vista, talleres reservados en un minuto y pago en un toque.',
                 complete='Completa tu kit', ad3_btn='Ver novedades', pdp_h3='Cada producto,<br>listo para comprar.',
                 pdp_points=[('Fotos que venden', 'Cada material, como en la tienda.'), ('Formato y precio', 'Se eligen en la ficha, sin preguntar por DM.'),
                             ('Completa tu kit', 'Más productos por pedido, más ticket medio.'), ('Talleres', 'Plazas reservadas y pagadas desde la web.')],
                 flow_new=[('Ve el producto', 'Instagram o anuncio'), ('Elige formato', 'En la ficha'), ('Paga', 'Tarjeta, Bizum, Apple Pay')]),
    'artesania': dict(shop_of='taller', item_pl='piezas', item_art='la pieza',
                      tienda_p='Diseñada a partir de las mejores tiendas de artesanía online: cada pieza con sus fotos y su historia, envío bien protegido, pago en un toque y los encargos por WhatsApp.',
                      complete='Completa el regalo', ad3_btn='Ver las piezas', pdp_h3='Cada pieza,<br>lista para comprar.',
                      pdp_points=[('Fotos de cada pieza', 'Desde todos los ángulos, como en el taller.'), ('Medidas y acabados', 'En la ficha, sin preguntar por DM.'),
                                  ('Completa el regalo', 'Más piezas por pedido, más ticket medio.'), ('Encargos', 'Lo que no está en la tienda, por WhatsApp.')],
                      flow_new=[('Ve la pieza', 'Instagram o anuncio'), ('Elige tamaño', 'En la ficha'), ('Paga', 'Tarjeta, Bizum, Apple Pay')]),
    'electro': dict(shop_of='tienda de electrodomésticos', item_pl='electrodomésticos', item_art='el electrodoméstico',
                    tienda_p='Diseñada a partir de las mejores tiendas de electrodomésticos online: precio y medidas a la vista, entrega a domicilio, garantía y pago en un toque.',
                    complete='Equipa tu cocina', ad3_btn='Ver ofertas', pdp_h3='Cada aparato,<br>listo para comprar.',
                    pdp_points=[('Fotos reales', 'Cada aparato tal y como está.'), ('Precio y medidas', 'En la ficha, sin llamar.'),
                                ('Entrega a domicilio', 'Se elige al pagar.'), ('WhatsApp directo', 'La duda se resuelve sin salir de la ficha.')],
                    flow_new=[('Ve la oferta', 'Instagram o anuncio'), ('Mira medidas y precio', 'En la ficha'), ('Paga', 'Tarjeta, Bizum, Apple Pay')]),
    'toys': dict(shop_of='tienda de juegos', item_pl='productos', item_art='el producto',
                 tienda_p='Diseñada a partir de las mejores tiendas de juegos online: cada caja con su ficha, novedades y reservas a la vista, pago en un toque y vuestro consejo siempre a mano.',
                 complete='Completa tu colección', ad3_btn='Ver novedades', pdp_h3='Cada producto,<br>listo para comprar.',
                 pdp_points=[('Fotos que venden', 'Cada caja y cada pieza, como en la tienda.'), ('Precio y stock', 'En la ficha, sin preguntar por DM.'),
                             ('Completa tu colección', 'Más productos por pedido, más ticket medio.'), ('Asesoramiento', 'La duda se resuelve por WhatsApp sin salir de la ficha.')],
                 flow_new=[('Ve el juego', 'Instagram o anuncio'), ('Mira la ficha', 'Precio y stock'), ('Paga', 'Tarjeta, Bizum, Apple Pay')]),
    'deporte': dict(shop_of='tienda de equitación', item_pl='productos', item_art='el producto',
                    tienda_p='Diseñada a partir de las mejores tiendas de equitación online: cada producto con su ficha, tallas a la vista, pago en un toque y vuestro consejo siempre a mano.',
                    complete='Completa tu equipo', ad3_btn='Ver novedades', pdp_h3='Cada producto,<br>listo para comprar.',
                    pdp_points=[('Fotos que venden', 'Cada pieza y cada acabado, como en la tienda.'), ('Talla y precio', 'Se eligen en la ficha, sin preguntar por DM.'),
                                ('Completa tu equipo', 'Más productos por pedido, más ticket medio.'), ('Asesoramiento', 'La duda se resuelve por WhatsApp sin salir de la ficha.')],
                    flow_new=[('Ve el producto', 'Instagram o anuncio'), ('Elige su talla', 'En la ficha'), ('Paga', 'Tarjeta, Bizum, Apple Pay')]),
}
for _v in NV.values():
    _v.update(wa_trust='te asesoramos por WhatsApp', wa_q='¿Dudas con el producto?', help2='Guía de compra',
              look_small=_v['complete'], look_p='Toca cada producto y añádelo a la cesta.', look_btn='Añadir los 3')

# Flow (mkjobs.CITY_BG y jobs37.SCENE)
CITY_BG = {'merceria': '#F1ECE5', 'arte': '#EEEEEA', 'artesania': '#EFE8DE', 'electro': '#EDF0F3', 'toys': '#EFECE6', 'deporte': '#EFE9E0'}
SCENE = {
    'merceria': 'a natural linen cloth on a light wooden worktable in a bright craft studio with soft daylight',
    'arte': "a light wooden artist's table in a bright studio with soft daylight",
    'artesania': 'a rustic wooden table in a sunlit artisan workshop with whitewashed walls',
    'electro': 'a bright modern kitchen with light stone worktops and soft daylight',
    'toys': 'a light wooden play table in a bright room with soft daylight',
    'deporte': 'a rustic wooden bench in the tack room of an Andalusian horse stable with warm light',
}
