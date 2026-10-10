/* Pure backup validation; also embedded in the standalone page. */
(() => {
 const profiles=new Set(['unbound','firered','leafgreen','ruby','sapphire','emerald']);
 const object=x=>x!==null&&typeof x==='object'&&!Array.isArray(x);
 const fail=message=>{throw new Error(`Invalid backup: ${message}`)};
 const integer=(v,min,max,label)=>{if(!Number.isInteger(v)||v<min||v>max)fail(label)};
 const id=(v,label)=>{if(typeof v!=='string'||!/^[A-Za-z0-9:._-]{1,200}$/.test(v))fail(label)};
 const text=(v,max,label)=>{if(typeof v!=='string'||v.length>max||/[\u0000-\u001f\u007f]/.test(v))fail(label)};
 const walk=(v,depth=0)=>{if(depth>16)fail('excessive nesting');if(v&&typeof v==='object'){for(const key of Object.keys(v)){if(['__proto__','constructor','prototype'].includes(key))fail('unsafe object key');walk(v[key],depth+1)}}};
 const optionalInt=(r,key,max)=>{if(r[key]!==undefined)integer(r[key],0,max,key)};
 const list=(v,size,max,label)=>{if(!Array.isArray(v)||v.length!==size)fail(label);v.forEach(x=>integer(x,0,max,label))};
 function validate(data){
  walk(data);
  if(!object(data)||data.format!=='PokemonProgramTransferHubBackup'||data.version!==2||!Array.isArray(data.archives)||!Array.isArray(data.pokemon)||data.archives.length>200||data.pokemon.length>20000)fail('format, version or counts');
  const archives=new Set(),pokemon=new Set();
  for(const a of data.archives){
   if(!object(a))fail('archive');id(a.id,'archive id');if(archives.has(a.id))fail('duplicate archive');archives.add(a.id);
   if(!profiles.has(a.profile)&&a.profile!=='unknown')fail('archive profile');text(a.name,255,'archive filename');
   if(a.bytesBase64!==undefined){if(typeof a.bytesBase64!=='string'||a.bytesBase64.length>2800000||! /^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$/.test(a.bytesBase64))fail('archive base64')}
  }
  for(const r of data.pokemon){
   if(!object(r))fail('Pokémon');id(r.id,'Pokémon id');if(pokemon.has(r.id))fail('duplicate Pokémon');pokemon.add(r.id);
   id(r.archiveId,'source archive');if(!archives.has(r.archiveId))fail('missing source archive');if(!profiles.has(r.sourceGame))fail('source game');
   integer(r.level,1,100,'level');integer(r.exp,0,2000000,'experience');integer(r.natureId,0,24,'nature');integer(r.abilityIndex,0,2,'ability');integer(r.itemId,0,65535,'item');integer(r.happiness,0,255,'friendship');integer(r.pid,0,4294967295,'PID');integer(r.otid,0,4294967295,'trainer id');
   integer(r.nationalId,0,1025,'National Dex');integer(r.unboundSpeciesId,0,2500,'Unbound species');if(!r.nationalId&&!r.unboundSpeciesId)fail('missing species');
   text(r.nickname,100,'nickname');text(r.species,200,'species name');if(typeof r.shiny!=='boolean')fail('shiny flag');
   list(r.moves,4,r.sourceGame==='unbound'?1023:354,'moves');
   for(const [field,max] of [['ivs',31],['evs',255]]){if(!object(r[field]))fail(field);for(const stat of ['HP','Atk','Def','Spe','SpA','SpD'])integer(r[field][stat],0,max,field+' '+stat)}
   for(const [key,max] of [['ppUps',255],['ballId',255],['language',255],['markings',255],['originInfo',65535],['pokerus',255],['metLocation',255],['ribbons',4294967295]])optionalInt(r,key,max);
   if(r.movePp!==undefined){if(!Array.isArray(r.movePp)||![0,4].includes(r.movePp.length))fail('move PP');r.movePp.forEach(x=>integer(x,0,255,'move PP'))}
   if(r.representations!==undefined){if(!object(r.representations))fail('representations');for(const [profile,rep] of Object.entries(r.representations)){if(!profiles.has(profile)||!object(rep))fail('representation');if(rep.raw!=null){if(!Array.isArray(rep.raw)||![58,80,100].includes(rep.raw.length))fail('raw record size');rep.raw.forEach(x=>integer(x,0,255,'raw byte'))}}}
  }
  return data;
 }
 globalThis.HubBackupValidation=Object.freeze({validate});
})();
