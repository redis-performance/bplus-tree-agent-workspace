#!/usr/bin/env python3
"""Generate the diagnostic from exact baseline bytes; never execute it."""
import argparse
import difflib
import hashlib
import json
from pathlib import Path
from hooks import lifecycle_hooks

HERE = Path(__file__).resolve().parent
EXP = HERE.parent
SOURCE_SHA = '16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9'
LOOKUP_SHA = '1e6dc19c9b0f49abafb75c67e3434a87cc6d7d5222049c90a68368755c2a5827'


def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()


def replace_once(text, old, new):
    assert text.count(old) == 1, repr(old)
    return text.replace(old, new)


def generate():
    source = (EXP / 'current/src/zset_btree.c').read_text()
    lookup = (EXP / 'lookup.c').read_text()
    assert sha(source) == SOURCE_SHA and sha(lookup) == LOOKUP_SHA
    start = source.index('static inline __attribute__((always_inline))\nint zbtIndexTableFind(')
    end = source.index('\n/* Find an entry whose leaf number', start)
    original = source[start:end]
    body = replace_once(original, '{\n    if (table->size', '{\n    censusCall *census=censusBegin(zs,table);\n    if (table->size')
    body = replace_once(body, '        uint64_t matches =',
        '        CENSUS_INC(census,bucket_visits);\n'
        '        if (probes) CENSUS_INC(census,displaced_bucket_visits);\n'
        '        uint64_t matches =')
    body = replace_once(body, '        while (matches) {',
        '        while (matches) {\n            CENSUS_INC(census,approximate_candidates);')
    body = replace_once(body, '            uint32_t id =',
        '            CENSUS_INC(census,true_tag_candidates);\n            uint32_t id =')
    body = replace_once(body, '                if (leaf == NULL || ZBT_IS_FREE_LEAF_ID(leaf)) {',
        '                if (leaf == NULL || ZBT_IS_FREE_LEAF_ID(leaf)) {\n'
        '                    CENSUS_INC(census,free_reference_skips);')
    body = replace_once(body, '                    if (in_new != migrated) {',
        '                    if (in_new != migrated) {\n                        CENSUS_INC(census,migration_skips);')
    body = replace_once(body,
        '                if (zbtScoreLeafFindMember(leaf, hash, ele, elelen, score,\n'
        '                                           score_pos))',
        '                if (shLeaf(census, table, bucket, pos, leaf, hash, ele, elelen, score,\n'
        '                               score_pos))')
    body = replace_once(body, '                    if (score_leaf) *score_leaf = leaf;',
        '                    if (probes == 0) CENSUS_INC(census,home_hit);\n'
        '                    if (score_leaf) *score_leaf = leaf;')
    body = replace_once(body, '            }\n            matches &= matches - 1;\n        }',
        '            } else {\n                CENSUS_INC(census,tombstone_skips);\n            }\n'
        '            matches &= matches - 1;\n        }')
    body = replace_once(body, '        if (probes == 0 && !zbtIndexHomeMayContain(table, hash)) return 0;',
        '        if (probes == 0) {\n'
        '            CENSUS_INC(census,filter_evaluated);\n'
        '            int may_contain=zbtIndexHomeMayContain(table, hash);\n'
        '            if (!may_contain) {\n'
        '                CENSUS_INC(census,filter_false);\n'
        '                return 0;\n'
        '            }\n'
        '            CENSUS_INC(census,filter_true);\n'
        '            CENSUS_INC(census,home_postfilter_fallback);\n'
        '        }')
    assert body.count('return 0;') == 4 and body.count('return 1;') == 1
    body = body.replace('return 0;', 'CENSUS_RETURN(census,0);').replace('return 1;', 'CENSUS_RETURN(census,1);')
    instrumented = source[:start] + body + source[end:]
    assert source[:start] == instrumented[:start] and instrumented.endswith(source[end:])

    instrumented = lifecycle_hooks(instrumented)

    # Preserve exact fixture construction, payload bytes, query order and the
    # independent source/target buffers. Hooks only bracket existing operations.
    fixture = lookup[lookup.index('static zbtreeSet *fixture'):lookup.index('__attribute__((noinline))')]
    loop = lookup[lookup.index('__attribute__((noinline))'):lookup.index('int main(')]
    loop = replace_once(loop, '            zbtreeInsertPosition p; double score;',
        '            censusQueryBegin(t);\n            zbtreeInsertPosition p; double score=0;')
    loop = replace_once(loop, '            zbtreeUpdateScore(t,members[i],i+1+(r%2?0.0:0.125),&p);',
        '            zbtreeUpdateScore(t,members[i],i+1+(r%2?0.0:0.125),&p);\n            censusQueryEnd(t);')
    loop = replace_once(loop, '            double score=0; hits+=zbtreeScoreRaw(t,q[i],len[i],&score); sum+=score;',
        '            censusQueryBegin(t);\n'
        '            double score=0; hits+=zbtreeScoreRaw(t,q[i],len[i],&score); sum+=score;\n'
        '            censusQueryEnd(t);')
    loop = replace_once(loop, '        for(uint64_t r=0;r<sweeps;r++) for(int i=0;i<N;i++)\n'
        '            hits+=zbtreeScoreRaw(t,q[i],len[i],NULL);',
        '        for(uint64_t r=0;r<sweeps;r++) for(int i=0;i<N;i++) {\n'
        '            censusQueryBegin(t);\n'
        '            hits+=zbtreeScoreRaw(t,q[i],len[i],NULL);\n'
        '            censusQueryEnd(t);\n        }')
    setup = lookup[lookup.index('    sds members[N],miss[N];'):lookup.index('    size_t bytes=zbtreeAllocSize(target);')]
    teardown = lookup[lookup.index('    zbtreeFree(source);'):]
    teardown = teardown.replace(' return 0;\n}', '\n    shCompletion();\n'+(HERE/'print_main.c.in').read_text()+'    return 0;\n}')
    harness = ('/* Generated from pinned lookup.c; untimed census only. */\n'
        '#define _POSIX_C_SOURCE 200809L\n#include "zset_btree.c"\n#include "../emit.h"\n#include <inttypes.h>\n#define N 500\n' +
        fixture + loop + (HERE / 'main_prefix.c.in').read_text() + setup +
        (HERE / 'main_suffix.c.in').read_text() + teardown)
    patch = ''.join(difflib.unified_diff(source.splitlines(True), instrumented.splitlines(True),
        fromfile='original/zset_btree.c', tofile='generated/zset_btree.c'))
    products = {'generated/zset_btree.c': instrumented, 'generated/census.c': harness,
                'instrumentation.patch': patch}
    manifest = dict(upstream='ee8e7f70152404649ac947157fd662d11b4a00d5',
        source_sha256=SOURCE_SHA, lookup_sha256=LOOKUP_SHA, fixture_sha256=sha(fixture),
        setup_sha256=sha(setup), generated_sha256={p: sha(s) for p, s in products.items()})
    manifest['generator_inputs_sha256'] = {p: sha((HERE/p).read_text()) for p in
        ['generate.py','hooks.py','shadow.h','emit.h','main_prefix.c.in','main_suffix.c.in','print_main.c.in','deny_clock.c']}
    products['GENERATION.json'] = json.dumps(manifest,indent=2)+'\n'
    return products


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    for path, content in generate().items():
        target=HERE/path
        if args.check:
            assert target.read_text()==content, str(target)
        else:
            target.parent.mkdir(exist_ok=True)
            with target.open('x') as file: file.write(content)
    print('Static source generation verified' if args.check else 'Generated; diagnostic not executed')
