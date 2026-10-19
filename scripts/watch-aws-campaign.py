#!/usr/bin/env python3
"""Publish small main-branch AWS progress snapshots from completed host commits.

Run in a dedicated clean checkout; private controller paths/config remain in scratch.
Does not merge host candidates, publish private logs, or change runner state.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import time


def run(command, cwd):
    result = subprocess.run(command, cwd=cwd, text=True, capture_output=True, timeout=120)
    if result.returncode:
        raise RuntimeError(f'{command[:3]} failed: {result.stderr[-300:]}')
    return result.stdout.strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--controller', type=Path, required=True)
    parser.add_argument('--checkout', type=Path, required=True)
    parser.add_argument('--deadline', required=True)
    args = parser.parse_args()
    end = datetime.fromisoformat(args.deadline).timestamp()
    configs = [json.loads((args.controller/'scratch'/f'aws-{name}-launch.json').read_text())
               for name in ('intel', 'amd', 'arm')]
    previous = None
    final_since = None
    while True:
        run(['git','fetch','origin'], args.checkout)
        records = []
        for config in configs:
            runtime = args.controller/config['worktree']/config['runtime_dir']/'status.json'
            status = json.loads(runtime.read_text()) if runtime.exists() else {'status':'starting','rounds':[]}
            native = args.controller/config['worktree']/config['campaign_dir']/'NATIVE-STATUS.json'
            native_status = json.loads(native.read_text()) if native.exists() else None
            sync = args.controller/'scratch'/f"{config['host_label']}-launch-sync-status.json"
            publication = json.loads(sync.read_text()) if sync.exists() else {}
            branch_commit = run(['git', 'rev-parse', 'origin/' + config['branch']], args.checkout)
            records.append(dict(host=config['host_label'], state=native_status.get('status', 'running') if native_status else status['status'],
                rounds=sum(r['status'] != 'running' for r in status['rounds']),
                publication='native worker commits' if native_status else publication.get('status', 'pending first completed round'),
                head=branch_commit,
                branch=config['branch'], path=config['campaign_dir']))
        fingerprint = hashlib.sha256(json.dumps(records, sort_keys=True).encode()).hexdigest()
        if fingerprint != previous:
            run(['git','merge','--ff-only','origin/main'], args.checkout)
            stamp = datetime.now(timezone.utc).isoformat()
            text = '# AWS worker publication status\n\nUpdated '+stamp+'. Deadline08:00UTC /09:00Lisbon.\n\n'
            text += '| Host | Worker | Historical CLI rounds | Publication | Latest evidence |\n|---|---|---:|---|---|\n'
            for record in records:
                url = 'https://github.com/redis-performance/bplus-tree-agent-workspace/blob/'+record['branch']+'/'+record['path']
                text += f"| {record['host']} | {record['state']} | {record['rounds']} | {record['publication']} `{record['head'][:8]}` | [Status]({url}/STATUS.md), [activity]({url}/ACTIVITY.md), [handoff]({url}/HANDOFF.md) |\n"
            text += '\nDetached CLI launchers failed before shell execution (bwrap uid-map failure) and were stopped. Native session agents continue via already-available authorized tools; no permission settings changed. Historical CLI usage is separate from native-agent usage, which is unknown.\nRaw results, decisions and losing patches are retained on each host branch.\nNo baseline source change or cross-host pooled performance claim is made here.\n'
            if re.search(r'/home/|\.pem|\b(?:\d{1,3}\.){3}\d{1,3}\b', text):
                raise RuntimeError('private-detail guard')
            dest=args.checkout/'experiments/NIGHT-EXPLORATION-001/AWS-WORKERS.md'
            dest.write_text(text)
            readme=args.checkout/'README.md'
            body=readme.read_text()
            block='''<!-- AWS-NIGHT-START -->
The **AWS Intel, AMD and Graviton campaign** is bounded to **19 October,
09:00 Lisbon / 08:00 UTC**. [Baselines and plan](experiments/NIGHT-EXPLORATION-001/AWS-STATUS.md),
[live workers and activity](experiments/NIGHT-EXPLORATION-001/AWS-WORKERS.md).
Each host publishes its completed decisions and evidence on a separate branch.
Source adoption remains NONE.
<!-- AWS-NIGHT-END -->'''
            body=re.sub(r'<!-- AWS-NIGHT-START -->.*?<!-- AWS-NIGHT-END -->',lambda m:block,body,flags=re.S)
            readme.write_text(body)
            activity=args.checkout/'experiments/NIGHT-EXPLORATION-001/AWS-ACTIVITY.md'
            with activity.open('a') as stream:
                stream.write('\n- '+stamp+': '+ '; '.join(f"{r['host']} {r['state']}, {r['rounds']} rounds, publication {r['publication']}" for r in records)+'.\n')
            run(['git','add','README.md','experiments/NIGHT-EXPLORATION-001/AWS-WORKERS.md','experiments/NIGHT-EXPLORATION-001/AWS-ACTIVITY.md'], args.checkout)
            run(['git','commit','-m','Refresh AWS overnight worker status and activity'], args.checkout)
            # Another session may publish main; incorporate it without overwriting edits.
            run(['git','pull','--rebase','origin','main'], args.checkout)
            run(['git','push','origin','HEAD:main'], args.checkout)
            previous=fingerprint
            print(stamp+' published worker status',flush=True)
        final = all(r['state'] not in ('running','starting') for r in records)
        if final:
            final_since = final_since or time.time()
        else:
            final_since = None
        if time.time()>end+300 or (final_since and time.time()-final_since>90):
            break
        time.sleep(30)


if __name__=='__main__':
    main()
