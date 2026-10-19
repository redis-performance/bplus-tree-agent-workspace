#!/usr/bin/env python3
"""Read immutable reporting objects; never execute renderer or benchmarks."""
import csv, hashlib, io, json, statistics, subprocess
from decimal import Decimal
from pathlib import Path
HERE = Path(__file__).resolve().parent
REV = 'a51d1a0ac'
BASE = 'experiments/NIGHT-EXPLORATION-001/'
inputs = {}
def read(rev,path):
    raw=subprocess.check_output(['git','show',rev+':'+path])
    inputs[rev+':'+path]=hashlib.sha256(raw).hexdigest()
    return raw
def js(rev,path): return json.loads(read(rev,path))
chart=js(REV,BASE+'latest-charts/aws-arm-mask-primary.json')
assert chart['decision']=='PARK' and chart['source_adoption']=='NONE' and chart['new_population'] is False
renderer=read(REV,'scripts/render-aws-arm-mask-primary.py')
assert hashlib.sha256(renderer).hexdigest()==chart['renderer_sha256']
for suffix,digest in chart['artifacts'].items():
    artifact=read(REV,BASE+'latest-charts/aws-arm-mask-primary'+suffix)
    assert hashlib.sha256(artifact).hexdigest()==digest
common=Path(subprocess.check_output(['git','rev-parse','--git-common-dir'],text=True).strip()).resolve()
local=common.parent/BASE/'latest-charts/aws-arm-mask-primary.png'
assert hashlib.sha256(local.read_bytes()).hexdigest()==chart['artifacts']['.png']
prior=js('16f074fbe',BASE+'runs/aws-intel/20261019T020000Z/025-arm-mask-raw-review/raw-audit.json')
assert len(chart['effects'])==len(prior['effects'])==12
for actual,expected in zip(chart['effects'],prior['effects']):
    assert (actual['size'],actual['block'])==(expected['size'],expected['block'])
    assert abs(Decimal(str(actual['effect_pct']))-Decimal(expected['effect_pct_decimal']))<Decimal('1e-10')
    assert actual['effect_pct']<=-2
for size in (100000,1000000):
    median=statistics.median(Decimal(x['effect_pct_decimal']) for x in prior['effects'] if x['size']==size)
    assert abs(Decimal(str(chart['median_effect_pct'][str(size)]))-median)<Decimal('1e-10')
prefix=BASE+'runs/aws-arm/20261019T020000Z/024-corrected-iterator/aa/'
aa=js('73c9e313f',prefix+'result.json'); groups={}
assert len(aa['runs'])==48
for run in aa['runs']:
    row,=csv.DictReader(io.StringIO(read('73c9e313f',prefix+run['name']+'.csv').decode()))
    assert row==run['row'] and run['returncode']==0
    assert run['seed']==701+run['block']%3
    assert row['operations']==row['requested_ops']=='50000000'
    assert row['member_bytes']=='16' and row['cpu_start']==row['cpu_end']=='2'
    groups.setdefault((run['size'],run['block']),[]).append((run,row))
assert len(groups)==len(chart['baseline_aa_effects'])==12
for actual,((size,block),runs) in zip(chart['baseline_aa_effects'],sorted(groups.items())):
    assert [x['label'] for x,r in runs]==list('ABBA')
    times=[int(r['elapsed_ns']) for _,r in runs]
    effect=100*(Decimal(times[1]+times[2])/Decimal(times[0]+times[3])-1)
    assert min(times)>=10000000 and abs(effect)<=1
    assert (actual['size'],actual['block'])==(size,block) and actual['qualified']
    assert abs(effect-Decimal(str(actual['effect_pct'])))<Decimal('1e-10')
root=js('27a4afee1',BASE+'reviews/aws-arm-iterator-baseline-independent-audit.json')
assert root['effects']==chart['baseline_aa_effects']
for path in ['README.md','experiments/EXPERIMENTS.md','experiments/SUMMARY.md',BASE+'AWS-STATUS.md',BASE+'AWS-DECISIONS.md',BASE+'latest-charts/README.md']:
    read(REV,path)
report={'status':'pass_with_known_text_correction_pending','revision':REV,'primary_blocks':12,'baseline_aa_blocks':12,'baseline_aa_raw_rows_recomputed':48,'primary_reference':'Independent Decimal reconstruction 16f074fbe; not producer audit code','maximum_allowed_rounding_error_pct':'1e-10','baseline_seeds':[701,702,703],'primary_seeds':[401,402,403],'decision':'PARK','source_adoption':'NONE','new_population':False,'visual_local_png_matches_pinned_object':True,'renderer_executed':False,'benchmark_build_or_remote_execution':False,'known_finding':'570 total validation commands includes 34 preparation/build/inspection commands; correction announced by coordinator but not present at reviewed revision','additional_material_findings':[],'input_count':len(inputs)}
(HERE/'audit.json').write_text(json.dumps(report,indent=2)+'\n')
(HERE/'input-hashes.json').write_text(json.dumps(inputs,indent=2,sort_keys=True)+'\n')
print(json.dumps(report))
