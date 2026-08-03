import sys, json
from playwright.sync_api import sync_playwright
html, sel = sys.argv[1], sys.argv[2]
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args=['--no-sandbox'])
    pg = b.new_page(viewport={'width':1280,'height':720})
    pg.goto('file://'+html)
    out = pg.evaluate("""(sel)=>{
      const el = document.querySelector(sel);
      if(!el) return null;
      const r = el.getBoundingClientRect();
      const kids=[...el.children].map(k=>{const q=k.getBoundingClientRect();
        return {t:(k.textContent||'').slice(0,26), w:Math.round(q.width), h:Math.round(q.height), y:Math.round(q.top)};});
      return {top:Math.round(r.top), h:Math.round(r.height), kids};
    }""", sel)
    print(json.dumps(out, ensure_ascii=False, indent=1))
    b.close()
