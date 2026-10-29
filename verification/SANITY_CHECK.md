# Furnishing and Sanity Check

This record separates scientific consistency, reproducibility, learning-route integrity and hosted presentation. It is not independent peer review or a bibliographic-priority certificate.

## Scope

Scientific baseline: `5b66564950f2a4b2d048e47859fd3453053ade02`. The furnished route uses one source, Holevo's second revised and expanded edition (2019), and adds no new research claim. The only scientific-prose correction describes the Mehler kernel's **logarithmic decay** as linear in large momentum difference; the former wording could be read as linear decay of the kernel itself. Its displayed equations and bounds are unchanged.

The model, exact threshold, conditional covariance, packet comparison, cubic bounds, fixed-input argument and Gaussian comparison were checked for consistent assumptions and conventions against the new explanations. In particular: positive kinetic dephasing is not silently replaced by zero; the physical mixture has no observed path record; state and noise covariance are distinct; preparation energy is not the dynamical Hamiltonian; qualitative NPT is not capacity.

## Performed checks

The four scientific Python sources were reconstructed from the live baseline and their Git blob hashes matched the fetched files before execution. A fresh `python3 verification/run_checks.py --output <local-file>` passed in Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0. All six threshold cases passed the declared signs and inequalities. Maximum packet-reduction discrepancy was `2.77555761450245e-16`; maximum finite-difference generator residual was `2.011311930879738e-09`. The bounds and semigroup-composition checks also passed. These are finite floating-point tests, not universal proofs or interval certificates.

`python3 verification/check_learning.py` checks exactly M01–M30, the 14/16 phase allocation, six required fields per milestone, earlier-only dependencies, a single anchor, local Markdown destinations and heading fragments, paired code fences, the primer's partial-transpose eigenvalues and its Gaussian determinant/cutoff example. The map's local-to-global progression and source/claim alignment are additionally reviewed in prose; syntactic tests alone cannot establish pedagogical quality.

The source bridge's edition, section numbers and page locations were checked against the publisher-distributed preview's extracted contents. The preview does not supply all chapter bodies. No detailed theorem numbering or exact source wording was invented. The primary-source attribution and existing research comparison remain in [related work](../references/RELATED_WORK.md).

A local pdfLaTeX draft-mode syntax check of the extracted mathematical expressions passed. This checks TeX syntax only; it is not a MathJax or hosted-page visual check.

## Presentation limitation

**Actual hosted visual mathematical rendering remains unverified.** The GitHub connector returns Markdown source for blob URLs, not rendered page pixels. A direct hosted-page request failed, and the available connected tools do not provide a live-browser screenshot. Source/link checks and any local TeX syntax compilation do not substitute for inspecting the actual GitHub README, learning pages and representative proof pages. Therefore this record does not assert an unqualified release-ready Sanity Check.

The remaining hosted inspection should cover `README.md`, `learning/PRIMER.md`, `learning/HOLEVO_BRIDGE.md`, `learning/MILESTONES.md`, `science/exact_threshold.md` and `science/cubic_distance.md`, including long equations and tables. No scientific gap was identified by the consistency checks above; presentation readiness is a separate verification state.
