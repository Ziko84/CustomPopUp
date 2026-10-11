#!/usr/bin/env python3
"""Apply one finding from findings.json to a local copy of a theme CSS file.

    python tools/apply.py <path/to/file.css> <ITEM_ID>            # apply
    python tools/apply.py <path/to/file.css> <ITEM_ID> --dry-run  # only check

Removes the item's exact_text (or replaces it with item.replacement) from the file.
Refuses to touch the file unless exact_text occurs EXACTLY ONCE. Never guesses.
"""
import json, pathlib, sys

def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    dry = '--dry-run' in sys.argv
    if len(args) != 2:
        print(__doc__); sys.exit(2)
    css_path, item_id = pathlib.Path(args[0]), args[1]
    data = json.loads((pathlib.Path(__file__).parent.parent / 'findings.json').read_text(encoding='utf-8'))
    item = next((i for i in data['items'] if i['id'] == item_id), None)
    if not item:
        sys.exit(f'No item {item_id} in findings.json')
    expected = item['file'].split('/')[-1]
    if css_path.name != expected:
        sys.exit(f'{item_id} belongs to {item["file"]}, not {css_path.name}')
    text = css_path.read_bytes().decode('utf-8')
    old = item['exact_text']
    n = text.count(old)
    if n != 1:
        sys.exit(f'REFUSED {item_id}: exact_text found {n} times (must be exactly 1). '
                 'The live file probably changed. Do not guess. Mark the item SKIPPED and tell the user.')
    new = text.replace(old, item.get('replacement', ''), 1)
    print(f'{item_id}: match found once, {len(old)} chars -> {len(item.get("replacement", ""))} chars '
          f'({text.count(chr(10)) - new.count(chr(10))} lines removed)')
    if dry:
        print('dry run, file not written'); return
    css_path.write_bytes(new.encode('utf-8'))
    print(f'written: {css_path}')

if __name__ == '__main__':
    main()
