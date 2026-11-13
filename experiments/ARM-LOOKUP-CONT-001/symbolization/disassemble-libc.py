#!/usr/bin/env python3
"""Print relevant instructions from the already captured matching ELF. No execution."""
import sys
from capstone import Cs, CS_ARCH_ARM64, CS_MODE_ARM
from elftools.elf.elffile import ELFFile

with open(sys.argv[1], "rb") as stream:
    elf = ELFFile(stream)
    build_id = next(n["n_desc"] for n in elf.get_section_by_name(".note.gnu.build-id").iter_notes()
                    if n["n_type"] == "NT_GNU_BUILD_ID")
    assert build_id == "54ae5337044aaabab70d65e0c3444f7e4735e059"
    print("ELF build ID:", build_id)
    disasm = Cs(CS_ARCH_ARM64, CS_MODE_ARM)
    for start, end in ((0x9a7b0, 0x9a7f0), (0xa13c0, 0xa1484), (0x9a800, 0x9a9c8)):
        segment = next(s for s in elf.iter_segments() if s["p_type"] == "PT_LOAD"
                       and s["p_vaddr"] <= start and end <= s["p_vaddr"] + s["p_filesz"])
        stream.seek(segment["p_offset"] + start - segment["p_vaddr"])
        print(f"Range {start:#x}..{end:#x}")
        for insn in disasm.disasm(stream.read(end-start), start):
            print(f"{insn.address:08x}: {insn.bytes.hex()} {insn.mnemonic} {insn.op_str}")
