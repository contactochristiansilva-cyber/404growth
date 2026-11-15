# Lote 37 (15/11/2026): las 50 del scrapeo del 15/11 (31 de moda, 10 de joyería, 6 de suplementos y herbolarios, 3 perfumerías).
# Referencias NN = scratchpad l37/src/<slug>/NN.jpg (sus últimas 33 publicaciones de Instagram, con hasta 3 fotos de cada carrusel).
# Se carga desde specs.py (exec) y usa su S. «crops»: referencia recortada (NNc) = (original, (x0, y0, x1, y1) en fracciones).
# Nunca referencias con menores.

# ---------------- moda
S['tribeca-boutique'] = dict(
    place='the Plaza de los Naranjos in the old town of Marbella, Spain, with whitewashed houses, orange trees and flower pots', who='woman',
    hero=('30', 'an olive green velvet jacket hand-embroidered with colourful flowers, worn open over a long flowing dress'),
    banner=(None, 'the inside of a colourful boho-chic boutique in Marbella with rails of embroidered velvet jackets, kaftans and fringed shawls, white walls and a terracotta floor, no people'),
    prods=[('31', 'an orange velvet jacket hand-embroidered with green, cream and red folk motifs and a long beaded necklace', 'Chaqueta de terciopelo bordada'),
           ('03', 'a crochet ethnic waistcoat with coloured woven bands, beads and long cream fringes, over a white T-shirt and light jeans', 'Chaleco étnico con abalorios'),
           ('12', 'a pale blue faux-fur coat with a brown faux-fur collar and cuffs and a tie belt, with flared jeans', 'Chaqueta de pelo con cinturón'),
           ('14', 'a pair of handmade soutache statement earrings in ivory and pink with a pale pink crystal, no logos', 'Pendientes artesanales'),
           ('34', 'an orange flowing maxi dress with a beaded halter front and side cut-outs', 'Vestido con abalorios'),
           ('16', 'a dusty pink crochet shawl with long fringes over a white top and flared jeans', 'Chal de flecos')],
    l1=('07', 'a black faux-fur gilet over a white T-shirt and light jeans'),
    l2=('25', 'a pair of mustard soutache statement earrings with amber crystals on a piece of weathered wood, no hands'),
    cats=[('Chaquetas', 'p1'), ('Vestidos', 'p5'), ('Complementos', 'p4')])

S['elma-shop'] = dict(
    place='the Plaza del Pilar in Zaragoza, Spain, with the domes of the Basilica del Pilar behind', who='woman',
    hero=('18', 'a beige double-breasted trench coat with a belt, over dark trousers'),
    banner=('22', 'the shop window and inside of a fashion boutique at dusk with dressed mannequins, rails of autumn clothes and warm lights, no people'),
    prods=[('18', 'a beige double-breasted belted trench coat', 'Gabardina'),
           ('10', 'black leather knee-high boots with a block heel, no logos', 'Bota alta negra'),
           ('07', 'a structured olive green leather tote handbag with top handles, no logos', 'Bolso verde'),
           ('03', 'a navy and cream striped knit cardigan with grey check wide-leg trousers', 'Rebeca de rayas'),
           ('28', 'a dark denim jumpsuit with ruffled shoulders and a belt', 'Mono vaquero'),
           ('31', 'an orange and grey striped padded clutch bag, no logos', 'Bolso de rayas')],
    l1=('04', 'a burgundy wool jacket with a belt, a grey check midi skirt and tall black boots'),
    l2=('26', 'a row of leather handbags in tan, brown and burgundy on white shelves, no logos'),
    cats=[('Abrigos', 'p1'), ('Calzado', 'p2'), ('Bolsos', 'p3')])

S['tangara-moda'] = dict(
    place='a sunny palm-lined square in the old town of Motril, Granada, Spain, with white houses', who='woman',
    hero=('20', 'a navy blue tulle and lace long dress with long sleeves and a slit'),
    banner=(None, 'the inside of a small bright fashion boutique with white slat walls, rails of party dresses and jumpers, pampas grass in tall vases and a polished marble floor, no people'),
    prods=[('11', 'a black faux-leather mini dress with a sweetheart neckline and small studs', 'Vestido de polipiel'),
           ('14', 'a navy long-sleeved wide-leg jumpsuit with shoulder pads', 'Mono con hombreras'),
           ('17', 'a black lace and velvet long-sleeved mini dress', 'Vestido de encaje'),
           ('26', 'a chocolate brown faux-suede short jumpsuit with a collar and long sleeves', 'Mono de antelina'),
           ('29', 'a grey satin halter mini dress', 'Vestido satinado'),
           ('32', 'beige faux-leather bermuda shorts with a navy fine-knit jumper', 'Bermuda de polipiel')],
    l1=('28', 'a brown faux-leather jacket over a white top and grey jeans'),
    l2=('15', 'dark brown faux-suede shorts with a fitted top and ankle boots'),
    cats=[('Vestidos', 'p1'), ('Monos', 'p2'), ('Fiesta', 'p3')])

S['el-armario-de-reme'] = dict(
    place='the Paseo de la Independencia in Zaragoza, Spain, with its arcades and autumn trees', who='woman',
    hero=('31', 'a khaki overshirt jacket with matching wide-leg trousers and a white top'),
    banner=(None, 'the inside of a cosy fashion boutique with rails of autumn clothes in brown, rust and khaki, white shelves with handbags and scarves and a light wooden floor, no people'),
    prods=[('31', 'a khaki overshirt jacket with matching wide-leg trousers', 'Conjunto caqui'),
           ('26', 'a brown sweatshirt layered over a light blue shirt with brown wide-leg trousers', 'Sudadera con camisa'),
           ('37', 'a pastel pink and blue check blouse with a ruffled collar and ruffled trims', 'Blusa de cuadros con volantes'),
           ('36', 'a pale yellow knit waistcoat with small gold studs over a white shirt', 'Chaleco con tachas'),
           ('38', 'a cream sweatshirt with ruffled trims on the shoulders', 'Sudadera con volantes'),
           ('18', 'a tan quilted crossbody bag with two small teddy bear charms, no logos', 'Bolso acolchado')],
    l1=('32', 'a white ruffled blouse with a cream fringed scarf and dark flared jeans'),
    l2=('40', 'a white shelf with leopard-print, tan and orange handbags and a striped knit jumper with a fringed scarf, no logos'),
    cats=[('Conjuntos', 'p1'), ('Blusas', 'p3'), ('Bolsos', 'p6')])

S['el-molinillo'] = dict(
    place='a sunny whitewashed street in Brenes, Sevilla, Spain, with orange trees', who='woman',
    hero=('14', 'a long black tailored coat over a dark outfit'),
    banner=(None, 'the inside of a warm small fashion shop with rails of jumpers, jackets and trousers, soft yellow walls, a large green plant and a fitting room curtain, no people'),
    prods=[('02', 'a dark brown faux-suede jacket with black trousers', 'Chaqueta de antelina'),
           ('25', 'an olive green knit set of a short-sleeved jumper and matching trousers', 'Conjunto de punto'),
           ('09', 'a burgundy bomber jacket with black trousers', 'Bomber'),
           ('15', 'an olive green and black striped jumper with black trousers', 'Jersey de rayas'),
           ('23', 'a beige knit jumper and trousers set', 'Conjunto de punto beige'),
           ('16', 'a black faux-leather jacket with black trousers', 'Chaqueta de polipiel')],
    l1=('12', 'a black and white striped knit polo jumper with dark trousers'),
    l2=('08', 'brown paisley print wide-leg trousers with a black top'),
    cats=[('Chaquetas', 'p1'), ('Conjuntos', 'p2'), ('Jerséis', 'p4')])

S['noetta'] = dict(
    place='the seafront promenade of Cangas, Pontevedra, Spain, with the Vigo estuary and fishing boats behind', who='woman',
    hero=('01', 'a beige quilted short jacket with a houndstooth scarf, dark brown wide trousers and a brown leather bag'),
    banner=('17', 'the inside of a fashion boutique with dressed mannequins in autumn coats and knitwear, white walls and warm spotlights, no people'),
    prods=[('01', 'a beige quilted short jacket with a houndstooth scarf and dark brown wide trousers', 'Chaqueta acolchada'),
           ('08', 'a dark brown oversized V-neck knit jumper', 'Jersey oversize'),
           ('09', 'a brown and beige lace-pattern fitted long-sleeved top', 'Camiseta de encaje'),
           ('37', 'tan suede ankle boots with a block heel, no logos', 'Botín de ante'),
           ('18', 'a grey wool overshirt with pearl buttons over a brown quilted vest', 'Sobrecamisa de lana'),
           ('19', 'a dark brown leather tote handbag, no logos', 'Bolso de piel')],
    l1=('10', 'a dark brown knit jumper dress with tall brown boots'),
    l2=('27', 'a black display stand with rows of chunky gold hoop earrings, no logos'),
    cats=[('Chaquetas', 'p1'), ('Punto', 'p2'), ('Calzado', 'p4')])

S['modas-la-tentacion'] = dict(
    place='the Roman bridge of Córdoba, Spain, with the Mezquita behind', who='woman',
    hero=('13', 'a beige belted trench coat over a dark top and trousers'),
    banner=(None, 'the inside of a small fashion shop in Córdoba packed with rails of dresses, jumpsuits and jackets in burgundy, brown and beige, a white tiled floor, no people'),
    prods=[('04', 'a cream shaggy faux-fur jacket', 'Chaqueta de pelo'),
           ('05', 'a brown faux-suede jacket with a collar', 'Chaqueta de antelina'),
           ('15', 'a burgundy satin midi dress with thin straps', 'Vestido burdeos'),
           ('24', 'black and white gingham wide-leg trousers with a black top', 'Pantalón de vichy'),
           ('11', 'a burgundy fluffy knit jumper', 'Jersey de punto'),
           ('30', 'a navy and white striped wide-leg jumpsuit', 'Mono de rayas')],
    l1=('18', 'a brown corset-style top with wide trousers'),
    l2=('07', 'a burgundy and cream floral print blouse with long sleeves'),
    cats=[('Chaquetas', 'p1'), ('Vestidos', 'p3'), ('Pantalones', 'p4')])

S['stylo-moda'] = dict(
    place='the riverside of the Guadalquivir at La Puebla del Río, Sevilla, Spain, with whitewashed houses', who='woman',
    hero=('24', 'a camel ribbed knit zip cardigan with a faux-fur collar, worn with brown corduroy trousers'),
    banner=(None, 'the inside of a small fashion boutique with rails of knitwear and faux-leather trousers, shelves of handbags and boots and a dark wood floor, no people'),
    prods=[('02', 'burgundy faux-leather balloon trousers with a cream fine-knit top', 'Pantalón polipiel bombacho'),
           ('23', 'a burgundy devoré velvet blouse with a floral pattern, worn with jeans', 'Blusa de terciopelo'),
           ('24', 'a camel ribbed knit zip cardigan with a faux-fur collar', 'Chaqueta con cuello de pelo'),
           ('22', 'dark brown suede slouchy knee boots with a pointed toe and a kitten heel, no logos', 'Bota de ante'),
           ('08', 'a brown suede hobo shoulder bag with tassels, no logos', 'Bolso de ante'),
           ('37', 'a chocolate brown bustier tank top with thin straps', 'Top corsé')],
    l1=('25', 'a black and olive floral velvet blouse with brown corduroy trousers'),
    l2=('09', 'a burgundy suede fringed bucket bag with a chain strap, no logos'),
    cats=[('Pantalones', 'p1'), ('Bolsos', 'p5'), ('Calzado', 'p4')])

S['mia-valladolid'] = dict(
    place='the Plaza Mayor of Valladolid, Spain, with its red arcaded buildings', who='woman',
    hero=('22', 'a brown and black animal-print maxi dress with long sleeves and a belt'),
    banner=(None, 'the inside of an elegant multi-brand fashion boutique with pink velvet curtains, rails of designer clothes, a patterned rug and warm light, no people'),
    prods=[('02', 'a burgundy knit mini jumper dress with dark tights and knee boots', 'Vestido de punto'),
           ('33', 'a pink satin blouse with a large neck bow and brown wide trousers', 'Blusa con lazada'),
           ('13', 'a cream chunky knit jumper with mustard wide trousers', 'Jersey de punto'),
           ('26', 'a black knit jumper with a green and red tartan midi skirt', 'Falda escocesa'),
           ('31', 'a burgundy fitted maxi dress with short sleeves', 'Vestido largo burdeos'),
           ('29', 'an olive green utility jacket with camouflage trousers', 'Chaqueta militar')],
    l1=('11', 'a grey knit jumper with wide light-blue jeans'),
    l2=('32', 'a cream knit jumper with matching wide trousers'),
    cats=[('Vestidos', 'p1'), ('Blusas', 'p2'), ('Punto', 'p3')])

S['bazar-laila-bilbao'] = dict(
    place='the riverside by the Guggenheim Museum in Bilbao, Spain', who='woman',
    hero=('26', 'a long chocolate brown wool coat with buttons, worn with a beige hijab and brown boots'),
    banner=('22', 'the inside of a modest-fashion boutique with an arched ceiling and warm golden lights, wooden shelves with perfumes and gift boxes and rails of long dresses and knitwear, no people'),
    prods=[('10', 'a long blue velvet kaftan dress with decorative frog buttons, worn with a matching hijab', 'Kaftán de terciopelo'),
           ('28', 'an olive green long wool coat with large gold buttons and matching wide trousers, worn with a matching hijab', 'Conjunto de abrigo y pantalón'),
           ('17', 'a brown and white wide-striped oversized knit jumper with gold buttons, worn with a matching hijab', 'Jersey de rayas'),
           ('30', 'a black hooded sweatshirt with a matching maxi skirt, worn with a matching hijab', 'Conjunto de falda larga'),
           ('31', 'a camel long wool coat, worn with a matching hijab', 'Abrigo largo camel'),
           ('16', 'a beige oversized shirt jacket with front pockets, worn with a matching hijab', 'Sobrecamisa beige')],
    l1=('19', 'a beige knit jacket and wide trousers set with a matching hijab and a tan handbag'),
    l2=('01', 'a grey knit cardigan and long skirt set with a matching hijab'),
    cats=[('Kaftanes', 'p1'), ('Abrigos', 'p5'), ('Conjuntos', 'p4')])

S['muymia'] = dict(
    place='the palm-lined Paseo del Parque by the port of Málaga, Spain, with the Alcazaba behind', who='woman',
    hero=('30', 'a leopard-print bodysuit with black faux-leather barrel-leg trousers'),
    banner=(None, 'the inside of a bright fashion boutique with golden curtains, rails of colourful clothes and a full-length mirror, no people'),
    prods=[('17', 'red faux-leather straight trousers with a white blouse and a brown blazer', 'Pantalón rojo de polipiel'),
           ('23', 'a long button-front ribbed knit midi dress', 'Vestido de punto'),
           ('32', 'a brown, cream and grey striped knit jumper and mini skirt set', 'Conjunto de lana'),
           ('25', 'black suede knee-high boots with a slim heel, no logos', 'Bota alta'),
           ('20', 'a leopard-print blouse with a long brown faux-leather slit skirt', 'Falda de polipiel'),
           ('13', 'a leopard-print sherpa fleece jacket with a zip', 'Chaqueta borrego de leopardo')],
    l1=('26', 'a cobalt blue jumper with grey check balloon trousers'),
    l2=('27', 'black faux-leather slouchy ankle boots with a pointed toe and a heel, no logos'),
    cats=[('Pantalones', 'p1'), ('Vestidos', 'p2'), ('Calzado', 'p4')])

S['alba-lorenzo-boutique'] = dict(
    place='the seafront of the old town of Cádiz, Spain, with the cathedral dome behind', who='woman',
    hero=('34', 'a lilac and pink floral print midi dress with a brown knit shawl'),
    banner=(None, 'the inside of a feminine boutique with soft pink walls, a flower garland arch, white rails of elegant clothes and handbags and warm light, no people'),
    prods=[('08', 'a cream padded parka jacket with a hood, worn with beige trousers', 'Parka acolchada'),
           ('18', 'a chocolate brown corduroy jacket and trousers set', 'Conjunto de pana'),
           ('16', 'a white cotton blouse with ruffled trims and long sleeves', 'Camisa blanca con volantes'),
           ('24', 'a leopard-print satin blouse', 'Blusa de leopardo'),
           ('21', 'a brown laser-cut leather tote bag, no logos', 'Bolso calado'),
           ('28', 'a brown and cream tartan blouse with a neck bow', 'Blusa de cuadros con lazada')],
    l1=('11', 'a grey knit poncho cape over black trousers'),
    l2=('35', 'a chunky resin and wood bead bracelet in grey and caramel tones on a wrist'),
    cats=[('Abrigos', 'p1'), ('Blusas', 'p3'), ('Bolsos', 'p5')])

S['javier-leon'] = dict(
    place='a sunny palm-lined square in the centre of Huelva, Spain, with white buildings', who='woman',
    hero=('29', 'a white cotton bambula maxi dress with embroidered details and thin straps'),
    banner=('17', 'the inside of a ceremony and flamenco fashion shop with an autumn display of dresses on mannequins, a bench and plants, warm light, no people'),
    prods=[('10', 'a camel embroidered maxi skirt with fringes and a brown halter top', 'Falda bordada con flecos'),
           ('27', 'a white bambula maxi dress with thin straps and an embroidered hem', 'Vestido de bambula'),
           ('16', 'a brown and cream embroidered flamenco shawl with long fringes', 'Mantón bordado'),
           ('19', 'a set of coral red flamenco earrings and a long coral bead necklace displayed in a black velvet box, no logos', 'Conjunto de flamenca'),
           ('14', "colourful men's flower lapel pins in red, coral and pink, displayed on dark green fabric in a small box", 'Pines de solapa'),
           ('28', 'a black bambula maxi dress with cream embroidered details and thin straps', 'Vestido negro bordado')],
    l1=('11', 'a black embroidered maxi skirt with fringes and a brown halter top'),
    l2=('37', 'a big pile of colourful flamenco hair flowers in red, pink, coral and white, no people'),
    cats=[('Vestidos', 'p2'), ('Flamenca', 'p3'), ('Complementos', 'p4')])

S['stylos-merce'] = dict(
    place='the Plaza del Arenal in Jerez de la Frontera, Spain, with palm trees and old palaces', who='woman',
    hero=('03', 'a black shaggy faux-fur coat with straight jeans'),
    banner=(None, 'the inside of a glamorous fashion boutique with a pink velvet sofa, a wall of pink roses, gold clothes rails and a marble floor, no people'),
    prods=[('01', 'a black shaggy faux-fur coat', 'Abrigo de pelo'),
           ('10', 'a burgundy faux-leather jacket over a black top and jeans', 'Chaqueta de polipiel'),
           ('05', 'a brown faux-leather midi skirt with a red satin top', 'Falda de polipiel'),
           ('21', 'red wide-leg trousers with a white fitted top', 'Pantalón rojo'),
           ('28', 'olive green suede retro sneakers with a cream sole, no logos', 'Zapatilla de ante'),
           ('17', 'leopard-print wide trousers with a black blouse', 'Pantalón de leopardo')],
    l1=('12', 'beige cargo trousers with a black top and a cream jacket'),
    l2=('32', 'burgundy suede sneakers with a white sole, no logos'),
    cats=[('Abrigos', 'p1'), ('Pantalones', 'p4'), ('Zapatillas', 'p5')])

S['bambula'] = dict(
    place='the Plaza de Santa María in Jaén, Spain, with the cathedral behind', who='woman',
    hero=('17', 'a camel short double-breasted trench jacket with dark jeans'),
    banner=('16', 'the inside of a fashion boutique with white walls, a wooden shelf with handbags and rails of jumpers and trousers in burgundy, blue and cream, no people'),
    prods=[('17', 'a camel short double-breasted trench jacket with dark jeans', 'Gabardina corta'),
           ('09', 'a cream tailored waistcoat with a black and white tartan maxi skirt', 'Chaleco y falda de cuadros'),
           ('13', 'a denim blue shirt with a peplum and brown faux-leather trousers', 'Camisa vaquera'),
           ('21', 'a brown smocked floral blouse with long sleeves', 'Blusa fruncida'),
           ('06', 'brown and mustard striped balloon trousers with a brown fitted T-shirt', 'Pantalón de rayas'),
           ('03', 'a brown hooded jacket with grey barrel-leg trousers', 'Chaqueta con capucha')],
    l1=('12', 'a burgundy floral midi skirt and blouse set'),
    l2=('36', 'an olive green smocked maxi dress with a statement necklace'),
    cats=[('Chaquetas', 'p1'), ('Faldas', 'p2'), ('Blusas', 'p4')])

S['nina-jaen'] = dict(
    place='a sunny street in the old town of Jaén, Spain, with the Castle of Santa Catalina on the hill behind', who='woman',
    hero=('28', 'a brown suede cropped jacket with an embroidered folk midi skirt and brown cowboy boots'),
    banner=('02', 'the inside of a modern fashion shop with a grey wood floor, round rails of knitwear and jackets and tall shelves, no people'),
    prods=[('15', 'a burgundy lace blouse with beige balloon trousers', 'Blusa de encaje'),
           ('20', 'a black glossy faux-leather bomber jacket with jeans', 'Chaqueta de polipiel'),
           ('21', 'camel suede loafers with tassels, no logos', 'Mocasín camel'),
           ('33', 'a large slouchy triangle bag in a colourful animal and floral print, no logos', 'Bolso tipo saco'),
           ('19', 'grey balloon trousers with small studs and a navy jumper', 'Pantalón globo con tachas'),
           ('35', 'brown suede western cowboy ankle boots with a slanted heel, no logos', 'Botas cowboy')],
    l1=('18', 'a cream wool jumper with embroidered flowers and straight jeans'),
    l2=('23', 'a brown suede studded hobo bag with fringes on a wooden table, no logos'),
    cats=[('Blusas', 'p1'), ('Calzado', 'p3'), ('Bolsos', 'p4')])

S['essencial'] = dict(
    place='the main square of Los Santos de Maimona, Badajoz, Spain, with whitewashed houses and the church tower', who='woman',
    hero=('13', 'a burgundy velvet ruffled maxi skirt and blouse set'),
    banner=('01', 'the inside of a bright fashion boutique with a polished grey floor, dressed mannequins, rails of knitwear and jeans and a large plant, no people'),
    prods=[('26', 'a red and light blue argyle knit jumper with jeans', 'Jersey de rombos'),
           ('06', 'a leopard-print knotted handle bag with long black fringes, no logos', 'Bolso de flecos'),
           ('18', 'black slingback kitten heel pump shoes with a bow, no logos', 'Destalonado con lazo'),
           ('39', 'a dark green blouse with a large embroidered collar and cream trousers', 'Blusa con cuello bordado'),
           ('03', 'a grey long coat with a big silver faux-fur collar', 'Abrigo con cuello de pelo'),
           ('24', 'navy suede ballet flat shoes with a bow, no logos', 'Bailarina de ante')],
    l1=('34', 'a purple satin maxi skirt with a matching top'),
    l2=('11', 'a light blue knit turtleneck jumper with a zebra-print crossbody bag'),
    cats=[('Punto', 'p1'), ('Bolsos', 'p2'), ('Calzado', 'p3')])

S['revuelo'] = dict(
    place='a sunny avenue with orange trees in Don Benito, Badajoz, Spain', who='woman',
    hero=('06', 'a long red velvet kimono coat over a dark outfit'),
    banner=(None, 'the inside of a fashion boutique packed with colourful party dresses and coats on rails, handbags on the top shelves and a light grey floor, no people'),
    prods=[('02', 'a burgundy fur gilet over a dark top', 'Chaleco de pelo'),
           ('05', 'a cream long wool coat with a large fur collar and a belt', 'Abrigo con cuello de pelo'),
           ('09', 'a taupe brown puffer jacket with a large faux-fur collar and jeans', 'Plumífero con pelo'),
           ('14', 'a purple lace midi dress with long sleeves', 'Vestido de encaje'),
           ('07', 'dark brown suede knee-high boots, no logos', 'Botas de ante'),
           ('26', 'a burgundy tailored blazer and wide trousers suit', 'Traje burdeos')],
    l1=('13', 'an olive green tulle midi skirt with a matching top'),
    l2=('10', 'a navy sequin maxi dress with a slit'),
    cats=[('Abrigos', 'p2'), ('Invitada', 'p4'), ('Calzado', 'p5')])

S['alebu'] = dict(
    place='the seafront promenade of San Lorenzo beach in Gijón, Spain', who='woman',
    hero=('16', 'a long red wool coat over a dark outfit'),
    banner=(None, 'the inside of a bohemian boutique with large woven rattan pendant lamps, a warm wooden floor and rails of knitwear, coats and shirts in earthy tones, no people'),
    prods=[('04', 'a brown and rust check tweed blazer with a burgundy jumper and jeans', 'Americana de tweed'),
           ('07', 'a leopard-print pony hair tote bag with leather handles, no logos', 'Bolso de pelo leopardo'),
           ('17', 'a brown, cream and black Fair Isle knit jumper', 'Jersey de punto nórdico'),
           ('28', 'a burgundy leather tote handbag with a zebra-print pouch, no logos', 'Bolso burdeos'),
           ('18', 'a burgundy and red tartan flannel shirt with jeans', 'Camisa de cuadros'),
           ('14', 'a grey Nordic pattern knit jumper with jeans', 'Jersey nórdico gris')],
    l1=('19', 'a floral print blouse with olive trousers and a brown bag'),
    l2=('27', 'a burgundy and cream striped knit jumper'),
    cats=[('Americanas', 'p1'), ('Punto', 'p3'), ('Bolsos', 'p2')])

S['moda-aurora'] = dict(
    place='the Plaza Mayor of Gijón, Spain, by the port, with its arcaded buildings', who='woman',
    hero=('18', 'a camel teddy wool long coat over a white outfit'),
    banner=('23', 'the inside of a colourful fashion boutique with a wooden lattice ceiling, rails full of bright knitwear and a green plant, no people'),
    prods=[('26', 'a burgundy corduroy jacket with a faux-fur collar and white trousers', 'Chaqueta de pana con pelo'),
           ('28', 'a navy and white Nordic pattern knit cardigan with white trousers', 'Chaqueta de punto nórdico'),
           ('09', 'a brown and cream check blouse with a ruffled collar', 'Blusa de cuadros'),
           ('06', 'a brown crochet poncho with long fringes over a white outfit', 'Poncho de ganchillo'),
           ('27', 'a burgundy and cream argyle knit jumper with white trousers', 'Jersey de rombos'),
           ('24', 'a green, rust and cream check overshirt jacket', 'Sobrecamisa de cuadros')],
    l1=('17', 'a brown tweed long coat with white trousers'),
    l2=('21', 'a colourful floral print satin blouse'),
    cats=[('Chaquetas', 'p1'), ('Punto', 'p2'), ('Blusas', 'p3')])

S['miaou'] = dict(
    place='the white glass gallery facades of the Marina in A Coruña, Spain', who='woman', eyebrow='Moda en tallas grandes',
    hero=('18', 'an oversized mid-blue denim jacket over a white top, on a curvy plus-size woman'),
    banner=('22', 'the inside of a fashion boutique for curvy women with a big glass shop window, rails of colourful clothes and a light floor, no people'),
    prods=[('16', 'a gold metallic hooded puffer jacket with black trousers, on a curvy plus-size model', 'Plumífero metalizado'),
           ('27', 'a grey knit poncho with a cowl neck, on a curvy plus-size model', 'Poncho de punto'),
           ('28', 'a black and grey abstract print long coat, on a curvy plus-size model', 'Abrigo estampado'),
           ('09', 'a purple hooded parka with patches, on a curvy plus-size model', 'Parka morada'),
           ('14', 'a beige knit V-neck jumper and trousers set, on a curvy plus-size model', 'Conjunto de punto'),
           ('13', 'a black loungewear set with big white star prints, on a curvy plus-size model', 'Conjunto de estrellas')],
    l1=('26', 'a khaki camouflage print jacket with a white top and jeans, on a curvy plus-size woman'),
    l2=('33', 'a denim shirt and wide denim trousers set with a white T-shirt, on a curvy plus-size woman'),
    cats=[('Abrigos', 'p1'), ('Ponchos', 'p2'), ('Conjuntos', 'p5')])

S['ana-piel'] = dict(
    place='the Calle Mayor of Palencia, Spain, with its arcades and historic buildings', who='woman',
    hero=('03', 'a cream shearling cropped jacket with a big fur collar, over dark trousers'),
    banner=('06', 'the shop window and inside of a premium outerwear boutique with mannequins wearing puffer jackets in green and black, white walls and warm spotlights, no people'),
    prods=[('01', 'a glossy chocolate brown quilted puffer jacket with cream trousers', 'Plumífero brillo'),
           ('05', 'a white cropped puffer jacket with a fur-trimmed hood', 'Plumífero corto con pelo'),
           ('16', 'a navy double-breasted long wool coat with fur cuffs', 'Abrigo cruzado con pelo'),
           ('22', 'tan suede western knee boots with a buckle strap, no logos', 'Bota camperas de ante'),
           ('15', 'a leopard-print bomber jacket with black trousers', 'Bomber de leopardo'),
           ('26', 'a plum purple faux-fur cropped jacket with dark jeans', 'Chaqueta de pelo')],
    l1=('07', 'a lime green quilted puffer jacket with black wide trousers'),
    l2=('18', 'black leather ankle boots with gold studs, no logos'),
    cats=[('Plumíferos', 'p1'), ('Abrigos', 'p3'), ('Calzado', 'p4')])

S['qbonico'] = dict(
    place='a sunny street in Mancha Real, Jaén, Spain, with whitewashed houses and olive groves on the hills behind', who='woman',
    hero=('38', 'a leopard-print quilted shoulder bag with a gold chain, carried with a cream outfit'),
    banner=('05', 'the inside of an accessories boutique with black metal shelves full of handbags in pink, blue and taupe, a pink wall and bright light, no people'),
    prods=[('04', 'a structured taupe faux-leather handbag with a top handle and a long strap, no logos', 'Bolso de mano'),
           ('07', 'a set of chunky gold rings with coloured stones displayed in a beige velvet box, no logos', 'Anillos dorados'),
           ('29', 'a mustard quilted faux-leather wallet with a gold clasp, no logos', 'Cartera acolchada'),
           ('13', 'a pair of big red and pink flamenco tassel earrings displayed in a small box', 'Pendientes de flamenca'),
           ('02', 'a long pink and burgundy chunky bead necklace displayed in a box', 'Collar de cuentas'),
           ('34', 'a white T-shirt with a bold orange and red graphic print and orange striped trousers', 'Camiseta estampada')],
    l1=('33', 'a white T-shirt with a print of colourful fish and denim shorts'),
    l2=('10', 'a white basket full of pink and red flamenco hair flowers, no people'),
    cats=[('Bolsos', 'p1'), ('Bisutería', 'p2'), ('Carteras', 'p3')])

S['nude-tarragona'] = dict(
    place='the Balcó del Mediterrani in Tarragona, Spain, with the sea and the Roman amphitheatre below', who='woman',
    hero=('19', 'a long chocolate brown wool coat over a cream knit and white wide jeans'),
    banner=(None, 'the inside of a minimalist fashion boutique with warm wood, cream walls, rails of knitwear in earthy tones, a woven chair and dried flowers, no people'),
    prods=[('04', 'a dark brown tailored waistcoat with matching trousers', 'Chaleco sastre'),
           ('03', 'a dark brown woven leather shoulder bag, no logos', 'Bolso trenzado'),
           ('18', 'a cream and burgundy chevron pattern knit jumper', 'Jersey de punto'),
           ('28', 'a chocolate brown long knit maxi dress', 'Vestido largo de punto'),
           ('16', 'a cream and pink leopard jacquard knit jumper with grey trousers', 'Jersey de leopardo'),
           ('10', 'four small pebbled leather coin purse cases in pink, yellow, orange and black, no logos', 'Monedero de piel')],
    l1=('12', 'a dark denim waistcoat with a cream pleated maxi skirt'),
    l2=('11', 'a brown macramé knotted handbag on a table, no logos'),
    cats=[('Punto', 'p3'), ('Vestidos', 'p4'), ('Bolsos', 'p2')])

S['kucaes'] = dict(
    place="a sunny old-town street in L'Olleria, Valencia, Spain, with the church bell tower", who='woman',
    hero=('02', 'a burgundy faux-leather jacket with a shearling collar over a cream knit and jeans'),
    banner=('22', 'the inside of a fashion boutique with a golden clothes rail of striped knitwear, beige walls and soft daylight, no people'),
    prods=[('02', 'a burgundy faux-leather jacket with a cream shearling collar and lining', 'Cazadora con borrego'),
           ('06', 'brown leather and suede knee-high riding boots with a gold buckle, no logos', 'Bota de montar'),
           ('18', 'a chocolate brown suede slouchy tote bag, no logos', 'Bolso de ante'),
           ('05', 'a burgundy and cream vertical striped knit cardigan', 'Chaqueta de rayas'),
           ('14', 'chocolate brown suede moccasin loafers with tiny silver studs and a bow, no logos', 'Mocasín con tachas'),
           ('08', 'a brown leopard-print long-sleeved mini dress with a ruffled hem', 'Vestido de leopardo')],
    l1=('11', 'a brown leather cropped jacket with grey wide wool trousers'),
    l2=('24', 'brown suede Mary Jane ballet flats with a buckle strap, no logos'),
    cats=[('Chaquetas', 'p1'), ('Calzado', 'p2'), ('Bolsos', 'p3')])

S['guapa'] = dict(
    place='the Paseo del Espolón in Burgos, Spain, with the cathedral spires behind', who='woman',
    hero=('18', 'a black faux-leather jacket with a black and white zig-zag knit maxi skirt'),
    banner=('08', 'the inside of a big bright fashion boutique with a polished concrete floor, white shelves full of jeans and knitwear, round jute rugs and tall plants, no people'),
    prods=[('20', 'black straight jeans with a white star patch on the back pocket and small studs', 'Pantalón de estrella'),
           ('31', 'a khaki parka with a faux-fur hood and embroidered details', 'Parka con capucha'),
           ('18', 'a black and white zig-zag knit maxi skirt with a black top', 'Falda de punto'),
           ('26', 'pink suede platform sneakers with a white sole, no logos', 'Zapatilla rosa'),
           ('13', 'an olive green utility jumpsuit with a belt', 'Mono caqui'),
           ('33', 'a leopard-print mini dress with black boots', 'Vestido de leopardo')],
    l1=('10', 'a leopard-print blouse with cream jeans and tan boots'),
    l2=('29', 'an orange knit top with relaxed jeans'),
    cats=[('Pantalones', 'p1'), ('Abrigos', 'p2'), ('Zapatillas', 'p4')])

S['helena-urzainqui-boutique'] = dict(
    place='the Plaza del Castillo in Pamplona, Spain, with its arcades and bandstand', who='woman',
    hero=('08', 'a camel long wool coat over a cream outfit'),
    banner=(None, 'the inside of an elegant boutique with a marble floor, white rails of clothes, a gilded mirror, an antique chest of drawers and modern art, no people'),
    prods=[('04', 'a camel shearling short jacket with white trousers', 'Chaqueta de borrego'),
           ('14', 'a rust brown tailored suit jacket and trousers', 'Traje teja'),
           ('21', 'a cream silk blouse with cascading ruffles and beige trousers', 'Blusa de seda con volantes'),
           ('01', 'a blue and grey check flannel overshirt jacket with black trousers', 'Sobrecamisa de cuadros'),
           ('15', 'an aubergine knit jumper with a matching satin midi skirt', 'Falda satinada'),
           ('30', 'a cream cardigan embroidered with colourful flowers and white trousers', 'Chaqueta bordada')],
    l1=('23', 'a brown suede jacket with white trousers'),
    l2=('07', 'a purple shirt with dark purple corduroy trousers'),
    cats=[('Chaquetas', 'p1'), ('Blusas', 'p3'), ('Punto', 'p6')])

S['boutique-farah'] = dict(
    place='the Rambla Nova of Tarragona, Spain, with its trees, near the Mediterranean balcony', who='woman',
    hero=('21', 'a long washed-denim belted trench coat dress, worn with a beige hijab'),
    banner=(None, 'the inside of a modest-fashion boutique with a warm wooden floor, white shelves full of folded hijabs and scarves, rails of long dresses and a golden mirror, no people'),
    prods=[('21', 'a long washed-denim belted trench coat dress, worn with a matching hijab', 'Gabardina vaquera larga'),
           ('05', 'a royal blue long shirt dress with buttons and a belt, worn with a matching hijab', 'Vestido camisero azul'),
           ('07', 'a beige long belted trench coat, worn with a matching hijab', 'Gabardina beige'),
           ('15', 'an aubergine long jacket with patterned trim on the cuffs, worn with a matching hijab', 'Chaqueta larga'),
           ('31', 'a dark brown open abaya with patterned bell sleeves over a matching dress, worn with a matching hijab', 'Abaya con mangas estampadas'),
           ('11', 'a cream long jacket with embroidered pockets and matching wide trousers, worn with a matching hijab', 'Conjunto crudo')],
    l1=('16', 'a long denim button-front shirt dress with a belt, worn with a hijab'),
    l2=('20', 'a fuchsia long tunic with matching wide trousers, worn with a hijab'),
    cats=[('Abayas', 'p5'), ('Abrigos', 'p3'), ('Vestidos', 'p2')])

S['agaiz-collection'] = dict(
    place='the Plaça del Mercadal in Reus, Spain, with its modernist buildings', who='woman', eyebrow='Caftanes y tekchitas en Reus',
    hero=('01', 'an emerald green satin Moroccan takchita with a gold embroidered front panel and a gold belt'),
    banner=(None, 'the inside of a Moroccan caftan boutique with white walls, golden wall sconces, rails of embroidered caftans in jewel colours and a light wooden floor, no people'),
    prods=[('01', 'an emerald green satin Moroccan takchita with a gold embroidered front panel and a gold belt', 'Tekchita verde esmeralda'),
           ('07', 'a red velvet Moroccan caftan with heavy gold embroidery and a gold belt', 'Caftán rojo bordado'),
           ('02', 'a fuchsia satin takchita with gold trim and a gold belt', 'Tekchita fucsia'),
           ('15', 'a white Moroccan caftan with silver embroidery and a train', 'Caftán blanco de novia'),
           ('29', 'a turquoise Moroccan caftan with copper embroidery and a gold belt', 'Caftán turquesa'),
           ('25', 'a black takchita with copper embroidery and a gold belt', 'Tekchita negra')],
    l1=('19', 'pastel satin takchitas in sky blue, pink and silver with silver belts'),
    l2=('22', 'a sky blue satin takchita with silver embroidery and a silver belt'),
    cats=[('Tekchitas', 'p1'), ('Caftanes', 'p2'), ('Novia', 'p4')])

S['luka-almeria'] = dict(
    place='the Paseo de Almería, Spain, with palm trees and the Alcazaba on the hill behind', who='woman',
    hero=('28', 'a multicolour floral jacquard cropped jacket with navy barrel-leg trousers'),
    banner=('06', 'the inside of a fashion boutique with soft pink and mustard walls, gold rails, dressed mannequins and burgundy boots and bags on a gold plinth, no people'),
    prods=[('01', 'a burgundy floral print ruffled blouse and matching midi skirt set', 'Conjunto estampado'),
           ('03', 'burgundy suede pointed slingback pump shoes with a block heel, no logos', 'Destalonado burdeos'),
           ('22', 'a navy wool cape jacket with a belt and matching trousers', 'Capa de paño azul marino'),
           ('26', 'an olive and mustard floral satin shirt and maxi skirt set', 'Conjunto satinado'),
           ('27', 'an olive green velvet jacket with gold buttons and matching wide trousers', 'Conjunto de terciopelo'),
           ('30', 'a red quilted leather shoulder bag with a chain, no logos', 'Bolso acolchado rojo')],
    l1=('38', 'a grey knit jumper with a navy tartan maxi skirt and a wide leather belt'),
    l2=('08', 'a burgundy leather handbag and a camel suede handbag on a gold stand, no logos'),
    cats=[('Conjuntos', 'p1'), ('Chaquetas', 'p3'), ('Calzado', 'p2')])

S['mayte-cuellar'] = dict(
    place='the Plaza Alta of Badajoz, Spain, with its colourful arcaded houses', who='woman', eyebrow='Tocados y moda en Badajoz',
    hero=('24', 'a brown and pink sculptural fascinator with flowers and feathers, with an elegant outfit'),
    banner=('09', 'the inside of a ceremony fashion and hat boutique with white shelves full of colourful fascinators and hats, rails of dresses and a wooden floor, no people'),
    prods=[('24', 'an elegant brown and pink sculptural fascinator with feathers and flowers', 'Tocado artesanal'),
           ('07', 'a taupe quilted reversible long coat with a hood', 'Abrigo reversible'),
           ('14', 'a pale pink ostrich feather collar necklace with pearls', 'Collar de plumas'),
           ('12', 'a brown velvet pleated pouch clutch bag, no logos', 'Bolso de terciopelo'),
           ('29', 'a big lilac wide-brimmed ceremony hat with a ribbon', 'Pamela lila'),
           ('21', 'a red and cream floral print fabric sash belt', 'Fajín estampado')],
    l1=('22', 'a coral pink ruffled long dress with a straw hat'),
    l2=('10', 'three mini compact umbrellas in pink, blue and cream in their cases, no logos'),
    cats=[('Tocados', 'p1'), ('Abrigos', 'p2'), ('Complementos', 'p4')])

# ---------------- joyería y bisutería
S['isabel-mediavilla'] = dict(
    place='Sevilla', who='none', theme=dict(acc='#B5452B'),
    hero=('04', 'a pair of coral red and gold flamenco statement earrings with small flowers and leaves'),
    banner=('40', 'the inside of a traditional Sevillian accessories shop with glass cabinets full of shawls, flowers, coral necklaces and earrings, red carnations and warm light, no people'),
    prods=[('04', 'a pair of coral red and gold flamenco drop earrings with small flowers and leaves', 'Pendientes de coral'),
           ('05', 'a pair of gold earrings with a square green stone and hanging baroque pearls', 'Pendientes de perla y piedra'),
           ('10', 'a gold brooch shaped like a sprig of leaves with small crystals', 'Broche de hojas'),
           ('26', 'a long gold bar brooch with three oval stones in mint, coral and lilac', 'Broche de piedras'),
           ('01', 'a pale sage green silk shawl hand-embroidered with roses and long fringes, laid flat', 'Mantoncillo de seda bordado'),
           ('37', 'a pair of drop earrings with white and coral resin beads', 'Pendientes de bolas')],
    l1=('19', 'coral red flamenco earrings and a long coral bead necklace displayed on a shop counter with red flowers'),
    l2=('13', 'a red embroidered flamenco shawl with fringes displayed with red carnations'),
    cats=[('Pendientes', 'p1'), ('Broches', 'p3'), ('Mantones', 'p5')])

S['boutique-de-la-alianza'] = dict(
    place='Murcia', who='none', theme=dict(acc='#A8823A'), eyebrow='Joyería nupcial desde 1973',
    hero=('22', 'a wide yellow gold wedding band with a hand-engraved textured pattern'),
    banner=('13', 'the inside of an elegant bridal jewellery boutique with a gold textured wall, glass display cases, warm light and a goldsmith desk, no people'),
    prods=[('22', 'a wide yellow gold wedding band with a hand-engraved textured pattern', 'Alianza de oro grabada'),
           ('21', 'a stack of white gold wedding bands with different hammered and brushed textures', 'Alianzas texturizadas'),
           ('07', 'a polished yellow gold wedding band with a subtle wave texture', 'Alianza de oro amarillo'),
           (None, 'a white gold solitaire engagement ring with a round brilliant natural diamond', 'Solitario de diamante'),
           (None, 'a pair of matching rose gold and white gold wedding bands, one with a row of small diamonds', 'Alianzas a juego'),
           ('26', 'a restored vintage steel automatic wristwatch with a silver dial and a steel bracelet, no logos', 'Reloj restaurado')],
    l1=('30', "a goldsmith's bench with small tools and a gold ring being hand-finished, no faces"),
    l2=('35', 'a white wedding ring box with a pair of gold wedding bands on a wooden table, no text'),
    cats=[('Alianzas', 'p1'), ('Compromiso', 'p4'), ('Relojes', 'p6')])

S['por-tu-cuenta'] = dict(
    place='Madrid', who='none', theme=dict(acc='#C0603A'), eyebrow='Bisutería y abalorios en Madrid',
    hero=('28', 'a long necklace of burgundy and gold glass beads with big gold flower pendants'),
    banner=('10', 'the inside of a bright bead and jewellery shop with wooden shelves full of beads, display stands of earrings and a long work table, no people'),
    prods=[('04', 'two round mother-of-pearl medals with a Virgin Mary image on fine gold chains', 'Medalla de la Virgen'),
           ('19', 'chunky cocktail rings with big polished stones in amber, blue and green on a display, no logos', 'Anillos de piedra'),
           ('16', 'colourful braided cord bracelets with small gold charms', 'Pulseras de hilo'),
           ('25', 'resin bangles in teal, amber and grey with gold details', 'Brazaletes de resina'),
           ('33', 'gold bracelets with small square enamel charms in red, blue and yellow', 'Pulseras esmaltadas'),
           ('40', 'a gold octopus pendant on a pearl and gold bead necklace', 'Collar pulpo')],
    l1=('12', 'braided cord bracelets with charms displayed on a stone angel statue with plants'),
    l2=('18', 'a hand wearing several chunky stone cocktail rings and beaded bracelets'),
    cats=[('Pulseras', 'p3'), ('Collares', 'p6'), ('Anillos', 'p2')])

S['ruby-abalorios-bcn'] = dict(
    place='Barcelona', who='none', theme=dict(acc='#B23A48'), eyebrow='Abalorios en Barcelona',
    hero=('17', 'a handmade gold chain necklace with colourful enamel charms: an eye, a heart, a star and a shell'),
    banner=('16', 'the inside of a huge bead and craft supplies shop with walls full of hanging bags of beads and charms, long aisles and bright light, no people'),
    prods=[('17', 'a handmade gold chain necklace with colourful enamel charms', 'Collar de charms'),
           ('27', 'spools of gold-plated chains sold by the metre hanging in a row, no logos', 'Cadena por metros'),
           ('23', 'a jade green stone pendant on a fine gold snake chain', 'Colgante de piedra'),
           ('19', 'spools of elastic jewellery thread in black and white in a tray', 'Hilo elástico'),
           ('29', 'a small tray of colourful glass and resin beads in candy colours', 'Abalorios de colores'),
           ('01', 'gold metal bag handles and purse frames in round and bamboo shapes, no logos', 'Asas para bolsos')],
    l1=('21', 'a display of beaded bracelets with coloured rectangular stones'),
    l2=('26', 'a hand holding small pastel blue and pink ceramic bird charms'),
    cats=[('Charms', 'p1'), ('Cadenas', 'p2'), ('Abalorios', 'p5')])

S['angels-joyeria'] = dict(
    place='Madrid', who='none', theme=dict(acc='#B8892B'), eyebrow='Oro 18K y 14K en Madrid',
    hero=('19', 'two heavy 18k gold rope chains displayed on a black velvet necklace bust'),
    banner=('02', 'the inside of a gold jewellery shop in a shopping centre with glass cabinets full of gold chains on black velvet busts, a gold textured wall and bright lights, no people'),
    prods=[('19', 'a heavy 18k yellow gold rope chain on a black velvet bust', 'Cadena cordón de oro 18K'),
           ('07', 'a gold rope chain with a large gold pendant of the face of Christ set with small crystals, on a black background', 'Colgante de Cristo'),
           ('20', 'two fine gold chains with small gold cross pendants on a black velvet bust', 'Cadena con cruz'),
           ('32', 'a silver iced-out cuban link bracelet fully set with small white stones', 'Pulsera cubana de plata'),
           ('23', 'three chunky gold signet rings with pink heart stones in a black box, no logos', 'Anillos de oro'),
           ('31', 'three gold chains with round gold medal and plaque pendants on a black velvet bust', 'Medallas de oro')],
    l1=('04', "a man's chest wearing a heavy silver iced-out cuban link chain over a black T-shirt"),
    l2=('17', "two heavy gold cuban chains with a big gold pendant on a man's neck over a white T-shirt"),
    cats=[('Cadenas', 'p1'), ('Colgantes', 'p2'), ('Anillos', 'p5')])

S['insphyria'] = dict(
    place='Bilbao', who='none', theme=dict(acc='#7A3FB0'), eyebrow='Pendientes de metacrilato en Bilbao',
    hero=('27', 'a pair of large blue and black faceted star-shaped acrylic statement earrings'),
    banner=('04', 'the inside of a colourful accessories shop with exposed brick, shelves of hats and bags, rails of ponchos and a big wall of statement earrings, no people'),
    prods=[('05', 'a pair of white and yellow daisy-shaped acrylic statement earrings', 'Pendientes margarita'),
           ('21', 'a pair of geometric triangle acrylic earrings in green, yellow and black', 'Pendientes geométricos'),
           ('22', 'a pair of rose gold mirrored acrylic crescent hoop earrings', 'Aros de metacrilato'),
           ('31', 'a pair of drop earrings with green crystal teardrops', 'Pendientes de cristal verde'),
           ('26', 'a pair of black acrylic treble clef music note earrings with a red glitter heart', 'Pendientes musicales'),
           ('01', 'a pink, black and green geometric pattern knit poncho, worn by a model', 'Poncho geométrico')],
    l1=('32', 'a display board full of colourful acrylic flower and leaf earrings'),
    l2=('19', 'a colourful printed silk scarf tied around the neck of a woman'),
    cats=[('Pendientes', 'p1'), ('Metacrilato', 'p2'), ('Ponchos', 'p6')])

S['from-bilbao'] = dict(
    place='Bilbao', who='none', theme=dict(acc='#7A2E2E'), eyebrow='Joyas antiguas desde 1940',
    hero=('05', 'an antique round platinum cluster ring with a central old-cut diamond surrounded by diamonds, in an antique red leather ring box'),
    banner=('11', 'the shop window of an antique jewellery shop with velvet trays of old rings, gold chains and brooches and warm light, no people'),
    prods=[('01', 'an antique gold ring with a central diamond inside a halo of blue sapphires, in an old ring box', 'Sortija ojo de perdiz'),
           ('08', 'an antique white gold ring with a large oval aquamarine surrounded by diamonds, in a blue velvet box', 'Sortija de aguamarina'),
           ('13', 'an 18k gold ring with a ruby and diamonds', 'Sortija de rubí y brillantes'),
           ('21', 'a pair of long Art Deco platinum drop earrings set with diamonds', 'Pendientes de brillantes'),
           ('17', 'a gold cocktail ring with a large oval opal surrounded by diamonds', 'Sortija de ópalo'),
           ('18', 'a wide gold band ring with a row of square sapphires and diamonds, in a black box', 'Sortija de zafiros')],
    l1=('34', 'a hand wearing an antique white gold flower ring with a pearl and sapphires'),
    l2=('33', 'antique gold rings displayed on a red leather jewellery tray'),
    cats=[('Sortijas', 'p1'), ('Pendientes', 'p4'), ('Piedras de color', 'p2')])

S['dolphins-bisuteria'] = dict(
    place='Madrid', who='none', theme=dict(acc='#1F7A8C'), eyebrow='Bisutería y complementos en Madrid',
    hero=('05', 'colourful thread-wrapped bangles with brass caps and round coloured stones on a white wooden surface'),
    banner=(None, 'the inside of a bohemian jewellery and accessories shop with walls of bracelets, earrings and bags, wooden display tables and warm light, no people'),
    prods=[('04', 'thread-wrapped bangle bracelets in bright colours with brass caps and coloured stones', 'Pulsera de hilo y piedra'),
           ('07', 'large tribal brass hoop earrings with engraved details in gold and silver tones', 'Aros étnicos'),
           ('01', 'animal print hair-on cowhide leather clutch bags in zebra, leopard and dalmatian, no logos', 'Bolso de piel animal print'),
           ('17', 'chunky gold rings with big oval stones in turquoise, amber and red', 'Anillos de piedra'),
           ('10', 'enamel sun and moon drop earrings in turquoise, purple and green', 'Pendientes de esmalte'),
           ('38', 'two chunky wooden bangles with small brass studs', 'Brazalete de madera')],
    l1=('15', 'a wrist wearing several engraved copper cuff bracelets'),
    l2=('22', 'colourful Indian embroidered patchwork zip purses on a white wooden table, no logos'),
    cats=[('Pulseras', 'p1'), ('Pendientes', 'p2'), ('Bolsos', 'p3')])

S['iris'] = dict(
    place='Moraleja', who='none', theme=dict(acc='#D6336C'), eyebrow='Bisutería artesanal en Moraleja',
    hero=('32', 'a pair of handmade white and yellow rockrose flower earrings and small green leaf earrings on a green background'),
    banner=(None, 'the inside of a bright small boutique with pink accents, a big arched mirror and display tables of handmade earrings, bracelets and handbags, no people'),
    prods=[('17', 'a pair of big handmade white flower statement earrings with a yellow and red centre', 'Pendientes Jara'),
           ('39', 'a pair of handmade red poppy flower earrings with black centres', 'Pendientes Amapola'),
           ('09', 'a wide burgundy embroidered fabric sash belt with a floral pattern', 'Fajín bordado'),
           ('23', 'a burgundy woven leather handbag with a top handle, no logos', 'Bolso trenzado burdeos'),
           ('27', 'a chunky orange bead statement necklace', 'Collar de cuentas naranja'),
           ('38', 'handmade red and white flower earrings and hoops', 'Pendientes San Juan')],
    l1=('40', 'a woman wearing big red poppy earrings and a red neck scarf'),
    l2=('22', 'a display of burgundy and brown leather handbags with plants, no logos'),
    cats=[('Pendientes', 'p1'), ('Bolsos', 'p4'), ('Collares', 'p5')])

S['tangara-jewelry'] = dict(
    place='Alicante', who='none', theme=dict(acc='#C27A8A'), eyebrow='Joyas de acero en Alicante',
    hero=('30', 'a gold necklace with a crescent moon and small coloured clover charms, with matching earrings, in an open blush pink jewellery box, no logos'),
    banner=('24', 'a pastel pink jewellery kiosk in a shopping centre with glass counters full of gold jewellery, pink walls and soft lights, no people'),
    prods=[('06', 'a gold-plated cross pendant on a fine chain, set with small crystals', 'Collar cruz'),
           ('07', 'a gold cross pendant with coloured baguette stones on a fine chain', 'Cruz de colores'),
           ('22', 'a pair of long gold drop earrings with a cascade of small stars', 'Pendientes de estrellas'),
           ('19', 'gold chain necklaces with colourful enamel charms of hearts, flowers and shells', 'Collar de charms'),
           ('10', 'gold-plated stainless steel chain bracelets displayed on a pink velvet roll', 'Pulseras de acero'),
           ('14', 'chunky gold-plated stainless steel rings displayed in a blush pink tray', 'Anillos de acero')],
    l1=('36', "a woman's neck wearing a gold round medallion necklace with a soft yellow top"),
    l2=('39', 'blush pink gift boxes and shopping bags with dried flowers, no logos'),
    cats=[('Collares', 'p1'), ('Pendientes', 'p3'), ('Pulseras', 'p5')])

# ---------------- suplementos y herbolarios
S['mh-nutrition'] = dict(
    place='Dos Hermanas', who='none', theme=dict(acc='#B8892B'), eyebrow='Nutrición deportiva en Dos Hermanas',
    hero=('07', 'a big white tub of whey protein powder with a plain label'),
    banner=('03', 'the inside of a sports nutrition shop with black and gold walls, shelves full of protein tubs and supplements and a bright counter, no people'),
    prods=[('07', 'a white 2 kg tub of whey protein powder with a plain label', 'Proteína whey'),
           ('11', 'a black tub of creatine monohydrate with a plain label next to lime slices', 'Creatina monohidrato'),
           ('24', 'four squeeze bottles of zero-sugar sauces in different colours with plain labels', 'Salsas zero'),
           ('29', 'protein bars in plain wrappers, one opened to show the chocolate layers', 'Barritas de proteína'),
           ('26', 'three jars of beauty collagen powder in pastel colours with plain labels', 'Colágeno'),
           ('09', 'a white bottle of NAD+ capsules with a plain label', 'NAD+ 500 mg')],
    l1=('21', 'a bowl of crunchy chocolate protein cereal balls with milk'),
    l2=('30', 'an open display box of oat flapjack protein bars in plain wrappers'),
    cats=[('Proteínas', 'p1'), ('Creatina', 'p2'), ('Snacks', 'p4')])

S['murcia-pro-nutrition'] = dict(
    place='Ceutí', who='none', theme=dict(acc='#C0392B'), eyebrow='Dietética y nutrición deportiva',
    hero=('18', 'a big white tub of gourmet whey protein with a plain label, with chocolate and cookie pieces around'),
    banner=(None, 'the inside of a sports nutrition shop with tall shelves full of protein tubs, a red and black counter and bright light, no people'),
    prods=[('12', 'a white tub of gourmet whey protein powder with a plain label', 'Proteína whey gourmet'),
           ('30', 'a white tub of creatine monohydrate powder with a plain label', 'Creatina monohidrato'),
           ('05', 'a white bottle of night fat-burner capsules with a plain label', 'Quemador nocturno'),
           ('07', 'chocolate protein brownies stacked on a plate next to plain wrappers', 'Brownie proteico'),
           ('26', 'pints of protein ice cream in different flavours with plain labels', 'Helado proteico'),
           ('32', 'a white tub of cappuccino-flavour whey isolate with a plain label and a cup of coffee', 'Isolate sabor capuchino')],
    l1=('09', 'glazed protein doughnuts on a dark plate'),
    l2=('08', 'chocolate protein muffins on a wooden board'),
    cats=[('Proteínas', 'p1'), ('Creatina', 'p2'), ('Snacks', 'p4')])

S['apolo-suplementacion-deportiva'] = dict(
    place='Las Palmas de Gran Canaria', who='none', theme=dict(acc='#D4A017'), eyebrow='Suplementación deportiva y herbolario',
    hero=('34', 'three tubs of whey protein in blue, black and yellow with plain labels'),
    banner=('35', 'the inside of a bright sports nutrition and herbalist shop with white shelves full of supplements, a blue ceiling and a counter, no people'),
    prods=[('34', 'a tub of whey protein powder with a plain blue label', 'Proteína whey'),
           (None, 'a tub of creatine monohydrate with a plain white label', 'Creatina'),
           (None, 'a jar of pre-workout powder with a plain black label next to a shaker', 'Preentreno'),
           (None, 'an amber glass bottle of magnesium capsules with a plain label and green leaves', 'Magnesio'),
           (None, 'a paper bag of loose herbal tea with dried chamomile and mint', 'Infusión de plantas'),
           (None, 'a box of vegan protein bars in plain wrappers', 'Barritas veganas')],
    l1=(None, 'a protein shake in a clear shaker on a gym bench with dumbbells, no people'),
    l2=(None, 'jars of dried medicinal herbs and essential oils on a wooden herbalist counter'),
    cats=[('Proteínas', 'p1'), ('Rendimiento', 'p3'), ('Herbolario', 'p5')])

S['herbolari-de-lina'] = dict(
    place='Burjassot', who='none', theme=dict(acc='#2E7D4F'), eyebrow='Herbolario en Burjassot', h1='Lo natural,<br>a un clic.',
    hero=(None, 'an amber glass bottle of collagen capsules with a plain label, with fresh herbs and a wooden spoon of powder'),
    banner=('05', 'the inside of a herbalist shop with tall white shelves packed with supplements, natural remedies and boxes, a green sign and bright light, no people'),
    prods=[(None, 'an amber glass jar of biotin capsules with a plain label', 'Biotina'),
           (None, 'a white tub of collagen powder with a plain label and a scoop', 'Colágeno'),
           (None, 'a glass bottle of apple cider vinegar with red apples', 'Vinagre de manzana'),
           ('20', 'a natural alum stone deodorant crystal block', 'Piedra de alumbre'),
           (None, 'an amber bottle of omega-3 fish oil softgel capsules with a plain label', 'Omega 3'),
           (None, "a glass jar of lion's mane mushroom capsules with dried mushroom pieces", 'Melena de león')],
    l1=('32', 'a cup of golden turmeric milk with cinnamon sticks and fresh ginger on a wooden table'),
    l2=('21', 'a festive gift box with a small handmade rag doll and Christmas decorations, no text'),
    cats=[('Suplementos', 'p1'), ('Belleza', 'p2'), ('Remedios naturales', 'p4')])

S['alloza-sport-nutrition'] = dict(
    place='Huelva', who='none', theme=dict(acc='#C8102E'), eyebrow='Nutrición deportiva en Huelva',
    hero=('07', 'a white tub of creatine monohydrate with a plain label next to a bottle of multivitamins'),
    banner=(None, 'the inside of a sports nutrition shop with black shelves full of protein tubs and creatine, a counter and bright light, no people'),
    prods=[('07', 'a white tub of micronized creatine monohydrate with a plain label', 'Creatina monohidrato'),
           ('08', 'a big tub of whey protein with a plain label', 'Proteína whey'),
           ('22', 'tubs of BCAA and glutamine powder in different flavours with plain labels', 'BCAA y glutamina'),
           ('32', 'colourful pouches of flavoured rice flour for protein recipes with plain labels', 'Harina de arroz'),
           ('29', 'white bottles of sleep support supplements with plain labels', 'Descanso'),
           ('25', 'bottles of carb blocker capsules with plain labels', 'Bloqueador de carbohidratos')],
    l1=(None, 'a creatine shake in a black shaker next to dumbbells on a gym floor, no people'),
    l2=('23', 'the shop front of a small sports nutrition store on a sunny street, no people'),
    cats=[('Creatina', 'p1'), ('Proteínas', 'p2'), ('Bienestar', 'p5')])

S['herbolario-tienda-verde'] = dict(
    place='Alhama de Murcia', who='none', theme=dict(acc='#3F8F3A'), eyebrow='Herbolario en Alhama de Murcia', h1='Lo natural,<br>a un clic.',
    hero=(None, 'a glass jar of loose herbal tea with dried flowers next to a cup of infusion'),
    banner=('13', 'the inside of a herbalist shop with tall white shelves full of natural products, teas and supplements, a green wooden sign and warm light, no people'),
    prods=[(None, 'a small amber essential oil bottle with a plain label and lavender sprigs', 'Aceite esencial de lavanda'),
           ('23', 'a matcha tea set: a bowl of bright green matcha, a bamboo whisk and a tin of matcha powder', 'Té matcha'),
           (None, 'a glass jar of golden milk turmeric spice blend with cinnamon sticks', 'Golden milk'),
           (None, 'an amber glass bottle of ashwagandha capsules with a plain label', 'Ashwagandha'),
           (None, 'a paper bag of organic loose herbal tea with chamomile and mint', 'Infusión ecológica'),
           (None, 'a bar of natural handmade soap with dried herbs on a wooden dish', 'Jabón natural')],
    l1=('17', 'a cup of golden milk with turmeric and spices on a wooden table'),
    l2=('37', 'a stone mortar with dried herbs and a singing bowl among green plants'),
    cats=[('Aceites esenciales', 'p1'), ('Infusiones', 'p5'), ('Suplementos', 'p4')])

# ---------------- perfumerías
S['perfumes-arabes-oasis-tenerife'] = dict(
    place='Santa Cruz de Tenerife', who='none', theme=dict(acc='#8C6A2F'), eyebrow='Perfumería árabe en Tenerife',
    hero=('23', 'a light blue rectangular perfume bottle with a silver cap, surrounded by ice cubes and lime slices'),
    banner=('10', 'the inside of an Arabic perfume shop with white floating shelves full of ornate perfume bottles and a grey textured wall, no people'),
    prods=[('23', 'a light blue rectangular perfume bottle with a silver cap', 'Perfume Freeze'),
           ('24', 'a red rectangular perfume bottle with a gold cap', 'Perfume Fire'),
           ('16', 'a round gold sphere-shaped perfume bottle with an ornate cap', 'Perfume esfera dorada'),
           ('29', 'a green apple-shaped perfume bottle in an open green presentation box', 'Perfume manzana verde'),
           ('15', 'a white perfume bottle with a black geometric pattern and a gold cap', 'Perfume geométrico'),
           ('14', 'a black and gold faceted perfume bottle in a black box', 'Perfume oud negro')],
    l1=('06', 'a group of gourmand Arabic perfume bottles in pink, cream and gold tones with strawberries and caramel, no text'),
    l2=('11', 'the shop window of a perfume shop full of colourful Arabic perfume bottles on white shelves, no people'),
    cats=[('Frescos', 'p1'), ('Gourmand', 'p3'), ('Oud', 'p6')])

S['perfumeria-paco'] = dict(
    place='Trebujena', who='none', theme=dict(acc='#C2185B'), eyebrow='Perfumería en Trebujena',
    hero=('09', 'a round pink and gold perfume bottle with an ornate gold cap, among pink flowers'),
    banner=('08', 'the inside of a bright perfumery and drugstore with shelves full of perfumes, make-up and skincare, a white floor and bright lights, no people'),
    prods=[('09', 'a round pink perfume bottle with an ornate gold cap', 'Perfume Yara Elixir'),
           ('26', 'an open makeup case full of eyeshadow palettes, lipsticks and brushes, no logos', 'Maletín de maquillaje'),
           ('24', 'two glass jar scented candles in lilac and blue, no logos', 'Velas aromáticas'),
           ('15', 'a row of cream eyeshadow sticks in pastel shimmer shades, no logos', 'Sombra en crema'),
           ('22', 'hair care bottles of shampoo and hair oil in coral and turquoise, no logos', 'Cuidado capilar'),
           ('35', 'velvet knotted headbands in burgundy, grey and gingham check', 'Diademas')],
    l1=('31', 'a white perfume gift box with a pink floral design next to a bottle of rose perfume, no text'),
    l2=('33', 'a tray of small Christmas candles shaped like Santa Claus and trees'),
    cats=[('Perfumes', 'p1'), ('Maquillaje', 'p2'), ('Hogar', 'p3')])

S['office-of-fragrance'] = dict(
    place='Pamplona', who='none', theme=dict(acc='#9C7A3C'), eyebrow='Perfumes árabes en Pamplona',
    hero=('04', 'a black and gold faceted perfume bottle with a gold cap in front of flames on dark marble'),
    banner=('02', 'the inside of a luxury Arabic perfume boutique with gold arched shelves full of perfume bottles, a marble floor and warm light, no people'),
    prods=[('04', 'a black faceted perfume bottle with a gold diamond pattern and a gold cap', 'Onyx Gold'),
           ('09', 'a deep blue rectangular perfume bottle with a silver cap', 'Hawas'),
           ('30', 'a white textured perfume bottle with a white cap on snowy stone', 'Shiyaaka Snow'),
           ('22', 'a faceted amber glass perfume bottle with a copper cap', 'Ateeq'),
           ('27', 'a pale pink perfume bottle with an ornate silver figure cap, with plums and roses', 'Perfume rosa'),
           ('21', 'a matte black perfume bottle with a gold horse emblem and a gold cap', "Noir d'Arabie")],
    l1=('11', 'a pink perfume bottle on the edge of a turquoise Moroccan riad fountain, no text'),
    l2=('33', 'a dark green perfume bottle with a gold cap among coconut halves and tropical leaves'),
    cats=[('Oud', 'p6'), ('Frescos', 'p3'), ('Ámbar', 'p4')])
