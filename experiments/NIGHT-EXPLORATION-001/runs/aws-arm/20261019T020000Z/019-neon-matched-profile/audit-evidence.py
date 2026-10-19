#!/usr/bin/env python3
"""Additive loss/serial/identity audit; frozen profile/parser remain unchanged."""
from pathlib import Path
import datetime,json,re,hashlib,collections
p=Path(__file__).resolve().parent;d=p/'profiles';m=json.loads((d/'result.json').read_text());f=json.loads((p/'plan-freeze.json').read_text());last=None
assert m['status']=='complete'and len(m['commands'])==52 and len(m['captures'])==12 and m['identity_before']==m['identity_after']
for a in m['commands']:
 assert a['returncode']==0
 start=datetime.datetime.fromisoformat(a['started_utc']);end=datetime.datetime.fromisoformat(a['finished_utc']);assert start<=end
 if last:assert last<=start
 last=end
 assert (d/(a['name']+'.stdout')).is_file()and(d/(a['name']+'.stderr')).is_file()
for name,h in f['inputs_sha256'].items():assert hashlib.sha256((p/name).read_bytes()).hexdigest()==h
loss=[];stderr=[]
for a in m['captures']:
 name=f"{a['variant']}-n{a['size']}-s{a['seed']}";s=(d/(name+'-report.stdout')).read_text();x=re.findall(r'^# Total Lost Samples: (\d+)$',s,re.M);assert len(x)==1;loss.append(dict(capture=name,reported_lost_samples=int(x[0])))
for file in sorted(d.glob('*.stderr')):
 s=file.read_text()
 if s.strip():stderr.append(dict(file=file.name,text=s))
rows=json.loads((p/'analysis/capture-summary.json').read_text());scopes=collections.Counter()
for row in rows:
 for k,v in row['scopes'].items():scopes[k]+=v['events']
r=dict(status='pass',commands=52,executions=28,captures=12,serial_commands=True,pre_post_identity_equal=True,frozen_inputs_unchanged=True,loss_reports=loss,reported_lost_samples_total=sum(x['reported_lost_samples']for x in loss),nonempty_stderr=stderr,unfiltered_sample_events=sum(x['events']for x in rows),sample_scope_events=dict(scopes),limits='Reported loss is what perf reports, not proof of perfect sampling. Incomplete and other stacks are retained; filtering scopes analysis only.')
(p/'analysis/evidence-audit.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
