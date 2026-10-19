def classify_pc(row,mapping):
 assert len(row)==6
 _,module,rawpc,rawbase,symbol,rawsym=row;pcval,base,sym=map(lambda x:int(x,16),[rawpc,rawbase,rawsym])
 aliases=(symbol,);section=None;image_pc=None;classification='external-symbol';limit=False
 if module==Path(PLAN['binary']).name:
  module='profile-program';aliases=();offset=None;image_start=None;symbol='unknown-own-image';classification='unmapped-own-image';limit=True
  if base and pcval>=base:
   image_pc=pcval-base;address=image_pc+mapping['image_vmaddr']
   matches=[s for s in mapping['sections'] if s['address']<=address<s['address']+s['size']]
   section=matches[0]['segment']+','+matches[0]['section'] if len(matches)==1 else None
   if mapping['text_start']<=address<mapping['text_end'] and address%4==0:
    addresses=[x['address'] for x in mapping['symbols']];i=bisect.bisect_right(addresses,address)-1
    if i>=0:
     entry=mapping['symbols'][i];offset=address-entry['address'];aliases=tuple(entry.get('aliases',[entry['name']]));symbol=entry['name'] if len(aliases)==1 else 'ambiguous-coalesced-symbol';image_start=entry['address']-mapping['image_vmaddr'];classification='text-symbol';limit=len(aliases)>1
   elif len(matches)==1 and matches[0]['segment']=='__TEXT' and matches[0]['section']=='__stubs':
    stub=matches[0];classification='import-stub';symbol='import-stub-unknown-target';offset=address-stub['address'];image_start=stub['address']-mapping['image_vmaddr'];limit=True
 else:offset=pcval-sym if sym and pcval>=sym else None;image_start=None
 module=module if re.fullmatch(r'[A-Za-z0-9_.-]{1,160}',module) else 'other-module'
 symbol=symbol if re.fullmatch(r'[A-Za-z0-9_.$-]{1,160}',symbol) else 'unknown'
 aliases=tuple(x if re.fullmatch(r'[A-Za-z0-9_.$-]{1,160}',x) else 'unknown' for x in aliases)
 return (module,symbol,offset,image_start,aliases,classification,image_pc,section,limit)

def derive(rec,paths,item,mapping):
 data=list(csv.DictReader(io.StringIO(paths['stdout'].read_text())));assert len(data)==1 and None not in data[0];r=data[0]
 case,n,seed=item['case'],item['size'],item['seed'];ops=10000000
 for key,value in dict(case=case,size=n,seed=seed,requested_ops=ops,member_bytes=16,warmup_passes=3).items():assert r[key]==str(value)
 operations,checksum=int(r['operations']),int(r['checksum']);owned=int(r['tree_bytes']);assert owned>0
 if case in ['lookup-hit','rank']:assert operations==ops and checksum==(n*(n-1)//2)*(ops//n) and int(r['traversals'])==0
 elif case=='lookup-miss':assert operations==ops and checksum==0 and int(r['traversals'])==0
 else:
  assert case=='scan' and int(r['traversals'])==ops//n and operations>=ops and operations%(ops//n)==0 and checksum%(ops//n)==0
 lines=paths['stderr'].read_text().splitlines();headers=[x for x in lines if x.startswith('PROFILE,')];assert len(headers)==1
 h=headers[0].split(',');assert len(h)==5 and h[1]==case and h[2]=='1000';count=int(h[3]);cap=int(h[4]);pc=[x.split(',') for x in lines if x.startswith('PC,')]
 assert count==len(pc) and cap==0 and count<=65536 and len(lines)==len(pc)+1
 bins=Counter(classify_pc(row,mapping) for row in pc)
 output=[dict(module=k[0],symbol=k[1],offset_bytes=k[2],symbol_image_offset=k[3],symbol_aliases=list(k[4]),symbol_ambiguous=len(k[4])>1,classification=k[5],own_image_pc_offset=k[6],section=k[7],mapping_limit=k[8],samples=v) for k,v in sorted(bins.items(),key=lambda x:repr(x[0]))]
 assert sum(x['samples'] for x in output)==count
 return dict(**item,requested_ops=ops,operations=operations,checksum=str(checksum),tree_bytes=owned,traversals=int(r['traversals']),sample_count=count,capped=False,sufficient=count>=10,sampler_usec_requested=1000,timing_fields_used=False,mapping_limit=any(x['mapping_limit'] for x in output),pc_bins=output)
