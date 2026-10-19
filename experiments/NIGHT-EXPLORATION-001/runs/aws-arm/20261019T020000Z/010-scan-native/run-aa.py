from pathlib import Path
import csv,datetime,json,subprocess,time
p=Path(__file__).parent;out=p/'aa.json';assert not out.exists();start=time.monotonic();m=dict(status='running',started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),rows=[])
for block in range(6):
 for n in ([100000,1000000] if block%2==0 else [1000000,100000]):
  seed=101+block%3
  for position in range(4):
   assert time.monotonic()-start<300
   cmd=['scratch/arm-scan-native/base/build/btree-bench','--case','scan','--size',str(n),'--ops','5000000','--member-bytes','16','--seed',str(seed)]
   t=datetime.datetime.now(datetime.timezone.utc).isoformat();r=subprocess.run(cmd,capture_output=True,text=True,timeout=min(60,300-(time.monotonic()-start)));tag=f'aa-{len(m["rows"]):03d}'
   (p/'raw'/(tag+'.stdout')).write_text(r.stdout);(p/'raw'/(tag+'.stderr')).write_text(r.stderr);assert r.returncode==0,r.stderr
   rows=list(csv.DictReader(r.stdout.splitlines()));assert len(rows)==1;row=rows[0];assert row['cpu_start']==row['cpu_end']=='2'
   m['rows'].append(dict(size=n,seed=seed,block=block,position=position,command=cmd,started_utc=t,finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),row=row));out.write_text(json.dumps(m,indent=2)+'\n')
effects=[]
for i in range(0,len(m['rows']),4):
 r=m['rows'][i:i+4];assert len({(x['row']['checksum'],x['row']['operations'],x['row']['tree_bytes']) for x in r})==1
 v=[int(x['row']['elapsed_ns'])/int(x['row']['operations']) for x in r];effect=100*((v[1]+v[2])/(v[0]+v[3])-1);minimum=min(int(x['row']['elapsed_ns']) for x in r)
 effects.append(dict(size=r[0]['size'],seed=r[0]['seed'],block=r[0]['block'],percent=effect,min_window_ns=minimum,qualified=abs(effect)<=1 and minimum>=10000000))
m.update(status='complete',finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,effects=effects);out.write_text(json.dumps(m,indent=2)+'\n');print('PASS48 serial rows; qualification:',{n:all(x['qualified'] for x in effects if x['size']==n) for n in [100000,1000000]})
