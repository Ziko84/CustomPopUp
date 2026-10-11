# Toylvia CSS cleanup

Dead and commented-out CSS found in the live theme of https://toylvia.com by a cloud Claude scan.
Every item was found by one agent and then attacked by a separate skeptic agent that tried to prove it still affects the page. Only items that survived are listed.

- Scan started: 2026-10-11T15:16:39Z | last update: 2026-10-11T17:04:37Z | rounds: 7
- Items: **120** total, **52 TODO** (proven safe), **68 REVIEW** (very likely safe, ask Ziko first)
- Lines removed if every item is applied (superseding items instead of the ones they contain): 3044 | TODO items only: 818
- Status legend: `TODO` apply | `REVIEW` apply only if Ziko says yes | `DONE` applied and verified | `SKIPPED: reason`

---

## FINAL SUMMARY FOR CLAUDE DESKTOP (read this first)

- STATE: nothing in this file has been applied to the live theme yet. Baseline md5s above were the live files at scan time (re-checked at ~16:20 UTC; the four main stylesheets were unchanged).
- WHAT TO DO, IN ORDER: (1) pull the live files listed under 'Files touched' (assets/*.css AND the .liquid files of T81-T88); (2) compare md5 with the baseline; (3) apply all TODO items with tools/apply.py (exact-text, refuses on any mismatch); (4) verify each file with tools/cssom.js compare against a backup (for every item the expected result is in its Verify line); (5) show Ziko the result and get his OK; (6) push with Shopify CLI (`--allow-live`), the Shopify MCP connector cannot write to the live theme; (7) re-pull and confirm md5; (8) mark items DONE/SKIPPED in findings.json, run tools/render.py, commit and push.
- REVIEW ITEMS: only with Ziko's approval, ideally applied to a duplicate theme first and previewed (homepage, product, collection, cart; desktop + mobile). Apply superseding items instead of the TODO items they contain.
- EXPECTED RESULT: TODO only = 806 lines removed (toylvia.css 6205 -> 5544, plus 99 lines of inline CSS in 8 .liquid files, T81-T88). Everything approved = 2592 lines (toylvia.css -> 3847). Both paths were tested end to end in the cloud: every item applied cleanly and every file changed exactly as predicted.
- DO NOT: repair dead code (e.g. re-add a missing /*), touch tlv-owner-overrides.css, fix the unclosed @media, or apply Ziko's DevTools row-spacing edits without asking (see 'Known issues').
- IF T01 FAILS with 'found 0 times': Ziko probably already deleted that block by hand; check and mark it DONE.
- NEXT (optional): finish the inline-CSS scan described under 'Not scanned yet' with the tools in tools/.

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
- Files touched: `assets/toylvia.css`, `assets/tlv-owner-overrides.css`, `assets/home-palette.css`, `assets/card-look.css`, `assets/live-card-fixes.css`, `assets/card-markers.css`, `sections/category-rows.liquid`, `sections/clg-hero.liquid`, `sections/collections-showcase.liquid`, `sections/story-pair.liquid`, `snippets/cr-card-styles.liquid`, `snippets/product-card-styles.liquid`, `snippets/product-recommendations.liquid`, `snippets/tlv-orbs.liquid`, `layout/theme.liquid`, `sections/about-us.liquid`, `sections/auth-drawer.liquid`, `sections/footer.liquid`, `sections/newsletter.liquid`, `sections/product-main.liquid`, `snippets/cart-drawer.liquid`, `snippets/collection-discovery-banners.liquid`, `snippets/collection-page.liquid`, `snippets/heart-js.liquid`, `snippets/product-description-card.liquid`, `templates/page.liquid`, `templates/page.wishlist.liquid`.
- Baseline md5 of each file when the scan read it:

  - `assets/toylvia.css`: `efc069df951128a76ac1adb542f17234`
  - `assets/tlv-owner-overrides.css`: `85a3bd4e370256a4f8dd92b7939a3531`
  - `assets/home-palette.css`: `01f05408f5ad9004afeb97c14313d787`
  - `assets/card-look.css`: `80c3701d5039636bd309a2760a3363b8`
  - `assets/live-card-fixes.css`: `35cf670e3bcd601f2d54a49ed3e57448`
  - `assets/card-markers.css`: `c447cc9f8b7e86be72bc5416aa421296`
  - `sections/category-rows.liquid`: `78e0ea43ea6c22153e712d8014de2d39`
  - `sections/clg-hero.liquid`: `3510c7d814872c85888695feb5d5589f`
  - `sections/collections-showcase.liquid`: `85bdf62c3f0d6f206b6bc6cd4c8151e3`
  - `sections/story-pair.liquid`: `f2ccb5e00a5bb4d9a1333e59f517b36f`
  - `snippets/cr-card-styles.liquid`: `b22ac5b7f2202ba5229f284573497e40`
  - `snippets/product-card-styles.liquid`: `a60975a8ed5af29e8213a5bd3d7f9016`
  - `snippets/product-recommendations.liquid`: `c67ce07f996cf2a3e53cbc865e4912ab`
  - `snippets/tlv-orbs.liquid`: `e34d6462a4f66ef79af21365bc84de89`
  - `layout/theme.liquid`: `e14a6630c3e8b81d3daaca6d74e109d4`
  - `sections/about-us.liquid`: `b7aa85c9aa5b63b878aab6f4e502fb8a`
  - `sections/auth-drawer.liquid`: `3a0b0dcfac22a6029223c9d8244b4000`
  - `sections/footer.liquid`: `fb7316ff5bbdeb1efe36ed02697df487`
  - `sections/newsletter.liquid`: `29b596d35351601c42e57980c5cdba52`
  - `sections/product-main.liquid`: `b1331d1f588dd6ece20379dc05d455f8`
  - `snippets/cart-drawer.liquid`: `3a9fc36e07af326c813d0c47a5ca9f1b`
  - `snippets/collection-discovery-banners.liquid`: `78c39ea9ba6ecab900a9574ad605c9ec`
  - `snippets/collection-page.liquid`: `94f2bf45e94598f0aea8bb08c70ede03`
  - `snippets/heart-js.liquid`: `5135fc3e5bb97a6843fc925e7473cbeb`
  - `snippets/product-description-card.liquid`: `060e2019b0ae50d0241fc632e631cb4e`
  - `templates/page.liquid`: `f9e800dd30cfeeada661b6ef57d71c08`
  - `templates/page.wishlist.liquid`: `6cb086aa507ac627e805af3d860ee3f9`

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
   - **Items in `.liquid` files** (CSS inside `<style>` blocks of templates/sections/snippets): compare CSS views instead of the raw files, because Liquid is not CSS:
     `python toylvia-css-cleanup/tools/liquid_css_view.py file.before.liquid before.css` and the same for the edited file, then `node toylvia-css-cleanup/tools/cssom.js compare before.css after.css`. The view keeps line numbers and replaces Liquid with neutral placeholders. Pull these files with `--only sections/x.liquid` / `--only snippets/x.liquid` / `--only layout/theme.liquid`. These files also contain HTML and Liquid: never edit anything outside the listed exact text.
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

### T57 [REVIEW] Collection back button: back-arrow, wrapper and pink/yellow/cyan colour variants
- **File:** `assets/toylvia.css` | baseline lines 1979-2027 | kind: orphan selectors (no markup uses these classes)
- **Why it is dead:** No markup or script ever outputs .back-arrow, .collection-back-wrapper, .collection-back-btn--pink, --yellow or --cyan. Their only mentions are CSS text: the CSS string toylvia.js:1103 injects into a <style> element, and the custom_css array in settings_data.json line 60. Neither counts as usage. The base .collection-back-btn rule (1962-1978, kept with its header) counts as used because of the querySelector strings in toylvia.js:1113 and 1267. Nothing in the theme builds 'collection-back-btn--' dynamically. The range covers whole rules from .collection-back-btn .back-arrow through .collection-back-btn--cyan:hover, plus one trailing blank line.
- **Proof:** Class search over all layout/sections/snippets/templates/settings_data and JS (class attributes, classList, className, querySelector strings, template literals, Liquid-built names; CSS-only mentions do not count): .back-arrow (only in toylvia.js:1103 CSS string); .collection-back-wrapper (only toylvia.js:1103 CSS string and settings_data custom_css); .collection-back-btn--pink/--yellow/--cyan (only toylvia.js:1103 CSS string); no 'collection-back-btn--' + / {{ }} construction anywhere Independently re-checked by a skeptic agent; Chrome CSSOM: only these rules removed.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .collection-back-btn .back-arrow { width: 18px; height: 18px; flex-shrink: 0; transition: transform 0.25s; display: inline-block; } /   - removed: .collection-back-btn:hover .back-arrow { transform: translateX(-3px); } /   - removed: .collection-back-wrapper { margin-bottom: 0.5rem; } /   - removed: .collection-back-btn--pink { border-color: hsl(var(--toylvia-pink)); color: hsl(var(--toylvia-pink)); } /   - removed: .collection-back-btn--pink:hover { background: hsl(var(--toylvia-pink)); color: rgb(255, 255, 255); transform: translateX(-4px); } /   - removed: .collection-back-btn--yellow { border-color: hsl(var(--toylvia-yellow)); color: rgb(204, 150, 0); } /   - removed: .collection-back-btn--yellow:hover { background: hsl(var(--toylvia-yellow)); color: rgb(26, 26, 26); transform: translateX(-4px); box-shadow: rgba(255, 216, 61, 0.4) 4px 4px 16px; } /   - removed: .collection-back-btn--cyan { border-color: hsl(var(--toylvia-cyan)); color: rgb(105, 179, 15); } /   - removed: .collection-back-btn--cyan:hover { background: hsl(var(--toylvia-cyan)); color: rgb(255, 255, 255); transform: translateX(-4px); box-shadow: rgba(33, 213, 237, 0.35) 4px 4px 16px; }**
- **Visual change if removed:** None expected (markup-based, hence REVIEW).
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 1979-2027). Manual anchor: from `.collection-back-btn .back-arrow {` to `}`.
Delete:
```css
.collection-back-btn .back-arrow {
  width: 18px;
  height: 18px;
  flex-shrink: 0;
  transition: transform 0.25s ease;
  display: inline-block;
}
.collection-back-btn:hover .back-arrow {
  transform: translateX(-3px);
}
.collection-back-wrapper {
  margin-bottom: 0.5rem;
}

/* pink pages: building-blocks, toy-blasters, all-products */
.collection-back-btn--pink {
  border-color: hsl(var(--toylvia-pink));
  color: hsl(var(--toylvia-pink));
}
.collection-back-btn--pink:hover {
  background: hsl(var(--toylvia-pink));
  color: #fff;
  transform: translateX(-4px);
  
}

/* yellow pages: collectibles, plush-toys */
.collection-back-btn--yellow {
  border-color: hsl(var(--toylvia-yellow));
  color: hsl(44, 100%, 40%);
}
.collection-back-btn--yellow:hover {
  background: hsl(var(--toylvia-yellow));
  color: #1a1a1a;
  transform: translateX(-4px);
  box-shadow: 4px 4px 16px hsla(48, 100%, 62%, 0.4);
}

/* cyan pages: vehicles, puzzles-iq */
.collection-back-btn--cyan {
  border-color: hsl(var(--toylvia-cyan));
  color: hsl(87, 85%, 38%);
}
.collection-back-btn--cyan:hover {
  background: hsl(var(--toylvia-cyan));
  color: #fff;
  transform: translateX(-4px);
  box-shadow: 4px 4px 16px hsla(187, 85%, 53%, 0.35);
}
```

### T58 [REVIEW] Legacy product-card image tints, badge and like button
- **File:** `assets/toylvia.css` | baseline lines 516-556 | kind: orphan selectors (no markup uses these classes)
- **Why it is dead:** No markup or JS outputs product-card__image, product-card__image--cyan/pink/yellow/purple/green/orange, product-card__badge or product-card__like. The product-card class is only added to cr-card in shared-product-card.liquid:73. Its children are cr-card__*, and nothing builds product-card__ or __image-- names dynamically. Both rules inside the (hover:hover) media block need .product-card__image, so the whole media group goes. .product-card__price (558) and .product-card__cta (563) are used and stay outside the range.
- **Proof:** Class search over all layout/sections/snippets/templates/settings_data and JS (class attributes, classList, className, querySelector strings, template literals, Liquid-built names; CSS-only mentions do not count): .product-card__image, .product-card__image--cyan/--pink/--yellow/--purple/--green/--orange, .product-card__badge, .product-card__like, .liked: 0 markup or script hits; .product-grid and .product-card are used, but every selector here also needs one of the missing classes Independently re-checked by a skeptic agent; Chrome CSSOM: only these rules removed.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (hover: hover) and (pointer: fine) [group] /   - removed: @media (hover: hover) and (pointer: fine) > .product-grid:hover .product-card__image img { filter: drop-shadow(rgba(0, 0, 0, 0.12) 0px 8px 20px) grayscale(0.6) brightness(0.92); } /   - removed: @media (hover: hover) and (pointer: fine) > .product-grid:hover .product-card:hover .product-card__image img { filter: drop-shadow(rgba(0, 0, 0, 0.12) 0px 8px 20px) grayscale(0); } /   - removed: .product-card__image--cyan { background: linear-gradient(to right bottom, rgb(226, 245, 248), rgb(203, 241, 246)); } /   - removed: .product-card__image--pink { background: linear-gradient(to right bottom, rgb(250, 235, 242), rgb(245, 214, 230)); } /   - removed: .product-card__image--yellow { background: linear-gradient(to right bottom, rgb(251, 246, 223), rgb(247, 235, 186)); } /   - removed: .product-card__image--purple { background: linear-gradient(to right bottom, rgb(241, 226, 248), rgb(232, 203, 246)); } /   - removed: .product-card__image--green { background: linear-gradient(to right bottom, rgb(226, 248, 234), rgb(205, 244, 218)); } /   - removed: .product-card__image--orange { background: linear-gradient(to right bottom, rgb(251, 235, 223), rgb(255, 219, 194)); } /   - removed: .product-card__badge { position: absolute; top: 0.75rem; left: 0.75rem; padding: 0.22rem 0.55rem; border-radius: 999px; background: transparent; font-size: 10px; font-weight: 700; letter-spacing: 0.08em; z-index: 5; } /   - removed: .product-card__like { position: absolute; top: 0.75rem; right: 0.75rem; width: 32px; height: 32px; border-radius: 50%; background: rgba(249, 250, 251, 0.8); backdrop-filter: blur(8px); display: flex; align-items: center; justify-content: center; transition: transform 0.3s cubic-bezier(0.34, 1.56, 0. /   - removed: .product-card__like:hover { transform: scale(1.1); } /   - removed: .product-card__like.liked svg { color: hsl(var(--destructive)); fill: hsl(var(--destructive)); }**
- **Visual change if removed:** None expected (markup-based, hence REVIEW).
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 516-556). Manual anchor: from `@media (hover: hover) and (pointer: fine) {` to `.product-card__like.liked svg { color: hsl(var(--destructive)); fill: hsl(var(--destruc...`.
Delete:
```css
@media (hover: hover) and (pointer: fine) {
  .product-grid:hover .product-card__image img { filter: drop-shadow(0 8px 20px rgba(0,0,0,0.12)) grayscale(0.6) brightness(0.92); }
  .product-grid:hover .product-card:hover .product-card__image img { filter: drop-shadow(0 8px 20px rgba(0,0,0,0.12)) grayscale(0); }
}
.product-card__image--cyan { background: linear-gradient(to bottom right, hsl(187,60%,93%), hsl(187,70%,88%)); }
.product-card__image--pink { background: linear-gradient(to bottom right, hsl(330,60%,95%), hsl(330,60%,90%)); }
.product-card__image--yellow { background: linear-gradient(to bottom right, hsl(48,80%,93%), hsl(48,80%,85%)); }
.product-card__image--purple { background: linear-gradient(to bottom right, hsl(280,60%,93%), hsl(280,70%,88%)); }
.product-card__image--green { background: linear-gradient(to bottom right, hsl(140,60%,93%), hsl(140,65%,88%)); }
.product-card__image--orange { background: linear-gradient(to bottom right, hsl(25,80%,93%), hsl(25,100%,88%)); }

.product-card__badge {
  position: absolute;
  top: 0.75rem;
  left: 0.75rem;
  padding: 0.22rem 0.55rem;
  border-radius: 999px;
  background: transparent;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.08em;
  z-index: 5;
}

.product-card__like {
  position: absolute;
  top: 0.75rem;
  right: 0.75rem;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: hsla(210, 20%, 98%, 0.8);
  backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
  z-index: 5;
}
.product-card__like:hover { transform: scale(1.1); }
.product-card__like.liked svg { color: hsl(var(--destructive)); fill: hsl(var(--destructive)); }
```

### T59 [REVIEW] Border-shine animation: borderShine* keyframes and product-card--<color> rules
- **File:** `assets/toylvia.css` | baseline lines 1051-1089 | kind: orphan selectors (no markup uses these classes)
- **Why it is dead:** No markup or script outputs .product-card--cyan, --pink, --yellow, --purple, --green or --orange. shared-product-card.liquid takes no color parameter, and no 'product-card--' prefix is built with {{ }}, + or ${}. The only product-card--* occurrences outside toylvia.css are CSS in a <style> block in theme.liquid (lines 1339-1347). Searching the whole theme shows the six @keyframes borderShine* are referenced only by the six orphaned rules at 1084-1089. The comment at line 6108 is only text. The block is the complete dead feature: six keyframes, comment and six rules. 1031-1049 is already logged and 1050 is blank, so there is no overlap. The range ends with one trailing blank line.
- **Proof:** Class search over all layout/sections/snippets/templates/settings_data and JS (class attributes, classList, className, querySelector strings, template literals, Liquid-built names; CSS-only mentions do not count): .product-card--cyan/--pink/--yellow/--purple/--green/--orange: no class attribute or JS usage (only theme.liquid <style> CSS); borderShineCyan/Pink/Yellow/Purple/Green/Orange: only referenced at toylvia.css 1084-1089 Independently re-checked by a skeptic agent; Chrome CSSOM: only these rules removed.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @keyframes borderShineCyan { 0% { border-color: rgba(33, 213, 237, 0.15); box-shadow: rgba(0, 0, 0, 0.06) 0px 4px 16px; } 50% { border-color: rgba(33, 213, 237, 0.5); box-shadow: rgba(0, 0, 0, 0.06) 0px 4px 16px, rgba(33, 213, 237, 0.15) 0px 0px 18px; } 100% { border-color: rgba(33, 213, 237, 0.15); /   - removed: @keyframes borderShinePink { 0% { border-color: rgba(255, 66, 161, 0.15); box-shadow: rgba(0, 0, 0, 0.06) 0px 4px 16px; } 50% { border-color: rgba(255, 66, 161, 0.5); box-shadow: rgba(0, 0, 0, 0.06) 0px 4px 16px, rgba(255, 66, 161, 0.15) 0px 0px 18px; } 100% { border-color: rgba(255, 66, 161, 0.15); /   - removed: @keyframes borderShineYellow { 0% { border-color: rgba(255, 216, 61, 0.15); box-shadow: rgba(0, 0, 0, 0.06) 0px 4px 16px; } 50% { border-color: rgba(255, 216, 61, 0.5); box-shadow: rgba(0, 0, 0, 0.06) 0px 4px 16px, rgba(255, 216, 61, 0.15) 0px 0px 18px; } 100% { border-color: rgba(255, 216, 61, 0.15 /   - removed: @keyframes borderShinePurple { 0% { border-color: rgba(167, 60, 221, 0.15); box-shadow: rgba(0, 0, 0, 0.06) 0px 4px 16px; } 50% { border-color: rgba(167, 60, 221, 0.5); box-shadow: rgba(0, 0, 0, 0.06) 0px 4px 16px, rgba(167, 60, 221, 0.15) 0px 0px 18px; } 100% { border-color: rgba(167, 60, 221, 0.15 /   - removed: @keyframes borderShineGreen { 0% { border-color: rgba(37, 177, 84, 0.15); box-shadow: rgba(0, 0, 0, 0.06) 0px 4px 16px; } 50% { border-color: rgba(37, 177, 84, 0.5); box-shadow: rgba(0, 0, 0, 0.06) 0px 4px 16px, rgba(37, 177, 84, 0.15) 0px 0px 18px; } 100% { border-color: rgba(37, 177, 84, 0.15); bo /   - removed: @keyframes borderShineOrange { 0% { border-color: rgba(255, 121, 26, 0.15); box-shadow: rgba(0, 0, 0, 0.06) 0px 4px 16px; } 50% { border-color: rgba(255, 121, 26, 0.5); box-shadow: rgba(0, 0, 0, 0.06) 0px 4px 16px, rgba(255, 121, 26, 0.15) 0px 0px 18px; } 100% { border-color: rgba(255, 121, 26, 0.15 /   - removed: .product-card--cyan { animation: 8s ease 0s infinite normal none running borderShineCyan; } /   - removed: .product-card--pink { animation: 8s ease 0s infinite normal none running borderShinePink; } /   - removed: .product-card--yellow { animation: 8s ease 0s infinite normal none running borderShineYellow; } /   - removed: .product-card--purple { animation: 8s ease 0s infinite normal none running borderShinePurple; } /   - removed: .product-card--green { animation: 8s ease 0s infinite normal none running borderShineGreen; } /   - removed: .product-card--orange { animation: 8s ease 0s infinite normal none running borderShineOrange; }**
- **Visual change if removed:** None expected (markup-based, hence REVIEW).
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 1051-1089). Manual anchor: from `@keyframes borderShineCyan {` to `.product-card--orange { animation: borderShineOrange 8s ease infinite; }`.
Delete:
```css
@keyframes borderShineCyan {
  0% { border-color: hsla(187, 85%, 53%, 0.15); box-shadow: 0 4px 16px rgba(0,0,0,0.06); }
  50% { border-color: hsla(187, 85%, 53%, 0.5); box-shadow: 0 4px 16px rgba(0,0,0,0.06), 0 0 18px hsla(187, 85%, 53%, 0.15); }
  100% { border-color: hsla(187, 85%, 53%, 0.15); box-shadow: 0 4px 16px rgba(0,0,0,0.06); }
}
@keyframes borderShinePink {
  0% { border-color: hsla(330, 100%, 63%, 0.15); box-shadow: 0 4px 16px rgba(0,0,0,0.06); }
  50% { border-color: hsla(330, 100%, 63%, 0.5); box-shadow: 0 4px 16px rgba(0,0,0,0.06), 0 0 18px hsla(330, 100%, 63%, 0.15); }
  100% { border-color: hsla(330, 100%, 63%, 0.15); box-shadow: 0 4px 16px rgba(0,0,0,0.06); }
}
@keyframes borderShineYellow {
  0% { border-color: hsla(48, 100%, 62%, 0.15); box-shadow: 0 4px 16px rgba(0,0,0,0.06); }
  50% { border-color: hsla(48, 100%, 62%, 0.5); box-shadow: 0 4px 16px rgba(0,0,0,0.06), 0 0 18px hsla(48, 100%, 62%, 0.15); }
  100% { border-color: hsla(48, 100%, 62%, 0.15); box-shadow: 0 4px 16px rgba(0,0,0,0.06); }
}
@keyframes borderShinePurple {
    0% { border-color: hsla(280, 70%, 55%, 0.15); box-shadow: 0 4px 16px rgba(0,0,0,0.06); }
      50% { border-color: hsla(280, 70%, 55%, 0.5); box-shadow: 0 4px 16px rgba(0,0,0,0.06), 0 0 18px hsla(280, 70%, 55%, 0.15); }
        100% { border-color: hsla(280, 70%, 55%, 0.15); box-shadow: 0 4px 16px rgba(0,0,0,0.06); }
        }
        @keyframes borderShineGreen {
          0% { border-color: hsla(140, 65%, 42%, 0.15); box-shadow: 0 4px 16px rgba(0,0,0,0.06); }
            50% { border-color: hsla(140, 65%, 42%, 0.5); box-shadow: 0 4px 16px rgba(0,0,0,0.06), 0 0 18px hsla(140, 65%, 42%, 0.15); }
              100% { border-color: hsla(140, 65%, 42%, 0.15); box-shadow: 0 4px 16px rgba(0,0,0,0.06); }
              }
              @keyframes borderShineOrange {
                0% { border-color: hsla(25, 100%, 55%, 0.15); box-shadow: 0 4px 16px rgba(0,0,0,0.06); }
                  50% { border-color: hsla(25, 100%, 55%, 0.5); box-shadow: 0 4px 16px rgba(0,0,0,0.06), 0 0 18px hsla(25, 100%, 55%, 0.15); }
                    100% { border-color: hsla(25, 100%, 55%, 0.15); box-shadow: 0 4px 16px rgba(0,0,0,0.06); }
                    }


/* Border shine animation defaults */
.product-card--cyan { animation: borderShineCyan 8s ease infinite; }
.product-card--pink { animation: borderShinePink 8s ease infinite; }
.product-card--yellow { animation: borderShineYellow 8s ease infinite; }
.product-card--purple { animation: borderShinePurple 8s ease infinite; }
.product-card--green { animation: borderShineGreen 8s ease infinite; }
.product-card--orange { animation: borderShineOrange 8s ease infinite; }
```

### T60 [REVIEW] Product page trust badges block
- **File:** `assets/toylvia.css` | baseline lines 990-990, 1010-1018 | kind: orphan selectors (no markup uses these classes)
- **Why it is dead:** The .product-trust-badges class appears nowhere in layout, sections, snippets, templates, settings_data or assets JS. product-main.liquid does not output it. Every rule in the block requires it: the base rule, the .trust-badge and .trust-badge__icon descendants, and the max-width:639px media group. That makes the whole comment-delimited block dead. It ends right before the already-logged likeBurst keyframes at 1020.
- **Proof:** Class search over all layout/sections/snippets/templates/settings_data and JS (class attributes, classList, className, querySelector strings, template literals, Liquid-built names; CSS-only mentions do not count): .product-trust-badges: 0 hits (.trust-badge and .trust-badge__icon only appear in toylvia.js querySelector strings, but every selector here is also scoped under .product-trust-badges) Independently re-checked by a skeptic agent; Chrome CSSOM: only these rules removed.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (max-width: 639px) [group] /   - removed: @media (max-width: 639px) > .product-trust-badges { justify-content: center; gap: 0.6rem 1rem; margin-top: 1rem; padding-top: 1rem; flex-wrap: nowrap !important; }**
- **Visual change if removed:** None expected (markup-based, hence REVIEW).
- **Parts:** 2 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 990-990). Manual anchor: from `/* === PRODUCT PAGE TRUST BADGES === */` to `/* === PRODUCT PAGE TRUST BADGES === */`.
Delete:
```css
/* === PRODUCT PAGE TRUST BADGES === */
```

**Part 2** (baseline lines 1010-1018). Manual anchor: from `@media (max-width: 639px) {` to `}`.
Delete:
```css
@media (max-width: 639px) {
  .product-trust-badges {
    justify-content: center;
    gap: 0.6rem 1rem;
    margin-top: 1rem;
    padding-top: 1rem;
    flex-wrap: nowrap !important;
  }
}
```

### T61 [REVIEW] Newsletter social icon row
- **File:** `assets/toylvia.css` | baseline lines 711-714 | kind: orphan selectors (no markup uses these classes)
- **Why it is dead:** sections/newsletter.liquid outputs only newsletter__title, __subtitle, __form, __input and __btn. Neither .newsletter__socials nor .newsletter__social-link appears in any markup or script. Their only other mentions are CSS inside a <style> block in templates/page.liquid (lines 61-71). The range is directly followed by the already-logged 715-749, so the two can be cut together.
- **Proof:** Class search over all layout/sections/snippets/templates/settings_data and JS (class attributes, classList, className, querySelector strings, template literals, Liquid-built names; CSS-only mentions do not count): .newsletter__socials, .newsletter__social-link: only in templates/page.liquid <style> CSS, no class attribute or JS usage Independently re-checked by a skeptic agent; Chrome CSSOM: only these rules removed.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .newsletter__social-link:hover { color: hsl(var(--primary)); border-color: rgba(255, 66, 161, 0.4); }**
- **Visual change if removed:** None expected (markup-based, hence REVIEW).
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 711-714). Manual anchor: from `.newsletter__social-link:hover {` to `}`.
Delete:
```css
.newsletter__social-link:hover {
  color: hsl(var(--primary));
  border-color: hsla(330,100%,63%,0.4);
}
```

### T62 [REVIEW] Plexus canvas class and Tailwind-style utility classes
- **File:** `assets/toylvia.css` | baseline lines 1120-1141 | kind: orphan selectors (no markup uses these classes)
- **Why it is dead:** The plexus background is <canvas id="plexus-bg"> in snippets/plexus-bg.liquid and is only accessed by id. No code ever gives it the .plexus-canvas class. None of the utilities appears in any class attribute, classList, className or selector string: .text-center, .flex, .items-center, .justify-center, .gap-4, .mt-8, .mb-8, .py-6, .space-y-4. Every hit for 'flex' is an inline-style or style-value string such as style="display:flex" or el.style.display='flex', never a class. Both comment-delimited mini-blocks are fully dead. The range ends with one blank line, before the used max-width:639px media block at 1143.
- **Proof:** Class search over all layout/sections/snippets/templates/settings_data and JS (class attributes, classList, className, querySelector strings, template literals, Liquid-built names; CSS-only mentions do not count): .plexus-canvas (0 hits; canvas uses id plexus-bg); .text-center, .items-center, .justify-center, .gap-4, .mt-8, .mb-8, .py-6, .space-y-4 (0 hits); .flex (all hits were inline-style values or style.display strings, no class usage) Independently re-checked by a skeptic agent; Chrome CSSOM: only these rules removed.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .plexus-canvas { position: fixed; inset: 0px; width: 100%; height: 100%; pointer-events: none; z-index: 0; filter: blur(2px); opacity: 0.6; } /   - removed: .text-center { text-align: center; } /   - removed: .flex { display: flex; } /   - removed: .items-center { align-items: center; } /   - removed: .justify-center { justify-content: center; } /   - removed: .gap-4 { gap: 1rem; } /   - removed: .mt-8 { margin-top: 2rem; } /   - removed: .mb-8 { margin-bottom: 2rem; } /   - removed: .py-6 { padding-top: 1.5rem; padding-bottom: 1.5rem; } /   - removed: .space-y-4 > * + * { margin-top: 1rem; }**
- **Visual change if removed:** None expected (markup-based, hence REVIEW).
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 1120-1141). Manual anchor: from `/* Plexus canvas */` to `.space-y-4 > * + * { margin-top: 1rem; }`.
Delete:
```css
/* Plexus canvas */
.plexus-canvas {
  position: fixed;
  inset: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 0;
  filter: blur(2px);
  opacity: 0.6;
}

/* Utility */
.text-center { text-align: center; }
.flex { display: flex; }
.items-center { align-items: center; }
.justify-center { justify-content: center; }
.gap-4 { gap: 1rem; }
.mt-8 { margin-top: 2rem; }
.mb-8 { margin-bottom: 2rem; }
.py-6 { padding-top: 1.5rem; padding-bottom: 1.5rem; }
.space-y-4 > * + * { margin-top: 1rem; }
```

### T63 [REVIEW] Futuristic glitch-grid background for section.category-arc (rule, ::before, ::after)
- **File:** `assets/toylvia.css` | baseline lines 4171-4213 | kind: orphan selectors (no markup uses these classes)
- **Why it is dead:** All three rules need the class category-arc on a <section>. No markup or script outputs that class. sections/category-arc.liquid renders <section id="cat-section" class="holo-section scroll-reveal">, and no section schema sets a wrapper tag or class. The class has zero hits in layout/sections/snippets/templates/assets/*.js once <style> blocks are stripped. It appears only as CSS: settings_data custom_css 'section.category-arc {padding-top...}'. I also checked live Shopify content and found it in no page, article, collection or product body. The next rule, 4215-4219 (.category-arc__grid, .all-products-btn__wrapper), stays because all-products-btn__wrapper is used in category-arc.liquid:148. After this cut, @keyframes glitch-sweep (4221-4231) and glitch-flicker (4233-4242) are referenced by nothing, but they are not part of this range. The range runs past 4200 by 14 lines.
- **Proof:** Class search over all layout/sections/snippets/templates/settings_data and JS (class attributes, classList, className, querySelector strings, template literals, Liquid-built names; CSS-only mentions do not count): category-arc (0 markup/JS hits; no section schema class/tag; 0 in Shopify page/article/collection/product bodies); all-products-btn__wrapper USED (kept, outside range) Independently re-checked by a skeptic agent; Chrome CSSOM: only these rules removed.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: section.category-arc { position: relative !important; overflow: hidden !important; background: repeating-linear-gradient(90deg, rgba(0, 200, 255, 0.06) 0px, rgba(0, 200, 255, 0.06) 1px, transparent 1px, transparent 80px), repeating-linear-gradient(0deg, rgba(0, 200, 255, 0.05) 0px, rgba(0, 200, 255, /   - removed: section.category-arc::before { content: "" !important; position: absolute !important; inset: 0px !important; pointer-events: none !important; background: linear-gradient(90deg, transparent 0%, rgba(0, 240, 255, 0.35) 15%, transparent 16%, transparent 30%, rgba(255, 0, 180, 0.25) 45%, transparent 46% /   - removed: section.category-arc::after { content: "" !important; position: absolute !important; inset: 0px !important; pointer-events: none !important; background: linear-gradient(0deg, transparent 0%, rgba(0, 240, 255, 0.2) 30%, transparent 31%, transparent 60%, rgba(255, 0, 180, 0.18) 75%, transparent 76%) 8**
- **Visual change if removed:** None expected (markup-based, hence REVIEW).
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 4171-4213). Manual anchor: from `/* Futuristic glitchy grid background for category section */` to `}`.
Delete:
```css
/* Futuristic glitchy grid background for category section */
section.category-arc {
  position: relative !important;
  overflow: hidden !important;
  background:
    repeating-linear-gradient(90deg,
      rgba(0, 200, 255, 0.06) 0px, rgba(0, 200, 255, 0.06) 1px,
      transparent 1px, transparent 80px),
    repeating-linear-gradient(0deg,
      rgba(0, 200, 255, 0.05) 0px, rgba(0, 200, 255, 0.05) 1px,
      transparent 1px, transparent 80px),
    repeating-linear-gradient(0deg,
      rgba(255, 0, 180, 0.025) 0px, rgba(255, 0, 180, 0.025) 1px,
      transparent 1px, transparent 4px),
    radial-gradient(ellipse at center, rgba(10, 20, 40, 0.04), transparent 70%) !important;
}

section.category-arc::before {
  content: '' !important;
  position: absolute !important;
  inset: 0 !important;
  pointer-events: none !important;
  background:
    linear-gradient(90deg, transparent 0%, rgba(0, 240, 255, 0.35) 15%, transparent 16%, transparent 30%, rgba(255, 0, 180, 0.25) 45%, transparent 46%, transparent 70%, rgba(0, 240, 255, 0.3) 82%, transparent 83%) 0 25% / 100% 1px no-repeat,
    linear-gradient(90deg, transparent 0%, transparent 20%, rgba(0, 240, 255, 0.25) 40%, transparent 41%, transparent 60%, rgba(255, 255, 0, 0.2) 75%, transparent 76%) 0 68% / 100% 1px no-repeat,
    linear-gradient(90deg, transparent 0%, rgba(255, 0, 180, 0.3) 10%, transparent 11%, transparent 55%, rgba(0, 240, 255, 0.3) 70%, transparent 71%) 0 88% / 100% 1px no-repeat !important;
  z-index: 0 !important;
  animation: glitch-sweep 5s steps(10) infinite !important;
}

section.category-arc::after {
  content: '' !important;
  position: absolute !important;
  inset: 0 !important;
  pointer-events: none !important;
  background:
    linear-gradient(0deg, transparent 0%, rgba(0, 240, 255, 0.2) 30%, transparent 31%, transparent 60%, rgba(255, 0, 180, 0.18) 75%, transparent 76%) 8% 0 / 1px 100% no-repeat,
    linear-gradient(0deg, transparent 0%, transparent 20%, rgba(0, 240, 255, 0.15) 40%, transparent 41%) 22% 0 / 1px 100% no-repeat,
    linear-gradient(0deg, transparent 0%, rgba(255, 255, 0, 0.15) 15%, transparent 16%, transparent 70%, rgba(0, 240, 255, 0.2) 85%, transparent 86%) 66% 0 / 1px 100% no-repeat,
    linear-gradient(0deg, transparent 0%, rgba(0, 240, 255, 0.2) 55%, transparent 56%) 93% 0 / 1px 100% no-repeat !important;
  z-index: 0 !important;
  animation: glitch-flicker 3.2s steps(8) infinite !important;
}
```

### T64 [REVIEW] Social icons block: .newsletter__social-link / .site-footer__social-icon styling and brand hover colours
- **File:** `assets/toylvia.css` | baseline lines 3561-3571, 3575-3598 | kind: orphan selectors (no markup uses these classes)
- **Why it is dead:** Every selector needs newsletter__social-link or site-footer__social-icon, and no markup or script outputs either one. sections/newsletter.liquid uses nl-socials, and sections/footer.liquid uses site-footer__soc-icon. The only other mentions are CSS inside the <style> block in templates/page.liquid (lines 50-73). Neither class appears in any Shopify page, article or product body. The range ends on one blank line, and 3600 starts the live shopify-policy rule.
- **Proof:** Class search over all layout/sections/snippets/templates/settings_data and JS (class attributes, classList, className, querySelector strings, template literals, Liquid-built names; CSS-only mentions do not count): newsletter__social-link (only in page.liquid <style>), site-footer__social-icon (0 hits; footer uses site-footer__soc-icon); none in Shopify content bodies Independently re-checked by a skeptic agent; Chrome CSSOM: only these rules removed.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .newsletter__social-link, .site-footer__social-icon { background: transparent !important; border: none !important; box-shadow: none !important; backdrop-filter: none !important; color: rgba(255, 255, 255, 0.55) !important; transition: color 250ms, background 250ms, transform 250ms !important; } /   - removed: .newsletter__social-link::before, .site-footer__social-icon::before { display: none !important; } /   - removed: .newsletter__social-link svg, .site-footer__social-icon svg { opacity: 1; transition: fill 250ms, stroke 250ms; } /   - removed: .newsletter__social-link[aria-label="Facebook"]:hover, .site-footer__social-icon[aria-label="Facebook"]:hover { color: rgb(24, 119, 242) !important; transform: translateY(-3px); } /   - removed: .newsletter__social-link[aria-label="Instagram"]:hover, .site-footer__social-icon[aria-label="Instagram"]:hover { color: rgb(225, 48, 108) !important; transform: translateY(-3px); } /   - removed: .newsletter__social-link[aria-label="TikTok"]:hover, .site-footer__social-icon[aria-label="TikTok"]:hover { color: rgb(255, 66, 161) !important; transform: translateY(-3px); } /   - removed: .newsletter__social-link[aria-label="Twitter"]:hover, .site-footer__social-icon[aria-label="Twitter"]:hover { color: rgb(29, 161, 242) !important; transform: translateY(-3px); } /   - removed: .newsletter__social-link[aria-label="YouTube"]:hover, .site-footer__social-icon[aria-label="YouTube"]:hover { color: rgb(255, 0, 0) !important; transform: translateY(-3px); } /   - removed: .newsletter__social-link:hover svg, .site-footer__social-icon:hover svg { fill: currentcolor; stroke: currentcolor; opacity: 1; }**
- **Visual change if removed:** None expected (markup-based, hence REVIEW).
- **Parts:** 2 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 3561-3571). Manual anchor: from `/* Social Icons — clean default, brand fill on hover */` to `}`.
Delete:
```css
/* Social Icons — clean default, brand fill on hover */
.newsletter__social-link,
.site-footer__social-icon {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  backdrop-filter: none !important;
  -webkit-backdrop-filter: none !important;
  color: rgba(255,255,255,0.55) !important;
  transition: color 250ms ease, background 250ms ease, transform 250ms ease !important;
}
```

**Part 2** (baseline lines 3575-3598). Manual anchor: from `.newsletter__social-link::before,` to `.site-footer__social-icon:hover svg { fill: currentColor; stroke: currentColor; opacity...`.
Delete:
```css
.newsletter__social-link::before,
.site-footer__social-icon::before { display: none !important; }

.newsletter__social-link svg,
.site-footer__social-icon svg { opacity: 1; transition: fill 250ms ease, stroke 250ms ease; }

/* Hover: fill with brand color */
.newsletter__social-link[aria-label="Facebook"]:hover,
.site-footer__social-icon[aria-label="Facebook"]:hover { color: #1877F2 !important; transform: translateY(-3px); }

.newsletter__social-link[aria-label="Instagram"]:hover,
.site-footer__social-icon[aria-label="Instagram"]:hover { color: #E1306C !important; transform: translateY(-3px); }

.newsletter__social-link[aria-label="TikTok"]:hover,
.site-footer__social-icon[aria-label="TikTok"]:hover { color: #ff42a1 !important; transform: translateY(-3px); }

.newsletter__social-link[aria-label="Twitter"]:hover,
.site-footer__social-icon[aria-label="Twitter"]:hover { color: #1DA1F2 !important; transform: translateY(-3px); }

.newsletter__social-link[aria-label="YouTube"]:hover,
.site-footer__social-icon[aria-label="YouTube"]:hover { color: #FF0000 !important; transform: translateY(-3px); }

.newsletter__social-link:hover svg,
.site-footer__social-icon:hover svg { fill: currentColor; stroke: currentColor; opacity: 1; }
```

### T65 [REVIEW] Product-page trust badges neumorphic block (.product-trust-badges ...) incl. .announcement-bar__track animation kill
- **File:** `assets/toylvia.css` | baseline lines 2931-2960 | kind: orphan selectors (no markup uses these classes)
- **Why it is dead:** All four rules need product-trust-badges, or announcement-bar__track for the third selector of the third rule. Neither class is output anywhere. The announcement-bar section outputs only announcement-bar, __inner-emboss, __inner, __logo and __text, and there is no product-trust-badges markup. trust-badge itself counts as used because toylvia.js calls .closest('.trust-badge') and querySelectorAll('.trust-badge__icon'), so every rule here is compounded with an unused class. The next rule (2968: '.product-trust-badges .trust-badge, .trust-badge, ...') is live and stays.
- **Proof:** Class search over all layout/sections/snippets/templates/settings_data and JS (class attributes, classList, className, querySelector strings, template literals, Liquid-built names; CSS-only mentions do not count): product-trust-badges (0 hits), announcement-bar__track (0 hits); trust-badge treated USED (JS querySelector) but every rule here also requires product-trust-badges Independently re-checked by a skeptic agent; Chrome CSSOM: only these rules removed.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .product-trust-badges .trust-badge { background-color: rgb(240, 240, 243) !important; box-shadow: rgba(163, 177, 198, 0.6) 9px 9px 16px, rgb(255, 255, 255) -9px -9px 16px !important; border-radius: 50px !important; padding: 8px 16px !important; display: flex !important; align-items: center !importan /   - removed: .product-trust-badges .trust-badge span { font-weight: 700 !important; color: rgb(68, 68, 68) !important; letter-spacing: 0.04em !important; text-decoration: none !important; font-variation-settings: "wght" 700 !important; } /   - removed: .product-trust-badges, .product-trust-badges *, .announcement-bar__track { animation: auto ease 0s 1 normal none running none !important; }**
- **Visual change if removed:** None expected (markup-based, hence REVIEW).
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 2931-2960). Manual anchor: from `/* 1. Neumorphic White Design & Layout */` to `}`.
Delete:
```css
/* 1. Neumorphic White Design & Layout */
.product-trust-badges .trust-badge {
  background-color: #f0f0f3 !important;
  box-shadow: 
    9px 9px 16px rgba(163, 177, 198, 0.6), 
    -9px -9px 16px rgba(255, 255, 255, 1) !important;
  border-radius: 50px !important;
  padding: 8px 16px !important;
  display: flex !important;
  align-items: center !important;
  gap: 8px !important;
  border: none !important;
}


/* 3. Text Consistency (Stop thinning/color changes) */
.product-trust-badges .trust-badge span {
  font-weight: 700 !important;
  color: #444 !important; /* Adjust to your preferred dark gray */
  letter-spacing: 0.04em !important;
  text-decoration: none !important;
  font-variation-settings: "wght" 700 !important;
}

/* 4. Disable All Original Animations/Marquees */
.product-trust-badges,
.product-trust-badges *,
.announcement-bar__track {
  animation: none !important;
}
```

### T66 [REVIEW] Old blog-page leftovers: .card-btn, .card:hover .card-btn, .card,.featured
- **File:** `assets/toylvia.css` | baseline lines 2590-2617 | kind: orphan selectors (no markup uses these classes)
- **Why it is dead:** These rules are leftovers from a pasted blog-page stylesheet (2516-2617). They need card-btn, card or featured. My robust class-attribute extraction, which handles Liquid and ${} in class="" and className/classList/querySelector strings, found none of the three anywhere. None appears in any of the 10 pages, 65 articles, collection bodies or 740 product descriptions on Shopify. The same feature has more orphaned ranges, left out here only because of the 6-item limit: 2564-2576 (.card ... .footer span, 10 rules, cssom-confirmed), 2553-2561 (.badge.cyan/.yellow, .featured-body h2/.excerpt/.meta, .read-more x3, 8 rules, confirmed) and 2522-2532 (.toylvia-blog-wrapper and ::before, 2 rules, confirmed). Do NOT delete .grid (2562-2563, 2580-2588): the live Contact page body uses class="grid". Do NOT delete .badge (2552): it is used in about-us.liquid:68 and the contact/return page bodies. Also 
- **Proof:** Class search over all layout/sections/snippets/templates/settings_data and JS (class attributes, classList, className, querySelector strings, template literals, Liquid-built names; CSS-only mentions do not count): card-btn, card, featured: 0 class usages in theme markup/JS (only alt text/prose) and 0 in Shopify page/article/collection/product bodies; grid IS used in contact page body (excluded); badge USED (excluded) Independently re-checked by a skeptic agent; Chrome CSSOM: only these rules removed.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .card-btn { display: inline-flex; margin-top: 1.5rem; padding: 0.924rem 2.464rem; font-weight: 900; font-size: 16px; background: rgb(249, 250, 251); color: rgb(255, 42, 148); border: 2.5px solid transparent; border-radius: 9999px; box-shadow: rgba(255, 255, 255, 0.9) -10px -8px 20px, rgba(148, 150,  /   - removed: .card:hover .card-btn { background: rgb(249, 250, 251); color: rgb(255, 42, 148); box-shadow: rgba(255, 255, 255, 0.6) -10px -8px 20px, rgba(176, 148, 162, 0.4) 10px 8px 20px, rgb(33, 213, 237) 0px 0px 45px; transform: scale(1.05); } /   - removed: .card, .featured { display: block; text-decoration: none !important; color: inherit !important; }**
- **Visual change if removed:** None expected (markup-based, hence REVIEW).
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 2590-2617). Manual anchor: from `.card-btn {` to `}`.
Delete:
```css
.card-btn {
  display: inline-flex;
  margin-top: 1.5rem;
  padding: 0.924rem 2.464rem;
  font-weight: 900;
  font-size: 16px;
  background: rgb(249,250,251);
  color: rgb(255,42,148);
  border: 2.5px solid transparent;
  border-radius: 9999px;
  box-shadow: -10px -8px 20px rgba(255,255,255,0.9), 10px 8px 20px rgba(148,150,176,0.45);
  text-transform: uppercase;
  transition: all 0.4s ease;
}

.card:hover .card-btn {
  background: rgb(249,250,251);
  color: rgb(255,42,148);
  box-shadow: -10px -8px 20px rgba(255,255,255,0.6), 
              10px 8px 20px rgba(176, 148, 162, 0.4), 
              rgb(33, 213, 237) 0px 0px 45px;
  transform: scale(1.05);
}
.card, .featured {
  text-decoration: none !important;
  color: inherit !important;
  display: block;
}
```

### T67 [REVIEW] Mobile PRODUCT DESCRIPTION @media block for .product-main__description-full
- **File:** `assets/toylvia.css` | baseline lines 3299-3316 | kind: orphan selectors (no markup uses these classes)
- **Why it is dead:** The whole @media (max-width: 640px) block holds only .product-main__description-full rules (base, h2/h3, table). That class has zero hits in theme markup or JS, and none in any of the 740 product descriptions on Shopify. product-main.liquid does not output it. The @media opener is part of the range and its closing brace is at 3316, so brace balance is kept. The range ends on one blank line. A separate one-line rule at 3397 inside the MOBILE FIX V2 @media is also orphaned but was not included.
- **Proof:** Class search over all layout/sections/snippets/templates/settings_data and JS (class attributes, classList, className, querySelector strings, template literals, Liquid-built names; CSS-only mentions do not count): product-main__description-full (0 hits theme; 0 in Shopify product/page bodies) Independently re-checked by a skeptic agent; Chrome CSSOM: only these rules removed.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (max-width: 640px) [group] /   - removed: @media (max-width: 640px) > .product-main__description-full { padding: 0px 0.5rem !important; font-size: 15px !important; line-height: 1.7 !important; margin-top: 2rem !important; } /   - removed: @media (max-width: 640px) > .product-main__description-full h2, .product-main__description-full h3 { font-size: 19px !important; margin: 1.75rem 0px 0.875rem !important; } /   - removed: @media (max-width: 640px) > .product-main__description-full table { width: 100% !important; font-size: 14px !important; display: block !important; overflow-x: auto !important; }**
- **Visual change if removed:** None expected (markup-based, hence REVIEW).
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 3299-3316). Manual anchor: from `/* ---- PRODUCT DESCRIPTION ---- */` to `}`.
Delete:
```css
                                                                          /* ---- PRODUCT DESCRIPTION ---- */
                                                                          @media (max-width: 640px) {
                                                                            .product-main__description-full {
                                                                                padding: 0 0.5rem !important;
                                                                                    font-size: 15px !important;
                                                                                        line-height: 1.7 !important;
                                                                                            margin-top: 2rem !important;
                                                                                              }
                                                                                                .product-main__description-full h2,
                                                                                                  .product-main__description-full h3 { font-size: 19px !important; margin: 1.75rem 0 0.875rem !important; }
                                                                                                    .product-main__description-full table {
                                                                                                        width: 100% !important;
                                                                                                            font-size: 14px !important;
                                                                                                                display: block !important;
                                                                                                                    overflow-x: auto !important;
                                                                                                                        -webkit-overflow-scrolling: touch !important;
                                                                                                                          }
                                                                                                                          }
```

### T68 [REVIEW] Old blog-page leftovers: .container, .page-title (h1/span/p), .featured, .featured-img, .featured-body
- **File:** `assets/toylvia.css` | baseline lines 2537-2551 | kind: orphan selectors (no markup uses these classes)
- **Why it is dead:** These are part of the same pasted blog-page stylesheet as q-4. The classes container, page-title, featured, featured-img and featured-body are not output by any theme markup or script; the word matches are only JS variable names, alt text and prose. None appears in any Shopify page, article, collection or product body. 2552 (.badge) is live, which is why this range stops at 2551. Keep 2516-2521 (*, :root vars) and 2533 (a{}) too, because they are global and live.
- **Proof:** Class search over all layout/sections/snippets/templates/settings_data and JS (class attributes, classList, className, querySelector strings, template literals, Liquid-built names; CSS-only mentions do not count): container, page-title, featured, featured-img, featured-body (0 class usages theme; 0 in Shopify content); placeholder only matched as an input attribute Independently re-checked by a skeptic agent; Chrome CSSOM: only these rules removed.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .container { max-width: 1280px; margin: 0px auto; padding: 2rem 1.5rem; position: relative; z-index: 1; } /   - removed: .page-title { text-align: center; margin-bottom: 2.5rem; } /   - removed: .page-title h1 { font-size: 2.5rem; font-weight: 800; letter-spacing: 3px; } /   - removed: .page-title h1 span { color: var(--pink); } /   - removed: .page-title p { color: var(--text-muted); font-size: 0.8rem; letter-spacing: 1.5px; margin-top: 0.5rem; } /   - removed: .featured { position: relative; border-radius: var(--radius); overflow: hidden; background: var(--card); border: 1px solid var(--border); margin-bottom: 3rem; display: grid; grid-template-columns: 1fr 1fr; min-height: 420px; transition: border-color 0.4s, box-shadow 0.4s; } /   - removed: .featured:hover { border-color: var(--pink); box-shadow: rgba(255, 66, 161, 0.12) 0px 0px 20px; } /   - removed: .featured-img { background: linear-gradient(135deg, rgba(255, 66, 161, 0.15), rgba(33, 213, 237, 0.15)); display: flex; align-items: center; justify-content: center; min-height: 300px; position: relative; overflow: hidden; } /   - removed: .featured-img .placeholder { color: var(--text-muted); font-size: 0.75rem; letter-spacing: 2px; } /   - removed: .featured-body { padding: 2.5rem; display: flex; flex-direction: column; justify-content: center; }**
- **Visual change if removed:** None expected (markup-based, hence REVIEW).
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 2537-2551). Manual anchor: from `/* Container */` to `.featured-body{padding:2.5rem;display:flex;flex-direction:column;justify-content:center}`.
Delete:
```css
/* Container */
.container{max-width:1280px;margin:0 auto;padding:2rem 1.5rem;position:relative;z-index:1}

/* Page Title */
.page-title{text-align:center;margin-bottom:2.5rem}
.page-title h1{font-size:2.5rem;font-weight:800;letter-spacing:3px}
.page-title h1 span{color:var(--pink)}
.page-title p{color:var(--text-muted);font-size:.8rem;letter-spacing:1.5px;margin-top:.5rem}

/* Featured Article */
.featured{position:relative;border-radius:var(--radius);overflow:hidden;background:var(--card);border:1px solid var(--border);margin-bottom:3rem;display:grid;grid-template-columns:1fr 1fr;min-height:420px;transition:border-color .4s,box-shadow .4s}
.featured:hover{border-color:var(--pink);box-shadow:0 0 20px hsla(330,100%,63%,.12)}
.featured-img{background:linear-gradient(135deg,hsla(330,100%,63%,.15),hsla(187,85%,53%,.15));display:flex;align-items:center;justify-content:center;min-height:300px;position:relative;overflow:hidden}
.featured-img .placeholder{color:var(--text-muted);font-size:.75rem;letter-spacing:2px}
.featured-body{padding:2.5rem;display:flex;flex-direction:column;justify-content:center}
```

### T69 [REVIEW] Rotating neon .launch-btn feature (@property --btn-angle, .launch-btn rules, @keyframes btn-spin)
- **File:** `assets/toylvia.css` | baseline lines 4817-4867 | kind: orphan selectors (no markup uses these classes)
- **Why it is dead:** No markup or script anywhere outputs launch-btn, so .launch-btn, .launch-btn::before and .launch-btn .arrow can never match. I searched layout/sections/snippets/templates/settings_data/assets/*.js for 'launch-btn', 'btn-spin' and 'btn-angle', and the only hits are inside this block. The @property --btn-angle and @keyframes btn-spin exist only for .launch-btn::before (conic-gradient from var(--btn-angle), animation btn-spin), so they become dead along with it. The range is depth 0, before the unclosed @media, and brace-balanced; it ends on one trailing blank line before the V14 header at 4869.
- **Proof:** Class search over all layout/sections/snippets/templates/settings_data and JS (class attributes, classList, className, querySelector strings, template literals, Liquid-built names; CSS-only mentions do not count): .launch-btn (0 markup/JS hits), .arrow (only as a descendant of .launch-btn), btn-spin keyframe name (0 uses outside the block), --btn-angle custom property (0 uses outside the block) Independently re-checked by a skeptic agent; Chrome CSSOM: only these rules removed.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @property --btn-angle { syntax: "<angle>"; inherits: false; initial-value: 0deg; } /   - removed: .launch-btn { position: relative; display: inline-flex; align-items: center; gap: 10px; padding: 14px 28px; border-radius: 999px; background: transparent; color: rgb(255, 255, 255); font-weight: 600; font-size: 16px; text-decoration: none; border: none; isolation: isolate; cursor: pointer; } /   - removed: .launch-btn::before { content: ""; position: absolute; inset: -2px; border-radius: inherit; padding: 2px; background: conic-gradient( /     from var(--btn-angle), /     #00e5ff, /     #ff00d4, /     #00e5ff /   ); mask: linear-gradient(rgb(0, 0, 0) 0px, rgb(0, 0, 0) 0px) content-box exclude, linear-gradient(r /   - removed: .launch-btn .arrow { color: rgb(0, 229, 255); } /   - removed: @keyframes btn-spin { 100% { --btn-angle: 360deg; } }**
- **Visual change if removed:** None expected (markup-based, hence REVIEW).
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 4817-4867). Manual anchor: from `@property --btn-angle {` to `}`.
Delete:
```css
@property --btn-angle {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

.launch-btn {
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 14px 28px;
  border-radius: 999px;
  background: transparent;          /* was #000 — now see-through */
  color: #fff;
  font-weight: 600;
  font-size: 16px;
  text-decoration: none;
  border: none;
  isolation: isolate;
  cursor: pointer;
}

/* The rotating neon ring — drawn OUTSIDE the button, nothing fills the center */
.launch-btn::before {
  content: "";
  position: absolute;
  inset: -2px;                      /* border thickness */
  border-radius: inherit;
  padding: 2px;
  background: conic-gradient(
    from var(--btn-angle),
    #00e5ff,
    #ff00d4,
    #00e5ff
  );
  -webkit-mask:
    linear-gradient(#000 0 0) content-box,
    linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
          mask-composite: exclude;
  animation: btn-spin 3s linear infinite;
  z-index: -1;
  pointer-events: none;
}

.launch-btn .arrow { color: #00e5ff; }

@keyframes btn-spin {
  to { --btn-angle: 360deg; }
}
```

### T70 [REVIEW] Old newsletter social icons (.newsletter__socials / .newsletter__social-link)
- **File:** `assets/toylvia.css` | baseline lines 5932-5973 | kind: orphan selectors (no markup uses these classes)
- **Why it is dead:** sections/newsletter.liquid now renders its social links as .nl-socials / .nl-social-btn and styles them inline. No markup or JS outputs newsletter__socials or newsletter__social-link. The only other occurrences are CSS inside the <style> block of templates/page.liquid (lines 61-71), which does not count. All 4 rules require one of these classes. This is the whole comment-delimited block, at depth 1 inside the unclosed max-width:1024px @media, and it is balanced. The next line (5974) is the .tlv-lede comment, which stays.
- **Proof:** Class search over all layout/sections/snippets/templates/settings_data and JS (class attributes, classList, className, querySelector strings, template literals, Liquid-built names; CSS-only mentions do not count): .newsletter__socials (CSS-only, page.liquid <style>), .newsletter__social-link (CSS-only), .newsletter (used, but every selector also requires .newsletter__socials) Independently re-checked by a skeptic agent; Chrome CSSOM: only these rules removed.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (max-width: 1024px) > html body .newsletter .newsletter__socials { display: flex !important; gap: 14px !important; justify-content: center !important; align-items: center !important; margin: 1.2rem 0px 1.6rem !important; flex-wrap: nowrap !important; } /   - removed: @media (max-width: 1024px) > html body .newsletter .newsletter__socials a.newsletter__social-link { width: 46px !important; height: 46px !important; min-width: 46px !important; min-height: 46px !important; display: inline-flex !important; align-items: center !important; justify-content: center !impo /   - removed: @media (max-width: 1024px) > html body .newsletter .newsletter__socials a.newsletter__social-link svg { width: 22px !important; height: 22px !important; fill: none !important; stroke: currentcolor !important; stroke-width: 2 !important; display: block !important; flex-shrink: 0 !important; } /   - removed: @media (max-width: 1024px) > html body .newsletter .newsletter__socials a.newsletter__social-link:hover { background: rgba(255, 66, 161, 0.12) !important; border-color: rgb(255, 66, 161) !important; color: rgb(255, 66, 161) !important; }**
- **Visual change if removed:** None expected (markup-based, hence REVIEW).
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 5932-5973). Manual anchor: from `/* === SOCIAL ICONS: DEFINITIVE FINAL OVERRIDE — must stay last in file === */` to `}`.
Delete:
```css
/* === SOCIAL ICONS: DEFINITIVE FINAL OVERRIDE — must stay last in file === */
html body .newsletter .newsletter__socials {
  display: flex !important;
  gap: 14px !important;
  justify-content: center !important;
  align-items: center !important;
  margin: 1.2rem 0 1.6rem !important;
  flex-wrap: nowrap !important;
}
html body .newsletter .newsletter__socials a.newsletter__social-link {
  width: 46px !important;
  height: 46px !important;
  min-width: 46px !important;
  min-height: 46px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  border-radius: 50% !important;
  background: transparent !important;
  border: 1.5px solid rgba(255,66,161,0.35) !important;
  box-shadow: none !important;
  backdrop-filter: none !important;
  -webkit-backdrop-filter: none !important;
  color: #ff42a1 !important;
  flex-shrink: 0 !important;
  transition: background 0.2s, border-color 0.2s !important;
  text-decoration: none !important;
}
html body .newsletter .newsletter__socials a.newsletter__social-link svg {
  width: 22px !important;
  height: 22px !important;
  fill: none !important;
  stroke: currentColor !important;
  stroke-width: 2 !important;
  display: block !important;
  flex-shrink: 0 !important;
}
html body .newsletter .newsletter__socials a.newsletter__social-link:hover {
  background: rgba(255,66,161,0.12) !important;
  border-color: #ff42a1 !important;
  color: #ff42a1 !important;
}
```

### T71 [REVIEW] Product card star ratings (.pc-stars / .pc-stars__count) incl. its two @media blocks
- **File:** `assets/toylvia.css` | baseline lines 6027-6054 | kind: orphan selectors (no markup uses these classes)
- **Why it is dead:** The cards (snippets/shared-product-card.liquid) render ratings as .cr-card__stars / .cr-card__stars__count. No file outputs pc-stars or pc-stars__count, and nothing builds 'pc-' + something dynamically; the only pc- classes in markup are pc-heart and pc-vcount*. Every rule in the block, including those in the nested min-width:768px and max-width:767px media queries, needs .pc-stars or .pc-stars__count. This is the whole comment-delimited feature, balanced at depth 1, with one trailing blank line before the SOLD OUT header.
- **Proof:** Class search over all layout/sections/snippets/templates/settings_data and JS (class attributes, classList, className, querySelector strings, template literals, Liquid-built names; CSS-only mentions do not count): .pc-stars (0 hits), .pc-stars__count (0 hits); other pc-* in markup: pc-heart, pc-vcount, pc-vcount--inline, pc-vcount__label, pc-vcount__separator only Independently re-checked by a skeptic agent; Chrome CSSOM: only these rules removed.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (max-width: 1024px) > @media (max-width: 767px) [group] /   - removed: @media (max-width: 1024px) > .pc-stars { display: flex; align-items: center; gap: 2px; margin-bottom: 5px; position: relative; z-index: 2; flex-wrap: nowrap; } /   - removed: @media (max-width: 1024px) > .pc-stars svg { flex-shrink: 0; display: block; } /   - removed: @media (max-width: 1024px) > .pc-stars__count { font-size: 11px; font-weight: 600; color: rgba(255, 255, 255, 0.65); margin-left: 4px; line-height: 1; white-space: nowrap; } /   - removed: @media (max-width: 1024px) > @media (min-width: 768px) [group] /   - removed: @media (max-width: 1024px) > @media (min-width: 768px) > .pc-stars svg { width: 13px; height: 13px; } /   - removed: @media (max-width: 1024px) > @media (min-width: 768px) > .pc-stars__count { font-size: 11.5px; } /   - removed: @media (max-width: 1024px) > @media (max-width: 767px) > .pc-stars { gap: 1.5px; margin-bottom: 4px; } /   - removed: @media (max-width: 1024px) > @media (max-width: 767px) > .pc-stars svg { width: 11px; height: 11px; } /   - removed: @media (max-width: 1024px) > @media (max-width: 767px) > .pc-stars__count { font-size: 10px; margin-left: 3px; }**
- **Visual change if removed:** None expected (markup-based, hence REVIEW).
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 6027-6054). Manual anchor: from `/* ===== PRODUCT CARD STAR RATINGS ===== */` to `}`.
Delete:
```css
/* ===== PRODUCT CARD STAR RATINGS ===== */
.pc-stars {
  display: flex;
  align-items: center;
  gap: 2px;
  margin-bottom: 5px;
  position: relative;
  z-index: 2;
  flex-wrap: nowrap;
}
.pc-stars svg { flex-shrink: 0; display: block; }
.pc-stars__count {
  font-size: 11px;
  font-weight: 600;
  color: rgba(255,255,255,0.65);
  margin-left: 4px;
  line-height: 1;
  white-space: nowrap;
}
@media (min-width: 768px) {
  .pc-stars svg { width: 13px; height: 13px; }
  .pc-stars__count { font-size: 11.5px; }
}
@media (max-width: 767px) {
  .pc-stars { gap: 1.5px; margin-bottom: 4px; }
  .pc-stars svg { width: 11px; height: 11px; }
  .pc-stars__count { font-size: 10px; margin-left: 3px; }
}
```

### T72 [REVIEW] Category sphere label centering (.category-sphere__label)
- **File:** `assets/toylvia.css` | baseline lines 4681-4705 | kind: orphan selectors (no markup uses these classes)
- **Why it is dead:** Both rules (4681-4700 and 4702-4705) require .category-sphere__label in every selector. That class appears in no markup and no script. toylvia.js only queries .category-sphere, .category-sphere__ball and .category-sphere__icon, and sections/category-arc.liquid now outputs .cat-card* markup. The range sits between the live 'html body .category-arc' rule (4677-4680) and the 'Align nav items' header (4706), at depth 0, and is balanced. It does not overlap the logged 4568-4649.
- **Proof:** Class search over all layout/sections/snippets/templates/settings_data and JS (class attributes, classList, className, querySelector strings, template literals, Liquid-built names; CSS-only mentions do not count): .category-sphere__label (0 markup/JS hits); .category-sphere, .category-sphere__ball, .category-arc (treated as used via JS querySelector or section type), but the selectors also require __label Independently re-checked by a skeptic agent; Chrome CSSOM: only these rules removed.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: html body .category-arc .category-sphere .category-sphere__ball .category-sphere__label, html body .category-sphere .category-sphere__ball .category-sphere__label { position: absolute !important; inset: 0px !important; width: 100% !important; height: 100% !important; margin: 0px !important; padding: /   - removed: html body .category-arc .category-sphere:hover .category-sphere__ball .category-sphere__label, html body .category-sphere:hover .category-sphere__ball .category-sphere__label { transform: none !important; }**
- **Visual change if removed:** None expected (markup-based, hence REVIEW).
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 4681-4705). Manual anchor: from `html body .category-arc .category-sphere .category-sphere__ball .category-sphere__label,` to `}`.
Delete:
```css
html body .category-arc .category-sphere .category-sphere__ball .category-sphere__label,
html body .category-sphere .category-sphere__ball .category-sphere__label {
  position: absolute !important;
  top: 0 !important;
  left: 0 !important;
  right: 0 !important;
  bottom: 0 !important;
  inset: 0 !important;
  width: 100% !important;
  height: 100% !important;
  margin: 0 !important;
  padding: 0 4px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  text-align: center !important;
  line-height: 1 !important;
  transform: none !important;
  box-sizing: border-box !important;
}

html body .category-arc .category-sphere:hover .category-sphere__ball .category-sphere__label,
html body .category-sphere:hover .category-sphere__ball .category-sphere__label {
  transform: none !important;
}
```

### T73 [REVIEW] V14 legacy CLG hero pill grid (.clg-bg-blob, .clg-grid, .clg-pill, .clg-bend/face/edge, .clg-icon, .clg-text/title/slogan, #clg-tech-grid)
- **File:** `assets/toylvia.css` | baseline lines 4902-4920 | kind: orphan selectors (no markup uses these classes)
- **Why it is dead:** sections/clg-hero.liquid (Hero Drift) contains no clg-* classes. Across all markup and JS the only clg strings are the 'clg-hero' section type, the href '/#clg-hero' and getElementById('clg-hero'). None of clg-bg-blob, clg-grid, clg-pill, clg-bend, clg-face, clg-edge, clg-icon, clg-text, clg-title, clg-slogan or the id clg-tech-grid is output anywhere. The live line 4901 '#clg-hero, .clg-hero' is kept. The range covers 18 single-line rules plus the '/* scale now handled dynamically by JS */' comment at 4914, at depth 0, balanced. It is outside the logged 4900 and 4992-4997. The duplicate .clg-* lines inside the 4934-4963 media queries are mixed with live rules and are not included.
- **Proof:** Class search over all layout/sections/snippets/templates/settings_data and JS (class attributes, classList, className, querySelector strings, template literals, Liquid-built names; CSS-only mentions do not count): .clg-bg-blob, .clg-bg-blob--pink, .clg-bg-blob--cyan, .clg-grid, .clg-pill, .clg-bend, .clg-face, .clg-edge, .clg-icon, .clg-text, .clg-title, .clg-slogan, #clg-tech-grid: all 0 markup/JS hits Independently re-checked by a skeptic agent; Chrome CSSOM: only these rules removed.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .clg-bg-blob { position: absolute; border-radius: 50%; filter: blur(110px); opacity: 0.01; pointer-events: none; z-index: 0; } /   - removed: .clg-bg-blob--pink { width: 520px; height: 520px; background: rgb(255, 90, 168); top: -120px; left: -120px; } /   - removed: .clg-bg-blob--cyan { width: 520px; height: 520px; background: rgb(34, 211, 238); bottom: -160px; right: -120px; } /   - removed: .clg-grid { position: relative; z-index: 2; display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; max-width: 1000px; margin: 0px auto; } /   - removed: .clg-pill { position: relative; z-index: 2; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 16px; height: 280px; border-radius: 40px; text-decoration: none; color: rgb(17, 17, 17); overflow: hidden; isolation: isolate; transition: transform 0.35s, box-shadow /   - removed: .clg-pill:hover { transform: translateY(-10px); box-shadow: rgba(34, 211, 238, 0.35) 0px 20px 50px; } /   - removed: .clg-bend, .clg-face, .clg-edge { position: absolute; inset: 0px; border-radius: inherit; pointer-events: none; } /   - removed: .clg-bend { backdrop-filter: blur(3px) url("#clg-glass-blur"); z-index: 0; } /   - removed: .clg-face { background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.08)); box-shadow: rgba(0, 0, 0, 0.08) 0px 8px 8px; z-index: 1; } /   - removed: .clg-edge { border: 1px solid rgba(255, 255, 255, 0.6); box-shadow: rgba(255, 255, 255, 0.9) 0px 1px 0px inset, rgba(255, 255, 255, 0.25) 0px -1px 0px inset; z-index: 2; } /   - removed: .clg-icon { position: relative; z-index: 3; width: 110px; height: 110px; border-radius: 24px; display: flex; align-items: center; justify-content: center; box-shadow: rgba(0, 0, 0, 0.5) 0px 25px 24px; transition: transform 0.7s; } /   - removed: .clg-icon img { width: 82%; height: 82%; object-fit: contain; transition: transform 0.35s; } /   - removed: .clg-text { position: relative; z-index: 3; display: flex; flex-direction: column; align-items: center; gap: 4px; } /   - removed: .clg-title { font-size: 18px; font-weight: 800; letter-spacing: 1.5px; transition: color 0.25s; } /   - removed: .clg-slogan { font-size: 13px; color: rgb(85, 85, 85); font-weight: 500; } /   - removed: .clg-pill:hover .clg-title { color: rgb(255, 90, 168); } /   - removed: #clg-tech-grid { position: absolute; inset: 0px; width: 100%; height: 100%; z-index: 0; pointer-events: none; opacity: 0.25; transition: opacity 0.4s; mask-image: linear-gradient(to right, transparent, black 25%, black 75%, transparent), linear-gradient(transparent, black 25%, black 75%, transparent /   - removed: #clg-hero:hover #clg-tech-grid, .clg-hero:hover #clg-tech-grid { opacity: 0.25; }**
- **Visual change if removed:** None expected (markup-based, hence REVIEW).
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 4902-4920). Manual anchor: from `.clg-bg-blob { position: absolute; border-radius: 50%; filter: blur(110px); opacity: 0....` to `#clg-hero:hover #clg-tech-grid, .clg-hero:hover #clg-tech-grid { opacity: 0.25; }`.
Delete:
```css
.clg-bg-blob { position: absolute; border-radius: 50%; filter: blur(110px); opacity: 0.01; pointer-events: none; z-index: 0; }
.clg-bg-blob--pink { width: 520px; height: 520px; background: #ff5aa8; top: -120px; left: -120px; }
.clg-bg-blob--cyan { width: 520px; height: 520px; background: #22d3ee; bottom: -160px; right: -120px; }
.clg-grid { position: relative; z-index: 2; display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; max-width: 1000px; margin: 0 auto; }
.clg-pill { position: relative; z-index: 2; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 16px; height: 280px; border-radius: 40px; text-decoration: none; color: #111; overflow: hidden; isolation: isolate; transition: transform .35s ease, box-shadow .35s ease; }
.clg-pill:hover { transform: translateY(-10px); box-shadow: 0 20px 50px rgba(34,211,238,0.35); }
.clg-bend, .clg-face, .clg-edge { position: absolute; inset: 0; border-radius: inherit; pointer-events: none; }
.clg-bend { backdrop-filter: blur(3px) url(#clg-glass-blur); -webkit-backdrop-filter: blur(3px); z-index: 0; }
.clg-face { background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.08)); box-shadow: 0 8px 8px rgba(0,0,0,0.08); z-index: 1; }
.clg-edge { border: 1px solid rgba(255,255,255,0.6); box-shadow: inset 0 1px 0 rgba(255,255,255,0.9), inset 0 -1px 0 rgba(255,255,255,0.25); z-index: 2; }
.clg-icon { position: relative; z-index: 3; width: 110px; height: 110px; border-radius: 24px; display: flex; align-items: center; justify-content: center; box-shadow: 0 25px 24px rgba(0,0,0,0.5); transition: transform 0.7s ease; }
.clg-icon img { width: 82%; height: 82%; object-fit: contain; transition: transform .35s ease; }
/* scale now handled dynamically by JS */
.clg-text { position: relative; z-index: 3; display: flex; flex-direction: column; align-items: center; gap: 4px; }
.clg-title { font-size: 18px; font-weight: 800; letter-spacing: 1.5px; transition: color .25s ease; }
.clg-slogan { font-size: 13px; color: #555; font-weight: 500; }
.clg-pill:hover .clg-title { color: #ff5aa8; }
#clg-tech-grid { position: absolute; inset: 0; width: 100%; height: 100%; z-index: 0; pointer-events: none; opacity: 0.25; transition: opacity 0.4s ease; -webkit-mask-image: linear-gradient(to right, transparent, black 25%, black 75%, transparent), linear-gradient(to bottom, transparent, black 25%, black 75%, transparent); -webkit-mask-composite: destination-in; mask-image: linear-gradient(to right, transparent, black 25%, black 75%, transparent), linear-gradient(to bottom, transparent, black 25%, black 75%, transparent); mask-composite: intersect; }
#clg-hero:hover #clg-tech-grid, .clg-hero:hover #clg-tech-grid { opacity: 0.25; }
```

### T74 [REVIEW] 'Smooth Hover Animation Fix' for legacy .clg-pill cards
- **File:** `assets/toylvia.css` | baseline lines 6002-6017 | kind: orphan selectors (no markup uses these classes)
- **Why it is dead:** All 3 rules require .clg-pill, plus .clg-prod-img or .clg-card-inner for two of them. None of these classes is output by any markup or script; the clg-hero section has no clg-* markup. This is the whole comment-delimited block with its numbered sub-comments, at depth 1 inside the unclosed @media, balanced, ending on one blank line. It sits directly before the logged 6019-6025 (also clg-pill) and does not overlap it.
- **Proof:** Class search over all layout/sections/snippets/templates/settings_data and JS (class attributes, classList, className, querySelector strings, template literals, Liquid-built names; CSS-only mentions do not count): .clg-pill, .clg-prod-img, .clg-card-inner (0 markup/JS hits); #clg-hero is only used via getElementById, but every selector also requires .clg-pill Independently re-checked by a skeptic agent; Chrome CSSOM: only these rules removed.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (max-width: 1024px) > #clg-hero a.clg-pill { transition: transform 0.4s cubic-bezier(0.25, 1, 0.5, 1), box-shadow 0.4s !important; } /   - removed: @media (max-width: 1024px) > #clg-hero .clg-pill img.clg-prod-img { transition: transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1), filter 0.4s !important; } /   - removed: @media (max-width: 1024px) > #clg-hero .clg-pill .clg-card-inner { transition: box-shadow 0.4s !important; }**
- **Visual change if removed:** None expected (markup-based, hence REVIEW).
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 6002-6017). Manual anchor: from `/* Smooth Hover Animation Fix */` to `}`.
Delete:
```css
/* Smooth Hover Animation Fix */

/* 1. Animate the main card container */
#clg-hero a.clg-pill {
    transition: transform 0.4s cubic-bezier(0.25, 1, 0.5, 1), box-shadow 0.4s ease !important;
}

/* 2. Animate the product image scaling */
#clg-hero .clg-pill img.clg-prod-img {
    transition: transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1), filter 0.4s ease !important;
}

/* 3. Ensure internal shadow also transitions smoothly */
#clg-hero .clg-pill .clg-card-inner {
    transition: box-shadow 0.4s ease !important;
}
```

### T75 [REVIEW] Dead .product-card__image-wrap wishlist-heart styling (4 rules, base/svg/hover/is-on)
- **File:** `assets/live-card-fixes.css` | baseline lines 158-161 | kind: orphan selectors (no markup uses these classes)
- **Why it is dead:** Each of the 4 rules is a single selector that needs .product-card__image-wrap. No markup outputs that class: snippets/product-card.liquid just renders shared-product-card with card_context 'collection', which outputs <a class="cr-card product-card"> and an image wrapper of <div class="cr-card__img-wrap">. The class shows up only in CSS (snippets/product-card-styles.liquid, cr-card-styles.liquid and card-secondary-image-styles.liquid <style> blocks, and the CSS strings in layout/theme.liquid line 1885). No JS querySelector, className or string concatenation produces it. The working cr-card twins at lines 154-157 stay. The shared comment header at line 153 stays because it also covers 154-157. The range is brace-balanced (4 open, 4 close) and lines 158-161 hold no other rule.
- **Proof:** Class search over all layout/sections/snippets/templates/settings_data and JS (class attributes, classList, className, querySelector strings, template literals, Liquid-built names; CSS-only mentions do not count): .product-card__image-wrap: 0 hits in layout/sections/snippets/templates/settings_data/assets JS outside CSS (also 0 after blanking CSS-in-JS strings and comments). No dynamic prefix (product-card__{{, product-card__'+, product-card__${) exists. .product-card, .pc-heart and .is-on are used but don't matter because the required class is missing. Independently re-checked by a skeptic agent; Chrome CSSOM: only these rules removed.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .product-card.product-card.product-card .product-card__image-wrap > .pc-heart.pc-heart { display: flex !important; visibility: visible !important /   - removed: html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .product-card.product-card.product-card .product-card__image-wrap > .pc-heart.pc-heart svg { width: 16px !important; height: 16px !important; min /   - removed: html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .product-card.product-card.product-card .product-card__image-wrap > .pc-heart.pc-heart:hover { transform: scale(1.2) !important; } /   - removed: html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .product-card.product-card.product-card .product-card__image-wrap > .pc-heart.pc-heart.is-on svg { fill: rgb(255, 66, 161) !important; stroke: rg**
- **Visual change if removed:** None expected (markup-based, hence REVIEW).
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 158-161). Manual anchor: from `html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#Main...` to `html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#Main...`.
Delete:
```css
html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .product-card.product-card.product-card .product-card__image-wrap>.pc-heart.pc-heart{display:flex!important;visibility:visible!important;opacity:1!important;pointer-events:auto!important;position:absolute!important;top:7px!important;left:7px!important;right:auto!important;bottom:auto!important;width:22px!important;height:22px!important;min-width:22px!important;min-height:22px!important;flex:0 0 22px!important;margin:0!important;padding:0!important;background:transparent!important;border:0!important;box-shadow:none!important;border-radius:0!important;z-index:15!important;cursor:pointer!important;align-items:center!important;justify-content:center!important;transition:transform .15s ease!important}
html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .product-card.product-card.product-card .product-card__image-wrap>.pc-heart.pc-heart svg{width:16px!important;height:16px!important;min-width:16px!important;min-height:16px!important;stroke:#e0457f!important;stroke-width:2!important;filter:drop-shadow(0 0 2px rgba(255,255,255,.95))!important;transition:fill .15s ease,transform .15s ease!important}
html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .product-card.product-card.product-card .product-card__image-wrap>.pc-heart.pc-heart:hover{transform:scale(1.2)!important}
html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .product-card.product-card.product-card .product-card__image-wrap>.pc-heart.pc-heart.is-on svg{fill:#ff42a1!important;stroke:#ff42a1!important}
```

### T76 [REVIEW] Dead .product-card__image-wrap heart resize overrides (3 rules)
- **File:** `assets/live-card-fixes.css` | baseline lines 182-184 | kind: orphan selectors (no markup uses these classes)
- **Why it is dead:** Same dead feature as s-1: the 'Heart 5% bigger' copies aimed at .product-card__image-wrap>.pc-heart, a wrapper no markup or script outputs. Collection cards use cr-card__img-wrap from shared-product-card.liquid. Lines 179-181 (cr-card versions) and 185-186 (drift-heart) stay, and so does the shared header at line 178. Each line is exactly one single-selector rule, and the range is brace-balanced (3/3).
- **Proof:** Class search over all layout/sections/snippets/templates/settings_data and JS (class attributes, classList, className, querySelector strings, template literals, Liquid-built names; CSS-only mentions do not count): .product-card__image-wrap: unused, as in s-1. The other classes (.product-card, .pc-heart, .is-on) are used but not enough to match. Independently re-checked by a skeptic agent; Chrome CSSOM: only these rules removed.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .product-card.product-card.product-card .product-card__image-wrap > .pc-heart.pc-heart { width: 23px !important; height:  /   - removed: html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .product-card.product-card.product-card .product-card__image-wrap > .pc-heart.pc-heart svg { width: 22.5px !important; he /   - removed: html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .product-card.product-card.product-card .product-card__image-wrap > .pc-heart.pc-heart.is-on svg { fill: rgb(255, 66, 161**
- **Visual change if removed:** None expected (markup-based, hence REVIEW).
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 182-184). Manual anchor: from `html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#Main...` to `html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#Main...`.
Delete:
```css
html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .product-card.product-card.product-card .product-card__image-wrap>.pc-heart.pc-heart{width:23px!important;height:23px!important;min-width:23px!important;min-height:23px!important;flex:0 0 23px!important}
html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .product-card.product-card.product-card .product-card__image-wrap>.pc-heart.pc-heart svg{width:22.5px!important;height:22.5px!important;min-width:22.5px!important;min-height:22.5px!important;fill:none!important;stroke:#111!important}
html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .product-card.product-card.product-card .product-card__image-wrap>.pc-heart.pc-heart.is-on svg{fill:#ff42a1!important;stroke:#ff42a1!important}
```

### T77 [REVIEW] Dead variant-count-line / cr-card__meta-row centering (2 rules)
- **File:** `assets/card-markers.css` | baseline lines 192-201 | kind: orphan selectors (no markup uses these classes)
- **Why it is dead:** Rule 192-198 has 3 selectors. They need .cr-card__variant-count-line, .product-card__variant-count-line, and .cr-card__meta-row (the 3rd is '.cr-card .cr-card__meta-row .cr-card__variation-count', and .cr-card__meta-row is required even though .cr-card__variation-count shows up in a JS querySelector). Rule 199-201 needs .cr-card__meta-row. None of these classes is output by any markup or script. The shared-product-card.liquid body is card-category-name, cr-card__name, cr-card__stars and cr-card__footer, with no meta-row and no variant-count-line. The comment header at line 187 stays because it also covers the live .var-dot rule at 188-191. The range is brace-balanced (2/2) and ends right before the 'Card hearts stay removed' comment on line 202.
- **Proof:** Class search over all layout/sections/snippets/templates/settings_data and JS (class attributes, classList, className, querySelector strings, template literals, Liquid-built names; CSS-only mentions do not count): .cr-card__variant-count-line: 0 hits. .product-card__variant-count-line: 0. .cr-card__meta-row: 0 outside CSS (only in snippets/cr-card-styles.liquid <style>). There is no 'variant-count', 'meta-row' or dynamic prefix anywhere in markup or JS. Independently re-checked by a skeptic agent; Chrome CSSOM: only these rules removed.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: html body #MainContent#MainContent#MainContent#MainContent .cr-card .cr-card__variant-count-line, html body #MainContent#MainContent#MainContent#MainContent .product-card .product-card__variant-count-line, html body #MainContent#MainContent#MainContent#MainContent .cr-card .cr-card__meta-row .cr-car /   - removed: html body #MainContent#MainContent#MainContent#MainContent .cr-card .cr-card__meta-row { display: block !important; width: 100% !important; min-height: 0px !important; height: auto !important; margin: 0px !important; padding: 0px !important; text-align: center !important; }**
- **Visual change if removed:** None expected (markup-based, hence REVIEW).
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 192-201). Manual anchor: from `html body #MainContent#MainContent#MainContent#MainContent .cr-card .cr-card__variant-c...` to `}`.
Delete:
```css
html body #MainContent#MainContent#MainContent#MainContent .cr-card .cr-card__variant-count-line,
html body #MainContent#MainContent#MainContent#MainContent .product-card .product-card__variant-count-line,
html body #MainContent#MainContent#MainContent#MainContent .cr-card .cr-card__meta-row .cr-card__variation-count{
  display:block!important;flex:0 0 auto!important;width:100%!important;height:auto!important;min-height:12.5px!important;margin:0 auto 4px!important;padding:0!important;
  color:#707783!important;text-align:center!important;font:600 10px/12.5px Nunito,system-ui,sans-serif!important;
  white-space:nowrap!important
}
html body #MainContent#MainContent#MainContent#MainContent .cr-card .cr-card__meta-row{
  display:block!important;width:100%!important;min-height:0!important;height:auto!important;margin:0!important;padding:0!important;text-align:center!important
}
```

### T78 [REVIEW] Dead meta-row heart button + hit-area rules
- **File:** `assets/card-markers.css` | baseline lines 69-70 | kind: orphan selectors (no markup uses these classes)
- **Why it is dead:** Both selectors in each rule need .product-card__meta-row or .cr-card__meta-row, and no markup or JS outputs either one. The card hearts live in .cr-card__img-wrap (shared-product-card.liquid), not in a meta row. These rules belong to the stale 'Card meta + compact outlined cart action' block at lines 64-81. Neighbouring rules there stay: line 68 (.cr-card__variation-count, which a querySelector in card-shop-action.js counts as used) and line 71 onward (.cr-card__footer .cr-card__buy, which is used). The same dead meta-row feature also appears at 66-67 (s-6), 74, 84-85 and 125-126, each verified dead but left out of this list because of the 6-candidate limit.
- **Proof:** Class search over all layout/sections/snippets/templates/settings_data and JS (class attributes, classList, className, querySelector strings, template literals, Liquid-built names; CSS-only mentions do not count): .product-card__meta-row: 0 hits. .cr-card__meta-row: 0 hits outside CSS. .pc-heart is used but not enough. Independently re-checked by a skeptic agent; Chrome CSSOM: only these rules removed.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: #MainContent .product-card__meta-row .pc-heart, #MainContent .cr-card__meta-row .pc-heart { display: flex !important; align-items: center !important; justify-content: center !important; width: 36px !important; height: 36px !important; min-width: 36px !important; min-height: 36px !important; margin:  /   - removed: #MainContent .product-card__meta-row .pc-heart::after, #MainContent .cr-card__meta-row .pc-heart::after { content: "" !important; position: absolute !important; inset: -3px !important; background: transparent !important; border: 0px !important; pointer-events: auto !important; }**
- **Visual change if removed:** None expected (markup-based, hence REVIEW).
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 69-70). Manual anchor: from `#MainContent .product-card__meta-row .pc-heart,#MainContent .cr-card__meta-row .pc-hear...` to `#MainContent .product-card__meta-row .pc-heart::after,#MainContent .cr-card__meta-row ....`.
Delete:
```css
#MainContent .product-card__meta-row .pc-heart,#MainContent .cr-card__meta-row .pc-heart{display:flex!important;align-items:center!important;justify-content:center!important;width:36px!important;height:36px!important;min-width:36px!important;min-height:36px!important;margin:0!important;flex:0 0 36px!important;position:relative!important;color:#59796a!important;z-index:12!important;cursor:pointer!important;pointer-events:auto!important;touch-action:manipulation!important}
#MainContent .product-card__meta-row .pc-heart::after,#MainContent .cr-card__meta-row .pc-heart::after{content:""!important;position:absolute!important;inset:-3px!important;background:transparent!important;border:0!important;pointer-events:auto!important}
```

### T79 [REVIEW] Dead .var-dot__count / .var-dot__label typography (2 rules)
- **File:** `assets/card-markers.css` | baseline lines 95-98 | kind: orphan selectors (no markup uses these classes)
- **Why it is dead:** Every selector needs .var-dot__count or .var-dot__label. Those child classes show up only in CSS (product-card-styles.liquid and cr-card-styles.liquid <style> blocks, and home-palette.css). No markup creates a .var-dot element with those children, and no JS builds them: the only script mention of 'var-dot' is the querySelector('.var-dot,...') in card-shop-action.js, with no __count or __label and no var-dot__ concatenation. Lines 86-94 (.var-dot itself) and 99-100 stay. home-palette.css 207-208 is the same dead pair (.cat-rows .cr-card__img-wrap > .var-dot .var-dot__count/.var-dot__label). It was also verified dead (cssom: 90 -> 89, only that rule removed) and can be cut together with this one.
- **Proof:** Class search over all layout/sections/snippets/templates/settings_data and JS (class attributes, classList, className, querySelector strings, template literals, Liquid-built names; CSS-only mentions do not count): .var-dot__count: 0 hits outside CSS. .var-dot__label: 0 hits outside CSS. .var-dot is treated as used (querySelector string in card-shop-action.js). .product-card__image-wrap is unused. Independently re-checked by a skeptic agent; Chrome CSSOM: only these rules removed.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: html body #MainContent#MainContent .cr-card.cr-card.cr-card .cr-card__img-wrap > .var-dot .var-dot__count, html body #MainContent#MainContent .product-card.product-card .product-card__image-wrap > .var-dot .var-dot__count { font: 600 9px / 1.2 Nunito, system-ui, sans-serif !important; } /   - removed: html body #MainContent#MainContent .cr-card.cr-card.cr-card .cr-card__img-wrap > .var-dot .var-dot__label, html body #MainContent#MainContent .product-card.product-card .product-card__image-wrap > .var-dot .var-dot__label { font: 600 9px / 1.2 Nunito, system-ui, sans-serif !important; text-transform**
- **Visual change if removed:** None expected (markup-based, hence REVIEW).
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 95-98). Manual anchor: from `html body #MainContent#MainContent .cr-card.cr-card.cr-card .cr-card__img-wrap>.var-dot...` to `html body #MainContent#MainContent .product-card.product-card .product-card__image-wrap...`.
Delete:
```css
html body #MainContent#MainContent .cr-card.cr-card.cr-card .cr-card__img-wrap>.var-dot .var-dot__count,
html body #MainContent#MainContent .product-card.product-card .product-card__image-wrap>.var-dot .var-dot__count{font:600 9px/1.2 Nunito,system-ui,sans-serif!important}
html body #MainContent#MainContent .cr-card.cr-card.cr-card .cr-card__img-wrap>.var-dot .var-dot__label,
html body #MainContent#MainContent .product-card.product-card .product-card__image-wrap>.var-dot .var-dot__label{font:600 9px/1.2 Nunito,system-ui,sans-serif!important;text-transform:none!important}
```

### T80 [REVIEW] Dead meta-row flex layout rules
- **File:** `assets/card-markers.css` | baseline lines 66-67 | kind: orphan selectors (no markup uses these classes)
- **Why it is dead:** Both rules only target .product-card__meta-row / .cr-card__meta-row, which no markup or script outputs (same dead meta-row feature as s-3 and s-4). Line 65 (.var-dot, used via querySelector) and line 68 (.cr-card__variation-count, used via querySelector) stay, so the 64-81 block can't be removed whole. Other meta-row-only rules verified dead in this file: line 74 (meta-row .pc-heart svg), 84-85 (meta-row variation-count hide, cssom 75->74) and 125-126 (__body meta-row hide, cssom 75->74). home-palette.css 207-208 is listed under s-5.
- **Proof:** Class search over all layout/sections/snippets/templates/settings_data and JS (class attributes, classList, className, querySelector strings, template literals, Liquid-built names; CSS-only mentions do not count): .product-card__meta-row: 0 hits. .cr-card__meta-row: 0 hits outside CSS. The attribute selector [aria-hidden] doesn't matter because the meta-row ancestor is required. Independently re-checked by a skeptic agent; Chrome CSSOM: only these rules removed.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: #MainContent .product-card__meta-row, #MainContent .cr-card__meta-row { display: flex !important; align-items: center !important; justify-content: space-between !important; gap: 8px !important; min-height: 28px !important; margin: 0px 0px 4px !important; } /   - removed: #MainContent .product-card__meta-row > [aria-hidden="true"], #MainContent .cr-card__meta-row > [aria-hidden="true"] { flex: 1 1 auto !important; }**
- **Visual change if removed:** None expected (markup-based, hence REVIEW).
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 66-67). Manual anchor: from `#MainContent .product-card__meta-row,#MainContent .cr-card__meta-row{display:flex!impor...` to `#MainContent .product-card__meta-row>[aria-hidden="true"],#MainContent .cr-card__meta-r...`.
Delete:
```css
#MainContent .product-card__meta-row,#MainContent .cr-card__meta-row{display:flex!important;align-items:center!important;justify-content:space-between!important;gap:8px!important;min-height:28px!important;margin:0 0 4px!important}
#MainContent .product-card__meta-row>[aria-hidden="true"],#MainContent .cr-card__meta-row>[aria-hidden="true"]{flex:1 1 auto!important}
```

### T81 [TODO] 1 always-overridden rule(s) inside <style> blocks of sections/category-rows.liquid
- **File:** `sections/category-rows.liquid` | baseline lines 2193-2193 | kind: always-overridden rules in inline CSS (same <style> block, tool-proven)
- **Why it is dead:** Each removed rule is restated later in the SAME <style> block by a rule with the same selectors, same or top-level @media, every property at equal-or-higher priority, so it can never win. Selectors: .cat-rows__scroll
- **Proof:** Automated scan of all 313 <style> blocks via the CSS view (identical line numbers). Only rules on lines of pure CSS (no HTML/Liquid) and without Liquid in the selector were considered; the winner had to be in the same <style> block and not inside a Liquid {% if/unless/case/for %}. Joint check with tools/cssom.js + tools/shadow.js on the views: all removed together -> PROVEN, no added rules.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (max-width: 767px) > .cat-rows__scroll { padding: 0px 1.25rem; }**
- **Visual change if removed:** None.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 2193-2193). Manual anchor: from `.cat-rows__scroll { padding: 0 1.25rem; }` to `.cat-rows__scroll { padding: 0 1.25rem; }`.
Delete:
```css
  .cat-rows__scroll { padding: 0 1.25rem; }
```

### T82 [TODO] 1 always-overridden rule(s) inside <style> blocks of sections/clg-hero.liquid
- **File:** `sections/clg-hero.liquid` | baseline lines 4581-4581 | kind: always-overridden rules in inline CSS (same <style> block, tool-proven)
- **Why it is dead:** Each removed rule is restated later in the SAME <style> block by a rule with the same selectors, same or top-level @media, every property at equal-or-higher priority, so it can never win. Selectors: .cat-strip__inner .cat-pill svg
- **Proof:** Automated scan of all 313 <style> blocks via the CSS view (identical line numbers). Only rules on lines of pure CSS (no HTML/Liquid) and without Liquid in the selector were considered; the winner had to be in the same <style> block and not inside a Liquid {% if/unless/case/for %}. Joint check with tools/cssom.js + tools/shadow.js on the views: all removed together -> PROVEN, no added rules.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .cat-strip__inner .cat-pill svg { width: 18px !important; height: 18px !important; }**
- **Visual change if removed:** None.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 4581-4581). Manual anchor: from `.cat-strip__inner .cat-pill svg{width:18px!important;height:18px!important}` to `.cat-strip__inner .cat-pill svg{width:18px!important;height:18px!important}`.
Delete:
```css
.cat-strip__inner .cat-pill svg{width:18px!important;height:18px!important}
```

### T83 [TODO] 2 always-overridden rule(s) inside <style> blocks of sections/collections-showcase.liquid
- **File:** `sections/collections-showcase.liquid` | baseline lines 138-138, 198-207 | kind: always-overridden rules in inline CSS (same <style> block, tool-proven)
- **Why it is dead:** Each removed rule is restated later in the SAME <style> block by a rule with the same selectors, same or top-level @media, every property at equal-or-higher priority, so it can never win. Selectors: .cs-card-wrap--featured .cs-card__cell img; .cs-card-wrap--featured .cs-card__cell img, .cs-card-wrap--featured .cs-card__cell:hover img
- **Proof:** Automated scan of all 313 <style> blocks via the CSS view (identical line numbers). Only rules on lines of pure CSS (no HTML/Liquid) and without Liquid in the selector were considered; the winner had to be in the same <style> block and not inside a Liquid {% if/unless/case/for %}. Joint check with tools/cssom.js + tools/shadow.js on the views: all removed together -> PROVEN, no added rules.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (min-width: 768px) > .cs-card-wrap--featured .cs-card__cell img { transition: none; } /   - removed: @media (max-width: 767px) > .cs-card-wrap--featured .cs-card__cell img, .cs-card-wrap--featured .cs-card__cell:hover img { position: static !important; width: 100% !important; height: 100% !important; left: auto !important; transform: none !important; transition: transform 0.32s !important; object-f**
- **Visual change if removed:** None.
- **Parts:** 2 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 138-138). Manual anchor: from `.cs-card-wrap--featured .cs-card__cell img { transition: none; }` to `.cs-card-wrap--featured .cs-card__cell img { transition: none; }`.
Delete:
```css
  .cs-card-wrap--featured .cs-card__cell img { transition: none; }
```

**Part 2** (baseline lines 198-207). Manual anchor: from `.cs-card-wrap--featured .cs-card__cell img,` to `}`.
Delete:
```css
  .cs-card-wrap--featured .cs-card__cell img,
  .cs-card-wrap--featured .cs-card__cell:hover img {
    position: static !important;
    width: 100% !important;
    height: 100% !important;
    left: auto !important;
    transform: none !important;
    transition: transform 0.32s ease !important;
    object-fit: cover !important;
  }
```

### T84 [TODO] 3 always-overridden rule(s) inside <style> blocks of sections/story-pair.liquid
- **File:** `sections/story-pair.liquid` | baseline lines 193-193, 194-194, 195-195 | kind: always-overridden rules in inline CSS (same <style> block, tool-proven)
- **Why it is dead:** Each removed rule is restated later in the SAME <style> block by a rule with the same selectors, same or top-level @media, every property at equal-or-higher priority, so it can never win. Selectors: .tlv-sp.tlv-sp; .tlv-sp.tlv-sp .tlv-sp-card.tlv-sp-card:nth-of-type(10); .tlv-sp.tlv-sp .tlv-sp-card.tlv-sp-card:nth-of-type(9)
- **Proof:** Automated scan of all 313 <style> blocks via the CSS view (identical line numbers). Only rules on lines of pure CSS (no HTML/Liquid) and without Liquid in the selector were considered; the winner had to be in the same <style> block and not inside a Liquid {% if/unless/case/for %}. Joint check with tools/cssom.js + tools/shadow.js on the views: all removed together -> PROVEN, no added rules.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (max-width: 767px) > .tlv-sp.tlv-sp { grid-template-columns: repeat(6, minmax(0px, 1fr)); } /   - removed: @media (max-width: 767px) > .tlv-sp.tlv-sp .tlv-sp-card.tlv-sp-card:nth-of-type(9) { grid-column: auto / span 2; } /   - removed: @media (max-width: 767px) > .tlv-sp.tlv-sp .tlv-sp-card.tlv-sp-card:nth-of-type(10) { grid-column: 3 / span 2; }**
- **Visual change if removed:** None.
- **Parts:** 3 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 193-193). Manual anchor: from `.tlv-sp.tlv-sp{grid-template-columns:repeat(6,minmax(0,1fr))}` to `.tlv-sp.tlv-sp{grid-template-columns:repeat(6,minmax(0,1fr))}`.
Delete:
```css
.tlv-sp.tlv-sp{grid-template-columns:repeat(6,minmax(0,1fr))}
```

**Part 2** (baseline lines 194-194). Manual anchor: from `.tlv-sp.tlv-sp .tlv-sp-card.tlv-sp-card:nth-of-type(9){grid-column:auto/span 2}` to `.tlv-sp.tlv-sp .tlv-sp-card.tlv-sp-card:nth-of-type(9){grid-column:auto/span 2}`.
Delete:
```css
.tlv-sp.tlv-sp .tlv-sp-card.tlv-sp-card:nth-of-type(9){grid-column:auto/span 2}
```

**Part 3** (baseline lines 195-195). Manual anchor: from `.tlv-sp.tlv-sp .tlv-sp-card.tlv-sp-card:nth-of-type(10){grid-column:3/span 2}` to `.tlv-sp.tlv-sp .tlv-sp-card.tlv-sp-card:nth-of-type(10){grid-column:3/span 2}`.
Delete:
```css
.tlv-sp.tlv-sp .tlv-sp-card.tlv-sp-card:nth-of-type(10){grid-column:3/span 2}
```

### T85 [TODO] 8 always-overridden rule(s) inside <style> blocks of snippets/cr-card-styles.liquid
- **File:** `snippets/cr-card-styles.liquid` | baseline lines 86-86, 87-87, 88-88, 89-89, 90-90, 94-94, 123-123, 125-125 | kind: always-overridden rules in inline CSS (same <style> block, tool-proven)
- **Why it is dead:** Each removed rule is restated later in the SAME <style> block by a rule with the same selectors, same or top-level @media, every property at equal-or-higher priority, so it can never win. Selectors: .cr-card__tag--building; .cr-card__tag--fidget; .cr-card__tag--keychain; .cr-card__tag--plush; .cr-card__tag--rc; .cr-card__tag.cr-card__tag.cr-card__tag.cr-card__tag.cr-card__tag.cr-card__tag.cr-card__tag.cr-card__tag; .soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot
- **Proof:** Automated scan of all 313 <style> blocks via the CSS view (identical line numbers). Only rules on lines of pure CSS (no HTML/Liquid) and without Liquid in the selector were considered; the winner had to be in the same <style> block and not inside a Liquid {% if/unless/case/for %}. Joint check with tools/cssom.js + tools/shadow.js on the views: all removed together -> PROVEN, no added rules.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .cr-card__tag--rc { border-color: rgb(220, 38, 38); color: rgb(220, 38, 38); } /   - removed: .cr-card__tag--building { border-color: rgb(234, 88, 12); color: rgb(234, 88, 12); } /   - removed: .cr-card__tag--keychain { border-color: rgb(22, 163, 74); color: rgb(22, 163, 74); } /   - removed: .cr-card__tag--plush { border-color: rgb(255, 66, 161); color: rgb(255, 66, 161); } /   - removed: .cr-card__tag--fidget { border-color: rgb(79, 110, 247); color: rgb(79, 110, 247); } /   - removed: .cr-card__tag--building { border-color: rgb(37, 99, 235); color: rgb(37, 99, 235); } /   - removed: .cr-card__tag.cr-card__tag.cr-card__tag.cr-card__tag.cr-card__tag.cr-card__tag.cr-card__tag.cr-card__tag { transition: right 0.26s cubic-bezier(0.4, 0, 1, 1) 0.12s !important; } /   - removed: .soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot { transition: right 0.26s cubic-bezier(0.4, 0, 1, 1) 0.12s !important; }**
- **Visual change if removed:** None.
- **Parts:** 8 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 86-86). Manual anchor: from `.cr-card__tag--rc { border-color: #dc2626; color: #dc2626; }` to `.cr-card__tag--rc { border-color: #dc2626; color: #dc2626; }`.
Delete:
```css
.cr-card__tag--rc { border-color: #dc2626; color: #dc2626; }
```

**Part 2** (baseline lines 87-87). Manual anchor: from `.cr-card__tag--building { border-color: #ea580c; color: #ea580c; }` to `.cr-card__tag--building { border-color: #ea580c; color: #ea580c; }`.
Delete:
```css
.cr-card__tag--building { border-color: #ea580c; color: #ea580c; }
```

**Part 3** (baseline lines 88-88). Manual anchor: from `.cr-card__tag--keychain { border-color: #16a34a; color: #16a34a; }` to `.cr-card__tag--keychain { border-color: #16a34a; color: #16a34a; }`.
Delete:
```css
.cr-card__tag--keychain { border-color: #16a34a; color: #16a34a; }
```

**Part 4** (baseline lines 89-89). Manual anchor: from `.cr-card__tag--plush { border-color: #ff42a1; color: #ff42a1; }` to `.cr-card__tag--plush { border-color: #ff42a1; color: #ff42a1; }`.
Delete:
```css
.cr-card__tag--plush { border-color: #ff42a1; color: #ff42a1; }
```

**Part 5** (baseline lines 90-90). Manual anchor: from `.cr-card__tag--fidget { border-color: #4f6ef7; color: #4f6ef7; }` to `.cr-card__tag--fidget { border-color: #4f6ef7; color: #4f6ef7; }`.
Delete:
```css
.cr-card__tag--fidget { border-color: #4f6ef7; color: #4f6ef7; }
```

**Part 6** (baseline lines 94-94). Manual anchor: from `.cr-card__tag--building{border-color:#2563eb;color:#2563eb}` to `.cr-card__tag--building{border-color:#2563eb;color:#2563eb}`.
Delete:
```css
.cr-card__tag--building{border-color:#2563eb;color:#2563eb}
```

**Part 7** (baseline lines 123-123). Manual anchor: from `.cr-card__tag.cr-card__tag.cr-card__tag.cr-card__tag.cr-card__tag.cr-card__tag.cr-card_...` to `.cr-card__tag.cr-card__tag.cr-card__tag.cr-card__tag.cr-card__tag.cr-card__tag.cr-card_...`.
Delete:
```css
.cr-card__tag.cr-card__tag.cr-card__tag.cr-card__tag.cr-card__tag.cr-card__tag.cr-card__tag.cr-card__tag{transition:right .26s cubic-bezier(.4,0,1,1) .12s!important}
```

**Part 8** (baseline lines 125-125). Manual anchor: from `.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot{trans...` to `.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot{trans...`.
Delete:
```css
.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot{transition:right .26s cubic-bezier(.4,0,1,1) .12s!important}
```

### T86 [TODO] 3 always-overridden rule(s) inside <style> blocks of snippets/product-card-styles.liquid
- **File:** `snippets/product-card-styles.liquid` | baseline lines 25-25, 54-54, 56-56 | kind: always-overridden rules in inline CSS (same <style> block, tool-proven)
- **Why it is dead:** Each removed rule is restated later in the SAME <style> block by a rule with the same selectors, same or top-level @media, every property at equal-or-higher priority, so it can never win. Selectors: .product-card__tag--building; .product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag; .soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot
- **Proof:** Automated scan of all 313 <style> blocks via the CSS view (identical line numbers). Only rules on lines of pure CSS (no HTML/Liquid) and without Liquid in the selector were considered; the winner had to be in the same <style> block and not inside a Liquid {% if/unless/case/for %}. Joint check with tools/cssom.js + tools/shadow.js on the views: all removed together -> PROVEN, no added rules.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .product-card__tag--building { border-color: rgb(37, 99, 235); color: rgb(37, 99, 235); } /   - removed: .product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag { transition: right 0.26s cubic-bezier(0.4, 0, 1, 1) 0.12s !important; } /   - removed: .soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot { transition: right 0.26s cubic-bezier(0.4, 0, 1, 1) 0.12s !important; }**
- **Visual change if removed:** None.
- **Parts:** 3 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 25-25). Manual anchor: from `.product-card__tag--building{border-color:#2563eb;color:#2563eb}` to `.product-card__tag--building{border-color:#2563eb;color:#2563eb}`.
Delete:
```css
.product-card__tag--building{border-color:#2563eb;color:#2563eb}
```

**Part 2** (baseline lines 54-54). Manual anchor: from `.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__...` to `.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__...`.
Delete:
```css
.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag{transition:right .26s cubic-bezier(.4,0,1,1) .12s!important}
```

**Part 3** (baseline lines 56-56). Manual anchor: from `.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot{trans...` to `.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot{trans...`.
Delete:
```css
.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot.soft-dot{transition:right .26s cubic-bezier(.4,0,1,1) .12s!important}
```

### T87 [TODO] 5 always-overridden rule(s) inside <style> blocks of snippets/product-recommendations.liquid
- **File:** `snippets/product-recommendations.liquid` | baseline lines 21-21, 22-22, 23-23, 24-24, 28-28 | kind: always-overridden rules in inline CSS (same <style> block, tool-proven)
- **Why it is dead:** Each removed rule is restated later in the SAME <style> block by a rule with the same selectors, same or top-level @media, every property at equal-or-higher priority, so it can never win. Selectors: #product-recs-grid .rec-card__tag--building; #product-recs-grid .rec-card__tag--fidget; #product-recs-grid .rec-card__tag--keychain; #product-recs-grid .rec-card__tag--plush
- **Proof:** Automated scan of all 313 <style> blocks via the CSS view (identical line numbers). Only rules on lines of pure CSS (no HTML/Liquid) and without Liquid in the selector were considered; the winner had to be in the same <style> block and not inside a Liquid {% if/unless/case/for %}. Joint check with tools/cssom.js + tools/shadow.js on the views: all removed together -> PROVEN, no added rules.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: #product-recs-grid .rec-card__tag--fidget { border-color: rgb(79, 110, 247) !important; color: rgb(79, 110, 247) !important; } /   - removed: #product-recs-grid .rec-card__tag--keychain { border-color: rgb(22, 163, 74) !important; color: rgb(22, 163, 74) !important; } /   - removed: #product-recs-grid .rec-card__tag--plush { border-color: rgb(255, 66, 161) !important; color: rgb(255, 66, 161) !important; } /   - removed: #product-recs-grid .rec-card__tag--building { border-color: rgb(234, 88, 12) !important; color: rgb(234, 88, 12) !important; } /   - removed: #product-recs-grid .rec-card__tag--building { border-color: rgb(37, 99, 235) !important; color: rgb(37, 99, 235) !important; }**
- **Visual change if removed:** None.
- **Parts:** 5 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 21-21). Manual anchor: from `#product-recs-grid .rec-card__tag--fidget { border-color:#4f6ef7 !important; color:#4f6...` to `#product-recs-grid .rec-card__tag--fidget { border-color:#4f6ef7 !important; color:#4f6...`.
Delete:
```css
#product-recs-grid .rec-card__tag--fidget { border-color:#4f6ef7 !important; color:#4f6ef7 !important; }
```

**Part 2** (baseline lines 22-22). Manual anchor: from `#product-recs-grid .rec-card__tag--keychain { border-color:#16a34a !important; color:#1...` to `#product-recs-grid .rec-card__tag--keychain { border-color:#16a34a !important; color:#1...`.
Delete:
```css
#product-recs-grid .rec-card__tag--keychain { border-color:#16a34a !important; color:#16a34a !important; }
```

**Part 3** (baseline lines 23-23). Manual anchor: from `#product-recs-grid .rec-card__tag--plush { border-color:#ff42a1 !important; color:#ff42...` to `#product-recs-grid .rec-card__tag--plush { border-color:#ff42a1 !important; color:#ff42...`.
Delete:
```css
#product-recs-grid .rec-card__tag--plush { border-color:#ff42a1 !important; color:#ff42a1 !important; }
```

**Part 4** (baseline lines 24-24). Manual anchor: from `#product-recs-grid .rec-card__tag--building { border-color:#ea580c !important; color:#e...` to `#product-recs-grid .rec-card__tag--building { border-color:#ea580c !important; color:#e...`.
Delete:
```css
#product-recs-grid .rec-card__tag--building { border-color:#ea580c !important; color:#ea580c !important; }
```

**Part 5** (baseline lines 28-28). Manual anchor: from `#product-recs-grid .rec-card__tag--building{border-color:#2563eb !important;color:#2563...` to `#product-recs-grid .rec-card__tag--building{border-color:#2563eb !important;color:#2563...`.
Delete:
```css
#product-recs-grid .rec-card__tag--building{border-color:#2563eb !important;color:#2563eb !important}
```

### T88 [TODO] 67 always-overridden rule(s) inside <style> blocks of snippets/tlv-orbs.liquid
- **File:** `snippets/tlv-orbs.liquid` | baseline lines 9-9, 30-30, 35-35, 36-36, 42-42, 43-43, 45-45, 47-47, 49-49, 52-52, 57-57, 58-58, 59-59, 60-60, 61-61, 62-62, 63-63, 65-65, 67-67, 88-88, 89-89, 90-90, 114-114, 118-118, 119-119, 125-125, 127-127, 131-131, 136-136, 144-144, 151-151, 158-158, 159-159, 162-162, 165-165, 166-166, 174-174, 187-187, 197-197, 198-198, 201-201, 204-204, 205-205, 209-209, 212-212, 213-213, 214-214, 215-215, 223-223, 224-224, 230-230, 231-231, 233-233, 234-234, 239-239, 240-240, 242-242, 243-243, 244-244, 258-258, 263-263, 265-265, 266-266, 272-272, 274-274, 275-275, 281-281 | kind: always-overridden rules in inline CSS (same <style> block, tool-proven)
- **Why it is dead:** Each removed rule is restated later in the SAME <style> block by a rule with the same selectors, same or top-level @media, every property at equal-or-higher priority, so it can never win. Selectors: .tlv-orb--has-subs .tlv-orb__subs span; .tlv-orb--has-subs .tlv-orb__subs span::before; .tlv-orb--has-subs .tlv-orb__subs span:nth-child(1); .tlv-orb--has-subs .tlv-orb__subs span:nth-child(1)::before; .tlv-orb--has-subs .tlv-orb__subs span:nth-child(2); .tlv-orb--has-subs .tlv-orb__subs span:nth-child(2)::before; .tlv-orb--has-subs .tlv-orb__subs span:nth-child(3); .tlv-orb--has-subs .tlv-orb__subs span:nth-child(3)::before; .tlv-orb--has-subs:hover .tlv-orb__subs span, .tlv-orb--has-subs:focus-within .tlv-orb__subs span; .tlv-orb--has-subs:hover .tlv-orb__wrap, .tlv-orb--has-subs:focus-within .tlv-orb__wrap; .tlv-orb:hover .tlv-orb__glow, .tlv-orb:focus-visible .tlv-orb__glow; .tlv-orb:hov
- **Proof:** Automated scan of all 313 <style> blocks via the CSS view (identical line numbers). Only rules on lines of pure CSS (no HTML/Liquid) and without Liquid in the selector were considered; the winner had to be in the same <style> block and not inside a Liquid {% if/unless/case/for %}. Joint check with tools/cssom.js + tools/shadow.js on the views: all removed together -> PROVEN, no added rules.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .tlv-orb__glow { display: none; } /   - removed: .tlv-orb--has-subs .tlv-orb__subs span { opacity: 0; transform: translate3d(-8px, 0px, 0px); transition: opacity 0.28s, transform 0.42s cubic-bezier(0.22, 0.8, 0.2, 1); } /   - removed: @media (hover: hover) > .tlv-orb--has-subs:hover .tlv-orb__wrap, .tlv-orb--has-subs:focus-within .tlv-orb__wrap { transform: translate3d(-34px, -3px, 0px); } /   - removed: @media (hover: hover) > .tlv-orb--has-subs:hover .tlv-orb__subs span, .tlv-orb--has-subs:focus-within .tlv-orb__subs span { opacity: 1; transform: translate3d(0px, 0px, 0px); } /   - removed: .tlv-orb--has-subs .tlv-orb__subs span::before { height: 1px; width: 34px; background: color-mix(in srgb,var(--c) 42%,#b7bec9); opacity: 0.55; } /   - removed: .tlv-orb--has-subs .tlv-orb__subs span:nth-child(1) { left: -92px; top: -70px; } /   - removed: .tlv-orb--has-subs .tlv-orb__subs span:nth-child(2) { left: 0px; top: 102px; } /   - removed: .tlv-orb--has-subs .tlv-orb__subs span:nth-child(3) { left: 92px; top: -70px; } /   - removed: .tlv-orb--has-subs .tlv-orb__subs span { min-width: 76px; padding: 0px; background: transparent; box-shadow: none; display: flex; flex-direction: column; align-items: center; gap: 5px; font-size: 10px; } /   - removed: .tlv-orb--has-subs .tlv-orb__subs span::before { left: 50%; top: 50%; width: 1px; height: 42px; background: color-mix(in srgb,var(--c) 42%,#b7bec9); } /   - removed: .tlv-orb--has-subs .tlv-orb__subs span::before { content: ""; position: absolute; z-index: -1; height: 1px; background: color-mix(in srgb,var(--c) 48%,#9aa3b5); transform-origin: left center; left: 50%; top: 50%; width: 36px; opacity: 0.7; } /   - removed: .tlv-orb--has-subs .tlv-orb__subs span:nth-child(1) { left: -82px; top: -62px; } /   - removed: .tlv-orb--has-subs .tlv-orb__subs span:nth-child(1)::before { transform: rotate(42deg); } /   - removed: .tlv-orb--has-subs .tlv-orb__subs span:nth-child(2) { left: 0px; top: 88px; } /   - removed: .tlv-orb--has-subs .tlv-orb__subs span:nth-child(2)::before { transform: rotate(-90deg); } /   - removed: .tlv-orb--has-subs .tlv-orb__subs span:nth-child(3) { left: 82px; top: -62px; } /   - removed: .tlv-orb--has-subs .tlv-orb__subs span:nth-child(3)::before { transform: rotate(138deg); } /   - removed: @media (hover: hover) > .tlv-orb--has-subs:hover .tlv-orb__wrap, .tlv-orb--has-subs:focus-within .tlv-orb__wrap { transform: translate3d(0px, 0px, 0px); } /   - removed: @media (hover: hover) > .tlv-orb--has-subs:hover .tlv-orb__subs span, .tlv-orb--has-subs:focus-within .tlv-orb__subs span { opacity: 1; transform: translate3d(-50%, -50%, 0px) scale(1); } /   - removed: .tlv-orb--has-subs .tlv-orb__subs span:nth-child(1)::before { transform: rotate(42deg) scaleX(0.15); } /   - removed: .tlv-orb--has-subs .tlv-orb__subs span:nth-child(2)::before { transform: rotate(-90deg) scaleX(0.15); } /   - removed: .tlv-orb--has-subs .tlv-orb__subs span:nth-child(3)::before { transform: rotate(138deg) scaleX(0.15); } /   - removed: .tlv-orb__glow::before { content: ""; position: absolute; left: 50%; top: -28px; width: 1px; height: 24px; border-left: 1px dotted color-mix(in srgb,var(--c) 62%,#aeb7c5); transform: translateX(-50%); opacity: 0; transition: opacity 0.2s 0.05s; } /   - removed: @media (hover: hover) > .tlv-orb:hover .tlv-orb__glow, .tlv-orb:focus-visible .tlv-orb__glow { opacity: 1; transform: translate(-50%, 0px) scale(1); } /   - removed: @media (hover: hover) > .tlv-orb:hover .tlv-orb__glow::before, .tlv-orb:focus-visible .tlv-orb__glow::before { opacity: 1; } /   - removed: .tlv-orb__glow::before { top: -92px !important; height: 88px !important; } /   - removed: @media (hover: hover) > .tlv-orb:hover .tlv-orb__glow::after, .tlv-orb:focus-visible .tlv-orb__glow::after { opacity: 0.82; transform: scale(1); } /   - removed: .tlv-orb__glow::before { display: none !important; } /   - removed: .tlv-orb__glow { top: calc(50% - 73px) !important; } /   - removed: .tlv-orb__wrap { width: clamp(64px, 19vw, 110px); flex: 0 0 auto; } /   - removed: .tlv-orb__glow { left: calc(50% + 57px) !important; top: calc(50% - 40px) !important; } /   - removed: .tlv-orb__wrap::before { transform: translateX(-50%) rotate(60deg) !important; transform-origin: center bottom !important; opacity: 0 !important; transition: opacity 0.25s !important; } /   - removed: .tlv-orb__wrap::after { transform: translateX(-50%) rotate(-60deg) !important; transform-origin: center bottom !important; opacity: 0 !important; transition: opacity 0.25s !important; } /   - removed: .tlv-orb__wrap::after { width: 2px !important; border: 0px !important; background: repeating-linear-gradient(to bottom,color-mix(in srgb,var(--c) 68%,#aeb7c5) 0 2px,transparent 2px 5px) !important; transform: translateX(-50%) rotate(-60deg) !important; transform-origin: center bottom !important; } /   - removed: .tlv-orb__wrap::before { transform: translateX(-50%) rotate(-120deg) !important; } /   - removed: .tlv-orb__wrap::after { transform: translateX(-50%) rotate(120deg) !important; } /   - removed: .tlv-orb__wrap::before, .tlv-orb__wrap::after { height: 86px !important; } /   - removed: @media (hover: hover) > .tlv-orb:hover .tlv-orb__glow, .tlv-orb:focus-visible .tlv-orb__glow { opacity: 1 !important; } /   - removed: @media (hover: hover) > .tlv-orb:hover .tlv-orb__glow::before, .tlv-orb:focus-visible .tlv-orb__glow::before, .tlv-orb:hover .tlv-orb__glow::after, .tlv-orb:focus-visible .tlv-orb__glow::after { opacity: 1 !important; } /   - removed: .tlv-orb__wrap::before, .tlv-orb__wrap::after { background: repeating-linear-gradient(to bottom,color-mix(in srgb,var(--c) 72%,#aeb7c5) 0 2px,transparent 2px 5px) !important; } /   - removed: .tlv-orb__glow::before { transition: opacity 0.25s 0.18s !important; } /   - removed: .tlv-orb__glow::after { transition: opacity 0.25s, transform 0.42s cubic-bezier(0.22, 0.8, 0.2, 1) !important; } /   - removed: .tlv-orb__wrap::before, .tlv-orb__wrap::after { transition: opacity 0.8s, transform 0.8s cubic-bezier(0.22, 0.8, 0.2, 1) !important; } /   - removed: .tlv-orb__glow::after { transition: opacity 0.3s 0.82s, transform 0.42s cubic-bezier(0.22, 0.8, 0.2, 1) 0.82s !important; } /   - removed: .tlv-orb__glow::before { transition: opacity 0.3s 1s !important; } /   - removed: .tlv-orb__glow::before { transition: opacity 0.3s 0.48s !important; } /   - removed: .tlv-orb__glow::before, .tlv-orb__glow::after { transition-delay: 0.48s !important; } /   - removed: .tlv-orb__wrap::before, .tlv-orb__wrap::after { transition: transform 0.8s linear, opacity 0.8s linear !important; } /   - removed: .tlv-orb__glow::before, .tlv-orb__glow::after { transition-delay: 0.85s !important; } /   - removed: .tlv-orb__glow { opacity: 0 !important; transition: opacity 0.3s 0.85s !important; } /   - removed: .tlv-orb__glow, .tlv-orb__glow::before, .tlv-orb__glow::after { transition: opacity 0.3s !important; } /   - removed: .tlv-orb__wrap::before, .tlv-orb__wrap::after { transition: opacity 0.8s 0.3s, transform 0.8s 0.3s !important; } /   - removed: .tlv-orb__glow { opacity: 0 !important; transition: opacity 0.25s 1.82s !important; } /   - removed: .tlv-orb__glow::before, .tlv-orb__glow::after { opacity: 0 !important; transition: opacity 0.25s 1.82s !important; } /   - removed: .tlv-orb__wrap::before, .tlv-orb__wrap::after { transform-origin: center top !important; opacity: 0 !important; } /   - removed: .tlv-orb__glow, .tlv-orb__glow::before, .tlv-orb__glow::after { opacity: 0 !important; transition: opacity 0.22s 1.86s !important; } /   - removed: @media (hover: hover) > .tlv-orb:hover .tlv-orb__wrap::before, .tlv-orb:focus-visible .tlv-orb__wrap::before { animation: 1.8s cubic-bezier(0.22, 0.8, 0.2, 1) 0s 1 normal both running tlv-arm-draw-right !important; } /   - removed: @media (hover: hover) > .tlv-orb:hover .tlv-orb__wrap::after, .tlv-orb:focus-visible .tlv-orb__wrap::after { animation: 1.8s cubic-bezier(0.22, 0.8, 0.2, 1) 0s 1 normal both running tlv-arm-draw-left !important; } /   - removed: @media (hover: hover) > .tlv-orb:hover .tlv-orb__glow, .tlv-orb:focus-visible .tlv-orb__glow, .tlv-orb:hover .tlv-orb__glow::before, .tlv-orb:focus-visible .tlv-orb__glow::before, .tlv-orb:hover .tlv-orb__glow::after, .tlv-orb:focus-visible .tlv-orb__glow::after { opacity: 1 !important; } /   - removed: .tlv-orb__glow, .tlv-orb__glow::before, .tlv-orb__glow::after { display: none !important; opacity: 0 !important; } /   - removed: .tlv-orb__wrap::before, .tlv-orb__wrap::after { clip-path: inset(0px 0px 100%) !important; opacity: 0 !important; } /   - removed: @media (hover: hover) > .tlv-orb:hover .tlv-orb__wrap::before, .tlv-orb:focus-visible .tlv-orb__wrap::before { animation: 1.15s cubic-bezier(0.22, 0.8, 0.2, 1) 0s 1 normal both running tlv-line-grow-right !important; } /   - removed: @media (hover: hover) > .tlv-orb:hover .tlv-orb__wrap::after, .tlv-orb:focus-visible .tlv-orb__wrap::after { animation: 1.15s cubic-bezier(0.22, 0.8, 0.2, 1) 0s 1 normal both running tlv-line-grow-left !important; } /   - removed: .tlv-orb__wrap::before, .tlv-orb__wrap::after { clip-path: none !important; height: 0px !important; opacity: 0 !important; } /   - removed: @media (hover: hover) > .tlv-orb:hover .tlv-orb__wrap::before, .tlv-orb:focus-visible .tlv-orb__wrap::before { animation: 1.15s cubic-bezier(0.22, 0.8, 0.2, 1) 0s 1 normal both running tlv-line-height-right !important; } /   - removed: @media (hover: hover) > .tlv-orb:hover .tlv-orb__wrap::after, .tlv-orb:focus-visible .tlv-orb__wrap::after { animation: 1.15s cubic-bezier(0.22, 0.8, 0.2, 1) 0s 1 normal both running tlv-line-height-left !important; } /   - removed: .tlv-orb__glow::before { transition-delay: 1.15s !important; }**
- **Visual change if removed:** None.
- **Parts:** 67 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 9-9). Manual anchor: from `.tlv-orb__glow{display:none}` to `.tlv-orb__glow{display:none}`.
Delete:
```css
.tlv-orb__glow{display:none}
```

**Part 2** (baseline lines 30-30). Manual anchor: from `.tlv-orb--has-subs .tlv-orb__subs span{opacity:0;transform:translate3d(-8px,0,0);transi...` to `.tlv-orb--has-subs .tlv-orb__subs span{opacity:0;transform:translate3d(-8px,0,0);transi...`.
Delete:
```css
.tlv-orb--has-subs .tlv-orb__subs span{opacity:0;transform:translate3d(-8px,0,0);transition:opacity .28s ease,transform .42s cubic-bezier(.22,.8,.2,1)}
```

**Part 3** (baseline lines 35-35). Manual anchor: from `.tlv-orb--has-subs:hover .tlv-orb__wrap,.tlv-orb--has-subs:focus-within .tlv-orb__wrap{...` to `.tlv-orb--has-subs:hover .tlv-orb__wrap,.tlv-orb--has-subs:focus-within .tlv-orb__wrap{...`.
Delete:
```css
  .tlv-orb--has-subs:hover .tlv-orb__wrap,.tlv-orb--has-subs:focus-within .tlv-orb__wrap{transform:translate3d(-34px,-3px,0)}
```

**Part 4** (baseline lines 36-36). Manual anchor: from `.tlv-orb--has-subs:hover .tlv-orb__subs span,.tlv-orb--has-subs:focus-within .tlv-orb__...` to `.tlv-orb--has-subs:hover .tlv-orb__subs span,.tlv-orb--has-subs:focus-within .tlv-orb__...`.
Delete:
```css
  .tlv-orb--has-subs:hover .tlv-orb__subs span,.tlv-orb--has-subs:focus-within .tlv-orb__subs span{opacity:1;transform:translate3d(0,0,0)}
```

**Part 5** (baseline lines 42-42). Manual anchor: from `.tlv-orb--has-subs .tlv-orb__subs span::before{height:1px;width:34px;background:color-m...` to `.tlv-orb--has-subs .tlv-orb__subs span::before{height:1px;width:34px;background:color-m...`.
Delete:
```css
.tlv-orb--has-subs .tlv-orb__subs span::before{height:1px;width:34px;background:color-mix(in srgb,var(--c) 42%,#b7bec9);opacity:.55}
```

**Part 6** (baseline lines 43-43). Manual anchor: from `.tlv-orb--has-subs .tlv-orb__subs span:nth-child(1){left:-92px;top:-70px}` to `.tlv-orb--has-subs .tlv-orb__subs span:nth-child(1){left:-92px;top:-70px}`.
Delete:
```css
.tlv-orb--has-subs .tlv-orb__subs span:nth-child(1){left:-92px;top:-70px}
```

**Part 7** (baseline lines 45-45). Manual anchor: from `.tlv-orb--has-subs .tlv-orb__subs span:nth-child(2){left:0;top:102px}` to `.tlv-orb--has-subs .tlv-orb__subs span:nth-child(2){left:0;top:102px}`.
Delete:
```css
.tlv-orb--has-subs .tlv-orb__subs span:nth-child(2){left:0;top:102px}
```

**Part 8** (baseline lines 47-47). Manual anchor: from `.tlv-orb--has-subs .tlv-orb__subs span:nth-child(3){left:92px;top:-70px}` to `.tlv-orb--has-subs .tlv-orb__subs span:nth-child(3){left:92px;top:-70px}`.
Delete:
```css
.tlv-orb--has-subs .tlv-orb__subs span:nth-child(3){left:92px;top:-70px}
```

**Part 9** (baseline lines 49-49). Manual anchor: from `.tlv-orb--has-subs .tlv-orb__subs span{min-width:76px;padding:0;background:transparent;...` to `.tlv-orb--has-subs .tlv-orb__subs span{min-width:76px;padding:0;background:transparent;...`.
Delete:
```css
.tlv-orb--has-subs .tlv-orb__subs span{min-width:76px;padding:0;background:transparent;box-shadow:none;display:flex;flex-direction:column;align-items:center;gap:5px;font-size:10px}
```

**Part 10** (baseline lines 52-52). Manual anchor: from `.tlv-orb--has-subs .tlv-orb__subs span::before{left:50%;top:50%;width:1px;height:42px;b...` to `.tlv-orb--has-subs .tlv-orb__subs span::before{left:50%;top:50%;width:1px;height:42px;b...`.
Delete:
```css
.tlv-orb--has-subs .tlv-orb__subs span::before{left:50%;top:50%;width:1px;height:42px;background:color-mix(in srgb,var(--c) 42%,#b7bec9)}
```

**Part 11** (baseline lines 57-57). Manual anchor: from `.tlv-orb--has-subs .tlv-orb__subs span::before{content:"";position:absolute;z-index:-1;...` to `.tlv-orb--has-subs .tlv-orb__subs span::before{content:"";position:absolute;z-index:-1;...`.
Delete:
```css
.tlv-orb--has-subs .tlv-orb__subs span::before{content:"";position:absolute;z-index:-1;height:1px;background:color-mix(in srgb,var(--c) 48%,#9aa3b5);transform-origin:left center;left:50%;top:50%;width:36px;opacity:.7}
```

**Part 12** (baseline lines 58-58). Manual anchor: from `.tlv-orb--has-subs .tlv-orb__subs span:nth-child(1){left:-82px;top:-62px}` to `.tlv-orb--has-subs .tlv-orb__subs span:nth-child(1){left:-82px;top:-62px}`.
Delete:
```css
.tlv-orb--has-subs .tlv-orb__subs span:nth-child(1){left:-82px;top:-62px}
```

**Part 13** (baseline lines 59-59). Manual anchor: from `.tlv-orb--has-subs .tlv-orb__subs span:nth-child(1)::before{transform:rotate(42deg)}` to `.tlv-orb--has-subs .tlv-orb__subs span:nth-child(1)::before{transform:rotate(42deg)}`.
Delete:
```css
.tlv-orb--has-subs .tlv-orb__subs span:nth-child(1)::before{transform:rotate(42deg)}
```

**Part 14** (baseline lines 60-60). Manual anchor: from `.tlv-orb--has-subs .tlv-orb__subs span:nth-child(2){left:0;top:88px}` to `.tlv-orb--has-subs .tlv-orb__subs span:nth-child(2){left:0;top:88px}`.
Delete:
```css
.tlv-orb--has-subs .tlv-orb__subs span:nth-child(2){left:0;top:88px}
```

**Part 15** (baseline lines 61-61). Manual anchor: from `.tlv-orb--has-subs .tlv-orb__subs span:nth-child(2)::before{transform:rotate(-90deg)}` to `.tlv-orb--has-subs .tlv-orb__subs span:nth-child(2)::before{transform:rotate(-90deg)}`.
Delete:
```css
.tlv-orb--has-subs .tlv-orb__subs span:nth-child(2)::before{transform:rotate(-90deg)}
```

**Part 16** (baseline lines 62-62). Manual anchor: from `.tlv-orb--has-subs .tlv-orb__subs span:nth-child(3){left:82px;top:-62px}` to `.tlv-orb--has-subs .tlv-orb__subs span:nth-child(3){left:82px;top:-62px}`.
Delete:
```css
.tlv-orb--has-subs .tlv-orb__subs span:nth-child(3){left:82px;top:-62px}
```

**Part 17** (baseline lines 63-63). Manual anchor: from `.tlv-orb--has-subs .tlv-orb__subs span:nth-child(3)::before{transform:rotate(138deg)}` to `.tlv-orb--has-subs .tlv-orb__subs span:nth-child(3)::before{transform:rotate(138deg)}`.
Delete:
```css
.tlv-orb--has-subs .tlv-orb__subs span:nth-child(3)::before{transform:rotate(138deg)}
```

**Part 18** (baseline lines 65-65). Manual anchor: from `.tlv-orb--has-subs:hover .tlv-orb__wrap,.tlv-orb--has-subs:focus-within .tlv-orb__wrap{...` to `.tlv-orb--has-subs:hover .tlv-orb__wrap,.tlv-orb--has-subs:focus-within .tlv-orb__wrap{...`.
Delete:
```css
 .tlv-orb--has-subs:hover .tlv-orb__wrap,.tlv-orb--has-subs:focus-within .tlv-orb__wrap{transform:translate3d(0,0,0)}
```

**Part 19** (baseline lines 67-67). Manual anchor: from `.tlv-orb--has-subs:hover .tlv-orb__subs span,.tlv-orb--has-subs:focus-within .tlv-orb__...` to `.tlv-orb--has-subs:hover .tlv-orb__subs span,.tlv-orb--has-subs:focus-within .tlv-orb__...`.
Delete:
```css
 .tlv-orb--has-subs:hover .tlv-orb__subs span,.tlv-orb--has-subs:focus-within .tlv-orb__subs span{opacity:1;transform:translate3d(-50%,-50%,0) scale(1)}
```

**Part 20** (baseline lines 88-88). Manual anchor: from `.tlv-orb--has-subs .tlv-orb__subs span:nth-child(1)::before{transform:rotate(42deg) sca...` to `.tlv-orb--has-subs .tlv-orb__subs span:nth-child(1)::before{transform:rotate(42deg) sca...`.
Delete:
```css
.tlv-orb--has-subs .tlv-orb__subs span:nth-child(1)::before{transform:rotate(42deg) scaleX(.15)}
```

**Part 21** (baseline lines 89-89). Manual anchor: from `.tlv-orb--has-subs .tlv-orb__subs span:nth-child(2)::before{transform:rotate(-90deg) sc...` to `.tlv-orb--has-subs .tlv-orb__subs span:nth-child(2)::before{transform:rotate(-90deg) sc...`.
Delete:
```css
.tlv-orb--has-subs .tlv-orb__subs span:nth-child(2)::before{transform:rotate(-90deg) scaleX(.15)}
```

**Part 22** (baseline lines 90-90). Manual anchor: from `.tlv-orb--has-subs .tlv-orb__subs span:nth-child(3)::before{transform:rotate(138deg) sc...` to `.tlv-orb--has-subs .tlv-orb__subs span:nth-child(3)::before{transform:rotate(138deg) sc...`.
Delete:
```css
.tlv-orb--has-subs .tlv-orb__subs span:nth-child(3)::before{transform:rotate(138deg) scaleX(.15)}
```

**Part 23** (baseline lines 114-114). Manual anchor: from `.tlv-orb__glow::before{content:"";position:absolute;left:50%;top:-28px;width:1px;height...` to `.tlv-orb__glow::before{content:"";position:absolute;left:50%;top:-28px;width:1px;height...`.
Delete:
```css
.tlv-orb__glow::before{content:"";position:absolute;left:50%;top:-28px;width:1px;height:24px;border-left:1px dotted color-mix(in srgb,var(--c) 62%,#aeb7c5);transform:translateX(-50%);opacity:0;transition:opacity .2s ease .05s}
```

**Part 24** (baseline lines 118-118). Manual anchor: from `.tlv-orb:hover .tlv-orb__glow,.tlv-orb:focus-visible .tlv-orb__glow{opacity:1;transform...` to `.tlv-orb:hover .tlv-orb__glow,.tlv-orb:focus-visible .tlv-orb__glow{opacity:1;transform...`.
Delete:
```css
 .tlv-orb:hover .tlv-orb__glow,.tlv-orb:focus-visible .tlv-orb__glow{opacity:1;transform:translate(-50%,0) scale(1)}
```

**Part 25** (baseline lines 119-119). Manual anchor: from `.tlv-orb:hover .tlv-orb__glow::before,.tlv-orb:focus-visible .tlv-orb__glow::before{opa...` to `.tlv-orb:hover .tlv-orb__glow::before,.tlv-orb:focus-visible .tlv-orb__glow::before{opa...`.
Delete:
```css
 .tlv-orb:hover .tlv-orb__glow::before,.tlv-orb:focus-visible .tlv-orb__glow::before{opacity:1}
```

**Part 26** (baseline lines 125-125). Manual anchor: from `.tlv-orb__glow::before{top:-92px!important;height:88px!important}` to `.tlv-orb__glow::before{top:-92px!important;height:88px!important}`.
Delete:
```css
.tlv-orb__glow::before{top:-92px!important;height:88px!important}
```

**Part 27** (baseline lines 127-127). Manual anchor: from `.tlv-orb:hover .tlv-orb__glow::after,.tlv-orb:focus-visible .tlv-orb__glow::after{opaci...` to `.tlv-orb:hover .tlv-orb__glow::after,.tlv-orb:focus-visible .tlv-orb__glow::after{opaci...`.
Delete:
```css
 .tlv-orb:hover .tlv-orb__glow::after,.tlv-orb:focus-visible .tlv-orb__glow::after{opacity:.82;transform:scale(1)}
```

**Part 28** (baseline lines 131-131). Manual anchor: from `.tlv-orb__glow::before{display:none!important}` to `.tlv-orb__glow::before{display:none!important}`.
Delete:
```css
.tlv-orb__glow::before{display:none!important}
```

**Part 29** (baseline lines 136-136). Manual anchor: from `.tlv-orb__glow{top:calc(50% - 73px)!important}` to `.tlv-orb__glow{top:calc(50% - 73px)!important}`.
Delete:
```css
.tlv-orb__glow{top:calc(50% - 73px)!important}
```

**Part 30** (baseline lines 144-144). Manual anchor: from `.tlv-orb__wrap{width:clamp(64px,19vw,110px);flex:0 0 auto}` to `.tlv-orb__wrap{width:clamp(64px,19vw,110px);flex:0 0 auto}`.
Delete:
```css
.tlv-orb__wrap{width:clamp(64px,19vw,110px);flex:0 0 auto}
```

**Part 31** (baseline lines 151-151). Manual anchor: from `.tlv-orb__glow{left:calc(50% + 57px)!important;top:calc(50% - 40px)!important}` to `.tlv-orb__glow{left:calc(50% + 57px)!important;top:calc(50% - 40px)!important}`.
Delete:
```css
.tlv-orb__glow{left:calc(50% + 57px)!important;top:calc(50% - 40px)!important}
```

**Part 32** (baseline lines 158-158). Manual anchor: from `.tlv-orb__wrap::before{transform:translateX(-50%) rotate(60deg)!important;transform-ori...` to `.tlv-orb__wrap::before{transform:translateX(-50%) rotate(60deg)!important;transform-ori...`.
Delete:
```css
.tlv-orb__wrap::before{transform:translateX(-50%) rotate(60deg)!important;transform-origin:bottom center!important;opacity:0!important;transition:opacity .25s ease!important}
```

**Part 33** (baseline lines 159-159). Manual anchor: from `.tlv-orb__wrap::after{transform:translateX(-50%) rotate(-60deg)!important;transform-ori...` to `.tlv-orb__wrap::after{transform:translateX(-50%) rotate(-60deg)!important;transform-ori...`.
Delete:
```css
.tlv-orb__wrap::after{transform:translateX(-50%) rotate(-60deg)!important;transform-origin:bottom center!important;opacity:0!important;transition:opacity .25s ease!important}
```

**Part 34** (baseline lines 162-162). Manual anchor: from `.tlv-orb__wrap::after{width:2px!important;border:0!important;background:repeating-linea...` to `.tlv-orb__wrap::after{width:2px!important;border:0!important;background:repeating-linea...`.
Delete:
```css
.tlv-orb__wrap::after{width:2px!important;border:0!important;background:repeating-linear-gradient(to bottom,color-mix(in srgb,var(--c) 68%,#aeb7c5) 0 2px,transparent 2px 5px)!important;transform:translateX(-50%) rotate(-60deg)!important;transform-origin:bottom center!important}
```

**Part 35** (baseline lines 165-165). Manual anchor: from `.tlv-orb__wrap::before{transform:translateX(-50%) rotate(-120deg)!important}` to `.tlv-orb__wrap::before{transform:translateX(-50%) rotate(-120deg)!important}`.
Delete:
```css
.tlv-orb__wrap::before{transform:translateX(-50%) rotate(-120deg)!important}
```

**Part 36** (baseline lines 166-166). Manual anchor: from `.tlv-orb__wrap::after{transform:translateX(-50%) rotate(120deg)!important}` to `.tlv-orb__wrap::after{transform:translateX(-50%) rotate(120deg)!important}`.
Delete:
```css
.tlv-orb__wrap::after{transform:translateX(-50%) rotate(120deg)!important}
```

**Part 37** (baseline lines 174-174). Manual anchor: from `.tlv-orb__wrap::before,.tlv-orb__wrap::after{height:86px!important}` to `.tlv-orb__wrap::before,.tlv-orb__wrap::after{height:86px!important}`.
Delete:
```css
.tlv-orb__wrap::before,.tlv-orb__wrap::after{height:86px!important}
```

**Part 38** (baseline lines 187-187). Manual anchor: from `.tlv-orb__wrap::before,.tlv-orb__wrap::after{background:repeating-linear-gradient(to bo...` to `.tlv-orb__wrap::before,.tlv-orb__wrap::after{background:repeating-linear-gradient(to bo...`.
Delete:
```css
.tlv-orb__wrap::before,.tlv-orb__wrap::after{background:repeating-linear-gradient(to bottom,color-mix(in srgb,var(--c) 72%,#aeb7c5) 0 2px,transparent 2px 5px)!important}
```

**Part 39** (baseline lines 197-197). Manual anchor: from `.tlv-orb__glow::before{transition:opacity .25s ease .18s!important}` to `.tlv-orb__glow::before{transition:opacity .25s ease .18s!important}`.
Delete:
```css
.tlv-orb__glow::before{transition:opacity .25s ease .18s!important}
```

**Part 40** (baseline lines 198-198). Manual anchor: from `.tlv-orb__glow::after{transition:opacity .25s ease 0s,transform .42s cubic-bezier(.22,....` to `.tlv-orb__glow::after{transition:opacity .25s ease 0s,transform .42s cubic-bezier(.22,....`.
Delete:
```css
.tlv-orb__glow::after{transition:opacity .25s ease 0s,transform .42s cubic-bezier(.22,.8,.2,1) 0s!important}
```

**Part 41** (baseline lines 201-201). Manual anchor: from `.tlv-orb__wrap::before,.tlv-orb__wrap::after{transition:opacity .8s ease,transform .8s ...` to `.tlv-orb__wrap::before,.tlv-orb__wrap::after{transition:opacity .8s ease,transform .8s ...`.
Delete:
```css
.tlv-orb__wrap::before,.tlv-orb__wrap::after{transition:opacity .8s ease,transform .8s cubic-bezier(.22,.8,.2,1)!important}
```

**Part 42** (baseline lines 204-204). Manual anchor: from `.tlv-orb__glow::after{transition:opacity .3s ease .82s,transform .42s cubic-bezier(.22,...` to `.tlv-orb__glow::after{transition:opacity .3s ease .82s,transform .42s cubic-bezier(.22,...`.
Delete:
```css
.tlv-orb__glow::after{transition:opacity .3s ease .82s,transform .42s cubic-bezier(.22,.8,.2,1) .82s!important}
```

**Part 43** (baseline lines 205-205). Manual anchor: from `.tlv-orb__glow::before{transition:opacity .3s ease 1s!important}` to `.tlv-orb__glow::before{transition:opacity .3s ease 1s!important}`.
Delete:
```css
.tlv-orb__glow::before{transition:opacity .3s ease 1s!important}
```

**Part 44** (baseline lines 209-209). Manual anchor: from `.tlv-orb__glow::before{transition:opacity .3s ease .48s!important}` to `.tlv-orb__glow::before{transition:opacity .3s ease .48s!important}`.
Delete:
```css
.tlv-orb__glow::before{transition:opacity .3s ease .48s!important}
```

**Part 45** (baseline lines 212-212). Manual anchor: from `.tlv-orb__glow::before,.tlv-orb__glow::after{transition-delay:.48s!important}` to `.tlv-orb__glow::before,.tlv-orb__glow::after{transition-delay:.48s!important}`.
Delete:
```css
.tlv-orb__glow::before,.tlv-orb__glow::after{transition-delay:.48s!important}
```

**Part 46** (baseline lines 213-213). Manual anchor: from `.tlv-orb__wrap::before,.tlv-orb__wrap::after{transition:transform .8s linear,opacity .8...` to `.tlv-orb__wrap::before,.tlv-orb__wrap::after{transition:transform .8s linear,opacity .8...`.
Delete:
```css
.tlv-orb__wrap::before,.tlv-orb__wrap::after{transition:transform .8s linear,opacity .8s linear!important;transition-delay:0s!important}
```

**Part 47** (baseline lines 214-214). Manual anchor: from `.tlv-orb__glow::before,.tlv-orb__glow::after{transition-delay:.85s!important}` to `.tlv-orb__glow::before,.tlv-orb__glow::after{transition-delay:.85s!important}`.
Delete:
```css
.tlv-orb__glow::before,.tlv-orb__glow::after{transition-delay:.85s!important}
```

**Part 48** (baseline lines 215-215). Manual anchor: from `.tlv-orb__glow{opacity:0!important;transition:opacity .3s ease .85s!important}` to `.tlv-orb__glow{opacity:0!important;transition:opacity .3s ease .85s!important}`.
Delete:
```css
.tlv-orb__glow{opacity:0!important;transition:opacity .3s ease .85s!important}
```

**Part 49** (baseline lines 223-223). Manual anchor: from `.tlv-orb__glow,.tlv-orb__glow::before,.tlv-orb__glow::after{transition:opacity .3s ease...` to `.tlv-orb__glow,.tlv-orb__glow::before,.tlv-orb__glow::after{transition:opacity .3s ease...`.
Delete:
```css
.tlv-orb__glow,.tlv-orb__glow::before,.tlv-orb__glow::after{transition:opacity .3s ease 0s!important}
```

**Part 50** (baseline lines 224-224). Manual anchor: from `.tlv-orb__wrap::before,.tlv-orb__wrap::after{transition:opacity .8s ease .3s,transform ...` to `.tlv-orb__wrap::before,.tlv-orb__wrap::after{transition:opacity .8s ease .3s,transform ...`.
Delete:
```css
.tlv-orb__wrap::before,.tlv-orb__wrap::after{transition:opacity .8s ease .3s,transform .8s ease .3s!important}
```

**Part 51** (baseline lines 230-230). Manual anchor: from `.tlv-orb__glow{opacity:0!important;transition:opacity .25s ease 1.82s!important}` to `.tlv-orb__glow{opacity:0!important;transition:opacity .25s ease 1.82s!important}`.
Delete:
```css
.tlv-orb__glow{opacity:0!important;transition:opacity .25s ease 1.82s!important}
```

**Part 52** (baseline lines 231-231). Manual anchor: from `.tlv-orb__glow::before,.tlv-orb__glow::after{opacity:0!important;transition:opacity .25...` to `.tlv-orb__glow::before,.tlv-orb__glow::after{opacity:0!important;transition:opacity .25...`.
Delete:
```css
.tlv-orb__glow::before,.tlv-orb__glow::after{opacity:0!important;transition:opacity .25s ease 1.82s!important}
```

**Part 53** (baseline lines 233-233). Manual anchor: from `.tlv-orb:hover .tlv-orb__glow,.tlv-orb:focus-visible .tlv-orb__glow{opacity:1!important}` to `.tlv-orb:hover .tlv-orb__glow,.tlv-orb:focus-visible .tlv-orb__glow{opacity:1!important}`.
Delete:
```css
 .tlv-orb:hover .tlv-orb__glow,.tlv-orb:focus-visible .tlv-orb__glow{opacity:1!important}
```

**Part 54** (baseline lines 234-234). Manual anchor: from `.tlv-orb:hover .tlv-orb__glow::before,.tlv-orb:focus-visible .tlv-orb__glow::before,.tl...` to `.tlv-orb:hover .tlv-orb__glow::before,.tlv-orb:focus-visible .tlv-orb__glow::before,.tl...`.
Delete:
```css
 .tlv-orb:hover .tlv-orb__glow::before,.tlv-orb:focus-visible .tlv-orb__glow::before,.tlv-orb:hover .tlv-orb__glow::after,.tlv-orb:focus-visible .tlv-orb__glow::after{opacity:1!important}
```

**Part 55** (baseline lines 239-239). Manual anchor: from `.tlv-orb__wrap::before,.tlv-orb__wrap::after{transform-origin:top center!important;opac...` to `.tlv-orb__wrap::before,.tlv-orb__wrap::after{transform-origin:top center!important;opac...`.
Delete:
```css
.tlv-orb__wrap::before,.tlv-orb__wrap::after{transform-origin:top center!important;opacity:0!important}
```

**Part 56** (baseline lines 240-240). Manual anchor: from `.tlv-orb__glow,.tlv-orb__glow::before,.tlv-orb__glow::after{opacity:0!important;transit...` to `.tlv-orb__glow,.tlv-orb__glow::before,.tlv-orb__glow::after{opacity:0!important;transit...`.
Delete:
```css
.tlv-orb__glow,.tlv-orb__glow::before,.tlv-orb__glow::after{opacity:0!important;transition:opacity .22s ease 1.86s!important}
```

**Part 57** (baseline lines 242-242). Manual anchor: from `.tlv-orb:hover .tlv-orb__wrap::before,.tlv-orb:focus-visible .tlv-orb__wrap::before{ani...` to `.tlv-orb:hover .tlv-orb__wrap::before,.tlv-orb:focus-visible .tlv-orb__wrap::before{ani...`.
Delete:
```css
 .tlv-orb:hover .tlv-orb__wrap::before,.tlv-orb:focus-visible .tlv-orb__wrap::before{animation:tlv-arm-draw-right 1.8s cubic-bezier(.22,.8,.2,1) both!important}
```

**Part 58** (baseline lines 243-243). Manual anchor: from `.tlv-orb:hover .tlv-orb__wrap::after,.tlv-orb:focus-visible .tlv-orb__wrap::after{anima...` to `.tlv-orb:hover .tlv-orb__wrap::after,.tlv-orb:focus-visible .tlv-orb__wrap::after{anima...`.
Delete:
```css
 .tlv-orb:hover .tlv-orb__wrap::after,.tlv-orb:focus-visible .tlv-orb__wrap::after{animation:tlv-arm-draw-left 1.8s cubic-bezier(.22,.8,.2,1) both!important}
```

**Part 59** (baseline lines 244-244). Manual anchor: from `.tlv-orb:hover .tlv-orb__glow,.tlv-orb:focus-visible .tlv-orb__glow,.tlv-orb:hover .tlv...` to `.tlv-orb:hover .tlv-orb__glow,.tlv-orb:focus-visible .tlv-orb__glow,.tlv-orb:hover .tlv...`.
Delete:
```css
 .tlv-orb:hover .tlv-orb__glow,.tlv-orb:focus-visible .tlv-orb__glow,.tlv-orb:hover .tlv-orb__glow::before,.tlv-orb:focus-visible .tlv-orb__glow::before,.tlv-orb:hover .tlv-orb__glow::after,.tlv-orb:focus-visible .tlv-orb__glow::after{opacity:1!important}
```

**Part 60** (baseline lines 258-258). Manual anchor: from `.tlv-orb__glow,.tlv-orb__glow::before,.tlv-orb__glow::after{display:none!important;opac...` to `.tlv-orb__glow,.tlv-orb__glow::before,.tlv-orb__glow::after{display:none!important;opac...`.
Delete:
```css
.tlv-orb__glow,.tlv-orb__glow::before,.tlv-orb__glow::after{display:none!important;opacity:0!important}
```

**Part 61** (baseline lines 263-263). Manual anchor: from `.tlv-orb__wrap::before,.tlv-orb__wrap::after{clip-path:inset(0 0 100% 0)!important;opac...` to `.tlv-orb__wrap::before,.tlv-orb__wrap::after{clip-path:inset(0 0 100% 0)!important;opac...`.
Delete:
```css
.tlv-orb__wrap::before,.tlv-orb__wrap::after{clip-path:inset(0 0 100% 0)!important;opacity:0!important}
```

**Part 62** (baseline lines 265-265). Manual anchor: from `.tlv-orb:hover .tlv-orb__wrap::before,.tlv-orb:focus-visible .tlv-orb__wrap::before{ani...` to `.tlv-orb:hover .tlv-orb__wrap::before,.tlv-orb:focus-visible .tlv-orb__wrap::before{ani...`.
Delete:
```css
 .tlv-orb:hover .tlv-orb__wrap::before,.tlv-orb:focus-visible .tlv-orb__wrap::before{animation:tlv-line-grow-right 1.15s cubic-bezier(.22,.8,.2,1) both!important}
```

**Part 63** (baseline lines 266-266). Manual anchor: from `.tlv-orb:hover .tlv-orb__wrap::after,.tlv-orb:focus-visible .tlv-orb__wrap::after{anima...` to `.tlv-orb:hover .tlv-orb__wrap::after,.tlv-orb:focus-visible .tlv-orb__wrap::after{anima...`.
Delete:
```css
 .tlv-orb:hover .tlv-orb__wrap::after,.tlv-orb:focus-visible .tlv-orb__wrap::after{animation:tlv-line-grow-left 1.15s cubic-bezier(.22,.8,.2,1) both!important}
```

**Part 64** (baseline lines 272-272). Manual anchor: from `.tlv-orb__wrap::before,.tlv-orb__wrap::after{clip-path:none!important;height:0!importan...` to `.tlv-orb__wrap::before,.tlv-orb__wrap::after{clip-path:none!important;height:0!importan...`.
Delete:
```css
.tlv-orb__wrap::before,.tlv-orb__wrap::after{clip-path:none!important;height:0!important;opacity:0!important}
```

**Part 65** (baseline lines 274-274). Manual anchor: from `.tlv-orb:hover .tlv-orb__wrap::before,.tlv-orb:focus-visible .tlv-orb__wrap::before{ani...` to `.tlv-orb:hover .tlv-orb__wrap::before,.tlv-orb:focus-visible .tlv-orb__wrap::before{ani...`.
Delete:
```css
 .tlv-orb:hover .tlv-orb__wrap::before,.tlv-orb:focus-visible .tlv-orb__wrap::before{animation:tlv-line-height-right 1.15s cubic-bezier(.22,.8,.2,1) both!important}
```

**Part 66** (baseline lines 275-275). Manual anchor: from `.tlv-orb:hover .tlv-orb__wrap::after,.tlv-orb:focus-visible .tlv-orb__wrap::after{anima...` to `.tlv-orb:hover .tlv-orb__wrap::after,.tlv-orb:focus-visible .tlv-orb__wrap::after{anima...`.
Delete:
```css
 .tlv-orb:hover .tlv-orb__wrap::after,.tlv-orb:focus-visible .tlv-orb__wrap::after{animation:tlv-line-height-left 1.15s cubic-bezier(.22,.8,.2,1) both!important}
```

**Part 67** (baseline lines 281-281). Manual anchor: from `.tlv-orb__glow::before{transition-delay:1.15s!important}` to `.tlv-orb__glow::before{transition-delay:1.15s!important}`.
Delete:
```css
.tlv-orb__glow::before{transition-delay:1.15s!important}
```

### T89 [REVIEW] 9 orphaned rule(s) inside <style> blocks of layout/theme.liquid (classes no markup or script uses)
- **File:** `layout/theme.liquid` | baseline lines 1339-1339, 1343-1343, 1347-1347, 1403-1403, 1419-1419, 1717-1717, 1721-1721, 1729-1729, 1733-1733 | kind: orphan selectors in inline CSS (scripted, conservative)
- **Why it is dead:** Every selector of each rule needs a class or ID that appears nowhere in the theme outside CSS: not in any HTML/Liquid markup, JS file, inline script or JSON (any mention, even in a string, counts as used; prefix-built names like x--{{ }} count as used; Shopify/app prefixes count as used; classes inside :not()/:is()/:where()/:has() are ignored). Selectors: .product-card--cyan:hover; .product-card--pink:hover; .product-card--yellow:hover; .tlv-sb-logo-letter; .tlv-sb-social-icon; .tlv-sb-social-icon svg; .tlv-sb-social-icon:active; .tlv-sb-social-icon:active svg; .tlv-sb-socials
- **Proof:** Scripted full-text search over all 119 theme files with <style> CSS removed. Only rules on lines of pure CSS without Liquid were considered. Joint Chrome check per file (CSS views): exactly these rules removed, nothing added. Not proven from CSS alone (an app or admin content could use a class), hence REVIEW.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .product-card--cyan:hover { outline-color: rgba(33, 213, 237, 0.7); } /   - removed: .product-card--pink:hover { outline-color: transparent; } /   - removed: .product-card--yellow:hover { outline-color: rgba(255, 216, 61, 0.7); } /   - removed: .tlv-sb-socials { display: none; } /   - removed: .tlv-sb-logo-letter { font-size: 1.15rem; font-weight: 900; color: rgb(255, 66, 161); font-family: Nunito, sans-serif; line-height: 1; } /   - removed: .tlv-sb-social-icon { width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; border-radius: 50%; border: 1px solid rgba(255, 66, 161, 0.35); background: transparent; cursor: pointer; text-decoration: none; -webkit-tap-highlight-color: transparent; flex-shrink: 0; tra /   - removed: .tlv-sb-social-icon svg { width: 16px; height: 16px; fill: none; stroke: rgb(255, 66, 161); stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; display: block; } /   - removed: .tlv-sb-social-icon:active { background: rgb(255, 66, 161); border-color: rgb(255, 66, 161); } /   - removed: .tlv-sb-social-icon:active svg { stroke: rgb(255, 255, 255); }**
- **Visual change if removed:** None expected.
- **Parts:** 9 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 1339-1339). Manual anchor: from `.product-card--cyan:hover { outline-color: hsla(187,85%,53%,0.7); }` to `.product-card--cyan:hover { outline-color: hsla(187,85%,53%,0.7); }`.
Delete:
```css
.product-card--cyan:hover { outline-color: hsla(187,85%,53%,0.7); }
```

**Part 2** (baseline lines 1343-1343). Manual anchor: from `.product-card--pink:hover { outline-color: transparent; }` to `.product-card--pink:hover { outline-color: transparent; }`.
Delete:
```css
.product-card--pink:hover { outline-color: transparent; }
```

**Part 3** (baseline lines 1347-1347). Manual anchor: from `.product-card--yellow:hover { outline-color: hsla(48,100%,62%,0.7); }` to `.product-card--yellow:hover { outline-color: hsla(48,100%,62%,0.7); }`.
Delete:
```css
.product-card--yellow:hover { outline-color: hsla(48,100%,62%,0.7); }
```

**Part 4** (baseline lines 1403-1403). Manual anchor: from `.tlv-sb-socials{display:none;}` to `.tlv-sb-socials{display:none;}`.
Delete:
```css
.tlv-sb-socials{display:none;}
```

**Part 5** (baseline lines 1419-1419). Manual anchor: from `.tlv-sb-logo-letter{font-size:1.15rem;font-weight:900;color:#ff42a1;font-family:'Nunito...` to `.tlv-sb-logo-letter{font-size:1.15rem;font-weight:900;color:#ff42a1;font-family:'Nunito...`.
Delete:
```css
.tlv-sb-logo-letter{font-size:1.15rem;font-weight:900;color:#ff42a1;font-family:'Nunito',sans-serif;line-height:1;}
```

**Part 6** (baseline lines 1717-1717). Manual anchor: from `.tlv-sb-social-icon{width:36px;height:36px;display:flex;align-items:center;justify-cont...` to `.tlv-sb-social-icon{width:36px;height:36px;display:flex;align-items:center;justify-cont...`.
Delete:
```css
.tlv-sb-social-icon{width:36px;height:36px;display:flex;align-items:center;justify-content:center;border-radius:50%;border:1px solid rgba(255,66,161,0.35);background:transparent;cursor:pointer;text-decoration:none;-webkit-tap-highlight-color:transparent;flex-shrink:0;transition:background 0.18s,border-color 0.18s;}
```

**Part 7** (baseline lines 1721-1721). Manual anchor: from `.tlv-sb-social-icon svg{width:16px;height:16px;fill:none;stroke:#ff42a1;stroke-width:2;...` to `.tlv-sb-social-icon svg{width:16px;height:16px;fill:none;stroke:#ff42a1;stroke-width:2;...`.
Delete:
```css
.tlv-sb-social-icon svg{width:16px;height:16px;fill:none;stroke:#ff42a1;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;display:block;}
```

**Part 8** (baseline lines 1729-1729). Manual anchor: from `.tlv-sb-social-icon:active{background:#ff42a1;border-color:#ff42a1;}` to `.tlv-sb-social-icon:active{background:#ff42a1;border-color:#ff42a1;}`.
Delete:
```css
.tlv-sb-social-icon:active{background:#ff42a1;border-color:#ff42a1;}
```

**Part 9** (baseline lines 1733-1733). Manual anchor: from `.tlv-sb-social-icon:active svg{stroke:#fff;}` to `.tlv-sb-social-icon:active svg{stroke:#fff;}`.
Delete:
```css
.tlv-sb-social-icon:active svg{stroke:#fff;}
```

### T90 [REVIEW] 10 orphaned rule(s) inside <style> blocks of sections/about-us.liquid (classes no markup or script uses)
- **File:** `sections/about-us.liquid` | baseline lines 9-9, 30-30, 40-40, 46-46, 47-47, 49-49, 50-50, 51-51, 52-52, 53-53 | kind: orphan selectors in inline CSS (scripted, conservative)
- **Why it is dead:** Every selector of each rule needs a class or ID that appears nowhere in the theme outside CSS: not in any HTML/Liquid markup, JS file, inline script or JSON (any mention, even in a string, counts as used; prefix-built names like x--{{ }} count as used; Shopify/app prefixes count as used; classes inside :not()/:is()/:where()/:has() are ignored). Selectors: .about-reveal-delay-5; .about-tcard; .about-tcard .author; .about-tcard .stars; .about-tcard blockquote; .about-tcard:hover; .about-testimonials; .about-testimonials h2; .hl-green; .icon-cyan
- **Proof:** Scripted full-text search over all 119 theme files with <style> CSS removed. Only rules on lines of pure CSS without Liquid were considered. Joint Chrome check per file (CSS views): exactly these rules removed, nothing added. Not proven from CSS alone (an app or admin content could use a class), hence REVIEW.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .about-reveal-delay-5 { transition-delay: 0.35s; } /   - removed: .icon-cyan { background: rgba(33, 213, 237, 0.08); color: rgb(33, 213, 237); } /   - removed: .hl-green { background: rgba(46, 184, 115, 0.06); color: rgb(36, 143, 89); } /   - removed: .about-testimonials { margin-bottom: 48px; } /   - removed: .about-testimonials h2 { font-size: 24px; font-weight: 900; text-align: center; margin-bottom: 24px; color: rgb(255, 66, 161); } /   - removed: .about-tcard { background: rgb(255, 255, 255); border: 1px solid rgb(228, 228, 231); border-radius: 0.75rem; padding: 28px 32px; transition: border-color 0.4s, box-shadow 0.4s, transform 0.4s; } /   - removed: .about-tcard:hover { border-color: rgba(255, 66, 161, 0.2); box-shadow: rgba(0, 0, 0, 0.04) 0px 4px 16px; transform: translateY(-2px); } /   - removed: .about-tcard .stars { color: rgb(255, 66, 161); font-size: 18px; margin-bottom: 10px; letter-spacing: 2px; } /   - removed: .about-tcard blockquote { text-transform: none; font-size: 15px; color: rgb(100, 116, 139); line-height: 1.8; font-style: italic; margin-bottom: 12px; } /   - removed: .about-tcard .author { font-size: 13px; font-weight: 700; color: rgb(30, 41, 59); }**
- **Visual change if removed:** None expected.
- **Parts:** 10 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 9-9). Manual anchor: from `.about-reveal-delay-5{transition-delay:0.35s}` to `.about-reveal-delay-5{transition-delay:0.35s}`.
Delete:
```css
.about-reveal-delay-5{transition-delay:0.35s}
```

**Part 2** (baseline lines 30-30). Manual anchor: from `.icon-cyan{background:hsla(187,85%,53%,.08);color:hsl(187,85%,53%)}` to `.icon-cyan{background:hsla(187,85%,53%,.08);color:hsl(187,85%,53%)}`.
Delete:
```css
.icon-cyan{background:hsla(187,85%,53%,.08);color:hsl(187,85%,53%)}
```

**Part 3** (baseline lines 40-40). Manual anchor: from `.hl-green{background:hsla(150,60%,45%,.06);color:hsl(150,60%,35%)}` to `.hl-green{background:hsla(150,60%,45%,.06);color:hsl(150,60%,35%)}`.
Delete:
```css
.hl-green{background:hsla(150,60%,45%,.06);color:hsl(150,60%,35%)}
```

**Part 4** (baseline lines 46-46). Manual anchor: from `.about-testimonials{margin-bottom:48px}` to `.about-testimonials{margin-bottom:48px}`.
Delete:
```css
.about-testimonials{margin-bottom:48px}
```

**Part 5** (baseline lines 47-47). Manual anchor: from `.about-testimonials h2{font-size:24px;font-weight:900;text-align:center;margin-bottom:2...` to `.about-testimonials h2{font-size:24px;font-weight:900;text-align:center;margin-bottom:2...`.
Delete:
```css
.about-testimonials h2{font-size:24px;font-weight:900;text-align:center;margin-bottom:24px;color:hsl(330,100%,63%)}
```

**Part 6** (baseline lines 49-49). Manual anchor: from `.about-tcard{background:#ffffff;border:1px solid #e4e4e7;border-radius:0.75rem;padding:...` to `.about-tcard{background:#ffffff;border:1px solid #e4e4e7;border-radius:0.75rem;padding:...`.
Delete:
```css
.about-tcard{background:#ffffff;border:1px solid #e4e4e7;border-radius:0.75rem;padding:28px 32px;transition:border-color 0.4s ease,box-shadow 0.4s ease,transform 0.4s ease}
```

**Part 7** (baseline lines 50-50). Manual anchor: from `.about-tcard:hover{border-color:hsla(330,100%,63%,.2);box-shadow:0 4px 16px rgba(0,0,0,...` to `.about-tcard:hover{border-color:hsla(330,100%,63%,.2);box-shadow:0 4px 16px rgba(0,0,0,...`.
Delete:
```css
.about-tcard:hover{border-color:hsla(330,100%,63%,.2);box-shadow:0 4px 16px rgba(0,0,0,.04);transform:translateY(-2px)}
```

**Part 8** (baseline lines 51-51). Manual anchor: from `.about-tcard .stars{color:#ff42a1;font-size:18px;margin-bottom:10px;letter-spacing:2px}` to `.about-tcard .stars{color:#ff42a1;font-size:18px;margin-bottom:10px;letter-spacing:2px}`.
Delete:
```css
.about-tcard .stars{color:#ff42a1;font-size:18px;margin-bottom:10px;letter-spacing:2px}
```

**Part 9** (baseline lines 52-52). Manual anchor: from `.about-tcard blockquote{text-transform:none;font-size:15px;color:#64748b;line-height:1....` to `.about-tcard blockquote{text-transform:none;font-size:15px;color:#64748b;line-height:1....`.
Delete:
```css
.about-tcard blockquote{text-transform:none;font-size:15px;color:#64748b;line-height:1.8;font-style:italic;margin-bottom:12px}
```

**Part 10** (baseline lines 53-53). Manual anchor: from `.about-tcard .author{font-size:13px;font-weight:700;color:#1e293b}` to `.about-tcard .author{font-size:13px;font-weight:700;color:#1e293b}`.
Delete:
```css
.about-tcard .author{font-size:13px;font-weight:700;color:#1e293b}
```

### T91 [REVIEW] 24 orphaned rule(s) inside <style> blocks of sections/auth-drawer.liquid (classes no markup or script uses)
- **File:** `sections/auth-drawer.liquid` | baseline lines 56-58, 59-64, 65-67, 69-74, 75-75, 77-80, 81-83, 85-85, 86-89, 90-94, 95-98, 100-107, 108-108, 109-109, 116-118, 119-119, 120-120, 182-193, 194-194, 195-195, 197-203, 204-208, 237-244, 245-248 | kind: orphan selectors in inline CSS (scripted, conservative)
- **Why it is dead:** Every selector of each rule needs a class or ID that appears nowhere in the theme outside CSS: not in any HTML/Liquid markup, JS file, inline script or JSON (any mention, even in a string, counts as used; prefix-built names like x--{{ }} count as used; Shopify/app prefixes count as used; classes inside :not()/:is()/:where()/:has() are ignored). Selectors: .tv-auth-drawer .tv-auth-tab; .tv-auth-drawer .tv-auth-tab[aria-selected="true"]; .tv-auth-drawer .tv-field input; .tv-auth-drawer .tv-field input:focus; .tv-auth-drawer .tv-submit; .tv-auth-drawer .tv-submit:active; .tv-auth-drawer .tv-submit:hover; .tv-auth-tab; .tv-auth-tab[aria-selected="true"]; .tv-auth-tabs; .tv-divider; .tv-divider::before,.tv-divider::after; .tv-field; .tv-field input; .tv-field input:focus; .tv-field label; .tv-form-msg; .tv-form-msg.error; .tv-form-msg.success; .tv-shop-login-btn; .tv-shop-login-btn:hover; .tv-submit; .tv-submit:active; .tv-submit:hover
- **Proof:** Scripted full-text search over all 119 theme files with <style> CSS removed. Only rules on lines of pure CSS without Liquid were considered. Joint Chrome check per file (CSS views): exactly these rules removed, nothing added. Not proven from CSS alone (an app or admin content could use a class), hence REVIEW.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .tv-auth-tabs { display: flex; background: rgb(244, 244, 245); border-radius: 9999px; padding: 0.25rem; } /   - removed: .tv-auth-tab { flex: 1 1 0%; padding: 0.6rem 1rem; border: none; background: transparent; border-radius: 9999px; font-size: 0.78rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; cursor: pointer; color: rgb(113, 113, 122); transition: 0.2s; } /   - removed: .tv-auth-tab[aria-selected="true"] { background: rgb(255, 255, 255); color: rgb(24, 24, 27); box-shadow: rgba(0, 0, 0, 0.08) 0px 1px 3px; } /   - removed: .tv-shop-login-btn { display: flex; align-items: center; justify-content: center; gap: 0.6rem; width: 100%; height: 48px; background: rgb(90, 49, 244); color: rgb(255, 255, 255); border: none; border-radius: 8px; font-weight: 600; font-size: 0.9rem; cursor: pointer; transition: background 0.2s; text /   - removed: .tv-shop-login-btn:hover { background: rgb(72, 35, 212); } /   - removed: .tv-divider { display: flex; align-items: center; gap: 0.75rem; color: rgb(161, 161, 170); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.1em; } /   - removed: .tv-divider::before, .tv-divider::after { content: ""; flex: 1 1 0%; height: 1px; background: rgb(228, 228, 231); } /   - removed: .tv-field { display: flex; flex-direction: column; gap: 0.4rem; } /   - removed: .tv-field label { font-size: 0.78rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.06em; color: rgb(63, 63, 70); } /   - removed: .tv-field input { height: 44px; padding: 0px 0.9rem; border: 1px solid rgb(228, 228, 231); border-radius: 8px; font-size: 0.95rem; transition: border-color 0.2s; background: rgb(255, 255, 255); } /   - removed: .tv-field input:focus { outline: none; border-color: rgb(236, 72, 153); box-shadow: rgba(236, 72, 153, 0.12) 0px 0px 0px 3px; } /   - removed: .tv-submit { height: 48px; border: none; border-radius: 9999px; cursor: pointer; background: linear-gradient(90deg, rgb(236, 72, 153), rgb(6, 182, 212), rgb(250, 204, 21)) 0% 50% / 200% 100%; color: rgb(255, 255, 255); font-weight: 700; font-size: 0.85rem; text-transform: uppercase; letter-spacing:  /   - removed: .tv-submit:hover { background-position: 100% 50%; transform: scale(1.02); } /   - removed: .tv-submit:active { transform: scale(0.98); } /   - removed: .tv-form-msg { font-size: 0.8rem; padding: 0.6rem 0.8rem; border-radius: 6px; } /   - removed: .tv-form-msg.error { background: rgb(254, 226, 226); color: rgb(153, 27, 27); } /   - removed: .tv-form-msg.success { background: rgb(220, 252, 231); color: rgb(22, 101, 52); } /   - removed: .tv-auth-drawer .tv-submit { background: linear-gradient(90deg, rgb(236, 72, 153), rgb(6, 182, 212), rgb(250, 204, 21)) 0% 50% / 200% 100% !important; color: rgb(255, 255, 255) !important; font-weight: 700 !important; border-radius: 9999px !important; height: 48px !important; border: none !important /   - removed: .tv-auth-drawer .tv-submit:hover { background-position: 100% 50% !important; transform: scale(1.02) !important; } /   - removed: .tv-auth-drawer .tv-submit:active { transform: scale(0.98) !important; } /   - removed: .tv-auth-drawer .tv-auth-tab { background: transparent !important; box-shadow: none !important; color: rgb(113, 113, 122) !important; border-radius: 9999px !important; font-weight: 700 !important; } /   - removed: .tv-auth-drawer .tv-auth-tab[aria-selected="true"] { background: rgb(255, 255, 255) !important; color: rgb(24, 24, 27) !important; box-shadow: rgba(0, 0, 0, 0.08) 0px 1px 3px !important; } /   - removed: .tv-auth-drawer .tv-field input { background: rgb(255, 255, 255) !important; border: 1px solid rgb(228, 228, 231) !important; border-radius: 8px !important; box-shadow: none !important; height: 44px !important; color: rgb(24, 24, 27) !important; } /   - removed: .tv-auth-drawer .tv-field input:focus { border-color: rgb(236, 72, 153) !important; box-shadow: rgba(236, 72, 153, 0.12) 0px 0px 0px 3px !important; }**
- **Visual change if removed:** None expected.
- **Parts:** 24 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 56-58). Manual anchor: from `.tv-auth-tabs{` to `}`.
Delete:
```css
  .tv-auth-tabs{
    display:flex; background:#f4f4f5; border-radius:9999px; padding:.25rem;
  }
```

**Part 2** (baseline lines 59-64). Manual anchor: from `.tv-auth-tab{` to `}`.
Delete:
```css
  .tv-auth-tab{
    flex:1; padding:.6rem 1rem; border:none; background:transparent;
    border-radius:9999px; font-size:.78rem; font-weight:700;
    text-transform:uppercase; letter-spacing:.08em; cursor:pointer;
    color:#71717a; transition:all .2s;
  }
```

**Part 3** (baseline lines 65-67). Manual anchor: from `.tv-auth-tab[aria-selected="true"]{` to `}`.
Delete:
```css
  .tv-auth-tab[aria-selected="true"]{
    background:#fff; color:#18181b; box-shadow:0 1px 3px rgba(0,0,0,.08);
  }
```

**Part 4** (baseline lines 69-74). Manual anchor: from `.tv-shop-login-btn{` to `}`.
Delete:
```css
  .tv-shop-login-btn{
    display:flex; align-items:center; justify-content:center; gap:.6rem;
    width:100%; height:48px; background:#5A31F4; color:#fff;
    border:none; border-radius:8px; font-weight:600; font-size:.9rem;
    cursor:pointer; transition:background .2s; text-decoration:none;
  }
```

**Part 5** (baseline lines 75-75). Manual anchor: from `.tv-shop-login-btn:hover{ background:#4823d4; }` to `.tv-shop-login-btn:hover{ background:#4823d4; }`.
Delete:
```css
  .tv-shop-login-btn:hover{ background:#4823d4; }
```

**Part 6** (baseline lines 77-80). Manual anchor: from `.tv-divider{` to `}`.
Delete:
```css
  .tv-divider{
    display:flex; align-items:center; gap:.75rem; color:#a1a1aa;
    font-size:.7rem; text-transform:uppercase; letter-spacing:.1em;
  }
```

**Part 7** (baseline lines 81-83). Manual anchor: from `.tv-divider::before,.tv-divider::after{` to `}`.
Delete:
```css
  .tv-divider::before,.tv-divider::after{
    content:""; flex:1; height:1px; background:#e4e4e7;
  }
```

**Part 8** (baseline lines 85-85). Manual anchor: from `.tv-field{ display:flex; flex-direction:column; gap:.4rem; }` to `.tv-field{ display:flex; flex-direction:column; gap:.4rem; }`.
Delete:
```css
  .tv-field{ display:flex; flex-direction:column; gap:.4rem; }
```

**Part 9** (baseline lines 86-89). Manual anchor: from `.tv-field label{` to `}`.
Delete:
```css
  .tv-field label{
    font-size:.78rem; font-weight:600; text-transform:uppercase;
    letter-spacing:.06em; color:#3f3f46;
  }
```

**Part 10** (baseline lines 90-94). Manual anchor: from `.tv-field input{` to `}`.
Delete:
```css
  .tv-field input{
    height:44px; padding:0 .9rem; border:1px solid #e4e4e7;
    border-radius:8px; font-size:.95rem; transition:border-color .2s;
    background:#fff;
  }
```

**Part 11** (baseline lines 95-98). Manual anchor: from `.tv-field input:focus{` to `}`.
Delete:
```css
  .tv-field input:focus{
    outline:none; border-color:#ec4899;
    box-shadow:0 0 0 3px rgba(236,72,153,.12);
  }
```

**Part 12** (baseline lines 100-107). Manual anchor: from `.tv-submit{` to `}`.
Delete:
```css
  .tv-submit{
    height:48px; border:none; border-radius:9999px; cursor:pointer;
    background:linear-gradient(90deg,#ec4899,#06b6d4,#facc15);
    background-size:200% 100%; background-position:0% 50%;
    color:#fff; font-weight:700; font-size:.85rem;
    text-transform:uppercase; letter-spacing:.08em;
    transition:background-position .4s, transform .15s;
  }
```

**Part 13** (baseline lines 108-108). Manual anchor: from `.tv-submit:hover{ background-position:100% 50%; transform:scale(1.02); }` to `.tv-submit:hover{ background-position:100% 50%; transform:scale(1.02); }`.
Delete:
```css
  .tv-submit:hover{ background-position:100% 50%; transform:scale(1.02); }
```

**Part 14** (baseline lines 109-109). Manual anchor: from `.tv-submit:active{ transform:scale(.98); }` to `.tv-submit:active{ transform:scale(.98); }`.
Delete:
```css
  .tv-submit:active{ transform:scale(.98); }
```

**Part 15** (baseline lines 116-118). Manual anchor: from `.tv-form-msg{` to `}`.
Delete:
```css
  .tv-form-msg{
    font-size:.8rem; padding:.6rem .8rem; border-radius:6px;
  }
```

**Part 16** (baseline lines 119-119). Manual anchor: from `.tv-form-msg.error{ background:#fee2e2; color:#991b1b; }` to `.tv-form-msg.error{ background:#fee2e2; color:#991b1b; }`.
Delete:
```css
  .tv-form-msg.error{ background:#fee2e2; color:#991b1b; }
```

**Part 17** (baseline lines 120-120). Manual anchor: from `.tv-form-msg.success{ background:#dcfce7; color:#166534; }` to `.tv-form-msg.success{ background:#dcfce7; color:#166534; }`.
Delete:
```css
  .tv-form-msg.success{ background:#dcfce7; color:#166534; }
```

**Part 18** (baseline lines 182-193). Manual anchor: from `.tv-auth-drawer .tv-submit {` to `}`.
Delete:
```css
  .tv-auth-drawer .tv-submit {
    background: linear-gradient(90deg,#ec4899,#06b6d4,#facc15) !important;
    background-size: 200% 100% !important;
    background-position: 0% 50% !important;
    color: #fff !important;
    font-weight: 700 !important;
    border-radius: 9999px !important;
    height: 48px !important;
    border: none !important;
    letter-spacing: .08em !important;
    text-transform: uppercase !important;
  }
```

**Part 19** (baseline lines 194-194). Manual anchor: from `.tv-auth-drawer .tv-submit:hover { background-position: 100% 50% !important; transform:...` to `.tv-auth-drawer .tv-submit:hover { background-position: 100% 50% !important; transform:...`.
Delete:
```css
  .tv-auth-drawer .tv-submit:hover { background-position: 100% 50% !important; transform: scale(1.02) !important; }
```

**Part 20** (baseline lines 195-195). Manual anchor: from `.tv-auth-drawer .tv-submit:active { transform: scale(.98) !important; }` to `.tv-auth-drawer .tv-submit:active { transform: scale(.98) !important; }`.
Delete:
```css
  .tv-auth-drawer .tv-submit:active { transform: scale(.98) !important; }
```

**Part 21** (baseline lines 197-203). Manual anchor: from `.tv-auth-drawer .tv-auth-tab {` to `}`.
Delete:
```css
  .tv-auth-drawer .tv-auth-tab {
    background: transparent !important;
    box-shadow: none !important;
    color: #71717a !important;
    border-radius: 9999px !important;
    font-weight: 700 !important;
  }
```

**Part 22** (baseline lines 204-208). Manual anchor: from `.tv-auth-drawer .tv-auth-tab[aria-selected="true"] {` to `}`.
Delete:
```css
  .tv-auth-drawer .tv-auth-tab[aria-selected="true"] {
    background: #fff !important;
    color: #18181b !important;
    box-shadow: 0 1px 3px rgba(0,0,0,.08) !important;
  }
```

**Part 23** (baseline lines 237-244). Manual anchor: from `.tv-auth-drawer .tv-field input {` to `}`.
Delete:
```css
  .tv-auth-drawer .tv-field input {
    background: #fff !important;
    border: 1px solid #e4e4e7 !important;
    border-radius: 8px !important;
    box-shadow: none !important;
    height: 44px !important;
    color: #18181b !important;
  }
```

**Part 24** (baseline lines 245-248). Manual anchor: from `.tv-auth-drawer .tv-field input:focus {` to `}`.
Delete:
```css
  .tv-auth-drawer .tv-field input:focus {
    border-color: #ec4899 !important;
    box-shadow: 0 0 0 3px rgba(236,72,153,.12) !important;
  }
```

### T92 [REVIEW] 6 orphaned rule(s) inside <style> blocks of sections/category-rows.liquid (classes no markup or script uses)
- **File:** `sections/category-rows.liquid` | baseline lines 2331-2331, 2337-2337, 7893-7893, 7905-7905, 9342-9342, 9352-9352 | kind: orphan selectors in inline CSS (scripted, conservative)
- **Why it is dead:** Every selector of each rule needs a class or ID that appears nowhere in the theme outside CSS: not in any HTML/Liquid markup, JS file, inline script or JSON (any mention, even in a string, counts as used; prefix-built names like x--{{ }} count as used; Shopify/app prefixes count as used; classes inside :not()/:is()/:where()/:has() are ignored). Selectors: .hw-glitch; .hw-glitch::after; html body #MainContent #tlv-fidget-pair-title; html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent #tlv-fidget-pair-title
- **Proof:** Scripted full-text search over all 119 theme files with <style> CSS removed. Only rules on lines of pure CSS without Liquid were considered. Joint Chrome check per file (CSS views): exactly these rules removed, nothing added. Not proven from CSS alone (an app or admin content could use a class), hence REVIEW.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent #tlv-fidget-pair-title { padding-left: 40px !important; padding-right: 40px !important; box-sizing: border-box !important; } /   - removed: @media (max-width: 767px) > html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent #tlv-fidget-pair-title { padding-left: 22px !important; padding-right: 22px !important; } /   - removed: .hw-glitch { position: relative; display: inline-block; isolation: isolate; color: rgb(17, 17, 17); animation: 6s ease-in-out 0s infinite normal none running hwNeon; } /   - removed: .hw-glitch::after { content: ""; position: absolute; inset: -120% -40%; z-index: -1; pointer-events: none; background: radial-gradient(closest-side, rgba(255, 66, 161, 0.22), rgba(255, 66, 161, 0.12) 35%, rgba(255, 66, 161, 0.05) 65%, rgba(255, 66, 161, 0) 100%); opacity: 0; animation: 6s ease-in-ou /   - removed: html body #MainContent #tlv-fidget-pair-title { padding-left: 40px !important; padding-right: 40px !important; box-sizing: border-box !important; } /   - removed: @media (max-width: 767px) > html body #MainContent #tlv-fidget-pair-title { padding-left: 22px !important; padding-right: 22px !important; }**
- **Visual change if removed:** None expected.
- **Parts:** 6 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 2331-2331). Manual anchor: from `html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#Main...` to `html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#Main...`.
Delete:
```css
html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent #tlv-fidget-pair-title{padding-left:40px!important;padding-right:40px!important;box-sizing:border-box!important}
```

**Part 2** (baseline lines 2337-2337). Manual anchor: from `html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#Main...` to `html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#Main...`.
Delete:
```css
  html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent #tlv-fidget-pair-title{padding-left:22px!important;padding-right:22px!important}
```

**Part 3** (baseline lines 7893-7893). Manual anchor: from `.hw-glitch{position:relative;display:inline-block;isolation:isolate;color:#111;animatio...` to `.hw-glitch{position:relative;display:inline-block;isolation:isolate;color:#111;animatio...`.
Delete:
```css
.hw-glitch{position:relative;display:inline-block;isolation:isolate;color:#111;animation:hwNeon 6s ease-in-out infinite}
```

**Part 4** (baseline lines 7905-7905). Manual anchor: from `.hw-glitch::after{content:"";position:absolute;left:-40%;right:-40%;top:-120%;bottom:-1...` to `.hw-glitch::after{content:"";position:absolute;left:-40%;right:-40%;top:-120%;bottom:-1...`.
Delete:
```css
.hw-glitch::after{content:"";position:absolute;left:-40%;right:-40%;top:-120%;bottom:-120%;z-index:-1;pointer-events:none;background:radial-gradient(closest-side,rgba(255,66,161,.22),rgba(255,66,161,.12) 35%,rgba(255,66,161,.05) 65%,rgba(255,66,161,0) 100%);opacity:0;animation:hwHalo 6s ease-in-out infinite}
```

**Part 5** (baseline lines 9342-9342). Manual anchor: from `html body #MainContent #tlv-fidget-pair-title{padding-left:40px!important;padding-right...` to `html body #MainContent #tlv-fidget-pair-title{padding-left:40px!important;padding-right...`.
Delete:
```css
html body #MainContent #tlv-fidget-pair-title{padding-left:40px!important;padding-right:40px!important;box-sizing:border-box!important}
```

**Part 6** (baseline lines 9352-9352). Manual anchor: from `html body #MainContent #tlv-fidget-pair-title{padding-left:22px!important;padding-right...` to `html body #MainContent #tlv-fidget-pair-title{padding-left:22px!important;padding-right...`.
Delete:
```css
  html body #MainContent #tlv-fidget-pair-title{padding-left:22px!important;padding-right:22px!important}
```

### T93 [REVIEW] 5 orphaned rule(s) inside <style> blocks of sections/clg-hero.liquid (classes no markup or script uses)
- **File:** `sections/clg-hero.liquid` | baseline lines 495-527, 531-575, 1334-1334, 1338-1350, 1484-1521 | kind: orphan selectors in inline CSS (scripted, conservative)
- **Why it is dead:** Every selector of each rule needs a class or ID that appears nowhere in the theme outside CSS: not in any HTML/Liquid markup, JS file, inline script or JSON (any mention, even in a string, counts as used; prefix-built names like x--{{ }} count as used; Shopify/app prefixes count as used; classes inside :not()/:is()/:where()/:has() are ignored). Selectors: .cat-pill--accent; .cat-pill--accent:hover; .cat-pill__icon; .dc-rating; .drift-card__footer
- **Proof:** Scripted full-text search over all 119 theme files with <style> CSS removed. Only rules on lines of pure CSS without Liquid were considered. Joint Chrome check per file (CSS views): exactly these rules removed, nothing added. Not proven from CSS alone (an app or admin content could use a class), hence REVIEW.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .drift-card__footer { height: 82px; overflow: hidden; background: rgb(255, 255, 255); border-radius: 0px 0px 18px 18px; } /   - removed: .dc-rating { position: absolute; bottom: 0px; left: 0px; right: 0px; height: 26px; background: rgba(255, 255, 255, 0.93); display: flex; align-items: center; padding: 0px 7px; gap: 9px; } /   - removed: .cat-pill--accent { border: 1px solid rgba(255, 66, 161, 0.34) !important; } /   - removed: .cat-pill--accent:hover { border-color: rgb(255, 66, 161) !important; box-shadow: 0 0 12px color-mix(in srgb, var(--glow, #ff42a1) 60%, transparent), 0 0 26px color-mix(in srgb, var(--glow, #ff42a1) 35%, transparent) !important; } /   - removed: .cat-pill__icon { width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 15px; flex-shrink: 0; line-height: 1; }**
- **Visual change if removed:** None expected.
- **Parts:** 5 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 495-527). Manual anchor: from `.drift-card__footer {` to `}`.
Delete:
```css
.drift-card__footer {



  height: 82px;



  overflow: hidden;



  /* Opaque — otherwise leftover space below a short name/no-rating



     card is transparent and the next rotated card underneath shows



     through, reading as a stray line of someone else's text. */



  background: #fff;



  border-radius: 0 0 18px 18px;



}
```

**Part 2** (baseline lines 531-575). Manual anchor: from `.dc-rating {` to `}`.
Delete:
```css
.dc-rating {



  position: absolute;



  bottom: 0;



  left: 0;



  right: 0;



  height: 26px;



  background: rgba(255,255,255,0.93);



  display: flex;



  align-items: center;



  padding: 0 7px;



  gap: 9px;



}
```

**Part 3** (baseline lines 1334-1334). Manual anchor: from `.cat-pill--accent { border: 1px solid rgba(255, 66, 161, 0.34) !important; }` to `.cat-pill--accent { border: 1px solid rgba(255, 66, 161, 0.34) !important; }`.
Delete:
```css
.cat-pill--accent { border: 1px solid rgba(255, 66, 161, 0.34) !important; }
```

**Part 4** (baseline lines 1338-1350). Manual anchor: from `.cat-pill--accent:hover {` to `}`.
Delete:
```css
.cat-pill--accent:hover {



  border-color: #ff42a1 !important;



  box-shadow: 0 0 12px color-mix(in srgb, var(--glow, #ff42a1) 60%, transparent), 0 0 26px color-mix(in srgb, var(--glow, #ff42a1) 35%, transparent) !important;



}
```

**Part 5** (baseline lines 1484-1521). Manual anchor: from `.cat-pill__icon {` to `}`.
Delete:
```css
.cat-pill__icon {
  width: 32px;



  height: 32px;



  border-radius: 50%;



  display: flex;



  align-items: center;



  justify-content: center;



  font-size: 15px;



  flex-shrink: 0;



  line-height: 1;



}
```

### T94 [REVIEW] 2 orphaned rule(s) inside <style> blocks of sections/footer.liquid (classes no markup or script uses)
- **File:** `sections/footer.liquid` | baseline lines 118-126, 127-127 | kind: orphan selectors in inline CSS (scripted, conservative)
- **Why it is dead:** Every selector of each rule needs a class or ID that appears nowhere in the theme outside CSS: not in any HTML/Liquid markup, JS file, inline script or JSON (any mention, even in a string, counts as used; prefix-built names like x--{{ }} count as used; Shopify/app prefixes count as used; classes inside :not()/:is()/:where()/:has() are ignored). Selectors: .site-footer__logo; .site-footer__logo sup
- **Proof:** Scripted full-text search over all 119 theme files with <style> CSS removed. Only rules on lines of pure CSS without Liquid were considered. Joint Chrome check per file (CSS views): exactly these rules removed, nothing added. Not proven from CSS alone (an app or admin content could use a class), hence REVIEW.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .site-footer__logo { display: inline-block; font-size: 1.8rem; font-weight: 800; color: rgb(17, 17, 17); text-decoration: none; letter-spacing: -0.03em; font-family: Nunito, system-ui, sans-serif; } /   - removed: .site-footer__logo sup { font-size: 0.5em; font-weight: 700; vertical-align: super; }**
- **Visual change if removed:** None expected.
- **Parts:** 2 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 118-126). Manual anchor: from `.site-footer__logo {` to `}`.
Delete:
```css
.site-footer__logo {
  display: inline-block;
  font-size: 1.8rem;
  font-weight: 800;
  color: #111;
  text-decoration: none;
  letter-spacing: -0.03em;
  font-family: 'Nunito', system-ui, sans-serif;
}
```

**Part 2** (baseline lines 127-127). Manual anchor: from `.site-footer__logo sup { font-size: 0.5em; font-weight: 700; vertical-align: super; }` to `.site-footer__logo sup { font-size: 0.5em; font-weight: 700; vertical-align: super; }`.
Delete:
```css
.site-footer__logo sup { font-size: 0.5em; font-weight: 700; vertical-align: super; }
```

### T95 [REVIEW] 5 orphaned rule(s) inside <style> blocks of sections/newsletter.liquid (classes no markup or script uses)
- **File:** `sections/newsletter.liquid` | baseline lines 2-2, 3-3, 4-4, 5-5, 6-6 | kind: orphan selectors in inline CSS (scripted, conservative)
- **Why it is dead:** Every selector of each rule needs a class or ID that appears nowhere in the theme outside CSS: not in any HTML/Liquid markup, JS file, inline script or JSON (any mention, even in a string, counts as used; prefix-built names like x--{{ }} count as used; Shopify/app prefixes count as used; classes inside :not()/:is()/:where()/:has() are ignored). Selectors: .nl-social-btn; .nl-social-btn svg; .nl-social-btn svg *; .nl-social-btn:hover; .nl-socials
- **Proof:** Scripted full-text search over all 119 theme files with <style> CSS removed. Only rules on lines of pure CSS without Liquid were considered. Joint Chrome check per file (CSS views): exactly these rules removed, nothing added. Not proven from CSS alone (an app or admin content could use a class), hence REVIEW.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .nl-socials { display: flex !important; gap: 16px !important; justify-content: center !important; align-items: center !important; margin: 1.4rem 0px 1.8rem !important; flex-wrap: nowrap !important; } /   - removed: .nl-social-btn { display: inline-flex !important; align-items: center !important; justify-content: center !important; width: 48px !important; height: 48px !important; min-width: 48px !important; min-height: 48px !important; border-radius: 50% !important; border: 1.5px solid rgba(255, 66, 161, 0.4) ! /   - removed: .nl-social-btn:hover { background: rgba(255, 66, 161, 0.12) !important; border-color: rgb(255, 66, 161) !important; } /   - removed: .nl-social-btn svg { width: 22px !important; height: 22px !important; fill: none !important; stroke: rgb(255, 66, 161) !important; stroke-width: 2 !important; display: block !important; flex-shrink: 0 !important; } /   - removed: .nl-social-btn svg * { stroke: rgb(255, 66, 161) !important; fill: none !important; }**
- **Visual change if removed:** None expected.
- **Parts:** 5 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 2-2). Manual anchor: from `.nl-socials{display:flex !important;gap:16px !important;justify-content:center !importa...` to `.nl-socials{display:flex !important;gap:16px !important;justify-content:center !importa...`.
Delete:
```css
.nl-socials{display:flex !important;gap:16px !important;justify-content:center !important;align-items:center !important;margin:1.4rem 0 1.8rem !important;flex-wrap:nowrap !important;}
```

**Part 2** (baseline lines 3-3). Manual anchor: from `.nl-social-btn{display:inline-flex !important;align-items:center !important;justify-con...` to `.nl-social-btn{display:inline-flex !important;align-items:center !important;justify-con...`.
Delete:
```css
.nl-social-btn{display:inline-flex !important;align-items:center !important;justify-content:center !important;width:48px !important;height:48px !important;min-width:48px !important;min-height:48px !important;border-radius:50% !important;border:1.5px solid rgba(255,66,161,0.4) !important;background:transparent !important;color:#ff42a1 !important;text-decoration:none !important;flex-shrink:0 !important;box-shadow:none !important;padding:0 !important;outline:none !important;}
```

**Part 3** (baseline lines 4-4). Manual anchor: from `.nl-social-btn:hover{background:rgba(255,66,161,0.12) !important;border-color:#ff42a1 !...` to `.nl-social-btn:hover{background:rgba(255,66,161,0.12) !important;border-color:#ff42a1 !...`.
Delete:
```css
.nl-social-btn:hover{background:rgba(255,66,161,0.12) !important;border-color:#ff42a1 !important;}
```

**Part 4** (baseline lines 5-5). Manual anchor: from `.nl-social-btn svg{width:22px !important;height:22px !important;fill:none !important;st...` to `.nl-social-btn svg{width:22px !important;height:22px !important;fill:none !important;st...`.
Delete:
```css
.nl-social-btn svg{width:22px !important;height:22px !important;fill:none !important;stroke:#ff42a1 !important;stroke-width:2 !important;display:block !important;flex-shrink:0 !important;}
```

**Part 5** (baseline lines 6-6). Manual anchor: from `.nl-social-btn svg *{stroke:#ff42a1 !important;fill:none !important;}` to `.nl-social-btn svg *{stroke:#ff42a1 !important;fill:none !important;}`.
Delete:
```css
.nl-social-btn svg *{stroke:#ff42a1 !important;fill:none !important;}
```

### T96 [REVIEW] 2 orphaned rule(s) inside <style> blocks of sections/product-main.liquid (classes no markup or script uses)
- **File:** `sections/product-main.liquid` | baseline lines 2407-2407, 2563-2563 | kind: orphan selectors in inline CSS (scripted, conservative)
- **Why it is dead:** Every selector of each rule needs a class or ID that appears nowhere in the theme outside CSS: not in any HTML/Liquid markup, JS file, inline script or JSON (any mention, even in a string, counts as used; prefix-built names like x--{{ }} count as used; Shopify/app prefixes count as used; classes inside :not()/:is()/:where()/:has() are ignored). Selectors: #trust-bar; .product-stars, .product-stars *
- **Proof:** Scripted full-text search over all 119 theme files with <style> CSS removed. Only rules on lines of pure CSS without Liquid were considered. Joint Chrome check per file (CSS views): exactly these rules removed, nothing added. Not proven from CSS alone (an app or admin content could use a class), hence REVIEW.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: #trust-bar { height: 82px !important; } /   - removed: .product-stars, .product-stars * { filter: none !important; box-shadow: none !important; text-shadow: none !important; }**
- **Visual change if removed:** None expected.
- **Parts:** 2 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 2407-2407). Manual anchor: from `#trust-bar { height:82px !important; }` to `#trust-bar { height:82px !important; }`.
Delete:
```css
    #trust-bar { height:82px !important; }
```

**Part 2** (baseline lines 2563-2563). Manual anchor: from `.product-stars, .product-stars * { filter: none !important; box-shadow: none !important...` to `.product-stars, .product-stars * { filter: none !important; box-shadow: none !important...`.
Delete:
```css
    .product-stars, .product-stars * { filter: none !important; box-shadow: none !important; text-shadow: none !important; }
```

### T97 [REVIEW] 1 orphaned rule(s) inside <style> blocks of snippets/cart-drawer.liquid (classes no markup or script uses)
- **File:** `snippets/cart-drawer.liquid` | baseline lines 118-118 | kind: orphan selectors in inline CSS (scripted, conservative)
- **Why it is dead:** Every selector of each rule needs a class or ID that appears nowhere in the theme outside CSS: not in any HTML/Liquid markup, JS file, inline script or JSON (any mention, even in a string, counts as used; prefix-built names like x--{{ }} count as used; Shopify/app prefixes count as used; classes inside :not()/:is()/:where()/:has() are ignored). Selectors: #tvCartDrawer .cart-bundle__discount
- **Proof:** Scripted full-text search over all 119 theme files with <style> CSS removed. Only rules on lines of pure CSS without Liquid were considered. Joint Chrome check per file (CSS views): exactly these rules removed, nothing added. Not proven from CSS alone (an app or admin content could use a class), hence REVIEW.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: #tvCartDrawer .cart-bundle__discount { font-size: 11px !important; color: rgb(22, 163, 74) !important; font-weight: 700 !important; margin-top: 6px !important; text-align: center !important; display: block !important; }**
- **Visual change if removed:** None expected.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 118-118). Manual anchor: from `#tvCartDrawer .cart-bundle__discount { font-size:11px !important; color:#16a34a !import...` to `#tvCartDrawer .cart-bundle__discount { font-size:11px !important; color:#16a34a !import...`.
Delete:
```css
  #tvCartDrawer .cart-bundle__discount { font-size:11px !important; color:#16a34a !important; font-weight:700 !important; margin-top:6px !important; text-align:center !important; display:block !important; }
```

### T98 [REVIEW] 1 orphaned rule(s) inside <style> blocks of snippets/collection-discovery-banners.liquid (classes no markup or script uses)
- **File:** `snippets/collection-discovery-banners.liquid` | baseline lines 3-3 | kind: orphan selectors in inline CSS (scripted, conservative)
- **Why it is dead:** Every selector of each rule needs a class or ID that appears nowhere in the theme outside CSS: not in any HTML/Liquid markup, JS file, inline script or JSON (any mention, even in a string, counts as used; prefix-built names like x--{{ }} count as used; Shopify/app prefixes count as used; classes inside :not()/:is()/:where()/:has() are ignored). Selectors: .collection-discovery--three
- **Proof:** Scripted full-text search over all 119 theme files with <style> CSS removed. Only rules on lines of pure CSS without Liquid were considered. Joint Chrome check per file (CSS views): exactly these rules removed, nothing added. Not proven from CSS alone (an app or admin content could use a class), hence REVIEW.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .collection-discovery--three { grid-template-columns: repeat(3, minmax(0px, 1fr)); }**
- **Visual change if removed:** None expected.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 3-3). Manual anchor: from `.collection-discovery--three{grid-template-columns:repeat(3,minmax(0,1fr))}` to `.collection-discovery--three{grid-template-columns:repeat(3,minmax(0,1fr))}`.
Delete:
```css
.collection-discovery--three{grid-template-columns:repeat(3,minmax(0,1fr))}
```

### T99 [REVIEW] 48 orphaned rule(s) inside <style> blocks of snippets/collection-page.liquid (classes no markup or script uses)
- **File:** `snippets/collection-page.liquid` | baseline lines 85-85, 86-86, 87-87, 88-88, 89-89, 103-103, 104-104, 106-106, 117-117, 126-138, 148-148, 149-149, 150-150, 151-151, 152-152, 153-153, 181-181, 185-185, 186-186, 187-187, 188-188, 189-189, 190-190, 191-191, 192-192, 193-193, 197-197, 202-202, 203-203, 204-204, 205-205, 206-206, 207-207, 211-211, 212-212, 230-230, 231-231, 232-232, 233-233, 234-234, 235-235, 236-236, 347-347, 348-348, 349-349, 350-350, 351-351, 352-352 | kind: orphan selectors in inline CSS (scripted, conservative)
- **Why it is dead:** Every selector of each rule needs a class or ID that appears nowhere in the theme outside CSS: not in any HTML/Liquid markup, JS file, inline script or JSON (any mention, even in a string, counts as used; prefix-built names like x--{{ }} count as used; Shopify/app prefixes count as used; classes inside :not()/:is()/:where()/:has() are ignored). Selectors: #tvFilters .tv-tc-label; #tvFilters .tv-theme-more; #tvFilters .tv-theme-more:hover; #tvFilters .tv-type-card; #tvFilters .tv-type-card.tv-type-card--active; #tvFilters .tv-type-card.tv-type-card--active .tv-tc-label; .coll-af-badge; .coll-af-badge--on; .coll-allfilters; .coll-allfilters--active; .coll-allfilters:hover; .coll-intro--collapsible .coll-intro__body; .coll-intro--collapsible.coll-intro--expanded .coll-intro__body; .coll-intro--has-overflow .coll-intro__fade; .coll-intro--has-overflow.coll-intro--expanded .coll-intro__fade; .coll-intro__badge; .coll-intro__body; .coll-intro__fade; .coll-vbtn; .coll-vbtn:hover:not(.coll-vbtn--on); .coll-view-toggle; .tv-tc-label; .tv-theme-more; .tv-theme-more:hover; .tv-theme-row--center; .tv-trust-bar; .tv-trust-icon; .tv-trust-icon--blue; .tv
- **Proof:** Scripted full-text search over all 119 theme files with <style> CSS removed. Only rules on lines of pure CSS without Liquid were considered. Joint Chrome check per file (CSS views): exactly these rules removed, nothing added. Not proven from CSS alone (an app or admin content could use a class), hence REVIEW.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .coll-allfilters { display: inline-flex; align-items: center; gap: 6px; padding: 0.65rem 1.2rem; border-radius: 9999px; border: 1.5px solid rgb(229, 231, 235); background: rgb(255, 255, 255); font-size: 13.5px; font-weight: 600; font-family: inherit; cursor: pointer; white-space: nowrap; box-shadow: /   - removed: .coll-allfilters:hover { border-color: rgb(255, 66, 161); color: rgb(255, 66, 161) !important; } /   - removed: .coll-allfilters--active { background: rgb(255, 66, 161) !important; border-color: rgb(255, 66, 161) !important; color: rgb(255, 255, 255) !important; } /   - removed: .coll-af-badge { display: none; align-items: center; justify-content: center; min-width: 18px; height: 18px; border-radius: 50%; background: rgb(255, 66, 161); font-size: 10px; font-weight: 800; padding: 0px 3px; color: rgb(255, 255, 255) !important; } /   - removed: .coll-af-badge--on { display: inline-flex !important; } /   - removed: .coll-view-toggle { display: inline-flex; align-items: center; border: 1.5px solid rgb(229, 231, 235); border-radius: 9999px; overflow: hidden; background: rgb(255, 255, 255); box-shadow: rgba(0, 0, 0, 0.07) 0px 1px 4px; flex-shrink: 0; } /   - removed: .coll-vbtn { display: flex; align-items: center; justify-content: center; width: 40px; height: 40px; border: none; background: transparent; cursor: pointer; color: rgb(136, 136, 136); transition: background 0.15s, color 0.15s; font-family: inherit; } /   - removed: .coll-vbtn:hover:not(.coll-vbtn--on) { color: rgb(255, 66, 161); } /   - removed: @media (max-width: 767px) > .coll-view-toggle { display: none; } /   - removed: .coll-intro__badge { display: inline-flex; align-items: center; color: var(--ci-accent, #ff42a1); background: var(--ci-badge-bg, rgba(255,66,161,0.08)); font-size: 13px; font-weight: 600; letter-spacing: 0.6px; border-radius: 999px; padding: 8px 22px; margin-bottom: 1.1rem; font-family: inherit; } /   - removed: .coll-intro__body { position: relative; } /   - removed: .coll-intro--collapsible .coll-intro__body { max-height: 92px; overflow: hidden; transition: max-height 0.3s; } /   - removed: .coll-intro--collapsible.coll-intro--expanded .coll-intro__body { max-height: 2000px; } /   - removed: .coll-intro__fade { position: absolute; bottom: 0px; left: 0px; right: 0px; height: 42px; background: linear-gradient(rgba(255, 255, 255, 0), rgb(255, 255, 255)); pointer-events: none; opacity: 0; transition: opacity 0.2s; } /   - removed: .coll-intro--has-overflow .coll-intro__fade { opacity: 1; } /   - removed: .coll-intro--has-overflow.coll-intro--expanded .coll-intro__fade { opacity: 0; } /   - removed: @media (max-width: 767px) > .coll-intro__badge { font-size: 12px; padding: 7px 18px; } /   - removed: .tv-trust-bar { display: flex; align-items: stretch; background: rgb(255, 245, 249); border-radius: 16px; padding: 1.25rem 2rem; margin-bottom: 2.5rem; gap: 0px; } /   - removed: .tv-trust-item { display: flex; align-items: center; gap: 1rem; flex: 1 1 0%; justify-content: center; padding: 0px 1rem; } /   - removed: .tv-trust-sep { width: 1px; background: rgb(240, 200, 221); flex-shrink: 0; align-self: stretch; } /   - removed: .tv-trust-icon { width: 52px; height: 52px; border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0; } /   - removed: .tv-trust-icon--pink { background: rgba(255, 66, 161, 0.15) !important; color: rgb(255, 66, 161) !important; } /   - removed: .tv-trust-icon--blue { background: rgba(59, 130, 246, 0.15) !important; color: rgb(59, 130, 246) !important; } /   - removed: .tv-trust-icon--green { background: rgba(34, 197, 94, 0.15) !important; color: rgb(34, 197, 94) !important; } /   - removed: .tv-trust-title { font-size: 15px; font-weight: 800; line-height: 1.3; color: rgb(17, 17, 17) !important; } /   - removed: .tv-trust-sub { font-size: 12.5px; margin-top: 3px; color: rgb(119, 119, 119) !important; } /   - removed: .tv-theme-row--center { justify-content: center !important; } /   - removed: .tv-type-card { transition: border-color 0.15s, box-shadow 0.15s; display: flex !important; flex-direction: column !important; align-items: center !important; justify-content: flex-start !important; width: 115px !important; padding: 0.85rem 0.5rem 0.7rem !important; border-radius: 14px !important; b /   - removed: .tv-type-card img { pointer-events: none; width: 72px !important; height: 72px !important; object-fit: cover !important; border-radius: 10px !important; } /   - removed: .tv-tc-label { pointer-events: none; font-size: 12px !important; font-weight: 600 !important; color: rgb(51, 51, 51) !important; text-align: center !important; line-height: 1.3 !important; } /   - removed: .tv-type-card:hover { border-color: rgb(255, 66, 161) !important; box-shadow: rgb(255, 66, 161) 0px 0px 0px 2px !important; } /   - removed: .tv-type-card--active { border-color: rgb(255, 66, 161) !important; box-shadow: rgb(255, 66, 161) 0px 0px 0px 2px !important; background: rgba(255, 66, 161, 0.04) !important; } /   - removed: .tv-type-card--active .tv-tc-label { color: rgb(255, 66, 161) !important; } /   - removed: .tv-theme-more { transition: border-color 0.15s, color 0.15s; display: inline-flex !important; align-items: center !important; gap: 5px !important; padding: 0.52rem 1.1rem !important; border-radius: 9999px !important; border: 1.5px solid rgb(226, 232, 240) !important; background: rgb(255, 255, 255)  /   - removed: .tv-theme-more:hover { border-color: rgb(255, 66, 161) !important; color: rgb(255, 66, 161) !important; } /   - removed: @media (max-width: 767px) > .tv-trust-bar { padding: 1rem; } /   - removed: @media (max-width: 767px) > .tv-trust-item { gap: 0.65rem; padding: 0px 0.25rem; } /   - removed: @media (max-width: 767px) > .tv-trust-icon { width: 40px; height: 40px; } /   - removed: @media (max-width: 767px) > .tv-trust-title { font-size: 12.5px; } /   - removed: @media (max-width: 767px) > .tv-trust-sub { font-size: 11px; } /   - removed: @media (max-width: 767px) > .tv-type-card { width: 90px !important; } /   - removed: @media (max-width: 767px) > .tv-type-card img { width: 58px !important; height: 58px !important; } /   - removed: #tvFilters .tv-theme-more { color: rgb(68, 68, 68) !important; background: rgb(255, 255, 255) !important; border: 1.5px solid rgb(226, 232, 240) !important; box-shadow: rgba(0, 0, 0, 0.06) 0px 1px 3px !important; } /   - removed: #tvFilters .tv-theme-more:hover { color: rgb(255, 66, 161) !important; background: rgb(255, 255, 255) !important; border-color: rgb(255, 66, 161) !important; } /   - removed: #tvFilters .tv-type-card { background: rgb(255, 255, 255) !important; border: 1.5px solid rgb(229, 231, 235) !important; box-shadow: rgba(0, 0, 0, 0.07) 0px 1px 5px !important; } /   - removed: #tvFilters .tv-tc-label { color: rgb(51, 51, 51) !important; font-weight: 600 !important; } /   - removed: #tvFilters .tv-type-card.tv-type-card--active .tv-tc-label { color: rgb(255, 66, 161) !important; } /   - removed: #tvFilters .tv-type-card.tv-type-card--active { border-color: rgb(255, 66, 161) !important; box-shadow: rgb(255, 66, 161) 0px 0px 0px 2px !important; background: rgba(255, 66, 161, 0.04) !important; }**
- **Visual change if removed:** None expected.
- **Parts:** 48 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 85-85). Manual anchor: from `.coll-allfilters { display:inline-flex; align-items:center; gap:6px; padding:0.65rem 1....` to `.coll-allfilters { display:inline-flex; align-items:center; gap:6px; padding:0.65rem 1....`.
Delete:
```css
.coll-allfilters { display:inline-flex; align-items:center; gap:6px; padding:0.65rem 1.2rem; border-radius:9999px; border:1.5px solid #e5e7eb; background:#fff; color:#111 !important; font-size:13.5px; font-weight:600; font-family:inherit; cursor:pointer; white-space:nowrap; box-shadow:0 1px 4px rgba(0,0,0,0.07); transition:border-color 0.15s,color 0.15s; flex-shrink:0; }
```

**Part 2** (baseline lines 86-86). Manual anchor: from `.coll-allfilters:hover { border-color:#ff42a1; color:#ff42a1 !important; }` to `.coll-allfilters:hover { border-color:#ff42a1; color:#ff42a1 !important; }`.
Delete:
```css
.coll-allfilters:hover { border-color:#ff42a1; color:#ff42a1 !important; }
```

**Part 3** (baseline lines 87-87). Manual anchor: from `.coll-allfilters--active { background:#ff42a1 !important; border-color:#ff42a1 !importa...` to `.coll-allfilters--active { background:#ff42a1 !important; border-color:#ff42a1 !importa...`.
Delete:
```css
.coll-allfilters--active { background:#ff42a1 !important; border-color:#ff42a1 !important; color:#fff !important; }
```

**Part 4** (baseline lines 88-88). Manual anchor: from `.coll-af-badge { display:none; align-items:center; justify-content:center; min-width:18...` to `.coll-af-badge { display:none; align-items:center; justify-content:center; min-width:18...`.
Delete:
```css
.coll-af-badge { display:none; align-items:center; justify-content:center; min-width:18px; height:18px; border-radius:50%; background:#ff42a1; color:#fff !important; font-size:10px; font-weight:800; padding:0 3px; }
```

**Part 5** (baseline lines 89-89). Manual anchor: from `.coll-af-badge--on { display:inline-flex !important; }` to `.coll-af-badge--on { display:inline-flex !important; }`.
Delete:
```css
.coll-af-badge--on { display:inline-flex !important; }
```

**Part 6** (baseline lines 103-103). Manual anchor: from `.coll-view-toggle { display:inline-flex; align-items:center; border:1.5px solid #e5e7eb...` to `.coll-view-toggle { display:inline-flex; align-items:center; border:1.5px solid #e5e7eb...`.
Delete:
```css
.coll-view-toggle { display:inline-flex; align-items:center; border:1.5px solid #e5e7eb; border-radius:9999px; overflow:hidden; background:#fff; box-shadow:0 1px 4px rgba(0,0,0,0.07); flex-shrink:0; }
```

**Part 7** (baseline lines 104-104). Manual anchor: from `.coll-vbtn { display:flex; align-items:center; justify-content:center; width:40px; heig...` to `.coll-vbtn { display:flex; align-items:center; justify-content:center; width:40px; heig...`.
Delete:
```css
.coll-vbtn { display:flex; align-items:center; justify-content:center; width:40px; height:40px; border:none; background:transparent; cursor:pointer; color:#888; transition:background 0.15s,color 0.15s; font-family:inherit; }
```

**Part 8** (baseline lines 106-106). Manual anchor: from `.coll-vbtn:hover:not(.coll-vbtn--on) { color:#ff42a1; }` to `.coll-vbtn:hover:not(.coll-vbtn--on) { color:#ff42a1; }`.
Delete:
```css
.coll-vbtn:hover:not(.coll-vbtn--on) { color:#ff42a1; }
```

**Part 9** (baseline lines 117-117). Manual anchor: from `.coll-view-toggle { display:none; }` to `.coll-view-toggle { display:none; }`.
Delete:
```css
  .coll-view-toggle { display:none; }
```

**Part 10** (baseline lines 126-138). Manual anchor: from `.coll-intro__badge {` to `}`.
Delete:
```css
.coll-intro__badge {
  display: inline-flex;
  align-items: center;
  color: var(--ci-accent, #ff42a1);
  background: var(--ci-badge-bg, rgba(255,66,161,0.08));
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.6px;
  border-radius: 999px;
  padding: 8px 22px;
  margin-bottom: 1.1rem;
  font-family: inherit;
}
```

**Part 11** (baseline lines 148-148). Manual anchor: from `.coll-intro__body { position: relative; }` to `.coll-intro__body { position: relative; }`.
Delete:
```css
.coll-intro__body { position: relative; }
```

**Part 12** (baseline lines 149-149). Manual anchor: from `.coll-intro--collapsible .coll-intro__body { max-height: 92px; overflow: hidden; transi...` to `.coll-intro--collapsible .coll-intro__body { max-height: 92px; overflow: hidden; transi...`.
Delete:
```css
.coll-intro--collapsible .coll-intro__body { max-height: 92px; overflow: hidden; transition: max-height 0.3s ease; }
```

**Part 13** (baseline lines 150-150). Manual anchor: from `.coll-intro--collapsible.coll-intro--expanded .coll-intro__body { max-height: 2000px; }` to `.coll-intro--collapsible.coll-intro--expanded .coll-intro__body { max-height: 2000px; }`.
Delete:
```css
.coll-intro--collapsible.coll-intro--expanded .coll-intro__body { max-height: 2000px; }
```

**Part 14** (baseline lines 151-151). Manual anchor: from `.coll-intro__fade { position: absolute; bottom: 0; left: 0; right: 0; height: 42px; bac...` to `.coll-intro__fade { position: absolute; bottom: 0; left: 0; right: 0; height: 42px; bac...`.
Delete:
```css
.coll-intro__fade { position: absolute; bottom: 0; left: 0; right: 0; height: 42px; background: linear-gradient(to bottom, rgba(255,255,255,0), #fff); pointer-events: none; opacity: 0; transition: opacity 0.2s; }
```

**Part 15** (baseline lines 152-152). Manual anchor: from `.coll-intro--has-overflow .coll-intro__fade { opacity: 1; }` to `.coll-intro--has-overflow .coll-intro__fade { opacity: 1; }`.
Delete:
```css
.coll-intro--has-overflow .coll-intro__fade { opacity: 1; }
```

**Part 16** (baseline lines 153-153). Manual anchor: from `.coll-intro--has-overflow.coll-intro--expanded .coll-intro__fade { opacity: 0; }` to `.coll-intro--has-overflow.coll-intro--expanded .coll-intro__fade { opacity: 0; }`.
Delete:
```css
.coll-intro--has-overflow.coll-intro--expanded .coll-intro__fade { opacity: 0; }
```

**Part 17** (baseline lines 181-181). Manual anchor: from `.coll-intro__badge { font-size: 12px; padding: 7px 18px; }` to `.coll-intro__badge { font-size: 12px; padding: 7px 18px; }`.
Delete:
```css
  .coll-intro__badge { font-size: 12px; padding: 7px 18px; }
```

**Part 18** (baseline lines 185-185). Manual anchor: from `.tv-trust-bar { display:flex; align-items:stretch; background:#fff5f9; border-radius:16...` to `.tv-trust-bar { display:flex; align-items:stretch; background:#fff5f9; border-radius:16...`.
Delete:
```css
.tv-trust-bar { display:flex; align-items:stretch; background:#fff5f9; border-radius:16px; padding:1.25rem 2rem; margin-bottom:2.5rem; gap:0; }
```

**Part 19** (baseline lines 186-186). Manual anchor: from `.tv-trust-item { display:flex; align-items:center; gap:1rem; flex:1; justify-content:ce...` to `.tv-trust-item { display:flex; align-items:center; gap:1rem; flex:1; justify-content:ce...`.
Delete:
```css
.tv-trust-item { display:flex; align-items:center; gap:1rem; flex:1; justify-content:center; padding:0 1rem; }
```

**Part 20** (baseline lines 187-187). Manual anchor: from `.tv-trust-sep { width:1px; background:#f0c8dd; flex-shrink:0; align-self:stretch; }` to `.tv-trust-sep { width:1px; background:#f0c8dd; flex-shrink:0; align-self:stretch; }`.
Delete:
```css
.tv-trust-sep { width:1px; background:#f0c8dd; flex-shrink:0; align-self:stretch; }
```

**Part 21** (baseline lines 188-188). Manual anchor: from `.tv-trust-icon { width:52px; height:52px; border-radius:50%; display:flex; align-items:...` to `.tv-trust-icon { width:52px; height:52px; border-radius:50%; display:flex; align-items:...`.
Delete:
```css
.tv-trust-icon { width:52px; height:52px; border-radius:50%; display:flex; align-items:center; justify-content:center; flex-shrink:0; }
```

**Part 22** (baseline lines 189-189). Manual anchor: from `.tv-trust-icon--pink { background:rgba(255,66,161,0.15) !important; color:#ff42a1 !impo...` to `.tv-trust-icon--pink { background:rgba(255,66,161,0.15) !important; color:#ff42a1 !impo...`.
Delete:
```css
.tv-trust-icon--pink { background:rgba(255,66,161,0.15) !important; color:#ff42a1 !important; }
```

**Part 23** (baseline lines 190-190). Manual anchor: from `.tv-trust-icon--blue { background:rgba(59,130,246,0.15) !important; color:#3b82f6 !impo...` to `.tv-trust-icon--blue { background:rgba(59,130,246,0.15) !important; color:#3b82f6 !impo...`.
Delete:
```css
.tv-trust-icon--blue { background:rgba(59,130,246,0.15) !important; color:#3b82f6 !important; }
```

**Part 24** (baseline lines 191-191). Manual anchor: from `.tv-trust-icon--green { background:rgba(34,197,94,0.15) !important; color:#22c55e !impo...` to `.tv-trust-icon--green { background:rgba(34,197,94,0.15) !important; color:#22c55e !impo...`.
Delete:
```css
.tv-trust-icon--green { background:rgba(34,197,94,0.15) !important; color:#22c55e !important; }
```

**Part 25** (baseline lines 192-192). Manual anchor: from `.tv-trust-title { font-size:15px; font-weight:800; color:#111 !important; line-height:1...` to `.tv-trust-title { font-size:15px; font-weight:800; color:#111 !important; line-height:1...`.
Delete:
```css
.tv-trust-title { font-size:15px; font-weight:800; color:#111 !important; line-height:1.3; }
```

**Part 26** (baseline lines 193-193). Manual anchor: from `.tv-trust-sub { font-size:12.5px; color:#777 !important; margin-top:3px; }` to `.tv-trust-sub { font-size:12.5px; color:#777 !important; margin-top:3px; }`.
Delete:
```css
.tv-trust-sub { font-size:12.5px; color:#777 !important; margin-top:3px; }
```

**Part 27** (baseline lines 197-197). Manual anchor: from `.tv-theme-row--center { justify-content:center !important; }` to `.tv-theme-row--center { justify-content:center !important; }`.
Delete:
```css
.tv-theme-row--center { justify-content:center !important; }
```

**Part 28** (baseline lines 202-202). Manual anchor: from `.tv-type-card { display:flex !important; flex-direction:column !important; align-items:...` to `.tv-type-card { display:flex !important; flex-direction:column !important; align-items:...`.
Delete:
```css
.tv-type-card { display:flex !important; flex-direction:column !important; align-items:center !important; justify-content:flex-start !important; width:115px !important; padding:0.85rem 0.5rem 0.7rem !important; border-radius:14px !important; border:1.5px solid #e5e7eb !important; background:#fff !important; cursor:pointer !important; gap:0.5rem !important; font-family:inherit !important; transition:border-color 0.15s,box-shadow 0.15s; box-shadow:0 1px 5px rgba(0,0,0,0.07) !important; }
```

**Part 29** (baseline lines 203-203). Manual anchor: from `.tv-type-card img { width:72px !important; height:72px !important; object-fit:cover !im...` to `.tv-type-card img { width:72px !important; height:72px !important; object-fit:cover !im...`.
Delete:
```css
.tv-type-card img { width:72px !important; height:72px !important; object-fit:cover !important; border-radius:10px !important; pointer-events:none; }
```

**Part 30** (baseline lines 204-204). Manual anchor: from `.tv-tc-label { font-size:12px !important; font-weight:600 !important; color:#333 !impor...` to `.tv-tc-label { font-size:12px !important; font-weight:600 !important; color:#333 !impor...`.
Delete:
```css
.tv-tc-label { font-size:12px !important; font-weight:600 !important; color:#333 !important; text-align:center !important; line-height:1.3 !important; pointer-events:none; }
```

**Part 31** (baseline lines 205-205). Manual anchor: from `.tv-type-card:hover { border-color:#ff42a1 !important; box-shadow:0 0 0 2px #ff42a1 !im...` to `.tv-type-card:hover { border-color:#ff42a1 !important; box-shadow:0 0 0 2px #ff42a1 !im...`.
Delete:
```css
.tv-type-card:hover { border-color:#ff42a1 !important; box-shadow:0 0 0 2px #ff42a1 !important; }
```

**Part 32** (baseline lines 206-206). Manual anchor: from `.tv-type-card--active { border-color:#ff42a1 !important; box-shadow:0 0 0 2px #ff42a1 !...` to `.tv-type-card--active { border-color:#ff42a1 !important; box-shadow:0 0 0 2px #ff42a1 !...`.
This text also exists elsewhere in the file, so it is located by the neighbouring lines (kept, not deleted): before = `(none)`, after = `.tv-type-card--active .tv-tc-label { color:#ff42a1 !important; }`.
Delete:
```css
.tv-type-card--active { border-color:#ff42a1 !important; box-shadow:0 0 0 2px #ff42a1 !important; background:rgba(255,66,161,0.04) !important; }
```

**Part 33** (baseline lines 207-207). Manual anchor: from `.tv-type-card--active .tv-tc-label { color:#ff42a1 !important; }` to `.tv-type-card--active .tv-tc-label { color:#ff42a1 !important; }`.
This text also exists elsewhere in the file, so it is located by the neighbouring lines (kept, not deleted): before = `(none)`, after = `.tv-theme-pill { display:inline-flex !important; align-items:center !important; padding...`.
Delete:
```css
.tv-type-card--active .tv-tc-label { color:#ff42a1 !important; }
```

**Part 34** (baseline lines 211-211). Manual anchor: from `.tv-theme-more { display:inline-flex !important; align-items:center !important; gap:5px...` to `.tv-theme-more { display:inline-flex !important; align-items:center !important; gap:5px...`.
Delete:
```css
.tv-theme-more { display:inline-flex !important; align-items:center !important; gap:5px !important; padding:0.52rem 1.1rem !important; border-radius:9999px !important; border:1.5px solid #e2e8f0 !important; background:#fff !important; color:#444 !important; font-size:13.5px !important; font-weight:400 !important; font-family:inherit !important; cursor:pointer !important; transition:border-color 0.15s,color 0.15s; box-shadow:0 1px 3px rgba(0,0,0,0.06) !important; }
```

**Part 35** (baseline lines 212-212). Manual anchor: from `.tv-theme-more:hover { border-color:#ff42a1 !important; color:#ff42a1 !important; }` to `.tv-theme-more:hover { border-color:#ff42a1 !important; color:#ff42a1 !important; }`.
Delete:
```css
.tv-theme-more:hover { border-color:#ff42a1 !important; color:#ff42a1 !important; }
```

**Part 36** (baseline lines 230-230). Manual anchor: from `.tv-trust-bar { padding:1rem; }` to `.tv-trust-bar { padding:1rem; }`.
Delete:
```css
  .tv-trust-bar { padding:1rem; }
```

**Part 37** (baseline lines 231-231). Manual anchor: from `.tv-trust-item { gap:0.65rem; padding:0 0.25rem; }` to `.tv-trust-item { gap:0.65rem; padding:0 0.25rem; }`.
Delete:
```css
  .tv-trust-item { gap:0.65rem; padding:0 0.25rem; }
```

**Part 38** (baseline lines 232-232). Manual anchor: from `.tv-trust-icon { width:40px; height:40px; }` to `.tv-trust-icon { width:40px; height:40px; }`.
Delete:
```css
  .tv-trust-icon { width:40px; height:40px; }
```

**Part 39** (baseline lines 233-233). Manual anchor: from `.tv-trust-title { font-size:12.5px; }` to `.tv-trust-title { font-size:12.5px; }`.
Delete:
```css
  .tv-trust-title { font-size:12.5px; }
```

**Part 40** (baseline lines 234-234). Manual anchor: from `.tv-trust-sub { font-size:11px; }` to `.tv-trust-sub { font-size:11px; }`.
Delete:
```css
  .tv-trust-sub { font-size:11px; }
```

**Part 41** (baseline lines 235-235). Manual anchor: from `.tv-type-card { width:90px !important; }` to `.tv-type-card { width:90px !important; }`.
Delete:
```css
  .tv-type-card { width:90px !important; }
```

**Part 42** (baseline lines 236-236). Manual anchor: from `.tv-type-card img { width:58px !important; height:58px !important; }` to `.tv-type-card img { width:58px !important; height:58px !important; }`.
Delete:
```css
  .tv-type-card img { width:58px !important; height:58px !important; }
```

**Part 43** (baseline lines 347-347). Manual anchor: from `#tvFilters .tv-theme-more { color:#444 !important; background:#fff !important; border:1...` to `#tvFilters .tv-theme-more { color:#444 !important; background:#fff !important; border:1...`.
Delete:
```css
      #tvFilters .tv-theme-more { color:#444 !important; background:#fff !important; border:1.5px solid #e2e8f0 !important; box-shadow:0 1px 3px rgba(0,0,0,0.06) !important; }
```

**Part 44** (baseline lines 348-348). Manual anchor: from `#tvFilters .tv-theme-more:hover { color:#ff42a1 !important; background:#fff !important;...` to `#tvFilters .tv-theme-more:hover { color:#ff42a1 !important; background:#fff !important;...`.
Delete:
```css
      #tvFilters .tv-theme-more:hover { color:#ff42a1 !important; background:#fff !important; border-color:#ff42a1 !important; }
```

**Part 45** (baseline lines 349-349). Manual anchor: from `#tvFilters .tv-type-card { background:#fff !important; border:1.5px solid #e5e7eb !impo...` to `#tvFilters .tv-type-card { background:#fff !important; border:1.5px solid #e5e7eb !impo...`.
Delete:
```css
      #tvFilters .tv-type-card { background:#fff !important; border:1.5px solid #e5e7eb !important; box-shadow:0 1px 5px rgba(0,0,0,0.07) !important; }
```

**Part 46** (baseline lines 350-350). Manual anchor: from `#tvFilters .tv-tc-label { color:#333 !important; font-weight:600 !important; }` to `#tvFilters .tv-tc-label { color:#333 !important; font-weight:600 !important; }`.
Delete:
```css
      #tvFilters .tv-tc-label { color:#333 !important; font-weight:600 !important; }
```

**Part 47** (baseline lines 351-351). Manual anchor: from `#tvFilters .tv-type-card.tv-type-card--active .tv-tc-label { color:#ff42a1 !important; }` to `#tvFilters .tv-type-card.tv-type-card--active .tv-tc-label { color:#ff42a1 !important; }`.
Delete:
```css
      #tvFilters .tv-type-card.tv-type-card--active .tv-tc-label { color:#ff42a1 !important; }
```

**Part 48** (baseline lines 352-352). Manual anchor: from `#tvFilters .tv-type-card.tv-type-card--active { border-color:#ff42a1 !important; box-sh...` to `#tvFilters .tv-type-card.tv-type-card--active { border-color:#ff42a1 !important; box-sh...`.
Delete:
```css
      #tvFilters .tv-type-card.tv-type-card--active { border-color:#ff42a1 !important; box-shadow:0 0 0 2px #ff42a1 !important; background:rgba(255,66,161,0.04) !important; }
```

### T100 [REVIEW] 19 orphaned rule(s) inside <style> blocks of snippets/cr-card-styles.liquid (classes no markup or script uses)
- **File:** `snippets/cr-card-styles.liquid` | baseline lines 47-60, 61-61, 62-62, 63-63, 64-64, 65-65, 66-66, 67-67, 196-202, 203-203, 204-204, 205-205, 206-206, 224-228, 233-238, 239-243, 284-284, 312-312, 313-313 | kind: orphan selectors in inline CSS (scripted, conservative)
- **Why it is dead:** Every selector of each rule needs a class or ID that appears nowhere in the theme outside CSS: not in any HTML/Liquid markup, JS file, inline script or JSON (any mention, even in a string, counts as used; prefix-built names like x--{{ }} count as used; Shopify/app prefixes count as used; classes inside :not()/:is()/:where()/:has() are ignored). Selectors: .cr-card__badge; .cr-card__badge--award; .cr-card__badge--bestseller; .cr-card__badge--hot; .cr-card__badge--new; .cr-card__badge--sale; .cr-card__badge--toppick; .cr-card__badge--trending; .cr-card__jdgm; .cr-card__jdgm .jdgm-prev-badge; .cr-card__jdgm .jdgm-prev-badge__count; .cr-card__jdgm .jdgm-prev-badge__stars; .cr-card__soldout; .pc-vcount__plus; .var-dot__count; .var-dot__label; html body #MainContent#MainContent .cr-card.cr-card .cr-card__meta-row .pc-heart.pc-heart; html body #MainContent#MainContent .cr-card.cr-card .cr-card__meta-row .pc-heart.pc-heart svg; html body #MainContent#MainContent .cr-card.cr-card .cr-card__meta-row.cr-card__meta-row
- **Proof:** Scripted full-text search over all 119 theme files with <style> CSS removed. Only rules on lines of pure CSS without Liquid were considered. Joint Chrome check per file (CSS views): exactly these rules removed, nothing added. Not proven from CSS alone (an app or admin content could use a class), hence REVIEW.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .cr-card__badge { position: absolute; top: 7px; left: 7px; font-size: 10px; font-weight: 800; letter-spacing: 0.05em; text-transform: uppercase; padding: 0.24rem 0.6rem; border-radius: 999px; color: rgb(255, 255, 255); pointer-events: none; background: transparent; } /   - removed: .cr-card__badge--new { background: transparent; border: 1.5px solid rgb(22, 163, 74); color: rgb(22, 163, 74); } /   - removed: .cr-card__badge--hot { background: transparent; border: 1.5px solid rgb(249, 115, 22); color: rgb(249, 115, 22); } /   - removed: .cr-card__badge--sale { background: transparent; border: 1.5px solid rgb(220, 38, 38); color: rgb(220, 38, 38); } /   - removed: .cr-card__badge--bestseller { background: transparent; border: 1.5px solid rgb(124, 58, 237); color: rgb(124, 58, 237); } /   - removed: .cr-card__badge--trending { background: transparent; border: 1.5px solid rgb(14, 165, 233); color: rgb(14, 165, 233); } /   - removed: .cr-card__badge--award { background: transparent; border: 1.5px solid rgb(202, 138, 4); color: rgb(202, 138, 4); } /   - removed: .cr-card__badge--toppick { background: transparent; border: 1.5px solid rgb(219, 39, 119); color: rgb(219, 39, 119); } /   - removed: .cr-card__soldout { font-size: 0.68rem; font-weight: 700; color: rgb(170, 170, 170); white-space: nowrap; flex-shrink: 0; } /   - removed: .cr-card__jdgm { line-height: 1; overflow: hidden; } /   - removed: .cr-card__jdgm .jdgm-prev-badge { display: inline-flex !important; align-items: center !important; gap: 1px !important; font-size: 0px !important; } /   - removed: .cr-card__jdgm .jdgm-prev-badge__stars { font-size: 11px !important; letter-spacing: 0px !important; } /   - removed: .cr-card__jdgm .jdgm-prev-badge__count { font-size: 10px !important; color: rgb(156, 163, 175) !important; margin-left: 3px !important; } /   - removed: html body #MainContent#MainContent .cr-card.cr-card .cr-card__meta-row.cr-card__meta-row { display: flex !important; visibility: visible !important; align-items: center !important; justify-content: space-between !important; gap: 8px !important; min-height: 32px !important; height: 32px !important; m /   - removed: html body #MainContent#MainContent .cr-card.cr-card .cr-card__meta-row .pc-heart.pc-heart { display: flex !important; visibility: visible !important; flex: 0 0 36px !important; width: 36px !important; height: 36px !important; min-width: 36px !important; min-height: 36px !important; opacity: 1 !impor /   - removed: html body #MainContent#MainContent .cr-card.cr-card .cr-card__meta-row .pc-heart.pc-heart svg { display: block !important; width: 27px !important; height: 27px !important; min-width: 27px !important; min-height: 27px !important; stroke: currentcolor !important; stroke-width: 1.9 !important; fill: no /   - removed: .pc-vcount__plus { display: none !important; } /   - removed: .var-dot__count { font-size: 9px; font-weight: 800; line-height: 1; letter-spacing: 0px; } /   - removed: .var-dot__label { font-size: 5px; font-weight: 700; line-height: 1; letter-spacing: 0px; text-transform: lowercase; }**
- **Visual change if removed:** None expected.
- **Parts:** 19 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 47-60). Manual anchor: from `.cr-card__badge {` to `}`.
Delete:
```css
.cr-card__badge {
  position: absolute;
  top: 7px;
  left: 7px;
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  padding: 0.24rem 0.6rem;
  border-radius: 999px;
  color: #fff;
  pointer-events: none;
  background: transparent;
}
```

**Part 2** (baseline lines 61-61). Manual anchor: from `.cr-card__badge--new { background: transparent; border: 1.5px solid #16a34a; color: #16...` to `.cr-card__badge--new { background: transparent; border: 1.5px solid #16a34a; color: #16...`.
Delete:
```css
.cr-card__badge--new        { background: transparent; border: 1.5px solid #16a34a; color: #16a34a; }
```

**Part 3** (baseline lines 62-62). Manual anchor: from `.cr-card__badge--hot { background: transparent; border: 1.5px solid #f97316; color: #f9...` to `.cr-card__badge--hot { background: transparent; border: 1.5px solid #f97316; color: #f9...`.
Delete:
```css
.cr-card__badge--hot        { background: transparent; border: 1.5px solid #f97316; color: #f97316; }
```

**Part 4** (baseline lines 63-63). Manual anchor: from `.cr-card__badge--sale { background: transparent; border: 1.5px solid #dc2626; color: #d...` to `.cr-card__badge--sale { background: transparent; border: 1.5px solid #dc2626; color: #d...`.
Delete:
```css
.cr-card__badge--sale       { background: transparent; border: 1.5px solid #dc2626; color: #dc2626; }
```

**Part 5** (baseline lines 64-64). Manual anchor: from `.cr-card__badge--bestseller { background: transparent; border: 1.5px solid #7c3aed; col...` to `.cr-card__badge--bestseller { background: transparent; border: 1.5px solid #7c3aed; col...`.
Delete:
```css
.cr-card__badge--bestseller { background: transparent; border: 1.5px solid #7c3aed; color: #7c3aed; }
```

**Part 6** (baseline lines 65-65). Manual anchor: from `.cr-card__badge--trending { background: transparent; border: 1.5px solid #0ea5e9; color...` to `.cr-card__badge--trending { background: transparent; border: 1.5px solid #0ea5e9; color...`.
Delete:
```css
.cr-card__badge--trending   { background: transparent; border: 1.5px solid #0ea5e9; color: #0ea5e9; }
```

**Part 7** (baseline lines 66-66). Manual anchor: from `.cr-card__badge--award { background: transparent; border: 1.5px solid #ca8a04; color: #...` to `.cr-card__badge--award { background: transparent; border: 1.5px solid #ca8a04; color: #...`.
Delete:
```css
.cr-card__badge--award      { background: transparent; border: 1.5px solid #ca8a04; color: #ca8a04; }
```

**Part 8** (baseline lines 67-67). Manual anchor: from `.cr-card__badge--toppick { background: transparent; border: 1.5px solid #db2777; color:...` to `.cr-card__badge--toppick { background: transparent; border: 1.5px solid #db2777; color:...`.
Delete:
```css
.cr-card__badge--toppick    { background: transparent; border: 1.5px solid #db2777; color: #db2777; }
```

**Part 9** (baseline lines 196-202). Manual anchor: from `.cr-card__soldout {` to `}`.
Delete:
```css
.cr-card__soldout {
  font-size: 0.68rem;
  font-weight: 700;
  color: #aaa;
  white-space: nowrap;
  flex-shrink: 0;
}
```

**Part 10** (baseline lines 203-203). Manual anchor: from `.cr-card__jdgm { line-height: 1; overflow: hidden; }` to `.cr-card__jdgm { line-height: 1; overflow: hidden; }`.
Delete:
```css
.cr-card__jdgm { line-height: 1; overflow: hidden; }
```

**Part 11** (baseline lines 204-204). Manual anchor: from `.cr-card__jdgm .jdgm-prev-badge { display: inline-flex !important; align-items: center ...` to `.cr-card__jdgm .jdgm-prev-badge { display: inline-flex !important; align-items: center ...`.
Delete:
```css
.cr-card__jdgm .jdgm-prev-badge { display: inline-flex !important; align-items: center !important; gap: 1px !important; font-size: 0 !important; }
```

**Part 12** (baseline lines 205-205). Manual anchor: from `.cr-card__jdgm .jdgm-prev-badge__stars { font-size: 11px !important; letter-spacing: 0 ...` to `.cr-card__jdgm .jdgm-prev-badge__stars { font-size: 11px !important; letter-spacing: 0 ...`.
Delete:
```css
.cr-card__jdgm .jdgm-prev-badge__stars { font-size: 11px !important; letter-spacing: 0 !important; }
```

**Part 13** (baseline lines 206-206). Manual anchor: from `.cr-card__jdgm .jdgm-prev-badge__count { font-size: 10px !important; color: #9ca3af !im...` to `.cr-card__jdgm .jdgm-prev-badge__count { font-size: 10px !important; color: #9ca3af !im...`.
Delete:
```css
.cr-card__jdgm .jdgm-prev-badge__count { font-size: 10px !important; color: #9ca3af !important; margin-left: 3px !important; }
```

**Part 14** (baseline lines 224-228). Manual anchor: from `html body #MainContent#MainContent .cr-card.cr-card .cr-card__meta-row.cr-card__meta-row{` to `}`.
Delete:
```css
html body #MainContent#MainContent .cr-card.cr-card .cr-card__meta-row.cr-card__meta-row{
  display:flex!important;visibility:visible!important;align-items:center!important;
  justify-content:space-between!important;gap:8px!important;min-height:32px!important;
  height:32px!important;margin:0!important;overflow:visible!important;
}
```

**Part 15** (baseline lines 233-238). Manual anchor: from `html body #MainContent#MainContent .cr-card.cr-card .cr-card__meta-row .pc-heart.pc-heart{` to `}`.
Delete:
```css
html body #MainContent#MainContent .cr-card.cr-card .cr-card__meta-row .pc-heart.pc-heart{
  display:flex!important;visibility:visible!important;flex:0 0 36px!important;width:36px!important;
  height:36px!important;min-width:36px!important;min-height:36px!important;opacity:1!important;
  align-items:center!important;justify-content:center!important;pointer-events:auto!important;
  cursor:pointer!important;touch-action:manipulation!important;
}
```

**Part 16** (baseline lines 239-243). Manual anchor: from `html body #MainContent#MainContent .cr-card.cr-card .cr-card__meta-row .pc-heart.pc-hea...` to `}`.
Delete:
```css
html body #MainContent#MainContent .cr-card.cr-card .cr-card__meta-row .pc-heart.pc-heart svg{
  display:block!important;width:27px!important;height:27px!important;min-width:27px!important;
  min-height:27px!important;stroke:currentColor!important;stroke-width:1.9!important;fill:none!important;
  pointer-events:none!important;
}
```

**Part 17** (baseline lines 284-284). Manual anchor: from `.pc-vcount__plus{display:none!important}` to `.pc-vcount__plus{display:none!important}`.
Delete:
```css
.pc-vcount__plus{display:none!important}
```

**Part 18** (baseline lines 312-312). Manual anchor: from `.var-dot__count { font-size:9px; font-weight:800; line-height:1; letter-spacing:0; }` to `.var-dot__count { font-size:9px; font-weight:800; line-height:1; letter-spacing:0; }`.
Delete:
```css
.var-dot__count { font-size:9px; font-weight:800; line-height:1; letter-spacing:0; }
```

**Part 19** (baseline lines 313-313). Manual anchor: from `.var-dot__label { font-size:5px; font-weight:700; line-height:1; letter-spacing:0; text...` to `.var-dot__label { font-size:5px; font-weight:700; line-height:1; letter-spacing:0; text...`.
Delete:
```css
.var-dot__label { font-size:5px; font-weight:700; line-height:1; letter-spacing:0; text-transform:lowercase; }
```

### T101 [REVIEW] 1 orphaned rule(s) inside <style> blocks of snippets/heart-js.liquid (classes no markup or script uses)
- **File:** `snippets/heart-js.liquid` | baseline lines 27-27 | kind: orphan selectors in inline CSS (scripted, conservative)
- **Why it is dead:** Every selector of each rule needs a class or ID that appears nowhere in the theme outside CSS: not in any HTML/Liquid markup, JS file, inline script or JSON (any mention, even in a string, counts as used; prefix-built names like x--{{ }} count as used; Shopify/app prefixes count as used; classes inside :not()/:is()/:where()/:has() are ignored). Selectors: .tlv-sc-count
- **Proof:** Scripted full-text search over all 119 theme files with <style> CSS removed. Only rules on lines of pure CSS without Liquid were considered. Joint Chrome check per file (CSS views): exactly these rules removed, nothing added. Not proven from CSS alone (an app or admin content could use a class), hence REVIEW.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .tlv-sc-count { white-space: nowrap; font: 700 2cqw / 1 Nunito, sans-serif; color: rgb(169, 169, 178); margin: 0.9cqw 0px 4.8cqw !important; }**
- **Visual change if removed:** None expected.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 27-27). Manual anchor: from `.tlv-sc-count{white-space:nowrap;margin:.9cqw 0 4.8cqw!important;font:700 2cqw/1 'Nunit...` to `.tlv-sc-count{white-space:nowrap;margin:.9cqw 0 4.8cqw!important;font:700 2cqw/1 'Nunit...`.
Delete:
```css
.tlv-sc-count{white-space:nowrap;margin:.9cqw 0 4.8cqw!important;font:700 2cqw/1 'Nunito',sans-serif;color:#a9a9b2}
```

### T102 [REVIEW] 38 orphaned rule(s) inside <style> blocks of snippets/product-card-styles.liquid (classes no markup or script uses)
- **File:** `snippets/product-card-styles.liquid` | baseline lines 8-8, 9-9, 10-10, 13-13, 14-14, 18-18, 19-19, 20-20, 21-21, 22-22, 23-23, 24-24, 26-26, 27-27, 28-28, 29-29, 30-30, 31-31, 38-38, 45-45, 46-46, 47-47, 49-49, 51-51, 55-55, 59-59, 60-60, 61-61, 66-66, 68-68, 70-70, 72-72, 74-74, 75-75, 76-76, 80-86, 117-117, 118-118 | kind: orphan selectors in inline CSS (scripted, conservative)
- **Why it is dead:** Every selector of each rule needs a class or ID that appears nowhere in the theme outside CSS: not in any HTML/Liquid markup, JS file, inline script or JSON (any mention, even in a string, counts as used; prefix-built names like x--{{ }} count as used; Shopify/app prefixes count as used; classes inside :not()/:is()/:where()/:has() are ignored). Selectors: .collection-page-wrap .product-card .product-card__img; .collection-page-wrap .product-card:hover .product-card__img; .product-card:hover .product-card__img; .product-card:hover .product-card__quickview; .product-card__image-wrap; .product-card__img; .product-card__jdgm .jdgm-prev-badge; .product-card__jdgm .jdgm-prev-badge__count; .product-card__jdgm .jdgm-prev-badge__stars; .product-card__link; .product-card__quickview; .product-card__sold-badge; .product-card__stars; .product-card__tag; .product-card__tag--blaster; .product-card__tag--building; .product-card__tag--building::before; .product-card__tag--collectible; .product-card__tag--fidget; .product-card__tag--halloween; .product-card__tag--keychain; .product-card__tag--plush; .product-card__tag--puzzle; .product-card__tag--puzzle::bef
- **Proof:** Scripted full-text search over all 119 theme files with <style> CSS removed. Only rules on lines of pure CSS without Liquid were considered. Joint Chrome check per file (CSS views): exactly these rules removed, nothing added. Not proven from CSS alone (an app or admin content could use a class), hence REVIEW.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .product-card__image-wrap { position: relative; width: 100%; aspect-ratio: 1 / 1; overflow: hidden; background: rgb(240, 240, 240); flex-shrink: 0; } /   - removed: .product-card__img { position: absolute; inset: 0px; width: 100%; height: 100%; object-fit: cover; display: block; transition: transform 0.3s; } /   - removed: .product-card:hover .product-card__img { transform: scale(1.04); } /   - removed: @media (hover: hover) and (pointer: fine) > .collection-page-wrap .product-card .product-card__img { transition: transform 0.32s !important; } /   - removed: @media (hover: hover) and (pointer: fine) > .collection-page-wrap .product-card:hover .product-card__img { transform: scale(1.06) !important; } /   - removed: .product-card__link { position: absolute; inset: 0px; z-index: 2; display: block; } /   - removed: .product-card__quickview { position: absolute; bottom: 10px; right: 10px; width: 30px; height: 30px; background: rgba(255, 255, 255, 0.92); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: rgb(68, 68, 68); text-decoration: none; opacity: 0; transition: opacity  /   - removed: .product-card:hover .product-card__quickview { opacity: 1; } /   - removed: .product-card__tag { position: absolute; top: 13px; left: 13px; z-index: 3; font-family: Nunito, system-ui, sans-serif; font-size: 4.7px; font-weight: 700; line-height: 1; letter-spacing: 0.03em; padding: 5px 11px; border: 1px solid rgb(234, 88, 12); border-radius: 999px; color: rgb(234, 88, 12); ba /   - removed: .product-card__tag--collectible { border-color: rgb(13, 148, 136); color: rgb(13, 148, 136); } /   - removed: .product-card__tag--keychain { border-color: rgb(22, 163, 74); color: rgb(22, 163, 74); } /   - removed: .product-card__tag--blaster { border-color: rgb(220, 38, 38); color: rgb(220, 38, 38); } /   - removed: .product-card__tag--plush { border-color: rgb(255, 66, 161); color: rgb(255, 66, 161); } /   - removed: .product-card__tag--fidget { border-color: rgb(79, 110, 247); color: rgb(79, 110, 247); } /   - removed: .product-card__tag--rc { position: absolute; border-color: transparent !important; color: transparent !important; background: linear-gradient(90deg, rgb(14, 165, 233), rgb(249, 115, 22)) text !important; } /   - removed: .product-card__tag--rc::before { content: ""; position: absolute; inset: 0px; border-radius: 999px; padding: 1px; background: linear-gradient(90deg, rgb(14, 165, 233), rgb(249, 115, 22)); mask: linear-gradient(rgb(0, 0, 0) 0px, rgb(0, 0, 0) 0px) content-box exclude, linear-gradient(rgb(0, 0, 0) 0px, /   - removed: .product-card__tag--building { position: absolute; border-color: transparent !important; color: transparent !important; background: linear-gradient(90deg, rgb(79, 70, 229), rgb(236, 72, 153)) text !important; } /   - removed: .product-card__tag--building::before { content: ""; position: absolute; inset: 0px; border-radius: 999px; padding: 1px; background: linear-gradient(90deg, rgb(79, 70, 229), rgb(236, 72, 153)); mask: linear-gradient(rgb(0, 0, 0) 0px, rgb(0, 0, 0) 0px) content-box exclude, linear-gradient(rgb(0, 0, 0) /   - removed: .product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag, .product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag:hover { border-radius: 10px !important; } /   - removed: .product-card__tag--puzzle { position: absolute; border-color: transparent !important; color: transparent !important; background: linear-gradient(90deg, rgb(6, 182, 212), rgb(244, 63, 94)) text !important; } /   - removed: .product-card__tag--puzzle::before { content: ""; position: absolute; inset: 0px; border-radius: 999px; padding: 1px; background: linear-gradient(90deg, rgb(6, 182, 212), rgb(244, 63, 94)); mask: linear-gradient(rgb(0, 0, 0) 0px, rgb(0, 0, 0) 0px) content-box exclude, linear-gradient(rgb(0, 0, 0) 0p /   - removed: .product-card__tag--halloween { border-color: rgb(17, 17, 17); color: rgb(17, 17, 17); } /   - removed: .product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag::before { content: "" !important; display: block !important; position: absolute !important; inset: 50% auto auto 100% !important; width: 11px !important; height: 1px !import /   - removed: html body .product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag { right: 1px !important; } /   - removed: .product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag::before { transform-origin: right center !important; transition: transform 0.26s cubic-bezier(0.4, 0, 1, 1) 0.12s, opacity 0.2s linear 0.12s !important; } /   - removed: @media (hover: hover) > .product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag:hover { right: -9px !important; transition: right 0.42s cubic-bezier(0.22, 1, 0.36, 1) 0.04s !important; } /   - removed: @media (hover: hover) > .product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag:hover::before { transform: translateY(-50%) scaleX(0) !important; opacity: 0 !important; transition: transform 0.42s cubic-bezier(0.22, 1, 0.36, 1) 0 /   - removed: @media (hover: hover) > .product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag:hover::after { transform: translateY(-50%) translateX(-10px) !important; transition: transform 0.2s cubic-bezier(0.22, 1, 0.36, 1) 0.2s, opacity 0.2s /   - removed: .product-card__sold-badge { position: absolute; top: 10px; left: 10px; background: rgba(0, 0, 0, 0.65); color: rgb(255, 255, 255); font-size: 11px; font-weight: 600; padding: 3px 8px; border-radius: 20px; z-index: 3; } /   - removed: .product-card__vendor { font-size: 11px; color: rgb(153, 153, 153); font-weight: 400; line-height: 1.2; } /   - removed: .product-card__title--two { white-space: normal !important; height: 36px !important; overflow: hidden !important; text-overflow: clip !important; } /   - removed: .product-card__stars { display: flex; align-items: center; gap: 1px; height: 16px; flex-shrink: 0; } /   - removed: .product-card__jdgm .jdgm-prev-badge { display: inline-flex !important; align-items: center !important; gap: 1px !important; font-size: 0px !important; } /   - removed: .product-card__jdgm .jdgm-prev-badge__stars { font-size: 11px !important; } /   - removed: .product-card__jdgm .jdgm-prev-badge__count { font-size: 11px !important; color: rgb(153, 153, 153) !important; margin-left: 3px !important; } /   - removed: .product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag { width: 24.15px !important; min-width: 24.15px !important; max-width: 24.15px !important; height: 24.15px !important; right: 2px !important; } /   - removed: .var-dot__count { font-size: 9px; font-weight: 800; line-height: 1; letter-spacing: 0px; } /   - removed: .var-dot__label { font-size: 5px; font-weight: 700; line-height: 1; letter-spacing: 0px; text-transform: lowercase; }**
- **Visual change if removed:** None expected.
- **Parts:** 38 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 8-8). Manual anchor: from `.product-card__image-wrap{position:relative;width:100%;aspect-ratio:1/1;overflow:hidden...` to `.product-card__image-wrap{position:relative;width:100%;aspect-ratio:1/1;overflow:hidden...`.
Delete:
```css
.product-card__image-wrap{position:relative;width:100%;aspect-ratio:1/1;overflow:hidden;background:#f0f0f0;flex-shrink:0}
```

**Part 2** (baseline lines 9-9). Manual anchor: from `.product-card__img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;di...` to `.product-card__img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;di...`.
Delete:
```css
.product-card__img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block;transition:transform 0.3s ease}
```

**Part 3** (baseline lines 10-10). Manual anchor: from `.product-card:hover .product-card__img{transform:scale(1.04)}` to `.product-card:hover .product-card__img{transform:scale(1.04)}`.
Delete:
```css
.product-card:hover .product-card__img{transform:scale(1.04)}
```

**Part 4** (baseline lines 13-13). Manual anchor: from `.collection-page-wrap .product-card .product-card__img{transition:transform .32s ease!i...` to `.collection-page-wrap .product-card .product-card__img{transition:transform .32s ease!i...`.
Delete:
```css
  .collection-page-wrap .product-card .product-card__img{transition:transform .32s ease!important}
```

**Part 5** (baseline lines 14-14). Manual anchor: from `.collection-page-wrap .product-card:hover .product-card__img{transform:scale(1.06)!impo...` to `.collection-page-wrap .product-card:hover .product-card__img{transform:scale(1.06)!impo...`.
Delete:
```css
  .collection-page-wrap .product-card:hover .product-card__img{transform:scale(1.06)!important}
```

**Part 6** (baseline lines 18-18). Manual anchor: from `.product-card__link{position:absolute;inset:0;z-index:2;display:block}` to `.product-card__link{position:absolute;inset:0;z-index:2;display:block}`.
Delete:
```css
.product-card__link{position:absolute;inset:0;z-index:2;display:block}
```

**Part 7** (baseline lines 19-19). Manual anchor: from `.product-card__quickview{position:absolute;bottom:10px;right:10px;width:30px;height:30p...` to `.product-card__quickview{position:absolute;bottom:10px;right:10px;width:30px;height:30p...`.
Delete:
```css
.product-card__quickview{position:absolute;bottom:10px;right:10px;width:30px;height:30px;background:rgba(255,255,255,0.92);border-radius:50%;display:flex;align-items:center;justify-content:center;color:#444;text-decoration:none;opacity:0;transition:opacity 0.2s;z-index:3}
```

**Part 8** (baseline lines 20-20). Manual anchor: from `.product-card:hover .product-card__quickview{opacity:1}` to `.product-card:hover .product-card__quickview{opacity:1}`.
Delete:
```css
.product-card:hover .product-card__quickview{opacity:1}
```

**Part 9** (baseline lines 21-21). Manual anchor: from `.product-card__tag{position:absolute;top:13px;left:13px;z-index:3;font-family:'Nunito',...` to `.product-card__tag{position:absolute;top:13px;left:13px;z-index:3;font-family:'Nunito',...`.
Delete:
```css
.product-card__tag{position:absolute;top:13px;left:13px;z-index:3;font-family:'Nunito',system-ui,sans-serif;font-size:4.7px;font-weight:700;line-height:1;letter-spacing:0.03em;padding:5px 11px;border:1px solid #ea580c;border-radius:999px;color:#ea580c;background:transparent;pointer-events:none}
```

**Part 10** (baseline lines 22-22). Manual anchor: from `.product-card__tag--collectible{border-color:#0d9488;color:#0d9488}` to `.product-card__tag--collectible{border-color:#0d9488;color:#0d9488}`.
Delete:
```css
.product-card__tag--collectible{border-color:#0d9488;color:#0d9488}
```

**Part 11** (baseline lines 23-23). Manual anchor: from `.product-card__tag--keychain{border-color:#16a34a;color:#16a34a}` to `.product-card__tag--keychain{border-color:#16a34a;color:#16a34a}`.
Delete:
```css
.product-card__tag--keychain{border-color:#16a34a;color:#16a34a}
```

**Part 12** (baseline lines 24-24). Manual anchor: from `.product-card__tag--blaster{border-color:#dc2626;color:#dc2626}` to `.product-card__tag--blaster{border-color:#dc2626;color:#dc2626}`.
Delete:
```css
.product-card__tag--blaster{border-color:#dc2626;color:#dc2626}
```

**Part 13** (baseline lines 26-26). Manual anchor: from `.product-card__tag--plush{border-color:#ff42a1;color:#ff42a1}` to `.product-card__tag--plush{border-color:#ff42a1;color:#ff42a1}`.
Delete:
```css
.product-card__tag--plush{border-color:#ff42a1;color:#ff42a1}
```

**Part 14** (baseline lines 27-27). Manual anchor: from `.product-card__tag--fidget{border-color:#4f6ef7;color:#4f6ef7}` to `.product-card__tag--fidget{border-color:#4f6ef7;color:#4f6ef7}`.
Delete:
```css
.product-card__tag--fidget{border-color:#4f6ef7;color:#4f6ef7}
```

**Part 15** (baseline lines 28-28). Manual anchor: from `.product-card__tag--rc{border-color:transparent!important;color:transparent!important;b...` to `.product-card__tag--rc{border-color:transparent!important;color:transparent!important;b...`.
Delete:
```css
.product-card__tag--rc{border-color:transparent!important;color:transparent!important;background:linear-gradient(90deg,#0ea5e9,#f97316)!important;-webkit-background-clip:text!important;background-clip:text!important;position:absolute}
```

**Part 16** (baseline lines 29-29). Manual anchor: from `.product-card__tag--rc::before{content:"";position:absolute;inset:0;border-radius:999px...` to `.product-card__tag--rc::before{content:"";position:absolute;inset:0;border-radius:999px...`.
Delete:
```css
.product-card__tag--rc::before{content:"";position:absolute;inset:0;border-radius:999px;padding:1px;background:linear-gradient(90deg,#0ea5e9,#f97316);-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;pointer-events:none}
```

**Part 17** (baseline lines 30-30). Manual anchor: from `.product-card__tag--building{border-color:transparent!important;color:transparent!impor...` to `.product-card__tag--building{border-color:transparent!important;color:transparent!impor...`.
Delete:
```css
.product-card__tag--building{border-color:transparent!important;color:transparent!important;background:linear-gradient(90deg,#4f46e5,#ec4899)!important;-webkit-background-clip:text!important;background-clip:text!important;position:absolute}
```

**Part 18** (baseline lines 31-31). Manual anchor: from `.product-card__tag--building::before{content:"";position:absolute;inset:0;border-radius...` to `.product-card__tag--building::before{content:"";position:absolute;inset:0;border-radius...`.
Delete:
```css
.product-card__tag--building::before{content:"";position:absolute;inset:0;border-radius:999px;padding:1px;background:linear-gradient(90deg,#4f46e5,#ec4899);-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;pointer-events:none}
```

**Part 19** (baseline lines 38-38). Manual anchor: from `.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__...` to `.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__...`.
Delete:
```css
.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag,.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag:hover{border-radius:10px!important}
```

**Part 20** (baseline lines 45-45). Manual anchor: from `.product-card__tag--puzzle{border-color:transparent!important;color:transparent!importa...` to `.product-card__tag--puzzle{border-color:transparent!important;color:transparent!importa...`.
Delete:
```css
.product-card__tag--puzzle{border-color:transparent!important;color:transparent!important;background:linear-gradient(90deg,#06b6d4,#f43f5e)!important;-webkit-background-clip:text!important;background-clip:text!important;position:absolute}
```

**Part 21** (baseline lines 46-46). Manual anchor: from `.product-card__tag--puzzle::before{content:"";position:absolute;inset:0;border-radius:9...` to `.product-card__tag--puzzle::before{content:"";position:absolute;inset:0;border-radius:9...`.
Delete:
```css
.product-card__tag--puzzle::before{content:"";position:absolute;inset:0;border-radius:999px;padding:1px;background:linear-gradient(90deg,#06b6d4,#f43f5e);-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;pointer-events:none}
```

**Part 22** (baseline lines 47-47). Manual anchor: from `.product-card__tag--halloween{border-color:#111111;color:#111111}` to `.product-card__tag--halloween{border-color:#111111;color:#111111}`.
Delete:
```css
.product-card__tag--halloween{border-color:#111111;color:#111111}
```

**Part 23** (baseline lines 49-49). Manual anchor: from `.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__...` to `.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__...`.
Delete:
```css
.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag::before{content:""!important;display:block!important;position:absolute!important;inset:auto!important;left:100%!important;top:50%!important;width:11px!important;height:1px!important;padding:0!important;border:0!important;border-radius:0!important;box-sizing:border-box!important;background:color-mix(in srgb,var(--dot) 58%,#d8dde5)!important;-webkit-mask:none!important;mask:none!important;clip-path:none!important;transform:translateY(-50%)!important;pointer-events:none!important;z-index:0!important}
```

**Part 24** (baseline lines 51-51). Manual anchor: from `html body .product-card__tag.product-card__tag.product-card__tag.product-card__tag.prod...` to `html body .product-card__tag.product-card__tag.product-card__tag.product-card__tag.prod...`.
Delete:
```css
html body .product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag{right:1px!important}
```

**Part 25** (baseline lines 55-55). Manual anchor: from `.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__...` to `.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__...`.
Delete:
```css
.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag::before{transform-origin:right center!important;transition:transform .26s cubic-bezier(.4,0,1,1) .12s,opacity .2s linear .12s!important}
```

**Part 26** (baseline lines 59-59). Manual anchor: from `.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__...` to `.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__...`.
Delete:
```css
  .product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag:hover{right:-9px!important;transition:right .42s cubic-bezier(.22,1,.36,1) .04s!important}
```

**Part 27** (baseline lines 60-60). Manual anchor: from `.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__...` to `.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__...`.
Delete:
```css
  .product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag:hover::before{transform:translateY(-50%) scaleX(0)!important;opacity:0!important;transition:transform .42s cubic-bezier(.22,1,.36,1) .04s,opacity .2s ease-out .04s!important}
```

**Part 28** (baseline lines 61-61). Manual anchor: from `.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__...` to `.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__...`.
Delete:
```css
  .product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag:hover::after{transform:translateY(-50%) translateX(-10px)!important;transition:transform .2s cubic-bezier(.22,1,.36,1) .2s,opacity .2s ease-out .2s!important}
```

**Part 29** (baseline lines 66-66). Manual anchor: from `.product-card__sold-badge{position:absolute;top:10px;left:10px;background:rgba(0,0,0,0....` to `.product-card__sold-badge{position:absolute;top:10px;left:10px;background:rgba(0,0,0,0....`.
Delete:
```css
.product-card__sold-badge{position:absolute;top:10px;left:10px;background:rgba(0,0,0,0.65);color:#fff;font-size:11px;font-weight:600;padding:3px 8px;border-radius:20px;z-index:3}
```

**Part 30** (baseline lines 68-68). Manual anchor: from `.product-card__vendor{font-size:11px;color:#999;font-weight:400;line-height:1.2}` to `.product-card__vendor{font-size:11px;color:#999;font-weight:400;line-height:1.2}`.
Delete:
```css
.product-card__vendor{font-size:11px;color:#999;font-weight:400;line-height:1.2}
```

**Part 31** (baseline lines 70-70). Manual anchor: from `.product-card__title--two{white-space:normal!important;height:36px!important;overflow:h...` to `.product-card__title--two{white-space:normal!important;height:36px!important;overflow:h...`.
Delete:
```css
.product-card__title--two{white-space:normal!important;height:36px!important;overflow:hidden!important;text-overflow:clip!important}
```

**Part 32** (baseline lines 72-72). Manual anchor: from `.product-card__stars{display:flex;align-items:center;gap:1px;height:16px;flex-shrink:0}` to `.product-card__stars{display:flex;align-items:center;gap:1px;height:16px;flex-shrink:0}`.
Delete:
```css
.product-card__stars{display:flex;align-items:center;gap:1px;height:16px;flex-shrink:0}
```

**Part 33** (baseline lines 74-74). Manual anchor: from `.product-card__jdgm .jdgm-prev-badge{display:inline-flex !important;align-items:center ...` to `.product-card__jdgm .jdgm-prev-badge{display:inline-flex !important;align-items:center ...`.
Delete:
```css
.product-card__jdgm .jdgm-prev-badge{display:inline-flex !important;align-items:center !important;gap:1px !important;font-size:0 !important;}
```

**Part 34** (baseline lines 75-75). Manual anchor: from `.product-card__jdgm .jdgm-prev-badge__stars{font-size:11px !important;}` to `.product-card__jdgm .jdgm-prev-badge__stars{font-size:11px !important;}`.
Delete:
```css
.product-card__jdgm .jdgm-prev-badge__stars{font-size:11px !important;}
```

**Part 35** (baseline lines 76-76). Manual anchor: from `.product-card__jdgm .jdgm-prev-badge__count{font-size:11px !important;color:#999 !impor...` to `.product-card__jdgm .jdgm-prev-badge__count{font-size:11px !important;color:#999 !impor...`.
Delete:
```css
.product-card__jdgm .jdgm-prev-badge__count{font-size:11px !important;color:#999 !important;margin-left:3px !important;}
```

**Part 36** (baseline lines 80-86). Manual anchor: from `.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__...` to `}`.
Delete:
```css
.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag {
  width: 24.15px !important;
  min-width: 24.15px !important;
  max-width: 24.15px !important;
  height: 24.15px !important;
  right: 2px !important;
}
```

**Part 37** (baseline lines 117-117). Manual anchor: from `.var-dot__count { font-size:9px; font-weight:800; line-height:1; letter-spacing:0; }` to `.var-dot__count { font-size:9px; font-weight:800; line-height:1; letter-spacing:0; }`.
Delete:
```css
.var-dot__count { font-size:9px; font-weight:800; line-height:1; letter-spacing:0; }
```

**Part 38** (baseline lines 118-118). Manual anchor: from `.var-dot__label { font-size:5px; font-weight:700; line-height:1; letter-spacing:0; text...` to `.var-dot__label { font-size:5px; font-weight:700; line-height:1; letter-spacing:0; text...`.
Delete:
```css
.var-dot__label { font-size:5px; font-weight:700; line-height:1; letter-spacing:0; text-transform:lowercase; }
```

### T103 [REVIEW] 1 orphaned rule(s) inside <style> blocks of snippets/product-description-card.liquid (classes no markup or script uses)
- **File:** `snippets/product-description-card.liquid` | baseline lines 32-32 | kind: orphan selectors in inline CSS (scripted, conservative)
- **Why it is dead:** Every selector of each rule needs a class or ID that appears nowhere in the theme outside CSS: not in any HTML/Liquid markup, JS file, inline script or JSON (any mention, even in a string, counts as used; prefix-built names like x--{{ }} count as used; Shopify/app prefixes count as used; classes inside :not()/:is()/:where()/:has() are ignored). Selectors: .pdc__label
- **Proof:** Scripted full-text search over all 119 theme files with <style> CSS removed. Only rules on lines of pure CSS without Liquid were considered. Joint Chrome check per file (CSS views): exactly these rules removed, nothing added. Not proven from CSS alone (an app or admin content could use a class), hence REVIEW.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .pdc__label { display: none !important; }**
- **Visual change if removed:** None expected.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 32-32). Manual anchor: from `.pdc__label { display:none !important; }` to `.pdc__label { display:none !important; }`.
Delete:
```css
  .pdc__label { display:none !important; }
```

### T104 [REVIEW] 2 orphaned rule(s) inside <style> blocks of snippets/product-recommendations.liquid (classes no markup or script uses)
- **File:** `snippets/product-recommendations.liquid` | baseline lines 18-18, 19-19 | kind: orphan selectors in inline CSS (scripted, conservative)
- **Why it is dead:** Every selector of each rule needs a class or ID that appears nowhere in the theme outside CSS: not in any HTML/Liquid markup, JS file, inline script or JSON (any mention, even in a string, counts as used; prefix-built names like x--{{ }} count as used; Shopify/app prefixes count as used; classes inside :not()/:is()/:where()/:has() are ignored). Selectors: #product-recs-grid .rec-card__kicker; #product-recs-grid .rec-card__read
- **Proof:** Scripted full-text search over all 119 theme files with <style> CSS removed. Only rules on lines of pure CSS without Liquid were considered. Joint Chrome check per file (CSS views): exactly these rules removed, nothing added. Not proven from CSS alone (an app or admin content could use a class), hence REVIEW.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: #product-recs-grid .rec-card__kicker { font-size: 0.72rem; font-weight: 600; color: rgb(138, 138, 153); } /   - removed: #product-recs-grid .rec-card__read { font-size: 0.78rem; font-weight: 600; color: rgb(107, 107, 123); text-decoration: none; }**
- **Visual change if removed:** None expected.
- **Parts:** 2 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 18-18). Manual anchor: from `#product-recs-grid .rec-card__kicker { font-size:0.72rem; font-weight:600; color:#8a8a9...` to `#product-recs-grid .rec-card__kicker { font-size:0.72rem; font-weight:600; color:#8a8a9...`.
Delete:
```css
#product-recs-grid .rec-card__kicker { font-size:0.72rem; font-weight:600; color:#8a8a99; }
```

**Part 2** (baseline lines 19-19). Manual anchor: from `#product-recs-grid .rec-card__read { font-size:0.78rem; font-weight:600; color:#6b6b7b;...` to `#product-recs-grid .rec-card__read { font-size:0.78rem; font-weight:600; color:#6b6b7b;...`.
Delete:
```css
#product-recs-grid .rec-card__read { font-size:0.78rem; font-weight:600; color:#6b6b7b; text-decoration:none; }
```

### T105 [REVIEW] 8 orphaned rule(s) inside <style> blocks of templates/page.liquid (classes no markup or script uses)
- **File:** `templates/page.liquid` | baseline lines 17-17, 18-18, 61-61, 62-62, 63-63, 69-69, 70-70, 71-71 | kind: orphan selectors in inline CSS (scripted, conservative)
- **Why it is dead:** Every selector of each rule needs a class or ID that appears nowhere in the theme outside CSS: not in any HTML/Liquid markup, JS file, inline script or JSON (any mention, even in a string, counts as used; prefix-built names like x--{{ }} count as used; Shopify/app prefixes count as used; classes inside :not()/:is()/:where()/:has() are ignored). Selectors: .contact-hero__title; .newsletter__social-link; .newsletter__social-link svg; .newsletter__socials; h1.contact-hero__title
- **Proof:** Scripted full-text search over all 119 theme files with <style> CSS removed. Only rules on lines of pure CSS without Liquid were considered. Joint Chrome check per file (CSS views): exactly these rules removed, nothing added. Not proven from CSS alone (an app or admin content could use a class), hence REVIEW.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .contact-hero__title { text-align: center !important; } /   - removed: h1.contact-hero__title { text-align: center !important; } /   - removed: .newsletter__socials { gap: 20px !important; margin-bottom: 0px !important; } /   - removed: .newsletter__social-link { width: 68px !important; height: 68px !important; border-radius: 50% !important; display: flex !important; align-items: center !important; justify-content: center !important; } /   - removed: .newsletter__social-link svg { width: 36px !important; height: 36px !important; } /   - removed: @media (max-width: 767px) > .newsletter__social-link { width: 56px !important; height: 56px !important; } /   - removed: @media (max-width: 767px) > .newsletter__social-link svg { width: 28px !important; height: 28px !important; } /   - removed: @media (max-width: 767px) > .newsletter__socials { gap: 12px !important; }**
- **Visual change if removed:** None expected.
- **Parts:** 8 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 17-17). Manual anchor: from `.contact-hero__title { text-align: center !important; }` to `.contact-hero__title { text-align: center !important; }`.
This text also exists elsewhere in the file, so it is located by the neighbouring lines (kept, not deleted): before = `(none)`, after = `h1.contact-hero__title { text-align: center !important; }`.
Delete:
```css
.contact-hero__title { text-align: center !important; }
```

**Part 2** (baseline lines 18-18). Manual anchor: from `h1.contact-hero__title { text-align: center !important; }` to `h1.contact-hero__title { text-align: center !important; }`.
Delete:
```css
h1.contact-hero__title { text-align: center !important; }
```

**Part 3** (baseline lines 61-61). Manual anchor: from `.newsletter__socials { gap: 20px !important; margin-bottom: 0 !important; }` to `.newsletter__socials { gap: 20px !important; margin-bottom: 0 !important; }`.
Delete:
```css
.newsletter__socials { gap: 20px !important; margin-bottom: 0 !important; }
```

**Part 4** (baseline lines 62-62). Manual anchor: from `.newsletter__social-link { width: 68px !important; height: 68px !important; border-radi...` to `.newsletter__social-link { width: 68px !important; height: 68px !important; border-radi...`.
Delete:
```css
.newsletter__social-link { width: 68px !important; height: 68px !important; border-radius: 50% !important; display: flex !important; align-items: center !important; justify-content: center !important; }
```

**Part 5** (baseline lines 63-63). Manual anchor: from `.newsletter__social-link svg { width: 36px !important; height: 36px !important; }` to `.newsletter__social-link svg { width: 36px !important; height: 36px !important; }`.
Delete:
```css
.newsletter__social-link svg { width: 36px !important; height: 36px !important; }
```

**Part 6** (baseline lines 69-69). Manual anchor: from `.newsletter__social-link { width: 56px !important; height: 56px !important; }` to `.newsletter__social-link { width: 56px !important; height: 56px !important; }`.
Delete:
```css
  .newsletter__social-link { width: 56px !important; height: 56px !important; }
```

**Part 7** (baseline lines 70-70). Manual anchor: from `.newsletter__social-link svg { width: 28px !important; height: 28px !important; }` to `.newsletter__social-link svg { width: 28px !important; height: 28px !important; }`.
Delete:
```css
  .newsletter__social-link svg { width: 28px !important; height: 28px !important; }
```

**Part 8** (baseline lines 71-71). Manual anchor: from `.newsletter__socials { gap: 12px !important; }` to `.newsletter__socials { gap: 12px !important; }`.
Delete:
```css
  .newsletter__socials { gap: 12px !important; }
```

### T106 [REVIEW] 6 orphaned rule(s) inside <style> blocks of templates/page.wishlist.liquid (classes no markup or script uses)
- **File:** `templates/page.wishlist.liquid` | baseline lines 10-10, 13-13, 14-14, 15-15, 16-16, 20-20 | kind: orphan selectors in inline CSS (scripted, conservative)
- **Why it is dead:** Every selector of each rule needs a class or ID that appears nowhere in the theme outside CSS: not in any HTML/Liquid markup, JS file, inline script or JSON (any mention, even in a string, counts as used; prefix-built names like x--{{ }} count as used; Shopify/app prefixes count as used; classes inside :not()/:is()/:where()/:has() are ignored). Selectors: #tlv-wlp .tlv-wlp__card a.tlv-wlp__t,#tlv-wlp .tlv-wlp__card a.tlv-wlp__t:visited; .tlv-wlp__b; .tlv-wlp__card .pc-price-row; .tlv-wlp__card img; .tlv-wlp__grid; .tlv-wlp__t
- **Proof:** Scripted full-text search over all 119 theme files with <style> CSS removed. Only rules on lines of pure CSS without Liquid were considered. Joint Chrome check per file (CSS views): exactly these rules removed, nothing added. Not proven from CSS alone (an app or admin content could use a class), hence REVIEW.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .tlv-wlp__grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; } /   - removed: .tlv-wlp__card img { width: 100%; aspect-ratio: 1 / 1; object-fit: contain; background: rgb(247, 247, 249); display: block; } /   - removed: .tlv-wlp__b { padding: 9px 11px 12px; } /   - removed: .tlv-wlp__t { font-size: 13px; font-weight: 600; color: rgb(26, 26, 46); text-decoration: none; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; min-height: 34px; } /   - removed: .tlv-wlp__card .pc-price-row { margin-top: 4px; } /   - removed: #tlv-wlp .tlv-wlp__card a.tlv-wlp__t, #tlv-wlp .tlv-wlp__card a.tlv-wlp__t:visited { color: rgb(26, 26, 46) !important; -webkit-text-fill-color: rgb(26, 26, 46) !important; }**
- **Visual change if removed:** None expected.
- **Parts:** 6 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 10-10). Manual anchor: from `.tlv-wlp__grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}` to `.tlv-wlp__grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}`.
Delete:
```css
.tlv-wlp__grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}
```

**Part 2** (baseline lines 13-13). Manual anchor: from `.tlv-wlp__card img{width:100%;aspect-ratio:1;object-fit:contain;background:#f7f7f9;disp...` to `.tlv-wlp__card img{width:100%;aspect-ratio:1;object-fit:contain;background:#f7f7f9;disp...`.
Delete:
```css
.tlv-wlp__card img{width:100%;aspect-ratio:1;object-fit:contain;background:#f7f7f9;display:block}
```

**Part 3** (baseline lines 14-14). Manual anchor: from `.tlv-wlp__b{padding:9px 11px 12px}` to `.tlv-wlp__b{padding:9px 11px 12px}`.
Delete:
```css
.tlv-wlp__b{padding:9px 11px 12px}
```

**Part 4** (baseline lines 15-15). Manual anchor: from `.tlv-wlp__t{font-size:13px;font-weight:600;color:#1a1a2e;text-decoration:none;display:-...` to `.tlv-wlp__t{font-size:13px;font-weight:600;color:#1a1a2e;text-decoration:none;display:-...`.
Delete:
```css
.tlv-wlp__t{font-size:13px;font-weight:600;color:#1a1a2e;text-decoration:none;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;min-height:34px}
```

**Part 5** (baseline lines 16-16). Manual anchor: from `.tlv-wlp__card .pc-price-row{margin-top:4px}` to `.tlv-wlp__card .pc-price-row{margin-top:4px}`.
Delete:
```css
.tlv-wlp__card .pc-price-row{margin-top:4px}
```

**Part 6** (baseline lines 20-20). Manual anchor: from `#tlv-wlp .tlv-wlp__card a.tlv-wlp__t,#tlv-wlp .tlv-wlp__card a.tlv-wlp__t:visited{color...` to `#tlv-wlp .tlv-wlp__card a.tlv-wlp__t,#tlv-wlp .tlv-wlp__card a.tlv-wlp__t:visited{color...`.
Delete:
```css
#tlv-wlp .tlv-wlp__card a.tlv-wlp__t,#tlv-wlp .tlv-wlp__card a.tlv-wlp__t:visited{color:#1a1a2e!important;-webkit-text-fill-color:#1a1a2e!important}
```

### T107 [REVIEW] 2 orphaned rule(s) inside minified/inline CSS of layout/theme.liquid
- **File:** `layout/theme.liquid` | baseline lines 1725-1725, 1725-1725 | kind: rule-level removal inside lines (exact text) - orphan selectors (scripted search)
- **Why it is dead:** Every selector of each rule needs a class/ID that appears nowhere in the theme outside CSS (markup, JS, JSON; any mention counts as used; prefix-built names count as used; Shopify/app prefixes count as used). Selectors: .tlv-sb-social-icon:hover; .tlv-sb-social-icon:hover svg
- **Proof:** Not provable from CSS alone, hence REVIEW; joint Chrome CSSOM check: exactly these rules removed, nothing added. These parts remove a single rule from the middle of a line: only the exact_text is removed, context is kept.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (hover: hover) > .tlv-sb-social-icon:hover { background: rgb(255, 66, 161); border-color: rgb(255, 66, 161); } /   - removed: @media (hover: hover) > .tlv-sb-social-icon:hover svg { stroke: rgb(255, 255, 255); }**
- **Visual change if removed:** None expected.
- **Parts:** 2 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 1725-1725). Manual anchor: from `.tlv-sb-social-icon:hover{background:#ff42a1;border-color:#ff42a1;}` to `.tlv-sb-social-icon:hover{background:#ff42a1;border-color:#ff42a1;}`.
Delete:
```css
.tlv-sb-social-icon:hover{background:#ff42a1;border-color:#ff42a1;}
```

**Part 2** (baseline lines 1725-1725). Manual anchor: from `.tlv-sb-social-icon:hover svg{stroke:#fff;}` to `.tlv-sb-social-icon:hover svg{stroke:#fff;}`.
Delete:
```css
.tlv-sb-social-icon:hover svg{stroke:#fff;}
```

### T108 [TODO] 3 always-overridden or empty rule(s) inside minified/inline CSS of sections/category-rows.liquid
- **File:** `sections/category-rows.liquid` | baseline lines 97-109, 9072-9072, 9191-9191 | kind: rule-level removal inside lines (exact text) - always overridden (tool-proven)
- **Why it is dead:** Each removed rule is restated later in the SAME <style> block (same selectors, same or top-level @media, every property at equal-or-higher priority, winner not inside a Liquid conditional), or is empty. Selectors: .cat-rows__row; html body #MainContent .cat-rows__row + .cat-rows__row; html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .cat-rows__row
- **Proof:** Joint shadow proof per file on the CSS views (tools/shadow.js) -> PROVEN; joint Chrome CSSOM check: exactly these rules removed, nothing added. These parts remove a single rule from the middle of a line: only the exact_text is removed, context is kept.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .cat-rows__row {  } /   - removed: @media (max-width: 1199px) > html body #MainContent .cat-rows__row + .cat-rows__row {  } /   - removed: html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .cat-rows__row {  }**
- **Visual change if removed:** None.
- **Parts:** 3 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 97-109). Manual anchor: from `.cat-rows__row {` to `}`.
Delete:
```css
.cat-rows__row {











}
```

**Part 2** (baseline lines 9072-9072). Manual anchor: from `html body #MainContent .cat-rows__row + .cat-rows__row{}` to `html body #MainContent .cat-rows__row + .cat-rows__row{}`.
Delete:
```css
html body #MainContent .cat-rows__row + .cat-rows__row{}
```

**Part 3** (baseline lines 9191-9191). Manual anchor: from `html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#Main...` to `html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#Main...`.
Delete:
```css
html body #MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent#MainContent .cat-rows__row{}
```

### T109 [REVIEW] 4 orphaned rule(s) inside minified/inline CSS of sections/category-rows.liquid
- **File:** `sections/category-rows.liquid` | baseline lines 7881-7881, 7881-7881, 7941-7941, 7941-7941 | kind: rule-level removal inside lines (exact text) - orphan selectors (scripted search)
- **Why it is dead:** Every selector of each rule needs a class/ID that appears nowhere in the theme outside CSS (markup, JS, JSON; any mention counts as used; prefix-built names count as used; Shopify/app prefixes count as used). Selectors: .cat-rows__scroll.is-hinting; .cat-rows__scroll.is-hinting .cr-card, .cat-rows__scroll.is-hinting .cr-card *; .hw-glitch; .hw-glitch, .hw-glitch::after
- **Proof:** Not provable from CSS alone, hence REVIEW; joint Chrome CSSOM check: exactly these rules removed, nothing added. These parts remove a single rule from the middle of a line: only the exact_text is removed, context is kept.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .cat-rows__scroll.is-hinting { scroll-snap-type: none !important; } /   - removed: .cat-rows__scroll.is-hinting .cr-card, .cat-rows__scroll.is-hinting .cr-card * { transition: none !important; animation-play-state: paused !important; } /   - removed: @media (prefers-reduced-motion: reduce) > .hw-glitch, .hw-glitch::after { animation: auto ease 0s 1 normal none running none; } /   - removed: @media (prefers-reduced-motion: reduce) > .hw-glitch { color: rgb(255, 66, 161); }**
- **Visual change if removed:** None expected.
- **Parts:** 4 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 7881-7881). Manual anchor: from `.cat-rows__scroll.is-hinting{scroll-snap-type:none!important}` to `.cat-rows__scroll.is-hinting{scroll-snap-type:none!important}`.
Delete:
```css
.cat-rows__scroll.is-hinting{scroll-snap-type:none!important}
```

**Part 2** (baseline lines 7881-7881). Manual anchor: from `.cat-rows__scroll.is-hinting .cr-card,.cat-rows__scroll.is-hinting .cr-card *{transitio...` to `.cat-rows__scroll.is-hinting .cr-card,.cat-rows__scroll.is-hinting .cr-card *{transitio...`.
Delete:
```css
.cat-rows__scroll.is-hinting .cr-card,.cat-rows__scroll.is-hinting .cr-card *{transition:none!important;animation-play-state:paused!important}
```

**Part 3** (baseline lines 7941-7941). Manual anchor: from `.hw-glitch,.hw-glitch::after{animation:none}` to `.hw-glitch,.hw-glitch::after{animation:none}`.
Delete:
```css
.hw-glitch,.hw-glitch::after{animation:none}
```

**Part 4** (baseline lines 7941-7941). Manual anchor: from `.hw-glitch{color:#ff42a1}` to `.hw-glitch{color:#ff42a1}`.
Delete:
```css
.hw-glitch{color:#ff42a1}
```

### T110 [TODO] 6 always-overridden or empty rule(s) inside minified/inline CSS of sections/clg-hero.liquid
- **File:** `sections/clg-hero.liquid` | baseline lines 1063-1063, 4585-4585, 4585-4585, 4585-4585, 4586-4586, 4586-4586 | kind: rule-level removal inside lines (exact text) - always overridden (tool-proven)
- **Why it is dead:** Each removed rule is restated later in the SAME <style> block (same selectors, same or top-level @media, every property at equal-or-higher priority, winner not inside a Liquid conditional), or is empty. Selectors: .cat-strip; .cat-strip__inner; .cat-strip__inner .cat-pill; .cat-strip__inner .cat-pill svg; .drift-strip
- **Proof:** Joint shadow proof per file on the CSS views (tools/shadow.js) -> PROVEN; joint Chrome CSSOM check: exactly these rules removed, nothing added. These parts remove a single rule from the middle of a line: only the exact_text is removed, context is kept.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (min-width: 1200px) > .drift-strip {  } /   - removed: @media (min-width: 721px) > .cat-strip { overflow: visible !important; } /   - removed: @media (min-width: 721px) > .cat-strip__inner .cat-pill { font-size: 9px !important; padding: 0.38rem 0.42rem !important; gap: 0.2rem !important; } /   - removed: @media (min-width: 721px) > .cat-strip__inner .cat-pill svg { width: 13px !important; height: 13px !important; } /   - removed: @media (min-width: 721px) and (max-width: 1199px) > .cat-strip__inner { grid-template-columns: repeat(5, minmax(0px, 1fr)); display: grid !important; gap: 5px !important; } /   - removed: @media (min-width: 721px) and (max-width: 1199px) > .cat-strip__inner .cat-pill { width: 94% !important; justify-self: center !important; justify-content: center !important; box-sizing: border-box !important; }**
- **Visual change if removed:** None.
- **Parts:** 6 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 1063-1063). Manual anchor: from `.drift-strip { }` to `.drift-strip { }`.
Delete:
```css
.drift-strip { }
```

**Part 2** (baseline lines 4585-4585). Manual anchor: from `.cat-strip{overflow:visible!important}` to `.cat-strip{overflow:visible!important}`.
Delete:
```css
.cat-strip{overflow:visible!important}
```

**Part 3** (baseline lines 4585-4585). Manual anchor: from `.cat-strip__inner .cat-pill{font-size:9px!important;padding:.38rem .42rem!important;gap...` to `.cat-strip__inner .cat-pill{font-size:9px!important;padding:.38rem .42rem!important;gap...`.
Delete:
```css
.cat-strip__inner .cat-pill{font-size:9px!important;padding:.38rem .42rem!important;gap:.2rem!important}
```

**Part 4** (baseline lines 4585-4585). Manual anchor: from `.cat-strip__inner .cat-pill svg{width:13px!important;height:13px!important}` to `.cat-strip__inner .cat-pill svg{width:13px!important;height:13px!important}`.
Delete:
```css
.cat-strip__inner .cat-pill svg{width:13px!important;height:13px!important}
```

**Part 5** (baseline lines 4586-4586). Manual anchor: from `.cat-strip__inner{display:grid!important;grid-template-columns:repeat(5,minmax(0,1fr));...` to `.cat-strip__inner{display:grid!important;grid-template-columns:repeat(5,minmax(0,1fr));...`.
Delete:
```css
.cat-strip__inner{display:grid!important;grid-template-columns:repeat(5,minmax(0,1fr));gap:5px!important}
```

**Part 6** (baseline lines 4586-4586). Manual anchor: from `.cat-strip__inner .cat-pill{width:94%!important;justify-self:center!important;justify-c...` to `.cat-strip__inner .cat-pill{width:94%!important;justify-self:center!important;justify-c...`.
Delete:
```css
.cat-strip__inner .cat-pill{width:94%!important;justify-self:center!important;justify-content:center!important;box-sizing:border-box!important}
```

### T111 [TODO] 1 always-overridden or empty rule(s) inside minified/inline CSS of sections/product-main.liquid
- **File:** `sections/product-main.liquid` | baseline lines 2419-2419 | kind: rule-level removal inside lines (exact text) - always overridden (tool-proven)
- **Why it is dead:** Each removed rule is restated later in the SAME <style> block (same selectors, same or top-level @media, every property at equal-or-higher priority, winner not inside a Liquid conditional), or is empty. Selectors: .product-main__price
- **Proof:** Joint shadow proof per file on the CSS views (tools/shadow.js) -> PROVEN; joint Chrome CSSOM check: exactly these rules removed, nothing added. These parts remove a single rule from the middle of a line: only the exact_text is removed, context is kept.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (max-width: 767px) > .product-main__price { font-size: 23px !important; }**
- **Visual change if removed:** None.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 2419-2419). Manual anchor: from `.product-main__price { font-size:23px !important; }` to `.product-main__price { font-size:23px !important; }`.
Delete:
```css
.product-main__price { font-size:23px !important; }
```

### T112 [REVIEW] 1 orphaned rule(s) inside minified/inline CSS of sections/product-main.liquid
- **File:** `sections/product-main.liquid` | baseline lines 2566-2566 | kind: rule-level removal inside lines (exact text) - orphan selectors (scripted search)
- **Why it is dead:** Every selector of each rule needs a class/ID that appears nowhere in the theme outside CSS (markup, JS, JSON; any mention counts as used; prefix-built names count as used; Shopify/app prefixes count as used). Selectors: .product-stars
- **Proof:** Not provable from CSS alone, hence REVIEW; joint Chrome CSSOM check: exactly these rules removed, nothing added. These parts remove a single rule from the middle of a line: only the exact_text is removed, context is kept.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (max-width: 767px) > .product-stars { justify-content: center !important; width: 100% !important; }**
- **Visual change if removed:** None expected.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 2566-2566). Manual anchor: from `.product-stars { justify-content: center !important; width: 100% !important; }` to `.product-stars { justify-content: center !important; width: 100% !important; }`.
Delete:
```css
.product-stars { justify-content: center !important; width: 100% !important; }
```

### T113 [REVIEW] 7 orphaned rule(s) inside minified/inline CSS of snippets/collection-discovery-banners.liquid
- **File:** `snippets/collection-discovery-banners.liquid` | baseline lines 17-17, 17-17, 17-17, 17-17, 17-17, 18-18, 18-18 | kind: rule-level removal inside lines (exact text) - orphan selectors (scripted search)
- **Why it is dead:** Every selector of each rule needs a class/ID that appears nowhere in the theme outside CSS (markup, JS, JSON; any mention counts as used; prefix-built names count as used; Shopify/app prefixes count as used). Selectors: .collection-discovery--three; .collection-discovery--three .collection-discovery__copy; .collection-discovery--three .collection-discovery__link:nth-child(3); .collection-discovery--three .collection-discovery__link:nth-child(3) .collection-discovery__copy; .collection-discovery--three .collection-discovery__link:nth-child(3) .collection-discovery__description; .collection-discovery--three .collection-discovery__link:nth-child(3) .collection-discovery__title; .collection-discovery--three .collection-discovery__title
- **Proof:** Not provable from CSS alone, hence REVIEW; joint Chrome CSSOM check: exactly these rules removed, nothing added. These parts remove a single rule from the middle of a line: only the exact_text is removed, context is kept.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (min-width: 1200px) > .collection-discovery--three .collection-discovery__copy { width: 55%; padding: 20px; } /   - removed: @media (min-width: 1200px) > .collection-discovery--three .collection-discovery__title { font-size: clamp(20px, 1.9vw, 26px); } /   - removed: @media (min-width: 1200px) > .collection-discovery--three .collection-discovery__link:nth-child(3) .collection-discovery__copy { width: 39%; padding: 20px; } /   - removed: @media (min-width: 1200px) > .collection-discovery--three .collection-discovery__link:nth-child(3) .collection-discovery__title { font-size: clamp(17px, 1.45vw, 20px); } /   - removed: @media (min-width: 1200px) > .collection-discovery--three .collection-discovery__link:nth-child(3) .collection-discovery__description { font-size: 8px; letter-spacing: 0.06em; } /   - removed: @media (max-width: 1199px) > .collection-discovery--three { grid-template-columns: repeat(2, minmax(0px, 1fr)); } /   - removed: @media (max-width: 1199px) > .collection-discovery--three .collection-discovery__link:nth-child(3) { grid-column: 1 / -1; }**
- **Visual change if removed:** None expected.
- **Parts:** 7 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 17-17). Manual anchor: from `.collection-discovery--three .collection-discovery__copy{width:55%;padding:20px}` to `.collection-discovery--three .collection-discovery__copy{width:55%;padding:20px}`.
Delete:
```css
.collection-discovery--three .collection-discovery__copy{width:55%;padding:20px}
```

**Part 2** (baseline lines 17-17). Manual anchor: from `.collection-discovery--three .collection-discovery__title{font-size:clamp(20px,1.9vw,26...` to `.collection-discovery--three .collection-discovery__title{font-size:clamp(20px,1.9vw,26...`.
Delete:
```css
.collection-discovery--three .collection-discovery__title{font-size:clamp(20px,1.9vw,26px)}
```

**Part 3** (baseline lines 17-17). Manual anchor: from `.collection-discovery--three .collection-discovery__link:nth-child(3) .collection-disco...` to `.collection-discovery--three .collection-discovery__link:nth-child(3) .collection-disco...`.
Delete:
```css
.collection-discovery--three .collection-discovery__link:nth-child(3) .collection-discovery__copy{width:39%;padding:20px}
```

**Part 4** (baseline lines 17-17). Manual anchor: from `.collection-discovery--three .collection-discovery__link:nth-child(3) .collection-disco...` to `.collection-discovery--three .collection-discovery__link:nth-child(3) .collection-disco...`.
Delete:
```css
.collection-discovery--three .collection-discovery__link:nth-child(3) .collection-discovery__title{font-size:clamp(17px,1.45vw,20px)}
```

**Part 5** (baseline lines 17-17). Manual anchor: from `.collection-discovery--three .collection-discovery__link:nth-child(3) .collection-disco...` to `.collection-discovery--three .collection-discovery__link:nth-child(3) .collection-disco...`.
Delete:
```css
.collection-discovery--three .collection-discovery__link:nth-child(3) .collection-discovery__description{font-size:8px;letter-spacing:.06em}
```

**Part 6** (baseline lines 18-18). Manual anchor: from `.collection-discovery--three{grid-template-columns:repeat(2,minmax(0,1fr))}` to `.collection-discovery--three{grid-template-columns:repeat(2,minmax(0,1fr))}`.
Delete:
```css
.collection-discovery--three{grid-template-columns:repeat(2,minmax(0,1fr))}
```

**Part 7** (baseline lines 18-18). Manual anchor: from `.collection-discovery--three .collection-discovery__link:nth-child(3){grid-column:1/-1}` to `.collection-discovery--three .collection-discovery__link:nth-child(3){grid-column:1/-1}`.
Delete:
```css
.collection-discovery--three .collection-discovery__link:nth-child(3){grid-column:1/-1}
```

### T114 [TODO] 1 always-overridden or empty rule(s) inside minified/inline CSS of snippets/cr-card-styles.liquid
- **File:** `snippets/cr-card-styles.liquid` | baseline lines 105-105 | kind: rule-level removal inside lines (exact text) - always overridden (tool-proven)
- **Why it is dead:** Each removed rule is restated later in the SAME <style> block (same selectors, same or top-level @media, every property at equal-or-higher priority, winner not inside a Liquid conditional), or is empty. Selectors: .cr-card__tag.cr-card__tag.cr-card__tag.cr-card__tag:hover::after, .age-dot.age-dot.age-dot:hover::after
- **Proof:** Joint shadow proof per file on the CSS views (tools/shadow.js) -> PROVEN; joint Chrome CSSOM check: exactly these rules removed, nothing added. These parts remove a single rule from the middle of a line: only the exact_text is removed, context is kept.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (hover: hover) > .cr-card__tag.cr-card__tag.cr-card__tag.cr-card__tag:hover::after, .age-dot.age-dot.age-dot:hover::after { transform: translateY(0px); opacity: 1; transition: transform 0.42s cubic-bezier(0.16, 1, 0.3, 1) 0.05s, opacity 0.15s 0.05s; }**
- **Visual change if removed:** None.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 105-105). Manual anchor: from `.cr-card__tag.cr-card__tag.cr-card__tag.cr-card__tag:hover::after,.age-dot.age-dot.age-...` to `.cr-card__tag.cr-card__tag.cr-card__tag.cr-card__tag:hover::after,.age-dot.age-dot.age-...`.
Delete:
```css
.cr-card__tag.cr-card__tag.cr-card__tag.cr-card__tag:hover::after,.age-dot.age-dot.age-dot:hover::after{transform:translateY(0);opacity:1;transition:transform .42s cubic-bezier(.16,1,.3,1) .05s,opacity .15s ease .05s}
```

### T115 [TODO] 1 always-overridden or empty rule(s) inside minified/inline CSS of snippets/product-card-styles.liquid
- **File:** `snippets/product-card-styles.liquid` | baseline lines 36-36 | kind: rule-level removal inside lines (exact text) - always overridden (tool-proven)
- **Why it is dead:** Each removed rule is restated later in the SAME <style> block (same selectors, same or top-level @media, every property at equal-or-higher priority, winner not inside a Liquid conditional), or is empty. Selectors: .product-card__tag.product-card__tag.product-card__tag.product-card__tag:hover::after, .age-dot.age-dot.age-dot:hover::after
- **Proof:** Joint shadow proof per file on the CSS views (tools/shadow.js) -> PROVEN; joint Chrome CSSOM check: exactly these rules removed, nothing added. These parts remove a single rule from the middle of a line: only the exact_text is removed, context is kept.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (hover: hover) > .product-card__tag.product-card__tag.product-card__tag.product-card__tag:hover::after, .age-dot.age-dot.age-dot:hover::after { transform: translateY(0px); opacity: 1; transition: transform 0.42s cubic-bezier(0.16, 1, 0.3, 1) 0.05s, opacity 0.15s 0.05s; }**
- **Visual change if removed:** None.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 36-36). Manual anchor: from `.product-card__tag.product-card__tag.product-card__tag.product-card__tag:hover::after,....` to `.product-card__tag.product-card__tag.product-card__tag.product-card__tag:hover::after,....`.
Delete:
```css
.product-card__tag.product-card__tag.product-card__tag.product-card__tag:hover::after,.age-dot.age-dot.age-dot:hover::after{transform:translateY(0);opacity:1;transition:transform .42s cubic-bezier(.16,1,.3,1) .05s,opacity .15s ease .05s}
```

### T116 [REVIEW] 21 orphaned rule(s) inside minified/inline CSS of snippets/product-card-styles.liquid
- **File:** `snippets/product-card-styles.liquid` | baseline lines 32-32, 32-32, 33-33, 33-33, 33-33, 33-33, 33-33, 33-33, 33-33, 33-33, 33-33, 33-33, 33-33, 33-33, 35-35, 37-37, 42-42, 42-42, 43-43, 43-43, 88-88 | kind: rule-level removal inside lines (exact text) - orphan selectors (scripted search)
- **Why it is dead:** Every selector of each rule needs a class/ID that appears nowhere in the theme outside CSS (markup, JS, JSON; any mention counts as used; prefix-built names count as used; Shopify/app prefixes count as used). Selectors: .age-dot ~ .product-card__tag.product-card__tag.product-card__tag; .age-dot ~ .product-card__tag.product-card__tag.product-card__tag.product-card__tag; .product-card__tag; .product-card__tag--blaster; .product-card__tag--building; .product-card__tag--collectible; .product-card__tag--fidget; .product-card__tag--halloween; .product-card__tag--keychain; .product-card__tag--plush; .product-card__tag--puzzle; .product-card__tag--rc; .product-card__tag--rc, .product-card__tag--puzzle, .product-card__tag--building; .product-card__tag.product-card__tag; .product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag; .product-card__tag.product-card__tag.product-card__tag.p
- **Proof:** Not provable from CSS alone, hence REVIEW; joint Chrome CSSOM check: exactly these rules removed, nothing added. These parts remove a single rule from the middle of a line: only the exact_text is removed, context is kept.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .product-card__tag { font-weight: 400 !important; } /   - removed: .product-card__tag--rc, .product-card__tag--puzzle, .product-card__tag--building { font-weight: 400 !important; } /   - removed: .product-card__tag.product-card__tag { --dot: #f97316; opacity: 0.85; cursor: default; top: 12px !important; left: auto !important; right: 12px !important; box-sizing: border-box !important; min-width: 8.4px !important; max-width: 8.4px !important; height: 8.4px !important; padding: 0px !important;  /   - removed: .product-card__tag.product-card__tag::before { display: none !important; } /   - removed: @media (hover: hover) > .product-card__tag.product-card__tag:hover { opacity: 1; max-width: 160px !important; height: 22px !important; padding: 0px 10px !important; font-size: 10.5px !important; background: var(--dot) !important; box-shadow: rgba(15, 23, 42, 0.18) 0px 4px 14px !important; } /   - removed: .product-card__tag--rc { --dot: #1d4ed8 !important; } /   - removed: .product-card__tag--halloween { --dot: #334155 !important; } /   - removed: .product-card__tag--collectible { --dot: #14b8a6 !important; } /   - removed: .product-card__tag--keychain { --dot: #22c55e !important; } /   - removed: .product-card__tag--blaster { --dot: #ef4444 !important; } /   - removed: .product-card__tag--puzzle { --dot: #f59e0b !important; } /   - removed: .product-card__tag--building { --dot: #84cc16 !important; } /   - removed: .product-card__tag--plush { --dot: #ec4899 !important; } /   - removed: .product-card__tag--fidget { --dot: #06b6d4 !important; } /   - removed: .age-dot ~ .product-card__tag.product-card__tag.product-card__tag { right: 18px !important; } /   - removed: .age-dot ~ .product-card__tag.product-card__tag.product-card__tag.product-card__tag { right: 4px !important; top: 21px !important; } /   - removed: .product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag { box-sizing: border-box !important; width: 25.15px !important; min-width: 25.15px !important; max-width: 25.15px !important; height: 25.15px !important; border: 8px solid transparent !import /   - removed: @media (hover: hover) > .product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag:hover { box-sizing: border-box !important; width: 25.15px !important; min-width: 25.15px !important; max-width: 25.15px !important; height: 25.15px !important; border: /   - removed: .product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag { background: transparent !important; box-shadow: inset 0 0 0 1.5px color-mix(in srgb,var(--dot) 70%,#fff) !important; } /   - removed: @media (hover: hover) > .product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag:hover { background: transparent !important; box-shadow: inset 0 0 0 1.5px color-mix(in srgb,var(--dot) 70%,#fff) !important; } /   - removed: @media (hover: hover) > .product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag:hover { transform: translateX(6px) !important; transition: transform 0.42s cubic-bezier(0.22, 1, 0.36, 1) 0.04s, right 0.42s cubic-bezier(0.22, 1, 0.**
- **Visual change if removed:** None expected.
- **Parts:** 21 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 32-32). Manual anchor: from `.product-card__tag{font-weight:400!important}` to `.product-card__tag{font-weight:400!important}`.
Delete:
```css
.product-card__tag{font-weight:400!important}
```

**Part 2** (baseline lines 32-32). Manual anchor: from `.product-card__tag--rc,.product-card__tag--puzzle,.product-card__tag--building{font-wei...` to `.product-card__tag--rc,.product-card__tag--puzzle,.product-card__tag--building{font-wei...`.
Delete:
```css
.product-card__tag--rc,.product-card__tag--puzzle,.product-card__tag--building{font-weight:400!important}
```

**Part 3** (baseline lines 33-33). Manual anchor: from `.product-card__tag.product-card__tag{--dot:#f97316;top:12px!important;left:auto!importa...` to `.product-card__tag.product-card__tag{--dot:#f97316;top:12px!important;left:auto!importa...`.
Delete:
```css
.product-card__tag.product-card__tag{--dot:#f97316;top:12px!important;left:auto!important;right:12px!important;box-sizing:border-box!important;min-width:8.4px!important;max-width:8.4px!important;height:8.4px!important;padding:0!important;border:0 solid transparent!important;border-radius:999px!important;background:color-mix(in srgb,var(--dot) 45%,#fff)!important;background-image:none!important;-webkit-background-clip:border-box!important;background-clip:border-box!important;color:#fff!important;-webkit-text-fill-color:#fff!important;font-size:0!important;font-weight:600!important;letter-spacing:.02em!important;line-height:1!important;white-space:nowrap!important;overflow:hidden!important;display:inline-flex!important;align-items:center!important;box-shadow:none!important;opacity:.85;pointer-events:auto!important;cursor:default;transition:max-width .28s cubic-bezier(.2,.8,.2,1),height .22s ease,padding .22s ease,font-size .18s ease!important;z-index:4!important}
```

**Part 4** (baseline lines 33-33). Manual anchor: from `.product-card__tag.product-card__tag::before{display:none!important}` to `.product-card__tag.product-card__tag::before{display:none!important}`.
Delete:
```css
.product-card__tag.product-card__tag::before{display:none!important}
```

**Part 5** (baseline lines 33-33). Manual anchor: from `.product-card__tag.product-card__tag:hover{max-width:160px!important;height:22px!import...` to `.product-card__tag.product-card__tag:hover{max-width:160px!important;height:22px!import...`.
Delete:
```css
.product-card__tag.product-card__tag:hover{max-width:160px!important;height:22px!important;padding:0 10px!important;font-size:10.5px!important;background:var(--dot)!important;opacity:1;box-shadow:0 4px 14px rgba(15,23,42,.18)!important}
```

**Part 6** (baseline lines 33-33). Manual anchor: from `.product-card__tag--rc{--dot:#1d4ed8!important}` to `.product-card__tag--rc{--dot:#1d4ed8!important}`.
Delete:
```css
.product-card__tag--rc{--dot:#1d4ed8!important}
```

**Part 7** (baseline lines 33-33). Manual anchor: from `.product-card__tag--halloween{--dot:#334155!important}` to `.product-card__tag--halloween{--dot:#334155!important}`.
Delete:
```css
.product-card__tag--halloween{--dot:#334155!important}
```

**Part 8** (baseline lines 33-33). Manual anchor: from `.product-card__tag--collectible{--dot:#14b8a6!important}` to `.product-card__tag--collectible{--dot:#14b8a6!important}`.
Delete:
```css
.product-card__tag--collectible{--dot:#14b8a6!important}
```

**Part 9** (baseline lines 33-33). Manual anchor: from `.product-card__tag--keychain{--dot:#22c55e!important}` to `.product-card__tag--keychain{--dot:#22c55e!important}`.
Delete:
```css
.product-card__tag--keychain{--dot:#22c55e!important}
```

**Part 10** (baseline lines 33-33). Manual anchor: from `.product-card__tag--blaster{--dot:#ef4444!important}` to `.product-card__tag--blaster{--dot:#ef4444!important}`.
Delete:
```css
.product-card__tag--blaster{--dot:#ef4444!important}
```

**Part 11** (baseline lines 33-33). Manual anchor: from `.product-card__tag--puzzle{--dot:#f59e0b!important}` to `.product-card__tag--puzzle{--dot:#f59e0b!important}`.
Delete:
```css
.product-card__tag--puzzle{--dot:#f59e0b!important}
```

**Part 12** (baseline lines 33-33). Manual anchor: from `.product-card__tag--building{--dot:#84cc16!important}` to `.product-card__tag--building{--dot:#84cc16!important}`.
Delete:
```css
.product-card__tag--building{--dot:#84cc16!important}
```

**Part 13** (baseline lines 33-33). Manual anchor: from `.product-card__tag--plush{--dot:#ec4899!important}` to `.product-card__tag--plush{--dot:#ec4899!important}`.
Delete:
```css
.product-card__tag--plush{--dot:#ec4899!important}
```

**Part 14** (baseline lines 33-33). Manual anchor: from `.product-card__tag--fidget{--dot:#06b6d4!important}` to `.product-card__tag--fidget{--dot:#06b6d4!important}`.
Delete:
```css
.product-card__tag--fidget{--dot:#06b6d4!important}
```

**Part 15** (baseline lines 35-35). Manual anchor: from `.age-dot~.product-card__tag.product-card__tag.product-card__tag{right:18px!important}` to `.age-dot~.product-card__tag.product-card__tag.product-card__tag{right:18px!important}`.
Delete:
```css
.age-dot~.product-card__tag.product-card__tag.product-card__tag{right:18px!important}
```

**Part 16** (baseline lines 37-37). Manual anchor: from `.age-dot~.product-card__tag.product-card__tag.product-card__tag.product-card__tag{right...` to `.age-dot~.product-card__tag.product-card__tag.product-card__tag.product-card__tag{right...`.
Delete:
```css
.age-dot~.product-card__tag.product-card__tag.product-card__tag.product-card__tag{right:4px!important;top:21px!important}
```

**Part 17** (baseline lines 42-42). Manual anchor: from `.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__...` to `.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__...`.
Delete:
```css
.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag{box-sizing:border-box!important;width:25.15px!important;min-width:25.15px!important;max-width:25.15px!important;height:25.15px!important;border:8px solid transparent!important;padding:0!important;background:color-mix(in srgb,var(--dot) 50%,#fff)!important;background-clip:padding-box!important;opacity:1!important;box-shadow:none!important}
```

**Part 18** (baseline lines 42-42). Manual anchor: from `.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__...` to `.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__...`.
Delete:
```css
.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag:hover{box-sizing:border-box!important;width:25.15px!important;min-width:25.15px!important;max-width:25.15px!important;height:25.15px!important;border:8px solid transparent!important;padding:0!important;background:color-mix(in srgb,var(--dot) 50%,#fff)!important;background-clip:padding-box!important;opacity:1!important;box-shadow:none!important}
```

**Part 19** (baseline lines 43-43). Manual anchor: from `.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__...` to `.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__...`.
Delete:
```css
.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag{background:transparent!important;box-shadow:inset 0 0 0 1.5px color-mix(in srgb,var(--dot) 70%,#fff)!important}
```

**Part 20** (baseline lines 43-43). Manual anchor: from `.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__...` to `.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__...`.
Delete:
```css
.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag:hover{background:transparent!important;box-shadow:inset 0 0 0 1.5px color-mix(in srgb,var(--dot) 70%,#fff)!important}
```

**Part 21** (baseline lines 88-88). Manual anchor: from `.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__...` to `.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__...`.
Delete:
```css
.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag.product-card__tag:hover{transform:translateX(6px)!important;transition:transform .42s cubic-bezier(.22,1,.36,1) .04s,right .42s cubic-bezier(.22,1,.36,1) .04s!important}
```

### T117 [REVIEW] 2 orphaned rule(s) inside minified/inline CSS of snippets/product-description-card.liquid
- **File:** `snippets/product-description-card.liquid` | baseline lines 88-88, 88-88 | kind: rule-level removal inside lines (exact text) - orphan selectors (scripted search)
- **Why it is dead:** Every selector of each rule needs a class/ID that appears nowhere in the theme outside CSS (markup, JS, JSON; any mention counts as used; prefix-built names count as used; Shopify/app prefixes count as used). Selectors: .pdc-spec-icon--green; .pdc-spec-icon--green svg
- **Proof:** Not provable from CSS alone, hence REVIEW; joint Chrome CSSOM check: exactly these rules removed, nothing added. These parts remove a single rule from the middle of a line: only the exact_text is removed, context is kept.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: .pdc-spec-icon--green { background: rgb(236, 253, 245); } /   - removed: .pdc-spec-icon--green svg { stroke: rgb(5, 150, 105); }**
- **Visual change if removed:** None expected.
- **Parts:** 2 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 88-88). Manual anchor: from `.pdc-spec-icon--green { background:#ecfdf5; }` to `.pdc-spec-icon--green { background:#ecfdf5; }`.
Delete:
```css
.pdc-spec-icon--green  { background:#ecfdf5; }
```

**Part 2** (baseline lines 88-88). Manual anchor: from `.pdc-spec-icon--green svg { stroke:#059669; }` to `.pdc-spec-icon--green svg { stroke:#059669; }`.
Delete:
```css
.pdc-spec-icon--green  svg { stroke:#059669; }
```

### T118 [REVIEW] 1 orphaned rule(s) inside minified/inline CSS of snippets/product-recommendations.liquid
- **File:** `snippets/product-recommendations.liquid` | baseline lines 20-20 | kind: rule-level removal inside lines (exact text) - orphan selectors (scripted search)
- **Why it is dead:** Every selector of each rule needs a class/ID that appears nowhere in the theme outside CSS (markup, JS, JSON; any mention counts as used; prefix-built names count as used; Shopify/app prefixes count as used). Selectors: #product-recs-grid .rec-card--guide:hover .rec-card__read
- **Proof:** Not provable from CSS alone, hence REVIEW; joint Chrome CSSOM check: exactly these rules removed, nothing added. These parts remove a single rule from the middle of a line: only the exact_text is removed, context is kept.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (hover: hover) > #product-recs-grid .rec-card--guide:hover .rec-card__read { color: rgb(26, 26, 46); }**
- **Visual change if removed:** None expected.
- **Parts:** 1 (apply.py handles all parts of an item at once)

**Exact text** (baseline lines 20-20). Manual anchor: from `#product-recs-grid .rec-card--guide:hover .rec-card__read { color:#1a1a2e; }` to `#product-recs-grid .rec-card--guide:hover .rec-card__read { color:#1a1a2e; }`.
Delete:
```css
#product-recs-grid .rec-card--guide:hover .rec-card__read { color:#1a1a2e; }
```

### T119 [TODO] 22 always-overridden or empty rule(s) inside minified/inline CSS of snippets/tlv-orbs.liquid
- **File:** `snippets/tlv-orbs.liquid` | baseline lines 19-19, 20-20, 38-38, 129-129, 133-133, 134-134, 145-145, 152-152, 156-156, 156-156, 191-191, 196-196, 216-216, 219-219, 219-219, 282-282, 285-285, 285-285, 291-291, 291-291, 294-294, 294-294 | kind: rule-level removal inside lines (exact text) - always overridden (tool-proven)
- **Why it is dead:** Each removed rule is restated later in the SAME <style> block (same selectors, same or top-level @media, every property at equal-or-higher priority, winner not inside a Liquid conditional), or is empty. Selectors: .tlv-orb--has-subs .tlv-orb__subs; .tlv-orb--has-subs .tlv-orb__subs span; .tlv-orb--has-subs:hover .tlv-orb__wrap, .tlv-orb--has-subs:focus-within .tlv-orb__wrap; .tlv-orb:hover .tlv-orb__glow, .tlv-orb:focus-visible .tlv-orb__glow; .tlv-orb:hover .tlv-orb__glow::after, .tlv-orb:focus-visible .tlv-orb__glow::after, .tlv-orb:hover .tlv-orb__glow::before, .tlv-orb:focus-visible .tlv-orb__glow::before; .tlv-orb:hover .tlv-orb__glow::before, .tlv-orb:focus-visible .tlv-orb__glow::before; .tlv-orb:hover .tlv-orb__glow::before, .tlv-orb:focus-visible .tlv-orb__glow::before, .tlv-orb:hover .tlv-orb__glow::after, .tlv-orb:focus-visible .tlv-orb__glow::after; .tlv-orb:hover .tlv-orb__wrap::after, .t
- **Proof:** Joint shadow proof per file on the CSS views (tools/shadow.js) -> PROVEN; joint Chrome CSSOM check: exactly these rules removed, nothing added. These parts remove a single rule from the middle of a line: only the exact_text is removed, context is kept.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (hover: hover) > .tlv-orb--has-subs:hover .tlv-orb__wrap, .tlv-orb--has-subs:focus-within .tlv-orb__wrap { transform: translate3d(-34px, 0px, 0px); } /   - removed: @media (max-width: 767px) > .tlv-orb--has-subs .tlv-orb__subs { display: none; } /   - removed: @media (prefers-reduced-motion: reduce) > .tlv-orb--has-subs .tlv-orb__subs span { transition: none; } /   - removed: @media (prefers-reduced-motion: reduce) > .tlv-orb__glow::after { transition: none; } /   - removed: @media (hover: hover) > .tlv-orb:hover .tlv-orb__wrap::before, .tlv-orb:focus-visible .tlv-orb__wrap::before { opacity: 1; transform: translateX(-50%) scaleY(1); } /   - removed: @media (prefers-reduced-motion: reduce) > .tlv-orb__wrap::before { transition: none; } /   - removed: @media (min-width: 768px) and (max-width: 1024px) > .tlv-orb__wrap { width: clamp(72px, 13vw, 96px); } /   - removed: @media (hover: hover) > .tlv-orb:hover .tlv-orb__wrap::before, .tlv-orb:focus-visible .tlv-orb__wrap::before { transform: translateX(-50%) rotate(60deg) scaleY(1) !important; } /   - removed: @media (hover: hover) > .tlv-orb:hover .tlv-orb__wrap::after, .tlv-orb:focus-visible .tlv-orb__wrap::after { opacity: 1; transform: translateX(-50%) rotate(-60deg) scaleY(1); } /   - removed: @media (hover: hover) > .tlv-orb:hover .tlv-orb__glow::before, .tlv-orb:focus-visible .tlv-orb__glow::before { opacity: 0.82; transform: scale(1); } /   - removed: @media (hover: hover) > .tlv-orb:hover .tlv-orb__glow, .tlv-orb:focus-visible .tlv-orb__glow { opacity: 1 !important; } /   - removed: @media (hover: hover) > .tlv-orb:hover .tlv-orb__glow::before, .tlv-orb:focus-visible .tlv-orb__glow::before, .tlv-orb:hover .tlv-orb__glow::after, .tlv-orb:focus-visible .tlv-orb__glow::after { transform: scale(1) !important; } /   - removed: @media (hover: hover) > .tlv-orb:hover .tlv-orb__glow::before, .tlv-orb:focus-visible .tlv-orb__glow::before { opacity: 1 !important; } /   - removed: @media (hover: hover) > .tlv-orb:hover .tlv-orb__wrap::before, .tlv-orb:focus-visible .tlv-orb__wrap::before { animation: 1.8s cubic-bezier(0.45, 0.05, 0.55, 0.95) 0s 1 normal both running tlv-arm-clock-right; } /   - removed: @media (hover: hover) > .tlv-orb:hover .tlv-orb__wrap::after, .tlv-orb:focus-visible .tlv-orb__wrap::after { animation: 1.8s cubic-bezier(0.45, 0.05, 0.55, 0.95) 0s 1 normal both running tlv-arm-clock-left; } /   - removed: .tlv-orb__glow::after { transition-delay: 1.24s !important; } /   - removed: @media (hover: hover) > .tlv-orb:hover .tlv-orb__wrap::before, .tlv-orb:focus-visible .tlv-orb__wrap::before { animation: 2.2s cubic-bezier(0.22, 0.8, 0.2, 1) 0s 1 normal both running tlv-arm-one-turn-right !important; } /   - removed: @media (hover: hover) > .tlv-orb:hover .tlv-orb__wrap::after, .tlv-orb:focus-visible .tlv-orb__wrap::after { animation: 2.2s cubic-bezier(0.22, 0.8, 0.2, 1) 0s 1 normal both running tlv-arm-one-turn-left !important; } /   - removed: @media (hover: hover) > .tlv-orb:hover .tlv-orb__wrap::before, .tlv-orb:focus-visible .tlv-orb__wrap::before { animation: 1.5s cubic-bezier(0.22, 0.8, 0.2, 1) 0s 1 normal both running tlv-arm-one-turn-right-fast !important; } /   - removed: @media (hover: hover) > .tlv-orb:hover .tlv-orb__wrap::after, .tlv-orb:focus-visible .tlv-orb__wrap::after { animation: 1.5s cubic-bezier(0.22, 0.8, 0.2, 1) 0s 1 normal both running tlv-arm-one-turn-left-fast !important; } /   - removed: @media (hover: hover) > .tlv-orb:hover .tlv-orb__wrap::before, .tlv-orb:focus-visible .tlv-orb__wrap::before { animation-duration: 1.9s !important; } /   - removed: @media (hover: hover) > .tlv-orb:hover .tlv-orb__wrap::after, .tlv-orb:focus-visible .tlv-orb__wrap::after { animation-duration: 1.9s !important; }**
- **Visual change if removed:** None.
- **Parts:** 22 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 19-19). Manual anchor: from `.tlv-orb--has-subs:hover .tlv-orb__wrap,.tlv-orb--has-subs:focus-within .tlv-orb__wrap{...` to `.tlv-orb--has-subs:hover .tlv-orb__wrap,.tlv-orb--has-subs:focus-within .tlv-orb__wrap{...`.
Delete:
```css
.tlv-orb--has-subs:hover .tlv-orb__wrap,.tlv-orb--has-subs:focus-within .tlv-orb__wrap{transform:translate3d(-34px,0,0)}
```

**Part 2** (baseline lines 20-20). Manual anchor: from `.tlv-orb--has-subs .tlv-orb__subs{display:none}` to `.tlv-orb--has-subs .tlv-orb__subs{display:none}`.
Delete:
```css
.tlv-orb--has-subs .tlv-orb__subs{display:none}
```

**Part 3** (baseline lines 38-38). Manual anchor: from `.tlv-orb--has-subs .tlv-orb__subs span{transition:none}` to `.tlv-orb--has-subs .tlv-orb__subs span{transition:none}`.
Delete:
```css
.tlv-orb--has-subs .tlv-orb__subs span{transition:none}
```

**Part 4** (baseline lines 129-129). Manual anchor: from `.tlv-orb__glow::after{transition:none}` to `.tlv-orb__glow::after{transition:none}`.
Delete:
```css
.tlv-orb__glow::after{transition:none}
```

**Part 5** (baseline lines 133-133). Manual anchor: from `.tlv-orb:hover .tlv-orb__wrap::before,.tlv-orb:focus-visible .tlv-orb__wrap::before{opa...` to `.tlv-orb:hover .tlv-orb__wrap::before,.tlv-orb:focus-visible .tlv-orb__wrap::before{opa...`.
Delete:
```css
.tlv-orb:hover .tlv-orb__wrap::before,.tlv-orb:focus-visible .tlv-orb__wrap::before{opacity:1;transform:translateX(-50%) scaleY(1)}
```

**Part 6** (baseline lines 134-134). Manual anchor: from `.tlv-orb__wrap::before{transition:none}` to `.tlv-orb__wrap::before{transition:none}`.
Delete:
```css
.tlv-orb__wrap::before{transition:none}
```

**Part 7** (baseline lines 145-145). Manual anchor: from `.tlv-orb__wrap{width:clamp(72px,13vw,96px)}` to `.tlv-orb__wrap{width:clamp(72px,13vw,96px)}`.
Delete:
```css
.tlv-orb__wrap{width:clamp(72px,13vw,96px)}
```

**Part 8** (baseline lines 152-152). Manual anchor: from `.tlv-orb:hover .tlv-orb__wrap::before,.tlv-orb:focus-visible .tlv-orb__wrap::before{tra...` to `.tlv-orb:hover .tlv-orb__wrap::before,.tlv-orb:focus-visible .tlv-orb__wrap::before{tra...`.
Delete:
```css
.tlv-orb:hover .tlv-orb__wrap::before,.tlv-orb:focus-visible .tlv-orb__wrap::before{transform:translateX(-50%) rotate(60deg) scaleY(1)!important}
```

**Part 9** (baseline lines 156-156). Manual anchor: from `.tlv-orb:hover .tlv-orb__wrap::after,.tlv-orb:focus-visible .tlv-orb__wrap::after{opaci...` to `.tlv-orb:hover .tlv-orb__wrap::after,.tlv-orb:focus-visible .tlv-orb__wrap::after{opaci...`.
Delete:
```css
.tlv-orb:hover .tlv-orb__wrap::after,.tlv-orb:focus-visible .tlv-orb__wrap::after{opacity:1;transform:translateX(-50%) rotate(-60deg) scaleY(1)}
```

**Part 10** (baseline lines 156-156). Manual anchor: from `.tlv-orb:hover .tlv-orb__glow::before,.tlv-orb:focus-visible .tlv-orb__glow::before{opa...` to `.tlv-orb:hover .tlv-orb__glow::before,.tlv-orb:focus-visible .tlv-orb__glow::before{opa...`.
Delete:
```css
.tlv-orb:hover .tlv-orb__glow::before,.tlv-orb:focus-visible .tlv-orb__glow::before{opacity:.82;transform:scale(1)}
```

**Part 11** (baseline lines 191-191). Manual anchor: from `.tlv-orb:hover .tlv-orb__glow::before,.tlv-orb:focus-visible .tlv-orb__glow::before,.tl...` to `.tlv-orb:hover .tlv-orb__glow::before,.tlv-orb:focus-visible .tlv-orb__glow::before,.tl...`.
This text also exists elsewhere in the file, so it is located by the neighbouring lines (kept, not deleted): before = `e(1)!important}`, after = `}`.
Delete:
```css
.tlv-orb:hover .tlv-orb__glow::before,.tlv-orb:focus-visible .tlv-orb__glow::before,.tlv-orb:hover .tlv-orb__glow::after,.tlv-orb:focus-visible .tlv-orb__glow::after{transform:scale(1)!important}
```

**Part 12** (baseline lines 196-196). Manual anchor: from `.tlv-orb:hover .tlv-orb__glow::before,.tlv-orb:focus-visible .tlv-orb__glow::before{opa...` to `.tlv-orb:hover .tlv-orb__glow::before,.tlv-orb:focus-visible .tlv-orb__glow::before{opa...`.
This text also exists elsewhere in the file, so it is located by the neighbouring lines (kept, not deleted): before = `a(hover:hover){`, after = `}`.
Delete:
```css
.tlv-orb:hover .tlv-orb__glow::before,.tlv-orb:focus-visible .tlv-orb__glow::before{opacity:1!important}
```

**Part 13** (baseline lines 216-216). Manual anchor: from `.tlv-orb:hover .tlv-orb__glow,.tlv-orb:focus-visible .tlv-orb__glow{opacity:1!important}` to `.tlv-orb:hover .tlv-orb__glow,.tlv-orb:focus-visible .tlv-orb__glow{opacity:1!important}`.
This text also exists elsewhere in the file, so it is located by the neighbouring lines (kept, not deleted): before = `a(hover:hover){`, after = `}`.
Delete:
```css
.tlv-orb:hover .tlv-orb__glow,.tlv-orb:focus-visible .tlv-orb__glow{opacity:1!important}
```

**Part 14** (baseline lines 219-219). Manual anchor: from `.tlv-orb:hover .tlv-orb__wrap::before,.tlv-orb:focus-visible .tlv-orb__wrap::before{ani...` to `.tlv-orb:hover .tlv-orb__wrap::before,.tlv-orb:focus-visible .tlv-orb__wrap::before{ani...`.
Delete:
```css
.tlv-orb:hover .tlv-orb__wrap::before,.tlv-orb:focus-visible .tlv-orb__wrap::before{animation:tlv-arm-clock-right 1.8s cubic-bezier(.45,.05,.55,.95) both}
```

**Part 15** (baseline lines 219-219). Manual anchor: from `.tlv-orb:hover .tlv-orb__wrap::after,.tlv-orb:focus-visible .tlv-orb__wrap::after{anima...` to `.tlv-orb:hover .tlv-orb__wrap::after,.tlv-orb:focus-visible .tlv-orb__wrap::after{anima...`.
Delete:
```css
.tlv-orb:hover .tlv-orb__wrap::after,.tlv-orb:focus-visible .tlv-orb__wrap::after{animation:tlv-arm-clock-left 1.8s cubic-bezier(.45,.05,.55,.95) both}
```

**Part 16** (baseline lines 282-282). Manual anchor: from `.tlv-orb__glow::after{transition-delay:1.24s!important}` to `.tlv-orb__glow::after{transition-delay:1.24s!important}`.
Delete:
```css
.tlv-orb__glow::after{transition-delay:1.24s!important}
```

**Part 17** (baseline lines 285-285). Manual anchor: from `.tlv-orb:hover .tlv-orb__wrap::before,.tlv-orb:focus-visible .tlv-orb__wrap::before{ani...` to `.tlv-orb:hover .tlv-orb__wrap::before,.tlv-orb:focus-visible .tlv-orb__wrap::before{ani...`.
Delete:
```css
.tlv-orb:hover .tlv-orb__wrap::before,.tlv-orb:focus-visible .tlv-orb__wrap::before{animation:tlv-arm-one-turn-right 2.2s cubic-bezier(.22,.8,.2,1) both!important}
```

**Part 18** (baseline lines 285-285). Manual anchor: from `.tlv-orb:hover .tlv-orb__wrap::after,.tlv-orb:focus-visible .tlv-orb__wrap::after{anima...` to `.tlv-orb:hover .tlv-orb__wrap::after,.tlv-orb:focus-visible .tlv-orb__wrap::after{anima...`.
Delete:
```css
.tlv-orb:hover .tlv-orb__wrap::after,.tlv-orb:focus-visible .tlv-orb__wrap::after{animation:tlv-arm-one-turn-left 2.2s cubic-bezier(.22,.8,.2,1) both!important}
```

**Part 19** (baseline lines 291-291). Manual anchor: from `.tlv-orb:hover .tlv-orb__wrap::before,.tlv-orb:focus-visible .tlv-orb__wrap::before{ani...` to `.tlv-orb:hover .tlv-orb__wrap::before,.tlv-orb:focus-visible .tlv-orb__wrap::before{ani...`.
Delete:
```css
.tlv-orb:hover .tlv-orb__wrap::before,.tlv-orb:focus-visible .tlv-orb__wrap::before{animation:tlv-arm-one-turn-right-fast 1.5s cubic-bezier(.22,.8,.2,1) both!important}
```

**Part 20** (baseline lines 291-291). Manual anchor: from `.tlv-orb:hover .tlv-orb__wrap::after,.tlv-orb:focus-visible .tlv-orb__wrap::after{anima...` to `.tlv-orb:hover .tlv-orb__wrap::after,.tlv-orb:focus-visible .tlv-orb__wrap::after{anima...`.
Delete:
```css
.tlv-orb:hover .tlv-orb__wrap::after,.tlv-orb:focus-visible .tlv-orb__wrap::after{animation:tlv-arm-one-turn-left-fast 1.5s cubic-bezier(.22,.8,.2,1) both!important}
```

**Part 21** (baseline lines 294-294). Manual anchor: from `.tlv-orb:hover .tlv-orb__wrap::before,.tlv-orb:focus-visible .tlv-orb__wrap::before{ani...` to `.tlv-orb:hover .tlv-orb__wrap::before,.tlv-orb:focus-visible .tlv-orb__wrap::before{ani...`.
Delete:
```css
.tlv-orb:hover .tlv-orb__wrap::before,.tlv-orb:focus-visible .tlv-orb__wrap::before{animation-duration:1.9s!important}
```

**Part 22** (baseline lines 294-294). Manual anchor: from `.tlv-orb:hover .tlv-orb__wrap::after,.tlv-orb:focus-visible .tlv-orb__wrap::after{anima...` to `.tlv-orb:hover .tlv-orb__wrap::after,.tlv-orb:focus-visible .tlv-orb__wrap::after{anima...`.
Delete:
```css
.tlv-orb:hover .tlv-orb__wrap::after,.tlv-orb:focus-visible .tlv-orb__wrap::after{animation-duration:1.9s!important}
```

### T120 [REVIEW] 4 orphaned rule(s) inside minified/inline CSS of templates/page.wishlist.liquid
- **File:** `templates/page.wishlist.liquid` | baseline lines 11-11, 12-12, 12-12, 17-17 | kind: rule-level removal inside lines (exact text) - orphan selectors (scripted search)
- **Why it is dead:** Every selector of each rule needs a class/ID that appears nowhere in the theme outside CSS (markup, JS, JSON; any mention counts as used; prefix-built names count as used; Shopify/app prefixes count as used). Selectors: .tlv-wlp a.tlv-wlp__t; .tlv-wlp__card; .tlv-wlp__card:hover; .tlv-wlp__grid
- **Proof:** Not provable from CSS alone, hence REVIEW; joint Chrome CSSOM check: exactly these rules removed, nothing added. These parts remove a single rule from the middle of a line: only the exact_text is removed, context is kept.
- **Verify:** expected `cssom.js compare` result for this item alone: **DIFFERENT /   - removed: @media (min-width: 768px) > .tlv-wlp__grid { grid-template-columns: repeat(4, 1fr); } /   - removed: .tlv-wlp__card { background: rgb(255, 255, 255); border: 1px solid rgb(228, 228, 231); border-radius: 8px; overflow: hidden; position: relative; transition: border-color 0.15s; } /   - removed: .tlv-wlp__card:hover { border-color: rgb(161, 161, 170); } /   - removed: .tlv-wlp a.tlv-wlp__t { color: rgb(26, 26, 46) !important; }**
- **Visual change if removed:** None expected.
- **Parts:** 4 (apply.py handles all parts of an item at once)

**Part 1** (baseline lines 11-11). Manual anchor: from `.tlv-wlp__grid{grid-template-columns:repeat(4,1fr)}` to `.tlv-wlp__grid{grid-template-columns:repeat(4,1fr)}`.
Delete:
```css
.tlv-wlp__grid{grid-template-columns:repeat(4,1fr)}
```

**Part 2** (baseline lines 12-12). Manual anchor: from `.tlv-wlp__card{background:#fff;border:1px solid #e4e4e7;border-radius:8px;overflow:hidd...` to `.tlv-wlp__card{background:#fff;border:1px solid #e4e4e7;border-radius:8px;overflow:hidd...`.
Delete:
```css
.tlv-wlp__card{background:#fff;border:1px solid #e4e4e7;border-radius:8px;overflow:hidden;position:relative;transition:border-color .15s ease}
```

**Part 3** (baseline lines 12-12). Manual anchor: from `.tlv-wlp__card:hover{border-color:#a1a1aa}` to `.tlv-wlp__card:hover{border-color:#a1a1aa}`.
Delete:
```css
.tlv-wlp__card:hover{border-color:#a1a1aa}
```

**Part 4** (baseline lines 17-17). Manual anchor: from `.tlv-wlp a.tlv-wlp__t{color:#1a1a2e!important}` to `.tlv-wlp a.tlv-wlp__t{color:#1a1a2e!important}`.
Delete:
```css
.tlv-wlp a.tlv-wlp__t{color:#1a1a2e!important}
```

---

## Files that are never rendered (REVIEW: delete the file, not its CSS)

These section/snippet files are not referenced by any template, layout, render/include/section tag, and their name appears in NO other theme file at all (not in JS, JSON or CSS either), so Shopify never renders them and their CSS never loads. Deleting the file is the cleanup (not editing its CSS). REVIEW: ask Ziko; a section can still be offered in the theme editor's 'Add section' list if it has a {% schema %} with presets, so check that first.

- `sections/cat-cards.liquid` (4751 bytes, 1 <style> block(s))
- `sections/featured-banner.liquid` (871 bytes, 1 <style> block(s))
- `sections/fish-background.liquid` (5232 bytes, 1 <style> block(s))
- `sections/glitch-background-backup.liquid` (9838 bytes, 1 <style> block(s))
- `sections/glitch-background.liquid` (17069 bytes, 1 <style> block(s))
- `sections/graffiti-tag.liquid` (9591 bytes, 1 <style> block(s))
- `sections/product-template.liquid` (9865 bytes, 1 <style> block(s))
- `sections/tlv-search-json.liquid` (1047 bytes, 0 <style> block(s))
- `snippets/collection-discovery-banners.liquid` (26094 bytes, 12 <style> block(s))
- `snippets/collection-wave.liquid` (9247 bytes, 1 <style> block(s))
- `snippets/fidget-showcase-banner.liquid` (10784 bytes, 1 <style> block(s))
- `snippets/fish-swim.liquid` (5222 bytes, 1 <style> block(s))
- `snippets/halloween-row-banner.liquid` (19932 bytes, 2 <style> block(s))
- `snippets/keychain-showcase-banner.liquid` (11091 bytes, 1 <style> block(s))
- `snippets/plexus-bg.liquid` (10831 bytes, 1 <style> block(s))
- `snippets/plush-showcase-banner.liquid` (10564 bytes, 1 <style> block(s))
- `snippets/product-rating-vals.liquid` (147 bytes, 0 <style> block(s))
- `snippets/product-rating.liquid` (131 bytes, 0 <style> block(s))
- `snippets/rc-showcase-banner.liquid` (8129 bytes, 1 <style> block(s))
- `snippets/torn-paper.liquid` (1102 bytes, 0 <style> block(s))
- `snippets/toylvia-loader.liquid` (5898 bytes, 1 <style> block(s))
- `snippets/ttt-graffiti.liquid` (11233 bytes, 0 <style> block(s))
- `snippets/tv-icon-defs.liquid` (6290 bytes, 1 <style> block(s))
- `snippets/tv-icon-tags.liquid` (6874 bytes, 0 <style> block(s))

---

## Deciding on REVIEW items

- TODO items are proven from the CSS alone (Chrome rule list unchanged, or every removed rule provably overridden). They are safe without looking at the site.
- Every REVIEW item rests on one claim: 'no template, snippet or script outputs these classes' (or the element is display:none). That was checked by a full-text search of all 119 theme files plus a skeptic agent, but an app or content in the Shopify admin (product descriptions, pages) could in theory use a class.
- Simplest safe way to approve REVIEW items: apply them to a DUPLICATE of the live theme first (Online Store > Themes > Duplicate, then push with --theme <duplicate id>), preview the homepage, one product page, one collection page and the cart on desktop and mobile, then push to the live theme.
- Supersede pairs: a few REVIEW items contain smaller TODO items. Approving the REVIEW item removes the TODO item's lines too; apply it instead of them.

---

## Not scanned yet (possible next step)

- INLINE CSS IN .liquid FILES (partly done: round 5 logged the always-overridden rules that sit on whole lines; NOT yet scanned for orphan/never-rendered CSS, and minified multi-rule lines, e.g. most of theme.liquid and collection-page.liquid, need declaration-level edits). ~670 KB of CSS in 313 <style> blocks across 68 files, biggest: snippets/collection-page.liquid (114 KB), layout/theme.liquid (113 KB, has Liquid {% if %} inside CSS), sections/category-rows.liquid (48 KB), snippets/tlv-orbs.liquid (41 KB), snippets/cr-card-styles.liquid (33 KB), sections/story-pair.liquid (29 KB), snippets/product-card-styles.liquid (28 KB), sections/clg-hero.liquid (25 KB). Tools are ready in tools/: liquid_css_view.py (CSS view with identical line numbers, `--stats` lists blocks and Liquid conditionals), lqcheck.sh (cut ranges + CSSOM diff + override proof), shadow.js, cut.py. Same rules as this file: only whole rules inside <style>, TODO only if proven from CSS alone, never use a winner inside a Liquid conditional, selectors with {{ }} target the section's own wrapper (treat as used). Also check for sections/snippets that are never rendered at all (e.g. sections/glitch-background-backup.liquid, sections/category-arc.liquid is not in templates/index.json).
- assets/tlv-owner-overrides.css: deliberately excluded (owner-requested file; one proven duplicate there was left alone on purpose).
- Declaration-level dead code inside live rules (single overridden properties). Only whole rules/blocks were logged.

---

## Known issues that are NOT deletions (do not apply without asking Ziko)

- **Unclosed @media in toylvia.css (real bug, but fixing it CHANGES the site)**: Baseline line ~5535 opens `@media (max-width: 1024px) {` with a dangling `.cat-ice-label` selector and never closes it. Everything after it (about 670 lines: outlined Add to Cart pill, transparent header, free shipping bar, cart bundle, badge colours, mobile crash fix, ...) only applies at widths <= 1024px. Fixing it would switch those styles ON for desktop. Ask Ziko whether he wants that before touching it.
- **Ziko's DevTools edits to homepage product rows (pending his decision)**: Earlier in the cloud session Ziko unticked declarations at mobile width in assets/tlv-owner-overrides.css (tlv-row-header-gap translateY(18px); tlv-row-spacing row margins/paddings, the clamp() row gap and header padding/margin; tlv-header-shift translateY(9px); tlv-header-no-padding mobile block; tlv-row-unite mobile block) and in assets/home-palette.css (.cat-rows__row margin 0 1.25rem 0 and padding 0). Several are not inside a media query, so applying them as-is also changes desktop. Recommendation given: apply them inside @media(max-width:767px) only. He has not decided yet. Do not apply without asking.

