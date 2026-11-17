"""Lote 37 · tienda de la propuesta con la estructura A «Editorial» (16/11/2026).
Chris la eligió en el lienzo de Claude Design «Tienda de propuesta · 3 estructuras» con dos cambios:
la cabecera sin cristal (transparente sobre la portada y blanca al bajar) y más aire en la sección 2 (Lo nuevo).
uso: L33_AI=<fotos> python3 gen37a.py <slug> [...] [--noimg]  → out/p-<slug>--tienda.html (+ fotos de detalle p1d…p6d)
La propuesta (gen33v.py) no cambia: mete esta tienda en sus marcos con ?tour=1, ?embed=1 y ?embed=1&at=destacado."""
import os, sys, urllib.parse
from PIL import Image
import gen33 as G

E = G.E; ic = G.ic; T = G.T; img = G.img
OUT = G.OUT

# textos de cada nicho (hablan a la clienta: tú). Lo que no cambia sale de G.NICHE.
NA = {
    'moda': dict(chip='Nueva colección · ya en la tienda', sub='Elegido en nuestra tienda de {city}. Ahora, con envío a toda España.',
                 trust=[('truck', 'Envío a toda España'), ('card', 'Bizum'), ('store', 'Recogida en tienda')],
                 new_e='Recién llegado a la tienda', new_h='Lo nuevo de la semana', cat_h='¿Por dónde empezamos?',
                 look_e='Así se lleva', look_h='Ideas para combinar', look_s='Tres prendas de la tienda que van solas. Llévatelas juntas o elige la que te falta.',
                 look_b='Añadir las 3 prendas', best_e='Lo más vendido', best_h='Lo que más nos pedís por Instagram'),
    'joya': dict(chip='Piezas nuevas · ya en la joyería', sub='Elegidas en nuestra joyería de {city}. Ahora, con envío asegurado a toda España.',
                 trust=[('shield', 'Envío asegurado'), ('card', 'Bizum'), ('store', 'Recogida en tienda')],
                 new_e='Recién llegado a la joyería', new_h='Las piezas nuevas', cat_h='¿Qué buscas hoy?',
                 look_e='Para regalar', look_h='Un regalo que no se olvida', look_s='Tres piezas de la joyería para acertar seguro.',
                 look_b='Añadir las 3 piezas', best_e='Las más deseadas', best_h='Lo que más nos pedís por Instagram'),
    'suplementos': dict(chip='Novedades · ya en la tienda', sub='Lo que te recomendamos en {city}, ahora con envío a toda España.',
                        trust=[('truck', 'Envío a toda España'), ('card', 'Bizum'), ('store', 'Recogida en tienda')],
                        new_e='Recién llegado a la tienda', new_h='Lo nuevo en la tienda', cat_h='¿Qué necesitas hoy?',
                        look_e='En un solo pedido', look_h='Tus básicos, juntos', look_s='Tres básicos de la tienda para pedirlos de una vez.',
                        look_b='Añadir los 3', best_e='Lo más vendido', best_h='Lo que más nos pedís en la tienda'),
    'cosmetica': dict(chip='Novedades · ya en la perfumería', sub='Lo que te recomendamos en {city}, ahora con envío a toda España.',
                      trust=[('truck', 'Envío a toda España'), ('card', 'Bizum'), ('store', 'Recogida en tienda')],
                      new_e='Recién llegado', new_h='Lo nuevo de la semana', cat_h='¿Qué te apetece hoy?',
                      look_e='Para regalar', look_h='Ideas para regalar o regalarte', look_s='Tres favoritos de la tienda, en un solo pedido.',
                      look_b='Añadir los 3', best_e='Los favoritos', best_h='Lo que más nos pedís por Instagram'),
}
NA['calzado'] = dict(NA['moda'], look_b='Añadir los 3', new_h='Lo nuevo de la semana')
NA['sneakers'] = NA['calzado']
NA['optica'] = dict(NA['joya'], chip='Monturas nuevas · ya en la óptica', sub='Las monturas de nuestra óptica de {city}, ahora con envío a toda España.',
                    trust=[('truck', 'Envío a toda España'), ('card', 'Bizum'), ('store', 'Ajuste en tienda')], new_e='Recién llegado a la óptica',
                    new_h='Las monturas nuevas', look_e='Para el sol', look_h='Tres monturas para elegir', look_b='Añadir las 3')
# lote 38 (16/11/2026): muebles, sofás, colchones y decoración. Cada tienda puede cambiar estos textos con «na» en su ficha (specs).
NA['deco'] = dict(rev_p='Así se verán las opiniones de vuestros clientes. Estas son de ejemplo.', visit_p='Ven a ver y a probar cada pieza en persona.', chip='Nuevos modelos · ya en la exposición', sub='Elegidos en nuestra tienda de {city}. Ahora, online y con entrega a domicilio.',
                  trust=[('truck', 'Entrega a domicilio'), ('card', 'Bizum'), ('store', 'Exposición en tienda')],
                  new_e='Recién llegado a la exposición', new_h='Lo nuevo en la tienda', cat_h='¿Qué buscas para tu casa?',
                  look_e='Ambiente completo', look_h='Ideas para tu casa', look_s='Tres piezas de la tienda que van juntas. Llévatelas a la vez o elige la que te falta.',
                  look_b='Añadir las 3', best_e='Lo más vendido', best_h='Lo que más nos pedís en la tienda',
                  fdet=[('truck', 'Entrega a domicilio'), ('store', 'Ven a verlo a la tienda de {city}'), ('card', 'Tarjeta, Bizum, Apple Pay o Google Pay')],
                  drp='Entrega a domicilio · Exposición en {city}')

# reseñas de ejemplo (se dice en la página que son de ejemplo): (nombre, ciudad, producto, texto). '*' = la ciudad de la tienda
REV = {
    'moda': [('Lucía', 'Sevilla', 0, 'Lo pedí un domingo por la noche y llegó tal cual se ve en las fotos.'),
             ('Rocío', 'Madrid', 1, 'Os sigo desde hace años en Instagram y por fin puedo comprar sin escribir por privado.'),
             ('Marta', 'Valencia', 2, 'Me ayudaron con la talla por WhatsApp en un momento. Sienta de maravilla.'),
             ('Carmen', '*', 3, 'Lo recogí en la tienda y aproveché para probarme dos cosas más.'),
             ('Ana', 'Málaga', 4, 'Pagué con Bizum en un minuto. Repetiré seguro.'),
             ('Paula', 'Bilbao', 5, 'Aún más bonito en persona. Ya tengo fichado el siguiente.')],
    'joya': [('Lucía', 'Sevilla', 0, 'Llegó en su estuche, perfecto para regalar. Le encantó.'),
             ('Rocío', 'Madrid', 1, 'Os sigo en Instagram y por fin puedo comprar sin escribir por privado.'),
             ('Marta', 'Valencia', 2, 'Me resolvieron todas las dudas por WhatsApp antes de comprar.'),
             ('Carmen', '*', 3, 'La recogí en la joyería y me atendieron de maravilla.'),
             ('Ana', 'Málaga', 4, 'Pagué con Bizum en un minuto y llegó muy bien protegida.'),
             ('Paula', 'Bilbao', 5, 'Brilla aún más en persona. Ya tengo fichada la siguiente.')],
    'suplementos': [('Javier', 'Sevilla', 0, 'Lo pedí el domingo por la noche y me llegó sin complicaciones.'),
                    ('Laura', 'Madrid', 1, 'Me asesoraron por WhatsApp sobre qué me convenía más.'),
                    ('Sergio', 'Valencia', 2, 'Por fin puedo pedir sin escribir por privado.'),
                    ('Carmen', '*', 3, 'Lo recogí en la tienda al salir del gimnasio.'),
                    ('Dani', 'Málaga', 4, 'Pagué con Bizum en un minuto. Repetiré seguro.'),
                    ('Marta', 'Bilbao', 5, 'Mi tienda de confianza, ahora también online.')],
    'cosmetica': [('Lucía', 'Sevilla', 0, 'Lo pedí el domingo por la noche y llegó perfecto.'),
                  ('Rocío', 'Madrid', 1, 'Os sigo en Instagram y por fin puedo comprar sin escribir por privado.'),
                  ('Marta', 'Valencia', 2, 'Me aconsejaron por WhatsApp como si estuviera en la tienda.'),
                  ('Carmen', '*', 3, 'Lo recogí en la tienda y aproveché para probar otro perfume.'),
                  ('Ana', 'Málaga', 4, 'Pagué con Bizum en un minuto. Repetiré seguro.'),
                  ('Paula', 'Bilbao', 5, 'Huele aún mejor en persona. Ya tengo fichado el siguiente.')],
}
for k in ('calzado', 'sneakers'):
    REV[k] = REV['moda']
REV['optica'] = REV['joya']
REV['deco'] = [('Lucía', 'Sevilla', 0, 'Lo elegí desde el móvil un domingo por la noche y a la semana ya lo tenía en casa.'),
               ('Javier', 'Madrid', 1, 'Me pasaron las medidas exactas por WhatsApp antes de comprar. Encaja perfecto.'),
               ('Marta', 'Valencia', 2, 'Igual que en las fotos. La entrega, puntual y con mucho cuidado.'),
               ('Carmen', '*', 3, 'Fui a probarlo a la tienda y terminé de pedirlo online desde casa.'),
               ('Ana', 'Málaga', 4, 'Pagué con Bizum en un minuto. Repetiremos para el dormitorio.'),
               ('Pablo', 'Bilbao', 5, 'Se nota la calidad. Ya tenemos fichada la pieza a juego.')]
import niches39 as _n39   # lote 39
NA.update(_n39.NA); REV.update(_n39.REV)

FDET = [('truck', 'Envío a toda España'), ('store', 'Recogida gratis en la tienda de {city}'), ('card', 'Tarjeta, Bizum, Apple Pay o Google Pay')]
STAR = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3.5l2.6 5.3 5.9.9-4.3 4.1 1 5.8-5.2-2.8-5.2 2.8 1-5.8-4.3-4.1 5.9-.9z"/></svg>'

CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{font-family:var(--f);color:#141010;background:#fff;-webkit-font-smoothing:antialiased;letter-spacing:-.01em;overflow-x:hidden}
img{display:block;max-width:100%}a{color:inherit;text-decoration:none}button,input{font:inherit;color:inherit}button{cursor:pointer;background:none;border:0}
.w{max-width:1360px;margin:0 auto;padding:0 40px}
.ic{flex:none}
/* cristal (solo donde hay foto detrás) */
.gl,.glw,.gk,.gd,.ga{position:relative;isolation:isolate;overflow:hidden}
.gl::before,.glw::before,.gk::before,.gd::before,.ga::before{content:"";position:absolute;inset:0;border-radius:inherit;pointer-events:none;z-index:-1;background:radial-gradient(120% 75% at 22% -12%,rgba(255,255,255,.6),rgba(255,255,255,0) 58%)}
.gl{color:#fff;background:linear-gradient(140deg,rgba(255,255,255,.28),rgba(255,255,255,.07) 58%,rgba(255,255,255,.13));-webkit-backdrop-filter:blur(18px) saturate(170%);backdrop-filter:blur(18px) saturate(170%);border:1px solid rgba(255,255,255,.34);box-shadow:inset 0 1px 0 rgba(255,255,255,.7),inset 0 -1px 0 rgba(255,255,255,.12),0 10px 30px rgba(0,0,0,.22)}
.gk{color:#fff;background:linear-gradient(140deg,rgba(28,20,18,.62),rgba(28,20,18,.36));-webkit-backdrop-filter:blur(22px) saturate(160%);backdrop-filter:blur(22px) saturate(160%);border:1px solid rgba(255,255,255,.22);box-shadow:inset 0 1px 0 rgba(255,255,255,.35),0 18px 44px rgba(0,0,0,.28)}
.gk::before{opacity:.35}
.glw{color:#141010;background:linear-gradient(180deg,rgba(255,255,255,.97),rgba(255,255,255,.82));border:1px solid rgba(255,255,255,.95);box-shadow:inset 0 1px 0 #fff,inset 0 -3px 8px rgba(0,0,0,.06),0 14px 34px rgba(0,0,0,.30),0 2px 6px rgba(0,0,0,.16)}
.gd{color:#fff;background:linear-gradient(180deg,#3b2f2f 0%,#181314 55%,#0e0b0b 100%);border:1px solid rgba(255,255,255,.10);box-shadow:inset 0 1px 0 rgba(255,255,255,.30),inset 0 -2px 6px rgba(0,0,0,.35),0 14px 30px -8px rgba(20,16,16,.5),0 2px 4px rgba(20,16,16,.18)}
.gd::before{opacity:.45}
.ga{color:#fff;background:linear-gradient(180deg,color-mix(in srgb,var(--ac) 70%,#fff) 0%,var(--ac) 52%,color-mix(in srgb,var(--ac) 78%,#000) 100%);border:1px solid rgba(255,255,255,.18);box-shadow:inset 0 1px 0 rgba(255,255,255,.4),inset 0 -2px 6px rgba(0,0,0,.25),0 14px 30px -8px color-mix(in srgb,var(--ac) 70%,transparent),0 2px 4px rgba(20,16,16,.18)}
.gw{color:#141010;background:linear-gradient(180deg,#fff,#f6f3f1);border:1px solid #e8e2de;box-shadow:inset 0 1px 0 #fff,0 1px 2px rgba(20,16,16,.05),0 10px 24px -14px rgba(20,16,16,.3)}
.bt{display:inline-flex;align-items:center;justify-content:center;gap:8px;height:54px;padding:0 26px;border-radius:999px;font-size:15.5px;font-weight:600;letter-spacing:-.01em;white-space:nowrap;transition:transform .25s cubic-bezier(.2,.8,.2,1)}
.bt:hover{transform:translateY(-2px)}.bt:active{transform:scale(.97)}
.ey{display:block;font-size:12.5px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:#6f6765}
.h2{font-size:44px;line-height:1.03;font-weight:700;letter-spacing:-.04em;margin-top:8px;text-wrap:balance}
.sub{margin-top:10px;font-size:17px;line-height:1.5;color:#6f6765}
.sx{padding:96px 0}.bl{border-top:1px solid #f1ece8}
.rv{opacity:0;transform:translateY(18px);transition:opacity .9s cubic-bezier(.2,.8,.2,1),transform .9s cubic-bezier(.2,.8,.2,1)}.rv.in{opacity:1;transform:none}
/* cabecera: sin cristal. Transparente sobre la portada y blanca al bajar */
.hd{position:absolute;top:0;left:0;right:0;z-index:40;color:#fff;transition:background .3s,color .3s,box-shadow .3s}
.hd.sc{position:fixed;background:#fff;color:#141010;box-shadow:0 1px 0 rgba(20,16,16,.08),0 10px 30px -18px rgba(20,16,16,.3)}
.hdi{height:78px;display:flex;align-items:center;gap:28px}
.hd .lg{margin-right:auto;display:flex;align-items:center}
.lgt{font-size:calc(17px * var(--lfs));font-weight:var(--lfw);letter-spacing:max(var(--lls),.22em);text-transform:uppercase;white-space:nowrap;display:flex;flex-direction:column;line-height:1}
.lgt small{font-size:9px;letter-spacing:.3em;font-weight:500;margin-top:5px;opacity:.75}
.lgi{height:34px;width:auto;max-width:170px;object-fit:contain}
.hd:not(.sc) .lgi,.fo .lgi{filter:brightness(0) invert(1)}
.nv{display:flex;gap:4px}.nv a{font-size:14.5px;font-weight:600;padding:8px 12px;border-radius:99px;opacity:.92;transition:background .2s,opacity .2s}
.nv a:hover{opacity:1;background:rgba(255,255,255,.14)}.hd.sc .nv a:hover{background:#f4f0ed}
.ia{display:flex;align-items:center;gap:2px;margin-left:auto}.ia button{width:44px;height:44px;border-radius:99px;display:inline-flex;align-items:center;justify-content:center;position:relative}
.bq{position:absolute;right:2px;top:3px;min-width:18px;height:18px;padding:0 5px;border-radius:99px;background:#fff;color:#141010;font-size:10.5px;font-weight:700;display:none;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,.3)}
.hd.sc .bq{background:#141010;color:#fff}.bq.on{display:flex}
.mb{display:none!important}
/* portada */
.hero{position:relative;height:min(100vh,900px);min-height:640px;overflow:hidden;background:#120d0b;color:#fff}
.emb .hero{height:760px;min-height:0}
.hero picture,.hero .hi{position:absolute;inset:0;width:100%;height:100%}
.hero .hi{object-fit:cover;object-position:var(--hp);animation:kb 2s cubic-bezier(.2,.8,.2,1) both}
.hg{position:absolute;inset:0;background:linear-gradient(90deg,rgba(12,8,7,.8) 0%,rgba(12,8,7,.42) 38%,rgba(12,8,7,0) 64%),linear-gradient(180deg,rgba(12,8,7,.5) 0%,rgba(12,8,7,0) 18%,rgba(12,8,7,0) 70%,rgba(12,8,7,.5) 100%)}
.hc{position:absolute;left:0;right:0;bottom:72px}
.hci{max-width:660px;display:flex;flex-direction:column;align-items:flex-start;gap:18px}
.chip{height:34px;padding:0 14px;border-radius:999px;display:inline-flex;align-items:center;gap:8px;font-size:13.5px;font-weight:600}
.chip i{width:7px;height:7px;border-radius:9px;background:#9be15d;box-shadow:0 0 10px #9be15d}
.hero h1{font-size:clamp(52px,5.6vw,82px);line-height:.95;font-weight:800;letter-spacing:-.05em;text-wrap:balance}
.hero p{font-size:19px;line-height:1.45;color:rgba(255,255,255,.85);max-width:500px}
.hb{display:flex;gap:12px;flex-wrap:wrap;margin-top:4px}.hb .bt{height:58px;padding:0 30px}
.htr{display:flex;gap:26px;flex-wrap:wrap;font-size:13.5px;font-weight:500;color:rgba(255,255,255,.78)}.htr span{display:inline-flex;align-items:center;gap:6px}
.hf{position:absolute;right:max(40px,calc((100vw - 1280px) / 2));bottom:72px;width:268px;border-radius:24px;padding:10px;display:flex;gap:12px;align-items:center}
.hf img{width:64px;height:84px;border-radius:15px;object-fit:cover}
.hf b{display:block;font-size:14.5px;letter-spacing:-.015em}.hf small{display:block;font-size:13px;opacity:.85;margin-top:2px}
.hf button{margin-top:8px;height:32px;padding:0 13px;border-radius:99px;font-size:12.5px;font-weight:600}
.r1{animation:up 1s cubic-bezier(.2,.8,.2,1) both}.r2{animation-delay:.08s}.r3{animation-delay:.16s}.r4{animation-delay:.24s}.r5{animation-delay:.34s}
@keyframes up{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:none}}
@keyframes kb{from{transform:scale(1.06)}to{transform:scale(1)}}
/* pestañas */
.tabs{border-bottom:1px solid #efeae6;background:#fff}
.tbi{display:flex;justify-content:center;gap:40px;overflow-x:auto;scrollbar-width:none}.tbi::-webkit-scrollbar{display:none}
.tb{padding:21px 0 18px;border-bottom:2px solid transparent;font-size:15px;font-weight:600;color:#8a817e;white-space:nowrap;transition:color .2s,border-color .2s}
.tb:hover{color:#141010}.tb.on{color:#141010;border-color:#141010}
/* sección 2: lo nuevo (más aire y los bordes alineados con el resto) */
.nw{padding:88px 0 80px}
.shd{display:flex;align-items:flex-end;justify-content:space-between;gap:20px;margin-bottom:34px}
.ar{display:flex;gap:10px;align-items:center}.ar a{font-size:15px;font-weight:600;margin-right:10px;display:inline-flex;align-items:center;gap:4px;white-space:nowrap}
.ar button{width:46px;height:46px;border-radius:99px;display:inline-flex;align-items:center;justify-content:center}
.car{display:flex;gap:24px;overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none;padding:8px max(40px,calc((100vw - 1280px) / 2)) 26px;scroll-padding-left:max(40px,calc((100vw - 1280px) / 2))}
.car::-webkit-scrollbar{display:none}.car>*{flex:none;scroll-snap-align:start}
.car::after{content:"";flex:0 0 calc(max(40px,calc((100vw - 1280px) / 2)) - 24px)}
.car .pc{width:292px}
.pg{height:3px;border-radius:3px;background:#efeae6;overflow:hidden;margin-top:6px}.pg i{display:block;height:100%;width:30%;background:#141010;border-radius:3px;transition:transform .2s}
/* tarjeta de producto */
.pc{position:relative}
.pim{position:relative;aspect-ratio:3/4;border-radius:20px;overflow:hidden;background:#f3efeb;box-shadow:0 1px 2px rgba(20,16,16,.05),0 14px 30px -12px rgba(20,16,16,.22);transition:transform .5s cubic-bezier(.2,.8,.2,1),box-shadow .5s}
.pc:hover .pim{transform:translateY(-6px);box-shadow:0 2px 4px rgba(20,16,16,.06),0 34px 56px -18px rgba(20,16,16,.34)}
.pim img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.pim .i2{opacity:0;transition:opacity .5s}.pc:hover .i2{opacity:1}
.tg{position:absolute;left:12px;top:12px;height:28px;padding:0 11px;border-radius:999px;font-size:12px;font-weight:600;display:inline-flex;align-items:center;background:rgba(255,255,255,.92);box-shadow:inset 0 1px 0 #fff,0 6px 16px rgba(20,16,16,.14)}
.hr{position:absolute;right:12px;top:12px;width:40px;height:40px;border-radius:99px;display:flex;align-items:center;justify-content:center;background:linear-gradient(180deg,rgba(255,255,255,.95),rgba(255,255,255,.78));box-shadow:inset 0 1px 0 #fff,0 6px 16px rgba(20,16,16,.16);transition:transform .25s}
.hr:active{transform:scale(.9)}.hr.on{color:var(--ac)}.hr.on svg{fill:currentColor}
.qa{position:absolute;left:12px;right:12px;bottom:12px;height:46px;border-radius:99px;display:flex;align-items:center;justify-content:center;gap:7px;font-size:14.5px;font-weight:600;background:linear-gradient(180deg,rgba(255,255,255,.96),rgba(255,255,255,.8));box-shadow:inset 0 1px 0 #fff,0 10px 24px rgba(20,16,16,.18);opacity:0;transform:translateY(8px);transition:opacity .35s,transform .35s cubic-bezier(.2,.8,.2,1)}
.pc:hover .qa,.qa.ok{opacity:1;transform:none}.qa.ok{background:#141010;color:#fff}
.pm{padding:14px 2px 0}.pm b{display:block;font-size:16px;font-weight:600;letter-spacing:-.015em;line-height:1.25}.pm span{display:block;font-size:14.5px;color:#6f6765;margin-top:3px}
/* categorías */
.cg{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px;margin-top:30px}
.tile{position:relative;display:block;border-radius:26px;overflow:hidden;background:#eee;box-shadow:0 1px 2px rgba(20,16,16,.05),0 26px 50px -24px rgba(20,16,16,.4)}
.tile img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform 1.1s cubic-bezier(.2,.8,.2,1)}
.tile:hover img{transform:scale(1.04)}
.cg .tile{height:540px}
.shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(12,8,7,0) 50%,rgba(12,8,7,.6) 100%)}
.tlb{position:absolute;left:24px;right:24px;bottom:24px;display:flex;align-items:flex-end;justify-content:space-between;color:#fff;gap:12px}
.tlb b{font-size:30px;letter-spacing:-.035em;line-height:1.05}
.tlb span{width:48px;height:48px;border-radius:99px;display:inline-flex;align-items:center;justify-content:center;flex:none}
/* ficha */
.ft{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:64px;align-items:start}
.fgal{display:flex;gap:14px}
.fth{display:flex;flex-direction:column;gap:12px}
.fth button{width:84px;height:112px;border-radius:16px;padding:3px;background:#fff;border:1px solid #ebe5e1;box-shadow:0 8px 18px -12px rgba(20,16,16,.4)}
.fth button.on{outline:2px solid #141010;outline-offset:2px}
.fth img{width:100%;height:100%;object-fit:cover;border-radius:13px}
.fmain{flex:1;aspect-ratio:4/5}
.fi h2{margin-top:10px}
.fpr{display:flex;justify-content:space-between;align-items:baseline;margin-top:24px;padding-top:22px;border-top:1px solid #f1ece8}.fpr b{font-size:24px;letter-spacing:-.03em}.fpr small{font-size:14px;color:#6f6765}
.fol{display:flex;justify-content:space-between;align-items:center;margin-top:22px;font-size:15px;font-weight:600}.fol a{font-size:14px;font-weight:500;color:#6f6765;text-decoration:underline}
.os{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}
.os button{min-width:60px;height:48px;padding:0 16px;border-radius:15px;border:1px solid #e3ddd9;background:#fff;font-size:15px;font-weight:600;box-shadow:0 1px 2px rgba(20,16,16,.05)}
.os button.on{color:#fff;border-color:transparent;background:linear-gradient(180deg,#3b2f2f,#141010);box-shadow:inset 0 1px 0 rgba(255,255,255,.25),0 10px 20px -10px rgba(20,16,16,.6)}
.fadd{width:100%;height:60px;margin-top:24px;font-size:16.5px}
.fwa{display:flex;justify-content:center;align-items:center;gap:7px;margin-top:14px;font-size:15px;font-weight:600}
.fdet{margin-top:24px;border-radius:22px;border:1px solid #efe9e5;padding:4px 20px;box-shadow:0 18px 36px -26px rgba(20,16,16,.35)}
.fdet div{display:flex;align-items:center;gap:14px;padding:15px 0;font-size:15px}.fdet div+div{border-top:1px solid #f3eeea}.fdet svg{color:var(--ac)}
/* así se lleva */
.lk{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);gap:64px;align-items:center}
.lk .tile{height:680px}
.lr{display:flex;align-items:center;gap:16px;padding:16px 0;border-bottom:1px solid #f1ece8}
.lr .n{width:24px;font-size:14px;font-weight:700;color:#8a817e}
.lr img{width:70px;height:92px;border-radius:14px;object-fit:cover;box-shadow:0 10px 20px -10px rgba(20,16,16,.4)}
.lr div{flex:1;min-width:0}.lr b{display:block;font-size:16.5px;font-weight:600}.lr small{display:block;font-size:14.5px;color:#6f6765;margin-top:2px}
.lr button{width:46px;height:46px;border-radius:99px;display:inline-flex;align-items:center;justify-content:center;flex:none}
.lr button.ok{background:#141010;color:#fff}
.lkb{margin-top:26px;height:58px;padding:0 34px}
/* lo más vendido */
.bg4{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:40px 24px}
/* reseñas */
.rvh{display:flex;align-items:flex-end;justify-content:space-between;gap:24px;flex-wrap:wrap;margin-bottom:36px}
.rsc{display:flex;align-items:center;gap:16px}.rsc>b{font-size:66px;font-weight:800;letter-spacing:-.05em;line-height:.85}
.st{display:inline-flex;gap:2px}.st svg{width:16px;height:16px;fill:currentColor}
.rsc p{font-size:13.5px;color:#6f6765;margin-top:5px;max-width:270px;line-height:1.4}
.rg{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px}
.rc{border-radius:22px;padding:24px;background:#fff;border:1px solid #efe9e5;box-shadow:0 1px 2px rgba(20,16,16,.04),0 18px 36px -20px rgba(20,16,16,.24);display:flex;flex-direction:column;gap:14px;transition:transform .4s cubic-bezier(.2,.8,.2,1)}
.rc:hover{transform:translateY(-4px)}
.rct{display:flex;justify-content:space-between;align-items:center}.rct .st{color:var(--ac)}
.ej{font-size:11.5px;font-weight:600;color:#6f6765;border:1px solid #e6e0dc;border-radius:99px;padding:3px 9px}
.rc q{font-size:17px;line-height:1.45;letter-spacing:-.012em;quotes:"«" "»"}
.rc figcaption{display:flex;align-items:center;gap:12px;margin-top:auto}
.rc figcaption img{width:44px;height:56px;border-radius:11px;object-fit:cover}
.rc figcaption span{font-size:14px;line-height:1.3}.rc figcaption small{display:block;color:#6f6765;font-size:13.5px}
/* la tienda */
.vs .tile{height:620px}
.vc{position:absolute;left:32px;bottom:32px;width:min(470px,calc(100% - 64px));border-radius:26px;padding:30px}
.vc .ey{color:rgba(255,255,255,.78)}.vc h3{font-size:38px;font-weight:700;letter-spacing:-.04em;line-height:1.02;margin-top:6px}
.vc p{margin:10px 0 20px;font-size:16px;line-height:1.5;color:rgba(255,255,255,.9)}.vc .hb .bt{height:52px;padding:0 24px}
/* instagram */
.igh{display:flex;align-items:center;gap:16px;margin-bottom:24px}
.igr{width:60px;height:60px;border-radius:99px;padding:3px;background:conic-gradient(from 200deg,#f2c27d,#e0566e,#8b2bb9,#e0566e,#f2c27d);flex:none}
.igr img{width:100%;height:100%;border-radius:99px;object-fit:cover;border:3px solid #fff}
.igh div{flex:1;min-width:0}.igh b{font-size:20px;letter-spacing:-.02em}.igh small{display:block;font-size:14.5px;color:#6f6765}
.igg{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:8px;border-radius:22px;overflow:hidden}.igg img{width:100%;aspect-ratio:1;object-fit:cover}
/* club */
.clb{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:30px}
.clb h2{font-size:36px}
.clb form{display:flex;gap:10px;flex:0 1 520px;min-width:0}
.clb input{flex:1;min-width:0;width:0;height:56px;border-radius:999px;border:1px solid #e6e0dc;padding:0 20px;font-size:15.5px;background:#faf8f6;box-shadow:inset 0 1px 2px rgba(20,16,16,.06)}
/* pie */
.fo{background:#110d0c;color:#fff;padding:72px 0 40px}
.fog{display:grid;grid-template-columns:1.3fr 1fr 1fr 1.3fr;gap:30px}
.fo p{font-size:14.5px;line-height:1.6;color:rgba(255,255,255,.66);margin-top:10px}
.fo h4{font-size:12px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:rgba(255,255,255,.5);margin-bottom:10px}
.fo nav a{display:block;font-size:15px;line-height:2.05;color:rgba(255,255,255,.74)}.fo nav a:hover{color:#fff}
.pay{display:flex;flex-wrap:wrap;gap:8px}.pay span{height:32px;padding:0 12px;border-radius:99px;display:inline-flex;align-items:center;font-size:12.5px;font-weight:600}
.fox{height:1px;background:rgba(255,255,255,.12);margin:44px 0 20px}
.fo .cp{font-size:13px;color:rgba(255,255,255,.55);margin:0}
/* cesta */
.ov{position:fixed;inset:0;background:rgba(12,8,7,.45);opacity:0;pointer-events:none;transition:opacity .3s;z-index:60}.ov.on{opacity:1;pointer-events:auto}
.dr{position:fixed;top:0;right:0;bottom:0;width:min(420px,100%);background:#fff;z-index:61;transform:translateX(100%);transition:transform .45s cubic-bezier(.2,.8,.2,1);display:flex;flex-direction:column;box-shadow:-30px 0 60px -20px rgba(0,0,0,.35)}
.dr.on{transform:none}
.dh{display:flex;justify-content:space-between;align-items:center;padding:22px 24px;border-bottom:1px solid #f1ece8}.dh b{font-size:19px;letter-spacing:-.02em}
.dh button{width:42px;height:42px;border-radius:99px;display:flex;align-items:center;justify-content:center;background:#f5f1ee}
.dl{flex:1;overflow:auto;padding:12px 24px}.de{color:#6f6765;font-size:15px;padding:30px 0}
.di{display:flex;gap:14px;align-items:center;padding:12px 0;border-bottom:1px solid #f4efec}.di img{width:64px;height:84px;border-radius:12px;object-fit:cover}
.di div{flex:1;min-width:0}.di b{display:block;font-size:15px}.di small{color:#6f6765;font-size:13.5px}
.di button{width:34px;height:34px;border-radius:99px;display:flex;align-items:center;justify-content:center;color:#8a817e}
.df{padding:18px 24px 26px;border-top:1px solid #f1ece8}.df .bt{width:100%}.df p{font-size:13px;color:#6f6765;text-align:center;margin-top:12px}
.tz{position:fixed;left:50%;bottom:28px;transform:translate(-50%,20px);opacity:0;pointer-events:none;z-index:70;background:#141010;color:#fff;font-size:14px;font-weight:500;padding:13px 18px;border-radius:16px;box-shadow:0 18px 40px rgba(0,0,0,.3);transition:opacity .3s,transform .3s;max-width:calc(100% - 32px);text-align:center}
.tz.on{opacity:1;transform:translate(-50%,0)}
/* ---------- móvil ---------- */
@media (max-width:760px){
.w{padding:0 20px}
.sx{padding:56px 0}
.h2{font-size:29px;letter-spacing:-.035em;margin-top:6px}
.sub{font-size:15px}
.hdi{height:62px;gap:0;display:grid;grid-template-columns:44px 1fr 88px}
.hd .lg{margin:0;justify-content:center}
.hd .lgt{font-size:calc(14px * var(--lfs));align-items:center;text-align:center}
.lgi{height:28px;max-width:150px}
.nv{display:none}.mb{display:inline-flex!important;width:44px;height:44px;align-items:center;justify-content:center;margin-left:-10px}
.ia{justify-content:flex-end;margin-right:-10px}.ia .hs2{display:none}
.hero{height:100svh;min-height:620px;max-height:900px}
.emb .hero{height:812px;max-height:none}
.hero .hi{object-position:var(--hpm)}
.hg{background:linear-gradient(180deg,rgba(12,8,7,.5) 0%,rgba(12,8,7,0) 18%,rgba(12,8,7,0) 40%,rgba(12,8,7,.72) 68%,rgba(12,8,7,.95) 100%)}
.hc{bottom:26px}
.hci{gap:14px}
.chip{height:30px;padding:0 12px;font-size:12.5px}
.hero h1{font-size:42px;line-height:.98;letter-spacing:-.048em}
.hero p{font-size:15.5px}
.hb{width:100%;gap:10px}.hb .bt{flex:1;height:52px;padding:0 14px;font-size:15px}
.htr{width:100%;justify-content:space-between;gap:6px;font-size:12px;flex-wrap:nowrap}.htr span{white-space:nowrap;gap:5px}.htr svg{width:15px;height:15px}
.hf{display:none}
.tbi{justify-content:flex-start;gap:24px}.tb{padding:17px 0 14px}
.nw{padding:48px 0 44px}
.shd{margin-bottom:22px;align-items:flex-end}
.ar button{display:none}.ar a{margin:0 0 3px;font-size:14px}
.car{gap:14px;padding:6px 20px 22px;scroll-padding-left:20px}
.car::after{flex:0 0 6px}
.car .pc{width:min(58vw,232px)}
.pim{border-radius:18px}
.qa{left:auto;right:10px;bottom:10px;width:42px;height:42px;padding:0;opacity:1;transform:none}.qa span{display:none}
.qa.ok{width:auto;padding:0 14px}
.hr{right:10px;top:10px;width:36px;height:36px}.tg{left:10px;top:10px;height:26px;font-size:11.5px;padding:0 10px}
.pm b{font-size:15px}.pm span{font-size:14px}
.cg{grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin-top:20px}
.cg .tile{height:270px;border-radius:22px}.cg .tile:nth-child(3){grid-column:span 2;height:200px}
.tlb{left:14px;right:14px;bottom:14px}.tlb b{font-size:20px}.tlb span{width:38px;height:38px}
.ft{grid-template-columns:1fr;gap:20px}
.fgal{flex-direction:column-reverse;gap:10px}
.fth{flex-direction:row}.fth button{width:64px;height:84px;border-radius:14px}.fth img{border-radius:11px}
.fmain{flex:none;width:100%;border-radius:24px;aspect-ratio:4/5}
.fpr{margin-top:16px;padding-top:16px}.fpr b{font-size:20px}
.os button{min-width:0;flex:1;height:46px;padding:0 6px;border-radius:14px;font-size:14.5px}
.fadd{height:56px;margin-top:18px;font-size:16px}
.fdet{margin-top:20px;padding:2px 16px}.fdet div{font-size:14px;padding:13px 0}
.lk{grid-template-columns:1fr;gap:18px}.lk .tile{height:440px;order:2}.lk>div:last-child{order:1;display:contents}
.lkt{order:1}.lkl{order:3}.lkb{order:4;width:100%;margin-top:6px;height:54px}
.lr{gap:12px;padding:12px 0}.lr img{width:54px;height:70px;border-radius:12px}.lr b{font-size:15px}.lr small{font-size:13.5px}.lr button{width:44px;height:44px}
.bg4{grid-template-columns:repeat(2,minmax(0,1fr));gap:24px 12px}
.rvh{margin-bottom:20px}.rsc>b{font-size:56px}
.rg{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;gap:12px;margin:0 -20px;padding:4px 20px 12px;scrollbar-width:none}.rg::-webkit-scrollbar{display:none}
.rg::after{content:"";flex:0 0 8px}
.rc{flex:none;width:276px;scroll-snap-align:start;padding:18px;gap:12px}.rc q{font-size:15px}
.vs .tile{height:470px}.vc{left:12px;right:12px;bottom:12px;width:auto;padding:18px;border-radius:22px}.vc h3{font-size:26px}.vc p{font-size:14px;margin:6px 0 14px}
.vc .hb .bt{height:46px;font-size:14.5px}
.igh{margin-bottom:16px}.igr{width:52px;height:52px}.igh b{font-size:16px}.igh small{font-size:13.5px}.igh .bt{height:40px;padding:0 16px;font-size:14px}
.igg{grid-template-columns:repeat(3,minmax(0,1fr));gap:4px;border-radius:18px}
.clb{gap:16px}.clb h2{font-size:25px}.clb form{flex:1 1 100%}.clb input{height:52px;font-size:15px}.clb .bt{height:52px;padding:0 20px}
.fo{padding:44px 0 30px}.fog{grid-template-columns:repeat(2,minmax(0,1fr));gap:26px 16px}.fog>div:first-child,.fog>div:last-child{grid-column:span 2}
.fox{margin:28px 0 18px}
}
@media (max-width:374px){.htr{font-size:11px}.htr svg{width:13px;height:13px}.hero h1{font-size:38px}}
@media (hover:none){.qa{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){.hero .hi,.r1{animation:none}.rv{opacity:1;transform:none;transition:none}html{scroll-behavior:auto}}
"""

JS = r"""
(function(){var d=document,q=function(s,e){return (e||d).querySelector(s)},qa=function(s,e){return [].slice.call((e||d).querySelectorAll(s))};
/* cabecera: blanca al bajar */var hd=q('.hd'),hh=q('.hero');function hs(){hd.classList.toggle('sc',scrollY>(hh?hh.offsetHeight-90:60))}addEventListener('scroll',hs,{passive:true});hs();
/* pestañas: llevan a la prenda en el carrusel */var car=q('.car'),pg=q('.pg i');
qa('.tb').forEach(function(b){b.addEventListener('click',function(){qa('.tb').forEach(function(x){x.classList.toggle('on',x===b)});var el=q('.car [data-id="'+b.dataset.go+'"]');if(el&&car){car.scrollTo({left:el.offsetLeft-car.offsetLeft-parseFloat(getComputedStyle(car).scrollPaddingLeft||0),behavior:'smooth'})}})});
function pr(){if(!car||!pg)return;var m=car.scrollWidth-car.clientWidth,f=car.clientWidth/car.scrollWidth;pg.style.width=(f*100)+'%';pg.style.transform='translateX('+(m>0?car.scrollLeft/m*(1/f-1)*100:0)+'%)'}if(car){car.addEventListener('scroll',pr,{passive:true});addEventListener('resize',pr);pr()}
qa('[data-dir]').forEach(function(b){b.addEventListener('click',function(){car.scrollBy({left:(+b.dataset.dir)*car.clientWidth*.8,behavior:'smooth'})})});
/* ficha: fotos */qa('.fth button').forEach(function(b){b.addEventListener('click',function(){qa('.fth button').forEach(function(x){x.classList.toggle('on',x===b)});q('.fmain img').src=b.dataset.src})});
/* el look: añadir las 3 */var lb=q('[data-look]');if(lb)lb.addEventListener('click',function(){qa('.lr [data-add]').forEach(function(b){b.click()})});
})();
"""


def detail(c):
    """foto de detalle de cada producto (para el paso del ratón): un recorte centrado y más cerca"""
    s = c['slug']; src = os.path.join(G.AI, s)
    for k in range(1, 7):
        f = os.path.join(src, f'p{k}.jpg')
        if not os.path.exists(f):
            continue
        im = Image.open(f).convert('RGB'); W, H = im.size
        cw = int(W * .64); ch = int(cw * 4 / 3)
        x0 = (W - cw) // 2; y0 = max(0, min(H - ch, int(H * .42 - ch / 2)))
        im = im.crop((x0, y0, x0 + cw, y0 + ch))
        if im.width > 900:
            im = im.resize((900, round(im.height * 900 / im.width)), Image.LANCZOS)
        im.save(os.path.join(OUT, f'p-{s}--b--p{k}d.jpg'), 'JPEG', quality=84, optimize=True, progressive=True)


def store(c):
    N = G.NICHE[c['niche']]; A = dict(NA[c['niche']], **(c.get('na') or {})); nm = E(c['name']); P = c['prods']; city = c['city']; s = c['slug']
    acc = (c.get('theme') or {}).get('acc') or N['acc']
    root = (':root{--f:%s;--ac:%s;--hp:%s;--hpm:%s}' % (G.FONT, acc, c.get('hp', 'center'), c.get('hpm', 'center')))
    cats = c['cats']; cn = [n for n, _ in cats]
    h1 = c.get('h1') or G.HX.get(s) or (E(cn[0]) + ', ' + E(cn[1].lower()) + '<br>y ' + E(cn[2].lower()) + '.')
    items = N['items']; opts = c.get('opts') or N['opts']; od = opts[min(2, len(opts) - 1)]
    pr = 'Vuestro precio'

    def add(p, cls='', inner=''):
        return (f'<button class="{cls}" data-add data-n="{E(p["name"])}" data-i="{img(c, p["id"])}" data-p="{pr}" data-o="{E(p.get("opt", od))}"'
                f' aria-label="Añadir {E(p["name"])} a la cesta">{inner}</button>')

    def card(p, tag=''):
        return (f'<article class="pc" data-id="{p["id"]}"><div class="pim"><img src="{img(c, p["id"])}" alt="{E(p["name"])}" loading="lazy">'
                f'<img class="i2" src="{img(c, p["id"] + "d")}" alt="" loading="lazy">'
                + (f'<span class="tg">{E(tag)}</span>' if tag else '')
                + f'<button class="hr" aria-label="Guardar {E(p["name"])}">{ic("heart", 18)}</button>'
                + add(p, 'qa', ic('plus', 18, 2) + '<span>Añadir a la cesta</span>')
                + f'</div><div class="pm"><b>{E(p["name"])}</b><span>{pr}</span></div></article>')

    o = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
         f'<meta name="robots" content="noindex,nofollow"><title>{nm} · Tienda online (ejemplo)</title><meta name="theme-color" content="#120d0b">'
         f'<link rel="preload" as="image" href="{img(c, "hm")}" media="(max-width:760px)"><link rel="preload" as="image" href="{img(c, "hd")}" media="(min-width:761px)">'
         f'<style>{root}{CSS}</style></head><body>')
    # cabecera (sin cristal)
    o += (f'<header class="hd"><div class="w hdi"><button class="mb" aria-label="Menú" data-demo>{ic("menu", 22)}</button>'
          f'<a class="lg" href="#" data-demo>{G.logo(c)}</a>'
          '<nav class="nv" aria-label="Principal"><a href="#nuevo">Novedades</a>' + ''.join(f'<a href="#cat">{E(n)}</a>' for n in cn) + '<a href="#visita">La tienda</a></nav>'
          f'<div class="ia"><button class="hs2" aria-label="Buscar" data-demo>{ic("search")}</button><button class="hs2" aria-label="Favoritos" data-demo>{ic("heart")}</button>'
          f'<button aria-label="Cesta" data-bag>{ic("bag", 22)}<span class="bq">0</span></button></div></div></header>')
    # portada
    p0 = P[0]
    o += (f'<section class="hero"><picture><source media="(max-width:760px)" srcset="{img(c, "hm")}"><img class="hi" src="{img(c, "hd")}" alt="{nm}" fetchpriority="high"></picture>'
          '<div class="hg"></div><div class="hc"><div class="w"><div class="hci">'
          f'<span class="chip gl r1"><i></i>{E(A["chip"])}</span><h1 class="r1 r2">{h1}</h1><p class="r1 r3">{E(T(A["sub"], c))}</p>'
          f'<div class="hb r1 r4"><a class="bt glw" href="#nuevo">Comprar ahora</a><a class="bt gl" href="#nuevo">Ver novedades</a></div>'
          '<div class="htr r1 r5">' + ''.join(f'<span>{ic(i, 16)}{E(t)}</span>' for i, t in A['trust']) + '</div></div></div></div>'
          f'<div class="hf gl r1 r5"><img src="{img(c, p0["id"])}" alt=""><div><b>{E(p0["name"])}</b><small>{pr}</small>'
          + add(p0, 'glw', 'Añadir') + '</div></div></section>')
    # pestañas
    o += ('<nav class="tabs" aria-label="Categorías"><div class="w tbi"><button class="tb on" data-go="' + P[0]['id'] + '">Novedades</button>'
          + ''.join(f'<button class="tb" data-go="{i}">{E(n)}</button>' for n, i in cats) + '</div></nav>')
    # 2 · lo nuevo
    o += (f'<section class="nw" id="nuevo"><div class="w shd"><div><span class="ey">{E(A["new_e"])}</span><h2 class="h2">{E(A["new_h"])}</h2></div>'
          f'<div class="ar"><a href="#mas">Ver las {len(P)}{ic("arrow", 16, 2)}</a><button class="gw" data-dir="-1" aria-label="Anterior">{ic("arrow", 18, 2).replace("<path", "<path transform=\"rotate(180 12 12)\"", 1)}</button>'
          f'<button class="gd" data-dir="1" aria-label="Siguiente">{ic("arrow", 18, 2)}</button></div></div>'
          '<div class="car">' + ''.join(card(p, N['badge'] if k in (0, 2) else '') for k, p in enumerate(P[:6])) + '</div>'
          '<div class="w"><div class="pg"><i></i></div></div></section>')
    # 3 · por categoría
    o += (f'<section class="sx" id="cat" style="padding-top:8px"><div class="w"><span class="ey rv">Compra por categoría</span><h2 class="h2 rv">{E(A["cat_h"])}</h2><div class="cg">'
          + ''.join(f'<a class="tile rv" href="#nuevo"><img src="{img(c, i + "d") if i.startswith("p") else img(c, i)}" alt="{E(n)}" loading="lazy"><span class="shade"></span>'
                    f'<span class="tlb"><b>{E(n)}</b><span class="gl">{ic("arrow", 18, 2)}</span></span></a>' for n, i in cats)
          + '</div></div></section>')
    # 4 · ficha (la propuesta la enseña con ?at=destacado)
    th = [(p0['id'], img(c, p0['id'])), (p0['id'] + 'd', img(c, p0['id'] + 'd')), ('l1', img(c, 'l1'))]
    o += (f'<section class="sx bl" id="destacado"><div class="w ft"><div class="fgal rv"><div class="fth">'
          + ''.join(f'<button class="{"on" if k == 0 else ""}" data-src="{u}" aria-label="Ver foto {k + 1}"><img src="{u}" alt="" loading="lazy"></button>' for k, (_, u) in enumerate(th))
          + f'</div><div class="tile fmain"><img src="{th[0][1]}" alt="{E(p0["name"])}" loading="lazy"></div></div>'
          f'<div class="fi rv"><span class="ey">{E(N["feat_e"])}</span><h2 class="h2">{E(p0["name"])}</h2>'
          + (f'<p class="sub">{E(p0["desc"])}</p>' if p0.get('desc') else '')
          + f'<div class="fpr"><b>{pr}</b><small>IVA incluido</small></div>'
          f'<div class="fol"><span>{E(c.get("opts_l", N["opts_l"]))}</span>' + ('<a href="#" data-demo>Guía de tallas</a>' if N['opts_l'] == 'Talla' else '') + '</div>'
          '<div class="os">' + ''.join(f'<button{" class=on" if x == od else ""}>{E(x)}</button>' for x in opts) + '</div>'
          f'<div class="ft1">' + add(p0, 'bt ga fadd', 'Añadir a la cesta') + '</div>'
          f'<a class="fwa" href="#" data-demo>{ic("chat", 18)}¿Dudas? Pregúntanos por WhatsApp</a>'
          '<div class="fdet">' + ''.join(f'<div>{ic(i, 22)}{E(T(t, c))}</div>' for i, t in A.get('fdet', FDET)) + '</div></div></div></section>')
    # 5 · así se lleva
    lk = P[1:4]
    o += (f'<section class="sx bl" id="look"><div class="w lk"><div class="tile rv"><img src="{img(c, "l1")}" alt="" loading="lazy">'
          f'</div><div>'
          f'<div class="lkt rv"><span class="ey">{E(A["look_e"])}</span><h2 class="h2">{E(A["look_h"])}</h2><p class="sub">{E(A["look_s"])}</p></div>'
          '<div class="lkl rv">' + ''.join(f'<div class="lr"><span class="n">{k + 1}</span><img src="{img(c, p["id"])}" alt="" loading="lazy"><div><b>{E(p["name"])}</b><small>{pr}</small></div>'
                                       + add(p, 'gw', ic('plus', 18, 2)) + '</div>' for k, p in enumerate(lk)) + '</div>'
          f'<button class="bt gd lkb rv" data-look>{E(A["look_b"])}</button></div></div></section>')
    # 6 · lo más vendido
    bs = [P[i] for i in (1, 4, 2, 5)]
    o += (f'<section class="sx bl" id="mas"><div class="w"><div class="shd rv"><div><span class="ey">{E(A["best_e"])}</span><h2 class="h2">{E(A["best_h"])}</h2></div></div>'
          '<div class="bg4">' + ''.join(card(p, f'Nº {k + 1}').replace('class="pc"', 'class="pc rv"') for k, p in enumerate(bs)) + '</div></div></section>')
    # 7 · reseñas de ejemplo
    rv = ''
    for n, cy, pi, t in (c.get('rev') or REV[c['niche']]):
        p = P[pi]; cy = city if cy == '*' else cy
        rv += (f'<figure class="rc"><div class="rct"><span class="st">{STAR * 5}</span><span class="ej">Ejemplo</span></div><q>{E(t)}</q>'
               f'<figcaption><img src="{img(c, p["id"])}" alt="" loading="lazy"><span><b>{n} · {E(cy)}</b><small>Compró: {E(p["name"])}</small></span></figcaption></figure>')
    o += (f'<section class="sx bl" id="opiniones"><div class="w"><div class="rvh rv"><div><span class="ey">Reseñas de ejemplo</span><h2 class="h2">Lo que dicen de la tienda</h2></div>'
          f'<div class="rsc"><b>4,9</b><div><span class="st">{STAR * 5}</span><p>{E(A.get("rev_p", "Así se verán las opiniones de vuestras clientas. Estas son de ejemplo."))}</p></div></div></div>'
          f'<div class="rg">{rv}</div></div></section>')
    # 8 · la tienda
    addr = c.get('address') or ''
    maps = 'https://www.google.com/maps/search/' + urllib.parse.quote(f'{c["name"]} {addr} {city}')
    where = (E(addr[0].upper() + addr[1:]) + ', en ' if addr else 'En ') + E(c.get('cityfull', city))
    o += (f'<section class="sx vs" id="visita" style="padding-top:24px"><div class="w"><div class="tile rv"><img src="{img(c, "b")}" alt="Nuestra tienda" loading="lazy">'
          f'<div class="vc gk"><span class="ey">Nuestra tienda</span><h3>{E(N["visit_h"])}</h3><p>{where}. {E(A.get("visit_p", "Recoge tu pedido gratis en la tienda."))}</p>'
          f'<div class="hb"><a class="bt glw" href="{maps}" target="_blank" rel="noopener">{ic("pin", 18)}Cómo llegar</a>'
          f'<a class="bt gl" href="#" data-demo>{ic("chat", 18)}Escríbenos</a></div></div></div></div></section>')
    # 9 · instagram
    o += (f'<section class="sx" style="padding-top:0"><div class="w"><div class="igh rv"><span class="igr"><img src="{img(c, p0["id"])}" alt=""></span>'
          f'<div><b>@{E(c["ig"])}</b><small>{c["fk"]} seguidores</small></div><a class="bt gd" href="https://www.instagram.com/{E(c["ig"])}/" target="_blank" rel="noopener">Seguir</a></div>'
          '<div class="igg rv">' + ''.join(f'<img src="{img(c, i)}" alt="" loading="lazy">' for i in (P[0]['id'], 'l1', 'b', P[2]['id'], 'l2', P[4]['id'])) + '</div></div></section>')
    # 10 · club
    o += (f'<section class="sx bl" style="padding:72px 0"><div class="w clb"><div class="rv"><h2 class="h2">{E(N["club"])}</h2><p class="sub">Te avisamos cuando llegue algo nuevo a la tienda.</p></div>'
          '<form class="rv"><input type="email" placeholder="Tu email" aria-label="Tu email"><button class="bt ga">Unirme</button></form></div></section>')
    # pie
    o += (f'<footer class="fo"><div class="w"><div class="fog"><div>{G.logo(c)}<p>{E(c.get("cityfull", city))}<br>@{E(c["ig"])}</p></div>'
          '<div><h4>Tienda</h4><nav><a href="#nuevo">Novedades</a>' + ''.join(f'<a href="#cat">{E(n)}</a>' for n in cn) + '</nav></div>'
          '<div><h4>Ayuda</h4><nav><a href="#" data-demo>Envíos</a><a href="#" data-demo>Cambios y devoluciones</a><a href="#visita">Recogida en tienda</a><a href="#" data-demo>Contacto</a></nav></div>'
          '<div><h4>Pago seguro</h4><div class="pay"><span class="gl">Tarjeta</span><span class="gl">Bizum</span><span class="gl">Apple Pay</span><span class="gl">Google Pay</span></div></div></div>'
          f'<div class="fox"></div><p class="cp">© {nm} · Tienda de ejemplo hecha por 404 Growth. No es la web oficial.</p></div></footer>')
    o += (f'<div class="ov"></div><aside class="dr" aria-label="Cesta"><div class="dh"><b>Tu cesta</b><button data-close aria-label="Cerrar">{ic("x", 22)}</button></div>'
          f'<div class="dl"></div><div class="df"><button class="bt gd" data-pay>Finalizar compra</button><p>{E(T(A.get("drp", "Envío a toda España · Recogida gratis en {city}"), c))}</p></div></aside><div class="tz"></div>')
    o += f'<script>{G.STORE_JS}</script><script>{JS}</script></body></html>'
    return o


def build(slug, imgs=True):
    c = G.load(slug); os.makedirs(OUT, exist_ok=True)
    if imgs:
        G.images(c); detail(c)
    h = store(c)
    open(os.path.join(OUT, f'p-{slug}--tienda.html'), 'w', encoding='utf-8').write(h)
    print('ok', slug, len(h))


if __name__ == '__main__':
    for s in [x for x in sys.argv[1:] if not x.startswith('-')]:
        build(s, '--noimg' not in sys.argv)
