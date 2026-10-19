#!/usr/bin/env python3
"""EXP-009 baseline prerequisites only. Every native phase requires root's frozen ACK."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,array,csv,hashlib,io,json,math,os,re,signal,subprocess,sys,time
R=Path.cwd(); E=Path(__file__).resolve().parent; REL=E.relative_to(R)
BUILD=Path('build/exp009-baseline'); PRIVATE=Path('scratch/exp009-driver')
ENV={'PATH':'/usr/bin:/bin:/usr/sbin:/sbin','LANG':'C','LC_ALL':'C','TZ':'UTC'}
SIGS={signal.SIGALRM,signal.SIGINT,signal.SIGTERM,signal.SIGHUP}
NATIVE=['-std=c11','-O3','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer','-fno-lto']
SAN=['-std=c11','-O1','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer','-fno-lto','-fsanitize=address,undefined','-fno-sanitize-recover=all']
INC=['-Isrc','-Icompat','-Ivendor/redis'];COMMON=['src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm']
EXPECTED={'src/zset_btree.c':'d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2','src/zset_btree.h':'496e72ff9dacb26793c64ba8794e2943dc9b678a8476cc1ae99d36d2b1d87a83','compat/server.h':'468a5811ad80fa4dc47196b90835586cbbbd8b7d235af225092637e930708fa7','compat/standalone.c':'c9237cd2e2fb08fff5c67431a9de5d6d1596d6211082a068116040c477689fb3'}
MASK=(1<<64)-1;MODELS={}
CSV_HEADER='case,size,requested_ops,member_bytes,seed,operations,elapsed_ns,ns_per_op,ops_per_sec,tree_bytes,checksum,thread_elapsed_ns,cpu_start,cpu_end,qos_reported_start,qos_reported_end,qos_relpri_start,qos_relpri_end,qos_effective,traversals,warmup_passes,warmup_elapsed_ns'.split(',')
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def utc():return datetime.now(timezone.utc).isoformat()
def load(path):return json.loads(Path(path).read_text())
def safe(text):
    text=text.replace(str(R),'<workspace>')
    return re.sub(r'/(?:Users|home)/[^/\s]+','<user-home>',text)
def save(path,value):
    path=Path(path);tmp=Path(str(path)+'.tmp');tmp.write_text(json.dumps(value,indent=2)+'\n');tmp.replace(path)
def verify(table):
    for name,want in table.items():
        path=Path(name);assert not path.is_absolute() and '..' not in path.parts,'relative frozen paths required'
        assert path.is_file() and sha(path)==want,'frozen identity mismatch: '+name
    for name,want in EXPECTED.items():assert sha(name)==want,'corrected source identity mismatch'
def alive(group):
    try:os.killpg(group,0);return True
    except ProcessLookupError:return False
def cancel(signum,frame):raise TimeoutError('phase interrupted or parent deadline reached')
def check_plan(plan):
    assert plan['source_commit']=='d13b3598f6e859969c764daf9982998f87233f73'
    required={'primary_sizes':[100000,1000000],'case':'lookup-hit','member_bytes':16,'calibration_operations':200000,'calibration_replicates':3,'target_elapsed_ns':600000000,'maximum_operations':100000000,'minimum_elapsed_ns':10000000,'discovery_seeds':[1,2,3,1,2,3],'qualification_phase_wall_limit_seconds':600,'profile_operations':10000000,'profile_seeds':[1],'profile_minimum_samples':25,'sampler_control_replicates':2,'ABBA':'ABBA'}
    for key,value in required.items():assert plan[key]==value,'preregistered contract mismatch: '+key

def model(n,seed):
    key=(n,seed)
    if key not in MODELS:
        order=list(range(n));state=seed ^ 0xd02703a89f4c51e7
        for i in range(n,1,-1):
            state=(state+0x9e3779b97f4a7c15)&MASK;z=state
            z=((z^(z>>30))*0xbf58476d1ce4e5b9)&MASK;z=((z^(z>>27))*0x94d049bb133111eb)&MASK;z^=z>>31
            j=z%i;order[i-1],order[j]=order[j],order[i-1]
        packed=array.array('Q',order)
        if sys.byteorder!='little':packed.byteswap()
        MODELS[key]=(order,hashlib.sha256(packed.tobytes()).hexdigest())
    return MODELS[key]
def expected_checksum(case,n,ops,seed):
    order,digest=model(n,seed);whole,tail=divmod(ops,n)
    if case=='lookup-hit':value=whole*(n*(n-1)//2)+sum(order[:tail])
    elif case=='lookup-miss':value=0
    else:
        assert case=='lookup-mixed' and n%2==0
        value=whole*sum(x+1 for i,x in enumerate(order) if i%2==0)+sum(order[i]+1 for i in range(0,tail,2))
    return value&MASK,digest

def lookup_cmd(binary,n,ops,seed,case='lookup-hit',member=16):
    return [str(binary),'--case',case,'--size',str(n),'--ops',str(ops),'--seed',str(seed),'--member-bytes',str(member),'--warmup-passes','1']
def parse_csv(paths,n,ops,seed,case='lookup-hit',member=16,profile=False):
    if not profile:assert paths['stderr'].stat().st_size==0,'unexpected native stderr; raw retained'
    reader=csv.DictReader(io.StringIO(paths['stdout'].read_text()));rows=list(reader)
    assert reader.fieldnames==CSV_HEADER and len(rows)==1 and None not in rows[0] and all(v is not None for v in rows[0].values()),'exact frozen CSV header/row shape required';r=rows[0]
    for key,value in {'case':case,'size':n,'requested_ops':ops,'member_bytes':member,'seed':seed,'operations':ops,'warmup_passes':1,'traversals':0}.items():assert r[key]==str(value),'CSV contract mismatch: '+key
    checksum,digest=expected_checksum(case,n,ops,seed);assert int(r['checksum'])==checksum,'independent query checksum mismatch'
    elapsed=int(r['elapsed_ns']);owned=int(r['tree_bytes']);assert elapsed>0 and owned>0
    for key,value in r.items():
        if key in ['case','qos_reported_start','qos_reported_end','qos_effective']:assert re.fullmatch(r'[A-Za-z0-9_-]{1,80}',value),'noncanonical CSV text'
        elif key in ['ns_per_op','ops_per_sec']:assert re.fullmatch(r'(0|[1-9][0-9]*)\.[0-9]{3}',value),'noncanonical rounded rate'
        else:assert re.fullmatch(r'-?(0|[1-9][0-9]*)',value) and value!='-0','noncanonical integer metadata'
    assert int(r['warmup_elapsed_ns'])>=0 and int(r['thread_elapsed_ns'])>=-1 and int(r['cpu_start'])>=-1 and int(r['cpu_end'])>=-1
    assert all(math.isfinite(float(r[k])) for k in ['ns_per_op','ops_per_sec'])
    assert abs(float(r['ns_per_op'])-elapsed/ops)<=.0006 and abs(float(r['ops_per_sec'])-ops*1e9/elapsed)<=.0006,'rounded rate inconsistent'
    fingerprint={key:r[key] for key in ['case','size','requested_ops','member_bytes','seed','operations','warmup_passes','traversals','checksum','tree_bytes']}
    return {'csv':r,'elapsed_ns':elapsed,'operations':ops,'checksum':str(checksum),'tree_bytes':owned,'query_order_sha256_le_u64':digest,'fingerprint':fingerprint,'output_mode':'score nonNULL / public zbtreeScore'}

def run(owner,cmd,name,extra_env=None,expect=0,max_seconds=60):
    owner.bound();raw=owner.raw;paths={k:raw/(name+'.'+k) for k in ['stdout','stderr']};assert not any(p.exists() for p in paths.values()),'no raw overwrite'
    cap=min(max_seconds,owner.remaining()-10);assert cap>0
    record={'name':name,'command':list(map(str,cmd)),'cwd':'.','environment':dict(ENV,**(extra_env or {})),'started_utc':utc(),'timeout_seconds':cap,'timed_out':False,'child_reaped':False,'owned_group_empty':False,'release_safe':False}
    child=None;started=time.monotonic();owner.state['release_safe']=False;owner.persist()
    try:
        with paths['stdout'].open('xb') as out,paths['stderr'].open('xb') as err:
            spawn_mask=signal.pthread_sigmask(signal.SIG_BLOCK,SIGS)
            try:child=subprocess.Popen(record['command'],stdout=out,stderr=err,env=record['environment'],start_new_session=True,preexec_fn=lambda:signal.pthread_sigmask(signal.SIG_SETMASK,spawn_mask))
            finally:signal.pthread_sigmask(signal.SIG_SETMASK,spawn_mask)
            while child.poll() is None:
                if time.monotonic()-started>=cap or owner.remaining()<=10:record['timed_out']=True;break
                time.sleep(.025)
    except BaseException as ex:record['exception_type']=type(ex).__name__;raise
    finally:
        mask=signal.pthread_sigmask(signal.SIG_BLOCK,SIGS)
        try:
            if child is not None:
                if alive(child.pid):
                    try:os.killpg(child.pid,signal.SIGTERM);record['term_sent']=True
                    except ProcessLookupError:record['term_exit_race']=True
                    until=time.monotonic()+1
                    while alive(child.pid) and time.monotonic()<until:time.sleep(.025)
                if alive(child.pid):
                    try:os.killpg(child.pid,signal.SIGKILL);record['kill_sent']=True
                    except ProcessLookupError:record['kill_exit_race']=True
                try:child.wait(timeout=4);record['child_reaped']=True
                except subprocess.TimeoutExpired:pass
                until=time.monotonic()+3
                while alive(child.pid) and time.monotonic()<until:time.sleep(.025)
                record.update(owned_group_empty=not alive(child.pid),returncode=child.returncode)
            record.update(finished_utc=utc(),wall_seconds=time.monotonic()-started,raw={})
            for channel,path in paths.items():
                if path.exists():record['raw'][channel]={'path':str(path),'sha256':sha(path),'bytes':path.stat().st_size}
            record['release_safe']=record['child_reaped'] and record['owned_group_empty']
            with (owner.out/'commands.jsonl').open('a') as f:f.write(json.dumps(record)+'\n');f.flush();os.fsync(f.fileno())
            owner.records.append(record);owner.state['release_safe']=all(r['release_safe'] for r in owner.records);owner.persist()
        finally:signal.pthread_sigmask(signal.SIG_SETMASK,mask)
    owner.bound();assert not record['timed_out'] and record['release_safe'] and record.get('returncode')==expect,'child failed; private raw retained: '+name
    return paths

class Owner:
    def __init__(self,phase,ack,manifest,manifest_path,plan):
        self.phase=phase;self.plan=plan;self.manifest=manifest;self.manifest_path=manifest_path;self.records=[];self.prerequisite_hashes={};self.started=time.monotonic()
        self.limit={'build':600,'calibrate':180,'profile':180,'aa':600}[phase]
        self.deadline=min(time.time()+self.limit,datetime.fromisoformat(plan['overall_stop_utc']).timestamp(),datetime.fromisoformat(ack['absolute_stop_utc']).timestamp());assert self.deadline-time.time()>20
        self.out=E/('profile-results/run' if phase=='profile' else 'bench-results/'+phase);self.raw=PRIVATE/phase/'raw'
        assert not self.out.exists() and not self.raw.parent.exists(),'no phase retry/overwrite'
        self.out.mkdir(parents=True);self.raw.mkdir(parents=True)
        self.state={'status':'RUNNING','phase':phase,'started_utc':utc(),'manifest_sha256':sha(manifest_path),'published_commit':ack['published_commit'],'wall_limit_seconds':self.limit,'release_safe':True,'source_adoption':'NONE','placement':'native macOS unpinned; CPU/thread/QoS endpoints are observations only','participant':'/root','driver_author':'/root/followup_proposal_b','backend':'Inherited Codex/GPT-6 family; exact model/token/currency costs unknown'}
    def remaining(self):return min(self.deadline-time.time(),self.limit-(time.monotonic()-self.started))
    def bound(self):assert self.remaining()>0,'phase/global deadline reached'
    def persist(self):save(self.out/'status.json',self.state)
    def finish(self,error=None):
        final_error=None
        try:
            verify(self.manifest['files_sha256']);verify(self.prerequisite_hashes);assert sha(self.manifest_path)==self.state['manifest_sha256'],'manifest changed';self.bound()
            self.state['post_frozen_entries_verified']=len(self.manifest['files_sha256'])
            if error:self.state.update(status='INCOMPLETE; preserve evidence; no retry',exception_type=type(error).__name__)
        except BaseException as ex:self.state.update(status='INCOMPLETE; preserve evidence; no retry',finalization_exception_type=type(ex).__name__);final_error=ex
        finally:
            mask=signal.pthread_sigmask(signal.SIG_BLOCK,SIGS)
            try:
                self.state.update(finished_utc=utc(),phase_wall_seconds=time.monotonic()-self.started,journaled_attempts=len(self.records),release_safe=all(r['release_safe'] for r in self.records))
                if self.remaining()<=0:self.state['status']='INCOMPLETE; deadline reached'
                self.persist()
                if self.remaining()<=0:self.state['status']='INCOMPLETE; final serialization crossed deadline';self.persist();final_error=TimeoutError('final serialization deadline')
                signal.setitimer(signal.ITIMER_REAL,0)
            finally:signal.pthread_sigmask(signal.SIG_SETMASK,mask)
        if final_error:raise final_error

def compile_binary(o,name,source,mode='native',include_tree=True,defines=()):
    path=BUILD/mode/name;path.parent.mkdir(parents=True,exist_ok=True);assert not path.exists()
    flags=SAN if mode=='san' else NATIVE
    cmd=['clang',*flags,*defines,'-I.',*INC,str(source),*(COMMON if include_tree else COMMON[1:]),'-o',str(path)]
    run(o,cmd,'compile-'+mode+'-'+name,max_seconds=120);assert path.is_file();return path

def build(o):
    assert not BUILD.exists(),'no build overwrite';BUILD.mkdir(parents=True)
    binaries={}
    for mode in ['native','san','profile']:
        binaries[mode]=compile_binary(o,'lookup',REL/'harness/lookup.c',mode,defines=['-DLOOKUP_PROFILE'] if mode=='profile' else [])
    for mode in ['native','san']:
        test=compile_binary(o,'original43','tests/upstream.c',mode,defines=['-DREDIS_TEST','-DREDIS_DEBUG']);binaries['tests-'+mode]=test
        paths=run(o,[test],mode+'-original43',max_seconds=120);text=paths['stdout'].read_text();assert paths['stderr'].stat().st_size==0 and '43 passed' in text and '0 failed, 43 total' in text
        assert [int(x) for x in re.findall(r'^(\d+) - .*PASSED',text,re.M)]==list(range(1,44))
        oracle=compile_binary(o,'physical-oracle',REL/'harness/physical-oracle.c',mode,include_tree=False);binaries['oracle-'+mode]=oracle
        paths=run(o,[oracle],mode+'-physical-oracle',max_seconds=120);assert paths['stderr'].stat().st_size==0
        assert paths['stdout'].read_text()=='PASS cells=4160 exact-score/position/output checks=515840; widths0..64 shifts0/3 reversed both signed-zero ties colliding-tags first-match misses\n'
        for member in [8,16,319,320,321,1024]:
            for case in ['lookup-hit','lookup-miss','lookup-mixed']:
                paths=run(o,lookup_cmd(binaries[mode],1000,2003,1,case,member),mode+'-'+case+'-m'+str(member),max_seconds=120);row=parse_csv(paths,1000,2003,1,case,member)
                save(o.out/(mode+'-'+case+'-m'+str(member)+'.json'),row)
        for name,args in [('bogus',['--case','bogus']),('all',['--case','all']),('missing',['--case']),('length7',['--case','lookup-hit','--size','100','--ops','203','--member-bytes','7'])]:
            paths=run(o,[binaries[mode],*args],mode+'-invalid-'+name,expect=2,max_seconds=120);assert paths['stderr'].stat().st_size>0
    binaries['sampler']=compile_binary(o,'sampler-control',REL/'harness/sampler-calibration.c','profile',include_tree=False)
    compiler=run(o,['clang','--version'],'compiler',max_seconds=30);compiler_text=safe(compiler['stdout'].read_text());assert compiler['stderr'].stat().st_size==0
    metadata={}
    for mode in ['native','profile','sampler']:
        paths={}
        for tool,args in [('nm',['nm','-n',binaries[mode]]),('assembly',['otool','-tvV',binaries[mode]])]:
            captured=run(o,args,mode+'-'+tool,max_seconds=30);assert captured['stderr'].stat().st_size==0;paths[tool]=str(captured['stdout'])
        metadata[mode]=paths
    assembly=Path(metadata['native']['assembly']).read_text();snippets={}
    for name in ['_zbtScoreLeafFindMember','_zbtreeScoreRaw','_zbtreeScore']:
        match=re.search(r'^'+re.escape(name)+r':\n(.*?)(?=^_[A-Za-z0-9_.$]+:|\Z)',assembly,re.M|re.S)
        if match:snippets[name]=safe(match[1])
    assert snippets,'no lookup-region assembly retained';save(o.out/'release-codegen.json',{'functions':snippets,'missing_symbols':[s for s in ['_zbtScoreLeafFindMember','_zbtreeScoreRaw','_zbtreeScore'] if s not in snippets],'scope':'Actual release instructions; absent/inlined symbols remain absent, no cost claim'})
    files=dict(o.manifest['files_sha256']);files[str(o.out/'release-codegen.json')]=sha(o.out/'release-codegen.json')
    for path in binaries.values():files[str(path)]=sha(path)
    for paths in metadata.values():
        for path in paths.values():files[path]=sha(path)
    for record in o.records:
        for meta in record['raw'].values():files[meta['path']]=meta['sha256']
    for path in o.out.glob('*.json'):
        if path.name!='status.json':files[str(path)]=sha(path)
    files[str(o.out/'commands.jsonl')]=sha(o.out/'commands.jsonl')
    result={'status':'COMPLETE','files_sha256':files,'input_manifest_path':str(o.manifest_path),'input_manifest_sha256':sha(o.manifest_path),'binaries':{k:str(v) for k,v in binaries.items()},'metadata':metadata,'compiler':compiler_text,'compiler_launcher_sha256':sha('/usr/bin/clang'),'native_flags':NATIVE,'sanitizer_flags':SAN,'environment':ENV,'validation':{'original43_invocations':2,'physical_oracle_invocations':2,'lookup_semantic_smokes':36,'invalid_cli_checks':8},'source_adoption':'NONE'}
    save(o.out/'build-manifest.json',result);o.bound();o.state.update(status='COMPLETE',validation=result['validation'])

def calibrate(o):
    build_manifest=o.manifest;assert build_manifest['status']=='COMPLETE';binary=build_manifest['binaries']['native'];rows=[];fixed={}
    for n in o.plan['primary_sizes']:
        for replicate in range(3):
            paths=run(o,lookup_cmd(binary,n,200000,1),'n'+str(n)+'-rep'+str(replicate));row=parse_csv(paths,n,200000,1);row.update(size=n,replicate=replicate,seed=1);rows.append(row);save(o.out/'observations.json',rows)
        rs=[r for r in rows if r['size']==n];assert all(r['fingerprint']==rs[0]['fingerprint'] for r in rs)
        fastest=min(r['elapsed_ns'] for r in rs);desired=(600000000*200000+fastest-1)//fastest;ops=min(100000000,desired)
        fixed[str(n)]={'operations':ops,'uncapped_operations':desired,'capped':desired>100000000,'fastest_elapsed_ns_at_200000':fastest,'estimator':'ceil(600000000*200000/minelapsed_ns); fastest exact elapsed for equal200Kqueries'}
    schedule=[]
    for block,seed in enumerate([1,2,3,1,2,3]):
        for n in ([100000,1000000] if block%2==0 else [1000000,100000]):
            for position,side in enumerate('ABBA'):schedule.append({'index':len(schedule),'block':block,'seed':seed,'size':n,'case':'lookup-hit','member_bytes':16,'warmup_passes':1,'position':position,'side':side,'operations':fixed[str(n)]['operations']})
    save(o.out/'counts.json',{'status':'COMPLETE','target_elapsed_ns':600000000,'calibration_operations':200000,'replicates':3,'fixture_seed':1,'fixed':fixed,'observations':rows,'build_manifest_sha256':sha(o.manifest_path)});save(o.out/'aa-schedule.json',schedule)
    o.state.update(status='COMPLETE',calibration_children=len(rows),fixed=fixed)

def control_checksum():
    # Independent affine-map exponentiation for x <-1664525*x+1013904223 modulo2^64.
    a,c=1664525,1013904223;out_a,out_c=1,0;n=200000000
    while n:
        if n&1:out_a,out_c=(a*out_a)&MASK,(a*out_c+c)&MASK
        a,c=(a*a)&MASK,(a*c+c)&MASK;n>>=1
    value=(out_a+out_c)&MASK;assert value==1128443088728658433;return value

def profile(o):
    m=o.manifest;assert m['status']=='COMPLETE';results=[]
    for index in range(2):
        paths=run(o,[m['binaries']['sampler']],'sampler-'+str(index),extra_env={'PROFILE_USEC':'1000'});assert paths['stdout'].read_text()=='result,'+str(control_checksum())+'\n'
        result=profile_derive(o,paths,m['binaries']['sampler'],m['metadata']['sampler'],'sampler-'+str(index),'sampler_probe')
        assert result['sample_count']>=25  # Mapper requires every PC inside actual contiguous probe extent, independently of dladdr aliases.
        results.append(result);save(o.out/'summary.json',results)
    for n in [100000,1000000]:
        paths=run(o,lookup_cmd(m['binaries']['profile'],n,10000000,1),'hit-n'+str(n),extra_env={'PROFILE_USEC':'1000'});csvrow=parse_csv(paths,n,10000000,1,profile=True)
        result=profile_derive(o,paths,m['binaries']['profile'],m['metadata']['profile'],'hit-n'+str(n),'lookup-hit');result['csv']=csvrow;results.append(result);save(o.out/'summary.json',results)
    assert all(r['sample_count']>=25 for r in results)
    o.state.update(status='COMPLETE',sampler_controls=2,lookup_captures=2,all_sufficient=True,profile_timing_fields_used=False)

def profile_derive(o,paths,binary,metadata,name,scope):
    lines=paths['stderr'].read_text().splitlines();headers=[x.split(',') for x in lines if x.startswith('PROFILE,')];pc=[x for x in lines if x.startswith('PC,')]
    assert len(headers)==1;h=headers[0];assert len(h)==5 and h[1]==scope and h[2]=='1000' and h[4]=='0' and int(h[3])==len(pc) and len(pc)<=65536 and len(lines)==len(pc)+1
    output=o.out/(name+'-map.json')
    cmd=['python3',str(REL/'profile-map.py'),'--stdout',str(paths['stdout']),'--stderr',str(paths['stderr']),'--binary',binary,'--nm',metadata['nm'],'--assembly',metadata['assembly'],'--output',str(output)]
    run(o,cmd,name+'-offline-map',max_seconds=30);assert output.is_file();mapped=load(output)
    assert mapped['status']=='PASS' and mapped['sample_count']==len(pc) and mapped['all_observations_conserved'] is True and mapped['binary_sha256']==sha(binary)
    assert mapped['stdout_sha256']==sha(paths['stdout']) and mapped['stderr_sha256']==sha(paths['stderr']) and mapped['nm_sha256']==sha(metadata['nm'])
    if scope=='sampler_probe':assert mapped['probe_symbol_samples']==len(pc) and mapped['control_result']==str(control_checksum())
    return {'name':name,'scope':scope,'sample_count':len(pc),'uncapped':True,'minimum_samples':25,'sufficient':len(pc)>=25,'binary_sha256':sha(binary),'map_path':str(output),'map_sha256':sha(output),'mapper_status':mapped.get('status'),'timing_fields_used':False,'raw':{k:{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for k,p in paths.items()}}

def aa(o):
    # Root timing manifest wraps exact prior build manifest and derived calibration artifacts.
    m=o.manifest
    for key in ['build_manifest_path','counts_path','schedule_path','profile_status_path','build_status_path','calibration_status_path']:assert m[key] in m['files_sha256'],'unfrozen AA prerequisite: '+key
    for key in ['build_status_path','calibration_status_path','profile_status_path']:
        prior=load(m[key]);assert prior['status']=='COMPLETE' and prior['release_safe'] is True,'incomplete prerequisite: '+key
    bm=load(m['build_manifest_path']);counts=load(m['counts_path']);schedule=load(m['schedule_path']);profile_state=load(m['profile_status_path'])
    assert bm['status']=='COMPLETE' and counts['status']=='COMPLETE' and counts['build_manifest_sha256']==sha(m['build_manifest_path'])
    assert profile_state['status']=='COMPLETE' and profile_state['all_sufficient'] is True and profile_state['lookup_captures']==2 and profile_state['sampler_controls']==2
    assert all(m['files_sha256'].get(p)==h for p,h in bm['files_sha256'].items()),'timing freeze must retain complete build identity table'
    expected=[]
    for block,seed in enumerate([1,2,3,1,2,3]):
        for n in ([100000,1000000] if block%2==0 else [1000000,100000]):
            for pos,side in enumerate('ABBA'):expected.append({'index':len(expected),'block':block,'seed':seed,'size':n,'case':'lookup-hit','member_bytes':16,'warmup_passes':1,'position':pos,'side':side,'operations':counts['fixed'][str(n)]['operations']})
    assert schedule==expected and len(schedule)==48
    for n in [100000,1000000]:
        for seed in [1,2,3]:model(n,seed)
    rows=[];blocks=[]
    for item in schedule:
        n,ops,seed=item['size'],item['operations'],item['seed'];paths=run(o,lookup_cmd(bm['binaries']['native'],n,ops,seed),f"{item['index']:03d}");row=parse_csv(paths,n,ops,seed);row.update(item);rows.append(row)
        if len(rows)%4==0:
            q=rows[-4:];assert all(r['fingerprint']==q[0]['fingerprint'] for r in q),'AA fixture/output/memory mismatch'
            A=q[0]['elapsed_ns']+q[3]['elapsed_ns'];Bsum=q[1]['elapsed_ns']+q[2]['elapsed_ns'];minimum=min(r['elapsed_ns'] for r in q)
            blocks.append({'block':item['block'],'size':n,'seed':seed,'baseline_elapsed_sum':A,'paired_elapsed_sum':Bsum,'effect_percent_display_only':100*(Bsum-A)/A,'minimum_elapsed_ns':minimum,'qualified':abs(Bsum-A)*100<=A and minimum>=10000000})
        save(o.out/'summary.json',{'rows':rows,'blocks':blocks});o.bound()
    assert len(rows)==48 and len(blocks)==12
    qualified=all(b['qualified'] for b in blocks);o.state.update(status='COMPLETE',qualified=qualified,decision='PREREQUISITES_AA_PASS; fresh profile and root review still mandatory' if qualified else 'PARK; no proposals/source/candidate timing',completed_processes=48)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('phase',choices=['build','calibrate','profile','aa']);parser.add_argument('--ack',required=True);parser.add_argument('--manifest');a=parser.parse_args()
    default=E/('input-manifest.json' if a.phase=='build' else 'timing-manifest.json' if a.phase=='aa' else 'bench-results/build/build-manifest.json');mp=Path(a.manifest) if a.manifest else default
    assert not mp.is_absolute() and '..' not in mp.parts;ack=load(a.ack);plan=load(E/'PLAN.json');m=load(mp);check_plan(plan)
    assert ack['status']=='authorized' and ack['phase']==a.phase and ack['exclusive_runner'] is True and ack['all_other_work_idle'] is True
    for field,path in [('manifest_sha256',mp),('driver_sha256',E/'driver.py'),('plan_sha256',E/'PLAN.json')]:assert ack[field]==sha(path)
    assert re.fullmatch(r'[0-9a-f]{40}',ack['published_commit']);reviews={r['reviewer'] for r in ack['reviews'] if r['status']=='PASS'};assert '/root' in reviews and '/root/followup_proposal_c' in reviews
    verify(m['files_sha256']);assert str(REL/'driver.py') in m['files_sha256'] and str(REL/'PLAN.json') in m['files_sha256']
    prerequisites={}
    if a.phase in ['calibrate','profile']:
        status_path=mp.parent/'status.json';prior=load(status_path)
        assert prior['status']=='COMPLETE' and prior['release_safe'] is True,'build final status is not complete/safe'
        prerequisites[str(status_path)]=sha(status_path)
    for sig in SIGS:signal.signal(sig,cancel)
    o=Owner(a.phase,ack,m,mp,plan);o.prerequisite_hashes=prerequisites;o.state['prerequisite_final_status_sha256']=prerequisites;o.persist();signal.setitimer(signal.ITIMER_REAL,max(.001,o.remaining()-10));error=None
    try:
        {'build':build,'calibrate':calibrate,'profile':profile,'aa':aa}[a.phase](o)
    except BaseException as ex:error=ex;o.state.update(status='INCOMPLETE; preserve evidence; no retry',exception_type=type(ex).__name__);raise
    finally:o.finish(error)
if __name__=='__main__':main()
