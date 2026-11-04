"""Runs Apimart image jobs in parallel. usage: python3 runjobs.py jobs.json [workers]
jobs.json = [{"out": ".../ai/<slug>/<id>.jpg", "prompt": "...", "refs": [paths], "size": "4:5", "res": "2K", "model": "..."}]
Skips outputs that already exist. Retries twice. Jobs with "split": [ids] are 2x2 grids (jobs_all.py --rejilla):
after download they are cut into <dir>/<id>.jpg with gridsplit.py. Appends a line per job to ai/log.txt and the total cost at the end."""
import json, os, sys, time, traceback
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import am
import gridsplit

J = json.load(open(sys.argv[1])); NW = int(sys.argv[2]) if len(sys.argv) > 2 else 8
LOG = os.path.join(os.path.dirname(os.path.abspath(sys.argv[1])), 'log.txt')


def log(s):
    with open(LOG, 'a') as f:
        f.write(time.strftime('%H:%M:%S ') + s + '\n')


def cut(j):
    d = os.path.dirname(j['out'])
    if all(os.path.exists(os.path.join(d, i + '.jpg')) for i in j['split']):
        return
    gx, gy = gridsplit.place(j['out'], j['split'], d)
    log('SPLIT %s %s calles %s %s%s' % (j['out'].split('/ai/')[-1], ','.join(j['split']), gx, gy, '' if gx and gy else '  ¡REVISAR!'))


def one(j):
    out = j['out']
    if os.path.exists(out):
        if j.get('split'):
            cut(j)
        return 'skip'
    os.makedirs(os.path.dirname(out), exist_ok=True)
    for a in range(3):
        try:
            sz, t = am.run(j.get('model', 'gemini-3-pro-image-preview'), j['prompt'], j.get('refs', []), j['size'], j.get('res', '2K'), out + '.part.jpg')
            os.rename(out + '.part.jpg', out)
            log('OK %s %s %.0fs' % (out.split('/ai/')[-1], sz, t))
            if j.get('split'):
                cut(j)
            return 'ok'
        except Exception as e:
            log('ERR %s try%d %s' % (out.split('/ai/')[-1], a, str(e)[:200]))
            time.sleep(5)
    return 'fail'


b0 = am.balance()
log('START %d jobs, saldo %s' % (len(J), b0))
with ThreadPoolExecutor(NW) as ex:
    R = list(ex.map(one, J))
b1 = am.balance()
log('END ok=%d skip=%d fail=%d coste=%.3f saldo=%s' % (R.count('ok'), R.count('skip'), R.count('fail'), (b0 or 0) - (b1 or 0), b1))
