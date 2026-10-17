#!/usr/bin/env python3
"""Summarise the preregistered identical-binary controls; never infer a speedup."""
import csv
import json
import math
from pathlib import Path
import statistics as stats
from collections import defaultdict

HERE=Path(__file__).resolve().parent
manifest=json.loads((HERE/"manifest.json").read_text())
groups=defaultdict(list)
for run in manifest["runs"]:
    if run["returncode"]: continue
    for row in csv.DictReader((HERE/run["csv"]).open()):
        row.update(block=run["block"],label=run["label"])
        groups[(run["cell"],row["case"])].append(row)
results=[]
for (cell,case),rows in sorted(groups.items()):
    ns=[int(r["elapsed_ns"])/int(r["operations"]) for r in rows]
    effects=[]
    for block in range(1,7):
        by_label={x:[int(r["elapsed_ns"])/int(r["operations"]) for r in rows
                     if r["block"]==block and r["label"]==x] for x in "AB"}
        if any(len(x)!=2 for x in by_label.values()): continue
        effects.append(100*(stats.mean(by_label["B"])/stats.mean(by_label["A"])-1))
    mean=stats.mean(effects) if effects else None
    half=2.5705818366147395*stats.stdev(effects)/math.sqrt(6) if len(effects)==6 else None
    lo,hi=(mean-half,mean+half) if half is not None else (None,None)
    elapsed_min=min(int(r["elapsed_ns"]) for r in rows)
    qualified=len(rows)==24 and half is not None and lo>=-1 and hi<=1 and elapsed_min>=10000000
    result={"cell":cell,"case":case,"n":len(ns),"median_ns_op":stats.median(ns),
        "min_ns_op":min(ns),"max_ns_op":max(ns),"cv_pct":100*stats.stdev(ns)/stats.mean(ns),
        "aa_mean_pct":mean,"aa_ci95_low_pct":lo,"aa_ci95_high_pct":hi,"aa_block_effects_pct":effects,
        "min_timed_ms":elapsed_min/1e6,"tree_bytes_min":min(int(r["tree_bytes"]) for r in rows),
        "tree_bytes_max":max(int(r["tree_bytes"]) for r in rows),
        "checksum_variants":len({r["checksum"] for r in rows}),
        "qualified_1pct":qualified}
    results.append(result)
(HERE/"summary.json").write_text(json.dumps(results,indent=2)+"\n")
with (HERE/"summary.csv").open("w") as out:
    fields=[k for k in results[0] if k!="aa_block_effects_pct"]
    writer=csv.DictWriter(out,fields,extrasaction="ignore",lineterminator="\n");writer.writeheader();writer.writerows(results)
lines=["# Identical-binary control summary", "", "All times are batch-average ns/op, not individual-operation latency percentiles.",
       "A and B are the same binary. Positive B/A effects are slower B; these are noise controls, not speedups.",
       "Intervals are 95% Student-t intervals over six block-paired effects (df=5), with independence/normality assumptions.",
       "Qualification requires the entire interval inside +/-1% and every timed region >=10 ms. No outliers removed.", "",
       "| Cell | Case | Median ns/op | Min–max | CV % | A/A mean % [95% interval] | Shortest ms | Qualified |",
       "|---|---|---:|---:|---:|---|---:|---|"]
for r in results:
    interval="incomplete" if r['aa_ci95_low_pct'] is None else f"{r['aa_mean_pct']:+.2f} [{r['aa_ci95_low_pct']:+.2f}, {r['aa_ci95_high_pct']:+.2f}]"
    lines.append(f"| {r['cell']} | {r['case']} | {r['median_ns_op']:.2f} | {r['min_ns_op']:.2f}–{r['max_ns_op']:.2f} | {r['cv_pct']:.2f} | {interval} | {r['min_timed_ms']:.3f} | {'yes' if r['qualified_1pct'] else 'no'} |")
(HERE/"SUMMARY.md").write_text("\n".join(lines)+"\n")
print(json.dumps({"status":manifest['status'],"processes":len(manifest['runs']),"rows":sum(len(x) for x in groups.values()),"qualified_cells":sum(r['qualified_1pct'] for r in results),"total_case_cells":len(results)},indent=2))
