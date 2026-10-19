from pathlib import Path
import csv,datetime,hashlib,json,subprocess,time
p=Path(__file__).parent;out=p/'aa.json';assert not out.exists();start=time.monotonic();base=Path('scratch/arm-corrected-scan/base');freeze=json.loads((p/'comparison-freeze.json').read_text())
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def check_hashes():
 for f,h in freeze['sha256'].items():assert hashlib.sha256((base/f).read_bytes()).hexdigest()==h
assert hashlib.sha256(Path(__file__).read_bytes()).hexdigest()==freeze['aa_driver_sha256']
(p/'raw').mkdir()
check_hashes();m=dict(status='running',started_utc=now(),rows=[],attempts=[])
def save():out.write_text(json.dumps(m,indent=2)+'\n')
save()
try:
 for block in range(6):
  for n in ([100000,1000000] if block%2==0 else [1000000,100000]):
   seed=701+block%3
   for position in range(4):
    remaining=300-(time.monotonic()-start);assert remaining>0
    cmd=[str(base/'build/btree-bench'),'--case','scan','--size',str(n),'--ops','5000000','--member-bytes','16','--seed',str(seed)]
    t=now();tag=f'aa-{len(m["rows"]):03d}';attempt=dict(size=n,seed=seed,block=block,position=position,command=cmd,started_utc=t)
    try:r=subprocess.run(cmd,capture_output=True,text=True,timeout=min(60,remaining))
    except subprocess.TimeoutExpired as e:
     decode=lambda v:v.decode(errors='replace') if isinstance(v,bytes) else v or ''
     (p/'raw'/(tag+'.stdout')).write_text(decode(e.stdout));(p/'raw'/(tag+'.stderr')).write_text(decode(e.stderr));attempt.update(finished_utc=now(),returncode=None,status='timeout');m['attempts'].append(attempt);save();raise
    (p/'raw'/(tag+'.stdout')).write_text(r.stdout);(p/'raw'/(tag+'.stderr')).write_text(r.stderr);attempt.update(finished_utc=now(),returncode=r.returncode,status='completed');m['attempts'].append(attempt);save();assert r.returncode==0,r.stderr
    rows=list(csv.DictReader(r.stdout.splitlines()));assert len(rows)==1;row=rows[0];assert row['cpu_start']==row['cpu_end']=='2'
    assert row['case']=='scan'and int(row['size'])==n and int(row['seed'])==seed and row['requested_ops']=='5000000'and row['member_bytes']=='16'
    m['rows'].append(dict(size=n,seed=seed,block=block,position=position,command=cmd,started_utc=t,finished_utc=attempt['finished_utc'],row=row));save()
 effects=[]
 for i in range(0,len(m['rows']),4):
  r=m['rows'][i:i+4];assert len({tuple(x['row'][k]for k in ['checksum','operations','tree_bytes','traversals','warmup_passes'])for x in r})==1
  v=[int(x['row']['elapsed_ns'])/int(x['row']['operations'])for x in r];effect=100*((v[1]+v[2])/(v[0]+v[3])-1);minimum=min(int(x['row']['elapsed_ns'])for x in r)
  effects.append(dict(size=r[0]['size'],seed=r[0]['seed'],block=r[0]['block'],percent=effect,min_window_ns=minimum,qualified=abs(effect)<=1 and minimum>=10000000))
 check_hashes();m.update(status='complete',effects=effects)
except BaseException as e:
 m.update(status='failed',error=str(e));raise
finally:
 m.update(finished_utc=now(),elapsed_seconds=time.monotonic()-start);save()
print('PASS48 serial rows; qualification:',{n:all(x['qualified']for x in effects if x['size']==n)for n in [100000,1000000]})
