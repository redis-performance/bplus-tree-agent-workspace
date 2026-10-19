#!/usr/bin/env python3
"""Read-only actual-binary instructions and retained-PC/DWARF source mapping."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess
import time

ROOT = Path.cwd()
OUT = Path(__file__).resolve().parent
BASE = OUT.parent
SCR = Path("scratch/m6-member-hot-map")
BINARY = Path("scratch/m6-corrected-member-index-profile/native/enabled")
OBJECT = BINARY.parent / "tree.o"
started = time.monotonic()
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert sha(BINARY) == "7c088393dcd381154869327e626d06e4bd73c42a93ed888663e796b1e8cfefb8"
assert sha("src/zset_btree.c") == "d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2"
assert not (OUT / "hot-region-map.json").exists()
commands = json.loads((OUT / "commands.json").read_text())


def metadata(args, name, cap=10):
    left = 120 - (time.monotonic() - started)
    assert left > 0
    result = subprocess.run(args, capture_output=True, timeout=min(cap, left))
    for channel, data in (("stdout", result.stdout), ("stderr", result.stderr)):
        path = SCR / (name + "." + channel)
        assert not path.exists()
        path.write_bytes(data)
    commands.append(dict(name=name, command=args, returncode=result.returncode,
                         bound_seconds=min(cap, left), raw_location="ignored scratch/m6-member-hot-map",
                         raw_sha256={c: sha(SCR / (name + "." + c)) for c in ("stdout", "stderr")}))
    (OUT / "commands.json").write_text(json.dumps(commands, indent=2) + "\n")
    assert result.returncode == 0
    return result.stdout.decode()


def functions(text):
    output, current = {}, None
    for line in text.splitlines():
        if re.fullmatch(r"_[A-Za-z0-9_.$]+:", line):
            current = line[:-1]
            output[current] = []
        elif current and re.match(r"^[0-9a-f]{16}\s", line):
            address, instruction = line.split(None, 1)
            output[current].append((int(address, 16), instruction))
    return output


linked = functions((SCR / "enabled-disassembly.stdout").read_text())
objects = functions(metadata(["/usr/bin/otool", "-tvV", str(OBJECT)], "tree-object-disassembly", 30))
rows = json.loads((BASE / "summary.json").read_text())
mapping = json.loads((BASE / "codegen.json").read_text())["enabled_mapping"]
names = ("_zbtIndexScanSlot", "_zbtIndexScanGroup", "_zbtreeScoreRaw", "_zbtScoreLeafFindMember", "_zbtreeRank")
output, excerpts = {}, []
for name in names:
    actual, obj = linked[name], objects[name]
    mnemonics = lambda code: [instruction.split()[0] for _, instruction in code]
    assert len(actual) == len(obj) and mnemonics(actual) == mnemonics(obj), name
    start, object_start = actual[0][0], obj[0][0]
    symbol = next(x for x in mapping["symbols"] if x["name"] == name)
    assert start == symbol["address"]
    cases = {}
    for row in rows:
        for b in row["pc_bins"]:
            if b["module"] == "profile-program" and b["symbol"] == name:
                assert not b["symbol_ambiguous"] and b["symbol_aliases"] == [name]
                key = (row["case"], row["size"], row["seed"], row["original_index"])
                cases.setdefault(key, Counter())[b["offset_bytes"]] += b["samples"]
    combined = Counter()
    for values in cases.values():
        combined.update(values)
    instruction_map = {address - start: instruction for address, instruction in actual}
    points = []
    for offset, count in sorted(combined.items()):
        assert offset in instruction_map
        lookup = metadata(["/usr/bin/dwarfdump", "--lookup", hex(object_start + offset), str(OBJECT)],
                          name.lstrip("_") + "-plus-" + str(offset))
        inline = []
        for block in re.split(r"(?m)(?=^0x[0-9a-f]+:.*DW_TAG_)", lookup):
            if "DW_TAG_inlined_subroutine" not in block:
                continue
            origin = re.search(r'DW_AT_abstract_origin[^\n]*"([A-Za-z0-9_]+)"', block)
            if origin:
                ranges = [(int(a, 16) - object_start, int(b, 16) - object_start)
                          for a, b in re.findall(r"\[0x([0-9a-f]+), 0x([0-9a-f]+)\)", block)]
                inline.append(dict(name=origin[1], function_relative_ranges=ranges))
        line = re.search(r"Line info: file '([^']+)', line (\d+), column (\d+).*start line (\d+)", lookup)
        points.append(dict(offset_bytes=offset, captured_locations=count,
                           instruction=instruction_map[offset], dwarf_inline_regions=inline,
                           compiler_line=(int(line[2]) if line else None),
                           compiler_column=(int(line[3]) if line else None),
                           inline_declaration_start_line=(int(line[4]) if line else None),
                           source_file=Path(line[1]).name if line else None,
                           source_line_limit="Optimized DWARF mapping; line0/no-line is not an exact statement and is not replaced with the declaration line"))
    vector = [dict(offset_bytes=address - start, instruction=ins) for address, ins in actual
              if re.search(r"\b(?:v|q)[0-9]+\b", ins)]
    output[name] = dict(symbol_image_offset=start - mapping["image_vmaddr"],
                        actual_instruction_count=len(actual), object_instruction_count=len(obj),
                        object_linked_mnemonic_sequence_identical=True,
                        address_mapping_method="Exact shared tree.o symbol+same instruction offset; linked/object instruction counts and ordered mnemonics match; address/relocation operands may differ",
                        vector_register_instructions=vector, sampled_points=points,
                        per_capture=[dict(case=k[0], size=k[1], seed=k[2], original_index=k[3],
                                          captured_locations=sum(v.values()), offsets=dict(v)) for k, v in cases.items()])
    excerpts.append(name + ":")
    for address, ins in actual:
        safe = re.sub(r"0x[0-9a-f]+", lambda m: "__image+0x%x" % (int(m[0], 16) - mapping["image_vmaddr"])
                      if int(m[0], 16) >= mapping["image_vmaddr"] else m[0], ins)
        excerpts.append("  +%04d  %s" % (address - start, safe))
    excerpts.append("")
(OUT / "selected-instructions.s").write_text("\n".join(excerpts))
slot = output["_zbtIndexScanSlot"]
inline_ranges = {tuple(pair) for point in slot["sampled_points"] for region in point["dwarf_inline_regions"]
                 if region["name"] == "zbtLeafTagMatches" for pair in region["function_relative_ranges"]}
assert inline_ranges == {(496, 612), (620, 1256)}
slot_partition = []
for capture in slot["per_capture"]:
    tag = sum(count for offset, count in capture["offsets"].items() if any(a <= offset < b for a, b in inline_ranges))
    slot_partition.append(dict(original_index=capture["original_index"], size=capture["size"], seed=capture["seed"],
                               slot_locations=capture["captured_locations"], inlined_tag_match_locations=tag,
                               other_slot_locations=capture["captured_locations"] - tag))
assert not slot["vector_register_instructions"]
report = dict(status="STATIC ACTUAL-BINARY/SOURCE LOCATION MAP; NO PROPOSAL OR COST CLAIM",
    enabled_binary_sha256=sha(BINARY), shared_tree_object_sha256=sha(OBJECT),
    source_c_sha256=sha("src/zset_btree.c"), source_h_sha256=sha("src/zset_btree.h"),
    corrected_adapter_header_sha256=sha("compat/server.h"), corrected_adapter_c_sha256=sha("compat/standalone.c"),
    summary_sha256=sha(BASE / "summary.json"), codegen_sha256=sha(BASE / "codegen.json"),
    functions=output, slot_inline_ranges=sorted(inline_ranges), scan_slot_partition=slot_partition,
    limits=["Captured PCs are exclusive locations, not costs, cycles, latency, unbiased time shares or proof that a nearby instruction caused delay.",
            "Optimized line0 and inlined source mappings remain ambiguous; addresses/relocations can differ between object and linked image.",
            "The enabled diagnostic frontend differs from the ordinary benchmark; unchanged tree object does not prove runtime equivalence to an uninstrumented baseline.",
            "External memchr/memcmp counts are dladdr location labels; this map does not inspect their implementations or sum inclusive frames.",
            "No other-ISA executable was inspected; no cross-architecture code or performance conclusion follows.",
            "Tag matching remains eight-byte scalar SWAR in this actual inline instance; absence of NEON here does not establish a profitable transformation."],
    metadata_only=True, new_builds_captures_tests_or_benchmarks=0,
    participant="/root/followup_proposal_b; inherited Codex/GPT-6 family; exact serving model/token/cost unknown")
(OUT / "hot-region-map.json").write_text(json.dumps(report, indent=2) + "\n")
print("Static map complete:", len(commands), "read-only commands; tag-match ranges", sorted(inline_ranges))
