#!/usr/bin/env python3
"""Offline EXP-009 PC conservation/map. No subprocess, build or workload path."""
from pathlib import Path
from collections import Counter,defaultdict
import argparse,csv,hashlib,io,json,re,struct
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def clean_name(value,fallback='unknown'):
    return value if re.fullmatch(r'[A-Za-z0-9_.$-]{1,160}',value) else fallback

def image_map(binary,nm_path=None):
    data=Path(binary).read_bytes()
    assert len(data)>=32 and struct.unpack_from('<I',data)[0]==0xfeedfacf,'expected little-endian Mach-O64'
    commands=struct.unpack_from('<I',data,16)[0];offset=32;sections=[];image=None
    for _ in range(commands):
        assert offset+8<=len(data)
        cmd,size=struct.unpack_from('<II',data,offset);assert size>=8 and offset+size<=len(data)
        if cmd==0x19:
            assert size>=72
            segment=data[offset+8:offset+24].split(b'\0')[0].decode()
            if segment=='__TEXT':image=struct.unpack_from('<Q',data,offset+24)[0]
            count=struct.unpack_from('<I',data,offset+64)[0];assert size>=72+count*80
            for j in range(count):
                pos=offset+72+j*80
                section=data[pos:pos+16].split(b'\0')[0].decode();seg=data[pos+16:pos+32].split(b'\0')[0].decode()
                addr,extent=struct.unpack_from('<QQ',data,pos+32)
                sections.append(dict(segment=seg,section=section,address=addr,size=extent))
        offset+=size
    assert image is not None
    text=[s for s in sections if s['segment']=='__TEXT' and s['section']=='__text'];assert len(text)==1
    lo=text[0]['address'];hi=lo+text[0]['size'];groups=defaultdict(list)
    if nm_path:
        for line in Path(nm_path).read_text().splitlines():
            match=re.fullmatch(r'([0-9a-fA-F]+)\s+([Tt])\s+(\S+)',line.strip())
            if match:
                address=int(match[1],16)
                if lo<=address<hi:
                    label=clean_name(match[3])
                    if label not in groups[address]:groups[address].append(label)
        assert groups,'nm supplied but no text symbols parsed'
    return dict(image=image,sections=sections,text_lo=lo,text_hi=hi,symbols=dict(groups))

def classify(fields,binary_name,mapping):
    assert len(fields)==6 and fields[0]=='PC'
    _,module,raw_pc,raw_base,label,raw_symbol=fields
    assert all(re.fullmatch(r'0x[0-9a-fA-F]+',x) for x in [raw_pc,raw_base,raw_symbol])
    pc,base,symbol_address=(int(x,16) for x in [raw_pc,raw_base,raw_symbol])
    own=module==binary_name
    out=dict(module='profile-program' if own else clean_name(module,'other-module'),symbol=clean_name(label),symbol_aliases=[],symbol_ambiguous=False,symbol_offset_bytes=None,own_image_pc_offset=None,symbol_image_offset=None,section=None,mapping_limit=True,classification='external-unknown')
    if not own:
        if label!='unknown' and clean_name(label)!='unknown' and symbol_address and pc>=symbol_address:
            out.update(symbol_aliases=[label],symbol_offset_bytes=pc-symbol_address,classification='external-dladdr-label',mapping_limit=False)
        return out
    out['symbol']='unknown-own-image';out['classification']='unmapped-own-image'
    if not base or pc<base:return out
    relative=pc-base;address=mapping['image']+relative;out['own_image_pc_offset']=relative
    sections=[s for s in mapping['sections'] if s['address']<=address<s['address']+s['size']]
    if len(sections)==1:out['section']=sections[0]['segment']+','+sections[0]['section']
    if mapping['text_lo']<=address<mapping['text_hi'] and address%4==0:
        preceding=[x for x in mapping['symbols'] if x<=address]
        if preceding:
            start=max(preceding);aliases=mapping['symbols'][start]
            out.update(symbol=aliases[0] if len(aliases)==1 else 'ambiguous-coalesced-symbol',symbol_aliases=aliases,symbol_ambiguous=len(aliases)>1,symbol_offset_bytes=address-start,symbol_image_offset=start-mapping['image'],classification='text-symbol',mapping_limit=len(aliases)>1)
        elif not mapping['symbols'] and symbol_address>=base:
            relative_symbol=symbol_address-base
            if mapping['text_lo']<=relative_symbol+mapping['image']<mapping['text_hi'] and pc>=symbol_address and clean_name(label)!='unknown':
                out.update(symbol=clean_name(label),symbol_aliases=[clean_name(label)],symbol_offset_bytes=pc-symbol_address,symbol_image_offset=relative_symbol,classification='own-text-dladdr-label')
    elif len(sections)==1 and sections[0]['segment']=='__TEXT' and sections[0]['section']=='__stubs':
        out.update(symbol='import-stub-unknown-target',classification='import-stub',symbol_offset_bytes=address-sections[0]['address'],symbol_image_offset=sections[0]['address']-mapping['image'])
    return out

def extract_assembly(path,image):
    wanted={'_zbtScoreLeafFindMember','_zbtScoreLeafScore','_zbtreeScoreRaw','_sampler_probe'};groups={};current=None
    for line in Path(path).read_text().splitlines():
        if re.fullmatch(r'_[A-Za-z0-9_.$]+:',line.strip()):
            current=line.strip()[:-1]
            if current in wanted:
                assert current not in groups,'duplicate wanted assembly label'
                groups[current]=[]
        elif current in wanted:
            match=re.match(r'^\s*([0-9a-fA-F]{8,16})\s+(.+)$',line)
            if match:groups[current].append((int(match[1],16),match[2]))
    normalized={};bounds={}
    for name,lines in groups.items():
        if not lines:continue
        while lines and re.fullmatch(r'nop(?:\s*;.*)?',lines[-1][1].strip()):lines.pop()
        if not lines:continue
        assert lines[0][0]%4==0 and [address for address,_ in lines]==list(range(lines[0][0],lines[-1][0]+4,4)),'unaligned/noncontiguous assembly instructions'
        start=lines[0][0];normalized[name]=[dict(offset_bytes=address-start,instruction=re.sub(r'/'+r'(?:Us'+r'ers|ho'+r'me)/[^\s\"]+','<private-path>',text)) for address,text in lines]
        bounds[name]=dict(image_start=start-image,image_end=lines[-1][0]+4-image,method='First through last retained otool instruction plus4; trailing nop padding excluded')
    return dict(sha256=sha(path),functions=normalized,function_bounds=bounds,instruction_counts={n:len(v) for n,v in normalized.items()},roundtrip_inspection='Retained fresh static instructions only. Manually inspect physical-to-logical mapping and decoder remapping; no automatic cost, speed or mechanism conclusion. Missing/inlined symbols remain a mapping limit.')

def map_profile(stdout_path,stderr_path,binary,nm_path=None,assembly_path=None,min_samples=None):
    mapping=image_map(binary,nm_path);lines=Path(stderr_path).read_text().splitlines()
    assert lines and lines[0].startswith('PROFILE,')
    header=lines[0].split(',');assert len(header)==5
    _,scope,interval,total,capped=header;assert clean_name(scope)==scope
    usec=int(interval);count=int(total);cap=int(capped)
    assert usec==1000 and cap==0 and 0<=count<=65536 and len(lines)==count+1
    observations=[]
    for index,line in enumerate(lines[1:]):observations.append(dict(ordinal=index,**classify(line.split(','),Path(binary).name,mapping)))
    assert len(observations)==count
    text=Path(stdout_path).read_text();semantics=None;control_result=None
    if re.fullmatch(r'result,[0-9]+\n?',text):kind='sampler-control';control_result=text.strip().split(',')[1]
    elif not text.strip():kind='sampler-control'
    else:
        reader=csv.DictReader(io.StringIO(text));rows=list(reader);assert len(rows)==1 and None not in rows[0]
        row=rows[0];assert row.get('case')==scope
        kind='lookup-capture';keys=['case','size','requested_ops','member_bytes','seed','operations','tree_bytes','checksum','traversals','warmup_passes']
        assert all(key in row for key in keys)
        for key in keys[1:]:assert re.fullmatch(r'[0-9]+',row[key])
        assert int(row['operations'])>0 and int(row['tree_bytes'])>0
        semantics={key:row[key] for key in keys}
    minimum=25 if min_samples is None else min_samples
    assert minimum>=25,'protocol minimum cannot be reduced'
    validity_errors=[]
    if count<minimum:validity_errors.append('insufficient fresh capture; retain all observations; no retry')
    counts=Counter(json.dumps({k:v for k,v in x.items() if k!='ordinal'},sort_keys=True) for x in observations)
    bins=[dict(json.loads(key),samples=value) for key,value in sorted(counts.items())]
    assert sum(x['samples'] for x in bins)==count
    symbols=Counter();classes=Counter()
    for x in bins:symbols[x['symbol']]+=x['samples'];classes[x['classification']]+=x['samples']
    assembly=extract_assembly(assembly_path,mapping['image']) if assembly_path else None
    probe_extent=assembly['function_bounds'].get('_sampler_probe') if assembly else None
    if probe_extent:
        probe_start=mapping['image']+probe_extent['image_start'];probe_end=mapping['image']+probe_extent['image_end']
        assert mapping['text_lo']<=probe_start<probe_end<=mapping['text_hi']
        assert mapping['symbols'].get(probe_start)==['_sampler_probe'],'probe extent must match unique actual nm entry'
        assert not any(probe_start<address<probe_end for address in mapping['symbols']),'probe extent crosses another text symbol'
        instructions=assembly['functions']['_sampler_probe'];assert [x['offset_bytes'] for x in instructions]==list(range(0,probe_end-probe_start,4))
    probe=sum(1 for x in observations if probe_extent and x['module']=='profile-program' and x['own_image_pc_offset'] is not None and x['own_image_pc_offset']%4==0 and probe_extent['image_start']<=x['own_image_pc_offset']<probe_extent['image_end'])
    if kind=='sampler-control':
        if scope!='sampler_probe' or control_result!='1128443088728658433':validity_errors.append('wrong known calibration work/result')
        if probe_extent is None or probe!=count:validity_errors.append('control PCs must all lie in actual probe instruction extent; no exclusions')
    result=dict(status='PASS' if not validity_errors else 'FAIL',validity_errors=validity_errors,kind=kind,scope=scope,sample_count=count,minimum_required=minimum,sufficient=count>=minimum,capped=False,sampler_usec=usec,binary_sha256=sha(binary),stdout_sha256=sha(stdout_path),stderr_sha256=sha(stderr_path),nm_sha256=sha(nm_path) if nm_path else None,csv_semantics=semantics,control_result=control_result,probe_symbol_samples=probe,symbol_counts=dict(symbols),classification_counts=dict(classes),observations=observations,pc_bins=bins,all_observations_conserved=True,timing_fields_used=False,source_candidate='NONE',limitations='PC observations and static locations only, not cycles, latency, unbiased frequencies/time shares, cache evidence or speed. External names are dladdr labels. Import targets/unaligned/nontext PCs remain unknown; aliases retain ambiguity. Timing/semantic oracle qualification is separate.')
    result['image_sections']=[dict(segment=s['segment'],section=s['section'],relative_start=s['address']-mapping['image'],size=s['size']) for s in mapping['sections']]
    result['probe_extent']=probe_extent
    result['probe_extent_samples']=probe
    if assembly:result['assembly']=assembly
    return result

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--stdout',required=True);parser.add_argument('--stderr',required=True);parser.add_argument('--binary',required=True);parser.add_argument('--nm');parser.add_argument('--assembly');parser.add_argument('--output',required=True);parser.add_argument('--min-samples',type=int)
    args=parser.parse_args();out=Path(args.output);assert not out.exists(),'no overwrite'
    result=map_profile(args.stdout,args.stderr,args.binary,args.nm,args.assembly,args.min_samples)
    result['mapper_sha256']=sha(__file__)
    with out.open('x') as target:target.write(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','kind','scope','sample_count','probe_symbol_samples','classification_counts']}))
    if result['status']!='PASS':raise SystemExit(1)
if __name__=='__main__':main()
