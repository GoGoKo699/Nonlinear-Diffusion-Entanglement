# Normal semigroup, resources, and the theorem contract

## Model

Let $\mathcal H=L^2(\mathbb R)$ and let $Q,P$ be the standard Schrödinger pair $[Q,P]=iI$ on a common core. Put $H=P^2/2$. The *normal random-unitary semigroup* $\Phi_t$ has the formal generator

$$
\mathcal L=-i\omega\,\operatorname{ad}_H
-D\,\operatorname{ad}_Q^2-\kappa\,\operatorname{ad}_H^2
-\eta\,\operatorname{ad}_P^2,
\quad D,\kappa>0,\quad\eta\ge0,\quad\omega\in\mathbb R.
$$

To avoid unjustified manipulations of unbounded Lindblad operators, define the channel as the expectation of the unitary stochastic evolution whose independent Stratonovich Hamiltonian increments are

$$
\omega H\,dt+\sqrt{2\kappa}\,H\circ dB_t
+\sqrt{2D}\,Q\circ dW_t+\sqrt{2\eta}\,P\circ dZ_t.
$$

Equivalently use the exact conditional Gaussian displacement integral in [the next chapter](conditional_gaussian.md). All unitaries are defined by Weyl displacements and shears on $\mathcal H$; their averaged action on normal trace-class states is CPTP, and independent increments establish the semigroup. On a suitable Schwartz finite-rank core it has the displayed formal generator. There is no harmonic trapping Hamiltonian in the evolution.

The environment and all Brownian paths are unobserved. No environment outcome, noiseless quantum bypass, or intermediate correction is granted. The reference system in the channel norm is arbitrary.

## Operational definitions

$\Phi$ is **entanglement breaking (EB)** when $(\Phi\otimes\mathrm{id}_R)(\rho_{SR})$ is separable for every normal joint state and every reference; separable means the trace-norm closed convex hull of product states. It is **PPT-inducing** when every such output remains positive under reference partial transpose. EB implies PPT-inducing.

The energy-unconstrained distance to EB is

$$
e(t)=\inf_{\Psi\in\mathrm{EB}}
\frac12\|\Phi_t-\Psi\|_\diamond.
$$

The diamond norm includes arbitrary reference dimensions and no energy cutoff. To check explicit finite-energy witnesses we use the reference oscillator cost

$$ H_{\rm ref}=(Q^2+P^2)/2, $$

which is **not** the dynamical free Hamiltonian $H=P^2/2$.

## Exact statements

**A. Sharp EB and PPT threshold:** For $\kappa>0$, the first EB time equals $(2\sqrt{D\eta})^{-1}$ when $\eta>0$, and is infinite when $\eta=0$. At and after the finite threshold the channel is EB; at every strictly earlier time a finite-$H_{\rm ref}$-energy state with a two-dimensional reference has NPT output. [Proof](exact_threshold.md).

**B. Unconstrained cubic-law proximity:** For $\eta=0$, $D=\kappa=1$ and fixed finite $\omega$, for all $t\ge1$,

$$
\frac{c_*}{1+\omega^2}e^{-4t^3-\omega^2t/2}
\le e(t)\le
\min\left\{1,\sqrt{\frac{8t^3}{1-e^{-8t^3}}}\,e^{-t^3}\right\},
$$

where $c_*=0.02153222609588753\ldots>0$ is given in elementary exact form in [the proof](cubic_distance.md). The general fixed-rate logarithmic order is $\Theta(D^2\kappa t^3)$, not an exact optimized exponent coefficient.

**C. Fixed finite-energy input:** For $\eta=0$, every fixed two-mode squeezed vacuum with nonzero finite squeezing has NPT output after applying $\Phi_t$ to only one mode, for all finite $t>0$. This is qualitative and need not give useful quantum memory. [Proof](fixed_input.md).

**Gaussian comparison, not a $\kappa>0$ theorem:** For $\kappa=0$, the threshold is the first positive root of $4D\eta t^2+(D^2\omega^2/3)t^4=1$; it is infinite when the expression never reaches one. [Derivation](interpretation.md).

These results neither imply positive quantum capacity nor generalize automatically to other nonlinear Lindblad generators. The input-energy statement in A means every *particular witness* has finite energy; it is not a uniform energy bound over all times.
