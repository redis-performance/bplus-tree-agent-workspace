# Independent operations correction review

**Both findings from5af5fdc6d are resolved in the reviewed bytes. No static acquisition/release blocker remains from this review. Lease NOT_ACQUIRED.** This does not grant acquisition or a workload; root still waits for the concrete independently reviewed diagnostic freeze.

The generated script now captures container enumeration, owned-unit enumeration, supervisor PID and helper-hash queries in standalone assignments whose exit status is checked by errexit/pipefail before interpreting their output. Both container checks and the unit check require a successfully returned empty result. Thus empty stdout from a failed query no longer passes as an absence proof.

Release records the stop return code, then requires a successful separate ActiveState query and exact `inactive` result before restarting the coordinator. A failed stop is tolerable only when that independent query confirms inactivity; query failure or active state aborts and preserves the error, rather than pretending owned work has stopped. Root must still inspect any failed release and obtain fresh live proof; this code review is not restoration evidence.

The public11-case stub test exercises the exact generated query/release check text. It covers successful empty/nonempty and failing-empty container/unit queries, inactive/active release states, failed stop with confirmed inactivity, query failure and combined stop/query failure. Its results are bound to the exact generated acquisition hash and all11 outcomes match their expected pass/fail behavior. I inspected these tests/results, verified their hash binding and parsed source; I did not rerun them or execute the lease/preparer/auditor.

Timer-before-stop ordering, ERR restoration trap, distinct front namespace, preserved prior leases, fresh saved/live coordinator PID, marker recency and recursive cgroup/error checks remain as previously reviewed. Independent11:45UTC timer and current helper hashes remain bound; any later script, deadline or namespace change needs a new binding. The initial rejected script hashes/findings remain preserved, and generic aliases keep all private paths/connection details out of this report.

See OPERATIONS-CORRECTION-REVIEW.json for exact input/release-body hashes. No SSH, service mutation, profiling, measurement or target-code change. Prior candidate REJECT/source NONE unchanged. Reviewer/root/aws_amd; inherited model/token/USD unknown. Available for the subsequent ARM030 concrete protocol review.
