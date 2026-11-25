# Lote 46 (25/11/2026): 15 más del scrapeo del 23/11 (sel46.json), para enviar ese mismo día junto al lote 45, con la propuesta
# v42b + «Los números» (gen42.py) y la tienda «Editorial» (gen37a.py). Referencias NN = fotos de su Instagram
# (scratchpad l46/rf/<slug>/NN.jpg; en Flow, con la cara tapada: n<slug>-NN.jpg). Nunca referencias con menores
# (Rociera y Bohothai tienen fotos de niñas: fuera) ni con marcas o logos (Galerías Abreu vende Lacoste y Tommy: todo solo con texto, sin logos).

S['rociera'] = dict(
    place='a whitewashed patio in the old town of Córdoba, Spain, with blue flower pots on the walls and red geraniums', who='woman',
    hero=('03', 'a fuchsia flamenca dress with layered ruffled sleeves and a fitted mermaid skirt, with a teal embroidered silk shawl with long fringe and a teal flower in the hair'),
    banner=(None, 'the inside of a traditional flamenca dress workshop and boutique in Córdoba with rails of ruffled polka dot flamenca dresses, embroidered shawls on mannequins and a wooden sewing table, warm light, no people, no text'),
    prods=[('01', 'a fuchsia flamenca dress with ruffled sleeves and a long ruffled skirt, with a teal embroidered fringed shawl', 'Traje fucsia y mantón agua'),
           ('20', 'a red flamenca dress with a fitted body and a long ruffled mermaid skirt', 'Traje rojo canastero'),
           ('23', 'a pink polka dot flamenca dress with three white-trimmed ruffles on a dress form, with a turquoise embroidered shawl with fringe', 'Traje de lunares rosa'),
           ('25', 'a black flamenca dress with multicoloured polka dot ruffles on a dress form, with a pink fringed embroidered shawl', 'Traje negro de lunares'),
           ('27', 'a mint green silk shawl with black embroidered flowers and long black fringe, displayed on a dress form', 'Mantón bordado agua'),
           (None, 'a royal blue flamenca dress with small white polka dots and ruffled sleeves, with a red embroidered shawl', 'Traje azul klein')],
    l1=('02', 'a fuchsia flamenca dress with ruffled sleeves and a teal embroidered fringed shawl, leaning on a balcony railing under a stone arch'),
    l2=('22', 'a red silk shawl with colourful embroidered flowers and red fringe on a dress form, with a red bead necklace, in a flamenca shop'),
    cats=[('Trajes de flamenca', 'p1'), ('Canastero', 'p2'), ('Mantones', 'p5')])

S['modas-victorias'] = dict(
    place='a street in the centre of Córdoba, Spain, with orange trees and white houses', who='curvy',
    hero=('09', 'a long brown faux fur gilet over a cream jumper with beige wide trousers'),
    banner=(None, 'the inside of a bright neighbourhood fashion shop with white shelves full of jumpers and handbags, rails of coats and dresses, a grey wooden floor and a white folding screen, no people, no text'),
    prods=[('20', 'a red long-sleeved pleated chiffon midi dress with a matching belt', 'Vestido plisado rojo'),
           ('18', 'a brown satin blouse with puff sleeves and an olive green tiered midi skirt', 'Conjunto falda de volantes'),
           ('15', 'a blue and white striped shirt with a brown belt and a navy denim midi skirt', 'Camisa de rayas y falda vaquera'),
           ('24', 'a navy floral print wrap midi dress with long sleeves', 'Vestido de flores'),
           ('13', 'a pink and burgundy tweed jacket with burgundy straight trousers', 'Chaqueta de tweed'),
           ('10', 'a dark brown quilted puffer jacket with a hood', 'Plumífero chocolate')],
    l1=('04', 'a cream wrap jacket with a dark midi skirt and black boots'),
    l2=('06', 'an ivory knitted cape top with black wide trousers, in a shop with white shelves of handbags'),
    cats=[('Vestidos', 'p1'), ('Conjuntos', 'p2'), ('Abrigos', 'p6')])

S['boutique-marisa'] = dict(
    place='a street in the centre of Badalona, Spain, near the sea, with modernist buildings and balconies', who='mature',
    hero=('20', 'a long brown wool coat with an olive green scarf, and a long black quilted coat, with dark trousers'),
    banner=(None, 'the inside of a warm multibrand fashion boutique with a light wooden floor, wooden shelves and walls, rails of coats, knits and jeans and a wooden bench with folded jumpers, no people, no text'),
    prods=[('12', 'a brown and grey check oversized blazer over an ivory fluffy jumper, with a long wooden bead necklace', 'Blazer de cuadros'),
           ('11', 'an ivory fluffy mohair-style jumper with a long wooden bead necklace and dark brown trousers', 'Jersey crudo'),
           ('16', 'a cream oversized turtleneck knit jumper with grey wide trousers, holding a leopard print faux fur bag', 'Jersey de cuello alto'),
           ('03', 'brown shearling-lined clog shoes with a buckle on a thick black sole (flat lay)', 'Zuecos con borrego'),
           ('26', 'a brown suede jacket with a mandarin collar and wide blue jeans', 'Chaqueta de ante'),
           ('29', 'a black faux leather jacket with wide black jeans', 'Cazadora efecto piel')],
    l1=('04', 'a navy wool coat with a blue and red check scarf, wide blue jeans and a crossbody bag'),
    l2=('10', 'mannequins in a boutique window with a brown teddy jacket, a check blazer and wide trousers, and a wooden bench with folded scarves'),
    cats=[('Abrigos', 'p1'), ('Punto', 'p2'), ('Calzado', 'p4')])

S['udalaitz'] = dict(
    place='a street in the old town of Vitoria-Gasteiz, Spain, with stone buildings and glazed balconies', who='mature',
    hero=(None, 'a red cropped jacket with a voluminous royal blue taffeta midi skirt and long black gloves, on a plain warm beige background'),
    banner=(None, 'the outside of a small fashion boutique with a black painted wooden façade and two large windows showing mannequins in colourful voluminous skirts, with pots of yellow flowers by the door, no people, no text'),
    prods=[(None, 'a voluminous plum purple taffeta midi skirt with a white shirt with a big printed brown hare on it', 'Falda tafetán ciruela'),
           (None, 'an oversized ivory cocoon coat with a large painted tulip print in red and green', 'Abrigo tulipán'),
           (None, 'an emerald and black gingham check short shirt jacket (flat lay)', 'Camisa de vichy verde'),
           (None, 'a chunky statement necklace of large orange and black resin beads (flat lay)', 'Collar de cuentas naranja'),
           (None, 'a short-sleeved boxy navy pleated top with a large abstract ivory leaf shape, with a full red taffeta skirt', 'Top plisado y falda roja'),
           (None, 'a bright kelly green technical jacket with a high collar and a black zip', 'Chaqueta verde')],
    l1=(None, 'a red cropped jacket and a voluminous royal blue taffeta midi skirt, walking down an old town street'),
    l2=(None, 'a full black taffeta midi skirt with a green gingham shirt and a chunky orange bead necklace, standing in a minimal warm beige studio'),
    cats=[('Faldas', 'p1'), ('Abrigos', 'p2'), ('Joyas', 'p4')])

S['ana-calzados'] = dict(
    place='a street in the centre of Dos Hermanas, Sevilla, Spain, with white houses and orange trees', who='woman',
    hero=('06', 'brown leather cowboy boots with stitched patterns and pointed toes, worn with black leggings'),
    banner=(None, 'the inside of a modern shoe shop with backlit white shelves full of boots, shoes and handbags, a grey floor and grey velvet seating cubes, no people, no text'),
    prods=[('02', 'beige suede slouchy ankle boots with a block heel and pointed toe', 'Botín slouchy camel'),
           ('05', 'black leather cowboy boots with embroidered stitching and a pointed toe', 'Bota cowboy negra'),
           ('07', 'burgundy leather cowboy boots with stitching and a pointed toe', 'Bota cowboy burdeos'),
           ('13', 'tan suede slip-on loafer mule shoes with moccasin stitching', 'Mocasín destalonado'),
           ('22', 'beige suede clog shoes with a buckle strap, next to a matching beige suede tote bag (flat lay)', 'Zueco de ante'),
           ('26', 'a brown suede shoulder bag with long fringe (flat lay)', 'Bolso de flecos')],
    l1=('12', 'a woman in a brown suede outfit with a fringed suede bag and suede loafer mules, sitting on a grey seat in a shoe shop'),
    l2=('11', 'a brown suede fringed bag and tan suede mules on a wooden floor in a shoe shop'),
    cats=[('Botas', 'p2'), ('Mocasines', 'p4'), ('Bolsos', 'p6')])

S['anselmo-galan'] = dict(
    place='a sunny street in the centre of Lebrija, Sevilla, Spain, with white houses and iron window grilles', who='woman',
    hero=('09', 'a cream knit jacket and trousers set with black floral embroidery and a black handbag'),
    banner=(None, 'the inside of an elegant women fashion boutique with rails full of colourful dresses, coats and knits, a light wallpapered wall and warm light, no people, no text'),
    prods=[('06', 'an olive jacquard jacket with a faux fur collar and dark brown velvet wide trousers', 'Chaqueta de jacquard'),
           ('11', 'a grey and black houndstooth knit bodycon midi dress with a black faux fur stole', 'Vestido pata de gallo'),
           ('13', 'a rust red peplum blouse and wide rust trousers set', 'Conjunto teja'),
           ('16', 'a bronze satin blouse with matching satin jogger trousers and a black faux fur stole', 'Conjunto de satén'),
           ('29', 'a cream cardigan with colourful embroidered folk flowers and wide blue jeans', 'Chaqueta bordada'),
           ('25', 'a white shirt with brown check wide trousers and brown heeled boots', 'Pantalón de cuadros')],
    l1=('23', 'two women in printed pleated midi skirts with brown jumpers and knee-high boots walking down a street'),
    l2=('15', 'a navy velvet long coat over a printed midi dress in a grand hall with marble columns'),
    cats=[('Conjuntos', 'p3'), ('Vestidos', 'p2'), ('Chaquetas', 'p1')])

S['modas-cache'] = dict(
    place='a street in Txurdinaga, Bilbao, Spain, with modern residential buildings and trees', who='woman',
    hero=('05', 'a tan faux leather bomber jacket with a big faux fur collar over a dark top with wide jeans'),
    banner=(None, 'the inside of a small multibrand fashion shop with wooden shelves full of jeans and jumpers, rails of jackets, a light wooden floor and a tall mirror, no people, no text'),
    prods=[('06', 'a black faux leather military-style jacket with gold buttons', 'Chaqueta militar'),
           ('08', 'a sage green quilted onion-stitch jacket over a pink top with black jeans', 'Chaqueta acolchada verde'),
           ('09', 'a black oversized faux leather jacket with black straight jeans', 'Cazadora negra'),
           ('02', 'a dark denim jacket with a check shirt tied around the waist', 'Chaqueta vaquera'),
           ('22', 'a green and navy check overshirt jacket with black faux leather trousers', 'Sobrecamisa de cuadros'),
           ('13', 'colourful beaded friendship bracelets with tassels in many colours (flat lay)', 'Pulseras de cuentas')],
    l1=('03', 'a navy and white striped jumper with dark flared jeans'),
    l2=('12', 'a burgundy and navy striped jumper with a black midi skirt, in a bright shop'),
    cats=[('Chaquetas', 'p1'), ('Vaqueros', 'p4'), ('Bisutería', 'p6')])

S['bohothai'] = dict(
    place='a street in the centre of Burjassot, Valencia, Spain, with orange trees and low houses', who='mature',
    hero=('16', 'a green and navy check wrap coat with a belt'),
    banner=(None, 'the inside of a boho fashion boutique with rails of colourful printed dresses and knits, baskets, dried flowers and wooden furniture, warm light, no people, no text'),
    prods=[('02', 'a chocolate brown short coat with a faux fur collar and a check midi skirt', 'Chaquetón con cuello de pelo'),
           ('05', 'a grey corduroy jacket with red trim and a burgundy top', 'Chaqueta de pana'),
           ('17', 'black suede slouchy ankle boots with a kitten heel and pointed toe (flat lay)', 'Botín de tacón fino'),
           ('22', 'a blue and brown printed oversized shirt', 'Camisa estampada'),
           ('23', 'a pink and purple paisley print long shirt dress with a purple clutch', 'Vestido camisero'),
           ('27', 'dark brown leather ballet flat shoes (flat lay)', 'Bailarina marrón')],
    l1=('07', 'a brown leather jacket with a brown and grey check midi skirt and boots'),
    l2=('20', 'colourful beaded phone straps and necklaces displayed in a boutique, warm light, no text'),
    cats=[('Abrigos', 'p1'), ('Calzado', 'p3'), ('Vestidos', 'p5')])

S['galerias-abreu'] = dict(
    place='a sunny street in the centre of Ayamonte, Huelva, Spain, with white houses and palm trees', who='woman',
    hero=(None, 'a black quilted puffer jacket with a stand collar over a burgundy jumper and beige trousers, with a plain dark green leather tote bag'),
    banner=(None, 'the inside of a classic fashion shop with wooden shelves of folded sweatshirts and jackets, rails of puffer jackets and a white tiled floor, no people, no text, no logos'),
    prods=[(None, 'a black matte quilted puffer jacket with a stand collar, completely plain with no logo', 'Plumífero negro'),
           (None, 'a plain dark green leather tote bag with long handles, completely plain front with no lettering and no logo (flat lay)', 'Bolso shopper verde'),
           (None, 'a plum coated canvas tote bag with long handles, completely plain front with no lettering and no logo (flat lay)', 'Bolso shopper ciruela'),
           (None, 'a black leather crossbody bag with a flap and a chain strap, plain, no logo (flat lay)', 'Bandolera negra'),
           (None, 'a chocolate brown fleece zip jacket with a high collar, completely plain with no logo (flat lay)', 'Forro polar chocolate'),
           (None, 'a royal blue hooded sweatshirt, completely plain with no print and no logo (flat lay)', 'Sudadera azul')],
    l1=(None, 'a woman in a printed white shirt and beige trousers holding a taupe leather half-moon handbag, no logos'),
    l2=(None, 'stacks of folded cream and green fleece jackets on wooden shelves in a fashion shop, no logos, no text'),
    cats=[('Chaquetas', 'p1'), ('Bolsos', 'p2'), ('Sudaderas', 'p6')])

S['hache-ubeda'] = dict(
    place='a Renaissance square in the old town of Úbeda, Jaén, Spain, with golden stone palaces', who='woman',
    hero=('19', 'a black faux leather biker jacket with an emerald green pleated midi skirt and black boots, holding a black handbag'),
    banner=(None, 'the inside of a minimal multibrand fashion boutique with long rails of coats and blouses in warm colours, a white floor and black spotlights, no people, no text'),
    prods=[('21', 'a burgundy and red check blouse with a big pussy bow', 'Blusa con lazada'),
           ('20', 'a burgundy pleated faux leather midi skirt with a burgundy printed blouse', 'Falda plisada burdeos'),
           (None, 'a camel double-breasted belted wool coat with wide blue jeans', 'Abrigo camel'),
           (None, 'a chocolate brown bomber jacket with small dark polka dots over a white T-shirt', 'Bomber de lunares'),
           (None, 'a bottle green diamond quilted jacket with gold buttons over a white shirt', 'Chaqueta acolchada verde'),
           (None, 'a rust brown long puffer coat with a high collar and a belt', 'Plumífero teja')],
    l1=('22', 'a black boxy wool jacket with cream wide trousers and a burgundy handbag in an old stone square'),
    l2=(None, 'a long rail of coats and jackets in camel, brown and black in a minimal boutique, no text'),
    cats=[('Blusas', 'p1'), ('Faldas', 'p2'), ('Abrigos', 'p3')])

S['ego-moda'] = dict(
    place='a sunny street in the centre of La Campana, Sevilla, Spain, with white houses and iron window grilles', who='woman',
    hero=('27', 'a brown check wool coat with a large chocolate faux fur collar over a white top'),
    banner=(None, 'the inside of a bright fashion boutique with a white wall, a wooden ladder rail with jumpers on hangers, plants and a light wooden floor, no people, no text'),
    prods=[('24', 'a short chocolate brown faux fur jacket with a big lapel collar and light jeans', 'Chaqueta de pelo'),
           ('28', 'a beige faux fur gilet over a camel knit top', 'Chaleco de pelo'),
           ('22', 'a pink and burgundy striped jumper with blue jeans', 'Jersey de rayas'),
           ('07', 'a plum flocked velvet floral long-sleeved bodysuit top with black trousers', 'Body de terciopelo'),
           ('10', 'a white shirt with black high-waisted wide-leg trousers and a black handbag', 'Pantalón palazzo negro'),
           ('03', 'a leopard print pussy bow blouse with chocolate brown wide trousers on a hanger', 'Blusa de leopardo')],
    l1=('21', 'a beige knit jumper with wide flared blue jeans in a sunny street'),
    l2=('29', 'faux fur gilets in burgundy, brown, cream and black hanging on a wooden ladder rail, white background, no text'),
    cats=[('Abrigos', 'p1'), ('Punto', 'p3'), ('Pantalones', 'p5')])

S['bella89-woman'] = dict(
    place='a street in the centre of Arganda del Rey, Madrid, Spain, with low brick buildings and trees', who='woman',
    hero=('07', 'a leopard print long-sleeved asymmetric midi dress with brown suede cowboy boots'),
    banner=(None, 'the inside of a small fashion boutique with a grey wall, a gold arch decorated with white drapes and red roses, white shelves of handbags and boots, no people, no text'),
    prods=[('01', 'a red lace long-sleeved bodycon mini dress with black ankle boots', 'Vestido de encaje rojo'),
           ('10', 'a black long-sleeved fitted maxi dress with a sheer mesh neckline', 'Vestido negro largo'),
           ('19', 'a black wide-leg jumpsuit with a deep V neckline', 'Mono negro'),
           ('11', 'a pastel pink fluffy jumper with dark skinny jeans', 'Jersey rosa'),
           ('03', 'dark brown suede cowboy ankle boots with a block heel and pointed toe', 'Botín cowboy marrón'),
           ('18', 'light blue denim cowboy boots with stitching and a block heel', 'Bota cowboy vaquera')],
    l1=('05', 'a burgundy wrap blouse with black flared trousers and black boots in a boutique'),
    l2=('21', 'beige suede chunky biker boots with buckles held up in a boutique'),
    cats=[('Vestidos', 'p1'), ('Monos', 'p3'), ('Botas', 'p5')])

S['sara-nunez'] = dict(
    place='a street in the centre of Alcalá de Guadaíra, Sevilla, Spain, with white houses, iron balconies and flower pots', who='woman',
    hero=('24', 'a cream silk manila shawl with large red and pink embroidered flowers and cream fringe, on a dress form'),
    banner=(None, 'the inside of a flamenca accessories shop with embroidered silk shawls hanging on the walls, glass cabinets of earrings, fans and brooches, and a tiled floor, no people, no text'),
    prods=[('23', 'a white silk manila shawl with red and pink embroidered flowers and long red fringe on a dress form', 'Mantón blanco y rojo'),
           ('29', 'a turquoise silk manila shawl with small red embroidered roses and turquoise fringe (flat lay)', 'Mantón turquesa'),
           ('15', 'a white silk shawl with large purple embroidered flowers and purple fringe', 'Mantón de flores malva'),
           ('08', 'flamenca statement earrings with painted floral tiles and beige hanging beads (flat lay)', 'Pendientes de azulejo'),
           ('06', 'two pink porcelain carnation flower brooches with green stems (flat lay)', 'Broche de clavel'),
           ('12', 'a white hand fan painted with colourful flowers, with red flamenca earrings (flat lay)', 'Abanico pintado')],
    l1=('17', 'a woman in a black skirt and pink blouse with a pink embroidered silk shawl in a whitewashed patio'),
    l2=('03', 'an ivory crochet shawl with long fringe draped over a chair in a shop'),
    cats=[('Mantones', 'p1'), ('Pendientes', 'p4'), ('Complementos', 'p5')])

S['cosquillas'] = dict(
    place='a street in the centre of Ferrol, Galicia, Spain, with white glazed balconies on stone buildings', who='woman',
    hero=('11', 'a burgundy glossy quilted puffer jacket with a black scarf and dark jeans'),
    banner=(None, 'the inside of a cheerful fashion boutique with a shop window with mannequins in colourful coats and check trousers, rails of jackets and a wooden floor, no people, no text'),
    prods=[('05', 'a lilac bouclé teddy coat with a funnel collar and blue jeans', 'Abrigo lila'),
           ('12', 'a royal blue glossy puffer jacket with a blue faux fur hood', 'Plumífero azul'),
           ('21', 'a long chocolate brown faux fur coat', 'Abrigo de pelo'),
           ('19', 'a navy and cream striped cardigan with wide jeans', 'Chaqueta de rayas'),
           ('26', 'a burgundy short jacket with a faux fur collar and toggle buttons, with a black mini skirt and brown boots', 'Chaqueta burdeos'),
           ('17', 'a leopard print silk scarf tied around the neck over a brown knit top with fringe', 'Pañuelo de leopardo')],
    l1=('22', 'a yellow and navy buffalo check jacket with grey trousers walking down a street with trees'),
    l2=('09', 'a black jumper with a diagonal band of white lace flowers'),
    cats=[('Abrigos', 'p1'), ('Chaquetas', 'p4'), ('Complementos', 'p6')])

S['olivia-by-sa'] = dict(
    place='a street in the centre of Solares, Cantabria, Spain, with stone houses and green hills behind', who='woman',
    hero=('03', 'a burgundy faux fur reversible jacket with a burgundy sequin mini skirt and a burgundy blouse'),
    banner=(None, 'the inside of a warm fashion boutique with a white wall, olive trees in pots, rails of coats and dresses, black boots on shelves and a light wooden floor, no people, no text'),
    prods=[('01', 'a long brown check belted wool coat with blue jeans and brown boots', 'Abrigo de cuadros'),
           ('06', 'a dark brown faux leather short jacket with a shirt collar', 'Cazadora marrón'),
           ('13', 'a black sheer mesh long-sleeved top with a bronze sequin mini skirt', 'Falda de lentejuelas'),
           ('19', 'a brown check long-sleeved midi dress with a belt and brown knee boots', 'Vestido de cuadros'),
           ('22', 'a burgundy paisley print mini dress with a high neck and long sleeves', 'Vestido burdeos'),
           ('09', 'tall brown suede knee-high boots with a block heel (flat lay)', 'Bota alta de ante')],
    l1=('15', 'a camel quilted jacket with a white T-shirt and light jeans'),
    l2=('24', 'two women in long faux fur coats and wide printed trousers in a fashion boutique'),
    cats=[('Abrigos', 'p1'), ('Vestidos', 'p4'), ('Botas', 'p6')])
