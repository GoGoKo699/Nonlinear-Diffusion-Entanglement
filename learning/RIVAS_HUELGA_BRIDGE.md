# Rivas–Huelga to nonlinear diffusion

[Learning route](README.md) · [30 milestones](MILESTONES.md) · [Model](../science/model.md)

## One anchor and two numbering systems

The educational anchor is **Ángel Rivas and Susana F. Huelga, _Open Quantum Systems: An Introduction_ (SpringerBriefs in Physics, 2012)**, DOI [10.1007/978-3-642-23354-8](https://doi.org/10.1007/978-3-642-23354-8). The freely available author text is [arXiv:1104.5242v2](https://arxiv.org/abs/1104.5242v2), revised **9 February 2012**; its [PDF](https://arxiv.org/pdf/1104.5242v2) fixes the section and equation numbering used below. These are two versions of the same selected source, not two educational anchors.

The printed book starts its mathematical material at Chapter 1; the author text includes an introductory Section 1, shifting the corresponding sections by one. A bare section number in this bridge always means **author version v2**. Book locations are supplied explicitly rather than silently mixing the two editions. Printed pagination and author-PDF pagination are not interchangeable.

| Foundation needed here | Printed book | Author v2 | Project connection |
|---|---|---|---|
| Norms and evolution families | Chapter 1, especially 1.1–1.3 | 2.1–2.3 | Trace-class states, contractions, semigroup composition |
| Unitary evolution and interaction pictures | Chapter 2 | 3 | Remove the stochastic free shear before treating linear noise |
| Channels valid for unknown inputs and references | 3.1–3.2 | 4.1–4.2 | Completely positive trace-preserving maps and the untouched reference |
| Trace-norm contraction and reversible dynamics | 3.3–3.4 | 4.3–4.4 | Operational error bounds and why general noise is not invertible |
| Markov composition and generators | 3.5 and 4.2 | 4.5 and 5.2 | Independent increments and the double-commutator generator |
| Stationary behavior and its assumptions | 4.4 | 5.4 | A warning: proximity to the EB set is not relaxation to a stationary state |

The publisher's chapter list and the author version's contents and Eq. (51) were checked on **29 October 2026**. These selected locations are a route into the project; reading every chapter is not required. The microscopic weak-coupling and non-Markovian chapters are not prerequisites for the specified random-unitary model.

## Notation and rate translation

The source's dynamical map becomes $\Phi_t$ here. Its generator becomes $\mathcal L$. In the source's Eq. (51), a self-adjoint jump $A$ with coefficient $\gamma$ contributes

```math
\gamma\left(A\rho A-\frac12\{A^2,\rho\}\right)
=-\frac\gamma2[A,[A,\rho]].
```

Therefore the coefficients in this project translate as follows:

| Project term | Source-style jump | Source-style rate |
|---|---|---|
| $-D[Q,[Q,\rho]]$ | $Q$ | $2D$ |
| $-\kappa[H,[H,\rho]]$ | $H=P^2/2$ | $2\kappa$ |
| $-\eta[P,[P,\rho]]$ | $P$ | $2\eta$ |

The deterministic Hamiltonian in that convention is **$\omega H$**, not $H$ alone. In particular, replacing $H$ by $P^2$ without rescaling its coefficients changes the model.

The commutator convention is $[A,B]=AB-BA$ and $\hbar=1$. Quadratures obey $[Q,P]=iI$. For a state, use the symmetrized covariance; the vacuum covariance is $I/2$. The matrix $V_S$ in the proof is instead the **classical covariance of added physical displacements**. It is added to a state's covariance. Isotropic additive covariance $I$ is the heterodyne measure-and-prepare boundary, so the one-mode condition is $\sqrt{\det V_S}\ge1$, not $1/2$.

The energy label $H_{\rm ref}=(Q^2+P^2)/2$ measures preparation resources. It does not describe an extra trapping term in the noisy evolution. The untouched reference and this reference energy are different uses of the word reference.

## The finite-dimensional boundary of the source

The author text states in its introduction that important mathematical proofs are restricted to finite dimensions. Its discussion after Eq. (51) also distinguishes bounded-generator infinite-dimensional results. The operators $Q$, $P$ and $P^2/2$ here are unbounded. Writing a Lindblad-looking expression is consequently not, by itself, an existence proof for this channel.

The project supplies that missing step in [the model](../science/model.md) and [conditional representation](../science/conditional_gaussian.md): construct each unitary trajectory through Weyl displacements and free shears, average its action on normal trace-class states, and use independent Brownian increments for semigroup composition. On the appropriate Schwartz core, the construction has the stated formal generator. This gives a well-defined normal channel without importing a finite-matrix exponential argument outside its domain.

The same caution applies to steady states. The source's finite-dimensional steady-state discussion is useful for recognizing what a relaxation claim would mean. It does not establish a normal stationary state for this unconfined particle. Here the EB comparator changes with $t$; no convergence to a single stationary state is asserted.

## From dephasing to Brownian motion

For a self-adjoint operator $A$, random unitary increments with angle variance $2c\,dt$ give, on a suitable core,

```math
\mathbb E\!\left[e^{-iA\,d\theta}\rho e^{iA\,d\theta}\right]
=\rho-c[A,[A,\rho]]\,dt+o(dt).
```

The linear term averages to zero and the second-order term contains half the angle variance. For a finite-dimensional teaching example, set $A=Z$; an off-diagonal qubit entry then decays as $e^{-4ct}$. The complete Bell-state calculation is in [the primer](README.md#2-a-complete-two-level-example), with executable checks.

For the project, independent Brownian motions multiply $Q,H,P$ with amplitudes $\sqrt{2D},\sqrt{2\kappa},\sqrt{2\eta}$. This interpretation supplies the meaning of the rates; the unbounded-domain construction remains the separate step above. Averaging over an unobserved environment does not provide a noise record for recovery.

## From an interaction picture to a conditional Gaussian channel

Define $S_s=\omega s+\sqrt{2\kappa}B_s$ and $U_{S_s}=e^{-iS_sP^2/2}$. The canonical commutator gives

```math
U_{S_s}^{\dagger}Q U_{S_s}=Q+S_sP.
```

At a fixed shear path, the interaction-picture noise is linear in $Q,P$. Commutators of such linear expressions are scalars, so the ordering phase disappears when a density operator is conjugated. The remaining average is a Gaussian displacement channel. The [canonical calculation](../science/conditional_gaussian.md) gives its covariance and the identity

```math
\det V_S=4D\eta t^2+
4D^2t\int_0^t(S_s-\overline S)^2ds.
```

The two terms have distinct roles: a path-independent floor from complementary diffusion, and a nonnegative area generated by temporal variation of the shear. Averaging over paths generally produces a non-Gaussian channel. Gaussian criteria are used **before** that average, not applied to the total channel's averaged covariance.

## Reference-assisted entanglement and distance

The source's complete-positivity discussion motivates adjoining an untouched reference. The project adds three different tests:

* EB is a universal condition on **every** joint input. Measure-and-prepare channels satisfy it and remain EB under channel pre- and postprocessing and mixtures.
* An NPT witness has nonnegative expectation on separable states. A negative value on one actual output disproves EB; failure to find a negative value is not a separability proof.
* Half-diamond distance compares complete channels uniformly on inputs and references. If an EB comparator differs only on conditional paths of total probability $p$, convexity bounds that distance by $p$.

These additions are supplied by the [model](../science/model.md), [threshold proof](../science/exact_threshold.md) and [distance proof](../science/cubic_distance.md). The primary Gaussian EB criterion is attributed to Holevo in [related work](../references/RELATED_WORK.md); that paper is a research dependency, not a replacement educational anchor.

## The bridge to the three results

**Sharp boundary.** The covariance floor proves the sufficient side, including equality. For necessity the project uses normalizable momentum packets with a qubit reference, an exact Mehler-kernel integral, and a comparison between coherence and wrong-packet leakage. The positive quadratic coefficient $1/(Dt)-4\eta t$ determines the strict pre-threshold region. This is a mixture-level witness proof, not an inference from the existence of a favorable trajectory.

**Cubic operational proximity.** The project derives the spectrum and Laplace transform of centered Brownian motion's integrated square. A Chernoff estimate bounds the exceptional-path probability. An independently normalized compact-packet witness supplies the lower bound in the same half-diamond norm. Matching logarithmic order does not identify the optimal coefficient in the exponent.

**One fixed input.** The project first obtains an NPT witness for each time, then truncates it in a number basis and realizes the truncated input by a bounded local filter on a fixed two-mode squeezed state. This reverses neither the filtering probability nor the order of quantifiers: the input is fixed, while the test/filter may depend on time. No uniform detectable entanglement amount follows.

The [30-milestone map](MILESTONES.md) assigns these links their dependencies. The scientific pages remain authoritative for statements, domains, proof constants and primary attribution; this bridge supplies the missing conceptual connections rather than a second competing proof record.
