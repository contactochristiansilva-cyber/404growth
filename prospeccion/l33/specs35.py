# Lote 35 (12/11/2026): cosmética, suplementos y joyería del scrapeo del 10/11 (referencias NN = ~/Downloads/l35src/<slug>/NN.jpg).
# Se carga desde specs.py (exec) y usa su S. «crops»: referencia recortada (NNc) = (original, (x0, y0, x1, y1) en fracciones), para quitar caras o texto.
# Las ref None van sin referencia (el banner cuando no hay una foto de la tienda sin gente).

S['cosa-de-dos'] = dict(
    place='Valencia', who='none', theme=dict(acc='#8A6A3B'),
    hero=('01', 'an oval pink sapphire engagement ring with a diamond halo and a pavé band in yellow and white gold'),
    banner=(None, 'an intimate engagement-ring boutique with warm golden light, a velvet armchair, a wooden table with open ring boxes and classic floral wallpaper, no people'),
    prods=[('15', 'an oval ruby engagement ring with a diamond halo and a pavé band in white gold', 'Anillo de rubí'),
           ('10', 'an oval blue sapphire engagement ring with a diamond halo and a pavé band in white gold', 'Anillo de zafiro'),
           ('22', 'an oval emerald engagement ring with a flower-shaped diamond halo and a pavé band', 'Anillo de esmeralda'),
           ('23', 'a round diamond solitaire engagement ring with a pavé band in white gold', 'Solitario de diamante'),
           ('28', 'a toi-et-moi ring with two oval blue sapphires framed in diamonds', 'Anillo tú y yo'),
           ('39', 'an oval yellow sapphire engagement ring with a diamond halo in yellow gold', 'Anillo de zafiro amarillo')],
    l1=('12', "a woman's hand showing a diamond solitaire engagement ring under the green northern lights over a frozen lake at night"),
    l2=('19', 'a hand holding an open dark ring box with a gold diamond solitaire engagement ring lit by a small light, dark background'),
    cats=[('Anillos de compromiso', 'p4'), ('Piedras de color', 'p2'), ('Tú y yo', 'p5')])

S['playfitness'] = dict(
    place='Granada', who='none', theme=dict(acc='#C1121F'),
    hero=('11', 'a large black tub of micellar casein protein with a pink and white label'),
    banner=('27', 'a large sports nutrition shop with red and black walls, floor-to-ceiling white shelves full of protein tubs, a glass fridge of drinks and bright ceiling lights, no people'),
    prods=[('11', 'a large black tub of micellar casein protein with a pink and white label', 'Caseína micelar'),
           ('13', 'black pre-workout tubs with colourful labels in red, blue and orange', 'Pre-entreno'),
           ('15', 'a protein bar in a white wrapper surrounded by peanuts and chocolate chunks', 'Barrita de proteína'),
           ('31', 'white BCAA powder tubs with fruit-coloured labels in green, blue and yellow', 'Aminoácidos BCAA'),
           ('30', 'two red bottles of antioxidant capsules with white labels', 'Antioxidante en cápsulas'),
           ('07', 'amber glass supplement jars with cork lids and pink labels', 'NAD+ en cápsulas')],
    l1=('14', 'protein bars in white wrappers stacked in an open cardboard box, seen from above'),
    l2=('40', 'three stacked tubs of protein powder in orange, blue and gold on a shop counter, no people'),
    cats=[('Proteínas', 'p1'), ('Pre-entrenos', 'p2'), ('Barritas', 'p3')])

S['joyeria-barc'] = dict(
    place='Barcelona', who='none',
    hero=('03', 'a thick yellow gold Cuban link chain with a diamond clasp on a black velvet bust, with a matching bracelet'),
    banner=('08', 'a luxury jewellery shop with black velvet necklace busts displaying gold and diamond tennis chains under warm spotlights, glass showcases, no people'),
    prods=[('03', 'a thick yellow gold Cuban link chain with a diamond-set box clasp', 'Cadena barbada'),
           ('06', 'white gold tennis bracelets set with round white stones', 'Pulsera riviere'),
           ('19', 'a yellow gold cross pendant paved with white stones on a tennis chain', 'Cruz con brillantes'),
           ('35', 'small gold cross pendants with green, red and blue enamel and white stones on a white ceramic tray', 'Cruces esmaltadas'),
           ('43', 'gold heart pendants with colourful striped enamel and pavé stones on a white ceramic tray', 'Corazones de colores'),
           ('47', 'two yellow gold signet rings set with baguette and round white stones', 'Sello con brillantes')],
    l1=('20', "a man's neck in a black t-shirt wearing a yellow gold rope chain with a square pendant, cropped at the chin"),
    l2=('41', 'gold engravable pendants in heart, round and square shapes with pavé borders on a white ceramic tray on white fur'),
    cats=[('Cadenas', 'p1'), ('Colgantes', 'p3'), ('Pulseras', 'p2')])

S['a-skina'] = dict(
    place='Arteixo', who='none', theme=dict(acc='#B5527A'),
    hero=('27c', 'Korean moisturising creams in pastel pink, white and mint boxes and jars'),
    banner=(None, 'a bright modern parapharmacy with white shelves full of Korean skincare in pastel packaging and a few tubs of supplements, soft daylight, no people'),
    prods=[('10', 'a holographic iridescent tube of CC cream with a pastel gradient', 'CC Cream'),
           ('14c', 'Korean moisturising creams: a pale blue tube, white tubes and jars with green and pink accents', 'Crema hidratante coreana'),
           ('22c', 'Korean cleansing oils in clear and amber pump bottles', 'Aceite limpiador'),
           ('27c', 'Korean moisturising creams in pastel pink, white and mint boxes and jars', 'Hidratante piel seca'),
           ('32c', 'a small gold spray serum bottle', 'Sérum en spray'),
           ('16c', 'a round pink jar of face cream', 'Crema facial rosa')],
    l1=('03c', 'a Korean skincare routine laid out in a row: cleanser, toner, serum, cream and sunscreen in white and pastel packaging'),
    l2=('20c', 'shelves of protein powder tubs and supplements in a bright parapharmacy, no people'),
    cats=[('Cosmética coreana', 'p2'), ('Limpieza', 'p3'), ('Rutinas', 'l1')],
    crops={'27c': ('27', (0.0, 0.45, 1.0, 0.98)), '14c': ('14', (0.0, 0.55, 1.0, 0.97)), '22c': ('22', (0.0, 0.55, 1.0, 0.95)),
           '32c': ('32', (0.45, 0.55, 1.0, 0.95)), '16c': ('16', (0.35, 0.45, 1.0, 0.8)), '03c': ('03', (0.0, 0.6, 1.0, 0.95)), '20c': ('20', (0.45, 0.0, 1.0, 0.6))})

S['micro-oro'] = dict(
    place='Madrid', who='none',
    hero=('13', 'a yellow gold heart-shaped ring paved with baguette and round white stones'),
    banner=(None, 'a luxury jewellery showroom with black marble walls with gold veins, warm spotlights and glass counters full of gold chains and pendants, no people'),
    prods=[('13', 'a yellow gold heart-shaped ring paved with baguette and round white stones', 'Anillo corazón'),
           ('14', 'three gold cross pendants set with red, blue and white stones', 'Cruz con piedras'),
           ('28', 'round pavé stud earrings in yellow gold with white stones', 'Pendientes de brillantes'),
           ('30', 'yellow gold flower-shaped earrings with four blue marquise stones and a pavé border', 'Pendientes flor azul'),
           ('24', 'a yellow gold goat pendant fully paved with white stones', 'Colgante cabra'),
           ('34', 'a yellow gold Cuban link chain in a black gift box', 'Cadena barbada')],
    l1=('34', 'a yellow gold chain displayed in an open black jewellery box on a glass showroom counter'),
    l2=('27', 'the inside of a jewellery shop with black and gold marble walls, glass showcases and a pink velvet chair, no people'),
    cats=[('Anillos', 'p1'), ('Colgantes', 'p2'), ('Pendientes', 'p3')])

S['farmacia-boquetillo'] = dict(
    place='Fuengirola', who='none', theme=dict(acc='#7A2E4D'),
    hero=('36', 'a collection of skincare bottles with orange and white packaging: dropper serums, pump bottles and cream jars'),
    banner=(None, 'a bright modern pharmacy interior with white shelves of dermocosmetics and a soft pink accent wall, no people'),
    prods=[('04', 'a pink and silver anti-pigment serum pump bottle next to its box', 'Sérum antimanchas'),
           ('08', 'a white tube of CC cream with a red cap', 'CC Crème'),
           ('07', 'a yellow and a red cleansing oil pump bottle and two CC cream tubes', 'Aceite limpiador'),
           ('12', 'a white retinol bottle and an amber vitamin C dropper serum', 'Retinol y vitamina C'),
           ('25', 'a white supplement jar with an orange label', 'Complemento digestivo'),
           ('39', 'a white omega-3 capsule bottle with a blue label next to a drinkable omega-3 box', 'Omega-3')],
    l1=('24', 'white skincare jars, glass dropper bottles and pink boxes on a pale pink surface'),
    l2=(None, 'a bright modern pharmacy counter with shelves of skincare products in pink and white tones, no people'),
    cats=[('Cuidado facial', 'p1'), ('Limpieza', 'p3'), ('Nutricosmética', 'p5')])

S['chic-and-txik'] = dict(
    place='Éibar', who='none', theme=dict(acc='#D6336C'),
    hero=('47', 'many colourful mirror acrylic half-moon earrings in pink, blue, purple, green and gold'),
    banner=(None, 'a small bright handmade accessories boutique with a wooden table displaying colourful acrylic earrings on kraft cards, warm light, no people'),
    prods=[('05', 'geometric acrylic stud earrings made of two overlapping triangles in mirror orange and coral, on a kraft card', 'Pendientes triángulo'),
           ('10', 'burgundy acrylic petal earrings with two overlapping leaves, on a kraft card', 'Pendientes pétalo'),
           ('27', 'square acrylic earrings layered in burgundy and red, on a kraft card', 'Pendientes rombo'),
           ('39', 'blue heart-shaped acrylic earrings with a silver mirror inner heart', 'Pendientes corazón'),
           ('21', 'gold mirror acrylic leaf earrings with a white round stud', 'Pendientes hoja dorada'),
           ('50', 'round open hoop earrings in purple and silver mirror acrylic', 'Aros de colores')],
    l1=('43', 'a hand holding a kraft card with blue layered acrylic leaf earrings'),
    l2=('36', 'pink lightning bolt acrylic earrings on pink fabric with gold metal details'),
    cats=[('Geométricos', 'p1'), ('Flores y hojas', 'p2'), ('Dorados', 'p5')])

S['rhinoforce'] = dict(
    place='Sevilla', who='none', theme=dict(acc='#C1121F'),
    hero=('32', 'a black tub of whey isolate protein with chocolate pieces'),
    banner=(None, 'a sports nutrition shop with black walls and a red accent, shelves full of protein tubs and supplements, bright spotlights, no people'),
    prods=[('23', 'a large black tub of whey protein with a gold label', 'Proteína whey'),
           ('13', 'a yellow and black pre-workout tub', 'Pre-entreno'),
           ('32', 'a black tub of whey isolate protein with chocolate pieces', 'Proteína isolate'),
           ('24', 'a red and white tub of creatine monohydrate', 'Creatina monohidrato'),
           ('01', 'a white tub of isotonic drink powder with a blue lid', 'Bebida isotónica'),
           ('28', 'a large white and red tub of mass gainer', 'Ganador de peso')],
    l1=('10', 'a glowing turquoise protein powder dispenser on a dark background'),
    l2=('26', 'a sunny pedestrian shopping street in Sevilla with traditional buildings and shop fronts, no people'),
    cats=[('Proteínas', 'p1'), ('Pre-entrenos', 'p2'), ('Creatina', 'p4')])

S['lb-metales-y-gemas'] = dict(
    place='Alicante', who='none',
    hero=('09', 'yellow gold chains and pendants on black velvet necklace busts in a bright white showcase'),
    banner=('15', 'a red velvet jewellery showcase full of gold rings, pendants and bracelets with small price tags, no people'),
    prods=[('01', 'a yellow gold flat mariner link chain', 'Cadena calabrote'),
           ('03', 'a heavy yellow gold chain with large rectangular links', 'Cadena de eslabones'),
           ('06', 'a yellow gold ring with a large red stone in an ornate setting', 'Sortija con piedra roja'),
           ('07', 'a large gold crown pendant paved with white stones on a gold rope chain', 'Colgante corona'),
           ('27', 'yellow gold mariner chains laid out on a black display', 'Cadenas de oro'),
           ('17', 'yellow gold bracelets with infinity links paved with white stones', 'Pulsera infinito')],
    l1=('11', 'gold chains displayed on black velvet busts on white shelves, close up'),
    l2=('05', 'the inside of a bright jewellery shop with a white marble floor and glass showcases, no people'),
    cats=[('Cadenas', 'p1'), ('Sortijas', 'p3'), ('Pulseras', 'p6')])

S['impulso-cadiz'] = dict(
    place='Cádiz', who='none', theme=dict(acc='#E2611B'),
    hero=('42', 'black tubs of whey protein and isolate with a red shaker'),
    banner=('02', 'a sports nutrition shop with white floor-to-ceiling shelves full of supplement tubs and a white counter, no people'),
    prods=[('32', 'a yellow bag of 100% whey protein with a chocolate splash', 'Whey 100 %'),
           ('07', 'two clear jars of creatine gummies, one with red gummies and one with yellow gummies', 'Gominolas de creatina'),
           ('26', 'open boxes of protein bars in brown and pink wrappers', 'Barritas de proteína'),
           ('48', 'two jars of protein peanut cream', 'Crema de cacahuete proteica'),
           ('45', 'a white bottle of pre-workout capsules with a black and orange label', 'Pre-entreno en cápsulas'),
           ('40', 'gorilla-head-shaped shaker cups in black, orange, red and white', 'Shaker gorila')],
    l1=('23', 'a red bag of protein puffs with chili and lime'),
    l2=('20', 'a sports nutrition shop front with black and white signage and a shop window full of products on a sunny street, no people'),
    cats=[('Proteínas', 'p1'), ('Creatina', 'p2'), ('Snacks', 'p3')])

S['gold-nutrition'] = dict(
    place='Sevilla', who='none', theme=dict(acc='#B8860B'),
    hero=('19', 'a large tub of whey protein with a chocolate biscuit design'),
    banner=('15', 'a sports nutrition shop aisle with tall white shelves full of protein tubs and supplements, no people'),
    prods=[('10', 'large white tubs of whey protein with colourful illustrated labels', 'Proteína whey'),
           ('04', 'black and red tubs of creatine gummies stacked on a shelf', 'Gominolas de creatina'),
           ('25', 'a clear jar of protein crunchy balls with dark chocolate', 'Protein crunchy'),
           ('31', 'a black tub of isolate protein with a peanut butter design', 'Isolate cacahuete'),
           ('23', 'jars of protein spread in black cookies and strawberry flavours', 'Crema proteica'),
           ('27', 'a large bag of zero-lactose isolate protein in teal and black', 'Isolate sin lactosa')],
    l1=('29', 'boxes of protein bars on a shop counter'),
    l2=('06', 'shelves stacked with tubs of whey protein in a bright shop, no people'),
    cats=[('Proteínas', 'p1'), ('Creatina', 'p2'), ('Snacks', 'p3')])

S['farmatural'] = dict(
    place='Las Palmas de Gran Canaria', who='none', theme=dict(acc='#C2552B'),
    hero=('06', 'an open round cream jar with a golden balm and an ivory lid'),
    banner=(None, 'a bright parapharmacy and herbalist shop with white shelves full of colourful skincare, supplements and natural products, no people'),
    prods=[('07', 'a round ivory jar of golden cleansing balm, open', 'Bálsamo limpiador'),
           ('21', 'three skincare booster tubes in pink, lime green and yellow boxes', 'Booster facial'),
           ('27', 'four Korean sunscreen tubes in white, beige and pale blue', 'Solar coreano'),
           ('03', 'a hair care line in coral and black bottles: serums, shampoo and capsules', 'Cuidado del cabello'),
           ('33', 'black pump bottles of argan and keratin shampoo and mask with golden liquid', 'Champú de argán'),
           ('26', 'a tall purple glass ampoule bottle on lilac crystals', 'Ampolla capilar')],
    l1=('32', 'yellow bottles of curly hair shampoo and conditioner scattered on a sunny surface'),
    l2=('13', 'a white facial cleansing brush device held in a hand'),
    cats=[('Cosmética coreana', 'p3'), ('Cabello', 'p4'), ('Facial', 'p2')])

S['joyeria-palicio'] = dict(
    place='Estepona', who='none',
    hero=('16', 'two yellow gold wedding bands in an open pale green jewellery box'),
    banner=(None, 'a classic Spanish jewellery and watch shop with wooden and glass showcases, soft warm light, no people'),
    prods=[('09', 'a pair of yellow gold wedding bands with a small diamond, in an open pale green jewellery box', 'Alianzas de oro'),
           ('11', 'a white gold solitaire engagement ring with a round diamond', 'Solitario'),
           ('29', 'a white gold ring with a square emerald surrounded by diamonds, in an open white box', 'Anillo de esmeralda'),
           ('32', 'a white gold ring with a large round pink stone and a diamond halo', 'Anillo de piedra rosa'),
           ('04', 'a silver necklace with a curved bar of multicolour stones', 'Collar de colores'),
           ('27', 'a yellow gold ring with a round orange shell cameo stone', 'Ojo de Santa Lucía')],
    l1=('25', "a woman's hand wearing a gold ring with a black stone, city lights at night behind"),
    l2=('34c', 'a white gold eternity ring with diamonds in an open white box'),
    cats=[('Alianzas', 'p1'), ('Anillos', 'p2'), ('Collares', 'p5')],
    crops={'34c': ('34', (0.1, 0.12, 0.95, 0.62))})

S['perfumes-a-la-carta'] = dict(
    place='Redondela', who='none', theme=dict(acc='#7B2D8E'),
    hero=('03', 'three glass perfume bottles in red, orange and gold tones on a bright pink background'),
    banner=(None, 'a bright perfume and cosmetics shop with walls of perfume bottles on lime green and white shelves and purple accents, no people'),
    prods=[('03', 'three glass perfume bottles in red, orange and gold tones', 'Perfume de equivalencia'),
           ('10', 'a green bottle of avocado and olive repairing shampoo with avocados and olives', 'Champú reparador'),
           ('11', 'a turquoise tube of after-sport hair and body wash with almonds', 'Gel después del deporte'),
           ('29', 'a large jar of strawberry and chocolate body mousse with strawberries', 'Mousse corporal'),
           ('16', 'a pink bottle of raspberry shower gel with raspberries', 'Gel de ducha frambuesa'),
           ('32', 'a round jar of blueberry and blackberry body cream', 'Crema corporal')],
    l1=('26', 'a hand scooping pink body butter from a jar on a wooden board with berries'),
    l2=('09', 'the inside of a bright perfume shop with a wall of perfume dispensers on lime green shelves, no people'),
    cats=[('Perfumes', 'p1'), ('Cuidado corporal', 'p4'), ('Cabello', 'p2')],
    opts_l='Formato', opts=['30 ml', '50 ml', '100 ml'])

S['ayoze-baez'] = dict(
    place='Icod de los Vinos', who='none', theme=dict(acc='#C1121F'),
    hero=('14', 'two black tubs of ultra pure whey protein with chocolate and coconut'),
    banner=('02', 'a sports nutrition shop with dark metal shelves full of protein tubs and supplements, no people'),
    prods=[('30', 'large black tubs of whey protein with a red and gold label', 'Proteína whey'),
           ('16', 'a pink and green tub of ultrafine creatine', 'Creatina'),
           ('10', 'a clear jar of green omega gummies', 'Gominolas omega'),
           ('23', 'three jars of protein spread with nuts and chocolate', 'Crema proteica'),
           ('18', 'a clear bag of micronised vanilla oat flour', 'Harina de avena'),
           ('04', 'a black hair supplement box and a black anti-hair-loss shampoo bottle', 'Champú anticaída')],
    l1=('07', 'a beige gym t-shirt with a bold illustrated print on a hanger'),
    l2=('24', 'a sunny street in Icod de los Vinos, Tenerife, with palm trees and shop fronts, no people'),
    cats=[('Proteínas', 'p1'), ('Creatina', 'p2'), ('Alimentación', 'p5')])

S['nutripro-cambrils'] = dict(
    place='Cambrils', who='none', theme=dict(acc='#C1121F'),
    hero=('31c', 'a white tub of pre-workout powder with a blue label'),
    banner=(None, 'a hardcore gym with black and red walls, iron weights and machines, dramatic lighting, no people'),
    prods=[('31c', 'a white tub of pre-workout powder with a blue label', 'Pre-entreno'),
           ('04c', 'a black and gold tub of capsules', 'Potenciador natural'),
           ('11c', 'a white tub of pre-workout next to a red shaker bottle', 'Pack pre-entreno y shaker'),
           (None, 'a large black tub of whey protein powder with a red lid', 'Proteína whey'),
           (None, 'a black gym t-shirt and a black gym tank top folded on a bench', 'Ropa de gimnasio'),
           (None, 'a black tub of creatine monohydrate', 'Creatina')],
    l1=(None, 'a dark gym with red lights, racks of dumbbells and weight plates, no people'),
    l2=(None, 'the counter of a gym supplement shop with tubs of protein and shakers on red and black shelves, no people'),
    cats=[('Pre-entrenos', 'p1'), ('Proteínas', 'p4'), ('Ropa', 'p5')],
    crops={'31c': ('31', (0.25, 0.55, 1.0, 1.0)), '04c': ('04', (0.56, 0.0, 1.0, 0.42)), '11c': ('11', (0.3, 0.5, 0.95, 0.95))})

S['esencia-natural'] = dict(
    h1='Lo natural,<br>a un clic.', place='Antequera', who='none', theme=dict(acc='#3F6B3A'),
    hero=('11', 'a small amber essential oil bottle of organic lavender with a purple label'),
    banner=(None, 'a bright herbalist shop with white shelves full of natural products, herbal teas, essential oils and organic food, hanging wicker lamps, no people'),
    prods=[('11', 'a small amber essential oil bottle of organic lavender with a purple label', 'Aceite esencial de lavanda'),
           ('14c', 'a clear box full of dried green medicinal herbs', 'Plantas a granel'),
           ('25c', 'glass jars of organic nut butter and spices with a wooden scoop', 'Crema de frutos secos bio'),
           ('07c', 'a takeaway cup of specialty coffee next to pastries', 'Café de especialidad'),
           (None, 'an amber glass bottle of ashwagandha capsules with a plain label', 'Ashwagandha'),
           ('24c', 'a jar of natural sweetener next to rolled crêpes', 'Endulzante natural')],
    l1=(None, 'a cup of herbal tea with dried chamomile and lavender on a wooden table, soft daylight'),
    l2=('06c', 'the facade of a small herbalist shop with a wooden sign on a sunny street, no people'),
    cats=[('Plantas medicinales', 'p2'), ('Aceites esenciales', 'p1'), ('Alimentación bio', 'p3')],
    crops={'14c': ('14', (0.3, 0.55, 1.0, 1.0)), '25c': ('25', (0.0, 0.55, 1.0, 1.0)), '07c': ('07', (0.0, 0.62, 1.0, 1.0)),
           '24c': ('24', (0.0, 0.0, 1.0, 1.0)), '06c': ('06', (0.0, 0.0, 1.0, 0.45))},
    eyebrow='Herbolario', sub='Las plantas, los aceites y los productos naturales que te recomendamos en {city}, ahora con envío a casa.',
    opts_l='Formato', opts=['Pequeño', 'Mediano', 'Grande'])

S['perfumeria-petalos'] = dict(
    place='Molina de Segura', who='none', theme=dict(acc='#A8834B'),
    hero=('24', 'rows of dark boxed perfumes on a shelf under a golden arch'),
    banner=(None, 'a modern perfume shop with tall black shelves full of perfume boxes, bright ceiling lights and a white floor, no people'),
    prods=[('02c', 'a silver and white perfume box with an abstract teardrop design', 'Perfume en estuche plata'),
           ('08c', 'a gold perfume box', 'Perfume dorado'),
           ('12c', 'a tall white cylindrical perfume box with gold details', 'Perfume Maison'),
           ('19c', 'a white perfume box with blue butterflies and a gold star emblem', 'Perfume mariposas'),
           ('26c', 'a pink perfume box with abstract shapes', 'Perfume rosa'),
           ('29c', 'a red perfume box with a round gold seal', 'Perfume rojo')],
    l1=(None, 'an Arabic perfume bottle with an ornate gold cap on a dark marble surface with oud wood and rose petals'),
    l2=(None, 'the inside of a modern perfume shop with long aisles of perfume boxes on black shelves, no people'),
    cats=[('Perfumes árabes', 'p1'), ('Para ella', 'p5'), ('Para él', 'p2')],
    crops={'02c': ('02', (0.2, 0.3, 0.95, 1.0)), '08c': ('08', (0.25, 0.45, 0.85, 0.95)), '12c': ('12', (0.3, 0.4, 0.75, 1.0)),
           '19c': ('19', (0.2, 0.45, 0.85, 0.95)), '26c': ('26', (0.2, 0.4, 0.8, 0.95)), '29c': ('29', (0.1, 0.45, 0.75, 1.0))})

S['azahar-ecocentro'] = dict(
    h1='Lo natural,<br>a un clic.', place='Santa Cruz de Tenerife', who='none', theme=dict(acc='#2E8A86'),
    hero=('33', 'amber bottles of all-in-one liquid daily supplement with white labels'),
    banner=('22', 'a bright organic shop with wooden shelves full of natural skincare and organic products, no people'),
    prods=[('33', 'amber bottles of all-in-one liquid daily supplement with white labels', 'Suplemento diario'),
           ('04', 'jars of ghee clarified butter with yellow and orange lids', 'Ghee ecológico'),
           ('28', 'two bags of overnight oats mix with oats and berries', 'Avena overnight'),
           ('44', 'a white bottle of pure aloe vera gel with aloe leaves', 'Gel de aloe vera'),
           ('42', 'a yellow tube of gluten-free oat biscuits', 'Galletas de avena'),
           ('37', 'a pink box of collagen beauty tablets', 'Colágeno belleza')],
    l1=('32', 'a wooden crate of fresh local fruit and vegetables: courgettes, apples and avocados'),
    l2=('21', 'a cup of turmeric golden latte with cinnamon sticks on a linen cloth'),
    cats=[('Suplementos', 'p1'), ('Alimentación ecológica', 'p2'), ('Cosmética natural', 'p4')],
    eyebrow='Herbolario y ecotienda', sub='Los productos naturales y ecológicos que te recomendamos en {city}, ahora con envío a casa.',
    opts_l='Formato', opts=['Pequeño', 'Mediano', 'Grande'])

S['joyeria-caceres'] = dict(
    place='Navia', who='none',
    hero=('11', 'gold necklaces with baroque pearls and matching pearl earrings on a linen display'),
    banner=(None, 'a bright jewellery and accessories shop with white shelves and wooden tables, displays of necklaces, watches and leather handbags, no people'),
    prods=[('11', 'gold necklaces with baroque pearls and matching pearl earrings on a linen display', 'Collar de perlas'),
           ('17', 'two heart pendant necklaces in silver and gold on a grey velvet display', 'Colgante corazón'),
           ('13', 'silver beaded bracelets with coloured glass charms', 'Pulseras de plata'),
           ('32', 'two rectangular watches with green and grey dials and leather straps', 'Reloj rectangular'),
           ('22', 'a gold bangle with a large faceted grey crystal and a gold cuff', 'Brazalete con cristal'),
           ('12', 'evening clutch bags in pleated beige, raffia and rattan', 'Bolso de fiesta')],
    l1=('18', "a woman's wrist wearing leather cord bracelets with silver and gold heart charms"),
    l2=('08', 'tan leather handbags, wallets and a blue scarf arranged on a white shop table'),
    cats=[('Joyas', 'p1'), ('Relojes', 'p4'), ('Bolsos', 'p6')])

S['art-joies'] = dict(
    place='Palma', who='none',
    hero=('04', 'a pile of yellow gold chains, bracelets and coins on a marble table with soft light'),
    banner=('08', 'a bright luxury jewellery shop with glass showcases, a white counter with chairs and pink accent walls, no people'),
    prods=[('02', 'heavy yellow gold chains and bracelets', 'Cadenas de oro'),
           ('06', 'loose diamonds and coloured gemstones: ruby, sapphire and emerald', 'Piedras preciosas'),
           ('05', 'antique silver candlesticks, a teapot and cutlery', 'Plata de ley'),
           ('12', 'gold bracelets and chains with a small gold bar', 'Pulseras de oro'),
           ('09', 'an antique silver tea set with a tray', 'Juego de té de plata'),
           (None, 'a vintage yellow gold signet ring', 'Sello de oro')],
    l1=(None, 'a jeweller examining a diamond with tweezers and a loupe, close up of the hands'),
    l2=('08', 'a bright luxury jewellery shop with glass showcases, a white counter with chairs and pink accent walls, no people'),
    cats=[('Oro', 'p1'), ('Piedras preciosas', 'p2'), ('Plata', 'p3')])

S['mestre-joieria'] = dict(
    place='La Pobla de Segur', who='none',
    hero=('10', 'gold textured hoop earrings with small green and pink stones on a pink beaded string'),
    banner=(None, 'a small boutique jewellery and accessories shop with white walls, glass showcases of gold jewellery, shelves of leather bags and soft light, no people'),
    prods=[('10', 'gold textured hoop earrings with small green and pink stones', 'Aros dorados'),
           ('19', 'a thin gold open cuff bracelet with round gold ends', 'Brazalete abierto'),
           ('32', 'gold rings with green and blue oval stones', 'Anillos con piedra'),
           ('33', 'long gold chains and a gold medallion pendant on a white display bust', 'Cadenas largas'),
           ('27', 'braided cord bracelets with silver details and turquoise stones', 'Pulseras de cordón'),
           ('14c', 'cream beaded bracelets with a red stone and a matching ring', 'Pulsera con rubí')],
    l1=('22', "a woman's hand wearing stacked thin diamond rings resting on blue jeans"),
    l2=('01c', 'a brown leather drawstring bucket bag'),
    cats=[('Pendientes', 'p1'), ('Pulseras', 'p2'), ('Anillos', 'p3')],
    crops={'14c': ('14', (0.1, 0.2, 0.95, 0.95)), '01c': ('01', (0.2, 0.5, 0.8, 1.0))})

S['seoul-beauty'] = dict(
    place='San Bartolomé', who='none', theme=dict(acc='#C2577A'),
    hero=('02', 'a cobalt blue glass dropper serum bottle'),
    banner=(None, 'a dreamy Korean beauty boutique with pastel pink arches, white shelves of skincare and cherry blossom branches, no people'),
    prods=[('12', 'a tall clear pump bottle of cleansing oil with a white label', 'Aceite limpiador'),
           ('11', 'a white jar of collagen peptide facial cream with its box', 'Crema de colágeno'),
           ('23', 'an amber glass bottle of centella toner with a white cap', 'Tónico de centella'),
           ('26', 'a green glass dropper ampoule bottle', 'Ampolla calmante'),
           ('27', 'a round white tub of moisturising toner pads', 'Discos hidratantes'),
           ('20', 'a cream-coloured tube of sunscreen lying on a leaf', 'Protector solar')],
    l1=('10', 'a hand holding up a white jar of face cream against a green sea'),
    l2=('16', 'a hand holding a small pink dropper serum against a turquoise sea'),
    cats=[('Limpieza', 'p1'), ('Tratamiento', 'p4'), ('Protección solar', 'p6')])

S['zattera'] = dict(
    place='Mislata', who='none', theme=dict(acc='#1F5C4A'),
    hero=('02', 'gold stainless steel jewellery: a wide cuff bangle, a horseshoe pendant and pearl rings'),
    banner=(None, 'a bright small jewellery shop with white displays and dark green accents, showcases of gold and silver jewellery, no people'),
    prods=[('17', 'a gold flower-shaped ring with a central white stone', 'Anillo flor'),
           ('18', 'a gold spiral ring', 'Anillo espiral'),
           ('28', 'butterfly stud earrings with marquise white stones in silver and gold', 'Pendientes mariposa'),
           ('24', 'gold necklaces with an open circle and an open heart pendant with small stones', 'Collar círculo y corazón'),
           ('10', 'a wide gold hexagonal cuff bangle', 'Brazalete hexagonal'),
           ('15', 'gold bracelets with a tree of life charm', 'Pulsera árbol de la vida')],
    l1=('32', 'stainless steel bangles in gold and silver arranged in a cream jewellery tray'),
    l2=('22c', 'a red velvet gift box with a gold butterfly ring'),
    cats=[('Anillos', 'p1'), ('Pendientes', 'p3'), ('Collares', 'p4')],
    crops={'22c': ('22', (0.1, 0.2, 0.9, 0.95))})

S['modas-gador'] = dict(
    place='Almería', who='none', theme=dict(acc='#D6336C'),
    hero=('01c', 'shelves of Arabic perfumes in ornate gold, pink and black bottles and boxes'),
    banner=(None, 'a colourful fashion and perfume boutique with rails of clothes on one side and glass shelves of Arabic perfumes on the other, warm light, no people'),
    prods=[('04c', 'Arabic perfume bottles in gold, pink and black on glass shelves', 'Perfumes árabes'),
           ('21c', 'rows of boxed Arabic perfumes on shelves', 'Perfume en estuche'),
           ('06c', 'a wall of Arabic perfume boxes and bottles in pink, blue and gold', 'Colección de perfumes'),
           ('18c', 'light blue denim jeans held on hangers', 'Vaqueros'),
           ('12c', 'colourful dresses and tops on a clothing rail', 'Vestidos'),
           ('29c', 'pastel t-shirts and tops hanging on a wall', 'Camisetas')],
    l1=(None, 'an ornate Arabic perfume bottle in gold and amber glass on a satin cloth with rose petals'),
    l2=(None, 'a bright boutique interior with rails of colourful clothes and a wall of perfumes, no people'),
    cats=[('Perfumes árabes', 'p1'), ('Moda', 'p5'), ('Vaqueros', 'p4')],
    crops={'01c': ('01', (0.0, 0.0, 1.0, 0.33)), '04c': ('04', (0.0, 0.0, 1.0, 0.42)), '21c': ('21', (0.0, 0.0, 1.0, 0.42)),
           '06c': ('06', (0.0, 0.0, 1.0, 0.38)), '18c': ('18', (0.0, 0.0, 0.62, 0.72)), '12c': ('12', (0.45, 0.25, 1.0, 0.85)),
           '29c': ('29', (0.5, 0.0, 1.0, 0.6))},
    opts_l='Formato', opts=['30 ml', '50 ml', '100 ml'])
