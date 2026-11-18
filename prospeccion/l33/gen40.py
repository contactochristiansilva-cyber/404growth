"""Lote 40 (19/11/2026) · la propuesta nueva. Versión 2, tras la primera revisión de Chris (18/11/2026, 22:00).

Lo que pidió:
  - volver a la propuesta de antes (cristal líquido, la tienda entera en el móvil y en el ordenador, la página de producto),
    con la letra de la versión «admin» (SF Pro, títulos a 400 y segunda línea fina en verde gris) y algo de sus colores;
  - TODO centrado: textos, títulos, botones y la tienda;
  - muchísimo menos texto: que se entienda de un vistazo (la garantía y el «por qué ahora», casi sin leer);
  - pensada para el móvil (casi todas las visitas son del móvil);
  - la agenda y el «¿lo hablamos?» más arriba;
  - la tienda se ve entera dentro de la página: sin botón para abrirla fuera;
  - sin precio, con la garantía de 90 días, sin testimonios de clientes, fotos de Google Flow. Solo para las propuestas nuevas.

uso: python3 gen40.py <slug> [...]   → out/p-<slug>.html  (la tienda, out/p-<slug>--tienda.html, la hace antes gen37a.py)
Los textos de cada tienda (su cita, su usuario) están en prop40.json.

Orden: cabecera de cristal · su frase de Instagram y «X, abierta 24 horas.» · la tienda entera (móvil y ordenador) · la ficha de
producto · la agenda con respuestas rápidas por WhatsApp · 5 pasos → 3 · la garantía en un gráfico · por qué ahora (fechas que se
calculan al abrirla) · anuncios · cierre. En el móvil, una barra fija abajo con «Reservar» y WhatsApp (se esconde en la agenda)."""
import html, json, os, sys, urllib.parse

D = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(D, 'out')
sys.path.insert(0, os.path.join(D, '..', '..', 'tools', 'agenda'))
import patch as AG  # noqa: E402

E = lambda s: html.escape(str(s), quote=True)
WA = '34610594450'


def wa(text):
    return f'https://wa.me/{WA}?text=' + urllib.parse.quote(text)


def I(p, cls='i'):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'


IC = {
    'eye': '<path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12Z"/><circle cx="12" cy="12" r="3"/>',
    'chat': '<path d="M21 12a8 8 0 0 1-11.8 7L4 20l1.1-4.6A8 8 0 1 1 21 12Z"/>',
    'ask': '<path d="M21 12a8 8 0 0 1-11.8 7L4 20l1.1-4.6A8 8 0 1 1 21 12Z"/><path d="M10 9.6a2.1 2.1 0 1 1 2.9 2c-.6.2-.9.7-.9 1.3v.3M12 16h.01"/>',
    'bizum': '<rect x="6" y="2.5" width="12" height="19" rx="2.5"/><path d="M10 18.5h4M12 7v6M9.8 8.6h3.1a1.3 1.3 0 0 1 0 2.6h-1.8a1.3 1.3 0 0 0 0 2.6h3.1"/>',
    'box': '<path d="M3.5 7.5 12 3l8.5 4.5v9L12 21l-8.5-4.5Z"/><path d="m3.5 7.5 8.5 4.5 8.5-4.5M12 12v9"/>',
    'tap': '<path d="M9 11V5.5a1.5 1.5 0 0 1 3 0V10m0-.5a1.5 1.5 0 0 1 3 0V11m0-.5a1.5 1.5 0 0 1 3 0V15a6 6 0 0 1-6 6h-.8a6 6 0 0 1-4.4-1.9L4.6 16.7a1.6 1.6 0 0 1 2.3-2.2L9 16.5"/>',
    'card': '<rect x="2.5" y="5" width="19" height="14" rx="2.5"/><path d="M2.5 10h19M6.5 15h4"/>',
    'phone': '<path d="M5 3.5h3.2l1.6 4.2-2.2 1.4a11 11 0 0 0 7.3 7.3l1.4-2.2 4.2 1.6V19a1.5 1.5 0 0 1-1.6 1.5A16.5 16.5 0 0 1 3.5 5.1 1.5 1.5 0 0 1 5 3.5Z"/>',
    'cam': '<path d="M4 7.5h3l1.6-2.5h6.8L17 7.5h3a1.5 1.5 0 0 1 1.5 1.5v9a1.5 1.5 0 0 1-1.5 1.5H4A1.5 1.5 0 0 1 2.5 18V9A1.5 1.5 0 0 1 4 7.5Z"/><circle cx="12" cy="13" r="3.6"/>',
    'bag': '<path d="M5 8h14l-1.2 12.1a1.5 1.5 0 0 1-1.5 1.4H7.7a1.5 1.5 0 0 1-1.5-1.4Z"/><path d="M9 8V6.5a3 3 0 0 1 6 0V8"/>',
    'gift': '<rect x="3" y="8" width="18" height="4.5" rx="1"/><path d="M5 12.5V20a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-7.5M12 8v13M12 8S10.5 3.5 8 3.5a2.2 2.2 0 0 0 0 4.5h4Zm0 0s1.5-4.5 4-4.5a2.2 2.2 0 0 1 0 4.5h-4Z"/>',
    'check': '<path d="m5 12.5 4.5 4.5L19 7.5"/>',
    'truck': '<path d="M2.5 6.5h11v10h-11zM13.5 10h4l3 3.2v3.3h-7"/><circle cx="6.5" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/>',
    'shirt': '<path d="m8 3.5-5 3 2 4 2.5-1.2V20.5h9V9.3L19 10.5l2-4-5-3a4 4 0 0 1-8 0Z"/>',
    'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    'shield': '<path d="M12 3 4.5 6v5.5c0 4.7 3.2 8.4 7.5 9.5 4.3-1.1 7.5-4.8 7.5-9.5V6Z"/><path d="m8.8 12 2.2 2.2 4.4-4.4"/>',
    'mob': '<rect x="6.5" y="2.5" width="11" height="19" rx="2.5"/><path d="M10.5 18.5h3"/>',
    'desk': '<rect x="2.5" y="4" width="19" height="13" rx="2"/><path d="M8 21h8M12 17v4"/>',
    'arrow': '<path d="M5 12h14M13 6l6 6-6 6"/>',
}
WAI = ('<svg class="wi" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3a.5.5 0 0 0 0-.5l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 11.9 11.9 0 0 0 4.6 4c1.7.7 2.4.8 3.2.7a2.8 2.8 0 0 0 1.8-1.3 2.3 2.3 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3Z"/></svg>')
LOGO = ('<svg class="mk" viewBox="20 60 362 280" aria-hidden="true"><g transform="skewX(-12) translate(52 0)" fill="none" stroke="currentColor" stroke-width="32" '
        'stroke-linecap="round" stroke-linejoin="round"><rect x="140" y="90" width="120" height="220" rx="60"/><path d="M155.1 110.2 L40 240 L140 240"/>'
        '<path d="M244.9 110.2 L360 240 L260 240"/></g></svg>')

CSS = r"""
:root{--bg:#F6F7F3;--ink:#111311;--ink2:#3A3F3A;--mut:#6F766E;--lm:#7C8B74;--line:rgba(17,19,17,.08);
--sage:#C9DDB8;--sage2:#B3CE9C;--leaf:#5E7F4E;
--glass:linear-gradient(160deg,rgba(255,255,255,.8),rgba(255,255,255,.5));
--gsh:inset 0 1px 0 #fff,inset 0 0 0 1px rgba(255,255,255,.55),0 0 0 1px rgba(17,19,17,.05),0 30px 60px -34px rgba(30,45,25,.38);
--gsh-sm:inset 0 1px 0 #fff,0 0 0 1px rgba(17,19,17,.07),0 8px 20px -12px rgba(30,45,25,.4);
--blur:blur(22px) saturate(170%);
--f:-apple-system,BlinkMacSystemFont,"SF Pro Display","SF Pro Text","Inter Tight",Inter,"Helvetica Neue",Arial,sans-serif;--ease:cubic-bezier(.2,.7,.2,1)}
*,*:before,*:after{box-sizing:border-box}
html{background:var(--bg);-webkit-text-size-adjust:100%;scroll-behavior:smooth;scroll-padding-top:90px}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--f);font-size:16px;line-height:1.45;-webkit-font-smoothing:antialiased;overflow-x:clip;text-align:center;letter-spacing:-.01em}
body:before{content:"";position:fixed;inset:0;z-index:-2;pointer-events:none;background:radial-gradient(700px 520px at 50% -8%,rgba(201,221,184,.75),transparent 70%),radial-gradient(600px 500px at 0% 45%,rgba(201,221,184,.35),transparent 70%),radial-gradient(600px 500px at 100% 75%,rgba(179,206,156,.3),transparent 70%),var(--bg)}
a{color:inherit}img,svg{display:block;max-width:100%}h1,h2,h3,p{margin:0}h1,h2,h3{font-weight:400;text-wrap:balance}p{text-wrap:balance}
:focus-visible{outline:2px solid var(--ink);outline-offset:3px;border-radius:10px}
[hidden]{display:none!important}
.w{width:100%;max-width:1180px;margin:0 auto;padding:0 20px}
.lm{display:block;color:var(--lm);font-weight:300}
.i{width:22px;height:22px;flex:none}.wi{width:20px;height:20px;flex:none;color:#25D366}
.sec{padding:96px 0 0}
.t2{font-size:clamp(32px,4.6vw,56px);line-height:1.04;letter-spacing:-.034em;margin:0 auto 30px;max-width:760px}

/* cristal líquido */
.gl{background:var(--glass);box-shadow:var(--gsh);-webkit-backdrop-filter:var(--blur);backdrop-filter:var(--blur)}
.pill{display:inline-flex;align-items:center;gap:8px;height:38px;padding:0 15px;border-radius:99px;background:rgba(255,255,255,.66);box-shadow:var(--gsh-sm);-webkit-backdrop-filter:var(--blur);backdrop-filter:var(--blur);font-size:14px;font-weight:500;color:var(--ink2);white-space:nowrap}
.pill .i{width:17px;height:17px;color:var(--leaf)}

/* botones */
.b{display:inline-flex;align-items:center;justify-content:center;gap:9px;min-height:54px;padding:0 26px;border-radius:99px;font-weight:600;font-size:16.5px;letter-spacing:-.01em;text-decoration:none;border:0;cursor:pointer;white-space:nowrap;transition:transform .2s var(--ease),background .2s}
.b:active{transform:scale(.97)}
.b.k{background:linear-gradient(160deg,#252a22,#0E100E);color:#F3F6EF;box-shadow:inset 0 1px 0 rgba(255,255,255,.14),0 16px 32px -14px rgba(17,19,17,.6)}
.b.g{background:rgba(255,255,255,.7);color:var(--ink);box-shadow:var(--gsh-sm);-webkit-backdrop-filter:var(--blur);backdrop-filter:var(--blur)}
.acts{display:flex;flex-wrap:wrap;justify-content:center;gap:10px}

/* cabecera: píldora de cristal centrada */
.nv{position:fixed;top:12px;left:0;right:0;z-index:60;display:flex;justify-content:center;pointer-events:none;padding:0 12px}
.nv-p{pointer-events:auto;display:flex;align-items:center;gap:10px;padding:6px 6px 6px 16px;border-radius:99px;background:rgba(255,255,255,.62);box-shadow:var(--gsh-sm),0 12px 30px -14px rgba(30,45,25,.35);-webkit-backdrop-filter:blur(24px) saturate(180%);backdrop-filter:blur(24px) saturate(180%);max-width:100%}
.nv-p .mk{width:30px;height:23px;color:var(--ink);flex:none}
.nv-p span{font-size:14px;font-weight:600;letter-spacing:-.015em;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.nv-p .b{min-height:40px;padding:0 16px;font-size:14.5px}

/* inicio */
.hero{padding-top:100px}
.ig{display:inline-flex;align-items:flex-start;gap:10px;max-width:440px;margin:0 auto 22px;padding:12px 16px 12px 12px;border-radius:22px 22px 22px 8px;text-align:left}
.ig .av{width:34px;height:34px;flex:none;border-radius:50%;padding:2px;background:linear-gradient(45deg,#F58529,#DD2A7B,#8134AF)}
.ig .av b{display:grid;place-items:center;width:100%;height:100%;border-radius:50%;background:#fff;font-size:13px;font-weight:700;color:var(--ink)}
.ig small{display:block;font-size:12px;font-weight:600;color:var(--ink);margin-bottom:2px}.ig small em{font-style:normal;font-weight:400;color:var(--mut)}
.ig p{font-size:14.5px;line-height:1.38;color:var(--ink2);text-wrap:pretty}
.hero h1{font-size:clamp(44px,7vw,88px);line-height:1;letter-spacing:-.04em;margin:0 auto}
.hero .pills{display:flex;flex-wrap:wrap;justify-content:center;gap:8px;margin:24px auto 0;max-width:560px}
.hero .acts{margin-top:22px}

/* la tienda, entera */
.shop{padding-top:44px}
.sw{display:inline-flex;gap:4px;padding:5px;border-radius:99px;margin:0 auto 24px}
.sw button{display:inline-flex;align-items:center;gap:7px;height:42px;padding:0 18px;border-radius:99px;border:0;background:transparent;font:inherit;font-size:14.5px;font-weight:600;color:var(--ink2);cursor:pointer;transition:background .25s,color .25s}
.sw button .i{width:18px;height:18px}
.sw button[aria-pressed=true]{background:#111311;color:#F3F6EF;box-shadow:0 8px 18px -10px rgba(10,16,8,.7)}
.fr{position:relative;width:100%;overflow:hidden;background:#fff}
.fr iframe{position:absolute;left:0;top:0;border:0;transform-origin:0 0;pointer-events:none;background:#fff}
.ph{position:relative;margin:0 auto;padding:9px;border-radius:46px;background:linear-gradient(160deg,#2A2E28,#0C0E0C);box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.12),0 40px 80px -36px rgba(10,16,8,.7)}
.ph:before{content:"";position:absolute;z-index:2;top:20px;left:50%;width:78px;height:22px;margin-left:-39px;border-radius:99px;background:#0C0E0C}
.ph .scr{border-radius:37px;overflow:hidden;background:#fff}.ph .sb{height:44px;background:#fff}
.bw{border-radius:18px;overflow:hidden;background:#fff;box-shadow:0 0 0 1px rgba(17,19,17,.07),0 40px 80px -40px rgba(20,30,16,.55)}
.bw .top{position:relative;display:flex;align-items:center;gap:7px;height:38px;padding:0 16px;background:#F1F2EE;border-bottom:1px solid rgba(17,19,17,.06)}
.bw .top i{width:11px;height:11px;border-radius:50%;background:#DCDDD8}
.bw .top span{position:absolute;left:50%;transform:translateX(-50%);width:min(320px,52%);height:24px;border-radius:8px;background:#fff;font-size:12px;color:var(--mut);display:flex;align-items:center;justify-content:center;white-space:nowrap;overflow:hidden}
.duo{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:40px;align-items:start}
.duo .side{position:sticky;top:96px}
.duo .side .ph{width:300px}
.lab{display:inline-flex;align-items:center;gap:7px;margin-bottom:12px;font-size:13px;font-weight:600;color:var(--mut)}.lab .i{width:17px;height:17px}
.mobv{display:none}
.pin{position:sticky;top:0;height:100vh;height:100svh;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:66px 0 14px}
.ph.vp{width:clamp(220px,min(76vw,calc((100svh - 226px) * .462)),310px)}
.mobv .bw{width:100%}
.mobv .vw{position:relative;width:100%}
.pg{width:min(200px,50vw);height:4px;border-radius:4px;background:rgba(17,19,17,.08);margin:14px auto 0;overflow:hidden;flex:none}.pg i{display:block;height:100%;width:0;border-radius:4px;background:#111311}
.mobv .sw{margin:12px auto 0;flex:none}

/* ficha de producto */
.pdp .row{display:flex;justify-content:center;align-items:center;gap:36px}
.pdp .bw{flex:1;max-width:760px}
.pdp .ph{width:290px;flex:none}
.pdp .pills{display:flex;flex-wrap:wrap;justify-content:center;gap:8px;margin-top:26px}

/* agenda */
.ag{--t:#111311;--td:#000;--cream:transparent;padding:96px 0 0!important;text-align:center}
.ag .ag-w{max-width:1000px!important}
.ag h2{font-weight:400!important;letter-spacing:-.034em!important;font-size:clamp(32px,4.6vw,56px)!important;line-height:1.04!important;margin-bottom:24px!important}
.ag h2 .lm{color:var(--lm)!important;font-weight:300}
.ag-card{text-align:left;border:0!important;border-radius:30px!important;box-shadow:var(--gsh)!important}
.ag-me{background:rgba(246,247,243,.75)!important}
.qr{display:flex;flex-wrap:wrap;justify-content:center;gap:8px;margin:0 auto 28px;max-width:640px}
.qr a{display:inline-flex;align-items:center;gap:8px;height:44px;padding:0 16px;border-radius:99px;background:rgba(255,255,255,.72);box-shadow:var(--gsh-sm);-webkit-backdrop-filter:var(--blur);backdrop-filter:var(--blur);text-decoration:none;font-size:14.5px;font-weight:600}
.qr a:hover{background:#fff}

/* 5 pasos → 3 */
.st .card{display:inline-block;padding:20px 24px 18px;border-radius:30px;margin:0 auto}
.st .card+.card{margin-top:14px}
.st .card.nw{background:linear-gradient(160deg,#1A1D19,#0E100E);color:#EEF2EA;box-shadow:0 30px 60px -30px rgba(10,16,8,.7)}
.st .hd{margin-bottom:14px;font-size:12.5px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--mut)}
.st .card.nw .hd{color:#9DB58D}
.st .dots{display:flex;align-items:flex-start;justify-content:center}
.st .dt{display:flex;flex-direction:column;align-items:center;gap:7px;width:70px}
.st .dt b{display:grid;place-items:center;width:52px;height:52px;border-radius:50%;background:#fff;box-shadow:var(--gsh-sm);color:var(--ink2)}
.st .dt small{font-size:12px;font-weight:500;color:var(--mut);line-height:1.2}
.st .ln{width:12px;height:2px;margin-top:25px;background:rgba(17,19,17,.14);flex:none}
.st .card.nw .dt b{background:var(--sage);color:#1E2D1A;box-shadow:none}.st .card.nw .dt small{color:#B7C2B2}.st .card.nw .ln{background:rgba(201,221,184,.35)}

/* garantía */
.gr .box{position:relative;max-width:620px;margin:0 auto;padding:30px 24px 26px;border-radius:34px;background:linear-gradient(160deg,#1A1D19,#0E100E);color:#EEF2EA;box-shadow:inset 0 1px 0 rgba(255,255,255,.08),0 40px 80px -36px rgba(10,16,8,.75);overflow:hidden}
.gr .box:before{content:"";position:absolute;left:-20%;right:-20%;top:-40%;height:80%;background:radial-gradient(closest-side,rgba(201,221,184,.18),transparent);pointer-events:none}
.gr .seal{display:inline-flex;align-items:center;gap:8px;height:34px;padding:0 14px;border-radius:99px;background:rgba(201,221,184,.14);color:var(--sage);font-size:13px;font-weight:600;letter-spacing:.06em;text-transform:uppercase}
.gr .seal .i{width:17px;height:17px}
.gr .big{font-weight:300;font-size:clamp(80px,15vw,124px);letter-spacing:-.06em;line-height:.95;margin:12px 0 0}.gr .big small{font-size:.26em;letter-spacing:-.02em;color:#9DB58D;margin-left:6px}
.gr .ch{width:100%;max-width:520px;margin:8px auto 0;overflow:visible}
.gr .ch .inv{stroke:#EEF2EA;stroke-width:2;stroke-dasharray:6 7;opacity:.55}
.gr .ch .sal{stroke:var(--sage);stroke-width:4;fill:none;stroke-linecap:round;stroke-dasharray:620;stroke-dashoffset:620;transition:stroke-dashoffset 2.2s cubic-bezier(.3,.6,.2,1)}
.gr .ch .ar{fill:url(#gg);opacity:0;transition:opacity 1s .9s}
.gr .ch .d90{stroke:rgba(255,255,255,.22);stroke-width:1.5;stroke-dasharray:3 5}
.gr .ch text{font-family:var(--f);font-size:19px;fill:#A7B1A3;font-weight:500}.gr .ch text.k{fill:#EEF2EA;font-weight:600}.gr .ch text.s{fill:var(--sage);font-weight:600}
.gr .ch .ok{opacity:0;transform-origin:center;transform-box:fill-box;transform:scale(.4);transition:opacity .4s 1.9s,transform .5s 1.9s cubic-bezier(.3,1.6,.5,1)}
.gr.in .ch .sal{stroke-dashoffset:0}.gr.in .ch .ar{opacity:1}.gr.in .ch .ok{opacity:1;transform:none}
.gr .or{margin-top:14px;font-size:clamp(19px,2.4vw,24px);font-weight:400;letter-spacing:-.025em;color:#EEF2EA;line-height:1.2}
.gr .or span{display:block;color:#9DB58D;font-weight:300}

/* por qué ahora */
.nw .tl{position:relative;display:grid;grid-template-columns:repeat(3,1fr);align-items:start;max-width:600px;margin:0 auto}
.nw .tl:before{content:"";position:absolute;top:27px;left:16.6%;right:16.6%;height:3px;border-radius:3px;background:linear-gradient(90deg,var(--sage2) 0 50%,#111311 50% 100%)}
.nw .ev{position:relative;display:flex;flex-direction:column;align-items:center;gap:8px}
.nw .ev b{display:grid;place-items:center;width:56px;height:56px;border-radius:50%;background:#fff;box-shadow:var(--gsh-sm);color:var(--ink)}
.nw .ev.k b{background:#111311;color:var(--sage);box-shadow:0 12px 24px -12px rgba(10,16,8,.7)}
.nw .ev.g b{background:var(--sage);color:#1E2D1A}
.nw .ev strong{font-weight:300;font-size:30px;letter-spacing:-.045em;line-height:1;margin-top:4px}
.nw .ev small{font-size:12px;font-weight:600;color:var(--mut);text-transform:uppercase;letter-spacing:.07em}
.nw .steps{display:flex;justify-content:center;gap:6px;margin:32px auto 0;flex-wrap:wrap;max-width:620px}
.nw .steps span{display:inline-flex;align-items:center;gap:7px;height:38px;padding:0 14px;border-radius:99px;background:rgba(255,255,255,.7);box-shadow:var(--gsh-sm);font-size:13.5px;font-weight:500}
.nw .steps span .i{width:17px;height:17px;color:var(--leaf)}
.nw .steps span em{font-style:normal;color:var(--mut);font-weight:400}
.nw .you{display:inline-flex;align-items:center;gap:10px;margin-top:20px;padding:13px 18px;border-radius:22px;font-size:14.5px;text-align:left}
.nw .you b{font-weight:600}.nw .you .i{color:var(--leaf)}

/* anuncios */
.ads .rail{display:flex;gap:14px;overflow-x:auto;scroll-snap-type:x mandatory;padding:6px 20px 26px;scrollbar-width:none;justify-content:safe center}
.ads .rail::-webkit-scrollbar{display:none}
.ad{flex:none;width:250px;scroll-snap-align:center;border-radius:22px;overflow:hidden;background:#fff;box-shadow:var(--gsh);text-align:left}
.ad .h{display:flex;align-items:center;gap:8px;padding:10px 12px}.ad .h i{width:26px;height:26px;border-radius:50%;padding:2px;background:linear-gradient(45deg,#F58529,#DD2A7B,#8134AF)}
.ad .h i:after{content:"";display:block;width:100%;height:100%;border-radius:50%;background:#fff}
.ad .h b{font-size:12.5px;font-weight:600;display:block}.ad .h small{display:block;font-size:11px;color:var(--mut);font-weight:400}
.ad .m{position:relative;aspect-ratio:4/5;background:#ddd center/cover no-repeat}
.ad .m:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 45%,rgba(10,10,8,.62))}
.ad .m h4{position:absolute;z-index:1;left:14px;right:14px;bottom:14px;margin:0;color:#fff;font-size:22px;font-weight:500;letter-spacing:-.03em;line-height:1.05}
.ad .m.col{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:3px;background:#fff}
.ad .m.col:after{display:none}
.ad .m.col div{background:#ddd center/cover no-repeat}.ad .m.col div:first-child{grid-row:span 2}
.ad .c{display:flex;justify-content:space-between;align-items:center;padding:11px 14px;font-size:13px;font-weight:600;border-top:1px solid var(--line)}
.ad .c .i{width:16px;height:16px}

/* cierre */
.cl{padding-top:96px;padding-bottom:40px}
.cl img.me{width:76px;height:76px;border-radius:50%;object-fit:cover;margin:0 auto 18px;box-shadow:0 0 0 5px rgba(255,255,255,.8),0 20px 40px -20px rgba(30,45,25,.5)}
.cl .t2{margin-bottom:24px}
footer{padding:24px 20px 130px;font-size:12px;color:var(--mut)}

/* barra fija del móvil */
.bar{position:fixed;left:12px;right:12px;bottom:12px;z-index:70;display:none;gap:8px;padding:7px;border-radius:99px;background:rgba(255,255,255,.66);box-shadow:var(--gsh-sm),0 16px 40px -16px rgba(20,30,16,.5);-webkit-backdrop-filter:blur(24px) saturate(180%);backdrop-filter:blur(24px) saturate(180%);transform:translateY(140%);transition:transform .45s var(--ease),opacity .3s}
.bar.on{transform:none}
.bar .b{min-height:48px;font-size:15.5px;flex:1}.bar .b.g{flex:0 0 48px;padding:0}
.bar.mo-off,.bar.wa-fab.ag-off{opacity:0;pointer-events:none;transform:translateY(140%)}

.rv{opacity:0;transform:translateY(16px);transition:opacity .8s var(--ease),transform .8s var(--ease)}.rv.in{opacity:1;transform:none}

@media (max-width:899px){
 .sec{padding-top:72px}.hero{padding-top:84px}
 .nv-p{padding:8px 16px 8px 14px}.nv-p .b{display:none}.nv-p span{font-size:13.5px}
 .hero .acts{flex-wrap:nowrap}.hero .acts .b{min-height:52px;padding:0 18px;font-size:15.5px;flex:1 1 auto}
 .duo{display:none}.mobv{display:block;position:relative;height:calc(100vh + var(--dist,2600px));height:calc(100svh + var(--dist,2600px))}.shop{padding-top:12px}
 .pdp{display:none}
 .st .card{padding:18px 12px 16px}.st .dt{width:56px}.st .dt b{width:44px;height:44px}.st .dt b .i{width:20px;height:20px}.st .dt small{font-size:11px}.st .ln{width:6px;margin-top:21px}
 .nw .ev strong{font-size:24px}
 .ads .rail{justify-content:flex-start}
 .bar{display:flex}
 .ag{padding-top:72px!important}
}
@media (min-width:900px){.d-hide{display:none!important}}
@media (prefers-reduced-motion:reduce){.rv{opacity:1;transform:none;transition:none}.gr .ch .sal,.gr .ch .ar,.gr .ch .ok{transition:none}}
"""

JS = r"""<script>(function(){
var d=document,A=function(s){return [].slice.call(d.querySelectorAll(s))};
/* los marcos de la tienda: escala a su caja; los enteros toman el alto que dice la tienda (h404) */
var FR=A('.fr');
function fit(){FR.forEach(function(w){var f=w.querySelector('iframe'),W=+w.dataset.w,s=w.clientWidth/W;if(!s)return;f.style.width=W+'px';f.style.transform='scale('+s+')';
 var h=w.dataset.full?(+w.dataset.h||0):+w.dataset.hh;if(h){f.style.height=h+'px';w.style.aspectRatio='auto';w.style.height=Math.round(h*s)+'px'}})}
addEventListener('resize',fit);fit();
addEventListener('message',function(m){var x=m.data;if(!x||!x.h404)return;FR.forEach(function(w){var f=w.querySelector('iframe');if(f.contentWindow===m.source&&w.dataset.full){w.dataset.h=x.h404;fit()}})});
function L(f){if(!f.src)f.src=f.dataset.src}
var F=A('iframe[data-src]');
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting)L(x.target);try{x.target.contentWindow&&x.target.contentWindow.postMessage({t404:x.isIntersecting},'*')}catch(e){}})},{rootMargin:'600px 0px'});F.forEach(function(f){io.observe(f)})}else F.forEach(L);
/* la tienda en el móvil: el móvil se queda fijo en el centro y, al seguir bajando, la que baja es la tienda de dentro,
   de arriba abajo; al llegar al final, la página sigue. Con «Ordenador», lo mismo con la tienda de ordenador. */
var MV=d.querySelector('.mobv'),dist=0,mx=0,top0=0,raf=0;
function fv(){return d.querySelector('.mobv [data-view]:not(.off) iframe')}
function doc(f){try{return f&&f.contentDocument&&f.contentDocument.body?f.contentDocument:null}catch(e){return null}}
function measure(){var f=fv(),D=doc(f);if(!MV||!D)return;var w=f.contentWindow,fr=f.parentNode,s=fr.clientWidth/(+fr.dataset.w||1);
 mx=Math.max(0,D.documentElement.scrollHeight-w.innerHeight);dist=Math.max(900,Math.round(mx*s*.65));MV.style.setProperty('--dist',dist+'px');top0=MV.getBoundingClientRect().top+scrollY;sync()}
function prog(){return dist?Math.min(1,Math.max(0,(scrollY-top0)/dist)):0}
function sync(){raf=0;var f=fv(),D=doc(f);if(!D)return;var p=prog(),w=f.contentWindow,y=Math.round(p*mx);if(Math.abs(w.scrollY-y)>.5)w.scrollTo(0,y);var b=d.querySelector('.pg i');if(b)b.style.width=(p*100)+'%'}
function hook(f){if(!f||f.__h)return;f.__h=1;f.addEventListener('load',function(){setTimeout(measure,60)});if(doc(f)&&doc(f).readyState==='complete')measure()}
if(MV){A('.mobv iframe').forEach(hook);addEventListener('scroll',function(){if(!raf)raf=requestAnimationFrame(sync)},{passive:true});addEventListener('resize',function(){fit();measure()});
 addEventListener('message',function(m){var f=fv();if(m.data&&m.data.h404&&f&&f.contentWindow===m.source)measure()});
 A('.sw button').forEach(function(b){b.addEventListener('click',function(){var v=b.dataset.v,p=prog();A('.sw button').forEach(function(x){x.setAttribute('aria-pressed',x===b)});
  A('.mobv [data-view]').forEach(function(e){e.classList.toggle('off',e.dataset.view!==v)});fit();var f=fv();if(f){L(f);hook(f)}measure();
  if(scrollY>top0)scrollTo({top:top0+p*dist,behavior:'instant'})})})}
/* aparición y gráfico de la garantía */
var R=A('.rv,.gr');
if('IntersectionObserver' in window){var io2=new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');io2.unobserve(x.target)}})},{rootMargin:'0px 0px -12% 0px'});R.forEach(function(e){io2.observe(e)})}else R.forEach(function(e){e.classList.add('in')});
/* por qué ahora: el lunes que viene, 15 días después y la siguiente fecha fuerte */
try{var now=new Date(),t0=new Date(now.getFullYear(),now.getMonth(),now.getDate(),12),add=(8-t0.getDay())%7||7,st=new Date(t0.getTime()+add*864e5),op=new Date(st.getTime()+15*864e5),Y=op.getFullYear();
 var EV=[[new Date(Y,11,20),'Navidad'],[new Date(Y+1,0,5),'Reyes'],[new Date(Y,0,5),'Reyes'],[new Date(Y,0,7),'Rebajas'],[new Date(Y,1,14),'San Valentín'],[new Date(Y+1,1,14),'San Valentín'],[new Date(Y,4,2),'Día de la Madre'],[new Date(Y,6,1),'Rebajas'],[new Date(Y,8,7),'Septiembre'],[new Date(Y,10,27),'Black Friday']]
  .filter(function(e){return e[0]>op}).sort(function(a,b){return a[0]-b[0]});
 var f=function(x){return new Intl.DateTimeFormat('es-ES',{day:'numeric',month:'short'}).format(x).replace('.','')},q=function(id,v){var e=d.getElementById(id);if(e)e.textContent=v};
 q('n-a',f(st));q('n-b',f(op));if(EV[0]){q('n-c',f(EV[0][0]));q('n-e',EV[0][1]);q('n-t',EV[0][1])}
}catch(e){}
/* barra del móvil: aparece al bajar */
var bar=d.querySelector('.bar');if(bar){var hb=function(){bar.classList.toggle('on',scrollY>420)};addEventListener('scroll',hb,{passive:true});hb();
 /* mientras se ve el móvil de la tienda, la barra se esconde para dejarle sitio */
 if(MV&&'IntersectionObserver' in window)new IntersectionObserver(function(es){bar.classList.toggle('mo-off',es[0].isIntersecting)},{rootMargin:'-30% 0px -30% 0px'}).observe(MV)}
})();</script>"""

EXTRA_CSS = '[data-view].off{display:none!important}'


def frame(src, w, hh=None, full=False, title=''):
    a = f' data-w="{w}"' + (' data-full="1"' if full else f' data-hh="{hh}"')
    h0 = 7000 if full else hh
    ar = f' style="aspect-ratio:{w}/{h0}"'
    return f'<div class="fr"{a}{ar}><iframe data-src="{src}" title="{E(title)}" tabindex="-1" style="width:{w}px;height:{h0}px"></iframe></div>'


def phone(src, hh=None, full=False, cls='', title=''):
    return f'<div class="ph{" " + cls if cls else ""}"><div class="scr"><div class="sb"></div>' + frame(src, 375, hh, full, title) + '</div></div>'


def browser(src, dom, hh=None, full=False, title=''):
    return f'<div class="bw"><div class="top"><i></i><i></i><i></i><span>{E(dom)}</span></div>' + frame(src, 1280, hh, full, title) + '</div>'


def build(slug):
    P = json.load(open(os.path.join(D, 'prop40.json'), encoding='utf-8'))[slug]
    sd = json.load(open(os.path.join(D, 'data', slug + '.json'), encoding='utf-8'))
    name, city, ig = P['name'], P['city'], sd['ig']
    t = f'/p-{slug}--tienda'
    dom = sd.get('domain') or slug.replace('-', '') + '.es'
    hi = f'Hola Christian, he visto la propuesta de {name}. '
    title = f'{E(name)} × 404 Growth · Vuestra tienda online'
    img = lambda i: f'/p-{slug}--b--{i}.jpg'

    head = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
            '<meta name="robots" content="noindex,nofollow"><meta name="theme-color" content="#F6F7F3">'
            f'<title>{title}</title><meta name="description" content="Así se vería la tienda online de {E(name)}: con vuestro catálogo, lista para vender en toda España.">'
            f'<meta property="og:type" content="website"><meta property="og:site_name" content="404 Growth"><meta property="og:title" content="{E(name)} × 404 Growth">'
            '<meta property="og:description" content="Así se vería vuestra tienda online, con vuestros productos. Os la he preparado: echadle un vistazo.">'
            f'<meta property="og:image" content="https://404growth.com/p-{slug}--b--og.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">'
            '<meta name="twitter:card" content="summary_large_image"><link rel="icon" href="/favicon.svg" type="image/svg+xml">'
            f'<style>{CSS}{EXTRA_CSS}</style></head>')

    nav = (f'<header class="nv"><div class="nv-p">{LOGO}<span>Propuesta para {E(name)}</span>'
           '<a class="b k" href="#agenda">Reservar 30 min</a></div></header>')

    hero = (f'<section class="hero w" id="inicio"><div class="ig gl"><span class="av"><b>{E(name[:1])}</b></span><div><small>@{E(ig)} <em>· {E(P["quote_when"])}</em></small><p>{E(P["quote"])}</p></div></div>'
            f'<h1>{E(name)},<span class="lm">abierta 24 horas.</span></h1>'
            f'<div class="pills"><span class="pill">{I(IC["clock"])}En 15 días</span><span class="pill">{I(IC["shield"])}Garantía 90 días</span><span class="pill">{I(IC["truck"])}Toda España</span></div>'
            f'<div class="acts"><a class="b k" href="#agenda">Reservar 30 min</a><a class="b g" href="{wa(hi)}" target="_blank" rel="noopener">{WAI}WhatsApp</a></div></section>')

    # la tienda: en el ordenador, el navegador entero y el móvil fijo al lado (Chris: «me gusta muchísimo»).
    # En el móvil (Chris, 18/11/2026, 22:28): el móvil se queda fijo y, al seguir bajando, baja la tienda de dentro hasta el final;
    # después sigue la propuesta. Debajo, Móvil / Ordenador.
    shop = (f'<section class="shop w" id="tienda">'
            '<div class="mobv"><div class="pin">'
            f'<div class="vw" data-view="m">{phone(t + "?embed=1", hh=812, cls="vp", title="Tienda en el móvil")}</div>'
            f'<div class="vw off" data-view="d">{browser(t + "?embed=1", dom, hh=860, title="Tienda en el ordenador")}</div>'
            '<div class="pg"><i></i></div>'
            f'<div class="sw gl" role="group" aria-label="Ver la tienda en"><button type="button" data-v="m" aria-pressed="true">{I(IC["mob"])}Móvil</button>'
            f'<button type="button" data-v="d" aria-pressed="false">{I(IC["desk"])}Ordenador</button></div></div></div>'
            '<div class="duo"><div class="main">'
            f'{browser(t + "?embed=1", dom, full=True, title="Tienda en el ordenador")}</div>'
            f'<div class="side"><div class="lab">{I(IC["mob"])}En el móvil</div>{phone(t + "?tour=1", hh=780, title="Tienda en el móvil, recorrido")}</div></div></section>')

    pdp = (f'<section class="pdp sec w" id="producto"><h2 class="t2 rv">Cada prenda,<span class="lm">lista para comprar.</span></h2>'
           f'<div class="row">{browser(t + "?embed=1&at=destacado", dom, hh=760, title="Ficha de producto")}{phone(t + "?embed=1&at=destacado", hh=780, title="Ficha en el móvil")}</div>'
           f'<div class="pills"><span class="pill">{I(IC["shirt"])}Su talla</span><span class="pill">{I(IC["card"])}Tarjeta y Bizum</span><span class="pill">{I(IC["truck"])}24/48 h</span></div></section>')

    qs = [('Me interesa', 'Me interesa la tienda. ¿Cuándo podemos hablar?'), ('¿Cuánto cuesta?', f'¿Cuánto costaría la tienda para {P.get("us", "nosotras")}?'), ('Tengo una duda', 'Tengo una duda: ')]
    qr = '<div class="qr">' + ''.join(f'<a href="{wa(hi + m)}" target="_blank" rel="noopener">{WAI}{E(l)}</a>' for l, m in qs) + '</div>'
    ag = AG.block(slug, name, P.get('sec', 'moda'), False)
    i0 = ag.index('<p class="ag-sub">'); i1 = ag.index('</p>', i0) + 4
    ag = ag[:i0] + qr + ag[i1:]
    a0 = '<span class="ag-eb">Agenda · 30 minutos</span><h2>Elige día y hora.<br><span>Te enseño la tienda en directo.</span></h2>'
    assert a0 in ag
    ag = ag.replace(a0, '<h2>¿Lo hablamos?<span class="lm">30 minutos, cuando queráis.</span></h2>')

    def lane(items, n, k):
        dots = '<span class="ln"></span>'.join(f'<span class="dt"><b>{I(IC[i])}</b><small>{E(s)}</small></span>' for i, s in items)
        return f'<div class="card {k}"><div class="hd">{E(n)}</div><div class="dots">{dots}</div></div>'
    st = ('<section class="st sec w" id="pedido"><h2 class="t2 rv">Menos mensajes,<span class="lm">más pedidos.</span></h2><div class="rv">'
          + lane([('eye', 'Lo ve'), ('chat', 'MD'), ('ask', '¿Talla?'), ('bizum', 'Bizum'), ('box', 'Envío')], 'Hoy · 5 pasos', 'gl')
          + '<br>' + lane([('eye', 'Lo ve'), ('tap', 'Compra'), ('box', 'Envío')], 'Con la tienda · 3 pasos', 'nw') + '</div></section>')

    gr = ('<section class="gr sec w" id="garantia"><div class="box">'
          f'<span class="seal">{I(IC["shield"])}Garantía</span><div class="big">90<small>días</small></div>'
          '<svg class="ch" viewBox="0 0 520 214" role="img" aria-label="Las ventas superan la inversión antes del día 90">'
          '<defs><linearGradient id="gg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#C9DDB8" stop-opacity=".38"/><stop offset="1" stop-color="#C9DDB8" stop-opacity="0"/></linearGradient></defs>'
          '<line class="d90" x1="440" y1="14" x2="440" y2="180"/>'
          '<line class="inv" x1="20" y1="92" x2="500" y2="92"/><text x="22" y="78">Vuestra inversión</text>'
          '<path class="ar" d="M20 180 C 120 176 200 152 270 120 S 390 52 500 24 L500 180 Z"/>'
          '<path class="sal" d="M20 180 C 120 176 200 152 270 120 S 390 52 500 24"/>'
          '<g class="ok"><circle cx="369" cy="73" r="15" fill="#C9DDB8"/><path d="m362 73 5 5 9-10" stroke="#111311" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>'
          '<text class="s" x="232" y="164">Ventas de la tienda</text>'
          '<text x="20" y="206">Día 0</text><text class="k" x="440" y="206" text-anchor="middle">Día 90</text></svg>'
          '<p class="or">Recuperáis la inversión<span>o trabajamos gratis.</span></p></div></section>')

    nw = ('<section class="nw sec w" id="ahora"><h2 class="t2 rv">Abierta antes de<span class="lm" id="n-t">Navidad</span></h2>'
          '<div class="tl rv">'
          f'<div class="ev"><b>{I(IC["phone"])}</b><strong id="n-a">lunes</strong><small>Empezamos</small></div>'
          f'<div class="ev k"><b>{I(IC["bag"])}</b><strong id="n-b">día 15</strong><small>Abierta</small></div>'
          f'<div class="ev g"><b>{I(IC["gift"])}</b><strong id="n-c">—</strong><small id="n-e">Navidad</small></div></div>'
          f'<div class="steps rv"><span>{I(IC["phone"])}Llamada <em>día 0</em></span><span>{I(IC["cam"])}Fotos y fichas</span><span>{I(IC["card"])}Pagos y envíos</span><span>{I(IC["check"])}Abierta <em>día 15</em></span></div>'
          f'<div class="you gl rv">{I(IC["check"])}<span><b>{P.get("you", "Vosotras")}:</b> una llamada y fotos.<br><b>El resto, nosotros.</b></span></div></section>')

    def ad(media, cta):
        return (f'<div class="ad"><div class="h"><i></i><div><b>{E(ig)}</b><small>Publicidad</small></div></div>{media}'
                f'<div class="c">{E(cta)}{I(IC["arrow"])}</div></div>')
    bgi = lambda i: f'style="background-image:url({img(i)})"'
    ads = ('<section class="ads sec" id="anuncios"><div class="w"><h2 class="t2 rv">Y anuncios<span class="lm">para llenarla.</span></h2></div><div class="rail">'
           + ad(f'<div class="m" {bgi("l1")}><h4>Nueva temporada.<br>Pídela hoy.</h4></div>', 'Comprar ahora')
           + ad(f'<div class="m" {bgi("h")}><h4>De {E(city)}<br>a toda España.</h4></div>', 'Comprar ahora')
           + ad(f'<div class="m col"><div {bgi("p2")}></div><div {bgi("p3")}></div><div {bgi("p4")}></div></div>', 'Ver el look')
           + ad(f'<div class="m" {bgi("b")}><h4>Vuestra tienda,<br>abierta 24 horas.</h4></div>', 'Visitar')
           + '</div></section>')

    cl = (f'<section class="cl w" id="hablar"><img class="me" src="/christian-hola.jpg" alt="Christian" width="76" height="76" loading="lazy">'
          f'<h2 class="t2">¿Abrimos {E(name)}<span class="lm">a toda España?</span></h2>'
          f'<div class="acts"><a class="b k" href="#agenda">Reservar 30 min</a><a class="b g" href="{wa(hi)}" target="_blank" rel="noopener">{WAI}Escribir a Christian</a></div></section>')

    foot = (f'<footer>404 Growth · Propuesta para {E(name)} · Tienda de ejemplo, con fotos hechas con IA a partir de vuestras publicaciones.</footer>'
            f'<div class="bar wa-fab"><a class="b k" href="#agenda">Reservar 30 min</a><a class="b g" href="{wa(hi)}" target="_blank" rel="noopener" aria-label="WhatsApp">{WAI}</a></div>')

    body = '<body>' + nav + '<main>' + hero + shop + pdp + ag + st + gr + nw + ads + cl + '</main>' + foot
    cnt = open(os.path.join(D, 'tpl', 'counter.html'), encoding='utf-8').read().replace('var slug="cafe-con-bacon"', f'var slug="{slug}"')
    assert f'var slug="{slug}"' in cnt
    h = head + body + JS + cnt + '</body></html>'
    out = os.path.join(OUT, f'p-{slug}.html')
    open(out, 'w', encoding='utf-8').write(h)
    print('ok', slug, len(h), out)
    return out


if __name__ == '__main__':
    for s in sys.argv[1:]:
        build(s)
