#!/usr/bin/env python3
"""Independent ARM030 native raw reconstruction. No producer imports/execution."""
import argparse,csv,hashlib,io,json,statistics,struct,subprocess,tarfile
from datetime import datetime,timezone
from decimal import Decimal,getcontext
from pathlib import Path
getcontext().prec=50
BASE='experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/030-frontend-diagnosis/'
CONTRACT='fa190bd9bdae6bbb40807d1cd5d6ea4b48908ac0'
DEADLINE=datetime(2026,10,19,11,45,tzinfo=timezone.utc)
MOD=1<<64
CACHE={};HASHES={};MODELS={}
def need(value,message):
    if not value:raise ValueError(message)
def sha(b):return hashlib.sha256(b).hexdigest()
def raw(rev,path):
    key=rev+':'+BASE+path
    if key not in CACHE:CACHE[key]=subprocess.check_output(['git','show',key])
    b=CACHE[key];HASHES[key]=sha(b);return b
def js(rev,path):return json.loads(raw(rev,path))
def date(s):return datetime.fromisoformat(s)
def load_phase(rev,phase):
    data=subprocess.check_output(['git','archive',rev,BASE+phase])
    with tarfile.open(fileobj=io.BytesIO(data)) as archive:
        for f in archive:
            if f.isfile():CACHE[rev+':'+f.name]=archive.extractfile(f).read()

def model(n,seed):
    if (n,seed) not in MODELS:
        state=seed
        def next_random():
            nonlocal state
            state=(state+0x9e3779b97f4a7c15)%MOD
            x=((state^(state>>30))*0xbf58476d1ce4e5b9)%MOD
            x=((x^(x>>27))*0x94d049bb133111eb)%MOD
            return x^(x>>31)
        for _ in range(16):next_random()
        order=list(range(n))
        for i in range(n-1,0,-1):
            j=next_random()%(i+1);order[i],order[j]=order[j],order[i]
        fingerprint=14695981039346656037
        for i in order:fingerprint=((fingerprint^i)*1099511628211)%MOD
        bits=sum(struct.unpack('<Q',struct.pack('<d',i-n//2))[0] for i in range(n))
        MODELS[(n,seed)]=dict(primary_one_traversal_checksum=n*(n-1)//2,h4_one_traversal_checksum=(bits+n)%MOD,h4_construction_fingerprint=fingerprint)
    return MODELS[(n,seed)]

def contract(phase):
    freeze=js(CONTRACT,'native-execution-freeze.json')
    for name,h in freeze['files'].items():need(sha(raw(CONTRACT,name))==h,'freeze '+name)
    cells=[]
    for frontend,direction in [('primary','forward'),('h4','forward'),('h4','reverse')]:
        for n in [100000,1000000]:cells.append(dict(id=f'{frontend}-{direction}-{n}',frontend=frontend,direction=direction,size=n,member_bytes=16,requested_ops=50000000 if frontend=='primary' else 20000000,warmup_passes=1 if frontend=='primary' else 3,score_contract='i' if frontend=='primary' else 'i-n/2',mask=4))
    need(cells==js(CONTRACT,'cells.json'),'cell inventory')
    runs=[]
    for block in range(6):
        for c in cells:
            for pos,label in enumerate(['control','A','A','control']):
                seed=1601+block%3
                args=['--size',str(c['size']),'--ops',str(c['requested_ops']),'--member-bytes','16','--seed',str(seed),'--warmup-passes',str(c['warmup_passes'])]
                args+=['--case','iterate'] if c['frontend']=='primary' else ['--direction',c['direction'],'--mask','4','--encoding','integer']
                runs.append(dict(index=len(runs),block=block,seed=seed,cell=c['id'],position=pos,label=label,source='control' if phase=='native-AA' else label,binary='actual',args=args))
    need(runs==js(CONTRACT,'schedules.json')[phase],'exact schedule')
    return {c['id']:c for c in cells},runs

def identity(got):
    ids=js(CONTRACT,'identities.json');expected={'binaries':{},'sources':{}}
    for name,b in ids['binaries'].items():
        expected['binaries'][name]=b['sha256'];s=dict(ids['source_hashes'])
        if name.endswith('-A'):s['src/zset_btree.c']=ids['candidate_source_sha256']
        if name.startswith('h4-'):s['bench/iterator_modes.c']=sha(raw(CONTRACT,'inputs/iterator_modes.c'))
        expected['sources'][name]=s
    need(got==expected,'complete source/binary identities')

def check_row(data,c,seed):
    rows=list(csv.DictReader(io.StringIO(data.decode())));need(len(rows)==1,'single raw row');r=rows[0]
    n=c['size'];visits=c['requested_ops'];passes=(visits+n-1)//n;expect=model(n,seed)
    need(expect==js(CONTRACT,'fixture-oracle.json')[f'{n}/{seed}'],'independent fixture oracle')
    checksum=expect[c['frontend']+'_one_traversal_checksum']*passes%MOD
    fields=dict(case='iterate' if c['frontend']=='primary' else 'iterator-modes',size=n,requested_ops=visits,operations=passes*n,member_bytes=16,seed=seed,traversals=passes,checksum=checksum,warmup_passes=c['warmup_passes'],cpu_start=2,cpu_end=2)
    if c['frontend']=='h4':fields.update(direction=c['direction'],mask=4,encoding='integer',expected_checksum=checksum,construction_fingerprint=expect['h4_construction_fingerprint'])
    for k,v in fields.items():need(r.get(k)==str(v),'row '+k)
    for k in ['elapsed_ns','thread_elapsed_ns','tree_bytes','warmup_elapsed_ns']:need(int(r[k])>0,'positive '+k)
    signature={k:r[k] for k in fields};signature['tree_bytes']=r['tree_bytes']
    return r,signature

def audit(rev,phase,earlier=None):
    load_phase(rev,phase);cells,schedule=contract(phase)
    seal=js(rev,phase+'-evidence-seal.json')
    for name,h in seal.items():need(sha(raw(rev,name))==h,'evidence seal '+name)
    publication=js(rev,phase+'/PUBLICATION.json')
    for name,v in publication.items():need(sha(raw(rev,phase+'/'+name))==v['public_sha256'],'publication '+name)
    s=js(rev,phase+'/result.json');need(s['status']=='complete' and s['phase']==phase and len(s['runs'])==144 and s['cpu']==2,'complete exact phase')
    need(s['freeze_sha256']==sha(raw(CONTRACT,'native-execution-freeze.json')),'execution freeze')
    scope=dict(unit_prefix='bplus-frontjob-20261019-',slice='bplus-front-20261019.slice',cpu=2,deadline=s['deadline'])
    need(s['lease_scope']==scope and date(s['deadline'])==DEADLINE,'new lease scope/deadline')
    need(len(s['lease_sha256'])==64 and all(c in '0123456789abcdef' for c in s['lease_sha256']),'lease hash format')
    identity(s['identities_before']);identity(s['identities_after'])
    start=date(s['started_utc']);end=date(s['finished_utc'])
    need(0<(end-start).total_seconds()<=600 and 0<s['elapsed_seconds']<=600 and (DEADLINE-start).total_seconds()>=620 and end<=DEADLINE,'phase cap/margin/deadline')
    refs={};blocks={};last=start;raw_hashes={}
    if earlier:
        need(date(earlier['finished_utc'])<start and earlier['lease_sha256']==s['lease_sha256'],'AA lease/serial join')
        need(s['AA_result_sha256']==earlier['raw_result_sha256'],'AA result identity')
        need(s['AA_audit_sha256']==sha(raw(rev,'native-AA/audit.json')),'AA producer audit identity')
        producer=js(rev,'native-AA/audit.json')
        need(producer['result_sha256']==earlier['raw_result_sha256'] and producer['raw_files_sha256']==earlier['raw_files_sha256'],'AA audit/raw result hash join')
        need(sha(raw(rev,'native-AA/result.json'))==earlier['raw_result_sha256'],'AA result retained')
        for name,h in earlier['raw_files_sha256'].items():need(sha(raw(rev,'native-AA/'+name))==h,'AA retained raw '+name)
    for expected,run in zip(schedule,s['runs']):
        need(all(run[k]==v for k,v in expected.items()),'run exact frozen schedule')
        need(run['stdout']==f'{expected["index"]:04d}.csv' and run['stderr']==f'{expected["index"]:04d}.stderr','raw filename identity')
        a=date(run['started_utc']);b=date(run['finished_utc']);need(last<=a<b<=end and (b-a).total_seconds()<=60,'serial child cap');last=b
        need(run['returncode']==0,'child rc');err=raw(rev,phase+'/'+run['stderr']);need(not err.strip(),'stderr')
        data=raw(rev,phase+'/'+run['stdout']);r,sig=check_row(data,cells[run['cell']],run['seed'])
        for name,bts in [(run['stdout'],data),(run['stderr'],err)]:raw_hashes[name]=sha(bts)
        key=(run['cell'],run['seed']);need(key not in refs or refs[key]==sig,'same-fixture exact semantics/memory');refs[key]=sig
        if earlier:need(earlier['_refs'][key]==sig,'AA corresponding fixture/memory')
        blocks.setdefault((run['cell'],run['block']),[]).append(r)
    output=[]
    for name in cells:
        effects=[]
        for block in range(6):
            rows=blocks[(name,block)];need(len(rows)==4,'four rows');ns=[int(r['elapsed_ns']) for r in rows]
            d=Decimal(100)*(Decimal(ns[1]+ns[2])/Decimal(ns[0]+ns[3])-1)
            effects.append(dict(block=block,seed=1601+block%3,effect_pct_decimal=str(d),minimum_window_ns=min(ns)))
        windows=all(e['minimum_window_ns']>=10000000 for e in effects)
        qualified=windows and (earlier['_qualified'][name] if earlier else all(abs(Decimal(e['effect_pct_decimal']))<=1 for e in effects))
        values=[Decimal(e['effect_pct_decimal']) for e in effects]
        direction='AA_QUALIFIED' if qualified else 'UNQUALIFIED'
        if earlier and qualified:direction='ALL_BLOCKS_FASTER' if all(v<0 for v in values) else 'ALL_BLOCKS_SLOWER' if all(v>0 for v in values) else 'MIXED'
        output.append(dict(id=name,qualified=qualified,observation=direction,blocks=effects,median_effect_pct_decimal=str(statistics.median(values))))
    return dict(integrity='PASS',revision=rev,phase=phase,processes=144,rows=144,blocks=36,cells=output,qualified_cells=sum(c['qualified'] for c in output),decision='DIAGNOSTIC_ONLY_PRIOR_REJECT_UNCHANGED',source_selection='NONE',started_utc=s['started_utc'],finished_utc=s['finished_utc'],elapsed_seconds=s['elapsed_seconds'],lease_sha256=s['lease_sha256'],raw_result_sha256=sha(raw(rev,phase+'/result.json')),raw_files_sha256=raw_hashes,verified_evidence_seals=len(seal),verified_publication_entries=len(publication),limitations=['Published immutable raw reconstruction; no live runner inspection or lease acquisition asserted.','Normalized public hashes verified; unavailable original private bytes are not rehashed.','Idle/preflight supplementary records require separate documented review; this script does not infer live idle or OSS state.','No candidate acceptance or profile authorization; qualified direction labels are descriptive, not promotion gates.'],_refs=refs,_qualified={c['id']:c['qualified'] for c in output})

def main():
    p=argparse.ArgumentParser();p.add_argument('--revision',required=True);p.add_argument('--phase',required=True,choices=['native-AA','native-comparison']);p.add_argument('--aa-revision');p.add_argument('--output',required=True,type=Path);a=p.parse_args()
    earlier=None
    if a.phase=='native-comparison':need(a.aa_revision is not None,'AA immutable revision required');earlier=audit(a.aa_revision,'native-AA')
    result=audit(a.revision,a.phase,earlier);a.output.mkdir(parents=True,exist_ok=False)
    for filename,report in [('raw-audit.json',result),('aa-raw-audit.json',earlier)]:
        if report is not None:(a.output/filename).write_text(json.dumps({k:v for k,v in report.items() if not k.startswith('_')},indent=2)+'\n')
    (a.output/'input-hashes.json').write_text(json.dumps(HASHES,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['cells','raw_files_sha256','limitations'] and not k.startswith('_')}))
if __name__=='__main__':main()
