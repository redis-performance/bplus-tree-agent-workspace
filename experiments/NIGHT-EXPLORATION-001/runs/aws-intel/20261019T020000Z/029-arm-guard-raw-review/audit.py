#!/usr/bin/env python3
"""Independent immutable raw ARM guard reconstruction. No producer code imports."""
import argparse
import csv
from datetime import datetime,timezone
from decimal import Decimal,getcontext
import hashlib
import io
import json
from pathlib import Path
import statistics
import struct
import subprocess
import tarfile

getcontext().prec=50
BASE='experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/027-mask-followup/'
CONTRACT='380ef3109'
DEADLINE=datetime(2026,10,19,10,15,tzinfo=timezone.utc)
CASES=['insert','lookup-hit','lookup-miss','rank','iterate','scan','update','delete']
INPUTS={};CACHE={};SCORE_CACHE={}

def need(ok,why):
    if not ok:raise ValueError(why)
def digest(data):return hashlib.sha256(data).hexdigest()
def raw(rev,path):
    key=rev+':'+path
    if key not in CACHE:CACHE[key]=subprocess.check_output(['git','show',key])
    data=CACHE[key];INPUTS[key]=digest(data);return data
def js(rev,path):return json.loads(raw(rev,BASE+path))
def date(s):return datetime.fromisoformat(s)
def preload(rev,phase):
    names=[BASE+phase,BASE+phase+'-evidence-seal.json',BASE+phase+'-preflight.json',BASE+phase+'-post-identity-idle.json']
    archive=subprocess.check_output(['git','archive',rev,*names])
    with tarfile.open(fileobj=io.BytesIO(archive)) as stream:
        for item in stream:
            if item.isfile():CACHE[rev+':'+item.name]=stream.extractfile(item).read()

def contracts(phase):
    freeze=js(CONTRACT,'timing-freeze.json')
    for path,sha in freeze['files'].items():need(digest(raw(CONTRACT,BASE+path))==sha,'frozen file mismatch '+path)
    iterator=js(CONTRACT,'iterator-guards.json');original=js(CONTRACT,'original-guards.json')
    need(len(iterator)==82 and all(x['required_for_acceptance'] for x in iterator),'iterator inventory')
    need(len(original)==40 and sum(x['required_for_acceptance'] for x in original)==29,'original inventory')
    family=phase.split('-')[0];aa=phase.endswith('AA')
    cells=iterator if family=='iterator' else [dict(id=family+'-'+str(n),size=n) for n in ([100000,1000000] if family=='primary' else [100,1000,10000,100000,1000000])]
    frozen=js(CONTRACT,'schedules/'+phase+'.json');generated=[]
    for block in range(6):
        for cell in cells if block%2==0 else reversed(cells):
            for position,label in enumerate('ABBA'):
                seed=(1101 if family=='primary' else 1301)+block%3
                variant='control' if aa or label=='A' else 'A';n=cell['size']
                if family=='iterator':
                    full=cell
                    argv=['<job>/'+variant+'/build/native/'+('modes5' if cell['referee']=='HARNESS-005' else 'modes'),'--size',str(n),'--ops',str(cell['requested_ops']),'--member-bytes',str(cell['member_bytes']),'--seed',str(seed),'--mask',str(cell['mask']),'--direction',cell['direction'],'--encoding',cell['encoding'],'--warmup-passes','3']
                    if cell.get('construction'):argv+=['--construction',cell['construction']]
                else:
                    ops=50000000 if family=='primary' else 1000000;case='iterate' if family=='primary' else 'all'
                    full=dict(cell,member_bytes=16,requested_ops=ops,case=case,warmup_passes=1)
                    if family=='primary':full['required_for_acceptance']=True
                    program='<checkout>/scratch/'+('adapter-worktree-13e459ff8' if variant=='control' else 'arm-exp005A-replication-13e459ff8/A')+'/build/adapter-requalification/btree-bench'
                    argv=[program,'--case',case,'--size',str(n),'--ops',str(ops),'--member-bytes','16','--seed',str(seed)]
                generated.append(dict(index=len(generated),name=f"b{block}-{cell['id']}-p{position}-{label}",block=block,position=position,label=label,variant=variant,seed=seed,cell=full,command=argv))
    need(frozen==generated,'schedule differs from independently reconstructed contract')
    cap=next(x['cap_seconds'] for x in js(CONTRACT,'phase-budgets.json')['phases'] if x['name']==phase)
    return generated,cap,{(x['size'],x['case']):x['required_for_acceptance'] for x in original}

def expected_mode_checksum(cell):
    n=cell['size'];key=(n,cell['encoding'],cell['referee'])
    if key not in SCORE_CACHE:
        enc=cell['encoding'];total=0
        for i in range(n):
            if enc=='alternating-zero':value=-0.0 if i%2 else 0.0
            elif enc=='zero':value=float(i) if i else -0.0
            elif enc=='fraction':value=i-(n//2)+0.25
            elif enc=='wide':value=float(2**53+2*i)
            else:value=float(i-(n//2))
            bits=int.from_bytes(struct.pack('>d',value),'big')
            total+=bits if cell['referee']=='HARNESS-004' else bits^(bits>>32)
        SCORE_CACHE[key]=total
    per=n;mask=cell['mask']
    if mask&1:
        per+=sum((i&255) if cell['encoding']!='alternating-zero' else ((i>>56)&255) for i in range(n))
    if mask&2:per+=n*cell['member_bytes']
    if mask&4:per+=SCORE_CACHE[key]
    return per*((cell['requested_ops']+n-1)//n)%(1<<64)

def fixture(row,run,family):
    c=run['cell'];n=c['size'];ops=c['requested_ops'];case=row['case']
    for key,val in [('size',n),('seed',run['seed']),('requested_ops',ops),('member_bytes',c['member_bytes'])]:need(row[key]==str(val),'fixture '+key)
    need(row['cpu_start']==row['cpu_end']=='2','CPU endpoints')
    need(int(row['elapsed_ns'])>0 and int(row['tree_bytes'])>0,'elapsed or memory invalid')
    count=int(row['operations']);traversals=int(row['traversals']);checksum=int(row['checksum'])
    if family=='iterator':
        for key in ['direction','mask','encoding','warmup_passes']:need(row[key]==str(c[key]),'iterator '+key)
        if 'construction' in c:need(row['construction']==c['construction'],'construction')
        need(case=='iterator-modes' and traversals==(ops+n-1)//n and count==traversals*n,'mode visits')
        need(0<=int(row['construction_fingerprint'])<2**64,'construction fingerprint range')
        need(checksum==int(row['expected_checksum'])==expected_mode_checksum(c),'independent IEEE checksum')
    else:
        need(case in CASES and (family!='primary' or case=='iterate'),'case')
        need(row['warmup_passes']==('0' if case=='insert' else '1'),'warmup')
        expected_traversals=(ops+n-1)//n if case in ['iterate','scan'] else 0
        need(traversals==expected_traversals,'traversals')
        if case=='scan':
            need(count>=n*traversals and count%traversals==0 and checksum%traversals==0,'duplicate-aware scan counts')
            need(n*(n-1)//2*traversals<=checksum<=count*(n-1),'scan sum bounds')
        else:
            expected_count=n if case in ['insert','delete'] else traversals*n if case=='iterate' else ops
            need(count==expected_count and ops%n==0,'operation count')
            expected={'insert':0,'lookup-hit':ops*(n-1)//2,'lookup-miss':0,'rank':ops*(n-1)//2,'iterate':expected_count*(n-1)//2,'update':ops,'delete':n}[case]
            need(checksum==expected,'numeric checksum')

def identities(state,post,receipt,freeze_sha):
    need(state['timing_freeze_sha256']==freeze_sha and post['timing_freeze_sha256']==freeze_sha,'timing freeze provenance')
    need(state['composite_receipt_sha256']==digest(raw(CONTRACT,BASE+'composite-correctness.json')),'composite receipt')
    expected={}
    for variant in ['actual','actualA','control','A']:
        expected[variant]=dict(receipt['source_hashes'])
        if variant in ['actualA','A']:expected[variant]['src/zset_btree.c']=receipt['candidate_source_sha256']
    for suffix in ['before','after']:
        need(state['sources_'+suffix]==expected,'source/referee identity')
        need(state['protected_'+suffix]==receipt['protected_binaries'],'protected binaries')
        need(state['guard_binaries_'+suffix]==receipt['guard_binary_sha256'],'guard binaries')
        joined=state['composite_'+suffix]
        need(joined['receipt_sha256']==state['composite_receipt_sha256'] and joined['snapshots']==receipt['snapshots_before'],'composite snapshot join')
        for key in ['binding_sha256','original_raw_result_sha256','suffix_raw_result_sha256','guard_binary_sha256','protected_binaries']:need(joined[key]==receipt[key],'composite '+key)
        need(joined['original_status']=='failed' and joined['suffix_status']=='six_command_suffix_complete_pending_independent_closure','original/suffix status')
    need(state['composite_before']==state['composite_after'],'composite before/after')
    need(post['protected_binaries']==receipt['protected_binaries'] and post['guard_binary_sha256']==receipt['guard_binary_sha256'],'post-phase identities')
    need(post['snapshots']==receipt['snapshots_before'],'post-phase snapshots')
    need(post['actual_sources']=={k:expected[k] for k in ['actual','actualA']},'post-phase actual sources')
    need(post['owned_units']==[] and post['owned_cgroup_pids']==[],'post-phase owned workload not idle')
    need(date(post['lease_deadline'])==DEADLINE,'post-phase lease')

SIGNATURE=['size','seed','member_bytes','requested_ops','operations','checksum','tree_bytes','traversals','warmup_passes']
def signature(row,family):
    keys=SIGNATURE+(['direction','mask','encoding','construction_fingerprint','expected_checksum'] if family=='iterator' else [])
    if 'construction' in row:keys+=['construction']
    return {key:row[key] for key in keys}

def audit(rev,phase,previous=None):
    preload(rev,phase);schedule,cap,required=contracts(phase);family=phase.split('-')[0];aa=phase.endswith('AA')
    receipt=js(CONTRACT,'composite-correctness.json');freeze_sha=digest(raw(CONTRACT,BASE+'timing-freeze.json'))
    seal=js(rev,phase+'-evidence-seal.json')
    for path,sha in seal.items():need(digest(raw(rev,BASE+path))==sha,'public evidence seal '+path)
    publication=js(rev,phase+'/PUBLICATION.json')
    for path,entry in publication.items():need(digest(raw(rev,BASE+phase+'/'+path))==entry['public_sha256'],'publication join '+path)
    state=js(rev,phase+'/result.json');post=js(rev,phase+'-post-identity-idle.json');pre=js(rev,phase+'-preflight.json')
    need(state['status']=='complete' and state['phase']==phase and len(state['runs'])==len(schedule),'incomplete/wrong phase')
    need(state['schedule_sha256']==digest(raw(CONTRACT,BASE+'schedules/'+phase+'.json')),'schedule hash')
    need(post['timing_inputs']==js(CONTRACT,'timing-freeze.json')['files'],'post-phase input freeze')
    identities(state,post,receipt,freeze_sha)
    start=date(state['started_utc']);finish=date(state['finished_utc'])
    need(state['cap_seconds']==cap and 0<=state['elapsed_seconds']<=cap,'monotonic phase cap')
    need(0<=(finish-start).total_seconds()<=cap and finish<=DEADLINE and (DEADLINE-start).total_seconds()>=cap,'wall phase/deadline cap')
    need(date(pre['checked_utc'])<=start<=finish<=date(post['checked_utc']),'pre/post ordering')
    need(pre['remaining_seconds']>=cap and pre['released_marker'] is False and not pre['owned_units'] and not pre['owned_cgroup_pids'],'preflight idle/lease')
    need(pre['coordinator_returncode']==3 and 'STOPPED' in pre['coordinator_status'],'coordinator stopped')
    if not aa:
        need(previous is not None and date(previous['finished_utc'])<start,'missing or overlapping AA phase')
        need(previous['timing_freeze_sha256']==freeze_sha,'AA source protocol differs')
    groups={};references={};last=start;rows_count=0;per_seed={}
    for contract,run in zip(schedule,state['runs']):
        need(all(run[k]==v for k,v in contract.items()),'run contract mismatch')
        begin=date(run['started_utc']);end=date(run['finished_utc'])
        need(last<=begin<=end<=finish and (end-begin).total_seconds()<=60,'serial/child interval');last=end
        need(run['returncode']==0,'child failure')
        rows=list(csv.DictReader(io.StringIO(raw(rev,BASE+phase+'/'+run['name']+'.csv').decode())))
        need(rows==run['rows'] and len(rows)==(8 if family=='original' else 1),'raw row equality/count')
        raw(rev,BASE+phase+'/'+run['name']+'.stderr')
        if family=='original':need([r['case'] for r in rows]==CASES,'original operation order')
        for row in rows:
            fixture(row,run,family);rows_count+=1
            cellid=run['cell']['id']+'/'+row['case'];sig=signature(row,family);key=(run['block'],cellid)
            need(key not in references or references[key]==sig,'within-block exact outputs/memory')
            references[key]=sig
            seedkey=(run['seed'],cellid)
            need(seedkey not in per_seed or per_seed[seedkey]==sig,'repeated-seed fixture drift')
            per_seed[seedkey]=sig
            if not aa:need(previous['_references'][key]==sig,'same-fixture AA output/memory mismatch')
            groups.setdefault(cellid,{}).setdefault(run['block'],[]).append((run,row))
    cells=[]
    for cellid,blocks in sorted(groups.items()):
        need(set(blocks)==set(range(6)),'missing blocks');n=int(blocks[0][0][1]['size']);case=blocks[0][0][1]['case']
        must=required[(n,case)] if family=='original' else True;effects=[]
        for block,items in sorted(blocks.items()):
            need([x[0]['label'] for x in items]==list('ABBA') and [x[0]['position'] for x in items]==list(range(4)),'ABBA order')
            ns=[int(x[1]['elapsed_ns']) for x in items];effect=Decimal(100)*(Decimal(ns[1]+ns[2])/Decimal(ns[0]+ns[3])-1)
            effects.append(dict(block=block,seed=items[0][0]['seed'],effect_pct_decimal=str(effect),minimum_window_ns=min(ns)))
        windows=all(x['minimum_window_ns']>=10000000 for x in effects);values=[Decimal(x['effect_pct_decimal']) for x in effects]
        if aa:
            qualifies=windows and all(abs(v)<=1 for v in values);decision='QUALIFIED' if qualifies else ('PARK' if must else 'UNQUALIFIED_DIAGNOSTIC')
        else:
            qualifies=previous['_qualification'][cellid] and windows
            if not qualifies:decision='PARK' if must else 'UNQUALIFIED_DIAGNOSTIC'
            elif family=='primary':decision='PRIMARY_PASS' if all(v<=-2 for v in values) else 'REJECT'
            elif all(v<=1 for v in values):decision='GUARD_PASS'
            elif all(v>1 for v in values):decision='REJECT'
            else:decision='PARK'
        cells.append(dict(id=cellid,size=n,case=case,required_for_acceptance=must,qualified=qualifies,decision=decision,median_effect_pct_decimal=str(statistics.median(values)),blocks=effects))
    reject=any(c['decision']=='REJECT' for c in cells);park=any(c['decision']=='PARK' for c in cells)
    report=dict(integrity='PASS',revision=rev,phase=phase,processes=len(schedule),rows=rows_count,blocks=sum(len(c['blocks']) for c in cells),cells=cells,
        required_cells=sum(c['required_for_acceptance'] for c in cells),qualified_cells=sum(c['qualified'] for c in cells),all_required_qualified=all(c['qualified'] for c in cells if c['required_for_acceptance']),
        decision='REJECT' if reject else 'PARK' if park else 'QUALIFIED' if aa else 'PHASE_PASS_NOT_ACCEPTANCE',
        phase_gate_pass=not reject and not park,source_selection='NONE',timing_freeze_sha256=freeze_sha,started_utc=state['started_utc'],finished_utc=state['finished_utc'],elapsed_seconds=state['elapsed_seconds'],verified_public_seals=len(seal),verified_publication_entries=len(publication),
        limits=['Immutable published raw-data reconstruction, no producer code imported/executed and no new live runner inspection.','Public normalized bytes are verified against public hashes; unavailable original raw bytes are not claimed rehashed.','SCAN coverage relies on unchanged assertion-checked full seen/member/score referee plus duplicate-aware arithmetic and paired exact outputs.','Construction fingerprint range and equality are checked, not independently regenerated from RNG state.','Integrity PASS is separate from precision/performance gates; no source adoption or launch grant.'])
    report['_references']=references;report['_qualification']={c['id']:c['qualified'] for c in cells};return report

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--revision',required=True);p.add_argument('--phase',required=True,choices=['primary-AA','primary-replication','original-AA','original-comparison','iterator-AA','iterator-comparison']);p.add_argument('--aa-revision');p.add_argument('--output',required=True,type=Path);a=p.parse_args()
    earlier=None
    if not a.phase.endswith('AA'):
        need(a.aa_revision is not None,'comparison requires independent AA reconstruction');earlier=audit(a.aa_revision,a.phase.split('-')[0]+'-AA')
    result=audit(a.revision,a.phase,earlier);a.output.mkdir(parents=True,exist_ok=False)
    for name,report in [('raw-audit.json',result),('aa-raw-audit.json',earlier)]:
        if report is not None:(a.output/name).write_text(json.dumps({k:v for k,v in report.items() if not k.startswith('_')},indent=2)+'\n')
    (a.output/'input-hashes.json').write_text(json.dumps(INPUTS,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['cells','limits'] and not k.startswith('_')}))
if __name__=='__main__':main()
