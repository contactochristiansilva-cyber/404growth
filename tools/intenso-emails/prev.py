import liquid, sys, os
from liquid import Environment
env = Environment()
def money(c, v): return (f"{v/100:.2f}".replace('.', ',') + " €")
def img_url(*a, **k): return "https://cdn.shopify.com/s/files/1/1026/0240/8263/files/intenso-estudio-nicho.jpg?width=200"
from urllib.parse import quote
env.filters["money"]=money; env.filters["img_url"]=img_url; env.filters["url_encode"]=lambda c, v: quote(str(v))
P = lambda t, ty: {"title": t, "type": ty}
lines = [{"product": P("Nº 7008","Nicho"), "title":"Nº 7008", "variant":{"title":"30 ml"}, "quantity":1, "final_line_price":1195},
         {"product": P("Nº 222","Esenciales"), "title":"Nº 222", "variant":{"title":"50 ml"}, "quantity":1, "final_line_price":995}]
ctx = dict(shop={"url":"https://intensofragancias.com"}, customer={"first_name":"Lucía"}, order_name="#1042", order_status_url="#",
  subtotal_line_items=lines, line_items=lines, subtotal_price=2190, shipping_price=595, total_price=2785, tax_price=483, discounts=[],
  shipping_address={"name":"Lucía Martín","address1":"C. Ejemplo, 12","zip":"29001","city":"Málaga"}, shipping_method={"title":"Envío estándar"},
  fulfillment={"tracking_url":"#","tracking_number":"123","tracking_company":"Correos"}, url="#", cancel_reason="customer")
os.makedirs("prev", exist_ok=True)
for f in sorted(os.listdir(".")):
    if f.endswith(".liquid"):
        out = env.parse(open(f).read()).render(ctx)
        open("prev/"+f.replace(".liquid",".html"),"w").write(out); print(f, "ok")
