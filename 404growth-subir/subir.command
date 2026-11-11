#!/bin/bash
# 404 Growth · sube a Cloudflare con wrangler, la herramienta oficial de Cloudflare. Doble clic.
#   1) la web (la carpeta que dice wrangler.jsonc), 2) el admin y el CRM (admin/), 3) Partner 404 (partner/), 4) el contador de visitas (visitas/).
#   Los Workers que no han cambiado desde su última subida buena no se vuelven a subir (archivo .subido de cada carpeta).
# La primera vez instala Node.js en ~/.404node (solo si no lo tienes) y te pide entrar en Cloudflare en el navegador.
cd "$(dirname "$0")" || exit 1
fin() { echo; read -r -p "  Pulsa Intro para cerrar." _; exit "${1:-0}"; }
SITE=$(sed -n 's/.*"directory": *"\([^"]*\)".*/\1/p' wrangler.jsonc)
echo
echo "  404 Growth · subir"
echo "  Web: $(cd "$SITE" 2>/dev/null && pwd)"
echo
if [ ! -d "$SITE" ]; then echo "  No encuentro la carpeta $SITE. Avisa a Claude."; fin 1; fi
printf '.DS_Store\nanterior\n_to_delete\n' > "$SITE/.assetsignore"   # las copias antiguas no se publican
export PATH="$HOME/.404node/bin:$PATH"
NODE_OK=0
if command -v node >/dev/null 2>&1; then [ "$(node -p 'process.versions.node.split(".")[0]')" -ge 22 ] && NODE_OK=1; fi
if [ $NODE_OK = 0 ]; then
  echo "  Instalando Node.js (solo la primera vez, en ~/.404node)…"
  ARCH=$(uname -m); [ "$ARCH" = "x86_64" ] && ARCH=x64
  BASE=https://nodejs.org/dist/latest-v22.x
  LINE=$(curl -fsSL "$BASE/SHASUMS256.txt" | grep " node-v[0-9.]*-darwin-$ARCH.tar.gz$")
  SUM=${LINE%% *}; FILE=${LINE##* }
  if [ -z "$FILE" ]; then echo "  No pude descargar Node.js. ¿Hay internet?"; fin 1; fi
  curl -fL --progress-bar "$BASE/$FILE" -o /tmp/404node.tgz || fin 1
  echo "$SUM  /tmp/404node.tgz" | shasum -a 256 -c - >/dev/null || { echo "  La descarga de Node.js no cuadra. No sigo."; fin 1; }
  mkdir -p "$HOME/.404node" && tar -xzf /tmp/404node.tgz -C "$HOME/.404node" --strip-components 1 && rm -f /tmp/404node.tgz
fi
W="npx --yes wrangler@4"
# entrar: la página de Cloudflare se abre en Chrome (donde ya tienes la sesión), no en el navegador por defecto
login_chrome() {
  LOG=$(mktemp -t 404login); $W login --browser=false >"$LOG" 2>&1 & PID=$!
  URL=""
  for i in $(seq 1 90); do
    URL=$(grep -o 'https://dash\.cloudflare\.com/oauth2/auth[^[:space:]]*' "$LOG" | head -1)
    [ -n "$URL" ] && break; kill -0 $PID 2>/dev/null || break; sleep 1
  done
  if [ -n "$URL" ]; then
    if [ -d "/Applications/Google Chrome.app" ]; then open -a "Google Chrome" "$URL"; else open "$URL"; fi
  fi
  wait $PID; R=$?; rm -f "$LOG"; return $R
}
if $W whoami 2>&1 | grep -qi "not authenticated"; then
  echo
  echo "  Ahora se abre Cloudflare en Chrome. Baja hasta el final de la página y pulsa el botón azul «Allow»."
  echo "  Tienes 2 minutos. Cuando salga «Authorization granted», vuelve a esta ventana."
  echo
  if ! login_chrome; then
    echo
    echo "  No llegó la autorización. Probamos de otra forma: abre el enlace que sale abajo y escribe el código que te da."
    echo
    $W login --device || { echo "  No se pudo entrar. Haz una captura de esta ventana para Claude."; fin 1; }
  fi
fi
export WRANGLER_LOG_PATH="$PWD/.logs"; mkdir -p "$WRANGLER_LOG_PATH"   # los registros de wrangler se quedan aquí, para que Claude los lea sin pedirte capturas
huella() { cat "$@" 2>/dev/null | shasum -a 256 | cut -c1-16; }
# paso <nombre> <wrangler.jsonc> [archivos del Worker]: si esos archivos no han cambiado desde la última subida buena (.subido), no se vuelve a subir.
# Así un fallo de Cloudflare en un Worker que no ha cambiado (el contador de visitas, 11/11/2026: «binding DB of type d1 failed to generate») no molesta.
paso() {
  local nom="$1" cfg="$2"; shift 2
  local marca="" h="" n
  if [ $# -gt 0 ]; then
    marca="$(dirname "$cfg")/.subido"; h=$(huella "$cfg" "$@")
    if [ -f "$marca" ] && [ "$(cat "$marca")" = "$h" ]; then echo; echo "  = $nom: igual que lo que ya está en Cloudflare, no hace falta subirlo."; return 0; fi
  fi
  echo
  echo "  ── Subiendo $nom… (si pregunta si quieres continuar, escribe y y pulsa Intro)"
  echo
  for n in 1 2 3 4 5 6; do
    if $W deploy -c "$cfg"; then echo; echo "  ✓ Subido: $nom"; [ -n "$marca" ] && echo "$h" > "$marca"; return 0; fi
    if [ $n -lt 6 ]; then echo; echo "  Cloudflare no ha respondido bien. Lo intento otra vez en $((n*20)) segundos ($n de 6)…"; sleep $((n*20)); fi
  done
  echo; echo "  No se pudo subir $nom. Sigo con lo demás; al final haz una captura de esta ventana para Claude."
  FALLOS="$FALLOS · $nom"; return 1
}
paso "la web" wrangler.jsonc   # primero la web, para que se publique aunque falle lo demás
[ -f admin/wrangler.jsonc ] && paso "el admin y el CRM" admin/wrangler.jsonc admin/worker.js
if [ -f partner/wrangler.jsonc ]; then
  paso "Partner 404 (app.404growth.com)" partner/wrangler.jsonc partner/worker.js
  # la clave que cifra las claves de Stripe, Anthropic y Meta: se crea una sola vez y se queda en Cloudflare
  # solo si Cloudflare contesta bien y la lista no la trae: si «secret list» falla (como el 11/11/2026), nunca se crea otra clave
  # (una clave nueva dejaría ilegibles las claves de Stripe, Anthropic y Meta guardadas)
  if SL=$($W secret list -c partner/wrangler.jsonc 2>/dev/null) && printf '%s' "$SL" | grep -q '"name"' && ! printf '%s' "$SL" | grep -q P404_KEY; then
    echo; echo "  Creando la clave de cifrado de Partner 404 (solo la primera vez)…"
    if openssl rand -base64 32 | tr -d '\n' | $W secret put P404_KEY -c partner/wrangler.jsonc >/dev/null 2>&1; then echo "  ✓ Clave de cifrado creada"
    else echo "  No se pudo crear la clave de cifrado. Partner 404 funciona igual; haz una captura para Claude."; fi
  fi
fi
[ -f visitas/wrangler.jsonc ] && paso "el contador de visitas" visitas/wrangler.jsonc visitas/worker.js   # el último: casi nunca cambia
if [ -n "$FALLOS" ]; then echo; echo "  Faltó por subir$FALLOS. Haz una captura de esta ventana para Claude."; fin 1; fi
echo
echo "  Listo: todo subido. La web está en https://404growth.com y Partner 404 en https://app.404growth.com"
fin 0
