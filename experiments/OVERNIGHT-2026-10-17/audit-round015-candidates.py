from pathlib import Path
import ast,hashlib,json,re
P=Path(__file__).resolve().parent;R=P.parents[1];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
tree=ast.parse((P/'verify-round015.py').read_text());function=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='apply_unified');scope={'re':re};exec(compile(ast.Module(body=[function],type_ignores=[]),'<patch-auditor>','exec'),scope);apply=scope['apply_unified']
status={'EXP-002':('REJECT','NONE','Fresh expanded guards reject all retained variants; supersedes earlier C/PARK.'),'EXP-003':('REJECT','NONE','Fresh full-output regressions reject all retained variants.'),'EXP-004':('PARK','A provisional; source NONE','Original mixed-output guard unresolved; additional subsets cannot replace it.'),'EXP-005':('PARK','NONE','Fresh primary confidence bounds fail benefit gate; guards unresolved.')}
records={};checks=0
for experiment,(decision,selection,reason) in status.items():
 base=R/'experiments'/experiment;F=json.loads((base/'freeze.json').read_text());root=R/F['snapshot_root'];old=(root/'control/src/zset_btree.c').read_text()
 for v,files in F['files'].items():
  for n,h in files.items():assert sha(root/v/n)==h,(experiment,v,n);checks+=1
 variants={}
 for v in ['A','B','C']:
  patch=base/'variants'/v/'candidate.patch';actual=root/v/'src/zset_btree.c';assert apply(old,patch.read_text())==actual.read_text();assert actual.read_text()!=old
  variants[v]=dict(patch=str(patch.relative_to(R)),patch_sha256=sha(patch),source_sha256=sha(actual),reconstruction='exact')
 texts=[base/'freeze.json',base/'selection.md',base/'implementation-selection.md',base/'README.md']
 texts.extend(f for f in (base/'proposals').glob('*.md'));texts.extend(f for f in (base/'variants').rglob('implementation.md'))
 records[experiment]=dict(decision=decision,selection=selection,reason=reason,base_commit=F['base_commit'],provenance=F['provenance'],source_baseline_sha256=sha(root/'control/src/zset_btree.c'),records={str(f.relative_to(R)):sha(f) for f in texts},variants=variants)
assert len({r['source_baseline_sha256'] for r in records.values()})==1
assert sha(R/'src/zset_btree.c')==records['EXP-004']['source_baseline_sha256']
result=dict(status='pass',frozen_file_hashes_checked=checks,candidate_patches_reconstructed=12,source_adopted='NONE',population_rounds=4,participants='sequential passes; independent agents unavailable',backend='unknown',model='unknown',token_cost='unknown',experiments=records)
(P/'ROUND-015-CANDIDATE-AUDIT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='experiments'},indent=2))
