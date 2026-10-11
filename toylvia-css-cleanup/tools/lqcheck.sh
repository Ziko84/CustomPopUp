#!/bin/bash
# lqcheck.sh <file.liquid> <a-b> [<c-d> ...] : cut line ranges, compare CSS views, prove "always overridden".
# Needs python3, node and Chrome (set CHROME if not auto-found).
set -e
D="$(cd "$(dirname "$0")" && pwd)"; F="$1"; shift; W=$(mktemp -d)
python3 "$D/cut.py" "$F" "$W/after.liquid" "$@"
python3 "$D/liquid_css_view.py" "$F" "$W/before.css"; python3 "$D/liquid_css_view.py" "$W/after.liquid" "$W/after.css"
echo "== cssom.js compare"; node "$D/cssom.js" compare "$W/before.css" "$W/after.css" || true
echo "== shadow.js"; node "$D/shadow.js" "$W/before.css" "$W/after.css" | grep -v '^shadowed' || true
rm -rf "$W"
