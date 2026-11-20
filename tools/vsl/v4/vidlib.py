import am, requests, time, json
def vsubmit(model, prompt, img, dur, res, extra=None):
    p = {'model': model, 'prompt': prompt, 'duration': dur, 'resolution': res, 'image_urls': [am.enc(img, 1920)]}
    if extra: p.update(extra)
    r = requests.post(am.B + '/videos/generations', json=p, headers=am.H, timeout=180); j = r.json()
    if r.status_code != 200: raise RuntimeError(str(j)[:500])
    d = j['data']; d = d[0] if isinstance(d, list) else d
    return d['task_id']
def vwait(tid, out, limit=1500):
    t0 = time.time()
    while time.time() - t0 < limit:
        time.sleep(8); d = requests.get(am.B + '/tasks/' + tid, headers=am.H, timeout=60).json().get('data', {})
        if d.get('status') == 'completed':
            res = d.get('result', {}); v = res.get('videos') or res.get('video') or res
            u = v[0]['url'] if isinstance(v, list) else (v.get('url') if isinstance(v, dict) else None)
            u = u[0] if isinstance(u, list) else u
            open(out, 'wb').write(requests.get(u, timeout=300).content); return out, round(time.time() - t0)
        if d.get('status') == 'failed': raise RuntimeError(str(d)[:500])
    raise RuntimeError('timeout')
