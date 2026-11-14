#!/usr/bin/env python3
"""Validate six saved fleet census outputs; never execute a workload."""
import argparse
import json
from pathlib import Path

CASES=('hit','score','miss','long','external','update')
COUNTERS=('bucket_visits','displaced_bucket_visits','approximate_candidates',
          'true_tag_candidates','tombstone_skips','free_reference_skips','migration_skips',
          'leaf_calls','leaf_successes','leaf_failures','distinct_failed_leaves',
          'repeat_failed_all','repeat_failed_consecutive','repeat_failed_cross_bucket',
          'leaf_entries_present','repeat_leaf_entries_present','home_hit','filter_evaluated',
          'filter_true','filter_false','home_postfilter_fallback')


def require(condition,message):
    if not condition:raise ValueError(message)


def check(row):
    case=row['case'];require(case in CASES,'Unknown case')
    require(row.get('verified') is True and row.get('untimed') is True and
            type(row.get('revision')) is int and row['revision']==0,'Bad identity')
    require(not any('elapsed' in k or k.endswith('_ns') for k in row),'Timing field forbidden')
    sweeps=2 if case=='update' else 1;queries=500*sweeps
    want=dict(seed=17,members=500,warmup_sweeps=1000,sweeps=sweeps,ops=queries,
              hits=0 if case=='miss' else queries,score_sum=125250 if case=='score' else 0,
              query_count=queries)
    for key,value in want.items():
        require(type(row.get(key)) is int and row[key]==value,'Bad model '+key)
    for key in ('owned_bytes_before','owned_bytes_after','owned_bytes_after_validation'):
        require(type(row.get(key)) is int and row[key]>0,'Bad memory')
    require(row['owned_bytes_before']==row['owned_bytes_after'],'Immediate memory changed')
    for key in ('active_resize_before','active_resize_after'):
        require(type(row.get(key)) is int and row[key] in (0,1),'Bad resize endpoint')
    states=row['query_resize'];require(len(states)==queries,'Missing query states')
    for state in states:require(len(state)==2 and all(type(x) is int and x in (0,1) for x in state),'Bad query state')
    require(states[0][0]==row['active_resize_before'] and states[-1][1]==row['active_resize_after'],'Endpoint/state mismatch')
    require(all(states[i][1]==states[i+1][0] for i in range(queries-1)),'Discontinuous query states')
    calls=row['table_calls'];require(type(row['table_call_count']) is int and
                                   len(calls)==row['table_call_count'] and 0<len(calls)<=4096,'Missing/excess calls')
    totals={k:0 for k in COUNTERS};results=[0]*queries;seen=[0]*queries;previous=-1
    for index,c in enumerate(calls):
        require(c['call']==index and type(c['call']) is int,'Call order')
        q=c['query'];require(type(q) is int and previous<=q<queries,'Query order');previous=q
        require(c['query']>=0,'Negative query');seen[q]+=1
        for key in ('result','active_resize','destination_table','wide_ids'):
            require(type(c[key]) is int and c[key] in (0,1),'Bad call flag')
        require(not c['destination_table'] or c['active_resize'],'Destination without resize')
        require(type(c['table_buckets']) is int and c['table_buckets']>=0,'Bad table size')
        for key in COUNTERS:
            require(type(c[key]) is int and c[key]>=0,'Invalid counter '+key);totals[key]+=c[key]
        require(c['leaf_calls']==c['leaf_successes']+c['leaf_failures'],'Leaf partition')
        require(c['leaf_successes']==c['result'],'Result/success mismatch');results[q]+=c['result']
        require(c['distinct_failed_leaves']+c['repeat_failed_all']==c['leaf_failures'],'Failure partition')
        require(c['repeat_failed_consecutive']<=c['repeat_failed_all'] and
                c['repeat_failed_cross_bucket']<=c['repeat_failed_all'],'Invalid repeat subset')
        require(c['true_tag_candidates']<=c['approximate_candidates'],'Tag partition')
        require(c['true_tag_candidates']==sum(c[k] for k in
                ('tombstone_skips','free_reference_skips','migration_skips','leaf_calls')),'Eligibility partition')
        require(c['filter_evaluated']==c['filter_true']+c['filter_false'] and
                c['home_postfilter_fallback']==c['filter_true'],'Filter partition')
        require(c['home_hit']+c['filter_evaluated']==int(c['table_buckets']!=0),'Home partition')
        require(c['home_hit']<=c['result'] and c['filter_evaluated']<=1,'Invalid home hit')
        require(c['bucket_visits']<=c['table_buckets'] and
                c['displaced_bucket_visits']==max(c['bucket_visits']-1,0),'Bucket partition')
        require(c['repeat_leaf_entries_present']<=c['leaf_entries_present'],'Entry exposure')
    require(all(n>0 for n in seen),'Query missing a table call')
    require(all(r==(0 if case=='miss' else 1) for r in results),'Per-query result mismatch')
    require(type(row['totals']) is dict and set(row['totals'])==set(COUNTERS) and
            all(type(x) is int for x in row['totals'].values()) and row['totals']==totals,'Totals mismatch')
    return totals


def check_all(data):
    require(len(data)==6 and {r['case'] for r in data}==set(CASES),'Require all six fixed cases')
    checked={r['case']:check(r) for r in data}
    return dict(verified=True,untimed=True,cases=6,
                primary_repeat_failed_all=checked['hit']['repeat_failed_all'],
                negative_cache_primary_opportunity=(checked['hit']['repeat_failed_all']!=0),
                no_speed_prediction=True,
                counts={c:{k:checked[c][k] for k in ('home_hit','filter_evaluated','filter_false',
                    'home_postfilter_fallback','displaced_bucket_visits','leaf_calls','leaf_failures',
                    'repeat_failed_all','repeat_failed_consecutive','repeat_failed_cross_bucket')} for c in CASES})


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('outputs',nargs='+');args=p.parse_args()
    print(json.dumps(check_all([json.loads(Path(f).read_text()) for f in args.outputs]),indent=2))
