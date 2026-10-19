import csv,datetime,json,os,subprocess,time,re
from pathlib import Path
p=Path(__file__).parent;start=time.monotonic();records=json.loads((p/'processes.json').read_text())
def run(tag,binary,n,ops,seed=1):
 assert time.monotonic()-start<300
 env=os.environ.copy();env['SAMPLE_OUT']=str(p/'profiles'/(tag+'.hist.csv'))
 cmd=[str(p/'build'/binary),'--case','scan','--size',str(n),'--ops',str(ops),'--member-bytes','16','--seed',str(seed)]
 t=datetime.datetime.now(datetime.timezone.utc).isoformat();r=subprocess.run(cmd,capture_output=True,text=True,env=env,timeout=60)
 (p/'profiles'/(tag+'.stdout')).write_text(r.stdout);(p/'profiles'/(tag+'.stderr')).write_text(r.stderr);assert r.returncode==0,r.stderr
 rows=list(csv.DictReader(r.stdout.splitlines()));assert len(rows)==1 and rows[0]['cpu_start']==rows[0]['cpu_end']=='2'
 records.append(dict(tag=tag,command=cmd,started_utc=t,finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),row=rows[0]));(p/'processes.json').write_text(json.dumps(records,indent=2)+'\n');return rows[0]
# Repeat sampler controls before any scoped scan captures.
known={mode:{int(r['offset']):int(r['count']) for r in csv.DictReader((p/'profiles'/('known-'+mode+'.hist.csv')).open())} for mode in ['enabled','disabled']}
assert sum(known['disabled'].values())==0
assert (p/'profiles/known-enabled.stdout').read_text()==(p/'profiles/known-disabled.stdout').read_text()
functions=[line.split() for line in (p/'known-enabled-symbols.txt').read_text().splitlines()]
work=[cols for cols in functions if cols[-1]=='known_work'];assert len(work)==1
address,size=int(work[0][0],16),int(work[0][1],16)
base=[int(cols[0],16) for cols in functions if cols[-1]=='__executable_start'][0]
total=sum(known['enabled'].values());inside=sum(count for offset,count in known['enabled'].items() if address<=base+offset<address+size)
assert total>=20 and inside/total>=0.9
(p/'control-check.json').write_text(json.dumps(dict(enabled_samples=total,known_work_samples=inside,disabled_samples=0,checksum_equal=True),indent=2)+'\n')
fields=['case','size','requested_ops','member_bytes','seed','operations','tree_bytes','checksum','traversals','warmup_passes']
a=run('original-sanitize-control','original-sanitize',1000,1000);b=list(csv.DictReader((p/'profiles/sanitize-control.stdout').open()))[0];assert all(a[k]==b[k] for k in fields)
for tag in ['disabled-100','disabled-1000','disabled-10000','sanitize-control']:
 assert sum(int(r['count']) for r in csv.DictReader((p/'profiles'/(tag+'.hist.csv')).open()))==0
for seed in [1,2,3]:
 for n in [100000,1000000]:run(f'scan-{n}-seed{seed}','profile',n,5000000,seed)
# Exact linker-relative mapping of all sampled buckets, preserving inline frames.
syms=subprocess.check_output(['nm','-n','-S',str(p/'build/profile')],text=True);(p/'profile-symbols.txt').write_text(syms)
base=None
for line in syms.splitlines():
 cols=line.split()
 if cols and cols[-1]=='__executable_start':base=int(cols[0],16)
assert base is not None
buckets=set()
for f in (p/'profiles').glob('scan-*.hist.csv'):buckets.update(int(r['offset']) for r in csv.DictReader(f.open()))
cmd=['addr2line','-a','-f','-i','-C','-e',str(p/'build/profile')]+[hex(base+x) for x in sorted(buckets)]
mapped=subprocess.check_output(cmd,text=True);(p/'inline-map.txt').write_text(mapped);(p/'mapping-command.json').write_text(json.dumps(dict(command=cmd,linker_base=base,bucket_count=len(buckets)),indent=2)+'\n')
print('PASS semantic controls and six scoped scan captures')
