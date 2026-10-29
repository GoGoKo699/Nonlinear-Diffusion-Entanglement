# Nonlinear Diffusion and Entanglement

**Quadratic stochastic motion can prevent exact entanglement death while an entire continuous-variable quantum channel approaches measure-and-prepare dynamics exponentially fast.** Direct position diffusion restores a sharp finite-time entanglement-breaking boundary.

Consider one free canonical degree of freedom with $[Q,P]=i$, $H=P^2/2$, and the normal random-unitary semigroup whose formal generator is

$$
\mathcal L(\rho)=-i\omega[H,\rho]-D[Q,[Q,\rho]]
-\kappa[H,[H,\rho]]-\eta[P,[P,\rho]],
\qquad D,\kappa>0,\quad\eta\ge0.
$$

The $D$ term causes position dephasing and momentum diffusion; the $\eta$ term causes momentum dephasing and position diffusion. The quadratic noise makes the free-motion shear stochastic. The evolution remains linear in the density operator.

## Results

**Exact boundary.** Its first entanglement-breaking time is

$$
\boxed{t_{\rm EB}=
\begin{cases}
(2\sqrt{D\eta})^{-1},&\eta>0,\\
\infty,&\eta=0.
\end{cases}}
$$

At and above the finite threshold the channel is entanglement breaking. At every strictly earlier positive time there is a **normalizable finite-energy system–qubit state with an NPT output**, so the interval is sharp even against arbitrary reference systems. This holds for all positive kinetic dephasing rates and finite deterministic drift. [Precise theorem and converse](science/exact_threshold.md).

**Operational classicalization without exact entanglement death.** For $\eta=0$, define the energy-unconstrained half-diamond distance $e(t)$ to the set of entanglement-breaking channels. At fixed positive $D,\kappa$ and finite $\omega$,

$$
-\log e(t)=\Theta(D^2\kappa t^3).
$$

The upper bound controls every input and reference; the matching logarithmic order is certified by finite-energy compact momentum packets. The optimal leading constant in the cubic exponent is **not** established. [Matching logarithmic bounds](science/cubic_distance.md).

**Singular Gaussian comparison.** At $\kappa=0$, the channel is Gaussian and the EB threshold instead solves

$$4D\eta t^2+\frac{D^2\omega^2t^4}{3}=1.$$

With $\eta=0$ and $\omega\neq0$, its finite cutoff is $3^{1/4}/\sqrt{D|\omega|}$, while every $\kappa>0$ removes the finite cutoff. The parameter dependence is singular because the quadratic noise generator is unbounded; this does **not** imply useful memory improvement or diamond-small perturbation. [Physical interpretation](science/interpretation.md).

For $\eta=0$, a single fixed **finite-energy two-mode squeezed vacuum** is also NPT after one mode experiences the channel at every finite time. This qualitative observation gives no uniform amount of entanglement and no capacity theorem. [Proof](science/fixed_input.md).

## Read the science

| Question | Authoritative file |
|---|---|
| Which physical channel, domains and resources? | [Model and exact claims](science/model.md) |
| Why do stochastic quadratic shears produce conditional Gaussian channels? | [Conditional representation](science/conditional_gaussian.md) |
| Why is the exact EB time sharp? | [Pathwise upper bound and finite-energy NPT converse](science/exact_threshold.md) |
| Why cubic decay in an all-input channel norm? | [Brownian upper and compact-packet lower](science/cubic_distance.md) |
| Can a fixed finite-energy input retain entanglement? | [Faithful-state corollary](science/fixed_input.md) |
| What changes at zero quadratic dephasing? | [Gaussian limit and operational limits](science/interpretation.md) |
| Which ingredients were already known? | [Primary sources and novelty comparison](references/RELATED_WORK.md) |
| How to check formulas and sample witnesses? | [Verification](verification/README.md) |

The [science index](science/README.md) connects the argument. The [LLM reading map](llms.txt) points to authoritative topic pages.

## Learn the project

The single educational anchor is **Ángel Rivas and Susana F. Huelga, _Open Quantum Systems: An Introduction_ (2012)**. Start with the [learning primer and complete qubit example](learning/README.md), then follow the [30-milestone understanding map](learning/MILESTONES.md): **12 background/preliminaries milestones and 18 narrative/innovation milestones**.

The [Rivas–Huelga source bridge](learning/RIVAS_HUELGA_BRIDGE.md) maps verified book chapters to the freely available author version, translates rates and quadrature conventions, and supplies the missing continuous-variable, stochastic and reference-assisted arguments. It explicitly separates the source's finite-dimensional generator foundations from this project's unbounded-operator channel construction. The shared learning route does not replace the exact proofs or require reading the whole book.

## Reproduce

Run the pinned Python consistency checks from the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_checks.py
```

The runner checks analytical packet integrals, rigorous inequalities, the Brownian Laplace product, Gaussian determinants, learning examples, milestone dependencies and local links. It writes a fresh success or failure manifest under `verification/local_results/`. The [verification guide](verification/README.md) distinguishes these checks from the written proofs and the separate inspection of actual hosted equations.

## Scope and attribution

The **model and exact propagator are inherited** from Speed, Lyu and Schubert (2023). The Gaussian EB criterion is inherited from Holevo (2008) and the Gaussian Brownian comparison from Riedel (2016). This account develops the nonlinear mixture's sharp EB/PPT boundary, finite-energy witnesses and uniform cubic-distance law. See [related work](references/RELATED_WORK.md). No exhaustive priority certification is claimed.

The carrier is one noncompact degree of freedom on $L^2(\mathbb R)$, not a finite spin or a bounded-energy physical device. The environment's stochastic path is never observed, and no noiseless quantum bypass or intermediate correction is supplied. NPT does **not** imply positive quantum capacity or an operationally useful quantum memory.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
