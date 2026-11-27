# Intenso: stock por ml (Shopify Flow)

Cada perfume (Esenciales, Nicho, Extractos) tiene 500 ml que comparten sus 4 tamaños.
El metacampo `custom.ml_stock` guarda lo que queda. Las variantes van con seguimiento de inventario,
«no vender sin stock» (DENY) y cantidad = floor(ml / tamaño).

Flujo «Stock en ml: descontar con cada pedido y avisar al 30 %» (Order created):
1. Get product data con la consulta en Liquid de `consulta_get_product_data.liquid` (máx. 100).
2. Run code: entrada `entrada_run_code.graphql`, código `run_code.js`, salida `salida_run_code.graphql`.
   Prueba local: `node test.mjs`.
3. For each `runCode.updates` → inventorySetQuantities (absoluto, `available`) + metafieldsSet,
   y si `aviso` (antes ≥ 150 y queda < 150) → Send internal email a holaintenso@gmail.com y contactochristiansilva@gmail.com.

Cuenta: tamaño normal = ml × cantidad; decant 5 ml (`Perfume: Nº X`, variante = línea) = 5 ml;
packs Dúo/Trío (`Perfume 1..3`, variante = tamaño) = tamaño por perfume. Los decants de regalo (3 ml) no cuentan.
Las cancelaciones y devoluciones no devuelven ml.
