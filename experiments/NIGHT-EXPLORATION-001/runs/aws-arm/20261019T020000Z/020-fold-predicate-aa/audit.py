from pathlib import Path
import csv,datetime,hashlib,json
p=Path(__file__).resolve().parent;m=json.loads((p/'aa.json').read_text());schedule=json.loads((p/'schedule.json').read_text());f=json.loads((p/'comparison-freeze.json').read_text());assert hashlib.sha256((p/'schedule.json').read_bytes()).hexdigest()==f['schedule_sha256'];rows=m['rows'];assert len(rows)<=48;last=None;complete=m['status']=='complete'
for i,r in enumerate(rows):
 for k,v in schedule[i].items():assert r[k]==v
 assert list(csv.DictReader((p/'raw'/f'aa-{i:03d}.stdout').open()))==[r['row']];assert not(p/'raw'/f'aa-{i:03d}.stderr').read_text();a=m['attempts'][i];assert a['returncode']==0
 expected=['scratch/arm-corrected-scan/base/build/btree-bench','--case','scan','--size',str(r['size']),'--ops','5000000','--member-bytes','16','--seed',str(r['seed'])];assert r['command']==a['command']==expected
 assert r['row']['cpu_start']==r['row']['cpu_end']=='2';assert r['row']['case']=='scan'and int(r['row']['size'])==r['size']and int(r['row']['seed'])==r['seed']and r['row']['requested_ops']=='5000000'and r['row']['member_bytes']=='16'
 start=datetime.datetime.fromisoformat(r['started_utc']);end=datetime.datetime.fromisoformat(r['finished_utc']);assert start<=end
 if last:assert last<=start
 last=end
effects=[]
for i in range(0,len(rows)-3,4):
 rr=rows[i:i+4];assert len({tuple(x['row'][k]for k in ['checksum','operations','tree_bytes','traversals','warmup_passes','size','seed','member_bytes'])for x in rr})==1
 ns=[int(x['row']['elapsed_ns'])/int(x['row']['operations'])for x in rr];effect=100*((ns[1]+ns[2])/(ns[0]+ns[3])-1);minimum=min(int(x['row']['elapsed_ns'])for x in rr);effects.append(dict(size=rr[0]['size'],seed=rr[0]['seed'],block=rr[0]['block'],percent=effect,min_window_ns=minimum,qualified=abs(effect)<=1 and minimum>=10000000))
if complete:assert len(rows)==len(m['attempts'])==48 and effects==m['effects']
summary=[]
for n in [100000,1000000]:
 rr=[x for x in effects if x['size']==n];summary.append(dict(size=n,blocks=len(rr),qualified=complete and len(rr)==6 and all(x['qualified']for x in rr),effects=[x['percent']for x in rr],minimum_window_ns=min([x['min_window_ns']for x in rr],default=None)))
a=dict(status='pass',phase_status=m['status'],rows=len(rows),blocks=len(effects),schedule_exact_prefix=True,serial=True,paired_fixtures_output_owned_memory_equal=True,summary=summary,source_adoption='NONE',limits='Fresh baseline controls for a potential distinct hypothesis. No rescue of rejected017 or failed original8fab controls; no candidate measured.')
(p/'aa-audit.json').write_text(json.dumps(a,indent=2)+'\n');print(json.dumps(a,indent=2))
