import sys, os, json, requests, concurrent.futures as cf
import am, vidlib
from scenes import S
DUR = {'c4': 10, 'c9': 10, 'c11': 10}
ids = sys.argv[1:] or [k for k in S if not os.path.exists(f'vid/{k}.mp4')]
print('saldo antes', am.balance(), ids, flush=True)
def up(p):
    r = requests.post(am.B+'/uploads/images', headers=am.H, files={'file': (os.path.basename(p), open(p, 'rb'), 'image/jpeg')}, timeout=120).json()
    return r['url']
def one(k):
    err = ''
    for attempt in range(2):
        try:
            u = up(f'jpg/{k}.jpg')
            p = {'model': 'MiniMax-Hailuo-2.3-Fast', 'prompt': S[k][2], 'duration': DUR.get(k, 6), 'resolution': '768P', 'first_frame_image': u}
            r = requests.post(am.B + '/videos/generations', json=p, headers=am.H, timeout=180); j = r.json()
            if r.status_code != 200: raise RuntimeError(str(j)[:300])
            d = j['data']; d = d[0] if isinstance(d, list) else d
            return k, vidlib.vwait(d['task_id'], f'vid/{k}.mp4')
        except Exception as e:
            err = str(e)[:300]
    return k, 'ERROR', err
with cf.ThreadPoolExecutor(5) as ex:
    for r in ex.map(one, ids): print(r, flush=True)
print('saldo después', am.balance(), flush=True)
