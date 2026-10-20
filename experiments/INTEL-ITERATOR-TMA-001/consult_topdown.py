"""Import verified slot-only samples into isolated SQLite and query real MCP.

Run with scratch/topdown-profiler-assessment/.venv/bin/python.
Raw data remain unchanged. Only the slot unit spelling is canonicalized for
upstream71dea5e; MUX and non-slot denominators never enter the funnel.
"""
import asyncio
import collections
import csv
import hashlib
import json
import os
import statistics
import uuid
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from topdown.storage.sqlite_backend import SQLiteBackend
from topdown.storage.models import Run, Sample

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
CATEGORIES = ["Frontend_Bound", "Bad_Speculation", "Backend_Bound", "Retiring"]


async def main():
    db = ROOT / "scratch/intel-iterator-tma-slots.db"
    if db.exists():
        db.unlink()
    backend = SQLiteBackend(db)
    backend.initialize()
    groups = collections.defaultdict(lambda: collections.defaultdict(list))
    captures = []
    for path in sorted((HERE / "results").glob("profile-*-*.stderr")):
        if "workload" in path.name:
            continue
        lines = path.read_text().splitlines()
        start = next(i for i, line in enumerate(lines) if line.startswith("Timestamp,Area,Value,Unit,"))
        rows = [r for r in csv.DictReader(lines[start:]) if r.get("Area")]
        assert len(rows) == 130
        parsed = json.loads(path.with_suffix(".json").read_text())
        assert len(rows) == len(parsed)
        for row, sample in zip(rows, parsed):
            assert row["Area"] == sample["metric_name"]
            assert float(row["Value"]) == sample["value"]
            assert row["Unit"] == sample["unit"]
            assert float(row["Multiplex"]) == 100
        size = int(path.name.split("-")[1])
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        run_id = str(uuid.uuid5(uuid.NAMESPACE_URL, "intel-iterator-tma-slots:" + digest))
        backend.insert_run(Run(
            run_id=run_id, process_name="bplus-secondary-intel-baseline",
            level=2, duration_seconds=10, system_wide=True,
            labels={"size": str(size), "cpu": "2", "variant": "baseline",
                    "raw_sha256": digest, "scope": "CPU2, separately audited workload accounting",
                    "processing": "slot-only; literal unit spelling canonicalized",
                    "timestamp_origin": "ingestion, not capture wall time"}))
        slots = []
        for sample in parsed:
            if sample["metric_name"].split(".")[0] in CATEGORIES and sample["unit"] in ("% Slots", "% Slots <"):
                groups[size][sample["metric_name"]].append(sample["value"])
                slots.append(Sample(run_id=run_id, **dict(sample, unit="%_Slots")))
        backend.insert_samples(slots)
        captures.append({"run_id": run_id, "size": size, "file": path.name,
                         "sha256": digest, "imported_slot_samples": len(slots)})
    backend.close()
    summary = {"processing": "Unweighted means of 30 one-second intervals per size; raw values unchanged.",
               "captures": captures, "groups": {
        str(size): {key: {"mean": statistics.mean(values), "min": min(values),
                         "max": max(values), "n": len(values)}
                    for key, values in metrics.items()} for size, metrics in groups.items()}}
    (HERE / "tma-summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    env = dict(os.environ, TOPDOWN_BACKEND="sqlite", TOPDOWN_DB_PATH=str(db))
    env.pop("TOPDOWN_DSN", None)
    command = str(ROOT / "scratch/topdown-profiler-assessment/.venv/bin/topdown")
    async with stdio_client(StdioServerParameters(command=command, args=["mcp-serve"], env=env)) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            schemas = {t.name: t.inputSchema for t in (await session.list_tools()).tools}
            calls = []
            for capture in captures:
                args = {"run_id": capture["run_id"], "level": 2}
                assert "get_funnel" in schemas
                result = await session.call_tool("get_funnel", args)
                calls.append({"tool": "get_funnel", "arguments": args,
                              "result": result.model_dump(mode="json", by_alias=True)})
            (HERE / "topdown-mcp-calls.json").write_text(json.dumps({
                "transport": "actual local stdio; upstream71dea5e; isolated slot-only SQLite",
                "tools": schemas, "calls": calls}, indent=2) + "\n")
            assert not any(c["result"].get("isError") for c in calls)
    print(json.dumps({"captures": len(captures), "calls": len(calls), "groups": summary["groups"]}))


if __name__ == "__main__":
    asyncio.run(main())
