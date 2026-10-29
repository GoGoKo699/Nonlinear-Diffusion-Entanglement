# Thirty milestones

[Learning entrypoint](README.md) · [Holevo bridge](HOLEVO_BRIDGE.md) · [Worked primer](PRIMER.md)

This learner-independent map has exactly **30 understanding targets**: 14 background/preliminaries targets and 16 narrative/innovation targets. The first phase assembles the operational question from local objects; the second assembles the answer from its mechanism and proof components. Dependencies refer only to earlier milestones. The map does not prescribe assessments or claim coverage of every technical detail.

All numbered book sections refer to the **second revised and expanded edition (2019)** of Holevo, the single educational anchor. Section locations and the distinction between textbook foundations and locally supplied derivations are documented in the [bridge](HOLEVO_BRIDGE.md).

## Background and preliminaries — M01–M14

### M01 — States and measurement probabilities

**Central question:** What mathematical object describes the noisy carrier?

**Understanding target:** Interpret a positive trace-one operator and compute a measurement probability; distinguish a state from a generator.

**Dependencies:** None.

**Story role:** Start with the local object on which every channel acts.

**Conceptual connection:** Positivity and trace normalization become the normal-state contract.

**Sources:** Holevo §§1.3–1.5, 2.2–2.3; [model](../science/model.md).

### M02 — The untouched reference

**Central question:** Why test a channel on half of an entangled state?

**Understanding target:** Explain tensor products and purification, and why preservation of an isolated input can miss lost correlations.

**Dependencies:** M01

**Story role:** Extend one carrier to the relevant joint experiment.

**Conceptual connection:** The reference is a diagnostic system, not a protected bypass available to an encoder.

**Sources:** Holevo §§3.1.1, 3.1.3; [primer](PRIMER.md#states-references-and-error).

### M03 — A negative partial-transpose witness

**Central question:** How can a bounded observable certify entanglement?

**Understanding target:** Distinguish a negative partial-transpose expectation from a negative probability; explain why separable states cannot produce it.

**Dependencies:** M01, M02

**Story role:** Introduce the local certificate used in the converse.

**Conceptual connection:** The Bell example gives a finite-dimensional model of the packet witness.

**Sources:** Holevo §6.4; [primer](PRIMER.md#worked-example-a-qubit-can-be-almost-classical-without-being-eb).

### M04 — Completely positive channels

**Central question:** Why must a physical map remain positive beside a reference?

**Understanding target:** Explain complete positivity and trace preservation, and distinguish a channel from one measurement branch.

**Dependencies:** M01, M02

**Story role:** Specify admissible transformations rather than just outputs.

**Conceptual connection:** Averaging unitary conjugations defines the channel on normal states.

**Sources:** Holevo §§6.1–6.3; [model](../science/model.md).

### M05 — Measurement and preparation

**Central question:** What does it mean for a channel to break all entanglement?

**Understanding target:** Explain the all-input EB property, its measure-and-prepare meaning, and its distinction from a single separable output.

**Dependencies:** M03, M04

**Story role:** Identify the comparison class.

**Conceptual connection:** Composition and convex averaging preserve EB; one non-EB component need not survive averaging.

**Sources:** Holevo §§6.4–6.5, 11.7; [conditional channel](../science/conditional_gaussian.md).

### M06 — Operational error with a reference

**Central question:** What does a small half-diamond distance guarantee?

**Understanding target:** Distinguish state trace distance, a selected-output test and the reference-uniform channel norm; retain the one-half convention.

**Dependencies:** M02, M04, M05

**Story role:** Turn qualitative classicality into a quantitative question.

**Conceptual connection:** A probability bound on bad trajectories will control every allowed experiment.

**Sources:** Holevo §2.4 for state discrimination and §6.3 for channels; the diamond extension is supplied in [primer](PRIMER.md#states-references-and-error) and [model](../science/model.md).

### M07 — Canonical observables and shears

**Central question:** How does free motion move a phase-space point?

**Understanding target:** Read the commutator and Weyl notation and explain why a quadratic Hamiltonian shears one quadrature by the other.

**Dependencies:** M01, M04

**Story role:** Introduce this physical carrier.

**Conceptual connection:** The identity U* Q U = Q + S P converts kinetic noise into random shear.

**Sources:** Holevo §§12.1.1–12.1.2, 12.2.1–12.2.3; [bridge](HOLEVO_BRIDGE.md#local-notation-and-normalization).

### M08 — Normal states and finite preparation energy

**Central question:** Which idealized vectors are not admissible inputs?

**Understanding target:** Distinguish trace-class states, plane-wave distributions, finite reference-oscillator energy and a uniform energy constraint.

**Dependencies:** M01, M07

**Story role:** Keep infinite-dimensional resources explicit.

**Conceptual connection:** The dynamical free Hamiltonian differs from the oscillator cost used for witnesses.

**Sources:** Holevo §§11.1, 11.5; [model](../science/model.md) and [bridge](HOLEVO_BRIDGE.md#local-notation-and-normalization).

### M09 — State covariance versus noise covariance

**Central question:** Which matrix measures added classical displacement?

**Understanding target:** Explain the vacuum covariance I/2 and the separate noise matrix V in C -> C+V; track quadrature ordering.

**Dependencies:** M07, M08

**Story role:** Fix the numerical normalization before applying Gaussian theory.

**Conceptual connection:** A state uncertainty bound and an EB noise threshold have different factors.

**Sources:** Holevo §§12.3.1–12.3.2, 12.4.1–12.4.2; [bridge](HOLEVO_BRIDGE.md#local-notation-and-normalization).

### M10 — The one-mode Gaussian EB criterion

**Central question:** How much additive noise suffices for measurement and preparation?

**Understanding target:** Use sqrt(det V) >= 1 in this normalization; explain the endpoint and invariance under symplectic shears.

**Dependencies:** M05, M09

**Story role:** Obtain the conditional theorem ingredient.

**Conceptual connection:** Heterodyne measurement and coherent preparation account for the unit noise threshold.

**Sources:** Holevo §§12.4.3–12.4.4, 12.6.2–12.6.3; [conditional criterion](../science/conditional_gaussian.md).

### M11 — A mixture is not an observed trajectory

**Central question:** What changes when the environmental record is discarded?

**Understanding target:** Distinguish conditioning used in analysis from a receiver-accessible record; explain why a mixture of Gaussian channels can be non-Gaussian.

**Dependencies:** M04, M05, M10

**Story role:** Move from local components to the physical average.

**Conceptual connection:** Convexity gives the upper implication but not the mixture-level converse.

**Sources:** Holevo §§1.5, 6.5, 12.4; [primer](PRIMER.md#from-the-example-to-a-random-shear).

### M12 — Markov evolution and Brownian increments

**Central question:** How do repeated random unitary increments define a semigroup?

**Understanding target:** Explain independent increments, variance proportional to elapsed time, and composition of the averaged channels.

**Dependencies:** M04, M07, M11

**Story role:** Add the time structure needed by the model.

**Conceptual connection:** The stochastic construction supplies an unbounded-generator definition; it is not inferred from finite matrices.

**Sources:** Holevo §6.1 and §12.2.3 as foundations; Brownian construction supplied in [model](../science/model.md) and [conditional representation](../science/conditional_gaussian.md).

### M13 — Hermitian jumps and factors of two

**Central question:** Which physical diffusion is generated by each double commutator?

**Understanding target:** Translate -D[Q,[Q,rho]] into jump sqrt(2D)Q; distinguish Q-generated momentum diffusion from P-generated position diffusion.

**Dependencies:** M07, M12

**Story role:** Connect master-equation notation to stochastic displacements.

**Conceptual connection:** The eta floor is position diffusion, even though its jump is P.

**Sources:** Holevo §6.1 as evolution background; local derivation in [bridge](HOLEVO_BRIDGE.md#from-channels-to-this-unbounded-dynamics) and [model](../science/model.md).

### M14 — Background synthesis

**Central question:** What must be specified before claiming that a channel becomes classical?

**Understanding target:** Assemble inputs, reference, normality, energy convention, hidden environment, EB class, norm and time dependence into one operational contract.

**Dependencies:** M03, M05, M06, M08, M10, M11, M12, M13

**Story role:** Close the background phase with the complete question.

**Conceptual connection:** Separate an existential entanglement witness from a uniform approximation theorem.

**Sources:** Holevo §§6.3–6.4, 11.1, 11.7, 12.4; [model](../science/model.md) and [primer](PRIMER.md).

## Narrative and innovation — M15–M30

### M15 — The nonlinear diffusion contract

**Central question:** Which parameters and resources define the theorem?

**Understanding target:** State D,kappa>0, eta>=0 and finite real drift; separate the kappa=0 Gaussian comparison from the positive-kappa theorem.

**Dependencies:** M14

**Story role:** Start the research narrative with its exact domain.

**Conceptual connection:** The same symbols and resources govern both proof directions.

**Sources:** Holevo §§11.1, 12.2.3; [model](../science/model.md).

### M16 — Conditioning on the kinetic shear

**Central question:** Why is the conditional channel Gaussian?

**Understanding target:** Explain the interaction picture and why scalar commutators leave only an irrelevant global phase in linear-noise time ordering.

**Dependencies:** M07, M11, M12, M13, M15

**Story role:** Expose the mechanism before its consequence.

**Conceptual connection:** A fixed quadratic-noise path turns the remaining dynamics into Gaussian displacement plus a shear.

**Sources:** Holevo §§12.2.1–12.2.3, 12.4.1; [conditional representation](../science/conditional_gaussian.md).

### M17 — Noise area as temporal variance

**Central question:** What does the conditional determinant measure?

**Understanding target:** Read det V_S as a deterministic floor plus a nonnegative centered-path variance and explain why a constant path has no variance term.

**Dependencies:** M09, M16

**Story role:** Reduce the matrix criterion to a scalar quantity.

**Conceptual connection:** The Gram determinant converts path geometry into an entanglement threshold.

**Sources:** Holevo §12.2.2 and §12.4.4; [conditional determinant](../science/conditional_gaussian.md).

### M18 — The pathwise upper bound and its endpoint

**Central question:** Why is the channel EB at and after the proposed time?

**Understanding target:** Combine the floor 4D eta t² with the Gaussian criterion and convexity, retaining equality at the boundary.

**Dependencies:** M05, M10, M17

**Story role:** Establish one direction of the sharp theorem.

**Conceptual connection:** A statement true for every conditional path survives averaging without an observed environment.

**Sources:** Holevo §§11.7, 12.4.4, 12.6.2; [threshold upper proof](../science/exact_threshold.md).

### M19 — Why exceptional paths are not a converse

**Central question:** Why do non-EB conditional channels fail to prove non-EB of their mixture?

**Understanding target:** Identify the invalid reverse-convexity inference and explain what an unconditional output witness must establish instead.

**Dependencies:** M03, M11, M18

**Story role:** Expose the gap between sufficiency and sharpness.

**Conceptual connection:** The subsequent packet calculation is necessary, not a decorative second proof.

**Sources:** Holevo §§1.5, 6.4; [primer](PRIMER.md#why-the-converse-needs-a-new-argument) and [threshold proof](../science/exact_threshold.md).

### M20 — Momentum kernel and inherited solvability

**Central question:** How does the master equation become a harmonic heat problem?

**Understanding target:** Explain the center/difference coordinates and the roles of diffusion, the quadratic potential, drift phase and eta damping.

**Dependencies:** M07, M13, M15, M19

**Story role:** Introduce the exact computational tool for the converse.

**Conceptual connection:** The Mehler propagator is inherited; the entanglement comparison uses it in a new task.

**Sources:** Holevo §12.1.2 for representation background; [kernel derivation](../science/exact_threshold.md) and [attribution](../references/RELATED_WORK.md).

### M21 — Normalized packets with a qubit reference

**Central question:** How can nonorthogonal packets produce a normalized joint input?

**Understanding target:** Use orthogonal reference labels to normalize the superposition; distinguish coherence from opposite-packet leakage.

**Dependencies:** M02, M03, M08, M20

**Story role:** Build a physical rather than distributional witness.

**Conceptual connection:** Reference labels, finite preparation cost and the sign of the partial-transpose expectation are all explicit.

**Sources:** Holevo §§3.1.1, 3.1.3, 6.4; [Gaussian packet witness](../science/exact_threshold.md).

### M22 — A finite-energy inequality certificate

**Central question:** Why can a large but finite packet separation witness NPT?

**Understanding target:** Compare the quadratic leakage exponent with coherence damping after setting width to the inverse separation; retain positive kappa.

**Dependencies:** M20, M21

**Story role:** Turn a formal asymptotic into an actual finite witness.

**Conceptual connection:** A positive quadratic coefficient eventually dominates the linear and logarithmic terms.

**Sources:** Holevo §§11.1, 12.1.2 as foundations; [packet bounds and sharpness](../science/exact_threshold.md).

### M23 — Exact-threshold synthesis

**Central question:** How do the two directions establish the complete EB/PPT interval?

**Understanding target:** Combine EB including the endpoint with NPT at every earlier time, and distinguish absence of a finite cutoff from zero noise.

**Dependencies:** M18, M19, M22

**Story role:** Integrate the first main theorem.

**Conceptual connection:** The same parameter convention gives an exact boundary rather than incomparable upper and lower times.

**Sources:** Holevo §§6.4, 11.7; [exact threshold](../science/exact_threshold.md).

### M24 — The centered Brownian functional

**Central question:** Why does the time dependence produce a cubic scale?

**Understanding target:** Explain Brownian rescaling, removal of the temporal mean and the cosine covariance spectrum; distinguish centered Brownian motion from a bridge.

**Dependencies:** M12, M17

**Story role:** Introduce the probability ingredient for the norm theorem.

**Conceptual connection:** The integrated squares share a distribution with a bridge, but the processes are not identical.

**Sources:** Holevo §1.2 for spectral background; probability derivation supplied in [conditional representation](../science/conditional_gaussian.md).

### M25 — Rare paths give a uniform channel upper bound

**Central question:** How does a probability become a half-diamond estimate?

**Understanding target:** Replace the exceptional conditional channels by state preparation, then apply the Laplace transform and Chernoff bound without restricting input energy.

**Dependencies:** M05, M06, M10, M16, M24

**Story role:** Convert probability into an operational all-input statement.

**Conceptual connection:** The EB comparator is time-dependent; no convergence to a fixed stationary state is implied.

**Sources:** Holevo §§6.4, 11.7; [cubic upper proof](../science/cubic_distance.md).

### M26 — Compact packets give a matching logarithmic lower order

**Central question:** Why use exactly orthogonal packets for the distance lower bound?

**Understanding target:** Explain the bounded witness norm, common packet weight and positive real coherence estimate; keep their normalization and energy finite.

**Dependencies:** M03, M06, M08, M20, M21

**Story role:** Construct a lower estimate on the same channel metric.

**Conceptual connection:** Compact support controls drift phase while separating useful coherence from leakage.

**Sources:** Holevo §§2.4, 3.1, 6.4; [compact-packet proof](../science/cubic_distance.md).

### M27 — Cubic-law synthesis and resource scaling

**Central question:** What exactly matches in the upper and lower distance estimates?

**Understanding target:** Explain agreement of cubic logarithmic order, nonmatching exponent constants, fixed-rate scaling and the sufficient t^4 packet energy.

**Dependencies:** M25, M26

**Story role:** Integrate the second main theorem and its resource cost.

**Conceptual connection:** A scaling law for the full channel is stronger than a selected moment but weaker than an exact exponent or fixed-energy optimum.

**Sources:** Holevo §11.5 for constraints; [cubic law and rescaling](../science/cubic_distance.md).

### M28 — One fixed squeezed input

**Central question:** How does a single finite-energy input work for every finite time?

**Understanding target:** Explain finite truncation and a bounded reference filter, why PPT would survive it, and why nonzero success is not useful success.

**Dependencies:** M02, M03, M08, M21, M23

**Story role:** Separate qualitative survival from the quantitative packet construction.

**Conceptual connection:** Strictly positive Schmidt weights supply a faithful input without an unnormalizable Choi vector.

**Sources:** Holevo §§3.1.3, 3.3.2, 11.1, 12.3.5; [fixed-input proof](../science/fixed_input.md).

### M29 — The singular Gaussian limit

**Central question:** How can arbitrarily weak quadratic noise remove an exact cutoff?

**Understanding target:** Compare the separate Gaussian determinant with the positive-kappa threshold and the one-sided weak-noise distance bound.

**Dependencies:** M07, M10, M23, M24, M27

**Story role:** Test the theorem at its most consequential boundary.

**Conceptual connection:** Small coefficients of an unbounded generator need not be small in unconstrained diamond norm; tiny EB distance is compatible with non-EB.

**Sources:** Holevo §§12.2.3, 12.6.1–12.6.3; [Gaussian and weak-noise comparison](../science/interpretation.md).

### M30 — Whole-project synthesis and scientific credit

**Central question:** What has changed in the physical understanding, and what has not been shown?

**Understanding target:** Explain the sharp boundary, cubic operational decay and fixed-input survival together; distinguish inherited machinery, proved consequences, finite checks and open coefficients or capacities.

**Dependencies:** M14, M23, M27, M28, M29

**Story role:** Close the narrative with its contribution, scope and evidence.

**Conceptual connection:** Exact entanglement survival is not reliable memory; the distinct contribution is the specified nonlinear law, not the generic exact/approximate distinction.

**Sources:** Holevo §§10.1.2, 10.2, 10.3.1, 11.7; [interpretation](../science/interpretation.md), [related work](../references/RELATED_WORK.md), [verification](../verification/README.md).
