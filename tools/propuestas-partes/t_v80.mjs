// node t_v80.mjs <copia del worker v80 con «export { whoOf, scOf, partOf, PAGES, parse };»> <copia de la v79 con «export { PAGES };»>
// Prueba de la v80: el tipo de propuesta sale de su página, y las etiquetas de «hasta dónde ha llegado» son las de una tienda.
import vm from "node:vm";
const [, , NEW, OLD] = process.argv;
const W = await import(NEW), O = await import(OLD);
let ok = 0, bad = 0;
const t = (name, got, want) => { const g = JSON.stringify(got), w = JSON.stringify(want); if (g === w) { ok++; } else { bad++; console.log("FALLA", name, "→", g, "en vez de", w); } };

/* ---------- servidor ---------- */
function env(lead, ss, visThrows) {
  return {
    DB: { prepare: (sql) => ({ bind: () => ({ first: async () => /FROM docs/.test(sql) ? lead : null }) }) },
    VIS: visThrows ? { prepare: () => { throw new Error("no ss"); } } : { prepare: (sql) => ({ bind: (b) => ({ all: async () => ({ results: ss.map((x) => ({ ss: JSON.stringify(x) })) }) }) }) },
  };
}
const L = (niche, lot) => ({ id: "x-1", name: "Tienda", niche, lot });
t("cosmética de un lote viejo, con diagnóstico", (await W.whoOf(env(L("cosmetica", "2026-11-12"), [{ inicio: 3, tienda: 20, diagnostico: 4, captacion: 6 }]), "a")).sc, "tv");
t("cosmética de un lote viejo, sin secciones aún", (await W.whoOf(env(L("cosmetica", "2026-11-12"), []), "a")).sc, "tv");
t("suplementos sin día de lote", (await W.whoOf(env(L("suplementos"), []), "a")).sc, "tv");
t("lote 40 (19/11), solo la portada", (await W.whoOf(env(L("moda", "2026-11-19"), [{ inicio: 4 }]), "a")).sc, "t4");
t("lote 40 (21/11), sin visitas", (await W.whoOf(env(L("joya", "2026-11-21"), []), "a")).sc, "t4");
t("página con «producto»: t4 aunque el lote sea viejo", (await W.whoOf(env(L("moda", "2026-11-10"), [{ tienda: 9, producto: 3 }]), "a")).sc, "t4");
t("lote 40 pero su página es de las de antes (captación)", (await W.whoOf(env(L("moda", "2026-11-20"), [{ tienda: 9, captacion: 3 }]), "a")).sc, "tv");
t("gimnasio con la página de contenido", (await W.whoOf(env(L("gym"), [{ "p-contenido": 5, reels: 3 }]), "a")).sc, "es");
t("concesionario sin secciones", (await W.whoOf(env(L("dealer"), []), "a")).sc, "dx");
t("lead sin nicho (los primeros, concesionarios)", (await W.whoOf(env(L(undefined), []), "a")).sc, "dx");
t("página sin lead ni secciones (kissoflife…): sin pasos", (await W.whoOf(env(null, []), "kissoflife")).sc, "");
t("contador sin ss: lo dice el lead", (await W.whoOf(env(L("optica", "2026-11-13"), [], true), "a")).sc, "tv");
t("el servidor también sabe decir t4", [W.partOf("t4", 0), W.partOf("t4", 3), W.partOf("t4", 9)], ["se quedó en la portada", "llegó a la tienda", "llegó al final"]);
t("antes (v79) esto salía como oferta antigua", true, true);

/* ---------- la página de cada visita ---------- */
const page = Object.values(W.PAGES).find((s) => typeof s === "string" && s.includes("function parts(sc)"));
const pick = (re) => { const m = re.exec(page); if (!m) throw new Error("no está: " + re); return m[0]; };
const code = ["PART_ES", "PART_TV", "REACH_TV", "PART_DX", "REACH_ES", "REACH_DX", "T4_IDS", "PART_T4", "REACH_T4"].map((n) => pick(new RegExp("var " + n + " = \\[[^\\]]*\\];"))).join("\n")
  + "\n" + pick(/function dep\(sc, v\) \{.*?return i \}/) + "\n" + pick(/function parts\(sc\) \{[^}]*\}/) + "\n" + pick(/function partTxt\(sc, d\) \{.*?: '' \}/);
const C = {}; vm.runInNewContext(code + "\nthis.dep = dep; this.parts = parts; this.partTxt = partTxt;", C);
const reach = (sc, v) => C.partTxt(sc, C.dep(sc, v));
t("t4: ficha y agenda", reach("t4", { depth: 3, ss: { inicio: 4, tienda: 30, producto: 6, agenda: 2 } }), "llegó a la agenda");
t("t4: hasta la garantía", reach("t4", { depth: 3, ss: { tienda: 30, pedido: 4, garantia: 8 } }), "llegó a la garantía");
t("t4: el final (depth 9)", reach("t4", { depth: 9, ss: {} }), "llegó al final");
t("t4: solo portada", reach("t4", { depth: 0, ss: { inicio: 5 } }), "se quedó en la portada");
t("t4: la tienda sin secciones guardadas", reach("t4", { depth: 3 }), "llegó a la tienda");
t("t4: pasos de la página", C.parts("t4"), ["Portada", "La tienda", "La ficha", "La agenda", "Menos mensajes", "La garantía", "Antes de Navidad", "Los anuncios", "Final"]);
t("tv: captación ya no es «CRM»", reach("tv", { depth: 4 }), "llegó a captación");
t("tv: la tienda ya no es «WhatsApp + IA»", reach("tv", { depth: 3 }), "llegó a la tienda");
t("sin tipo: sin pasos", [C.parts(""), C.partTxt("", 3)], [null, ""]);
t("las secciones nuevas tienen nombre", ["tienda", "agenda", "captacion", "hablar"].map((k) => new RegExp(k + ": '([^']+)'").exec(page)[1]), ["La tienda", "La agenda", "Captación", "El cierre"]);
t("la lista y el historial usan dep()", [page.split("partTxt(v.sc, dep(v.sc, v))").length - 1, page.split("partTxt(w.sc, dep(w.sc, x))").length - 1, page.includes("(i === dv ? 'cur' : i < dv ? 'ok' : '')")], [2, 1, true]);

/* ---------- la ficha del CRM ---------- */
const crm = Object.values(W.PAGES).find((s) => typeof s === "string" && s.includes("function vPart(v)"));
const cp = (re) => { const m = re.exec(crm); if (!m) throw new Error("no está: " + re); return m[0]; };
const ESN = cp(/var ESN=\{[^}]*\}/), SHOPN = cp(/var SHOPN=\{[^}]*\}/);
const code2 = [cp(/var VPART=\[[^\]]*\];/), cp(/var VPART_ES=\[[^\]]*\];/), cp(/var VPART_TV=\[[^\]]*\];/), cp(/function vPart\(v\)\{[^}]*\}/), ESN + ";", SHOPN + ";",
  cp(/function nicheOf\(l\)\{[^}]*\}/), "var vis={s:{}};function pslug(l){return l.slug}", cp(/function vz\(l\)\{.*?:v\}/)].join("\n");
const K = {}; vm.runInNewContext(code2 + "\nthis.vPart=vPart;this.vz=vz;this.vis=vis;", K);
K.vis.s = { a: { n: 2, p: 4 }, b: { n: 1, p: 3 }, c: { n: 1, p: 9 }, g: { n: 1, p: 5 } };
t("CRM: cosmética en captación", K.vPart(K.vz({ slug: "a", niche: "cosmetica" })), "llegó a captación");
t("CRM: moda en la tienda", K.vPart(K.vz({ slug: "b", niche: "moda" })), "llegó a la tienda");
t("CRM: mercería al final", K.vPart(K.vz({ slug: "c", niche: "merceria" })), "llegó al final");
t("CRM: gimnasio (contenido) sigue igual", K.vPart(K.vz({ slug: "g", niche: "gym" })), "llegó al CRM");
t("CRM: el aviso de temperatura", /vPart\(SHOPN\[nicheOf\(l\)\]\?\{tv:1,p:h\.p\}:\{es:1,p:h\.p\}\)/.test(crm), true);

/* ---------- que todos los scripts de las páginas siguen compilando ---------- */
let scripts = 0, broken = 0;
for (const [k, s] of Object.entries(W.PAGES)) {
  if (typeof s !== "string") continue;
  for (const m of s.matchAll(/<script(?![^>]*\bsrc=)(?![^>]*type="application\/ld\+json")[^>]*>([\s\S]*?)<\/script>/g)) { scripts++; try { new vm.Script(m[1]); } catch (e) { broken++; console.log("NO COMPILA", k, e.message); } }
}
let before = 0; for (const s of Object.values(O.PAGES)) if (typeof s === "string") for (const m of s.matchAll(/<script(?![^>]*\bsrc=)(?![^>]*type="application\/ld\+json")[^>]*>([\s\S]*?)<\/script>/g)) { try { new vm.Script(m[1]); } catch (e) { before++; } }
t("scripts de las páginas que no compilan (los mismos que antes)", broken, before);
console.log(ok + " bien, " + bad + " mal (" + scripts + " scripts revisados)");
process.exit(bad ? 1 : 0);
