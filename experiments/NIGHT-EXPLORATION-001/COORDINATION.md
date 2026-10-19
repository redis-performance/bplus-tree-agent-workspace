# M1 publication and M6 decision checks

M1 runs in a clean Git worktree on its own branch. Its workspace-write worker
cannot create the worktree's Git index lock; it saves exact evidence and patches
under the host campaign directory and records the denial once. The host coordinator
runs [sync-night-campaign.py](../../scripts/sync-night-campaign.py) outside that
sandbox. After every completed supervisor round it stages the host campaign
evidence and the shared README/experiment logs, commits, and pushes the M1 branch. It refuses obvious credential/private
path strings and stops on a publication failure. No force push or main-branch merge.
The coordinator's status file is in ignored `scratch/` alongside the launch config.

Before a candidate trial, the worker checks the remote for M6 host branches and
reads the newest published M6 decision. It records the exact branch/commit/time and
skips an idea that M6 has explicitly discarded. An absent/unpublished M6 decision
is UNKNOWN, so M1 may continue provisional exploration. Every M1 result stays
labeled Apple M1; M6 data is never pooled into its comparison.

To check publication and supervisor status from the original checkout:

```sh
cat scratch/m1-night-launch-sync-status.json
cat worktrees/night-m1-RUNID/scratch/night-apple-m1-RUNID/status.json
git ls-remote --heads origin 'refs/heads/exploration/apple-*'
```

Replace RUNID using `scratch/m1-night-launch.json`. The coordinator exits after
the supervisor. The supervisor STOP file remains the sole supported early stop.
