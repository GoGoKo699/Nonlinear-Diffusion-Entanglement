# Holevo-to-project source bridge

[Learning entrypoint](README.md) · [Worked primer](PRIMER.md) · [30 milestones](MILESTONES.md) · [Exact science](../science/README.md)

## One source and its verified edition

**Alexander S. Holevo, _Quantum Systems, Channels, Information: A Mathematical Introduction_, 2nd revised and expanded edition, De Gruyter, 2019.** DOI: [10.1515/9783110642490](https://doi.org/10.1515/9783110642490); print ISBN 978-3-11-064224-7; PDF ISBN 978-3-11-064249-0.

The [publisher record](https://www.degruyterbrill.com/document/doi/10.1515/9783110642490/html) identifies the edition. The [publisher-distributed preview](https://api.pageplace.de/preview/DT0400.9783110642490_A39059069/preview-9783110642490_A39059069.pdf), contents pp. XI–XV, supplies the section numbers and printed page numbers below. Locations were checked on 29 October 2026 against that preview's extracted text. The complete chapter bodies were not available in this check; no uninspected theorem number or exact wording is asserted. The source is the 2019 book, not the 2012 first edition, an unrelated review, or the author's 2008 research paper.

## Selective source route

| Book location and printed page | Use here | Project continuation |
|---|---|---|
| §§1.3–1.5, pp. 5–7; §§2.2–2.4, pp. 13–30 | Positivity, trace, convexity, states, observables and discrimination | [Primer: states and error](PRIMER.md#states-references-and-error) and [model](../science/model.md) |
| §§3.1.1, 3.1.3, pp. 33, 37; §3.3.2, p. 46 | Tensor products, purification, entanglement and local operations | Reference-qubit witnesses and [fixed-input filtering](../science/fixed_input.md) |
| §§6.1–6.4, pp. 99–111; §6.5, p. 112 | Evolutions, complete positivity, channels, EB/PPT and measurement | The stochastic model and distinction between channels and individual outputs |
| §§10.1.2, 10.2, 10.3.1, pp. 189, 195, 202 | Error-correction task, fidelity and achievable rates | [Interpretation](../science/interpretation.md): why a one-use fidelity bound is not a capacity formula |
| §11.1, p. 233; §11.5, p. 243; §11.7, p. 248 | Infinite-dimensional convergence, input constraints and EB | Normal states, unrestricted channel distance, and finite-rank approximations |
| §§12.1.1–12.1.2, pp. 255–260; §§12.2.1–12.2.3, pp. 265–272 | Self-adjoint generators, Weyl relations, symplectic transformations and quadratic dynamics | Definition by unitary displacements and shears rather than formal bounded-generator algebra |
| §§12.3.1–12.3.2, pp. 273–278; §12.3.5, p. 284 | Characteristic functions, Gaussian states, separability and purification | Covariance conventions and the finitely squeezed reference state |
| §§12.4.1–12.4.4, pp. 287–296; §§12.6.1–12.6.3, pp. 319–327 | Gaussian channels, observables, EB and the single-mode case | Apply the Gaussian criterion to each conditional component, not to their non-Gaussian mixture |

These selections provide the foundations. Reading the capacity chapters in full is not a prerequisite for the theorem. The map cites the relevant selections again where they are used.

## Local notation and normalization

The following dictionary fixes this repository's conventions. It is a translation aid, not a claim that every displayed symbol is used identically in the book.

| Object | Repository convention | Consequence |
|---|---|---|
| Canonical observables | $`R=(Q,P)^T`$, $`[Q,P]=iI`$ | Planck's constant is one; changing quadrature units changes numerical covariance thresholds. |
| Physical state covariance | $`C_{ab}=\langle\{R_a-m_a,R_b-m_b\}\rangle/2`$ | Vacuum has $`C=I_2/2`$. |
| Additive displacement noise | Classical displacement covariance $`V`$ | A centered additive channel sends $`C\mapsto C+V`$. Do not mistake $`V`$ for the total output covariance. |
| Channel picture | $`\Phi`$ acts on states; $`\Phi^*`$ on observables | $`\mathrm{Tr}[\Phi(\rho)A]=\mathrm{Tr}[\rho\Phi^*(A)]`$. |
| Distance | Half diamond norm; arbitrary input and reference; no energy bound | The factor one-half matches discrimination bias conventions. |
| Dynamical Hamiltonian | $`H=P^2/2`$ | Free motion, not harmonic confinement. |
| Preparation cost | $`H_{\mathrm{ref}}=(Q^2+P^2)/2`$ | Used only to check that a witness has finite oscillator preparation energy. |
| Logarithms | Natural logarithms in distance exponents | The statement is a logarithmic decay order, not a bit capacity. |

For a concrete characteristic-function convention, define $`W(z)=e^{iz^TR}`$. An additive centered Gaussian channel obeys

```math
\mathcal N_V^*(W(z))=e^{-z^TVz/2}W(z).
```

If a subsequent Gaussian unitary has $`U^*RU=XR`$, then the full dual channel is

```math
(\mathrm{Ad}_U\circ\mathcal N_V)^*(W(z))
=e^{-z^TXVX^Tz/2}W(X^Tz).
```

Thus the interaction-picture covariance $`V_S`$ and the output noise covariance $`X V_S X^T`$ are different matrices. Their determinants agree for a symplectic shear. This removes a possible apparent discrepancy between Schrödinger-picture covariance propagation and the project's conditional formula.

For a one-mode positive definite displacement covariance,

```math
\mathcal N_V\text{ is EB}\quad\Longleftrightarrow\quad\sqrt{\det V}\ge1.
```

The unit threshold is **noise covariance**, not the uncertainty threshold $`\sqrt{\det C}\ge1/2`$ for a quantum state. At $`V=I_2`$, heterodyne measurement followed by coherent-state preparation adds one half-unit from each operation. The primary theorem attribution remains [Holevo (2008)](../references/RELATED_WORK.md); the 2019 book is the educational anchor.

## What the bridge must add

### From channels to this unbounded dynamics

The book's channel language identifies the admissible maps and their extensions to a reference. This project additionally defines a particular normal random-unitary semigroup through Weyl displacements and free shears. For a Hermitian $`A`$,

```math
\mathcal D[A](\rho)=A\rho A-\tfrac12\{A^2,\rho\}
=-\tfrac12[A,[A,\rho]].
```

Consequently $`-D[Q,[Q,\rho]]`$ corresponds formally to jump $`\sqrt{2D}Q`$. The analogous jumps are $`\sqrt{2\kappa}H`$ and $`\sqrt{2\eta}P`$. Unbounded operators require the explicit construction in [model](../science/model.md); a finite-dimensional Lindblad theorem alone does not settle their domains.

The stochastic shear is $`S_s=\omega s+\sqrt{2\kappa}B_s`$, with standard Brownian increments of variance $`ds`$. Conditioning on this mathematical trajectory leaves linear quadrature noise. Its accumulated displacement is Gaussian. Averaging over the unobserved shear produces a channel that is generally **not Gaussian**. This stochastic reduction and its exact propagator are attributed in the [source account](../references/RELATED_WORK.md), rather than assigned to the textbook.

### From a covariance criterion to a sharp unconditional theorem

The [conditional representation](../science/conditional_gaussian.md) gives

```math
\det V_S=4D\eta t^2+4D^2t\int_0^t(S_s-\overline S)^2ds.
```

The second term is nonnegative. Once the first reaches one, every component is EB, so their mixture is EB. This gives sufficiency and includes the endpoint. Before that time, the existence of non-EB components does **not** prove that their mixture is non-EB. The separate [packet witness](../science/exact_threshold.md) proves a negative partial-transpose expectation for the actual averaged output. This is the indispensable extra step between Gaussian theory and the exact nonlinear result.

### From one witness to an all-input distance estimate

For states, half trace distance controls all measurement probability differences. The diamond norm makes the control uniform in the input and an untouched reference. In this project a bad set of Brownian paths can be replaced by state preparation, producing a genuine EB comparator; its half-diamond error is at most the probability of that set. The [Brownian spectral calculation](../science/conditional_gaussian.md) and [Chernoff argument](../science/cubic_distance.md) bound that probability. These are supplied derivations, not an implicit textbook prerequisite.

The lower estimate uses compact orthogonal packets and a bounded entanglement witness on the same channel metric. Its energy grows with time in this construction. The upper and lower logarithmic orders agree, but their leading constants do not. A single selected output would be insufficient for the upper estimate.

### From finite-energy states to the correct quantifiers

The [fixed-input proof](../science/fixed_input.md) starts from any one finitely squeezed two-mode state with strictly positive Schmidt weights. A finite-rank filter on its reference can reproduce a finite truncation of a time-dependent witness. Since local filtering preserves positivity of partial transpose, the fixed state's output cannot be PPT. The success probability may be extremely small. This proves qualitative survival without establishing a quantitative memory or communication rate.

## Where the book ends and the project begins

The anchor supplies a systematic language for channels, infinite-dimensional inputs and Gaussian systems. The research contribution is the specified nonlinear mixture's exact boundary, the singular Gaussian comparison and the cubic all-input distance law. The known model, Mehler propagator, Gaussian EB criterion, Brownian identities and filtering method retain their individual attribution. A proof's short length, or the availability of a textbook foundation, does not establish novelty; [related work](../references/RELATED_WORK.md) records the scoped comparison.
