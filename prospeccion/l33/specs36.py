# Lote 36 (13/11/2026): las 19 del scrapeo del 10/11 que faltaban (10 ópticas y 9 de calzado y deporte).
# Referencias NN = ~/Downloads/l36src/<slug>/NN.jpg (sus últimas 32 publicaciones de Instagram). Se carga desde specs.py (exec) y usa su S.
# «crops»: referencia recortada (NNc) = (original, (x0, y0, x1, y1) en fracciones), para quitar caras, textos o logos.
# Ref None = sin referencia: casi todas las ópticas publican vídeos a cámara, sin fotos de producto.
# Nunca referencias con menores: fuera Vivavisión 29 y 31, Valdevisión 06, Óptica Tenerife 23, Lupitas 24 y 25, Santa Ana 32.

# ---------------- calzado (zapaterías: tienda clara)
S['burgos-zapaterias'] = dict(
    place='a sunny whitewashed street in Azuaga, Badajoz, Spain, with the stone tower of the parish church behind', who='woman', light=True,
    eyebrow='Zapatería en Azuaga', h1='Tus zapatos,<br>a un clic.',
    hero=('05', 'cognac suede pointed knee-high boots with a slim heel, worn with brown leather trousers and a croc-effect tote bag'),
    banner=('21', 'the inside of a shoe shop with white glowing shelves full of boots, ankle boots and handbags, a light marble floor, no people, no logos'),
    prods=[('05', 'cognac suede pointed knee-high boots with a slim heel, no logos', 'Bota alta de ante'),
           ('07', 'pointed ankle boots in fawn-print calf hair with a gold metal toe cap and a black block heel, no logos', 'Botín estampado'),
           ('04', 'black leather pointed mid-calf boots with a buckle strap and a slim heel, no logos', 'Bota negra con hebilla'),
           ('13', 'black leather loafers with a gold horsebit, no logos', 'Mocasín con hebilla dorada'),
           ('18', 'brown leather pointed slingback pump shoes with cut-out straps and a bow, no logos', 'Salón destalonado'),
           ('10', 'light grey suede ankle boots with fringes and a low block heel, no logos', 'Botín con flecos')],
    l1=('12', 'black leather horsebit loafers worn with cuffed light jeans and a zebra-print clutch, framed from the knees down'),
    l2=('15', 'flat black sandals with crystal-studded braided straps next to a black crystal clutch, no logos'),
    cats=[('Botas', 'p1'), ('Botines', 'p2'), ('Fiesta', 'p5')])

S['calzados-hermanos-lopez'] = dict(
    place='the riverside promenade of Ayamonte, Huelva, Spain, with white houses and boats on the Guadiana river', who='woman', light=True,
    hero=('03', 'brown suede knee-high boots with a block heel, worn with a cream knit midi dress'),
    banner=('24', 'the inside of a shoe shop with white wall shelves full of shoes, boots and handbags and tall green plants, no people, no logos'),
    prods=[('02', 'dark brown leather knee-high boots with a block heel, no logos', 'Bota alta de piel'),
           ('17', 'dark brown leather ankle boots with a block heel and a gold buckle strap, no logos', 'Botín con hebilla'),
           ('21', 'dark brown suede slouchy knee boots with a block heel, no logos', 'Bota arrugada'),
           ('12', 'a taupe suede fringed bucket bag with a long strap, no logos', 'Bolso de flecos'),
           ('06c', "men's navy suede lace-up moccasin ankle boots with a thick grey sole, no logos", 'Botín de hombre'),
           ('10', 'cognac suede low sneakers with a snake-print heel tab and a cream sole, no logos', 'Zapatilla de ante')],
    l1=('30', 'black leather pointed ankle boots with tiny studs and a kitten heel, worn with straight jeans, framed from the knees down'),
    l2=('26c', 'leopard-print fluffy slipper flats on a soft cream rug, no logos'),
    cats=[('Botas', 'p1'), ('Botines', 'p2'), ('Bolsos', 'p4')],
    crops={'06c': ('06', (0.0, 0.38, 1.0, 1.0)), '26c': ('26', (0.0, 0.16, 1.0, 1.0))})

S['calzados-cane'] = dict(
    place='the seafront promenade of Benicarló, Castellón, Spain, with palm trees and the marina', who='woman', light=True,
    eyebrow='Calzado cómodo en Benicarló', h1='Cómodos.<br>Y a un clic.',
    hero=('01', 'dark brown leather lace-up comfort shoes with a side zip and a wedge sole, worn with jeans and a camel coat, walking on autumn leaves'),
    banner=(None, 'the inside of a bright family shoe shop with glass shop windows, light wooden shelves of comfort shoes and boots, no people, no logos'),
    prods=[('02', 'metallic bronze and pewter comfort sneakers with laces and a light wedge sole, no logos', 'Deportiva metalizada'),
           ('05c', 'taupe suede waterproof wedge ankle boots lined with shearling, no logos', 'Botín waterproof'),
           ('15c', 'brown and black leather ankle boots with a block heel and a buckle strap, no logos', 'Botín con hebilla'),
           ('30', 'black patent leather Mary Jane shoes with two straps and a block heel, no logos', 'Merceditas de charol'),
           ('13', "men's dark brown suede lace-up casual shoes with a light sole, no logos", 'Zapato de hombre'),
           ('27c', 'burgundy and cream leather slip-on comfort sneakers with elastic laces, no logos', 'Deportiva elástica')],
    l1=('32c', 'a black leather ankle boot with a buckle and a block heel standing on green grass, no logos'),
    l2=('12', "men's tan and brown suede casual lace-up shoes on terracotta tiles, no logos"),
    cats=[('Botines', 'p2'), ('Comodidad', 'p1'), ('Hombre', 'p5')],
    crops={'05c': ('05', (0.0, 0.2, 1.0, 1.0)), '15c': ('15', (0.0, 0.0, 1.0, 0.76)),
           '27c': ('27', (0.0, 0.2, 1.0, 1.0)), '32c': ('32', (0.0, 0.25, 1.0, 1.0))})

S['acouga'] = dict(
    place='a quiet granite street in Salvaterra de Miño, Pontevedra, Spain, near the Miño river, with green trees', who='woman', light=True,
    eyebrow='Zapatería en Salvaterra', h1='Pisa bonito.<br>Pide fácil.',
    hero=('20c', 'brown leather western cowboy boots with stitching, worn with a long dark skirt and a cream jumper'),
    banner=(None, 'a cosy shoe shop with a dark green velvet armchair, eucalyptus branches in vases, wooden shelves of boots and bags and a light patterned rug, no people, no logos'),
    prods=[('08', 'burgundy suede lace-up barefoot ankle boots with a thin flexible sole, no logos', 'Botín barefoot burdeos'),
           ('07c', 'black leather chelsea barefoot ankle boots with elastic sides and a thin sole, no logos', 'Chelsea barefoot'),
           ('27c', 'taupe suede pointed ballet flats with a strap and small gold studs, no logos', 'Bailarina con tachas'),
           ('20c', 'brown leather western cowboy boots with stitching, no logos', 'Bota cowboy'),
           ('22c', 'a black leather slouchy shoulder bag, no logos', 'Bolso de piel negro'),
           ('26', 'a black knitted hood scarf with a drawstring, no logos', 'Capucha de punto')],
    l1=('25', 'eucalyptus branches in a vase next to a black knitted hood and black studded ballet flats on a velvet armchair, no logos'),
    l2=('32c', "children's rain boots in black and pink on a light rug, no logos, no people"),
    cats=[('Botines', 'p1'), ('Bailarinas', 'p3'), ('Bolsos', 'p5')],
    crops={'20c': ('20', (0.4, 0.3, 1.0, 1.0)), '07c': ('07', (0.0, 0.15, 1.0, 1.0)), '27c': ('27', (0.0, 0.27, 1.0, 0.53)),
           '22c': ('22', (0.0, 0.3, 0.62, 1.0)), '32c': ('32', (0.0, 0.3, 1.0, 1.0))})

S['zapateria-buades'] = dict(
    place='a sunny stone street with green wooden shutters in the old town of Artà, Mallorca, Spain', who='woman', light=True,
    eyebrow='Calzado y bolsos en Mallorca', h1='Zapatos y bolsos<br>que se notan.',
    hero=('03c', 'black leather platform ankle boots with a block heel, worn with a long beige skirt and a white shirt'),
    banner=('05', 'the inside of a minimalist white shoe and bag shop with lit niche shelves of handbags and white display plinths with sneakers, no people, no logos'),
    prods=[('02', 'dark brown suede chelsea ankle boots with a chunky lug sole, no logos', 'Chelsea de ante'),
           ('05c', 'retro running sneakers in white with brown suede panels and in dark brown suede, no logos', 'Zapatilla retro'),
           ('03c', 'black leather platform ankle boots with a block heel, no logos', 'Botín plataforma'),
           ('06c', 'a red leather tote handbag with gold hardware, no logos', 'Bolso rojo de piel'),
           (None, 'tan leather loafers with a thin gold bar, no logos', 'Mocasín de piel'),
           (None, 'a cream leather crossbody bag with a short top handle, no logos', 'Bolso cruzado crema')],
    l1=(None, 'a woman in a white shirt and wide jeans holding a brown leather handbag in a stone street of a Mallorcan village, framed from the shoulders down'),
    l2=(None, 'white lit niche shelves with handbags in white, black and tan, no logos, no people'),
    cats=[('Botines', 'p3'), ('Zapatillas', 'p2'), ('Bolsos', 'p4')],
    crops={'03c': ('03', (0.0, 0.45, 1.0, 1.0)), '05c': ('05', (0.0, 0.5, 1.0, 0.9)), '06c': ('06', (0.0, 0.6, 0.5, 1.0))})

S['mapi-shoes'] = dict(
    place='a sunny square with palm trees in San Vicente del Raspeig, Alicante, Spain', who='woman', light=True,
    eyebrow='Calzado a buen precio', h1='Tus zapatos,<br>a un clic.',
    hero=('14c', 'brown suede fringed western knee boots, worn with a short black dress'),
    banner=(None, 'the inside of a big bright shoe shop with long white shelves full of boots, shoes and sandals and a light floor, no people, no logos'),
    prods=[('14c', 'brown suede fringed western knee boots with a low heel, no logos', 'Bota de flecos'),
           ('12', 'burgundy suede pointed pump shoes with a kitten heel and a draped front, no logos', 'Salón de ante burdeos'),
           ('03', 'studded suede ballet flat shoes in beige and black, no logos', 'Bailarina con tachas'),
           ('07', 'brown and tan suede square-toe ballet flat shoes with criss-cross laces, no logos', 'Bailarina de cordones'),
           ('02c', 'magenta suede pointed stiletto pump shoes, no logos', 'Stiletto fucsia'),
           ('28c', 'black suede strappy wedge espadrille sandal shoes with a jute wedge, no logos', 'Cuña de esparto')],
    l1=('24c', 'black suede fringed wedge sandals with a jute sole, worn, feet and ankles only'),
    l2=('32c', 'three pairs of footbed sandal shoes with buckles in black, tan and white on a white surface, no logos'),
    cats=[('Botas', 'p1'), ('Tacones', 'p2'), ('Bailarinas', 'p3')],
    crops={'14c': ('14', (0.0, 0.35, 1.0, 1.0)), '02c': ('02', (0.0, 0.0, 1.0, 0.58)), '28c': ('28', (0.3, 0.35, 1.0, 1.0)),
           '24c': ('24', (0.4, 0.3, 1.0, 1.0)), '32c': ('32', (0.0, 0.46, 1.0, 0.7))})

S['calzados-guillen'] = dict(
    place='a sunny street with whitewashed houses in Elche de la Sierra, Albacete, Spain, with green hills behind', who='woman', light=True,
    eyebrow='Zapatería de tendencias', h1='Tendencia<br>a tus pies.',
    hero=('20', 'tan suede western ankle boots with embroidery, studs and a side zip, worn with cropped jeans'),
    banner=(None, 'the inside of a bright shoe shop with light wooden floor, glass shelves of sneakers and boots and a wall of handbags, no people, no logos'),
    prods=[('20', 'tan suede western ankle boots with embroidery, small studs and a side zip, no logos', 'Botín camperos'),
           ('06', 'black leather pointed ankle boots with a slim heel, no logos', 'Botín de tacón'),
           ('16', 'brown suede and nylon retro running sneakers, no logos', 'Zapatilla retro'),
           ('25', 'tan suede low sneakers with gold stripes and a glitter heel tab, no logos', 'Zapatilla con brillo'),
           ('30', 'a black woven leather hobo bag with a gold metal handle, no logos', 'Bolso trenzado'),
           ('10', 'a black soft leather shoulder bag with a knotted handle, no logos', 'Bolso de nudo')],
    l1=('13', 'a brown quilted nylon crossbody bag with a wide black strap, no logos'),
    l2=('27', "men's navy suede and mesh running sneakers with a burgundy heel and a gum sole, no logos"),
    cats=[('Botines', 'p1'), ('Zapatillas', 'p3'), ('Bolsos', 'p5')])

# ---------------- deporte (tienda oscura, niche sneakers)
S['ibaimendi-kirolak'] = dict(
    place='a street in the old town of Hernani, Gipuzkoa, Spain, with green mountains behind', who='man',
    eyebrow='Deporte y montaña', h1='Sal ahí fuera.<br>Equipado.',
    hero=('17c', 'a mustard yellow quilted puffer jacket with a dark grey yoke and chest pockets, worn with dark jeans and trail shoes, no logos'),
    banner=(None, 'the inside of a mountain and sports shop with wooden shelves of hiking boots and trail running shoes, racks of technical jackets and lime green accents, no people, no logos'),
    prods=[('30c', 'a long dark teal waterproof parka with a hood, no logos', 'Parka impermeable'),
           ('25c', 'trail running shoes in grey, yellow and blue, no logos', 'Zapatilla de trail'),
           ('07c', 'road running shoes in light blue, white with yellow and mint green, no logos', 'Zapatilla de running'),
           ('17c', 'a mustard yellow quilted puffer jacket with a dark grey yoke, no logos', 'Plumífero mostaza'),
           ('32c', 'a navy quilted padded vest over a dark knitted jumper, no logos', 'Chaleco acolchado'),
           ('22c', 'retro sneakers in pink, brown and white suede, no logos', 'Zapatilla retro')],
    l1=(None, 'a hiker in a technical jacket and hiking boots walking on a green mountain ridge in the Basque Country, seen from behind, no logos'),
    l2=(None, 'brown leather hiking boots on a wooden bench in a mountain shop, no logos'),
    cats=[('Chaquetas', 'p1'), ('Running', 'p3'), ('Montaña', 'p2')],
    crops={'17c': ('17', (0.0, 0.1, 1.0, 1.0)), '30c': ('30', (0.0, 0.18, 0.5, 0.9)), '25c': ('25', (0.0, 0.2, 0.5, 0.75)),
           '07c': ('07', (0.3, 0.45, 0.95, 0.63)), '32c': ('32', (0.0, 0.12, 1.0, 1.0)), '22c': ('22', (0.25, 0.48, 0.8, 1.0))})

S['yaiza-sport'] = dict(
    place='a sunny street with palm trees in Tejina, Tenerife, Spain, with green hills behind', who='woman',
    eyebrow='Deporte para todos', h1='Tu deporte,<br>a un clic.',
    hero=(None, 'a black zip training jacket, black leggings and white running shoes, no logos'),
    banner=(None, 'the inside of a big sports shop with walls of shoe boxes in red and blue, shelves of sneakers, racks of sportswear and balls hanging from the ceiling, no people, no logos'),
    prods=[('09', 'black mesh sneakers with two velcro straps and a non-slip sole, no logos', 'Zapatilla de velcro'),
           ('22c', 'white running shoes with grey details, no logos', 'Zapatilla blanca'),
           (None, 'colourful running shoes in orange, purple and yellow with a thick foam sole, no logos', 'Zapatilla de running'),
           (None, 'a burgundy hoodie with a white chest print, no logos', 'Sudadera burdeos'),
           ('02c', 'colourful flip-flop sandal shoes and pool slider shoes, no logos', 'Chanclas'),
           (None, 'a black sports backpack with many pockets, no logos', 'Mochila deportiva')],
    l1=(None, 'a woman jogging on a seafront path in Tenerife at sunrise in running shoes and black leggings, framed from the knees up, no logos'),
    l2=(None, 'a pair of white running shoes on a shelf of a sports shop, no logos'),
    cats=[('Zapatillas', 'p1'), ('Running', 'p3'), ('Ropa', 'p4')],
    crops={'22c': ('22', (0.0, 0.4, 1.0, 0.95)), '02c': ('02', (0.0, 0.0, 1.0, 0.95))})

# ---------------- ópticas
S['vivavision'] = dict(
    place='Burgos', who='none', theme=dict(acc='#2C6E8F'),
    hero=('12c', 'three sunglasses in black, tortoiseshell and grey acetate on a light wooden table'),
    banner=(None, 'the inside of a bright white optician shop with long white walls of glass shelves full of eyeglasses and a white counter, no people, no logos'),
    prods=[('11c', 'teal green cat-eye acetate sunglasses, no logos', 'Gafa de sol verde'),
           ('19c', 'red rectangular acetate eyeglasses, no logos', 'Gafa roja'),
           (None, 'lime green chunky acetate sunglasses with small pearl studs on the corners, no logos', 'Gafa de sol lima'),
           (None, 'black double-bridge aviator eyeglasses in thin metal, no logos', 'Gafa doble puente'),
           (None, 'matte black wraparound sport sunglasses with prescription lenses, no logos', 'Gafa deportiva graduada'),
           ('12c', 'tortoiseshell round sunglasses, no logos', 'Gafa de sol carey')],
    l1=(None, 'a smiling woman with long brown hair wearing lime green sunglasses in a bright white optician shop'),
    l2=(None, 'an optometrist in a white coat doing an eye exam for a man in a bright clinic room'),
    cats=[('Graduadas', 'p2'), ('De sol', 'p1'), ('Deportivas', 'p5')],
    crops={'12c': ('12', (0.0, 0.1, 1.0, 0.56)), '11c': ('11', (0.0, 0.35, 1.0, 0.57)), '19c': ('19', (0.0, 0.22, 1.0, 0.385))})

S['optica-santa-ana'] = dict(
    place='Torredelcampo', who='none', theme=dict(acc='#1D5D9B'),
    hero=(None, 'thin gold metal round eyeglasses and tortoiseshell acetate eyeglasses'),
    banner=(None, 'the inside of a bright optician and hearing centre with pale blue walls, white counters and walls of eyeglasses, no people, no logos'),
    prods=[('13c', 'sport wraparound sunglasses with mirrored pink, blue and red lenses on a display stand, no logos', 'Gafas deportivas'),
           (None, 'black rectangular acetate eyeglasses with a small gold detail on the temples, no logos', 'Gafa negra'),
           (None, 'tortoiseshell round acetate eyeglasses, no logos', 'Gafa redonda carey'),
           (None, 'rose-tinted cat-eye eyeglasses in transparent pink acetate, no logos', 'Gafa rosa'),
           (None, 'classic black sunglasses with polarised green lenses, no logos', 'Gafa de sol polarizada'),
           (None, 'a small modern behind-the-ear hearing aid in beige next to its charging case', 'Audífono recargable')],
    l1=(None, 'a smiling woman with curly hair wearing red eyeglasses, soft light, bright optician shop'),
    l2=(None, 'an audiologist fitting a small hearing aid behind the ear of a smiling senior man, bright clinic'),
    cats=[('Graduadas', 'p2'), ('Deportivas', 'p1'), ('Audición', 'p6')],
    crops={'13c': ('13', (0.0, 0.08, 0.72, 0.86))})

S['optica-romany'] = dict(
    place='Dénia', who='none', theme=dict(acc='#C0392B'),
    hero=(None, 'gold metal aviator eyeglasses and black acetate sunglasses'),
    banner=(None, 'the inside of a warm optician shop with lit beige wall niches full of eyeglasses and a light wooden floor, no people, no logos'),
    prods=[('21c', 'a black sport shield sunglass with a single dark mirrored lens, no logos', 'Gafa deportiva de pádel'),
           (None, 'gold metal double-bridge aviator eyeglasses, no logos', 'Gafa aviador dorada'),
           (None, 'black round acetate eyeglasses with clear lenses, no logos', 'Gafa redonda negra'),
           (None, 'red heart-shaped acetate sunglasses, no logos', 'Gafa de sol corazón'),
           (None, 'orange-tinted black acetate eyeglasses for screens, no logos', 'Gafa filtro naranja'),
           (None, 'dark green round acetate sunglasses, no logos', 'Gafa de sol verde')],
    l1=(None, 'a smiling man with dark hair wearing gold aviator eyeglasses in a bright optician shop'),
    l2=(None, 'a padel player wearing sport sunglasses on a blue padel court, sunny'),
    cats=[('Graduadas', 'p2'), ('De sol', 'p6'), ('Deporte', 'p1')],
    crops={'21c': ('21', (0.03, 0.4, 0.97, 0.72))})

S['optika-la-garriga'] = dict(
    place='La Garriga', who='none', theme=dict(acc='#7A4E2D'),
    hero=('26c', 'burgundy oval acetate sunglasses on a glasses case'),
    banner=(None, 'the inside of an elegant optician and hearing centre with dark wooden shelves of eyeglasses, warm light and a cream counter, no people, no logos'),
    prods=[('26c', 'burgundy oval acetate sunglasses, no logos', 'Gafa de sol burdeos'),
           ('20c', 'black square acetate sunglasses with rose lenses, no logos', 'Gafa de sol rosa'),
           ('12c', 'a dusty pink velvet glasses case, no logos', 'Funda de terciopelo'),
           (None, 'thin gold oval sunglasses with brown lenses, no logos', 'Gafa de sol dorada'),
           (None, 'black rectangular acetate eyeglasses, no logos', 'Gafa graduada negra'),
           (None, 'a small modern behind-the-ear hearing aid in champagne next to its charging case', 'Audífono')],
    l1=(None, 'a blonde woman wearing small gold oval sunglasses, close up, sunny'),
    l2=(None, 'an optometrist examining a woman with a slit lamp in a modern clinic room'),
    cats=[('De sol', 'p1'), ('Graduadas', 'p5'), ('Audición', 'p6')],
    crops={'26c': ('26', (0.0, 0.15, 1.0, 0.7)), '20c': ('20', (0.15, 0.18, 0.85, 0.82)), '12c': ('12', (0.0, 0.25, 1.0, 0.85))})

S['valdevision'] = dict(
    place='La Almunia de Doña Godina', who='none', theme=dict(acc='#1F3C88'),
    hero=('19c', 'tortoiseshell round acetate eyeglasses on a white stone plinth'),
    banner=('29', 'the shop window of an optician with framed photos and eyeglasses on white shelves, no people, no logos'),
    prods=[('19c', 'tortoiseshell round acetate eyeglasses, no logos', 'Gafa redonda carey'),
           ('18c', 'transparent crystal acetate eyeglasses, no logos', 'Gafa transparente'),
           ('20c', 'brown and pink marbled acetate eyeglasses, no logos', 'Gafa jaspeada'),
           (None, 'white round acetate sunglasses with dark lenses, no logos', 'Gafa de sol blanca'),
           (None, 'black oval sunglasses, no logos', 'Gafa de sol negra'),
           (None, 'a small modern behind-the-ear hearing aid in grey next to its charging case', 'Audífono')],
    l1=(None, 'a woman with long brown hair wearing white round sunglasses in front of a brick church tower in a sunny Aragonese town square'),
    l2=(None, 'an optometrist in a white coat doing a vision therapy exercise with an adult woman, bright clinic room'),
    cats=[('Graduadas', 'p1'), ('De sol', 'p4'), ('Audición', 'p6')],
    crops={'19c': ('19', (0.1, 0.08, 0.95, 0.31)), '18c': ('18', (0.1, 0.04, 1.0, 0.31)), '20c': ('20', (0.0, 0.18, 1.0, 0.62))})

S['optica-color'] = dict(
    place='Mula', who='none', theme=dict(acc='#3E6B48'),
    hero=('15c', 'olive green oval acetate sunglasses with green lenses on a grey box'),
    banner=(None, 'the inside of a bright optician shop with a light wooden wall, white lit panels full of sunglasses and a white counter, no people, no logos'),
    prods=[('15c', 'dark green oval acetate sunglasses with green lenses, no logos', 'Gafa de sol ovalada'),
           ('07c', 'brown double-bridge pilot sunglasses with amber lenses, no logos', 'Gafa de sol piloto'),
           ('09c', 'tortoiseshell oval sunglasses with brown lenses, no logos', 'Gafa de sol carey'),
           ('16c', 'black aviator sunglasses with a thick top bar and dark lenses, no logos', 'Gafa de sol aviador'),
           ('08c', 'black and gold oval metal sunglasses, no logos', 'Gafa de sol negra y oro'),
           (None, 'dark green marbled square acetate eyeglasses, no logos', 'Gafa graduada verde')],
    l1=(None, 'a young woman with long dark hair and a sage green top wearing oversized tortoiseshell sunglasses, soft light'),
    l2=(None, 'a young woman in a white shirt trying on sunglasses in front of a white wall of sunglasses in an optician shop'),
    cats=[('De sol', 'p1'), ('Graduadas', 'p6'), ('Novedades', 'p2')],
    crops={'15c': ('15', (0.1, 0.1, 1.0, 0.62)), '07c': ('07', (0.15, 0.15, 1.0, 0.6)), '09c': ('09', (0.0, 0.08, 1.0, 0.72)),
           '16c': ('16', (0.0, 0.1, 1.0, 0.58)), '08c': ('08', (0.15, 0.15, 1.0, 0.6))})

S['crealens'] = dict(
    place='Sevilla', who='none', theme=dict(acc='#C9A227'),
    hero=('07', 'tortoiseshell round acetate eyeglasses and honey sunglasses on black and white bird-pattern wallpaper'),
    banner=(None, 'the inside of a modern optician shop with mustard yellow wooden slat walls, black and white bird-pattern wallpaper and glass shelves of eyeglasses, no people, no logos'),
    prods=[('07', 'honey tortoiseshell round acetate eyeglasses, no logos', 'Gafa redonda miel'),
           (None, 'red and burgundy cat-eye acetate eyeglasses, no logos', 'Gafa ojo de gato roja'),
           (None, 'purple oval acetate eyeglasses, no logos', 'Gafa morada'),
           (None, 'turquoise square acetate eyeglasses, no logos', 'Gafa turquesa'),
           (None, 'classic brown sunglasses with brown gradient lenses, no logos', 'Gafa de sol marrón'),
           (None, 'thin black round metal eyeglasses, no logos', 'Gafa metálica negra')],
    l1=(None, 'a smiling woman with long wavy hair wearing turquoise eyeglasses in front of black and white bird-pattern wallpaper'),
    l2=(None, 'an optometrist in a cream blouse doing a vision therapy exercise with an adult in a bright room with yellow walls'),
    cats=[('Graduadas', 'p1'), ('De sol', 'p5'), ('Terapia visual', 'l2')])

S['optica-tenerife'] = dict(
    place='Candelaria', who='none', theme=dict(acc='#1E88C8'),
    hero=('04c', 'black cat-eye eyeglasses with a matching magnetic sun clip-on'),
    banner=(None, 'the inside of a bright optician shop with white walls, long white shelves of eyeglasses and sunglasses and a light floor, no people, no logos'),
    prods=[('04c', 'black cat-eye acetate eyeglasses with a magnetic sun clip-on, no logos', 'Gafa con clip solar negra'),
           ('05c', 'dark green cat-eye acetate eyeglasses with a magnetic sun clip-on, no logos', 'Gafa con clip solar verde'),
           ('06c', 'transparent pink cat-eye eyeglasses with a magnetic sun clip-on, no logos', 'Gafa con clip solar rosa'),
           ('20c', 'beige cat-eye sunglasses with a clip-on, no logos', 'Gafa de sol beige'),
           (None, 'black polarised square sunglasses, no logos', 'Gafa de sol polarizada'),
           (None, 'red cat-eye sunglasses, no logos', 'Gafa de sol roja')],
    l1=(None, 'a smiling woman with red hair wearing black sunglasses on a sunny terrace by the sea in Tenerife'),
    l2=(None, 'an optometrist doing an eye exam for an adult woman with a phoropter in a bright clinic room'),
    cats=[('Clip solar', 'p1'), ('De sol', 'p5'), ('Revisión visual', 'l2')],
    crops={'04c': ('04', (0.0, 0.57, 0.92, 0.98)), '05c': ('05', (0.0, 0.57, 0.92, 0.98)), '06c': ('06', (0.0, 0.57, 0.92, 0.98)),
           '20c': ('20', (0.0, 0.1, 1.0, 0.75))})

S['optica-lupitas'] = dict(
    place='Don Benito', who='none', theme=dict(acc='#E2A400'),
    hero=('05', 'tortoiseshell oversized sunglasses resting on fresh lemons on a wooden table'),
    banner=('30c', 'the inside of a modern optician shop with a rustic wooden wall display of sunglasses, white walls and warm light, no people, no logos'),
    prods=[('05', 'tortoiseshell oversized sunglasses, no logos', 'Gafa de sol carey'),
           ('08c', 'colourful acetate eyeglasses in red, blue and tortoiseshell on top of their cases, no logos', 'Gafas graduadas'),
           ('30c', 'sunglasses in white, pink and black on a rustic wooden wall display, no logos', 'Gafas de sol'),
           (None, 'black square thick acetate eyeglasses, no logos', 'Gafa negra'),
           (None, 'red and pink round acetate eyeglasses, no logos', 'Gafa roja'),
           (None, 'a pack of monthly contact lenses next to a bottle of contact lens solution, no logos', 'Lentillas')],
    l1=(None, 'a smiling woman with short hair wearing red round eyeglasses, sunny street'),
    l2=(None, 'an optometrist doing an eye exam for an adult man with a slit lamp in a bright clinic'),
    cats=[('De sol', 'p1'), ('Graduadas', 'p2'), ('Lentillas', 'p6')],
    crops={'30c': ('30', (0.05, 0.05, 0.95, 0.78)), '08c': ('08', (0.0, 0.0, 1.0, 0.48))})

S['centro-optico-don-benito'] = dict(
    place='Don Benito', who='none', theme=dict(acc='#D0312D'),
    hero=('05', 'many sunglasses lined up in orange display trays'),
    banner=('12', 'the inside of a modern optician shop with grey and red accents, tall columns of eyeglasses, a bench and a light floor, no people, no logos'),
    prods=[('05', 'black sport sunglasses with blue mirrored lenses, no logos', 'Gafa de sol deportiva'),
           ('32c', 'thin gold metal oval sunglasses with dark lenses, no logos', 'Gafa de sol metálica'),
           ('15', "colourful flexible children's eyeglasses in blue, pink and red, no logos, no people", 'Gafas infantiles'),
           (None, 'black rectangular acetate eyeglasses with progressive lenses, no logos', 'Gafa progresiva'),
           (None, 'tortoiseshell square sunglasses, no logos', 'Gafa de sol carey'),
           (None, 'thin silver metal round eyeglasses, no logos', 'Gafa graduada metálica')],
    l1=(None, 'a smiling woman with her hair up wearing thin eyeglasses, sunny street in a Spanish town'),
    l2=('19', 'rows of eyeglasses on tall white display columns in a modern optician shop, no people, no logos'),
    cats=[('De sol', 'p1'), ('Graduadas', 'p4'), ('Infantil', 'p3')],
    crops={'32c': ('32', (0.0, 0.25, 1.0, 0.75))})
