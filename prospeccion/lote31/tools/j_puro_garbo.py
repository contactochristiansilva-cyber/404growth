from jobs_lib import job, studio_moda
S = 'puro-garbo'; BG = 'warm ivory (#EEE7DE)'
J = [
    job(S, 'hero', [1], '16:9',
        "Wide luxury fashion campaign photo in Seville: a model wearing the rust-red satin long tunic coat with mandarin collar "
        "and the matching wide palazzo trousers from the reference, plus a wide-brimmed dark straw hat, standing on the marble "
        "steps of a sunlit Sevillian palace courtyard with white arches, terracotta pots and bougainvillea, golden late-afternoon "
        "light. The model stands in the right third of the frame, full body; the left 45% of the image is calm, softly blurred "
        "courtyard wall for a headline. Editorial, cinematic, warm Andalusian colour.", 'moda'),
    studio_moda(S, 'p2', 6, 'the purple asymmetric satin dress with the diagonal ruffle', BG),
    studio_moda(S, 'p3', 10, 'the beige and black botanical print midi dress with the high bow neck and the wide black belt', BG),
    studio_moda(S, 'p4', 23, 'the petrol-teal draped top and long skirt set (without the necklace if it hides the neckline)', BG),
    studio_moda(S, 'p5', 20, 'the raspberry long-sleeve draped jersey dress', BG),
    job(S, 'x1', [1], '3:4',
        f"E-commerce detail view: the rust-red satin tunic coat and palazzo trousers from the reference worn by a model seen in "
        f"three-quarter back view, face not visible, showing the side slits, the fall of the satin and the trousers, on a seamless "
        f"{BG} studio background, soft daylight. Leave calm empty background on the left and right edges.", 'moda'),
    job(S, 'x2', [1], '4:5',
        "Lifestyle photo: a woman wearing the rust-red satin tunic coat and palazzo trousers from the reference as a wedding "
        "guest, walking through an orange-tree patio of a Sevillian hacienda with whitewashed walls, holding a small clutch, "
        "soft golden light, full outfit visible.", 'moda'),
    job(S, 'x3', [1], '4:5',
        "Macro detail photo of the rust-red satin from the reference: the mandarin collar and the row of small fabric-covered "
        "buttons, the satin sheen catching soft side light, very shallow depth of field, rich colour, studio.", 'moda'),
    job(S, 'look', [7], '4:5',
        "Shop-the-look editorial: a model wearing the mustard-yellow oversized satin top and matching skirt from the reference, "
        "a wide-brimmed straw hat and a green beaded necklace, posing next to a classic white marble column in a Seville garden "
        "with clipped hedges, full body, soft daylight.", 'moda'),
    job(S, 'l1', [17], '4:5',
        "Editorial category photo 'Invitada': a model wearing the fuchsia-raspberry short-sleeve dress with the asymmetric "
        "draped hem from the reference and a wide-brimmed hat, standing in a green Andalusian garden path, full body, soft light.", 'moda'),
    job(S, 'l2', [22], '4:5',
        "Editorial category photo 'Madrina': a model wearing the long navy satin wrap coat-dress with tie belt from the reference, "
        "standing beside a stone balustrade of a Sevillian palace terrace at golden hour, full body, elegant.", 'moda'),
    job(S, 'l3', [15], '4:5',
        "Editorial category photo 'Pantalón': a model wearing the navy wide trousers with side slits and the blouse with the large "
        "olive bow from the reference, standing against a whitewashed Seville wall with pink bougainvillea, full body.", 'moda'),
    job(S, 'l4', [13], '4:5',
        "Editorial category photo: a model wearing the navy jacquard blouson top and long skirt set from the reference with a "
        "wide-brimmed hat and an amber necklace, standing against a white wall with soft shadows, full body, minimal.", 'moda'),
    job(S, 'l5', [11, 9], '16:9',
        "Wide interior photo of an elegant small fashion boutique in central Seville like the references: white walls with black "
        "bird decorations, open rails with beige, black and orange garments, a full-length mirror, hats and necklaces on a shelf, "
        "warm boutique lighting, inviting, no people. Keep the real look of this boutique, just beautifully photographed.", 'moda'),
]
