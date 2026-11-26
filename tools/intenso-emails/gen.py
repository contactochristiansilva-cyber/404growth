# Genera las 7 notificaciones de Shopify (Liquid + HTML de email con tablas) de Intenso.
import os
OUT = os.path.dirname(os.path.abspath(__file__))
F = "-apple-system,BlinkMacSystemFont,'SF Pro Text',Inter,'Helvetica Neue',Helvetica,Arial,sans-serif"
CDN = "https://cdn.shopify.com/s/files/1/1026/0240/8263/files/"
WA = "https://wa.me/34623585666"
REVIEW = "https://search.google.com/local/writereview?placeid=ChIJl5a3vJL7cg0R6fPbml3RYrM"
MAPS = "https://www.google.com/maps/search/?api=1&query=Intenso+Fragancias+C.+Hoyo+11+Torremolinos&query_place_id=ChIJl5a3vJL7cg0R6fPbml3RYrM"
S = "{{ shop.url }}"
INK, MUTED, BODY, GOLD, CREAM, CREAM2, LINE, DARK = "#111111", "#6B6052", "#473F34", "#8A5E22", "#F6F1EA", "#FBF8F3", "#EFE7DC", "#14100C"


def img(name, w):
    return f"{CDN}{name}?width={w * 2}"


def btn(text, href, dark=True, size=14):
    bg, fg = (INK, "#FFFFFF") if dark else (CREAM, INK)
    return (f'<table role="presentation" cellpadding="0" cellspacing="0" style="display:inline-table;margin:0 4px 8px">'
            f'<tr><td style="background:{bg};border-radius:999px"><a href="{href}" style="display:inline-block;padding:13px 24px;'
            f'font-family:{F};font-size:{size}px;font-weight:600;color:{fg};text-decoration:none;border-radius:999px">{text}</a></td></tr></table>')


def eyebrow(t, c=GOLD):
    return f'<div style="font-size:11px;font-weight:700;letter-spacing:.08em;color:{c};text-transform:uppercase">{t}</div>'


def h1(t, c=INK):
    return f'<h1 class="h1" style="margin:10px 0 0;font-family:{F};font-size:32px;line-height:1.08;font-weight:800;letter-spacing:-.03em;color:{c}">{t}</h1>'


def h2(t):
    return f'<h2 style="margin:0;font-family:{F};font-size:22px;line-height:1.15;font-weight:800;letter-spacing:-.02em;color:{INK}">{t}</h2>'


def p(t, c=BODY, size=15, mt=12):
    return f'<p style="margin:{mt}px 0 0;font-size:{size}px;line-height:1.55;color:{c}">{t}</p>'


def row(inner, pad="32px 40px 0", bg=None):
    b = f"background:{bg};" if bg else ""
    return f'<tr><td class="px" style="{b}padding:{pad}">{inner}</td></tr>\n'


def card_link(title, sub, href, num=None, dark=False):
    bg = DARK if dark else CREAM2
    tc, sc, ac = ("#FFFFFF", "#D9D2C7", "#E9B872") if dark else (INK, MUTED, GOLD)
    lead = f'<td width="38" valign="middle" style="font-size:24px;font-weight:300;color:{GOLD}">{num}</td>' if num else ""
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin:0 0 10px;background:{bg};border-radius:18px">'
            f'<tr>{lead}<td style="padding:16px 18px"><a href="{href}" style="text-decoration:none;color:{tc}"><b style="font-size:15px;color:{tc}">{title}</b><br>'
            f'<span style="font-size:13px;color:{sc}">{sub}</span></a></td>'
            f'<td width="40" align="right" style="padding-right:18px"><a href="{href}" style="text-decoration:none;font-size:18px;color:{ac}">&rarr;</a></td></tr></table>')


def regalo_box(title, text, link=None, link_text=None):
    l = f'<br><a href="{link}" style="display:inline-block;margin-top:10px;font-size:13px;font-weight:700;color:{GOLD};text-decoration:none">{link_text} &rarr;</a>' if link else ""
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:{CREAM};border-radius:22px;overflow:hidden"><tr>'
            f'<td width="200" class="stack" valign="top" style="line-height:0"><img src="{img("email-decants-regalo.jpg", 200)}" width="200" alt="Los 2 decants de regalo de Intenso, atados con un lazo" style="display:block;width:200px;height:auto;border:0"></td>'
            f'<td class="stack" valign="middle" style="padding:22px 24px">{eyebrow("En tu caja")}'
            f'<div style="margin-top:8px;font-size:20px;line-height:1.2;font-weight:700;color:{INK}">{title}</div>{p(text, size=14, mt=8)}{l}</td></tr></table>')


def lines3(prefix_link=""):
    cells = ""
    for name, h, sub in (("Esenciales", "esenciales", "Desde 6,95 €"), ("Nicho", "nicho", "Desde 11,95 €"), ("Extractos", "extractos", "De 8 a 12 horas")):
        cells += (f'<td width="33%" valign="top" style="padding:0 6px"><a href="{S}/collections/{h}" style="text-decoration:none;color:{INK}">'
                  f'<img src="{img("intenso-lineas-" + h + ".jpg", 160)}" width="160" alt="Línea {name}" style="display:block;width:100%;max-width:160px;height:auto;border-radius:16px;border:0">'
                  f'<b style="display:block;margin-top:10px;font-size:15px">{name} &rarr;</b><span style="font-size:12px;color:{MUTED}">{sub}</span></a></td>')
    return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>{cells}</tr></table>'


def bestsellers():
    items = (("7008", "Nº 7008", "Nicho", "intenso-estudio-nicho.jpg", "Desde 11,95 €"),
             ("8004", "Nº 8004", "Nicho", "intenso-estudio-nicho.jpg", "Desde 11,95 €"),
             ("222", "Nº 222", "Esenciales", "intenso-estudio-esenciales.jpg", "Desde 6,95 €"))
    cells = ""
    for hnd, t, line, im, price in items:
        u = f"{S}/products/{hnd}"
        cells += (f'<td width="33%" valign="top" style="padding:0 6px"><a href="{u}" style="text-decoration:none;color:{INK}">'
                  f'<img src="{img(im, 170)}" width="170" alt="{t}" style="display:block;width:100%;max-width:170px;height:auto;border-radius:14px;border:0"></a>'
                  f'<div style="margin-top:10px;font-size:11px;font-weight:600;letter-spacing:.06em;color:{GOLD};text-transform:uppercase">{line}</div>'
                  f'<div style="font-size:16px;font-weight:700;color:{INK}">{t}</div><div style="font-size:13px;color:{INK};margin:2px 0 10px">{price}</div>'
                  f'<a href="{u}" style="display:block;background:{INK};color:#FFFFFF;text-align:center;text-decoration:none;font-size:13px;font-weight:600;padding:11px 0;border-radius:999px">Ver perfume</a></td>')
    return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>{cells}</tr></table>'


NAV = [("Mujer", "/collections/mujer"), ("Hombre", "/collections/hombre"), ("Esenciales", "/collections/esenciales"),
       ("Nicho", "/collections/nicho"), ("Extractos", "/collections/extractos"), ("Packs", "/pages/packs")]


def page(title, body, pre=""):
    nav = " &nbsp;&nbsp; ".join(f'<a href="{S}{u}" style="color:{INK};text-decoration:none">{t}</a>' for t, u in NAV)
    perks = (f'<td width="33%" valign="top" align="center" style="padding:0 8px"><div style="font-size:20px;line-height:1;color:{GOLD}">&#9992;</div>'
             f'<b style="display:block;margin-top:8px;font-size:13px">Envío gratis desde 59 €</b><span style="font-size:12px;color:{MUTED}">2 a 3 días hábiles en la Península</span></td>'
             f'<td width="33%" valign="top" align="center" style="padding:0 8px"><img src="{img("email-decants-regalo.jpg", 40)}" width="40" alt="" style="display:inline-block;width:40px;height:auto;border-radius:8px;border:0">'
             f'<b style="display:block;margin-top:6px;font-size:13px">2 decants de regalo</b><span style="font-size:12px;color:{MUTED}">De 3 ml, en cada pedido</span></td>'
             f'<td width="33%" valign="top" align="center" style="padding:0 8px"><div style="font-size:16px;line-height:1;color:#E9B872;letter-spacing:2px">&#9733;&#9733;&#9733;&#9733;&#9733;</div>'
             f'<b style="display:block;margin-top:8px;font-size:13px">5,0 en Google</b><span style="font-size:12px;color:{MUTED}">225 reseñas</span></td>')
    links = " &nbsp;·&nbsp; ".join(f'<a href="{S}/pages/{h}" style="color:#D9D2C7;text-decoration:none">{t}</a>' for t, h in (
        ("Envíos", "envios"), ("Devoluciones", "cambios-y-devoluciones"), ("Preguntas", "preguntas-frecuentes"), ("Privacidad", "politica-de-privacidad")))
    return f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="x-apple-disable-message-reformatting"><title>{title}</title>
<style>
@media (max-width:620px){{
 .wrap{{width:100%!important;border-radius:0!important}}
 .px{{padding-left:20px!important;padding-right:20px!important}}
 .h1{{font-size:27px!important}}
 .stack{{display:block!important;width:100%!important;box-sizing:border-box!important}}
 .stack img{{width:100%!important;max-width:100%!important}}
 .nav{{font-size:12px!important}}
}}
</style></head>
<body style="margin:0;padding:0;background:{CREAM};-webkit-font-smoothing:antialiased">
<div style="display:none;max-height:0;overflow:hidden;opacity:0">{pre}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:{CREAM}"><tr><td align="center" style="padding:20px 0">
<table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" style="width:600px;max-width:600px;background:#FFFFFF;border-radius:24px;overflow:hidden;font-family:{F};color:{INK}">
<tr><td align="center" style="background:{INK};color:#FFFFFF;font-size:12px;letter-spacing:.02em;padding:9px 16px">Envío gratis desde 59 € · 2 decants de regalo en cada pedido</td></tr>
<tr><td align="center" style="padding:26px 32px 14px"><a href="{S}"><img src="{img("email-logo-intenso.png", 120)}" width="120" alt="Intenso" style="display:block;width:120px;height:auto;border:0"></a></td></tr>
<tr><td align="center" class="nav" style="padding:0 16px 22px;font-size:13px;font-weight:500">{nav}</td></tr>
{body}
<tr><td style="padding:40px 0 0"></td></tr>
<tr><td style="background:{CREAM};padding:26px 24px"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>{perks}</tr></table></td></tr>
<tr><td align="center" style="background:{DARK};color:#FFFFFF;padding:34px 32px 30px;text-align:center">
<img src="{img("email-logo-intenso-blanco.png", 100)}" width="100" alt="Intenso" style="display:inline-block;width:100px;height:auto;border:0">
<p style="margin:18px 0 16px;font-size:14px;line-height:1.5;color:#D9D2C7">¿Dudas con tu perfume? Te contesta una persona, no un robot.</p>
<table role="presentation" cellpadding="0" cellspacing="0" align="center"><tr><td style="background:#FFFFFF;border-radius:999px"><a href="{WA}" style="display:inline-block;padding:12px 22px;font-size:14px;font-weight:600;color:{INK};text-decoration:none">Escríbenos por WhatsApp</a></td></tr></table>
<p style="margin:18px 0 0;font-size:12px;line-height:1.6;color:#9A8F82">Intenso Fragancias · C. Hoyo, 11 · 29620 Torremolinos (Málaga)<br>623 58 56 66 · holaintenso@gmail.com</p>
<p style="margin:14px 0 0;font-size:12px">{links}</p>
</td></tr>
</table></td></tr></table></body></html>
"""


def items_table(loop="subtotal_line_items", price="line.final_line_price"):
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0">{{% for line in {loop} %}}'
            f'<tr><td width="76" style="padding:0 0 14px;border-bottom:1px solid {LINE}"><img src="{{{{ line | img_url: \'144x180\', crop: \'center\' }}}}" width="64" alt="" style="display:block;width:64px;height:80px;border-radius:10px;background:{CREAM}"></td>'
            f'<td style="padding:0 0 14px 12px;border-bottom:1px solid {LINE}"><b style="font-size:15px;color:{INK}">{{{{ line.product.title | default: line.title }}}}</b><br>'
            f'<span style="font-size:13px;color:{MUTED}">{{% if line.product.type != blank %}}{{{{ line.product.type }}}} · {{% endif %}}{{% if line.variant.title != \'Default Title\' %}}{{{{ line.variant.title }}}} · {{% endif %}}{{{{ line.quantity }}}} ud.</span></td>'
            f'<td align="right" style="padding:0 0 14px;border-bottom:1px solid {LINE};font-size:15px;font-weight:700;white-space:nowrap">{{{{ {price} | money }}}}</td></tr>'
            f'<tr><td colspan="3" style="height:14px;line-height:14px;font-size:0">&nbsp;</td></tr>{{% endfor %}}</table>')


# ---------- T01 · Confirmación de pedido ----------
steps = ""
for i, (t, s, on) in enumerate((("Confirmado", "Hoy", "#2F6B3A"), ("Preparando", "Hoy", "#D19A50"), ("Enviado", "&nbsp;", None), ("En tu casa", "2 a 3 días", None))):
    dot = f'background:{on};' if on else f'border:2px solid #E5DCCF;'
    steps += (f'<td width="25%" align="center" valign="top" style="font-size:12px"><div style="width:12px;height:12px;border-radius:999px;{dot}margin:0 auto 8px;box-sizing:border-box"></div>'
              f'{"<b>" + t + "</b>" if on else "<span style=color:" + MUTED + ">" + t + "</span>"}<br><span style="color:{MUTED}">{s}</span></td>')

decant_cell = (
    "{% assign t = line.product.type %}{% if dn < 2 %}{% if t == 'Nicho' or t == 'Esenciales' or t == 'Extractos' %}"
    "{% if t == 'Nicho' %}{% assign vid = '55956377665863' %}{% assign dp = '2,95 €' %}{% elsif t == 'Esenciales' %}{% assign vid = '55956377633095' %}{% assign dp = '1,95 €' %}{% else %}{% assign vid = '55956377698631' %}{% assign dp = '3,95 €' %}{% endif %}"
    "{% assign ph = line.product.title | remove: 'Nº ' | strip | downcase %}"
    f'<td width="50%" valign="top" class="stack" style="padding:0 6px 12px"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border:1px solid {LINE};border-radius:18px"><tr>'
    f'<td width="70" style="padding:14px 0 14px 14px"><img src="{{{{ line | img_url: \'112x140\', crop: \'center\' }}}}" width="56" alt="" style="display:block;width:56px;height:70px;border-radius:8px"></td>'
    f'<td style="padding:14px"><b style="font-size:14px;color:{INK}">{{{{ line.product.title }}}} · 5 ml</b><br><span style="font-size:13px;color:{MUTED}">{{{{ dp }}}}</span><br>'
    f'<a href="{S}/cart/add?id={{{{ vid }}}}&quantity=1&properties%5BPerfume%5D={{{{ line.product.title | url_encode }}}}&properties%5B_u%5D=%2Fproducts%2F{{{{ ph | url_encode }}}}" '
    f'style="display:inline-block;margin-top:8px;background:{INK};color:#FFFFFF;text-decoration:none;font-size:12px;font-weight:600;padding:8px 14px;border-radius:999px">Lo quiero</a></td></tr></table></td>'
    "{% assign dn = dn | plus: 1 %}{% endif %}{% endif %}")

T01 = page("Pedido confirmado", (
    row(f'<div style="text-align:center"><div style="width:56px;height:56px;line-height:56px;border-radius:999px;background:#EAF3EC;color:#2F6B3A;font-size:28px;font-weight:700;margin:0 auto">&#10003;</div>'
        f'<div style="margin-top:14px;font-size:13px;color:{MUTED}">Pedido {{{{ order_name }}}}</div>'
        + h1("¡Gracias{% if customer.first_name %}, {{ customer.first_name }}{% endif %}!<br>Tu pedido está confirmado.")
        + p("Ya lo estamos preparando en la tienda. Te avisamos en cuanto salga, con el número de seguimiento.")
        + f'<div style="margin-top:20px">{btn("Ver mi pedido", "{{ order_status_url }}")}{btn("Seguir mirando", S + "/collections/all", False)}</div></div>', "8px 40px 0")
    + row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:{CREAM2};border-radius:18px"><tr><td style="padding:20px 10px"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>{steps}</tr></table></td></tr></table>', "24px 40px 0")
    + row(h2("Tu pedido") + '<div style="height:16px"></div>' + items_table()
          + f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="font-size:14px">'
          f'<tr><td style="padding:4px 0;color:{MUTED}">Subtotal</td><td align="right">{{{{ subtotal_price | money }}}}</td></tr>'
          f'{{% for d in discounts %}}<tr><td style="padding:4px 0;color:{MUTED}">Descuento {{{{ d.code }}}}</td><td align="right">−{{{{ d.savings | money }}}}</td></tr>{{% endfor %}}'
          f'<tr><td style="padding:4px 0;color:{MUTED}">{{% if shipping_address %}}Envío{{% else %}}Recogida en tienda{{% endif %}}</td><td align="right">{{% if shipping_price == 0 %}}Gratis{{% else %}}{{{{ shipping_price | money }}}}{{% endif %}}</td></tr>'
          f'<tr><td style="padding:4px 0;color:{MUTED}">2 decants de 3 ml</td><td align="right" style="color:#2F6B3A;font-weight:600">De regalo</td></tr>'
          f'<tr><td style="padding:10px 0 0;font-size:17px;font-weight:700">Total</td><td align="right" style="padding:10px 0 0;font-size:17px;font-weight:700">{{{{ total_price | money }}}}</td></tr>'
          f'<tr><td colspan="2" align="right" style="font-size:12px;color:{MUTED}">IVA incluido{{% if tax_price > 0 %}}: {{{{ tax_price | money }}}}{{% endif %}}</td></tr></table>'
          "{% assign falta = 5900 | minus: subtotal_price %}{% if shipping_price > 0 and falta > 0 %}"
          f'<div style="margin-top:14px;background:{CREAM};border-radius:12px;padding:12px 14px;font-size:13px;color:{BODY}">Te faltaban {{{{ falta | money }}}} para el envío gratis. La próxima vez, desde 59 € no pagas envío.</div>{{% endif %}}')
    + row(regalo_box("2 decants de 3 ml de regalo", "Los elegimos de nuestros más vendidos. Pruébalos y, si alguno te enamora, ya sabes su número."), "28px 40px 0")
    + "{% assign dn = 0 %}{% capture decants %}{% for line in subtotal_line_items %}" + decant_cell + "{% endfor %}{% endcapture %}{% if dn > 0 %}"
    + row(f'<div style="text-align:center">{eyebrow("Ya que estás")}<div style="margin-top:6px">{h2("Tu perfume, también en el bolso")}</div>'
          + p("El mismo número en un decant de cristal de 5 ml. Pídelo aparte; si lo quieres en la misma caja, escríbenos por WhatsApp antes de que salga.", size=14) + '</div>'
          + '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin-top:18px"><tr>{{ decants }}</tr></table>', "40px 34px 0")
    + "{% endif %}"
    + "{% assign tl = 'nicho' %}{% for line in subtotal_line_items %}{% assign t = line.product.type %}{% if t == 'Nicho' or t == 'Esenciales' or t == 'Extractos' %}{% assign tl = t | downcase %}{% break %}{% endif %}{% endfor %}"
    + row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>'
          f'<td width="50%" valign="top" class="stack" style="padding:0 6px 12px"><a href="{S}/pages/packs" style="text-decoration:none;color:{INK};display:block;background:{CREAM};border-radius:22px;overflow:hidden">'
          f'<img src="{CDN}pack-trio-{{{{ tl }}}}.jpg?width=520&height=440&crop=center" width="260" alt="Pack Trío de Intenso" style="display:block;width:100%;height:auto;border:0">'
          f'<div style="padding:18px"><b style="font-size:17px">Monta tu Trío</b><br><span style="font-size:13px;color:{BODY}">Tres perfumes de la misma línea en su caja, un euro menos que sueltos.</span><br>'
          f'<b style="display:inline-block;margin-top:8px;font-size:13px;color:{GOLD}">Elegir mis tres &rarr;</b></div></a></td>'
          f'<td width="50%" valign="top" class="stack" style="padding:0 6px 12px"><a href="{S}/collections/ambientadores" style="text-decoration:none;color:#FFFFFF;display:block;background:{DARK};border-radius:22px;overflow:hidden">'
          f'<img src="{CDN}ambientador-erba.jpg?width=520&height=440&crop=center" width="260" alt="Ambientador de Intenso" style="display:block;width:100%;height:auto;border:0">'
          f'<div style="padding:18px"><b style="font-size:17px;color:#FFFFFF">Para casa</b><br><span style="font-size:13px;color:#D9D2C7">Ambientadores con el aroma de Intenso, 15,95 €.</span><br>'
          f'<b style="display:inline-block;margin-top:8px;font-size:13px;color:#D19A50">Ver ambientadores &rarr;</b></div></a></td></tr></table>', "28px 34px 0")
    + row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="font-size:13px;line-height:1.6"><tr>'
          f'<td width="50%" valign="top" class="stack" style="padding:0 12px 12px 0"><b style="font-size:14px">{{% if shipping_address %}}Se envía a{{% else %}}Recogida en{{% endif %}}</b><br><span style="color:{BODY}">'
          "{% if shipping_address %}{{ shipping_address.name }}<br>{{ shipping_address.address1 }}{% if shipping_address.address2 %}, {{ shipping_address.address2 }}{% endif %}<br>{{ shipping_address.zip }} {{ shipping_address.city }}{% else %}Intenso · C. Hoyo, 11<br>29620 Torremolinos (Málaga){% endif %}</span></td>"
          f'<td width="50%" valign="top" class="stack"><b style="font-size:14px">Entrega</b><br><span style="color:{BODY}">{{{{ shipping_method.title | default: "Recogida en tienda" }}}}<br>Factura en <a href="{{{{ order_status_url }}}}" style="color:{GOLD}">tu pedido</a></span></td></tr></table>', "28px 40px 0")
), "Ya lo estamos preparando. Y van 2 decants de regalo en tu caja.")

# ---------- T02 · Confirmación de envío ----------
T02 = page("Pedido enviado", (
    row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:{DARK};border-radius:26px;overflow:hidden">'
        f'<tr><td style="line-height:0"><img src="{img("email-decants-regalo.jpg", 520)}" width="520" alt="Tu pedido de Intenso, con los 2 decants de regalo" style="display:block;width:100%;height:260px;object-fit:cover;border:0"></td></tr>'
        f'<tr><td style="padding:28px 30px 32px;color:#FFFFFF">{eyebrow("Pedido {{ order_name }} · en camino", "#D19A50")}{h1("Tu perfume ya ha salido de Torremolinos.", "#FFFFFF")}'
        + p("Llega en 2 a 3 días hábiles. Puedes seguirlo en todo momento con tu número de envío.", "#D9D2C7")
        + '<div style="margin-top:18px">{% if fulfillment.tracking_url %}'
        + f'<table role="presentation" cellpadding="0" cellspacing="0"><tr><td style="background:#FFFFFF;border-radius:999px"><a href="{{{{ fulfillment.tracking_url }}}}" style="display:inline-block;padding:13px 24px;font-size:14px;font-weight:600;color:{INK};text-decoration:none">Seguir mi pedido</a></td></tr></table>'
        + '{% else %}'
        + f'<table role="presentation" cellpadding="0" cellspacing="0"><tr><td style="background:#FFFFFF;border-radius:999px"><a href="{{{{ order_status_url }}}}" style="display:inline-block;padding:13px 24px;font-size:14px;font-weight:600;color:{INK};text-decoration:none">Ver mi pedido</a></td></tr></table>'
        + '{% endif %}</div>'
        + '{% if fulfillment.tracking_number %}<p style="margin:12px 0 0;font-size:12px;color:#9A8F82">Nº de seguimiento {{ fulfillment.tracking_number }}{% if fulfillment.tracking_company %} · {{ fulfillment.tracking_company }}{% endif %}</p>{% endif %}'
        + '</td></tr></table>', "4px 24px 0")
    + row(h2("Mientras llega") + '<div style="height:16px"></div>'
          + card_link("Cómo hacer que dure más", "Dónde aplicarlo y por qué no frotar las muñecas.", S + "/pages/preguntas-frecuentes")
          + card_link("Encuentra tu siguiente perfume", "Test de 1 minuto con 4 preguntas.", S + "/#test")
          + card_link("¿Algo con la dirección?", "Escríbenos por WhatsApp con tu número de pedido.", WA + "?text=Hola%2C%20tengo%20una%20duda%20con%20mi%20pedido%20{{ order_name | url_encode }}"), "36px 40px 0")
    + row(f'<div style="text-align:center">{eyebrow("Para la próxima")}<div style="margin-top:6px">{h2("Los que más se repiten")}</div></div><div style="height:20px"></div>' + bestsellers(), "40px 34px 0")
), "Llega en 2 a 3 días hábiles. Síguelo aquí.")

# ---------- T03 · Entregado ----------
tips = ""
for n, t, s in (("1", "Sobre la piel hidratada", "Después de la ducha y la crema, el perfume se agarra mejor."),
                ("2", "En los puntos de calor", "Cuello, muñecas y detrás de las orejas."),
                ("3", "Sin frotar", "Deja que se seque solo para no romper las notas.")):
    tips += (f'<td width="33%" valign="top" class="stack" style="padding:0 6px 12px"><div style="background:{CREAM2};border-radius:18px;padding:20px 16px">'
             f'<div style="font-size:28px;font-weight:300;color:{GOLD}">{n}</div><b style="display:block;margin-top:6px;font-size:14px">{t}</b>'
             f'<span style="display:block;margin-top:6px;font-size:12px;line-height:1.45;color:{MUTED}">{s}</span></div></td>')
stars = "".join(
    f'<td style="padding:0 3px"><a href="{REVIEW}" style="display:inline-block;background:{"#E9B872" if k == 5 else "#2A231C"};color:{INK if k == 5 else "#FFFFFF"};text-decoration:none;font-size:14px;font-weight:700;padding:11px 14px;border-radius:999px">{k}&#9733;</a></td>'
    for k in range(1, 6))
T03 = page("Pedido entregado", (
    row(f'<div style="text-align:center">{eyebrow("Pedido {{ order_name }} · entregado")}{h1("Ya lo tienes en casa.<br>Ahora, a estrenarlo.")}{p("Tres gestos para que te dure todo el día.")}</div>', "8px 40px 0")
    + row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>{tips}</tr></table>', "24px 34px 0")
    + row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:{DARK};border-radius:26px"><tr><td align="center" style="padding:34px 26px;text-align:center;color:#FFFFFF">'
          f'<div style="font-size:22px;color:#E9B872;letter-spacing:4px">&#9733;&#9733;&#9733;&#9733;&#9733;</div>'
          f'<div style="margin-top:10px;font-size:24px;line-height:1.2;font-weight:800;color:#FFFFFF">¿Nos cuentas qué te ha parecido?</div>'
          + p("Somos una tienda de barrio en Torremolinos. Tu reseña en Google ayuda a que más gente nos encuentre.", "#D9D2C7", 14)
          + f'<table role="presentation" cellpadding="0" cellspacing="0" align="center" style="margin-top:18px"><tr>{stars}</tr></table>'
          f'<p style="margin:12px 0 0;font-size:12px;color:#9A8F82">Toca las estrellas y te llevamos a Google.</p></td></tr></table>', "32px 24px 0")
    + row(regalo_box("¿Te ha enamorado algún decant de regalo?", "Mira el número en la etiqueta y búscalo en la tienda.", S + "/search", "Buscar su número"), "24px 40px 0")
    + row(f'<div style="text-align:center">{eyebrow("El siguiente paso")}<div style="margin-top:6px">{h2("Prueba otra línea")}</div></div><div style="height:18px"></div>' + lines3(), "40px 34px 0")
), "Tres gestos para que te dure todo el día.")

# ---------- T04 · Listo para recoger ----------
T04 = page("Listo para recoger", (
    row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:{DARK};border-radius:26px;overflow:hidden">'
        f'<tr><td style="line-height:0"><img src="{CDN}intenso-tienda-hd.jpg?width=1040&crop=center&height=760" width="520" alt="La tienda de Intenso en C. Hoyo, 11" style="display:block;width:100%;height:auto;border:0"></td></tr>'
        f'<tr><td style="padding:26px 30px 30px;color:#FFFFFF">{eyebrow("Pedido {{ order_name }} · listo", "#E9B872")}{h1("Tu pedido te espera en la tienda.", "#FFFFFF")}'
        f'<p style="margin:10px 0 0;font-size:15px;color:#E5DDD2">C. Hoyo, 11 · Torremolinos</p></td></tr></table>', "4px 24px 0")
    + row(f'<div style="text-align:center">{btn("Cómo llegar", MAPS)}{btn("Avisar de que voy", WA + "?text=Hola%2C%20voy%20a%20recoger%20mi%20pedido%20{{ order_name | url_encode }}", False)}</div>', "26px 40px 0")
    + row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:{CREAM2};border-radius:20px;font-size:14px">'
          f'<tr><td style="padding:18px 22px 8px;color:{MUTED}">Qué traer</td><td align="right" style="padding:18px 22px 8px;font-weight:700">Tu nombre o el número {{{{ order_name }}}}</td></tr>'
          f'<tr><td valign="top" style="padding:8px 22px 18px;color:{MUTED}">Horario</td><td align="right" style="padding:8px 22px 18px;font-weight:700">L a V: 10:00–14:00 y 18:00–20:30<br>Sábados: 10:00–14:00</td></tr></table>'
          '{% if pickup_instructions != blank %}<p style="margin:12px 0 0;font-size:13px;color:#473F34">{{ pickup_instructions }}</p>{% endif %}', "24px 40px 0")
    + row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border:1px solid {LINE};border-radius:20px"><tr>'
          f'<td width="104" style="padding:18px 0 18px 18px"><img src="{img("intenso-lineas-nicho.jpg", 88)}" width="88" alt="Perfumes de Intenso" style="display:block;width:88px;height:auto;border-radius:14px"></td>'
          f'<td style="padding:18px"><b style="font-size:16px">Ya que vienes, huélelos todos</b>{p("En la tienda tienes más de 300 fragancias para probar antes de elegir la siguiente.", MUTED, 13, 6)}</td></tr></table>', "24px 40px 0")
), "Ya puedes pasar a recogerlo en C. Hoyo, 11.")

# ---------- T05 · Cancelado ----------
T05 = page("Pedido cancelado", (
    row(f'<div style="text-align:center">{eyebrow("Pedido {{ order_name }} · cancelado", MUTED)}{h1("Hemos cancelado tu pedido.")}'
        + p("{% case cancel_reason %}{% when 'customer' %}Lo hemos cancelado a petición tuya.{% when 'inventory' %}Nos hemos quedado sin alguno de tus perfumes y no queríamos hacerte esperar.{% when 'declined' %}El pago no se pudo completar.{% else %}Lo hemos tenido que cancelar.{% endcase %} No tienes que hacer nada más.")
        + '</div>', "8px 40px 0")
    + row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:{CREAM2};border-radius:20px"><tr><td style="padding:22px 24px">'
          f'<b style="font-size:16px">Tu reembolso</b>'
          f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin-top:10px;font-size:14px"><tr><td style="color:{MUTED}">Importe del pedido</td><td align="right"><b>{{{{ total_price | money }}}}</b></td></tr></table>'
          + p("Si ya lo habías pagado, te lo devolvemos a la misma forma de pago. Lo verás en tu cuenta en unos días hábiles, según tu banco.", BODY, 13, 10)
          + '</td></tr></table>', "24px 40px 0")
    + row(f'<div style="text-align:center">{h2("¿Lo volvemos a intentar?")}{p("Tus perfumes siguen esperándote.", BODY, 14, 6)}'
          f'<div style="margin-top:18px">{btn("Volver a la tienda", S + "/collections/all")}{btn("Preguntar por WhatsApp", WA + "?text=Hola%2C%20quer%C3%ADa%20preguntar%20por%20mi%20pedido%20cancelado%20{{ order_name | url_encode }}", False)}</div></div>', "34px 40px 0")
    + row('<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>' + "".join(
        f'<td width="33%" style="padding:0 5px"><a href="{S}{u}" style="display:block;text-decoration:none;color:{INK};border:1px solid {LINE};border-radius:16px;padding:16px 8px;text-align:center;font-size:14px;font-weight:600">{t} &rarr;</a></td>'
        for t, u in (("Para ella", "/collections/mujer"), ("Para él", "/collections/hombre"), ("Packs", "/pages/packs"))) + '</tr></table>', "24px 35px 0")
), "Te explicamos qué pasa con tu dinero.")

# ---------- T06 · Pago abandonado ----------
sizes = "".join(
    f'<td width="25%" style="padding:0 4px"><a href="{S}/pages/guia-de-tamanos" style="display:block;text-decoration:none;color:{INK};background:#FFFFFF;border-radius:14px;padding:14px 4px;text-align:center"><b style="font-size:15px">{t}</b><br><span style="font-size:11px;color:{MUTED}">{s}</span></a></td>'
    for t, s in (("30 ml", "Para probar"), ("50 ml", "El de diario"), ("100 ml", "Para todo el año"), ("500 ml", "Recarga")))
perks3 = "".join(
    f'<td width="33%" valign="top" style="padding:0 5px"><div style="background:{CREAM2};border-radius:16px;padding:14px 8px;text-align:center">{extra}<b style="font-size:13px">{t}</b><br><span style="font-size:12px;color:{MUTED}">{s}</span></div></td>'
    for t, s, extra in (("2 decants de regalo", "En cada pedido", f'<img src="{img("email-decants-regalo.jpg", 56)}" width="56" alt="" style="display:block;width:56px;height:auto;border-radius:10px;margin:0 auto 8px">'),
                        ("2 a 3 días", "En la Península", ""), ("5,0 en Google", "225 reseñas", "")))
T06 = page("Te has dejado algo", (
    row(f'<div style="text-align:center">{eyebrow("Tu cesta")}{h1("Te has dejado algo<br>que huele muy bien.")}{p("Te lo guardamos tal cual. Un toque y terminas la compra.")}{{% if custom_message != blank %}}<p style="margin:12px 0 0;font-size:15px;line-height:1.55;color:#473F34">{{{{ custom_message }}}}</p>{{% endif %}}</div>', "8px 40px 0")
    + row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border:1px solid {LINE};border-radius:22px"><tr><td style="padding:22px 22px 8px">'
          + items_table("line_items", "line.final_line_price")
          + f'<div style="text-align:center">{btn("Terminar mi compra", "{{ url }}", True, 15)}</div>'
          "{% assign falta = 5900 | minus: subtotal_price %}{% if falta > 0 %}"
          f'<p style="margin:4px 0 14px;text-align:center;font-size:12px;color:{MUTED}">Te faltan {{{{ falta | money }}}} para el envío gratis (desde 59 €)</p>{{% else %}}'
          f'<p style="margin:4px 0 14px;text-align:center;font-size:12px;color:#2F6B3A;font-weight:600">Tu envío es gratis</p>{{% endif %}}'
          '</td></tr></table>', "24px 40px 0")
    + row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>{perks3}</tr></table>', "24px 35px 0")
    + row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:{CREAM};border-radius:22px"><tr><td style="padding:22px 20px">'
          f'<b style="font-size:17px">¿Dudas con el tamaño?</b><table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin-top:14px"><tr>{sizes}</tr></table>'
          f'<a href="{WA}?text=Hola%2C%20tengo%20una%20duda%20antes%20de%20comprar" style="display:inline-block;margin-top:14px;font-size:14px;font-weight:600;color:{GOLD};text-decoration:none">Pregúntanos por WhatsApp &rarr;</a></td></tr></table>', "28px 40px 0")
    + row(f'<div style="text-align:center">{h2("Los más vendidos")}</div><div style="height:18px"></div>' + bestsellers(), "40px 34px 0")
), "Tu cesta te espera tal cual la dejaste.")

# ---------- T07 · Bienvenida de cuenta ----------
T07 = page("Tu cuenta de Intenso", (
    row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:{CREAM};border-radius:26px;overflow:hidden">'
        f'<tr><td style="line-height:0"><img src="{img("intenso-hero-hd.jpg", 520)}" width="520" alt="Los tres frascos de Intenso" style="display:block;width:100%;height:auto;border:0"></td></tr>'
        f'<tr><td style="padding:28px 30px 32px">{eyebrow("Tu cuenta está lista")}{h1("Hola{% if customer.first_name %}, {{ customer.first_name }}{% endif %}.<br>Esta es tu perfumería.")}'
        + p("Desde tu cuenta ves tus pedidos, repites tus números en un toque y guardas tus datos para la próxima.")
        + f'<div style="margin-top:18px;margin-left:-4px">{btn("Entrar en mi cuenta", S + "/account")}</div></td></tr></table>', "4px 24px 0")
    + row(h2("Por dónde empezar") + '<div style="height:16px"></div>'
          + card_link("No sé cuál elegir", "Test de 1 minuto y te decimos tus números.", S + "/#test", dark=True)
          + card_link("Ya sé mi número", "Búscalo y añádelo a la cesta.", S + "/search")
          + card_link("Quiero probar varios", "Dúo y Trío de la misma línea.", S + "/pages/packs"), "36px 40px 0")
    + row(lines3(), "28px 34px 0")
    + row('{% if unsubscribe_url != blank %}<p style="margin:0;text-align:center;font-size:11px;color:#8A7F72">¿No quieres recibir nuestros correos? <a href="{{ unsubscribe_url }}" style="color:#8A7F72">Darte de baja</a></p>{% endif %}', "24px 40px 0")
), "Tus pedidos, tus números y tus datos, en un sitio.")

for name, html in (("order_confirmation", T01), ("shipping_confirmation", T02), ("shipment_delivered", T03), ("ready_for_pickup", T04),
                   ("order_cancelled", T05), ("abandoned_checkout_notification", T06), ("customer_account_welcome", T07)):
    with open(os.path.join(OUT, name + ".liquid"), "w") as f:
        f.write(html)
    print(name, len(html))
