#!/usr/bin/env python3
"""Verify source and optionally saved native ELF; never execute it."""
import argparse,hashlib,json,re,sys,importlib.util
from pathlib import Path
HERE=Path(__file__).resolve().parent
EXP=HERE.parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def validate(build=None):
    dependencies=json.loads((HERE/'DEPENDENCIES.json').read_text())
    for name,value in dependencies.items():assert sha(EXP/name)==value,name
    old=EXP/'slot-hint-census'
    assert sha(old/'SHA256SUMS')=='f2f8f882de6d48a6207ffff86f9af5fae53461ff0593e9e06bcc39c4fa82849b'
    for line in (old/'SHA256SUMS').read_text().splitlines():
        digest,name=line.split(None,1);assert sha(old/name)==digest,name
    for name in ('generated/zset_btree.c','shadow.h','deny_clock.c'):
        assert (HERE/name).read_bytes()==(old/name).read_bytes(),name
    source=(HERE/'lifecycle.c').read_text()
    assert 'shCountStart();' not in source and 'sh_phase=SH_COUNT' not in source
    assert source.index('sdsfree(lc_members[i]);')<source.index('shCompletion();')<source.index('    printf("{\\"diagnostic')
    assert source.index('rank>=512 && rank<=1536')<source.index('zbtreeDeleteRangeByRank(original,512,1536)')
    assert 'lcFingerprint' not in source and 'memcmp(lc_saved_hints' in source
    assert not re.search(r'\b(clock_gettime|clock|gettimeofday|time|syscall)\s*\(',source)
    result=dict(passed=True,diagnostic_executions=0,frozen_93_files_unchanged=True,source_sha256=sha(HERE/'lifecycle.c'),completion_after_original_frees=True)
    if build:
        p=Path(build);root=EXP.parent.parent
        for line in (p/'SHA256SUMS').read_text().splitlines():
            value,name=line.split(None,1);assert sha(root/name)==value,name
        sys.path.insert(0,str(old))
        spec=importlib.util.spec_from_file_location('frozen_static',old/'validate_static.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
        assembly=(p/'assembly.txt').read_text();functions=mod.disassembly_functions(assembly)
        symbols=(p/'symbols.txt').read_text();undefined=(p/'undefined.txt').read_text()
        denied=re.findall(r'^DENY\((\w+)\)',(HERE/'deny_clock.c').read_text(),re.M)
        for name in denied:
            assert re.search(r'\b__wrap_'+name+r'$',symbols,re.M),name
            assert not re.search(r'\b'+name+r'(?:@\S*)?$',undefined,re.M),name
            body=functions['__wrap_'+name]
            assert any(op.startswith('call') and '<write@plt>' in args for _,op,args in body)
            assert any(op.startswith('call') and '<_exit@plt>' in args for _,op,args in body)
        result.update(elf_sha256=sha(p/'lifecycle'),assembly_sha256=sha(p/'assembly.txt'),
            receipt_sha256=sha(p/'SHA256SUMS'),clock_denials=len(denied),original_call_cfg=mod.prove_original_call(assembly))
    return result
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('build',nargs='?');args=p.parse_args();print(json.dumps(validate(args.build),indent=2))
