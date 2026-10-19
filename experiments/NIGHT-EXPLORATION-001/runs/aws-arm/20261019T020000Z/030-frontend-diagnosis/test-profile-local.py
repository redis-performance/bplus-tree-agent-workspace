#!/usr/bin/env python3
"""Small synthetic negative controls; no performance or ARM claims."""
import copy,json,pathlib,tempfile
from profile_common import counters,raw_samples,mapping,scope_validity,row,allocator_mode
from native_common import HERE
checks=[]
assert allocator_mode({'command':['build/h4-census-san']})=='ASan_UBSan' and allocator_mode({'command':['build/h4-census']})=='native'
checks.append(dict(name='allocator_modes_separate',pass_=True))
def rejects(name,fn):
 try:fn()
 except (AssertionError,ValueError,KeyError):checks.append(dict(name=name,detected=True));return
 raise AssertionError('fault accepted: '+name)
with tempfile.TemporaryDirectory() as td:
 p=pathlib.Path(td)/'stat';base='100,,cycles:u,1000000,100.00\n90,,instructions:u,1000000,100.00\n10,,branches:u,1000000,100.00\n0,,branch-misses:u,1000000,100.00\n';p.write_text(base);assert counters(p,True)['enabled'];checks.append(dict(name='positive_counter_parser',pass_=True))
 for name,bad in [('infinite_count',base.replace('100,,','inf,,',1)),('nan_count',base.replace('100,,','nan,,',1)),('fraction_count',base.replace('100,,','1.5,,',1)),('negative_count',base.replace('100,,','-1,,',1)),('zero_cycles',base.replace('100,,','0,,',1)),('zero_runtime',base.replace(',1000000,',',0,',1)),('infinite_runtime',base.replace(',1000000,',',inf,',1)),('nan_runtime',base.replace(',1000000,',',nan,',1)),('multiplexed',base.replace(',100.00',',99.00',1)),('missing_event','\n'.join(base.splitlines()[:-1])+'\n'),('duplicate_event',base+base.splitlines()[0]+'\n')]:
  p.write_text(bad);rejects(name,lambda:counters(p,True))
 p.write_text(base);rejects('disabled_nonzero',lambda:counters(p,False));p.write_text('100\n 400000 main+0x0\n');assert raw_samples(p)[0]['physical_ip']=='400000';checks.append(dict(name='raw_PC_preserved',pass_=True))
 for name,bad in [('zero_sample_period','0\n 400000 main+0x0\n'),('missing_raw_PC','100\n main+0x0\n'),('missing_frame','100\n')]:
  p.write_text(bad);rejects(name,lambda:raw_samples(p))
 fn={i*4:{'bytes':[f'{i:08x}']} for i in range(10)};assert mapping(fn,fn,16)['status']=='same_offset_exact';other={k+100:v for k,v in fn.items()};assert mapping(fn,other,16)['status']=='unique_exact_seven_word_window';other[116]={'bytes':['ffffffff']};assert mapping(fn,other,16)['status']=='ambiguous_or_unmatched';checks.append(dict(name='map_mismatch_retained',detected=True))
 assert scope_validity(True,[],True);assert not scope_validity(False,[],True);assert not scope_validity(True,['lost warning'],True);assert not scope_validity(True,[],False);checks.extend(dict(name=n,detected=True) for n in ['lost_invalidates_scope','warning_retained_invalidates_scope','missing_PC_map_invalidates_scope'])
 # Independent fixture parser rejects corrupt actual-row outputs using retained native controls.
 fixture=json.loads((HERE/'cells.json').read_text())[0];fixture=dict(fixture,seed=1601);text=(HERE/'native-AA/0000.csv').read_text();row(text,fixture)
 import csv,io
 for field in ['operations','checksum','traversals']:
  z=list(csv.DictReader(text.splitlines()))[0];z[field]=str(int(z[field])+1);o=io.StringIO();w=csv.DictWriter(o,fieldnames=z);w.writeheader();w.writerow(z);rejects('wrong_'+field,lambda:row(o.getvalue(),fixture))
result=dict(platform='local synthetic Python; no ARM PMU execution',checks=checks,missing_disable_control='Real separately compiled faulty known source is in fixed ARM commands; not executed by these tests',instruction_direction='Not a validity predicate; unfavorable valid observations retained');(HERE/'PROFILE-LOCAL-CHECKS.json').write_text(json.dumps(result,indent=2)+'\n');print(len(checks),'local parser/fault checks pass')
