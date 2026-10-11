# Toylvia CSS cleanup

Dead and commented-out CSS found in the live theme of https://toylvia.com by a cloud Claude scan.
Every item was found by one agent and then attacked by a separate skeptic agent that tried to prove it still affects the page. Only items that survived are listed.

- Scan started: 2026-10-11T15:16:39Z | last update: 2026-10-11T16:04:48Z | rounds: 3
- Items: **56** total, **38 TODO** (proven safe), **18 REVIEW** (very likely safe, ask Ziko first)
- Lines removed if every item is applied (superseding items instead of the ones they contain): 1953 | TODO items only: 707
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
- Files touched: `assets/toylvia.css`, `assets/tlv-owner-overrides.css`, `assets/home-palette.css`, `assets/card-look.css`, `assets/live-card-fixes.css`, `assets/card-markers.css`.
- Baseline md5 of each file when the scan read it:

  - `assets/toylvia.css`: `efc069df951128a76ac1adb542f17234`
  - `assets/tlv-owner-overrides.css`: `85a3bd4e370256a4f8dd92b7939a3531`
  - `assets/home-palette.css`: `01f05408f5ad9004afeb97c14313d787`
  - `assets/card-look.css`: `80c3701d5039636bd309a2760a3363b8`
  - `assets/live-card-fixes.css`: `35cf670e3bcd601f2d54a49ed3e57448`
  - `assets/card-markers.css`: `c447cc9f8b7e86be72bc5416aa421296`

**Rules (non-negotiable)**
1. Get the CURRENT live file first. Never edit an old copy (assets/tlv-owner-overrides.css warns that a stale save already destroyed owner work once).
2. Only remove the exact text listed for an item. `findings.json` -> `items[].parts[]` is authoritative (the README blocks below are for reading and may be shortened). Context lines are only for locating; they stay.
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
4. Decide the list first: all TODO items, plus the REVIEW items Ziko approved. If an approved item `supersedes` other items, drop those from the list (it contains them). Then for each item, in order (superseding items first):
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
- **Why it is dead:** All three rules (+/- quantity links, quantity number, REMOVE link) use `:contains()` in every selector. `:contains()` exists only in jQuery, no browser supports it in CSS, and one invalid selector invalidates the whole rule, so Chrome drops all three rules (33 !important declarations). They have never applied.
- **Proof:** grep shows `:contains(` only on baseline lines 2439-2441, 2458-2460, 2474. The rules are top level (brace depth 0). Headless Chrome keeps 881 top-level rules with or without this block, byte-identical. A control test (removing the live checkout rule right after it) is detected (880).
- **Verify:** expected `cssom.js compare` result for this item alone: **IDENTICAL: Chrome keeps exactly the same rules in the same order. No visual change is possible.**
- **Visual change if removed:** None. Keep the `/* 5. Neumorphic Checkout Button` rule that follows: it is live.
- **Notes:** Ziko may already have deleted this manually in Shopify admin. If apply.py says the text is not found, check whether the block is already gone; if so mark DONE.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 2438-2486). Manual anchor: from `/* 2. Neumorphic Quantity Buttons (+ and -) */` to `}`.
Delete:
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
- **Why it is dead:** The banner comment 'GLASSMORPHIC ADVANCED NAVIGATION SYSTEM' is missing its opening `/*`. Its text (`GLASSMORPHIC ... ==== */`) becomes part of the next selector, which is invalid, so Chrome drops the whole `.site-header { position: sticky; ... padding: 8px 18px; z-index: 50; }` rule.
- **Proof:** Verified by two agents and headless Chrome: the rule is absent from the parsed rule list; removing these lines leaves Chrome's rule list identical (see Verify).
- **Verify:** expected `cssom.js compare` result for this item alone: **IDENTICAL: Chrome keeps exactly the same rules in the same order. No visual change is possible.**
- **Visual change if removed:** None.
- **Notes:** Do NOT fix it by adding the missing `/*`. That would switch on a .site-header rule that has never been live and change the header.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 3482-3498). Manual anchor: from `GLASSMORPHIC ADVANCED NAVIGATION SYSTEM — Toylvia` to `}`.
Delete:
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
- **Why it is dead:** `@keyframes marquee` is defined twice at top level (baseline 978-981 and 3021-3028). When names repeat, only the last definition is used, so this one never runs. Both definitions are identical (translateX(0) to translateX(-50%)).
- **Proof:** Brace-depth scan: both at depth 0, before the unclosed @media. No @layer/@supports/@container in the file. Only consumer: `.announcement-bar .announcement-bar__track { animation: marquee 22s linear infinite !important }`.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @keyframes marquee { 0% { transform: translateX(0px); } 100% { transform: translateX(-50%); } }**
- **Visual change if removed:** None. Keep the `/* === KEYFRAMES === */` comment and `@keyframes trustIconBounce` that follow.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 978-981). Manual anchor: from `@keyframes marquee {` to `}`.
Delete:
```css
@keyframes marquee {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
```

### T04 [TODO] Empty rule `.category-sphere:hover .category-sphere__ball {  }` and its orphan comment
- **File:** `assets/toylvia.css` | baseline lines 2109-2110 | kind: empty rule
- **Why it is dead:** The rule has no declarations, so it cannot do anything. (Its target is also hidden: `.category-sphere { display: none !important }` in the V14 block.)
- **Proof:** Rule body is only whitespace. Top level, depth 0.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .category-sphere:hover .category-sphere__ball {  }**
- **Visual change if removed:** None. Keep line 2108 `/* === PRODUCT CARD BADGE COLORS === */`, it labels the badge rules below.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 2109-2110). Manual anchor: from `/* === CATEGORY SPHERE HOVER GLOW === */` to `.category-sphere:hover .category-sphere__ball { }`.
Delete:
```css
/* === CATEGORY SPHERE HOVER GLOW === */
.category-sphere:hover .category-sphere__ball {  }
```

### T05 [TODO] Empty rule `.clg-hero canvas, .clg-grid { }` ('GRID PANEL FADED EDGES')
- **File:** `assets/toylvia.css` | baseline lines 4992-4997 | kind: empty rule
- **Why it is dead:** The rule body is a blank line, no declarations. The faded-edge effect it was for was removed long ago.
- **Proof:** Top level, depth 0. Real styling for these elements lives at `.clg-grid` and `#clg-hero, .clg-hero` in the V14 block.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .clg-hero canvas, .clg-grid {  }**
- **Visual change if removed:** None.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 4992-4997). Manual anchor: from `/* === GRID PANEL FADED EDGES === */` to `}`.
Delete:
```css
/* === GRID PANEL FADED EDGES === */
.clg-hero canvas,
.clg-grid {

}
```

### T06 [TODO] `#MainContent > .shopify-section:first-child { background: #e5efea !important }` always loses
- **File:** `assets/home-palette.css` | baseline lines 25-27 | kind: cascade-dead rule
- **Why it is dead:** Its only declaration always loses to rules in the same file that match the same element: line 78 (same specificity, later, also !important) and line 310 (`#MainContent` x48 `>.shopify-section:first-child{background:#f2f2f2!important}`, far higher specificity). #e5efea never renders.
- **Proof:** Same file, so stylesheet load order does not matter. No media queries involved. Checked in headless Chrome by changing the value to a sentinel: computed background unchanged.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: html body #MainContent > .shopify-section:first-child { background: rgb(229, 239, 234) !important; }**
- **Visual change if removed:** None (the section stays #f2f2f2).
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 25-27). Manual anchor: from `html body #MainContent > .shopify-section:first-child {` to `}`.
Delete:
```css
html body #MainContent > .shopify-section:first-child {
  background: #e5efea !important;
}
```

### T07 [TODO] `.cr-card__img-wrap > .cr-card__tag { border-radius: 50% !important }` duplicated by a stronger copy
- **File:** `assets/home-palette.css` | baseline lines 275-277 | kind: cascade-dead rule (duplicate)
- **Why it is dead:** Lines 278-281 match exactly the same elements (`.cr-card__tag` repeated 12 times) with the same `border-radius: 50% !important`, at much higher specificity (0,14,2 vs 0,3,2).
- **Proof:** Same combinators, same declaration, same file, no media query. Checked in headless Chrome with a sentinel value at 9 widths: computed value unchanged.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: html body .cat-rows .cr-card__img-wrap > .cr-card__tag { border-radius: 50% !important; }**
- **Visual change if removed:** None (tags stay round via lines 278-281).
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 275-277). Manual anchor: from `html body .cat-rows .cr-card__img-wrap > .cr-card__tag {` to `}`.
Delete:
```css
html body .cat-rows .cr-card__img-wrap > .cr-card__tag {
  border-radius: 50% !important;
}
```

### T08 [TODO] `.announcement-bar.announcement-bar { background: #f1fbfa }` duplicated by a stronger copy
- **File:** `assets/card-look.css` | baseline lines 177-178 | kind: cascade-dead rule (duplicate)
- **Why it is dead:** Line 181 has the same two declarations (`background:#f1fbfa!important; background-image:none!important`) for the same element with higher specificity (class repeated 7 times vs 2).
- **Proof:** Same file, no media query, both !important. Checked in headless Chrome with a sentinel value: computed value unchanged.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: html body .announcement-bar.announcement-bar { background: none rgb(241, 251, 250) !important; }**
- **Visual change if removed:** None. Keep the comment on line 175 and the stronger rule on line 181.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 177-178). Manual anchor: from `html body .announcement-bar.announcement-bar{background:#f1fbfa!important;background-im...` to `html body .announcement-bar.announcement-bar{background:#f1fbfa!important;background-im...`.
Delete:
```css
html body .announcement-bar.announcement-bar{background:#f1fbfa!important;background-image:none!important}
```

### T09 [REVIEW] `.all-products-btn:hover` accidentally nested inside `.all-products-btn`
- **File:** `assets/toylvia.css` | baseline lines 2144-2152 | kind: accidental nesting (never-matching selector)
- **Why it is dead:** The `.all-products-btn {` rule is not closed before the hover rule, so the hover rule is nested. With CSS nesting it means `.all-products-btn .all-products-btn:hover` (a button inside a button), which the theme markup never has. The intended hover style (gradient border, scale 1.12) has never applied.
- **Proof:** Headless Chrome serializes it as `& .all-products-btn:hover` inside `.all-products-btn`. Theme markup uses .all-products-btn without nesting (index sections and templates/404.liquid).
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .all-products-btn > & .all-products-btn:hover { color: rgb(12, 12, 12) !important; border: 1px solid transparent !important; background: linear-gradient(rgb(249, 250, 251), rgb(249, 250, 251)) padding-box padding-box, linear-gradient(135deg, rgb(255, 41, 148), rgb(33, 213, 237)) border-box border-bo**
- **Visual change if removed:** None expected. HIGH confidence, not mathematically proven: it depends on markup (an app could in theory inject nested buttons).
- **Notes:** REVIEW: ask Ziko first. The edit replaces the nested block with a single `}` that closes the parent rule, so the parent's own declarations stay exactly the same.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 2144-2152). Manual anchor: from `.all-products-btn:hover {` to `}}`.
Replace with: `}` (keeps the parent rule closed).
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

### T10 [TODO] Old drafts of the category-sphere ball styles, fully re-declared later (7 rules, 69 lines)
- **File:** `assets/toylvia.css` | baseline lines 4354-4376, 4568-4598, 4635-4649 | kind: same-file overridden duplicates
- **Why it is dead:** Seven `.category-sphere__ball` / icon rules (pink ring + hover, centred icon + hover, glass fill, ::before inherit, 'Pill' hover) are each re-declared later in the same file with the same selector and !important for every property, so the earlier copies can never win. Two of them are byte-identical to the later copies at baseline 4599-4632.
- **Proof:** Static shadow proof (headless Chrome CSSOM): each of the 7 removed rules has a later kept rule with an identical selector, same-or-top-level scope and the same longhands at equal-or-higher priority -> PROVEN. A separate agent also compared computed styles at 7 widths with forced :hover: 0 differences in 192,192 checks. (Also: `.category-sphere` is display:none !important anyway.)
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: html body .category-sphere__ball { box-shadow: rgba(255, 66, 161, 0.55) 0px 0px 0px 1px, rgba(255, 66, 161, 0.45) 0px 0px 8px, rgba(255, 66, 161, 0.25) 0px 0px 18px, rgba(20, 30, 60, 0.16) 0px 18px 34px, rgba(20, 30, 60, 0.1) 0px 6px 12px, rgba(255, 255, 255, 0.9) 0px 2px 3px inset, rgba(80, 90, 120 /   - removed: html body .category-sphere:hover .category-sphere__ball, html body .category-sphere__ball:hover { box-shadow: rgba(255, 66, 161, 0) 0px 0px 0px 0px, rgba(255, 66, 161, 0) 0px 0px 0px, rgba(255, 66, 161, 0) 0px 0px 0px, rgba(30, 40, 70, 0.1) 0px 14px 32px, rgba(30, 40, 70, 0.06) 0px 4px 10px, rgba(25 /   - removed: html body .category-arc .category-sphere .category-sphere__ball .category-sphere__icon:not(#_x_) { position: absolute !important; inset: 50% auto auto 50% !important; margin: 0px !important; transform: translate(-50%, -50%) !important; transform-origin: center center !important; z-index: 2 !importan /   - removed: html body .category-arc .category-sphere:hover .category-sphere__ball .category-sphere__icon:not(#_x_) { transform: translate(-50%, -50%) !important; opacity: 0 !important; filter: blur(4px) !important; } /   - removed: html body .category-arc .category-sphere__ball { background: radial-gradient(circle at 30% 22%, rgba(255, 255, 255, 0.82) 0%, rgba(248, 250, 252, 0.78) 18%, rgba(232, 237, 243, 0.7) 58%, rgba(213, 221, 230, 0.65) 100%) !important; backdrop-filter: blur(6px) saturate(1.1) !important; } /   - removed: html body .category-arc .category-sphere__ball::before { background: inherit !important; } /   - removed: html body .category-arc .category-sphere:hover .category-sphere__ball { background: radial-gradient(circle at 30% 22%, rgba(255, 255, 255, 0.48) 0%, rgba(248, 250, 252, 0.42) 18%, rgba(232, 237, 243, 0.34) 58%, rgba(213, 221, 230, 0.28) 100%) !important; backdrop-filter: blur(10px) saturate(1.15) !i**
- **Visual change if removed:** None. The later rules that win (baseline ~4418-4428, 4599-4632, 4784-4795) stay.
- **Parts:** 3 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 4354-4376). Manual anchor: from `/* Sphere: thin glowing pink ring idle, fades to 0 on hover */` to `}`.
Delete:
```css
/* Sphere: thin glowing pink ring idle, fades to 0 on hover */
html body .category-sphere__ball {
  box-shadow:
    0 0 0 1px rgba(255, 66, 161, 0.55),
    0 0 8px rgba(255, 66, 161, 0.45),
    0 0 18px rgba(255, 66, 161, 0.25),
    0 18px 34px rgba(20, 30, 60, 0.16),
    0 6px 12px rgba(20, 30, 60, 0.10),
    inset 0 2px 3px rgba(255, 255, 255, 0.9),
    inset 0 -10px 20px rgba(80, 90, 120, 0.18),
    inset 4px 4px 8px rgba(255, 255, 255, 0.35) !important;
}
html body .category-sphere:hover .category-sphere__ball,
html body .category-sphere__ball:hover {
  box-shadow:
    0 0 0 0px rgba(255, 66, 161, 0),
    0 0 0 rgba(255, 66, 161, 0),
    0 0 0 rgba(255, 66, 161, 0),
    0 14px 32px rgba(30, 40, 70, 0.10),
    0 4px 10px rgba(30, 40, 70, 0.06),
    inset 0 1px 0 rgba(255, 255, 255, 0.9),
    inset 0 -6px 14px rgba(200, 210, 225, 0.35) !important;
}
```

**Part 2** (baseline lines 4568-4598). Manual anchor: from `/* --- Icon: perfectly centered with high-specificity override -------- */` to `}`.
Delete:
```css
/* --- Icon: perfectly centered with high-specificity override -------- */
html body .category-arc .category-sphere .category-sphere__ball .category-sphere__icon:not(#_x_) {
  position: absolute !important;
  left: 50% !important;
  top: 50% !important;
  right: auto !important;
  bottom: auto !important;
  margin: 0 !important;
  transform: translate(-50%, -50%) !important;
  transform-origin: center center !important;
  z-index: 2 !important;
}
html body .category-arc .category-sphere:hover .category-sphere__ball .category-sphere__icon:not(#_x_) {
  transform: translate(-50%, -50%) !important;
  opacity: 0 !important;
  filter: blur(4px) !important;
}

/* --- Sphere: slightly transparent glass fill ----------------------- */
html body .category-arc .category-sphere__ball {
  background: radial-gradient(circle at 30% 22%,
    rgba(255, 255, 255, 0.82) 0%,
    rgba(248, 250, 252, 0.78) 18%,
    rgba(232, 237, 243, 0.70) 58%,
    rgba(213, 221, 230, 0.65) 100%) !important;
  backdrop-filter: blur(6px) saturate(1.1) !important;
  -webkit-backdrop-filter: blur(6px) saturate(1.1) !important;
}
html body .category-arc .category-sphere__ball::before {
  background: inherit !important;
}
```

**Part 3** (baseline lines 4635-4649). Manual anchor: from `/* Pill (hover-morphed state): extra translucent glass */` to `}`.
Delete:
```css
/* Pill (hover-morphed state): extra translucent glass */
html body .category-arc .category-sphere:hover .category-sphere__ball {
  background: radial-gradient(circle at 30% 22%,
    rgba(255, 255, 255, 0.48) 0%,
    rgba(248, 250, 252, 0.42) 18%,
    rgba(232, 237, 243, 0.34) 58%,
    rgba(213, 221, 230, 0.28) 100%) !important;
  -webkit-backdrop-filter: blur(10px) saturate(1.15) !important;
          backdrop-filter: blur(10px) saturate(1.15) !important;
  box-shadow:
    inset -4px -6px 14px rgba(160, 170, 185, 0.25),
    inset  3px  4px 10px rgba(255, 255, 255, 0.55),
    0 8px 20px rgba(60, 70, 90, 0.10),
    0 3px 8px rgba(60, 70, 90, 0.06) !important;
}
```

### T11 [TODO] Superseded `.product-main` / `.product-main__grid` padding and gap rules (8 rules)
- **File:** `assets/toylvia.css` | baseline lines 1194-1196, 1770-1784, 1787-1789, 3258-3265, 3269-3269 | kind: same-file overridden duplicates
- **Why it is dead:** `.product-main` padding is set four times without !important, then `.product-main { padding: 20px 20px !important }` (and its 768/1024 !important variants) always wins. Two earlier `@media (max-width: 899px)` / `(max-width: 640px)` blocks are repeated later with the same selectors and !important. `.product-main__grid { gap: 2.5rem }` is re-declared later.
- **Proof:** Static shadow proof (headless Chrome CSSOM): all 8 removed rules are fully shadowed by later kept rules -> PROVEN.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (min-width: 768px) [group] /   - removed: @media (min-width: 1024px) [group] /   - removed: .product-main { padding: 3rem 1rem; } /   - removed: .product-main { padding: 2rem 1.5rem; } /   - removed: @media (min-width: 768px) > .product-main { padding: 3rem 2rem; } /   - removed: @media (min-width: 1024px) > .product-main { padding: 4rem 3rem; } /   - removed: .product-main__grid { gap: 2.5rem; } /   - removed: @media (max-width: 899px) [group] /   - removed: @media (max-width: 899px) > .product-main { padding: 1rem 0.875rem !important; } /   - removed: @media (max-width: 899px) > .product-main__grid { grid-template-columns: 1fr !important; gap: 1.5rem !important; } /   - removed: @media (max-width: 640px) > .product-main { padding: 0.75rem 0.625rem !important; }**
- **Visual change if removed:** None (product pages keep the same padding and gaps).
- **Parts:** 5 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 1194-1196). Manual anchor: from `.product-main {` to `}`.
Delete:
```css
.product-main {
  padding: 3rem 1rem;
}
```

**Part 2** (baseline lines 1770-1784). Manual anchor: from `.product-main {` to `}`.
Delete:
```css
.product-main {
  padding: 2rem 1.5rem;
}

@media (min-width: 768px) {
  .product-main {
    padding: 3rem 2rem;
  }
}

@media (min-width: 1024px) {
  .product-main {
    padding: 4rem 3rem;
  }
}
```

**Part 3** (baseline lines 1787-1789). Manual anchor: from `.product-main__grid {` to `}`.
Delete:
```css
.product-main__grid {
  gap: 2.5rem;
}
```

**Part 4** (baseline lines 3258-3265). Manual anchor: from `/* ---- PRODUCT MAIN: single-column below 900px ---- */` to `}`.
Delete:
```css
                  /* ---- PRODUCT MAIN: single-column below 900px ---- */
                  @media (max-width: 899px) {
                    .product-main { padding: 1rem 0.875rem !important; }
                      .product-main__grid {
                          grid-template-columns: 1fr !important;
                              gap: 1.5rem !important;
                                }
                                }
```

**Part 5** (baseline lines 3269-3269). Manual anchor: from `.product-main { padding: 0.75rem 0.625rem !important; }` to `.product-main { padding: 0.75rem 0.625rem !important; }`.
Delete:
```css
                                  .product-main { padding: 0.75rem 0.625rem !important; }
```

### T12 [TODO] 11 @keyframes that nothing uses (trustIconBounce, likeBurst, likeBounceFull, sphere-shine, sphere-float-0..5, ctaSoftBounce)
- **File:** `assets/toylvia.css` | baseline lines 982-988, 1020-1023, 1031-1049, 2124-2129 | kind: unreferenced @keyframes
- **Why it is dead:** A @keyframes rule only matters if some `animation`/`animation-name` uses its name. These 11 names appear only in their own definitions.
- **Proof:** grep across the whole theme (all sections, snippets, templates, layout/theme.liquid incl. inline styles, all JS assets, all 9 CSS assets, settings_data custom CSS): each name occurs once, in its definition; partial-name greps find nothing (no names built at runtime). Chrome's parsed animation-name values never reference them.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @keyframes trustIconBounce { 0% { transform: scale(1) rotate(0deg); } 25% { transform: scale(1.3) rotate(-12deg); } 50% { transform: scale(0.9) rotate(8deg); } 75% { transform: scale(1.15) rotate(-4deg); } 100% { transform: scale(1) rotate(0deg); } } /   - removed: @keyframes likeBurst { 0% { transform: rotate(var(--deg, 0deg)) translateY(-4px); opacity: 1; } 100% { transform: rotate(var(--deg, 0deg)) translateY(-18px); opacity: 0; } } /   - removed: @keyframes likeBounceFull { 0% { transform: scale(1); } 25% { transform: scale(1.35); } 50% { transform: scale(0.85); } 75% { transform: scale(1.15); } 100% { transform: scale(1); } } /   - removed: @keyframes sphere-shine { 0% { background-position: -200% center; opacity: 0; } 10% { opacity: 1; } 90% { opacity: 1; } 100% { background-position: 200% center; opacity: 0; } } /   - removed: @keyframes sphere-float-0 { 0%, 100% { transform: translateY(0px); } 50% { transform: translateY(-8px); } } /   - removed: @keyframes sphere-float-1 { 0%, 100% { transform: translateY(0px); } 50% { transform: translateY(-6px); } } /   - removed: @keyframes sphere-float-2 { 0%, 100% { transform: translateY(0px); } 50% { transform: translateY(-10px); } } /   - removed: @keyframes sphere-float-3 { 0%, 100% { transform: translateY(0px); } 50% { transform: translateY(-7px); } } /   - removed: @keyframes sphere-float-4 { 0%, 100% { transform: translateY(0px); } 50% { transform: translateY(-9px); } } /   - removed: @keyframes sphere-float-5 { 0%, 100% { transform: translateY(0px); } 50% { transform: translateY(-6px); } } /   - removed: @keyframes ctaSoftBounce { 0% { transform: scale(1); } 45% { transform: scale(1.03); } 100% { transform: scale(1); } }**
- **Visual change if removed:** None. Keep `@keyframes cartBump` (1024-1029, used by `.cart-bump`) and `marquee`/`borderShine*`, which are used.
- **Parts:** 4 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 982-988). Manual anchor: from `@keyframes trustIconBounce {` to `}`.
Delete:
```css
@keyframes trustIconBounce {
  0% { transform: scale(1) rotate(0deg); }
  25% { transform: scale(1.3) rotate(-12deg); }
  50% { transform: scale(0.9) rotate(8deg); }
  75% { transform: scale(1.15) rotate(-4deg); }
  100% { transform: scale(1) rotate(0deg); }
}
```

**Part 2** (baseline lines 1020-1023). Manual anchor: from `@keyframes likeBurst {` to `}`.
Delete:
```css
@keyframes likeBurst {
  0% { transform: rotate(var(--deg, 0deg)) translateY(-4px); opacity: 1; }
  100% { transform: rotate(var(--deg, 0deg)) translateY(-18px); opacity: 0; }
}
```

**Part 3** (baseline lines 1031-1049). Manual anchor: from `@keyframes likeBounceFull {` to `@keyframes sphere-float-5 { 0%, 100% { transform: translateY(0); } 50% { transform: tra...`.
Delete:
```css
@keyframes likeBounceFull {
  0% { transform: scale(1); }
  25% { transform: scale(1.35); }
  50% { transform: scale(0.85); }
  75% { transform: scale(1.15); }
  100% { transform: scale(1); }
}
@keyframes sphere-shine {
  0% { background-position: -200% center; opacity: 0; }
  10% { opacity: 1; }
  90% { opacity: 1; }
  100% { background-position: 200% center; opacity: 0; }
}
@keyframes sphere-float-0 { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-8px); } }
@keyframes sphere-float-1 { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-6px); } }
@keyframes sphere-float-2 { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-10px); } }
@keyframes sphere-float-3 { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-7px); } }
@keyframes sphere-float-4 { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-9px); } }
@keyframes sphere-float-5 { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-6px); } }
```

**Part 4** (baseline lines 2124-2129). Manual anchor: from `/* CTA buttons: soft scale bounce only */` to `}`.
Delete:
```css
      /* CTA buttons: soft scale bounce only */
      @keyframes ctaSoftBounce {
        0%   { transform: scale(1);    }
          45%  { transform: scale(1.03); }
            100% { transform: scale(1);    }
            }
```

### T13 [TODO] Sizing rules for `.category-arc__grid`, an element that is always hidden and never rendered
- **File:** `assets/toylvia.css` | baseline lines 273-280, 290-296, 298-304 | kind: styles for a hidden element
- **Why it is dead:** `.category-sphere, .category-arc__grid { display: none !important; }` (baseline 4875, top level, in the V14 block) hides the grid at every width and nothing overrides it. Its height/width/transform/padding/margin/transition can never render. Lines 303-304 also repeat 300-301. In addition, no template or snippet outputs `.category-arc__grid` at all.
- **Proof:** Every display declaration on this selector across all theme CSS was checked: none with !important except the hider. Chrome reports display:none at 768-1920px. grep: `category-arc__grid` appears in no .liquid/.js/.json file.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (min-width: 768px) [group] /   - removed: @media (min-width: 768px) [group] /   - removed: @media (min-width: 1024px) [group] /   - removed: @media (min-width: 1024px) [group] /   - removed: .category-arc__grid { position: relative; margin: 0px auto; transform-origin: center top; height: 260px; } /   - removed: @media (max-width: 639px) > .category-arc__grid { width: 680px; height: 260px; transition: filter 1.8s cubic-bezier(0.4, 0, 0.2, 1), transform 1.8s cubic-bezier(0.4, 0, 0.2, 1); margin-bottom: 0px; padding: 0px 1.5rem; box-sizing: border-box; } /   - removed: @media (min-width: 480px) [group] /   - removed: @media (min-width: 480px) > .category-arc__grid { transform: scale(0.58); margin-bottom: -110px; } /   - removed: @media (min-width: 640px) [group] /   - removed: @media (min-width: 640px) > .category-arc__grid { height: 330px; transform: scale(0.75); margin-bottom: 0px; } /   - removed: @media (min-width: 768px) > .category-arc__grid { height: 330px; transform: scale(0.9); margin-bottom: 0px; } /   - removed: @media (min-width: 1024px) > .category-arc__grid { height: 300px; transform: scale(1); margin-bottom: 0px; } /   - removed: @media (min-width: 768px) > .category-arc__grid { height: 330px; transform: scale(0.9); } /   - removed: @media (min-width: 1024px) > .category-arc__grid { height: 300px; transform: scale(1); }**
- **Visual change if removed:** None. Keep the `.category-arc` and `.category-arc .max-store` rules at 282-289 and the `}` at 297.
- **Notes:** If someone ever brings the category spheres back (removes the display:none), these sizes would have to be rewritten anyway.
- **Superseded by:** T22 (REVIEW). If Ziko approves T22, skip this item; it is included there.
- **Parts:** 3 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 273-280). Manual anchor: from `/* === CATEGORY ARC === */` to `}`.
Delete:
```css
/* === CATEGORY ARC === */
.category-arc__grid {
  position: relative;
  margin: 0 auto;
  transform-origin: top center;
  height: 260px;
 
}
```

**Part 2** (baseline lines 290-296). Manual anchor: from `.category-arc__grid {` to `}`.
Delete:
```css
  .category-arc__grid {
    width: 680px;
    height: 260px;
transition: filter 1.8s cubic-bezier(0.4, 0, 0.2, 1), transform 1.8s cubic-bezier(0.4, 0, 0.2, 1);    margin-bottom: 0;
    padding: 0 1.5rem;        /* add this */
    box-sizing: border-box;   /* add this */
  }
```

**Part 3** (baseline lines 298-304). Manual anchor: from `@media (min-width: 480px) { .category-arc__grid { transform: scale(0.58); margin-bottom...` to `@media (min-width: 1024px) { .category-arc__grid { height: 300px; transform: scale(1); } }`.
Delete:
```css
@media (min-width: 480px) { .category-arc__grid { transform: scale(0.58); margin-bottom: -110px; } }
@media (min-width: 640px) { .category-arc__grid { height: 330px; transform: scale(0.75); margin-bottom: 0; } }
@media (min-width: 768px) { .category-arc__grid { height: 330px; transform: scale(0.9); margin-bottom: 0; } }
@media (min-width: 1024px) { .category-arc__grid { height: 300px; transform: scale(1); margin-bottom: 0; } }

@media (min-width: 768px) { .category-arc__grid { height: 330px; transform: scale(0.9); } }
@media (min-width: 1024px) { .category-arc__grid { height: 300px; transform: scale(1); } }
```

### T14 [TODO] Dangling `.cat-ice-label` fused into an impossible selector `.cat-ice-label html body .trust-badges`
- **File:** `assets/toylvia.css` | baseline lines 5538-5538, 5544-5546 | kind: never-matching selector
- **Why it is dead:** A cut-off selector `.cat-ice-label` (no `{`) merges with the next rule `html body .trust-badges { padding: 2rem 3rem !important }`. The result `.cat-ice-label html body .trust-badges` needs an ancestor of <html>, which cannot exist. (`.trust-badges` is also not used in markup; the section uses `.trust-strip`.)
- **Proof:** Chrome's CSSOM shows the fused rule; removing both parts removes exactly that one rule. Proven from CSS alone.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (max-width: 1024px) > .cat-ice-label html body .trust-badges { padding: 2rem 3rem !important; }**
- **Visual change if removed:** None.
- **Notes:** Both parts must go together (one item, apply.py does that). Deleting only the rule would let `.cat-ice-label` fuse with the NEXT selector and break it. This does not fix the unclosed `@media (max-width: 1024px)` (see 'Known issues'): that block stays open, so nothing changes.
- **Parts:** 2 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 5538-5538). Manual anchor: from `.cat-ice-label` to `.cat-ice-label`.
Delete:
```css
                                                                                                                                                                                                                                                                                                                                                            .cat-ice-label
```

**Part 2** (baseline lines 5544-5546). Manual anchor: from `html body .trust-badges {` to `}`.
Delete:
```css
html body .trust-badges {
  padding: 2rem 3rem !important;
}
```

### T15 [TODO] Stale 'Shopify CDN: Minification failed' error header saved into the source
- **File:** `assets/toylvia.css` | baseline lines 1-7 | kind: junk comment (not CSS)
- **Why it is dead:** Shopify prepends this error report to the served file when minification fails. Someone saved it back into the source. The errors it lists (lines 2468, 2545, 3977) no longer exist.
- **Proof:** Comment only, so Chrome's rule list is identical. If minification still fails, Shopify adds a fresh, accurate header to what it serves.
- **Verify:** expected `cssom.js compare` result for this item alone: **IDENTICAL: Chrome keeps exactly the same rules in the same order. No visual change is possible.**
- **Visual change if removed:** None.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 1-7). Manual anchor: from `/** Shopify CDN: Minification failed` to `**/`.
Delete:
```css
/** Shopify CDN: Minification failed

Line 2468:0 Unexpected "<"
Line 2545:0 Unexpected "<"
Line 3977:224 Unexpected "}"

**/
```

### T16 [TODO] Broken double banner comment ('ICE CARD CATEGORY GRID' + 'complete rewrite')
- **File:** `assets/toylvia.css` | baseline lines 5313-5317 | kind: junk comment (not CSS)
- **Why it is dead:** An old banner was opened with `/*` and never closed, then a newer banner was pasted inside it. CSS comments do not nest, so it is one comment holding only banner text.
- **Proof:** Comment only, Chrome's rule list is identical. The following `@keyframes cat-ice-float` parses normally either way.
- **Verify:** expected `cssom.js compare` result for this item alone: **IDENTICAL: Chrome keeps exactly the same rules in the same order. No visual change is possible.**
- **Visual change if removed:** None.
- **Superseded by:** T31 (REVIEW). If Ziko approves T31, skip this item; it is included there.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 5313-5317). Manual anchor: from `/* ============================================================` to `===================================================== */`.
Delete:
```css
            /* ============================================================
               ICE CARD CATEGORY GRID  –  Toylvia
                  /* =====================================================
                     ICE CATEGORY CARDS — complete rewrite
                        ===================================================== */
```

### T17 [REVIEW] `body.index-page { background: transparent !important }`: <body> never has that class
- **File:** `assets/toylvia.css` | baseline lines 21-24 | kind: never-matching selector (markup)
- **Why it is dead:** layout/theme.liquid renders a bare `<body>`. The only class ever added is `tlv-support` (theme.liquid JS). `index-page` appears in no theme file. The stylesheet itself says at line ~52: 'body.template-index doesn't work (body has no class)'.
- **Proof:** grep of all layout/section/snippet/template files and JS assets. Not provable from CSS alone (an app could add body classes), hence REVIEW.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: body.index-page { background: transparent !important; }**
- **Visual change if removed:** None expected.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 21-24). Manual anchor: from `/* Homepage: transparent body so glitch bg layer shows through */` to `}`.
Delete:
```css
/* Homepage: transparent body so glitch bg layer shows through */
body.index-page {
  background: transparent !important;
}
```

### T18 [REVIEW] Two rules for section wrappers that no longer exist (`#shopify-section-template--29786103284043__glitch-bg`, `...__trust-badges`)
- **File:** `assets/toylvia.css` | baseline lines 4874-4874, 4900-4900 | kind: never-matching selector (markup)
- **Why it is dead:** Shopify gives JSON-template sections the id `shopify-section-template--<templateId>__<key>`. templates/index.json and product.json have no `glitch-bg` or `trust-badges` key, so neither wrapper is rendered. The second rule also needs `.trust-badges`, which no markup uses.
- **Proof:** Section keys checked in templates/index.json and templates/product.json; grep of the whole theme.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: #shopify-section-template--29786103284043__glitch-bg { display: none !important; } /   - removed: html body #shopify-section-template--29786103284043__trust-badges .trust-badges { padding-top: 8px !important; }**
- **Visual change if removed:** None expected.
- **Notes:** Would only come back to life if sections with those exact keys were re-added to the template with id 29786103284043.
- **Parts:** 2 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 4874-4874). Manual anchor: from `#shopify-section-template--29786103284043__glitch-bg { display: none !important; }` to `#shopify-section-template--29786103284043__glitch-bg { display: none !important; }`.
Delete:
```css
#shopify-section-template--29786103284043__glitch-bg { display: none !important; }
```

**Part 2** (baseline lines 4900-4900). Manual anchor: from `html body #shopify-section-template--29786103284043__trust-badges .trust-badges { paddi...` to `html body #shopify-section-template--29786103284043__trust-badges .trust-badges { paddi...`.
Delete:
```css
html body #shopify-section-template--29786103284043__trust-badges .trust-badges { padding-top: 8px !important; }
```

### T19 [REVIEW] 'Desktop only' `.clg-pill .clg-block-header .clg-title` rule that can only apply at exactly 1024px, for markup that does not exist
- **File:** `assets/toylvia.css` | baseline lines 6019-6025 | kind: never-true media + never-matching selector
- **Why it is dead:** It sits inside the unclosed `@media (max-width: 1024px)`, so `@media (min-width: 1024px)` inside it is only true at exactly 1024px. And no template uses `clg-pill`, `clg-block-header` or `clg-title`.
- **Proof:** Chrome CSSOM shows `@media (max-width:1024px) > @media (min-width:1024px)`. grep of all .liquid/.js/.json: no match for those classes.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (max-width: 1024px) > @media (min-width: 1024px) [group] /   - removed: @media (max-width: 1024px) > @media (min-width: 1024px) > .clg-pill .clg-block-header .clg-title { font-size: 24px; font-weight: bold; }**
- **Visual change if removed:** None expected.
- **Notes:** If Ziko fixes the unclosed @media later, this rule would become desktop-wide, but it still matches no element.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 6019-6025). Manual anchor: from `/* Target only screens wider than 1024px (Desktop) */` to `}`.
Delete:
```css
/* Target only screens wider than 1024px (Desktop) */
@media (min-width: 1024px) {
  .clg-pill .clg-block-header .clg-title {
    font-size: 24px; /* Adjust this value as needed */
    font-weight: bold; /* Optional: makes it stand out more */
  }
}
```

### T20 [TODO] First copy of the duplicated CART styles: 21 rules re-declared later (about 100 lines)
- **File:** `assets/toylvia.css` | baseline lines 1459-1461, 1463-1466, 1476-1480, 1483-1486, 1488-1495, 1498-1504, 1506-1509, 1516-1520, 1522-1525, 1527-1530, 1537-1542, 1544-1548, 1550-1553, 1555-1559, 1568-1575, 1579-1581, 1588-1590, 1592-1596, 1608-1613, 1622-1624, 1626-1629 | kind: same-file overridden duplicates
- **Why it is dead:** The 'CART BASE' block was pasted again later as '/* === CART === */'. These 21 earlier rules are re-declared later with the same selector, same media query and same importance, so they never win. Interleaved rules that still contribute a value (e.g. `.cart__header` justify-content, `.cart__title` margin-bottom, `.cart__total`, `.cart__update`, the @media wrappers) are NOT in the ranges and stay.
- **Proof:** Static shadow proof (headless Chrome CSSOM): all 21 removed rules are fully shadowed by later kept rules -> PROVEN. Control: deleting the later live copy of `.cart` instead is correctly reported NOT shadowed.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .cart { padding: 3rem 1rem; } /   - removed: .cart__inner { max-width: 900px; margin: 0px auto; } /   - removed: .cart__back { font-size: 14px; text-decoration: none; color: rgb(85, 85, 85); } /   - removed: .cart__empty { text-align: center; margin-top: 4rem; } /   - removed: .cart__cta { display: inline-block; margin-top: 1rem; padding: 0.7rem 1.4rem; background: rgb(0, 0, 0); color: rgb(255, 255, 255); border-radius: 999px; } /   - removed: .cart__item { display: grid; grid-template-columns: 90px 1fr auto; gap: 1.2rem; align-items: center; margin-bottom: 1.8rem; } /   - removed: .cart__img { width: 90px; border-radius: 0.5rem; } /   - removed: .cart__variant { font-size: 13px; color: rgb(119, 119, 119); margin-bottom: 0.3rem; } /   - removed: .cart__price { font-size: 14px; margin-bottom: 0.4rem; } /   - removed: .cart__qty { width: 65px; padding: 0.3rem; } /   - removed: .cart__footer { margin-top: 3rem; display: flex; justify-content: space-between; gap: 2rem; } /   - removed: .cart__row { display: flex; justify-content: space-between; margin-bottom: 0.5rem; } /   - removed: .cart__note { font-size: 13px; color: rgb(119, 119, 119); } /   - removed: .cart__actions { display: flex; flex-direction: column; gap: 0.6rem; } /   - removed: .cart__checkout { padding: 1rem 2rem; border-radius: 999px; background: linear-gradient(90deg, rgb(255, 66, 161), rgb(255, 123, 189)); color: rgb(255, 255, 255); font-weight: 800; border: none; } /   - removed: @media (max-width: 768px) > .cart__item { grid-template-columns: 70px 1fr; } /   - removed: @media (max-width: 768px) > .cart__footer { flex-direction: column; } /   - removed: .cart__actions { display: flex; flex-direction: column; gap: 0.8rem; } /   - removed: .cart__header { display: flex; align-items: center; gap: 1rem; margin-bottom: 2rem; } /   - removed: .cart__back:hover { color: rgb(0, 0, 0); } /   - removed: .cart__title { font-size: 24px; font-weight: 800; }**
- **Visual change if removed:** None (cart page https://toylvia.com/cart keeps the same computed styles).
- **Notes:** 21 parts. Several parts are byte-identical to their later copies, so they are located with neighbouring context lines. Always use apply.py; do not delete by hand by searching for the rule text (you would hit the live copy).
- **Superseded by:** T26 (REVIEW). If Ziko approves T26, skip this item; it is included there.
- **Parts:** 21 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 1459-1461). Manual anchor: from `.cart {` to `}`.
This text also exists elsewhere in the file, so it is located by the neighbouring lines (kept, not deleted): before = `/* === CART BASE === */`, after = `(none)`.
Delete:
```css
.cart {
  padding: 3rem 1rem;
}
```

**Part 2** (baseline lines 1463-1466). Manual anchor: from `.cart__inner {` to `}`.
This text also exists elsewhere in the file, so it is located by the neighbouring lines (kept, not deleted): before = `(none)`, after = `/* HEADER */ .cart__header { display: flex; justify-content: space-between;`.
Delete:
```css
.cart__inner {
  max-width: 900px;
  margin: 0 auto;
}
```

**Part 3** (baseline lines 1476-1480). Manual anchor: from `.cart__back {` to `}`.
This text also exists elsewhere in the file, so it is located by the neighbouring lines (kept, not deleted): before = `(none)`, after = `/* EMPTY */`.
Delete:
```css
.cart__back {
  font-size: 14px;
  text-decoration: none;
  color: #555;
}
```

**Part 4** (baseline lines 1483-1486). Manual anchor: from `.cart__empty {` to `}`.
This text also exists elsewhere in the file, so it is located by the neighbouring lines (kept, not deleted): before = `color: #555; } /* EMPTY */`, after = `(none)`.
Delete:
```css
.cart__empty {
  text-align: center;
  margin-top: 4rem;
}
```

**Part 5** (baseline lines 1488-1495). Manual anchor: from `.cart__cta {` to `}`.
This text also exists elsewhere in the file, so it is located by the neighbouring lines (kept, not deleted): before = `color: #555; } /* EMPTY */ .cart__empty { text-align: center; margin-top: 4rem; }`, after = `(none)`.
Delete:
```css
.cart__cta {
  display: inline-block;
  margin-top: 1rem;
  padding: 0.7rem 1.4rem;
  background: #000;
  color: #fff;
  border-radius: 999px;
}
```

**Part 6** (baseline lines 1498-1504). Manual anchor: from `.cart__item {` to `}`.
This text also exists elsewhere in the file, so it is located by the neighbouring lines (kept, not deleted): before = `(none)`, after = `.cart__img { width: 90px; border-radius: 0.5rem; } .cart__title {`.
Delete:
```css
.cart__item {
  display: grid;
  grid-template-columns: 90px 1fr auto;
  gap: 1.2rem;
  align-items: center;
  margin-bottom: 1.8rem;
}
```

**Part 7** (baseline lines 1506-1509). Manual anchor: from `.cart__img {` to `}`.
This text also exists elsewhere in the file, so it is located by the neighbouring lines (kept, not deleted): before = `(none)`, after = `.cart__title {`.
Delete:
```css
.cart__img {
  width: 90px;
  border-radius: 0.5rem;
}
```

**Part 8** (baseline lines 1516-1520). Manual anchor: from `.cart__variant {` to `}`.
This text also exists elsewhere in the file, so it is located by the neighbouring lines (kept, not deleted): before = `.cart__title { font-weight: 700; margin-bottom: 0.3rem; }`, after = `(none)`.
Delete:
```css
.cart__variant {
  font-size: 13px;
  color: #777;
  margin-bottom: 0.3rem;
}
```

**Part 9** (baseline lines 1522-1525). Manual anchor: from `.cart__price {` to `}`.
This text also exists elsewhere in the file, so it is located by the neighbouring lines (kept, not deleted): before = `(none)`, after = `.cart__qty { width: 65px; padding: 0.3rem; } .cart__total {`.
Delete:
```css
.cart__price {
  font-size: 14px;
  margin-bottom: 0.4rem;
}
```

**Part 10** (baseline lines 1527-1530). Manual anchor: from `.cart__qty {` to `}`.
This text also exists elsewhere in the file, so it is located by the neighbouring lines (kept, not deleted): before = `(none)`, after = `.cart__total {`.
Delete:
```css
.cart__qty {
  width: 65px;
  padding: 0.3rem;
}
```

**Part 11** (baseline lines 1537-1542). Manual anchor: from `.cart__footer {` to `}`.
This text also exists elsewhere in the file, so it is located by the neighbouring lines (kept, not deleted): before = `.cart__total { font-weight: 700; } /* FOOTER */`, after = `(none)`.
Delete:
```css
.cart__footer {
  margin-top: 3rem;
  display: flex;
  justify-content: space-between;
  gap: 2rem;
}
```

**Part 12** (baseline lines 1544-1548). Manual anchor: from `.cart__row {` to `}`.
This text also exists elsewhere in the file, so it is located by the neighbouring lines (kept, not deleted): before = `.cart__total { font-weight: 700; } /* FOOTER */ .cart__footer { margin-top: 3rem; displ...`, after = `(none)`.
Delete:
```css
.cart__row {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.5rem;
}
```

**Part 13** (baseline lines 1550-1553). Manual anchor: from `.cart__note {` to `}`.
This text also exists elsewhere in the file, so it is located by the neighbouring lines (kept, not deleted): before = `(none)`, after = `.cart__actions { display: flex; flex-direction: column; gap: 0.6rem; } .cart__update {`.
Delete:
```css
.cart__note {
  font-size: 13px;
  color: #777;
}
```

**Part 14** (baseline lines 1555-1559). Manual anchor: from `.cart__actions {` to `}`.
This text also exists elsewhere in the file, so it is located by the neighbouring lines (kept, not deleted): before = `(none)`, after = `.cart__update {`.
Delete:
```css
.cart__actions {
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}
```

**Part 15** (baseline lines 1568-1575). Manual anchor: from `.cart__checkout {` to `}`.
This text also exists elsewhere in the file, so it is located by the neighbouring lines (kept, not deleted): before = `border-radius: 0.4rem; }`, after = `(none)`.
Delete:
```css
.cart__checkout {
  padding: 1rem 2rem;
  border-radius: 999px;
  background: linear-gradient(90deg,#ff42a1,#ff7bbd);
  color: #fff;
  font-weight: 800;
  border: none;
}
```

**Part 16** (baseline lines 1579-1581). Manual anchor: from `.cart__item {` to `}`.
This text also exists elsewhere in the file, so it is located by the neighbouring lines (kept, not deleted): before = `(none)`, after = `.cart__total {`.
Delete:
```css
  .cart__item {
    grid-template-columns: 70px 1fr;
  }
```

**Part 17** (baseline lines 1588-1590). Manual anchor: from `.cart__footer {` to `}`.
This text also exists elsewhere in the file, so it is located by the neighbouring lines (kept, not deleted): before = `(none)`, after = `} .cart__actions {`.
Delete:
```css
  .cart__footer {
    flex-direction: column;
  }
```

**Part 18** (baseline lines 1592-1596). Manual anchor: from `.cart__actions {` to `}`.
Delete:
```css
.cart__actions {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
}
```

**Part 19** (baseline lines 1608-1613). Manual anchor: from `.cart__header {` to `}`.
This text also exists elsewhere in the file, so it is located by the neighbouring lines (kept, not deleted): before = `}`, after = `(none)`.
Delete:
```css
.cart__header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 2rem;
}
```

**Part 20** (baseline lines 1622-1624). Manual anchor: from `.cart__back:hover {` to `}`.
This text also exists elsewhere in the file, so it is located by the neighbouring lines (kept, not deleted): before = `white-space: nowrap; }`, after = `(none)`.
Delete:
```css
.cart__back:hover {
  color: #000;
}
```

**Part 21** (baseline lines 1626-1629). Manual anchor: from `.cart__title {` to `}`.
This text also exists elsewhere in the file, so it is located by the neighbouring lines (kept, not deleted): before = `(none)`, after = `/* === CART === */`.
Delete:
```css
.cart__title {
  font-size: 24px;
  font-weight: 800;
}
```

### T21 [TODO] Superseded connector-width, age-label size and card padding tweaks (6 rules)
- **File:** `assets/live-card-fixes.css` | baseline lines 105-122 | kind: overridden rules (cross-file, !important + higher specificity)
- **Why it is dead:** Six earlier tweaks, each fully replaced by a later !important rule with higher specificity that matches every element they match: connector width/min-width lose to live-card-fixes 197-199 (16 IDs), `.age-tag` 10px loses to 232-233 (22 IDs, 9px), `.cr-card` padding-bottom loses to card-look.css 45 (#MainContent x308, padding shorthand !important), body padding loses to later card rules.
- **Proof:** Checked property by property by two agents. live-card-fixes.css and card-look.css are both loaded unconditionally on every page (layout/theme.liquid lines ~2091 and ~2095), and !important plus higher specificity wins regardless of order. Chrome CSSOM: removing the range removes exactly these 6 rules.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: html body #MainContent#MainContent#MainContent#MainContent .cr-card__tag.cr-card__tag.cr-card__tag::before, html body #MainContent#MainContent#MainContent#MainContent .product-card__tag.product-card__tag.product-card__tag::before, html body #MainContent#MainContent#MainContent#MainContent .soft-dot  /   - removed: html body #MainContent#MainContent#MainContent .age-tag.age-tag.age-tag { font-size: 10px !important; } /   - removed: html body #MainContent#MainContent#MainContent#MainContent .cr-card.cr-card.cr-card { padding-bottom: 6.3px !important; } /   - removed: html body #MainContent#MainContent#MainContent#MainContent .cr-card.cr-card.cr-card .cr-card__body { padding-left: 6px !important; padding-right: 6px !important; } /   - removed: html body #MainContent#MainContent#MainContent#MainContent#MainContent .cr-card.cr-card.cr-card .cr-card__body { padding-left: 4px !important; padding-right: 4px !important; } /   - removed: html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .cr-card.cr-card.cr-card .cr-card__body { padding-bottom: 7.5px !important; }**
- **Visual change if removed:** None.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 105-122). Manual anchor: from `html body #MainContent#MainContent#MainContent#MainContent .cr-card__tag.cr-card__tag.c...` to `html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .cr-...`.
Delete:
```css
html body #MainContent#MainContent#MainContent#MainContent .cr-card__tag.cr-card__tag.cr-card__tag::before,
html body #MainContent#MainContent#MainContent#MainContent .product-card__tag.product-card__tag.product-card__tag::before,
html body #MainContent#MainContent#MainContent#MainContent .soft-dot>.tag-edge-line.tag-edge-line{width:calc(var(--marker-inset,8.68625px) - 3px)!important;min-width:calc(var(--marker-inset,8.68625px) - 3px)!important}

/* Age label on cards: 9px -> 10px. */
html body #MainContent#MainContent#MainContent .age-tag.age-tag.age-tag{font-size:10px!important}

/* Space under the price: 14px total -> about 12.3px (-12%). */
html body #MainContent#MainContent#MainContent#MainContent .cr-card.cr-card.cr-card{padding-bottom:6.3px!important}

/* Text sits 14px from the card edge: 8px card padding + 6px body padding. */
html body #MainContent#MainContent#MainContent#MainContent .cr-card.cr-card.cr-card .cr-card__body{padding-left:6px!important;padding-right:6px!important}

/* Text area side padding 4px (text sits 12px from the card edge). */
html body #MainContent#MainContent#MainContent#MainContent#MainContent .cr-card.cr-card.cr-card .cr-card__body{padding-left:4px!important;padding-right:4px!important}

/* Text area bottom padding 7.5px (sides stay 4px). */
html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .cr-card.cr-card.cr-card .cr-card__body{padding-bottom:7.5px!important}
```

### T22 [REVIEW] The whole original CATEGORY ARC / category-sphere block (37 rules, 173 lines)
- **File:** `assets/toylvia.css` | baseline lines 273-445 | kind: styles for hidden + non-existent elements
- **Why it is dead:** Styles for the old round 'category sphere' buttons. `.category-sphere, .category-arc__grid { display: none !important }` (baseline 4875, top level) hides them on every page and nothing overrides it. On top of that, no template, snippet or script outputs `category-sphere` or `category-arc` at all (sections/category-arc.liquid renders `.holo-section` / `.cat-grid` and is not used in templates/index.json).
- **Proof:** grep of all .liquid/.js/.json: no markup with these classes; only querySelector calls and a settings_data custom-CSS selector. No CSS anywhere sets display with !important on these selectors except the hider. Chrome CSSOM: removing 273-445 removes exactly the 37 category-arc/sphere rules.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (min-width: 768px) [group] /   - removed: @media (min-width: 768px) [group] /   - removed: @media (min-width: 1024px) [group] /   - removed: @media (min-width: 1024px) [group] /   - removed: .category-arc__grid { position: relative; margin: 0px auto; transform-origin: center top; height: 260px; } /   - removed: @media (max-width: 639px) [group] /   - removed: @media (max-width: 639px) > .category-arc { overflow-x: auto; padding: 0px 1.5rem; } /   - removed: @media (max-width: 639px) > .category-arc .max-store { min-width: 680px; } /   - removed: @media (max-width: 639px) > .category-arc__grid { width: 680px; height: 260px; transition: filter 1.8s cubic-bezier(0.4, 0, 0.2, 1), transform 1.8s cubic-bezier(0.4, 0, 0.2, 1); margin-bottom: 0px; padding: 0px 1.5rem; box-sizing: border-box; } /   - removed: @media (min-width: 480px) [group] /   - removed: @media (min-width: 480px) > .category-arc__grid { transform: scale(0.58); margin-bottom: -110px; } /   - removed: @media (min-width: 640px) [group] /   - removed: @media (min-width: 640px) > .category-arc__grid { height: 330px; transform: scale(0.75); margin-bottom: 0px; } /   - removed: @media (min-width: 768px) > .category-arc__grid { height: 330px; transform: scale(0.9); margin-bottom: 0px; } /   - removed: @media (min-width: 1024px) > .category-arc__grid { height: 300px; transform: scale(1); margin-bottom: 0px; } /   - removed: @media (min-width: 768px) > .category-arc__grid { height: 330px; transform: scale(0.9); } /   - removed: @media (min-width: 1024px) > .category-arc__grid { height: 300px; transform: scale(1); } /   - removed: .category-sphere { position: absolute; cursor: pointer; transition: filter 1.8s cubic-bezier(0.4, 0, 0.2, 1), transform 1.8s cubic-bezier(0.4, 0, 0.2, 1); z-index: 1; } /   - removed: .category-sphere:hover { z-index: 10; } /   - removed: .category-sphere__ball { width: 132px; height: 132px; border-radius: 50%; background: radial-gradient(circle at 32% 25%, rgba(255, 255, 255, 0.85) 0%, rgba(246, 247, 248, 0.75) 25%, rgba(228, 231, 236, 0.6) 50%, rgba(202, 207, 216, 0.5) 75%, rgba(179, 186, 198, 0.45) 100%); display: flex; align-item /   - removed: .category-sphere:hover .category-sphere__ball { width: 175px; height: 100px; border-radius: 999px; background: hsl(var(--card)); } /   - removed: .category-sphere__icon { transition: opacity 1.8s cubic-bezier(0.4, 0, 0.2, 1), transform 1.8s cubic-bezier(0.4, 0, 0.2, 1), filter 1.8s cubic-bezier(0.4, 0, 0.2, 1); } /   - removed: .category-sphere:hover .category-sphere__icon { opacity: 0; transform: scale(0.5); filter: blur(6px); } /   - removed: .category-sphere__label { position: absolute; inset: 0px; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700; letter-spacing: 0.22em; white-space: nowrap; text-transform: uppercase; color: hsl(var(--foreground)); opacity: 0; transform: translateX(10px) sca /   - removed: .category-sphere:hover .category-sphere__label { opacity: 1; transform: translateX(0px) scale(1); } /   - removed: .category-sphere__rim { position: absolute; top: 1px; left: 8%; right: 8%; height: 3px; border-radius: 50%; filter: blur(1.5px); opacity: 0.7; } /   - removed: .category-sphere:hover .category-sphere__rim { opacity: 0; } /   - removed: .category-sphere__shadow { width: 65px; height: 15px; border-radius: 50%; background: radial-gradient(rgba(0, 0, 0, 0.06), transparent 70%); margin: 14px auto 0px; transition: width 1s cubic-bezier(0.22, 1, 0.36, 1), opacity 0.85s; opacity: 0; } /   - removed: .category-sphere:hover .category-sphere__shadow { width: 100px; } /   - removed: .category-sphere::after { display: none; } /   - removed: .category-sphere__ball { background: radial-gradient(circle at 50% 120%, rgb(228, 234, 241) 0%, rgba(193, 202, 215, 0.9) 25%, rgba(151, 164, 186, 0.75) 60%, rgba(99, 116, 156, 0.65) 85%, rgba(74, 85, 120, 0.6) 100%); overflow: visible; } /   - removed: .category-sphere__ball::before { content: ""; position: absolute; top: 1%; left: 5%; width: 90%; height: 90%; border-radius: 50%; background: radial-gradient(circle at 50% 0px, rgba(255, 255, 255, 0.88), rgba(255, 255, 255, 0) 58%); filter: blur(5px); z-index: 2; pointer-events: none; } /   - removed: .category-sphere__ball::after { content: ""; position: absolute; top: 8%; left: 10%; width: 40%; height: 25%; border-radius: 50%; background: radial-gradient(circle, rgba(255, 255, 255, 0.75), rgba(255, 255, 255, 0) 70%); transform: rotate(-30deg) skewX(-10deg); filter: blur(3px); z-index: 3; pointe /   - removed: .category-sphere__ball { background: radial-gradient(circle at 50% 120%, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.3) 25%, rgba(255, 255, 255, 0.55) 60%, rgba(240, 240, 248, 0.75) 85%, rgba(220, 222, 235, 0.85) 100%); } /   - removed: .category-sphere__ball { background: linear-gradient(165deg, rgb(255, 255, 255) 0%, rgb(232, 234, 237) 50%, rgb(220, 222, 226) 95%, rgb(180, 182, 196) 100%); box-shadow: rgba(255, 255, 255, 0.95) -12px -10px 24px, rgba(148, 150, 176, 0.55) 12px 10px 24px; transition: 0.4s; } /   - removed: .category-sphere:hover .category-sphere__ball { background: linear-gradient(165deg, rgb(255, 255, 255) 0%, rgb(232, 234, 237) 50%, rgb(220, 222, 226) 95%, rgb(180, 182, 196) 100%); box-shadow: rgba(255, 255, 255, 0.95) -12px -10px 24px, rgba(148, 150, 176, 0.55) 12px 10px 24px; } /   - removed: .category-sphere:hover .category-sphere__ball { height: 135px; width: 200px; }**
- **Visual change if removed:** None (the spheres are never shown).
- **Notes:** Markup-based (the `.category-arc` and `.category-arc .max-store` rules are not hidden by CSS, they just match nothing), hence REVIEW. Contains T13 entirely.
- **Supersedes:** T13, T39. This bigger item already contains them. If Ziko approves it, apply it INSTEAD of T13, T39 and mark those `DONE (covered by T22)`. Apply it before them; once they are applied this item no longer matches.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 273-445). Manual anchor: from `/* === CATEGORY ARC === */` to `}`.
Delete:
```css
/* === CATEGORY ARC === */
.category-arc__grid {
  position: relative;
  margin: 0 auto;
  transform-origin: top center;
  height: 260px;
 
}
@media (max-width: 639px) {
  .category-arc {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
       padding: 0 1.5rem; 
  }
  .category-arc .max-store {
    min-width: 680px;
  }
  .category-arc__grid {
    width: 680px;
    height: 260px;
transition: filter 1.8s cubic-bezier(0.4, 0, 0.2, 1), transform 1.8s cubic-bezier(0.4, 0, 0.2, 1);    margin-bottom: 0;
    padding: 0 1.5rem;        /* add this */
    box-sizing: border-box;   /* add this */
  }
}
/* ... 123 more lines, see findings.json exact_text ... */
  filter: blur(3px);
  z-index: 3;
  pointer-events: none;
  mix-blend-mode: screen;
}
/* === WHITE / TRANSPARENT SPHERE OVERRIDE === */
.category-sphere__ball {
  background: radial-gradient(circle at 50% 120%, rgba(255,255,255,0.10) 0%, rgba(255,255,255,0.30) 25%, rgba(255,255,255,0.55) 60%, rgba(240,240,248,0.75) 85%, rgba(220,222,235,0.85) 100%);
}
/* === KEV_KAN_CODE NEUMORPHIC (adapted for spheres) === */
.category-sphere__ball {
  background: linear-gradient(165deg, rgba(255,255,255,1) 0%, rgba(232,234,237,1) 50%, rgba(220,222,226,1) 95%, rgba(180,182,196,1) 100%);
    box-shadow: -12px -10px 24px rgba(255,255,255,0.95), 12px 10px 24px rgba(148,150,176,0.55);
      transition: all 0.4s ease;
}
/* Hover stays the same */
.category-sphere:hover .category-sphere__ball {
  background: linear-gradient(165deg, rgba(255,255,255,1) 0%, rgba(232,234,237,1) 50%, rgba(220,222,226,1) 95%, rgba(180,182,196,1) 100%);
    box-shadow: -12px -10px 24px rgba(255,255,255,0.95), 12px 10px 24px rgba(148,150,176,0.55);
    }
    /* === PILL HOVER HEIGHT === */
  .category-sphere:hover .category-sphere__ball {
        height: 135px;
          width: 200px;
          }
```

### T23 [REVIEW] 'Consolidated overrides' sections 1-4: sphere fills, centred icon/label, hover fade, blurred overlay (11 rules)
- **File:** `assets/toylvia.css` | baseline lines 4417-4485 | kind: styles for hidden + non-existent elements
- **Why it is dead:** Sections 1-4 of the 'TOYLVIA - Consolidated custom overrides' group only style `.category-sphere__ball`, its ::before, `__shadow`, `__icon`, `__label` and hover versions. The spheres are display:none !important and no markup outputs these classes. Section 5 (ALL PRODUCTS button, live) and the group header comment are NOT included.
- **Proof:** Chrome CSSOM: removing 4417-4485 removes exactly 11 category-sphere rules. grep: no markup with these classes.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: html body .category-sphere__ball { background: radial-gradient(circle at 30% 22%, rgb(255, 255, 255) 0%, rgb(248, 250, 252) 18%, rgb(232, 237, 243) 58%, rgb(213, 221, 230) 100%) !important; box-shadow: rgba(160, 170, 185, 0.45) -8px -10px 20px inset, rgba(255, 255, 255, 0.95) 6px 8px 18px inset, rgb /   - removed: html body .category-sphere:hover .category-sphere__ball { transform: none !important; } /   - removed: html body .category-sphere__shadow { display: none !important; } /   - removed: html body .category-sphere__ball { position: relative !important; overflow: hidden !important; } /   - removed: html body .category-sphere__ball .category-sphere__icon, html body .category-sphere__ball .category-sphere__label { position: absolute !important; left: 50% !important; top: 50% !important; transform: translate(-50%, -50%) !important; z-index: 2 !important; text-align: center !important; } /   - removed: html body .category-sphere__icon { transition: opacity 0.45s cubic-bezier(0.4, 0, 0.2, 1), filter 0.45s cubic-bezier(0.4, 0, 0.2, 1) !important; } /   - removed: html body .category-sphere__label { opacity: 0; transition: opacity 0.38s cubic-bezier(0.4, 0, 0.2, 1) 0.38s !important; } /   - removed: html body .category-sphere:hover .category-sphere__icon, html body .category-sphere__ball:hover .category-sphere__icon { opacity: 0 !important; filter: blur(4px) !important; } /   - removed: html body .category-sphere:hover .category-sphere__label, html body .category-sphere__ball:hover .category-sphere__label { opacity: 1 !important; } /   - removed: html body .category-sphere__ball::before { content: "" !important; position: absolute !important; inset: 0px !important; border-radius: 50% !important; background: inherit !important; filter: blur(0px) !important; opacity: 0 !important; pointer-events: none !important; transition: opacity 0.3s, filt /   - removed: html body .category-sphere:hover .category-sphere__ball::before, html body .category-sphere__ball:hover::before { opacity: 1 !important; filter: blur(2px) !important; }**
- **Visual change if removed:** None.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 4417-4485). Manual anchor: from `/* ---------- 1. SPHERES: solid neumorphic fills, no pink glow ---------- */` to `}`.
Delete:
```css
/* ---------- 1. SPHERES: solid neumorphic fills, no pink glow ---------- */
html body .category-sphere__ball {
  background: radial-gradient(circle at 30% 22%, #ffffff 0%, #f8fafc 18%, #e8edf3 58%, #d5dde6 100%) !important;
  box-shadow:
    inset -8px -10px 20px rgba(160, 170, 185, 0.45),
    inset  6px  8px 18px rgba(255, 255, 255, 0.95),
    0 12px 28px rgba(60, 70, 90, 0.18),
    0 4px 10px rgba(60, 70, 90, 0.10) !important;
  backdrop-filter: none !important;
  -webkit-backdrop-filter: none !important;
  transition: all 0.75s cubic-bezier(0.42, 0, 0.58, 1) !important;
}
html body .category-sphere:hover .category-sphere__ball {
  transform: none !important; /* kill theme's translateY(-4px) jump */
}
html body .category-sphere__shadow { display: none !important; }

/* ---------- 2. SPHERES: center icon + label, layered above blur ---------- */
html body .category-sphere__ball {
  position: relative !important;
  overflow: hidden !important;
}
html body .category-sphere__ball .category-sphere__icon,
html body .category-sphere__ball .category-sphere__label {
  position: absolute !important;
/* ... 19 more lines, see findings.json exact_text ... */
  filter: blur(4px) !important;
}
html body .category-sphere:hover .category-sphere__label,
html body .category-sphere__ball:hover .category-sphere__label {
  opacity: 1 !important;
}

/* ---------- 4. SPHERE HOVER: blurred overlay (text stays crisp) ------- */
html body .category-sphere__ball::before {
  content: "" !important;
  position: absolute !important;
  inset: 0 !important;
  border-radius: 50% !important;
  background: inherit !important;
  filter: blur(0px) !important;
  opacity: 0 !important;
  pointer-events: none !important;
  transition: opacity 0.3s ease, filter 0.3s ease !important;
  z-index: 0 !important;
}
html body .category-sphere:hover .category-sphere__ball::before,
html body .category-sphere__ball:hover::before {
  opacity: 1 !important;
  filter: blur(2px) !important;
}
```

### T24 [REVIEW] Second copy of the `html body .category-arc .category-sphere...` glass/icon block (the copy that T10 keeps)
- **File:** `assets/toylvia.css` | baseline lines 4599-4633 | kind: styles for non-existent elements
- **Why it is dead:** Every selector needs an ancestor with class `.category-arc`, which no markup has, and the spheres are display:none !important anyway. T10 deletes the first copy (proven duplicates); this deletes the remaining copy.
- **Proof:** Chrome CSSOM: removing the range removes only `html body .category-arc ...` rules. grep: `category-arc` appears only in CSS and in a settings_data custom-CSS selector.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: html body .category-arc .category-sphere:hover .category-sphere__ball .category-sphere__icon:not(#_x_) { transform: translate(-50%, -50%) !important; opacity: 0 !important; filter: blur(4px) !important; } /   - removed: html body .category-arc .category-sphere__ball { background: radial-gradient(circle at 30% 22%, rgba(255, 255, 255, 0.82) 0%, rgba(248, 250, 252, 0.78) 18%, rgba(232, 237, 243, 0.7) 58%, rgba(213, 221, 230, 0.65) 100%) !important; backdrop-filter: blur(6px) saturate(1.1) !important; } /   - removed: html body .category-arc .category-sphere__ball::before { background: inherit !important; } /   - removed: html body .category-arc .category-sphere .category-sphere__ball .category-sphere__icon:not(#_x_) { position: absolute !important; inset: 50% auto auto 50% !important; margin: 0px !important; transform: translate(-50%, -50%) !important; transform-origin: center center !important; z-index: 2 !importan**
- **Visual change if removed:** None.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 4599-4633). Manual anchor: from `/* Icon: perfectly centered - high specificity to beat theme */` to `}`.
Delete:
```css
/* Icon: perfectly centered - high specificity to beat theme */
html body .category-arc .category-sphere .category-sphere__ball .category-sphere__icon:not(#_x_) {
  position: absolute !important;
  left: 50% !important;
  top: 50% !important;
  right: auto !important;
  bottom: auto !important;
  margin: 0 !important;
  transform: translate(-50%, -50%) !important;
  transform-origin: center center !important;
  z-index: 2 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
}
html body .category-arc .category-sphere:hover .category-sphere__ball .category-sphere__icon:not(#_x_) {
  transform: translate(-50%, -50%) !important;
  opacity: 0 !important;
  filter: blur(4px) !important;
}

/* Sphere: translucent glass */
html body .category-arc .category-sphere__ball {
  background: radial-gradient(circle at 30% 22%,
    rgba(255, 255, 255, 0.82) 0%,
    rgba(248, 250, 252, 0.78) 18%,
    rgba(232, 237, 243, 0.70) 58%,
    rgba(213, 221, 230, 0.65) 100%) !important;
  -webkit-backdrop-filter: blur(6px) saturate(1.1) !important;
          backdrop-filter: blur(6px) saturate(1.1) !important;
}
html body .category-arc .category-sphere__ball::before {
  background: inherit !important;
}
```

### T25 [REVIEW] Newsletter form, email input and Subscribe button styles (the form is hidden on every page)
- **File:** `assets/toylvia.css` | baseline lines 715-749 | kind: styles for a hidden element
- **Why it is dead:** `.newsletter__title, .newsletter__subtitle, .newsletter__form { display: none !important }` (baseline ~3610, top level; templates/page.liquid repeats it) hides the form site-wide. The input and button live inside the form (sections/newsletter.liquid), so their styles never render.
- **Proof:** No CSS, inline style or JS gives `.newsletter__form` a display with !important. Chrome CSSOM: removing the range removes exactly 7 newsletter rules.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (min-width: 640px) [group] /   - removed: .newsletter__form { display: flex; flex-direction: column; gap: 0.75rem; max-width: 28rem; margin: 0px auto; } /   - removed: @media (min-width: 640px) > .newsletter__form { flex-direction: row; } /   - removed: .newsletter__input { flex: 1 1 0%; padding: 0.875rem 1rem; border-radius: 0.75rem; border: 2px solid hsl(var(--border)); background: hsl(var(--background)); font-size: 14px; font-weight: 500; color: hsl(var(--foreground)); outline: none; transition: border-color 0.3s, box-shadow 0.3s; } /   - removed: .newsletter__input:focus { border-color: hsl(var(--secondary)); box-shadow: rgba(33, 213, 237, 0.1) 0px 0px 0px 3px; } /   - removed: .newsletter__btn { padding: 0.875rem 1.5rem; border-radius: 0.75rem; background: hsl(var(--secondary)); color: hsl(var(--secondary-foreground)); font-weight: 800; font-size: 14px; transition: background 0.3s; white-space: nowrap; } /   - removed: .newsletter__btn:hover { background: rgba(33, 213, 237, 0.9); }**
- **Visual change if removed:** None. The social icons part of the newsletter section is styled elsewhere and stays.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 715-749). Manual anchor: from `.newsletter__form {` to `.newsletter__btn:hover { background: hsla(187, 85%, 53%, 0.9); }`.
Delete:
```css
.newsletter__form {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  max-width: 28rem;
  margin: 0 auto;
}
@media (min-width: 640px) { .newsletter__form { flex-direction: row; } }
.newsletter__input {
  flex: 1;
  padding: 0.875rem 1rem;
  border-radius: 0.75rem;
  border: 2px solid hsl(var(--border));
  background: hsl(var(--background));
  font-size: 14px;
  font-weight: 500;
  color: hsl(var(--foreground));
  outline: none;
  transition: border-color 0.3s, box-shadow 0.3s;
}
.newsletter__input:focus {
  border-color: hsl(var(--secondary));
  box-shadow: 0 0 0 3px hsla(187,85%,53%,0.1);
}
.newsletter__btn {
  padding: 0.875rem 1.5rem;
  border-radius: 0.75rem;
  background: hsl(var(--secondary));
  color: hsl(var(--secondary-foreground));
  font-weight: 800;
  font-size: 14px;
  transition: background 0.3s;
  white-space: nowrap;
}
.newsletter__btn:hover { background: hsla(187, 85%, 53%, 0.9); }
```

### T26 [REVIEW] The whole old cart-page stylesheet (`.cart`, `.cart__*`), both copies (310 lines)
- **File:** `assets/toylvia.css` | baseline lines 1457-1766 | kind: orphan selectors (feature removed)
- **Why it is dead:** An older cart design, pasted twice. The live cart (templates/cart.liquid) uses `.cart-page`, `.tv-stepper-*`, `.tv-remove-btn`, `.tv-checkout-btn`; the drawer uses `.cart-drawer__*`. No element has the class `cart` or any `cart__*` class.
- **Proof:** grep for `cart__` in all .liquid/.js/.json: 0 hits; no element with the bare class `cart` (regex over class attributes and classList calls). Chrome CSSOM: removing 1457-1766 removes only `.cart` / `.cart__*` rules and their @media wrappers.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (max-width: 768px) [group] /   - removed: @media (max-width: 768px) [group] /   - removed: .cart { padding: 3rem 1rem; } /   - removed: .cart { padding: 3rem 1rem; } /   - removed: .cart__inner { max-width: 900px; margin: 0px auto; } /   - removed: .cart__inner { max-width: 900px; margin: 0px auto; } /   - removed: .cart__header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem; } /   - removed: .cart__back { font-size: 14px; text-decoration: none; color: rgb(85, 85, 85); } /   - removed: .cart__back { font-size: 14px; text-decoration: none; color: rgb(85, 85, 85); } /   - removed: .cart__empty { text-align: center; margin-top: 4rem; } /   - removed: .cart__empty { text-align: center; margin-top: 4rem; } /   - removed: .cart__cta { display: inline-block; margin-top: 1rem; padding: 0.7rem 1.4rem; background: rgb(0, 0, 0); color: rgb(255, 255, 255); border-radius: 999px; } /   - removed: .cart__cta { display: inline-block; margin-top: 1rem; padding: 0.7rem 1.4rem; background: rgb(0, 0, 0); color: rgb(255, 255, 255); border-radius: 999px; } /   - removed: .cart__item { display: grid; grid-template-columns: 90px 1fr auto; gap: 1.2rem; align-items: center; margin-bottom: 1.8rem; } /   - removed: .cart__item { display: grid; grid-template-columns: 90px 1fr auto; gap: 1.2rem; align-items: center; margin-bottom: 1.8rem; } /   - removed: .cart__img { width: 90px; border-radius: 0.5rem; } /   - removed: .cart__img { width: 90px; border-radius: 0.5rem; } /   - removed: .cart__title { font-weight: 700; margin-bottom: 0.3rem; } /   - removed: .cart__variant { font-size: 13px; color: rgb(119, 119, 119); margin-bottom: 0.3rem; } /   - removed: .cart__variant { font-size: 13px; color: rgb(119, 119, 119); margin-bottom: 0.3rem; } /   - removed: .cart__price { font-size: 14px; margin-bottom: 0.4rem; } /   - removed: .cart__price { font-size: 14px; margin-bottom: 0.4rem; } /   - removed: .cart__qty { width: 65px; padding: 0.3rem; } /   - removed: .cart__qty { width: 65px; padding: 0.3rem; } /   - removed: .cart__total { font-weight: 700; } /   - removed: .cart__footer { margin-top: 3rem; display: flex; justify-content: space-between; gap: 2rem; } /   - removed: .cart__footer { margin-top: 3rem; display: flex; justify-content: space-between; gap: 2rem; } /   - removed: .cart__row { display: flex; justify-content: space-between; margin-bottom: 0.5rem; } /   - removed: .cart__row { display: flex; justify-content: space-between; margin-bottom: 0.5rem; } /   - removed: .cart__note { font-size: 13px; color: rgb(119, 119, 119); } /   - removed: .cart__note { font-size: 13px; color: rgb(119, 119, 119); } /   - removed: .cart__actions { display: flex; flex-direction: column; gap: 0.6rem; } /   - removed: .cart__actions { display: flex; flex-direction: column; gap: 0.6rem; } /   - removed: .cart__update { padding: 0.6rem 1.2rem; background: rgb(238, 238, 238); border: none; border-radius: 0.4rem; } /   - removed: .cart__checkout { padding: 1rem 2rem; border-radius: 999px; background: linear-gradient(90deg, rgb(255, 66, 161), rgb(255, 123, 189)); color: rgb(255, 255, 255); font-weight: 800; border: none; } /   - removed: .cart__checkout { padding: 1rem 2rem; border-radius: 999px; background: linear-gradient(90deg, rgb(255, 66, 161), rgb(255, 123, 189)); color: rgb(255, 255, 255); font-weight: 800; border: none; } /   - removed: @media (max-width: 768px) > .cart__item { grid-template-columns: 70px 1fr; } /   - removed: @media (max-width: 768px) > .cart__item { grid-template-columns: 70px 1fr; } /   - removed: @media (max-width: 768px) > .cart__total { grid-column: span 2; text-align: right; } /   - removed: @media (max-width: 768px) > .cart__footer { flex-direction: column; } /   - removed: @media (max-width: 768px) > .cart__footer { flex-direction: column; } /   - removed: .cart__actions { display: flex; flex-direction: column; gap: 0.8rem; } /   - removed: .cart__back-inline { font-size: 14px; color: rgb(102, 102, 102); text-decoration: none; text-align: center; } /   - removed: .cart__back-inline:hover { color: rgb(0, 0, 0); } /   - removed: .cart__header { display: flex; align-items: center; gap: 1rem; margin-bottom: 2rem; } /   - removed: .cart__header { display: flex; align-items: center; gap: 1rem; margin-bottom: 2rem; } /   - removed: .cart__back { font-size: 14px; text-decoration: none; color: rgb(85, 85, 85); white-space: nowrap; } /   - removed: .cart__back:hover { color: rgb(0, 0, 0); } /   - removed: .cart__back:hover { color: rgb(0, 0, 0); } /   - removed: .cart__title { font-size: 24px; font-weight: 800; } /   - removed: .cart__title { font-size: 24px; font-weight: 800; } /   - removed: .cart__name { font-weight: 700; margin-bottom: 0.3rem; } /   - removed: .cart__line { font-weight: 700; } /   - removed: @media (max-width: 768px) > .cart__line { grid-column: span 2; text-align: right; }**
- **Visual change if removed:** None (https://toylvia.com/cart does not use these classes).
- **Notes:** Contains T20 (the proven duplicate half). If approved, apply this instead of T20.
- **Supersedes:** T20. This bigger item already contains them. If Ziko approves it, apply it INSTEAD of T20 and mark those `DONE (covered by T26)`. Apply it before them; once they are applied this item no longer matches.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 1457-1766). Manual anchor: from `/* === CART BASE === */` to `}`.
Delete:
```css
/* === CART BASE === */

.cart {
  padding: 3rem 1rem;
}

.cart__inner {
  max-width: 900px;
  margin: 0 auto;
}

/* HEADER */
.cart__header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.cart__back {
  font-size: 14px;
  text-decoration: none;
  color: #555;
}

/* ... 260 more lines, see findings.json exact_text ... */

.cart__checkout {
  padding: 1rem 2rem;
  border-radius: 999px;
  background: linear-gradient(90deg,#ff42a1,#ff7bbd);
  color: #fff;
  font-weight: 800;
  border: none;
}

/* MOBILE */
@media (max-width: 768px) {
  .cart__item {
    grid-template-columns: 70px 1fr;
  }

  .cart__line {
    grid-column: span 2;
    text-align: right;
  }

  .cart__footer {
    flex-direction: column;
  }
}
```

### T27 [REVIEW] Unused sticky add-to-cart bar and old product-description styles (`.sticky-cart`, `.product-main__description(-full)`)
- **File:** `assets/toylvia.css` | baseline lines 1313-1408 | kind: orphan selectors (feature removed)
- **Why it is dead:** No template renders `.sticky-cart` or `.product-main__description` / `__description-full`. The live product page (sections/product-main.liquid) uses `.product-main__info/top/vendor/title/price/bottom` and the `.pdc*` description card.
- **Proof:** grep of all .liquid/.js/.json: 0 hits for `sticky-cart` and for the description classes outside CSS. Chrome CSSOM: removing the range removes only those rules.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .sticky-cart { position: fixed; bottom: 0px; left: 0px; right: 0px; background: rgb(255, 255, 255); border-top: 1px solid rgb(238, 238, 238); padding: 0.75rem; display: none; z-index: 9999; } /   - removed: .sticky-cart .sticky-cart__btn { width: 100%; padding: 1rem; border-radius: 999px; font-weight: 800; background: linear-gradient(90deg, rgb(255, 66, 161), rgb(255, 123, 189)) !important; color: rgb(255, 255, 255) !important; } /   - removed: @media (max-width: 768px) [group] /   - removed: @media (max-width: 768px) [group] /   - removed: @media (max-width: 768px) > .sticky-cart { display: block; } /   - removed: .product-main__description { margin-top: 2rem; line-height: 1.6; font-size: 14px; color: rgb(68, 68, 68); } /   - removed: .product-main__description-full { max-width: 1100px; margin: 5rem auto 0px; padding: 0px 1.5rem; font-size: 18px; line-height: 1.9; color: rgb(26, 26, 26); } /   - removed: .product-main__description-full h2, .product-main__description-full h3 { font-size: 26px; font-weight: 900; margin: 3rem 0px 1.2rem; letter-spacing: 0.02em; } /   - removed: .product-main__description-full p { margin-bottom: 1.4rem; font-weight: 500; } /   - removed: .product-main__description-full strong { font-weight: 800; color: rgb(0, 0, 0); } /   - removed: .product-main__description-full ul { padding-left: 1.4rem; margin: 1.5rem 0px; } /   - removed: .product-main__description-full li { margin-bottom: 0.7rem; line-height: 1.8; } /   - removed: .product-main__description-full hr { margin: 2.5rem 0px; border-right: none; border-bottom: none; border-left: none; border-image: initial; border-top: 1px solid rgb(221, 221, 221); } /   - removed: @media (max-width: 768px) > .product-main__description-full { font-size: 16px; line-height: 1.7; margin-top: 3rem; } /   - removed: @media (max-width: 768px) > .product-main__description-full h2, .product-main__description-full h3 { font-size: 22px; }**
- **Visual change if removed:** None.
- **Supersedes:** T37. This bigger item already contains them. If Ziko approves it, apply it INSTEAD of T37 and mark those `DONE (covered by T27)`. Apply it before them; once they are applied this item no longer matches.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 1313-1408). Manual anchor: from `/* === STICKY ADD TO CART === */` to `}`.
Delete:
```css
/* === STICKY ADD TO CART === */
.sticky-cart {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background: #fff;
  border-top: 1px solid #eee;
  padding: 0.75rem;
  display: none;
  z-index: 9999;
}

.sticky-cart .sticky-cart__btn {
  width: 100%;
  padding: 1rem;
  border-radius: 999px;
  background: linear-gradient(90deg,#ff42a1,#ff7bbd) !important;
  color: #fff !important;
  font-weight: 800;
}

@media (max-width: 768px) {
  .sticky-cart { display: block; }
}
/* ... 46 more lines, see findings.json exact_text ... */
.product-main__description-full li {
  margin-bottom: 0.7rem;
  line-height: 1.8;
}

/* SEPARATORS */
.product-main__description-full hr {
  margin: 2.5rem 0;
  border: none;
  border-top: 1px solid #ddd;
}

/* MOBILE FIX */
@media (max-width: 768px) {
  .product-main__description-full {
    font-size: 16px;
    line-height: 1.7;
    margin-top: 3rem;
  }

  .product-main__description-full h2,
  .product-main__description-full h3 {
    font-size: 22px;
  }
}
```

### T28 [REVIEW] Variant pill-button styles (`.product-variants__options`, `.product-variants__btn*`) for buttons the product page no longer renders
- **File:** `assets/toylvia.css` | baseline lines 2187-2255 | kind: orphan selectors (feature removed)
- **Why it is dead:** Variants are now a dropdown (`.product-variants__select` inside `.product-variants__select-wrap`). The options row and pill buttons are never output. The live `.product-variants`, `__group`, `__label` rules above (2173-2185) are not included.
- **Proof:** grep: `product-variants__btn` appears in no .liquid/.js/.json; `product-variants__options` appears only inside CSS (settings_data custom CSS and an inline <style> in product-main.liquid), never in markup.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .product-variants__options { display: flex; flex-wrap: wrap; gap: 10px; justify-content: flex-start; } /   - removed: .product-variants__btn { position: relative; display: inline-flex; align-items: center; justify-content: center; min-width: 80px; padding: 7px 16px; border-radius: 999px; background: rgb(255, 255, 255); color: rgb(26, 26, 46); font-size: 0.82rem; font-weight: 600; letter-spacing: 0.03em; cursor: poi /   - removed: .product-variants__btn:hover:not(.disabled):not(.selected) { border-color: rgb(255, 66, 161); background: rgb(255, 245, 250); color: rgb(255, 66, 161); box-shadow: none; transform: none; } /   - removed: .product-variants__btn:not(.disabled):active { background: rgb(255, 232, 244); border-color: rgb(255, 66, 161); box-shadow: none; transform: none; } /   - removed: .product-variants__btn.selected { background: rgb(255, 245, 250); color: rgb(255, 66, 161); box-shadow: none; padding-bottom: 7px; border: 2px solid rgb(255, 66, 161) !important; } /   - removed: .product-variants__btn.selected::after { display: none; } /   - removed: .product-variants__btn.disabled:not(.selected) { opacity: 0.4; cursor: not-allowed; text-decoration: line-through; color: rgb(187, 187, 187); border-color: rgb(229, 231, 235); background: rgb(249, 250, 251); box-shadow: none; } /   - removed: .product-variants__btn.disabled.selected { cursor: not-allowed; }**
- **Visual change if removed:** None.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 2187-2255). Manual anchor: from `.product-variants__options {` to `}`.
Delete:
```css
.product-variants__options {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: flex-start;
}

.product-variants__btn {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 80px;
  padding: 7px 16px;
  border-radius: 999px;
  border: 1.5px solid #d1d5db !important;
  background: #fff;
  color: #1a1a2e;
  font-size: 0.82rem;
  font-weight: 600;
  letter-spacing: 0.03em;
  cursor: pointer;
  transition: border-color 0.15s ease, background 0.15s ease, color 0.15s ease;
  box-shadow: none;
  outline: none;
/* ... 19 more lines, see findings.json exact_text ... */
.product-variants__btn.selected {
  border: 2px solid #ff42a1 !important;
  background: #fff5fa;
  color: #ff42a1;
  box-shadow: none;
  padding-bottom: 7px;
}

.product-variants__btn.selected::after {
  display: none;
}

.product-variants__btn.disabled:not(.selected) {
  opacity: 0.4;
  cursor: not-allowed;
  text-decoration: line-through;
  color: #bbb;
  border-color: #e5e7eb;
  background: #f9fafb;
  box-shadow: none;
}

.product-variants__btn.disabled.selected {
  cursor: not-allowed;
}
```

### T29 [REVIEW] 'Neumorphic trust badges - product page' block for `.product-trust-badges`, which is never rendered
- **File:** `assets/toylvia.css` | baseline lines 2350-2396 | kind: orphan selectors (feature removed)
- **Why it is dead:** Every selector needs a `.product-trust-badges` ancestor. The product page now uses the `.pdp-trust-trio` component instead.
- **Proof:** grep: `product-trust-badges` appears in no .liquid/.js/.json file. Chrome CSSOM: only these rules are removed.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .product-trust-badges { display: flex; flex-wrap: nowrap; gap: 8px; margin-top: 1.5rem; padding-top: 0px; border-top: none; overflow: visible; } /   - removed: .product-trust-badges .trust-badge { display: flex; align-items: center; gap: 6px; font-size: 12px; font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; color: rgb(68, 68, 68); background: rgb(235, 235, 238); padding: 8px 10px; border-radius: 50px; box-shadow: rgba(0, 0, 0, 0.13) 5px /   - removed: .product-trust-badges .trust-badge:hover { box-shadow: rgba(0, 0, 0, 0.15) 6px 6px 15px, rgb(255, 255, 255) -6px -6px 15px; } /   - removed: .product-trust-badges .trust-badge__icon { width: 15px; height: 15px; color: hsl(var(--toylvia-pink, 330 100% 63%)); stroke: hsl(var(--toylvia-pink, 330 100% 63%)); flex-shrink: 0; }**
- **Visual change if removed:** None.
- **Supersedes:** T43. This bigger item already contains them. If Ziko approves it, apply it INSTEAD of T43 and mark those `DONE (covered by T29)`. Apply it before them; once they are applied this item no longer matches.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 2350-2396). Manual anchor: from `/* ========================================` to `}`.
Delete:
```css
/* ========================================
   NEUMORPHIC TRUST BADGES - PRODUCT PAGE (SINGLE ROW)
   ======================================== */

.product-trust-badges {
  display: flex;
  flex-wrap: nowrap;
  gap: 8px;
  margin-top: 1.5rem;
  padding-top: 0;
  border-top: none;
  overflow: visible;
}

.product-trust-badges .trust-badge {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: #444;
  background: #ebebee;
  padding: 8px 10px;
  border-radius: 50px;
  box-shadow:
    5px 5px 12px rgba(0, 0, 0, 0.13),
    -5px -5px 12px rgba(255, 255, 255, 0.95);
  transition: box-shadow 0.2s ease;
  white-space: nowrap;
  flex-shrink: 0;
}

.product-trust-badges .trust-badge:hover {
  box-shadow:
    6px 6px 15px rgba(0, 0, 0, 0.15),
    -6px -6px 15px rgba(255, 255, 255, 1);
}

.product-trust-badges .trust-badge__icon {
  width: 15px;
  height: 15px;
  color: hsl(var(--toylvia-pink, 330 100% 63%));
  stroke: hsl(var(--toylvia-pink, 330 100% 63%));
  flex-shrink: 0;
}
```

### T30 [REVIEW] Unused 'BRAND LOADER' (`#brand-loader`, `.pl`, `.pl__dot*` and 15 dot-* @keyframes, 157 lines)
- **File:** `assets/toylvia.css` | baseline lines 3690-3846 | kind: orphan selectors (feature removed)
- **Why it is dead:** A full-screen dot-spinner loader that the theme never outputs; no script adds `.bl-hidden`. The 15 keyframes are used only by these `.pl__dot` rules.
- **Proof:** grep: `brand-loader`, `pl__dot`, `bl-hidden` appear in no .liquid/.js/.json file. Chrome CSSOM: removing the range removes exactly the 45 loader rules and keyframes.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: #brand-loader { position: fixed; inset: 0px; z-index: 9999; display: flex; align-items: center; justify-content: center; background: hsla(var(--background), 0.95); backdrop-filter: blur(4px); transition: opacity 0.4s, visibility 0.4s; } /   - removed: #brand-loader.bl-hidden { opacity: 0; visibility: hidden; pointer-events: none; } /   - removed: .pl { aspect-ratio: 1 / 1; display: grid; gap: 1em; grid-template-columns: repeat(3, 1fr); grid-template-rows: repeat(3, 1fr); width: 8em; } /   - removed: .pl__dot { position: relative; } /   - removed: .pl__dot, .pl__dot::before, .pl__dot::after { animation-duration: 2s; animation-timing-function: linear; animation-iteration-count: infinite; } /   - removed: .pl__dot::before, .pl__dot::after { aspect-ratio: 1 / 1; background-color: hsl(var(--foreground)); border-radius: 50%; content: ""; display: block; position: absolute; width: 100%; transition: background-color 0.3s; } /   - removed: .pl__dot::after { top: 50%; left: 50%; transform: translate(-50%, -50%) scale(0); } /   - removed: .pl__dot--red::before, .pl__dot--red::after { background-color: rgb(245, 61, 61); } /   - removed: .pl__dot--yellow::before, .pl__dot--yellow::after { background-color: rgb(242, 185, 13); } /   - removed: .pl__dot--green::before, .pl__dot--green::after { background-color: rgb(10, 194, 102); } /   - removed: .pl__dot--blue::before, .pl__dot--blue::after { background-color: rgb(13, 128, 242); } /   - removed: .pl__dot--lg::after { width: 500%; } /   - removed: .pl__dot--sm::after { width: 167%; } /   - removed: .pl__dot:nth-child(1)::before { animation-name: dot-scale1; } /   - removed: .pl__dot:nth-child(2) { animation-name: dot-rotate; transform-origin: 50% 200%; } /   - removed: .pl__dot:nth-child(2)::before { animation-name: dot-scale2; } /   - removed: .pl__dot:nth-child(3)::before { animation-name: dot-scale3; } /   - removed: .pl__dot:nth-child(3)::after { animation-name: dot-wave3; } /   - removed: .pl__dot:nth-child(4) { animation-name: dot-rotate; transform-origin: 200% 50%; } /   - removed: .pl__dot:nth-child(4)::before { animation-name: dot-scale4; } /   - removed: .pl__dot:nth-child(5)::before { animation-name: dot-scale5; } /   - removed: .pl__dot:nth-child(5)::after { animation-name: dot-wave5a, dot-wave5b; } /   - removed: .pl__dot:nth-child(6) { animation-name: dot-rotate; transform-origin: -100% 50%; } /   - removed: .pl__dot:nth-child(6)::before { animation-name: dot-scale6; } /   - removed: .pl__dot:nth-child(7)::before { animation-name: dot-scale7; } /   - removed: .pl__dot:nth-child(7)::after { animation-name: dot-wave7; } /   - removed: .pl__dot:nth-child(8) { animation-name: dot-rotate; transform-origin: 50% -100%; } /   - removed: .pl__dot:nth-child(8)::before { animation-name: dot-scale8; } /   - removed: .pl__dot:nth-child(9)::before { animation-name: dot-scale9; } /   - removed: .pl__dot:nth-child(9)::after { animation-name: dot-wave9; } /   - removed: @keyframes dot-rotate { 0%, 22% { animation-timing-function: ease-out; transform: rotate(-45deg); } 37%, 100% { transform: rotate(0deg); } } /   - removed: @keyframes dot-scale1 { 0%, 36% { transform: translate(0px, 0px) scale(0); } 50%, 71% { transform: translate(0px, 0px) scale(1); } 87%, 100% { transform: translate(75%, 75%) scale(0); } } /   - removed: @keyframes dot-scale2 { 0%, 25% { animation-timing-function: ease-out; transform: translate(0px, 0px) scale(0); } 40%, 71% { transform: translate(0px, 0px) scale(1); } 87%, 100% { transform: translate(0px, -100%) scale(0); } } /   - removed: @keyframes dot-scale3 { 0%, 27% { animation-timing-function: ease-in; transform: translate(0px, 0px) scale(0); } 45%, 71% { transform: translate(0px, 0px) scale(1); } 87%, 100% { transform: translate(-75%, 75%) scale(0); } } /   - removed: @keyframes dot-scale4 { 0%, 28% { animation-timing-function: ease-out; transform: translate(0px, 0px) scale(0); } 43%, 71% { transform: translate(0px, 0px) scale(1); } 87%, 100% { transform: translate(-100%, 0px) scale(0); } } /   - removed: @keyframes dot-scale5 { 0%, 9%, 100% { transform: scale(0); } 26% { transform: scale(1.17); } 41%, 75% { transform: scale(1); } } /   - removed: @keyframes dot-scale6 { 0%, 22% { animation-timing-function: ease-out; transform: translate(0px, 0px) scale(0); } 37%, 71% { transform: translate(0px, 0px) scale(1); } 87%, 100% { transform: translate(100%, 0px) scale(0); } } /   - removed: @keyframes dot-scale7 { 0%, 36% { animation-timing-function: ease-in; transform: translate(0px, 0px) scale(0); } 53%, 71% { transform: translate(0px, 0px) scale(1); } 87%, 100% { transform: translate(75%, -75%) scale(0); } } /   - removed: @keyframes dot-scale8 { 0%, 24% { animation-timing-function: ease-out; transform: translate(0px, 0px) scale(0); } 39%, 71% { transform: translate(0px, 0px) scale(1); } 87%, 100% { transform: translate(0px, 100%) scale(0); } } /   - removed: @keyframes dot-scale9 { 0%, 32% { animation-timing-function: ease-in; transform: translate(0px, 0px) scale(0); } 49%, 71% { transform: translate(0px, 0px) scale(1); } 87%, 100% { transform: translate(-75%, -75%) scale(0); } } /   - removed: @keyframes dot-wave3 { 0% { visibility: hidden; } 45% { opacity: 1; transform: translate(-50%, -50%) scale(calc(0.598802)); visibility: hidden; } 61%, 100% { opacity: 0; transform: translate(-50%, -50%) scale(1); } } /   - removed: @keyframes dot-wave5a { 0% { transform: translate(-50%, -50%) scale(0.2); } 8% { transform: translate(-50%, -50%) scale(0.8); } 25%, 100% { transform: translate(-50%, -50%) scale(1); } } /   - removed: @keyframes dot-wave5b { 0%, 25%, 100% { opacity: 0; } 8% { opacity: 0.5; } } /   - removed: @keyframes dot-wave7 { 0% { visibility: hidden; } 53% { opacity: 1; transform: translate(-50%, -50%) scale(calc(0.598802)); visibility: hidden; } 69%, 100% { opacity: 0; transform: translate(-50%, -50%) scale(1); } } /   - removed: @keyframes dot-wave9 { 0% { visibility: hidden; } 49% { opacity: 1; transform: translate(-50%, -50%) scale(calc(0.598802)); visibility: hidden; } 65%, 100% { opacity: 0; transform: translate(-50%, -50%) scale(1); } }**
- **Visual change if removed:** None. (snippets/toylvia-loader.liquid is a different loader and has its own styles.)
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 3690-3846). Manual anchor: from `/* === BRAND LOADER === */` to `}`.
Delete:
```css
/* === BRAND LOADER === */
#brand-loader {
  position: fixed;
  inset: 0;
  z-index: 9999;
  display: flex;
  align-items: center;
  justify-content: center;
  background: hsla(var(--background), 0.95);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  transition: opacity 0.4s ease, visibility 0.4s ease;
}
#brand-loader.bl-hidden {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
}
.pl {
  aspect-ratio: 1;
  display: grid;
  gap: 1em;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(3, 1fr);
  width: 8em;
/* ... 107 more lines, see findings.json exact_text ... */
}
@keyframes dot-wave3 {
  from { visibility: hidden; }
  45% { opacity: 1; transform: translate(-50%, -50%) scale(calc(1 / 1.67)); visibility: hidden; }
  61%, to { opacity: 0; transform: translate(-50%, -50%) scale(1); }
}
@keyframes dot-wave5a {
  from { transform: translate(-50%, -50%) scale(0.2); }
  8% { transform: translate(-50%, -50%) scale(0.8); }
  25%, to { transform: translate(-50%, -50%) scale(1); }
}
@keyframes dot-wave5b {
  from, 25%, to { opacity: 0; }
  8% { opacity: 0.5; }
}
@keyframes dot-wave7 {
  from { visibility: hidden; }
  53% { opacity: 1; transform: translate(-50%, -50%) scale(calc(1 / 1.67)); visibility: hidden; }
  69%, to { opacity: 0; transform: translate(-50%, -50%) scale(1); }
}
@keyframes dot-wave9 {
  from { visibility: hidden; }
  49% { opacity: 1; transform: translate(-50%, -50%) scale(calc(1 / 1.67)); visibility: hidden; }
  65%, to { opacity: 0; transform: translate(-50%, -50%) scale(1); }
}
```

### T31 [REVIEW] Unused 'ICE CARD CATEGORY GRID' feature (`.cat-ice-*`, 220 lines)
- **File:** `assets/toylvia.css` | baseline lines 5313-5532 | kind: orphan selectors (feature removed)
- **Why it is dead:** No element uses any `.cat-ice-*` class. The live category grid uses `.cat-grid` / `.cat-card`.
- **Proof:** grep: `cat-ice` appears in no .liquid/.js/.json file. The range is brace-balanced and stops BEFORE the 'RESPONSIVE' comment and the unclosed `@media (max-width: 1024px) {` opener (must stay). Chrome CSSOM: removes only `.cat-ice-*` rules.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (hover: hover) and (pointer: fine) [group] /   - removed: @keyframes cat-ice-float { 0%, 100% { transform: translateY(0px); } 50% { transform: translateY(-10px); } } /   - removed: .cat-ice-grid { display: flex; flex-wrap: nowrap; justify-content: center; gap: 20px; padding: 40px 24px 20px; position: relative; } /   - removed: .cat-ice-card { flex: 1 1 0px; min-width: 0px; position: relative; display: flex; flex-direction: column; align-items: center; text-decoration: none; cursor: pointer; animation: 3.8s ease-in-out 0s infinite normal none running cat-ice-float; transition: filter 0.5s, transform 0.45s cubic-bezier(0.34 /   - removed: .cat-ice-card:nth-child(1) { animation-delay: 0s; } /   - removed: .cat-ice-card:nth-child(2) { animation-delay: 0.5s; } /   - removed: .cat-ice-card:nth-child(3) { animation-delay: 1s; } /   - removed: .cat-ice-card:nth-child(4) { animation-delay: 1.5s; } /   - removed: .cat-ice-card:nth-child(5) { animation-delay: 2s; } /   - removed: .cat-ice-card:nth-child(6) { animation-delay: 2.5s; } /   - removed: .cat-ice-frame { position: relative; width: 100%; aspect-ratio: 1 / 1; border-radius: 28px; background: linear-gradient(135deg, rgba(255, 255, 255, 0.72) 0%, rgba(220, 240, 255, 0.48) 40%, rgba(190, 225, 255, 0.38) 100%); backdrop-filter: blur(18px) saturate(1.4); border: 1px solid rgba(255, 255, 25 /   - removed: .cat-ice-frame::before { content: ""; position: absolute; inset: 0px; border-radius: inherit; background: linear-gradient(135deg, rgba(255, 255, 255, 0.55) 0%, rgba(255, 255, 255, 0) 55%); pointer-events: none; z-index: 2; } /   - removed: .cat-ice-frame::after { content: ""; position: absolute; top: 10px; left: 12px; width: 36px; height: 36px; background: radial-gradient(circle, rgba(255, 255, 255, 0.9) 0%, rgba(255, 255, 255, 0) 70%); pointer-events: none; z-index: 3; } /   - removed: .cat-ice-glow { position: absolute; inset: -20px; border-radius: 40px; background: radial-gradient(ellipse at center, /                                                                                                                                                                                        /   - removed: .cat-ice-img-wrap { position: relative; width: 82%; aspect-ratio: 1 / 1; display: flex; align-items: center; justify-content: center; z-index: 1; } /   - removed: .cat-ice-img { display: block; width: 100%; height: 100%; object-fit: contain; transition: filter 0.5s, transform 0.45s; filter: drop-shadow(rgba(0, 0, 0, 0.18) 0px 12px 20px) drop-shadow(rgba(0, 0, 0, 0.1) 0px 4px 8px); } /   - removed: .cat-ice-img-shadow { position: absolute; bottom: -4px; left: 50%; transform: translateX(-50%) scaleX(0.75) scaleY(0.3); width: 70%; height: 28px; background: radial-gradient(rgba(60, 80, 120, 0.35) 0%, transparent 70%); filter: blur(6px); border-radius: 50%; transition: transform 0.45s, opacity 0.4 /   - removed: .cat-ice-light-emit { position: absolute; inset: 10px; border-radius: 50%; background: radial-gradient(circle, /                                                                                                                                                                                               /   - removed: .cat-ice-label { margin-top: 14px; font-size: 13px; font-weight: 800; letter-spacing: 0.12em; text-transform: uppercase; color: rgb(45, 58, 74); text-align: center; transition: color 0.4s, transform 0.45s cubic-bezier(0.34, 1.56, 0.64, 1); } /   - removed: .cat-ice-desc { margin-top: 4px; font-size: 11.5px; color: rgb(122, 143, 166); text-align: center; letter-spacing: 0.03em; transition: color 0.4s, transform 0.45s cubic-bezier(0.34, 1.56, 0.64, 1); } /   - removed: @media (hover: hover) and (pointer: fine) > .cat-ice-grid.cat-ice-active .cat-ice-card { filter: brightness(0.52) saturate(0.7); } /   - removed: @media (hover: hover) and (pointer: fine) > .cat-ice-grid.cat-ice-active .cat-ice-card.cat-ice-on { filter: brightness(1.18) saturate(1.2) !important; transform: translateY(-14px) !important; animation: auto ease 0s 1 normal none running none !important; } /   - removed: @media (hover: hover) and (pointer: fine) > .cat-ice-card.cat-ice-on .cat-ice-glow { opacity: 0.5; } /   - removed: @media (hover: hover) and (pointer: fine) > .cat-ice-card.cat-ice-on .cat-ice-img-shadow { transform: translateX(-50%) scaleX(0.45) scaleY(0.18); width: 50%; opacity: 0.5; } /   - removed: @media (hover: hover) and (pointer: fine) > .cat-ice-card.cat-ice-on .cat-ice-light-emit { opacity: 0.5; } /   - removed: @media (hover: hover) and (pointer: fine) > .cat-ice-card.cat-ice-on .cat-ice-img { filter: drop-shadow(0 0 14px var(--card-accent, rgba(255,255,255,0.6))) /             drop-shadow(0 16px 28px rgba(0,0,0,0.22)); } /   - removed: @media (hover: hover) and (pointer: fine) > .cat-ice-card.cat-ice-on .cat-ice-label, .cat-ice-card.cat-ice-on .cat-ice-desc { transform: translateY(10px); } /   - removed: @media (hover: hover) and (pointer: fine) > .cat-ice-card.cat-ice-on .cat-ice-label { background: rgba(255, 255, 255, 0.78); border-radius: 6px; padding: 3px 8px; }**
- **Visual change if removed:** None.
- **Notes:** Contains T16 (the broken banner comment). The 3 `.cat-ice-*` lines inside the unclosed @media opener area are NOT touched (see Known issues).
- **Supersedes:** T16. This bigger item already contains them. If Ziko approves it, apply it INSTEAD of T16 and mark those `DONE (covered by T31)`. Apply it before them; once they are applied this item no longer matches.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 5313-5532). Manual anchor: from `/* ============================================================` to `}`.
Delete:
```css
            /* ============================================================
               ICE CARD CATEGORY GRID  –  Toylvia
                  /* =====================================================
                     ICE CATEGORY CARDS — complete rewrite
                        ===================================================== */

                        /* Float keyframe */
                        @keyframes cat-ice-float {
                          0%,100% { transform: translateY(0px); }
                            50%      { transform: translateY(-10px); }
                            }

                            /* Grid container */
                            .cat-ice-grid {
                              display: flex;
                                flex-wrap: nowrap;
                                  justify-content: center;
                                    gap: 20px;
                                      padding: 40px 24px 20px;
                                        position: relative;
                                        }

                                        /* Each card link */
                                        .cat-ice-card {
                                          flex: 1 1 0;
/* ... 170 more lines, see findings.json exact_text ... */
    filter: brightness(1.18) saturate(1.2) !important;
    transform: translateY(-14px) !important;
    animation: none !important;
  }
  .cat-ice-card.cat-ice-on .cat-ice-glow { opacity: 0.5; }
  .cat-ice-card.cat-ice-on .cat-ice-img-shadow {
    transform: translateX(-50%) scaleX(0.45) scaleY(0.18);
    width: 50%;
    opacity: 0.5;
  }
  .cat-ice-card.cat-ice-on .cat-ice-light-emit { opacity: 0.5; }
  .cat-ice-card.cat-ice-on .cat-ice-img {
    filter: drop-shadow(0 0 14px var(--card-accent, rgba(255,255,255,0.6)))
            drop-shadow(0 16px 28px rgba(0,0,0,0.22));
  }
  .cat-ice-card.cat-ice-on .cat-ice-label,
  .cat-ice-card.cat-ice-on .cat-ice-desc {
    transform: translateY(10px);
  }
  .cat-ice-card.cat-ice-on .cat-ice-label {
    background: rgba(255,255,255,0.78);
    border-radius: 6px;
    padding: 3px 8px;
  }
}
```

### T32 [REVIEW] Unused 'PRODUCT DESCRIPTION CARD' styles (`.product-desc-card*`)
- **File:** `assets/toylvia.css` | baseline lines 5729-5835 | kind: orphan selectors (feature removed)
- **Why it is dead:** An older description-card design. The live product page uses `#product-desc-wrap` and the `.pdc*` classes, styled by the second 'PRODUCT DESCRIPTION CARD' block further down (kept).
- **Proof:** grep: `product-desc-card` appears in no .liquid/.js/.json file. The range is inside the unclosed 1024px @media and stays balanced (depth 1 at both ends). Chrome CSSOM: removes 13 `.product-desc-card*` rules plus one nested @media.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (max-width: 1024px) > @media (max-width: 767px) [group] /   - removed: @media (max-width: 1024px) > .product-desc-card { max-width: 1200px; margin: 3rem auto 2rem; padding: 0px 1.5rem; } /   - removed: @media (max-width: 1024px) > .product-desc-card__label { display: inline-flex; align-items: center; gap: 0.5rem; font-size: 0.75rem; font-weight: 800; letter-spacing: 0.1em; text-transform: uppercase; color: rgb(255, 66, 161); margin-bottom: 0.75rem; } /   - removed: @media (max-width: 1024px) > .product-desc-card__label::before { content: ""; display: inline-block; width: 28px; height: 3px; background: rgb(255, 66, 161); border-radius: 2px; } /   - removed: @media (max-width: 1024px) > .product-desc-card__body { background: rgb(255, 255, 255); border-radius: 1.25rem; border: 2px solid hsl(var(--border)); box-shadow: rgba(0, 0, 0, 0.05) 0px 4px 24px; padding: 2.5rem 3rem; font-size: 17px; line-height: 1.9; color: rgb(51, 51, 51); position: relative; ove /   - removed: @media (max-width: 1024px) > .product-desc-card__body::before { content: ""; position: absolute; top: 0px; left: 0px; width: 5px; height: 100%; background: linear-gradient(180deg, #ff42a1, hsl(var(--secondary))); border-radius: 4px 0px 0px 4px; } /   - removed: @media (max-width: 1024px) > .product-desc-card__body h2, .product-desc-card__body h3 { font-size: 1.3rem; font-weight: 800; color: rgb(255, 66, 161); margin: 2rem 0px 0.6rem; letter-spacing: 0.01em; } /   - removed: @media (max-width: 1024px) > .product-desc-card__body h2:first-child, .product-desc-card__body h3:first-child { margin-top: 0px; } /   - removed: @media (max-width: 1024px) > .product-desc-card__body p { margin-bottom: 1.1rem; } /   - removed: @media (max-width: 1024px) > .product-desc-card__body p:last-child { margin-bottom: 0px; } /   - removed: @media (max-width: 1024px) > .product-desc-card__body ul { list-style: none; padding: 0px; margin: 1rem 0px; } /   - removed: @media (max-width: 1024px) > .product-desc-card__body ul li { padding-left: 1.5rem; position: relative; margin-bottom: 0.55rem; line-height: 1.7; } /   - removed: @media (max-width: 1024px) > .product-desc-card__body ul li::before { content: ""; position: absolute; left: 0px; top: 0.55em; width: 8px; height: 8px; background: rgb(255, 66, 161); border-radius: 50%; } /   - removed: @media (max-width: 1024px) > .product-desc-card__body strong { font-weight: 700; color: rgb(17, 17, 17); } /   - removed: @media (max-width: 1024px) > @media (max-width: 767px) > .product-desc-card { padding: 0px 0.75rem; margin-top: 2rem; } /   - removed: @media (max-width: 1024px) > @media (max-width: 767px) > .product-desc-card__body { padding: 1.5rem 1.25rem; font-size: 15px; } /   - removed: @media (max-width: 1024px) > @media (max-width: 767px) > .product-desc-card__body h2, .product-desc-card__body h3 { font-size: 1.1rem; }**
- **Visual change if removed:** None.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 5729-5835). Manual anchor: from `/* =============================================` to `}`.
Delete:
```css
/* =============================================
   PRODUCT DESCRIPTION CARD
   ============================================= */
.product-desc-card {
  max-width: 1200px;
  margin: 3rem auto 2rem;
  padding: 0 1.5rem;
}

.product-desc-card__label {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.75rem;
  font-weight: 800;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #ff42a1;
  margin-bottom: 0.75rem;
}
.product-desc-card__label::before {
  content: '';
  display: inline-block;
  width: 28px;
  height: 3px;
/* ... 57 more lines, see findings.json exact_text ... */
  margin-bottom: 0.55rem;
  line-height: 1.7;
}
.product-desc-card__body ul li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0.55em;
  width: 8px;
  height: 8px;
  background: #ff42a1;
  border-radius: 50%;
}

.product-desc-card__body strong {
  font-weight: 700;
  color: #111;
}

@media (max-width: 767px) {
  .product-desc-card { padding: 0 0.75rem; margin-top: 2rem; }
  .product-desc-card__body { padding: 1.5rem 1.25rem; font-size: 15px; }
  .product-desc-card__body h2,
  .product-desc-card__body h3 { font-size: 1.1rem; }
}
```

### T33 [REVIEW] Superseded card shadow, connector-line and text-area spacing tweaks (11 rules)
- **File:** `assets/live-card-fixes.css` | baseline lines 60-78 | kind: overridden rules (cross-file)
- **Why it is dead:** Old tweaks that later rules replaced: card box-shadows lose to card-look.css 19-21 (#MainContent x304, !important); connector sizes and text spacing lose to later !important rules in the same file.
- **Proof:** Property-by-property check by two agents; Chrome CSSOM shows exactly the 11 rules removed. REVIEW because part of the proof relies on very high specificity in another file (Chrome caps an ID count at 255, which still wins).
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: html body #MainContent .cr-card, html body #MainContent .product-card { box-shadow: rgba(0, 0, 0, 0.07) 0px 1px 5px, rgba(0, 0, 0, 0.04) 0px 1px 2px !important; } /   - removed: @media (hover: hover) [group] /   - removed: @media (hover: hover) > html body #MainContent .cr-card:hover, html body #MainContent .product-card:hover { box-shadow: rgba(0, 0, 0, 0.1) 0px 3px 8px, rgba(0, 0, 0, 0.04) 0px 1px 2px !important; } /   - removed: html body #MainContent#MainContent .cr-card__img-wrap > .cr-card__tag.cr-card__tag.cr-card__tag::before, html body #MainContent#MainContent .product-card__image-wrap > .product-card__tag.product-card__tag.product-card__tag::before, html body #MainContent#MainContent .cr-card__img-wrap > .soft-dot >  /   - removed: html body #MainContent#MainContent#MainContent .cr-card.cr-card.cr-card .cr-card__body { height: auto !important; min-height: 0px !important; justify-content: flex-start !important; gap: 6px !important; } /   - removed: html body #MainContent#MainContent#MainContent .cr-card.cr-card.cr-card .cr-card__name { min-height: 31px !important; margin: 0px !important; } /   - removed: html body #MainContent#MainContent#MainContent .cr-card.cr-card.cr-card .cr-card__footer { margin-top: 0px !important; } /   - removed: html body #MainContent#MainContent#MainContent .cr-card.cr-card.cr-card .cr-card__body { padding: 5px 9px 4px !important; gap: 3px !important; } /   - removed: html body #MainContent#MainContent#MainContent .cr-card.cr-card.cr-card .cr-card__name { min-height: 30px !important; } /   - removed: html body #MainContent#MainContent#MainContent .cr-card.cr-card.cr-card .cr-card__footer { margin-top: 0px !important; margin-bottom: 0px !important; } /   - removed: html body #MainContent#MainContent#MainContent .cr-card.cr-card.cr-card .card-shop-action { margin-bottom: 0px !important; }**
- **Visual change if removed:** None.
- **Supersedes:** T56. This bigger item already contains them. If Ziko approves it, apply it INSTEAD of T56 and mark those `DONE (covered by T33)`. Apply it before them; once they are applied this item no longer matches.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 60-78). Manual anchor: from `html body #MainContent .cr-card,html body #MainContent .product-card{box-shadow:0 1px 5...` to `html body #MainContent#MainContent#MainContent .cr-card.cr-card.cr-card .card-shop-acti...`.
Delete:
```css
html body #MainContent .cr-card,html body #MainContent .product-card{box-shadow:0 1px 5px rgba(0,0,0,.07),0 1px 2px rgba(0,0,0,.04)!important}
@media(hover:hover){html body #MainContent .cr-card:hover,html body #MainContent .product-card:hover{box-shadow:0 3px 8px rgba(0,0,0,.10),0 1px 2px rgba(0,0,0,.04)!important}}

/* Tag connector line runs from the circle's right edge to the card's right edge. */
html body #MainContent#MainContent .cr-card__img-wrap>.cr-card__tag.cr-card__tag.cr-card__tag::before,
html body #MainContent#MainContent .product-card__image-wrap>.product-card__tag.product-card__tag.product-card__tag::before,
html body #MainContent#MainContent .cr-card__img-wrap>.soft-dot>.tag-edge-line,
html body #MainContent#MainContent .product-card__image-wrap>.soft-dot>.tag-edge-line{width:calc(2px + var(--marker-inset,8.68625px))!important;min-width:calc(2px + var(--marker-inset,8.68625px))!important;height:.5px!important}

/* Title-to-price gap: size the card body to its content instead of a fixed 100px with the price pushed to the bottom. */
html body #MainContent#MainContent#MainContent .cr-card.cr-card.cr-card .cr-card__body{height:auto!important;min-height:0!important;justify-content:flex-start!important;gap:6px!important}
html body #MainContent#MainContent#MainContent .cr-card.cr-card.cr-card .cr-card__name{min-height:31px!important;margin:0!important}
html body #MainContent#MainContent#MainContent .cr-card.cr-card.cr-card .cr-card__footer{margin-top:0!important}

/* Tighter card text area (about 5% shorter card); the image area is untouched. */
html body #MainContent#MainContent#MainContent .cr-card.cr-card.cr-card .cr-card__body{padding:5px 9px 4px!important;gap:3px!important}
html body #MainContent#MainContent#MainContent .cr-card.cr-card.cr-card .cr-card__name{min-height:30px!important}
html body #MainContent#MainContent#MainContent .cr-card.cr-card.cr-card .cr-card__footer{margin-top:0!important;margin-bottom:0!important}
html body #MainContent#MainContent#MainContent .cr-card.cr-card.cr-card .card-shop-action{margin-bottom:0!important}
```

### T34 [REVIEW] Unused 'marker cluster' layout (`.card-marker-cluster`, `.drift-marker-cluster`) plus a duplicate body-height rule
- **File:** `assets/live-card-fixes.css` | baseline lines 319-339 | kind: orphan selectors + duplicate
- **Why it is dead:** The cluster wrapper classes appear nowhere in markup or JS. Line 339 matches the same elements as line 341 with the same declarations.
- **Proof:** grep `cluster` in all .liquid/.js/.json: 0 hits. Chrome CSSOM: removes exactly the 6 cluster rules and line 339.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (max-width: 767px) [group] /   - removed: html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .card-marker-cluster, html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#Main /   - removed: html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .card-marker-cluster > .age-tag, html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainC /   - removed: html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .card-marker-cluster > .cr-card__tag::before, html body #MainContent#MainContent#MainContent#MainContent#Main /   - removed: @media (max-width: 767px) > html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .card-marker-cluster, html body #MainContent#MainContent#MainContent#MainContent# /   - removed: html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .drift-marker-cluster > [data-drift-category] { display: block !important; width: 8.4px !important; min-width /   - removed: html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .cr-card .card-marker-cluster, html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainCon /   - removed: html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .cr-card .cr-card__body { height: 122px !important; min-height: 122px !important; max-height: 122px !importan**
- **Visual change if removed:** None.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 319-339). Manual anchor: from `/* Center age, collection, and soft markers as a compact row at the top of every card i...` to `html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#Main...`.
Delete:
```css
/* Center age, collection, and soft markers as a compact row at the top of every card image. */
html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .card-marker-cluster,
html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .drift-marker-cluster{position:absolute!important;top:8px!important;right:auto!important;bottom:auto!important;left:50%!important;transform:translateX(-50%)!important;display:flex!important;align-items:center!important;justify-content:center!important;gap:6px!important;width:max-content!important;max-width:calc(100% - 40px)!important;z-index:12!important;pointer-events:none!important;white-space:nowrap!important}
html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .card-marker-cluster>.age-tag,
html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .card-marker-cluster>.cr-card__tag,
html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .card-marker-cluster>.product-card__tag,
html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .card-marker-cluster>.soft-dot,
html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .drift-marker-cluster>[data-drift-age],
html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .drift-marker-cluster>[data-drift-category]{position:relative!important;top:auto!important;right:auto!important;bottom:auto!important;left:auto!important;margin:0!important;transform:none!important;flex:0 0 auto!important;pointer-events:auto!important}
html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .card-marker-cluster>.cr-card__tag::before,
html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .card-marker-cluster>.soft-dot>.tag-edge-line,
html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .drift-marker-cluster>[data-drift-category]::before{content:none!important;display:none!important}
@media(max-width:767px){html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .card-marker-cluster,html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .drift-marker-cluster{top:6px!important;gap:4px!important}}

html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .drift-marker-cluster>[data-drift-category]{display:block!important;width:8.4px!important;min-width:8.4px!important;max-width:8.4px!important;height:8.4px!important;padding:0!important;overflow:visible!important;border:0!important;border-radius:50%!important;background:color-mix(in srgb,var(--label-color) 50%,white)!important;color:transparent!important;font-size:0!important;line-height:0!important;box-sizing:border-box!important}


/* Keep the image clear: standard card markers sit centered above the title. */
html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .cr-card .card-marker-cluster,
html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .product-card .card-marker-cluster{position:relative!important;top:auto!important;right:auto!important;bottom:auto!important;left:auto!important;transform:none!important;display:flex!important;align-items:center!important;justify-content:center!important;gap:6px!important;width:100%!important;max-width:100%!important;height:22px!important;min-height:22px!important;max-height:22px!important;margin:0 0 1px!important;z-index:3!important;pointer-events:none!important}
html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .cr-card .cr-card__body{height:122px!important;min-height:122px!important;max-height:122px!important;overflow:hidden!important}
```

### T35 [REVIEW] Layout for the removed 'Fidget pair' banners (`#tlv-fidget-pair`, `#tlv-squishy-banner`)
- **File:** `assets/card-look.css` | baseline lines 71-95 | kind: orphan selectors (feature removed)
- **Why it is dead:** The only code that creates these elements (snippets/heart-js.liquid, script tlv-insert-squishy-banner) starts with `return true;`, so they are never built. tlv-owner-overrides.css also hides them with display:none !important (owner removed these banners).
- **Proof:** grep: the ids appear elsewhere only inside CSS/<style> blocks. Chrome CSSOM: removes 2 @media rules and their 8 nested rules.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (max-width: 767px) [group] /   - removed: @media (min-width: 768px) [group] /   - removed: @media (min-width: 768px) > html body #tlv-fidget-pair { gap: 20px; width: calc(100% - 40px); align-items: flex-start; display: flex !important; margin: 28px 20px 32px !important; } /   - removed: @media (min-width: 768px) > html body #tlv-fidget-pair > #tlv-mechanical-fidgets-banner#tlv-mechanical-fidgets-banner, html body #tlv-fidget-pair > #tlv-squishy-banner { min-width: 0px; border-radius: 30px; overflow: hidden; box-shadow: var(--tlv-shared-card-shadow); flex: 1 1 0px !important; width: /   - removed: @media (min-width: 768px) > html body #tlv-fidget-pair #tlv-mechanical-fidgets-banner img.tlv-mechanical-fidgets-desktop, html body #tlv-fidget-pair #tlv-squishy-banner img { display: block !important; width: 100% !important; height: 100% !important; max-width: 100% !important; object-fit: cover !im /   - removed: @media (min-width: 768px) > html body #tlv-squishy-banner .tlv-sq-link { display: block; width: 100%; height: 100%; } /   - removed: @media (max-width: 767px) > html body #tlv-fidget-pair { display: block; width: calc(100% - 20px); margin: 20px auto 24px; } /   - removed: @media (max-width: 767px) > html body #tlv-squishy-banner { display: block; margin-top: 14px; border-radius: 22px; overflow: hidden; box-shadow: var(--tlv-shared-card-shadow); } /   - removed: @media (max-width: 767px) > html body #tlv-squishy-banner img { display: block; width: 100%; height: auto; } /   - removed: @media (max-width: 767px) > html body #tlv-fidget-pair > #tlv-mechanical-fidgets-banner { width: 100% !important; margin: 0px !important; }**
- **Visual change if removed:** None.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 71-95). Manual anchor: from `/* Fidget pair: Mechanical + Squishy half-width 8:3 cards side by side (tablet + deskto...` to `}`.
Delete:
```css
/* Fidget pair: Mechanical + Squishy half-width 8:3 cards side by side (tablet + desktop) */

@media(min-width:768px){

html body #tlv-fidget-pair{display:flex!important;gap:20px;width:calc(100% - 40px);margin:28px 20px 32px!important;align-items:flex-start}

html body #tlv-fidget-pair>#tlv-mechanical-fidgets-banner#tlv-mechanical-fidgets-banner,html body #tlv-fidget-pair>#tlv-squishy-banner{flex:1 1 0!important;width:auto!important;min-width:0;max-width:none!important;height:auto!important;aspect-ratio:8/3!important;margin:0!important;border-radius:30px;overflow:hidden;box-shadow:var(--tlv-shared-card-shadow)}

html body #tlv-fidget-pair #tlv-mechanical-fidgets-banner img.tlv-mechanical-fidgets-desktop,html body #tlv-fidget-pair #tlv-squishy-banner img{display:block!important;width:100%!important;height:100%!important;max-width:100%!important;object-fit:cover!important}

html body #tlv-squishy-banner .tlv-sq-link{display:block;width:100%;height:100%}

}

@media(max-width:767px){

html body #tlv-fidget-pair{display:block;width:calc(100% - 20px);margin:20px auto 24px}

html body #tlv-squishy-banner{display:block;margin-top:14px;border-radius:22px;overflow:hidden;box-shadow:var(--tlv-shared-card-shadow)}

html body #tlv-squishy-banner img{display:block;width:100%;height:auto}

html body #tlv-fidget-pair>#tlv-mechanical-fidgets-banner{width:100%!important;margin:0!important}

}
```

### T36 [TODO] Product page: early CTA, mobile description and 1:1 main-image rules restated later
- **File:** `assets/toylvia.css` | baseline lines 1303-1312, 1411-1429, 1923-1927 | kind: always-overridden rules (same file, tool-proven)
- **Why it is dead:** The first .product-main__cta block (1303-1312) and the 'buttons less harsh' tweak (1923-1927) are fully redeclared by .product-main__cta at 2399. The whole '/* MOBILE FIX */' @media (max-width: 768px) block (1396-1408) is redeclared by the top-level description rules at 1792, 1902 and 1911. The first '1:1' .product-main__main-image block and its img rule (1411-1429, including the '/* image inside */' comment) are redeclared by the later 'FORCE PRODUCT IMAGE 1:1' block at 1821 and 1844. Each later rule has the same selector in the same or a top-level context, so the removed rules can never win. cssom.js shows only these 6 rules removed, plus the @media group that is left empty.
- **Proof:** shadow.js (headless Chrome): every removed rule has a LATER kept rule in the same file with a selector list containing its selectors, the same or top-level @media context, and every longhand at equal-or-higher priority -> PROVEN. Winners: 1303-1312 -> 2399 (1924 is also removed here; 2399 alone covers it); 1398-1402 -> 1792, 1902; 1404-1407 -> 1911; 1411-1422 -> 1821; 1425-1429 -> 1844; 1924-1927 -> 2399. Re-run independently by a skeptic agent (same result, no added rules).
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .product-main__cta { width: fit-content; padding: 1rem 2.2rem; border-radius: 999px; background: rgb(17, 17, 17); color: rgb(255, 255, 255); font-weight: 800; border: none; cursor: pointer; } /   - removed: .product-main__main-image { width: 100%; aspect-ratio: 1 / 1; background: rgb(246, 246, 246); border-radius: 1rem; display: flex; align-items: center; justify-content: center; overflow: hidden; } /   - removed: .product-main__main-image img { width: 100%; height: 100%; object-fit: contain; } /   - removed: .product-main__cta { font-weight: 700; letter-spacing: 0.03em; }**
- **Visual change if removed:** None.
- **Parts:** 3 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 1303-1312). Manual anchor: from `.product-main__cta {` to `}`.
Delete:
```css
.product-main__cta {
  width: fit-content;
  padding: 1rem 2.2rem;
  border-radius: 999px;
  background: #111;
  color: #fff;
  font-weight: 800;
  border: none;
  cursor: pointer;
}
```

**Part 2** (baseline lines 1411-1429). Manual anchor: from `.product-main__main-image {` to `}`.
Delete:
```css
.product-main__main-image {
  width: 100%;
  aspect-ratio: 1 / 1; /* key line */
  background: #f6f6f6;
  border-radius: 1rem;

  display: flex;
  align-items: center;
  justify-content: center;

  overflow: hidden;
}

/* image inside */
.product-main__main-image img {
  width: 100%;
  height: 100%;
  object-fit: contain; /* keeps full product visible */
}
```

**Part 3** (baseline lines 1923-1927). Manual anchor: from `/* buttons less harsh */` to `}`.
Delete:
```css
/* buttons less harsh */
.product-main__cta {
  font-weight: 700;
  letter-spacing: 0.03em;
}
```

### T37 [TODO] Product page: early CTA, mobile description and 1:1 main-image rules restated later (part inside T27)
- **File:** `assets/toylvia.css` | baseline lines 1396-1408 | kind: always-overridden rules (same file, tool-proven)
- **Why it is dead:** The first .product-main__cta block (1303-1312) and the 'buttons less harsh' tweak (1923-1927) are fully redeclared by .product-main__cta at 2399. The whole '/* MOBILE FIX */' @media (max-width: 768px) block (1396-1408) is redeclared by the top-level description rules at 1792, 1902 and 1911. The first '1:1' .product-main__main-image block and its img rule (1411-1429, including the '/* image inside */' comment) are redeclared by the later 'FORCE PRODUCT IMAGE 1:1' block at 1821 and 1844. Each later rule has the same selector in the same or a top-level context, so the removed rules can never win. cssom.js shows only these 6 rules removed, plus the @media group that is left empty.
- **Proof:** shadow.js (headless Chrome): every removed rule has a LATER kept rule in the same file with a selector list containing its selectors, the same or top-level @media context, and every longhand at equal-or-higher priority -> PROVEN. Winners: 1303-1312 -> 2399 (1924 is also removed here; 2399 alone covers it); 1398-1402 -> 1792, 1902; 1404-1407 -> 1911; 1411-1422 -> 1821; 1425-1429 -> 1844; 1924-1927 -> 2399. Re-run independently by a skeptic agent (same result, no added rules).
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (max-width: 768px) [group] /   - removed: @media (max-width: 768px) > .product-main__description-full { font-size: 16px; line-height: 1.7; margin-top: 3rem; } /   - removed: @media (max-width: 768px) > .product-main__description-full h2, .product-main__description-full h3 { font-size: 22px; }**
- **Visual change if removed:** None.
- **Superseded by:** T27 (REVIEW). If Ziko approves T27, skip this item; it is included there.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 1396-1408). Manual anchor: from `/* MOBILE FIX */` to `}`.
Delete:
```css
/* MOBILE FIX */
@media (max-width: 768px) {
  .product-main__description-full {
    font-size: 16px;
    line-height: 1.7;
    margin-top: 3rem;
  }

  .product-main__description-full h2,
  .product-main__description-full h3 {
    font-size: 22px;
  }
}
```

### T38 [TODO] Original trust-badge rules (homepage + product page) restated later
- **File:** `assets/toylvia.css` | baseline lines 237-250, 260-271, 991-1008 | kind: always-overridden rules (same file, tool-proven)
- **Why it is dead:** The original homepage trust-badge styles are all redeclared later. .trust-badges, including its two one-line @media variants (237-241), is redeclared with !important at 5084. .trust-badges__inner (242-250) is redeclared with !important at 2825 and 2855. .trust-badge__icon, the two hover rules and .trust-badge span (260-271) are redeclared with !important at 3183, 2918, 2922 and 3193. The original product-page trust-badge rules (991-1008) are redeclared by the 'NEUMORPHIC TRUST BADGES - PRODUCT PAGE' block at 2354, 2364 and 2390. The live .trust-badge rule (251-259), the live @media at 1010, and the section comments at 236 and 990 are kept. cssom.js shows only these 11 rules removed, plus the two one-line @media groups.
- **Proof:** shadow.js (headless Chrome): every removed rule has a LATER kept rule in the same file with a selector list containing its selectors, the same or top-level @media context, and every longhand at equal-or-higher priority -> PROVEN. Winners: 237-241 -> 5084; 242-250 -> 2825, 2855; 260-264 -> 3183; 265-267 -> 2918; 268-270 -> 2922; 271 -> 3193; 991-998 -> 2354; 1000-1003 -> 2364; 1005-1008 -> 2390. Re-run independently by a skeptic agent (same result, no added rules).
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (min-width: 768px) [group] /   - removed: @media (min-width: 1024px) [group] /   - removed: .trust-badges { padding: 2.5rem 3rem; } /   - removed: @media (min-width: 768px) > .trust-badges { padding: 2.5rem 6rem; } /   - removed: @media (min-width: 1024px) > .trust-badges { padding: 2.5rem 8rem; } /   - removed: .trust-badges__inner { max-width: 1200px; margin: 0px auto; display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 2rem; } /   - removed: .trust-badge__icon { width: 28px; height: 28px; color: hsl(var(--secondary)); } /   - removed: .trust-badge:hover .trust-badge__icon { color: hsl(var(--primary)); } /   - removed: .trust-badge:hover span { color: hsl(var(--foreground)); } /   - removed: .trust-badge span { text-transform: uppercase; } /   - removed: .product-trust-badges { display: flex; flex-wrap: wrap; gap: 0.75rem 1.25rem; margin-top: 1.25rem; padding-top: 1.25rem; border-top: 1px solid hsl(var(--border)); } /   - removed: .product-trust-badges .trust-badge { font-size: 12px; gap: 0.5rem; } /   - removed: .product-trust-badges .trust-badge__icon { width: 22px; height: 22px; }**
- **Visual change if removed:** None.
- **Parts:** 3 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 237-250). Manual anchor: from `.trust-badges {` to `}`.
Delete:
```css
.trust-badges {
  padding: 2.5rem 3rem;
}
@media (min-width: 768px) { .trust-badges { padding: 2.5rem 6rem; } }
@media (min-width: 1024px) { .trust-badges { padding: 2.5rem 8rem; } }
.trust-badges__inner {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  gap: 2rem;
}
```

**Part 2** (baseline lines 260-271). Manual anchor: from `.trust-badge__icon {` to `.trust-badge span { text-transform: uppercase; }`.
Delete:
```css
.trust-badge__icon {
  width: 28px;
  height: 28px;
  color: hsl(var(--secondary));
}
.trust-badge:hover .trust-badge__icon {
  color: hsl(var(--primary));
}
.trust-badge:hover span {
  color: hsl(var(--foreground));
}
.trust-badge span { text-transform: uppercase; }
```

**Part 3** (baseline lines 991-1008). Manual anchor: from `.product-trust-badges {` to `}`.
Delete:
```css
.product-trust-badges {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem 1.25rem;
  margin-top: 1.25rem;
  padding-top: 1.25rem;
  border-top: 1px solid hsl(var(--border));
}

.product-trust-badges .trust-badge {
  font-size: 12px;
  gap: 0.5rem;
}

.product-trust-badges .trust-badge__icon {
  width: 22px;
  height: 22px;
}
```

### T39 [TODO] Category-arc / All-Products-button rules overridden by later copies (part inside T22)
- **File:** `assets/toylvia.css` | baseline lines 287-289, 338-342, 426-429 | kind: always-overridden rules (same file, tool-proven)
- **Why it is dead:** These are category-arc rules that later rules with the same selector fully redeclare. 287-289: the mobile .category-arc .max-store min-width is redeclared by 1145 in the same @media. 338-342: the sphere icon hover is redeclared at 4105. 426-429: the 'WHITE / TRANSPARENT SPHERE OVERRIDE' background is redeclared by the neumorphic .category-sphere__ball at 431; that comment describes only this rule. 463-466 and 468: the first .all-products-btn:hover and the one-line .all-products-btn are redeclared by 469, 2840, 2122, 2135 and 3952; comment 467 is kept because it also heads the live 469. 1166-1173: the mobile ball and svg sizes are redeclared with !important at 1945 and 1949 in the same @media. 2091 and 2095: these one-line rules inside the mobile @media are redeclared by the top-level rules at 4105 and 2840 (!important). cssom.js shows exactly these 9 rules removed.
- **Proof:** shadow.js (headless Chrome): every removed rule has a LATER kept rule in the same file with a selector list containing its selectors, the same or top-level @media context, and every longhand at equal-or-higher priority -> PROVEN. Winners: 287-289 -> 1145; 338-342 -> 4105; 427-429 -> 431; 463-466 -> 469, 2840; 468 -> 2122, 2135, 3952; 1166-1169 -> 1945; 1170-1173 -> 1949; 2091 -> 4105; 2095 -> 2840. Re-run independently by a skeptic agent (same result, no added rules).
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (max-width: 639px) > .category-arc .max-store { min-width: 680px; } /   - removed: .category-sphere:hover .category-sphere__icon { opacity: 0; transform: scale(0.5); filter: blur(6px); } /   - removed: .category-sphere__ball { background: radial-gradient(circle at 50% 120%, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.3) 25%, rgba(255, 255, 255, 0.55) 60%, rgba(240, 240, 248, 0.75) 85%, rgba(220, 222, 235, 0.85) 100%); }**
- **Visual change if removed:** None.
- **Superseded by:** T22 (REVIEW). If Ziko approves T22, skip this item; it is included there.
- **Parts:** 3 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 287-289). Manual anchor: from `.category-arc .max-store {` to `}`.
Delete:
```css
  .category-arc .max-store {
    min-width: 680px;
  }
```

**Part 2** (baseline lines 338-342). Manual anchor: from `.category-sphere:hover .category-sphere__icon {` to `}`.
Delete:
```css
.category-sphere:hover .category-sphere__icon {
  opacity: 0;
  transform: scale(0.5);
  filter: blur(6px);
}
```

**Part 3** (baseline lines 426-429). Manual anchor: from `/* === WHITE / TRANSPARENT SPHERE OVERRIDE === */` to `}`.
Delete:
```css
/* === WHITE / TRANSPARENT SPHERE OVERRIDE === */
.category-sphere__ball {
  background: radial-gradient(circle at 50% 120%, rgba(255,255,255,0.10) 0%, rgba(255,255,255,0.30) 25%, rgba(255,255,255,0.55) 60%, rgba(240,240,248,0.75) 85%, rgba(220,222,235,0.85) 100%);
}
```

### T40 [TODO] Category-arc / All-Products-button rules overridden by later copies
- **File:** `assets/toylvia.css` | baseline lines 463-466, 468-468, 1166-1173, 2091-2091, 2095-2095 | kind: always-overridden rules (same file, tool-proven)
- **Why it is dead:** These are category-arc rules that later rules with the same selector fully redeclare. 287-289: the mobile .category-arc .max-store min-width is redeclared by 1145 in the same @media. 338-342: the sphere icon hover is redeclared at 4105. 426-429: the 'WHITE / TRANSPARENT SPHERE OVERRIDE' background is redeclared by the neumorphic .category-sphere__ball at 431; that comment describes only this rule. 463-466 and 468: the first .all-products-btn:hover and the one-line .all-products-btn are redeclared by 469, 2840, 2122, 2135 and 3952; comment 467 is kept because it also heads the live 469. 1166-1173: the mobile ball and svg sizes are redeclared with !important at 1945 and 1949 in the same @media. 2091 and 2095: these one-line rules inside the mobile @media are redeclared by the top-level rules at 4105 and 2840 (!important). cssom.js shows exactly these 9 rules removed.
- **Proof:** shadow.js (headless Chrome): every removed rule has a LATER kept rule in the same file with a selector list containing its selectors, the same or top-level @media context, and every longhand at equal-or-higher priority -> PROVEN. Winners: 287-289 -> 1145; 338-342 -> 4105; 427-429 -> 431; 463-466 -> 469, 2840; 468 -> 2122, 2135, 3952; 1166-1169 -> 1945; 1170-1173 -> 1949; 2091 -> 4105; 2095 -> 2840. Re-run independently by a skeptic agent (same result, no added rules).
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .all-products-btn:hover { transform: scale(1.15); box-shadow: rgba(255, 255, 255, 0.35) 0px 0px 0px 1px inset, rgba(255, 255, 255, 0.2) 0px 2px 6px inset, rgb(33, 213, 237) 0px 0px 45px, rgba(33, 213, 237, 0.45) 0px 0px 120px, rgba(0, 0, 0, 0.35) 0px 16px 50px; } /   - removed: .all-products-btn { padding: 0.924rem 2.464rem; font-size: 16.016px; background: rgb(249, 250, 251); border: 2.5px solid transparent; color: rgb(255, 42, 148); box-shadow: rgba(255, 255, 255, 0.9) -10px -8px 20px, rgba(148, 150, 176, 0.45) 10px 8px 20px; } /   - removed: @media (max-width: 639px) > .category-sphere__ball { width: 70px; height: 70px; } /   - removed: @media (max-width: 639px) > .category-sphere__ball svg { width: 24px; height: 24px; } /   - removed: @media (max-width: 639px) > .category-sphere:hover .category-sphere__icon { opacity: 1; transform: none; filter: none; } /   - removed: @media (max-width: 639px) > .all-products-btn:hover { transform: none; box-shadow: rgba(255, 255, 255, 0.9) -10px -8px 20px, rgba(148, 150, 176, 0.45) 10px 8px 20px; }**
- **Visual change if removed:** None.
- **Parts:** 5 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 463-466). Manual anchor: from `.all-products-btn:hover {` to `}`.
Delete:
```css
.all-products-btn:hover {
  transform: scale(1.15);
  box-shadow: inset 0 0 0 1px rgba(255,255,255,0.35), inset 0 2px 6px rgba(255,255,255,0.2), 0 0 45px hsla(187,85%,53%,1.0), 0 0 120px hsla(187,85%,53%,0.45), 0 16px 50px rgba(0,0,0,0.35);
}
```

**Part 2** (baseline lines 468-468). Manual anchor: from `.all-products-btn { padding: 0.924rem 2.464rem; font-size: 16.016px; background: rgb(24...` to `.all-products-btn { padding: 0.924rem 2.464rem; font-size: 16.016px; background: rgb(24...`.
Delete:
```css
.all-products-btn { padding: 0.924rem 2.464rem; font-size: 16.016px; background: rgb(249,250,251); border: 2.5px solid transparent; color: rgb(255,42,148); box-shadow: -10px -8px 20px rgba(255,255,255,0.9), 10px 8px 20px rgba(148,150,176,0.45); }
```

**Part 3** (baseline lines 1166-1173). Manual anchor: from `.category-sphere__ball {` to `}`.
Delete:
```css
  .category-sphere__ball {
    width: 70px;
    height: 70px;
  }
  .category-sphere__ball svg {
    width: 24px;
    height: 24px;
  }
```

**Part 4** (baseline lines 2091-2091). Manual anchor: from `.category-sphere:hover .category-sphere__icon { opacity: 1; transform: none; filter: no...` to `.category-sphere:hover .category-sphere__icon { opacity: 1; transform: none; filter: no...`.
Delete:
```css
                        .category-sphere:hover .category-sphere__icon { opacity: 1; transform: none; filter: none; }
```

**Part 5** (baseline lines 2095-2095). Manual anchor: from `.all-products-btn:hover { transform: none; box-shadow: -10px -8px 20px rgba(255,255,255...` to `.all-products-btn:hover { transform: none; box-shadow: -10px -8px 20px rgba(255,255,255...`.
Delete:
```css
                                .all-products-btn:hover { transform: none; box-shadow: -10px -8px 20px rgba(255,255,255,0.9), 10px 8px 20px rgba(148,150,176,0.45); }
```

### T41 [TODO] Original header nav rules (logo, nav, link underline, dropdown) restated later
- **File:** `assets/toylvia.css` | baseline lines 145-145, 154-154, 164-178, 198-200, 1929-1933 | kind: always-overridden rules (same file, tool-proven)
- **Why it is dead:** These are original header rules that later !important header overrides redeclare. .site-header__logo (145) is redeclared at 3098. The one-line @media (min-width: 1024px) .site-header__nav (154) is redeclared at 3106. The nav-link hover color, the ::after underline and hover::after (164-178) are redeclared at 3906, 3921 and 3935. .nav-dropdown position (198-200) is redeclared by the 'Dropdown hover-bridge fix' at 3529. The 'nav less robotic' tweak (1929-1933, comment included) is redeclared at 3888. The live .site-header__nav-link base rule (155-163) and the '/* Dropdown */' comment are kept. cssom.js shows only these 7 rules removed, plus the one-line @media group.
- **Proof:** shadow.js (headless Chrome): every removed rule has a LATER kept rule in the same file with a selector list containing its selectors, the same or top-level @media context, and every longhand at equal-or-higher priority -> PROVEN. Winners: 145 -> 3098; 154 -> 3106; 164 -> 3906; 165-177 -> 3921; 178 -> 3935; 198-200 -> 3529; 1930-1933 -> 3888. Re-run independently by a skeptic agent (same result, no added rules).
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (min-width: 1024px) [group] /   - removed: .site-header__logo { flex-shrink: 0; } /   - removed: @media (min-width: 1024px) > .site-header__nav { display: flex; } /   - removed: .site-header__nav-link:hover { color: hsl(var(--foreground)); } /   - removed: .site-header__nav-link::after { content: ""; position: absolute; bottom: 0px; left: 0px; width: 100%; height: 2px; background: hsl(var(--primary)); border-radius: 1px 1px 0px 0px; transform: scaleX(0); transform-origin: left center; transition: transform 0.5s cubic-bezier(0.25, 0.1, 0.25, 1); } /   - removed: .site-header__nav-link:hover::after { transform: scaleX(1); } /   - removed: .nav-dropdown { position: relative; } /   - removed: .site-header__nav-link { letter-spacing: 0.05em; font-weight: 500; }**
- **Visual change if removed:** None.
- **Parts:** 5 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 145-145). Manual anchor: from `.site-header__logo { flex-shrink: 0; }` to `.site-header__logo { flex-shrink: 0; }`.
Delete:
```css
.site-header__logo { flex-shrink: 0; }
```

**Part 2** (baseline lines 154-154). Manual anchor: from `@media (min-width: 1024px) { .site-header__nav { display: flex; } }` to `@media (min-width: 1024px) { .site-header__nav { display: flex; } }`.
Delete:
```css
@media (min-width: 1024px) { .site-header__nav { display: flex; } }
```

**Part 3** (baseline lines 164-178). Manual anchor: from `.site-header__nav-link:hover { color: hsl(var(--foreground)); }` to `.site-header__nav-link:hover::after { transform: scaleX(1); }`.
Delete:
```css
.site-header__nav-link:hover { color: hsl(var(--foreground)); }
.site-header__nav-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background: hsl(var(--primary));
  border-radius: 1px 1px 0 0;
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.5s cubic-bezier(0.25, 0.1, 0.25, 1);
}
.site-header__nav-link:hover::after { transform: scaleX(1); }
```

**Part 4** (baseline lines 198-200). Manual anchor: from `.nav-dropdown {` to `}`.
Delete:
```css
.nav-dropdown {
  position: relative;
}
```

**Part 5** (baseline lines 1929-1933). Manual anchor: from `/* nav less robotic */` to `}`.
Delete:
```css
/* nav less robotic */
.site-header__nav-link {
  letter-spacing: 0.05em;
  font-weight: 500;
}
```

### T42 [TODO] Original newsletter socials / social-link / dot-texture rules restated later
- **File:** `assets/toylvia.css` | baseline lines 692-710, 2057-2060 | kind: always-overridden rules (same file, tool-proven)
- **Why it is dead:** The original .newsletter__socials (692-698) and .newsletter__social-link (699-710) are fully redeclared by the later 'Social Icons' and 'SOCIAL ICONS' rules at 3562, 3650 and 3651. The .newsletter dot-texture background (2057-2060) is redeclared by the !important footer override at 3647. The live .newsletter__social-link:hover (711) and the other dot-texture rules (2049-2056, 2061-2064) are kept. cssom.js shows exactly these 3 rules removed.
- **Proof:** shadow.js (headless Chrome): every removed rule has a LATER kept rule in the same file with a selector list containing its selectors, the same or top-level @media context, and every longhand at equal-or-higher priority -> PROVEN. Winners: 692-698 -> 3650; 699-710 -> 3562, 3651; 2057-2060 -> 3647. Re-run independently by a skeptic agent (same result, no added rules).
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .newsletter__socials { display: flex; align-items: center; justify-content: center; gap: 1rem; margin-bottom: 2rem; } /   - removed: .newsletter__social-link { width: 40px; height: 40px; border-radius: 50%; border: 2px solid hsl(var(--border)); background: hsl(var(--background)); display: flex; align-items: center; justify-content: center; color: hsl(var(--muted-foreground)); transition: color 0.3s, border-color 0.3s; } /   - removed: .newsletter { background-image: radial-gradient(circle, rgba(175, 155, 210, 0.13) 1.1px, transparent 1.1px); background-size: 26px 26px; }**
- **Visual change if removed:** None.
- **Parts:** 2 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 692-710). Manual anchor: from `.newsletter__socials {` to `}`.
Delete:
```css
.newsletter__socials {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 2rem;
}
.newsletter__social-link {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: 2px solid hsl(var(--border));
  background: hsl(var(--background));
  display: flex;
  align-items: center;
  justify-content: center;
  color: hsl(var(--muted-foreground));
  transition: color 0.3s, border-color 0.3s;
}
```

**Part 2** (baseline lines 2057-2060). Manual anchor: from `.newsletter {` to `}`.
Delete:
```css
                .newsletter {
                  background-image: radial-gradient(circle, rgba(175,155,210,0.13) 1.1px, transparent 1.1px);
                    background-size: 26px 26px;
                    }
```

### T43 [TODO] Earlier trust-badge container, hover and animation rules restated by later override blocks (part inside T29)
- **File:** `assets/toylvia.css` | baseline lines 2384-2388 | kind: always-overridden rules (same file, tool-proven)
- **Why it is dead:** Trust-badge styling was pasted several times. Five earlier .trust-badges__inner rules (the max-width 920px one, the whole min-width 921px @media block with its 'Desktop (Above 920px)' comment, the top-level '2. ALIGN & FIX TRUST BADGE CONTAINER' rule, and the max-width 768px one) are fully restated with !important by .trust-badges__inner at 2855-2864, 3037-3045, 4886-4891 and 5090-5098. The '1. REMOVE ANIMATIONS FROM TRUST BADGES' rule (2816-2822) is restated by the larger list at 2888-2902. On the product page, .product-trust-badges .trust-badge:hover at 2384-2388 and 2961-2967 are restated by the 'Definitively kill all hover shadows' rule at 2980-2991, and the white-background rule at 2968-2978 is restated by 2992-3012 and 3160-3180. The included comments (2804, 2815, 2824) describe only removed rules. The section comment at 2779-2782 and the 920px .trust-badge rule at 2796-2801 stay b
- **Proof:** shadow.js (headless Chrome): every removed rule has a LATER kept rule in the same file with a selector list containing its selectors, the same or top-level @media context, and every longhand at equal-or-higher priority -> PROVEN. Winners: toylvia.css 2855-2864, 2888-2902, 2980-2991, 2992-3012, 3037-3045, 3160-3180, 4886-4891, 5090-5098. Re-run independently by a skeptic agent (same result, no added rules).
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .product-trust-badges .trust-badge:hover { box-shadow: rgba(0, 0, 0, 0.15) 6px 6px 15px, rgb(255, 255, 255) -6px -6px 15px; }**
- **Visual change if removed:** None.
- **Superseded by:** T29 (REVIEW). If Ziko approves T29, skip this item; it is included there.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 2384-2388). Manual anchor: from `.product-trust-badges .trust-badge:hover {` to `}`.
Delete:
```css
.product-trust-badges .trust-badge:hover {
  box-shadow:
    6px 6px 15px rgba(0, 0, 0, 0.15),
    -6px -6px 15px rgba(255, 255, 255, 1);
}
```

### T44 [TODO] Earlier trust-badge container, hover and animation rules restated by later override blocks
- **File:** `assets/toylvia.css` | baseline lines 2784-2794, 2804-2837, 2876-2879, 2961-2978 | kind: always-overridden rules (same file, tool-proven)
- **Why it is dead:** Trust-badge styling was pasted several times. Five earlier .trust-badges__inner rules (the max-width 920px one, the whole min-width 921px @media block with its 'Desktop (Above 920px)' comment, the top-level '2. ALIGN & FIX TRUST BADGE CONTAINER' rule, and the max-width 768px one) are fully restated with !important by .trust-badges__inner at 2855-2864, 3037-3045, 4886-4891 and 5090-5098. The '1. REMOVE ANIMATIONS FROM TRUST BADGES' rule (2816-2822) is restated by the larger list at 2888-2902. On the product page, .product-trust-badges .trust-badge:hover at 2384-2388 and 2961-2967 are restated by the 'Definitively kill all hover shadows' rule at 2980-2991, and the white-background rule at 2968-2978 is restated by 2992-3012 and 3160-3180. The included comments (2804, 2815, 2824) describe only removed rules. The section comment at 2779-2782 and the 920px .trust-badge rule at 2796-2801 stay b
- **Proof:** shadow.js (headless Chrome): every removed rule has a LATER kept rule in the same file with a selector list containing its selectors, the same or top-level @media context, and every longhand at equal-or-higher priority -> PROVEN. Winners: toylvia.css 2855-2864, 2888-2902, 2980-2991, 2992-3012, 3037-3045, 3160-3180, 4886-4891, 5090-5098. Re-run independently by a skeptic agent (same result, no added rules).
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (max-width: 920px) > .trust-badges__inner { display: flex !important; flex-wrap: wrap !important; gap: 0.75rem !important; width: 100% !important; padding: 1rem 0.5rem !important; justify-content: center !important; align-items: center !important; overflow: visible !important; margin: 0px !im /   - removed: @media (min-width: 921px) [group] /   - removed: @media (min-width: 921px) > .trust-badges__inner { display: flex !important; flex-wrap: nowrap !important; justify-content: center !important; gap: 3rem !important; width: 100% !important; margin: 0px auto !important; } /   - removed: .trust-badge, .trust-badge *, .trust-badge__icon, .trust-badge span { animation: auto ease 0s 1 normal none running none !important; transition: none !important; } /   - removed: .trust-badges__inner { display: flex !important; flex-wrap: wrap !important; justify-content: center !important; align-items: center !important; width: 100% !important; max-width: 1212px !important; margin-left: auto !important; margin-right: auto !important; gap: 20px !important; overflow: hidden ! /   - removed: @media (max-width: 768px) > .trust-badges__inner { justify-content: center !important; gap: 30px 10% !important; } /   - removed: .product-trust-badges .trust-badge:hover { box-shadow: rgba(163, 177, 198, 0.6) 9px 9px 16px, rgb(255, 255, 255) -9px -9px 16px !important; transform: none !important; } /   - removed: .product-trust-badges .trust-badge, .trust-badge, .trust-badge:hover { background: rgb(255, 255, 255) !important; box-shadow: none !important; filter: none !important; border: none !important; transform: none !important; transition: none !important; }**
- **Visual change if removed:** None.
- **Parts:** 4 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 2784-2794). Manual anchor: from `.trust-badges__inner {` to `}`.
Delete:
```css
  .trust-badges__inner {
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 0.75rem !important;
    width: 100% !important;
    padding: 1rem 0.5rem !important;
    justify-content: center !important;
    align-items: center !important;
    overflow: visible !important;
    margin: 0 !important;
  }
```

**Part 2** (baseline lines 2804-2837). Manual anchor: from `/* Desktop (Above 920px) */` to `}`.
Delete:
```css
/* Desktop (Above 920px) */
@media (min-width: 921px) {
  .trust-badges__inner {
    display: flex !important;
    flex-wrap: nowrap !important;
    justify-content: center !important;
    gap: 3rem !important;
    width: 100% !important;
    margin: 0 auto !important;
  }
}
/* 1. REMOVE ANIMATIONS FROM TRUST BADGES */
.trust-badge, 
.trust-badge *, 
.trust-badge__icon, 
.trust-badge span {
  animation: none !important;
  transition: none !important;
}

/* 2. ALIGN & FIX TRUST BADGE CONTAINER */
.trust-badges__inner {
  display: flex !important;
  flex-wrap: wrap !important;
  justify-content: center !important;
  align-items: center !important;
  width: 100% !important;
  max-width: 1212px !important; /* Matches your category grid width */
  margin-left: auto !important;
  margin-right: auto !important;
  gap: 20px !important;
  overflow: hidden !important;
  height: auto !important;
}
```

**Part 3** (baseline lines 2876-2879). Manual anchor: from `.trust-badges__inner {` to `}`.
Delete:
```css
  .trust-badges__inner {
    justify-content: center !important;
    gap: 30px 10% !important; /* Vertical gap 30px, Horizontal gap 10% */
  }
```

**Part 4** (baseline lines 2961-2978). Manual anchor: from `.product-trust-badges .trust-badge:hover {` to `}`.
Delete:
```css
.product-trust-badges .trust-badge:hover {
  /* Match the non-hover state to avoid sinking */
  box-shadow: 
    9px 9px 16px rgba(163, 177, 198, 0.6), 
    -9px -9px 16px rgba(255, 255, 255, 1) !important;
  transform: none !important;
}
.product-trust-badges .trust-badge,
.trust-badge,
.trust-badge:hover {
  background: #ffffff !important;
  background-color: #ffffff !important;
  box-shadow: none !important;
  filter: none !important;
  border: none !important;
  transform: none !important;
  transition: none !important;
}
```

### T45 [TODO] Duplicated site-header nav-link, ::before, inner and mobile header rules
- **File:** `assets/toylvia.css` | baseline lines 3116-3121, 3252-3253, 3507-3507, 3510-3510, 3521-3526 | kind: always-overridden rules (same file, tool-proven)
- **Why it is dead:** .site-header__nav-link {position;padding;border-radius;transition} was pasted twice (3116-3121 and 3521-3526), and both copies are restated by .site-header__nav-link at 3888-3904. .site-header::before at 3507 is restated by 4064-4077 and 4872. .site-header__inner {position;z-index} at 3510 is restated by 4088. In the 'MOBILE RESPONSIVE' @media (max-width:768px) block, .site-header__inner and .site-header__logo img at 3252-3253 (not !important) are restated with !important in the same media by 'MOBILE FIX V2' at 3375-3376. The live neighbours stay: 3508 ::after, 3254-3255, and .site-header__nav at 3512-3519. cssom.js shows exactly these 6 rules removed.
- **Proof:** shadow.js (headless Chrome): every removed rule has a LATER kept rule in the same file with a selector list containing its selectors, the same or top-level @media context, and every longhand at equal-or-higher priority -> PROVEN. Winners: toylvia.css 3375, 3376, 3888-3904, 4064-4077, 4088, 4872. Re-run independently by a skeptic agent (same result, no added rules).
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .site-header__nav-link { position: relative; padding: 8px 16px; border-radius: 999px; transition: 0.25s; } /   - removed: .site-header__nav-link { position: relative; padding: 8px 16px; border-radius: 999px; transition: 0.25s; } /   - removed: @media (max-width: 768px) > .site-header__inner { padding: 0px 1rem; height: 60px; } /   - removed: @media (max-width: 768px) > .site-header__logo img { height: 46px; } /   - removed: .site-header::before { top: 1px; background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.9), transparent); } /   - removed: .site-header__inner { position: relative; z-index: 1; }**
- **Visual change if removed:** None.
- **Parts:** 5 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 3116-3121). Manual anchor: from `.site-header__nav-link {` to `}`.
This text also exists elsewhere in the file, so it is located by the neighbouring lines (kept, not deleted): before = `(none)`, after = `/* Positioning the action icons (account, search, cart) on the right */`.
Delete:
```css
.site-header__nav-link {
  position: relative;
  padding: 8px 16px;
  border-radius: 999px;
  transition: all .25s ease;
}
```

**Part 2** (baseline lines 3252-3253). Manual anchor: from `.site-header__inner { padding: 0 1rem; height: 60px; }` to `.site-header__logo img { height: 46px; }`.
Delete:
```css
            .site-header__inner { padding: 0 1rem; height: 60px; }
              .site-header__logo img { height: 46px; }
```

**Part 3** (baseline lines 3507-3507). Manual anchor: from `.site-header::before { top: 1px; background: linear-gradient(90deg, transparent, rgba(2...` to `.site-header::before { top: 1px; background: linear-gradient(90deg, transparent, rgba(2...`.
Delete:
```css
.site-header::before { top: 1px;    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.9), transparent); }
```

**Part 4** (baseline lines 3510-3510). Manual anchor: from `.site-header__inner { position: relative; z-index: 1; }` to `.site-header__inner { position: relative; z-index: 1; }`.
Delete:
```css
.site-header__inner { position: relative; z-index: 1; }
```

**Part 5** (baseline lines 3521-3526). Manual anchor: from `.site-header__nav-link {` to `}`.
This text also exists elsewhere in the file, so it is located by the neighbouring lines (kept, not deleted): before = `(none)`, after = `/* Dropdown hover-bridge fix */`.
Delete:
```css
.site-header__nav-link {
  position: relative;
  padding: 8px 16px;
  border-radius: 999px;
  transition: all .25s ease;
}
```

### T46 [TODO] Overridden All-Products / See-all button rules
- **File:** `assets/toylvia.css` | baseline lines 2121-2122, 2511-2512, 2692-2695 | kind: always-overridden rules (same file, tool-proven)
- **Why it is dead:** 'GRADIENT BORDER: ALL PRODUCTS BUTTON' .all-products-btn {background} at 2122 is restated by the !important backgrounds at 2135-2143 and 3952-3969. a.all-products-btn:active {transform} at 2693-2695 is restated with !important at 2746-2748. The one-line .see-all-btn:hover at 2511 and .see-all-btn {font-size;padding} at 2512 are restated with !important by 2643-2650 and 3661-3669, and by 2625-2641. Both comments (2121, 2692) describe only the removed rule. 2507-2510 stay because they are live. CAUTION: the already-logged range 2144-2152 removes the '}}' that also closes the .all-products-btn rule opened at 2135. Cut alone, cssom.js shows 27 rules lost (e.g. '*,::before,::after' at 2516), so that logged entry looks broken. This candidate does not depend on it, because 3952-3969 also covers 2122.
- **Proof:** shadow.js (headless Chrome): every removed rule has a LATER kept rule in the same file with a selector list containing its selectors, the same or top-level @media context, and every longhand at equal-or-higher priority -> PROVEN. Winners: toylvia.css 2135-2143 (and 3952-3969), 2625-2641, 2643-2650, 3661-3669, 2746-2748. Re-run independently by a skeptic agent (same result, no added rules).
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .all-products-btn { background: linear-gradient(rgb(249, 250, 251), rgb(249, 250, 251)) padding-box padding-box, linear-gradient(135deg, rgb(255, 41, 148), rgb(33, 213, 237)) border-box border-box; } /   - removed: .see-all-btn:hover { box-shadow: rgb(209, 209, 209) 3px 3px 8px, rgb(255, 255, 255) -3px -3px 8px !important; transform: translateY(-2px) !important; color: rgb(17, 17, 17) !important; } /   - removed: .see-all-btn { font-size: 16px !important; padding: 20px 41px 16px !important; } /   - removed: a.all-products-btn:active { transform: translateY(4px); }**
- **Visual change if removed:** None.
- **Parts:** 3 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 2121-2122). Manual anchor: from `/* === GRADIENT BORDER: ALL PRODUCTS BUTTON === */` to `.all-products-btn { background: linear-gradient(rgb(249,250,251), rgb(249,250,251)) pad...`.
Delete:
```css
/* === GRADIENT BORDER: ALL PRODUCTS BUTTON === */
.all-products-btn { background: linear-gradient(rgb(249,250,251), rgb(249,250,251)) padding-box, linear-gradient(135deg, #ff2994, #21d5ed) border-box; }
```

**Part 2** (baseline lines 2511-2512). Manual anchor: from `.see-all-btn:hover { box-shadow: 3px 3px 8px #d1d1d1, -3px -3px 8px #ffffff !important;...` to `.see-all-btn { font-size: 16px !important; padding: 20px 41px 16px 41px !important; }`.
Delete:
```css
.see-all-btn:hover { box-shadow: 3px 3px 8px #d1d1d1, -3px -3px 8px #ffffff !important; transform: translateY(-2px) !important; color: #111 !important; }
.see-all-btn { font-size: 16px !important; padding: 20px 41px 16px 41px !important; }
```

**Part 3** (baseline lines 2692-2695). Manual anchor: from `/* 5. Active State: Deep "Pressed" effect when clicked */` to `}`.
Delete:
```css
/* 5. Active State: Deep "Pressed" effect when clicked */
a.all-products-btn:active {
  transform: translateY(4px);
}
```

### T47 [TODO] 'MOBILE LAYOUT FIXES' (max-width 639px) trust-badge and section-title rules restated later
- **File:** `assets/toylvia.css` | baseline lines 2101-2104 | kind: always-overridden rules (same file, tool-proven)
- **Why it is dead:** Inside @media (max-width: 639px) at 2099-2106, .trust-badges, .trust-badges__inner, .section-title and .section-title__line (2101-2104) are not !important. The later top-level !important rules in the numbered mobile-fix block restate them: .trust-badges 5084-5088, .trust-badges__inner 5090-5098, .section-title 5134-5140 and .section-title__line 5142-5144 (margin shorthand). The @media opener and closer, the 2098 comment, and the live 2100 and 2105 rules stay, so the block remains balanced. cssom.js shows exactly these 4 rules removed.
- **Proof:** shadow.js (headless Chrome): every removed rule has a LATER kept rule in the same file with a selector list containing its selectors, the same or top-level @media context, and every longhand at equal-or-higher priority -> PROVEN. Winners: toylvia.css 5084-5088, 5090-5098, 5134-5140, 5142-5144. Re-run independently by a skeptic agent (same result, no added rules).
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (max-width: 639px) > .trust-badges { padding: 1.5rem 1rem; } /   - removed: @media (max-width: 639px) > .trust-badges__inner { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; justify-items: start; } /   - removed: @media (max-width: 639px) > .section-title { text-align: center; display: inline-block; } /   - removed: @media (max-width: 639px) > .section-title__line { margin-left: auto; margin-right: auto; }**
- **Visual change if removed:** None.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 2101-2104). Manual anchor: from `.trust-badges { padding: 1.5rem 1rem; }` to `.section-title__line { margin-left: auto; margin-right: auto; }`.
Delete:
```css
                                    .trust-badges { padding: 1.5rem 1rem; }
                                      .trust-badges__inner { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; justify-items: start; }
                                        .section-title { text-align: center; display: inline-block; }
                                          .section-title__line { margin-left: auto; margin-right: auto; }
```

### T48 [TODO] Newsletter mobile padding/input and social-link colour restated later
- **File:** `assets/toylvia.css` | baseline lines 3320-3320, 3324-3324, 3572-3574 | kind: always-overridden rules (same file, tool-proven)
- **Why it is dead:** In the 'NEWSLETTER' @media (max-width:640px) block, .newsletter {padding !important} at 3320 is restated by .newsletter at 3394, and .newsletter__input {width;box-sizing !important} at 3324 is restated by '.newsletter__input, .newsletter__btn' at 3396. Both later rules are in the same media in 'MOBILE FIX V2'. The stand-alone .newsletter__social-link {color:#aab4c0 !important} at 3572-3574 is restated by the one-line .newsletter__social-link at 3651. 3321-3323 and 3325 stay because they are live. cssom.js shows exactly these 3 rules removed.
- **Proof:** shadow.js (headless Chrome): every removed rule has a LATER kept rule in the same file with a selector list containing its selectors, the same or top-level @media context, and every longhand at equal-or-higher priority -> PROVEN. Winners: toylvia.css 3394, 3396, 3651. Re-run independently by a skeptic agent (same result, no added rules).
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (max-width: 640px) > .newsletter { padding: 2.5rem 1.25rem !important; } /   - removed: @media (max-width: 640px) > .newsletter__input { width: 100% !important; box-sizing: border-box !important; } /   - removed: .newsletter__social-link { color: rgb(170, 180, 192) !important; }**
- **Visual change if removed:** None.
- **Parts:** 3 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 3320-3320). Manual anchor: from `.newsletter { padding: 2.5rem 1.25rem !important; }` to `.newsletter { padding: 2.5rem 1.25rem !important; }`.
Delete:
```css
                                                                                                                            .newsletter { padding: 2.5rem 1.25rem !important; }
```

**Part 2** (baseline lines 3324-3324). Manual anchor: from `.newsletter__input { width: 100% !important; box-sizing: border-box !important; }` to `.newsletter__input { width: 100% !important; box-sizing: border-box !important; }`.
Delete:
```css
                                                                                                                                    .newsletter__input { width: 100% !important; box-sizing: border-box !important; }
```

**Part 3** (baseline lines 3572-3574). Manual anchor: from `.newsletter__social-link {` to `}`.
Delete:
```css
.newsletter__social-link {
  color: #aab4c0 !important;
}
```

### T49 [TODO] V14 trust-badge sizing one-liners overridden by the later trust-badge block
- **File:** `assets/toylvia.css` | baseline lines 4892-4892, 4936-4937, 4945-4946, 4957-4959 | kind: always-overridden rules (same file, tool-proven)
- **Why it is dead:** In the 'TOYLVIA V14 PERMANENT STYLES' block, 8 one-line rules (.trust-badge gap at top level, plus .trust-badges__inner gap, .trust-badge__icon width/height and .trust-badge span font-size inside @media 1024/768/480) are restated later at top level with the same selectors and !important on every longhand. A top-level later rule beats an earlier media-scoped rule with the same selector, so these values never apply. The sibling rules on the same media lines (section-title, clg-*, padding, flex) are kept.
- **Proof:** shadow.js (headless Chrome): every removed rule has a LATER kept rule in the same file with a selector list containing its selectors, the same or top-level @media context, and every longhand at equal-or-higher priority -> PROVEN. Winners: toylvia.css 5090-5098 (.trust-badges__inner gap 16px 8px !important), 5100-5109 (.trust-badge gap 0.6rem !important), 5111-5114 (.trust-badge span font-size 11px !important), 5116-5121 (.trust-badge__icon width/height 36px !important), all top level. Re-run independently by a skeptic agent (same result, no added rules).
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .trust-badge { gap: 14px !important; } /   - removed: @media (max-width: 1024px) > .trust-badges__inner { gap: 36px !important; } /   - removed: @media (max-width: 1024px) > .trust-badge__icon { width: 22px !important; height: 22px !important; } /   - removed: @media (max-width: 768px) > .trust-badge__icon { width: 18px !important; height: 18px !important; } /   - removed: @media (max-width: 768px) > .trust-badge span { font-size: 12px !important; } /   - removed: @media (max-width: 480px) > .trust-badges__inner { gap: 14px !important; } /   - removed: @media (max-width: 480px) > .trust-badge__icon { width: 14px !important; height: 14px !important; } /   - removed: @media (max-width: 480px) > .trust-badge span { font-size: 11px !important; }**
- **Visual change if removed:** None.
- **Parts:** 4 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 4892-4892). Manual anchor: from `.trust-badge { gap: 14px !important; }` to `.trust-badge { gap: 14px !important; }`.
Delete:
```css
.trust-badge { gap: 14px !important; }
```

**Part 2** (baseline lines 4936-4937). Manual anchor: from `.trust-badges__inner { gap: 36px !important; }` to `.trust-badge__icon { width: 22px !important; height: 22px !important; }`.
Delete:
```css
  .trust-badges__inner { gap: 36px !important; }
  .trust-badge__icon { width: 22px !important; height: 22px !important; }
```

**Part 3** (baseline lines 4945-4946). Manual anchor: from `.trust-badge__icon { width: 18px !important; height: 18px !important; }` to `.trust-badge span { font-size: 12px !important; }`.
Delete:
```css
  .trust-badge__icon { width: 18px !important; height: 18px !important; }
  .trust-badge span { font-size: 12px !important; }
```

**Part 4** (baseline lines 4957-4959). Manual anchor: from `.trust-badges__inner { gap: 14px !important; }` to `.trust-badge span { font-size: 11px !important; }`.
Delete:
```css
  .trust-badges__inner { gap: 14px !important; }
  .trust-badge__icon { width: 14px !important; height: 14px !important; }
  .trust-badge span { font-size: 11px !important; }
```

### T50 [TODO] Earlier nav-dropdown bridge / padding / z-index attempts restated by the final nav block
- **File:** `assets/toylvia.css` | baseline lines 4318-4322, 4344-4347, 4548-4552, 4665-4667 | kind: always-overridden rules (same file, tool-proven)
- **Why it is dead:** Three earlier attempts at the nav dropdown hover bridge set .nav-dropdown position/padding-bottom/margin-bottom/z-index, .nav-dropdown__menu transition/pointer-events, and .site-header__nav-link/.nav-dropdown__trigger padding-bottom. A later top-level block at 4726-4782 sets every one of these longhands again, with the same selectors and !important. The section comments at 4317 and 4547 are kept because they also describe the live ::before/::after/hover rules next to these.
- **Proof:** shadow.js (headless Chrome): every removed rule has a LATER kept rule in the same file with a selector list containing its selectors, the same or top-level @media context, and every longhand at equal-or-higher priority -> PROVEN. Winners: toylvia.css 4726-4731 (html body .nav-dropdown padding/margin/position/z-index !important), 4744-4758 (html body .nav-dropdown__menu transition/pointer-events !important), 4780-4783 (html body .site-header__nav-link, html body .nav-dropdown__trigger padding-bottom 10px !important). Re-run independently by a skeptic agent (same result, no added rules).
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: html body .nav-dropdown { position: relative !important; padding-bottom: 18px !important; margin-bottom: -18px !important; } /   - removed: html body .nav-dropdown__menu { transition: opacity 0.25s 0.15s, transform 0.25s 0.15s !important; pointer-events: auto !important; } /   - removed: html body .nav-dropdown { position: relative; } /   - removed: html body .site-header__nav-link, html body .nav-dropdown__trigger { padding-bottom: 22px !important; } /   - removed: html body .nav-dropdown { z-index: 9999 !important; }**
- **Visual change if removed:** None.
- **Parts:** 4 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 4318-4322). Manual anchor: from `html body .nav-dropdown {` to `}`.
Delete:
```css
html body .nav-dropdown {
  position: relative !important;
  padding-bottom: 18px !important;
  margin-bottom: -18px !important;
}
```

**Part 2** (baseline lines 4344-4347). Manual anchor: from `html body .nav-dropdown__menu {` to `}`.
Delete:
```css
html body .nav-dropdown__menu {
  transition: opacity 0.25s ease 0.15s, transform 0.25s ease 0.15s !important;
  pointer-events: auto !important;
}
```

**Part 3** (baseline lines 4548-4552). Manual anchor: from `html body .nav-dropdown { position: relative; }` to `}`.
Delete:
```css
html body .nav-dropdown { position: relative; }
html body .site-header__nav-link,
html body .nav-dropdown__trigger {
  padding-bottom: 22px !important;
}
```

**Part 4** (baseline lines 4665-4667). Manual anchor: from `html body .nav-dropdown {` to `}`.
Delete:
```css
html body .nav-dropdown {
  z-index: 9999 !important;
}
```

### T51 [TODO] 'Doubled titles' 128px / 72px section-title sizes overridden later
- **File:** `assets/toylvia.css` | baseline lines 4307-4315 | kind: always-overridden rules (same file, tool-proven)
- **Why it is dead:** The '/* Doubled titles */' block sets section-title font-size 128px and line-height 1.02 at top level, and 72px inside @media (max-width:768px). The later top-level rules 4503 (line-height 1.1, font-size 64px) and 4876 (font-size 40px) restate both longhands with superset selector lists and !important, and the later @media (max-width:768px) rule at 4942 restates the 72px value. The comment and the @media wrapper contain only these two rules, so the whole block goes.
- **Proof:** shadow.js (headless Chrome): every removed rule has a LATER kept rule in the same file with a selector list containing its selectors, the same or top-level @media context, and every longhand at equal-or-higher priority -> PROVEN. Winners: toylvia.css 4503-4509 (line-height/font-size !important, top level), 4876-4885 (font-size 40px !important, top level), 4942 inside @media (max-width:768px) (font-size 26px !important). Re-run independently by a skeptic agent (same result, no added rules).
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (max-width: 768px) [group] /   - removed: html body .section-title, html body h2.section-title { font-size: 128px !important; line-height: 1.02 !important; } /   - removed: @media (max-width: 768px) > html body .section-title { font-size: 72px !important; }**
- **Visual change if removed:** None.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 4307-4315). Manual anchor: from `/* Doubled titles */` to `}`.
Delete:
```css
/* Doubled titles */
html body .section-title,
html body h2.section-title {
  font-size: 128px !important;
  line-height: 1.02 !important;
}
@media (max-width: 768px) {
  html body .section-title { font-size: 72px !important; }
}
```

### T52 [TODO] Product-card CTA border reset restated by a later CTA rule
- **File:** `assets/toylvia.css` | baseline lines 4294-4298 | kind: always-overridden rules (same file, tool-proven)
- **Why it is dead:** This rule sets border-width:0 and border-style:none !important on .product-card__cta (both selectors). The later top-level rule at 4921 has the identical selector list and 'border: none !important', which sets every border-width/style longhand. The comment at 4285 is kept because it also describes the live rule at 4286-4293.
- **Proof:** shadow.js (headless Chrome): every removed rule has a LATER kept rule in the same file with a selector list containing its selectors, the same or top-level @media context, and every longhand at equal-or-higher priority -> PROVEN. Winners: toylvia.css 4921-4927 (html body .product-card .product-card__cta, html body .product-card .product-card__footer .product-card__cta { border: none !important; ... }). Re-run independently by a skeptic agent (same result, no added rules).
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: html body .product-card .product-card__cta, html body .product-card .product-card__footer .product-card__cta { border-width: 0px !important; border-style: none !important; }**
- **Visual change if removed:** None.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 4294-4298). Manual anchor: from `html body .product-card .product-card__cta,` to `}`.
Delete:
```css
html body .product-card .product-card__cta,
html body .product-card .product-card__footer .product-card__cta {
  border-width: 0 !important;
  border-style: none !important;
}
```

### T53 [TODO] card-markers.css: category-marker size/inset/connector rules restated by later marker blocks
- **File:** `assets/card-markers.css` | baseline lines 3-6, 11-12, 17-19, 53-54 | kind: always-overridden rules (same file, tool-proven)
- **Why it is dead:** These are earlier copies of the category-marker rules that later blocks in the same file restate with the same selector lists, top-level context and !important. 3-6 (marker box, 9 longhands) is shadowed by 53 and then 59. 11-12 (soft-dot::before inset, radius, clip-path, background) is shadowed by 54 and then 62. 18 (connector width, min-width, height) is shadowed by 55. 19 (drift-card marker ::before width and height) is shadowed by 36-41. 53 (17 longhands) is fully restated by 59. 54 is fully restated by 62. The comment on line 17 describes only rules 18-19, so it goes with them. The comments on lines 2 and 52 stay because they also describe the live rules at 7-16 and 55. Every shadowing value is a var() or a plain length, so it is valid at parse time in every browser. shadow.js: 6 removed, PROVEN. cssom.js shows exactly these 6 rules removed and nothing added.
- **Proof:** shadow.js (headless Chrome): every removed rule has a LATER kept rule in the same file with a selector list containing its selectors, the same or top-level @media context, and every longhand at equal-or-higher priority -> PROVEN. Winners: card-markers.css 36-41, 55, 59, 62. Re-run independently by a skeptic agent (same result, no added rules).
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: #MainContent .cr-card__img-wrap > .cr-card__tag, #MainContent .product-card__image-wrap > .product-card__tag, #MainContent .cr-card__img-wrap > .soft-dot, #MainContent .product-card__image-wrap > .soft-dot { box-sizing: border-box !important; width: 25.15px !important; min-width: 25.15px !important; /   - removed: #MainContent .cr-card__img-wrap > .soft-dot::before, #MainContent .product-card__image-wrap > .soft-dot::before { inset: 0px !important; border-radius: 50% !important; clip-path: none !important; background: color-mix(in srgb,var(--dot) 50%,#fff) !important; } /   - removed: #MainContent .cr-card__img-wrap > .cr-card__tag::before, #MainContent .product-card__image-wrap > .product-card__tag::before, #MainContent .cr-card__img-wrap > .soft-dot > .tag-edge-line, #MainContent .product-card__image-wrap > .soft-dot > .tag-edge-line { width: var(--card-marker-dot-size) !import /   - removed: html body .drift-card [data-drift-category]::before { width: var(--card-marker-dot-size) !important; height: 0.5px !important; } /   - removed: #MainContent .cr-card__img-wrap > .cr-card__tag, #MainContent .product-card__image-wrap > .product-card__tag, #MainContent .cr-card__img-wrap > .soft-dot, #MainContent .product-card__image-wrap > .soft-dot { box-sizing: border-box !important; width: 25.15px !important; min-width: 25.15px !important; /   - removed: #MainContent .cr-card__img-wrap > .soft-dot::before, #MainContent .product-card__image-wrap > .soft-dot::before { inset: 8.6px !important; border-radius: 50% !important; clip-path: none !important; }**
- **Visual change if removed:** None.
- **Parts:** 4 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 3-6). Manual anchor: from `#MainContent .cr-card__img-wrap>.cr-card__tag,` to `#MainContent .product-card__image-wrap>.soft-dot{box-sizing:border-box!important;width:...`.
Delete:
```css
#MainContent .cr-card__img-wrap>.cr-card__tag,
#MainContent .product-card__image-wrap>.product-card__tag,
#MainContent .cr-card__img-wrap>.soft-dot,
#MainContent .product-card__image-wrap>.soft-dot{box-sizing:border-box!important;width:25.15px!important;min-width:25.15px!important;max-width:25.15px!important;height:25.15px!important;border-radius:50%!important}
```

**Part 2** (baseline lines 11-12). Manual anchor: from `#MainContent .cr-card__img-wrap>.soft-dot::before,` to `#MainContent .product-card__image-wrap>.soft-dot::before{inset:0!important;border-radiu...`.
Delete:
```css
#MainContent .cr-card__img-wrap>.soft-dot::before,
#MainContent .product-card__image-wrap>.soft-dot::before{inset:0!important;border-radius:50%!important;clip-path:none!important;background:color-mix(in srgb,var(--dot) 50%,#fff)!important}
```

**Part 3** (baseline lines 17-19). Manual anchor: from `/* Match every top-right marker dot and connector exactly; only the hue varies by tag. */` to `html body .drift-card [data-drift-category]::before{width:var(--card-marker-dot-size)!i...`.
Delete:
```css
/* Match every top-right marker dot and connector exactly; only the hue varies by tag. */
#MainContent .cr-card__img-wrap>.cr-card__tag::before,#MainContent .product-card__image-wrap>.product-card__tag::before,#MainContent .cr-card__img-wrap>.soft-dot>.tag-edge-line,#MainContent .product-card__image-wrap>.soft-dot>.tag-edge-line{width:var(--card-marker-dot-size)!important;min-width:var(--card-marker-dot-size)!important;height:.5px!important}
html body .drift-card [data-drift-category]::before{width:var(--card-marker-dot-size)!important;height:.5px!important}
```

**Part 4** (baseline lines 53-54). Manual anchor: from `#MainContent .cr-card__img-wrap>.cr-card__tag,#MainContent .product-card__image-wrap>.p...` to `#MainContent .cr-card__img-wrap>.soft-dot::before,#MainContent .product-card__image-wra...`.
Delete:
```css
#MainContent .cr-card__img-wrap>.cr-card__tag,#MainContent .product-card__image-wrap>.product-card__tag,#MainContent .cr-card__img-wrap>.soft-dot,#MainContent .product-card__image-wrap>.soft-dot{box-sizing:border-box!important;width:25.15px!important;min-width:25.15px!important;max-width:25.15px!important;height:25.15px!important;border-radius:50%!important;border-width:8.6px!important;padding:0!important}
#MainContent .cr-card__img-wrap>.soft-dot::before,#MainContent .product-card__image-wrap>.soft-dot::before{inset:8.6px!important;border-radius:50%!important;clip-path:none!important}
```

### T54 [TODO] home-palette.css: superseded .cat-strip__inner gap values (12px, mobile 8px)
- **File:** `assets/home-palette.css` | baseline lines 118-118, 262-262 | kind: always-overridden rules (same file, tool-proven)
- **Why it is dead:** "html body .cat-strip__inner { gap: 12px !important }" at line 118 is restated by the same selector at top level at line 288 (gap:14px !important), in the 'breathing room' block. The copy inside @media (max-width:767px) at line 262 (gap:8px !important) is shadowed by the top-level rule at 288 and also by the same-media rule at 303 (gap:10px !important). Line 262 is a single-line rule inside the 252-263 media block, so the block stays balanced. shadow.js: 2 removed, PROVEN. cssom.js shows exactly these 2 rules removed.
- **Proof:** shadow.js (headless Chrome): every removed rule has a LATER kept rule in the same file with a selector list containing its selectors, the same or top-level @media context, and every longhand at equal-or-higher priority -> PROVEN. Winners: home-palette.css 288 (and 303 inside @media max-width:767px). Re-run independently by a skeptic agent (same result, no added rules).
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: html body .cat-strip__inner { gap: 12px !important; } /   - removed: @media (max-width: 767px) > html body .cat-strip__inner { gap: 8px !important; }**
- **Visual change if removed:** None.
- **Parts:** 2 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 118-118). Manual anchor: from `html body .cat-strip__inner { gap: 12px !important; }` to `html body .cat-strip__inner { gap: 12px !important; }`.
Delete:
```css
html body .cat-strip__inner { gap: 12px !important; }
```

**Part 2** (baseline lines 262-262). Manual anchor: from `html body .cat-strip__inner { gap: 8px !important; }` to `html body .cat-strip__inner { gap: 8px !important; }`.
Delete:
```css
  html body .cat-strip__inner { gap: 8px !important; }
```

### T55 [TODO] card-markers.css: duplicate 'remove wishlist hearts' rule pasted twice
- **File:** `assets/card-markers.css` | baseline lines 175-180 | kind: always-overridden rules (same file, tool-proven)
- **Why it is dead:** Lines 176-179 (.cr-card .pc-heart, .product-card .pc-heart with 4x#MainContent: display:none, visibility:hidden, pointer-events:none, all !important) are a byte-identical copy of the rule at 203-206, which comes later in the same file at top level. The comment on line 175 describes only this rule, and line 180 is the blank line after it. shadow.js: 1 removed, PROVEN. cssom.js shows only this rule removed. The other scan looking for hidden-element styles may overlap with this.
- **Proof:** shadow.js (headless Chrome): every removed rule has a LATER kept rule in the same file with a selector list containing its selectors, the same or top-level @media context, and every longhand at equal-or-higher priority -> PROVEN. Winners: card-markers.css 203-206. Re-run independently by a skeptic agent (same result, no added rules).
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: html body #MainContent#MainContent#MainContent#MainContent .cr-card .pc-heart, html body #MainContent#MainContent#MainContent#MainContent .product-card .pc-heart { display: none !important; visibility: hidden !important; pointer-events: none !important; }**
- **Visual change if removed:** None.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 175-180). Manual anchor: from `/* Remove wishlist hearts from product cards only. The sidebar wishlist remains intact. */` to `}`.
Delete:
```css
/* Remove wishlist hearts from product cards only. The sidebar wishlist remains intact. */
html body #MainContent#MainContent#MainContent#MainContent .cr-card .pc-heart,
html body #MainContent#MainContent#MainContent#MainContent .product-card .pc-heart{
  display:none!important;visibility:hidden!important;pointer-events:none!important
}

```

### T56 [TODO] live-card-fixes.css: duplicate .cr-card__footer margin-top:0 rule (part inside T33)
- **File:** `assets/live-card-fixes.css` | baseline lines 72-72 | kind: always-overridden rules (same file, tool-proven)
- **Why it is dead:** Line 72 (3x#MainContent .cr-card.cr-card.cr-card .cr-card__footer{margin-top:0!important}) is fully restated by the identical selector at line 77 ({margin-top:0!important;margin-bottom:0!important}), at top level with the same !important. The comment on line 69 also describes the live rules at 70-71, so it stays. shadow.js: 1 removed, PROVEN. cssom.js shows only this rule removed.
- **Proof:** shadow.js (headless Chrome): every removed rule has a LATER kept rule in the same file with a selector list containing its selectors, the same or top-level @media context, and every longhand at equal-or-higher priority -> PROVEN. Winners: live-card-fixes.css 77. Re-run independently by a skeptic agent (same result, no added rules).
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: html body #MainContent#MainContent#MainContent .cr-card.cr-card.cr-card .cr-card__footer { margin-top: 0px !important; }**
- **Visual change if removed:** None.
- **Superseded by:** T33 (REVIEW). If Ziko approves T33, skip this item; it is included there.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 72-72). Manual anchor: from `html body #MainContent#MainContent#MainContent .cr-card.cr-card.cr-card .cr-card__foote...` to `html body #MainContent#MainContent#MainContent .cr-card.cr-card.cr-card .cr-card__foote...`.
Delete:
```css
html body #MainContent#MainContent#MainContent .cr-card.cr-card.cr-card .cr-card__footer{margin-top:0!important}
```

---

## Known issues that are NOT deletions (do not apply without asking Ziko)

- **Unclosed @media in toylvia.css (real bug, but fixing it CHANGES the site)**: Baseline line ~5535 opens `@media (max-width: 1024px) {` with a dangling `.cat-ice-label` selector and never closes it. Everything after it (about 670 lines: outlined Add to Cart pill, transparent header, free shipping bar, cart bundle, badge colours, mobile crash fix, ...) only applies at widths <= 1024px. Fixing it would switch those styles ON for desktop. Ask Ziko whether he wants that before touching it.
- **Ziko's DevTools edits to homepage product rows (pending his decision)**: Earlier in the cloud session Ziko unticked declarations at mobile width in assets/tlv-owner-overrides.css (tlv-row-header-gap translateY(18px); tlv-row-spacing row margins/paddings, the clamp() row gap and header padding/margin; tlv-header-shift translateY(9px); tlv-header-no-padding mobile block; tlv-row-unite mobile block) and in assets/home-palette.css (.cat-rows__row margin 0 1.25rem 0 and padding 0). Several are not inside a media query, so applying them as-is also changes desktop. Recommendation given: apply them inside @media(max-width:767px) only. He has not decided yet. Do not apply without asking.

