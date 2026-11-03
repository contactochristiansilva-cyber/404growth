"""Apimart (images/generations, async tasks). The key is read from .ak next to this file and never printed."""
import base64, io, json, os, time, requests
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
K = open(os.path.join(HERE, '.ak')).read().strip()
H = {'Authorization': 'Bearer ' + K}
B = 'https://api.apimart.ai/v1'


def balance():
    j = requests.get(B + '/user/balance', headers=H, timeout=30).json()
    return j.get('remain_balance')


def enc(p, maxside=2048):
    im = Image.open(p).convert('RGB')
    if max(im.size) > maxside:
        im.thumbnail((maxside, maxside))
    b = io.BytesIO(); im.save(b, 'JPEG', quality=90)
    return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()


def submit(model, prompt, refs, size, res='2K'):
    p = {'model': model, 'prompt': prompt, 'size': size, 'n': 1, 'resolution': res}
    if refs:
        p['image_urls'] = [enc(r) for r in refs]
    r = requests.post(B + '/images/generations', json=p, headers=H, timeout=180)
    j = r.json()
    if r.status_code != 200:
        raise RuntimeError('submit %s %s' % (r.status_code, str(j)[:300]))
    d = j.get('data'); d = d[0] if isinstance(d, list) else d
    return d['task_id']


def status(tid):
    j = requests.get(B + '/tasks/' + tid + '?language=es', headers=H, timeout=60).json()
    return j.get('data', {})


def fetch(d, out):
    u = d['result']['images'][0]['url']; u = u[0] if isinstance(u, list) else u
    img = requests.get(u, timeout=180).content
    open(out, 'wb').write(img)
    return Image.open(out).size


def run(model, prompt, refs, size, res, out, every=5, limit=900):
    tid = submit(model, prompt, refs, size, res)
    t0 = time.time()
    while time.time() - t0 < limit:
        time.sleep(every)
        d = status(tid)
        st = d.get('status')
        if st == 'completed':
            return fetch(d, out), time.time() - t0
        if st == 'failed':
            raise RuntimeError('failed ' + str(d)[:300])
    raise RuntimeError('timeout')
