# Lote 33: lo que se ve en las fotos de Instagram de cada tienda (referencias NN = l33src/<slug>/NN.jpg).
# prods: (ref, descripción en inglés para la IA, nombre en la tienda). hero/banner/l1/l2: (ref o None, descripción).
# place: sitio reconocible de su ciudad para el hero. who: woman | man | none (producto solo).
S = {}

S['rosisima'] = dict(
    place='the medieval Castle of Almansa on its rocky hill in Almansa, Spain, seen from a sunny old-town square', who='woman',
    hero=('14', 'a camel and black leopard-print long wool coat over a dark outfit'),
    banner=('03', 'the inside of a bright fashion boutique: white built-in shelves with ceramic vases and plants, a vertical wooden slat wall, rails of autumn clothes, warm wooden floor, no people'),
    prods=[('15', 'a satin blouse with wide diagonal purple and rust-orange stripes, high neck with a bow and puffed sleeves', 'Blusa satinada de rayas'),
           ('17', 'a beige shaggy faux-fur jacket worn over a grey top and rust-red wide trousers', 'Chaqueta de pelo beige'),
           ('08', 'a brown and cream gingham-check midi shirt dress with long sleeves and a belt', 'Vestido camisero de cuadros'),
           ('10', 'a dark brown chunky knit jumper with brown and black tartan barrel-leg trousers and a brown belt', 'Pantalón de cuadros'),
           ('11', 'a black leather biker jacket over a grey top and slim grey jeans', 'Cazadora de cuero'),
           ('06', 'a grey oversized blazer with a rust top, a wide brown belt and light flared jeans', 'Blazer gris')],
    l1=('04', 'a burgundy fine-knit midi dress with a belt and long sleeves'),
    l2=('18', 'a grey and lilac tartan dress with a ruffled high neck'),
    cats=[('Vestidos', 'l1'), ('Chaquetas', 'p2'), ('Pantalones', 'p4')])

S['rocio-ortega'] = dict(
    place='a sunny whitewashed street in the old town of Sanlúcar de Barrameda, Spain, with the Guadalquivir light', who='woman',
    hero=('16', 'a flowing yellow maxi dress with a bold tropical floral print and a halter neck'),
    banner=('02', 'the inside of a colourful boutique with traditional patterned hydraulic floor tiles, wooden shelves full of handbags, hats, sunglasses and wax jackets, no people'),
    prods=[('08', 'a cropped tweed jacket with big brown fur cuffs and collar, worn with a zig-zag knit maxi skirt', 'Chaqueta con pelo'),
           ('10', 'a long-sleeved olive and gold printed satin maxi dress', 'Vestido largo satinado'),
           ('11', 'a long multicolour striped kaftan dress in purple, orange and green', 'Caftán de rayas'),
           ('18', 'a black and white striped halter maxi dress with a tiered skirt', 'Vestido de rayas'),
           ('14', 'a white folding hand fan with a natural wood frame, shown open', 'Abanico blanco'),
           ('09', 'a matching tartan blazer and long skirt set in grey and brown check', 'Conjunto de cuadros')],
    l1=('04', 'three luxurious fur stoles in lilac, brown and black, draped together'),
    l2=('17', 'leather clutch bags and belts in black, tan and croc-embossed brown with silver details, arranged on a wooden table'),
    cats=[('Vestidos', 'p2'), ('Pieles y abrigos', 'l1'), ('Bolsos', 'l2')])

S['molupita'] = dict(
    place='the Kursaal and the beach promenade of Gros in San Sebastián, Spain, on a bright day', who='woman',
    hero=('06', 'a black and white tartan cropped jacket with a matching skirt'),
    banner=('05', 'the inside of an elegant white fashion boutique with classic mouldings, rails of knitwear and coats, a striped shopping-bag sign, no people'),
    prods=[('04', 'a grey fine-knit midi dress with a pleated skirt and a bow at the neck', 'Vestido de punto plisado'),
           ('18', 'an argyle V-neck jumper in charcoal, grey and pink', 'Jersey de rombos'),
           ('10', 'a black knit off-shoulder top with a draped collar and a gold brooch', 'Jersey con broche'),
           ('17', 'a brown chiffon shirt with a tweed front panel and matching brown tweed shorts', 'Conjunto de tweed'),
           ('08', 'a grey knit jumper with black floral rope appliqué', 'Jersey de flores'),
           ('11', 'a grey ribbed turtleneck knit jumper with straight blue jeans', 'Jersey de canalé')],
    l1=('13', 'a metallic silver draped cowl-neck top with a black satin midi skirt, for an evening event'),
    l2=('09', 'a taupe wool coat with a round collar and buttons'),
    cats=[('Punto', 'p5'), ('Fiesta', 'l1'), ('Abrigos', 'l2')])

S['maria-antonia'] = dict(
    place='the Gothic cathedral of Burgos, Spain, seen from a sunny square', who='woman',
    hero=('06', 'a beige faux-fur jacket over a long beige jumpsuit with a wide brown belt and a grey beret'),
    banner=('11', 'the inside of a cosy boutique with patterned wallpaper, a red and green kilim rug, a light blue wooden table with folded knitwear, rails of colourful clothes and floor lamps, no people'),
    prods=[('04', 'a burgundy long cardigan over a burgundy and grey tartan maxi skirt', 'Falda de cuadros'),
           ('12', 'a grey argyle cardigan with a grey check midi skirt', 'Chaqueta de rombos'),
           ('07', 'a long striped knit cardigan in navy, teal and burgundy', 'Rebeca larga de rayas'),
           ('03', 'a black and white patchwork knit jacket with an orange scarf and black trousers', 'Chaqueta de punto'),
           ('09', 'a long burgundy and white jacquard knit cardigan over a burgundy dress', 'Rebeca de jacquard'),
           ('01', 'a red and green tartan umbrella with a wooden handle', 'Paraguas de cuadros')],
    l1=('05', 'a long brown knit coat with a light blue printed scarf and brown wide trousers'),
    l2=('10', 'a dark green blouse with a long patterned shawl and black trousers'),
    cats=[('Punto', 'p3'), ('Abrigos', 'l1'), ('Complementos', 'p6')])

S['carlos-pina-shop'] = dict(
    place='the medieval Castle of Almansa on its rocky hill in Almansa, Spain, seen from a street in the old town', who='man',
    hero=('17', 'a beige cotton field jacket over a dark green knit and blue jeans'),
    banner=('10', 'the inside of a men\'s clothing shop with red walls, wooden tables with folded shirts and jumpers, shelves of jeans and a London Underground style round sign without text, no people'),
    prods=[('08', 'a beige linen blazer with a white shirt and blue jeans', 'Americana beige'),
           ('14', 'a long beige quilted puffer coat with a hood', 'Plumífero largo'),
           ('16', 'a dark green quarter-zip knit jumper', 'Jersey de cremallera'),
           ('11', 'a white cotton shirt with a small round logo patch on the chest', 'Camisa blanca'),
           ('18', 'a brown quilted puffer jacket', 'Cazadora acolchada'),
           ('06', 'a navy blue polo shirt with beige chinos', 'Polo azul marino')],
    l1=('01', 'a navy zip jacket with grey trousers and white sneakers'),
    l2=('13', 'a cream knit jumper with blue jeans'),
    cats=[('Chaquetas', 'p2'), ('Camisas', 'p4'), ('Punto', 'l2')])

S['trendy'] = dict(
    place='the Gothic cathedral of Plasencia, Spain, with its stone portal and steps', who='woman',
    hero=('03', 'a long plum satin gown with thin straps'),
    banner=('04', 'the inside of a modern white fashion boutique with pendant lamps, a dark wood counter and rails of clothes, a glowing empty lightbox on the wall, no people'),
    prods=[('01', 'a teal blue wrap midi dress with sheer long sleeves and feather details at the shoulders', 'Vestido azul de invitada'),
           ('17', 'a red long fitted dress with one sleeve and a big black ruffle on the shoulder', 'Vestido rojo de fiesta'),
           ('13', 'a black leather military-style jacket with gold buttons and frogging', 'Chaqueta militar'),
           ('09', 'a brown leather aviator jacket with a shearling collar and brown wide trousers', 'Cazadora de borrego'),
           ('18', 'a cream waistcoat with double buttons over a brown satin maxi skirt', 'Chaleco y falda satinada'),
           ('05', 'a burgundy hobo handbag in leather and suede', 'Bolso de ante')],
    l1=('02', 'a men\'s mauve check three-piece suit with a pink waistcoat and burgundy tie (a male model)'),
    l2=('06', 'pointed dark brown and burgundy suede ankle boots'),
    cats=[('Fiesta', 'p2'), ('Hombre', 'l1'), ('Bolsos y botines', 'l2')])

S['king-s-road'] = dict(
    place='the Elogio del Horizonte concrete sculpture on the Cerro de Santa Catalina in Gijón, Spain, with the sea behind', who='woman',
    hero=('11', 'a dark green suede jacket with matching trousers, a dark shirt and a paisley neck scarf'),
    banner=('02', 'the inside of a characterful clothing shop with exposed whitewashed brick, wooden French windows, dried flower garlands and rails of coats and knitwear, no people'),
    prods=[('04', 'a tobacco-brown padded short jacket with dark brown trousers', 'Cazadora acolchada'),
           ('05', 'a long light-blue wool coat with a belt and a brown fur pocket detail', 'Abrigo azul cielo'),
           ('06', 'an oversized taupe suit: relaxed blazer and wide trousers', 'Traje oversize'),
           ('09', 'a burgundy chiffon slip maxi dress with thin straps', 'Vestido lencero'),
           ('10', 'a dark chocolate-brown shearling jacket with toggle fastenings', 'Chaqueta de borrego'),
           ('08', 'an olive-brown glossy leather trench coat with matching trousers', 'Gabardina de piel')],
    l1=('07', 'a long khaki waxed parka with an orange collar'),
    l2=('12', 'a cream short-sleeved knit top with a long black skirt and a small red bag'),
    cats=[('Abrigos', 'p2'), ('Chaquetas', 'l1'), ('Vestidos', 'p4')])

S['cunadas'] = dict(
    place='the Alcazaba of Antequera, Spain, with the Peña de los Enamorados on the horizon', who='woman',
    hero=('12', 'a camel suede western jacket and trousers with fringes and a silk neck scarf'),
    banner=('04', 'the inside of a glamorous boutique with deep red velvet curtains, a large gilded baroque mirror, a Persian rug and rails of clothes, no people'),
    prods=[('06', 'a burgundy suede jacket with a belt over a floral blouse and cream wide-leg trousers', 'Chaqueta de ante burdeos'),
           ('10', 'a leopard-print jacket over a white tee and wide light-blue jeans', 'Chaqueta de leopardo'),
           ('09', 'a grey wool short jacket and mini skirt set with brown knee boots', 'Conjunto gris'),
           ('05', 'a metallic grey satin blouse with a black leather skirt', 'Blusa satinada'),
           ('11', 'a long snake-print kimono coat over a white tee and black shorts', 'Kimono animal print'),
           ('08', 'a chocolate-brown fringed suede vest over a white shirt and cream trousers', 'Chaleco de flecos')],
    l1=('07', 'a brown fur gilet over a navy jumper and a tweed maxi skirt'),
    l2=('03', 'a long camel coat over a printed silk maxi skirt'),
    cats=[('Chaquetas', 'p1'), ('Conjuntos', 'p3'), ('Abrigos', 'l2')])

S['cache-vila'] = dict(hx='94%', 
    place='the white sail-shaped Auditorio de Tenerife by the sea in Santa Cruz de Tenerife, Spain', who='woman',
    hero=('09', 'a brown suede jacket over a yellow knit jumper with a silk scarf and corduroy trousers'),
    banner=('12', 'the inside of a bright minimalist boutique with white walls, rails of autumn clothes, woven straw hats hanging on the wall and a white counter, no people'),
    prods=[('01', 'an oversized argyle knit jumper in cream and dark brown', 'Jersey de rombos'),
           ('04', 'a burgundy fine-knit jumper with a scalloped hem', 'Jersey burdeos'),
           ('11', 'a black and white gingham shirt with dark flared jeans and a belt', 'Camisa de cuadro vichy'),
           ('10', 'a black long-sleeved belted midi shirt dress', 'Vestido camisero negro'),
           ('06', 'a white jumper with black polka dots and light wide-leg jeans', 'Jersey de topos'),
           ('05', 'dark brown suede penny loafers', 'Mocasines de ante')],
    l1=('02', 'a denim shirt with a tartan wrap skirt and a camel suede coat'),
    l2=('08', 'a brown leather shoulder bag with beige suede ankle boots and a striped knit'),
    cats=[('Punto', 'p1'), ('Vestidos y camisas', 'p4'), ('Bolsos y calzado', 'l2')])

S['lluna-de-drap'] = dict(
    place='La Seu Vella cathedral on its hill above Lleida, Spain', who='woman',
    hero=('04', 'a long beige teddy coat with white wide trousers'),
    banner=('06', 'the inside of a bright clothing shop with white walls, ceiling spotlights and long rails of black and cream coats and puffer jackets, no people'),
    prods=[('05', 'a navy quilted coat with a hood', 'Abrigo acolchado'),
           ('02', 'a mustard yellow cardigan over a light blue shirt with olive trousers', 'Rebeca mostaza'),
           ('08', 'a shirt with a bold multicolour check print in blue, red, yellow and white', 'Camisa de cuadros'),
           ('12', 'a navy asymmetric peplum tunic with matching navy trousers', 'Conjunto azul marino'),
           ('11', 'a dark green check wool coat with grey wide trousers', 'Abrigo de cuadros'),
           ('07', 'a long black and white geometric print scarf with a black leather jacket', 'Fular geométrico')],
    l1=('03', 'a black jacket over a printed tee with black wide palazzo trousers'),
    l2=('09', 'a silver metallic jacket over a cream top'),
    cats=[('Abrigos', 'p1'), ('Camisas', 'p3'), ('Complementos', 'p6')])

# ---------------- joyería (hero partido: bodegón; who='none' salvo l1/l2 puestas)
S['madrid-oro-la-guaira'] = dict(
    place='Madrid', who='none', theme=dict(acc='#B8892F'),
    hero=('06', 'a heavy 18k yellow gold crown ring with a red stone, next to a gold Cuban link chain'),
    banner=('03', 'the inside of a luxurious jewellery shop with black marble walls with gold veins, glowing glass showcases full of gold chains and rings, no people'),
    prods=[('06', 'a chunky 18k yellow gold crown-shaped ring set with a red stone and small white stones', 'Anillo corona'),
           ('09', 'a polished 18k yellow gold nameplate ring with a cursive name', 'Anillo con nombre'),
           ('11', 'a round blue evil-eye pendant framed with small white stones on a gold rope chain', 'Colgante ojo turco'),
           ('12', 'a thick 18k yellow gold Cuban link chain necklace', 'Cadena barbada'),
           ('09', 'a men\'s 18k yellow gold signet ring with a small diamond, rectangular top', 'Sello de caballero'),
           ('04', 'a fine 18k yellow gold rope chain necklace', 'Cordón de oro')],
    l1=('11', 'a man wearing a gold rope chain with a blue evil-eye pendant over a black t-shirt, cropped at the chin'),
    l2=('04', 'a hand wearing several chunky 18k gold rings and a gold chain bracelet, close up'),
    cats=[('Anillos', 'p1'), ('Cadenas', 'p4'), ('Colgantes', 'p3')])

S['little-things'] = dict(
    place='Oviedo', who='none', theme=dict(acc='#B5482E', bg='#FBF5EE'),
    hero=('01', 'a statement necklace of twisted blue rope with a long rust-orange fringe and a brown pompom, with round matching earrings'),
    banner=('02', 'the inside of a cheerful accessories shop with a pastel mint wooden cabinet, plants and a warm gold neon-style sign without readable text, no people'),
    prods=[('01', 'a statement necklace of twisted blue rope with a long rust-orange fringe and a small brown pompom', 'Collar de flecos'),
           ('07', 'a chunky bracelet with a large gold ring clasp and charms: a yellow star, a red drop and green beads', 'Pulsera de charms'),
           ('16', 'a burgundy rope necklace with a big baroque pearl and a gold stirrup pendant', 'Collar de perla y estribo'),
           ('12', 'a black cord phone strap with colourful resin beads in orange, white and burgundy', 'Colgante para el móvil'),
           ('15', 'a gold chain bracelet with a white heart, a coin medallion and a pink charm', 'Pulsera de medalla'),
           ('03', 'a black leather tote bag with a small hand-drawn family illustration embroidered in gold thread', 'Bolso personalizado')],
    l1=('05', 'a woman in a white tee and a retro orange-and-blue flower print jacket wearing a colourful beaded necklace with gems, cropped at the lips'),
    l2=('17', 'a woman in a white tee and khaki jacket wearing a leather cord necklace with a round tortoiseshell pendant, cropped at the lips'),
    cats=[('Collares', 'l1'), ('Pulseras', 'p2'), ('Bolsos', 'p6')])

S['joyeria-coca'] = dict(
    place='Lora del Río', who='none',
    hero=('08', 'yellow gold Virgin medals with mother-of-pearl centres and filigree frames'),
    banner=('16', 'the inside of a classic jewellery shop with wooden showcases and white display trays of necklaces, rings and earrings, warm light, no people'),
    prods=[('08', 'a yellow gold oval religious medal with a mother-of-pearl centre and an ornate filigree frame', 'Medalla de la Virgen'),
           ('03', 'stud earrings with an emerald, a sapphire and a ruby each surrounded by small white stones', 'Pendientes de piedras'),
           ('05', 'beaded gemstone necklaces in ruby red, sapphire blue and emerald green with small gold pendants', 'Collar de piedras'),
           ('15', 'a yellow gold necklace of small round coin links with a matching bangle', 'Collar de monedas'),
           ('09', 'a silver vertical bar pendant on a fine silver chain', 'Colgante de barra'),
           ('04', 'a selection of delicate gold and silver rings with small stones', 'Anillos finos')],
    l1=('14', 'a smiling woman\'s wrist wearing thin gold bracelets, cropped, no face'),
    l2=('18', 'a woman wearing a fine necklace of tiny multicolour beads with a green drop pendant, cropped at the lips'),
    cats=[('Medallas', 'p1'), ('Pendientes', 'p2'), ('Collares', 'l2')])

S['maeve-sevilla'] = dict(
    place='Sevilla', who='none', theme=dict(acc='#9C2F3A'),
    hero=('02', 'colourful gold drop earrings with turquoise, coral and amethyst stones'),
    banner=('07', 'a jewellery shop window with necklace busts, statement necklaces and rows of colourful leather cuffs on a blue table, no people'),
    prods=[('02', 'gold statement drop earrings with an oval turquoise stone and a coral teardrop', 'Pendientes de piedra'),
           ('09', 'long white bone bead necklaces and a white carved flamenco hair comb', 'Collar de hueso y peina'),
           ('12', 'a clutch bag covered in colourful mirrored mosaic glass stones', 'Bolso de mosaico'),
           ('10', 'folded embroidered silk Manila shawls in coral, fuchsia, ivory and black', 'Mantón bordado'),
           ('04', 'large ivory resin drop earrings', 'Pendientes de lágrima'),
           ('11', 'a tiny red coral cross pendant on a fine gold chain', 'Cruz de coral')],
    l1=('01', 'a woman in a brown turtleneck wearing a red coral cross on a red cord, cropped at the lips'),
    l2=('06', 'two soft leather tote bags in black and navy hanging from a shoulder'),
    cats=[('Pendientes', 'p1'), ('Mantones', 'p4'), ('Bolsos', 'p3')])

S['makalo'] = dict(
    place='Caravaca de la Cruz', who='none', theme=dict(acc='#B07A3E'),
    hero=('03', 'a gold leaf hair headpiece with crystals on a low chignon'),
    banner=('05', 'the inside of a bright boutique of hats, headpieces and accessories with lilac walls and shelves of hats on stands, no people'),
    prods=[('03', 'a gold leaf hair vine headpiece with small crystals, worn on a low chignon, seen from behind', 'Tocado de hojas doradas'),
           ('12', 'a delicate silver bridal tiara of leaves and pearls', 'Tiara de novia'),
           ('04', 'gold statement earrings: a curved crescent, a sun with a pearl and a leaf with a pearl drop', 'Pendientes dorados'),
           ('11', 'long white floral statement earrings with pearls', 'Pendientes de flor'),
           ('10', 'a black birdcage veil fascinator', 'Tocado con redecilla'),
           ('02', 'a gold hair comb of leaves and crystals', 'Peina dorada')],
    l1=('09', 'a bride in a long silver sequinned gown with a sheer embellished cape on a staircase, seen from a distance'),
    l2=('08', 'a woman in a burgundy strapless peplum gown with a matching scarf, at an event, seen from a distance'),
    cats=[('Tocados', 'p1'), ('Novias', 'l1'), ('Pendientes', 'p3')])

S['carlos-joyeria'] = dict(
    place='Gijón', who='none', theme=dict(acc='#1F3C78'),
    hero=('10', 'a round blue sapphire ring with a diamond halo in white gold'),
    banner=('03', 'the inside of an elegant jewellery shop window with grey velvet necklace busts and rows of rings on dark display stands, no people'),
    prods=[('01', 'a yellow gold cocktail ring with three stones: a blue cabochon sapphire, a purple square amethyst and a light blue topaz', 'Anillo de tres piedras'),
           ('02', 'a white gold ring with a square brown smoky quartz and a pavé band', 'Anillo de cuarzo'),
           ('10', 'a white gold ring with a round blue sapphire surrounded by a diamond halo', 'Anillo de zafiro'),
           ('11', 'a yellow gold ring with three round emeralds and small diamonds', 'Anillo de esmeraldas'),
           ('09', 'gold link earrings made of two textured oval links with pavé', 'Pendientes de eslabón'),
           ('06', 'a yellow gold toi-et-moi ring with two hexagonal sapphires framed in diamonds', 'Anillo tú y yo')],
    l1=('05', 'two stacked thin gold rings, one with an emerald and one with a ruby, on a sage-green velvet box'),
    l2=('07', 'a woman\'s hand wearing a small sapphire halo ring, elegant, close up'),
    cats=[('Anillos', 'p1'), ('Pendientes', 'p5'), ('Piedras de color', 'l1')])

S['joieria-torres'] = dict(
    place='Lleida', who='none', theme=dict(acc='#2E2A26'),
    hero=('05', 'an oval emerald ring with a diamond halo in yellow gold'),
    banner=('02', 'an elegant woman in a black blazer holding a small black jewellery gift bag tied with a white satin bow, cropped at the chest, no text on the bag'),
    prods=[('05', 'a yellow gold ring with an oval emerald surrounded by small diamonds', 'Anillo de esmeralda'),
           ('01', 'long drop earrings with a dark garnet stone and small diamonds', 'Pendientes de granate'),
           ('03', 'a delicate engagement ring with a round diamond solitaire', 'Solitario de compromiso'),
           ('12', 'a pair of classic yellow gold wedding bands', 'Alianzas de boda'),
           ('11', 'a stack of thin gold rings with a small emerald', 'Anillos apilables'),
           ('02', 'a thin gold bracelet and a fine ring with a small stone', 'Pulsera fina')],
    l1=('04', 'a bride\'s hand with an engagement ring resting on a groom\'s dark suit sleeve, white veil, close up, no faces'),
    l2=('09', 'a bride wearing small diamond earrings, soft light, seen from the side, face mostly turned away'),
    cats=[('Compromiso', 'p3'), ('Alianzas', 'p4'), ('Pendientes', 'p2')])

S['joyeria-benito-hidalgo'] = dict(
    place='Sabadell', who='none', theme=dict(acc='#1E3A5F'),
    hero=('12', 'a steel diver watch with a navy blue dial on a sunny Mediterranean table with lemons, no brand names'),
    banner=('08', 'the inside of a modern watch and jewellery shop with dark wood panels, framed pictures and a showcase counter, no brand names or logos, no people'),
    prods=[('02', 'a stack of four white gold eternity rings set with round diamonds', 'Alianzas de diamantes'),
           ('05', 'a steel chronograph watch with a blue dial and an integrated steel bracelet, no brand name or logo on the dial', 'Reloj cronógrafo azul'),
           ('09', 'a steel diver watch with a black dial and a turquoise rubber strap, no brand name or logo', 'Reloj de buceo turquesa'),
           ('10', 'a steel watch with a mint green dial and a steel bracelet, no brand name or logo', 'Reloj esfera menta'),
           ('12', 'a steel diver watch with a navy blue dial and a steel bracelet, no brand name or logo', 'Reloj de buceo azul'),
           ('01', 'a brown leather zip watch case', 'Estuche de piel')],
    l1=('11', 'a hand on the wheel of a classic convertible wearing a small steel watch, sunny, no brand names'),
    l2=('03', 'a woman in a beige trench coat by a stone fountain wearing a slim gold watch, cropped, no face'),
    cats=[('Relojes', 'p2'), ('Anillos', 'p1'), ('Regalo', 'p6')])

S['joyeria-matiz'] = dict(
    place='Santander', who='none', theme=dict(acc='#A27A3A'),
    hero=('01', 'twisted gold and silver cable bangles with diamond rondelles'),
    banner=('07', 'the inside of a bright jewellery shop with white walls, glass showcases and a black and red accent wall, no people'),
    prods=[('01', 'flexible cable bangles in yellow gold and white gold with pavé diamond rondelles', 'Brazaletes de cable'),
           ('02', 'a large sculpted gold petal earring', 'Pendiente escultura'),
           ('11', 'gold wire flower earrings with a short necklace of white beads and a gold flower', 'Pendientes de flor'),
           ('05', 'macramé cord bracelets in burgundy, brown and navy with a silver religious medal', 'Pulsera de medalla'),
           ('10', 'a gold hoop earring with a pearl and a gold bead necklace with pearl drops', 'Collar de perlas'),
           ('03', 'a gold spiked ear cuff with a matching open ring', 'Ear cuff dorado')],
    l1=('09', 'a laughing woman in a red satin halter top wearing a stack of colourful beaded bracelets and gold rings, seen from a distance'),
    l2=('04', 'a silver medal pendant on a navy cord over a white shirt with embroidered flowers, cropped at the chin'),
    cats=[('Pulseras', 'p1'), ('Pendientes', 'p2'), ('Collares', 'p5')])

S['mr-gold-almeria'] = dict(
    place='Almería', who='none', theme=dict(acc='#B58A2C'),
    hero=('11', 'a heavy yellow gold bangle with two facing lion heads'),
    banner=('05', 'a jewellery shop showcase with layered yellow gold chains on a glass shelf, warm light, no people'),
    prods=[('11', 'a heavy polished yellow gold bangle ending in two facing lion heads', 'Brazalete de leones'),
           ('12', 'a polished yellow gold bangle ending in two facing horse heads with black enamel manes', 'Brazalete de caballos'),
           ('06', 'a long thick yellow gold rope chain', 'Cordón de oro'),
           ('08', 'a thick yellow gold anchor-style link chain with a box clasp', 'Cadena de eslabones'),
           ('04', 'a men\'s yellow gold signet ring with a black onyx top', 'Sello con ónix'),
           ('09', 'a thin smooth yellow gold bangle', 'Esclava lisa')],
    l1=('05', 'layered yellow gold Figaro chains worn on a tanned neck with a white shirt, cropped at the chin'),
    l2=('10', 'a woman\'s wrist wearing a gold animal-head bangle, close up'),
    cats=[('Brazaletes', 'p1'), ('Cadenas', 'p3'), ('Anillos', 'p5')])

# ---------------- cosmética y perfumería (marcas ajenas: sin nombres ni logos)
S['intenso-fragancias'] = dict(
    place='Torremolinos', who='none', theme=dict(acc='#B5651D'),
    hero=('04', 'a tall rectangular glass perfume bottle with amber juice, a black cap and a black label with a gold S-shaped emblem, on warm amber stone with autumn light'),
    banner=('03', 'a perfume bar with rows of large glass dispenser jars with metal taps and reed diffusers on wooden shelves, warm light, no people'),
    prods=[('04', 'a tall rectangular glass perfume bottle with amber juice, a black cap and a black label with a gold S-shaped emblem', 'Extracto Ambre Levant'),
           ('05', 'a tall rectangular glass perfume bottle with golden juice, black cap and a cream label with a black S-shaped emblem, with saffron and passion fruit around', 'Extracto Oud Maracuyá'),
           ('06', 'a glass reed diffuser bottle with a cream label and wooden sticks, next to vanilla flowers', 'Mikado Bianco Latte'),
           ('11', 'clear plastic home fragrance spray bottles with white labels and a black S-shaped emblem', 'Ambientador en spray'),
           ('07', 'a rectangular perfume bottle with golden juice and a black label with an S emblem and the number 7008, with lemon slices', 'Perfume 7008'),
           ('09', 'two rectangular perfume bottles with a black label and a gold S emblem on a wooden log in an autumn forest', 'Perfume de bolsillo')],
    l1=('03', 'a close up of large glass perfume dispenser jars with metal taps and white labels'),
    l2=('12', 'a small amber reed diffuser bottle with an S emblem, beside a halved orange on driftwood'),
    cats=[('Perfumes', 'p1'), ('Hogar', 'p3'), ('Extractos', 'p2')])

S['la-marquesa-perfumeria'] = dict(
    place='Almería', who='none', theme=dict(acc='#B3262B', bg='#F5F1EC'),
    hero=('06', 'a square perfume bottle with a red-to-amber gradient and a black round cap, on black stone with smoke, no brand names'),
    banner=('05', 'the inside of a modern perfume shop with black and white shelves full of perfume boxes and bottles, dramatic spotlights, no people'),
    prods=[('06', 'a square glass perfume bottle with a deep red-to-amber gradient and a black cap, no brand name or logo', 'Perfume rojo intenso'),
           ('04', 'a dark red rectangular perfume bottle with an embossed geometric pattern, no brand name', 'Perfume oriental rojo'),
           ('07', 'an ornate teal and gold perfume bottle with an amber juice, no brand name', 'Perfume ámbar y azahar'),
           ('12', 'a silver speckled rectangular perfume bottle with a black cap, no brand name', 'Perfume plata'),
           ('08', 'a black perfume box with an iridescent holographic panel, no readable text', 'Estuche de regalo'),
           ('05', 'three oriental perfume bottles in black, gold and white on a glossy black surface, no brand names', 'Perfumes árabes')],
    l1=('03', 'rows of oriental perfume boxes on white shelves, close up, no readable brand names'),
    l2=('10', 'a man in a white tee spraying perfume on his wrist, soft light, face cropped'),
    cats=[('Perfumes árabes', 'p6'), ('De hombre', 'p1'), ('Regalo', 'p5')])

S['perfumeria-hebe'] = dict(
    place='Antequera', who='none', theme=dict(acc='#B0546A'),
    hero=('05', 'a luxurious composition of a clear perfume bottle, a black lipstick and a cream skincare jar on pale marble, soft pink light, no brand names'),
    banner=('01', 'the inside of an elegant perfumery with glass shelves full of perfumes and skincare, warm lighting and framed beauty posters, no people, no brand names'),
    prods=[('05', 'a clear faceted glass perfume bottle with a gold cap, no brand name', 'Eau de parfum'),
           ('06', 'a row of skincare supplement jars in pastel colours on white marble, no readable brand names', 'Complementos de belleza'),
           ('07', 'a selection of luxury lipsticks and a mascara in black and gold cases, no brand names', 'Labiales'),
           ('08', 'a black skincare night routine set: serum bottle and cream jar with a pink pouch, no brand names', 'Rutina de noche'),
           ('03', 'a bright pink advent calendar box with gold confetti, no brand name', 'Calendario de adviento'),
           ('04', 'a pink tube of lip gloss and a mint gift box, no brand names', 'Gloss')],
    l1=('11', 'a makeup counter with mirrors and lights in a perfumery, no people, no brand names'),
    l2=('09', 'hands unwrapping a pink makeup bag with skincare samples, no brand names'),
    cats=[('Perfumes', 'p1'), ('Tratamiento', 'p4'), ('Maquillaje', 'p3')])

S['perfumoon'] = dict(
    place='Alicante', who='none', theme=dict(acc='#7A4FA0', bg='#F5F1F7'),
    hero=('04', 'an ornate lilac and gold square perfume bottle on a white marble pedestal with purple light, no brand names'),
    banner=('01', 'the inside of a bright white perfume shop with backlit niches holding perfume bottles, soft lighting, no people'),
    prods=[('04', 'an ornate lilac square perfume bottle with gold geometric decoration and a white cap, no brand name', 'Perfume lila y oro'),
           ('08', 'a tall sage-green column-shaped perfume bottle with an antique bronze cap, no brand name', 'Perfume columna verde'),
           ('09', 'a playful pink perfume bottle shaped like a cupcake with a strawberry on top, no brand name', 'Perfume gourmand'),
           ('10', 'a perfume bottle with a gold coiled snake wrapped around a gold cap, no brand name', 'Perfume serpiente'),
           ('11', 'a tall black rectangular perfume bottle with a black cap, no brand name', 'Perfume negro'),
           ('12', 'a heavy faceted crystal perfume bottle with turquoise juice, no brand name', 'Perfume cristal turquesa')],
    l1=('06', 'a row of five colourful oriental perfume bottles on marble, no brand names'),
    l2=('07', 'two perfume bottles side by side, one pale green and one black, on a white surface, no brand names'),
    cats=[('De mujer', 'p1'), ('De hombre', 'p5'), ('Árabes', 'l1')])

S['amusko'] = dict(
    place='A Coruña', who='none', theme=dict(acc='#E2673A'),
    hero=('06', 'a rectangular glass perfume bottle with amber juice and a black cap, held up against a light grey wall'),
    banner=('05', 'the inside of a minimal light grey perfume lab shop with white shelves of perfume bottles and a white counter, no people'),
    prods=[('06', 'a rectangular glass perfume bottle with amber juice and a black cap with a simple handwritten-style label', 'Perfume amaderado'),
           ('05', 'a white shelf with rows of small perfume bottles in different colours', 'Perfumes de autor'),
           ('09', 'a bright orange paper shopping bag with white rope handles and a gift box', 'Bolsa de regalo'),
           ('04', 'a small travel perfume atomiser and a paper scent strip', 'Formato viaje'),
           ('11', 'a set of three perfume tester strips fanned out on a white table', 'Prueba de olor'),
           ('08', 'a glass perfume bottle with pale pink juice and a gold cap', 'Perfume floral')],
    l1=(None, 'a cosmetic flat lay of a face cream jar, a serum dropper and a body lotion in neutral packaging, no brand names'),
    l2=(None, 'a home fragrance set: a reed diffuser and a scented candle on a linen cloth, no brand names'),
    cats=[('Perfumes', 'p1'), ('Cosmética', 'l1'), ('Hogar', 'l2')])

S['perfumeria-paris'] = dict(
    place='Santander', who='none', theme=dict(acc='#8E1F2F'),
    hero=('08', 'a pink-tinted glass perfume bottle held in a hand above a red dress on green grass, no brand names'),
    banner=('02', 'the inside of a traditional perfumery with wooden shelves packed with perfumes and cosmetics, warm light, no people, no brand names'),
    prods=[('05', 'a snake-print handbag with black knotted rope handles and a dangling charm, no logo', 'Bolso serpiente'),
           ('06', 'a soft taupe faux-fur shoulder bag, no logo', 'Bolso de pelo'),
           ('08', 'a pink-tinted glass perfume bottle with a silver cap, no brand name', 'Perfume rosa'),
           ('02', 'a navy and gold perfume gift box with a laurel pattern, no brand name', 'Estuche de regalo azul'),
           ('07', 'a leopard-print handbag with a top handle, no logo', 'Bolso de leopardo'),
           ('03', 'a deep red perfume gift box tied with a red ribbon, no brand name', 'Estuche de regalo rojo')],
    l1=('10', 'a smiling woman in a red dress holding a small perfume bottle to her chest, eyes closed, sunny'),
    l2=('04', 'silver and white perfume gift boxes stacked in a perfumery, no brand names'),
    cats=[('Perfumes', 'p3'), ('Estuches', 'p4'), ('Bolsos', 'p1')])

S['madina-perfumes'] = dict(
    place='Pamplona', who='none', theme=dict(acc='#9A6B2F'),
    hero=('06', 'a cream and silver oriental perfume bottle on fresh white snow, no brand names'),
    banner=('12', 'the inside of a perfume shop with tall white shelves packed with colourful oriental perfume boxes and bottles, wooden floor, no people'),
    prods=[('06', 'a cream perfume bottle with a silver band and a cream cap, no brand name', 'Perfume vainilla'),
           ('01', 'a white and silver cylindrical perfume bottle with a chrome cap, no brand name', 'Perfume blanco'),
           ('05', 'a perfume bottle with a clock-like engraved silver face, no brand name', 'Perfume reloj'),
           ('07', 'a faceted amber perfume bottle with a peach box, no brand name', 'Perfume ámbar'),
           ('09', 'a white rectangular perfume bottle with a gold label frame, no brand name', 'Perfume cedro blanco'),
           ('04', 'a black sculpted perfume bottle shaped like a torso, no brand name', 'Perfume negro')],
    l1=('02', 'tall shelves packed with colourful oriental perfume boxes, close up, no readable brand names'),
    l2=('11', 'a hand opening a bright yellow perfume box, no readable brand name'),
    cats=[('De mujer', 'p1'), ('De hombre', 'p6'), ('Novedades', 'p4')])

S['rosa-rosae'] = dict(
    place='Olmedo', who='none', theme=dict(acc='#B5677A'),
    hero=('08', 'a chunky coral bead statement necklace and turquoise resin pieces on a raw linen table'),
    banner=('06', 'the inside of a bright drugstore perfumery with white shelves full of colourful colognes, cosmetics and gifts, no people, no brand names'),
    prods=[('08', 'a multi-strand coral-red bead statement necklace', 'Collar de coral'),
           ('06', 'four tall cologne bottles in orange, green, blue and pink, no brand names', 'Colonias de colores'),
           ('12', 'a silver necklace with a tiny heart pendant on a white card in a gift box', 'Collar de corazón'),
           ('04', 'sun cream bottles and tubes in blue and white, no brand names', 'Protección solar'),
           ('09', 'a jar of rich body butter with an orange lid, no brand name', 'Manteca corporal'),
           ('05', 'a shelf of small cologne bottles in pastel colours, no brand names', 'Colonias de verano')],
    l1=('01', 'a shelf of elegant cologne bottles in amber and gold, no brand names'),
    l2=('08', 'colourful bead bracelets and turquoise resin earrings on a wooden board'),
    cats=[('Perfumes', 'p2'), ('Bisutería', 'p1'), ('Cuidado', 'p5')])

S['urban-fragance'] = dict(
    place='Villena', who='none', theme=dict(acc='#3E3A36', bg='#F4F1EC'),
    hero=('03', 'a minimalist round glass perfume bottle with a black cap and a white typewriter-style label on a slice of wood'),
    banner=('11', 'the inside of a minimalist perfume shop with long white walls of wooden shelves holding hundreds of identical perfume bottles, no people'),
    prods=[('03', 'a round glass perfume bottle with a black cap and a white minimalist label', 'Perfume de autor'),
           ('06', 'two kraft cardboard perfume boxes with a white label and a red felt heart', 'Caja de regalo'),
           ('09', 'a Christmas set: a reed diffuser, a room spray and three small perfume bottles in amber, gold and white', 'Pack de Navidad'),
           ('04', 'a glass bottle being refilled from a tap with amber perfume', 'Recarga de perfume'),
           ('05', 'a small perfume bottle and its kraft box on a wooden table', 'Perfume y estuche'),
           ('09', 'a teal glass reed diffuser with wooden sticks', 'Mikado')],
    l1=('07', 'rows of identical minimalist perfume bottles on wooden shelves, close up'),
    l2=('01', 'two people smelling scent strips at a wooden counter in a bright perfume shop, seen from behind'),
    cats=[('Perfumes', 'p1'), ('Regalo', 'p2'), ('Hogar', 'p6')])

# ---------------- sneakers y calzado
S['dewe-almeria'] = dict(
    place='the Cable Inglés iron pier in Almería, Spain, at sunset', who='man',
    hero=('03', 'a beige workwear jacket over a white tee, brown wide trousers and grey retro running sneakers, no logos'),
    banner=('04', 'the inside of a modern sneaker shop with wooden wall shelves of sneakers, a brown leather sofa and a concrete floor, no people, no logos'),
    prods=[('05', 'a cream suede low sneaker with brown speckles, dark green stripes and a gum sole, no logos or brand names', 'Zapatilla terrace'),
           ('04', 'a grey and silver chunky retro running sneaker, no logos', 'Runner gris'),
           ('01', 'a red chunky knit turtleneck jumper with a cream chest band, no text', 'Jersey de cuello alto'),
           ('03', 'a beige cotton workwear jacket', 'Chaqueta workwear'),
           ('08', 'a dark green knit cardigan with white trims, no logos', 'Cárdigan verde'),
           ('01', 'beige and burgundy hiking boots with red laces, no logos', 'Bota de montaña')],
    l1=('03', 'three young men walking in a city street in denim, black and beige jackets, caps and brown trousers, no logos'),
    l2=('09', 'a man in a yellow knit and a woman in a white jacket with yellow striped trousers sitting on a classic car in the desert, no logos'),
    cats=[('Zapatillas', 'p1'), ('Ropa', 'p4'), ('Novedades', 'l1')])

S['23-sneakers'] = dict(
    place='the Plaza de los Fueros arcades in Tudela, Spain', who='man',
    hero=('02', 'an oversized graphic tee, light ripped jeans, a black trucker cap and bright red sneakers, no logos'),
    banner=('07', 'the inside of a streetwear shop with an LED hexagon ceiling, a wall of sneakers on floating shelves, a pool table and caps covering the floor, no people, no logos'),
    prods=[('09', 'a red suede and black trucker cap with white embroidered gothic lettering on the front', 'Gorra roja bordada'),
           ('12', 'a green and white trucker cap with dark green gothic embroidered lettering', 'Gorra verde bordada'),
           ('11', 'a pink suede trucker cap with pink gothic embroidered lettering', 'Gorra rosa bordada'),
           ('03', 'a pale yellow suede high-top basketball sneaker, no logos', 'Zapatilla amarilla'),
           ('03', 'a neon green and black high-top basketball sneaker, no logos', 'Zapatilla verde neón'),
           ('10', 'a white and black trucker cap with a red star-pattern brim and red gothic embroidery', 'Gorra de estrellas')],
    l1=('01', 'a guy in a white tracksuit with a black crossbody bag next to a table stacked with fitted caps, no logos'),
    l2=('05', 'a woman seen from behind in a yellow tee and camo trousers wearing a black cap, in front of a sneaker wall, no logos'),
    cats=[('Gorras', 'p1'), ('Zapatillas', 'p4'), ('Streetwear', 'l1')])

S['byb-multimarca'] = dict(
    place='the Alhambra seen from the Mirador de San Nicolás in Granada, Spain', who='man',
    hero=('10', 'a black jacket with an all-over white print, black trousers and black leather sneakers, no logos or text'),
    banner=('11', 'the inside of a menswear shop with rails of colourful t-shirts and hoodies, glossy floor, no people, no logos'),
    prods=[('02', 'a burgundy hoodie with grey trousers, no logos or text', 'Sudadera burdeos'),
           ('13', 'a dark green tracksuit with blue leaf prints on the sleeves and legs, no text', 'Chándal verde'),
           ('09', 'a sage grey hooded tracksuit, no text', 'Chándal gris salvia'),
           ('05', 'chunky white leather sneakers, no logos or text', 'Zapatilla blanca'),
           ('06', 'a black puffer jacket with a white all-over typographic pattern, no readable words', 'Plumífero estampado'),
           ('14', 'a black sneaker with a mesh upper and a transparent air sole, no logos', 'Zapatilla negra')],
    l1=('03', 'a man in a navy puffer vest and navy tracksuit in a shop, face hidden behind a phone, no logos'),
    l2=('16', 'grey cargo jogger trousers with white sneakers, close up of the legs, no logos'),
    cats=[('Chándales', 'p2'), ('Sudaderas', 'p1'), ('Zapatillas', 'p4')])

S['calzados-carrillo'] = dict(
    place='a sunny pedestrian street with orange trees in Atarfe, Granada, Spain, with Sierra Nevada far away', who='woman', light=True,
    eyebrow='Calzado para toda la familia', h1='Tus zapatos,<br>a un clic.',
    hero=('12', 'burgundy leather ankle boots with a block heel, worn with jeans'),
    banner=('04', 'the inside of a family shoe shop with white walls, shelves of shoes and handbags and a woven jute rug, no people, no logos'),
    prods=[('13', 'black leather pointed ankle boots with a slim kitten heel, no logos', 'Botín de tacón'),
           ('12', 'burgundy leather ankle boots with a block heel, no logos', 'Botín burdeos'),
           ('09', 'beige suede short sheepskin-lined boots, no logos', 'Bota australiana'),
           ('10', 'dark brown leather lace-up men\'s derby shoes, no logos', 'Zapato de piel de hombre'),
           ('14', 'retro sneakers in white, beige and black suede, no logos', 'Zapatilla retro'),
           ('06', 'a bronze leather wedge ankle boot and a brown metallic backpack, no logos', 'Botín de cuña')],
    l1=('08', 'dark brown and black suede ankle boots with a block heel on a jute rug, no logos'),
    l2=('07', 'burgundy and grey suede sneakers on a white shelf, no logos'),
    cats=[('Botines', 'p1'), ('Hombre', 'p4'), ('Zapatillas', 'p5')])

# ---------------- calzado (zapaterías: tienda clara, niche calzado)
S['zapateria-passos'] = dict(
    place='a stone street with slate roofs in the old town of Cacabelos, León, Spain', who='woman', light=True,
    hero=('10', 'cognac suede pointed western ankle boots with small studs, worn with straight jeans and a black cardigan'),
    banner=('05', 'the inside of a modern shoe shop with glass display tables, shelves of boots and loafers and warm light, no people, no logos'),
    prods=[('01', 'tan suede lace-up moccasin shoes with a chunky black lug sole, no logos', 'Mocasín de cordones'),
           ('10', 'cognac suede pointed western ankle boots with tiny studs on the toe, no logos', 'Botín cowboy de ante'),
           ('12', 'burgundy patent leather derby shoes with a zebra-print calf hair panel and a thick sole, no logos', 'Blucher de cebra'),
           ('04', 'black leather pointed cowboy boots with stitching, mid-calf, no logos', 'Bota cowboy negra'),
           ('14', 'camel suede lace-up winter boots lined with shearling, no logos', 'Bota con borrego'),
           ('15', 'navy suede sock ankle boots with a dark green croc-embossed toe cap and a buckle, no logos', 'Botín bicolor')],
    l1=('16', 'brown leather ankle boots with a long front gold zip, no logos'),
    l2=('17', 'dark brown suede boat shoes with red rope laces and a thick gum sole, no logos'),
    cats=[('Botines', 'p2'), ('Mocasines', 'p1'), ('Botas', 'p4')])

S['soul-feet'] = dict(
    place='the seafront promenade of Benicàssim, Castellón, Spain, with palm trees', who='woman', light=True,
    eyebrow='Barefoot y calzado respetuoso', h1='Pisa libre.<br>Pisa bonito.',
    hero=('04', 'brown suede barefoot sneakers with a thin flexible gum sole, worn with cropped light jeans'),
    banner=(None, 'the inside of a warm small shoe shop with light wooden shelves of barefoot shoes and boots, a round rug and plants, no people, no logos'),
    prods=[('04', 'brown suede minimalist barefoot sneakers with a wide toe box and a thin gum sole, no logos', 'Barefoot de ante'),
           ('11', 'navy leather barefoot sneakers with light blue laces and a thin gum sole, no logos', 'Barefoot azul marino'),
           ('12', 'dark brown leather tall barefoot boots with a flat flexible sole, no logos', 'Bota alta barefoot'),
           ('01', 'a tan leather handbag with a sculpted tulip-shaped top and two short handles', 'Bolso tulipán'),
           ('09', 'retro barefoot sneakers in brown suede with green stripes and in red suede with cream stripes, no logos', 'Zapatilla retro barefoot'),
           ('08', 'black foam clogs decorated with small gold charms, no logos', 'Zuecos con charms')],
    l1=('07', 'fluffy pink faux-fur house slippers on a grey floor'),
    l2=(None, 'a woman walking on a sunny seafront promenade wearing brown barefoot sneakers and cropped jeans, framed from the knees down'),
    cats=[('Barefoot', 'p1'), ('Botas', 'p3'), ('Bolsos', 'p4')])

S['scarpa'] = dict(
    niche='moda', place='the Bizkaia Bridge (Puente Colgante) over the river in Getxo and Portugalete, near Bilbao, Spain', who='woman',
    hero=('02', 'a burgundy patent leather trench coat with burgundy tights and burgundy heeled shoes'),
    banner=('12', 'the inside of an eclectic boutique with corrugated metal walls, glass pendant lamps, colourful patterned bags on hooks and a table of sneakers and espadrilles, no people'),
    prods=[('02', 'a glossy burgundy patent leather trench coat with a belt', 'Gabardina de charol'),
           ('11', 'a green and white striped trench coat with an orange silk scarf', 'Gabardina de rayas'),
           ('10', 'a pink and brown check blazer with matching wide trousers and a cream top', 'Traje de cuadros'),
           ('05', 'a khaki cotton overshirt jacket with matching wide trousers', 'Conjunto caqui'),
           ('03', 'a white puff-sleeve cotton blouse with a navy and white striped ruffled midi skirt', 'Falda de rayas con volante'),
           ('08', 'flat leather sandals in brown, ballet flats in cream and a round woven straw bag', 'Sandalias y capazo')],
    l1=('09', 'an orange knit jumper with a silk neckerchief and white high-waisted trousers'),
    l2=('05', 'a row of colourful polka-dot and patterned shopper bags hanging on a corrugated metal wall'),
    cats=[('Abrigos', 'p1'), ('Conjuntos', 'p3'), ('Calzado y bolsos', 'p6')])

S['calzados-angela-vaya-zapatos'] = dict(
    logo=dict(text='Vaya Zapatos', sub='Calzados Ángela'), short='Vaya Zapatos',
    place='the narrow cobbled streets of the Jewish quarter of Hervás, Cáceres, Spain, with chestnut trees', who='woman', light=True,
    hero=('08', 'tall brown suede western boots worn with a long denim skirt'),
    banner=('01', 'the inside of a bright shoe shop with light wooden shelves full of shoes and boots and a teal seating pouf, no people, no logos'),
    prods=[('04', 'cognac textured leather western ankle boots with a block heel, no logos', 'Botín camperos'),
           ('01', 'black quilted padded ankle boots with a side zip and a chunky sole, no logos', 'Botín acolchado'),
           ('06', 'loafers in black leather and in brown suede with a gold bar detail, no logos', 'Mocasín con detalle dorado'),
           ('08', 'tall brown suede western boots with a block heel, no logos', 'Bota alta de ante'),
           ('03', 'tan suede lace-up comfort ankle boots, no logos', 'Botín de cordones'),
           ('05', 'taupe metallic comfort sneakers with a side zip, no logos', 'Deportiva cómoda')],
    l1=('02', 'a blue and brown wide-striped chunky knit jumper with jeans'),
    l2=('11', 'gold metallic strappy flat sandals worn with a black skirt, feet only'),
    cats=[('Botines', 'p1'), ('Botas', 'p4'), ('Mocasines', 'p3')])

S['mizor'] = dict(
    place='a sunny square with orange trees in Onda, Castellón, Spain, with the castle on the hill', who='woman', light=True,
    eyebrow='Zapatos y bolsos', h1='Zapatos y bolsos<br>que se notan.',
    hero=('02', 'burgundy patent leather pointed Mary Jane pumps worn with black wide trousers and a cow-print handbag'),
    banner=(None, 'the inside of a bright shoe and bag shop with white shelves, warm marble floor and displays of handbags and shoes, no people, no logos'),
    prods=[('02', 'burgundy patent leather pointed Mary Jane pumps with a slim heel, no logos', 'Salón Mary Jane'),
           ('01', 'a brown and white cow-print bowling handbag with tassels, no logos', 'Bolso vaca'),
           ('05', 'tan suede loafers with a snake-print strap, no logos', 'Mocasín de ante'),
           ('06', 'brown and white cowhide sneakers with fringes and braided laces, no logos', 'Zapatilla con flecos'),
           ('11', 'tan suede retro sneakers with a gum sole, no logos', 'Zapatilla retro'),
           ('09', 'men\'s brown leather casual sneakers with a light sole, no logos', 'Deportiva de piel de hombre')],
    l1=('04', 'a black leather shoulder bag with many zip pockets, carried with jeans, no logos'),
    l2=('03', 'burgundy and black leather wallets and a purse on a white table, no logos'),
    cats=[('Zapatos', 'p1'), ('Bolsos', 'p2'), ('Hombre', 'p6')])

S['calzados-moreno'] = dict(
    place='the Roman bridge over the Guadiana in Mérida, Spain', who='woman', light=True,
    hero=('07', 'dark brown suede slouchy knee boots with a kitten heel, worn with jeans'),
    banner=('13', 'the inside of a family shoe shop with tall shelves of shoe boxes, glass shop window and bright light, no people, no logos'),
    prods=[('07', 'dark brown suede slouchy knee-high boots with a slim kitten heel, no logos', 'Bota arrugada'),
           ('08', 'chunky sneakers in beige, white and lilac with a thick sole, no logos', 'Deportiva plataforma'),
           ('16', 'brown suede ankle boots with a high block heel and a small platform, no logos', 'Botín de tacón alto'),
           ('18', 'black leather knee boots with a block heel and a buckle, no logos', 'Bota alta negra'),
           ('06', 'cognac leather wedge ankle boots with two zips, no logos', 'Botín de cuña'),
           ('04', 'brown and black leather ankle boots with a medium block heel, no logos', 'Botín tacón medio')],
    l1=('12', 'black suede sock ankle boots with a high block heel worn with jeans, from the knees down'),
    l2=('17', 'brown suede comfort shoes with a double zip, worn with jeans, from the knees down'),
    cats=[('Botines', 'p3'), ('Botas', 'p1'), ('Deportivas', 'p2')])

S['perfums-alomar'] = dict(
    place='Sóller', who='none', theme=dict(acc='#2F4B3A'),
    hero=('02', 'a black square perfume bottle with a heavy black cap on dark stone with warm light, no brand names'),
    banner=('11', 'the inside of a bright perfumery with long walls of glass shelves full of perfumes and cosmetics, no people, no brand names'),
    prods=[('02', 'a black square glass perfume bottle with a black cap, no brand name', 'Perfume intenso'),
           ('05', 'a row of liquid lip tints in red and rose shades, no brand names', 'Tinte de labios'),
           ('14', 'a gift set wrapped in a white pouch with a red bow, perfume and creams, no brand names', 'Set de regalo'),
           ('16', 'colourful sheet face masks in yellow, blue and green packaging, no brand names', 'Mascarillas'),
           ('18', 'a bottle of golden body oil and a tube of hand cream in yellow packaging, no brand names', 'Aceite corporal'),
           ('13', 'a white textured perfume bottle with an embossed pattern, no brand name', 'Perfume blanco')],
    l1=('03', 'a perfumery shop window with glass doors and autumn branches, warm light, no brand names'),
    l2=('04', 'a makeup artist applying make-up to a woman in a perfumery, seen from the side'),
    cats=[('Perfumes', 'p1'), ('Maquillaje', 'p2'), ('Tratamiento', 'p5')])

# ---------------- ópticas (hero partido: bodegón de gafas; marcas sin logos)
S['centro-optico-plaza'] = dict(
    place='Madrid', who='none', theme=dict(acc='#D25A86'),
    hero=('07', 'colourful acetate eyeglasses in orange, blue and purple on a pink stone plinth'),
    banner=('11', 'the inside of a cheerful optician shop with a pink wall, mint green round shelves holding glasses, white counters and a white desk, no people, no logos'),
    prods=[('07', 'bold eyeglasses with layered orange, blue and purple acetate, no logos', 'Gafa multicolor'),
           ('02', 'red rectangular acetate eyeglasses, no logos', 'Gafa roja'),
           ('09', 'thin pink metal round eyeglasses, no logos', 'Gafa rosa'),
           ('01', 'tortoiseshell acetate sunglasses with brown lenses, no logos', 'Gafa de sol carey'),
           ('10', 'black rectangular acetate eyeglasses, no logos', 'Gafa negra clásica'),
           ('06', 'mint green acetate sunglasses, no logos', 'Gafa de sol menta')],
    l1=('07', 'a smiling woman with curly hair wearing bold colourful eyeglasses, in a bright shop'),
    l2=('02', 'a man in a navy hoodie wearing red rectangular eyeglasses, in a bright shop'),
    cats=[('Graduadas', 'p1'), ('De sol', 'p4'), ('Revisión visual', 'l1')])

S['lulu-eyewear-gallery'] = dict(
    place='Marbella', who='none', theme=dict(acc='#9A6B4F', bg='#FAF6F1'),
    hero=('01', 'designer sunglasses in burgundy cat-eye, blue oval and black wrap shapes on a sunny white garden table'),
    banner=('02', 'the inside of a luxury eyewear gallery with backlit cream shelves displaying sunglasses, warm light, no people, no logos'),
    prods=[('01', 'burgundy acetate cat-eye sunglasses with dark lenses, no logos', 'Gafa de sol cat-eye'),
           ('04', 'brown transparent hexagonal sunglasses and brown aviator sunglasses, no logos', 'Gafa de sol hexagonal'),
           ('07', 'pink oval sunglasses next to a pink case and a pink rose, no logos', 'Gafa de sol rosa'),
           ('12', 'black round thick acetate sunglasses, no logos', 'Gafa de sol redonda'),
           ('05', 'green mirrored sport shield sunglasses, no logos', 'Gafa de sol deportiva'),
           ('02', 'gold and tortoiseshell sunglasses with amber lenses, no logos', 'Gafa de sol ámbar')],
    l1=('03', 'a young woman with long hair wearing rose-tinted rimless sunglasses, sunny terrace'),
    l2=('10', 'many designer sunglasses spread on a marble table in the sun, no logos'),
    cats=[('Gafas de sol', 'p1'), ('Novedades', 'l2'), ('Graduadas', 'p4')])

S['optica-ballester'] = dict(
    place='Vitoria-Gasteiz', who='none', theme=dict(acc='#C23B5A'),
    hero=('02', 'bright green cat-eye acetate eyeglasses with a small red dot on the temple on white marble'),
    banner=(None, 'the inside of an elegant optician shop with white walls, wooden shelves of colourful eyeglasses and a bright counter, no people, no logos'),
    prods=[('02', 'bright green cat-eye acetate eyeglasses with a red dot on the hinge, no logos', 'Gafa verde ojo de gato'),
           ('05', 'bold hot-pink acetate eyeglasses, no logos', 'Gafa fucsia'),
           ('06', 'burgundy and green octagonal thin eyeglasses, no logos', 'Gafa octogonal'),
           ('07', 'cat-eye eyeglasses in navy, red and tortoiseshell acetate, no logos', 'Gafa ojo de gato'),
           ('10', 'round black and white speckled acetate eyeglasses, no logos', 'Gafa redonda moteada'),
           ('04', 'round two-tone peach and grey sunglasses among pink carnations, no logos', 'Gafa de sol redonda')],
    l1=('11', 'a laughing young woman with curly blonde hair wearing square burgundy eyeglasses'),
    l2=('12', 'a young woman with a fringe wearing thin square metal eyeglasses, close up, soft light'),
    cats=[('Graduadas', 'p1'), ('De sol', 'p6'), ('Revisión visual', 'l1')])

S['optica-constitucion'] = dict(
    place='Murcia', who='none', theme=dict(acc='#1F5FA8'),
    hero=('02', 'flexible unbreakable black and blue eyeglasses on a light wooden table'),
    banner=('10', 'the inside of a classic optician shop with walls of eyeglasses, wooden counters and blue accents, no people, no logos'),
    prods=[('02', 'flexible black and blue unbreakable eyeglasses, no logos', 'Gafa irrompible'),
           ('09', 'a tray of tinted sunglass lens samples in amber, rose and grey', 'Lentes de sol a medida'),
           ('06', 'black wayfarer-style sunglasses, no logos', 'Gafa de sol negra'),
           ('11', 'simple black reading glasses, no logos', 'Gafa de cerca'),
           ('12', 'tortoiseshell round sunglasses, no logos', 'Gafa de sol carey'),
           ('07', 'thin gold metal round eyeglasses, no logos', 'Gafa metálica dorada')],
    l1=('07', 'an optometrist in a white coat checking a young woman\'s vision with a trial frame, in a clinic room'),
    l2=('12', 'a smiling woman in a straw hat wearing tortoiseshell sunglasses on a sunny day'),
    cats=[('Graduadas', 'p1'), ('De sol', 'p3'), ('Revisión visual', 'l1')])

S['deseover'] = dict(
    place='Elche', who='none', theme=dict(acc='#D03A2F'),
    hero=('05', 'three sunglasses in honey, burgundy and black acetate on a bright white shelf'),
    banner=('04', 'the inside of a bright optician shop with a red ceiling arch and long white walls of sunglasses, no people, no logos'),
    prods=[('05', 'honey-coloured acetate sunglasses, no logos', 'Gafa de sol miel'),
           ('06', 'black square thick acetate eyeglasses, no logos', 'Gafa negra cuadrada'),
           ('08', 'gold metal sunglasses with burgundy gradient lenses, no logos', 'Gafa de sol metálica'),
           ('09', 'oversized black square sunglasses, no logos', 'Gafa de sol oversize'),
           ('11', 'black square sunglasses with a burgundy leather case, no logos', 'Gafa de sol con estuche'),
           ('03', 'rimless rose-tinted sunglasses, no logos', 'Gafa de sol rosa')],
    l1=('03', 'a smiling young woman with long straight hair wearing rose-tinted rimless sunglasses, white top'),
    l2=('07', 'a smiling woman with short hair wearing thin black eyeglasses, in an optician shop'),
    cats=[('De sol', 'p1'), ('Graduadas', 'p2'), ('Revisión visual', 'l2')])

S['optica-dh-vision'] = dict(
    place='Dos Hermanas', who='none', theme=dict(acc='#3C5A4F'),
    hero=('02', 'round tortoiseshell eyeglasses on a beige linen cloth with dried pampas grass'),
    banner=('07', 'the inside of a calm optician shop with floral wallpaper, small wooden shelves with glasses and a white desk, no people, no logos'),
    prods=[('02', 'round tortoiseshell acetate eyeglasses, no logos', 'Gafa redonda carey'),
           ('12', 'burgundy acetate eyeglasses, no logos', 'Gafa burdeos'),
           ('07', 'black rectangular eyeglasses, no logos', 'Gafa negra'),
           ('11', 'black rectangular eyeglasses with a magnetic sun clip-on, no logos', 'Gafa con clip solar'),
           ('01', 'black cat-eye sunglasses, no logos', 'Gafa de sol negra'),
           ('08', 'a wall of sunglasses in many colours, no logos', 'Gafas de sol')],
    l1=('02', 'a young woman in a brown blazer wearing round eyeglasses and holding a mug, soft light'),
    l2=('11', 'a young man in a pink polo shirt trying on sunglasses in an optician shop'),
    cats=[('Graduadas', 'p1'), ('De sol', 'p5'), ('Clip solar', 'p4')])

S['antonio-martin-centro-optico'] = dict(
    place='Almería', who='none', theme=dict(acc='#1E5C5A'),
    hero=('07', 'three classic black and tortoiseshell sunglasses with green lenses on pale stone'),
    banner=('12', 'the inside of a modern optician and hearing centre with a grey wall, white counters and walls of glasses, no people, no logos'),
    prods=[('07', 'classic black square sunglasses with green lenses, no logos', 'Gafa de sol clásica'),
           ('05', 'black oval chunky sunglasses, no logos', 'Gafa de sol ovalada'),
           ('11', 'amber orange transparent sunglasses, no logos', 'Gafa de sol ámbar'),
           ('08', 'dark tortoiseshell square sunglasses, no logos', 'Gafa de sol carey'),
           ('09', 'black oval sunglasses with gold details, no logos', 'Gafa de sol con detalle dorado'),
           ('02', 'thin round eyeglasses with clear lenses, no logos', 'Gafa graduada redonda')],
    l1=('11', 'a woman with wavy hair in a black leather jacket wearing amber sunglasses, studio portrait'),
    l2=('09', 'a woman in a white tank top wearing black oval sunglasses, sunny'),
    cats=[('De sol', 'p1'), ('Graduadas', 'p6'), ('Audición', 'l1')])

S['optica-miraflores'] = dict(
    place='Burgos', who='none', theme=dict(acc='#1C3F94'),
    hero=('02', 'blue and pale pink acetate sunglasses on a pink brick on a bright blue background'),
    banner=('01', 'the outside of an optician shop with a stone facade and big glass windows on a street in Burgos, no people, no logos'),
    prods=[('02', 'chunky blue acetate sunglasses with pale pink temples, no logos', 'Gafa de sol azul'),
           ('05', 'purple acetate eyeglasses with red details, no logos', 'Gafa morada'),
           ('08', 'black cat-eye sunglasses with gold metal details on the temples, no logos', 'Gafa de sol negra y oro'),
           ('09', 'black square sunglasses with gold hinges, no logos', 'Gafa de sol cuadrada'),
           ('12', 'thick black rectangular eyeglasses, no logos', 'Gafa negra gruesa'),
           ('07', 'a glass cabinet full of sports sunglasses, no logos', 'Gafas deportivas')],
    l1=('06', 'three smiling women wearing colourful sunglasses, cheerful'),
    l2=('12', 'a young woman with a fringe in a striped tee wearing thick black eyeglasses'),
    cats=[('De sol', 'p1'), ('Graduadas', 'p2'), ('Deporte', 'p6')])

S['guillermo-ramos-optico'] = dict(
    place='Málaga', who='none', theme=dict(acc='#1F6FB2'),
    hero=('09', 'tortoiseshell and black acetate eyeglasses and sunglasses on a grey stone surface'),
    banner=('15', 'the inside of a bright optician shop with long white walls of glass shelves full of eyeglasses, no people, no logos'),
    prods=[('09', 'tortoiseshell cat-eye sunglasses, no logos', 'Gafa de sol carey'),
           ('09', 'black rectangular eyeglasses with silver rivets, no logos', 'Gafa negra'),
           ('02', 'bright blue rectangular acetate eyeglasses, no logos', 'Gafa azul'),
           ('03', 'a wall of sunglasses in brown and black tones, no logos', 'Gafas de sol'),
           ('18', 'red and black sports eyeglasses for kids sport, no logos', 'Gafa deportiva'),
           ('15', 'thin metal eyeglasses in silver and gold, no logos', 'Gafa metálica')],
    l1=('12', 'an optician in a white coat adjusting eyeglasses on a smiling woman in a clinic'),
    l2=('06', 'a woman trying on eyeglasses in front of a round mirror in an optician shop, seen from behind'),
    cats=[('Graduadas', 'p2'), ('De sol', 'p1'), ('Revisión visual', 'l1')])

S['centro-optico-emperatriz'] = dict(
    place='Granada', who='none', theme=dict(acc='#1A2A4A'),
    hero=('13', 'round dark sunglasses on a sunny white surface with a palm shadow'),
    banner=('05', 'the inside of a modern optician shop with grey ceiling lights, white shelves of glasses and a white counter, no people, no logos'),
    prods=[('13', 'round black sunglasses with dark lenses, no logos', 'Gafa de sol redonda'),
           ('06', 'transparent light blue rectangular eyeglasses, no logos', 'Gafa azul transparente'),
           ('14', 'cat-eye sunglasses in burgundy and black on a straw hat, no logos', 'Gafa de sol cat-eye'),
           ('07', 'a box of monthly contact lenses, no brand name', 'Lentillas'),
           ('02', 'black square eyeglasses, no logos', 'Gafa negra'),
           ('12', 'a wall of sunglasses in many colours on white shelves, no logos', 'Gafas de sol')],
    l1=('01', 'an elegant woman in a striped maxi dress putting on sunglasses at a shop door'),
    l2=('05', 'a smiling young woman wearing tortoiseshell eyeglasses in a modern optician shop'),
    cats=[('De sol', 'p1'), ('Graduadas', 'p2'), ('Lentillas', 'p4')])

# ---- Lote 34 (11/11/2026): las 10 de moda que faltaban y 10 perfumerías (referencias = l34src/<slug>/NN.jpg) ----
S['dafne'] = dict(
    place='the Plaza del Castillo in Pamplona, Spain, with its arcades and bandstand on a sunny day', who='woman',
    hero=('14', 'a long rust-orange wool coat over a brown knit top and brown trousers'),
    banner=('25', 'the inside of a bright fashion boutique with rails of colourful printed blouses and shirts, white walls and a warm wooden floor, no people'),
    prods=[('16', 'a brown suede bomber jacket over a brown knit and brown check straight trousers', 'Conjunto Natural Elegance'),
           ('17', 'a violet double-breasted blazer with matching wide violet trousers and a grey scarf', 'Traje violeta'),
           ('22', 'a pink floral print loose shirt with long sleeves', 'Camisa de flores rosa'),
           ('21', 'a white midi dress with short puff sleeves, a V-neck and buttons', 'Vestido blanco'),
           ('08', 'a black and grey printed short jacket with ribbed trims over black flared trousers', 'Chaqueta estampada'),
           ('19', 'a pair of leopard-print calf-hair loafer shoes with a gold chain detail', 'Mocasines de leopardo')],
    l1=('18', 'a blue, red and cream printed boho midi dress with long sleeves'),
    l2=('03', 'a chunky gold snake-chain collar necklace with a black oval stone, lying on grey linen'),
    cats=[('Blusas', 'p3'), ('Vestidos', 'p4'), ('Complementos', 'p6')])

S['frecuencia'] = dict(
    place='the Plaza del Pilar in Zaragoza, Spain, with the Basilica of El Pilar behind, on a sunny afternoon', who='woman',
    hero=('17', 'a long brown and black tie-dye print satin wrap dress with wide sleeves and a deep V-neck, for an evening event'),
    banner=('05', 'the inside of an elegant boutique with patterned wallpaper, gold-framed mirrors, rails of colourful party dresses and coats, shelves of shoes and a cream marble floor, no people'),
    prods=[('19', 'a plum velvet waistcoat with gold buttons and matching wide palazzo trousers', 'Conjunto granate'),
           ('18', 'a burgundy lace two-piece: a long-sleeved lace top and a tiered lace maxi skirt', 'Conjunto de encaje'),
           ('23', 'a puff-sleeved midi dress with a pink, purple and gold floral print and a square neck', 'Vestido estampado'),
           ('13', 'a long white crepe bridal dress with long sleeves, a high neck and a train', 'Vestido de novia'),
           ('28', 'a pair of grey-blue velvet slingback shoes with a big buckle', 'Zapato de terciopelo'),
           ('32', 'a pair of white satin pointed shoes with a crystal trim', 'Zapato de novia')],
    l1=('27', 'a pair of burgundy velvet slingback shoes and a matching velvet headpiece on a black round table'),
    l2=('12', 'colourful faux-fur stoles in white, pink, red, lilac and blue hanging on a rail'),
    cats=[('Fiesta', 'p2'), ('Novia', 'p4'), ('Zapatos', 'p5')])

S['teresa-tello'] = dict(
    place='the seafront promenade of Sant Feliu de Guíxols on the Costa Brava, Spain, with the bay and the pine-covered hills', who='woman',
    hero=('09', 'a long python-print knit maxi dress with a high neck and long sleeves, with black knee boots'),
    banner=('06', 'the inside of a minimalist boutique with rails of dark knitwear and coats, grey textured plaster walls and a few pairs of shoes on a light floor, no people'),
    prods=[('01', 'a chocolate-brown velvet blazer and matching straight velvet trousers', 'Traje de terciopelo'),
           ('02', 'a cream rib-knit off-shoulder maxi dress with a side slit', 'Vestido de punto crudo'),
           ('03', 'a cream knit mini dress with long flared lace-trimmed sleeves and a crochet hem', 'Vestido de crochet'),
           ('08', 'a brown fitted knit maxi dress with a draped side and faux-fur cuffs', 'Vestido con puños de pelo'),
           ('18', 'a grey baseball cap with an embroidered teddy-bear patch', 'Gorra de osito'),
           ('11', 'a khaki parka with a big grey faux-fur collar over a white top', 'Parka con pelo')],
    l1=('25', 'a leopard-print wide-sleeved crop top with matching wide leopard trousers'),
    l2=('04', 'a long paisley-embroidered coat with frayed edges over light jeans'),
    cats=[('Vestidos', 'p2'), ('Abrigos', 'p6'), ('Complementos', 'p5')])

S['legend'] = dict(
    place='the colourful houses along the Onyar river in Girona, Spain, on a crisp sunny day', who='man',
    hero=('18', 'a dark green waxed cotton jacket with a corduroy collar over an orange jumper and blue jeans'),
    banner=('21', 'the inside of a modern menswear shop with black metal shelves of folded knitwear, jackets on hangers and boots on display, white walls, no people'),
    prods=[('10', 'a pair of brown suede moc-toe lace-up boots with a chunky tan sole', 'Botas de ante'),
           ('12', 'a pair of brown tartan wool lace-up shoes with a chunky dark sole', 'Zapato de cuadros'),
           ('06', 'a navy blue unstructured blazer over a white shirt', 'Americana azul'),
           ('25', 'a grey-green softshell hooded jacket', 'Chaqueta técnica'),
           ('15', 'round orange acetate sunglasses with their case, on denim', 'Gafas de sol naranjas'),
           ('23', 'a pair of beige and silver running sneakers', 'Zapatillas')],
    l1=('01', 'a man wearing a long olive wool coat over an orange and green knitted jumper and green trousers'),
    l2=('31', 'a stack of folded knitwear and trousers with a pair of brown suede sneakers on top and tortoiseshell sunglasses'),
    cats=[('Calzado', 'p1'), ('Chaquetas', 'p4'), ('Complementos', 'p5')])

S['violeta-y-chloe'] = dict(
    place='the Roman walls of Lugo, Spain, on a sunny autumn day', who='woman',
    hero=('16', 'a long blue printed boho maxi dress with a tiered skirt under a long camel cardigan'),
    banner=('30', 'the inside of a bright white fashion boutique with a crystal chandelier, rails full of colourful clothes and knitwear along white walls and a light wooden floor, no people'),
    prods=[('19', 'a brown check blazer with a faux-fur collar over a white top, with matching check trousers', 'Traje de cuadros con pelo'),
           ('11', 'a burgundy bomber jacket with cream stripes on the sleeves over a striped top and blue jeans', 'Bomber granate'),
           ('22', 'a brown satin blouse with tie fronts and long sleeves', 'Blusa satinada'),
           ('29', 'a black and cream polka-dot wrap midi dress with long sleeves', 'Vestido de lunares'),
           ('17', 'a grey-brown faux-fur jacket', 'Abrigo de pelo'),
           ('02', 'a rust and black leopard-print knit jumper with beige trousers', 'Jersey de leopardo')],
    l1=('15', 'a red and black floral print midi dress with long sleeves'),
    l2=('05', 'a beige puffer jacket with a high collar over black trousers'),
    cats=[('Abrigos', 'p5'), ('Vestidos', 'p4'), ('Punto', 'p6')])

S['estil-unic'] = dict(
    place='a sunny sandstone street of Porreres, Mallorca, Spain, with green wooden shutters', who='woman',
    hero=('05', 'a long teal-blue belted trench coat over a white top'),
    banner=('23', 'the inside of a warm boutique with sandstone walls, wooden glass display cabinets with jewellery and bags, a wooden counter and rails of clothes, no people'),
    prods=[('09', 'a purple satin blouse with voluminous sleeves and a black pleated midi skirt', 'Blusa morada'),
           ('08', 'a white shirt with embroidered red roses and wide-leg blue jeans', 'Camisa de rosas'),
           ('06', 'a long rust silk printed duster over a bronze satin blouse and matching trousers', 'Conjunto satinado'),
           ('29', 'a white shirt with a long green pleated crinkle skirt', 'Falda plisada verde'),
           ('24', 'a rust-brown belted midi shirt dress', 'Vestido camisero'),
           ('22', 'a long grey waistcoat over a white T-shirt and wide grey trousers', 'Chaleco largo')],
    l1=('13', 'a brown fringed knit poncho over a white shirt and a dark skirt'),
    l2=('10', 'a cosy corner of the boutique with a wicker armchair, a sandstone wall, a leather bag and an olive tree'),
    cats=[('Blusas', 'p1'), ('Vestidos', 'p5'), ('Faldas', 'p4')])

S['urban-crew'] = dict(
    place='the Plaza de España in Santa Cruz de Tenerife, Spain, with palm trees and the sea, on a sunny day', who='woman',
    hero=('26', 'a grey and brown tartan oversized blazer with a black studded leather crossbody bag and wide dark jeans'),
    banner=('08', 'the inside of a bright small boutique with white walls, a grey table with folded knitwear and jeans, rails of clothes and a light wooden floor, no people'),
    prods=[('01', 'a dark brown leather biker jacket over an olive knit top', 'Cazadora de piel'),
           ('06', 'a rust-brown draped cowl-neck long-sleeved top', 'Top drapeado'),
           ('36', 'a brown, olive and cream argyle knit jumper over a white shirt', 'Jersey de rombos'),
           ('19', 'a pink knit jumper with a white shirt collar and blue straight jeans', 'Jersey rosa'),
           ('16', 'a pair of black ruched leather Mary Jane flat shoes', 'Bailarinas Mary Jane'),
           ('05', 'a black T-shirt with a teddy bear print', 'Camiseta de osito')],
    l1=('23', 'a white shirt with a burgundy knit jumper tied over the shoulders and burgundy trousers with a paisley scarf as a belt'),
    l2=('32', 'a table of neatly folded trousers and knitwear in olive, rust, cream and striped colours'),
    cats=[('Chaquetas', 'p1'), ('Punto', 'p3'), ('Zapatos', 'p5')])

S['elena-blanco-moda'] = dict(
    place='the seafront of Algeciras, Spain, with the bay and the Rock of Gibraltar in the distance, on a sunny day', who='woman',
    hero=('01', 'a long red and navy paisley print maxi dress with long sleeves'),
    banner=('12', 'the inside of a fashion boutique with blue toile wallpaper, white shelves, long rails packed with colourful clothes, a white counter and a light wooden floor, no people'),
    prods=[('13', 'a matching black, white and brown geometric print shirt and wide trousers set', 'Conjunto estampado'),
           ('07', 'a dark brown faux-fur jacket over a pink satin midi skirt', 'Chaqueta de pelo'),
           ('11', 'a white embroidered lace-trimmed boho blouse with black wide trousers', 'Blusa ibicenca'),
           ('18', 'a khaki camouflage-print shirt jacket and matching wide trousers', 'Conjunto militar'),
           ('25', 'a long denim-blue tiered maxi dress with long sleeves', 'Vestido vaquero largo'),
           ('20', 'a pair of tan suede knee-high boots', 'Botas altas de ante')],
    l1=('27', 'an orange linen shirt and matching wide orange trousers'),
    l2=('26', 'a long cream shirt dress with a red and green floral print'),
    cats=[('Conjuntos', 'p1'), ('Vestidos', 'p5'), ('Calzado', 'p6')])

S['el-tendedero-de-nieves'] = dict(
    place='the riverside promenade of El Puerto de Santa María, Cádiz, Spain, with whitewashed buildings and palm trees', who='woman',
    hero=('11', 'a long brown faux-leather trench coat over a brown top and brown trousers, with a long wooden bead necklace'),
    banner=('31', 'the inside of a light boutique with white shelves of bags and scarves, rails of clothes, an orange pendant lamp and dried flowers, no people'),
    prods=[('17', 'a brown bomber jacket embroidered with floral and paisley patterns over a white top and light wide jeans', 'Cazadora bordada'),
           ('03', 'a brown and camel check knit poncho', 'Poncho de cuadros'),
           ('10', 'a navy blouse with red flowers and a tie neck, with dark jeans', 'Blusa de flores'),
           ('30', 'an olive cardigan with colourful embroidered flowers and wide blue jeans', 'Chaqueta bordada'),
           ('14', 'a wide black leather belt with a knotted paisley silk scarf, worn over a white shirt', 'Cinturón con pañuelo'),
           ('26', 'a pair of brown suede ankle boots with a strap and buckle', 'Botines de ante')],
    l1=('12', 'a long plum satin trench coat over a plum top and plum trousers'),
    l2=('21', 'chunky green and wooden bead statement necklaces displayed on linen busts'),
    cats=[('Chaquetas', 'p1'), ('Blusas', 'p3'), ('Complementos', 'p5')])

S['vainilla-moda'] = dict(
    place='a sunny street of Bullas, Murcia, Spain, with whitewashed houses and vineyards on the hills behind', who='woman',
    hero=('18', 'tan suede flat knee-high boots with a cream knit midi dress and a camel coat'),
    banner=('05', 'the inside of a bright accessories shop with white shelves full of bags, scarves, jewellery and pink cosmetics, no people'),
    prods=[('08', 'a leopard-print shoulder bag with a pink scarf knotted on the handle', 'Bolso de leopardo'),
           ('19', 'a pair of tan suede cowboy boots with stitched details', 'Botas camperas'),
           ('20', 'a pair of taupe suede slouchy knee boots with a kitten heel', 'Botas altas'),
           ('22', 'a pair of dark brown croc-embossed leather ankle boots with a kitten heel and a buckle strap', 'Botines de piel'),
           ('04', 'a long brown faux-fur stole scarf', 'Estola de pelo'),
           ('16', 'a brown knit jumper with a dachshund and polka-dot print, with beige trousers', 'Jersey de perrito')],
    l1=('15', 'oversized knit sweaters in cream and black hanging on a rail'),
    l2=('30', 'fluffy leopard and pastel faux-fur slippers on a shelf'),
    cats=[('Botas', 'p2'), ('Bolsos', 'p1'), ('Ropa', 'p6')])

S['aromas-artesanales'] = dict(niche='cosmetica',
    place='a sunny street of Pozoblanco, Córdoba, Spain', who='none',
    hero=('19', 'a purple glass perfume bottle with a light wooden cap standing on a stack of smooth grey stones with small yellow wild flowers'),
    banner=('03', 'the inside of a bright perfume shop with mint-green walls, glass shelves full of perfume bottles and cosmetics, a wooden counter and a light wooden floor, no people'),
    prods=[('02', 'a white ceramic decanter bottle with a cork and a hang tag next to a turquoise glass perfume bottle with a light wooden cap', 'Ubide · eau de parfum'),
           ('07', 'a white ceramic decanter bottle with a cork and a hang tag next to a blue glass perfume bottle with a light wooden cap', 'Candamo · perfume masculino'),
           ('13', 'a magenta-pink glass perfume bottle with a light wooden cap and a small pink ribbon', 'Robres · eau de parfum'),
           ('17', 'a blue glass perfume bottle with a light wooden cap', 'Perfume azul'),
           ('23', 'two green pump bottles of body oil and a green jar of body cream', 'Cosmética corporal'),
           ('20', 'a pink micellar water bottle, a white tube and a pink jar of face cream', 'Cuidado facial')],
    l1=('21', 'two blue glass perfume bottles with light wooden caps splashing into clear water'),
    l2=('24', 'a palo santo stick gently smoking on a small brass bowl on a dark wooden table'),
    cats=[('Perfumes', 'p1'), ('Cosmética', 'p5'), ('Ambientación', 'l2')])

S['anmar-perfumes'] = dict(niche='cosmetica',
    place='the seafront of Santa Cruz de Tenerife, Spain', who='none',
    hero=('06', 'a pale pink and gold perfume bottle with a sculpted gold cap, wrapped in torn peach paper with vanilla pods and caramel'),
    banner=('04', 'the inside of a perfume boutique with white shelves full of colourful Arabian perfume bottles and warm light, no people'),
    prods=[('02', 'two perfume bottles side by side, one gold and one black, each wrapped by a sculpted metal snake', 'Dúo de serpientes'),
           ('07', 'a pink perfume bottle with a tall pink cap, with strawberries and cream around it', 'Yara'),
           ('08', 'a brown and bronze perfume bottle with a dark cap, in torn paper with dark chocolate', 'Asad Bourbon'),
           ('26', 'a clear glass perfume bottle with pale blue liquid and a black cap', 'Intimation'),
           ('28', 'a red glass perfume bottle with a round black cap', 'Royale Charm'),
           ('27', 'a black and gold perfume bottle topped with a black and gold sculpted bust', 'His Confession')],
    l1=('03', 'an orange and cream perfume bottle with orange slices and star anise on a warm golden background'),
    l2=('01', 'a black perfume box with a gold snake emblem held in black-gloved hands'),
    cats=[('Mujer', 'p2'), ('Hombre', 'p3'), ('Novedades', 'l1')])

# --- lote 34 (11/11): 8 perfumerías árabes más ---
S['perfumes-casa-grande'] = dict(niche='cosmetica',
    place='the seafront of Mataró, Barcelona, Spain', who='none',
    hero=('20', 'a tall ornate gold perfume bottle with a gold cap standing on its open black presentation box'),
    banner=('12', 'the inside of a perfume boutique with tall shelves full of Arabian perfume bottles, a red carpet and warm light, no people'),
    prods=[('03', 'a black perfume bottle with a silver chain and medallion, in its open black box', 'Supremacy Not Only Intense'),
           ('09', 'a dark grey perfume bottle with a black textured cap and a silver band', 'Odyssey Nexus'),
           ('11', 'a dark amber glass perfume bottle with a gold and black emblem', 'SHK'),
           ('14', 'a round red perfume bottle with a red cap, next to its red box', 'Nitro Red'),
           ('21', 'a clear white perfume bottle with a sculpted silver cap', 'Spirito Mystic'),
           ('31', 'a gold perfume bottle next to its black and gold box', 'Fawah')],
    l1=('15', 'a pink gift box holding four Yara perfume bottles in pastel colours'),
    l2=('28', 'a silver perfume bottle shaped like a curved Arabian dagger on a stone stand'),
    cats=[('Mujer', 'l1'), ('Hombre', 'p1'), ('Novedades', 'p5')])

S['tyana-perfumes'] = dict(niche='cosmetica',
    place='the Explanada de España in Alicante, Spain', who='none',
    hero=('24', 'a ribbed gold glass perfume bottle with a gold cap among candles, dried oranges and amber stones'),
    banner=('30', 'the inside of a perfume boutique with white shelves full of Arabian perfume bottles and a counter, no people'),
    prods=[('03', 'a pale green glass perfume bottle with a gold cap', 'Equinox'),
           ('02', 'an amber-gold gradient glass perfume bottle with a gold cap', 'Vanilla Vibe'),
           ('09', 'an amber glass perfume bottle with a copper cap and its brown patterned box', 'Khamrah Mira'),
           ('14', 'a pale sage green perfume bottle with a gold cap', 'Club de Nuit Timeless'),
           ('45', 'a dark grey perfume bottle with a black textured cap and a silver band', 'Odyssey Nexus'),
           ('43', 'a navy blue perfume bottle with a gold cap and its blue box', 'Legacy')],
    l1=('04', 'two perfume bottles, one deep red and one teal, side by side on a counter in a perfume shop'),
    l2=('06', 'a red gift box open to show a row of small Nitro perfume bottles'),
    cats=[('Mujer', 'p2'), ('Hombre', 'p5'), ('Regalos', 'l2')])

S['dulce-fragancia'] = dict(niche='cosmetica',
    place='the seafront promenade of Benidorm, Spain', who='none',
    hero=('19', 'three round gourmand perfume bottles in amber and white glass with gold caps'),
    banner=('24', 'the inside of a perfume boutique with white shelves full of Arabian perfume bottles and soft light, no people'),
    prods=[('25', 'a purple perfume bottle with a silver cap and its purple and gold box', 'Amethyst'),
           ('31', 'a deep red perfume bottle with an ornate gold cap', 'Elysia Vanilla'),
           ('32', 'a pale blue perfume bottle with a silver cap', 'Kaaf'),
           ('22', 'a dusty pink glittery perfume box with a dark medallion', 'Queen of Roses'),
           ('15', 'a pink and gold perfume box with a deep red bottle', 'Bahiya Garnet'),
           ('28', 'a ribbed gold perfume box', 'Aristo')],
    l1=('26', 'a yellow gift set box with a black and yellow perfume bottle'),
    l2=('04', 'two perfume bottles, one pale green and one amber, with gold caps'),
    cats=[('Mujer', 'p2'), ('Unisex', 'p3'), ('Packs', 'l1')])

S['naira-aromas'] = dict(niche='cosmetica',
    place='the Paseo de Almería in Almería, Spain', who='none',
    hero=('01', 'a brown and gold perfume bottle with an ornate gold cap and Arabic lettering, with mango slices and white flowers'),
    banner=('28', 'the inside of a perfume boutique with white shelves full of colourful perfume bottles and Korean skincare, warm light, no people'),
    prods=[('02', 'a bright yellow perfume bottle with an ornate gold cap', 'Bana Bliss'),
           ('06', 'a round pink perfume bottle shaped like a doughnut with a gold cap, with strawberries', 'Sugar Rush Sprinkle Joy'),
           ('10', 'a pastel iridescent pink and blue perfume bottle with its matching box, among raspberries', 'Ajwad Pink To Pink'),
           ('24', 'a black perfume bottle with a gold horse emblem and a gold cap', 'Arabian Nights'),
           ('32', 'a green and blue gradient perfume bottle with a silver cap', 'Hawas Atlantis'),
           ('18', 'an amber orange perfume bottle with a gold cap and gold medallion', 'Mango Punch')],
    l1=('33', 'a gold perfume bottle with passion fruit and vanilla pods on a bright yellow background'),
    l2=('12', 'a small dark glass serum bottle with a pump on soft white fabric'),
    cats=[('Perfumes', 'p1'), ('Cosmética coreana', 'l2'), ('Novedades', 'l1')])

S['perfumeria-habibi'] = dict(niche='cosmetica',
    place='the Calle Príncipe in Vigo, Spain', who='none',
    hero=('19', 'an amber perfume bottle with a gold cap among candles and rose petals in a warm dark scene'),
    banner=('23', 'the inside of a perfume boutique with gold shelves full of Arabian perfume bottles and warm light, no people'),
    prods=[('18', 'a white square perfume bottle with a blue Arabic pattern and a silver cap', 'Rayhaan Azul'),
           ('19', 'an amber perfume bottle with a gold cap', 'Vous Elegante'),
           ('41', 'a blue perfume bottle with a silver circle emblem', 'Club de Nuit Iconic'),
           ('42', 'a gold perfume bottle with a dark cap inside a gold box with Arabic patterns', 'Atheeri'),
           ('15', 'the deep red and gold perfume bottle with a round gold label and gold cap (the first bottle on the left)', 'Hasaa'),
           ('15', 'the pale aqua glass perfume bottle with a clear faceted cap (the last bottle on the right)', 'Khamrah Waha')],
    l1=('15', 'the orange velvet perfume bottle with a gold cap (the second bottle from the left) with white flowers'),
    l2=('33', 'a gold trophy-shaped perfume bottle in a black box'),
    cats=[('Mujer', 'p5'), ('Hombre', 'p3'), ('Novedades', 'l1')])

S['casa-perfume-arabe'] = dict(niche='cosmetica',
    place='the Plaza de la Catedral in León, Spain', who='none',
    hero=('05', 'an ornate gold Arabian perfume bottle with a dome cap among white orchids'),
    banner=('22', 'the inside of a perfume boutique with long white shelves full of Arabian perfume bottles, no people'),
    prods=[('18', 'a dark blue gradient perfume bottle with a silver cap', 'Hawas for Him'),
           ('20', 'a pale blue perfume box with a white pattern', 'Khamrah Waha'),
           ('27', 'a dark brown perfume bottle with a large copper number 9 and a black cap', '9 PM'),
           ('29', 'a black square perfume bottle with a silver medallion', 'Club de Nuit Intense Man'),
           ('39', 'a bright pink perfume box with a colourful candy-shaped bottle', 'Odyssey Pink Pop'),
           ('34', 'a dark square perfume box with a gold geometric pattern', 'Rayhaan Terra')],
    l1=('15', 'a black perfume bottle with a woven cord around the neck, with lavender, cinnamon and nuts'),
    l2=('11', 'a pink and purple perfume gift set with two bottles in an open box'),
    cats=[('Hombre', 'p1'), ('Mujer', 'p5'), ('Regalos', 'l2')])

S['perfumes-arabes-aisha'] = dict(niche='cosmetica',
    place='the Gran Vía in Bilbao, Spain', who='none',
    hero=('10', 'a ribbed gold perfume bottle with a gold cap among lemons and golden flowers'),
    banner=('12', 'the inside of a perfume boutique with dark shelves full of colourful Arabian perfume boxes, no people'),
    prods=[('01', 'an amber orange perfume bottle with a black cap and flames', 'Club de Nuit Intense Fuego'),
           ('04', 'a black faceted perfume bottle with a gold cap and its black box', 'Royal Blend Nero'),
           ('26', 'a pale pink perfume bottle with a gold cap', 'Fayora'),
           ('30', 'a black square perfume bottle with a gold Arabic pattern', 'Qaed Al Fursan'),
           ('33', 'a pink and red perfume bottle with a gold cap', 'Yara'),
           ('15', 'a small white roll-on perfume bottle with a gold cap', 'Roll-on mini')],
    l1=('11', 'an amber perfume bottle with a gold cap among caramel flan, cookies and vanilla flowers'),
    l2=('31', 'a caramel-coloured perfume bottle with a rose gold cap with honeycomb and cream'),
    cats=[('Perfumes', 'p1'), ('Mujer', 'p5'), ('Roll-on', 'p6')])

S['saba-essences'] = dict(niche='cosmetica',
    place='the beach promenade of La Cala de Finestrat, Alicante, Spain', who='none',
    hero=('08', 'two perfume bottles topped with sculpted busts, one white and one black, with gold details'),
    banner=('15', 'the inside of a bright perfume boutique with long white shelves lit from below and rows of Arabian perfume bottles, no people'),
    prods=[('08', 'the white perfume bottle topped with a white sculpted bust and gold details (the one on the left)', 'Her Confession'),
           ('07', 'a square faceted glass perfume bottle with amber liquid and a clear cap', 'Khamrah Qahwa'),
           ('05', 'the pale green perfume bottle with a sculpted gold cap (the one on the right)', 'Eclaire Pistacho'),
           ('05', 'the cream and gold perfume bottle with a sculpted gold cap (the one in the middle)', 'Eclaire'),
           ('01', 'a square orange perfume bottle with a black cap', 'Club de Nuit'),
           ('02', 'a gold perfume bottle with a dark cap and its gold box with Arabic patterns', 'Atheeri')],
    l1=('11', 'a round pink glass perfume bottle wrapped in gold vines, with soft pink flowers'),
    l2=('04', 'a round perfume bottle with a pale blue centre framed in sculpted gold, on a marble table'),
    cats=[('Mujer', 'p1'), ('Hombre', 'p5'), ('Novedades', 'l1')])

# Lote 35 (12/11/2026)
import os as _os
exec(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'specs35.py'), encoding='utf-8').read())
exec(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'specs36.py'), encoding='utf-8').read())
