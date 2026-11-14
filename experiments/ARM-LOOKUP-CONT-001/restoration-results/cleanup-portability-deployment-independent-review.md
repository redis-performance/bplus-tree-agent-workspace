# Independent cleanup replacement deployment review

**APPROVED: replace the reviewed cleanup bytes at the original basename and start the same bounded generation-bound cleanup service.** This approval authorizes no workload, reservation extension, timer edit or new diagnostic. It does not certify that restoration has completed. No wrapper, remote payload, service or fleet command was executed by this reviewer.

| Bound artifact | SHA256 |
|---|---|
| Final deployment wrapper | `6e79f3de96db4b6b46f55fbef9c9a4465d43976e5f493f78ddb06f01f98cf7b2` |
| Replacement cleanup | `5274d598e52037c2cdd30ab14e654740a3df09671a90859245eacec9b7570a1c` |
| Original cleanup | `115b44d09b7d64ec59c005b4f9c54b0acd8584188594cd182f5d933efb691f1c` |
| Exact first-failed lease | `37b2645a29b57709a1e3fa50a8d6625fae0d5a222ef4685db1e72d72ac8aa9b7` |

The [independent core repair review](cleanup-portability-final-independent-review.md) remains applicable to the unchanged replacement hash, including its 37 passing mocked tests. This separate review covers the deployment wrapper. The original wrapper revision lacked an explicit comparison to the frozen failed-lease hash and a deadline check immediately before service start. Both were corrected in the final hash above; revision0 is retained. No deployment occurred between revisions.

The local wrapper requires an exact structured approval-file hash, APPROVED/schema1, its own exact script hash and the reviewed cleanup payload hash. It explicitly pins the local failed-lease hash before embedding it in the remote payload. The remote payload independently verifies payload bytes, original cleanup bytes and the same exact remote failed lease. It accepts only the unchanged generation/root and the specific prior stop failure with empty restoration proof.

Under the existing exclusive cleanup lock, it checks the saved coordinator is stopped with its original start identity, CPU50 remains offline, the profiler inactive/PID0, and the work unit exactly not-found/inactive/PID0 with empty ControlGroup. Expected work cgroup membership and owned process/container sets must be empty. It checks both release services' exact generation-bound ExecStart and unchanged Type/timeout/KillMode/SendSIGKILL settings; both timer schedules, target services, accuracy and randomized delay remain pinned. The wrapper writes no timer or unit settings.

An exclusive new repair directory prevents overwriting prior backup evidence. Original cleanup and exact failed lease are copied and rehashed; a bounded original release journal is retained before replacement. Immediately before changing the cleanup file, the original cleanup and lease hashes are checked again and time must remain before 07:10 UTC. Replacement uses a same-directory temporary file, file fsync, atomic rename and directory fsync, followed by replacement/unchanged-lease verification. A deployment receipt binds the old/new hashes, verified original backup, approval and observed unit/timer properties. Historical inputs and original failure evidence remain intact.

The lock is released before service start so the cleanup can acquire it. Time is rechecked immediately before invoking `systemctl start --no-block` for the same primary bounded service. Start stdout/stderr/status are recorded and nonzero status propagates; successful start is not treated as successful release. Root must still inspect cleanup completion and independently verify the restored coordinator, CPU, profiler policy/affinities, owned-work absence and timer retirement. The final cleanup's own unchanged-lease and identity checks remain active after launch.

Both local and embedded remote programs parse and compile as Python without execution. Independent AST/order checks confirm exclusive backup creation before replacement, launch outside the lock, and the immediate pre-start deadline gate. These are static wrapper checks, not a mocked end-to-end SSH/deployment run. The review-only check initially matched the retained stop-error string when looking too broadly for systemctl; it was narrowed to the actual start argv, without changing deployment code. No additional source or operation scope was introduced.

The original-basename contract is essential: the locally prepared `cleanup-portability-final.py` is deployed as `cleanup-portability.py`, preserving existing timer commands and same-generation waiter identity. Direct invocation of the local filename is not authorized. Raw operational files remain private; publication must use selected sanitized fields because unrelated Docker records may contain authentication arguments.
