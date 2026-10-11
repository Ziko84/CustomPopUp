#!/usr/bin/env node
// Proves a CSS edit cannot change rendering.
//
//   node cssom.js compare <before.css> <after.css>
//
// Loads each file into headless Chrome and lists every rule Chrome keeps after
// parsing (the CSSOM), including rules nested in @media / @supports / nesting.
// Rendering is computed only from those rules, so:
//   IDENTICAL                      -> the edit cannot change anything on any page or width
//   DIFFERENT (+ list of rules)    -> the listed rules were added/removed; check that this
//                                     matches what the finding says
//
// Chrome is found via the CHROME env var, otherwise common install paths.
// macOS:   CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
// Windows: set CHROME=C:\Program Files\Google\Chrome\Application\chrome.exe
const fs = require('fs'), os = require('os'), path = require('path');
const { execFileSync } = require('child_process');
const { pathToFileURL } = require('url');

function findChrome() {
  if (process.env.CHROME) return process.env.CHROME;
  const c = [
    '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '/Applications/Chromium.app/Contents/MacOS/Chromium',
    'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
    '/usr/bin/google-chrome', '/usr/bin/chromium', '/usr/bin/chromium-browser',
  ];
  const hit = c.find((p) => fs.existsSync(p));
  if (!hit) throw new Error('Chrome not found. Set the CHROME env var to the Chrome executable.');
  return hit;
}

function parse(cssFile) {
  const css = fs.readFileSync(cssFile, 'utf8');
  if (/<\/style/i.test(css)) throw new Error(cssFile + ' contains "</style", cannot inline');
  const html = `<!doctype html><html><head><meta charset="utf-8"><style id="s">${css}</style></head><body><pre id="out"></pre><script>
function walk(rules, ctx, out){for(const r of rules){
  const head = r.cssRules ? (r.selectorText || r.conditionText || r.name || r.constructor.name) : null;
  out.push(ctx + r.cssText);
  if (r.cssRules && r.constructor.name !== 'CSSKeyframesRule') walk(r.cssRules, ctx + r.constructor.name + '(' + head + ') > ', out);
} return out}
const s = document.getElementById('s').sheet;
document.getElementById('out').textContent = 'S@@' + encodeURIComponent(JSON.stringify(walk(s.cssRules, '', []))) + '@@E';
</script></body></html>`;
  const tmp = path.join(os.tmpdir(), 'cssom-' + process.pid + '-' + path.basename(cssFile) + '.html');
  fs.writeFileSync(tmp, html);
  const dom = execFileSync(findChrome(), ['--headless=new', '--no-sandbox', '--disable-gpu', '--dump-dom', pathToFileURL(tmp).href],
    { maxBuffer: 1 << 28, stdio: ['ignore', 'pipe', 'ignore'] }).toString();
  fs.unlinkSync(tmp);
  const m = dom.match(/S@@([\s\S]*?)@@E/);
  if (!m) throw new Error('Chrome produced no output for ' + cssFile);
  return JSON.parse(decodeURIComponent(m[1]));
}

function multiset(list) { const m = new Map(); for (const x of list) m.set(x, (m.get(x) || 0) + 1); return m; }

const [, , cmd, a, b] = process.argv;
if (cmd !== 'compare' || !a || !b) { console.error('usage: node cssom.js compare <before.css> <after.css>'); process.exit(2); }
const A = parse(a), B = parse(b);
const ma = multiset(A), mb = multiset(B);
const removed = [], added = [];
for (const [k, n] of ma) for (let i = (mb.get(k) || 0); i < n; i++) removed.push(k);
for (const [k, n] of mb) for (let i = (ma.get(k) || 0); i < n; i++) added.push(k);
const sameOrder = A.length === B.length && A.every((x, i) => x === B[i]);
console.log(`before: ${A.length} rules (incl. nested) | after: ${B.length}`);
if (sameOrder) { console.log('IDENTICAL: Chrome keeps exactly the same rules in the same order. No visual change is possible.'); process.exit(0); }
console.log('DIFFERENT');
if (!removed.length && !added.length) console.log('Same rules, different ORDER (order can matter in the cascade). Investigate.');
for (const r of removed) console.log('  - removed: ' + r.slice(0, 300));
for (const r of added) console.log('  + added:   ' + r.slice(0, 300));
process.exit(1);
