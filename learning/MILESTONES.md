# Thirty milestones for the complete scientific story

[Learning route](README.md) · [Single-source bridge](RIVAS_HUELGA_BRIDGE.md) · [Scientific statements](../science/model.md)

This is the project's learner-independent understanding map. **M01–M12 are background/preliminaries; M13–M30 are narrative/innovation.** The 12/18 allocation reflects a connection between open-system dynamics and reference-assisted continuous-variable entanglement: the first phase assembles that language, and the second follows the specific proof mechanism to its global implications. Each phase progresses from local objects to a synthesis. These targets cover the conceptual story, not every lemma or technical detail.

The one educational anchor is Rivas–Huelga, _Open Quantum Systems: An Introduction_ (2012). All source section numbers below refer to **arXiv:1104.5242v2**; the [bridge](RIVAS_HUELGA_BRIDGE.md#one-anchor-and-two-numbering-systems) gives the corresponding printed-book locations. A source section supplies the stated foundation, not an attribution of the project's new result to the textbook. Project-specific Gaussian, witness and stochastic estimates are supplied locally and retain primary-paper attribution in the scientific account.

<a id="backgroundpreliminaries-m01m12"></a>
## Background/preliminaries — M01–M12

### M01 — A carrier and an untouched reference

**Question:** What information is being tested when only one half of an entangled pair experiences noise?

**Target:** Explain a density operator, a composite state and the distinction between an inaccessible reference and a usable quantum bypass.

**Dependencies:** None. This introduces the physical objects before any noise model.

**Connection:** The question concerns preservation of joint quantum correlations, not just a particle's position distribution.

**Sources:** Rivas–Huelga 4.1–4.2; [primer, Section 1](README.md#1-state-reference-channel); [model](../science/model.md).

### M02 — Canonical motion and preparation energy

**Question:** Which operators describe the motion, and which quantity measures the cost of an input state?

**Target:** Distinguish $Q,P$, the canonical relation $[Q,P]=i$, free kinetic energy $P^2/2$, and the preparation cost $(Q^2+P^2)/2$.

**Dependencies:** M01. This identifies the carrier's observables and resource convention.

**Connection:** A finite-energy entanglement witness does not introduce a harmonic trap or an energy constraint into the channel norm.

**Sources:** Rivas–Huelga 3 for unitary-evolution context; [notation bridge](RIVAS_HUELGA_BRIDGE.md#notation-and-rate-translation); [model](../science/model.md).

### M03 — A channel must remain physical beside a reference

**Question:** Why is positivity on isolated inputs insufficient for a universal noise operation?

**Target:** Explain linearity, trace preservation and complete positivity, including the action of a channel tensored with the identity on a reference.

**Dependencies:** M01. This promotes an isolated state description to an operational map.

**Connection:** The same reference requirement enters both entanglement breaking and the diamond norm.

**Sources:** Rivas–Huelga 4.1–4.2; [reference-assisted bridge](RIVAS_HUELGA_BRIDGE.md#reference-assisted-entanglement-and-distance); [model](../science/model.md).

### M04 — State error versus complete-channel error

**Question:** What changes when an error bound must cover every input, including entangled ones?

**Target:** Interpret half trace distance, contraction under channels and the reference-assisted half-diamond distance, without confusing a sampled state error with a uniform bound.

**Dependencies:** M01, M03. This supplies the metric for the operational claim.

**Connection:** A bounded witness gives a lower bound for one input; a mixture argument can give an upper bound for all inputs.

**Sources:** Rivas–Huelga 2.1 and 4.3; [primer, Section 1](README.md#1-state-reference-channel); [model](../science/model.md).

### M05 — Markov composition is not a claim about equilibrium

**Question:** What does dividing the noisy interval into two pieces preserve?

**Target:** Explain $\Phi_{t+s}=\Phi_t\circ\Phi_s$, independent increments and the distinction between a semigroup and relaxation to one stationary state.

**Dependencies:** M03, M04. This connects maps at different times.

**Connection:** Local postprocessing cannot recreate reference entanglement after an EB channel, while a time-dependent EB comparator need not be a stationary-state channel.

**Sources:** Rivas–Huelga 2.3, 4.5 and 5.4; [domain warning](RIVAS_HUELGA_BRIDGE.md#the-finite-dimensional-boundary-of-the-source); [cubic bounds](../science/cubic_distance.md).

### M06 — Read a double commutator with the correct rate

**Question:** How does a Hermitian Lindblad jump become a dephasing term?

**Target:** Use $\gamma\mathcal D[A](\rho)=-(\gamma/2)[A,[A,\rho]]$ for self-adjoint $A$, and distinguish the rates $2D,2\kappa,2\eta$ from the coefficients in the project's generator.

**Dependencies:** M02, M03, M05. This translates the source's generator into the actual model.

**Connection:** The factor of two fixes the covariance and the numerical entanglement-breaking threshold.

**Sources:** Rivas–Huelga 5.2, Eq. (51); [rate translation](RIVAS_HUELGA_BRIDGE.md#notation-and-rate-translation); [qubit example](README.md#2-a-complete-two-level-example).

### M07 — Unobserved random unitaries

**Question:** How can averaging reversible trajectories give irreversible noise?

**Target:** Connect Brownian angle variance $2c\,dt$ to $-c[A,[A,\rho]]$, and distinguish mathematical conditioning from a noise record given to a decoder.

**Dependencies:** M05, M06. This supplies a construction rather than a formal generator alone.

**Connection:** Independent Hamiltonian noises define the channel that will later be decomposed into conditional Gaussian components.

**Sources:** Rivas–Huelga 3 and 5.2 for evolution context; [Brownian-noise bridge](RIVAS_HUELGA_BRIDGE.md#from-dephasing-to-brownian-motion); [model](../science/model.md).

### M08 — Gaussian displacement and covariance conventions

**Question:** What does a classical displacement covariance describe, and how is it different from a quantum state's covariance?

**Target:** Distinguish added noise from the input covariance, retain the vacuum convention $I/2$, and interpret Gaussian shear as a canonical unitary transformation.

**Dependencies:** M02, M07. This introduces the local phase-space description needed by the proof.

**Connection:** Conditional Gaussian channels can be analyzed using noise area even when their total mixture is non-Gaussian.

**Sources:** Rivas–Huelga 3 for unitary context; [notation bridge](RIVAS_HUELGA_BRIDGE.md#notation-and-rate-translation); [conditional Gaussian representation](../science/conditional_gaussian.md).

### M09 — Entanglement breaking is universal

**Question:** Why does a measure-and-prepare operation destroy every input's reference entanglement?

**Target:** Explain EB, its universal quantifier and its preservation under channel composition and convex mixtures; distinguish it from loss of entanglement for one chosen input.

**Dependencies:** M01, M03, M08. This identifies the target class of classical comparators.

**Connection:** The conditional Gaussian EB criterion gives a sufficient route for the whole mixture only when every component qualifies.

**Sources:** Rivas–Huelga 4.2 for reference-system foundations; [reference-assisted bridge](RIVAS_HUELGA_BRIDGE.md#reference-assisted-entanglement-and-distance); [model](../science/model.md).

### M10 — A negative witness is a one-sided certificate

**Question:** What does a negative partial-transpose expectation establish?

**Target:** Explain why separable states have positive partial transpose, why a negative witness disproves EB, and why a nonnegative test need not prove separability.

**Dependencies:** M01, M03, M09. This supplies the converse tool.

**Connection:** The Bell-state example separates finite-time NPT from convergence toward a separable state without assuming a continuous-variable Choi vector.

**Sources:** Rivas–Huelga 4.2 for positivity context; [complete qubit example](README.md#2-a-complete-two-level-example); [threshold witness](../science/exact_threshold.md).

### M11 — Normal states and finite approximations

**Question:** Which finite-dimensional arguments survive for an unbounded continuous-variable system?

**Target:** Distinguish normalizable trace-class states, formal eigenstates, bounded witnesses and finite-rank approximation; explain why a Lindblad-looking expression alone does not establish an unbounded generator.

**Dependencies:** M02, M04, M06, M10. This exposes the analytic boundary before using infinite-dimensional constructions.

**Connection:** Channel contractivity transfers a strictly negative bounded witness to a sufficiently close finite-rank input.

**Sources:** Rivas–Huelga introduction, 2.1–2.3 and the discussion after Eq. (51); [domain bridge](RIVAS_HUELGA_BRIDGE.md#the-finite-dimensional-boundary-of-the-source); [fixed-input proof](../science/fixed_input.md).

### M12 — Assemble the operational question

**Question:** What would it take to prove both exact entanglement death and approximate classical behavior?

**Target:** State the carrier, unobserved environment, allowed reference, absent bypass, energy conventions and two distinct claims: membership in EB and distance to EB.

**Dependencies:** M04, M05, M07, M08, M09, M10, M11. This is the synthesis of the background phase.

**Connection:** It separates the universal sufficient proof, an explicit counterexample below threshold and the two-sided channel-distance problem.

**Sources:** Rivas–Huelga 4.2–4.5 and 5.2 as foundations; [model and exact statements](../science/model.md); [primer synthesis](README.md#6-read-the-conclusions-with-their-quantifiers).

<a id="narrativeinnovation-m13m30"></a>
## Narrative/innovation — M13–M30

### M13 — Remove the stochastic free shear

**Question:** Why does the interaction-picture position operator become $Q+S_sP$?

**Target:** Explain the canonical shear identity and how conditioning on the quadratic-noise path leaves only linear quadrature noises.

**Dependencies:** M02, M07, M08, M12. This begins the mechanism with one transformed operator.

**Connection:** Scalar commutators make the ordering phase irrelevant to density-operator conjugation.

**Sources:** Rivas–Huelga 3; [interaction-picture bridge](RIVAS_HUELGA_BRIDGE.md#from-an-interaction-picture-to-a-conditional-gaussian-channel); [conditional representation, Section 1](../science/conditional_gaussian.md#1-factor-the-stochastic-shear).

### M14 — Separate the covariance floor from temporal shear variation

**Question:** Which part of the displacement determinant is independent of the random path?

**Target:** Read the determinant as $4D\eta t^2$ plus the nonnegative centered-shear integral, and explain the roles of complementary diffusion and temporal variation.

**Dependencies:** M08, M13. This converts the local noise model into a pathwise scalar condition.

**Connection:** The same determinant drives both the finite-time sufficient threshold and the exceptional-path probability.

**Sources:** [Conditional covariance and Brownian scaling, Section 2](../science/conditional_gaussian.md#2-a-gram-determinant-that-controls-channel-classicality); [bridge](RIVAS_HUELGA_BRIDGE.md#from-an-interaction-picture-to-a-conditional-gaussian-channel).

### M15 — A sufficient EB time that includes equality

**Question:** Why does $4D\eta t^2\ge1$ force the unobserved mixture to be EB?

**Target:** Apply the inherited one-mode Gaussian condition to each conditional channel, preserve EB under shear and averaging, and include the threshold endpoint.

**Dependencies:** M09, M14. This establishes one direction without pretending it proves sharpness.

**Connection:** Existence of some non-EB paths below the floor threshold is not a converse for their mixture.

**Sources:** [Exact threshold, Section 1](../science/exact_threshold.md#1-pathwise-measure-and-preparation-the-upper-proof); [primary attribution](../references/RELATED_WORK.md).

### M16 — Resolve the averaged channel in momentum variables

**Question:** What do the mean momentum and momentum difference reveal about the evolution?

**Target:** Interpret $s=(p+p')/2$, $y=p-p'$ and the heat equation with a quadratic potential; recognize which Mehler-kernel ingredients are inherited.

**Dependencies:** M06, M11, M13. This starts an independent mixture-level converse rather than reversing M15.

**Connection:** The variable $y$ controls coherence, while diffusion acts on mean momentum.

**Sources:** [Momentum-kernel calculation, Section 2](../science/exact_threshold.md#2-exact-momentum-space-kernel); [related work](../references/RELATED_WORK.md).

### M17 — Prepare a legitimate finite-energy witness

**Question:** Why are the system–qubit packet states normalized even when the two system packets overlap?

**Target:** Use orthogonal reference labels, calculate the finite preparation-energy terms and distinguish finite energy for each witness from one uniform energy budget.

**Dependencies:** M02, M10, M11, M16. This supplies physical input and test vectors.

**Connection:** No momentum eigenstate or unnormalizable oscillator maximally entangled vector is needed.

**Sources:** [Gaussian-packet witness, Section 3](../science/exact_threshold.md#3-an-actual-finite-energy-systemreference-witness); [primer](README.md#5-why-the-two-main-proofs-need-different-witnesses).

### M18 — Coherence must exceed wrong-packet leakage

**Question:** Which two matrix elements determine the negative partial-transpose expectation?

**Target:** Explain $c_A$, $d_A$ and the witness value $(d_A-\operatorname{Re}c_A)/2$, including the role of parity covariance.

**Dependencies:** M10, M16, M17. This turns the existence question into a testable inequality.

**Connection:** The witness is applied to the averaged channel, so it addresses the operational task that a favorable trajectory alone cannot settle.

**Sources:** [Normalized witness and its expectation, Section 3](../science/exact_threshold.md#3-an-actual-finite-energy-systemreference-witness); [verification](../verification/README.md).

### M19 — Compare the competing tails

**Question:** Why can surviving coherence dominate leakage despite both becoming extremely small?

**Target:** Interpret the positive integral formulas, the diagonal upper bound and coherence lower bound; with $\delta=A^{-1}$, identify their different quadratic and linear exponents.

**Dependencies:** M16, M18. This isolates the mathematical reason for sharpness.

**Connection:** Finite drift contributes damping but does not change the controlling coefficient $1/(Dt)-4\eta t$.

**Sources:** [Positive integrals, Section 4](../science/exact_threshold.md#4-positive-one-dimensional-integral-reduction); [matching argument, Section 5](../science/exact_threshold.md#5-prove-the-exact-threshold-including-its-endpoint).

### M20 — Close the exact EB and PPT boundary

**Question:** How do the two proof directions establish the entire time interval rather than selected examples?

**Target:** Combine the strict pre-threshold NPT construction with the inclusive pathwise EB bound, retaining $D,\kappa>0$, both cases of $\eta$, and the endpoint.

**Dependencies:** M15, M19. This is the first global synthesis of the new result.

**Connection:** The same boundary separates PPT-inducing from non-PPT-inducing channels in this model, without a capacity inference.

**Sources:** [Exact theorem](../science/exact_threshold.md#theorem-and-significance-of-the-quantifiers); [model contract](../science/model.md).

### M21 — The zero-quadratic-noise model is different

**Question:** Why can setting $\kappa$ exactly to zero change the entanglement-breaking time discontinuously?

**Target:** Derive the deterministic-shear Gaussian determinant, distinguish the separate $\kappa=0$ calculation from the positive-$\kappa$ converse, and interpret the weak-noise upper bound without assuming diamond-small perturbations.

**Dependencies:** M14, M20. This connects the threshold to its closest physical baseline.

**Connection:** Unbounded generators and exact set membership make a singular boundary possible without a demonstrated useful-memory gain.

**Sources:** [Gaussian comparison and weak-noise bound, Sections 2–3](../science/interpretation.md); [source-domain warning](RIVAS_HUELGA_BRIDGE.md#the-finite-dimensional-boundary-of-the-source).

### M22 — Replace exceptional paths by an EB channel

**Question:** How can a probability bound control a complete quantum channel uniformly?

**Target:** Construct the good-path/bad-path EB comparator and explain why its half-diamond error is at most the replaced probability for every input and reference.

**Dependencies:** M04, M09, M14. This starts the quantitative classicalization proof.

**Connection:** Conditioning is an analytical device; the construction grants the receiver no trajectory information.

**Sources:** [Uniform upper estimate, Section 1](../science/cubic_distance.md#1-uniform-upper-bound-by-removing-exceptional-brownian-paths); [bridge](RIVAS_HUELGA_BRIDGE.md#reference-assisted-entanglement-and-distance).

### M23 — Centered Brownian motion supplies the rare-event scale

**Question:** Which random quadratic functional controls the exceptional-path event?

**Target:** Identify centered Brownian motion, its cosine covariance modes, mean-square integral and Laplace transform; distinguish it as a process from a Brownian bridge even though their integrated squares share a law.

**Dependencies:** M07, M14. This supplies the probability estimate's input.

**Connection:** Brownian scaling introduces $D^2\kappa t^3$, while deterministic shear enters the noncentral shift.

**Sources:** [Brownian quadratic functional, Section 4](../science/conditional_gaussian.md#4-a-brownian-small-ball-event-and-its-exact-transform); [finite checks](../verification/README.md).

### M24 — Obtain the cubic-exponential upper bound

**Question:** Why does the selected Chernoff parameter produce a cubic exponent?

**Target:** Combine the Laplace transform with the bad-event cutoff, retain the prefactor and the trivial bound one, and distinguish a proven bound from an optimal asymptotic constant.

**Dependencies:** M22, M23. This completes the uniform direction of the distance theorem.

**Connection:** Positive finite-time entanglement can coexist with an extremely small all-input distance to EB.

**Sources:** [Cubic upper proof, Section 1](../science/cubic_distance.md#1-uniform-upper-bound-by-removing-exceptional-brownian-paths); [theorem contract](../science/model.md).

### M25 — Normalize a quantitative converse

**Question:** Why replace overlapping Gaussian packets with disjoint compact packets for the distance lower bound?

**Target:** Explain exact orthogonality, the witness norm $1/2$, the common nonnegative packet weight and its scaling proportional to width rather than width squared.

**Dependencies:** M04, M10, M16, M18. This creates a quantitatively controlled certificate against every EB comparator.

**Connection:** Normalization and shared integration weight are essential when comparing two exponentially small quantities.

**Sources:** [Compact packets, Section 2](../science/cubic_distance.md#2-exactly-orthogonal-finite-energy-momentum-packets); [common weight, Section 3](../science/cubic_distance.md#3-shared-weight-and-mehler-bounds).

### M26 — Choose centers and widths to keep a positive gap

**Question:** How do the time-dependent packet choices turn the kernel bounds into a positive channel-distance lower bound?

**Target:** Interpret the choices of $a,w$, control the drift phase and compare the diagonal and coherence estimates to obtain a strictly positive $c_*$.

**Dependencies:** M25. This completes the second direction in the same norm used by M24.

**Connection:** One and four are different bounding cubic coefficients; matching order is not matching the exact exponent.

**Sources:** [Parameter choice and constant, Section 4](../science/cubic_distance.md#4-parameter-choice-and-a-positive-universal-constant); [statement](../science/cubic_distance.md#theorem).

### M27 — Restore physical rates and charge witness energy

**Question:** What survives a canonical rescaling, and what resources grow in the quantitative witness?

**Target:** Explain $\tau=D^{2/3}\kappa^{1/3}t$, the rescaled drift, invariance of EB and diamond distance, and the sufficient $O(t^4)$ energy cost at fixed canonical drift.

**Dependencies:** M02, M24, M26. This synthesizes the full distance law with its resource accounting.

**Connection:** The energy cost of this construction is not a lower bound on the energy needed merely for nonzero entanglement.

**Sources:** [Energy and general strengths, Section 5](../science/cubic_distance.md#5-physical-resource-and-general-rate-scaling); [learning verification](../verification/check_learning.py).

### M28 — Exchange time-dependent witnesses for one fixed input

**Question:** How can a single finitely squeezed state remain NPT at all finite times?

**Target:** Follow finite-rank approximation and bounded reference filtering, keeping the input fixed while the test and filtering probability may depend on time.

**Dependencies:** M11, M17, M20. This sharpens the survival quantifier without changing the channel model.

**Connection:** A vanishingly unlikely filter branch proves qualitative NPT, not useful entanglement strength or recovery performance.

**Sources:** [Fixed-input proof](../science/fixed_input.md#bounded-reference-filter-proof); [bridge to the three results](RIVAS_HUELGA_BRIDGE.md#the-bridge-to-the-three-results).

### M29 — Convert proximity into a logical-memory limitation

**Question:** What does a small EB distance imply for encoding and recovering a fixed logical register?

**Target:** Explain $F_e\le1/d+e(t)$ under deterministic CPTP encoding/recovery without a quantum bypass, and distinguish this one-use statement from many-use quantum capacity.

**Dependencies:** M04, M09, M27, M28. This gives the operational meaning of the exact/approximate separation.

**Connection:** Surviving NPT and poor worst-task storage are compatible, rather than contradictory conclusions.

**Sources:** [Fixed logical register, Section 4](../science/interpretation.md#4-what-an-operational-approximation-says-about-coding); [primer synthesis](README.md#6-read-the-conclusions-with-their-quantifiers).

### M30 — The complete contribution and its evidence

**Question:** What has changed relative to known diffusion and Gaussian-channel theory, and what has not been established?

**Target:** Connect the inherited model and propagator to the sharp nonlinear EB/PPT boundary, singular Gaussian comparison, cubic all-input distance bounds and fixed-input corollary; distinguish proofs, finite checks and unproved extensions.

**Dependencies:** M20, M21, M27, M28, M29. This is the global synthesis of the narrative phase.

**Connection:** The contribution is the specific classification and quantified operational law, not a new general definition of classicality, a new diffusion model or a positive-capacity theorem.

**Sources:** [Primary comparison](../references/RELATED_WORK.md); [physical interpretation](../science/interpretation.md); [verification scope](../verification/README.md); [scientific reading map](../science/README.md).
