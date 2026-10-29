# Physical interpretation, Gaussian limit, and consequential boundaries

[Model](model.md) · [Exact threshold](exact_threshold.md) · [Cubic distance](cubic_distance.md)

## 1. Why a quadratic noise term changes the exact entanglement boundary

Position-generated dephasing $`-D[Q,[Q,\rho]]`$ randomly displaces momentum, so it is momentum diffusion. Under *deterministic* free motion, a momentum kick is carried into a position displacement by a known time-dependent shear. Together they fill both quadratures. If that noise spans enough phase-space area, the Gaussian channel becomes measure-and-prepare: all system–reference entanglement is lost.

Quadratic dephasing $`-\kappa[P^2/2,[P^2/2,\rho]]`$ instead makes the shear itself stochastic. Some rare paths keep its temporal variation unusually small, even if the typical displacement noise spans a large phase-space area. The individual pathwise Gaussian channels can be EB on nearly every path while the *unconditional non-Gaussian mixture* retains a very small NPT contribution. Because the kinetic operator is unbounded, the high-momentum witness can separate the rare coherent and incoherent terms exponentially strongly. This mechanism does not require measuring the environment or dynamically selecting a rare path; the NPT signal occurs in the unconditional output.

The exact theorem shows more: a positive independent position-diffusion rate $`\eta`$ puts a direct full-rank floor under every conditional displacement covariance. That floor enforces the exact cutoff $`(2\sqrt{D\eta})^{-1}`$ independently of the shear statistics. The NPT converse proves that rare paths prevent an **earlier** exact cutoff.

## 2. The singular Gaussian boundary is an explicit calculation

When $`\kappa=0`$, $`S_s=\omega s`$ is deterministic. The unconditional channel is now Gaussian, up to the final deterministic shear, with displacement covariance

```math
V_t=2D\begin{pmatrix}
\omega^2 t^3/3&-\omega t^2/2\\
-\omega t^2/2&t
\end{pmatrix}
+2\eta t\begin{pmatrix}1&0\\0&0\end{pmatrix}.
```

Its determinant is

```math
\boxed{\det V_t=4D\eta t^2+\frac{D^2\omega^2t^4}{3}.}
```

The standard one-mode Gaussian EB criterion states that the channel is EB iff $`\det V_t\ge1`$. Hence its first EB time is the first positive root of $`4D\eta t^2+D^2\omega^2t^4/3=1`$. In particular, with $`\eta=0`$ and $`\omega\ne0`$,

```math
\boxed{t_{\mathrm G}=\frac{3^{1/4}}{\sqrt{D|\omega|}}<\infty.}
```

For **every** positive $`\kappa`$, however small, and $`\eta=0`$, the exact EB time becomes infinite. With $`\eta>0`$ and $`\omega\ne0`$, the positive-$`\kappa`$ time instead becomes $`(2\sqrt{D\eta})^{-1}`$, delaying the Gaussian cutoff. The Gaussian result is a separate member of the parameter family, not the $`\kappa\to0`$ limit of a finite-$`\kappa`$ converse theorem. The deterministic-drift case $`\omega=0`$ has no such Gaussian finite-time cutoff when $`\eta=0`$.

## 3. Weak quadratic dephasing: the discontinuity is operationally tiny

Fix $`D>0`$, $`\omega\ne0`$, $`\eta=0`$, and a time $`t>t_{\mathrm G}`$. The noncentral Brownian transform in [the mixture derivation](conditional_gaussian.md) supplies a quantitative upper bound as $`\kappa\downarrow0`$.

For any $`r>0`$ define

```math
I_t(r)=\frac{\omega^2t}{4}
\left[1-\frac{2\tanh(r/2)}r\right]
-\frac{r^2}{16D^2t^3}.
```

Chernoff's inequality applied to the event $`\det V_S<1`$ yields

```math
e(t)\le\sqrt{\frac r{\sinh r}}
\exp[-I_t(r)/\kappa].
```

For $`r\downarrow0`$,

```math
I_t(r)=\frac{D^2\omega^2t^4-3}{48D^2t^3}\,r^2
-\frac{\omega^2t}{480}r^4+O(r^6).
```

When $`t>t_{\mathrm G}`$, the quadratic coefficient is positive; choose a sufficiently small *fixed* $`r`$ for which $`I_t(r)>0`$. Then

```math
e(t)\le C_{t,r}\exp[-I_t(r)/\kappa].
```

This is a **one-sided upper bound**, not a sharp weak-noise exponent. It shows how exact NPT persistence at every $`\kappa>0`$ can coexist with an operational error that becomes exponentially small as $`\kappa\to0`$ beyond the Gaussian cutoff. No similar general lower coefficient or full asymptotic is claimed.

## 4. What an operational approximation says about coding

Let $`d`$ be fixed, and allow arbitrary deterministic CPTP encoding $`\mathcal E`$ of a logical $`d`$-level system into the one noisy carrier and final recovery $`\mathcal R`$ afterward, with **no additional quantum memory crossing the interval**. If $`\Psi_t`$ is an EB comparator with half-diamond distance at most $`\varepsilon`$, then $`\mathcal R\circ\Psi_t\circ\mathcal E`$ is EB. Its entanglement fidelity on a maximally entangled logical input is at most $`1/d`$. Diamond contractivity and a two-outcome overlap measurement give

```math
F_e(\mathcal R\circ\Phi_t\circ\mathcal E)
\le\frac1d+\varepsilon.
```

Take $`\varepsilon\downarrow e(t)`$ to obtain $`F_e\le1/d+e(t)`$. This is a *single-use fixed-logical-dimension* bound, not a quantum-capacity theorem: capacity requires regularized coding over many independent uses and cannot be inferred from a naive dimension-independent continuity argument in infinite dimension. NPT by itself likewise does not prove positive unassisted quantum capacity.

## 5. Physical limits and interpretation hazards

- **One ideal noncompact carrier.** The system is a free canonical degree of freedom on $`L^2(\mathbb R)`$, not a confined harmonic oscillator or a finite-dimensional spin. The reference oscillator Hamiltonian used to measure preparation cost is different from the dynamical free Hamiltonian.
- **Unbounded quadratic jump.** Small $`\kappa`$ does not guarantee a small difference in unconstrained diamond norm, because $`H=P^2/2`$ is unbounded. The singular cutoff concerns *exact* entanglement-breaking as a model parameter varies.
- **Tiny survivors.** Even a fixed finitely squeezed two-mode state remains formally NPT for all finite times at $`\eta=0`$, but its survival is not a lower bound on high-fidelity storage, observability, distillable entanglement or nonzero quantum capacity.
- **No free environment record.** Conditional Gaussian channels are a proof tool, not an allowed operational measurement, postselection or side information.
- **No universal nonlinear-noise theorem.** The exact formula uses the specified $`Q`$, $`P`$, $`P^2/2`$ operators and positive rates. Other potentials, additional reservoirs, loss and nonlinear Hamiltonians require separate analysis.
- **Shared scientific ancestry.** The general exact-versus-approximate distinction is known for dephasing. The distinguishing quantitative contribution is the *noise-dependent sharp threshold and cubic channel-distance law* in the precisely attributed nonlinear model; see [related work](../references/RELATED_WORK.md).
