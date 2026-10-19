from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parent
s=Path('src/zset_btree.c').read_text();a=s.index('static int zbtScoreUpdateInPlace(');b=s.index('/* Record the page share',a);fn=s[a:b]
fn=fn.replace('{\n    zbtScoreLeaf *neighbor','{\n    update_calls++;\n    zbtScoreLeaf *neighbor',1)
fn=fn.replace('return 0;','{ update_order_fail++; return 0; }')
fn=fn.replace('if (!zbtScoreLeafPackScore(leaf, score, &delta)) { update_order_fail++; return 0; }','if (!zbtScoreLeafPackScore(leaf, score, &delta)) { update_pack_fail++; return 0; }')
fn=fn.replace('    return 1;','    update_success++;\n    return 1;')
s=s[:a]+'unsigned long long update_calls, update_success, update_order_fail, update_pack_fail;\n'+fn+s[b:]
D=Path('scratch/intel-update-census');D.mkdir(exist_ok=True);(D/'source.c').write_text(s)
h=(P/'update.c').read_text();h=h.replace('static const char *update_pattern','extern unsigned long long update_calls, update_success, update_order_fail, update_pack_fail;\nstatic const char *update_pattern')
h=h.replace('        uint64_t start = now_ns();','        update_calls=update_success=update_order_fail=update_pack_fail=0;\n        uint64_t start = now_ns();')
h=h.replace('        int64_t thread_end = thread_ns();','        printf("CENSUS,%llu,%llu,%llu,%llu\\n",update_calls,update_success,update_order_fail,update_pack_fail);\n        serverAssert(update_calls==ops && update_calls==update_success+update_order_fail+update_pack_fail);\n        int64_t thread_end = thread_ns();')
(D/'harness.c').write_text(h)
(P/'census-sha256.json').write_text(json.dumps({f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in D.glob('*.c')},indent=2)+'\n')
