-- 19/11/2026 · traslado de 404 Content: en la base nueva (cuenta de Javier), lo cifrado otra vez con la clave nueva (p_reseal,
-- hecho por el Worker viejo con reseal_patch.py) sustituye a lo cifrado con la vieja. Después, p_reseal se borra.
UPDATE p_cfg SET v = (SELECT r.v FROM p_reseal r WHERE r.t = 'cfg' AND r.a = p_cfg.k AND r.b = '')
  WHERE EXISTS (SELECT 1 FROM p_reseal r WHERE r.t = 'cfg' AND r.a = p_cfg.k AND r.b = '');
UPDATE p_conn SET token = (SELECT r.v FROM p_reseal r WHERE r.t = 'conn' AND r.a = p_conn.tenant_id AND r.b = p_conn.kind)
  WHERE EXISTS (SELECT 1 FROM p_reseal r WHERE r.t = 'conn' AND r.a = p_conn.tenant_id AND r.b = p_conn.kind);
DROP TABLE p_reseal;
