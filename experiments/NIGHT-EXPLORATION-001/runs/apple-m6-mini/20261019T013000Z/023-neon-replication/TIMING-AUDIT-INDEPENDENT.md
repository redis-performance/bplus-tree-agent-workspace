# Independent offline timing auditor

Prepared only: `timing-audit-independent.py` has been AST-parsed, not executed. It never imports `timing.py`, invokes a subprocess, builds, profiles or runs a native workload. Root invokes it after a phase completes:

`PYTHONDONTWRITEBYTECODE=1 python3 <023>/timing-audit-independent.py --phase aa --ack <same-AA-authorization>`

Use `--phase discovery` and its corresponding authorization only if a complete independently qualified AA permits discovery. The audit writes new `independent-audit.json` and `independent-audit-seal.json` under the completed phase directory, refusing to overwrite an existing report. Its own offline alarm is 180 seconds. Failures preserve a partial report and all existing raw evidence.

The expected schedule is independently constructed before reading the stored schedule or summaries: six blocks; seeds 401/402/403 twice; alternating 100K/1M size order; baseline/base-only AA or rotating A/B/C discovery order; ABBA positions; exact 5M requested operations, 16-byte members and one warmup pass. Expected counts are 48 AA and 144 discovery processes. Every journal command and fixed environment must match.

The audit reads every raw CSV/stderr through its recorded byte length and SHA-256, checks there are no unaccounted raw files, reconstructs exact semantic fingerprints including actual duplicate SCAN callbacks, and checks original header/numeric/checksum/traversal/owned-byte/rounded-rate contracts. It derives every block from integer elapsed sums. AA uses `abs(Bsum-Asum)*100 <= Asum`; primary uses `Bsum*100 <= Asum*98`; every window must be at least 10,000,000 ns. Failed AA controls stay in the report. Published rows/blocks/status are cross-checks, not statistical inputs. Discovery fixture identities must match the independently audited qualifying AA.

It verifies authorization/freeze/schedule/source/binary identities, the successful validation snapshots, all original source-manifest hashes and produced native binaries, serial recorded UTC intervals, direct reaping/group cleanup, per-child/phase/absolute bounds, and pre/post frozen/raw hashes. It does not infer actual core residency or frequency from CPU endpoint fields. A PASS raw audit is separate from AA qualification, primary selection, full guards, independent fresh confirmation, profile validation and acceptance.

Participant `/root/followup_proposal_a`; inherited Codex/GPT-6 family, exact serving model/token/currency costs unknown. No native execution or timing has been performed by this preparation. Root owns invocation and launch decisions; no shared status or Git edits.
