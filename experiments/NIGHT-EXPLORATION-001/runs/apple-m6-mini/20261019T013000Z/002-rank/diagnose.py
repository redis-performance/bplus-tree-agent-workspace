#!/usr/bin/env python3
"""Untimed policy term census and static assembly after failed public screen."""
from pathlib import Path
import json,hashlib,difflib,subprocess,importlib.util,sys
sys.dont_write_bytecode = True
OUT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('comparison',OUT/'compare.py');c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
p=OUT/'postmortem';p.mkdir(exist_ok=True)
results=[]
for ident,binary in [('base',c.BASE)]+[(i,c.SNAP/i/'build/rank') for i in c.IDS]:
    result=c.run(['otool','-tvV',binary],f'{ident}-assembly','postmortem')
    raw=Path('scratch/m6-rank')/f'{ident}-postmortem-assembly.txt';raw.write_text(result.stdout);(p/(f'{ident}-assembly.stdout')).unlink()
    lines=result.stdout.splitlines();start=lines.index('_zbtreeRank:');end=next(i for i in range(start+1,len(lines)) if lines[i].startswith('_') and lines[i].endswith(':'));asm=lines[start:end]
    target=p/f'{ident}-zbtreeRank.asm';target.write_text('\n'.join(asm)+'\n')
    ins=[l for l in asm[1:] if l and l[0].isdigit()]
    results.append(dict(variant=ident,function_bytes=int(ins[-1].split()[0],16)-int(ins[0].split()[0],16)+4,static_add_2d_instructions=sum('\tadd.2d\t' in l for l in ins),static_sub_2d_instructions=sum('\tsub.2d\t' in l for l in ins),assembly_sha256=sha(target),full_assembly_local_sha256=sha(raw)))
source=(OUT/'accumulation-diagnostic.c').read_text();code=source.replace('    uint64_t parents = 0,','    uint64_t shorter = 0, suffix_choices = 0;\n    uint64_t parents = 0,').replace('            this_siblings += node->parent_index;','''            this_siblings += node->parent_index;
            uint64_t preceding = node->parent_index;
            uint64_t following = node->parent->n.count - preceding - 1;
            shorter += preceding < following ? preceding : following;
            suffix_choices += following < preceding;
            serverAssert(node->parent->child_count[preceding] == node->subtree);
            unsigned long total = 0;
            for (unsigned int j=0;j<node->parent->n.count;j++) total += node->parent->child_count[j];
            serverAssert(total == node->parent->n.subtree);''').replace('#ifdef COUNT_MODE\n    printf(','''#ifdef COUNT_MODE
    fprintf(stderr,"POLICY,shorter_terms,%" PRIu64 ",suffix_choices,%" PRIu64 "\\n",shorter,suffix_choices);
    printf(''')
patch=p/'policy-census.patch';patch.write_text(''.join(difflib.unified_diff(source.splitlines(True),code.splitlines(True),fromfile='a/accumulation-diagnostic.c',tofile='b/accumulation-diagnostic.c')))
src=Path('scratch/m6-rank/policy-census.c');src.write_text(code);binary=Path('scratch/m6-rank/build/policy-census')
c.run(['clang','-std=c11','-g','-O3','-DCOUNT_MODE','-Isrc','-Icompat','-Ivendor/redis',src,'compat/standalone.c','vendor/redis/siphash.c','-lm','-o',binary],'build-policy-census','postmortem')
counts=[]
for n in c.SIZES:
    r=c.run([binary,n,1],f'policy-n{n}','postmortem');a=r.stderr.strip().split(',');assert a[:2]==['POLICY','shorter_terms']
    counts.append(dict(size=n,shorter_terms=int(a[2]),mean_shorter_terms=int(a[2])/n,suffix_choices=int(a[4])))
summary=dict(assembly=results,policy_counts=counts,source_sha256=sha(src),binary_sha256=sha(binary),scope='Logical summand census and static instructions, not hardware loads/cycles or exact dynamic branch counts. Source includes baseline and asserts parent/current subtree invariants. No new performance timing.')
(p/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
