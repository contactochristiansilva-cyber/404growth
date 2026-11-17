# Lote 39 (17/11/2026): las 30 del scrapeo del 17/11 (prospeccion/scrapeo-17nov/candidatos.json): +10k en Instagram, activas,
# sin tienda online o con una floja, sin moda ni comida. Nichos nuevos de niches39.py (mercería, bellas artes, artesanía, electro, juegos, equitación).
# Referencias NN = scratchpad l39/full/<slug>/NN.jpg (sus últimas 36 publicaciones, hasta 3 fotos por carrusel). Nunca referencias con menores.
# Todas con hero de bodegón (still=True): el producto en el tercio derecho, sin modelo. Se carga desde specs.py (exec) y usa su S.

S['only-today'] = dict(
    who='none', still=True, eyebrow='Perfumes personalizados', h1='Tu perfume,<br>hecho a tu medida.',
    sub='Perfumes que creamos contigo en nuestra perfumería de {city}. Ahora, también online.',
    hero=('19', 'a clear glass perfume bottle with an amber liquid and a cork stopper, surrounded by small glass vials of essences, dried flowers and orange peel on a dark wooden counter'),
    banner=(None, 'the inside of a small artisan perfumery in Córdoba with shelves full of glass bottles of essences, warm lamps and dark wooden counters, no people'),
    prods=[(None, 'a 50 ml clear glass perfume bottle with an amber liquid and a black cap, no label', 'Perfume personalizado 50 ml'),
           (None, 'a 100 ml clear glass perfume bottle with a pale golden liquid and a gold cap, no label', 'Perfume personalizado 100 ml'),
           (None, 'a gift box with a perfume creation kit: six small glass vials of essences, a glass beaker and paper testing strips', 'Experiencia: crea tu perfume'),
           (None, 'three small amber glass dropper bottles of essential oils, no labels', 'Aceites esenciales'),
           (None, 'a 30 ml clear glass travel perfume atomizer with a silver cap', 'Perfume de viaje 30 ml'),
           (None, 'a small glass bottle of musk perfume oil with a glass rod applicator', 'Almizcle en aceite')],
    l1=(None, 'a perfumer pouring essence from a small glass beaker into a perfume bottle, seen from the chest down, on a wooden counter full of glass bottles'),
    l2=(None, 'paper perfume testing strips fanned out next to glass bottles of essences and dried flowers'),
    opts_l='Formato', opts=['30 ml', '50 ml', '100 ml'],
    cats=[('Perfumes', 'p1'), ('Experiencias', 'p3'), ('Aceites', 'p4')])

S['factory-electrodomesticos'] = dict(
    who='none', still=True,
    hero=(None, 'a stainless steel American-style side-by-side fridge with a water dispenser, no logos, in a bright modern kitchen'),
    banner=(None, 'the inside of a bright home appliance outlet store with rows of white washing machines and stainless steel fridges, white walls with a red stripe, no people, no logos'),
    prods=[(None, 'a stainless steel American-style side-by-side fridge with a water and ice dispenser, no logos', 'Frigorífico americano'),
           (None, 'a white front-loading washing machine with a dark round door, no logos', 'Lavadora 8 kg'),
           (None, 'a stainless steel two-door combi fridge freezer, no logos', 'Frigorífico combi'),
           (None, 'a white freestanding dishwasher, no logos', 'Lavavajillas 60 cm'),
           (None, 'a black glass induction hob with four cooking zones, no logos', 'Placa de inducción'),
           (None, 'a black digital air fryer, no logos', 'Freidora de aire')],
    l1=(None, 'a bright modern kitchen with a stainless steel combi fridge and a white dishwasher, soft daylight, no logos'),
    l2=(None, 'a bright laundry room with a white washing machine and folded towels on a wooden shelf, no logos'),
    cats=[('Frío', 'p1'), ('Lavado', 'p2'), ('Cocina', 'p5')])

S['herbolario-cai-salud'] = dict(
    who='none', still=True, eyebrow='Herbolario', h1='Lo natural,<br>a un clic.',
    sub='Lo que te recomendamos en nuestro herbolario de {city} desde 2001. Ahora, con envío a casa.',
    hero=(None, 'amber glass bottles of herbal remedies, a glass jar of loose herbal tea and a bar of olive oil soap with fresh herbs, no labels'),
    banner=(None, 'the inside of a bright herbalist shop with wooden shelves full of herbal remedies, teas in glass jars and natural cosmetics, green plants, no people'),
    prods=[(None, 'a bar of traditional olive and laurel oil soap, no text', 'Jabón de Alepo'),
           (None, 'a small amber glass bottle of lavender essential oil with a dropper, no label', 'Aceite esencial de lavanda'),
           (None, 'a glass jar of loose chamomile and herbal tea blend', 'Infusión relajante'),
           (None, 'a white supplement bottle of capsules with a plain label, no text', 'Magnesio'),
           (None, 'a glass jar of raw honey with a wooden dipper, no label', 'Miel cruda'),
           (None, 'a white tube of natural arnica cream with a plain label, no text', 'Crema de árnica')],
    l1=(None, 'a cup of herbal tea next to fresh herbs and a glass teapot on a wooden table by a window'),
    l2=(None, 'natural soaps and amber glass bottles arranged on a wooden shelf with eucalyptus leaves'),
    opts_l='Formato', opts=['Unidad', 'Pack ahorro'],
    cats=[('Cosmética natural', 'p1'), ('Aceites esenciales', 'p2'), ('Infusiones', 'p3')])

S['merceria-mari-carmen'] = dict(
    who='none', still=True, h1='Lanas y labores,<br>a un clic.',
    hero=('32', 'soft balls of merino and mohair yarn in many colours with a wooden crochet hook'),
    banner=('04', 'the inside of a haberdashery shop with white shelves full of colourful balls of yarn from floor to ceiling, no people'),
    prods=[('01', 'a ball of rust orange merino wool yarn, no label', 'Lana merino'),
           (None, 'three gradient yarn cakes in rainbow tones', 'Ovillos degradados'),
           ('20', 'a red crochet triangle shawl with a long grey fringe on a hanger', 'Chal de ganchillo'),
           (None, 'a set of bamboo crochet hooks of different sizes in a floral fabric case', 'Juego de ganchillos'),
           ('30', 'a skein of natural raffia yarn and two round wooden bag handles', 'Kit bolso de rafia'),
           ('36', 'a cream crochet maxi dress with a fringed hem on a dressmaker mannequin', 'Patrón vestido de ganchillo')],
    l1=(None, 'hands crocheting a cream shawl with a wooden hook on a sunny garden table'),
    l2=('19', 'balls and cakes of yarn in many colours stacked in white shelf cubbies'),
    cats=[('Lanas', 'p1'), ('Kits', 'p5'), ('Accesorios', 'p4')])

S['lanas-paloma'] = dict(
    who='none', still=True,
    hero=('26', 'skeins of silky mohair yarn with sequins in mustard, orange and brown'),
    banner=(None, 'the inside of a long bright yarn shop in Málaga with white shelves full of colourful wool from floor to ceiling, no people'),
    prods=[('26', 'a skein of silky mohair yarn with tiny sequins in chocolate brown, no label', 'Mohair con lentejuelas'),
           ('30', 'a skein of lilac mohair yarn and a cake of mauve cotton yarn, no labels', 'Mohair lila'),
           ('34', 'spools of cotton cord yarn with sequins in blue and lime green, no labels', 'Cordón con lentejuelas'),
           ('21', 'cones of metallic silver and gold raffia yarn', 'Rafia metalizada'),
           ('01', 'a red knitted triangle shawl with a long red fringe (flat lay)', 'Kit chal con flecos'),
           ('29', 'a burnt orange crochet shawl with flower motifs and tassels (flat lay)', 'Kit chal de flores')],
    l1=('20', 'a multicolour knitted shawl with a long cream fringe draped over a wooden chair'),
    l2=(None, 'a knitting workshop table with yarn, needles and cups of coffee, seen from above'),
    cats=[('Lanas', 'p1'), ('Kits', 'p5'), ('Rafias', 'p4')])

S['fernandez-cruz-miguel'] = dict(
    who='none', still=True, eyebrow='Mercería y cofradías', h1='Tradición cofrade,<br>a un clic.',
    sub='Mercería, bordados y artículos de cofradía de nuestra tienda de {city}, con más de 80 años. Ahora, online.',
    hero=('13', 'gilded and silver-plated filigree flamenca hair combs on red damask'),
    banner=(None, 'the inside of a traditional haberdashery and religious goods shop in Málaga with wooden drawers, shelves of thread and red damask counters, no people'),
    prods=[('13', 'a gilded filigree hair comb', 'Peinecillo dorado'),
           ('25', 'a silver rosary with crystal beads and a crucifix', 'Rosario'),
           ('31', 'a red and green hand-painted wooden flamenco fan', 'Abanico'),
           ('23', 'an embroidered heraldic shield patch', 'Escudo bordado'),
           (None, 'a burgundy velvet balcony banner with a gold embroidered ornament and a gold fringe, no text', 'Balconera de terciopelo'),
           ('06', 'a silver-plated incense burner with chains', 'Incensario')],
    l1=(None, 'a burgundy velvet hood and a white cord belt laid on a wooden table with a rosary'),
    l2=('05', 'glass display drawers full of pins, needles and haberdashery in a traditional shop'),
    opts_l='Acabado', opts=['Dorado', 'Plateado'],
    cats=[('Cofradías', 'p1'), ('Rosarios', 'p2'), ('Bordados', 'p4')])

S['jaspe-art'] = dict(
    who='none', still=True,
    hero=('24', 'tubes of acrylic paint in pink, purple and blue with a palette knife and paint swatches'),
    banner=(None, 'the inside of a fine art supplies shop with walls of colourful paint tubes, brushes and canvases, no people'),
    prods=[('24', 'a set of acrylic paint tubes, no labels', 'Set de acrílicos'),
           ('23', 'a blank stretched cotton canvas and a jar of white gesso', 'Lienzo de algodón'),
           (None, 'a professional watercolour paint set in a metal tin with a brush', 'Acuarelas en pastilla'),
           ('07', 'three illustrated hardcover sketchbooks', 'Cuadernos ilustrados'),
           (None, 'a set of round and flat artist paintbrushes in a canvas roll', 'Juego de pinceles'),
           (None, 'a box of oil pastels in many colours', 'Pasteles al óleo')],
    l1=('31', 'a hand drawing an ocean wave in graphite and watercolour on paper'),
    l2=(None, 'an art workshop table with easels, paints and canvases in a bright studio'),
    opts_l='Formato', opts=['Unidad', 'Pack'],
    cats=[('Pintura', 'p1'), ('Lienzos', 'p2'), ('Cuadernos', 'p4')])

S['lanas-cachemir'] = dict(
    who='none', still=True, eyebrow='Lanas y chales hechos a mano', h1='Chales tejidos a mano,<br>a un clic.',
    hero=('24', 'handmade knitted wool shawls with long fluffy fringes draped over a wooden chair'),
    banner=(None, 'the inside of a wool shop in Gijón with white shelves full of colourful yarn and knitted shawls hanging, no people'),
    prods=[('16', 'a black knitted wool shawl with a long fringe (flat lay)', 'Chal negro de flecos'),
           ('15', 'a beige lace knitted shawl (flat lay)', 'Chal calado beige'),
           (None, 'a cream knitted wool shawl with a long fluffy mohair fringe, folded (flat lay)', 'Chal crudo de mohair'),
           ('33', 'an orange knitted shawl with a long brown fringe hung on a branch', 'Chal naranja y marrón'),
           (None, 'a turquoise knitted shawl with a long turquoise fringe (flat lay)', 'Chal turquesa'),
           (None, 'balls of soft cashmere blend yarn in grey, cream and camel', 'Lana cachemir')],
    l1=(None, 'a red knitted wool shawl with a long fringe draped over a stone wall by the sea'),
    l2=(None, 'a knitted striped jumper and balls of yarn on a wooden table in a wool shop'),
    cats=[('Chales', 'p1'), ('Lanas', 'p6'), ('Novedades', 'p4')])

S['botones-de-plata'] = dict(
    who='none', still=True, eyebrow='Joyería en plata y oro', h1='Plata a tu medida,<br>a un clic.',
    hero=('27', 'a pair of sterling silver cufflinks with an engraved monogram and a silver bangle on a tan leather saddle'),
    banner=(None, 'the inside of a silversmith workshop in Andalusia with a wooden workbench, tools and silver pieces, warm light, no people'),
    prods=[('17', 'a sterling silver bangle with a round engraved monogram disc', 'Brazalete con iniciales'),
           ('27', 'a pair of sterling silver cufflinks with an engraved monogram in a black box', 'Gemelos grabados'),
           ('37', 'a polished silver belt buckle with engraved initials on a tan leather belt', 'Hebilla de plata'),
           ('13', 'a sterling silver round medal pendant with a relief of a saint on a chain', 'Medalla de plata'),
           ('26', 'a stack of silver bangles with silver bead ends', 'Pulseras de bolas'),
           ('14', 'a silver pocket watch with an engraved monogram', 'Reloj de bolsillo')],
    l1=('08', "a man's wrist wearing a silver bangle and a watch"),
    l2=(None, 'a rider in a traditional Andalusian short jacket with silver buttons, seen from the chest down, holding leather reins'),
    opts_l='Acabado', opts=['Plata', 'Oro'],
    cats=[('Pulseras', 'p1'), ('Gemelos', 'p2'), ('Hebillas', 'p3')])

S['magdala-joyeria'] = dict(
    who='none', still=True, eyebrow='Joyería de autor', h1='Joyas tejidas a mano,<br>a un clic.',
    hero=('01', 'a gold woven wire cuff bracelet with a large blue stone'),
    banner=(None, 'a jewellery atelier with a wooden worktable, spools of gold wire, pliers and woven jewellery on white busts, soft daylight, no people'),
    prods=[('01', 'a gold woven wire cuff bracelet with a large blue stone', 'Brazalete con piedra azul'),
           ('20', 'a pair of green crystal flower drop earrings', 'Pendientes flor verde'),
           ('28', 'a pair of gold woven wire disc earrings', 'Pendientes de disco'),
           ('09', 'a gold woven wire necklace with grey stones on a white bust', 'Collar tejido'),
           ('05', 'a silver woven wire tube bracelet', 'Pulsera de plata tejida'),
           ('27', 'a white pearl flower bridal hair piece', 'Tocado de novia')],
    l1=(None, 'hands weaving fine gold wire with a crochet technique on a wooden table'),
    l2=('23', 'a white woven flower hair piece on a marble stand with red flowers'),
    opts_l='Acabado', opts=['Oro', 'Plata'],
    cats=[('Brazaletes', 'p1'), ('Pendientes', 'p2'), ('Novias', 'p6')])

S['ceramica-fajalauza'] = dict(
    who='none', still=True, eyebrow='Cerámica de Fajalauza desde 1517', h1='Cerámica de Granada,<br>a un clic.',
    hero=('04', 'a traditional Granada blue and green glazed ceramic teapot and cups'),
    banner=(None, 'the inside of a traditional pottery workshop in Granada with shelves of blue and green glazed ceramics and a potter wheel, no people'),
    prods=[('13', 'a blue and green glazed ceramic teapot with floral decoration', 'Tetera'),
           ('07', 'two glazed ceramic cups with green and blue decoration', 'Tazas con plato'),
           ('19', 'three rectangular ceramic trays with red, green and blue floral decoration', 'Bandejas'),
           ('32', 'glazed ceramic jugs in blue, green and red', 'Jarras'),
           ('31', 'a large glazed bowl with a blue bird decoration', 'Lebrillo'),
           ('37', 'a hand-painted ceramic tile with a colourful pattern', 'Azulejo')],
    l1=('21', 'a ceramic plate with a colourful salad on a sunny table'),
    l2=('33', 'glazed ceramic bowls and pots on a patterned tiled floor'),
    opts_l='Tamaño', opts=['Pequeño', 'Mediano', 'Grande'],
    cats=[('Mesa', 'p1'), ('Jarras', 'p4'), ('Azulejos', 'p6')])

S['merceria-san-garcia'] = dict(
    who='none', still=True,
    hero=('25', 'cakes of variegated cotton yarn in turquoise, cream and orange'),
    banner=(None, 'the inside of a haberdashery shop in Algeciras with bright green walls and shelves full of yarn and thread cones, no people'),
    prods=[('26', 'a hand-dyed skein of variegated wool yarn in red, green and orange autumn tones', 'Madeja otoño'),
           ('27', 'a hand-dyed skein of blue and grey wool yarn', 'Madeja azul noche'),
           ('16', 'cakes of soft yarn in pastel pink, coral, lilac and cream', 'Ovillos pastel'),
           ('23', 'a cake of variegated cotton yarn in beige and brown', 'Algodón degradado'),
           (None, 'a yellow crochet hook and a pair of bamboo knitting needles', 'Ganchillo y agujas'),
           ('40', 'a cream lace crochet triangle shawl', 'Patrón chal calado')],
    l1=(None, 'hands crocheting with a yellow crochet hook and pastel cotton yarn'),
    l2=('11', 'a crochet pattern chart printed on paper with a crochet hook beside it'),
    cats=[('Lanas', 'p1'), ('Accesorios', 'p5'), ('Patrones', 'p6')])

S['mina-mina'] = dict(
    who='none', still=True, eyebrow='Telas y taller en Gràcia', h1='Telas con alegría,<br>a un clic.',
    hero=('01', 'stacks of colourful printed cotton fabrics with Japanese patterns'),
    banner=('22', 'the inside of a colourful fabric shop in Barcelona with bolts of fabric, bunting and handmade bags on the walls, no people'),
    prods=[('01', 'folded printed cotton fabrics with Japanese patterns', 'Telas japonesas'),
           ('17', 'a stack of gingham check cotton fabrics', 'Telas vichy'),
           ('31', 'rolls of striped canvas fabric', 'Lona de rayas'),
           ('32', 'a colourful floral cotton print fabric', 'Algodón floral'),
           ('38', 'two cotton toiletry bags in blue and mustard, no labels', 'Neceser'),
           ('09', 'a red cotton fanny pack, no label', 'Riñonera')],
    l1=(None, 'a sewing table with printed fabric, scissors and a tape measure in a sunny shop'),
    l2=('34', 'colourful fabric bunting hung on a white wall'),
    opts_l='Medida', opts=['0,5 m', '1 m', '2 m'],
    cats=[('Telas', 'p1'), ('Hecho por nosotras', 'p5'), ('Lonas', 'p3')])

S['bordados-perales'] = dict(
    who='none', still=True, eyebrow='Taller de bordado y arte sacro', h1='Bordado en oro,<br>a un clic.',
    hero=('23', 'rich gold thread embroidery on black velvet with pink flowers'),
    banner=(None, 'the inside of an embroidery workshop in Seville with gold embroidered velvet mantles, banners and wooden embroidery frames, warm light, no people'),
    prods=[('30', 'gold embroidered flower appliqués', 'Aplicaciones bordadas'),
           ('08', 'a cream silk fabric with gold embroidery', 'Paño bordado en oro'),
           ('22', 'red velvet with silver and white embroidery', 'Bordado en terciopelo'),
           (None, 'a green velvet banner with gold embroidery and a gold fringe, no text', 'Estandarte bordado'),
           (None, 'a burgundy velvet cushion with gold embroidery', 'Cojín bordado'),
           (None, 'a cream liturgical stole with gold embroidered crosses', 'Estola bordada')],
    l1=('38', 'hands embroidering gold thread on cream fabric stretched on a wooden frame'),
    l2=('37', 'close-up of gold and silver thread embroidery on blue and black fabric'),
    opts_l='Tamaño', opts=['Pequeño', 'Mediano', 'Grande'],
    cats=[('Aplicaciones', 'p1'), ('Bordados', 'p2'), ('Encargos', 'p4')])

S['cocorola'] = dict(
    who='none', still=True, eyebrow='Mercería y complementos', h1='Hecho a mano,<br>con botones.',
    hero=('02', 'a crochet collar necklace decorated with colourful vintage buttons'),
    banner=(None, 'a colourful haberdashery stall in a Barcelona flea market with jars of buttons, spools of thread and handmade necklaces, no people'),
    prods=[('02', 'a cream crochet collar necklace with colourful buttons', 'Collar de botones'),
           ('21', 'a necklace with a fringe of pink and red raffia strips', 'Collar de rafia'),
           ('20', 'a cream crochet loop collar necklace', 'Collar de ganchillo'),
           ('06', 'a blue floral sewing kit case with threads, scissors and a tape measure', 'Costurero de viaje'),
           ('31', 'spools of metallic thread in silver, gold and copper', 'Hilos metalizados'),
           ('41', 'a rust red crochet shoulder bag', 'Bolso de ganchillo')],
    l1=('17', 'a rust red knitted triangle shawl with ruffles on a mannequin'),
    l2=('23', 'a large striped red and yellow wooden button'),
    cats=[('Collares', 'p1'), ('Mercería', 'p4'), ('Bolsos', 'p6')])

S['madejas-tejerlo'] = dict(
    who='none', still=True,
    hero=('17', 'hand-dyed turquoise wool skeins on green grass'),
    banner=(None, 'the inside of a yarn shop in Galicia with stone walls and wooden shelves full of hand-dyed skeins, no people'),
    prods=[('07', 'hand-dyed skeins of white wool with red speckles, no label', 'Madeja jaspeada'),
           ('28', 'a hand-dyed skein in orange, grey and teal', 'Madeja Albolafia'),
           ('29', 'a gradient yarn cake in grey, orange and burgundy', 'Ovillo degradado'),
           ('36', 'gradient yarn cakes in green, purple and silver, no labels', 'Ovillos de colores'),
           ('39', 'mini skeins of wool in blue, orange and pink in a kraft box', 'Kit mini madejas'),
           ('37', 'a pink and navy crochet basket filled with yarn', 'Cesta de trapillo')],
    l1=('19', 'a knitted shawl in coral and grey draped over a chair'),
    l2=('16', 'a turquoise skein and a knitting project next to red geraniums'),
    cats=[('Madejas', 'p1'), ('Ovillos', 'p3'), ('Kits', 'p5')])

S['bisuterapia'] = dict(
    who='none', still=True, eyebrow='Bisutería hecha a mano', h1='Bisutería de autor,<br>a un clic.',
    hero=('37', 'a pair of ceramic sacred heart earrings with flowers and coloured beads'),
    banner=(None, 'the inside of a small jewellery boutique in Murcia with wooden busts, necklaces and earrings on display stands, warm light, no people'),
    prods=[('37', 'ceramic sacred heart earrings with pink flowers and beads', 'Pendientes corazón'),
           ('07', 'long earrings with cream flowers and red beads', 'Pendientes de flores'),
           ('14', 'a red beaded choker with crystal drops', 'Gargantilla roja'),
           ('12', 'a wooden bead necklace with a painted round pendant', 'Collar con colgante'),
           ('16', 'a burgundy leaf statement necklace', 'Collar de hojas'),
           ('40', 'striped black and cream disc earrings with a black leaf drop', 'Pendientes de rayas')],
    l1=(None, 'a woman wearing statement earrings and a beaded necklace, seen from the side from the lips down'),
    l2=('34', 'a display of colourful bracelets on a wooden stand'),
    opts_l='Acabado', opts=['Dorado', 'Plateado'],
    cats=[('Pendientes', 'p1'), ('Collares', 'p4'), ('Gargantillas', 'p3')])

S['my-scrap-place'] = dict(
    who='none', still=True, eyebrow='Tienda-taller de scrapbooking', h1='Todo para tu scrap,<br>a un clic.',
    hero=('16', 'a floral scrapbook mini album with ribbons, scissors and patterned paper'),
    banner=('27', 'the inside of a scrapbooking shop with wooden shelves of paper pads and a patterned tiled floor, no people'),
    prods=[('16', 'a floral handmade mini album', 'Mini álbum floral'),
           ('25', 'jars of texture paste and stencils with geometric patterns, no labels', 'Pastas y plantillas'),
           ('11', 'scrapbooking tools: cutting mat, scoring board, scissors, bone folder and craft knife', 'Kit de herramientas'),
           ('05', 'four handmade greeting cards', 'Pack de tarjetas'),
           ('13', 'handmade decorated tags with ribbons', 'Etiquetas decoradas'),
           ('40', 'an accordion photo album with patterned paper', 'Álbum acordeón')],
    l1=('15', 'an open scrapbook album with photos and decorations on a wooden table'),
    l2=('24', 'colourful ribbons around a small handmade tag book on a wooden table'),
    opts_l='Formato', opts=['Unidad', 'Pack'],
    cats=[('Álbumes', 'p1'), ('Herramientas', 'p3'), ('Tarjetas', 'p4')])

S['fga-equitacion'] = dict(
    who='none', still=True, eyebrow='Doma vaquera y clásica', h1='Todo para montar,<br>a un clic.',
    hero=('16', 'a grey wide-brimmed Andalusian riding hat on a leather saddle'),
    banner=(None, 'the inside of an equestrian shop with wooden shelves, saddles, bridles and riding hats on the walls, no people'),
    prods=[('09', 'a black velvet riding helmet', 'Casco de equitación'),
           ('16', 'a grey wide-brimmed Andalusian riding hat', 'Sombrero de ala ancha'),
           ('34', 'a pair of tall black leather riding boots', 'Botas de montar'),
           ('05', 'a pair of red fleece horse leg wraps', 'Vendas de descanso'),
           ('06', 'a houndstooth wool flat cap', 'Gorra de tweed'),
           ('18', 'brown leather Andalusian riding chaps with tooled decoration', 'Zahones')],
    l1=(None, 'a vaquera saddle with a sheepskin seat cover on a wooden stand in a stable'),
    l2=('31', 'a silver pocket watch on a white sheepskin'),
    cats=[('Jinete', 'p1'), ('Caballo', 'p4'), ('Botas', 'p3')])

S['nexus-tabletop'] = dict(
    who='none', still=True, eyebrow='Juegos de mesa y miniaturas', h1='Tu próxima partida,<br>a un clic.',
    hero=(None, 'a fantasy wargame table with painted miniature knights, ruined stone buildings, dice and a measuring tape'),
    banner=(None, 'the inside of a tabletop gaming shop with gaming tables, terrain and shelves full of board game boxes, no people, no logos'),
    prods=[(None, 'a box of unpainted grey plastic fantasy knight miniatures on sprues, plain packaging, no logos', 'Caja de miniaturas'),
           (None, 'a set of 24 small miniature paint pots in many colours, no labels', 'Set de pinturas'),
           (None, 'a set of seven polyhedral dice in translucent purple', 'Dados de rol'),
           (None, 'a sealed box of trading card booster packs in plain packaging, no logos', 'Caja de sobres'),
           (None, 'ruined gothic building terrain pieces for wargames', 'Escenografía'),
           (None, 'a set of fine miniature paint brushes', 'Pinceles de detalle')],
    l1=(None, "players' hands moving painted fantasy miniatures on a wargame table with terrain"),
    l2=(None, 'a hand painting a small fantasy knight miniature with a fine brush under a lamp'),
    cats=[('Miniaturas', 'p1'), ('Pinturas', 'p2'), ('Cartas', 'p4')])

S['dmario-tejidos'] = dict(
    who='none', still=True, eyebrow='Tejidos para cofradías y fallas', h1='Telas de cofradía,<br>a un clic.',
    hero=('20', 'black and gold brocade fabric'),
    banner=('09', 'a fabric warehouse with tall racks of colourful fabric rolls, no people'),
    prods=[('14', 'a black and gold damask brocade fabric', 'Brocado negro y oro'),
           ('10', 'a light blue and cream damask fabric', 'Damasco azul y crudo'),
           ('21', 'a purple and gold brocade fabric', 'Brocado morado'),
           (None, 'rolls of burgundy, green and navy velvet fabric', 'Terciopelo'),
           ('23', 'gold and yellow fringes and trims', 'Flecos dorados'),
           ('05', 'white tulle embroidered with gold sequins', 'Tul bordado')],
    l1=('06', 'rolls of emerald green and cream damask fabric'),
    l2=('16', 'grey and silver damask fabric draped in folds'),
    opts_l='Medida', opts=['1 m', '2 m', '5 m'],
    cats=[('Brocados', 'p1'), ('Terciopelos', 'p4'), ('Pasamanería', 'p5')])

S['juguetes-duba'] = dict(
    who='none', still=True, eyebrow='Radiocontrol y juguetes', h1='Radiocontrol,<br>a un clic.',
    hero=('33', 'a pink 1:8 nitro RC racing car on a race track, no logos, no stickers'),
    banner=('28', 'the inside of a radio control hobby shop with walls full of spare parts, tyres and RC cars, no people, no logos'),
    prods=[('39', 'a green 1:10 RC rock crawler off-road truck, no logos', 'Crawler 1:10'),
           ('33', 'a pink 1:8 GT nitro RC car, no logos', 'Coche GT8 nitro'),
           ('30', 'an unpainted white and blue RC car body shell', 'Carrocería'),
           (None, 'an orange 1:10 electric RC buggy, no logos', 'Buggy eléctrico 1:10'),
           (None, 'a black RC pistol-grip radio transmitter, no logos', 'Emisora 2,4 GHz'),
           (None, 'a set of four RC car wheels with white rims and slick tyres', 'Juego de ruedas')],
    l1=('26', 'an RC race track with red and white kerbs on a sunny day, no people'),
    l2=('29', 'shelves of RC parts and tyres in a hobby shop, no logos'),
    opts_l='Versión', opts=['RTR', 'Kit'],
    cats=[('Coches', 'p1'), ('Recambios', 'p3'), ('Emisoras', 'p5')])

S['teixits-donna'] = dict(
    who='none', still=True, eyebrow='Tienda de telas en Barcelona', h1='Telas para crear,<br>a un clic.',
    hero=('22', 'rolls of sequined and embroidered lace fabrics in many colours'),
    banner=(None, 'the inside of a large fabric shop in Barcelona with shelves full of fabric bolts and long cutting tables, no people'),
    prods=[('18', 'a printed silk fabric with colourful swirls', 'Seda estampada'),
           ('37', 'double gauze muslin fabric in sage, navy and mustard', 'Muselina'),
           ('22', 'embroidered sequin lace fabric', 'Encaje con lentejuelas'),
           ('21', 'a resinated cotton tablecloth fabric with a botanical print', 'Tela resinada'),
           ('27', 'printed satin fabrics with floral and animal prints', 'Rasos estampados'),
           ('31', 'batik cotton fabrics in red and green', 'Batiks')],
    l1=(None, 'a dressmaker table with fabric, scissors, a tape measure and paper patterns'),
    l2=('24', 'pink feather appliqués with sequined flowers'),
    opts_l='Medida', opts=['0,5 m', '1 m', '2 m'],
    cats=[('Sedas', 'p1'), ('Algodones', 'p2'), ('Fiesta', 'p3')])

S['scrapa2'] = dict(
    who='none', still=True, eyebrow='Scrapbooking y lettering', h1='Papeles y talleres,<br>a un clic.',
    hero=('12', 'a handmade herbarium notebook with a pressed fern and burlap'),
    banner=(None, 'a bright scrapbooking shop and workshop in Zaragoza with shelves of patterned paper pads and a large work table, no people'),
    prods=[('12', 'a handmade herbarium notebook with a fern', 'Cuaderno herbario'),
           ('31', 'a pad of floral patterned scrapbooking paper', 'Bloc de papeles'),
           ('23', 'sticker packs with illustrations and washi tape', 'Pegatinas'),
           ('34', 'small spiral notebooks with gingham covers', 'Libretas'),
           ('16', 'a green macramé Christmas tree wall hanging', 'Árbol de macramé'),
           ('26', 'a striped journaling notebook with washi tapes', 'Kit de journaling')],
    l1=('30', 'a striped notebook, washi tapes and a candle on a wooden desk'),
    l2=('10', 'a pad of Christmas patterned papers on a table with a small tree'),
    opts_l='Formato', opts=['Unidad', 'Pack'],
    cats=[('Cuadernos', 'p1'), ('Papeles', 'p2'), ('Talleres', 'p5')])

S['cast-tejidos'] = dict(
    who='none', still=True, eyebrow='Tejidos de flamenca y fiesta', h1='Telas de flamenca,<br>a un clic.',
    hero=('39', 'red polka dot flamenco fabric folded'),
    banner=(None, 'a large fabric warehouse in Seville with walls of colourful fabric rolls, no people'),
    prods=[('39', 'white fabric with red polka dots', 'Lunares rojos'),
           ('25', 'black and white polka dot fabrics and teal with white dots', 'Lunares'),
           ('01', 'pink embroidered lace fabric', 'Encaje bordado'),
           ('07', 'a black fabric embroidered with pink flowers and green leaves', 'Bordado floral'),
           ('18', 'a red and white jacquard fabric', 'Jacquard'),
           ('42', 'a black fabric printed with large red and blue flowers with a long fringe', 'Tela de mantón')],
    l1=('05', 'stacks of white lace fabrics'),
    l2=(None, 'rolls of colourful printed flamenco fabrics on a cutting table'),
    opts_l='Medida', opts=['1 m', '2 m', '5 m'],
    cats=[('Lunares', 'p1'), ('Encajes', 'p3'), ('Novedades', 'p5')])

S['alfares-sevilla'] = dict(
    who='none', still=True, eyebrow='Taller de piezas de belén', h1='Tu belén,<br>a un clic.',
    hero=('23', 'a miniature nativity scene basket of pumpkins'),
    banner=(None, 'the inside of a nativity scene workshop shop in Seville with shelves full of handmade clay figures and miniature market stalls, no people'),
    prods=[('23', 'a miniature basket of pumpkins for a nativity scene', 'Cesta de calabazas'),
           ('22', 'a miniature basket of salmon steaks for a nativity scene', 'Cesta de salmón'),
           ('24', 'miniature cheeses for a nativity scene', 'Quesos'),
           ('29', 'miniature hanging hams for a nativity scene', 'Jamones colgados'),
           ('40', 'miniature clay pots of olives', 'Tinajas de aceitunas'),
           ('42', 'miniature demijohns in wicker baskets', 'Damajuanas')],
    l1=('14', 'a miniature market stall full of fruit and vegetables in a nativity scene'),
    l2=('37', 'a miniature aged clay amphora'),
    opts_l='Escala', opts=['12 cm', '18 cm'],
    cats=[('Cestas', 'p1'), ('Bodegón', 'p3'), ('Cerámica', 'p5')])

S['esparto-antonio-lopez'] = dict(
    who='none', still=True, eyebrow='Esparto artesano de Chiclana', h1='Esparto de siempre,<br>a un clic.',
    hero=('09', 'handmade esparto grass baskets and a woven esparto donkey'),
    banner=(None, 'an esparto grass craft workshop in Andalusia with baskets, mats and woven animals hanging from the ceiling, no people'),
    prods=[('11', 'a round esparto grass basket', 'Canasto de esparto'),
           ('36', 'a round esparto rug', 'Alfombra de esparto'),
           ('33', 'a rolled esparto blind', 'Persiana de esparto'),
           ('02', 'a large woven esparto horse sculpture', 'Caballo de esparto'),
           ('05', 'esparto pendant lamp shades', 'Lámpara de esparto'),
           ('30', 'a wooden chair with a woven seat and back', 'Silla de anea')],
    l1=('09', 'esparto baskets stacked on shelves'),
    l2=(None, 'an esparto basket with lemons on a whitewashed patio in Andalusia'),
    opts_l='Tamaño', opts=['Pequeño', 'Mediano', 'Grande'],
    cats=[('Cestería', 'p1'), ('Hogar', 'p2'), ('Piezas únicas', 'p4')])

S['art-antic'] = dict(
    who='none', still=True, eyebrow='Fabricantes de aderezos', h1='Aderezos de valenciana,<br>a un clic.',
    hero=('01', 'a gold and pearl Valencian jewellery set with earrings, a brooch and a pearl necklace'),
    banner=(None, 'the inside of a traditional jewellery workshop in Valencia with glass display cases of gold and pearl jewellery, warm light, no people'),
    prods=[('01', 'a pair of gold filigree earrings with pearls', 'Pendientes de aderezo'),
           ('01', 'a multi-strand pearl necklace with a gold filigree pendant', 'Collar de perlas'),
           ('12', 'a gold brooch with pearls and coloured stones', 'Joya de pecho'),
           (None, 'a set of three gold filigree hair pins for a traditional Valencian hairstyle', 'Agujas de moño'),
           (None, 'a gold hair comb with filigree', 'Peineta'),
           (None, 'gold filigree bridal earrings with a pearl drop', 'Pendientes de novia')],
    l1=(None, 'a woman fastening a gold filigree and pearl earring, close-up from the lips down'),
    l2=(None, 'gold and pearl jewellery pieces on a black velvet tray'),
    opts_l='Acabado', opts=['Oro', 'Plata'],
    cats=[('Pendientes', 'p1'), ('Collares', 'p2'), ('Peinetas', 'p5')])

S['sederias-natalia'] = dict(
    who='none', still=True, eyebrow='Sederías y bordados', h1='Bordados y tradición,<br>a un clic.',
    hero=('07', 'a red hand-embroidered silk manila shawl with a long fringe'),
    banner=(None, 'the inside of a traditional haberdashery and silk shop in Zaragoza with shelves of boxes, embroidered shawls and fabrics, no people'),
    prods=[('07', 'a red hand-embroidered silk manila shawl', 'Mantón bordado a mano'),
           ('08', 'a blue printed shawl with a long fringe on a mannequin', 'Mantón aragonés'),
           ('31', 'a red and black checked traditional vest', 'Chaleco de la Ribagorza'),
           ('33', 'traditional embroidered garters with tassels', 'Atapiernas'),
           ('06', 'a personalized wooden snowflake tea light holder', 'Portavelas personalizado'),
           ('36', 'a purple patterned skirt and shawl set on a mannequin', 'Falda y mantón')],
    l1=('03', 'a traditional Aragonese costume with an embroidered blue apron on a mannequin'),
    l2=('02', 'rolls of traditional patterned fabrics in red and blue'),
    cats=[('Mantones', 'p1'), ('Indumentaria', 'p3'), ('Regalos', 'p5')])

S['roda-peinetas'] = dict(
    who='none', still=True, eyebrow='Orfebres desde 1950', h1='Peinetas y aderezos,<br>a un clic.',
    hero=('17', 'a gold and pearl Valencian jewellery set with earrings, a brooch, hair pins and a pearl necklace on black'),
    banner=(None, 'a traditional goldsmith shop in Valencia with wooden display cases full of gold combs and jewellery, warm light, no people'),
    prods=[('16', 'a gold filigree jewellery set with green stones', 'Aderezo verde'),
           ('17', 'a gold and pearl jewellery set', 'Aderezo de perlas'),
           ('18', 'a gold jewellery set with garnet red stones and a cross', 'Aderezo granate'),
           ('19', 'a gold and topaz jewellery set with a pearl choker', 'Aderezo topacio'),
           ('35', 'a multi-strand pearl choker with a gold bow pendant', 'Collar de perlas'),
           (None, 'a gold Valencian hair comb with filigree', 'Peineta de oro')],
    l1=(None, 'a traditional Valencian hairstyle with gold hair pins and a comb, seen from behind'),
    l2=(None, 'gold hair pins and combs laid on black velvet'),
    opts_l='Acabado', opts=['Oro', 'Plata'],
    cats=[('Aderezos', 'p1'), ('Collares', 'p5'), ('Peinetas', 'p6')])
