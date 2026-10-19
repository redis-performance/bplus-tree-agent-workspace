#!/usr/bin/env python3
"""Use the reviewed unchanged serial owner for the original EXP007 shortlist follow-up."""
import importlib.util
from pathlib import Path
path = Path(__file__).with_name('serial-owner.py')
spec = importlib.util.spec_from_file_location('serial_owner', path)
owner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(owner)
owner.PHASES = {
    '007-confirmation-A': ('007', ['experiments/EXP-007/run.py', '--out', 'build/m6-replications/EXP007/confirmation', '--confirmation', 'A', '--budget-seconds', '180'], 240),
    '007-profile-A': ('007', ['experiments/EXP-007/profile.py', 'A', '--out-dir', 'build/m6-replications/EXP007/profiles'], 40),
}
if __name__ == '__main__':
    owner.main()
