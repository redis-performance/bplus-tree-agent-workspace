#!/usr/bin/env python3
"""Synthetic Python only; never executes lifecycle or another C program."""
import copy,unittest
import check_output as c
import validate_static as v
def synthetic():
    a=dict(enabled=2,eligible=2,unchanged=1,stale=1,out_of_range=0,ineligible=0,full_success=1)
    points=[dict(name=n,count=len(ids),score_sum=sum(i+1 for i in ids),id_sum=sum(ids),model_lookups=8192,owned_bytes=10000,audit=dict(a)) for n,ids in zip(c.NAMES,c.models())]
    life=[]
    for seq,(kind,g,parent,slot,phase) in enumerate([(0,1,0,0,0),(2,2,1,1,0),(0,3,0,2,0),(1,1,0,0,0),(1,3,0,2,0),(1,2,0,1,4)],1):
        life.append(dict(seq=seq,kind=kind,generation=g,parent=parent,registry_slot=slot,phase=phase,buckets=128,wide_ids=0))
    return dict(diagnostic='slot-lifecycle',revision=0,verified=True,untimed=True,seed=17,members=2048,
        delete_count=64,range_deleted=1025,lookup_bound=65536,verification_lookups=57344+18,
        delete_id_writes=2,delete_invalidations=1,copied_tables=1,copied_hints=2,copied_stale=1,
        dup_reseeded=0,rebuild_seeds=2,rebuild_origin2=2,retired_original_tables=1,
        duplicate_unchanged=True,cleanup_complete=True,live_generations=0,census_queries=0,
        predup_audit=dict(a),dup_audit=dict(a),old_generations=[1,0],rebuilt_generation=3,
        rebuild_begin=2,rebuild_end=4,checkpoints=points,lifecycle=life)
class Static(unittest.TestCase):
    def reject(self,row):
        with self.assertRaises(ValueError):c.check(row)
    def test_complete_fixed_model(self):
        c.check(synthetic());self.assertEqual([len(x) for x in c.models()],[2048,1984,1984,1984,959,1984,1984])
    def test_frozen_source_and_completion(self):self.assertTrue(v.validate()['passed'])
    def test_required_coverage_and_completion(self):
        for k,value in [('copied_stale',0),('delete_invalidations',0),('rebuild_seeds',0),('cleanup_complete',False),
                        ('dup_reseeded',1),('duplicate_unchanged',False),('census_queries',1),('verification_lookups',65537)]:
            row=synthetic();row[k]=value
            with self.subTest(key=k):self.reject(row)
    def test_model_and_lookup_counts(self):
        for key in ('count','score_sum','id_sum','model_lookups'):
            row=synthetic();row['checkpoints'][4][key]+=1;self.reject(row)
        row=synthetic();row['verification_lookups']+=1;self.reject(row)
    def test_schema_and_integer_types(self):
        for k,value in [('cycles',1),('elapsed_ns',1),('address','x')]:
            row=synthetic();row[k]=value;self.reject(row)
        for value in (True,2048.0):
            row=synthetic();row['members']=value;self.reject(row)
        row=synthetic();row['checkpoints'][0]['extra']=1;self.reject(row)
        for text in ('{"a":1,"a":2}','{"a":NaN}'):
            with self.assertRaises(ValueError):c.loads(text)
    def test_audit_partition_and_copied_identity(self):
        row=synthetic();row['predup_audit']['stale']=0;self.reject(row)
        row=synthetic();row['checkpoints'][1]['audit'].update(stale=0,unchanged=2,full_success=2);self.reject(row)
        row=synthetic();row['dup_audit']['out_of_range']=1;self.reject(row)
    def test_generation_lifetime_failures(self):
        for index,key,value in [(1,'parent',9),(2,'generation',1),(2,'registry_slot',1),(5,'kind',4),(0,'buckets',127),(0,'phase',2)]:
            row=synthetic();row['lifecycle'][index][key]=value
            with self.subTest(key=key,index=index):self.reject(row)
    def test_rebuild_evidence_and_checkpoint_order(self):
        for k,value in [('rebuild_begin',3),('rebuild_end',3),('rebuilt_generation',2),('old_generations',[2,0]),('retired_original_tables',2)]:
            row=synthetic();row[k]=value;self.reject(row)
        row=synthetic();row['checkpoints'][0]['name']='deleted';self.reject(row)
if __name__=='__main__':unittest.main(verbosity=2)
