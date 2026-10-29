# Primary sources and contribution boundaries

Primary-source comparison checked on October 29, 2026. Its purpose is exact *scientific attribution*, not an exhaustive priority certificate. Our central result is an **operational entanglement theorem for an already known nonlinear diffusion model**. Physical and mathematical ingredients that precede it are identified below.

## What is inherited and what is derived here

| Statement or technique | Status and material source | Difference in this project |
|---|---|---|
| $`Q`$ and $`P^2/2`$ Hermitian Lindblad diffusion, Grushin form and exact propagator | **Inherited:** Speed–Lyu–Schubert (2023), equations 18–22 and 58–62 | The model and Mehler solution are *not* introduced or rediscovered here. |
| Gaussian channels, symplectic covariance and the additive-noise EB criterion | **Inherited:** Holevo (2008); Gaussian QBM interpretation in Riedel (2016) | Applied to each conditioned path; a *new lower witness* establishes the exact mixture threshold. |
| Finite-time entanglement breaking for Gaussian Brownian motion | **Inherited:** Riedel (2016); related positivity theorems in Diósi–Kiefer (2002) | The singular effect is caused by a **quadratic stochastic** Hamiltonian, making the total channel non-Gaussian. |
| Brownian quadratic functional and Laplace-product identities | **Established probability machinery** | Used here to give a *uniform channel* distance bound, not merely a state-specific decoherence factor. |
| Partial-transpose entanglement witnesses and the PPT criterion | **Standard quantum-information method** | Matched with explicit, normalizable momentum packets and exact Mehler estimates. |
| Non-EB at every finite time while asymptotically close to EB | **Qualitative phenomenon already known** (e.g. finite-dimensional dephasing) | The distinctive result is the **exact nonlinear-noise cutoff, singular Gaussian boundary, and cubic-log quantitative law**. |
| Exact $`t_{\rm EB}=(2\sqrt{D\eta})^{-1}`$ for positive kinetic noise, with finite-energy NPT below it | **Derived here**, for the stated $`D,\kappa,\eta,\omega`$ model | Not a general theorem about all unbounded generators or channels. |
| $`-\log e(t)=\Theta(D^2\kappa t^3)`$ with an energy-unconstrained diamond upper bound | **Derived here** for $`\eta=0`$ | Matching *order* of exponents, not exact optimal leading coefficient. |
| Fixed-TMSV qualitative NPT survival | **Derived as a corollary using standard faithful-state filtering** | Not a new code or practical longevity guarantee. |

## Closest model predecessor

**Speed, Lyu, and Schubert, *Beyond Gaussian Quantum Channels: A model case*, arXiv:2305.08467v1 (2023).** [Record and versions](https://arxiv.org/abs/2305.08467), [original PDF](https://arxiv.org/pdf/2305.08467).

This is the direct scientific predecessor. Equations 18–22 use the free Hamiltonian $`H=P^2/2`$ with Lindblad operators proportional to position and kinetic energy. The paper derives a Grushin-type diffusion, an exact propagator and characteristic-function solutions, evaluates semiclassical/perturbative approximations and entropy growth. The kernel and its mathematical solvability are inherited. The version inspected in exploration did **not** state the all-reference EB/PPT cutoff, finite-energy NPT converse, or uniform cubic diamond law. That scoped observation does not certify global novelty or exclude a later unknown paper.

## Gaussian entanglement breaking, finite-time measurement, and Wigner positivity

**Holevo, *Entanglement-breaking channels in infinite dimensions*, Problems of Information Transmission 44 (2008), 171–184.** [arXiv:0802.0235](https://arxiv.org/abs/0802.0235), [journal](https://doi.org/10.1134/S0032946008030010). The general Gaussian EB criterion is standard. In the normalization with vacuum covariance $`I/2`$, a one-mode additive-noise channel $`\mathcal N_V`$ is EB precisely when $`\sqrt{\det V}\ge1`$. No novelty is claimed for this Gaussian threshold.

**Riedel, *Quantum Brownian motion as an iterated entanglement-breaking measurement by the environment*, Physical Review A 93, 012107 (2016).** [arXiv:1507.04083](https://arxiv.org/abs/1507.04083), [journal](https://doi.org/10.1103/PhysRevA.93.012107). Its deterministic symplectic/Gaussian treatment supplies an important comparison: quadratic deterministic Hamiltonians with linear jumps lead to finite-time Gaussian measure-and-prepare descriptions. The unconditional channel here is **not Gaussian** once stochastic quadratic dephasing is added. Its pathwise Gaussian decomposition is a technique, not an assertion that Riedel's result alone proves the mixed channel's exact EB boundary.

**Diósi and Kiefer, *Exact positivity of the Wigner and P-functions of a Markovian open system*, Journal of Physics A 35, 2675 (2002).** [arXiv:quant-ph/0111139](https://arxiv.org/abs/quant-ph/0111139), [DOI](https://doi.org/10.1088/0305-4470/35/11/312). Free-particle motion and linear position decoherence already generate nontrivial finite-time positivity; the additional quadratic Hermitian jump is outside their model. Wigner- or P-positivity must not be equated without argument to the all-reference EB property.

## General Markovian and Gaussian-channel context

**Hanson, Rouzé and Stilck França, *Eventually entanglement breaking Markovian dynamics: Structure and characteristic times*, Annales Henri Poincaré 21 (2020), 1517–1571.** [Published paper](https://doi.org/10.1007/s00023-020-00906-4). Its classification is on finite-dimensional Hilbert spaces. Elementary finite-dimensional dephasing illustrates that asymptotic approach to EB without finite-time EB is an old phenomenon. The finite-dimensional result is not an all-input theorem for an unbounded, noncompact oscillator.

**Bardet, Junge, LaRacuente, Rouzé and Stilck França, *Group transference techniques for the estimation of the decoherence times and capacities of quantum Markov semigroups*, IEEE Transactions on Information Theory 67 (2021).** [arXiv:1904.11043](https://arxiv.org/abs/1904.11043). Its transfer of classical probability bounds to quantum semigroups motivates part of the methodology. Its compact-group and finite-representation assumptions do not supply the present oscillator result; no novelty is claimed for transference in general.

**Schubert and Plastow, *Decoherence Time Scales and the Hörmander Condition*, arXiv:2307.08799 (2023).** [arXiv record](https://arxiv.org/abs/2307.08799). Commutator-generated spreading of noise and hypoelliptic timescales are established context. This is not a claim to have discovered hypoellipticity or its cubic Brownian scaling.

**Shchukin and van Loock, *Separability rigidity of Gaussian states under positive domination*, arXiv:2609.36336v2 (2026).** [arXiv record](https://arxiv.org/abs/2609.36336). Its Gaussian-channel result involves positive EB subchannels while assuming a *Gaussian total channel*. Our full channel is non-Gaussian, and its finite-time NPT witness is compatible with a positive-weight EB component. The Gaussian-total hypothesis is not silently dropped.

**Szczygielski and Chruściński, *Eventually entanglement breaking divisible quantum dynamics*, arXiv:2407.16583v2 (2024).** [arXiv record](https://arxiv.org/abs/2407.16583). The inspected operator setting is finite matrix algebras, not this unbounded generator. Similarly **Bhat, Dey and Saha**, [arXiv:2609.24168](https://arxiv.org/abs/2609.24168), concerns finite-dimensional unital channels.

## Relationship to the author's existing research

The [Spin-Diffusion-Classicalization](https://github.com/GoGoKo699/Spin-Diffusion-Classicalization/tree/48547a557c0a1ce0ef54f3d251824ff80d0f46ca) project already proves that large-spin isotropic diffusion can approach the EB set uniformly while a tiny negative partial-transpose eigenvalue survives along an appropriate sequence. Therefore the **exact-versus-operational distinction alone is shared, not a separately discovered general principle**. The spin result concerns a compact finite-dimensional irreducible carrier with a large-spin limit; its witness and $`O(1/n)`$ result do not imply the present noncompact nonlinear-noise threshold, its discontinuity in $`\kappa`$, or the all-time cubic-log law.

The [Bosonic-Phase-Memory](https://github.com/GoGoKo699/Bosonic-Phase-Memory/tree/aa346e09df1d52381a77ae08ac3677fda8c64b8b) project gives an exact one-use code-optimization theorem for commuting, compact angular phase noise generated by nondegenerate oscillator number. This channel has simultaneous $`Q`$ and $`P^2/2`$ noise, noncommuting generators and a noncompact phase-space task. Its angular-cell converse cannot simply be transferred. Other related projects on autonomous entanglement stabilization and environmental records concern different channel/input obligations; their results are not borrowed as new implications here.

These comparisons concern the linked scientific revisions. A common distinction between exact and approximate classicality does not supply a theorem transferring between their different dynamical models.

## Scientific remainder and limits

After subtracting the known nonlinear model and propagator, standard Gaussian EB theory, standard Brownian quadratic functionals and familiar PPT witnesses, the remaining contribution is a **sharp phase transition in the finite-time EB property under quadratic stochastic noise**, an **exact direct-noise regularization threshold**, and a **reference-uniform cubic-exponential operational estimate with a finite-energy converse**. Its scope is one unbounded free continuous-variable carrier. No practical memory performance, positive capacity or universal classification of nonlinear reservoirs is implied.
