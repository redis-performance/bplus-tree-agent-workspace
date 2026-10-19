# Launch validation

Actual host: Apple M6, arm64; Apple Clang 21.0.0; Python 3.13.15; Codex CLI 0.162.1.
Host capture is in launch-manifest.json. Tree source and referee are unchanged.

- Publication checks: 4 tests passed, including a real bare-remote push, host/source isolation, private-path rejection, staged-change refusal and matching publication acknowledgement.
- Supervisor checks: all 6 real process-control tests passed in 47.796 seconds, covering deadline cleanup, STOP, continuation, usage, campaign isolation and lock protection.
- CLI preflight completed successfully as a model turn. Date/read tools worked; sysctl was denied in the existing workspace-write sandbox. Launcher host capture is authoritative for this run. No permission changes. The launcher runs the original baseline runner outside the worker before startup.
- Preflight usage emitted: 40,367 input tokens, 27,392 cached input tokens, 252 output tokens. Monetary cost and exact backend/model unavailable. Full transcript remains in ignored scratch/.
- Initial unit-test failure used a noncanonical temporary path on macOS; canonicalizing the test root fixed the fixture. No benchmark evidence was produced by that failure.
- Whitespace check passed. Initial real GitHub publication and live worker startup are checked separately by the launcher.

No optimization selected; no source adoption or population-count change.
