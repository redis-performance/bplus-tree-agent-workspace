from pathlib import Path
import shutil,json,hashlib,difflib
P=Path(__file__).resolve().parent;R=P.parents[2];B=R/'scratch/overnight-diag-005/base'
F=json.loads((P.parent/'DIAG-004/freeze.json').read_text())
assert not B.exists();B.mkdir(parents=True)
for name,h in F['files'].items():
 src=R/F['snapshot']/name;assert hashlib.sha256(src.read_bytes()).hexdigest()==h
 dst=B/name;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
original=(B/'bench/microbench.c').read_text();new=original
changes=[
 ('    const char *fixture_order = "shuffled";','    const char *fixture_order = "shuffled";\n    const char *query_order = "coupled";'),
 ('        else if (!strcmp(arg, "--fixture-order")) fixture_order = value;','        else if (!strcmp(arg, "--fixture-order")) fixture_order = value;\n        else if (!strcmp(arg, "--query-order")) query_order = value;'),
 ('    uint64_t rng = seed;','    serverAssert(!strcmp(query_order,"coupled") || !strcmp(query_order,"independent"));\n    uint64_t rng = seed;'),
 ('    size_t *order = zmalloc(n * sizeof(*order));','    size_t *order = zmalloc(n * sizeof(*order));\n    size_t *query = zmalloc(n * sizeof(*query));'),
 ('    puts("case,size,requested_ops,', '''    memcpy(query,order,n*sizeof(*query));
    uint64_t query_rng=seed ^ UINT64_C(0xa0761d6478bd642f);
    if(!strcmp(query_order,"independent")) for(size_t i=n;i>1;i--){
        size_t j=random64(&query_rng)%i,t=query[i-1];query[i-1]=query[j];query[j]=t;
    }
    uint64_t query_fingerprint=UINT64_C(14695981039346656037);
    for(size_t i=0;i<n;i++)query_fingerprint=(query_fingerprint^query[i])*UINT64_C(1099511628211);
    puts("case,size,requested_ops,'''),
 ('keys[order[i]], &score) && score == (double)order[i]','keys[query[i]], &score) && score == (double)query[i]'),
 ('leaf_min,leaf_max");','leaf_min,leaf_max,query_order,query_fingerprint");'),
 ('%s,%zu,%zu,%zu\\n",','%s,%zu,%zu,%zu,%s,%" PRIu64 "\\n",'),
 ('warmup_elapsed, fixture_order, leaf_count, leaf_min, leaf_max);','warmup_elapsed, fixture_order, leaf_count, leaf_min, leaf_max, query_order, query_fingerprint);'),
 ('    zfree(keys); zfree(order);','    zfree(keys); zfree(order); zfree(query);')]
for old,replacement in changes:
 assert new.count(old)==1,old;new=new.replace(old,replacement)
assert new.count('order[i % n]')==4
new=new.replace('order[i % n]','query[i % n]')
(B/'bench/microbench.c').write_text(new)
(P/'diagnostic-harness.patch').write_text(''.join(difflib.unified_diff(original.splitlines(True),new.splitlines(True),fromfile='a/bench/microbench.c',tofile='b/bench/microbench.c')))
freeze={'base_commit':F['base_commit'],'parent_freeze_sha256':hashlib.sha256((P.parent/'DIAG-004/freeze.json').read_bytes()).hexdigest(),'snapshot':str(B.relative_to(R)),'provenance':'uncommitted diagnostic extension over DIAG-004; root source/referee untouched','files':{str(f.relative_to(B)):hashlib.sha256(f.read_bytes()).hexdigest() for f in B.rglob('*') if f.is_file()}}
(P/'freeze.json').write_text(json.dumps(freeze,indent=2)+'\n')
