"""Lote 40 (19/11/2026) · la propuesta nueva, con el aspecto del admin (tema v34).
Chris (18/11/2026): «mismo lettering, colores y estructuras que nuestro admin», sin precio, con la garantía («retorno de la inversión
en 90 días o trabajamos gratis hasta conseguirlo»), sin testimonios de clientes, con la agenda dentro y las fotos de Google Flow.
Solo para las propuestas nuevas: las ya enviadas se quedan como están (gen33v.py).

uso: python3 gen40.py <slug> [...] [--local]   → out/p-<slug>.html
  - la tienda (out/p-<slug>--tienda.html y sus fotos) la hace antes gen37a.py (L33_AI=<fotos> python3 gen37a.py <slug>);
  - los textos de cada tienda están en prop40.json (sus palabras, cómo venden hoy, sus envíos);
  - --local: los marcos piden p-<slug>--tienda.html (para verla desde file:// en el Mac); en la web van sin .html.

Estructura (como el Inicio del admin): saludo con la fecha, cuatro anillos (15 días, 24/7, 90 días, 3 cosas), su tienda en un
navegador y un móvil, la garantía en negro, sus palabras, «Del «me lo guardas» al pedido», los 15 días en barras, por qué ahora
(fechas calculadas al abrirla), lo que les pedimos (3 cosas), dudas, respuestas rápidas por WhatsApp, la agenda y la nota de Christian."""
import html, json, os, sys, urllib.parse

D = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(D, 'out')
sys.path.insert(0, os.path.join(D, '..', '..', 'tools', 'agenda'))
import patch as AG  # noqa: E402

E = lambda s: html.escape(str(s), quote=True)
WA = '34610594450'


def wa(text):
    return f'https://wa.me/{WA}?text=' + urllib.parse.quote(text)


LOGO = ('<svg class="mk" viewBox="20 60 362 280" aria-hidden="true"><g transform="skewX(-12) translate(52 0)" fill="none" stroke="currentColor" stroke-width="32" '
        'stroke-linecap="round" stroke-linejoin="round"><rect x="140" y="90" width="120" height="220" rx="60"/><path d="M155.1 110.2 L40 240 L140 240"/>'
        '<path d="M244.9 110.2 L360 240 L260 240"/></g></svg>')
AR = '<svg class="ar" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
OUTL = '<svg class="ar" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/></svg>'
WAI = ('<svg class="wi" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3a.5.5 0 0 0 0-.5l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 11.9 11.9 0 0 0 4.6 4c1.7.7 2.4.8 3.2.7a2.8 2.8 0 0 0 1.8-1.3 2.3 2.3 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3Z"/></svg>')
QM = '<svg class="qm" viewBox="0 0 34 26" aria-hidden="true"><path fill="currentColor" d="M0 26V15.6C0 6.9 4.3 1.7 12.9 0l1.6 3.4C9.8 4.9 7.5 7.8 7.2 12h6.4v14H0Zm19.5 0V15.6C19.5 6.9 23.8 1.7 32.4 0L34 3.4c-4.7 1.5-7 4.4-7.3 8.6h6.4v14H19.5Z"/></svg>'
CHK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 12.5 4 4L18 8"/></svg>'


def ring(p, dark=False):
    c = 2 * 3.14159265 * 42
    return (f'<svg class="rg" viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="42" class="bg"/>'
            f'<circle cx="50" cy="50" r="42" class="fg{" k" if dark else ""}" style="stroke-dasharray:{c:.1f};stroke-dashoffset:{c:.1f};--o:{c * (1 - p / 100):.1f}"/></svg>')


def tile(p, big, sub, lbl, cls=''):
    dark = 'noir' in cls
    return (f'<div class="c t {cls}">{ring(p, dark)}<div><div class="big">{big}'
            + (f'<small>{sub}</small>' if sub else '') + f'</div><div class="lbl">{lbl}</div></div></div>')


CSS = r"""
:root{--bg:#F6F7F3;--ink:#111311;--ink2:#3A3F3A;--mut:#6F766E;--lm:#7C8B74;--line:rgba(17,19,17,.09);--line2:rgba(17,19,17,.06);
--sage:#C9DDB8;--sage2:#B3CE9C;--sage3:#E8F0E0;--noir:#111311;
--glass:linear-gradient(160deg,rgba(255,255,255,.84),rgba(255,255,255,.56));
--gsh:inset 0 1px 0 #fff,inset 0 0 0 1px rgba(255,255,255,.6),0 0 0 1px rgba(17,19,17,.05),0 24px 48px -30px rgba(30,45,25,.34);
--gsh-sm:inset 0 1px 0 #fff,0 0 0 1px rgba(17,19,17,.08),0 6px 16px -10px rgba(30,45,25,.4);
--f:-apple-system,BlinkMacSystemFont,"SF Pro Display","SF Pro Text","Inter Tight",Inter,"Helvetica Neue",Arial,sans-serif;--pad:40px;--r:28px;--ease:cubic-bezier(.2,.7,.2,1)}
*,*:before,*:after{box-sizing:border-box}
html{background:var(--bg);-webkit-text-size-adjust:100%;scroll-behavior:smooth;scroll-padding-top:84px}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--f);font-size:16px;line-height:1.5;-webkit-font-smoothing:antialiased;overflow-x:clip;position:relative;isolation:isolate;letter-spacing:-.005em}
body:before{content:"";position:fixed;inset:0;z-index:-2;pointer-events:none;background:radial-gradient(900px 520px at 8% -6%,rgba(201,221,184,.62),transparent 70%),radial-gradient(800px 600px at 100% 38%,rgba(201,221,184,.38),transparent 70%),radial-gradient(700px 500px at 30% 110%,rgba(179,206,156,.3),transparent 70%),var(--bg)}
::selection{background:rgba(179,206,156,.6)}
a{color:inherit}img,svg{display:block;max-width:100%}h1,h2,h3,p{margin:0}h1,h2,h3{text-wrap:balance;font-weight:500}p{text-wrap:pretty}ul,ol{margin:0;padding:0;list-style:none}
:focus-visible{outline:2px solid var(--ink);outline-offset:3px;border-radius:10px}
.w{width:100%;max-width:1240px;margin:0 auto;padding:0 var(--pad)}
.lm{color:var(--lm);font-weight:300}.mut{color:var(--mut)}
@media (max-width:899px){:root{--pad:20px;--r:24px}}@media (max-width:420px){:root{--pad:16px}}

/* cabecera */
.nv{position:sticky;top:0;z-index:40;background:rgba(246,247,243,.94);transition:box-shadow .3s}
@media (min-width:900px){.nv{background:rgba(246,247,243,.7);-webkit-backdrop-filter:blur(22px) saturate(170%);backdrop-filter:blur(22px) saturate(170%)}}
.nv.on{box-shadow:0 1px 0 var(--line2)}
.nv-in{display:flex;align-items:center;gap:14px;height:68px}
.nv-logo{display:flex;align-items:center;gap:9px;text-decoration:none;font-weight:800;letter-spacing:-.03em;font-size:16px;white-space:nowrap}.nv-logo .mk{width:32px;height:25px;color:var(--ink)}
.nv-for{display:inline-flex;align-items:center;gap:8px;height:34px;padding:0 14px;border-radius:99px;background:rgba(255,255,255,.66);box-shadow:var(--gsh-sm);font-size:13.5px;font-weight:500;color:var(--ink2);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;min-width:0}
.nv-for i{width:7px;height:7px;border-radius:50%;background:#7DBA5E;box-shadow:0 0 0 3px rgba(125,186,94,.22);flex:none}
.nv-lk{display:flex;gap:2px;margin-left:auto;font-size:14px;font-weight:500;color:var(--ink2)}.nv-lk a{text-decoration:none;padding:8px 12px;border-radius:99px}.nv-lk a:hover{background:rgba(255,255,255,.7);color:var(--ink)}
.b-pri{display:inline-flex;align-items:center;justify-content:center;gap:9px;min-height:44px;padding:0 20px;border-radius:99px;background:linear-gradient(160deg,#22261F,#0E100E);color:#F3F6EF;font-weight:600;font-size:15px;letter-spacing:-.01em;text-decoration:none;border:0;cursor:pointer;white-space:nowrap;box-shadow:inset 0 1px 0 rgba(255,255,255,.14),0 14px 30px -14px rgba(17,19,17,.6);transition:transform .2s var(--ease)}
.b-pri:hover{transform:translateY(-1px)}.b-pri:active{transform:scale(.98)}.b-pri.lg{min-height:54px;padding:0 26px;font-size:16.5px}
.b-gl{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:44px;padding:0 18px;border-radius:99px;background:rgba(255,255,255,.72);box-shadow:var(--gsh-sm);border:0;font-weight:600;font-size:15px;text-decoration:none;cursor:pointer;color:var(--ink);white-space:nowrap}
.b-gl:hover{background:#fff}.b-gl.lg{min-height:54px;padding:0 22px;font-size:16px}
.ar{width:17px;height:17px;flex:none}.wi{width:19px;height:19px;flex:none;color:#25D366}
@media (max-width:1060px){.nv-lk{display:none}.nv-in>.b-pri{margin-left:auto}}
@media (max-width:640px){.nv-for{display:none}.nv-in{height:60px}.nv-in>.b-gl{display:none}}

/* saludo (como el Inicio del admin) */
.hd{padding-top:44px;padding-bottom:26px}
.dt{font-size:14px;color:var(--mut);font-weight:500;margin-bottom:12px}
.hd h1{font-size:clamp(36px,5.2vw,66px);line-height:1.04;letter-spacing:-.034em;font-weight:400}
.hd h1 .lm{display:block}
.hd .sub{margin-top:18px;max-width:720px;font-size:clamp(17px,1.6vw,19.5px);color:var(--ink2);line-height:1.5}
.hd .acts{display:flex;flex-wrap:wrap;gap:10px;margin-top:24px}
.sig{display:flex;flex-wrap:wrap;gap:8px;margin-top:22px}
.sig li{display:inline-flex;align-items:center;gap:8px;height:32px;padding:0 13px;border-radius:99px;background:rgba(255,255,255,.62);box-shadow:var(--gsh-sm);font-size:13px;font-weight:500;color:var(--ink2)}
.sig li svg{width:14px;height:14px;color:#5E7F4E}

/* la rejilla de tarjetas */
.g{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));gap:16px;margin-bottom:16px}
.c{position:relative;border-radius:var(--r);padding:22px 24px;background:var(--glass);box-shadow:var(--gsh)}
@media (min-width:900px){.c{-webkit-backdrop-filter:blur(20px) saturate(160%);backdrop-filter:blur(20px) saturate(160%)}}
.noir{background:linear-gradient(160deg,#1A1D19,#0E100E);color:#EEF2EA;box-shadow:inset 0 1px 0 rgba(255,255,255,.08),0 30px 60px -30px rgba(10,16,8,.7)}
.s3{grid-column:span 3}.s4{grid-column:span 4}.s5{grid-column:span 5}.s6{grid-column:span 6}.s7{grid-column:span 7}.s8{grid-column:span 8}.s12{grid-column:span 12}
.t{display:flex;align-items:center;gap:16px;padding:20px 22px}
.rg{width:84px;height:84px;flex:none;transform:rotate(-90deg)}.rg circle{fill:none;stroke-width:9}.rg .bg{stroke:rgba(17,19,17,.07)}
.rg .fg{stroke:var(--sage2);stroke-linecap:round;transition:stroke-dashoffset 1.6s cubic-bezier(.2,.8,.2,1)}.rg .fg.k{stroke:var(--sage)}.noir .rg .bg{stroke:rgba(255,255,255,.1)}
.in .rg .fg{stroke-dashoffset:var(--o)!important}
.big{font-weight:300;font-size:40px;letter-spacing:-.04em;line-height:1;white-space:nowrap}.big small{font-size:14px;color:var(--mut);margin-left:5px;letter-spacing:-.01em;font-weight:400}
.noir .big small{color:#9DA79A}
.lbl{font-size:13px;color:var(--mut);margin-top:7px;line-height:1.38}.noir .lbl{color:#A7B1A3}
.ch{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:14px}
.ch h2,.ch h3{font-size:15.5px;font-weight:600;letter-spacing:-.02em}.ch small{color:var(--mut);font-size:13px}.noir .ch small{color:#9DA79A}
.eb{font-size:12.5px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--lm)}
.noir .eb{color:#9DB58D}

/* su tienda */
.shop{padding:22px 24px 26px;overflow:hidden}
.shop .ch a{white-space:nowrap;flex:none;display:inline-flex;align-items:center;gap:7px;font-size:14px;font-weight:600;text-decoration:none;padding:8px 14px;border-radius:99px;background:rgba(255,255,255,.8);box-shadow:var(--gsh-sm)}
.stage{position:relative;padding:0 0 28px}
.bw{border-radius:16px;overflow:hidden;background:#fff;box-shadow:0 0 0 1px rgba(17,19,17,.08),0 30px 60px -34px rgba(20,30,16,.5)}
.bw-b{display:flex;align-items:center;gap:7px;height:34px;padding:0 14px;background:#F1F2EE;border-bottom:1px solid rgba(17,19,17,.06)}
.bw-b i{width:10px;height:10px;border-radius:50%;background:#DCDDD8}.bw-b span{margin-left:12px;flex:1;max-width:340px;height:22px;border-radius:7px;background:#fff;font-size:11.5px;color:var(--mut);display:flex;align-items:center;padding:0 10px;white-space:nowrap;overflow:hidden}
.sc{position:relative;width:100%;aspect-ratio:1280/740;overflow:hidden}
.sc iframe{position:absolute;left:0;top:0;width:1280px;height:740px;border:0;transform-origin:0 0;transform:scale(var(--s,.6));background:#fff;pointer-events:none}
.ph{position:absolute;right:-6px;bottom:0;width:190px;border-radius:30px;padding:7px;background:#111311;box-shadow:0 30px 60px -24px rgba(10,16,8,.6)}
.ph .pin{position:relative;border-radius:24px;overflow:hidden;aspect-ratio:375/780;background:#fff}
.ph iframe{position:absolute;left:0;top:0;width:375px;height:780px;border:0;transform-origin:0 0;transform:scale(var(--p,.47));pointer-events:none}
.shop .cap{display:flex;flex-wrap:wrap;gap:8px 18px;margin-top:4px;font-size:13px;color:var(--mut)}.shop .cap span{display:inline-flex;align-items:center;gap:6px}.shop .cap svg{width:14px;height:14px;color:#5E7F4E}

/* garantía */
.gar{display:flex;flex-direction:column;gap:16px;padding:26px}
.gar .gr{position:relative;width:150px;height:150px;margin:6px 0 2px}.gar .gr .rg{width:150px;height:150px}.gar .gr b{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;font-weight:300;font-size:54px;letter-spacing:-.06em;line-height:1}
.gar .gr b small{display:block;font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;color:#9DB58D;font-weight:600;margin-top:6px}
.gar h2{font-size:26px;letter-spacing:-.035em;line-height:1.1;font-weight:500}
.gar p{color:#C3CCBF;font-size:15.5px;line-height:1.5}.gar p b{color:#fff;font-weight:600}
.gar ul{display:flex;flex-direction:column;gap:9px;margin-top:2px}.gar li{display:flex;gap:10px;font-size:14px;color:#D8DFD4;line-height:1.4}.gar li svg{width:17px;height:17px;flex:none;color:var(--sage);margin-top:1px}

/* sus palabras */
.qt{display:flex;flex-direction:column;gap:16px;padding:26px}
.qt blockquote{margin:0;font-size:clamp(22px,2.2vw,28px);line-height:1.22;letter-spacing:-.03em;font-weight:400}
.qt .qm{width:34px;height:26px;color:var(--sage2)}
.qt cite{font-style:normal;font-size:13px;color:var(--mut);display:flex;align-items:center;gap:8px}.qt cite i{width:22px;height:22px;border-radius:7px;background:linear-gradient(45deg,#F58529,#DD2A7B,#8134AF);flex:none}
.qt p{font-size:15px;color:var(--ink2);line-height:1.55}.qt p.an{padding-top:14px;border-top:1px solid var(--line2);color:var(--ink)}

/* del «me lo guardas» al pedido */
.fl .cols{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.fl h4{margin:0 0 10px;font-size:13.5px;font-weight:600;display:flex;align-items:baseline;gap:8px}.fl h4 em{font-style:normal;font-weight:300;font-size:30px;letter-spacing:-.045em}
.fl h4 span{font-weight:400;color:var(--mut);font-size:12.5px}
.fl ol{display:flex;flex-direction:column;gap:7px;counter-reset:s}
.fl li{position:relative;display:grid;grid-template-columns:22px 1fr;gap:10px;align-items:center;min-height:44px;padding:8px 12px 8px 10px;border-radius:14px;font-size:13.5px;line-height:1.3;background:rgba(17,19,17,.035)}
.fl li:before{counter-increment:s;content:counter(s);display:grid;place-items:center;width:22px;height:22px;border-radius:8px;font-size:11.5px;font-weight:700;background:var(--sage);color:#1E2D1A}
.fl li.v:before{background:#111311;color:#C9DDB8}
.fl .nw li{background:rgba(201,221,184,.32)}
.fl .key{display:flex;flex-wrap:wrap;gap:6px 16px;margin-top:14px;font-size:12.5px;color:var(--ink2)}.fl .key span{display:inline-flex;align-items:center;gap:7px}.fl .key i{width:10px;height:10px;border-radius:3px;background:var(--sage)}.fl .key i.v{background:#111311}
.fl .nt{margin-top:12px;font-size:13.5px;color:var(--mut);line-height:1.5}

/* los 15 días */
.pl .gt{position:relative;margin-top:6px}
.pl .ax{display:grid;grid-template-columns:repeat(16,1fr);font-size:11px;color:var(--mut);margin:0 0 8px 0;padding-left:var(--lw)}
.pl .ax span{text-align:left}
.pl{--lw:230px}
.pl .rw{display:grid;grid-template-columns:var(--lw) 1fr;align-items:center;gap:0;min-height:40px}
.pl .rw b{font-size:13.5px;font-weight:600;padding-right:14px;line-height:1.25}.pl .rw b small{display:block;font-weight:400;color:var(--mut);font-size:12px}
.pl .tr{position:relative;height:26px;border-radius:9px;background:rgba(17,19,17,.04)}
.pl .tr i{position:absolute;top:0;bottom:0;left:calc(var(--a)*100%/16);width:0;border-radius:9px;background:linear-gradient(90deg,var(--sage2),var(--sage));transition:width 1.1s cubic-bezier(.2,.8,.2,1)}
.pl .rw.k .tr i{background:#111311}
.pl.in .tr i{width:calc(var(--w)*100%/16)}
.pl .tr i em{position:absolute;right:8px;top:50%;transform:translateY(-50%);font-style:normal;font-size:11px;font-weight:600;color:#1E2D1A;white-space:nowrap}.pl .rw.k .tr i em{color:#C9DDB8}.pl .tr i.o em{right:auto;left:calc(100% + 8px);color:var(--ink2)}.pl .rw.k .tr i.ol em{right:calc(100% + 8px);color:var(--ink)}
.pl .grid{position:absolute;top:24px;bottom:0;left:var(--lw);right:0;display:grid;grid-template-columns:repeat(16,1fr);pointer-events:none}.pl .grid span{border-left:1px dashed rgba(17,19,17,.06)}

/* por qué ahora */
.nw2{display:flex;flex-direction:column;gap:14px}
.nw2 .dd{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:10px}
.nw2 .dd div{padding:14px;border-radius:18px;background:rgba(255,255,255,.75);box-shadow:var(--gsh-sm)}
.nw2 .dd div.k{background:#111311;color:#EEF2EA;box-shadow:none}
.nw2 .dd small{display:block;font-size:11.5px;color:var(--mut);font-weight:600;letter-spacing:.06em;text-transform:uppercase}.nw2 .dd div.k small{color:#9DB58D}
.nw2 .dd b{display:block;font-weight:300;font-size:30px;letter-spacing:-.05em;line-height:1.05;margin-top:4px}.nw2 .dd span{display:block;font-size:12.5px;color:var(--mut);text-transform:capitalize}.nw2 .dd div.k span{color:#A7B1A3}
.nw2 .dd>svg{width:20px;height:20px;color:var(--mut)}
.nw2 p{font-size:15px;line-height:1.5;color:var(--ink2)}.nw2 p b{color:var(--ink)}

/* lo que os pedimos */
.yo .three{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.yo .three div{padding:18px;border-radius:20px;background:rgba(255,255,255,.75);box-shadow:var(--gsh-sm)}
.yo .three b{display:block;font-weight:300;font-size:34px;letter-spacing:-.05em;line-height:1;color:var(--lm)}
.yo .three h3{font-size:16px;font-weight:600;letter-spacing:-.02em;margin:12px 0 6px}.yo .three p{font-size:14px;color:var(--mut);line-height:1.5}
.yo .rest{display:flex;align-items:center;gap:14px;margin-top:12px;padding:16px 18px;border-radius:20px;background:#111311;color:#EEF2EA}
.yo .rest svg{width:22px;height:22px;flex:none;color:var(--sage)}.yo .rest p{font-size:14.5px;line-height:1.45;color:#D8DFD4}.yo .rest b{color:#fff}

/* dudas */
.fq details{border-top:1px solid var(--line2)}.fq details:first-of-type{border-top:0}
.fq summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:14px;padding:15px 2px;font-size:15.5px;font-weight:600;letter-spacing:-.015em}
.fq summary::-webkit-details-marker{display:none}
.fq summary:after{content:"";width:26px;height:26px;flex:none;border-radius:50%;background:rgba(17,19,17,.05) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23111311' stroke-width='2.2' stroke-linecap='round'%3E%3Cpath d='M12 6v12M6 12h12'/%3E%3C/svg%3E") center/14px no-repeat;transition:transform .3s var(--ease)}
.fq details[open] summary:after{transform:rotate(45deg)}
.fq details p{padding:0 2px 16px;font-size:15px;color:var(--ink2);line-height:1.55;max-width:640px}

/* respuestas rápidas */
.qr{display:flex;flex-direction:column;gap:14px}.qr .me{margin-top:auto;display:flex;align-items:center;gap:12px;padding-top:16px;border-top:1px solid rgba(255,255,255,.1);font-size:13.5px;color:#A7B1A3}.qr .me img{width:40px;height:40px;border-radius:50%;object-fit:cover}.qr .me b{display:block;color:#F3F6EF;font-weight:600;font-size:14.5px}
.qr h2{font-size:28px;letter-spacing:-.03em;line-height:1.08;font-weight:500}.qr h2 .lm{display:block}
.qr p{font-size:14.5px;color:#C3CCBF;line-height:1.5}
.qr .bt{display:flex;flex-direction:column;gap:8px}
.qr .bt a{display:flex;align-items:center;gap:10px;padding:13px 16px;border-radius:16px;background:rgba(255,255,255,.07);box-shadow:inset 0 0 0 1px rgba(255,255,255,.1);color:#F3F6EF;text-decoration:none;font-size:15px;font-weight:500;transition:background .2s}
.qr .bt a:hover{background:rgba(255,255,255,.13)}.qr .bt a span{flex:1}.qr .bt a .ar{color:#9DB58D}
.qr .or{display:flex;gap:10px;flex-wrap:wrap;margin-top:4px}
.qr .or a{flex:1}
.qr .b-pri{background:#F3F6EF;color:#111311;box-shadow:none}

/* nota de Christian */
.nt2{display:grid;grid-template-columns:auto 1fr;gap:22px;align-items:start;padding:28px}
.nt2 img{width:64px;height:64px;border-radius:50%;object-fit:cover}
.nt2 p{font-size:17px;line-height:1.6;color:var(--ink2);max-width:760px}.nt2 p+p{margin-top:12px}
.nt2 .sg{margin-top:16px;font-size:14px;color:var(--mut)}.nt2 .sg b{color:var(--ink);font-weight:600}

/* la agenda, con el mismo aspecto */
.ag{--t:#111311;--td:#000;--cream:transparent;padding:56px 0 40px!important}
.ag h2{font-weight:500!important;letter-spacing:-.034em!important}.ag h2 span{color:var(--lm)!important;font-weight:300}
.ag .ag-w{max-width:1240px!important;padding:0 var(--pad)!important}
.ag-card{border:0!important;border-radius:var(--r)!important;box-shadow:var(--gsh)!important}
.ag-me{background:rgba(246,247,243,.7)!important}

footer{padding:34px 0 120px;font-size:13px;color:var(--mut)}footer .w{display:flex;flex-wrap:wrap;gap:8px 22px;justify-content:space-between}

/* WhatsApp fijo */
.wa-fab{position:fixed;right:20px;bottom:20px;z-index:70;display:flex;align-items:center;gap:11px;padding:7px 20px 7px 7px;border-radius:999px;background:rgba(17,19,17,.92);color:#F3F6EF;text-decoration:none;font-size:14.5px;font-weight:600;box-shadow:0 20px 40px -18px rgba(10,16,8,.7);transform:translateY(120%);opacity:0;transition:transform .45s var(--ease),opacity .3s}
.wa-fab.on{transform:none;opacity:1}.wa-fab img{width:38px;height:38px;border-radius:50%;object-fit:cover}.wa-fab small{display:block;font-size:12px;font-weight:400;color:#A7B1A3}

/* aparición */
.rv{opacity:0;transform:translateY(14px);transition:opacity .7s var(--ease),transform .7s var(--ease)}.rv.in{opacity:1;transform:none}

@media (max-width:1100px){.s3{grid-column:span 6}.s4,.s5,.s7,.s8{grid-column:span 12}.pl{--lw:190px}}
@media (max-width:899px){
 .hd{padding-top:26px;padding-bottom:18px}.sig li:nth-child(n+3){display:none}.hd .acts{display:grid;grid-template-columns:1fr 1fr}.hd .acts a{min-height:50px;padding:0 12px;font-size:15px}
 .g{gap:12px;margin-bottom:12px}.c{padding:18px}
 .s3{grid-column:span 6}.t{flex-direction:column;align-items:flex-start;gap:12px;padding:16px}.t .rg{width:56px;height:56px}.big{font-size:32px}.lbl{font-size:12.5px}
 .shop{order:-1;padding:18px 16px 20px}.shop .ch h2{font-size:15px}.shop .ch a{padding:8px 12px;font-size:13.5px}.shop .cap{justify-content:center;margin-top:14px}
 .stage{padding:0}.bw{display:none}.ph{position:relative;right:auto;bottom:auto;width:min(290px,78vw);margin:4px auto 0}
 .fl .cols{grid-template-columns:1fr}
 .pl{--lw:0px}.pl .ax,.pl .grid{display:none}.pl .rw{grid-template-columns:1fr;gap:6px;margin-bottom:10px}
 .yo .three{grid-template-columns:1fr}
 .nt2{grid-template-columns:1fr;padding:22px}.nt2 p{font-size:16px}
 .wa-fab{left:12px;right:12px;bottom:12px;justify-content:center}
 .ag{padding:36px 0 24px!important}
}
@media (max-width:380px){.big{font-size:28px}}
@media (prefers-reduced-motion:reduce){.rv{opacity:1;transform:none;transition:none}.rg .fg,.pl .tr i{transition:none}}
"""

JS = r"""<script>(function(){
var d=document;
/* saludo y fecha, en hora de España */
try{var tz='Europe/Madrid',now=new Date(),h=+new Intl.DateTimeFormat('es-ES',{hour:'numeric',hourCycle:'h23',timeZone:tz}).format(now);
 var g=h>=6&&h<14?'Buenos días':h>=14&&h<21?'Buenas tardes':'Buenas noches';var el=d.getElementById('gr');if(el)el.textContent=g;
 var dt=d.getElementById('dt');if(dt){var ds=new Intl.DateTimeFormat('es-ES',{weekday:'long',day:'numeric',month:'long',timeZone:tz}).format(now);dt.textContent=ds.charAt(0).toUpperCase()+ds.slice(1)+' · '+dt.getAttribute('data-c')}
 /* por qué ahora: si empezamos el lunes que viene, abre 15 días después; la fecha que viene después */
 var t0=new Date(now.getTime());t0.setHours(12,0,0,0);var add=(8-t0.getDay())%7||7;var st=new Date(t0.getTime()+add*864e5),op=new Date(st.getTime()+15*864e5);
 var Y=op.getFullYear(),EV=[[new Date(Y,11,18),'los pedidos de Navidad','Navidad'],[new Date(Y+1,0,4),'Reyes','Reyes'],[new Date(Y,0,4),'Reyes','Reyes'],[new Date(Y,0,7),'las rebajas de enero','Rebajas'],[new Date(Y,1,10),'San Valentín','San Valentín'],
  [new Date(Y,2,15),'la temporada de primavera','Primavera'],[new Date(Y,3,28),'el Día de la Madre','Día de la Madre'],[new Date(Y,5,25),'las rebajas de verano','Rebajas'],[new Date(Y,8,10),'la vuelta de septiembre','Septiembre'],[new Date(Y,10,20),'el Black Friday','Black Friday'],
  [new Date(Y+1,1,10),'San Valentín','San Valentín']].filter(function(e){return e[0]>op}).sort(function(a,b){return a[0]-b[0]});
 var f=function(x){return new Intl.DateTimeFormat('es-ES',{day:'numeric',month:'short'}).format(x).replace('.','')},fw=function(x){return new Intl.DateTimeFormat('es-ES',{weekday:'long'}).format(x)};
 var q=function(id,v){var e=d.getElementById(id);if(e)e.textContent=v};
 q('nw-a',f(st));q('nw-aw',fw(st));q('nw-b',f(op));q('nw-bw',fw(op));
 if(EV[0]){var ev=EV[0],dd=Math.round((ev[0]-op)/864e5);q('nw-e',ev[1]);q('nw-d',dd>1?dd+' días antes':'justo a tiempo')}
}catch(e){}
/* cabecera con línea al bajar, aparición, anillos y barras */
var nv=d.querySelector('.nv');addEventListener('scroll',function(){nv&&nv.classList.toggle('on',scrollY>8)},{passive:true});
var R=[].slice.call(d.querySelectorAll('.rv,.c,.pl'));
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target)}})},{rootMargin:'0px 0px -8% 0px'});R.forEach(function(e){io.observe(e)})}else R.forEach(function(e){e.classList.add('in')});
/* los marcos de la tienda: se cargan al acercarse y se escalan a su caja */
var F=[].slice.call(d.querySelectorAll('iframe[data-src]'));function L(f){if(!f.src)f.src=f.dataset.src}
function fit(){d.querySelectorAll('.sc').forEach(function(s){s.style.setProperty('--s',(s.clientWidth/1280).toFixed(4))});d.querySelectorAll('.pin').forEach(function(p){p.style.setProperty('--p',(p.clientWidth/375).toFixed(4))})}
fit();addEventListener('resize',fit);
if('IntersectionObserver' in window){var io2=new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting)L(x.target);try{x.target.contentWindow&&x.target.contentWindow.postMessage({t404:x.isIntersecting},'*')}catch(e){}})},{rootMargin:'400px 0px'});F.forEach(function(f){io2.observe(f)})}else F.forEach(L);
/* WhatsApp fijo: aparece al bajar y se esconde en la agenda (agenda.js) */
var b=d.querySelector('.wa-fab');if(b){var hb=function(){b.classList.toggle('on',scrollY>520)};addEventListener('scroll',hb,{passive:true});hb()}
})();</script>"""


def build(slug, local=False):
    P = json.load(open(os.path.join(D, 'prop40.json'), encoding='utf-8'))[slug]
    sd = json.load(open(os.path.join(D, 'data', slug + '.json'), encoding='utf-8'))
    name, city = P['name'], P['city']
    tienda = f'p-{slug}--tienda' + ('.html' if local else '')
    shop_url = f'/p-{slug}--tienda' if not local else tienda
    hi = f'Hola Christian, he visto la propuesta de {name}. '
    title = f'{E(name)} × 404 Growth · Vuestra tienda online'
    og_t, og_d = f'{E(name)} × 404 Growth', 'Así se vería vuestra tienda online, con vuestros productos. Os la he preparado: echadle un vistazo.'
    dom = sd.get('domain') or slug.replace('-', '') + '.es'
    who = P.get('who', 'vosotras')

    head = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
            '<meta name="robots" content="noindex,nofollow"><meta name="theme-color" content="#F6F7F3">'
            f'<title>{title}</title><meta name="description" content="Así se vería la tienda online de {E(name)}: con vuestro catálogo, lista para vender en toda España.">'
            f'<meta property="og:type" content="website"><meta property="og:site_name" content="404 Growth"><meta property="og:title" content="{og_t}"><meta property="og:description" content="{og_d}">'
            f'<meta property="og:image" content="https://404growth.com/p-{slug}--b--og.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">'
            '<meta name="twitter:card" content="summary_large_image"><link rel="icon" href="/favicon.svg" type="image/svg+xml">'
            f'<style>{CSS}</style></head>')

    nav = (f'<header class="nv"><div class="w nv-in"><a class="nv-logo" href="#inicio">{LOGO}404 Growth</a>'
           f'<span class="nv-for"><i></i>Propuesta para {E(name)}</span>'
           '<nav class="nv-lk"><a href="#tienda">La tienda</a><a href="#garantia">Garantía</a><a href="#plan">15 días</a><a href="#dudas">Dudas</a></nav>'
           f'<a class="b-gl" href="{wa(hi)}" target="_blank" rel="noopener">{WAI}Escribir</a>'
           f'<a class="b-pri" href="#agenda">Reservar llamada</a></div></header>')

    sig = ''.join(f'<li>{CHK}{E(s)}</li>' for s in P['signals'])
    hd = (f'<section class="hd w" id="inicio"><p class="dt" id="dt" data-c="{E(city)}">{E(city)}</p>'
          f'<h1><span id="gr">Hola</span>, {E(name)}.<span class="lm">Vuestra tienda online ya está hecha.</span></h1>'
          f'<p class="sub">La hemos montado con vuestras prendas para que la veáis antes de decidir nada. Tiene cesta, tallas y pago, y se ve igual de bien en el móvil.</p>'
          f'<ul class="sig">{sig}</ul>'
          f'<div class="acts"><a class="b-pri lg" href="#tienda">Ver vuestra tienda{AR}</a><a class="b-gl lg" href="#agenda">Reservar 30 min</a></div></section>')

    kpis = (tile(100, '15', 'días', 'para tenerla abierta y vendiendo', 's3')
            + tile(100, '24/7', '', 'abierta también de noche y en domingo', 's3 noir')
            + tile(78, '90', 'días', 'o trabajamos gratis hasta que recuperéis la inversión', 's3')
            + tile(30, '3', 'cosas', f'es todo lo que os pedimos; lo demás, nosotros', 's3'))

    shop = (f'<section class="c s8 shop" id="tienda"><div class="ch"><div><p class="eb">Vuestra tienda online</p><h2>{E(name)}, abierta 24 horas</h2></div>'
            f'<a href="{shop_url}" target="_blank" rel="noopener">Abrir la tienda{OUTL}</a></div>'
            f'<div class="stage"><div class="bw"><div class="bw-b"><i></i><i></i><i></i><span>{E(dom)}</span></div>'
            f'<div class="sc"><iframe data-src="{tienda}?tour=1" title="Tienda de {E(name)}" tabindex="-1" loading="lazy"></iframe></div></div>'
            f'<div class="ph"><div class="pin"><iframe data-src="{tienda}?tour=1" title="Tienda de {E(name)} en el móvil" tabindex="-1" loading="lazy"></iframe></div></div></div>'
            f'<div class="cap"><span>{CHK}Hecha con vuestras prendas</span><span>{CHK}Tallas, cesta y pago</span><span>{CHK}Envíos a península y Portugal</span></div></section>')

    gar = (f'<section class="c s4 noir gar" id="garantia"><p class="eb">Garantía</p><div class="gr">{ring(100, True)}<b>90<small>días</small></b></div>'
           f'<h2>Recuperáis la inversión en 90 días, o trabajamos gratis hasta conseguirlo.</h2>'
           f'<p>Lo que invertís en la tienda tiene que volver con las ventas de la tienda. Si a los 90 días no ha vuelto, <b>seguimos trabajando sin cobrar</b> hasta que vuelva.</p>'
           f'<ul><li>{CHK}Va por contrato, firmado por los dos.</li><li>{CHK}Cuentan las ventas que entren por la tienda online.</li></ul></section>')

    qt = (f'<section class="c s5 qt" id="vuestras-palabras"><p class="eb">Lo decís vosotras</p>{QM}<blockquote>{E(P["quote"])}</blockquote>'
          f'<cite><i></i>{E(P["quote_src"])}</cite><p>{E(P["quote_why"])}</p><p class="an">{E(P["answer"])}</p></section>')

    def steps(L, cls=''):
        return f'<ol class="{cls}">' + ''.join(f'<li class="{k}"><span>{E(t)}</span></li>' for k, t in L) + '</ol>'
    nv_today = sum(1 for k, _ in P['today'] if k == 'v'); nv_store = sum(1 for k, _ in P['store'] if k == 'v')
    fl = (f'<section class="c s7 fl" id="como"><div class="ch"><h2>Del «me lo guardas» al pedido</h2><small>cada pedido, paso a paso</small></div>'
          f'<div class="cols"><div><h4><em>{len(P["today"])}</em>pasos hoy <span>· {nv_today} pasan por {who}</span></h4>{steps(P["today"])}</div>'
          f'<div><h4><em>{len(P["store"])}</em>con la tienda <span>· {nv_store} pasa por {who}</span></h4>{steps(P["store"], "nw")}</div></div>'
          f'<div class="key"><span><i></i>Lo hace la {E(P.get("client", "clienta"))}</span><span><i class="v"></i>Lo hacéis {who}</span></div>'
          f'<p class="nt">{E(P["store_note"])}</p></section>')

    rows = [('Llamada de arranque', 'Día 0 · 60 minutos', 0, 1, 'Día 0'), ('Fotos y fichas', 'de vuestras prendas', 1, 5, 'Días 1–5'),
            ('Pagos y envíos', 'tarjeta, Bizum, Apple Pay', 4, 5, 'Días 4–8'), ('Dominio y textos legales', 'todo en regla', 7, 4, 'Días 7–10'),
            ('Pruebas y vuestro visto bueno', 'pedidos de prueba', 10, 3, 'Días 10–12'), ('Os enseñamos a usarla', 'subir prendas desde el móvil', 12, 3, 'Días 12–14'),
            ('Abierta', 'a toda España', 15, 1, 'Día 15')]
    pr = ''.join(f'<div class="rw{" k" if i == len(rows) - 1 else ""}"><b>{E(a)}<small>{E(b)}</small></b><div class="tr"><i class="{'ol' if s >= 14 else ('o' if w <= 1 else '')}" style="--a:{s};--w:{w}"><em>{E(lab)}</em></i></div></div>'
                 for i, (a, b, s, w, lab) in enumerate(rows))
    ax = ''.join(f'<span>{n if n in (0, 5, 10, 15) else ""}</span>' for n in range(16))
    pl = (f'<section class="c s8 pl" id="plan"><div class="ch"><h2>Vuestros 15 días</h2><small>lo hacemos nosotros</small></div>'
          f'<div class="gt"><div class="ax">{ax}</div><div class="grid">' + '<span></span>' * 16 + f'</div>{pr}</div></section>')

    arr = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
    nw = (f'<section class="c s4 nw2" id="ahora"><div class="ch"><h2>Por qué ahora</h2></div>'
          f'<div class="dd"><div><small>Empezamos</small><b id="nw-a">el lunes</b><span id="nw-aw"></span></div>{arr}<div class="k"><small>Abierta</small><b id="nw-b">15 días después</b><span id="nw-bw"></span></div></div>'
          f'<p>Si arrancamos el lunes, la tienda está vendiendo antes de <b id="nw-e">la próxima campaña</b>: <span id="nw-d">con margen</span>. Lo que enseñéis en los directos de esas semanas ya tendrá su enlace.</p></section>')

    yo = (f'<section class="c s12 yo" id="trabajo"><div class="ch"><h2>Vuestro trabajo: 3 cosas</h2><small>y ninguna es técnica</small></div><div class="three">'
          '<div><b>1</b><h3>Una llamada de arranque</h3><p>Una hora para conocer vuestra tienda: tallas, marcas, cómo enviáis y qué se vende más.</p></div>'
          '<div><b>2</b><h3>Fotos de lo que entra</h3><p>Nos mandáis por WhatsApp fotos de las prendas, de las del móvil. Con ellas hacemos las fotos de tienda y las fichas.</p></div>'
          '<div><b>3</b><h3>Preparar los paquetes</h3><p>Los pedidos os llegan ya pagados y con la dirección. Como ahora, pero sin perseguir a nadie por mensaje.</p></div></div>'
          f'<div class="rest">{LOGO}<p><b>Todo lo demás lo hacemos nosotros:</b> diseño, fotos, fichas, pagos, envíos, dominio y textos legales.</p></div></section>')

    faqs = [('¿Tenemos que dejar el WhatsApp y los directos?',
             'No. Son vuestra forma de vender y funcionan. La tienda les pone un enlace: lo que enseñáis en el directo ya está en la web con su talla y su precio, y quien prefiera escribiros os sigue escribiendo.'),
            ('¿Cuánto cuesta?',
             'Un precio cerrado, sin sorpresas. Os lo doy en la llamada, con todo lo que incluye por escrito. Y con la garantía: si en 90 días la tienda no os ha devuelto la inversión, seguimos trabajando gratis hasta que lo haga.'),
            ('¿Y si no vende?', 'Para eso está la garantía de 90 días, por contrato. Nuestro trabajo no termina el día que se abre: termina cuando la tienda os ha devuelto lo invertido.'),
            ('¿Quién sube las prendas nuevas?',
             'Vosotras, desde el móvil, en un par de minutos: es como publicar un post. Os lo enseñamos antes de abrir y tenéis guías paso a paso en vuestro portal. Los cambios grandes los hacemos nosotros.'),
            ('¿Y los envíos?', P['ship']),
            ('¿Cuánto tardáis?', 'Quince días desde la llamada de arranque. Ese día empieza a contar y el día 15 la tienda está abierta.')]
    fq = ('<section class="c s7 fq" id="dudas"><div class="ch"><h2>Lo que os estaréis preguntando</h2></div>'
          + ''.join(f'<details name="fq"{" open" if i == 0 else ""}><summary>{E(q)}</summary><p>{E(a)}</p></details>' for i, (q, a) in enumerate(faqs)) + '</section>')

    qs = [('Me interesa: ¿cuándo podemos hablar?', 'Me interesa la tienda. ¿Cuándo podemos hablar?'),
          ('¿Cuánto costaría para nosotras?', '¿Cuánto costaría la tienda para nosotras?'),
          ('Tengo una duda', 'Tengo una duda sobre la tienda: ')]
    qr = (f'<section class="c s5 noir qr" id="hablar"><p class="eb">¿Lo hablamos?</p><h2>Escribidme sin compromiso.<span class="lm">Os contesto yo, Christian.</span></h2>'
          '<p>Tocad una y se abre WhatsApp con el mensaje ya escrito.</p><div class="bt">'
          + ''.join(f'<a href="{wa(hi + m)}" target="_blank" rel="noopener">{WAI}<span>{E(t)}</span>{AR}</a>' for t, m in qs)
          + f'</div><div class="or"><a class="b-pri" href="#agenda">O elegid día y hora{AR}</a></div>'
          '<div class="me"><img src="/christian-hola.jpg" alt="" width="40" height="40" loading="lazy"><span><b>Christian Silva</b>Fundador de 404 Growth</span></div></section>')

    ag = AG.block(slug, name, P.get('sec', 'moda'), False)

    note = ('<section class="w" id="nota"><div class="c nt2 rv"><img src="/christian-hola.jpg" alt="Christian" width="64" height="64" loading="lazy"><div>'
            f'<p>Os he preparado esta tienda con vuestras prendas porque ya vendéis online, solo que a mano: cada MD, cada Bizum, cada «¿me lo guardas?». La tienda no os quita eso. Os quita el trabajo de detrás.</p>'
            f'<p>Si os encaja, lo vemos en 30 minutos y os enseño cómo quedaría con todo vuestro catálogo.</p>'
            '<p class="sg"><b>Christian</b> · 404 Growth</p></div></div></section>')

    foot = (f'<footer><div class="w"><span>404 Growth · Propuesta privada para {E(name)}</span>'
            '<span>Tienda de ejemplo: las fotos están hechas con IA a partir de vuestras publicaciones.</span></div></footer>'
            f'<a class="wa-fab" href="{wa(hi)}" target="_blank" rel="noopener"><img src="/christian-hola.jpg" alt="" width="38" height="38"><span>Escribir a Christian<small>por WhatsApp</small></span></a>')

    body = ('<body>' + nav + '<main>' + hd + '<div class="w"><div class="g">' + kpis + shop + gar + '</div><div class="g">' + qt + fl + '</div><div class="g">' + pl + nw + '</div>'
            + '<div class="g">' + yo + '</div><div class="g">' + fq + qr + '</div></div>' + ag + note + '</main>' + foot)

    cnt = open(os.path.join(D, 'tpl', 'counter.html'), encoding='utf-8').read().replace('var slug="cafe-con-bacon"', f'var slug="{slug}"')
    assert f'var slug="{slug}"' in cnt
    h = head + body + JS + cnt + '</body></html>'
    if local:   # desde file:// no hay raíz: las fotos de Christian y la agenda van al lado
        h = h.replace('src="/christian-hola.jpg"', 'src="christian-hola.jpg"').replace('src="/agenda.js"', 'src="agenda.js"')
    out = os.path.join(OUT, f'p-{slug}.html' if not local else f'p-{slug}--local.html')
    open(out, 'w', encoding='utf-8').write(h)
    print('ok', slug, len(h), out)
    return out


if __name__ == '__main__':
    a = sys.argv[1:]
    loc = '--local' in a
    for s in [x for x in a if not x.startswith('--')]:
        build(s)
        if loc:
            build(s, local=True)
