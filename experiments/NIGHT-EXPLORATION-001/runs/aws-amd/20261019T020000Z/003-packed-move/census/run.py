import pathlib,subprocess,json,csv,datetime,os,hashlib
p=pathlib.Path('scratch/amd-census');rows=[];records=[]
cases=[('update',100000,101717),('update',1000000,52593),('update',100000,3000000),('insert',100000,100000),('insert',1000000,1000000),('delete',100000,100000),('delete',1000000,1000000)]
for index,(case,n,ops) in enumerate([cases[0]]+cases):
 label=('disabled-' if index==0 else '')+f'{case}-n{n}-ops{ops}';env=os.environ.copy()
 if index==0:env['CENSUS_DISABLED']='1'
 cmd=[str(p/'census'),'--case',case,'--size',str(n),'--ops',str(ops),'--member-bytes','16','--seed','1'];start=datetime.datetime.now(datetime.timezone.utc).isoformat();r=subprocess.run(cmd,env=env,capture_output=True,text=True,timeout=120)
 (p/(label+'.csv')).write_text(r.stdout);(p/(label+'.stderr')).write_text(r.stderr)
 records.append(dict(label=label,command=cmd,start=start,end=datetime.datetime.now(datetime.timezone.utc).isoformat(),returncode=r.returncode));(p/'processes.json').write_text(json.dumps(records,indent=2)+'\n');r.check_returncode()
 counts=json.loads(r.stderr);bench=list(csv.DictReader(r.stdout.splitlines()))[0];rows.append(dict(label=label,counts=counts,checksum=bench['checksum'],tree_bytes=bench['tree_bytes']))
 if index==0:assert counts['encoding_calls']==0 and counts['build_calls']==0 and all(sum(v for k,v in x.items() if k!='bits')==0 for x in counts['widths'])
 if index==1:assert rows[0]['checksum']==rows[1]['checksum'] and rows[0]['tree_bytes']==rows[1]['tree_bytes']
(p/'summary.json').write_text(json.dumps(rows,indent=2)+'\n');(p/'hashes.json').write_text(json.dumps({x:hashlib.sha256((p/x).read_bytes()).hexdigest() for x in ['census','zset_btree.c','census-bench.c']},indent=2)+'\n')
