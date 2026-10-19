# Read-only diagnosis of rejected ARM NEON implementations

The strongest static explanation is the generated fold predicate, not the presence of
NEON equality instructions alone. In all three exact timing binaries, Clang 18.1.3
reconstructs a 16-lane predicate for the source `if (tag == 1)` inside every complete
16-byte chunk loop. It stores two bytes on the stack, reloads one halfword, extracts
16 scalar bits and transfers those bits into 16 vector lanes: **35 instructions per
chunk**, in both forward and reversed paths. The resulting predicate gates the zero
comparison before normalization (`shl`/`cmlt`), `shrn`, and integer mask extraction.
The loop backedges return to these stack stores, so this is repeated chunk work,
even when the source tag is ordinary. This is a likely contributor to the measured
regression; these artifacts do not establish its dynamic cost or causal share.

All evidence comes from already sealed 017 validation disassembly of the actual
candidate timing binaries. The rebuilt baseline text was proven identical to the
unchanged 869425ed timing control during validation. No compiler, binary, source,
fixture, timing, or profile was changed or executed for this diagnosis.

| Variant | Function instructions / bytes | Stack frame | Continuing forward zero-mask path |
|---|---:|---:|---:|
| Baseline | 509 / 2036 | 528 bytes | 19 instructions per 8-byte chunk |
| A | 654 / 2616 | 544 bytes | 56 instructions per 16-byte chunk |
| B | 642 / 2568 | 544 bytes | 51 instructions per 16-byte chunk |
| C | 646 / 2584 | 544 bytes | 54 instructions per 16-byte chunk |

The final column traces one specific path through the frozen assembly: a forward
chunk with zero match mask, another complete chunk remaining, including the loop
backedge. Two baseline chunks therefore account for 38 instructions on this path.
These are static instruction counts, not cycles, retired-instruction measurements,
or an estimate of whole-scan speed. Match-bearing chunks and final exits differ.
The function-size count includes cold assertion and migration branches; the 16-byte
stack-frame increase is distinct from unchanged tree-owned heap memory.

## Exact attribution

`analysis.json` retains every opcode/address used in each count, artifact SHA256,
and half-open regions. `analyze.py` reproduces the analysis locally without builds.
Addresses below are absolute addresses in each captured ELF, not sample offsets.

| Variant | Reversed predicate region | Forward predicate region |
|---|---|---|
| A | [0x10498, 0x1052c) | [0x106bc, 0x10750) |
| B | [0x1049c, 0x10530) | [0x1059c, 0x10630) |
| C | [0x10498, 0x10530) | [0x106a4, 0x1073c) |

These enclosing regions also contain independently listed tag loads/offset arithmetic
(and two interleaved comparisons for C), excluded from the 35-instruction predicate
count. The 35 retained instructions comprise exactly 2 `strb`, 1 `ldrh`, 1 scalar
`and`, 14 `ubfx`, 1 scalar `lsr`, 1 scalar-to-vector `fmov`, and 15 vector-lane `mov`.
The source-linked assembly maps the ensuing masked zero comparison to the fold
condition. No out-of-line helper call accounts for this path.

A and C additionally lower the forward `mask &= mask - 1` loop into an iteration
count formed by `fmov`/`cnt`/`uaddlv`/`fmov` before the zero test (A 0x10778–0x10788;
C 0x10758–0x10768). B tests the whole nibble mask directly at 0x10650 and clears the
selected nibble in its matching loop. This is a concrete generated-code difference,
not proof of why B's measured slowdown was smaller, and does not make B eligible.
All three retain the original word and scalar residual paths; those paths and the
later packed member/score decoding also experienced register/layout changes.

## Limits and decision

The discovery already demonstrated all-block regressions: A roughly +97–102%/+69–72%,
B +77–79%/+55–56%, and C +99–102%/+68–70% at 100K/1M. This static diagnosis cannot
apportion those elapsed-time effects among predicate reconstruction, dependency
chains, stack store/reload behavior, mask iteration, register pressure, code layout,
branch prediction, or downstream decode. Two static hash call sites in candidates
versus one in the baseline do not prove an extra dynamically executed hash call.
No candidate PMU samples were collected here, and the baseline's sampled-period
share must not be assigned to these changed addresses.

The source-level conditional is a plausible place to investigate only through a
new, explicitly reviewed hypothesis/profile/control process. No corrective patch,
compiler switch, retry, fresh population, or confirmation is authorized by this
report. The completed population remains **REJECT, source NONE**. The ARM runner
remained idle throughout. Actual author: /root/aws_arm; exact model and cost unknown.
