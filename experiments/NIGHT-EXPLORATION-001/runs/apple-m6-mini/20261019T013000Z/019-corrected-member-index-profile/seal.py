#!/usr/bin/env python3
"""Seal static preparation evidence only; never import/execute capture driver."""
from pathlib import Path
from collections import Counter,defaultdict
import json,hashlib,re,struct,ast
R=Path.cwd();E=Path(__file__).resolve().parent;S=R/'scratch/m6-corrected-member-index-profile';BASE=E.parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,x):Path(p).write_text(json.dumps(x,indent=2)+'\n')
prep=json.loads((E/'PREPARATION.json').read_text());assert prep['enabled_executed'] is False
for f,h in prep['inputs_sha256'].items():assert sha(f)==h
for x in prep['binaries'].values():assert sha(x['path'])==x['sha256']
def bodies(file):
 result=[];body=None
 for line in Path(file).read_text().splitlines():
  if re.fullmatch(r'[_A-Za-z.$][A-Za-z0-9_.$]*:',line):body=dict(name=line[:-1],instructions=[]);result.append(body)
  elif body is not None:
   m=re.match(r'^([0-9a-fA-F]{16})\s+(.+)$',line)
   if m:body['instructions'].append(m.group(2).split(';',1)[0].strip())
 counts=Counter(x['name'] for x in result)
 for x in result:
  x['comparison_eligible']=counts[x['name']]==1;x['instruction_lines']=len(x['instructions']);x['entry_prefix']=x['instructions'][:16];x['instruction_text_sha256']=hashlib.sha256('\n'.join(x['instructions']).encode()).hexdigest()
 return result
inventories={label:bodies(S/'logs'/(label+'-frontend-otool.stdout')) for label in prep['binaries']}
public_inv={label:[{k:v for k,v in row.items() if k!='instructions'} for row in rows] for label,rows in inventories.items()}
original={x['name']:x for x in inventories['original'] if x['comparison_eligible']};disabled={x['name']:x for x in inventories['disabled'] if x['comparison_eligible']};enabled={x['name']:x for x in inventories['enabled'] if x['comparison_eligible']}
comparisons=[]
for name in sorted(set(original)&set(disabled)&set(enabled)):
 comparisons.append(dict(name=name,original_instructions=original[name]['instruction_lines'],disabled_instructions=disabled[name]['instruction_lines'],enabled_instructions=enabled[name]['instruction_lines'],original_disabled_exact_instruction_text_equal=original[name]['instructions']==disabled[name]['instructions']))
# Mach-O64 load-command inspection supplies the actual enabled image/section ranges.
binary=Path(prep['binaries']['enabled']['path']);data=binary.read_bytes();magic=struct.unpack_from('<I',data)[0];assert magic==0xfeedfacf;ncmds=struct.unpack_from('<I',data,16)[0];pos=32;vmaddr=None;text=None
for _ in range(ncmds):
 cmd,size=struct.unpack_from('<II',data,pos)
 if cmd==0x19:
  segname=data[pos+8:pos+24].split(b'\0')[0].decode();vm=struct.unpack_from('<Q',data,pos+24)[0];nsects=struct.unpack_from('<I',data,pos+64)[0]
  if segname=='__TEXT':vmaddr=vm
  for i in range(nsects):
   off=pos+72+i*80;sect=data[off:off+16].split(b'\0')[0].decode();seg=data[off+16:off+32].split(b'\0')[0].decode();addr,length=struct.unpack_from('<QQ',data,off+32)
   if sect=='__text' and seg=='__TEXT':text=(addr,addr+length)
 pos+=size
assert vmaddr is not None and text
symbols=[]
for line in (S/'logs/enabled-nm.stdout').read_text().splitlines():
 m=re.fullmatch(r'([0-9a-fA-F]+) [tT] (.+)',line)
 if m and text[0]<=int(m[1],16)<text[1]:symbols.append(dict(address=int(m[1],16),name=m[2]))
assert symbols==sorted(symbols,key=lambda x:x['address'])
alias_groups=defaultdict(list)
for entry in symbols:alias_groups[entry['address']].append(entry['name'])
symbols=[dict(address=address,name=names[0],aliases=names) for address,names in alias_groups.items()]
mapdata=dict(image_vmaddr=vmaddr,text_start=text[0],text_end=text[1],symbols=symbols,binary_sha256=sha(binary),mapping='Runtime PC-base + exact Mach-O image vmaddr; nearest actual local/global text symbol, only within exact __text; image-relative symbol start disambiguates duplicate outlined names')
tree=bodies(S/'logs/native-tree-otool.stdout');tree_public=[{k:v for k,v in x.items() if k!='instructions'} for x in tree]
codegen=dict(enabled_mapping=mapdata,frontend_inventories=public_inv,unique_frontend_comparisons=comparisons,native_tree_object_sha256=sha(S/'native/tree.o'),shared_native_tree_object='Identical actual tree.o linked into original, disabled and enabled; no tree source inclusion into frontend',tree_object_function_inventory=tree_public,limits='Counts are static instruction lines, not costs or CFG proof. Frontend register/frame/control flow changes from hooks are explicit; source equivalence with hooks removed does not claim runtime/codegen equivalence. Linked relocations/addresses differ. Duplicate outlined labels are not paired by ordinal.')
save(E/'codegen.json',codegen)
plan=dict(identity='M6-CORRECTED-MEMBER-INDEX-SOFTWARE-PROFILE-001',classification='PREPARATION ONLY baseline diagnosis, no source optimization/candidate/population',source_c_sha256=prep['inputs_sha256']['src/zset_btree.c'],source_h_sha256=prep['inputs_sha256']['src/zset_btree.h'],corrected_adapter_header_sha256=prep['inputs_sha256']['compat/server.h'],corrected_adapter_c_sha256=prep['inputs_sha256']['compat/standalone.c'],binary=prep['binaries']['enabled']['path'],captures=[dict(case=case,size=n,seed=seed) for case in ['lookup-hit','lookup-miss','rank','scan'] for n in [100000,1000000] for seed in [1,2]],requested_ops=10000000,member_bytes=16,warmup_passes=3,environment_overrides={'PROFILE_USEC':'1000'},minimum_captured_PCs=10,maximum_captured_PCs=65536,uncapped_required=True,insufficient_policy='Keep every fixed row; insufficient stays insufficient; no repeat/retune',phase_cap_seconds=600,child_cap_seconds=45,child_clipped_remaining=True,cleanup_reserve_seconds=10,absolute_stop_utc='2026-10-19T07:15:00+00:00',sample_scope='Hooks immediately after original start timestamp and before original elapsed timestamp around selected operation, after warmup/expected-work preparation; signal boundary/hook code can be sampled. No fixture setup/warmup/post-oracle inside bracket.',scan_semantics='Scan may emit duplicate entries. Preserve canonical actual emitted operations, checksum, traversals and independent full byte/score/coverage oracle; no n-only replacement.',timing_fields_used=False,metrics='PC counts/locations only; no cycles, cache costs, latency, speed or unbiased time-share claims',authorization='Root and distinct independent PASS, published exact freeze ACK, exclusive idle runner, no captures during preparation',participant='/root/followup_proposal_c',backend='Inherited Codex/GPT-6 family; exact serving model/token/currency cost unknown')
save(E/'PLAN.json',plan)
planned=[]
for row in plan['captures']:
 cmd=[plan['binary'],'--case',row['case'],'--size',str(row['size']),'--ops','10000000','--member-bytes','16','--seed',str(row['seed']),'--warmup-passes','3'];planned.append(dict(**row,command=cmd,environment_overrides=plan['environment_overrides']))
save(E/'planned-commands.json',planned)
ast.parse((E/'capture.py').read_text());ast.parse((E/'prepare.py').read_text());ast.parse((E/'seal.py').read_text())
records=json.loads((E/'commands.json').read_text());assert all(x['returncode']==0 and not x['timed_out'] for x in records)
for rec in records:
 for x in rec['raw'].values():assert sha(x['path'])==x['sha256']
# Generic public static dumps. Raw originals remain private with command hashes.
for name in ['original-nm','disabled-nm','enabled-nm','original-frontend-otool','disabled-frontend-otool','enabled-frontend-otool','native-tree-otool']:
 text=(S/'logs'/(name+'.stdout')).read_text().replace(str(R),'<workspace>');assert not re.search('/'+'Users/',text);(E/(name+'.txt')).write_text(text)
# Raw correctness CSV elapsed fields stay private; public rows retain only semantics/metadata.
validation=json.loads((E/'validation.json').read_text());fields=['case','size','requested_ops','member_bytes','seed','operations','tree_bytes','checksum','traversals','warmup_passes','binary'];validation['rows']=[{k:r[k] for k in fields} for r in validation['rows']];save(E/'validation.json',validation)
prep.update(status='READY FOR ROOT/INDEPENDENT STATIC REVIEW; NO CAPTURES AUTHORIZED',static_commands=len(records),native_tree_shared_object=True,frontend_codegen=codegen['unique_frontend_comparisons'],profile_binary_not_executed=True,driver_syntax_AST_only='PASS',source_equivalence='Exact byte restoration by removing only three conditional hook blocks; disabled frontend still has different assertion source filename/line constants',correctness='24 bounded processes across original/disabled/sanitizer-disabled; enabled binary never executed')
save(E/'PREPARATION.json',prep)
# Files are sealed only after all sources and evidence are final.
owned=[p for p in E.iterdir() if p.is_file() and p.name not in ['freeze.json']]
freeze={str(p.relative_to(R)):sha(p) for p in owned}
freeze.update(prep['inputs_sha256']);freeze.update({x['path']:x['sha256'] for x in prep['binaries'].values()});freeze.update(prep['all_build_objects_sha256'])
save(E/'freeze.json',dict(status='PREPARED ONLY; no enabled binary execution or capture authorized',files_sha256=freeze,participant=plan['participant'],backend=plan['backend']))
print('SEALED',len(freeze),'inputs;16 planned captures; static comparisons',comparisons)
