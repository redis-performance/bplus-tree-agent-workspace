from pathlib import Path
import json,hashlib,datetime,os
ROOT=Path.cwd();P=Path(__file__).parent.resolve();SOURCES=ROOT/'scratch/intel-corrected-scan-replication';ACTUAL=ROOT/'scratch/intel-corrected-adapter'
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def check_execution():
 assert os.sched_getaffinity(0)=={2}
 for f,h in json.loads((P/'execution-freeze.json').read_text())['files'].items():assert sha(P/f)==h
 for f,h in json.loads((P/'input-freeze.json').read_text())['files'].items():assert sha(P/f)==h
 assert sha(P/'plan-freeze.json')==json.loads((P/'execution-freeze.json').read_text())['plan_freeze_sha256']
def actual_identity(tag):
 expected=json.loads((P.parent/'013-corrected-adapter-baseline/source-after.json').read_text())['files'];assert sha(P.parent/'013-corrected-adapter-baseline/source-after.json')==json.loads((P/'execution-freeze.json').read_text())['actual_manifest_sha256'];observed={f:sha(ACTUAL/f) for f in expected};assert observed==expected;(P/(tag+'.json')).write_text(json.dumps(dict(status='pass',files=observed,utc=datetime.datetime.now(datetime.timezone.utc).isoformat()),indent=2)+'\n')
def build_identity(tag):
 expected=json.loads((P/'build-freeze.json').read_text());observed={v:{f:sha(SOURCES/v/f) for f in names} for v,names in expected.items()};assert observed==expected;(P/(tag+'.json')).write_text(json.dumps(dict(status='pass',files=observed,utc=datetime.datetime.now(datetime.timezone.utc).isoformat()),indent=2)+'\n')
