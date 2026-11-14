#!/usr/bin/env python3
"""Pure Python synthetic/static admission checks; no C executable is run."""
import copy
import unittest
import check_output as c

def synthetic(case='hit',hint=0,lifecycle=None):
    count=1000 if case=='update' else 500;seq=0
    def tick():
        nonlocal seq
        seq+=1;return seq
    lifecycle=lifecycle or [(0,1,0,0),(0,2,0,1)]
    lives=[];live={}
    for kind,g,parent,slot in lifecycle:
        e=dict(seq=tick(),phase=0,kind=kind,generation=g,parent=parent,registry_slot=slot,wide_ids=0,buckets=128)
        lives.append(e)
        if kind in (0,2):live[g]=e
        elif kind==1:del live[g]
    begin=tick();calls=[];leaves=[];filters=[];bounds=[]
    for q in range(count):
        qbegin=tick();call={k:0 for k in c.COUNTERS}
        call.update(call=q,query=q,seq=tick(),generation=2,active_resize=0,destination_table=0,
                    wide_ids=0,table_buckets=128,result=int(case!='miss'),bucket_visits=1)
        if case=='miss':
            call.update(filter_evaluated=1,filter_false=1)
            filters.append(dict(event=len(filters),seq=tick(),generation=2,query=q,call=q,consumer=0,original=0,folded=0))
        else:
            call.update(approximate_candidates=1,true_tag_candidates=1,leaf_calls=1,leaf_successes=1,home_hit=1)
            terminal=5 if hint and q==0 else 4 if hint else 1
            leaves.append(dict(event=len(leaves),seq=tick(),generation=2,query=q,call=q,bucket=0,slot=0,
                code=hint,count=20,terminal=terminal,stale=0 if hint else -1,result=1,useful=int(terminal==5),leaf_id=0))
        call['end_seq']=tick();calls.append(call);bounds.append([qbegin,tick()])
    end=tick()
    for g,e in sorted(live.items(),reverse=True):
        lives.append(dict(e,seq=tick(),phase=4,kind=1,parent=0))
    rows=dict(revision=0,diagnostic='slot-hint',verified=True,untimed=True,cleanup_complete=True,
        live_generations_after_cleanup=0,case=case,seed=17,members=500,warmup_sweeps=1000,sweeps=count//500,
        ops=count,hits=0 if case=='miss' else count,score_sum=125250 if case=='score' else 0,
        owned_bytes_before=c.MEMORY[case],owned_bytes_after=c.MEMORY[case],owned_bytes_after_validation=c.MEMORY[case],
        active_resize_before=0,active_resize_after=0,query_count=count,query_resize=[[0,0] for _ in range(count)],
        query_bounds=bounds,count_start=begin,count_end=end,table_call_count=len(calls),table_calls=calls,
        lifecycle=lives,initial_hints=[dict(generation=2,bucket=0,code=hint,origin=1,id=0)] if hint else [],
        phase_totals=[dict(phase=i,id_writes=int(bool(hint) and i==0),invalidations=0,
                         seed_attempts=int(bool(hint) and i==0),seeds=int(bool(hint) and i==0)) for i in range(5)],
        mutations=[],leaf_events=leaves,filter_events=filters)
    return recount(rows)

def recount(row):
    terminal=[0]*6;stale=[0]*3;useful=set();filters=[[0]*3 for _ in range(3)]
    for e in row['leaf_events']:
        terminal[e['terminal']]+=1;stale[e['stale']+1]+=1
        if e['useful']:useful.add(e['query'])
    for e in row['filter_events']:filters[e['consumer']][0 if e['original'] else 2 if e['folded'] else 1]+=1
    row['totals']=dict(terminals=terminal,stale=stale,useful_queries=len(useful),filters=filters)
    return row

def shift_sequences(row,at,delta):
    for key in ('count_start','count_end'):
        if row[key]>=at:row[key]+=delta
    for pair in row['query_bounds']:
        for i in range(2):
            if pair[i]>=at:pair[i]+=delta
    for key in ('lifecycle','mutations','leaf_events','filter_events','table_calls'):
        for e in row[key]:
            for field in ('seq','end_seq'):
                if field in e and e[field]>=at:e[field]+=delta

class Admission(unittest.TestCase):
    def reject(self,row):
        with self.assertRaises((ValueError,KeyError)):c.check(row)

    def test_six_models_and_positive_exposure(self):
        result=c.check_all([synthetic(k) for k in c.CASES]);self.assertTrue(result['zero_primary_closes_lead'])
        self.assertEqual(c.check(synthetic(hint=1))['useful_queries'],1)

    def test_fixed_model_memory_and_completion(self):
        for key,value in [('seed',29),('ops',499),('hits',0),('score_sum',1),('cleanup_complete',False),
                          ('live_generations_after_cleanup',1),('warmup_sweeps',999),('elapsed_ns',1),('verified',False)]:
            row=synthetic();row[key]=value
            with self.subTest(key=key):self.reject(row)
        for case in c.CASES:
            row=synthetic(case);row['owned_bytes_before']=row['owned_bytes_after']=c.MEMORY[case]+1;self.reject(row)
        row=synthetic();row['owned_bytes_after_validation']+=1;c.check(row)

    def test_four_prior_census_admission_classes(self):
        for change in [dict(home_hit=0,filter_evaluated=1,filter_false=1),dict(active_resize=1,destination_table=1),dict(bucket_visits=0)]:
            row=synthetic();row['table_calls'][0].update(change);self.reject(row)
        row=synthetic();row['leaf_events'][0].update(terminal=5,useful=1);self.reject(recount(row))

    def test_terminal_stale_bijection(self):
        changes=[dict(terminal=0),dict(stale=0),dict(code=97),dict(slot=1),dict(useful=1),dict(count=0)]
        for change in changes:
            row=synthetic();row['leaf_events'][0].update(change)
            with self.subTest(change=change):self.reject(recount(row))
        for terminal in (3,4,5):
            for stale in (0,1):
                row=synthetic(hint=1);row['leaf_events'][0].update(terminal=terminal,stale=stale,useful=int(terminal==5))
                c.check(recount(row))
        row=synthetic(hint=1);row['leaf_events'][0]['stale']=-1;self.reject(recount(row))

    def test_equal_count_is_stale_out_of_range(self):
        row=synthetic(hint=21)
        for e in row['leaf_events']:e.update(terminal=2,stale=1,useful=0)
        c.check(recount(row))
        row['leaf_events'][0].update(terminal=4,stale=0);self.reject(recount(row))

    def test_nonzero_slots_never_use_hint(self):
        row=synthetic(hint=1)
        for e in row['leaf_events']:e.update(slot=1,code=0,terminal=0,stale=-1,useful=0)
        c.check(recount(row));row['leaf_events'][0].update(code=1,terminal=5,stale=0,useful=1);self.reject(recount(row))

    def test_hint_success_requires_original_success(self):
        row=synthetic(hint=1);row['leaf_events'][0]['result']=0;self.reject(row)
        row=synthetic(hint=1);row['totals']['useful_queries']=500;self.reject(row)
        row=synthetic(hint=1);row['totals']['terminals'][0]=False;self.reject(row)

    def test_filter_conservative_observations(self):
        row=synthetic('miss');row['filter_events'][0]['folded']=1
        self.assertEqual(c.check(recount(row))['filters'][0][2],1)
        row['filter_events'][0].update(original=1,folded=0);self.reject(recount(row))
        row=synthetic('miss');row['filter_events'][0]['call']=1;self.reject(row)

    def test_lifecycle_dup_promotion_rebind_and_slot_reuse(self):
        life=[(0,1,0,0),(0,2,0,1),(2,3,1,2),(3,3,0,2),(4,3,0,2),(1,1,0,0),(0,4,0,0)]
        c.check(synthetic(lifecycle=life))
        for index,change in [(2,dict(parent=9)),(6,dict(generation=1)),(6,dict(registry_slot=1)),
                             (3,dict(generation=9)),(0,dict(buckets=1025))]:
            row=synthetic(lifecycle=life);row['lifecycle'][index].update(change)
            with self.subTest(index=index,change=change):self.reject(row)
        row=synthetic();row['lifecycle'][-1]['kind']=4;self.reject(row)

    def test_counted_slot_zero_invalidation_and_reseed(self):
        row=synthetic(hint=1);at=row['table_calls'][0]['seq'];shift_sequences(row,at,2)
        row['mutations']=[dict(seq=at,generation=2,query=0,kind=0,bucket=0,id=0,code=1,origin=0),
                          dict(seq=at+1,generation=2,query=0,kind=1,bucket=0,id=0,code=2,origin=1)]
        row['phase_totals'][2].update(id_writes=1,invalidations=1,seeds=1,seed_attempts=1)
        for e in row['leaf_events']:e['code']=2
        c.check(row)
        for field,value in [('origin',3),('code',97),('id',1),('bucket',1)]:
            bad=copy.deepcopy(row);bad['mutations'][1][field]=value
            with self.subTest(field=field):self.reject(bad)
        bad=copy.deepcopy(row);del bad['mutations'][0];shift_sequences(bad,at+1,-1)
        bad['phase_totals'][2].update(id_writes=0,invalidations=0);self.reject(bad)

    def test_counted_dup_copies_stale_hint(self):
        row=synthetic(hint=1);at=row['table_calls'][0]['seq'];shift_sequences(row,at,1)
        row['lifecycle'].append(dict(seq=at,phase=2,kind=2,generation=3,parent=2,registry_slot=2,wide_ids=0,buckets=128))
        last=max(e['seq'] for e in row['lifecycle'])
        row['lifecycle'].append(dict(seq=last+1,phase=4,kind=1,generation=3,parent=0,registry_slot=2,wide_ids=0,buckets=128))
        row['lifecycle'].sort(key=lambda e:e['seq'])
        for call in row['table_calls']:call['generation']=3
        for e in row['leaf_events']:e.update(generation=3,stale=1)
        c.check(recount(row))
        row['lifecycle'][2]['parent']=1;self.reject(row)

    def test_event_order_generation_and_domains(self):
        for key,value in [('seq',1),('generation',9),('query',1),('call',1),('bucket',128),('code',True),('leaf_id',1<<32)]:
            row=synthetic();row['leaf_events'][0][key]=value
            with self.subTest(key=key):self.reject(row)
        row=synthetic();row['query_bounds'][0][1]+=1;self.reject(row)
        row=synthetic();row['lifecycle'][-1]['phase']=2;self.reject(row)
        row=synthetic();row['phase_totals'][2]['id_writes']=1;self.reject(row)

    def test_resize_completion_valid(self):
        row=synthetic();row['query_resize'][0]=[1,0];row['active_resize_before']=1;c.check(row)

    def test_six_cases_required(self):
        with self.assertRaises(ValueError):c.check_all([synthetic()])

class FoldAlgebra(unittest.TestCase):
    def test_all_tags_and_bit_basis(self):
        low=(1<<56)-1;mask=(1<<64)-1
        def fold(x):return (x&low)|(x>>56)
        def bits(tag):
            mixed=(tag*0x9e3779b97f4a7c15)&mask
            return (1<<(tag&63))|(1<<(mixed>>58))|(1<<((mixed>>36)&63))
        for tag in range(256):
            m=bits(tag)
            for bit in range(64):
                word=m|(1<<bit)
                self.assertEqual(fold(word),fold(m)|fold(1<<bit))
                self.assertEqual(fold(word)&fold(m),fold(m))
            for other in range(256):self.assertEqual(fold(m|bits(other)),fold(m)|fold(bits(other)))
            for hint in range(256):self.assertEqual(((hint<<56)|fold(m))&low,fold(m))

if __name__=='__main__':unittest.main(verbosity=2)
