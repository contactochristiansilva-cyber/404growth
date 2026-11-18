// R2 de mentira para el brief: put (cuerpo entero), get, head y delete.
export function makeR2() {
  const objs = new Map();
  return {
    objs,
    async put(k, body, o) { const d = new Uint8Array(await new Response(body).arrayBuffer()); objs.set(k, { data: d, type: o && o.httpMetadata && o.httpMetadata.contentType }); return { key: k, size: d.length }; },
    async head(k) { const o = objs.get(k); return o ? { size: o.data.length } : null; },
    async get(k) { const o = objs.get(k); if (!o) return null; return { body: new Blob([o.data]).stream(), size: o.data.length }; },
    async delete(k) { for (const x of [].concat(k)) objs.delete(x); },
  };
}
