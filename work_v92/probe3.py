import sys
from playwright.sync_api import sync_playwright
html, sel, ncol = sys.argv[1], sys.argv[2], int(sys.argv[3])
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args=['--no-sandbox'])
    pg = b.new_page(viewport={'width':1280,'height':720})
    pg.goto('file://'+html)
    out = pg.evaluate("""([sel,n])=>{
      const el=document.querySelector(sel); const r=document.createRange();
      const mx=new Array(n).fill(0);
      [...el.children].forEach((k,i)=>{r.selectNodeContents(k);
        const w=Math.ceil(r.getBoundingClientRect().width); mx[i%n]=Math.max(mx[i%n],w);});
      return mx;}""", [sel, ncol])
    print('need+20:', [w+20 for w in out], 'tot', sum(w+20 for w in out))
    b.close()
