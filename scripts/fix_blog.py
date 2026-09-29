#!/usr/bin/env python3
"""Clean up Toylvia blog article bodies (SEO audit, 2026-09-29).

Fixes, in this order:
  1. Editor notes left in HTML comments ("Suggested image: ...", "SHOPIFY BLOG PUBLISHING DETAILS").
  2. Visible "[Image Placeholder: ...]" paragraphs.
  3. A second <h1> in the body: removed when it repeats the article title (the theme already
     prints the title as the H1), otherwise demoted to <h2>.
  4. Internal links to old URLs: pointed straight at the page they redirect to (LINK_MAP).
  5. Spaced hyphens used as dashes (" - "), in visible text only:
       - two in one sentence become parentheses: "a - b - c" -> "a (b) c"
       - a single one after "Yes"/"No" becomes a comma: "Yes - it does" -> "Yes, it does"
       - any other single one becomes a colon: "<strong>Size</strong> - 30cm" -> "<strong>Size</strong>: 30cm"

Usage:
  python3 scripts/fix_blog.py                            # dry run: report only
  python3 scripts/fix_blog.py --apply                    # update articles, then verify
  python3 scripts/fix_blog.py --from-jsonl export.jsonl  # offline dry run on a bulk export

Credentials come from the environment: SHOPIFY_CLIENT_ID and SHOPIFY_CLIENT_SECRET of a
Dev Dashboard app installed on the store (exchanged for a 24-hour token via the client
credentials grant), or a ready-made SHOPIFY_ADMIN_TOKEN. The app needs the read_content
and write_content scopes.
"""
import argparse
import difflib
import json
import os
import re
import sys
import urllib.request
from collections import Counter

STORE = os.environ.get("SHOPIFY_STORE", "7bcmti-jy.myshopify.com")
API_VERSION = "2026-07"

# Old internal paths found in articles on 2026-09-29, mapped to where they currently redirect.
# The number-plush product is archived (it returned 404), so its links go to Plush Toys.
LINK_MAP = {
    "/blogs/news/6-outdoor-halloween-decorations-2026": "/blogs/news/best-halloween-decorations-2026",
    "/blogs/news/best-cartoon-stuffed-toys-plushies-buyers-guide": "/blogs/news/the-complete-plush-animal-stuffed-toy-buying-guide",
    "/blogs/news/cute-keychains-plush-accessories": "/collections/collectibles-key-drops",
    "/blogs/news/kevin-bird-building-blocks-the-ultimate-guide-to-toylvias-cartoon-animal-display-sets": "/blogs/news",
    "/blogs/news/puzzle-types-compared-wooden-jigsaw-wild-cut-3d-build": "/blogs/news/3d-wooden-puzzles-guide-benefits-tips-best-models-for-all-ages-2026",
    "/blogs/news/shell-ejecting-toy-guns-compared": "/blogs/news/best-shell-ejecting-toy-guns-2026",
    "/blogs/news/skibidi-building-blocks-guide": "/blogs/news",
    "/blogs/news/toy-building-kits-guide-best-sets": "/blogs/news/toylvia-journal-building-blocks-for-creative-kids-2025",
    "/collections/animal-plush-collection": "/collections/plush-toys",
    "/collections/birthday-gifts": "/collections/trending-now",
    "/collections/capybara": "/collections/plush-toys",
    "/collections/city-builds": "/collections/building-blocks",
    "/collections/collectibles": "/collections/collectibles-key-drops",
    "/collections/construction-toys": "/collections/building-blocks",
    "/collections/cute-plush": "/collections/plush-toys",
    "/collections/educational-toys": "/collections/building-blocks",
    "/collections/engineering-gifts": "/collections/building-blocks",
    "/collections/fresh-drops": "/collections/new-arrivals",
    "/collections/jelly-building-blocks": "/collections/building-blocks",
    "/collections/kawaii-plush": "/collections/plush-toys",
    "/collections/mechanical-models": "/collections/building-blocks",
    "/collections/plush": "/collections/plush-toys",
    "/collections/plush-kawaii": "/collections/plush-toys",
    "/collections/puzzles": "/collections/puzzles-iq",
    "/collections/puzzles-3d-builds": "/collections/puzzles-iq",
    "/collections/speed-builds": "/collections/building-blocks",
    "/collections/stem-toys": "/collections/building-blocks",
    "/collections/under-50": "/collections/trending-now",
    "/collections/vehicles": "/collections/4-wheels",
    "/collections/vehicles-military": "/collections/building-blocks",
    "/collections/wooden-puzzles": "/collections/puzzles-iq",
    "/pages/shipping-policy": "/policies/shipping-policy",
    "/products/10pcs-cartoon-number-plush-doll-toy-educational-stuffed-kids-gift": "/collections/plush-toys",
    "/products/6pcs-set-mini-sprunki-action-figure-face-changing-toy-wenda-keychain": "/collections/all",
    "/products/care-bears-rainbow-plush-kawaii-sound-toy-keychain-bag-doll": "/collections/plush-toys",
    "/products/clippy-paperclip-building-block-set": "/collections/building-blocks",
    "/products/deadpool-wade-wilson-action-figure": "/collections/collectibles-key-drops",
    "/products/duo-green-owl-plush-toy-30cm": "/collections/plush-toys",
    "/products/leisurely-old-woman-wooden-jigsaw-puzzle": "/collections/puzzles-iq",
    "/products/long-rabbit-doll-plush-leg-clip-body-pillow-90cm-120cm": "/collections/plush-toys",
    "/products/majin-vegeta-20cm-dragon-ball-action-figure": "/collections/collectibles-key-drops",
    "/products/sword-of-holy-spirit-castle-2484pcs-medieval-moc-building-blocks": "/products/2484pcs-sword-of-holy-spirit-castle-building-blocks-model-toys-sets-small-particle-moc-street-view-bricks-for-christmas-gifts",
    "/products/unique-wooden-turtle-puzzle-adults-4-5-difficulty-jigsaw": "/collections/puzzles-iq",
}

TOKENS = re.compile(r"<!--.*?-->|<script.*?</script>|<style.*?</style>|<[^>]*>|[^<]+", re.S | re.I)
BLOCK_TAG = re.compile(
    r"</?(p|li|h[1-6]|td|th|div|ul|ol|br|blockquote|tr|table|nav|section|article)\b", re.I
)
EDITOR_NOTE = re.compile(r"<!--\s*(?:Suggested image|SHOPIFY BLOG PUBLISHING DETAILS).*?-->\s*", re.S | re.I)
PLACEHOLDER = re.compile(r"<p>\s*\[Image Placeholder:[^\]]*\]\s*</p>\s*", re.I)
BODY_H1 = re.compile(r"<h1(\s[^>]*)?>(.*?)</h1>", re.S | re.I)
HREF = re.compile(r'href="((?:https?://(?:www\.)?toylvia\.com)?)(/[^"?#]*)([^"]*)"', re.I)


def fix_dashes(body):
    items = [(not t.startswith("<"), t) for t in (m.group(0) for m in TOKENS.finditer(body))]

    # Group dash positions by sentence; a block-level tag or sentence end starts a new group.
    groups, cur = [], []
    for i, (is_text, s) in enumerate(items):
        if not is_text:
            if BLOCK_TAG.match(s) and cur:
                groups.append(cur)
                cur = []
            continue
        for k in range(len(s)):
            if s[k] in ".!?" and (k + 1 == len(s) or s[k + 1] == " ") and cur:
                groups.append(cur)
                cur = []
            if s.startswith(" - ", k):
                cur.append((i, k))
    if cur:
        groups.append(cur)

    rep = {}
    for g in groups:
        j = 0
        while j < len(g):
            if j + 1 < len(g):
                rep[g[j]], rep[g[j + 1]] = " (", ") "
                j += 2
                continue
            i, k = g[j]
            word = re.findall(r"(\w+)$", items[i][1][:k])
            rep[g[j]] = ", " if word and word[0] in ("Yes", "No") else ": "
            j += 1

    out = []
    for i, (is_text, s) in enumerate(items):
        if is_text:
            for k in sorted((k for (ii, k) in rep if ii == i), reverse=True):
                s = s[:k] + rep[(i, k)] + s[k + 3:]
            s = s.replace(" ) ", ") ")
        out.append(s)
    return "".join(out), len(rep)


def _plain(html):
    return re.sub(r"[^a-z0-9]+", " ", re.sub(r"<[^>]+>", " ", html).lower()).strip()


def fix_h1(body, title):
    n = 0

    def repl(m):
        nonlocal n
        n += 1
        if difflib.SequenceMatcher(None, _plain(m.group(2)), _plain(title)).ratio() >= 0.75:
            return ""
        return f"<h2{m.group(1) or ''}>{m.group(2)}</h2>"

    body = BODY_H1.sub(repl, body)
    return body.lstrip("\n") if n else body, n


def fix_links(body):
    n = 0

    def repl(m):
        nonlocal n
        path = m.group(2).rstrip("/") or "/"
        if path not in LINK_MAP:
            return m.group(0)
        n += 1
        return f'href="{m.group(1)}{LINK_MAP[path]}{m.group(3)}"'

    return HREF.sub(repl, body), n


def fix_all(article):
    body, counts = article.get("body") or "", Counter()
    body, counts["editor notes"] = EDITOR_NOTE.subn("", body)
    body, counts["placeholders"] = PLACEHOLDER.subn("", body)
    body, counts["duplicate h1"] = fix_h1(body, article.get("title") or "")
    body, counts["links"] = fix_links(body)
    body, counts["dashes"] = fix_dashes(body)
    return body, +counts


_token = None


def access_token():
    global _token
    if _token:
        return _token
    _token = os.environ.get("SHOPIFY_ADMIN_TOKEN")
    if _token:
        return _token
    client_id = os.environ.get("SHOPIFY_CLIENT_ID")
    client_secret = os.environ.get("SHOPIFY_CLIENT_SECRET")
    if not (client_id and client_secret):
        sys.exit("Set SHOPIFY_CLIENT_ID and SHOPIFY_CLIENT_SECRET (or SHOPIFY_ADMIN_TOKEN)")
    req = urllib.request.Request(
        f"https://{STORE}/admin/oauth/access_token",
        data=json.dumps({"client_id": client_id, "client_secret": client_secret,
                         "grant_type": "client_credentials"}).encode(),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        _token = json.load(resp)["access_token"]
    return _token


def gql(query, variables=None):
    token = access_token()
    req = urllib.request.Request(
        f"https://{STORE}/admin/api/{API_VERSION}/graphql.json",
        data=json.dumps({"query": query, "variables": variables or {}}).encode(),
        headers={"Content-Type": "application/json", "X-Shopify-Access-Token": token},
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.load(resp)
    if data.get("errors"):
        sys.exit(f"GraphQL error: {data['errors']}")
    return data["data"]


def fetch_articles():
    articles, after = [], None
    while True:
        data = gql(
            "query($after: String) { articles(first: 50, after: $after) {"
            " nodes { id handle title body } pageInfo { hasNextPage endCursor } } }",
            {"after": after},
        )["articles"]
        articles += data["nodes"]
        if not data["pageInfo"]["hasNextPage"]:
            return articles
        after = data["pageInfo"]["endCursor"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write changes to the store")
    ap.add_argument("--from-jsonl", help="read articles from a bulk export instead of the API")
    args = ap.parse_args()

    if args.from_jsonl:
        articles = [json.loads(line) for line in open(args.from_jsonl)]
    else:
        articles = fetch_articles()

    fixes, total = {}, Counter()
    for a in articles:
        new_body, counts = fix_all(a)
        if counts:
            fixes[a["id"]] = (a["handle"], new_body, counts)
            total += counts
    print(f"{len(articles)} articles scanned, {len(fixes)} to fix: "
          + ", ".join(f"{v} {k}" for k, v in total.items()))
    if not args.apply:
        for handle, _, counts in sorted(fixes.values(), key=lambda x: -sum(x[2].values())):
            print(f"  {handle}: " + ", ".join(f"{v} {k}" for k, v in counts.items()))
        return

    for article_id, (handle, body, counts) in fixes.items():
        res = gql(
            "mutation($id: ID!, $article: ArticleUpdateInput!) {"
            " articleUpdate(id: $id, article: $article) { userErrors { field message } } }",
            {"id": article_id, "article": {"body": body}},
        )["articleUpdate"]
        print(f"  {handle}: {res['userErrors'] or 'ok'}")

    # Verify against a fresh read: every body matches, and a second pass finds nothing left.
    live = {a["id"]: a for a in fetch_articles()}
    bad = [h for aid, (h, body, _) in fixes.items()
           if (live[aid]["body"] or "").rstrip("\n") != body.rstrip("\n")]
    left = sum((fix_all(a)[1] for a in live.values()), Counter())
    print(f"verified: {len(fixes) - len(bad)}/{len(fixes)} match; left to fix: {dict(left) or 'nothing'}")
    if bad:
        print("mismatched:", ", ".join(bad))
        sys.exit(1)


if __name__ == "__main__":
    main()
