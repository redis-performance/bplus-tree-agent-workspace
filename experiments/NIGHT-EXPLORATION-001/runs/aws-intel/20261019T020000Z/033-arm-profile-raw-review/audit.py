#!/usr/bin/env python3
"""Independent ARM030 profile reconstruction. No operator imports or execution.
Reuses only this reviewer's previously published native fixture model and Git IO.
"""
import argparse,collections,csv,hashlib,importlib.util,io,json,re,struct,sys
from decimal import Decimal as D,getcontext
from pathlib import Path
getcontext().prec=50
spec=importlib.util.spec_from_file_location('own_native_audit',Path(__file__).resolve().parent.parent/'031-arm-native-raw-review/audit.py')
N=importlib.util.module_from_spec(spec);spec.loader.exec_module(N)
PIN='2d4e93924';need=N.need;raw=N.raw;js=N.js;sha=N.sha;date=N.date
EVENTS={'cycles:u','instructions:u','branches:u','branch-misses:u'}

def assembly(text):
    result={};current=None;source=None
    for line in text.splitlines():
        m=re.fullmatch(r'\s*([0-9a-f]+) <([^>]+)>:',line)
        if m:
            current=m[2];need(current not in result,'duplicate assembly symbol')
            result[current]={'start':int(m[1],16),'code':{}};source=None;continue
        m=re.fullmatch(r'.*?([^/\s]+\.[ch]):(\d+)(?:\s.*)?',line)
        if m:source=(m[1],int(m[2]));continue
        m=re.match(r'^\s*([0-9a-f]+):\s+([0-9a-f]{8})\s+(.+)$',line)
        if m and current:
            offset=int(m[1],16)-result[current]['start'];need(offset>=0 and offset%4==0,'aligned assembly offset')
            need(offset not in result[current]['code'],'duplicate assembly instruction')
            result[current]['code'][offset]=(m[2],m[3],source)
    need(result,'nonempty assembly');return result

def match_instruction(diag,original,offset):
    if diag.keys()==original.keys() and all(diag[k][0]==original[k][0] for k in diag):return {'method':'whole_body_exact','offset':offset}
    delta=range(-12,13,4)
    if not all(offset+d in diag for d in delta):return {'method':'unmatched_boundary'}
    hits=[o for o in original if all(o+d in original and original[o+d][0]==diag[offset+d][0] for d in delta)]
    return {'method':'unique_seven_words','offset':hits[0]} if len(hits)==1 else {'method':'ambiguous_or_unmatched','matches':hits}

def samples(text):
    answer=[]
    for block in re.split(r'\n\s*\n',text.strip()):
        if not block.strip():continue
        lines=block.splitlines();need(re.fullmatch(r'\s*[0-9]+\s*',lines[0]),'raw sample period')
        period=int(lines[0]);need(period>0,'positive sample period');frames=[]
        for line in lines[1:]:
            m=re.fullmatch(r'\s*([0-9a-f]+)\s+(.+)',line);need(m is not None,'raw sample frame')
            frames.append({'pc':int(m[1],16),'label':m[2]})
        need(frames,'sample frames');pc=frames[0]['pc'];physical='[unknown]'
        for frame in frames:
            if frame['pc']==pc and '(inlined)' not in frame['label']:physical=frame['label']
        m=re.fullmatch(r'(.+?)\+0x([0-9a-f]+)',physical)
        answer.append(dict(period=period,pc=pc,symbol=m[1] if m else physical,offset=int(m[2],16) if m else None,frames=frames))
    return answer

def sample_report(text,rows):
    loss=re.search(r'Total Lost Samples:\s*(\d+)',text);count=re.search(r'Event count \(approx\.\):\s*(\d+)',text)
    need(loss is not None and count is not None,'report loss/event count')
    period=sum(r['period'] for r in rows);need(int(count[1])==period,'sample period equals report event count')
    label=re.search(r'^# Samples:\s*([^\n]+)',text,re.M)
    if label:
        plain=re.match(r'(\d+)\s+of event',label[1])
        if plain:need(int(plain[1])==len(rows),'sample number equals report')
    return dict(samples=len(rows),period=period,lost=int(loss[1]),sample_label=label[1] if label else None)

def stats(text,enabled):
    values={};runtimes={}
    for r in csv.reader(io.StringIO(text)):
        if not r or r[0].startswith('#'):continue
        need(len(r)>=3 and r[2] in EVENTS and r[2] not in values,'exact counter identity')
        v=r[0].strip();values[r[2]]=v
        if enabled:
            need(re.fullmatch('[0-9]+',v) is not None,'unscaled integer event')
            need(len(r)>=5 and D(r[3]).is_finite() and D(r[3])>0 and D(r[4]).is_finite() and D(r[4])==100,'reported runtime/100 percent')
            runtimes[r[2]]={'runtime_ns':r[3],'percent':r[4]}
        else:need(v in ['0','<not counted>'],'disabled counter zero')
    need(values.keys()==EVENTS,'all four counters')
    if enabled:
        for event in EVENTS:need(int(values[event])>=0 if event=='branch-misses:u' else int(values[event])>0,'positive enabled counter')
    return {'values':values,'runtime_pct':runtimes,'enabled':enabled}

def mode(c):return 'ASan_UBSan' if any(v.startswith('build/') and v.endswith('-san') for v in c['command']) else 'native'

def fixture(text,f):
    rows=list(csv.DictReader(io.StringIO(text)));need(len(rows)==1,'one fixture CSV row');r=rows[0]
    n=f['size'];m=N.model(n,f['seed']);t=(f['requested_ops']+n-1)//n
    expected=dict(case='iterate' if f['frontend']=='primary' else 'iterator-modes',size=n,seed=f['seed'],member_bytes=16,requested_ops=f['requested_ops'],operations=t*n,traversals=t,warmup_passes=f['warmup_passes'],cpu_start=2,cpu_end=2,checksum=m[f['frontend']+'_one_traversal_checksum']*t%N.MOD)
    if f['frontend']=='h4':expected.update(direction=f['direction'],mask=4,encoding='integer',expected_checksum=expected['checksum'],construction_fingerprint=m['h4_construction_fingerprint'])
    need(all(r.get(k)==str(v) for k,v in expected.items()),'independent fixture semantics')
    for k in ['tree_bytes','elapsed_ns','thread_elapsed_ns','warmup_elapsed_ns']:need(int(r[k])>0,'positive row '+k)
    signature={k:r[k] for k in expected};signature['tree_bytes']=r['tree_bytes'];return r,signature

DIGESTS={}
def score_digest(front,n):
    key=(front,n)
    if key not in DIGESTS:
        h=14695981039346656037
        for i in range(n):
            bits=struct.unpack('<Q',struct.pack('<d',float(i if front=='primary' else i-n//2)))[0]
            h=((h^bits)*1099511628211)%N.MOD
        DIGESTS[key]=h
    return DIGESTS[key]

def census(text,f,row):
    lines=text.splitlines();need(len(lines)==1 and lines[0].startswith('CENSUS '),'single census record');c=json.loads(lines[0][7:]);n=f['size']
    need(c['members']==n and c['tree_bytes']==int(row['tree_bytes']) and 0<c['leaves']<=n,'census count/memory')
    for name,length,total in [('width_entry_hist',65,n),('shift_entry_hist',65,n),('occupancy_leaf_hist',97,c['leaves'])]:
        h=c[name];need(len(h)==length and all(type(x)==int and x>=0 for x in h) and sum(h)==total,'census histogram '+name)
    need(sum(i*v for i,v in enumerate(c['occupancy_leaf_hist']))==n,'census occupied entries')
    joint=c['joint_leaf_hist'];need(all(len(x)==4 and 0<=x[0]<=64 and 0<=x[1]<=64 and x[2] in [0,1] and x[3]>0 for x in joint),'joint bins')
    need(sum(x[3] for x in joint)==c['leaves'] and sum(x[3] for x in joint if x[2])==c['reversed_leaves'],'joint census count')
    need(c['width0_entries']==c['width_entry_hist'][0] and c['width64_entries']==c['width_entry_hist'][64],'width0/64')
    need(c['width0_entries']+c['aligned_nonzero_entries']+c['unaligned_nonzero_entries']==n and 0<=c['ninth_byte_entries']<=c['unaligned_nonzero_entries'],'alignment census')
    need(c['transitions_per_traversal']==c['leaves']-1 and 0<=c['reversed_members']<=n,'transitions/reversal')
    need(c['score_digest']==score_digest(f['frontend'],n),'independent exact score digest')
    return c

def recurrence(mult,add,value,rounds):
    factor=1;offset=0
    while rounds:
        if rounds&1:factor=factor*mult%N.MOD;offset=(offset*mult+add)%N.MOD
        add=add*(mult+1)%N.MOD;mult=mult*mult%N.MOD;rounds//=2
    return f'{(factor*value+offset)%N.MOD:016x}'

def audit(rev):
    N.load_phase(rev,'profile');freeze=js(PIN,'profile-execution-freeze.json');commands=js(PIN,'profile-commands.json')
    need(len(commands)==642 and len(freeze['files'])==36,'frozen inventory')
    for path,h in freeze['files'].items():need(sha(raw(PIN,path))==h and sha(raw(rev,path))==h,'frozen bytes '+path)
    seal=js(rev,'profile-evidence-seal.json')['files']
    for path,h in seal.items():need(sha(raw(rev,path))==h,'publication seal '+path)
    pub=js(rev,'profile/PUBLICATION.json')
    for path,v in pub.items():need(sha(raw(rev,'profile/'+path))==v['public_sha256'],'normalized public hash '+path)
    s=js(rev,'profile/result.json');need(s['status']=='complete' and s['cpu']==2 and len(s['commands'])==642,'complete profile phase')
    need(s['execution_freeze_sha256']==sha(raw(PIN,'profile-execution-freeze.json')),'result freeze binding')
    scope=dict(unit_prefix='bplus-frontjob-20261019-',slice='bplus-front-20261019.slice',cpu=2,deadline='2026-10-19T11:45:00Z')
    need({**s['lease_scope'],'deadline':date(s['lease_scope']['deadline']).isoformat()}=={**scope,'deadline':N.DEADLINE.isoformat()},'lease namespace/CPU/deadline')
    start=date(s['started_utc']);end=date(s['finished_utc']);need(0<(end-start).total_seconds()<=1200 and 0<s['elapsed_seconds']<=1200 and (N.DEADLINE-start).total_seconds()>=1220 and end<=N.DEADLINE,'phase cap/start margin')
    N.identity(s['identities_before']);N.identity(s['identities_after']);ids=js(PIN,'identities.json')
    need(s['sources_before']==s['sources_after'] and s['binaries_before']==s['binaries_after'],'diagnostic before/after parity')
    need(set(s['sources_before'])==set(s['binaries_before'])=={'control','A'},'diagnostic sources exact set')
    for v,got in s['sources_before'].items():
        expected=dict(ids['source_hashes'])
        for name,h in freeze['files'].items():
            if name.startswith('inputs/') and Path(name).suffix in ['.c','.h']:expected['bench/'+Path(name).name]=h
        if v=='A':expected['src/zset_btree.c']=ids['candidate_source_sha256']
        need(got==expected,'diagnostic source exact identity')
    need(set(s['original_actual_text_identity'])==set(ids['binaries']),'four text identities')
    for key,v in s['original_actual_text_identity'].items():
        front,source=key.split('-');need(v['original_text_sha256']==v['actual_text_sha256'] and v['actual_binary_sha256']==ids['binaries'][key]['sha256'] and v['original_binary_sha256']==s['binaries_before'][source]['build/'+front+'-original'],'actual/rebuilt text binding')
    rows={};refs={};censuses={};counters={};warnings=[];last=start;rawhash={}
    known_expected={'before':recurrence(6364136223846793005,1442695040888963407,1,100000000),'inside':recurrence(2862933555777941757,3037000493,3,100000000),'after':recurrence(6364136223846793005,1442695040888963407,7,100000000),'rounds':100000000}
    for c,r in zip(commands,s['commands']):
        need(all(r[k]==v for k,v in c.items()),'exact command contract '+c['name']);a=date(r['started_utc']);b=date(r['finished_utc']);need(last<=a<b<=end and (b-a).total_seconds()<=120 and r['returncode']==0,'serial/child cap/rc');last=b
        files={suffix:raw(rev,'profile/'+c['name']+suffix) for suffix in ['.stdout','.stderr']}
        rawhash.update({c['name']+k:sha(v) for k,v in files.items()});text=files['.stdout'].decode();err=files['.stderr'].decode()
        if re.search(r'\b(lost|warning)\b',err,re.I):warnings.append({'command':c['name'],'stderr':err})
        if c['kind']=='original43':need('43 passed, 0 failed, 43 total' in re.sub(r'\x1b\[[0-9;]*m','',text),'original correctness suite')
        if c['fixture']:
            f=c['fixture'];row,sig=fixture(text,f);need(row==r['row'],'row recorded/raw join');rows[c['name']]=row
            key=(f['frontend'],f['direction'],f['size'],f['seed'],f['requested_ops'],mode(c));need(key not in refs or refs[key]==sig,'mode-specific source/fixture parity');refs[key]=sig
            if c['kind']=='census':
                obs=census(err,f,row);need(obs==r['census'] and (key not in censuses or censuses[key]==obs),'census source/mode parity');censuses[key]=obs
            elif c['kind'] in ['tree','instrument']:need(not err.strip(),'fixture stderr')
        if c['kind'] in ['tree-stat','disabled-stat','known-stat']:
            need('--no-scale' in c['command'],'explicit unscaled stat');enabled=c['kind']=='tree-stat' or c['name']=='known-enabled-stat';data=raw(rev,'profile/'+c['stat_file']);rawhash[c['stat_file']]=sha(data);obs=stats(data.decode(),enabled);need(obs==r['counters'],'counter raw/record join');counters[c['name']]=obs
        if c['kind'] in ['known','known-stat']:need(json.loads(text)==known_expected,'independent known recurrence expected output')
    need(len(counters)==42,'exact stat count')
    known_rows=samples(raw(rev,'profile/known-samples.stdout').decode());known_report=sample_report(raw(rev,'profile/known-report.stdout').decode(),known_rows)
    known_inside=[x for x in known_rows if x['symbol']=='known_work'];known_outside=[x for x in known_rows if x['symbol']=='outside_work']
    need(known_report['lost']==0 and len(known_inside)>=20 and sum(x['period'] for x in known_inside)*5>known_report['period']*4 and not known_outside,'known positive scoped sample gate')
    fault=samples(raw(rev,'profile/known-missing-disable-samples.stdout').decode());fr=sample_report(raw(rev,'profile/known-missing-disable-report.stdout').decode(),fault)
    need(fr['lost']==0 and any(x['symbol']=='outside_work' for x in fault) and s['scope_fault_detected'],'missing disable negative gate')
    need(len(s['raw_data_sha256'])==38 and all(re.fullmatch('[0-9a-f]{64}',v) for v in s['raw_data_sha256'].values()),'38 retained binary profile identities')
    maps={};body=[]
    for front in ['primary','h4']:
        for v in ['control','A']:
            key=front+'-'+v;parsed={kind:assembly(raw(rev,'profile/'+key+'-'+kind+'-full-asm.stdout').decode()) for kind in ['original','actual','profile']}
            def words(a):return {fn['start']+off:item[0] for fn in a.values() for off,item in fn['code'].items()}
            need(words(parsed['original'])==words(parsed['actual']),'rebuilt actual complete encoded listing')
            maps[key]=parsed
            for sym in sorted(set(parsed['profile'])|set(parsed['actual'])):
                if not (sym.startswith('zbt') or sym in ['main','traverse']):continue
                codes={kind:parsed[kind].get(sym,{}).get('code',{}) for kind in parsed};matches=collections.Counter()
                for off in codes['profile']:matches[match_instruction(codes['profile'],codes['actual'],off)['method']]+=1
                body.append(dict(binary=key,symbol=sym,instruction_counts={k:len(v) for k,v in codes.items()},diagnostic_actual_mapping=dict(matches)))
    profiles=[];alltree=True;allpc=True;allzero=True;linked_samples=[]
    for c in commands:
        if 'capture_file' not in c:continue
        label=c['capture_file'].removesuffix('.data');ss=samples(raw(rev,'profile/'+label+'-samples.stdout').decode());report=sample_report(raw(rev,'profile/'+label+'-report.stdout').decode(),ss)
        need(ss and report['period']>0,'nonempty scientific capture');allzero &= report['lost']==0
        m=maps[c['fixture']['frontend']+'-'+c['variant']];cats=collections.Counter();periods=collections.Counter();bases=set();treegood=True;matchcounts=collections.Counter();sampledetails=[]
        for x in ss:
            sym=x['symbol'];off=x['offset'];cat='unknown';detail=dict(x)
            if sym in m['profile'] and off in m['profile'][sym]['code']:
                fn=m['profile'][sym];address=fn['start']+off;base=x['pc']-address;need(base>=0 and base%4096==0,'physical PC/ELF load base');bases.add(base)
                links={kind:match_instruction(fn['code'],m[kind].get(sym,{}).get('code',{}),off) for kind in ['original','actual']};matched=all(z['method'] in ['whole_body_exact','unique_seven_words'] for z in links.values());matchcounts['matched' if matched else 'unmatched']+=1
                instruction=fn['code'][off];detail.update(elf_address=address,load_base=base,instruction=instruction,links=links)
                if sym.startswith('zbt'):
                    treegood &= matched;cat='IteratorNext_other' if sym=='zbtreeIteratorNext' else 'other_tree';src=instruction[2]
                    if src and src[0]=='zset_btree.c':
                        upper=518 if c['variant']=='control' else 517;shift=0 if c['variant']=='control' else -1
                        if 499<=src[1]<=upper:cat='packed_score_decoder'
                        elif sym=='zbtreeIteratorNext' and src[1] in [v+shift for v in [4041,4042,4043,4049,4050,4051]]:cat='IteratorNext_leaf_transition'
                elif sym=='traverse':cat='H4_consumer_traverse'
                elif sym=='main':cat='primary_consumer_main' if c['fixture']['frontend']=='primary' else 'H4_other_main'
                else:cat='scope_or_other_own_code'
            elif sym!='[unknown]' and not sym.startswith('0x'):cat='external_or_unmapped'
            cats[cat]+=1;periods[cat]+=x['period'];detail['exclusive_category']=cat;sampledetails.append(detail)
        need(len(bases)<=1,'single executable load base per capture');allpc &= bool(bases);alltree &= treegood
        profiles.append(dict(label=label,fixture=c['fixture'],variant=c['variant'],report=report,exclusive_events=dict(cats),exclusive_periods=dict(periods),mapping=dict(matchcounts),load_bases=sorted(bases),all_sampled_tree_bytes_match_actual=treegood));linked_samples.append(dict(label=label,samples=sampledetails))
    need(len(profiles)==36,'36 scientific captures')
    blocks=collections.defaultdict(list)
    for c in commands:
        if c['kind']=='instrument':blocks[(c['variant'],c['fixture']['id'],c['instrument_phase'],c['instrument_contract']['block'])].append((c,rows[c['name']]))
    need(len(blocks)==72,'72 instrumentation ABBA blocks');effects=[]
    for key,items in blocks.items():
        need(len(items)==4,'four instrumentation positions');v=[D(r['elapsed_ns'])/D(r['operations']) for _,r in items];effect=100*((v[1]+v[2])/(v[0]+v[3])-1);floor=min(int(r['elapsed_ns']) for _,r in items)
        effects.append(dict(source=key[0],cell=key[1],phase=key[2],block=key[3],effect_pct_decimal=str(effect),minimum_window_ns=floor,qualified=abs(effect)<=1 and floor>=10000000))
    qualifications=[]
    for source,cell in sorted({(e['source'],e['cell']) for e in effects}):
        subset=[e for e in effects if (e['source'],e['cell'])==(source,cell)];need(len(subset)==6,'six instrumentation controls per source/cell');qualifications.append(dict(source=source,cell=cell,elapsed_transfer_qualified=all(e['qualified'] for e in subset)))
    pairs=[]
    for cell in js(PIN,'cells.json'):
        for seed in [1701,1702,1703]:
            per={}
            for v in ['control','A']:
                name=f'{v}-{cell["id"]}-s{seed}-stat';per[v]={event:D(count)/D(rows[name]['operations']) for event,count in counters[name]['values'].items()}
            delta={e:str(100*(per['A'][e]/per['control'][e]-1)) if per['control'][e] else None for e in EVENTS}
            pairs.append(dict(cell=cell['id'],seed=seed,per_visit={v:{e:str(x) for e,x in values.items()} for v,values in per.items()},change_pct_decimal=delta,instructions_decreased=per['A']['instructions:u']<per['control']['instructions:u']))
    scopevalid=allzero and not warnings and allpc
    return dict(integrity='PASS',revision=rev,freeze_revision=PIN,commands=642,verified_freeze_inputs=36,evidence_seal_entries=len(seal),publication_entries=len(pub),result_sha256=sha(raw(rev,'profile/result.json')),started_utc=s['started_utc'],finished_utc=s['finished_utc'],elapsed_seconds=s['elapsed_seconds'],lease_sha256=s['lease_sha256'],source_selection='NONE',prior_decision='REJECT',scope_valid=scopevalid,code_attribution_valid=scopevalid and alltree,all_sampled_tree_bytes_match_actual=alltree,known_report=known_report,known_inside_events=len(known_inside),negative_scope_report=fr,negative_scope_outside_events=sum(x['symbol']=='outside_work' for x in fault),warnings=warnings,scientific_events=sum(p['report']['samples'] for p in profiles),scientific_period=sum(p['report']['period'] for p in profiles),profiles=profiles,complete_body_mapping=body,instrumentation_blocks=effects,instrumentation_qualification=qualifications,matched_counter_pairs=pairs,instruction_hypothesis='SUPPORTED' if scopevalid and all(p['instructions_decreased'] for p in pairs) else 'FALSIFIED' if scopevalid else 'INCONCLUSIVE',census=[dict(key=list(k),value=v) for k,v in censuses.items()],raw_hashes=rawhash,raw_data_sha256=s['raw_data_sha256'],limitations=['Local immutable public evidence only; no live runner access.','Binary perf.data and actual ELF bytes are not available here; published hashes and exported actual instruction bytes are checked, not unavailable files.','100.00% runtime is reported rounded precision, not proof of exact arbitrary precision enabled/running equality.','Exclusive period shares retain unknown/external frames in denominator; PC skid, caller attribution limits and scope boundaries remain.','Profile scope/count validity and instrumentation elapsed transfer are separate gates; neither can reverse prior REJECT.','Shared root cpu-perf consultation dfff5540f had zero indexed source passages; no independent direct cpu-perf tool was exposed.'],_samples=linked_samples)

def main():
    p=argparse.ArgumentParser();p.add_argument('--revision',required=True);p.add_argument('--output',required=True,type=Path);args=p.parse_args();result=audit(args.revision);args.output.mkdir(parents=True,exist_ok=False)
    (args.output/'audit.json').write_text(json.dumps({k:v for k,v in result.items() if not k.startswith('_')},indent=2)+'\n')
    (args.output/'sample-mapping.json').write_text(json.dumps(result['_samples'],indent=2)+'\n');(args.output/'input-hashes.json').write_text(json.dumps(N.HASHES,sort_keys=True,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['integrity','commands','scope_valid','code_attribution_valid','instruction_hypothesis','scientific_events']}))
if __name__=='__main__':main()
