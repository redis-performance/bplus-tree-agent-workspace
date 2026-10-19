#!/usr/bin/env python3
"""ACK-bound exact NEON replication. No build/calibration/retry/profile path."""
import argparse,csv,hashlib,io,json,math,os,re,signal,subprocess,time
from pathlib import Path
from datetime import datetime,timezone
R=Path.cwd(); E=Path(__file__).resolve().parent
SIGNALS={signal.SIGINT,signal.SIGTERM,signal.SIGHUP,signal.SIGALRM}
ENV={'PATH':'/usr/bin:/bin:/usr/sbin:/sbin','LC_ALL':'C','LANG':'C','TZ':'UTC'}
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def utc(): return datetime.now(timezone.utc).isoformat()
def save(p,x):
    tmp=Path(str(p)+'.tmp');tmp.write_text(json.dumps(x,indent=2)+'\n');tmp.replace(p)
def alive(pid):
    try: os.killpg(pid,0);return True
    except ProcessLookupError:return False
def cancel(sig,frame): raise TimeoutError('owned phase cancelled or deadline reached')
def verify(freeze):
    for path,digest in freeze['files_sha256'].items():
        assert not Path(path).is_absolute() and '..' not in Path(path).parts
        assert sha(R/path)==digest,'frozen identity mismatch'
def run(cmd,name,out,raw,seconds,deadline):
    paths={k:raw/(name+'.'+k) for k in ['stdout','stderr']}
    rec={'name':name,'command':cmd,'environment':ENV,'started_utc':utc(),'timeout_seconds':seconds,'timed_out':False,'child_reaped':False,'owned_group_empty':False,'release_safe':False}
    child=None;start=time.monotonic()
    try:
        with paths['stdout'].open('xb') as sout,paths['stderr'].open('xb') as serr:
            child=subprocess.Popen(cmd,stdout=sout,stderr=serr,env=ENV,start_new_session=True)
            while child.poll() is None:
                if time.monotonic()-start>=seconds or time.time()>=deadline-10:
                    rec['timed_out']=True;break
                time.sleep(.025)
    except BaseException as ex:
        rec['exception_type']=type(ex).__name__;raise
    finally:
        mask=signal.pthread_sigmask(signal.SIG_BLOCK,SIGNALS)
        try:
            if child is not None:
                if alive(child.pid):
                    try:os.killpg(child.pid,signal.SIGTERM);rec['term_sent']=True
                    except ProcessLookupError:rec['term_exit_race']=True
                    until=time.monotonic()+1
                    while alive(child.pid) and time.monotonic()<until:time.sleep(.025)
                if alive(child.pid):
                    try:os.killpg(child.pid,signal.SIGKILL);rec['kill_sent']=True
                    except ProcessLookupError:rec['kill_exit_race']=True
                try:child.wait(timeout=4);rec['child_reaped']=True
                except subprocess.TimeoutExpired:rec['child_reaped']=False
                until=time.monotonic()+3
                while alive(child.pid) and time.monotonic()<until:time.sleep(.025)
                rec['owned_group_empty']=not alive(child.pid);rec['returncode']=child.returncode
            rec.update(finished_utc=utc(),wall_seconds=time.monotonic()-start,raw={})
            for key,p in paths.items():
                if p.exists():rec['raw'][key]={'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size}
            rec['release_safe']=rec['child_reaped'] and rec['owned_group_empty']
            with (out/'commands.jsonl').open('a') as journal:
                journal.write(json.dumps(rec)+'\n');journal.flush();os.fsync(journal.fileno())
        finally:signal.pthread_sigmask(signal.SIG_SETMASK,mask)
    return rec,paths
FINGERPRINT=['case','size','seed','requested_ops','member_bytes','warmup_passes','operations','checksum','tree_bytes','traversals']
def parse(paths,item):
    assert paths['stderr'].stat().st_size==0,'nonempty stderr retained privately'
    rows=list(csv.DictReader(io.StringIO(paths['stdout'].read_text())))
    assert len(rows)==1 and None not in rows[0];r=rows[0]
    expected={'case':'scan','size':item['size'],'seed':item['seed'],'requested_ops':5000000,'member_bytes':16,'warmup_passes':1}
    for key,value in expected.items():assert r[key]==str(value),'CSV contract mismatch'
    # Preserve all numeric metadata; only the documented QoS strings may be text.
    safe={}
    for key,value in r.items():
        if key in ['case','qos_reported_start','qos_reported_end','qos_effective']:
            assert re.fullmatch(r'[A-Za-z0-9_-]{1,80}',value);safe[key]=value
        else:
            assert re.fullmatch(r'-?[0-9]+(?:\.[0-9]+)?',value);safe[key]=value
    ops=int(r['operations']);trav=int(r['traversals']);elapsed=int(r['elapsed_ns']);owned=int(r['tree_bytes']);checksum=int(r['checksum']);n=item['size']
    assert trav==(5000000+n-1)//n and ops>=trav*n and ops%trav==0
    assert checksum>=trav*n*(n-1)//2 and checksum%trav==0 and owned>0 and elapsed>0
    assert abs(float(r['ns_per_op'])-elapsed/ops)<=.000501
    assert abs(float(r['ops_per_sec'])-ops*1e9/elapsed)<=.000501
    assert all(math.isfinite(float(r[k])) for k in ['ns_per_op','ops_per_sec'])
    return dict(**item,csv=safe,elapsed_ns=elapsed,operations=ops,tree_bytes=owned,checksum=str(checksum),ns_per_op_exact=elapsed/ops,window_qualified=elapsed>=10000000,fingerprint={k:r[k] for k in FINGERPRINT})
def derive(rows):
    assert len(rows)%4==0
    blocks=[]
    for i in range(0,len(rows),4):
        q=rows[i:i+4];first=q[0]
        assert [x['position'] for x in q]==[0,1,2,3] and [x['side'] for x in q]==['A','B','B','A']
        assert all(x['fingerprint']==first['fingerprint'] for x in q),'fixture/output/memory mismatch within ABBA'
        assert all((x['block'],x['size'],x['variant'])==(first['block'],first['size'],first['variant']) for x in q)
        baseline_elapsed_sum=q[0]['elapsed_ns']+q[3]['elapsed_ns'];candidate_elapsed_sum=q[1]['elapsed_ns']+q[2]['elapsed_ns']
        effect=100*(candidate_elapsed_sum-baseline_elapsed_sum)/baseline_elapsed_sum
        blocks.append(dict(block=first['block'],size=first['size'],seed=first['seed'],variant=first['variant'],effect_percent=effect,all_windows_qualified=all(x['window_qualified'] for x in q),baseline_elapsed_sum=baseline_elapsed_sum,candidate_elapsed_sum=candidate_elapsed_sum,aa_qualified=abs(candidate_elapsed_sum-baseline_elapsed_sum)*100<=baseline_elapsed_sum and all(x['window_qualified'] for x in q),primary_speed_gate=candidate_elapsed_sum*100<=baseline_elapsed_sum*98 and all(x['window_qualified'] for x in q)))
    return blocks

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--phase',choices=['aa','discovery'],required=True);ap.add_argument('--ack',required=True);a=ap.parse_args()
    ack=json.loads(Path(a.ack).read_text());freeze=json.loads((E/'freeze.json').read_text());plan=json.loads((E/'PLAN.json').read_text())
    assert ack['status']=='authorized' and ack['phase']==a.phase and ack['exclusive_runner'] is True and ack['all_other_work_idle'] is True and ack['validation_status']=='PASS'
    for field,file in [('freeze_sha256','freeze.json'),('driver_sha256','timing.py'),('plan_sha256','PLAN.json'),('schedule_sha256',a.phase+'-schedule.json')]:assert ack[field]==sha(E/file)
    assert re.fullmatch('[0-9a-f]{40}',ack['published_commit'])
    assert any(x['reviewer']=='/root' and x['status']=='PASS' for x in ack['reviews'])
    assert any(x['reviewer'] not in ['/root','/root/followup_proposal_b'] and x['status']=='PASS' for x in ack['reviews'])
    verify(freeze)
    manifest=json.loads((E/'source-manifest.json').read_text());binaries={k:str(Path(v['worktree'])/'build/native/btree-bench') for k,v in manifest['variants'].items()}
    assert set(binaries)=={'base','A','B','C'} and all(p in freeze['files_sha256'] for p in binaries.values())
    schedule=json.loads((E/(a.phase+'-schedule.json')).read_text());assert len(schedule)==(48 if a.phase=='aa' else 144)
    expected=[]
    for block in range(6):
        variants=['base'] if a.phase=='aa' else ['A','B','C'][block%3:]+['A','B','C'][:block%3]
        for variant in variants:
            for size in ([100000,1000000] if block%2==0 else [1000000,100000]):
                for pos,side in enumerate(['A','B','B','A']):expected.append(dict(index=len(expected),block=block,variant=variant,size=size,seed=401+block%3,position=pos,side=side,binary='base' if side=='A' or a.phase=='aa' else variant,case='scan',requested_ops=5000000,member_bytes=16,warmup_passes=1))
    assert schedule==expected
    aa_refs={}
    if a.phase=='discovery':
        assert ack['aa_status_sha256']==sha(E/'aa/status.json') and ack['aa_summary_sha256']==sha(E/'aa/summary.json')
        status=json.loads((E/'aa/status.json').read_text());aa=json.loads((E/'aa/summary.json').read_text())
        assert status['status']=='COMPLETE' and status['qualified'] is True and status['completed_processes']==48 and status['release_safe'] is True and status['freeze_sha256']==sha(E/'freeze.json')
        assert len(aa['rows'])==48 and len(aa['blocks'])==12 and all(x['aa_qualified'] for x in derive(aa['rows']))
        for row in aa['rows']:
            key=(row['size'],row['seed']);assert key not in aa_refs or aa_refs[key]==row['fingerprint'];aa_refs[key]=row['fingerprint']
    cutoff=min(datetime.fromisoformat(plan['experimental_cutoff_utc']).timestamp(),datetime.fromisoformat(ack['absolute_stop_utc']).timestamp())
    assert cutoff<=datetime(2026,10,19,7,15,tzinfo=timezone.utc).timestamp() and time.time()+20<cutoff
    out=E/a.phase;raw=R/'scratch/m6-neon-replication/timing'/a.phase
    assert not out.exists() and not raw.exists(),'no retry/overwrite'
    out.mkdir();raw.mkdir(parents=True)
    for sig in SIGNALS:signal.signal(sig,cancel)
    start=time.monotonic();deadline=min(time.time()+300,cutoff);rows=[];blocks=[]
    state=dict(status='RUNNING',phase=a.phase,started_utc=utc(),planned_processes=len(schedule),completed_processes=0,release_safe=True,qualified=False,freeze_sha256=sha(E/'freeze.json'),published_commit=ack['published_commit'],placement='native macOS unpinned; CPU endpoints retained, residency/frequency unknown',source_adoption='NONE')
    save(out/'status.json',state);signal.setitimer(signal.ITIMER_REAL,max(.001,deadline-time.time()-10))
    try:
        for item in schedule:
            remaining=min(deadline-time.time(),300-(time.monotonic()-start));assert remaining>10,'phase/global budget exhausted'
            cmd=[binaries[item['binary']],'--case','scan','--size',str(item['size']),'--ops','5000000','--member-bytes','16','--seed',str(item['seed']),'--warmup-passes','1']
            state['release_safe']=False;save(out/'status.json',state)
            rec,paths=run(cmd,f"{item['index']:03d}",out,raw,min(60,remaining-10),deadline)
            state['release_safe']=rec['release_safe'];assert rec.get('returncode')==0 and not rec['timed_out'] and rec['release_safe'],'child failed; raw output retained'
            assert time.time()<deadline and time.monotonic()-start<300
            row=parse(paths,item)
            if a.phase=='discovery':assert row['fingerprint']==aa_refs[(row['size'],row['seed'])],'fixture differs from fresh AA'
            rows.append(row);state['completed_processes']=len(rows)
            if len(rows)%4==0:blocks=derive(rows)
            save(out/'summary.json',{'rows':rows,'blocks':blocks})
            assert time.time()<deadline and time.monotonic()-start<300,'derive/serialization over budget'
        verify(freeze)
        assert time.time()<deadline and time.monotonic()-start<300,'post-identity audit over budget'
        state['post_identities_verified']=len(freeze['files_sha256'])
        if len(rows)==len(schedule):
            state['status']='COMPLETE'
            if a.phase=='aa':state['qualified']=len(blocks)==12 and all(x['aa_qualified'] for x in blocks)
            else:
                survivors=[v for v in ['B','C','A'] if all(x['primary_speed_gate'] for x in blocks if x['variant']==v) and len([x for x in blocks if x['variant']==v])==12]
                state['primary_survivors']=survivors;state['selected_for_further_gates']=survivors[0] if survivors else 'NONE';state['qualified']=False
        save(out/'summary.json',{'rows':rows,'blocks':blocks});assert time.time()<deadline and time.monotonic()-start<300
    except BaseException as ex:
        state.update(status='INCOMPLETE; preserve all evidence; no retry',exception_type=type(ex).__name__);raise
    finally:
        mask=signal.pthread_sigmask(signal.SIG_BLOCK,SIGNALS)
        try:
            signal.setitimer(signal.ITIMER_REAL,0)
            # A pending cancellation may have arrived after run journaled cleanup.
            journal=out/'commands.jsonl'
            if journal.exists():
                records=[json.loads(x) for x in journal.read_text().splitlines()];state['release_safe']=all(x['release_safe'] for x in records);state['journaled_process_attempts']=len(records)
            state.update(finished_utc=utc(),phase_wall_seconds=time.monotonic()-start,completed_processes=len(rows))
            if time.time()>=deadline or time.monotonic()-start>=300:state.update(status='INCOMPLETE; deadline reached',qualified=False)
            save(out/'status.json',state)
            if time.time()>=deadline or time.monotonic()-start>=300:
                state.update(status='INCOMPLETE; final serialization crossed deadline',qualified=False);save(out/'status.json',state)
        finally:signal.pthread_sigmask(signal.SIG_SETMASK,mask)
if __name__=='__main__':main()
