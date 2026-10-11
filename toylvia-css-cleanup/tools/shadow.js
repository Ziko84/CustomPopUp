// node shadow.js <before.css> <after.css>
// For every style rule present in BEFORE but not in AFTER, prove it was shadowed:
// a LATER rule in BEFORE that is kept in AFTER, whose selector list contains every selector of the
// removed rule, whose condition chain is identical or empty (top level), and which declares every
// longhand of the removed rule with equal-or-higher priority. Prints PROVEN or the uncovered longhands.
const fs = require('fs'), os = require('os'), path = require('path');
const { execFileSync } = require('child_process'); const { pathToFileURL } = require('url');
function parse(f) {
  const css = fs.readFileSync(f, 'utf8');
  const html = `<!doctype html><meta charset="utf-8"><style id="s">${css}</style><pre id="o"></pre><script>
  const out=[];function walk(rules,ctx){for(const r of rules){
    if(r.constructor.name==='CSSStyleRule'){const d=[];for(let i=0;i<r.style.length;i++){const p=r.style.item(i);d.push([p,r.style.getPropertyPriority(p)])}
      out.push({ctx:ctx.join(' > '),sel:r.selectorText,decl:d,text:r.cssText});
      if(r.cssRules&&r.cssRules.length)walk(r.cssRules,ctx.concat(['&'+r.selectorText]));}
    else if(r.cssRules&&r.constructor.name!=='CSSKeyframesRule'){walk(r.cssRules,ctx.concat([r.constructor.name+'('+(r.conditionText||r.name||'')+')']));}
    else out.push({ctx:ctx.join(' > '),sel:null,decl:[],text:r.cssText});}}
  walk(document.getElementById('s').sheet.cssRules,[]);
  document.getElementById('o').textContent='S@@'+encodeURIComponent(JSON.stringify(out))+'@@E';</script>`;
  const tmp = path.join(os.tmpdir(), 'shadow-' + process.pid + '.html'); fs.writeFileSync(tmp, html);
  const dom = execFileSync(process.env.CHROME || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', ['--headless=new','--no-sandbox','--disable-gpu','--dump-dom',pathToFileURL(tmp).href], {maxBuffer:1<<28, stdio:['ignore','pipe','ignore']}).toString();
  return JSON.parse(decodeURIComponent(dom.match(/S@@([\s\S]*?)@@E/)[1]));
}
const B = parse(process.argv[2]), A = parse(process.argv[3]);
const key = (r) => r.ctx + '||' + r.text;
// align AFTER as a subsequence of BEFORE, matching from the END (a deletion never reorders rules,
// and when an earlier copy of an identical rule is deleted, the later copy is the one kept)
const kept = new Array(B.length).fill(false);
for (let i = B.length - 1, j = A.length - 1; i >= 0; i--) { if (j >= 0 && key(B[i]) === key(A[j])) { kept[i] = true; j--; } }
if (kept.filter(Boolean).length !== A.length) { console.log('ALIGNMENT FAILED: AFTER is not a pure deletion of BEFORE'); process.exit(1); }
const splitSel = (s) => s.split(/,\s*(?![^()]*\))/).map((x) => x.trim());
let allOk = true, nRemoved = 0;
B.forEach((r, i) => {
  if (kept[i]) return; nRemoved++;
  if (!r.sel) { console.log('NOT A STYLE RULE (check by hand): ' + r.text.slice(0, 120)); allOk = false; return; }
  const sels = splitSel(r.sel); const uncovered = [];
  for (const [prop, prio] of r.decl) {
    const ok = B.some((c, j) => j > i && kept[j] && c.sel && (c.ctx === r.ctx || c.ctx === '') &&
      sels.every((s) => splitSel(c.sel).includes(s)) &&
      c.decl.some(([p2, pr2]) => p2 === prop && (prio !== 'important' || pr2 === 'important')));
    if (!ok) uncovered.push(prop + (prio ? ' !' + prio : ''));
  }
  if (uncovered.length) { allOk = false; console.log('NOT SHADOWED: [' + r.ctx + '] ' + r.sel + ' -> ' + uncovered.join(', ')); }
  else console.log('shadowed: [' + (r.ctx || 'top') + '] ' + r.sel.slice(0, 90) + ' (' + r.decl.length + ' longhands)');
});
console.log(nRemoved + ' removed rules. ' + (allOk ? 'PROVEN: every removed rule is fully shadowed by a later kept rule.' : 'NOT PROVEN (see above).'));
