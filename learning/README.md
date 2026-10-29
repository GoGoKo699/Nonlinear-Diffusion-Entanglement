# Learning nonlinear diffusion and entanglement

**How can a noisy channel retain some entanglement forever, yet become almost indistinguishable from a measurement followed by preparation?** The answer requires two different questions: whether *any* reference entanglement survives, and how well *every* input can be approximated by a classical channel.

The single educational anchor is **Alexander S. Holevo, _Quantum Systems, Channels, Information: A Mathematical Introduction_, second revised and expanded edition (De Gruyter, 2019)**. Start with selected sections, not the whole book. The [source bridge](HOLEVO_BRIDGE.md) gives verified section locations, local conventions, and the additional arguments supplied by this project. Primary research references remain necessary for attribution; they are not extra educational anchors.

## Reading route

Begin with the [worked primer](PRIMER.md). It solves a two-qubit dephasing example to separate exact entanglement breaking from small operational error, then follows the project's stochastic shear and finite-energy witnesses. The example illustrates established ideas; it is not the project's novelty claim.

Next use the [30-milestone map](MILESTONES.md). **M01–M14** build background from states, references and channels to Gaussian noise and the complete operational question. **M15–M30** assemble the model, two directions of the sharp threshold proof, cubic distance bounds, fixed-input corollary and physical interpretation. Both phases progress from local ingredients to a global account. The 14/16 allocation gives the infinite-dimensional and probability prerequisites enough space without turning the map into the textbook's contents.

The map is learner-independent: every milestone states a central question, understanding target, dependencies, story role, conceptual connection and sources. It covers the project's conceptual structure rather than every technical lemma. Exact definitions and proofs remain in [science/](../science/README.md); the learning material does not replace them.

## Four distinctions to carry through the route

| Distinction | Why it matters |
|---|---|
| One physical channel versus its conditional Gaussian components | The environment's trajectory is not observed. A decomposition used in a proof is not free information for a decoder. |
| Entanglement breaking versus proximity to that set | A positive but arbitrarily small negative-partial-transpose witness can coexist with an all-input error bound tending to zero. |
| Finite energy for each witness versus one uniform resource bound | Time-dependent packets have finite energy at each time; that alone does not make their energy uniformly bounded. |
| A fixed entangled input versus usable storage or capacity | Qualitative survival of a squeezed-state tail establishes neither a useful entanglement amount nor reliable many-use communication. |

## Specialist shortcuts

For the precise assumptions and normalization, go directly to [model](../science/model.md). For the sharp boundary, read [conditional Gaussian representation](../science/conditional_gaussian.md) and [threshold proof](../science/exact_threshold.md). For the operational estimate, read [cubic distance](../science/cubic_distance.md). The [interpretation](../science/interpretation.md) and [source comparison](../references/RELATED_WORK.md) distinguish the scientific contribution from inherited machinery.

The [verification guide](../verification/README.md) documents finite checks, including the primer's matrix example. Those checks can detect factor and convention errors; the universal claims depend on analytical arguments.
