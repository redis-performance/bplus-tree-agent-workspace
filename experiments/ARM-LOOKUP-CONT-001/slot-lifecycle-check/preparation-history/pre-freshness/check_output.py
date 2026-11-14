#!/usr/bin/env python3
"""Strict offline checker for the one frozen lifecycle transcript."""
import argparse,json
from pathlib import Path
NAMES=('inserted','deleted','dup_original','dup_copy','rebuilt_original','rebuilt_copy','freed_original_copy')
AUDIT=('enabled','eligible','unchanged','stale','out_of_range','ineligible','full_success')
ROOT=('diagnostic','revision','verified','untimed','seed','members','delete_count','range_deleted','lookup_bound',
      'verification_lookups','delete_id_writes','delete_invalidations','copied_tables','copied_hints','copied_stale',
      'dup_reseeded','rebuild_seeds','rebuild_origin2','retired_original_tables','duplicate_unchanged',
      'cleanup_complete','live_generations','census_queries','predup_audit','dup_audit','old_generations',
      'rebuilt_generation','rebuild_begin','rebuild_end','checkpoints','lifecycle')
def require(x,message):
    if not x:raise ValueError(message)
def integer(x,low=0,high=(1<<64)-1):
    require(type(x) is int and low<=x<=high,'Integer domain');return x
def keys(x,want):require(type(x) is dict and set(x)==set(want),'Exact schema')
def audit(a):
    keys(a,AUDIT)
    for k in AUDIT:integer(a[k])
    require(a['enabled']==a['eligible']+a['ineligible'],'Eligibility partition')
    require(a['eligible']==a['unchanged']+a['stale'],'Stale partition')
    require(a['out_of_range']<=a['stale'] and a['unchanged']<=a['full_success']<=a['eligible'],'Audit result')
def models():
    all_ids=list(range(2048));deleted=[i for i in all_ids if i not in range(0,128,2)]
    survivors=deleted[:512]+deleted[1537:]
    return [all_ids,deleted,deleted,deleted,survivors,deleted,deleted]
def check(row):
    keys(row,ROOT);require(row['diagnostic']=='slot-lifecycle','Identity')
    for k in ('verified','untimed','cleanup_complete','duplicate_unchanged'):require(row[k] is True,'Completion flag')
    for k,v in dict(revision=0,seed=17,members=2048,delete_count=64,range_deleted=1025,lookup_bound=65536,
                    dup_reseeded=0,live_generations=0,census_queries=0).items():require(integer(row[k])==v,'Fixed model '+k)
    integer(row['delete_id_writes'],1);integer(row['delete_invalidations'],1,row['delete_id_writes'])
    integer(row['copied_tables'],1,2);integer(row['copied_hints'],1);integer(row['copied_stale'],1)
    require(integer(row['rebuild_seeds'],1)==integer(row['rebuild_origin2'],1),'Rebuild seeds')
    audit(row['predup_audit']);audit(row['dup_audit'])
    require(row['predup_audit']==row['dup_audit'],'Copied hints differ')
    require(row['copied_hints']==row['predup_audit']['enabled'] and row['copied_stale']==row['predup_audit']['stale'],'Copied coverage')
    points=row['checkpoints'];require(type(points) is list and len(points)==7,'Checkpoint count')
    lookups=0
    for p,name,ids in zip(points,NAMES,models()):
        keys(p,('name','count','score_sum','id_sum','model_lookups','owned_bytes','audit'))
        require(p['name']==name,'Checkpoint order')
        for k,v in dict(count=len(ids),score_sum=sum(i+1 for i in ids),id_sum=sum(ids),model_lookups=8192).items():
            require(integer(p[k])==v,'Checkpoint model '+k)
        integer(p['owned_bytes'],1);audit(p['audit']);lookups+=8192+p['audit']['eligible']
    require(points[1]['audit']['stale']>0 and points[1]['audit']['unchanged']>0,'Missing deletion coverage')
    lookups+=row['predup_audit']['eligible']+row['dup_audit']['eligible']
    require(integer(row['verification_lookups'],1,65536)==lookups,'Exact lookup count')
    life=row['lifecycle'];require(type(life) is list and 0<len(life)<=4096,'Lifecycle bound')
    live={};slots={};highest=0;phase=0;copies=0;snapshots={0:set()}
    for seq,e in enumerate(life,1):
        keys(e,('seq','phase','kind','generation','parent','registry_slot','wide_ids','buckets'))
        require(integer(e['seq'])==seq,'Lifecycle sequence')
        ep=integer(e['phase'],0,4);require(ep in (0,4) and ep>=phase,'Census phase used');phase=ep
        op=integer(e['kind'],0,4);require(op!=3,'Unexpected defrag')
        g=integer(e['generation'],1);parent=integer(e['parent']);slot=integer(e['registry_slot'],0,15)
        size=integer(e['buckets'],4,1024);require(size&(size-1)==0,'Table size');integer(e['wide_ids'],0,1)
        if op in (0,2):
            require(g==highest+1 and slot not in slots,'Generation reuse');highest=g
            if op==2:
                require(parent in live and all(e[k]==live[parent][k] for k in ('wide_ids','buckets')),'Copy parent');copies+=1
            else:require(parent==0,'Allocation parent')
            live[g]=e;slots[slot]=g
        else:
            require(parent==0 and g in live and slots.get(slot)==g and all(e[k]==live[g][k] for k in ('wide_ids','buckets')),'Lifetime identity')
            if op==1:del live[g];del slots[slot]
        snapshots[seq]=set(live)
    require(phase==4 and not live and not slots and copies==row['copied_tables'],'Cleanup/copy mismatch')
    old=row['old_generations'];require(type(old) is list and len(old)==2,'Old table record')
    integer(old[0],1);integer(old[1]);require(not old[1] or old[1]!=old[0],'Duplicate old generation')
    oldset=set(old)-{0};begin=integer(row['rebuild_begin'],0,len(life));end=integer(row['rebuild_end'],begin+1,len(life))
    new=integer(row['rebuilt_generation'],1)
    require(oldset<=snapshots[begin] and not oldset&snapshots[end] and new not in snapshots[begin] and new in snapshots[end],'Rebuild lifetime')
    span=life[begin:end]
    require(sum(e['kind']==1 and e['generation'] in oldset for e in span)==integer(row['retired_original_tables'],1,2)==len(oldset),'Rebuild retirement')
    require(any(e['kind']==0 and e['generation']==new for e in span),'Rebuild allocation missing')
    return dict(verified=True,untimed=True,checkpoints=7,verification_lookups=lookups,
                stale_after_delete=points[1]['audit']['stale'],copied_stale=row['copied_stale'],
                rebuild_seeds=row['rebuild_seeds'],cleanup_complete=True,no_performance_claim=True)
def loads(text):
    def unique(pairs):
        result={}
        for k,v in pairs:require(k not in result,'Duplicate JSON key');result[k]=v
        return result
    def bad(x):raise ValueError('Nonfinite JSON '+x)
    return json.loads(text,object_pairs_hook=unique,parse_constant=bad)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('output');a=p.parse_args();print(json.dumps(check(loads(Path(a.output).read_text())),indent=2))
