import sys
src, out, *rs = sys.argv[1:]
lines = open(src, encoding='utf-8').read().split('\n')
drop = set()
for r in rs:
    a, b = (map(int, r.split('-')) if '-' in r else (int(r), int(r))); drop.update(range(a, b + 1))
open(out, 'w', encoding='utf-8').write('\n'.join(l for n, l in enumerate(lines, 1) if n not in drop))
