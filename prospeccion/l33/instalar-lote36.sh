#!/bin/bash
# Lote 36 (13/11/2026): instala las 19 propuestas en web117-404growth y el admin con lpatch_20261113.
# Uso: bash ~/Downloads/instalar-lote36.sh
set -e
D="$HOME/Downloads"; T="$D/l36pkg"
rm -rf "$T"; mkdir -p "$T"; cd "$T"
cat "$D"/l36-paq.tar.part-* | tar xf -
tar xf "$D/l36-fotos-rehechas.tar" -C web
n=$(ls web | wc -l | tr -d ' ')
[ "$n" -ge 247 ] || { echo "Faltan archivos ($n de 247)"; exit 1; }
cp -f web/* "$D/web117-404growth/"
for s in burgos-zapaterias ibaimendi-kirolak calzados-hermanos-lopez vivavision optica-santa-ana optica-romany calzados-cane acouga zapateria-buades mapi-shoes optika-la-garriga valdevision optica-color crealens optica-tenerife optica-lupitas yaiza-sport calzados-guillen centro-optico-don-benito; do mkdir -p "$D/web117-404growth/p/$s"; cp -f "web/p-$s.html" "$D/web117-404growth/p/$s/index.html"; done
W="$D/404growth-subir/admin/worker.js"
h=$(shasum -a 256 "$W" | cut -c1-16)
if [ "$h" = "d9cb4d71b740cad6" ]; then
  cp "$W" "$D/404growth-subir/anterior/worker-13nov-antes-l36.js"; cp -f admin/worker.js "$W"; echo "Admin actualizado (lpatch_20261113)"
elif [ "$h" = "$(shasum -a 256 admin/worker.js | cut -c1-16)" ]; then echo "El admin ya estaba actualizado"
else echo "OJO: el admin del Mac no es el esperado ($h): no lo toco"; fi
echo "Listo: 19 propuestas en web117-404growth. Ahora: subir-web.command y subir.command"
