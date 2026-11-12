# JS para la pestaña de Flow: __JT (textos de los trabajos de unas tiendas) para emparejar cada imagen con su trabajo (__match).
import json, sys
J = json.load(open('flow/jobs35.json'))
S = set(sys.argv[1:])
T = [[j['slug'], j['id'], j['text']] for j in J if j['slug'] in S]
print("window.__JT=(window.__JT||[]).filter(x=>!%s.includes(x[0])).concat(%s.map(([s,i,t])=>[s,i,__tok(t)]));window.__R=window.__R||{};window.__seen=window.__seen||{};window.__wlog=window.__wlog||[];'JT '+__JT.length"
      % (json.dumps(sorted(S)), json.dumps(T, ensure_ascii=False)))
