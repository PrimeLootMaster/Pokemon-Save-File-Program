import test from 'node:test';
import assert from 'node:assert/strict';
import '../tools/backup-validation.js';
const stats=n=>Object.fromEntries(['HP','Atk','Def','Spe','SpA','SpD'].map(k=>[k,n]));
const valid=()=>({format:'PokemonProgramTransferHubBackup',version:2,archives:[{id:'emerald:test',profile:'emerald',name:'test.sav'}],pokemon:[{id:'mon:1',archiveId:'emerald:test',sourceGame:'emerald',level:12,exp:1728,natureId:0,abilityIndex:0,itemId:0,happiness:0,pid:1,otid:2,nationalId:1,unboundSpeciesId:1,nickname:'BUDDY',species:'Bulbasaur',shiny:false,moves:[33,0,0,0],ivs:stats(31),evs:stats(0)}]});
const validate=x=>HubBackupValidation.validate(x);
test('valid metadata backup preserves zero friendship',()=>assert.equal(validate(valid()).pokemon[0].happiness,0));
for(const [name,mutate] of [
 ['fractional level',x=>x.pokemon[0].level=1.5],['negative PID',x=>x.pokemon[0].pid=-1],['wrong stat',x=>x.pokemon[0].ivs.HP=32],['string move',x=>x.pokemon[0].moves[0]='33'],['missing source',x=>x.pokemon[0].archiveId='absent'],['duplicate record',x=>x.pokemon.push(x.pokemon[0])],['raw length',x=>x.pokemon[0].representations={emerald:{raw:[1]}}],['unsafe key',x=>x.extra=JSON.parse('{"__proto__":{}}')],['invalid base64',x=>x.archives[0].bytesBase64='%%%'],['missing stats',x=>delete x.pokemon[0].evs.Spe],['invalid game',x=>x.pokemon[0].sourceGame='anything'],['control characters',x=>x.pokemon[0].nickname='bad\u0000name']]){
 test('rejects '+name,()=>{const x=valid();mutate(x);assert.throws(()=>validate(x),/Invalid backup/)});
}
test('read-only unknown archive can be preserved',()=>{const x=valid();x.archives.push({id:'unknown:test',profile:'unknown',name:'unknown.bin'});assert.equal(validate(x).archives.length,2)});
