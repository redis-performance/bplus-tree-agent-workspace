from pathlib import Path
import subprocess,json,hashlib,datetime,time
root=Path.cwd();p=Path(__file__).parent.resolve();dest=root/'scratch/intel-corrected-adapter';start=time.monotonic();events=[]
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def run(cmd,tag,cwd=root):
 left=1800-(time.monotonic()-start);assert left>0
 begin=datetime.datetime.now(datetime.timezone.utc).isoformat();r=subprocess.run(cmd,cwd=cwd,capture_output=True,text=True,timeout=left)
 (p/(tag+'.stdout')).write_text(r.stdout);(p/(tag+'.stderr')).write_text(r.stderr);events.append(dict(tag=tag,command=cmd,started_utc=begin,finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),returncode=r.returncode));(p/'processes.json').write_text(json.dumps(events,indent=2)+'\n');r.check_returncode();return r.stdout.strip()
commit='13e459ff8800be3f02b6b45c87dd7b0c39453fa9';assert not dest.exists();freeze=json.loads((p/'source-freeze.json').read_text());utility=p.parent/'008-original-guards/post-phase-hashes.py';oldfreeze=p.parent/'007-scan-replication/candidate-freeze.json'
def oldcheck(tag):run(['python3',str(utility),'--freeze',str(oldfreeze),'--sources','scratch/intel-scan-replication','--out',str(p/(tag+'.json'))],tag)
oldcheck('original-before-hashes')
run(['git','fetch','origin',commit],'fetch-source');run(['git','worktree','add','--detach',str(dest),commit],'isolated-worktree');assert run(['git','rev-parse','HEAD'],'source-head',dest)==commit
observed={f:sha(dest/f) for f in freeze['files']};assert observed==freeze['files'];(p/'source-before.json').write_text(json.dumps(dict(commit=commit,files=observed),indent=2)+'\n')
run(['python3','scripts/run-size-matrix.py','--out',str(p/'results'),'--build','build/corrected-adapter-intel','--ops','1000000','--member-bytes','16','--budget-seconds','1200'],'baseline',dest)
assert {f:sha(dest/f) for f in freeze['files']}==freeze['files'];after={f:sha(dest/f) for f in freeze['files']};after.update({f:sha(dest/f) for f in ['build/corrected-adapter-intel/btree-bench','build/corrected-adapter-intel/btree-test','build/corrected-adapter-intel/sanitize/btree-bench','build/corrected-adapter-intel/sanitize/btree-test']});(p/'source-after.json').write_text(json.dumps(dict(commit=commit,files=after),indent=2)+'\n');oldcheck('original-after-hashes')
run(['python3','scripts/analyse-size-matrix.py',str(p/'results')],'analysis',dest);(p/'complete.json').write_text(json.dumps(dict(status='complete',elapsed_seconds=time.monotonic()-start),indent=2)+'\n');print('PASS corrected-adapter baseline and original artifacts unchanged')
