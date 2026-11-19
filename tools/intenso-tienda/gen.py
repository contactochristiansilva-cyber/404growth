import sys, concurrent.futures as cf
sys.path.insert(0, '/home/claude/404growth/prospeccion/lote31/tools'); import am
SRC = '/tmp/claude-0/-home-claude/a676b6bb-0020-5a51-9455-0108b5df14a8/scratchpad/intenso/theme/assets/tienda.jpg'
OUT = '/tmp/claude-0/-home-claude/a676b6bb-0020-5a51-9455-0108b5df14a8/scratchpad/tienda/'
P = ("Upscale and restore this exact photograph to a crisp, high-resolution 4K photo. This is a faithful restoration, not a new image: "
     "keep EVERYTHING identical to the input: the same composition, framing, crop, camera angle and perspective, every object in exactly the same place and size, "
     "the same colors, white balance, exposure and lighting. Do not add, remove, move, restyle or redesign anything. "
     "Keep the wall logo exactly as it is: the word [INTENSO] between square brackets, the line FRAGANCIAS PARA CADA DIA below it and the mandala ornament above and below, same lettering. "
     "Only recover fine detail and sharpness: the glass bottles with cork stoppers and small labels on the white shelves, the shelf edges, the white brick wall, "
     "the rattan pendant lamp, the hanging greenery, the lavender pot, the long-leaf plant, the framed certificates, the counter, the light wooden floor and the tiled doormat. "
     "Remove blur, JPEG compression artifacts and noise. Photorealistic, natural phone photo quality, no added text, no watermark.")
jobs = [('seedream-5-5', 'sd', i) for i in range(2)] + [('gemini-3-pro-image-preview', 'nb', i) for i in range(2)]
def one(j):
    m, k, i = j
    try:
        return k, i, am.run(m, P, [SRC], '9:16', '4K', OUT + f'{k}_{i}.png')
    except Exception as e:
        return k, i, str(e)[:300]
with cf.ThreadPoolExecutor(4) as ex:
    for r in ex.map(one, jobs): print(r, flush=True)
print('saldo', am.balance())
