# Toylvia CSS cleanup

Dead and commented-out CSS found in the live theme of https://toylvia.com by a cloud Claude scan.
Every item was found by one agent and then attacked by a separate skeptic agent that tried to prove it still affects the page. Only items that survived are listed.

- Scan started: 2026-10-11T15:16:39Z | last update: 2026-10-11T15:19:58Z | rounds: 0
- Items: **9** total, **8 TODO** (proven safe), **1 REVIEW** (very likely safe, ask Ziko first)
- Status legend: `TODO` apply | `REVIEW` apply only if Ziko says yes | `DONE` applied and verified | `SKIPPED: reason`

---

## For Ziko (what you do)

1. On your computer, open this repo and get the branch: `git fetch origin && git checkout claude/chrome-devtools-state-preservation-o47p8j && git pull`
2. Open Claude (desktop / Claude Code) in this repo and say:
   **"Read toylvia-css-cleanup/README.md and apply the TODO items to the live theme."**
   (Add "and the REVIEW items" if you also want those.)
3. Claude will ask before it saves anything to the live theme. Say yes after you have read its summary.
4. If Claude cannot push to Shopify, it will tell you the exact lines to delete in Shopify admin (Online Store, Themes, Edit code).

---

## For Claude (desktop): what you need to do

You are applying a cleanup that was already researched and verified. Do not re-research; follow this procedure exactly.

**Store / theme**
- Live theme: "lior's theme for toylvia", id `209157554507` (gid://shopify/OnlineStoreTheme/209157554507).
- Files touched: `assets/toylvia.css`, `assets/tlv-owner-overrides.css`, `assets/home-palette.css`, `assets/card-look.css`.
- Baseline md5 of each file when the scan read it:

  - `assets/toylvia.css`: `efc069df951128a76ac1adb542f17234`
  - `assets/tlv-owner-overrides.css`: `85a3bd4e370256a4f8dd92b7939a3531`
  - `assets/home-palette.css`: `01f05408f5ad9004afeb97c14313d787`
  - `assets/card-look.css`: `80c3701d5039636bd309a2760a3363b8`

**Rules (non-negotiable)**
1. Get the CURRENT live file first. Never edit an old copy (assets/tlv-owner-overrides.css warns that a stale save already destroyed owner work once).
2. Only remove the exact text listed for an item. `findings.json` -> `items[].exact_text` is authoritative (the README blocks below are for reading and may be shortened).
3. If an item's exact text is not found exactly once in the live file, SKIP it, set its status to `SKIPPED: <reason>` and tell the user. Never adapt or guess.
4. Never "repair" dead code (for example by adding a missing `/*` or fixing a selector). Repairs switch on styles that were never live and visibly change the site. Only delete.
5. Ask Ziko before saving anything to the live theme. Show him the list of item ids you will apply and the verification result.
6. Do not touch anything that is not a TODO item here.

**Procedure**
1. Pull the live files into a working folder, e.g. with Shopify CLI:
   `shopify theme pull --theme 209157554507 --only assets/toylvia.css --only assets/tlv-owner-overrides.css --only assets/home-palette.css --only assets/card-look.css --path ./theme-live`
   (add `--store <store>.myshopify.com` if the CLI asks). If the CLI is not available, ask Ziko to copy the file contents from Shopify admin, or ask him to do the deletions manually using the anchors below.
2. Make a backup copy of each file you will edit (e.g. `toylvia.before.css`).
3. Compare md5 with the baseline above. If it differs, the file was edited since the scan. Continue, but rule 3 protects you.
4. For each TODO item, in order:
   - `python toylvia-css-cleanup/tools/apply.py ./theme-live/assets/<file> <ID>` (use `--dry-run` first if unsure)
   - It refuses unless the exact text occurs once.
5. Verify each edited file against its backup:
   `node toylvia-css-cleanup/tools/cssom.js compare toylvia.before.css ./theme-live/assets/toylvia.css`
   - Needs Chrome. If not auto-detected, set `CHROME` (macOS: `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`, Windows: `C:\Program Files\Google\Chrome\Application\chrome.exe`).
   - Each item's **Verify** line is the measured result of applying that item alone to the baseline file.
   - If every item you applied to a file says `IDENTICAL`, the whole file must compare `IDENTICAL`.
   - Otherwise the output may only contain the `removed` / `added` rules listed in the Verify lines of the items you applied to that file. Nothing else.
   - If anything else appears, stop, restore the backup, tell Ziko.
6. After Ziko approves, push only the edited files:
   `shopify theme push --theme 209157554507 --only assets/toylvia.css --path ./theme-live --allow-live`
   (the Shopify MCP connector blocks writes to the live theme, so it will not work for this.)
7. Re-pull the file and confirm the live copy equals your edited copy (md5).
8. Update `findings.json` statuses (`DONE` / `SKIPPED: reason`), run `python toylvia-css-cleanup/tools/render.py`, commit and push.

---

## Findings

### T01 [TODO] Cart quantity/remove button rules using :contains() (never valid CSS)
- **File:** `assets/toylvia.css` | baseline lines 2438-2486 | kind: parser-dropped rules
- **Anchor (to find it in Shopify admin):** starts at `/* 2. Neumorphic Quantity Buttons (+ and -) */`, ends with `}`
- **Why it is dead:** All three rules (+/- quantity links, quantity number, REMOVE link) use `:contains()` in every selector. `:contains()` exists only in jQuery, no browser supports it in CSS, and one invalid selector invalidates the whole rule, so Chrome drops all three rules (33 !important declarations). They have never applied.
- **Proof:** grep shows `:contains(` only on baseline lines 2439-2441, 2458-2460, 2474. The rules are top level (brace depth 0). Headless Chrome keeps 881 top-level rules with or without this block, byte-identical. A control test (removing the live checkout rule right after it) is detected (880).
- **Verify:** expected `cssom.js compare` result for this item alone: **IDENTICAL: Chrome keeps exactly the same rules in the same order. No visual change is possible.**
- **Visual change if removed:** None. Keep the `/* 5. Neumorphic Checkout Button` rule that follows: it is live.
- **Notes:** Ziko may already have deleted this manually in Shopify admin. If apply.py says the text is not found, check whether the block is already gone; if so mark DONE.

Exact text to delete:
```css
/* 2. Neumorphic Quantity Buttons (+ and -) */
#MainContent a:contains("+"), 
#MainContent a:contains("−"), 
#MainContent a:contains("-") {
    display: inline-flex !important;
    justify-content: center !important;
    align-items: center !important;
    width: 32px !important;
    height: 32px !important;
    background: #ffffff !important;
    border-radius: 10px !important;
    box-shadow: 4px 4px 8px rgba(0, 0, 0, 0.08), -4px -4px 8px rgba(255, 255, 255, 1) !important;
    color: #000000 !important;
    text-decoration: none !important;
    font-weight: bold !important;
    margin: 5px !important;
    border: none !important;
}

/* 3. Neumorphic Quantity Number (Recessed look) */
#MainContent span:has(+ a:contains("+")),
#MainContent a:contains("−") + span,
#MainContent a:contains("-") + span {
    display: inline-flex !important;
    justify-content: center !important;
    align-items: center !important;
    width: 40px !important;
    height: 32px !important;
    background: #f8f8f8 !important;
    border-radius: 8px !important;
    box-shadow: inset 2px 2px 5px rgba(255, 255, 255, 0.05), inset -2px -2px 5px rgba(255, 255, 255, 1) !important;
    color: #000000 !important;
    font-weight: bold !important;
}

/* 4. Neumorphic Remove Button */
#MainContent a:contains("REMOVE") {
    color: #000000 !important;
    background: #ffffff !important;
    padding: 6px 14px !important;
    border-radius: 12px !important;
    font-size: 11px !important;
    text-decoration: none !important;
    text-transform: uppercase !important;
    display: inline-block !important;
    box-shadow: 4px 4px 8px rgba(0, 0, 0, 0.06), -4px -4px 8px rgba(255, 255, 255, 0.9) !important;
    margin-left: 15px !important;
}
```

### T02 [TODO] .site-header rule swallowed by a comment that lost its opening /*
- **File:** `assets/toylvia.css` | baseline lines 3482-3498 | kind: parser-dropped rule
- **Anchor (to find it in Shopify admin):** starts at `GLASSMORPHIC ADVANCED NAVIGATION SYSTEM — Toylvia`, ends with `}`
- **Why it is dead:** The banner comment 'GLASSMORPHIC ADVANCED NAVIGATION SYSTEM' is missing its opening `/*`. Its text (`GLASSMORPHIC ... ==== */`) becomes part of the next selector, which is invalid, so Chrome drops the whole `.site-header { position: sticky; ... padding: 8px 18px; z-index: 50; }` rule.
- **Proof:** Verified by two agents and headless Chrome: the rule is absent from the parsed rule list; removing these lines leaves Chrome's rule list identical (see Verify).
- **Verify:** expected `cssom.js compare` result for this item alone: **IDENTICAL: Chrome keeps exactly the same rules in the same order. No visual change is possible.**
- **Visual change if removed:** None.
- **Notes:** Do NOT fix it by adding the missing `/*`. That would switch on a .site-header rule that has never been live and change the header.

Exact text to delete:
```css
   GLASSMORPHIC ADVANCED NAVIGATION SYSTEM — Toylvia
   ========================================================== */
.site-header {
  position: sticky;
  top: 0;
  margin: 0;
  width: 100%;
  max-width: 100%;
  background: transparent !important;
  backdrop-filter: none !important;
  -webkit-backdrop-filter: none !important;
  border: none !important;
  border-radius: 0 !important;
  box-shadow: none !important;
  padding: 8px 18px;
  z-index: 50;
}
```

### T03 [TODO] First of two identical @keyframes marquee definitions
- **File:** `assets/toylvia.css` | baseline lines 978-981 | kind: shadowed duplicate @keyframes
- **Anchor (to find it in Shopify admin):** starts at `@keyframes marquee {`, ends with `}`
- **Why it is dead:** `@keyframes marquee` is defined twice at top level (baseline 978-981 and 3021-3028). When names repeat, only the last definition is used, so this one never runs. Both definitions are identical (translateX(0) to translateX(-50%)).
- **Proof:** Brace-depth scan: both at depth 0, before the unclosed @media. No @layer/@supports/@container in the file. Only consumer: `.announcement-bar .announcement-bar__track { animation: marquee 22s linear infinite !important }`.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @keyframes marquee {  /   0% { transform: translateX(0px); } /   100% { transform: translateX(-50%); } / }**
- **Visual change if removed:** None. Keep the `/* === KEYFRAMES === */` comment and `@keyframes trustIconBounce` that follow.

Exact text to delete:
```css
@keyframes marquee {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
```

### T04 [TODO] Empty rule `.category-sphere:hover .category-sphere__ball {  }` and its orphan comment
- **File:** `assets/toylvia.css` | baseline lines 2109-2110 | kind: empty rule
- **Anchor (to find it in Shopify admin):** starts at `/* === CATEGORY SPHERE HOVER GLOW === */`, ends with `.category-sphere:hover .category-sphere__ball { }`
- **Why it is dead:** The rule has no declarations, so it cannot do anything. (Its target is also hidden: `.category-sphere { display: none !important }` in the V14 block.)
- **Proof:** Rule body is only whitespace. Top level, depth 0.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .category-sphere:hover .category-sphere__ball { }**
- **Visual change if removed:** None. Keep line 2108 `/* === PRODUCT CARD BADGE COLORS === */`, it labels the badge rules below.

Exact text to delete:
```css
/* === CATEGORY SPHERE HOVER GLOW === */
.category-sphere:hover .category-sphere__ball {  }
```

### T05 [TODO] Empty rule `.clg-hero canvas, .clg-grid { }` ('GRID PANEL FADED EDGES')
- **File:** `assets/toylvia.css` | baseline lines 4992-4997 | kind: empty rule
- **Anchor (to find it in Shopify admin):** starts at `/* === GRID PANEL FADED EDGES === */`, ends with `}`
- **Why it is dead:** The rule body is a blank line, no declarations. The faded-edge effect it was for was removed long ago.
- **Proof:** Top level, depth 0. Real styling for these elements lives at `.clg-grid` and `#clg-hero, .clg-hero` in the V14 block.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .clg-hero canvas, .clg-grid { }**
- **Visual change if removed:** None.

Exact text to delete:
```css
/* === GRID PANEL FADED EDGES === */
.clg-hero canvas,
.clg-grid {

}
```

### T06 [TODO] `#MainContent > .shopify-section:first-child { background: #e5efea !important }` always loses
- **File:** `assets/home-palette.css` | baseline lines 25-27 | kind: cascade-dead rule
- **Anchor (to find it in Shopify admin):** starts at `html body #MainContent > .shopify-section:first-child {`, ends with `}`
- **Why it is dead:** Its only declaration always loses to rules in the same file that match the same element: line 78 (same specificity, later, also !important) and line 310 (`#MainContent` x48 `>.shopify-section:first-child{background:#f2f2f2!important}`, far higher specificity). #e5efea never renders.
- **Proof:** Same file, so stylesheet load order does not matter. No media queries involved. Checked in headless Chrome by changing the value to a sentinel: computed background unchanged.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: html body #MainContent > .shopify-section:first-child { background: rgb(229, 239, 234) !important; }**
- **Visual change if removed:** None (the section stays #f2f2f2).

Exact text to delete:
```css
html body #MainContent > .shopify-section:first-child {
  background: #e5efea !important;
}
```

### T07 [TODO] `.cr-card__img-wrap > .cr-card__tag { border-radius: 50% !important }` duplicated by a stronger copy
- **File:** `assets/home-palette.css` | baseline lines 275-277 | kind: cascade-dead rule (duplicate)
- **Anchor (to find it in Shopify admin):** starts at `html body .cat-rows .cr-card__img-wrap > .cr-card__tag {`, ends with `}`
- **Why it is dead:** Lines 278-281 match exactly the same elements (`.cr-card__tag` repeated 12 times) with the same `border-radius: 50% !important`, at much higher specificity (0,14,2 vs 0,3,2).
- **Proof:** Same combinators, same declaration, same file, no media query. Checked in headless Chrome with a sentinel value at 9 widths: computed value unchanged.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: html body .cat-rows .cr-card__img-wrap > .cr-card__tag { border-radius: 50% !important; }**
- **Visual change if removed:** None (tags stay round via lines 278-281).

Exact text to delete:
```css
html body .cat-rows .cr-card__img-wrap > .cr-card__tag {
  border-radius: 50% !important;
}
```

### T08 [TODO] `.announcement-bar.announcement-bar { background: #f1fbfa }` duplicated by a stronger copy
- **File:** `assets/card-look.css` | baseline lines 177-178 | kind: cascade-dead rule (duplicate)
- **Anchor (to find it in Shopify admin):** starts at `html body .announcement-bar.announcement-bar{background:#f1fbfa!important;background-im...`, ends with `html body .announcement-bar.announcement-bar{background:#f1fbfa!important;background-im...`
- **Why it is dead:** Line 181 has the same two declarations (`background:#f1fbfa!important; background-image:none!important`) for the same element with higher specificity (class repeated 7 times vs 2).
- **Proof:** Same file, no media query, both !important. Checked in headless Chrome with a sentinel value: computed value unchanged.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: html body .announcement-bar.announcement-bar { background: none rgb(241, 251, 250) !important; }**
- **Visual change if removed:** None. Keep the comment on line 175 and the stronger rule on line 181.

Exact text to delete:
```css
html body .announcement-bar.announcement-bar{background:#f1fbfa!important;background-image:none!important}
```

### T09 [REVIEW] `.all-products-btn:hover` accidentally nested inside `.all-products-btn`
- **File:** `assets/toylvia.css` | baseline lines 2144-2152 | kind: accidental nesting (never-matching selector)
- **Anchor (to find it in Shopify admin):** starts at `.all-products-btn:hover {`, ends with `}}`
- **Why it is dead:** The `.all-products-btn {` rule is not closed before the hover rule, so the hover rule is nested. With CSS nesting it means `.all-products-btn .all-products-btn:hover` (a button inside a button), which the theme markup never has. The intended hover style (gradient border, scale 1.12) has never applied.
- **Proof:** Headless Chrome serializes it as `& .all-products-btn:hover` inside `.all-products-btn`. Theme markup uses .all-products-btn without nesting (index sections and templates/404.liquid).
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .all-products-btn { /   color: rgb(12, 12, 12) !important; letter-spacing: normal !important; animation: auto ease 0s 1 normal none running none !important; padding: 1.016rem 2.71rem !important; font-size: 17.618px !important; background: linear-gradient(rgb(249, 250, 251), rgb(249, 250, 251)) padding /   - removed: CSSStyleRule(.all-products-btn) > & .all-products-btn:hover { color: rgb(12, 12, 12) !important; border: 1px solid transparent !important; background: linear-gradient(rgb(249, 250, 251), rgb(249, 250, 251)) padding-box padding-box, linear-gradient(135deg, rgb(255, 41, 148), rgb(33, 213, 237)) border /   + added:   .all-products-btn { color: rgb(12, 12, 12) !important; letter-spacing: normal !important; animation: auto ease 0s 1 normal none running none !important; padding: 1.016rem 2.71rem !important; font-size: 17.618px !important; background: linear-gradient(rgb(249, 250, 251), rgb(249, 250, 251)) padding-b**
- **Visual change if removed:** None expected. HIGH confidence, not mathematically proven: it depends on markup (an app could in theory inject nested buttons).
- **Notes:** REVIEW: ask Ziko first. The edit replaces the nested block with a single `}` that closes the parent rule, so the parent's own declarations stay exactly the same.

Exact text to delete:
```css
                                      .all-products-btn:hover {
                                        color: rgb(12, 12, 12) !important;
border: 1px solid transparent !important;
background:
  linear-gradient(rgb(249, 250, 251), rgb(249, 250, 251)) padding-box,
  linear-gradient(135deg, rgb(255, 41, 148), rgb(33, 213, 237)) border-box !important;
box-shadow: none !important;
transform: scale(1.12) !important;
                                      }}
```

---

## Known issues that are NOT deletions (do not apply without asking Ziko)

- **Unclosed @media in toylvia.css (real bug, but fixing it CHANGES the site)**: Baseline line ~5535 opens `@media (max-width: 1024px) {` with a dangling `.cat-ice-label` selector and never closes it. Everything after it (about 670 lines: outlined Add to Cart pill, transparent header, free shipping bar, cart bundle, badge colours, mobile crash fix, ...) only applies at widths <= 1024px. Fixing it would switch those styles ON for desktop. Ask Ziko whether he wants that before touching it.
- **Ziko's DevTools edits to homepage product rows (pending his decision)**: Earlier in the cloud session Ziko unticked declarations at mobile width in assets/tlv-owner-overrides.css (tlv-row-header-gap translateY(18px); tlv-row-spacing row margins/paddings, the clamp() row gap and header padding/margin; tlv-header-shift translateY(9px); tlv-header-no-padding mobile block; tlv-row-unite mobile block) and in assets/home-palette.css (.cat-rows__row margin 0 1.25rem 0 and padding 0). Several are not inside a media query, so applying them as-is also changes desktop. Recommendation given: apply them inside @media(max-width:767px) only. He has not decided yet. Do not apply without asking.

