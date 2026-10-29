# Verification and reproduction

[Project](../README.md) · [Scientific statements](../science/model.md) · [Learning route](../learning/README.md)

The analytical proofs in `science/` establish the universal and asymptotic claims. The programs here test selected finite cases, normalizations, constants and the consistency of the learning route. Successful computation is not independent proof certification, an exhaustive novelty review or evidence of a practical quantum-memory advantage.

## Numerical and structural checks

With Python 3.12 and the pinned NumPy/SciPy versions:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r verification/requirements.txt
.venv/bin/python verification/run_checks.py
```

The runner executes four modules and prints its complete JSON report. Fresh reports are written to the ignored directory `verification/local_results/`. Before importing the checks it atomically replaces `checks.json` with `status: running` and `all_assertions_passed: false`. Each completed module updates that report. A failure records the active module and exception and exits unsuccessfully; interruption cannot leave an earlier passing report masquerading as the current run. Only `status: passed` together with `all_assertions_passed: true` denotes a complete run.

| Module | What is checked | What is not established |
|---|---|---|
| [check_threshold.py](check_threshold.py) | Six positive-kappa Gaussian-packet cases: independently evaluated coherence and diagonal integrals, their analytical bounds and expected witness signs | Universal sharpness, the endpoint, optimal witness energy |
| [check_bounds.py](check_bounds.py) | Cosine-packet overlap integral and constant, five finite spectral Laplace comparisons, Gaussian determinants, Gaussian cutoff and nine packet-parameter inequality cases | Optimal cubic coefficient, full diamond-distance computation |
| [check_learning.py](check_learning.py) | Qubit generator/Bell-state example, three deterministic covariance examples, rate rescaling, Brownian trace, packet moments, squeezed-state energy and bounded finite-rank filtering | The infinite-dimensional theorem from finite truncations |
| [check_repository.py](check_repository.py) | Exactly M01–M30, 12/18 phase split, required target fields, backward-only dependencies, local file/section links, source bridge routes and topic-based science | Scientific truth, external-link availability, actual hosted mathematical rendering |

For the threshold cases, the expected NPT-sign pattern is `true, true, false, false, true, true`. The two nonnegative tested witnesses at or above the threshold are consistent checks, not independent proofs of EB. The exact overlap constant is `2/3 + 5/pi**2`, and the cubic lower-bound constant evaluates to approximately `0.02153222609588753`.

The committed [reference_results.json](reference_results.json) records the earlier research-stage summary. It is not a fresh-run manifest and does not include the later learning/structure checks. Compare a new run's actual outputs rather than treating this historical reference as evidence that the new code executed.

## Actual hosted-rendering check

Source syntax and numerical success do not establish how GitHub displays equations. The separate [check_hosted.py](check_hosted.py) opens the **actual public GitHub pages at a full commit SHA**, waits for rendered math, rejects rendering-error nodes and records screenshots, page text and a page-by-page manifest.

```bash
.venv/bin/python -m pip install -r verification/requirements-render.txt
.venv/bin/python -m playwright install --with-deps chromium
SOURCE_REF="$(git rev-parse HEAD)" .venv/bin/python verification/check_hosted.py
```

This check requires network access to GitHub and a compatible Chromium runtime. It inspects the README, learning primer, source bridge, milestone map and three mathematical proof pages. Evidence is written under `verification/local_results/hosted/`. The automated DOM checks detect missing math and reported rendering errors; screenshots must also be inspected for visual readability, clipping and table layout. An unavailable hosted check remains a presentation-verification gap, not a successful local preview.

The workflow in `.github/workflows/verify.yml` runs the numerical/structural checks and the hosted-page capture for pull requests and main. It records the tested head SHA and uploads fresh reports, screenshots and an exact `git archive` of that source. Artifacts expire after seven days; durable findings and any required retained evidence belong in the final verification record, not solely in an expiring download link.

## Scientific sanity boundaries

The central consistency checks must retain the same conventions throughout the README, model, proofs and learning route: $[Q,P]=i$, $H=P^2/2$, positive $D,\kappa$, nonnegative $\eta$, vacuum covariance $I/2$, added Gaussian covariance threshold $\sqrt{\det V}=1$, and **half** diamond distance. The $\eta$ noise is momentum dephasing/position diffusion; the $D$ noise is position dephasing/momentum diffusion.

The sharp theorem includes the finite EB endpoint and proves NPT strictly below it. The cubic law concerns $\eta=0$ and fixed rates, and its leading exponent constant is not optimized. A fixed finitely squeezed input gives qualitative NPT, while the quantitative compact-packet construction has a growing sufficient preparation cost. None of these claims establishes positive quantum capacity or useful storage. Full source attribution remains in [related work](../references/RELATED_WORK.md).
