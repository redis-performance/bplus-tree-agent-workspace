#!/usr/bin/env python3
"""Source and saved-ELF inspection only. Never executes compiled code."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import generate

HERE=Path(__file__).resolve().parent
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def function_region(source,name):
    m=re.search(r'\b'+re.escape(name)+r'\([^;{}]*\)\s*\{',source)
    assert m,name
    start=m.start();i=m.end();depth=1
    while depth:
        if source[i]=='{':depth+=1
        if source[i]=='}':depth-=1
        i+=1
    return start,i

def apply_patch(original,patch):
    lines=original.splitlines(True);out=[];cursor=0;pieces=patch.splitlines(True);i=0
    while i<len(pieces):
        m=re.match(r'@@ -(\d+)(?:,\d+)? \+\d+(?:,\d+)? @@',pieces[i])
        if not m:i+=1;continue
        start=int(m[1])-1;assert start>=cursor;out+=lines[cursor:start];cursor=start;i+=1
        while i<len(pieces) and not pieces[i].startswith('@@'):
            line=pieces[i];i+=1;assert line[0] in ' +-'
            if line[0] in ' -':assert lines[cursor]==line[1:];cursor+=1
            if line[0] in ' +':out.append(line[1:])
    return ''.join(out+lines[cursor:])

def disassembly_functions(text):
    result={};name=None
    for line in text.splitlines():
        m=re.match(r'^([0-9a-f]+) <([^>]+)>:$',line)
        if m:name=m[2];result[name]=[];continue
        if name is None:continue
        fields=line.split('\t')
        if len(fields)<3 or not re.fullmatch(r'\s*[0-9a-f]+:',fields[0]):continue
        instruction=fields[2].strip()
        if not instruction:continue
        parts=instruction.split(None,1)
        result[name].append((int(fields[0].strip()[:-1],16),parts[0],parts[1] if len(parts)>1 else ''))
    return result

def prove_original_call(text):
    funcs=disassembly_functions(text)
    leafnames=[n for n in funcs if n=='zbtScoreLeafFindMember' or n.startswith('zbtScoreLeafFindMember.')]
    assert leafnames,'Original leaf body missing'
    for name in leafnames:
        body=funcs[name]
        assert any('memchr' in args and op.startswith('call') for _,op,args in body),name
        assert any('memcmp' in args and op.startswith('call') for _,op,args in body),name
    reports=[]
    for name,body in funcs.items():
        if not name.startswith('shLeaf'):continue
        addresses={address:i for i,(address,_,_) in enumerate(body)}
        pending=[(0,0)];visited=set();return_paths=set();panic_paths=set();original_sites=set()
        while pending:
            index,calls=pending.pop()
            if (index,calls) in visited:continue
            assert index<len(body),(name,'fell off function')
            visited.add((index,calls));address,op,args=body[index]
            target=re.search(r'\b([0-9a-f]+) <([^>]+)>',args)
            original=target and target[2] in leafnames
            panic=target and ('standalone_panic' in target[2] or target[2].startswith('__stack_chk_fail'))
            if op.startswith('call'):
                if panic:panic_paths.add(address);continue
                if original:calls+=1;original_sites.add(address)
                assert calls<=1,(name,'multiple original calls')
                pending.append((index+1,calls))
            elif op in ('ret','retq'):
                assert calls==1,(name,'return bypasses original helper',hex(address));return_paths.add(address)
            elif op.startswith('j'):
                assert target,(name,'indirect jump',args)
                target_address=int(target[1],16)
                if original:
                    assert op=='jmp' and calls==0,(name,'bad original tail call');original_sites.add(address);return_paths.add(address)
                elif panic:panic_paths.add(address)
                else:
                    assert target_address in addresses,(name,'jump leaves inspected function',args)
                    pending.append((addresses[target_address],calls))
                if op!='jmp':pending.append((index+1,calls))
            else:pending.append((index+1,calls))
        assert return_paths and original_sites,name
        reports.append(dict(symbol=name,original_call_sites=[hex(a) for a in sorted(original_sites)],
                            normal_exit_sites=[hex(a) for a in sorted(return_paths)],
                            assertion_exit_sites=len(panic_paths),normal_paths_exactly_one_original_call=True))
    assert reports,'Shadow leaf wrapper missing'
    return reports

def validate(builds):
    products=generate.generate()
    for name,content in products.items():assert (HERE/name).read_text()==content,name
    original=(HERE.parent/'current/src/zset_btree.c').read_text()
    instrumented=products['generated/zset_btree.c'];harness=products['generated/census.c']
    assert apply_patch(original,products['instrumentation.patch'])==instrumented
    allowed=('zbtIndexSetId','zbtIndexHomeMayContain','zbtIndexTableAlloc','zbtIndexTableRelease',
             'zbtIndexTableInsertRaw','zbtIndexTableFind','zbtIndexCopyLeaf','zbtIndexRehashStep',
             'zbtIndexDupTable','zbtDefragPlainAllocation','zbtreeDefragStart','zbtIndexRebuild','zbtIndexScanSlot')
    stripped=[]
    for text in (original,instrumented):
        text=text.replace('#include "../shadow.h"\n\n','')
        spans=[function_region(text,n) for n in allowed]
        for start,end in sorted(spans,reverse=True):text=text[:start]+'FUNCTION'+text[end:]
        stripped.append(text)
    assert stripped[0]==stripped[1],'Mutation outside allowed hook functions'
    a,b=function_region(original,'zbtScoreLeafFindMember');x,y=function_region(instrumented,'zbtScoreLeafFindMember')
    assert original[a:b]==instrumented[x:y],'Original leaf body changed'
    lookup=(HERE.parent/'lookup.c').read_text()
    fixture=lookup[lookup.index('static zbtreeSet *fixture'):lookup.index('__attribute__((noinline))')]
    setup=lookup[lookup.index('    sds members[N],miss[N];'):lookup.index('    size_t bytes=zbtreeAllocSize(target);')]
    assert fixture in harness and setup in harness
    assert harness.index('lookup_loop(target,query,len,1000')<harness.index('shCountStart();')<harness.index('shCountEnd();')
    assert harness.index('shCountEnd();')<harness.index('size_t owned_after=')<harness.index('zbtreeIterator final;')
    assert harness.index('zbtreeFree(source);zbtreeFree(target);')<harness.index('shCompletion();')<harness.index('printf(')
    assert harness.index('sdsfree(miss[i]);')<harness.index('shCompletion();')
    assert not re.search(r'\b(clock_gettime|clock|time|gettimeofday|syscall)\s*\(',harness)
    assert 'elapsed' not in harness
    hooks=(HERE/'shadow.h').read_text()
    assert hooks.count('zbtScoreLeafFindMember(')==1
    assert 'shPredicate(leaf,physical,hint->hash,hint->bytes,hint->len)' in hooks
    assert 'shPredicate(leaf,physical,hash,ele,elelen)' in hooks
    assert hooks.index('zbtExternalHash(record)!=hash')<hooks.index('const unsigned char *current=zbtPackedData')
    assert 'physical<leaf->n.count && physical<96' in hooks and 'hint->code-1U>=leaf->n.count' in hooks
    assert 'serverAssert(newptr && !shFind((uintptr_t)newptr))' in hooks
    assert 'shInc(&sh_generation)' in hooks and 'serverAssert(*v<UINT64_MAX)' in hooks
    assert instrumented.count('shSeedBegin(')==2 and instrumented.count('shSeedEnd(')==2
    assert 'PhysicalPos(leaf,i),hash,1)' in instrumented and 'PhysicalPos(leaf,i),hash,2)' in instrumented
    deny=re.findall(r'^DENY\((\w+)\)',(HERE/'deny_clock.c').read_text(),re.M)
    result=[]
    for raw in builds:
        p=Path(raw);symbols=(p/'symbols.txt').read_text();undefined=(p/'undefined.txt').read_text()
        for name in deny:
            assert re.search(r'\b__wrap_'+name+r'$',symbols,re.M),name
            assert not re.search(r'\b'+name+r'(?:@\S*)?$',undefined,re.M),name
        result.append(dict(mode=p.name,elf_sha256=digest(p/'census'),
            compiler=(p/'compiler.txt').read_text().splitlines()[0],denied_clock_symbols=len(deny),
            call_control_flow=prove_original_call((p/'assembly.txt').read_text())))
    return dict(passed=True,diagnostic_executions=0,source_scope=list(allowed),original_leaf_body_unchanged=True,
                original_fixture_setup_exact=True,post_original_free_completion_fence=True,
                outputs_after_completion_only=True,builds=result)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('builds',nargs='*');a=p.parse_args()
    print(json.dumps(validate(a.builds),indent=2))
