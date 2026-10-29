"""Run all finite consistency checks and optionally save a truthful manifest."""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import platform
import tempfile
from datetime import datetime, timezone
import numpy
import scipy
from check_threshold import run_checks as threshold
from check_bounds import run_checks as bounds
from check_kernel import run_checks as kernel


def save(path: Path | None, report: dict) -> None:
    if path is None:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(report, indent=2, sort_keys=True, allow_nan=False) + '\n'
    with tempfile.NamedTemporaryFile('w', encoding='utf-8', dir=path.parent,
                                     delete=False) as temporary:
        name = temporary.name
        temporary.write(text)
    try:
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def run_all(output: Path | None = None) -> dict:
    report = {'status':'running','all_assertions_passed':False,
              'started_at_utc':datetime.now(timezone.utc).isoformat().replace('+00:00','Z'),
              'environment':{'python':platform.python_version(),
                             'numpy':numpy.__version__,'scipy':scipy.__version__},
              'scope':'Finite consistency checks; analytical proofs are in science/.',
              'checks':{}}
    save(output, report)
    for name, check in [('threshold',threshold),('bounds',bounds),('kernel',kernel)]:
        report['active_check'] = name
        save(output, report)
        try:
            report['checks'][name] = check()
        except Exception as error:
            report.update(status='failed',error=f'{type(error).__name__}: {error}')
            save(output, report)
            raise
    report.pop('active_check',None)
    report.update(status='passed',all_assertions_passed=True)
    save(output, report)
    return report

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='Optional JSON manifest; replaced atomically.')
    args = parser.parse_args()
    print(json.dumps(run_all(args.output),indent=2,sort_keys=True,allow_nan=False))
