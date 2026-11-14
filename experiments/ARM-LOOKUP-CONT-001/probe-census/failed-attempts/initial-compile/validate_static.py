#!/usr/bin/env python3
"""Pure source and saved-ELF metadata checks; never run diagnostic code."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('generator',HERE/'generate.py')
g=importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)


def apply_patch(original,patch):
    old=original.splitlines(True);out=[];cursor=0;lines=patch.splitlines(True);i=0
    while i<len(lines):
        match=re.match(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@',lines[i])
        if not match:i+=1;continue
        start=int(match[1])-1
        assert start>=cursor
        out+=old[cursor:start];cursor=start;i+=1
        while i<len(lines) and not lines[i].startswith(('@@','diff --git')):
            line=lines[i];i+=1
            assert line[0] in ' +-'
            if line[0] in ' -':assert old[cursor]==line[1:];cursor+=1
            if line[0] in ' +':out.append(line[1:])
    out+=old[cursor:]
    return ''.join(out)


def validate(builds):
    products=g.generate()
    for path,content in products.items():assert (HERE/path).read_text()==content
    original=(HERE.parent/'current/src/zset_btree.c').read_text()
    instrumented=products['generated/zset_btree.c'];harness=products['generated/census.c']
    assert apply_patch(original,products['instrumentation.patch'])==instrumented
    # Exact original fixture and query setup are embedded in the generated file.
    lookup=(HERE.parent/'lookup.c').read_text()
    fixture=lookup[lookup.index('static zbtreeSet *fixture'):lookup.index('__attribute__((noinline))')]
    setup=lookup[lookup.index('    sds members[N],miss[N];'):lookup.index('    size_t bytes=zbtreeAllocSize(target);')]
    assert fixture in harness and setup in harness
    assert not re.search(r'\b(clock_gettime|clock|time|gettimeofday|timespec_get|syscall)\s*\(',harness)
    assert 'elapsed' not in harness
    assert harness.index('hits=lookup_loop(target,query,len,1000')<harness.index('censusReset();')<harness.index('census_enabled=1;')
    assert harness.index('census_enabled=0;')<harness.index('size_t owned_after=')<harness.index('zbtreeIterator final;')
    assert 'unsigned seed=17;' in harness and 'uint64_t sweeps=updating ? 2:1;' in harness
    assert 'censusLeaf(census, leaf, hash, ele, elelen, score,' in instrumented
    hooks=(HERE/'instrumentation.h').read_text()
    assert hooks.count('zbtScoreLeafFindMember(leaf,hash,ele,elelen,score,position)')==2
    assert hooks.index('int result=zbtScoreLeafFindMember(')<hooks.index('if (repeat) {')
    assert 'serverAssert(!result);' in hooks
    assert 'memcmp(score_before,score,sizeof(score_before))==0' in hooks
    assert 'memcmp(position_before,position,sizeof(position_before))==0' in hooks
    assert 'census_failed_count=0;census_has_last_failed=0;' in hooks
    assert 'census_failed[census_failed_count++]=(censusFailed){leaf->id,bucket};' in hooks
    assert 'return censusEnd(census,0);' in instrumented
    # The original finder remains byte-identical outside its isolated region.
    start=original.index('static inline __attribute__((always_inline))\nint zbtIndexTableFind(')
    end=original.index('\n/* Find an entry whose leaf number',start)
    assert instrumented.startswith(original[:start]) and instrumented.endswith(original[end:])
    denied=re.findall(r'^DENY\((\w+)\)',(HERE/'deny_clock.c').read_text(),re.M)
    build_results=[]
    for build in builds:
        path=Path(build);symbols=(path/'symbols.txt').read_text();undefined=(path/'undefined.txt').read_text()
        for name in denied:
            assert re.search(r'\b__wrap_'+name+r'$',symbols,re.M),name
            assert not re.search(r'\b'+name+r'(?:@\S*)?$',undefined,re.M),name
        build_results.append(dict(mode=path.name,elf_sha256=hashlib.sha256((path/'census').read_bytes()).hexdigest(),
                                  compiler=(path/'compiler.txt').read_text().splitlines()[0],clock_wrappers=len(denied)))
    return dict(passed=True,source_patch_reconstructs=True,original_fixture_and_setup_exact=True,
                counters_after_warmup_only=True,immediate_memory_before_validation=True,
                original_leaf_call_always_executed=True,clock_api_wrappers=len(denied),
                diagnostic_executions=0,builds=build_results)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('builds',nargs='*')
    args=parser.parse_args()
    print(json.dumps(validate(args.builds),indent=2))
