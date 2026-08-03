import sys, json
from playwright.sync_api import sync_playwright
html, sel = sys.argv[1], sys.argv[2]
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args=['--no-sandbox'])
    pg = b.new_page(viewport={'width':1280,'height':720})
    pg.goto('file://'+html)
    out = pg.evaluate("""(sel)=>{
      const el=document.querySelector(sel);
      const r=document.createRange();
      return [...el.children].map(k=>{r.selectNodeContents(k);
        const w=Math.ceil(r.getBoundingClientRect().width);
        return {t:(k.textContent||'').slice(0,24), need:w, has:Math.round(k.getBoundingClientRect().width)-20};});
    }""", sel)
    for o in out:
        if o['need'] > o['has']: print('WRAP', o)
    b.close()
