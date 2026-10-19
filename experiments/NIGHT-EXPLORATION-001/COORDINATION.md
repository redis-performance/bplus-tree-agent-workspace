# M1 publication and M6 decision checks

## M6 driver, 19 October

The user authorized M6 execution and ongoing publication through 09:00 Lisbon.
Branch: `exploration/apple-m6-mini-20261019T013000Z`. Follow its
[STATUS.md](runs/apple-m6-mini/20261019T013000Z/STATUS.md) and exact candidate/harness
hashes before spending M1 time on the same hypothesis. No M6 decision means UNKNOWN.

The generalized coordinator supports the M6 checkout and M1 worktrees. The M6 worker
requests publication at every status/decision milestone through an atomic runtime
`publish-request.json` containing a unique `id` and exact additional harness `paths`.
The worker pauses experiments and Git writes until a matching successful
`publish-ack.json` records the pushed revision. This makes publication a boundary
between measurements. The coordinator also publishes each completed round. It
includes the host evidence, experiment ledgers, README and shared memory; requested
paths cannot stage source, the original test entry point or another host campaign.
Only the coordinator writes commits/pushes on this host. No main pushes or merges.

Local runtime checks:

```sh
cat scratch/m6-night-launch-sync-status.json
cat scratch/night-apple-m6-mini-20261019T013000Z/status.json
git ls-remote --heads origin 'refs/heads/exploration/apple-m6-mini-*'
```

## Existing M1 coordinator

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
