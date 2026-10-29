"""Run finite scientific and repository checks with a fresh atomic manifest."""
from datetime import datetime, timezone
import argparse
import importlib
import importlib.metadata
import json
from pathlib import Path
import platform
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def write_report(path, report):
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile('w', encoding='utf-8', dir=path.parent,
                                     prefix='.check-', delete=False) as f:
        temporary = Path(f.name)
        try:
            json.dump(report, f, indent=2, sort_keys=True, allow_nan=False)
            f.write('\n')
        except BaseException:
            temporary.unlink(missing_ok=True)
            raise
    try:
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


def run_all(output=None):
    destination = Path(output) if output is not None else ROOT/'verification/local_results/checks.json'
    try:
        revision = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT,
                                            stderr=subprocess.DEVNULL, text=True).strip()
    except (OSError, subprocess.CalledProcessError):
        revision = None
    report = {'status': 'running', 'all_assertions_passed': False,
              'started_at_utc': datetime.now(timezone.utc).isoformat(),
              'source_revision': revision, 'python': platform.python_version(),
              'packages': {}, 'checks': {},
              'scope': 'Finite consistency checks and navigation, not universal proofs or hosted rendering.'}
    write_report(destination, report)
    try:
        report['packages'] = {n: importlib.metadata.version(n) for n in ('numpy', 'scipy')}
        for name in ('threshold', 'bounds', 'kernel', 'learning', 'repository'):
            report['active_check'] = name
            write_report(destination, report)
            report['checks'][name] = importlib.import_module('check_'+name).run_checks()
            write_report(destination, report)
        report.pop('active_check', None)
        report.update(status='passed', all_assertions_passed=True)
    except BaseException as error:
        report.update(status='failed', all_assertions_passed=False,
                      error={'type': type(error).__name__, 'message': str(error)})
        write_report(destination, report)
        raise
    write_report(destination, report)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='Override the fresh JSON manifest location.')
    args = parser.parse_args()
    print(json.dumps(run_all(args.output), indent=2, sort_keys=True, allow_nan=False))


if __name__ == '__main__':
    main()
