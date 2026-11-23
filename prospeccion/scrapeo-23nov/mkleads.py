# 23/11/2026: 50 tiendas más con los filtros del lote del 23/11 (scrapeo-22nov): moda, joyería, perfumería y calzado;
# nada de mercerías, artesanía ni muebles; nivel de conciencia (A: anuncian en Meta; B: web rota, cerrada o casi vacía;
# C: venden a distancia sin anuncios ni web), activas, con móvil o WhatsApp, sin Canarias, nada árabe y fuera del CRM.
# Los días (24 al 27/11) se reparten para que no haya dos del mismo pueblo el mismo día (con lo que ya hay en esos lotes).
# uso: python3 mkleads.py leads.json
import json, sys, unicodedata, re

DAYS = ['2026-11-24', '2026-11-25', '2026-11-26', '2026-11-27']
TAKEN = {'2026-11-24': {'vigo', 'jerez de la frontera', 'plasencia'}, '2026-11-25': {'vigo', 'jerez de la frontera'},
         '2026-11-26': {'jerez de la frontera'}, '2026-11-27': set()}
IG = {  # f, mediana de «me gusta», interacción %, publicaciones en 30 días, días desde la última
 "alquilerflamencamadrid":[4122,38,0.92,8,1],"sondelunares_modaflamenca":[3199,49,1.53,6,7],"inma_benicio":[5498,64,1.16,9,1],"prettyroseboutique":[9706,43,0.44,7,0],"mareamodas":[2097,6,0.29,12,0],"carlosboutique03":[2640,10,0.38,12,3],"orquessa":[4267,363,8.51,12,1],"joyeriaazorin":[3293,130,3.95,9,2],"almermadrid":[4505,34,0.75,2,3],"s.d_calzados":[2352,16,0.68,10,2],"arenaymarmoda":[4391,56,1.28,12,4],"ladano_perfumeria":[2296,66,2.87,12,2],"modanaomi":[2369,18,0.76,1,4],"carmonacalzados":[1619,29,1.79,4,3],"abigu_complementos":[9863,69,0.7,12,1],"decomodashop":[10964,134,1.22,12,3],"bali_aviles":[3275,36,1.1,12,6],"andyswomanmoda":[3364,31,0.92,7,0],"isabelhernandezflamenca":[34793,524,1.51,10,3],"fondodearmario_":[7157,89,1.24,8,1],"modaflamencavictoria":[2295,40,1.74,11,3],"rociera_moda_flamenca":[4691,23,0.49,5,4],"modasvictoriass":[5048,21,0.42,11,0],"_rachelandyou_":[11294,64,0.57,12,3],"cosadetresvlc":[7064,161,2.28,6,3],"igual_roba_i_complements":[5300,29,0.55,11,2],"ladescreida.shop":[2691,48,1.78,10,1],"you_too_moda_hombre":[2313,48,2.08,8,1],"calzadossanti":[3157,17,0.54,9,2],"bohothaibycarmela":[7087,81,1.14,9,1],"nubamodas":[1787,18,1.01,4,5],"martinelbisutero":[2560,14,0.55,5,11],"galeriasabreu":[2550,27,1.06,10,5],"hacheubeda":[2282,14,0.61,12,1],"egomoda.shop":[3769,15,0.4,12,4],"_anselmogalan_":[11944,61,0.51,12,4],"tiendalacoquetaa":[4084,34,0.83,4,13],"bella89woman":[2690,31,1.15,12,1],"zapatilleriaisabelcarballo":[2052,17,0.83,12,3],"mibolso2021":[3029,21,0.69,7,5],"boutiquemarisa_cris":[5564,197,3.54,12,1],"udalaitzshop":[7949,218,2.74,2,1],"saranunezlara":[2246,8,0.36,12,0],"cosquillasferrol":[5834,18,0.31,12,0],"cachetxurdinaga":[4111,36,0.88,12,2],"basikcollection":[10425,74,0.71,11,1],"anacalzadosdh":[2594,10,0.39,1,9],"olivia_by_sa":[1961,19,0.97,12,1],"pisoton_calzado":[2576,40,1.55,10,5],"twinsvalencia":[13697,53,0.39,3,6]}

MAPS = 'el móvil sale de su ficha de Google Maps'
# ig, nombre, nicho, móvil, otro móvil, fijo, publica el móvil como WhatsApp, publica el fijo como WhatsApp, pueblo, provincia, dirección,
# tiendas, nivel, anuncios, tienda online, venta a distancia, qué es, avisos, nota del móvil
R = [
 # --- A: anuncian en Meta y no tienen tienda online de verdad
 ('alquilerflamencamadrid', 'Los Lunares de Piluka', 'moda', '627094947', '675935072', '', True, False, 'Madrid', 'Madrid', '', 1, 'A',
  'unos 17 anuncios de «Los lunares de Piluka» y «Alquiler Flamenco Madrid» (el último, del 1/11/2026)',
  'alquilerflamencamadrid.com no carga, y trajesdeflamencamadrid.com (la de su ficha de Google) está cerrada con contraseña',
  'publicaciones: «Hacemos envíos», «Escríbenos por privado», «escríbenos al WhatsApp»',
  'Vestidos de flamenca a la venta y en alquiler en Madrid', ['Atienden solo con cita previa'], 'el otro móvil sale de su ficha de Google Maps'),
 ('sondelunares_modaflamenca', 'Son de Lunares', 'moda', '722678879', '670779236', '', False, False, 'Valencia', 'Valencia', 'C/ Balmes, 43', 1, 'A',
  '2 anuncios (el último, de noviembre de 2026)', 'sondelunaresmodaflamenca.es: WooCommerce con solo 11 productos',
  'no lo dice en Instagram; su web tiene carrito con 11 productos',
  'Tienda de moda flamenca y danza española en Valencia', ['No dice en Instagram que haga envíos'], ''),
 ('inma_benicio', 'Inma Benicio', 'moda', '654172220', '', '', False, False, 'Córdoba', 'Córdoba', '', 1, 'A',
  '3 anuncios (el último, del 7/05/2026)', 'inmabenicio.es da error de WordPress',
  'no lo dice en Instagram (cita previa por teléfono)', 'Diseñadora jerezana de vestidos de flamenca y de fiesta en Córdoba',
  ['Es diseñadora con cita previa: comprobar que tiene tienda física', 'No dice en Instagram que haga envíos'], ''),
 ('prettyroseboutique', 'Pretty Rose Boutique', 'moda', '', '', '976097374', False, False, 'Zaragoza', 'Zaragoza', 'Calle Delicias, 54', 1, 'A',
  '13 anuncios (el último, del 22/09/2026)', 'prettyrose.es: WooCommerce con 20 productos y cerrada con contraseña',
  'bio: «Bizum-Revolut-Efectivo», «Envíos a toda España 24/48h»', 'Boutique de moda de mujer en Zaragoza',
  ['Solo publica fijo'], ''),
 ('mareamodas', 'Marea Modas', 'moda', '644713161', '', '', True, False, 'Málaga', 'Málaga', 'Calle José Fernando Carvajal, 15 (Campanillas)', 1, 'A',
  '1 anuncio (junio de 2026)', 'mareamodas.es: WooCommerce con solo 9 productos',
  'bio: «WhatsApp: 644713161», «Envíos Península 48/72H - 4.99€»', 'Ropa, calzado y complementos de mujer en Campanillas (Málaga)',
  ['Interacción baja (0,29 %)'], ''),
 ('carlosboutique03', 'Carlos Boutique', 'moda', '631427031', '662435000', '', False, False, 'Madrid', 'Madrid', 'Calle Teruel, 32', 1, 'A',
  '9 anuncios (el último, de noviembre de 2026)', 'no tiene', 'publicaciones: «ENVÍO TODA ESPAÑA»',
  'Tienda de moda en Madrid (Tetuán), abierta de lunes a domingo', [], ''),
 ('orquessa', 'Orquessa', 'joya', '624464353', '', '', False, False, 'Valencia', 'Valencia', '', 1, 'A',
  '1 anuncio (junio de 2026)', 'no tiene', 'bio: «Envíos a toda España y Europa»; publicaciones: «Hacemos envíos»',
  'Joyas hechas con flores reales, con muchísima interacción (8,5 %)',
  ['No pone la dirección en Instagram: comprobar que tiene tienda física'], MAPS),
 ('joyeriaazorin', 'Joyería Azorín', 'joya', '', '', '968791951', False, False, 'Yecla', 'Murcia', 'C/ Hospital, 23', 1, 'A',
  '4 anuncios (el último, de noviembre de 2026)', 'no tiene', 'bio: «Hacemos envíos nacionales gratis»',
  'Joyería en Yecla con mucha interacción (3,95 %)', ['Solo tiene fijo (sale de su ficha de Google Maps)'], ''),
 ('almermadrid', 'Almer Joyas Madrid', 'joya', '', '', '914310908', False, False, 'Madrid', 'Madrid', 'C/ Hermosilla, 52', 1, 'A',
  '1 anuncio (noviembre de 2026)', 'no tiene', 'publicaciones: envíos',
  'Joyería de piezas únicas y a medida en el barrio de Salamanca', ['Solo publica fijo', 'Publica poco (2 en 30 días)'], ''),
 ('s.d_calzados', 'Santo Domingo Calzados', 'sneakers', '722837823', '', '', False, False, 'Sanlúcar de Barrameda', 'Cádiz', '', 1, 'A',
  '5 anuncios (enero de 2026)', 'santodomingocalzados.com no se pudo abrir (Cloudflare bloquea la visita)', 'bio: «Envíos a toda España»',
  'Zapatería en Sanlúcar de Barrameda', ['Comprobar su web santodomingocalzados.com: no se pudo abrir'], ''),
 ('arenaymarmoda', 'Arena y Mar', 'moda', '617780237', '', '', True, False, 'Alicante', 'Alicante', 'C/ del Teatro, 34', 1, 'A',
  '3 anuncios (junio de 2026)', 'arenaymarmoda.com (Squarespace): catálogo sin carrito; el pedido se hace por WhatsApp',
  'bio: «VENTA ONLINE», WhatsApp', 'Boutique multimarca mediterránea, Premio Comercio Alicante 2023', [], ''),
 ('ladano_perfumeria', 'Ládano Perfumería', 'cosmetica', '614125962', '', '', False, False, 'Vila-real', 'Castellón', 'C/ Colom, 14', 1, 'A',
  '5 anuncios (el último, del 18/11/2026)', 'ladanoperfumeria.com: web sin tienda (no se puede comprar)', 'bio: «Envíos España y Europa»',
  'Perfumería nicho y de autor (marcas originales, sin equivalencias), con mucha interacción (2,9 %)', [], ''),
 ('modanaomi', 'Modas Naomi', 'moda', '601204829', '', '', False, False, 'Córdoba', 'Córdoba', 'Av. El Cairo, 2 · Av. Almogávares, 38', 2, 'A',
  '9 anuncios (mayo de 2026)', 'modanaomi.es: web sin productos', 'bio: «Envíos Nacionales e Internacionales»',
  'Dos tiendas de moda de mujer en Córdoba', ['Publica poco en Instagram (1 en 30 días)'], ''),
 ('carmonacalzados', 'Calzados Carmona', 'sneakers', '624169398', '', '954447090', False, False, 'Lebrija', 'Sevilla', 'C/ José Sánchez de Alva, 27', 3, 'A',
  '6 anuncios (marzo de 2026)', 'no tiene', 'no lo dice en Instagram; tres tiendas (Lebrija, Las Cabezas y Sanlúcar)',
  'Zapatería con 40 años y tres tiendas', ['No dice en Instagram que haga envíos'], ''),
 ('abigu_complementos', 'Abigú Complementos', 'joya', '647456501', '623154024', '', False, False, 'Vilagarcía de Arousa', 'Pontevedra', '', 2, 'A',
  '1 anuncio (julio de 2026)', 'no tiene', 'bio: «Envíos a toda España»; directos de bolsos',
  'Tienda de joyas y complementos en Pontevedra y Vilagarcía de Arousa', [], ''),
 ('decomodashop', 'Decomoda', 'moda', '', '', '938963787', False, True, 'Sant Pere de Ribes', 'Barcelona', 'C/ Ildefons Cerdà, 15-17', 1, 'A',
  '16 anuncios (el último, del 5/11/2026)', 'no tiene: vende con el catálogo de WhatsApp',
  'bio: «venta online desde nuestro Catálogo de WhatsApp»; publicaciones: «Escríbenos por WhatsApp al 93 896 37 87»',
  'Moda real para mujeres, de la talla 34 a la 50', [], ''),
 ('bali_aviles', 'Bali', 'sneakers', '669319094', '', '', False, False, 'Avilés', 'Asturias', 'C/ José Cueto, 1', 1, 'A',
  '9 anuncios (abril de 2026)', 'no tiene', 'no lo dice en Instagram', 'Calzado, moda y complementos en Avilés',
  ['No dice en Instagram que haga envíos'], ''),
 ('andyswomanmoda', "Andy's Woman", 'moda', '686490826', '', '', False, False, 'Barbastro', 'Huesca', 'C/ Corona de Aragón, 26', 1, 'A',
  "1 anuncio de «Andy's Woman Junior» (noviembre de 2026)", 'no tiene', 'bio: «Hacemos envíos 24/48h»',
  'Tienda de moda multimarca en Barbastro (también @aw_andys)', [], ''),
 # --- B: web rota, cerrada o casi vacía
 ('isabelhernandezflamenca', 'Isabel Hernández Flamenca', 'moda', '691956060', '606125020', '', False, False, 'Arroyomolinos de León', 'Huelva', '', 1, 'B',
  'no', 'isabelhernandez.es: WooCommerce con solo 20 productos', 'presupuestos por su web; atelier con cita previa',
  'Diseñadora de moda flamenca con atelier en Arroyomolinos de León; 34.800 seguidores y mucha interacción (1,5 %)',
  ['Atelier con cita previa: comprobar que vende en tienda'], 'el otro móvil sale de su ficha de Google Maps'),
 ('fondodearmario_', 'Fondo de Armario', 'moda', '665925641', '722609341', '', True, False, 'Estepona', 'Málaga', 'Av. España, 140', 1, 'B',
  'no', 'fondodearmarioshop.com: WooCommerce con solo 22 productos', 'bio: «Envíos a toda España», «Atención personalizada por WA»',
  'Tienda de ropa de mujer en Estepona', [], ''),
 ('modaflamencavictoria', 'Victoria Mena Moda Flamenca', 'moda', '696778066', '', '937887412', False, False, 'Terrassa', 'Barcelona', 'Calle Bailén, 50', 1, 'B',
  'no', 'victoriamena.es: cerrada con contraseña', 'publicaciones: envíos a la península',
  'Moda flamenca y complementos en Terrassa, con mucha interacción (1,7 %)', [], ''),
 ('rociera_moda_flamenca', 'Rociera Moda Flamenca', 'moda', '667796357', '', '', True, False, 'Córdoba', 'Córdoba', '', 1, 'B',
  'no', 'rociera.es: web sin tienda', 'bio: «Tienda física y online», WhatsApp; «Escríbenos por privado con la talla»',
  'Trajes de flamenca a medida, con más de 35 años de experiencia', ['Interacción baja (0,49 %)'], ''),
 ('modasvictoriass', "Modas Victoria's", 'moda', '616238179', '', '', False, False, 'Córdoba', 'Córdoba', '', 1, 'B',
  'no', 'modasvictorias.com: muy pocos productos', 'publicaciones: «se hacen envíos»',
  'Ropa juvenil, tallas grandes, lencería y complementos en Córdoba', ['Interacción baja (0,42 %)'], ''),
 ('_rachelandyou_', 'Rachel & You', 'moda', '620039670', '', '', False, False, 'Benicarló', 'Castellón', 'C/ Rei En Jaume, 51', 1, 'B',
  'no', 'rachelandyou.es: web sin tienda', 'no lo dice en Instagram (multimarca con asesoría de imagen)',
  'Tienda multimarca de mujer en Benicarló', ['No dice en Instagram que haga envíos'], ''),
 ('cosadetresvlc', 'Cosa de Tres', 'moda', '644338713', '', '', False, False, 'Benifaió', 'Valencia', 'C/ Santa Bárbara, 19', 1, 'B',
  'no', 'cosadetres.com: web sin tienda', 'bio: «ENVÍOS A TODA ESPAÑA»; directos',
  'Tienda de moda en Benifaió con mucha interacción (2,3 %)', [], ''),
 ('igual_roba_i_complements', 'Igual Shop', 'moda', '649726935', '', '', False, False, 'Masquefa', 'Barcelona', 'Calle Sant Pere, 8', 1, 'B',
  'no', 'igualshop.com: web sin tienda (no se puede comprar)', 'bio: «Envíos a toda la península, 48h, más de 70 € envío gratuito»',
  'Ropa y complementos en Masquefa', [], ''),
 ('ladescreida.shop', 'La Descreída', 'joya', '613151680', '', '', True, False, 'El Puerto de Santa María', 'Cádiz', 'C/ Manuel Jesús Viñas', 1, 'B',
  'no', 'ladescreida.com: tiene carrito pero no se ven precios', 'bio: «Envíos a toda España», WhatsApp; directos',
  'Moda y joyería hecha a mano, con mucha interacción (1,8 %)', ['Comprobar su web ladescreida.com: puede que ya venda'], ''),
 # --- C: venden a distancia, sin anuncios ni web
 ('you_too_moda_hombre', 'You Too', 'moda', '665810432', '', '947040515', True, False, 'Burgos', 'Burgos', 'C/ Santiago Apóstol, 52', 1, 'C',
  'no', 'no tiene', 'bio: «Envíos a toda España», «Pedidos por DM o WhatsApp»',
  'Moda de hombre en Burgos desde hace 24 años, con mucha interacción (2,1 %)', [], ''),
 ('calzadossanti', 'Calzados Santi', 'sneakers', '618675966', '', '', True, False, 'Jerez de la Frontera', 'Cádiz', 'Parque Atlántico, bloque 13', 1, 'C',
  'no', 'no tiene', 'bio: «Pedidos por WhatsApp», «Envíos a toda España (24h/72h) — 6€»', 'Zapatería de barrio desde el año 2000', [], ''),
 ('bohothaibycarmela', 'Bohothai by Carmela', 'moda', '639288604', '678430416', '', False, False, 'Burjassot', 'Valencia', 'C/ Mendizábal, 105', 1, 'C',
  'no', 'no tiene', 'bio: «pedidos 639288604-678430416», «envíos 24/48h»', 'Moda y complementos de estilo boho', [], ''),
 ('nubamodas', 'Nubamodas', 'moda', '656967788', '', '', False, False, 'Málaga', 'Málaga', 'C/ Cristo de la Epidemia, 60', 1, 'C',
  'no', 'no tiene', 'bio: «Pedido al 656967788 bizum», «envíos en 24/48 horas»', 'Tienda de moda en Málaga', [], ''),
 ('martinelbisutero', 'Martín el Bisutero', 'joya', '640017861', '', '', True, False, 'por confirmar', 'por confirmar', '', 1, 'C',
  'no', 'no tiene', 'publicaciones: «enviamos a toda España», «Escríbenos al 640 017 861»',
  'Bisutería personalizada con cristales de Swarovski', ['Falta la ciudad: no la pone en Instagram', 'La última publicación es de hace 11 días'], ''),
 ('galeriasabreu', 'Galerías Abreu', 'moda', '628555012', '', '959321019', True, False, 'Ayamonte', 'Huelva', 'C/ Paseo de la Ribera, 4', 1, 'C',
  'no', 'no tiene', 'bio: «Pedidos por MD o whatsapp», «Envío GRATIS compras superiores a 50€»', 'Tienda de moda en Ayamonte', [], ''),
 ('hacheubeda', 'Hache Úbeda', 'moda', '619646320', '', '', False, False, 'Úbeda', 'Jaén', 'C/ Obispo Cobos, 20', 1, 'C',
  'no', 'no tiene', 'bio: «ENVÍO ESPAÑA»', 'Multimarca con firmas españolas en Úbeda', [], ''),
 ('egomoda.shop', 'Ego Moda', 'moda', '611084185', '', '', False, False, 'La Campana', 'Sevilla', 'C/ Baleares, 17', 1, 'C',
  'no', 'no tiene', 'bio: «Envíos 4,99€ 24/48 horas», «Para comprar 611 084 185»',
  'Vestidos de invitada y complementos, con tienda de hombre (@egomoda.man)', ['Interacción baja (0,4 %)'], ''),
 ('_anselmogalan_', 'Anselmo Galán', 'moda', '623634627', '617555254', '', False, False, 'Lebrija', 'Sevilla', 'C/ Andrés Sánchez de Alba, 5', 1, 'C',
  'no', 'no tiene', 'bio: «Envíos a toda España 24/48h»', 'Moda y complementos de mujer en Lebrija (11.900 seguidores)', [], ''),
 ('tiendalacoquetaa', 'La Coqueta', 'moda', '636785495', '', '856661328', False, False, 'Jerez de la Frontera', 'Cádiz', 'Calle Antonio Chacón Ferral', 1, 'C',
  'no', 'no tiene', 'bio: «Envíos 2.99€», «Pedidos 636 78 54 95»', 'Tienda de ropa', ['La última publicación es de hace 13 días', 'Comprobar la ciudad (la calle y el fijo apuntan a Jerez)'], ''),
 ('bella89woman', 'Bella89 Woman', 'moda', '630501969', '', '', False, False, 'Arganda del Rey', 'Madrid', 'Calle Santa Teresa, 6, local 1', 1, 'C',
  'no', 'no tiene', 'bio: «se hacen envíos a toda España», «teléfono de pedidos 630501969»', 'Tienda de moda en Arganda del Rey', [], ''),
 ('zapatilleriaisabelcarballo', 'Zapatillería Isabel', 'sneakers', '645145523', '', '', True, False, 'Carballo', 'A Coruña', 'Rúa Camiño Novo, 9', 1, 'C',
  'no', 'no tiene', 'WhatsApp en la bio', 'Zapatillas de casa, sandalias, alpargatas y calzado de confort', ['No dice en Instagram que haga envíos'], ''),
 ('mibolso2021', 'Mi Bolso', 'moda', '692515389', '', '', False, False, 'por confirmar', 'por confirmar', '', 1, 'C',
  'no', 'no tiene', 'bio: «Envíos 24/48H»; directos en Instagram; «ENVÍOS A TODA LA PENÍNSULA»', 'Moda y complementos de mujer',
  ['Falta la ciudad: no la pone en Instagram'], ''),
 ('boutiquemarisa_cris', 'Boutique Marisa', 'moda', '691168525', '', '', False, False, 'Badalona', 'Barcelona', 'C/ Guifré, 105', 1, 'C',
  'no', 'no tiene', 'no lo dice en Instagram', 'Tienda multimarca desde 1989, con mucha interacción (3,5 %)',
  ['No dice en Instagram que haga envíos', 'Su correo es de boutiquemarisa.com: comprobar si tiene web'], ''),
 ('udalaitzshop', 'Udalaitz', 'moda', '607991006', '', '', False, False, 'Vitoria-Gasteiz', 'Álava', 'Postas, 5', 1, 'C',
  'no', 'no tiene', 'bio: «Ventas a distancia (+34) 607991006»', 'Marca vasca con fabricación propia y mucha interacción (2,7 %)',
  ['Publica poco (2 en 30 días)'], ''),
 ('saranunezlara', 'Sara Núñez', 'moda', '626114388', '', '', False, False, 'Alcalá de Guadaíra', 'Sevilla', 'Calle La Plata, 17', 1, 'C',
  'no', 'no tiene', 'no lo dice en Instagram', 'Complementos y trajes de flamenca', ['No dice en Instagram que haga envíos', 'Interacción baja (0,36 %)'], ''),
 ('cosquillasferrol', 'Cosquillas', 'moda', '665574775', '', '', False, False, 'Ferrol', 'A Coruña', 'Rúa Carme, 20', 1, 'C',
  'no', 'no tiene', 'no lo dice en la bio', 'Vestidos de invitada para bodas, comuniones y graduaciones', ['Interacción baja (0,31 %)'], ''),
 ('cachetxurdinaga', 'Modas Caché', 'moda', '661403321', '', '944129581', True, False, 'Bilbao', 'Bizkaia', 'Arbidea, 8 (Txurdinaga)', 1, 'C',
  'no', 'no tiene', 'bio: «Compra directa por WhatsApp»', 'Multimarca en Txurdinaga (Bilbao)', [], ''),
 ('basikcollection', 'Basik', 'moda', '653512074', '', '', True, False, 'por confirmar', 'por confirmar', '', 1, 'C',
  'no', 'no tiene', 'bio: «Pedidos por WhatsApp», catálogo', 'Tienda de moda que vende por WhatsApp (10.400 seguidores)',
  ['Falta la ciudad y comprobar que tiene tienda física'], ''),
 ('anacalzadosdh', 'Ana Calzados', 'sneakers', '640357682', '', '', False, False, 'Dos Hermanas', 'Sevilla', 'Calle de la Mina, 16', 1, 'C',
  'no', 'no tiene', 'bio: «Tienda física y online», «ENVÍOS 24/48»', 'Zapatería de mujer en Dos Hermanas',
  ['Publica poco (1 en 30 días, la última hace 9 días)', 'Interacción baja (0,39 %)'], ''),
 ('olivia_by_sa', 'Olivia', 'moda', '612254555', '', '', False, False, 'Solares', 'Cantabria', 'Avda. Calvo Sotelo, 4-6', 1, 'C',
  'no', 'no tiene', 'bio: «Pedidos y asesoramiento 612254555»', 'Ropa, calzado y complementos en Solares', [], ''),
 ('pisoton_calzado', 'Pisotón', 'sneakers', '615584170', '', '', False, False, 'San Clemente', 'Cuenca', 'C/ Boteros, 50', 2, 'C',
  'no', 'no tiene', 'bio: «Envíos a toda España», pedidos por MD', 'Calzado y complementos, con tiendas en Villarrobledo y San Clemente', [], MAPS),
 ('twinsvalencia', 'Twins', 'moda', '', '', '960239479', False, False, 'Valencia', 'Valencia', '', 1, 'B',
  'no', 'twinsmoda.es (la de su ficha de Google) no carga', 'bio: «Envíos 24/48h», «Pide tu look por DM»',
  'Looks de fiesta, eventos y casual (13.700 seguidores)', ['Solo publica fijo', 'Interacción baja (0,39 %)'], ''),
]
NB = {'cosmetica': 10, 'suplementos': 10, 'sneakers': 8, 'joya': 5, 'moda': 0}

def key(z):
    return unicodedata.normalize('NFKD', z).encode('ascii', 'ignore').decode().lower()

WEB = {"alquilerflamencamadrid": "alquilerflamencamadrid.com", "sondelunares_modaflamenca": "sondelunaresmodaflamenca.es", "inma_benicio": "inmabenicio.es", "prettyroseboutique": "prettyrose.es", "mareamodas": "mareamodas.es", "s.d_calzados": "santodomingocalzados.com", "arenaymarmoda": "arenaymarmoda.com", "ladano_perfumeria": "ladanoperfumeria.com", "modanaomi": "modanaomi.es", "isabelhernandezflamenca": "isabelhernandez.es", "fondodearmario_": "fondodearmarioshop.com", "modaflamencavictoria": "victoriamena.es", "rociera_moda_flamenca": "rociera.es", "modasvictoriass": "modasvictorias.com", "_rachelandyou_": "rachelandyou.es", "cosadetresvlc": "cosadetres.com", "igual_roba_i_complements": "igualshop.com", "ladescreida.shop": "ladescreida.com", "twinsvalencia": "twinsmoda.es"}
out = []
for (ig, name, ni, mob, mob2, fijo, waPub, waFijo, zone, region, addr, centers, tier, ads, shop, sig, what, aviso, mnote) in R:
    f, med, eng, n30, last = IG[ig]
    score = {'A': 70, 'B': 55, 'C': 40}[tier] + NB[ni] + (5 if eng >= 1.5 else 0) + (3 if (waPub or waFijo) else 0) + (3 if f >= 10000 else 0) + (3 if last <= 4 else 0)
    x = dict(niche=ni, name=name, ig=ig, f=f, med=med, eng=eng, n30=n30, lastDays=last, mobile=mob, mobile2=mob2, fijo=fijo,
             waPub=waPub, waFijo=waFijo, zone=zone, region=region, address=addr, centers=centers, tier=tier, score=score,
             ads=ads, shop=shop, sig=sig, what=what, aviso=list(aviso), mobileNote=mnote)
    if ig in WEB:
        x['web'] = WEB[ig]
    if not mob and not waFijo:
        x['priority'] = 50
    out.append(x)
assert len(out) == 50 and len({x['ig'] for x in out}) == 50
out.sort(key=lambda x: -x['score'])
load = {d: 0 for d in DAYS}
for x in out:
    z = key(x['zone'])
    ok = [d for d in DAYS if z == 'por confirmar' or z not in TAKEN[d]]
    if not ok:   # el quinto pueblo repetido (Jerez) pasa al lunes 30
        ok = ['2026-11-30']; load.setdefault('2026-11-30', 0); TAKEN.setdefault('2026-11-30', set())
    d = min(ok, key=lambda d: (load[d], DAYS.index(d) if d in DAYS else 9))
    x['day'] = d; load[d] += 1
    if z != 'por confirmar':
        TAKEN[d].add(z)
json.dump(out, open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
cnt = {}
for x in out:
    cnt[x['tier']] = cnt.get(x['tier'], 0) + 1
print(len(out), cnt, load, {n: sum(1 for x in out if x['niche'] == n) for n in NB})
