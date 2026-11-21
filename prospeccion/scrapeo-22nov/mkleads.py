# 22/11/2026: el lote del lunes 23/11 rehecho con lo que decidió Chris el 21/11:
#   - nichos: moda (mujer, hombre, flamenca, ceremonia…), perfumería y cosmética, joyería, suplementos. Nada de mercerías,
#     artesanía ni muebles;
#   - conciencia: anuncios en Meta (nivel A) o web que no vende (B); de relleno (C), las que ya venden a distancia con buena
#     interacción o con dos tiendas;
#   - un móvil o WhatsApp publicado por el negocio.
# Del lote del 21/11 (scrapeo-21nov) se quedan las 19 de nivel A y B que no son mercerías (fuera Calzados Isacio: solo fijo).
# Se añaden 17 nuevas del scrapeo del 21-22/11 (Instagram + Biblioteca de anuncios + comprobación de webs).
# uso: python3 mkleads.py leads.json
import json, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
MON, TUE, WED = '2026-11-23', '2026-11-24', '2026-11-25'
OLD = json.load(open(os.path.join(HERE, '..', 'scrapeo-21nov', 'leads.json'), encoding='utf-8'))
keep = [x for x in OLD if x['niche'] != 'merceria' and x['tier'] in 'AB' and x['ig'] != 'calzadosisaciolinares']
assert len(keep) == 19, len(keep)

R = [
 # --- A: anuncian en Meta y no tienen tienda online de verdad
 ('cambiat_personalshopper', 'Cambia-T Personal Shopper', 'moda', 2686, 48, 1.79, 8, 10, '608698491', '663858189', True, 'Benidorm', 'Alicante', 'Av. Beniardá, 2', 'A',
  'anuncios de «Cambia-T Personal Shopper» (3-30/12/2025)', 'no tiene', 'bio: «Pedidos WhatsApp», «Envíos en 24/48h»',
  'Moda y complementos de mujer, con otra cuenta de flamenca (@cambiat_flamencas_benidorm)', ['La dirección sale de sus publicaciones (la de Cambia-T Flamencas)']),
 ('joyeriamolinacuevas', 'Joyería Molina Cuevas', 'joya', 23007, 368, 1.6, 4, 0, '699577454', '913658728', True, 'Madrid', 'Madrid', 'Calle Hermosilla, 20', 'A',
  'anuncios de «JOYERIA MOLINA CUEVAS» (el último del 30/05 al 2/06/2026)', 'no tiene',
  'publicaciones: «Realizamos envíos gratuitos y asegurados a cualquier destino»; WhatsApp en la bio',
  'Joyería de compra, venta y restauración de joyas antiguas (art déco, platino y diamantes) en el barrio de Salamanca', []),
 ('oopscomplementos', 'Oops Complementos', 'moda', 9536, 41, 0.43, 11, 0, '604063916', '', True, 'Vigo', 'Pontevedra', 'Calle Urzáiz, 89', 'A',
  'anuncios de «OOPS Complementos» (16/03 al 1/06/2026)', 'no tiene', 'bio: «Envío 24/48 horas», WhatsApp y club de clientas',
  'Tienda de ropa, calzado y complementos de mujer en Vigo', []),
 ('_ilovecomplementos', 'I Love Complementos', 'moda', 1631, 15, 0.92, 12, 0, '636034034', '', True, 'Vigo', 'Pontevedra', 'Avda. Alcalde Gregorio Espino, 10', 'A',
  'anuncios de «I Love Complementos» (2-4/12/2025)', 'no tiene', 'publicaciones: «Pedidos consultas wsp», «Envío a la península 5 €»',
  'Moda de mujer a buen precio en Vigo; publica a diario', ['Otra tienda de Vigo en el lote (Oops): va el martes 24']),
 ('amancia_shop', 'Amancia', 'moda', 2045, 3, 0.15, 8, 3, '649544501', '', True, 'Jerez de la Frontera', 'Cádiz', 'C/ Consistorio, 2 · C/ Isabelita Ruiz', 'A',
  'anuncios de «Amancia» (30/10 al 2/11/2026)', 'amancia.es: WooCommerce con solo 41 productos', 'bio: «WhatsApp pedidos», «Worldwide shipping»',
  'Dos tiendas en Jerez de ropa, complementos y alta bisutería', ['Interacción baja (0,15 %)', 'Otras dos tiendas de Jerez en el lote (Namá y Chabeli): van otro día']),
 ('riapita_modaflamenca', 'Riá Pitá Moda Flamenca', 'moda', 1865, 19, 1.02, 4, 8, '686262303', '952800199', True, 'Estepona', 'Málaga', 'Calle de los Reyes, 34', 'A',
  'anuncios de «riapita_modaflamenca» (24/09 al 3/11/2026) y de «RIA PITA Moda Flamenca» (abril de 2026)',
  'riapita.com: «Página bajo construcción» (WooCommerce con 12 productos que no se ven)', 'publicaciones: «Escríbenos por DM o WhatsApp»; envíos',
  'Moda flamenca, complementos y artículos para academias, con diseñadores andaluces', []),
 # --- B: web rota o sin tienda propia, sin anuncios encontrados
 ('joyeriaesenciamojacar', 'Joyería Esencia Mojácar', 'joya', 1684, 23, 1.37, 7, 3, '663787370', '', False, 'Mojácar', 'Almería', 'Parque Comercial de Mojácar, local 39', 'B',
  'no', 'joyeriaesencia.com no existe (el dominio no responde en dns.google)', 'bio: «Envíos 24/72h»',
  'Joyería con Pandora y Nomination en Mojácar', ['No dice que el móvil sea WhatsApp']),
 ('antollos_espaciodemoda', 'Antollos Espacio de Moda', 'moda', 2303, 13, 0.56, 12, 0, '616203762', '', False, 'Verín', 'Ourense', 'Rúa Laureano Peláez, 2', 'B',
  'no', 'antolloscomplementos.es no existe (el dominio no responde en dns.google)', 'bio: «ENVÍOS 🇪🇸»',
  'Tienda multimarca (Silbon, Pepe Jeans, Ecoalf…) en Verín', ['No dice que el móvil sea WhatsApp']),
 ('regalat_complementos', 'Regala-T Complementos & Moda', 'moda', 2180, 3, 0.14, 12, 0, '623562069', '', False, 'Palma del Río', 'Córdoba', 'Calle Ancha, 56C', 'B',
  'no (el nombre lo usan otros anunciantes)', 'regalat.es: Shopify cerrado con contraseña («Muy pronto»)', 'bio: «Pedidos 623 562 069», «Envíos 24/48h 4 €»; directos',
  'Moda, complementos, joyas de acero y hogar en Palma del Río', ['Interacción baja (0,14 %)', 'No dice que el móvil sea WhatsApp']),
 ('uniqomanvaldepenas', 'Uniqo Man', 'moda', 2974, 15, 0.5, 2, 8, '660562364', '', True, 'Valdepeñas', 'Ciudad Real', 'C/ Escuelas, 28', 'B',
  'no', 'no tiene web propia: vende en Miravia (marketplace)', 'bio: «Compra por DM o en nuestra web»; publicaciones: «Pedidos y consultas por WhatsApp»',
  'Moda de hombre en Valdepeñas', ['Publica poco (2 en 30 días)']),
 # --- C: ya venden a distancia, con buena interacción o dos tiendas, sin anuncios ni web
 ('la_casadeines', 'La Casa de Inés', 'moda', 3039, 12, 0.39, 10, 0, '646630665', '', True, 'Pozoblanco y Córdoba', 'Córdoba',
  'Calle Mayor, 75 (Pozoblanco) · Calle Concepción, 10 (Córdoba)', 'C', 'no', 'no tiene',
  'publicaciones: «pedidos por WhatsApp», «Pago por Bizum o transferencia», entrega en 24 h por 3,95 €',
  'Dos tiendas de ropa original para mujer, en Pozoblanco y Córdoba', []),
 ('sevillaflamenca.oficial', 'Sevilla Flamenca', 'moda', 13573, 193, 1.42, 12, 0, '722603507', '', False, 'Sevilla', 'Sevilla',
  'Polígono La Chaparrilla, autovía Sevilla-Málaga km 3,2', 'C', 'no (los anuncios con «Sevilla Flamenca» son de otras tiendas)', 'no tiene',
  '«Escríbenos por DM»; venta a todo el público', 'Moda y complementos de flamenca, con mucha interacción (1,4 %)',
  ['No dice en la bio que envíe', 'No dice que el móvil sea WhatsApp']),
 ('tuesencia_almansa', 'Tu Esencia', 'moda', 3740, 73, 1.95, 10, 1, '661095084', '', False, 'Almansa', 'Albacete', 'Calle Colón, 9', 'C',
  'no', 'no tiene', 'bio: «Envíos península 24/48h»; pedidos por teléfono',
  'Moda femenina hasta la 5XL en Almansa, con mucha interacción (1,95 %)', ['No dice que el móvil sea WhatsApp']),
 ('modas_cereza', 'Modas Cereza', 'moda', 3006, 45, 1.5, 10, 0, '667725116', '', False, 'Plasencia', 'Cáceres', 'Plaza Mayor, 44', 'C',
  'no', 'no tiene', 'bio: «Envíos a toda la península»; directos de novedades',
  'Tienda multimarca de señora, caballero y complementos en Plasencia', ['Otra tienda de Plasencia en el lote (Ábaco): va el martes 24', 'No dice que el móvil sea WhatsApp']),
 ('casual_sanlucar', 'Casual Sanlúcar', 'moda', 1896, 33, 1.74, 12, 1, '621406980', '646970440', True, 'Sanlúcar de Barrameda', 'Cádiz', 'Calle Barrameda, 40', 'C',
  'no', 'no tiene', 'bio: «Envíos WhatsApp 621 406 980»',
  'Moda de hombre y mujer en Sanlúcar', ['El nombre de la tienda no sale claro en Instagram (el perfil se llama «Lola»)']),
 ('lucia_vela_shop', 'Lucía Vela', 'moda', 1748, 8, 0.46, 4, 9, '674387484', '639214462', False, 'Úbeda', 'Jaén', 'Avda. Cristo Rey, 2', 'C',
  'no', 'no tiene', 'bio: «Envíos gratis a partir de 69,99 €»',
  'Moda de invitada y ceremonia en Úbeda', ['No dice que el móvil sea WhatsApp']),
 ('sabripontevedra_complemento', 'Sabrina Ortega Complementos', 'joya', 2493, 3, 0.12, 8, 1, '627113073', '674402794', True, 'Pontevedra', 'Pontevedra',
  'Rúa Conde San Román, 20', 'C', 'no', 'no tiene', 'bio: «RESERVAS / ENVÍOS X WhatsApp»',
  'Tienda de complementos y bisutería en el casco histórico de Pontevedra; la lleva Sabrina Ortega', ['Interacción baja (0,12 %)']),
]

NW = {'cosmetica': 10, 'suplementos': 10, 'sneakers': 8, 'joya': 5, 'moda': 0}
# mismo pueblo, días distintos
DAY = {'_ilovecomplementos': TUE, 'glamourmodavigo': WED, 'nama_collection_': TUE, 'chabeli_modas': WED, 'modas_cereza': TUE}
out = []
for x in keep:
    x = dict(x)
    x['day'] = DAY.get(x['ig'], MON)
    if x['ig'] in ('nama_collection_', 'chabeli_modas'):
        x['aviso'] = [a for a in x['aviso'] if 'Jerez' not in a] + ['Otras tiendas de Jerez en el lote (Amancia y ' + ('Chabeli' if x['ig'] == 'nama_collection_' else 'Namá') + '): va otro día']
    if x['ig'] == 'glamourmodavigo':
        x['aviso'] = x['aviso'] + ['Otras tiendas de Vigo en el lote (Oops e I Love Complementos): va el miércoles 25']
    out.append(x)
for r in R:
    (ig, name, ni, f, med, eng, n30, last, mob, fijo2, wa, zone, region, addr, tier, ads, shop, sig, what, aviso) = r
    score = {'A': 70, 'B': 55, 'C': 40}[tier] + NW[ni] + (5 if eng >= 1.5 else 0) + (3 if wa else 0) + (3 if f >= 10000 else 0) + (3 if last <= 4 else 0)
    x = {'day': DAY.get(ig, MON), 'niche': ni, 'name': name, 'ig': ig, 'f': f, 'med': med, 'eng': eng, 'n30': n30, 'lastDays': last,
         'mobile': mob, 'waPub': wa, 'zone': zone, 'region': region, 'address': addr,
         'tier': tier, 'score': min(score, 99), 'ads': ads, 'shop': shop, 'sig': sig, 'what': what, 'aviso': aviso,
         'priority': 90 if tier == 'A' else 80 if tier == 'B' else 70}
    if fijo2:
        x['mobile2' if fijo2.startswith(('6', '7')) else 'fijo'] = fijo2
    out.append(x)
assert len(out) == 36 and len({x['ig'] for x in out}) == 36
out.sort(key=lambda x: -x['score'])
json.dump(out, open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
from collections import Counter
print(len(out), Counter(x['tier'] for x in out), Counter(x['niche'] for x in out), Counter(x['day'] for x in out))
