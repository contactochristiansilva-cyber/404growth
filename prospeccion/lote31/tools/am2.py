"""Like am.run but also returns the result URL (and accepts http URLs as refs)."""
import time, requests, am
def submit(model, prompt, refs, size, res='2K'):
    p = {'model': model, 'prompt': prompt, 'size': size, 'n': 1, 'resolution': res}
    if refs:
        p['image_urls'] = [r if str(r).startswith('http') else am.enc(r) for r in refs]
    r = requests.post(am.B + '/images/generations', json=p, headers=am.H, timeout=180)
    j = r.json()
    if r.status_code != 200:
        raise RuntimeError('submit %s %s' % (r.status_code, str(j)[:300]))
    d = j.get('data'); d = d[0] if isinstance(d, list) else d
    return d['task_id']
def run(model, prompt, refs, size, res, out, every=5, limit=900):
    tid = submit(model, prompt, refs, size, res)
    t0 = time.time()
    while time.time() - t0 < limit:
        time.sleep(every)
        d = am.status(tid); st = d.get('status')
        if st == 'completed':
            u = d['result']['images'][0]['url']; u = u[0] if isinstance(u, list) else u
            sz = am.fetch(d, out)
            return u, sz
        if st == 'failed':
            raise RuntimeError('failed ' + str(d)[:300])
    raise RuntimeError('timeout')
