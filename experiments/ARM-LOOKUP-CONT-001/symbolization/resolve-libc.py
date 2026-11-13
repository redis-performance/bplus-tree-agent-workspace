#!/usr/bin/env python3
"""Offline attribution of captured samples; never collects performance data.

Usage: PYTHONPATH=<private-dependencies> python3 resolve-libc.py LIBC HIT_DATA LONG_DATA
Requires pyelftools. Prints sanitized JSON; profile/host paths are omitted.
"""
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from elftools.elf.elffile import ELFFile

EXPECTED = "54ae5337044aaabab70d65e0c3444f7e4735e059"
elf_path = sys.argv[1]
with open(elf_path, "rb") as stream:
    elf = ELFFile(stream)
    notes = elf.get_section_by_name(".note.gnu.build-id")
    build_id = next(n["n_desc"] for n in notes.iter_notes() if n["n_type"] == "NT_GNU_BUILD_ID")
    assert build_id == EXPECTED, build_id
    assert any(s["p_type"] == "PT_LOAD" and s["p_flags"] & 1 and s["p_vaddr"] == s["p_offset"] == 0
               for s in elf.iter_segments())
    symbols = {s.name: {"address": hex(s["st_value"]), "size": s["st_size"], "type": s["st_info"]["type"]}
               for s in elf.get_section_by_name(".dynsym").iter_symbols()
               if s.name in ("memchr", "memcmp", "__memcmpeq")}
result = {"scope": "Offline reanalysis of old whole-process user-cycle samples; includes setup/warmup",
          "elf_build_id": build_id, "elf_sha256": hashlib.sha256(open(elf_path, "rb").read()).hexdigest(),
          "dynamic_symbols": symbols, "profiles": {}}
for label, path in zip(("hit", "long"), sys.argv[2:]):
    ids = subprocess.check_output(["perf", "buildid-list", "-i", path], text=True, stderr=subprocess.DEVNULL)
    assert EXPECTED in ids
    process = subprocess.Popen(["perf", "script", "-i", path, "--show-mmap-events", "-F", "pid,ip,sym,dso,period"],
                               stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
    mappings = []
    counts = Counter()
    weights = Counter()
    offsets = Counter()
    for line in process.stdout:
        if "PERF_RECORD_MMAP2" in line:
            if "libc.so.6" in line:
                match = re.search(r"\[(0x[0-9a-f]+)\((0x[0-9a-f]+)\) @ ([0-9a-fx]+)", line)
                assert match, line
                start, size, fileoff = [int(v, 16) for v in match.groups()]
                mappings.append((start, start + size, fileoff))
            continue
        match = re.match(r"\s*(\d+)\s+(\d+)\s+([0-9a-f]+)\s+", line)
        if not match:
            continue
        period, ip = int(match[2]), int(match[3], 16)
        category = "other"
        if "libc.so.6" in line:
            mapping = next((m for m in reversed(mappings) if m[0] <= ip < m[1]), None)
            assert mapping is not None
            offset = ip - mapping[0] + mapping[2]
            # This ELF's executable PT_LOAD has equal vaddr and file offset (both zero).
            if 0xa13c0 <= offset < 0xa1484:
                category = "memchr_ifunc_default"
                offsets[hex(offset)] += period
            elif 0x9a800 <= offset < 0x9a9c8:
                category = "memcmp"
            else:
                category = "other_libc"
        counts[category] += 1
        weights[category] += period
    assert process.wait() == 0
    total = sum(weights.values())
    result["profiles"][label] = {"sha256": hashlib.sha256(open(path, "rb").read()).hexdigest(),
        "sample_count": sum(counts.values()), "total_sample_period": total,
        "categories": {k: {"samples": counts[k], "sample_period": v, "percent_of_all_sample_period": 100 * v / total}
                       for k, v in sorted(weights.items())},
        "memchr_offsets_period": dict(sorted(offsets.items()))}
print(json.dumps(result, indent=2))
