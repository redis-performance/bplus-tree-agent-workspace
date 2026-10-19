#!/usr/bin/env python3
"""Fresh corrected-adapter baseline profile. Preparation never executes profiler."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import argparse, csv, hashlib, io, json, os, re, signal, subprocess, time
ROOT=Path.cwd(); OUT=Path(__file__).resolve().parent; REL=OUT.relative_to(ROOT); BASE=OUT.parent
SCRATCH=Path('scratch/m6-corrected-iterator-profile')
PLAN=json.loads((OUT/'PLAN.json').read_text()); CONTRACTS=PLAN['contracts']
GLOBAL_STOP=datetime.fromisoformat(PLAN['budgets']['absolute_capture_stop_utc']).timestamp()
def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,data):
 p=Path(p);q=p.with_name(p.name+'.tmp');q.write_text(json.dumps(data,indent=2)+'\n');q.replace(p)
def generic(s):
 s=s.replace(str(ROOT),'<workspace>')
 return re.sub(r'/var/'+r'folders/[^\s]+/T/','<compiler-temporary-directory>/',s)
def execute(command, name, folder, timeout, env=None):
    """Bound and reap a process group; retain stdout/stderr even on timeout."""
    assert timeout > 0, "no remaining child budget"
    destination = OUT / folder
    destination.mkdir(exist_ok=True)
    raw_dir = SCRATCH / "raw-logs"
    raw_dir.mkdir(parents=True, exist_ok=True)
    public_paths = {c: destination / (name + "." + c) for c in ("stdout", "stderr")}
    raw_paths = {c: raw_dir / (name + "." + c) for c in ("stdout", "stderr")}
    assert not any(p.exists() for p in [*public_paths.values(), *raw_paths.values()]), ("no retry/overwrite", name)
    command = list(map(str, command))
    public_command = [generic(argument) for argument in command]
    executable_identity = None
    if Path(command[0]).is_absolute():
        executable_identity = dict(name=Path(command[0]).name, sha256=sha(command[0]))
        public_command[0] = executable_identity["name"]
    (raw_dir / (name + ".command.json")).write_text(json.dumps(dict(command=command, cwd=str(ROOT))) + "\n")
    record = dict(name=name, command=public_command, executable_identity=executable_identity,
                  cwd="workspace-root", started_utc=utc(),
                  timeout_seconds=timeout, timed_out=False, returncode=None,
                  environment_override={"PROFILE_USEC": env["PROFILE_USEC"]} if env is not None and "PROFILE_USEC" in env else {})
    start = time.monotonic()
    process = None
    stdout, stderr = "", ""

    def terminate_and_collect():
        if process.poll() is None:
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                # The child can finish between poll() and killpg().
                pass
        return process.communicate()

    try:
        process = subprocess.Popen(command, cwd=ROOT, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, text=True, start_new_session=True, env=env)
        try:
            stdout, stderr = process.communicate(timeout=timeout)
        except subprocess.TimeoutExpired:
            record["timed_out"] = True
            stdout, stderr = terminate_and_collect()
        record["returncode"] = process.returncode
    except OSError as error:
        record["spawn_error"] = generic(repr(error))
        if process is not None and process.poll() is None:
            stdout, stderr = terminate_and_collect()
            record["returncode"] = process.returncode
    except BaseException as error:
        record["interrupted"] = generic(repr(error))
        if process is not None:
            stdout, stderr = terminate_and_collect()
            record["returncode"] = process.returncode
    finally:
        # communicate() has reaped the child on both normal and timeout paths.
        record.update(finished_utc=utc(), wall_seconds=time.monotonic() - start,
                      process_reaped=process is None or process.poll() is not None)
        record["logs"] = {}
        for channel, data in (("stdout", stdout), ("stderr", stderr)):
            raw_paths[channel].write_text(data)
            public_data = generic(data)
            if folder == "profiles" and channel == "stderr":
                pc_count = sum(line.startswith("PC,") for line in public_data.splitlines())
                public_data = "\n".join(line for line in public_data.splitlines() if not line.startswith("PC,")) + "\n"
                public_data += "RAW_PC_ROWS_RETAINED_PRIVATELY,%d\n" % pc_count
            public_paths[channel].write_text(public_data)
            record["logs"][channel] = dict(file=str(public_paths[channel].relative_to(OUT)),
                                            sha256=sha(public_paths[channel]),
                                            original_raw_sha256=sha(raw_paths[channel]),
                                            original_raw="ignored " + str(raw_paths[channel]))
        with (OUT / "commands.jsonl").open("a") as journal:
            journal.write(json.dumps(record) + "\n")
    if (record["timed_out"] or record["returncode"] != 0 or "interrupted" in record
            or not record["process_reaped"]):
        raise RuntimeError(json.dumps(dict(child=name, timed_out=record["timed_out"],
                                           returncode=record["returncode"],
                                           evidence="commands.jsonl + retained stdout/stderr")))
    return stdout, stderr, record


def args(binary,n,ops,seed,c,warmup):
 return [str(binary),'--size',str(n),'--ops',str(ops),'--seed',str(seed),'--member-bytes','16','--warmup-passes',str(warmup),'--direction',c['direction'],'--mask',str(c['mask']),'--encoding',c['encoding']]
def parse_row(out,n,ops,seed,c,warmup):
 rows=list(csv.DictReader(io.StringIO(out)));assert len(rows)==1
 row=rows[0];count=((ops+n-1)//n)*n
 assert row['case']=='iterator-modes' and int(row['size'])==n and int(row['seed'])==seed
 assert int(row['requested_ops'])==ops and int(row['operations'])==count and int(row['traversals'])==count//n
 assert int(row['member_bytes'])==16 and int(row['warmup_passes'])==warmup
 assert int(row['mask'])==c['mask'] and row['direction']==c['direction'] and row['encoding']==c['encoding']
 assert row['checksum']==row['expected_checksum'] and int(row['tree_bytes'])>0
 return row

def prepare():
 assert not (OUT/'freeze.json').exists(),'already frozen; no preparation rerun'
 SCRATCH.mkdir(parents=True,exist_ok=True)
 for name in ('iterator.c','microbench.c','apple-sampler-bridge.c'):
  assert (OUT/name).read_bytes()==(BASE/'009-iterator-profile'/name).read_bytes()
 assert sha('src/zset_btree.c')==PLAN['source_sha256'] and sha('src/zset_btree.h')==PLAN['header_sha256']
 for path,h in PLAN['adapter_hashes'].items():assert sha(path)==h,path
 # Prior43-test evidence has exact current target/adapter/hash/test input identity.
 evidence=json.loads((BASE/'012-contract-diagnostic/reused-tests.json').read_text())['new']
 for path,h in evidence['source_identity'].items():assert sha(path)==h,path
 for path,h in evidence['native_sanitizer_evidence'].items():assert sha(BASE/path)==h,path
 save(OUT/'reused-tests.json',evidence)
 checks=[]
 for label,sanitized,profile in [('iterator-native',False,False),('iterator-san',True,False),('iterator-profile',False,True)]:
  flags=PLAN['flags'].copy()
  if sanitized:
   flags[flags.index('-O3')]='-O1';flags+=['-fsanitize=address,undefined','-fno-sanitize-recover=all']
  if profile:flags+=PLAN['profile_extra_flags']
  execute(['clang',*flags,'-Isrc','-Icompat','-Ivendor/redis',REL/'iterator.c',*([REL/'apple-sampler-bridge.c'] if profile else []),'src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',SCRATCH/label],'build-'+label,'validation',120)
 for label in ('iterator-native','iterator-san'):
  for c in CONTRACTS:
   out,err,record=execute(args(SCRATCH/label,1000,2003,1,c,1),label+'-'+c['id'],'validation',120)
   row=parse_row(out,1000,2003,1,c,1)
   checks.append(dict(build=label,contract=c['id'],operations=int(row['operations']),checksum=row['checksum'],tree_bytes=int(row['tree_bytes']),status='PASS',logs=record['logs']))
 save(OUT/'validation.json',dict(status='PASS',native_sanitizer_runs=8,checks=checks,profile_binary_executed=False,original43test_identity='reused-tests.json'))
 prior=[]
 for i in (0,1):
  p=BASE/'002-rank/profile'/('sampler-calibration-'+str(i)+'.stderr');pc=[x for x in p.read_text().splitlines() if x.startswith('PC,')]
  assert pc and all('sampler_probe' in x for x in pc)
  prior.append(dict(file=str(p.relative_to(ROOT)),sha256=sha(p),captured_pcs=len(pc),all_pcs_at_known_sampler_probe=True,note='Historical known-work control reused; unchanged sampler text, not a new corrected-adapter calibration.'))
 out,_,_=execute(['otool','-tvV',SCRATCH/'iterator-profile'],'release-assembly','validation',120)
 selected=[];active=False
 for line in out.splitlines():
  if line.startswith('_') and line.endswith(':'):active=line=='_zbtreeIteratorNext:'
  if active:selected.append(line)
 assert selected;(OUT/'zbtreeIteratorNext.asm').write_text('\n'.join(selected)+'\n')
 execute(['nm','-nm',SCRATCH/'iterator-profile'],'release-nm','validation',120)
 compiler=execute(['clang','--version'],'compiler','validation',120)[0]
 planned=[]
 for cell in PLAN['captures']:
  c=next(x for x in CONTRACTS if x['id']==cell['contract']);name=f"n{cell['size']}-{c['id']}-s{cell['seed']}"
  planned.append(dict(name=name,command=args(SCRATCH/'iterator-profile',cell['size'],cell['requested_items'],cell['seed'],c,cell['warmup_passes']),environment={'PROFILE_USEC':'1000'},child_seconds_max=120))
 save(OUT/'planned-commands.json',dict(status='PLANNED ONLY; NO CAPTURE AUTHORIZATION',commands=planned,count=16))
 files=['src/zset_btree.c','src/zset_btree.h','compat/server.h','compat/standalone.c','vendor/redis/siphash.c','vendor/redis/sds.h','vendor/redis/testhelp.h','tests/upstream.c',str(BASE.relative_to(ROOT)/'002-rank/night-rank-sampler.h')]
 files += [str(REL/name) for name in ('iterator.c','microbench.c','apple-sampler-bridge.c','PLAN.json','run.py','README.md','planned-commands.json','validation.json','reused-tests.json')]
 save(OUT/'freeze.json',dict(status='PREPARED; CAPTURES NOT AUTHORIZED',frozen_utc=utc(),files_sha256={p:sha(p) for p in files},binaries_sha256={str(SCRATCH/name):sha(SCRATCH/name) for name in ('iterator-native','iterator-san','iterator-profile')},compiler='\n'.join(s for s in compiler.splitlines() if not s.startswith('InstalledDir:')),flags=PLAN['flags'],sampler_prior_controls=prior,no_optimization_selected=True,participant='/root/followup_proposal_a',backend=PLAN['backend']))
 save(OUT/'STATUS.json',dict(status='READY; awaiting root exclusive-runner ACK after plot/raw audit complete',profile_captures_started=False,native_sanitizer_checks=8,planned_captures=16,all_preparation_children_reaped=True))
 print('READY:3 binaries,8 semantic checks,16 planned captures; NO PROFILE CAPTURE',flush=True)

def verify_freeze():
 f=json.loads((OUT/'freeze.json').read_text())
 for path,h in {**f['files_sha256'],**f['binaries_sha256']}.items():assert sha(path)==h,path
 return f

def captures(ack_path):
 verify_freeze();ack=json.loads(Path(ack_path).read_text())
 assert ack['status']=='authorized' and ack['authorized_action']=='captures'
 assert ack['exclusive_runner'] is True and ack['other_work_idle'] is True
 for key,name in [('freeze_sha256','freeze.json'),('driver_sha256','run.py'),('plan_sha256','PLAN.json')]:assert ack[key]==sha(OUT/name),key
 assert not (OUT/'capture-status.json').exists() and not (OUT/'summary.json').exists(),'no capture retry/resume'
 assert time.time()<GLOBAL_STOP
 lock=SCRATCH/'CAPTURE.lock';fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600);os.write(fd,json.dumps(dict(pid=os.getpid(),started_utc=utc())).encode());os.close(fd)
 results=[];started=time.monotonic();state=dict(status='running',started_utc=utc(),planned=16,completed=0,ack_sha256=sha(ack_path),captures=[],elapsed_fields_unused=True)
 save(OUT/'capture-status.json',state)
 env=os.environ.copy();env['PROFILE_USEC']='1000'
 try:
  planned_document=json.loads((OUT/'planned-commands.json').read_text());planned=planned_document['commands']
  assert len(PLAN['captures'])==planned_document['count']==len(planned)==16, 'exact planned capture count'
  assert len({job['name'] for job in planned})==16, 'duplicate capture name'
  # Validate the complete schedule before launching any capture, including extras.
  for index,cell in enumerate(PLAN['captures']):
   c=next(x for x in CONTRACTS if x['id']==cell['contract']);job=planned[index]
   expected_name=f"n{cell['size']}-{c['id']}-s{cell['seed']}"
   expected_command=args(SCRATCH/'iterator-profile',cell['size'],cell['requested_items'],cell['seed'],c,cell['warmup_passes'])
   assert job['name']==expected_name and job['command']==expected_command, 'planned command mismatch'
   assert job['environment']=={'PROFILE_USEC':'1000'} and job['child_seconds_max']==PLAN['budgets']['child_seconds'], 'planned environment/timeout mismatch'
  for index,cell in enumerate(PLAN['captures']):
   job=planned[index]
   verify_freeze();remaining=min(PLAN['budgets']['capture_phase_wall_seconds']-(time.monotonic()-started),GLOBAL_STOP-time.time());assert remaining>0
   c=next(x for x in CONTRACTS if x['id']==cell['contract'])
   out,err,record=execute(job['command'],job['name'],'profiles',min(120,remaining),env=env)
   row=parse_row(out,cell['size'],cell['requested_items'],cell['seed'],c,cell['warmup_passes'])
   pcs=[line.split(',') for line in err.splitlines() if line.startswith('PC,')];headers=[line.split(',') for line in err.splitlines() if line.startswith('PROFILE,')]
   assert len(headers)==1;header=headers[0];assert int(header[2])==1000 and int(header[3])==len(pcs) and header[4]=='0'
   symbols=Counter();bins=Counter()
   for pc in pcs:
    assert len(pc)==6;module,address,base,symbol,symbol_start=pc[1:];start_addr=int(symbol_start,16);address=int(address,16)
    offset=address-start_addr if start_addr and address>=start_addr else None
    module=Path(module).name;symbols[symbol]+=1;bins[(module,symbol,offset)]+=1
   item=dict(size=cell['size'],seed=cell['seed'],contract=c['id'],mask=c['mask'],direction=c['direction'],encoding=c['encoding'],operations=int(row['operations']),checksum=row['checksum'],expected_checksum=row['expected_checksum'],tree_bytes=int(row['tree_bytes']),construction_fingerprint=row['construction_fingerprint'],samples=len(pcs),minimum_samples=25,sufficient=len(pcs)>=25,requested_interval_us=1000,symbols=dict(symbols),pc_bins=[dict(module=k[0],symbol=k[1],offset_bytes=k[2],count=v) for k,v in sorted(bins.items(),key=lambda p:(p[0][0],p[0][1],-1 if p[0][2] is None else p[0][2]))],raw=record['logs'],started_utc=record['started_utc'],finished_utc=record['finished_utc'],scope=PLAN['sampling_scope'],counts_not_costs=True,emitted_elapsed_fields_unused=True)
   save(OUT/'profiles'/(job['name']+'.json'),item);results.append(item);state.update(completed=len(results),captures=results);save(OUT/'capture-status.json',state)
   assert time.monotonic()-started<=PLAN['budgets']['capture_phase_wall_seconds'] and time.time()<=GLOBAL_STOP
   verify_freeze()
   print('CAPTURE',len(results),'/16',job['name'],'PCs',len(pcs),'sufficient',item['sufficient'],flush=True)
  assert len(results)==16;verify_freeze();assert time.monotonic()-started<=PLAN['budgets']['capture_phase_wall_seconds'] and time.time()<=GLOBAL_STOP
  state.update(status='complete',finished_utc=utc(),sufficient=sum(x['sufficient'] for x in results),total_captures=16,no_optimization_selected=True)
  save(OUT/'summary.json',state)
 except BaseException as error:
  state.update(status='incomplete',failure=generic(repr(error)),finished_utc=utc());raise
 finally:
  records=[json.loads(line) for line in (OUT/'commands.jsonl').read_text().splitlines()]
  state.update(all_children_reaped=all(x['process_reaped'] for x in records),wall_seconds=time.monotonic()-started);save(OUT/'capture-status.json',state);lock.unlink()
 print('CAPTURES COMPLETE; baseline only; no speed claim',flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('action',choices=['prepare','captures']);p.add_argument('--ack');a=p.parse_args()
 if a.action=='prepare':prepare()
 else:
  assert a.ack,'Root exclusive-runner ACK is required';captures(a.ack)
