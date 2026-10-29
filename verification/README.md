# Verification — commands, evidence, and limits

The canonical scientific arguments are in [`science/`](../science/README.md). This suite checks exact finite integrals, their explicit elementary bounds, covariance determinants and Brownian quadratic-function formulas. **A passing finite script cannot prove an all-energy diamond estimate, a sharp boundary for every time, or bibliographic priority.**

## Reproduction

Tested in Python 3.13.5 with the dependencies pinned below. From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_checks.py
python3 verification/check_learning.py
```

The scientific runner imports three checks and exits nonzero on any failed assertion. Its reference JSON output is recorded as [`reference_results.json`](reference_results.json). No randomness, network access, external datasets, or hidden numerical notebooks are required. An optional `--output verification/local_results/run.json` writes an atomic manifest, first marked running and not passed. A caught failure records failed status; after manifest initialization, an interrupted run does not retain an earlier passing manifest. Fresh output is separate from the committed reference.

## Which assertions are checked?

| Test | What it verifies | What it cannot establish |
|---|---|---|
| `check_kernel.py` | Direct two-dimensional Gaussian quadrature versus the reduced packet factors, finite-difference evolution equation, and kernel composition | A proof of the unbounded-generator domain or its universal estimates |
| `check_threshold.py` | Evaluation of the reduced one-dimensional Gaussian-packet integrals; lower coherence and upper leakage inequalities; NPT at parameter points strictly below the predicted EB boundary | NPT at all earlier times, nor EB at and above the boundary, which require proof |
| `check_bounds.py` | Independent integration of compact-packet $`c_f`$; Gaussian covariance determinant and $`\kappa=0`$ cutoff; Brownian spectral product versus hyperbolic Laplace transform; positivity of $`c_*`$, late-time inequalities, and the weak-kinetic-noise Chernoff identity | An optimized exponent, energy-constrained capacity or the positivity of all untested cases |
| `check_learning.py` | Exactly 30 ordered milestones, phase allocation, fields, dependencies, one anchor, local source links and worked-example identities | Learner mastery, universal proof correctness or hosted visual rendering |

For $`D=2,\kappa=0.3,\eta=0.125,\omega=0.7`$, the analytical threshold is $`t_{\mathrm{EB}}=1`$. At finite packet parameters $`A=20,\delta=0.05`$ the output NPT witness is negative at $`t=0.5`$ and $`0.9`$; it is nonnegative at $`t=1`$ and $`1.1`$. The exact integrals and rigorous bounds are separately recorded, so the test does not treat a floating-point sign as a proof of the theorem. Weak-$`\kappa`$ and nonzero-drift cases probe the lower-bound factors with negative or positive $`\omega`$.

The independent kernel tests have maximum packet-reduction error below `3e-16`, semigroup-composition error below `4e-16`, and finite-difference generator residual below `3e-9` in the recorded cases. These are numerical residuals at declared finite parameters, not interval-arithmetic certificates.

The Brownian Laplace tests compare closed form with a truncated 30,000-mode cosine product. The truncation is expected to have a nonzero residual and is checked against a declared tolerance, not fitted to agree. The proof instead uses exact spectral identities and elementary Chernoff bounds.

## Learning-route checks

The independent learning checker evaluates the primer's qubit partial transpose at four coherence values and compares twelve finite Gaussian covariance determinants with their closed formula. It checks the example cutoff $`\sqrt{(\sqrt{21}-3)/2}`$. The exact diamond-distance argument in that example is analytical; the script does not silently substitute a finite matrix norm for a diamond norm.

Map and navigation assertions operate on current files, so a missing milestone, forward dependency or broken local destination fails the command. Structural checks are paired with a semantic review of the two phases and the source-to-project bridge. The [Sanity Check record](SANITY_CHECK.md) states the inspected baseline, scope and outstanding hosted-rendering limitation.

## Reproducibility boundaries

- `numpy==2.3.5` and `scipy==1.17.0` are pinned for numerical consistency; the analytical formulas do not depend on them.
- High-momentum witnesses can produce very small overlaps. The script uses logarithmic quadrature and reports logs to avoid false zero/negative judgments from underflow. Numerical stability is checked for its six named cases, not every possible input.
- No Monte Carlo fit is used to infer the cubic exponent; upper and lower bounds are established analytically in [`science/cubic_distance.md`](../science/cubic_distance.md).
- The normal semigroup and Gaussian pathwise criterion are mathematical steps, not inferred from a finite truncation of the Hilbert space.
- Hosted mathematical rendering is a separate visual check. Passing the scripts does not certify how GitHub displays the pages.
