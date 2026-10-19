#!/usr/bin/env python3
"""Offline pinned Git-object/tar receipt audit. No extraction or native workload."""
from pathlib import Path
from collections import Counter
from datetime import datetime
import csv,hashlib,io,json,math,re,signal,subprocess,tarfile,time
E=Path(__file__).resolve().parent
sha=lambda x:hashlib.sha256(x).hexdigest()
def gitshow(spec):
 p=subprocess.run(['git','show',spec],capture_output=True,timeout=30);assert p.returncode==0;return p.stdout
def expire(*args):raise TimeoutError('180-second receipt audit bound')
def main():
 signal.signal(signal.SIGALRM,expire);signal.alarm(180);t=time.monotonic()
 receipt=json.loads((E/'RECEIPT.json').read_text());commit=receipt['commit'];roundaudit=json.loads((E/'inputs/ROUND-003-AUDIT.json').read_text());declared=json.loads((E/'inputs/005-decode/AUDIT.json').read_text())
 result=dict(status='RUNNING',participant='/root/followup_proposal_a',backend='Inherited Codex/GPT-6 family; exact serving model/token/currency costs unknown',commit=commit,archive_extraction=False,native_workloads=0,read_only_git_metadata=True,copied_docs={},sources={},phases={})
 try:
  metadata=subprocess.run(['git','show','-s','--format=%cI',commit],capture_output=True,timeout=30);assert metadata.returncode==0 and datetime.fromisoformat(metadata.stdout.decode().strip())==datetime.fromisoformat(receipt['commit_utc'])
  for name,item in receipt['files'].items():
   data=gitshow(commit+':'+item['git_path']);assert sha(data)==item['sha256'] and data==(E/'inputs'/name).read_bytes();result['copied_docs'][name]=sha(data)
  for path,digest in receipt['source_sha256'].items():
   assert sha(gitshow(commit+':'+path))==digest;result['sources'][path]=digest
  totaloutputs=totalrows=0
  for phase,entry in receipt['archive_git_blobs'].items():
   data=gitshow(commit+':'+entry['git_path']);assert sha(data)==entry['sha256'] and len(data)==entry['bytes']
   key='aa' if phase=='aa' else phase[-1];assert roundaudit['decode_phase_status'][key]['archive_sha256']==sha(data) and declared[key]['archive_sha256']==sha(data)
   files=0;rows=0;stderr=0;cells=set();process_indices=set();groups=Counter();minimum=float('inf');maximum=0;maximum_minimum=0;blankcounters=True;allshort=True
   with tarfile.open(fileobj=io.BytesIO(data),mode='r:gz') as tar:
    names=set()
    for member in tar:
     assert member.isfile() and member.name not in names;names.add(member.name)
     name=Path(member.name);assert not name.is_absolute() and '..' not in name.parts
     contents=tar.extractfile(member).read()
     if member.name.endswith('.stderr'):stderr+=1;continue
     match=re.fullmatch(r'(\d+)-b(\d+)-w(\d+)-r([01])-n(\d+)-([AB])\.csv',member.name);assert match,member.name
     index,block,width,reverse,count=map(int,match.groups()[:5]);side=match[6];assert index not in process_indices;process_indices.add(index)
     cell=(width,reverse,count);cells.add(cell);groups[(block,*cell,side)]+=1
     samples=list(csv.DictReader(io.StringIO(contents.decode())));assert len(samples)==129 and [int(r['sample']) for r in samples]==list(range(129))
     process_min=float('inf')
     for r in samples:
      assert r['kind']=='time' and (int(r['width']),int(r['reversed']),int(r['count']))==cell
      elapsed=float(r['elapsed_ns']);assert math.isfinite(elapsed) and elapsed>0
      minimum=min(minimum,elapsed);maximum=max(maximum,elapsed);process_min=min(process_min,elapsed);allshort=allshort and elapsed<10000000
      assert int(r['operations'])==int(r['leaves'])*int(r['rounds'])*count
      blankcounters=blankcounters and r['cycles']=='' and r['instructions']==''
     maximum_minimum=max(maximum_minimum,process_min);files+=1;rows+=len(samples)
   expected={(w,r,n) for w in [0,8,57,59,60,63,64] for r in [0,1] for n in [1,2,4,16,96]}
   assert cells==expected and len(cells)==70 and process_indices==set(range(1680)) and files==stderr==1680 and rows==216720
   assert groups==Counter({(b,*cell,side):2 for b in range(6) for cell in expected for side in ['A','B']})
   assert allshort and blankcounters
   assert declared[key]['processes']==files and declared[key]['rows']==rows and declared[key]['cells']==70 and declared[key]['qualified_cells']==0
   assert abs(declared[key]['minimum_window_ms']-minimum/1000000)<1e-12 and abs(declared[key]['maximum_process_min_window_ms']-maximum_minimum/1000000)<1e-12
   result['phases'][phase]=dict(archive_sha256=sha(data),archive_bytes=len(data),process_outputs=files,stderr_outputs=stderr,sample_rows=rows,cells=70,blocks_per_cell=6,samples_per_process=129,all_sample_windows_below_10ms=allshort,minimum_ns=minimum,maximum_ns=maximum,maximum_process_minimum_ns=maximum_minimum,cycles_and_instructions_blank=blankcounters)
   totaloutputs+=files;totalrows+=rows
  assert totaloutputs==roundaudit['decode_total_processes']==receipt['m1_processes']==6720 and totalrows==roundaudit['decode_total_rows']==receipt['m1_sample_rows']==866880
  result.update(status='PASS_WITH_PROVENANCE_WORDING_FINDING',copied_doc_count=9,source_identity_count=5,archive_count=4,total_process_outputs=totaloutputs,total_csv_sample_rows=totalrows,aa_cells=70,aa_qualified_cells_under_10ms_gate=0,decision='M1 PARK/source NONE; no tree speedup or acceptance',m1_adapter='legacy79b3/adf0; distinct from current corrected M6 468a/c923',limits=['Reconstructed archive counts/coverage/window bounds and pins; did not independently recompute all candidate effect statistics or prove serial UTC/returncodes absent from these archives.','Native/sanitizer1040-cell and8-selftest claims are reported prior evidence, not rerun here.','Nine total M1 populations and same-worker sequential local rank/decoder passes verified from copied docs; receipt all-nine-sequential classification is not supported by these docs and conflicts with the inherited actual-agent populations.','Newly observed publication of an01:46UTC commit does not prove current runner liveness or M6 consumption; DNS unknown is historical M1-reported state.'],audit_wall_seconds=time.monotonic()-t)
 except BaseException as ex:result.update(status='FAIL',error_type=type(ex).__name__,error=str(ex));raise
 finally:
  signal.alarm(0);result['script_sha256']=sha(Path(__file__).read_bytes());(E/'INDEPENDENT-RECEIPT-A.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:result[k] for k in ['status','total_process_outputs','total_csv_sample_rows','aa_cells','aa_qualified_cells_under_10ms_gate']}))
if __name__=='__main__':main()
