#!/usr/bin/env python3
"""Regenerate README.md from findings.json:  python tools/render.py"""
import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent
data = json.loads((ROOT / 'findings.json').read_text(encoding='utf-8'))
items = data['items']
todo = [i for i in items if i['status'] == 'TODO']
review = [i for i in items if i['status'] == 'REVIEW']

def fence(t):
    t = t.rstrip('\n')
    lines = t.split('\n')
    if len(lines) > 60:
        t = '\n'.join(lines[:25] + [f'/* ... {len(lines) - 50} more lines, see findings.json exact_text ... */'] + lines[-25:])
    return '```css\n' + t + '\n```'

out = []
w = out.append
w(f"""# Toylvia CSS cleanup

Dead and commented-out CSS found in the live theme of https://toylvia.com by a cloud Claude scan.
Every item was found by one agent and then attacked by a separate skeptic agent that tried to prove it still affects the page. Only items that survived are listed.

- Scan started: {data['scan']['started']} | last update: {data['scan']['updated']} | rounds: {data['scan']['rounds']}
- Items: **{len(items)}** total, **{len(todo)} TODO** (proven safe), **{len(review)} REVIEW** (very likely safe, ask Ziko first)
- Lines removed if every item is applied: {sum(sum(pp['exact_text'].count(chr(10)) - pp.get('replacement', '').count(chr(10)) for pp in i['parts']) for i in items)} (TODO only: {sum(sum(pp['exact_text'].count(chr(10)) - pp.get('replacement', '').count(chr(10)) for pp in i['parts']) for i in todo)})
- Status legend: `TODO` apply | `REVIEW` apply only if Ziko says yes | `DONE` applied and verified | `SKIPPED: reason`

---

## For Ziko (what you do)

1. On your computer, open this repo and get the branch: `git fetch origin && git checkout {data['scan']['branch']} && git pull`
2. Open Claude (desktop / Claude Code) in this repo and say:
   **"Read toylvia-css-cleanup/README.md and apply the TODO items to the live theme."**
   (Add "and the REVIEW items" if you also want those.)
3. Claude will ask before it saves anything to the live theme. Say yes after you have read its summary.
4. If Claude cannot push to Shopify, it will tell you the exact lines to delete in Shopify admin (Online Store, Themes, Edit code).

---

## For Claude (desktop): what you need to do

You are applying a cleanup that was already researched and verified. Do not re-research; follow this procedure exactly.

**Store / theme**
- Live theme: "{data['scan']['theme_name']}", id `{data['scan']['theme_id']}` (gid://shopify/OnlineStoreTheme/{data['scan']['theme_id']}).
- Files touched: {', '.join('`assets/' + f + '`' for f in data['scan']['baseline'])}.
- Baseline md5 of each file when the scan read it:
""")
for f, m in data['scan']['baseline'].items():
    w(f"  - `assets/{f}`: `{m}`")
w(f"""
**Rules (non-negotiable)**
1. Get the CURRENT live file first. Never edit an old copy (assets/tlv-owner-overrides.css warns that a stale save already destroyed owner work once).
2. Only remove the exact text listed for an item. `findings.json` -> `items[].parts[]` is authoritative (the README blocks below are for reading and may be shortened). Context lines are only for locating; they stay.
3. If an item's exact text is not found exactly once in the live file, SKIP it, set its status to `SKIPPED: <reason>` and tell the user. Never adapt or guess.
4. Never "repair" dead code (for example by adding a missing `/*` or fixing a selector). Repairs switch on styles that were never live and visibly change the site. Only delete.
5. Ask Ziko before saving anything to the live theme. Show him the list of item ids you will apply and the verification result.
6. Do not touch anything that is not a TODO item here.

**Procedure**
1. Pull the live files into a working folder, e.g. with Shopify CLI:
   `shopify theme pull --theme {data['scan']['theme_id']} --only assets/toylvia.css --only assets/tlv-owner-overrides.css --only assets/home-palette.css --only assets/card-look.css --path ./theme-live`
   (add `--store <store>.myshopify.com` if the CLI asks). If the CLI is not available, ask Ziko to copy the file contents from Shopify admin, or ask him to do the deletions manually using the anchors below.
2. Make a backup copy of each file you will edit (e.g. `toylvia.before.css`).
3. Compare md5 with the baseline above. If it differs, the file was edited since the scan. Continue, but rule 3 protects you.
4. For each TODO item, in order:
   - `python toylvia-css-cleanup/tools/apply.py ./theme-live/assets/<file> <ID>` (use `--dry-run` first if unsure)
   - It refuses unless the exact text occurs once.
5. Verify each edited file against its backup:
   `node toylvia-css-cleanup/tools/cssom.js compare toylvia.before.css ./theme-live/assets/toylvia.css`
   - Needs Chrome. If not auto-detected, set `CHROME` (macOS: `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`, Windows: `C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe`).
   - Each item's **Verify** line is the measured result of applying that item alone to the baseline file.
   - If every item you applied to a file says `IDENTICAL`, the whole file must compare `IDENTICAL`.
   - Otherwise the output may only contain the `removed` / `added` rules listed in the Verify lines of the items you applied to that file. Nothing else.
   - If anything else appears, stop, restore the backup, tell Ziko.
6. After Ziko approves, push only the edited files:
   `shopify theme push --theme {data['scan']['theme_id']} --only assets/toylvia.css --path ./theme-live --allow-live`
   (the Shopify MCP connector blocks writes to the live theme, so it will not work for this.)
7. Re-pull the file and confirm the live copy equals your edited copy (md5).
8. Update `findings.json` statuses (`DONE` / `SKIPPED: reason`), run `python toylvia-css-cleanup/tools/render.py`, commit and push.

---

## Findings
""")
import re
def short(t):
    t = re.sub(r'\s+', ' ', t.strip())
    return t if len(t) <= 90 else t[:87] + '...'

for i in items:
    w(f"### {i['id']} [{i['status']}] {i['title']}")
    w(f"- **File:** `{i['file']}` | baseline lines {i['baseline_lines']} | kind: {i['kind']}")
    w(f"- **Why it is dead:** {i['why']}")
    w(f"- **Proof:** {i['proof']}")
    w(f"- **Verify:** expected `cssom.js compare` result for this item alone: **{i['verify']}**")
    w(f"- **Visual change if removed:** {i['visual_change']}")
    if i.get('notes'):
        w(f"- **Notes:** {i['notes']}")
    w(f"- **Parts:** {len(i['parts'])} (apply.py handles all parts of an item at once)")
    w('')
    for n, part in enumerate(i['parts'], 1):
        nb = [l for l in part['exact_text'].split('\n') if l.strip()]
        label = f"Part {n}" if len(i['parts']) > 1 else 'Exact text'
        w(f"**{label}** (baseline lines {part['lines']}). Manual anchor: from `{short(nb[0])}` to `{short(nb[-1])}`.")
        if part['context_before'] or part['context_after']:
            w('This text also exists elsewhere in the file, so it is located by the neighbouring lines '
              '(kept, not deleted): before = `' + short(part['context_before'] or '(none)') + '`, after = `' + short(part['context_after'] or '(none)') + '`.')
        if 'replacement' in part:
            w('Replace with: `' + part['replacement'].strip() + '` (keeps the parent rule closed).')
        else:
            w('Delete:')
        w(fence(part['exact_text']))
        w('')

if data.get('do_not_apply'):
    w('---\n\n## Known issues that are NOT deletions (do not apply without asking Ziko)\n')
    for d in data['do_not_apply']:
        w(f"- **{d['title']}**: {d['text']}")
    w('')

(ROOT / 'README.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
print(f'README.md written: {len(items)} items, {len(todo)} TODO')
