#!/bin/bash
# 404 Growth · pasa 404 Content (404-content.com) a la cuenta de Cloudflare de Javier. 19/11/2026. Doble clic.
# Se puede volver a abrir si algo falla: lo que ya se hizo (marcas en .mover/) se salta.
#   1) clave nueva de cifrado (solo en .mover/k, nunca en pantalla)
#   2) el Worker viejo (tu cuenta), sin cron y con /__reseal, vuelve a cifrar con la clave nueva las claves y las conexiones de cada cliente
#   3) app.404growth.com pasa a ser solo un puente hacia 404-content.com (partner-puente/)
#   4) copia las tablas de 404 Content (p_*) de tu base a una base nueva en la cuenta de Javier; nada de 404 Growth sale de tu cuenta
#   5) sube 404 Content a la cuenta de Javier con 404-content.com, pone su clave y comprueba que responde
cd "$(dirname "$0")" || exit 1
fin() { echo; read -r -p "  Pulsa Intro para cerrar." _; exit "${1:-0}"; }
para() { echo; echo "  $1"; echo "  Haz una captura de esta ventana para Claude."; fin 1; }
export PATH="$HOME/.404node/bin:$PATH"
command -v node >/dev/null 2>&1 || { echo "  Falta Node.js: abre antes subir.command una vez."; fin 1; }
W="npx --yes wrangler@4"
CH=d59d5d5e6d9dba65f2a977ef91ab2840     # tu cuenta
JV=a78e09fb957fd8c5bd1a88468bdf2a10                           # la cuenta de Javier
DBN=404content
M=.mover; mkdir -p "$M" && chmod 700 "$M"
export WRANGLER_LOG_PATH="$PWD/.logs"; mkdir -p "$WRANGLER_LOG_PATH"
hecho() { [ -f "$M/$1.ok" ]; }
marca() { date > "$M/$1.ok"; }
S=mover-404content
echo
echo "  404 Content · traslado a la cuenta de Cloudflare de Javier"
echo
WHO=$($W whoami 2>&1)
if printf '%s' "$WHO" | grep -qi "not authenticated"; then para "No estás dentro de Cloudflare: abre antes subir.command (te pide entrar) y vuelve a abrir este."; fi
printf '%s' "$WHO" | grep -q "$JV" || para "Tu usuario de Cloudflare todavía no ve la cuenta de Javier. Acepta la invitación del correo de Cloudflare y vuelve a abrir este."
echo "  ✓ Tu usuario ve tu cuenta y la de Javier"

# 1) la clave nueva
if [ ! -s "$M/k" ]; then (umask 077; openssl rand -base64 32 | tr -d '\n' > "$M/k") || para "No pude crear la clave nueva."; fi
HDR=$(shasum -a 256 < "$M/k" | cut -d' ' -f1)

# 2) el Worker viejo: sin cron (para que no cambie nada mientras copiamos) y con /__reseal
if ! hecho viejo; then
  echo; echo "  ── 1 de 5 · Preparo el Worker viejo (tu cuenta). Si pregunta si quieres continuar, escribe y y pulsa Intro."
  $W deploy -c partner-viejo/wrangler.jsonc || para "No se pudo subir el Worker viejo."
  $W secret put P404_KEY_NEW -c partner-viejo/wrangler.jsonc < "$M/k" >/dev/null || para "No se pudo guardar la clave nueva en el Worker viejo."
  marca viejo
fi
if ! hecho reseal; then
  echo; echo "  ── 2 de 5 · Vuelvo a cifrar las claves y las conexiones de cada cliente con la clave nueva…"
  OK=0
  for i in $(seq 1 20); do
    curl -sS -X POST "https://app.404growth.com/__reseal" -H "x-p404-reseal: $HDR" -o "$M/reseal.json" 2>/dev/null
    if grep -q '"ok":true' "$M/reseal.json" 2>/dev/null; then OK=1; break; fi
    sleep 3
  done
  [ $OK = 1 ] || para "El Worker viejo no respondió a /__reseal."
  node "$S/sql.mjs" reseal < "$M/reseal.json"
  marca reseal
fi

# 3) app.404growth.com: solo puente (esto para el Worker viejo y su cron)
if ! hecho puente; then
  echo; echo "  ── 3 de 5 · app.404growth.com pasa a reenviar a 404-content.com. Si pregunta, escribe y y pulsa Intro."
  $W deploy -c partner-puente/wrangler.jsonc || para "No se pudo subir el puente de app.404growth.com."
  marca puente
fi

# 4) los datos: de tu base (solo las tablas p_*) a una base nueva en la cuenta de Javier
if ! hecho export; then
  echo; echo "  ── 4 de 5 · Copio los datos de 404 Content…"
  $W d1 execute 404growth-admin --remote --json -c partner-viejo/wrangler.jsonc \
    --command "SELECT name FROM sqlite_master WHERE type = 'table' AND substr(name, 1, 2) = 'p_'" > "$M/tablas.json" || para "No pude leer la lista de tablas."
  TL=$(node "$S/sql.mjs" tablas < "$M/tablas.json")
  [ -n "$TL" ] || para "No encontré las tablas de 404 Content."
  echo "  Tablas: $TL"
  ARGS=(); for t in $TL; do ARGS+=(--table "$t"); done
  $W d1 export 404growth-admin --remote -c partner-viejo/wrangler.jsonc --output "$M/p404.sql" "${ARGS[@]}" || para "No se pudo exportar la base."
  $W d1 execute 404growth-admin --remote --json -c partner-viejo/wrangler.jsonc \
    --command "SELECT id, email, salt, hash, iter FROM users WHERE role = 'admin' AND disabled = 0" > "$M/admins.json" || para "No pude leer tus usuarios de admin."
  node "$S/sql.mjs" admins < "$M/admins.json" > "$M/admins.sql" || para "No pude preparar los admins."
  echo "  ✓ Exportado ($(du -h "$M/p404.sql" | cut -f1))"
  marca export
fi
if ! hecho base; then
  DBID=$(CLOUDFLARE_ACCOUNT_ID=$JV $W d1 list --json 2>/dev/null | node "$S/sql.mjs" dbid "$DBN")
  if [ -z "$DBID" ]; then
    CLOUDFLARE_ACCOUNT_ID=$JV $W d1 create "$DBN" --location weur < /dev/null || para "No se pudo crear la base en la cuenta de Javier."
    DBID=$(CLOUDFLARE_ACCOUNT_ID=$JV $W d1 list --json 2>/dev/null | node "$S/sql.mjs" dbid "$DBN")
  fi
  [ -n "$DBID" ] || para "No encuentro la base nueva en la cuenta de Javier."
  [ -f "$M/partner-wrangler-cuenta-chris.jsonc" ] || cp partner/wrangler.jsonc "$M/partner-wrangler-cuenta-chris.jsonc"
  sed -e "s/__JAVIER__/$JV/" -e "s/__DBID__/$DBID/" "$S/wrangler.jsonc" > partner/wrangler.jsonc
  grep -v '"triggers"' partner/wrangler.jsonc > partner/wrangler-sin-cron.jsonc
  echo "  ✓ Base «$DBN» en la cuenta de Javier ($DBID)"
  marca base
fi
if ! hecho import; then
  N=$($W d1 execute "$DBN" --remote --json -c partner/wrangler-sin-cron.jsonc --command "SELECT count(*) AS n FROM sqlite_master WHERE name = 'p_tenants'" 2>/dev/null | grep -o '"n": *[0-9]*' | grep -o '[0-9]*$')
  [ "$N" = "0" ] || para "La base nueva ya tiene datos de un intento anterior a medias. No sigo para no mezclar nada."
  $W d1 execute "$DBN" --remote -c partner/wrangler-sin-cron.jsonc --file "$M/p404.sql" --yes || para "No se pudieron cargar los datos en la base nueva."
  $W d1 execute "$DBN" --remote -c partner/wrangler-sin-cron.jsonc --file "$M/admins.sql" --yes || para "No se pudieron cargar los admins."
  $W d1 execute "$DBN" --remote -c partner/wrangler-sin-cron.jsonc --file "$S/aplicar.sql" --yes || para "No se pudo aplicar la clave nueva."
  echo "  ✓ Datos cargados en la cuenta de Javier"
  marca import
fi

# 5) 404 Content en la cuenta de Javier: primero sin cron, luego la clave y después con cron
if ! hecho nuevo; then
  echo; echo "  ── 5 de 5 · Subo 404 Content a la cuenta de Javier con 404-content.com. Si pregunta, escribe y y pulsa Intro."
  $W deploy -c partner/wrangler-sin-cron.jsonc || para "No se pudo subir 404 Content a la cuenta de Javier (mira si 404-content.com aún tiene registros A en su DNS)."
  $W secret put P404_KEY -c partner/wrangler.jsonc < "$M/k" >/dev/null || para "No se pudo guardar la clave en la cuenta de Javier."
  $W deploy -c partner/wrangler.jsonc || para "No se pudo subir 404 Content con su cron."
  marca nuevo
fi
echo; echo "  Compruebo que responde (puede tardar unos minutos mientras Cloudflare hace el certificado)…"
OK=0
for i in $(seq 1 40); do
  A=$(curl -s -o /dev/null -w '%{http_code}' https://404-content.com/)
  B=$(curl -s -o /dev/null -w '%{http_code}' https://404-content.com/api/me)
  if [ "$A" = "200" ] && [ "$B" != "000" ] && [ "${B:0:1}" != "5" ]; then OK=1; break; fi
  sleep 15
done
[ $OK = 1 ] || para "404-content.com todavía no responde bien (portada $A, API $B)."
C=$(curl -s -o /dev/null -w '%{http_code}' https://app.404growth.com/api/me)
echo "  ✓ 404-content.com responde (portada $A, API $B) y app.404growth.com la reenvía (API $C)"

# limpieza: tu cuenta no se queda con nada que abra lo de Javier
if ! hecho limpio; then
  $W d1 execute 404growth-admin --remote -c partner-viejo/wrangler.jsonc --command "DROP TABLE IF EXISTS p_reseal" >/dev/null 2>&1
  echo y | $W secret delete P404_KEY_NEW -c partner-puente/wrangler.jsonc >/dev/null 2>&1
  rm -P "$M/k" 2>/dev/null || rm -f "$M/k"
  rm -f "$M/p404.sql" "$M/admins.sql" "$M/admins.json"
  marca limpio
fi
huella() { cat "$@" 2>/dev/null | shasum -a 256 | cut -c1-16; }
huella partner/wrangler.jsonc partner/worker.js > partner/.subido
echo
echo "  Listo: 404 Content está en la cuenta de Javier, en https://404-content.com"
fin 0
