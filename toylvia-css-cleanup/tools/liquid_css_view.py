#!/usr/bin/env python3
"""Turn a .liquid file into a pure-CSS "view" with IDENTICAL line numbers, so cssom.js can check edits.

    python tools/liquid_css_view.py <file.liquid> <out.css>          # write the view
    python tools/liquid_css_view.py <file.liquid> --stats            # list <style> blocks

- Keeps only the content of <style>...</style> and {% style %}...{% endstyle %} blocks
  (blocks inside <script> are ignored: they are JS strings, not CSS the browser parses as-is).
- Everything else becomes empty lines (newlines are kept, so line N of the view = line N of the file).
- Inside blocks, Liquid output {{ ... }} becomes `liq` when it is part of a selector (the next of { ; }
  is "{"), e.g. #shopify-section-{{ section.id }} -> #shopify-section-liq, and `var(--liq)` when it is
  part of a value. Liquid tags {% ... %} are removed (newlines kept). {% comment %} blocks are blanked.
- `--stats` also lists the line ranges inside {% if/unless/case/for %} in each block: rules there only
  render conditionally, so they must not be used as the "winner" in an override proof.
- Each block is closed on its own last line (missing `}` / `*/` appended without adding lines),
  because in the browser every <style> element is a separate stylesheet.
Rendered order is assumed to follow source order; Liquid conditionals are not evaluated.
"""
import re, sys

TAG_OPEN = re.compile(r'<style\b[^>]*>|\{%-?\s*style\s*-?%\}', re.I)
TAG_CLOSE = {'<': re.compile(r'</style\s*>', re.I), '{': re.compile(r'\{%-?\s*endstyle\s*-?%\}', re.I)}
SCRIPT = re.compile(r'<script\b[^>]*>.*?</script\s*>', re.I | re.S)

def keep_newlines(s, filler=''):
    return filler + '\n' * s.count('\n')

def liquid_to_css(block):
    block = re.sub(r'\{%-?\s*comment\s*-?%\}.*?\{%-?\s*endcomment\s*-?%\}', lambda m: keep_newlines(m.group(0)), block, flags=re.S)
    def out_tag(m):
        nxt = re.search(r'[{;}]', re.sub(r'\{\{.*?\}\}|\{%.*?%\}', ' ', block[m.end():m.end() + 4000], flags=re.S))
        return keep_newlines(m.group(0), 'liq' if nxt and nxt.group(0) == '{' else 'var(--liq)')
    block = re.sub(r'\{\{.*?\}\}', out_tag, block, flags=re.S)
    block = re.sub(r'\{%.*?%\}', lambda m: keep_newlines(m.group(0)), block, flags=re.S)
    return block

def close_block(css):
    depth, i, in_c, q = 0, 0, False, None
    while i < len(css):
        c = css[i]
        if in_c:
            if css.startswith('*/', i): in_c = False; i += 1
        elif q:
            if c == '\\': i += 1
            elif c == q: q = None
        elif css.startswith('/*', i): in_c = True; i += 1
        elif c in '"\'': q = c
        elif c == '{': depth += 1
        elif c == '}': depth = max(0, depth - 1)
        i += 1
    return css + ('*/' if in_c else '') + '}' * depth

def blocks(text):
    scripts = [(m.start(), m.end()) for m in SCRIPT.finditer(text)]
    pos, out = 0, []
    while True:
        m = TAG_OPEN.search(text, pos)
        if not m: break
        if any(a <= m.start() < b for a, b in scripts):
            pos = m.end(); continue
        c = TAG_CLOSE['{' if m.group(0).startswith('{') else '<'].search(text, m.end())
        end = c.start() if c else len(text)
        out.append((m.end(), end))
        pos = c.end() if c else len(text)
    return out

def view(text):
    res, last = [], 0
    for a, b in blocks(text):
        res.append(keep_newlines(text[last:a]))
        res.append(close_block(liquid_to_css(text[a:b])))
        last = b
    res.append(keep_newlines(text[last:]))
    return ''.join(res)

if __name__ == '__main__':
    src = sys.argv[1]; text = open(src, encoding='utf-8').read()
    if len(sys.argv) > 2 and sys.argv[2] == '--stats':
        for a, b in blocks(text):
            l1, l2 = text.count('\n', 0, a) + 1, text.count('\n', 0, b) + 1
            body = text[a:b]
            print(f'{src}:{l1}-{l2} chars={len(body)} rules~{body.count("{")} liquid_out={len(re.findall(r"{{", body))} liquid_tags={len(re.findall(r"{%", body))}')
            stack = []
            for t in re.finditer(r'\{%-?\s*(\w+)', body):
                name, line = t.group(1), text.count('\n', 0, a + t.start()) + 1
                if name in ('if', 'unless', 'case', 'for'): stack.append((name, line))
                elif name in ('endif', 'endunless', 'endcase', 'endfor') and stack:
                    n0, l0 = stack.pop()
                    if not stack: print(f'    conditional {n0}: lines {l0}-{line}')
    else:
        v = view(text)
        assert v.count('\n') == text.count('\n'), 'line count changed'
        open(sys.argv[2], 'w', encoding='utf-8').write(v)
