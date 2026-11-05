import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from msgs import jobs_all, jobs_lib, sents
jobs_lib.GRID = False
def keys(slug):
    J = {os.path.basename(j['out'])[:-4]: j for j in jobs_all.S[slug](slug)}
    S = {i: sents(j['prompt']) for i, j in J.items()}
    cnt = {}
    for ss in S.values():
        for x in set(ss): cnt[x] = cnt.get(x, 0) + 1
    out = {}
    for i, ss in S.items():
        uniq = [x for x in ss if cnt[x] == 1]
        best = max(uniq, key=len)
        out[i] = best[:70]
    return out
if __name__ == '__main__':
    print(json.dumps(keys(sys.argv[1]), ensure_ascii=False))
