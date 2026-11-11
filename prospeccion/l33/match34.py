# Empareja las imágenes de Flow (meta: mid, p=prompt, w, h) con los trabajos de flow/jobs34.json por las palabras del prompt.
import json,re,sys
J=json.load(open('flow/jobs34.json'))
tok=lambda s:set(re.findall(r'[a-z0-9#]+',s.lower()))
JT=[tok(j['text']) for j in J]
M=[]
for f in sys.argv[2:]: M+=json.load(open(f))
out=json.load(open(sys.argv[1])) if __import__('os').path.exists(sys.argv[1]) else {}
for m in M:
    if not m['p']: continue
    t=tok(m['p']); s,i=max((len(t&JT[i])/len(t|JT[i]),i) for i in range(len(J)))
    if s<0.6: print('low',s,m['p'][:80]); continue
    k=J[i]['slug']+'|'+J[i]['id']; out.setdefault(k,m['mid'])
json.dump(out,open(sys.argv[1],'w'),indent=0)
miss=[j['slug']+'|'+j['id'] for j in J if j['slug']+'|'+j['id'] not in out]
print(len(out),'missing',miss)
