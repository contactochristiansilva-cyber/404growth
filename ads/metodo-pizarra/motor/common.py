# Motor común de las pizarras de /metodo (vídeos 2–8).
# Cada vídeo define marcos (HTML) y líneas de guion con marcadores; aquí se calculan los tiempos.
import json, re, os
HERE = os.path.dirname(os.path.abspath(__file__))
MAP = json.load(open(os.path.join(HERE, '..', 'map.json')))

RATE = 2.5     # palabras por segundo al narrar
GAP = 0.5      # pausa entre frases
FLY = 1.6      # duración de un vuelo de cámara

# ---------------- iconos (24×24, trazo) ----------------
IC = {
 'box': '<path d="M3 7.5l9-4.5 9 4.5v9l-9 4.5-9-4.5z"/><path d="M3 7.5l9 4.5 9-4.5M12 12v9"/>',
 'truck': '<path d="M2 6h11v10H2z"/><path d="M13 9h5l3 3v4h-8z"/><circle cx="6" cy="18" r="1.8"/><circle cx="17" cy="18" r="1.8"/>',
 'bell': '<path d="M6 16v-5a6 6 0 0 1 12 0v5l1.5 2h-15z"/><path d="M10 20a2 2 0 0 0 4 0"/>',
 'store': '<path d="M4 10v10h16V10"/><path d="M3 10l2-6h14l2 6z"/><path d="M10 20v-5h4v5"/>',
 'camera': '<path d="M4 8h3l2-3h6l2 3h3v11H4z"/><circle cx="12" cy="13" r="3.5"/>',
 'mega': '<path d="M3 10v4h3l7 4V6L6 10z"/><path d="M16 9a4 4 0 0 1 0 6M18.5 7a7 7 0 0 1 0 10"/>',
 'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
 'card': '<rect x="3" y="6" width="18" height="12" rx="2"/><path d="M3 10h18M7 15h3"/>',
 'chart': '<path d="M4 20V11M10 20V5M16 20v-6M2 20h20"/>',
 'lock': '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
 'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 'users': '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c.7-3.5 3.3-5.5 6.5-5.5s5.8 2 6.5 5.5"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14.8c2 .7 3.2 2.5 3.5 5.2"/>',
 'repeat': '<path d="M4 12a7 7 0 0 1 12-5l2 2M20 12a7 7 0 0 1-12 5l-2-2"/><path d="M18 4v5h-5M6 20v-5h5"/>',
 'star': '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>',
 'gift': '<rect x="3" y="8" width="18" height="5"/><path d="M5 13v8h14v-8M12 8v13"/><path d="M12 8c-2-4-6-4-6-1.5S9 8 12 8c3 0 6-.5 6-1.5S14 4 12 8z"/>',
 'pin': '<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
 'home': '<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/>',
 'tag': '<path d="M3 12V3h9l9 9-9 9z"/><circle cx="7.5" cy="7.5" r="1.5"/>',
 'doc': '<path d="M6 3h9l4 4v14H6z"/><path d="M15 3v4h4M9 12h7M9 16h7"/>',
 'search': '<circle cx="11" cy="11" r="6.5"/><path d="M16 16l5 5"/>',
 'bag': '<path d="M5 8h14l-1 12H6L5 8z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/>',
 'play': '<path d="M8 5.5v13l11-6.5z" fill="currentColor" stroke="none"/>',
 'check': '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
 'x': '<path d="M6 6l12 12M18 6L6 18"/>',
 'phone': '<rect x="7" y="2" width="10" height="20" rx="2.5"/><path d="M11 18h2"/>',
 'cal': '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
 'video': '<rect x="3" y="6" width="13" height="12" rx="2"/><path d="M16 10l5-3v10l-5-3z"/>',
 'wa': '<path d="M4 20l1.3-4A8 8 0 1 1 8 18.7z"/><path d="M9 9.5c.5 2 2 3.6 4.5 4.5"/>',
 'bank': '<path d="M3 9l9-5 9 5M5 10v8M9.7 10v8M14.3 10v8M19 10v8M3 20h18"/>',
 'eye': '<path d="M2 12s3.5-6 10-6 10 6 10 6-3.5 6-10 6S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
 'cart': '<path d="M3 4h2l2.5 11h11L21 7H6.3"/><circle cx="9" cy="19" r="1.5"/><circle cx="17" cy="19" r="1.5"/>',
 'spark': '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5L18 18M6 18l2.5-2.5M15.5 8.5L18 6"/>',
 'gear': '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M4.2 4.2l2.1 2.1M17.7 17.7l2.1 2.1M2 12h3M19 12h3M4.2 19.8l2.1-2.1M17.7 6.3l2.1-2.1"/>',
 'arrow': '<path d="M4 12h15M13 6l6 6-6 6"/>',
}
def ic(n, s=24, sw=1.8, col='currentColor', extra=''):
    return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" {extra}>{IC[n]}</svg>'

BAG = '<svg viewBox="0 0 120 120" width="{w}" height="{w}"><path d="M40 46c0-14 9-23 20-23s20 9 20 23" fill="none" stroke="#7A4E33" stroke-width="5" stroke-linecap="round"/><rect x="22" y="44" width="76" height="60" rx="11" fill="#C98B5E"/><path d="M22 58h76" stroke="#B0764B" stroke-width="3"/><rect x="54" y="62" width="12" height="9" rx="2" fill="#EBCFA3"/></svg>'
def bag(w=120): return BAG.replace('{w}', str(w))

# ---------------- piezas ----------------
def frame(fid, x, y, name, inner, w=1000, h=940):
    return f'<div class="fr" id="{fid}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><div class="fname">{name}</div>{inner}</div>'
def kick(t, col='var(--mute)', top=56):
    return f'<div class="kick" style="color:{col};top:{top}px">{t}</div>'
def h2(t, top=84, size=60):
    return f'<div class="h2 disp" style="top:{top}px;font-size:{size}px">{t}</div>'
def pill(t, id='', extra=''):
    return f'<div class="pill" {f"id={chr(34)}{id}{chr(34)}" if id else ""} {extra}>{t}</div>'
def st(id, x, y, l, v, s='', col='yel', w=272, h=214, vs=48, r=0, icon=None, extra=''):
    i = f'<div class="sti">{ic(icon, 26)}</div>' if icon else ''
    return (f'<div class="st {col}" id="{id}" data-r="{r}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;{extra}">{i}'
            f'<div class="l">{l}</div><div class="v" style="font-size:{vs}px">{v}</div>' + (f'<div class="s">{s}</div>' if s else '') + '</div>')
def card(id, x, y, w, h, inner, extra='', cls=''):
    a = f'id="{id}" ' if id else ''
    return f'<div class="card {cls}" {a}style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;{extra}">{inner}</div>'
def ab(id, x, y, inner, extra='', cls=''):
    a = f'id="{id}" ' if id else ''
    return f'<div class="abs {cls}" {a}style="left:{x}px;top:{y}px;{extra}">{inner}</div>'
def chk(ok=True):
    return f'<i class="{"ok" if ok else "no"}"></i>'
def lrow(id, text, ok=True, sub='', tag='', h=72, fs=27):
    s = f'<span class="rs">{sub}</span>' if sub else ''
    tg = f'<b class="tg {tag[0]}">{tag[1]}</b>' if tag else ''
    return f'<div class="row" id="{id}" style="height:{h}px;font-size:{fs}px">{chk(ok)}<span class="rt">{text}{s}</span>{tg}</div>'
def node(id, x, y, w, h, icon, title, sub='', badge=None, col='g'):
    b = f'<b class="badge {badge[0]}">{badge[1]}</b>' if badge else ''
    return (f'<div class="card node" id="{id}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">{b}'
            f'<i class="ni {col}">{ic(icon, 30)}</i><div class="nt">{title}</div>' + (f'<div class="ns">{sub}</div>' if sub else '') + '</div>')
import math
def _head(id, x1, y1, ang, col, w):
    L = 7 + w * 2.2
    a1, a2 = ang + math.radians(150), ang - math.radians(150)
    p = f"{x1:.1f},{y1:.1f} {x1+L*math.cos(a1):.1f},{y1+L*math.sin(a1):.1f} {x1+L*math.cos(a2):.1f},{y1+L*math.sin(a2):.1f}"
    return f'<polygon id="{id}h" data-fx="fade" data-d=".2" points="{p}" fill="{col}" stroke="{col}" stroke-width="{w*.6}" stroke-linejoin="round"/>'
def arr(id, pts, w=3, col='#1E2321', head=True):
    """flecha recta por puntos [(x,y),...]"""
    d = 'M' + ' L'.join(f'{x} {y}' for x, y in pts)
    h = _head(id, pts[-1][0], pts[-1][1], math.atan2(pts[-1][1]-pts[-2][1], pts[-1][0]-pts[-2][0]), col, w) if head else ''
    return f'<path id="{id}" data-fx="draw" d="{d}" pathLength="1" fill="none" stroke="{col}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" class="dash"/>' + h
def carr(id, x0, y0, cx, cy, x1, y1, w=3, col='#1E2321', head=True, d=.8):
    """flecha curva (cuadrática)"""
    h = _head(id, x1, y1, math.atan2(y1-cy, x1-cx), col, w) if head else ''
    return f'<path id="{id}" data-fx="draw" data-d="{d}" d="M{x0} {y0} Q{cx} {cy} {x1} {y1}" pathLength="1" fill="none" stroke="{col}" stroke-width="{w}" stroke-linecap="round" class="dash"/>' + h
def svg(inner, x=0, y=0, w=1000, h=940, extra=''):
    return f'<svg class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;overflow:visible" viewBox="0 0 {w} {h}" {extra}>{inner}</svg>'
def phone(id, x, y, inner, w=320, h=640, dark=False, extra=''):
    a = f'id="{id}" ' if id else ''
    sb = '#fff' if dark else '#16191A'
    return (f'<div class="phone" {a}style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;{extra}"><div class="scr{" dk" if dark else ""}">'
            f'<div class="sbar" style="color:{sb}"><span>23:15</span><span class="sbi"><i></i><i></i><i></i></span></div>{inner}</div></div>')
def nextframe(fid, x, y, recap_l, recap_v, recap_s, nv, ntitle, final=False):
    btn = (f'<div id="play" style="position:absolute;left:34px;bottom:34px;width:76px;height:76px;border-radius:50%;background:#fff;display:grid;place-items:center;color:#0B100E">{ic("play",28)}</div>'
           f'<div style="position:absolute;left:128px;bottom:58px;font-size:19px;color:rgba(255,255,255,.7)">Míralo ahora</div>') if not final else \
          (f'<div id="play" style="position:absolute;left:34px;bottom:34px;height:64px;padding:0 26px;border-radius:99px;background:#fff;display:flex;align-items:center;gap:12px;color:#0B100E;font-size:20px;font-weight:600">{ic("cal",24)}Hasta la llamada</div>')
    lab = f'VÍDEO {nv} · ≈2 MIN' if not final else 'LO HAS VISTO TODO'
    inner = (kick('SIGUIENTE' if not final else 'FIN') +
             st('nrec', 56, 120, recap_l, recap_v, recap_s, col='yel', w=300, h=250, vs=40, r=-1.4) +
             f'<div class="abs vcard" id="ncard" style="left:400px;top:110px;width:544px;height:430px">'
             f'<div style="font-size:16px;letter-spacing:.14em;font-weight:600;color:var(--g1)">{lab}</div>'
             f'<div class="disp" style="font-size:44px;font-weight:300;letter-spacing:-.035em;line-height:1.1;margin-top:16px">{ntitle}</div>{btn}</div>')
    return frame(fid, x, y, 'Siguiente' if not final else 'Hasta la llamada', inner, h=600)

# ---------------- mapa ----------------
def mapsvg(id, x, y, w, pts_cfg='', extra=''):
    sc = w / MAP['W']; h = MAP['H'] * sc
    return (f'<div class="abs map" id="{id}" style="left:{x}px;top:{y}px;width:{w}px;height:{h:.0f}px;{extra}">'
            f'<svg viewBox="0 0 {MAP["W"]} {MAP["H"]}" style="position:absolute;left:0;top:0;width:100%;height:100%;overflow:visible"><path class="es" d="{MAP["d"]}"/></svg>{pts_cfg}</div>')
def mpt(k, w):
    sc = w / MAP['W']; p = MAP['pts'][k]; return p[0] * sc, p[1] * sc
def mdot(id, k, w, col, lab=None, side=1, size=18):
    x, y = mpt(k, w)
    l = ''
    if lab:
        pos = f'left:{x+16:.0f}px' if side > 0 else f'right:{w-x+16:.0f}px'
        l = f'<div class="mlab" id="{id}l" style="{pos};top:{y-17:.0f}px;color:{col}">{lab}</div>'
    return f'<div class="mdot" id="{id}" style="left:{x:.0f}px;top:{y:.0f}px"><b style="background:{col};width:{size}px;height:{size}px;left:{-size/2}px;top:{-size/2}px"></b></div>{l}'
def mring(id, k, w, r, col, fill, dashed=True):
    x, y = mpt(k, w)
    return f'<div class="mring" id="{id}" style="left:{x-r:.0f}px;top:{y-r:.0f}px;width:{2*r}px;height:{2*r}px;border:2.5px {"dashed" if dashed else "solid"} {col};background:{fill}"></div>'

# ---------------- tiempo ----------------
TOK = re.compile(r'\{[^}]+\}|\S+')
def timeline(lines, frames_html, extra_cam=None):
    """lines: lista de textos con marcadores. Devuelve (times, cam, cur, ev, lines_out, dur)."""
    # qué elemento está en qué marco
    owner = {}
    for fid, html in frames_html.items():
        for m in re.finditer(r'id="([^"]+)"', html):
            owner.setdefault(m.group(1), fid)
    place = set()
    for html in frames_html.values():
        for m in re.finditer(r'<div class="st [^"]*" id="([^"]+)"', html): place.add(m.group(1))
        for m in re.finditer(r'id="([^"]+)"[^>]*data-place', html): place.add(m.group(1))
    t = 0.6; times = {}; cam = [[0, 'OV0', 0]]; cur = []; ev = {}; out = []
    for ln in lines:
        toks = TOK.findall(ln); start = t; words = []
        for tk in toks:
            if tk.startswith('{') and tk.endswith('}'):
                for part in tk[1:-1].split(','):
                    part = part.strip()
                    if part.startswith('p:'): t += float(part[2:]); continue
                    if part.startswith('@'):
                        tgt = part[1:]; dur = FLY; z = None
                        if '/' in tgt: tgt, dur = tgt.split('/'); dur = float(dur)
                        if '*' in tgt: tgt, z = tgt.split('*'); z = float(z)
                        if tgt == 'ALL': dur = 2.0
                        cam.append([round(t, 3), tgt, dur] + ([z] if z else []))
                        continue
                    if part.startswith('>>'): cur.append([round(t, 3), part[2:], .7, 1]); continue
                    if part.startswith('>'): cur.append([round(t, 3), part[1:], .7, 0]); continue
                    if part.startswith('!'): ev[part[1:]] = round(t, 3); continue
                    if part.endswith('*'):
                        pre = part[:-1]; allh = ''.join(frames_html.values())
                        ids = [m.group(1) for m in re.finditer(r'id="(' + re.escape(pre) + r'[A-Za-z0-9_]*)"', allh)]
                        for i, k in enumerate(dict.fromkeys(ids)): times[k] = round(t + 0.05 + i * 0.13, 3)
                        continue
                    off = 0.0
                    mm = re.match(r'^(.+?)([+-]\d*\.?\d+)$', part)
                    if mm: part, off = mm.group(1), float(mm.group(2))
                    times[part] = round(t + 0.05 + off, 3)
            else:
                words.append(tk); t += 1 / RATE
        out.append([round(start, 2), ' '.join(words)])
        t += GAP
    dur = round(t + 2.2, 2)
    # llegada de la cámara a cada marco → nada de su contenido aparece antes
    arrive = {}
    for k in cam[1:]:
        tgt = k[1]; fid = tgt if tgt in frames_html else owner.get(tgt)
        if fid and fid not in arrive: arrive[fid] = k[0] + k[2] * 0.8
    allh = ''.join(frames_html.values())
    for el in list(times):
        if f'id="{el}h"' in allh: times[el + 'h'] = times[el] + 0.62
        if f'id="{el}l"' in allh and el + 'l' not in times: times[el + 'l'] = times[el] + 0.35
        if f'id="{el}-p"' in allh: times[el + '-p'] = times[el] + 0.3
    for el, tt in list(times.items()):
        fid = owner.get(el)
        if fid in arrive and tt < arrive[fid]: times[el] = round(arrive[fid] + 0.1, 3)
    # cursor: coloca cada pósit; tras cada vuelo, se asoma al marco nuevo
    for el, tt in times.items():
        if el in place: cur.append([round(tt - 0.12, 3), el, .6, 1])
    for k in cam[1:]:
        tgt = k[1]
        if tgt in frames_html and tgt != 'ALL':
            a = k[0] + k[2]
            if not any(a - 0.3 <= c[0] <= a + 1.6 for c in cur): cur.append([round(a, 3), tgt, .9, 0])
    cur.sort(key=lambda c: c[0])
    # viajes que no se pisan
    for i in range(1, len(cur)):
        gap = cur[i][0] - cur[i-1][0]
        cur[i][2] = round(max(.22, min(cur[i][2], gap - .05)), 3)
    return times, cam, cur, ev, out, dur

def inject_times(html, times):
    def _of(m):
        k = m.group(1); mm = re.match(r'^(.+?)([+-]\d*\.?\d+)$', k); off = 0
        if mm: k, off = mm.group(1), float(mm.group(2))
        return f'data-out="{times[k] + off:.3f}"'
    html = re.sub(r'data-outf="([^"]+)"', _of, html)
    def rep(m):
        i = m.group(1)
        return f'id="{i}" data-t="{times[i]}"' if i in times else m.group(0)
    return re.sub(r'id="([^"]+)"', rep, html)

TEMPLATE = open(os.path.join(HERE, 'engine.html')).read()

def build(num, title, frames, lines, out_path, world_extra=''):
    fh = {fid: html for fid, html in frames}
    times, cam, cur, ev, lout, dur = timeline(lines, dict(fh, _w=world_extra))
    missing = [k for k in times if not re.search(f'id="{re.escape(k)}"', ''.join(fh.values()) + world_extra)]
    assert not missing, ('faltan ids', missing)
    board = inject_times(''.join(h for _, h in frames) + world_extra, times)
    spec = {'cam': cam, 'cur': cur, 'ev': ev, 'dur': dur, 'lines': lout}
    html = (TEMPLATE.replace('__NUM__', str(num)).replace('__TITLE__', title)
            .replace('__BOARD__', board).replace('__SPEC__', json.dumps(spec, ensure_ascii=False)))
    open(out_path, 'w').write(html)
    return spec
