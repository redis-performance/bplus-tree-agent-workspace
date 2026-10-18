from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parent;R=P.parents[2];M=json.loads((P/'manifest.json').read_text());rows=[]
for c in M['captures']:
 if not c['variant'].startswith('C-'):continue
 p=R/c['counts'];assert hashlib.sha256(p.read_bytes()).hexdigest()==c['counts_sha256'];fs=json.loads(p.read_text());f=next(f for f in fs if f['name']=='zbtInlineTagSearch');b=f['branches'];assert len(b)==7
 assert [x['source'].strip() for x in b]==['while (n >= 16) {','if (matches) return p + (__builtin_ctzll(matches) >> 3);','if (matches) return p + (__builtin_ctzll(matches) >> 3);','if (n >= 8) {','if (matches) return p + (__builtin_ctzll(matches) >> 3);','while (n--) { if (*p == tag) return p; p++; }','while (n--) { if (*p == tag) return p; p++; }']
 # Each logical word examination enters one corresponding matches condition.
 first=b[1]['true']+b[1]['false'];second=b[2]['true']+b[2]['false'];tail=b[4]['true']+b[4]['false'];scalar=b[6]['true']+b[6]['false'];returns=sum(b[i]['true'] for i in [1,2,4,6]);miss=b[5]['false']
 assert first==b[0]['true'] and second==b[1]['false'] and tail==b[3]['true'] and scalar==b[5]['true'];assert returns+miss==f['count'];assert b[0]['false']==b[3]['true']+b[3]['false']
 leaf=next(f for f in fs if f['name']=='zbtScoreLeafFindMember')['count'];row=dict(seed=c['seed'],variant=c['variant'],batch=c['batch'],leaf_calls=leaf,helper_calls=f['count'],first_word_examinations=first,second_word_examinations=second,tail_word_examinations=tail,scalar_tag_tests=scalar,first_returns=b[1]['true'],second_returns=b[2]['true'],tail_returns=b[4]['true'],scalar_returns=b[6]['true'],no_match_returns=miss,total_word_examinations=first+second+tail,non_null_returns=returns,extra_helper_calls=f['count']-leaf);rows.append(row)
for seed in [83103,83111]:
 rs=[{k:v for k,v in r.items() if k not in ['variant','batch']} for r in rows if r['seed']==seed];assert len(rs)==4 and all(r==rs[0] for r in rs)
(P/'helper-census.json').write_text(json.dumps(dict(scope='post-hoc descriptive arithmetic on existing scoped counters; no new capture, timing, or decision criterion',rows=rows,conservation_checks='PASS'),indent=2)+'\n')
for seed in [83103,83111]:print(next(r for r in rows if r['seed']==seed))
