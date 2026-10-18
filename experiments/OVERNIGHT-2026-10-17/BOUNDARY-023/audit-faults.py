from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parent;R=P.parents[2];rows=json.loads((P/'faults/manifest.json').read_text());out=[]
for row in rows:
 run=row['runs'][-1];stderr=P/'faults'/(row['name']+'-run.stderr');text=stderr.read_text();assert hashlib.sha256(stderr.read_bytes()).hexdigest()==run['stderr_sha256']
 assert row['runs'][0]['returncode']==0 and run['returncode']==-6
 if row['name']=='decode-wide-as-narrow':
  assert text=='tests/../src/zset_btree.c:4199: count != 0\n'
  src=(R/row['snapshot']/'src/zset_btree.c').read_text().splitlines();assert src[4198].strip()=='serverAssert(count != 0);'
  assert '#define serverAssert(x) do { if (!(x)) standalone_panic(__FILE__, __LINE__, #x); } while (0)' in (R/row['snapshot']/'compat/server.h').read_text()
 out.append(dict(name=row['name'],original_classifier=row['outcome'],audited_outcome='detected',returncode=run['returncode'],stderr=text))
(P/'faults/audit.json').write_text(json.dumps(dict(status='pass',method='read-only source/adapter/stderr audit; no rerun or test change',results=out),indent=2)+'\n')
print('PASS: both faults aborted; width fault hit production assertion; original classifier error retained')
