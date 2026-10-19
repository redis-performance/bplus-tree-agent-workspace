from pathlib import Path
import shutil,json,csv,io,hashlib,subprocess,datetime,copy
src=Path(__file__).resolve().parent;root=Path('scratch/arm027-auditor-v2-synthetic');root.mkdir(exist_ok=True);schedule=json.loads((src/'schedules/original-comparison.json').read_text());original=json.loads((src/'original-guards.json').read_text());results=[];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=[('diagnostic-all-six-loss','REJECT'),('diagnostic-mixed-loss','PARK'),('diagnostic-unqualified-loss','PHASE_PASS_NOT_ACCEPTANCE'),('wrong-seed',None),('wrong-operations',None),('wrong-checksum',None),('wrong-warmup',None),('wrong-scan-divisibility',None),('child-over60',None),('phase-overcap',None),('after-deadline',None)]
for kind,want in checks:
 p=root/kind;p.mkdir(exist_ok=True);(p/'schedules').mkdir(exist_ok=True);aa=p/'original-AA';aa.mkdir(exist_ok=True);out=p/'original-comparison';out.mkdir(exist_ok=True)
 for name in ['audit-phase.py','original-guards.json','phase-budgets.json']:shutil.copyfile(src/name,p/name)
 (p/'schedules/original-comparison.json').write_text(json.dumps(schedule,indent=2)+'\n')
 receipt=json.loads((src/'composite-correctness.json').read_text());receipt['status']='PASS_COMPOSITE_CORRECTNESS';(p/'composite-correctness.json').write_text(json.dumps(receipt));(p/'timing-freeze.json').write_text(json.dumps(dict(files={n:sha(p/n) for n in ['audit-phase.py','original-guards.json','phase-budgets.json','composite-correctness.json','schedules/original-comparison.json']})))
 qualified=[dict(id='original-'+str(c['size'])+'/'+c['case'],qualified=not(kind=='diagnostic-unqualified-loss' and c['size']==100 and c['case']=='insert')) for c in original]
 beginning=datetime.datetime(2026,10,19,9,tzinfo=datetime.timezone.utc)
 state=dict(status='complete',synthetic_for_local_auditor_test=True,cap_seconds=600,started_utc=beginning.isoformat(),finished_utc=(beginning+datetime.timedelta(seconds=241)).isoformat(),elapsed_seconds=241,schedule_sha256=sha(p/'schedules/original-comparison.json'),runs=[])
 state['timing_freeze_sha256']=sha(p/'timing-freeze.json');state['composite_receipt_sha256']=sha(p/'composite-correctness.json')
 joined={k:receipt[k] for k in ['binding_sha256','original_raw_result_sha256','suffix_raw_result_sha256','guard_binary_sha256','protected_binaries']};joined.update(receipt_sha256=state['composite_receipt_sha256'],original_status='failed',suffix_status='six_command_suffix_complete_pending_independent_closure',snapshots=receipt['snapshots_before']);state['composite_before']=state['composite_after']=joined
 state['protected_before']=state['protected_after']=receipt['protected_binaries'];state['guard_binaries_before']=state['guard_binaries_after']=receipt['guard_binary_sha256']
 expected_sources={}
 for variant in ['actual','actualA','control','A']:
  expected_sources[variant]=dict(receipt['source_hashes'])
  if variant in ['actualA','A']:expected_sources[variant]['src/zset_btree.c']=receipt['candidate_source_sha256']
 state['sources_before']=state['sources_after']=expected_sources
 for i,contract in enumerate(schedule):
  rows=[];n=contract['cell']['size'];requested=contract['cell']['requested_ops']
  for c in [c for c in original if c['size']==n]:
   case=c['case'];traversals=(requested+n-1)//n if case in ['iterate','scan'] else 0;count=n if case in ['insert','delete'] else (traversals*n if traversals else requested)
   checksum={'insert':0,'lookup-hit':requested*(n-1)//2,'lookup-miss':0,'rank':requested*(n-1)//2,'iterate':count*(n-1)//2,'scan':count*(n-1)//2,'update':requested,'delete':n}[case]
   loss=n==100 and case=='insert' and contract['label']=='B' and (kind!='diagnostic-mixed-loss' or contract['block']==0) and kind.startswith('diagnostic')
   rows.append({k:str(v) for k,v in dict(case=case,size=n,requested_ops=requested,member_bytes=16,seed=contract['seed'],operations=count,checksum=checksum,tree_bytes=100,traversals=traversals,warmup_passes=0 if case=='insert' else 1,cpu_start=2,cpu_end=2,elapsed_ns=102000000 if loss else 100000000).items()})
  st=beginning+datetime.timedelta(seconds=i*2);state['runs'].append(dict(contract,returncode=0,checked=True,rows=rows,started_utc=st.isoformat(),finished_utc=(st+datetime.timedelta(seconds=1)).isoformat()))
 aa_state=copy.deepcopy(state);(aa/'result.json').write_text(json.dumps(aa_state));(aa/'audit.json').write_text(json.dumps(dict(complete=True,cells=qualified,raw_sha256={'result.json':sha(aa/'result.json')})))
 if kind=='wrong-seed':state['runs'][0]['rows'][0]['seed']='9999'
 if kind=='wrong-operations':state['runs'][0]['rows'][0]['operations']='1'
 if kind=='wrong-checksum':state['runs'][0]['rows'][1]['checksum']='1'
 if kind=='wrong-warmup':state['runs'][0]['rows'][0]['warmup_passes']='1'
 if kind=='wrong-scan-divisibility':state['runs'][0]['rows'][5]['operations']=str(int(state['runs'][0]['rows'][5]['operations'])+1)
 if kind=='child-over60':state['runs'][0]['finished_utc']=(beginning+datetime.timedelta(seconds=61)).isoformat()
 if kind=='phase-overcap':state['elapsed_seconds']=601
 if kind=='after-deadline':state['finished_utc']='2026-10-19T10:16:00+00:00'
 for r in state['runs']:
  stream=io.StringIO();writer=csv.DictWriter(stream,fieldnames=list(r['rows'][0]));writer.writeheader();writer.writerows(r['rows']);(out/(r['name']+'.csv')).write_text(stream.getvalue());(out/(r['name']+'.stderr')).write_text('')
 (out/'result.json').write_text(json.dumps(state));run=subprocess.run(['python3',str(p/'audit-phase.py'),'--phase','original-comparison'],capture_output=True,text=True)
 (p/'audit.stdout').write_text(run.stdout);(p/'audit.stderr').write_text(run.stderr)
 if want is not None:
  assert run.returncode==0,(kind,run.stderr);observed=json.loads((out/'audit.json').read_text())['decision'];assert observed==want,(kind,observed)
 else:assert run.returncode!=0,(kind,'accepted invalid synthetic evidence');observed='REJECTED_INVALID_INPUT'
 results.append(dict(synthetic_test=kind,expected=want or 'REJECTED_INVALID_INPUT',observed=observed))
(src/'TIMING-LOCAL-CHECKS.json').write_text(json.dumps(dict(status='PASS',scope='Synthetic local independent auditor tests only, no host access or workload. Invented data under ignored scratch are NOT scientific measurements.',tests=results,script_sha256=sha(Path(__file__))),indent=2)+'\n');print(results)
