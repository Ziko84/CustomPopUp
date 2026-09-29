#!/usr/bin/env python3
"""Replace spaced hyphens used as dashes (" - ") in Toylvia blog article bodies.

Rules, applied to visible text only (HTML tags, comments, <script> and <style> are untouched):
  - Two dashes in the same sentence become parentheses: "a - b - c" -> "a (b) c"
  - A single dash after "Yes"/"No" becomes a comma: "Yes - it does" -> "Yes, it does"
  - Any other single dash becomes a colon: "<strong>Size</strong> - 30cm" -> "<strong>Size</strong>: 30cm"

Usage:
  SHOPIFY_ADMIN_TOKEN=shpat_... python3 scripts/fix_blog_dashes.py            # dry run: report only
  SHOPIFY_ADMIN_TOKEN=shpat_... python3 scripts/fix_blog_dashes.py --apply    # update articles, then verify
  python3 scripts/fix_blog_dashes.py --from-jsonl export.jsonl                # offline dry run on a bulk export

The token needs the read_content and write_content scopes.
"""
import argparse
import json
import os
import re
import sys
import urllib.request

STORE = os.environ.get("SHOPIFY_STORE", "7bcmti-jy.myshopify.com")
API_VERSION = "2026-07"

TOKENS = re.compile(r"<!--.*?-->|<script.*?</script>|<style.*?</style>|<[^>]*>|[^<]+", re.S | re.I)
BLOCK_TAG = re.compile(
    r"</?(p|li|h[1-6]|td|th|div|ul|ol|br|blockquote|tr|table|nav|section|article)\b", re.I
)


def fix_body(body):
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


def gql(query, variables=None):
    token = os.environ.get("SHOPIFY_ADMIN_TOKEN")
    if not token:
        sys.exit("SHOPIFY_ADMIN_TOKEN is not set")
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
            " nodes { id handle body } pageInfo { hasNextPage endCursor } } }",
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

    fixes = {}
    for a in articles:
        new_body, n = fix_body(a.get("body") or "")
        if n:
            fixes[a["id"]] = (a["handle"], new_body, n)
    print(f"{len(articles)} articles scanned, {len(fixes)} to fix, "
          f"{sum(n for _, _, n in fixes.values())} dashes")
    if not args.apply:
        for handle, _, n in sorted(fixes.values(), key=lambda x: -x[2]):
            print(f"  {n:4d}  {handle}")
        return

    for article_id, (handle, body, n) in fixes.items():
        res = gql(
            "mutation($id: ID!, $article: ArticleUpdateInput!) {"
            " articleUpdate(id: $id, article: $article) { userErrors { field message } } }",
            {"id": article_id, "article": {"body": body}},
        )["articleUpdate"]
        status = res["userErrors"] or "ok"
        print(f"  {handle}: {n} fixed, {status}")

    # Verify against a fresh read.
    live = {a["id"]: a for a in fetch_articles()}
    bad = [h for aid, (h, body, _) in fixes.items()
           if (live[aid]["body"] or "").rstrip("\n") != body.rstrip("\n")]
    left = sum(fix_body(a.get("body") or "")[1] for a in live.values())
    print(f"verified: {len(fixes) - len(bad)}/{len(fixes)} match; spaced hyphens left: {left}")
    if bad:
        print("mismatched:", ", ".join(bad))
        sys.exit(1)


if __name__ == "__main__":
    main()
