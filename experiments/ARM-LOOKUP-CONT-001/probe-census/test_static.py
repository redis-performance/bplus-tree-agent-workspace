#!/usr/bin/env python3
"""Synthetic Python checks only; no diagnostic ELF may be executed here."""
import copy
import importlib.util
from pathlib import Path
import unittest

HERE=Path(__file__).resolve().parent
def module(name):
    spec=importlib.util.spec_from_file_location(name,HERE/(name+'.py'))
    value=importlib.util.module_from_spec(spec);spec.loader.exec_module(value);return value
c=module('check_output');v=module('validate_static')


def synthetic(case):
    sweeps=2 if case=='update' else 1;count=500*sweeps;calls=[]
    for i in range(count):
        row={k:0 for k in c.COUNTERS}
        row.update(call=i,query=i,active_resize=0,destination_table=0,wide_ids=0,
                   result=int(case!='miss'),table_buckets=128,bucket_visits=1)
        if case=='miss':row.update(filter_evaluated=1,filter_false=1)
        else:row.update(approximate_candidates=1,true_tag_candidates=1,leaf_calls=1,
                        leaf_successes=1,leaf_entries_present=20,home_hit=1)
        calls.append(row)
    return dict(revision=0,verified=True,untimed=True,case=case,seed=17,members=500,
                warmup_sweeps=1000,sweeps=sweeps,ops=count,hits=0 if case=='miss' else count,
                score_sum=125250 if case=='score' else 0,owned_bytes_before=c.EXPECTED_OWNED_BYTES[case],
                owned_bytes_after=c.EXPECTED_OWNED_BYTES[case],owned_bytes_after_validation=c.EXPECTED_OWNED_BYTES[case],
                active_resize_before=0,active_resize_after=0,query_count=count,
                query_resize=[[0,0] for _ in range(count)],table_call_count=count,
                table_calls=calls,totals={k:sum(r[k] for r in calls) for k in c.COUNTERS})


def recount(row):
    row['totals']={k:sum(r[k] for r in row['table_calls']) for k in c.COUNTERS}
    return row


def reviewer_adversaries():
    # Exact independent-review examples; totals are intentionally consistent so
    # rejection must come from crosschecks rather than a stale aggregate.
    changes={
        'repeat_without_distinct':dict(approximate_candidates=2,true_tag_candidates=2,
            leaf_calls=2,leaf_failures=1,repeat_failed_all=1,
            repeat_leaf_entries_present=10,leaf_entries_present=30),
        'filter_rejects_success':dict(home_hit=0,filter_evaluated=1,filter_false=1),
        'resize_without_endpoints':dict(active_resize=1,destination_table=1),
        'home_hit_without_visit':dict(bucket_visits=0),
    }
    for name,change in changes.items():
        row=synthetic('hit');row['table_calls'][0].update(change)
        yield name,recount(row)


class Static(unittest.TestCase):
    def test_generated_patch_and_source_scope(self):
        self.assertTrue(v.validate([])['passed'])

    def test_six_synthetic_models(self):
        report=c.check_all([synthetic(case) for case in c.CASES])
        self.assertEqual(report['primary_repeat_failed_all'],0)
        self.assertFalse(report['negative_cache_primary_opportunity'])

    def test_seed_count_checksum_timing_memory_rejected(self):
        for key,value in [('seed',29),('warmup_sweeps',999),('sweeps',2),('ops',499),
                           ('hits',0),('score_sum',1),('untimed',False),('elapsed_ns',1),
                           ('owned_bytes_after',12344),('members',501),('query_count',499)]:
            row=synthetic('hit');row[key]=value
            with self.subTest(key=key),self.assertRaises(ValueError):c.check(row)

    def test_update_restore_count(self):
        row=synthetic('update');self.assertEqual(row['ops'],1000);c.check(row)
        row['sweeps']=1
        with self.assertRaises(ValueError):c.check(row)

    def test_incomplete_case_set(self):
        with self.assertRaises(ValueError):c.check_all([synthetic('hit')])
        with self.assertRaises(ValueError):c.check_all([synthetic('hit') for _ in range(6)])

    def test_counter_partitions_and_types(self):
        for key,value in [('approximate_candidates',0),('leaf_calls',2),('leaf_failures',1),
                           ('distinct_failed_leaves',1),('repeat_failed_all',1),
                           ('repeat_failed_consecutive',1),('repeat_failed_cross_bucket',1),
                           ('home_hit',0),('filter_evaluated',1),('table_buckets',0),
                           ('displaced_bucket_visits',1),('migration_skips',1),
                           ('tombstone_skips',1),('leaf_entries_present',False),
                           ('destination_table',1),('result',0)]:
            row=synthetic('hit');row['table_calls'][0][key]=value
            with self.subTest(key=key),self.assertRaises(ValueError):c.check(row)

    def test_call_order_totals_and_states(self):
        row=synthetic('hit');row['table_calls'][0]['call']=1
        with self.assertRaises(ValueError):c.check(row)
        row=synthetic('hit');row['table_calls'][0]['query']=1
        with self.assertRaises(ValueError):c.check(row)
        row=synthetic('hit');row['totals']['leaf_calls']+=1
        with self.assertRaises(ValueError):c.check(row)
        row=synthetic('hit');row['query_resize'][10]=[1,0]
        with self.assertRaises(ValueError):c.check(row)

    def test_repeated_failed_leaf_synthetic_accounting(self):
        # Abstract trace: failed A,A,B in home bucket, then failed A elsewhere,
        # then successful C. This does not execute or simulate the C workload.
        row=synthetic('hit');call=row['table_calls'][0]
        call.update(bucket_visits=2,displaced_bucket_visits=1,approximate_candidates=5,
                    true_tag_candidates=5,leaf_calls=5,leaf_failures=4,distinct_failed_leaves=2,
                    repeat_failed_all=2,repeat_failed_consecutive=1,repeat_failed_cross_bucket=1,
                    leaf_entries_present=100,repeat_leaf_entries_present=40,home_hit=0,
                    filter_evaluated=1,filter_true=1,home_postfilter_fallback=1)
        row['totals']={k:sum(r[k] for r in row['table_calls']) for k in c.COUNTERS}
        self.assertEqual(c.check(row)['repeat_failed_all'],2)
        broken=copy.deepcopy(row);broken['table_calls'][0]['repeat_failed_all']=0
        with self.assertRaises(ValueError):c.check(broken)

    def test_independent_review_adversaries(self):
        for name,row in reviewer_adversaries():
            with self.subTest(name=name),self.assertRaises(ValueError):c.check(row)

    def test_wrong_but_equal_memory(self):
        for case in c.CASES:
            row=synthetic(case)
            row['owned_bytes_before']=row['owned_bytes_after']=c.EXPECTED_OWNED_BYTES[case]+1
            with self.subTest(case=case),self.assertRaises(ValueError):c.check(row)
        # The validation endpoint remains separate, not the admission endpoint.
        row=synthetic('hit');row['owned_bytes_after_validation']+=1;c.check(row)

    def test_bucket_and_repeat_crosschecks(self):
        changes={
            'candidate_capacity':dict(approximate_candidates=9),
            'home_after_displacement':dict(bucket_visits=2,displaced_bucket_visits=1),
            'cross_without_displacement':dict(approximate_candidates=3,true_tag_candidates=3,
                leaf_calls=3,leaf_failures=2,distinct_failed_leaves=1,repeat_failed_all=1,
                repeat_failed_cross_bucket=1,repeat_leaf_entries_present=20,leaf_entries_present=60),
            'exposure_without_repeat':dict(repeat_leaf_entries_present=1),
            'migration_without_resize':dict(approximate_candidates=2,true_tag_candidates=2,migration_skips=1),
            'free_without_resize':dict(approximate_candidates=2,true_tag_candidates=2,free_reference_skips=1),
        }
        for name,change in changes.items():
            row=synthetic('hit');row['table_calls'][0].update(change)
            with self.subTest(name=name),self.assertRaises(ValueError):c.check(recount(row))
        row=synthetic('miss');row['table_calls'][0].update(bucket_visits=2,displaced_bucket_visits=1)
        with self.assertRaises(ValueError):c.check(recount(row))
        row=synthetic('miss');row['table_calls'][0].update(table_buckets=0,bucket_visits=0,
                                                         filter_evaluated=0,filter_false=0)
        c.check(recount(row))
        # With otherwise-valid empty-table flags, even approximate work is invalid.
        row['table_calls'][0]['approximate_candidates']=1
        with self.assertRaises(ValueError):c.check(recount(row))

    def test_resize_completion_remains_valid(self):
        # Rehash completion may precede the first table call of a query.
        row=synthetic('hit');row['active_resize_before']=1;row['query_resize'][0]=[1,0]
        c.check(row)
        # A still-active resize may find the member in the destination table.
        row=synthetic('hit');row['active_resize_before']=row['active_resize_after']=1
        row['query_resize']=[[1,1] for _ in row['query_resize']]
        for call in row['table_calls']:call.update(active_resize=1,destination_table=1)
        c.check(row)
        # Free IDs are only legitimate in the resizing source table.
        call=row['table_calls'][0]
        call.update(destination_table=0,approximate_candidates=2,true_tag_candidates=2,free_reference_skips=1)
        c.check(recount(row))
        call['destination_table']=1
        with self.assertRaises(ValueError):c.check(recount(row))


if __name__=='__main__':unittest.main(verbosity=2)
