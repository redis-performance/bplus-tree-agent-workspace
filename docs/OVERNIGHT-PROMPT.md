# Overnight experiment worker

The user explicitly requested: "continue experimeting. loop over the entire night".
This continues the standalone B+ tree work in this repository. Local microbenchmarks
and use of the CPU Performance Engineering MCP are authorised. Work until the bounded
round deadline; another fresh worker resumes from your saved evidence and handoff.

Read AGENTS.md, all three shared memory files, docs/POPULATION.md and
experiments/OVERNIGHT-2026-10-17/PLAN.md first. Do useful experimental work now.
Do not just describe a plan, wait out the night, or repeat identical failed trials.
The campaign ends at 2026-10-18 08:00 Europe/Lisbon (07:00 UTC).

## Work queue and evidence

1. Start with a separate harness change: improve duration and scheduling observability.
   Consult cpu_perf.ask, then the methods/code of benchmarks 05-measurement-pitfalls
   and 14-pcore-vs-ecore. Prior broad ask retrieval was irrelevant; do not cite that
   output as support. Inspect local APIs before adopting code. Add thread CPU time,
   boundary CPU IDs where supported, actual QoS, and repeated iterator/scan traversals
   with accurate effective counts/checksums. Preserve meaningful checks. Longer
   fixed operation counts and explicit settling are options, not assumed cures.
   Do not transfer M4 Pro CPU numbering, frequencies or measurements to this M1.
2. Freeze the harness, preregister an affordable targeted A/A qualification, then run
   it serially. Use wall time as the primary metric; thread time and CPU IDs explain
   scheduling but do not prove stable frequency or exclude within-window migration.
   Select blocks/counts before observing outcomes. Preserve all raw rows and failures;
   no optional stopping, outlier removal or thresholds changed after measurement.
   Clock/frequency remain unknown unless measured by a defensible method.
3. If qualification permits meaningful comparisons, execute both population stages
   exactly as docs/POPULATION.md requires: three separate proposals and a chair, then
   three isolated implementations of one selected hypothesis and measured selection.
   Baseline profiles in EXP-001 show short-key leaf memchr and long-key SipHash hot;
   these are evidence, not predetermined winners. Use agents if available under
   AGENTS.md. Otherwise explicitly label sequential passes as not independent agents.
   All agents must be idle during measurement. Never fabricate agent/model/token data.
4. Correctness, sanitizers, serial same-session ABBA, unchanged memory guards, profile
   explanation, fresh seeds/confirmation and adversarial review remain required.
   A large exploratory gain can motivate more work; it cannot bypass a failed gate.
   Preserve losing patches. Keep all source candidates in isolated copies/worktrees
   and preserve the main source baseline until a separate morning review.
5. When noise blocks acceptance, PARK that claim and use time for a new, preregistered
   diagnostic: duration/fixture coverage, clock/placement, source inspection, stronger
   boundary tests or a different profiled bottleneck. Do not rerun the same analysis
   indefinitely. Finish the final round with a readable morning report, not a new trial.

## Execution boundaries

- Single coordinator; one benchmark/profile at a time. No builds, tests or local agent
  computation overlapping measured runs. Limit individual benchmark children to 120s
  unless a larger bounded duration is justified beforehand. No detached processes.
- The runner has workspace-write sandbox and existing configuration. Never change
  permission settings, disable hooks, use bypass flags, or retry denied actions with
  greater permissions. Do not inspect private SSH/cloud credentials or other repos.
- No network publishing, git pushes, upstream PRs/comments, releases or messages to
  others. Keep drafts local. Git metadata may be protected: if commit/worktree creation
  is denied, record it once and use isolated file snapshots beneath scratch/ instead.
  Freeze exact base commit plus SHA256 files and saved patches; label uncommitted
  provenance explicitly. Commit-based acceptance remains pending morning review.
- Do not modify scripts/overnight.py, this prompt, the supervisor's runtime files,
  deadline, STOP file, or another worker's existing results. Read status/reports only.
- Do not delete/reset user edits or overwrite evidence. Create a fresh run directory
  per trial. Leave credentials/private paths/full agent transcripts under ignored
  scratch/ only. Curate public summaries without private hostnames or machine paths.
- Update experiments/EXPERIMENTS.md, experiments/SUMMARY.md, README counts and shared
  memory on every actual decision. Separate harness/baseline work from optimisation
  counts. Save patches, exact commands, stdout, stderr, checksums and source hashes.
- Use the existing CPU Performance Engineering MCP when relevant; it is available.
  Consult its evidence checker before headline claims. Respect attribution and unknowns.
- Check remaining wall time before lengthy commands. Save progress continuously. At
  least 90 seconds before your deadline, stop starting work and write the handoff.
- If infrastructure blocks every useful action, write the concrete blocker in your
  report and create experiments/OVERNIGHT-2026-10-17/BLOCKED.md explaining what can
  resume it. Do not invent results or burn repeated rounds on the same denied action.

End with: completed work, commands/tests and their outcomes, evidence locations,
decisions (including NONE/PARK), remaining uncertainty, and the next concrete action.
Report exact backend/model only if visible; otherwise unknown. The supervisor records
actual CLI token usage separately. The final round should write
experiments/OVERNIGHT-2026-10-17/MORNING-REPORT.md.
