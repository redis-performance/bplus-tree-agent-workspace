from pathlib import Path
import json,hashlib,shutil,difflib
P=Path(__file__).resolve().parent;R=P.parents[2];F=json.loads((R/'experiments/EXP-004/freeze.json').read_text());S=R/'scratch/overnight-diag-011';assert not S.exists();S.mkdir();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();files={}
for v in ['control','A']:
 B=S/v;B.mkdir()
 for name,h in F['files'][v].items():
  src=R/F['snapshot_root']/v/name;assert sha(src)==h;dst=B/name;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
 p=B/'bench/iterator_modes.c';old=p.read_text();s=old;a=s.index('static uint64_t traverse(');b=s.index('static void verify(',a);fun=s[a:b];clones=''
 for mask in [4,6,7]:
  code=fun.replace('static uint64_t traverse(',f'static uint64_t traverse_fixed{mask}(').replace('    uint64_t sum = 0;','    UNUSED(mask);\n    uint64_t sum = 0;').replace('mask&',f'{mask}&');clones+=code
 s=s[:b]+clones+s[b:]
 replacements=[('const char *encoding="integer";','const char *encoding="integer",*caller="dynamic";'),('        else if(!strcmp(a,"--encoding"))encoding=v;','        else if(!strcmp(a,"--encoding"))encoding=v;\n        else if(!strcmp(a,"--caller"))caller=v;'),('    uint64_t rng=seed;', '''    uint64_t (*run_traversal)(zbtreeSet*,size_t,size_t,int,unsigned)=traverse;
    if(!strcmp(caller,"fixed")) {
        if(mask==4)run_traversal=traverse_fixed4;
        else if(mask==6)run_traversal=traverse_fixed6;
        else if(mask==7)run_traversal=traverse_fixed7;
        else return 2;
    } else if(strcmp(caller,"dynamic")) return 2;
    uint64_t rng=seed;'''),('traverse(tree,n,passes,reverse,mask)','run_traversal(tree,n,passes,reverse,mask)'),('traverse(tree,n,traversals,reverse,mask)','run_traversal(tree,n,traversals,reverse,mask)')]
 for a,b in replacements:assert s.count(a)==1,(a,s.count(a));s=s.replace(a,b)
 p.write_text(s);patch=''.join(difflib.unified_diff(old.splitlines(True),s.splitlines(True),fromfile='a/bench/iterator_modes.c',tofile='b/bench/iterator_modes.c'))
 if v=='control':(P/'caller.patch').write_text(patch)
 else:assert patch==(P/'caller.patch').read_text()
 files[v]={str(p.relative_to(B)):sha(p) for p in B.rglob('*') if p.is_file()}
(P/'freeze.json').write_text(json.dumps(dict(base_commit=F['base_commit'],snapshot_root=str(S.relative_to(R)),provenance='uncommitted caller-context diagnostic; retained EXP-004 control/A sources unchanged',plan_sha256=sha(P/'PLAN.md'),files=files),indent=2)+'\n')
