#!/usr/bin/env python3
"""Canonical EXP-007 builds and correctness only; never run campaign/profile scripts."""
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import time

ROOT = Path.cwd()
OUT = Path(__file__).resolve().parent
WT = ROOT / "worktrees/m6-replica-exp007"
SCR = ROOT / "scratch/m6-exp007-replication-prep"
SCR.mkdir(parents=True, exist_ok=True)
START = time.monotonic()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def generic(value):
    return re.sub(r"/" + r"Users/[^\s\"']+", "<user-path>", value.replace(str(ROOT), "<workspace>"))


def save(name, value):
    (OUT / name).write_text(json.dumps(value, indent=2) + "\n")


assert not (OUT / "preparation.json").exists(), "preserve prior preparation; no unchanged retries"
identity = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=WT, text=True).strip()
assert identity == "e52c26c4b52c167b5ed3948eb9440f3fc2ffabaf"
frozen = json.loads((WT / "experiments/EXP-007/freeze.json").read_text())
assert all(sha(WT / p) == h for p, h in frozen["files"].items())
assert sha(WT / "src/zset_btree.c") == frozen["production_source_sha256"]
original_patches = {v: (WT / f"experiments/EXP-007/variants/{v}/candidate.patch").read_bytes() for v in "ABC"}
for v, value in original_patches.items():
    (SCR / (v + "-original.patch")).write_bytes(value)
state = dict(status="PREPARING BUILDS/CORRECTNESS ONLY", harness_commit=identity,
             nested_source_commit=frozen["source_commit"], commands=[],
             adapter="Original legacy adapter; same campaign identity as M1, not corrected adapter",
             no_campaign_or_profile_started=True, production_source_or_canonical_referee_hand_edited=False, canonical_nested_sources_generated=True,
             participant="/root/followup_proposal_b; inherited Codex/GPT-6 family; exact model/token/cost unknown")
save("preparation.json", state)


def command(args, name, limit):
    left = 480 - (time.monotonic() - START)
    assert left > 0, "preparation global8minute bound"
    p = subprocess.Popen(args, cwd=WT, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         text=True, start_new_session=True)
    item = dict(command=args, cwd="<EXP-007-worktree>", timeout_seconds=min(limit, left))
    stdout = stderr = ""
    try:
        stdout, stderr = p.communicate(timeout=item["timeout_seconds"])
    except BaseException as error:
        item["failure"] = generic(repr(error))
        if p.poll() is None:
            try:
                os.killpg(p.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
        stdout, stderr = p.communicate(timeout=10)
    finally:
        item.update(returncode=p.returncode, direct_child_reaped=p.poll() is not None)
        for channel, value in (("stdout", stdout), ("stderr", stderr)):
            raw = SCR / (name + "." + channel)
            assert not raw.exists()
            raw.write_text(value)
            public = OUT / (name + "." + channel)
            public.write_text(generic(value))
            item[channel] = dict(public=public.name, public_sha256=sha(public),
                                 raw="ignored scratch/m6-exp007-replication-prep/" + raw.name,
                                 raw_sha256=sha(raw))
        state["commands"].append(item)
        save("preparation.json", state)
    assert item["returncode"] == 0 and "failure" not in item, name


try:
    command(["python3", "experiments/EXP-007/build.py"], "native-build", 180)
    command(["python3", "experiments/EXP-007/build.py", "--sanitize"], "sanitizer-build", 180)
    for build in ("exp007", "exp007-sanitize"):
        for variant in ("base", "A", "B", "C"):
            command(["python3", "tests/test_decoder.py", f"build/{build}/{variant}/decoder-bench"],
                    build + "-" + variant + "-decoder-tests", 90)
    manifests = {}
    for build in ("exp007", "exp007-sanitize"):
        source = WT / "build" / build / "build.json"
        manifests[build] = json.loads(source.read_text())
        (OUT / (build + "-build.json")).write_text(generic(source.read_text()))
    regeneration = {}
    for variant, before in original_patches.items():
        after = (WT / f"experiments/EXP-007/variants/{variant}/candidate.patch").read_bytes()
        regeneration[variant] = dict(before_sha256=hashlib.sha256(before).hexdigest(),
                                    after_sha256=hashlib.sha256(after).hexdigest(), changed=before != after)
        if before != after:
            (OUT / (variant + "-before.patch")).write_bytes(before)
            (OUT / (variant + "-after.patch")).write_bytes(after)
    assert all(sha(WT / p) == h for p, h in frozen["files"].items())
    state.update(status="READY: NATIVE/SANITIZER CANONICAL CORRECTNESS PASS; NO MEASUREMENT",
                 commands_passed=len(state["commands"]), tests="4 unittest methods per binary,8 binaries; self-test1820 fixtures each",
                 canonical_patch_regeneration=regeneration, original_campaign_freeze_verified=True,
                 all_preparation_children_reaped=all(c["direct_child_reaped"] for c in state["commands"]))
    tracked = set(frozen["files"]) | {"src/zset_btree.c", "src/zset_btree.h", "compat/server.h", "compat/standalone.c", "vendor/redis/siphash.c", "tests/test_decoder.py", "experiments/EXP-007/audit.py", "experiments/EXP-007/profile.py", "experiments/EXP-007/freeze.json"}
    save("freeze.json", dict(harness_commit=identity, nested_source_commit=frozen["source_commit"],
         files_sha256={p: sha(WT / p) for p in sorted(tracked)},
         build_manifests_sha256={b: sha(WT / "build" / b / "build.json") for b in manifests},
         binary_sha256={b: {v: sha(WT / "build" / b / v / "decoder-bench") for v in ("base", "A", "B", "C")} for b in manifests},
         helper_and_variant_identities={b: m["variants"] for b, m in manifests.items()},
         status="PREPARATION ONLY; runner/profile require root exclusive publication ACK"))
except BaseException as error:
    state.update(status="PREPARATION FAILED; PRESERVED", failure=generic(repr(error)))
    raise
finally:
    state["preparation_wall_seconds"] = time.monotonic() - START
    save("preparation.json", state)
print(state["status"])
