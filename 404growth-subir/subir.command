#!/bin/bash
# 404 Growth · sube a Cloudflare con wrangler, la herramienta oficial de Cloudflare. Doble clic.
#   1) el contador de visitas (carpeta visitas/), 2) el admin y el CRM (carpeta admin/), 3) Partner 404 (carpeta partner/), 4) la web (la carpeta que dice wrangler.jsonc).
# La primera vez instala Node.js en ~/.404node (solo si no lo tienes) y te pide entrar en Cloudflare en el navegador.
cd "$(dirname "$0")" || exit 1
fin() { echo; read -r -p "  Pulsa Intro para cerrar." _; exit "${1:-0}"; }
# 0) antes de subir nada, trae lo último de GitHub: así siempre sube la última versión (las imágenes que solo están en el Mac no se tocan)
REPO_URL="https://github.com/contactochristiansilva-cyber/404growth.git"
ROOT="$(cd .. && pwd)"
if [ "$1" != "--ya" ]; then
  echo
  if ! xcode-select -p >/dev/null 2>&1; then
    echo "  Para que esto se actualice solo, el Mac necesita las herramientas de desarrollo de Apple."
    echo "  Abre Terminal, escribe:  xcode-select --install  y acepta. Mientras, subo lo que hay en esta carpeta."
  else
    echo "  Trayendo lo último de GitHub…"
    ANTES=$(shasum "$0" 2>/dev/null)
    export GIT_TERMINAL_PROMPT=0
    if [ ! -d "$ROOT/.git" ]; then ( cd "$ROOT" && git init -q && git remote add origin "$REPO_URL" ) >/dev/null 2>&1; fi
    ( cd "$ROOT" && git config credential.helper osxkeychain ) >/dev/null 2>&1   # el acceso a GitHub se guarda en el llavero del Mac
    OKF=0; ( cd "$ROOT" && git fetch -q origin main ) 2>/dev/null && OKF=1
    if [ $OKF = 0 ]; then
      echo
      echo "  GitHub necesita saber que eres tú (solo esta vez; luego se guarda en el llavero del Mac)."
      echo "  1) Se abre GitHub en el navegador. Pon de nombre «subir 404», en «Repository access» elige «Only select repositories» → 404growth,"
      echo "     en «Permissions» → «Contents» elige «Read-only», y pulsa «Generate token». Copia el código que sale (empieza por github_pat_)."
      echo "  2) Vuelve aquí. En «Username» escribe:  contactochristiansilva-cyber   y en «Password» pega el código (al pegar no se ve nada: es normal) y pulsa Intro."
      echo
      open "https://github.com/settings/personal-access-tokens/new" 2>/dev/null
      ( cd "$ROOT" && GIT_TERMINAL_PROMPT=1 git fetch -q origin main ) && OKF=1
    fi
    if [ $OKF = 1 ]; then
      if ( cd "$ROOT" && git rev-parse -q --verify HEAD >/dev/null 2>&1 ); then
        if ( cd "$ROOT" && git merge -q --ff-only origin/main ) >/dev/null 2>&1; then echo "  ✓ Carpeta al día con GitHub"
        else
          # hay cambios hechos en este Mac: se guardan aparte (git stash) y se pone la versión de GitHub
          ( cd "$ROOT" && git stash push -q -u -m "subir.command $(date '+%Y-%m-%d %H:%M')" -- . ':(exclude)*.jpg' ':(exclude)*.jpeg' ':(exclude)*.png' ':(exclude)*.webp' ':(exclude)*.mp4' ) >/dev/null 2>&1
          if ( cd "$ROOT" && git merge -q --ff-only origin/main ) >/dev/null 2>&1 || ( cd "$ROOT" && git reset -q --keep origin/main ) >/dev/null 2>&1; then echo "  ✓ Carpeta al día con GitHub (tus cambios locales quedan guardados en git stash)"
          else echo "  ! No pude ponerla al día sola. Avisa a Claude. Subo lo que hay en esta carpeta."; fi
        fi
      else
        # primera vez: la carpeta no estaba conectada a GitHub
        if ( cd "$ROOT" && git checkout -q -f -B main origin/main && git branch -q --set-upstream-to=origin/main main ) >/dev/null 2>&1; then echo "  ✓ Carpeta conectada a GitHub y al día"
        else echo "  ! No pude conectarla a GitHub. Avisa a Claude. Subo lo que hay en esta carpeta."; fi
      fi
      # si este mismo archivo ha cambiado, se vuelve a abrir con la versión nueva
      if [ "$(shasum "$0" 2>/dev/null)" != "$ANTES" ]; then exec /bin/bash "$0" --ya; fi
    else
      echo "  ! No pude leer GitHub (¿sin internet o sin permiso?). Subo lo que hay en esta carpeta."
    fi
  fi
fi
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
paso() {
  echo
  echo "  ── Subiendo $1… (si pregunta si quieres continuar, escribe y y pulsa Intro)"
  echo
  if $W deploy -c "$2"; then echo; echo "  ✓ Subido: $1"
  else echo; echo "  No se pudo subir $1. Haz una captura de esta ventana y mándasela a Claude."; fin 1; fi
}
[ -f visitas/wrangler.jsonc ] && paso "el contador de visitas" visitas/wrangler.jsonc
[ -f admin/wrangler.jsonc ] && paso "el admin y el CRM" admin/wrangler.jsonc
if [ -f partner/wrangler.jsonc ]; then
  paso "Partner 404 (app.404growth.com)" partner/wrangler.jsonc
  # la clave que cifra las claves de Stripe, Anthropic y Meta: se crea una sola vez y se queda en Cloudflare
  if ! $W secret list -c partner/wrangler.jsonc 2>/dev/null | grep -q P404_KEY; then
    echo; echo "  Creando la clave de cifrado de Partner 404 (solo la primera vez)…"
    if openssl rand -base64 32 | tr -d '\n' | $W secret put P404_KEY -c partner/wrangler.jsonc >/dev/null 2>&1; then echo "  ✓ Clave de cifrado creada"
    else echo "  No se pudo crear la clave de cifrado. Partner 404 funciona igual; haz una captura para Claude."; fi
  fi
fi
paso "la web" wrangler.jsonc
echo
echo "  Listo: todo subido. La web está en https://404growth.com y Partner 404 en https://app.404growth.com"
fin 0
