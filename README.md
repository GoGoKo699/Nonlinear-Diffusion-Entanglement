# Nonlinear Diffusion and Entanglement

**Quadratic stochastic motion can prevent exact entanglement death while driving an entire continuous-variable quantum channel exponentially close to a measure-and-prepare channel.** Independent position diffusion restores a sharp finite-time entanglement-breaking threshold.

On one noncompact canonical degree of freedom, with $`[Q,P]=i`$ and $`H=P^2/2`$, study the normal random-unitary semigroup with formal generator

```math
\mathcal L(\rho)=-i\omega[H,\rho]
-D[Q,[Q,\rho]]-\kappa[H,[H,\rho]]
-\eta[P,[P,\rho]],\quad D,\kappa>0,\ \eta\ge0.
```

The *exact entanglement-breaking time* is

```math
\boxed{t_{\mathrm{EB}}=\begin{cases}
(2\sqrt{D\eta})^{-1},&\eta>0,\\
\infty,&\eta=0.
\end{cases}}
```

For every positive time strictly below this boundary, a **normalizable finite-energy system–qubit input** yields a negative-partial-transpose (NPT) output; at and beyond the finite boundary, the channel is entanglement breaking. The threshold includes its endpoint and does not depend on positive $`\kappa`$ or finite drift $`\omega`$. [Exact theorem and proof](science/exact_threshold.md).

When $`\eta=0`$, let $`e(t)`$ be the infimum of the half-diamond distance to all entanglement-breaking channels, with **no input-energy restriction**. For fixed $`D,\kappa>0`$ and $`\omega\in\mathbb R`$,

```math
-\log e(t)=\Theta(D^2\kappa t^3)\quad(t\to\infty).
```

The upper bound applies uniformly to every input and reference; the lower bound is certified by compact, exactly orthogonal finite-energy momentum packets. The exponent's leading constant is **not** optimized. [Cubic-distance theorem](science/cubic_distance.md).

## The singular Gaussian boundary

At $`\kappa=0`$, the channel instead has Gaussian additive noise (up to a Gaussian unitary), with entanglement-breaking threshold determined by

```math
4D\eta t^2+\frac{D^2\omega^2t^4}{3}=1.
```

With $`\eta=0`$ and $`\omega\ne0`$, it becomes entanglement breaking after the **finite** time $`3^{1/4}/\sqrt{D|\omega|}`$. Every $`\kappa>0`$, however small, removes this exact finite cutoff. This is a singular statement about the exact entanglement-breaking property in an unbounded-noise model, **not** a claim that a diamond-small perturbation dramatically enhances usable quantum memory. [Physical interpretation](science/interpretation.md).

A single fixed, finitely squeezed two-mode squeezed vacuum also has NPT output at all finite times for $`\eta=0`$; this follows from normal-state filtering and yields **no lower bound** on useful surviving entanglement or quantum capacity. [Fixed-input corollary](science/fixed_input.md).

## Scientific reading route

| Question | Read |
|---|---|
| Precise Hilbert-space model, allowed resources, conventions and propositions | [Model and definitions](science/model.md) |
| Why does conditioning on quadratic noise produce a mixture of Gaussian channels? | [Conditional Gaussian representation](science/conditional_gaussian.md) |
| Where is the exact entanglement-breaking cutoff proved? | [Sharp threshold and finite-energy witness](science/exact_threshold.md) |
| Why is the channel uniformly close to classical but never exactly classical? | [Matching cubic logarithmic bounds](science/cubic_distance.md) |
| Does one fixed finite-energy entangled input survive? | [Faithful-state corollary](science/fixed_input.md) |
| Which conclusions matter physically and which do not follow? | [Interpretation and limits](science/interpretation.md) |
| What is inherited and what distinguishes this result? | [Primary-literature comparison](references/RELATED_WORK.md) |
| How are the formulas and finite witnesses checked? | [Verification and reproducibility](verification/README.md) |

The [science index](science/README.md) gives a connected proof route. An [LLM-oriented retrieval guide](llms.txt) points to each claim's authoritative home. The educational bridge and project-defined 30-milestone map are added after a single source is selected; none is assumed here.

## Reproduce

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_checks.py
```

The tests check the Mehler kernel, exact packet integrals, rigorous bounds, Gaussian-channel cutoff and Brownian quadratic-functional identities. Finite tests inspect algebra and numerical conventions; the universal statements rely on the written proofs. No Monte Carlo data are needed for the principal result.

## Attribution and scope

The position/kinetic-energy-dephasing model, Grushin geometry and exact propagator come from **Speed, Lyu and Schubert (2023)**. Gaussian entanglement-breaking criteria and finite-time Gaussian Brownian measurement descriptions are inherited from **Holevo (2008)** and **Riedel (2016)**. The present account derives the precise **non-Gaussian entanglement-breaking boundary**, its singular dependence on quadratic noise, normalized NPT witnesses and the operational cubic-distance law. See the [related-work comparison](references/RELATED_WORK.md); no exhaustive priority claim is made.

The dynamics act on $`L^2(\mathbb R)`$, not a bounded-energy device or an irreducible finite spin. The environment is unobserved; the reference is arbitrary; no intermediate correction or noiseless quantum bypass is allowed. The lack of finite-time entanglement breaking does **not** imply positive quantum capacity, finite-error memory, or experimentally useful survival. Statements that vary $`\kappa`$ cannot be interpreted as unconstrained-diamond-small perturbations because $`H`$ is unbounded.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
