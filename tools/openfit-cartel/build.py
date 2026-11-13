import json, base64, sys, os
d='web/'
tpl=open('tour.html',encoding='utf-8').read()
P=json.load(open(d+'patches.json'))
def b64(f,mime='image/jpeg'): return 'data:%s;base64,%s'%(mime,base64.b64encode(open(d+f,'rb').read()).decode())
mode=sys.argv[1]
if mode=='web':
    img={'dia':{'s':'img/dia-2400.jpg','l':'img/dia-4032.jpg'},'noche':{'s':'img/noche-2400.jpg','l':'img/noche-4032.jpg'}}
    pt=[dict(p,src='img/%s.jpg'%p['n']) for p in P]
    rep={'__LOGO__':'img/logo.png','__ROOF__':'img/plano-rotulo.jpg','__LONA__':'img/plano-lona.jpg'}
else:
    di=b64('dia-2400.jpg'); ni=b64('noche-2400.jpg')
    img={'dia':{'s':di,'l':di},'noche':{'s':ni,'l':ni}}
    pt=[dict(p,src=b64(p['n']+'.jpg')) for p in P]
    rep={'__LOGO__':b64('logo.png','image/png'),'__ROOF__':b64('plano-rotulo.jpg'),'__LONA__':b64('plano-lona.jpg')}
out=tpl.replace('__IMG__',json.dumps(img)).replace('__PATCH__',json.dumps(pt))
for k,v in rep.items(): out=out.replace(k,v)
open(sys.argv[2],'w',encoding='utf-8').write(out); print(sys.argv[2], len(out)//1024,'KB')
