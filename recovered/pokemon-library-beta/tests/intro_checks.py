"""Actual pointer entry and recovery from failed animation APIs."""
import os
from playwright.sync_api import sync_playwright
base=os.environ.get('APP_BASE','http://127.0.0.1:8770/Pokemon-Save-File-Program/')
with sync_playwright() as p:
 b=p.chromium.launch(executable_path=os.environ.get('CHROMIUM','/usr/bin/chromium'),args=['--no-sandbox'])
 for artifact in ['Pokemon-Save-File-Library-BETA.html','dist/']:
  for mode in ['desktop','touch','canvas-error','drawing-error','reduced-motion']:
   page=b.new_page(viewport={'width':390 if mode=='touch' else 1280,'height':844},is_mobile=mode=='touch',has_touch=mode=='touch',reduced_motion='reduce' if mode=='reduced-motion' else 'no-preference')
   errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
   if mode=='canvas-error':page.add_init_script("HTMLCanvasElement.prototype.getContext=function(){throw new Error('Canvas unavailable')}")
   if mode=='drawing-error':page.add_init_script("CanvasRenderingContext2D.prototype.clearRect=function(){throw new Error('Drawing unavailable')}")
   page.goto(base+artifact)
   button=page.get_by_role('button',name='Enter the save file library',exact=True)
   if mode=='touch':button.tap()
   else:button.click()
   page.wait_for_function("!document.getElementById('shinySaversIntro')",timeout=4000)
   assert not page.locator('.app').evaluate('(el)=>el.inert')
   assert not errors,errors
   print('PASS',artifact,mode)
   page.close()
 b.close()
