"""VSL v4: escenas de monigotes (estilo de los Ads 2 y 4, en horizontal). Imagen (Nano Banana Pro) -> vídeo."""
STYLE = (" Visual style exactly like the reference images: minimalist 3D clay render, matte white featureless figurines "
         "(round smooth head with no face, simple rounded body, like small white mannequin toys), miniature architectural models "
         "in off-white plaster, shop with a dark forest green awning and a warm softly glowing shop window, glass smartphones with "
         "iridescent edges, seamless clean white studio background, soft diffuse light, soft contact shadows, neutral palette with "
         "forest green and mint accents only. Horizontal 16:9 frame, the scene centered and sitting in the upper 80% of the frame, "
         "the bottom 20% left as clean empty white floor. Absolutely no text, no letters, no numbers, no logos, no watermark.")

# id: (refs, image prompt, motion prompt)
S = {
 'c1a': (['a4_21.5', 'a2_3.2'],
   "A miniature shop model seen from the front, still being set up: the shop window is empty and unlit. On the left, a white figurine hands a large key to another white figurine in front of the door. In the middle, a white figurine on a small ladder paints the facade with a paint roller, with a bucket and wooden planks on the floor. On the right, a white figurine wearing a dark green apron stands waiting behind a small counter.",
   "The figurine on the ladder paints the wall slowly with the roller, the figurine on the left hands the key over, the figurine with the apron shifts its weight. Static camera, slow calm motion."),
 'c1b': (['a4_3.5'],
   "Isometric miniature model of a street block with five small off-white buildings; the shop in the middle has a dark green awning and a warm lit window. A translucent mint-green circle on the ground marks a small area just around that shop. Three white figurines walk on the sidewalk inside the circle. The rest of the street outside the circle is completely empty.",
   "The three figurines walk slowly along the sidewalk inside the green circle, the green circle pulses gently. Static camera."),
 'c2': (['a4_30.5', 'a2_5'],
   "Night scene on a soft dark blue-gray studio background with a small crescent moon. A miniature shop with its metal roller shutter fully closed next to a small street lamp. Floating above the shop, a large glass smartphone glowing, showing a clean online store screen with a 2x2 grid of products (a beige handbag, white sneakers, a cream sweater, a gift box) and a green button. Three small glass notification bubbles with green check marks float next to the phone.",
   "The glass smartphone floats gently up and down and glows, the notification bubbles pop up one after another, the street lamp light flickers softly. Static camera."),
 'c3': (['a4_7.5'],
   "A matte white 3D relief map of Spain (the Iberian peninsula part that is Spain, with the Balearic islands) lying on the white floor, seen from above at an angle. Six white figurines stand on different regions of the map, each one holding and looking at a smartphone. A small glowing green location pin floats above each figurine.",
   "The green pins bounce softly one after another, the figurines tap on their smartphones. Slow slight camera push in."),
 'c4': (['a4_21.5', 'a2_9.2'],
   "A scene in two halves. Left half: at a miniature shop counter, a white figurine clerk wearing a dark green apron holds up a beige handbag and explains it to a white figurine customer. Right half: a white figurine sits alone on a light gray sofa looking at a smartphone; above the phone floats a glass card showing the same beige handbag and a large glass question mark bubble.",
   "On the left the clerk figurine gestures while showing the handbag and the customer nods. On the right the figurine on the sofa scratches its head and the question mark bubble wobbles. Static camera."),
 'c5': (['a4_21.5'],
   "A white figurine shop owner stands behind a counter with both hands on its head, overwhelmed, surrounded by chaos: tall leaning stacks of cardboard parcels, loose papers and receipts flying in the air, a card payment terminal, a ringing smartphone, an open laptop, tangled cables on the floor.",
   "Loose papers flutter and fall slowly through the air, the figurine shakes its head from side to side with both hands on its head. The cardboard boxes are rigid and stay perfectly still and unchanged. Static camera, calm slow motion."),
 'c6': (['a4_3.5'],
   "A small plain light-gray shop unit with a completely blank facade (no sign, no awning), standing alone between large gray windowless industrial warehouses in a miniature industrial estate model with a wide empty road. No customers anywhere. A single white figurine shop owner stands at the open door waiting with arms crossed. A small tumbleweed on the road.",
   "The tumbleweed rolls slowly across the empty road, the figurine at the door looks left and right and waits. Static camera."),
 'c7': (['a4_21.5'],
   "A miniature shop with a dark green awning and a warm lit window full of products. A cheerful queue of seven white figurines on the sidewalk, several of them carrying dark green shopping bags. One figurine leans to another pointing at the shop. Small glass bubbles with a green heart icon, a star icon and a thumbs-up icon float above them.",
   "The queue of figurines moves forward slowly, one figurine walks out of the shop with a green bag, the glass bubbles float up gently. Static camera."),
 'c8a': (['a4_30.5', 'a2_9.2'],
   "A large glass smartphone standing upright in the center showing a clean online store with a 2x3 grid of products and a green button. Next to it a white figurine holds a bank card towards a small contactless payment terminal showing a green check mark. Another white figurine pays by holding a smartphone near a second terminal. Floating glass icons: a bank card, a contactless waves symbol and a green check.",
   "The figurine taps the card on the terminal and a green check lights up, the glass icons float gently, the phone screen scrolls slightly. Static camera."),
 'c8b': (['a4_40', 'a4_21.5'],
   "On the left a miniature shop with a dark green awning, with a white figurine at its door picking up a dark green bag. On the right a small off-white house model with a white figurine at its open door. A dotted mint-green curved line connects the shop to the house, with a small parcel box with a green ribbon travelling along it. Above the shop a glass bubble with two circular sync arrows and a green check.",
   "The parcel travels along the dotted line from the shop to the house, the figurine at the house receives it, the sync arrows in the glass bubble rotate. Static camera."),
 'c9': (['a4_30.5', 'a4_21.5'],
   "A large white megaphone model on the left pointing to the right. Coming out of it in an arc, floating glass cards showing a product ad (a beige handbag with a green button) and small white envelope icons. On the right, a group of five white figurines look at their smartphones, and two of them walk towards a big glass smartphone showing an online store in the center.",
   "The glass ad cards and the envelopes fly out of the megaphone in an arc towards the figurines, two figurines walk towards the big smartphone. Static camera."),
 'c10': (['a4_21.5'],
   "Two white figurines sit face to face at a small light wooden table. One of them, the shop owner wearing a dark green apron, shows products placed on the table: a beige handbag, a pair of white sneakers and a small bottle. The other one takes notes on a laptop. Behind them, a miniature shop with a dark green awning.",
   "The figurine with the apron lifts the handbag and gestures while explaining, the other figurine types on the laptop and nods. Static camera."),
 'c11': (['a4_30.5'],
   "A 3D bar chart made of matte blocks on the white floor: four bars growing from left to right, the first two light gray and short, the last two dark forest green and much taller. Next to the gray bars a miniature shop model with a green awning; next to the tall green bars a large glass smartphone showing an online store. A white figurine stands pointing at the tallest green bar. A mint-green arrow line rises above the bars.",
   "The green bars grow taller smoothly, the mint arrow extends upward, the figurine raises its arm pointing at the tallest bar. Static camera."),
 'c12': (['a4_21.5'],
   "A large white contract sheet standing upright with gray placeholder lines instead of text, a green wax seal and a handwritten signature scribble. In front of it two white figurines shake hands. On the left a single small stack of gold coins; on the right three tall stacks of gold coins; a mint-green arrow goes from the single stack to the three stacks.",
   "The two figurines shake hands, the three stacks of coins on the right grow coin by coin, the green seal shines softly. Static camera."),
 'c13': (['a4_7.5'],
   "A matte white 3D relief map of Western Europe (Spain, Portugal, France, Italy, Germany) seen from above at an angle. A miniature shop with a green awning stands on Spain. Dotted mint-green curved lines go from the shop to glowing green location pins in Portugal, France, Italy and Germany, with small parcel boxes travelling along the lines.",
   "The parcels travel along the dotted lines from the shop in Spain to the pins in the other countries, the pins bounce softly when a parcel arrives. Static camera."),
 'c15': (['a4_7.5', 'a4_21.5'],
   "A matte white 3D relief map of Spain seen from above at an angle. A small shop model with a green awning stands in the south of the map. White figurines stand in different cities all across the map, each carrying a dark forest green shopping bag, with a glowing green location pin above each one. Thin dotted mint-green lines connect each figurine back to the shop.",
   "The figurines lift their green shopping bags happily one after another, the dotted lines pulse from the shop outward. Slow slight camera push in."),
}
