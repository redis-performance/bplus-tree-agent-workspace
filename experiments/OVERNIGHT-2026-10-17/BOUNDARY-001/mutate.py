#!/usr/bin/env python3
"""Test-only intentional faults in isolated scratch sources; never candidates."""
from pathlib import Path
import difflib,hashlib,json,subprocess
ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
source=(ROOT/'src/zset_btree.c').read_text()
mutations=[
 ('signed-zero','    return zbtOrderedToScore(ordered);','    double broken = zbtOrderedToScore(ordered);\n    return broken == 0.0 ? 0.0 : broken;'),
 ('binary-nul','    uint32_t hash = (uint32_t)dictGenHashFunction(ele, elelen);\n    return zbtIndexFind(zs, hash, ele, elelen, score,','    elelen = strlen((const char *)ele);\n    uint32_t hash = (uint32_t)dictGenHashFunction(ele, elelen);\n    return zbtIndexFind(zs, hash, ele, elelen, score,'),
 ('rank-offset','    return reverse ? zs->length - rank - 1 : rank;','    return reverse ? zs->length - rank - 1 : rank + 1;'),
 ('scan-omission','        fn(privdata, ele, len, zbtScoreLeafScore(leaf, positions[i]));','        if (len != 320) fn(privdata, ele, len, zbtScoreLeafScore(leaf, positions[i]));')]
for name,old,new in mutations:
    assert source.count(old)==1,name
    scratch=ROOT/'scratch/overnight-boundary-001'/name;scratch.mkdir()
    out=HERE/'mutations'/name;out.mkdir(parents=True)
    modified=source.replace(old,new)
    path=scratch/'zset_btree.c';path.write_text(modified)
    (out/'fault.patch').write_text(''.join(difflib.unified_diff(source.splitlines(True),modified.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c')))
    binary=scratch/'oracle'
    command=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer','-DREDIS_DEBUG','-O3','tests/boundary_oracle.c',str(path.relative_to(ROOT)),'compat/standalone.c','vendor/redis/siphash.c','-lm','-o',str(binary.relative_to(ROOT))]
    with (out/'build.stdout').open('w') as stdout,(out/'build.stderr').open('w') as stderr:
        p=subprocess.run(command,cwd=ROOT,stdout=stdout,stderr=stderr,timeout=120)
    manifest={'build_command':command,'build_returncode':p.returncode,'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
    if p.returncode==0:
        with (out/'run.stdout').open('w') as stdout,(out/'run.stderr').open('w') as stderr:
            try:
                p=subprocess.run([str(binary)],cwd=ROOT,stdout=stdout,stderr=stderr,timeout=120)
                rc=p.returncode
            except subprocess.TimeoutExpired: rc='timeout'
        manifest.update(run_command=[str(binary.relative_to(ROOT))],run_returncode=rc,binary_sha256=hashlib.sha256(binary.read_bytes()).hexdigest())
    (out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(name,manifest,flush=True)
