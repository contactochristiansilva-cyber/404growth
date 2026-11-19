// 404 Growth · «404growth-partner» en la cuenta de Chris, desde el 19/11/2026 solo un puente.
// 404 Content se fue a la cuenta de Cloudflare de Javier, con 404-content.com. Esta dirección vieja (app.404growth.com) solo reenvía:
// las páginas, con un 301; lo demás (webhooks de Stripe y Meta, la API, la demo, los medios), tal cual, para que nada de lo que
// está configurado fuera con esta dirección se rompa.
const SITE = "https://404-content.com";
const API = (p) => p.startsWith("/api/") || p.startsWith("/admin/api/") || /^\/(wa|ig|meta)\//.test(p) || p.startsWith("/demo") || p === "/c/e" || p.startsWith("/m/") || p.startsWith("/s/") || p === "/sw.js";
export default {
  async fetch(req) {
    const u = new URL(req.url), p = u.pathname, M = req.method;
    if ((M === "GET" || M === "HEAD") && !API(p)) return new Response("", { status: 301, headers: { location: SITE + p + u.search } });
    const h = new Headers();
    for (const [k, v] of req.headers) if (!/^(host|cf-|x-forwarded-|x-real-ip|cdn-loop)/i.test(k)) h.set(k, v);
    const r = await fetch(SITE + p + u.search, { method: M, headers: h, body: M === "GET" || M === "HEAD" ? undefined : await req.arrayBuffer(), redirect: "manual" });
    return new Response(r.body, { status: r.status, headers: r.headers });
  },
};
