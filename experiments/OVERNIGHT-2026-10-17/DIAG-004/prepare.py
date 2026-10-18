from pathlib import Path
import shutil,json,hashlib,difflib
P=Path(__file__).resolve().parent;ROOT=P.parents[2];B=ROOT/'scratch/overnight-diag-004/base'
F=json.loads((P.parent/'HARNESS-001/freeze.json').read_text())
assert not B.exists();B.mkdir(parents=True)
for name,digest in F['files'].items():
 src=ROOT/F['snapshot']/name;assert hashlib.sha256(src.read_bytes()).hexdigest()==digest
 dst=B/name;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
original=(B/'bench/microbench.c').read_text();new=original
changes=[
 ('    const char *selected = "all";','    const char *selected = "all";\n    const char *fixture_order = "shuffled";'),
 ('        else if (!strcmp(arg, "--case")) selected = value;','        else if (!strcmp(arg, "--case")) selected = value;\n        else if (!strcmp(arg, "--fixture-order")) fixture_order = value;'),
 ('    uint64_t rng = seed;','    serverAssert(!strcmp(selected,"lookup-hit"));\n    serverAssert(!strcmp(fixture_order,"ascending") || !strcmp(fixture_order,"shuffled"));\n    uint64_t rng = seed;'),
 ('if (c != 0) for (size_t i = 0; i < n; i++) insert(tree, keys[order[i]], (double)order[i]);','''if (c != 0) for (size_t i = 0; i < n; i++) {
            size_t id = !strcmp(fixture_order,"ascending") ? i : order[i];
            insert(tree, keys[id], (double)id);
        }
        size_t leaf_count=0,leaf_min=n,leaf_max=0,leaf_items=0,observed=0;
        void *previous=NULL;zbtreeIterator observation;
        zbtreeIteratorStart(tree,0,&observation);
        while (observation.leaf) {
            if (observation.leaf != previous) {
                if (previous) {if(leaf_items<leaf_min)leaf_min=leaf_items;if(leaf_items>leaf_max)leaf_max=leaf_items;}
                previous=observation.leaf;leaf_count++;leaf_items=0;
            }
            serverAssert(zbtreeIteratorNext(&observation,0,NULL,NULL,NULL));leaf_items++;observed++;
        }
        if(leaf_items<leaf_min)leaf_min=leaf_items;if(leaf_items>leaf_max)leaf_max=leaf_items;
        serverAssert(observed==n && leaf_count>0);'''),
 ('qos_effective,traversals,warmup_passes,warmup_elapsed_ns");','qos_effective,traversals,warmup_passes,warmup_elapsed_ns,fixture_order,leaf_count,leaf_min,leaf_max");'),
 ('unknown,%zu,%zu,%" PRIu64 "\\n",','unknown,%zu,%zu,%" PRIu64 ",%s,%zu,%zu,%zu\\n",'),
 ('traversals, c == 0 ? 0 : warmup_passes, warmup_elapsed);','traversals, c == 0 ? 0 : warmup_passes, warmup_elapsed, fixture_order, leaf_count, leaf_min, leaf_max);')]
for old,replacement in changes:
 assert new.count(old)==1,old;new=new.replace(old,replacement)
(B/'bench/microbench.c').write_text(new)
(P/'diagnostic-harness.patch').write_text(''.join(difflib.unified_diff(original.splitlines(True),new.splitlines(True),fromfile='a/bench/microbench.c',tofile='b/bench/microbench.c')))
freeze={'base_commit':F['base_commit'],'snapshot':str(B.relative_to(ROOT)),'provenance':'uncommitted diagnostic harness over frozen HARNESS-001; root source/referee untouched','files':{str(f.relative_to(B)):hashlib.sha256(f.read_bytes()).hexdigest() for f in B.rglob('*') if f.is_file()}}
(P/'freeze.json').write_text(json.dumps(freeze,indent=2)+'\n')
