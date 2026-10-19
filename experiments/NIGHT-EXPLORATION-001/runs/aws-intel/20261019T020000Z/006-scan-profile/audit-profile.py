from pathlib import Path
import csv,json,collections,re,runpy,datetime
p=Path(__file__).parent
runpy.run_path(str(p/'audit-gnu-profile.py'))
(p/'gnu-profile-audit.json').write_bytes((p/'profile-audit.json').read_bytes())
base=json.loads((p/'mapping-command.json').read_text())['linker_base']
llvm={int(x['Address'],16)-base:x['Symbol'] for x in json.loads((p/'llvm-inline-map.json').read_text())}
prior=json.loads((p/'gnu-profile-audit.json').read_text());records=[];aggregate={}
for n in [100000,1000000]:
 a=dict(captured=0,tagmatches=0,scan_slot=0,helper_direct_source_lines=0,captures=0);aggregate[str(n)]=a
 for seed in [1,2,3]:
  tag=f'scan-{n}-seed{seed}';hist={int(r['offset']):int(r['count']) for r in csv.DictReader((p/'profiles'/(tag+'.hist.csv')).open())};counts=collections.Counter();direct=0
  for offset,count in hist.items():
   symbols=llvm[offset]
   for name in {s['FunctionName'] for s in symbols}:counts[name]+=count
   if any(s['FileName'].endswith('/src/zset_btree.c') and 4129<=s['Line']<=4153 for s in symbols):direct+=count
  total=sum(hist.values());a['captured']+=total;a['tagmatches']+=counts['zbtLeafTagMatches'];a['scan_slot']+=counts['zbtIndexScanSlot'];a['helper_direct_source_lines']+=direct;a['captures']+=1
  records.append(dict(tag=tag,captured=total,tagmatches_pct=100*counts['zbtLeafTagMatches']/total,inclusive_inline_samples=dict(counts),direct_helper_line_samples=direct))
for a in aggregate.values():
 a['tagmatches_pct']=100*a['tagmatches']/a['captured'];a['scan_slot_pct']=100*a['scan_slot']/a['captured'];a['materially_present']=a['tagmatches']>=10 and a['tagmatches_pct']>=5
elapsed=0
for name in ['scan-diagnostic','scan-diagnostic-resume','scan-symbolize']:
 j=json.loads((p/(name+'.sh.job.json')).read_text());elapsed+=(datetime.datetime.fromisoformat(j['finished_utc'])-datetime.datetime.fromisoformat(j['started_utc'])).total_seconds()
assert elapsed<300
hashes=(p/'build-sha256.txt').read_text().splitlines();assert hashes[0].split()[0]=='d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2'
result=dict(status='pass',captures=6,serial_process_windows=15,aggregate_helper_seconds=elapsed,scope=prior['scope'],denominator=prior['denominator'],mapping='LLVM18 inline frames; GNU mapping retained separately and omits this helper name',aggregate=aggregate,records=records)
(p/'profile-audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(aggregate,indent=2))
