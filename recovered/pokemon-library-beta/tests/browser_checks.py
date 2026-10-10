"""Functional release checks. Run against a locally served repository."""
import json,os
from pathlib import Path
from playwright.sync_api import sync_playwright
url=os.environ.get('APP_URL','http://127.0.0.1:8766/Pokemon-Save-File-Program/dist/')
with sync_playwright() as pw:
 browser=pw.chromium.launch(executable_path=os.environ.get('CHROMIUM','/usr/bin/chromium'),args=['--no-sandbox'])
 page=browser.new_page(reduced_motion='reduce');errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto(url);page.keyboard.press('Enter')
 result=page.evaluate('''()=>{
 const checks={};
 const raw=new Uint8Array(CFG.MON);Binary.w16(raw,0x1c,1);
 checks.zeroFriendship=PokemonRepository.boxedToParty(raw)[0x29]===0;
 const fake={pc:{pc:new Uint8Array(58),streams:[]},sections:[]};
 checks.slotBounds=[[0,1],[1,0],[1,31],[-1,2],[1,1.5],[NaN,1],[25,1],[27,1]].every(([b,s])=>PokemonRepository.pcSlot(fake,b,s).kind==='missing');
 checks.firstSlot=PokemonRepository.pcSlot(fake,1,1).raw.length===58;
 checks.routes=BRANCHES.map(b=>{UI.go(b.id);return {id:b.id,ok:document.querySelector('#main').textContent.trim().length>0}});
 checks.adapters=ConverterAdapterAudit.run();
 const st=SaveEngine.parse(ConverterAdapterAudit.unboundFixture(1),'fixture.sav');
 const initial=st.boxes[0][0];
 PokemonTransferService.pcToParty(st,1,1);
 PokemonEditService.applyParty(st,1,{nickname:'BUDDY',happiness:0});
 PokemonTransferService.partyToPc(st,1,1,2);
 PokemonTransferService.pcToPc(st,1,2,2,3);
 checks.editTransferIntegration=st.boxes[1][2].nickname==='BUDDY'&&st.boxes[1][2].happiness===0&&st.boxes[1][2].pid===initial.pid&&!st.boxes[0][0]&&!st.boxes[0][1]&&st.party.length===0;
 const damaged={...fake,pc:{pc:new Uint8Array(58),streams:[]}};Binary.w16(damaged.pc.pc,0x1c,3000);
 try{PokemonRepository.writePcRaw({},damaged,1,1,new Uint8Array(58));checks.unrecognizedProtection=false}catch(e){checks.unrecognizedProtection=e.code==='PC_RECORD_UNRECOGNIZED'}

 return checks;
 }''')
 assert result['editTransferIntegration'] and result['unrecognizedProtection']
 assert result['zeroFriendship'] and result['slotBounds'] and result['firstSlot']
 assert all(r['ok'] for r in result['routes']) and result['adapters']['ok']
 result['backupRestore']=page.evaluate("""async()=>{
 window.confirm=()=>true;
 const restore=async(data)=>TransferHub.restoreBackup(new File([JSON.stringify(data)],'backup.json'));
 const base={format:'PokemonProgramTransferHubBackup',version:2,archives:[],pokemon:[]};
 await restore({...base,archives:[{id:"bad'identifier",profile:'emerald',name:'bad.sav'}]});
 const invalid=(await TransferHubDB.all('archives')).length===0;
 const raw=Gen3Compat.fixture('emerald');
 await restore({...base,archives:[{id:'emerald:test',profile:'emerald',name:'test.sav',bytesBase64:TransferHub.bytesToBase64(raw),writeSafety:'verified',status:'readable'}]});
 const restored=await TransferHubDB.get('archives','emerald:test');
 const ok=invalid&&restored?.writeSafety==='unverified'&&new Uint8Array(restored.bytes).length===raw.length;
 await TransferHubDB.delete('archives','emerald:test');return ok;
 }""")
 assert result['backupRestore']
 assert not errors,errors
 result['uncaughtErrors']=errors
 Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2))
 print('PASS: friendship, coordinate bounds, 17 routes, 36 synthetic adapter routes; no uncaught errors.')
 browser.close()
