# Lote 48 (26/11/2026): tiendas del scrapeo nocturno del 25-26/11 (más grandes: varias tiendas físicas y sin tienda online),
# para enviar el 26/11 (sel48.json). Propuesta v42b + «Los números» (gen42.py) y la tienda «Editorial» (gen37a.py).
# Referencias NN = fotos de su Instagram (scratchpad l48/rf/<ig>/NN.jpg; en Flow, con la cara tapada: n<slug>-NN.jpg).
# Nunca referencias con menores, marcas, logos ni personajes conocidos (Snoopy de Nuria Roig 09 fuera).

S['nuria-roig'] = dict(
    place='a quiet elegant street in Sarrià, Barcelona, Spain, with stone buildings and plane trees', who='mature',
    hero=('17', 'a black quilted puffer jacket with a big natural fur hood, worn with blue jeans'),
    banner=(None, 'the inside of an elegant multibrand boutique in Barcelona with white walls, rails of knitwear, coats and blazers, white shelves with folded jumpers, boots and handbags, a light wooden floor, no people, no text'),
    prods=[('01', 'a black quilted puffer jacket with a fur-trimmed hood (flat lay)', 'Plumífero con capucha'),
           ('07', 'a cream oversized turtleneck knit jumper with grey trousers', 'Jersey de cuello alto'),
           ('19', 'a long black wool coat over a grey top and wide black trousers', 'Abrigo largo negro'),
           ('02', 'brown suede slouchy knee-high boots and brown leather loafers (flat lay)', 'Bota alta de ante'),
           ('23', 'a cream fluffy fleece jacket with straight blue jeans and white trainers', 'Chaqueta de borreguito'),
           ('20', 'a silver metallic shoulder bag with a curved shape (flat lay)', 'Bolso plateado')],
    l1=('14', 'a woman in a camel coat over a dark green quilted jacket, checked trousers and brown boots, standing in a boutique'),
    l2=('10', 'brown leather ankle boots and handbags on white shelves in a boutique, close up'),
    cats=[('Abrigos', 'p1'), ('Punto', 'p2'), ('Botas', 'p4')])

S['maribel-fernandez'] = dict(
    place='a sunny street in the centre of Murcia, Spain, with elegant buildings and orange trees', who='woman',
    hero=('15', 'a light grey tailored blazer with a matching midi pencil skirt with a front slit'),
    banner=(None, 'the inside of a bright modern fashion boutique in Murcia with rails full of trousers, jackets and knitwear, a white tufted ottoman, a beige rug and white walls, no people, no text'),
    prods=[('09', 'a grey double-breasted blazer with a white blouse and grey wide trousers', 'Traje gris'),
           ('17', 'an olive green blazer and matching wide trousers suit', 'Traje verde oliva'),
           ('22', 'a dark denim shirt with wide barrel-leg jeans', 'Conjunto vaquero'),
           ('14', 'a brown leather-look blazer with matching brown trousers and a belt', 'Traje marrón'),
           ('06', 'a black and white striped knit midi skirt with a black top', 'Falda de punto'),
           ('19', 'a camel blazer with a black top, black flared trousers and a gold chain belt', 'Blazer camel')],
    l1=('23', 'a woman in a burgundy leather-look trench coat and matching wide trousers in a white boutique'),
    l2=('03', 'a woman in a brown leather pencil skirt, a cropped jacket and high heels in a boutique with rails of clothes'),
    cats=[('Trajes', 'p1'), ('Vaqueros', 'p3'), ('Faldas', 'p5')])

S['rosi-botiga'] = dict(
    place='a narrow cobbled street in the old town of Girona, Spain, with stone arcades and tall buildings', who='mature',
    hero=('22', 'a camel wool coat with a colourful striped scarf and blue jeans'),
    banner=('04', 'the inside of a warm fashion and shoe shop in Girona with wooden shelves full of boots, shoes and bags, rails of coats, branches as decoration, no people, no text'),
    prods=[('03', 'a long dark grey wool coat with blue jeans', 'Abrigo gris largo'),
           ('02', 'a lime green oversized knit jumper with wide blue jeans', 'Jersey lima'),
           ('13', 'a pink and blue patterned long kimono coat over jeans', 'Kimono estampado'),
           ('09', 'a cream textured coat with matching cream trousers and trainers', 'Abrigo crema'),
           ('19', 'a dark brown oversized wool coat with brown trousers', 'Abrigo marrón'),
           ('07', 'an olive green shirt dress with a belt and a woven straw bag', 'Vestido camisero')],
    l1=('24', 'a woman in a mustard yellow jacket, a long denim skirt and a red bag standing at a green wooden door'),
    l2=('18', 'cream sneaker shoes and a fluffy cream bag on a glass shelf in a shop window, close up'),
    cats=[('Abrigos', 'p1'), ('Punto', 'p2'), ('Vestidos', 'p6')])

S['le-coquett'] = dict(
    place='a sunny shopping street in the centre of Barcelona, Spain, with modernist buildings and trees', who='woman',
    hero=('07', 'a khaki green parka with a fluffy brown faux fur lining, black tights and a brown leather handbag'),
    banner=('16', 'the inside of a warm fashion boutique with mannequins in quilted jackets and knitwear, wooden shelves with autumn decoration and a light floor, no people, no text'),
    prods=[('04', 'a red and burgundy patterned knit jumper with red corduroy trousers', 'Jersey de punto rojo'),
           ('11', 'a brown faux fur jacket over a cream top and black trousers', 'Chaqueta de pelo'),
           ('18', 'a burgundy blazer and matching wide trousers suit with a printed blouse', 'Traje burdeos'),
           ('09', 'a navy and mustard zigzag knit jumper with blue jeans', 'Jersey zigzag'),
           ('01', 'tan suede lace-up ankle boots lined with white faux fur (flat lay)', 'Botín forrado'),
           ('21', 'long wooden bead necklaces in brown, beige and black hanging on a display', 'Collares de madera')],
    l1=('20', 'a woman in a grey waistcoat, grey wide trousers and black boots posing at a boutique door'),
    l2=('05', 'a reversible quilted shirt jacket in khaki green and navy blue, two looks side by side'),
    cats=[('Punto', 'p1'), ('Abrigos', 'p2'), ('Trajes', 'p3')])

S['moda-tammara'] = dict(
    place='a sunny street in Peligros, Granada, Spain, with white buildings and the Sierra Nevada mountains in the distance', who='woman',
    hero=('12', 'a bright red short wool jacket over a burgundy striped top and light blue jeans'),
    banner=(None, 'the inside of a cosy women\'s fashion shop in Granada with rails of jeans and knitwear, wooden crates with folded clothes and a light floor, no people, no text'),
    prods=[('03', 'a fluffy dark brown faux fur jacket (flat lay)', 'Chaqueta de pelo'),
           ('08', 'a navy satin blouse with a pussy bow, straight blue jeans and burgundy heeled ankle boots (flat lay)', 'Blusa de lazada'),
           ('11', 'a brown knit wrap cardigan with a belt over black trousers', 'Rebeca con cinturón'),
           ('16', 'a burgundy and lilac striped long-sleeve top with straight blue jeans', 'Camiseta de rayas'),
           ('07', 'burgundy patent leather pointed-toe ankle boots with a kitten heel (flat lay)', 'Botín burdeos'),
           ('20', 'a cream short wool jacket with a belt and black wide trousers', 'Chaqueta crema')],
    l1=('23', 'a woman in a cream short trench jacket with a high collar and blue jeans in a fashion shop'),
    l2=('04', 'faux fur jackets in white, grey and black hanging on a rail, close up'),
    cats=[('Abrigos', 'p1'), ('Blusas', 'p2'), ('Calzado', 'p5')])

S['maria-tacones'] = dict(
    place='a sunny white street in Morón de la Frontera, Sevilla, Spain, with orange trees', who='woman',
    hero=('09', 'a dark brown top with a fluffy faux fur collar and a brown and grey checked wrap midi skirt'),
    banner=(None, 'the inside of a small Andalusian women\'s fashion boutique with black curtains, rails of jumpers, jeans and jackets, a wooden counter and a light floor, no people, no text'),
    prods=[('12', 'a grey wool cape coat with long sleeves and a high collar over a grey dress', 'Capa gris'),
           ('13', 'a brown paisley print blazer and matching trousers suit', 'Traje estampado'),
           ('17', 'a plaid jacket and matching trousers with a khaki faux fur collar', 'Conjunto de cuadros'),
           ('08', 'a burgundy off-the-shoulder knit jumper with burgundy jeans', 'Jersey burdeos'),
           ('15', 'a khaki green striped knit cardigan with khaki trousers', 'Rebeca de rayas'),
           ('06', 'wide-leg blue jeans with a black top and a burgundy leather jacket', 'Vaquero ancho')],
    l1=('18', 'a woman in a colourful patchwork brocade jacket and blue jeans in a boutique'),
    l2=('02', 'colourful embroidered round bag charms and keyrings, close up on a table'),
    cats=[('Abrigos', 'p1'), ('Conjuntos', 'p2'), ('Punto', 'p4')])

S['tribeca-store'] = dict(
    place='a quiet street in Cabezón de la Sal, Cantabria, Spain, with traditional stone houses and green hills', who='woman',
    hero=('03', 'a brown quilted puffer jacket with a teddy collar over blue jeans'),
    banner=('01', 'the inside of a bright modern fashion boutique with white round tables full of folded jumpers, an olive tree, rails of clothes along the walls and a light wooden floor, no people, no text'),
    prods=[('07', 'a burgundy and white argyle knit jumper with pale pink wide trousers', 'Jersey de rombos'),
           ('06', 'a cream knit cardigan with cream tailored shorts on a hanger', 'Rebeca crema'),
           ('13', 'a beige trench coat over a black top and black trousers with a black handbag', 'Gabardina beige'),
           ('17', 'a burgundy blouse with cream wide trousers', 'Blusa burdeos'),
           ('11', 'a black poncho with a colourful zigzag border over black trousers', 'Poncho negro'),
           ('15', 'a large red paisley silk scarf worn over a white top and jeans', 'Pañuelo estampado')],
    l1=('09', 'a woman in a navy and white striped jumper and wide blue jeans in a bright boutique'),
    l2=('10', 'colourful silk scarves with prints spread on a table, close up'),
    cats=[('Punto', 'p1'), ('Abrigos', 'p3'), ('Complementos', 'p6')])

S['doble-g-barcelona'] = dict(
    place='a sunny street in the Eixample of Barcelona, Spain, with modernist buildings and plane trees', who='mature',
    hero=('12', 'a long burgundy wool coat over a cream blouse and cream trousers'),
    banner=('11', 'the inside of an elegant multibrand women\'s boutique in Barcelona with rails of coats in burgundy, pink and grey, warm lights and a light floor, no people, no text'),
    prods=[('03', 'a camel wool coat over a pink scarf and burgundy wide trousers', 'Abrigo camel'),
           ('04', 'a black leather jacket over a black and white argyle knit jumper and cream wide trousers', 'Cazadora de piel'),
           ('13', 'a burgundy faux fur jacket with brown wide trousers and a burgundy handbag', 'Chaqueta de pelo'),
           ('15', 'a beige and pink checked wool coat over a burgundy top and burgundy trousers', 'Abrigo de cuadros'),
           ('18', 'a green and mustard checked quilted jacket with cream corduroy trousers', 'Chaqueta de cuadros'),
           ('24', 'an orange blazer with a printed scarf and black wide trousers', 'Blazer naranja')],
    l1=('19', 'a woman in a brown suede jacket, a brown printed scarf and cream trousers walking in a boutique'),
    l2=('02', 'a boutique display with knitwear, blazers, pink scarves and burgundy handbags on a wooden table'),
    cats=[('Abrigos', 'p1'), ('Chaquetas', 'p2'), ('Blazers', 'p6')])

S['ke-pasada-moda'] = dict(
    place='a sunny street in Palma de Mallorca, Spain, with sandstone buildings and palm trees', who='woman',
    hero=('12', 'a brown faux fur cropped jacket over a pinstripe corset top and black trousers'),
    banner=(None, 'the inside of a modern women\'s fashion shop in Palma with rails of black and neutral clothes, white tables with folded jeans, a grey stone floor and mirrors, no people, no text'),
    prods=[('04', 'a black knit top with an asymmetric collar and black wide trousers', 'Conjunto negro'),
           ('06', 'a cream knit top with an asymmetric zip collar and cream trousers', 'Conjunto crema'),
           ('13', 'a black faux leather belted jacket with black leather trousers', 'Conjunto de polipiel'),
           ('18', 'a burgundy and green tartan midi dress with a wide belt', 'Vestido de cuadros'),
           ('21', 'a brown zip-up sweatshirt with matching wide sweatpants', 'Chándal marrón'),
           ('15', 'a black sheer lace top with flared sleeves and a black maxi skirt', 'Top de encaje')],
    l1=('10', 'a woman in a black puffer jacket with a big faux fur collar and black leather trousers'),
    l2=('01', 'a woman in a black shirt and zebra print wide trousers in a fashion shop with colourful dresses'),
    cats=[('Conjuntos', 'p1'), ('Chaquetas', 'p3'), ('Vestidos', 'p4')])

S['aura-olot'] = dict(
    place='a narrow stone street in the old town of Olot, Girona, Spain, with old wooden doors and balconies', who='woman',
    hero=('09', 'a long camel wool coat with a khaki scarf next to a long light blue wool coat with a navy scarf'),
    banner=('13', 'the inside of a bright women\'s fashion shop in Olot with rails of coats and knitwear, a round wooden table, paper lamps and a light wooden floor, no people, no text'),
    prods=[('01', 'a long grey double-breasted wool coat over a burgundy jumper', 'Abrigo gris'),
           ('04', 'a grey knit jumper with straight blue jeans and a tan suede handbag', 'Jersey gris'),
           ('06', 'a white cropped knit cardigan with black buttons', 'Rebeca blanca'),
           ('12', 'a dark brown suede knee-high boot with a chunky sole (flat lay)', 'Bota alta de ante'),
           ('18', 'a khaki waistcoat with straight blue jeans', 'Chaleco caqui'),
           ('22', 'a black sleeveless midi dress with a keyhole neckline', 'Vestido negro')],
    l1=('10', 'a woman in an orange jumper, a colourful plaid scarf and blue jeans standing at a grey wooden door'),
    l2=('03', 'a navy wool coat with a long camel scarf, close up in a boutique'),
    cats=[('Abrigos', 'p1'), ('Punto', 'p2'), ('Calzado', 'p4')])

S['moda-martina-alvarez'] = dict(
    place='a sunny street in the centre of A Coruña, Spain, with white glass balconies (galerías)', who='woman',
    hero=('11', 'a khaki utility jacket over a long floral print midi dress'),
    banner=(None, 'the inside of a women\'s fashion boutique in A Coruña with pink walls, rails of dresses and coats, a herringbone wooden floor and a large mirror, no people, no text'),
    prods=[('17', 'a beige leopard print blouse with a black midi skirt', 'Blusa de leopardo'),
           ('03', 'a leopard print jacket with a gold pleated wide midi skirt', 'Falda plisada dorada'),
           ('14', 'a black puffer jacket over a camel jumper with black barrel jeans', 'Plumífero negro'),
           ('16', 'a dark brown teddy fleece coat with buttons', 'Abrigo de borreguito'),
           ('22', 'a beige knit cardigan with gold buttons over a black top', 'Rebeca beige'),
           ('24', 'a long navy floral maxi dress with a brown handbag and a wide-brim hat', 'Vestido largo de flores')],
    l1=(None, 'a woman in a zebra print jacket, a black top and a white pearl necklace standing in a pink fashion boutique'),
    l2=(None, 'a bright women\'s fashion boutique with a pink curtain, rails of coats and dresses and a herringbone wooden floor'),
    cats=[('Blusas', 'p1'), ('Abrigos', 'p3'), ('Vestidos', 'p6')])

S['alemany'] = dict(
    place='a pedestrian shopping street in the centre of Mataró, Barcelona, Spain, with shops and trees', who='mature', still=True,
    hero=('15', 'a brown leather hobo handbag with a front pocket and a matching tan leather crossbody bag'),
    banner=('05', 'the inside of a bag and accessories shop with shelves full of leather handbags in brown, burgundy and black, a colourful painting on the wall and warm lights, no people, no text'),
    prods=[('07', 'a tan leather crossbody bag with a front zip pocket (flat lay)', 'Bandolera de piel'),
           ('12', 'a navy blue laptop backpack with a front zip pocket, plain without logos (flat lay)', 'Mochila azul'),
           ('04', 'a lilac hard-shell cabin suitcase with four wheels, plain without logos', 'Maleta de cabina'),
           ('19', 'a petrol blue nylon tote bag with leather handles (flat lay)', 'Bolso shopper'),
           ('10', 'a big rainbow coloured umbrella open on a street', 'Paraguas arcoíris'),
           ('13', 'a dark green silk scarf with a colourful floral print (flat lay)', 'Pañuelo de seda')],
    l1=(None, 'a woman holding a brown leather shoulder bag in a bright accessories shop full of handbags'),
    l2=('18', 'a black silk scarf with a colourful paisley pattern, close up'),
    cats=[('Bolsos', 'p1'), ('Mochilas', 'p2'), ('Maletas', 'p3')])

S['tretze-girona'] = dict(
    place='a narrow stone street in the old town of Girona, Spain, with arcades and old buildings', who='woman',
    hero=('12', 'a brown teddy fleece jacket over a blue shirt, a long brown coat and checked trousers'),
    banner=('19', 'the inside of a multibrand fashion boutique in Girona with mannequins in coats and knitwear, black lamps, rails of clothes and a light floor, no people, no text'),
    prods=[('04', 'a dark brown wool blazer over a light blue shirt', 'Blazer marrón'),
           ('06', 'a mustard yellow knit jumper with a big grey checked scarf and a grey skirt', 'Jersey mostaza'),
           ('09', 'tan suede loafers lined with shearling and a tan suede crossbody bag (flat lay)', 'Mocasín forrado'),
           ('14', 'a cream knit cardigan over a black and white gingham blouse and black trousers', 'Rebeca crema'),
           ('18', 'a mustard yellow wool coat over a striped jumper and blue jeans', 'Abrigo mostaza'),
           ('22', 'a burgundy velvet top with dark khaki wide trousers', 'Top de terciopelo')],
    l1=('07', 'a woman in a long cream coat with a checked scarf and brown trousers walking in a boutique'),
    l2=('02', 'mannequins in a boutique with a leopard print shirt, a red jumper and checked trousers with slippers on the floor'),
    cats=[('Chaquetas', 'p1'), ('Punto', 'p2'), ('Calzado', 'p3')])

S['sucursal-moda'] = dict(
    place='a sunny street in Villarrobledo, Albacete, Spain, with white houses and a church tower', who='woman',
    hero=('12', 'a beige knit cardigan with a brown belt and a brown checked pleated midi skirt with a burgundy handbag'),
    banner=('06', 'the inside of a fashion and shoe shop with white lit shelves full of shoes, trainers and handbags, a light floor, no people, no text'),
    prods=[('03', 'a long-sleeve floral print midi dress in dark purple with black ankle boots', 'Vestido de flores'),
           ('07', 'a brown suede waistcoat with a printed silk scarf and a brown suede skirt', 'Chaleco de ante'),
           ('10', 'a ruffled off-the-shoulder floral blouse with dark brown wide trousers', 'Blusa de volantes'),
           ('14', 'a burgundy wrap blazer with puff sleeves and a belt and matching trousers', 'Traje burdeos'),
           ('13', 'a khaki military style knit jacket with gold buttons and camouflage trousers', 'Chaqueta militar'),
           ('09', 'a black lace long-sleeve maxi dress', 'Vestido de encaje')],
    l1=('16', 'a woman in a red checked shirt and brown trousers in a bright boutique with red coats on rails'),
    l2=('22', 'white lit shelves with sandals, espadrilles and trainers in many colours in a shoe shop'),
    cats=[('Vestidos', 'p1'), ('Chaquetas', 'p2'), ('Blusas', 'p3')])

S['uomo-palma'] = dict(
    place='a sunny street in the centre of Palma de Mallorca, Spain, with sandstone buildings and palm trees', who='man',
    hero=('06', 'a tan suede shearling-lined jacket over a white t-shirt and blue jeans on a man'),
    banner=('10', 'the inside of a premium menswear shop with rails of shirts and jackets, shelves with folded jumpers and an orange overshirt on display, white walls, no people, no text'),
    prods=[('04', 'a navy wool overcoat on a hanger', 'Abrigo azul marino'),
           ('12', 'a camel wool overcoat on a hanger', 'Abrigo camel'),
           ('09', 'a green and white floral print men\'s shirt on a hanger', 'Camisa estampada'),
           ('03', 'brown leather brogue shoes with a white sole (flat lay)', 'Zapato de piel'),
           ('21', 'a brown and cream houndstooth wool blazer on a hanger', 'Americana de pata de gallo'),
           ('07', 'navy suede and brown suede desert boots (flat lay)', 'Botín de ante')],
    l1=('14', 'a man in a cream knit jumper, dark jeans and white trainers sitting in a menswear shop'),
    l2=('08', 'three men\'s suits in navy, black and grey on mannequins in a shop window at night'),
    cats=[('Abrigos', 'p1'), ('Camisas', 'p3'), ('Calzado', 'p4')])

S['wilco'] = dict(
    place='a street in the centre of Vitoria-Gasteiz, Spain, with elegant stone buildings and glass balconies', who='woman',
    hero=('12', 'a long khaki green quilted puffer coat with a hood and a black shoulder bag'),
    banner=(None, 'the inside of a modern concept store in Vitoria with rails of coats and knitwear, mannequins, warm wooden shelves and a concrete floor, no people, no text'),
    prods=[('10', 'a rust red long quilted puffer coat', 'Plumífero rojo'),
           ('08', 'a brown oversized quilted puffer jacket with a high collar', 'Plumífero marrón'),
           ('06', 'a long olive green hooded parka', 'Parka verde'),
           ('09', 'brown suede moccasin boat shoes with laces, hanging side by side (flat lay)', 'Náutico de ante'),
           ('15', 'a grey checked tweed blazer with grey pinstripe wide trousers', 'Blazer de tweed'),
           ('20', 'a brown teddy fleece jacket with a red checked midi skirt and a hat', 'Chaqueta de borreguito')],
    l1=('19', 'a man in a camel trench coat over a brown jumper and dark trousers on a city street'),
    l2=('16', 'a grey soft knit jumper with a long pendant necklace with a turquoise stone, close up'),
    cats=[('Abrigos', 'p1'), ('Calzado', 'p4'), ('Blazers', 'p5')])

S['nud-madrid'] = dict(
    place='an elegant street in the Salamanca district of Madrid, Spain, with classic stone buildings and trees', who='woman',
    hero=('10', 'a pink, brown and burgundy plaid wool coat over a pink shirt and burgundy trousers with a burgundy leather bag'),
    banner=(None, 'the inside of an elegant multibrand boutique in Madrid with white walls, rails of shirts, coats and knitwear in burgundy, olive and camel tones, a wooden floor, no people, no text'),
    prods=[('03', 'an ivory pleated cotton shirt with burgundy trousers and a burgundy leather bucket bag', 'Camisa marfil'),
           ('09', 'a green and yellow striped knit jumper with burgundy trousers and burgundy flats', 'Jersey de rayas'),
           ('05', 'a pink and brown checked shirt with colourful floral embroidery', 'Camisa bordada'),
           ('14', 'two leather drawstring bucket bags, one burgundy and one olive green', 'Bolso saco'),
           ('19', 'a camel knit cardigan jacket over a white shirt and brown trousers', 'Chaqueta de punto'),
           ('21', 'a navy and burgundy checked short jacket with navy trousers and burgundy loafers', 'Chaqueta de cuadros')],
    l1=('07', 'a woman in a long navy wool coat over a white shirt and burgundy trousers'),
    l2=('08', 'a woven straw basket bag full of dried orange and brown hydrangeas, close up'),
    cats=[('Camisas', 'p1'), ('Punto', 'p2'), ('Bolsos', 'p4')])

S['ulldelavila'] = dict(
    place='a cobbled street in the medieval old town of Montblanc, Tarragona, Spain, with stone buildings', who='curvy',
    hero=('17', 'a bright orange oversized knit jumper over a black top and black trousers'),
    banner=('18', 'the inside of a cosy women\'s fashion shop in an old stone building with an arched ceiling, rails of knitwear and colourful clothes, warm lights, no people, no text'),
    prods=[('08', 'a beige short-sleeve knit jumper over a long brown linen dress with a green beaded necklace', 'Jersey beige'),
           ('20', 'a black and white striped oversized knit cardigan over a black top and black trousers with a long necklace', 'Rebeca de rayas'),
           (None, 'a grey wool oversized coat with wide lapels over a black jumper', 'Abrigo gris'),
           (None, 'a red and white striped oversized jumper with dark jeans', 'Jersey marinero'),
           (None, 'a leopard print oversized shirt over a black top and black wide trousers', 'Camisa de leopardo'),
           ('11', 'a light grey knitted triangle scarf worn over a black lace top', 'Chal de punto')],
    l1=(None, 'a curvy woman in her forties in a long black cardigan, a striped top and black trousers smiling in a colourful fashion shop'),
    l2=(None, 'a shop window in an old stone arch with knitwear, scarves and colourful bags on display'),
    cats=[('Punto', 'p1'), ('Abrigos', 'p3'), ('Camisas', 'p5')])

S['laazo-80'] = dict(
    place='a sunny street in the centre of Murcia, Spain, with elegant buildings and palm trees', who='woman',
    hero=('16', 'a burgundy faux fur coat over a burgundy dress'),
    banner=('04', 'the inside of a big bright fashion boutique for women and men in Murcia with white walls, rails of coats and shirts, tables with folded jumpers in many colours, no people, no text'),
    prods=[('05', 'a burgundy and cream striped satin blouse with burgundy trousers', 'Blusa de rayas'),
           ('08', 'a burgundy and white floral print wrap midi dress', 'Vestido estampado'),
           ('14', 'a cream faux fur jacket with a brown belt over a brown lace midi dress', 'Chaqueta de pelo crema'),
           ('15', 'a brown jumper with white floral embroidery and brown trousers', 'Jersey bordado'),
           ('17', 'a beige corduroy overshirt jacket with buttons on a man', 'Sobrecamisa de pana'),
           ('06', 'a navy cable-knit turtleneck jumper on a man', 'Jersey de ochos')],
    l1=('02', 'a man in a navy suit and light blue shirt in a menswear shop with blazers on display'),
    l2=('19', 'a woman in a long brown faux fur coat in a bright boutique'),
    cats=[('Mujer', 'p1'), ('Abrigos', 'p3'), ('Hombre', 'p5')])

S['space-baricentro'] = dict(
    place='a big modern shopping centre near Barcelona, Spain, with glass and bright shop fronts', who='woman',
    hero=('24', 'a brown faux leather belted jacket over a black turtleneck with black trousers'),
    banner=('01', 'the front of a women\'s fashion shop inside a shopping centre with a glass window, mannequins and racks of clothes, warm lights, no people, no text'),
    prods=[('02', 'a black one-shoulder fitted midi dress', 'Vestido asimétrico'),
           ('08', 'a brown and pink argyle knit jumper with a brown pencil skirt', 'Jersey de rombos'),
           ('12', 'a black and white patterned blouse with a black pleated mini skirt', 'Blusa estampada'),
           ('15', 'a brown checked mini skirt with a white top and a long brown cardigan', 'Falda de cuadros'),
           ('16', 'a pale yellow V-neck jumper with black faux leather trousers', 'Jersey amarillo'),
           ('23', 'a black and beige plaid cropped shirt jacket with a black pleated skirt', 'Sobrecamisa de cuadros')],
    l1=('21', 'a woman in a burgundy satin top and black faux leather wide trousers in a fashion shop'),
    l2=('13', 'a white and gold glitter sneaker shoe with a chunky sole held in a hand, plain without logos'),
    cats=[('Vestidos', 'p1'), ('Punto', 'p2'), ('Faldas', 'p4')])

S['mediavilla-calzados'] = dict(
    place='a sunny street in the Triana neighbourhood of Sevilla, Spain, with colourful houses and orange trees', who='woman', still=True,
    hero=('01', 'a red silk manila shawl (mantón) with big embroidered flowers and long red fringes, spread open'),
    banner=('12', 'the inside of a traditional shoe and accessories shop in Sevilla with wooden shelves full of colourful handbags and shoes, warm lights, no people, no text'),
    prods=[('15', 'a brown silk manila shawl with cream embroidered flowers and long fringes (flat lay)', 'Mantón bordado marrón'),
           ('17', 'red, blue and black embroidered silk manila shawls hanging on a wall', 'Mantones de Manila'),
           ('04', 'navy blue suede lace-up ankle boots for women (flat lay)', 'Botín de ante'),
           ('03', 'grey and black lace-up trainers with a chunky white sole, plain without logos', 'Deportiva gris'),
           ('13', 'small leather handbags in orange, white and pale blue on wooden shelves', 'Bolso de mano'),
           ('24', 'a big cream and orange flamenco hair flower (flat lay)', 'Flor de flamenca')],
    l1=('19', 'a woman in a white polka dot flamenco dress with a red embroidered shawl at a fair'),
    l2=('11', 'a red embroidered manila shawl draped on a staircase, close up'),
    cats=[('Mantones', 'p1'), ('Calzado', 'p3'), ('Complementos', 'p5')])

S['laura-santiago'] = dict(
    place='a sunny white street in a town in Andalusia, Spain, with orange trees', who='woman',
    hero=('04', 'three long belted wool coats in khaki green, cream and black'),
    banner=(None, 'the inside of a bright women\'s fashion shop with rails of coats, jumpers and trousers, dried pampas grass, a wooden floor and white walls, no people, no text'),
    prods=[('09', 'faux leather belted jackets in brown, burgundy and black', 'Chaqueta de polipiel'),
           ('12', 'a long purple houndstooth double-breasted coat on a hanger', 'Abrigo de pata de gallo'),
           ('16', 'a purple blazer with patterned purple trousers', 'Traje morado'),
           ('17', 'satin halter neck blouses in lime green, brown and cream with striped jeans', 'Camisa satinada'),
           ('22', 'triangle scarves with geometric prints and fringes in mustard, green and red (flat lay)', 'Pañuelo de flecos'),
           ('24', 'short faux fur jackets in black, burgundy and taupe', 'Abriguito de pelo')],
    l1=('21', 'a woman in a striped knit jacket and khaki green balloon trousers with heels'),
    l2=('14', 'soft fleece jogger trousers in brown, cream and black on hangers'),
    cats=[('Abrigos', 'p1'), ('Trajes', 'p3'), ('Complementos', 'p5')])

S['seville-chic'] = dict(
    place='a sunny white street in El Cuervo de Sevilla, Spain, with orange trees and white houses', who='woman',
    hero=('18', 'a long khaki parka with a big brown faux fur collar over khaki trousers'),
    banner=(None, 'the inside of a colourful multibrand fashion shop in Andalusia with rails full of bright jumpers, coats and dresses, a grey round pouf, a light wooden floor and mirrors, no people, no text'),
    prods=[('01', 'an orange and black tiger print faux fur coat', 'Abrigo de tigre'),
           ('08', 'a pink and brown striped knit jumper with brown wide trousers', 'Jersey de rayas'),
           ('09', 'a bright yellow chunky knit jumper with a big cowl collar and grey wide trousers', 'Jersey amarillo'),
           ('12', 'a cream sequin jumper with fluffy cuffs and a cream sequin midi skirt', 'Conjunto de lentejuelas'),
           ('16', 'a light blue tweed jacket with a jewelled trim and wide dark jeans', 'Chaqueta de tweed'),
           ('03', 'a silver sequin zip jacket with matching silver trousers', 'Conjunto plateado')],
    l1=('02', 'a woman in a khaki trench coat over a red and green striped jumper and khaki trousers in a fashion shop'),
    l2=('21', 'a rust orange knitted triangle shawl with a ruffle border over a khaki shirt, close up'),
    cats=[('Abrigos', 'p1'), ('Punto', 'p2'), ('Fiesta', 'p4')])

S['victoria-shop'] = dict(
    place='a sunny white street in Cantillana, Sevilla, Spain, with orange trees', who='woman',
    hero=('19', 'a black belted faux leather trench coat with black trousers and burgundy boots'),
    banner=('01', 'the inside of a women\'s fashion shop with rails of coats, jackets and knitwear, wooden shelves with boots, a light floor, no people, no text'),
    prods=[('02', 'a black faux leather sleeveless top with a black mini skirt and black knee boots', 'Conjunto de polipiel'),
           ('04', 'a black and white checked shirt jacket with black faux leather shorts and knee boots', 'Sobrecamisa de cuadros'),
           ('06', 'a navy and white striped knit jumper with light blue baggy jeans', 'Jersey de rayas'),
           ('10', 'black croc-embossed knee-high boots with a stiletto heel (flat lay)', 'Bota alta de coco'),
           ('11', 'dark brown slouchy faux leather ankle boots with a stiletto heel (flat lay)', 'Botín arrugado'),
           ('17', 'a long off-the-shoulder floral print maxi dress in dark teal and rust', 'Vestido largo de flores')],
    l1=('21', 'a woman in a light blue denim shirt with black shorts and black knee boots in a fitting room'),
    l2=('15', 'rails of pink and cream printed pyjamas and blouses in a shop'),
    cats=[('Conjuntos', 'p1'), ('Punto', 'p3'), ('Botas', 'p4')])

S['islu-creaciones'] = dict(
    place='a sunny seafront promenade in Garrucha, Almería, Spain, with palm trees and the sea', who='woman',
    hero=('10', 'a fitted red flamenco dress with long sleeves, a red sheer shawl and red ruffles at the hem'),
    banner=(None, 'the inside of a flamenco dress boutique with rails of colourful ruffled flamenco dresses in red, turquoise and pink, shawls and flowers on display, a light floor, no people, no text'),
    prods=[('04', 'a red and black fitted flamenco dress with ruffled sleeves and a black shawl', 'Traje rojo y negro'),
           ('19', 'a white flamenco dress with black polka dots and big white ruffles', 'Traje de lunares'),
           ('15', 'a magenta purple flamenco dress with layered ruffles', 'Traje morado'),
           ('12', 'a black flamenco dress with a pink ruffled hem', 'Traje negro y rosa'),
           ('17', 'a pale aqua fitted ceremony dress with puff sleeves', 'Vestido de ceremonia'),
           ('23', 'a black off-the-shoulder flamenco dress with large ruffles', 'Traje negro')],
    l1=('14', 'a woman in a red flamenco dress with white fringed shawl twirling on a sunny terrace by the sea'),
    l2=('08', 'a light blue and white flamenco dress with a fringed shawl seen from behind, by the sea'),
    cats=[('Flamenca', 'p1'), ('Lunares', 'p2'), ('Ceremonia', 'p5')])

S['mandarina-palencia'] = dict(
    place='an arcaded street in the centre of Palencia, Spain, with stone columns and shops', who='mature',
    hero=('12', 'a brown reversible shearling-style jacket over a printed blouse and blue jeans'),
    banner=('01', 'the front of a women\'s fashion shop with a big window under the stone arcades of Palencia, mannequins and racks of clothes, no people, no text'),
    prods=[('02', 'a khaki green knit top and matching wide trousers set with a long pendant necklace', 'Conjunto verde'),
           ('03', 'a beige knit top and matching beige trousers set with a long necklace', 'Conjunto beige'),
           ('07', 'a long tan suede coat with a fur collar over a white top', 'Abrigo de ante'),
           ('11', 'a multicoloured zigzag knit cardigan over a black top and dark green trousers', 'Rebeca de zigzag'),
           ('18', 'a black and white zebra print blouse with dark brown leather trousers', 'Blusa de cebra'),
           ('20', 'a red ruffled blouse with a paisley scarf and blue jeans', 'Blusa roja')],
    l1=('22', 'a woman in a white knit jumper with a patterned scarf and beige trousers in a boutique'),
    l2=('09', 'reversible jackets in brown and camel tones on a rail in a boutique, close up'),
    cats=[('Conjuntos', 'p1'), ('Abrigos', 'p3'), ('Blusas', 'p5')])

S['charlotte-odil'] = dict(
    place='a sunny street in Majadahonda, Madrid, Spain, with modern brick buildings and trees', who='mature',
    hero=('17', 'a cream and rust leaf print cape jacket with a black panel over black trousers'),
    banner=('16', 'the inside of an elegant boutique with a black and white checkerboard floor, rails of blouses and jackets, a marble fireplace with flowers, no people, no text'),
    prods=[('02', 'a black and white blazer with gold buttons and black trousers', 'Chaqueta bicolor'),
           ('09', 'a rust orange off-the-shoulder knit jumper with a cream knit midi skirt', 'Jersey teja'),
           ('15', 'a beige knit cardigan with brown embroidered details and a tan leather bag', 'Rebeca bordada'),
           ('18', 'a white floral print chiffon blouse with brown trousers', 'Blusa de flores'),
           ('19', 'a grey faux fur jacket with blue jeans and a red handbag', 'Chaqueta de pelo gris'),
           ('20', 'a camel knit midi dress with buttons and a wide brown belt', 'Vestido de punto')],
    l1=('05', 'a woman in a lilac knit top with a peplum and a lilac pleated skirt in an elegant boutique'),
    l2=('14', 'an elegant boutique with a black and white checkerboard floor, a round mirror and colourful clothes on display'),
    cats=[('Chaquetas', 'p1'), ('Punto', 'p2'), ('Blusas', 'p4')])

S['caruncho-kodina'] = dict(
    place='a granite stone street in the old town of Pontevedra, Spain, with arcades', who='none', still=True,
    hero=('22', 'a pair of handmade gold drop earrings with natural baroque pearls and small pink stones'),
    banner=(None, 'the inside of a small artisan jewellery workshop and shop in Pontevedra with a granite wall, a wooden workbench with tools and glass showcases with gold jewellery, warm light, no people, no text'),
    prods=[('01', 'a gold ring with a rectangular top set with three blue sapphires and small diamonds', 'Anillo de zafiros'),
           ('03', 'a pair of wavy gold earrings with small blue topaz stones', 'Pendientes de topacio'),
           ('07', 'a thin gold bangle bracelet with small knots', 'Pulsera de nudos'),
           ('14', 'a wide gold ring with a big brilliant-cut white stone and small diamonds', 'Sortija de brillantes'),
           ('17', 'a gold ring with a big oval green turquoise stone and a small pink stone', 'Anillo de turquesa'),
           ('19', 'a gold cuff bracelet with engraved details and a small green emerald', 'Brazalete grabado')],
    l1=('09', 'two thin gold bangles with small stones on a woman\'s wrist, close up'),
    l2=('11', 'a gold bracelet with big white baroque pearls on a woman\'s wrist, close up'),
    cats=[('Anillos', 'p1'), ('Pendientes', 'p2'), ('Pulseras', 'p3')])

S['eme-flamenca'] = dict(
    place='a sunny traditional street in Sevilla, Spain, with orange walls, iron balconies and a wooden door', who='woman',
    hero=('11', 'a navy flamenco dress with white polka dots and ruffles with a big green embroidered fringed shawl'),
    banner=(None, 'the inside of a flamenco fashion atelier in Madrid with rails of colourful ruffled flamenco dresses, embroidered shawls hanging on the wall, a big mirror and a wooden floor, no people, no text'),
    prods=[('01', 'a fuchsia flamenco dress with black polka dots and a beige embroidered fringed shawl', 'Traje fucsia'),
           ('04', 'a teal blue flamenco dress with ruffles and a teal fringed shawl', 'Traje turquesa'),
           ('10', 'a black flamenco dress with white polka dots and white ruffle trims', 'Traje de lunares'),
           ('13', 'a royal blue flamenco dress with white ruffle trims and a colourful embroidered shawl', 'Traje azul'),
           ('09', 'a big beige silk shawl with long fringes worn over a dress', 'Mantoncillo beige'),
           ('23', 'a red embroidered silk shawl with flowers over a white ruffled flamenco dress', 'Mantón rojo bordado')],
    l1=('06', 'a woman in a red and white flamenco dress at the Seville fair next to a horse carriage'),
    l2=('20', 'a burgundy embroidered silk shawl with flowers and long fringes, close up'),
    cats=[('Trajes', 'p1'), ('Lunares', 'p3'), ('Mantones', 'p5')])

S['baul-de-mariquilla'] = dict(
    place='a sunny square in the old town of Sevilla, Spain, with orange walls and orange trees', who='woman', still=True,
    hero=('17', 'an antique pink silk manila shawl with colourful embroidered flowers and long pink fringes, displayed on a stand'),
    banner=(None, 'the inside of a small antiques and vintage accessories shop with embroidered silk shawls on the walls, glass showcases with old necklaces and earrings, warm light, no people, no text'),
    prods=[('05', 'a cream embroidered silk shawl with burgundy pompom fringes on a stand', 'Mantoncillo crema'),
           ('12', 'a black silk shawl with big white embroidered flowers (flat lay)', 'Mantón negro bordado'),
           ('19', 'an orange embroidered silk shawl draped on a stand, close up', 'Mantón naranja'),
           ('04', 'a long red coral bead necklace on a stand', 'Collar de coral'),
           ('06', 'a long green jade bead necklace with a carved white pendant (flat lay)', 'Collar de jade'),
           ('18', 'an antique silver mesh evening bag with a frame clasp (flat lay)', 'Bolso de malla')],
    l1=(None, 'a smiling woman with long hair wearing vintage red and turquoise drop earrings, in a sunny street'),
    l2=('03', 'a close up of a pink silk shawl with large embroidered flowers in pink, green and cream'),
    cats=[('Mantones', 'p1'), ('Collares', 'p4'), ('Bolsos', 'p6')])

S['fran-gamez'] = dict(
    place='a sunny street in Écija, Sevilla, Spain, with baroque church towers and orange trees', who='woman',
    hero=('02', 'a white flamenco dress with black polka dots and black ruffles'),
    banner=(None, 'the inside of a flamenco fashion designer\'s atelier in Écija with rails of colourful ruffled flamenco dresses, fabric rolls, a sewing table and a big mirror, no people, no text'),
    prods=[('04', 'a red fitted flamenco dress with white and pink ruffles', 'Traje rojo y rosa'),
           ('08', 'a red flamenco dress with a white fringed shawl', 'Traje rojo'),
           ('12', 'a white flamenco dress with big white ruffles', 'Traje blanco'),
           ('17', 'a red flamenco dress with lilac ruffled sleeves and a lilac shawl', 'Traje rojo y lila'),
           ('21', 'a white flamenco dress with black embroidered details and a long ruffled skirt', 'Traje bordado'),
           ('24', 'a navy blue flamenco dress with a red fringed shawl', 'Traje azul marino')],
    l1=('23', 'a woman in a white flamenco dress with red polka dots and a red shawl at the fair'),
    l2=(None, 'colourful ruffled flamenco dresses on mannequins in a designer atelier, close up of the ruffles'),
    cats=[('Lunares', 'p1'), ('Lisos', 'p3'), ('Bordados', 'p5')])

S['de-flores-y-floreros'] = dict(
    place='a sunny street in the Ruzafa neighbourhood of Valencia, Spain, with colourful facades and balconies', who='woman', still=True,
    hero=('04', 'a pair of mustard yellow leather pointed flat shoes with blue gingham bows, and a pair of pale blue pointed flats'),
    banner=('05', 'the inside of a charming handmade shoe shop in Valencia with wooden shelves full of colourful shoes, dried flowers and a vintage wooden cart, no people, no text'),
    prods=[('16', 'a pointed flat shoe in a colourful floral print fabric with a small strap (flat lay)', 'Bailarina de flores'),
           ('17', 'purple velvet pointed flats with a big pink bow, worn with wide beige trousers', 'Bailarina con lazo'),
           ('08', 'olive green leather ankle boots with mustard studded details', 'Botín verde'),
           ('14', 'grey suede pointed ankle boots with long fringes and a kitten heel', 'Botín de flecos'),
           ('20', 'a glitter pointed shoe with pink feathers, worn with dark wide trousers', 'Zapato de plumas'),
           ('22', 'mint green and tan leather lace-up oxford shoes on a wooden shelf', 'Blucher de colores')],
    l1=('07', 'a woman wearing blue and silver pointed lace-up shoes with wide light blue jeans, close up of the feet'),
    l2=('13', 'a woman wearing tiger stripe woven leather flat shoes with grey jeans, close up of the feet'),
    cats=[('Bailarinas', 'p1'), ('Botines', 'p3'), ('Blucher', 'p6')])

S['presintown'] = dict(
    place='a sunny street in the centre of Lorca, Murcia, Spain, with baroque facades and balconies', who='man',
    hero=('19', 'a navy blue tailored suit with a light blue shirt and a patterned tie on a mannequin'),
    banner=(None, 'the inside of a classic menswear shop in Lorca with dark wooden shelves full of folded shirts and jumpers, rails of jackets and suits and warm lights, no people, no text'),
    prods=[(None, 'a navy blue tailored blazer on a hanger', 'Americana azul'),
           (None, 'a light blue Oxford cotton shirt for men, folded (flat lay)', 'Camisa Oxford'),
           (None, 'a camel cable-knit crew neck jumper for men, folded (flat lay)', 'Jersey de ochos'),
           (None, 'beige cotton chino trousers for men, folded (flat lay)', 'Chino beige'),
           (None, 'brown suede loafers for men (flat lay)', 'Mocasín de ante'),
           (None, 'a dark green quilted gilet for men on a hanger', 'Chaleco acolchado')],
    l1=(None, 'a man in his forties wearing a white linen shirt, beige chinos and brown loafers in a menswear shop'),
    l2=('21', 'dark wooden shelves with folded shirts and jumpers in a classic menswear shop, close up'),
    cats=[('Americanas', 'p1'), ('Camisas', 'p2'), ('Punto', 'p3')])

S['deluxe-fashion'] = dict(
    place='a sunny street in Fuente Álamo, Murcia, Spain, with white houses and palm trees', who='woman',
    hero=('18', 'an orange faux suede jacket with a big brown faux fur collar'),
    banner=(None, 'the inside of a bright fashion and shoe shop with pink walls, rails of jumpers and coats, shelves with boots and bags and green plants, no people, no text'),
    prods=[('01', 'tan suede short ankle boots lined with faux fur (flat lay)', 'Botín forrado'),
           ('04', 'burgundy suede pointed slingback heels (flat lay)', 'Zapato destalonado'),
           ('09', 'brown and black leather knee-high riding boots (flat lay)', 'Bota alta de montar'),
           ('10', 'a burgundy and black paisley velvet blouse on a hanger', 'Blusa de terciopelo'),
           ('08', 'a burgundy long knit cardigan with buttons on a hanger', 'Rebeca burdeos'),
           ('22', 'a brown and white polka dot dress on a hanger', 'Vestido de lunares')],
    l1=(None, 'a woman in a checked blazer, a white blouse and black trousers with brown knee boots in a pink boutique'),
    l2=('21', 'cosy white slippers with a red Christmas pattern, close up'),
    cats=[('Calzado', 'p1'), ('Blusas', 'p4'), ('Punto', 'p5')])

S['selene-moda'] = dict(
    place='a street in the centre of Gernika, Bizkaia, Spain, with traditional Basque buildings and green hills', who='mature',
    hero=('12', 'a burgundy quilted puffer jacket with a hood over a white jumper and black trousers'),
    banner=('04', 'the inside of a fashion and bag shop with lit white shelves full of handbags, stacks of boxes and rails of clothes, warm light, no people, no text'),
    prods=[('02', 'a cream fitted jacket with black buttons', 'Chaqueta crema'),
           ('03', 'a beige and brown checked faux fur jacket with brown trousers', 'Chaqueta de pelo'),
           ('05', 'a mustard yellow corduroy jacket over a khaki jumper with checked trousers', 'Chaqueta de pana'),
           ('09', 'a cream quilted gilet over a striped knit jumper and beige trousers', 'Chaleco acolchado'),
           ('10', 'a burgundy fitted top with brown checked bermuda shorts', 'Bermuda de cuadros'),
           ('06', 'a long navy quilted puffer coat with a fur hood', 'Plumífero azul')],
    l1=('18', 'a woman in a khaki green jumper and checked trousers in a bag shop'),
    l2=(None, 'lit white shelves full of leather handbags in burgundy, black and brown, close up'),
    cats=[('Chaquetas', 'p1'), ('Chalecos', 'p4'), ('Abrigos', 'p6')])

S['kokomoda'] = dict(
    place='a sunny white street in Jerez de la Frontera, Cádiz, Spain, with orange trees and iron balconies', who='woman',
    hero=('02', 'a chocolate brown satin blouse with a pussy bow, wide camel trousers, a braided belt and a woven leather tote bag'),
    banner=(None, 'the inside of an elegant women\'s fashion shop in Jerez with rails of blouses, jackets and trousers, a velvet armchair, dried flowers and a light floor, no people, no text'),
    prods=[('01', 'a cream fitted top with a sweetheart neckline and a matching cream mini skirt', 'Conjunto crema'),
           ('04', 'a dark brown military style knit jacket with gold braid and matching trousers', 'Conjunto militar'),
           ('05', 'a burgundy pleated midi dress with a wide fringed belt', 'Vestido plisado'),
           ('12', 'a brown faux leather belted jacket', 'Chaqueta de polipiel'),
           ('13', 'dark brown leather penny loafers (flat lay)', 'Mocasín chocolate'),
           ('24', 'a khaki faux leather belted short trench jacket with blue jeans', 'Cazadora de polipiel')],
    l1=('18', 'a mannequin in a blue shirt, a brown checked long coat and blue jeans with a brown belt in a boutique'),
    l2=('20', 'wide jogger trousers with a contrast waistband in brown, grey, khaki, black and beige'),
    cats=[('Conjuntos', 'p1'), ('Vestidos', 'p3'), ('Chaquetas', 'p4')])

S['mar-de-caprichos'] = dict(
    place='a sunny street in La Unión, Murcia, Spain, with old mining town buildings and palm trees', who='woman',
    hero=('12', 'a dark brown off-the-shoulder fitted midi dress with a flared skirt'),
    banner=(None, 'the inside of a bright women\'s fashion boutique with rails of dresses and blouses in burgundy and brown tones, dried pampas grass, a wooden floor and white curtains, no people, no text'),
    prods=[('02', 'a navy denim waistcoat with gold buttons over a white shirt and wide blue jeans', 'Chaleco vaquero'),
           ('03', 'a burgundy striped blouse with a ruffled yoke and brown wide jeans', 'Blusa de volantes'),
           ('06', 'a cream military style jacket with gold buttons and blue jeans', 'Chaqueta militar'),
           ('08', 'a brown dress with a burgundy ruffled collar and a belt', 'Vestido de volante'),
           ('13', 'a burgundy off-the-shoulder fitted midi dress with a flared skirt', 'Vestido burdeos'),
           ('16', 'a navy and white striped hooded knit jumper with blue jeans', 'Jersey de rayas')],
    l1=('09', 'a woman in a cream jumper with studs and a long brown wrap skirt'),
    l2=('10', 'a soft beige knit jumper and matching jogger trousers set with white trainers'),
    cats=[('Vestidos', 'p4'), ('Chaquetas', 'p1'), ('Punto', 'p6')])

S['moda-sabana'] = dict(
    place='a sunny street in Sant Andreu de la Barca, Barcelona, Spain, with modern buildings and trees', who='woman',
    hero=('03', 'a teal green draped wrap midi party dress'),
    banner=('02', 'the inside of a fashion and party dress shop with shelves full of handbags, rails of colourful evening dresses and pink curtains, no people, no text'),
    prods=[('02', 'a fuchsia backless satin evening dress', 'Vestido de fiesta fucsia'),
           ('14', 'a black and white striped knit jumper with blue jeans', 'Jersey de rayas'),
           ('16', 'a cream long trench coat with a black panel collar', 'Gabardina crema'),
           ('22', 'a brown chiffon cape top with matching wide trousers', 'Conjunto capa'),
           ('23', 'a black cropped jacket with gold buttons over a white top', 'Chaqueta de botones'),
           ('24', 'a taupe suede jacket with a faux fur collar', 'Chaqueta de ante')],
    l1=('20', 'a woman in a cream knit two-piece set of cardigan and wide trousers with white trainers'),
    l2=('15', 'a brown knit jumper with bow details on the sleeves, close up'),
    cats=[('Fiesta', 'p1'), ('Punto', 'p2'), ('Chaquetas', 'p5')])

S['la-piconela'] = dict(
    place='a sunny white street in an Andalusian town, Spain, with orange walls, iron window grilles and flower pots', who='woman',
    hero=('12', 'a white flamenco dress with red ruffles and a red embroidered shawl'),
    banner=('15', 'the inside of a flamenco fashion shop with mannequins in colourful flamenco dresses in red, blue and white, embroidered shawls and a light floor, no people, no text'),
    prods=[('01', 'an emerald green flamenco dress with lime green ruffles and a green fringed shawl', 'Traje verde'),
           ('03', 'a white flamenco dress with big black polka dots and ruffled sleeves', 'Traje de lunares'),
           ('08', 'a burgundy silk shawl with big pink embroidered roses and long fringes (flat lay)', 'Mantón bordado'),
           ('14', 'a dusty pink flamenco dress with small polka dots and a cream fringed shawl on a mannequin', 'Traje rosa'),
           ('16', 'a cream silk shawl with burgundy embroidery and long fringes on a mannequin', 'Mantoncillo crema'),
           ('06', 'big flamenco hair flowers in burgundy, red and pink with purple hoop earrings (flat lay)', 'Flores y pendientes')],
    l1=('24', 'a woman in a pale blue flamenco dress with white polka dots on a sunny terrace with olive hills behind'),
    l2=('09', 'flamenco dresses with embroidered shawls on mannequins under a row of big flowers, close up'),
    cats=[('Trajes', 'p1'), ('Mantones', 'p3'), ('Complementos', 'p6')])

S['maria-palmero'] = dict(
    place='a sunny elegant street in the centre of Zaragoza, Spain, with classic buildings and iron balconies', who='woman',
    hero=('01', 'a long camel wool coat over a brown checked midi skirt'),
    banner=(None, 'the inside of an elegant women\'s fashion boutique in Zaragoza with rails of coats, knitwear and plaid skirts, a wooden floor and warm lights, no people, no text'),
    prods=[('02', 'a yellow and brown plaid shirt jacket with grey wide trousers', 'Sobrecamisa de cuadros'),
           ('09', 'a black and white striped knit jumper with grey trousers', 'Jersey de rayas'),
           ('12', 'a purple and pink striped knit jumper with a purple scarf', 'Jersey morado'),
           ('17', 'a brown pinstripe waistcoat and matching wide trousers with a brown blazer', 'Traje de raya diplomática'),
           ('18', 'a cream knit jumper with black toggle buttons and a black skirt', 'Jersey con alamares'),
           ('24', 'a grey and green checked cropped jacket with matching wide trousers', 'Conjunto de cuadros')],
    l1=('19', 'a woman in a black and white checked blazer, a white shirt and checked wide trousers on a city street'),
    l2=('16', 'a brown checked shirt with a wide brown leather belt and a suede bag, close up'),
    cats=[('Abrigos', 'p1'), ('Punto', 'p2'), ('Trajes', 'p4')])

S['de-lunares-y-volantes'] = dict(
    place='a sunny square in Sevilla, Spain, with an old white wall, a fountain and orange trees', who='woman',
    hero=('10', 'a fitted red flamenco dress with long ruffled sleeves and a red ruffled hem'),
    banner=(None, 'the inside of a flamenco dress atelier with rails of colourful ruffled flamenco dresses, fabric rolls, embroidered shawls and a big mirror, no people, no text'),
    prods=[('02', 'a royal blue fitted flamenco dress with ruffled sleeves and a ruffled hem', 'Traje azul'),
           ('04', 'a fuchsia flamenco dress with ruffles and a teal fringed shawl', 'Traje fucsia'),
           ('12', 'a short white flamenco dress with layered ruffles and puff sleeves', 'Traje blanco corto'),
           ('13', 'a rust brown fitted flamenco dress with long sleeves and a flared ruffled hem', 'Traje teja'),
           ('18', 'a mint green flamenco dress with white polka dots', 'Traje verde agua'),
           ('24', 'a white flamenco dress with red polka dots and big red ruffles', 'Traje de lunares rojo')],
    l1=('23', 'a woman in a magenta blouse with ruffled sleeves and black wide trousers, a flamenco look'),
    l2=('16', 'colourful flamenco skirts in red, white and green with embroidered shawls, close up'),
    cats=[('Trajes', 'p1'), ('Lunares', 'p5'), ('Cortos', 'p3')])

S['teresa-b'] = dict(
    place='a sunny white street in the old town of Badajoz, Spain, with an elegant shop front and potted plants', who='woman', still=True,
    hero=('23', 'three half-moon leather bags in black, chocolate brown and tan stacked as a sculpture'),
    banner=(None, 'the inside of an elegant accessories boutique in Badajoz with white walls, wooden shelves with handbags, jewellery stands and silk scarves, warm light, no people, no text'),
    prods=[('16', 'an olive green half-moon leather bag with a gold clasp (flat lay)', 'Bolso media luna'),
           ('17', 'long drop earrings with oval orange carnelian stones set in gold', 'Pendientes de cornalina'),
           ('08', 'a layered thin gold necklace with small pearls', 'Collar de perlas'),
           ('14', 'a tan woven leather shoulder bag', 'Bolso trenzado'),
           ('19', 'a dark brown velvet pouch clutch bag', 'Bolso de terciopelo'),
           ('03', 'colourful handwoven round hand fans with wooden handles (flat lay)', 'Abanicos tejidos')],
    l1=('24', 'a woman in a grey knit cardigan with a burgundy paisley silk scarf in a boutique'),
    l2=('21', 'a beaded bird brooch in blue and gold held in a hand with dried red flowers behind, close up'),
    cats=[('Bolsos', 'p1'), ('Joyas', 'p2'), ('Regalos', 'p6')])

S['naif-cuir'] = dict(
    place='a rustic stone village in the Alto Tajo, Guadalajara, Spain, with old stone walls and autumn trees', who='woman', still=True,
    hero=('13', 'a big olive green leather half-moon bag with a red and orange ruffled leather trim, on a rustic wooden bench'),
    banner=('04', 'a rustic leather artisan atelier with a sewing machine, colourful leather pieces, stone walls and wooden beams, no people, no text'),
    prods=[('01', 'a black leather half-moon bag with a multicoloured striped leather trim (flat lay)', 'Bolso media luna'),
           ('03', 'small round leather pouches in bright colour blocks with ruffled trims (flat lay)', 'Monedero de colores'),
           ('08', 'silver metallic and black and white striped leather clutch bags (flat lay)', 'Bolso plateado'),
           ('12', 'a small red and cream striped leather crossbody bag', 'Bandolera de rayas'),
           ('22', 'a leopard print leather clutch bag with a ruched top', 'Bolso de leopardo'),
           ('21', 'three leather half-moon bags with ruffled trims and long leather tassels hanging on a wooden beam', 'Bolso con borla')],
    l1=('19', 'a woman in a khaki jacket holding a red checked leather bag with a striped lining, close up'),
    l2=('05', 'a leather sewing machine in a rustic artisan workshop, close up'),
    cats=[('Bolsos', 'p1'), ('Monederos', 'p2'), ('Bandoleras', 'p4')])

S['ole-yo-santona'] = dict(
    place='a seaside street in Santoña, Cantabria, Spain, with the harbour and green mountains behind', who='mature',
    hero=('06', 'a long brown quilted puffer coat with a faux fur hood and cream trousers'),
    banner=(None, 'the inside of a cosy women\'s fashion shop in Cantabria with rails of coats and knitwear, shelves of colourful scarves and a wooden floor, no people, no text'),
    prods=[('01', 'a big burgundy fluffy knit scarf with a black top', 'Bufanda burdeos'),
           ('05', 'a brown quilted short puffer jacket with a faux fur hood', 'Chaquetón acolchado'),
           ('14', 'a mustard yellow cardigan with grey wide culottes', 'Rebeca mostaza'),
           ('15', 'a burgundy and cream argyle knit jumper with beige trousers', 'Jersey de rombos'),
           ('20', 'a cream Nordic pattern knit jumper with blue jeans', 'Jersey nórdico'),
           ('23', 'a burgundy leather slouchy shoulder bag (flat lay)', 'Bolso burdeos')],
    l1=('18', 'a woman in a camel blazer, a checked shirt and brown leather bermuda shorts on a street'),
    l2=('08', 'a stack of soft scarves in many colours, close up'),
    cats=[('Abrigos', 'p2'), ('Punto', 'p4'), ('Complementos', 'p1')])
