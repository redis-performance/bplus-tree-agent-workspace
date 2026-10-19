"""Read-only artifact identity check after a phase; never rebuilds or runs workloads."""
from pathlib import Path
import argparse,json,hashlib,datetime,sys
p=argparse.ArgumentParser();p.add_argument('--freeze',type=Path,required=True);p.add_argument('--sources',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--variants',default='base,B');a=p.parse_args();assert not a.out.exists();expected=json.loads(a.freeze.read_text());result=dict(started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),command=sys.argv,expected_manifest=str(a.freeze),expected_manifest_sha256=hashlib.sha256(a.freeze.read_bytes()).hexdigest(),sources=str(a.sources),observed={},mismatches=[])
for v in a.variants.split(','):
 result['observed'][v]={}
 for file,h in expected[v].items():
  f=a.sources/v/file;actual=hashlib.sha256(f.read_bytes()).hexdigest();result['observed'][v][file]=actual
  if actual!=h:result['mismatches'].append(dict(variant=v,file=file,expected=h,observed=actual))
result.update(finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='pass' if not result['mismatches'] else 'fail',read_only=True,no_workload_executed=True);a.out.write_text(json.dumps(result,indent=2)+'\n');assert result['status']=='pass',result['mismatches'];print('PASS post-phase artifact hashes',sum(len(x) for x in result['observed'].values()))
