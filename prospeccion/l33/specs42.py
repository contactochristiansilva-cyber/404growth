# Lote 42 (22/11/2026): las 36 del scrapeo del 21-22/11 (sel42.json), con la propuesta v42 (gen42.py) y la tienda «Editorial» (gen37a.py).
# Referencias NN = las fotos de su Instagram (scratchpad l42/rf/<usuario>/NN.jpg; en Flow, con la cara tapada: n<slug>-NN.jpg).
# Nunca referencias con menores.

S['la-plateria-del-sur'] = dict(
    place='Jerez de la Frontera', who='none', theme=dict(acc='#9E2A2B'),
    hero=('31', 'a red coral cross pendant with gold caps on a fine gold chain'),
    banner=(None, 'the inside of a small silver jewellery shop in Andalusia with dark wooden glass display cases full of crosses and medals, warm golden light and a whitewashed wall, no people, no text'),
    prods=[('12', 'a red enamel cross pendant with a gold frame on a fine gold chain', 'Cruz roja'),
           ('22', 'an ornate turquoise and gold cross pendant on a fine gold chain', 'Cruz turquesa'),
           ('10', 'red coral bead hoop earrings', 'Aros de coral'),
           ('23', 'a long red drop earring with a gold bow and a red cabochon', 'Pendientes de lazo'),
           ('34', 'a silver cross pendant with a gold inner cross on a silver paperclip chain', 'Cruz de plata'),
           ('14', 'a set of oxidised silver religious medal pendant and matching earrings', 'Medallas de plata')],
    l1=('20', 'many gold and red enamel cross pendants on chains laid on a white box'),
    l2=('19', 'two cross necklaces in red and silver on a black velvet bust with red coral hoops'),
    cats=[('Cruces', 'p1'), ('Pendientes', 'p3'), ('Plata', 'p5')])

S['joyeria-molina-cuevas'] = dict(
    place='Madrid', who='none', theme=dict(acc='#7A1F2B'),
    hero=('18', 'a pair of vintage diamond and white South Sea pearl drop earrings in platinum'),
    banner=(None, 'an elegant antique jewellery salon in Madrid with deep red damask walls, gilded wooden armchairs, glass cabinets with vintage jewels and warm light, no people, no text'),
    prods=[('11', 'a three-row diamond tennis bracelet in white gold', 'Pulsera de diamantes'),
           ('21', 'an aquamarine cocktail ring framed in diamonds in white gold', 'Anillo de aguamarina'),
           ('25', 'a yellow gold flower garland necklace', 'Collar de flores'),
           ('17', 'a pair of yellow gold wing earrings with small diamonds', 'Pendientes de alas'),
           ('32', 'a vintage toi-et-moi ring with a pearl and an old-cut diamond in yellow gold', 'Anillo tú y yo'),
           ('14', 'a pair of long diamond cascade drop earrings', 'Pendientes de cascada')],
    l1=('28', 'an art deco diamond bow necklace on a black velvet bust'),
    l2=('10', 'a 1950s yellow gold knot necklace with two tassels on pale velvet'),
    cats=[('Pendientes', 'p4'), ('Anillos', 'p2'), ('Pulseras', 'p1')])

S['jardilin'] = dict(   # zapatería infantil: nunca niños, solo producto (bodegones)
    place='Bilbao', who='none', niche='calzado', still=True,
    hero=('20', "a row of children's leather Mary Jane shoes in lime green, orange and green, displayed on a wooden table in a shoe shop with a vintage carousel horse behind"),
    banner=(None, "the inside of a classic children's shoe shop in Bilbao with wooden shelves full of small shoes, a vintage carousel horse, warm lights and a wooden floor, no people, no text"),
    prods=[('21', "children's metallic silver and beige leather Mary Jane shoes with a strap", 'Merceditas metalizadas'),
           ('15', "children's Menorcan avarca sandal shoes in yellow, glitter and black", 'Menorquinas'),
           ('17', "children's tan and brown leather closed-toe T-bar sandal shoes", 'Sandalias de cuero'),
           ('23', "children's sporty closed-toe sandal shoes in navy blue and lime green with a bungee lace", 'Sandalias de montaña'),
           ('32', "children's pastel leather ballet flat shoes with a bow in light blue, pink and white", 'Bailarinas de lazo'),
           ('35', "children's suede retro sneakers in green, pink and mustard with a hook-and-loop strap", 'Zapatillas retro')],
    l1=('28', "a circle of children's leather ballet flat shoes in many colours on a grey patterned tiled floor"),
    l2=('16', "children's white and pink leather sandal shoes on green grass in the sun"),
    cats=[('Merceditas', 'p1'), ('Sandalias', 'p3'), ('Zapatillas', 'p6')])

S['aine-shoes'] = dict(
    place='a street in the centre of A Coruña, Galicia, Spain, with white glazed balconies (galerías)', who='woman', niche='calzado',
    hero=('17', 'black leather knee-high riding boots with a gold buckle strap, with dark trousers'),
    banner=('15', 'the inside of a bright women\'s shoe boutique with white shelves of shoes and handbags, a long glass display table of shoes, dried flowers and branches, no people, no text'),
    prods=[('01', 'tan suede lace-up ankle boots with a low block heel', 'Botines de cordones'),
           ('02', 'black leather Chelsea boots with a chunky lug sole', 'Botas Chelsea'),
           ('06', 'black patent leather tassel loafers with a chunky sole', 'Mocasines de borlas'),
           ('18', 'brown patent leather penny loafers', 'Mocasines marrones'),
           ('24', 'black leather pointed ankle boots with a ruched shaft and a low block heel', 'Botines fruncidos'),
           ('28', 'beige quilted leather lace-up sneakers with a white sole', 'Zapatillas acolchadas')],
    l1=('27', 'tan suede and black leather western ankle boots on a white shelf with dried flowers'),
    l2=('26', 'a tan leather tote bag next to green suede retro sneakers on a white shelf'),
    cats=[('Botas y botines', 'p1'), ('Mocasines', 'p3'), ('Zapatillas', 'p6')])

S['a-saia-da-carolina'] = dict(
    place='a quiet granite street in the centre of Carballo, Galicia, Spain, with stone houses and green doors', who='woman',
    hero=('11', 'a red satin off-the-shoulder ruffled top with small pearls and a matching red satin pencil skirt with a pearl fringe hem, red heels'),
    banner=(None, 'the inside of a stylish fashion boutique in Galicia with deep red velvet fitting room curtains, black shelves with handbags, rails of dresses and a warm wooden floor, no people, no text'),
    prods=[('02', 'a fuchsia jersey midi dress with a twisted one-shoulder neckline and a slit', 'Vestido fucsia'),
           ('05', 'a teal green satin wrap midi dress with short sleeves, a belt and a front slit', 'Vestido verde azulado'),
           ('33', 'a long white crochet lace slip dress with thin straps', 'Vestido de crochet'),
           ('27', 'a burgundy halter-neck wide-leg jumpsuit', 'Mono burdeos'),
           ('32', 'a beige utility jumpsuit with a belt and long sleeves', 'Mono safari'),
           ('13', 'a long green and burgundy zigzag print maxi dress with long sleeves and a black belt', 'Vestido zigzag')],
    l1=('26', 'a black waistcoat with a red embroidered fringed shawl over a white shirt and wide light jeans'),
    l2=('23', 'a patchwork printed kimono jacket over a black top with a chunky red necklace'),
    cats=[('Vestidos', 'p1'), ('Monos', 'p4'), ('Invitada', 'p2')])

S['lalex-joies'] = dict(
    place='Tarragona', who='none', theme=dict(acc='#3B3B3B'),
    hero=('01', 'a round sterling silver pendant shaped like a gothic rose window on a fine silver ball chain'),
    banner=(None, "the inside of a silversmith's jewellery shop in Catalonia with a wooden workbench, small tools, white display cases with silver rings and pendants and a stone arch, no people, no text"),
    prods=[('02', 'a wide sterling silver ring with a pierced architectural facade pattern', 'Anillo arquitectura'),
           ('15', 'a sterling silver pendant shaped like a mountain ridge silhouette', 'Colgante La Mola'),
           ('20', 'a minimalist sterling silver cross pendant on a thin silver wire choker', 'Cruz de plata'),
           ('03', 'a sterling silver ring shaped like a row of Gaudí-style catenary arches', 'Anillo de arcos'),
           ('28', 'a pair of yellow gold band rings with small notches', 'Alianzas de oro'),
           ('17', 'a sterling silver ring shaped like an organic wave', 'Anillo ola')],
    l1=('11', 'several sterling silver crown-shaped rings with arches on an old wooden workbench, warm light'),
    l2=('10', 'a braided cord bracelet with a silver arches plaque among chestnuts and yellow gourds'),
    cats=[('Anillos', 'p1'), ('Colgantes', 'p2'), ('Oro', 'p5')])

S['sinu-and-son'] = dict(   # joyería urbana: sin armas, sin relojes de marca ni personajes
    place='Barcelona', who='none', theme=dict(acc='#1F6F6B'),
    hero=('29', 'a large iced-out cross pendant fully set with white stones with a small gold figure at the centre'),
    banner=(None, 'the inside of a modern urban jewellery studio in Barcelona with black walls, a glowing turquoise round neon emblem with no letters, black velvet busts with iced chains in glass cases and warm spotlights, no people, no text'),
    prods=[('05', 'an iced-out gothic letter O pendant fully set with white stones on a tennis chain', 'Inicial gótica'),
           ('11', 'a yellow gold number 17 pendant in gothic style set with white stones', 'Colgante de número'),
           ('12', 'a yellow gold Cuban link chain set with stones with a small iced house-shaped pendant', 'Cadena cubana'),
           ('15', 'a yellow gold signet ring with a gothic letter M fully set with white stones', 'Anillo con inicial'),
           (None, 'a white gold cocktail ring topped with one five-pointed star fully pavé-set with small white stones on a plain round band, with no letters or initials', 'Anillo estrella'),
           ('36', 'a yellow gold eternity band set with white and black stones', 'Alianza bicolor')],
    l1=('30', 'a tiger-eye bead rosary with a silver cross and a silver medal on dark velvet'),
    l2=('21', 'macro close-up of a heavy yellow gold rope chain on black'),
    cats=[('Colgantes', 'p1'), ('Cadenas', 'p3'), ('Anillos', 'p4')])

S['abaco-moda'] = dict(
    place='the sunny Plaza Mayor of Plasencia, Cáceres, Spain, with stone arcades', who='woman',
    hero=('06', 'a burgundy satin blouse with balloon sleeves and matching burgundy satin balloon trousers'),
    banner=(None, 'the inside of a bright fashion boutique with terracotta floor tiles, tall palm plants, rails full of autumn clothes, a burgundy velvet pouf and a backlit golden letter-free wall sconce, no people, no text'),
    prods=[('05', 'a camel teddy faux-fur jacket with gold military frogging over a white lace blouse', 'Chaqueta húsar'),
           ('14', 'a brown and pink check belted coat over a plum turtleneck', 'Abrigo de cuadros'),
           ('15', 'an olive green satin blouse with a high neck with light blue embroidered jeans', 'Blusa verde'),
           ('27', 'a pink and burgundy striped knit sweater with dark wide jeans', 'Jersey de rayas'),
           ('22', 'leopard print wide-leg trousers with a cream blouse', 'Pantalón de leopardo'),
           ('04', 'a burgundy quilted velvet shoulder bag with leather handles', 'Bolso burdeos')],
    l1=('23', 'a navy knit vest over a denim shirt with dark barrel jeans'),
    l2=('29', 'an olive green padded jacket over a navy jumper and grey trousers, worn by a man'),
    cats=[('Blusas', 'p3'), ('Abrigos', 'p2'), ('Punto', 'p4')])

S['la-gatita-presumida'] = dict(
    place='a sunny seafront street in Sanxenxo, Pontevedra, Spain, with the Atlantic and white buildings', who='woman',
    hero=('25', 'a black and grey argyle knit sweater over a white shirt with cream wide jeans and a long black coat'),
    banner=(None, 'the inside of a warm pink-toned fashion boutique with rounded arches, a modern brass globe chandelier, a terrazzo counter, rails of neutral knitwear and a pink velvet bench, no people, no text'),
    prods=[('04', 'a black and white Breton striped long-sleeve top with dark trousers', 'Camiseta marinera'),
           ('06', 'a burgundy sweater with a cut-out shoulder and white trousers', 'Jersey burdeos'),
           ('12', 'a brown Fair Isle knit sweater with blue wide jeans', 'Jersey de ochos'),
           ('23', 'a cream and brown argyle chunky knit sweater', 'Jersey de rombos'),
           ('31', 'a navy and grey check jacket with matching check wide trousers', 'Conjunto de cuadros'),
           ('17', 'a navy tailored jacket with matching wide trousers', 'Traje azul marino')],
    l1=('16', 'a beige Fair Isle sweater with brown corduroy trousers and white sneakers'),
    l2=('24', 'a grey striped oversized shirt with straight blue jeans'),
    cats=[('Punto', 'p3'), ('Camisetas', 'p1'), ('Trajes', 'p6')])

S['la-casa-de-las-cuentas'] = dict(
    place='Huelva', who='none', theme=dict(acc='#C0392B'),
    hero=('30', 'a pair of statement earrings with a red coral cabochon, a gold bar and a cluster of red coral drops'),
    banner=(None, 'the inside of a small Andalusian jewellery and accessories shop with white walls, gold stands full of colourful flamenca earrings, coral necklaces on busts and a wooden counter, no people, no text'),
    prods=[('26', 'a pair of gold sun-shaped earrings with purple stones and coral bead drops', 'Pendientes sol'),
           ('27', 'a pair of gold earrings with a green stone and a red coral bead drop', 'Pendientes de jade'),
           ('29', 'a pair of gold earrings with a purple square stone and small pearls', 'Pendientes morados'),
           ('23', 'a red coral bead cross necklace', 'Collar de cruz'),
           ('21', 'a turquoise and coral bead choker with a carved bone centrepiece', 'Gargantilla turquesa'),
           ('01', 'a set of flamenca hair combs with fuchsia flowers and pearls', 'Peinas de flamenca')],
    l1=('12', 'a tortoiseshell flamenca hair comb with coral and gold earrings on a cream table'),
    l2=('02', 'several coral and black bead necklaces with gold medals on white busts'),
    cats=[('Pendientes', 'p1'), ('Collares', 'p4'), ('Flamenca', 'p6')])

S['cambia-t'] = dict(
    place='a sunny whitewashed street in the old town of Benidorm, Alicante, Spain, near the sea', who='mature',
    hero=('13', 'a rust satin camisole with a white tropical leaf print and lace trim with matching rust satin wide-leg trousers'),
    banner=(None, 'the inside of a bright Mediterranean fashion boutique with olive green velvet fitting room curtains, white walls, a glass chandelier, rails of colourful dresses and flamenca dresses with ruffles, no people, no text'),
    prods=[('19', 'an olive green satin asymmetric top with matching olive satin wide trousers', 'Conjunto oliva'),
           ('27', 'a green and white ikat print blouse with champagne satin wide trousers', 'Blusa estampada'),
           ('15', 'a brown double-breasted waistcoat over a white shirt with a leopard print midi skirt', 'Chaleco y falda'),
           ('32', 'a navy blue satin wrap blouse with matching navy satin wide trousers', 'Conjunto marino'),
           ('06', 'a light blue flamenca dress with flounced sleeves and a ruffled hem with a navy fringed shawl', 'Traje de flamenca'),
           ('03', 'a black polka dot flamenca dress with white ruffles and a red fringed shawl', 'Flamenca de lunares')],
    l1=('02', 'a taupe knit top with a matching cardigan and taupe wide trousers'),
    l2=('28', 'a black and white zebra print satin shirt with matching trousers'),
    cats=[('Conjuntos', 'p1'), ('Blusas', 'p2'), ('Flamenca', 'p5')])

S['nama'] = dict(
    place='a sunny street in the old town of Jerez de la Frontera, Cádiz, Spain, with whitewashed walls and orange trees', who='woman',
    hero=('06', 'a cream tapestry jacket with a red and green floral pattern over a white shirt with blue jeans'),
    banner=(None, 'the inside of a bohemian fashion boutique with a huge installation of dried pampas grass and dried flowers on the ceiling, rattan lamps, rails of colourful embroidered jackets and a light floor, no people, no text'),
    prods=[('09', 'a colourful embroidered patchwork jacket with a large cream faux-fur collar', 'Chaqueta con pelo'),
           ('12', 'a burgundy quilted jacket with a blue and cream floral print', 'Chaqueta burdeos'),
           ('20', 'a lilac long-sleeve wrap midi dress with a belt', 'Vestido lila'),
           (None, 'a mustard yellow chunky knit cardigan with small embroidered flowers over a white blouse with light blue jeans', 'Rebeca bordada'),   # el de la foto 26 era un caftán: fuera (nada que recuerde a lo árabe)
           ('30', 'a teal tiered maxi dress with an orange floral print', 'Vestido de flores'),
           ('36', 'a chartreuse green satin wrap jumpsuit with wide legs', 'Mono verde')],
    l1=('25', 'a coral one-shoulder dress with a black velvet clutch and a black wide-brim hat'),
    l2=('31', 'a green and black striped sweater with light blue jeans'),
    cats=[('Chaquetas', 'p1'), ('Vestidos', 'p3'), ('Invitada', 'p6')])

S['rk-sport'] = dict(   # streetwear: sin referencias (sus prendas y zapatillas llevan marcas), todo genérico y sin logos
    place='a city street in Santa Coloma de Gramenet, Barcelona, Spain, with brick apartment buildings', who='man',
    hero=(None, 'a black zip-up tracksuit with white piping and black and white high-top sneakers'),
    banner=(None, 'the inside of a streetwear shop with a graffiti wall, glass counters, walls full of flat-brim caps, sneakers on shelves and oversized graphic t-shirts on rails, neon lights, no people, no text, no logos'),
    prods=[(None, 'a black zip-up tracksuit jacket with white piping and matching joggers', 'Chándal negro'),
           (None, 'a white oversized t-shirt with an abstract red splatter print and white jeans', 'Camiseta salpicada'),
           (None, 'black stacked skinny jeans with a waxed coated finish and a black t-shirt', 'Vaquero encerado'),
           (None, 'vintage-wash beige distressed skinny jeans with a black t-shirt', 'Vaquero lavado'),
           (None, 'a plain black flat-brim snapback cap with a red under-brim', 'Gorra plana'),
           (None, 'chunky high-top basketball sneakers in black and red leather with no logos', 'Zapatillas altas')],
    l1=(None, 'a black oversized t-shirt with an abstract print, black jeans and a black cap laid out as a flat lay on a grey tiled floor, no people'),
    l2=(None, 'a black tracksuit with white stripes and white sneakers, worn by a man'),
    cats=[('Chándals', 'p1'), ('Vaqueros', 'p3'), ('Gorras', 'p5')])

S['oops-complementos'] = dict(
    place='a street in the centre of Vigo, Galicia, Spain, with granite buildings', who='mature',
    hero=('17', 'a burgundy quilted padded hooded coat over a white top and blue jeans'),
    banner=(None, 'the inside of a bright white fashion boutique with black metal clothes rails of coats and knitwear, wooden round tables with handbags and scarves and a light floor, no people, no text'),
    prods=[('15', 'a long beige trench coat with a belt', 'Gabardina beige'),
           ('04', 'a burgundy hooded raincoat with a white polka dot print', 'Chubasquero de lunares'),
           ('09', 'a navy, blue and taupe argyle sweater with blue jeans', 'Jersey de rombos'),
           ('13', 'a khaki quilted hooded parka with a zip', 'Parka acolchada'),
           ('27', 'a burgundy faux-leather bomber jacket over a white top and cream trousers', 'Cazadora burdeos'),
           ('08', 'a grey nylon tote bag with black handles and a tassel', 'Bolso gris')],
    l1=('25', 'a black and beige palm leaf print scarf'),
    l2=('29', 'a soft grey wool scarf folded on a cork stand'),
    cats=[('Abrigos', 'p1'), ('Punto', 'p3'), ('Bolsos', 'p6')])

S['i-love-complementos'] = dict(
    place='a street in the centre of Vigo, Galicia, Spain, with granite buildings', who='curvy',
    hero=('24', 'a long turquoise, red and cream zigzag knit cardigan over a white striped shirt with straight trousers'),
    banner=(None, 'the inside of a cosy fashion boutique with a pastel floral wallpaper, a teal velvet armchair, a white ornate mirror and rails of autumn clothes, no people, no text'),
    prods=[('07', 'a burgundy satin shirt with matching burgundy wide trousers', 'Conjunto burdeos'),
           ('10', 'a long black and white check shirt jacket over a white turtleneck with brown balloon trousers', 'Sobrecamisa de cuadros'),
           ('13', 'a dark green and grey floral print kimono jacket with wide trousers', 'Kimono estampado'),
           ('16', 'a beige jacket with a brown collar over a brown top with a printed skirt', 'Chaqueta beige'),
           ('29', 'a plum satin blouse with matching plum satin trousers', 'Conjunto satinado'),
           ('32', 'an olive green chunky knit sweater with a matching olive skirt', 'Conjunto verde')],
    l1=('18', 'a long camel knit cardigan with a leopard print scarf and a burgundy bag'),
    l2=('27', 'a beige knit V-neck sweater with brown balloon trousers'),
    cats=[('Conjuntos', 'p1'), ('Chaquetas', 'p2'), ('Punto', 'p6')])

S['amancia'] = dict(
    place='a sunny street in the old town of Jerez de la Frontera, Cádiz, Spain, with palm trees and stone buildings', who='woman',
    hero=('26', 'a white blouse with a long teal ruffled skirt and a wide red sash belt'),
    banner=('18', 'the inside of a colourful fashion boutique with rails packed with colourful clothes, a wooden central table with jewellery, mannequins in bright dresses and warm lights, no people, no text'),
    prods=[('20', 'a long brown wrap jumpsuit with long sleeves and a belt, with a turquoise clutch', 'Mono marrón'),
           ('28', 'a long fuchsia draped wrap dress with long sleeves', 'Vestido fucsia'),
           ('24', 'a red midi dress with a ruffled shoulder peplum', 'Vestido rojo'),
           ('17', 'a mustard velvet midi dress with flutter sleeves', 'Vestido de terciopelo'),
           ('33', 'a long emerald green satin halter-neck dress with a flared hem', 'Vestido esmeralda'),
           ('34', 'two chunky resin bangle bracelets in pink and cream with gold-set stones', 'Brazaletes de resina')],
    l1=('09', 'a cropped camel trench coat over a white top with jeans and a red bead necklace'),
    l2=('35', 'cream and olive green resin bangles with coral heart stones on a wrist'),
    cats=[('Vestidos', 'p2'), ('Monos', 'p1'), ('Bisutería', 'p6')])

S['deleite-de-tela'] = dict(
    place='a narrow pedestrian street in the centre of Murcia, Spain, with shop windows and potted plants', who='mature',
    hero=('25', 'a long rust satin wrap dress with long sleeves and a deep V-neck'),
    banner=(None, 'the inside of a warm fashion and jewellery boutique with velvet drum pendant lamps in burgundy and green, rails of autumn clothes, a wall of colourful necklaces and a light wooden floor, no people, no text'),
    prods=[('01', 'a dark green faux-leather coat over a white top with brown wide trousers', 'Abrigo verde'),
           ('10', 'a navy double-breasted short jacket with a blue pleated midi skirt', 'Chaqueta marino'),
           ('11', 'a long brown wool coat with a high collar', 'Abrigo camel'),
           ('13', 'a leopard print short jacket over a dark skirt', 'Chaqueta de leopardo'),
           ('16', 'a burgundy and silver silk reversible kimono jacket over black trousers', 'Kimono de seda'),
           ('24', 'a dark green knit sweater with a matching long green knit skirt', 'Conjunto de punto')],
    l1=('15', 'a mustard silk vest with large fuchsia and turquoise embroidered flowers'),
    l2=('31', 'a fluffy beige faux-fur gilet over a black top'),
    cats=[('Abrigos', 'p1'), ('Kimonos', 'p5'), ('Punto', 'p6')])

S['ria-pita'] = dict(   # moda flamenca: nunca las fotos con niñas
    place='a whitewashed street in the old town of Estepona, Málaga, Spain, with flower pots on the walls', who='woman',
    hero=('17', 'a light blue flamenca dress with flounced sleeves and a long ruffled hem with a cream embroidered fringed shawl with pink flowers'),
    banner=(None, 'the inside of an Andalusian flamenca fashion shop with rails packed with colourful flamenca dresses with ruffles, embroidered shawls, big hair flowers and flamenco shoes on a shelf, no people, no text'),
    prods=[('14', 'a red flamenca dress with layers of ruffles and a cream embroidered shawl', 'Traje de volantes'),
           ('01', 'a mint and black flamenca dress with black ruffles and a black embroidered shawl', 'Flamenca menta'),
           ('02', 'a white and purple flamenca dress with purple ruffles', 'Flamenca morada'),
           ('15', 'a cream embroidered silk manila shawl with pink flowers and long fringes', 'Mantón bordado'),
           ('19', 'black leather flamenco dance shoes with a double strap and a wooden heel', 'Zapato de baile'),
           ('11', 'red glitter flamenco dance shoes with a strap', 'Zapato flamenco rojo')],
    l1=('13', 'a big pink and red flamenca hair flower and gold earrings on a mannequin'),
    l2=('20', 'black and red leather flamenco shoes with laces on a red hat'),
    cats=[('Trajes de flamenca', 'p1'), ('Mantones', 'p4'), ('Zapatos de baile', 'p5')])

S['lorma'] = dict(   # zapatería y ropa interior/térmica; casi todas sus fotos son cajas: muchas sin referencia
    place='a stone arcaded street in the old town of Avilés, Asturias, Spain, on a rainy-bright day', who='woman', niche='calzado',
    hero=(None, 'dark brown leather knee-high boots with a low block heel, with a camel coat and dark jeans'),
    banner=(None, 'the inside of a busy shoe shop in Asturias with white shelves full of boots, ankle boots and sneakers, small handbags, a central table with shoe boxes and warm lights, no people, no text'),
    prods=[(None, 'black leather lace-up comfort ankle boots with a chunky rubber sole', 'Botines de cordones'),
           (None, 'brown suede slip-on loafer shoes with a cushioned sole', 'Mocasines de ante'),
           (None, 'grey suede sporty sneakers with a thick white sole', 'Zapatillas grises'),
           (None, 'black leather Chelsea ankle boots with a low heel', 'Botas Chelsea'),
           ('05', 'a black thermal long-sleeve top with a lace neckline (flat lay)', 'Camiseta térmica'),
           ('04', 'two pairs of chunky ribbed wool socks in beige and charcoal (flat lay)', 'Calcetines de lana')],
    l1=(None, 'black leather ankle boots and a small crossbody bag on a white shelf in a bright shoe shop'),
    l2=('07', 'navy and black thermal long-sleeve tops with lace hanging on wooden hooks'),
    cats=[('Botas y botines', 'p1'), ('Zapatillas', 'p3'), ('Térmicos', 'p5')])

S['joyeria-esencia'] = dict(   # vende marcas (Nomination, Majorica, Lladró…): fotos genéricas, sin diseños de marca
    place='Mojácar', who='none', theme=dict(acc='#B8860B'),
    hero=('17', 'a gold paperclip chain necklace with a blue butterfly charm and two engraved silver and gold coin pendants'),
    banner=(None, 'the inside of a bright modern jewellery shop in Andalusia with white glass display cases full of necklaces, bracelets and watches, light blue accents and soft spotlights, no people, no text'),
    prods=[('09', 'a gold paperclip chain necklace with an engraved gold coin pendant', 'Collar de medalla'),
           ('26', 'a green enamel butterfly brooch with gold details', 'Broche mariposa'),
           ('28', 'colourful enamel butterfly brooches in green and purple with gold edges', 'Broches esmaltados'),
           ('13', 'a gold chain necklace with a round tiger-eye stone pendant', 'Collar ojo de tigre'),
           ('27', 'a pink enamel starfish brooch with gold bangles', 'Broche estrella de mar'),
           (None, 'a pair of polished gold hoop earrings with a small white pearl drop', 'Aros con perla')],
    l1=('05', 'a white jewellery display case with gold necklaces, bracelets and a watch under soft light'),
    l2=(None, 'stacked gold rings and gold hoop earrings on a cream ceramic dish with dried flowers'),
    cats=[('Collares', 'p1'), ('Broches', 'p2'), ('Pendientes', 'p6')])

# Modas Carisma: fuera (22/11): modascarisma.com ya es una tienda Shopify con unos 35 productos y carrito.

S['glamour-moda-vigo'] = dict(
    place='a street in the centre of Vigo, Galicia, Spain, with granite buildings and trees', who='mature',
    hero=('20', 'a cobalt blue one-shoulder midi dress with a side slit and gold sandals'),
    banner=('02', 'the inside of a bright women\'s fashion boutique with white built-in wardrobes full of red, brown and cream clothes, hats and handbags on the shelves, a vintage sewing machine and soft light, no people, no text'),
    prods=[('22', 'a coral pink fitted midi dress with large fabric roses on the shoulder', 'Vestido con flores'),
           ('23', 'a turquoise and white floral off-the-shoulder ruffled midi dress', 'Vestido de flores'),
           ('17', 'a light blue waistcoat with matching light blue wide trousers', 'Traje chaleco'),
           ('13', 'a navy blazer over a white top with cream trousers and a red silk scarf', 'Blazer marino'),
           ('12', 'a beige chunky knit hooded jacket with cream trousers', 'Chaqueta de punto'),
           ('05', 'a burgundy leather handbag with a printed silk scarf tied to the handle', 'Bolso burdeos')],
    l1=('31', 'a blue linen shirt with a blue and white palm print midi skirt and a straw bag'),
    l2=('15', 'a red eyelet cotton shirt dress with a belt and a red handbag'),
    cats=[('Vestidos', 'p1'), ('Trajes', 'p3'), ('Bolsos', 'p6')])
# TJ Moda: fuera (22/11): anunció el cierre definitivo («Sábado 24 de octubre cerramos definitivamente») y está liquidando.
# Más que Divas: fuera (22/11): en sus vídeos salen cajas y bolsos de marcas de lujo a precios de 17-30 €; no montamos tienda para eso.

S['crisly-coquette'] = dict(
    place='a sunny street in a Spanish town centre with modern shop fronts', who='curvy',
    hero=('24', 'a burgundy faux-leather oversized jacket over a black and white check shirt with black wide jogger trousers'),
    banner=(None, 'the inside of a small modern fashion boutique with a light wooden slat wall, a round mirror, pink cherry blossom branches, rails of black, grey and brown clothes and a light wooden floor, no people, no text'),
    prods=[('13', 'a black fitted mini dress with puff sleeves and a corset lace-up front', 'Vestido corsé'),
           ('15', 'a brown fitted mini dress with puff sleeves and a corset lace-up front', 'Vestido corsé marrón'),
           ('17', 'a long grey oversized blazer over a grey crop top and grey leggings', 'Blazer gris'),
           ('27', 'a navy and white check flannel shirt over a white top with dark wide trousers', 'Camisa de cuadros'),
           ('34', 'a burgundy long-sleeve bodysuit with black wide jogger trousers', 'Body burdeos'),
           ('12', 'a grey knit hoodie dress', 'Vestido sudadera')],
    l1=('35', 'an olive green fitted long-sleeve top with dark brown wide jogger trousers and white sneakers'),
    l2=('10', 'a black cardigan over a black lace camisole with a brown belt and black trousers'),
    cats=[('Vestidos', 'p1'), ('Chaquetas', 'p3'), ('Conjuntos', 'p5')])

S['chabeli-modas'] = dict(
    place='a sunny street in the old town of Jerez de la Frontera, Cádiz, Spain, with whitewashed walls', who='woman',
    hero=('20', 'an olive green wrap blazer with a tie belt and matching olive wide trousers'),
    banner=(None, 'the inside of a warm fashion boutique with a light wooden slat wall, a big round wall clock, hanging green plants and purple bougainvillea, rails of colourful blouses and jackets and a mirror, no people, no text'),
    prods=[('18', 'a multicolour floral print blouse with black velvet bow ties down the front with white trousers', 'Blusa de lazos'),
           ('19', 'a multicolour striped satin shirt knotted at the waist with light blue jeans', 'Camisa de rayas'),
           ('22', 'a pink, teal and black abstract print blouse with ruffled shoulders and white trousers', 'Blusa con volantes'),
           ('06', 'a brown and cream paisley quilted jacket over a white turtleneck with cream trousers', 'Chaqueta acolchada'),
           ('26', 'a sage green quilted jacket with a big collar over a white blouse with jeans', 'Chaqueta verde'),
           ('17', 'brown suede Mary Jane ballet flat shoes with gold studs (flat lay)', 'Merceditas con tachas')],
    l1=('35', 'a brown argyle knit sweater over a grey turtleneck with white trousers'),
    l2=('08', 'a dark green check blouse with a ruffle collar and a long olive skirt'),
    cats=[('Blusas', 'p1'), ('Chaquetas', 'p4'), ('Trajes', 'p1')])

S['antollos'] = dict(   # multimarca: sin logos ni etiquetas de marca
    place='a granite street in the centre of Verín, Ourense, Galicia, Spain, with stone houses', who='woman',
    hero=('19', 'a fluffy beige faux-fur jacket over a red knit dress with white flower appliqués'),
    banner=(None, 'the inside of a bright multibrand fashion shop with light wooden display frames, rails of padded coats and knitwear, handbags on white shelves and a light grey floor, no people, no text, no logos'),
    prods=[('04', 'a red and cream Nordic pattern knit sweater (no letters)', 'Jersey nórdico'),
           ('25', 'a black leather biker jacket over a rust print dress', 'Cazadora de cuero'),
           ('07', 'an orange hooded puffer jacket with no logos', 'Plumífero naranja'),
           ('34', 'a cream chunky knit cardigan with buttons', 'Rebeca crema'),
           ('35', 'a burgundy quilted gilet with dark brown trousers', 'Chaleco acolchado'),
           ('06', 'a tan pebbled leather tote bag with a shoulder strap', 'Bolso de piel')],
    l1=('12', 'a navy hooded parka over a grey sweater with a beige scarf, worn by a man'),
    l2=('29', 'black rubber Chelsea rain boots with a gum sole next to an orange padded tote bag'),
    cats=[('Abrigos', 'p3'), ('Punto', 'p1'), ('Bolsos', 'p6')])

S['regala-t'] = dict(
    place='a sunny whitewashed street in Palma del Río, Córdoba, Spain, with orange trees', who='woman',
    hero=('25', 'a brown check blazer with matching brown check trousers'),
    banner=('21', 'the inside of a fashion and accessories shop with a marble floor, rails of men\'s and women\'s clothes, a wall of handbags on white shelves and a dark green velvet fitting room curtain, no people, no text'),
    prods=[('20', 'a long black knit dress with gold buttons', 'Vestido de punto'),
           ('26', 'a beige satin blouse with navy wide trousers', 'Blusa beige'),
           ('11', 'a burgundy corduroy overshirt over a white t-shirt with light jeans, worn by a man', 'Sobrecamisa burdeos'),
           ('12', 'a black quarter-zip knit jumper with white trousers, worn by a man', 'Jersey con cremallera'),
           ('13', 'a navy quilted field jacket with a corduroy collar, worn by a man', 'Chaqueta acolchada'),
           (None, 'a brown leather shoulder bag with a gold buckle', 'Bolso marrón')],
    l1=(None, 'a wall of colourful leather handbags on white shelves in a bright shop'),
    l2=(None, 'stainless steel gold-tone necklaces and bracelets on a cream velvet tray'),
    cats=[('Mujer', 'p1'), ('Hombre', 'p3'), ('Bolsos', 'p6')])

S['uniqo-man'] = dict(   # moda de hombre multimarca: sin logos
    place='a sunny street in the centre of Valdepeñas, Ciudad Real, Spain, with white houses and iron balconies', who='man',
    hero=('36', 'a white zip-up harrington jacket over a burgundy knit with white trousers'),
    banner=(None, "the inside of a bright modern men's fashion shop with a long aisle, white shelves of folded shirts and jumpers, rails of jackets and suits, track lights and a light floor, no people, no text, no logos"),
    prods=[('01', 'a white quilted puffer jacket over a navy hoodie with no logos', 'Plumífero blanco'),
           ('06', 'a tan suede overshirt over a ribbed beige knit', 'Sobrecamisa de ante'),
           ('34', 'an olive green padded jacket with a cream scarf and a cream beanie (worn by a man)', 'Chaqueta acolchada'),
           ('31', 'a light blue three-piece suit with a white shirt and a yellow tie', 'Traje azul'),
           ('13', 'a dark grey short-sleeve shirt with matching dark grey trousers over a white vest', 'Conjunto gris'),
           ('35', 'a dark charcoal jacket over a grey jumper with black trousers', 'Chaqueta gris')],
    l1=('21', 'three men in light suits by a swimming pool on a sunny day, one white double-breasted suit'),
    l2=('23', 'a white graphic t-shirt with light blue relaxed jeans'),
    cats=[('Chaquetas', 'p1'), ('Trajes', 'p4'), ('Camisas', 'p5')])

S['casual-sanlucar'] = dict(
    place='a sunny whitewashed street in Sanlúcar de Barrameda, Cádiz, Spain, near the river', who='mature',
    hero=('03', 'a navy blue wool coat with a large blue faux-fur collar'),
    banner=(None, 'the inside of a bright fashion boutique with a big decorative tree of pink bougainvillea flowers, white shelves of handbags, rails full of colourful clothes and a white floor, no people, no text'),
    prods=[('10', 'a short beige trench jacket with a belt over a white blouse', 'Gabardina corta'),
           ('12', 'a burgundy knit sweater with matching burgundy trousers', 'Conjunto burdeos'),
           ('17', 'an olive green and black striped zip-up jacket with blue jeans', 'Chaqueta de rayas'),
           ('21', 'a brown and burgundy check blazer over a white top with jeans', 'Blazer de cuadros'),
           ('24', 'a blue denim jacket with cream wide trousers', 'Cazadora vaquera'),
           ('26', 'a white shirt with a wide turquoise embroidered sash belt and blue jeans', 'Fajín bordado')],
    l1=('25', 'green and teal striped knit sweaters on hangers'),
    l2=('04', 'a brown fitted top with a satin midi skirt and a printed sash belt'),
    cats=[('Chaquetas', 'p1'), ('Conjuntos', 'p2'), ('Fajines', 'p6')])

S['sabrina-ortega'] = dict(   # complementos y bisutería; vende marcas (Guess, Majorica, Liu Jo): solo piezas sin marca
    place='Pontevedra', who='none', theme=dict(acc='#2E6F8E'),
    hero=('18', 'chunky marble resin bangles in pink and turquoise with a natural stone set in gold'),
    banner=(None, 'the inside of a small accessories and jewellery shop in the old town of Pontevedra with glass display cases full of jewellery, handbags on white shelves, silk scarves and dried flowers, no people, no text'),
    prods=[('04', 'a set of chunky gold-plated sterling silver hoop earrings', 'Aros de plata'),
           ('08', 'a sterling silver open bangle with a round blue crystal', 'Brazalete con cristal'),
           ('23', 'a long gold and silver two-tone chain necklace with an oval pendant', 'Collar largo'),
           (None, 'a chunky gold chain necklace with a round gold pendant', 'Collar de eslabones'),
           ('19', 'a white silk scarf with a colourful floral print', 'Fular de flores'),
           ('12', 'a tan leather slouchy hobo bag', 'Bolso hobo')],
    l1=('22', 'folded silk scarves with pink, teal and mint geometric fan prints'),
    l2=('10', 'a gold bangle and a watch on a wrist among dried winter flowers'),
    cats=[('Pendientes', 'p1'), ('Pulseras', 'p2'), ('Fulares', 'p5')])

S['tu-esencia'] = dict(
    place='a sunny street in the centre of Almansa, Albacete, Spain, with a castle on the hill behind', who='woman',
    hero=('10', 'a burgundy fitted knit top with a long tiered grey and burgundy check skirt and a burgundy handbag'),
    banner=(None, 'the inside of a feminine fashion boutique with pale pink damask wallpaper, a pink oval logo-free frame on the wall, white shelves of folded knitwear and handbags and a pink round table, no people, no text'),
    prods=[('07', 'a cream trench jacket with a brown tweed peplum, gold buttons and black trousers', 'Chaqueta peplum'),
           ('28', 'a floral tapestry jacket over a white top with a burgundy midi skirt', 'Chaqueta de tapiz'),
           ('15', 'a grey utility jumpsuit with a cream lace yoke and balloon legs', 'Mono con encaje'),
           ('21', 'a navy, white and burgundy striped polo knit sweater with jeans', 'Polo de rayas'),
           ('27', 'a long leopard print coat over a blue shirt', 'Abrigo de leopardo'),
           ('36', 'a brown and cream check sleeveless top with matching wide trousers', 'Conjunto de cuadros')],
    l1=('23', 'a red pleated blouse with a zebra print hem and a zebra scarf'),
    l2=('19', 'a grey oversized jacket over a burgundy top with burgundy culottes and black boots'),
    cats=[('Chaquetas', 'p1'), ('Conjuntos', 'p6'), ('Punto', 'p4')])

S['modas-cereza'] = dict(
    place='the sunny Plaza Mayor of Plasencia, Cáceres, Spain, with stone arcades', who='mature',
    hero=('03', 'a long green, brown and pink check wool coat over a grey turtleneck with dark trousers'),
    banner=(None, "the inside of a bright women's and men's fashion shop with white shelves of folded jumpers and caps, rails of coats and trousers, ceiling lights and a light grey floor, no people, no text"),
    prods=[('05', 'a red and navy check blazer over a white t-shirt with grey trousers', 'Blazer de cuadros'),
           ('15', 'a black faux-leather jacket with small silver studs', 'Cazadora con tachas'),
           ('16', 'a floral tapestry bomber jacket with a brown collar', 'Bomber de tapiz'),
           ('18', 'a burgundy faux-leather shirt jacket with a matching burgundy pleated skirt', 'Conjunto burdeos'),
           ('19', 'a grey tailored blazer with matching grey wide trousers', 'Traje gris'),
           ('02', 'a cream teddy fleece coat with a shawl collar', 'Abrigo de borreguito')],
    l1=('14', 'black and burgundy cowboy boots and studded bucket bags on white shelves'),
    l2=('32', 'a long brown suede trench coat over a black dress'),
    cats=[('Abrigos', 'p6'), ('Chaquetas', 'p1'), ('Trajes', 'p5')])

S['la-casa-de-ines'] = dict(
    place='a sunny street in the centre of Pozoblanco, Córdoba, Spain, with white houses', who='woman',
    hero=('28', 'a burgundy floral chiffon blouse with a matching burgundy floral mini skirt'),
    banner=('05', 'the inside of a warm fashion boutique with wooden shutter screens, rails of patterned dresses and coats, handbags on wooden stands and a light wooden floor, no people, no text'),
    prods=[('14', 'a white tweed cropped jacket with black trim over a black top with black trousers (flat lay)', 'Chaqueta de tweed'),
           ('17', 'a black faux-fur jacket with a black pleated skirt (flat lay)', 'Abrigo de pelo'),
           ('19', 'a blue and burgundy printed satin kimono jacket with a matching midi skirt (flat lay)', 'Kimono estampado'),
           ('30', 'a dark green knit cape over a black top with green check balloon trousers', 'Capa verde'),
           ('04', 'crochet ponchos in brown, burgundy and cream with fringed faux-fur hems (flat lay)', 'Ponchos de crochet'),
           ('31', 'a camel suede slouchy shoulder bag with a long strap', 'Bolso de ante')],
    l1=('20', 'a grey tweed jacket with a bow and a matching grey midi skirt'),
    l2=('26', 'a white and black polka dot top with matching polka dot trousers and black ankle boots (flat lay)'),
    cats=[('Chaquetas', 'p1'), ('Conjuntos', 'p3'), ('Bolsos', 'p6')])

S['sevilla-flamenca'] = dict(
    place='a sunny street in the Triana neighbourhood of Seville, Spain, with white and ochre houses and orange trees', who='woman',
    hero=('16', 'an orange flamenca dress with many ruffles and a teal embroidered fringed manila shawl with a red hair flower'),
    banner=('05', 'the inside of a huge flamenca fashion store with long rails packed with colourful ruffled flamenca dresses, a wall of flamenca hair flowers in every colour and a light grey floor, no people, no text'),
    prods=[('14', 'an orange flamenca dress with layers of ruffles and a teal embroidered fringed shawl', 'Traje de flamenca'),
           ('11', 'a white flamenca dress with black-trimmed ruffles and an embroidered shawl', 'Flamenca blanca'),
           ('12', 'a black fitted flamenca dress with a red ruffle at the neck and a red shawl', 'Flamenca negra'),
           ('07', 'an orange silk manila shawl with colourful embroidered flowers and long fringes (flat lay)', 'Mantón bordado'),
           ('04', 'big flamenca hair flowers in turquoise, red, yellow and purple (flat lay)', 'Flores de flamenca'),
           (None, 'red leather flamenco dance shoes with a strap and a wooden heel', 'Zapato flamenco')],
    l1=('10', 'a white flamenca dress with black trim seen in a bright flamenca store'),
    l2=(None, 'a flamenca outfit flat lay with red coral earrings, a red hair flower, a fan and a fringed shawl'),
    cats=[('Trajes de flamenca', 'p1'), ('Mantones', 'p4'), ('Complementos', 'p5')])

S['lucia-vela'] = dict(   # invitada y flamenca; nunca las fotos de comunión con niñas
    place='the Renaissance square of Úbeda, Jaén, Spain, with golden stone palaces', who='woman',
    hero=('05', 'a green jacquard jacket with black frog fastenings and matching green wide trousers'),
    banner=(None, 'the inside of an elegant guest-dress and flamenca boutique with racks of colourful party dresses and ruffled flamenca dresses, a vintage dresser with accessories, flowers and warm light, no people, no text'),
    prods=[('06', 'a long burgundy satin wrap dress with a leaf print and a tie waist', 'Vestido de raso'),
           ('10', 'a lilac midi dress with cap sleeves and a belt', 'Vestido lila'),
           ('11', 'an olive satin midi dress with a V-neck', 'Vestido satinado'),
           ('04', 'a grey jacquard jacket with black frog fastenings', 'Chaqueta jacquard'),
           ('34', 'a coral flamenca dress with ruffles and a black embroidered fringed shawl', 'Traje de flamenca'),
           ('31', 'a pink and white polka dot flamenca dress with ruffles', 'Flamenca de lunares')],
    l1=('18', 'rails of colourful polka dot flamenca dresses in a boutique'),
    l2=('33', 'flamenca accessories: red hair flowers, big earrings and fans on a table'),
    cats=[('Invitada', 'p1'), ('Chaquetas', 'p4'), ('Flamenca', 'p5')])
