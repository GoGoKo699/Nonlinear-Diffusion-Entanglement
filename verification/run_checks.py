"""Run the self-contained scientific consistency suite."""
from pathlib import Path
import sys
import json

sys.path.insert(0,str(Path(__file__).resolve().parent))
from check_threshold import run_checks as threshold
from check_bounds import run_checks as bounds


def run_all():
    a=threshold()
    b=bounds()
    return {"status":"passed","all_assertions_passed":True,
            "scope":"finite formula and factor checks; theorems are analytical",
            "threshold_cases":a,"independent_formula_checks":b}


if __name__ == "__main__":
    print(json.dumps(run_all(),indent=2,sort_keys=True,allow_nan=False))
