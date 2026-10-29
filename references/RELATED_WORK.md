# Literature comparison and attribution

Checked against relevant primary records and the author's accessible portfolio during the October 29, 2026 exploration, then carried into scientific integration. This is a **bounded** comparison, not an exhaustive priority or publication certificate. The contribution is an entanglement theorem for a **known** exactly solvable diffusion, not a new model or solution method.

## Attribution matrix

| Ingredient or result | Status and precedent | What remains here |
|---|---|---|
| Hermitian $Q$ and $P^2/2$ dephasing, non-Gaussian Grushin diffusion and Mehler propagator | **Inherited:** Speed–Lyu–Schubert (2023), model Eqs. 18–22 and propagator Eqs. 58–62 | Operational EB/PPT classification and normalized reference witnesses |
| Gaussian-channel EB condition and heterodyne measure-and-prepare realization | **Inherited:** Holevo (2008) | Applied pathwise, then matched by a new *mixture-level* converse |
| Finite-time Gaussian Brownian measurement and deterministic-shear spreading | **Inherited:** Riedel (2016); related Wigner/P positivity Diósi–Kiefer (2002) | Exact singular change after stochastic quadratic shear |
| Neumann cosine Brownian spectral expansion and $\sinh$ product | **Established probability identities** | Reference-uniform cubic channel-distance theorem |
| PPT witnesses and exact vs approximate EB distinction | **Standard:** including finite-dimensional dephasing and large-spin cases | Specific exact $\eta$ boundary, noncompact all-time NPT and cubic log law |
| Sharp $t_{\rm EB}=(2\sqrt{D\eta})^{-1}$ for $\kappa>0$, NPT below | **Derived in this repository** | Scope is the specified free, one-mode nonlinear Markov family |
| $-\log e(t)=\Theta(D^2\kappa t^3)$ for $\eta=0$ | **Derived in this repository** | Upper is an energy-unconstrained channel estimate; leading exponent constant is not optimized |
| Fixed-TMSV NPT corollary | **Derived using standard faithful-state filtering** | Not a practical coding or capacity guarantee |

## Closest external works

**Speed, Lyu and Schubert — Beyond Gaussian Quantum Channels: A model case** (2023), [arXiv:2305.08467v1](https://arxiv.org/abs/2305.08467v1). The paper introduces exactly the free-particle position/kinetic-dephasing model, its Grushin geometry and an integral/Mehler propagator. It analyzes Gaussian-state propagation, approximation accuracy and entropy. It receives full credit for the physical model and solution technique. The inspected version did not establish the sharp all-reference EB/PPT threshold or the cubic diamond estimate. This does not rule out uninspected external sources.

**Holevo — Entanglement-breaking channels in infinite dimensions**, *Problems of Information Transmission* **44**, 171–184 (2008), [arXiv:0802.0235](https://arxiv.org/abs/0802.0235), [DOI](https://doi.org/10.1134/S0032946008030010). The Gaussian criterion, its one-mode additive-noise specialization and measure-and-prepare structure are inherited. A Gaussian property of each conditional component is **not** by itself a theorem about the full non-Gaussian mixture.

**Riedel — Quantum Brownian motion as an iterated entanglement-breaking measurement by the environment**, *Physical Review A* **93**, 012107 (2016), [arXiv:1507.04083](https://arxiv.org/abs/1507.04083), [DOI](https://doi.org/10.1103/PhysRevA.93.012107). Finite-time EB under quadratic deterministic Hamiltonians and *linear* Lindblad operators is an essential Gaussian comparison. Stochastic $P^2/2$ Lindblad noise violates the total-Gaussian hypothesis.

**Diósi and Kiefer — Exact positivity of the Wigner and P-functions of a Markovian open system**, *Journal of Physics A* **35**, 2675 (2002), [arXiv:quant-ph/0111139](https://arxiv.org/abs/quant-ph/0111139). Free motion and position diffusion already yield finite-time Wigner/P positivity; this is not automatically equivalent to the reference-uniform EB property and has no kinetic-dephasing jump.

**Schubert and Plastow — Decoherence Time Scales and the Hörmander Condition** (2023), [arXiv:2307.08799](https://arxiv.org/abs/2307.08799). Noise spreading, Grushin/hypoelliptic geometry and its time scales are established background, not concepts newly introduced here.

**Hanson, Rouzé and Stilck França — Eventually entanglement breaking Markovian dynamics: Structure and characteristic times**, *Annales Henri Poincaré* **21**, 1517–1571 (2020), [DOI](https://doi.org/10.1007/s00023-020-00906-4). Finite-dimensional eventual/asymptotic EB results prevent an originality claim for merely distinguishing finite from infinite EB time. The theorem's finite-dimensional assumptions do not give the present unbounded-oscillator classification.

**Bardet et al. — Group transference techniques for the estimation of decoherence times and capacities of quantum Markov semigroups**, *IEEE Transactions on Information Theory* (2021), [arXiv:1904.11043](https://arxiv.org/abs/1904.11043). The broad idea of transferring classical probability estimates to quantum-channel norms is inherited; its compact group/finite representation framework does not imply this result.

**Shchukin and van Loock — Separability rigidity of Gaussian states under positive domination**, [arXiv:2609.36336v2](https://arxiv.org/abs/2609.36336) (2026). Its positive EB-subchannel implication has a **Gaussian total-channel** hypothesis. Here the total channel is non-Gaussian despite its Gaussian components, so the theorem is not transferred without the relevant assumption.

**Szczygielski and Chruściński**, [arXiv:2407.16583v2](https://arxiv.org/abs/2407.16583); **Bhat, Dey and Saha**, [arXiv:2609.24168](https://arxiv.org/abs/2609.24168): the inspected eventual-EB classifications are over finite matrix algebras, not this unbounded noncompact semigroup.

## Internal contribution comparison

The [Spin-Diffusion-Classicalization project](https://github.com/GoGoKo699/Spin-Diffusion-Classicalization/tree/48547a557c0a1ce0ef54f3d251824ff80d0f46ca) already shows a large-spin channel uniformly close to EB while retaining exponentially small NPT Choi-sector entanglement. The **qualitative distinction is shared foundation**, not a separate discovery. That model is an irreducible compact spin in a large-$j$ limit; its theorems do not transfer to the present infinite-dimensional quadratic shear, exact $\eta$ threshold and cubic all-time channel bound.

The [Bosonic-Phase-Memory project](https://github.com/GoGoKo699/Bosonic-Phase-Memory/tree/aa346e09df1d52381a77ae08ac3677fda8c64b8b) studies a *commuting compact angular number-phase channel* and an exact code-optimization angular-cell law. Its uniform phase twirl and nondegenerate number spectrum do not apply to simultaneous noncommuting $Q$ and $P^2/2$ diffusion. Autonomous entanglement stabilization and environmental record coherence projects have different tasks and accessible resources. No unproved transfer or sister relationship is asserted.

## Consequential remainder and unresolved priority risk

The new, scoped remainder is the **exact EB/PPT time under stochastic quadratic noise**, the **singular change relative to the Gaussian $\kappa=0$ member**, and a **uniform cubic logarithmic EB-distance law certified by finite-energy inputs**. It does not imply useful quantum storage or any universal nonlinear-noise theorem. Specialized exact-solvability papers, newer uninspected preprints or parallel results could narrow the novelty case; the primary-source screen is evidence, not independent expert review.
