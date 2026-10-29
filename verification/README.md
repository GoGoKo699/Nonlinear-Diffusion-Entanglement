# Verification and reproducibility

The canonical analytical arguments are in [science](../science/README.md). The suite checks *finite* exact packet integrals, their elementary inequalities, the Gaussian determinant and the Brownian spectral/Laplace formula. Passing scripts are not proofs of all-time statements or an assessment of novelty.

## Commands

Tested using Python 3.12+ with the pinned dependencies in this repository:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_checks.py
```

The runner exits nonzero upon any failed assertion, prints JSON on a passing run, and requires neither a network request nor external data or randomized sampling. [Recorded reference values](reference_results.json) identify the tested finite regime.

## Checks

| Check | What it tests | What it does not prove |
|---|---|---|
| `check_threshold.py` | Mehler/Gaussian-packet one-dimensional integrals in log arithmetic; upper diagonal and lower coherence inequalities; NPT signs at six fixed parameter points | NPT at all pre-threshold times or EB at the endpoint |
| `check_bounds.py` | Exact cosine autocorrelation integral, Brownian Laplace expression versus a 30,000-mode product, deterministic Gaussian covariance and threshold, analytic positivity of cubic lower constant | Sharp exponent coefficient, capacity, general perturbation theory |

For $D=2,\kappa=0.3,\eta=0.125,\omega=0.7$ the theorem predicts $t_{\rm EB}=1$. With $A=20,\delta=0.05$ the finite witness is NPT at $t=0.5$ and $0.9$ and not NPT at $t=1$ and $1.1$. Additional checks use negative drift and very small positive $\kappa$; all tested inequality directions pass.

The Gaussian packet numerics use Gaussian quadrature, log sums and a stable small-$|y|$ expansion; their very small numbers must not be rounded to zero before comparing signs. The Brownian spectral expansion has a controlled finite truncation discrepancy and checks the exact formula with a tolerance, without fitting any exponent.

Analytical proof of the general EB threshold is in [exact_threshold.md](../science/exact_threshold.md); the all-reference cubic upper and normalized packet lower are in [cubic_distance.md](../science/cubic_distance.md). We did not measure a physical device, infer an unconstrained capacity, independently verify every claim with a second experimental apparatus or certify hosted Markdown rendering through these numerical tests. Hosted math rendering belongs to the later automatic furnishing/Sanity Check.
