// Referencias de Instagram (lote 48): 24 publicaciones por cuenta, primera foto, reducida a 720 px en la página.
// En la pestaña de Instagram (con gq). RF.run(['cuenta1', …]) y luego RF.send('r1', 'rf48a.json') a una pestaña
// receptora instagram.com/robots.txt (window.__me = 'r1' + BroadcastChannel('rf48')).
window.RF = window.RF || { out: {}, st: { ok: 0, err: 0, img: 0 } };
RF.vars = (u) => ({ data: { count: 24, include_reel_media_seen_timestamp: true, include_relationship_info: true, latest_besties_reel_media: true, latest_reel_media: true }, username: u });
RF.url = (n) => { const m = (n.carousel_media && n.carousel_media[0]) || n; const c = (m.image_versions2 && m.image_versions2.candidates) || (n.image_versions2 && n.image_versions2.candidates) || []; const s = c.slice().sort((a, b) => b.width - a.width).find((x) => x.width <= 1080) || c[0]; return s && s.url; };
RF.jpg = async (url) => { const r = await fetch(url); const bm = await createImageBitmap(await r.blob()); const k = Math.min(1, 720 / Math.max(bm.width, bm.height)); const c = document.createElement('canvas'); c.width = Math.round(bm.width * k); c.height = Math.round(bm.height * k); c.getContext('2d').drawImage(bm, 0, 0, c.width, c.height); return c.toDataURL('image/jpeg', 0.86); };
RF.one = async (u) => {
  const p = await gq('PolarisProfilePostsQuery', RF.vars(u));
  const e = p.data && p.data.xdt_api__v1__feed__user_timeline_graphql_connection; const ed = (e && e.edges) || [];
  const L = []; let i = 0;
  for (const x of ed) { const n = x.node; if (!n) continue; i++; const url = RF.url(n); if (!url) continue;
    try { L.push({ n: String(i).padStart(2, '0'), d: await RF.jpg(url), cap: ((n.caption && n.caption.text) || '').slice(0, 400), t: n.taken_at || 0 }); RF.st.img++; } catch (err) { RF.st.err++; } }
  RF.out[u] = L; RF.st.ok++; return L.length;
};
RF.run = async (list) => { for (const u of list) { if (RF.out[u]) continue; try { await RF.one(u); } catch (e) { RF.st.err++; } await new Promise((r) => setTimeout(r, 1500)); } RF.done = true; };
RF.send = (to, name, keys) => { const o = {}; (keys || Object.keys(RF.out)).forEach((k) => { o[k] = RF.out[k]; }); const bc = new BroadcastChannel('rf48'); const json = JSON.stringify(o); bc.postMessage({ to, name, json }); return json.length; };
'rf48 ok';
