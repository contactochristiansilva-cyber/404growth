# 21/11/2026: las 40 tiendas para el lunes 23/11 con el criterio nuevo (nivel de conciencia antes que seguidores).
# uso: python3 mkleads.py leads.json
# Cada fila: ig, nombre, nicho, seguidores, mediana de «me gusta», interacción %, publicaciones en 30 días, última (días),
# móvil, otro teléfono, WhatsApp publicado, zona, provincia, dirección, nivel (A anuncios / B web rota o sin tienda / C relleno),
# anuncios en Meta, estado de la web, cómo venden a distancia, qué es, avisos.
import json, sys

DAY = '2026-11-23'
R = [
 # --- A: anuncian en Meta y no tienen tienda online de verdad
 ('mercerialaverdadera', 'Mercería La Verdadera', 'merceria', 7863, 48, 0.61, 9, 1, '686794972', '', False, 'Jaén', 'Jaén', 'Plaza San Francisco, 4', 'A',
  '17 anuncios en la Biblioteca de Meta, 3 activos; el último del 13/11/2026', 'no tiene: solo un linkr.bio', 'bio: «#merceriaonline #enviosnacionales», «envíos a toda España»',
  'Mercería desde 1934, especialistas en artículos cofrades, hilaturas y bordados', []),
 ('tienda_tusovillos', 'Tienda Tu Ovillos', 'merceria', 5642, 53, 0.94, 2, 14, '635992021', '', True, 'Gijón', 'Asturias', '', 'A',
  '2 anuncios (junio de 2026)', 'no tiene: YouTube, canal y catálogo de WhatsApp', 'bio: «Envíos a toda la península»; catálogo en WhatsApp',
  'Tienda de lanas y crochet con patrones propios, vídeos y clases en Gijón', ['Publica menos: la última hace 14 días']),
 ('elcantodegreses', 'El Cantó de Greses', 'merceria', 2513, 3, 0.12, 11, 2, '616230144', '', True, 'Valencia (Benimaclet)', 'Valencia', '', 'A',
  '2 anuncios (febrero de 2026)', 'no tiene', 'bio: «💬 616 23 01 44», pedidos por WhatsApp',
  'Mercería de barrio especializada en indumentaria tradicional valenciana, encajes y cintas', ['Interacción baja (0,12 %)']),
 ('deleite.detela', 'Deleite de Tela', 'moda', 8211, 53, 0.65, 12, 3, '620220747', '', False, 'Murcia', 'Murcia', 'Calle Jabonerías, 10', 'A',
  '16 anuncios (diciembre de 2025), varios con «Murcia en la Vitrina»', 'no tiene: solo Google Maps', 'en sus publicaciones: envíos y pedidos por WhatsApp',
  'Tienda de moda mujer «ropa con alma, diseño con intención» en el centro de Murcia', []),
 ('abaco_moda', 'Ábaco Moda', 'moda', 38714, 50, 0.13, 12, 1, '644215351', '644214341', True, 'Plasencia y Montehermoso', 'Cáceres', 'C/ del Rey, 17 (Plasencia) · Plaza Constitución, 36 (Montehermoso)', 'A',
  '13 anuncios, 1 activo; el último de octubre de 2026', 'no tiene', 'bio: «Pedidos por WhatsApp bajo atención personalizada 644215351»',
  'Dos tiendas de moda mujer a buen precio en Plasencia y Montehermoso', ['Interacción baja para su tamaño (0,13 %)']),
 ('asaiadacarolinastore', 'A Saia da Carolina', 'moda', 10609, 710, 6.69, 6, 2, '611887761', '', False, 'Carballo', 'A Coruña', 'Rúa Igrexa, 28', 'A',
  'anuncios propios (marzo-abril de 2026)', 'no tiene: solo TikTok', 'asesoramiento personalizado por mensaje; no dice envíos en la bio',
  'Tienda física de moda mujer, calzado y complementos, con tallas curvy; la interacción más alta del lote (6,7 %)', ['No publica que el móvil sea WhatsApp']),
 ('jardilin.bilbao', 'Jardilín', 'sneakers', 5371, 51, 0.95, 1, 1, '674734958', '944160963', True, 'Bilbao', 'Bizkaia', 'Doctor Achucarro, 2', 'A',
  '2 anuncios (noviembre de 2025 y enero de 2026)', 'jardilin.es: catálogo sin precios ni carrito', 'bio: «venta online» y enlace de WhatsApp; la web dice «entrega en 2-3 días»',
  'Zapatería infantil y juvenil en Bilbao', ['Los teléfonos salen de su web (contacto), no de Instagram', 'Publica poco en el feed (1 en 30 días)']),
 ('laplateriadelsur', 'La Platería del Sur', 'joya', 12992, 275, 2.12, 7, 2, '615055511', '', True, '', '', '', 'A',
  '1 anuncio (3-7/11/2026)', 'no tiene: el catálogo es el de WhatsApp', 'bio: «24/48H 📦», «BIZUM O TRANSFER», catálogo de WhatsApp',
  'Joyería de plata y oro que ya vende por WhatsApp a toda España, con mucha interacción (2,1 %)', ['Falta la ciudad: no la pone en la bio ni en sus publicaciones']),
 ('lacasadelascuentass', 'La Casa de las Cuentas', 'joya', 2008, 13, 0.65, 6, 8, '679844424', '674318726', True, 'Huelva', 'Huelva', 'Mercado del Carmen, puesto 169', 'A',
  '1 anuncio (febrero de 2026)', 'no tiene', 'bio: «Envío a toda España», dos WhatsApp',
  'Bisutería artesanal personalizada en el Mercado del Carmen de Huelva', []),
 ('alexandre_joies', "L'Àlex Joies", 'joya', 4077, 29, 0.71, 7, 3, '633016344', '', True, 'Tarragona y Terrassa', 'Tarragona', '', 'A',
  'unos 100 anuncios (el último de agosto de 2026)', 'no tiene', 'bio: «📞/Wsp 633016344»',
  'Diseño y creación de joyas propias', ['Comprobar que tiene tienda física: la bio dice «Tarragona / Terrassa» sin dirección']),
 ('cristinaparlangelabores', 'Cristina Parlange Labores', 'merceria', 14375, 123, 0.86, 12, 2, '609574229', '913250981', True, 'Majadahonda', 'Madrid', 'Calle Morrones, 3', 'A',
  '11 anuncios (el último de octubre de 2026)', 'cristinaparlangelabores.com: web de la escuela, sin tienda ni precios', 'bio: enlace de WhatsApp; vende telas y materiales',
  'Tienda-escuela de patchwork, bordado, punto y crochet', []),
 ('aine_shoes', 'Áine Shoes', 'sneakers', 1747, 18, 1.03, 9, 2, '690312804', '', True, 'A Coruña', 'A Coruña', 'C/ Francisco Mariño, 12', 'A',
  '20 anuncios (enero-mayo de 2026)', 'aineshoes.com: PrestaShop con muy pocos productos a la vista', 'bio: «Envíos e info» y WhatsApp',
  'Zapatería de selección artesanal en A Coruña', ['Tiene web con carrito: es «web floja», no «sin web»']),
 ('lagatitapresumidashop', 'La Gatita Presumida', 'moda', 39669, 263, 0.66, 9, 1, '604006899', '', True, 'Sanxenxo', 'Pontevedra', 'Rúa dos Cesteiros, local 3', 'A',
  '2 anuncios (abril-julio de 2026)', 'lagatitapresumida.es: tiene carrito pero la tienda («/shop») da error 404 y no enseña precios', 'enlace de WhatsApp en la bio; envíos a toda España',
  'Boutique de moda en Sanxenxo con casi 40.000 seguidores', []),
 # --- A con web rota
 ('nama_collection_', 'Namá', 'moda', 22872, 76, 0.33, 11, 2, '678686464', '', False, 'Jerez de la Frontera', 'Cádiz', 'Avenida del Tío Pepe, 4', 'A',
  '1 anuncio (abril-mayo de 2026)', 'nama.es no funciona: Wix enseña «Reconnect Your Domain»', 'bio: «Envíos a toda España 48/72h, envíos 4,99 €»',
  'Tienda de ropa de mujer en Jerez', ['No publica que el móvil sea WhatsApp']),
 ('joyeriasinuandson', 'Sinu & Son', 'joya', 18890, 3, 0.02, 3, 5, '625490040', '', True, 'Barcelona', 'Barcelona', '', 'A',
  '4 anuncios (diciembre de 2025)', 'joyeriasinuandson.com no funciona: «Website unavailable»', 'bio: «Presupuestos al WhatsApp», «Envíos a todo Europa»',
  'Joyería personalizada en Barcelona', ['Interacción muy baja (0,02 %)', 'Comprobar la dirección de la tienda']),
 ('rk_sport23', 'RK Sport', 'moda', 3552, 27, 0.76, 9, 1, '691070383', '', True, 'Santa Coloma de Gramenet', 'Barcelona', 'Carrer de Sant Just, 10', 'A',
  'anuncios propios (diciembre de 2025 y julio de 2026)', 'rksport23.es no carga (error de certificado)', 'bio: «Envío a toda Europa», enlace de WhatsApp',
  'Tienda de ropa urbana y deportiva', []),
 # --- B: web rota o sin tienda, sin anuncios encontrados
 ('crisly_coquette', 'Crisly Coquette', 'moda', 2040, 16, 0.78, 9, 3, '665452136', '', False, '', '', '', 'B',
  'no encontrados', 'crislycoquette.es no carga (error de certificado; apunta a Shopify)', 'bio: «Tienda online», «Envíos a toda España, gratis desde 50 €»',
  'Tienda de moda y complementos de dos socias', ['Falta la ciudad']),
 ('modascarisma', 'Modas Carisma', 'moda', 11914, 21, 0.18, 9, 2, '621280022', '', False, '', '', '', 'B',
  'no encontrados', 'modascarisma.com no carga (error de certificado; apunta a Shopify)', 'bio: «10 % de descuento en tu primera compra» con enlace a la web que no funciona',
  'Tienda de moda mujer desde 2010', ['Falta la ciudad']),
 ('glamourmodavigo', 'Glamour Moda Vigo', 'moda', 2407, 30, 1.25, 3, 3, '679007824', '', True, 'Vigo', 'Pontevedra', 'Avenida de Camelias, 136', 'B',
  'no encontrados', 'glamourmoda.es no carga', 'bio: «Envío a domicilio», «Compra y recoge en tienda», WhatsApp',
  'Tienda de moda mujer en Vigo', []),
 ('chabeli_modas', 'Chabeli Modas', 'moda', 2461, 15, 0.61, 3, 2, '657195059', '', False, 'Jerez de la Frontera', 'Cádiz', 'Viveros Hermosín', 'B',
  'no encontrados', 'chabelimodas.com ya no existe (el dominio no resuelve)', 'bio: «Envíos a toda 🇪🇸»',
  'Tienda de ropa de mujer', ['Jerez: misma ciudad que Namá']),
 ('calzadosisaciolinares', 'Calzados Isacio', 'sneakers', 5466, 33, 0.6, 11, 1, '', '953656473', False, 'Linares', 'Jaén', 'Pasaje del Comercio, 5', 'B',
  'solo uno de la asociación de comerciantes de Linares (agosto de 2026)', 'calzadosisacio.com ya no existe (el dominio no resuelve)', 'bio: «envíos a toda España»',
  'Zapatería, moda y complementos en Linares', ['Solo publica fijo'], 50),
 ('modajoventj', 'TJ Moda y Calzado', 'moda', 13521, 16, 0.12, 2, 11, '645555374', '942522361', True, 'Solares', 'Cantabria', 'C/ Calvo Sotelo, 12', 'B',
  'no encontrados', 'tjmoda.com no responde', 'bio: «Envíos a España 24/48h», WhatsApp',
  'Tienda de moda y calzado', ['Publica menos: la última hace 11 días']),
 ('lormastories', 'Lorma', 'sneakers', 4593, 32, 0.7, 12, 1, '679776853', '', True, 'Avilés', 'Asturias', 'Avenida de Cervantes, 2', 'B',
  'no encontrados', 'lormastories.es da error 500 («Esta página no funciona»)', 'bio: «Envíos en menos de 24h», «Compra online» (con el enlace roto), grupo de WhatsApp',
  'Tienda de calzado, complementos, lencería y baño', []),
 ('masquedivasmoda', 'Más que Divas', 'moda', 12098, 43, 0.36, 9, 1, '652025669', '', True, 'Algeciras', 'Cádiz', 'Urb. Mirasierra, 23', 'B',
  'no encontrados', 'masquedivasmoda.com no carga (el dominio no tiene servidor)', 'bio: «Pedidos y precios vía WhatsApp», «Envíos a toda España»',
  'Moda y complementos', ['Comprobar que es tienda física: la dirección parece una urbanización']),
 ('nicolina.merceriatecnica', 'Nicolina Mercería Técnica', 'merceria', 3097, 43, 1.39, 3, 4, '611627261', '', False, 'Valencia', 'Valencia', 'C/ Cuenca, 38', 'B',
  'no encontrados', 'su web era de Google (negocio.site) y Google la cerró: da 404', 'bio: «Envíos a toda España»',
  'Mercería técnica en Valencia', []),
 ('lastijerasdegloria', 'Las Tijeras de Gloria', 'merceria', 2003, 17, 0.85, 9, 5, '649113844', '', False, 'Alicante', 'Alicante', 'Calle Manuel Antón, 4', 'B',
  'no encontrados', 'su web es una página de Canva, sin tienda', 'no lo dice en la bio',
  'Tienda especializada en patchwork', ['No dice en la bio que envíe']),
 ('hilalalibelula', 'Hila la Libélula', 'merceria', 13181, 159, 1.21, 8, 5, '669897643', '', True, 'Miranda de Ebro', 'Burgos', 'Calle Concepción Arenal, 19', 'B',
  'no encontrados', 'hilalalibelula.com: Wix sin tienda ni precios', 'bio: «Envíos a todo España»',
  'Tienda de patchwork con 13.000 seguidores', []),
 # --- C: relleno (venden a distancia, nichos prioritarios, sin anuncios ni web)
 ('herboristeria.natussi', 'Herbolario Natussi', 'suplementos', 1908, 30, 1.57, 8, 3, '633601240', '', True, 'Archena', 'Murcia', '', 'C',
  'no (los anuncios con «Natussi» son de otro anunciante)', 'no tiene', 'pedidos por WhatsApp (enlace en la bio)',
  'Herbolario y ecotienda con fitoterapia y suplementación', []),
 ('paquigutierrezcalzados', 'Paqui Gutiérrez Calzados', 'sneakers', 2452, 38, 1.55, 11, 1, '686828819', '686828818', True, '', '', '', 'C',
  'no', 'no tiene', 'bio: «Hacemos envíos», precios y móvil en cada publicación',
  'Zapatería con marcas como Gioseppo', ['Falta la ciudad']),
 ('eva_zapateria_y_complementos', 'Eva Zapatería y Complementos', 'sneakers', 3083, 21, 0.68, 12, 1, '665060573', '665065073', True, 'Armilla', 'Granada', 'Calle Real de Motril, 5, local 3', 'C',
  'no', 'no tiene', 'bio: «Envíos península 4,99 €», «Pagos Bizum y PayPal», WhatsApp',
  'Zapatería y complementos', []),
 ('lananegra_valencia', 'Lana Negra', 'merceria', 3535, 56, 1.58, 9, 5, '620664421', '', True, 'Valencia', 'Valencia', '', 'C',
  'no (el nombre lo usan otros anunciantes)', 'no tiene', 'enlace de WhatsApp en la bio',
  'Mercería de lanas con talleres creativos', ['No dice en la bio que envíe']),
 ('claus_pamplona', "Clau's Calzado y Complementos", 'sneakers', 4533, 12, 0.26, 10, 2, '680550094', '', False, 'Pamplona', 'Navarra', 'C/ San Miguel, 5', 'C',
  'no', 'no tiene', 'bio: «Envío por MD 24/48h»',
  'Zapatería y complementos en el centro de Pamplona', []),
 ('coserycantarml', 'Coser & Cantar', 'merceria', 1850, 37, 2.0, 12, 4, '687371531', '958320818', True, 'Loja', 'Granada', 'Avda. de los Ángeles, 31', 'C',
  'no', 'no tiene', 'WhatsApp en la bio',
  'Mercería y lencería', ['No dice en la bio que envíe']),
 ('gironessedaoficial', 'Gironés Seda', 'merceria', 14771, 157, 1.06, 4, 7, '662498306', '', True, 'Manises', 'Valencia', 'C/ Maestro Serrano, 14', 'C',
  'no', 'no tiene', 'enlace de WhatsApp en la bio',
  'Fabricantes de tejidos para indumentaria tradicional valenciana', ['Comprobar que venden al público: se presentan como fabricantes']),
 ('merceriamabe', 'Mercería-Corsetería Mabe', 'merceria', 1792, 83, 4.63, 6, 3, '601609052', '', False, 'Alicante', 'Alicante', '', 'C',
  'no', 'no tiene', 'no lo dice en la bio',
  'Mercería y corsetería desde 1990, especialistas en tallas de sujetador', ['No dice en la bio que envíe', 'El móvil sale de sus publicaciones']),
 ('saobymedialdea', 'SAÓ Jewels', 'joya', 3455, 3, 0.09, 4, 10, '672081810', '', True, 'Sant Feliu de Guíxols', 'Girona', 'Carrer Major, 43', 'C',
  'no', 'no tiene', 'directos y enlace de WhatsApp',
  'Tienda de joyas y complementos para regalo', ['Interacción baja (0,09 %)']),
 ('tejidoslaine', 'Tejidos Laine', 'merceria', 2600, 24, 0.92, 11, 4, '629691892', '', False, 'Valencia', 'Valencia', 'C/ San Vicente, 110', 'C',
  'no', 'no tiene', 'no lo dice en la bio',
  'Tienda de tejidos desde 1964, con confección', ['No dice en la bio que envíe']),
 ('lamerceria__', 'La Mercería', 'merceria', 2208, 26, 1.18, 4, 4, '609831281', '', False, 'Santa Coloma de Farners', 'Girona', 'Carrer Major, 2', 'C',
  'no', 'no tiene', 'no lo dice en la bio',
  'Mercería con lanas, telas, arreglos y talleres', ['No dice en la bio que envíe']),
 ('zapateria_moda_paula', 'Zapatería y Moda Paula', 'sneakers', 6349, 23, 0.36, 12, 4, '661623380', '', True, 'La Cañada (Almería)', 'Almería', 'Plaza Antonio de Torres, 12', 'C',
  'no', 'no tiene', 'bio: «Envíos 24/48h», «Bizum o transferencia», «Pedidos por WhatsApp»',
  'Zapatería y moda', ['La Cañada: en el lote 38 ya hubo otra tienda de allí (La Cañada Showroom)']),
 ('patchworkandcompany', 'Patchwork and Company', 'merceria', 4100, 93, 2.27, 5, 5, '629233169', '', True, 'Móstoles', 'Madrid', 'Calle Pintor Rivera, 5', 'C',
  'no', 'no tiene', 'enlace de WhatsApp en la bio',
  'Tienda de telas de patchwork con clases presenciales', ['No dice en la bio que envíe']),
]

NW = {'cosmetica': 10, 'suplementos': 10, 'merceria': 8, 'sneakers': 8, 'joya': 5, 'moda': 0}
out = []
for r in R:
    (ig, name, ni, f, med, eng, n30, last, mob, fijo2, wa, zone, region, addr, tier, ads, shop, sig, what, aviso) = r[:20]
    pr = r[20] if len(r) > 20 else None
    score = {'A': 70, 'B': 55, 'C': 40}[tier] + NW[ni] + (5 if eng >= 1.5 else 0) + (3 if wa else 0) + (3 if f >= 10000 else 0) + (3 if last <= 4 else 0)
    x = {'day': DAY, 'niche': ni, 'name': name, 'ig': ig, 'f': f, 'med': med, 'eng': eng, 'n30': n30, 'lastDays': last,
         'mobile': mob, 'waPub': wa, 'zone': zone or 'por confirmar', 'region': region or 'por confirmar', 'address': addr,
         'tier': tier, 'score': min(score, 99), 'ads': ads, 'shop': shop, 'sig': sig, 'what': what, 'aviso': aviso}
    if fijo2:
        if fijo2.startswith(('6', '7')):
            x['mobile2'] = fijo2
        else:
            x['fijo'] = fijo2
    if not mob:
        x['mobile'] = ''
    x['priority'] = pr or (90 if tier == 'A' else 80 if tier == 'B' else 70)
    out.append(x)
assert len(out) == 40 and len({x['ig'] for x in out}) == 40
out.sort(key=lambda x: -x['score'])
json.dump(out, open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
from collections import Counter
print(len(out), Counter(x['tier'] for x in out), Counter(x['niche'] for x in out))
