// a small D1 on node:sqlite: prepare/bind/first/all/run/batch and meta.size_after
import { DatabaseSync } from 'node:sqlite';
export function makeD1() {
  const db = new DatabaseSync(':memory:');
  const size = () => { const pc = db.prepare('PRAGMA page_count').get().page_count, ps = db.prepare('PRAGMA page_size').get().page_size; return pc * ps; };
  const conv = (v) => v instanceof Uint8Array ? v : (v === undefined ? null : v);
  const out = (row) => { if (!row) return row; const o = {}; for (const k in row) { const v = row[k]; o[k] = v instanceof Uint8Array ? Array.from(v) : v; } return o; };   // D1 gives blobs as arrays of numbers
  class St {
    constructor(sql, args) { this.sql = sql; this.args = args || []; }
    bind(...a) { return new St(this.sql, a.map(conv)); }
    _p() { return db.prepare(this.sql); }
    async first(col) { const r = out(this._p().get(...this.args)); return r === undefined ? null : (col ? r[col] : r); }
    async all() { return { results: this._p().all(...this.args).map(out), meta: { size_after: size() } }; }
    async run() { const s = this._p(); let changes = 0; if (/^\s*select/i.test(this.sql)) s.all(...this.args); else changes = s.run(...this.args).changes; return { success: true, meta: { size_after: size(), changes } }; }
  }
  return { prepare: (sql) => new St(sql), batch: async (sts) => { db.exec('BEGIN'); try { const r = []; for (const s of sts) r.push(await s.run()); db.exec('COMMIT'); return r; } catch (e) { db.exec('ROLLBACK'); throw e; } }, _db: db };
}
