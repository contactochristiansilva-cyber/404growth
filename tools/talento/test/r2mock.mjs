// R2 de mentira para las pruebas (subida por partes, rangos, borrar). Comprueba lo mismo que R2: partes de igual tamaño, salvo la última.
export function makeR2() {
  const objs = new Map(), ups = new Map(); let seq = 0;
  const read = async (b) => (b instanceof Uint8Array ? b : new Uint8Array(await new Response(b).arrayBuffer()));
  const mk = (k, id) => ({
    key: k, uploadId: id,
    async uploadPart(n, body) { const u = ups.get(id); if (!u) throw new Error('no upload'); const d = await read(body); u.parts.set(n, d); return { partNumber: n, etag: 'e' + n + '-' + d.length }; },
    async complete(parts) {
      const u = ups.get(id); if (!u) throw new Error('no upload');
      const bufs = parts.map((p) => { const d = u.parts.get(p.partNumber); if (!d || p.etag !== 'e' + p.partNumber + '-' + d.length) throw new Error('etag'); return d; });
      for (let i = 0; i < bufs.length - 1; i++) if (bufs[i].length !== bufs[0].length || bufs[i].length < 5 * 1048576) throw new Error('part size');
      const all = new Uint8Array(bufs.reduce((a, b) => a + b.length, 0)); let o = 0; for (const b of bufs) { all.set(b, o); o += b.length; }
      objs.set(k, { data: all, type: u.type }); ups.delete(id); return { key: k, size: all.length };
    },
    async abort() { ups.delete(id); },
  });
  return {
    objs, ups,
    async createMultipartUpload(k, o) { const id = 'u' + (++seq); ups.set(id, { k, type: o && o.httpMetadata && o.httpMetadata.contentType, parts: new Map() }); return mk(k, id); },
    resumeMultipartUpload(k, id) { return mk(k, id); },
    async head(k) { const o = objs.get(k); return o ? { size: o.data.length, httpMetadata: { contentType: o.type } } : null; },
    async get(k, opt) { const o = objs.get(k); if (!o) return null; let d = o.data; if (opt && opt.range) d = d.slice(opt.range.offset, opt.range.offset + opt.range.length); return { body: new Blob([d]).stream(), size: o.data.length }; },
    async delete(k) { for (const x of [].concat(k)) objs.delete(x); },
  };
}
