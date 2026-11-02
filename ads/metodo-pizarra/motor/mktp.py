import json,sys
v=sys.argv[1]
p=json.load(open(f'tp{v}.json'))
h=open('tele.html').read().replace('__V__',v).replace('__PLAN__',json.dumps(p,ensure_ascii=False))
open(f'tp{v}.html','w').write(h)
