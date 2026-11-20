# Vuelve a transcribir una ventana de 16 s alrededor de cada corte de 30 s de la primera pasada, para recuperar las palabras cortadas.
import sherpa_onnx, soundfile as sf, json, sys
d = "sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8/"
r = sherpa_onnx.OfflineRecognizer.from_transducer(encoder=d+"encoder.int8.onnx", decoder=d+"decoder.int8.onnx", joiner=d+"joiner.int8.onnx",
    tokens=d+"tokens.txt", num_threads=2, model_type="nemo_transducer", decoding_method="greedy_search")
a, sr = sf.read("vsl2/audio.wav", dtype="float32")
W = json.load(open("vsl2/words.json"))
# cortes: huecos donde la primera pasada partió (cerca de múltiplos de 30 s)
out = {}
for c in [30, 60, 89, 119.4, 149.4, 179.9, 208.5]:
    a0, a1 = c-8, c+8
    s = r.create_stream(); s.accept_waveform(sr, a[int(a0*sr):int(a1*sr)]); r.decode_stream(s); res = s.result
    toks, ts = list(res.tokens), list(res.timestamps); du = list(getattr(res, "durations", []) or [])
    ws = []
    for i, (t, st) in enumerate(zip(toks, ts)):
        en = st + (du[i] if du else ((ts[i+1]-st) if i+1 < len(ts) else 0.1))
        if t.startswith(" ") or t.startswith("▁") or not ws:
            ws.append([t.replace("▁", " ").strip(), round(st+a0, 2), round(en+a0, 2)])
        else:
            ws[-1][0] += t; ws[-1][2] = round(en+a0, 2)
    out[c] = ws
    print(c, ' '.join(f"{w[0]}" for w in ws if c-4 <= w[1] <= c+4))
    print('   antes:', ' '.join(w[0] for w in W if c-4 <= w[1] <= c+4))
json.dump(out, open("vsl4/fix.json", "w"), ensure_ascii=False)
