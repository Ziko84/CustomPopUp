# Toylvia CSS cleanup

Dead and commented-out CSS found in the live theme of https://toylvia.com by a cloud Claude scan.
Every item was found by one agent and then attacked by a separate skeptic agent that tried to prove it still affects the page. Only items that survived are listed.

- Scan started: 2026-10-11T15:16:39Z | last update: 2026-10-11T15:45:17Z | rounds: 1
- Items: **20** total, **16 TODO** (proven safe), **4 REVIEW** (very likely safe, ask Ziko first)
- Lines removed if every item is applied: 380 (TODO only: 359)
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

---

## Known issues that are NOT deletions (do not apply without asking Ziko)

- **Unclosed @media in toylvia.css (real bug, but fixing it CHANGES the site)**: Baseline line ~5535 opens `@media (max-width: 1024px) {` with a dangling `.cat-ice-label` selector and never closes it. Everything after it (about 670 lines: outlined Add to Cart pill, transparent header, free shipping bar, cart bundle, badge colours, mobile crash fix, ...) only applies at widths <= 1024px. Fixing it would switch those styles ON for desktop. Ask Ziko whether he wants that before touching it.
- **Ziko's DevTools edits to homepage product rows (pending his decision)**: Earlier in the cloud session Ziko unticked declarations at mobile width in assets/tlv-owner-overrides.css (tlv-row-header-gap translateY(18px); tlv-row-spacing row margins/paddings, the clamp() row gap and header padding/margin; tlv-header-shift translateY(9px); tlv-header-no-padding mobile block; tlv-row-unite mobile block) and in assets/home-palette.css (.cat-rows__row margin 0 1.25rem 0 and padding 0). Several are not inside a media query, so applying them as-is also changes desktop. Recommendation given: apply them inside @media(max-width:767px) only. He has not decided yet. Do not apply without asking.

