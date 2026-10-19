"""Exercise actual process cleanup and continuation without calling a model."""
from datetime import datetime, timedelta, timezone
import fcntl
import importlib.util
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location(
    "overnight", Path(__file__).resolve().parents[1] / "scripts/overnight.py")
overnight = importlib.util.module_from_spec(spec)
spec.loader.exec_module(overnight)


class SupervisorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name).resolve()
        (self.root / "docs").mkdir()
        (self.root / "docs/OVERNIGHT-PROMPT.md").write_text("Test worker only.\n")
        self.worker = self.root / "fake-codex"
        self.handlers = {s: signal.getsignal(s) for s in (signal.SIGTERM, signal.SIGINT)}

    def tearDown(self):
        for sig, handler in self.handlers.items():
            signal.signal(sig, handler)
        self.tmp.cleanup()

    def run_supervisor(self, code, seconds, extra_args=()):
        self.worker.write_text(f"#!{sys.executable}\n" + code)
        self.worker.chmod(0o700)
        end = (datetime.now(timezone.utc) + timedelta(seconds=seconds)).isoformat()
        argv = ["overnight", "--deadline", end, "--run-dir", "scratch/test", *extra_args]
        with patch.object(overnight, "ROOT", self.root), patch.object(sys, "argv", argv), \
             patch.object(overnight.shutil, "which", side_effect=lambda n: str(self.worker) if n == "codex" else None):
            overnight.main()
        return json.loads((self.root / "scratch/test/status.json").read_text())

    @staticmethod
    def alive(pid):
        result = subprocess.run(["ps", "-p", str(pid), "-o", "stat="],
                                capture_output=True, text=True)
        return result.returncode == 0 and not result.stdout.strip().startswith("Z")

    def test_deadline_cleans_separate_session_child_but_not_unrelated_process(self):
        unrelated = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(60)"])
        try:
            state = self.run_supervisor("""
import pathlib, subprocess, sys, time
sys.stdin.read()
p = subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(60)'], start_new_session=True)
pathlib.Path('child.pid').write_text(str(p.pid))
time.sleep(60)
""", 7)
            child = int((self.root / "child.pid").read_text())
            self.assertEqual(state["status"], "deadline_reached")
            self.assertEqual(state["rounds"][0]["status"], "timed_out")
            self.assertFalse(self.alive(child))
            self.assertIsNone(unrelated.poll())
        finally:
            unrelated.terminate()
            unrelated.wait()

    def test_stop_file_interrupts_running_worker(self):
        state = self.run_supervisor("""
import pathlib, sys, time
sys.stdin.read()
pathlib.Path('scratch/test/STOP').touch()
time.sleep(60)
""", 45)
        self.assertEqual(state["status"], "stopped_by_request")
        self.assertFalse(self.alive(state["rounds"][0]["worker_pid"]))

    def test_completed_round_resumes_and_records_actual_usage(self):
        state = self.run_supervisor("""
import json, pathlib, sys
sys.stdin.read()
count = pathlib.Path('count.txt')
n = int(count.read_text()) + 1 if count.exists() else 1
count.write_text(str(n))
pathlib.Path(sys.argv[sys.argv.index('-o') + 1]).write_text('saved handoff')
print(json.dumps({'type':'turn.completed','usage':{'input_tokens':12,'output_tokens':3}}))
if n == 2:
    pathlib.Path('scratch/test/STOP').touch()
""", 45)
        self.assertEqual(len(state["rounds"]), 2)
        self.assertTrue(all(r["status"] == "completed" for r in state["rounds"]))
        self.assertEqual(state["rounds"][1]["usage"]["output_tokens"], 3)
        self.assertEqual(state["status"], "stopped_by_request")

    def test_second_supervisor_refuses_existing_lock(self):
        (self.root / "scratch").mkdir()
        with (self.root / "scratch/overnight.lock").open("w") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            with self.assertRaises(SystemExit) as caught:
                self.run_supervisor("raise Exception('must not start')\n", 45)
            self.assertEqual(caught.exception.code, 2)
        self.assertFalse((self.root / "scratch/test").exists())

    def test_custom_campaign_uses_own_prompt_and_blocker(self):
        (self.root / "docs/new-night.md").write_text("NEW CAMPAIGN INSTRUCTIONS\n")
        old = self.root / "experiments/OVERNIGHT-2026-10-17"
        old.mkdir(parents=True)
        (old / "BLOCKED.md").write_text("Historical blocker must not stop new campaign")
        state = self.run_supervisor("""
import json, pathlib, sys
prompt = sys.stdin.read()
assert 'NEW CAMPAIGN INSTRUCTIONS' in prompt
assert 'Host label: apple-m6-mini' in prompt
assert 'Evidence directory: experiments/new-night/apple-m6-mini' in prompt
count = pathlib.Path('count.txt')
n = int(count.read_text()) + 1 if count.exists() else 1
count.write_text(str(n))
if n == 2:
    evidence = pathlib.Path('experiments/new-night/apple-m6-mini')
    evidence.mkdir(parents=True)
    (evidence/'BLOCKED.md').write_text('This campaign is blocked')
print(json.dumps({'type':'turn.completed','usage':{}}))
""", 45, ['--prompt-file', 'docs/new-night.md', '--campaign-dir',
          'experiments/new-night/apple-m6-mini', '--host-label', 'apple-m6-mini'])
        self.assertEqual(len(state['rounds']), 2)
        self.assertEqual(state['status'], 'blocked_reported_by_worker')
        self.assertEqual(state['host_label'], 'apple-m6-mini')

    def test_invalid_campaign_path_refused_before_launch(self):
        with self.assertRaises(SystemExit):
            self.run_supervisor("raise Exception('must not start')\n", 45,
                                ['--campaign-dir', '../outside'])
        self.assertFalse((self.root / 'scratch/test').exists())


if __name__ == "__main__":
    unittest.main()
