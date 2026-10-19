"""Independently reconstruct immutable ARM exact-mask screen; never execute its code."""
import csv,decimal,hashlib,io,json,statistics,subprocess
from pathlib import Path
from datetime import datetime
D=decimal.Decimal
REV='6bcd8e575';BASE='experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/'
P=BASE+'026-exp005A-replication/';inputs={};cache={}
def read(path,rev=REV):
    key=rev+':'+path
    if key not in cache:cache[key]=subprocess.check_output(['git','show',key]);inputs[key]=hashlib.sha256(cache[key]).hexdigest()
    return cache[key]
def obj(path,rev=REV):return json.loads(read(path,rev))
def utc(x):return datetime.fromisoformat(x.replace('Z','+00:00'))
def sha(path,rev=REV):return hashlib.sha256(read(path,rev)).hexdigest()
freeze=obj(P+'execution-freeze.json');expected=obj(P+'expected.json');schedule=obj(P+'screen-schedule.json')
assert read(P+'execution-freeze.json')==read(P+'execution-freeze.json','a9b09cadc')
for name,h in freeze['files'].items():assert sha(P+name)==h
assert len(freeze['files'])==20 and freeze['screen_cap_seconds']==300 and freeze['conditional_screen_rows']==48
assert sha(P+'candidate.patch')==expected['candidate_patch_sha256']=='ca14579cbf4325816d5511697cb0bec5ab0e618ef661830acbc4bfe72a5cc88f'
validation=obj(P+'validation/result.json');gate=obj(P+'codegen-gate.json');record=obj(P+'screen/result.json');post=obj(P+'post-screen-identity-idle.json')
assert read(P+'validation/result.json')==read(P+'validation/result.json','d99bc1077')
assert read(P+'validation-evidence-seal.json')==read(P+'validation-evidence-seal.json','d99bc1077')
assert read(P+'codegen-gate.json')==read(P+'codegen-gate.json','347ec1b7a')
assert validation['status']=='correctness_complete_static_gate_pending' and gate['status']=='PASS'
assert gate['validation_result_sha256']==sha(P+'validation/result.json')
assert gate['execution_freeze_sha256']==record['execution_freeze_sha256']==sha(P+'execution-freeze.json')
assert gate['baseline_mask_instructions']==4 and gate['candidate_mask_instructions']==3 and gate['added_conditional_branches']==0 and gate['ordinary_nonzero_path_instruction_delta']==-1
assert gate['shared_caller_review_pass'] is True
validation_pub=obj(P+'validation/PUBLICATION.json')
for v,h in gate['assembly_sha256'].items():
    item=validation_pub[v+'-asm.stdout'];assert item['raw_sha256']==h
    assert sha(P+'validation/'+v+'-asm.stdout')==item['public_sha256']
assert record['codegen_gate_sha256']==sha(P+'codegen-gate.json')=='cfc93a564b91f4bb722cbd46f28889a4c51124f5c591fa745c01065cc9b04b77'
assert validation['text_sha256']['actual']==validation['text_sha256']['control']=='b17746defd935a8c4d1befc2277cbd06baa92d6ac9881ac3e0ab628a96f646e3'
assert validation['actual_binary_before']==validation['actual_binary_after']==expected['aa_binary_sha256']
binaries={'baseline':expected['aa_binary_sha256'],'candidate':validation['binary_sha256']['A']}
assert binaries==gate['timing_binary_sha256']==record['binary_before']==record['binary_after']
assert binaries['candidate']=='b1cb9e4b2a1df204a75b4b4a3264364c3f0b5b46dbf475bae72c3c9a3ee5811d'
sources={'baseline':expected['source_hashes'],'candidate':dict(expected['source_hashes'],**{'src/zset_btree.c':expected['candidate_source_sha256']})}
assert record['sources_before']==record['sources_after']==sources
for name,h in expected['source_hashes'].items():assert sha(name,expected['commit'])==h
assert validation['actual_sources_before']==validation['actual_sources_after']==expected['source_hashes']
assert validation['protected_before']==validation['protected_after']==expected['protected_binaries']==post['protected_hashes']
assert post['source_hashes']==expected['source_hashes'] and post['frozen_input_hashes']==freeze['files']
assert post['candidate_binary_sha256']==binaries['candidate'] and post['owned_units']==post['owned_cgroup_pids']==[] and post['lease_released_marker'] is False
assert post['source_match'] and post['protected_match'] and post['frozen_match']
assert record['status']=='complete' and len(record['runs'])==len(schedule)==48
# Derive the schedule from the written contract rather than trust the schedule file alone.
derived=[]
for block in range(6):
    for size in ([100000,1000000] if block%2==0 else [1000000,100000]):
        for position,label in enumerate('ABBA'):
            derived.append(dict(index=len(derived),block=block,size=size,seed=401+block%3,position=position,label=label,binary='baseline' if label=='A' else 'candidate',requested_ops=50000000,member_bytes=16))
assert schedule==derived
job=obj(BASE+'jobs/arm026-exp005a-screen.job-output.txt');assert job['cpu']==2 and job['returncode']==0 and job['limit_seconds']==300
assert utc(job['started_utc'])<=utc(record['started_utc'])<utc(freeze['cutoff_new_phase'])
assert utc(record['finished_utc'])<=utc(job['finished_utc'])<utc('2026-10-19T08:00:00Z')
assert 0<record['elapsed_seconds']<=300 and (utc(job['finished_utc'])-utc(job['started_utc'])).total_seconds()<=300
assert utc(validation['finished_utc'])<utc(record['started_utc'])<utc(record['finished_utc'])<utc(post['updated_utc'])
rows=[];last_end=utc(record['started_utc']);pub=obj(P+'screen/PUBLICATION.json')
for want,run in zip(derived,record['runs']):
    assert all(run[k]==v for k,v in want.items())
    name=f"b{want['block']}-n{want['size']}-p{want['position']}-{want['label']}";assert run['name']==name
    command=['<'+want['binary']+'>/build/adapter-requalification/btree-bench','--case','iterate','--size',str(want['size']),'--ops','50000000','--member-bytes','16','--seed',str(want['seed'])]
    assert run['command']==command and run['returncode']==0
    start,end=utc(run['started_utc']),utc(run['finished_utc']);assert last_end<=start<end<=utc(record['finished_utc']) and (end-start).total_seconds()<=30;last_end=end
    raw=read(P+'screen/'+name+'.csv');parsed=list(csv.DictReader(io.StringIO(raw.decode())));assert len(parsed)==1;row=parsed[0];assert row==run['row']
    n=want['size'];exact=dict(case='iterate',size=n,seed=want['seed'],requested_ops=50000000,operations=50000000,member_bytes=16,traversals=50000000//n,checksum=50000000*(n-1)//2,warmup_passes=1,cpu_start=2,cpu_end=2)
    assert all(row[k]==str(v) for k,v in exact.items());assert int(row['tree_bytes'])>0 and int(row['elapsed_ns'])>=10000000
    assert D(row['elapsed_ns'])<=D(str((end-start).total_seconds()))*D(10**9)
    assert abs(D(row['ns_per_op'])-D(row['elapsed_ns'])/D(50000000))<=D('.000501')
    assert sha(P+'screen/'+name+'.csv')==pub[name+'.csv']['raw_sha256']==pub[name+'.csv']['public_sha256']
    err=read(P+'screen/'+name+'.stderr');assert not err.strip() and pub[name+'.stderr']['raw_bytes']==0 and pub[name+'.stderr']['raw_sha256']==hashlib.sha256(b'').hexdigest()
    rows.append(dict(want,elapsed_ns=int(row['elapsed_ns']),tree_bytes=int(row['tree_bytes'])))
effects=[];mem={}
for size in [100000,1000000]:
    for block in range(6):
        q=sorted([r for r in rows if r['size']==size and r['block']==block],key=lambda r:r['position']);assert len(q)==4 and len({r['tree_bytes'] for r in q})==1
        fixture=(size,q[0]['seed']);previous=mem.setdefault(fixture,q[0]['tree_bytes']);assert previous==q[0]['tree_bytes']
        a=D(q[0]['elapsed_ns']+q[3]['elapsed_ns']);candidate=D(q[1]['elapsed_ns']+q[2]['elapsed_ns']);effect=100*(candidate/a-1)
        effects.append({'size':size,'block':block,'seed':q[0]['seed'],'effect_pct_decimal':str(effect),'minimum_window_ns':min(r['elapsed_ns'] for r in q),'primary_pass':effect<=-2})
# Only after reconstructing effects, compare worker summary (never import analyzer).
reported=obj(P+'screen/audit.json');assert reported['rows']==48 and reported['blocks']==12
for effect,r in zip(effects,reported['effects']):
    assert (effect['size'],effect['block'])==(r['size'],r['block'])
    assert abs(D(effect['effect_pct_decimal'])-D(str(r['effect_pct'])))<D('1e-10')
    assert effect['minimum_window_ns']==r['minimum_window_ns'] and effect['primary_pass']==r['primary_pass']
assert all(e['primary_pass'] for e in effects) and reported['all_primary_blocks_pass'] and reported['decision']=='PARK' and reported['source_selection']=='NONE'
for name,h in reported['evidence_sha256'].items():assert pub[name]['raw_sha256']==h
for name,meta in pub.items():assert sha(P+'screen/'+name)==meta['public_sha256']
seal_counts={}
for filename in ['validation-evidence-seal.json','screen-evidence-seal.json']:
    seal=obj(P+filename)
    for name,h in seal.items():assert sha(P+name)==h
    seal_counts[filename]=len(seal)
# Original same-binary qualification is a separate earlier seed701-703 contract.
aa_path=BASE+'024-corrected-iterator/aa/result.json';aa=obj(aa_path,'73c9e313f')
assert aa['status']=='complete' and aa['binary_sha256_before']==aa['binary_sha256_after']==binaries['baseline']
assert aa['source_hashes_before']==aa['source_hashes_after']==expected['source_hashes']
assert utc(aa['finished_utc'])<utc(record['started_utc']) and len(aa['runs'])==48
assert {int(r['row']['seed']) for r in aa['runs']}=={701,702,703}
assert all(r['row']['case']=='iterate' and int(r['row']['operations'])==50000000 and int(r['row']['member_bytes'])==16 for r in aa['runs'])
# Confirm README issue fixed at immutable published revision, not only working tree.
readme=read('README.md','03445990a').decode();assert 'Current original-adapter decision: REJECT/NONE' in readme and 'Overall decision remains PARK.' not in readme
summary={str(size):{'median_effect_pct':str(statistics.median(D(e['effect_pct_decimal']) for e in effects if e['size']==size)),'minimum_effect_pct':min(D(e['effect_pct_decimal']) for e in effects if e['size']==size).to_eng_string(),'maximum_effect_pct':max(D(e['effect_pct_decimal']) for e in effects if e['size']==size).to_eng_string(),'minimum_window_ns':min(r['elapsed_ns'] for r in rows if r['size']==size)} for size in [100000,1000000]}
result={'status':'pass','revision':REV,'raw_processes':48,'blocks':12,'decision':'PARK','source_selection':'NONE','new_measured_population':False,'effects':effects,'summary':summary,'started_utc':record['started_utc'],'finished_utc':record['finished_utc'],'phase_elapsed_seconds':record['elapsed_seconds'],'binary_sha256':binaries,'frozen_inputs':len(freeze['files']),'published_screen_files':len(pub),'verified_evidence_seals':seal_counts,'input_file_count':len(inputs),'input_manifest_sha256':hashlib.sha256(json.dumps(inputs,sort_keys=True).encode()).hexdigest(),'readme_fixed_revision':'03445990a','limits':['Raw CSV and frozen evidence reconstruction only; no benchmark, build, runner access or worker audit-code import.','No new live binary hash read by this reviewer; identity assertions reconstructed from immutable pre/post records and seals.','Prior024 same-binary AA on701-703 qualifies the unchanged contract; screen401-403 is not an additional standalone AA phase.','Native diagnostic primary only; missing guards, independent fresh confirmation, matched profile and acceptance review keep PARK.','Static4-to3 mask reduction does not causally explain elapsed change; other layout/shared-caller changes remain.','HistoricalEXP005PARK and all other host decisions unchanged; lease release still pending.']}
Path(__file__).with_name('raw-audit.json').write_text(json.dumps(result,indent=2)+'\n')
Path(__file__).with_name('input-hashes.json').write_text(json.dumps(inputs,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','raw_processes','blocks','decision','summary','verified_evidence_seals','input_file_count']}))
