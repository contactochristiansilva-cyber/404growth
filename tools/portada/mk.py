import json,math
g=json.load(open('es.json'))
C=math.cos(math.radians(40));K=56.8
def P(lon,lat): return ((lon+9.6)*C*K,(44.0-lat)*K)
IS=0.78; IX,IY=418,384
CC=math.cos(math.radians(28.3))
def PI(lon,lat): return (IX+(lon+18.3)*CC*K*IS,IY+(29.5-lat)*K*IS)
main=[];can=[]
for poly in g['coordinates']:
    ring=poly[0];lat=sum(p[1] for p in ring)/len(ring)
    (main if lat>33 else can).append([(P if lat>33 else PI)(*p) for p in ring])
def inside(x,y,rings):
    c=False
    for r in rings:
        n=len(r);j=n-1
        for i in range(n):
            xi,yi=r[i];xj,yj=r[j]
            if (yi>y)!=(yj>y) and x<(xj-xi)*(y-yi)/(yj-yi)+xi: c=not c
            j=i
    return c
def dots(rings,step,minw=3):
    xs=[p[0] for r in rings for p in r];ys=[p[1] for r in rings for p in r]
    out=[];y=math.floor(min(ys)/step)*step+step/2
    while y<max(ys):
        x=math.floor(min(xs)/step)*step+step/2
        while x<max(xs):
            if inside(x,y,rings): out.append((x,y))
            x+=step
        y+=step
    for r in rings:
        if not any(inside(x,y,[r]) for x,y in out):
            w=max(p[0] for p in r)-min(p[0] for p in r)
            if w>minw: out.append((sum(p[0] for p in r)/len(r),sum(p[1] for p in r)/len(r)))
    return out
d1=dots(main,8.4);d2=dots(can,5.2,2)
xs=[p[0] for r in main for p in r];ys=[p[1] for r in main for p in r]
cx=[p[0] for r in can for p in r];cy=[p[1] for r in can for p in r]
def path(ds): return ''.join('M%.1f %.1fh0'%(x,y) for x,y in ds)
cities={'shop':(-3.70,40.42),'sevilla':(-5.98,37.39),'bilbao':(-2.93,43.26),'valencia':(-0.38,39.47),'coruna':(-8.41,43.36),'barcelona':(2.17,41.39),'palma':(2.65,39.57),'malaga':(-4.42,36.72),'zaragoza':(-0.88,41.65)}
cp={k:tuple(round(v,1) for v in P(*c)) for k,c in cities.items()}
W=round(max(max(xs),max(cx))+8);H=round(max(max(ys),max(cy))+8)
print('dots',len(d1),len(d2),'W',W,'H',H,'can',min(cx),max(cx),min(cy),max(cy))
cpath=''.join('M'+'L'.join('%.1f %.1f'%p for p in r)+'Z' for r in can)
json.dump({'d1':path(d1),'d2':cpath,'cities':cp,'W':W,'H':H,'can':[round(min(cx)-8),round(min(cy)-8),round(max(cx)+8),round(max(cy)+8)]},open('map.json','w'))
