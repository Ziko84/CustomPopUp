#!/usr/bin/env python3
"""Apply one finding from findings.json to a local copy of a theme CSS file.

    python tools/apply.py <path/to/file.css> <ITEM_ID>            # apply
    python tools/apply.py <path/to/file.css> <ITEM_ID> --dry-run  # only check

An item has one or more parts. Each part = context_before + exact_text + context_after.
The context lines are only used to find the right spot (they are kept); exact_text is
removed (or replaced by part.replacement). Every part must match EXACTLY ONCE, and all
parts are located before anything is changed. If any part fails, nothing is written.
"""
import json, pathlib, sys

def apply_item(text, item):
    """Return (new_text, message) or (None, reason). Pure function, no I/O."""
    spans = []
    for p in item['parts']:
        needle = p['context_before'] + p['exact_text'] + p['context_after']
        n = text.count(needle)
        if n != 1:
            return None, (f"part {p['lines']}: found {n} times (must be exactly 1). The file probably changed "
                          "or the item was already applied. Do not guess.")
        start = text.index(needle) + len(p['context_before'])
        spans.append((start, start + len(p['exact_text']), p.get('replacement', ''), p['lines']))
    spans.sort()
    for (s1, e1, _, l1), (s2, e2, _, l2) in zip(spans, spans[1:]):
        if s2 < e1:
            return None, f'parts {l1} and {l2} overlap'
    new = text
    for s, e, rep, _ in reversed(spans):
        new = new[:s] + rep + new[e:]
    removed = text.count('\n') - new.count('\n')
    return new, f"{item['id']}: {len(spans)} part(s) matched once each, {removed} lines removed"

def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if len(args) != 2:
        print(__doc__); sys.exit(2)
    css_path, item_id = pathlib.Path(args[0]), args[1]
    data = json.loads((pathlib.Path(__file__).resolve().parent.parent / 'findings.json').read_text(encoding='utf-8'))
    item = next((i for i in data['items'] if i['id'] == item_id), None)
    if not item:
        sys.exit(f'No item {item_id} in findings.json')
    if css_path.name != item['file'].split('/')[-1]:
        sys.exit(f"{item_id} belongs to {item['file']}, not {css_path.name}")
    text = css_path.read_bytes().decode('utf-8')
    new, msg = apply_item(text, item)
    if new is None:
        sys.exit(f'REFUSED {item_id}: {msg} Mark the item SKIPPED (or DONE if it is already gone) and tell the user.')
    print(msg)
    if '--dry-run' in sys.argv:
        print('dry run, file not written'); return
    css_path.write_bytes(new.encode('utf-8'))
    print(f'written: {css_path}')

if __name__ == '__main__':
    main()
