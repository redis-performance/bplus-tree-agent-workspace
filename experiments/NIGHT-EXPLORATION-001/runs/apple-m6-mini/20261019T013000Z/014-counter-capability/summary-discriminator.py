#!/usr/bin/env python3
"""Read only named archived Summary: Metrics structural metadata; never export rows."""
import hashlib
import json
import plistlib
from pathlib import Path

OUT = Path(__file__).resolve().parent
TRACE = Path("scratch/m6-counter-capability/availability.trace")


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


freeze = json.loads((OUT / "freeze.json").read_text())
assert all(sha(path) == digest for path, digest in freeze["files_sha256"].items())
objects = plistlib.loads((TRACE / "form.template").read_bytes())["$objects"]


def resolve(value):
    return objects[value.data] if isinstance(value, plistlib.UID) else value


def dictionary(value):
    return {resolve(key): resolve(item) for key, item in
            zip(value.get("NS.keys", []), value.get("NS.objects", []))
            if isinstance(resolve(key), str)}


summaries = []
counter_ui = []
configs = []
for value in objects:
    if isinstance(value, dict) and "NS.keys" in value:
        fields = dictionary(value)
        if fields.get("detailIdentifier") == "Summary: Metrics":
            summaries.append(sorted(fields))
        if fields.get("identifier") == "com.apple.dt.instruments.cpu.counters":
            counter_ui.append({name + "_registered_count": len(fields[name].get("NS.objects", []))
                               for name in ("brushes", "details") if isinstance(fields.get(name), dict)})
    if isinstance(value, bytes) and b"countingLevel" in value and len(value) < 4096:
        configs.append(json.loads(value))
assert len(configs) == 1
config = configs[0]
result = dict(
    status="UNKNOWN: actual counter acquisition versus unavailable/export-hidden guided data remains unresolved",
    method="Read-only plist decoding of exact retained form.template; named Summary: Metrics, counter instrument UI registration and serialized counter configuration only",
    invocation="python3 <campaign>/014-counter-capability/summary-discriminator.py",
    summary_metric_detail_registration_count=len(summaries),
    summary_metric_registration_field_names=summaries,
    counter_instrument_ui_registration=counter_ui,
    structural_interpretation="Summary: Metrics records contain detailIdentifier only; they identify a selected UI view, not a persisted metric result. Empty registered UI brushes/details do not establish absence of raw acquisition.",
    configuration=dict(configurationType=config["configurationType"],
                       selectedCountingMode=config["selectedCountingMode"],
                       selectedCountingModeDisplayName=config["selectedCountingModeDisplayName"],
                       countingLevel=config["countingLevel"],
                       allEventsAndFormulas_count=len(config["allEventsAndFormulas"])),
    actual_metric_values="NOT EXTRACTED; no proven own-target metric scope or unit mapping",
    actual_counter_scope="UNQUALIFIED", actual_counter_units="UNQUALIFIED",
    recommendation="Stop this discriminator; do not repeat unchanged CPU Counters capture. Distinct CPU Profiler pilot remains a separate reviewed qualification proposal.",
    frozen_files_unchanged=True, new_recordings=0, counter_row_exports=0, trace_writes=0,
    instruments_ui_opened=False, source_hashes={
        "private form.template": sha(TRACE / "form.template"),
        "freeze.json": sha(OUT / "freeze.json"),
        "summary-discriminator.py": sha(__file__)},
    public_hygiene="Only named generic configuration/UI structure, counts and hashes; no process names, PIDs, machine identity or actual metric values",
    parser_preparation_failure="Initial generic keyed-dictionary decoder met a non-string archived key (TypeError: unhashable dict); restricted decoding to named string fields. No trace modification or row export.",
    participant="/root/followup_proposal_b; inherited Codex/GPT-6 family; exact model/token/cost unknown")
(OUT / "SUMMARY-DISCRIMINATOR.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"status": result["status"], "summary_registrations": len(summaries),
                  "counter_ui_registrations": counter_ui, "frozen_files_unchanged": True}))
