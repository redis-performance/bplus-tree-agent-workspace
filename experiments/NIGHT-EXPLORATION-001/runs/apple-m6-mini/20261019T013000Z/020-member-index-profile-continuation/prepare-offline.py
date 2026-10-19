#!/usr/bin/env python3
"""Offline continuation preparation only: inspect immutable files, no workloads/import cache."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import hashlib,json,re,struct,ast,bisect,csv,io,subprocess,time
R=Path.cwd();E=Path(__file__).resolve().parent;OLD=E.parent/'019-corrected-member-index-profile';S=R/'scratch/m6-corrected-member-index-profile-continuation'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,x):Path(p).write_text(json.dumps(x,indent=2)+'\n')
def utc():return datetime.now(timezone.utc).isoformat()
assert not (E/'PREPARATION.json').exists(),'no overwrite';started=utc()
freeze=json.loads((OLD/'freeze.json').read_text());assert len(freeze['files_sha256'])==53 and all(sha(p)==h for p,h in freeze['files_sha256'].items())
oldplan=json.loads((OLD/'PLAN.json').read_text());state=json.loads((OLD/'capture-status.json').read_text());oldsummary=json.loads((OLD/'summary.json').read_text());records=[json.loads(x) for x in (OLD/'commands.jsonl').read_text().splitlines()]
assert state['status'].startswith('INCOMPLETE') and state['completed_captures']==2 and state['exclusive_runner_release_safe'] and len(records)==3 and len(oldsummary)==2
assert state['phase_wall_seconds']+480<600
for i,rec in enumerate(records):
 item=oldplan['captures'][i];assert rec['returncode']==0 and rec['release_safe'] and rec['child_reaped'] and rec['owned_group_empty'] and not rec['timed_out']
 assert rec['name']==f"{i:02d}-{item['case']}-{item['size']}-s{item['seed']}" and rec['environment_overrides']=={'PROFILE_USEC':'1000'}
 for x in rec['raw'].values():assert sha(x['path'])==x['sha256']
# Read-only static section dump, bounded30s; original stream remains private.
cmd=['/usr/bin/otool','-l',oldplan['binary']];t=time.monotonic();before=utc();p=subprocess.run(cmd,capture_output=True,timeout=30);assert p.returncode==0
(S/'section-dump.stdout').write_bytes(p.stdout);(S/'section-dump.stderr').write_bytes(p.stderr)
save(E/'OFFLINE-COMMAND.json',dict(command=cmd,bound_seconds=30,started_utc=before,finished_utc=utc(),wall_seconds=time.monotonic()-t,returncode=p.returncode,stdout_sha256=sha(S/'section-dump.stdout'),stderr_sha256=sha(S/'section-dump.stderr'),scope='Read-only existing binary load commands; no benchmark/build/profile'))
(E/'section-dump.txt').write_text(p.stdout.decode().replace(str(R),'<workspace>'))
data=Path(oldplan['binary']).read_bytes();assert struct.unpack_from('<I',data)[0]==0xfeedfacf;pos=32;sections=[]
for _ in range(struct.unpack_from('<I',data,16)[0]):
 command,size=struct.unpack_from('<II',data,pos)
 if command==0x19:
  for j in range(struct.unpack_from('<I',data,pos+64)[0]):
   off=pos+72+j*80;section=data[off:off+16].split(b'\0')[0].decode();segment=data[off+16:off+32].split(b'\0')[0].decode();addr,length=struct.unpack_from('<QQ',data,off+32);sections.append(dict(segment=segment,section=section,address=addr,size=length))
 pos+=size
codegen=json.loads((OLD/'codegen.json').read_text());mapping=codegen['enabled_mapping'];mapping['sections']=sections
stubs=next(x for x in sections if x['segment']=='__TEXT' and x['section']=='__stubs');assert (stubs['address']-mapping['image_vmaddr'],stubs['address']+stubs['size']-mapping['image_vmaddr'])==(74408,74828)
save(E/'codegen.json',codegen);save(E/'sections.json',dict(binary_sha256=sha(oldplan['binary']),image_vmaddr=mapping['image_vmaddr'],sections=sections,source='Exact current immutable Mach-O64 segment/section records; independently retained otool -l stream'))
plan=dict(oldplan);plan.update(identity='M6-MEMBER-INDEX-PROFILE-CONTINUATION-001',classification='SEPARATE continuation of13 previously unstarted captures plus offline rederivation of3 retained captures;019 remains INCOMPLETE',captures=[dict(**item,original_index=i,origin_campaign='020') for i,item in enumerate(oldplan['captures']) if i>=3],phase_cap_seconds=480,prior_phase_seconds=state['phase_wall_seconds'],combined_actual_phase_cap_seconds=state['phase_wall_seconds']+480,prior_profile_published_commit=json.loads((OLD/'EXCLUSIVE-RELEASE.json').read_text())['published_commit'],prior_status='INCOMPLETE; no retry or changed019 evidence',original_indices_completed=[0,1,2],indices_to_execute=list(range(3,16)),repair_pause='Record original019finished UTC through actual020start separately; do not count as a continuous original phase',classifier='__text uses frozen text symbols plus all coalesced aliases; __stubs retained as import-stub/unknown-target; all other own-image PCs retained unknown with relative image offset and mapping_limit. No nearest-symbol fallback outside __text.',parent_watchdog='Copied reviewed019 SIGALRM deferral through owned cleanup/journal; parent min480s/absolute07:15UTC minus10s cleanup reserve.',participant='/root/followup_proposal_c',backend='Inherited Codex/GPT-6 family; exact serving model/token/currency cost unknown')
save(E/'PLAN.json',plan)
# Generate continuation from frozen019 source; never import it, so no old __pycache__ writes.
source=(OLD/'capture.py').read_text();tree=ast.parse(source);derive_node=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='derive');fragment=(E/'classifier-fragment.py').read_text();lines=source.splitlines(True);source=''.join(lines[:derive_node.lineno-1])+fragment+'\n'+''.join(lines[derive_node.end_lineno:])
source=source.replace("S=R/'scratch/m6-corrected-member-index-profile'","S=R/'scratch/m6-corrected-member-index-profile-continuation'")
source=source.replace("started=time.monotonic();deadline=min(cutoff,time.time()+600);rows=[];", "started=time.monotonic();deadline=min(cutoff,time.time()+480);rows=json.loads((E/'offline-summary.json').read_text());assert len(rows)==3;" )
source=source.replace('planned_captures=16','planned_captures=13,combined_planned_captures=16,prior_retained_captures=3,original019status=\'INCOMPLETE\',repair_pause_start_utc=PLAN[\'prior_finished_utc\'],repair_pause_end_utc=utc()')
source=source.replace("for i,item in enumerate(PLAN['captures']):", "for item in PLAN['captures']:\n   i=item['original_index']")
source=source.replace('600-(time.monotonic()-started)','480-(time.monotonic()-started)').replace('time.monotonic()-started<600','time.monotonic()-started<480')
source=source.replace("state['status']='COMPLETE descriptive capture set; sufficient only if all16>=10PCs and uncapped'", "state['status']='COMPLETE020 continuation; combined16 descriptive rows,019 remains INCOMPLETE'")
source=source.replace('completed_captures=len(rows),all_sufficient=', 'completed_new_captures=len(rows)-3,combined_captures=len(rows),combined_actual_phase_seconds=PLAN[\'prior_phase_seconds\']+time.monotonic()-started,all_sufficient=')
plan['prior_finished_utc']=state['finished_utc'];save(E/'PLAN.json',plan);(E/'capture.py').write_text(source);ast.parse(source)
oldrun=ast.get_source_segment((OLD/'capture.py').read_text(),next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='run'));newtree=ast.parse(source);newrun=ast.get_source_segment(source,next(n for n in newtree.body if isinstance(n,ast.FunctionDef) and n.name=='run'));assert oldrun==newrun
# Evaluate only pure classifier/derive definitions from new source, with no import/main/run execution.
ns=dict(Path=Path,PLAN=plan,re=re,bisect=bisect,Counter=Counter,csv=csv,io=io)
functions=[n for n in newtree.body if isinstance(n,ast.FunctionDef) and n.name in ['classify_pc','derive']];exec(compile(ast.Module(body=functions,type_ignores=[]),'<offline-classifier>','exec'),ns)
rows=[];pc_total=0
for i,rec in enumerate(records):
 paths={ch:R/x['path'] for ch,x in rec['raw'].items()};item=dict(**oldplan['captures'][i],original_index=i,origin_campaign='019');row=ns['derive'](rec,paths,item,mapping);rows.append(row);pc_total+=row['sample_count']
 if i<2:
  original=oldsummary[i]
  assert all(row[k]==v for k,v in original.items() if k!='pc_bins')
  keys=['module','symbol','offset_bytes','symbol_image_offset','symbol_aliases','symbol_ambiguous']
  def project(bins):
   counter=Counter()
   for b in bins:counter[tuple(json.dumps(b[k],sort_keys=True) for k in keys)]+=b['samples']
   return counter
  assert project(row['pc_bins'])==project(original['pc_bins'])
assert rows[2]['sample_count']==274
stub_bins=[x for x in rows[2]['pc_bins'] if x['classification']=='import-stub'];assert sum(x['samples'] for x in stub_bins)==3 and {x['own_image_pc_offset']:x['samples'] for x in stub_bins}=={74604:2,74616:1}
assert sum(sum(x['samples'] for x in r['pc_bins']) for r in rows)==pc_total
save(E/'offline-summary.json',rows);(E/'019-summary-preserved.json').write_bytes((OLD/'summary.json').read_bytes())
rawinputs={str((OLD/'freeze.json').relative_to(R)):sha(OLD/'freeze.json'),str((OLD/'capture-status.json').relative_to(R)):sha(OLD/'capture-status.json'),str((OLD/'commands.jsonl').relative_to(R)):sha(OLD/'commands.jsonl'),str((OLD/'summary.json').relative_to(R)):sha(OLD/'summary.json'),str((OLD/'EXCLUSIVE-RELEASE.json').relative_to(R)):sha(OLD/'EXCLUSIVE-RELEASE.json')}
for rec in records:
 for x in rec['raw'].values():rawinputs[x['path']]=x['sha256']
save(E/'PRIOR-INPUTS.json',rawinputs)
save(E/'planned-commands.json',[dict(original_index=i['original_index'],command=[plan['binary'],'--case',i['case'],'--size',str(i['size']),'--ops','10000000','--member-bytes','16','--seed',str(i['seed']),'--warmup-passes','3'],environment_overrides={'PROFILE_USEC':'1000'}) for i in plan['captures']])
save(E/'PREPARATION.json',dict(status='OFFLINE READY; no new enabled execution, build or profile',participant=plan['participant'],backend=plan['backend'],started_utc=started,finished_utc=utc(),original53freeze_all_hashes_match=True,original019status_unchanged=True,original_rows_preserved_byte_exact=True,original_two_summary_rows_projection_exact=True,retained_captures=3,retained_pcs=[r['sample_count'] for r in rows],all_retained_pc_count=pc_total,third_capture_stub_pcs=3,third_stub_offsets={str(x['own_image_pc_offset']):x['samples'] for x in stub_bins},source_binary_sampler_changes=False,new_enabled_executions=0,run_function_copy_byte_exact=True,run_function_sha256=hashlib.sha256(oldrun.encode()).hexdigest(),no_old_module_import_or_pycache=True,no_019_file_write=True,new_indices=list(range(3,16)),original_phase_seconds=state['phase_wall_seconds'],new_phase_cap=480,combined_phase_cap=state['phase_wall_seconds']+480,repair_pause_start_utc=state['finished_utc'],repair_pause_note='Actual continuation start recorded at launch, separate from phase wall caps.'))
print('OFFLINE READY', [r['sample_count'] for r in rows], '3 stubs retained;13 indices', [i['original_index'] for i in plan['captures']])
