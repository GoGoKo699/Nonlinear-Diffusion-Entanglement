# Physical mechanism, singular Gaussian limit, and scope

[Model](model.md) · [Exact threshold](exact_threshold.md) · [Cubic proximity](cubic_distance.md)

## Why non-Gaussian shear noise changes an exact cutoff

Position decoherence generates random momentum kicks. Under deterministic free-particle motion these kicks shear into position displacements; the resulting Gaussian noise fills both quadratures and can become measure-and-prepare in finite time.

Quadratic Hermitian dephasing instead makes the free shear **itself stochastic**. Nearly all late-time shear paths produce Gaussian noise large enough to be EB, but rare trajectories keep their centered temporal variance small. The physical output is their *unconditioned non-Gaussian mixture*. At high momentum, a normalized state can distinguish rare remaining coherence from much smaller opposite-packet leakage. This keeps exact NPT alive even while the entire channel is uniformly very close to EB.

Direct $P$ dephasing with coefficient $\eta>0$ adds a nonzero path-independent covariance floor. Every conditional channel becomes EB when $4D\eta t^2\ge1$; the finite-energy NPT converse shows there cannot be an earlier unconditional cutoff.

## The exactly Gaussian $\kappa=0$ case

With no stochastic quadratic shear, $S_s=\omega s$ is deterministic and the total channel is Gaussian up to a known unitary. Its additive displacement covariance is

$$
V_t=2D\begin{pmatrix}
\omega^2t^3/3&-\omega t^2/2\\
-\omega t^2/2&t
\end{pmatrix}
+2\eta t\begin{pmatrix}1&0\\0&0\end{pmatrix}.
$$

Hence

$$
\boxed{\det V_t=4D\eta t^2+\frac{D^2\omega^2t^4}{3}.}
$$

The Gaussian EB criterion gives the first cutoff as the first time this expression reaches one. If $\eta=0$, $\omega\neq0$,

$$
\boxed{t_G=3^{1/4}/\sqrt{D|\omega|}<\infty.}
$$

By contrast every $\kappa>0$ with $\eta=0$ gives $t_{\rm EB}=\infty$. At positive $\eta$ and nonzero $\omega$, adding any $\kappa>0$ delays the exact Gaussian EB cutoff to $1/(2\sqrt{D\eta})$. The $\kappa=0$ theorem is a **separate model**: inserting $\kappa=0$ into a proof requiring a positive harmonic Mehler potential is invalid.

## Weak quadratic noise: operational distance can be tiny

Fix $D>0,\eta=0,\omega\neq0$ and a time $t>t_G$. The noncentral Laplace transform from [the Brownian mixture](conditional_gaussian.md) gives, for any $r>0$,

$$
e(t)\le\sqrt{\frac r{\sinh r}}\,
\exp[-I_t(r)/\kappa],
$$

where

$$
I_t(r)=\frac{\omega^2t}{4}
\left[1-\frac{2\tanh(r/2)}r\right]
-\frac{r^2}{16D^2t^3}.
$$

For small $r$,

$$
I_t(r)=\frac{D^2\omega^2t^4-3}{48D^2t^3}r^2
-\frac{\omega^2t}{480}r^4+O(r^6).
$$

Since $t>t_G$, the quadratic coefficient is positive. Some sufficiently small fixed $r$ gives $I_t(r)>0$, so for every $\kappa>0$ the channel is not EB, yet its EB distance is at most $C_{t,r}e^{-I_t(r)/\kappa}$. This is only a **one-sided upper bound**; the optimal coefficient and a full weak-noise asymptotic remain unknown.

The statement is not that an arbitrarily weak quadratic jump is a small perturbation in unconstrained diamond norm. Because $P^2/2$ is unbounded, changing its coefficient can be singular for unrestricted high-energy inputs.

## Consequence for a fixed logical register

For a deterministic CPTP encoding $\mathcal E$ of a logical $d$-level state into this *single* noisy carrier and final recovery $\mathcal R$, with no extra quantum bypass, take an EB comparator $\Psi$ within half-diamond distance $\varepsilon$. The effective channel $\mathcal R\Psi\mathcal E$ is EB, so its maximally entangled overlap is at most $1/d$. Contractivity and an overlap test imply

$$
F_e(\mathcal R\Phi_t\mathcal E)\le\frac1d+\varepsilon.
$$

Taking comparators approaching the infimum gives $F_e\le1/d+e(t)$. This is a one-use, fixed-logical-dimension statement. Unassisted quantum capacity requires a separate many-use analysis in infinite dimension; neither NPT nor this single-use error bound establishes it.

## Limitations to retain

- One noncompact free carrier on $L^2(\mathbb R)$, no confinement, loss or additional spatial degrees of freedom.
- The reference-energy operator $(P^2+Q^2)/2$ measures packet preparation; it is not the Hamiltonian of the noisy dynamics.
- Environmental Brownian trajectories are unobserved and cannot be postselected or used as decoder side information.
- The exact/operational distinction already exists for simpler dephasing models. The new case is the **specific sharp nonlinear boundary, singular Gaussian comparison, and cubic all-input decay order**, not a general discovery that approximate and exact EB differ.
- The fixed TMSV result may rely on extremely small tails. No fixed-quality storage, positive capacity, optimal cubic coefficient, finite-spin transfer, or universal theorem for arbitrary nonlinear reservoirs is claimed.
