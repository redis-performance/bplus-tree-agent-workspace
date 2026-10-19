@../AGENTS.md

Shared rules and state live in AGENTS.md and .workspace-memory/. The prompts in skills/
are backend-neutral; actual agent/model choices belong in each experiment record.

Every Claude investigation/optimization session must use the `cpu-perf` MCP from
[CPU Performance Engineering](https://github.com/usamahz/cpu-performance-engineering),
as required by AGENTS.md and [the shared workflow](../docs/PERFORMANCE-MCP.md).
Check availability/library coverage, consult it on the actual investigation, and
log calls, findings and limits. This requirement also applies to Codex sessions.
