#!/usr/bin/env python3
"""Offline admission of saved slot-hint outputs; never invokes a workload."""
import argparse
import json
from pathlib import Path

CASES=('hit','score','miss','long','external','update')
MEMORY=dict(hit=14272,score=14272,miss=14272,long=146656,external=217600,update=14432)
COUNTERS=('bucket_visits','displaced_bucket_visits','approximate_candidates','true_tag_candidates',
          'tombstone_skips','free_reference_skips','migration_skips','leaf_calls','leaf_successes',
          'leaf_failures','home_hit','filter_evaluated','filter_true','filter_false','home_postfilter_fallback')

def require(condition,message):
    if not condition:raise ValueError(message)

def integer(value,low=0,high=(1<<64)-1):
    require(type(value) is int and low<=value<=high,'Integer domain')
    return value

def bit(value):return integer(value,0,1)

def no_timing(value):
    if isinstance(value,dict):
        for key,item in value.items():
            require('elapsed' not in key and not key.endswith('_ns'),'Timing forbidden')
            no_timing(item)
    elif isinstance(value,list):
        for item in value:no_timing(item)

def check(row):
    no_timing(row);case=row['case'];require(case in CASES,'Case')
    require(row['diagnostic']=='slot-hint' and type(row['revision']) is int and row['revision']==0,'Identity')
    require(row['verified'] is True and row['untimed'] is True and row['cleanup_complete'] is True,'Missing success fence')
    require(integer(row['live_generations_after_cleanup'])==0,'Live generation at completion')
    count=1000 if case=='update' else 500
    expected=dict(seed=17,members=500,warmup_sweeps=1000,sweeps=count//500,ops=count,
                  query_count=count,hits=0 if case=='miss' else count,score_sum=125250 if case=='score' else 0)
    for key,value in expected.items():require(integer(row[key])==value,'Model '+key)
    for key in ('owned_bytes_before','owned_bytes_after'):
        require(integer(row[key])==MEMORY[case],'Fixed immediate memory')
    integer(row['owned_bytes_after_validation'],1)
    states=row['query_resize'];bounds=row['query_bounds']
    require(len(states)==len(bounds)==count,'Missing query records')
    for pair in states:
        require(len(pair)==2,'Query state pair');bit(pair[0]);bit(pair[1])
    require(bit(row['active_resize_before'])==states[0][0] and bit(row['active_resize_after'])==states[-1][1],'Resize endpoints')
    require(all(states[i][1]==states[i+1][0] for i in range(count-1)),'Resize continuity')
    begin=integer(row['count_start'],1);end=integer(row['count_end'],begin+1)
    events=[]
    def add(seq,kind,data):events.append((integer(seq,1),kind,data))
    add(begin,'begin',None);add(end,'end',None)
    last=begin
    for q,pair in enumerate(bounds):
        require(len(pair)==2 and last<integer(pair[0],1)<integer(pair[1],1)<end,'Query bounds')
        add(pair[0],'qbegin',q);add(pair[1],'qend',q);last=pair[1]
    calls=row['table_calls'];require(len(calls)==integer(row['table_call_count'],1,4096),'Call count')
    bycall=[[] for _ in calls];byfilter=[[] for _ in calls];results=[0]*count;seen=[0]*count
    lastq=-1
    for i,c in enumerate(calls):
        require(integer(c['call'])==i,'Call order');q=integer(c['query'],0,count-1)
        require(q>=lastq,'Query order');lastq=q;seen[q]+=1
        for key in ('active_resize','destination_table','wide_ids','result'):bit(c[key])
        require(not c['destination_table'] or c['active_resize'],'Destination outside resize')
        require(not c['active_resize'] or states[q][0],'Resize absent at query entry')
        size=integer(c['table_buckets'],0,1024)
        for key in COUNTERS:integer(c[key])
        require(c['leaf_calls']==c['leaf_successes']+c['leaf_failures'] and c['leaf_successes']==c['result'],'Leaf partition')
        require(c['true_tag_candidates']<=c['approximate_candidates']<=8*c['bucket_visits'],'Tag capacity')
        require(c['true_tag_candidates']==sum(c[k] for k in ('tombstone_skips','free_reference_skips','migration_skips','leaf_calls')),'Eligibility partition')
        require(c['filter_evaluated']==c['filter_true']+c['filter_false'] and c['home_postfilter_fallback']==c['filter_true'],'Filter partition')
        require(c['home_hit']+c['filter_evaluated']==int(size!=0) and c['home_hit']<=c['result'],'Home partition')
        require(bool(c['bucket_visits'])==bool(size) and c['bucket_visits']<=size,'Bucket visits')
        require(c['displaced_bucket_visits']==max(0,c['bucket_visits']-1),'Displacement')
        require(not c['home_hit'] or c['bucket_visits']==1,'Home hit displaced')
        require(not c['filter_false'] or (c['result']==0 and c['bucket_visits']==1),'Successful filter rejection')
        require(not c['displaced_bucket_visits'] or c['filter_true']==1,'Displacement without filter')
        require(not c['migration_skips'] or c['active_resize'],'Migration outside resize')
        require(not c['free_reference_skips'] or (c['active_resize'] and not c['destination_table']),'Free reference state')
        if not size:require(c['generation'] is None and c['result']==0 and all(c[k]==0 for k in COUNTERS),'Empty table work')
        else:integer(c['generation'],1)
        require(bounds[q][0]<integer(c['seq'],1)<integer(c['end_seq'],1)<bounds[q][1],'Call bounds')
        add(c['seq'],'call',c);add(c['end_seq'],'callend',c);results[q]+=c['result']
    require(all(seen) and all(r==(0 if case=='miss' else 1) for r in results),'Query result')
    require(len(row['lifecycle'])<=4096 and len(row['initial_hints'])<=16*1024,'Registry bound')
    require(all(len(row[k])<=65536 for k in ('leaf_events','filter_events','mutations')),'Event bound')
    for key in ('lifecycle','mutations','leaf_events','filter_events'):
        seqs=[integer(e['seq'],1) for e in row[key]]
        require(all(a<b for a,b in zip(seqs,seqs[1:])),'Raw event order')
    for e in row['lifecycle']:add(e['seq'],'life',e)
    for e in row['mutations']:add(e['seq'],'mutation',e)
    for i,e in enumerate(row['leaf_events']):
        require(integer(e['event'])==i,'Leaf event order');add(e['seq'],'leaf',e)
    for i,e in enumerate(row['filter_events']):
        require(integer(e['event'])==i,'Filter event order');add(e['seq'],'filter',e)
    events.sort(key=lambda x:x[0]);require([e[0] for e in events]==list(range(1,len(events)+1)),'Missing/duplicate sequence')
    live={};slots={};hints={};maxgen=0;phase=0;active_query=None;active_call=None
    terminals=[0]*6;stale=[0]*3;useful=set();filters=[[0]*3 for _ in range(2)]
    mutations=dict(id_writes=0,invalidations=0,seeds=0);previous_mutation=None
    def valid_generation(e):
        g=integer(e['generation'],1);require(g in live,'Generation is not live');return g
    def qevent(e):
        require(phase==2 and integer(e['query'],0,count-1)==active_query,'Event outside query')
    for seq,kind,e in events:
        if kind=='begin':
            require(phase<=1 and live,'Bad count start');phase=2
            for hint in row['initial_hints']:
                g=valid_generation(hint);b=integer(hint['bucket'],0,live[g]['buckets']-1)
                require((g,b) not in hints,'Duplicate initial hint')
                integer(hint['code'],1,96);integer(hint['origin'],1,2);integer(hint['id'],0,(1<<32)-2)
                require(live[g]['wide_ids'] or hint['id']<65535,'Truncated narrow ID')
                hints[g,b]=(hint['code'],hint['id'],hint['origin'])
        elif kind=='end':
            require(phase==2 and active_query is None and active_call is None,'Unfinished counted context');phase=3
        elif kind=='qbegin':
            require(phase==2 and active_query is None and active_call is None,'Nested query');active_query=e
        elif kind=='qend':
            require(active_query==e and active_call is None,'Query completion');active_query=None
        elif kind=='life':
            ep=integer(e['phase'],0,4);require(ep>=phase,'Lifecycle phase reversal')
            require((ep<2 and seq<begin) or (ep==2 and begin<seq<end) or (ep>2 and seq>end),'Lifecycle phase/boundary')
            phase=ep;g=integer(e['generation'],1);op=integer(e['kind'],0,4)
            slot=integer(e['registry_slot'],0,15);size=integer(e['buckets'],1,1024);bit(e['wide_ids'])
            parent=integer(e['parent']);require(op==2 or parent==0,'Unexpected parent')
            if op in (0,2):
                require(g==maxgen+1 and slot not in slots,'Reused generation/occupied registry');maxgen=g
                if op==2:
                    require(parent in live and live[parent]['buckets']==size and live[parent]['wide_ids']==e['wide_ids'],'Duplication source')
                    for (old,b),value in list(hints.items()):
                        if old==parent:hints[g,b]=value
                else:require(parent==0,'Allocation parent')
                live[g]=e;slots[slot]=g
            else:
                require(g in live and slots.get(slot)==g and live[g]['buckets']==size and live[g]['wide_ids']==e['wide_ids'],'Lifecycle identity')
                if op==1:
                    del live[g];del slots[slot]
                    hints={key:value for key,value in hints.items() if key[0]!=g}
        elif kind=='call':
            qevent(e);require(active_call is None,'Nested table call');active_call=e['call']
            if e['table_buckets']:
                g=valid_generation(e);require(live[g]['buckets']==e['table_buckets'] and live[g]['wide_ids']==e['wide_ids'],'Table shape')
        elif kind=='callend':
            qevent(e);require(active_call==e['call'],'Table call completion');active_call=None
        elif kind=='mutation':
            qevent(e);g=valid_generation(e);b=integer(e['bucket'],0,live[g]['buckets']-1)
            op=integer(e['kind'],0,1);code=integer(e['code'],0,96);identity=integer(e['id'],0,(1<<32)-1)
            require(live[g]['wide_ids'] or identity<65535 or identity==(1<<32)-1,'Narrow ID domain')
            if not op:
                require(integer(e['origin'])==0 and code==hints.get((g,b),(0,0,0))[0],'Invalidation snapshot')
                mutations['id_writes']+=1;mutations['invalidations']+=bool(code);hints.pop((g,b),None)
            else:
                integer(e['origin'],1,2);require(code>0 and identity!=(1<<32)-1 and (g,b) not in hints,'Bad seed')
                require(previous_mutation is not None and previous_mutation['kind']==0 and
                    all(e[k]==previous_mutation[k] for k in ('generation','bucket','id','query')),'Seed without exact preceding ID write')
                hints[g,b]=(code,identity,e['origin']);mutations['seeds']+=1
            previous_mutation=e
        elif kind=='leaf':
            qevent(e);g=valid_generation(e);require(integer(e['call'],0,len(calls)-1)==active_call,'Leaf outside call')
            c=calls[e['call']];require(c['generation']==g,'Leaf table mismatch')
            b=integer(e['bucket'],0,live[g]['buckets']-1);slot=integer(e['slot'],0,7)
            code=integer(e['code'],0,96);n=integer(e['count'],1,96);t=integer(e['terminal'],0,5);s=integer(e['stale'],-1,1)
            identity=integer(e['leaf_id'],0,(1<<32)-2);bit(e['result']);bit(e['useful'])
            if slot:require(code==0 and t==0 and s==-1,'Nonzero slot hint')
            else:
                saved=hints.get((g,b),(0,0,0));require(code==saved[0],'Hint differs from shadow state')
                if not code:require(t==1 and s==-1,'Disabled classification')
                else:
                    require(identity==saved[1],'Hint/leaf ID mismatch')
                    if code-1>=n:require(t==2 and s==1,'Out-of-range classification')
                    else:require(t in (3,4,5) and s in (0,1),'In-range stale partition')
            require(t!=5 or e['result']==1,'Hint success but original failure')
            require(e['useful']==int(t==5 and e['result']==1),'Useful classification')
            terminals[t]+=1;stale[s+1]+=1
            if e['useful']:useful.add(e['query'])
            bycall[e['call']].append(e)
        elif kind=='filter':
            qevent(e);g=valid_generation(e);scan=bit(e['scan']);original=bit(e['original']);folded=bit(e['folded'])
            require(scan==0,'Fixed six cases do not call scan')
            require(not original or folded,'Folded false negative')
            if not scan:
                require(integer(e['call'],0,len(calls)-1)==active_call and calls[e['call']]['generation']==g,'Filter outside table call')
                byfilter[e['call']].append(e)
            else:require(e['call'] is None,'Scan call identity')
            filters[scan][0 if original else 2 if folded else 1]+=1
    require(not live and not slots and phase==4 and active_query is None and active_call is None,'Cleanup did not complete')
    for i,c in enumerate(calls):
        require(len(bycall[i])==c['leaf_calls'] and sum(e['result'] for e in bycall[i])==c['result'],'Leaf events disagree with calls')
        require(len(byfilter[i])==c['filter_evaluated'] and sum(e['original'] for e in byfilter[i])==c['filter_true'],'Filter events disagree with calls')
    pt=row['phase_totals'];require(len(pt)==5,'Phase totals')
    for i,t in enumerate(pt):
        require(integer(t['phase'])==i,'Phase order')
        for key in ('id_writes','invalidations','seed_attempts','seeds'):integer(t[key])
        require(t['invalidations']<=t['id_writes'] and t['seeds']<=min(t['seed_attempts'],t['id_writes']),'Mutation totals')
    require(all(pt[2][k]==v for k,v in mutations.items()),'Counted mutation events disagree')
    totals=dict(terminals=terminals,stale=stale,useful_queries=len(useful),filters=filters)
    def typed_equal(a,b):
        if type(a) is not type(b):return False
        if isinstance(b,dict):return set(a)==set(b) and all(typed_equal(a[k],b[k]) for k in b)
        if isinstance(b,list):return len(a)==len(b) and all(typed_equal(x,y) for x,y in zip(a,b))
        return a==b
    require(typed_equal(row['totals'],totals),'Derived totals mismatch')
    return totals

def check_all(rows):
    require(len(rows)==6 and {r['case'] for r in rows}==set(CASES),'Six fixed cases required')
    results={r['case']:check(r) for r in rows}
    return dict(verified=True,untimed=True,counts=results,
                primary_useful_exposure=results['hit']['useful_queries'],
                zero_primary_closes_lead=(results['hit']['useful_queries']==0),no_speed_prediction=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('outputs',nargs='+');args=parser.parse_args()
    print(json.dumps(check_all([json.loads(Path(p).read_text()) for p in args.outputs]),indent=2))
