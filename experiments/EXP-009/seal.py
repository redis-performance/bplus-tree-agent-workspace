#!/usr/bin/env python3
"""Write-once local evidence seals; no native workloads or source mutations."""
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json

R = Path.cwd()
E = Path(__file__).resolve().parent

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def read(path):
    return json.loads(Path(path).read_text())

def write(path, value):
    with path.open('x') as out:
        out.write(json.dumps(value, indent=2) + '\n')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('kind', choices=['input', 'timing'])
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    relative = lambda p: str(p.relative_to(R))
    if args.kind == 'input':
        files = [R/'Makefile']
        for directory in ['src', 'compat', 'vendor', 'bench', 'tests']:
            files.extend(p for p in (R/directory).rglob('*') if p.is_file())
        files.extend(p for p in (E/'harness').rglob('*') if p.is_file())
        files.extend(E/name for name in [
            'README.md', 'PLAN.json', 'baseline-identity.json', 'host.json',
            'harness-origin.json', 'driver.py', 'profile-map.py', 'seal.py', 'publish-raw.py'])
        identities = {relative(p): digest(p) for p in sorted(set(files))}
        baseline = read(E/'baseline-identity.json')
        for path, expected in baseline['sha256'].items():
            assert identities[path] == expected, path
        value = dict(status='SEALED', baseline_commit=baseline['commit'],
                     files_sha256=identities,
                     scope='Corrected baseline only; build/profile/calibration prerequisites')
    else:
        build_path = E/'bench-results/build/build-manifest.json'
        counts_path = E/'bench-results/calibrate/counts.json'
        schedule_path = E/'bench-results/calibrate/aa-schedule.json'
        profile_path = E/'profile-results/run/status.json'
        build_status_path = E/'bench-results/build/status.json'
        calibration_status_path = E/'bench-results/calibrate/status.json'
        build, counts, profile = map(read, [build_path, counts_path, profile_path])
        assert digest(R/build['input_manifest_path']) == build['input_manifest_sha256']
        assert build['status'] == counts['status'] == profile['status'] == 'COMPLETE'
        assert profile['release_safe'] and profile['all_sufficient']
        for path in [build_status_path, calibration_status_path]:
            final_status = read(path)
            assert final_status['status'] == 'COMPLETE' and final_status['release_safe']
        assert len(read(schedule_path)) == 48
        identities = dict(build['files_sha256'])
        for path in [R/build['input_manifest_path'], build_path, build_status_path]:
            identities[relative(path)] = digest(path)
        for directory in [E/'bench-results/calibrate', E/'profile-results/run',
                          R/'scratch/exp009-driver/calibrate',
                          R/'scratch/exp009-driver/profile']:
            for path in directory.rglob('*'):
                if path.is_file():
                    identities[relative(path)] = digest(path)
        for path, expected in identities.items():
            assert digest(R/path) == expected, path
        value = dict(status='SEALED', files_sha256=identities,
                     build_manifest_path=relative(build_path),
                     counts_path=relative(counts_path), schedule_path=relative(schedule_path),
                     build_status_path=relative(build_status_path),
                     calibration_status_path=relative(calibration_status_path),
                     profile_status_path=relative(profile_path),
                     scope='48 fixed serial baseline A/A runs; no candidate timing')
    value['sealed_utc'] = datetime.now(timezone.utc).isoformat()
    destination = args.output if args.output else E/(args.kind+'-manifest.json')
    if not destination.is_absolute():
        destination = R/destination
    assert destination.parent == E, 'manifest must stay in this experiment'
    write(destination, value)
    print(json.dumps(dict(path=relative(destination), sha256=digest(destination),
                          entries=len(identities))))

if __name__ == '__main__':
    main()
