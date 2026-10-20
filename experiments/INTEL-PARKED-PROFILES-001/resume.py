"""Launcher correction only; verify and reuse completed original preparation."""
import hashlib,json,os,shutil,subprocess,time
from pathlib import Path
OLD=Path('attempt1-results');OUT=Path('results');OUT.mkdir(exist_ok=True)
summary=json.loads((OLD/'summary.json').read_text())
assert len(summary)==36 and all(r['captures']==[] and r['workload_returncode']==1 for r in summary)
hashes=json.loads((OLD/'build-sha256.json').read_text())
for path,digest in hashes.items():assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==digest,path
commands=json.loads((OLD/'validation-commands.json').read_text());assert all(r['returncode']==0 for r in commands)
names={'validation-commands.json','completed-checks.json','build-sha256.json','environment.json'}
for r in commands:
 for suffix in ['.stdout','.stderr']:names.add(r['tag']+suffix)
for name in names:shutil.copy2(OLD/name,OUT/name)
probe=['numactl','--all','--physcpubind=2','--membind=0','python3','-c','import os; assert os.sched_getaffinity(0)=={2}; print(sorted(os.sched_getaffinity(0)))']
r=subprocess.run(probe,capture_output=True,text=True);assert r.returncode==0,(r.stdout,r.stderr)
meta={'time':time.time(),'preparation_origin':'attempt1-results; exact raw copies, no rerun','unchanged_hashes_verified':len(hashes),'launcher_probe':{'args':probe,'returncode':r.returncode,'stdout':r.stdout,'stderr':r.stderr},'controller_affinity':sorted(os.sched_getaffinity(0)),'frequency_path_readable':Path('/sys/devices/system/cpu/cpu2/cpufreq/scaling_cur_freq').read_text().strip()}
(OUT/'resume-provenance.json').write_text(json.dumps(meta,indent=2)+'\n')
subprocess.run(['python3','collect-v2.py'],check=True,env=dict(os.environ,PYTHONPATH='glue:pmu'))
