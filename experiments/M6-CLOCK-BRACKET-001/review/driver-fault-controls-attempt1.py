#!/usr/bin/env python3
"""Offline phase-chain/deadline fault injection; no child process/native workload."""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
from datetime import datetime, timezone, timedelta

E = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('bracket_driver_fault_test', E / 'driver.py')
d = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d)
results = []


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value))


def setup(root, build='COMPLETE', controls='COMPLETE'):
    d.E = root
    write(root / 'PLAN.json', {'absolute_stop_utc': (datetime.now(timezone.utc) + timedelta(minutes=5)).isoformat(),
          'phase_wall_caps_seconds': {'build': 120, 'controls': 120, 'aa': 120}})
    write(root / 'inputs.json', {'files_sha256': {}})
    write(root / 'results/build/build-manifest.json', {'status': 'COMPLETE', 'files_sha256': {}})
    write(root / 'results/build/status.json', {'status': build, 'release_safe': True})
    if controls is not None:
        write(root / 'results/controls/status.json', {'status': controls, 'release_safe': True, 'native_lock_released': True})
        write(root / 'results/controls/summary.json', {'sensitivity_pass': True})
        target = root / 'control-pin.json'
        write(target, {'value': 1})
        write(root / 'results/controls/evidence-manifest.json', {'files_sha256': {str(target): d.sha(target)}})


with tempfile.TemporaryDirectory(prefix='bracket-offline-fault-') as temporary:
    root = Path(temporary)
    for name, phase, bs, cs in [('failed-build-rejected', 'controls', 'FAILED_FINALIZATION_NO_RETRY', None),
                              ('failed-controls-rejected', 'aa', 'COMPLETE', 'FAILED_FINALIZATION_NO_RETRY')]:
        folder = root / name
        setup(folder, bs, cs)
        try:
            d.Owner(phase, 'synthetic-only')
        except AssertionError:
            results.append({'case': name, 'pass': True})
        else:
            raise AssertionError(name)
    folder = root / 'control-pin-postcheck'
    setup(folder)
    owner = d.Owner('aa', 'synthetic-only')
    write(folder / 'control-pin.json', {'value': 2})
    try:
        owner.finish(None)
    except AssertionError:
        assert d.load(owner.out / 'status.json')['status'] == 'FAILED_FINALIZATION_NO_RETRY'
        results.append({'case': 'control-pin-mutation-fails-postcheck', 'pass': True})
    else:
        raise AssertionError('Control pin mutation not detected')
    folder = root / 'late-finalization'
    setup(folder, controls=None)
    owner = d.Owner('build', 'synthetic-only')
    owner.absolute = 0
    try:
        owner.finish(None)
    except TimeoutError:
        assert d.load(owner.out / 'status.json')['status'] == 'FAILED_DEADLINE_NO_RETRY'
        results.append({'case': 'late-finalization-cannot-complete', 'pass': True})
    else:
        raise AssertionError('Late finalization accepted')

output = {'status': 'PASS_OFFLINE_FAULT_CONTROLS', 'cases': results, 'synthetic': True,
          'native_children_launched': 0, 'driver_sha256': d.sha(E / 'driver.py'),
          'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
with (E / 'review/DRIVER-FAULT-CONTROLS.json').open('x') as f:
    json.dump(output, f, indent=2)
    f.write('\n')
print(json.dumps(output))
