# Lote 38 (16/11/2026): tiendas con anuncios en Meta, sin tienda online de verdad y con WhatsApp comprobado (scrapeo-16nov/crm30.json + los nuevos).
# Sin muebles (Chris: «no veo bien muebles»). Matia (Bilbao) fuera: cerró el 30/07/2026.
# Referencias NN = scratchpad l38/src/<slug>/NN.jpg (sus últimas 33 publicaciones, con hasta 3 fotos de cada carrusel).
# Se carga desde specs.py (exec) y usa su S. CROPS38: referencia recortada 'NNc' = (original, (x0, y0, x1, y1) en fracciones). Nunca referencias con menores.
CROPS38 = {}
MEN_REV = [('Javier', 'Sevilla', 0, 'Lo pedí un domingo por la noche y llegó tal cual se ve en las fotos.'),
           ('Álvaro', 'Madrid', 1, 'Por fin puedo comprar sin escribir por privado. La talla, perfecta.'),
           ('Marcos', 'Valencia', 2, 'Me ayudaron con la talla por WhatsApp en un momento.'),
           ('Pablo', '*', 3, 'Lo recogí en la tienda y aproveché para probarme dos cosas más.'),
           ('Daniel', 'Málaga', 4, 'Pagué con Bizum en un minuto. Repetiré seguro.'),
           ('Sergio', 'Bilbao', 5, 'La calidad se nota. Ya tengo fichado lo siguiente.')]

# ---------------- joyería
S['luxoro'] = dict(
    who='none', h1='Oro y joyas,<br>a un clic.',
    hero=('19', 'gold chain bracelets and gold rings'),
    banner=('17', 'a modern jewellery and gold stand in a bright shopping centre with glass display cases full of gold bars and gold jewellery, warm light, no people'),
    prods=[('22', 'a small gold investment bar with a plain stamped surface, no logos and no text', 'Lingote de oro'),
           ('19', 'the gold curb chain bracelet with an ID plate (the one on the left)', 'Pulsera de oro'),
           ('20', 'a pair of polished gold wedding rings', 'Alianzas de oro'),
           ('21', 'a pair of gold teardrop drop earrings with an open hoop design', 'Pendientes de oro'),
           ('28', 'a stack of small gold bars of different sizes with plain surfaces, no logos and no text', 'Lingotes pequeños'),
           ('35', 'a stack of gold rings of different styles', 'Anillos de oro')],
    l1=('04', 'gold rings and a gold chain on a café table next to a cappuccino'),
    l2=('17', 'a glass display case with gold bars and gold jewellery in a jewellery shop'),
    opts_l='Peso', opts=['1 g', '5 g', '10 g', '1 onza'],
    cats=[('Lingotes', 'p1'), ('Joyas de oro', 'p2'), ('Alianzas', 'p3')])

S['gm-joyerias'] = dict(
    who='none', h1='Joyas de oro<br>a precio de oro.',
    hero=('18', 'chunky gold chains, gold link bracelets and gold rings'),
    banner=('29', 'the inside of a bright jewellery shop with illuminated amber display cabinets full of gold jewellery, no people'),
    prods=[('01', 'the open gold bangle bracelet with a twisted texture (the large one at the bottom)', 'Brazalete de oro'),
           ('17', 'a pair of large twisted gold hoop earrings', 'Aros torzados'),
           ('18', 'a single chunky gold curb link chain necklace', 'Cadena de oro'),
           ('16', 'a cocktail ring with a large oval blue stone surrounded by small diamonds, in an open white jewellery box', 'Sortija con piedra azul'),
           ('28', 'a fine gold chain necklace with a small gold letter initial pendant', 'Colgante con inicial'),
           ('42', 'a bracelet of white pearls with small gold beads', 'Pulsera de perlas')],
    l1=('44', 'gold bangles and bracelets displayed on a cream velvet bracelet stand in a jewellery shop'),
    l2=('19', 'several gold chains of different link styles laid diagonally on beige linen'),
    cats=[('Pulseras', 'p1'), ('Pendientes', 'p2'), ('Colgantes', 'p5')])

# ---------------- moda
S['mantones-africa'] = dict(
    place='the Real de la Feria de Abril in Seville, Spain, with striped casetas and paper lanterns', who='woman',
    h1='Mantones bordados,<br>de fábrica a tu casa.',
    hero=('54', 'a royal blue silk manila shawl richly embroidered with red and pink flowers and a long blue fringe, worn over a white flamenco dress with navy polka dots'),
    banner=(None, 'the inside of an artisan shawl shop in Andalusia with rows of colourful embroidered silk manila shawls hanging on rails and folded on wooden tables, no people'),
    prods=[('12', 'a sage green silk manila scarf embroidered with pink and coral flowers and a long magenta fringe, folded into a triangle', 'Mantón verde agua'),
           ('26', 'a cream silk manila scarf embroidered with multicoloured flowers and a long mauve fringe, folded into a triangle', 'Mantón marfil bordado'),
           ('42', 'a navy blue silk manila scarf embroidered with red roses, blue birds and colourful flowers', 'Mantón azul noche'),
           ('43', 'a white silk manila scarf embroidered in black with large flowers', 'Mantón blanco y negro'),
           ('31', 'an orange silk manila scarf embroidered with tone-on-tone flowers and a long orange fringe', 'Mantón naranja'),
           ('48', 'a small purple embroidered shawl with flowers and a long purple fringe, worn over the shoulders of a yellow polka dot flamenco dress', 'Mantoncillo morado')],
    l1=('23', 'a cream manila shawl embroidered with red and pink roses and a long cream fringe, worn over a red and white flamenco dress'),
    l2=('40', 'a pile of folded small silk scarves in pink, red, mustard, navy and cream'),
    opts_l='Tamaño', opts=['Mantoncillo', 'Mediano', 'Grande'],
    na=dict(chip='Mantones nuevos · de nuestra fábrica', sub='Bordados en nuestro taller de {city}. Ahora, con envío a toda España.', new_h='Los mantones nuevos',
            look_e='Para la feria', look_h='El mantón de cada traje', look_b='Añadir los 3'),
    cats=[('Mantones', 'p1'), ('Mantoncillos', 'p6'), ('Novedades', 'p3')])

S['mirage-pamplona'] = dict(
    place='the Plaza del Castillo in Pamplona, Spain, with its arcades and cafés', who='woman',
    hero=('13', 'a cream long knit cardigan coat over a light blue jumper and cream wide-leg trousers'),
    banner=(None, 'the shop front and inside of a women\'s fashion boutique in Pamplona with rails of navy, beige and camel knitwear and flower pots at the door, no people'),
    prods=[('05c', 'a navy blue light fleece sweatshirt with gold buttons along the side', 'Sudadera con botones'),
           ('31', 'a long cream double-breasted wool maxi coat with a belt over a striped jumper and a brown mini skirt with tall brown boots', 'Abrigo maxi de paño'),
           ('12', 'a chocolate brown suede biker jacket over a light blue openwork jumper and straight jeans', 'Cazadora de gamuza'),
           ('22', 'a pink and chocolate striped jumper with a brown faux-suede wrap mini skirt and tall brown boots', 'Jersey de rayas'),
           ('18', 'a camel long coat over a lilac argyle jumper and plum wide palazzo trousers', 'Pantalón palazzo'),
           ('15', 'a navy pea coat over a pink jumper and dark wide-leg jeans', 'Chaquetón marino')],
    l1=('23', 'a pale blue long coat over a grey knit jumper and brown shorts with tall brown boots'),
    l2=('33', 'a navy maxi wool coat with a beige argyle jumper and navy wide-leg trousers'),
    cats=[('Jerséis', 'p4'), ('Abrigos', 'p2'), ('Pantalones', 'p5')])
CROPS38['mirage-pamplona'] = {'05c': ('05', (.38, .14, .66, .44))}

S['tete-plata'] = dict(
    place='the Plaza Alta in Badajoz, Spain, with its colourful arcaded houses', who='woman',
    hero=('08', 'a khaki green utility parka jacket with houndstooth check cuffs'),
    banner=('18', 'the inside of a warm fashion boutique with a wooden floor, golden-lit rails of autumn clothes and a central wooden table with folded jumpers, no people'),
    prods=[('01', 'a grey paisley-print knit cardigan jacket', 'Chaqueta de paisley'),
           ('20', 'a navy and cream striped V-neck jumper with blue jeans', 'Jersey de rayas'),
           ('21', 'a black jumper with small gold buttons on the front and blue jeans', 'Jersey con botones'),
           ('15', 'a black double-breasted wool waistcoat over a grey top and jeans', 'Chaleco cruzado'),
           ('31', 'a leopard-print padded jacket', 'Cazadora de leopardo'),
           ('17', 'an argyle jumper in brown, cream and navy with blue jeans', 'Jersey de rombos')],
    l1=('06', 'a light blue and white striped ruffled blouse with navy trousers'),
    l2=('24', 'a rust orange jumper with beige trousers and a leopard print handbag'),
    cats=[('Jerséis', 'p2'), ('Chaquetas', 'p1'), ('Chalecos', 'p4')])

S['la-canada-showroom'] = dict(
    place='the Calleja de las Flores in Córdoba, Spain, with whitewashed walls and blue flower pots', who='woman',
    hero=('18', 'a long orange and brown floral print dress with a sheer orange shawl'),
    banner=(None, 'the inside of a multibrand fashion boutique with rails of colourful autumn clothes, a red upholstered bench and big shop windows onto the street, no people'),
    prods=[('13', 'a red fine-knit cardigan with a navy, red and white tartan midi skirt', 'Falda de cuadros'),
           ('17', 'a purple and pink check midi dress with long puffed sleeves and an asymmetric hem', 'Vestido de cuadros'),
           ('20', 'a khaki green fitted jacket with buttons and a matching long flared skirt', 'Conjunto caqui'),
           ('28', 'a red satin off-the-shoulder top with a matching long flared skirt', 'Conjunto rojo de fiesta'),
           ('32', 'an olive green asymmetric ruffled midi dress', 'Vestido verde oliva'),
           ('27', 'a printed jacket and wide trousers set with an ethnic geometric pattern in brown, red and gold', 'Traje estampado')],
    l1=('19', 'a red and black floral print long dress'),
    l2=('15', 'a black leather jacket over a red and navy zigzag knit midi dress'),
    cats=[('Vestidos', 'p2'), ('Faldas', 'p1'), ('Fiesta', 'p4')])

S['deja-vu-villafranca'] = dict(
    place='a sunny square in Villafranca de los Barros, Badajoz, Spain, with whitewashed houses and orange trees', who='woman',
    hero=('04c', 'a chocolate brown lightweight quilted puffer jacket'),
    banner=(None, 'the inside of a small family fashion shop in a Spanish town with rails of women\'s clothes, shelves of folded jumpers and a wooden floor, no people'),
    prods=[('02c', 'a navy blue quilted padded gilet with a high collar over a white top', 'Chaleco acolchado'),
           ('04c', 'a chocolate brown lightweight quilted puffer jacket', 'Plumífero ligero'),
           ('22', 'a cream shirt with a brown and burgundy check midi skirt', 'Falda de cuadros'),
           ('30', 'a beige and brown striped shirt', 'Camisa de rayas'),
           ('29', 'a brown check short-sleeved jacket', 'Chaqueta de cuadros'),
           ('13', 'a burgundy fringed wool poncho over a black top and jeans', 'Poncho con flecos')],
    l1=('20', 'a brown and cream geometric print blouse with dark flared jeans'),
    l2=('32', 'a dark plum satin blouse with a brown printed tiered maxi skirt'),
    cats=[('Abrigos', 'p2'), ('Faldas', 'p3'), ('Camisas', 'p4')])
CROPS38['deja-vu-villafranca'] = {'02c': ('02', (.0, .32, .52, 1.)), '04c': ('04', (.0, .14, .56, .52))}

S['amelie-bilbao'] = dict(
    place='the Gran Vía of Bilbao, Spain, with its elegant buildings and autumn trees', who='woman',
    hero=('06', 'a long camel faux-fur teddy coat'),
    banner=('01', 'the inside of a designer fashion boutique with a colourful patterned wallpaper wall, track lights, rails of dark designer clothes and a light wooden floor, no people'),
    prods=[('04', 'a red faux-fur coat with a wide collar', 'Abrigo de pelo rojo'),
           ('10', 'a long sage grey quilted padded coat with a tie belt', 'Abrigo acolchado'),
           ('08', 'an oversized brown and black striped jumper with black wide trousers', 'Jersey de rayas'),
           ('12', 'a pair of white leather low-top sneakers with a camouflage and pink suede upper and a gold heel tab', 'Zapatillas de camuflaje'),
           ('28', 'a khaki belted utility jacket with matching wide trousers', 'Conjunto caqui'),
           ('20', 'an olive quilted cape jacket with a hood', 'Capa acolchada')],
    l1=('30', 'a lilac blue ruffled blouse with black wide trousers'),
    l2=('18', 'a black leather blazer over a dark top'),
    cats=[('Abrigos', 'p1'), ('Punto', 'p3'), ('Calzado', 'p4')])

S['pepita-mariquita'] = dict(
    place='a sunny pedestrian shopping street in Getafe, Madrid, Spain', who='woman',
    hero=('15', 'a brown, cream and rust striped blanket poncho over brown trousers'),
    banner=(None, 'the inside of a small women\'s fashion boutique with rails of colourful dresses, dressed mannequins, hats and handbags on high shelves, white walls and a light floor, no people'),
    prods=[('06', 'a burgundy velvet long coat over a cream top with lilac trousers', 'Abrigo de terciopelo'),
           ('23', 'a purple peplum knit jumper with dark jeans', 'Jersey con volante'),
           ('28', 'a teal green printed long-sleeved midi dress with a keyhole neckline', 'Vestido estampado'),
           ('21', 'an olive green overshirt jacket with matching wide trousers', 'Conjunto verde'),
           ('31', 'a blue, orange and cream wavy print midi dress', 'Vestido de invitada'),
           ('19', 'a long brown long-sleeved draped maxi dress', 'Vestido largo')],
    l1=('12', 'an olive utility jacket over a white T-shirt with brown trousers'),
    l2=('26', 'a beige jacket over a white top with a grey check skirt'),
    cats=[('Vestidos', 'p3'), ('Abrigos', 'p1'), ('Invitada', 'p5')])

S['zona-coolto'] = dict(
    place='the Paseo de Pereda in Santander, Spain, by the bay', who='woman',
    hero=('03', 'a dark olive oversized jumper with mustard wide corduroy trousers'),
    banner=('11', 'the inside of a fashion store with whitewashed stone walls, exposed wooden beams, rails of autumn clothes, dressed mannequins and a red oriental rug, no people'),
    prods=[('30', 'a dark brown waxed cotton field jacket with a brown corduroy collar over a striped shirt', 'Chaqueta encerada'),
           ('35', 'a navy quilted velvet waistcoat with a tie belt over a check shirt', 'Chaleco acolchado'),
           ('20', 'an olive green knit jumper with light jeans hand-painted with yellow and red flowers', 'Vaquero pintado'),
           ('06c', 'a long cream wool coat', 'Abrigo de paño crudo'),
           ('23', 'a long brown and green tartan maxi skirt with a belted dark brown jacket', 'Falda larga de cuadros'),
           ('36', 'a navy and white pinstripe oversized shirt with matching wide pleated trousers', 'Conjunto de rayas')],
    l1=('19', 'a long brown printed coat over black wide trousers'),
    l2=('32', 'a mustard knit jumper with a multicoloured printed scarf and burgundy trousers'),
    cats=[('Abrigos', 'p4'), ('Chaquetas', 'p1'), ('Pantalones', 'p3')])
CROPS38['zona-coolto'] = {'06c': ('06', (.0, .1, .55, 1.))}

S['azalea-moda'] = dict(
    place='a tree-lined boulevard in Torrelavega, Cantabria, Spain', who='man',
    hero=('01', 'a camel wool overcoat over a grey hooded jumper and beige chinos'),
    banner=('07', 'the inside of a men\'s clothing store with wooden floors, rails of blazers and shirts and tables of folded jumpers and jeans, no people'),
    prods=[('02', 'a mustard yellow wool blazer with a navy jumper', 'Americana mostaza'),
           ('03c', 'a khaki green hooded puffer jacket over a grey jumper and beige chinos', 'Plumífero caqui'),
           ('14', 'a grey houndstooth blazer over a beige waistcoat, a white shirt and beige trousers', 'Americana de pata de gallo'),
           ('10', 'light grey slim cargo trousers', 'Pantalón cargo'),
           ('17', 'a suede sneaker in beige, green and mustard with perforated details', 'Zapatilla de ante'),
           ('22', 'grey washed slim jeans', 'Vaquero gris')],
    l1=('24', 'a navy zip-up wool jacket over a white T-shirt and grey jeans'),
    l2=('11c', 'a pair of grey suede and mesh running sneakers on a wooden floor'),
    opts=['S', 'M', 'L', 'XL', 'XXL'],
    rev=MEN_REV, na=dict(rev_p='Así se verán las opiniones de vuestros clientes. Estas son de ejemplo.', look_s='Tres prendas de la tienda que van solas. Llévatelas juntas o elige la que te falta.'),
    cats=[('Americanas', 'p1'), ('Abrigos', 'p2'), ('Pantalones', 'p4')])
CROPS38['azalea-moda'] = {'03c': ('03', (.52, .08, 1., .95)), '11c': ('11', (.0, .2, 1., .5))}

S['bellamoda'] = dict(
    place='the main square of Belalcázar, Córdoba, Spain, with the castle tower in the background', who='woman',
    hero=('42', 'an argyle knit jumper in brown, cream and beige with a pleated beige skirt'),
    banner=(None, 'the inside of a bright small-town women\'s fashion shop with rails of jumpers and coats, shelves with slippers and scarves, pink accents and a light floor, no people'),
    prods=[('17', 'a black oversized knit jumper with balloon sleeves and cream faux-fur trims at the collar and cuffs', 'Jersey con pelo'),
           ('20', 'a dark brown faux-leather belted jacket with beige wide trousers', 'Chaqueta de polipiel'),
           ('28', 'a navy knit jumper with cream stripes at the hem and matching wide trousers', 'Conjunto de punto'),
           ('39', 'a burgundy jumper with small embroidered hearts and a champagne satin midi skirt', 'Jersey de corazones'),
           ('12', 'black suede slip-on slipper shoes with an embroidered trim', 'Zapatillas de casa'),
           ('47', 'a blue fleece pyjama set with a teddy bear motif top and snowflake trousers', 'Pijama polar')],
    l1=('59', 'a brown and cream striped jumper with dark trousers and a black handbag'),
    l2=('33', 'a grey and white striped turtleneck jumper with a black faux-leather mini skirt'),
    cats=[('Jerséis', 'p1'), ('Conjuntos', 'p3'), ('Pijamas', 'p6')])

S['mh-mercedes-henares'] = dict(
    place='the Real de la Feria de Abril in Seville, Spain, with striped casetas and paper lanterns', who='woman',
    h1='Moda flamenca<br>y campera.',
    hero=('32', 'an orange polka dot fitted flamenco dress with white ruffles'),
    banner=('13', 'the inside of a flamenco fashion boutique with rails of colourful polka dot flamenco dresses, embroidered shawls, red carnations and lanterns, no people, no text'),
    prods=[('28', 'a red polka dot flamenco dress with three-quarter ruffled sleeves and a tiered ruffled skirt', 'Traje de flamenca rojo'),
           ('33', 'a pink and burgundy polka dot fitted flamenco dress with ruffled sleeves and a mermaid ruffled hem', 'Traje de flamenca rosa'),
           ('29', 'a royal blue polka dot flamenco dress with puff sleeves and tiered ruffles', 'Traje de flamenca azulina'),
           ('11', 'a colour-block wool poncho in black, camel, rust and olive with a cream trim', 'Poncho campero'),
           ('01', 'a long black flamenco rehearsal skirt with a full ruffled hem, worn with a black top', 'Falda de ensayo'),
           ('50', 'a grey and white rociera skirt with a grey ruffled blouse', 'Traje de rociera')],
    l1=('48', 'a cream ruffled flamenco dress with a mustard embroidered shawl'),
    l2=('19', 'red, white and black embroidered flamenco shawls (manila scarves) hanging with long fringes'),
    na=dict(chip='Nueva temporada flamenca', look_e='Para la feria', look_h='Tu traje, completo', look_b='Añadir los 3'),
    cats=[('Flamenca', 'p1'), ('Mantones', 'l2'), ('Campera', 'p4')])

S['libe-boutique'] = dict(
    place='a sunny street of Dénia, Alicante, Spain, with plane trees and café terraces', who='woman',
    hero=('39', 'a long camel wool coat over a burgundy paisley print midi dress with brown boots'),
    banner=('04', 'the inside of an elegant bright boutique with cream armchairs, a white marble floor, a white counter and rails of clothes, no people, no text'),
    prods=[('43', 'a white shirt with navy and orange contrast piping and gold heart buttons', 'Camisa con vivos'),
           ('25', 'a cream silk shirt with a whimsical print of hot-air balloons, planets and birds', 'Camisa estampada'),
           ('17', 'a navy tweed jacket with gold buttons and black faux-fur cuffs', 'Chaqueta de tweed'),
           ('20', 'a beige suede and knit zip jacket over a brown top with beige wide-leg trousers', 'Conjunto camel'),
           ('38', 'a pink and red paisley print long-sleeved midi shirt dress', 'Vestido de paisley'),
           ('44', 'a green leather jacket over a blue and white striped shirt with jeans', 'Cazadora verde')],
    l1=('10', 'a black long coat over a camel jumper with black trousers and a large tan handbag'),
    l2=('45', 'a long blue, brown and white check wool coat'),
    cats=[('Camisas', 'p1'), ('Chaquetas', 'p3'), ('Vestidos', 'p5')])

S['pilm'] = dict(
    place='the main square of La Vall d\'Uixó, Castellón, Spain, with its church and palm trees', who='woman',
    hero=('13', 'a navy blue cropped wool jacket with gold buttons and burgundy trousers'),
    banner=('28', 'the inside of a small elegant women\'s boutique with a rail of black and white garments, white walls and soft light, no people, no text'),
    prods=[('06', 'a black blazer with a long fringe yoke over a sheer black blouse and jeans', 'Blazer con flecos'),
           ('07', 'a brown faux-fur jacket with a black belt and wide brown faux-leather trousers', 'Chaqueta de pelo'),
           ('19', 'a brown jumper with a brown, cream and black check midi skirt', 'Falda de cuadros'),
           ('15c', 'a beige double-breasted short trench jacket with black trousers', 'Trenca corta'),
           ('27c', 'a burgundy knit cardigan with gold buttons and a burgundy and black tartan midi skirt', 'Chaqueta granate'),
           ('31', 'slim camel coated jeans with a burgundy top', 'Vaquero camel')],
    l1=('10', 'a black puffer jacket over a grey top with a black and white houndstooth midi skirt'),
    l2=('09c', 'a fluffy brown faux-fur jacket over a black top with a black faux-leather midi skirt'),
    cats=[('Chaquetas', 'p1'), ('Faldas', 'p3'), ('Pantalones', 'p6')])
CROPS38['pilm'] = {'15c': ('15', (.48, .1, 1., 1.)), '27c': ('27', (.48, .1, 1., 1.)), '09c': ('09', (.45, .1, 1., 1.))}

S['mia-moll'] = dict(
    place='the Calle Trapería in Murcia, Spain, with the cathedral tower in the background', who='woman',
    h1='Diseño propio,<br>hecho en Murcia.',
    hero=('06', 'a white fluffy short-sleeved top with a fuchsia croc-effect leather mini skirt'),
    banner=('11', 'the inside of a colourful pop-style designer boutique with a pink wall, white rails with bright sixties-style dresses and pink balloons, no people, no text'),
    prods=[('05', 'a fuchsia croc-effect leather pencil mini skirt with a white fluffy top', 'Falda fucsia'),
           ('03', 'a metallic silver shoulder bag with a curved handle', 'Bolso plata'),
           ('08c', 'a sleeveless colour-block mini shift dress in pink and green', 'Vestido bicolor'),
           ('10', 'a sleeveless colour-block knit dress with stripes of pink, yellow, green and white', 'Vestido Arcoíris'),
           ('07', 'a grey and blue houndstooth knit jumpsuit with a wide blue collar', 'Mono de punto'),
           ('01c', 'a pink and white check tweed mini skirt with a white cropped fluffy top', 'Falda de tweed rosa')],
    l1=('12', 'a white teddy coat over a rainbow stripe mini dress with white platform boots'),
    l2=('13', 'a grey and white colour-block fitted jumpsuit'),
    cats=[('Vestidos', 'p4'), ('Faldas', 'p1'), ('Bolsos', 'p2')])
CROPS38['mia-moll'] = {'08c': ('08', (.33, .0, .67, 1.)), '01c': ('01', (.5, .0, 1., 1.))}

# ---------------- calzado (zapaterías: nicho «calzado» en la tienda; en el CRM son «sneakers»)
S['kisco-calzados'] = dict(niche='calzado',
    place='the Plaza del Arenal in Jerez de la Frontera, Spain, with palm trees', who='woman',
    hero=('02', 'black leather mid-calf cowboy boots with stitching, with cream trousers'),
    banner=(None, 'the inside of a charming shoe boutique with wooden crates, shoe displays on tables, dried flowers and warm light, no people, no text'),
    prods=[('07', 'black croc-effect leather ankle boots with a slim heel and a pointed toe', 'Botín efecto piel'),
           ('13', 'black and brown Mary Jane ballet flat shoes with a buckle strap', 'Merceditas'),
           ('22', 'brown suede tasselled loafers', 'Mocasín de serraje'),
           ('16', 'brown velvet slingback kitten heel shoes with a bow', 'Destalonado de terciopelo'),
           ('26', 'a burgundy leather T-bar platform high heel sandal shoes', 'Sandalia de tacón'),
           ('33', 'classic pointed leather pump shoes in burgundy', 'Salón clásico')],
    l1=('23', 'a pair of brown suede tassel loafers on a stone café table with a cappuccino and a magazine'),
    l2=('43', 'woven leather lace-up flat shoes in beige and brown on a patterned tile floor by a blue door'),
    cats=[('Botines', 'p1'), ('Planos', 'p2'), ('Tacones', 'p4')])

S['calzados-toni'] = dict(niche='calzado',
    place='the main street of Chauchina, Granada, Spain, with the Sierra Nevada in the background', who='woman',
    hero=('06', 'black leather knee-high boots with a block heel, with a dark midi skirt'),
    banner=('03', 'the inside of a shoe shop with white shelves full of boots and ankle boots, handbags on display and a light wooden floor, no people, no text'),
    prods=[('02', 'the black leather knee-high boot with a block heel and a buckle strap (not the handbag)', 'Bota alta con hebilla'),
           ('29', 'brown suede wedge ankle boots with a side zip and a small stud', 'Botín de cuña'),
           ('17', 'brown quilted padded ankle boots with a chunky sole', 'Botín acolchado'),
           ('20', 'black suede sock ankle boots with a block heel and a crystal chain detail', 'Botín con strass'),
           ('23', 'taupe and beige suede lace-up sneakers with a curved side panel', 'Deportiva de ante'),
           ('26', 'brown leather slip-on loafers with a gold buckle and a light platform sole', 'Mocasín con hebilla')],
    l1=('05', 'brown suede ankle boots lined with faux fur on a wooden floor'),
    l2=('12', 'pink fluffy house slipper shoes with embroidered hearts'),
    cats=[('Botas', 'p1'), ('Botines', 'p2'), ('Deportivas', 'p5')])

S['livorno-calzados'] = dict(niche='calzado',
    place='a street of Mieres, Asturias, Spain, after the rain, with green hills behind', who='woman',
    hero=('04', 'tall dark brown leather riding boots with a buckle strap, with jeans'),
    banner=(None, 'the inside of a bright shoe shop with white shelves full of shoes and boots, a red counter and a light floor, no people, no text'),
    prods=[('06c', 'a tall black leather riding boot with a buckle strap at the ankle', 'Bota alta de piel'),
           ('24', 'taupe suede western-style ankle boots with a stacked heel and small studs', 'Botín camperos'),
           ('25', 'beige faux-leather lace-up ankle boots with a faux-fur collar and a white platform sole', 'Botín con pelo'),
           ('29c', 'a brown leather ankle boot with a chunky block heel', 'Botín de tacón ancho'),
           ('19', 'brown suede lace-up sneakers with cream side stripes', 'Deportiva de ante'),
           ('13c', 'fluffy blue house slipper shoes with a pale blue heart', 'Zapatillas de casa')],
    l1=('30', 'a brown and a tan suede ankle boot among autumn leaves'),
    l2=('37', 'beige suede slingback kitten heel shoes'),
    cats=[('Botas', 'p1'), ('Botines', 'p2'), ('Zapatillas de casa', 'p6')])
CROPS38['livorno-calzados'] = {'06c': ('06', (.0, .1, .55, .85)), '29c': ('29', (.5, .25, 1., .85)), '13c': ('13', (.0, .2, .6, .95))}

# ---------------- los 11 nuevos (16/11/2026, segundo scrapeo: anuncios en Meta + WhatsApp comprobado). Referencias en l38/src2/<slug>/NN.jpg
S['verde-agua-reinosa'] = dict(
    place='a street of Reinosa, Cantabria, Spain, with stone houses and green mountains behind', who='woman',
    hero=('28', 'a red cropped puffer jacket over a red and white striped top with chocolate brown wide-leg trousers and a navy fringed shoulder bag'),
    banner=('09', 'the inside of a warm fashion boutique with an arched mirror, golden spotlights, a light wooden floor and rails full of colourful winter coats and knitwear, no people'),
    prods=[('01', 'a brown suede coat with shaggy faux-fur collar, cuffs and hem over a light blue shirt and jeans', 'Abrigo de ante y pelo'),
           ('38', 'a fawn-print faux-fur jacket with light blue faux-fur collar and cuffs over a white shirt with wide light blue jeans', 'Chaqueta de pelo cervatillo'),
           ('10', 'a cream and burgundy floral jacquard knit jacket with light grey wide trousers', 'Chaqueta jacquard'),
           ('47', 'a brown faux-suede biker jacket with long fringes over a floral print top and floral trousers', 'Chaqueta de flecos'),
           ('43', 'a brown and cream striped chunky knit jumper with sequin-print trousers', 'Jersey de rayas'),
           ('42', 'a khaki camouflage knit jumper with a star patch and dark flared jeans', 'Jersey camuflaje')],
    l1=('44', 'a cream floral teddy jacket over a red and white striped top with burgundy leather trousers'),
    l2=('13', 'a navy wool coat with a long cobalt blue fringed scarf and jeans'),
    cats=[('Abrigos', 'p1'), ('Chaquetas', 'p2'), ('Jerséis', 'p5')])

S['venus-lenceria-jerez'] = dict(
    who='none', still=True, h1='Tu talla de sujetador,<br>ahora también online.',
    hero=('01', 'a deep red lace underwired bra laid on a soft burgundy knit blanket with a few autumn leaves'),
    banner=('06', 'the inside of a lingerie shop with a wall of white shelves full of bra boxes, a long counter and a soft pink sign wall, no people, no text'),
    prods=[('01', 'a deep red lace underwired bra (flat lay)', 'Sujetador de encaje'),
           ('13', 'a nude seamless moulded t-shirt bra (flat lay)', 'Sujetador sin costuras'),
           ('18', 'a black microfibre high-waist brief with a wide pink waistband (flat lay)', 'Braga alta'),
           ('10', 'a cream satin long pyjama set with a brown animal print, folded on a hanger (flat lay)', 'Pijama satinado'),
           ('08', 'a white soft fleece hooded dressing gown on a wooden hanger (flat lay)', 'Bata polar'),
           ('26', 'a raspberry pink knitted lounge set with a long cardigan, folded (flat lay)', 'Conjunto de punto')],
    l1=('12', 'a folded light blue cotton pyjama set with white piping on an unmade bed with white sheets and a cup of tea'),
    l2=('04', 'a pile of folded striped and pink knitted socks and thermal tops on a wooden table'),
    cats=[('Sujetadores', 'p1'), ('Pijamas', 'p4'), ('Batas', 'p5')])

S['donna-islantilla'] = dict(
    place='a whitewashed street near the beach in Islantilla, Huelva, Spain, with bougainvillea and palm trees', who='woman',
    hero=('06', 'a brown faux-fur cape poncho over a long brown satin skirt and suede boots'),
    banner=(None, 'the inside of a bright Andalusian-style fashion boutique in a shopping centre near the beach, white walls, terracotta pots, wooden rails of colourful dresses and a big mirror, no people'),
    prods=[('23', 'a dark green wool jacket embroidered with colourful flowers and leaves', 'Chaqueta bordada'),
           ('07', 'a pink and grey fringed knit poncho cape over a cream top and cream wide trousers', 'Capa de flecos'),
           ('08', 'a black leather waistcoat over a cream top with a brown zebra-print satin maxi skirt', 'Falda de cebra'),
           ('10', 'a long olive and pink floral tiered ruffled maxi dress with long sleeves', 'Vestido de volantes'),
           ('05', 'a white blazer hand-painted with colourful hearts, flowers and doodles over a black top and jeans', 'Chaqueta pintada a mano'),
           ('33', 'burgundy suede ballet flat shoes with small gold studs and a strap', 'Bailarinas con tachas')],
    l1=('09', 'a brown blouse with teal and brown wide striped wide-leg trousers and a long necklace'),
    l2=('12', 'a burgundy floral long-sleeved tiered midi dress'),
    cats=[('Vestidos', 'p4'), ('Chaquetas', 'p1'), ('Calzado', 'p6')])

S['intimo-nicoletta'] = dict(
    place='a sunny street in the Triana district of Seville, Spain, with colourful houses and orange trees', who='curvy',
    opts=['M', 'L', 'XL', '2XL', '3XL'],
    hero=('15', 'a long rust and brown floral print chiffon maxi dress'),
    banner=('15', 'the inside of a cosy women\'s fashion boutique with a cream sofa, warm lights, autumn flowers on the wall and rails of colourful clothes, no people'),
    prods=[('09', 'a white blouse with burgundy polka dots and a tie neck with black trousers', 'Blusa de lunares'),
           ('12', 'a grey and silver faux-fur jacket over a black top and black trousers', 'Chaqueta de pelo'),
           ('20', 'a sleeveless brown and cream tribal print midi dress (the one on the left)', 'Vestido estampado'),
           ('07', 'a mustard gold satin blouse with a tonal floral print over black trousers', 'Blusa satinada'),
           ('30', 'a fuchsia pink short-sleeved midi dress (the one on the left)', 'Vestido fucsia'),
           ('10', 'a burgundy handbag with small gold studs (the one on the right)', 'Bolso con tachas')],
    l1=('29', 'a mustard and cream colour-block midi dress'),
    l2=('33', 'a mustard midi dress with a large black and white leaf print'),
    cats=[('Vestidos', 'p3'), ('Blusas', 'p1'), ('Bolsos', 'p6')])

S['ailec-modas'] = dict(
    place='a sunny street of Algeciras, Cádiz, Spain, with white buildings and palm trees', who='woman',
    hero=('30', 'a camel ribbed knit midi jumper dress with a black belt and black ankle boots'),
    banner=(None, 'the inside of a bright women\'s fashion boutique in Andalusia with white walls, rails of autumn dresses and knitwear, a big mirror and a wooden floor, no people'),
    prods=[('03', 'a sleeveless burgundy fitted knit midi dress covered with small silver studs', 'Vestido de tachas'),
           ('19', 'a burgundy and pink floral print chiffon wrap midi dress with long sleeves', 'Vestido de gasa'),
           ('29', 'a red ribbed knit midi jumper dress with a black belt and black ankle boots', 'Vestido de punto'),
           ('22', 'a cream satin draped long-sleeved top with a brown A-line mini skirt', 'Top drapeado'),
           ('02', 'a leopard print satin midi skirt with a plain white long-sleeved top', 'Falda de leopardo'),
           ('06', 'a black sequin strapless mini dress with a cream faux-fur stole', 'Vestido de lentejuelas')],
    l1=('20', 'a rust floral print chiffon midi dress with a tie waist'),
    l2=('33', 'a brown halter top with a long camel fringed crochet skirt'),
    cats=[('Vestidos', 'p1'), ('Faldas', 'p5'), ('Fiesta', 'p6')])

S['calzados-bergillos'] = dict(niche='calzado',
    place='a sunny whitewashed square in Cártama, Málaga, Spain, with bougainvillea and terracotta tiles', who='woman', h1='Desde 1973,<br>ahora a un clic.',
    hero=('03', 'beige and taupe retro running sneakers with cream wide-leg trousers and a long camel trench coat'),
    banner=(None, 'the inside of a family shoe shop in a Spanish town with wooden shelves full of women\'s and men\'s shoes, a cream seating bench and a mirror, no people, no text'),
    prods=[('02', 'beige and taupe suede retro running sneakers with a brown stripe', 'Deportiva retro'),
           ('09', 'white chunky dad sneakers with grey details', 'Deportiva chunky'),
           ('17', 'black knit sneakers with a gold stripe and a white platform sole', 'Deportiva negra y oro'),
           ('21', 'black suede ankle boots with a block heel and a side zip', 'Botín de ante'),
           ('36', 'taupe suede loafers with a braided strap', 'Mocasín de ante'),
           ('39', 'black leather penny loafers with a chunky lug sole', 'Mocasín de suela gruesa')],
    l1=('26', 'a woman seen from the knees down in cuffed blue jeans and black suede loafers, sitting on a wooden bench'),
    l2=('34', 'black suede ballet flat shoes with small gold studs and a bow on a terracotta tiled floor'),
    cats=[('Deportivas', 'p1'), ('Botines', 'p4'), ('Mocasines', 'p5')])

S['caprichos-deva'] = dict(
    place='a sunny street of Torrellano, Elche, Alicante, Spain, with palm trees', who='woman',
    hero=('10', 'a brown, teal and cream palm-leaf print long-sleeved shirt dress'),
    banner=('17', 'the inside of a cosy women\'s fashion boutique with a floral wallpaper, a white counter, rails of clothes and mannequins, no people, no text'),
    prods=[('02', 'black high-waisted wide-leg sailor trousers with gold buttons and a white top', 'Pantalón marinero'),
           ('08', 'a brown and gold paisley and animal print long-sleeved blouse with knit cuffs', 'Blusa estampada'),
           ('21', 'a black and cream zebra print long-sleeved dress with tall black boots', 'Vestido de cebra'),
           ('24', 'a black knit long-sleeved mini dress with a lace hem and black boots', 'Vestido de punto'),
           ('16', 'a beige, black and brown wide-striped blouse with black trousers', 'Blusa de rayas'),
           ('30', 'a burgundy long-sleeved top with a long black skirt', 'Conjunto granate')],
    l1=('25', 'a black and cream abstract print long dress with boots'),
    l2=('31', 'black straight tailored trousers with a cream jumper'),
    cats=[('Vestidos', 'p3'), ('Blusas', 'p2'), ('Pantalones', 'p1')])

S['giancarlo-novias'] = dict(
    place='a sunny square in Parla, Madrid, Spain', who='man', h1='Trajes de fiesta<br>y de caballero.',
    hero=('38', 'a dark teal slim-fit three-piece suit with a burgundy waistcoat and a burgundy tie'),
    banner=('47', 'the inside of a bridal and ceremony shop with rails of colourful party dresses, white bridal gowns and men\'s suits, mirrors and soft lighting, no people'),
    prods=[('27', 'a charcoal three-piece suit with a white shirt and a black tie', 'Traje de tres piezas'),
           ('29', 'a navy pinstripe three-piece suit with a navy patterned tie', 'Traje diplomático'),
           ('30', 'a black wedding suit with a grey waistcoat and a grey patterned tie', 'Traje de novio'),
           ('42', 'a royal blue slim-fit suit with a light blue shirt and a patterned tie', 'Traje azul'),
           ('46', 'a magenta satin off-the-shoulder mermaid evening gown, worn by a woman', 'Vestido de madrina'),
           ('40', 'a navy suit with a light blue shirt and a pink tie', 'Traje de padrino')],
    l1=('14', 'an ivory lace bridal gown with a deep V neckline, worn by a woman'),
    l2=('37', 'a dark teal suit with a burgundy waistcoat and a burgundy tie'),
    opts=['46', '48', '50', '52', '54', '56'],
    cats=[('Caballero', 'p1'), ('Novio', 'p3'), ('Fiesta', 'p5')])

S['mar-govantes'] = dict(
    place='a sunny pedestrian street of Dos Hermanas, Seville, Spain, with orange trees', who='curvy',
    opts=['42', '44', '46', '48', '50', '52'],
    hero=('13', 'a long orange, green and yellow tropical print maxi dress'),
    banner=('15', 'the inside of a women\'s fashion boutique with walls full of colourful blouses and jumpers on rails, a glass door onto the street and a wooden floor, no people'),
    prods=[('01', 'a long black and white abstract print shirt dress', 'Vestido estampado'),
           ('02', 'a long orange open cardigan over a brown and black paisley print dress', 'Rebeca larga'),
           ('17', 'a long-sleeved blue and grey geometric print maxi dress', 'Vestido largo'),
           ('22', 'a black quilted puffer gilet over a burgundy top and black trousers', 'Chaleco acolchado'),
           ('23', 'a light blue cable-knit jumper with a white lace hem and navy trousers', 'Jersey con encaje'),
           ('25', 'a purple, green and orange zigzag knit midi dress', 'Vestido de zigzag')],
    l1=('09', 'a teal and purple printed blouse and wide trousers set with a gold belt'),
    l2=('31', 'a violet trouser suit with a pink printed scarf'),
    cats=[('Vestidos', 'p1'), ('Punto', 'p5'), ('Chalecos', 'p4')])

S['moda-guay'] = dict(
    place='the harbour promenade of Mahón, Menorca, Spain, with white houses and boats', who='curvy', h1='Moda curvy,<br>de la M a la 3XL.',
    opts=['M', 'L', 'XL', '2XL', '3XL'],
    hero=('26', 'a cream faux-fur zip-up gilet over a cream jumper and cream wide-leg trousers (the one on the left)'),
    banner=(None, 'the inside of a bright women\'s fashion boutique in Menorca with white walls, wooden rails of knitwear and coats, a jewellery display and a big window onto a sunny street, no people'),
    prods=[('09', 'a chocolate brown faux-fur zip-up gilet over a black top and dark trousers (the second from the left)', 'Chaleco de pelo'),
           ('11', 'a cream, burgundy and brown wavy-striped V-neck jumper with white jeans (the second from the left)', 'Jersey de ondas'),
           ('24', 'a black and white striped polo-collar jumper with jeans', 'Jersey a rayas'),
           ('29', 'a white fluffy knit zip-up cardigan with white trousers (the one on the right)', 'Cárdigan de pelo'),
           ('05', 'a chocolate brown quilted handbag with small gold studs and a gold chain strap', 'Bolso con tachas'),
           ('12', 'a gold chain necklace with a starfish, shell and charm pendants and matching gold star stud earrings on beige sand (flat lay)', 'Collar estrella de mar')],
    l1=('33', 'a brown and cream geometric print long-sleeved top with cream trousers, carrying shopping bags'),
    l2=('13', 'a dark brown faux-fur handbag and a paisley embroidered fringed shawl on a cream armchair'),
    cats=[('Chalecos', 'p1'), ('Jerséis', 'p2'), ('Complementos', 'p5')])

S['carmen-roba-complements'] = dict(
    place='the seaside promenade of Moraira, Teulada, Alicante, Spain, with the Mediterranean behind', who='mature',
    hero=('18', 'a periwinkle blue long evening gown with a flowing chiffon cape'),
    banner=('14', 'the inside of an elegant fashion boutique with rails of colourful party dresses, a round marble table with dried flowers and soft lighting, no people'),
    prods=[('15', 'a fuchsia satin long evening dress with long cape sleeves', 'Vestido de fiesta'),
           ('09', 'a grey oversized knit jumper with a black abstract flower appliqué and black trousers', 'Jersey con flor'),
           ('08', 'a navy satin structured long-sleeved top with a navy midi skirt', 'Conjunto marino'),
           ('23', 'a sleeveless magenta and black floral jacquard midi dress', 'Vestido de jacquard'),
           ('28', 'a long burgundy wool double-breasted coat with burgundy knee-high boots', 'Abrigo burdeos'),
           ('22', 'a black sequin high-neck long-sleeved top with black trousers', 'Jersey de lentejuelas')],
    l1=('35', 'a beige trench coat over a black and white print dress'),
    l2=('32', 'a navy blouse with a navy and brown check maxi skirt'),
    cats=[('Fiesta', 'p1'), ('Abrigos', 'p5'), ('Punto', 'p2')])
