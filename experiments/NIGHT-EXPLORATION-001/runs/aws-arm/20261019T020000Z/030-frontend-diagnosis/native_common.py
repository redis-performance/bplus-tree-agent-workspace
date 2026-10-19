import csv,hashlib,json,pathlib
HERE=pathlib.Path(__file__).resolve().parent
CELLS={x['id']:x for x in json.loads((HERE/'cells.json').read_text())}
IDS=json.loads((HERE/'identities.json').read_text())
ORACLE=json.loads((HERE/'fixture-oracle.json').read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def identities(root):
 result={'binaries':{},'sources':{}}
 for name,info in IDS['binaries'].items():
  exe=root/info['path'];result['binaries'][name]=sha(exe);assert result['binaries'][name]==info['sha256'],name
  snapshot=exe.parents[2];expect=dict(IDS['source_hashes'])
  if name.endswith('-A'):expect['src/zset_btree.c']=IDS['candidate_source_sha256']
  if name.startswith('h4-'):expect['bench/iterator_modes.c']=sha(HERE/'inputs/iterator_modes.c')
  result['sources'][name]={n:sha(snapshot/n) for n in expect};assert result['sources'][name]==expect,name
 return result
def check_row(text,contract):
 z=list(csv.DictReader(text.splitlines()));assert len(z)==1;z=z[0];c=CELLS[contract['cell']];n=c['size'];seed=contract['seed'];traversals=(c['requested_ops']+n-1)//n;ref=ORACLE[f'{n}/{seed}'];checksum=(ref[c['frontend']+'_one_traversal_checksum']*traversals)&((1<<64)-1)
 expected=dict(case='iterate' if c['frontend']=='primary' else 'iterator-modes',size=n,seed=seed,requested_ops=c['requested_ops'],member_bytes=16,operations=traversals*n,traversals=traversals,checksum=checksum,warmup_passes=c['warmup_passes'],cpu_start=2,cpu_end=2)
 if c['frontend']=='h4':expected.update(direction=c['direction'],mask=4,encoding='integer',expected_checksum=checksum,construction_fingerprint=ref['h4_construction_fingerprint'])
 for k,v in expected.items():assert z[k]==str(v),(k,z[k],v)
 assert int(z['elapsed_ns'])>0 and int(z['thread_elapsed_ns'])>0 and int(z['tree_bytes'])>0 and int(z['warmup_elapsed_ns'])>0
 return z
SEMANTIC=['case','size','seed','requested_ops','member_bytes','operations','traversals','checksum','warmup_passes','tree_bytes','direction','mask','encoding','expected_checksum','construction_fingerprint']
def same_semantics(a,b):return all(a.get(k)==b.get(k) for k in SEMANTIC)
