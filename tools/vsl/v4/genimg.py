import sys, os, concurrent.futures as cf
import am
from scenes import S, STYLE
ids = sys.argv[1:] or list(S)
print('saldo antes', am.balance(), flush=True)
def one(k):
    refs, p, _ = S[k]
    out = f'img/{k}.png'
    for attempt in range(2):
        try:
            sz, t = am.run('gemini-3-pro-image-preview', p + STYLE, [f'refs/{r}.jpg' for r in refs], '16:9', '2K', out)
            return k, sz, round(t)
        except Exception as e:
            err = str(e)[:200]
    return k, 'ERROR', err
with cf.ThreadPoolExecutor(6) as ex:
    for r in ex.map(one, ids): print(r, flush=True)
print('saldo después', am.balance(), flush=True)
