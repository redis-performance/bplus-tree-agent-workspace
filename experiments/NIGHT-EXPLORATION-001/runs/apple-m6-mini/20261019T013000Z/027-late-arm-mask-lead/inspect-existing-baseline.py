#!/usr/bin/env python3
"""Read retained M6 baseline assembly; no compilation or native workload."""
import hashlib
import json
from pathlib import Path
import re

P = Path(__file__).resolve().parent
source = P.parent / "023-neon-replication/validation/base-native-codegen.stdout"
binary_manifest = json.loads((P.parent / "023-neon-replication/validation/binary-freeze.json").read_text())
text = source.read_text()
start = text.index("_zbtreeIteratorNext:\n")
lines = text[start:].splitlines()[1:]
instructions = []
for line in lines:
    if re.fullmatch(r"_[A-Za-z0-9_.$]+:", line):
        break
    match = re.match(r"^([0-9a-f]{16})\s+([A-Za-z][A-Za-z0-9.]*)\s*(.*)$", line)
    if match:
        instructions.append((int(match[1], 16), match[2], match[3]))
assert len(instructions) == 114
base = instructions[0][0]
window = [(address - base, mnemonic, operands) for address, mnemonic, operands in instructions
          if 0x100 <= address - base <= 0x110]
assert [x[1] for x in window] == ["mov", "lsl", "cmp", "csinv", "and"]
assert window[2][2] == "w11, #0x40"
payload = dict(scope="Existing baseline static report only; future M6 candidate remains unselected",
               codegen_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
               timing_binary_sha256=binary_manifest["snapshots"]["base"]["timing_binary_sha256"],
               source_c_sha256="d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2",
               symbol="_zbtreeIteratorNext", static_instructions=114,
               offsets_relative_to_symbol=True,
               window=[dict(offset_hex=hex(o), mnemonic=m, operands=a) for o, m, a in window],
               native_workloads=0, builds=0, modified_candidate_inspected=False,
               interpretation="Original width-64 conditional mask selection exists. Instruction count is not cost or a prediction of gain.",
               limitations="No attribution of prior PC samples to this new window, no cycle weights, no patched M6 codegen or timing, no acceptance.")
(P / "M6-BASELINE-MECHANISM.json").write_text(json.dumps(payload, indent=2) + "\n")
listing = "\n".join(f"+0x{o:03x}  {m:6s} {a}" for o, m, a in window)
(P / "M6-BASELINE-MECHANISM.md").write_text(
    "# Retained M6 baseline mask window\n\n"
    "The original mask-selection path exists in the retained corrected-adapter M6 baseline. "
    "This is a read-only observation of the already validated native binary and its saved disassembly.\n\n"
    "The unique IteratorNext body has 114 static instructions. Its symbol-relative window is:\n\n"
    "```asm\n" + listing + "\n```\n\n"
    "These five lines include the constant load and final AND. The compare/select handles the original "
    "width-64 special case. The source's outer `bits != 0` guard remains present. The historical patch "
    "replaces the conditional mask expression inside that guard; it has not been compiled or measured on M6 here.\n\n"
    "No sampled cycle cost, removable fraction or gain follows from this window. Prior PC locations are "
    "not reassigned across binaries. Patched local codegen, fresh qualified controls and all validation "
    "and acceptance gates remain future work under a new plan. No candidate is selected, and no native "
    "workload or build ran for this report. File and binary identities are in the adjacent JSON.\n")
print("Retained baseline: 114 instructions; original five-line mask window present; no candidate build or timing")
