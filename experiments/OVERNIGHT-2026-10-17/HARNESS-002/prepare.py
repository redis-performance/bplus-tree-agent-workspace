from pathlib import Path
import hashlib,json,shutil,difflib
from datetime import datetime,timezone
P=Path(__file__).resolve().parent; R=P.parents[2]; B=R/'scratch/overnight-harness-002/base'
F=json.loads((P.parent/'HARNESS-001/freeze.json').read_text());assert not B.exists();B.mkdir(parents=True)
for name,h in F['files'].items():
 src=R/F['snapshot']/name;assert hashlib.sha256(src.read_bytes()).hexdigest()==h
 dst=B/name;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
original=(B/'bench/microbench.c').read_text();s=original
changes=[
('    uint64_t seed = 1;', '    uint64_t seed = 1, query_seed = 2;\n    const char *query_order = "coupled";'),
('[--warmup-passes N>=1]', '[--warmup-passes N>=1] [--query-order coupled|independent] [--query-seed N]'),
('        else if (!strcmp(arg, "--seed")) seed = number(value);','        else if (!strcmp(arg, "--seed")) seed = number(value);\n        else if (!strcmp(arg, "--query-seed")) query_seed = number(value);\n        else if (!strcmp(arg, "--query-order")) query_order = value;'),
('    uint64_t rng = seed;', '''    if (strcmp(query_order, "coupled") && strcmp(query_order, "independent")) {
        fputs("Invalid query order (coupled|independent)\\n", stderr); return 2;
    }
    uint64_t rng = seed;'''),
('    size_t *order = zmalloc(n * sizeof(*order));','    size_t *order = zmalloc(n * sizeof(*order));\n    size_t *query = zmalloc(n * sizeof(*query));'),
('    puts("case,size,requested_ops,','''    /* Independent queries start from identity and their own PRNG state: neither
     * hash-seed draws nor insertion shuffle affect this permutation. Both modes
     * allocate/touch the same arrays. Coupled mode preserves historical order. */
    for (size_t i = 0; i < n; i++) query[i] = !strcmp(query_order, "coupled") ? order[i] : i;
    uint64_t query_rng = query_seed;
    if (!strcmp(query_order, "independent")) for (size_t i = n; i > 1; i--) {
        size_t j = random64(&query_rng) % i, tmp = query[i-1];
        query[i-1] = query[j]; query[j] = tmp;
    }
    uint64_t construction_fingerprint = UINT64_C(14695981039346656037);
    uint64_t query_fingerprint = UINT64_C(14695981039346656037);
    for (size_t i = 0; i < n; i++) {
        construction_fingerprint = (construction_fingerprint ^ order[i]) * UINT64_C(1099511628211);
        query_fingerprint = (query_fingerprint ^ query[i]) * UINT64_C(1099511628211);
    }
    puts("case,size,requested_ops,'''),
('warmup_elapsed_ns");','warmup_elapsed_ns,construction_order,construction_fingerprint,query_order,query_seed,query_fingerprint");'),
('keys[order[i]], &score) && score == (double)order[i]','keys[query[i]], &score) && score == (double)query[i]'),
('checksum += zbtreeDelete(tree, keys[order[i]])','checksum += zbtreeDelete(tree, keys[query[i]])'),
('serverAssert(zbtreeScore(tree, keys[order[i]], &score));','serverAssert(zbtreeScore(tree, keys[query[i]], &score));'),
('serverAssert(score == (double)order[i] + (double)(repeats * n));','serverAssert(score == (double)query[i] + (double)(repeats * n));'),
('unknown,%zu,%zu,%" PRIu64 "\\n",','unknown,%zu,%zu,%" PRIu64 ",shuffled,%" PRIu64 ",%s,%" PRIu64 ",%" PRIu64 "\\n",'),
('traversals, c == 0 ? 0 : warmup_passes, warmup_elapsed);','traversals, c == 0 ? 0 : warmup_passes, warmup_elapsed,\n               construction_fingerprint, query_order, query_seed, query_fingerprint);'),
('zfree(keys); zfree(order);','zfree(keys); zfree(order); zfree(query);')]
for a,b in changes:
 assert s.count(a)==1,a;s=s.replace(a,b)
assert s.count('order[i % n]')==4;s=s.replace('order[i % n]','query[i % n]')
(B/'bench/microbench.c').write_text(s)
(P/'harness.patch').write_text(''.join(difflib.unified_diff(original.splitlines(True),s.splitlines(True),fromfile='a/bench/microbench.c',tofile='b/bench/microbench.c')))
freeze=dict(base_commit=F['base_commit'],snapshot=str(B.relative_to(R)),frozen_utc=datetime.now(timezone.utc).isoformat(),parent_freeze_sha256=hashlib.sha256((P.parent/'HARNESS-001/freeze.json').read_bytes()).hexdigest(),provenance='uncommitted isolated HARNESS-002 over HARNESS-001; protected git not retried; root source/referee unchanged',files={str(f.relative_to(B)):hashlib.sha256(f.read_bytes()).hexdigest() for f in B.rglob('*') if f.is_file()})
(P/'freeze.json').write_text(json.dumps(freeze,indent=2)+'\n')
