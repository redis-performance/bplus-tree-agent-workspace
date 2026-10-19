#!/usr/bin/env python3
import importlib.util,json,shutil,subprocess,hashlib,time
from pathlib import Path
from datetime import datetime,timezone
OUT=Path(__file__).resolve().parent;REL=OUT.relative_to(Path.cwd());BASE=Path('scratch/m6-lookup/variants');rows=[]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def command(cmd,name,cwd,expect=0):
 folder=OUT/'physical-faults';folder.mkdir(exist_ok=True);start=datetime.now(timezone.utc).isoformat();r=subprocess.run(list(map(str,cmd)),cwd=cwd,capture_output=True,text=True,timeout=120)
 (folder/(name+'.stdout')).write_text(r.stdout);(folder/(name+'.stderr')).write_text(r.stderr)
 with (OUT/'candidate-commands.jsonl').open('a') as f:f.write(json.dumps(dict(name=name,variant='fault',command=list(map(str,cmd)),cwd=str(cwd),started_utc=start,finished_utc=datetime.now(timezone.utc).isoformat(),returncode=r.returncode,folder='physical-faults'))+'\n')
 if expect is not None:assert r.returncode==expect,(name,r.returncode,r.stderr[:700])
 return r
src=(BASE/'C/src/zset_btree.c').read_text()
for name,old,new,expected in [
 ('reversed-base','                uint64_t ordered = leaf->reversed ? leaf->score_base - delta :','                uint64_t ordered = leaf->reversed ? leaf->score_base + delta :','exact(score)==expected[physical]'),
 ('logical-output','*position = zbtScoreLeafPhysicalPos(leaf, physical);','*position = physical;','pos==(reversed?count-physical-1:physical)')]:
 assert src.count(old)==1
 d=Path('scratch/m6-lookup/physical-faults')/name;d.mkdir(parents=True)
 for path in ('src','compat','vendor'):shutil.copytree(BASE/'C'/path,d/path)
 (d/'src/zset_btree.c').write_text(src.replace(old,new));shutil.copy2(OUT/'physical-oracle.c',d/'oracle.c')
 command(['clang','-std=c11','-O1','-g','-fsanitize=address,undefined','-fno-sanitize-recover=all','-I.','-Isrc','-Icompat','-Ivendor/redis','oracle.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','oracle'],'build-'+name,d)
 r=command(['./oracle'],name,d,expect=None);assert r.returncode and expected in r.stderr
 rows.append(dict(fault=name,detected=True,returncode=r.returncode,expected_assertion=expected,source_sha256=sha(d/'src/zset_btree.c')))
(OUT/'physical-fault-controls.json').write_text(json.dumps(rows,indent=2)+'\n')
assembly=[]
for v in ('0','A','B','C'):
 r=subprocess.run(['otool','-tvV',str(BASE/v/'build/lookup')],capture_output=True,text=True,check=True);lines=r.stdout.splitlines();func='zbtScoreLeafFindMember';a=next(i for i,l in enumerate(lines) if l.strip()=='_'+func+':');b=next((i for i in range(a+1,len(lines)) if lines[i].startswith('_') and lines[i].endswith(':')),len(lines));section='\n'.join(lines[a:b])+'\n';dest=OUT/'codegen';dest.mkdir(exist_ok=True);(dest/(v+'-leaf.asm')).write_text(section)
 assert '_memchr' in section and '_memcmp' in section
 assembly.append(dict(variant=v,instruction_lines=b-a-1,memchr_call_sites=section.count('_memchr'),memcmp_call_sites=section.count('_memcmp'),sha256=sha(dest/(v+'-leaf.asm'))))
(OUT/'codegen/summary.json').write_text(json.dumps(assembly,indent=2)+'\n');print(json.dumps(dict(faults=rows,assembly=assembly),indent=2))
