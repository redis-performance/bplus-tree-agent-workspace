# H6 supplemental descriptor guards

Provisional revision 0 is ready for independent review and controller freeze. It has not been qualified or measured on the fleet. See [PROTOCOL.md](PROTOCOL.md) for the exact fixture, four cases, provisional counts and unchanged acceptance gates.

Local correctness completed: 384 cells against frozen baseline and H6-A/B/C, native plus ASan/UBSan, seeds 17/29/43 and 1/2/5/8 sweeps. Every cell passed; the independent Python oracle checked all 384 checksum rows. All four sources have identical logical results and memory endpoints within a build mode: native 86,008 bytes; sanitizer 85,267 bytes. Before, immediate-after and post-validation endpoints agree in these short correctness runs. These are allocator-specific correctness observations, not a fleet memory qualification or duration estimate.

From the repository root, reproduce correctness only:

```sh
python3 experiments/ARM-LOOKUP-CONT-001/descriptor-guards/verify.py
python3 experiments/ARM-LOOKUP-CONT-001/descriptor-guards/check_oracle.py
```

`verify.py` builds the current frozen baseline plus isolated H6-A/B/C sources and executes only `verify` mode, which does not read a clock. Exact source/referee/binary hashes, compiler identity and build invocations are in [correctness-manifest.json](correctness-manifest.json). All 384 invocation arguments, return codes, stdout/stderr and build logs are retained under `correctness/`. `local/` contains ignored correctness binaries. The manifest's source identities must match the intended candidate freeze; changing any source requires fresh correctness and identity records before fleet use.

The initial shell-case terminator error, which prevented compilation, is preserved under `failed-attempts/build-case-terminator/`. No performance attempt occurred. No original fixture, existing guard, candidate source or timing controller was changed.

This author implemented H6-A. Independent harness review and independent candidate review remain required. Externally stored short records, forced collisions/active resize, mutation and physical reverse-leaf representation are not claimed by these timed cases; their existing correctness oracles remain necessary.
