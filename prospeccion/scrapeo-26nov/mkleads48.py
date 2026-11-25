# Scrapeo del 25-26/11/2026 (noche) para el lote del 26/11: 70 tiendas «más grandes» (Chris: «negocios que ya tengan
# varios negocios físicos abiertos, pero sobre todo que no tengan tienda online»).
# uso: python3 mkleads48.py <prof.json del motor> leads.json ../l33/sel48.json
# Tier A = varias tiendas físicas y sin tienda online; B = una tienda grande (muchos seguidores) sin tienda online;
# C = relleno: una tienda que vende a distancia sin tienda online.
import json, sys
prof = {p['u']: p for p in json.load(open(sys.argv[1]))}
# slug, ig, nombre, nicho, zona, provincia, dirección, centros, tier, «qué es», tienda online, móvil (si no sale del perfil), aviso
L = [
 ('nuria-roig', 'nuriaroig.bcn', 'Nuria Roig', 'moda', 'Barcelona', 'Barcelona', 'Diagonal 537 · Capità Arenas 29 · Major de Sarrià 7', 3, 'A', 'Tres tiendas multimarca de mujer en Barcelona (y Capi 27 Uomo)', 'web sin tienda (nuriaroig.com, WordPress sin carrito)', None, ''),
 ('maribel-fernandez', 'maribelfernandez_boutique', 'Boutique Maribel Fernández', 'moda', 'Murcia', 'Murcia', 'Calle Sociedad 4, Murcia · C/ Natalio Rivas 38, Adra', 2, 'A', 'Dos boutiques de mujer, en Murcia y Adra', 'web vacía (maribelfernandez.com no carga nada)', None, ''),
 ('doble-g-barcelona', 'doblegbarcelona', 'Doble G Barcelona', 'moda', 'Barcelona', 'Barcelona', 'Mallorca 446 · Plaça de Sants 4-5 · Aragó 99', 3, 'A', 'Tres tiendas multimarca de mujer en Barcelona desde 1978', 'web caída (doblegbarcelona.com da 404)', None, ''),
 ('tribeca-store', 'tribecastoree', 'Tribeca Store', 'moda', 'Cabezón de la Sal', 'Cantabria', 'Av. Solares 6, Sarón · Av. Cantabria 14, Cabezón de la Sal · C/ Peñas Arriba 2, Los Corrales', 3, 'A', 'Tres tiendas de ropa, calzado y complementos en Cantabria', 'no tiene', None, ''),
 ('rosi-botiga', 'rosi_botiga', 'Rosi Botiga', 'moda', 'Girona', 'Girona', 'C/ Nou 10, Girona · C/ Santa Anna 3, l\'Estartit', 2, 'A', 'Dos tiendas de ropa, zapatos y complementos (Girona y l\'Estartit)', 'no tiene', None, ''),
 ('le-coquett', 'lecoquett_oficial', 'Le Coquett', 'moda', 'Barcelona', 'Barcelona', '', 2, 'A', 'Marca de moda con tiendas físicas en Cataluña y Galicia', 'no tiene', None, 'Comprobar qué tiendas tiene: la bio solo dice «Tiendas físicas en Catalunya y Galicia»'),
 ('moda-tammara', 'moda_tammara', 'Moda Tammara', 'moda', 'Peligros', 'Granada', 'C/ San Ildefonso 1, Peligros · C/ San Felipe 1, Atarfe', 2, 'A', 'Dos tiendas de moda de mujer en Peligros y Atarfe (Granada)', 'no tiene', None, ''),
 ('maria-tacones', 'mariataconesshop', 'María Tacones Shop', 'moda', 'Morón de la Frontera', 'Sevilla', 'C/ Almería 30 · Pza. de las Flores, local 1 (flamenca)', 2, 'A', 'Dos tiendas en Morón: moda y complementos, y moda flamenca', 'no tiene', None, ''),
 ('ke-pasada-moda', 'ke_pasada_moda', 'Ke Pasada Moda', 'moda', 'Palma', 'Baleares', 'C/ Cardenal Rosell 33 (Coll d\'en Rabassa) · C/ Joan Crespí 21 (Palma)', 2, 'A', 'Dos tiendas de moda de mujer en Palma, con directos', 'no tiene', None, ''),
 ('aura-olot', 'aura_modaicomplements', 'Aura Moda i Complements', 'moda', 'Olot', 'Girona', 'C/ Sant Rafel 6, Olot', 2, 'A', 'Tiendas de mujer, hogar y complementos en Olot', 'no tiene', None, ''),
 ('laazo-80', 'laazo80_boutique', 'Laazo 80', 'moda', 'Murcia', 'Murcia', '', 2, 'A', 'Boutique grande de mujer y hombre en Murcia (con @laazo80_)', 'no tiene', None, ''),
 ('wilco', 'thisiswilco', 'Wilco', 'moda', 'Vitoria-Gasteiz', 'Álava', 'General Álava 1, Vitoria · Azara 9, Zarautz', 2, 'A', 'Concept store de moda con tiendas en Vitoria y Zarautz', 'web sin tienda (thisiswilco.com, WordPress sin carrito)', None, 'Solo publican fijos (945 13 13 67 y 943 13 25 59)'),
 ('nud-madrid', 'nud_madrid', 'Nud Madrid', 'moda', 'Madrid', 'Madrid', 'Claudio Coello 38 · Barquillo 42 · Del Prado 7 · outlet Plaza del Ángel 4', 4, 'A', 'Multimarca con tres tiendas y un outlet en Madrid', 'web cerrada («Sitio privado», nudmadrid.com)', None, 'Solo publican fijos (91 531 33 80 y 91 299 57 37)'),
 ('tretze-girona', 'tretze_girona_', 'Tretze Girona', 'moda', 'Girona', 'Girona', 'Santa Clara 24 · Argenteria 31', 2, 'A', 'Dos tiendas multimarca en Girona desde 1995; venden por Instagram', 'no tiene', None, 'Solo publican fijos (972 29 67 44 y 972 20 81 28)'),
 ('moda-martina-alvarez', 'moda_martinaalvarez', 'Moda Martina Álvarez', 'moda', 'A Coruña', 'A Coruña', 'C/ Teresa Herrera 6 · C/ Barcelona 29', 2, 'A', 'Dos tiendas de moda y complementos en A Coruña desde 1996', 'no tiene', None, 'Solo publican fijos (981 45 69 75 y 981 26 25 81)'),
 ('alemany', 'alemanymataroblanes', 'Alemany', 'moda', 'Mataró', 'Barcelona', 'C. Barcelona 6, Mataró · P. de Dintre 28, Blanes', 2, 'A', 'Dos tiendas de bolsos, maletas y complementos (Mataró y Blanes)', 'no tiene', None, 'Solo publican fijos (937 90 33 37 y 972 33 11 07); dicen que tienen WhatsApp'),
 ('sucursal-moda', 'sucursal.moda', 'Sucursal Moda', 'moda', 'Villarrobledo', 'Albacete', '', 2, 'A', 'Moda de mujer con tiendas en Villarrobledo y Hellín', 'no tiene', None, 'Solo publican fijo (967 96 68 70)'),
 ('uomo-palma', 'tiendas_uomo', 'Uomo', 'moda', 'Palma', 'Baleares', 'Josep Tous i Ferrer 12 · Sant Felip Neri 10 (novios) · Josep Tous i Ferrer 4 (casual)', 3, 'A', 'Tres tiendas de moda de hombre en Palma desde 1974', 'no tiene', None, 'Solo publican fijo (971 71 56 83)'),
 ('space-baricentro', 'moda.space', 'Space', 'moda', 'Barberà del Vallès', 'Barcelona', 'CC Baricentro, puerta 5, local 157', 1, 'B', 'Tienda de moda de mujer en el CC Baricentro; pedidos por WhatsApp', 'no tiene', None, ''),
 ('seville-chic', 'sevilleandchic', 'Seville&Chic', 'moda', 'El Cuervo de Sevilla', 'Sevilla', 'Avenida de Jerez 59', 1, 'B', 'Multimarca de mujer con 74.000 seguidores', 'no tiene', None, ''),
 ('ulldelavila', 'soniaulldelavila', 'Ulldelavila', 'moda', 'Montblanc', 'Tarragona', 'C/ Major 53', 1, 'B', 'Tienda de ropa de mujer y tallas grandes con 65.000 seguidores', 'no tiene', None, ''),
 ('de-flores-y-floreros', 'defloresyflorerosvalencia', 'De Flores y Floreros', 'calzado', 'Valencia', 'Valencia', 'C/ Mestre Gozalbo 1', 1, 'B', 'Calzado de diseño, artesano, con 44.000 seguidores; pedidos por WhatsApp', 'no tiene', None, ''),
 ('charlotte-odil', 'charlotte_odil', 'Charlotte Odil', 'moda', 'Majadahonda', 'Madrid', 'C/ San Isidro 20', 1, 'B', 'Boutique de mujer y asesoría de imagen (48.000 seguidores)', 'no tiene', None, ''),
 ('islu-creaciones', 'islucreaciones', 'Islu Creaciones', 'moda', 'Garrucha', 'Almería', 'C/ Mayor, local 3B', 1, 'B', 'Moda flamenca y de ceremonia propia (34.000 seguidores)', 'no tiene', None, ''),
 ('laura-santiago', 'modaslaurasantiago', 'Modas Laura Santiago', 'moda', 'Andalucía', 'Andalucía', '', 1, 'B', 'Tienda de moda de mujer con 30.000 seguidores; pedidos por MD y WhatsApp', 'no tiene', None, 'No pone ciudad ni dirección en Instagram: comprobar'),
 ('de-lunares-y-volantes', 'dlunaresyvolantes', 'De Lunares y Volantes', 'moda', 'Sevilla', 'Sevilla', '', 1, 'B', 'Moda flamenca propia (32.000 seguidores)', 'no tiene', None, 'No pone dirección en Instagram: comprobar'),
 ('caruncho-kodina', 'carunchoykodina', 'Caruncho Kodina', 'joya', 'Pontevedra', 'Pontevedra', 'C/ Michelena', 1, 'B', 'Joyería artesana desde 1992 (29.000 seguidores)', 'no tiene', None, ''),
 ('eme-flamenca', 'eme.flamenca', 'Eme Eme Flamenca', 'moda', 'Madrid', 'Madrid', '', 1, 'B', 'Moda y asesoría flamenca en Madrid, con cita previa', 'no tiene', None, ''),
 ('teresa-b', 'tteresa.b', 'Teresa·b', 'moda', 'Badajoz', 'Badajoz', 'C/ Vasco Núñez 1A', 1, 'B', 'Tienda de complementos, bolsos y joyas en Badajoz', 'no tiene', None, ''),
 ('mediavilla-calzados', 'tmediavillacalzados', 'Calzados Mediavilla', 'calzado', 'Sevilla', 'Sevilla', 'Pagés del Corro 47, Triana', 1, 'B', 'Zapatos, complementos y mantones en Triana desde 1980', 'no tiene', None, ''),
 ('mandarina-palencia', 'mandarina.palencia', 'Mandarina', 'moda', 'Palencia', 'Palencia', 'Calle Don Sancho 2', 1, 'B', 'Tienda de moda de mujer en Palencia', 'no tiene', None, ''),
 ('selene-moda', 'selene.moda', 'Selene Moda', 'moda', 'Gernika', 'Bizkaia', 'Andra Mari 1', 1, 'B', 'Moda y bolsos de mujer; 25 años en Gernika', 'no tiene', None, ''),
 ('naif-cuir', 'naifcuir', 'Naif Cuir', 'moda', 'Alto Tajo', 'Guadalajara', '', 1, 'B', 'Marca artesana de bolsos de piel hechos a mano', 'no tiene', None, 'Taller propio; comprobar si tiene tienda abierta al público'),
 ('victoria-shop', 'victoria_shopmoda', 'Victoria Shop', 'moda', 'Cantillana', 'Sevilla', 'Avda. Nuestra Señora de la Soledad 87', 1, 'B', 'Tienda de moda de mujer; envíos 24-72 h', 'no tiene', None, ''),
 ('moda-sabana', 'msabanamoda', 'Moda Sabana', 'moda', 'Sant Andreu de la Barca', 'Barcelona', 'Carrer de Catalunya 23', 1, 'B', 'Moda de fiesta y día a día hasta la talla 50', 'no tiene', None, ''),
 ('la-piconela', 'la_piconela_moda_flamenca', 'La Piconela', 'moda', 'Andalucía', 'Andalucía', '', 1, 'B', 'Moda flamenca; anuncian que abren tienda («próxima apertura»)', 'no tiene', None, 'No pone ciudad: comprobar'),
 ('fran-gamez', 'fran_gamez_', 'Fran Gámez', 'moda', 'Écija', 'Sevilla', 'Avda. Doctor Fleming 41', 1, 'B', 'Diseñador de moda flamenca', 'no tiene', None, ''),
 ('baul-de-mariquilla', 'bauldmariquilla', 'El Baúl de Mariquilla', 'joya', 'Sevilla', 'Sevilla', '', 1, 'B', 'Antigüedades: mantones, peinas y bisutería vintage', 'no tiene', None, 'No pone dirección: comprobar'),
 ('presintown', 'presintown_lorca', 'Presintown', 'moda', 'Lorca', 'Murcia', 'Calle Corredera 27', 1, 'B', 'Moda de hombre en Lorca desde hace 30 años', 'no tiene', None, ''),
 ('deluxe-fashion', 'deluxe.fashionstore', 'Deluxe Fashion Store', 'moda', 'Fuente Álamo', 'Murcia', 'C/ Manuel de Falla 11', 1, 'B', 'Moda, calzado y regalos; envíos 24 h', 'no tiene', None, ''),
 ('kokomoda', 'kokomoda3', 'Kokomoda', 'moda', 'Jerez de la Frontera', 'Cádiz', 'Avda. Nazaret, local 1', 1, 'B', 'Moda elegante de mujer; pedidos por WhatsApp', 'no tiene', None, ''),
 ('mar-de-caprichos', 'mardecapriichos', 'Mar de Caprichos', 'moda', 'La Unión', 'Murcia', 'Calle Mayor 85', 1, 'B', 'Moda de evento y casual; reservas por WhatsApp', 'no tiene', None, ''),
 ('maria-palmero', 'mariapalmerozgz', 'María Palmero', 'moda', 'Zaragoza', 'Zaragoza', 'Calle Hernán Cortés 7', 1, 'B', 'Moda y complementos de mujer en Zaragoza', 'no tiene', None, ''),
 ('ole-yo-santona', 'oleyosantona', 'Olé Yo', 'moda', 'Santoña', 'Cantabria', 'Calle Santander 2', 1, 'C', 'Moda y complementos; envíos a toda España', 'no tiene', None, ''),
 # sin propuesta todavía (si Flow no llega): entran en el CRM con su día
 ('bonhomia-concept', 'bonhomiaconcept', 'Bonhomia Concept', 'moda', 'Meliana', 'Valencia', 'C/ Ausias March 18', 1, 'B', 'Tienda de mujer con 71.000 seguidores; venta por MD y WhatsApp', 'no tiene', None, ''),
 ('la-nena', 'lanenashop', 'La Nena', 'joya', 'Villaviciosa', 'Asturias', 'Calle Sol 18', 1, 'B', 'Bisutería artesanal desde 2014 (36.000 seguidores)', 'no tiene', None, ''),
 ('lino-1959', 'lino1959sevilla', 'Lino 1959', 'moda', 'Sevilla', 'Sevilla', 'Avda. Eduardo Dato 22', 1, 'B', 'Tienda de moda de hombre y mujer en Sevilla', 'no tiene', None, ''),
 ('maria-catalina', 'mariacatalina_store', 'María Catalina', 'moda', 'Vigo', 'Pontevedra', 'Calle Regueiro 10', 1, 'C', 'Tienda de moda en Vigo; pedidos por WhatsApp', 'no tiene', None, ''),
 ('dhwoman', 'dhwoman', 'DHWoman', 'moda', 'Cocentaina', 'Alicante', '', 1, 'C', 'Moda de mujer (Cocentaina, Muro, Alcoy)', 'no tiene', None, 'No pone dirección: comprobar'),
 ('benoit-madrid', 'benoitmadrid_', 'Benoît Madrid', 'moda', 'Madrid', 'Madrid', 'Plaza Marqués de Camarines 1, Aravaca', 1, 'C', 'Moda española en ediciones limitadas (Aravaca)', 'no tiene', None, ''),
 ('icono-burgos', 'icono_burgos', 'Icono', 'moda', 'Burgos', 'Burgos', 'Calle San Lesmes 10', 1, 'C', 'Espacio de moda de mujer en Burgos', 'no tiene', None, ''),
 ('antonio-rivas', 'antoniorivas_boutique', 'Antonio Rivas', 'moda', 'Madrid', 'Madrid', '', 1, 'C', 'Atelier de madrinas, invitadas y novias desde 1979', 'no tiene', None, ''),
 ('dizeno-cordoba', 'dizenocordoba', 'Dizeño', 'moda', 'Córdoba', 'Córdoba', '', 1, 'C', 'Moda y bienestar en Córdoba', 'no tiene', None, 'No pone dirección: comprobar'),
 ('modas-ohara', 'modas_ohara', "Modas O'hara", 'moda', 'Crevillent', 'Alicante', 'Av. Madrid 31', 1, 'C', 'Moda de mujer; envíos a toda España e islas', 'no tiene', None, ''),
 ('bsmoda', 'bsmoda_sharo', 'BS Moda', 'moda', 'El Puerto de Santa María', 'Cádiz', 'Calle Ganado 30', 1, 'C', 'Moda de mujer con grupo de difusión de WhatsApp', 'no tiene', None, ''),
 ('anais-moda', 'anaismodajoven', 'Anais', 'moda', 'Valladolid', 'Valladolid', 'Plaza de San Juan 14', 1, 'C', 'Boutique de moda y complementos; venta online a toda España por MD', 'no tiene', None, ''),
 ('zapateria-paula', 'zapateria_moda_paula', 'Zapatería y Moda Paula', 'calzado', 'La Cañada', 'Almería', 'Plaza Antonio de Torres 12', 1, 'C', 'Zapatería y moda; pedidos por WhatsApp', 'no tiene', None, ''),
 ('pitusa-gasul', 'pitusagasul.modaflamenca', 'Pitusa Gasul', 'moda', 'Andalucía', 'Andalucía', '', 1, 'C', 'Mantoncillos, camisas y chales flamencos de diseño propio', 'no tiene', None, 'No pone ciudad: comprobar'),
 ('more-amore', 'moreamorestoree', 'More Amore Store', 'moda', 'El Pajar', 'Las Palmas', 'C/ Carmen Jorge Artiles 4', 1, 'C', 'Moda y complementos (madre e hija)', 'no tiene', None, 'Está en Canarias (envíos)'),
 ('rosario-modas', 'rosariomodasalhaurin', 'Rosario Modas', 'moda', 'Alhaurín el Grande', 'Málaga', 'Avda. Gerard Brenan 19', 1, 'C', 'Moda y complementos en Alhaurín el Grande', 'no tiene', None, ''),
 ('cal-manso', 'cal_manso', 'Cal Manso', 'moda', 'Manlleu', 'Barcelona', 'C/ Passió 13', 1, 'C', 'Roba de dona: botiga i mercat', 'no tiene', None, ''),
 ('complementos-motril', 'complementos_motril', 'Complementos Motril', 'moda', 'Motril', 'Granada', '', 1, 'C', 'Complementos; envíos 24-48 h', 'no tiene', None, 'No pone dirección: comprobar'),
 ('lenana-novias', 'lenana_novias', 'Lenana', 'moda', 'Huelva', 'Huelva', 'Calle Bocas 13', 1, 'C', 'Novias, madrinas y fiesta en Huelva', 'no tiene', None, ''),
 ('matilda-estepona', 'matildaestepona', 'Matilda', 'moda', 'Estepona', 'Málaga', 'C/ Santa Ana 22', 1, 'C', 'Moda y artesanía; envíos a toda España', 'no tiene', None, ''),
 ('jaleo-mieres', 'jaleomieres', 'Jaleo', 'moda', 'Mieres', 'Asturias', 'C/ Jerónimo Ibrán 6', 1, 'C', 'Tienda de moda y complementos en Mieres', 'no tiene', None, ''),
 ('k-me-pongo', 'k_me_pongo', 'K Me Pongo', 'moda', 'Casas-Ibáñez', 'Albacete', 'Calle Tercia 26', 1, 'C', 'Ropa y complementos de hombre y mujer', 'no tiene', None, ''),
 ('sao-jewels', 'saobymedialdea', 'Saó Jewels', 'joya', 'Sant Feliu de Guíxols', 'Girona', 'Carrer Major 43', 1, 'C', 'Joyas y complementos para regalar', 'no tiene', None, ''),
 ('maison-shop', 'maison.shop.0', 'Maison Shop', 'moda', 'España', 'España', '', 1, 'C', 'Venta de ropa; envíos a toda España', 'no tiene', None, 'No pone ciudad ni dirección: comprobar que tenga tienda física'),
 ('edurne-oinetakoak', 'e.oinetakoak', 'Edurne Oinetakoak', 'calzado', 'Euskadi', 'Euskadi', '', 1, 'C', 'Tienda de zapatos y complementos', 'no tiene', None, 'Solo publica fijo (945 03 59 81); no pone dirección'),
 ('boutique-martina', 'la.boutiquedemartina', 'La Boutique de Martina', 'moda', 'España', 'España', '', 1, 'C', 'Novedades semanales de moda; envíos a Europa', 'no tiene', None, 'No pone ciudad ni dirección: comprobar que tenga tienda física'),
]
fmt = lambda n: f"{n:,}".replace(',', '.')
out = []
for k, (slug, ig, name, ni, zone, reg, addr, cen, tier, what, shop, mob, aviso) in enumerate(L):
    p = prof[ig]
    ph = mob or (p['ph'][0] if p['ph'] else '')
    fx = p['fx'][0] if p['fx'] else ''
    sc = {'A': 80, 'B': 65, 'C': 50}[tier] + min(10, cen * 3) + (5 if p['f'] >= 20000 else 0) + (3 if ph else -10) + (2 if p['wa'] else 0)
    out.append(dict(slug=slug, ig=ig, name=name, niche=ni, zone=zone, region=reg, address=addr, centers=cen, tier=tier, what=what,
                    shop=shop, f=p['f'], wa=ph, fijo=fx, waBio=bool(p['wa']), score=min(99, sc), aviso=aviso, last=p['last'],
                    sig=p['sig'], eng=p['eng'], date='26/11/2026', day='2026-11-26'))
json.dump(out, open(sys.argv[2], 'w'), ensure_ascii=False, indent=1)
from specs import S
sel = [x for x in out if x['slug'] in S]
json.dump(sel, open(sys.argv[3], 'w'), ensure_ascii=False, indent=1)
print(len(out), 'leads;', len(sel), 'con specs;', sum(1 for x in out if not x['wa']), 'sin móvil')
