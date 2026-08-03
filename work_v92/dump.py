import re, sys, html as H
s = open(sys.argv[1], encoding='utf-8').read()
def slides(s):
    out=[]
    for m in re.finditer(r'<div[^>]*class="slide[^"]*"[^>]*id="([^"]+)"[^>]*>|<div[^>]*id="([^"]+)"[^>]*class="slide[^"]*"[^>]*>', s):
        i = m.group(1) or m.group(2)
        start=m.start(); end=s.index('\n</div>', start)+len('\n</div>')
        out.append((i, s[start:end]))
    return out
for i, body in slides(s):
    t = re.sub(r'<(script|style)[\s\S]*?</\1>','',body)
    t = re.sub(r'<[^>]+>',' | ',t)
    t = H.unescape(t)
    t = re.sub(r'\s*\|\s*',' | ',t)
    t = re.sub(r'(\s*\|\s*)+',' | ',t).strip(' |')
    t = re.sub(r'[ \t]+',' ',t)
    print(f'\n===== {i} =====')
    print(t)
