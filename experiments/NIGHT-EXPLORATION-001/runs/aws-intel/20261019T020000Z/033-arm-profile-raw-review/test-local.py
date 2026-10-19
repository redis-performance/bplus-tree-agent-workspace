#!/usr/bin/env python3
"""Local synthetic parser/arithmetic checks; does not invoke benchmark tools."""
import importlib.util,json
from pathlib import Path
p=Path(__file__).with_name('audit.py');spec=importlib.util.spec_from_file_location('review',p);a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
checks=[]
def ok(name,value):a.need(value,name);checks.append(name)
def reject(name,fn):
 try:fn()
 except (ValueError,KeyError):checks.append(name);return
 raise AssertionError(name)
x=a.assembly('00001000 <zbtreeIteratorNext>:\nzset_btree.c:508\n 1000: d503201f nop\n 1004: d65f03c0 ret\n')
ok('assembly source/word/address',x['zbtreeIteratorNext']['code'][0]==('d503201f','nop',('zset_btree.c',508)))
f={i*4:(f'{i:08x}','x',None) for i in range(12)}
ok('whole function exact',a.match_instruction(f,dict(f),16)['method']=='whole_body_exact')
g={k+8:v for k,v in f.items()}
ok('unique seven word relocation',a.match_instruction(f,g,16)=={'method':'unique_seven_words','offset':24})
g.update({k+100:v for k,v in f.items()})
ok('ambiguous repeated window rejected',a.match_instruction(f,g,16)['method']=='ambiguous_or_unmatched')
ok('function boundary cannot claim window',a.match_instruction(f,{},0)['method']=='unmatched_boundary')
s='10\n 1000 zbtScoreLeafScore+0x0 (inlined)\n 1000 zbtreeIteratorNext+0x4\n 2000 main+0x10\n\n20\n 3000 [unknown]\n'
r=a.samples(s);ok('physical not inclusive attribution',r[0]['symbol']=='zbtreeIteratorNext' and r[0]['offset']==4 and len(r[0]['frames'])==3)
ok('unknown period retained',r[1]['symbol']=='[unknown]' and sum(x['period'] for x in r)==30)
rep='# Total Lost Samples: 0\n# Samples: 2 of event cycles:u\n# Event count (approx.): 30\n'
ok('raw/report period conservation',a.sample_report(rep,r)['samples']==2)
reject('wrong report period rejected',lambda:a.sample_report(rep.replace('30','31'),r))
reject('wrong exact sample count rejected',lambda:a.sample_report(rep.replace('Samples: 2','Samples: 3'),r))
ok('compact sample label retained',a.sample_report(rep.replace('Samples: 2','Samples: 2K'),r)['sample_label'].startswith('2K'))
reject('zero period rejected',lambda:a.samples('0\n 1000 main+0x0\n'))
text='\n'.join(f'100,,{e},10000,100.00' for e in sorted(a.EVENTS))
ok('enabled unscaled counts/runtime',len(a.stats(text,True)['values'])==4)
reject('multiplexed reported runtime rejected',lambda:a.stats(text.replace('100.00','99.99'),True))
reject('fractional scaled count rejected',lambda:a.stats(text.replace('100,,','100.1,,'),True))
reject('missing counter rejected',lambda:a.stats('\n'.join(text.splitlines()[:-1]),True))
ok('disabled zero/not counted permitted',len(a.stats(text.replace('100,,','<not counted>,,'),False)['values'])==4)
reject('disabled positive rejected',lambda:a.stats(text,False))
ok('allocator mode split',a.mode({'command':['build/h4-profile-san']})=='ASan_UBSan' and a.mode({'command':['build/h4-profile']})=='native')
ok('independent affine recurrence',a.recurrence(2862933555777941757,3037000493,3,100000000)=='dcbca4dc3edf4303')
frozen=a.js(a.PIN,'profile-execution-freeze.json')
for name,h in frozen['files'].items():ok('freeze '+name,a.sha(a.raw(a.PIN,name))==h)
contracts=a.js(a.PIN,'profile-commands.json');ok('642 contracts',len(contracts)==642);stats=[c for c in contracts if c['kind'] in ['tree-stat','disabled-stat','known-stat']];ok('42 unscaled counters',len(stats)==42 and all('--no-scale' in c['command'] for c in stats));ok('36 sample contracts',sum('capture_file' in c for c in contracts)==36)
for front in ['primary','h4']:
 for n in [129,100000,1000000]:ok(f'independent score digest {front}/{n}',a.score_digest(front,n)==a.js(a.PIN,'census-score-oracle.json')[f'{front}/{n}'])
print(json.dumps({'status':'PASS','checks':checks,'count':len(checks),'no_runner_or_benchmark_execution':True},indent=2))
